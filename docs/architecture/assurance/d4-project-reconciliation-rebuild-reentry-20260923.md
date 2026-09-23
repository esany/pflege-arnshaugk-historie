# Histo-Orla — D4 project reconciliation and rebuild re-entry decision

**Date:** 2026-09-23  
**Review owners:** #64 (project finding disposition), #92 (re-entry gate)  
**Inputs:** PR #125; D4 / PR #126; current repository evidence and owner evidence cited therein  
**Authority:** `project-review disposition / re-entry decision only` — no Requirement, Method, Architecture, Selection, Roadmap, Delivery or implementation authority

## 1. Scope, evidence roles, and decision boundary

This is the required project-side reconciliation of the F1–F14 disposition in PR #125 with D4 external research. It preserves pointwise findings and counterfindings; it does not turn them into a common root cause or a solution synthesis.

`PE` = repository/incident/test/documented project behaviour; `OE` = persisted owner/workflow feedback; `ER` = D4 scholarly or standards evidence; `RS` = D4 related-system evidence; `RI` = this review's inference; `OH` = open hypothesis. D4 supplies `ER`/`RS` and explicitly marked `RI`; it does not itself gain Requirement or Architecture authority.

**Phase boundary:** this decision ends at `architecture-relevant concerns, constraints, protected distinctions, forbidden assumptions, and unknowns`. A fresh later work context under #48/#42/#59 may derive concerns from those inputs. It must not inherit an earlier solution synthesis, and this artifact does not derive a design.

## 2. D4 admissibility review

| Check | Result | Basis / limit |
|---|---|---|
| F1–F14 coverage and split mechanisms | PASS | D4 §§2, 3, 6 treats every finding, including F2a/b, F3a/b, F5a/b/c and F13a/b. |
| Intended research clusters R-A–R-H | PASS | D4 §3 covers all eight clusters; §5 preserves their cross-cluster separations. |
| Theory, empirical material, counterevidence and transfer limits | PASS for this bounded transition | Present per cluster; D4 distinguishes full text, abstract, specification and related-system inspection. It is not an exhaustive review. |
| PE/OE versus ER/RS | PASS | D4 §§1.4–1.5 and each reconciliation distinguish evidence roles; AI prose is explicitly not evidence. |
| Claim discipline and inspection status | PASS | D4 §1.3 says no claim relies on title/snippet alone and gives inspection notation; sources used only as abstracts remain marked. |
| Foreign-population transfer | PASS with qualified scope | Health-care, safety, scientific-workflow and software-team results transfer only at named mechanisms, not as population equivalence. |
| Unresolved questions and execution mode | PASS | D4 records `browser-assisted` rather than unavailable dedicated Deep Research mode and names remaining external/PE gaps (§§7–9). This is a limitation, not a hidden substitution. |
| No solution synthesis | PASS | D4 stops before architecture, workflow, technology, roadmap, selection or implementation. |
| Current CI for D4 head | PASS | `project-assurance` completed successfully on `dfc3857` (runs `35783759160` and `35783755019`). |

**Admissibility disposition:** D4 is sufficient as a bounded external-research input to this reconciliation. No identified defect changes a finding disposition or prevents deriving later concerns. It is neither independent specialist validation nor a warrant for a particular solution.

## 3. Pointwise final project disposition

