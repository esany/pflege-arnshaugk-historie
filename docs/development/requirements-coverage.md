# Histo-Orla – Requirements Delivery Coverage

**Status:** `active delivery ledger / 2026-08-31`  
**Owner:** #59 Development & Verification  
**Technical Lead:** #48  
**Requirements Owner:** #42  
**Governance:** `docs/governance/lean-agile-non-regression.md`

## 1. Zweck

Diese Datei ist die monotone **Delivery-/Verification-Sicht auf alle aktiven Systemanforderungen**.

Sie ist keine zweite Requirement Truth. Kanonische Anforderungen liegen in:

1. `docs/research/synthesis/requirements-baseline.md` – 39 accepted Requirements/Constraints;
2. `docs/research/synthesis/requirements-extensions.md` – 13 accepted Extensions aus Live-/Domain-Research;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints.

Ein Requirement verschwindet nicht durch Priorisierung, Chat-Wechsel, neue Technikbegriffe oder einen anderen Delivery-Schnitt.

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
- `nicht im aktuellen Inkrement` bleibt `not-started`, nicht `owner-deferred`;
- `implemented` bedeutet Funktion vorhanden, `verified` erfordert passende Acceptance-/Regression-/Invariant-/Real-Case-Tests;
- `partial` benennt konkret die fehlende Qualität/Funktion;
- Scope-/Qualitätsänderungen erfolgen nur unter #42/#44, nicht in diesem Ledger.

## 3. Requirements Baseline – Coverage

| Requirement | Primary owner/work packages | Status | Notes |
|---|---|---|---|
| REQ-EPI-001 | #60/#54/#55/#59 | not-started | Domain method + evidence standard traceability |
| REQ-EPI-002 | #60/#59 | not-started | professional problem translation |
| REQ-EPI-003 | #50/#60/#59 | not-started | terminology layers/context |
| REQ-EPI-004 | #50/#54/#55 | not-started | unresolved/contradiction first-class |
| REQ-EPI-005 | #54/#55 | not-started | AI ≠ evidence/independent validation |
| REQ-SRC-001 | #50/#51 | not-started | source identity ≠ representation |
| REQ-SRC-002 | #49/#50/#51 | not-started | inspected instance status |
| REQ-SRC-003 | #50/#51/#55 | not-started | editorial/normalization separation |
| REQ-SRC-004 | #51/#55 | not-started | findspot roundtrip |
| REQ-SRC-005 | #60/#59 | not-started | archive provenance/function routing |
| REQ-OCR-001 | #52/#51 | not-started | OCR/HTR derivative + parentage |
| REQ-OCR-002 | #52/#51 | not-started | page/folio/region mapping |
| REQ-OCR-003 | #52 | not-started | research-critical OCR benchmark |
| REQ-RET-001 | #53/#59 | not-started | exact/auditable search without LLM |
| REQ-RET-002 | #53/#60 | not-started | controlled historical variants |
| REQ-RET-003 | #53/#57 | not-started | query/corpus provenance |
| REQ-RET-004 | #53/#55/#60 | not-started | bounded negative findings |
| REQ-RET-005 | #53 | not-started | semantic/RAG additive only if benchmark-admitted |
| REQ-CRIT-001 | #50/#55/#60 | not-started | claim-specific source dependence |
| REQ-CRIT-002 | #50/#55/#60 | not-started | discrepancy before harmonization |
| REQ-ENT-001 | #54/#50 | not-started | candidate→promotion / false-merge protection |
| REQ-REL-001 | #50/#55/#60 | not-started | proxy/co-presence ≠ relation |
| REQ-SPAT-001 | #50/#55/#60 | not-started | temporal/multi-scale place context |
| REQ-ACT-001 | #50/#55/#60 | not-started | action/motive/attribution/structure separation |
| REQ-SYN-001 | #50/#55/#60 | not-started | evidence axes remain distinct |
| REQ-SYN-002 | #55/#60/#59 | not-started | synthesis preserves alternatives |
| REQ-UX-001 | #55/#59 | not-started | finding→source/findspot→method audit |
| REQ-UX-002 | #54/#55/#59 | not-started | challenge/correct/demote without micromanagement |
| REQ-VAL-001 | #54/#55/#60 | not-started | consequence-based validation levels |
| REQ-VAL-002 | #55/#60 | not-started | honest independent specialist validation status |
| REQ-WF-001 | #54/#59 | not-started | deterministic formal invariants |
| REQ-WF-002 | #57/#59 | not-started | reproducible/restartable processing/search |
| REQ-STATE-001 | #50/#57/#59 | not-started | provider-/chat-independent portable state |
| REQ-STATE-002 | #50/#57 | not-started | curated vs regenerable state |
| REQ-INT-001 | #49/#57 | not-started | integration escape hatch |
| REQ-LEAN-001 | #48 | in-progress | smallest sufficient components; SOTA/existing tools first |
| REQ-RGT-001 | #56 | not-started | external-processing rights admission |
| REQ-RGT-002 | #56 | not-started | privacy screening |
| REQ-BND-001 | #50/#59 | not-started | mediation cannot back-write research state |

