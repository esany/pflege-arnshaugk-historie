# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1 Gesamtstand; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Sie ersetzt weder Requirements, Research-Artefakte noch Architecture-/Method-Artefakte, sondern verweist auf deren kanonische Orte.

## 1. Aktuelle Phase

Der erste Durchlauf #28–#43 hat eine **v0.1 Discovery-/SOTA-/Requirements-Baseline** und ein damaliges Architecture-Readiness-Gate erzeugt.

Der vertiefte Live Case #46 und die daraus sichtbar gewordene fehlende fachwissenschaftliche Methodenschicht (#60) haben die frühere Readiness-Annahme materiell challenged. Deshalb sind **#42 und #43 seit 31.08.2026 reopened**.

Aktuelle Gate-Position:

**`architecture decision not admitted / technical discovery allowed`**

Kanonische Reconciliation:

`docs/research/synthesis/phase-reconciliation.md`

Aktueller Arbeitsfluss:

```text
Live Research / Problem Discovery (#46/#47)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↓
Problem-/Capability-/Requirement Reconciliation (#42)
        ↕
Technical Discovery / Engineering Advisory (#48)
        ↓
Architecture Readiness Re-Gate (#43)
        ↓ nur bei PASS
Architecture Variants / ADR / MVP Cut (#58)
        ↓
Development / Verification (#59)
```

**Softwaretechnologischer Stand:** Greenfield. Es gibt noch keinen produktiven Anwendungscode, keinen gewählten Runtime-/UI-/Backend-Stack, keine entschiedene Persistenz-/Search-/OCR-/Workflow-Technologie und keine validierte Zielarchitektur.

## 2. Baselines: Status und Präzedenz

### Historischer erster Durchlauf

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Question Portfolio – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risk / Constraint / Rights – completed
- #41 Capability Map + Quality Catalogue – completed
- #42 Requirements Baseline v0.1 – **reopened für Coverage-/Acceptance-Reconciliation**
- #43 Architecture Readiness – **reopened / Re-Gate erforderlich**
- #27 frühere Execution Control – historisch completed

Wichtig: #28/#29 bleiben nützliche Baselines, sind aber nicht mit vollständiger empirischer Product-/Workflow-Discovery gleichzusetzen. Reale Toolfriktionen, Arbeitsabläufe und fachliche Methoden werden durch #46/#47/#60 weiter konkretisiert.

Kanonische Synthese-Artefakte:

- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/risks-constraints.md`
- `docs/research/synthesis/capability-map.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md` – historischer Gate-Report
- `docs/research/synthesis/phase-reconciliation.md` – aktueller Phasen-/Re-Gate-Stand

## 3. Aktive Work Owner

### Historische Live-Forschung

- **#46** – U2 Knau/Orlagau, `in-research / working-research`
- **#47** – U1 Orlagau Teich-/Feuchtkulturlandschaft, `in-research / working-research`

Aktuelle #46-Makrofrage:

> **Wie verändern sich soziale, kirchliche, dynastische, grundherrliche und administrative Organisation des Orla-Grenzraums zwischen ca. 1200 und 1400, welche älteren Rechte und Netzwerke überleben diese Veränderungen, und wie werden Boden, Wege, Kirchen, Abgaben, Wasser und Menschen in diesen Strukturen verfügbar gemacht oder geschützt?**

Wichtige aktuelle #46-Artefakte:

- `docs/research/cases/u2-orlagau-zeitscheiben-herrschaftsnetz.md`
- `docs/research/cases/u2-transdisziplinaere-rekonstruktionsmatrix.md` – case-derived method candidate
- `docs/research/cases/u2-quellenerschliessung-sota-best-practice.md` – working-method candidate

### Fachwissenschaftliche Methodik

- **#60** – Domain Method Profiles v0.1, `in-research / cross-cutting-method-work-package`

Kanonisch:

- `docs/research/methods/README.md`
- `docs/research/methods/domain-method-profile-contract.md`

#60 besitzt **Method Truth**: Wie eine konkrete Fachdisziplin an konkreten Problem-/Quellentypen nach ihrem SOTA arbeitet. Ein Profil muss SOTA, Quellenlogik, Playbook, Inferenzvertrag, Evidence Appetite, QA/Falsifikation, Interfaces und AI-/Automation-Grenzen nachweisen und an realen Fällen getestet werden.

Erste Priorität: Diplomatik/Urkundenlehre + Editionswissenschaft; danach Archivistik/Provenienz/Registraturkunde und historische Philologie/mittellateinische Semantik/Hermeneutik.

### Requirements

- **#42** – einziger Owner akzeptierter Requirements; `reconciliation-active`.

Die Baseline v0.1 bleibt als akzeptierter **Subset** gültig, soweit neue Evidenz sie nicht gezielt widerlegt. Neue Findings aus #46/#47/#60 werden zunächst Requirement Candidates und erst nach SOTA-/Generalisierbarkeits-/Risk-Prüfung promoted.

### Technical Discovery / Engineering Advisory

- **#48** – `active / technical-discovery / engineering-advisory / architecture-decision-paused`

#48 ist der führende technische Owner **vor** dem Re-Gate. Er besitzt technische SOTA-/Best-Practice-Recherche, Feasibility, Integrationen, Migrations-/Lock-in-Risiken, technische Unknowns/Priorisierung und kleine reversible diskriminierende Spikes.

#48 besitzt **nicht** Fachsemantik, accepted Requirements oder Zielarchitektur.

Technical Intake:

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

### Aktive technische Research-/Feasibility-Pakete

- **#49** – Zotero ↔ OneDrive Integration, read-first feasibility
- **#50** – Canonical Research State / Source Identity; nur bereits accepted cross-cutting Invarianten als Contract-Hypothesen weiterprüfen
- **#51** – Document-/Findspot-Pipeline, bounded contract/spike
- **#52** – OCR/HTR Benchmark-Harness nur mit konkretem Corpus/Frage
- **#53** – Historical Retrieval Baseline / Benchmark
- **#54** – Promotion/Invariant Enforcement als technical feasibility
- **#55** – Audit View Research/Prototype
- **#56** – Rights Admission / Credentials
- **#57** – Provider Removal / Export / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff **als Technical/Assurance Research Hypothesis**, keine eingefrorene Workflowarchitektur

### HOLD / BLOCKED

- **#58** – Architecture Decision Package: HOLD bis #42 Reconciliation + #43 Re-Gate PASS + #48 Evidence
- **#59** – MVP Development: BLOCKED bis #42 + #43 + #58

Der bisherige Thin-Slice-Vorschlag bleibt eine **Architecture/MVP Hypothesis**, kein bereits beschlossener MVP-Scope.

## 4. Cross-cutting Constraints

### Source / Storage Responsibility

```text
OneDrive
= Source of Bytes / physischer Primärspeicher der Quellen-/Literaturdateien

