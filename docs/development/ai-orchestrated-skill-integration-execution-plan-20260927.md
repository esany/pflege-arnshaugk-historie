# Histo-Orla – Revised Execution Plan: AI-orchestrierte externe Capability-Integration

**Stand:** 2026-09-28  
**Status:** `pre-implementation / PARTIAL / closure-review-required / no implementation admission`  
**Parent:** `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`  
**Independent findings:** `docs/architecture/assurance/ai-orchestrated-skill-integration-independent-review-findings-20260928.md`  
**Technical Owner:** #48  
**Development / Verification:** #59  
**Work Context / Handoff:** #61  
**Current Histo basis:** `main@00891652761d479cc98d0752ea8d11a2ac61dcc3`

> Der frühere feste Graph `P0 → generic P1 core → P2 → P3` ist verworfen. Dieser Plan enthält nur den nach Independent Review verbleibenden problem-schließenden Delta. Kein Schritt ist durch dieses Dokument admitted.

---

## 1. Revised Delivery Graph

```text
R-CLOSE  fresh closure review of revised delta
        ↓ if READY
OWNER GO binds exact implementation stages
        ↓
E0  conditional create-target support
    condition: E1 requires legitimate new files
        ↓ tests + same-checkout revalidation
E1  concrete immutable Availability Derivative of frozen pilot package
        ↓ full tests + diff + STOP
NORMAL-CHAT REVIEW of E0/E1 delta
        ↓ separate trial admission
T1  real #48-owned bounded Skill trial
        ↓ review
V1  fresh-context / upstream-delta / source-unavailable / owner-burden falsification
        ↓
OWNER / LOCAL ADMISSION DECISION
keep | adapt | reject | unresolved
```

E0 und E1 dürfen später in **einem** isolierten executor run laufen, wenn ein einzelner Owner GO beide Stufen ausdrücklich und separat bindet. E1 erhält keine Authority allein aus E0-PASS.

T1/V1 werden nicht in diesen scarce implementation run vorgezogen.

---

## 2. What was removed

Nicht mehr geplant:

- generisches `external_skill_binding.schema.json`;
- generischer Compatibility Evaluator;
- persistente External-Skill Registry;
- persistierter `current upstream`-/`latest compatible`-State;
- automatisches semantisches Compatibility-Scoring;
- Product Skill Manager / Workflow Engine / Multi-Agent Runtime.

Grund: Existing Work Context / bounded Work Order deckt Authority, Scope, refs, STOP, fresh basis und handoff bereits ab. Für den Pilot blieb nur recoverable Availability als echter Gap.

---

# 3. E0 — Conditional exact create-target support

## 3.1 Why E0 is now legitimately required

Der Minimality Discriminator wurde ausgeführt:

- reference-only schließt Authority/Freshness/Trial-Binding;
- er schließt nicht recoverable execution availability;
- E1 benötigt deshalb vier legitime neue snapshot files;
- `tools/operational/execution_order.py` blockiert heute jeden execution target, der beim Preflight nicht bereits als Datei existiert.

Damit ist die ursprünglich konditionale E0-Bedingung **für diesen Pilot erfüllt**.

E0 bleibt Enabler, kein eigenständiger Produktzweck.

## 3.2 Exact modify scope candidate

Nur:

1. `docs/development/work-orders/codex-rebuild-execution-contract.md`
2. `docs/development/work-orders/codex-rebuild-execution-contract.schema.json`
3. `tools/operational/execution_order.py`
4. `tools/operational/tests/test_execution_order.py`

Kein anderes File ohne erneute Admission.

## 3.3 Required semantics

Der Contract muss exact new-file targets von exact existing-file targets unterscheiden können.

Semantisch erforderlich:

```text
existing change target
= path must exist at preflight

create target
= exact path must not exist at preflight
```

Harte Invarianten:

- safe relative paths only;
- keine Globs/Directories;
- `sources/**` bleibt verboten;
- included + create dürfen sich nicht überschneiden;
- existing target missing → BLOCK;
- create target already exists → BLOCK/revalidation;
- changed-file check erlaubt nur explizit gebundene existing + create targets;
- keine Scope-Erweiterung nach Start;
- alte Work Orders bleiben gültig;
- create support erzeugt keine neue Authority.

Schema-Versionierung muss beim Closure-/Implementation-Review sauber entschieden werden; additive Backward Compatibility ist Pflicht. Kein stilles inkompatibles Reinterpretieren vorhandener 0.1 Work Orders.

