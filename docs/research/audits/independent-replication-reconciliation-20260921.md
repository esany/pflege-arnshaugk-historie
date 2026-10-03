# Independent replication audit — reconciliation

**Work Owner:** #121  
**Date:** 2026-09-21  
**Status:** `reconciliation-after-frozen-blind-analysis`  
**Blind baseline:** `docs/research/audits/independent-replication-20260921.md` at commit `326178444528194e511688ae5e914aec0670c802`  
**Reconciliation sources opened only after that freeze:** Issue #64, Issue #70, PR #116, PR #118, PR #120; PR #119 was additionally inspected because PR #120 identified it as a distinct prior issue not reconstructed in the blind phase.

## 1. Method

This file does **not** revise the frozen independent analysis. It compares that analysis against the previously blocked Histo-Orla self-diagnoses.

Classification vocabulary:

- `independent convergence`
- `partial convergence`
- `novel independent finding`
- `contradiction`
- `prior finding not reproduced`
- `prior finding only weakly supported`
- `blind audit missed prior issue`
- `unresolved`

A convergence claim requires a trace from the frozen blind report to evidence that was already available without the blocked diagnostic source. Similar wording alone is not treated as replication.

## 2. Blindness limitations and their effect on interpretation

The experiment was not perfectly blind.

Before the freeze, the mandatory repository bootstrap exposed brief current-state references to later audits in `PROJECT_STATE.md`. A broad allowed fetch of #59 comments also surfaced one later PR #118 delivery summary. Those contents were explicitly excluded from the blind evidentiary basis and external-search framing, but their existence means the result should be described as **source-blinded with documented contamination**, not double-blind.

The user-provided experiment prompt also listed possible labels such as governance accretion, Human as Semantic Compiler, Need-to-Structure Inversion, premature abstraction, coordination rebound and meta-persistence. The blind report deliberately did not adopt these labels and instead generated its own mechanism names.

This matters most for broad convergence claims such as “governance creates coordination load”: the existence of a later audit was known. Independence is stronger for specific reconstructions that came from primary evidence and were not stated in the mandatory bootstrap, for example:

- the same-day MVP steering-layer creation and removal;
- FB-20260901-002 notification/CI friction;
- FB-20260902-003 manual/chat orchestration;
- the U2/Sachenbacher `NOT PASS`;
- the 2026-09-19 owner-mental-model promotion correction;
- the positive Source/Instance/Derivative/Findspot boundary;
- the external Suchman/Bates/Kuhlthau/Galaxy framing used by the blind analysis.

## 3. Source-specific reconciliation

### 3.1 Issue #64 — Product/Research Value vs Governance Complexity

#64 argues that Histo-Orla has strong explicit needs, authority and assurance boundaries, while governance/operationalisation complexity, handoffs and formal-success-vs-product-success are major risks. Later owner feedback sharpens this into “Governance-Sumpf”, research being hidden behind meta-state, over-broad “pilots”, mixed research/system-learning artefacts, and the need to distinguish historical output from system learning.

**Reconciliation:**

- The broad claim that formal/project structure can outrun owner-facing research utility is **independent convergence** with blind M3 `formal-value gap`.
- The claim that issue/owner decomposition can generate handoff cost is **independent convergence** with blind M1/M4 and the specialization↔coordination tension.
- The claim that formal green state is not product success is **independent convergence**; the blind analysis independently used #62/#63 boundaries and FB-20260902-003.
- The specific diagnosis that U1–U4 were wrongly cut as practical pilots with oversized DoDs is **prior finding not reproduced**. The blind audit found that live cases outperform abstract pre-structure, but did not independently derive the same pilot-boundary critique.
- The specific “5-minute handoff” usability criterion is **prior finding not reproduced**; the blind audit did not perform a timed navigation/usability study.
- The claim that historical research output and system-learning material are mixed in some live artefacts is **partial convergence**. The blind audit observed long/manual Markdown and integration burden, but did not independently perform the same artefact-product decomposition.

### 3.2 Issue #70 — AI-resilient root-cause audit

#70 explicitly describes a possible loop:

`AI error → new rule → new governance layer → more context/handoffs → new orientation errors → more rules`

and then separates symptom, protected goal, root cause, enforcement and eventual rule retirement. It also records concrete connector/write-boundary failures and later retirement of active audit machinery.

