# Histo-Orla – Execution Plan: AI-orchestrierte externe Skill-Integration

**Stand:** 2026-09-27  
**Status:** `pre-implementation plan / PARTIAL / no implementation admission`  
**Parent Readiness:** `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`  
**Technical Owner:** #48  
**Development / Verification:** #59  
**Work Context / Handoff:** #61  
**Requirements / Constraints:** #42 + bindende Governance + explizite Owner Constraints des Planungsauftrags  
**Current planning basis:** `main@00891652761d479cc98d0752ea8d11a2ac61dcc3`  

> Ziel dieses Plans ist eine spätere Ausführung mit möglichst geringer Gesamtressource und hoher Ersttrefferwahrscheinlichkeit. Kein Work Package in diesem Dokument ist durch seine Beschreibung admitted.

---

# 1. Delivery Principle

Der Implementation-Slice wird nicht auf „kleinste technisch mögliche Änderung“ optimiert, sondern auf den **kleinsten problem-schließenden End-to-End-Umfang**:

```text
gebundene Authority
+ aktuelle externe Skill-Identität/Maturity
+ exact consumer basis
+ fail-closed update handling
+ bounded AI-owned execution
+ restartable provenance
+ real-use problem closure
```

Ein kleinerer Slice ist unzulässig, wenn er nur einen Validator, ein Manifest oder einen Prompt erzeugt, ohne den realen Skill unter Histo-Orla-Authority sicher nutzen zu können.

---

# 2. Architektur-Schnitt: vorhandene Strukturen zuerst

Der geplante Slice integriert sich in:

- `AGENTS.md` – Work-Context-/Handoff-Governance;
- `docs/architecture/operational-execution-architecture.md` – Operational Core + dünne Adapter;
- `docs/architecture/prior-art-development-inputs.md` – Cross-Repo Prior Art;
- `docs/architecture/assurance/method-conformance-work-context.md` – Work Context / Authority / STOP;
- `docs/development/work-orders/codex-rebuild-execution-contract.*` – bounded model-agnostic execution;
- `tools/operational/execution_order.py` – deterministic Work-Order checks;
- `tools/operational/mutation.py` – mechanical bounded-write/no-op protection;
- `tools/operational/core.py` – common loader/schema infrastructure;
- `tools/operational/tests/` – deterministic positive/negative regression;
- `.github/workflows/project-assurance.yml` – existing operational test discovery;
- #63 trace only when an actual implementation is admitted.

Nicht vorgesehen ist ein neuer Product Runtime / `src/histo_orla/`-Move. Der Slice ist Operational Support, solange kein realer dauerhafter Product Consumer einen anderen Boundary erzwingt.

---

# 3. Work-Package Graph

```text
WO-SKILL-P0  Safe create-target support for bounded Work Orders
        ↓
WO-SKILL-P1  External Skill Source Binding + compatibility core
        ↓
WO-SKILL-P2  Frozen real Skill pilot / Histo execution profile
        ↓
WO-SKILL-P3  Fresh-context + incompatible-update + owner-burden acceptance
        ↓
OWNER ADMISSION FOR KEEP/ADAPT/DERIVATIVE/REJECT
```

P0 ist nur deshalb eingeplant, weil der reale P1-Slice neue Dateien benötigt und `tools/operational/execution_order.py` heute jeden `scope.included_files[*].path` als bereits existente Datei verlangt. P0 ist **kein allgemeiner Workflow-Ausbau**.

---

# 4. WO-SKILL-P0 — Bounded Work Orders dürfen explizite Create Targets deklarieren

## 4.1 Problem / Gap

Der bestehende bounded Execution Contract kann existierende Dateien exakt begrenzen, aber keine legitime neue Datei als Execution Target deklarieren. Dadurch wären für den realen P1-Slice nur schlechte Alternativen möglich:

- neue Integrationsverantwortung in bestehende unpassende Dateien pressen;
- Work-Order-Guard umgehen;
- Scope nach Start erweitern.

Das wäre Scope Laundering bzw. Safety Regression.

## 4.2 Causal Driver

- Owner Constraint: kritische Zustände und vermeidbare Planungs-/Implementierungsfehler präventiv verhindern;
- `REQ-WF-001`;
- `REQ-WF-002`;
- `REQ-STATE-001`;
- `REQ-LEAN-001`;
- bestehender bounded Execution Contract unter #48/#59/#61.

