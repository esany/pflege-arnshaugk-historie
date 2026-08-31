# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk/Orla und für die Entwicklung einer **transdisziplinären historischen Forschungsassistenz**.

Ziel ist ein **funktionierendes, dauerhaft nutzbares Forschungswerkzeug**, das belastbare Quellenarbeit, fachliche Problemübersetzung, regionalisierte Expertise, transdisziplinäre Analyse und einen nachvollziehbaren, restartbaren Forschungszustand unterstützt.

## Pflicht-Bootstrap / Handoff

Vor substantieller Arbeit:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. dieses `README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

Für substantielle Arbeit gilt zusätzlich `AGENTS.md` §13: primäre Funktion, Work Owner, bounded Scope, Method-/Quality-Frame, Authority-Grenzen, Stop/Handoff, Return Condition und Persistenzort müssen rekonstruierbar sein.

## Präzedenz

```text
konkreter Forschungsauftrag / Nutzer-Pain
→ führende Fachdomäne(n)
→ wissenschaftliche Standards / Domain Method / Evidenzbedarf
→ State of the Art + internes Prior Art
→ validierte Needs / Capabilities / Quality Attributes
→ Requirements + Acceptance Criteria
→ Architecture Readiness
→ Architektur / Design
→ Development / Integration
→ technische + wissenschaftliche Verifikation
→ MVP / Nutzung
→ Evaluation / Iteration
```

**Fachdomänen führen. Technologie dient.**  
**Dev informiert Requirements; Dev besitzt sie nicht.**

## Aktuelle Phase – Reconciliation vor Architekturentscheidung

Der erste Durchlauf #28–#43 erzeugte eine v0.1 Discovery-/SOTA-/Requirements-Baseline und zunächst das Gate `architecture-ready-with-bounded-research-debt`.

Der vertiefte Live Case #46 und die daraus entstandene fachwissenschaftliche Methodenschicht #60 haben gezeigt, dass diese Readiness erneut geprüft werden muss. Deshalb sind **#42 Requirements und #43 Architecture Readiness reopened**.

Aktuell gilt:

**`architecture decision not admitted / technical discovery allowed`**

Kanonisch:

`docs/research/synthesis/phase-reconciliation.md`

Arbeitsfluss:

```text
#46/#47 Live Research / Problem Discovery
        ↕
#60 Domain Method SOTA / Operationalisierung
        ↓
#42 Requirements Reconciliation
        ↕
#48 Technical Discovery / Engineering Advisory
        ↓
#43 Architecture Readiness Re-Gate
        ↓ nur bei PASS
#58 Architecture Decision / ADR / MVP Cut
        ↓
