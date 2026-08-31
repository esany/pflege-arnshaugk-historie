# Histo-Orla – MVP Requirements & Acceptance Coverage

**Status:** `active delivery ledger / initial baseline 2026-08-31`  
**Owner:** #59 MVP Development  
**Technical Lead:** #48  
**Requirements/Acceptance Owner:** #42  
**Governance:** `docs/governance/lean-agile-non-regression.md`

## 1. Zweck

Diese Datei ist die **monotone Delivery-Coverage-Sicht** auf den vollständigen privaten MVP-Scope.

Sie verhindert, dass akzeptierte Anforderungen durch Slice-Priorisierung, neue Buzzwords, Architekturwechsel oder Chat-Wechsel still verschwinden.

Kanonische Requirement-/Acceptance-Wahrheit bleibt in #42 und den jeweiligen Artefakten. Diese Datei besitzt **nur Delivery-Status und Implementierungs-/Verification-Traceability**.

Quellen:

1. `docs/research/synthesis/requirements-baseline.md` – 39 accepted Requirements/Constraints;
2. `docs/research/synthesis/mvp-acceptance.md` – 38 owner-accepted MVP Acceptance Criteria;
3. spätere explizit akzeptierte Deltas aus #42 werden hier ergänzt, niemals still ersetzt.

## 2. Statusmodell

```text
not-started
in-progress
implemented
verified
partial
blocked
research-needed
owner-deferred
```

Regeln:

- `owner-deferred` nur nach expliziter Owner-Entscheidung;
- `nicht im aktuellen Slice` bleibt `not-started`, nicht `owner-deferred`;
- `implemented` bedeutet Code/Funktion vorhanden, aber noch nicht zwingend vollständig verifiziert;
- `verified` benötigt passende Acceptance-/Regression-/Invariant-/Real-Case-Tests;
- `partial` muss konkret sagen, welcher Teil fehlt;
- Scope-/Qualitätsreduktion erfolgt niemals in diesem Ledger, sondern nur über #42/#44 mit Traceability.

## 3. Accepted Requirements Baseline – Delivery Coverage

| Requirement | Delivery owner / primary work package | Status | Evidence / implementation | Notes |
|---|---|---|---|---|
| REQ-EPI-001 | #60/#54/#55/#59 | not-started | – | Domain method + evidence standard traceability |
| REQ-EPI-002 | #60/#59 | not-started | – | professional problem translation |
| REQ-EPI-003 | #50/#60/#59 | not-started | – | terminology layers/context |
| REQ-EPI-004 | #50/#54/#55 | not-started | – | unresolved/contradiction first-class |
| REQ-EPI-005 | #54/#55 | not-started | – | AI ≠ evidence/independent validation |
| REQ-SRC-001 | #50/#51 | not-started | – | source identity ≠ representation |
| REQ-SRC-002 | #49/#50/#51 | not-started | – | inspected instance status |
| REQ-SRC-003 | #50/#51/#55 | not-started | – | editorial/normalization layer separation |
| REQ-SRC-004 | #51/#55 | not-started | – | findspot roundtrip |
| REQ-SRC-005 | #60/#59 | not-started | – | archive provenance/function routing |
| REQ-OCR-001 | #52/#51 | not-started | – | OCR/HTR derivative + parentage |
| REQ-OCR-002 | #52/#51 | not-started | – | page/folio/region mapping |
| REQ-OCR-003 | #52 | not-started | – | research-critical OCR benchmark |
| REQ-RET-001 | #53/#59 | not-started | – | exact/auditable search without LLM |
| REQ-RET-002 | #53/#60 | not-started | – | controlled historical variants |
| REQ-RET-003 | #53/#57 | not-started | – | query/corpus provenance |
| REQ-RET-004 | #53/#55/#60 | not-started | – | bounded negative findings |
| REQ-RET-005 | #53 | not-started | – | semantic/RAG additive only if benchmark-admitted |
| REQ-CRIT-001 | #50/#55/#60 | not-started | – | claim-specific source dependence |
| REQ-CRIT-002 | #50/#55/#60 | not-started | – | discrepancy before harmonization |
| REQ-ENT-001 | #54/#50 | not-started | – | candidate→promotion / false-merge protection |
| REQ-REL-001 | #50/#55/#60 | not-started | – | proxy/co-presence ≠ relation |
| REQ-SPAT-001 | #50/#55/#60 | not-started | – | temporal/multi-scale place context |
| REQ-ACT-001 | #50/#55/#60 | not-started | – | action/motive/attribution/structure separation |
| REQ-SYN-001 | #50/#55/#60 | not-started | – | evidence axes remain distinct |
| REQ-SYN-002 | #55/#60/#59 | not-started | – | transdisciplinary synthesis preserves alternatives |
| REQ-UX-001 | #55/#59 | not-started | – | answer→finding→source/findspot→method audit |
| REQ-UX-002 | #54/#55/#59 | not-started | – | challenge/correct/demote without micromanagement |
| REQ-VAL-001 | #54/#55/#60 | not-started | – | consequence-based validation levels |
| REQ-VAL-002 | #55/#60 | not-started | – | honest independent specialist validation status |
| REQ-WF-001 | #54/#59 | not-started | – | deterministic formal invariants |
| REQ-WF-002 | #57/#59 | not-started | – | reproducible/restartable processing/search |
| REQ-STATE-001 | #50/#57/#59 | not-started | – | provider-/chat-independent portable state |
| REQ-STATE-002 | #50/#57 | not-started | – | curated vs regenerable state |
| REQ-INT-001 | #49/#57 | not-started | – | integration escape hatch |
| REQ-LEAN-001 | #48 | in-progress | #48 + non-regression contract | smallest sufficient components; SOTA/existing tools first |
| REQ-RGT-001 | #56 | not-started | – | external-processing rights admission |
| REQ-RGT-002 | #56 | not-started | – | privacy screening |
| REQ-BND-001 | #50/#59 | not-started | – | mediation cannot back-write research state |

