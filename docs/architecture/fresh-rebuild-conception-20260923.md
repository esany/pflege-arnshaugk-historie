# Histo-Orla — Fresh Rebuild Conception

**Date:** 2026-09-23  
**Status:** fresh-rebuild-conception-complete / implementation-admission-required / no implementation authority  
**Re-entry owner:** #92  
**Technical / Architecture Lead:** #48  
**Requirements Authority:** #42  
**Development / Verification:** #59  
**Domain Method Truth:** #60  
**Input review:** #64 + D4 reconciliation  
**Current work selection:** selection-open  
**Authority:** architecture conception and technical derivation only. This artifact does not create Requirement, Method, Research Selection, Delivery or Implementation Authority.

## 1. Decision summary

This conception re-derives Histo-Orla from the accepted Requirements, the repository that actually exists, the reconciled F1–F14 project findings and D4 external research. It does not continue the old #92 / PR #119 roadmap by default.

The resulting target is deliberately smaller than the earlier platform-shaped hypotheses:

1. **Research truth remains Git-native and provider-independent.** Histo-Orla needs a small durable research-state spine for machine-relevant research objects and relations, but not a database, workflow engine, graph platform or universal ontology as canonical truth.
2. **Narrative scholarship and machine state have different jobs.** Rich argument, interpretation and synthesis may remain narrative/versioned artifacts. Stable machine-relevant identities, parentage, status, provenance, findspots, availability/admission facts and explicit references should become structured only where an accepted Requirement and a real consumer justify it. One fact has one canonical owner.
3. **Derived views and indexes are rebuildable.** Human-readable audit/workplace views, search indexes, caches, embeddings, context packets and reports are derived from canonical state. Their loss must not destroy the research record.
4. **External systems stay adapters, not truth owners.** Zotero remains bibliographic/attachment management; OneDrive remains Source of Bytes; Histo-Orla owns scholarly research state. Provider identifiers and paths are references, not Histo-Orla identity.
5. **Readiness is operation-specific and derived.** Existence, identity/provenance, byte availability, rights/admission, currency and fitness remain separate predicates. There is no single global readiness flag.
6. **Current small operational mechanisms are retained where they protect demonstrated losses.** Requirements/trace assurance, bounded context/resume, document-evidence roundtrip and derived audit rendering are useful evidence. They are not proof that the old Operational Core shape is the target architecture.
7. **Exact retrieval remains baseline-first.** A rebuildable local index such as SQLite FTS5 is a strong candidate for exact/filter/prefix/substring retrieval, but it is not selected as canonical storage. Historical variants remain an explicit controlled layer; semantic retrieval remains benchmark-admitted only.
8. **Standards are interoperability boundaries, not an ontology mandate.** JSON Schema is suitable for small structured records; W3C Web Annotation / IIIF can map findspots when applicable; ALTO/TEI can be consumed for layout/transcription where present; W3C PROV and RO-Crate are useful provenance/export mappings. None becomes Histo-Orla semantic authority.
9. **The owner-facing workplace is a required capability, not a preselected UI stack.** The first useful surface should be generated from canonical state, support progressive disclosure and reduce chat/text orchestration. CLI, static/generated view or local UI remain implementation options until tested.
10. **No implementation is authorized by this conception.** The first proposed implementation package is a bounded, reversible Canonical Research State Spine v0 plus derived audit roundtrip. It requires explicit implementation admission under #48/#59 before code or migration begins.

The old roadmap is dispositioned pointwise in §8. No old wave is automatically active.

## 2. Evidence and derivation boundary

### 2.1 Canonical project inputs

This conception used the current repository state on main beginning at commit c759d4eb2884f96314933a2949e002dd7ce1115d and freshly read:

- root AGENTS.md, PROJECT_STATE.md and README.md;
- #92 and the Fresh Rebuild Conception Work Context;
- #42 and the 39 baseline Requirements + 14 accepted extensions;
- Requirements structure and responsibility/dependency mapping;
- #48 requirements-to-architecture derivation contract;
- #59 delivery/verification coverage;
- #64 repeated-audit findings and D4 research/reconciliation;
- current #49–#63 issue state where architecture-relevant;
- current canonical research-state, operational execution and prior-art contracts;
- current code/tests in tools/requirements, tools/assurance, tools/operational and tools/document_evidence;
- merged real slices and regressions, especially #51, #55 and #61.

### 2.2 Evidence roles

The following are kept separate:

- accepted Requirement / Constraint: #42 authority;
- Domain Method Truth: #60 authority;
- PE: current repository / implementation / test evidence;
- OE: persisted owner/workflow evidence;
- ER: external scholarly/standards evidence;
- RS: related-system evidence;
- technical SOTA/tool evidence: evidence about implementation means;
- architecture inference: #48 solution reasoning;
- unresolved / design-testable unknown: explicitly retained.

No external standard, related repository or architecture pattern creates a Histo-Orla Requirement.

### 2.3 Current technical SOTA / standards inspected

Current sources were inspected on 2026-09-23 after the technical research questions were explicit:

- JSON Schema current specification: https://json-schema.org/specification and https://json-schema.org/draft/2020-12/
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/
- W3C Web Annotation Data Model family: https://www.w3.org/groups/wg/annotation/publications/
- IIIF Presentation API 3.0: https://iiif.io/api/presentation/3.0/
- IIIF Content State API 1.0: https://iiif.io/api/content-state/1.0/
- SQLite FTS5: https://www.sqlite.org/fts5.html
- SQLite JSON functions: https://www.sqlite.org/json1.html
- SQLite WAL: https://www.sqlite.org/wal.html
- Zotero Web API v3 / Local API: https://www.zotero.org/support/dev/web_api/v3/ and https://www.zotero.org/support/dev/web_api/v3/local_api
- Zotero linked/stored file behavior: https://www.zotero.org/support/attaching_files
- Microsoft Graph OneDrive addressing, content and delta: https://learn.microsoft.com/en-us/graph/onedrive-addressing-driveitems ; https://learn.microsoft.com/en-us/graph/api/driveitem-get-content?view=graph-rest-1.0 ; https://learn.microsoft.com/en-us/graph/api/driveitem-delta?view=graph-rest-1.0
- ALTO: https://www.loc.gov/standards/alto/
- TEI P5 zone/facsimile model: https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-zone.html
- RO-Crate: https://www.researchobject.org/ro-crate/

