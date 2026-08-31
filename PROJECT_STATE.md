# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1 Gesamtstand; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Sie ersetzt weder Requirements, Research-Artefakte noch Architecture Contracts, sondern verweist auf deren kanonische Orte.

## 1. Aktuelle Phase

Die Discovery-/SOTA-/Requirements-Kette #28–#43 ist abgeschlossen.

Architecture Gate #43:

**`architecture-ready-with-bounded-research-debt`**

Aktuelle Hauptphase:

```text
Requirements
→ Architecture Contracts / Invariants / Assurance
→ reversible Integrations-/Technik-Spikes
→ Thin Vertical Slice
→ Architekturvarianten + Trade-offs
→ ADRs
→ MVP-Schnitt
→ Development / Verification
```

Architecture Execution Owner: **#48**.

Parallel läuft weiterhin reale historische Forschung als eigenständiger Research- und Falsifikationsstrang, insbesondere #46/#47. Seit dem Methodik-Audit vom 31.08.2026 läuft zusätzlich #60 als cross-cutting Research Work Package zur **SOTA-basierten Operationalisierung domänenspezifischer Fachmethoden**. Seit dem Work-Context-/Method-Conformance-Audit läuft außerdem #61 als P0 Architecture/Assurance Work Package zur **strukturellen Absicherung von Work Context, Method Application, Promotion und Handoff**.

## 2. Abgeschlossene Baselines / Gates

- #28 Problem-/Need-/Pain-Baseline – completed
- #29 Workflows U1–U4 – completed
- #30 Research Question Portfolio – completed
- #31–#39 SOTA C1–C9 – completed
- #40 Risk / Constraint / Rights – completed
- #41 Capability Map + Quality Catalogue – completed
- #42 Requirements Baseline v0.1 – completed
- #43 Architecture Readiness – completed
- #27 frühere Execution Control bis Gate – completed

Kanonische Artefakte:

- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/risks-constraints.md`
- `docs/research/synthesis/capability-map.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md`

## 3. Aktive Work Owner

### Laufende historische Forschung / Falsifikation

- **#46** – U2 Knau/Orlagau, `in-research / working-research`
- **#47** – U1 Orlagau Teich-/Feuchtkulturlandschaft, `in-research / working-research`

Diese Cases sind **nicht abgeschlossen**. Sie dürfen neue Requirement-/Architecture-Candidates erzeugen. Sie blockieren die Architektur nicht pauschal, können aber eine architecture-driving Invariante falsifizieren und damit gezieltes Reopening auslösen.

### Cross-cutting Fachmethoden-Operationalisierung

- **#60** – Domain Method Profiles v0.1, `in-research / cross-cutting-method-work-package`

#60 besitzt die bislang fehlende Operationalisierungsschicht zwischen Kompetenz-/Visionsebene (#16/#19/#22) und akzeptierten Systemanforderungen (#42). Ziel sind keine Rollenprompts, sondern **SOTA-belegte, an Live-Quellen testbare Domain Method Profiles** mit Fachbegriffen/Gegenstandsmodellen, Quellen-/Materiallogik, ausführbaren Playbooks, Inferenzregeln, Evidence Appetite/Search Vocabulary, QA/Falsifikation, transdisziplinären Übergaben und AI-/Automation-Grenzen.

Kanonische Methoden-Wissensbasis:

- `docs/research/methods/README.md` – Status-/Ownership-Karte: Vision vs. Methode vs. Work Order vs. Hypothese vs. Requirement vs. Architektur vs. Prompt;
- `docs/research/methods/domain-method-profile-contract.md` – Vertrag für Aufbau, SOTA-Nachweis, Live-Case-Test und Promotion von Domain Method Profiles.

Aktuelle Statusregel:

```text
#16/#19 = Vision / fachliches Zielniveau
#22     = Kompetenzinventar / Routing-Scope
#45     = bindender cross-cutting Research-/Evidence-Rahmen
#60     = domänenspezifische Methoden-Operationalisierung
#46/#47 = historische Live-Fälle + Method Stress/Validation
#42     = accepted Requirements
#48ff   = technische Architektur/Delivery/Assurance
Prompt  = austauschbares Ausführungsartefakt, niemals Method Truth
```

Die aktuelle Requirements Baseline bleibt dabei **unverändert**. #60 operationalisiert insbesondere `REQ-EPI-001`; Requirement-Deltas werden erst nach SOTA- und Live-Case-Nachweis als Candidates an #42 zurückgespielt.

### Work-Context / Method-Conformance / Handoff Assurance

- **#61** – Executable Work-Context, Method-Conformance und Handoff Contract, `active-research / P0 architecture-assurance / cross-cutting`

#61 schließt die zweite Lücke nach #60:

```text
Method Truth
= Was ist fachlich eine zulässige Methode?
Owner #60

