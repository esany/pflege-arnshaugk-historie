# Histo-Orla – AI-Resilience Root-Cause Audit

**Status:** `audit / review-input / no requirement-or-implementation-authority`  
**Work Owner:** #70  
**Interfaces:** #64, #42, #24, #48, #50, #54, #61, #62, #63  
**Stand:** 2026-09-03  
**Structural prior art:** `esany/Wissensarbeit` (generic project handling only; no Histo-Orla semantic authority)

## 1. Zweck und Arbeitsregel

Dieser Audit prüft nicht, ob Histo-Orla möglichst viele Schutzregeln besitzt. Er rekonstruiert reale oder plausible KI-/System-Failure-Modes rückwärts:

```text
observed phenomenon / evidence
→ symptom
→ original motivation
→ protected goal
→ root cause
→ current relevance + dependencies
→ actual enforcement
→ smallest effective intervention
→ disposition of active rule/governance
```

Problemstatus und Regelstatus bleiben getrennt:

- Problem: `confirmed-current | conditional | historical-only | unproven | superseded-by-structure`
- Regel/Mechanismus: `retain | refine | narrow | merge | derive | replace | retire-active | defer`

Die operative Reaktion wird erst nach der Ursachenanalyse bestimmt: `BLOCK | HOLD | REDIRECT | ESCALATE`.

Dieses Artefakt ist der eine versionierte Audit-Ort für #70; einzelne Slices sollen keine neue Meta-Artefaktfamilie erzeugen.

---

# 2. Slice 1 – Canonical Mutation / Authority

## 2.1 Kurzurteil

Der aktuelle Stand zeigt **keine primäre Requirement-Lücke**, sondern eine deutliche Differenz zwischen bereits starker Schutzsemantik und realer Ausführung:

1. Histo-Orla hat Candidate-vs.-Canonical, History-Erhalt, AI-non-evidence und deterministische Promotion Guards bereits in akzeptierten Requirements und Architekturverträgen angelegt.
2. Die allgemeine `transition`-Capability für Research-State-Mutation ist weiterhin `planned`; #54 ist nicht implementiert.
3. `main` ist am 2026-09-03 nicht geschützt; der Repository-Ruleset-Endpunkt liefert keine Rulesets.
4. Der einzige GitHub-Workflow `Project Assurance` ist deshalb keine verpflichtende Pre-Promotion-Grenze. Er läuft nur für ausgewählte Pfade und **nicht** für `PROJECT_STATE.md`, `README.md` oder `docs/research/cases/**`.
5. Die #63 Changed-Code-Policy kontrolliert nur technische Pfade (`src/**`, `app/**`, `histo_orla/**`, `tools/**`, `tests/**`, `.github/workflows/**`) – nicht Project State, Requirements-/Governance-Semantik oder historische Research-State-Artefakte.
6. Ein realer Histo-Orla-Vorfall am 2026-09-03 belegt, dass ein AI-gestützter Full-File-Replace gültigen kanonischen Handoff-State auf `main` löschen konnte, bevor der Fehler durch Diff-Inspektion erkannt und korrigiert wurde.

Damit sind **Repo-/Project-State-Mutation** und **wissenschaftliche Research-State-Transition** verwandte, aber nicht identische Probleme. Beide schützen History/Authority Integrity, brauchen jedoch unterschiedliche technische Grenzen.

---

## 2.2 Evidence Register

