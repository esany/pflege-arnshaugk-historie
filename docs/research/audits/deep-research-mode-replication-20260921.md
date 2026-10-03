# Deep-Research mode replication — socio-technical project analysis

**Repository:** esany/pflege-arnshaugk-historie  
**Date:** 2026-09-21  
**Work Owner:** #121  
**Experiment context:** #123 / generic-system-problem-analysis-prompt-v1-20260921  
**Status:** deep-research expansion / contamination-declared replication / research evidence only  
**Authority:** no Requirement, Method Truth, Research Selection, Architecture Decision, implementation authorization, roadmap or priority change

## A. Untersuchungsrahmen

### A.1 Scope

This report executes the user-supplied generic system-analysis prompt as a socio-technical, epistemic and organizational investigation of Histo-Orla. It asks how owner needs, scholarly method, requirements, software, AI, governance and project organization interact; which failure/recovery patterns are evidenced; and how those observations compare with research, standards and real systems.

It does not select a solution, architecture, tool, roadmap, priority, refactor, agent topology or new Requirement.

### A.2 Fresh repository basis

Freshly read before substantive analysis:

- AGENTS.md
- PROJECT_STATE.md
- README.md
- Work Owner #121
- Research Protocol #45
- docs/research/source-identity-protocol.md
- primary/timely discovery and requirements artifacts, including docs/research/discovery/problem-baseline.md, docs/research/discovery/workflows.md, docs/research/synthesis/requirements-baseline.md, docs/research/synthesis/requirements-extensions.md and docs/development/requirements-coverage.md
- selected early/current issues, implementation PRs and live research artifacts
- live U2 evidence around Knau/Orlagau and the Lampe vertical slice
- current executable tooling surface under tools/requirements, tools/assurance, tools/operational and tools/document_evidence

### A.3 Experimental validity and contamination

This invocation was intended to test the unchanged v1 prompt in dedicated Deep Research mode, separate from the later v2 prompt experiment. The present run cannot be classified as a clean blind replication.

Before the #121 experimental blocklist had been located, a broad issue search accidentally surfaced diagnostic content from #64. Later in the run, #121 comments necessarily exposed the existence and summary of the earlier frozen blind run, its reconciliation and the depth assessment on #123. Those channels are declared rather than hidden.

To reduce assimilation after that point, the mechanism reconstruction below was grounded in primary/timely project evidence already inspected independently and then challenged through external research. The report therefore has value as a deep external challenge and replication-with-contamination, but not as an uncontaminated mode-effect experiment.

This report does not replace the frozen blind analysis on PR #122 or the experiment-provenance register on PR #123.

### A.4 Evidence classes

- **Project Evidence (PE):** repository artifact, issue, commit, code, test, CI, documented behavior.
- **Owner Evidence (OE):** documented Research Owner need, pain, correction, acceptance/non-acceptance.
- **External Research Evidence (ER):** scholarly literature, standards, empirical study.
- **Related-System Evidence (RS):** documented behavior/design of real systems/infrastructures.
- **Researcher Inference (RI):** interpretation derived from evidence.
- **Open Hypothesis (OH):** plausible but not sufficiently discriminated.

Confidence vocabulary: strongly supported, supported, plausible, weakly supported, contested, unresolved, falsified, insufficient evidence.

### A.5 Search boundaries and limits

The repository case is unusually young, AI-intensive and highly instrumented. Its documentation exposes errors and reversals that less instrumented projects may hide; raw count of issues, commits or files is therefore not evidence of dysfunction. Some owner evidence exists only after normalization into repository artifacts. The external review is broad but not a systematic review with preregistered databases and exhaustive screening. Transfer from healthcare safety, organizational sociology, general software engineering and scientific workflow infrastructure is mechanism-level, not direct domain equivalence.

## B. Projekt-/Fallrekonstruktion

### B.1 Reconstructed intent and owner need

The strongest early project intent is operational rather than technological. The owner wants rigorous transdisciplinary historical research without having to know in advance the correct specialist vocabulary, responsible discipline, retrieval technique, archival method or implementation choice. At the same time, the system must preserve uncertainty, source identity, exact findspots, challengeability and durable state.

PE/OE support is visible early in Issue #1, the problem baseline and workflow discovery. The core pains include unknown terminology, inability to determine which discipline should lead, scattered sources, lost findspots, repetitive mechanical work, chat-state loss, provider lock-in and difficulty understanding specialist state. The accepted need is therefore not merely "more research rigor"; it is rigor with selective absorption of avoidable operational and translation complexity.

**RI — strongly supported:** the target experience is asymmetric. The system is expected to absorb mechanical, coordination and translation burden where that can be done safely, while irreducible scholarly judgment and consequential strategic decisions remain visible to the owner.

### B.2 Early correction: plausible tools were mistaken for requirements

