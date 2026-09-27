# Histo-Orla – AI-orchestrierte Skill-Integration: Readiness- und Assurance-Plan

**Stand:** 2026-09-27  
**Status:** `planning / reconciliation / readiness-candidate / no-implementation-authority`  
**Work Owner:** #48 Technical Lead  
**Development / Verification:** #59  
**Work Context / Handoff:** #61  
**Requirements:** #42  
**Value / Decision / Delivery Trace:** #63  
**Owner-Decision-Eskalation:** #44 nur für echte verbleibende materielle Entscheidungen/Blocker  
**Histo-Basis:** `main@00891652761d479cc98d0752ea8d11a2ac61dcc3`  
**Wissensarbeit-Basis:** `main@9b16601c3550bde37ed4410eec3cec3bd6aa6846`  
**Real-Skill-Pilotbasis:** `esany/Wissensarbeit` PR #51, frozen reviewed head `f3726c962807b311e8a2a7df63f738e11790fbed`  

> Dieses Artefakt zieht die konzeptionellen Befunde zu Zuverlässigkeit, Authority, AI-Orchestrierung, Ressourcenökonomie und Cross-Repository-Skills zusammen und leitet daraus die kleinste problem-schließende Implementierungsplanung ab. Es ist **keine Implementation Admission**, keine Requirement-Promotion und keine Produkt-Multi-Agent-Architektur.

---

## 1. Ausgangslage und Authority dieses Plans

Der Owner hat für diesen Arbeitskontext ausdrücklich autorisiert:

- aktuelle Repository-Zustände frisch zu lesen und zu reconciliieren;
- konzeptionelle Befunde systematisch zusammenzuführen;
- offene Fragen, Blocker, Unsicherheiten, Hazards und Dependencies vor Implementierung zu klären;
- die Planung und notwendige Vorarbeiten transparent und versioniert im Repository zu sichern;
- implementation-ready Work Packages, Tests und Work-Order-Kandidaten vorzubereiten.

Nicht autorisiert sind:

- Implementierung;
- automatische Implementation Admission;
- automatische Research Selection;
- Requirement-/Method-Promotion;
- Merge nach `main`;
- Ableitung weiterer Authority aus einem grünen Planungs-/CI-Status.

Ziel ist `READY FOR OWNER ADMISSION`; bis alle Readiness-Gates erfüllt sind bleibt der Status darunter.

---

# 2. Rekonstruiertes Owner-Problem und Motivation

## 2.1 Primäres Problem

Histo-Orla soll anspruchsvolle Forschungs-/Entwicklungsarbeit zunehmend selbständig, zuverlässig, restartbar und ressourceneffizient durchführen können. Der Owner soll Ziel, Bedeutung, Priorität, Risiko und materielle Akzeptanz besitzen, aber **nicht** zum manuellen Workflow-Operator, Prompt Engineer oder Agenten-Kurier werden.

Gleichzeitig ist real wiederholt beobachtet worden, dass KI aus einem legitimen Analyseauftrag durch plausible Scope-/Abstraktions-Erweiterung eine Lösung, ein Projektartefakt oder eine Repository-Mutation ableitet, ohne dass dieser nächste Authority-Schritt tatsächlich autorisiert war.

Das zentrale Failure Pattern lautet:

```text
Owner-Frage / Analyseauftrag
→ plausible Interpretation
→ Abstraktions-/Scope-Erweiterung
→ Lösungskonzept
→ vermeintlicher Projektkandidat
→ persistente Mutation / Folgephase
```

Reale Histo-Evidence dafür liegt mindestens in:

- `docs/architecture/assurance/chat-operationalization-self-audit-20260920.md`;
- `docs/research/discovery/chat-audit-quellenerschliessung-kompetenz-intent-20260927.md`;
- `docs/architecture/assurance/ai-resilience-root-cause-audit.md`;
- dem unautorisiert angelegten #48-Kommentar `5856746930`, der hier nur als Failure-/Provenienz-Evidence gilt, nicht als Owner-Entscheidung.

## 2.2 Gegenproblem: keine Human-as-Workflow-Engine-Lösung

Eine pauschale Gegenregel „vor jedem Schritt nachfragen“ würde einen anderen bereits evidenzierten Pain verschärfen:

- Owner-Metaarbeit;
- Chat-Orchestrierung;
- wiederholtes Kontext-Copying;
- triviale technische Entscheidungen beim Owner;
- Ressourcenverlust durch unnötige Handoffs.

Histo-Orla erlaubt #48 reversible technische Entscheidungen innerhalb accepted Requirements/Constraints. Wissensarbeit priorisiert ebenfalls Automation operativer Notwendigkeit und menschliche Gates nur an materiellen Grenzen.

Gesucht ist deshalb **nicht weniger Initiative**, sondern sauber gebundene Initiative.

## 2.3 Owner Constraint dieses Arbeitskontexts

