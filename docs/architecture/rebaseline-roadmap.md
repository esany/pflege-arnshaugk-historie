# Histo-Orla – Architecture / Product Re-Baseline Roadmap

**Status:** `review-candidate / architecture reconciliation / no requirement-or-method authority`  
**Work Owner:** #92  
**Technical / Architecture Authority:** #48  
**Requirements Authority:** #42  
**Domain Method Truth:** #60  
**Development / Verification:** #59  
**Baseline inspected:** `main@df38958cd30cf82c86da05fa9fab1485bd667f20`  
**Stand:** 2026-09-10

## 1. Zweck

Histo-Orla besitzt bereits belastbare Requirements, fachliche Research-/Method-Grenzen, einen Canonical-Research-State-Contract, technische Integrationsspikes und erste ausführbare Assurance-/Operational-Core-Bausteine. Das Problem ist deshalb **nicht fehlende Substanz**, sondern die inzwischen schwer lesbare Gesamtgestalt eines historisch gewachsenen Projekts.

Dieses Dokument reconciliiert den aktuellen Stand zu einer **verständlichen, dependency-getriebenen Produkt- und Ausführungsarchitektur**, ohne die vorhandenen Authorities umzuschreiben oder eine neue Meta-Plattform einzuführen.

Zielzustand ist ein praktisch nutzbarer historischer Forschungsarbeitsplatz, bei dem:

- historisches Verstehen, Quellenarbeit und wissenschaftlich belastbarer Research State das eigentliche Ergebnis tragen;
- Fachdomänen, Methoden und Evidenzgrenzen sichtbar bleiben;
- dauerhafte Produktfähigkeiten reale Forschungsarbeit abnehmen;
- Zotero, OneDrive, PDF-/Document-Processing, OCR/HTR, Retrieval und weitere Werkzeuge sinnvoll integriert werden;
- Operational Tooling Projektbetrieb, Assurance, Trace, Context und Derivation unterstützt, aber nicht zum Produkt oder zweiten Truth Store wird;
- Piloten, Testfixtures und historische Review-Artefakte nicht unbemerkt zu Dauerarchitektur werden;
- ein neuer Bearbeiter den Stand ohne alten Chat rekonstruieren kann.

Dieses Dokument ist eine **Architecture-/Roadmap-Sicht**, keine neue Requirement-, Method-, Historical- oder Selection-Authority.

---

## 2. Authority- und Non-Regression-Grenze

Die Re-Baseline ordnet vorhandene Arbeit; sie ersetzt keine bestehenden Owner.

| Gegenstand | Kanonische Authority / Owner | Re-Baseline darf |
|---|---|---|
| akzeptierte Systemanforderungen | #42 | referenzieren, Coverage-/Architecture-Implikationen sichtbar machen |
| fachwissenschaftliche Method Truth | #60 | referenzieren, benötigte Interfaces/Constraints sichtbar machen |
| technische Mittelwahl / Architektur | #48 | Optionen, Dependencies und reversible Strukturkandidaten reconciliieren |
| Implementierung / Verification | #59 | Delivery-Reihenfolge und Acceptance-Zusammenhang strukturieren |
| Governance / Ownership | #9 / #23 | vorhandene Regeln anwenden; echte Deltas zurückrouten |
| historische Findings / Live Research | #46 / #47 bzw. jeweiliger Research Owner | nur als reale Falsifikations-/Nutzungsevidenz verwenden |
| Owner-/Workflow-Akzeptanz | Research Owner / #63 Feedback-Pfad | als Product-/Workflow-Evidence berücksichtigen |
| Selection / current work choice | explizite Research-/Product-Owner-Auswahl | **nicht** aus Roadmap, PR, Resumability oder CI ableiten |

Materiale Deltas werden daher nicht in diesem Dokument „mit erledigt“:

```text
Requirement-Delta  -> #42
Method-Delta       -> #60
Governance-Delta   -> #9/#23
materiale technische Entscheidung -> #48, ggf. #58/#44
historisches Finding -> zuständiger Research Owner
Selection           -> explizite Owner-Autorisierung
```

---

## 3. Prior Art: Challenge, nicht Bauplan

### `esany/Wissensarbeit`

Für Histo-Orla relevant sind insbesondere:

- klare Trennung von `project`, `domain`, `system`, `tools`, `tests` als **Verantwortungsarten**;
- Human-in-the-loop statt Human-as-workflow-engine;
- systemische Integration neuer Aspekte (`fuse | refine | reframe | supersede | conflict | reject | defer`) statt Append-only-Wachstum;
- Candidates vor Promotion;
- deterministische Regeln in Code/Tests/CI, fachliches Urteil sichtbar als Urteil;
- Architecture Fitness: `avoid -> reuse -> configure -> integrate -> thin custom layer -> build custom`;
- Produktcode entsteht nur, wenn ein konkretes Projekt ihn benötigt.

