# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-09-03  
**State Owner:** #1; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Kanonische Detailwahrheit liegt in Requirements-, Research-, Method-, Architecture- und Development-Artefakten.

## 1. Aktueller Projektmodus

Histo-Orla ist ein privates, leanes und agiles Forschungssystem.

`MVP` wird **nicht mehr als kanonische Projektphase oder zusätzliche Requirement-Schicht verwendet**.

### Aktuelle strukturelle Review-/Audit-Inputs

- **#64** – Product-/Research-Value gegen Governance-Komplexität: aktuelles Owner-Feedback bewertet Root-/Handoff-Sicht als zu meta-lastig und U1–U4 als breite Research Journeys statt praktisch scharf geschnittene Piloten. Künftige praktische Tests sollen als kleine Vertical Research Slices historischen Research Output und System-Learning sichtbar trennen.
- **#70** – AI-resilientes Projekthandling: Root-Cause-Audit gegen reale KI-Failure-Modes und `esany/Wissensarbeit` als generische Strukturreferenz. Schutzregeln werden nicht als Selbstzweck geprüft, sondern entlang `beobachtetes KI-Phänomen/Symptom → ursprüngliche Motivation/Evidence → aktuelle Relevanz und Abhängigkeiten → eigentliches Schutzgut/Ziel → Root Cause → kleinste wirksame Gegenmaßnahme`. D1 Safe Mutation / Progress ist inzwischen auf `main` implementiert (`8babc69`): bounded local writes werden aus fresh state konstruiert, destructive mismatch wird blockiert und bereits erfüllter Zielzustand ergibt `NO_CHANGE`. PR #74 (`5e358a6`) lässt `Project Assurance` auf jedem Pull Request laufen und bereitet einen globalen Required Check vor. Die verbleibende repo-weite Prevention gegen direct GitHub writes ist als `DD-20260903-001` in #44 isoliert, weil `main` unprotected ist und der aktuelle Connector Rulesets/Branch Protection nicht schreiben kann. Der Audit soll zugleich zeigen, welche aktive Governance-Doppelung nach struktureller Absicherung entfallen oder abgeleitet werden kann.

Verbindlich gilt:

- die gesamte bereits akzeptierte Requirements-/Quality-/Governance-Basis bleibt aktiv;
- Live-/Domain-Research und reale Owner-/Nutzererfahrung präzisieren und ergänzen diese Requirements;
- Lean/Agile optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value, nicht den Anspruch;
- State of the Art und Best Practice sind Basis wissenschaftlicher und technischer Entscheidungen;
- technische Umsetzung läuft parallel, sobald ein Requirement-/Constraint-Cluster hinreichend klar ist, ersetzt aber nicht die fachliche Arbeit;
- formal geklärte Requirements-, Governance- und Traceability-Regeln werden deterministisch geprüft statt dauerhaft nur Prompt-/Chat-Compliance zu bleiben;
- technische Arbeit bleibt bis zu Goals/Needs/Pains bzw. expliziten Constraints rückführbar; reale Nutzung/Owner-Feedback schließt die Delivery-Schleife;
- externe Pilot-/Prior-Art-Befunde sind Review Input und erhalten erst nach Histo-Orla-eigener Authority-/Lifecycle-Disposition Requirement-, Method- oder Implementation Authority.

Kanonisch:

- `docs/research/discovery/problem-baseline.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`
- `docs/architecture/requirements-derivation.md`
- `docs/architecture/operational-execution-architecture.md`
- `docs/architecture/prior-art-development-inputs.md`
- `docs/architecture/assurance/requirements-assurance-harness.md`
- `docs/architecture/assurance/value-decision-delivery-assurance.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/requirements-coverage.md`
- `docs/research/synthesis/phase-reconciliation.md`

Aktueller Arbeitsfluss:

```text
Goals / Needs / Pains / reale Research-Friktion (#28, #46/#47, Owner Feedback)
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
Decision / Implementation Trace gegen Requirements + G/N/P + Governance (#63)
        ↓
Development & Verification (#59)
        ↓
reale Nutzung / Owner-Feedback (#63)
        ↺
Pain bestätigt | Pain bleibt | Regression | neuer Need | Requirement-/Method-/Decision-Delta
```

## 2. Requirements / Non-Regression

