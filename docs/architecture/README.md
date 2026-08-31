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
→ Architecture Contracts
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
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten

### P0/P1 Contracts, Spikes und Verification

- **#51** – Document-/Findspot-Pipeline / Source→Excerpt-Roundtrip
- **#52** – OCR/HTR Processor Contract + research-critical Benchmark Harness
- **#53** – Historical Retrieval Baseline: Exact, Varianten, Query Log, Findspots
- **#54** – Candidate→Review→Promotion + deterministic invariant enforcement
- **#55** – Human-readable Research Audit View
- **#56** – Rights Admission, Credentials und External-Processing Guards
- **#57** – Provider Removal, Export und Restartability

### Decision / Delivery

- **#58** – 2–3 Architekturvarianten, Trade-off-/Loss-Matrix, ADRs, MVP Cut
- **#59** – MVP Development & Verification; durch #58 blockiert

## Dependency Map

```text
#50 Canonical State / Identity
   ├─→ #54 Promotion / Invariants
   ├─→ #56 Rights Admission
   ├─→ #55 Audit Contract
   └─→ #57 synthetic provider-removal tests

#49 Zotero / OneDrive Resolver
   ↓
#51 Document / Findspot Pipeline
   ├─→ #52 OCR/HTR End-to-End
   └─→ #53 Historical Retrieval End-to-End

#50 + #49 + #51 + #53 + #54 + #56 + #57
   ↓
#58 Architecture Variants / ADR / MVP Cut
   ↓
#59 Development / Verification
```

#52 und #55 können teilweise parallel vorbereitet werden. Live Research #46/#47 dient als reale Falsifikation und muss für die case-unabhängigen Contracts nicht vollständig abgeschlossen sein.

## Aktuelles Artefakt

- `contracts/canonical-research-state.md` – #50

Weitere Dateien werden erst bei substantiellem Inhalt erzeugt.

## Technische Grundregeln

- kein Stack ohne Requirement-/Acceptance-Bezug;
- Provider/Produkt ist Lösung, nicht Requirement;
- deterministische Invarianten soweit möglich deterministisch erzwingen;
- Source/Instance/Derivative/Findspot nicht aus technischer Convenience verschmelzen;
- read-first bei externen Integrationen;
- Secrets/Credentials niemals im Repo;
- jeder Spike: Hypothese → Setup → Test → Ergebnis → Failure Modes → Disposition;
- jeder Provider muss prinzipiell entfernbar sein, ohne kuratierten Research State epistemisch zu zerstören;
- reale U1/U2/U4-Cases falsifizieren Architektur, definieren sie aber nicht allein;
- produktiver Code folgt Architecture Decision/MVP Cut; diskriminierende Prototypen dürfen vorher entstehen.

## Development Visibility

Bis #43 war produktive Implementierung bewusst nach Requirements/Architecture Readiness verschoben. Seit der aktuellen Phase besitzt Development einen expliziten Pfad bis #59.

Damit gilt ab jetzt:

```text
Technical Contract/Spike ohne Ergebnis
≠ Development-Fortschritt

getestete Architecture Evidence
→ Decision
→ implementierter MVP
→ Verification
= Delivery-Fortschritt
```

Der Repo-Zustand soll diese Kette jederzeit sichtbar machen.