## 4.3 Exact Implementation Scope Candidate

**Modify only:**

1. `docs/development/work-orders/codex-rebuild-execution-contract.md`
2. `docs/development/work-orders/codex-rebuild-execution-contract.schema.json`
3. `tools/operational/execution_order.py`
4. `tools/operational/tests/test_execution_order.py`

Kein anderes File ohne neue Admission.

## 4.4 Minimal Contract Delta

Versionierte, rückwärtskompatible Ergänzung eines Create-Target-Konzepts, z. B. semantisch:

```text
scope.included_files = existing exact files allowed to change
scope.create_files   = exact new paths allowed to be created
```

Harte Regeln:

- jeder `create_files`-Pfad ist safe-relative;
- `sources/` bleibt verboten;
- create target **muss beim Preflight fehlen**;
- existing target **muss beim Preflight existieren**;
- `check_changed_files()` erlaubt nur die Union beider Mengen;
- nach Erstellung ist ein create target kein impliziter Freibrief für andere Dateien;
- keine Glob-/Directory-Scopes;
- keine automatische Scope-Erweiterung;
- alte Work Orders bleiben semantisch unverändert gültig.

Die endgültige Feldform darf leicht variieren, wenn Review/Tests eine einfachere rückwärtskompatible Lösung ergeben; die Safety-Semantik darf nicht geschwächt werden.

## 4.5 Acceptance

- P0-A01: bestehender 0.1 Work Order bleibt PASS;
- P0-A02: exakt deklarierter fehlender create path PASS;
- P0-A03: create path, der bereits existiert, BLOCK;
- P0-A04: undeclared created file wird als scope drift BLOCK;
- P0-A05: `sources/**` create BLOCK;
- P0-A06: absolute / traversal path BLOCK;
- P0-A07: included existing path, der fehlt, bleibt BLOCK;
- P0-A08: create target erzeugt keine downstream Authority.

## 4.6 Negative / Hazard Tests

- duplicate path in included + create → BLOCK;
- target appears between preflight and mutation → refetch/revalidation required;
- directory/glob target → BLOCK;
- no-op existing change bleibt NO_CHANGE in mutation layer;
- create support darf `mutation.py`-Authority-Grenze nicht umdeuten.

## 4.7 Rollback

P0 ändert nur Contract/Validator/Tests auf Branch. Bei Regression kompletter Commit-Revert; kein Research State betroffen.

## 4.8 Execution Class

`EC-MECHANICAL` für Implementierung, **nach** Sol/Judgement-Level Review des Contract-Deltas. Stark deterministisch testbar.

## 4.9 STOP

STOP wenn:

- rückwärtskompatible Semantik nicht erreichbar ist;
- Create-Target-Support zu generischem File-Operation-DSL ausufert;
- ein einfacherer bestehender Mechanismus entdeckt wird;
- Änderung andere Authority-/Persistence-Semantik erzwingt.

---

# 5. WO-SKILL-P1 — External Skill Source Binding + Compatibility Core

## 5.1 Problem / Gap

Histo-Orla kann externes Prior Art frisch lesen, besitzt aber noch keinen kleinen ausführbaren Integrationsvertrag, der bei **einem tatsächlich konsumierten externen Skill** gleichzeitig erhält:

- konkrete upstream Identität;
- nicht-main exact ref;
- Work Owner / Review/Maturity;
- latest observed vs locally reviewed/used basis;
- compatibility disposition;
- derivative lineage;
- fail-closed update semantics.

Ein Issue-Kommentar oder Git-Pin allein schließt diese Lücke nicht.

## 5.2 Architekturform

Kleinste vorgesehene Form: **ein machine-readable source-binding record + JSON Schema + kleiner provider-neutraler evaluator + Tests + kurzer Contract**.

Kein Netzwerkclient gehört in den Core. Ein Execution Adapter (z. B. aktuell GitHub-Connector in Work/Codex) liefert einen frisch gelesenen `observed upstream snapshot`. Der Core beurteilt nur formale Identität/Delta-/Disposition-Invarianten.

Damit bleibt:

- Live-Providerzugriff austauschbar;
- Histo Core testbar;
- Credential/Tooling keine Authority;
- Semantic Compatibility ein sichtbares Judgement, nicht erfundener Determinismus.

## 5.3 Exact File Topology Candidate

**Create:**

1. `docs/architecture/contracts/external-skill-source-binding.md`
2. `tools/operational/external_skill_binding.schema.json`
3. `tools/operational/external_skill.py`
4. `tools/operational/external-skills.json`
5. `tools/operational/tests/test_external_skill.py`

**Modify only if required by existing test/index conventions:**

6. `docs/architecture/README.md`

`.github/workflows/project-assurance.yml` muss voraussichtlich **nicht** geändert werden, weil `tools/operational/tests/test_*.py` bereits vollständig entdeckt wird. Eine Workflow-Änderung ist nur bei nachgewiesenem Test-Discovery-Gap zulässig.

## 5.4 Binding Record – minimale Semantik

Der Record soll nur Integrationsmetadaten besitzen, keine kopierte Skill Truth. Mindestens:

```text
binding_id
source_repository
source_owner_refs
tracking_ref
last_observed_ref
last_observed_status
last_observed_maturity
consumer_capability
locally_reviewed_basis_ref
compatibility_state
compatibility_evidence_refs
local_derivative_ref?          # optional
local_derivative_reason?       # optional
reconciliation_policy_ref
```

### Bedeutungen

- `tracking_ref`: wie der relevante Upstream-State gefunden wird, z. B. PR/Issue/branch selector; kein automatisches Trust-Signal.
- `last_observed_ref`: zuletzt frisch beobachteter Upstream-Ref.
- `locally_reviewed_basis_ref`: exact Ref, gegen den Histo Compatibility/Use tatsächlich geprüft hat.
- `compatibility_state`: mindestens `unreviewed | compatible | incompatible | unresolved | stale`.
- `local_derivative_*`: nur wenn wirklich vorhanden; keine prophylaktische Kopie.

Nicht im Record:

- Histo Requirements-Prosa;
- Histo Method Truth;
- vollständige Upstream Skill-Inhalte;
- Model/Providerwahl;
- Projektpriorität;
- Implementation Admission.

## 5.5 Observed Upstream Snapshot

Der adapterseitig frisch gelesene Snapshot muss für den Pilot mindestens enthalten:

```text
source_repository
work_owner/status
runtime_pr/status
exact_head_ref
base_ref
review/maturity markers
source_paths
observed_at
```

Die konkrete Snapshot-Repräsentation kann transient bleiben; nur material veränderte Binding-/Review-Ergebnisse müssen persistent werden.

## 5.6 Deterministische vs judgement-basierte Disposition

### Deterministisch

- Repo/ref/status fields syntaktisch gültig;
- exact ref gleich/ungleich;
- source paths vorhanden;
- locally reviewed basis referenziert;
- derivative lineage vollständig;
- status changed / ref changed;
- current binding stale gegenüber supplied snapshot.

### Judgement

- semantische Compatibility;
- Method-Fit;
- ob ein Delta Histo Requirements/Method/Quality berührt;
- ob lokales Derivat sinnvoll ist;
- ob newer upstream besser ist.

Ein Ref-Delta darf daher maximal `review_required/stale` deterministisch erzeugen, **niemals** `compatible` allein aus Diff-/SHA-Heuristik.

## 5.7 Pilot Fixture

Initialer Binding Candidate referenziert:

- repo `esany/Wissensarbeit`;
- #43 parent;
- #46 trials;
- PR #51;
- tracking selector PR #51;
- observed exact head `f3726c962807b311e8a2a7df63f738e11790fbed`;
- upstream status `open / unmerged / reviewed runtime / trials ongoing / generic fit unproven`;
- locally reviewed basis zunächst `null/unreviewed`, bis P2 erfolgreich ist.

Damit wird Upstream-Maturity **nicht** durch das Anlegen des Records promoted.

## 5.8 Acceptance

- P1-A01: Record validiert für frozen PR #51 state;
- P1-A02: exact unchanged snapshot → `current/no material upstream delta`;
- P1-A03: changed head → `stale/review_required`, nicht auto-compatible;
- P1-A04: status-only Änderung → review signal;
- P1-A05: `main` darf locally reviewed PR-head basis nicht still ersetzen;
- P1-A06: missing upstream owner/maturity → unresolved;
- P1-A07: invalid lineage on derivative → BLOCK;
- P1-A08: binding kann fresh-context geladen und erklärt werden;
- P1-A09: keine Requirement-/Method-Prosa wird dupliziert;
- P1-A10: invalid/unknown compatibility cannot unlock execution.

