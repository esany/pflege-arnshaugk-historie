# WP1 Implementation Admission — Canonical Research State Spine v0 + derived audit roundtrip

**Date:** 2026-09-23  
**Status:** `ADMITTED / bounded implementation authority effective on integration / no implementation performed in this admission cycle`  
**Technical Lead:** #48  
**Development / Verification:** #59  
**Requirements Authority:** #42  
**Trace / Assurance:** #63  
**Rebuild re-entry:** #92  
**Base main:** `3831f4fda71bc00edfcbebcfbb59009a6a46d08c`  
**Canonical conception:** `docs/architecture/fresh-rebuild-conception-20260923.md`  
**Implementation trace:** `DEC-STATE-SPINE-001` / `IMP-STATE-SPINE-001`

## 1. Admission decision

WP1 **Canonical Research State Spine v0 + derived audit roundtrip** is **ADMITTED** as a small, reversible implementation package.

The admission is narrower than a general research-state data model. The first implementation is a **canonical identity/owner/reference spine over existing canonical homes**, plus a read-only resolver/validator and a derived audit roundtrip. It is not a new content truth store.

The implementation may make stable machine-relevant research identities resolvable without copying the substantive source, finding or work-order content that already has a canonical owner.

The implementation must stop and return to #48/#42/#60/#54 as applicable if it would need to invent:

- historical or method semantics;
- a general promotion/state machine;
- a new canonical content owner for facts already owned elsewhere;
- a product-package boundary;
- a database/persistence platform;
- provider integration;
- a new historical Research Selection.

No prerequisite spike is required before implementation. The remaining unknowns can be preserved or measured without irreversible assumptions.

## 2. Admission question answered

**Question:** Is WP1 sufficiently requirements-, evidence-, consumer- and test-defined to admit a bounded implementation?

**Answer:** Yes, because all of the following are already established:

1. the relevant scientific distinctions are accepted Requirements/contracts rather than solution hypotheses;
2. a real #51 Source/Representation/Instance/Findspot path exists;
3. #55 is a real current read-only consumer and currently relies on a manually assembled regenerable projection for the real Sachenbacher chain;
4. #61 supplies a real structured Work Order / derived CurrentContext boundary that demonstrates restartable reference use without requiring Work Order content to move into WP1;
5. #63 can bind the implementation to Requirements, drivers, files and later verification;
6. the implementation can remain Git-native, read-only with respect to scholarly content, and fully reversible;
7. no database, package reorganization, provider choice, Method Application model or promotion engine is needed for the first slice.

## 3. A — WP1 current-state inventory

| Surface | Current reality | Classification | WP1 disposition |
|---|---|---|---|
| #50 / `canonical-research-state.md` | technology-neutral identity/state contract | canonical architecture contract | controlling input |
| Source ledger | owns bibliographic/archival Source identities such as `SRC-LIT-0001` | canonical domain/research state | reference, never copy as second truth |
| #46 findings artifact | owns historical Finding `F-U2-009` | canonical research state | reference, never copy as second truth |
| #51 Sachenbacher v0.3 manifest | real fingerprinted Instance + neutral locator reference case | bounded technical/reference state | reuse as real input/adapter fixture |
| #55 `audit.py` | deterministic read-only audit renderer | current real consumer | adapt to consume resolved canonical references |
| #55 real audit test projection | manually assembled regenerable structure from #51/#46 | derived test projection | eliminate manual real-state assembly |
| #61 Lampe Work Order | real structured task/restart state referring existing Source/Excerpt/Finding homes | separate canonical task state | reference-only; do not absorb |
| `context.py` / `context_spec.py` | derived CurrentContext / restart mechanics | product-supporting operational capability | reuse pattern; no merge into state spine |
| `mutation.py` | bounded file-write guard | operational support | reuse only for implementation hygiene; not Research-State promotion |
| #54 | general candidate/promotion/demotion contract not implemented | planned | outside WP1 |
| #57 | provider-removal/restartability verification | planned + synthetic checks | later consumer/cross-cutting acceptance |
| #63 | current trace validator and changed-code guard | implemented assurance | mandatory implementation trace |

### Material current gap

The real #55 Sachenbacher audit is correct but its test constructs a **regenerable manual projection** containing Source, Representation, Instance, Excerpts/Findspots and Finding references.

That projection is explicitly not canonical Research State.

WP1 addresses this gap without making that projection canonical: it provides stable machine resolution from an identity/reference registry to the existing owners and derives the audit input from those owners/adapters.

