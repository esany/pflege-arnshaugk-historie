# Histo-Orla – Method Conformance, Work Context und Handoff Assurance

**Status:** `working-architecture / assurance-research v0.1`  
**Work Owner:** #61  
**Parent:** #48 Architecture Execution  
**Domain Method Owner:** #60  
**Governance:** #9 / `AGENTS.md`  
**Accepted Requirement Inputs:** #42, insbesondere `REQ-EPI-001`, `REQ-WF-001`, `REQ-UX-001`, `REQ-VAL-001/002`, `REQ-STATE-001`  
**Architecture Interfaces:** #50, #54, #55, #57  
**Stand:** 2026-08-31

## 1. Problem

#60 etabliert die bislang fehlende fachwissenschaftliche Mittelschicht: domänenspezifische Method Profiles müssen SOTA-belegt, quellentypbezogen, inferenzkritisch und an realen Fällen getestet sein.

Das löst **Method Truth**, aber noch nicht automatisch **Method Conformance**.

Ein System kann einen exzellenten Methoden-Text besitzen und trotzdem scheitern, wenn ein konkreter Work Context:

- ohne eindeutigen Scope/Owner/Authority startet;
- ein `method-candidate` wie eine etablierte operative Methode verwendet;
- Findings ohne rekonstruierbare Method Application promoted;
- Evidence-/Validation-Gates überspringt;
- beim Domain→Dev-Handoff Fachsemantik verliert;
- bei einem neuen Chat Rolle/Methodik anders rekonstruiert;
- formale Invarianten nur durch Prompt-Disziplin schützt.

Leittrennung:

```text
METHOD TRUTH
Was ist fachlich ein zulässiges Vorgehen?
Owner: #60 / Fachdomäne

METHOD CONFORMANCE
Wurde dieses Vorgehen in diesem konkreten Work Context korrekt referenziert,
angewandt, geprüft und nur durch erlaubte Übergänge promoted?
Owner: #61 + #50/#54/#55/#57
```

## 2. Bereits akzeptierte Systemgrundlage

Es ist derzeit **kein neues Requirement erforderlich**, um die erste Assurance-Schicht zu rechtfertigen.

### `REQ-EPI-001`

Consequential Research muss führende Domäne(n), domänenspezifische Methoden, Evidenzmaßstab und zulässige Schlussarten nachvollziehbar machen. Generischer AI-Output ohne Fachrouting darf nicht consequential promoted werden.

### `REQ-WF-001`

Formal prüfbare wissenschaftliche/technische Invarianten dürfen nicht allein von Prompt-/LLM-Compliance abhängen.

### `REQ-UX-001`

Eine wesentliche Ausgabe muss bis Finding, Quelle/Fundstelle, Evidenzstatus, Methode/Kompetenz, Unsicherheit und Research History auditierbar sein.

### `REQ-VAL-001/002`

Validation Levels und unabhängige qualifizierte Fachvalidierung müssen unterscheidbar bleiben.

### `REQ-STATE-001`

Kuratierter Research State muss provider-/chatunabhängig und restartbar sein.

Daher ist die erste Aufgabe **Operationalisierung vorhandener Requirements**, nicht Requirements-Proliferation.

## 3. SOTA-/Best-Practice-Referenzrahmen

Die folgenden Standards/Patterns werden als Referenzrahmen geprüft. Sie sind **keine vorweggenommene Technologieentscheidung**.

### 3.1 Schema-as-Contract / machine-readable validation

**JSON Schema 2020-12** ist ein aktueller etablierter Standard zur Beschreibung und Validierung strukturierter JSON-Dokumente.

Referenz: https://json-schema.org/draft/2020-12

Relevanz für Histo-Orla:

- required structure;
- controlled values;
- referential/completeness checks in Verbindung mit eigener Validatorlogik;
- versionierbare Contract-Spezifikation;
- tool-/providerunabhängige, portable Validierung.

Nicht ausreichend für:

- historische Wahrheit;
- komplexe wissenschaftliche Inferenz;
- alleinige Cross-Record-Transition-/Referenzlogik.

