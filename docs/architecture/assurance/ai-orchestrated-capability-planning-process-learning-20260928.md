# Process Learning 2026-09-28 – AI-orchestrierte Capability-Integration / PR #149

**Status:** `critical self-review / process learning / no new Requirement, Architecture or Implementation authority`  
**Scope:** der vollständige verfügbare Arbeitsverlauf zur Planung von PR #149 – von `implementation ready` über Independent Review, Review-Reconciliation und Closure Review bis zur Owner-Korrektur, dass Assurance/Chat-Orchestrierung selbst zum Fortschrittshemmnis geworden ist.  
**Primary technical owner:** #48  
**Related:** PR #149, #57, #59, #61, #63  
**Important boundary:** Dieses Artefakt bewertet den Entwicklungs-/Orchestrierungsprozess und hält daraus abgeleitete Learnings fest. Es entscheidet weder den offenen PR-#149-Plan noch einen Work Order, keine Architecture Promotion, keine Implementation Admission und keine fachliche Research Selection.

---

## 1. Warum dieses Learning existiert

Der Arbeitsauftrag dieses Chats war **technisches Enablement**, nicht historische Fachforschung und nicht eine neue Rekonstruktion des gesamten Histo-Orla-Systembilds.

Das Systembild ist das übergeordnete Warum: Histo-Orla soll als private, transdisziplinäre historische Forschungsassistenz belastbare Quellenarbeit, fachliche Problemübersetzung, Methoden, Analyse und restartbaren Research State unterstützen.

Der konkrete technische Pain dieses Arbeitsstrangs war enger:

> Histo-Orla benötigt belastbare Grundstrukturen, durch die die KI externe bzw. evolvierende Fähigkeiten selbständig, aktuell, authority-sauber, restartbar und ressourceneffizient nutzen und orchestrieren kann, damit der Human Owner nicht länger Skills, Chats, Versionen, Kontexte und Ausführungswege manuell koordinieren muss.

Der reale erste Pilot hierfür war der in `esany/Wissensarbeit` entwickelte Skill `system-analysis-deep-research`.

Dieses Learning wurde notwendig, weil der Planungs-/Assurance-Prozess genau die Owner-Belastung reproduzierte, die die technische Capability eigentlich reduzieren sollte.

---

## 2. Was am Anfang korrekt verstanden war

### 2.1 Capability statt einzelner Dateikopie

Das technische Ziel war nicht lediglich, einen externen Skill lokal zu speichern.

Der angestrebte Capability-Pfad war sinngemäß:

```text
externe Capability existiert
→ Histo kann sie eindeutig identifizieren
→ relevanten / zulässigen Stand bestimmen
→ Histo-Authority und Scope binden
→ Capability im Work Context benutzen
→ KI orchestriert die Ausführung
→ Ergebnis kontrolliert zurückführen
→ Zustand restartbar halten
→ Upstream-Delta / Unavailability sichtbar behandeln
```

Damit ist der externe Skill ein **realer Integrationspilot für foundational technical enablement**, nicht das Produktziel selbst.

### 2.2 User GO, Assistant Initiative

Richtig war auch die Authority-Idee:

- die KI soll Analyse, Routing, Vorbereitung und Orchestrierung übernehmen;
- der Human Owner soll materielle GO-/Admission-Grenzen behalten;
- ein Analyse- oder Review-Auftrag darf nicht still Implementation/Merge/Folgephasen autorisieren;
- der Owner soll aber auch nicht für deterministisch lösbare Routing-, Chat-, Skill-, Pfad- oder Validatorentscheidungen zum Operator werden.

### 2.3 Capability-first und Ressourcenökonomie

Richtig war ebenfalls:

```text
normaler Chat / verfügbare Connectoren
= Analyse, Planung, Review, Reconciliation, Fresh-State-Checks

scarce / isolierter Executor
= nur dort, wo nicht substituierbare Filesystem-/Git-Isolation, Mutation und lokale Tests benötigt werden
```

