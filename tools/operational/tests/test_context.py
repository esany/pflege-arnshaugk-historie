from __future__ import annotations

import unittest

from tools.operational.context import (
    BasisRef,
    ContextError,
    assess_cursor_request,
    derive_current_context,
    prerequisite_needs_revalidation,
    prerequisite_state,
)


class CurrentContextTests(unittest.TestCase):
    def _base_context(self, *, prerequisites=(), unresolved=(), blockers=()):
        return derive_current_context(
            primary_function="Architecture / Development / RSE",
            work_owner_ref="issue:#61",
            work_order_ref="WO-TEST-CONTEXT",
            objective="Derive a restartable current context from canonical state.",
            scope=["current context", "resume", "prerequisite validity"],
            exclusions=["historical interpretation", "priority authority"],
            leading_domains=["Research Software Engineering"],
            method_quality_frame=["AGENTS.md §13", "issue:#61"],
            required_evidence=["canonical work-owner state", "versioned prerequisite basis"],
            current_executable_action="run fresh-context restart fixture",
            prerequisites=list(prerequisites),
            open_blockers=list(blockers),
            unresolved=list(unresolved),
            may=["derive transient context"],
            must_not=["invent scholarly truth"],
            stop_handoff_when=["authority boundary changes"],
            return_condition="fresh context can resume from canonical refs",
            persistence_target="issue:#61 / implementation trace",
            source_refs=["AGENTS.md", "issue:#61"],
        )

    def test_f_ec_03_model_uncertainty_does_not_invalidate_unchanged_prerequisite(self):
        basis = [BasisRef("docs/research/source.md", "sha256:abc")]
        previous = prerequisite_state("source-inspected", "pass", basis)
        self.assertFalse(prerequisite_needs_revalidation(previous, basis))

    def test_f_ec_04_changed_basis_requires_revalidation(self):
        previous = prerequisite_state(
            "source-inspected",
            "pass",
            [BasisRef("docs/research/source.md", "sha256:abc")],
        )
        changed = [BasisRef("docs/research/source.md", "sha256:def")]
        self.assertTrue(prerequisite_needs_revalidation(previous, changed))

    def test_f_ec_05_support_task_without_priority_authority_redirects(self):
        context = self._base_context()
        assessment = assess_cursor_request(
            context,
            requested_work_owner_ref="issue:#70",
            requested_action="expand governance audit",
        )
        self.assertEqual("redirect", assessment.reaction)
        self.assertEqual("issue:#61", assessment.work_owner_ref)
        self.assertEqual("run fresh-context restart fixture", assessment.current_executable_action)

    def test_authorized_priority_change_can_continue_on_new_cursor(self):
        context = self._base_context()
        assessment = assess_cursor_request(
            context,
            requested_work_owner_ref="issue:#46",
            requested_action="resume Lampe 420 research",
            priority_authorized=True,
        )
        self.assertEqual("continue", assessment.reaction)
        self.assertEqual("issue:#46", assessment.work_owner_ref)
        self.assertEqual("resume Lampe 420 research", assessment.current_executable_action)

    def test_f_ec_06_fresh_context_preserves_full_resume_contract(self):
        prerequisite = prerequisite_state(
            "archive-concordance",
            "unresolved",
            [BasisRef("docs/research/cases/orlagau-source-ledger.md", "sha256:ledger")],
            note="modern archive concordance not yet resolved",
        )
        context = self._base_context(
            prerequisites=[prerequisite],
            unresolved=["editorial identification requires independent collation"],
        )
        self.assertEqual("issue:#61", context.work_owner_ref)
        self.assertEqual("WO-TEST-CONTEXT", context.work_order_ref)
        self.assertEqual("run fresh-context restart fixture", context.current_executable_action)
        self.assertEqual("unresolved", context.status)
        self.assertIn("prerequisite:archive-concordance", context.unresolved)
        self.assertIn("historical interpretation", context.exclusions)
        self.assertIn("Research Software Engineering", context.leading_domains)
        self.assertIn("AGENTS.md §13", context.method_quality_frame)
        self.assertIn("versioned prerequisite basis", context.required_evidence)
        self.assertEqual("issue:#61 / implementation trace", context.persistence_target)
        self.assertIn("AGENTS.md", context.source_refs)

    def test_failed_prerequisite_blocks_context(self):
        prerequisite = prerequisite_state(
            "required-evidence-available",
            "fail",
            [BasisRef("SRC-INSTANCE-1", "availability:false")],
        )
        context = self._base_context(prerequisites=[prerequisite])
        self.assertEqual("blocked", context.status)
        self.assertIn("prerequisite:required-evidence-available", context.open_blockers)

    def test_ready_context_requires_full_minimum_resume_contract(self):
        context = self._base_context()
        self.assertEqual("ready", context.status)
        self.assertEqual("issue:#61", context.work_owner_ref)
        self.assertTrue(context.work_order_ref)
        self.assertTrue(context.scope)
        self.assertTrue(context.leading_domains)
        self.assertTrue(context.method_quality_frame)
        self.assertTrue(context.required_evidence)
        self.assertTrue(context.persistence_target)
        self.assertTrue(context.source_refs)

    def test_missing_persistence_target_fails_closed(self):
        with self.assertRaises(ContextError):
            derive_current_context(
                primary_function="RSE",
                work_owner_ref="issue:#61",
                work_order_ref="WO-TEST",
                objective="test",
                scope=["resume"],
                exclusions=[],
                leading_domains=["RSE"],
                method_quality_frame=["AGENTS.md §13"],
                required_evidence=["canonical state"],
                current_executable_action="test",
                prerequisites=[],
                open_blockers=[],
                unresolved=[],
                may=[],
                must_not=[],
                stop_handoff_when=[],
                return_condition="done",
                persistence_target="",
                source_refs=["issue:#61"],
            )

    def test_missing_required_evidence_fails_closed(self):
        with self.assertRaises(ContextError):
            derive_current_context(
                primary_function="Domain / Source Research",
                work_owner_ref="issue:#46",
                work_order_ref="WO-U2-LAMPE-420-001",
                objective="test",
                scope=["Lampe 420"],
                exclusions=[],
                leading_domains=["Diplomatik"],
                method_quality_frame=["issue:#45"],
                required_evidence=[],
                current_executable_action="test",
                prerequisites=[],
                open_blockers=[],
                unresolved=[],
                may=[],
                must_not=[],
                stop_handoff_when=[],
                return_condition="done",
                persistence_target="docs/research/cases/u2-deutschorden-schleiz-quellenexzerpte.md",
                source_refs=["issue:#46"],
            )


if __name__ == "__main__":
    unittest.main()
