# Histo-Orla — pointwise disposition of repeated system-analysis findings

**Date:** 2026-09-22  
**Review owner:** #64  
**Evidence inputs:** PR #118, PR #120, #121 / PR #122, dedicated Deep Research mode run PR #124, prompt-experiment provenance and reviews on PR #123  
**Status:** project finding disposition / no Requirement, Method, Architecture, Selection or Delivery authority

## 1. Purpose

This artifact does **not** average the repeated audits into one smoother narrative.

It preserves the identity of each material finding and decides, point by point, whether it should be:

- **KEEP** — substantively retained;
- **STRENGTHEN** — retained with stronger evidence status;
- **REFRAME** — same empirical core, different interpretation;
- **SPLIT** — one former point actually contains multiple mechanisms;
- **DOWNGRADE** — evidence supports only a narrower/weaker claim;
- **NEW** — materially new analytical point;
- **RESOLVED / HISTORICAL** — important historically, not evidence of a current active problem;
- **UNRESOLVED** — not enough evidence for disposition.

“Research” below means **external theoretical / methodological / empirical research into the observed problem mechanism**. It does **not** mean user research, usability research, or measurement work unless those are explicitly the research object.

No solution, architecture, roadmap or implementation recommendation is created here.

---

# 2. Finding-by-finding disposition

## F1 — Core needs were visible early

**Disposition: STRENGTHEN**

### Empirical core

The repeated runs converge that the owner’s major needs — rigorous research, complexity absorption, restartability, provenance, understandable interaction, preservation of uncertainty — were visible early.

### What changes

Do **not** explain the project’s repeated difficulty primarily as a failure of need elicitation or as “requirements were missing”.

The sharper problem is downstream:

```text
need present
→ interpretation
→ representation / requirement / work partition
→ operationalization
→ integration
→ actual owner/research experience
```

### What does not follow

This does not prove that all current requirements are sufficient or correctly prioritized.

### External research agenda

Investigate:
- Requirements Engineering: requirements transformation, requirements drift, requirements-to-design translation;
- design rationale and traceability;
- boundary between elicitation quality and downstream interpretation;
- empirical research on user involvement where high involvement still fails to guarantee system success;
- design fixation / premature commitment where relevant.

**Research question:** How can well-understood needs still be transformed into operational structures that do not deliver the intended value?

---

## F2 — “Need-to-Structure Inversion” was too coarse

**Disposition: SPLIT**

The earlier single mechanism should become two distinct findings.

### F2a — Premature problem-partition promotion

**Disposition: STRENGTHEN / REFRAME**

Observed examples support a recurring pattern in which a plausible mental model, module, phase, category or conceptual partition is promoted into durable project structure before situated evidence has established that it is the right unit of work.

The important problem is not “structure” itself.

It is:

```text
plausible interpretation
→ promoted problem partition
→ real work must conform to it
→ later evidence forces reframing
```

This covers the owner-mental-model promotion and the rejected U2/module framing more precisely than “Need-to-Structure Inversion”.

### F2b — Representation ratchet / representation-maintenance burden

**Disposition: KEEP, but distinct from F2a**

Once an idea becomes a durable artefact, owner, issue, schema or canonical representation, new work appears:
- synchronization;
- consistency maintenance;
- handoff/context requirements;
- lifecycle/status management;
- reconciliation when reality changes.

This can happen even when the original representation was reasonable.

### Why the split matters

F2a is about **premature semantic/problem partitioning**.

F2b is about **secondary work created by durable representation**.

They have different causes and need different research.

### External research agenda

For F2a:
- situated action;
- exploratory search / berrypicking;
- sensemaking;
- information-search-process research;
- design fixation / premature commitment;
- evolutionary requirements;
- adaptive / emergent work structures;
- scientific model formation and revision.

For F2b:
- articulation work;
- coordination theory;
- information/representation maintenance;
- documentation and knowledge-maintenance cost;
- organizational routines;
- technical / organizational debt;
- distributed cognition and external representations.

