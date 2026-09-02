"""Formal checks for the Requirement -> Enforcement technical projection."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tools.operational.core import load_json, read_text, schema_violations


@dataclass(frozen=True)
class EnforcementFinding:
    rule_id: str
    severity: str
    message: str
    requirement_id: str | None = None
    source: str | None = None


def validate_enforcement_map(root: Path, requirement_ids: set[str]) -> list[EnforcementFinding]:
    source = root / "tools/operational/enforcement-map.json"
    schema = load_json(root / "tools/operational/enforcement-map.schema.json")
    data = load_json(source)
    findings = [
        EnforcementFinding("OPM001", "error", f"Schema violation at {v.location}: {v.message}", v.item_id, str(source))
        for v in schema_violations(schema, data, collection_key="mappings")
    ]

    rules = data.get("rules", [])
    rule_ids = [rule.get("id") for rule in rules if rule.get("id")]
    if len(rule_ids) != len(set(rule_ids)):
        findings.append(EnforcementFinding("OPM002", "error", "Rule catalogue contains duplicate IDs", source=str(source)))

    mapping_ids: set[str] = set()
    known_rules = set(rule_ids)
    for mapping in data.get("mappings", []):
        req_id = mapping.get("requirement_id")
        if req_id in mapping_ids:
            findings.append(EnforcementFinding("OPM003", "error", "Requirement appears more than once in enforcement map", req_id, str(source)))
        mapping_ids.add(req_id)
        if req_id not in requirement_ids:
            findings.append(EnforcementFinding("OPM004", "error", "Enforcement map references an unknown/non-accepted requirement", req_id, str(source)))

        for item in mapping.get("enforcement", []):
            for rule_id in item.get("rule_refs", []):
                if rule_id not in known_rules:
                    findings.append(EnforcementFinding("OPM005", "error", f"Unknown rule reference: {rule_id}", req_id, str(source)))
            if item.get("class") in {"mixed", "scholarly", "procedural"} and not mapping.get("human_or_specialist_review_refs"):
                findings.append(EnforcementFinding("OPM006", "error", "Non-deterministic enforcement class requires an explicit human/domain/specialist review boundary", req_id, str(source)))

    for rule in rules:
        for fixture_ref in rule.get("fixture_refs", []):
            file_ref, _, selector = fixture_ref.partition("::")
            fixture_path = root / file_ref
            if not fixture_path.is_file():
                findings.append(EnforcementFinding("OPM007", "error", f"Fixture file does not exist: {file_ref}", source=str(source)))
            elif selector and selector not in read_text(fixture_path):
                findings.append(EnforcementFinding("OPM007", "error", f"Fixture selector does not exist: {fixture_ref}", source=str(source)))
    return findings