Issue #11 documents a fast and productive correction. Early assumptions had treated Zotero as source of truth, script-first/local-first/SQLite/FTS choices as if they were requirements, OCR-in-Git as too specific, semantic search as assumed, and transdisciplinary methods as prematurely fixed. These were demoted to hypotheses.

**Observed mechanism:** owner/problem language or a promising tool can jump directly into durable technical structure.

**Recovery mechanism:** explicit Goal/Need/Pain → Research → Capability → Requirement separation, plus architecture gates and later deterministic requirement assurance.

**Confidence:** strongly supported historically; weakly supported as a current uncorrected dominant pattern.

### B.3 Discovery and requirements: broad semantic maturity arrived quickly

The project created an explicit chain from problem/needs through workflows, research questions, SOTA, risks, capability/quality synthesis and requirements. This produced 39 baseline requirements plus 14 later extensions with traceability.

That is a positive control against requirements laundering. Yet workflow discovery itself explicitly records missing real-use observations and some inferred rather than observed flows. Live research continued to discover method constraints after formal requirements maturity.

**RI — supported:** representational closure became stronger faster than situated-work certainty. This does not falsify the requirements; it means traceability can be internally correct while the upstream observation base remains incomplete.

### B.4 Live U2 research as a counterexample to "meta-work only"

The U2 Knau/Orlagau research artifacts contain substantive source criticism: homonymous places are not merged on string similarity; editorial additions are separated from historical wording; negative findings carry search boundaries; 1374/1378 remains unresolved rather than harmonized; charter/legal sequences are reconstructed from multiple documents; current archive-signature uncertainty is preserved.

The Lampe Nr. 420 vertical slice further showed a real gap: a finding could exist while the concrete digital edition instance and findspot-capable excerpt were not yet captured. The later source-ledger/excerpt work closed that gap.

**RI — strongly supported:** formalization sometimes directly protects scholarly meaning. Source/Representation/Instance/Derivative/Findspot separation is not well described as bureaucracy or architecture astronautics; in this case it encodes non-equivalence boundaries whose loss would create false evidence claims.

### B.5 Assurance expansion and the formal-value gap

Requirements assurance, value/decision/delivery assurance, work-context derivation and mutation guards arose after real semantic drift, stale-state and mutation failures. They encode decidable boundaries while repeatedly stating that CI PASS is not scholarly validation or owner acceptance.

At the same time, docs/development/requirements-coverage.md shows a pronounced implementation asymmetry: many direct research capabilities remain NOT STARTED while assurance/operational safeguards have executable support. Exact search, historical variants, bounded-negative retrieval, additive semantic retrieval, most entity/relation/spatial/action/synthesis/UX functions and durable state remain incomplete or absent.

**RI — strongly supported:** formal/semantic project maturity and owner-facing research capability can diverge. The project itself recognizes this; the finding is not that governance "failed", but that assurance success cannot serve as a proxy for use-value.

### B.6 Process layers can become objects of work

A historical natural experiment is the rapid introduction and removal of an MVP steering layer. It was introduced to make delivery leaner and then removed because it overlaid an already rich requirement state and created semantic drift/reconciliation work.

Later operational mechanisms similarly needed their own schemas, tests, enforcement maps, work orders and owner/status semantics.

**RI — supported:** the project exhibits a representation ratchet: a new control artifact solves a local ambiguity but then becomes a new object whose own state, consistency and handoff must be maintained.

**Counterevidence:** several such layers were removed or narrowed quickly. Governance is not merely accumulating monotonically; the project has active pruning and falsification.

## C. Problem-/Mechanismenkarte

### M1 — Premature structuralization of owner language

**Observed phenomenon:** mental models, metaphors or examples can be promoted into durable project objects faster than their epistemic status warrants.

**Evidence:** early solution assumptions; later explicit owner-input classification rules; documented correction around "historical knowledge space".

**Possible mechanism:** language produced in collaborative sensemaking is treated as a specification rather than as a provisional representation.

**Alternative explanation:** rapid externalization is useful because it makes assumptions inspectable and reversible.

**Amplifiers:** AI fluency, repository persistence, traceability machinery, desire to make ambiguity actionable.

**Counteracting factors:** explicit classification of Observation/Goal/Need/Pain/Mental Model/etc.; owner review; one-fact-one-home; reversions.

**Confidence:** supported.

### M2 — Governance/assurance accretion

**Observed phenomenon:** semantic drift or tool failures lead to new guards, registries, contracts and status rules; these reduce some risks while creating coordination/maintenance surfaces.

**Evidence:** #62/#63 assurance, operational context/mutation tooling, work orders, branch/mutation incidents.

**Alternative explanation:** the added surfaces are proportionate because AI-mediated work has unusually high restartability and authority risks.

**When problematic:** when control maintenance consumes the scarce integration attention it was meant to protect, or when controls are evaluated by their own PASS state rather than owner-facing outcome.

**When useful:** when they encode stable, decidable invariants that prevent silent authority/evidence mutation.

**Confidence:** strongly supported as dual-effect mechanism; unresolved whether cumulative level is excessive.