**Reconciliation:**

- The idea that controls can create their own coordination surface is **independent convergence** with blind M4.
- The claim that governance can be simultaneously protective and burden-producing is **independent convergence** with blind F6/G/K.
- The direct GitHub Contents/API bypass of local mutation protection is **independent convergence** at the mechanism level: the blind phase independently found DD-20260903-001, which already established that a local guard cannot prevent direct GitHub writes. #70 later supplies additional incident evidence (audit-branch truncation).
- The exact recursive `error → rule → context → new error` genealogy is **partial convergence**. The blind audit reconstructed assurance side effects and representation obligations, but did not independently derive #70's complete recursive rule-genealogy model.
- #70's dynamic competence-discovery comparison against `esany/Wissensarbeit` is **partial convergence**. The blind report independently reconstructed the need for problem-dependent expertise routing, but did not use the external repository comparator.
- #70's explicit rule-retirement result is a **prior finding not reproduced** as an empirical project outcome; the blind analysis recognized layer removal (especially MVP) but did not audit #70's retirement execution itself.

### 3.3 PR #116 — chat operationalization self-audit

PR #116 identifies a fast lifecycle:

`Owner signal → assistant abstraction → repo persistence`

instead of classification, alternative readings, domain/SOTA challenge, real-workflow challenge and only then possible promotion.

**Reconciliation:**

- Premature promotion of owner mental models is **independent convergence**. The blind report reconstructed the 2026-09-19 correction directly from the primary commit and classified it as a recurring semantic risk surface.
- “Architecture by metaphor” / literalization of a user mental model is **independent convergence** at the phenomenon level.
- PR #116's communication-specific `mirroring / affirmative abstraction` submechanism is **partial convergence**. The blind report observed fast coherent promotion but did not inspect the underlying chat language patterns (“Genau”, “das ist der Kern”) and therefore did not independently reproduce mirroring as the causal explanation.
- PR #116's cluster-specific meta-persistence analysis of #108–#115 is **partial convergence**. Blind M1 `representation ratchet` independently reaches a similar mechanism from broader project evidence, but it did not reconstruct that exact PR sequence.

### 3.4 PR #118 — socio-technical research architecture deep research

The diagnostic core of PR #118 says the bottleneck is better described as transdisciplinary interface/orchestration friction than as a demonstrated missing universal ontology, and that the owner/chat still performs too much integration across domain/method/evidence/tools/state/synthesis/restart.

**Reconciliation:**

- “Interface/orchestration friction rather than missing universal ontology” is **independent convergence** in mechanism, with an important qualification: the blind audit does not rank it as the single measured “bottleneck” because owner-effort/throughput was not quantified.
- The owner acting as workflow integrator is **independent convergence** at the observed-work level via FB-20260902-003.
- The stronger label “Human as Semantic Compiler” is **partial convergence**. The blind report states that the owner can become final integrator across separately correct states, but does not show enough direct task decomposition to prove the full semantic-compiler role as a stable general mechanism.
- The related-system conclusion that no single inspected system covers fuzzy problem framing + domain authority + source/findspot fidelity + durable state + owner-readable synthesis is **independent convergence**. The blind report independently found no direct whole-system comparator and instead identified partial mechanisms in Tropy, Galaxy, PROV and RO-Crate.
- PR #118's architecture/intervention classes are outside this experiment's analysis-only scope and are **not reconciled as findings**.

### 3.5 PR #120 — systemic project-development deep audit

PR #120 is the closest prior analysis to the experiment. It names:

- Need-to-Structure Inversion;
- Semantic Decomposition → Coordination Rebound;
- Governance Accretion through Error Response;
- Meta-Persistence Loop;
- Local Verification / Global Utility Gap;
- Readiness Conflation / Assumption Laundering;
- Mirroring / Affirmative Abstraction Bias;
- Context/Handoff Protection can become Context/Handoff Work;
- AI coherence/generation outpacing real evidence;
- the owner as semantic/workflow integrator.

**Reconciliation by mechanism:**

#### Need-to-Structure Inversion

**Classification: `independent convergence`.**

Blind M1 `representation ratchet` and the Need→System Translation Audit independently reconstruct the same core transformation: an owner need for complexity absorption can become additional explicit project/state representations whose maintenance is then part of the work.