## 3.4 Acceptance

- E0-A01 existing current work-order fixtures bleiben PASS;
- E0-A02 exact missing create path PASS;
- E0-A03 create path already present BLOCK;
- E0-A04 undeclared new file BLOCK;
- E0-A05 duplicate existing/create path BLOCK;
- E0-A06 absolute/traversal/source path BLOCK;
- E0-A07 existing target missing BLOCK;
- E0-A08 stale path state between preflight/mutation → revalidation required;
- E0-A09 no model/provider fields introduced;
- E0-A10 no downstream authority implied.

## 3.5 STOP

STOP if:

- implementation grows into a generic file-operation DSL;
- backward compatibility cannot be maintained;
- changed-file scope cannot include exact create targets safely;
- a simpler existing exact-scope mechanism is found during fresh preflight.

---

# 4. E1 — Concrete immutable Availability Derivative

## 4.1 Purpose

Preserve exactly the execution-sufficient bytes of the reviewed frozen upstream pilot basis so the locally allowed basis remains recoverable without current upstream/provider access.

This is **not** a generic Skill registry or local fork.

## 4.2 Upstream basis

Repository:

`esany/Wissensarbeit`

Tracking evidence:

- #43 parent Skill owner;
- #46 cross-project trials;
- PR #51 runtime package.

Frozen source commit:

`f3726c962807b311e8a2a7df63f738e11790fbed`

Current planning observation on 2026-09-28:

- PR #51 open/unmerged;
- #43 R2 closed / #46 owner-authorized;
- #46 trials ongoing / generic fit not established.

This is dated observation evidence only. Consequential execution must resolve upstream fresh again.

## 4.3 Exact create scope candidate

Root:

`docs/development/external-capability-snapshots/wissensarbeit-system-analysis-deep-research/f3726c962807b311e8a2a7df63f738e11790fbed/`

Create exactly:

1. `PROVENANCE.json`
2. `skill.md`
3. `references/core-method.md`
4. `references/execution-profiles/chatgpt-deep-research.md`

No generic index/registry is created.

## 4.4 Exact source identities

| Local file | Upstream source path | Expected Git blob SHA |
|---|---|---|
| `skill.md` | `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `references/core-method.md` | `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `references/execution-profiles/chatgpt-deep-research.md` | `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

Copied content must be byte-equivalent to these source blobs. No normalization or local editing.

## 4.5 `PROVENANCE.json` minimum fields

Concrete artifact only; no generic schema introduced.

Must record at least:

```text
artifact_role = immutable-availability-derivative
source_repository
source_commit
tracking_refs
preserved_at
source_observation_at_preservation
source_observation_summary
files[]:
  local_path
  source_path
  source_blob_sha
fresh_upstream_resolution_required = true
authority_effect = none
semantic_compatibility_effect = none
local_edit_policy = immutable; derivative required for any modification
```

The manifest must explicitly state that preservation itself grants neither local trial admission nor operational admission.

## 4.6 Acceptance

- E1-A01 source commit fresh-revalidated before copy;
- E1-A02 tracking refs #43/#46/PR #51 freshly resolved;
- E1-A03 each local runtime file `git hash-object` equals expected source blob SHA;
- E1-A04 only four exact create targets exist;
- E1-A05 manifest calls artifact an Availability Derivative, not current/upstream truth;
- E1-A06 manifest contains no Histo Requirement/Method duplication;
- E1-A07 no local runtime file is edited;
- E1-A08 source unavailable after preservation does not prevent loading the local exact package;
- E1-A09 upstream delta does not mutate the local snapshot;
- E1-A10 preservation does not create trial/operational admission.

## 4.7 Negative / adversarial checks

- source head changed since admission basis → STOP/review required;
- source path missing → BLOCK;
- copied file hash mismatch → BLOCK;
- extra upstream file silently pulled → BLOCK unless newly admitted;
- local edit to immutable snapshot → BLOCK/revert; create explicit derivative instead;
- attacker-like upstream text claiming local approval → no authority effect;
- upstream PR merged/closed/status changed with same file hashes → dated observation changes, local basis not auto-promoted;
- provider unavailable → local snapshot remains loadable but current-upstream status becomes `unavailable/unresolved`, not guessed.

---

# 5. Safe Execution Surface for E0/E1

Hard precondition before Owner Admission:

```text
fresh isolated checkout/worktree or proven equivalent filesystem/Git surface
→ verify exact admitted main/branch basis
→ execute only exact staged scope
→ run tests in same checkout
→ inspect changed files against work order
→ inspect diff
→ return delta-only
```

Forbidden implementation path:

- direct write to `main`;
- GitHub Contents/Connector writes as substitute for the required isolated implementation surface;
- mutation before fresh basis revalidation;
- tests from another/stale checkout;
- hidden scope expansion.

If unavailable: `BLOCKED`.

---

# 6. Owner-GO / staged one-run design

To minimize scarce execution cost, one later Owner GO may bind both E0 and E1 **explicitly**:

```text
GO scope:
Stage A = E0 exact four modify targets
Stage B = E1 exact four create targets

