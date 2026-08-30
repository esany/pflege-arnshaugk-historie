# C9 – Capability Allocation: Mensch, deterministische Software, spezialisierte Verfahren, KI und externe Fachprüfung

**Work Owner:** #39  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** Research Software Engineering, Software Architecture, AI/ML Evaluation, Quality Engineering, Research Integrity.  
**Controlling competencies:** jeweilige führende Fachdomäne, Human Factors, RDM/Provenienz, Legal/Rights/Data Governance.

## 1. Research Questions

RQ-C9-01 bis RQ-C9-05:

1. Nach welchen Kriterien werden Capabilities zwischen Mensch, deterministischer Software, spezialisierten Verfahren und GenAI verteilt?
2. Für welche probabilistischen Outputs ist Candidate→Review→Promotion sinnvoll?
3. Welche Kerninvarianten müssen deterministisch bleiben?
4. Wann reuse/integrate/build und welche Portabilitätsgrenzen?
5. Welche Rights/Data-Governance-Fragen sind Admission Criteria vor Cloud-/AI-Verarbeitung?

## 2. Search Scope / Boundary

Geprüft wurden:

- NIST AI RMF / GenAI Profile (aktueller Stand 2026) zu Confabulation und Risikomanagement;
- Human-AI-Interaction-Prinzipien aus C8;
- Research Software Engineering/Sustainability zu Testing, Reproducibility, Reuse und Versionierung;
- FAIR for Research Software als Wiederverwendungs-/Interoperabilitätsreferenz;
- local-first als Architekturprinzip für Ownership/Offline/Provider-Unabhängigkeit;
- Ergebnisse C1–C8 als führende fachliche Requirements-Inputs.

Nicht beansprucht wird eine finale Zielarchitektur oder Produkt-/Providerwahl.

## 3. Inspected sources

- NIST, **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)**, 2024, page updated 2026-04-08: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST AI RMF current page: https://www.nist.gov/itl/ai-risk-management-framework
- Microsoft Research, **Guidelines for Human-AI Interaction**: https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- Software Sustainability Institute, **Testing your software**: https://www.software.ac.uk/guide/testing-your-software
- Software Sustainability Institute, **Manifesto**: https://www.software.ac.uk/about-us/manifesto
- SSI, **FAIR Principles for Research Software Released**: https://www.software.ac.uk/news/fair-principles-research-software-released
- FAIR4RS v1.0 DOI: https://doi.org/10.15497/RDA00068
- Kleppmann et al., **Local-first software: You own your data, in spite of the cloud**: https://www.inkandswitch.com/essay/local-first/

## 4. Findings

### F-C9-01 – Generative AI has a structurally different risk profile from deterministic/software checks

NIST defines GenAI **confabulation** as confidently generated erroneous/false content and explicitly notes risks of fabricated logic/citations, especially in contextual/domain-expertise tasks and consequential decisions.

For Histo-Orla this is not an argument against GenAI. It is an allocation rule:

```text
if output must be exact/reproducible/formally valid
→ do not delegate ownership to generative model
```

Examples:

- hash/checksum;
- source ID / known findspot mapping;
- file existence;
- schema/status transition;
- rights flag already recorded;
- query/filter execution;
- version history;
- exact citation formatting from known metadata;
- promotion rule.

GenAI may explain these states, not own them.

### F-C9-02 – Narrow probabilistic methods and GenAI are different technical classes

C7 strongly supports specialized procedures for:

- OCR/HTR;
- layout analysis;
- fuzzy matching;
- historical spelling matching;
- IR ranking;
- embeddings;
- entity/gazetteer candidates;
- statistical classifiers.

These methods are probabilistic but typically have **narrower measurable objectives** than an LLM doing an open semantic task.

Histo-Orla should therefore not use the binary:

```text
human vs AI
```

but at least:

```text
Research Owner
Qualified Scholarly Specialist
Deterministic Software
Specialized Algorithm / Classical ML / IR / OCR / GIS
Generative AI / LLM
External Systems/Services
```

### F-C9-03 – Work allocation should follow task epistemics, not implementation fashion

Decision rules v0.1:

#### Deterministic software preferred when

- formal rule exists;
- bit-/state-reproducibility matters;
- integrity/state transition is involved;
- exact matching/counting/filtering is sufficient;
- validation can be encoded as invariant.