Das sollte knappe Execution-Ressourcen sparen und gleichzeitig unnötige Context Switches vermeiden.

---

## 3. Entwickelte Lösungsansätze und heutige Einordnung

### 3.1 Generischer External-Skill Binding Core

Frühe Hypothese:

- Binding Contract;
- JSON Schema;
- Compatibility Evaluator;
- persistenter Binding Record / Registry-artige Projektion.

Ziel war, Tracking Identity, exact upstream basis, lokale Review-Basis und Delta/Compatibility sichtbar zu halten.

**Review-Learning:** für den ersten Pilot übergeneralisiert. Existing Histo Work Context / Work Order kann bereits Authority, Scope, Refs, MAY/MUST NOT, STOP, Persistence und Basis-Revalidation tragen. Ein generischer Registry-/Evaluator-Layer war nicht als kleinstes notwendiges Mittel bewiesen.

**Disposition im bisherigen Plan:** `reject/defer`.

### 3.2 Trial Admission vs. Operational Admission

Der erste Plan enthielt eine zirkuläre Semantik: ein noch nicht lokal geprüfter Skill sollte durch genau den Trial lokal legitimiert werden, für dessen Start er scheinbar bereits positive Compatibility benötigte.

Die korrigierte Trennung ist wertvoll:

```text
UPSTREAM REVIEWED
→ LOCAL TRIAL ADMISSION
→ bounded real trial
→ review
→ LOCAL OPERATIONAL ADMISSION | adapt | reject | unresolved
```

Upstream Review bleibt externe Evidence und erzeugt keine Histo-Authority. Trial Admission darf genau den Test erlauben, ohne vorher Operational/Generic Compatibility zu behaupten.

### 3.3 Fresh upstream statt pseudo-current State

Ebenfalls beizubehalten:

- Tracking Identity darf persistent sein;
- dated Observation darf persistent sein;
- `current upstream` wird bei consequential use frisch resolved;
- Ref-/Status-Delta kann deterministisch sichtbar werden;
- positive semantische Compatibility/Admission bleibt Review-/Authority-Evidence.

### 3.4 Immutable Availability Derivative

Aus der Restartability-/Provider-Loss-Frage entstand die Hypothese, einen exact frozen, execution-sufficient Upstream-Basisstand lokal mit Provenienz zu erhalten.

Der Closure Review bewertete die Grundidee positiv, präzisierte aber:

- sie garantiert recoverable **Skill/source-package basis**, nicht die fortdauernde Verfügbarkeit eines AI-/Research-Providers;
- local integrity kann mit vorhandener Git-Blob-Basis-Revalidation geschützt werden;
- der environment-specific ChatGPT profile bleibt aus exact reviewed-package fidelity erhalten, nicht weil er vendor-neutral Core wäre.

**Wichtiges Prozess-Learning:** selbst eine technisch plausible Restartability-Maßnahme darf nicht automatisch zur zwingenden Precondition für jeden ersten reversiblen Capability-Trial werden. Ihre Stellung muss gegen den tatsächlich benötigten Increment geprüft werden.

### 3.5 P0 / generische Create-Target-Erweiterung

Aus einer Einschränkung des bounded execution validators – deklarierte Scope-Dateien müssen heute bereits existieren – wurde P0 abgeleitet: generische `create_files`-Semantik in Contract/Schema/Validator/Tests.

Der Closure Review zeigte:

> Diese Einschränkung des optionalen Validators ist keine Projektinvariante und macht generische Create-Target-Infrastruktur für einen einzelnen E1-Run nicht automatisch notwendig.

Ein konkreter reversibler Create-Run kann durch bestehenden Work Context / Owner Authority plus isolierte Git-/Filesystem-Surface, exact pre-bound absent target paths, fail-if-present, exact changed-file check und Diff Review gebunden werden.

**Learning:** ein bestehender Hilfsmechanismus darf nicht unbemerkt zum mandatory gateway werden, nur weil der geplante Slice sonst nicht durch genau diesen Mechanismus passt.

