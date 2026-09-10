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


class ProviderRemovalRestartabilityTests(unittest.TestCase):
    """#57 synthetic checks for #50 provider-removal acceptance invariant."""

    @staticmethod
    def _curated_state():
        return {
            "source_id": "SRC-001",
            "instance_id": "INS-001",
            "excerpt_id": "EXC-001",
            "finding_id": "FND-001",
            "source_refs": {"zotero_item_key": "ABC123"},
            "instance_refs": {
                "onedrive_drive_item_id": "drive-item-42",
                "content_hash": "sha256:fixture",
            },
            "availability": {"zotero": "available", "onedrive": "available"},
            "relations": {
                "instance_source": ["INS-001", "SRC-001"],
                "excerpt_instance": ["EXC-001", "INS-001"],
                "finding_excerpt": ["FND-001", "EXC-001"],
            },
            "finding": {
                "id": "FND-001",
                "status": "working",
                "statement": "Synthetic finding; not historical evidence.",
            },
            "regenerable": {
                "search_index": "cache/search-v1",
                "ocr_cache": "cache/ocr-v1",
            },
        }

    @staticmethod
    def _without_providers(state):
        removed = dict(state)
        removed["availability"] = {"zotero": "unavailable", "onedrive": "unavailable"}
        removed["regenerable"] = {}
        return removed

    @staticmethod
    def _assert_provider_neutral_identity(testcase, state):
        for field in ("source_id", "instance_id", "excerpt_id", "finding_id"):
            testcase.assertTrue(state.get(field), f"missing provider-neutral {field}")
        testcase.assertEqual(
            [state["instance_id"], state["source_id"]],
            state["relations"]["instance_source"],
        )
        testcase.assertEqual(
            [state["excerpt_id"], state["instance_id"]],
            state["relations"]["excerpt_instance"],
        )
        testcase.assertEqual(
            [state["finding_id"], state["excerpt_id"]],
            state["relations"]["finding_excerpt"],
        )

    def test_provider_removal_preserves_curated_identity_and_relations(self):
        before = self._curated_state()
        after = self._without_providers(before)

        self._assert_provider_neutral_identity(self, after)
        self.assertEqual(before["source_id"], after["source_id"])
        self.assertEqual(before["instance_id"], after["instance_id"])
        self.assertEqual(before["excerpt_id"], after["excerpt_id"])
        self.assertEqual(before["finding_id"], after["finding_id"])
        self.assertEqual(before["finding"], after["finding"])

    def test_provider_removal_degrades_availability_without_erasing_provider_refs(self):
        after = self._without_providers(self._curated_state())
        self.assertEqual("unavailable", after["availability"]["zotero"])
        self.assertEqual("unavailable", after["availability"]["onedrive"])
        self.assertEqual("ABC123", after["source_refs"]["zotero_item_key"])
        self.assertEqual("drive-item-42", after["instance_refs"]["onedrive_drive_item_id"])
        self.assertEqual({}, after["regenerable"])

    def test_fresh_context_can_resume_with_provider_unavailability_as_explicit_debt(self):
        provider_state = prerequisite_state(
            "source-provider-available",
            "unresolved",
            [BasisRef("INS-001", "provider-availability:unavailable")],
            note="Provider unavailable; curated identity remains restartable.",
        )
        context = derive_current_context(
            primary_function="Architecture / Verification / RSE",
            work_owner_ref="issue:#57",
            work_order_ref="WO-57-PROVIDER-REMOVAL-SYNTHETIC",
            objective="Verify restartability after provider removal.",
            scope=["provider removal", "curated state", "fresh-context restartability"],
            exclusions=["real provider access", "historical interpretation"],
            leading_domains=["Research Software Engineering"],
            method_quality_frame=["issue:#50", "issue:#57"],
            required_evidence=["provider-neutral IDs", "curated relations", "explicit availability"],
            current_executable_action="resume from curated state or report provider debt",
            prerequisites=[provider_state],
            open_blockers=[],
            unresolved=[],
            may=["derive transient resume context"],
            must_not=["infer provider availability", "invent missing bytes"],
            stop_handoff_when=["provider-dependent byte inspection becomes required"],
            return_condition="curated state is understandable without provider access",
            persistence_target="issue:#57",
            source_refs=["issue:#50", "issue:#57"],
        )
        self.assertEqual("unresolved", context.status)
        self.assertIn("prerequisite:source-provider-available", context.unresolved)
        self.assertNotIn("prerequisite:source-provider-available", context.open_blockers)
        self.assertEqual("issue:#57", context.work_owner_ref)

    def test_provider_only_identity_fixture_fails_closed(self):
        invalid = {
            "source_id": "",
            "instance_id": "",
            "excerpt_id": "EXC-001",
            "finding_id": "FND-001",
            "relations": {
                "instance_source": ["drive-item-42", "ABC123"],
                "excerpt_instance": ["EXC-001", "drive-item-42"],
                "finding_excerpt": ["FND-001", "EXC-001"],
            },
        }
        with self.assertRaises(AssertionError):
            self._assert_provider_neutral_identity(self, invalid)


if __name__ == "__main__":
    unittest.main()