### 3.2 Provenance model

**W3C PROV / PROV-O** stellt Entity, Activity und Agent sowie Beziehungen wie `used`, `wasGeneratedBy`, `wasDerivedFrom`, `wasRevisionOf`, Attribution und qualifizierte Provenienz bereit.

Referenz: https://www.w3.org/TR/prov-o/

Relevanz:

- Method Application als Activity statt Eigenschaft eines Findings;
- klare Trennung von Evidence/Artifact, Processing/Research Activity und verantwortlichem Agent/Reviewer;
- Revision/Demotion/Derivation ohne History-Verlust;
- interoperabler Referenzrahmen für Provenienz.

Nicht daraus ableiten:

- RDF/OWL als Pflichtspeicher;
- vollständige PROV-O-Ontologie im MVP.

### 3.3 Portable Research Objects

**RO-Crate** ist ein etablierter leichtgewichtiger Ansatz, Forschungsdaten und Kontextmetadaten als portables Research Object menschen- und maschinenlesbar zu bündeln. Die aktuelle Spezifikationsseite führt RO-Crate 1.3 als current long-term release.

Referenz: https://www.researchobject.org/ro-crate/specification.html

Relevanz:

- Export-/Handoff-Paket;
- portable Verknüpfung von Files, externen Ressourcen, Personen/Software/Metadaten;
- möglicher providerneutraler Export des kuratierten Research State.

Hypothese:

RO-Crate ist für Histo-Orla wahrscheinlicher **Interchange/Export Boundary** als primäres internes Canonical-State-Modell. Das ist zu testen.

### 3.4 Execution provenance

**Workflow Run / Provenance Run RO-Crate** beschreibt retrospektive Provenienz von Tool-/Workflow-Ausführungen mit Inputs, Outputs, Software und einzelnen Schritten.

Referenz: https://www.researchobject.org/workflow-run-crate/

Relevanz:

- Processing Run / OCR / Retrieval / reproduzierbare mechanische Workflows;
- Trennung von prospective workflow und tatsächlichem Run;
- Vergleichsfolie für `Method Profile` vs. `Method Application`.

Wichtig:

Eine historische Method Application ist nicht identisch mit einem Computation Workflow Run. Das Pattern ist nützlich für Provenienz, nicht als Modell der Geschichtswissenschaft selbst.

### 3.5 Policy-as-Code / policy decision vs enforcement

**Policy-as-Code** trennt deklarierte Regeln von deren technischer Enforcement. OPA ist ein etablierter, CNCF-graduated general-purpose Policy Engine Kandidat.

Referenz: https://www.openpolicyagent.org/docs

Relevanz als Pattern:

- `policy says transition is forbidden` getrennt von `application enforces transition`;
- versionierbare Policies;
- negative tests und Decision Logs.

Disposition für v0.1:

**Pattern adopt; OPA implementation deferred.** Für den aktuellen Umfang ist ein kleiner lokaler Validator/Transition Layer wahrscheinlich hinreichender. OPA wird erst neu bewertet, wenn reale Policy-Komplexität/mehrere Enforcement Points dies rechtfertigen.

## 4. Internes Prior Art: `paleo-type`

Aktueller Challenge-Befund:

### 4.1 Machine-readable source contract + validator

`paleo-type` führt fachlich geklärte Source-/File-/Project-Invarianten nicht nur in Prosa, sondern zusätzlich in `corpus/source-contract.json`. `tools/source_contract.py` prüft u. a. required fields, IDs, Parent-/Part-of-Beziehungen, Zyklen, SHA-256, Storage State und referentielle Integrität.

Generalisierbares Pattern:

```text
human-readable method/governance
→ machine-readable projection settled invariants
→ deterministic validator
→ negative regression fixtures
```

Nicht generalisieren:

- konkrete TSV-/JSON-Struktur;
- konkrete Paleo-Source-Hierarchie.

### 4.2 Replaceable work context

#71/#77 verfolgen:

> `standardize the path, not the scholarly outcome`

Stable werden Role/Authority, required context, checks, stop/handoff, canonical owner und return path; wissenschaftliches Urteil bleibt nicht deterministisch.