| Finding | Pre-D4 disposition | D4 result | Final project disposition | Evidence basis | What may now be assumed | What must **not** be assumed | Remaining gap |
|---|---|---|---|---|---|---|---|
| F1 needs visible early | STRENGTHEN | downstream transformation has ER support | STRENGTHEN | PE/OE + ER | early needs were materially visible; downstream translation is a legitimate concern | needs prove sufficient/currently prioritized requirements or delivery success | PROJECT-EVIDENCE-GAP: need-to-outcome trace in live work |
| F2a premature problem-partition promotion | STRENGTHEN / REFRAME | exploratory inquiry supports revisable framing | REFRAME | PE + ER | provisional frames may be necessary; durable partitions need situated support | all early categories/modules/phases were wrong or structure is harmful | DESIGN-TESTABLE-UNKNOWN: case-level intrinsic inquiry versus avoidable promotion |
| F2b representation-maintenance burden | KEEP | representation benefit and lifecycle cost both supported | STRENGTHEN | PE + ER | durable representations can generate maintenance/reconciliation work | that every representation is net burden or F2a's causal mechanism | PROJECT-EVIDENCE-GAP: use, revision, consumer and manual-sync burden |
| F3a protective loss-boundary formalization | NEW / SPLIT | provenance and boundary-object analogues support protection | STRENGTHEN | PE + ER | non-equivalence and explicit `unresolved` can preserve epistemic optionality | each existing boundary is optimally scoped or formalization settles interpretation | DESIGN-TESTABLE-UNKNOWN: scope/proportionality of individual boundaries |
| F3b constraining problem-partition formalization | NEW / SPLIT | premature commitment and viscosity support distinct risk | SPLIT | PE + ER | loss boundaries and problem partitions serve different functions | ontology/classification is generally forbidden | DESIGN-TESTABLE-UNKNOWN: when a partition becomes constraining |
| F4 specialization / coordination rebound | STRENGTHEN | coordination literature supports broker/rebound mechanism | STRENGTHEN | PE/OE + ER | semantically sound specialization may impose operational integration cost | boundaries are wrong, or this is F9's temporal burden | PROJECT-EVIDENCE-GAP: local dependency/broker-time evidence; software-population transfer limit |
| F5a secondary control work | KEEP | control/handoff work can create secondary surfaces | STRENGTHEN | PE + ER | a control has a cost that must be assessed with its loss model | control count/document count proves net burden | PROJECT-EVIDENCE-GAP: control-specific time, false-block and understanding data |
| F5b recursive error→rule loop | DOWNGRADE | full recursion not externally or independently reproduced | DOWNGRADE | bounded PE + ER + OH | specific episodes can be investigated as a historical project hypothesis | a global recursive causal loop exists | PROJECT-EVIDENCE-GAP: episode timeline, recurrence and counterfactual evidence |
| F5c protective control value | STRENGTHEN | safety/provenance analogues support protective function | STRENGTHEN | PE + ER | a control can be worth secondary work where it prevents a defined loss | all controls are proportionate or F6 disappears | PROJECT-EVIDENCE-GAP: observed prevention/recovery performance |
| F6 local verification / global utility gap | STRENGTHEN | verification/validation distinction strongly supported | STRENGTHEN | PE/OE + ER | local conformance does not establish end-to-end research value | controls/local checks are useless or owner impressions alone establish utility | PROJECT-EVIDENCE-GAP: task/outcome measures correlated with owner value |
| F7 readiness / admission conflation | KEEP separate | contracts, freshness and fitness-for-use distinguish predicates | STRENGTHEN | PE + ER | existence, traceability, availability, admission, currency and fitness must not be silently collapsed | a general documentation/governance problem, or a fixed number of states | DESIGN-TESTABLE-UNKNOWN: smallest useful readiness vocabulary; PE incident classification |
| F8 premature semantic promotion | REFRAME; mirroring downgraded | lifecycle mechanism supported; causal label not isolated | REFRAME | PE/OE + ER + OH | owner language/context should remain traceable without becoming untested durable semantics | AI sycophancy/mirroring caused a project event | PROJECT-EVIDENCE-GAP: discriminate collaboration, anchoring, pressure, persistence and AI effects |
| F9 restart / handoff burden | KEEP separate | resumption cues help; excess handoff information can burden | STRENGTHEN | PE/OE + ER | continuity across time has a distinct benefit/cost trade-off | it is F4, or more context is always better | DESIGN-TESTABLE-UNKNOWN: task-specific minimum sufficient context |
| F10 evidence-led reframing | NEW / STRENGTHEN | berrypicking/sensemaking support revisable inquiry | STRENGTHEN | PE + ER | evidence can legitimately alter terms, questions and units of work | arbitrary/repeated non-learning churn is justified | DESIGN-TESTABLE-UNKNOWN: normal reframing versus avoidable project error |
| F11 visible correction / recovery | NEW | recovery is conditional, not automatic, evidence | REFRAME | PE + ER | visible reversal can show detection/recovery when recurrence or recovery cost improves | correction count proves health or instability | PROJECT-EVIDENCE-GAP: detection latency, recurrence and recovery-time evidence |
| F12 AI amplification | DOWNGRADE / qualified | AI can shift production/validation balance; causality remains open | UNRESOLVED | ER + PE + OH | AI effects require end-to-end, task-specific assessment | AI is the primary cause of the structural pattern, or irrelevant | PROJECT-EVIDENCE-GAP: local causal/comparative evidence |
| F13a owner as workflow integrator | KEEP | integration labour is supported | KEEP | OE/PE + ER | cross-tool/state integration work is observable and may be measured | all integration is accidental rather than scholarly judgment | PROJECT-EVIDENCE-GAP: essential judgment versus accidental coordination |
| F13b human as semantic compiler | DOWNGRADE | stronger stable-role claim lacks direct support | DOWNGRADE | OH + limited PE/ER | this remains a question, not a settled role diagnosis | the system ought to replace a human semantic compiler | DESIGN-TESTABLE-UNKNOWN: nature and recurrence of mediation work |
| F14 orchestration friction / bottleneck rank | KEEP mechanism; rank downgraded | friction is real; no comparative rank | UNRESOLVED | OE/PE + ER | interface/orchestration friction is a candidate measurable constraint | it is Histo-Orla's dominant bottleneck | PROJECT-EVIDENCE-GAP: comparative delay/effort/outcome data across constraints |