**Research questions:**
1. When should exploratory work resist early partitioning?
2. When does durable representation reduce complexity, and when does it create a maintenance ratchet?

---

## F3 — Formalization is not one homogeneous phenomenon

**Disposition: NEW; replaces broad anti-formalization language**

The independent audit supplied a discriminating counterexample.

### F3a — Loss-boundary formalization

Examples:
- Source ≠ Instance/Representation;
- Instance ≠ Derivative;
- Derivative ≠ Findspot;
- Findspot ≠ Finding;
- AI output ≠ Evidence;
- unresolved ≠ false.

These formal distinctions appear to **prevent epistemic loss** while leaving interpretation open.

**Current status:** protective / positive mechanism.

### F3b — Problem-partition formalization

Examples:
- predefining modules;
- turning a mental model into a project ontology/work structure;
- fixing research phases/categories before evidence stabilizes them.

These are the formalizations most strongly associated with later correction.

### Consequence for analysis

Do not use:
> “formalization is causing the problem”.

Use:
> “formalization has different functions; observed failures cluster around premature problem partitioning, while loss-boundary formalization is a strong protective counterexample.”

### External research agenda

Investigate:
- boundary objects;
- information-loss / provenance preservation;
- schema evolution;
- scientific pluralism;
- formalization in knowledge work;
- boundary infrastructures;
- cognitive dimensions, especially viscosity / closeness of mapping;
- when classification supports vs constrains discovery.

**Research question:** Which kinds of formalization preserve epistemic optionality, and which prematurely constrain the problem space?

---

## F4 — Semantic decomposition creates coordination rebound

**Disposition: STRENGTHEN**

### Empirical core

Separating:
- Domain Authority;
- Requirement Lifecycle;
- Technical Delivery;
- Verification;
- Work Owners;
- evidence/state responsibilities

can be scientifically and organizationally correct while introducing real dependency edges and integration work.

### Important correction

Do not infer:
> decomposition is wrong.

The problem is the non-equivalence:

```text
semantic correctness of boundaries
≠
low operational coordination cost
```

### External research agenda

Investigate:
- coordination theory;
- articulation work;
- socio-technical congruence;
- modularity vs coordination cost;
- Conway-type organizational coupling;
- transaction-cost perspectives where applicable;
- boundary objects / trading zones;
- team cognition / distributed cognition;
- coordination in AI-mediated work where empirical literature exists.

**Research question:** Under what conditions does semantic specialization reduce complexity overall, and under what conditions does it export integration work to a central actor?

---

## F5 — Governance / assurance accretion is not a single established root cause

**Disposition: SPLIT + DOWNGRADE**

The earlier “Governance Accretion through Error Response” is too broad as one causal explanation.

### F5a — Controls create secondary operational surfaces

**Disposition: KEEP**

Controls can require:
- context;
- status;
- review;
- handoff;
- synchronization;
- recovery.

That work is real and independently reproduced.

### F5b — Recursive error → rule → complexity → new error loop

**Disposition: DOWNGRADE to partially supported hypothesis**

PR #70 documents this genealogy in specific episodes, but the independent audit did not reproduce the complete recursive mechanism.

It should remain a bounded historical/project hypothesis, not the global explanatory model.

### F5c — Controls can be protective and worth their cost

**Disposition: STRENGTHEN as counterfinding**

Source identity, fail-closed states, NOT PASS, reversals and explicit unresolved states prevented silent escalation.

The correct question is therefore not:
> “how much governance is too much?”

but:
> “which control prevents which loss, at what secondary coordination cost, under which conditions?”

### External research agenda

Investigate:
- resilience engineering;
- Safety-I / Safety-II traditions;
- high-reliability organizations;
- defense-in-depth and control overhead;
- safety bureaucracy / proceduralization research;
- organizational routines;
- error-management culture;
- normalization of deviance / control failure where applicable;
- software assurance economics / compliance burden where evidence exists.