The blind wording is somewhat narrower: explicit structure is not itself treated as inversion; the issue appears when the new representation increases integration obligations without equivalent owner relief.

#### Semantic Decomposition → Coordination Rebound

**Classification: `independent convergence`.**

The blind report independently found that semantically correct owner/authority separation can create operational dependency edges and that modular decomposition does not eliminate integration work. Its external research used Schmidt & Bannon and Cataldo/Herbsleb/Carley rather than relying on the prior label.

#### Governance Accretion through Error Response

**Classification: `partial convergence`.**

The blind report independently found secondary work from assurance and controls, plus the same-day creation/removal of the MVP layer. It did **not** independently reconstruct the full #70 error→rule→new-error genealogy. The broader causal claim therefore remains only partially replicated.

#### Meta-Persistence Loop

**Classification: `partial convergence`.**

Blind M1 independently says that once an idea becomes a durable artefact, it creates consistency/update obligations and may gain apparent project weight. However, the blind phase did not reconstruct #108–#116 turn-by-turn and did not establish how frequently persistence itself changed promotion probability.

#### Local Verification / Global Utility Gap

**Classification: `independent convergence`.**

Blind M3 `formal-value gap` is nearly the same mechanism, independently derived from #62/#63 plus real owner feedback. Both analyses explicitly reject the inference `technical/formal PASS = owner/research utility`.

#### Readiness Conflation / Assumption Laundering

**Classification: `blind audit missed prior issue`.**

The blind analysis did not inspect/reconstruct #119 before freeze. After reconciliation opened PR #120 and then PR #119, the distinct case is clear: a real provenance path had been treated as if it implied admitted text-bearing retrieval input/current corpus availability. This is genuinely additional evidence and a separate failure mode, not something that should be backfilled into the blind report.

#### Mirroring / Affirmative Abstraction Bias

**Classification: `partial convergence`.**

The blind phase reproduced premature semantic promotion and the owner-mental-model case. It did not reproduce the chat-level conversational mirroring evidence or establish it as a distinct model-behaviour cause.

#### Context/Handoff Protection → Context/Handoff Work

**Classification: `independent convergence`.**

Blind M1/M4 and the tensions section independently describe restartability and handoff protection as simultaneously valuable and work-generating.

#### AI generates coherence/structure faster than evidence

**Classification: `prior finding only weakly supported` for AI-specific causality; `partial convergence` for the throughput asymmetry itself.**

Blind M7 independently observed that artefact generation/mutation is cheap while semantic validation depends on domain fit and real use. But it explicitly judged causal attribution to AI itself as unproven because tool constraints, project novelty, human review practice and repository structure are confounders. External AI-productivity evidence is context-dependent and mixed.

#### Human as Semantic Compiler / Workflow Engine

**Classification: `partial convergence`.**

The blind report strongly reproduces “human as workflow integrator” through owner feedback and separate-state integration burden. “Semantic compiler” is a stronger claim. The blind evidence shows examples of owner correction and cross-domain interpretation, but no quantitative or task-level decomposition proving that role across the project.

## 4. Cross-analysis reconciliation matrix