### 3.6 Isolierte Implementation Surface

Weiterhin ein valider technischer Schutz:

```text
fresh isolated checkout/worktree oder nachweislich äquivalent
→ exact admitted basis
→ branch-scoped mutation
→ same-checkout tests
→ exact changed-file check
→ diff review
→ delta-only return
```

Dies adressiert ein reales Risiko: direkte GitHub-Contents-/Connector-Writes können lokale Mutation Guards umgehen. Isolation ist daher eine echte Capability-/Safety-Eigenschaft und kein bloßes Meta-Gate.

---

## 4. Wo der Prozess entgleiste

### 4.1 Goal Substitution

Das eigentliche technische Acceptance-Ziel hätte durchgehend lauten müssen:

> Histo kann eine externe Capability ohne manuelle Owner-Orchestrierung kontrolliert benutzen und den Zustand nachvollziehbar/restartbar weiterführen.

Stattdessen wurde der jeweils aktuelle Teilmechanismus schrittweise zum neuen Hauptproblem:

```text
Capability Integration
→ Binding
→ Admission
→ Availability
→ Snapshot
→ Create Target
→ Validator
```

Jeder Schritt war lokal begründbar. Global sank jedoch `time-to-working-capability`.

### 4.2 Assurance Recursion

Die ursprüngliche sinnvolle Idee war:

> einmal unabhängig challengen, damit teure Implementation nicht auf einer grob falschen Annahme startet.

Tatsächliche Dynamik:

```text
Plan A
→ Independent Review
→ Plan B

Plan B ist materiell neu
→ Closure Review
→ Finding gegen Plan B
→ Plan C nötig

Plan C wäre erneut materiell verändert
→ potentiell weiterer Review
```

Es fehlte ein Closure-Kriterium für Assurance selbst.

### 4.3 Risk Flattening

Reversible Unsicherheit und echte irreversible/kritische Zustände wurden zu ähnlich behandelt.

Dadurch wanderte zu viel Arbeit vor die Implementation.

Besserer Unterschied:

**Pre-Implementation-Blocker** nur wenn Nichtklärung u. a. zu folgendem führen kann:

- nicht akzeptabler irreversibler State-/Datenverlust;
- unautorisierte consequential Mutation/Promotion;
- nicht rekonstruierbarer oder nicht aussagekräftiger Versuch;
- nicht beherrschbarer Scope-/Rights-/Security-Schaden.

**Pilot-/Acceptance-Frage**, wenn:

- der Zustand reversibel ist;
- der Versuch observierbar/falsifizierbar ist;
- die Unsicherheit gerade durch reale Nutzung besser beantwortbar ist als durch weitere Planung.

### 4.4 Owner-Burden-Blindheit

Der Prozess optimierte knappe Work/Codex-/Executor-Ressourcen, aber zu wenig:

- Human Attention;
- Context Switching;
- Chat-Orchestrierung;
- Time-to-Working-Capability.

Der Human Owner wurde faktisch zum Postboten:

```text
Handoff-Prompt holen
→ frischen Chat starten
→ Review ausführen lassen
→ Ergebnis zurücktransportieren
→ Reconciliation triggern
→ nächsten Review transportieren
```

Damit reproduzierte der Prozess den Pain, den die Capability reduzieren soll.

### 4.5 Falsche Auslegung eines Owner-Angebots

Der Owner sagte sinngemäß, dass kleine Handoff-Prompts für neue normale Chats bei überschaubarer Arbeit akzeptabel seien.

Das wurde zu stark als allgemeines Orchestrierungsmodell interpretiert.

**Learning:** Bereitschaft zu gelegentlichen manuellen Handoffs ist keine Präferenz, dauerhaft Human-in-the-loop Chat-Routing zu übernehmen.

### 4.6 Überkorrektur nach Owner-Kritik

Nach der Kritik an Review-/Planungsschleifen wurde zunächst korrekt erkannt, dass Assurance selbst zum Blocker geworden war.