**Research question:** How do protective controls change failure probability, recovery ability and coordination burden simultaneously?

---

## F6 — Local verification / global utility gap

**Disposition: STRENGTHEN; keep as independent point**

### Empirical core

Formal PASS, green CI, traceability completeness or locally correct components do not establish:
- research usefulness;
- end-to-end workflow adequacy;
- cognitive relief;
- correct problem framing;
- successful integration.

This finding converges strongly across audits.

### Why it must remain separate

This is not reducible to governance burden.

A system can have low governance burden and still optimize local proxies that miss global utility.

### External research agenda

Investigate:
- Goodhart-like proxy effects;
- local vs system optimization;
- socio-technical systems evaluation;
- outcome vs process metrics;
- software quality models vs actual utility;
- human-centered evaluation of expert knowledge systems;
- DevOps/DORA-type metric transfer limits to research software;
- verification vs validation distinctions in systems engineering.

**Research question:** Which forms of local correctness are valid proxies for end-to-end research value, and where do they systematically fail?

---

## F7 — Readiness conflation / assumption laundering

**Disposition: KEEP AS SEPARATE FAILURE CLASS**

### Empirical core

PR #119 exposed a distinct error:
a valid provenance path or available upstream object was treated as if it implied admitted, current, text-bearing retrieval input / corpus readiness.

The independent blind audit missed this.

### Why this must not be averaged into F2/F5/F6

The failure is specifically:

```text
state/evidence A exists
→ unstated assumption
→ prerequisite B is treated as satisfied
→ execution proceeds on false readiness
```

This is neither merely premature abstraction nor merely governance burden.

It is a **precondition / admission / state-validity failure**.

### External research agenda

Investigate:
- design by contract / precondition enforcement;
- typestate and state-machine validity;
- admission control;
- workflow/data-pipeline readiness;
- provenance vs availability vs fitness-for-use distinctions;
- state freshness / stale validity;
- TOCTOU-style assumption gaps where conceptually relevant;
- safety cases / assurance cases for prerequisite claims;
- epistemic status and evidence-to-action transitions.

**Research question:** How should systems distinguish “exists”, “is traceable”, “is available”, “is admitted”, “is current”, and “is fit for this operation” without collapsing them into one readiness state?

---

## F8 — Premature promotion of owner language is established; “mirroring” is not

**Disposition: REFRAME + DOWNGRADE causal label**

### Established finding

Owner language / mental models were in at least one material case promoted too quickly into durable semantics/project structure.

### Not established strongly enough

The stronger conversational explanation:
- mirroring;
- affirmative abstraction bias;
- agreement language as primary cause

was not independently reconstructed.

### New canonical wording for analysis

Prefer:

> **premature semantic promotion of owner language / mental models**

Treat “mirroring / affirmative abstraction” as one candidate mechanism, not the finding itself.

### External research agenda

Investigate:
- requirements elicitation and interpretation;
- confirmation bias;
- anchoring;
- conversational alignment / accommodation;
- AI sycophancy / agreement bias where empirical work supports it;
- collaborative sensemaking;
- design-by-metaphor;
- mental models in HCI;
- semantic commitment in participatory/co-design processes.

**Research question:** Through which interaction mechanisms does provisional user language become over-authoritative design structure?

---

## F9 — Context/handoff protection can become context/handoff work

**Disposition: KEEP, but do not merge with F4**

### Distinction from F4

F4 is coordination caused by **semantic decomposition**.

F9 is secondary work caused by mechanisms intended to preserve:
- restartability;
- state continuity;
- authority boundaries;
- reproducibility;
- cross-chat handoff.

These overlap but are not identical.

### Empirical status

The tension is independently reproduced:
restartability/context protection is valuable, but maintaining those protections can itself become work.

### External research agenda

