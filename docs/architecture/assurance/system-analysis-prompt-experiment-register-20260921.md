# System-analysis prompt experiment register — pre-comparison evidence freeze

**Freeze date:** 2026-09-21  
**Work Owner / review context:** #64  
**Research quality:** #45  
**Status:** empirical provenance register / pre-comparison freeze / no interpretation of independent fresh-chat result  
**Authority:** no Requirement, Method, Architecture, Selection or Delivery authority

## 1. Purpose

This register freezes the provenance of the analysis attempts that existed **before** the separate fresh-chat result is introduced into the present work context.

The purpose is experimental hygiene:

- preserve prior outputs instead of retrospectively rewriting them;
- distinguish self-audit, seeded/contaminated analysis and intended independent replication;
- record methodological failures in the experiment design itself;
- prevent later convergence/divergence analysis from laundering prior knowledge into an allegedly independent run.

**Hard boundary at freeze:** the owner has reported that a fresh-chat run of the generic prompt has completed. Its findings have **not** been supplied to or read in this work context at the time of this register. No claim about their content is made here.

## 2. Terminology

### Independent in the experimental sense

A run is called **independent** here only if its analytical result was produced without first consuming the prior Histo-Orla self-diagnoses that are later being compared against it, except where those materials are encountered naturally under the unchanged generic prompt itself.

### Seeded / contaminated

A run is **seeded/contaminated for replication purposes** when the prompt, work context or analyst already contains the target diagnoses, expected mechanisms or a prior report whose convergence is later of interest.

This does **not** mean the run is scientifically worthless. It means it cannot serve as an independent replication of those same diagnoses.

### Process evidence

Prompt-design mistakes, owner corrections and aborted experiment designs are retained as evidence about the analysis process even when they produced no research report.

---

# 3. Frozen experimental instrument

The generic analysis prompt produced in the originating chat is frozen at:

`docs/architecture/assurance/generic-system-problem-analysis-prompt-v1-20260921.md`

Creation commit on this provenance branch:

`3117eb512e6fbfe84707f7d2b656c3fb1dfa05b7`

Important limitation:

- the file preserves the prompt body produced in the originating chat;
- the exact wrapper/preamble actually pasted into the separate fresh chat has not yet been independently captured in the repository;
- therefore exact stimulus identity between this file and the fresh-chat invocation remains **owner-reported / not yet independently verified**.

No result from the fresh chat is included in this register.

---

# 4. Pre-existing evidence chronology

## E0 — Corrective self-audit, PR #116

**Type:** self-audit / corrective analysis  
**Date:** 2026-09-20  
**PR:** #116 — `Audit: consolidate owner user research and self-correct operationalization`  
**Merged head:** `8b5f343cd0a910dc62355336c84032d897e382af`  
**Canonical artifact:**  
`docs/architecture/assurance/chat-operationalization-self-audit-20260920.md`  
**Blob SHA on main:** `73c0a1a023c04261f84c3f0e9c9479cc5e98656a`

**Experimental status:** **not independent**.

Reason:

- it explicitly reviews the assistant's own prior handling of Owner/User-Research input;
- it knows the intervention sequence it is auditing;
- it generated diagnoses such as overly fast abstraction and `Owner signal → assistant abstraction → repo persistence`.

**Use later:** prior/self-diagnostic evidence only, never an independent replication result.

---

## E1 — First socio-technical Deep Research, PR #118

**Type:** seeded deep research / architecture-oriented research  
**PR:** #118 — `Deep research: derive socio-technical research architecture from current failure loops`  
**Created:** 2026-09-20  
**Current head at freeze:** `5c39a346037e7a1615e9a91ce39f06be86bd7f3b`  
**Canonical artifact:**  
`docs/architecture/assurance/sociotechnical-research-architecture-deep-research-20260920.md`  
**Blob SHA at current PR head:** `47831204c8d384bebcf9ce7f6bb81ed5a8edccaa`

**Prompt provenance:** #64 issue comment  
`https://github.com/esany/pflege-arnshaugk-historie/issues/64#issuecomment-5752243617`

That prompt explicitly required reading, among other materials:

- #64;
- #70;
- `chat-operationalization-self-audit-20260920.md` / PR #116;
- `shared-research-state-audit-20260919.md`;
- the #108–#117 correction chronology.

It also seeded the problem framing with already named risks such as:

- Meta-/Governance complexity;
- Human-as-Workflow-Engine;
- premature abstraction;
- second truth stores;
- pilot fossilization;
- assurance-success laundering.

**Experimental status:** **seeded / contaminated for any later replication test of those diagnoses**.

This is not a defect relative to its original purpose: PR #118 was intentionally a research continuation from an already articulated problem analysis. It is simply not an independent test of the later generic prompt.

**Important branch history:** later #119 calibration findings modified/corrected parts of PR #118. Git history and #64 comment `5753133321` preserve that correction chain.

---

## E2 — In-chat attempted application of the new generic prompt, PR #120