Related-system state was also read fresh from esany/Wissensarbeit and esany/paleo-type. They are challenge/prior-art inputs only.

## 3. A — Fresh current-state inventory

### 3.1 What actually exists

| Area | Current repository reality | Classification | Architectural consequence |
|---|---|---|---|
| Accepted Requirements | 39 baseline + 14 accepted extensions; #42 authoritative | governing/project | Full scope remains active; delivery order is not historical P0/P1/P2 or old #92 waves |
| Requirement assurance | JSON Schema/data/validator/tests under tools/requirements | operational support, implemented | Retain formal validation; do not confuse it with scientific validation |
| Value/decision/delivery trace | tools/assurance v0.1 + CI changed-code guard | operational support, implemented | Retain the trace invariant; reduce manual projection where possible |
| Enforcement projection | tools/operational/enforcement-map.json | operational support, implemented | Useful derived technical map; not Requirement truth |
| Shared operational mechanics | tools/operational/core.py | operational support, implemented | Small shared loader/schema mechanics justified; no evidence for a broad framework |
| Mutation guard | tools/operational/mutation.py | operational support, implemented/local | Protects bounded local writes; does not provide repo-wide GitHub admission or scholarly authority |
| Work context / resume | tools/operational/context.py + context_spec.py | product-supporting capability prototype, implemented | Retain derived-context pattern; do not promote to global workflow engine |
| Real Work Order | u2-lampe-420-work-order.json | domain/research canonical task state, one real fixture | Demonstrates task-specific structured restart state; generality remains limited |
| Document/findspot roundtrip | tools/document_evidence + Sachenbacher reference v0.3 | bounded product-capability falsification / pilot, implemented and reviewed | Strong evidence for stable instance + neutral page-space locator + derived highlights; not a general document platform |
| Audit rendering | tools/operational/audit.py | product-supporting read-only capability prototype, implemented | Strong pattern: derive audit from explicit refs, expose missing/unresolved, do not interpret |
| Real audit acceptance | #55 real Sachenbacher projection | technical validation complete; owner-workflow acceptance still open | Local correctness is not global utility |
| Canonical research-state contract | docs/architecture/contracts/canonical-research-state.md | architecture contract | Strong semantic constraint, but physical persistence/runtime still open |
| Zotero ↔ OneDrive | #49 | planned / read-first spike | No general provider resolver exists |
| OCR/HTR | #52 | planned / benchmark-required | No general OCR/HTR processing capability exists |
| Historical retrieval | #53 | planned | No general exact/variant retrieval runtime exists |
| Promotion / research-state mutation | #54 | planned beyond generic assurance | No general research-object transition runtime exists |
| Rights / external processing | #56 | contract/planned | No operational admission evaluator exists |
| Provider removal / export / research-ready availability | #57 | planned | No general export/restore/provider-removal runtime exists |
| Domain Method Profiles | #60 | research-needed / in progress | Architecture must reference method truth but cannot invent its schema/content |
| Product package | no src/histo_orla or equivalent | absent | Do not create a package for symmetry; introduce only when durable runtime consumers justify it |
| User-facing research workplace | absent | unmet | Owner pain remains: research is still text/chat/manual-orchestration heavy |
| Current research selection | selection-open | governing state | Architecture work creates no selected historical case |
| Repo-wide required PR enforcement | DD-20260903-001 open | platform blocker only | Does not block conception; remains a separate GitHub prevention gap |

### 3.2 What is currently only partial or locally proven

The following must not be overclaimed:

- Source/Representation/Instance/Findspot separation is proven in a bounded #51 reference case, not yet as a general persistence/integration path.
- Page/region roundtrip is proven for one concrete publication instance; OCR/HTR transformation itself was not exercised.
- CurrentContext is proven against one real Work Order; minimal sufficient restart context remains a design-testable unknown.
- Audit rendering is deterministic against structured input and one real projection, but the general canonical state feeding it does not yet exist.
- Requirements/trace CI proves formal repository invariants, not owner utility or scholarly sufficiency.
- Git history gives repository history, but does not by itself provide all domain-level demotion/supersession/provenance semantics required by research objects.

### 3.3 Manual synchronization / secondary-work surfaces

Current duplication is not treated as automatically harmful; each surface is evaluated against the loss it protects.

Material surfaces are:

1. accepted Requirement prose ↔ structured requirement records ↔ delivery coverage ↔ implementation trace;
2. issue/current-state pointers ↔ canonical artifacts;
3. Work Order fields ↔ owner/research artifacts;
4. document-evidence manifest ↔ source ledger / research finding references;
5. synthetic or manually assembled structured state needed to feed the audit renderer;
6. repeated owner/status/context prose used to restart work.

The key architecture problem is therefore not “remove documents” but:

> Which stable facts should have one structured canonical home so that audit, context, retrieval and verification can be generated without forcing interpretive research into an over-rigid schema?

This is a direct F2a/F2b/F3a/F3b/F5/F9 concern.

## 4. B — Requirement → responsibility re-derivation

The conception uses eight logical responsibilities. They are responsibilities, not mandatory packages/services.

