# Process Learning 2026-09-28 – AI-orchestrierte Capability-Integration / PR #149

**Status:** `critical self-review / process learning / corrected after Owner feedback / no new Requirement, Architecture or Implementation authority`  
**Scope:** kompletter verfügbare Arbeitsverlauf zu PR #149 – von `implementation ready` über Independent Review, Reconciliation, Closure Review und Owner-Korrekturen bis zum Exit aus der Assurance-/Planungsschleife.  
**Primary technical owner:** #48  
**Related:** PR #149, #42, #57, #59, #61, #63  

> Dieses Artefakt bewertet den Entwicklungs-/Orchestrierungsprozess. Es erzeugt keine neue Requirement-, Method-, Architecture-, Merge-, Research-Selection- oder Operational-Admission-Authority.

---

## 1. Ausgangsproblem dieses Workstreams

Der Auftrag dieses Chats war **foundational technical enablement**, nicht historische Fachforschung und nicht die erneute Rekonstruktion des gesamten Histo-Orla-Systembilds.

Das übergeordnete Systembild erklärt das Warum. Der konkrete technische Pain war:

> Histo-Orla braucht belastbare Grundstrukturen, durch die die KI externe bzw. evolvierende Fähigkeiten selbständig, aktuell, authority-sauber, restartbar und ressourceneffizient nutzen und orchestrieren kann, damit der Human Owner nicht Skills, Chats, Versionen, Kontexte und Ausführungswege manuell koordinieren muss.

Der reale erste Pilot ist der in `esany/Wissensarbeit` entwickelte Skill `system-analysis-deep-research`.

Der gewünschte Capability-Pfad war von Anfang an ungefähr:

```text
external capability exists
→ Histo identifies the relevant exact basis
→ Histo binds task / authority / STOP
→ AI uses the capability without owner relay work
→ result returns under Histo authority
→ state remains restartable
→ upstream delta / unavailability remain visible
```

Der Skill ist damit Integrationspilot für eine grundlegende technische Fähigkeit, nicht Produktziel und nicht fachlicher Forschungsgegenstand.

---

## 2. Was am Anfang richtig war

### 2.1 User GO, Assistant Initiative

Richtig war die Trennung:

- KI besitzt Initiative für Analyse, Routing, Vorbereitung und Orchestrierung;
- der Human Owner behält materielle GO-/Admission-Grenzen;
- Analyse-/Review-Auftrag erzeugt keine stille Implementation-/Merge-/Folgephasen-Authority;
- der Owner soll aber nicht für deterministisch lösbare Routing-, Chat-, Skill-, Pfad- oder Validatorentscheidungen zum Operator werden.

### 2.2 Capability-first / Kosten

Richtig war ebenfalls:

```text
normaler Chat + verfügbare Connectoren
= Analyse, Planung, Review, Fresh-State-Checks, Reconciliation

scarce / isolierter Executor
= nur nicht substituierbare filesystem/Git-Isolation, Mutation, lokale Tests
```

Das Problem entstand später nicht aus dieser Trennung selbst, sondern daraus, dass wir Executor-Tokens stärker optimierten als Owner-Aufwand und Time-to-Working-Capability.

### 2.3 Ein realer Pilot statt abstrakter Plattform

Richtig war, einen konkreten reviewed-but-unmerged Skill-Stand aus Wissensarbeit zu verwenden und dabei Histo-Authority, upstream maturity und Generic Fit strikt zu trennen.

---

## 3. Entwickelte Lösungsansätze und heutige Disposition

### 3.1 Generischer Binding-/Compatibility-Core

Frühe Hypothese:

- Binding Contract;
- JSON Schema;
- Compatibility Evaluator;
- persistenter Binding/Registry-State.

**Review-Ergebnis:** zu früh generalisiert. Existing Histo Work Context / Work Order deckt bereits Owner, Scope, Refs, MAY/MUST NOT, STOP, Persistence und Basis-Revalidation ab.

**Disposition:** `reject/defer`.

### 3.2 Trial Admission vs. Operational Admission

Wertvolle Korrektur:

```text
UPSTREAM REVIEWED
→ LOCAL TRIAL ADMISSION
→ bounded real trial
→ review
→ LOCAL OPERATIONAL ADMISSION | adapt | reject | unresolved
```

Upstream Review ist Evidence über den Upstream, keine Histo-Authority. Trial Admission erlaubt Prüfung, ohne positive Operational/Generic Compatibility vorwegzunehmen.

### 3.3 Fresh upstream statt pseudo-current State

Beibehalten:

- Tracking Identity darf persistent sein;
- datierte Observation darf persistent sein;
- `current upstream` wird bei consequential use frisch resolved;
- Delta/Staleness kann deterministisch erkannt werden;
- semantische Compatibility/Admission bleibt Review-/Authority-Sache.

### 3.4 Exact Availability Derivative

Die Restartability-Frage führte zu einer kleinen lokalen, provenance-erhaltenden Kopie des exact reviewed Runtime-Pakets.

Der Closure Review bestätigte die Grundidee, aber schärfte ihre Reichweite:

- sie sichert die **recoverable Skill/source-package basis**;
- sie sichert nicht AI-/Research-Provider, Credentials, Quoten oder externe Quellen;
- lokale Integrität soll über vorhandene Git-Blob-Basis-Revalidation geprüft werden;
- alle drei Dateien bleiben aus exact reviewed-package fidelity erhalten, nicht weil das ChatGPT-Profil vendor-neutral Core wäre.

**Disposition:** als konkreter Pilotbestandteil beibehalten; keine Vendor-/Mirror-/Registry-Plattform daraus ableiten.

### 3.5 E0/P0 – generische Create-Target-Erweiterung

Aus einer Einschränkung des optionalen bounded-execution Validators wurde fälschlich ein vorgelagerter Infrastrukturbedarf abgeleitet.

Der Closure Review zeigte:

> Die Validator-Grenze ist keine Projektinvariante. Ein konkreter reversibler Create-Slice kann über Owner Authority / Work Context + isolierte Git-Surface + exact absent target paths + changed-file/diff checks gebunden werden.

**Disposition:** `remove from critical path`.

Kein generischer Create-Target-Contract/Schema/Validator wird für diesen Pilot gebaut.

### 3.6 Isolierte Implementation Surface

Beibehalten:

```text
fresh isolated checkout/worktree oder nachweislich äquivalent
→ exact admitted basis
→ branch-scoped mutation
→ same-checkout verification
→ exact changed-file check
→ diff review
→ delta-only return
```

Das adressiert ein reales Safety-Problem und ist keine bloße Meta-Zeremonie.

---

## 4. Wo der Prozess entgleiste

### 4.1 Goal Substitution

Das Outcome hätte durchgehend sichtbar bleiben müssen:

> Histo kann eine externe Capability ohne manuelle Owner-Orchestrierung kontrolliert benutzen und restartbaren State hinterlassen.

Stattdessen wurde der jeweils aktuelle Teilmechanismus nacheinander zum Hauptproblem:

```text
Capability Integration
→ Binding
→ Admission
→ Availability
→ Snapshot
→ Create Target
→ Validator
```

Lokale technische Sauberkeit nahm zu; `time-to-working-capability` nahm ab.

### 4.2 Assurance Recursion

Sinnvoll war ein einmaliger unabhängiger Challenge vor teurer Implementation.

Entgleist ist daraus:

```text
Plan A
→ Independent Review
→ Plan B
→ Plan B ist neu
→ Closure Review
→ Plan C nötig
→ potentiell wieder Review
```

Assurance hatte kein eigenes Kosten-/Stop-Kriterium.

### 4.3 Owner-Burden-Blindheit

Der Owner wurde faktisch zum Postboten:

```text
Handoff-Prompt holen
→ neuen Chat starten
→ Review transportieren
→ Reconciliation auslösen
→ nächsten Review transportieren
```

Damit reproduzierte der Prozess genau den Orchestrierungs-Pain, den die technische Capability reduzieren soll.

Die Bereitschaft des Owners, gelegentlich kleine Handoff-Prompts zu nutzen, wurde fälschlich als Präferenz für dauerhaftes Human-in-the-loop Chat-Routing interpretiert.

### 4.4 Falsche Überkorrektur

