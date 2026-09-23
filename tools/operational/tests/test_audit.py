from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.operational.audit import render_audit_view, render_research_state_audit
from tools.research_state.state import (
    ResearchStateError,
    build_audit_state,
    load_registry,
    validate_registry_data,
)


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

    @staticmethod
    def _repo_root():
        return Path(__file__).resolve().parents[3]

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

    def test_real_sachenbacher_chain_is_readable_without_inventing_missing_method_state(self):
        rendered = render_research_state_audit(self._repo_root(), "F-U2-009")

        expected_fragments = (
            "finding_id: F-U2-009",
            "excerpt_id: AUD-EXC-L51-04-TEXT-D",
            "excerpt_id: AUD-EXC-L51-04-MAP-A",
            "complete published map",
            "excerpt_id: AUD-EXC-L51-04-CAPTION-C",
            "excerpt_id: AUD-EXC-L51-04-ZONE-EXPLANATION",
            "instance_id: DI-SACHENBACHER-2022-COMPLETE-PDF-20260914",
            "representation_id: REP-SACHENBACHER-2022-COMPLETE-PDF",
            "source_id: SRC-LIT-0001",
            "content_hash: sha256:3857636c854325eddaa0b658cd7b936a47d1b7712ccd7cbbc7296141e62616a0",
            "Sekundärquellen-/Modellbefund.",
            "keine unabhängige historische Validierung",
            "R51-06",
            '"evaluation":"unresolved"',
            "method_application_id: missing/unresolved",
            "missing/unresolved: finding F-U2-009 has no method application reference",
            "alternatives: missing/unresolved",
        )
        for fragment in expected_fragments:
            self.assertIn(fragment, rendered)

        self.assertNotIn("L51-04-KEY-B", rendered)
        self.assertNotIn("validation_status: validated", rendered)

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