| Responsibility | Main drivers | Accepted Requirements / constraints | Architecture concern |
|---|---|---|---|
| R1 Research State / Identity / Provenance | G-004, G-006, G-008; N-005, N-014, N-015; P-010, P-016 | REQ-SRC-001..004, REQ-EPI-004..006, REQ-STATE-001/002, REQ-BND-001 | stable identity, epistemic non-loss, history, provider independence |
| R2 Evidence Access / Availability | G-004, G-007, G-008; N-002, N-016; P-002, P-015 | REQ-INT-001/002, REQ-STATE-003, REQ-SRC-002, REQ-RGT-001/002 | identity ≠ locator ≠ availability ≠ admission; replaceable providers |
| R3 Document / Derivative / Findspot | G-004, G-006; N-006/007; P-003/004 | REQ-SRC-003/004, REQ-OCR-001..003 | byte/derivative provenance, exact roundtrip, layout loss |
| R4 Method / Work Context / Promotion | G-002/003/008; N-002/013/014/017/018/019 | REQ-MTH-001..005, REQ-RSCH-001..004, REQ-WF-001/002, REQ-VAL-001/002 | open exploration, controlled promotion, restartability, authority boundaries |
| R5 Retrieval | G-004/007; N-008; P-003/005 | REQ-RET-001..005, REQ-EPI-002/003, REQ-RSCH-002 | auditable exact baseline, historical variants, corpus/query provenance |
| R6 Audit / Research UX | G-001/009; N-014/015; P-008/014 | REQ-UX-001..003, REQ-STATE-001/002, REQ-TRACE-001 | progressive disclosure, no second truth, owner comprehension |
| R7 Rights / External Processing Admission | N-016; P-015; CH-009 | REQ-RGT-001/002, REQ-INT-001, REQ-STATE-003 | least privilege, action-specific admission, unknown preserved |
| R8 Trace / Assurance / Safe Change | G-007/008/011/012; N-017/018; P-009/010/016 | REQ-WF-001, REQ-TRACE-001, REQ-LEAN-001 | executable settled invariants, low secondary work, change safety |

These responsibilities intentionally overlap through references. They are not a new layered ontology.

### 4.1 Quality / failure scenarios

**Q1 — Source/findspot non-loss.**  
Given a consequential finding and a fresh context, when the user asks for its evidence, the system resolves the finding to the explicit excerpt/findspot and the exact inspected Instance or returns a visible unresolved/unavailable state. It must not silently substitute a different representation, provider item or regenerated text.

**Q2 — Provider change.**  
Given a known OneDrive/Zotero locator, when a file is moved, renamed, unavailable or byte-changed, internal research identity remains stable; changed bytes/version create a new/changed Instance state instead of silently rewriting prior inspection truth.

**Q3 — Restart.**  
Given repository + authorized evidence and no old chat, a fresh worker can reconstruct owner, bounded task, required evidence, method frame, unresolveds, prohibited moves and next allowed action. Excess context is not required merely because it exists.

**Q4 — Promotion safety.**  
Given an AI/method candidate, when evidence/method prerequisites are insufficient, the result can remain candidate/unresolved and cannot be represented as independently validated or evidentially established.

**Q5 — Retrieval.**  
Given a known-hit corpus/query fixture, exact search returns auditable matches with corpus snapshot, query parameters and findspots. Controlled historical expansion is explicit. Semantic retrieval cannot replace or conceal the exact baseline.

**Q6 — Human audit.**  
Given a current claim/finding, the owner sees a compact result and can progressively drill down to source, instance, findspot, method, uncertainty, alternatives, validation and history from the same canonical state.

**Q7 — External processing.**  
Given an external processing request and incomplete rights/privacy facts, the operation can be blocked as unknown/restricted while local research state remains readable and usable.

**Q8 — Control proportionality.**  
Given a formal guard, its protected loss, false-block behavior and maintenance burden can be observed. A green validator alone does not establish net workflow value.

## 5. C — F1–F14 / D4 constraint integration

| Finding(s) | Consequence for conception | What remains unresolved |
|---|---|---|
| F1 | Every material capability must trace back to user/research need and accepted Requirement, not old roadmap position | live need→outcome effectiveness |
| F2a / F3b | Do not make early research partitions into hard product modules or universal states | when a partition becomes constraining |
| F2b | Minimize manually synchronized representations; prefer generated views | net burden/benefit of each representation |
| F3a | Preserve formal boundaries only where they prevent a named scientific/operational loss | proportionality of individual boundaries |
| F4 | Specialization needs low-friction integration and explicit handoff boundaries | essential scholarly integration vs accidental coordination |
| F5a / F5c | Controls have both cost and protective value; retain controls with defined loss model and observable benefit | control-specific burden/prevention data |
| F5b | Do not design around an assumed global error→rule recursion | recurrence/counterfactual evidence |
| F6 | Separate local verification from end-to-end research/workflow utility | task/outcome measurements |
| F7 | Model identity/provenance/availability/admission/currency/fitness separately; derive operation readiness | smallest useful predicate set |
| F8 | Candidate/promoted semantics and owner wording must remain traceable; no AI-sycophancy causal assumption | local causal mechanism |
| F9 | Restart context must be task-specific and minimal enough to avoid context burden | minimum sufficient context |
| F10 | Architecture must tolerate evidence-led reframing and preserve reversible provisional states | intrinsic reframing vs avoidable framing error |
| F11 | Corrections need history and recovery evidence; correction count alone means neither health nor instability | detection/recovery data |
| F12 | AI is one possible amplifier, not assumed root cause | local comparative AI effect |
| F13a / F13b | Reduce accidental integration work without automating scholarly judgement; do not design for a “semantic compiler” role | boundary between scholarly and accidental coordination |
| F14 | Treat orchestration friction as measurable, not automatically dominant | comparative bottleneck ranking |

