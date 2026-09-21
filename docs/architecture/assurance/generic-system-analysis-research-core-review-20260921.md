# Generic System Analysis + Deep Research — Core Intent Review

**Date:** 2026-09-21  
**Review context:** #121 / PR #123  
**Compared instruments:** generic prompt v1, v2, independent run, initial PR #118 Deep Research  
**Status:** prompt-method review / no project solution, Requirement, Method, Architecture, Selection or Delivery authority

## 1. Owner intent reconstructed for this review

The intended generic quality-assurance building block is not simply:

> inspect a project and then append a broad literature review.

It is a two-stage knowledge process:

```text
CURRENT PROJECT / DEVELOPMENT EVIDENCE
→ deep system/problem analysis
→ observed phenomena, tensions, hypotheses, risks, challenges, unknowns
→ research agenda derived from those findings
→ deep external research for each material finding/cluster
   (theory + methods + empirical evidence + related work + lessons + best practice + counterevidence)
→ fit / misfit / interface / transferability assessment
→ unresolved questions / research gaps
```

Hard boundary:

```text
NO solution selection
NO target architecture
NO roadmap
NO implementation recommendation
NO normative project synthesis
```

Allowed and required:

- diagnostic/analytical integration;
- comparison of explanations;
- fit/misfit evaluation;
- identification of theoretical mechanisms;
- assessment of transferability;
- comparison of best-practice conditions;
- contradictions and tensions;
- confidence and uncertainty;
- research gaps.

Therefore the phrase “no synthesis” must be interpreted as **no prescriptive/solution synthesis**. Diagnostic synthesis is necessary; otherwise the research cannot be connected to the observed project findings.

## 2. Overall fit of v1/v2

### What is already strongly aligned

The current prompt correctly requires:

- socio-technical rather than software-only analysis;
- symmetry between domain, user/work, requirements/product, technology, organization and epistemic architecture;
- historical/genealogical project reconstruction;
- need/nonknowledge translation analysis;
- professional error culture;
- alternative explanations and counterevidence;
- essential vs accidental complexity;
- explicit evidence classes;
- no automatic solution promotion;
- related systems and standards;
- research-quality controls;
- uncertainty / unresolved;
- cross-project caution.

v2 additionally improves research execution through:

- research planning;
- phenomenon-first search;
- evidence portfolios;
- citation chaining;
- cross-disciplinary triangulation;
- adversarial search;
- source-inspection status;
- search logging;
- saturation;
- depth self-audit;
- execution metadata.

These are strong foundations.

## 3. Main mismatch: analysis and research are adjacent, not causally coupled

Current flow is approximately:

```text
system analysis sections
→ candidate failure-pattern checklist
→ broad SOTA by predefined fields
→ related systems
→ fit analysis
```

This is not yet strict enough for the owner intent.

The desired flow is:

```text
PROJECT FINDING F1
→ what exactly is observed?
→ what remains unexplained?
→ competing project-level explanations
→ which external disciplines could discriminate them?
→ dedicated research questions
→ deep external evidence
→ what does that evidence support / weaken / leave unresolved about F1?

PROJECT FINDING F2
→ same process

...
```

The external research must be **finding-driven**, not merely field-driven.

Without this bridge, a capable model can satisfy the prompt by producing a broad but partially generic survey of HCI, RE, CSCW, AI, provenance, etc., even when some of those literatures do not discriminate the actual project problem.

## 4. Missing object: Research Agenda derived from the system analysis

Between current sections 6 and 7 a new explicit analytical object is needed.

For every material observed phenomenon/problem cluster:

```text
finding / phenomenon
project evidence
current vs historical status
scope
why it matters
what is known
what is inference
what remains unexplained
competing explanations
discriminating questions
leading / controlling disciplines
search vocabulary / alternative terminology
expected authoritative evidence types
related-system classes worth inspecting
counterevidence sought
research-depth tier
```

This is not a solution artifact.

It is the traceable bridge:

```text
PROJECT ANALYSIS
→ RESEARCH QUESTION
→ EXTERNAL RESEARCH
```

## 5. The project analysis itself needs a stronger current-state distinction

Because projects evolve, historical failure evidence must not be silently treated as current failure.

Every important project finding should be classified, for example:

- current-active;
- recurring;
- historical-resolved;
- historical-with-latent-risk;
- protective/recovery mechanism;
- one-off/tool-specific;
- unresolved.

This directly addresses the fact that a new research run may know older reports while the project has changed.

Prior audits should be treated as:

```text
secondary project evidence / prior hypotheses / research leads
```

not as authority.

Their claims should be revalidated against current and primary/timely project evidence.

## 6. The current central question is too leading for a generic instrument

v1/v2 foreground:

> does the system arise from user needs, or does an internal logic of architecture/governance/tooling become the work itself?

and supplies the explicit chain:

```text
need
→ explicitization
→ modeling
→ formalization
→ governance
→ coordination
→ user integration
```

For Histo-Orla this is a legitimate hypothesis.

For a generic QA component it is too close to a preferred explanation.

A better generic core question is:

> How are user/domain needs, uncertainty, evidence and constraints transformed through the project’s development system, and where do empirically supported fit, misfit, loss, transfer, coordination burden, recovery or value emerge?

The Histo-Orla chain can remain as one **candidate mechanism / challenge hypothesis**, not the central model.

## 7. The large anti-pattern list is useful but currently too early

The current prompt names dozens of patterns before independent analysis.

Advantages:
- high recall;
- useful challenge checklist;
- helps avoid missing known software/organizational failure classes.

Risk:
- anchoring;
- label matching;
- apparent “rediscovery” of prompt-supplied categories;
- research searches driven by labels rather than observed mechanisms.

Better role:

1. inductive project reconstruction first;
2. project-native phenomenon description;
3. own candidate mechanisms;
4. **then** use the anti-pattern list as a challenge/completeness checklist;
5. record which supplied patterns were not supported.

This makes the list adversarial rather than generative.

## 8. SOTA should be organized primarily by findings, secondarily by discipline

The current “State of the Art” section is organized by fields:

- software/system engineering;
- HCI/product;
- organization;
- epistemology;
- AI;
- knowledge systems.

This is useful for breadth control but can produce textbook-like survey output.

For the intended workflow, primary organization should be:

```text
Problem Cluster / Finding A
  → relevant theoretical traditions
  → methods / empirical results
  → counterevidence
  → related work / systems
  → best-practice conditions
  → transfer assessment
  → unresolved

Problem Cluster / Finding B
  → ...
```

Then add a secondary **cross-disciplinary theory map** showing recurring theories across clusters.

That preserves broad research while keeping it grounded in actual project evidence.

## 9. “Best practice” needs a non-prescriptive meaning

Because the overall task forbids solution conclusions, Best Practice cannot mean:

> therefore the project should adopt X.

It should mean:

```text
practice / mechanism
evidence base
population/context
reported benefits
reported costs/failure modes
preconditions
where it does not work
maturity / controversy
transferability to the observed project finding
```

The result may be:
- strong fit;
- conditional fit;
- partial fit;
- weak fit;
- misfit;
- unresolved.

No adoption conclusion follows.

## 10. Theory and method must be separated

The intended research asks for both theoretical and methodological foundations.

Current v1/v2 can blur these.

For each finding, distinguish:

### Theory / explanatory mechanism
What explains the phenomenon?

Examples of classes:
- coordination theory;
- distributed cognition;
- situated action;
- boundary objects;
- technical debt / software evolution;
- resilience / human factors.

### Method / investigation approach
How is such a phenomenon empirically studied or assessed?

Examples:
- contextual inquiry;
- cognitive task analysis;
- process mining;
- ethnographic observation;
- repository mining;
- incident analysis;
- time-on-task / workload measures;
- socio-technical congruence analysis;
- longitudinal case study;
- controlled experiment where meaningful.

This distinction matters because the owner wants not just labels that explain a problem, but knowledge of **how the field knows what it claims**.

## 11. Research depth should be proportional to finding centrality

v2’s evidence portfolio is strong, but treating every mechanism equally can create formal source collection.

A better depth model:

### Tier A — central explanatory finding
Requires broad deep dive:
- review/state-of-the-art;
- foundational work;
- recent empirical evidence;
- counterevidence/competing theory;
- methods used in the field;
- related systems/cases;
- transfer analysis;
- citation chaining;
- saturation assessment.

### Tier B — important supporting mechanism
Requires several authoritative/empirical sources plus countercheck.

### Tier C — peripheral/contextual point
Targeted authoritative verification is sufficient.

This avoids both superficiality and artificial exhaustiveness.

## 12. Finding-to-research traceability is the missing QA invariant

At completion, require a coverage table:

| Project finding | Status | Research questions | External fields | Evidence depth | Related work | Counterevidence | Fit result | Remaining uncertainty |

Two negative checks are essential:

1. **Unresearched major finding:** a central system-analysis finding has no external challenge.
2. **Unanchored research:** substantial external research has no material project finding it helps explain.

This prevents both shallow project analysis and encyclopedic literature drift.

## 13. Prior research should be reused without becoming the answer

A new run does not need artificial blindness to older reports.

For an evolving real project, the better generic rule is:

```text
prior report
= prior analysis / hypothesis / source lead

current project evidence
= revalidation basis

new external research
= update/challenge basis
```

The run should ask:

- Does the prior finding still describe current state?
- Was it resolved?
- Did the mechanism recur in another form?
- Is there new project evidence?
- Is there newer/stronger external research?
- Did prior research overstate or understate the mechanism?

This creates cumulative research without converting the old report into authority.

## 14. Deep Research execution profile should be separated from the generic method