### 4.3 Directed Source Research → Domain Review → Dev

Der aktuelle G2-Zyklus zeigt praktisch:

```text
persisted source-bound evidence
→ Domain Review
→ classifies source-local / project / existing generic requirement / deterministic candidate / specialist need
→ no automatic implementation
→ project STATUS / NEXT ACTION synchronized
```

### 4.4 Fresh-context availability

Der jüngste Restart-Test unterscheidet:

```text
RETRIEVABLE
≠ STAGED
≠ VISION-INSPECTABLE
```

Generalisierbares Muster für Histo-Orla:

Eine NEXT ACTION ist nur ausführbar, wenn die notwendige Evidenz im Zielkontext tatsächlich verfügbar ist; bekannte Identität/Route allein reicht nicht.

## 5. Empfohlene minimale Assurance-Architektur

Noch keine physische Technologieentscheidung. Verantwortlichkeiten zuerst.

### A. Human-readable Domain Method Profile

Owner #60.

Enthält SOTA, Fachbegriffe, Quellenmodell, Playbook, Inferenzvertrag, Evidence Appetite, QA/Falsifikation, Interfaces und AI-Grenzen.

### B. Machine-readable Method Profile Projection

Owner fachliche Semantik #60; technische Projektion #61/#50/#54.

Kandidat für formal prüfbare Teile:

```text
profile_id
version
status
scope / applicability
leading_when / controlling_when
required gates
allowed output classes
validation requirements
handoff triggers
supersedes / deprecated_by
```

Die Projektion darf **nur** fachlich bereits geklärte Struktur enthalten. Sie ist kein zweiter Methoden-Text.

### C. Work Order / Work Context

Definiert konkrete Aufgabe und Authority Boundary:

```text
work_order_id
work_owner
primary_function
question / objective
scope / exclusions
leading + controlling domains
applicable_method_profiles
required evidence/context
may / must_not
stop/handoff
completion/return
persistence target
```

Soweit aus Repository-State ableitbar, wird dies komponiert statt manuell dupliziert.

### D. Method Application

Eigenes Provenienzobjekt für die konkrete Anwendung:

```text
method_application_id
work_order
method_profile + version/status
actor / agent class
inputs / evidence
steps/gates actually executed
not-assessable / skipped-with-reason
outputs
started/ended
review target
```

Dies verhindert die falsche Abkürzung:

`Finding has method = Diplomatik`.

Stattdessen:

`Finding ← generated/reviewed through Method Application ← used Method Profile version X`.

### E. Review / Validation

Eigene Activity/State:

```text
review_id
review_type
reviewer_class
object reviewed
evidence inspected
method/context
result
limits
validation_level
next transition permitted?
```

Independent Specialist Review bleibt eigene Reviewer-/Validation-Klasse.

### F. Handoff

Gerichteter Transfer zwischen Authority-Bereichen:

```text
from / to
trigger
owner/task
evidence
established
unresolved / not investigated
request
non-goals
allowed authority
return condition
persistence
```

### G. Transition/Policy Layer

Kleine explizite State-/Transition-Tabelle + Validator ist die bevorzugte v0.1-Hypothese.

Beispiel:

```text
IF research_object target_status >= consequential
THEN method_profile.status >= working-method
AND evidence/findspot present
AND required review level satisfied
AND authority transition allowed
ELSE deny transition, retain candidate
```

Der Validator prüft den **Übergang**, nicht die Richtigkeit der historischen Aussage.

### H. Derived Audit View

#55 rendert aus demselben State:

```text
Finding
→ Evidence / Findspot
→ Work Order / Scope
→ Method Application
→ Method Profile + version/status
→ Review / Validation
→ Alternatives / Unresolved
→ Transition / History
```

Kein manuell gepflegter zweiter Audit-Truth-Store.

## 6. Verantwortungsteilung / Delegationsmatrix