Zotero
= bibliographische/archivische Verwaltung, Collections, Tags, Notes,
  Attachment-Referenzen

Histo-Orla
= wissenschaftlicher Research State
```

Keines dieser externen Systeme besitzt allein die wissenschaftliche Source-/Instance-/Finding-Truth.

### Source Identity

Bindend: `docs/research/source-identity-protocol.md` unter #45.

```text
Source / Überlieferung
→ Representation / Edition / Katalog / Reproduktion
→ konkrete inspizierte Instanz
→ Derivative / OCR / HTR / Transkription
→ Findspot / Excerpt / Observation
→ Finding
→ Claim / Interpretation / Synthesis
```

### Method / Work Context / Handoff

Bindend: `AGENTS.md` §13.

- Chat/Prompt/Modellwissen ist keine Method Truth.
- `method-candidate` darf Exploration anleiten; consequential operative Methodik benötigt `working-method` oder höher.
- Exploration bleibt offen; Promotion ist fail-closed gegenüber fehlender Method-/Evidence-/Validation-Grundlage.
- Dev darf fehlende Fachsemantik nicht aus technischer Convenience ergänzen.
- unabhängige Fachvalidierung bleibt eigener Review-Typ.

## 5. Aktuelle Blocker / Decisions

#44 bleibt das Register für echte Owner-/Rights-/Lock-in-/External-Validation-Entscheidungen. Aktuell liegt **kein solcher #44-Blocker** vor.

Die aktuelle Rückstufung der Architekturfreigabe ist kein normativer Owner-Blocker, sondern ein methodisch begründetes Re-Gate nach neuer Evidenz.

## 6. Was jetzt parallel sinnvoll ist

### Domain / Research

1. #46/#47 reale Forschung fortsetzen und Problem-/Workflow-Friktionen explizit persistieren.
2. #60 erstes belastbares Diplomatik-/Editionswissenschaft-Profil SOTA-basiert erarbeiten und an realen NHUB-Fällen testen.
3. daraus Method-/Capability-/Requirement Candidates sauber trennen.
4. #42 fortlaufend nur ausreichend generalisierte Candidates dispositionieren.

### Technical Discovery

1. #48 technische SOTA-/Best-Practice- und Existing-Tool-Landschaft **problembezogen** untersuchen.
2. #49 Zotero/OneDrive read-only Feasibility prüfen.
3. technische Invarianten/Spikes nur dort durchführen, wo accepted Requirements oder konkrete Research-Friktion die Frage tragen.
4. Ergebnisse als `feasibility finding | architecture hypothesis | requirement candidate` zurückgeben.

### Noch nicht

- keine Zielarchitektur;
- keine produktive Stack-/Frameworkwahl;
- kein MVP-Cut;
- keine systemweite KG/RAG/Multi-Agent/Workflow-/Policy-Plattform;
- keine produktive Implementierung #59.

## 7. Re-Gate #43

Architecture Readiness kann erneut PASS erhalten, wenn mindestens:

1. die für den ersten realen Slice benötigten Domain Methods ausreichend operationalisiert oder nachweislich nicht architecture-driving sind;
2. #42 relevante Candidates/Acceptance-Deltas dispositioniert hat;
3. MVP-relevante Problem-/Workflow-Lücken geklärt oder bounded sind;
4. #48 technische SOTA-/Feasibility-Evidence mit existierenden Tools und echten Greenfield-Alternativen geliefert hat;
5. erst danach reale Architekturfragen/Varianten vergleichbar sind.

## 8. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- aktuelle Phase und Gate-Status;
- primäre Arbeitsfunktion / Authority;
- Scope / Exclusions;
- Method-/Quality-Frame;
- verfügbare Evidenz;
- erlaubte nächste Aktion;
- Stop/Handoff/Return Condition;
- kanonischen Persistenzort.

Leitregel:

> **Fachliche und produktbezogene Ungewissheit wird nicht durch Architekturfortschritt kompensiert. Dev exploriert früh, entscheidet aber spät.**

> **Greenfield bedeutet technische Freiheit – nicht Freiheit, fachliche Semantik zu erfinden.**