| Prior claim / mechanism | Blind analogue | Classification | Reason |
|---|---|---|---|
| owner needs were explicit early; problem is not simple bad elicitation | B.1, P1 | independent convergence | derived from #1/#13/#28 before blocked audits |
| Need-to-Structure Inversion | M1 representation ratchet; D key distinction | independent convergence | same transformation reconstructed under different vocabulary |
| semantic decomposition creates coordination rebound | M4 + specialization↔coordination | independent convergence | independent project evidence + coordination literature |
| governance/error response can recursively add burden | M4, M5 | partial convergence | side effects reproduced; recursive genealogy not fully reconstructed |
| meta-persistence / persisted ideas gain weight | M1 | partial convergence | mechanism reproduced broadly, exact #108–#116 lifecycle not |
| formal/local PASS != owner utility | M3 formal-value gap | independent convergence | direct owner evidence + assurance boundaries |
| owner/chat as workflow engine | B.6, G.2, H interfaces | independent convergence | direct FB-20260902-003 evidence |
| owner as semantic compiler | owner integration burden | partial convergence | phenomenon visible; stable role not fully demonstrated |
| premature abstraction from owner mental models | B.9, M2 | independent convergence | Sep19 primary correction independently read |
| mirroring/affirmative abstraction | no direct chat-language analysis | partial convergence | result reproduced, conversational cause not |
| interface/orchestration friction > missing universal ontology | B/D/H/J | partial convergence | interface friction strongly reproduced; “dominant bottleneck” not measured |
| source/evidence formalization is necessary | F.1/L counterevidence | independent convergence | direct live-case utility |
| source identity is a positive counterexample to harmful formalization | P7 | novel independent finding | blind audit makes this explicit discriminating counterexample |
| real evidence/live source work is strongest correction mechanism | B.8/M6/P4 | novel independent finding / partial prior support | prior audits value pilots/countercases, blind audit gives live evidence-led reframing central explanatory status |
| churn can reflect healthy correction instrumentation | M5/P8 | independent convergence | PR120 error-culture section independently compatible |
| #119 readiness/admission error | none in frozen report | blind audit missed prior issue | not inspected before freeze |
| U1–U4 practical pilots were too broad / mixed products | no equivalent specific audit | prior finding not reproduced | blind evidence supports situated work generally, not this precise pilot judgement |
| 5-minute handoff failure | no timed handoff test | prior finding not reproduced | no independent measurement |
| dynamic competence activation vs static role catalog | expertise routing from need | partial convergence | blind conceptual need matches; no Wissensarbeit comparison |
| direct GitHub writes bypass local guard | B.10/M4 | independent convergence | independently found via #44 incident |
| AI-specific mechanism is primary root cause | M7 | prior finding only weakly supported | plausible contribution, causal isolation absent |
| cross-project generality | N/P limits | unresolved | both analyses explicitly lack independent other-repo cases |

## 5. Novel independent contributions

These are findings whose *specific analytical role* was not simply copied from the prior diagnostics.

### 5.1 Formalization-type discrimination

The blind audit found that “more structure” is too coarse a category. The Source→Instance→Derivative→Findspot→Finding boundary is a strong counterexample: it appears to reduce ambiguity and source laundering while leaving historical interpretation open.

The relevant distinction emerging independently is therefore:

- **loss-boundary formalization**: preserves identity, provenance, uncertainty or non-equivalence;
- **problem-partition formalization**: decides in advance how research questions, modules, phases, categories or mental models should organize work.

The observed failures cluster much more strongly in the second category. This distinction remains a **Researcher Inference**, not a new project rule.

### 5.2 Evidence-led reframing as a project-development signal

The blind reconstruction gives live U2 source encounters a larger role than the prior meta-audits: sources do not merely validate historical claims; they also falsify the project's chosen research partition. Moxa, Triptis and the rejected module frame show that evidence changes what the useful unit of work is.

Prior analyses use pilots/countercases, so this is not wholly absent there; the stronger claim that **research evidence itself is one of the best discriminators of workflow/model adequacy** is a novel emphasis.

### 5.3 Correction visibility as counterevidence

The blind audit explicitly treats reversals, `NOT PASS`, unresolved findings and removed layers as evidence of a functioning recovery system, not merely churn.

PR #120 independently values error detection, so there is convergence on correction. The blind addition is methodological: a highly instrumented project may look more unstable precisely because it exposes errors that another project would silently retain.

### 5.4 Situated-action literature changes the interpretation

The blind external search independently added Suchman's situated action, Bates' berrypicking and Kuhlthau's Information Search Process. These sources strengthen a specific alternative explanation:

The recurring mismatch may not primarily be “insufficient governance” or even “bad abstraction”; exploratory historical work may inherently discover its useful concepts, search terms and next questions during interaction with evidence. A fixed structure can therefore fail even when it was rational and well designed at creation time.

This is compatible with the prior sensemaking/exploratory-search literature but is a distinct theoretical route.

## 6. Prior findings not reproduced or only weakly reproduced

### 6.1 U1–U4 practical-pilot cut

Not independently reproduced. The blind audit did not test the practical usability of every U1–U4 pilot definition or DoD.

### 6.2 Five-minute root/handoff usability

Not independently reproduced. No timed handoff/usability trial was performed in the blind phase.