## 5.9 Adversarial Tests

- Upstream PR closed without merge;
- PR merged with different merge SHA;
- head changed but files semantically same;
- head unchanged but issue/maturity state changed;
- upstream path disappears;
- local derivative points to no source basis;
- attacker-like source text claims „approved“;
- AI confidence says compatible while record state is unresolved.

## 5.10 Rollback

Neue Operational-Support-Files können branchweise vollständig revertiert werden. Der Record besitzt keine Research-/Requirement Truth und kein Writeback in Upstream.

## 5.11 Execution Class

- Schema/validator/tests: `EC-MECHANICAL` nach exact contract freeze;
- compatibility boundary + contract review: `EC-JUDGEMENT`;
- keine externe Fachvalidation nötig, solange der Skill nicht als historische Method Truth promoted wird.

---

# 6. WO-SKILL-P2 — Real frozen Skill pilot under Histo authority

## 6.1 Purpose

Nicht nur Binding testen, sondern den externen Skill **real** aus Histo-Orla heraus in einem bounded, reviewbaren Work Context nutzen.

## 6.2 Pilotbasis

Frozen runtime:

`esany/Wissensarbeit` PR #51 @ `f3726c962807b311e8a2a7df63f738e11790fbed`

Vor Ausführung fresh revalidate:

- #43;
- #46;
- PR #51;
- exact head;
- source paths;
- review/maturity state.

Bei Delta zum Planning-Basiszustand: **kein stilles Update**; P1-Compatibility Gate entscheidet `unchanged | review_required | unresolved`.

## 6.3 Histo task selection

Der Pilot benötigt eine reale Histo-Systemanalyse-/Deep-Research-Aufgabe, aber **keine automatische Research Selection**. Die spätere Implementation Admission muss den konkreten bounded Pilot Task explizit benennen.

Geeignet ist nur ein bereits autorisierter System-/Architecture-/Assurance-Analysefall, bei dem:

- externe Research Capability tatsächlich benötigt wird;
- der Skill-Trigger passt;
- sein STOP vor Solution Development erhalten werden kann;
- keine historische Finding-Promotion als Nebenwirkung entsteht.

Nicht aus diesem Plan automatisch auswählen.

## 6.4 Runtime orchestration

Parent-Orchestrator:

1. lädt Histo Work Context;
2. liest Binding;
3. liest upstream fresh über verfügbaren authorised Adapter;
4. revalidiert exact source basis/maturity;
5. lädt Skill-Dateien by exact ref;
6. erstellt bounded task context;
7. routet mechanische Vorarbeit möglichst billig;
8. hält systemische/semantic judgement in starker Execution Class;
9. sammelt Resultate;
10. führt deterministic checks aus;
11. STOP am Skill-/Work-Order-Ende;
12. persistiert nur im admitted Persistence Target.

Der Owner muss keine Worker-Chats manuell erstellen/verbinden.

## 6.5 Current execution-surface candidates

Stand Sep 2026 sind ChatGPT Work, Codex und – abhängig von Plan/Workspace – Workspace Agents aktuelle mögliche Execution Surfaces. Diese Namen sind **nicht** Teil des Work Orders.

Preflight muss aktuell prüfen:

- GitHub read/write capability;
- ability to load exact refs/files;
- available model/reasoning classes;
- ability to keep orchestration AI-owned;
- approval controls for consequential actions;
- inspectability/audit trail;
- quotas/cost constraints.

Wenn kein aktueller Modus AI-owned multi-worker orchestration hinreichend bietet, darf der Parent die Arbeit selbst/sequenziell ausführen oder mechanische Teile in Tools auslagern. **Kein Fallback auf Human-as-router.**

## 6.6 Pilot Evidence to persist

- exact Histo basis SHA;
- exact Binding version;
- fresh upstream snapshot refs/status;
- exact Skill ref/source paths;
- selected Histo Work Order;
- execution capability/mode class (not authority);
- bounded context refs;
- output;
- source/evidence boundaries;
- STOP result;
- failure/limitations;
- owner-burden observation;
- Problem Closure assessment.

