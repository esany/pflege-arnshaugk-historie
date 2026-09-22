# Independent prompt run — depth and comparability assessment

**Date:** 2026-09-21  
**Review context:** #121 / #64  
**Comparison baseline:** PR #118 first socio-technical Deep Research  
**Experiment provenance:** PR #123 pre-comparison freeze  
**Status:** post-run methodological assessment / no Requirement, Method, Architecture, Selection or Delivery authority

## 1. Question

Assess the fresh-chat execution of the generic system/problem-analysis prompt:

- Was it genuinely deep research or mainly a structured audit with targeted web research?
- How does it compare with the initial PR #118 Deep Research?
- How much independent analytical value did it add?
- What does the result say about the generic prompt as a QA building block?

## 2. Evidence boundary

Compared:

- frozen blind artifact at commit `326178444528194e511688ae5e914aec0670c802`:
  `docs/research/audits/independent-replication-20260921.md`
- reconciliation artifact at PR #122 head `074a6502228bae2fe4c646b31dea10e691c63f80`
- initial PR #118 report at head `5c39a346037e7a1615e9a91ce39f06be86bd7f3b`:
  `docs/architecture/assurance/sociotechnical-research-architecture-deep-research-20260920.md`
- owner-supplied chat output from the fresh run.
- OpenAI current documentation on Deep Research activation/behaviour.

## 3. Important distinction: chat summary != blind artifact

The owner-visible fresh-chat answer is a compressed synthesis of the already-persisted #121/#122 experiment. It is not itself the full blind report.

The frozen blind report is materially larger:

- ~55,489 characters;
- ~813 lines;
- 92 headings;
- explicit independent project reconstruction;
- mechanism map;
- Need→System translation audit;
- external SOTA section;
- related-systems section;
- tensions/counterevidence;
- research gaps;
- confidence matrix;
- frozen independent findings.

Therefore the visible chat response alone understates the amount of repo analysis performed.

## 4. External-research depth compared with PR #118

### Fresh independent blind run

Observed in the frozen artifact:

- ~22 named external references in the final research boundary;
- ~10 unique DOI strings;
- external fields include:
  - Requirements Engineering;
  - Human-Centred Design;
  - Situated Action / Information Seeking / Sensemaking;
  - CSCW / articulation work / socio-technical congruence;
  - Boundary Objects;
  - Human-AI Interaction;
  - AI-assisted developer productivity;
  - FAIR / PROV / RO-Crate;
- related-system deep dives are narrow:
  - Tropy;
  - Galaxy;
  - PROV/RO-Crate as interoperable substrate.

The external research is generally well-qualified:
- evidence type;
- transferability;
- limitations;
- alternative explanations;
- counterevidence.

But it is not broad across a large related-system landscape.

### Initial PR #118

Observed:

- ~85,392 characters;
- ~1,470 lines;
- 127 headings;
- 30 unique explicit web URLs in the report;
- ~12 unique DOI strings;
- much broader related-system landscape (~21 named systems/standards in the comparison surface), including:
  Zotero, Tropy, OpenRefine, Recogito/Pelagios, WHG, Wikibase, Omeka S, nodegoat, Heurist, ResearchSpace, Arches, TEI, IIIF/Web Annotation, RiC-O, W3C PROV, RO-Crate, DataLad/git-annex, DVC, eScriptorium/Kraken, Transkribus, Obsidian, Logseq;
- broader fields:
  transdisciplinarity / trading zones / boundary objects;
  HCI / sensemaking / mixed initiative / resumption;
  DH / historical infrastructures;
  provenance / research objects;
  RSE / scientific workflows / local-first;
  requirements / design science;
  AI tooling / single-vs-multi-agent;
- explicit related-work matrix, capability/interface analysis, technical-interface landscape and falsification experiments.

### Assessment

The fresh run is **materially narrower** than PR #118 in external search breadth and related-system coverage.

It is stronger as a bounded independent project audit than as a comprehensive state-of-the-art review.

Best label:

> **research-informed independent audit with targeted SOTA challenge**

rather than:

> **full deep-research survey comparable in breadth to PR #118**.

## 5. Was ChatGPT Deep Research product mode likely used?

Current OpenAI documentation states that ChatGPT Deep Research is started by explicitly selecting Deep Research or typing `/Deepresearch` / `@Deepresearch`; it produces a research plan/progress experience and is intended for multi-step, in-depth source synthesis. OpenAI describes typical Deep Research tasks as taking roughly 5–30 minutes.