class WP1StateSpineTests(unittest.TestCase):
    @staticmethod
    def _repo_root():
        return Path(__file__).resolve().parents[3]

    @staticmethod
    def _write_minimal_root(
        root: Path,
        *,
        finding_statement: str = "Canonical bounded finding.",
        instance_id: str = "DI-001",
        registry_instance_id: str | None = None,
    ) -> None:
        ledger = root / "docs/research/cases/orlagau-source-ledger.md"
        findings = root / "docs/research/cases/u2-knau-orlagau-quellenbefunde.md"
        manifest_path = root / "tools/document_evidence/data/reference.json"
        registry_path = root / "tools/research_state/data/records.json"
        for path in (ledger, findings, manifest_path, registry_path):
            path.parent.mkdir(parents=True, exist_ok=True)

        ledger.write_text(
            "# Ledger\n\n"
            "## SRC-LIT-0001 – Canonical source label\n\n"
            "- **source_type:** published-secondary-work\n",
            encoding="utf-8",
        )
        findings.write_text(
            "# Findings\n\n"
            "### F-U2-009 – Canonical finding\n\n"
            f"**Finding:** {finding_statement}\n\n"
            "**Status:** working-bounded\n\n"
            "**Aussagegrenze:** This is bounded and not independent validation.\n",
            encoding="utf-8",
        )

        manifest = {
            "instance": {
                "source_id": "SRC-LIT-0001",
                "representation_id": "REP-001",
                "instance_id": instance_id,
                "representation_kind": "complete-pdf",
                "inspection_status": "inspected",
                "sha256": "abc123",
            },
            "findings": [
                {
                    "finding_id": "F-U2-009",
                    "limit": "Reference scope remains bounded.",
                }
            ],
            "reference_cases": [
                {
                    "case_id": "REF-001",
                    "finding_id": "F-U2-009",
                    "locators": [
                        {
                            "locator_id": "L51-01",
                            "role": "text-reference",
                            "pdf_page_index": 1,
                            "printed_page": {"status": "resolved", "label": "1"},
                            "scope_note": "bounded locator",
                        }
                    ],
                }
            ],
            "relations": [
                {
                    "relation_id": "R-OPEN",
                    "type": "scope_relation",
                    "from_locator_id": "L51-01",
                    "to_locator_id": "L51-01",
                    "evaluation": "unresolved",
                    "note": "Still open.",
                }
            ],
        }
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        registry_instance_id = registry_instance_id or instance_id
        registry = {
            "schema_version": "0.1",
            "records": [
                {
                    "id": "SRC-LIT-0001",
                    "role": "source",
                    "canonical_ref": (
                        "docs/research/cases/orlagau-source-ledger.md"
                        "#heading=SRC-LIT-0001"
                    ),
                },
                {
                    "id": "REP-001",
                    "role": "representation",
                    "canonical_ref": (
                        "tools/document_evidence/data/reference.json"
                        "#representation_id=REP-001"
                    ),
                },
                {
                    "id": registry_instance_id,
                    "role": "instance",
                    "canonical_ref": (
                        "tools/document_evidence/data/reference.json"
                        f"#instance_id={registry_instance_id}"
                    ),
                },
                {
                    "id": "L51-01",
                    "role": "findspot",
                    "canonical_ref": (
                        "tools/document_evidence/data/reference.json"
                        "#locator_id=L51-01"
                    ),
                },
                {
                    "id": "F-U2-009",
                    "role": "finding",
                    "canonical_ref": (
                        "docs/research/cases/u2-knau-orlagau-quellenbefunde.md"
                        "#heading=F-U2-009"
                    ),
                },
            ],
        }
        registry_path.write_text(json.dumps(registry), encoding="utf-8")

    def test_wp1_at01_registry_keeps_only_identity_role_and_owner_reference(self):
        registry = load_registry(self._repo_root())
        for record in registry["records"]:
            self.assertEqual({"id", "role", "canonical_ref"}, set(record))
            self.assertNotIn("statement", record)
            self.assertNotIn("status", record)

    def test_wp1_at02_source_representation_instance_identities_are_distinct(self):
        state, _ = build_audit_state(self._repo_root(), "F-U2-009")
        source_id = state["sources"][0]["id"]
        representation_id = state["representations"][0]["id"]
        instance_id = state["instances"][0]["id"]
        self.assertEqual(3, len({source_id, representation_id, instance_id}))

    def test_wp1_at03_real_findspot_roundtrip_uses_registered_owner_chain(self):
        state, claim_id = build_audit_state(self._repo_root(), "F-U2-009")
        rendered = render_audit_view(state, claim_id)
        self.assertIn("L51-04-MAP-A", rendered)
        self.assertIn("DI-SACHENBACHER-2022-COMPLETE-PDF-20260914", rendered)
        self.assertIn("SRC-LIT-0001", rendered)

    def test_wp1_at04_unresolved_reference_and_missing_method_remain_explicit(self):
        rendered = render_research_state_audit(self._repo_root(), "F-U2-009")
        self.assertIn('"evaluation":"unresolved"', rendered)
        self.assertIn("R51-06", rendered)
        self.assertIn("method_application_id: missing/unresolved", rendered)
        self.assertIn("alternatives: missing/unresolved", rendered)

    def test_wp1_at05_resolution_is_read_only_for_canonical_research_owners(self):
        paths = [
            self._repo_root() / "docs/research/cases/orlagau-source-ledger.md",
            self._repo_root() / "docs/research/cases/u2-knau-orlagau-quellenbefunde.md",
            self._repo_root() / "tools/document_evidence/data/sachenbacher-2022-reference-v0.3.json",
        ]
        before = {path: path.read_bytes() for path in paths}
        build_audit_state(self._repo_root(), "F-U2-009")
        after = {path: path.read_bytes() for path in paths}
        self.assertEqual(before, after)

    def test_wp1_at06_same_canonical_basis_yields_same_derived_audit(self):
        first = render_research_state_audit(self._repo_root(), "F-U2-009")
        second = render_research_state_audit(self._repo_root(), "F-U2-009")
        self.assertEqual(first, second)

    def test_wp1_at07_derived_ids_are_not_persisted_as_canonical_records(self):
        registry = load_registry(self._repo_root())
        ids = {record["id"] for record in registry["records"]}
        self.assertFalse(any(item.startswith("AUDIT-ROOT-") for item in ids))
        self.assertFalse(any(item.startswith("AUD-EXC-") for item in ids))

    def test_wp1_at08_fresh_repo_context_resolves_without_chat_state(self):
        state, claim_id = build_audit_state(self._repo_root(), "F-U2-009")
        self.assertEqual("AUDIT-ROOT-F-U2-009", claim_id)
        self.assertEqual("F-U2-009", state["findings"][0]["id"])

    def test_wp1_at09_broken_reference_fails_instead_of_guessing(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = {
                "schema_version": "0.1",
                "records": [
                    {
                        "id": "SRC-LIT-0001",
                        "role": "source",
                        "canonical_ref": "missing.md#heading=SRC-LIT-0001",
                    }
                ],
            }
            with self.assertRaises(ResearchStateError):
                validate_registry_data(root, data)

    def test_wp1_at10_no_validation_or_alternative_semantics_are_invented(self):
        state, _ = build_audit_state(self._repo_root(), "F-U2-009")
        finding = state["findings"][0]
        owner_text = (
            self._repo_root() / "docs/research/cases/u2-knau-orlagau-quellenbefunde.md"
        ).read_text(encoding="utf-8")
        self.assertIn(finding["statement"], owner_text)
        self.assertNotIn("validation_status", finding)
        self.assertNotIn("alternatives", finding)

    def test_wp1_nt01_provider_key_cannot_substitute_for_source_identity(self):
        data = {
            "schema_version": "0.1",
            "records": [
                {
                    "id": "ZOT-ABC123",
                    "role": "source",
                    "canonical_ref": "ledger.md#heading=SRC-LIT-0001",
                }
            ],
        }
        with self.assertRaises(ResearchStateError):
            validate_registry_data(self._repo_root(), data)

    def test_wp1_nt02_provider_path_cannot_be_internal_instance_identity(self):
        data = {
            "schema_version": "0.1",
            "records": [
                {
                    "id": "tmp/book.pdf",
                    "role": "instance",
                    "canonical_ref": "fixture.json#instance_id=tmp/book.pdf",
                }
            ],
        }
        with self.assertRaises(ResearchStateError):
            validate_registry_data(self._repo_root(), data)

    def test_wp1_nt03_instance_mismatch_fails_closed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_minimal_root(
                root,
                instance_id="DI-ACTUAL",
                registry_instance_id="DI-EXPECTED",
            )
            with self.assertRaises(ResearchStateError):
                build_audit_state(root, "F-U2-009")

    def test_wp1_nt04_research_statement_is_loaded_from_owner_not_hardcoded(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            statement = "Changed canonical owner statement."
            self._write_minimal_root(root, finding_statement=statement)
            state, _ = build_audit_state(root, "F-U2-009")
            self.assertEqual(statement, state["findings"][0]["statement"])

    def test_wp1_nt05_unresolved_relation_is_not_normalized_away(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_minimal_root(root)
            state, claim_id = build_audit_state(root, "F-U2-009")
            rendered = render_audit_view(state, claim_id)
            self.assertIn('"evaluation":"unresolved"', rendered)
            self.assertIn("R-OPEN", rendered)

    def test_wp1_nt06_resolution_never_writes_owner_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_minimal_root(root)
            owner = root / "docs/research/cases/u2-knau-orlagau-quellenbefunde.md"
            before = owner.read_bytes()
            build_audit_state(root, "F-U2-009")
            self.assertEqual(before, owner.read_bytes())

    def test_wp1_nt07_derived_claim_role_is_not_admitted_to_registry(self):
        data = {
            "schema_version": "0.1",
            "records": [
                {
                    "id": "AUDIT-ROOT-F-U2-009",
                    "role": "claim",
                    "canonical_ref": "anything.md#heading=AUDIT-ROOT-F-U2-009",
                }
            ],
        }
        with self.assertRaises(ResearchStateError):
            validate_registry_data(self._repo_root(), data)

    def test_wp1_nt08_similar_label_does_not_repair_missing_identity(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "ledger.md"
            path.write_text(
                "## SRC-LIT-0002 – Same human label\n",
                encoding="utf-8",
            )
            data = {
                "schema_version": "0.1",
                "records": [
                    {
                        "id": "SRC-LIT-0001",
                        "role": "source",
                        "canonical_ref": "ledger.md#heading=SRC-LIT-0001",
                    }
                ],
            }
            with self.assertRaises(ResearchStateError):
                validate_registry_data(root, data)

    def test_wp1_nt09_fixture_only_field_cannot_expand_registry_contract(self):
        data = {
            "schema_version": "0.1",
            "records": [
                {
                    "id": "SRC-LIT-0001",
                    "role": "source",
                    "canonical_ref": "ledger.md#heading=SRC-LIT-0001",
                    "statement": "convenience copy",
                }
            ],
        }
        with self.assertRaises(ResearchStateError):
            validate_registry_data(self._repo_root(), data)

    def test_wp1_nt10_selection_or_next_action_role_is_not_admitted(self):
        for role in ("selection", "next_action"):
            data = {
                "schema_version": "0.1",
                "records": [
                    {
                        "id": "CURRENT",
                        "role": role,
                        "canonical_ref": "state.md#heading=CURRENT",
                    }
                ],
            }
            with self.assertRaises(ResearchStateError):
                validate_registry_data(self._repo_root(), data)


if __name__ == "__main__":
    unittest.main()