There is no architecture justification for one “root-cause component”.

## 6. D — Technical research questions and current evidence

### TRQ-1 — Smallest durable canonical research state

**Question:** What representation gives stable provider-independent identities, explicit uncertainty/history, safe mutation and generated views without making every research thought a schema object?

**Evidence / SOTA:**
- JSON Schema 2020-12 remains the current published JSON Schema version and is already used successfully in Histo-Orla formal assurance.
- Git already supplies versioned repository history and is the governing project memory.
- W3C PROV provides a stable provenance vocabulary, but adopting its full RDF model internally would add semantic/operational complexity not required by current Histo-Orla use.
- RO-Crate is explicitly a lightweight packaging/interchange approach for research artifacts and metadata; it is a better export/restart candidate than a reason to replace Histo-Orla’s internal research semantics.

**Disposition:**  
Use a **Git-native structured-record spine only for stable machine-relevant research state**, validated by JSON Schema, alongside narrative scholarly artifacts. Do not make SQLite, RDF/PROV or RO-Crate the canonical operational store. Map/export to standards when that yields interoperability.

**Decision class:** implement-reversible, bounded by real objects; no big-bang migration.

### TRQ-2 — Zotero / OneDrive resolution and evidence availability

**Question:** How can the system resolve bibliography and bytes while keeping Histo-Orla identity provider-independent and exposing actual availability/change?

**Evidence / SOTA:**
- Zotero’s current Local API exposes Web-API-like read access on localhost, works offline, avoids network/rate-limit dependency and can return a local attachment file URL; versions are explicitly local-instance-specific.
- Zotero itself distinguishes stored files from linked files and recommends a base directory for externally synced linked-file workflows.
- OneDrive Graph supports item-ID addressing whose ID persists across user rename/move, while path addressing changes with rename/move.
- Graph delta exposes change tracking, and driveItem content supports direct byte retrieval, but cloud permissions/authentication remain a real operational and rights surface.

**Disposition:**  
#49 should test a **read-first, local-first adapter path**:
1. resolve Zotero metadata/attachment via Local API where available;
2. resolve already synchronized local OneDrive bytes when safely available;
3. use stable OneDrive driveItem IDs / Graph metadata and delta only where local resolution is insufficient or remote freshness/change detection is required;
4. return identity, locator, availability, provider version/change metadata and bytes separately;
5. never promote Zotero key, path or driveItem ID to Histo-Orla Source/Instance identity.

**Decision class:** spike/benchmark before general integration; no cloud requirement is created.

### TRQ-3 — Findspot and document interoperability

**Question:** How can findspots remain exact across PDF/image/text/layout sources without forcing one external standard on every source?

**Evidence / SOTA:**
- W3C Web Annotation supplies a general target/selector model.
- IIIF Presentation 3.0 uses Web Annotation and Canvas semantics for page/view resources; Content State 1.0 supports deep links to a resource/region across clients.
- ALTO provides OCR text + physical layout positions; TEI facsimile/zone provides surface-relative region semantics.
- The current #51 implementation already proves that normalized neutral page-space coordinates can remain independent of the PDF library adapter.

**Disposition:**  
Keep a **minimal internal locator contract**:
- target Instance or Derivative;
- page/folio/section identity;
- locator kind;
- coordinate system/version where spatial;
- value/region;
- optional external selector/canvas reference;
- provenance/review status.

Provide adapters/mappings for Web Annotation/IIIF/ALTO/TEI only when the source/representation actually uses them. Do not replace the internal identity chain with any one standard.

**Decision class:** retain/adapt current #51 direction.

### TRQ-4 — Work Context, Method Application and Promotion

**Question:** What machine state is enough to restart consequential work and enforce settled transitions without making the owner or AI operate a workflow engine?

**Evidence / project state:**
- CurrentContext + Work Order have real-case evidence.
- paleo-type independently demonstrates value in generated restart context, sticky prerequisites and explicit distinction between source/evidence/resource state and work authority.
- Wissensarbeit demonstrates both the utility and maintenance cost of a persisted execution cursor; its current state is itself undergoing context-fidelity correction work.

**Disposition:**  
Retain **task-specific Work Orders + derived CurrentContext** for consequential/resumable work. Do not import a universal persisted execution cursor or workflow engine. A global “next action” is derived only when current owners/selection make it deterministic; otherwise no deterministic next action is valid. Method Application and Promotion references are added only as #60/#54 semantics mature.

**Decision class:** retain/adapt; minimal-context unknown remains testable.

### TRQ-5 — Exact and historical retrieval

**Question:** What is the smallest replaceable exact-search baseline for a private corpus that preserves query/corpus provenance and findspots?

**Evidence / SOTA:**
- SQLite FTS5 is an embedded full-text module with exact token/phrase, prefix and BM25-style facilities and built-in unicode61 and trigram tokenizers.
- unicode61 handles Unicode/case/diacritics; trigram can support substring matching. Porter is English-specific and therefore not an appropriate default historical-German stemmer.
- SQLite JSON functions can carry structured derived metadata, but this does not imply SQLite should own canonical research truth.

**Disposition:**  
Use **SQLite FTS5 as the leading derived-index test candidate**, not an admitted canonical store. Benchmark it against the simplest non-indexed baseline on real known-hit queries once a technical/research fixture is authorized. Historical variants are controlled query-expansion data/method, not tokenizer magic. Persist corpus snapshot/derivative refs, query and explicit expansions. Semantic/RAG remains later additive only if it beats the admitted baseline without provenance loss.

**Decision class:** TEST / benchmark.

### TRQ-6 — Audit / progressive-disclosure workplace

**Question:** How can the owner work from a compact surface without turning a summary into a second truth store?

