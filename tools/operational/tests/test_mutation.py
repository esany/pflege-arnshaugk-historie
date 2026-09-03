from __future__ import annotations

import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools.operational.mutation import (
    MutationBlocked,
    apply_bounded_file_edit,
    assess_bounded_candidate,
    assess_full_replacement,
    assess_state_delta,
    plan_bounded_replace,
)


class MutationGuardTests(unittest.TestCase):
    def test_identical_candidate_is_no_change(self):
        current = "alpha\nbeta\n"
        assessment = assess_state_delta(current, current)
        self.assertEqual("no_change", assessment.status)
        self.assertEqual(assessment.current_sha256, assessment.candidate_sha256)

    def test_exact_bounded_edit_is_allowed_and_preserves_unrelated_tail(self):
        current = "# State\n\nmarker: old\n\n## Keep\nimportant tail\n"
        candidate = "# State\n\nmarker: new\n\n## Keep\nimportant tail\n"
        assessment = assess_bounded_candidate(current, candidate, "marker: old", "marker: new")
        self.assertEqual("change", assessment.status)
        self.assertEqual(candidate, assessment.candidate_text)
        self.assertIn("important tail", assessment.candidate_text)

    def test_bounded_edit_rejects_unrelated_tail_deletion(self):
        current = "# State\n\nmarker: old\n\n## Keep\nimportant tail\n"
        destructive_candidate = "# State\n\nmarker: new\n"
        assessment = assess_bounded_candidate(current, destructive_candidate, "marker: old", "marker: new")
        self.assertEqual("blocked", assessment.status)
        self.assertIn("outside the declared bounded replacement", assessment.reason)

    def test_repeated_bounded_edit_is_no_change(self):
        current = "# State\n\nmarker: new\n\n## Keep\nimportant tail\n"
        assessment = plan_bounded_replace(current, "marker: old", "marker: new")
        self.assertEqual("no_change", assessment.status)
        self.assertEqual(current, assessment.candidate_text)

    def test_ambiguous_bounded_precondition_is_blocked(self):
        current = "marker: old\nother\nmarker: old\n"
        assessment = plan_bounded_replace(current, "marker: old", "marker: new")
        self.assertEqual("blocked", assessment.status)
        self.assertIn("ambiguous", assessment.reason)

    def test_missing_precondition_and_postcondition_is_blocked(self):
        current = "marker: something-else\n"
        assessment = plan_bounded_replace(current, "marker: old", "marker: new")
        self.assertEqual("blocked", assessment.status)

    def test_full_replacement_requires_explicit_mutation_type(self):
        current = "alpha\nbeta\n"
        candidate = "rewritten\n"
        assessment = assess_full_replacement(current, candidate)
        self.assertEqual("blocked", assessment.status)
        self.assertIn("not explicitly declared", assessment.reason)

    def test_explicit_full_replacement_can_proceed_to_downstream_review(self):
        current = "alpha\nbeta\n"
        candidate = "rewritten\n"
        assessment = assess_full_replacement(current, candidate, explicit=True)
        self.assertEqual("change", assessment.status)
        self.assertEqual(candidate, assessment.candidate_text)

    def test_atomic_file_adapter_applies_only_declared_edit(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.md"
            path.write_bytes(b"# State\n\nmarker: old\n\n## Keep\nimportant tail\n")
            os.chmod(path, 0o640)

            assessment = apply_bounded_file_edit(path, "marker: old", "marker: new")

            self.assertEqual("change", assessment.status)
            self.assertEqual("# State\n\nmarker: new\n\n## Keep\nimportant tail\n", path.read_bytes().decode("utf-8"))
            self.assertEqual(0o640, path.stat().st_mode & 0o777)

    def test_atomic_file_adapter_skips_replace_when_postcondition_already_holds(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.md"
            current = b"# State\n\nmarker: new\n\n## Keep\nimportant tail\n"
            path.write_bytes(current)

            with patch("tools.operational.mutation.os.replace") as replace:
                assessment = apply_bounded_file_edit(path, "marker: old", "marker: new")

            self.assertEqual("no_change", assessment.status)
            replace.assert_not_called()
            self.assertEqual(current, path.read_bytes())

    def test_atomic_file_adapter_blocks_ambiguous_edit_without_touching_file(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.md"
            current = b"marker: old\nother\nmarker: old\n"
            path.write_bytes(current)

            with self.assertRaises(MutationBlocked):
                apply_bounded_file_edit(path, "marker: old", "marker: new")

            self.assertEqual(current, path.read_bytes())


if __name__ == "__main__":
    unittest.main()