### M3 — Formal correctness without owner utility

**Observed phenomenon:** requirements can be traceable and assurance can pass while the lived research loop remains manually orchestrated.

**Evidence:** requirements coverage versus executable research capability; owner feedback in assurance records; live research dependence on curated Markdown and chat-guided integration.

**Alternative explanation:** this is normal sequencing in an early project: infrastructure first, product loop later.

**Counteracting factors:** live pilots, vertical slices, owner acceptance distinct from CI.

**Confidence:** strongly supported phenomenon; causal interpretation remains partly unresolved.

### M4 — Human as workflow engine

**Observed phenomenon:** the owner repeatedly supplies cross-cutting integration, clarifies what should be selected, distinguishes mental model from requirement, corrects over-abstraction and steers return to real research.

**Mechanism hypothesis:** the system transfers ambiguity upward because its internal boundaries are safer when explicit, but the owner then carries the integration burden across those boundaries.

**Counterevidence:** project artifacts explicitly try to remove this burden; deterministic tooling already absorbs some mechanics; domain research cases show meaningful autonomous synthesis.

**Confidence:** supported but not total. "Owner is the workflow engine" would overstate the evidence.

### M5 — State fragmentation versus semantic separation

**Observed phenomenon:** bibliographic state, bytes, research state, source identity, derivatives and findings are deliberately separated.

**Positive mechanism:** avoids false identity, hidden transformations, stale evidence and lock-in.

**Negative mechanism:** creates resolver/adapter/restart complexity and more cross-object dependencies.

**Confidence:** strongly supported tension; neither pole is reducible to the other.

### M6 — Test-passing as proxy risk

**Observed phenomenon:** the project has extensive deterministic tests for requirements/governance/operations, while many direct capabilities are immature.

**Evidence:** code/tooling topology and coverage matrix.

**Counterevidence:** project governance repeatedly states CI PASS ≠ scholarly validation/product acceptance.

**External challenge:** current AI benchmark audits show how strict, underspecified or low-coverage tests can mismeasure capability; this does not prove Histo-Orla tests are flawed, but it strengthens the general distinction between measured invariant conformance and end-to-end value.

**Confidence:** proxy risk supported; actual specification gaming within Histo-Orla insufficiently evidenced.

### M7 — AI overreach and AI under-utilization coexist

**Overreach evidence:** premature promotion/interpretation risks; owner corrections; strict authority boundaries against AI creating evidence or canonical truth.

**Under-utilization evidence:** many repetitive research functions remain manual despite explicit needs to automate search, context, provenance and restartability.

**External evidence:** AI-development productivity studies conflict by population/task/tool generation: METR found a 19% slowdown for experienced maintainers in early-2025 mature repositories; three enterprise RCTs found ~26% more completed tasks; a 2026 quasi-experiment reported gains concentrated differently by experience; large-scale observational work finds gains attenuate from coding activity to releases. There is no defensible single "AI speeds development" coefficient for this case.

**Confidence:** coexistence strongly supported; AI-specific causality for project structural complexity only plausible.

### M8 — Recovery capacity is a first-class system property

**Observed phenomenon:** premature architecture was corrected; MVP overlay was removed; source ambiguity remains unresolved rather than normalized; benchmark-like/assurance proxies are explicitly bounded; owner feedback becomes durable evidence.

**External fit:** system-oriented safety/error literature treats latent conditions, near misses and recovery mechanisms as central rather than reducing error to individual blame.

**Confidence:** strongly supported positive pattern.

## D. Need → System Translation Audit

| Owner signal / need | System translation | Fit | Evidence / qualification |
|---|---|---|---|
| "I do not know the right specialist term/discipline" | domain routing, vocabulary discovery, methods research, explicit domain fit | strong fit | directly reflected in early needs and #45 |
| "I want to research, not operate the project" | automation, work contexts, restartability, governance | partial fit | intent strong; lived workflow still needs owner integration |
| "I need exact evidence and why" | source identity, findspots, excerpts, provenance, uncertainty | strong fit | live U2 provides positive empirical counterexample |
| "Do not make me choose technical options I cannot evaluate" | accepted requirement authority + architecture gate + owner constraints | conditional fit | prevents technology laundering, but can return unresolved technical coordination to owner |
| "Keep uncertainty visible" | explicit unresolved statuses, falsification hooks, bounded negative findings | strong fit | consistently evidenced in research artifacts |
| owner metaphor / mental model | sometimes promoted to durable structure | misfit when literalized | documented correction; later classification guard |
| repeated mechanical source work | deterministic/AI-assisted capability requirements | weak-to-partial current fit | many are accepted but not yet implemented |
| restartability | GitHub canonical state, work owner, work context, provenance tooling | partial fit | improved, but state remains distributed across systems/artifacts |

Central translation finding: **Nonwissen is usually recognized as a system requirement at the conceptual level, but not always absorbed at the operational level.** The project understands that the owner should not need disciplinary/technical foresight, yet current execution still sometimes converts unresolved integration into owner steering work.

