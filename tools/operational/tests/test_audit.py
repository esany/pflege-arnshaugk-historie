from __future__ import annotations

from copy import deepcopy
import unittest

from tools.operational.audit import render_audit_view


class DerivedAuditViewTests(unittest.TestCase):
    @staticmethod
    def _state():
        return {
            "sources": [
                {
                    "id": "SRC-001",
                    "label": "Synthetic source; not historical evidence.",
                    "type": "archival-unit",
                    "provider_refs": {"zotero_item_key": "ZOT-ABC123"},
                    "availability": {"zotero": "available"},
                }
            ],
            "representations": [
                {
                    "id": "REP-001",
                    "source_id": "SRC-001",
                    "kind": "edition",
                    "label": "Synthetic representation",
                }
            ],
            "instances": [
                {
                    "id": "INS-001",
                    "representation_id": "REP-001",
                    "inspection_status": "inspected",
                    "provider_refs": {
                        "content_hash": "sha256:synthetic-fixture",
                        "onedrive_drive_item_id": "OD-42",
                    },
                    "availability": {"onedrive": "available"},
                }
            ],
            "derivatives": [
                {
                    "id": "DER-001",
                    "instance_id": "INS-001",
                    "kind": "transcription",
                    "status": "working",
                    "processor": "synthetic-fixture-tool",
                    "version": "1",
                }
            ],
            "excerpts": [
                {
                    "id": "EXC-001",
                    "derivative_id": "DER-001",
                    "findspot": "p. 12, lines 3-5",
                    "text": "Synthetic excerpt text.",
                }
            ],
            "findings": [
                {
                    "id": "FND-001",
                    "statement": "Synthetic finding; not historical evidence.",
                    "status": "working",
                    "validation_status": "working",
                    "excerpt_ids": ["EXC-001"],
                    "method_application_id": "MAPP-001",
                    "candidate_origin": {"kind": "human-fixture"},
                    "uncertainty": {
                        "status": "unresolved",
                        "note": "Synthetic alternative remains open.",
                    },
                    "alternatives": ["ALT-SYNTH-001"],
                }
            ],
            "claims": [
                {
                    "id": "CLM-001",
                    "statement": "Synthetic answer for audit navigation.",
                    "status": "working",
                    "finding_ids": ["FND-001"],
                }
            ],
            "method_applications": [
                {
                    "id": "MAPP-001",
                    "profile_ref": "METHOD-SYNTH",
                    "profile_version": "0.1",
                    "profile_status": "working-method",
                    "work_order_ref": "WO-SYNTH-55",
                    "scope": ["synthetic audit fixture"],
                    "leading_domains": ["Research Software Engineering"],
                    "application_summary": "Synthetic application; no historical claim.",
                    "validation_status": "working",
                }
            ],
        }

    def test_happy_path_navigates_claim_to_method_and_source(self):
        rendered = render_audit_view(self._state(), "CLM-001")

        expected_fragments = (
            "claim_id: CLM-001",
            "finding_id: FND-001",
            "excerpt_id: EXC-001",
            "findspot: p. 12, lines 3-5",
            "derivative_id: DER-001",
            "instance_id: INS-001",
            "representation_id: REP-001",
            "source_id: SRC-001",
            "method_application_id: MAPP-001",
            "method_profile_ref: METHOD-SYNTH",
            "method_profile_status: working-method",
            "work_order_ref: WO-SYNTH-55",
            "validation_status: working",
            "uncertainty:",
            "alternatives:",
            "reference gaps: []",
        )
        for fragment in expected_fragments:
            self.assertIn(fragment, rendered)

    def test_uncertainty_is_preserved_instead_of_rendered_as_certain(self):
        state = self._state()
        state["findings"][0]["status"] = "unresolved"
        state["findings"][0]["validation_status"] = "external-validation-required"
        state["findings"][0]["uncertainty"] = {
            "status": "unresolved",
            "note": "Two synthetic readings remain possible.",
        }

        rendered = render_audit_view(state, "CLM-001")

        self.assertIn("status: unresolved", rendered)
        self.assertIn("validation_status: external-validation-required", rendered)
        self.assertIn('"status":"unresolved"', rendered)
        self.assertIn("Two synthetic readings remain possible.", rendered)

    def test_provider_unavailable_keeps_internal_identity_and_provider_refs_visible(self):
        state = self._state()
        state["sources"][0]["availability"]["zotero"] = "unavailable"
        state["instances"][0]["availability"]["onedrive"] = "unavailable"

        rendered = render_audit_view(state, "CLM-001")

        self.assertIn("source_id: SRC-001", rendered)
        self.assertIn("instance_id: INS-001", rendered)
        self.assertIn("source.provider_ref.zotero_item_key: ZOT-ABC123", rendered)
        self.assertIn("instance.provider_ref.onedrive_drive_item_id: OD-42", rendered)
        self.assertIn("source.availability.zotero: unavailable", rendered)
        self.assertIn("instance.availability.onedrive: unavailable", rendered)

    def test_missing_finding_excerpt_or_findspot_is_explicitly_unresolved(self):
        base = self._state()

        missing_finding = deepcopy(base)
        missing_finding["claims"][0]["finding_ids"] = ["FND-MISSING"]
        rendered = render_audit_view(missing_finding, "CLM-001")
        self.assertIn(
            "missing/unresolved: claim CLM-001 references absent finding FND-MISSING",
            rendered,
        )

        missing_excerpt = deepcopy(base)
        missing_excerpt["findings"][0]["excerpt_ids"] = ["EXC-MISSING"]
        rendered = render_audit_view(missing_excerpt, "CLM-001")
        self.assertIn(
            "missing/unresolved: finding FND-001 references absent excerpt EXC-MISSING",
            rendered,
        )

        missing_findspot = deepcopy(base)
        del missing_findspot["excerpts"][0]["findspot"]
        rendered = render_audit_view(missing_findspot, "CLM-001")
        self.assertIn(
            "missing/unresolved: excerpt EXC-001 has no findspot",
            rendered,
        )

    def test_demoted_finding_keeps_history_and_does_not_look_currently_validated(self):
        state = self._state()
        finding = state["findings"][0]
        finding["status"] = "demoted"
        finding["validation_status"] = "superseded"
        finding["superseded_by"] = "FND-002"
        finding["history"] = [
            {"status": "working", "ref": "REV-001"},
            {"status": "demoted", "ref": "REV-002"},
        ]

        rendered = render_audit_view(state, "CLM-001")

        self.assertIn("status: demoted", rendered)
        self.assertIn("validation_status: superseded", rendered)
        self.assertIn("superseded_by: FND-002", rendered)
        self.assertIn('"ref":"REV-001"', rendered)
        self.assertIn('"ref":"REV-002"', rendered)
        self.assertNotIn("validation_status: validated", rendered)

    def test_ai_candidate_without_evidence_link_is_not_rendered_as_evidence(self):
        state = self._state()
        state["findings"] = [
            {
                "id": "FND-AI",
                "statement": "Synthetic AI candidate.",
                "status": "candidate",
                "validation_status": "candidate",
                "candidate_origin": {"kind": "ai", "ref": "MODEL-RUN-SYNTH"},
                "excerpt_ids": [],
                "method_application_id": "MAPP-001",
                "uncertainty": {"status": "unresolved"},
                "alternatives": [],
            }
        ]
        state["claims"][0]["finding_ids"] = ["FND-AI"]

        rendered = render_audit_view(state, "CLM-001")

        self.assertIn('candidate_origin: {"kind":"ai","ref":"MODEL-RUN-SYNTH"}', rendered)
        self.assertIn("missing/unresolved: finding FND-AI has no excerpt reference", rendered)
        self.assertNotIn("excerpt_id:", rendered)
        self.assertNotIn("source_id:", rendered)

    def test_same_input_is_deterministic_and_not_mutated(self):
        state = self._state()
        before = deepcopy(state)

        first = render_audit_view(state, "CLM-001")
        second = render_audit_view(state, "CLM-001")

        self.assertEqual(first, second)
        self.assertEqual(before, state)


if __name__ == "__main__":
    unittest.main()
