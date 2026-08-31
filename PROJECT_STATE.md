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
→ Architecture Contracts / Invariants
→ reversible Integrations-/Technik-Spikes
→ Thin Vertical Slice
→ Architekturvarianten + Trade-offs
→ ADRs
→ MVP-Schnitt
→ Development / Verification
```

Architecture Execution Owner: **#48**.

Parallel läuft weiterhin reale historische Forschung als eigenständiger Research- und Falsifikationsstrang, insbesondere #46/#47. Seit dem Methodik-Audit vom 31.08.2026 läuft zusätzlich #60 als cross-cutting Research Work Package zur **SOTA-basierten Operationalisierung domänenspezifischer Fachmethoden**.

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
#48ff   = technische Architektur/Delivery
Prompt  = austauschbares Ausführungsartefakt, niemals Method Truth
```

Die aktuelle Requirements Baseline bleibt dabei **unverändert**. #60 operationalisiert insbesondere `REQ-EPI-001`; Requirement-Deltas werden erst nach SOTA- und Live-Case-Nachweis als Candidates an #42 zurückgespielt.

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
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten
- **#51** – Document-/Findspot-Pipeline / Source→Excerpt-Roundtrip
- **#52** – OCR/HTR Processor Contract + research-critical Benchmark Harness
- **#53** – Historical Retrieval Baseline: Exact, Varianten, Query Log, Findspots
- **#54** – Candidate→Review→Promotion + deterministic invariant enforcement
- **#55** – Human-readable Research Audit View
- **#56** – Rights Admission, Credentials und External-Processing Guards
- **#57** – Provider Removal, Export und Restartability
- **#58** – Architekturvarianten, Trade-off-/Loss-Matrix, ADRs, MVP Cut
- **#59** – MVP Development & Verification; aktuell durch #58 blockiert

Architecture Index:

`docs/architecture/README.md`

Kanonischer Contract #50:

`docs/architecture/contracts/canonical-research-state.md`

## 4. Aktuelle cross-cutting Owner Constraints

### Source / Storage Responsibility

```text
OneDrive
= Source of Bytes / primärer physischer Speicher der Quellen-/Literaturdateien

Zotero
= bibliographische/archivische Verwaltung, Collections, Tags, Notes, Attachment-Referenz

Histo-Orla
= wissenschaftlicher Research State: Evidenz, Findings, Claims, Discrepancies,
  Validation, Provenienz-/Findspot-Bezug
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

Bindender gemeinsamer Forschungsrahmen bleibt #45. Domänenspezifische Methodik wird unter #60 operationalisiert. Für consequential Research gilt bereits accepted `REQ-EPI-001`: führende Domäne, domänenspezifische Methode, Evidenzmaßstab und zulässige Schlussart müssen nachvollziehbar sein; ein Rollenprompt ist kein Fachmethodennachweis.

Status- und Ownership-Karte:

`docs/research/methods/README.md`

Leittrennung:

```text
Vision
≠ Work Order
≠ Observation/Finding
≠ historische Hypothese
≠ Methodenhypothese
≠ Requirement Candidate
≠ accepted Requirement
≠ Architecture Choice
≠ Prompt
```

### Chat / Handoff

`AGENTS.md` ist bindender Repo-Vertrag.

Kein continuation-critical State darf ausschließlich in Chat/Modellzustand verbleiben.

Aktueller Governance-Audit:

`docs/governance/work-context-handoff-audit.md`

Befund: Der Anti-Wissensmonopol-/Repo-Bootstrap ist stark. Noch nicht bindend operationalisiert ist jedoch eine generische **Work-Context-/Authority-Schicht** für alle substantielle Chats (primäre Funktion, bounded Scope, MAY/MUST NOT, Stop/Handoff, Return Condition). Eine entsprechende `AGENTS.md`-Schärfung ist derzeit **Empfehlung, nicht bereits bindende Regel**; sie benötigt Owner-Admit, bevor sie als materielle Governanceänderung promoted wird.

## 5. Aktuelle Blocker / Decisions

**#44 enthält derzeit keinen Gate-blockierenden Owner-/Rights-/External-Validation-Fall.**

Normale offene Forschung, reversible Architekturfragen und technische Experimente sind keine #44-Blocker.

Die im Governance-Audit empfohlene Work-Context-Schärfung blockiert laufende Research-/Architecture-Arbeit nicht. Sie wird deshalb nicht als Blocker behandelt; eine bindende Promotion in `AGENTS.md` erfolgt nur nach explizitem Owner-Admit.

Die fachmethodische Operationalisierung #60 ist ebenfalls **kein allgemeiner Architekturblocker**. Sie kann jedoch gezielte Requirement-/Acceptance- oder Architektur-Reopenings auslösen, wenn reale Domain Profiles eine bisherige architecture-driving Annahme falsifizieren.

## 6. Aktueller kritischer Architektur-/Delivery-Pfad

```text
#50 Canonical State / Identity Contract
        ↓
#49 Zotero/OneDrive Source Resolver
        ↓
#51 Document / Findspot Pipeline
        ├─→ #52 OCR/HTR End-to-End
        └─→ #53 Historical Retrieval End-to-End