## 6.7 Acceptance

- P2-A01: Skill can be loaded/usefully executed by exact ref;
- P2-A02: Histo authority remains controlling;
- P2-A03: Skill STOP is preserved; no solution/implementation cascade;
- P2-A04: upstream candidate maturity remains visible;
- P2-A05: result is restartable from repo;
- P2-A06: no Histo semantic truth copied into Skill binding;
- P2-A07: owner does not manually orchestrate worker contexts;
- P2-A08: result materially advances the selected real Histo question;
- P2-A09: execution cost/context is captured sufficiently for later routing calibration;
- P2-A10: any failure is classifiable as source-binding / execution-surface / model / Skill-method / host-context / authority issue.

---

# 7. WO-SKILL-P3 — Falsification / restart / incompatible evolution

P3 is part of problem closure, not optional polish.

## 7.1 Required scenarios

### F1 — Fresh-context restart

New execution context receives only repo bootstrap + binding + Work Order and resumes correctly.

### F2 — Upstream head changed

Synthetic or real snapshot with different exact head must trigger `review_required`, not auto-update.

### F3 — Maturity-only change

Same SHA, changed PR/owner/trial status must remain semantically visible.

### F4 — Incompatible semantic change

Adversarial fixture changes an authority/STOP/method boundary. Histo must retain last reviewed basis and refuse auto-adoption.

### F5 — Local derivative candidate

Without actually creating a permanent fork unless needed, prove the lineage contract can represent:

- source repo;
- source basis ref;
- local delta reason;
- incompatibility reason;
- reconciliation/rebase policy;
- continuing upstream tracking.

### F6 — Owner-GO no-cascade

A bounded pilot admission cannot authorize follow-on adapter/derivative/merge work.

### F7 — Platform boundary

Demonstrate honestly which actions are repo-enforced versus platform approval/procedural only.

### F8 — Owner burden

Compare AI-owned orchestration against manual multi-chat routing. If owner still has to courier context/results, Problem Closure fails.

## 7.2 Kill / correction criteria

Shrink/adapt/reject the integration if:

- a simple fresh-read-by-reference approach gives equivalent safety/restartability without persistent binding record;
- compatibility state cannot be made reviewable without large framework machinery;
- owner meta-work is not reduced;
- source binding duplicates upstream or Histo truth;
- resource savings depend on context starvation;
- agent orchestration adds more maintenance than it removes;
- exact ref/maturity cannot be reconstructed reliably;
- provider-specific code becomes dominant without demonstrated need.

---

# 8. Work-Order Preparation Rules

No machine-readable Implementation Work Order should be marked ready/admitted until:

1. this plan has fresh independent adversarial review;
2. P0 design is accepted as the minimal create-target fix;
3. exact implementation branch basis is refreshed;
4. current requirements/owner constraints are revalidated;
5. exact file list/create list is frozen;
6. all required tests are named;
7. no current critical `unresolved` remains;
8. runtime environment can install/run test dependencies;
9. current execution surface/capabilities are checked;
10. separate Owner Implementation GO exists.

## Draft Work-Order identities

Reserve semantic identities only; these are **not admitted Work Orders**:

- `WO-SKILL-P0-CREATE-TARGETS`
- `WO-SKILL-P1-SOURCE-BINDING`
- `WO-SKILL-P2-REAL-PILOT`
- `WO-SKILL-P3-FALSIFICATION`

After Owner GO, instantiate the currently selected package in JSON against the then-current Work-Order schema and current basis SHAs. Do not pre-create an `admitted` JSON artifact that could later be mistaken for live authority.

---

# 9. Model-/Token-Economy Plan

Canonical Work Orders remain model-agnostic.

At execution time, use current capability discovery and classify each subtask:

| Task | Default class | Escalate when |
|---|---|---|
| repo/file inventory, ref checks | EC-MECHANICAL | conflicting source identity/status |
| schema/test implementation | EC-MECHANICAL | contract ambiguity/architecture drift |
| repetitive fixture generation | EC-MECHANICAL | fixture encodes judgement semantics |
| source-binding status comparison | EC-MECHANICAL | semantic compatibility unclear |
| compatibility review | EC-JUDGEMENT | specialist domain semantics implicated |
| architecture reconciliation | EC-JUDGEMENT | material owner decision required |
| independent adversarial plan/code review | EC-JUDGEMENT | critical specialist validation needed |
| owner acceptance | Human Owner | never delegated as AI judgement |