| ID | Typ | Evidenz | Aussage |
|---|---|---|---|
| E-AM-001 | observed Histo failure | Commit `ca4118fb7e6cfa04ed6ac6f0e10a1d35f03ec82c` | Bounded beabsichtigte Änderung von `PROJECT_STATE.md` führte zu massiver unbeabsichtigter Löschung nachgelagerter Abschnitte. |
| E-AM-002 | observed recovery | Commit `c01a59e3c606bf38e3b251c21e50a1647d6f034c` | Vorgängerinhalt wurde aus Git rekonstruiert und vollständig wiederhergestellt; Git half bei Recovery, verhinderte den Schaden aber nicht. |
| E-AM-003 | current repo state | `GET /repos/esany/pflege-arnshaugk-historie/branches/main` | `protected:false`; required status checks `off`. |
| E-AM-004 | current repo state | `GET /repos/esany/pflege-arnshaugk-historie/rulesets` | keine Repository-Rulesets. |
| E-AM-005 | current CI | `.github/workflows/project-assurance.yml` | Workflow existiert, überwacht aber weder `PROJECT_STATE.md`/`README.md` noch `docs/research/cases/**`. |
| E-AM-006 | observed CI absence | Actions query für Head SHA `ca4118...` | für den schädlichen `PROJECT_STATE.md`-Commit existiert kein Workflow-Lauf. |
| E-AM-007 | current enforcement | `tools/operational/enforcement-map.json` | `REQ-WF-001 = partial`; `transition` für `REQ-ENT-001`/`REQ-MTH-004` ist `planned`; keine Rule-Refs. |
| E-AM-008 | current contract | `docs/architecture/contracts/canonical-research-state.md` | Candidate/Working/Promoted/Unresolved/Superseded sowie History-Erhalt und AI-non-evidence sind semantisch explizit. |
| E-AM-009 | current work owner | #54 | Candidate→Review→Promotion und Research-State-Transition sind weiterhin `planned`. |
| E-AM-010 | current trace policy | `tools/assurance/policy.json` | Changed-Code-Guard ist bewusst auf technische Pfade begrenzt. |
| E-AM-011 | historical/project evidence | #9 + `docs/governance/work-context-handoff-audit.md` | Model-/Process-/Authority-Drift wurde bereits als eigene Lücke identifiziert; U2 zeigte gute Persistenz, aber keine flächendeckende Runtime-Garantie. |
| E-AM-012 | accepted requirement | `REQ-WF-001` | Formal prüfbare Invarianten dürfen nicht allein von Prompt-/LLM-Compliance abhängen; adversarial invalid candidate darf Promotion nicht erzwingen. |

**Evidenzklassifikation:** `E-AM-001/002/006` sind echte Histo-Orla-Laufereignisse. `E-AM-003/004/005/007/009/010` sind aktuelle strukturelle Zustände. Die ursprüngliche Candidate→Promotion-Idee aus #39/#24 ist überwiegend SOTA-/Risiko-/Architekturableitung und darf nicht rückwirkend als historisch beobachteter Histo-Schadensfall ausgegeben werden.

---

# 3. Root-Cause Cases

## AM-01 – Bounded edit wird zum destruktiven Full-File-Replace

### Observed phenomenon

Am 2026-09-03 sollte `PROJECT_STATE.md` nur um einen kleinen Audit-/Review-Pointer ergänzt werden. Commit `ca4118...` änderte darüber hinaus den Dateischwanz massiv und löschte gültige Handoff-/Next-Action-/Blocker-Inhalte. Commit `c01a59...` stellte sie aus dem direkten Git-Vorgänger wieder her.

### Symptom

`kleines Delta gewollt → große kanonische Mutation ausgeführt`.

### Protected goal

- Verlustfreiheit des kanonischen Projekt-/Handoff-State;
- rekonstruierbare Research-/Project History;
- Fortsetzbarkeit ohne Chat;
- Nutzerentlastung: der Owner soll nicht jede Routine-Dateioperation kontrollieren müssen.

### Root cause

Nicht primär „KI war unvorsichtig“, sondern eine Kombination aus Ausführungs- und Authority-Design:

1. **Operation mismatch:** Für eine kleine Änderung wurde eine API benutzt, die den vollständigen Dateiinhalt ersetzt.
2. **No bounded-mutation guard:** Der gültige Vorgänger-SHA schützt gegen konkurrierende Stale Writes, aber nicht gegen einen semantisch destruktiven Replace auf genau diesem Vorgänger.
3. **No pre-promotion diff/loss gate:** Es gab keine mechanische Grenze, die bei einer als bounded deklarierten Änderung unerwartete Löschungen blockiert.
4. **Immediate canonical write:** Die Änderung ging direkt auf `main`; Diff-Review war nur nachgelagerte Fehlererkennung.
5. **Path not assured:** `PROJECT_STATE.md` löst den aktuellen Assurance-Workflow nicht aus.

### Current relevance

`confirmed-current`.

Die gleiche Full-Replace-Fähigkeit besteht weiterhin; Git-Recovery reduziert Folgen, verhindert aber keinen temporär falschen kanonischen State.

### Existing basis

