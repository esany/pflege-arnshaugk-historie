# Histo-Orla – Audit: Chat-/KI-Unabhängigkeit, Work-Context-Scope und Domain↔Dev-Handoff

**Status:** `governance-analysis / recommendation / owner-admission-pending-for-binding-change`  
**Stand:** 2026-08-31  
**Governance Owner:** #9  
**Issue-/Ownership-Schnittstelle:** #23  
**Research Quality:** #45  
**Architecture/Dev-Schnittstelle:** #48–#59  
**Prior-Art-Challenge:** `esany/paleo-type`, insbesondere aktueller `AGENTS.md`, #71–#79 und `requirements/ai-role-handoff-engineering-analysis.md`

## 1. Anlass

Nach Einführung von Root-`AGENTS.md`, `PROJECT_STATE.md` und projektweitem ChatGPT-Bootstrap ist zu prüfen, ob Histo-Orla nicht nur **Chat-State-Unabhängigkeit**, sondern auch **Model-/Prozess-/Rollen-Unabhängigkeit** hinreichend sicherstellt.

Leitfragen:

1. Ist der aktuell laufende historische Forschungsauftrag aus dem Repository ohne Chat rekonstruierbar?
2. Wie flächendeckend ist `Chat ist Werkstatt; GitHub ist Projektgedächtnis` bereits operationalisiert?
3. Braucht jeder substantielle Chat/Work Context zusätzlich einen expliziten initialen Scope?
4. Wie müssen Domain Research, Domain Review/Requirements und Architecture/Development getrennt werden, damit technische Convenience keine Fachsemantik erzeugt?
5. Welche aktuellen `paleo-type`-Muster sind generalisierbares Prior Art, ohne dessen konkrete Architektur unkritisch zu kopieren?

## 2. Aktueller Live-Research-State: explizite Fragestellung ist sichtbar

Der aktuell aktive U2-Work-Owner bleibt #46. Seit dem letzten `PROJECT_STATE.md`-Snapshot wurde sein Forschungsrahmen materiell geschärft.

### 2.1 Aktuelle Makrofrage

Kanonisch im neuen Zeitscheiben-/Herrschaftsnetz-Artefakt und in #46 dokumentiert:

> **Wie verändern sich soziale, kirchliche, dynastische, grundherrliche und administrative Organisation des Orla-Grenzraums zwischen ca. 1200 und 1400, welche älteren Rechte und Netzwerke überleben diese Veränderungen, und wie werden Boden, Wege, Kirchen, Abgaben, Wasser und Menschen in diesen Strukturen verfügbar gemacht oder geschützt?**

Kurzform im #46-Checkpoint:

> **Wie verändert sich die soziale, kirchliche, dynastische und administrative Organisation des Orla-Grenzraums zwischen ca. 1200 und 1400, und welche älteren Rechte/Netzwerke überleben die Territorialisierung?**

Kanonisches Artefakt:

`docs/research/cases/u2-orlagau-zeitscheiben-herrschaftsnetz.md`

### 2.2 Aktueller methodischer Pilot

Parallel wird Triptis 1212 / `nimia paupertas` als realer Methodentest genutzt.

Dabei ist strikt getrennt:

- quellenexplizit: erhebliche Armut als genannte Begründung der Verlegung;
- beobachtbare institutionelle/ökonomische/soziale Konstellation;
- mögliche Ursachen als **konkurrierende Hypothesen**, die je eigene Evidenzpfade benötigen.

Kanonische methodische Vertiefungen:

- `docs/research/cases/u2-transdisziplinaere-rekonstruktionsmatrix.md`
- `docs/research/cases/u2-quellenzentrierte-erschliessung-sota.md` bzw. der im Commit `24bbe67` angelegte SOTA-/Best-Practice-Artefaktpfad des U2-Workstreams.

Der neue Arbeitsgrundsatz lautet sinngemäß:

```text
source-local first
→ quellennahe Beobachtung
→ research hooks / Evidence Demand
→ begründete Scope-Erweiterung
→ disziplinspezifische Evidenzpfade
→ Cross-Evidence-Abgleich
→ konkurrierende Erklärungen
→ Synthese
```

Damit ist die laufende explizite Fragestellung **repo-seitig vorhanden und rekonstruierbar**. Sie ist jedoch im aktuellen Root-`PROJECT_STATE.md` noch nicht ausreichend sichtbar; der Handoff-Snapshot ist gegenüber den jüngsten #46-Commits nachgezogen werden müssen.

