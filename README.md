# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk/Orla und für die Entwicklung einer **privaten, transdisziplinären historischen Forschungsassistenz**.

Ziel ist ein früh nutzbares, dauerhaft belastbares Forschungswerkzeug, das Quellenarbeit, fachliche Problemübersetzung, domänenspezifische Methoden, transdisziplinäre Analyse und einen nachvollziehbaren, restartbaren Forschungszustand unterstützt.

## Pflicht-Bootstrap / Handoff

Vor substantieller Arbeit:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. dieses `README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

## Projektmodus

Histo-Orla ist privat, lean und agil.

`MVP` wird **nicht als kanonische Projektphase oder zusätzliche Requirement-Schicht verwendet**.

Verbindlich gilt:

- die gesamte bereits akzeptierte Requirements-/Quality-/Governance-Basis bleibt aktiv;
- Live-/Domain-Research und reale Nutzung präzisieren/ergänzen die Requirements;
- fachlicher SOTA und technische SOTA/Best Practice sind Basis der jeweiligen Entscheidungen;
- Lean/Agile optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value, nicht den Anspruch;
- technische Umsetzung beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist, und läuft rückgekoppelt mit realer Forschung;
- formal geklärte Schutzregeln werden deterministisch geprüft statt dauerhaft nur Chat-/Prompt-Compliance zu bleiben;
- materielle technische Arbeit bleibt auf Nutzer-/Forschungsdriver, Requirements und Governance rückführbar; reale Owner-/Nutzungsrückmeldung schließt die Schleife.

Kanonisch:

- `docs/research/discovery/problem-baseline.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`
- `docs/architecture/requirements-derivation.md`
- `docs/architecture/assurance/requirements-assurance-harness.md`
- `docs/architecture/assurance/value-decision-delivery-assurance.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/requirements-coverage.md`
- `docs/research/synthesis/phase-reconciliation.md`

## Aktueller Arbeitsfluss

```text
Goal / Need / Pain / reale Research-Friktion (#28, #46/#47, Owner Feedback)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↕
Accepted Requirements + Extensions (#42)
        ↕
Requirement Structure / Authority / Dependencies (#42)
        ↕
Deterministic Requirements QA (#62)
        ↕
Technical Derivation: Concerns / SOTA / Options (#48)
        ↓
Decision / Implementation Trace (#63)
        ↓
Development & Verification (#59)
        ↓
reale Nutzung / Owner-Feedback (#63)
        ↺
Pain bleibt | bestätigt | Regression | neuer Need | Requirement-/Method-/Decision-Delta
```

## Requirements

#42 ist der kanonische Owner akzeptierter Systemanforderungen.

Aktive Basis:

- 39 accepted Requirements/Constraints in `requirements-baseline.md`;
- 14 accepted Extensions aus vertieftem Live-/Domain-/Owner-Feedback in `requirements-extensions.md`;
- bindende Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints.

Neu cross-cutting: **REQ-TRACE-001** verlangt die dauerhafte Rückführung materieller Systemarbeit von Goals/Needs/Pains über Requirement, technische Entscheidung, Implementation und Verification bis zu realer Nutzung/Owner-Feedback.

Innere Struktur und Traceability:

- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`

Für neue bzw. materiell bearbeitete Requirements werden insbesondere Motivation, konkrete Herkunft/Evidence, Domain Authority, Acceptance Authority, Scope, Dependencies, Criticality, Architecture Significance und Verification unterschieden. `#42` besitzt den Requirement-Lifecycle; fachliche Kompetenz besitzt die Semantik; #48/#59 besitzen technische Ableitung/Umsetzung.

`Criticality` ist ausdrücklich **nicht** dasselbe wie aktuelle Delivery-Reihenfolge.

Delivery-/Verification-Coverage:

`docs/development/requirements-coverage.md`

Neue Begriffe, Tools, Frameworks oder Phasen superseden bestehenden accepted Scope niemals implizit.

## Deterministic Requirements Assurance – #62

#62 besitzt den generischen formalen Requirements-QA-Baustein:

- Contract: `docs/architecture/assurance/requirements-assurance-harness.md`
- Schema: `tools/requirements/requirement-record.schema.json`
- QA-/Traceability-Projektion: `tools/requirements/data/records.json`
- Validator: `tools/requirements/validate.py`
- Regressionstests: `tools/requirements/tests/`
- CI: `.github/workflows/requirements-assurance.yml`

Leitgrenze:

> **Schema prüft Form. Validator prüft formale Beziehungen/Invarianten. Fachreview prüft Bedeutung.**

Ein formaler PASS ist keine wissenschaftliche Validierung.

Aktueller Realtest: Requirements-Assurance-Lauf `33479807761` erfolgreich; `REQ-TRACE-001` ist selbst als strukturierter Requirement-Record und in der Coverage erfasst.

## Value / Decision / Delivery / Feedback Assurance – #63

#63 ergänzt die Requirements-QA um die ausführbare Traceability der gesamten technischen Wertschleife.

Machine-readable Bausteine:

- `tools/assurance/trace-record.schema.json`
- `tools/assurance/governance-registry.json`
- `tools/assurance/policy.json`
- `tools/assurance/data/trace-records.json`
- `tools/assurance/validate.py`
- `tools/assurance/tests/`
- `.github/workflows/project-assurance.yml`

Der formale Guard prüft u. a.:

```text
materielle technische Änderung
→ aktueller Implementation Trace
→ accepted Requirement(s)
→ G/N/P-Driver
→ bindende Governance
→ Decision bzw. begründete reversible Ausnahme
→ Implementation
→ Verification
→ bei owner-workflow-relevanter Acceptance: reales Owner-Feedback
```

Ein früherer `verified` Implementation-Record schaltet einen Codepfad nicht dauerhaft frei. Neue kontrollierte technische Änderungen brauchen einen aktuellen Trace-Kontext.

Reale Nutzung/Owner-Feedback ist **Product-/Workflow-Evidence**, nicht historische/wissenschaftliche Evidenz. Negative Outcomes müssen einen sichtbaren Delta-Pfad erzeugen; `owner-workflow-acceptance` darf nicht durch technische Selbsttests simuliert werden.

Project-Assurance-Lauf `33479807679` ist erfolgreich; 15 Assurance-Spine-Regressionstests bestanden. Das aktuelle Owner-Feedback, das diesen Ausbau ausgelöst hat, ist als `FB-20260901-001` persistiert und bleibt bis zur realen Owner-Akzeptanz offen.

## Aktive Owner

### Domain / Research

- **#46** – U2 Knau/Orlagau Live Research
- **#47** – U1 Teich-/Feuchtkulturlandschaft Live Research
- **#60** – Domain Method Profiles / fachwissenschaftliche Method Truth
- **#42** – accepted Requirements / Lifecycle / Traceability

### Technical Lead / Development / Assurance

- **#48** – Technical Lead: lean Umsetzung, SOTA/Best Practice, evolutionäre Architektur
- **#59** – System Development & Verification
- **#58** – just-in-time ADRs bei materiellen/schwer reversiblen Entscheidungen
- **#62** – deterministische Requirements-QA
- **#63** – Goal/Need/Pain → Requirement → Decision → Delivery → Feedback Assurance

Technische Ableitungslogik:

`docs/architecture/requirements-derivation.md`

```text
Requirement / Cluster
→ upstream Goal/Need/Pain verstehen
→ System Responsibility
→ Architecture Concern / Quality Attribute
→ Technical Research Question
→ Existing Tools / Standards / Patterns
→ Candidate Approach
→ Trade-off / Reversibility
→ Decision / Implementation Trace
→ implement | spike/benchmark | ADR | #44
→ Verification
→ reale Nutzung / Feedback
```

### Technische Teilpakete

- **#49** – Zotero ↔ OneDrive Integration
- **#50** – Canonical Research State / Source Identity
- **#51** – Document-/Findspot-Pipeline
- **#52** – OCR/HTR Benchmark / Integration
- **#53** – Historical Retrieval
- **#54** – Promotion / deterministische Invarianten
- **#55** – Human-readable Audit
- **#56** – Rights / Credentials / External Processing
- **#57** – Provider Removal / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff Technical Research

## Dev Authority Boundary

Dev darf reversible technische Entscheidungen früh treffen, bestehende Tools/Standards bevorzugen und refactoren.

Dev muss:

- den vollständigen Requirement-Scope kennen und sichtbar halten;
- Motivation, Goals/Needs/Pains, Scope, Dependencies und fachliche Authority der aktiv bearbeiteten Requirements verstehen;
- SOTA/Best Practice für konkrete Entscheidungen proportional prüfen;
- zunächst Architecture Concerns und Technical Research Questions ableiten, bevor eine konkrete Technologie zur Lösung erklärt wird;
- formale Requirements-QA über #62 und technische Value-/Decision-/Delivery-Traceability über #63 absichern, wo operationalisiert;
- fehlende/partielle Umsetzung sichtbar führen;
- die leanste **hinreichende** Lösung wählen, nicht den Anspruch verkleinern;
- reale Nutzung/Feedback zurück in Requirements/Decisions routen, statt Erfolg allein aus technischen Tests abzuleiten.

Dev darf nicht:

- Fachsemantik oder Method Truth erfinden;
- akzeptierte Requirements still abschwächen oder streichen;
- technische Präferenz als Requirement Source behandeln;
- AI zur Evidenz-/Truth-Instanz machen;
- wissenschaftliche Unsicherheit aus Convenience eliminieren;
- Prototypqualität als vollständige Erfüllung ausgeben;
- Owner-/Nutzerakzeptanz durch einen technischen Selbsttest simulieren;
- irreversible/teure/lock-in-relevante Entscheidungen ohne explizite Begründung treffen.

## Method Truth

#60 operationalisiert Fachmethoden SOTA-basiert. Aktuelle erste Priorität:

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. weitere Profile problemgetrieben aus #46/#47.

Methodische Candidates dürfen Exploration anleiten, aber keine höhere wissenschaftliche Sicherheit vortäuschen.

## Quellen-/Storage-Verantwortung

```text
OneDrive  = Source of Bytes
Zotero    = bibliographische/archivische Verwaltung + Attachment-Referenzen
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht die wissenschaftliche Source-/Instance-Identität.

## Kanonische Einstiege

### Governance

- `AGENTS.md`
- `docs/governance/lean-agile-non-regression.md`

### Research / Requirements

- `docs/research/README.md`
- `docs/research/discovery/problem-baseline.md`
- `docs/research/source-identity-protocol.md`
- `docs/research/methods/`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`
- `docs/research/synthesis/phase-reconciliation.md`

### Technical Delivery / Assurance

- `docs/architecture/README.md`
- `docs/architecture/requirements-derivation.md`
- `docs/architecture/assurance/requirements-assurance-harness.md`
- `docs/architecture/assurance/value-decision-delivery-assurance.md`
- `tools/requirements/README.md`
- `tools/assurance/`
- `docs/development/requirements-coverage.md`
- `docs/architecture/contracts/canonical-research-state.md`
- `docs/architecture/assurance/method-conformance-work-context.md`

## Governing Principles

- **Lean heißt kleinste hinreichende Lösung – nicht kleinster Anspruch.**
- **Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**
- **State of the Art und Best Practice sind Basis der Mittelwahl.**
- **Needs/Pains/Goals begründen das Warum; Requirements operationalisieren das Was; Technik entscheidet das Wie; reale Nutzung schließt die Schleife.**
- Fachdomänen führen. Technologie dient.
- Method Truth kommt aus Fach-SOTA, nicht aus Prompt/Technik.
- Kein Wissensmonopol im Chat.
- Exploration offen; wissenschaftliche Promotion bleibt evidenz-/methodengebunden.
- vorhandene Tools/Standards vor Eigenbau;
- Provider-Unabhängigkeit des kuratierten Research State;
- Architecture ist Mittel zur Umsetzung, kein Selbstzweck.
- **Requirement Source, fachliche Authority, Requirement Lifecycle und technische Umsetzung sind unterschiedliche Verantwortlichkeiten.**
- **Formale Regeln werden, sobald operationalisiert, durch Code/Tests statt durch Modellselbstkontrolle abgesichert.**

## Handoff-Test

Ein neuer kompetenter Bearbeiter muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat aktuelle Aufgabe, Authority, vollständige aktive Requirements, Motivation/Origin/Dependencies aktiv bearbeiteter Requirements, upstream Goal/Need/Pain, Methodenstatus, Evidenz, technische Entscheidungen/Implementation/Verification, formale QA-Regeln, reale Owner-/Nutzungsrückmeldung oder offenen Feedback-Bedarf, Delivery-/Verification-Status, nächste erlaubte Aktion und Persistenzort rekonstruieren können.