Für die weitere Planung gilt als expliziter Owner-Input:

> **User GO, Assistant Initiative.** Die KI erkennt selbständig Persistenz-, Kompetenz-, Routing- und Orchestrierungsbedarf. Persistente/externe Mutation und materielle Folgephasen müssen jedoch durch einen sichtbar gebundenen Owner-GO bzw. eine bereits gültige Admission getragen sein. Authority kaskadiert nicht still in Nachfolgeschritte.

Dieser Plan behandelt das als **Owner Constraint / Planning Driver**, nicht automatisch als neues accepted Requirement. Eine spätere repo-weite Governance-/Requirement-Promotion bleibt getrennt zu dispositionieren.

## 2.4 Problem Closure Contract

Die kleinste hinreichende Lösung ist **nicht** die technisch trivialste Teilfunktion. Sie muss einen realen problem-schließenden Umfang liefern.

### Originalproblem

Histo-Orla soll relevante, sich entwickelnde externe Skill-/Kompetenzpakete dauerhaft und aktuell nutzbar machen können und deren Nutzung AI-seitig orchestrieren, ohne:

- fremde Repository-Semantik zur Histo-Orla-Authority zu machen;
- den Owner zum Chat-/Agenten-Orchestrator zu machen;
- blind neuestes Upstream zu übernehmen;
- Review-/Maturity-/Authority-Status zu verlieren;
- Histo Requirements/Method Truth zu duplizieren;
- bei inkompatibler Upstream-Evolution einen funktionierenden lokalen Stand zu verlieren;
- eine neue Workflow-/Agentenplattform auf Vorrat zu bauen;
- unautorisierte persistente/externe Folgeaktionen aus Analyse oder Plausibilität abzuleiten.

### Problem-schließender Zielzustand

Ein frischer kompetenter AI-Orchestrator kann aus dem Repository:

1. einen konkreten externen Skill eindeutig identifizieren;
2. den **aktuellen Upstream-Zustand bei Nutzung** frisch bestimmen;
3. Upstream Work Owner, Maturity/Review-Status und exakten Ref erhalten;
4. einen lokal bereits geprüften/zugelassenen Ref von „latest observed“ unterscheiden;
5. Änderungen ohne stilles Upgrade erkennen;
6. kompatible / semantisch geänderte / inkompatible Zustände unterscheiden bzw. bei nicht sicherer Entscheidung fail-closed bleiben;
7. bei Inkompatibilität den letzten lokal zugelassenen Stand weiter referenzieren und eine lokale Derivation nur mit expliziter Lineage planen;
8. einen bounded Work Context für den tatsächlichen Consumer erzeugen;
9. die Arbeit AI-seitig nach Kompetenz/Qualitätsbedarf orchestrieren, ohne Owner-Metaarbeit;
10. vor nicht bereits gebundener persistenter/externer Mutation oder materieller Folgephase stoppen bzw. ein sichtbares GO/Admission-Gate nutzen;
11. aus Repo-State restartbar sein, ohne Chatgedächtnis;
12. nach Real-Use nachweisen, ob der Skill das konkrete Histo-Problem wirklich schließt.

Erst wenn dieser End-to-End-Zustand für einen realen Skill-Pilot demonstriert ist, ist der Problem-Slice geschlossen. Ein Manifest allein, ein Pin allein, ein Agent allein oder ein grüner Validator allein genügt nicht.

---

# 3. Source-Role Ledger

| ID | Aussage / Input | Source Role | Status in diesem Plan |
|---|---|---|---|
| SR-01 | Verlässlichkeit/Transparenz, Unsicherheit zulassen, bei echter Ambiguität fragen | Owner statement | bindender Planning Driver |
| SR-02 | AI soll Persistenz-/Orchestrierungsbedarf selbst erkennen; GO bleibt beim Owner | Owner statement | bindender Planning Driver; keine automatische #42-Promotion |
| SR-03 | kritische Zustände sollen nie entstehen; Planung trägt besondere Präventionsverantwortung | Owner statement | bindender Planning-/Safety-Constraint |
| SR-04 | „kleinste Lösung“ = kleinster Umfang, der Problem/Erkenntnislücke schließt | Owner statement | bindende Lean-Auslegung für diesen Plan |
| SR-05 | unautorisierte #48 Skill-Source-Binding-Notiz | AI-produced repository artifact | Failure Evidence + Candidate Prior Art, keine Owner-Authority |
| SR-06 | #70: delegated Git credential != Human Authority; Safe-Mutation/Admission-Gaps | canonical audit evidence | starkes bestehendes Schutzgut / Delivery-Evidence |
| SR-07 | Sep-20/Sep-27 Self-Audits: zu schnelle Abstraktion/Persistenz, Task-Layer-Fehler | canonical audit evidence | wiederholtes Real-Use-Failure Pattern |
| SR-08 | Wissensarbeit #55 GO-01..GO-10 | external prior-art candidate, reviewed spec evidence | starke Challenge-/Reuse-Evidence; keine Histo-Authority |
| SR-09 | Wissensarbeit #52 Skill organism | external candidate prior art | Composition/anti-proliferation input only |
| SR-10 | Wissensarbeit #54 standalone Skill falsifiziert/geschlossen | external trial evidence | Gegenbeleg gegen Skill-/Agent-Proliferation |
| SR-11 | PR #51 frozen reviewed Skill head | external concrete integration target | realer Pilot, nicht Generic Fit / nicht merged |
| SR-12 | Work/Workspace-Agent/Codex-Fähigkeiten 2026-09 | current product capability evidence | Runtime-Option, bei Ausführung frisch revalidieren; keine Requirement-Semantik |