## E. Fachdomänenanalyse

The historical-research complexity is genuinely essential in several dimensions:

- source, edition, representation, concrete digital instance and derivative are not equivalent;
- editorial identification can differ from historical wording;
- homonyms/variants require time, place, network and provenance, not string equality;
- negative search results have meaning only inside documented corpus/search boundaries;
- historical claims, archaeological indications, place-name evidence and later historiography have different evidential force;
- unresolved contradictions are valid outputs;
- multiple disciplines can be relevant without any one discipline having universal authority.

These are not software-created complications. The source-identity protocol and U2 findings show that collapsing them would damage scholarly validity.

However, essential domain complexity does not imply that the user must manually carry every representation, file, lookup, handoff or consistency relation. The distinction between scholarly judgment and mechanical/coordination burden remains analytically necessary.

## F. Technologische Analyse

### F.1 Current executable emphasis

The persistent executable surface is concentrated in:

- requirements validation/assurance;
- broader assurance and trace invariants;
- operational context/enforcement/mutation safety;
- a bounded document-evidence roundtrip.

Direct end-user research capabilities are less mature than the control plane. This is an implementation distribution, not proof of architectural failure.

### F.2 Coupling profile

The project couples GitHub work owners, Markdown/JSON canonical artifacts, external bibliographic/file providers, AI-mediated work and deterministic validators. This provides inspectability and restartability but raises the number of cross-system identity and state transitions.

### F.3 Technical debt and proxy caution

Technical-debt research shows that tools disagree substantially on what counts as problematic debt; code metrics should not be treated as an objective debt oracle. For Histo-Orla, "many artifacts" or "many checks" cannot by themselves establish accidental complexity. The stronger evidence is behavioral: rework, duplicate interpretation layers, owner integration load, stale/overwritten state, and end-to-end capability gaps.

### F.4 Essential versus accidental complexity

**Essential domain complexity:** provenance, source identity, uncertainty, multidisciplinary evidence rules.

**Accidental technical complexity:** connector/mutation peculiarities, duplicated or temporary steering layers, tool-environment limitations.

**Organizational complexity:** work-owner boundaries, reviews, authority routing, handoff discipline.

**Interface complexity:** translating owner intent to method/Requirement and cross-system source/state identity.

**Governance complexity:** maintaining invariants, gates, trace registries and status semantics.

**Complexity transferred to user:** manual integration and correction when system boundaries do not recompose into an owner-facing research flow.

The borders are not static. A control can convert accidental error into manageable explicit state while simultaneously adding organizational/interface cost.

## G. Organisations-/Governance-Analyse

The repository treats issues as Work Owners and versioned artifacts as durable truth. This is a strong response to chat/agent context loss. It also creates a topology of owners, gates and handoffs that must be navigated.

Boundary-object research is useful here: shared artifacts can coordinate communities with different local knowledge without making their meanings identical. Histo-Orla's requirements, source ledgers, work contexts and research protocols behave like boundary objects. The literature also warns indirectly that boundary objects do not abolish translation work; they organize it. The project therefore faces a dual effect: artifacts reduce ambiguity at boundaries but can create additional articulation work if every distinction becomes a separate coordination boundary.

Audit/control sociology offers another relevant mechanism: monitoring systems can acquire operational life and shape the activity being monitored. Michael Power explicitly later qualified the broad "audit explosion" thesis as needing more empirical support. That caution matters here: one should not infer dysfunction merely because assurance grew. The case-specific question is whether assurance tracks and protects owner value or begins to substitute for it.

## H. Interface Analysis

### Human ↔ AI

Strong safety boundary: AI output is not evidence and does not own scholarly truth. Human-AI research supports correction, uncertainty handling, explanations, global controls and cautious adaptation. Fit is strong at the principle level. Current friction lies less in insufficient human authority than in how much orchestration the human must still perform.

### User ↔ expert method

The project explicitly routes vague owner questions into specialist domains/methods. Fit is strong conceptually. Risk appears when clarification becomes a demand that the owner supply specialist distinctions rather than a system responsibility.

### Domain ↔ software

The strongest examples are loss-boundary formalizations: source identity, findspots, derivatives and unresolved state. These encode methodological constraints without claiming historical truth. Fit strong.

### Requirement ↔ implementation

Traceability is strong; realized capability is uneven. Fit between accepted requirement state and implementation status is transparent, but owner-facing usefulness is still incomplete.

### Evidence ↔ state

This is among the strongest project areas. Evidence classes, source identity, search boundaries and AI non-authority are explicit and empirically exercised.

### Component ↔ system

Local components can pass while end-to-end research remains manually integrated. This is the clearest current system-level tension.

### Research ↔ development

Live pilots have corrected development assumptions and exposed missing evidence/state behavior. Positive feedback loop exists. But a large volume of meta/assurance work can delay exposure to real-use discriminating evidence.