Nicht übernommen wird die Annahme, Histo-Orla müsse deshalb mechanisch dieselbe Ordnerstruktur besitzen. Insbesondere ist `src/` **keine generische Pflicht**.

### `esany/paleo-type`

Für Histo-Orla relevant sind insbesondere:

- Evidence before plausibility;
- Quellen-/Forschungsverständnis als Produkt, Technik subsidiär;
- Original/Instanz/Derivat/Interpretation sauber trennen;
- Human Auditability Ergebnis -> Evidenz;
- provider-/modellunabhängiger, restartbarer Zustand;
- settled invariants ausführbar machen;
- material research-system changes nicht als technische Nebenwirkung einführen.

Auch hier gilt: Prior Art challengt eine Entscheidung; Histo-Orla Requirements, Method Truth, reale Research-Pains und Owner-Akzeptanz entscheiden.

---

## 4. Semantische Re-Baseline: sechs Kategorien

Die Architektur wird zunächst **semantisch**, nicht über Verzeichnisse geordnet.

### A. `governing/project`

Warum, was, Priorität, Authority, Quality, Constraints, Decisions und projektweiter Zustand.

Typische Inhalte:

- Goals / Needs / Pains;
- accepted Requirements;
- Governance / Authority;
- Delivery-/Verification-Trace;
- echte Decisions / ADRs;
- Current-State-/Handoff-Sicht.

### B. `domain/research`

Fachliche Bedeutung, wissenschaftliche Methodik, Evidence-/Source-Semantik und konkrete Research-Arbeit.

Typische Inhalte:

- Domain Method Profiles;
- Source-/Instance-/Findspot-/Finding-Semantik;
- Research Cases / Findings / Hypothesen / Unsicherheit;
- fachliche Validation / Falsifikation;
- transdisziplinäre Schnittstellen.

### C. `product capability`

Dauerhafte ausführbare Fähigkeiten, die der Research Owner im Forschungsalltag **benutzt** und die Forschungsarbeit konkret abnehmen oder sicherer machen.

Beispiele:

- bibliographische/source-seitige Auflösung aus Zotero;
- Zugriff auf Source Bytes via OneDrive/lokale Quelle;
- Document Inspection und Findspot Round-trip;
- OCR/HTR Processing;
- Exact/Historical Retrieval;
- Research-State Navigation;
- kontrollierte Candidate-/Promotion-Funktionen;
- human-readable Research Views.

### D. `operational support`

Werkzeuge zum Betreiben, Prüfen, Ableiten und Wiederaufnehmen des Projekts. Sie unterstützen Produktentwicklung und Research, sind aber nicht automatisch die Forschungsassistenz selbst.

Beispiele:

- Requirements-/Trace-Validatoren;
- Enforcement Map;
- Repo-/CI-Assurance;
- Context-/Handoff-Generator;
- Migration-/Audit-Helper;
- deterministische Derived-View-Generatoren.

### E. `pilot/testfixture`

Bewusst begrenzte Experimente, Gold Cases, Benchmarks oder falsifikatorische Slices ohne automatische Dauerhaftigkeit.

### F. `superseded/archive`

Historisch wertvolle, aber nicht mehr aktive Zustände; dürfen als Provenienz bleiben, sollen den aktuellen mentalen Modellraum jedoch nicht dominieren.

**Wichtig:** Diese Kategorien sind keine neue Lifecycle-/Authority-Taxonomie. Sie sind eine Architekturlese- und Dispositionssicht.

---

## 5. Aktuelle Work-Owner-/Artefakt-Disposition

Die folgende Tabelle **ändert keine Issue-Ownership**. Sie beantwortet nur: Welche Rolle spielt dieser Strang im heutigen Zielbild?

