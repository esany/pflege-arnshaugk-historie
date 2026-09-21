# Histo-Orla – Agentic Refactoring Execution Plan

**Status:** execution-preparation / reviewed after failed admission / no new requirement-or-method authority  
**Work Owners:** #48 Technical Lead, #59 Development & Verification  
**Current calibration lane:** #53 / PR #119  
**Review input:** #64 / PR #118  
**Stand:** 2026-09-20

## 1. Purpose

This plan turns the Deep-Research findings into an execution sequence that is safe to hand to bounded implementation agents.

It does **not** create new product scope, Requirement authority, Method Truth, historical Findings, Research Selection or a new agent framework.

The immediate correction is mandatory:

> **No implementation agent is released until the current-stage prerequisites are proven executable in the actual checkout and execution environment.**

The first #53 calibration exposed that the earlier plan had confused:

1. a real Source/Instance/Findspot provenance chain;
2. a text-bearing retrieval corpus;
3. current execution-context availability.

Those are not equivalent.

## 2. Non-loss contract

Every stage preserves the full accepted Histo-Orla requirement set. A bounded increment may implement only a subset, but it may not weaken or silently defer the rest.

Hard cross-cutting invariants include:

- Source != Representation != Instance != Derivative != Findspot/Excerpt != Finding != Claim;
- AI output is not Evidence and not independent validation;
- unresolved, contradiction, missing and unavailable are valid states;
- Retrieval Hit != Finding/Claim;
- exact/auditable retrieval must work without LLM/semantic retrieval;
- query/corpus conditions must be reconstructable;
- curated/canonical state must remain distinct from regenerable indexes/views;
- provider IDs/paths are references, not sufficient internal identity;
- direct source inspection requires actual current Evidence Availability;
- material technical work remains traceable to accepted Requirements and G/N/P drivers.

## 3. Admission model

### 3.1 Current-stage prerequisites

A Work Order is executable only if **all** prerequisites required for its current action are pass.

The existing context core defines:

~~~text
prerequisite fail       -> CurrentContext.status = blocked
prerequisite unresolved -> CurrentContext.status = unresolved
unresolved[] non-empty  -> CurrentContext.status = unresolved
otherwise                -> CurrentContext.status = ready
~~~

Therefore:

> Downstream research/development dependencies that are not required for the current bounded action must **not** be stored as current prerequisites or unresolved.

They are recorded separately as downstream/deferred dependencies.

### 3.2 Mandatory preflight before any implementer

Before code mutation:

1. checkout is the intended repository and branch;
2. working tree is clean or contains only explicitly owned changes;
3. fresh bootstrap according to AGENTS.md;
4. current Work Order is loaded from the checkout;
5. all prerequisite basis fingerprints match;
6. CurrentContext.status == ready;
7. required input is actually present at the required evidence level;
8. required dependencies/tooling can be installed or CI fallback is explicitly known;
9. acceptance + negative tests are defined;
10. no Requirement/Method/Architecture/Selection decision is being smuggled into implementation;
11. branch/PR/trace/coverage persistence target is known.

If any condition fails, **no implementation begins**.

## 4. Evidence-availability ladder

For every real-source stage, record these separately:

~~~text
IDENTIFIED
RETRIEVABLE / RESOLVABLE
ACCESSIBLE NOW
INSPECTABLE IN CURRENT CONTEXT
TEXT/DERIVATIVE AVAILABLE FOR REQUESTED OPERATION
FINDSPOT-MAPPED
RIGHTS-ADMISSIBLE
VERSION/FINGERPRINT REVALIDATED
~~~

A PASS at one level does not imply a PASS at the next.

Current Sachenbacher path:

- bibliographic/source identity: available;
- inspected complete PDF identity/hash: established historically under #51;
- locator geometry: established;
- real audit projection: available;
- current general byte resolver: not established;
- text-bearing searchable corpus in repository/runtime: not established;
- therefore real #53 retrieval: **not admitted yet**.

## 5. Current dependency truth

### #49 Zotero / OneDrive

Established:

- local Zotero read-only metadata;
- item/tag/note reads;
- attachment metadata;
- one legacy local file locator and filesystem-entry reachability.

Not established:

- target OneDrive/device-independent resolver;
- remote Zotero/OneDrive authorization in generic execution context;
- concrete provider-stable byte identity;
- general byte availability/hydration;
- Zotero fulltext as admitted Histo-Orla retrieval derivative.

Consequence: real-library retrieval remains downstream.

### #51 Document / Findspot

Established for one real Sachenbacher instance:

- concrete PDF fingerprint/hash/size/page count;
- owner-reviewed locators;
- page/region geometry;
- real Source/Representation/Instance/Findspot provenance;
- fail-closed byte-fingerprint roundtrip when bytes are supplied.

Not established:

- generic text extraction/corpus admission;
- generic resolver from current work context to those bytes.

### #55 Audit View

Established:

- deterministic read-only audit renderer;
- real Sachenbacher provenance chain can be represented via a regenerable test projection;
- missing method state remains missing/unresolved.

Not established:

- a canonical or searchable real text corpus.

### #57 Availability / Restartability

Still planned. This is the correct owner for distinguishing identity from actual research-ready availability in later real slices.

## 6. Execution waves and gates

### Wave 0 — Planning/Admission repair

**Model:** Sol High / strong planner-reviewer.  
**Implementation:** none.

Required outputs:

- this execution plan;
- corrected #53 work-order admission semantics;
- corrected Deep-Research sequencing where it implied real #53 readiness too early;
- #55 clarification that its real audit chain is not itself a text-bearing retrieval corpus;
- Project Assurance green for planning changes.

Exit gate:

~~~text
all current calibration prerequisites PASS
CurrentContext.status == ready
downstream real-corpus gaps isolated outside current context
~~~

### Wave 1 — Synthetic Exact Retrieval calibration

**Owner:** #53/#59 under #48.  
**Implementer:** Terra only after Wave-0 admission.  
**Reviewer:** Sol High.

Input:

- existing synthetic provider-neutral state in tools/operational/tests/test_audit.py;
- existing text-bearing synthetic excerpt;
- existing Source/Representation/Instance/Derivative/Findspot links.

Scope:

- case-sensitive literal substring/phrase retrieval for this bounded calibration;
- equality filters only over existing provenance IDs;
- exact query + match mode + filters;
- caller-supplied corpus reference plus deterministic SHA-256 corpus fingerprint;
- explicit implementation version;
- known-hit;
- no-hit;
- hit -> excerpt/findspot -> derivative/instance/representation/source roundtrip;
- missing ancestry / unknown filter / empty query fail closed;
- no LLM/semantic layer.

Forbidden:

- real-source verification claim;
- historical variant expansion;
- schema/state invention;
- database/index persistence;
- src/histo_orla extraction.

Exit criteria:

1. preflight READY;
2. exact-search unit tests pass;
3. negative tests pass;
4. existing operational/document/requirements/assurance suites pass;
5. #63 trace + #59 coverage updated only to demonstrated level;
6. PR Project Assurance green;
7. Sol review finds no semantic/authority drift.

Calibration decision:
- PASS -> Terra admitted for equivalent bounded Tier-B implementation;
- FAIL-semantic -> stronger model or tighter contract;
- FAIL-environment -> fix execution environment, do not change Requirements;
- FAIL-contract -> return to #48 planning, not to implementer improvisation.

### Wave 2 — Real Evidence/Corpus Admission

No retrieval implementation yet.

**Owners:** #49/#51/#57 with #48.

Goal: make one real source operation-ready without creating a second truth store.

Empirically discriminate the smallest sufficient path:

- existing fingerprinted PDF bytes in an authorized local context;
- native PDF text layer extracted as regenerable derivative;
- Zotero indexed fulltext if provider semantics/findspot fidelity are sufficient;
- OCR/HTR only if required by the chosen source.

Admission record must prove:

~~~text
source_id
representation_id
instance_id
byte/version fingerprint
derivative identity + parent
text availability
page/findspot mapping
rights/admission
regeneration/revalidation method
~~~

No provider path becomes canonical identity.

**Exit gate:** one concrete real text-bearing derivative can be opened/rebuilt and maps hits back to the accepted instance/findspot model.

### Wave 3 — Real Exact Retrieval falsification

**Owner:** #53.  
**Implementer:** Terra if Wave 1 passed and Work Order is fully bounded.  
**Reviewer:** Sol High.

Tests:

- known real query hit;
- no-hit with explicit search boundary;
- query/corpus/version log;
- result -> derivative -> findspot -> instance -> source roundtrip;
- source bytes/derivative changed -> stale/revalidation path;
- verify that a no-hit result does **not** automatically become a Finding or completeness claim.

Only after this stage may REQ-RET-001/003/SRC-004 coverage advance beyond synthetic implementation.

### Wave 4 — Controlled historical variants

**Owners:** #53 + #60/domain authority for real historical expansions.

First synthetic contract, then real domain-owned variants.

Each expansion records:

- original user query;
- expanded variant;
- provenance/rationale for variant;
- filters/corpus;
- results;
- no automatic entity merge.

A variant list generated only by a model is not promoted to authoritative historical equivalence.

### Wave 5 — Shared runtime reader / product-code trigger

Do **not** extract a shared product package merely because retrieval exists.

Trigger requires at least two real runtime consumers, for example:

~~~text
retrieval + audit view
or
retrieval + evidence availability/resume
~~~

using the same provider-neutral state access.

Then #48 reviews actual duplicated responsibility, stable I/O contract and the smallest extraction path. Only then consider src/histo_orla/.

### Wave 6 — Restartability / Availability integration

**Owner:** #57.

Tests:

- provider unavailable -> explicit degraded/unavailable;
- internal identities remain usable;
- regenerable search/index loss does not destroy research meaning;
- fresh context can determine next allowed action;
- if direct inspection is required, unavailable bytes block truthfully.

### Wave 7 — Heterogeneous #47 Vertical Research Slice

Only after real retrieval + availability are proven on at least one source chain.

A small owner-selected #47 question uses:

~~~text
question
-> context
-> source/instance resolve
-> admitted evidence
-> retrieval
-> findspot inspection
-> method application
-> research finding/unresolved
-> research-first view
-> restart
~~~

Historical Research Output and Product/System Learning remain separate.

### Wave 8 — Read-model probe only if measured pain remains

SQLite/FTS or similar is admitted only if Wave 3/7 show concrete navigation/query friction.

Hard criteria:

- delete/rebuild;
- no read-model-only research truth;
- no canonical writeback;
- stable ID/provenance roundtrip;
- measurable owner benefit.

### Wave 9 — Thin skill/MCP/UI adapter

Only after stable capabilities exist. The adapter routes calls; it does not copy Requirements/Method Truth or own state.

## 7. Model allocation

### Sol High

Required for:

- prerequisite/architecture reconciliation;
- ambiguous evidence/corpus semantics;
- Requirement/Method/Authority boundaries;
- material cross-cutting refactor review;
- independent review of Terra output.

### Terra

Allowed only for:

- Work Order CurrentContext.status == ready;
- bounded implementation with settled semantics;
- explicit tests/negative tests;
- no material architecture decision;
- no historical/method promotion.

### Luna

Deferred until Terra calibration has produced stable task classes. Use only for mechanical edits where correct output is deterministically testable and no semantics are inferred.

## 8. Mandatory test matrix

| Test | Purpose | Gate |
|---|---|---|
| Work Order loads | no malformed execution packet | pre-implementation |
| Basis fingerprints current | no stale PASS | pre-implementation |
| Context status = READY | no hidden blocker | pre-implementation |
| Known hit | positive retrieval behavior | implementation |
| No hit | no fabricated result / no completeness claim | implementation |
| Equality filter + unknown-filter failure | filter behavior explicit, no inferred identity | implementation |
| Corpus fingerprint stability/change | reproducible corpus boundary | implementation |
| Findspot/source roundtrip | provenance retention | implementation |
| Missing/unresolved retained | no epistemic filling | regression |
| AI not required | REQ-RET-001 | regression |
| Changed bytes/derivative detected | stale result safety | real-source stage |
| Provider unavailable -> degraded | availability honesty | #57 |
| Existing Project Assurance | non-regression | every PR |
| Fresh-context restart | no chat dependency | integrated slice |
| Owner workflow acceptance | actual product value | vertical slice |

## 9. Review checklist

An independent material review must answer:

1. Did the implementer obey the current Work Order rather than infer downstream intent?
2. Was any downstream dependency silently converted into a current assumption?
3. Did any fixture become a second truth store?
4. Did any derived/test projection get mistaken for canonical state?
5. Did a provider locator become internal identity?
6. Did any Hit become Finding/Claim?
7. Did any missing/unresolved state disappear?
8. Is query/corpus/version provenance sufficient to explain reruns?
9. Did the change introduce product architecture without the required reuse trigger?
10. Are Coverage/Trace claims exactly proportional to what was tested?
11. Can a fresh agent resume from Git without this chat?
12. Does the change remove owner work rather than add another required meta-step?

Any no blocks promotion.

## 10. Current admission matrix (2026-09-20)

