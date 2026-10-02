# Execution Packet – PR #149 bounded external-capability pilot / E1

**Stand:** 2026-09-28  
**Status:** `OWNER-ADMITTED / EXACT IMPLEMENTATION HANDOFF / ONE ISOLATED RUN / NO MERGE`  
**Technical Owner:** #48  
**Development / Verification:** #59  
**Parent plan:** `ai-orchestrated-skill-integration-execution-plan-20260927.md`  
**Owner GO:** recorded in PR #149 after closure-review reconciliation  

> Dieser Packet ist bewusst mechanisch. Der Executor soll **keine Discovery, Requirements-Arbeit, Architekturentscheidung, Scope-Erweiterung oder erneute Planungsrunde** durchführen.

---

## 1. Mission

Implementiere ausschließlich **E1**: eine exact, commit-scoped, provenance-erhaltende lokale Availability Derivative des frozen reviewed `system-analysis-deep-research` Runtime-Pakets aus `esany/Wissensarbeit`.

Danach Tests/Diff ausführen und STOP.

Kein T1/V1 im isolierten Executor.

---

## 2. Mandatory fresh bootstrap

Vor Mutation frisch lesen:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. #48
5. PR #149 inkl. aktuellem Head und neuestem `OWNER-ADMITTED PILOT`-Statuskommentar
6. `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`
7. `docs/architecture/assurance/ai-orchestrated-skill-integration-closure-review-findings-20260928.md`
8. `docs/development/ai-orchestrated-skill-integration-execution-plan-20260927.md`
9. dieses Execution Packet

Der im neuesten PR-Statuskommentar deklarierte **admitted planning head** ist die exakte Histo-Ausführungsbasis.

Wenn PR #149 inzwischen einen anderen Head besitzt und dieser nicht ausdrücklich als neuer admitted planning head ausgewiesen ist: `BLOCKED / STOP`.

---

## 3. Required execution surface

Pflicht:

```text
fresh isolated checkout/worktree or proven equivalent filesystem/Git surface
→ exact admitted PR-149 head
→ clean working tree
→ dedicated implementation branch
→ mutation/tests/diff in same checkout
```

Empfohlener Branchname:

`impl/ai-orchestrated-capability-pilot-20260928`

Forbidden:

- direct mutation of `main`;
- GitHub Contents-/Connector-Writes als Ersatz für die isolierte filesystem/Git-Surface;
- Mutation aus einem stale/dirty checkout;
- Hidden Scope Expansion.

Kann diese Surface nicht hergestellt werden: STOP ohne Mutation.

---

## 4. Fresh upstream preflight

Fresh resolve:

- `esany/Wissensarbeit` #43;
- #46;
- PR #51.

Admitted source basis:

`f3726c962807b311e8a2a7df63f738e11790fbed`

Erwarteter State bei Planung:

- PR #51 open/unmerged at exact head;
- #43 R2-closed / #46-owner-authorized;
- #46 trials ongoing;
- Generic Fit nicht etabliert.

### Source blob identities

| Source path | Expected Git blob SHA |
|---|---|
| `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

STOP if:

- exact source commit cannot be retrieved;
- any required source path is missing;
- retrieved bytes do not hash to the expected Git blob ID;
- upstream state creates a new material Authority/Safety ambiguity.

A status-only/maturity change does **not** silently alter the frozen source basis. Report it visibly; if it materially affects trial admissibility, STOP and return `unresolved` rather than interpreting it away.

---

## 5. Exact create scope

Create exactly these four previously absent files:

```text
docs/development/external-capability-snapshots/
  wissensarbeit-system-analysis-deep-research/
    f3726c962807b311e8a2a7df63f738e11790fbed/
      PROVENANCE.json
      skill.md
      references/core-method.md
      references/execution-profiles/chatgpt-deep-research.md