### Development ↔ feedback

Owner feedback is versioned and often consequential. That is a recovery strength. The burden is that the owner is also frequently the sensor that detects system-level semantic drift.

## I. External State of the Art

### I.1 Requirements Engineering

ISO/IEC/IEEE 29148 defines a Requirement as an expression translating a need plus constraints/conditions and treats Requirements Engineering as an interdisciplinary mediation function. It distinguishes stakeholder needs/requirements from system requirements and formalizes traceability.

**Project fit:** strong for the explicit Need → Requirement separation and traceability.  
**Transfer limit:** the standard does not determine how much discovery is enough before formalization in exploratory historical research.

Nuseibeh/Easterbrook's classic RE roadmap emphasizes elicitation, analysis/modeling, communication, agreement and evolution rather than a one-shot specification event.

**Project implication as observation:** requirement maturity does not end discovery; real-use findings can legitimately revise upstream understanding without meaning the earlier requirements process was irrational.

### I.2 HCI, sensemaking and distributed cognition

Distributed cognition treats people, representations and technologies as one cognitive system. This supports evaluating the entire owner–AI–repository–source environment, not isolated interface screens.

Human-AI guidelines by Amershi et al. emphasize efficient correction, scoping when uncertain, explanations, feedback and control. Histo-Orla aligns strongly on correction/challengeability, while current owner orchestration load remains an empirical UX issue.

Sensemaking theory treats representations as part of the work: actors search for representations and encode information into them because different representations change the cost of subsequent operations. This helps explain why project formalizations can be both valuable and dangerous: a representation can reduce later work if it matches the task, or create encoding/reconciliation work if it partitions the problem poorly.

### I.3 Organization, coordination and boundary work

Star/Griesemer show that cooperation across heterogeneous social worlds can be enabled by standardized methods and boundary objects that are locally adaptable but retain a common identity. Carlile adds that knowledge boundaries can require transfer, translation and transformation, especially when knowledge is localized and invested.

**Fit:** strong for Histo-Orla's cross-domain artifacts.  
**Limit:** these theories do not imply "more artifacts is better"; boundary objects work because they support actual coordination, not because they exist.

Software/system coordination studies of boundary objects similarly distinguish artifacts shared across boundaries from locally relevant artifacts. This is relevant to the project's tendency to canonicalize many distinctions: not every local work object necessarily requires a cross-project coordination role.

### I.4 Error culture and high reliability

Reason's system approach distinguishes active errors from latent organizational conditions and argues against explaining failure only through individual fault. Histo-Orla's stated error culture is highly compatible: source false merges, semantic drift, mutation failures and near misses are treated as evidence for system correction.

High-reliability literature emphasizes preoccupation with failure, reluctance to simplify, sensitivity to operations and resilience. That maps well to unresolved states and falsification hooks, but the transfer is limited because historical research software is not a high-hazard operational domain.

### I.5 Audit/control systems

Power's Audit Society and later "Second Thoughts" identify a risk that monitoring/control practices develop their own operational logic, while also acknowledging that the breadth and generality of the thesis require empirical support.

**Fit:** conditional. The project shows assurance generating its own engineering and notification problems, but it also shows concrete prevention/recovery value. Evidence supports a control-cost tension, not a general claim that governance is excessive.

### I.6 Provenance, reproducibility and research objects

W3C PROV models entities, activities and agents involved in production and is designed for provenance interchange. FAIR emphasizes findability, accessibility, interoperability and reusability for both humans and machines, and explicitly says good data management is a means to discovery/reuse rather than an end in itself. RO-Crate 1.3 packages research data plus contextual/provenance metadata in JSON-LD.

**Fit:** strong for durable provenance and machine/human inspectability.  
**Limit:** these standards describe provenance/research objects; they do not define historical truth, source criticism or owner workflow.

### I.7 AI-assisted software development

The empirical literature is heterogeneous:

- METR's early-2025 RCT: 16 experienced developers, 246 tasks in mature repositories, AI allowed increased completion time by 19%; developers nevertheless perceived speedups.
- Three enterprise field experiments (4,867 developers) found ~26% more completed tasks with AI coding assistants, with heterogeneous effects.
- A 2026 quasi-experiment found substantial output/task gains in a different organizational context.
- NBER 2026 observational work across >500,000 GitHub developers finds activity gains attenuating strongly from commits to releases, consistent with downstream human/production bottlenecks.
- DORA 2025 describes AI as an amplifier of existing organizational strengths/weaknesses.
- METR's 2026 follow-up explicitly says selection effects and concurrent-agent work make updated speedup estimation difficult.

**Project relevance:** strong evidence against simple productivity narratives. AI can increase local production while leaving verification, integration and release bottlenecks dominant. That pattern is compatible with Histo-Orla's high artifact-production capacity and persistent owner/system integration burden, but does not establish causality.

### I.8 Evaluation and benchmark limits

