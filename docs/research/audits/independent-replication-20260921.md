# Independent replication audit — blind analysis

**Work Owner:** #121  
**Date:** 2026-09-21  
**Status:** `blind-independent-analysis / frozen-before-reconciliation`  
**Repository:** `esany/pflege-arnshaugk-historie`  
**Purpose:** independent reconstruction and external research; **not** solution design, roadmap, target architecture, prioritization, or normative synthesis.

## A. Investigation frame

### A.1 Experimental boundary

This document was completed **before intentionally opening or using** the diagnostic content of Issue #64, Issue #70, PR #116, PR #118, and PR #120. Those items are reserved for a later, separately versioned reconciliation.

The blind condition is not perfect. Two contamination channels were unavoidable or accidental:

1. mandatory fresh bootstrap required reading `PROJECT_STATE.md`, which contains brief current-state references to later audits, including #64/#70;
2. a broad fetch of comments on Development owner #59 returned one later comment referring to PR #118.

Those later diagnostic statements were excluded from the evidentiary basis below, were not used as search terms for external research, and were not used to name the mechanisms below. The experiment is therefore **source-blinded with documented contamination**, not double-blind.

The user-supplied experimental prompt itself named several candidate anti-patterns. Those names are treated as experiment instructions, not evidence.

### A.2 Fresh bootstrap and canonical project basis read

Freshly read from GitHub before analysis:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `README.md`
- Work Owner #121
- Research Protocol #45
- `docs/research/source-identity-protocol.md`

Additional allowed project evidence included Issues #1–#63 except intentionally blocked #64/#70, selected issue comments, canonical discovery/requirements/research-design artefacts, live research owners, commit history, and concrete implementation/assurance records.

### A.3 Evidence classes

The analysis distinguishes:

- **Project Evidence (PE):** repository artefact, issue, commit, code/test/CI record, or documented behaviour.
- **Owner Evidence (OE):** documented Research Owner need, pain, correction, acceptance or non-acceptance.
- **External Research Evidence (ER):** scholarly literature, standards, empirical studies.
- **Related-System Evidence (RS):** documented behaviour/design of real systems or research infrastructures.
- **Researcher Inference (RI):** interpretation derived from evidence.
- **Open Hypothesis (OH):** plausible explanation not yet sufficiently discriminated.

### A.4 Limits

This is a single-repository case study over an unusually short, AI-intensive development period (2026-08-29 to 2026-09-21). Commit frequency is **not** interpreted as effort or dysfunction by itself. The repository is highly instrumented, so it exposes corrections that less explicit projects might hide. Some owner statements are already normalized into repo artefacts rather than raw conversation transcripts. No claim is made that this case generalizes to software projects in general.

---

# B. Independent project reconstruction

## B.1 Reconstructed owner need before technical structure

The strongest recurring need is not “build a knowledge graph”, “build agents”, “use RAG”, or “formalize a research workflow”. The repository repeatedly states a more operational requirement:

> a Research Owner with substantial historical interest but without needing to pre-possess every specialist vocabulary, disciplinary routing decision, retrieval technique, software choice, or archival method should be able to conduct rigorous, source-anchored, transdisciplinary historical research while retaining challengeability and control.

Evidence:

- **PE:** Issue #1: the user may ask imprecisely; the system should translate to appropriate professional concepts, methods and evidence rules.
- **PE:** Issue #13: the user “soll nicht selbst wissen müssen, welche Fachdisziplin zuständig ist”.
- **PE:** `docs/research/discovery/problem-baseline.md`: G-002/N-001/P-001 and N-002/P-007 explicitly encode missing terminology and missing ability to determine the responsible discipline as system needs/pains.
- **PE:** G-009/P-014 require scientific complexity to remain understandable and expert-auditable rather than being simplified into false certainty.
- **PE:** P-009 identifies repeated mechanical source/file/search work as consuming time that does not require scholarly judgement.
- **PE:** Issues #2/#4/#5 require source/findspot fidelity, OCR/search assistance, historical variants and repeatable retrieval.
- **PE:** Issues #9/#45 and the source-identity protocol require evidence/provenance boundaries, uncertainty, and durable non-chat state.
- **RI:** The target experience is therefore asymmetric: the system is expected to absorb *operational and translation complexity* while leaving irreducible scholarly judgement and strategic choice visible to the owner.

This distinction matters because later project structure can be evaluated against a need that is more specific than “rigorous research”: rigorous research **with reduced unnecessary orchestration load**.

## B.2 Initial solution hypotheses were explicitly unstable

Very early Issues #2–#8 already contain retractions or demotions of concrete solution ideas:

- personal archivist demoted from whole-system target to specialist role (#2);
- Zotero demoted from sole source of truth to bibliographic/reference layer (#3);
- Git storage of OCR extracts demoted from requirement to architecture hypothesis (#4/#6);
- semantic search/RAG demoted from fixed component to optional hypothesis (#5);
- fixed methods/phase assumptions in early concept material were marked superseded (#7 and later research-design history).

**PE:** these changes were recorded on 2026-08-30, within roughly one day of repository creation.

**RI:** Early correction pressure was not caused only by later implementation complexity. It already existed at the problem-to-solution translation boundary: plausible tools/metaphors were repeatedly found to be too specific to carry the underlying need.

## B.3 Discovery-to-requirements was broad and fast

The first formal chain was executed under #27:

`#28 Problem/Need → #29 Workflows → #30 Research Questions → #31–#39 SOTA → #40 Risks → #41 Capabilities/Quality → #42 Requirements → #43 Architecture Readiness`.

Commit chronology shows these artefacts being created in a compressed period around 2026-08-30/31. The requirements baseline commit `168ceb038a...` created a 763-line baseline with explicit traceability and acceptance conditions.

This is not by itself evidence of low quality. AI-assisted drafting can compress elapsed time. Two facts are nevertheless important:

1. live research #46/#47 was still actively discovering method and workflow constraints;
2. the architecture gate was shortly afterwards reframed, then an MVP steering layer was installed and removed on the same day.

**OH:** the formal synthesis may have reached representational closure faster than real-use uncertainty had stabilized.

Counterevidence: the requirements explicitly preserve `unresolved`, separate evidence classes, forbid AI-as-evidence, and later changes were accepted as deltas rather than silently overwritten.

## B.4 Episode: architecture gate → lean/MVP layer → rapid removal

### Trigger

#43 initially concluded `architecture-ready-with-bounded-research-debt`. The owner then judged a renewed heavyweight gate to be inappropriate for a private lean/agile project and authorized “build now, harden while using” (DD-001 under #44).

### Interpretation/intervention

A rapid sequence of commits introduced an MVP framing, acceptance criteria, coverage and steering artefacts:

- `f14d6d...` Shift phase reconciliation to lean agile MVP delivery
- `1b5230...` Define owner-accepted lean MVP acceptance criteria
- `741448...` Adopt lean agile MVP delivery mode
- `538ff9...` Reframe architecture as just-in-time lean MVP support

### Immediate benefit

The intervention made time-to-use and reversible delivery explicit and broke a potentially open-ended pre-development gate.

### Side effect and correction

Within the same day another sequence removed the MVP layer:

- `cc451c...` Remove MVP phase framing and restore content-driven workflow
- `c153...` Remove MVP framing...
- `72afe...` Remove MVP steering layer
- `941d...` Remove MVP from root
- `4a253...` Deprecate MVP acceptance before removal
- `9c882...` Remove retired MVP acceptance layer
- `03ae...` Remove retired MVP delivery ledger
- `45c5...` Consolidate domain-derived system requirements without MVP layer

DD-002 records the reason: the MVP layer had begun to overlay the already-developed requirement state and repeatedly introduced phase/scope semantic drift.

### Independent inference

**RI — strongly supported:** A process concept introduced to reduce delivery friction became an additional semantic layer that itself required reconciliation and removal. The problem is not “MVP is bad”; it is **a steering abstraction becoming a second interpretation layer over an already rich accepted state**.

Alternative explanation: the correction is evidence that governance worked exactly as intended—an unsuitable abstraction was detected early and cheaply.

## B.5 Episode: rapid assurance expansion

On 2026-09-01 the repository added, in rapid succession:

- deterministic requirements assurance (#62): schema, validator, tests, CI;
- value/decision/delivery/feedback assurance (#63): governance registry, trace schema, trace data, policy, validator, tests, CI;
- rules connecting implementation to accepted requirements and upstream Goals/Needs/Pains.

### Why it was plausible

The repository had already observed accidental semantic drift, stale state, and the risk that AI/technical work could silently promote assumptions. Deterministic checks protect formally decidable boundaries without claiming historical truth.

### Positive mechanism

- formal PASS is explicitly separated from scholarly validation and owner acceptance;
- negative tests encode known failure classes;
- the system preserves non-regression and makes restartability stronger;
- owner feedback becomes a durable record rather than disappearing in chat.

### Side effects observed almost immediately

**OE, #63 / FB-20260901-002:** GitHub Actions failures caused unwanted email noise. The documented cause included avoidable red intermediate states from serially writing logically coupled changes to `main` plus overlapping workflow triggers. The correction required atomic/branch-first changes and workflow-trigger separation.

**RI:** assurance did not merely reduce risk; it introduced a new operational surface whose coupling, notification and sequencing behaviour itself had to be engineered.

This is not evidence against assurance. It is evidence that assurance is a socio-technical component with its own failure modes and maintenance cost.

## B.6 Episode: real PDF use exposes formal-value gap

**OE, #63 / FB-20260902-003:** real Lampe-PDF use found that the research operation remained too manually/chat-orchestrated despite accepted requirements. The record identifies:

- long manually maintained Markdown artefacts;
- old annotations;
- insufficient generated human-readable research views;
- little automated Context/Trace/Derive work.

The record explicitly says no new scholarly requirement was discovered; rather, existing accepted UX/workflow/state goals were insufficiently realized in delivery.

**RI — strongly supported:** The project could be formally well-specified and increasingly well-guarded while the owner-facing research loop still required substantial manual integration. This is a **formal-state / lived-work divergence**, not a failure of the scientific requirements themselves.

Counterevidence: #63 exists precisely to record this divergence; the project did not equate green CI with product acceptance.

## B.7 Episode: static module framing rejected in live research

**OE, #63 NOT PASS, 2026-09-03:** while continuing U2/Sachenbacher work, an earlier “modular research/search inventory” framing was rejected as too static and not fitting the target understanding.

Owner-accepted working movement became:

`Source → statement → scope → uncertainty → follow-up question → next test trail`

instead of:

`Source → module → routing → search hook`.

### Independent interpretation

This is one of the clearest natural experiments in the repository.

- A pre-structured organizational representation was plausible as a way to make work manageable.
- In situated research, it pulled attention toward classifying evidence into a module framework.
- The owner preferred a dynamic, claim/evidence/uncertainty-driven progression in which the next step emerges from what the source actually says and does not say.

**RI — strongly supported:** The mismatch is between **pre-enumerated work structure** and **evidence-contingent inquiry**, not between “structure” and “no structure”.

## B.8 Episode: live U2 repeatedly changes what counts as the right unit of work

Issue #46 and its research artefacts show several concrete corrections produced by source work:

- early string/place search was widened into variant-aware and source-context analysis;
- Moxa evidence revealed family property, dotal rights, heirs, guarantees, ecclesiastical authority, war as procedural constraint, patronage and memoria in one charter complex;
- the owner explicitly corrected the research from locality/single-document hits toward time-slices, lordship layers, actor networks, institutional function, legal forms, economy/resources, conflict and falsification questions;
- unclear user forms were kept unresolved rather than silently normalized;
- `Knau` homonyms and 1374/1378 dating were kept separate/unresolved rather than harmonized.

**RI:** real evidence does not only fill predefined slots; it changes the useful analytical partition. That is an empirical reason to treat some workflow/category structures as provisional and revisable.

## B.9 Episode: owner mental model promoted too literally

Commit `1a6b76c6ba...` and #63 owner feedback on 2026-09-19 record a process regression: examples/metaphors from owner conversation were prematurely promoted into canonical target/Requirement/architecture language (the “historical knowledge space” case).

The correction explicitly requires first classifying owner input as one of:

`Observation / Goal / Need / Pain / Mental Model / Research Question / Constraint / Quality Attribute / Capability Hypothesis / Feature Idea / Solution Hypothesis`

before domain/SOTA/requirements routing.

**RI — strongly supported:** In this project, the owner’s ability to articulate an experience metaphor is **not** reliable evidence that the metaphor should become the internal object model. The user-research interface itself is a recurring semantic risk surface.

## B.10 Episode: mutation and repository mechanics become a work source

The commit history contains multiple sequences of accidental overwrite/no-op/restore/revert activity, notably around 2026-09-03 and again later. #44 DD-20260903-001 records that local mutation guards could not prevent direct GitHub Contents-API writes to unprotected `main`; real prevention required server-side branch protection/rulesets that the available connector could not configure.

This evidence supports a narrower claim:

**PE:** repository mutation mechanics and connector limits generated consequential operational work independent of historical research.

It does **not** prove that the project architecture caused those failures. A substantial portion may be tool/environment-specific.

---

# C. Problem / mechanism map

## C.1 Mechanism M1 — representation ratchet

**Observed phenomenon:** an ambiguous need or open uncertainty is often converted into a named artefact, owner, schema, contract, or status transition. Once created, that representation itself creates consistency and update obligations.

**Evidence:** #23 ownership topology; #42 requirement truth; #60 method truth; #61 context; #62/#63 assurance; repeated PROJECT_STATE/coverage/trace reconciliation; MVP layer creation/removal.

**Possible mechanism:** explicitness improves restartability but increases the number of representations that must remain mutually consistent.

**Alternative explanations:**
- high artefact count may simply expose necessary domain distinctions;
- the project deliberately optimizes for cross-chat restartability, so some duplication of navigational views is intentional;
- many artefacts are projections rather than independent truth stores.

**Amplifiers:** AI can generate formal artefacts much faster than a human can absorb or validate their combined interaction; frequent project-state updates increase coupling.

**Counteracting factors:** one-fact/one-canonical-home rule; generated/projection distinction; deterministic validators; Work Owner model.

**Confidence:** supported.

## C.2 Mechanism M2 — situated-work mismatch

**Observed phenomenon:** fixed phase/module/category models are repeatedly corrected after live source work.

**Evidence:** early specialist-role demotions; same-day MVP removal; U2 static-module NOT PASS; Sep19 mental-model correction; live #46 method widening.

**Mechanism:** exploratory historical research discovers relevant vocabulary, entities, relations and discriminating questions during interaction with sources; a structure chosen before that interaction can become a constraint rather than a support.

**Alternative explanations:** individual bad abstractions rather than a generic issue; better-designed pre-structures may work.

**Counteracting factors:** keeping `unresolved`; live research as falsification; reversible architecture; explicit candidate→accepted transitions.

**Confidence:** strongly supported for several concrete structures, not for all formalization.

## C.3 Mechanism M3 — formal-value gap

**Observed phenomenon:** formal validity/CI/restartability can improve without equivalent improvement in owner-facing research flow.

**Evidence:** #62/#63 explicitly distinguish formal pass from acceptance; FB-20260902-003 reports manual/chat orchestration after formal baseline and assurance existed; synthetic verification was repeatedly distinguished from real case use.

**Mechanism:** technical/formal tests measure invariants that are necessary but incomplete proxies for research utility.

**Alternative explanation:** this was an expected maturation stage; formal foundation may be prerequisite to later usability.

**Counteracting factors:** owner-feedback records, real-use acceptance, NOT PASS status.

**Confidence:** strongly supported.

## C.4 Mechanism M4 — coordination surface generated by quality controls

**Observed phenomenon:** new guards/traceability reduce one class of error while adding coupling, notification, sequencing and maintenance work.

**Evidence:** FB-20260901-002; DD-20260903-001; repeated assurance synchronization.

**Mechanism:** every control that depends on multiple artefacts adds coordination requirements; if technical/work dependencies are not aligned, local changes require non-local updates.

**Alternative explanation:** early setup cost that amortizes later; GitHub connector constraints are external.

**Confidence:** supported, with uncertain long-run net effect.

## C.5 Mechanism M5 — correction instrumentation

**Observed phenomenon:** the repository records reversals, unresolved findings, negative tests, non-PASS states and owner corrections unusually explicitly.

**Evidence:** #44 DD-002; #63 NOT PASS; source-identity protocol; #45; #46; negative assurance tests; archived superseded artefacts.

**Mechanism:** visible falsification and preservation of superseded state increase apparent churn while lowering risk of silent error.

**Alternative explanation:** instrumentation can also become self-referential work.

**Confidence:** strongly supported as a positive mechanism.

## C.6 Mechanism M6 — evidence-led reframing

**Observed phenomenon:** live source encounters repeatedly generate richer or different analytical units than initial task lists.

**Evidence:** U2 Moxa/Triptis/network corrections; source→statement→scope→uncertainty loop; observation-first corrections in later real cases.

**Mechanism:** sources act as discriminating evidence not only for historical claims but for the adequacy of the research workflow itself.

**Alternative explanation:** current live cases may be unusually complex and not representative of simpler retrieval tasks.

**Confidence:** strongly supported for U2; cross-case generality unresolved.

## C.7 Mechanism M7 — AI/tool throughput can outrun semantic validation

**Observed phenomenon:** large formal structures and linked artefacts are produced quickly; later owner/live-use corrections discover semantic mismatch or integration cost.

**Evidence:** compressed #28→#43 chain; rapid MVP creation/removal; repeated accidental connector writes; Sep19 owner-input promotion error.

**Mechanism:** generation/mutation has low marginal cost while semantic validation remains bottlenecked by domain fit and owner experience.

**Alternative explanation:** elapsed time and output volume are not measures of cognitive review; AI may also reduce validation cost.

**Confidence:** plausible/supported, but causal attribution to AI specifically is not proven.

---

# D. Need → system translation audit

| Owner need / uncertainty | Observed system translation | Fit | Evidence / qualification |
|---|---|---|---|
| “I do not know the right historical/archival terminology.” | problem translation, terminology layers, expertise routing | strong fit | #1/#13/#28; later U2 variants validate need |
| “I should not need to know which discipline is responsible.” | expertise profiles, domain owners, routing logic | partial fit | conceptual fit strong; owner still carries significant integration burden |
| repeated mechanical source/search work should be absorbed | OCR/retrieval/provenance/tooling requirements | partial fit | needs are well captured; FB-20260902-003 says operation remained too manual |
| uncertainty/contradiction must survive | explicit `unresolved`, discrepancy/search-boundary states | strong fit | #42/#45/#46; repeatedly used productively |
| research must be inspectable/challengeable | source/instance/findspot/derivative/finding separation + audit | strong fit | source identity protocol and real case corrections |
| durable state must survive chats/models | GitHub canon, work owners, restartability | strong fit conceptually; operational cost non-trivial | frequent recovery/reconciliation work |
| owner mental models should communicate desired experience | sometimes promoted into product/system structure too directly | misfit in observed Sep19 case | explicit owner correction |
| “work should flow from source evidence” | at times replaced by static modules/inventories | misfit in observed Sep3 case | explicit NOT PASS |
| “lean/private/agile” delivery preference | temporarily translated into additional MVP governance layer | weak fit in that episode | DD-002 removed the layer |
| human control without micromanagement | detailed authority/trace controls | conditional fit | controls improve challengeability; real workflow still required manual orchestration |

### D.1 Key distinction

The project often translates **epistemic uncertainty** well: unresolved identities, competing interpretations, provenance and search boundaries survive.

The harder translation is **operational uncertainty**: when the owner does not know which technical/fachliche choice should be made next, the system has sometimes answered by creating more explicit structure that the owner then has to integrate, review, or correct.

This claim is supported but not universal: branch guards, exact retrieval baselines and source identity constraints demonstrably remove decision burden rather than merely document it.

---

# E. Domain complexity

## E.1 Clearly essential complexity

Strongly supported as intrinsic to the historical research domain:

- source vs edition/regest/digital instance/derivative;
- precise findspots and inspection status;
- historical orthography, names and homonyms;
- source dependence and transmission history;
- uncertainty and contradiction;
- claim-specific evidentiary scope;
- changing geographic/political scales;
- multiple disciplinary methods;
- archival provenance and institutional/registrarial logic;
- distinction between explicit source statement and later motive/interpretation.

Removing these distinctions would reduce scientific validity.

## E.2 Complexity whose source is mixed or uncertain

- number of Work Owners and cross-owner handoffs;
- multiple trace/projection artefacts;
- requirement/coverage/assurance synchronization;
- branch/CI/mutation ceremony;
- manually curated long Markdown research views.

These may encode necessary safety properties, accidental technical constraints, or both.

## E.3 Complexity transferred to the owner

Direct owner evidence supports at least:

- manual chat orchestration;
- long manual Markdown maintenance;
- correcting static conceptual frames;
- correcting premature promotion of conversation metaphors;
- handling CI notification noise.

The amount of burden eliminated later by automation is not fully measured in the repository.

---

# F. Technology analysis

## F.1 Robust technical-semantic boundary

The source identity protocol and accepted requirements consistently separate:

`Source → representation/instance → derivative → findspot/excerpt → observation/finding → interpretation`.

This separation is repeatedly useful in U2 and later technical work. It prevents a common failure mode: turning OCR, catalogue metadata, editorial identification or AI output into historical fact.

**Independent finding:** not all formalization is showing the same failure pattern. This particular formalization appears to reduce semantic ambiguity without forcing research closure.

## F.2 Deterministic core vs probabilistic assistance

Issue #24 and requirements distinguish deterministic identity/provenance/status/invariants from probabilistic/LLM-supported exploration. External standards and HAI literature are consistent with this separation, but they do not prove that the exact local architecture is optimal.

## F.3 Technical debt / operational defects

Observed classes include:

- accidental repository mutations and restores;
- missing server-side branch protection;
- CI trigger/noise problems;
- authentication/publication blockers;
- synthetic checks preceding real workflow evidence.

These defects are real but heterogeneous. They should not be collapsed into one “architecture failure” narrative.

---

# G. Organization / governance analysis

## G.1 What governance demonstrably succeeds at

- preserving authority boundaries;
- recording `unresolved`;
- preventing technical tests from being called scholarly validation;
- preserving owner corrections;
- making requirement/decision lineage inspectable;
- enabling restarts by new agents/chats;
- isolating actual blockers rather than asking the owner to decide every uncertainty.

## G.2 What governance can cost

- each new formal owner/artefact adds a potential synchronization edge;
- controls can produce non-domain work (CI noise, trace maintenance);
- a formally correct local change can leave other views stale;
- the owner can become final integrator when multiple specialized states remain separately correct but jointly difficult to use.

The repository itself contains controls intended to reduce these costs, so the relevant question is not “more or less governance?” but **whether each control removes more coordination/semantic burden than it creates in the actual research loop**. This analysis does not answer that quantitatively.

---

# H. Interface analysis

## H.1 Human ↔ AI

Strong project rule: AI output is assistance, not evidence or independent validation. This boundary is scientifically protective.

Observed risk is elsewhere: AI can generate plausible *system interpretations* of owner language and rapidly materialize them into artefacts. The Sep19 correction shows that this can happen before fachliche/user-research classification.

## H.2 User ↔ expert method

Target state is explicitly asymmetrical: user need not know the discipline; the system should route expertise. Live U2 shows this can work when source evidence triggers method widening. It fails when the system instead asks the owner to validate a prebuilt conceptual decomposition.

## H.3 Domain ↔ software

The strongest interface contracts are those that encode loss boundaries (source identity, findspot, unresolved status) rather than theories of historical interpretation.

## H.4 Requirement ↔ implementation

Traceability is unusually strong. Utility traceability remains weaker because real-use acceptance arrives later than formal implementation checks.

## H.5 Evidence ↔ state

This is one of the most mature interfaces: source identity, inspected instance, derivative and finding are actively separated.

## H.6 Component ↔ system

Issue topology supports local ownership, but the repeated need for reconciliation suggests non-trivial hidden coupling among “canonical truth + projections + coverage + current state”. The magnitude is not yet quantified.

## H.7 Research ↔ development

Live cases improve requirements and method truth, but development and assurance often create structures before enough real-case evidence exists. Both directions are visible; neither fully dominates.

---

# I. Independent external state of the art

The literature search started from the observed mechanisms above rather than later Histo-Orla diagnoses.

## I.1 Requirements engineering and user involvement

### Inayat et al. 2015 — agile requirements engineering systematic review
Irum Inayat et al., “A systematic literature review on agile requirements engineering practices and challenges”, *Computers in Human Behavior* 51 (2015), 915–929. DOI: 10.1016/j.chb.2014.10.046.

**Evidence type:** systematic literature review (21 included papers, literature through June 2013).  
**Finding relevant here:** agile RE practices can overcome several traditional RE challenges but introduce new challenges; the review identified 17 practices, 5 overcome challenges and 8 challenges introduced by agile RE.  
**Transferability:** moderate. Histo-Orla is an unusual solo-owner/AI-mediated research software case, not a conventional agile team.  
**Relevance:** supports the symmetric interpretation that iterative/lean requirements can reduce premature freezing while creating coordination and non-functional-requirement problems. It does **not** support “agile is better” or “formal RE is worse”.

### Bano & Zowghi 2015 — user involvement systematic review
Muneera Bano, Didar Zowghi, “A systematic review on the relationship between user involvement and system success”, *Information and Software Technology* 58 (2015), 148–169. DOI: 10.1016/j.infsof.2014.06.011.

**Evidence type:** systematic review of empirical studies.  
**Finding:** the empirically observed relationship between user involvement and system success was not uniformly positive.  
**Relevance:** owner involvement is necessary evidence but not a guarantee that examples or preferences should be translated literally into requirements. The *quality, timing, interpretation and role* of involvement matter.

### ISO/IEC/IEEE 29148:2018
Current 2018 Requirements Engineering standard, confirmed in 2024 and under revision in 2026.

**Evidence type:** international standard.  
**Relevant property:** requirements processes are iterative/recursive across the lifecycle; the standard distinguishes requirements engineering processes and information items rather than treating a one-time requirements document as final truth.  
**Transferability:** high at principle level, low for any specific Histo-Orla artefact topology.

## I.2 Human-centred design and situated action

### ISO 9241-210:2019
Human-centred design standard for interactive systems.

**Evidence type:** international standard.  
**Finding:** design should focus on users, their needs and requirements throughout the lifecycle, with iterative human-centred activities.  
**Relevance:** owner-facing research flow is a first-class quality dimension, not inferable from internal correctness alone.

### Suchman 2006/2012 — plans and situated actions
Lucy Suchman, *Human-Machine Reconfigurations: Plans and Situated Actions*, Cambridge University Press.

**Evidence type:** foundational ethnomethodological/HCI analysis, not a software experiment.  
**Finding:** plans are resources for practical deliberation and retrospective/projective accounts; situated action cannot be fully prescribed by abstract structures detached from circumstances.  
**Relevance:** strong conceptual fit to the U2 module rejection and evidence-contingent next-step formation.  
**Limit:** does not imply that plans/workflows are useless; it challenges treating them as complete causal prescriptions.

### Kuhlthau — Information Search Process
Carol Kuhlthau’s ISP model synthesizes longitudinal and large-sample information-seeking research.

**Finding:** uncertainty often increases during exploration before focus formulation; information seeking is constructive, not just collection; premature movement from selection directly to collection can bypass necessary exploration.  
**Relevance:** strong fit to a historical research system in which “not knowing” is normal input rather than an exception to be eliminated immediately.  
**Limit:** much empirical work comes from library/education/workplace information seeking, not AI-assisted historical scholarship.

### Bates 1989 — berrypicking
Marcia J. Bates, “The Design of Browsing and Berrypicking Techniques for the Online Search Interface”, *Online Review* 13(5), 407–424. DOI: 10.1108/eb024320.

**Finding:** real search often evolves through successive partial discoveries; the query itself changes.  
**Relevance:** supports source-driven search expansion and cautions against treating an initial research query/module as stable.

### Russell, Stefik, Pirolli & Card 1993 — sensemaking
“The cost structure of sensemaking”, CHI/INTERACT 1993. DOI: 10.1145/169059.169209.

**Finding:** sensemaking involves searching for useful representations and encoding data into them; representations shift to reduce task costs.  
**Relevance:** suggests a more discriminating interpretation than “formalization is bad”: representations are valuable when they reduce downstream cognitive operations, and harmful when they increase representation-maintenance cost or become hard to change.

### Green & Petre 1996 — Cognitive Dimensions
“Usability Analysis of Visual Programming Environments: A ‘Cognitive Dimensions’ Framework”, *Journal of Visual Languages & Computing* 7(2), 131–174. DOI: 10.1006/jvlc.1996.0009.

**Finding:** representational systems involve trade-offs such as closeness of mapping and viscosity (resistance to change).  
**Relevance:** the same-day MVP removal and cross-artefact synchronization are consistent with representation “viscosity”, but the framework is an analytic vocabulary, not causal proof.

## I.3 Coordination and socio-technical systems

### Schmidt & Bannon 1992 — articulation work
“Taking CSCW seriously: supporting articulation work”, *Computer Supported Cooperative Work* 1, 7–40. DOI: 10.1007/BF00752449.

**Relevance:** cooperative work requires work that coordinates and integrates the primary work itself. This offers a better-fitting lens for Histo-Orla than treating every extra artefact as simple bureaucracy: some meta-work is necessary articulation work. The empirical question is whether the system supports that articulation or exports it to the Research Owner.

### Cataldo, Herbsleb & Carley 2008 — socio-technical congruence
“Socio-Technical Congruence: A Framework for Assessing the Impact of Technical and Work Dependencies on Software Development Productivity”, ESEM 2008. DOI: 10.1145/1414004.1414008.

**Evidence type:** empirical software-engineering study/framework.  
**Finding:** coordination aligned with actual technical/work dependencies was associated with shorter modification resolution; simple modular decomposition does not eliminate coordination needs.  
**Relevance:** issue decomposition can look clean while cross-owner semantic dependencies remain. The key variable is alignment between dependency and coordination, not number of modules/issues alone.

### Star & Griesemer 1989 — boundary objects
“Institutional Ecology, ‘Translations’ and Boundary Objects”, *Social Studies of Science* 19(3), 387–420. DOI: 10.1177/030631289019003001.

**Finding:** heterogeneous scientific actors coordinate through standardization and boundary objects that are robust enough to retain identity while adaptable to local viewpoints.  
**Relevance:** Histo-Orla’s source identity, requirements and research views may function as boundary objects. The theory also warns that successful shared artefacts need local interpretive flexibility; a single rigid representation need not fit all disciplines.

## I.4 Human–AI interaction and AI-assisted development

### Amershi et al. 2019 — Guidelines for Human-AI Interaction
CHI 2019, DOI: 10.1145/3290605.3300233.

**Evidence:** synthesis plus multi-stage validation, including 49 design practitioners evaluating 20 AI-infused products.  
**Relevant mechanisms:** user control, appropriate correction, failure handling, and adapting AI behaviour to context/time.  
**Relevance:** supports Histo-Orla’s challengeability and correction mechanisms; does not say every AI action needs prior human approval.

### NIST AI RMF 1.0 / Playbook
NIST AI 100-1 (2023), current framework being revised in 2026.

**Relevant findings:** human roles/responsibilities should be explicitly differentiated; human-AI interaction outcomes vary; complex human phenomena can lose necessary context when represented in measurable models; oversight configuration should depend on context/risk.  
**Relevance:** consistent with separating domain authority, owner authority and AI assistance. Also cautions against using “human in the loop” as an unspecified catch-all role.

### Peng et al. 2023 — GitHub Copilot controlled experiment
“The Impact of AI on Developer Productivity: Evidence from GitHub Copilot”, arXiv:2302.06590.

**Finding:** participants with Copilot completed a bounded JavaScript HTTP-server task about 55.8% faster.  
**Transfer limit:** relatively bounded task, different from long-lived familiar repository maintenance.

### METR 2025/2026 — real-repository developer productivity
Joel Becker et al., “Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity” (METR, 2025).

**Finding:** 16 experienced maintainers working on 246 real tasks in repositories they knew well took 19% longer when AI tools were allowed, despite believing AI sped them up.

METR’s 2026 follow-up explicitly says newer data are confounded by selection effects and likely indicate improved AI usefulness, but cannot reliably quantify the change.

**Relevance:** together with the positive Copilot experiment, this is strong counterevidence to any blanket claim that AI either inherently accelerates or inherently impairs development. Task structure, repository context, prior knowledge, review standards and tool generation all matter.

## I.5 Research data, provenance and reproducibility

### Wilkinson et al. 2016 — FAIR
“The FAIR Guiding Principles for scientific data management and stewardship”, *Scientific Data* 3, 160018. DOI: 10.1038/sdata.2016.18.

**Relevant finding:** provenance, identifiers and domain-relevant standards support reuse; the authors explicitly say good data stewardship is a means to discovery/reuse, not a goal in itself, and FAIR principles precede implementation choices.

**Relevance:** strong support for Histo-Orla’s durable/provenance state; equally, FAIRness does not establish user-facing research utility.

### W3C PROV-O / PROV-DM (2013)
W3C Recommendation for interoperable provenance representation across entities, activities and agents.

**Relevance:** demonstrates that explicit provenance can be standardized without encoding domain interpretation as provenance truth. Fits the project’s source/derivative lineage boundary.

### RO-Crate 1.3 (2026)
Current recommendation published 2026-06-22; uses JSON-LD metadata to aggregate and contextualize research objects.

**Related-system lesson:** packaging/context/provenance can be made machine-readable and portable, but RO-Crate deliberately does not define the scholarly meaning of each domain’s findings.

---

# J. Related systems / comparative cases

## J.1 Tropy

Tropy is a desktop research-photo system that groups photos into source items, supports metadata, tags, notes/transcriptions and search, and exports JSON-LD/CSV/Omeka S. Its documentation explicitly states what it is **not**: not a citation manager, not a full writing platform, not an online presentation platform.

**Mechanism relevant to this case:** clear capability boundaries can hide low-level file complexity without claiming to own the entire research process.

**Transferability:** partial; Tropy handles archival-source organization, not transdisciplinary interpretation or AI orchestration.

## J.2 Galaxy

Galaxy’s scientific workflow platform records histories containing inputs, parameters, tool versions and outputs. Importantly, workflows can be **extracted from histories of analyses already performed**, not only designed in advance.

**Mechanism relevant to this case:** operational history can precede reusable workflow formalization. This is a concrete related-system example of formalizing from situated practice rather than requiring all practice to conform to a pre-existing workflow.

**Transferability:** conditional. Galaxy’s computational analyses are more repeatable/deterministic than historical interpretation.

## J.3 RO-Crate and W3C PROV

Both demonstrate portable structured metadata/provenance without making that structure a universal domain ontology.

**Mechanism:** a stable interop/provenance substrate can coexist with domain-specific interpretation layers.

## J.4 No direct “same system” comparator found

No reviewed related system combines all of Histo-Orla’s intended properties: expert-routing for historical scholarship, archival/source handling, durable provenance, AI-assisted interpretation, requirements traceability, and software-development self-governance. This limits any claim that one existing architecture constitutes established best practice for the whole problem.

---

# K. Contradictions and tensions

These are not resolved here.

1. **Auditability ↔ cognitive/coordination load**  
   More explicit state improves restartability and review but increases the number of things that can become stale.

2. **Formal safety ↔ situated research flow**  
   Guards prevent silent semantic loss; fixed stages/categories can obstruct inquiry when the next relevant question emerges from the source.

3. **Domain pluralism ↔ integrated user experience**  
   Separate authority domains protect method truth but can make the owner responsible for cross-domain integration.

4. **Automation ↔ human authority**  
   Automation can remove mechanical work, but over-automation can silently promote interpretations; under-automation leaves the human as workflow integrator.

5. **Modularity ↔ coordination cost**  
   Separate owners reduce local ambiguity but do not remove dependencies among their states.

6. **Durable project memory ↔ meta-work**  
   Canonical persistence prevents chat monopoly; maintaining many persistent views can become a secondary workload.

7. **Early structure ↔ discovery**  
   Structure improves searchability and tests; early structure can encode an incorrect partition of the research problem.

8. **Fast AI generation ↔ slow semantic validation**  
   AI can create documentation/code quickly; domain/owner validation remains contextual and may be the pacing constraint.

9. **High correction visibility ↔ appearance of churn**  
   A healthy system that records every reversal may look less stable than a system that silently forgets them.

---

# L. Counterevidence against a simple failure narrative

The repository contains strong counterevidence to a claim that it merely accumulates bureaucracy or abstraction:

- early tool/architecture hypotheses were repeatedly demoted rather than defended;
- `unresolved` is an accepted first-class state;
- AI output is explicitly prevented from becoming evidence;
- source identity/provenance distinctions survive repeated real-case testing;
- formal assurance repeatedly states its own limits;
- owner feedback is stored as Product/Workflow evidence, not historical truth;
- NOT PASS can invalidate a formally persisted approach;
- real cases actively alter research method and downstream technical work;
- the project removes governance layers (e.g. MVP layer) when they become misleading;
- branch/CI problems were treated as technical defects rather than rationalized as user error.

Therefore the strongest independent account is **not** “the project failed because it had too much governance”. It is that the project has a powerful correction apparatus whose own coordination footprint can sometimes compete with the owner-facing research experience it is intended to protect.

---

# M. Unresolved questions

1. How much owner time is actually spent on historical judgement vs coordinating artefacts/agents/tools? The repo has qualitative feedback but no time/interaction study.
2. Which formal artefacts are consulted in real work, and which mainly serve agent restart/assurance?
3. Does coordination cost decline after the current foundation stabilizes, or does each new capability keep adding comparable meta-work?
4. Which live cases besides U2 reproduce the static-structure mismatch?
5. Are repeated accidental Git/GitHub mutations primarily connector/tool failures or consequences of the project’s state topology?
6. Does generated human-readable view infrastructure measurably reduce manual Markdown work?
7. How many owner corrections result from incorrect scholarly reasoning versus incorrect translation of owner intent versus software/tool defects?
8. Which requirements were actually falsified by use, rather than merely extended?
9. Does the source/instance/findspot/finding model remain sufficient for heterogeneous non-text evidence (maps, LiDAR, archaeology, GIS)?
10. At what point does preserving restartability become cheaper than reconstructing context ad hoc?
11. Can the project distinguish “necessary articulation work” from avoidable coordination overhead empirically rather than rhetorically?
12. Are there countercases where a prebuilt module/workflow structure worked well and reduced owner burden? The current audit found positive formal structures (source identity, retrieval baseline) but not a strong positive example of a fixed research-module model.

---

# N. Research gaps

- empirical studies of single-owner, multi-agent/LLM-mediated scholarly software development are still sparse;
- classic coordination literature largely assumes human teams, not one human coordinating many transient AI work contexts;
- HAI guidelines address interaction quality more than durable epistemic provenance in humanities research;
- FAIR/PROV/RO-Crate address data/provenance portability but not evolving interpretive inquiry;
- developer-productivity studies for AI disagree by task/context and change rapidly with model/tool generations;
- no mature evidence base was found for the optimal amount of formal governance in AI-heavy personal research software.

---

# O. Confidence / evidence matrix

| Statement | Main evidence | Confidence | Counterevidence / alternative | Open question |
|---|---|---|---|---|
| Owner need includes system absorption of terminology/routing/mechanical complexity | #1/#13/#28/problem baseline | strongly supported | none material | exact desired interaction still evolving |
| Project repeatedly turns uncertainty into explicit artefacts/owners/contracts | issue topology, assurance history | strongly supported | much explicitness is scientifically necessary | net coordination cost |
| Some prebuilt steering/organizational structures were mismatched to real work | DD-002, U2 NOT PASS, Sep19 correction | strongly supported | other structures survived well | boundary between useful/over-early structure |
| Live source work is a major falsification mechanism | #46, owner corrections | strongly supported | U2 may be unusually rich | cross-case replication |
| Formal correctness can diverge from owner-facing utility | #62/#63 boundaries + FB-20260902-003 | strongly supported | project explicitly knows this | whether later delivery closed gap |
| Governance/assurance creates secondary operational work | CI noise, mutation guard, reconciliation | supported | may be temporary setup cost | long-run net effect |
| AI throughput specifically causes the above | chronology + external AI studies | plausible | causal evidence weak; tooling and project novelty confound | controlled comparison absent |
| Source/instance/derivative/findspot/finding separation is a robust positive mechanism | protocol + live case use | strongly supported | non-text evidence less tested | heterogeneous evidence |
| More user involvement alone would solve translation errors | Bano/Zowghi + Sep19 case | falsified as simple claim | quality/timing/interpretation matter | best involvement form |
| Less governance would necessarily improve the system | project recovery evidence + coordination literature | unsupported | governance prevents real errors | control-by-control net value |
| More automation would necessarily reduce owner burden | mixed project evidence, HAI literature | unresolved | automation can shift/obscure authority | task-specific allocation |
| Research flow is better modeled as evidence-contingent inquiry than fixed modules | U2 NOT PASS + Suchman/Bates/Kuhlthau | supported for exploratory research | deterministic processing pipelines differ | scope of applicability |

---

# P. Independent findings — frozen before reconciliation

The strongest independently supported findings are:

1. **The owner’s underlying need is not merely rigorous persistence; it is rigorous research with the system absorbing avoidable translation, routing and mechanical coordination burden.**
2. **The project is very good at preserving epistemic uncertainty, but less consistently good at absorbing operational uncertainty.** In several episodes, uncertainty became new explicit structure that then required owner/agent integration.
3. **Several abstractions became real work objects before situated evidence had stabilized their fit.** The clearest replications are the same-day MVP layer, the rejected U2 module framing, and the Sep19 literalization of an owner mental model.
4. **Real source work is the strongest observed corrective mechanism.** It repeatedly changes terminology, scope, method and next questions.
5. **Formal assurance and owner-facing utility are distinct.** The project knows this conceptually, yet real use still exposed the gap.
6. **Governance is neither simply the problem nor simply the solution.** It prevents semantic loss and preserves correction, while also creating coordination dependencies and operational failure surfaces.
7. **The source/provenance identity model is an important counterexample to “formalization is harmful”: it appears to encode stable loss boundaries rather than prematurely fixing historical interpretation.**
8. **The apparent churn is partly healthy falsification made visible.** A less instrumented project could hide the same errors instead of recording them.
9. **External research supports a situated, iterative interpretation of exploratory knowledge work and a context-dependent view of AI assistance.** It does not justify a single-cause narrative.
10. **A central unexplained variable remains the net owner burden:** the repo documents several pains and recoveries but does not quantify whether the total system is progressively reducing or merely redistributing that burden.

This document intentionally ends without an intervention, architecture, roadmap, recommendation, or “next step”. The later reconciliation may classify convergence/divergence with prior self-diagnoses, but must not rewrite this frozen independent result.

---

# References / external research boundary

- Inayat, I. et al. (2015). *A systematic literature review on agile requirements engineering practices and challenges*. Computers in Human Behavior 51, 915–929. DOI 10.1016/j.chb.2014.10.046.
- Bano, M.; Zowghi, D. (2015). *A systematic review on the relationship between user involvement and system success*. Information and Software Technology 58, 148–169. DOI 10.1016/j.infsof.2014.06.011.
- ISO/IEC/IEEE 29148:2018. *Systems and software engineering — Life cycle processes — Requirements engineering*.
- ISO 9241-210:2019. *Ergonomics of human-system interaction — Human-centred design for interactive systems*.
- Suchman, L. (2006/2012 online). *Human-Machine Reconfigurations: Plans and Situated Actions*. Cambridge University Press.
- Kuhlthau, C. Information Search Process theory and empirical programme.
- Bates, M. J. (1989). *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*. DOI 10.1108/eb024320.
- Russell, D. M.; Stefik, M. J.; Pirolli, P.; Card, S. K. (1993). *The cost structure of sensemaking*. DOI 10.1145/169059.169209.
- Green, T. R. G.; Petre, M. (1996). *Usability Analysis of Visual Programming Environments: A ‘Cognitive Dimensions’ Framework*. DOI 10.1006/jvlc.1996.0009.
- Schmidt, K.; Bannon, L. (1992). *Taking CSCW seriously: supporting articulation work*. DOI 10.1007/BF00752449.
- Cataldo, M.; Herbsleb, J. D.; Carley, K. M. (2008). *Socio-Technical Congruence...*. DOI 10.1145/1414004.1414008.
- Star, S. L.; Griesemer, J. R. (1989). *Institutional Ecology, ‘Translations’ and Boundary Objects*. DOI 10.1177/030631289019003001.
- Amershi, S. et al. (2019). *Guidelines for Human-AI Interaction*. CHI 2019. DOI 10.1145/3290605.3300233.
- NIST (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, plus current Playbook.
- Peng, S.; Kalliamvakou, E.; Cihon, P.; Demirer, M. (2023). *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. arXiv:2302.06590.
- Becker, J.; Rush, N.; Barnes, B.; Rein, D. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*. METR.
- Becker, J.; Rush, N.; Cunningham, T.; Rein, D.; Mahamud, K. (2026). *We are Changing our Developer Productivity Experiment Design*. METR.
- Wilkinson, M. D. et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. Scientific Data 3:160018. DOI 10.1038/sdata.2016.18.
- W3C (2013). PROV Data Model / PROV-O Recommendations.
- RO-Crate Community (2026). *RO-Crate Metadata Specification 1.3*, published 2026-06-22.
- Tropy documentation, current 2026.
- Galaxy Project / Galaxy Training Network, histories and reproducibility documentation, current 2026.
