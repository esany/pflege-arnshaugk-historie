from __future__ import annotations

import copy
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.operational import enforcement


ROOT = Path(__file__).resolve().parents[3]
ACCEPTED = {
    "REQ-WF-001",
    "REQ-LEAN-001",
    "REQ-STATE-001",
    "REQ-TRACE-001",
    "REQ-MTH-004",
    "REQ-ENT-001",
    "REQ-STATE-003",
    "REQ-UX-001",
}


def rule_ids(findings):
    return {finding.rule_id for finding in findings}


class EnforcementMapTests(unittest.TestCase):
    def setUp(self):
        self.data = enforcement.load_json(ROOT / "tools/operational/enforcement-map.json")
        self.schema = enforcement.load_json(ROOT / "tools/operational/enforcement-map.schema.json")

    def run_with(self, data):
        original = enforcement.load_json

        def fake_load(path):
            if path.name == "enforcement-map.json":
                return data
            if path.name == "enforcement-map.schema.json":
                return self.schema
            return original(path)

        with patch.object(enforcement, "load_json", side_effect=fake_load):
            return enforcement.validate_enforcement_map(ROOT, ACCEPTED)

    def test_repository_map_is_formally_valid(self):
        self.assertFalse([f for f in enforcement.validate_enforcement_map(ROOT, ACCEPTED) if f.severity == "error"])

    def test_unknown_requirement_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["mappings"][0]["requirement_id"] = "REQ-X-999"
        self.assertIn("OPM004", rule_ids(self.run_with(data)))

    def test_unknown_rule_reference_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["mappings"][0]["enforcement"][0]["rule_refs"] = ["REQ999"]
        self.assertIn("OPM005", rule_ids(self.run_with(data)))

    def test_mixed_class_without_review_boundary_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["mappings"][0]["human_or_specialist_review_refs"] = []
        self.assertIn("OPM006", rule_ids(self.run_with(data)))

    def test_missing_fixture_selector_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["rules"][0]["fixture_refs"] = ["tools/requirements/tests/test_validate.py::test_does_not_exist"]
        self.assertIn("OPM007", rule_ids(self.run_with(data)))


if __name__ == "__main__":
    unittest.main()