OpenAI stopped treating SWE-bench Verified as a reliable frontier capability measure because of test defects and contamination, then later audited SWE-bench Pro and estimated roughly 30% of public tasks were broken through overly strict tests, underspecified prompts, low-coverage tests and misleading prompts.

**Relevance:** not that Histo-Orla's tests share these defects, but that algorithmic PASS can diverge from the intended capability when specification/evaluation boundaries are wrong. This externally reinforces the project's own explicit separation of CI, scholarly validation and owner acceptance.

## J. Related Systems / Comparative Cases

### Tropy

Tropy deliberately scopes itself to organizing research photos, metadata, notes/transcriptions and export. Its own documentation says it is not a citation manager, research-writing system or publication platform.

**Mechanism:** narrow responsibility boundary and explicit non-goals.  
**What complexity it hides:** local SQLite persistence, metadata templates, photo organization/export.  
**What it returns to user:** scholarly interpretation and broader research synthesis.  
**Fit to Histo-Orla:** strong as a comparison for bounded specialist tools; weak as a model for the whole transdisciplinary assistant.

### Zotero

Zotero separates bibliographic parent items from attachment files, supports stored versus linked files, annotations and full-text indexing.

**Mechanism:** bibliographic identity and attachment/file management are related but not collapsed.  
**Fit:** strong with Histo-Orla's decision not to treat Zotero as sole source of truth.  
**Limit:** Zotero does not supply historical evidence interpretation or workflow authority.

### IIIF

IIIF Presentation 3 treats OCR, manual transcription and translation as supplementing content associated with a Canvas; Content Search 2 searches annotation content while preserving scope.

**Mechanism:** layered representations and standard addressability rather than collapsing derivative text into the image/source.  
**Fit:** strong with Source/Instance/Derivative/Findspot separation.  
**Limit:** IIIF gives interoperability semantics, not scholarly validation.

### eScriptorium

eScriptorium supports import, segmentation, transcription, automatic prediction and export to PAGE/ALTO/text, with reusable export artifacts.

**Mechanism:** specialist OCR/HTR workflow with explicit derived representations.  
**Fit:** strong as evidence that derivative-management complexity can live in a specialized tool boundary.

### Transkribus

Transkribus exports Page XML, ALTO, TEI, text/PDF and can preserve layout/zone structures.

**Mechanism:** structured derivatives remain exportable and interoperable rather than being the original.  
**Fit:** strong for derivative/findspot concepts.  
**Limit:** platform workflow and subscription/cloud assumptions differ from Histo-Orla's private/local/restartability goals.

### W3C PROV / RO-Crate as infrastructure cases

These systems make provenance and research-object structure explicit without claiming that structured provenance equals domain interpretation.

**Mechanism:** formalize lineage boundaries while leaving domain meaning to profiles/communities.  
**Fit:** strong positive comparator for loss-boundary formalization.

## K. Cross-Case Analysis

Only one project repository is under direct case analysis here. No multi-repository genericity claim is made.

Across external systems, one recurring pattern is nevertheless visible: successful infrastructures often narrow their authority. Zotero owns bibliographic/library functions; Tropy owns research-photo organization; IIIF owns interoperable presentation/search conventions; eScriptorium/Transkribus own OCR/HTR workflows; PROV/RO-Crate own provenance/research-object representation. None of these systems claims the entire scholarly reasoning chain.

That observation is **Related-System Evidence**, not a recommendation that Histo-Orla adopt their boundaries.

A second recurring pattern is that interoperability standards formalize non-equivalence and lineage rather than trying to encode all domain interpretation. This is the strongest external counterexample to treating formalization itself as the problem.

## L. Contradictions and Tensions

### Auditability ↔ cognitive load

More explicit provenance, owners and state improve inspectability and restartability; each explicit relation also creates something that may need navigation and maintenance.

### Formal safety ↔ flow

Fail-closed guards protect authority/evidence boundaries; excessive admission friction can delay low-risk situated learning.

### Domain pluralism ↔ integration

Different disciplines need different methods and evidence rules; owner-facing research still needs a coherent experience across them.

### Restartability ↔ state complexity

Durable state prevents chat loss; splitting state correctly across source/file/bibliographic/research/work-owner layers increases resolver and handoff work.

### Automation ↔ human authority

Automation can absorb mechanical burden; if safety is implemented by returning every uncertainty to the owner, authority is preserved at the cost of workload.

### Modularity ↔ handoff cost

Clear component/owner boundaries reduce semantic conflation; too many boundaries increase articulation work.

### Provider independence ↔ practical integration

Avoiding lock-in improves durability; every provider abstraction can add adapter/resolution complexity.

### Local optimization ↔ end-to-end value

A validator, context generator, source ledger or OCR step can be locally correct while the complete research task remains cumbersome.

### Epistemic safety ↔ progressive disclosure

The system must preserve detailed provenance without forcing all detail into the owner's immediate working surface.

These tensions are not resolved in this report.