---

# 4. Concept / Evidence / Authority Reconciliation

| ID | Befund | Aktueller Owner/Mechanismus | Coverage | Disposition | Planungsfolge |
|---|---|---|---|---|---|
| R-01 | Repo muss aus fresh state arbeiten | AGENTS / #61 | covered | confirm | jeder Run revalidiert Basis-SHAs/Refs |
| R-02 | Credential/Connectorzugriff ist keine Authority | #70 B3/B1, #48/#59 | partial | strengthen | Interaction-/Admission-Bindung vor consequential mutation explizit machen |
| R-03 | Work Context besitzt Scope/MAY/MUST NOT/STOP/Persistence | AGENTS/#61, bounded Execution Contract | partial | reuse/refine | keinen neuen Agenten-State erfinden; bestehende Work-Order-Semantik erweitern, falls nötig |
| R-04 | Mutation Guard verhindert destructive/no-op local writes, entscheidet aber keine Authority | `tools/operational/mutation.py` | partial | retain | mechanische Write Safety und Authority getrennt behandeln |
| R-05 | Direct Connector/Contents writes umgehen local Mutation Guard | #70 closure / PROJECT_STATE | genuine delivery gap | retain | Branch/PR; keine Aussage, Repo-Guard decke Plattformaktionen ab |
| R-06 | Owner-GO muss sichtbar gebunden sein und darf nicht kaskadieren | Owner Constraint + Wissensarbeit #55 prior art | partial | refine into Histo execution contract candidate | genau-ein Work Package / no downstream authority |
| R-07 | Owner darf nicht zum Workflow-/Agenten-Orchestrator werden | Owner Input + Histo Owner-Pain + Wissensarbeit GO/BBs | partial | strengthen | Orchestrierung ist AI-Verantwortung, Execution Surface capability-first |
| R-08 | Skills sind bounded Operatoren, keine Truth Stores/Authority | Histo operational architecture + Wissensarbeit #52 | covered conceptually | confirm | Skill/adapter bleibt dünn; Histo Semantik lokal |
| R-09 | Skill-Lifecycle ist organisch; Candidate kann schrumpfen/sterben | Wissensarbeit #54 trial | external evidence | adopt as challenge | keine automatische Registry-/Skill-Proliferation |
| R-10 | „latest“ ist semantisch nicht identisch mit `main`/neuester Commit | PR #51/#46 real state | genuine integration requirement/constraint candidate | retain | source binding muss Ref + Owner + Maturity erhalten |
| R-11 | Ressourcen sparen darf Qualität/Context Fidelity nicht senken | Histo capability-first + Wissensarbeit #48 | covered conceptually | confirm | routing nach Qualitätsäquivalenz, nicht Task-Label/Preis allein |
| R-12 | Planung muss kritische Zustände präventiv verhindern | Owner Constraint + historische #119-Replanung | partial | strengthen | Hazard/Precondition/Test/Recovery vor Implementierung |
| R-13 | Lean darf Problemraum nicht trivial verkürzen | #42/#48/README + Owner-Präzisierung | covered principle, new explicit closure test | refine | Problem Closure Contract wird Slice-Gate |
| R-14 | „Learning dokumentiert“ != Enforcement/Real-Use-Verhalten | #70 / Wissensarbeit Learning Assurance | covered conceptually | confirm | Readiness-Maturity streng staffeln |
| R-15 | AI-Orchestrierung ist Execution-Methode, nicht Product Multi-Agent Architecture | #61 / bounded Execution Contract | covered | confirm | kein Product-Agent-Framework ohne separaten Need |

### Ergebnis

Es gibt **keinen bestätigten Bedarf für eine neue allgemeine Workflow-/Agent-/Authority-Plattform**.

Die problem-schließende Planung soll vorhandene Mechanismen zusammensetzen und nur dort minimal erweitern, wo der reale Pilot eine Lücke nachweist.

---

# 5. Requirements-/Constraint-Coverage

Die aktuelle Analyse bestätigt **noch keinen neuen #42-Requirement-Gap**.

Relevante bestehende Basis:

- `REQ-WF-001` – settled invariants technisch erzwingen, wo möglich;
- `REQ-WF-002` – reproducible/restartable workflow;
- `REQ-STATE-001` – portability/restartability/current state;
- `REQ-EPI-004` – Unsicherheit/Korrektur/`unresolved`;
- `REQ-EPI-005` – AI output ist keine Evidence/independent validation;
- `REQ-UX-001/002/003` – Auditierbarkeit, Human control, progressive disclosure;
- `REQ-TRACE-001` – G/N/P → Requirement → Decision → Delivery → Feedback;
- `REQ-LEAN-001` – technische Subsidiarität/kleinste hinreichende Lösung;
- bindende Governance aus `AGENTS.md`;
- explizite Owner Constraints dieses Arbeitskontexts.

### Noch offene Lifecycle-Frage

Ob `User GO / no cascade` repo-weit künftig als:

1. Governance-Präzisierung unter #9,
2. Work-Context/Execution-Contract unter #61,
3. Requirement-Delta unter #42,
4. oder Kombination mit unterschiedlichen Rollen

kanonisch promoted werden soll, wird **nicht** durch diesen Plan entschieden. Für den bounded Pilot ist der explizite Owner Constraint als Driver hinreichend; die allgemeine Promotion ist ein separater Reconciliation-/Admission-Punkt.

---

# 6. Technical Derivation – kleinste problem-schließende Architektur

## 6.1 System Responsibilities

Der geplante Slice braucht nur vier Verantwortungen:

### SR-A — Bound Execution / Admission Context

Der ausführende Kontext muss erkennen können:

- welches Work Package autorisiert ist;
- welcher Scope/Mutationstyp erlaubt ist;
- wo die Authority endet;
- wann STOP/HANDOFF gilt;
- dass Folgepakete keine implizite Authority erben.

Diese Verantwortung erweitert/konkretisiert den bestehenden bounded Execution Contract; sie ist **kein neuer globaler Authority Service**.

### SR-B — External Skill Source Identity + Status

Eine kleine provider-neutrale Source-Binding-Repräsentation muss mindestens unterscheiden:

- upstream repository;
- upstream Work Owner / relevante PR-/Issue-Identität;
- tracking selector/ref;
- aktuell beobachteten exact ref;
- upstream maturity/review/status;
- lokal geprüften/zugelassenen consumer basis ref;
- local consumer / capability;
- compatibility state;
- lineage bei lokalem Derivat;
- review/evidence refs.

Sie speichert **keine kopierte Skill-Semantik** und ist keine zweite Requirement-/Method-/Skill Truth.

### SR-C — Freshness / Compatibility Gate

Vor materieller Skill-Nutzung:

```text
fresh upstream inspect
→ identity/status/maturity/ref compare
→ unchanged
   | changed-compatible-candidate
   | semantic/maturity-change
   | incompatible
   | unresolved
→ local disposition under Histo authority
```

Default ist **freshness on material use**, nicht permanente Polling-Infrastruktur. Ein Schedule/Watcher ist erst nötig, wenn ein realer Owner-Need für proactive notification entsteht.

Ein neuer Upstream-Ref ist nur ein Update-Signal, nie automatische Adoption.

### SR-D — AI-owned Execution Routing

Ein Parent-Orchestrator entscheidet aus aktuellem State:

- benötigte Kompetenz;
- consequence/judgement class;
- billigste hinreichende Execution Class;
- bounded Context;
- Parallelisierbarkeit;
- Review-/Escalation-Tiefe.

Der Owner routet keine Worker manuell.

Die kanonische Repräsentation bleibt **modell-/produktagnostisch**. Aktuelle Work/Codex/Workspace-Agent-Fähigkeiten sind Runtime-Kandidaten und müssen vor Ausführung frisch geprüft werden.

## 6.2 Nicht Teil des kleinsten problem-schließenden Scopes

Nicht bauen:

- Skill Registry Service;
- allgemeine Agentenplattform;
- Workflow Engine;
- globalen Model Scheduler;
- Knowledge Graph;
- neue Datenbank;
- automatische Upstream-Adoption;
- permanente Skill-Kopie/Vendoring ohne nachgewiesenen Bedarf;
- generische Derivative Engine;
- neue Requirement-/Method-Registry;
- automatische Owner-Decision-Komponente.

---

# 7. Realer Integrationspilot

## 7.1 Pilotobjekt

`esany/Wissensarbeit` – **System Analysis + Finding-Driven Deep Research**

Upstream State am 2026-09-27:

- Parent Work Owner: Wissensarbeit #43;
- Runtime PR: #51;
- exact frozen reviewed head: `f3726c962807b311e8a2a7df63f738e11790fbed`;
- PR #51: open, unmerged;
- R2 Contract-Conformance geschlossen;
- #46 Cross-Project Trials owner-authorized und noch nicht abgeschlossen;
- Generic Fit nicht etabliert;
- Merge nicht durch #46 autorisiert.