## 4. B — Requirement and driver trace

### 4.1 Direct WP1 obligations

| Requirement | Driver basis | WP1 obligation |
|---|---|---|
| REQ-SRC-001 | G-004, G-006, N-005 | Source and Representation remain distinct and machine-resolvable |
| REQ-SRC-002 | N-005, N-015 | inspected Instance is distinct from Source/Representation/provider locator |
| REQ-SRC-004 | G-004, N-006, P-004 | Finding can resolve to precise Findspot and parent Instance |
| REQ-EPI-004 | G-006, G-009, N-014 | unresolved/missing stays explicit and is never inferred away |
| REQ-EPI-006 | G-006, N-015 | semantic research-state roles remain distinguishable |
| REQ-STATE-001 | G-008, N-015, N-017, P-010 | machine-relevant references are restartable without chat/provider |
| REQ-STATE-002 | G-008, G-012 | canonical references remain distinct from generated audit/context |
| REQ-WF-001 | N-017 | record/ref integrity and settled role boundaries are deterministic |
| REQ-UX-001 | G-009, N-015, N-018 | audit can navigate Finding → evidence path from the same canonical basis |
| REQ-LEAN-001 | G-011, G-012, N-020, P-016 | reuse existing mechanisms; no speculative platform/component expansion |
| REQ-TRACE-001 | G-011, N-015 | WP1 remains traceable through decision, implementation, verification and later use |

### 4.2 Constraints only in WP1

- **REQ-SRC-003:** WP1 must not flatten editorial/normalization layers, but v0 does not introduce an editorial-text model.
- **REQ-EPI-005:** AI output cannot become Evidence through the spine.
- **REQ-BND-001:** derived audit is read-only and cannot back-write Research State.

### 4.3 Future consumer requirements, not WP1 scope

- REQ-UX-002 / REQ-UX-003: later owner-facing challenge/progressive-disclosure behavior;
- REQ-WF-002: later processing/search execution provenance;
- Method Profile/Application Requirements: #60/#61 own semantics and maturity;
- provider availability / retrieval / rights requirements: later #49/#53/#56/#57 consumers.

Admission does not claim these as implemented.

## 5. C — Consumer-first scope

| Consumer | Classification | Consequence |
|---|---|---|
| #55 Derived Audit | **current-real-consumer** | first implementation target |
| #51 Document/Findspot reference case | **current-bounded-fixture producer/input** | real falsification path; not a generic product model |
| #61 Work Order / CurrentContext | **current-real adjacent consumer of stable refs** | references spine identities; its task truth remains separate |
| #57 Restartability / provider removal | **near-term dependent** | tests provider-neutral readability; no new availability model in WP1 |
| #49 Provider resolver | **future consumer** | must map to internal IDs later; no provider code now |
| #53 Retrieval provenance | **future consumer** | may return spine refs later; no search/index now |
| #54 Promotion/transition | **future consumer** | general mutation/history semantics deferred |

This consumer set justifies one small shared identity/reference capability, but not a database, workflow engine, shared runtime framework or universal ontology.

## 6. D — Minimal State Spine v0 boundary

### 6.1 What the spine owns

The v0 spine owns only **machine addressability and canonical ownership references** for stable roles required by the admitted path.

A v0 record may carry only fields justified by an accepted invariant or consumer, such as:

- stable internal `id`;
- settled `role`;
- `canonical_ref` identifying the authoritative home/record;
- optional basis/version reference needed to detect stale resolution;
- no substantive statement/content copied merely for convenience.

### 6.2 Role disposition

| Role | WP1 disposition | Reason |
|---|---|---|
| Source | **IN-WP1 as identity/owner ref** | direct current path and REQ-SRC-001 |
| Representation | **IN-WP1 as identity/owner ref** | direct current path |
| Inspected Instance | **IN-WP1 as identity/owner ref** | direct current path and REQ-SRC-002 |
| Findspot | **IN-WP1 as identity/owner ref** | direct current audit path and REQ-SRC-004 |
| Finding | **IN-WP1 as identity/owner ref** | direct current audit root; content stays in finding owner |
| Derivative | **REFERENCE-ONLY / schema role may be admissible, no real v0 record required** | current Sachenbacher primary path does not require a derivative |
| Excerpt | **REFERENCE-ONLY / DEFER concrete v0 record** | existing canonical excerpt homes remain separate; #51 path uses locators |
| Claim/Answer | **NOT-NOW as canonical role** | current real audit root is derived navigation, not a historical claim |
| Research Hook / Hypothesis | **DEFER** | no current WP1 consumer |
| Work Order | **REFERENCE-ONLY** | #61 owns task state |
| Method Application | **DEFER** | current real audit correctly exposes it as missing/unresolved |
| Review / Validation | **REFERENCE-ONLY** | existing owners remain authoritative |
| Rights / Admission | **DEFER** | no current WP1 consumer |
| Provider Reference / Availability | **REFERENCE-ONLY** | providers remain attributes of their owners, not spine identity |
| general History / Supersession | **DEFER to #54** | WP1 must not create a universal transition model |