Nach der Kritik an der Meta-Schleife wurde der Scope anschließend zu weit zum gesamten Systembild bzw. sogar zu historischen Fachfragen verschoben.

Das war erneut Abstraktionsdrift.

**Korrekte Arbeitsebene:** foundational technical enablement.

### 4.5 Closure Pressure

Ein zusätzlicher Root Cause war der Drang, einen scheinbar vollständigen, entscheidungsreifen Plan präsentieren zu wollen.

Dadurch wurden offene Stellen zu oft durch neue Interpretation, zusätzliche Architektur oder weitere Review-Gates gefüllt, statt sie als offene Stellen sichtbar zu lassen.

---

## 5. Owner-Korrektur zur Unsicherheit

Die frühere Formulierung, Unsicherheit müsse „beherrschbar gemacht“ werden, war falsch.

Der Owner hat ausdrücklich korrigiert:

> Es geht nicht darum, Unsicherheit zu beherrschen. Sie soll transparent gemacht und zugelassen werden. Sie darf nicht mit Interpretationen gefüllt werden, nur damit eine Lösung präsentiert werden kann.

Daraus folgt für diesen Prozess:

```text
Unsicherheit
→ sichtbar machen
→ Herkunft / Reichweite benennen
→ konkurrierende Lesarten erhalten
→ unresolved zulassen
→ Claim-/Handlungsreichweite entsprechend begrenzen
→ nur durch zusätzliche Evidenz / explizite Authority weiter verdichten
```

Wichtig:

- `unresolved` ist kein Prozessversagen;
- fehlende Evidenz ist kein Auftrag, eine plausible Lücke zu füllen;
- konkurrierende Lesarten müssen nicht harmonisiert werden;
- eine offene reversible Frage ist nicht automatisch ein Implementation-Blocker;
- ein Pilot darf offene Fragen **mitführen und sichtbar testen**, ohne vorab eine Antwort zu behaupten;
- Planung darf nicht aus dem Wunsch nach Closure zusätzliche Semantik erfinden.

Der richtige Gegensatz ist daher nicht `uncertainty → control`, sondern:

> **false closure vermeiden; Unsicherheit transparent erhalten.**

---

## 6. Root Causes

### RC-01 – Abstraktionsdrift

Systembild, Capability-Increment und Implementierungsmechanismus wurden nicht stabil getrennt.

### RC-02 – Goal Substitution

Teilmechanismen ersetzten schrittweise das End-to-End-Ziel.

### RC-03 – Assurance ohne Stop-Kriterium

Review wurde als grundsätzlich risikosenkend behandelt, ohne Rekursions- und Owner-Kosten zu berücksichtigen.

### RC-04 – Unknowns wurden zu leicht zu Blockern

Offene Fragen wurden zu oft in `must resolve before implementation` übersetzt.

### RC-05 – Closure Pressure / Interpretation Fill

Offene Stellen wurden mit plausibler technischer Semantik gefüllt, um einen vollständigen Plan zu erzeugen.

### RC-06 – lokale Optimierung

Teilsemantik wurde sauberer, während das funktionierende End-to-End-Increment weiter wegrückte.

### RC-07 – falsche Ressourcenmetrik

Scarce Executor Tokens wurden stark optimiert; Human Attention, Context Switching, Owner Routing und Time-to-Value zu schwach.

### RC-08 – fehlende Outcome-Revalidation

Nach Revisionen fehlte wiederholt die Frage:

> Was kann Histo nach diesem Increment real, was es vorher nicht konnte?

---

## 7. Prozessheuristiken – Review Input, keine neue Governance

### L-01 – Outcome Anchor

Jeder technische Workstream behält einen sichtbaren end-to-end Outcome. Teilmechanismen dürfen ihn nicht ersetzen.

### L-02 – Unsicherheit transparent, nicht künstlich schließen

Ein Unknown wird beschrieben, begrenzt und – falls nötig – als `unresolved` mitgeführt. Es wird nicht durch Interpretation gefüllt, nur um einen scheinbar vollständigen Plan zu erzeugen.

### L-03 – Blocker nur bei echter Vorbedingung