Investigate:
- interruption/resumption;
- distributed cognition;
- external memory;
- handoff design;
- cognitive offloading;
- context reconstruction;
- knowledge continuity;
- provenance and reproducibility overhead;
- coordination cost in transient/rotating teams;
- AI-agent context persistence and handoff research where mature evidence exists.

**Research question:** What is the minimum representation needed to preserve high-fidelity restartability without turning restart protection into a parallel work system?

---

## F10 — Live evidence does more than validate; it reframes the unit of work

**Disposition: NEW / STRENGTHEN**

### Empirical core

Live source encounters repeatedly changed:
- terminology;
- search direction;
- relevant entities;
- evidence demands;
- useful analytical units;
- the appropriateness of pre-existing modules/partitions.

### Important reinterpretation

Some “churn” may not be a process defect.

It may be intrinsic to exploratory historical inquiry:
the useful problem structure is partly discovered **through evidence interaction**.

This does not excuse arbitrary churn; it creates a competing explanation that must be retained.

### External research agenda

Investigate deeply:
- situated action;
- exploratory search;
- berrypicking;
- information search process;
- sensemaking;
- abductive reasoning;
- hermeneutic iteration;
- scientific discovery / model revision;
- exploratory data analysis;
- inquiry-driven workflow systems;
- adaptive workflow / case management vs prescriptive workflow.

**Research question:** Which project reframings are avoidable design errors, and which are normal evidence-driven evolution of an exploratory research problem?

---

## F11 — Visible correction/churn is partly evidence of recovery capability

**Disposition: NEW**

### Empirical core

The project records:
- NOT PASS;
- reversals;
- rejected abstractions;
- unresolved states;
- layer removal;
- corrected assumptions.

A less instrumented project could retain the same errors silently.

### Why this matters

“Number of corrections” cannot be interpreted directly as “project instability”.

At minimum distinguish:
- error creation;
- detection latency;
- propagation;
- recovery;
- recurrence.

### External research agenda

Investigate:
- resilience engineering;
- error management;
- learning organizations;
- high-reliability organizations;
- incident learning;
- software rollback/recovery;
- observability of failure;
- safety culture;
- antifragility claims only if empirically grounded.

**Research question:** When does visible correction indicate healthy error detection and recovery rather than uncontrolled project churn?

---

## F12 — AI may amplify structure generation, but AI-primary causality is not established

**Disposition: DOWNGRADE**

### Retained narrower claim

AI/LLM tooling can plausibly make generation of:
- coherent prose;
- schemas;
- issue structures;
- abstractions;
- implementation artefacts

cheap relative to semantic validation.

### Not established

Current evidence does not isolate AI as the primary cause of:
- governance growth;
- coordination burden;
- premature abstraction;
- project loops.

### External research agenda

Investigate:
- empirical AI-assisted software engineering;
- automation bias;
- human-AI joint performance;
- AI-generated specification quality;
- calibration and overtrust;
- productivity vs review/rework cost;
- agentic context/handoff error;
- task-dependent differences between bounded coding and complex long-lived knowledge work.

**Research question:** Does AI materially change the ratio between artefact-generation speed and validation/integration capacity in complex research-software development?

---

## F13 — “Owner as workflow integrator” is supported; “Human as Semantic Compiler” is stronger than the evidence

**Disposition: SPLIT / DOWNGRADE stronger label**

### F13a — Owner as workflow/integration point

**Disposition: KEEP**

Direct qualitative evidence supports that the owner has had to integrate across:
- chat;
- repository;
- tools;
- research artefacts;
- work owners;
- technical/fachliche states.

### F13b — Human as Semantic Compiler

**Disposition: DOWNGRADE to open hypothesis**

This implies a stronger, stable role:
the human repeatedly performs semantic compilation that the system ought to perform.

The independent evidence is insufficient to establish that across the project.

### External research agenda

