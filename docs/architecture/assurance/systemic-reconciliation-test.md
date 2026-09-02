# Histo-Orla – Systemic Reconciliation Test

**Status:** `architecture/assurance candidate / repeated real-use failure demonstrated / no mechanism decision yet`  
**Owner:** #48 Technical Lead; assurance interface #63; delivery interface #59  
**Prior art:** current `esany/Wissensarbeit` systemic-integration/reconciliation finding  
**Requirements:** REQ-TRACE-001, REQ-WF-001, REQ-LEAN-001, REQ-UX-001/002; governance `AGENTS.md`  
**Evidence boundary:** test of repository/project-state coherence, not historical/scientific evidence

## 1. Question

Does Histo-Orla reliably prevent a locally correct material change from leaving semantically affected existing project state stale?

This is deliberately different from asking whether a changed file, local research slice or validator is internally correct.

Test pattern:

```text
material delta
→ identify existing objects/statements whose meaning may be affected
→ disposition each relevant impact
→ reconcile canonical/derived current state
→ only then treat the change as systemically integrated
```

Candidate dispositions for the test are descriptive review vocabulary, not a new accepted lifecycle:

`unchanged | confirmed | refined | partially-satisfied | superseded | stale | conflict | needs-decision`

## 2. Prior-art trigger

The current `esany/Wissensarbeit` review found a recurring failure pattern across several PRs: direct contracts and tests were updated locally, while roadmap/current-state/audit statements whose meaning changed were not always re-evaluated. Its existing concepts already provide most ingredients: systemic integration, trace, audit, derived views and Git delta. The missing part is reliable chaining and a sufficiently strong integration gate.

Histo-Orla uses this only as prior-art challenge input. The following findings are independently reproduced against current Histo-Orla state.

## 3. Histo-Orla evidence

### T1 – Operational Core vs. Requirements Delivery Coverage

Current `PROJECT_STATE.md` records the Operational Core increment as implemented and verified: Requirement→Enforcement map, shared core, 14 Requirements tests, 16 Trace tests and 5 Operational tests.

Before this test, `docs/development/requirements-coverage.md` still classified `REQ-WF-001 – Formal prüfbare Invarianten werden deterministisch erzwungen` as `not-started` and did not list #62/#63 among its active delivery packages.

Disposition:

- `REQ-WF-001` delivery view → **stale**, corrected during this test to `partial`;
- implemented Requirements-/Trace-/Enforcement-map guards → **confirmed**;
- Research-State Promotion/Transition guards under #54 → **still open**.

This is a direct example of a locally valid implementation not being reconciled into the global delivery view.

### T2 – Architecture index vs. later consolidated assurance state

`docs/architecture/README.md` still describes an older Assurance test count/state (15 Project-Assurance tests and older intermediate CI wording), while `PROJECT_STATE.md` records the later consolidated verified state with 16 Trace and 5 Enforcement-Map tests.

Disposition:

- Architecture index assurance-status paragraph → **stale / needs reconciliation**;
- current canonical operational result in `PROJECT_STATE.md` + implementation trace → **confirmed**.

This test does not rewrite the whole index because the important finding is the missing reconciliation mechanism itself; the stale paragraph remains a fixture until deliberately reconciled under #48/#59.

### T3 – Real Lampe pilots vs. Human-readable Audit work state

The two real #46/#61 source pilots produced increasingly careful research state and, in pilot 2, a manually written German user-oriented explanation. Owner feedback then identified that the actual research workplace remained dominated by manually maintained Markdown text walls and chat orchestration.

At that point #55 still had status `planned / P1 / architecture-prototype` and explicitly allowed starting against synthetic state. The real pilot had materially changed the evidence for priority and the appropriate fixture, but that consequence had not been automatically/systematically fed back into #55/#59 delivery state.

Disposition:

- #55 requirement itself → **confirmed**;
- synthetic-first assumption → **refined by real-case availability**;
- delivery priority → **needs re-evaluation from real owner pain**, not a new Requirement;
- manual German explanation embedded in research Markdown → **useful prototype evidence, not fulfilment of REQ-UX-001/002/003**.

`FB-20260902-003` now persists the owner/workflow pain and `requirements-coverage.md` points #55 at the real #46 state.

### T4 – Capability-first governance change

`AGENTS.md` gained the binding rule `Capability-first Tooling und Handoff` after a real routing failure: the current ChatGPT context already had PDF and GitHub capabilities, but a Work handoff was initiated anyway.