**Evidence / project state:**
- audit.py already proves deterministic read-only derivation with visible missing/unresolved.
- Owner feedback records a real pain: current scientifically correct state is still too text/chat/manual-orchestration heavy.
- Wissensarbeit and paleo-type both independently reinforce generated current/audit views over manually synchronized summaries.

**Disposition:**  
The target includes a **derived owner-facing research view** with progressive disclosure:
- current bounded question/action;
- current findings/candidates/unresolveds;
- evidence availability;
- source/findspot drill-down;
- method/validation/history;
- retrieval/search trace where relevant.

The first surface should be the smallest useful local/read-only implementation. CLI, generated Markdown/HTML or a local UI remain candidates; no frontend framework is selected here.

**Decision class:** required capability; UI technology DEFER/TEST.

### TRQ-7 — Rights / external-processing admission

**Question:** How can external processing fail closed without making the whole source/research state unusable?

**Disposition:**  
Represent rights/admission facts separately: access, local retention/copy, computational processing, external/cloud processing, publication/sharing and privacy. “unknown” is valid. Admission is evaluated per intended operation. Credentials stay outside research state. External processing may be blocked while local source inspection and existing research state remain available.

**Decision class:** retain #50/#56 contract; later implement-reversible evaluator.

### TRQ-8 — Assurance and change safety

**Question:** Which controls should survive and which should be generated/simplified?

**Disposition:**  
Retain:
- Requirements formal QA;
- value/decision/delivery trace;
- deterministic reference/invariant tests;
- explicit mutation/transition boundary;
- fresh-context and loss fixtures.

Simplify by:
- deriving coverage/audit/status views wherever their content is mechanically available;
- avoiding prose duplication of rules already executable;
- not requiring every exploratory thought to pass a machine lifecycle;
- tracking control burden/false blocks in later owner feedback.

Do not build a new generic governance/runtime platform.

## 7. E — Candidate approaches and trade-offs

### 7.1 Canonical research-state persistence

| Candidate | Benefit | Cost / loss risk | Disposition |
|---|---|---|---|
| Keep Markdown-only canonical state | minimal change, highly readable | brittle machine resolution, repeated manual projection, weak generic referential checks | ADAPT, not sufficient alone |
| Git-native structured records + narrative artifacts with one canonical owner per fact | portable, diffable, schema-validatable, easy backup/restart, low lock-in, fits current repo | requires careful granularity and incremental migration; structured records can become bureaucratic if overused | **TARGET BASELINE** |
| SQLite as canonical research store | transactions/querying/indexing | binary diff/audit burden, stronger runtime dependency, encourages DB semantics before need; migration/backup discipline larger | REJECT NOW / revisit only on measured need |
| Graph/RDF store as canonical state | rich relations/interoperability | ontology/ops complexity, risk of forcing research categories, no current scale/use need | REJECT NOW |
| External SaaS/tool as canonical research truth | ready-made UX/search | provider lock-in, rights/availability dependence, violates provider-removal objective | REJECT |

**Granularity rule:** structured state exists only for stable, machine-relevant distinctions with a real consumer or formal invariant. Exploratory prose, interpretation and synthesis do not become fields merely for completeness.

### 7.2 Search/read model

| Candidate | Disposition | Reason |
|---|---|---|
| direct file scan / regex baseline | RETAIN as benchmark/control | zero index maintenance; sufficient at small scale for exact fixtures |
| SQLite FTS5 derived index | TEST | strong local embedded candidate with exact/prefix/trigram options and no server |
| custom search engine/service | DEFER | no measured scale/performance need |
| semantic/vector index | DEFER | REQ-RET-005 requires benchmark admission; provenance/false confidence risks remain |

### 7.3 Provider integration

| Candidate | Disposition |
|---|---|
| local Zotero API read + local synced file resolution | TEST FIRST |
| Microsoft Graph stable ID + delta/content | TEST as fallback/remote-change capability |
| direct Zotero SQLite/database access | REJECT unless API proves insufficient; bypasses supported boundary |
| provider IDs as canonical Histo-Orla IDs | REJECT |

### 7.4 Research UX

| Candidate | Disposition |
|---|---|
| generated Markdown/HTML audit/current view | RETAIN/ADAPT as lowest-cost baseline |
| local CLI with drill-down/search | TEST where owner interaction benefits |
| local web/desktop UI | DEFER until interaction pattern and real workflow value are measured |
| MCP/Skill as primary product UI | DEFER; adapter only if a concrete interface need emerges |
| chat transcript as state/UI | REJECT as canonical or restart surface |

### 7.5 Operational structure

| Candidate | Disposition |
|---|---|
| continue small capability modules in tools while they are operational/supporting | RETAIN |
| force all capability code into a new src package now | DEFER |
| complete a predefined universal Operational Core | REJECT |
| extract shared runtime only after two real consumers or one cross-cutting invariant | RETAIN as admission rule |
| generic workflow/agent platform | REJECT |

## 8. F — Pointwise disposition of old #92 / PR #119 plan