| Work / Artefakt | Re-Baseline-Kategorie | Dauerhafte Rolle | Roadmap-Disposition |
|---|---|---|---|
| #42 Requirements | governing/project | bindende Systempflichten | **keep canonical**; nicht in Architekturprosa duplizieren |
| #48 Technical Lead | governing/project + architecture coordination | technische Mittelwahl/Dependencies | **keep**; #92 bleibt bounded Reconciliation unter #48 |
| #49 Zotero ↔ OneDrive | product capability candidate + integration spike | Bibliographie-/Source-/Byte-Resolution | **continue**; Spike-Erkenntnisse erst bei dauerhafter Runtime-Funktion in Product Code überführen |
| #50 Canonical Research State | domain/research ↔ product contract boundary | stabile Source-/Instance-/Derivative-/Finding-Grundsemantik | **keep core contract**; keine Provider- oder Persistenzwahl hineinziehen |
| #51 Document / Findspot | product capability | inspeziertes Dokument ↔ belastbare Fundstelle | **continue**; realer Byte-Slice nach #49 |
| #52 OCR/HTR | product capability + benchmark/testfixture | Processing hinter Processor Contract | **continue when representative need/material**; Engine nur nach Benchmark |
| #53 Historical Retrieval | product capability | Exact/Variants/Query Log/Findspot Retrieval | **continue**; realer E2E-Pfad nach #51 |
| #54 Candidate/Promotion | product-state safety + operational guard | kontrollierte Mutation/Promotion | **continue** als `transition`-Capability; kein eigener Workflow-Stack |
| #55 Human-readable Audit | product view + derived support | Research-Navigation/Audit | **continue** als generierte Sicht; keine zweite Truth |
| #56 Rights/Processing | cross-cutting product/operational guard | Processing Admission / Credentials-Grenze | **continue**; vor externem Processing wirksam |
| #57 Restartability/Availability | product quality + verification | providerunabhängige Fortsetzbarkeit | **continue**; synthetisch parallel, real nach #49/#51/#53 |
| #58 ADR | governing/project | material/reversible Entscheidungsgrenze | **keep on-demand**, kein Gate |
| #59 Development/Verification | governing/project + delivery | Umsetzung accepted Requirements | **keep**; Vertical Product Slices als primäre Delivery-Einheit bevorzugen |
| #60 Domain Method Profiles | domain/research | Method Truth | **keep core**; method-sensitive Product Logic konsumiert, definiert sie nicht |
| #61 Work Context/Method Conformance | operational support | Resume-/Conformance-Unterstützung | **continue bounded**; generiert/referenziert statt Method Truth zu duplizieren |
| #62 Requirements Assurance | operational support | formale Requirement-QA | **keep background**; keine Produkt-Erfolgsmetrik |
| #63 Value/Decision/Delivery/Feedback | operational support + governing trace | Trace/Feedback-Schleife | **keep background**; Feedback als Product Evidence, nicht historische Evidenz |
| #64 Complexity Audit | review input | Anti-Pathology-/Value-Challenge | **consume into #92**, danach dispositionieren; keine Implementation Authority |
| #65 Wissensarbeit Pilot Review | pilot/review input | candidate prior-art feedback | **consume selectively**, keine automatische Promotion |
| #67 Project Memory | operational support candidate | Conversation->Git / readable state | **reconcile with existing context/derive mechanisms**; keine zweite Memory-Plattform |
| #85 Ranis Material Corpus | pilot/testfixture | case-spezifischer Research-State-Stressfall | **keep isolated until pilot closure**, dann archive/keep-case-specific |
| #86 Shared Research State Pilot | pilot/testfixture | Test vorhandener State-/Context-Mechanismen | **closure path only**; kein `ResearchModule`-Revival |
| #89 Fresh-context Eval | pilot verification | unabhängiger Closure-Test #86 | **complete before #86 disposition** |
| PR #83 / #84 | repair/cleanup | Selection-/Handoff-Reconciliation | **separate from re-baseline**; nicht als Dauerarchitektur übernehmen |
| PR #69 | review/cleanup | früher Zielbild-/Wissensarbeit-Review | **do not use as authority**; nach Re-Baseline verkürzen/close/supersede nach Review |
| PR #90 | pilot/spike evidence under #51 | Document-Evidence-Falsifikation | **continue only to resolve stated semantic gates**; technische Reproduktion != Acceptance |
| PR #91 | integration evidence under #49 | Zotero capability probe | **review as #49 evidence**; branch result != main/canonical completion |

### Konsequenz

Die meisten benötigten Verantwortungen existieren bereits. **#92 erzeugt daher keine Serie neuer Architektur-Issues.** Neue Folgetickets entstehen nur, wenn R1–R4 eine echte unabhängige Lücke mit eigener DoD nachweisen.

---

## 6. Ziel-Verantwortungsmodell

Die folgende Darstellung ist **kein Layer Cake** und keine erlaubte Abhängigkeitsrichtung. Sie macht Verantwortungen sichtbar.

```text
HISTORISCHE FORSCHUNG / RESEARCH OWNER
Frage · Relevanz · Priorität · Review · Acceptance
          |
          v
DOMAIN / RESEARCH
Fachkompetenz · Methode · Quellenkritik · Evidence Meaning
Source · Instance · Derivative · Findspot · Finding · Claim · Hypothese
          |
          v
PRODUCT CAPABILITIES
Source/Library Support · Document Inspection · OCR/HTR · Retrieval
Research Navigation · Candidate/Promotion UX · Audit/Views
          |
          +-----------------------------+
          |                             |
          v                             v
INTEGRATION ADAPTERS              OPERATIONAL SUPPORT
Zotero · OneDrive · PDF libs      validate · trace · context
OCR/HTR engines · Search          resolve · evidence · transition · derive
          |                             |
          +-------------+---------------+
                        v
                CANONICAL / CURATED STATE
                + regenerierbare Derivate
```

### Keine harte Schichtenabhängigkeit

- `domain/research` ist kein technisches Library-Layer, sondern besitzt fachliche Bedeutung/Method Truth.
- Integrationen können technisch Teil einer Product-Package-Struktur sein.
- Operational Support darf Domain-/Product-State lesen und formale Regeln ausführen, besitzt aber nicht deren fachliche Wahrheit.
- Product Capabilities können externe Werkzeuge nutzen, ohne externe Provider zum kanonischen Research State zu machen.