Vor Implementation muss eine Frage nur dann geklärt werden, wenn ihr Offenlassen den nächsten Versuch unaussagekräftig macht oder nicht akzeptablen irreversiblen, Authority-, Rights-, Security- oder State-Loss-Schaden erzeugen kann.

Andere offene Fragen dürfen als explizite Acceptance-/Falsification-Fragen in einen kleinen reversiblen Pilot gehen.

### L-04 – Assurance Budget / Stop Rule

Nach einem hinreichenden Independent Review und dessen Disposition löst eine subtraktive oder klar non-blocking Revision **nicht automatisch** einen weiteren Fresh Review aus.

Ein weiterer unabhängiger Review braucht einen konkreten neuen materiellen irreversiblen/Authority-/Safety-Risikotyp.

### L-05 – Tooling ist Mittel, nicht Gateway

Eine Grenze eines vorhandenen Validators/Contracts wird nicht automatisch zur Projektvoraussetzung.

### L-06 – Owner Burden ist Qualitätsdimension

Ressourcenökonomie betrachtet gemeinsam:

- scarce execution cost;
- Human Attention;
- manuelle Handoffs;
- Context loss;
- Rework risk;
- Time-to-Working-Capability.

### L-07 – Handoff nur bei echtem Mehrwert

Handoff nur bei realer Capability-Lücke, notwendiger Isolation, Rights-/Safety-Grenze oder materialer unabhängiger Review-Wirkung.

### L-08 – Foundational technical enablement bleibt technical enablement

Der unmittelbare Output muss keine historische Erkenntnis sein. Er muss aber eine reale technische Fähigkeit liefern, die für das Systembild nötig ist.

### L-09 – End-to-End Acceptance

Für diesen Strang ist ein technisches Inkrement erst aussagekräftig, wenn ein frischer Kontext:

1. die externe Capability aus Repo-State identifiziert;
2. exact Basis / Currentness / Authority korrekt unterscheidet;
3. die Capability ohne manuellen Skill-/Prompt-/Kontexttransport des Owners nutzt;
4. ihre STOP-/Authority-Grenzen wahrt;
5. kontrollierten restartbaren State hinterlässt;
6. Upstream-Delta oder Unavailability sichtbar behandelt;
7. offene Fragen nicht durch Interpretation schließt.

---

## 8. No-loss disposition des bisherigen PR-#149-Learnings

**Beibehalten:**

- exact upstream identity;
- fresh upstream resolution;
- Trial Admission ≠ Operational Admission;
- Skill-/Upstream-Review ≠ Histo Authority;
- keine Generic-Fit-Behauptung;
- isolated implementation surface;
- exact source provenance / package fidelity;
- Git-Blob-Revalidation vorhandener lokaler Basis;
- AI-owned Orchestration als Acceptance-Dimension.

**Verworfen/deferred:**

- generische Binding Registry;
- Compatibility Evaluator;
- pseudo-current Upstream Store;
- generischer Agent-/Workflow-Layer;
- E0/P0 Create-Target-Infrastruktur für diesen Pilot;
- weitere Review-Kaskade ohne neuen materiellen Risikotyp.

**Offen und zulässig:**

- ob der lokale Availability Derivative langfristig die richtige Preservation-Form bleibt;
- welche zusätzliche Generalisierung erst nach weiteren realen Consumern sinnvoll wird;
- welche Provider-/Execution-Limits beim Trial auftreten;
- ob der Skill für den konkreten lokalen Einsatz nach Trial beibehalten, angepasst, verworfen oder `unresolved` bleibt.

Diese offenen Punkte sind bewusst **nicht** mit vorweggenommenen Lösungen gefüllt.

---

## 9. Abschluss-Learning

Der zentrale Fehler dieses Workstreams war nicht zu wenig Governance, sondern die Kombination aus Goal Substitution, Assurance-Rekursion und Closure Pressure.

Die Korrektur lautet:

> **Nicht Unsicherheit beseitigen oder beherrschen. Unsicherheit transparent erhalten. Nur die Vorbedingungen schließen, die für den nächsten sicheren und aussagekräftigen Schritt tatsächlich notwendig sind. Dann reale technische Fähigkeit liefern und anhand realer Nutzung lernen.**
