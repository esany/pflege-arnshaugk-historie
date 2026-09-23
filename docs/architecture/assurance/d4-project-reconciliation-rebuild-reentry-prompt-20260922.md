# Histo-Orla — D4 project reconciliation and rebuild re-entry prompt

**Date:** 2026-09-22  
**Purpose:** reconcile D4 external research into the current project problem model and decide the #92 rebuild re-entry gate  
**Authority:** review/reconciliation only; no Requirement, Method Truth, Architecture, Selection, Delivery or implementation authority

---

Work exclusively in the repository `esany/pflege-arnshaugk-historie`.

This task is **not another Deep Research run** and **not yet the rebuild/architecture phase**.

Its sole purpose is to reconcile the completed D4 external research against the current Histo-Orla F1–F14 project findings, preserve all material distinctions/counterfindings, classify remaining unknowns, and determine whether the explicit #92 Research→Rebuild re-entry condition is satisfied.

Do not smooth the findings into an averaged narrative.

---

# 1. Mandatory fresh bootstrap

Before substantive work, freshly read in this order:

1. root `AGENTS.md`;
2. root `PROJECT_STATE.md`;
3. root `README.md`;
4. issue #64;
5. issue #92, especially the current Re-entry Gate;
6. PR #125 and:
   `docs/architecture/assurance/repeated-system-audits-project-implications-20260922.md`;
7. PR #126 and:
   `docs/research/audits/d4-problem-driven-external-research-20260922.md`;
8. #45 only insofar as needed to assess whether D4 met the project Research-quality boundary;
9. #42/#48/#59 and current Architecture/Requirements contracts only as needed to judge the later re-entry boundary.

Freshly resolve current PR/branch/merge state.

Do not infer current project state from this prompt or prior chat.

Repository precedence applies.

---

# 2. Exact phase boundary

Current sequence:

```text
F1–F14 project analysis
→ D4 external research
→ THIS project reconciliation
→ #92 re-entry decision
---------------- HARD BOUNDARY ----------------
later:
fresh rebuild conception under #48/#42/#59
→ technical SOTA/options
→ architecture decisions
→ implementation
```

Therefore this task must **not**:

- design a target architecture;
- propose a new workflow;
- select a product topology;
- decide Core/package/UI/MCP/read-model structure;
- select AI/agent roles;
- create an implementation roadmap;
- prioritize delivery;
- change accepted Requirements;
- create Method Truth;
- select current work;
- authorize implementation.

The task may identify **architecture-relevant concerns, constraints, forbidden assumptions and unresolved unknowns**, because these are the handoff into the later architecture phase.

It must not solve them.

---

# 3. Primary question

Answer:

> **What is the current project-level disposition of F1–F14 after D4, which findings are now strong enough to become inputs/constraints for later architecture reasoning, which remain unresolved hypotheses or project-evidence gaps, and does that state satisfy #92’s Research→Rebuild re-entry condition?**

Do not answer this by averaging the findings.

Process each finding independently first.

Only afterwards inspect cross-finding implications.

---

# 4. Evidence roles

Keep strictly distinct:

- **PE — Project Evidence:** repository events, issues, code, tests, incidents, documented workflow behaviour;
- **OE — Owner Evidence:** documented owner needs, corrections, workflow feedback;
- **ER — External Research:** scholarly/standards evidence from D4;
- **RS — Related-System Evidence:** documented systems/cases from D4;
- **RI — Researcher Inference:** analytical conclusion;
- **OH — Open Hypothesis:** plausible but not sufficiently discriminated.

D4 is external-research evidence plus researcher synthesis.

D4 does **not** itself have Requirement or Architecture authority.

PR #125 is the pre-D4 project finding disposition.

This reconciliation decides the current **review/problem-model disposition**, not technical design.

---

# 5. First task — quality/admissibility review of D4

Do not redo the full literature search.

Check whether D4 is sufficiently usable for this project transition.

At minimum verify:

- F1–F14 coverage is complete;
- R-A–R-H cover the intended problem clusters;
- theory, empirical evidence, counterevidence and transfer limits are materially present;
- inspection status is visible;
- project evidence and external evidence are not conflated;
- D4 does not cross into solution synthesis;
- important claims are not based only on snippets/titles;
- major transfer from other populations is qualified;
- material unresolved questions are explicit;
- D4’s execution-mode limitation is recorded;
- Project Assurance/CI status for PR #126 is freshly checked rather than relying on the local checkout statement.