Owner report:
- Deep Research was not explicitly selected;
- the prompt itself did not invoke Deep Research;
- total visible duration was about 2 minutes.

The runtime UI cannot be independently inspected from the repository, so absolute proof is unavailable.

However, the evidence makes it **highly likely that this was standard ChatGPT reasoning + web/search/tool use, not the dedicated Deep Research product mode**.

Important consequence:

> Asking for “Deep Research” or “broad research” in prompt prose does not itself guarantee execution through the Deep Research product workflow.

This is an experimental finding about the generic prompt as a reusable QA instrument.

## 6. Independent analytical quality

Despite limited external breadth, the blind run is not merely superficial.

Strong independent work includes:

- reconstructing early owner needs before technical solutions;
- identifying the MVP-layer creation/removal as a natural experiment;
- separating formal-state maturity from lived owner utility;
- distinguishing static work partitioning from evidence-contingent inquiry;
- identifying assurance as both protection and its own coordination surface;
- treating Source/Instance/Derivative/Findspot formalization as a **positive counterexample** to the thesis that formalization itself is harmful;
- distinguishing epistemic uncertainty from operational uncertainty;
- introducing a useful contrast between:
  - `loss-boundary formalization`;
  - `problem-partition formalization`;
- preserving alternative explanations and counterevidence;
- weakening AI-specific causal claims instead of overclaiming them.

These are substantive contributions.

## 7. Limits to “independent convergence”

The generic prompt itself includes a long candidate failure-pattern list, including:
- premature abstraction;
- governance accretion;
- handoff explosion;
- human-as-workflow-engine;
- human-as-semantic-compiler;
- formal correctness without utility;
- coordination overload;
- essential vs accidental complexity.

Therefore convergence on these categories is **not equivalent to a blind spontaneous rediscovery**. They are part of the experimental stimulus.

The stronger independent evidence is where the run:
- chooses concrete project episodes itself;
- rejects simple versions of the seeded hypotheses;
- produces distinctions not explicitly supplied by the prompt;
- finds positive counterexamples;
- assigns lower confidence to AI-causality;
- identifies missing evidence.

Thus the valid replication claim is:

> the prompt successfully led a fresh context to reconstruct project evidence consistent with several prior diagnoses while also producing independent qualifications and counterfindings.

Not:

> a totally unseeded analyst independently discovered the same theory.

## 8. Methodological side effect: the fresh chat invented a blind protocol

The generic prompt did not instruct the model to create #121's explicit blocklist/reconciliation phases.

The fresh chat itself created:
- Work Owner #121;
- exclusion of #64/#70/PR #116/#118/#120 for the blind phase;
- frozen commit before reconciliation;
- separate reconciliation.

This is part of the prompt's observed behaviour.

Positive interpretation:
- strong experimental hygiene;
- it recognized contamination risk and protected the independent artifact.

Negative/neutral interpretation:
- it spent part of the run designing an experiment rather than broadening external research;
- it changed the operational method beyond the generic prompt;
- strict comparability with a simple “run the prompt and analyse” execution is therefore imperfect.

## 9. Overall classification

### Project/repository reconstruction
**Depth: high**

The run inspected a substantial project history and selected discriminating episodes.

### Problem/mechanism analysis
**Depth: medium-high**

Good causal caution, alternatives and positive counterexamples.

### External literature / SOTA
**Depth: medium**

Good source quality and relevance, but limited breadth and chaining.

### Related systems / best-practice landscape
**Depth: low-medium relative to PR #118**

Only a small number of systems were examined in depth.

### Dedicated Deep Research execution
**Most likely: no**

Owner-reported runtime and OpenAI activation semantics strongly indicate normal chat/search rather than Deep Research mode.

### Independence
**Useful but qualified**

Fresh context and source-blinding were meaningful, but:
- prompt itself seeded many candidate mechanisms;
- mandatory repo bootstrap leaked some later audit context;
- the run added its own blind-protocol method.

## 10. Main experiment finding about the generic prompt

The generic prompt is currently strong at producing:

- a disciplined independent audit;
- explicit evidence classes;
- counterhypotheses;
- error culture;
- interface analysis;
- scoped external challenge.

It does **not** by itself guarantee:

- dedicated ChatGPT Deep Research mode;
- broad/exhaustive external literature search;
- citation chaining;
- systematic related-system survey;
- evidence saturation;
- a minimum research duration/source corpus.

Therefore “Deep-Research-/Systemanalyse-Prompt” is currently an aspirational task description, not an execution guarantee.

No solution or prompt revision is decided in this assessment.