Investigate:
- articulation work;
- invisible work;
- human-in-the-loop role allocation;
- distributed cognition;
- mixed-initiative systems;
- boundary spanning;
- coordination load;
- orchestration in multi-tool / AI-assisted work;
- semantic mediation / knowledge integration.

**Research question:** Which integration activities genuinely require human scholarly judgement, and which are accidental coordination work created by the system’s boundaries?

---

## F14 — Interface/orchestration friction is real; “dominant bottleneck” is not established

**Disposition: KEEP mechanism / DOWNGRADE rank claim**

### Retained

Interface and orchestration friction is repeatedly observed.

### Removed from current confident language

Do not call it:
> the measured primary or dominant bottleneck.

There is insufficient comparative evidence to rank it against:
- source access/retrieval;
- method uncertainty;
- historical complexity;
- implementation defects;
- documentation/state burden;
- other workflow costs.

### External research agenda

This is a **cross-cutting synthesis question**, not a standalone literature field.

Relevant research comes from F4, F6, F9, F13 plus:
- bottleneck theory;
- Theory of Constraints where transferable;
- cognitive work analysis;
- work-system analysis;
- socio-technical performance evaluation.

**Research question:** Under what evidence could interface/orchestration friction legitimately be ranked as a dominant system constraint rather than one important friction class among several?

---

# 3. What should no longer be one finding

The following earlier compressions should be explicitly retired:

| Old bundled wording | New disposition |
|---|---|
| “Need-to-Structure Inversion” | split into F2a problem-partition promotion + F2b representation ratchet |
| “Formalization problem” | replaced by F3a protective loss-boundary formalization + F3b problem-partition formalization |
| “Governance Accretion” | split into F5a control work surface + F5b recursive rule loop + F5c protective control |
| “Mirroring / Affirmative Abstraction Bias” as finding | finding becomes F8 premature semantic promotion; mirroring remains candidate cause |
| “Human as Semantic Compiler / Workflow Engine” | split into F13a supported workflow integrator + F13b unresolved semantic-compiler hypothesis |
| “Interface/orchestration bottleneck” | mechanism retained; bottleneck ranking downgraded |
| “Churn / repeated correction” | split into failure occurrence and F11 recovery visibility |
| “readiness” as part of generic assumption error | F7 remains its own admission/precondition failure class |

---

# 4. New aspects that must remain visible

The repeated runs add four material analytical advances that should not be absorbed into older labels:

1. **F3 — formalization-type discrimination:** protective loss boundaries vs constraining problem partitions.
2. **F7 — readiness/admission is a distinct failure class:** existence/provenance does not imply operational fitness/readiness.
3. **F10 — evidence-led reframing:** live evidence can change the correct unit of work, not merely validate it.
4. **F11 — correction visibility:** visible reversals are partly evidence of recovery capacity, not simply project failure.

These are not wording refinements. They change the problem model.

---

# 5. External research programme implied by the findings

This is a **problem-research agenda**, not a user-research agenda and not a solution programme.

## R-A — Exploratory inquiry vs premature problem partitioning

Driven by F2a, F3b, F10.

Research domains:
- situated action;
- exploratory search / berrypicking;
- information search process;
- sensemaking;
- abductive reasoning;
- hermeneutic iteration;
- design fixation;
- evolutionary requirements;
- adaptive case/workflow management.

Core question:
> How should systems support inquiry whose meaningful structure emerges during evidence interaction?

## R-B — Representation, formalization and epistemic loss

Driven by F2b, F3a/F3b.

Research domains:
- provenance;
- schema evolution;
- boundary objects;
- scientific pluralism;
- cognitive dimensions;
- information-loss prevention;
- knowledge representation under uncertainty.

Core question:
> Which representations stabilize necessary loss boundaries without prematurely stabilizing interpretation or work partition?

## R-C — Decomposition, specialization and coordination rebound

Driven by F4, F13.

