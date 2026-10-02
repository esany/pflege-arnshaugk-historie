# Histo-Orla – AI-orchestrierte externe Capability-Integration: Execution Plan

**Stand:** 2026-09-28  
**Status:** `OWNER-ADMITTED BOUNDED TECHNICAL PILOT / E1 IMPLEMENTATION PENDING`  
**Parent:** `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`  
**Closure evidence:** `docs/architecture/assurance/ai-orchestrated-skill-integration-closure-review-findings-20260928.md`  
**Technical Owner:** #48  
**Development / Verification:** #59  
**Work Context:** #61

> Dieser Plan ersetzt den früheren `E0 → E1 → T1 → V1`-Graph. E0/P0 ist vollständig aus dem Critical Path entfernt. Der Pilot baut keine generische Create-Target-Infrastruktur.

---

## 1. Final delivery graph

```text
OWNER GO (recorded 2026-09-28)
        ↓
E1 exact Availability Derivative
        ↓ verify + diff + STOP
NORMAL-CHAT DELTA REVIEW
        ↓ if E1 PASS
T1 real bounded capability use
        ↓
V1 restart / delta / unavailability / owner-burden falsification
        ↓
keep | adapt | reject | unresolved
        ↓
STOP before any Operational Admission / Generic Fit / Merge / further implementation
```

Kein weiterer unabhängiger Planreview ist vorgesehen, solange kein neuer materieller irreversibler/Authority-/Safety-Risikotyp entsteht.

---

## 2. Explicit removals

Nicht mehr Teil dieses Piloten:

- `E0/P0 create-target support`;
- Änderung von `docs/development/work-orders/codex-rebuild-execution-contract.md`;
- Änderung des Work-Order JSON Schemas;
- Änderung von `tools/operational/execution_order.py`;
- Änderung von `tools/operational/tests/test_execution_order.py`;
- generische External-Skill Registry;
- Binding Schema;
- Compatibility Evaluator;
- persistent pseudo-current Upstream Store;
- Product Skill Manager / Workflow Engine / Multi-Agent Runtime.

Grund: Für den one-off exact create slice reicht die bestehende Histo Authority-/Work-Context-Schicht zusammen mit einer isolierten Git-/Filesystem-Ausführung. Die Einschränkung eines optionalen Validators ist keine Projektinvariante.

---

## 3. E1 – exact local Availability Derivative

### 3.1 Purpose

Erhalte die exact reviewed Runtime-Package-Bytes des frozen Upstream-Piloten lokal, sodass der verwendete Skill-Basisstand auch bei später nicht erreichbarem Upstream als **recoverable Skill/source-package basis** verfügbar bleibt.

E1 behauptet nicht:

- AI-/Research-Provider Availability;
- Current Upstream;
- semantic compatibility;
- Trial Admission;
- Operational Admission;
- Generic Fit.

### 3.2 Frozen source basis

Repository: `esany/Wissensarbeit`  
Tracking refs: #43, #46, PR #51  
Frozen source commit: `f3726c962807b311e8a2a7df63f738e11790fbed`

Fresh revalidation 2026-09-28:

- PR #51 `open / unmerged` at exact frozen head;
- #43 `R2-closed / #46-owner-authorized`;
- #46 trials ongoing; Generic Fit not established.

### 3.3 Exact create scope

Create exactly:

```text
docs/development/external-capability-snapshots/
  wissensarbeit-system-analysis-deep-research/
    f3726c962807b311e8a2a7df63f738e11790fbed/
      PROVENANCE.json
      skill.md
      references/core-method.md
      references/execution-profiles/chatgpt-deep-research.md
```

All four targets must be absent immediately before creation. If any exists: STOP and revalidate; do not overwrite.

### 3.4 Exact source identities