| Old element | Disposition | Current basis |
|---|---|---|
| Product / Vertical Slice as primary research unit | **ADAPT** | A bounded end-to-end slice is useful for falsification/acceptance, but must not become a hard research partition. Use real tasks as evaluation envelopes, not ontology. |
| Product-code boundary / src/histo_orla | **DEFER** | No current product package exists and current runtime responsibilities are still small. Trigger only when durable product logic has multiple real consumers or operational tooling can no longer own it cleanly. |
| Operational Core as validate/resolve/derive/context/evidence/transition target | **ADAPT** | Retain already-proven small mechanics and capability boundaries; reject the fixed target shape and universal-core destination. |
| Shared runtime reader | **TEST** | A common read/projection layer may reduce duplicated state assembly once canonical structured records exist and at least two consumers need it. |
| Restartability/context representation | **RETAIN + ADAPT** | Work Order + derived CurrentContext are real evidence; keep task-specific and test minimal sufficient context. No global execution cursor by default. |
| Heterogeneous research slice | **ADAPT** | Useful later for cross-capability falsification, not an architecture primitive or current Research Selection. |
| Read model | **TEST** | A derived read model is justified only when multiple views/searches need it and it remains rebuildable. |
| SQLite | **TEST** | Strong candidate for derived local index/read model; not canonical store. |
| FTS | **TEST** | FTS5 benchmark candidate for REQ-RET-001/002; compare against direct baseline and real known-hit queries. |
| Skill / MCP layer | **DEFER** | Interface adapter only after the research-workplace interaction need is proven; not core truth or workflow. |
| UI layer | **ADAPT / DEFER TECHNOLOGY** | Owner-facing progressive disclosure is required; implementation technology remains open. |
| #49→#51→#53→#55→#57 fixed W1 sequence | **REJECT** | Delivery must follow actual prerequisites and admitted work; existing pieces can proceed in parallel only under their own authority/admission. |
| PR #119 waves as execution authority | **REJECT** | Historical prior art only. |
| “Orchestration is dominant bottleneck” premise | **REJECT as premise / TEST as metric** | F14 mechanism exists; rank is unresolved. |
| “AI is primary cause” premise | **REJECT** | F12 remains unresolved; architecture must not depend on that causal claim. |

## 9. G — Fresh target conception

### 9.1 Logical responsibility map

The target system is a small set of cooperating capabilities around one research-state boundary:

**Domain / Research**
- research question, source reading, scholarly judgement, method truth, findings/interpretation;
- remains owned by Research/Domain authorities.

**Canonical Research State Spine**
- stable internal identities;
- explicit object relations / parentage;
- inspected-instance state;
- findspot/excerpt references;
- candidate/finding/hypothesis/uncertainty/history state where required;
- method/work/review references where consequential;
- rights/admission facts where applicable;
- provider references as attributes only.

**Provider / Evidence Adapters**
- Zotero bibliographic/attachment resolution;
- OneDrive/local byte resolution;
- future archive/IIIF/provider adapters;
- return provider metadata and availability without owning research truth.

**Derivative / Document Capabilities**
- OCR/HTR/transcription/layout processing;
- processor/version/parameter provenance;
- findspot roundtrip;
- standards adapters only where applicable.

**Retrieval**
- rebuildable exact/filter/index capability;
- controlled historical variants;
- corpus/query provenance;
- semantic retrieval only as an admitted additive layer.

**Research Transition / Context**
- task-specific Work Order;
- derived CurrentContext;
- explicit candidate/promotion/demotion/history boundary;
- deterministic guards only for settled invariants.

**Derived Audit / Workplace**
- compact current research view;
- progressive drill-down;
- search results with source/findspot;
- uncertainty/method/review/history;
- no canonical back-write except through explicit authorized mutation/transition paths.

**Assurance / Trace**
- Requirements/driver/decision/implementation/verification feedback trace;
- formal invariants and CI;
- independent of scholarly truth.

### 9.2 Canonical vs. derived boundary

**Canonical / curated when needed**
- internal IDs and stable relations;
- bibliographic/archival identity owned by Histo-Orla where curated;
- exact inspected Instance identity + byte/version/hash evidence where available;
- selected provider locators/IDs with provenance;
- Derivative parentage and consequential processing metadata;
- Findspot / Excerpt;
- Finding / Hypothesis / Uncertainty / alternatives / validation status where material;
- Method Application / Work Order / review refs where consequential;
- Rights/admission facts;
- explicit supersession/demotion/history relationships.

**Narrative canonical artifacts**
- source-critical prose;
- interpretive reasoning;
- research syntheses;
- method research / scholarly discussion where machine structure is not an accepted need.

**Derived / regenerable**
- CurrentContext;
- audit/current-state views;
- search indexes / SQLite FTS database;
- caches;
- embeddings;
- thumbnails/crops that can be rebuilt;
- generated prompts/context packages;
- coverage/status reports where mechanically derivable;
- UI presentation state.

A derived layer may cache canonical IDs/content, but it is invalidated/rebuilt when its declared source basis changes.

### 9.3 Record and schema strategy

The implementation baseline is **small JSON records validated by JSON Schema** for object types that genuinely need machine operations. This follows existing repository practice and is reversible.

Rules:

1. No universal “research object” schema containing every possible historical concept.
2. Start only from accepted stable distinctions already required: Source, Representation, Instance, Derivative, Findspot/Excerpt, Finding/Hypothesis/Research Hook as needed, Work Order/Method Application refs, review/validation refs.
3. Add fields/object types only when a Requirement + real workflow/test consumes them.
4. Rich narrative may be referenced rather than atomized.
5. One field/fact has one canonical owner. Derived Markdown/HTML/UI must be regenerated, not manually corrected as a second truth.
6. Schema versioning and migration must preserve old readable state and history.
7. Provider-specific IDs remain provider refs.
8. No requirement to store source bytes, all OCR output or indexes in Git.

This is a target baseline, not implementation authority.

### 9.4 Operation-specific readiness

Do not persist one broad “ready” state for evidence. For a concrete operation derive a readiness result from independent facts:

- identity known?
- required Instance identified?
- required bytes currently inspectable?
- basis/current version still valid?
- processing/admission allowed?
- method/review prerequisites satisfied?
- relevant derived asset current or rebuildable?
- unresolved state acceptable for this operation?

The output may be ready, blocked, unresolved or not-applicable for that operation, with reasons. The independent underlying facts remain canonical.

This preserves F7 without proliferating a universal fixed state machine.