### 6.3 Mirroring as distinct AI conversational mechanism

Only partially reproduced. Premature promotion was independently observed; mirroring/affirmative agreement as its causal conversational mechanism was not independently tested.

### 6.4 AI as primary source of structural proliferation

Only weakly supported. AI plausibly lowers the cost of producing coherent structure, but the observed system also contains human product choices, GitHub/connector constraints, issue topology, restartability requirements and real scientific complexity.

### 6.5 Dominant-bottleneck ranking

PR #118 calls interface/orchestration friction the current bottleneck. The blind audit strongly observes the mechanism but does not have quantitative owner-time, throughput or comparative-friction measurements. Therefore the **mechanism converges; its rank as the dominant bottleneck remains unresolved**.

## 7. Contradictions

No strong factual contradiction was found between the frozen blind analysis and the descriptive cores of #64/#70/PR #116/#118/#120.

There are, however, two **analytical tensions**:

1. Prior audits sometimes use broad labels such as Governance Accretion or Human as Semantic Compiler. The blind audit supports narrower observable mechanisms but is more conservative about causal or role-wide generalization.
2. The blocked analyses place more emphasis on explicit meta-work lifecycle failures (#108–#119). The blind audit places relatively more emphasis on live historical evidence as a force that changes the appropriate research partition.

These are differences in explanatory weight, not mutually exclusive claims.

## 8. What the replication changes epistemically

The main value of the replication is not that it found different vocabulary. It changes the evidence status of several claims.

### Stronger after independent convergence

The following no longer rest only on later self-diagnosis:

- owner needs were explicit early;
- formal/semantic maturity can diverge from owner-facing utility;
- semantically correct decomposition can produce coordination work;
- premature structuralization of owner language occurred;
- controls can create secondary operational work;
- live research repeatedly falsifies or reframes prebuilt structures;
- governance is simultaneously protective and burden-producing;
- less governance / more automation / “AI is unreliable” are insufficient one-factor explanations.

### Still not strongly established

- AI is the primary causal source of the pattern;
- “Human as Semantic Compiler” accurately describes most owner work;
- U1–U4 pilot scope is generally the principal current problem;
- interface/orchestration friction is quantitatively the single dominant bottleneck;
- the pattern generalizes beyond Histo-Orla;
- any specific architectural or process intervention would reduce total owner burden without losing scientific safeguards.

### Newly visible because of divergence

The blind miss on #119 is important: a high-quality independent reconstruction can still omit a distinct failure class if its evidence sampling emphasizes historical development and owner feedback over the most recent implementation calibration. This places a limit on claims that the blind report is complete.

Conversely, the blind report's positive formalization counterexample and situated-action framing show that prior labels can be too coarse if they imply “formalization” or “governance” as a homogeneous class.

## 9. Final reconciliation state

### Most robustly replicated

1. **Need presence was not the main missing ingredient.**
2. **Need→system translation and operational integration were recurring failure surfaces.**
3. **Formal correctness and real owner utility diverged at least at documented points.**
4. **Specialization/semantic decomposition created real coordination dependencies.**
5. **Premature promotion of owner language into durable structure occurred.**
6. **Governance/assurance both prevented failures and generated additional work.**
7. **Real source work repeatedly supplied corrective evidence that abstract planning did not.**
8. **A single-cause account (“too much governance”, “bad requirements”, “LLMs”, “not enough automation”) is not supported.**

### Most important counterfindings

1. Provenance/source-identity formalization repeatedly protected the research rather than distorting it.
2. Fail-closed checks, owner corrections, `NOT PASS`, reversals and audit history prevented silent escalation of several errors.
3. Some apparent project churn is therefore recovery evidence.
4. The owner burden is real qualitatively but remains insufficiently quantified.
5. The blind audit itself missed #119, demonstrating that any single reconstruction can have coverage blind spots.

### Largest unresolved questions

- net owner effort over time;
- which meta artefacts are actually used vs merely maintained;
- whether coordination cost is transitional or structurally persistent;
- which observed mechanisms reproduce across heterogeneous research cases;
- the causal contribution of AI relative to project structure/tooling;
- whether other repositories reproduce the pattern independently.

No solution, roadmap, target architecture, framework selection, new Requirement, governance change or implementation recommendation is created by this reconciliation.