### 6.3 Hard non-goal

WP1 must not introduce a universal `ResearchObject` type or add fields “for later”.

## 7. One fact / one canonical home

| Fact | Canonical owner during WP1 | Spine behavior |
|---|---|---|
| Sachenbacher bibliographic/source identity | `docs/research/cases/orlagau-source-ledger.md#SRC-LIT-0001` | stable ID + canonical ref only |
| F-U2-009 historical finding/content/status | `docs/research/cases/u2-knau-orlagau-quellenbefunde.md#F-U2-009` | stable ID + canonical ref only |
| #51 exact reviewed PDF Instance and locator geometry | `tools/document_evidence/data/sachenbacher-2022-reference-v0.3.json` | resolve/adapt; do not manually duplicate geometry |
| Lampe Work Order | `docs/research/cases/u2-lampe-420-work-order.json` | reference only |
| derived audit navigation root | generated by audit capability | never canonical |
| method application absent in real Sachenbacher chain | explicit missing/unresolved | do not invent a Method Application |

If implementation discovers that a material fact would need two authoritative copies, it must STOP and redesign the reference/derivation path rather than synchronize both.

## 8. Canonical vs derived boundary

### Canonical in this WP

- provider-neutral internal identity;
- role;
- canonical owner reference;
- only the minimum structural reference metadata required to resolve that owner without ambiguity.

### Remains canonical elsewhere

- source metadata and research use;
- inspected-instance/locator technical reference details already owned by #51;
- historical finding prose/status;
- Work Order/task truth;
- method/review/rights facts.

### Derived/regenerable

- normalized loader output;
- #55 audit Markdown;
- audit navigation root;
- CurrentContext;
- any convenience projection used by tests;
- later indexes/UI state.

**Deletion test:** deleting all generated audit/projection output must lose no curated research state.

## 9. Mutation boundary

WP1 is read-only with respect to scholarly content.

Allowed write behavior during implementation is limited to creating/updating the admitted technical registry/schema/tests and the implementation trace.

WP1 does **not** implement:

- finding promotion/demotion;
- source/entity merge;
- scholarly correction;
- Method Application creation;
- rights/admission mutation;
- provider writes;
- historical content migration.

If a real Research-State correction is required to make the implementation pass, STOP and hand off to the canonical research owner. General transition semantics return to #54.

## 10. Reuse / architecture fitness

### Reuse/adapt

- existing JSON/JSON-Schema and deterministic validation patterns;
- `tools/operational/core.py` loader/schema helpers where sufficient;
- existing #55 renderer rather than a new UI;
- #51 real reference manifest as bounded input;
- #61 Work Order only as a separate restart/reference surface;
- #63 current trace/changed-code guard.

### Do not build

- database;
- RDF/graph store;
- workflow engine;
- event-sourcing platform;
- `src/histo_orla/` package;
- provider adapters;
- OCR/retrieval;
- MCP/Skill/UI stack;
- broad shared runtime.

### Related-system check

Fresh current-state review of `esany/Wissensarbeit` and `esany/paleo-type` supports the same bounded choice: canonical ownership + rebuildable derived context/views, deterministic reference validation, and no invented next action/authority. Neither repository is imported as semantic authority.

### SOTA disposition

No new external technology/dependency is selected by this admission. The implementation uses already-established repository mechanisms. Therefore no new technology SOTA decision is necessary for admission. If implementation requires a new persistence/library/platform choice, STOP and return to #48 for explicit technical research/fit comparison.

## 11. Acceptance tests

### AT-01 — One Fact / One Canonical Home
The bounded real path contains no manually synchronized second source/finding/work-order truth.

### AT-02 — Identity Separation
Source, Representation and Instance are different stable IDs. Provider key/path/hash cannot substitute for Histo-Orla identity.