### 9.5 Physical code topology rule

No repository reorganization is required by this conception.

Keep existing operational/support code where it is until a concrete product boundary is justified. Introduce a product package such as src/histo_orla only when at least one of these becomes true:

1. two or more durable product/runtime capabilities need shared importable code;
2. an owner-facing runtime/UI needs a stable application boundary;
3. operational-support and product semantics can no longer be kept clear in tools;
4. packaging/testing/dependency isolation materially improves reliability or replaceability.

If none applies, do not create the package.

### 9.6 Provider and AI boundary

- Provider access is capability/adaptor state, not research identity.
- Histo-Orla must remain readable/exportable if Zotero, OneDrive or an AI provider is unavailable.
- AI may generate candidates, translation, search expansion, summaries or code, but never becomes evidence, method authority, independent validation or silent mutation authority.
- Deterministic mechanisms validate settled structure. Scholarly judgement stays explicit.

## 10. Migration / no-migration strategy

There is **no big-bang migration**.

Use a strangler-style, evidence-led transition:

1. Existing research artifacts remain canonical until a specific fact/object is intentionally re-homed.
2. New/mature machine-relevant state is written in the new structured canonical home only when a real capability needs it.
3. When an existing fact is migrated, the old location becomes a pointer/narrative reference or is removed from authoritative status; do not maintain two authoritative copies.
4. Existing #51 manifests and #61 Work Orders remain valid bounded artifacts. They are not retroactively declared the universal final schema.
5. Derived audit/search/context layers learn to consume the new structured state incrementally.
6. No historical research content is rewritten merely to normalize formatting.
7. Migration of a source/finding object requires explicit before/after roundtrip and history checks.
8. If the structured representation adds more manual maintenance than it removes, the affected representation must be simplified, generated or rejected.

## 11. Explicit unknowns and discriminating tests

| Unknown | Class | Planned discriminator |
|---|---|---|
| Minimal structured record granularity | DESIGN-TESTABLE-UNKNOWN | first bounded state-spine implementation: measure duplicate facts, required manual edits, audit completeness |
| Minimal sufficient restart context | DESIGN-TESTABLE-UNKNOWN | fresh-context tests with deliberately omitted/nonessential fields |
| Smallest readiness predicate set | DESIGN-TESTABLE-UNKNOWN | operation-specific fixtures for inspect/search/external-process/resume |
| Structured-state burden vs benefit | PROJECT-EVIDENCE-GAP | compare manual sync/repair effort before and after first real consumer |
| Essential scholarly integration vs accidental coordination | PROJECT-EVIDENCE-GAP | observe which owner actions remain judgement versus mechanical routing in real use |
| Exact retrieval index choice | DESIGN-TESTABLE-UNKNOWN | known-hit benchmark: direct scan vs SQLite FTS5 configurations, with historical variants |
| Local Zotero/OneDrive resolver route | DESIGN-TESTABLE-UNKNOWN | #49 read-only feasibility against actual owner setup; local API/local bytes vs Graph fallback |
| UX surface | DESIGN-TESTABLE-UNKNOWN | owner task test with generated view/CLI before committing to app framework |
| Control proportionality | PROJECT-EVIDENCE-GAP | false-block, maintenance and recovery observations per guard |
| Bottleneck rank | PROJECT-EVIDENCE-GAP | comparative owner/time/error data; no architecture premise before measurement |
| AI end-to-end effect | PROJECT-EVIDENCE-GAP | task-specific comparison where useful; not a prerequisite for core design |
| Related-system transfer | NON-BLOCKING-UNKNOWN | generic-fit check per imported pattern; no whole-framework adoption |

No item above is a current RESEARCH-BLOCKER.

## 12. Acceptance and evaluation strategy

Later implementation must be evaluated on different evidence classes, not one PASS.

### 12.1 Deterministic / technical

- schema/reference integrity;
- provider-ID does not replace internal identity;
- byte-change detection;
- derivative parentage;
- findspot roundtrip;
- stale-basis invalidation;
- generated-view determinism;
- provider-removal/export;
- exact retrieval known-hit behavior;
- query/corpus provenance;
- rights/admission fail-closed behavior;
- no silent canonical mutation.

### 12.2 Scholarly / domain adequacy

- source/representation/instance distinctions remain meaningful in real materials;
- editorial/normalization/interpretation layers are not flattened;
- uncertainty/alternatives survive;
- Method Application and evidence demand are sufficient for the real domain;
- validation status does not overclaim.

This requires #60/domain review where applicable. CI cannot establish it.

### 12.3 Owner / workflow utility

Measure on real authorized work:

- can the owner answer “what do we know, from where, with what uncertainty?” without reconstructing chat?
- time/steps to resume a task after context loss;
- time/steps to open exact evidence from a finding/search hit;
- manual copying/reconciliation work added/removed;
- number and cost of false blocks;
- comprehension of status/uncertainty without expert-level UI micromanagement;
- whether the system supports evidence-led reframing without data repair;
- whether an abstraction has at least two real consumers or a demonstrated cross-cutting invariant.

Owner/workflow evidence remains separate from historical evidence.

## 13. Dependency-driven implementation proposal

This is a proposal only. No package below is currently authorized.

### Candidate WP1 — Canonical Research State Spine v0 + derived audit roundtrip

**Purpose:** establish the smallest durable machine-readable research-state path needed by multiple accepted Requirements without creating a database/platform.

**Scope:**
- minimal JSON Schema records for the already-settled identity/provenance roles needed by the selected technical fixtures;
- stable IDs and explicit parent/reference integrity;
- unknown/unresolved and history/supersession fields only where required;
- read-only loader/resolver;
- derive the existing audit path from canonical structured records rather than a manually assembled projection;
- reuse existing #51 / #61 technical/reference fixtures without creating a new historical Research Selection;
- no provider write, no OCR engine, no search engine, no UI framework, no broad migration.