## 4. Required separations retained

This reconciliation retains, rather than averages, the following non-equivalences: F2a ≠ F2b; F3a ≠ F3b; F4 ≠ F9; F5a ≠ F5b ≠ F5c; F6 ≠ a verdict against controls; F7 ≠ documentation/governance burden; F8 ≠ proven AI sycophancy; F10 ≠ arbitrary churn; F11 ≠ automatic health; F12 ≠ AI-primary causation; F13a ≠ F13b; and F14 mechanism ≠ bottleneck rank. No stronger evidence than D4 was found that permits a merger.

## 5. Remaining gaps classified by consequence

| Material unknown | Class | Why it does not block re-entry |
|---|---|---|
| Intrinsic exploratory reframing versus avoidable framing error | DESIGN-TESTABLE-UNKNOWN | later work can preserve revisability and formulate a bounded discrimination without presupposing the answer |
| Net burden/benefit of representations and controls | PROJECT-EVIDENCE-GAP | D4 establishes the dual mechanism; local use, recovery and burden evidence belongs in validation/acceptance |
| Essential scholarly integration versus accidental coordination | PROJECT-EVIDENCE-GAP | a concern can be stated without deciding which activities should disappear |
| Minimal sufficient restart context | DESIGN-TESTABLE-UNKNOWN | known cue benefit permits concern derivation; task-specific minimum remains open |
| F5b full recursive-loop causality | PROJECT-EVIDENCE-GAP | no global causal claim is needed to retain control-cost/recovery concerns |
| F8 causal mechanism and F12 AI-primary causality | PROJECT-EVIDENCE-GAP | promotion/validation asymmetry is enough to state a concern without attributing a root cause |
| F7 optimal readiness granularity | DESIGN-TESTABLE-UNKNOWN | predicate separation is established; cardinality is not |
| F11 recovery versus churn | PROJECT-EVIDENCE-GAP | correction remains conditional evidence and can be evaluated locally |
| F14 actual bottleneck ranking | PROJECT-EVIDENCE-GAP | architecture concerns need not be ranked as a delivery plan before evidence exists |
| Transfer from software/health-care/related systems | NON-BLOCKING-UNKNOWN | D4 restricts transfer to named mechanisms and does not inherit foreign workflows or stakes |

**RESEARCH-BLOCKER:** none. Each remaining material uncertainty can be preserved without assuming an answer; none prevents #48 from formulating an architecture concern from accepted requirements, current repository reality and these constrained findings.

## 6. Architecture handoff — inputs only

### 6.1 Established constraints / protected distinctions

**CONSTRAINT:** Source, Instance, Derivative, Findspot and Finding; AI output and evidence; and `unresolved` and false remain non-equivalent.  
**BASIS:** PE + D4 ER.  
**DOES NOT IMPLY:** a database, schema, package or product topology.