v2 currently contains ChatGPT-product-mode concerns (“do not simulate Deep Research”).

For a truly generic reusable component, separate:

### A. Vendor-neutral research method
Defines:
- evidence;
- phases;
- depth;
- search quality;
- chaining;
- saturation;
- output.

### B. Execution profile
For ChatGPT:
- use dedicated Deep Research mode;
- expose research plan/progress;
- record mode.

Another platform can implement the same method differently.

This makes the generic QA block portable.

## 15. Prompt size and compliance risk

v2 is already ~32k characters.

Risk:
- model spends capacity satisfying headings/checklists rather than discriminating evidence;
- duplicate quality rules;
- superficial checkbox compliance;
- lower portability to other contexts.

Recommended structure of the generic instrument:

1. **Core intent + hard boundaries** — short.
2. **Phase A: empirical system analysis**.
3. **Research Agenda Gate**.
4. **Phase B: finding-driven deep research**.
5. **Phase C: cross-findings/interface assessment**.
6. **Evidence/depth protocol**.
7. **Output schema**.
8. Appendices:
   - candidate anti-pattern checklist;
   - candidate disciplinary map;
   - optional multi-repo module;
   - platform-specific execution profiles.

This is both stricter and smaller in the main execution path.

## 16. What should be preserved from initial PR #118

PR #118 had important strengths that should survive:

- broad theory/SOTA map;
- heterogeneous related-work landscape;
- transdisciplinary interfaces;
- standards and tooling evidence;
- search boundaries/bibliography.

But its later sections crossed the boundary now intentionally excluded:

- technical capability candidates;
- Git/state options;
- architecture variants;
- solution archetypes;
- tailored recommendation;
- decisive solution experiments;
- development waves;
- stop/kill list;
- refactoring blueprint.

For the intended generic analysis/research component, the useful cutoff is roughly:

```text
Intent / genealogy
+ system/root-cause analysis
+ theory/SOTA
+ related work
+ interface / fit assessment
+ uncertainties / research gaps
```

without converting those findings into a target system.

## 17. Proposed target knowledge flow

The intended generic mechanism is best represented as:

```text
PHASE A — EMPIRICAL SYSTEM ANALYSIS

Current state + history + owner/user evidence + implementation evidence
→ observations
→ episodes / natural experiments / near misses / recovery mechanisms
→ need-to-system translation audit
→ current-vs-historical classification
→ problem clusters
→ competing project-level explanations
→ confidence / gaps

                  ↓

RESEARCH AGENDA GATE

For every material cluster:
problem finding
→ unexplained mechanism
→ competing explanations
→ discriminating research questions
→ disciplines / terminology
→ evidence classes
→ related-system classes
→ counterevidence target
→ depth tier / stop criteria

                  ↓

PHASE B — FINDING-DRIVEN DEEP RESEARCH

For each cluster:
theoretical foundations
+ methodological foundations
+ reviews
+ foundational works
+ recent empirical evidence
+ critiques / competing theories
+ related works / real systems
+ documented learnings / failure cases
+ best-practice evidence and conditions
+ transfer limits
+ citation chaining
+ saturation

                  ↓

PHASE C — ANALYTICAL RECONNECTION

external finding
↔ project finding
→ strong / partial / conditional / weak / misfit / unresolved
→ what was strengthened?
→ what was weakened?
→ what changed framing?
→ what remains unknown?
→ cross-cluster tensions / shared mechanisms

                  ↓

STOP

NO solution synthesis
NO architecture
NO roadmap
NO project recommendation
```

## 18. Overall judgement

### Fit to owner intent

**Current v1:** partial-to-strong analytical fit, insufficient research-depth control.

**Current v2:** strong research-quality improvement, but only **partial-to-strong overall fit** because the crucial project-finding → research-agenda → deep-dive trace is not explicit enough.

### Main correction needed

Not “more literature” and not “more prompt length”.

The decisive correction is:

> **Make the system analysis the generator of the research agenda, and make the research agenda the mandatory routing layer for Deep Research.**

Then require deep research to return to each original finding with theory, method, empirical evidence, related work, best-practice conditions, counterevidence and transfer limits — without progressing into solutions.

## 19. Acceptance criteria for the future generic block

A run is not complete unless:

- every central project finding has current/historical status;
- every central finding has competing explanations or a justified reason why not;
- every central finding produces explicit research questions;
- every Tier-A finding receives a deep external research package;
- theory and research method are distinguished;
- external research is traceable back to project findings;
- substantial research with no project anchor is excluded or explicitly justified;
- prior reports are revalidated rather than inherited;
- counterevidence materially capable of changing the framing was sought;
- at least some external findings are allowed to weaken/reframe project hypotheses;
- best practices are reported with applicability conditions and failure modes;
- unresolved remains valid;
- final output contains no solution selection, target architecture, roadmap or implementation recommendation.