| Verantwortung | Owner | Übergabe an | Darf nicht |
|---|---|---|---|
| Fachmethoden-SOTA, Inferenzregeln, QA | #60 / Fachdomäne | #61/#42 bei Systemimplikation | Architektur/Validator aus Convenience festlegen |
| Historische Evidence/Findings | #46/#47 | #60 bei Method Friction; Domain Review/Requirements bei generalisierbarem Gap | lokale Finding automatisch generalisieren |
| Work-Context-/Handoff-Governance | #9 / `AGENTS.md` | #61 zur technischen Enforcement | Fachmethode definieren |
| Accepted Requirements | #42 | #48ff | Lösungstechnologie als Requirement tarnen |
| Canonical State Responsibilities | #50 | #54/#55/#57 | Fachurteil entscheiden |
| Transition/Invariant Enforcement | #54 / #61 | Domain Review bei fachlich offener Semantik | wissenschaftliche Wahrheit determinisieren |
| Human-readable Audit | #55 | Research Owner/Reviewer | parallelen Research State führen |
| Restartability / Provider Removal | #57 | #48/#58 | bloße Dokumentexistenz als ausführbaren Handoff werten |
| Architecture Coordination | #48 | #58 ADR/MVP | neue Method Truth erzeugen |
| Dev / Implementation | später #59 | Domain Review / scholarly adequacy | Fachrequirement selbst erfinden |
| unabhängige Fachvalidierung | externe qualifizierte Fachperson | Domain Review / Owner | Projekt-/Architekturautorität übernehmen |

## 7. Harte vs. weiche Kontrolle

### Hart / deterministisch

Sobald implementiert:

- erforderliche IDs/Referenzen;
- Work Owner / Scope vorhanden;
- Method Profile referenziert;
- Method Profile Status erlaubt den gewünschten Promotion Level;
- Evidence/Findspot für evidenzielle Findings vorhanden;
- AI Output nicht als Evidence Class;
- erlaubte Status-/Authority-Transition;
- erforderliche Review-Klasse vorhanden;
- Handoff required fields vorhanden;
- History wird bei Revision/Demotion nicht gelöscht;
- externe Processing Rights werden vor externem Run geprüft.

### Fachlich / nicht deterministisch

- richtige historische Interpretation;
- welche Lesart bei ambiger Quelle überzeugt;
- ob Quellenlage fachlich hinreichend ist, soweit nicht über klar etablierte Mindestgates operationalisierbar;
- welche Hypothese historisch am besten erklärt;
- ob ein Domain Method Profile fachlich inhaltlich richtig ist;
- unabhängige Expertenbewertung.

## 8. Fail-closed-Regel

Wichtigste Sicherheitsentscheidung:

> **Fail closed on promotion, not on exploration.**

Das System darf weiterarbeiten, wenn Methodenlage noch nicht final ist:

```text
method missing/insufficient
→ candidate/exploratory allowed
→ method debt visible
→ #60 work/handoff
```

Es darf aber nicht still hochstufen:

```text
candidate + plausible AI narrative
→ consequential validated
```

Damit blockiert Method Research nicht die Forschung, schützt aber den kanonischen Qualitätsstatus.

## 9. Noch zu härtende Research-Themen

### R-MC-01 — Method Applicability / Routing

Wie wird fachlich entschieden, welches Profile `leading`, `controlling` oder `not applicable` ist? Ein Keyword-/Disziplinlabel reicht nicht.

Owner: #60; technische Folge #61.

### R-MC-02 — Multi-Method Composition

Wie werden mehrere Domain Profiles auf dasselbe Situation Dossier angewandt, ohne Master-Domain, doppelte Arbeit oder semantische Vermischung?

Zu klären:

- Reihenfolge vs. Parallelität;
- gemeinsame Pflichtbeobachtungen;
- inkommensurable Begriffe;
- widersprechende Fachinterpretationen;
- Cross-Evidence Return Contract.

Owner: #60.

### R-MC-03 — Method Version Drift / Revalidation

Was passiert mit früheren Findings, wenn `method-profile v1` durch `v2` ersetzt/deprecated wird?

Nicht automatisch neu bewerten; aber abhängig von Change Impact ggf. `review-needed` markieren.