## M. Unresolved Questions

1. How much of the current owner integration burden is a transient phase of an early project versus a stable consequence of the project's state/authority topology?
2. Which accepted workflows are grounded in observed repeated use versus inferred representative use?
3. Which governance artifacts are actively consulted by humans/agents during real work, and which are mostly maintained for consistency?
4. How often do deterministic guards prevent consequential errors compared with how often they create false blocks/rework?
5. What fraction of research-session time is spent on source work, interpretation, mechanical retrieval, repository coordination, context recovery and assurance?
6. Which formal distinctions reduce error measurably, and which merely relocate ambiguity?
7. Does AI-mediated work amplify artifact/issue proliferation specifically, or would comparable complexity emerge with human developers under the same epistemic constraints?
8. How stable is the current capability gap once exact retrieval/state operations mature?
9. What owner-facing cognitive load is caused by domain-essential uncertainty versus by project/interface structure?
10. Can the project's strong recovery culture coexist with lower coordination surface, or are some apparent costs the price of visible, correctable uncertainty?

## N. Research Gaps

- No longitudinal time-on-task or cognitive-load dataset exists for owner research sessions.
- No systematic inventory distinguishes artifacts actually used as boundary objects from locally useful or obsolete artifacts.
- No controlled comparison isolates AI causality from domain complexity, rapid iteration and tool constraints.
- No quantitative near-miss register estimates how often assurance prevented a consequential semantic/evidence error.
- No repeated end-to-end benchmark measures research utility without collapsing it into test PASS.
- External AI productivity studies remain strongly context-sensitive and partly contradictory.
- General provenance standards do not answer how much provenance detail should surface in a historian's immediate workflow.
- Requirements standards do not specify sufficient discovery depth for exploratory transdisciplinary research.
- Boundary-object literature explains coordination mechanisms but does not supply a project-specific optimum artifact topology.

## O. Confidence / Evidence Matrix

| Statement | Evidence | Confidence | Counterevidence | Open question |
|---|---|---|---|---|
| Core owner needs were clear early | PE/OE #1, problem baseline, workflows | strongly supported | exact situated workflows partly inferred | how much detail was still missing? |
| Premature solution/architecture promotion occurred | PE #11 and later corrections | strongly supported historically | strong recovery and demotion mechanisms | how recurrent is it now? |
| Formalization is not uniformly harmful | PE live U2/source identity; ER PROV/IIIF/FAIR | strongly supported | formalization can add maintenance cost | which types are loss-protective vs partition-imposing? |
| Assurance both protects and creates coordination work | PE #62/#63, operational tooling; ER audit/control literature | strongly supported | cumulative burden not quantified | net effect under real use? |
| Formal maturity can exceed owner-facing utility | PE coverage matrix + live-use feedback | strongly supported | early-project sequencing may explain gap | persistence after direct capabilities mature? |
| Owner sometimes acts as integration layer | OE corrections + project steering | supported | tooling absorbs some mechanics; live research substantive | stable or transitional? |
| Governance is "too much" | RI only | unresolved | multiple controls have concrete recovery value | needs measured cost/value data |
| AI causes structural proliferation | RI + process context | weakly supported/plausible | domain/governance/tool factors confounded | comparative evidence needed |
| Current architecture is intrinsically overcomplex | insufficient evidence | unresolved | essential domain complexity is high | need coupling/use measurements |
| Test PASS is not product success | PE governance + external benchmark audits | strongly supported principle | project already encodes distinction | whether any local proxy gaming occurs |
| Project is trapped in meta-work | PE implementation asymmetry | only partially supported | substantial live historical research exists | ratio over time unknown |
| Recovery/error culture is a strength | PE repeated corrections and unresolved preservation | strongly supported | recovery itself costs coordination | cost/effectiveness balance unknown |

## External evidence portfolio

### Requirements / HCI

- ISO/IEC/IEEE 29148:2018, Systems and software engineering — Life cycle processes — Requirements engineering. Current edition confirmed 2024; 2026 DIS successor under development. https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29148:ed-2:v1:en
- Nuseibeh, B.; Easterbrook, S. (2000), Requirements Engineering: A Roadmap, ICSE. DOI: 10.1145/336512.336523.
- Hollan, J.; Hutchins, E.; Kirsh, D. (2000), Distributed Cognition: Toward a New Foundation for Human-Computer Interaction Research, TOCHI 7(2), 174–196.
- Amershi, S. et al. (2019), Guidelines for Human-AI Interaction, CHI. DOI: 10.1145/3290605.3300233.

### Organization / coordination / error culture

