# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Kanonische Detailwahrheit liegt in Requirements-, Research-, Method-, Architecture- und Development-Artefakten.

## 1. Aktueller Projektmodus

Histo-Orla ist ein privates, leanes und agiles Forschungssystem.

`MVP` wird **nicht mehr als kanonische Projektphase oder zusätzliche Requirement-Schicht verwendet**.

Verbindlich gilt:

- die gesamte bereits akzeptierte Requirements-/Quality-/Governance-Basis bleibt aktiv;
- Live-/Domain-Research präzisiert und ergänzt diese Requirements;
- Lean/Agile optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value, nicht den Anspruch;
- State of the Art und Best Practice sind Basis wissenschaftlicher und technischer Entscheidungen;
- technische Umsetzung läuft parallel, sobald ein Requirement-/Constraint-Cluster hinreichend klar ist, ersetzt aber nicht die fachliche Arbeit.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/requirements-coverage.md`
- `docs/research/synthesis/phase-reconciliation.md`

Aktueller Arbeitsfluss:

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

## 2. Requirements / Non-Regression

Aktive Systemanforderungen bestehen mindestens aus:

1. 39 accepted Requirements/Constraints in `requirements-baseline.md`;
2. 13 accepted Extensions aus `requirements-extensions.md`;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints;
4. späteren explizit akzeptierten Deltas unter #42.

Materielle Scope-/Qualitätsänderungen benötigen ein explizites Requirement-/Decision-Delta. Neue Buzzwords, Tools, Frameworks oder Phasenbegriffe ändern keinen akzeptierten Scope implizit.

Delivery-/Verification-Status wird in `docs/development/requirements-coverage.md` geführt.

## 3. Baselines und Präzedenz

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Questions – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risks/Constraints – completed
- #41 Capability/Quality – completed
- #42 Requirements Baseline + accepted Extensions – aktiver Requirements Owner
- #43 historisches Architecture-Readiness-Gate; kein aktuelles Blocking-Gate

Die Baselines bleiben gültig, werden aber durch reale Research-/Methodenbefunde präzisiert.

## 4. Aktive fachliche Work Owner

### #46 – U2 Knau/Orlagau

`in-research / live-use-case / working-research`

Aktueller historischer Fokus: mittelalterliche Quellen-, Herrschafts-, Siedlungs- und Beziehungsräume im Orla-Grenzraum; konkrete Findings, Search Boundaries und Quellenexzerpte unter `docs/research/cases/`.

### #47 – U1 Teich-/Feuchtkulturlandschaft

`in-research / working-research`

### #60 – Domain Method Profiles

`in-research / cross-cutting-method-work-package`

Besitzt Method Truth, nicht Systemarchitektur.

Aktuelle Priorität:

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. weitere Profile problemgetrieben aus #46/#47.

## 5. Requirements Owner #42

#42 ist einziger Owner akzeptierter Systemanforderungen.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`

Neue fachlich belastbare Systembedarfe aus #46/#47/#60 gehen als Requirement-Deltas dorthin. Fachmethodische Wahrheit selbst bleibt #60-Eigentum.

## 6. Technical Lead #48

#48 besitzt:

- technische SOTA-/Best-Practice-/Existing-Tool-Einordnung;
- technische Priorisierung nach Requirement, Dependency, Risiko, fachlichem Nutzen und Reversibilität;
- reversible technische Entscheidungen und Refactoring;
- Integrations-/Feasibility-Spikes;
- evolutionäre Architektur;
- technische Acceptance-/Regression-/Invariant-Tests;
- Rückgabe fachlicher/Requirements-Fragen an #42/#60.

#48 besitzt nicht:

- historische Findings;
- Method Truth;
- Scope-Reduktion akzeptierter Requirements;
- das Recht, fachliche Unsicherheit technisch wegzumodellieren.

## 7. Development & Verification #59

#59 implementiert und verifiziert akzeptierte Requirements. Es ist keine eigene Produktphase und kein Scope-Owner.

Delivery Coverage:

`docs/development/requirements-coverage.md`

Status je Requirement:

`not-started | in-progress | implemented | verified | partial | blocked | research-needed | owner-deferred`.

Technische Arbeit beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist; noch offene Fachsemantik bleibt sichtbar und wird nicht von Dev erfunden.

## 8. Technische Teilpakete

- #49 – Zotero ↔ OneDrive, read-first Integration/Feasibility
- #50 – Canonical Research State / Source Identity
- #51 – Document-/Findspot-Pipeline
- #52 – OCR/HTR Benchmark/Integration
- #53 – Historical Retrieval
- #54 – Promotion / deterministic invariants
- #55 – Human-readable Audit
- #56 – Rights / Credentials / External Processing
- #57 – Provider Removal / Export / Restartability
- #58 – just-in-time ADRs bei materiellen/schwer reversiblen Entscheidungen
- #61 – Work-Context / Method-Conformance / Handoff Technical Research

## 9. Source / Storage Responsibility

```text
OneDrive  = Source of Bytes
Zotero    = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht Source-/Instance-Identität.

## 10. Aktuelle nächste Aktionen

### Inhaltlich führend

1. #46/#47 reale Forschung fortführen.
2. #60 den ersten SOTA-basierten Domain-Method-Block Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik erarbeiten und an realen NHUB-Fällen testen.
3. danach Archivistik/Provenienz/Registraturkunde und historische Philologie/Semantik.
4. neue Systemanforderungen aus diesen Arbeiten als Requirement-Deltas unter #42 konsolidieren.

### Technisch parallel

5. #48 mappt aktive Requirements auf aktuellen technischen SOTA/Best Practice und vorhandene Werkzeuge.
6. #49 Zotero↔OneDrive weiter prüfen.
7. #50/#51 Source/Instance/Findspot/Provenienz so einfach wie hinreichend technisch absichern.
8. #53 Exact Search und #55 Audit dort früh umsetzen, wo sie reale Forschung unmittelbar tragen.
9. #57 Restartability/Research-ready Availability aus frischem Kontext testen.

## 11. Blocker / Decisions

#44 bleibt Register für echte Blocker und Owner-Entscheidungen.

Die frühere DD-001-Entscheidung bleibt historische Provenienz; die aktuelle Steuerung benötigt keine `MVP`-Schicht. Die vollständigen Requirements bleiben unverändert wirksam.

## 12. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- aktuelle historische und methodische Arbeit;
- vollständige aktive Requirements;
- primäre Funktion/Authority;
- Method-/Evidence-Status;
- technischen Delivery-/Verification-Status;
- offene Debt/Blocker;
- nächste Aktion und Persistenzort.

> **Fachdomänen führen. Technologie dient.**

> **Requirements führen den Systemumfang. Lean/Agile optimiert die Mittel.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**
