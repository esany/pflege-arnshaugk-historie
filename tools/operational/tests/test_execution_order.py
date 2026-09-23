from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import unittest

from tools.operational.execution_order import check_changed_files, validate_execution_order

ROOT = Path(__file__).resolve().parents[3]


def valid_order() -> dict:
    return {
        "schema_version": "0.1", "work_order_ref": "WO-REBUILD-EXEC-001", "work_owner_ref": "issue:#59",
        "primary_function": "Architecture / Development / Research Software Engineering",
        "causal_driver_slice": {"goal_refs": ["G-RESEARCH-001"], "need_refs": ["N-RESTART-001"], "pain_refs": ["P-CONTEXT-001"], "constraint_refs": ["AGENTS.md §13–14"]},
        "authority": {"work_owner_ref": "issue:#59", "semantic_authority_refs": ["issue:#42", "issue:#61"], "acceptance_authority_refs": ["issue:#59", "issue:#63"]},
        "accepted_requirements": [{"id": "REQ-TRACE-001", "acceptance_refs": ["docs/architecture/assurance/value-decision-delivery-assurance.md"], "verification_refs": ["tools/operational/tests/test_execution_order.py::test_positive_order_passes"]}],
        "scope": {"included_files": [{"path": "tools/operational/execution_order.py", "purpose": "bounded validator", "allowed_change": "add or revise validator behavior"}, {"path": "tools/operational/tests/test_execution_order.py", "purpose": "positive and negative checks", "allowed_change": "extend regression fixtures"}], "excluded_paths": ["sources/", "src/histo_orla/", "all other files"]},
        "minimal_context": {"max_refs": 5, "required_refs": [{"ref": "AGENTS.md §13–14", "why": "binding work-context and traceability rules"}, {"ref": "issue:#59", "why": "implementation and verification authority"}, {"ref": "issue:#61", "why": "handoff/restartability research owner"}, {"ref": "REQ-TRACE-001", "why": "accepted causal trace requirement"}]},
        "tests": [{"ref": "tools/operational/tests/test_execution_order.py::test_positive_order_passes", "purpose": "valid contract passes", "kind": "positive"}, {"ref": "tools/operational/tests/test_execution_order.py::test_scope_drift_is_rejected", "purpose": "out-of-scope file is rejected", "kind": "negative"}],
        "stop_handoff_when": ["accepted requirement or authority is unclear", "a new product architecture is proposed"], "persistence_target": "issue:#59 + implementation trace + tests",
        "return_contract": {"format": "delta-only", "required_fields": ["delta", "verification", "open_points", "handoff"], "handoff_fields": ["from", "to", "trigger", "established", "unresolved", "request", "acceptance", "persistence_target"]},
        "non_goals": ["no product multi-agent architecture", "no workflow engine", "no new requirement truth"],
    }


class ExecutionOrderTests(unittest.TestCase):
    def test_positive_order_passes(self): self.assertEqual([], validate_execution_order(valid_order(), root=ROOT))
    def test_scope_drift_is_rejected(self): self.assertEqual(["EXEC016"], [x.rule_id for x in check_changed_files(valid_order(), ["tools/operational/execution_order.py", "README.md"])])
    def test_missing_authority_is_rejected(self):
        order = deepcopy(valid_order()); order["authority"]["acceptance_authority_refs"] = []
        self.assertIn("EXEC004", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_incomplete_acceptance_is_rejected(self):
        order = deepcopy(valid_order()); order["accepted_requirements"][0]["verification_refs"] = []
        self.assertIn("EXEC006", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_broad_context_is_rejected(self):
        order = deepcopy(valid_order()); order["minimal_context"]["required_refs"][0] = {"ref": "entire repository", "why": "everything"}
        self.assertIn("EXEC009", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_requirement_invention_is_rejected(self):
        order = deepcopy(valid_order()); order["accepted_requirements"][0]["id"] = "REQ-INVENTED-999"
        self.assertIn("EXEC005", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_handoff_loss_is_rejected(self):
        order = deepcopy(valid_order()); order["return_contract"]["handoff_fields"] = ["from", "to"]
        self.assertIn("EXEC014", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_model_specific_execution_is_rejected(self):
        order = deepcopy(valid_order()); order["model"] = "some-model"
        self.assertIn("EXEC002", {x.rule_id for x in validate_execution_order(order, root=ROOT)})
    def test_product_multi_agent_scope_is_required_as_non_goal(self):
        order = deepcopy(valid_order()); order["non_goals"] = ["no new requirement truth"]
        self.assertIn("EXEC015", {x.rule_id for x in validate_execution_order(order, root=ROOT)})


if __name__ == "__main__": unittest.main()