The local governance change was correct, but its initial work cycle did not produce an explicit impact/disposition set for #48 technical-selection logic, #61 Work Context/Handoff, #63 feedback or the current-state view. Those relationships were only revisited later after further owner criticism.

Disposition:

- capability-first rule → **confirmed**;
- initial integration process → **incomplete systemic reconciliation**;
- #48/#61/#63 implications → **must be considered when the mechanism is operationalized**, without duplicating the governance rule into multiple truth stores.

## 4. Result

The same structural failure is reproduced in Histo-Orla:

> **Histo-Orla currently does not reliably prevent locally correct material changes from leaving semantically affected global project state stale.**

The pattern is visible across research, architecture, delivery coverage and governance changes. Existing update rules mostly enumerate direct artifacts to maintain; they do not reliably perform semantic impact discovery across already-existing statements, open work, derived views and priorities.

This matters because stale global state can cause later work to compensate for an obsolete picture, producing additional local structures instead of refining the existing system.

## 5. What is already available

No new framework is justified by this finding. Histo-Orla already has most semantic/technical ingredients:

- `REQ-TRACE-001` and #63 for Goal/Need/Pain → Decision/Delivery/Feedback trace;
- `REQ-WF-001` for deterministic enforcement where rules are formalizable;
- #48 systemic integration / prior-art challenge questions;
- #62/#63 validators and the shared Operational Core;
- #55 derived human-readable views;
- #61 generated Work Context/Handoff direction;
- Git diff/history as concrete change evidence;
- `fuse | refine | reframe | supersede | conflict | reject | defer` as already accepted review vocabulary from prior art, not a new lifecycle.

The gap is primarily **composition/chaining**: impact discovery and explicit reconciliation are not yet a reliable step before a material change is treated as globally integrated.

## 6. Candidate mechanism to test next

Do not build a workflow engine. Test the smallest composition that can fail on the real fixtures above.

```text
material change / candidate promotion
→ IMPACT DISCOVERY
   identify potentially affected Requirements, Decisions, Work Owners,
   current-state statements, open feedback/debt, derived views and tests
→ RECONCILIATION
   disposition relevant impacts explicitly
→ DIRECT FIXES / DERIVED REBUILD
→ PROMOTION / MERGE CONFIDENCE
   material state is not called globally current while required reconciliation is open
```

Important boundaries:

- no requirement that every changed object causes edits everywhere;
- `unchanged` with a reason is valid;
- semantic impact discovery may require AI/judgement, while reference integrity and required disposition presence may be deterministic;
- historical/scientific truth is never decided by this mechanism;
- frequency/boundary is unresolved: commit vs. PR vs. merge vs. selected material transitions must be tested, not assumed;
- a derived view should be rebuilt rather than manually updated when derivation is reliable;
- historical records may remain historical, but they need enough temporal/version context not to masquerade as current state.

## 7. Candidate acceptance test

Use at least the four real fixtures above.

A candidate mechanism succeeds only if, from each material delta, it surfaces the already-observed affected state without relying on chat memory:

1. Operational Core delta finds `REQ-WF-001` delivery coverage and architecture status as affected;
2. Lampe pilot/owner feedback finds #55/#59/UX delivery state as affected without treating the manual German paragraph as implementation;
3. capability-first governance change finds #48/#61/#63 integration implications;
4. unaffected objects can be explicitly dispositioned `unchanged` without forced edits.

False-positive burden and human micromanagement are part of acceptance. A mechanism that merely asks the owner to review dozens of files fails the `Human-in-the-loop, not human-as-workflow-engine` objective.

## 8. Open decisions

Not decided here:

- exact materiality threshold;
- whether impact discovery runs at PR, merge, canonical promotion or another boundary;
- which candidate impacts are deterministic/reference-derived vs. AI-assisted judgement;
- whether the existing Operational Core gets a new `integrate/reconcile` capability or #63 absorbs it;
- schema/record format;
- UI.

#48/#63 should first run the smallest real-fixture spike and compare it with current `Wissensarbeit` implementation before any new technical component is admitted.

## 9. Handoff

Established:

- repeated systemic-reconciliation failure reproduced in Histo-Orla;
- one clear stale delivery status corrected (`REQ-WF-001: not-started → partial`);
- additional stale/current-state mismatches identified as fixtures;
- owner workflow pain already persisted as `FB-20260902-003`.

Next action:

> Under #48/#63, prototype or simulate impact-discovery + reconciliation on the four real fixtures, using existing Operational Core/trace machinery first. Do not add a framework. Evaluate accuracy, false-positive burden, human workload and whether the gate would have prevented the observed stale states.
