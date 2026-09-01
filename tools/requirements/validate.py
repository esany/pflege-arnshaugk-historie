#!/usr/bin/env python3
"""Deterministic Requirements Assurance Harness for Histo-Orla.

This tool validates formal requirements conformance only. It does not judge
historical truth, domain-method quality, or scholarly sufficiency.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - explicit operational error path
    Draft202012Validator = None


REQ_HEADING_RE = re.compile(r"^#{2,4}\s+(REQ-[A-Z]+-[0-9]{3})\s+[–-]\s+(.+?)\s*$")
COVERAGE_ROW_RE = re.compile(
    r"^\|\s*(REQ-[A-Z]+-[0-9]{3})\s*\|[^|]*\|\s*([^|]+?)\s*\|"
)

ACTIVE_STRUCTURE_STATUSES = {
    "in-progress",
    "implemented",
    "verified",
    "partial",
    "blocked",
    "owner-deferred",
}

ALLOWED_EXIT_STATUSES = {
    "not-started",
    "in-progress",
    "implemented",
    "verified",
    "partial",
    "blocked",
    "research-needed",
    "owner-deferred",
}


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str  # error | warning
    message: str
    requirement_id: str | None = None
    source: str | None = None


class HarnessError(RuntimeError):
    pass


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise HarnessError(f"Cannot read {path}: {exc}") from exc


def load_json(path: Path):
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise HarnessError(f"Invalid JSON in {path}: {exc}") from exc


def extract_requirement_occurrences(paths: Iterable[Path]) -> dict[str, list[str]]:
    occurrences: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        for line_no, line in enumerate(read_text(path).splitlines(), start=1):
            match = REQ_HEADING_RE.match(line)
            if match:
                req_id = match.group(1)
                occurrences[req_id].append(f"{path}:{line_no}")
    return dict(occurrences)


def parse_coverage(path: Path) -> tuple[dict[str, str], list[Finding]]:
    statuses: dict[str, str] = {}
    findings: list[Finding] = []
    for line_no, line in enumerate(read_text(path).splitlines(), start=1):
        match = COVERAGE_ROW_RE.match(line)
        if not match:
            continue
        req_id, status = match.group(1), match.group(2).strip()
        if req_id in statuses:
            findings.append(
                Finding(
                    "REQ013",
                    "error",
                    "Requirement appears more than once in delivery coverage ledger",
                    req_id,
                    f"{path}:{line_no}",
                )
            )
        statuses[req_id] = status
        if status not in ALLOWED_EXIT_STATUSES:
            findings.append(
                Finding(
                    "REQ014",
                    "error",
                    f"Unknown delivery status: {status}",
                    req_id,
                    f"{path}:{line_no}",
                )
            )
    return statuses, findings


def validate_schema(schema: dict, data: dict, source: Path) -> list[Finding]:
    if Draft202012Validator is None:
        raise HarnessError(
            "Python package 'jsonschema' is required. Install with "
            "'python -m pip install -r tools/requirements/requirements.txt'."
        )
    validator = Draft202012Validator(schema)
    findings: list[Finding] = []
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        req_id = None
        path_parts = list(error.absolute_path)
        if len(path_parts) >= 2 and path_parts[0] == "records" and isinstance(path_parts[1], int):
            try:
                req_id = data["records"][path_parts[1]].get("id")
            except Exception:
                req_id = None
        location = "/".join(str(x) for x in path_parts) or "<root>"
        findings.append(
            Finding(
                "REQ006",
                "error",
                f"Schema violation at {location}: {error.message}",
                req_id,
                str(source),
            )
        )
    return findings


def find_requires_cycle(records_by_id: dict[str, dict]) -> list[list[str]]:
    graph: dict[str, list[str]] = defaultdict(list)
    for req_id, record in records_by_id.items():
        for relation in record.get("relations", []):
            if relation.get("type") == "requires":
                graph[req_id].append(relation.get("target"))

    state: dict[str, int] = {}  # 0/unseen, 1/visiting, 2/done
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(node: str) -> None:
        status = state.get(node, 0)
        if status == 2:
            return
        if status == 1:
            if node in stack:
                idx = stack.index(node)
                cycles.append(stack[idx:] + [node])
            return
        state[node] = 1
        stack.append(node)
        for target in graph.get(node, []):
            visit(target)
        stack.pop()
        state[node] = 2

    for node in sorted(graph):
        if state.get(node, 0) == 0:
            visit(node)
    return cycles


def run_checks(
    requirement_occurrences: dict[str, list[str]],
    coverage: dict[str, str],
    records_data: dict,
    records_source: Path,
) -> list[Finding]:
    findings: list[Finding] = []

    accepted_ids = set(requirement_occurrences)
    coverage_ids = set(coverage)

    # Duplicate requirement definitions.
    for req_id, locations in sorted(requirement_occurrences.items()):
        if len(locations) > 1:
            findings.append(
                Finding(
                    "REQ001",
                    "error",
                    "Requirement ID is defined multiple times: " + ", ".join(locations),
                    req_id,
                )
            )

    # Accepted requirements and delivery coverage must be the same set.
    for req_id in sorted(accepted_ids - coverage_ids):
        findings.append(
            Finding(
                "REQ002",
                "error",
                "Accepted requirement is missing from delivery coverage ledger",
                req_id,
            )
        )
    for req_id in sorted(coverage_ids - accepted_ids):
        findings.append(
            Finding(
                "REQ002",
                "error",
                "Delivery coverage contains an ID not defined in accepted requirements",
                req_id,
            )
        )

    records = records_data.get("records", [])
    records_by_id: dict[str, dict] = {}
    for record in records:
        req_id = record.get("id")
        if not req_id:
            continue
        if req_id in records_by_id:
            findings.append(
                Finding(
                    "REQ001",
                    "error",
                    "Structured QA record appears more than once",
                    req_id,
                    str(records_source),
                )
            )
        records_by_id[req_id] = record

    # Stale records and lifecycle owner.
    for req_id, record in sorted(records_by_id.items()):
        if req_id not in accepted_ids:
            findings.append(
                Finding(
                    "REQ012",
                    "error",
                    "Structured QA record points to an unknown/non-accepted requirement",
                    req_id,
                    str(records_source),
                )
            )
        if record.get("lifecycle_owner") != "#42":
            findings.append(
                Finding(
                    "REQ010",
                    "error",
                    "Accepted requirement lifecycle owner must be #42",
                    req_id,
                    str(records_source),
                )
            )

    # Incremental migration gate: active technical states require structured records.
    for req_id, status in sorted(coverage.items()):
        if status in ACTIVE_STRUCTURE_STATUSES and req_id not in records_by_id:
            findings.append(
                Finding(
                    "REQ007",
                    "error",
                    f"Delivery status '{status}' requires a structured QA record",
                    req_id,
                    str(records_source),
                )
            )
        elif status in {"not-started", "research-needed"} and req_id not in records_by_id:
            findings.append(
                Finding(
                    "REQ101",
                    "warning",
                    "Requirement has not yet been migrated to a structured QA record",
                    req_id,
                    str(records_source),
                )
            )

    # Cross-record references and authority boundaries.
    for req_id, record in sorted(records_by_id.items()):
        for field in (
            "domain_authority",
            "technical_delivery_competence",
            "verification_authority",
        ):
            values = record.get(field) or []
            if not values:
                findings.append(
                    Finding(
                        "REQ011",
                        "error",
                        f"Required authority/competence field is empty: {field}",
                        req_id,
                        str(records_source),
                    )
                )

        dep_status = record.get("dependency_status")
        if dep_status == "unresolved":
            findings.append(
                Finding(
                    "REQ102",
                    "warning",
                    "Dependency status is explicitly unresolved",
                    req_id,
                    str(records_source),
                )
            )

        for relation in record.get("relations", []):
            target = relation.get("target")
            relation_type = relation.get("type")
            if target not in accepted_ids:
                findings.append(
                    Finding(
                        "REQ003",
                        "error",
                        f"Relation '{relation_type}' targets unknown requirement {target}",
                        req_id,
                        str(records_source),
                    )
                )
            if target == req_id:
                findings.append(
                    Finding(
                        "REQ004",
                        "error",
                        f"Self-relation is not allowed for '{relation_type}'",
                        req_id,
                        str(records_source),
                    )
                )

        for interaction in record.get("interactions", []):
            target = interaction.get("with")
            if target not in accepted_ids:
                findings.append(
                    Finding(
                        "REQ003",
                        "error",
                        f"Interaction targets unknown requirement {target}",
                        req_id,
                        str(records_source),
                    )
                )
            if target == req_id:
                findings.append(
                    Finding(
                        "REQ004",
                        "error",
                        "Self-interaction is not allowed",
                        req_id,
                        str(records_source),
                    )
                )

        delivery_status = coverage.get(req_id)
        if delivery_status == "verified" and not record.get("verification_evidence_refs"):
            findings.append(
                Finding(
                    "REQ008",
                    "error",
                    "Verified requirement must reference verification evidence",
                    req_id,
                    str(records_source),
                )
            )
        if delivery_status == "owner-deferred" and not record.get("decision_refs"):
            findings.append(
                Finding(
                    "REQ009",
                    "error",
                    "owner-deferred requires an explicit owner decision reference",
                    req_id,
                    str(records_source),
                )
            )

    # Requires cycles are invalid for the formal prerequisite relation.
    for cycle in find_requires_cycle(records_by_id):
        findings.append(
            Finding(
                "REQ005",
                "error",
                "Cycle in 'requires' dependency graph: " + " -> ".join(cycle),
                cycle[0] if cycle else None,
                str(records_source),
            )
        )

    # conflicts_with should be symmetric once both sides are structured.
    conflicts: set[tuple[str, str]] = set()
    for req_id, record in records_by_id.items():
        for relation in record.get("relations", []):
            if relation.get("type") == "conflicts_with":
                conflicts.add((req_id, relation.get("target")))
    for source_id, target_id in sorted(conflicts):
        if target_id in records_by_id and (target_id, source_id) not in conflicts:
            findings.append(
                Finding(
                    "REQ103",
                    "warning",
                    f"conflicts_with is not symmetric in structured records: {target_id} does not point back",
                    source_id,
                    str(records_source),
                )
            )

    return findings


def render_text(findings: list[Finding]) -> str:
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    lines = [
        "Requirements Assurance Harness",
        "formal-conformance only; not scholarly/domain validation",
        f"errors={errors} warnings={warnings}",
    ]
    for finding in sorted(
        findings,
        key=lambda f: (0 if f.severity == "error" else 1, f.rule_id, f.requirement_id or ""),
    ):
        req = f" [{finding.requirement_id}]" if finding.requirement_id else ""
        source = f" ({finding.source})" if finding.source else ""
        lines.append(
            f"{finding.severity.upper()} {finding.rule_id}{req}: {finding.message}{source}"
        )
    if not findings:
        lines.append("PASS: no formal conformance findings")
    elif errors == 0:
        lines.append("PASS WITH WARNINGS: formal hard rules satisfied")
    else:
        lines.append("FAIL: formal hard-rule violations found")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args(argv)

    root = args.repo_root.resolve()
    requirements_files = [
        root / "docs/research/synthesis/requirements-baseline.md",
        root / "docs/research/synthesis/requirements-extensions.md",
    ]
    coverage_path = root / "docs/development/requirements-coverage.md"
    schema_path = root / "tools/requirements/requirement-record.schema.json"
    records_path = root / "tools/requirements/data/records.json"

    try:
        occurrences = extract_requirement_occurrences(requirements_files)
        coverage, findings = parse_coverage(coverage_path)
        schema = load_json(schema_path)
        records_data = load_json(records_path)
        findings.extend(validate_schema(schema, records_data, records_path))
        findings.extend(run_checks(occurrences, coverage, records_data, records_path))
    except HarnessError as exc:
        if args.json_output:
            print(json.dumps({"tool_error": str(exc)}, ensure_ascii=False, indent=2))
        else:
            print(f"TOOL ERROR: {exc}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.json_output:
        print(
            json.dumps(
                {
                    "formal_conformance": "fail" if errors else "pass",
                    "scholarly_validation": "not_assessed",
                    "errors": len(errors),
                    "warnings": len(warnings),
                    "findings": [asdict(f) for f in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render_text(findings))

    if errors:
        return 1
    if args.strict_warnings and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