**Baseline:** 39 / 39 represented.

## 4. Accepted Requirements Extensions – Coverage

| Requirement | Primary owner/work packages | Status | Notes |
|---|---|---|---|
| REQ-EPI-006 | #50/#59 | not-started | semantic research-state roles remain distinct |
| REQ-INT-002 | #49/#50 | not-started | OneDrive/Zotero/Histo-Orla responsibility boundary |
| REQ-MTH-001 | #60/#50/#59 | research-needed | versioned Domain Method Profiles |
| REQ-MTH-002 | #60/#50 | research-needed | profile expressiveness derives from fachlicher SOTA |
| REQ-MTH-003 | #60/#50/#55/#61 | research-needed | method status/version/application traceability |
| REQ-MTH-004 | #60/#54/#61 | research-needed | exploration open; promotion method/evidence bound |
| REQ-MTH-005 | #60/#54 | research-needed | overclaim/counterexample/evidence-starved QA |
| REQ-RSCH-001 | #50/#59 | not-started | research hook ≠ hypothesis ≠ finding |
| REQ-RSCH-002 | #60/#50/#59 | research-needed | Evidence Demand routing |
| REQ-RSCH-003 | #60/#55 | research-needed | source finding ≠ explanatory research space |
| REQ-RSCH-004 | #60/#50/#55 | research-needed | multi-method/domain handoff |
| REQ-STATE-003 | #49/#57 | not-started | research-ready evidence availability |
| REQ-UX-003 | #55/#59 | not-started | progressive disclosure without epistemic hiding |

**Extensions:** 13 / 13 represented.

## 5. Current content-driven priorities

Delivery-Priorisierung richtet sich nach dem aktuellen fachlichen/requirements-seitigen Stand, nicht nach einer separaten Produktphase.

### Inhaltlich aktiv

- #46/#47 Live Research;
- #60 erster SOTA-Block Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik;
- #42 Requirements-Konsolidierung aus realen Domain-/Case-Befunden.

### Technisch parallel sinnvoll

- #48 prüft für konkrete Requirements den aktuellen SOTA/Best Practice und die leansten geeigneten Mittel;
- #49 Zotero ↔ OneDrive read-first Feasibility/Integration;
- #50/#51 Source/Instance/Findspot-State und Provenienz;
- #53 Exact Search;
- #55 Audit;
- #57 Restartability/Availability.

Eine technische Implementierung darf beginnen, sobald ein Requirement-/Constraint-Cluster hinreichend klar ist. Sie ist **keine eigene Phase, die fachliche Arbeit ersetzt oder ihr vorausläuft**.

## 6. Update Rule

Jede materielle Implementierung aktualisiert in demselben Work Cycle:

1. betroffene Requirements;
2. Delivery-/Verification-Status;
3. Implementation/Test-Referenz;
4. Failure/Debt bei `partial`;
5. neue fachliche/systemische Deltas zurück an #42/#60.

Neue akzeptierte Requirements werden ergänzt. Entfernt/geändert wird nur durch tracebare #42/#44-Entscheidung.

> **Coverage ist monoton, solange der Owner den Scope nicht explizit ändert.**
