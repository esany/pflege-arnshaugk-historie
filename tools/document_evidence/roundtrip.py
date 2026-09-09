#!/usr/bin/env python3
"""Reproduce neutral page-space locators against one fingerprinted PDF instance.

PyMuPDF is deliberately an adapter.  The manifest owns no PyMuPDF object IDs and
stores only normalized page-space coordinates plus explicit scientific relations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


class EvidenceError(ValueError):
    """The instance or manifest violates the bounded #51 contract."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_manifest(data)
    return data


def validate_manifest(data: dict[str, Any]) -> None:
    if data.get("schema_version") != "0.1":
        raise EvidenceError("unsupported schema_version")
    instance = data.get("instance", {})
    required_instance = {
        "instance_id", "representation_id", "source_id", "direct_file_url",
        "sha256", "byte_size", "page_count",
    }
    missing = sorted(required_instance - set(instance))
    if missing:
        raise EvidenceError(f"instance fields missing: {', '.join(missing)}")
    if not data.get("findings") or not data.get("gold_cases"):
        raise EvidenceError("at least one finding and one gold case are required")

    if type(instance["page_count"]) is not int or instance["page_count"] <= 0:
        raise EvidenceError("invalid page_count")
    finding_ids = {item["finding_id"] for item in data["findings"]}
    locator_ids: set[str] = set()
    for case in data["gold_cases"]:
        if case["finding_id"] not in finding_ids:
            raise EvidenceError(f"unknown finding_id in {case['case_id']}")
        if not case.get("locators"):
            raise EvidenceError(f"{case['case_id']} has no locators")
        for locator in case["locators"]:
            locator_id = locator["locator_id"]
            if locator_id in locator_ids:
                raise EvidenceError(f"duplicate locator_id: {locator_id}")
            locator_ids.add(locator_id)
            if locator.get("coordinate_system") != "normalized-page-space-v0.1":
                raise EvidenceError(f"tool-specific/unknown coordinate system: {locator_id}")
            index = locator.get("pdf_page_index")
            if type(index) is not int or not 0 <= index < instance["page_count"]:
                raise EvidenceError(f"invalid pdf_page_index: {locator_id}")
            geometry = locator.get("page_geometry_points")
            if (not isinstance(geometry, list) or len(geometry) != 2
                    or any(type(v) not in (int, float) or not math.isfinite(v) or v <= 0 for v in geometry)):
                raise EvidenceError(f"invalid page geometry: {locator_id}")
            bbox = locator.get("bbox")
            if not isinstance(bbox, list) or len(bbox) != 4:
                raise EvidenceError(f"invalid bbox: {locator_id}")
            x0, y0, x1, y1 = bbox
            if any(type(v) not in (int, float) or not math.isfinite(v) for v in bbox) or not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
                raise EvidenceError(f"bbox outside normalized page: {locator_id}")
            if locator.get("printed_page", {}).get("status") not in {
                "resolved", "absent", "ambiguous", "unresolved"
            }:
                raise EvidenceError(f"invalid printed-page state: {locator_id}")

    for relation in data.get("relations", []):
        if relation["from_locator_id"] not in locator_ids or relation["to_locator_id"] not in locator_ids:
            raise EvidenceError(f"relation references unknown locator: {relation['relation_id']}")
        if relation["authority"] not in {"human-curated", "parser-heuristic"}:
            raise EvidenceError(f"invalid relation authority: {relation['relation_id']}")
        if relation.get("research_critical"):
            if relation.get("evaluation") not in {"correct", "wrong", "unresolved"}:
                raise EvidenceError(f"research-critical relation lacks valid evaluation: {relation['relation_id']}")
        if relation["authority"] == "parser-heuristic" and relation.get("evaluation") not in {"correct", "wrong", "unresolved"}:
            raise EvidenceError(f"parser relation lacks evaluation: {relation['relation_id']}")


def normalized_to_page(bbox: list[float], width: float, height: float) -> tuple[float, float, float, float]:
    x0, y0, x1, y1 = bbox
    return x0 * width, y0 * height, x1 * width, y1 * height


def run(manifest_path: Path, pdf_path: Path, output_dir: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    instance = manifest["instance"]
    actual_hash = sha256_file(pdf_path)
    if actual_hash != instance["sha256"]:
        raise EvidenceError(f"instance fingerprint mismatch: {actual_hash}")
    if pdf_path.stat().st_size != instance["byte_size"]:
        raise EvidenceError("instance byte_size mismatch")

    try:
        import pymupdf
    except ImportError as exc:  # pragma: no cover - environment-dependent message
        raise EvidenceError("PyMuPDF is required only for the mechanical adapter run") from exc

    document = pymupdf.open(pdf_path)
    if document.page_count != instance["page_count"]:
        raise EvidenceError("instance page_count mismatch")
    output_dir.mkdir(parents=True, exist_ok=True)
    rendered: list[dict[str, Any]] = []

    for case in manifest["gold_cases"]:
        for locator in case["locators"]:
            page = document[locator["pdf_page_index"]]
            expected = locator["page_geometry_points"]
            actual = [page.rect.width, page.rect.height]
            if any(abs(a - b) > 0.02 for a, b in zip(actual, expected)):
                raise EvidenceError(f"page geometry mismatch: {locator['locator_id']}")
            page_bbox = normalized_to_page(locator["bbox"], *actual)
            clip = pymupdf.Rect(page_bbox)
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(2, 2), clip=clip, alpha=False)
            payload = pixmap.tobytes("png")
            target = output_dir / f"{locator['locator_id']}.png"
            target.write_bytes(payload)
            rendered.append({
                "case_id": case["case_id"],
                "finding_id": case["finding_id"],
                "locator_id": locator["locator_id"],
                "role": locator["role"],
                "pdf_page_index": locator["pdf_page_index"],
                "printed_page": locator["printed_page"],
                "scope_state": locator.get("scope_state", "unspecified"),
                "scope_note": locator.get("scope_note"),
                "page_bbox_points": [round(value, 4) for value in page_bbox],
                "crop_sha256": hashlib.sha256(payload).hexdigest(),
            })

    critical_relations = [r for r in manifest.get("relations", []) if r.get("research_critical")]
    parser_relations = [r for r in critical_relations if r["authority"] == "parser-heuristic"]
    wrong = [r["relation_id"] for r in critical_relations if r["evaluation"] == "wrong"]
    unresolved = [r["relation_id"] for r in critical_relations if r["evaluation"] == "unresolved"]
    report = {
        "schema_version": "0.1",
        "result": "pass" if not wrong else "fail",
        "result_scope": "mechanical reproduction and declared evaluations only; not semantic or human-gold validation",
        "semantic_validation": "not-performed",
        "gold_review": manifest.get("gold_review", {"status": "unresolved"}),
        "findings": manifest["findings"],
        "instance_id": instance["instance_id"],
        "instance_sha256": actual_hash,
        "adapter": {"name": "PyMuPDF", "version": pymupdf.VersionBind, "authority": "mechanical-only"},
        "rendered_locators": rendered,
        "research_critical_relations": len(critical_relations),
        "research_critical_parser_relations": len(parser_relations),
        "silent_error_count": len(wrong),
        "silent_error_relation_ids": wrong,
        "unresolved_relation_ids": unresolved,
    }
    (output_dir / "roundtrip-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    try:
        report = run(args.manifest, args.pdf, args.output_dir)
    except EvidenceError as exc:
        parser.exit(1, f"FAIL: {exc}\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["result"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