Aktive Systemanforderungen bestehen mindestens aus:

1. 39 accepted Requirements/Constraints in `requirements-baseline.md`;
2. 14 accepted Extensions aus `requirements-extensions.md`;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints;
4. späteren explizit akzeptierten Deltas unter #42.

Neu cross-cutting akzeptiert ist `REQ-TRACE-001`: materielle Systemarbeit bleibt von Goals/Needs/Pains über Requirement, technische Entscheidung, Implementation und Verification bis zu realer Nutzung/Owner-Feedback rückführbar. Feedback ist Product-/Workflow-Evidence, nicht historische/wissenschaftliche Evidenz.

### Innere Requirement-Struktur

Kanonischer Arbeitsvertrag:

`docs/research/synthesis/requirements-structure.md`

Für neue oder materiell geänderte Requirements werden mindestens auseinandergehalten:

```text
Requirement Identity / Role
Motivation / Driver
Origin / Source / Evidence
Domain Authority / Acceptance Authority / Delivery / Verification Authority
Scope / Exclusions
Dependencies / Relations
Criticality
Architecture Significance
Acceptance / Verification
Risks / Forbidden Loss
Status
```

Wichtig:

- `Source` = konkrete Herkunft/Begründung des Requirements;
- `Domain Authority` = Kompetenz, die seine fachliche Bedeutung besitzt;
- `#42` = kanonischer Requirements-Lifecycle-Owner;
- `#48/#59` = technische Ableitung/Umsetzung, nicht fachliche Semantik;
- `Criticality` ≠ `Delivery Priority`;
- Delivery-Reihenfolge wird dynamisch nach Nutzen, Dependencies, Risiko, Reversibilität und aktuellem Research-Pain bestimmt.

Responsibility-/Dependency-Sicht:

`docs/research/synthesis/requirements-responsibility-dependency-map.md`

Keine Big-Bang-Migration: bestehende Requirements werden clusterweise nachgezogen, sobald sie technisch/fachlich aktiv bearbeitet werden.

### Deterministic Requirements Assurance – #62

#62 besitzt die formale Quality-Assurance-Schicht für bereits geklärte Requirements-Regeln.

Bausteine:

- `tools/requirements/requirement-record.schema.json` – JSON Schema Draft 2020-12;
- `tools/requirements/data/records.json` – machine-readable QA-/Traceability-Projektion, keine zweite fachliche Requirement Truth;
- `tools/requirements/validate.py` – deterministischer Cross-Record-/Repo-Validator;
- `tools/requirements/tests/` – positive/negative Regressionstests;
- `.github/workflows/project-assurance.yml` – konsolidierter automatischer Assurance-Check;
- `docs/architecture/assurance/requirements-assurance-harness.md` – Rule-/Scope-Vertrag.

Harte Grenze:

```text
Schema / Validator
= Form, Referenzintegrität, Authority-/Dependency-/Coverage-/Lifecycle-Invarianten

Domain / Fachreview
= Bedeutung, fachliche Richtigkeit, wissenschaftliche Suffizienz
```

Ein Harness-PASS bedeutet nur `formal requirements conformance for the implemented rule set`, niemals wissenschaftliche Validierung.

Aktuelle Realtests 2026-09-03:

- Requirements-/Trace-/Operational-Assurance ist nach der #62-Reconciliation wieder vollständig grün;
- PR #73 / Run `33764679014`: `REQ-WF-001` besitzt nun den von #62 verlangten strukturierten QA-Record für den weiterhin sachlich korrekten Status `partial`;
- PR #72 / Run `33765119632`: D1 Safe Mutation / Progress bestand Requirements-, Assurance- und Operational-Regressionen sowie beide formalen Validatoren;
- PR #74 / Run `33766069328`: Admission-Prep bestand dieselbe vollständige Assurance-Kette;
- `REQ-TRACE-001` bleibt in Coverage und strukturiertem Requirement-Record erfasst.

### Operational Integration – #48/#59

Der gemeinsame Integrationsschnitt ist inkrementell erweitert:

- `tools/operational/enforcement-map.json` projiziert Requirements referenzbasiert auf Enforcement-Klassen, Contracts, Rule-IDs, Capabilities, Fixtures, Status und fachliche Review-Grenzen; sie dupliziert keine Requirement-Semantik;
- `tools/operational/core.py` stellt gemeinsame mechanische Loader-/JSON-Schema-Infrastruktur für die bestehenden #62/#63-Commands bereit;
- `tools/operational/mutation.py` ergänzt den lokalen Pre-write-/Progress-Guard: bounded replacement aus fresh state, destructive mismatch `blocked`, bereits erfüllter Zustand `NO_CHANGE`, expliziter Full-Replacement-Typ und atomarer lokaler Write-Adapter;
- `tools/requirements/validate.py` und `tools/assurance/validate.py` bleiben kompatible Wrapper/Commands; kein Big-Bang-Rewrite;
- `Project Assurance` prüft Map-/Requirements-/Trace-/Operational-Regeln und läuft seit PR #74 auf jedem Pull Request; Push-Pfadfilter bleiben zur Lärmbegrenzung bestehen;
- wissenschaftliche/Methoden-/Owner-Urteile bleiben explizite Review-Grenzen und werden nicht als Validator-PASS determinisiert;
- repo-weite GitHub-Admission ist noch nicht vollständig: direct writes nach `main` bleiben bis zur serverseitigen Required-PR/Protection-Konfiguration außerhalb des lokalen D1-Adapters.

Kanonischer Architektur-/Trade-off-Ort: `docs/architecture/operational-execution-architecture.md`. Implementations-/Verification-Trace liegt in `tools/assurance/data/trace-records.json`; D1 und Admission-Prep sind zusätzlich unter #70/#48/#59 und #44 (`DD-20260903-001`) geroutet.

### Value / Decision / Delivery / Feedback Assurance – #63

#63 schützt die formale Kette:

```text
Goal / Need / Pain / Constraint
→ accepted Requirement
→ Decision bzw. begründete reversible Direktumsetzung
→ Implementation
→ Verification
→ reale Nutzung / Owner-Feedback
→ Delta
```

Bausteine:

- `tools/assurance/trace-record.schema.json`;
- `tools/assurance/governance-registry.json`;
- `tools/assurance/policy.json`;
- `tools/assurance/data/trace-records.json`;
- `tools/assurance/validate.py`;
- `tools/assurance/tests/`;
- `.github/workflows/project-assurance.yml`;
- `docs/architecture/assurance/value-decision-delivery-assurance.md`.

Der Changed-Code-Guard prüft kontrollierte technische Pfade gegen einen **aktuellen** Implementation-Trace. Ein alter `verified` Record schaltet einen Pfad nicht dauerhaft frei. Materielle technische Records müssen auf accepted Requirements, `G/N/P`-Driver und bindende Governance rückführbar sein.

Owner-/Nutzerfeedback wird als eigener Product-/Workflow-Evidence-Typ geführt. Negative Outcomes wie `pain-persists`, `regression`, `new-pain`, `new-need` oder `requirement-change` müssen einen offenen Delta-Pfad erzeugen. `owner-workflow-acceptance` kann nicht durch technische Selbsttests ersetzt werden.

`FB-20260902-003` persistiert das reale Owner-Feedback nach dem Lampe-PDF-Pilot: Der wissenschaftliche State ist zunehmend korrekt, der operative Forschungsarbeitsplatz bleibt aber zu stark manuell/chat-orchestriert und textlastig. Bestehende `REQ-UX-001/002`, `REQ-WF-001`, `REQ-STATE-001`, `REQ-LEAN-001` decken das Ziel bereits; der offene Delta ist primär Delivery-/Architecture-Priorisierung hin zu strukturiertem Research State, automatischem Context/Trace/Derive und daraus erzeugten menschenlesbaren Sichten.

Materielle Scope-/Qualitätsänderungen benötigen weiterhin ein explizites Requirement-/Decision-Delta. Neue Buzzwords, Tools, Frameworks oder Phasenbegriffe ändern keinen akzeptierten Scope implizit.

Delivery-/Verification-Status wird in `docs/development/requirements-coverage.md` geführt.

### Wissensarbeit-Pilot-Rückfluss – #65

`esany/Wissensarbeit` hat Histo-Orla als realen Pilot verwendet und den generischen Pilot am 2026-09-02 geschlossen. Projektspezifische Erkenntnisse wurden korrekt als #65 nach Histo-Orla zurückgegeben: `external pilot review input / candidate / no implementation authority`.