---

## 7. Produktcode vs. `tools/`: Entscheidungsregel

Die Re-Baseline setzt **nicht** voraus, dass jedes konkrete Projekt `src/` benötigt. Sie setzt nur eine semantische Grenze voraus:

> **Dauerhafte Forschungsassistenz-Produktlogik und Repo-/Assurance-/Operational-Tooling dürfen nicht unbemerkt dieselbe Verantwortungszone werden.**

### Operational Tooling bleibt typischerweise unter `tools/`, wenn es primär:

- Repo-/Project-State validiert;
- Coverage/Trace/Audit ableitet;
- Migration/Fixture/Benchmark ausführt;
- CI/Developer-/Handoff-Prozesse unterstützt;
- einmalige Feasibility-/Probe-Aufgaben erledigt.

### Product Logic entsteht, wenn eine Fähigkeit:

- im normalen Forschungsworkflow dauerhaft aufgerufen wird;
- eine fachlich/produktseitig akzeptierte Capability realisiert;
- nicht nur Repo-/Dev-Betrieb, sondern Research Work ausführt;
- stabile Product Interfaces/Tests benötigt;
- unabhängig von einem einzelnen Spike wiederverwendet wird.

### `src/histo_orla/` als Candidate

Eine Package-Grenze wie `src/histo_orla/` wird erst eingeführt, wenn ein reales Inkrement dies rechtfertigt. Gute Trigger wären z. B.:

1. #49 liefert einen dauerhaften Zotero/Source Resolver, **oder**
2. #51/#53 benötigen denselben Runtime Research-State-/Document-Core, **oder**
3. Product-/Operational-Code beginnt dieselben Begriffe mit unterschiedlichen Verantwortungen zu vermischen.

Nicht ausreichende Trigger:

- „Wissensarbeit erwähnt `src/`“;
- Wunsch nach schönerer Ordneroptik;
- leere Future-Proof-Struktur;
- ein einzelnes experimentelles Skript.

Erste mögliche Struktur **nur bei Trigger**, nicht als Vorabentscheidung:

```text
src/histo_orla/
  research/          # product-nahe Research-State-Anwendung, keine Method Truth
  sources/           # Source/Instance runtime handling
  integrations/      # z. B. zotero/, onedrive/
  documents/         # inspect/findspot runtime
  processing/        # OCR/HTR processor adapters
  retrieval/         # exact/historical retrieval
  views/             # productseitige Research Views
```

Die konkrete Struktur wird aus den ersten realen Product Capabilities refactored, nicht prophylaktisch vollständig angelegt.

---

## 8. Tooling-Support als First-Class Product Concern

„Provider austauschbar“ bedeutet **nicht** „konkretes Tooling ist nebensächlich“.

Für Histo-Orla gilt:

> Ein Werkzeug besitzt keine wissenschaftliche Wahrheit; eine hochwertige Integration des Werkzeugs kann trotzdem zentraler Produktnutzen sein.

### Zotero / OneDrive als Referenzfall

Verantwortungsgrenze:

```text
Zotero
= bibliographische/archivische Verwaltung + Item/Attachment-Referenzen

OneDrive / lokale Datei
= Source of Bytes / Locator- und Versionsebene

Histo-Orla
= providerunabhängiger kuratierter Research State
```

Produktziel für den späteren dauerhaften Pfad:

```text
Zotero Item
-> Attachment
-> permitted linked-file / byte resolver
-> konkret verifizierte inspected instance
-> document / page / region / findspot
-> derivative / OCR / retrieval
-> finding / audit view
```

Wissenschaftliche Schutzgrenzen:

- Zotero Key != interne kanonische Identität;
- Pfad/URL != inspected instance;
- Metadatenzugriff != Evidence Availability;
- Byte-Erreichbarkeit != fachliche Inspection;
- OCR/HTR != Originalbefund;
- Retrieval Hit != Finding/Claim;
- Write-back nur kontrolliert und nach realem Need.

### Architecture-Fitness-Regel für jedes Tool

```text
reales Research Need / Pain
-> avoid unnötige Technik
-> reuse vorhandenes gutes Fach-/Standardwerkzeug
-> configure
-> integrate
-> thin custom layer
-> build custom nur bei nachgewiesener Restlücke
```

Für jede neue Tool-/Provider-Entscheidung müssen mindestens Nutzen, wissenschaftlicher Loss-Risk, Rights/Privacy, Portabilität, Recovery und Exit Path sichtbar sein.

---

## 9. Dependency-Map der bestehenden technischen Arbeit

### 9.1 Semantische / fachliche Prerequisites

- #42 liefert accepted Requirements.
- #50 liefert den case-unabhängigen Canonical-State-/Identity-Contract.
- #60 liefert Method Truth für method-sensitive Research-Arbeit.
- #56 liefert Processing-/Rights-Admission für externe Verarbeitung.

