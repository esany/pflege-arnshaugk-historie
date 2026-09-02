# Histo-Orla – Operational Execution Architecture Integration

**Status:** `technical integration analysis / architecture hypothesis / no framework decision`  
**Work Owner:** #48 Technical Lead  
**Interfaces:** #42 Requirements, #50 Canonical State, #54 Transitions, #55 Audit, #57 Restartability/Evidence Availability, #61 Work Context/Method Conformance, #62 Requirements Assurance, #63 Value/Decision/Delivery/Feedback Assurance  
**Prior Art:** `esany/paleo-type` #66/#77/#79, `tools/source_contract.py`  
**Stand:** 2026-09-02

## 1. Fragestellung

Histo-Orla hat bereits mehrere richtige Schutzmechanismen aufgebaut:

- Requirements-Struktur, Authority und Dependencies (#42);
- deterministische Requirements-QA (#62);
- Goal/Need/Pain → Requirement → Decision → Delivery → Feedback Traceability (#63);
- bindenden Work-Context-/Handoff-Vertrag (`AGENTS.md` §13/14);
- geplante Candidate→Review→Promotion-/Transition-Grenze (#54);
- Method-Conformance-/Restartability-Research (#61/#57);
- Human-readable Audit als abgeleitete Sicht (#55).

Das neue Risiko ist nicht mehr fehlende Governance, sondern **fragmentierte Operationalisierung**: dieselbe Ausführungslogik darf nicht künftig parallel als Markdown-Regel, eigener Validator, Workflow-Snippet, Template und Skill rekonstruiert werden.

Die Integrationsfrage lautet daher:

> Wie werden bereits akzeptierte wissenschaftliche/produktseitige Semantiken mit dem kleinsten kohärenten technischen Kern ausführbar, ohne Fachurteil in Software zu determinisieren oder ein neues Plattformprojekt zu erzeugen?

## 2. Übertragbarer Kern aus `paleo-type`

Das relevante Pattern ist:

```text
SCHOLARLY / GOVERNING SEMANTICS
Goals / Needs / Pains + Requirements + Method + Decisions
                    ↓
OPERATIONAL CONTRACT LAYER
Ownership + Enforcement Mapping + Invariants + Transition/Capability Boundaries
                    ↓
SMALL RSE CORE
validate | resolve | derive | context | evidence | transition
                    ↓
EXECUTION ADAPTERS
CLI | CI | Skills | Templates
                    ↓
DERIVED VIEWS
Audit | Context | Handoff | Coverage | Reports
                    ↓
AI / HUMAN EXECUTION
replaceable model/session/researcher
                    ↓
CANONICAL RESEARCH STATE
```

Leitprinzipien:

1. **Das Modell soll keine Regel erinnern müssen, die Software zuverlässig ausführen kann.**
2. **Software darf kein wissenschaftliches Urteil entscheiden, das Evidenz-/Fachbewertung verlangt.**
3. **Skills/Templates/CI sind Adapter, nicht Truth Stores.**
4. **Generierte Views sind rebuildbar und werden nicht manuell als zweite Wahrheit gepflegt.**
5. **Ein anderes Modell darf andere Candidates erzeugen; es erhält dadurch keine automatische Mutation Authority.**

## 3. Histo-Orla: Was bereits vorhanden ist

| Funktion | Semantic Owner | Aktueller Mechanismus | Status |
|---|---|---|---|
| Requirement Truth / Lifecycle | #42 | Markdown Requirements + Responsibility/Dependency Map | vorhanden |
| Requirement formale QA | #62 | JSON Schema + `tools/requirements/validate.py` + Tests + CI | implementiert |
| Value/Decision/Delivery/Feedback Trace | #28/#42/#48/#59 | `tools/assurance/*` + Tests + CI | implementiert v0.1 |
| Governance-IDs | #9 | `tools/assurance/governance-registry.json` | implementiert v0.1 |
| Work Context / Authority / Handoff | #9/#61 | `AGENTS.md` + Architecture Research | semantisch vorhanden, Generator fehlt |
| Method Application / Conformance | #60/#61 | Architecture Contract/Hypothese | teilweise, ausführbarer Teil fehlt |
| Candidate→Review→Promotion / canonical mutation | #54 | Technical Contract geplant | noch nicht implementiert |
| Source/Instance/Findspot resolution | #50/#49/#51 | Canonical-State Contract + Integrationsarbeit | teilweise/noch nicht ausführbar |
| Evidence availability / restartability | #57/#49 | Verification Contract | noch nicht ausführbar |
| Audit / human-readable research view | #55 | Prototype Contract | noch nicht implementiert |
| Skills | jeweilige Capability | noch keine kanonische Operational-Schicht | bewusst deferred |

Damit liegt Histo-Orla **nicht am Anfang**. Der sinnvolle Schnitt ist Konsolidierung und Erweiterung einer bereits begonnenen Assurance-Architektur.

## 4. Konkreter Fragmentierungsbefund im aktuellen Code

Die zwei vorhandenen Validatoren sind fachlich getrennt richtig, besitzen aber bereits wiederholte Infrastruktur:

- eigene `Finding`-Dataklasse;
- eigene Root-/Datei-/JSON-Loader;
- eigene JSON-Schema-Validation;
- eigene Requirement-ID-Extraktion;
- eigene Coverage-Parsing-/Referenzlogik;
- eigene CLI-/Exit-Code-/Output-Logik.

Aktuell:

- `tools/requirements/validate.py`
- `tools/assurance/validate.py`

Ein dritter separater Validator/Resolver für #61/#54/#57 würde diese Fragmentierung weiter verstärken.

**Disposition:** Die vorhandenen Tools bleiben funktional gültig. Vor dem nächsten neuen Operational-Tool wird ein kleiner gemeinsamer Core extrahiert; kein Big-Bang-Rewrite.

## 5. Zentrales fehlendes Element: Requirement → Enforcement Registry

Histo-Orla besitzt Requirement Truth und erste ausführbare Guards, aber noch keine globale technische Sicht:

```text
Requirement
→ wer besitzt seine Bedeutung?
→ welche Teile sind deterministisch / prozedural / fachlich?
→ welcher Contract operationalisiert sie?
→ welche Rule-ID erzwingt sie?
→ welcher Resolver/Generator/Transition-Guard unterstützt sie?
→ welche Fixture beweist das Verhalten?
→ welcher Teil bleibt Human/Domain/Specialist Review?
→ Implementations-/Verification-Status?
```

Empfohlene minimale machine-readable **Operational Enforcement Map** unter #48, mit Referenzen statt duplizierter Requirement-Prosa.

Candidate-Felder:

```text
requirement_id
semantic_owner_refs[]
enforcement_class = deterministic | procedural | scholarly | mixed
contract_refs[]
rule_refs[]
core_capabilities[]
human_or_specialist_review[]
fixture_refs[]
implementation_status
notes
```

Nicht hinein gehören:

- Requirement Statement/Rationale als zweite Truth;
- historische Interpretation;
- komplette Method Profiles;
- technische Lieblingslösung ohne Requirement-Bezug.

### Warum das jetzt relevant ist

Die Map würde #62, #63, #54, #55, #57 und #61 erstmals **als eine Ausführungsarchitektur** sichtbar machen, statt als nebeneinanderliegende Workstreams. Sie ist Technical-Delivery-Metadaten unter #48, nicht neuer Requirement Owner.

## 6. Kleiner gemeinsamer RSE Core – Ziel, nicht sofortiger Rewrite

Sobald ein dritter ausführbarer Mechanismus hinzukommt, sollte die gemeinsame Infrastruktur nicht erneut kopiert werden.

Logische Capabilities:

```text
validate    formale Invarianten / Referenzintegrität
resolve     kanonische IDs, Ownership, Ancestry, Source/Instance/Requirement-Pfade
derive      rebuildbare Views / Coverage / Audit / Reports
context     aktuellen Work Context/Handoff aus kanonischem State komponieren
evidence    Identität, tatsächliche Verfügbarkeit, Rights-/Access-Status prüfen
transition  zulässige canonical-state Mutation prüfen, nie Fachurteil erzeugen
```

Später nur bei realem Bedarf:

```text
intake      wiederkehrende korrekte Initialisierung
migrate     explizite, verlustgeprüfte State-Migration
```

### Implementationsstrategie

Kein sofortiges neues Framework. Leaner Pfad:

1. gemeinsame Loader/Findings/Schema-/Reference-Utilities aus #62/#63 extrahieren;
2. bestehende zwei Validatoren zunächst als Wrapper/Commands weiterverwenden;
3. nächster neuer Mechanismus (#61/#54/#57) nutzt den gemeinsamen Core;
4. erst dann eine einheitliche CLI-Oberfläche stabilisieren.

Wenn daraus ein dauerhaftes lokales Python-Tool wird, ist eine normale `pyproject.toml`-/`src`-Package-Struktur mit einem `project.scripts`-Entry-Point der aktuelle Python-Packaging-Standard. Das ist Packaging Best Practice, keine Requirement-/Framework-Pflicht.

Referenz: https://packaging.python.org/en/latest/guides/creating-command-line-tools/

## 7. Empfohlene CLI-Oberfläche als Adapter

Langfristiges UX-Ziel, noch keine Pflicht-Namenskonvention:

```text
histo validate requirements
histo validate trace
histo validate all

histo context <work-owner/task>
histo evidence check <source/instance/task>
histo resolve <id>
histo derive audit <object>
histo transition check <candidate/target>
```

Der CLI-Adapter enthält keine eigene fachliche Regelwahrheit. Dieselbe Core-Funktion wird aus CI, Skill oder lokalem Tool aufgerufen.

## 8. Work Contexts: sehr relevant, aber generiert

Der paleo-type-Gedanke ist direkt übertragbar:

```text
stable governance + current repo state + task/owner
→ transient executable context
```

Für Histo-Orla soll ein späterer Context-Generator mindestens die in `AGENTS.md` bereits bindend definierten Elemente komponieren:

- primary function;
- current work owner;
- purpose/scope/exclusions;
- leading/controlling domains;
- applicable method/quality frame;
- required evidence;
- may/must-not;
- stop/handoff;
- completion/return;
- persistence target.

Zusätzlich aus den `paleo-type`-Fixtures relevant:

- **CURRENT EXECUTABLE STAGE** vs. downstream not-yet-authorized work;
- **Evidence identified** vs. **Evidence accessible now**;
- Access-/Identity-Verifikation und Rights-Grenze.

Der Output ist ein **Build-Artefakt**, kein kanonischer Task-Truth-Store.

## 9. Skills: dünne Kompetenzadapter

Für Histo-Orla relevant, aber erst nach Core/API:

Ein Skill darf:

- passenden Work Context anfordern;
- den richtigen Core-Command ausführen;
- deterministische Ergebnisse erklären;
- fachliche Kandidaten/Research-Schritte innerhalb seiner Authority bearbeiten;
- Stop-/Handoff-Bedingungen einhalten.

Ein Skill darf nicht:

- AGENTS/Requirements/Methodik kopieren und damit zum zweiten Rule Store werden;
- Validator-PASS selbst behaupten;
- fachliche Validation simulieren;
- kanonische Mutation allein durch Modellurteil autorisieren.

## 10. Evidence Management: später eigener Core-Command

Für Histo-Orla besonders relevant wegen Zotero/OneDrive.

Zu trennen:

```text
IDENTIFIED
REPRODUCIBLE / VERSION-CHECKABLE
RETRIEVABLE
ACCESSIBLE NOW
INSPECTABLE IN CURRENT CONTEXT
RIGHTS-ADMISSIBLE FOR REQUESTED OPERATION
```

#49/#57 liefern die Semantik/Adapter. Ein späteres `evidence check` soll nur technisch prüfbare Teile auflösen und verbleibendes fachliches/visuelles Urteil explizit offenlassen.

Wichtig: `URN/URL/Zotero-Key bekannt` bedeutet nicht `Quelle jetzt für NEXT ACTION inspizierbar`.

## 11. Canonical Writes / Transition Control: höchste noch offene Relevanz

Dieser Punkt ist für Histo-Orla wichtiger als zusätzliche Prompt-/Skill-Templates.

Heute schützt #63 primär **technische Code-/Decision-Traceability**. #54 soll dagegen **Research-State-Promotion/Mutation** absichern.

Zielgrenze:

```text
READ / ANALYZE
→ innerhalb Role/Scope erlaubt

PROPOSE
→ Candidate/Alternative/Challenge

WRITE NEW OBSERVATION/FINDING
→ nur gemäß Objekt-/Method-/Evidence-Contract

PROMOTE / SUPERSEDE CANONICAL RESEARCH STATE
→ explizite zulässige Transition
→ Vorgängerzustand + Basis + Verantwortung/Review erhalten
```

Nicht automatisieren:

- richtige Lesung;
- historische Identität;
- Motiv/Interpretation;
- fachliche Suffizienz.

Automatisierbar, sobald Semantik stabil:

- Candidate ≠ canonical;
- unterschiedliches Modellurteil ≠ Mutation Authority;
- erforderliche Evidence/Method/Review-Refs vorhanden;
- Vorgänger/history bleibt erhalten;
- verbotene Transition wird abgewiesen.

**Empfehlung:** #54 wird nicht als separater Workflow-Stack gebaut, sondern als `transition`-Capability desselben Operational Core, sobald reale Histo-Orla-Research-State-Objekte die minimal nötige Semantik liefern.

## 12. Derived Views: #55 als Generator, nicht Truth Store

Direkt übertragbar:

```text
canonical state
→ deterministic derivation
→ human-readable view
```

Geeignete Histo-Orla Views:

- Research Audit;
- Requirement/Enforcement Coverage;
- Work Context;
- Handoff Packet;
- unresolved/debt view;
- Source/Instance/Findspot provenance view;
- Method Application / Review chain;
- Provider/availability report.

Wo eine View vollständig aus kanonischem State ableitbar ist, soll sie nicht manuell als zweite Wahrheit gepflegt werden.

## 13. CI: Vollstrecker, nicht Forschungsrichter

Aktueller #62/#63-Grundsatz bleibt richtig.

CI prüft nur bereits formal entschiedene Invarianten:

- Referenzen/IDs;
- Coverage;
- Governance-/Requirement-Trace;
- rebuildbare Derived Views;
- Migration-/History-Erhalt;
- zulässige formale Transitionen;
- technische Provider-/Availability-Fixtures.

CI entscheidet nie:

- historische Wahrheit;
- Quellenlesung;
- Methodenqualität;
- Specialist Agreement;
- reale Owner-Akzeptanz.

### Workflow-Konsolidierung

Seit dem gemeinsamen Core-Grundbaustein führt **ein** automatischer, path-gefilterter Assurance-Workflow die Requirements-, Trace- und Operational-Checks aus. Damit werden gekoppelte Änderungen atomar geprüft und parallele Läufe/Benachrichtigungen vermieden. Die Validator-Commands bleiben separat lokal ausführbar.

## 14. Adopt / Adapt / Defer

| `paleo-type`-Idee | Histo-Orla-Disposition | Begründung |
|---|---|---|
| Requirement→Enforcement Matrix | **ADOPT NOW** | zentrale aktuelle Integrationslücke |
| kleiner RSE Core statt Script-Sammlung | **ADOPT INCREMENTALLY** | zwei Validatoren zeigen bereits Infrastrukturduplikation |
| generated Work Context | **ADAPT / NEXT AFTER #61 MINIMUM** | Governance vorhanden, transienter Generator fehlt |
| Skills als dünne Adapter | **ADOPT PRINCIPLE / DEFER IMPLEMENTATION** | erst Core/API stabilisieren |
| Templates nur für Initialisierung | **ADOPT PRINCIPLE / DEFER** | noch kein wiederkehrender Histo-Intake-Bottleneck ausreichend belegt |
| Evidence Check | **ADAPT AFTER #49/#57** | für OneDrive/Zotero sehr relevant, Adaptersemantik noch in Arbeit |
| canonical mutation boundary | **ADOPT AS #54 CORE CAPABILITY** | größte noch offene Modellunabhängigkeitslücke im Research State |
| generated research/audit views | **ADOPT AS #55 DERIVATION** | verhindert manuelle zweite Wahrheit |
| ein CLI für alle Operationen | **ADOPT AS UX TARGET, NOT YET REWRITE** | konsistent, aber kein Big-Bang-Refactor |
| universal workflow/policy/agent engine | **REJECT NOW** | kein Requirement, Overengineering |
| paleo METHOD/CORPUS/PROJECT-Modell kopieren | **REJECT** | Histo-Orla besitzt eigene Source-/Research-State-Semantik |
| manuscript-specific witness tooling | **REJECT AS GENERIC** | nur quellentypspezifisch bei späterem Requirement |

## 15. Initiale Operational Architecture Matrix v0.1

| Systemfunktion | Kanonische Semantik | Determinismus | Mechanismus heute | Nächster Integrationsschritt |
|---|---|---|---|---|
| Requirements Authority/Deps | #42 | teils deterministisch | #62 | Enforcement Map ergänzen |
| Value/Decision/Delivery Trace | #28/#42/#48/#59 | formale Trace deterministic | #63 | in gemeinsamen Core integrieren |
| Governance Applicability | #9 | refs deterministic, Bedeutung nicht | #63 registry | Enforcement Map referenziert GOV-IDs |
| Work Context/Handoff | #9/#61 | Struktur teils deterministic | Prosa/Contract | read-only Context Composer |
| Method Conformance | #60/#61 | mixed | Contract | nur settled profile/application refs operationalisieren |
| Promotion/Mutation | #54 + Domain Method | transition deterministic, Urteil nicht | geplant | `transition` Core Capability mit realen Fixtures |
| Source/Instance/Findspot | #50/#49/#51 | Struktur/Resolution weitgehend deterministic | Contract/Research | `resolve` nach realem State/Adapter |
| Evidence Availability | #57/#49 | mixed | Verification Plan | `evidence check` nach Adapter |
| Audit | #55 | Darstellung deterministic aus State | geplant | `derive audit` statt manuelle Doppelpflege |
| Coverage/Reports | #42/#59 | deterministic | teils manuelles Markdown | langfristig aus machine state generieren |
| Skills | Capability/Role Owner | probabilistischer Executor | none | dünne Adapter nach Core |
| CI | #62/#63 | deterministic | 1 konsolidierter Workflow / getrennte Commands | Subchecks nur bei realem Laufzeitbedarf konditionalisieren |

## 16. Implementierter Integrationsschnitt v0.1 (2026-09-02)

Der erste kohärente Schnitt ist umgesetzt:

- `tools/operational/enforcement-map.json` ist die machine-readable technische Projektion `Requirement → Enforcement`; sie referenziert kanonische Requirements/Owner/Contracts, Rule-IDs, Fixtures, Core-Capabilities und Review-Grenzen, enthält aber keine Requirement-Statements oder fachliche Semantik;
- `tools/operational/enforcement-map.schema.json` und die Regeln `OPM001`–`OPM007` prüfen Form, bekannte Requirement-/Rule-Referenzen, eindeutige Mappings, vorhandene Fixture-Dateien und explizite Human-/Domain-/Specialist-Review-Grenzen für nicht rein deterministische Klassen;
- `tools/operational/core.py` bündelt ausschließlich mechanische Infrastruktur (Repo-Pfad, UTF-8-/JSON-Loading, JSON-Schema-Fehlernormalisierung);
- `tools/requirements/validate.py` und `tools/assurance/validate.py` bleiben die bestehenden Commands/Wrapper und behalten ihre Rule-Semantik;
- die Enforcement-Map wird durch Project Assurance validiert; ein dritter Workflow/Command wurde nicht eingeführt;
- die beiden bisherigen Workflows wurden zu einem path-gefilterten `Project Assurance`-Workflow konsolidiert. Er führt Requirements-, Assurance- und Operational-Core-Regressionen sowie beide bestehenden Validator-Commands in einem Lauf aus.

Die Map ist absichtlich inkrementell: implementierte #62/#63-Teile sowie konkret geplante #54/#55/#57/#61-Anschlüsse sind sichtbar. Fehlende Mappings bedeuten nicht, dass ein Requirement entfällt oder keine fachliche Prüfung benötigt.

### Authority-Grenze

`deterministic` bezeichnet nur formal etablierte Regeln. `mixed`, `procedural` und `scholarly` erzwingen in der Map eine explizite Review-Grenze; der Validator entscheidet weder historische Wahrheit noch Methodensuffizienz, Quellenlesung, Specialist Agreement oder Owner-Akzeptanz.

### Prior-Art-Disposition

Der Schnitt **fused** die in Histo-Orla bereits vorhandenen #62/#63-Mechanismen statt neue parallele Tools anzuhängen. Aus `paleo-type` wurden canonical-vs-derived, executable settled invariants und Mutation-Authority-Trennung übernommen; aus `Wissensarbeit` die Capability-Sicht und `deterministic | procedural | judgement`-Grenze adaptiert. Ein generisches Framework, Workflow-Engine oder fremdes Domainmodell wurde verworfen/deferred, weil Histo-Orla Requirements und reale Nutzung dafür keinen Bedarf begründen.

## 17. Empfohlene Reihenfolge

### Schritt A – abgeschlossen: Integrationssicht statt weiterer Einzelskripte

1. Requirement→Enforcement Map als technische Projektion definieren;
2. aktuelle #62/#63 Rule-IDs und Fixtures darin erfassen;
3. #54/#55/#57/#61 als `planned/partial` sichtbar machen;
4. keine neue fachliche Semantik erfinden.

### Schritt B – Grundbaustein abgeschlossen, weitere Extraktion nur bei Bedarf

Loader und Schema-Mechanik sind gemeinsam extrahiert; #62/#63 bleiben Wrapper. Findings-/fachspezifische Parsing-/Rule-Logik bleibt zunächst bewusst bei ihren Ownern. Weitere Extraktion oder ein `validate all`-Entry-Point erfolgt erst bei einem realen dritten Capability-Bedarf.

### Schritt C – erster neuer Read-only Nutzen

Bevor Mutation Automation entsteht:

- `context` oder `derive audit` als read-only Capability;
- reale #46/#60/#48-Handoffs als Fixture;
- Nutzen/Bürokratie über Owner-Feedback prüfen.

### Schritt D – Evidence und Transition nur nach realer Semantik

- `evidence` nach #49/#57;
- `transition` nach #54 + realen Canonical-State-Objekten;
- keine universelle State Machine.

### Schritt E – Skills zuletzt

Skills rufen Core/Context auf; keine duplizierten Regeltexte.

## 17. Falsifikationskriterien

Die Integrationsrichtung ist falsch oder zu groß, wenn:

- das gemeinsame Core-Paket mehr Boilerplate erzeugt als es Duplikation entfernt;
- ein neuer Research-Schritt erst Infrastrukturarbeit verlangt, obwohl kein Qualitäts-/Restartability-Gap besteht;
- Requirement→Enforcement zur zweiten Requirement Truth wird;
- Context Generation große Methodikblöcke dupliziert;
- Transition Code fachliche Interpretation entscheidet;
- Skills ohne Core genauso viel Regelwissen wiederholen müssen wie heute;
- Derived Views manuell nachkorrigiert werden müssen und dadurch wieder Truth Stores werden;
- CI-/Assurance-Komplexität mehr operative Störung als nachweisbare Fehlervermeidung erzeugt.

## 18. Architekturentscheidung / Status

Diese Analyse **entscheidet noch keinen konkreten Paketnamen, keine Datenbank, keinen Workflow-Engine-Stack und keine Agentenarchitektur**.

Sie stellt jedoch einen hinreichend belegten Integrationsbefund fest:

> **Vor weiteren unabhängigen Assurance-/Context-/Evidence-/Transition-Skripten soll Histo-Orla die bereits vorhandenen #62/#63-Mechanismen durch eine Requirement→Enforcement-Sicht und einen kleinen gemeinsamen Operational Core zusammenführen.**

Das ist eine evolutionäre Refactoring-/Integration-Richtung unter #48. Konkrete schwer reversible Entscheidungen bleiben #58/#44 vorbehalten.
