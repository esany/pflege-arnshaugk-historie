# D4 — Problem-driven external Deep Research: project findings F1–F14

**Repository basis:** `review/repeated-audit-project-implications-20260922` @ `f5dd6b013af1064e039148f25a8c4e4ccf813165`
**Date:** 2026-09-22
**Work owner:** #64 (review input); re-entry interface: #92
**Research protocol:** #45 and `docs/research/source-identity-protocol.md`
**Status:** `external-research evidence / finding-by-finding reconciliation input / no Requirement, Method, Architecture, Selection, Roadmap or Delivery authority`

> **EXECUTION MODE INSUFFICIENT FOR REQUESTED DEEP RESEARCH:** the dedicated ChatGPT Deep Research product workflow was not available in this execution context. This is a transparent, browser-assisted, multi-surface research run, not a substitute silently presented as that product mode. It uses inspected full texts where accessible, otherwise publisher abstracts/metadata; the source trail marks that distinction. It is adequate as a bounded reconciliation input, not an exhaustive systematic review or independent expert validation.

## 1. Purpose, boundary, and method

### 1.1 Question and exclusion

This report challenges the current project findings rather than treating them as facts to be confirmed. It asks which mechanisms external theory and empirical research support, under what conditions their converse holds, and which project explanations remain underdetermined.

It ends before any rebuild conception. It does **not** select a technology, prescribe a workflow, propose a target architecture, create requirements, prioritize delivery, or authorize implementation.

### 1.2 Fresh project baseline

Read afresh: root `AGENTS.md`, `PROJECT_STATE.md`, `README.md`, issues #64, #92 and #45, #92's 2026-09-22 re-entry gate, `docs/research/source-identity-protocol.md`, PR #125's pointwise finding disposition, and the evidence-bearing audit chain represented by PRs #118, #120, #122 and #124. The current branch is ahead of `main` and is explicitly treated as review evidence, not as merged project truth.

The controlling sequence is therefore:

```text
system findings → this external research → finding-by-finding reconciliation → HARD STOP
```

The prior #92 execution waves are prior solution hypotheses only. In particular, this report does not revive their implied topology, read model, interface, package, owner structure, or capability order.

### 1.3 Research plan and search surfaces

The research began with the eight problem clusters in the handoff, then used backward/forward leads from foundational works and recent reviews. Search surfaces: publisher full texts and abstracts, ACM/IEEE/ICLR proceedings, PubMed/PMC, W3C and research-infrastructure specifications, university repositories, and documented real systems. Searches were conducted in English because the pertinent research traditions are predominantly anglophone.

Priority was: (1) systematic reviews, meta-analyses and standards; (2) mechanism-defining primary work; (3) empirical case studies/RCTs; (4) official related-system documentation. Search stopped where additional high-quality results predominantly repeated the same mechanism. Paywalled full texts, non-indexed books, private industrial data and non-English regional literature remain access boundaries.

**Inspection notation:** `full` = substantive full text inspected; `abstract` = publisher/proceedings abstract and metadata inspected; `spec` = official specification inspected; `related system` = official system documentation/paper inspected. No claim below relies on a title or snippet alone.

### 1.4 Evidence discipline and transfer rule

| Label | Meaning in this report |
|---|---|
| **PE** | Project evidence: repository, issue, pull request, test or documented behaviour |
| **OE** | Owner/workflow evidence persisted in the project |
| **ER** | External scholarly or standards evidence |
| **RS** | Related-system evidence |
| **RI** | Researcher inference, explicitly separated from its inputs |
| **OH** | Open hypothesis; plausible but not discriminated |

Healthcare handoffs, safety engineering, computational science and software teams are mechanism analogies, not population equivalences. A result transfers only at the named mechanism (for example, cue-supported resumption), not as an automatic claim about historical research or Histo-Orla.

### 1.5 Anchoring and contamination risk

The F1–F14 map is an unavoidable research agenda and thus an anchoring risk. To counter it, every cluster includes a competing account, an example where the apparent opposite is useful, and an explicit non-transfer. Earlier internal audits were used only to identify PE, never as ER. AI-generated prose is not evidence.

## 2. Current project-finding baseline

