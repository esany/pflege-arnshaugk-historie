# Histo-Orla – AI-orchestrierte externe Capability-Integration: Readiness Plan

**Stand:** 2026-09-28  
**Status:** `PARTIAL / independent findings dispositioned / fresh closure review required / no implementation authority`  
**Work Owner:** #48  
**Development / Verification:** #59  
**Work Context / Handoff:** #61  
**Requirements:** #42 unchanged  
**Restartability / Provider Removal:** #57  
**Traceability:** #63  
**Histo basis:** `main@00891652761d479cc98d0752ea8d11a2ac61dcc3`  
**Wissensarbeit basis:** `main@9b16601c3550bde37ed4410eec3cec3bd6aa6846`  
**Pilot upstream:** Wissensarbeit PR #51 @ `f3726c962807b311e8a2a7df63f738e11790fbed`  
**Independent review evidence:** `ai-orchestrated-skill-integration-independent-review-findings-20260928.md`

> Dieser Plan ist keine Implementation Admission, keine Requirement-/Method-Promotion und keine Product-Multi-Agent-/Workflow-Architektur. Er dokumentiert den kleinsten derzeit begründbaren problem-schließenden Pfad und stoppt vor Implementierung.

---

## 1. Owner-Problem und Problem Closure

Histo-Orla soll relevante, sich entwickelnde externe Skill-/Capability-Pakete **aktuell, authority-sauber, restartbar und dauerhaft nutzbar** machen können, ohne:

- fremde Semantik zur Histo-Orla-Authority zu machen;
- blind `latest` zu übernehmen;
- Upstream Review mit lokaler Zulassung zu verwechseln;
- bei Upstream-Evolution oder Providerverlust den letzten funktionierenden lokalen Basisstand zu verlieren;
- den Owner zum Agenten-/Chat-Orchestrator zu machen;
- eine Registry-, Workflow-, Agenten- oder Policy-Plattform auf Vorrat zu bauen;
- Analysis/Review-GO still in Persistence/Implementation/Follow-up-Authority zu erweitern.

### Problem-Closure-Contract

Für den ersten realen Pilot ist der Slice erst geschlossen, wenn ein frischer AI-Orchestrator aus Repo-State:

1. die externe Capability und ihre Tracking Identity kennt;
2. den aktuellen Upstream-Zustand bei consequential Nutzung frisch liest;
3. Upstream Owner/Review/Maturity als externe Observation von Histo-Authority trennt;
4. einen exact frozen Basisstand als **local trial basis** verwenden kann;
5. bei Upstream-Delta nicht still aktualisiert;
6. den exact locally allowed Basisstand auch ohne aktuellen Upstreamzugriff wieder ausführen kann;
7. Scope, MAY/MUST NOT, STOP, Persistence und no-cascade aus Histo Work Context/Work Order kennt;
8. einen realen bounded Trial ausführen kann, ohne daraus automatisch Operational Admission abzuleiten;
9. nach Trial + Review getrennt über lokale Operational Admission entscheiden kann;
10. die Arbeit AI-seitig orchestriert, ohne den Owner zum Workflow-Router zu machen.

Ein Pin, Manifest, Validator oder Remote-SHA allein schließt diesen Slice nicht.

---

## 2. Source-Role- und Authority-Trennung

| Objekt | Rolle | Darf nicht bedeuten |
|---|---|---|
| Wissensarbeit #43/#46/PR #51 | external prior-art / upstream maturity evidence | Histo local admission |
| frozen upstream commit | Source Identity / source basis | current upstream forever |
| dated fresh observation | Evidence, was zu Zeitpunkt X upstream sichtbar war | persistierte `current truth` |
| local availability derivative | immutable execution-sufficient Kopie eines exact basis | neue Skill Truth / generische Compatibility |
| local trial admission | bounded Histo-Erlaubnis für exact Pilot | operational/general admission |
| local operational admission | nach Trial + Review definierte lokale Zulassung | generic fit / upstream promotion |
| AI/Tool/Connector/Credential | Execution Capability | Authority |

Owner Constraint bleibt:

> **User GO, Assistant Initiative.** AI besitzt Initiative für Analyse, Routing, Orchestrierung und Vorschläge; persistente/externe Mutation und materielle Folgephasen benötigen sichtbar gebundene Authority. Authority kaskadiert nicht still.

Der Plan behandelt dies weiterhin als expliziten Owner Constraint, nicht als automatisch neues #42 Requirement.

---

## 3. Independent-Review-Reconciliation

Der fresh independent Review des früheren Planning Heads meldete F-01..F-07. Projektseitige Detail-Disposition: `ai-orchestrated-skill-integration-independent-review-findings-20260928.md`.

Ergebnis:

- F-01 Trial/Operational Admission: **bestätigt und getrennt**;
- F-02 generischer P1 Binding-Core: **verworfen/deferred**;
- F-03 P0: **conditionalized**;
- F-04 durable identity vs availability: **auf recoverable locally allowed basis geschärft**;
- F-05 write surface: **harte Admission-Precondition**;
- F-06 identity/observation/maturity/local disposition: **getrennt**;
- F-07 #48-owned Pilot: **beibehalten**.

Kein neues Requirement und keine generische Agent-/Workflow-/Registry-Architektur folgt daraus.

---

## 4. Minimality Discriminator

### Alternative A — existing Work Context / reference-only

Vorhandene Histo-Mechanismen können bereits binden:

- Work Owner / primary function;
- exact task scope;
- accepted Requirements / constraints;
- external canonical refs in required context;
- semantic / acceptance authority;
- MAY / MUST NOT / STOP;
- persistence target;
- fresh basis revalidation;
- delta-only return / handoff.

Damit sind Authority, trial scope, fresh resolution und no-cascade grundsätzlich ohne neuen Binding-Core lösbar.

**Failure:** reference-only garantiert keine recoverable execution-sufficient Basis, wenn der aktuelle Upstream/Provider später nicht mehr erreichbar ist.

### Alternative B — existing Work Context + concrete immutable Availability Derivative

Ergänzung nur des nach A fehlenden Schutzguts:

- exact execution-sufficient Bytes des frozen Pilotpakets lokal immutable erhalten;
- source repo/ref/path + source blob identities erhalten;
- lokale Kopie explizit als `availability derivative` markieren;
- keine lokale Kopie als `current upstream`, Skill Truth oder Compatibility-Beweis verwenden;
- fresh upstream bei consequential Nutzung weiterhin neu lesen;
- lokale Kopie darf nur durch explizite Trial-/Operational-Admission verwendet werden.

**Disposition:** kleinste derzeit problem-schließende Option.

### Alternative C — generischer Binding-/Compatibility-Core

`Contract + JSON Schema + Evaluator + Registry/Binding Store`.

**Disposition:** `reject/defer`. Für den ersten Pilot existiert kein nachgewiesener Failure, den B nicht kleiner schließt. Wiederholte reale Friktion darf später eine Generalisierung begründen.

---

## 5. Durable Availability Semantik

Verbindliche Trennung:

```text
IDENTIFIED
→ TRACKABLE
→ RETRIEVABLE NOW
→ EXECUTION-AVAILABLE NOW
→ RECOVERABLE WITHOUT CURRENT UPSTREAM
```

Der erste problem-closing Slice verlangt für eine lokal trial-/operational erlaubte Basis die letzte Stufe.

Das erzeugt **keine** prophylaktische Vendor-/Mirror-Plattform. Für den Pilot genügt eine immutable lokale Availability-Derivation der drei execution-sufficient Upstream-Dateien.

Frozen source basis:

`esany/Wissensarbeit@f3726c962807b311e8a2a7df63f738e11790fbed`

| Source file | Git blob SHA |
|---|---|
| `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

Die lokale Preservation darf diese Dateien nicht semantisch bearbeiten. Jede spätere lokale Modifikation wäre eine neue Derivation mit eigener Lineage und separatem Review.

---

## 6. Admission State Model

```text
UPSTREAM REVIEWED BASIS
external evidence only
        ↓
LOCAL TRIAL ADMISSION
exact source/snapshot + exact task + exact authority
        ↓ real trial
TRIAL EVIDENCE + REVIEW
        ↓