## 3. Bewertung des Anti-Wissensmonopol-Musters in Histo-Orla

### 3.1 Normative Abdeckung: stark

Projektweit bestehen inzwischen mehrere redundanzarme, sich ergänzende Schutzschichten:

1. ChatGPT-Projektinstruktion erzwingt frischen GitHub-Bootstrap.
2. Root-`AGENTS.md` verbietet continuation-critical State ausschließlich in Chat/Modell/Scratchpad.
3. `PROJECT_STATE.md` ist phasenübergreifende Handoff-/Navigationssicht.
4. Issues besitzen Work Ownership; substantielle Inhalte gehören in versionierte Artefakte.
5. #45 verlangt für Research Frage, Scope, führende Domänen, Evidenz, Search Boundaries und Persistenz.
6. `docs/research/source-identity-protocol.md` verhindert Quellen-/Instanz-/Fundstellenverlust.
7. #42/#43/#48ff verhindern, dass Dev/Architektur still Requirements oder Fachsemantik übernimmt.
8. Handoff Gate in `AGENTS.md` verlangt Fortsetzbarkeit ohne Chat.

**Bewertung:** Normativ ist das Muster repo-weit bereits stark und nicht nur auf einen einzelnen Chat beschränkt.

### 3.2 Empirische Umsetzung: im U2-Live-Chat sehr stark, projektweit nicht vollständig beobachtbar

Die jüngsten U2-Commits zeigen reale Compliance:

- methodische Korrekturen wurden versioniert statt nur diskutiert;
- neue Makrofrage und neue Arbeitsmodelle wurden in #46 + Artefakten persistiert;
- frühere zu enge Interpretationen wurden explizit korrigiert;
- Findings, Unresolved States, Search Boundaries und nächste Aktionen bleiben sichtbar;
- Requirement Candidates RC-U2-09…18 werden nicht automatisch zu Requirements promoted.

Damit ist der aktive Research-Chat **praktisch restartbar**.

Eine Aussage `alle Chats halten dies vollständig ein` ist hingegen nicht aus dem Repository beweisbar: GitHub zeigt persistierte Ergebnisse, aber keine vollständige Telemetrie aller Chatläufe. Deshalb gilt:

- **normative Flächendeckung:** hoch;
- **beobachtete Compliance:** für U2 und die jüngsten Governance-/Architecture-Workstreams gut;
- **vollständige Runtime-Garantie über jeden einzelnen Chat:** nicht nachweisbar.

## 4. Noch offene Lücke: Chat-State-Unabhängigkeit ist nicht dasselbe wie Rollen-/Prozess-Unabhängigkeit

Ein neuer Chat kann heute korrekt `AGENTS.md`, `PROJECT_STATE.md` und den Work Owner lesen und trotzdem unterschiedlich rekonstruieren:

- welche **primäre Funktion** er gerade erfüllt;
- wie eng oder breit sein Task-Scope ist;
- welche Fachdomänen führend bzw. kontrollierend sind;
- was er selbst entscheiden darf;
- wann er an Domain Review, Dev, Owner oder unabhängigen Spezialisten übergeben muss;
- ob eine technische Folge schon Requirement ist oder nur Research Candidate;
- welche Kontextinformation absichtlich noch **nicht** geladen werden darf, wenn sie eine unabhängige Quellenlektüre kontaminieren würde.

Das ist keine Wissensmonopol-Lücke im engeren Sinn, sondern eine **Model-/Process-Dependency- und Authority-Drift-Lücke**.

## 5. Relevantes aktuelles Prior Art aus `paleo-type`

`paleo-type` unterscheidet inzwischen ausdrücklich drei Probleme:

1. **Chat/state dependency** – Chat darf nicht alleiniger State Owner sein.
2. **Model/process dependency** – ein neuer Lauf kann trotz vollständigem State Rolle, Kontext, Authority oder Handoff anders rekonstruieren.
3. **Scholarly judgement variability** – unterschiedliche evidenzgebundene fachliche Urteile dürfen legitim bestehen bleiben und sollen nicht softwareseitig erzwungen vereinheitlicht werden.

Daraus folgt dort nicht ein Multi-Agent-System, sondern ein **replaceable work-context model**:

```text
canonical governing context + canonical project/source state
→ explicit bounded role/function
→ role-appropriate work
→ explicit handoff at authority/competence boundary
→ receiving role + review/return condition
→ canonical persistence / NEXT ACTION
```

