# Histo-Orla – Architecture / Technical Delivery Index

**Phase Owner:** #48  
**Gate:** #43 `architecture-ready-with-bounded-research-debt`  
**Requirements:** #42  
**Project Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Zweck

Dieses Verzeichnis enthält substanzielle Architekturartefakte und technische Entscheidungs-/Experimentergebnisse nach dem Requirements-/Readiness-Gate.

Es ist kein Ablageort für spekulative Future-Proof-Designs. Dateien entstehen nur, wenn ein Work Package tatsächlichen Inhalt erzeugt.

## Leitpfad

```text
#42 Requirements
→ Architecture Contracts / Invariants / Assurance
→ reversible Spikes / Benchmarks
→ Thin Vertical Slice
→ Variantenvergleich / Trade-offs
→ ADRs
→ MVP Cut
→ Implementation
→ Verification / Evaluation
```

## Technische Work Owner

### Phase Control / Integrationen / Kerncontract

- **#48** – Architecture Execution Control
- **#49** – Zotero ↔ OneDrive Source-of-Bytes / Metadata / Research-State Boundary
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten + Method-/Work-/Review-Provenienz

### P0/P1 Contracts, Spikes und Verification

- **#51** – Document-/Findspot-Pipeline / Source→Excerpt-Roundtrip
- **#52** – OCR/HTR Processor Contract + research-critical Benchmark Harness
- **#53** – Historical Retrieval Baseline: Exact, Varianten, Query Log, Findspots
- **#54** – Candidate→Review→Promotion + deterministic invariant enforcement, einschließlich Method-/Authority-Transition Guards
- **#55** – Human-readable Research Audit View bis Method Application/Profile/Review
- **#56** – Rights Admission, Credentials und External-Processing Guards
- **#57** – Provider Removal, Export und fresh-context Restartability
- **#61** – Executable Work-Context, Method-Conformance und Handoff Assurance

### Fachliche Upstream-Schnittstelle

- **#60** – Domain Method Profiles; besitzt fachliche Method Truth/SOTA, nicht technische Enforcement.

#61 operationalisiert formal prüfbare Conformance- und Handoff-Invarianten aus #42/#60, ohne wissenschaftliches Urteil zu determinisieren.

### Decision / Delivery

- **#58** – 2–3 Architekturvarianten, Trade-off-/Loss-Matrix, ADRs, MVP Cut
- **#59** – MVP Development & Verification; durch #58 blockiert

## Dependency Map

```text
#50 Canonical State / Identity / Method Provenance
   ├─→ #54 Promotion / Transition Invariants
   ├─→ #56 Rights Admission
   ├─→ #55 Audit Contract
   └─→ #57 Provider Removal / Resume

#60 Domain Method Profiles ─────┐
                               ├─→ #61 Method Conformance / Work Context
#50 ────────────────────────────┘          │
                                           ├─→ #54
                                           ├─→ #55
                                           └─→ #57

#49 Zotero / OneDrive Resolver
   ↓
#51 Document / Findspot Pipeline
   ├─→ #52 OCR/HTR End-to-End
   └─→ #53 Historical Retrieval End-to-End

belastbare Evidence aus #49–#57/#61
   ↓
#58 Architecture Variants / ADR / MVP Cut
   ↓
#59 Development / Verification
```

Live Research #46/#47 dient als reale Falsifikation. #60/#61 blockieren Exploration nicht pauschal; sie sichern, dass fehlende Method-/Evidence-/Validation-Grundlage nicht durch Modellplausibilität zu consequential State promoted wird.

## Aktuelle Artefakte

- `contracts/canonical-research-state.md` – #50
- `assurance/method-conformance-work-context.md` – #61

Weitere Dateien werden erst bei substantiellem Inhalt erzeugt.

## Technische Grundregeln

- kein Stack ohne Requirement-/Acceptance-Bezug;
- Provider/Produkt ist Lösung, nicht Requirement;
- deterministische Invarianten soweit möglich deterministisch erzwingen;
- **fail closed on promotion, not on exploration**;
- Fachmethode (#60) und deren technische Conformance (#61/#54) bleiben getrennte Verantwortlichkeiten;
- Source/Instance/Derivative/Findspot nicht aus technischer Convenience verschmelzen;
- Method Profile, konkrete Method Application, Work Context, Review/Validation und Prompt/Model Run nicht still verschmelzen;
- read-first bei externen Integrationen;
- Secrets/Credentials niemals im Repo;
- jeder Spike: Hypothese → Setup → Test → Ergebnis → Failure Modes → Disposition;
- jeder Provider muss prinzipiell entfernbar sein, ohne kuratierten Research State epistemisch zu zerstören;
- reale U1/U2/U4-Cases falsifizieren Architektur, definieren sie aber nicht allein;
- produktiver Code folgt Architecture Decision/MVP Cut; diskriminierende Prototypen, Validatoren und Contract-Projektionen dürfen vorher entstehen, wenn sie auf accepted Requirements rückführbar sind.

## SOTA-/Best-Practice-Referenzrahmen für Assurance

#61 prüft technologieoffen insbesondere:

- schema-as-contract / maschinenlesbare Validierung;
- W3C PROV für Activity-/Entity-/Agent- und Revisionsprovenienz;
- RO-Crate / Workflow Run RO-Crate für portable Research Objects und Ausführungsprovenienz;
- Policy-as-Code als Pattern für getrennte Policy Definition und Enforcement.

Keiner dieser Ansätze ist allein durch Aufnahme in den Referenzrahmen als Zieltechnologie entschieden. Bevorzugt wird die kleinste hinreichende, lokal auditierbare und providerunabhängige Lösung.

## Development Visibility

Bis #43 war produktive Implementierung bewusst nach Requirements/Architecture Readiness verschoben. Seit der aktuellen Phase besitzt Development einen expliziten Pfad bis #59.

Damit gilt ab jetzt:

```text
Technical Contract/Spike ohne Ergebnis
≠ Development-Fortschritt

getestete Architecture/Assurance Evidence
→ Decision
→ implementierter MVP
→ technische + wissenschaftliche Verification
= Delivery-Fortschritt
```

Der Repo-Zustand soll diese Kette jederzeit sichtbar machen.