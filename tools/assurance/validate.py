#!/usr/bin/env python3
"""Histo-Orla Value / Decision / Delivery / Feedback assurance validator.

This validator checks formal traceability and governance conformance only.
It does not judge scholarly truth, requirement sufficiency, user meaning, or
whether a technical decision is substantively the best option.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    Draft202012Validator = None


REQ_RE = re.compile(r"^#{2,4}\s+(REQ-[A-Z]+-[0-9]{3})\s+[–-]\s+", re.MULTILINE)
DRIVER_RE = re.compile(r"\b([GNP]-[0-9]{3})\b")
COVERAGE_ROW_RE = re.compile(r"^\|\s*(REQ-[A-Z]+-[0-9]{3})\s*\|[^|]*\|\s*([^|]+?)\s*\|", re.MULTILINE)


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    message: str
    record_id: str | None = None
    source: str | None = None


class AssuranceError(RuntimeError):
    pass


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise AssuranceError(f"Cannot read {path}: {exc}") from exc


def load_json(path: Path):
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise AssuranceError(f"Invalid JSON in {path}: {exc}") from exc


def canonical_requirement_ids(root: Path) -> set[str]:
    ids: set[str] = set()
    for rel in (
        "docs/research/synthesis/requirements-baseline.md",
        "docs/research/synthesis/requirements-extensions.md",
    ):
        ids.update(REQ_RE.findall(read_text(root / rel)))
    return ids


def canonical_driver_ids(root: Path) -> set[str]:
    return set(DRIVER_RE.findall(read_text(root / "docs/research/discovery/problem-baseline.md")))


def coverage_statuses(root: Path) -> dict[str, str]:
    text = read_text(root / "docs/development/requirements-coverage.md")
    return {req: status.strip() for req, status in COVERAGE_ROW_RE.findall(text)}


def schema_findings(schema: dict, data: dict, source: Path) -> list[Finding]:
    if Draft202012Validator is None:
        raise AssuranceError(
            "Python package 'jsonschema' is required; install tools/requirements/requirements.txt"
        )
    out: list[Finding] = []
    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        record_id = None
        parts = list(error.absolute_path)
        if len(parts) >= 2 and parts[0] == "records" and isinstance(parts[1], int):
            try:
                record_id = data["records"][parts[1]].get("id")
            except Exception:
                pass
        loc = "/".join(str(x) for x in parts) or "<root>"
        out.append(Finding("VDD001", "error", f"Schema violation at {loc}: {error.message}", record_id, str(source)))
    return out


def matching_implementation_records(path: str, records: list[dict]) -> list[str]:
    matches: list[str] = []
    for rec in records:
        if rec.get("kind") != "implementation":
            continue
        # Only an active/in-flight implementation may justify a new code change.
        # A verified historical implementation cannot permanently whitelist a path.
        if rec.get("status") not in {"active", "implemented"}:
            continue
        for pattern in rec.get("implementation_files", []):
            if fnmatch.fnmatch(path, pattern):
                matches.append(rec["id"])
                break
    return matches


def is_controlled(path: str, policy: dict) -> bool:
    if any(fnmatch.fnmatch(path, p) for p in policy.get("changed_path_exemptions", [])):
        return False
    return any(fnmatch.fnmatch(path, p) for p in policy.get("controlled_technical_paths", []))


def changed_files(root: Path, changed_from: str | None) -> list[str]:
    if not changed_from:
        return []
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"{changed_from}..HEAD"],
            cwd=root,
            text=True,
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise AssuranceError(f"Cannot compute changed files from {changed_from}: {exc.stderr.strip()}") from exc
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def run_checks(
    records_data: dict,
    governance: dict,
    policy: dict,
    requirement_ids: set[str],
    driver_ids: set[str],
    coverage: dict[str, str],
    requirement_records: dict,
    changed: list[str],
) -> list[Finding]:
    findings: list[Finding] = []
    records = records_data.get("records", [])

    by_id: dict[str, dict] = {}
    for rec in records:
        rid = rec.get("id")
        if not rid:
            continue
        if rid in by_id:
            findings.append(Finding("VDD002", "error", "Duplicate trace record ID", rid))
        by_id[rid] = rec

    governance_ids = {entry.get("id") for entry in governance.get("entries", [])}
    global_governance = set(policy.get("global_governance_refs", []))
    negative_outcomes = set(policy.get("negative_feedback_outcomes", []))

    for rec in records:
        rid = rec.get("id", "<unknown>")
        kind = rec.get("kind")

        expected_prefix = {"decision": "DEC-", "implementation": "IMP-", "feedback": "FB-"}.get(kind)
        if expected_prefix and not rid.startswith(expected_prefix):
            findings.append(Finding("VDD003", "error", f"Record kind {kind} requires ID prefix {expected_prefix}", rid))

        for req in rec.get("requirement_refs", []):
            if req not in requirement_ids:
                findings.append(Finding("VDD004", "error", f"Unknown requirement reference: {req}", rid))

        for driver in rec.get("driver_refs", []):
            if driver not in driver_ids:
                findings.append(Finding("VDD005", "error", f"Unknown Goal/Need/Pain driver reference: {driver}", rid))

        for gov in rec.get("governance_refs", []):
            if gov not in governance_ids:
                findings.append(Finding("VDD006", "error", f"Unknown governance reference: {gov}", rid))

        if kind in {"decision", "implementation"}:
            missing = global_governance - set(rec.get("governance_refs", []))
            if missing:
                findings.append(Finding("VDD007", "error", "Missing global governance refs: " + ", ".join(sorted(missing)), rid))
            if not rec.get("requirement_refs"):
                findings.append(Finding("VDD008", "error", "Technical decision/implementation has no accepted Requirement reference", rid))
            if not rec.get("driver_refs"):
                findings.append(Finding("VDD009", "error", "Technical decision/implementation has no Goal/Need/Pain driver", rid))

        if kind == "implementation":
            for decision in rec.get("decision_refs", []):
                target = by_id.get(decision)
                if target is None or target.get("kind") != "decision":
                    findings.append(Finding("VDD010", "error", f"Implementation references unknown/non-decision record: {decision}", rid))
            if rec.get("materiality") != "mechanical" and not rec.get("decision_refs") and not rec.get("decision_not_required_reason"):
                findings.append(Finding("VDD011", "error", "Non-mechanical implementation needs decision_ref or decision_not_required_reason", rid))
            if rec.get("status") in {"implemented", "verified"} and not rec.get("implementation_files"):
                findings.append(Finding("VDD012", "error", "Implemented/verified record has no implementation_files", rid))
            if rec.get("status") == "verified" and not rec.get("verification_refs"):
                findings.append(Finding("VDD013", "error", "Verified implementation has no verification_refs", rid))

        if kind == "feedback":
            for imp in rec.get("implementation_refs", []):
                target = by_id.get(imp)
                if target is None or target.get("kind") != "implementation":
                    findings.append(Finding("VDD014", "error", f"Feedback references unknown/non-implementation record: {imp}", rid))
            if rec.get("feedback_outcome") in negative_outcomes and not rec.get("requires_delta"):
                findings.append(Finding("VDD015", "error", "Negative/material feedback outcome must set requires_delta=true", rid))
            if rec.get("requires_delta") and not rec.get("delta_refs"):
                findings.append(Finding("VDD016", "error", "Feedback requires delta but has no delta_refs", rid))

    # Owner-workflow acceptance is a real user/owner signal, not a technical self-test.
    feedback_by_req: dict[str, list[dict]] = {}
    for rec in records:
        if rec.get("kind") == "feedback":
            for req in rec.get("requirement_refs", []):
                feedback_by_req.setdefault(req, []).append(rec)
    for req_id, req_record in requirement_records.items():
        if coverage.get(req_id) != "verified":
            continue
        if "owner-workflow-acceptance" in req_record.get("verification_methods", []):
            acceptable = [
                rec for rec in feedback_by_req.get(req_id, [])
                if rec.get("feedback_outcome") in {"confirms", "no-change"} and rec.get("status") in {"resolved", "verified"}
            ]
            if not acceptable:
                findings.append(Finding("VDD017", "error", "Requirement verified with owner-workflow-acceptance but no resolved confirming feedback record", req_id))

    # Changed-code guard.
    for path in changed:
        if not is_controlled(path, policy):
            continue
        matches = matching_implementation_records(path, records)
        if not matches:
            findings.append(Finding("VDD018", "error", "Changed controlled technical path is not covered by an active/implemented Implementation Record", source=path))

    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--strict-warnings", action="store_true")
    parser.add_argument("--changed-from", default=None, help="Git ref/SHA used for changed-code traceability guard")
    args = parser.parse_args(argv)

    root = repo_root()
    try:
        schema_path = root / "tools/assurance/trace-record.schema.json"
        records_path = root / "tools/assurance/data/trace-records.json"
        schema = load_json(schema_path)
        records_data = load_json(records_path)
        governance = load_json(root / "tools/assurance/governance-registry.json")
        policy = load_json(root / "tools/assurance/policy.json")
        requirement_ids = canonical_requirement_ids(root)
        driver_ids = canonical_driver_ids(root)
        coverage = coverage_statuses(root)
        requirement_records_data = load_json(root / "tools/requirements/data/records.json")
        requirement_records = {r["id"]: r for r in requirement_records_data.get("records", [])}
        changed = changed_files(root, args.changed_from)

        findings = schema_findings(schema, records_data, records_path)
        findings.extend(run_checks(
            records_data,
            governance,
            policy,
            requirement_ids,
            driver_ids,
            coverage,
            requirement_records,
            changed,
        ))
    except AssuranceError as exc:
        print(f"ASSURANCE TOOL ERROR: {exc}", file=sys.stderr)
        return 2

    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.as_json:
        print(json.dumps({
            "formal_scope": "value/decision/delivery/feedback traceability only",
            "errors": len(errors),
            "warnings": len(warnings),
            "findings": [asdict(f) for f in findings],
        }, ensure_ascii=False, indent=2))
    else:
        print("Histo-Orla Project Assurance Spine")
        print("formal traceability/conformance only; not scholarly truth or user-meaning validation")
        print(f"errors={len(errors)} warnings={len(warnings)}")
        for f in findings:
            rid = f" [{f.record_id}]" if f.record_id else ""
            source = f" ({f.source})" if f.source else ""
            print(f"{f.severity.upper()} {f.rule_id}{rid}: {f.message}{source}")
        if not errors:
            print("PASS: implemented formal traceability rules satisfied")

    if errors:
        return 1
    if warnings and args.strict_warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