**CONSTRAINT:** Protective loss-boundary formalization and constraining problem-partition formalization must be evaluated separately.  
**BASIS:** PE + ER.  
**DOES NOT IMPLY:** formalization is always good or always harmful.

**CONSTRAINT:** Local verification and global research/workflow utility require different evidence.  
**BASIS:** PE/OE + ER.  
**DOES NOT IMPLY:** removal of deterministic controls or replacement of validation with opinion.

**CONSTRAINT:** Existence, provenance, availability, admission, currency and fitness-for-operation are distinct claims.  
**BASIS:** PE + ER.  
**DOES NOT IMPLY:** a fixed state model or maximal control surface.

**CONSTRAINT:** Preserve reversibility where inquiry may reframe the working problem; do not silently promote provisional language or partitions.  
**BASIS:** PE/OE + ER.  
**DOES NOT IMPLY:** no durable representation or no specialization.

**CONSTRAINT:** Evaluate secondary coordination, control and restart work against their protected loss/continuity value.  
**BASIS:** PE/OE + ER.  
**DOES NOT IMPLY:** that any one burden is the dominant bottleneck.

### 6.2 Forbidden inherited assumptions

- A vertical research slice is already the right primary unit of research work.
- The operational core's form, a shared runtime/product package, or any package topology is established.
- A read model, SQLite, FTS, Skill, MCP or UI is a default next step.
- Orchestration is the dominant bottleneck, AI the primary cause, or the owner a proven semantic compiler.
- More formalization is inherently harmful, fewer controls inherently better, or visible correction inherently means instability.
- Existing #92 / PR #119 planning waves are an execution authority.

Rejecting these inherited premises does not establish their opposites.

### 6.3 Open architecture unknowns

- Which problem boundaries require durable representation and which must remain provisional?
- What local evidence would show that a boundary/control reduces more loss or effort than it adds?
- Which readiness predicates are needed for a bounded operation without state proliferation?
- What task-specific context is sufficient for reliable resumption?
- Which integration work is irreducibly scholarly and which is accidental coordination?
- Which outcome measures distinguish local conformance from research/workflow value?
- What is the comparative constraint profile before any bottleneck ranking?
- Under what local evidence, if any, does AI change end-to-end validation or integration capacity?

## 7. #92 gate decision and integration state

**Research Reconciliation Status:** `COMPLETE`  
**Rebuild Re-entry Status:** `READY`

The exact #92 condition is met epistemically: D4 is persisted and admissible for this bounded purpose; every current F1–F14 finding now has a project disposition; material unknowns are classified; and #48 can derive later architecture concerns without treating earlier solution synthesis as authority.

`READY` does **not** authorize architecture conception in this task, requirements changes, delivery selection, implementation, or resurrection of R4–R8. It does not assert that the unknowns are resolved.

**Repo / PR Integration Status:** `COMPLETE`.

- PR #125 was merged to `main` as `ec9736c8649fd1f94e053f863efcd0d2de07d09e` after successful `Project Assurance` run `35779487893`.
- PR #126 was rebased semantically onto the integrated PR-#125 state and merged to `main` as `09b938dc56b3db3795f40232375991e90f3cb195` after successful `Project Assurance` run `35864983824`.
- The stacked Research→Rebuild evidence is therefore integrated. `REPO-INTEGRATION-PENDING` is no longer an active project state.
- `PROJECT_STATE.md` now carries the integrated handoff state.

**Exact next allowed phase:** `Fresh rebuild conception under #48/#42/#59 from accepted Requirements + current repository reality + reconciled F1–F14 project findings + D4 external research.` It begins with concern derivation and retains every constraint and unknown above. It is not implementation authority.

## 8. Handoff check

Material change: the D4 input is pointwise reconciled with F1–F14 and #92's epistemic re-entry decision is explicit. Its canonical home is this #64/#92 review/assurance artifact; #64 and #92 carry concise pointer/status updates. D4 evidence, project evidence and RI remain separated. No new issue is required. The stacked PRs are integrated, `REPO-INTEGRATION-PENDING` is no longer active, and a new work context can continue from this artifact without using this chat.