### AT-03 — Real Findspot Roundtrip
For the bounded Sachenbacher path, a Finding ref resolves through the admitted spine/adapters to the correct #51 findspots and exact inspected Instance/Source without manual audit projection assembly.

### AT-04 — Unresolved Preservation
`R51-06` and any missing Method Application remain explicitly unresolved/missing through load → resolve → audit.

### AT-05 — No Silent History/Correction
WP1 does not overwrite a canonical predecessor. Any encountered correction that needs research-state history is handed to #54/canonical owner.

### AT-06 — Derived Audit Reproducibility
The same canonical basis yields the same audit output; the renderer does not mutate/enrich canonical state.

### AT-07 — Derived Deletion Safety
Deleting generated audit/projection output loses no Source, Instance, Findspot, Finding or Work Order state.

### AT-08 — Fresh-context Resolution
A fresh authorized context can resolve the bounded Source/Instance/Findspot/Finding chain from repository state without old chat.

### AT-09 — Broken Reference Failure
Unknown ID, duplicate spine ID, missing canonical ref or ambiguous role/ref resolution fails explicitly; no path/name plausibility repair is allowed.

### AT-10 — No Domain-Semantics Invention
No test or loader creates historical, editorial, method, validation or Research-Selection meaning not supplied by the canonical owner.

## 12. Negative tests

1. Zotero key used as Histo-Orla Source ID → fail.
2. local/provider path used as Instance identity → fail.
3. Findspot resolves to a different Instance than its bounded owner path → fail.
4. audit contains substantive research information not resolved from an owner/input → fail.
5. unresolved/missing becomes resolved/false/empty → fail.
6. implementation tries to overwrite historical finding content/history → outside WP1 / fail-handoff.
7. generated audit/projection is edited as canonical truth → unsupported/fail.
8. missing reference is reconstructed from matching label/path → fail closed.
9. fixture-only field/role is generalized without Requirement + current consumer → reject in schema/review.
10. spine/audit creates a Research Selection or scholarly NEXT ACTION → fail.

## 13. Unknown classification

| Unknown | Class | Disposition |
|---|---|---|
| exact physical module filenames | SAFE-TO-DEFER | reversible within admitted paths |
| exact JSON record grouping | MEASURE-IN-IMPLEMENTATION | choose smallest that satisfies ATs |
| whether a reusable common reader emerges | MEASURE-IN-REAL-USE | no extraction until second real consumer |
| product-package boundary | SAFE-TO-DEFER | `src/histo_orla/` trigger not met |
| Method Application representation | SAFE-TO-DEFER | keep missing/unresolved |
| general History/Supersession model | SAFE-TO-DEFER | #54 |
| provider availability model | SAFE-TO-DEFER | #49/#57 |
| owner burden/benefit | MEASURE-IN-REAL-USE | feedback after implementation |
| cross-case generality | MEASURE-IN-REAL-USE | coverage ceiling forbids claim |

**IMPLEMENTATION-BLOCKER:** none.  
**SPIKE-BEFORE-IMPLEMENTATION:** none.

## 14. Coverage ceiling

This WP1 may establish only that, for the explicitly admitted roles and bounded fixtures:

- stable provider-neutral identities can resolve to their existing canonical owners;
- the current real #51/#46 evidence path can feed the #55 audit without a manually assembled second real-state projection;
- missing/unresolved state and reference failures remain explicit;
- generated audit/context state is rebuildable.

It does **not** establish:

- a complete/general historical research-state ontology;
- all Source/Excerpt/Finding cases;
- provider integration or current byte availability;
- OCR/HTR;
- retrieval;
- Method Conformance;
- Promotion/Transition semantics;
- Rights Admission;
- UI/workplace utility;
- owner acceptance;
- cross-case generality;
- any historical truth beyond the referenced canonical research owners.

## 15. Bounded implementation Work Order

### WORK PACKAGE
`WP1-STATE-SPINE-V0` — Canonical Research State identity/owner/reference spine + derived audit roundtrip.

### PRIMARY FUNCTION
Architecture / Development / Research Software Engineering.

### OWNERS
#48 Technical Lead; #59 Development/Verification; #42 Requirements controlling; #63 trace.

### CANONICAL BASIS
- main at admission: `3831f4fda71bc00edfcbebcfbb59009a6a46d08c`;
- this admission artifact;
- `docs/architecture/fresh-rebuild-conception-20260923.md`;
- `docs/architecture/contracts/canonical-research-state.md`;
- #51/#55/#61 current owners and fixtures.

### IN SCOPE