### 9.2 Runtime-/Data-Prerequisites

```text
#50 Canonical State / Identity
  |
  +--> #49 external bibliographic/source mapping
  |       |
  |       +--> real byte resolution
  |               |
  |               v
  +-----------> #51 Document / Findspot
                    |
                    +--> #53 real Retrieval E2E
                    +--> #52 real OCR/HTR E2E
                    +--> #55 real provenance/audit navigation
                    +--> #57 real restartability/availability verification

#50 --> #54 transition / canonical mutation guards
#56 --> any external/cloud processor action
```

### 9.3 Parallel mögliche Arbeit

Ohne auf den kompletten kritischen Pfad zu warten:

- #52 Processor Contract / synthetischer Benchmark-Harness;
- #53 Exact-/Variant-/Query-Log Contract mit synthetischen Fixtures;
- #54 Transition-Contract + synthetische negative State-Transitions;
- #55 Derived Audit View gegen synthetischen State;
- #56 Rights-/Admission Contract;
- #57 providerneutraler Export-/Removal Contract;
- #60 Method Profiles;
- #61 generierter Work Context / Conformance nur für bereits geklärte Semantik;
- #62/#63 bestehende Assurance weiterverwenden, nicht ausbauen ohne beobachtete Lücke.

### 9.4 Pilot-/Cleanup-Dependencies

```text
#89 fresh-context evaluation
  -> #86 final disposition
      -> #85 later archive/keep-case-specific decision

PR #83
  -> PR #84 revalidation / PROJECT_STATE selection reconciliation

PR #90
  -> human/semantic gold-region + finding-anchor review
  -> erst dann #51 disposition dieses Spikes

PR #91
  -> #49 evidence review
  -> kein Ersatz für verbleibende byte/integrity/cross-device tests
```

Selection-Reconciliation ist **kein Blocking-Prerequisite für R1–R4**, aber ein konkreter realer Product Slice darf daraus nicht selbst eine `selected-current` Research-Aufgabe erfinden.

---

## 10. Roadmap

### R0 — Fresh Baseline / Freeze on Invention

**Ziel:** Keine Reorganisation aus Erinnerung oder ästhetischem Impuls.

**Inputs:** AGENTS, PROJECT_STATE, README, #42, #48, #50, #60, aktuelle Architecture-/Assurance-Artefakte, offene Issues/PRs, frisches `Wissensarbeit`/`paleo-type` Prior Art.

**Exit:**

- inspected baseline mit Commit-/PR-/Issue-Stand dokumentiert;
- branch-only Findings klar von `main` getrennt;
- keine neue Authority/Selection erfunden.

**Status:** mit Anlage von #92 und diesem Dokument begonnen; vor materieller Fortsetzung jeweils fresh-read.

### R1 — Inventory / Disposition

**Ziel:** Das gewachsene System entlang der sechs Kategorien lesbar machen.

**Arbeit:**

- relevante Docs/Tools/Issues klassifizieren;
- doppelte oder nur historisch aktive Artefakte markieren;
- `keep | reconcile | route | archive/supersede | needs-decision` vergeben;
- echte Lücken von bloß schwer auffindbaren bereits vorhandenen Mechanismen unterscheiden.

**Exit:**

- ein Concern hat nicht mehrere scheinbar gleichrangige Truth Homes;
- jede dauerhafte Capability besitzt einen bestehenden Owner oder eine belegte echte Lücke;
- keine neue Issue-Serie nur für Umbenennung/Klassifikation.

### R2 — Governing / Product Objective Reconciliation

**Ziel:** Eine verständliche obere Hierarchie aus bereits akzeptierter Substanz herstellen.

**Output Candidate:** kurze, menschenlesbare Sicht auf:

1. Forschungs-/Produktziel;
2. Governing Invariants;
3. Authority-/Evidence-Präzedenz;
4. Tooling-/Product-Subsidiarität;
5. Restartability/HITL;
6. Verhältnis Research State ↔ Product Assistance ↔ Operational Support.

**Schutz:** Kein neuer Grundsatz wird als bindend markiert, nur weil er aus Prior Art gut klingt. Materiale Deltas werden zu bestehender Authority geroutet.

### R3 — Product / Research / Tool Capability Architecture

**Ziel:** Das eigentliche Produkt sichtbar machen, nicht nur seine Governance.

**Output Candidate:** Capability Map mit mindestens:

- Source/Library Support;
- Document Inspection / Findspot;
- Processing OCR/HTR;
- Historical Retrieval;
- Research-State Navigation;
- Method-/Competence-aware Assistance;
- Candidate/Promotion Interaction;
- Audit / Human-readable Views;
- Restartability / Availability;
- Tool-/Provider Integrations.

Für jede Capability:

```text
Research Need / Pain
-> accepted Requirement(s)
-> Domain / Method constraints
-> existing external tool / standard
-> Product responsibility
-> Operational support needed
-> dependencies
-> verification / owner acceptance
-> non-goals
```

### R4 — Minimal Repo-/Code-Topology Decision

**Ziel:** Physische Struktur folgt Verantwortung, nicht umgekehrt.

**Entscheidungsfragen:**

- Welche heutige `tools/`-Logik ist wirklich Operational Support?
- Welche kommende Runtime-Funktion ist dauerhafte Product Capability?
- Gibt es reale Coupling-/Packaging-/Testprobleme, die `src/histo_orla/` löst?
- Welche bestehenden Dateien müssen **nicht** verschoben werden?
- Welche Migration hätte epistemischen/traceability Loss?

**Default:** no move.

**Trigger für Strukturänderung:** erster dauerhafter Product-Code-Slice oder belegte Vermischung.

**Bei materieller/schwer reversibler Entscheidung:** #58 / ggf. #44.

### R5 — Thin Vertical Product Slice

**Ziel:** Gesamtarchitektur an realer Arbeit beweisen, bevor weitere horizontale Infrastruktur wächst.

**Candidate Slice – noch keine Research-Selection:**

```text
Owner-authorisierte reale Quelle
-> Zotero item/attachment resolve (#49)
-> bytes erreichbar + instance verifizieren (#49/#50/#56)
-> Seite/Region/Findspot inspectable (#51)
-> Exact/Historical Retrieval (#53; ggf. OCR/HTR #52 falls nötig)
-> Observation/Finding bleibt evidence-/method-aware (#50/#60)
-> human-readable provenance/audit view (#55)
-> next action / context restartbar (#57/#61)
-> Owner-Workflow-Feedback (#63)
```

Der konkrete Research Case/Source wird **nicht von dieser Roadmap ausgewählt**.

**Acceptance:**

- echte manuelle Orchestrierung sinkt;
- Source/Instance/Findspot bleiben korrekt;
- Retrieval/Processing überclaimt nicht;
- keine fachliche Promotion durch Tool/CI;
- neuer Kontext kann fortsetzen;
- Owner versteht Ergebnis und nächste Aktion ohne Repo-Engineering.

### R6 — Operational Core Consolidation

**Ziel:** vorhandene Mechanismen kohärent ausführen, nicht neues Framework bauen.

Logische Capabilities:

```text
validate | resolve | context | evidence | transition | derive
```

**Reihenfolge:**

1. existierenden `tools/operational/core.py` nur dort erweitern, wo reale Consumer entstehen;
2. #62/#63 Wrapper kompatibel halten;
3. #49/#57 speisen `evidence` nur mit technisch prüfbaren Zuständen;
4. #54 wird `transition`-Capability statt separater Workflow-Engine;
5. #55/#61 konsumieren `derive/context` statt Regelprosa zu kopieren;
6. einheitliche CLI/Skill-Hülle erst nach stabilen Core-Interfaces.

**Stop Rule:** Keine Abstraktion ohne mindestens zwei reale Consumer oder klaren Cross-Cutting-Invariant.

### R7 — Pilot / Legacy / Review Cleanup

**Ziel:** Entstehungsgeschichte bleibt nachvollziehbar, dominiert aber nicht mehr den aktiven Systemstand.

**Dispositionen erst nach jeweiligem Gate:**

- #64: Findings in #92/Owner-Pfade aufgenommen -> close/archive as review input;
- #65 / PR #69: nur noch nicht anderswo aufgenommene Candidate-Learnings behalten; keine Parallel-Architektur;
- #86 nach #89: `archive pilot | keep case-specific | route concrete friction`;
- #85 danach separat `archive | keep case-specific fixture`;
- Selection-Repair #83/#84 nach Integration nicht als dauerhafte Produktkomponente behandeln;
- historische/überholte Architecture-Prosa klar als superseded/provenance markieren, nicht löschen, sofern Provenienz relevant bleibt.

### R8 — Fresh-Context + Owner Acceptance / Closure

**Ziel:** Ganzheitliche Operationalisierung wird an Nutzung, nicht Dokumentmenge gemessen.

**Fresh-context test:** Ein neuer kompetenter Bearbeiter kann ohne Chat beantworten:

- Was ist das Produktziel?
- Was ist Domain/Method Truth und wo liegt sie?
- Was ist Product Capability, was Operational Support?
- Welcher State ist canonical, welcher derived/regenerable?
- Welche Piloten sind aktiv, abgeschlossen oder nur Provenienz?
- Welche technische Arbeit ist als Nächstes dependency-ready?
- Welche Arbeit darf **nicht** ohne Owner/Domain/Requirement-Entscheidung erfolgen?

**Owner acceptance:** Mindestens für den Thin Vertical Slice:

- weniger manuelle Schritte/Medienbrüche;
- weniger Chat-/Repo-Orchestrierung durch den Owner;
- gleiche oder bessere Quellen-/Provenienz-/Methoden-Nachvollziehbarkeit;
- Fehler/Unverfügbarkeit werden sichtbar statt still kompensiert;
- keine neue störende Governance-Zeremonie entsteht.