**Acceptance:**
1. one fact/one canonical home within the bounded fixture;
2. Source→Representation→Instance→Derivative→Findspot/Excerpt→Finding roundtrip where applicable;
3. provider refs remain attributes, not internal identity;
4. missing/unresolved stays visible;
5. prior state/history survives correction;
6. generated audit is reproducible and not manually maintained;
7. fresh context can resolve the bounded state without chat;
8. deleting any derived projection does not lose curated research state;
9. no requirement or domain-method semantics are invented;
10. Project Assurance + appropriate owner/domain review pass for exactly the supported claims.

**Admission needed:** explicit #48/#59 implementation admission with #42 trace. This conception does not supply it.

### Candidate WP2 — Evidence resolver / availability slice

After WP1 proves the state boundary, test #49/#57:
- Zotero Local API metadata/attachment resolution;
- local synced bytes;
- optional Graph stable IDs/change metadata fallback;
- changed/unavailable detection;
- action-local availability;
- no provider truth ownership.

Can run partly in parallel with later WP1 refinement if the interface is stable.

### Candidate WP3 — Exact retrieval baseline

After a searchable derivative/corpus fixture is authorized:
- direct scan control;
- SQLite FTS5 candidate;
- exact/phrase/prefix plus explicit historical variants;
- findspot-preserving results;
- query/corpus provenance;
- no semantic layer until benchmark admission.

### Candidate WP4 — Derived research workplace

Build the smallest owner-facing read-only surface from the same canonical state:
- current question/action;
- findings/candidates/unresolved;
- evidence availability;
- search;
- drill-down audit;
- history/method/validation.

Use real owner acceptance before choosing a larger UI stack.

### Candidate WP5 — Promotion / method / rights operationalization

Only as #60/#54/#56 semantics are mature:
- explicit transition guards for settled formal rules;
- Method Application links;
- consequence-based validation status;
- operation-specific rights admission.

Do not build a universal state machine.

### Cross-cutting verification track

#57 restartability/provider removal and #62/#63 assurance run across packages rather than waiting for a final wave. Real owner feedback closes each meaningful increment.

### Dependency view

WP1 State Spine
→ enables reliable derived Audit/Workplace and stable object refs
→ supports WP2 provider availability mapping
→ supports WP3 corpus/query provenance
→ supports WP5 transitions only where semantics are settled

WP2 Evidence Resolver
→ enables research-ready source inspection and real document/retrieval paths

WP3 Retrieval and WP4 Workplace
→ can evolve in parallel once their data/evidence inputs are real

#60 Method Truth
→ constrains WP5 and method-sensitive acceptance, but does not block unrelated mechanical state/resolver work

#56 Rights
→ constrains external/cloud operations, not local research-state readability

#57 / #62 / #63
→ continuous assurance, restartability and feedback, not a final acceptance proxy

This is deliberately not the historical #49→#51→#53→#55→#57 W1 sequence.

## 14. ADR / owner-decision candidates

No new #44 blocker is created by this conception.

Potential later ADR/#58 triggers:

- making a database the canonical research store;
- adopting an external/cloud service as required infrastructure;
- irreversible broad migration of existing canonical research artifacts;
- a product package/runtime boundary with significant dependency/packaging consequences;
- a UI architecture with persistent local/server state;
- a standard/profile that changes Histo-Orla semantics rather than merely mapping them.

Potential #44 triggers remain only normative/rights/scope choices that cannot be resolved by evidence or bounded reversible tests.

The existing DD-20260903-001 GitHub branch-protection admission gap remains separate.

## 15. Non-goals / forbidden assumptions

This conception does not:

- select a historical case;
- authorize implementation;
- define Domain Method Truth;
- replace accepted Requirements;
- create a universal ontology;
- require a database;
- require SQLite as canonical state;
- require an MCP, Skill, agent framework or workflow engine;
- require src/histo_orla now;
- claim orchestration is the dominant bottleneck;
- claim AI is the root cause;
- treat fewer controls as inherently better;
- treat formalization as inherently harmful;
- treat CI as scholarly or owner acceptance;
- treat Related Systems as Histo-Orla authority;
- re-activate PR #119 or R4–R8.

## 16. Conception completion and handoff

### Established

- The actual repository has useful small technical capabilities but no general historical-research runtime/workplace.
- The stable target is responsibility-first and provider-independent.
- Canonical state should remain Git-native; structured records are admitted only for stable machine-relevant facts with real consumers.
- Derived views/indexes are rebuildable and may use fit-for-purpose local technologies.
- External standards/tools are adapters/interchange candidates, not semantic authority.
- Old #92/PR #119 elements have been pointwise dispositioned.
- A bounded first implementation candidate is defined.

### Still unresolved by design

- exact record granularity;
- exact physical package layout;
- exact local provider-resolution route in the owner environment;
- exact retrieval index configuration;
- exact owner-facing UI technology;
- readiness predicate minimum;
- control burden/benefit;
- bottleneck rank and AI causal contribution.

These unknowns have explicit discriminators and do not require speculative architecture.

### Next allowed phase after this conception is integrated

**Implementation Admission / bounded execution planning for Candidate WP1 under #48/#59, traced to #42, while retaining selection-open and no automatic Research Case Selection.**

The proposed first package is:

**Canonical Research State Spine v0 + derived audit roundtrip**

It is a proposal, not current implementation authority. Before code/migration, #48/#59 must admit the bounded scope and create the current implementation trace required by #63.

After this artifact is integrated, the Fresh Rebuild Conception is COMPLETE and the conception work context stops. Implementation must begin only in a separately admitted work context.