- `AGENTS.md`: kein Handoff-/State-Verlust; one fact / one canonical home; `PROJECT_STATE.md` als zentrale Handoff-Sicht.
- `REQ-STATE-001`: chat-/providerunabhängiger, recoverable State.
- `REQ-WF-001`: deterministische formale Schutzgrenzen nicht als Promptpflicht.
- #24: Dateiintegrität, Versionierung, Status/State und kanonische Speicherung gehören in die KI-negative Kernzone.

### Best current intervention hypothesis

Kein neuer Prompt „vor Änderungen vorsichtig sein“.

Die kleinste stärkere Richtung ist ein **operation-typed canonical write boundary**:

```text
bounded edit / patch
→ darf nur den explizit adressierten Bereich ändern

full replace / migration / mass rewrite
→ eigener deklarierter Mutationstyp
→ vollständiger Diff/Loss-Check
→ proportionale Review-/Promotion-Grenze
```

Die konkrete Implementierung (Patch API, Branch/PR, lokale Diff-Guard-Library, GitHub Ruleset oder Kombination) ist #48/#59-Aufgabe und wird durch diesen Audit nicht entschieden.

### Reaction / disposition

- Reaktion: `BLOCK` bei unerwartetem Full-Replace/Deletion außerhalb des deklarierten Mutationstyps.
- Problemstatus: `confirmed-current`.
- bestehende Governance: `refine/derive` – die Schutzsemantik bleibt, Detailwarnungen zur Dateioperation sollten nach ausführbarem Guard nicht als Promptpflicht dupliziert werden.

---

## AM-02 – CI existiert, aber `main` ist keine kontrollierte Promotion Boundary

### Observed/current phenomenon

Histo-Orla besitzt einen Project-Assurance-Workflow, aber GitHub meldet `main` als unprotected und ohne required checks; Repository-Rulesets fehlen. AI-gestützte GitHub-Writes können dadurch direkt kanonische Commits erzeugen.

Der schädliche Commit `ca4118...` demonstriert die Konsequenz praktisch: Er war sofort Teil von `main` und löste wegen des Pfadfilters nicht einmal nachträglich den Workflow aus.

### Symptom

`Assurance vorhanden` wird leicht mit `Promotion geschützt` verwechselt.

### Protected goal

- canonical repository state darf nicht durch explorative/unvalidierte AI-Ausführung still verändert werden;
- Checks und Review sollen vor, nicht erst nach consequential Promotion wirken;
- direkte Schreibrechte sollen proportional zum Mutationstyp sein.

### Root cause

1. **Assurance vs. admission conflated:** Workflow-Ausführung ist kein Merge-/Write-Gate.
2. **Branch authority not encoded:** `main` akzeptiert direkte Writes.
3. **Coverage gap:** zentrale Project-/Research-State-Pfade liegen außerhalb des aktuellen Workflow-Triggers.
4. **Credential ≠ authority:** AI-gestützte Connector-Writes erscheinen in Git als Commit des verbundenen GitHub-Nutzers. Die Git-Actor-Identität beweist daher nicht, dass eine materielle Owner-Entscheidung menschlich getroffen wurde.

Der vierte Punkt ist besonders wichtig: **Git provenance ist notwendige technische Provenienz, aber unter delegierter AI-Nutzung kein hinreichender Authority-Beleg.**

### Current relevance

`confirmed-current`.

### Existing basis

- #42: nur Requirements Owner kann accepted Requirements ändern.
- #48: Dev darf fachliche/Requirement-Semantik nicht eigenmächtig ändern.
- #63: technischer Implementation Trace + Owner-Decision für Scope-/Quality-Reduktion.
- `REQ-WF-001`, `REQ-STATE-001`, `REQ-TRACE-001`.
- `Wissensarbeit/system/authority.json`: AI darf materielle Reframes/Requirements/Priority nur vorschlagen; materielle Akzeptanz benötigt Human Authority.

### Best current intervention hypothesis

Zwei Grenzen nicht vermischen:

**A. Repository admission**  
Canonical/high-risk Pfade brauchen einen Promotionweg, bei dem relevante Checks/Diff vor `main` liegen. Branch+PR ist vorhandenes GitHub-Pattern; ob dies repo-weit oder path-/mutationstyp-spezifisch erzwungen wird, ist eine Lean-/UX-Frage für #48.