#### Specialized algorithm/ML preferred when

- task is narrow pattern recognition;
- benchmark/ground truth can be defined;
- confidence/error classes are measurable;
- method outperforms hand-written rules.

#### Generative AI useful when

- task is open semantic exploration;
- user does not know terminology/problem frame;
- multiple hypotheses/queries need generating;
- explanation/translation of complex research state is needed;
- structured synthesis of already evidenced material adds value.

#### Fachspezialist required when

- inference standard is disciplinary;
- ambiguity/controversy is consequential;
- expert validation status is claimed;
- source requires specialist reading not benchmarkably delegated.

#### Research Owner required when

- project goal/scope/value trade-off is normative;
- residual risk is consciously accepted;
- publication/use consequence changes review level.

### F-C9-04 – Candidate→Review→Promotion is the default safe pattern for open/probabilistic semantic work

For C2/C3/C4/C5 and entity/relation extraction, outputs should initially be **candidates**, e.g.:

- Fachbegriff candidate;
- archive/source candidate;
- entity match candidate;
- place/gazetteer candidate;
- relation candidate;
- motive/explanation candidate;
- OCR correction candidate;
- claim extraction candidate.

Promotion depends on task-specific verification:

```text
input + provenance
→ probabilistic/generative candidate
→ candidate state with method/version/reason
→ deterministic / algorithmic / scholarly check
→ human review proportional to consequence
→ promoted canonical state OR rejected/deferred
```

**Not every candidate needs manual click approval.** Promotion may be automatic where a deterministic/benchmarkable check makes the residual risk acceptably low. The governing rule is consequence- and domain-based validation, not universal manual workflow.

### F-C9-05 – AI-negative core is scientifically justified

The following should not have generative AI as canonical owner:

- Source/record identifiers;
- file/instance hashes where used;
- source↔derivative links;
- known page/folio/findspot mapping;
- file integrity;
- version history;
- access/rights flags;
- workflow/promotional status;
- deterministic validation results;
- processing/query logs;
- reproducibility metadata;
- backup/restore state;
- explicit user/owner decisions.

LLM may **read, summarize and propose changes**, but mutations pass a deterministic state-changing interface with validation.

### F-C9-06 – Research software engineering is not merely implementation cleanup; it protects research results

SSI explicitly links testing/documentation/version control/reproducibility to confidence in research software outputs. For Histo-Orla:

- architecture-driving invariants need automated tests where formalizable;
- regression tests should use U1–U4 Gold/Acceptance cases;
- software version/configuration relevant to a consequential derived result must be reconstructible;
- silent software/model behavior changes are material when they can change Research State.

This validates Dev as full implementation discipline after requirements, while preserving scholarly ownership of rules.

### F-C9-07 – Reuse/integrate before build is a strong Lean rule, not an absolute prohibition on custom software

C7 already found strong reuse candidates (Zotero, OCR/HTR engines, PAGE/ALTO-style standards). FAIR4RS/SSI emphasize reuse, interoperability, versioning and sustainability.

For every technical capability, compare:

1. **reuse as-is**;
2. **configure/adapt/integrate**;
3. **thin wrapper/adapter**;
4. **small custom component**;
5. **new substantial subsystem** only if evidence requires it.

Decision factors:

- scholarly requirement fit;
- findspot/provenance integrity;
- reversibility/data export;
- local/offline needs;
- rights/privacy;
- maturity/community/maintenance;
- testability;
- API/open formats;
- cost;
- observed performance need.

Power/features that do not solve validated Needs count as complexity, not benefit.

### F-C9-08 – Local-first is a strong portability pattern, but not a universal architecture requirement yet

Local-first research argues for user data ownership, offline operation and survival if a server disappears. This matches Histo-Orla goals G-008/K-002 and the user’s personal research workflow.

However:

- some high-quality HTR/AI/archive services are cloud-based;
- collaboration/sync/backup can be valuable;
- local-only could increase maintenance burden.

Thus the requirement should be **provider-independent durable research state / exportability / restartability**, not prematurely „every computation runs locally“.

Potential architecture preference later:

> canonical curated state remains portable/user-controlled; cloud services may be replaceable processors/integrations.

### F-C9-09 – Rights/privacy are Admission Criteria, not post-hoc documentation