Research domains:
- coordination theory;
- articulation work;
- socio-technical congruence;
- modularity;
- Conway-type coupling;
- distributed cognition;
- boundary spanning;
- knowledge integration.

Core question:
> When do correct responsibility boundaries reduce overall complexity, and when do they merely relocate integration cost?

## R-D — Controls, assurance, recovery and secondary work

Driven by F5 and F11.

Research domains:
- resilience engineering;
- HRO;
- Safety-I / Safety-II;
- error management;
- incident learning;
- control/procedural overhead;
- software assurance;
- organizational routines.

Core question:
> How can the project distinguish protective control, wasteful proceduralization, and healthy recovery instrumentation?

## R-E — Local correctness vs global utility

Driven by F6.

Research domains:
- systems validation;
- proxy metrics / Goodhart effects;
- human-centered evaluation;
- socio-technical performance;
- software verification vs validation;
- expert knowledge-system evaluation.

Core question:
> What evidence is required before local technical/formal success can be treated as evidence of end-to-end research value?

## R-F — Readiness, preconditions and assumption laundering

Driven by F7.

Research domains:
- design by contract;
- typestate/state machines;
- admission control;
- data/workflow readiness;
- freshness/staleness;
- provenance vs fitness-for-use;
- assurance cases.

Core question:
> How should multi-stage research/software systems represent and verify prerequisite status without silently promoting weaker evidence into stronger readiness claims?

## R-G — Human-AI interaction as promotion/amplification mechanism

Driven by F8 and F12.

Research domains:
- AI sycophancy / agreement bias;
- automation bias;
- human-AI calibration;
- AI-generated specifications;
- AI-assisted software engineering;
- mixed-initiative interaction;
- conversational alignment;
- review/rework economics.

Core question:
> Where does AI specifically alter promotion, validation or integration dynamics, and where is it only one accelerator inside a broader socio-technical mechanism?

## R-H — Restartability, handoffs and external memory

Driven by F9.

Research domains:
- interruption/resumption;
- cognitive offloading;
- distributed cognition;
- knowledge continuity;
- provenance/reproducibility overhead;
- handoff design;
- transient-team / agent context transfer.

Core question:
> What is the minimum sufficient durable context for high-fidelity restart without creating a parallel coordination system?

---

# 6. Documentation changes implied now

These are narrow documentation corrections, not new project machinery.

1. **#64:** current reconciliation must supersede its older “Hauptrisiko = Governance-/Operationalisierungskomplexität” wording as present diagnosis; old wording remains historical.
2. **PR #120:** retain as informed second-order audit, not independent replication.
3. **PR #122:** retain as the independent/source-blinded replication artifact with its misses explicitly preserved.
4. **PR #118:** retain its broad SOTA/related-work value, but do not carry its solution/architecture recommendations forward as findings.
5. **Current finding vocabulary:** use F1–F14 / their semantic distinctions in future audit synthesis rather than reusing the old bundled labels without qualification.
6. **PROJECT_STATE:** update only after audit PR disposition, with one concise accepted review pointer rather than copying this full model into the root handoff.

No new governance document is required beyond this disposition.

---

# 7. What does not need to change now

The repeated runs do not currently establish:

- a new accepted Requirement;
- a new Domain Method Truth;
- a new Architecture Decision;
- a new technical framework;
- a new owner topology;
- a new current-work selection.

The material change is in the **problem model and the research agenda**.

---


# 7. Impact on the already-started architecture/refactoring plan

This section answers whether #92 / PR #119 should be stopped because the repeated audits changed the problem model.

## Overall disposition

**NO BLANKET STOP.**

The current plan contains two different classes of work:

1. **loss-boundary / readiness / reversible capability work** that is now better supported by the repeated audits;
2. **solution-structure / integration-shape hypotheses** that must no longer be treated as an automatic downstream roadmap.

The correct disposition is therefore:

```text
keep implemented protective boundaries
+ continue bounded requirement-backed capability tests
+ freeze automatic progression into later architecture waves
+ reframe evidence-led integration steps
+ revalidate solution-shaped downstream waves before release
```

No rollback of #50/#51 or existing deterministic safety work is justified by the new findings.

## 7.1 #92 Re-Baseline Roadmap

| Roadmap element | Disposition | Reason |
|---|---|---|
| R0 fresh baseline / freeze on invention | **KEEP** | directly compatible with anti-promotion / evidence-first findings |
| R1 inventory + disposition | **KEEP / historical-completed** | reconciliation mechanism, not research partition |
| R2 objective reconciliation | **KEEP** | preserves accepted authority; does not solve research structure |
| R3 Product/Research/Tool responsibility view | **KEEP WITH BOUNDARY** | useful as architecture reading model only; must not become the researcher's fixed work ontology |
| R4 minimal repo/code topology | **HOLD UNTIL TRIGGER** | current `no product-code move yet` is reinforced by new findings |
| R5 Thin Vertical Product Slice | **REFRAME** | useful only as bounded evidence-led experiment; must not be a fixed primary research partition or pre-sized pilot |
| R6 Operational Core consolidation | **CONDITIONAL KEEP** | only settled loss-boundaries / real shared consumers; no expansion because “core completeness” looks attractive |
| R7 pilot/legacy cleanup | **KEEP** | reduces representation ratchet if disposition removes stale active surfaces |
| R8 fresh-context + owner acceptance | **KEEP + EXTEND ANALYTICALLY** | must test not only resume/acceptance but whether the system permits evidence-led reframing without new meta-work |

### Required R5 reinterpretation

Old risk:
```text
predefined vertical slice
→ treated as correct unit of work
→ real evidence forced to fit slice
```

Required interpretation:
```text
bounded current question
→ real evidence interaction
→ slice may narrow / widen / reframe
→ research output and system learning remain distinct
→ no automatic architecture promotion
```

Thus **Vertical Slice is an experimental envelope, not a canonical partition of historical inquiry**.

## 7.2 PR #119 Agentic Refactoring / #53 Retrieval Plan

### Wave 0 — Planning/admission repair
**CONTINUE / KEEP.**

The new F7 readiness/admission finding strongly validates the distinction:

`provenance exists != text-bearing input != current availability != admitted corpus != fit-for-operation`.

This repair is not obsolete; it is one of the best-supported corrections.

### Wave 1 — Synthetic Exact Retrieval
**CONTINUE WHEN EXPLICITLY SELECTED AND PREFLIGHT-READY.**

Reason:
- accepted REQ-RET basis exists;
- bounded/reversible;
- no architecture commitment;
- exact retrieval without LLM remains a valid capability requirement;
- tests protect Source/Derivative/Findspot boundaries.

Important: passing Wave 1 must not be interpreted as evidence for the later architecture.

### Wave 2 — Real Evidence/Corpus Admission
**CONTINUE / KEEP.**

This is a direct operationalization of F3 loss-boundary formalization + F7 readiness/admission.

It should remain a distinct stage.

### Wave 3 — Real Exact Retrieval falsification
**CONTINUE CONDITIONALLY.**

Still a valid capability falsification after Wave 2. No automatic product-architecture inference follows.

### Wave 4 — Controlled historical variants
**CONTINUE CONDITIONALLY / DOMAIN-OWNED.**

Compatible with evidence-led research only if variant generation remains a search decision with provenance and can change as evidence changes.

### Wave 5 — Shared runtime reader / product-code trigger
**HOLD AS HYPOTHESIS.**

The existing “two real consumers” trigger is good, but this wave is no longer a presumed next architectural step. Revalidate actual duplicated responsibility after Waves 2–4.

### Wave 6 — Restartability / Availability integration
**CONTINUE, BUT MINIMIZE REPRESENTATION.**

Restartability is an accepted need and F9 confirms the tension. The task is not to maximize handoff structure; it is to find the minimum durable context that preserves truthful resumption.