**B. Material authority**  
Für Zweck, Priorität, Requirements, fachliche Semantik oder andere owner-only Changes darf `Git author == owner account` nicht als Human-Authority-Nachweis gelten, wenn AI unter demselben Principal handelt. Der Promotionpfad braucht eine **Authority-Evidence, die die proposal-generierende AI nicht selbst erzeugen kann**. Das genaue Mittel ist offen; es darf den Owner nicht zum Workflow-Manager machen.

### Reaction / disposition

- formale invalid mutation / fehlende required admission: `BLOCK`;
- AI-Vorschlag zu Purpose/Requirement/Priority: `HOLD` als Candidate;
- echte materielle Owner-Entscheidung: `ESCALATE`.
- Problemstatus: `confirmed-current`.
- Governance disposition: `merge/derive` – mehrere „AI darf X nicht“-Sätze sollten langfristig aus einer kleinen Authority-/Promotion-Grenze ableitbar sein.

---

## AM-03 – Research-State-Promotion ist semantisch definiert, technisch aber noch kein Write Interface

### Observed/current phenomenon

Der Canonical-State-Contract trennt Candidate/Working/Validated/Unresolved/Superseded und verlangt History-Erhalt. #54 spezifiziert negative Fixtures für Promotion, ist aber `planned`. Die Enforcement Map führt `transition` ohne Rule-Refs als `planned`.

Die realen Research-Artefakte liegen derzeit überwiegend als versionierte Dateien unter `docs/research/cases/**`; der einzige Workflow überwacht diesen Pfad nicht.

### Symptom

`wissenschaftliche Promotion-Regel ist klar` aber `Dateiänderung und wissenschaftliche Transition sind technisch nicht unterscheidbar`.

### Protected goal

- AI darf neue Lesungen/Hypothesen/Candidates frei erzeugen;
- ein anderes Modellurteil ist keine Mutation Authority;
- Promotion/Supersession braucht Vorgänger, Basis, Evidence/Method/Review proportional zur Konsequenz;
- Correction/Demotion darf Research History nicht zerstören.

### Root cause

Die Domain-/Research-Semantik ist weiter als die Operationalisierung. Es fehlt noch der kleine **transition boundary** zwischen generativer/analytischer Arbeit und canonical Research-State-Mutation.

Das ist nicht identisch mit allgemeinem Git-Branch-Schutz: Git kann zeigen, dass Text geändert wurde, aber nicht, ob `candidate → promoted`, `finding → superseded` oder `unresolved → resolved` wissenschaftlich zulässig deklariert wurde.

### Current relevance

- beobachteter Histo-Fall einer stillen wissenschaftlichen Überschreibung: `unproven`;
- strukturelle Exposition und fehlendes Enforcement: `confirmed-current`.

Der Audit darf diese beiden Aussagen nicht zusammenziehen.

### Existing basis

- `REQ-EPI-004/005`, `REQ-VAL-001/002`, `REQ-WF-001`;
- `REQ-EPI-006`, `REQ-MTH-004`, `REQ-RSCH-001`;
- #24 Candidate→Validation→Promotion;
- #50 Canonical Research State;
- #54 Transition Owner;
- `docs/architecture/operational-execution-architecture.md` §11.

### Best current intervention hypothesis

Bestehende Architekturhypothese bleibt passend und wird durch den Vorfall eher gestärkt:

```text
READ / ANALYZE       → frei innerhalb Scope
PROPOSE              → Candidate/Alternative/Challenge
WRITE NEW OBJECT     → Objekt-/Evidence-/Method-Contract
PROMOTE / SUPERSEDE  → transition capability + predecessor/basis/review/history guards
```

Kein universeller Workflow-Stack und keine Softwareentscheidung über historische Wahrheit.

Erster Implementationstest soll an **einem realen Research Slice** erfolgen. Legacy-Markdown muss nicht vorab Big-Bang-migriert werden.

### Reaction / disposition

- AI-Neuurteil: `HOLD`;
- formal ungültige Promotion: `BLOCK`;
- fachlich consequential Promotion: `ESCALATE` an passende Domain-/Review-Authority;
- Problemstatus: `conditional` für tatsächlichen Schadensfall, `confirmed-current` für Enforcement-Gap.
- bestehende Regeln: `retain`, später `derive` sobald Transition-Guard ausführbar ist.