| Stage | Admission | Reason |
|---|---|---|
| Wave 1 synthetic exact retrieval | **READY after corrected Work Order preflight** | text-bearing synthetic fixture + provider-neutral provenance already exist |
| Real Sachenbacher exact retrieval | **NOT READY** | real chain has locators/provenance, but no admitted current text-bearing corpus/byte resolver |
| Historical variants on real corpus | **NOT READY** | depends on real corpus + domain-owned variant evidence |
| Shared runtime reader extraction | **NOT READY** | two real runtime consumers not yet demonstrated |
| SQLite/FTS read model | **NOT READY** | no measured post-runtime query/navigation pain |
| #47 vertical slice | **NOT READY** | first real retrieval/availability path must exist |
| thin Skill/MCP/UI | **NOT READY** | stable product capabilities not yet proven |

## 11. Immediate next action

Do **not** release an implementation agent until:

1. PR #119 Work Order deterministically derives CurrentContext.status == ready;
2. corrected planning files pass Project Assurance;
3. a Sol-level review confirms current prerequisites are sufficient and downstream dependencies are isolated;
4. only then run Terra on Wave 1.


## 12. Pre-implementation review evidence – 2026-09-20

The planning/admission repair was reviewed before releasing another implementation agent.

### Repository freshness

- current `main`: `ff2bc993d959afd594dff2acf772e0e608963f97`;
- PR #119 base: exact same commit;
- PR #119 current head at review start: `0fcf3d75915c1f8ab4a04e3be0c360d4bfbe88f9`;
- no newer `main` commit existed at the review point.

### Work-order admission check

Current Work Order:

`docs/development/work-orders/wo-ret-001-exact-retrieval-calibration.json`

Deterministic check against the actual `tools/operational/context.py` semantics:

- all current-stage prerequisites: `pass`;
- all declared basis Git blob SHAs: exact match;
- `open_blockers = []`;
- `unresolved = []`;
- derived `CurrentContext.status = ready`;
- real byte/corpus questions are isolated under `downstream_deferred_dependencies` and therefore do not falsely block the synthetic stage.

### Current prerequisite evidence

| Prerequisite | Result |
|---|---|
| accepted retrieval requirements basis | PASS |
| provider-neutral research-state contract basis | PASS |
| synthetic text-bearing fixture availability | PASS |
| delivery/trace/coverage basis | PASS |
| local assurance dependency setup declared | PASS |

### CI

- PR #119 Project Assurance Run #256 (`35541719983`): **success** on head `0fcf3d75915c1f8ab4a04e3be0c360d4bfbe88f9`;
- PR #118 sequencing correction Project Assurance Run #254 (`35541677959`): **success** on head `642d7aa01a0807aecba4f2d2360fa15124def46c`.

### Review findings corrected before release

1. Initial calibration wrongly assumed the real #55 audit projection was sufficient retrieval input.
2. First repair still put a downstream real-corpus gap into current `prerequisites/unresolved`, which would have forced another correct stop.
3. #55 Work-Owner text overstated readiness of real #53 retrieval; corrected.
4. PR #118 O.15 overstated readiness of real #53 retrieval; corrected to staged admission.
5. Work Order lacked explicit G/N/P drivers, acceptance tests, negative tests and forbidden-loss list; added.
6. Local `jsonschema` absence was an execution-environment setup omission; the repository already declares and CI installs `tools/requirements/requirements.txt`.

### Remaining review boundary

This review admits **only Wave 1 synthetic Exact Retrieval calibration**.

It does not admit:

- real Sachenbacher retrieval;
- real historical variant expansion;
- a shared runtime state reader;
- a product package boundary;
- SQLite/FTS;
- the #47 vertical slice;
- a Skill/MCP/UI layer.

Those remain gated by the earlier sections of this plan.



## 13. Second pre-implementation hardening review – 2026-09-21

The user explicitly challenged the earlier preparation as too assumption-driven. A second review therefore re-opened Wave-1 admission instead of relying on the prior READY result.

### 13.1 Revalidated prerequisite chain

Freshly re-read:

- root governance / project handoff / README;
- #42 Requirements authority;
- #48 Technical Lead;
- #49 Zotero/OneDrive capability boundary;
- #50 canonical research-state contract;
- #51 real Document/Findspot result;
- #53 Retrieval owner;
- #55 audit-view boundary;
- #57 availability/restartability;
- #59 delivery/verification;
- #63 traceability;
- #64 review findings;
- #92 architecture re-baseline;
- current PR #119 Work Order and admission regression.

The earlier suspicion is now explicit dependency truth:

```text
real Source/Instance/Findspot path
!= text-bearing retrieval input
!= currently available retrieval corpus
!= provider-independent byte resolver
```

Therefore no later stage may infer one level from another.

### 13.2 Requirements/driver review

Wave 1 is bounded by:

- REQ-RET-001;
- REQ-RET-003;
- REQ-SRC-004;
- REQ-EPI-004/005;
- REQ-WF-001;
- REQ-STATE-002;
- REQ-TRACE-001;
- REQ-LEAN-001.

Upstream driver references were rechecked in `problem-baseline.md`:

- G-004 concrete source/findspot traceability;
- G-008 restartable/provider-independent research state;
- N-006 exact findspot preservation;
- N-008 exact search + controlled historical variants;
- N-015 versioned non-duplicated research state;
- N-018 capability-specific acceptance criteria;
- P-004 search-hit loss of findspots.

No Requirement change is needed for Wave 1.

### 13.3 Additional ambiguity removed before Terra

The prior Work Order was directionally correct but still left several reversible choices to the implementation model. These are now fixed:

1. **Mutation boundary:** only retrieval implementation/test + exact trace/coverage files may change; fixture extraction is conditional and bounded.
2. **Trace contract:** reserve `IMP-RET-001`; initial state `implemented`, never `verified` before canonical CI + independent Sol review.
3. **Coverage ceiling:** only REQ-RET-001/003 may move `not-started -> in-progress`; REQ-SRC-004 remains `partial`; no other RET status may change.
4. **Deterministic result order:** hits sorted by `excerpt_id`.
5. **Malformed-state handling:** duplicate IDs, malformed relevant collections/records, and non-string non-empty text fail closed.
6. **Environment admission:** repository-declared Python dependency installation must succeed before code mutation. Failure is `HANDOFF/ENVIRONMENT`, not a reason to weaken checks.
7. **Corpus fingerprint policy:** Wave 1 fingerprints the complete supplied JSON-compatible state conservatively. This may over-invalidate after unrelated state changes, but avoids hidden corpus drift; narrowing is deferred to real-corpus evidence.
8. **Out-of-scope file need:** any need to edit outside the declared mutation boundary is a handoff, not implementer discretion.

### 13.4 Expanded Wave-1 test gate

Before release, the Work Order now specifies **9 acceptance** and **9 negative** tests, including:

- known hit / no hit;
- query/filter/corpus reproducibility;
- provenance roundtrip;
- no AI dependency;
- equality filter behavior;
- fingerprint stability/change;
- deterministic hit order;
- exact mutation/trace/coverage boundary;
- case/normalization non-equivalence;
- missing ancestry;
- no real-corpus laundering;
- no persistent state/index;
- unknown filter / empty query;
- duplicate IDs;
- malformed structures;
- invalid text type.

The Work Order admission regression must assert these contracts exist before implementation.

### 13.5 Stage-by-stage prerequisite register

| Stage | Required evidence/capability before release | Current status | Owner |
|---|---|---|---|
| Wave 1 synthetic exact | accepted REQ basis; provider-neutral synthetic text fixture; READY Work Order; local assurance setup; fixed tests/mutation boundary | **admitted after CI + this review** | #53/#59 |
| Wave 2 real corpus admission | actual bytes or admitted text derivative; parent Instance/Derivative; findspot mapping; rights; rebuild/revalidation path | **not ready** | #49/#51/#57/#48 |
| Wave 3 real exact | Wave 1 pass + Wave 2 admitted real corpus + known real query/search boundary | **not ready** | #53 |
| Wave 4 variants | Wave 3 + domain-owned variant rationale/evidence + expansion logging | **not ready** | #53/#60 |
| Wave 5 shared runtime reader | at least two real runtime consumers with demonstrated duplicated state-access responsibility | **not ready** | #48/#59 |
| Wave 6 availability/restart | real provider loss/degraded-state scenario + portable curated state | **not ready** | #57 |
| Wave 7 #47 vertical slice | owner-selected bounded question + real retrieval/availability path + applicable methods/evidence | **not ready** | #47/#60/#59 |
| Wave 8 read model | measured query/navigation pain after real integrated use | **not ready** | #48 |
| Wave 9 Skill/MCP/UI | stable product APIs/capabilities proven by real consumers | **not ready** | #48/#59 |

### 13.6 Release rule

Terra is **not** being trusted to resolve any prerequisite or design ambiguity.

Terra may be released only when all of the following are simultaneously true on the exact implementation checkout:

```text
clean intended branch
+ fresh bootstrap
+ repo dependency install succeeds
+ all Work Order basis fingerprints match
+ CurrentContext.status == ready
+ mutation boundary understood
+ 9 acceptance + 9 negative tests present
+ trace/coverage contract fixed
+ no hidden semantic/architecture decision
```

A failure before code mutation is a successful fail-closed admission result, not permission to improvise.