Leitprinzip:

> **Standardize the path, not the scholarly outcome.**

Die zentrale generalisierbare Einsicht für Histo-Orla lautet deshalb:

> Nicht jedes Modell muss dasselbe historische Urteil produzieren. Es muss aber aus demselben kanonischen State zuverlässig rekonstruieren können, **welche Funktion es gerade erfüllt, welche Evidenz gilt, was es entscheiden darf, wann es stoppen/handoffen muss und wo das Ergebnis kanonisch zurückgeschrieben wird.**

### 5.1 Reale Falsifikation in `paleo-type`

Das Muster ist dort nicht nur Planungsprosa. Der aktuelle G2-Zyklus wurde bereits als gerichteter Rollenwechsel ausgeführt:

```text
Source Research / Checkpoint-B evidence
→ persistiertes Semantic-Loss-Artefakt
→ Domain Review
→ Klassifikation source-local / project / existing generic requirement / deterministic-system candidate / specialist need
→ keine automatische Implementation
```

Der Domain Review dokumentiert ausdrücklich seine Nicht-Autoritäten und verwendet vorhandene Requirements statt aus einem schwierigen Einzelbefund spontan neue Architektur zu erzeugen.

## 6. Braucht jeder Chat initial einen Scope?

### Empfehlung: jeder **substantielle Work Context** braucht einen minimalen, aus dem Repository abgeleiteten Scope – aber nicht jeder Chat ein neues Issue/Formular/Promptpaket.

Für Research ist dies in #45 teilweise bereits bindend:

```text
precise question
scope / exclusions
leading disciplines
source/evidence classes
search vocabulary
intended decision/capability consequence
```

Was noch fehlt, ist eine **generische Work-Context-Schicht**, die auch Domain Review, Architecture, Dev und Governance abdeckt.

Empfohlener minimaler Start-/Resume-Contract:

```text
PRIMARY FUNCTION
CURRENT CANONICAL TASK / WORK OWNER
PURPOSE / BOUNDED QUESTION OR TASK
SCOPE / EXCLUSIONS
LEADING DOMAINS / REQUIRED COMPETENCIES
REQUIRED CANONICAL CONTEXT + EVIDENCE
MAY DECIDE / DO
MUST NOT DECIDE / DO
STOP / HANDOFF WHEN
COMPLETION / RETURN CONDITION
CANONICAL PERSISTENCE TARGET
```

Dieser Contract soll **automatisch aus Task + Repo-State abgeleitet** werden. Der Nutzer soll kein Formular ausfüllen und keine Routine-Rollenentscheidung treffen müssen.

### Nicht erforderlich

- nicht jeder triviale Orientierungschat braucht Zeremonie;
- nicht jede Fachdisziplin braucht einen eigenen Chat;
- nicht jede Kompetenz braucht eine eigene Agentenrolle;
- kein Prompt-Registry, Workflow-Engine oder Multi-Agent-Runtime;
- kein per-chat kanonischer Wahrheitsspeicher.

Eine Sitzung kann mehrere Fachkompetenzen aktivieren. Entscheidend ist **eine primäre Authority-/Work-Funktion zu einem Zeitpunkt**. Wechselt die Authority-Grenze materiell, erfolgt ein expliziter Handoff oder ein klar dokumentierter Rollenwechsel.

## 7. Empfohlene Work-Context-Funktionen für Histo-Orla

Nicht als Agentenklassen, sondern als Verantwortungs-/Arbeitskontexte:

### A. Domain / Source Research

Zweck:
- direkte Quellen-/Literatur-/Materialarbeit nach führender Fachdomäne;
- Working Findings, Uncertainty, Evidence Demand, Hypothesen und Requirement Candidates erzeugen.

Darf nicht:
- aus technischem Komfort Architektur festlegen;
- einen Einzelbefund selbst zum generischen Requirement machen;
- AI-Arbeit als unabhängige Fachvalidierung bezeichnen.

### B. Cross-disciplinary Domain Review / Scholarly Sequencing

Zweck:
- Findings fachübergreifend klassifizieren;
- nächsten wissenschaftlich zulässigen Schritt bestimmen;
- source-local vs. project-specific vs. generalisierbar unterscheiden;
- vorhandene Requirements anwenden bzw. echte neue Requirement Candidates begründen;
- entscheiden, ob überhaupt ein technischer/systemischer Gap vorliegt.