- Star, S. L.; Griesemer, J. R. (1989), Institutional Ecology, Translations and Boundary Objects, Social Studies of Science 19(3), 387–420. DOI: 10.1177/030631289019003001.
- Carlile, P. R. (2002), A Pragmatic View of Knowledge and Boundaries, Organization Science 13(4), 442–455. DOI: 10.1287/orsc.13.4.442.2953.
- Power, M. (2000), The Audit Society — Second Thoughts, International Journal of Auditing 4, 111–119. DOI: 10.1111/1099-1123.00306.
- Reason, J. (2000), Human error: models and management, BMJ 320, 768–770. DOI: 10.1136/bmj.320.7237.768.
- Wohlrab, R. et al. (2019/2020), empirical work on boundary objects/methodological islands in agile systems engineering, including 53 practitioners across six automotive companies.

### Provenance / research infrastructure

- W3C PROV Overview / PROV Primer (2013), https://www.w3.org/TR/prov-overview/
- Wilkinson, M. D. et al. (2016), FAIR Guiding Principles, Scientific Data 3:160018. DOI: 10.1038/sdata.2016.18.
- RO-Crate Metadata Specification 1.3, Recommendation, 2026-06-22, https://www.researchobject.org/ro-crate/specification/1.3/
- Workflow Run RO-Crate (2024), provenance model implemented across six workflow systems.
- IIIF Presentation API 3.0 and Content Search API 2.0, https://iiif.io/api/
- Tropy official documentation, https://www.tropy.org/ and https://docs.tropy.org/
- Zotero official file/search documentation, https://www.zotero.org/support/
- eScriptorium documentation, https://escriptorium.readthedocs.io/
- Transkribus help/export documentation, https://help.transkribus.org/

### Software complexity / AI-assisted development

- Brooks, F. P. (1987), No Silver Bullet — Essence and Accidents of Software Engineering, IEEE Computer 20(4), 10–19. DOI: 10.1109/MC.1987.1663532.
- Lefever, J. et al. (2021), On the Lack of Consensus Among Technical Debt Detection Tools, SANER/IEEE.
- Becker, J. et al. / METR (2025), Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity: 16 developers, 246 mature-repo tasks, 19% slowdown in that population/context.
- Cui, Z. et al. (2026), The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers, Management Science: 4,867 developers, combined 26.08% increase in completed tasks, heterogeneous effects.
- Gambacorta, L. et al. (2026), Generative AI and labour productivity: A quasi experiment on coding, Journal of Financial Stability 84.
- Demirer, M.; Musolff, L.; Yang, L. (2026), Writing Code vs. Shipping Code, NBER WP 35275: activity gains attenuate across production hierarchy.
- DORA (2025), State of AI-assisted Software Development: AI as amplifier of organizational strengths/weaknesses.
- OpenAI (2026-02-23), Why SWE-bench Verified no longer measures frontier coding capabilities.
- OpenAI (2026-07-08), Separating signal from noise in coding evaluations: audit estimates ~30% of SWE-bench Pro public tasks broken.

## Abschluss: strongest findings, counterfindings, tensions, uncertainties

### Am stärksten belegte Problembefunde

1. **Formal-state maturity and owner-facing utility have diverged.** The repository has strong requirements/assurance state while many direct research capabilities remain incomplete.
2. **Semantic decomposition creates coordination work even when the decomposition is correct.** Source/state/authority boundaries are protective, but their recomposition is not free.
3. **The owner still performs material integration and correction work that the target experience intends the system to absorb.**
4. **Project controls have a dual nature:** they prevent real errors and also become operational systems with their own coupling, maintenance and failure modes.
5. **Representations are consequential:** owner metaphors or steering abstractions can become harmful when treated as durable problem partitions too early.

### Wichtigste Gegenbefunde

1. The project is not simply "stuck in meta-work": live U2 research is substantive, source-critical and epistemically careful.
2. Formalization is not itself the problem. Source/Instance/Derivative/Findspot separation demonstrably reduces semantic loss and aligns with mature provenance/interoperability practice.
3. Governance has strong recovery value: premature assumptions were demoted, unsuitable steering layers removed, unresolved states preserved and errors turned into durable evidence.
4. AI is not isolated as the cause. External productivity research is context-dependent and contradictory; domain complexity, tool constraints and organizational design remain competing explanations.

### Wesentliche Spannungen

- auditability ↔ cognitive load
- formal safety ↔ research flow
- domain pluralism ↔ owner-facing integration
- restartability ↔ state complexity
- automation ↔ human authority
- modularity ↔ handoff/articulation cost
- provider independence ↔ integration complexity
- local correctness ↔ end-to-end research value
- provenance depth ↔ progressive disclosure

### Größte verbleibende Unsicherheiten

The project lacks measurement of real research-session time, owner cognitive load, assurance prevention rate, artifact usage and end-to-end research utility. Without those, "too much governance", "architecture too complex", "AI caused proliferation" and "current burden is only temporary" all remain underdetermined.

### Offene Forschungsfragen

The discriminating questions are not which architecture or tool to choose, but which observed complexities are irreducible scholarly complexity, which are protective loss-boundaries, which are coordination/interface overhead, how much of that overhead reaches the owner, and whether those ratios change as direct research capabilities mature.

No project recommendation is made here.
