# Fresh Closure Review – PR #149 revised external-capability plan

**Status:** `review-task / read-only / no implementation authority`  
**Target branch:** `plan/ai-orchestrated-skill-readiness-20260927`  
**Primary owner:** #48  

## Purpose

Perform one short fresh-context adversarial closure review of the **revised delta only** after the broader independent review of PR #149.

Do not repeat the whole original audit unless a newly discovered dependency requires it.

## Fresh bootstrap

Read current:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. #48
5. PR #149 and current head
6. `docs/architecture/assurance/ai-orchestrated-skill-integration-readiness-20260927.md`
7. `docs/architecture/assurance/ai-orchestrated-skill-integration-independent-review-findings-20260928.md`
8. `docs/development/ai-orchestrated-skill-integration-execution-plan-20260927.md`
9. `docs/architecture/assurance/ai-orchestrated-skill-integration-author-self-review-20260927.md`
10. controlling #57/#61/bounded-work-order/mutation contracts only where needed.

Freshly revalidate the upstream pilot identity/status:

- `esany/Wissensarbeit` #43
- #46
- PR #51
- exact reviewed head `f3726c962807b311e8a2a7df63f738e11790fbed`

## Revised hypothesis to falsify

The earlier generic Binding Core has been removed.

The revised minimum is:

```text
existing Histo Work Context / Work Order
+ fresh upstream resolution
+ explicit local trial admission
+ immutable local Availability Derivative of exact frozen execution-sufficient Skill bytes
+ no auto-compatibility / no current-upstream store
+ isolated implementation surface
```

The Availability Derivative contains only:

- `PROVENANCE.json`
- `skill.md`
- `references/core-method.md`
- `references/execution-profiles/chatgpt-deep-research.md`

under the exact frozen source commit.

P0 create-target support remains only because those legitimate new files must be declared exactly and the current execution-order validator requires every target file to pre-exist.

## Review questions

Try to falsify the revised plan on these points:

1. **Problem closure:** Does the revised design actually close `current + durable usable basis`, or is durable availability still being renamed/overclaimed?
2. **Minimality:** Can any already-existing Histo mechanism preserve execution-sufficient bytes/recoverability with less structure than the proposed immutable snapshot?
3. **Second truth risk:** Does the snapshot remain an immutable Availability Derivative, or does it accidentally become a fork/second Skill Truth?
4. **Authority:** Are `upstream reviewed`, `local trial admitted`, and `local operationally admitted` genuinely non-circular and non-cascading?
5. **Currentness:** Is current upstream always fresh-resolved rather than reconstructed from dated observation/provenance metadata?
6. **P0 necessity:** Given the revised E1 exact create targets, is P0 now genuinely necessary? If a smaller safe exact-create mechanism already exists, identify it.
7. **P0 scope:** Does create-target support stay a small bounded contract delta instead of becoming a generic file-operation DSL?
8. **Snapshot topology:** Are four files exactly sufficient and necessary? Is any file missing or redundant?
9. **Integrity:** Are upstream commit + per-file Git blob SHA + byte-equivalence checks sufficient for the claimed provenance/integrity level?
10. **Safe write surface:** Is isolated checkout/worktree + exact basis + same-checkout tests + changed-file check + diff review sufficient to prevent the known direct-write hazard?
11. **One-run economy:** Can E0 and E1 safely be executed in one scarce run when both stages are explicitly pre-bound by one Owner GO and E1 starts only after E0 PASS/revalidation?
12. **Trial boundary:** Can T1 use the preserved basis under explicit trial admission without claiming operational/general compatibility?
13. **Resource efficiency:** Is any scarce executor work still present that normal Chat can perform equivalently?
14. **Architecture creep:** Does the revised plan introduce any hidden registry, workflow, agent, compatibility, vendoring or policy platform?
15. **Restartability:** Can a fresh competent context reconstruct source identity, local preserved basis, trial authority, current-upstream check and STOP without old chat state?

## Finding format

For each material finding:

```text
ID
Severity: blocking | major | minor | observation
Finding
Exact repo evidence
Why it matters
Disposition recommendation: keep | refine | remove | split | unresolved
Blocks READY FOR OWNER ADMISSION: yes | no
```

## Verdict

Return exactly one:

- `READY`
- `READY WITH NON-BLOCKING REFINEMENTS`
- `PARTIAL`
- `UNRESOLVED`
- `BLOCKED`

If `READY WITH NON-BLOCKING REFINEMENTS`, separate them clearly from anything required before Owner Admission.

## Authority

Read/review only.

Do not:

- modify repository state;
- implement E0/E1;
- create Work Orders;
- merge PR #149;
- promote Requirements/Method/Architecture;
- perform Research Selection;
- infer Owner GO.

The result is review evidence only. A separate Histo-Orla reconciliation may persist/disposition it.