#50 ─→ #54 Promotion / Invariants
#50 ─→ #56 Rights Admission
#50 ─→ #55 Audit Contract
#50 ─→ #57 synthetic Provider-Removal / Export

belastbare Evidence aus #49–#57
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
- #57 synthetische Export-/Removal-Tests;
- Live Research #46/#47;
- Domain Method Profile Research #60.

Zusätzlicher Restartability-Test aus aktuellem `paleo-type`-Prior-Art, für #49/#57 zu prüfen:

```text
Identifiability
≠ Reproducibility
≠ Research-ready Availability
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

Das war **für die abgeschlossene Research-/Requirements-Phase methodisch richtig**. Ab der aktuellen Phase besitzt Delivery nun explizite technische Work Owner #49–#59.

Der aktuelle technische Stand ist überwiegend **Architecture Contract / Spike / Benchmark**, noch nicht produktiver MVP-Code.

Produktive Implementierung ist bewusst in #59 gebündelt und durch #58 blockiert, bis eine belastbare Architektur-/MVP-Entscheidung vorliegt. Kleine diskriminierende Prototypen und Test-Harnesses sind vorher ausdrücklich zulässig.

#60 ist **keine technische Systementwicklung**, sondern fachwissenschaftliche Methodenforschung/Operationalisierung mit möglicher downstream Requirements-Wirkung.

## 9. Nächste ausführbare Aktionen

### Fachmethodik #60

1. Ersten SOTA-Block **Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik** durchführen; konkrete Methodenliteratur/Standards fundstellenfähig dokumentieren.
2. Daraus erstes Domain Method Profile gemäß `domain-method-profile-contract.md` bauen und an NHUB-II-Fällen testen, einschließlich mindestens eines Overclaim-/Counterexample-Falls.
3. Danach **Archivistik / Provenienz / Registraturkunde** sowie **historische Philologie / mittellateinische Semantik / Hermeneutik** operationalisieren.
4. Weitere Profile problemgetrieben aus #46/#47 priorisieren; keine vollständige Methoden-Enzyklopädie vorab.
5. Requirement-Deltas zunächst nur als Candidates führen; #42 bleibt bis zur nachgewiesenen Generalisierbarkeit unverändert.

### Live Research

6. #46 entlang der aktualisierten Makrofrage fortführen: Source-local Erschließung + Zeitscheiben-/Situations-Dossiers + Evidence-Demand-Routing; dabei Case-Methodik als Candidate behandeln, wenn das passende Domain Profile noch nicht validiert ist.
7. NHUB-II-/CDS-/Lehnbuch-/Saalfeld-Kollation nach den aktuellen #45-/Source-Identity-Regeln fortsetzen.
8. Triptis 1212 und weitere Situationen nicht aus einem Einzeltext kausal erklären, sondern Hypothesen klar vom direkten Quellenbefund trennen und spätere fachliche Anschlussanalyse unter #60 routen.
9. RC-U2-09…18 nur über Cross-Use-Case-/SOTA-/Requirement-Prüfung weiterpromovieren.

### Case-unabhängig / Architecture

10. **#50** Contract fertig prüfen und synthetische Invariant-Tests ableiten.
11. **#54** Promotion-/Invariant-Regeln gegen synthetische Fixtures konkretisieren.
12. **#56** Rights-Admission-/Credential-Contract spezifizieren.
13. **#49** read-only Zotero-/OneDrive-Identifier-/Locator-Mapping empirisch prüfen, sobald Zugang/Fixture verfügbar ist.
14. **#51** Document-/Findspot-Contract synthetisch beginnen; realer Byte-Slice folgt #49.
15. **#52/#53/#55/#57** parallel als Harness/Contract vorbereiten, soweit ihre Abhängigkeiten erfüllt sind.
16. Fresh-context Source-Availability in #49/#57 gegen reale OneDrive-/Zotero-Pfade testen.

### Nach belastbaren Spikes / Falsifikation

17. U1/U2/U4 als Falsifikation für Source/Instance/Findspot/OCR/Retrieval/Audit verwenden.
18. #60-Methodenprofile ebenfalls als wissenschaftliche Acceptance-/Failure-Quelle für bestehende Architekturannahmen nutzen, ohne Methodenentscheidungen technisch zu usurpieren.
19. **#58** 2–3 Architekturvarianten vergleichen und ADR/MVP Cut ableiten.
20. **#59** produktiven Thin Slice implementieren und wissenschaftlich + technisch verifizieren.

## 10. Handoff-Test

Ein neuer Chat/Bearbeiter soll nach Lesen von:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. zuständigem Work-Owner-Issue + dessen Artefakt

ohne vorherige Chat-Historie produktiv fortsetzen können.

Wenn dies nach einer materiellen Änderung nicht mehr stimmt, muss dieser State vor Abschluss der Arbeit nachgezogen werden.

Materialer `PROJECT_STATE`-Update-Trigger sind insbesondere Änderungen an:

- aktiver Leit-/Makrofrage oder Work-Owner-Scope;
- Phase/Gate;
- kritischer Dependency/Blocker;
- nächstem ausführbaren Hauptschritt;
- cross-cutting Owner Constraint;
- Requirement-/Architecture-/Decision-Status.

Einzelne Findings gehören weiterhin in ihre kanonischen Work-Owner-Artefakte und nicht in diesen Handoff-Snapshot.