Method Conformance
= Wurde diese Methode in diesem Work Context korrekt referenziert,
  angewandt, geprüft und nur durch erlaubte Übergänge promoted?
Owner #61 + #50/#54/#55/#57
```

Leitregel:

> **Exploration darf offen sein. Promotion ist fail-closed gegenüber fehlender Method-/Evidence-/Validation-Grundlage.**

Kanonisches Assurance-Artefakt:

`docs/architecture/assurance/method-conformance-work-context.md`

SOTA-/Best-Practice-Referenzrahmen: schema-as-contract / machine-readable validation, W3C PROV, RO-Crate / Workflow Run RO-Crate, Policy-as-Code als Pattern; keine Tool-/RDF-/OPA-/Workflow-Engine-Pflichtentscheidung.

### #46 – aktuelle Leit-/Makrofrage nach jüngsten Research-Updates

Der U2-Forschungsrahmen wurde am 31.08.2026 materiell geschärft. Aktuelle Leitfrage:

> **Wie verändern sich soziale, kirchliche, dynastische, grundherrliche und administrative Organisation des Orla-Grenzraums zwischen ca. 1200 und 1400, welche älteren Rechte und Netzwerke überleben diese Veränderungen, und wie werden Boden, Wege, Kirchen, Abgaben, Wasser und Menschen in diesen Strukturen verfügbar gemacht oder geschützt?**

Kanonische neue Arbeitsartefakte:

- `docs/research/cases/u2-orlagau-zeitscheiben-herrschaftsnetz.md` – Zeitscheiben, Herrschaftsschichten und Beziehungsnetze;
- `docs/research/cases/u2-transdisziplinaere-rekonstruktionsmatrix.md` – historische Situations-/Problem-Dossiers, Evidence Demand und transdisziplinäre Lebenswelt-Rekonstruktion; **case-derived method extension/candidate**, kein universeller Pflichtstandard;
- `docs/research/cases/u2-quellenerschliessung-sota-best-practice.md` – SOTA/Best Practice für quellenzentrierte Erschließung, `source-local first → scope expansion second`; **working-method candidate**, unter #60 domänenspezifisch zu validieren.

Aktueller methodischer Pilot ist u. a. **Triptis 1212 / `nimia paupertas`**: die explizite Quellenbegründung bleibt vom Ursachenerklärungsraum getrennt; ökonomische, institutionelle, soziale, räumliche, ökologische, politische oder religiöse Ursachen sind nur über eigene Evidenzpfade zu prüfen.

Aktuelle methodische Schärfung:

```text
Quelle / quellennahe Beobachtung
→ research hooks / Evidence Demand
→ begründete Scope-Erweiterung
→ disziplinspezifische Evidenzpfade
→ Cross-Evidence-Abgleich
→ konkurrierende Erklärungen
→ transdisziplinäre Synthese
```

Expertise Routing soll dabei nicht bei Disziplinlabels enden, sondern **Evidence Routing** erzeugen. Die konkrete fachliche Operationalisierung dieses Prinzips wird jedoch nicht mehr aus dem Live Case selbst generalisiert, sondern unter #60 aus den jeweiligen Fachmethoden erarbeitet und getestet.

### Architektur / Integration / technische Spikes

- **#48** – Architecture Execution Control
- **#49** – Zotero ↔ OneDrive ↔ Histo-Orla Integration Spike, read-first
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten + Method-/Work-/Review-Provenienz
- **#51** – Document-/Findspot-Pipeline / Source→Excerpt-Roundtrip
- **#52** – OCR/HTR Processor Contract + research-critical Benchmark Harness
- **#53** – Historical Retrieval Baseline: Exact, Varianten, Query Log, Findspots
- **#54** – Candidate→Review→Promotion + deterministic invariant enforcement, inkl. Method-/Authority-Transition Guards
- **#55** – Human-readable Research Audit View
- **#56** – Rights Admission, Credentials und External-Processing Guards
- **#57** – Provider Removal, Export und Restartability inkl. fresh-context Role/Method/Evidence Resume
- **#58** – Architekturvarianten, Trade-off-/Loss-Matrix, ADRs, MVP Cut
- **#59** – MVP Development & Verification; aktuell durch #58 blockiert
- **#61** – Work-Context / Method-Conformance / Handoff Assurance

Architecture Index:

`docs/architecture/README.md`

Kanonischer Contract #50:

`docs/architecture/contracts/canonical-research-state.md`

Assurance Contract/Research #61:

`docs/architecture/assurance/method-conformance-work-context.md`

## 4. Aktuelle cross-cutting Owner Constraints

### Source / Storage Responsibility

```text
OneDrive
= Source of Bytes / primärer physischer Speicher der Quellen-/Literaturdateien

