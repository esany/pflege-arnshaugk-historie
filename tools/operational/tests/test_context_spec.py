from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.operational.context_spec import git_blob_sha, load_work_order


class WorkOrderContextTests(unittest.TestCase):
    def test_real_lampe_420_work_order_resumes_from_current_repo_state(self):
        path = Path("docs/research/cases/u2-lampe-420-work-order.json")
        context = load_work_order(path, root=Path("."))

        self.assertEqual("issue:#46", context.work_owner_ref)
        self.assertEqual("WO-U2-LAMPE-420-001", context.work_order_ref)
        self.assertEqual("unresolved", context.status)
        self.assertIn("Diplomatik / Urkundenlehre", context.leading_domains)
        self.assertTrue(any("SRC-ED-0004" in item for item in context.required_evidence))
        self.assertTrue(any("seller" in item and "purchase" in item for item in context.unresolved))
        self.assertIn("preceding purchase/seller", context.current_executable_action)
        self.assertIn("issue:#46", context.source_refs)
        self.assertIn("treat editorial identification as charter wording", context.must_not)
        self.assertIn("orlagau-source-ledger.md", context.persistence_target)

        states = {item.ref: item.status for item in context.prerequisites}
        self.assertEqual("pass", states["lampe-420-edition-instance-and-findspot-inspected"])
        self.assertEqual("unresolved", states["modern-archive-concordance"])
        self.assertEqual("unresolved", states["grune-modern-identification-independent-collation"])

    def test_ret_001_calibration_work_order_is_ready_before_implementation(self):
        path = Path("docs/development/work-orders/wo-ret-001-exact-retrieval-calibration.json")
        context = load_work_order(path, root=Path("."))

        self.assertEqual("issue:#53", context.work_owner_ref)
        self.assertEqual("WO-RET-001-CALIBRATION", context.work_order_ref)
        self.assertEqual("ready", context.status)
        self.assertEqual((), context.open_blockers)
        self.assertEqual((), context.unresolved)
        self.assertTrue(context.current_executable_action.startswith("Run the current-stage admission preflight first"))
        self.assertIn("treat AI/model output as evidence or retrieval ground truth", context.must_not)

        states = {item.ref: item.status for item in context.prerequisites}
        self.assertTrue(states)
        self.assertTrue(all(status == "pass" for status in states.values()))

        raw = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual("ready", raw["execution_admission"]["required_status"])
        self.assertEqual(7, len(raw["acceptance_tests"]))
        self.assertEqual(6, len(raw["negative_tests"]))
        self.assertTrue(raw["forbidden_loss"])
        self.assertTrue(raw["upstream_driver_refs"])
        self.assertTrue(raw["downstream_deferred_dependencies"])
        self.assertTrue(all(
            item["status"] == "not-authorized-in-current-stage"
            for item in raw["downstream_deferred_dependencies"]
        ))
        self.assertIn("Do not mark REQ-RET-001", raw["coverage_claim_limit"])
        self.assertEqual("tools/operational/retrieval.py", raw["implementation_shape"]["implementation_file"])
        self.assertEqual("none in this calibration", raw["implementation_shape"]["cli"])
        self.assertEqual("exact-literal-v0.1", raw["implementation_shape"]["implementation_version"])
        self.assertIn("corpus_fingerprint", raw["implementation_shape"]["output_contract"]["query_log"])
        self.assertEqual(["excerpt_id", "derivative_id", "instance_id", "representation_id", "source_id"], raw["implementation_shape"]["supported_filter_keys"])

    def test_changed_pass_basis_is_downgraded_to_unresolved(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            basis_path = root / "basis.md"
            basis_path.write_text("inspected state\n", encoding="utf-8")
            expected = git_blob_sha(basis_path)

            spec = {
                "schema_version": "0.1",
                "work_order_ref": "WO-TEST-1",
                "primary_function": "Domain / Source Research",
                "work_owner_ref": "issue:#46",
                "objective": "test basis invalidation",
                "scope": ["test"],
                "exclusions": ["none"],
                "leading_domains": ["Diplomatik"],
                "method_quality_frame": ["issue:#45"],
                "required_evidence": ["basis.md"],
                "current_executable_action": "continue source check",
                "prerequisites": [{
                    "ref": "inspected-source",
                    "status": "pass",
                    "basis": [{"path": "basis.md", "git_blob_sha": expected}],
                    "note": "passed on recorded basis"
                }],
                "open_blockers": [],
                "unresolved": [],
                "may": ["inspect"],
                "must_not": ["invent"],
                "stop_handoff_when": ["authority changes"],
                "return_condition": "done",
                "persistence_target": "result.md",
                "source_refs": ["basis.md"]
            }
            spec_path = root / "work-order.json"
            spec_path.write_text(json.dumps(spec), encoding="utf-8")

            basis_path.write_text("changed state\n", encoding="utf-8")
            context = load_work_order(spec_path, root=root)

            self.assertEqual("unresolved", context.status)
            self.assertEqual("unresolved", context.prerequisites[0].status)
            self.assertIn("prerequisite:inspected-source", context.unresolved)
            self.assertIn("revalidation required", context.prerequisites[0].note)


if __name__ == "__main__":
    unittest.main()