---

## AM-04 – Purpose / Priority / Requirement Authority kann semantisch korrekt und technisch trotzdem nicht beweisbar sein

### Observed/current phenomenon

Histo-Orla hat starke semantische Owner-Grenzen: #42 ist alleiniger Requirements-Lifecycle-Owner; Research Owner besitzt Ziel/Nutzen/Pain; Dev besitzt keine Fachsemantik. Der Work-Context-Audit hat Model-/Process-/Authority-Drift bereits explizit erkannt.

Ein bestätigter Histo-Fall, in dem AI eigenmächtig ein accepted Requirement oder Projektziel promoted hat, ist in diesem Slice **nicht belegt**.

Gleichzeitig erlaubt die aktuelle Repo-/Credential-Struktur AI-gestützte Writes unter demselben GitHub-Principal wie der Owner. Formale Requirements-QA kann Semantik/Owner-Intent bewusst nicht selbst bestimmen.

### Symptom

`persistiert von Owner-Account` kann fälschlich als `materiell vom Owner autorisiert` gelesen werden.

### Protected goal

Purpose & Authority Integrity: Ziel, Priorität, Requirements und materielle Akzeptanz dürfen nicht durch Modellplausibilität oder delegierte technische Identität entstehen.

### Root cause

Nicht fehlende Owner-Prosa, sondern eine **Authority-evidence gap an der Promotiongrenze**:

- fachliche/materielle Authority ist semantisch definiert;
- GitHub-Actor repräsentiert technische Credential-Identität;
- bei delegierter AI-Nutzung sind beide nicht dasselbe.

### Current relevance

`conditional` – keine belegte falsche Promotion in Histo-Orla, aber reale technische Möglichkeit und bereits beobachtete delegierte AI-Commits unter Owner-Identität.

### Best current intervention hypothesis

- AI darf materielle Change-Candidates strukturieren und auf einem nicht-kanonischen Pfad persistieren.
- Promotion owner-only Zustände braucht explizite Authority-Evidence außerhalb des bloßen Git-Author-Feldes.
- Wissenschaftliche/fachliche Entscheidungen benötigen zusätzlich die jeweils passende Domain-/Specialist-Authority; Human Owner ist kein Ersatz-Fachspezialist.
- Kein zusätzlicher Requirements-Satz ist derzeit erkennbar: #42/#9/#24 + bestehende Requirements tragen das Ziel bereits. Die Lücke ist zunächst Delivery/Architecture/Tool Authority.

### Reaction / disposition

- Vorschlag: `HOLD`;
- materieller Owner-Entscheid: `ESCALATE`;
- unautorisierte direkte Promotion: `BLOCK` soweit formal erkennbar;
- Problemstatus: `conditional`.
- Governance disposition: `merge/derive`, keine neue Authority-Regelwelt.

---

# 4. Was Slice 1 über die eigentliche Zielstruktur zeigt

Die vier Fälle reduzieren sich nicht sinnvoll auf vier neue Regeln. Sie zeigen zwei technische Schutzgrenzen plus eine fachliche Authority-Grenze:

```text
1. SAFE REPOSITORY MUTATION
operation type + bounded delta + diff/loss + admission

2. RESEARCH-STATE TRANSITION
candidate/new object/promotion/supersession + predecessor/history + formal refs

3. MATERIAL / SCHOLARLY AUTHORITY
proposal != acceptance
technical actor identity != human/domain authority evidence
```

Diese Grenzen passen in die bereits vorgesehene Operational-Struktur:

```text
canonical semantics/state
→ validate / context / resolve / transition
→ BLOCK | HOLD | ESCALATE
→ thin GitHub/AI/CLI adapter
```

Für diesen Slice ist `REDIRECT` sekundär; es wird voraussichtlich im nächsten Cursor-/Loop-Slice zentral.

---

# 5. Minimaler Delta – noch keine Implementationsentscheidung

## Bereits vorhanden und zu behalten

- #42 Authority/Lifecycle;
- `REQ-WF-001` und `REQ-STATE-001`;
- #24 KI-negative Kernzone + Candidate→Promotion;
- #50 Canonical-State-/History-Semantik;
- #54 als Transition-Delivery-Owner;
- #63 für technische Value-/Decision-/Delivery-Traceability;
- Operational Core als gemeinsame Mechanik statt weiterem Validator-Silo.