| Local runtime file | Upstream source path | Expected Git blob SHA |
|---|---|---|
| `skill.md` | `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `references/core-method.md` | `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `references/execution-profiles/chatgpt-deep-research.md` | `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

Runtime content must be byte-equivalent to the frozen source blobs. No normalization or local editing.

### 3.5 `PROVENANCE.json`

Concrete pilot record only; no generic schema is introduced.

Minimum content:

```json
{
  "artifact_role": "immutable-availability-derivative",
  "source_repository": "esany/Wissensarbeit",
  "source_commit": "f3726c962807b311e8a2a7df63f738e11790fbed",
  "tracking_refs": ["#43", "#46", "PR #51"],
  "preserved_at": "<UTC timestamp>",
  "source_observation_at_preservation": "<UTC timestamp>",
  "source_observation_summary": "PR #51 open/unmerged at frozen head; #46 trials ongoing; generic fit not established",
  "fresh_upstream_resolution_required": true,
  "authority_effect": "none",
  "semantic_compatibility_effect": "none",
  "local_edit_policy": "immutable; explicit new derivative required for modification",
  "files": [
    {
      "local_path": "skill.md",
      "source_path": "skills/system-analysis-deep-research/skill.md",
      "source_blob_sha": "845f5cfa9d224384f7d81c79fd7829b8d26cbf06"
    },
    {
      "local_path": "references/core-method.md",
      "source_path": "skills/system-analysis-deep-research/references/core-method.md",
      "source_blob_sha": "4a1aa371e0a7da30e7f98834cee58aa03ccc4821"
    },
    {
      "local_path": "references/execution-profiles/chatgpt-deep-research.md",
      "source_path": "skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md",
      "source_blob_sha": "77fa8cfc31fdace2a928f3b936a21687d81de297"
    }
  ]
}
```

The concrete preserved timestamp is execution evidence, not a freshness claim.

---

## 4. E1 safe execution contract

E1 runs only on:

```text
fresh isolated checkout/worktree or proven equivalent filesystem/Git surface
→ exact admitted PR-149 planning basis revalidation
→ dedicated implementation branch
→ fresh upstream revalidation
→ exact four-target absence check
→ exact source-byte acquisition
→ local file creation
→ local git-blob verification
→ exact changed-file-set check
→ relevant same-checkout tests / Project Assurance
→ diff review
→ STOP + delta-only return
```

### Forbidden

- direct write to `main`;
- GitHub Contents/Connector writes as substitute for isolated implementation;
- overwrite of pre-existing target;
- any fifth changed implementation file without STOP/re-admission;
- editing copied runtime bytes;
- changes to execution-order/schema/contracts;
- Merge;
- T1 before E1 PASS + delta review.

### E1 acceptance

- `E1-A01` admitted PR-149 basis is exact and fresh;
- `E1-A02` upstream #43/#46/PR #51 fresh-resolved before copy;
- `E1-A03` frozen commit remains exact `f3726c...`;
- `E1-A04` four target paths absent before creation;
- `E1-A05` three local runtime Git blobs equal expected upstream blobs;
- `E1-A06` no extra file changed;
- `E1-A07` provenance contains no Histo Requirement/Method duplication;
- `E1-A08` provenance grants no authority or compatibility;
- `E1-A09` local package remains loadable if upstream becomes unavailable;
- `E1-A10` Project Assurance / relevant existing tests remain green.

### E1 negative cases

STOP / BLOCK on:

- upstream head/ref mismatch affecting admitted basis;
- source path unavailable before preservation;
- source hash mismatch;
- target already exists;
- unexpected extra diff;
- local content normalization/change;
- unavailable isolated execution surface.

---

## 5. T1 – real bounded capability trial

T1 is already bound by the 2026-09-28 Owner GO but starts only after E1 PASS + delta review.

### Trial purpose

Test the technical integration path, not a historical research question and not a new architecture exercise.

A fresh normal-Chat context must, from repository state alone:

1. identify the exact preserved capability basis;
2. fresh-resolve upstream currentness;
3. reconstruct Histo Trial Authority, Scope and STOP;
4. load `skill.md` and mandatory `core-method.md` itself;
5. use the capability on a bounded #48-owned technical/system-analysis object;
6. preserve evidence/source/capability limits and `unresolved`;
7. stop before solution development as the Skill requires;
8. return reviewable output without Human Owner relaying Skill text, prompt history or context between chats.

### Trial authority

```text
upstream reviewed evidence
≠ local trial authority
≠ local operational admission
```

T1 has local **trial-only** authority for this bounded integration test.

T1 must not create:

- target architecture;
- implementation plan;
- Requirement/Method Truth;
- Generic Fit;
- Operational Admission;
- Research Selection;
- Merge authority.

### Unsicherheit

T1 must not fill evidence gaps with plausible interpretation. Missing/ambiguous evidence remains explicit and can produce bounded completion or `unresolved`.

---

## 6. V1 – falsification after T1

Normal-Chat-first.

Check at least:

1. fresh context reconstructs capability basis / lineage / authority / STOP from repo only;
2. three local runtime files are bound as prerequisite Git-blob bases; local drift becomes `unresolved / revalidation required`;
3. upstream head/status delta becomes visible and never auto-upgrades local basis;
4. upstream unavailability still permits loading the preserved exact package while current-upstream status remains unavailable/unresolved;
5. local derivative cannot claim Current Upstream or Compatibility;
6. Skill STOP prevents solution development;
7. trial success does not produce Operational Admission;
8. open questions remain explicit rather than interpretation-filled;
9. Human Owner did not have to route Skill/context/version among multiple workers;
10. the increment yields a real new technical capability rather than only a stored artifact.

Final pilot disposition:

`keep | adapt | reject | unresolved`.

No automatic next implementation follows.

---

## 7. Resource plan

### Current Chat / normal Chat

Use for:

- fresh repo/upstream checks;
- T1 execution if current capability is adequate;
- V1 review/falsification;
- interpretation of results;
- persistence of bounded evidence where already authorized.

### Isolated executor

Use only for E1 because the current normal Chat environment cannot establish a networked isolated Git checkout/push surface. The executor receives no discovery or architecture task.

Expected scarce execution before T1: **one exact E1 run**.

---

## 8. Current next action

Execute the exact packet:

`docs/development/ai-orchestrated-capability-pilot-execution-packet-20260928.md`

After E1 returns:

```text
review exact delta here
→ if PASS continue T1/V1 under already-bound Owner GO
→ otherwise expose blocker/unresolved and STOP
```