Cost optimisation target:

```text
strong enough planning/specification
→ bounded cheap/mechanical execution where safe
→ deterministic tests
→ strong independent review
→ real-use acceptance
```

Do not optimise a single worker token budget at the cost of extra failed runs or owner orchestration.

---

# 10. Pre-Implementation Safety Gate

Before any code mutation, derive:

```text
repo state ready?
runtime environment ready?
upstream source state revalidated?
work order scope exact?
create targets safe?
authority/admission current?
critical unresolved = none?
positive + negative tests declared?
rollback known?
persistence target exact?
```

Any `no` → `BLOCKED` or `UNRESOLVED`, no code mutation.

This explicitly preserves the historical #119 learning:

> `repo-ready != Work-runtime-ready`.

---

# 11. Independent Review Contract

A fresh strong review context must receive only:

1. `AGENTS.md`;
2. current `PROJECT_STATE.md` + warning about staleness if still applicable;
3. #42/#48/#59/#61 controlling owner refs;
4. Readiness artifact;
5. this execution plan;
6. exact Wissensarbeit #43/#46/#52/#55 + PR #51 refs;
7. relevant #70/self-audit evidence;
8. no hidden chat rationale.

Review questions:

- Ist das rekonstruierte Owner-Problem korrekt oder bereits solution-framed?
- Schließt P0–P3 wirklich das Problem oder nur Integrationsmetadaten?
- Ist P0 echte prerequisite oder Infrastructure Creep?
- Ist ein persistent binding record begründet oder reicht fresh-read-by-reference?
- Kann die Semantik noch kleiner ohne Loss werden?
- Fehlt eine Critical State / Recovery Class?
- Werden platform approvals fälschlich als repo-enforceable behandelt?
- Kann ein günstiger Worker an irgendeiner Stelle Authority/Judgement übernehmen?
- Bleibt PR #51 Maturity korrekt erhalten?
- Gibt es einen einfacheren Existing-Tool-Ansatz?
- Ist AI-owned orchestration realistisch ohne Human-as-router?
- Sind alle New-File/Write-Surfaces bounded?
- Entsteht ein zweiter Truth Store?
- Ist das Review selbst unabhängig genug?

Disposition jedes Findings:

`accept | refine | reject | unresolved`

Erst danach kann `READY FOR OWNER ADMISSION` behauptet werden.

---

# 12. Current Readiness / Blockers

## Planung abgeschlossen

- Problem/Intent rekonstruiert;
- Source Roles getrennt;
- bestehende Mechanismen und Prior Art reconciliert;
- kein neuer Requirement-Gap behauptet;
- smallest problem-closing architecture bounded;
- realer Pilot festgelegt;
- Dependency Graph vorhanden;
- Hazards/Recovery vorhanden;
- Acceptance/negative/adversarial tests vor Code definiert;
- Ressourcen-/Orchestrierungslogik modellagnostisch geplant;
- exact candidate file topology vorhanden.

## Noch offen vor `READY FOR OWNER ADMISSION`

1. **Fresh independent adversarial review** dieses Planning Heads.
2. Review-Disposition.
3. Danach final bestätigen, dass P0 tatsächlich nötig/minimal bleibt und P1 file topology nicht vereinfacht werden kann.

## Kein neuer Owner-Blocker

Es ist derzeit keine neue #44-Decision erforderlich. Der bestehende Branch-Protection-Blocker bleibt unverändert.

## Aktueller Status

**`PARTIAL / INDEPENDENT REVIEW REQUIRED / NO IMPLEMENTATION AUTHORITY`**

---

# 13. Handoff

Ein neuer Planning Reviewer soll ohne Chat fortsetzen können aus:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `README.md`
- #42/#48/#59/#61/#63
- `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`
- diesem Plan
- Wissensarbeit #43/#46/#48/#52/#53/#55 und PR #51 frisch gelesen.

**STOP: Keine Implementierung vor separatem Owner-GO.**