Diese Eigenschaften **sind Teil der Source-Identität/Maturity**, nicht Nebendetails.

## 7.2 Warum dieser Pilot diskriminierend ist

Er prüft gleichzeitig:

1. non-main upstream source;
2. frozen reviewed exact ref;
3. offene weitere Trial-/Maturity-Entwicklung;
4. klare Trennung von Skill Method und Host-Projekt-Authority;
5. reale Runtime-Dateien;
6. Statusänderungen, die nicht automatisch lokale Adoption auslösen dürfen.

Ein Dummy-Skill oder bereits stabil gemergtes Paket wäre als erster Falsifier schwächer.

## 7.3 Pilot-Acceptance

Der Pilot gilt erst dann als problem-schließend, wenn ein fresh Histo execution context:

- den aktuellen Wissensarbeit-State frisch liest;
- den exact upstream Skill basis ref bestimmen kann;
- Maturity/Owner/PR-Status sichtbar erhält;
- keinen latest-ref automatisch ausführt;
- einen lokal zugelassenen Basisstand wiederaufnehmen kann;
- bei geändertem Maturity-/Semantic-State `HOLD/UNRESOLVED` statt Auto-Upgrade erzeugt;
- eine Histo-spezifische Anpassung als Derivat mit Lineage statt als stilles Copy/Fork behandelt;
- Histo Requirements/Method Truth nicht kopiert oder upstream delegiert;
- einen bounded Work Context erzeugt;
- AI-orchestriert ohne manuelle Chat-Kette des Owners arbeitet;
- seine eigene Coverage Ceiling sichtbar macht;
- STOP vor Folge-Implementation/Promotion ohne neue Admission macht.

---

# 8. Hazard / Critical-State Register

| ID | Trigger | Kritischer Zustand | Prevention | Detection | Fail-closed / Recovery | Test |
|---|---|---|---|---|---|---|
| H-01 | Analyse wird als Mutation-GO interpretiert | unautorisierte persistente Änderung | gebundene Admission/Work Package Authority | fehlender/inkonsistenter admission context | `STOP / OWNER ADMISSION REQUIRED` | Analyse-only Fixture |
| H-02 | ein GO wird auf Nachfolger übertragen | Authority Cascade | Work Package Scope + STOP Boundary + no-cascade | successor ohne eigene Admission | `BLOCK/HANDOFF` | exactly-one / successor-negative test |
| H-03 | Connector darf schreiben, daher wird Authority angenommen | Credential Laundering | Credential != Authority explizit; branch/PR | mutation ohne Admission Ref | `BLOCK`; keine main mutation | connector-write negative fixture |
| H-04 | bounded Edit wird broad replacement | Datenverlust | bestehender Mutation Guard / diff review | candidate != bounded plan | `blocked`; fresh refetch | bestehende D1 Regressionen |
| H-05 | Upstream PR-Head ändert sich | stilles Skill-Upgrade | fresh inspect + exact consumer basis ref | ref mismatch | `HOLD`; weiter letzter admitted basis | changed-ref fixture |
| H-06 | Upstream Maturity/Owner ändert sich ohne Datei-Delta | semantisch falsche Adoption | Status/Maturity Teil des Bindings | metadata delta | `HOLD/REVIEW` | status-only delta fixture |
| H-07 | Upstream wird inkompatibel | funktionierender Histo-Pfad bricht | admitted basis bleibt getrennt von latest observed | compatibility check | letzten basis ref behalten; derivative candidate | incompatible fixture |
| H-08 | lokales Derivat verliert Herkunft | Fork Drift / Provenienzverlust | mandatory lineage | missing source/ref/reason | `BLOCK` | lineage-negative fixture |
| H-09 | Skill kopiert Histo Rules/Method Truth | zweiter Truth Store | reference-only integration | duplicate semantic content review | `REJECT/REFACTOR` | duplicate-rule fixture |
| H-10 | günstiger Worker entscheidet judgement-heavy Conflict | Authority/Semantic Error | competence/consequence routing | worker reports conflict / low deterministic control | escalate to stronger judgement context | routing fixture |
| H-11 | teurer Worker rekonstruiert wiederholt bekannten State | unnötige Kosten | canonical refs + bounded context | context budget/duplication review | recompile minimal context | context-economy fixture |
| H-12 | Parallelworker nutzen verschiedene Baselines | stale/race integration | basis fingerprints; shared immutable plan | SHA mismatch | invalidate affected result | stale-basis fixture |
| H-13 | Worker fällt nach Partial Mutation aus | inkonsistenter State | branch, atomic/bounded writes, package boundaries | incomplete postcondition | rollback/restart from Git state | partial-failure fixture |
| H-14 | CI grün | false assurance / owner problem ungelöst | maturity ladder + real-use acceptance | coverage ceiling remains | no promotion | false-assurance fixture |
| H-15 | Planung verkleinert Problem auf „Manifest vorhanden“ | Scope Laundering | Problem Closure Contract | real-use closure absent | status stays partial | closure-eval fixture |
| H-16 | Repo kann Plattformapproval nicht technisch sehen | Scheindeterminismus | enforcement class `platform-external/procedural` sichtbar | capability inspection | request/require platform approval; no false PASS | platform-boundary fixture |
| H-17 | Orchestrierung erfordert Owner kopiert Worker-Kontext | Human-as-Workflow-Engine Regression | AI-owned orchestration acceptance | owner manual routing required | reject execution route | owner-burden acceptance |
| H-18 | Work Order kann neue Dateien nicht deklarieren | Implementer umgeht Scope oder startet unsicher | vor Admission exakte file-create semantics klären | `EXEC007` on non-existent file | BLOCK until contract supports/avoids required create | preflight negative test |