Zotero
= bibliographische/archivische Verwaltung, Collections, Tags, Notes, Attachment-Referenz

Histo-Orla
= wissenschaftlicher Research State: Evidenz, Findings, Claims, Discrepancies,
  Validation, Provenienz-/Findspot-/Method-Application-Bezug
```

Keine dieser externen Schichten ist alleiniger kanonischer Research-State-Owner.

### Source Identity

Bindendes Forschungsprotokoll:

`docs/research/source-identity-protocol.md`

Grundtrennung:

```text
Source / Überlieferung
→ Representation / Edition / Katalog / Reproduktion
→ konkrete inspizierte Instanz
→ Derivative / OCR / HTR / Transkription
→ Findspot / Excerpt / Observation
→ Finding
→ Claim / Interpretation / Synthesis
```

### Methodische Autorität / kein Prompt als Fachmethode

Bindender gemeinsamer Forschungsrahmen bleibt #45. Domänenspezifische Methodik wird unter #60 operationalisiert. Für consequential Research gilt accepted `REQ-EPI-001`: führende Domäne, domänenspezifische Methode, Evidenzmaßstab und zulässige Schlussart müssen nachvollziehbar sein; ein Rollenprompt ist kein Fachmethodennachweis.

Status- und Ownership-Karte:

`docs/research/methods/README.md`

Leittrennung:

```text
Vision
≠ Work Order
≠ Domain Method Profile
≠ Method Application
≠ Observation/Finding
≠ historische Hypothese
≠ Methodenhypothese
≠ Requirement Candidate
≠ accepted Requirement
≠ Architecture Choice
≠ Prompt / Model Run
```

### Chat / Work Context / Handoff

`AGENTS.md` ist bindender Repo-Vertrag.

Kein continuation-critical State darf ausschließlich in Chat/Modellzustand verbleiben.

**Neu bindend seit Commit `59e74b1`:** §13 verlangt für substanzielle Arbeit zusätzlich zum Repo-Bootstrap eine explizit rekonstruierbare Work-Context-/Authority-/Method-/Handoff-Grenze. Mindestinhalt: primäre Funktion, Work Owner, bounded Scope/Exclusions, leading/controlling Domains, applicable Method/Quality Frame, MAY/MUST NOT, Stop/Handoff, Return Condition und Persistence Target.

Für consequential Research gilt:

- `method-candidate` darf Exploration anleiten;
- reguläre consequential operative Methodik benötigt `working-method` oder höher;
- fehlende Method-/Evidence-/Validation-Grundlage blockiert **Promotion**, nicht offene Exploration;
- gerichtete Hauptübergabe: `Domain Research → Domain Review/Requirements → Architecture/Dev → scholarly adequacy return → Research NEXT ACTION`;
- independent specialist validation bleibt getrennt.

Früherer Governance-Audit:

`docs/governance/work-context-handoff-audit.md`

Seine damalige `owner-admission-pending`-Empfehlung zur Work-Context-Schicht ist durch die aktuelle bindende `AGENTS.md`-Regel superseded. Technische Operationalisierung: #61.

## 5. Aktuelle Blocker / Decisions

**#44 enthält derzeit keinen Gate-blockierenden Owner-/Rights-/External-Validation-Fall.**

Normale offene Forschung, reversible Architekturfragen und technische Experimente sind keine #44-Blocker.

Die Work-Context-Schärfung ist inzwischen owner-admitted und bindend; kein offener Owner-Blocker bleibt daraus.

Die fachmethodische Operationalisierung #60 und Method-Conformance-Assurance #61 sind **keine allgemeinen Architekturblocker**. Sie können jedoch gezielte Requirement-/Acceptance- oder Architektur-Reopenings auslösen, wenn reale Domain Profiles/Thin-Slice-Tests eine bisherige architecture-driving Annahme falsifizieren.

## 6. Aktueller kritischer Architektur-/Delivery-Pfad

```text
#50 Canonical State / Identity / Method-Provenance Contract
        ↓
#49 Zotero/OneDrive Source Resolver
        ↓