CI/Tests sind notwendige technische Evidenz, aber kein Ersatz für diese Acceptance.

---

## 11. Kritischer Pfad und Parallelisierung

### Kritischer Product Path

```text
#50 semantic contract
-> #49 reliable source/byte resolution
-> #51 document/findspot runtime path
-> #53 exact/historical retrieval against real source
-> #55 understandable audit/navigation
-> #57 fresh-context availability/restartability
-> R5 owner acceptance
```

### Parallel Guard / Safety Path

```text
#42 requirements
-> #54 transition guards
-> #56 rights admission
-> #62/#63 existing formal assurance
-> R6 incremental core integration
```

### Parallel Method Path

```text
#60 Domain Method Profiles
-> method-sensitive constraints for R5
-> domain review / no false promotion
```

### Parallel Pilot Closure Path

```text
#89 -> #86 disposition -> #85 later cleanup
```

Keine dieser Parallelspuren wird künstlich zu einem globalen Gate. Nur der konkret abhängige Product Slice wartet auf seine echten Prerequisites.

---

## 12. Anti-Pathology / Architecture Fitness Checks

Vor jeder Re-Baseline-bedingten Änderung wird diese Liste geprüft.

### AP-01 — Owner Proliferation

**Signal:** neuer Begriff erzeugt automatisch neues Issue/Owner/Registry.  
**Guard:** erst bestehendes kanonisches Home suchen; neues Issue nur nach AGENTS/#23-Kriterien.

### AP-02 — Second Truth Store

**Signal:** Roadmap, JSON, View oder Tool kopiert fachliche/Requirement-Prosa und kann driften.  
**Guard:** referenzieren/derive statt duplizieren.

### AP-03 — Folder-Driven Architecture

**Signal:** Ordner werden angelegt, bevor reale Product Responsibilities implementiert sind.  
**Guard:** semantische Klassifikation zuerst; `src/` nur bei Trigger.

### AP-04 — Big-Bang Refactor

**Signal:** große Verschiebung/Rewrite nur für Kohärenzgefühl.  
**Guard:** strangler-/incremental move; bestehende Commands kompatibel; no-loss verification.

### AP-05 — Operational Core becomes Platform

**Signal:** Workflow Engine, Policy DSL, Agent Framework, Event Bus oder universeller Service-Layer ohne konkreten Need.  
**Guard:** kleinster Core; jede Erweiterung braucht realen Consumer/Requirement.

### AP-06 — Pilot Fossilization

**Signal:** Case-Begriff, Fixture-Struktur oder Pilot-Workflow wird still generisch.  
**Guard:** explizite `keep | route | archive | supersede`; Cross-Case-/SOTA-/Authority-Promotion separat.

### AP-07 — Tool Marginalization

**Signal:** Provider-Unabhängigkeit wird so verstanden, dass konkrete Research UX/Integration unwichtig sei.  
**Guard:** Tooling als Product Capability evaluieren; wissenschaftliche Authority trotzdem außerhalb des Tools halten.

### AP-08 — Tool Lock-in

**Signal:** Zotero/OneDrive/Search/OCR-Identifier werden alleinige Research-State-Identität.  
**Guard:** Adapter-/External-Reference-Grenzen aus #50/#49; Export/Provider Removal #57.

### AP-09 — Assurance Success Laundering

**Signal:** green CI / reproducible output wird als wissenschaftliche oder Owner Acceptance kommuniziert.  
**Guard:** Verification Class explizit ausweisen; R8 Owner-/Domain-Acceptance separat.

### AP-10 — Human as Workflow Engine

**Signal:** Owner muss Resolver, Exporte, Context, Trace, Tools und Persistenz manuell orchestrieren.  
**Guard:** Product Slice misst eingesparte Handarbeit/Medienbrüche; deterministische Mechanik automatisieren.

### AP-11 — Domain Flattening

**Signal:** generischer Product-/AI-Workflow ersetzt disziplinspezifische Methodik.  
**Guard:** #60 Method Truth bleibt eigene Authority; Product Code konsumiert Method Constraints.

### AP-12 — Premature Abstraction

**Signal:** gemeinsame API/Modelle entstehen vor zwei realen Verwendungen.  
**Guard:** lokale Implementation zuerst; erst nach realer Duplikation oder Cross-Cutting-Invariant extrahieren.

---

## 13. Migration-/No-Migration-Regeln

Die Re-Baseline ist **keine Repo-Aufräumaktion um ihrer selbst willen**.

### Standard: nicht verschieben

Bestehende kanonische Artefakte bleiben zunächst dort, wo ihre Ownership/Traceability heute funktioniert.

### Verschieben/refactoren nur wenn mindestens eines gilt