| Finding | Current project disposition | Currentness | Main competing explanation | Tier |
|---|---|---|---|---|
| F1 needs visible early | strengthen | current | missing/poorly prioritized requirements still matter | A |
| F2a premature partition promotion | strengthen/reframe | current | early externalization can make assumptions testable | A |
| F2b representation-maintenance ratchet | keep | current | maintenance can be the price of valuable memory | A |
| F3 formalization types | new/split | current | all formalization may constrain, or all may simply document | A |
| F4 decomposition/coordination rebound | strengthen | current | specialization may lower net cost at sufficient scale | A |
| F5 controls and recovery | split; loop downgraded | current/historical mixed | controls may be net protective; full recursive loop not reproduced | A |
| F6 local PASS/global utility gap | strengthen | current | some local measures are valid leading indicators | A |
| F7 readiness/admission conflation | keep separate | current | a smaller state model may be enough for bounded operations | A |
| F8 owner language promotion | reframe; mirroring downgraded | current | literal language may accurately encode a stable need | A |
| F9 handoff protection becomes work | keep separate | current | durable cues can reduce net work | A |
| F10 evidence-led reframing | new/strengthen | current | some churn is avoidable framing error | A |
| F11 visible correction as recovery | new | current | repeated correction can still be uncontrolled churn | A |
| F12 AI amplifier vs primary cause | unresolved/qualified | current | AI may alter the production–review ratio without causing the base problem | B |
| F13 owner integrator vs semantic compiler | split | current | integration may be irreducible expert judgment | B |
| F14 orchestration friction as bottleneck | unresolved | current | other constraints may dominate | B |

## 3. Deep research by problem cluster

## R-A — Exploratory inquiry versus premature problem partitioning (F2a, F3b, F10; cross-cutting F1/F14)

### Mechanism and theory