Before a source/derivative is uploaded to external OCR/AI/storage service, Histo-Orla must know enough to answer:

- Is external processing permitted by archive/license/contract?
- Is material public-domain, licensed, private, embargoed or unclear?
- Does it include personal/sensitive modern data?
- Where is service processing/storage located and retained?
- Can output/derived text be stored/reused/exported?
- Does provider use input for training or other purposes, if contractually relevant?

At this stage there is no universal answer because rights depend on source, archive and service. Therefore architecture must support **rights-aware routing** rather than assume uploadability.

### F-C9-10 – Model/provider changes need consequence-aware revalidation

Because GenAI/embedding/OCR models change, Histo-Orla needs:

- model/tool/version identification where relevant;
- benchmark suite before replacing architecture-driving processor;
- regression against Gold Cases;
- no silent reprocessing/promotion of canonical state;
- ability to regenerate derivatives from retained source + configuration where feasible.

This follows NIST risk management, SSI reproducibility and #12 material-change prior art.

## 5. Capability Allocation Matrix v0.1

| Capability / task | Preferred owner/actor | Supporting actor | Canonical promotion rule |
|---|---|---|---|
| define research goal/scope | Research Owner | Coordinator | explicit owner decision when material |
| translate fuzzy observation to problem candidates | GenAI/Research Coordinator + domain retrieval | Fachdomäne | candidate until domain/evidence check |
| define scholarly term meaning/validity | Fachdomäne | retrieval/LLM explanation | profile/SOTA evidence |
| archive/source discovery | deterministic search + GenAI heuristic candidate | Archivistik | find-aid discovery status; inspect before evidence promotion |
| source identity/provenance | deterministic system + Archivistik | LLM explanation | formal validation + scholarly source status |
| OCR/HTR | specialized engine | human/palaeographic review | benchmark/quality threshold; derivative status |
| OCR correction | specialized/LLM candidate | human/rules | candidate/review according to consequence |
| exact/fuzzy/historical search | IR engine | C2 vocabulary | deterministic/reproducible query log |
| semantic retrieval | embedding/search model | lexical baseline | admitted only after benchmark; never source evidence alone |
| entity/place matching | specialized matching + LLM candidate | domain/owner | ambiguity/threshold + review |
| relation extraction | LLM/rules candidate | source/domain method | evidence-backed promotion; proxy distinction |
| source dependence | scholarly method + assistance | citation/text analysis | explicit evidence/status |
| historical interpretation | Fachdomäne | LLM synthesis/retrieval | L1/L2/L3 validation depending consequence |
| actor motive/explanation | Fachdomäne | LLM alternative generation | cannot auto-promote strong motive claim |
| uncertainty/controversy view | deterministic view of Research State | LLM explanation | must not change underlying state |
| canonical state mutation | deterministic validated interface | AI/user proposal | invariant checks + authorization |
| external expert validation | qualified independent specialist | system evidence package | explicit L3 status |
| issue/research artifact persistence | deterministic/Git tooling + assistant | Research Owner review only if material | §14 one canonical home |

## 6. Deterministic Invariant Catalogue v0.1

Where known/applicable, software should be able to reject invalid state such as:

1. consequential Finding with no Source/Evidence link when source evidence is required;
2. OCR derivative promoted as Original;
3. find-aid discovery labeled `inspected source`;
4. Research View back-writing mediation text into canonical finding without promotion path;
5. `independent expert validated` without explicit external validation record;
6. dependent source automatically counted as independent corroboration;
7. historical relation created solely from co-presence proxy without relation status/evidence;
8. raw OCR overwritten by normalized correction;
9. source/derivative orphaning on file update;
10. material processor/model change without benchmark/revalidation flag where required.

Exact implementation waits for requirements/data model.

## 7. Build / Integrate / Reuse Admission Test

For every proposed technical component:

```text
A. Which validated Need/Pain/Requirement?
B. Which scholarly owner defines correctness?
C. Can existing tool/standard satisfy it?
D. Smallest integration that works?
E. How is quality tested on U1–U4?
F. What data/knowledge lock-in?
G. Can component be replaced without losing curated Research State?
H. What rights/privacy constraints?
I. What maintenance/operational burden?
J. What evidence would justify a more complex solution?
```

If A/B/E are unclear: do not build yet.

## 8. AI Admission / Evaluation Criteria

GenAI/LLM is admitted to a capability only if:

1. task has meaningful open-semantic component;
2. simpler deterministic/specialized method is insufficient;
3. expected user/research gain is explicit;
4. failure mode is bounded/observable;
5. candidate/output provenance can be retained;
6. canonical promotion is separately controlled;
7. evaluation cases/criteria exist;
8. model/provider can be replaced without losing curated research knowledge.

## 9. Capability Candidates

- `CAP-RESPONSIBILITY-ALLOCATION`
- `CAP-CANDIDATE-PROMOTION`
- `CAP-DETERMINISTIC-INVARIANTS`
- `CAP-RIGHTS-AWARE-PROCESSING`
- `CAP-REPLACEABLE-PROCESSORS`
- `CAP-REPRODUCIBLE-TOOLING`
- `CAP-PORTABLE-RESEARCH-STATE`
- `CAP-BENCHMARKED-MODEL-CHANGE`
- `CAP-REUSE-INTEGRATION`

## 10. Quality / Requirement Candidates

- REQ-C9-A: Deterministically checkable canonical invariants must not rely solely on LLM judgment.
- REQ-C9-B: Probabilistic/GenAI contributions to canonical research facts require an explicit promotion mechanism proportional to consequence.
- REQ-C9-C: System must distinguish human, specialist, deterministic software, specialized algorithm and GenAI responsibility for material actions/findings.
- REQ-C9-D: Research State must remain exportable/restartable independent of a specific AI/provider/service.
- REQ-C9-E: Architecture must permit replaceable external processors where feasible and preserve curated state across replacements.
- REQ-C9-F: External/cloud processing must support rights/privacy admission before upload/processing.
- REQ-C9-G: Architecture-driving software/model changes require regression/evaluation before silent adoption.
- REQ-C9-H: Existing tools/standards must be evaluated before substantial custom implementation.

## 11. Disposition of major technical hypotheses

| Hypothesis | C9 disposition |
|---|---|
| Zotero as central bibliographic/integration layer | **adapt / strong candidate**, not whole Research State |
| local-first | **principle candidate**: portability/ownership required; all-local computation not yet required |
| SQLite/FTS | **defer to architecture benchmark**; C7 defines retrieval behavior first |
| RAG/embeddings | **optional benchmark-admitted layer**, not baseline |
| Knowledge Graph | **defer**; relational capabilities valid, graph technology not required |
| Multi-Agent | **defer / likely unnecessary initially**; competency modularity does not imply agent plurality |
| Candidate→Review→Promotion | **validated as core governance pattern**, implementation varies by consequence |
| curated versioned state vs regenerable indexes | **strongly supported**, exact storage boundary later |

## 12. Challenge interner Prior Art

`paleo-type` technical subsidiarity/material-change/restartability patterns are strongly supported by RSE/NIST/local-first principles, but local-first is softened from possible dogma to **portability/restartability invariant**.

RGK does not define technical architecture. Its relational patterns can be implemented only after C1–C6 scholarly requirements, and graph technology remains optional.

## 13. Open Questions / bounded debt

- actual cost/privacy/license comparison of concrete OCR/LLM/providers belongs architecture/prototype phase;
- source-specific legal permissions require case-by-case review, not global Research-SOTA conclusion;
- data model/storage/search engine benchmark occurs after #42;
- operational backup/sync strategy after architecture, constrained by portability requirement.

## 14. #45 Quality Check

- **Domain fit:** RSE/AI evaluation lead technical allocation; scholarly owner remains correctness authority.
- **Evidence fit:** NIST/SSI/FAIR4RS/local-first sources directly inspected; C1–C8 provide domain evidence.
- **Inference fit:** local-first and FAIR are treated as design principles/reference, not automatic requirements; GenAI risk does not imply blanket ban.
- **Terminology fit:** deterministic vs specialized probabilistic vs GenAI vs human validation separated.
- **Provenance fit:** candidate/promotion/tool-version/reproducibility requirements explicit.
- **Falsification/challenge:** every technical component must pass need/quality/benchmark/reversibility admission tests.

## 15. Sättigungsbegründung

C9 is sufficient to derive requirements because allocation rules can now be traced to task epistemics and failure modes. Choosing concrete storage/search/model/provider products before #42/#43 would be premature solution design; those choices can be discriminated by architecture prototypes against the validated requirements.