Owner: fachlich #60; State/Transition #50/#54/#61.

### R-MC-04 — Mandatory vs. conditional gates

Welche Profilgates sind immer erforderlich, welche nur bei Trigger? Wie wird `not-assessable` von `not executed` unterschieden?

Owner: #60; Validatorprojektion #61.

### R-MC-05 — Review independence / validation provenance

Reviewer-Klasse, Independence, evidence actually inspected und Validation Scope müssen sauber modelliert werden.

Owner: #45/#60; State #50/#54.

### R-MC-06 — AI / Tool provenance proportionality

Nicht jeden Prompt archivieren. Zu bestimmen ist, wann Model/Tool/Version/Parameters wissenschaftlich materiell sind.

Owner: #45/#61/#52/#53.

### R-MC-07 — Work-context fresh restart

Nicht nur State exportieren: ein neuer Chat muss Authority, Methode, Evidence Availability und NEXT ACTION korrekt rekonstruieren.

Owner: #57/#61.

### R-MC-08 — Audit UX

Kann ein fachinteressierter Nutzer ohne Repositorywissen erklären:

`Warum glaubst du das? Welche Quelle? Welche Methode? Welche Alternative? Was war KI? Was wurde extern validiert?`

Owner: #55.

## 10. Thin Slice / Falsifikation

Erster realer Test:

- Triptis 1212 / NHUB II Nr. 8;
- zweiter U2-Fall mit anderer methodischer Belastung, z. B. Moxa 1296 oder Schleiz-Transsumpt.

Ablauf:

```text
Work Order
→ Domain Profile
→ Method Application
→ exact Evidence
→ Observations
→ Findings / Research Hooks / Hypotheses
→ Domain Review
→ Promotion Guard
→ Audit View
→ fresh-context Resume
```

### Negative Tests

1. consequential Promotion ohne Method Profile → deny.
2. `method-candidate` statt `working-method` → candidate work erlaubt, consequential Promotion deny.
3. Finding ohne Evidence/Findspot → deny evidenziellen Promotion State.
4. AI Output als Evidence → deny.
5. Dev Scope ohne accepted Requirement/Owner Constraint → return/deny expansion.
6. fehlender Handoff-Return-State → handoff incomplete.
7. `unresolved/not-assessable` wird durch Schema zu erfundener Aussage gezwungen → contract fail.
8. Method Profile v2 ersetzt v1 und alte Findings werden still umgedeutet → fail.
9. unabhängige Review wird aus AI self-review abgeleitet → fail.
10. frischer Context kennt Dokumente, aber kann Evidence nicht inspecten → restart fail für die konkrete NEXT ACTION.

## 11. Vorläufige Architecture Recommendation

Für v0.1 bevorzugte Hypothese:

```text
Markdown = human-readable canonical fachliche Methode
+
small machine-readable manifest/projection = settled formal semantics only
+
local deterministic validator + explicit transition table
+
Git/versioned canonical state/history
+
derived audit/resume views
+
portable export evaluated against RO-Crate/PROV compatibility
```

### Vorerst nicht aufnehmen

- OPA-Service / zentrale Policy Platform;
- Workflow Engine;
- Multi-Agent Runtime;
- RDF Triple Store;
- Knowledge Graph nur für Method Conformance;
- Event-Sourcing-Plattform;
- Prompt Registry als Truth Store.

Diese werden erst bei realem Trigger neu bewertet.

## 12. Handoff / nächste Aktion

1. #60 setzt fachliche Domain-Profile-SOTA fort – zuerst Diplomatik/Edition.
2. #61 leitet aus dem ersten Profil die kleinste machine-readable Projection und Work-Context-/Method-Application-Struktur ab.
3. #54 implementiert zunächst synthetische Transition-/negative Tests.
4. #50 hält die erforderliche Provenienz als technology-neutral responsibility fest.
5. #55 definiert den Audit Drill-down.
6. #57 ergänzt fresh-context Role/Method/Evidence-Resume.
7. Erst der Thin Slice entscheidet über konkrete Serialisierung/Validator-Technik.
