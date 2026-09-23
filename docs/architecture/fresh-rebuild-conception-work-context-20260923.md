# Histo-Orla — Fresh Rebuild Conception Work Context

**Date:** 2026-09-23  
**Status:** `ready-for-fresh-rebuild-conception / conception-only / no implementation authority`  
**Current Work Owner / Re-entry:** #92  
**Technical / Architecture Lead:** #48  
**Requirements Authority:** #42  
**Development / Verification:** #59  
**Domain Method Truth:** #60  
**Input review:** #64 + D4 reconciliation  
**Current work selection:** `selection-open` for research/product work; this work context creates no research-case selection.

## 1. Purpose

This is the canonical start/resume context for the first **fresh rebuild conception** after the completed D4 Research→Rebuild reconciliation.

The task is to re-derive the project rebuild from the current evidence and current repository reality. It must **not** continue or patch the earlier #92 R4–R8 sequence or PR #119 as if they were the current plan.

The governing input equation is:

```text
accepted Requirements (#42)
+ current repository reality
+ reconciled F1–F14 project findings
+ D4 external research
→ fresh technical/architecture derivation under #48
```

The old #92 roadmap, PR #118 solution synthesis and PR #119 execution plan are **Prior Art / earlier solution hypotheses**. Each may be retained, adapted, rejected, deferred or used as a test hypothesis only after fresh derivation.

## 2. Mandatory bootstrap

Before substantive work, freshly read in this order:

1. root `AGENTS.md`;
2. root `PROJECT_STATE.md`;
3. root `README.md`;
4. issue #92;
5. this work context;
6. issue #42 and:
   - `docs/research/synthesis/requirements-baseline.md`;
   - `docs/research/synthesis/requirements-extensions.md`;
   - `docs/research/synthesis/requirements-structure.md`;
   - `docs/research/synthesis/requirements-responsibility-dependency-map.md`;
7. issue #48 and `docs/architecture/requirements-derivation.md`;
8. issue #59 and `docs/development/requirements-coverage.md`;
9. current D4/project-reconciliation inputs:
   - `docs/architecture/assurance/repeated-system-audits-project-implications-20260922.md`;
   - `docs/research/audits/d4-problem-driven-external-research-20260922.md`;
   - `docs/architecture/assurance/d4-project-reconciliation-rebuild-reentry-20260923.md`;
10. current relevant Architecture Contracts / ADRs / operational code for any responsibility being assessed;
11. only after the problem/concern is explicit, current technical SOTA / Existing Tools / Standards / Prior Art relevant to the concrete technical research question.

Do not infer current implementation state from old roadmap prose. Inspect the repository, current coverage and relevant code/tests.

## 3. Primary function

`Architecture / Development / Research Software Engineering — conception and technical derivation only`.

This work may synthesize architecture concerns, technical research questions, alternatives, trade-offs, target responsibility boundaries, migration/no-migration strategy and a rebuild plan.

It does **not** itself authorize implementation.

## 4. Bounded question

> Given the accepted Requirements, the system that actually exists today, the reconciled F1–F14 problem model and D4 external research, what is the smallest sufficient, evidence-responsive rebuild conception that improves the historical research workplace without losing scientific integrity, provenance, restartability or explicit uncertainty?

The answer must show **why** each material proposed responsibility or structural change exists and which evidence/Requirement it serves.

## 5. Required evidence roles

Keep distinct:

- accepted Requirement / Constraint — #42 authority;
- Domain Method Truth — #60 authority;
- PE — current project/repository evidence;
- OE — persisted owner/workflow evidence;
- ER — D4 external research evidence;
- RS — related-system evidence;
- technical SOTA / tool evidence — evidence about implementation means, not Requirement truth;
- architecture inference / solution hypothesis — #48 technical reasoning;
- unresolved / design-testable unknown — must remain explicit.

No solution hypothesis may silently become a Requirement.

## 6. Protected distinctions and hard inputs from the D4 reconciliation

The conception must preserve the current reconciled distinctions unless stronger new evidence is explicitly routed through the proper authority:

- F2a premature problem-partition promotion ≠ F2b representation-maintenance burden;
- F3a protective loss-boundary formalization ≠ F3b constraining problem-partition formalization;
- F4 specialization/coordination rebound ≠ F9 temporal restart/handoff burden;
- F5a secondary control work ≠ F5b recursive error→rule hypothesis ≠ F5c protective control value;
- F6 local verification ≠ global research/workflow utility;
- F7 existence/provenance/availability/admission/currency/fitness are distinct claims;
- F8 premature semantic promotion ≠ proven AI-sycophancy causation;
- F10 evidence-led reframing ≠ arbitrary churn;
- F11 visible correction is conditional recovery evidence, not automatic health;
- F12 AI amplification ≠ AI-primary causation;
- F13 workflow integration ≠ proven human “semantic compiler” role;
- F14 orchestration friction ≠ proven dominant bottleneck.

Also preserve:

```text
Source ≠ Representation/Instance
Instance ≠ Derivative
Derivative ≠ Findspot
Findspot ≠ Finding
AI output ≠ Evidence
unresolved ≠ false
```

These are constraints on reasoning. They do not prescribe a database, package layout or product topology.

## 7. Forbidden inherited assumptions

The fresh conception must not start from any of the following as established facts:

- the old Vertical Research/Product Slice is the correct primary unit of historical research work;
- the prior `validate | resolve | derive | context | evidence | transition` “Operational Core” shape is already the target core;
- a shared runtime/package is the natural destination;
- `src/histo_orla/` is required;
- a read model, SQLite, FTS, Skill, MCP or UI is a default later step;
- the #49→#51→#53→#55→#57 W1 chain is the current critical path;
- #49 is automatically the current technical enabler;
- PR #119 waves are an active execution sequence;
- orchestration is the dominant bottleneck;
- AI is the primary root cause;
- more formalization is inherently harmful;
- fewer controls are inherently better;
- every visible correction means instability.

Rejecting an inherited assumption does not establish its opposite.

## 8. Remaining unknowns to carry, not silently solve

At minimum carry forward the D4-reconciliation unknowns:

- intrinsic exploratory reframing vs avoidable framing error — `DESIGN-TESTABLE-UNKNOWN`;
- net burden/benefit of individual representations and controls — `PROJECT-EVIDENCE-GAP`;
- essential scholarly integration vs accidental coordination — `PROJECT-EVIDENCE-GAP`;
- minimal sufficient restart context — `DESIGN-TESTABLE-UNKNOWN`;
- F5b full recursive-loop causality — `PROJECT-EVIDENCE-GAP`;
- F8 causal mechanism / F12 AI-primary causality — `PROJECT-EVIDENCE-GAP`;
- optimal readiness-state granularity — `DESIGN-TESTABLE-UNKNOWN`;
- recovery vs churn in F11 — `PROJECT-EVIDENCE-GAP`;
- actual bottleneck ranking — `PROJECT-EVIDENCE-GAP`;
- transfer limits from other domains — `NON-BLOCKING-UNKNOWN`.

No current `RESEARCH-BLOCKER` exists.

Architecture may proceed by preserving these unknowns, designing reversible alternatives or specifying later evidence/acceptance needed to discriminate them.

## 9. Required work sequence

### A. Fresh current-state inventory

Build a concise current-state inventory from the repository:

- what is actually implemented and verified;
- what is partial;
- what exists only as contract, plan, pilot or prior-art hypothesis;
- what is duplicated or manually synchronized;
- what product/runtime responsibilities genuinely exist today;
- which accepted Requirements are currently unmet/partial and architecture-significant;
- which existing technical structures protect a demonstrated loss boundary.

Do not treat issue activity or old plan order as implementation reality.

### B. Requirement → responsibility re-derivation

Using #42 and the current `requirements-derivation.md` contract:

```text
Requirement / Cluster
→ upstream Goal / Need / Pain
→ System Responsibility / Capability
→ Architecture Concern / Quality Attribute
→ Quality / Failure Scenario where useful
→ Technical Research Question
```

Do this before naming a technology or target package.

### C. Integrate F1–F14 / D4 constraints

For each material concern state:

- which reconciled finding(s) it touches;
- which protected distinction/loss it must preserve;
- which forbidden inherited assumption it avoids;
- which unknown remains unresolved;
- whether the concern is local, cross-cutting or only an evaluation concern.

Do not build a single “root-cause architecture”.

### D. Technical SOTA / Existing Tools / Standards

Only after the technical research question is explicit:

- inspect current technical SOTA and Best Practice proportional to consequence;
- inspect current versions/capabilities of Existing Tools and Standards;
- prefer `avoid → reuse → configure → integrate → thin custom layer → build custom`;
- treat standards/tools as implementation means, not semantic authority;
- document transfer limits and lock-in/loss risks.

Use fresh external verification for current software/tool/standard claims.

### E. Candidate approaches and trade-offs

For each material responsibility/concern, compare meaningful alternatives including where applicable:

- keep current;
- simplify/remove;
- derive/generate instead of maintain;
- reuse/configure/integrate existing tool;
- thin custom adapter;
- custom implementation;
- defer pending project evidence;
- bounded spike/benchmark.

Record:

```text
requirements covered
benefit
complexity / secondary work
scientific loss risk
operational coordination cost
reversibility / lock-in
existing-tool leverage
unknowns
verification / acceptance target
decision class
```

### F. Pointwise disposition of prior rebuild plan

Do not patch the old roadmap globally.

Disposition each materially relevant old element from #92 / PR #119 as:

- `RETAIN`
- `ADAPT`
- `REJECT`
- `DEFER`
- `TEST`

with current evidence and Requirement basis.

At minimum review:

- prior Product/Vertical Slice semantics;
- product-code boundary / `src/`;
- Operational Core;
- shared runtime reader;
- restartability/context representation;
- heterogeneous research slice;
- read model / SQLite / FTS;
- Skill/MCP/UI layer;
- old #49/#51/#53/#55/#57 sequencing.

