# G8. W7 – Fresh Restart / Handoff Tester

**Status:** `P0-frozen work packet / not yet executed`  
**Work Owner:** #150  
**Source Lock:** `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md` (exact blob SHA is bound in the manifest)  
**Assurance:** `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md`

**WORKER ID** — `W7`  
**PRIMARY FUNCTION** — fresh-context empirical restartability test.  
**BOUND INTENT** — prove a competent new worker can reconstruct current competence-analysis state from repo-only entry path without this chat.  
**CURRENT CANONICAL TASK / WORK OWNER** — Preservation Work Owner until test/closeout completes.  
**PURPOSE** — detect navigation, status, authority or semantic handoff failures that other reviews may miss.  
**REQUIRED COMPETENCE** — repository bootstrap, comprehension, status/owner reasoning; no source-memory advantage.  
**SOURCE OF MEANING** — final repository candidate state only.  
**CANONICAL INPUTS** — AGENTS→PROJECT_STATE→README→Preservation Issue→competence-analysis README→analysis baseline→referenced artifacts as needed.  
**FORBIDDEN OVERRIDE INPUTS** — current chat, W1–W6 reasoning, expected verdict, PR147 as substitute baseline; Source Lock unless provenance inspection is explicitly needed.  
**ENTRY CONDITIONS** — W6 PASS; fresh context; candidate repo navigation complete.  
**SCOPE** — answer Restart Oracle and identify nav vs semantic failure.  
**MAY** — follow repo references; inspect provenance when needed.  
**MUST** — reconstruct status, source role, profiles, operational depth, interfaces, activation, owners, open debt, next allowed work.  
**MUST PRESERVE** — independence, no chat handoff.  
**MUST NOT** — infer missing state from general knowledge; treat PR147/148 as current truth.  
**AUTHORITY BOUNDARY** — test verdict only.  
**APPLICABLE METHOD / QUALITY FRAME** — QC-12, Restart Oracle J.  
**REQUIRED EVIDENCE** — question-by-question answer with repo source path and uncertainty.  
**QUALITY CRITERIA** — every oracle question materially correct; source path discoverable.  
**EXPECTED OUTPUT** — restart reconstruction + `PASS|REVISE|STOP`.  
**PERSISTENCE TARGET** — run-assurance / PR review evidence.  
**POSITIVE ACCEPTANCE TESTS** — can distinguish analysis vs Method Truth, P6 boundary, initial vs deep verification, interfaces, open SOTA.  
**NEGATIVE / ADVERSARIAL TESTS** — labels-only reconstruction; 16 final profiles; PR148=truth; document=Method Truth closure.  
**PASS** — all material semantic answers correct without chat.  
**REVISE** — only navigation/pointer/handoff wording defect with semantics intact → W6 once.  
**STOP** — material semantic misunderstanding, missing canonical source, need for chat, or assurance escape.  
**ALLOWED REPAIR TARGETS** — W6 navigation only; semantic failure = `STOP-ASSURANCE-ESCAPE`.  
**RETURN CONTRACT** — `PASS|REVISE|STOP + oracle_matrix + source_paths + nav_failures + semantic_failures`.  
**NEXT ALLOWED TRANSITION** — PASS→DONE.  
**INDEPENDENCE REQUIREMENT** — mandatory fresh context.  
**MODEL / CAPABILITY CLASS** — lower-cost fresh context allowed if it can follow repo navigation reliably; the test measures handoff clarity, not hidden reasoning power.