#51 Document / Findspot Pipeline
        ├─→ #52 OCR/HTR End-to-End
        └─→ #53 Historical Retrieval End-to-End

#60 Domain Method Profiles ─────┐
                               ├─→ #61 Method Conformance / Work Context
#50 ────────────────────────────┘          │
#50 ─→ #54 Promotion / Invariants ←────────┤
#50 ─→ #55 Audit Contract ←────────────────┤
#50 ─→ #57 Restartability ←────────────────┘
#50 ─→ #56 Rights Admission

belastbare Evidence aus #49–#57/#61
        ↓
#58 Architecture Variants / ADRs / MVP Cut
        ↓
#59 MVP Development / Verification
```

Parallel möglich:

- #49 read-only Zotero/API-Probing;
- #50/#54 synthetische Invariant-/Promotion-Tests;
- #56 Rights-Admission-Contract;
- #52 OCR/HTR Benchmark-Harness auf isoliertem Testmaterial;
- #55 Audit-View-Contract;
- #57 synthetische Export-/Removal-/Resume-Tests;
- Live Research #46/#47;
- Domain Method Profile Research #60;
- #61 SOTA-/Contract-Arbeit und synthetische Work-Context-/Method-Transition-Fixtures.

Zusätzlicher Restartability-Test aus aktuellem `paleo-type`-Prior-Art, für #49/#57/#61 zu prüfen:

```text
Identifiability / Retrievability
≠ Staged in target context
≠ actually inspectable for the target NEXT ACTION
```

Wenn eine NEXT ACTION direkte Quelleninspektion verlangt, muss ein frischer autorisierter Work Context die tatsächlich benötigte Instanz über einen dokumentierten zulässigen Pfad öffnen können; bekannte Source Identity allein genügt nicht.

## 7. Research-Design-Dokument: Status

`docs/research-design/transdisziplinaerer-literaturassistent.md` bleibt ein **foundational design document** mit weiterhin gültigen Governing Principles und fachlichem Zielbild.

Es ist **nicht mehr der alleinige aktuelle Operations-/Requirements-/Architecture-State**, weil seine letzte grundlegende Konsolidierung vor Abschluss von #28–#43 liegt.

Für aktuelle Detailfragen gilt:

```text
Research Design Principles
→ aktuelle Research/SOTA-/Methods-Artefakte
→ #42 Requirements
→ #43 Gate
→ #48ff Architecture Contracts / Spikes / ADRs
```

Siehe `docs/research-design/README.md`.

## 8. Technischer Entwicklungsstand

Bis #43 war technische Implementierung bewusst nachgeordnet; deshalb enthält das Repository bislang wenig Anwendungscode.

Das war **für die abgeschlossene Research-/Requirements-Phase methodisch richtig**. Ab der aktuellen Phase besitzt Delivery nun explizite technische Work Owner #49–#59/#61.

Der aktuelle technische Stand ist überwiegend **Architecture Contract / Spike / Benchmark / Assurance Research**, noch nicht produktiver MVP-Code.

Produktive Implementierung ist bewusst in #59 gebündelt und durch #58 blockiert, bis eine belastbare Architektur-/MVP-Entscheidung vorliegt. Kleine diskriminierende Prototypen, machine-readable Contract-Projektionen, Validatoren und Test-Harnesses sind vorher ausdrücklich zulässig, wenn sie auf accepted Requirements rückführbar sind.

#60 ist **keine technische Systementwicklung**, sondern fachwissenschaftliche Methodenforschung/Operationalisierung mit möglicher downstream Requirements-Wirkung. #61 ist technische/architektonische Assurance-Operationalisierung und darf Method Truth nicht besitzen.

## 9. Nächste ausführbare Aktionen

### Fachmethodik #60

1. Ersten SOTA-Block **Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik** durchführen; konkrete Methodenliteratur/Standards fundstellenfähig dokumentieren.
2. Daraus erstes Domain Method Profile gemäß `domain-method-profile-contract.md` bauen und an NHUB-II-Fällen testen, einschließlich mindestens eines Overclaim-/Counterexample-Falls.
3. Dabei zusätzlich Method Applicability/Routing, Multi-Method Composition, Method Version Drift, mandatory vs. conditional gates und Review-Independence als fachliche Fragen explizit prüfen.
4. Danach **Archivistik / Provenienz / Registraturkunde** sowie **historische Philologie / mittellateinische Semantik / Hermeneutik** operationalisieren.
5. Weitere Profile problemgetrieben aus #46/#47 priorisieren; keine vollständige Methoden-Enzyklopädie vorab.
6. Requirement-Deltas zunächst nur als Candidates führen; #42 bleibt bis zur nachgewiesenen Generalisierbarkeit unverändert.

### Live Research

7. #46 entlang der aktualisierten Makrofrage fortführen: Source-local Erschließung + Zeitscheiben-/Situations-Dossiers + Evidence-Demand-Routing; dabei Case-Methodik als Candidate behandeln, wenn das passende Domain Profile noch nicht `working-method` ist.
8. NHUB-II-/CDS-/Lehnbuch-/Saalfeld-Kollation nach den aktuellen #45-/Source-Identity-Regeln fortsetzen.
9. Triptis 1212 und weitere Situationen nicht aus einem Einzeltext kausal erklären, sondern Hypothesen klar vom direkten Quellenbefund trennen und spätere fachliche Anschlussanalyse unter #60 routen.
10. RC-U2-09…18 nur über Cross-Use-Case-/SOTA-/Requirement-Prüfung weiterpromovieren.

### Method Conformance / Assurance #61

11. Aus dem ersten realen #60-Profile die **kleinste machine-readable Projektion** formal bereits entschiedener Semantik ableiten; keine zweite Method Truth erzeugen.
12. Minimalen Work-Order-/Work-Context-/Method-Application-/Handoff-Vertrag gegen Triptis 1212 + zweiten U2-Fall testen.
13. SOTA-Pattern gegen kleinste Lösung diskriminieren: JSON-Schema-artiger Contract, lokale Transition-/Validatorlogik, W3C-PROV-/RO-Crate-Kompatibilität; OPA/Workflow Engine/RDF nur bei realem Trigger.
14. `fail closed on promotion, not on exploration` mit negativen Fixtures belegen.

### Case-unabhängig / Architecture

15. **#50** aktualisierten Contract prüfen und synthetische Invariant-Tests ableiten.
16. **#54** Promotion-/Method-/Authority-Transition-Regeln gegen mindestens zehn positive/negative Fixtures konkretisieren.
17. **#56** Rights-Admission-/Credential-Contract spezifizieren.
18. **#49** read-only Zotero-/OneDrive-Identifier-/Locator-Mapping empirisch prüfen, sobald Zugang/Fixture verfügbar ist.
19. **#51** Document-/Findspot-Contract synthetisch beginnen; realer Byte-Slice folgt #49.
20. **#52/#53/#55/#57** parallel als Harness/Contract vorbereiten; #55 bis Method Application/Profile/Review auditieren, #57 fresh-context Role/Method/Evidence Resume testen.

### Nach belastbaren Spikes / Falsifikation

21. U1/U2/U4 als Falsifikation für Source/Instance/Findspot/OCR/Retrieval/Audit verwenden.
22. #60-Methodenprofile ebenfalls als wissenschaftliche Acceptance-/Failure-Quelle für bestehende Architekturannahmen nutzen, ohne Methodenentscheidungen technisch zu usurpieren.
23. #61-Method-Conformance- und Handoff-Fixtures als Assurance-Gate in den Thin Slice aufnehmen.
24. **#58** 2–3 Architekturvarianten vergleichen und ADR/MVP Cut ableiten.
25. **#59** produktiven Thin Slice implementieren und wissenschaftlich + technisch verifizieren.

## 10. Handoff-Test

Ein neuer Chat/Bearbeiter soll nach Lesen von:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. zuständigem Work-Owner-Issue + dessen Artefakt

ohne vorherige Chat-Historie produktiv fortsetzen können.

Seit der bindenden Work-Context-Schärfung reicht reine Dokumentauffindbarkeit nicht: Der neue Bearbeiter muss zusätzlich primäre Funktion/Authority, bounded Scope, applicable Method/Quality Frame, Evidence Availability, nächste erlaubte Aktion und Handoff-/Return-Bedingung korrekt rekonstruieren können.

Wenn dies nach einer materiellen Änderung nicht mehr stimmt, muss dieser State vor Abschluss der Arbeit nachgezogen werden.

Materialer `PROJECT_STATE`-Update-Trigger sind insbesondere Änderungen an:

- aktiver Leit-/Makrofrage oder Work-Owner-Scope;
- Phase/Gate;
- kritischer Dependency/Blocker;
- nächstem ausführbaren Hauptschritt;
- cross-cutting Owner Constraint;
- Requirement-/Architecture-/Decision-Status.

Einzelne Findings gehören weiterhin in ihre kanonischen Work-Owner-Artefakte und nicht in diesen Handoff-Snapshot.