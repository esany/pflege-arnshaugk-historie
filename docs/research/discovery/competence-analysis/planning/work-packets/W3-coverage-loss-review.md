# G4. W3 – Coverage & Loss Auditor

**Status:** `P0-frozen work packet / not yet executed`  
**Work Owner:** #150  
**Source Lock:** `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md` (exact blob SHA is bound in the manifest)  
**Assurance:** `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md`

**WORKER ID** — `W3`  
**PRIMARY FUNCTION** — fresh semantic coverage/loss review.  
**BOUND INTENT** — falsify the claim that W2 fully and faithfully represents the frozen source.  
**CURRENT CANONICAL TASK / WORK OWNER** — Preservation Work Owner; W3 review only.  
**PURPOSE** — detect missing, partial, flattened, promoted or unsupported content before repo reconciliation.  
**REQUIRED COMPETENCE** — exact source/draft comparison, semantic differencing, status/provenance awareness.  
**SOURCE OF MEANING** — Source Lock.  
**CANONICAL INPUTS** — Source Lock; W1; W2 draft; Assurance Contract/Oracles; W3 packet.  
**FORBIDDEN OVERRIDE INPUTS** — W2 author reasoning; PR147/148; expected PASS.  
**ENTRY CONDITIONS** — fresh context; W2 returned complete draft+mapping.  
**SCOPE** — representation fidelity and additions only; no scientific truth review.  
**MAY** — map each INV to draft; search unsupported claims; grade coverage.  
**MUST** — inspect profile detail, interface, activation, open-state, P6 reversibility, status.  
**MUST PRESERVE** — source authority; independent challengeability.  
**MUST NOT** — improve model; import repo derivative; decide Profile SOTA.  
**AUTHORITY BOUNDARY** — review verdict over representation only.  
**APPLICABLE METHOD / QUALITY FRAME** — QC-01…08, 15…18; Coverage Oracle.  
**REQUIRED EVIDENCE** — row-by-row coverage/loss matrix with draft locations.  
**QUALITY CRITERIA** — every material INV `FULL`; no S2/S3; zero unmarked substantive additions.  
**EXPECTED OUTPUT** — `INV_ID | location | FULL/PARTIAL/MISSING/ALTERED/FLATTENED/PROMOTED/UNSUPPORTED | severity | correction`.  
**PERSISTENCE TARGET** — execution-run review evidence, later summarized.  
**POSITIVE ACCEPTANCE TESTS** — distributed representation may PASS if fully reconstructable.  
**NEGATIVE / ADVERSARIAL TESTS** — one lost inference boundary; unsupported sensible rule; unresolved→likely answer; P6 hardening.  
**PASS** — 100% material coverage, no unmarked additions/status drift.  
**REVISE** — deterministic S1/S2 representation defects with exact patch instructions → W2.  
**STOP** — source/draft conflict requires choosing meaning or same material failure recurs.  
**ALLOWED REPAIR TARGETS** — W2 only; one automatic cycle.  
**RETURN CONTRACT** — `PASS|REVISE|STOP + matrix_ref + QC_verdicts + repair_set`.  
**NEXT ALLOWED TRANSITION** — PASS→W4; REVISE→W2; STOP→Human.  
**INDEPENDENCE REQUIREMENT** — fresh context; no author rationale.  
**MODEL / CAPABILITY CLASS** — lower-cost/medium may suffice because Oracle+exact source comparison externalize evaluation; escalate if long-context comparison quality is doubtful.
