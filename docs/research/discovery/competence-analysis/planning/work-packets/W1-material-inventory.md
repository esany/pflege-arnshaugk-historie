# G2. W1 – Material Inventory & Open-State Mapper

**Status:** `P0-frozen work packet / not yet executed`  
**Work Owner:** #150  
**Source Lock:** `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md` (exact blob SHA is bound in the manifest)  
**Assurance:** `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md`

**WORKER ID** — `W1`  
**PRIMARY FUNCTION** — semantic inventory / preservation preparation.  
**BOUND INTENT** — enumerate every material element of the frozen owner-confirmed analysis without writing the final baseline or importing external meaning.  
**CURRENT CANONICAL TASK / WORK OWNER** — Preservation Work Owner; #22/#60 retain content/method ownership.  
**PURPOSE** — create a falsifiable completeness basis before prose transformation.  
**REQUIRED COMPETENCE** — semantic fidelity, careful source decomposition, provenance/status discrimination.  
**SOURCE OF MEANING** — exact frozen Source Lock blob only.  
**CANONICAL INPUTS** — AGENTS; Preservation Issue; Source Lock+blob SHA; Assurance Contract; W1 packet.  
**FORBIDDEN OVERRIDE INPUTS** — PR #147/#148, Method Profile Contract, later AI summaries; may not fill gaps or normalize source.  
**ENTRY CONDITIONS** — P0 merged; Source Lock frozen; Assurance Contract final; no unresolved P0 owner decision.  
**SCOPE** — inventory and classify material content/open states only.  
**MAY** — segment source; assign `INV-*`; classify type; record explicit relations/status/open states.  
**MUST** — anchor every material item to Source Lock; distinguish shared concept/profile/interface/activation/failure/case/open-state.  
**MUST PRESERVE** — wording-dependent distinctions, uncertainty, P6 boundary, case-vs-general, non-promotion.  
**MUST NOT** — author baseline; perform SOTA; infer missing profile content; import PR147 richness; decide split/merge; create historical findings.  
**AUTHORITY BOUNDARY** — inventory judgement only; cannot establish domain truth or modify owner meaning.  
**APPLICABLE METHOD / QUALITY FRAME** — #53 Semantic Fidelity as candidate aid; #5 Harvest/material-state prior art; QC-01/02/03/04/08/09/17/18.  
**REQUIRED EVIDENCE** — Source anchors and full inventory table.  
**QUALITY CRITERIA** — all Cross-cutting/Meta/Profile/Interface/Activation classes represented; no unsupported additions.  
**EXPECTED OUTPUT** — `INV_ID | source_anchor | type | meaning_to_preserve | must_preserve_distinctions | explicit_relations | epistemic_status | open_state | explicit_non_conclusion`.  
**PERSISTENCE TARGET** — execution PR temporary `runs/<run>/W1-inventory.md`, later summarized into run-assurance.  
**POSITIVE ACCEPTANCE TESTS** — every profile has multiple material items beyond label; interfaces/activation/open-state items explicit.  
**NEGATIVE / ADVERSARIAL TESTS** — delete Detectability or Handoff nuance; tempt import from #147; Herrmann example as finding.  
**PASS** — every material Source-Lock element inventoried or explicitly non-material with rationale; no semantic addition.  
**REVISE** — none autonomously when source meaning unclear; mechanical formatting correction only before verdict.  
**STOP** — `STOP-SEMANTIC`, `STOP-PROVENANCE`, `STOP-CAPABILITY` if frozen source unavailable.  
**ALLOWED REPAIR TARGETS** — Human source clarification only for material ambiguity.  
**RETURN CONTRACT** — `PASS|STOP + inventory_ref + coverage_summary + unresolved_source_ambiguities`.  
**NEXT ALLOWED TRANSITION** — W2 on PASS.  
**INDEPENDENCE REQUIREMENT** — no; but source lock must be frozen.  
**MODEL / CAPABILITY CLASS** — lower-cost route permitted only if it can compare long structured source reliably; W3/W5 provide independent semantic controls.
