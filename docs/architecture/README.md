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

## Aktive / geplante technische Work Owner

- #48 – Architecture Execution Control
- #49 – Zotero ↔ OneDrive Source-of-Bytes / Metadata / Research-State Boundary
- #50 – Canonical Research State / Source Identity / providerunabhängige Invarianten

Weitere technische Work Owner werden hier nach ihrer Anlage ergänzt und unter #48 synchronisiert.

## Aktuelles Artefakt

- `contracts/canonical-research-state.md` – #50

## Technische Grundregeln

- kein Stack ohne Requirement-/Acceptance-Bezug;
- Provider/Produkt ist Lösung, nicht Requirement;
- deterministische Invarianten soweit möglich deterministisch erzwingen;
- Source/Instance/Derivative/Findspot nicht aus technischer Convenience verschmelzen;
- read-first bei externen Integrationen;
- Secrets/Credentials niemals im Repo;
- jeder Spike: Hypothese → Setup → Test → Ergebnis → Failure Modes → Disposition;
- jeder Provider muss prinzipiell entfernbar sein, ohne kuratierten Research State epistemisch zu zerstören;
- reale U1/U2/U4-Cases falsifizieren Architektur, definieren sie aber nicht allein.

## Wann Code entsteht

Code entsteht bei einem begrenzten diskriminierenden Prototyp oder nach hinreichender Architecture Decision/MVP-Abgrenzung. Vorher sind Contracts, Test-Harnesses und Integrationsspikes zulässig, wenn sie eine konkrete Architekturfrage entscheiden.

Produktiver MVP-Code wird nicht nur deshalb begonnen, weil eine Technologie attraktiv erscheint.