Der generische Pilot hat sechs ausführbare Learnings abgesichert:

- materieller State darf nicht nur im Chat bleiben (`conversation harvesting`);
- generierte/komprimierte Contexts brauchen Fidelity gegen materielle Referenzen und `unresolved`-Zustände;
- Token-/Kontextreduktion ist nur nach `lossless-by-reference` zulässig;
- Co-Creation/Elicitation geht Requirement-/Decision-Promotion voraus;
- ein erfolgreicher Case ändert generische Mechanismen erst nach Generic-Fit;
- Case-Isolation verhindert, dass Pilotsemantik in generische Core-Strukturen ausläuft.

Kanonische technische Einordnung: `docs/architecture/prior-art-development-inputs.md`. #65 selbst bleibt Candidate-Review-Input und wird nur bei realer Relevanz über die zuständigen Histo-Orla-Owner einzeln dispositioniert.

## 3. Baselines und Präzedenz

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed, weiterhin upstream Value-/Problem-Basis
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Questions – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risks/Constraints – completed
- #41 Capability/Quality – completed
- #42 Requirements Baseline + accepted Extensions + Requirements Structure – aktiver Requirements Owner
- #43 historisches Architecture-Readiness-Gate; kein aktuelles Blocking-Gate

Die Baselines bleiben gültig und werden durch reale Research-, Methoden- und Nutzungsbefunde präzisiert.

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

#42 ist einziger Owner akzeptierter Systemanforderungen und ihres Lifecycles.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`

Neue fachlich belastbare Systembedarfe aus #46/#47/#60 sowie belastbare Product-/Workflow-Deltas aus realer Nutzung gehen als Requirement-Deltas dorthin. Fachmethodische Wahrheit selbst bleibt #60-Eigentum; Research-Owner-Feedback besitzt Ziel/Nutzen/Pain, nicht historische Wahrheit.

#62 prüft die formalisierten Requirement-Strukturen deterministisch. #63 prüft formale Value-/Decision-/Delivery-/Feedback-Traceability. Beide besitzen weder Requirement Truth noch Domain Authority.

## 6. Technical Lead #48

#48 besitzt:

- technische SOTA-/Best-Practice-/Existing-Tool-Einordnung;
- technische Priorisierung nach Requirement, Dependency, Risiko, fachlichem Nutzen und Reversibilität;
- reversible technische Entscheidungen und Refactoring;
- Integrations-/Feasibility-Spikes;
- evolutionäre Architektur;
- technische Acceptance-/Regression-/Invariant-Tests;
- Rückgabe fachlicher/Requirements-Fragen an #42/#60.

Kanonischer Ableitungsvertrag:

`docs/architecture/requirements-derivation.md`

Technische Ableitung erfolgt nicht direkt `Requirement → Technologie`, sondern:

```text
Requirement / Cluster
→ upstream Goal/Need/Pain verstehen
→ System Responsibility
→ Architecture Concern / Quality Attribute
→ Technical Research Question
→ Existing Tools / Standards / Patterns
→ Candidate Approach
→ Trade-off / Risk / Reversibility
→ Decision / Implementation Trace (#63)
→ Implementation / Verification
→ reale Nutzung / Feedback
```

Zusätzliche aktuelle Prior-Art-/Operational-Inputs:

- `docs/architecture/operational-execution-architecture.md`;
- `docs/architecture/prior-art-development-inputs.md`;
- `esany/paleo-type` und `esany/Wissensarbeit` werden bei direkt relevanten materiellen Entscheidungen frisch als Prior Art gelesen, niemals als fremde Requirement-/Semantik-Authority.

#48 besitzt nicht historische Findings, Method Truth, Scope-Reduktion akzeptierter Requirements oder das Recht, fachliche Unsicherheit technisch wegzumodellieren.

## 7. Development & Verification #59

#59 implementiert und verifiziert akzeptierte Requirements. Es ist keine eigene Produktphase und kein Scope-Owner.

Delivery Coverage:

`docs/development/requirements-coverage.md`

Status je Requirement:

`not-started | in-progress | implemented | verified | partial | blocked | research-needed | owner-deferred`.

