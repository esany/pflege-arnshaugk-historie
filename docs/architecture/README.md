# Histo-Orla – Technical Discovery / Architecture Research Index

**Technical Discovery Owner:** #48  
**Requirements:** #42 `reconciliation-active`  
**Architecture Gate:** #43 `reopened / reassessment-required`  
**Current admission:** `architecture decision not admitted / technical discovery allowed`  
**Project Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Zweck

Dieses Verzeichnis enthält technische Research-/Feasibility-/Assurance-Artefakte und später – **erst nach erneutem #43 PASS** – Architecture Decisions/ADRs.

Der aktuelle Stand ist technisch Greenfield. Ein Contract, Spike oder SOTA-Vergleich ist **kein** Beleg, dass eine Zielarchitektur bereits entschieden ist.

Kanonische Phasenklärung:

`../research/synthesis/phase-reconciliation.md`

## Aktueller Leitpfad

```text
Live Research / Domain Methods
        ↓
#42 Requirements Reconciliation
        ↕
#48 Technical Discovery / Engineering Advisory
        ↓
#43 Architecture Readiness Re-Gate
        ↓ nur bei PASS
#58 Architecture Variants / ADR / MVP Cut
        ↓
#59 Development / Verification
```

## #48 – führende technische Verantwortung vor dem Re-Gate

#48 besitzt:

- technische SOTA-/Best-Practice-Recherche;
- Existing-Tool-/Integration-/Feasibility-Vergleich;
- technische Risiken, Dependencies, Migration, Lock-in, Kosten;
- Priorisierung technischer Unknowns;
- kleine reversible Spikes/Benchmarks mit konkreter Forschungsfrage;
- Rückgabe von `feasibility finding | architecture hypothesis | requirement candidate`.

#48 besitzt nicht:

- Domain Method Truth (#60);
- historische Findings (#46/#47);
- accepted Requirements (#42);
- Zielarchitektur/Stack/MVP vor #43 PASS.

## Technical Intake Gate

```text
PROBLEM / OBSERVED FRICTION
DOMAIN / WORK OWNER
EVIDENCE / REAL FIXTURE
CURRENT STATUS
TECHNICAL QUESTION
SOTA / EXISTING TOOL OPTIONS
SMALLEST DISCRIMINATING TEST
WHAT MAY BE LEARNED
WHAT MAY NOT BE DECIDED YET
RETURN TARGET
```

## Aktive Research-/Feasibility-Pakete

- **#49** – Zotero ↔ OneDrive Source-of-Bytes / Metadata Boundary, read-first
- **#50** – Canonical Research State / Source Identity; technology-neutral Contract-Hypothesen zu bereits accepted Invarianten
- **#51** – Document-/Findspot-Pipeline, bounded research/spike
- **#52** – OCR/HTR Benchmark Research
- **#53** – Historical Retrieval Baseline / Benchmark
- **#54** – Candidate/Promotion / formal prüfbare Invarianten, feasibility
- **#55** – Human-readable Audit Research/Prototype
- **#56** – Rights Admission / Credentials / External Processing
- **#57** – Provider Removal / Export / fresh-context Restartability
- **#61** – Work-Context / Method-Conformance / Handoff als **Technical Assurance Research Hypothesis**

### Fachliche Upstream-Schnittstelle

- **#60** – Domain Method Profiles / Method Truth.

#61 darf erst aus realen #60-Profilen ableiten, welche fachlich geklärten Teile tatsächlich formal/machine-checkable sind. Es besitzt keine Method Truth und friert derzeit kein Workflowmodell ein.

## HOLD / Downstream

- **#58** – Architecture Decision Package: HOLD bis #42 Reconciliation + #43 PASS + belastbare #48 Evidence
- **#59** – MVP Development: BLOCKED bis #42 + #43 + #58

Keine produktive Stack-/Frameworkwahl vor diesem Gate.

## Aktuelle Artefakte

- `contracts/canonical-research-state.md` – #50; working technology-neutral contract, nicht physisches Schema/ADR
- `assurance/method-conformance-work-context.md` – #61; Working Research / Architecture Hypothesis, keine accepted Requirement-/ADR-Quelle
- `assurance/live-pilot-system-analysis-chat-2026-08-31.md` – #61; reale Pilot-Evidence und Requirement-Candidates aus dem Chat-/Work-Context
- `assurance/knowledge-work-project-learnings.md` – #61; pilot-abgeleitete, nicht bindende Transfer-Learnings für zukünftige Wissensarbeitsprojekte

## Technische Grundregeln

- Problem/Requirement vor Lösung.
- Existing tools / Standards vor Eigenentwicklung.
- Dev informiert Requirements; Dev besitzt sie nicht.
- Fachsemantik nicht aus technischer Convenience ableiten.
- deterministische Regeln nur dort erzwingen, wo die wissenschaftliche Semantik bereits geklärt und accepted ist.
- Source/Instance/Derivative/Findspot nicht verschmelzen.
- Provider/Produkt ist Lösung, nicht Requirement.
- kleine reversible Tests vor dauerhaften Entscheidungen.
- AI/RAG/KG/Multi-Agent/Workflow-/Policy-Plattformen nur bei demonstriertem Need und diskriminierender Evidence.
- Technical Research/Spike ≠ Development-Fortschritt.

## Was Technical Discovery jetzt besonders klären soll

Problemgetrieben, nicht als vorgezogene Produktliste:

- Bibliography/source integration;
- Source-Byte storage/sync/local-first und OneDrive/Zotero-Grenze;
- portable/restartable research state / provenance;
- document/derivative/findspot pipeline;
- OCR/HTR/layout processing;
- exact/historical information retrieval;
- machine-checkable validation, soweit fachlich formalisiert;
- audit/research UX;
- rights/security/credentials;
- Betrieb/Performance erst bei realem Bedarf.

## Leitregel

> **Dev exploriert früh, entscheidet spät.**

> **Greenfield ist technische Freiheit, nicht fachliche Definitionsmacht.**