## Reale aktuelle Gaps

### G-AM-01 – Safe canonical repository mutation

Kein aktueller ausführbarer Guard verhindert, dass ein bounded beabsichtigter Change via Full Replace unerwartet gültigen kanonischen Inhalt löscht.

**Route:** #48/#59 unter bestehendem `REQ-WF-001`, `REQ-STATE-001`, `REQ-LEAN-001`; kein neuer Requirement-Candidate aus diesem Audit.

### G-AM-02 – Pre-promotion repository admission

`main` ist unprotected; keine Rulesets; Assurance ist nicht required-before-promotion. Zentrale Project-/Research-State-Pfade liegen teilweise außerhalb des Workflow-Triggers.

**Route:** #48/#59 technische Mittel-/UX-Prüfung; ggf. #63 nur soweit formale Delivery-Trace betroffen ist. Keine automatische Forderung „alles braucht PR“ – die Lösung muss Owner-Aufwand minimieren.

### G-AM-03 – Research-state transition enforcement

#54 / `transition` ist geplant, nicht implementiert.

**Route:** bestehender #54-Owner; first-real-slice statt neuer Governance.

### G-AM-04 – Material authority evidence under delegated AI credentials

Git actor/credential ist kein hinreichender Beleg für Human-/Domain-Authority, wenn AI unter demselben Account schreibt.

**Route:** zunächst #48/#61/#63 als Architecture/Work-Context/Promotion-Frage gegen bestehende Authority Requirements prüfen. Nur falls eine echte Requirement-Lücke verbleibt, Rückgabe an #42.

---

# 6. Simplification / Löschpotenzial

Noch wird **keine bindende Governance gelöscht**, weil die Ersatzmechanismen nicht implementiert sind. Slice 1 identifiziert aber konkretes späteres Konsolidierungspotenzial:

1. Wiederholte Prosa `AI darf canonical X nicht still ändern` kann nach wirksamer Mutation-/Transition-Grenze aus Adaptern/Skills/Prompts verschwinden und auf den kanonischen Contract verweisen.
2. Detailwarnungen über Full-File-Replace gehören nach einem executable safe-write boundary nicht dauerhaft in Agentenprompts.
3. `Candidate before Canonical` bleibt fachlich als eine Invariante erhalten; einzelne Workflow-Wiederholungen können aus Derived Context/Transition Policy erzeugt werden.
4. GitHub-/CI-Prozess darf kein neuer Owner-Workflow werden: sobald eine technische Admission-Grenze zuverlässig wirkt, soll der Research Owner im Normalfall nur consequential Ausnahmen/Entscheidungen sehen.

**Löschregel:** Erst Ersatznachweis + adversarial fixture, dann `retire-active`; Git/Issue-Historie bewahrt Motivation und frühere Failure-Evidence.

---

# 7. Adversarial Fixtures aus Slice 1

Diese Fixtures sind Audit-/Delivery-Inputs, noch keine neuen Tests dieses PRs:

### F-AM-01 – Bounded edit deletes unrelated canonical tail

Given: bounded Änderung an einem Abschnitt.  
When: Adapter erzeugt zusätzlich große nicht deklarierte Löschung.  
Then: `BLOCK` vor canonical promotion.

Realer Seed: Commit `ca4118...`.

### F-AM-02 – Direct canonical write without required admission

Given: AI kann Branch/Repo beschreiben.  
When: consequential canonical path soll direkt promoted werden.  
Then: vorgeschriebener Admission-Pfad darf nicht umgangen werden.

### F-AM-03 – New model supersedes Working Finding by plausibility only

Given: existing Working Finding + history.  
When: anderes Modell schlägt widersprechendes Urteil ohne neue Basis vor.  
Then: `HOLD` als Candidate; keine Supersession.

### F-AM-04 – AI-authored commit appears as owner credential

Given: delegated GitHub write uses owner principal.  
When: Change beansprucht material owner authority nur wegen Git author.  
Then: Authority bleibt unbewiesen; `ESCALATE/HOLD`.

### F-AM-05 – Valid scholarly correction with complete basis

