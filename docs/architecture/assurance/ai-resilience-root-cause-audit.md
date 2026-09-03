# Histo-Orla – AI-Resilience Root-Cause Audit

**Status:** `audit / review-input / no requirement-or-implementation-authority`  
**Work Owner:** #70  
**Interfaces:** #64, #42, #24, #45, #48, #50, #54, #56, #57, #60, #61, #62, #63  
**Stand:** 2026-09-03  
**Structural prior art:** `esany/Wissensarbeit` (generic project handling only; no Histo-Orla semantic authority)

## 1. Auditfrage und Methode

Dieser Audit schützt **keine Regeln um ihrer selbst willen**. Er rekonstruiert reale oder plausible KI-/System-Failure-Modes rückwärts:

```text
observed phenomenon / evidence
→ visible symptom
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

Die operative Reaktion wird erst nach der Ursachenanalyse bestimmt:

- `BLOCK` – formal/mechanisch unzulässiger Schritt;
- `HOLD` – möglicher Candidate/Challenge, aber keine kanonische Promotion;
- `REDIRECT` – gültiger Cursor/Postcondition existiert bereits; Ausführung driftet oder loopt;
- `ESCALATE` – echte materielle Owner-/Fachentscheidung.

**Evidenzklassen dieses Audits:**

- `observed-histo` – reales Histo-Orla-Laufereignis oder Owner-Feedback;
- `current-state` – aktuell verifizierter Repo-/Contract-/Implementation-State;
- `cross-repo/adversarial` – reale oder synthetische Referenz aus anderem Projekt; kein automatischer Histo-Befund;
- `hypothesis` – noch zu falsifizierende Ursache oder Intervention.

Kein Audit-Finding besitzt allein Requirement-, Method-, Architecture- oder Implementation-Authority.

---

# 2. Slice 1 – Canonical Mutation / Authority

## 2.1 Kurzurteil

Die Schutzsemantik ist weitgehend vorhanden, die Ausführung nicht:

1. Candidate-vs.-Canonical, History-Erhalt, AI-non-evidence und deterministische Promotion Guards sind in Requirements/#24/#50 bereits angelegt.
2. #54 / `transition` ist weiterhin `planned`.
3. `main` ist am 2026-09-03 `protected:false`; Repository-Rulesets fehlen.
4. `Project Assurance` ist daher keine verpflichtende Pre-Promotion-Grenze und überwacht weder `PROJECT_STATE.md`/`README.md` noch `docs/research/cases/**`.
5. Ein realer AI-gestützter Full-File-Replace hat gültigen kanonischen Handoff-State auf `main` gelöscht und musste aus Git-History repariert werden.

Das ist **keine primäre Requirement-Lücke**, sondern eine Differenz zwischen akzeptierter Semantik und realer Mutation-/Admission-Grenze.

## 2.2 Evidence Register

| ID | Klasse | Evidenz | Aussage |
|---|---|---|---|
| E-AM-001 | observed-histo | Commit `ca4118fb7e6cfa04ed6ac6f0e10a1d35f03ec82c` | bounded beabsichtigte Änderung an `PROJECT_STATE.md` führte zu massiver unbeabsichtigter Löschung |
| E-AM-002 | observed-histo | Commit `c01a59e3c606bf38e3b251c21e50a1647d6f034c` | Recovery aus direktem Git-Vorgänger; Git half beim Wiederherstellen, verhinderte den Schaden aber nicht |
| E-AM-003 | current-state | GitHub branch state `main` | `protected:false`, required status checks off |
| E-AM-004 | current-state | repository rulesets | keine Rulesets |
| E-AM-005 | current-state | `.github/workflows/project-assurance.yml` | zentrale Project-/Research-State-Pfade liegen außerhalb des Trigger-Scope |
| E-AM-006 | observed-histo | Actions query für `ca4118...` | kein Workflow-Lauf für den schädlichen Commit |
| E-AM-007 | current-state | `tools/operational/enforcement-map.json` | `REQ-WF-001 = partial`; `transition` für relevante Promotionen `planned`, ohne Rule-Refs |
| E-AM-008 | current-state | `docs/architecture/contracts/canonical-research-state.md` | Candidate/Working/Promoted/Unresolved/Superseded, History und AI-non-evidence semantisch explizit |
| E-AM-009 | current-state | #54 | Research-State-Promotion/Transition noch nicht implementiert |
| E-AM-010 | current-state | `tools/assurance/policy.json` | Changed-Code-Guard kontrolliert technische Pfade, nicht Research-/Project-State allgemein |

## AM-01 – Bounded edit wird destruktiver Full-File-Replace

**Observed phenomenon:** Kleine Ergänzung an `PROJECT_STATE.md` erzeugte einen wesentlich größeren Replace mit Verlust gültiger Abschnitte.

**Protected goal:** Verlustfreiheit, rekonstruierbare History, restartbarer Project State, geringe Owner-Micromanagement-Last.

**Root cause:**

- Operation mismatch: Full Replace für bounded edit;
- gültiger Vorgänger-SHA verhindert Stale Write, aber nicht semantisch destruktiven Replace;
- kein bounded-delta / destructive-loss guard;
- unmittelbarer Write auf `main`;
- betroffener Pfad nicht durch Project Assurance erfasst.

**Problemstatus:** `confirmed-current`.

**Best current intervention hypothesis:** operation-typed safe write boundary:

```text
bounded edit / patch
→ nur deklarierter Bereich darf sich ändern

full replace / migration / mass rewrite
→ expliziter Mutationstyp
→ vollständiger Diff/Loss-Check
→ proportionale Admission-/Review-Grenze
```

**Reaction:** `BLOCK` bei unerwartetem Delete/Replace außerhalb des deklarierten Mutationstyps.

**Rule disposition:** `refine → derive`; nach executable Guard keine dauerhafte Promptwarnung über Full-File-Replaces nötig.

## AM-02 – Assurance ist nicht Admission

**Observed/current phenomenon:** CI existiert, aber `main` kann direkte AI-gestützte Writes aufnehmen. Der schädliche Commit war sofort canonical und triggerte nicht einmal den Workflow.

**Protected goal:** Konsequenzielle canonical changes müssen vor Promotion den richtigen Diff-/Check-/Authority-Pfad durchlaufen.

**Root cause:**

1. Workflow-Ausführung und Admission wurden strukturell nicht gekoppelt.
2. Branch Authority ist nicht technisch erzwungen.
3. zentrale Pfade haben Coverage-Gaps.
4. **Credential ≠ Authority:** AI-Connector-Writes erscheinen unter dem verbundenen GitHub-Principal; `Git author == owner account` beweist keine menschliche materielle Entscheidung.

**Problemstatus:** `confirmed-current`.

**Best intervention hypothesis:**

- repository admission für consequential/high-risk mutation types;
- separat: explizite Authority-Evidence für owner-only/material changes, die die proposal-generierende AI nicht selbst erzeugen kann;
- kein Dogma `alles muss PR` – die Lösung muss `REQ-UX-002`/`REQ-LEAN-001` erfüllen.

**Reaction:** `BLOCK` bei fehlender formaler Admission; `HOLD` für AI-Vorschlag; `ESCALATE` für materielle Owner-Entscheidung.

**Rule disposition:** `merge/derive`.

## AM-03 – Research-State-Promotion ist Contract, noch kein Write Interface

**Current phenomenon:** #50 trennt Research States und verlangt History; #54/`transition` ist geplant, nicht ausführbar. Git kann Dateidiffs zeigen, aber nicht entscheiden, ob `candidate → promoted` oder `finding → superseded` formal zulässig deklariert wurde.

**Observed scholarly overwrite in Histo:** `unproven`.

**Structural enforcement gap:** `confirmed-current`.

**Protected goal:** freie Exploration bei kontrollierter wissenschaftlicher Promotion/Correction/Demotion.

**Best intervention hypothesis:** vorhandene Architektur beibehalten:

```text
READ / ANALYZE       → frei im Scope
PROPOSE              → Candidate/Alternative/Challenge
WRITE NEW OBJECT     → Objekt-/Evidence-/Method-Contract
PROMOTE / SUPERSEDE  → transition + predecessor/basis/review/history guards
```

**Reaction:** `HOLD` für Neuurteil; `BLOCK` bei formal ungültiger Promotion; `ESCALATE` für consequential scholarly judgement.

**Rule disposition:** `retain → derive after transition enforcement`.

## AM-04 – Material Authority unter delegierten Credentials

**Current phenomenon:** Histo-Orla besitzt klare semantische Owner. Ein belegter Histo-Fall eigenmächtig akzeptierter Requirement-/Purpose-Promotion durch AI liegt nicht vor. Technisch kann AI jedoch unter demselben GitHub-Principal schreiben wie der Owner.

**Problemstatus:** `conditional`.

**Root cause:** fehlende Trennung zwischen technischer Actor Identity und materialer Human-/Domain-Authority-Evidence an der Promotiongrenze.

**Best intervention hypothesis:** Candidate-Persistenz darf automatisiert sein; owner-only/domain-only Promotion braucht passende externe Authority-Evidence. Human Owner ist kein Ersatz-Fachspezialist.

**Reaction:** `HOLD / ESCALATE`; formal erkennbare unautorisierte Promotion `BLOCK`.

**Requirement disposition Slice 1:** **kein neuer Requirement-Candidate**. Route über bestehende `REQ-WF-001`, `REQ-STATE-001`, `REQ-TRACE-001`, `REQ-UX-002`, #24/#42/#48/#54/#61/#63.

---

# 3. Slice 2 – Execution Cursor / Sticky Prerequisites / No-progress Loops

## 3.1 Kurzurteil

Hier liegt der zentrale Fehler nicht in mangelnder KI-Disziplin, sondern in zwei noch fehlenden Operational Capabilities:

1. **Postcondition / Progress / Idempotency Guard** – eine bereits erfüllte Operation erzeugt keine weitere Arbeit und keinen weiteren Commit.
2. **Generated Current Execution Context** – ein frischer Ausführer erhält aus kanonischem State den gültigen Work Owner, die erlaubte nächste Aktion, Preconditions/Blocker und Stop-/Return-Bedingungen.

`Sticky Prerequisites` ist daraus ableitbar und braucht keine eigene Governance-Welt.

## 3.2 Evidence Register

| ID | Klasse | Evidenz | Aussage |
|---|---|---|---|
| E-EC-001 | observed-histo | Commit `c01a59e3...` | eigentliche Recovery änderte State real |
| E-EC-002 | observed-histo | `258753b9...` | direkt folgender Commit: gleicher Tree, `0 additions`, `0 deletions`, `files=[]` |
| E-EC-003 | observed-histo | `39103f19...` | erneut gleicher Tree, `0/0`, keine Dateien |
| E-EC-004 | observed-histo | `34a69afc...` | erneut gleicher Tree, `0/0`, keine Dateien |
| E-EC-005 | observed-histo | `6253ae24...` | erneut gleicher Tree, `0/0`, keine Dateien |
| E-EC-006 | observed-histo | `docs/architecture/assurance/live-pilot-system-analysis-chat-2026-08-31.md` P-SA-007 | frischer Context braucht funktionalen Restart, nicht bloße Dokumentexistenz |
| E-EC-007 | observed-histo | `FB-20260902-003` | Owner-Pain: zu viel manuelle/chat-orchestrierte State-/Workflow-Arbeit |
| E-EC-008 | current-state | `docs/architecture/operational-execution-architecture.md` | Work Context semantisch vorhanden, Generator fehlt |
| E-EC-009 | current-state | `tools/operational/enforcement-map.json` | `context/resolve` für relevante Requirements geplant, nicht executable |
| E-EC-010 | current-state | #61 / method-conformance-work-context | Work Context/Handoff als generierbare Struktur fachlich analysiert, noch kein Runtime-Resolver |
| E-EC-011 | current-state | #24 S6 | Workflow/Pipeline Engineering soll Jobs idempotent und restartbar machen |

## EC-01 – Wiederholte No-op Writes erzeugen künstliche Arbeit

**Observed phenomenon:** Nach der eigentlichen Recovery wurden vier weitere Commits mit gleichem Commit-Message-Intent und identischem Tree erzeugt. Jeder hatte `stats.total=0`, `files=[]`.

**Symptom:**

```text
Postcondition bereits erfüllt
→ dieselbe Write-Aktion erneut
→ neuer Commit
→ kein State Delta
→ Wiederholung
```

**Protected goal:** Fortschritt, saubere History, geringe Owner-/CI-Last, keine Loops ohne Erkenntnis-/State-Gewinn.

**Root cause hypothesis:**

- Write-Adapter akzeptiert no-op replacement als Commit;
- Ausführung prüft vor Write nicht, ob gewünschter Zielzustand bereits gilt;
- nach Tool-Ergebnis existiert keine kleine Progress-Postcondition;
- Wiederholung derselben Operation auf demselben State besitzt keine Idempotency-/Loop-Semantik.

Nicht belegt ist, **warum** das Modell/der Tool-Caller viermal wiederholte. Der Audit behauptet daher keinen psychologischen „LLM Loop“, sondern einen strukturell erlaubten No-progress-Pfad.

**Problemstatus:** `confirmed-current`.

**Best intervention hypothesis:** Adapter/Core prüft mindestens:

```text
current_state_fingerprint
requested_postcondition
candidate_state_fingerprint

candidate == current
→ NO_CHANGE
→ kein Write / kein Commit
→ REDIRECT auf nächste gültige Aktion
```

Bei erneut identischer `(operation, target, input-state, postcondition)` ohne Delta: keine weitere Ausführung; sichtbares no-progress result.

**Reaction:** primär `REDIRECT`; `BLOCK` nur für einen technisch unzulässigen erneuten No-op-Write.

**Rule disposition:** `replace` wiederholte Prompt-/Retry-Anweisungen durch Idempotency-/Postcondition-Guard.

## EC-02 – Fresh-context Resume kennt Semantik, aber keinen ausführbaren Cursor

**Observed/current phenomenon:** P-SA-007 belegt, dass zuverlässige Fortsetzung erst nach erneutem Repo-Bootstrap gelang. #61 und AGENTS definieren die nötige Semantik; die Operational Architecture weist den fehlenden Context Generator ausdrücklich aus.

**Protected goal:** Ein neuer Chat/Modell/Ausführer setzt **am gültigen Punkt** fort und eröffnet nicht aus Plausibilität eine andere Arbeitsstufe.

**Root cause:** Current task/owner/next action/authority sind heute über mehrere kanonische Stellen rekonstruierbar, aber nicht als kleiner transienter Execution Context deterministisch komponiert. Dadurch bleibt die Orchestrierung zu stark Aufgabe des Modells/Chats.

**Problemstatus:** `confirmed-current` als Delivery-/Runtime-Gap; nicht jede einzelne falsche Cursorverschiebung ist als Histo-Schadensfall belegt.

**Best intervention hypothesis:** `context`/`resolve` erzeugt einen rebuildbaren Work Context aus bestehenden Truth Sources, mindestens:

```text
work_owner_ref
primary_function
bounded objective / scope / exclusions
current executable action or stage
completed prerequisites + basis
open blockers / unresolved dependencies
may / must-not
stop / handoff / return condition
persistence target
```

Der Output ist Derived/Runtime Context, **kein zweiter Task Truth Store**.

**Reaction:** `REDIRECT` bei Drift auf nicht autorisierte/erledigte Stufe; `ESCALATE` nur bei echter materialer Mehrdeutigkeit.

**Rule disposition:** `derive`; Handoff-/Work-Context-Prosa soll langfristig aus kanonischem State kompiliert werden.

## EC-03 – Sticky Prerequisite braucht Basis + Invalidierung, nicht „nie wieder prüfen“

**Observed Histo failure:** `unproven` für den spezifischen Fall „neue KI rollt deterministisch bestandene Precondition erneut auf“.

**Current structural state:** Es gibt keine allgemeine executable Prerequisite-/Invalidation-Projektion. #63 besitzt bereits ein engeres Freshness-Pattern: ein alter `verified` Implementation-Record schaltet veränderten Code nicht dauerhaft frei. Das zeigt, dass Gültigkeit an Basis/Change gebunden werden kann.

**Protected goal:** Fortschritt über Context-/Modelwechsel erhalten, ohne legitime Re-Validierung zu verhindern.

**Root cause if it occurs:** Der Status einer Precondition und die Bedingungen, unter denen er ungültig wird, sind nicht explizit genug außerhalb des Modells repräsentiert.

**Best intervention hypothesis:** kein globaler Workflow Engine State. Wo eine echte Precondition formal relevant ist:

```text
prerequisite_ref
status = pass | fail | unresolved
basis_refs / fingerprint
validated_at
invalidation_conditions_or_events
```

Neue Modellunsicherheit ist **kein** Invalidation Event. Geänderte Basis, Source-Version, Requirement, Method Status, Rights-/Availability-State oder expliziter Owner-Change **kann** eines sein.

**Problemstatus:** `conditional`.

**Reaction:** `REDIRECT` bei grundloser Wiederholung; bei realem Invalidation Event normale Re-Validation; bei fachlicher Unsicherheit `HOLD/ESCALATE` statt künstlichem PASS.

**Rule disposition:** `defer/derive`; keine neue „sticky prerequisite“-Regel bis ein realer Consumer die Projektion benötigt.

## EC-04 – Support-/Governance-Arbeit kann den Research Cursor übernehmen

**Observed phenomenon:** #64 und `FB-20260902-003` dokumentieren realen Owner-Pain: Root/Handoff/Meta-Artefakte und manuelle Chat-Orchestrierung beanspruchen zu viel Aufmerksamkeit; Schutz-/Systemarbeit droht selbst zum sichtbaren Value Stream zu werden.

**Protected goal:** Research Owner arbeitet an historischen Fragen; System-/Support-Arbeit bleibt dienend und erzeugt nicht durch Eigengewicht einen neuen Forschungsauftrag.

**Root cause:**

- semantisch getrennte Owner/Issues werden im aktuellen textlastigen Betrieb zu manuellen operativen Handoffs;
- Current Research Question/Next Research Action ist nicht als research-first Derived View/Context verfügbar;
- Support-Artefakte können dadurch faktisch zum nächsten Cursor werden, obwohl sie keine Research-Priority-Authority besitzen.

**Problemstatus:** `confirmed-current`.

**Best intervention hypothesis:** Current Context muss den **autoritativen Primärauftrag** und dessen nächste Aktion von Support-/Review-Arbeit unterscheiden. Support work darf Findings/Candidates/System-Learnings erzeugen, aber einen neuen primary research cursor nur über vorhandene Purpose/Priority Authority.

**Reaction:** `REDIRECT`.

**Rule disposition:** `merge/derive`; die lange Owner-/Handoff-Topologie darf nicht als Nutzerworkflow gespiegelt werden.

## 3.3 Slice-2 Konsolidierung

Die Fälle reduzieren sich auf zwei Capabilities:

```text
A. CURRENT EXECUTION CONTEXT / CURSOR RESOLUTION
canonical owners + task + dependencies + prerequisite validity
→ generated current executable action

B. PROGRESS / IDEMPOTENCY GUARD
requested postcondition + current state + outcome
→ delta | no_change | blocker
→ no repeated work without delta
```

**Requirement disposition Slice 2:** kein neuer Requirement-Candidate. Bestehende Basis: `REQ-WF-002`, `REQ-STATE-001`, `REQ-TRACE-001`, `REQ-UX-001/002`, `REQ-LEAN-001`, #24, #61.

---

# 4. Slice 3 – Evidence / Epistemic Boundary

## 4.1 Kurzurteil

Dieser Slice unterscheidet zwei Kategorien, die nicht gemeinsam „wegoptimiert“ werden dürfen:

1. **dauerhafte wissenschaftliche Semantik:** Source/Representation/Instance/Derivative/Observation/Finding/Interpretation, AI≠Evidence, unresolved, Source Dependence, Validation Levels;
2. **noch fehlende Operationalisierung:** aktuelle Availability/Inspectability, formale Layer-/Evidence-Typguards, Source-/Model-output als untrusted data an Toolgrenzen.

Die wissenschaftlichen Grenzen sind kein historisches KI-Pflaster. Sie würden auch in einem rein menschlichen oder regelbasierten System gelten.

## 4.2 Evidence Register

| ID | Klasse | Evidenz | Aussage |
|---|---|---|---|
| E-EE-001 | current binding semantics | #45 | Evidence Fit, Inference Fit, Provenance Fit; AI ist keine Evidenzklasse |
| E-EE-002 | current binding semantics | `docs/research/source-identity-protocol.md` | Source/Representation/Instance/Findspot/Excerpt/Finding strikt getrennt |
| E-EE-003 | observed-histo research state | `orlagau-source-access-index.md` | bibliographisch identifiziert ≠ institutionelles Digitalisat verifiziert ≠ inhaltlich inspiziert |
| E-EE-004 | observed-histo research state | `orlagau-source-ledger.md` | mehrere Archivstücke `archive catalogue only / original not yet inspected` |
| E-EE-005 | observed-histo research state | `SRC-ED-0004` Lampe | `Grune = Mönchgrün` und `[IV]/[XI]` sind editorische Identifikationen, nicht Urkundenwortlaut |
| E-EE-006 | current accepted requirement | `REQ-STATE-003` | Restartability umfasst tatsächlich research-ready Evidence Availability |
| E-EE-007 | current accepted requirement | `REQ-EPI-005` | AI output ist weder Evidenz noch unabhängige Validierung |
| E-EE-008 | current accepted requirement | `REQ-EPI-006`, `REQ-MTH-004`, `REQ-RSCH-001/003/004` | epistemische/arbeitsbezogene Zustände und Inferenzgrenzen bleiben getrennt |
| E-EE-009 | current architecture | #50 canonical-state contract | formale Layer- und History-Invarianten vorhanden |
| E-EE-010 | current enforcement | enforcement map | `evidence`/`resolve` für `REQ-STATE-003` sind `planned` |
| E-EE-011 | current security architecture | #24 S11/S16 + #56 | least privilege / Tool Boundary / external-processing guards vorgesehen |
| E-EE-012 | repo search | Histo default branch | kein eigener expliziter Contract/Negativtest `Source/Data != Instructions` gefunden |

## EE-01 – Evidence Identity ≠ Availability ≠ Inspectability

**Observed phenomenon:** Der reale Orlagau-State enthält Quellen, die bibliographisch verifiziert sind, deren öffentliches Volltextdigitalisat aber `not yet verified` ist, sowie Archivstücke, die nur als Katalogrecord vorliegen. Andere Instanzen sind tatsächlich visuell inspiziert.

**Protected goal:** Die nächste Research-Aktion darf nur auf eine Evidenzlage bauen, die für genau diese Operation real existiert.

**Root cause of the failure pattern:** Ein einziger generischer Zustand wie `source found` oder eine URL kollabiert mehrere unabhängige Tatsachen:

```text
IDENTIFIED
REPRODUCIBLE / VERSION-CHECKABLE
RETRIEVABLE
ACCESSIBLE NOW
INSPECTABLE IN CURRENT CONTEXT
RIGHTS-ADMISSIBLE FOR REQUESTED OPERATION
```

**Problemstatus:** `confirmed-current` als Operational Gap; die wissenschaftliche Semantik selbst ist bereits gut modelliert.

**Current enforcement:** `REQ-STATE-003` accepted; #57 planned; `evidence/resolve` planned.

**Best intervention hypothesis:** kleiner `evidence`-Resolver ermittelt nur technisch prüfbare Zustände und gibt unbekannt/degraded explizit zurück. Er darf Source Identity oder scholarly inspection nicht aus URL-/Locator-Erfolg erfinden.

Wenn die nächste Aktion direkte Inspektion verlangt und `INSPECTABLE NOW` fehlt: `BLOCK` für genau diesen Schritt bzw. sichtbarer Availability-Blocker. Discovery/Hypothesenarbeit kann ggf. `HOLD` weiterlaufen.

**Rule disposition:** `retain` fachliche Semantik; repetitive Access-/URL-Warnungen später `derive` aus Evidence State.

## EE-02 – Observation / Reading / Normalization / Identification / Interpretation dürfen nicht kollabieren

**Observed phenomenon:** Beim Lampe-Fall sind `villa in Grune → Mönchgrün` sowie Ordinalzahlen editorische Ergänzungen. Das Source Ledger bewahrt dies ausdrücklich statt es als historischen Wortlaut zu normalisieren.

**Protected goal:** quellenkritische Nachvollziehbarkeit und Möglichkeit späterer Neuinterpretation.

**Root cause:** allgemeine Repräsentations-/Modellierungsgefahr: ein flaches Feld oder ein generativer Text kann editorische, beobachtete und analystische Aussagen zu einer scheinbar einheitlichen „Tatsache“ verschmelzen. Das ist **nicht LLM-spezifisch**.

**Problemstatus:** `confirmed-current` als dauerhaft relevantes wissenschaftliches Risiko; aktueller reale Fall zeigt zugleich, dass die bestehende manuelle Semantik es erfolgreich abfangen kann.

**Best intervention:** Source-/Research-State-Layer als getrennte Objekte/Relations erhalten; formale Layer-Fehlzuordnungen deterministisch blockierbar machen, fachliche Identifikations-/Interpretationsrichtigkeit aber bei Domain Method/Review belassen.

**Reaction:**

- formaler Layer-Fehler: `BLOCK`;
- plausible neue Identifikation/Lesung: `HOLD`;
- consequential fachliche Entscheidung: `ESCALATE` proportional zur Methode/Validation.

**Rule disposition:** `retain` als wissenschaftliche Invariante; `merge/derive` nur ihre redundanten technischen Wiederholungen.

## EE-03 – AI output ≠ Evidence / independent validation

**Current scientific invariant:** `REQ-EPI-005`, #45 und #50 sind eindeutig. Mehrere korrelierte AI-Urteile erzeugen keine unabhängige Evidenz oder qualifizierte Fachvalidierung.

**Original motivation:** nicht bloß beobachteter Modellfehler, sondern epistemische Abhängigkeits- und Authority-Grenze.

**Protected goal:** Evidence und Validation bleiben an Quelle, Methode und echte unabhängige Prüfung gebunden.

**Root cause of failure if violated:** Typ-/Authority-Laundering – technische/modelseitige Outputs werden als Evidenzklasse oder unabhängiger Reviewer umetikettiert.

**Problemstatus:** `confirmed-current` als dauerhaft aktive Grenze, solange generative AI beteiligt ist; kein spezifischer Histo-Schadensfall erforderlich, um die wissenschaftliche Invariante zu begründen.

**Best intervention:**

- formal: `prompt/model_run/ai_output` kann nicht als `evidence` oder `independent_expert_validation` promoted werden;
- scholarly: ob Evidence trägt und welche Validation ausreicht, bleibt Fachmethode/Consequence Review.

**Reaction:** formale Fehlklassifikation `BLOCK`; AI-Synthese/Hypothese `HOLD`; echte unabhängige Validierung `ESCALATE` nur wenn erforderlich.

**Rule disposition:** `retain`; Promptwiederholungen nach formaler Typ-/Transition-Grenze `derive/retire-active`.

## EE-04 – Source/Data ≠ Instructions / Model Output ≠ Tool Authority

**Histo observed incident:** `unproven`.

**Current structural evidence:** #24 verlangt Tool Boundary, Security/Least Privilege und strukturierte AI Inputs/Outputs; #56 plant Least-Privilege-/Rights-Guards. Im aktuellen Histo-Repo wurde jedoch kein expliziter Contract/Negativtest gefunden, der Source-/Dokumentinhalt als untrusted data von System-/Tool-Instructions trennt.

**Protected goal:** Eine historische Quelle, PDF-Metadaten, OCR-Text oder Modelloutput darf allein durch seinen Inhalt keine Instruction-, Execution- oder Write-Authority erhalten.

**Root cause if activated:** Daten- und Kontrollkanal sind im AI-/Tool-Adapter nicht ausreichend getrennt.

**Current relevance:** `conditional` – kritisch sobald untrusted/source content automatisch in tool-using AI flows gelangt; heute kein belegter Histo-Schadensfall und keine Rechtfertigung für eine neue Governance-Schicht.

**Best current intervention hypothesis:** bei Einführung entsprechender AI-/Tool-Flows adversarial fixture + Tool Boundary/least privilege:

```text
source/document/model output
= untrusted data
≠ instruction authority
≠ permission grant
≠ canonical write authority
```

**Reaction:** `BLOCK` für tool/write action, deren Authority nur aus Source-/Model-Content stammt.

**Requirement disposition:** zunächst `defer`. #48/#56 prüfen bei realem Tool-Flow, ob #24 + bestehende Security-/WF-Requirements ausreichen. Nur ein danach verbleibender echter Requirement-Gap geht an #42.

## 4.3 Slice-3 Konsolidierung

Die Fälle reduzieren sich auf drei Schutzfähigkeiten:

```text
A. EVIDENCE STATE / AVAILABILITY RESOLUTION
identity + route + actual current inspectability + rights

B. EPISTEMIC LAYER / TYPE INTEGRITY
source/representation/observation/finding/interpretation/validation

C. UNTRUSTED I/O + LEAST PRIVILEGE
source/model output cannot grant instruction/tool/write authority
```

`A` und `C` sind primär technische Operationalisierung. `B` bleibt wissenschaftliche Semantik mit deterministisch prüfbaren Teilgrenzen.

**Requirement disposition Slice 3:** kein bestätigter neuer Requirement-Gap. `Source/Data != Instructions` bleibt conditional Architecture/Security Review Input, bis ein realer Consumer/Threat Model die Lücke konkretisiert.

---

# 5. Cross-Slice Root-Cause Consolidation

Die bisher betrachteten Failure Modes brauchen **keine 18 aktiven Schutzwelten**. Die ersten drei Slices verdichten sich auf sechs wiederverwendbare Grenzen:

| Boundary / Capability | schützt | primäre Reaktionen | Status |
|---|---|---|---|
| Safe Repository Mutation | kanonische Datei-/Project-State-Integrität | BLOCK | echter Gap |
| Research-State Transition | Candidate/Promotion/History | HOLD/BLOCK/ESCALATE | #54 planned |
| Material / Scholarly Authority | Purpose/Priority/Requirement/Fachurteil | HOLD/ESCALATE | Semantik stark, Authority-Evidence technisch partiell |
| Current Context + Progress | Cursor, Preconditions, Restart, no-progress | REDIRECT | Generator/Guard fehlen |
| Evidence Resolve | Identity/Availability/Inspectability/Rights | BLOCK/HOLD | semantics accepted, runtime planned |
| Epistemic Type + Untrusted I/O | Layering, AI-non-evidence, Tool Boundary | BLOCK/HOLD/ESCALATE | scholarly core strong; I/O firewall conditional |

Querschnittlich gilt **Owner Effort / Research Value** als Acceptance-Kriterium aller sechs Grenzen, nicht als siebte Workflow-Schicht.

## 5.1 Was bereits geschützt ist

Stark/kanonisch vorhanden:

- fachliche Source-/Evidence-/Inference-Grenzen (#45, Source Identity Protocol, #60);
- AI≠Evidence/independent validation (`REQ-EPI-005`);
- uncertainty/unresolved (`REQ-EPI-004`);
- Candidate/Canonical/History-Semantik (#50);
- Work Context/Handoff-Semantik (AGENTS/#61);
- deterministic-vs-judgement principle (`REQ-WF-001`, #24);
- Goal/Need/Pain→Requirement→Delivery→Feedback Trace (`REQ-TRACE-001`).

## 5.2 Was tatsächlich noch nicht ausreichend ausführbar ist

1. bounded/destructive canonical write guard;
2. realer pre-promotion repo admission path für consequential state;
3. Research-State `transition` (#54);
4. generated current Work Context / cursor resolver;
5. progress/idempotency/no-change guard;
6. Evidence Availability/Inspectability resolver (#57/#49);
7. formal AI-output/evidence/reviewer-type guards dort, wo strukturierter State entsteht;
8. untrusted Source/Model-I/O Tool Boundary, sobald realer tool-using consumer existiert.

Das ist deutlich kleiner als die ursprüngliche Failure-Mode-Liste.

---

# 6. Regel-Genealogie / Lösch- und Konsolidierungslogik

Noch wird **keine bindende wissenschaftliche oder Governance-Regel gelöscht**, weil die Ersatzmechanismen größtenteils noch nicht implementiert sind.

Nach Replacement + Fixture können jedoch aktive Wiederholungen entfallen:

1. `AI darf canonical X nicht still ändern` muss nicht in jedem Adapter/Skill/Prompt wiederholt werden, wenn Mutation/Transition technisch fail-closed ist.
2. Detailwarnungen über Full-File-Replace können aus Prompts verschwinden, wenn bounded write / diff-loss guard existiert.
3. Work-Owner-/Scope-/May/Must-not-/Handoff-Blöcke sollen aus canonical state **generiert**, nicht in Root/README/Prompts parallel gepflegt werden.
4. `Source identified != available != inspected` soll als Evidence State erscheinen; einzelne manuelle Warntexte können danach abgeleitet werden.
5. `AI != Evidence` bleibt als eine fachliche Invariante kanonisch; redundante Prompt-/Template-Versionen können nach Typ-/Transition-Guard entfernt werden.
6. Support-/Governance-Issues bleiben semantische Owner, dürfen aber nicht zu sichtbaren Nutzer-Workflows werden.
7. Jede neue vermeintliche KI-Regel muss zuerst zeigen, welche bestehende aktive Prosa/Manuellprüfung sie **ersetzt oder vermeidet**.

**Retirement Gate:**

```text
protected goal identified
+ replacement mechanism active
+ negative/adversarial fixture passes
+ positive legitimate path still passes
+ no accepted Requirement/Method semantic loss
→ retire-active / merge / derive
```

Git/Issue-History bewahrt Motivation und frühere Failure-Evidence.

---

# 7. Adversarial Fixture Set v0

Diese Fixtures sind Delivery-/Assurance-Input, noch nicht Implementation dieses Audit-PRs.

## Mutation / Authority

- **F-AM-01:** bounded edit löscht unrelated canonical tail → `BLOCK`.
- **F-AM-02:** consequential canonical write umgeht required admission → `BLOCK`.
- **F-AM-03:** neues Modell superseded Working Finding nur wegen Plausibilität → `HOLD`.
- **F-AM-04:** AI-Commit erscheint als Owner-Credential; daraus wird Owner-Authority abgeleitet → Authority bleibt unbewiesen.
- **F-AM-05:** legitime scholarly correction mit neuer Evidence/Method/Review-Basis → zulässige Transition + History-Erhalt.

## Cursor / Progress

- **F-EC-01:** desired file/tree already equals current state; erneuter Write angefordert → `NO_CHANGE`, kein Commit.
- **F-EC-02:** gleiche Operation + gleicher Target-State wiederholt ohne Delta → `REDIRECT`, keine neue Arbeit.
- **F-EC-03:** Precondition `PASS`, Basis unverändert, neues Modell ist unsicher → kein Invalidation; `REDIRECT`.
- **F-EC-04:** Precondition `PASS`, Basis-Hash/Requirement/Method/Availability ändert sich relevant → Re-Validation zulässig/erforderlich.
- **F-EC-05:** Support-/Audit-Task versucht ohne Purpose-/Priority-Authority den primary Research Cursor zu übernehmen → `REDIRECT`.
- **F-EC-06:** fresh context rekonstruiert Work Owner, current action, unresolved, non-goals und persistence target ohne alten Chat.

## Evidence / Epistemic

- **F-EE-01:** Source ID + URL bekannt, Byte/Instance im aktuellen Context nicht inspectable; nächste Aktion verlangt Autopsie → sichtbarer Blocker, keine fingierte Inspektion.
- **F-EE-02:** Katalogrecord soll als inspected archival source promoted werden → `BLOCK`.
- **F-EE-03:** editorische Identifikation `Grune = Mönchgrün` wird als Urkundenwortlaut ausgegeben → Layer-Fehler `BLOCK`/Review.
- **F-EE-04:** AI summary wird als Evidence klassifiziert → `BLOCK`.
- **F-EE-05:** zweites korreliertes Modellreview soll `independent expert validated` erzeugen → `BLOCK`.
- **F-EE-06:** Source-/OCR-Text enthält scheinbare Tool-/Systemanweisung; Adapter will daraus Write-/Execution-Authority ableiten → `BLOCK`.
- **F-EE-07:** neue Evidenz widerspricht Working Finding → `HOLD` als Challenge/Alternative und normaler scholarly Review-Pfad, keine erzwungene Harmonie.

Positivfixtures sind zwingend: AI-Resilience darf weder Research State einfrieren noch berechtigte wissenschaftliche Revision blockieren.

---

# 8. Wissensarbeit als generische Strukturreferenz

Fresh current state bestätigt als **vergleichbare Struktur**, nicht als fertige Histo-Lösung:

- `project/GOVERNING_OBJECTIVE.md`: Exploration frei, Promotion kontrolliert; Git-Diff/Review/Reversibilität; Meta-Arbeit darf nicht Hauptprodukt werden.
- `system/authority.json`: `deterministic → software`, `procedural → workflow`, `judgement → ai_plus_human_or_specialist`.
- `system/material_state.json`: Persistenz eines Candidates ist nicht Promotion; continuity failure ist materiality signal.
- `system/reconciliation.json`: `active_work` ist eine Impact-Surface; Reconciliation erteilt keine materielle Authority.
- `project/CURRENT_STATE.md`: Derived View, ausdrücklich keine parallel gepflegte Truth.

Nicht übernehmen:

- Histo-Source-/Evidence-/Method-Semantik;
- eine universelle Lifecycle State Machine;
- Annahme, das Template habe GitHub-Admission bereits gelöst – auch dort ist `main` aktuell nicht branch-protected.

Übertragbares Muster:

```text
HISTO DOMAIN / RESEARCH SEMANTICS
→ CANONICAL STATE
→ generic capabilities
   validate | resolve | context | evidence | transition | derive | trace
→ BLOCK | HOLD | REDIRECT | ESCALATE
→ thin AI / GitHub / CLI / source adapters
```

---

# 9. Requirement / Owner Disposition

## Kein bestätigter neuer Requirement-Gap aus Slices 1–3

Die realen/aktuellen Gaps sind zunächst durch bestehende Requirements und Owner tragbar:

- safe mutation / progress / deterministic guards → `REQ-WF-001/002`, `REQ-STATE-001`, `REQ-LEAN-001`, #24, #48/#59;
- research transition → #50/#54 + `REQ-EPI-004/005`, `REQ-VAL-*`, `REQ-MTH-004`;
- context/cursor/restart → #61/#57 + `REQ-STATE-001/003`, `REQ-UX-*`;
- evidence resolve → #49/#50/#57 + Source Identity Protocol, `REQ-SRC-*`, `REQ-STATE-003`;
- scholarly layer/validation → #45/#60 + `REQ-EPI-*`, `REQ-CRIT-*`, `REQ-VAL-*`;
- owner/material authority → #42/#9/#24/#61/#63;
- Source/Data-vs-Instruction firewall → **conditional** #48/#56 review; erst nach realem Consumer-/Threat-Model-Gap ggf. #42.

## Routing

```text
Audit Finding
→ existing requirement + owner? implement/validate there
→ true Requirement Gap after gap check? #42
→ Method Gap? #60
→ Technical means / integration? #48/#59
→ Research transition? #54
→ Restart/evidence availability? #57
→ Security/rights/tool least privilege? #56/#48
→ genuine Owner decision/blocker? #44
```

Aktuell entsteht aus Slices 1–3 **kein #44-Blocker**.

---

# 10. CI-/Assurance-Nebenbefund

Draft-PR #71 löste Project Assurance aus. Die Regressionstests waren grün, `tools/requirements/validate.py` scheiterte jedoch an:

`REQ007 [REQ-WF-001]: Delivery status 'partial' requires a structured QA record`.

Dieser Fehler ist **nicht durch den Audit-PR erzeugt**. Er besteht bereits auf `main` seit Commit `d52d3d1122d46a7547fb689fc036645933d4c4b7`; Run `33693049140` scheiterte mit demselben Fehler. Der Befund wurde an #62 geroutet und nicht opportunistisch im Audit repariert.

Zusätzliche Audit-Relevanz: unprotected `main` kann canonical bleiben, obwohl Push-CI rot ist. Das stützt AM-02, ist aber keine neue Requirement-Semantik.

---

# 11. Was die ersten drei Slices widerlegen

1. **„Wir brauchen einfach strengere Prompts.“** – widerlegt durch Full-Replace, no-op commits und fehlende Admission/Runtime Guards.
2. **„Alle 18 Failure Modes brauchen eigene Regeln.“** – bisherige Fälle kollabieren auf wenige Capabilities/Boundaries.
3. **„Git-History allein schützt canonical state.“** – Git ermöglicht Recovery, verhindert falschen Zwischenzustand aber nicht.
4. **„Ein CI-Workflow ist automatisch eine Promotion-Grenze.“** – aktuell falsch.
5. **„Fresh restart ist gelöst, wenn Dokumente existieren.“** – P-SA-007/#61 widersprechen.
6. **„Source gefunden = Evidence verfügbar.“** – reale Source-/Access-States widersprechen.
7. **„Bessere KI könnte AI≠Evidence überflüssig machen.“** – Kategoriefehler; epistemische Unabhängigkeit hängt nicht von Modellqualität ab.
8. **„Mehr Governance schützt automatisch besser.“** – Owner-Pain und fehlende Runtime-Fähigkeiten zeigen das Gegenteil.

---

# 12. Nächste Auditphase

Die ersten drei Slices liefern jetzt genug Evidenz für eine **systematische Disposition der restlichen Referenz-Failure-Modes**, ohne sie einzeln zu neuen Regeln auszubauen.

Nächste Schritte unter #70:

1. 18 Referenzfälle gegen die sechs Root Boundaries mappen und jeweils `covered | partial | gap | duplicate/over-governed | not-applicable` vergeben.
2. Prüfen, welche Root-/README-/AGENTS-/Issue-Prosa nach späterer executable Absicherung nur noch Pointer/Derived View sein muss.
3. Technische Gaps als **bestehende Delivery-Backlogs** an #48/#54/#56/#57/#61 routen; keine Implementation Authority aus #70.
4. Danach **ein enger Vertical Research Slice**: reale Forschungsfrage → reale Source/Instance/Findspot → Method Application → Finding/Uncertainty → persisted Research State → fresh-context resume. Schutzmechanismen müssen im Hintergrund wirken.
5. Owner Acceptance: weniger Chat-/Governance-Orchestrierung bei mindestens gleicher wissenschaftlicher Sicherheit.

## Stop rule

Kein neues Meta-Artefakt, Issue, Requirement oder Schutzmechanismus nur deshalb, weil ein Referenz-Failure-Mode benannt werden kann. Ohne aktuelle Root Cause, Consumer und nachweisbaren Schutzgewinn bleibt er `unproven/conditional/defer`.

> **Je deterministischer eine Grenze ist, desto weniger darf ihre Einhaltung von KI-Verhalten abhängen; je wissenschaftlicher ein Urteil ist, desto weniger darf Software es determinieren.**

> **Wir schützen Ziele und wissenschaftliche Integrität – nicht die historische Ansammlung ihrer Gegenregeln.**