```

Preflight:

- every target must be absent;
- if any target exists: STOP and return the observed state; do not overwrite;
- no fifth file may be changed.

No modification of:

- execution-order code;
- Work-Order schema/contract;
- Requirements;
- Architecture contracts;
- CI configuration;
- existing Skill source.

---

## 6. Copy semantics

Copy the three Runtime files **byte-identically** from frozen upstream.

No:

- newline normalization;
- frontmatter injection;
- wording changes;
- local comments;
- path rewriting inside copied files;
- formatting cleanup.

Verification must use Git blob identity or byte-equivalent proof. Expected result:

```text
local skill.md
= git-blob:845f5cfa9d224384f7d81c79fd7829b8d26cbf06

local references/core-method.md
= git-blob:4a1aa371e0a7da30e7f98834cee58aa03ccc4821

local references/execution-profiles/chatgpt-deep-research.md
= git-blob:77fa8cfc31fdace2a928f3b936a21687d81de297
```

---

## 7. `PROVENANCE.json`

Create a concrete record; **no generic schema**.

Required semantic content:

```json
{
  "artifact_role": "immutable-availability-derivative",
  "source_repository": "esany/Wissensarbeit",
  "source_commit": "f3726c962807b311e8a2a7df63f738e11790fbed",
  "tracking_refs": ["#43", "#46", "PR #51"],
  "preserved_at": "<actual UTC timestamp>",
  "source_observation_at_preservation": "<actual UTC timestamp>",
  "source_observation_summary": "<factual fresh observation only>",
  "fresh_upstream_resolution_required": true,
  "authority_effect": "none",
  "semantic_compatibility_effect": "none",
  "local_edit_policy": "immutable; explicit new derivative required for modification",
  "package_fidelity": "exact reviewed PR #51 runtime package",
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

Do not add inferred claims such as `compatible`, `approved`, `current`, `stable`, `generic-fit` or `production-ready`.

If fresh state is ambiguous, record only factual observation and preserve ambiguity explicitly.

---

## 8. Verification

Run in the same checkout:

1. confirm only the four admitted paths are new/changed;
2. compute Git blob IDs of the three Runtime files;
3. compare all three against expected upstream IDs;
4. parse `PROVENANCE.json` as JSON;
5. verify it contains no authority/compatibility promotion;
6. run existing Project Assurance / relevant repository tests available in the checkout;
7. inspect final `git diff --check` and full diff;
8. confirm no existing file changed.

If the repository's standard full Project Assurance cannot execute because of an environment/dependency limitation, report the exact limitation. Do **not** fabricate PASS. Run every available substitutable check and return `unresolved` for the unavailable verification obligation.

---

## 9. Commit / remote persistence

After all available verification passes:

- commit only the four admitted files on the dedicated implementation branch;
- use a narrow commit message, e.g. `Add frozen external capability pilot basis`;
- if the execution environment has authorized GitHub push/PR capability, push the branch and open/update a **Draft PR** against the appropriate Histo base;
- do not merge;
- if remote persistence is unavailable, return exact commit SHA + full changed-file list + diff summary so the canonicalization gap is explicit.

Do not use direct-main writes as fallback.

---

## 10. Return contract

Return only a compact execution report:

```text
OUTCOME
- PASS | BLOCKED | PARTIAL

BASIS
- admitted Histo planning head
- execution branch / commit
- fresh upstream PR #51 head/state

CHANGES
- exact four paths or none

VERIFICATION
- three local Git blob IDs
- JSON parse
- tests / Project Assurance
- diff check

UNRESOLVED
- only actual unresolved items; do not fill with interpretation

STOP CONFIRMATION
- no E0
- no T1/V1 executed
- no Requirement/Method/Architecture/Generic-Fit/Operational-Admission
- no merge
```

Do not return a new architecture proposal or next-work plan.

---

## 11. After executor return

The normal Histo Chat will:

1. fresh-read the returned implementation state;
2. review the exact delta;
3. if E1 PASS, continue T1/V1 under the already-recorded Owner GO;
4. otherwise preserve `blocked` / `partial` / `unresolved` transparently and STOP.

No additional Human Owner routing is required unless a genuinely new Authority/Safety/Scope decision appears.