- aktuelle Lage verursacht reale Fehlklassifikation oder Drift;
- Product/Operational-Verantwortung kann sonst nicht sauber getestet/deployed/genutzt werden;
- derselbe Runtime-Code wird in mehreren Tools kopiert;
- Packaging/Imports/Test-Isolation werden real zum Bottleneck;
- der neue Ort verbessert Restartability/Discoverability ohne zweiten Truth Store.

### Jede Migration braucht

- Source/Target und Canonical-Ownership-Erhalt;
- referential/no-loss check;
- Backlink/Supersedes-Hinweis, falls nötig;
- Tests/CI für technische Invarianten;
- keine Änderung fachlicher Bedeutung als Seiteneffekt.

---

## 14. Roadmap-Steuerung ohne neue Bürokratie

#92 ist der Re-Baseline-Owner. Dieses Dokument hält **die integrierte Roadmap**, aber nicht Detailwahrheiten der Teilpakete.

Arbeitsregel:

```text
#92 / rebaseline-roadmap.md
= integrierte Disposition + Dependencies + Gate/Next-Step

#49–#63 / jeweilige kanonische Artefakte
= Detail-Scope, Findings, Contracts, Tests, Implementation
```

Updates in #92 erfolgen nur bei:

- veränderter Dependency;
- bestätigter Kategorie-/Disposition;
- neu nachgewiesener echter Architecture-Lücke;
- beschlossenem Repo-/Product-Code-Topology-Delta;
- Abschluss eines Roadmap-Gates;
- relevanter Owner-/Workflow-Acceptance.

Keine manuelle Synchronisation jedes Detailstatus in mehrere Dateien.

---

## 15. Definition of Done der Re-Baseline

Die Re-Baseline ist abgeschlossen, wenn:

1. ein frischer Bearbeiter die aktuelle Systemgestalt aus wenigen kanonischen Einstiegspunkten versteht;
2. `governing/project`, `domain/research`, `product capability`, `operational support`, `pilot/testfixture`, `superseded/archive` praktisch unterscheidbar sind;
3. Product Capability vs. Operational Tooling an realer Implementierung sauber getrennt ist;
4. Tooling-Support – insbesondere Zotero/OneDrive/Document/OCR/HTR/Retrieval – als Produktnutzen sichtbar ist, ohne wissenschaftliche Authority zu übernehmen;
5. #49–#63 in einer kohärenten Dependency-/Delivery-Sicht stehen, ohne neue Parallelowner;
6. eine mögliche `src/histo_orla/`-Grenze nur aus realer Product-Implementierung entstanden ist oder bewusst als derzeit unnötig verworfen wurde;
7. mindestens ein Thin Vertical Product Slice end-to-end real benutzt und Owner-seitig bewertet wurde;
8. Operational Core nur die tatsächlich gemeinsam benötigten Mechanismen enthält;
9. Piloten/Review-Learnings explizit disponiert sind und keine stale Pilotsemantik aktuelle Arbeit steuert;
10. technische Verification, wissenschaftliche/Methodenprüfung und Owner-/Workflow-Akzeptanz weiterhin getrennt bleiben;
11. keine Re-Baseline-Migration Research-/Provenienz-/Requirement-/Authority-Bedeutung verloren hat;
12. `PROJECT_STATE.md` und Einstiegssichten nach Abschluss der separaten Selection-Reconciliation wieder den tatsächlich akzeptierten Stand kompakt abbilden.

---

## 16. Unmittelbar nächste, dependency-sichere Aktionen

1. **R1 abschließen:** Repo-Artefakte/Tools gegen die Dispositionsmatrix prüfen; nur echte Widersprüche/Lücken in #92 festhalten.
2. **#49/PR #91 sauber reviewen:** aktuelle Zotero-Probe als Integrationsevidenz einordnen; verbleibende Byte-/Integrity-/Cross-device-Grenzen nicht überspringen.
3. **#50/#51-Grenze stabil halten:** kein Product-Code-Refactor vor belastbarem Source/Instance/Findspot Runtime Need.
4. **#83 -> #84 separat reconciliieren:** `PROJECT_STATE.md` erst danach aus der Re-Baseline aktualisieren.
5. **#89 abschließen:** danach #86 und anschließend #85 disponieren, statt Pilotbegriffe in R3 mitzuschleppen.
6. **R2/R3 als Review-Candidate erarbeiten:** kurze Governing-/Product-Sicht + Capability Architecture, ohne accepted Requirements oder Method Truth zu überschreiben.
7. **Erst danach R4:** Product-Code-/Repo-Topology entscheiden.
8. **Dann R5 auswählen:** konkreten Thin Vertical Product Slice nur nach expliziter Owner-Auswahl der realen Research-Aufgabe/Quelle ausführen.

> **Leitregel:** Erst vorhandene Substanz lesbar zusammenführen, dann genau die kleinste fehlende Produktstruktur implementieren. Kein neuer Rahmen darf mehr Koordinationsarbeit erzeugen als er dem Research Owner abnimmt.