**Baseline count:** 39 / 39 represented.

## 4. Owner-Accepted MVP Overlay – Delivery Coverage

| Acceptance Criterion | Delivery owner / primary work package | Status | Evidence / implementation | Notes |
|---|---|---|---|---|
| AC-MVP-001 | #48/#59 | in-progress | active lean delivery mode | private / lean / agile without quality reduction |
| AC-MVP-002 | #48/#58 | in-progress | #48/#58 governance | evolutionary architecture |
| AC-MVP-003 | #42/#48/#59 | in-progress | non-regression contract | Domain/accepted criteria lead delivery |
| AC-EPI-001 | #50/#59 | not-started | – | state/object types distinguishable |
| AC-EPI-002 | #50/#54 | not-started | – | uncertainty valid state |
| AC-EPI-003 | #54/#55 | not-started | – | AI is not evidence |
| AC-SRC-001 | #50/#51 | not-started | – | source layers separated |
| AC-SRC-002 | #51/#55 | not-started | – | findspot roundtrip |
| AC-SRC-003 | #49/#50 | not-started | – | OneDrive/Zotero/Histo-Orla responsibility |
| AC-SRC-004 | #49 | not-started | – | read-first integration |
| AC-METHOD-001 | #60/#50/#59 | not-started | – | method profile ≠ prompt |
| AC-METHOD-002 | #60/#50 | research-needed | #60 active | profile expressiveness derives from SOTA |
| AC-METHOD-003 | #60/#50/#54 | not-started | – | method status/version |
| AC-METHOD-004 | #50/#55/#61 | not-started | – | concrete Method Application traceability |
| AC-METHOD-005 | #54/#61 | not-started | – | fail closed on promotion, not exploration |
| AC-METHOD-006 | #60/#54 | research-needed | #60 active | evidence-starved behavior |
| AC-METHOD-007 | #60/#54 | research-needed | #60 active | overclaim/counterexample prevention |
| AC-METHOD-008 | #60/#59 | research-needed | #60 active | first real Diplomatik/Editions profile |
| AC-RESEARCH-001 | #50/#59 | not-started | – | research hook ≠ hypothesis ≠ finding |
| AC-RESEARCH-002 | #60/#50/#59 | research-needed | #60 active | Evidence Demand routing |
| AC-RESEARCH-003 | #60/#55 | research-needed | #46/#60 active | source does not bound explanatory scope |
| AC-RESEARCH-004 | #60/#50/#55 | research-needed | #60 active | multi-method/domain handoff |
| AC-RESEARCH-005 | #50/#55 | not-started | – | competing explanations remain parallel |
| AC-IR-001 | #53/#59 | not-started | – | exact search without LLM |
| AC-IR-002 | #53/#60 | not-started | – | historical variants |
| AC-IR-003 | #52/#51 | not-started | – | OCR/HTR derivative |
| AC-IR-004 | #52 | not-started | – | research-critical OCR quality |
| AC-AUDIT-001 | #55/#59 | not-started | – | human-readable audit |
| AC-AUDIT-002 | #57/#59 | in-progress | repo bootstrap/governance exists | product-level restartability still to verify |
| AC-AUDIT-003 | #49/#57 | not-started | – | research-ready evidence availability |
| AC-GUARD-001 | #54/#59 | not-started | – | deterministic safeguards |
| AC-TECH-001 | #50/#57 | not-started | – | portable/restartable state |
| AC-TECH-002 | #50/#57 | not-started | – | curated vs regenerable |
| AC-TECH-003 | #56 | not-started | – | rights/privacy admission |
| AC-TECH-004 | #48 | in-progress | #48/non-regression contract | technical subsidiarity + SOTA/best practice |
| AC-UX-001 | #55/#59 | not-started | – | progressive disclosure |
| AC-UX-002 | #60/#59 | research-needed | #60 active | unscharf fragen → fachlich sauber |
| AC-UX-003 | #48/#59 | in-progress | owner scope | private workflow first |

**Overlay count:** 38 / 38 represented.

## 5. Current Delivery Slice

Current priority is a first **scientifically correct vertical slice**, not a reduced MVP definition:

```text
Source metadata / fixture
→ inspected Instance
→ Findspot
→ Excerpt / Observation
→ basic Research Object state
→ Exact Search
→ minimal Audit
→ persistent/exportable handoff
```

Initial criteria expected to move first toward `implemented/verified`:

- REQ-SRC-001/002/004;
- REQ-RET-001;
- REQ-STATE-001/002;
- REQ-UX-001;
- REQ-WF-001 where already formally clear;
- AC-EPI-001/002/003;
- AC-SRC-001/002;
- AC-IR-001;
- AC-AUDIT-001/002;
- AC-TECH-001/002.

This prioritization does **not** demote any other active criterion.

## 6. Update rule

Every material #59 increment must update this ledger in the same work cycle:

1. affected criteria;
2. new status;
3. implementation/test reference;
4. failure/debt if partial;
5. new Acceptance Delta if real use exposed one.

A new criterion accepted under #42 is appended immediately. A criterion is removed only by explicit #42/#44 traceable decision.

## 7. Completion rule

`MVP complete` requires:

- no active criterion silently missing from this ledger;
- all active MVP criteria `verified`, or explicitly `owner-deferred` by owner decision;
- owner-deferred items documented with consequences and revisit condition;
- real U2 end-to-end acceptance;
- scientific overclaim/evidence-starved negative tests;
- fresh-context restartability;
- known technical/scientific debt visible.

> **Coverage is monotone unless the Owner explicitly changes scope.**