**Type:** second-order systemic audit in the same informed chat  
**PR:** #120 — `Deep audit: recurring socio-technical project-development patterns`  
**Created:** 2026-09-21  
**Final current head at freeze:** `9045f282a152711a83e8e72e499d212db4546765`  
**Canonical artifact:**  
`docs/architecture/assurance/systemic-project-development-pattern-deep-audit-20260921.md`  
**Blob SHA:** `822ebeab42969140f89459c9a7cbf109c647af6b`

Relevant preserved commits from the run:

- initial report commit: `409b63dcdee1f4a9aff4aa8a82e21bd842f2c322`;
- index/update state: `ac181f2cb169d11d318959ecfee4773d52beeeb9`;
- final citation/wording correction: `9045f282a152711a83e8e72e499d212db4546765`.

**Experimental status:** **not independent / contaminated**.

Reason:

the work context had already consumed and used:

- #70;
- #116;
- PR #118;
- #119 and its corrected execution assumptions;
- existing #64 diagnoses.

The PR body currently uses the phrase “independent, transdisciplinary analysis”. That phrase describes intended critical stance, but is **experimentally misleading** if read as independence from the prior diagnosis. This register supplies the explicit correction without rewriting the historical report.

PR #120 remains useful as:

- a second-order audit of the existing diagnosis;
- an external literature challenge;
- a record of how the informed chat elaborated the known problem.

It must not be counted as a blind or independent replication.

---

## E3 — Experiment-design contamination after the owner requested a truly independent test

**Type:** process evidence / aborted design, no research report  
**Medium:** originating chat  
**Date:** 2026-09-21

Sequence preserved here because it was not otherwise canonical:

1. Owner clarified that the purpose was not another diff/reinterpretation report but an **independent test of what the new generic analysis prompt itself can do**.
2. Assistant correctly recognized PR #120 as methodologically contaminated.
3. Assistant then proposed a new-chat “blind replication” instruction that added:
   - explicit blind phases;
   - a list of forbidden prior artifacts;
   - prescribed reconstruction order;
   - later reconciliation categories.
4. Owner rejected this too, because these additions again **changed/interpreted the experimental stimulus** instead of testing the generic prompt unchanged.
5. Assistant acknowledged that the clean experiment must be:
   `fresh chat + repository + unchanged generic prompt`, without added expected mechanisms or blind-phase instructions.

**Experimental status:** **aborted / no result**.

**Why it matters:** this is direct process evidence that the assistant twice responded to a request for a pure prompt test by adding its own methodological structure. It is evidence about the development/analysis process, but not evidence about the fresh-chat result.

Because the raw chat transcript is not itself a repository artifact, this section is a **contemporaneous provenance summary**, not a verbatim transcript.

---

## E4 — Fresh-chat generic-prompt run

**Type:** intended independent prompt test  
**Date:** 2026-09-21  
**Status at this freeze:** **owner reports completed; result intentionally not ingested here yet**.

Known at freeze:

- a separate fresh ChatGPT conversation was used;
- the owner reports that the generic prompt was run there;
- the findings have not yet been supplied to this work context.

Not yet established here:

- exact pasted wrapper/preamble;
- exact repository snapshot/head observed by that chat;
- exact set/order of repository artifacts it consumed;
- external search corpus and sources;
- model/tool execution trace;
- output artifact path/branch/PR, if any;
- the findings themselves.

These must be captured from the fresh-chat output/repository evidence **after** this pre-comparison freeze, without back-editing E0–E3.

---

# 5. Comparison firewall

Before E4 findings are introduced:

- E0–E3 classifications above are frozen as pre-comparison provenance;
- PR #116, #118 and #120 remain unchanged as historical source artifacts;
- no E4 finding is to be used to rewrite their original claims;
- later comparison must distinguish:
  - prior finding;
  - independent finding;
  - post-hoc reconciliation;
  - convergence;
  - divergence;
  - non-reproduction;
  - new finding;
  - unresolved comparability.

If E4 turns out to have read PR #118/#120 or equivalent summaries naturally under the unchanged prompt, that fact does not invalidate the prompt test; it changes the **interpretation of independence** and must be recorded empirically rather than retroactively hidden.

---

# 6. Current evidence completeness assessment

At freeze, the earlier material is preserved at three levels:

1. **raw/versioned report artifacts:** yes for E0–E2;
2. **Git/PR chronology:** yes for E0–E2, including corrective history;
3. **experimental provenance / contamination classification:** this register supplies the previously missing layer.

Remaining gaps:

- exact fresh-chat invocation text is not yet repository-verified;
- exact fresh-chat execution/repository observation trace is not yet captured;
- E3 raw chat transcript is not in Git; only this contemporaneous provenance summary is persisted;
- the E4 findings are deliberately excluded until after this freeze.

---

# 7. Handoff rule

A later comparison must start from this register and the frozen prompt stimulus before reading E4 findings.

It must not silently reinterpret E0–E2 as independent runs merely because their reports use critical or independent-review language.

No project decision follows from this register.