### Wave 7 — Heterogeneous #47 Vertical Research Slice
**REFRAME / NO AUTOMATIC RELEASE.**

The current plan already says “owner-selected bounded question”; that is essential.

New requirement for interpretation:
- the slice may be reframed by live evidence;
- success is not “the predesigned chain ran end-to-end”;
- success includes whether the system can preserve state when the useful research partition changes.

No #47 selection follows from this review.

### Wave 8 — Read-model probe
**HOLD / EVIDENCE-TRIGGERED ONLY.**

The existing “only if measured pain remains” condition is strengthened. Do not treat SQLite/FTS/read-model as the destination implied by earlier solution synthesis.

### Wave 9 — Thin Skill/MCP/UI adapter
**DOWNGRADE FROM ROADMAP DESTINATION TO OPTIONAL LATER HYPOTHESIS.**

This step is solution-shaped and not entailed by the replicated problem findings.

It may be reconsidered only after stable capabilities and a demonstrated interaction/integration need exist.

## 7.3 Existing work that should NOT be rolled back

### #50 Canonical Research State / Source Identity
**KEEP.**

The repeated audits and PR #124 strengthen this architecture contract as a positive example of loss-boundary formalization.

### #51 Document / Findspot
**KEEP.**

Its concrete separation of Source / Representation / Instance / Derivative / Findspot is one of the clearest project successes under the new problem model.

### Existing fail-closed / unresolved semantics
**KEEP.**

The new research treats visible correction, NOT PASS and unresolved as recovery capacity, not waste by default.

### Requirements/Assurance safety already encoding settled invariants
**KEEP, but freeze expansion without a demonstrated loss.**

The question is not whether these controls exist; it is whether each additional control has a known protected loss and acceptable secondary work.

## 7.4 Work that should be paused before further expansion

The following should **not** advance merely because they are listed downstream in #92/#119:

- new product-package topology;
- shared runtime abstraction without real duplication;
- generic capability/core expansion without multiple real consumers or a settled cross-cutting invariant;
- additional Work-Context/Handoff fields not tied to a demonstrated information-loss/restart failure;
- read-model/index infrastructure without measured post-capability navigation pain;
- Skill/MCP/UI layer without stable product interfaces and observed interaction need;
- any fixed pilot/module/work partition treated as the “correct” research structure before evidence contact.

## 7.5 Stop condition for the plan itself

A **full stop/re-baseline** would be justified if any of the following becomes true:

1. an accepted Requirement that materially motivates the plan is withdrawn or contradicted;
2. Source/Instance/Findspot separation is shown to damage rather than protect the live research workflow;
3. current capability work requires a new durable ontology/problem partition not supported by evidence;
4. bounded capability increments repeatedly add more owner coordination than they remove;
5. the plan cannot accommodate evidence-led reframing without rewriting its own architecture;
6. downstream waves begin to execute because of roadmap sequence rather than fresh prerequisite/evidence checks.

Current evidence does **not** establish any of 1–5 as already true. #119 explicitly protects against 6 at the current stage.

## 7.6 Current recommendation

The project should **not stop the entire rebuild**.

It should stop treating the plan as a single committed transformation sequence.

The active interpretation should become:

```text
protect proven loss boundaries
→ execute only bounded accepted capabilities
→ let real evidence challenge the work partition
→ re-evaluate architecture after each material real-use result
→ promote shared/product structure only from demonstrated reuse / stable responsibility
```

This is a narrower and more evidence-responsive continuation of the existing plan, not a restart from zero.


# 8. Handoff

This file is the current #64 **finding-disposition layer**.

It does not replace the evidence-bearing source audits.

A fresh reviewer should use it to understand:
- which old claims survive;
- which were split or weakened;
- which new mechanisms appeared;
- which external research programmes are now justified by specific project findings.

No #44 blocker is created.