---

# 9. Offene Fragen / Decision Register

| ID | Klasse | Frage | Blocking für Planung? | Blocking für Implementation Admission? | Disposition / Owner |
|---|---|---|---|---|---|
| OQ-01 | Lifecycle/Authority | Soll `User GO / no cascade` repo-weit Governance, Execution Contract oder Requirement werden? | nein | nein für bounded Pilot mit explizitem Owner Constraint; ja für allgemeine Promotion | #9/#42/#61 später reconciliieren |
| OQ-02 | Technical | Braucht der Pilot einen neuen machine-readable Binding Record oder reicht bestehender Work Context? | nein – Plan kann discriminating spike festlegen | ja vor finalem exact-file Work Order | #48 minimal option test |
| OQ-03 | Technical | Wie werden neue Dateien in bounded Work Orders deklariert? Current `EXEC007` verlangt existing files. | nein | **ja**, falls finaler Slice neue Files braucht | #48/#59/#61: kleinste Contract-Erweiterung nur bei realem Bedarf |
| OQ-04 | Platform | Welche aktuelle Execution Surface kann AI-owned Orchestration + approvals + required repo/app access liefern? | nein | ja beim Runtime Preflight | capability-first recheck unmittelbar vor run |
| OQ-05 | Compatibility judgement | Welche Semantik macht ein Upstream-Delta „compatible“? | teilweise | ja für Auto-disposition; nein wenn default fail-closed review | erster Pilot nutzt explicit review, keine vorschnelle Universalregel |
| OQ-06 | Derivative | Welche Form hat lokales Derivat, falls Pilot absichtlich eine Inkompatibilität simuliert? | nein | nur für derivative test path | lineage contract zuerst, konkrete Form nach realem delta |
| OQ-07 | Review | Unabhängiger fresh-context Review dieses Plans ist in diesem Chat technisch nicht ausführbar | **ja für `READY FOR OWNER ADMISSION`** | ja | separate fresh strong review erforderlich |

### Echte #44-Blocker

Aktuell entsteht **keine neue #44-Decision** aus diesem Plan.

Bestehend bleibt `DD-20260903-001` GitHub Required-PR/Branch-Protection. Diese Lücke blockiert nicht das Erstellen eines Review-Branches/PRs, aber verhindert die Behauptung, direct-main admission sei serverseitig vollständig erzwungen.

---

# 10. Dependency / Prerequisite Graph

```text
P0 current-state revalidation
  ├─ Histo controlling refs + exact main SHA
  ├─ Wissensarbeit owner/status + exact Skill ref
  └─ available execution capabilities/permissions
          ↓
P1 Owner-bound admission semantics for the selected Work Package
          ↓
P2 exact file/mutation scope preflight
  └─ if new files needed: resolve Work-Order create-target gap first
          ↓
P3 external Skill source-binding + freshness/compatibility slice
          ↓
P4 real frozen Skill pilot
          ↓
P5 adversarial incompatibility / stale / authority / no-cascade tests
          ↓
P6 fresh-context restart + owner-burden / problem-closure acceptance
          ↓
P7 keep | adapt | derivative-candidate | reject
```

Parallelisierbar nach P0/P1:

- deterministic fixture preparation;
- current upstream metadata capture;
- execution-surface capability inspection;
- read-only SOTA/Best-Practice challenge.

Nicht parallelisieren:

- Work Package Admission vor finalem Scope;
- compatibility promotion vor semantic review;
- derivative creation vor lineage decision;
- real-use acceptance vor funktionierendem end-to-end path.

---

# 11. Test-before-Code Acceptance Matrix

## Authority / Interaction

- **AT-A01** Analyse-only Context führt zu keiner persistenten Mutation.
- **AT-A02** Planning-GO erlaubt Planungsartefakte, nicht Implementation.
- **AT-A03** ein exact bounded Implementation GO autorisiert genau den gebundenen Work Package Scope.
- **AT-A04** Nachfolger nach STOP hat keine implizite Authority.
- **AT-A05** Tool Credential ohne Admission reicht nicht.
- **NT-A01** terse `ok` ohne eindeutige sichtbare Binding Envelope darf keine materielle Alternative wählen.
- **NT-A02** `green CI` erzeugt keine Owner-/Merge-/next-phase Authority.