Technische Arbeit beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist; noch offene Fachsemantik bleibt sichtbar und wird nicht von Dev erfunden.

Bei materieller technischer Arbeit gelten #62/#63 als reproduzierbare formale QA-Schichten. `verified` braucht weiterhin zusätzlich die inhaltlich passende Verification Authority/Evidenz; bei `owner-workflow-acceptance` reale bestätigende Owner-/Nutzererfahrung.

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
- #62 – Requirements Assurance Harness / deterministische Requirements-QA
- #63 – Goal/Need/Pain → Requirement → Decision → Delivery → Feedback Assurance Spine

## 9. Source / Storage Responsibility

```text
OneDrive  = Source of Bytes
Zotero    = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht Source-/Instance-Identität.

## 10. Aktuelle nächste Aktionen

### Inhaltlich führend

1. #46/#47 reale Forschung fortführen. Der zweite #46/#61-Pilot hat die bereitgestellte Lampe-PDF-Instanz, den allgemeinen Bandlauf, `EX-U2-0010`–`0013`, eine nutzerverständliche Ableitung und den Zugangsvergleich persistiert. Nächster fachlicher Schritt: Kauf/Verkäufer und Archivkonkordanz von Nr. 420 auflösen, `Grune = Mönchgrün` unabhängig kollationieren und die neuen Comparanda ohne vorzeitige Gesamtstrategie-Synthese prüfen.
2. #60 den ersten SOTA-basierten Domain-Method-Block Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik erarbeiten und an realen NHUB-/Deutschordensfällen testen.
3. danach Archivistik/Provenienz/Registraturkunde und historische Philologie/Semantik.
4. neue Systemanforderungen aus diesen Arbeiten als Requirement-Deltas unter #42 konsolidieren.
5. #65 nicht pauschal promoten: einzelne Candidate-Punkte nur dann durch Domain-/Product-/Requirements-Owner dispositionieren, wenn reale Arbeit sie benötigt.

### Requirements / Struktur / Assurance

6. neue/materiell bearbeitete Requirements nach `requirements-structure.md` führen.
7. zuerst cross-cutting Cluster Source/Provenance, State/Restartability, Method/Research, Audit/Validation und Retrieval strukturieren, sobald #42/#48 sie aktiv benötigt.
8. Dependencies nicht nur als statische Priorität, sondern als `requires/refines/constrains/conflicts` sichtbar machen.
9. Requirement→Enforcement-Map und #62-Harness bei aktiven Requirements inkrementell um Records/Rules/Fixtures erweitern; keine Big-Bang-Migration.
10. #63 für neue materielle technische Arbeit real verwenden: aktueller Decision/Implementation Trace, Requirements + `G/N/P` + Governance, danach Verification/Feedback.
11. jede neue Hard Rule braucht Rule-ID + negativen Regressionstest und darf keine fachliche Wahrheit simulieren.
12. bei generierten/komprimierten Work Contexts künftig Material-/Reference-Coverage und `unresolved`-Fidelity als eigene Assurance-Frage behandeln; Tokenreduktion ist kein Qualitätsziel vor Fidelity.

### Technisch parallel

13. **Reales Owner-Feedback `FB-20260902-003` ist jetzt führender Technical-Delivery-Pain:** #48 priorisiert einen vertikalen Research-Operations-Schnitt aus #50/#55/#61: `structured canonical research state → automated context/intake/trace → deterministic derive → human-readable research workspace/view`. Der Nutzer/Chat darf nicht Workflow Engine für routinehafte State-Pflege bleiben.
14. `esany/Wissensarbeit` für diesen Schnitt frisch als konkrete Prior Art verwenden: vorhandene Building Blocks, Context-/Trace-/Derive-Patterns, Standards, Templates und GitHub-Workflows auf `reuse → configure → integrate → thin custom layer` prüfen, statt die Semantik erneut in Histo-Orla-Prosa zu beschreiben.
15. Weitere Governance-/Architecture-Markdown-Verträge nur ergänzen, wenn sie eine unmittelbar ausführbare Capability, Guard, Datenstruktur oder Derived View freischalten; keine Textschicht als Ersatz für Bedienbarkeit/Automation.
16. #55 Human-readable Audit ist kein späterer UI-Feinschliff mehr: früh gegen reale #46-Daten einen generierten, drill-down-fähigen Research View liefern; keine manuell gepflegte zweite Wahrheit.
17. #61 Work Context/Handoff als ausführbaren Compiler/Resolver aus kanonischem State erproben; Chat soll Kontext nicht jedes Mal manuell zusammensuchen.
18. #50/#51 den realen Research State so strukturieren, dass Source/Instance/Findspot/Excerpt/Finding/Hook/Uncertainty maschinenlesbar und verlustfrei referenzierbar sind, ohne Fachsemantik zu flatten.
19. #53 Exact Search und der kombinierte lokale-PDF→institutionelle-Fundstelle-Pfad an diesen strukturierten State anbinden; #49/#57 dort weiterführen, wo Availability/Restartability den Slice real blockieren.
20. Sobald der vertikale Slice benutzt wird, Owner-Feedback über #63 als `confirms | pain-persists | regression | new-pain | new-need | requirement-change` routen; Erfolg ist erst erreicht, wenn reale Nutzung weniger manuelle Orchestrierung und bessere Menschenlesbarkeit bestätigt.
21. #70 nach D1 nicht mit weiterer Governance-Prosa fortsetzen: als nächsten ausführbaren Schutzslice #61 Current Context / Resume gegen die bereits persistierten Cursor-/Sticky-Prerequisite-Fixtures operationalisieren; GitHub-Admission kann parallel nach Auflösung von `DD-20260903-001` end-to-end verifiziert werden.

## 11. Blocker / Decisions

#44 bleibt Register für echte Blocker und Owner-Entscheidungen.

Aktuell aktiv:

- `DD-20260903-001` – **GitHub Required-PR / Branch-Protection Admission**: D1 schützt den lokalen Operational-Write-Pfad und PR #74 bereitet `Project Assurance` als globalen Required Check vor. `main` ist jedoch weiterhin unprotected, Rulesets sind leer und der aktuell autorisierte GitHub-Connector besitzt keine Ruleset-/Branch-Protection-Schreibfunktion. Empfohlene Auflösung durch Repository-Admin: Required Pull Request für `main` + Required Status Check `Project Assurance`. Danach End-to-End-Negativtest unter #59: direct main write muss abgewiesen werden; normaler PR mit grünem Check bleibt zulässig.

Der Blocker betrifft nur die repo-weite GitHub-Prevention. #46/#47 Live Research, #54 Transition, #57 Evidence Availability/Restartability, #61 Current Context sowie weitere technische/researchseitige Arbeit bleiben parallel ausführbar. `FB-20260902-003` ist weiterhin kein Scope-Konflikt, sondern ein Delivery-/Priorisierungsdelta innerhalb bereits akzeptierter Requirements. #65 bleibt Review Input und ändert weder fachliche Requirement Truth noch Method Truth oder Architektur automatisch.

## 12. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- aktuelle historische und methodische Arbeit;
- vollständige aktive Requirements;
- Motivation/Origin/Authority/Scope/Dependencies eines aktiv bearbeiteten Requirements;
- welche Regeln deterministisch durch #62/#63 geprüft werden und welche Fach-/Owner-Review bleiben;
- von welchem Goal/Need/Pain eine materielle technische Änderung getragen wird;
- welche Decision/Implementation/Verification sie realisiert;
- welche reale Nutzung/Owner-Rückmeldung vorliegt oder noch fehlt;
- dass #65 externer Pilot-Review-Input ohne automatische Promotion ist;
- welche Prior-Art-Learnings bei materiellen technischen Entscheidungen zu challengen sind, einschließlich Context Fidelity, Generic-Fit und Case Isolation;
- primäre Funktion/Authority;
- Method-/Evidence-Status;
- technischen Delivery-/Verification-Status;
- offene Debt/Blocker;
- nächste Aktion und Persistenzort.

> **Fachdomänen führen. Technologie dient.**

> **Needs/Pains/Goals begründen das Warum; Requirements operationalisieren das Was; Technik entscheidet das Wie; reale Nutzung schließt die Schleife.**

> **Schema prüft Form; Validator prüft formale Invarianten; Fach-/Owner-Review prüft Bedeutung und Nutzen.**

> **Criticality ist nicht Delivery-Reihenfolge.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**