If a material D4 defect would change the project reconciliation, mark exactly that defect.

Do **not** request another broad research run merely because some literature remains incomplete.

---

# 6. Second task — pointwise F1–F14 reconciliation

For every current project finding, compare:

1. pre-D4 project disposition from PR #125;
2. D4 external disposition;
3. current PE/OE;
4. remaining limits.

Use the following disposition vocabulary:

- `STRENGTHEN`
- `KEEP`
- `REFRAME`
- `SPLIT`
- `DOWNGRADE`
- `FALSIFY`
- `RESOLVED/HISTORICAL`
- `UNRESOLVED`

Do not invent a weaker generic label if one of these captures the evidence.

For split findings, preserve the child mechanisms separately.

## Required table

For every F1–F14 and existing sub-findings such as F2a/F2b, F3a/F3b, F5a/F5b/F5c, F13a/F13b record:

| Finding | Pre-D4 disposition | D4 result | Final project disposition | Evidence basis | What may now be assumed | What must NOT be assumed | Remaining gap |

The columns **What may now be assumed** and **What must NOT be assumed** are essential.

They form the safe handoff into architecture without designing architecture.

---

# 7. Preserve the distinctions D4 strengthened

Explicitly test that the reconciliation does not collapse the following:

- F2a premature problem-partition promotion ≠ F2b representation-maintenance burden;
- F3a protective loss-boundary formalization ≠ F3b constraining problem-partition formalization;
- F4 specialization/coordination rebound ≠ F9 temporal restart/handoff burden;
- F5a secondary control work ≠ F5b recursive error→rule loop ≠ F5c protective control value;
- F6 local verification/global utility ≠ “controls are useless”;
- F7 readiness/admission ≠ general documentation or governance burden;
- F8 premature semantic promotion ≠ AI sycophancy as proven cause;
- F10 evidence-led reframing ≠ arbitrary churn;
- F11 visible correction/recovery ≠ automatic project health;
- F12 AI amplification ≠ AI-primary causation;
- F13 workflow integration ≠ proven “semantic compiler” role;
- F14 real orchestration friction ≠ proven dominant bottleneck.

If the reconciliation merges any of these, justify it with stronger evidence than D4; otherwise keep them separate.

---

# 8. Third task — classify remaining gaps by their consequence for rebuild conception

Do **not** treat every unresolved research question as a blocker.

Classify every material remaining gap as exactly one of:

### A. `NON-BLOCKING-UNKNOWN`
Architecture may proceed if it preserves the uncertainty and does not assume an answer.

### B. `DESIGN-TESTABLE-UNKNOWN`
The later architecture phase may formulate reversible options/experiments that discriminate it.

### C. `PROJECT-EVIDENCE-GAP`
External research is sufficient, but Histo-Orla lacks local evidence. Carry the gap explicitly into later validation/acceptance.

### D. `RESEARCH-BLOCKER`
Architecture concerns cannot be responsibly derived without additional external research.

Use `RESEARCH-BLOCKER` sparingly and only with a concrete explanation of what decision would otherwise be unsafe or ill-posed.

Examples D4 currently leaves open include:
- intrinsic exploratory reframing vs avoidable project framing error;
- essential scholarly integration vs accidental coordination;
- minimal sufficient restart context;
- actual bottleneck ranking;
- causal status of F5b;
- AI-primary causality.

Do not assume these are blockers merely because they are unresolved.

---

# 9. Fourth task — derive the architecture handoff, not the architecture

Produce a concise list of **architecture-relevant handoff statements** in three categories.

## 9.1 Established constraints / protected distinctions

These are things later architecture reasoning must preserve unless new evidence overturns them.

Example form:

```text
CONSTRAINT:
Source / Instance / Derivative / Findspot / Finding non-equivalence remains protected.

BASIS:
PE + D4 ER.

DOES NOT IMPLY:
a particular database/schema/product topology.
```

## 9.2 Forbidden inherited assumptions

These are assumptions from earlier #92/PR #119/PR #118 solution synthesis that may no longer be carried forward as premises.

Examples to examine:

- fixed Vertical Slice is the correct primary unit of research work;
- “Operational Core” shape is already established;
- shared runtime/package is the natural destination;
- read model / SQLite / FTS is a later default;
- Skill/MCP/UI is a default destination;
- orchestration is the dominant bottleneck;
- AI is the primary root cause;
- more formalization is inherently harmful;
- fewer controls are inherently better;
- every correction indicates instability.

Do not decide the opposite.

Simply state which old premises are no longer valid starting assumptions.

## 9.3 Open architecture unknowns

List unresolved questions the architecture phase must carry without pretending they are solved.

No solution options yet.

---

# 10. Fifth task — assess the #92 re-entry gate explicitly

Evaluate the exact #92 condition:

> the next problem-driven Deep Research has been persisted and reconciled against the current F1–F14 finding disposition, and #48 can derive architecture concerns from that reconciled evidence without inheriting the earlier solution synthesis as authority.

Return **two separate statuses**:

## Research reconciliation status

Choose exactly one:

- `COMPLETE`
- `INCOMPLETE`

## Rebuild re-entry status

Choose exactly one:

- `READY`
- `NOT-READY`

`READY` means:

- D4 is sufficiently admissible for the current purpose;
- F1–F14 have explicit final project dispositions;
- remaining gaps are classified and can be preserved as unknowns;
- architecture concerns can be derived without pretending those unknowns are solved;
- old solution synthesis is not being inherited as authority.

`READY` does **not** mean:
- architecture is already known;
- all research questions are solved;
- implementation may start;
- #92’s previous roadmap becomes active again.

If `NOT-READY`, identify the **minimal exact blockers**.

Do not answer `NOT-READY` just because unresolved questions remain.

---

# 11. Sixth task — repository/PR integration state

PR #126 is stacked on the PR #125 branch.

Freshly determine:

- whether PR #125 is open/merged;
- whether PR #126 is open/merged;
- whether their merge order/dependency is clear;
- whether current `PROJECT_STATE.md` on main is stale;
- whether the reconciliation can be canonically persisted without creating competing truth.

Do not silently describe an open branch as merged project truth.

If the research is epistemically ready but branch integration is pending, report this separately as:

`REPO-INTEGRATION-PENDING`

This is not the same as `Research reconciliation INCOMPLETE`.

---

# 12. Required canonical output

Persist one concise project-reconciliation artefact, preferably under the existing #64/#92 review/assurance surface, containing:

1. D4 admissibility review;
2. final F1–F14 disposition table;
3. remaining-gap classification;
4. established constraints;
5. forbidden inherited assumptions;
6. open architecture unknowns;
7. Research reconciliation status;
8. Rebuild re-entry status;
9. repo/PR integration status;
10. exact next allowed phase.

Do not create a new issue unless repository governance requires a genuinely independent Work Owner.

Update #64 and #92 only with concise status/pointers.

Update `PROJECT_STATE.md` if and only if the handoff state materially changes.

---

# 13. Status transition rules

If:

```text
Research reconciliation = COMPLETE
AND
Rebuild re-entry = READY
```

then #92 may be changed from:

`hold-for-research-reconciliation`

to a status equivalent to:

`research-reconciled / ready-for-fresh-rebuild-conception / no implementation authority`

Do **not** reactivate the old R4–R8 sequence.

The next action becomes:

> fresh rebuild conception under #48/#42/#59 from accepted Requirements + current repository reality + reconciled project findings + D4 external research.

If the gate is not satisfied, leave #92 on hold and state the minimal missing evidence/reconciliation work.

---

# 14. Hard stop

Even if the gate becomes READY, **STOP before architecture conception**.

Do not in the same task:

- propose architecture options;
- research technical stacks;
- rewrite the roadmap;
- reactivate PR #119;
- select a work package;
- implement code.

The next chat/work package will perform the rebuild conception from the now-reconciled evidence.

---

# 15. Handoff check

Before completion confirm:

- What materially changed?
- Where is the canonical disposition?
- Are #64/#92 statuses/pointers current?
- Are D4 evidence and project inference distinguishable?
- Are remaining unknowns visible without being averaged away?
- Is the exact next allowed action visible?
- Can a fresh competent chat continue using only the repository?

If not, complete the repository handoff before finishing.