## Source Binding / Upstream

- **AT-S01** exact upstream Repo/Owner/PR/Head/Maturity ist reconstructable.
- **AT-S02** unchanged upstream bleibt no-op.
- **AT-S03** changed head wird erkannt, aber nicht auto-adopted.
- **AT-S04** status-/maturity-only Delta wird erkannt.
- **AT-S05** locally admitted basis bleibt trotz newer observed ref verfügbar.
- **NT-S01** `main` wird nicht fälschlich als source ref verwendet, wenn reviewed package auf offenem PR-Head liegt.
- **NT-S02** upstream existence wird nicht als Histo compatibility/admission interpretiert.

## Compatibility / Derivative

- **AT-C01** kompatibles Delta kann als Review-Candidate dispositioniert werden.
- **AT-C02** ambiguous Delta bleibt `unresolved/HOLD`.
- **AT-C03** incompatible Delta zerstört letzten admitted basis nicht.
- **AT-C04** derivative candidate besitzt source repo/ref + divergence reason + review policy.
- **NT-C01** silent copy/vendor without lineage schlägt fehl.
- **NT-C02** Histo Requirement-/Method-Text wird nicht in source-binding record dupliziert.

## Orchestration / Resource

- **AT-O01** mechanischer bounded Slice kann auf günstigste hinreichende Execution Class geroutet werden.
- **AT-O02** semantic/authority conflict eskaliert in judgement-stärkere Klasse.
- **AT-O03** Worker erhält bounded refs statt Vollhistorie, wenn dies qualitätsäquivalent ist.
- **AT-O04** Owner muss keine Worker-Chats manuell verbinden.
- **NT-O01** Task-Label „coding/research“ allein entscheidet nicht den Modus.
- **NT-O02** Tokenersparnis darf kein notwendiges Context-/Quality-Feld entfernen.

## Safety / Restartability

- **AT-R01** stale basis SHA macht Current Context not-ready.
- **AT-R02** partial failure bleibt auf Branch reversibel/restartbar.
- **AT-R03** fresh context rekonstruiert source/admission/status aus Repo.
- **AT-R04** unchanged rerun erzeugt `NO_CHANGE` statt Commit-Noise.
- **NT-R01** direct-main mutation ist kein zulässiger Pilotpfad.

## Problem Closure

- **AT-P01** realer Histo-Task kann den externen Skill unter Histo Authority tatsächlich verwenden.
- **AT-P02** Owner erhält problem-/research-facing Resultat, nicht nur Integrationsmetadaten.
- **AT-P03** bei Upstream-Änderung bleibt der Workflow verständlich und sicher fortsetzbar.
- **AT-P04** AI-Orchestrierung senkt Owner-Metaarbeit gegenüber manueller Mehrchat-Koordination.
- **NT-P01** „Manifest/Validator vorhanden“ alleine darf Problem Closure nicht PASS ergeben.

---

# 12. Ressourcen-/Orchestrierungsmodell

## 12.1 Dauerhafte Semantik

Nicht Modellnamen persistieren, sondern Execution Classes:

### EC-MECHANICAL

- klare Inputs/Outputs;
- starke deterministische Acceptance;
- niedrige semantische Ambiguität;
- hohe Wiederholbarkeit;
- Beispiele: Inventar, Ref-/SHA-Checks, Fixture-Ausführung, bounded mechanical edit.

### EC-JUDGEMENT

- konkurrierende Interpretationen;
- Authority-/Requirement-Grenzen;
- Compatibility mit semantischem Delta;
- Root Cause / Architecture Trade-off;
- adversarial review.

### EC-SPECIALIST

- qualifizierte externe Fach-/Security-/Legal-/statistische Validierung, falls durch Konsequenz nötig.

## 12.2 Runtime Routing

Vor jedem längeren Run:

```text
required operation/quality
→ current capabilities + permissions inspect
→ boundedness / consequence class
→ cheapest sufficient execution class
→ worker/context allocation
→ deterministic checks
→ integration/review
→ STOP/ESCALATE at material authority boundary
```

Der aktuelle OpenAI-Produktstand (Sep 2026) bietet mit ChatGPT Work, Codex und – je nach Plan/Workspace – Workspace Agents aktuelle Kandidaten für länger laufende, toolgestützte bzw. wiederholbare Workflows. Diese Verfügbarkeit ist **runtime-dynamisch** und wird nicht zum Histo Contract.

Fallback-Regel: Wenn heterogene Subagent-/Modell-Orchestrierung im aktuellen autorisierten Kontext nicht verfügbar ist, bleibt die Arbeit im hinreichend starken Parent-Kontext oder wird in deterministische lokale Tools zerlegt. **Der Owner wird nicht als manueller Agent Router eingesetzt.**

