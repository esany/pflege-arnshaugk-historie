from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "validate.py"
spec = importlib.util.spec_from_file_location("requirements_validate", MODULE_PATH)
assert spec and spec.loader
rv = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = rv
spec.loader.exec_module(rv)


def record(req_id: str, **overrides):
    base = {
        "id": req_id,
        "source_file": "docs/research/synthesis/requirements-baseline.md",
        "lifecycle_owner": "#42",
        "domain_authority": ["Domain"],
        "technical_delivery_competence": ["RSE"],
        "verification_authority": ["Test"],
        "dependency_status": "none-known",
        "relations": [],
        "interactions": [],
        "criticality": "fundamental",
        "architecture_significance": "bounded",
        "verification_methods": ["deterministic-test"],
        "verification_evidence_refs": [],
        "decision_refs": [],
    }
    base.update(overrides)
    return base


def findings_for(occurrences, coverage, records):
    return rv.run_checks(
        occurrences,
        coverage,
        {"schema_version": "0.1", "records": records},
        Path("records.json"),
    )


def rules(findings):
    return [f.rule_id for f in findings]


class RequirementsHarnessTests(unittest.TestCase):
    def test_positive_formal_case(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        result = findings_for(occurrences, coverage, [record("REQ-A-001")])
        self.assertFalse([f for f in result if f.severity == "error"])

    def test_rejects_duplicate_requirement_definition(self):
        occurrences = {"REQ-A-001": ["a.md:1", "b.md:2"]}
        coverage = {"REQ-A-001": "not-started"}
        self.assertIn("REQ001", rules(findings_for(occurrences, coverage, [])))

    def test_rejects_accepted_id_missing_from_coverage(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        self.assertIn("REQ002", rules(findings_for(occurrences, {}, [])))

    def test_rejects_coverage_id_missing_from_requirements(self):
        coverage = {"REQ-A-001": "not-started"}
        self.assertIn("REQ002", rules(findings_for({}, coverage, [])))

    def test_rejects_stale_structured_record(self):
        self.assertIn(
            "REQ012",
            rules(findings_for({}, {}, [record("REQ-A-001")])),
        )

    def test_rejects_active_requirement_without_structured_record(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        self.assertIn("REQ007", rules(findings_for(occurrences, coverage, [])))

    def test_rejects_unknown_dependency_target(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        rec = record(
            "REQ-A-001",
            dependency_status="known",
            relations=[{"type": "requires", "target": "REQ-X-999"}],
        )
        self.assertIn("REQ003", rules(findings_for(occurrences, coverage, [rec])))

    def test_rejects_self_dependency(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        rec = record(
            "REQ-A-001",
            dependency_status="known",
            relations=[{"type": "requires", "target": "REQ-A-001"}],
        )
        self.assertIn("REQ004", rules(findings_for(occurrences, coverage, [rec])))

    def test_rejects_requires_cycle(self):
        occurrences = {
            "REQ-A-001": ["a.md:1"],
            "REQ-B-001": ["b.md:1"],
        }
        coverage = {
            "REQ-A-001": "in-progress",
            "REQ-B-001": "in-progress",
        }
        a = record(
            "REQ-A-001",
            dependency_status="known",
            relations=[{"type": "requires", "target": "REQ-B-001"}],
        )
        b = record(
            "REQ-B-001",
            dependency_status="known",
            relations=[{"type": "requires", "target": "REQ-A-001"}],
        )
        self.assertIn("REQ005", rules(findings_for(occurrences, coverage, [a, b])))

    def test_rejects_verified_without_verification_evidence(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "verified"}
        self.assertIn(
            "REQ008",
            rules(findings_for(occurrences, coverage, [record("REQ-A-001")])),
        )

    def test_accepts_verified_with_verification_evidence(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "verified"}
        rec = record("REQ-A-001", verification_evidence_refs=["tests/test_a.py::test_ok"])
        result = findings_for(occurrences, coverage, [rec])
        self.assertNotIn("REQ008", rules(result))

    def test_rejects_owner_deferred_without_decision(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "owner-deferred"}
        self.assertIn(
            "REQ009",
            rules(findings_for(occurrences, coverage, [record("REQ-A-001")])),
        )

    def test_rejects_missing_authority(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        rec = record("REQ-A-001", domain_authority=[])
        self.assertIn("REQ011", rules(findings_for(occurrences, coverage, [rec])))

    def test_warns_for_unresolved_dependency_state(self):
        occurrences = {"REQ-A-001": ["a.md:1"]}
        coverage = {"REQ-A-001": "in-progress"}
        rec = record("REQ-A-001", dependency_status="unresolved")
        result = findings_for(occurrences, coverage, [rec])
        self.assertIn("REQ102", rules(result))
        self.assertFalse([f for f in result if f.rule_id == "REQ102" and f.severity == "error"])


if __name__ == "__main__":
    unittest.main()