The strongest external fit is not “exploration means no structure.” Bates’ **berrypicking** model treats the information need and the retrieved information as changing during search, unlike a one-shot query/answer model ([Bates 1989, full](https://pages.gseis.ucla.edu/faculty/bates/articles/berrypicking.pdf)). Contemporary review work confirms exploratory search as a distinct area with conceptual frameworks, influencing factors, design features and evaluation metrics rather than a synonym for ordinary lookup ([Liu & Qin 2024, abstract](https://doi.org/10.1108/EL-11-2023-0264)). Sensemaking literature similarly distinguishes fitting evidence to a frame from revising the frame itself; it cautions against flattening different information-seeking theories into one process ([Urquhart 2025, full](https://doi.org/10.1002/asi.24866)).

The counterweight is cognitive-dimensions research. *Premature commitment* names constraints on the order in which a person must make decisions; *viscosity* names resistance to later change ([Green & Blackwell, full](https://citeseerx.ist.psu.edu/document?doi=c9b5833587138da5e1ef563febe3084800e6199e&repid=rep1&type=pdf)). These concepts fit F2a precisely, but they are analysis vocabulary, not a proof that any particular project partition was premature.

Design-fixation research provides a second mechanism: precedents can inappropriately constrain later designs, but effects depend on designer, problem, source, process, goals, similarity and distance. A review synthesized 50 empirical studies rather than finding a universal effect ([Sio et al. 2018, abstract](https://doi.org/10.1080/21650349.2017.1320232)). That heterogeneity directly weakens a blanket anti-structure conclusion.

### Methodology and empirical discrimination

Useful observables are not counts of reframings. They are: changes in the operative question; query/path divergence; discarded versus retained frames; time or effort to revise a classification; whether a frame concealed a decisive source class; and whether a stable decision was forced before its evidence became available. Suitable study forms are longitudinal contextual inquiry, search-session traces, pre/post task framing, and comparative cases with an initially fixed versus revisable representation. Validity risks include calling any learning “churn,” observer-induced search behaviour, and treating a later good frame as proof that early framing was irrational.

Adaptive case-management literature is an informative but limited comparison. It contrasts predefined routing with case workers deciding what can be done toward a goal in knowledge-intensive work ([van der Aalst et al. 2005, abstract](https://doi.org/10.1016/j.datak.2004.07.003)); a review notes that many knowledge processes cannot be fully specified at design time ([Müller et al. 2014, abstract](https://www.researchgate.net/publication/263366724_Research_Challenges_in_Adaptive_Case_Management_A_Literature_Review)). It supports the existence of an exploration/prescription distinction, not a claim that historical inquiry should be managed by a case-management product.

### Reconciliation

**Supported:** PE of evidence-led reframing has a strong theoretical analogue: in open inquiry, the working problem structure can itself be discovered. **Weakened:** F2a cannot infer that all early modules, phases or categories were wrong. **Split:** distinguish a provisional external representation used to expose an assumption from a promoted partition that constrains work, identity or authority. **Unresolved:** PE has not measured whether particular Histo-Orla reframings were avoidable or intrinsic. F14 must not rank framing cost above source access, expertise, or technical reliability without comparative data.

## R-B — Representation, formalization and epistemic loss (F2b, F3a/F3b)

### Mechanism and theory

External representations can lower memory and inference burden: Kirsh and Maglio’s experiments distinguish **epistemic actions**—actions that reveal or simplify cognition—from merely pragmatic actions ([1994, abstract](https://doi.org/10.1207/S15516709COG1804_1)). Distributed-cognition work studies tasks whose information is distributed between people and external representations ([Zhang & Norman 1994, abstract](https://www.sciencedirect.com/science/article/abs/pii/0364021394900213)). These theories support F2b’s first half: representation can create real cognitive value.

But representations have a lifecycle. Schema-evolution literature exists because changing structures must retain data and functionality across a temporal mismatch ([Roddick 1995, abstract](https://doi.org/10.1016/0950-5849(95)91494-K)); a recent review reports heterogeneous approaches and treats semantics, propagation, integrity and software evolution as separate dimensions ([Brahmia, Grandi & Oliboni 2024, abstract](https://doi.org/10.1142/S2972370124300012)). Thus F2b’s maintenance burden is not a metaphor: persistent schemas convert a cognitive aid into a versioning and reconciliation object.

Star and Griesemer’s boundary-object account is a crucial counterexample to broad anti-formalization. Their museum case explains cooperation across heterogeneous social worlds through objects that are locally adaptable yet stable enough for shared work ([1989, full text](https://griesemer.net/wp-content/uploads/2020/12/07-star-griesemer-1989-sss19-3387-420-boundary-objects.pdf)). It supports neither total semantic unification nor unstructured pluralism.

### Loss-boundaries versus partition formalization

F3’s distinction is externally coherent. W3C PROV treats provenance as information about entities, activities and agents used to assess quality, reliability and trustworthiness; its model is deliberately an interchange model, not a truth engine ([W3C PROV Overview, spec](https://www.w3.org/TR/prov-overview/)). Provenance-aware knowledge-representation literature separately identifies the difficulty of attaching context and provenance to claims ([Sikos & Philp 2020, abstract](https://doi.org/10.1007/s41019-020-00118-0)). These are analogues of **loss-boundary formalization**: they maintain distinctions without settling historical interpretation.

By contrast, classifications, fixed research phases and global ontologies allocate what exists and what kind of work is permissible. The relevant empirical question is not whether a schema is present, but whether it forces conversion, suppresses alternatives, or makes revisions expensive. F3b is therefore a separate mechanism from F3a.

### Related systems and limits

W3C PROV and RO-Crate make identity, derivation and packaging inspectable; RO-Crate explicitly aggregates research resources and contextual metadata ([RO-Crate 1.3, spec](https://www.researchobject.org/ro-crate/specification/1.3/index.html)). Neither determines a discipline’s substantive interpretation. Galaxy tracks computational analysis details to make work accessible and reproducible ([Galaxy 2020, related system](https://pmc.ncbi.nlm.nih.gov/articles/PMC7319590/)). These systems illuminate explicit provenance and derived views, but their computational workflow scope is not historical source criticism and should not be treated as a product template.

**Reconciliation:** F3a is strongly strengthened as a protective hypothesis where PE demonstrates actual non-equivalence (source/instance/derivative/findspot/finding, AI/evidence, unresolved/false). F3b is strengthened as a distinct risk, not a verdict against ontology or classification. F2b is supported but conditional: the net burden depends on use frequency, number of consumers, rate of change, and whether derivations are manually synchronized. No external source establishes the project’s current net balance.

## R-C — Decomposition, specialization and coordination rebound (F4, F13, part of F14)

### Mechanism and theory

Coordination theory defines coordination as managing dependencies among activities and identifies resource, producer–consumer, simultaneity and task/subtask dependencies ([Malone & Crowston 1994, full](https://ccs.mit.edu/papers/ccswp157.html)). Strauss’ articulation-work account is a complementary theory: the work of arranging, repairing and aligning project work is itself organizational work, not noise outside the project ([Strauss 1988, abstract](https://doi.org/10.1111/j.1533-8525.1988.tb01249.x)).

Socio-technical congruence adds empirical leverage. Research on large software projects found better modification-request resolution when observed coordination aligns with technical coordination needs; a later synthesis reports the original average reduction as 32%, but this is a software-project result, not a general human-work coefficient ([Rajapakse 2025, abstract](https://doi.org/10.1002/smr.70040)). Communication studies also find that complex, unfamiliar or changing work increases cross-team information seeking and makes boundary-spanning roles visible ([Hannay et al. 2022, full](https://link.springer.com/article/10.1007/s10664-021-10027-z)).

### Counterevidence and transfer limit

Modularity can improve participation and adaptation: an empirical study found substantial structural differences between Linux and Mozilla and argues that management can influence modularity ([MacCormack, Rusnak & Baldwin 2006, abstract](https://doi.org/10.1287/mnsc.1060.0552)). Therefore, F4 does not support “boundaries are bad.” It identifies a non-equivalence: semantic correctness does not guarantee low *operational* coordination cost.

F13 must stay split. Cross-tool/state integration can be observed and measured (handoff count, broker time, unresolved dependency age, rework after handoff); calling an owner a stable “semantic compiler” makes a far stronger claim about irreducible interpretation and has no direct support here. It may conflate essential scholarly judgment with accidental boundary repair.

### Reconciliation

**Strengthen F4:** dependencies can move work to a broker despite correct authority boundaries. **Split F13:** `workflow integration` is a supported PE/ER mechanism; `semantic compiler` remains OH. **Weaken F14:** coordination research makes friction measurable, but offers no basis to declare it Histo-Orla’s dominant bottleneck. A legitimate bottleneck claim needs comparative delay/effort and outcome data across source access, method uncertainty, integration, evaluation and technical execution.

## R-D — Controls, assurance, error and recovery (F5, F11)

### Theory, evidence and criticism

Safety-I emphasizes preventing unacceptable outcomes; Safety-II/resilience work emphasizes the adaptive performance through which work normally succeeds. Reviews explicitly caution that Safety-I methods can still be useful, rather than presenting a replacement ([Hollnagel et al. 2021, full](https://pmc.ncbi.nlm.nih.gov/articles/PMC7940128/)). A 472-contribution review identifies a broad, still evolving research field ([Righi, Saurin & Wachs 2018, abstract](https://doi.org/10.1016/j.ssci.2017.10.005)). Its empirical measurement base is limited: one integrative review screened 3,884 studies but found only 17 quantitative studies meeting inclusion criteria ([Pillay & Morel 2020, full](https://doi.org/10.3390/safety6030037)). A strong published critique argues that central Safety-II propositions lack adequate evidence of impact ([Nielsen 2022, abstract](https://doi.org/10.1016/j.ssci.2020.105047)).

This evidence disfavors both slogans. Controls can prevent loss and support recovery, but a resilience vocabulary alone does not prove a control is effective or proportionate. Health-care handoff reviews further illustrate the duality: standardized transfer can reduce omissions, yet excess information can distract and research does not identify a single best handoff tool ([Segall et al. 2012, full](https://pmc.ncbi.nlm.nih.gov/articles/PMC6152818/); [Mardis et al. 2021, abstract](https://pubmed.ncbi.nlm.nih.gov/33325520/)). The population and stakes differ radically, so only the mechanism—information loss versus burden—transfers.

### Methodological implications (not an intervention)

F5 needs separate dependent variables: prevented/contained error, time to detection, time to recovery, false blocks, new documentation/synchronization time, and user understanding. Incident/near-miss analysis can identify control value; longitudinal work sampling can identify secondary work; comparison with a no-control condition is often ethically or practically impossible. Counting controls or errors alone cannot establish net effect.

### Reconciliation

**F5a supported:** controls make visible secondary work. **F5c strengthened:** PE’s loss boundaries and explicit unresolved/reversal states plausibly act as protective controls, and external safety literature makes that mechanism credible. **F5b remains downgraded:** no external evidence converts project episodes into a demonstrated recursive error→rule→complexity→error causal loop. **F11 reframed:** visible correction is evidence of detection/recovery *only when* it follows identifiable errors and reduces recurrence or recovery cost; repeated unbounded reversal without learning is churn, not resilience.

## R-E — Local correctness versus global research utility (F6)

Verification asks whether specified properties hold; validation concerns intended use. Knowledge-based-system evaluation literature already noted that formal specifications cannot express all user requirements and that a single general evaluation procedure is unavailable ([Gonzalez & Barr 2000, abstract](https://www.sciencedirect.com/science/article/abs/pii/S0950705198000471)). This directly supports F6’s distinction but not a dismissal of local verification.

Metrics/proxy literature supplies the mechanism: a local, legible measure can become a target rather than remain evidence about the underlying outcome. The transfer here is conceptual; there is no demonstrated Goodhart episode in Histo-Orla. Stronger evidence comes from evaluation design: socio-technical systems literature is itself heterogeneous, and a recent systematic review calls for clearer use of the term and explicit system boundaries ([Polojärvi 2023, abstract](https://doi.org/10.1002/sys.21664)).

The relevant study design is mixed-method, end-to-end and comparative: completion and error data; time-on-task; workload; evidence quality as independently reviewed where necessary; owner comprehension; and qualitative observation of workarounds. A green CI result may be a valid proxy for a narrow invariant (for example, referential integrity) but cannot proxy the whole research experience unless empirically correlated with it.

**Reconciliation:** F6 is strongly supported. It must not be merged into F5: a low-burden control plane can still optimize a local proxy. The converse is equally important: owner impressions alone are not reliable global utility evidence; objective task and outcome measures are needed. The project currently lacks such correlation evidence.

## R-F — Readiness, preconditions and assumption laundering (F7)

F7 has a precise external analogue in contracts, state machines and data quality. Design-by-contract treats preconditions, postconditions and invariants as distinct interface claims; its value lies in checking a claim at the boundary, not treating an upstream object as automatically valid for a downstream operation ([Eiffel: Design by Contract and Assertions, reference](https://www.eiffel.org/doc/eiffelstudio/I2E-_Design_by_Contract_and_Assertions)). Wang and Strong’s information-quality tradition defines quality from a consumer’s **fitness for use**, not accuracy alone ([1996, abstract](https://doi.org/10.1080/07421222.1996.11518099)). W3C PROV similarly records provenance to support assessment, but provenance is not itself a fitness assertion ([PROV Primer, spec](https://www.w3.org/TR/prov-primer/)).

This gives a robust discrimination: `exists`, `traceable`, `available`, `admitted`, `current` and `fit for operation` answer different predicates. A source record may be traceable but inaccessible; a byte stream may be accessible but inadmissible; a correct earlier validation may be stale. The evidence does not prescribe how many states any one system needs. A proliferation of nominal states could reproduce F2b/F5 burden.

**Reconciliation:** F7 is strengthened as its own failure class. The narrow PE question is whether each historical incident actually crossed a false prerequisite, rather than merely encountered an unavailable resource. The external gap is empirical evidence about the smallest useful readiness vocabulary for research software; current sources establish the distinction, not its optimal granularity.

## R-G — Human/AI interaction as promotion and amplification mechanism (F8, F12)

### Owner language and collaboration

Requirements research supports preserving origin and context: a 77-paper SLR finds pre-requirements traceability useful for understanding a requirement’s context, change history and responsibility, while also reporting unclear benefits and the need to tailor strategy to project, role and use ([Mucha, Kaufmann & Riehle 2024, full](https://link.springer.com/article/10.1007/s00766-023-00412-z)). A systematic review of user involvement finds that involvement must extend beyond elicitation to design and testing, with uncertainty and complexity affecting the required form of involvement ([Bano & Zowghi 2015, abstract](https://www.sciencedirect.com/science/article/pii/S0950584914001505)). Thus F1 and F8 are compatible: user language should remain traceable without becoming untested system semantics.

AI sycophancy is a real but limited candidate mechanism. An ICLR study found five assistants showed sycophancy across four free-text tasks and connected it partly to preference judgments favoring belief-congruent responses ([Sharma et al. 2024, full abstract](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html)). This supports research into agreement bias; it does **not** establish that it caused a particular Histo-Orla promotion. Human collaborative sensemaking, anchoring, time pressure, and a persistence process can produce the same observed promotion without model sycophancy.

### AI production versus validation capacity

The current evidence is context-sensitive. METR’s RCT of 16 experienced open-source developers on 246 tasks in familiar mature repositories found early-2025 AI tools increased completion time despite positive user expectations ([Becker et al. 2025, full](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf)). Conversely, a Google RCT reports results for enterprise tasks and explicitly warns that an effect size cannot be assumed to generalize across tools, time or ecosystems ([Denny et al. 2024, abstract](https://arxiv.org/abs/2410.12944)). The valid conclusion is not “AI slows work” or “AI accelerates work.” It is that output rate, review burden, user calibration, task novelty and prior codebase knowledge interact.

**Reconciliation:** F8 is strengthened as a lifecycle phenomenon and its causal label is correctly downgraded: mirroring/sycophancy is one OH among several. F12 is reframed: AI plausibly reduces the cost of producing candidate artifacts and may shift bottlenecks toward review/integration, but current project and external evidence do not establish AI as the primary cause of the structural pattern. AI effects should be measured at an end-to-end task level, not inferred from artifact count.

## R-H — Restartability, handoffs and external memory (F9)

Interruption research gives direct evidence for the benefit side of F9. In a controlled study, resumption lag was substantially longer than ordinary inter-action intervals, while cues available before interruption reduced the lag ([Altmann & Trafton 2004, full](https://www.interruptions.net/literature/Altmann-CogSci04.pdf)). That supports durable, task-relevant resumption cues—not every possible context field.

The burden side is equally real. Systematic handoff reviews identify omissions and delays but find no single best tool; excess information can distract or be low-value ([Mardis et al. 2021, abstract](https://pubmed.ncbi.nlm.nih.gov/33325520/)). Computational notebooks are a related-system warning: they support exploration and narrative, but empirical studies document hidden state, out-of-order execution and non-executed cells that undermine reproducibility ([Pimentel et al. 2021, full](https://pmc.ncbi.nlm.nih.gov/articles/PMC8106381/)).

**Reconciliation:** F9 is supported and must remain separate from F4. Its core mechanism is continuity across time, not specialization across roles. The minimal sufficient context is unresolved and likely task-dependent. Candidate measurements are resumption lag, omitted prerequisite rate, time spent creating/repairing context, successful fresh-context completion, and which retained fields are actually consulted. Clinical handoff findings transfer only at controlled information continuity, not in their protocol content or safety claims.

## 4. Related-systems comparison: discriminating matrix

| Archetype / system | Problem actually addressed | Authority/formalized boundary | Complexity exposed or hidden | Transferable mechanism | Explicit non-transfer |
|---|---|---|---|---|---|
| W3C PROV | provenance interchange and assessment | entity/activity/agent history, not truth | requires capture choices and granular provenance | distinguish derivation from interpretation | no historical-method authority or research workflow ([spec](https://www.w3.org/TR/prov-overview/)) |
| RO-Crate | package/describe research resources | resources + contextual metadata | metadata maintenance/version compatibility | aggregate and describe without claiming a research conclusion | no evidence of suitability for live historical reasoning ([spec](https://www.researchobject.org/ro-crate/specification/1.3/index.html)) |
| Galaxy | reproducible computational analyses | tools, datasets, histories/workflows | tool versions, computational environment, training | automatic capture can lower reproducibility burden | domain is data-intensive biomedicine; its workflow formalization is not a historical inquiry model ([related system](https://pmc.ncbi.nlm.nih.gov/articles/PMC7319590/)) |
| Jupyter notebooks | exploratory computational work | visible cells, but runtime state can escape representation | hidden state and execution order | exploration and reproducibility are in tension | notebook failures do not diagnose repository documentation ([study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8106381/)) |
| Clinical handoff protocols | safe shift/transfer continuity | patient-specific transfer information | checklist length, interruption, training and attention | content must be relevant; more context is not always better | patient outcomes/stakes/protocols do not transfer ([review](https://pubmed.ncbi.nlm.nih.gov/33325520/)) |
| Adaptive case handling | flexible knowledge-intensive cases | case data/goal rather than fixed routing | worker discretion and authorization remain | distinguish what is known from what can be prescribed | no implication that a research assistant needs a case-management engine ([study](https://doi.org/10.1016/j.datak.2004.07.003)) |

## 5. Cross-cluster relations — and separations that must remain

1. **F2a/F3b/F10 interact but are not identical.** Exploration makes reframing normal; a premature durable partition makes a particular reframing costly. Either can exist without the other.
2. **F2b/F5/F9 all create secondary work but have different value claims.** A representation maintains memory, a control prevents a defined loss, a handoff preserves continuity. Lumping them into “governance” erases the trade-off.
3. **F4 and F13 concern coordination across specialization; F9 concerns time.** A single owner can have F9 without F4; a tightly coupled team can have F4 without a context handoff.
4. **F6 is an evaluation problem, not proof that controls are useless.** Local checks can be valid proxies for their declared invariants, but global utility requires separate evidence.
5. **F7 is a state-transition claim, not a documentation claim.** Provenance can support readiness assessment without satisfying an operation’s admission predicate.
6. **F8/F12 are amplification candidates, not established root causes.** The same promotion can arise from human conversation, organizational incentives, available persistence mechanisms, or AI agreement behaviour.
7. **F11 is conditional recovery evidence.** A visible correction signals health only where recurrence/recovery data show learning; otherwise it is merely a visible reversal.

No evidence supports collapsing these relations into a single “root cause: complexity” or “root cause: governance.”

## 6. Finding-by-finding disposition after external research

| Finding | Disposition | External evidence and PE relationship | Limits / remaining gap |
|---|---|---|---|
| F1 | **strengthen** | User involvement and traceability literature support the downstream transformation problem; PE already shows early needs. | Need presence does not prove requirements sufficiency or delivery priority. |
| F2a | **strengthen + reframe** | Exploratory search, cognitive dimensions and fixation research support revisable framing. | No case-level causal test distinguishes necessary exploration from project error. |
| F2b | **strengthen** | External representations help cognition; schema evolution validates maintenance as a real cost. | Net benefit depends on use/revision/consumer data absent in PE. |
| F3a | **strengthen** | Provenance and boundary-object research support protective distinctions. | External models are not proof that every project distinction is well scoped. |
| F3b | **split + strengthen** | Premature commitment/viscosity and exploratory inquiry support a distinct constraining mechanism. | No general anti-ontology conclusion. |
| F4 | **strengthen** | Coordination and socio-technical congruence support dependency/coordination rebound. | Existing estimates come largely from software teams, not historical research. |
| F5a | **strengthen** | Handoff/safety work recognizes secondary coordination cost. | Control work must be measured, not inferred from document count. |
| F5b | **remain downgraded / OH** | Safety literature supports feedback concepts, not the complete project recursion. | Requires episode-level temporal analysis and counterfactuals. |
| F5c | **strengthen** | Safety and provenance analogues support protection/recovery value. | Requires concrete loss model and observed control performance. |
| F6 | **strengthen** | V&V and socio-technical evaluation distinguish local conformance from use value. | Which local measures predict owner value is unmeasured. |
| F7 | **strengthen** | Contract, freshness and fitness-for-use distinctions support non-collapse of states. | Minimal state vocabulary and false-block cost unresolved. |
| F8 | **reframe; causal label unresolved** | Traceability supports retaining language/context; AI sycophancy is empirically real. | Cannot attribute a project event to sycophancy rather than normal collaboration/anchoring. |
| F9 | **strengthen** | Resumption-cue experiments support benefit; handoff reviews support burden/overload risk. | Minimal sufficient context is task-specific and not yet measured. |
| F10 | **strengthen** | Berrypicking/sensemaking/abduction support evidence-driven reframing. | Does not excuse arbitrary or repeated non-learning churn. |
| F11 | **reframe** | Resilience/error research makes detection/recovery a legitimate outcome. | Need recurrence and recovery-time evidence to distinguish healthy correction from churn. |
| F12 | **reframe + unresolved** | AI RCTs show highly context-dependent production/productivity effects. | No causal PE links AI to the structural pattern’s primary cause. |
| F13 | **split** | Articulation work supports integration labour; human judgment remains a separate claim. | Measure essential scholarly judgment versus accidental coordination. |
| F14 | **unresolved** | Coordination costs are real and measurable. | No comparative bottleneck analysis exists; ranking would overclaim. |

## 7. Research gaps and confidence matrix

| Conclusion | Evidence classes | Confidence | Counterevidence / transfer limit |
|---|---|---|---|
| Exploration can legitimately reframe a problem’s unit of work | ER + PE | high | does not show every reframe is necessary |
| Persistent representations can both help cognition and create maintenance | ER + PE | high | net balance is project-specific |
| Loss-boundary formalization differs from partition formalization | ER + PE | high | boundary models may themselves overspecify at bad granularity |
| Correct specialization can export integration work | ER + PE | medium-high | specialization can lower net coordination at suitable scale |
| Protective controls have value but create work | ER + PE | high | safety effectiveness evidence is heterogeneous and domain-bound |
| Formal PASS cannot establish research utility | ER + PE | high | selected local checks may still be valid indicators |
| AI is the primary cause of structural complexity | ER + PE | low / unresolved | evidence shows variable effects, not project causation |
| Orchestration is the dominant bottleneck | PE + ER | low / unresolved | no comparative measurement |

### External-research gaps

- Few causal studies compare alternative degrees of formalization in long-lived, exploratory scholarly work.
- Resilience/control research has uneven measurement and contested conceptual claims.
- There is little empirical evidence on the minimal, task-sensitive representation for high-fidelity human/AI context transfer.
- AI-assisted development studies change rapidly and vary by task, population, tool generation and outcome.

### Histo-Orla PE gaps

- No longitudinal task-level measure of owner time, cognitive workload, handoff/recovery effort, or end-to-end research output quality.
- No controlled or comparative evidence separating essential scholarly integration from accidental system-boundary coordination.
- No documented correlation between current local assurance checks and owner/research utility.
- No incident-level causal test for the full F5b loop or for AI/“mirroring” as cause of F8.

## 8. Search log and selected bibliography

### Search families and saturation rationale

| Family | Examples of terms/surfaces | What changed the analysis | Stop rationale |
|---|---|---|---|
| exploratory inquiry | berrypicking, exploratory search, sensemaking, abduction, cognitive dimensions, adaptive case management | separated normal reframing from costly premature promotion | recent reviews repeated the non-linear inquiry finding |
| representation/formalization | external representations, boundary objects, provenance, schema evolution | supplied the F3a/F3b distinction and maintenance mechanism | reached foundation + review + standard + cases |
| coordination | coordination theory, articulation work, socio-technical congruence, modularity | made F4 measurable and challenged anti-decomposition language | software population limit became the remaining uncertainty |
| controls/recovery | Safety-I/II, resilience, handoff, control burden | supplied dual-effect and contested-evidence frame | reviews repeated the measurement/effectiveness gap |
| value/readiness | V&V, proxy metrics, fitness for use, preconditions, provenance | separated predicate states and local/global evaluation | no direct research-software minimal-state study found |
| AI/promotion | user involvement, pre-RS traceability, sycophancy, AI productivity RCT | downgraded causal attribution and showed context dependence | additional sources repeated contextual heterogeneity |
| restartability | task interruption, handoff, notebooks, scientific workflows | provided measurable cue benefit and hidden-state counterexample | direct human/AI long-term context evidence remained sparse |

### Core bibliography

1. Bates, M. J. (1989). *The design of browsing and berrypicking techniques for the online search interface.* [Full text](https://pages.gseis.ucla.edu/faculty/bates/articles/berrypicking.pdf).
2. Liu, Y. & Qin, C. (2024). *Exploratory search in information systems: a systematic review.* [Publisher record](https://doi.org/10.1108/EL-11-2023-0264). `abstract`.
3. Sio, U. N. et al. (2018). *A review of design fixation.* [Publisher record](https://doi.org/10.1080/21650349.2017.1320232). `abstract`.
4. Green, T. R. G. & Blackwell, A. F. *Cognitive Dimensions of Notations.* [Full text](https://citeseerx.ist.psu.edu/document?doi=c9b5833587138da5e1ef563febe3084800e6199e&repid=rep1&type=pdf).
5. Kirsh, D. & Maglio, P. (1994). *On Distinguishing Epistemic from Pragmatic Action.* [Publisher record](https://doi.org/10.1207/S15516709COG1804_1). `abstract`.
6. Star, S. L. & Griesemer, J. R. (1989). *Institutional Ecology, ‘Translations’ and Boundary Objects.* [Full text](https://griesemer.net/wp-content/uploads/2020/12/07-star-griesemer-1989-sss19-3387-420-boundary-objects.pdf).
7. Brahmia, Z., Grandi, F. & Oliboni, B. (2024). *A Literature Review on Schema Evolution in Databases.* [Publisher record](https://doi.org/10.1142/S2972370124300012). `abstract`.
8. W3C (2013). *PROV Overview / Primer.* [Overview](https://www.w3.org/TR/prov-overview/), [Primer](https://www.w3.org/TR/prov-primer/). `spec`.
9. Malone, T. & Crowston, K. (1994). *The Interdisciplinary Study of Coordination.* [Full text](https://ccs.mit.edu/papers/ccswp157.html).
10. Strauss, A. (1988). *The Articulation of Project Work.* [Publisher record](https://doi.org/10.1111/j.1533-8525.1988.tb01249.x). `abstract`.
11. Cataldo, M. & Herbsleb, J. / later synthesis: Rajapakse, N. (2025). *Towards Multi-Class Socio-Technical Congruence.* [Publisher record](https://doi.org/10.1002/smr.70040). `abstract`.
12. Righi, A., Saurin, T. & Wachs, P. (2018). *Resilience engineering: current status.* [Publisher record](https://doi.org/10.1016/j.ssci.2017.10.005). `abstract`.
13. Hollnagel, E. et al. (2021). *Safety-II and Resilience Engineering in a Nutshell.* [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7940128/).
14. Nielsen, K. J. (2022). *The Emperor has no clothes: A critique of Safety-II.* [Publisher record](https://doi.org/10.1016/j.ssci.2020.105047). `abstract`.
15. Mucha, J., Kaufmann, A. & Riehle, D. (2024). *Pre-requirements specification traceability SLR.* [Full text](https://link.springer.com/article/10.1007/s00766-023-00412-z).
16. Bano, M. & Zowghi, D. (2015). *User involvement and system success SLR.* [Publisher record](https://www.sciencedirect.com/science/article/pii/S0950584914001505). `abstract`.
16a. Eiffel Software. *Design by Contract and Assertions.* [Documentation](https://www.eiffel.org/doc/eiffelstudio/I2E-_Design_by_Contract_and_Assertions). `inspected`.
17. Sharma, M. et al. (2024). *Towards Understanding Sycophancy in Language Models.* [ICLR record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html). `full abstract`.
18. Becker, J. et al. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.* [Full paper](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf).
19. Altmann, E. M. & Trafton, J. G. (2004). *Task interruption: Resumption lag and the role of cues.* [Full paper](https://www.interruptions.net/literature/Altmann-CogSci04.pdf).
20. Pimentel, J. F. et al. (2021). *Understanding and improving the quality and reproducibility of Jupyter notebooks.* [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8106381/).

## 9. Completion boundary — research result only

**Strongest externally supported project findings:** evidence-led reframing is normal in exploratory inquiry; representation and controls have dual benefit/burden effects; provenance/loss boundaries are analytically distinct from problem partitions; and local conformance cannot establish end-to-end research value.

**Strongest counterfindings:** early externalization can be cognitively valuable; specialization/modularity can lower net coordination; protective controls may be worth their secondary work; visible correction can indicate recovery rather than instability.

**Materially reframed or weakened:** broad anti-formalization, broad anti-governance, “mirroring” as established cause, the complete recursive control loop, AI as primary cause, owner as semantic compiler, and orchestration as dominant bottleneck.

**Unresolved competing explanations:** which observed reframings were intrinsic inquiry versus avoidable design error; which integration is essential scholarship versus accidental coordination; the smallest high-fidelity resumption context; and the project’s actual bottleneck ranking.

**Questions sufficiently clarified for a later, separate rebuild phase:** which distinctions must remain analytically separate, which claims require end-to-end rather than local evidence, and which causal labels may not be inherited from the audit chain.

# STOP

This report deliberately does not derive a rebuild conception, architecture, workflow, roadmap, tool choice, implementation plan, selection, or delivery authorization.