1. introduce the smallest structured **identity/owner/reference registry** for admitted roles;
2. validate stable ID uniqueness, supported role and resolvable canonical ref;
3. add a read-only resolver/adapter sufficient for the bounded Sachenbacher chain;
4. adapt the #55 real audit test/path to derive its input from the registry + existing canonical owners/#51 reference input rather than `_real_sachenbacher_projection()`;
5. retain missing/unresolved markers;
6. add deterministic acceptance/negative regressions above;
7. update #63 trace to implementation/verification status only as work actually occurs.

### OUT OF SCOPE

- changes to historical source/finding meaning;
- Research Selection;
- changing #51 locator decisions;
- broad source ledger migration;
- Work Order schema redesign;
- Method Application creation;
- provider/OCR/search/UI;
- general promotion/history engine;
- database;
- product package / repo reorganization.

### ALLOWED TECHNICAL SURFACES

The implementation trace admits changes only within:

- `tools/research_state/**` **or a strictly smaller equivalent location chosen under #48 without changing semantics**;
- `tools/operational/audit.py`;
- `tools/operational/tests/test_audit.py`;
- `tools/assurance/data/trace-records.json`.

If the implementer chooses not to create `tools/research_state/**`, reuse under an existing smaller operational module is allowed only if the same boundaries and tests are preserved.

### FORBIDDEN WITHOUT HANDOFF / NEW TRACE

- `docs/research/cases/**` substantive research content;
- `tools/document_evidence/data/**` reviewed #51 reference decisions;
- `src/**`, `app/**`, `histo_orla/**`;
- provider/integration/OCR/retrieval/UI code;
- Requirements text/semantics;
- Method Truth;
- #54 promotion semantics.

### IMPLEMENTATION STEPS

1. fresh bootstrap and clean branch/worktree;
2. re-check exact basis SHAs and current #63 active trace;
3. write the smallest schema/record contract required by AT-01..AT-10;
4. implement read-only loading/resolution with explicit failure on missing/ambiguous refs;
5. implement bounded #51 adapter/resolution;
6. replace the real audit test’s manually assembled projection with resolved state;
7. run acceptance + negative regressions;
8. run full Project Assurance;
9. update `IMP-STATE-SPINE-001` with actual implementation files/verification and only then change status from `active`;
10. return for review; do not expand scope to fix unrelated debt.

### PREFLIGHT

Before any code mutation the implementation context must confirm:

- fresh `main`/branch base and no unintended working-tree changes;
- Python/runtime required by current repository tests is available;
- current #51 v0.3 manifest, #55 audit code/tests, #63 trace and this admission artifact match the declared basis or changes are reconciled;
- `IMP-STATE-SPINE-001` is present and `active`;
- Project Assurance can be executed.

If runtime/dependency/basis admission fails: **STOP before code mutation**.

### STOP / HANDOFF CONDITIONS

Stop and return if:

- a required field has no accepted Requirement/current consumer;
- a canonical research fact would need duplicate manual ownership;
- historical/method meaning must be invented;
- a #51 reviewed locator/instance decision must change;
- a new provider/library/database/package/platform is required;
- promotion/history semantics beyond reference integrity become necessary;
- the bounded real chain cannot be derived without migrating substantive research content;
- scope must touch a forbidden path.

## 16. #63 trace contract

The admission creates:

- **DEC-STATE-SPINE-001** — local-reversible architecture/delivery decision: use a minimal identity/owner/reference spine, not a new content store/platform.
- **IMP-STATE-SPINE-001** — current bounded implementation trace with status `active`.

`active` here means **implementation is admitted and the trace can authorize the separately started code work**. It does not mean code was changed in this admission cycle.

No Requirement delivery status changes to `in-progress` solely because admission is complete.

## 17. Post-implementation verification and feedback

Technical verification must cover AT-01..AT-10, NT-01..NT-10 and Project Assurance.

Later owner/workflow evidence must separately test whether the implementation actually reduces:

- manual real-state projection/assembly;
- restart reconstruction;
- duplicated maintenance;

without increasing:

- epistemic hiding;
- correction friction;
- owner meta-work.

Technical PASS is not owner acceptance or scholarly validation.

## 18. Next exact action after integration

Start a **new fresh implementation Work Context** for `WP1-STATE-SPINE-V0` from this artifact and `IMP-STATE-SPINE-001`.

That implementation context may execute only the bounded scope above.

This admission cycle ends here.

**STOP: no code, schema implementation, migration, fixture rewrite or implementation run is performed by this admission work.**