Diese Funktion ähnelt Teilen des heutigen Research Coordinator / Expertise Routing, darf aber **keine epistemische Oberinstanz** werden.

### C. Architecture / Development / Research Software & AI Systems Engineering

Zweck:
- einen bereits begründeten, bounded technischen Auftrag implementieren oder durch Spike/Benchmark diskriminieren;
- kleinste hinreichende Lösung wählen;
- deterministische Invarianten dort maschinenprüfbar machen, wo Semantik bereits geklärt ist.

Muss als Input kennen:

```text
demonstrated problem / evidence fixture
applicable accepted requirement / owner constraint
canonical information owner
minimum scholarly meaning/information to preserve
deterministic vs epistemic boundary
non-goals
migration/reversibility/loss constraints
technical acceptance tests
scholarly return/adequacy criteria
```

Darf nicht:
- fehlende Fachsemantik durch technische Annahmen ersetzen;
- ungelöste historische Urteile determinisieren;
- `Tests grün` mit wissenschaftlicher Akzeptanz gleichsetzen;
- neuen Stack/Schema/Owner nur aus Convenience einführen.

### D. Human Owner / Governance

Nur für nicht ableitbare normative Entscheidungen:
- Forschungszweck/Prioritäten;
- Rechte-/Zugangs-Fakten, die nur Owner klären kann;
- materielle Systemänderung/Lock-in/Kosten/Privacy;
- folgenschwere Publikations-/Nutzungsentscheidung.

Nicht für Routine-Engineering oder Spezialistenurteile.

### E. Qualified Independent Specialist Review

Kein normaler Chat-Status, sondern Validierungs-/Handoff-Endpunkt bei entsprechendem Risiko/Fachstandard.

AI-assisted Domain Review bleibt davon getrennt.

## 8. Domain↔Dev-Handoff als zentrale Schutzgrenze

Histo-Orla hat bereits die Formel:

> **Dev informiert Requirements; Dev besitzt sie nicht.**

Für mehrere Chats sollte daraus ein operationaler Vertrag werden:

```text
Research evidence / observed failure
→ Domain Review / Generalisability Check
→ accepted requirement or bounded architecture question
→ explicit Dev handoff
→ implementation / deterministic verification
→ scholarly adequacy return review
→ research NEXT ACTION
```

Damit wird verhindert:

```text
Dev sees problem
→ chooses convenient model/schema
→ retrofits scholarly requirement
```

und zugleich vermieden, dass der Research Owner Routine-Implementation micromanagen muss.

## 9. Fresh-context evidence availability: wichtiger zusätzlicher Anti-Chat-Punkt

`paleo-type` hat jüngst eine weitere Restartability-Lücke empirisch gefunden:

```text
IDENTIFIABILITY
≠ REPRODUCIBILITY
≠ RESEARCH-READY AVAILABILITY
```

Eine Quelle kann korrekt identifiziert und ein Derivat reproduzierbar beschrieben sein, während ein neuer autorisierter Chat die tatsächlich benötigten Bytes/Bilder trotzdem nicht öffnen kann.

Für Histo-Orla ist das unmittelbar relevant zu #49 und dem Owner Constraint `OneDrive = Source of Bytes`.

Daraus folgt als Architecture-/Verification-Candidate, nicht als neue Technologieentscheidung:

> Wenn die aktuelle NEXT ACTION direkte Quelleninspektion benötigt, muss ein frischer autorisierter Work Context einen dokumentierten, zulässigen Zugriffspfad auf die tatsächlich benötigte Instanz besitzen. `known source` ist nicht automatisch `source accessible now`.

Das sollte in #49/#57 als Fresh-context-Restart-Test aufgenommen werden, bevor die Zotero/OneDrive-Integration als restartbar gilt.

## 10. Aktueller Handoff-Failure-Test: `PROJECT_STATE.md` ist bereits veraltet

Die Einführung von `PROJECT_STATE.md` war richtig, aber die jüngsten U2-Commits zeigen eine reale Schwachstelle:

- Snapshot enthält #46 als aktiven Live Case;
- er enthält noch nicht die neue Makrofrage;
- er enthält noch nicht die neuen methodischen U2-Artefakte / Evidence-Demand-/Situations-Dossier-Schärfung.

Damit gilt aktuell:

```text
Bootstrap-Regel korrekt
+ Work Owner korrekt
+ kanonische Artefakte korrekt
- zentrale Handoff-Sicht nicht vollständig frisch
```