#59 Development / Verification
```

### Softwaretechnologischer Stand

Histo-Orla ist **technisch Greenfield**:

- kein produktiver Anwendungscode;
- kein gewählter Runtime-/UI-/Backend-Stack;
- keine entschiedene Persistenz-, Search-, OCR- oder Workflow-Technologie;
- keine validierte Zielarchitektur.

Vorhanden sind wissenschaftliche Invarianten, Requirements v0.1, technische SOTA-/Allocation-Prinzipien und bounded Research-/Feasibility-Hypothesen. Das ist noch keine Systemarchitektur.

## Aktive fachliche Owner

- **#46** – U2 Knau/Orlagau Live Research
- **#47** – U1 Teich-/Feuchtkulturlandschaft Live Research
- **#60** – Domain Method Profiles / fachwissenschaftliche Method Truth
- **#42** – einziger Owner akzeptierter Requirements; aktuell Reconciliation
- **#43** – Architecture Readiness Re-Gate

Methodenbasis:

- `docs/research/methods/README.md`
- `docs/research/methods/domain-method-profile-contract.md`
- #45 Research-/Evidence-Protokoll
- `docs/research/source-identity-protocol.md`

## Führender technischer Owner vor dem Re-Gate

**#48 – Technical Discovery / Engineering Advisory**

#48 darf und soll:

- technische SOTA/Best Practice und vorhandene Tools untersuchen;
- Feasibility, Integrationen, Migration, Lock-in, Kosten und Dependencies prüfen;
- technische Unknowns priorisieren;
- kleine reversible Spikes/Benchmarks durchführen, wenn sie eine konkrete Research-/Requirement-Frage diskriminieren;
- Ergebnisse an #42/#60 als Findings/Candidates zurückgeben.

#48 darf vor #43 PASS **nicht**:

- Fachsemantik definieren;
- Requirements akzeptieren;
- Zielarchitektur, produktiven Stack oder MVP-Schnitt festlegen.

Leitregel:

> **Dev exploriert früh, entscheidet spät.**

## Technische Research-/Feasibility-Workstreams

- **#49** – Zotero ↔ OneDrive Integration, read-first feasibility
- **#50** – Canonical Research State / Source Identity
- **#51** – Document-/Findspot-Pipeline
- **#52** – OCR/HTR Benchmark Research
- **#53** – Historical Retrieval Baseline
- **#54** – Promotion / formal prüfbare Invarianten
- **#55** – Human-readable Audit
- **#56** – Rights / Credentials / External Processing
- **#57** – Provider Removal / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff als Technical Assurance Research Hypothesis

Diese Pakete liefern **Research/Feasibility Evidence**, nicht automatisch Architekturfortschritt.

### HOLD

- **#58** – Architekturvarianten / ADR / MVP Cut: HOLD bis #42 + #43 PASS
- **#59** – produktive MVP-Entwicklung: BLOCKED bis #42 + #43 + #58

## Method Truth vs. technische Conformance

```text
METHOD TRUTH
→ #60 / Fachdomäne / SOTA

TECHNICAL CONFORMANCE RESEARCH
→ #61 / #48
→ untersucht nur, welche bereits fachlich geklärten Teile später formal prüfbar sind
→ Requirement-Deltas zurück an #42
```

Ein Prompt oder technischer Contract ist keine Fachmethode.

## Quellen-/Storage-Verantwortung

```text
OneDrive = Source of Bytes
Zotero   = bibliographische/archivische Verwaltung + Attachment-Referenzen
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht die wissenschaftliche Source-/Instance-Identität.

## Kanonische Einstiege

### Foundational Design

- `docs/research-design/transdisziplinaerer-literaturassistent.md`
- `docs/research-design/README.md`

Foundational, aber nicht alleiniger aktueller Operations-/Requirements-/Architecture-State.

### Research / Requirements

- `docs/research/README.md`
- `docs/research/source-identity-protocol.md`
- `docs/research/methods/`
- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md` – historischer Gate-Report
- `docs/research/synthesis/phase-reconciliation.md` – aktueller Reassessment-State

### Technical Discovery / Architecture Research

- `docs/architecture/README.md`
- `docs/architecture/contracts/canonical-research-state.md`
- `docs/architecture/assurance/method-conformance-work-context.md` – Working Research/Hypothesis, keine ADR

## Governing Principles

- Wissenschaft vor Convenience.
- Method Truth vor Prompt/Technik.
- Kein Wissensmonopol im Chat.
- Exploration offen; Promotion nur mit ausreichender Method-/Evidence-/Validation-Grundlage.
- technische Subsidiarität: vorhandene Werkzeuge vor Eigenbau.
- Provider-Unabhängigkeit des kuratierten Research State.
- Dev informiert Requirements; Dev besitzt sie nicht.
- **Greenfield bedeutet technische Freiheit – nicht fachliche Definitionsmacht.**

## Handoff-Test

Ein neuer kompetenter Bearbeiter muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat aktuelle Phase, Authority, Scope, Methodenstatus, Evidenz, nächste erlaubte Aktion und Return/Handoff korrekt rekonstruieren können.