### G. Fresh target conception

Only after A–F, derive the new conception:

- system responsibility map;
- canonical vs derived/generated state boundaries;
- product capability vs operational tooling boundaries;
- domain/research vs technical execution boundary;
- integration/handoff boundaries;
- minimum durable state and explicit readiness/admission semantics;
- evidence-responsive/revisable research-work support;
- evaluation/acceptance model separating local verification from global research utility;
- repository/code topology only where justified;
- migration / no-migration strategy;
- architecture decisions and ADR candidates;
- explicit open unknowns and tests;
- dependency/release sequence.

The target conception may be concrete, but every concrete structure must be traceable to current evidence and Requirements.

## 10. Treatment of real research workflow

The rebuild must support historical inquiry whose useful unit of work may change after source contact.

Therefore:

- a bounded experiment/slice is an **experimental envelope**, not automatically the ontology of historical research;
- the system must allow a question, terminology or analytical unit to narrow, widen or reframe without corrupting provenance/state;
- durable representations should be promoted only when their protected loss/shared responsibility is known;
- research output and system-learning/evaluation remain distinguishable.

This does not forbid structure. It requires reversible, evidence-responsive structure.

## 11. Evaluation / acceptance requirements for the conception

Do not use CI/trace completeness as the sole success criterion.

The conception must specify how later implementation can test at least:

- scientific/provenance non-loss;
- correctness of readiness/admission claims;
- restartability/resumption fidelity;
- research-owner comprehension and usability;
- end-to-end task/output quality where relevant;
- manual coordination / secondary work introduced or removed;
- detection/recovery behaviour for controlled losses;
- whether architecture can accommodate evidence-led reframing;
- whether shared abstractions have real consumers;
- whether an alleged bottleneck is actually measured rather than assumed.

Owner/workflow evidence is not historical evidence.

## 12. MAY / MUST NOT

### MAY

- derive Architecture Concerns and Technical Research Questions;
- research current technical SOTA and existing tools;
- produce solution hypotheses and comparisons;
- define a fresh target architecture/conception;
- define migration/no-migration strategy;
- create ADRs under #58 where a material architecture decision is actually mature;
- identify bounded spikes/benchmarks needed before implementation;
- propose a new implementation/release sequence.

### MUST NOT

- change accepted Requirements outside #42;
- invent Domain Method Truth outside #60;
- silently resolve scholarly uncertainty;
- inherit the old roadmap as authority;
- start implementation/code migration as part of this conception task;
- select a historical research case as `selected-current`;
- promote a pilot/case pattern to generic architecture without evidence;
- create a new workflow/agent/platform layer merely for conceptual completeness;
- treat D4 external research as direct solution authority.

## 13. Stop / handoff conditions

Return to the relevant authority if:

- a required system obligation is not supported by an accepted Requirement/Owner constraint → #42;
- a material scholarly/method meaning is missing → #60;
- a normative/irreversible/rights/scope decision is required → #44/#58 as applicable;
- a technical option cannot be compared without a bounded experiment → define a spike/benchmark, do not guess;
- a supposed architecture necessity depends on an unresolved F-finding that can be preserved as an unknown → preserve it, do not turn it into a research blocker.

## 14. Canonical output

Persist the substantive result as a new versioned conception artifact rather than overwriting historical prior art.

Preferred target:

`docs/architecture/fresh-rebuild-conception-20260923.md`

It should contain at minimum:

1. current-state inventory;
2. accepted Requirement / responsibility map used for the conception;
3. Architecture Concerns / Quality Attributes;
4. F1–F14 / D4 constraint mapping;
5. technical research questions and SOTA/Existing-Tool evidence;
6. candidate approaches and trade-offs;
7. prior-plan disposition;
8. fresh target responsibility/architecture conception;
9. migration/no-migration strategy;
10. explicit unknowns / spikes / ADRs;
11. acceptance/evaluation strategy;
12. dependency-driven implementation proposal;
13. non-goals and forbidden assumptions;
14. exact handoff to implementation planning/execution.

Update #92/#48 with concise pointers/status only. Update `PROJECT_STATE.md` if the phase or next allowed action changes.

Do not create a new issue unless a genuinely independent Work Owner/DoD is required under #23.

## 15. Completion condition

The conception is complete only when a fresh competent implementer can answer from the repository:

- what the system is being rebuilt toward and why;
- which accepted Requirements and project findings justify each material responsibility;
- which parts of the old plan were retained/adapted/rejected/deferred/tested;
- which technical choices are decisions vs hypotheses vs spikes;
- which scientific/epistemic boundaries cannot be lost;
- which unknowns remain and how later work can discriminate them;
- what the dependency-driven implementation sequence is;
- what requires #58/#44/owner input;
- what the first implementation work package may be **after explicit implementation admission**.

Then stop before implementation.