Das System bleibt rekonstruierbar, weil der Bootstrap das Work-Owner-Issue verlangt. Die zusätzliche `PROJECT_STATE`-Orientierung ist aber schwächer als vorgesehen.

Empfohlener Trigger:

`PROJECT_STATE.md` muss spätestens vor Abschluss eines substantiellen Chats aktualisiert werden, wenn mindestens eines materiell geändert wurde:

- aktive Leit-/Makrofrage;
- Work-Owner-Scope;
- Phase/Gate;
- kritische Dependency/Blocker;
- nächster ausführbarer Hauptschritt;
- neuer cross-cutting Constraint;
- Architecture/Requirement-Status.

Nicht jedes neue Finding gehört dort hinein.

## 11. Gesamtbewertung

| Dimension | Stand Histo-Orla | Bewertung |
|---|---|---|
| Chat darf nicht Wahrheitsspeicher sein | Projektprompt + AGENTS + Issues + Artefakte | **stark** |
| Fresh repo bootstrap | projektweit verpflichtend | **stark** |
| One fact / one canonical home | explizit | **stark** |
| Research Scope vor Recherche | #45 explizit | **stark für Research** |
| Persistenz realer U2-Fortschritte | jüngste Commits zeigen konsequente Nutzung | **stark** |
| Neue Session kennt aktuelle Leitfrage sofort aus Top-Level-Handoff | `PROJECT_STATE` hinter #46 | **mittel / nachzuziehen** |
| Chat weiß seine konkrete Rolle/Authority | nicht generisch operationalisiert | **mittel** |
| Domain↔Dev-Handoff | konzeptionell stark, aber kein generischer Work-Context-Contract | **mittel-gut** |
| Fresh-context Source-Byte-Verfügbarkeit | durch OneDrive-Zielbild geplant, noch nicht empirisch verifiziert | **offen** |
| Modellunabhängige Prozessgrenzen | implizit, paleo-type weiter | **mittel** |
| Unabhängige Fachvalidierung ≠ AI Review | explizit | **stark** |

## 12. Empfehlung / Owner-Decision

Ich empfehle, **nicht** weitere Agenten-/Rollenarchitektur einzuführen.

Stattdessen sollte Histo-Orla nach Owner-Admit den Root-`AGENTS.md` um einen kurzen verpflichtenden **Work Context Bootstrap** ergänzen:

1. jeder substantielle Chat identifiziert seine primäre Funktion;
2. Current Task/Work Owner + bounded Scope werden aus Repo-State bestimmt;
3. führende Domänen/Kompetenzen und erforderliche Evidenz werden geladen;
4. `MAY / MUST NOT / STOP-HANDOFF / RETURN` werden proportional zum Task explizit;
5. keine neue Wahrheit entsteht im Chat;
6. Rollenwechsel/Handoff ist nur bei echter Authority-/Competence-Grenze nötig;
7. Dev erhält Fachsemantik/Requirements als Handoff, erfindet sie nicht;
8. aktueller Source-Zugriff wird bei source-inspection tasks als Fresh-context-Voraussetzung geprüft.

Das ist eine **materielle repo-weite Governance-Schärfung**. Dieses Audit empfiehlt sie, nimmt sie aber nicht autonom vor. Eine bindende Änderung an `AGENTS.md` sollte als Owner-Decision/Admission sichtbar erfolgen.

## 13. Falsifikation / Akzeptanz

Die vorgeschlagene Schicht ist nur dann sinnvoll, wenn reale Chats davon profitieren. Sie scheitert, wenn:

- jeder Chat in Formularzeremonie endet;
- bereits aus Work Owner ableitbare Information redundant dupliziert wird;
- Source Research langsamer wird, ohne Authority-Drift zu verhindern;
- jede Kompetenz zu einer eigenen Rolle/Chatinstanz wird;
- Templates zur zweiten Wahrheit werden;
- Dev trotz Handoff weiterhin Fachrequirements neu interpretieren muss;
- ein frischer Chat weiterhin alten Gesprächskontext benötigt.

Erfolgskriterium:

> Ein kompetenter neuer Chat kann nach Repo-Bootstrap **ohne alten Chat** in wenigen Schritten sagen: `Was ist meine Aufgabe? Welche Fach-/Authority-Grenze gilt? Welche Evidenz brauche ich? Was darf ich verändern? Wann muss ich handoffen? Wo persistiere ich? Was ist mein Completion/Return Condition?` – und anschließend korrekt arbeiten.
