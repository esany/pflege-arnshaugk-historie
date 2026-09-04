# Histo-Orla – Current Work Selection / Reconciliation 2026-09-04

**Status:** `work-control-reconciliation / minimal-selection-disposition / no-workflow-engine`  
**Work Owner:** #64 review input; technical consumers #48/#61/#63; research owners #46/#47/#60  
**Scope:** current work-control and selection semantics only. No new Fachforschung, no PR #76 promotion, no architecture decision, no universal lifecycle.

## 1. Fresh current-state audit

Fresh bootstrap read for this pass:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `README.md`
- #42, #44, #46, #47, #48, #51/#52/#53, #59, #60, #61, #62, #63, #64 as current Work Owner surface
- `docs/research/source-identity-protocol.md`
- `docs/research/synthesis/phase-reconciliation.md`
- `docs/architecture/contracts/canonical-research-state.md`
- `docs/architecture/assurance/method-conformance-work-context.md`
- `docs/architecture/assurance/systemic-reconciliation-test.md`
- `docs/architecture/assurance/value-decision-delivery-assurance.md`
- `docs/architecture/operational-execution-architecture.md`
- `docs/development/requirements-coverage.md`
- `tools/operational/context.py`
- `tools/operational/context_spec.py`
- `tools/operational/tests/test_context.py`
- `tools/operational/tests/test_context_spec.py`
- PR #76 and current `main` vs. `research/sachenbacher-clean-room-20260903` comparison

Current canonical state already says:

- `PROJECT_STATE.md` is a navigation/handoff view, not full truth.
- Accepted Requirements remain #42-owned; #62/#63 only check formalized conformance/traceability.
- #46/#47 are real live-research owners.
- #60 owns Method Truth, not historical Findings or current work selection.
- #48/#59/#61 may implement/harden context and assurance, but cannot invent Fachauthority or priority.
- The systemic reconciliation failure is already reproduced: locally correct material deltas can leave global current-state/delivery/handoff statements stale.

Current mismatch found in this pass:

- `PROJECT_STATE.md` still foregrounds Lampe 420 as an active bounded cursor. That is valid as a resumable Work Order, but it is not proof of `selected-current` without explicit selection authority.
- PR #76 is fachlich relevant and open, but it is not integrated and not selected-current by virtue of being open, mergeable or green-tested.
- #47 is an active independent research owner, but active ownership is not current selection.
- #60 is active cross-cutting method work, but supporting/method truth is not a historical current slice.
- No existing repo structure cleanly represents the four separate questions below as a current work-control view.

```text
What exists?
What is valid / resumable?
What is integrated?
What is currently and explicitly authorized for work?
```

## 2. Minimal vocabulary boundary

The following words are used here only as **dispositions of real Work Objects**. They are not a new universal lifecycle and not a workflow state machine.

```text
selected-current
resumable
branch-candidate
supporting
review-input
blocked
selection-open
```

Hard invariant:

```text
valid/resumable
≠ integrated
≠ selected-current
≠ technically evidence-capable
```

A fresh worker must not infer `selected-current` from any of these alone:

```text
resumable
open PR
active Work Owner
newest commit
valid Work Order
green CI
existing cursor
technical executability
```

`selected-current` may only represent an explicit authorized selection. If no such authority is present, `selection-open` is the correct state and must be preserved.

## 3. Work-control disposition