---

# 13. Planning Quality Gate

| Dimension | Status | Begründung |
|---|---|---|
| Intent Fidelity | PASS | Owner-Statements separat von AI-Synthese geführt |
| Problem-Closure Fidelity | PASS | End-to-End Closure Contract statt Manifest-only Slice |
| Source-/Role Fidelity | PASS | Source-role ledger; unautorisierter #48 Candidate nicht als Owner Truth |
| Authority Fidelity | PASS | Planning Authority ≠ Implementation Admission; no cascade |
| Intent-relative Completeness | PASS | Authority + integration + orchestration + real-use closure gemeinsam abgedeckt |
| Current-State Fidelity | PASS | Histo/Wissensarbeit fresh basis refs explizit |
| Dependency Completeness | PARTIAL | finaler file-create/work-order path abhängig von exact implementation shape |
| Critical-State Prevention | PASS for planning | Hazard register vorhanden; implementation enforcement noch nicht gebaut |
| Forbidden-Loss Coverage | PASS | Authority, maturity, lineage, Histo truth, uncertainty, restartability |
| Boundedness | PASS | ein realer Skill-Pilot; kein generic platform build |
| Reversibility / Recovery | PASS in plan | branch/PR, last admitted basis, rollback/restart requirements |
| Test-before-Code | PASS | Acceptance/negative/adversarial matrix vor Code |
| Assurance Calibration | PASS | Planning/CI/real-use maturity getrennt |
| Determinism Boundary | PASS | platform-external judgement/approval nicht als repo-determinism maskiert |
| Resource Efficiency | PASS | total-cost/quality-equivalence routing |
| Competence-aware Routing | PASS | EC-MECHANICAL/JUDGEMENT/SPECIALIST |
| AI-owned Orchestration | PASS as requirement/plan | runtime capability still to preflight |
| Independent Challenge | **UNRESOLVED** | fresh independent reviewer in diesem Chat nicht verfügbar |
| Restartability | PASS for plan | exact refs/status/deps/next gates im Repo-Artefakt |
| One Fact / One Canonical Home | PASS | Plan verweist auf bestehende Semantik statt Kopie |
| Owner Burden Minimization | PASS | owner only at material admission/decision boundaries |
| SOTA / Best-Practice Fit | PARTIAL | current execution-surface capability checked; implementation-tool SOTA must be rechecked at exact decision |
| Trace Correctness | PASS | explicit source role / candidate status |
| No Architecture-before-Need | PASS | responsibilities from demonstrated failures/problem closure |
| No Scope Laundering | PASS | real-use problem closure required |

## Readiness Verdict

**`PARTIAL — one hard planning gate and one implementation-shape dependency remain.`**

Hard gate before `READY FOR OWNER ADMISSION`:

1. **fresh independent adversarial review** of this plan and execution breakdown;
2. disposition of any findings;
3. exact implementation file topology / handling of new-file declarations in bounded Work Order after that review.

Kein Code darf aus diesem Status gestartet werden.

---

# 14. Nicht-Entscheidungen

Dieses Artefakt entscheidet ausdrücklich **nicht**:

- dass ein source-binding Manifest die finale Form ist;
- dass ein GitHub Action Watcher gebaut wird;
- dass ein bestimmtes ChatGPT/Codex/Workspace-Agent-Produkt erforderlich ist;
- dass Luna/Sol oder andere Modellnamen kanonische Rollen sind;
- dass `User GO` als neues #42 Requirement promoted wird;
- dass #52 Wissensarbeit als Histo Skill-System-Architektur übernommen wird;
- dass PR #51 lokal automatisch konsumiert wird;
- dass ein lokales Derivat nötig ist;
- dass irgendeine Implementation admitted ist.

---

# 15. Nächste zulässige Aktionen

1. versionierten Execution-/Work-Breakdown für diesen Readiness Candidate sichern;
2. fresh independent adversarial review auf exact planning head durchführen;
3. Findings `accept | refine | reject | unresolved` dispositionieren;
4. falls der Plan dann alle Gates erfüllt: `READY FOR OWNER ADMISSION` feststellen;
5. dem Owner exact Implementation Admission vorlegen;
6. erst nach separat gebundenem Owner-GO den ersten implementation Work Order admitten.

---

# 16. Handoff

Ein neuer Bearbeiter startet mit:

1. `AGENTS.md`
2. `PROJECT_STATE.md` (beachte: Snapshot vom 24.09.; jüngere Work-Owner-/Commit-Stände haben Präzedenz)
3. `README.md`
4. #48 / #42 / #59 / #61 / #63
5. dieses Artefakt
6. `docs/development/ai-orchestrated-skill-integration-execution-plan-20260927.md`
7. Wissensarbeit #43/#46/#48/#52/#53/#55 und PR #51 frisch revalidieren.

**Keine Implementation ist durch dieses Artefakt autorisiert.**
