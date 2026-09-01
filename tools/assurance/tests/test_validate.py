from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "validate.py"
spec = importlib.util.spec_from_file_location("project_assurance_validate", MODULE_PATH)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


REQS = {"REQ-A-001", "REQ-B-001"}
DRIVERS = {"G-001", "N-001", "P-001"}
GOV = {
    "entries": [
        {"id": "GOV-AGENTS"},
        {"id": "GOV-NONREG"},
    ]
}
POLICY = {
    "global_governance_refs": ["GOV-AGENTS", "GOV-NONREG"],
    "controlled_technical_paths": ["src/**", "tools/**"],
    "changed_path_exemptions": ["tools/assurance/data/trace-records.json"],
    "negative_feedback_outcomes": ["pain-persists", "regression", "new-pain", "new-need", "requirement-change"],
}


def decision(rid="DEC-A", **kw):
    base = {
        "id": rid,
        "kind": "decision",
        "status": "active",
        "materiality": "local-reversible",
        "requirement_refs": ["REQ-A-001"],
        "driver_refs": ["G-001"],
        "governance_refs": ["GOV-AGENTS", "GOV-NONREG"],
        "decision_refs": [],
        "implementation_refs": [],
        "implementation_files": [],
        "verification_refs": [],
        "feedback_outcome": None,
        "requires_delta": False,
        "delta_refs": [],
        "notes": "",
    }
    base.update(kw)
    return base


def implementation(rid="IMP-A", **kw):
    base = {
        "id": rid,
        "kind": "implementation",
        "status": "implemented",
        "materiality": "local-reversible",
        "requirement_refs": ["REQ-A-001"],
        "driver_refs": ["G-001"],
        "governance_refs": ["GOV-AGENTS", "GOV-NONREG"],
        "decision_refs": ["DEC-A"],
        "implementation_refs": [],
        "implementation_files": ["src/a.py"],
        "verification_refs": [],
        "feedback_outcome": None,
        "requires_delta": False,
        "delta_refs": [],
        "notes": "",
    }
    base.update(kw)
    return base


def feedback(rid="FB-A", **kw):
    base = {
        "id": rid,
        "kind": "feedback",
        "status": "open",
        "materiality": "material",
        "requirement_refs": ["REQ-A-001"],
        "driver_refs": ["P-001"],
        "governance_refs": [],
        "decision_refs": [],
        "implementation_refs": ["IMP-A"],
        "implementation_files": [],
        "verification_refs": [],
        "source_ref": "owner-feedback:test",
        "feedback_outcome": "no-change",
        "requires_delta": False,
        "delta_refs": [],
        "notes": "",
    }
    base.update(kw)
    return base


def run(records, changed=None, coverage=None, requirement_records=None):
    return mod.run_checks(
        {"schema_version": "0.1", "records": records},
        GOV,
        POLICY,
        REQS,
        DRIVERS,
        coverage or {},
        requirement_records or {},
        changed or [],
    )


def rule_ids(findings):
    return [f.rule_id for f in findings]


class AssuranceSpineTests(unittest.TestCase):
    def test_positive_decision_implementation_feedback_chain(self):
        findings = run([decision(), implementation(), feedback()])
        self.assertFalse([f for f in findings if f.severity == "error"])

    def test_unknown_requirement_fails(self):
        rec = decision(requirement_refs=["REQ-X-999"])
        self.assertIn("VDD004", rule_ids(run([rec])))

    def test_unknown_driver_fails(self):
        rec = decision(driver_refs=["N-999"])
        self.assertIn("VDD005", rule_ids(run([rec])))

    def test_missing_global_governance_fails(self):
        rec = decision(governance_refs=["GOV-AGENTS"])
        self.assertIn("VDD007", rule_ids(run([rec])))

    def test_technical_record_without_driver_fails(self):
        rec = decision(driver_refs=[])
        self.assertIn("VDD009", rule_ids(run([rec])))

    def test_implementation_unknown_decision_fails(self):
        rec = implementation(decision_refs=["DEC-NOT-THERE"])
        self.assertIn("VDD010", rule_ids(run([rec])))

    def test_nonmechanical_implementation_without_decision_fails(self):
        rec = implementation(decision_refs=[])
        self.assertIn("VDD011", rule_ids(run([rec])))

    def test_verified_implementation_without_verification_fails(self):
        rec = implementation(status="verified", verification_refs=[])
        self.assertIn("VDD013", rule_ids(run([decision(), rec])))

    def test_negative_feedback_without_delta_flag_fails(self):
        fb = feedback(feedback_outcome="pain-persists", requires_delta=False)
        self.assertIn("VDD015", rule_ids(run([decision(), implementation(), fb])))

    def test_feedback_unknown_implementation_fails(self):
        fb = feedback(implementation_refs=["IMP-NOT-THERE"])
        self.assertIn("VDD014", rule_ids(run([fb])))

    def test_changed_code_without_active_implementation_record_fails(self):
        self.assertIn("VDD018", rule_ids(run([decision()], changed=["src/new.py"])))

    def test_changed_code_is_covered_by_inflight_implementation(self):
        findings = run([decision(), implementation(status="implemented")], changed=["src/a.py"])
        self.assertNotIn("VDD018", rule_ids(findings))

    def test_verified_historical_implementation_does_not_permanently_whitelist_path(self):
        imp = implementation(status="verified", verification_refs=["test:ok"])
        self.assertIn("VDD018", rule_ids(run([decision(), imp], changed=["src/a.py"])))

    def test_owner_workflow_acceptance_needs_resolved_confirming_feedback(self):
        req_records = {
            "REQ-A-001": {
                "id": "REQ-A-001",
                "verification_methods": ["owner-workflow-acceptance"],
            }
        }
        findings = run(
            [decision(), implementation(status="verified", verification_refs=["test:ok"])],
            coverage={"REQ-A-001": "verified"},
            requirement_records=req_records,
        )
        self.assertIn("VDD017", rule_ids(findings))

    def test_owner_workflow_acceptance_passes_with_resolved_feedback(self):
        req_records = {
            "REQ-A-001": {
                "id": "REQ-A-001",
                "verification_methods": ["owner-workflow-acceptance"],
            }
        }
        fb = feedback(status="resolved", feedback_outcome="confirms")
        findings = run(
            [decision(), implementation(status="verified", verification_refs=["test:ok"]), fb],
            coverage={"REQ-A-001": "verified"},
            requirement_records=req_records,
        )
        self.assertNotIn("VDD017", rule_ids(findings))


if __name__ == "__main__":
    unittest.main()
