# Histo-Orla – Cross-Repository Development Prior Art

**Status:** active technical prior-art input / not a Requirement Truth / not an Architecture Decision  
**Owner:** #48 Technical Lead  
**Target project:** Histo-Orla  
**Current prior art:** `esany/paleo-type`, `esany/Wissensarbeit`  
**Precedence:** Histo-Orla Governance + accepted Requirements + Domain Method Truth always override prior art.

## 1. Purpose

Future Histo-Orla development should not rediscover already-demonstrated engineering lessons from the owner's related projects. At the same time, another repository must never silently become Histo-Orla's semantic or architectural authority.

Use cross-repository material as:

- prior art;
- failure/fixture evidence;
- architecture and RSE challenge input;
- candidate reusable patterns;
- SOTA/Best-Practice starting points.

Do **not** copy domain models, workflows, requirements, storage structures or technology choices unless Histo-Orla requirements and real use justify them.

## 2. `paleo-type` – primary transferable lessons

`paleo-type` is strongest as prior art for scholarly research-state integrity and model-independent scientific work.

Relevant patterns:

1. **Governing semantics precede implementation.** Scientific purpose and epistemic invariants outrank data model, AI tooling and workflow convenience.
2. **Evidence before plausibility.** Observation/reading/normalization/identification/interpretation and archival/textual/historical truth domains must not silently rewrite each other.
3. **Canonical state vs derived views.** One canonical owner; generated views remain rebuildable.
4. **Executable settled invariants.** Stable referential/provenance rules belong in machine-readable contracts + validators/resolvers/tests rather than repeated prompt prose.
5. **Canonical mutation is distinct from new judgement.** A different AI/researcher judgement may create a candidate/challenge/alternative but is not itself mutation authority. Consequential replacement must preserve predecessor, basis/reason, evidence/re-evaluation and proportional responsibility/review provenance.
6. **Work context is generated from canonical state.** Stable role/authority, current executable stage, required evidence, stop/handoff and downstream not-yet-authorized work should be composable rather than maintained as master prompts.
7. **Evidence identity is not evidence availability.** A known Source/File/URN/hash does not imply the current context can actually inspect the evidence required by the next action.
8. **Real fixtures before generic schema.** Formalize only distinctions demonstrated by real research-state failures or recurring work.
9. **Technical subsidiarity.** Tooling exists for research outcomes, not vice versa.
10. **Human authority is not specialist validity.** Owner admission/purpose and independent disciplinary validation remain distinct.

Histo-Orla adaptation:

- source/manuscript-specific `paleo-type` structures are **not** copied;
- the generic pattern informs #50/#54/#55/#57/#61 and the Operational Execution Architecture;
- Source/Representation/Instance/Derivative/Findspot/Finding semantics remain Histo-Orla-owned.

## 3. `Wissensarbeit` – primary transferable lessons

`Wissensarbeit` is strongest as prior art for generic project operation, competency routing, systemic integration and lean technical decision-making.

### 3.1 Human-in-the-loop, not human-as-workflow-engine

Routine project mechanics, context compilation, validation, derived views and operational maintenance should be automated where reliable. The owner is consulted for material meaning, purpose, priority, risk acceptance, quality change and hard-to-reverse consequences.

### 3.2 Systemic integration before append

A new material aspect should be assessed against objective, current state, requirements and decisions and dispositioned explicitly as:

`fuse | refine | reframe | supersede | conflict | reject | defer`

For Histo-Orla this is a **review vocabulary**, not a new lifecycle requirement. It is useful whenever new research, technology or prior art would otherwise simply be appended as another layer.

### 3.3 Building blocks are capabilities

Useful generic capabilities include:

- Canonical State;
- Context Compiler;
- Competence Discovery;
- SOTA/Fit Research;
- Systemic Integration;
- Requirements/Criteria;
- Concept/Architecture;
- Implementation;
- Assurance;
- Trace/Explain;
- Derived Views;
- Operations/DevOps;
- Use/Learn.

These are **capabilities, not mandatory folders, agents, services or separate workstreams**. Histo-Orla instantiates only what current requirements/use need.

### 3.4 Explicit rule/authority classes

Useful control classes:

- `deterministic` → software/CI can enforce settled structure;
- `procedural` → process/handoff/consultation structure can be required while content remains judgement;
- `judgement` → AI + human/domain/specialist evaluation, never disguised as deterministic PASS.

This aligns with #62/#63 and should be reused rather than inventing parallel taxonomies.

### 3.5 Competence and interface competence

Material changes should consider not only domain or software expertise but interface competencies such as:

- domain → data;
- domain → software;
- research → product;
- AI → domain;
- method → software;
- project → engineering.

This is directly relevant to Histo-Orla's #24/#48 responsibility model.

### 3.6 Architecture fitness before technology selection

For a material technical choice, inspect only relevant concerns such as data, backend, ML/data science, AI/LLM, infrastructure/DevOps, security/privacy.

Preferred decision order from least to most custom burden:

`avoid → reuse → configure → integrate → thin custom layer → build custom`

Adopt this as a **decision heuristic under #48**, subordinate to Histo-Orla requirements and scientific loss constraints.

### 3.7 Derived current state

Where a human-readable current-state/audit/coverage view is deterministically derivable, generate it from canonical sources rather than maintain it as parallel truth.

### 3.8 Real-pilot closure learnings from Histo-Orla (2026-09-02)

`Wissensarbeit` used Histo-Orla as a real pilot and then closed that pilot without importing case semantics into its generic core. The generic closure retained six executable regression lessons and returned project-specific content to Histo-Orla as #65 (`external pilot review input / candidate / no implementation authority`).

Transferable engineering lessons:

1. **Conversation harvesting:** no material project state may remain only in conversation; closure requires a canonical reference.
2. **Context fidelity:** context compression/compilation can introduce semantic drift and must be checked against lossless references for material assertions and unresolved states.
3. **Lossless-by-reference before token efficiency:** shorter context is only an optimization after reference coverage/fidelity are preserved.
4. **Elicitation before promotion:** co-created proposals and AI suggestions remain candidates until the authorized Requirement/Decision lifecycle promotes them.
5. **Generic-Fit before core change:** a successful case/pilot is evidence, not automatic authority to change generic framework/core semantics; first try to sharpen an existing mechanism.
6. **Case isolation / anti-overfitting:** project-specific identities, findings and research questions stay in the case repository; the generic system retains only dispositioned generic learning, provenance and regressions.

Histo-Orla consequences:

- these lessons strengthen #61 Context/Handoff, #62/#63 Assurance and the planned Operational Core;
- `context`/`derive` mechanisms should eventually be testable for semantic/reference fidelity, not only structural validity;
- #65 must be dispositioned by the proper Histo-Orla authorities before any Requirement/Method/Architecture promotion;
- no new Histo-Orla building block, framework, graph model or data architecture follows automatically from the pilot.

## 4. Combined prior-art lens for Histo-Orla

The two repositories complement each other:

```text
paleo-type
    scholarly evidence / source-state integrity
    canonical mutation / transition safety
    research-context and evidence-access discipline
                +
Wissensarbeit
    systemic project integration
    competence/authority routing
    lean architecture fitness
    generic operational-core pattern
                ↓
Histo-Orla
    own Goals / Needs / Pains
    own accepted Requirements
    own Domain Method Truth
    own source/research semantics
    own real-use feedback
```

Neither repository is a template to copy wholesale.

## 5. Mandatory challenge questions for future material development decisions

For each material #48/#59 decision, proportionally answer or make reconstructable:

1. **Value:** Which Histo-Orla Goal/Need/Pain and accepted Requirement justify this work?
2. **Integration:** Does the new input `fuse`, `refine`, `reframe`, `supersede`, `conflict`, `reject` or `defer` relative to current state? Avoid append-only architecture.
3. **Competence:** Which domain, method, data, software, AI, operations and especially interface competencies are actually required? Which remain uncovered?
4. **SOTA/Fit:** What current standard/best practice/existing tool is relevant, and under which assumptions does it fit or not fit Histo-Orla?
5. **Architecture fitness:** Can the need be avoided, reused, configured, integrated or solved by a thin layer before custom build?
6. **Enforcement class:** Which parts are deterministic, procedural or judgement-based? Do not encode scholarly judgement as software.
7. **Canonical ownership:** What is canonical input/state? What is merely derived/rebuildable? No second truth store.
8. **Mutation authority:** Could this mechanism silently replace accepted research state? If yes, require an explicit transition preserving predecessor/history and appropriate evidence/review.
9. **AI/model independence:** Is correctness resting on prompt/model memory where code/resolution/generation could reliably carry it instead?
10. **Evidence availability:** If work is evidence-dependent, is required evidence actually accessible/inspectable now, not merely identified?
11. **Verification:** Which deterministic tests, domain adequacy review, specialist validation and/or owner workflow acceptance are required, and which are explicitly *not* interchangeable?
12. **Operations burden:** What maintenance, dependency, security/privacy, backup/recovery, observability or cost burden is introduced? Is it proportionate?
13. **Use/Learn:** What real-use feedback could falsify the decision, and how does that return to #42/#48/#60?
14. **Context fidelity:** If context is compressed/generated, which material refs/assertions/unresolved states prove that no semantic loss was introduced?
15. **Generic Fit / case isolation:** Is this really a reusable Histo-Orla mechanism, or merely evidence/need from one case that should remain case-owned until repeated or explicitly promoted?

These questions are a decision-quality lens, not a form that must be filled for every trivial change.

## 6. Relationship to existing Histo-Orla Operational Execution Architecture

Canonical Histo-Orla integration artifact:

`docs/architecture/operational-execution-architecture.md`

This prior-art note strengthens its direction:

- global Requirement→Enforcement mapping;
- one small operational/RSE core instead of accumulating scripts;
- generated context/handoff/audit views;
- evidence availability/resolution capability;
- explicit canonical-state transition controls;
- thin Skills/CLI/CI as replaceable adapters;
- context/derived-view fidelity checks for material references and unresolved state;
- Generic-Fit/case-isolation checks before promoting case observations into reusable operational mechanisms.

No framework, database, agent runtime, workflow engine or new service is admitted by this document.

## 7. Revisit rule

Because both source repositories are evolving, future material architecture decisions may re-read their **current** canonical state when they are directly relevant. Do not rely on this snapshot as proof that those repositories have not changed.

## 8. Applied integration review – 2026-09-02

For the Requirement→Enforcement/Operational-Core increment, the current GitHub state of both prior-art repositories was re-read. Disposition:

- **fuse/adapt:** canonical-vs-derived, executable settled invariants, model-independent mechanics and explicit review/mutation boundaries;
- **fuse/adapt:** capability-oriented core, `deterministic | procedural | judgement` separation and thin command/CI adapters;
- **reject now:** copying `paleo-type` METHOD/CORPUS/PROJECT semantics or `Wissensarbeit` as a universal project framework;
- **defer:** unified broad CLI, context/evidence/transition implementations and packaging until a concrete Histo-Orla capability needs them.

Histo-Orla's accepted Requirements, Governance, Domain Method Truth and current #48/#59 constraints controlled the resulting schema and code. The prior art supplied challenge criteria, not semantic authority.