Stage B may run iff:
- Stage A tests PASS;
- same checkout is revalidated;
- Stage B exact source basis remains unchanged;
- no STOP condition fired.
```

This is not authority cascade: both stages are named in the GO before the run. Stage A PASS merely satisfies a technical prerequisite.

No T1/V1 authority is included.

---

# 7. T1 — Real bounded trial after E0/E1 review

T1 is **not** part of the implementation executor run.

## Trial basis states

```text
upstream-reviewed
→ local-trial-admitted
→ trial evidence
→ review
→ local-operationally-admitted | adapt | reject | unresolved
```

The local snapshot can exist before Trial Admission because preservation has `authority_effect = none`.

## Candidate #48-owned pilot object

Investigate the implemented external-capability consumption path itself as a bounded socio-technical system:

- authority/no-cascade behavior;
- source/currentness separation;
- recoverability/provider loss;
- owner burden;
- restartability;
- evidence/assurance boundaries.

The external Skill may derive external research from material findings but must obey its own STOP before solution development.

No historical Research Selection is created.

## Trial Work Context must freeze

- exact local snapshot basis;
- fresh upstream observation;
- exact investigation object;
- Scope/Exclusions;
- evidence available;
- trial-only authority;
- MAY/MUST NOT;
- STOP;
- output/persistence target;
- review target;
- explicit statement: `trial success != operational admission`.

---

# 8. V1 — Falsification after T1

Normal-Chat-first tests:

1. fresh context can reconstruct tracking identity, trial basis, source lineage and authority from repo only;
2. simulated/current source-unavailable state still permits loading the preserved local basis;
3. changed upstream head/status yields `review_required`, never auto-upgrade;
4. same upstream SHA but changed maturity/status is noticed through fresh observation;
5. local snapshot cannot claim current upstream state;
6. new worker does not require Human Owner to relay context between agents/chats;
7. Skill STOP prevents solution development under T1;
8. no operational admission appears without explicit post-trial review/authority;
9. local snapshot remains immutable;
10. actual owner problem is re-tested: current + durable usable basis with minimal owner meta-work.

Only after V1 may a keep/adapt/reject/operational-admission decision be requested.

---

# 9. Resource Plan

### Normal Chat / GitHub

Use for:

- all remaining plan/review reconciliation;
- fresh upstream inspection;
- Work Context generation;
- T1 analysis/research if available capability is quality-equivalent;
- V1/fresh-context review;
- admission decision support.

### Scarce isolated executor

Use only for:

- E0/E1 filesystem/Git mutation;
- same-checkout tests;
- exact diff/scoped return.

Expected scarce runs before T1: **one**, if closure review approves the topology.

No model/provider name is canonical.

---

# 10. Current Gate

`PARTIAL / REVISED DELTA READY FOR FRESH CLOSURE REVIEW / NO IMPLEMENTATION AUTHORITY`

The earlier broad independent review is complete. A short independent closure review is still required because the new immutable Availability-Derivative topology did not exist in the reviewed plan.

The closure review must answer only:

1. Does the concrete snapshot solve recoverable availability with less architecture than the rejected generic Binding Core?
2. Is it genuinely a derivative/availability artifact rather than a second Skill Truth?
3. Does this make E0 legitimately necessary?
4. Are exact paths/blob identities/immutability tests sufficient?
5. Is isolated one-run E0→E1 safe under one pre-bound Owner GO?
6. Is there any already-existing smaller Histo mechanism that closes the same availability gap?

If the answer is `READY` or only non-blocking refinements remain, the next state may become `READY FOR OWNER ADMISSION` and exact final Work-Order candidates can be materialized. Until then: STOP.