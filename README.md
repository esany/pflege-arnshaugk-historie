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
- Live-/Domain-Research präzisiert und ergänzt die Requirements;
- fachlicher SOTA und technische SOTA/Best Practice sind Basis der jeweiligen Entscheidungen;
- Lean/Agile optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value, nicht den Anspruch;
- technische Umsetzung beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist, und läuft rückgekoppelt mit realer Forschung.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/requirements-coverage.md`
- `docs/research/synthesis/phase-reconciliation.md`

## Aktueller Arbeitsfluss

```text
Live Research / Problem- und Quellenarbeit (#46/#47)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↕
Accepted Requirements + Extensions (#42)
        ↕
Technical Lead: SOTA / Best Practice / Existing Tools / Umsetzung (#48)
        ↕
Development & Verification (#59)
        ↓
reale Nutzung
        ↺
Finding / Method / Requirement / Technical Delta
```

## Requirements

#42 ist der kanonische Owner akzeptierter Systemanforderungen.

Aktive Basis:

- 39 accepted Requirements/Constraints in `requirements-baseline.md`;
- 13 accepted Extensions aus vertieftem Live-/Domain-Research in `requirements-extensions.md`;
- bindende Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints.

Delivery-/Verification-Coverage:

`docs/development/requirements-coverage.md`

Neue Begriffe, Tools, Frameworks oder Phasen superseden bestehenden accepted Scope niemals implizit.

## Aktive Owner

### Domain / Research

- **#46** – U2 Knau/Orlagau Live Research
- **#47** – U1 Teich-/Feuchtkulturlandschaft Live Research
- **#60** – Domain Method Profiles / fachwissenschaftliche Method Truth
- **#42** – accepted Requirements

### Technical Lead / Development

- **#48** – Technical Lead: lean Umsetzung, SOTA/Best Practice, evolutionäre Architektur
- **#59** – System Development & Verification
- **#58** – just-in-time ADRs bei materiellen/schwer reversiblen Entscheidungen

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
- SOTA/Best Practice für konkrete Entscheidungen proportional prüfen;
- fehlende/partielle Umsetzung sichtbar führen;
- die leanste **hinreichende** Lösung wählen, nicht den Anspruch verkleinern.

Dev darf nicht:

- Fachsemantik oder Method Truth erfinden;
- akzeptierte Requirements still abschwächen oder streichen;
- AI zur Evidenz-/Truth-Instanz machen;
- wissenschaftliche Unsicherheit aus Convenience eliminieren;
- Prototypqualität als vollständige Erfüllung ausgeben;
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
- `docs/research/source-identity-protocol.md`
- `docs/research/methods/`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/phase-reconciliation.md`

### Technical Delivery

- `docs/architecture/README.md`
- `docs/development/requirements-coverage.md`
- `docs/architecture/contracts/canonical-research-state.md`
- `docs/architecture/assurance/method-conformance-work-context.md`

## Governing Principles

- **Lean heißt kleinste hinreichende Lösung – nicht kleinster Anspruch.**
- **Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**
- **State of the Art und Best Practice sind Basis der Mittelwahl.**
- Fachdomänen führen. Technologie dient.
- Method Truth kommt aus Fach-SOTA, nicht aus Prompt/Technik.
- Kein Wissensmonopol im Chat.
- Exploration offen; wissenschaftliche Promotion bleibt evidenz-/methodengebunden.
- vorhandene Tools/Standards vor Eigenbau;
- Provider-Unabhängigkeit des kuratierten Research State;
- Architecture ist Mittel zur Umsetzung, kein Selbstzweck.

## Handoff-Test

Ein neuer kompetenter Bearbeiter muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat aktuelle Aufgabe, Authority, vollständige aktive Requirements, Methodenstatus, Evidenz, technischen Delivery-/Verification-Status, nächste erlaubte Aktion und Persistenzort rekonstruieren können.