LOCAL OPERATIONAL ADMISSION | ADAPT | REJECT | UNRESOLVED
```

### Local Trial Admission

Muss mindestens binden:

- exact capability basis;
- exact Histo task;
- current upstream fresh observation;
- local availability derivative identity;
- scope / required evidence;
- MAY / MUST NOT;
- STOP;
- output/persistence target;
- no generic compatibility claim;
- no downstream implementation/architecture authority.

### Operational Admission

Kann erst nach Trial + Review entstehen. Sie ist auf den explizit akzeptierten lokalen Einsatz begrenzt und behauptet weder Wissensarbeit Generic Fit noch Histo Method Truth.

---

## 7. Current Upstream Semantics

Persistent dürfen gehalten werden:

- Tracking Identity;
- exact locally trial-/reviewed/admitted basis;
- immutable availability derivative + provenance;
- datierte Observation Evidence;
- Review-/Admission-Evidence.

Nicht persistent als scheinbar aktuelle Wahrheit:

- `current upstream maturity`;
- `latest compatible`;
- `currently approved upstream`.

Bei consequential Nutzung:

```text
tracking identity
→ fresh upstream resolution
→ compare against local basis
→ unchanged | delta-detected | unavailable | unresolved
→ judgement/review if material
```

Deterministik darf Delta/Staleness/Lineage feststellen, nicht semantische Compatibility erfinden.

---

## 8. Safe Implementation Surface

Jede spätere technische P0/P1-Mutation benötigt vor Start:

```text
fresh isolated checkout/worktree or equivalent isolated filesystem surface
→ exact admitted basis verification
→ branch-scoped mutation
→ tests in the same checkout
→ exact changed-file scope check
→ diff review
→ delta-only return
```

Direkte Contents-API-/Connector-Writes sind **kein** zulässiger Ersatz für diese Implementation Surface. `tools/operational/mutation.py` schützt mechanische lokale Writes, entscheidet aber keine Authority.

Kann der Executor diese Surface nicht bereitstellen: `BLOCKED`.

---

## 9. Revised Hazard Register

| Hazard | Prevention / fail-closed |
|---|---|
| upstream review → lokale Authority laundering | separate local trial admission required |
| latest/head silently replaces local basis | fresh delta detection; no auto-upgrade |
| stale observation becomes current truth | dated observation only; current always fresh-resolved |
| provider/upstream disappears | immutable local availability derivative |
| local snapshot becomes second truth | immutable derivative role + exact source lineage; no editing/currentness claim |
| semantic compatibility determinized | only delta/lineage mechanically checked; compatibility requires review |
| direct GitHub write bypasses local guards | isolated filesystem/Git surface required |
| P0 infrastructure becomes general DSL | exact `create_files` only; no glob/directory/generic operation model |
| trial creates operational admission automatically | explicit post-trial review/admission gate |
| owner becomes chat router | AI orchestrates; owner gates only material admission |
| scarce executor used for planning | Chat/GitHub for planning/review; executor only for non-substitutable filesystem/Git implementation |

---

## 10. Resource Economy

Before Owner Implementation GO:

- normal Chat + GitHub only;
- no scarce Work/Codex executor;
- no model/provider encoded into canonical work orders.

If the revised plan passes closure review, expected scarce execution is at most **one isolated implementation run** for the technical enabling delta + concrete preserved pilot basis, with explicit staged authority:

```text
Stage A: P0 create-target support (only because Stage B needs new files)
→ tests / revalidate
Stage B: immutable pilot availability derivative + provenance
→ tests / diff / STOP
```

Both stages must be explicitly bound by the later Owner GO; Stage B does not inherit authority merely because Stage A passed.

P2 real trial and P3/fresh-context falsification remain normal-Chat-first and are not automatically part of that scarce run.

---

## 11. Quality Gate

| Dimension | Current state | Reason |
|---|---|---|
| Intent Fidelity | PASS | owner problem preserved |
| Problem-Closure Fidelity | PASS in revised design | recoverable availability added; no scope laundering |
| Source-/Role Fidelity | PASS | upstream/review/observation/local admission separated |
| Authority Fidelity | PASS in plan | trial vs operational admission + no cascade |
| Current-State Fidelity | PASS | current main/upstream refs freshly revalidated 2026-09-28 |
| Dependency Completeness | PASS in plan | P0 conditional cause now explicit |
| Critical-State Prevention | PASS in plan | isolated write surface + fail-closed gates |
| Forbidden Loss | PASS in plan | last allowed basis remains recoverable |
| Boundedness | PASS | generic binding core removed |
| Reversibility / Recovery | PASS in plan | branch-scoped changes + immutable source derivative |
| Test-before-Code | PASS in plan | exact tests in execution plan |
| Determinism Boundary | PASS | semantic compatibility remains judgement |
| Assurance Calibration | PASS | planning/review/admission/implementation remain distinct |
| Resource Efficiency | PASS | planning free-chat-first; one scarce run maximum expected |
| AI-owned Orchestration | PASS in plan | no human routing loop |
| Owner Burden | PASS in plan | owner only at material admission boundaries |
| Independent Challenge | PASS for old plan / PARTIAL for revised delta | revised snapshot topology not yet freshly challenged |
| Restartability | PASS in design | repo refs + recoverable exact basis |
| One Canonical Home | PASS | no registry/second Skill truth |
| No Architecture-before-Need | PASS | generic core removed |
| No Scope Laundering | PASS | durable availability preserved rather than renamed away |

---

## 12. Readiness Verdict

**Current verdict:**

`PARTIAL / BLOCKING FINDINGS DISPOSITIONED / FRESH CLOSURE REVIEW REQUIRED / NO IMPLEMENTATION AUTHORITY`

F-01..F-06 are materially dispositioned. The remaining gate is intentionally narrow: a fresh reviewer must challenge the **newly minimized delta**, chiefly the concrete local Availability-Derivation topology and the now-evidenced P0 necessity.

No further broad architecture audit is requested.

If that closure review returns `READY` or only non-blocking refinements and no new material problem emerges, the plan can move to `READY FOR OWNER ADMISSION` without another discovery cycle.

No Implementation Work Order is admitted by this status.