| Work Object | Exists | Validity / resumability | Integration | Selection | Authority | Disposition | Next action |
|---|---|---|---|---|---|---|---|
| #46 / Sachenbacher model-check / PR #76 | yes, on branch `research/sachenbacher-clean-room-20260903` | fachlich relevant evidence-bearing secondary-publication/model-check; not final synthesis | not integrated; PR #76 open; branch diverged from current `main` | not selected-current | #46 owns historical research; #60 owns method learning; PR merge authority requires #48/#63/#64 reconciliation | `branch-candidate` | Disposition final intended branch state before any merge/rebuild. |
| #46 / Lampe 420 / `WO-U2-LAMPE-420-001` | yes, on `main` | valid/resumable bounded Work Order; D2 can resume it with unresolved prerequisites visible | integrated as Work Order and technical D2 acceptance fixture | not selected-current unless explicitly re-authorized | #46 owns research scope; #61/#48 own D2 consumer mechanics | `resumable` | Keep as resumable; do not use it to infer project priority. |
| #47 Teich-/Wasserlandschaft | yes | active independent research owner with its own source logic | integrated as issue/research case | not selected-current by default | #47 owns U1 research scope/status; #45/source protocol controls source identity | `resumable` / active owner, not current selection | Preserve as parallel work owner; no selection by inference. |
| #60 Domain Method Work | yes | active cross-cutting Method Truth work | integrated as method owner/work package | not a historical current slice | #60 owns Fachmethodik; #42 receives accepted Requirement deltas | `supporting` | Continue when method work is the explicitly selected technical/method task or required by a real slice. |
| #64 structural audit/review | yes | active review input | integrated as issue/commentary/audit owner | not selected-current historical research | #64 has review-input authority only; material deltas must route to #42/#48/#59/#60/etc. | `review-input` | Use as reconciliation driver, not direct requirement/architecture truth. |
| Systemic Reconciliation Test | yes | architecture/assurance candidate with reproduced failure fixtures | integrated architecture assurance artifact | not selected-current work by itself | #48/#63/#59 | `supporting` | Reuse as mechanism boundary; do not build workflow engine. |
| Document-Evidence / Sachenbacher PDF pain | yes as observed technical capability pain, not yet a selected implementation stack | valid technical research input | not implemented; no architecture decision | not selected-current historical research | #48/#51/#52/#53/#57 plus #50 source/instance contract; domain owners validate scholarly relevance | `supporting` technical spike candidate | Treat as separate goldtest/spike only if explicitly selected; no PR #76 promotion. |
| Overall current selection | selection question exists | multiple valid candidates exist | no explicit authoritative selection found in current canonical state | no selected-current identified | Research/Product Owner selection needed; #48/#61 can represent/propagate only | `selection-open` | Preserve selection-open until an explicit owner-authorized choice is recorded. |

## 4. Minimal solution cut

Existing structures are close but insufficient:

- `PROJECT_STATE.md` is intentionally a small derived/handoff view and should not become a full state matrix.
- #46/#47/#60 Issues own their own scopes, but they do not globally select the next project work.
- `tools/operational/context.py` can preserve/redirect a supplied cursor, but it depends on caller-resolved priority authority and currently lacks an explicit upstream selection-disposition view.
- `systemic-reconciliation-test.md` describes the broader failure but not the current Work Object selection table.

Therefore this file is the smallest repo-specific structure for the current gap:

```text
versioned minimal selection/disposition view
→ no new schema
→ no new lifecycle
→ no workflow engine
→ no fachliche selection by Agent
→ future D2/derived-view consumers may read this or its later machine-readable projection if that becomes necessary
```

A later machine-readable projection is allowed only after this table is stable across real cases and has an accepted consumer. Until then, this remains a controlled reconciliation artifact, not a platform.

## 5. D2 / context consumer check

Current D2 state:

- `tools/operational/context.py` derives a transient `CurrentContext` from facts supplied by adapters/callers.
- It stores no task truth and explicitly does not infer scholarly meaning.
- `assess_cursor_request()` redirects cursor drift unless `priority_authorized=True` is supplied by the caller.
- `tools/operational/context_spec.py` loads a JSON Work Order and validates declared Git-blob prerequisite bases; stale pass becomes `unresolved`.
- The real Lampe 420 Work Order proves resumability, prerequisite revalidation and `unresolved` preservation.

Consumer risk:

- D2 uses the term `current canonical cursor`. Without an explicit upstream selection/disposition layer, a valid resumable Work Order can be operationally conserved too strongly.
- A caller could treat the Lampe Work Order as global `selected-current` because it is a valid D2 fixture and appears in `PROJECT_STATE.md` next actions.
- D2 cannot currently represent `selection-open` as a first-class upstream fact. It can only refuse unauthorized cursor switches once a context has already been supplied.

Required invariant for D2 consumers:

```text
D2 may continue/redirect only against caller-supplied selection authority.
D2 must not derive selected-current from work_order_ref, open PR, latest commit, green CI or successful prerequisite validation.
If upstream state says selection-open, D2 must preserve that uncertainty and must not choose among resumable candidates.
```

Minimum future technical test candidate, not implemented here:

```text
Given:
- a valid/resumable Work Order
- an open PR
- an active Work Owner
- no explicit selected-current authority

Then:
- generated/derived context may report resumability
- it must not mark any candidate selected-current
- cursor request must return unresolved/redirect rather than silently continue as project priority
```

No D2 code change is required in this PR because the missing fact is upstream selection semantics, not a proven bug in the existing `priority_authorized` parameter. A code/test change becomes justified when a machine-readable selection projection or context composer consumes this disposition.

## 6. Root / handoff impact

`PROJECT_STATE.md` and README should remain short derived/handoff views. The next root/handoff rebuild should say, in condensed form:

```text
Current Work Selection: selection-open.
Valid/resumable work exists, especially #46/Lampe 420, #47 U1 and #60 method work.
PR #76 is a branch-candidate requiring final-intended-state reconciliation, not selected-current.
No new Fachforschung starts until the selected-current decision or selection-open status is explicit for the next work cycle.
```

Do not copy this full table into `PROJECT_STATE.md`. Link or derive from this artifact once merged.

## 7. PR #76 reconciliation plan, separate from work selection

PR #76 must not be handled as `rebase → CI → merge`.

Current facts:

- PR #76 is open and not merged.
- Base recorded in the PR is older than current `main`.
- Current comparison is `diverged`: 19 commits ahead, 31 behind.
- It adds five Sachenbacher-related research/method/source-ledger files.
- The PR itself states: Sachenbacher is a secondary publication/model/source-router, not truth authority; direct collation debts remain; `Knauwe villa` remains unresolved.

Required final-intended-state disposition per PR content unit:

| Unit | Initial disposition | Required check before merge/rebuild |
|---|---|---|
| `orlagau-source-ledger-sachenbacher-2022-delta.md` | `refine` | Fold into or link from main source ledger without duplicating Source Truth; mark direct-collation debt. |
| `u2-sachenbacher-2022-clean-room-slice.md` | `supersede/refine` | Earlier Ranis-focused slice is partly superseded by later model-check orientation; retain only if historically useful with clear temporal status. |
| `u2-sachenbacher-2022-landesausbau-model-check.md` | `retain/refine` | Keep model-check as branch candidate, but reconcile language against #63 NOT-PASS and #64 research-first/pilot critique. |
| `u2-sachenbacher-2022-makro-meso-mikro-model-check-delta-20260903.md` | `retain/refine` | Preserve wider Search Space and non-Masterraum correction; ensure not promoted as final synthesis. |
| `sachenbacher-clean-room-method-learning-20260903.md` | `refine/defer` | Keep as #60 method-learning candidate only; no validated-method claim. |
| PR-level merge readiness | `defer` | Reconcile against current `main`, #46 comments, #60 method ownership, #63 NOT-PASS, #64 audit and source-identity concerns before merge. |
| Current-work selection implication | `unaffected` | Even if reconciled and mergeable, PR #76 does not become `selected-current` automatically. |

## 8. Document-Evidence spike boundary

The Sachenbacher document-evidence pain is real but separate.

It may become a technical goldtest under #48/#51/#52/#53/#57 if explicitly selected. It is not:

- historical Work Selection;
- PR #76 promotion;
- an Architecture Decision;
- Requirement Promotion.

Technical Evidence Plane for any later spike:

```text
Source / Publication
→ Instance
→ Page
→ Region
→ Derivative / Extraction
→ Observation
→ Interpretation
→ Synthesis
```

Initial tool candidates remain unordered candidates only:

```text
avoid
→ reuse
→ configure
→ integrate
→ thin custom layer
→ custom build
```

Goldtest pages should cover normal text, long footnotes, complex reading order, map+legend, map labels/symbols, table, figure+caption+text reference, image-heavy page, problematic scan/text layer, and PDF-page vs print-page mapping.

Parser accuracy alone is not success. Success requires region round-trip, visible loss/heuristics/uncertainty and reproducibility by a fresh worker without chat memory.

## 9. Requirements / assurance impact

No new accepted Requirement is introduced here.

Existing coverage appears sufficient:

- `REQ-TRACE-001`: material work remains traceable through Goal/Need/Pain → Requirement → Decision/Delivery/Feedback.
- `REQ-WF-001`: formalizable invariants should not depend only on prompt/model discipline.
- `REQ-STATE-001`: curated state must remain restartable and not chat/provider dependent.
- `REQ-UX-001/002/003`: owner-readable audit/challenge views must expose evidence, method, uncertainty and correction/demotion.
- `REQ-MTH-003/004`: method status/application and promotion boundaries remain visible.
- `REQ-SRC-*` / `REQ-OCR-*` / `REQ-RET-*`: later document-evidence spike may touch them, but this Selection PR does not implement those capabilities.

Assurance impact:

- This PR is documentation/reconciliation only.
- No hard rule, schema, validator or architecture decision is added.
- A future machine-readable selection projection would require #48/#61/#63 trace and negative tests.

## 10. Systemic reconciliation matrix

| Claim / artifact / area | Disposition | Reason / follow-up |
|---|---|---|
| `AGENTS.md` bootstrap and Handoff Gate | `retain` | Already requires repo truth and handoff completeness. |
| `PROJECT_STATE.md` as navigation view | `retain/refine` | Correct role, but current next-action wording should be derived from explicit Selection state. |
| Lampe 420 Work Order | `retain/refine` | Valid resumable bounded Work Order; refine global interpretation to not-selected-current unless authorized. |
| D2 context mechanics | `retain/refine` | Correctly requires external priority authority; future consumer test should preserve selection-open. |
| PR #76 Sachenbacher | `defer/refine` | Reconcile final intended branch state before merge; no current selection implication. |
| #47 U1 research owner | `retain` | Active independent research owner; no selection inference. |
| #60 Method Work | `retain` | Supporting/cross-cutting Method Truth; not historical current slice. |
| #64 audit input | `retain` | Review input, no direct Requirement/Architecture authority. |
| Document-Evidence spike | `defer` | Valid technical pain/candidate; separate from selection and PR promotion. |
| New workflow/lifecycle engine | `reject` | No current requirement; #64 warns against new meta-system. |
| New Requirement promotion | `reject` | Existing Requirements cover the issue. |
| Root/Handoff full matrix | `reject` | Would make `PROJECT_STATE.md` a second truth store. |
| `selection-open` | `retain` | Correct state until explicit owner-authorized selected-current exists. |

## 11. Exactly one next small repo step

After this artifact is reviewed, the next single small step should be:

> Update `PROJECT_STATE.md` with a short derived Current Work Selection line: `selection-open`; link this artifact; mark Lampe as `resumable`, PR #76 as `branch-candidate`, #47 as active independent research owner, #60 as supporting Method Truth; do not choose a Vertical Research Slice in that same PR unless the Research/Product Owner explicitly authorizes it.

That step should be a root/handoff derivation only, not new Fachforschung and not D2 code work.