Danach erfolgte jedoch eine falsche Abstraktionsverschiebung zum gesamten Histo-Orla-Systembild und sogar zur Idee, wieder einen historischen Forschungsfall zu wählen.

Das war erneut Scope Drift.

**Korrekte Ebene:** foundational technical enablement.

Das Systembild erklärt das Warum; dieser Workstream soll belastbare technische Grundstrukturen liefern, damit spätere Fachforschung nicht weiterhin an Tooling-/Orchestrierungsproblemen hängen bleibt.

---

## 5. Root Causes des Assistenz-/Planungsfehlers

### RC-01 – Abstraktionsdrift

Systembild, technischer Capability-Increment und konkrete Implementierungsmechanismen wurden nicht stabil getrennt.

### RC-02 – Goal Substitution

Der aktuelle Submechanismus wurde zum neuen Hauptziel, ohne ihn erneut gegen den ursprünglichen technischen Outcome zu prüfen.

### RC-03 – Assurance ohne eigenes Budget/Stop-Kriterium

Review wurde als grundsätzlich risikosenkende Maßnahme behandelt, ohne dessen eigene Kosten und Rekursionsrisiko zu begrenzen.

### RC-04 – Blockerbegriff zu breit

`unknown` wurde zu oft in `must resolve before implementation` übersetzt.

### RC-05 – lokale Optimierung

Einzelne technische Semantiken wurden immer sauberer, während der Gesamtpfad zu einer funktionierenden Capability langsamer wurde.

### RC-06 – falsche Ressourcenmetrik

Scarce executor tokens wurden stark optimiert; Human Attention / Owner Routing Burden / Time-to-Value zu schwach.

### RC-07 – fehlende End-to-End-Outcome-Revalidation

Nach jeder größeren Planrevision fehlte die harte Frage:

> Was kann Histo nach diesem Increment real, was es vorher nicht konnte?

---

## 6. Zukünftige Arbeitsheuristiken aus diesem Learning

**Status:** Prozessheuristiken / Review Input; keine neue Governance oder Requirement Authority.

### L-01 – Outcome Anchor vor Submechanismus

Jeder technische Workstream braucht einen sichtbaren End-to-End Outcome.

Für diesen Strang:

> Ein frischer Histo-Kontext kann eine konkrete externe Capability identifizieren, zulässigen Stand/Authority binden, sie ohne manuellen Skill-/Kontexttransport des Owners benutzen und restartbaren kontrollierten State zurücklassen.

Teilmechanismen sind nur dann blocking, wenn sie für genau diesen Outcome vor dem nächsten sicheren realen Versuch tatsächlich erforderlich sind.

### L-02 – Assurance Budget / Stop Rule

Ein Independent Review kann vor consequential/teurer Implementation sinnvoll sein.

Nach Review-Reconciliation gilt jedoch standardmäßig:

- neue **subtraktive** oder klar non-blocking Refinements lösen nicht automatisch einen neuen unabhängigen Review aus;
- ein weiterer Fresh Review braucht einen konkreten neuen catastrophic/irreversible-risk trigger;
- Assurance selbst muss gegen Owner Burden und Time-to-Working-Capability gerechtfertigt werden.

### L-03 – Reversible Unknowns in den Pilot

Wenn ein Unknown durch einen kleinen isolierten/reversiblen Versuch besser beantwortet wird und kein unacceptable-loss-Risiko erzeugt, wird er als Acceptance-/Falsification-Frage in den Pilot verschoben statt als Planungsblocker behandelt.

### L-04 – Tooling ist Mittel, nicht Gateway

Bestehende Validatoren/Contracts sind Hilfsmittel. Ihre aktuelle technische Grenze darf nicht ohne separate Begründung zur Projektvoraussetzung werden.

### L-05 – Owner Burden ist eine echte Qualitätsdimension

Ressourcenökonomie muss mindestens gleichzeitig betrachten:

- scarce execution cost;
- Human Attention;
- Anzahl manueller Handoffs;
- Context loss;
- Rework risk;
- Time-to-Working-Capability.

### L-06 – Handoff nur bei echtem Mehrwert

Ein neuer Chat/Executor ist nur gerechtfertigt durch:

- echte Capability-Lücke;
- notwendige Isolation;
- unabhängige Review-Eigenschaft mit materialer Risikoreduktion;
- Rechte-/Safety-Grenze.

Nicht allein, weil die Aufgabe theoretisch in einem anderen Kontext sauberer aussehen würde.

### L-07 – Foundational Technical Enablement ≠ Fachforschung

Für technische Grundstrukturen ist reale fachliche Erkenntnis nicht zwingend der unmittelbare Increment-Output.

Der Increment muss aber eine **reale technische Fähigkeit** liefern, die für das Systembild erforderlich ist und die vorher nicht belastbar vorhanden war.

### L-08 – Trial/Use ist Teil von Delivery

Ein Capability-Increment endet nicht bei Dokument/Schema/Snapshot/Validator.

Es braucht einen realen technischen Gebrauchstest:

```text
identify
→ bind
→ execute
→ return
→ resume
→ detect delta/failure
```

Erst dieser Pfad kann zeigen, ob die Grundstruktur funktioniert.

---

## 7. Was aus PR #149 als wertvoll erhalten bleibt

Die bisherigen Schleifen waren nicht vollständig verlorene Arbeit. Sie haben mehrere übergroße Kandidaten eliminiert und echte Invarianten geschärft.

Beibehalten bzw. ernsthaft weiterzuverwenden:

- kein generischer Binding-/Registry-/Compatibility-Core ohne reale wiederholte Friktion;
- `upstream reviewed ≠ local trial admitted ≠ local operationally admitted`;
- current upstream bei consequential use fresh resolve;
- Ref-/Lineage-/Staleness-Checks dürfen deterministisch sein, semantische Compatibility nicht;
- isolierte Git-/Filesystem-Execution bei echter Mutation;
- AI-owned Orchestration / Owner nicht als Chat Router;
- Trial/Resume/Delta/Unavailable-Falsifikation als echte Capability-Acceptance.

Nicht allein aufgrund dieses Learning-Artefakts entschieden:

- ob/wann eine lokale Availability Derivative zwingend vor dem ersten Trial benötigt wird;
- die endgültige PR-#149-Readiness;
- konkrete Implementation Scope/Work Order;
- Trial Admission oder Operational Admission.

---

## 8. Aktueller Handoff nach diesem Learning

Dieses Artefakt selbst verändert den aktuellen Implementation-/Readiness-State **nicht**.

Zum Zeitpunkt seiner Erstellung gilt weiterhin der auf PR #149 persistierte Stand; der zuletzt im Chat gelieferte Closure Review ist separate Review-Evidence und muss vor einer kanonischen Plan-/Readiness-Änderung noch projektseitig dispositioniert werden.

Die nächste Reconciliation soll deshalb nicht erneut den gesamten System-/Intent-Raum aufrollen, sondern drei Dinge gleichzeitig bewahren:

1. **technischer Workstream bleibt foundational capability enablement**;
2. **bereits gewonnene Review-Evidence reduziert unnötige Infrastruktur**;
3. **Assurance darf den realen, reversiblen Capability-Lernzyklus nicht erneut verdrängen**.

Leitfrage für den nächsten Schritt:

> Welche kleinste sichere technische Änderung erlaubt jetzt einen aussagekräftigen end-to-end Capability-Trial, ohne den Human Owner wieder zum Orchestrator zu machen?

---

## 9. Learning in einem Satz

> **Blockerprävention ist nur dann Fortschritt, wenn sie einen realen technischen Lern-/Delivery-Schritt sicherer macht; sobald Assurance selbst den Owner zum Workflow-Router macht oder reversible Unknowns dauerhaft vor die Implementation zieht, reproduziert sie den Pain, den das technische Enablement eigentlich beseitigen soll.**