Given: neue Evidenz + passende Method/Review-Basis.  
When: bestehendes Finding korrigiert/superseded wird.  
Then: Transition muss zulässig sein und History erhalten; Guard darf legitime wissenschaftliche Revision nicht blockieren.

Dieser Positivfall verhindert, dass AI-Resilience in Unveränderlichkeit des Research State kippt.

---

# 8. Wissensarbeit-Vergleich – strukturell, nicht normativ

Aktueller `esany/Wissensarbeit`-Stand bestätigt als generische Strukturreferenz:

- `project/GOVERNING_OBJECTIVE.md`: Exploration frei, Promotion kontrolliert; Git-Provenienz/Diff/Review/Reversibilität; Meta-Arbeit darf nicht Hauptprodukt werden.
- `system/authority.json`: `deterministic → software`, `procedural → workflow`, `judgement → ai_plus_human_or_specialist`; AI darf materielle Requirement-/Priority-/Domain-Änderungen vorschlagen, nicht akzeptieren.
- `system/material_state.json`: Persistenz eines Candidates ist ausdrücklich nicht Promotion.
- `tools/work.py`: kleine executable Contracts/Validatoren statt Agenten-/Workflow-Plattform.

Wichtig für Histo-Orla: Das Template liefert **kein fertiges Repo-Sicherheitsmodell** und ersetzt keine Histo-Research-Semantik. Auch im Wissensarbeit-Repository ist `main` aktuell nicht GitHub-branch-protected. Das übertragbare Muster ist daher Capability-/Authority-Trennung, nicht die Annahme, das Referenzrepo habe jede Promotion technisch gelöst.

---

# 9. Slice-1 Disposition

| Fall | Histo-Problemstatus | primäre Reaktion | aktuelle Schutzlage | Regel-/Mechanismus-Disposition |
|---|---|---|---|---|
| AM-01 destructive full replace | `confirmed-current` | `BLOCK` | Recovery durch Git, Prävention fehlt | `refine → replace prose by executable safe-write boundary` |
| AM-02 unprotected canonical admission | `confirmed-current` | `BLOCK/ESCALATE` | CI vorhanden, aber nicht required; Pfadlücken | `merge/derive` |
| AM-03 silent Research-State supersession | Schadensfall `unproven`, Enforcement-Gap `confirmed-current` | `HOLD/BLOCK/ESCALATE` | Semantik stark, #54 `planned` | `retain → derive after transition implementation` |
| AM-04 authority laundering via delegated credential | `conditional` | `HOLD/ESCALATE` | semantische Owner klar, technische Authority-Evidence offen | `merge/derive` |

## Requirement disposition

**Kein neuer Requirement-Candidate aus Slice 1.**

Die bestätigten Gaps werden gegen bestehende Requirements getragen:

- `REQ-WF-001` – deterministic invariant enforcement;
- `REQ-STATE-001` – canonical/recoverable/chat-independent state;
- `REQ-TRACE-001` – material technical work to authority/value/decision/feedback;
- `REQ-UX-002` – challenge/correct/demote ohne Routine-Micromanagement;
- #42/#9/#24 – Material-/Requirement-/AI-Authority.

Sollte G-AM-04 nach technischer Analyse nicht aus bestehenden Authority-/Trace-/Work-Context-Verträgen ableitbar sein, ist erst dann ein echter Requirement-Gap an #42 zurückzugeben.

---

# 10. Nächste Aktion unter #70

Slice 2 prüft **Execution Cursor / Sticky Prerequisites / No-progress Loops** nach derselben Genealogie. Dabei ist der aktuelle Nebenbefund zu untersuchen, dass am 2026-09-03 mehrere identische/inhaltlich no-op Restore-Commits mit gleichem Tree erzeugt wurden: mögliche Tool-/Retry-/Loop-Friktion, aber noch keine vorweggenommene Root-Cause-Disposition.

Vor jeder Implementation aus Slice 1 gilt:

```text
Audit finding
→ existing requirement/owner?
→ #48 technical option / smallest sufficient mechanism
→ #59 implementation + adversarial fixture
→ real vertical research use
→ owner feedback
→ only then governance retirement
```

Kein #44-Blocker ergibt sich aus Slice 1: Es liegt aktuell keine nicht-ableitbare Owner-Entscheidung vor, sondern zunächst technische/operationalisierbare Lücken innerhalb bestehender Requirements.
