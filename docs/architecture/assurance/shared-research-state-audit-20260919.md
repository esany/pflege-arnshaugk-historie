# Repo Audit 2026-09-19 – Shared Research State / transdisziplinärer Wissensraum

**Status:** `review input / current-main audit / no new authority`  
**Audit scope:** Repository `esany/pflege-arnshaugk-historie` at main `9643e7a109fa2e6ec66488f04a8785d4b577a825`  
**Relevant owners:** #1 project concept; #42 accepted Requirements; #48 Technical Lead; #50 Canonical Research State; #59 Development; #60 Method Truth; #64 Product/Research Value Audit; #92 Architecture Re-Baseline  
**Research pilots inspected:** #46, #47, #85/#86/#89, #103  
**Purpose:** current-state audit of intent, fachliche Konzepte, accepted Requirements, technical operationalization/assurance, gaps, and the path by which heterogeneous research pilots can feed one shared knowledge base.

This document is an audit/reconciliation view only. It creates no Requirement, Method Truth, historical Finding, Selection Authority or technology decision.

---

## Audit-Caution / spätere Selbstkorrektur 2026-09-20

Der faktische Inventarteil dieses Audits bleibt als Review-Evidenz nutzbar, insbesondere die beobachtete Cross-Case-Fragmentierung (z. B. `SRC-LIT-0001` vs. `ARS-009`) und die Trennung zwischen starker Governance/Assurance und noch nicht integrierter Research-State-Praxis.

**Nicht als bereits etablierter Architekturvertrag zu lesen** sind dagegen die hier relativ bestimmt formulierten Zielobjekte wie globale Entity-/Observation-/Relation-/Discrepancy-Layer, `Case = View` oder eine bestimmte gemeinsame State-Spine. Diese waren Review-Hypothesen und wurden im nachfolgenden kritischen Self-Audit methodisch herabgestuft bzw. genauer eingeordnet.

Aktuelle Korrektur-/Einordnungssicht:

`docs/architecture/assurance/chat-operationalization-self-audit-20260920.md`

Historische Aussagen und PR-/Kommentar-Chronologie bleiben aus Provenienzgründen erhalten.

---

## 1. Executive finding

Histo-Orla already has a strong **epistemic and governance architecture**:

- a clear product/research intent;
- 39 accepted baseline Requirements plus 14 accepted Extensions;
- explicit Source/Representation/Instance/Derivative/Findspot/Finding separation;
- uncertainty, contradiction and competing interpretation as first-class states;
- transdisciplinary evidence-axis separation;
- temporal/multi-scale place semantics;
- Domain Method Profile governance;
- provider/chat-independent canonical-state requirements;
- deterministic Requirements/Decision/Delivery assurance;
- a bounded executable document/findspot model;
- tested operational helpers for audit, context, mutation and enforcement.

The central missing layer is not another governance framework. It is the **shared, reusable canonical Research State itself**.

Today, substantial historical state is still primarily persisted in case-specific Markdown ledgers/registers and bounded JSON fixtures. This works for rigorous case research, but it does not yet guarantee that different pilots reuse the same Source, Entity, Observation, Relation, Claim or Discrepancy identities.

Concrete evidence of the gap: Peter Sachenbacher's *Thüringen östlich der Saale im Mittelalter* is the shared Orlagau Source `SRC-LIT-0001`, while #103 independently records the same work as `ARS-009`. This is a correctable local duplication, but it demonstrates that pilot-local source identity can become parallel canonical identity unless cross-case resolution is made operational.

The correct next integration problem is therefore:

> **How can multiple questions, periods, disciplines and pilots append to one provenance-safe regional Research State while keeping disciplinary semantics, temporal validity, contradictions and research history intact?**

---

## 2. Project intent / generic ideas already present

The current project intent is coherent and already substantially documented in #1, README, the foundational research-design document, #13/#14/#16 and the accepted Requirements.

### 2.1 Product intent

Histo-Orla is a private, durable research environment for **transdisciplinary historical research**, not an AI demo, a bibliography manager or a single-case database.

The user may ask imprecisely; the system must translate that into scientifically appropriate concepts, domains, methods, evidence needs and research actions.

### 2.2 Regional anchor, open explanatory horizon

The regional development of Orla/Saalfeld/eastern Thuringia is the organizing anchor, not an analytical container. Supraregional, imperial/state, European or global contexts enter when a historically grounded relation makes them relevant to regional development.

The current foundational design now explicitly supports a roughly **2000-year diachronic research horizon**, including medieval, early-modern, nineteenth-/twentieth-century, DDR and transformation-history questions, together with archaeological, building-historical, technical, scientific and textual evidence.

### 2.3 Shared knowledge, changing questions

A Research Question or Work Context should **reference evidence, not own it**. This is already the key learning of #86/#88.

The same source, observation or entity may be relevant to multiple questions, disciplines and periods. Cases are views/work contexts over a shared state, not separate copies of truth.

### 2.4 Epistemic plurality, not flattening

The project explicitly rejects a universal single disciplinary vocabulary.

Diplomatics, archaeology, building history, environmental history, legal history, prosopography, modern political history, press history, etc. may produce different evidence objects and inference limits. A shared core must preserve those differences rather than flatten them.

### 2.5 Contradiction is legitimate state

`unresolved`, genuine contradiction, competing interpretation, evidence gap, rejected identity and superseded findings are legitimate persisted states. Research does not have to converge prematurely to one narrative.

### 2.6 Lean technical subsidiarity

Technology is downstream of Needs/Requirements/Domain Method.

Existing tools and standards should be reused before custom infrastructure. KG/RAG/vector DB/multi-agent/graph DB are not requirements. Architecture evolves from real research pains and discriminating slices.

---

## 3. Existing fachliche / epistemic concepts

The repo already distinguishes, at concept or Requirement level:

| Concept | Current canonical basis | Audit status |
|---|---|---|
| Domain owns method/evidence standard | REQ-EPI-001, #60 | accepted; concrete profiles still incomplete |
| Problem translation / concept discovery | REQ-EPI-002/003 | accepted |
| Uncertainty / contradiction / controversy | REQ-EPI-004, REQ-CRIT-002 | accepted |
| AI is not evidence / independent validation | REQ-EPI-005 | accepted hard constraint |
| Source vs representation vs inspected instance | REQ-SRC-001/002, source-identity protocol, #50 | accepted + architecture contract |
| Editorial intervention distinct from source wording | REQ-SRC-003 | accepted |
| Exact findspot / roundtrip | REQ-SRC-004, #51 | accepted; bounded technical slice exists |
| OCR/HTR as derivative with parentage | REQ-OCR-001/002/003 | accepted; implementation mostly pending |
| Exact/auditable retrieval before semantic retrieval | REQ-RET-001–005 | accepted; implementation pending |
| Source dependence / false corroboration | REQ-CRIT-001 | accepted |
| Entity candidate→promotion / false-merge protection | REQ-ENT-001 | accepted; transition implementation pending |
| Proxy/co-presence ≠ historical relation | REQ-REL-001 | accepted |
| Places/territories are temporal contexts | REQ-SPAT-001 | accepted |
| Action, motive, attribution and structure separated | REQ-ACT-001 | accepted |
| Multiple evidence axes remain distinct | REQ-SYN-001 | accepted |
| Synthesis preserves alternatives | REQ-SYN-002 | accepted |
| Human-readable audit/challenge | REQ-UX-001/002/003 | accepted; partial executable support |
| Consequence-based validation | REQ-VAL-001/002 | accepted |
| Deterministic guards for formal invariants | REQ-WF-001 | accepted; partially implemented |
| Restartable/reproducible workflows | REQ-WF-002 | accepted; incomplete |
| Provider-/chat-independent canonical state | REQ-STATE-001/002/003 | accepted; architecture defined, runtime incomplete |
| Integration escape hatch | REQ-INT-001/002 | accepted |
| Rights/privacy processing admission | REQ-RGT-001/002 | accepted; implementation pending |
| Research/mediation boundary | REQ-BND-001 | accepted |
| Domain Method Profile + Method Application | REQ-MTH-001–005, #60/#61 | accepted; Method Truth still research-needed |
| Research Hook ≠ hypothesis ≠ finding | REQ-RSCH-001–004 | accepted |
| Driver→Requirement→Decision→Delivery→Feedback | REQ-TRACE-001, #63 | accepted + implemented formal trace layer |

This is already a substantial domain model, even though it is deliberately not yet a physical database schema.

---

## 4. Technical operationalization and assurance

### 4.1 Requirements assurance – real executable state

Existing:

- `tools/requirements/requirement-record.schema.json`
- `tools/requirements/data/records.json`
- `tools/requirements/validate.py`
- regression tests
- CI integration

This verifies formal Requirement IDs, references, dependency/authority rules, coverage and lifecycle invariants. It does not decide historical or scholarly truth.

Current test suite contains 14 Requirements-assurance test methods.

### 4.2 Value / Decision / Delivery / Feedback assurance

Existing:

- `tools/assurance/trace-record.schema.json`
- `governance-registry.json`
- `policy.json`
- `trace-records.json`
- deterministic validator
- changed-code guard
- CI integration

This protects the chain from Goal/Need/Pain through accepted Requirement and technical implementation to Verification/Owner feedback.

Current suite contains 16 assurance test methods.

### 4.3 Operational support core

Existing under `tools/operational/`:

- common loaders/core utilities;
- Requirement→Enforcement projection;
- Work Context derivation and prerequisite revalidation;
- bounded safe mutation;
- derived Research Audit rendering;
- negative regression tests.

The current operational test suites contain 39 test methods.

Important: this is **support infrastructure**, not yet a shared canonical historical data store.

### 4.4 Document / Findspot contract

#51 has a bounded real-source implementation using Sachenbacher 2022:

- Source / Representation / concrete inspected Instance;
- byte hash;
- print/PDF mapping;
- normalized page coordinates;
- map/text/caption/footnote roles;
- human-reviewed locator corrections;
- a canonical Finding reference;
- deterministic roundtrip tooling.

Current document-evidence suite contains 13 test methods.

This is the most concrete implementation of the Source→Instance→Findspot part of the canonical-state contract.

### 4.5 Derived Audit View

`tools/operational/audit.py` already expects a logical state with:

- `sources`
- `representations`
- `instances`
- `derivatives`
- `excerpts`
- `findings`
- `claims`
- `method_applications`

It renders Claim→Finding→Excerpt/Findspot→Instance→Representation→Source→Method and exposes missing references as `missing/unresolved`.

This is an important embryonic generic Research-State projection.

However, the state used here is currently a **test/regenerable projection**, not a canonical persistent store.

### 4.6 Work Context

A real bounded Work Order exists for Lampe Nr. 420:

`docs/research/cases/u2-lampe-420-work-order.json`

It contains objective, scope, exclusions, leading domains, method/quality frame, required evidence, prerequisite Git-blob fingerprints, unresolved items, allowed/forbidden actions, return condition and persistence targets.

This is a strong restartability pattern, but it references case artefacts rather than a generic shared state service/store.

### 4.7 CI

`.github/workflows/project-assurance.yml` executes:

- Requirements tests;
- Assurance tests;
- Operational-core tests;
- document-evidence tests;
- formal Requirements validation;
- value/decision/delivery validation.

Current source contains 82 test methods across these four suites (14 + 16 + 39 + 13).

The latest inspected PR assurance run (#206, PR #108) succeeded.

---

## 5. What is conceptually strong but not yet operationally complete

### 5.1 Domain Method Profiles

#60 and the Method Profile contract are strong and explicit, but concrete SOTA-backed working/validated profiles are still incomplete.

This matters because a shared data spine alone cannot decide whether an archaeological, diplomatic, architectural or twentieth-century source supports a particular inference.

### 5.2 Provider resolution / bibliography / bytes

#49 has useful Zotero evidence and a clear responsibility split:

`OneDrive = bytes; Zotero = bibliography/reference; Histo-Orla = research state`.

But reliable device-independent byte/instance resolution and integrity across the target workflow remain incomplete.

### 5.3 Historical retrieval

REQ-RET-* and #53 are well specified but the exact/variant/query-log/findspot retrieval baseline is not yet a real cross-case product path.

### 5.4 OCR/HTR

Processor contract/benchmark is planned. No general research-critical OCR/HTR path is active yet.

### 5.5 Rights / privacy

The semantic requirement exists; technical admission enforcement is still planned.

### 5.6 Restartability / availability

There are strong Work Context and fresh-context patterns, but REQ-STATE-001/003 are not yet satisfied as a complete provider-independent product path.

---

## 6. Audit of the current research pilots

### #46 U2 Knau/Orlagau

Strengths:

- deepest current source/evidence work;
- shared `orlagau-source-ledger.md`;
- exact excerpt dossiers;
- Findings with IDs `F-U2-001...`;
- source criticism, homonym protection, negative-boundary discipline;
- real Work Order and document-evidence slice.

Limitation:

- much of the canonical historical state still lives in structured Markdown rather than a generic shared state.

### #47 U1 Teich-/Feuchtlandschaft

Strengths:

- shares part of the Orlagau source/search space with #46;
- explicitly uses separate evidence axes and cross-period landscape questions.

Limitation:

- shared reuse is primarily by shared files/conventions, not by common canonical object identity for all evidence/entities/findings.

### #103 Anno/Richeza/Saalfeld

Strengths:

- observation-first research;
- explicit Observation and Relation registers;
- separate Source Ledger;
- contradictions/unresolved status preserved.

Critical cross-case gap:

- it created a new case-local source namespace `ARS-*`.
- Sachenbacher 2022 appears as `ARS-009`, while the existing shared Orlagau ledger already identifies the same bibliographic work as `SRC-LIT-0001`.
- relations reference entity names rather than globally stable entity IDs.

This is the clearest current evidence that good case methodology does **not yet automatically feed a shared knowledge base**.

### #85 Ranis material-corpus pilot

Strength:

- explicitly organizes heterogeneous material by Source/Instance, Space, Time, Material/Evidence axis, Inspection status and relations/hooks.

This is close to the desired long-term research-space concept, but remains branch-isolated and has no main authority.

### #86/#88 Shared Research State pilot

Most relevant generic finding:

> Research questions reference evidence; they do not own it.

The prototype showed that the same Ranis Evidence ID can support multiple Work Contexts and derived views without copy.

It deliberately rejected:

- a compulsory `ResearchModule` object;
- a new question-state machine;
- a new relation ontology;
- a graph/backend decision.

This is a good architectural constraint.

But #89 fresh-context evaluation is still the closure gate, and the pilot remains isolated from main.

---

## 7. Main gap: no shared canonical Research-State implementation

The repo currently has **three layers that do not yet fully meet**:

1. **Strong semantic contract** (#42/#50/#60)
2. **Strong case research** (#46/#47/#103 and branch pilots)
3. **Strong formal assurance/tooling** (#62/#63/`tools/operational`)

What is missing between them is a common canonical data path.

### 7.1 No global source resolution / aliasing path

There is no operational mechanism that says:

`ARS-009 candidate source` → resolve against existing canonical sources → reuse `SRC-LIT-0001`.

Without this, each pilot can create locally valid but globally duplicate Source IDs.

### 7.2 No global Entity identity layer

REQ-ENT-001 exists, but the current canonical contract does not yet require a persistent shared entity registry as part of the implemented minimum.

For a 2000-year regional knowledge space, stable identities/identity-candidates for places, persons, institutions, objects, buildings, landscape elements etc. are necessary for reuse across questions.

They must support:

- aliases/historical names;
- temporal validity;
- candidate identity;
- merge/split history;
- rejected homonyms;
- external authority refs without outsourcing canonical identity.

### 7.3 Observation is not yet a shared executable first-class object

#103 correctly uses atomic Observations; the generic audit code currently jumps from Excerpt to Finding.

The architecture contract names Findspot/Excerpt/Observation together, but no generic persistent Observation contract/store is implemented.

For cross-disciplinary research this is important because:

`source-near observation != domain finding != claim/interpretation`.

### 7.4 Relation / event / temporal assertion state is not implemented generically

REQ-REL-001 and REQ-SPAT-001 exist, but there is no shared runtime/persistent representation for temporal relations/events with evidence links.

#103 relation rows are currently case-local Markdown.

### 7.5 Discrepancy / contradiction is accepted semantically but not structurally implemented

REQ-EPI-004 / REQ-CRIT-002 require contradiction as state. The generic executable state has uncertainty/alternatives fields but no current canonical cross-case Discrepancy object/relationship.

### 7.6 No cross-case query/navigation layer

The repo can audit one synthetic/derived claim chain, but it cannot yet answer from one common persisted state:

- all observations about Saalfeld across cases;
- all sources reused by multiple questions;
- all unresolved identity conflicts around an entity;
- all evidence/claims for one place across 1000 years;
- all contradictions between archaeology, written sources and building history;
- all research hooks generated by a given observation.

### 7.7 Markdown is doing too much canonical data work

Markdown is excellent for human-readable Research Truth and remains valuable.

But today it also carries IDs, source records, observations, relations and findings in case-specific tables/prose. That makes global referential integrity, deduplication, temporal querying and shared identity hard to enforce.

The problem is not Markdown itself. The problem is lack of a **single structured canonical projection or store** behind/across the Markdown views.

### 7.8 Product Runtime remains absent

There is intentionally no `src/histo_orla/` today. All executable logic is support tooling.

This is not automatically wrong, but a persistent shared Research State plus resolution/query/transition operations may become the first justified durable Product Capability that crosses the current `tools/` boundary.

That decision belongs to #48/#58 only after the need is accepted and a thin slice demonstrates it.

---

## 8. Technology-neutral target: shared epistemic spine + disciplinary lenses

The shared knowledge base should **not** be one flattened universal ontology.

The smallest useful shared logical spine is:

```text
Source
→ Representation
→ Inspected Instance
→ Derivative
→ Findspot / Excerpt
→ Observation
→ Finding
→ Claim / Interpretation

plus shared references to:
Entity / Entity Candidate
Temporal-Spatial Context
Relation / Event Assertion
Discrepancy / Competing Claim
Method Application
Review / Validation / Transition History
Work Context / Research Question
```

Important ownership rule:

```text
Research Question / Work Context
= selects, references, asks, routes evidence demand
≠ owns or copies evidence
```

Discipline-specific semantics sit **around** this shared spine through Method Profiles, typed observations/findings and domain-specific extensions. They must not be forced into one universal relation vocabulary.

---

## 9. How all pilots can feed the same knowledge base

Recommended generic flow, still technology-neutral:

```text
Pilot / Work Context
  ↓
discover or inspect Source/Instance
  ↓
resolve identity against shared canonical IDs
  ↓
append source-near Observation with exact provenance
  ↓
link existing Entity IDs or create Entity Candidates
  ↓
create domain Finding(s) via explicit Method Application
  ↓
create Claim / Relation / Event / Discrepancy candidates as needed
  ↓
review / promote / demote / supersede without deleting history
  ↓
derive case view, timeline, network, map, audit or synthesis
  ↓
other Work Contexts reuse the same IDs
```

### What remains case-specific

- Research Question;
- scope/exclusions;
- evidence demand;
- method application;
- temporary hooks/queues;
- case-specific synthesis;
- owner priorities.

### What should be shared whenever identity is actually the same

- bibliographic/archival Source identity;
- inspected Instance identity;
- Entity identity/candidates;
- Excerpts/Observations;
- supported Findings where the Finding itself is reusable and scope-compatible;
- contradiction/dependence/history relationships;
- provenance and availability state.

---

## 10. Best next discriminating slice

Do **not** begin by selecting a database or graph technology.

Use a real cross-case collision already present:

### Slice A – Sachenbacher / Saalfeld cross-case reuse

Inputs:

- #46 shared source `SRC-LIT-0001`;
- #103 duplicate `ARS-009`;
- #51 inspected Sachenbacher Instance and Findspot reference model;
- Saalfeld as a shared regional entity across #46/#103.

Acceptance:

1. one canonical Source identity is used by both Work Contexts;
2. the old case-local ID is preserved as alias/history, not silently deleted;
3. both cases can reference the same inspected Instance where applicable;
4. case-specific Observations/Findings remain distinct;
5. Saalfeld identity is reused without forcing all historical meanings/territorial contexts into one static record;
6. a derived #46 view and a derived #103 view can be regenerated from the shared state;
7. no historical Claim changes merely because identity was deduplicated;
8. rollback/export remains possible.

This slice tests the exact problem exposed by the current repo without requiring a broad migration.

---

## 11. Gap register / routing

| Gap | Severity | Existing owner path |
|---|---|---|
| Explicit shared cross-question Research-State requirement/refinement | fundamental | #42 |
| Canonical cross-case Source identity resolution / aliases | P0 | #50 + #49/#59 |
| Observation as generic first-class shared state | P0 | #42/#50, informed by #103 |
| Shared Entity candidate/identity/merge-split state | P0 | REQ-ENT-001 → #50/#54/#59 |
| Temporal Relation/Event assertion state | P0/P1 | REQ-REL-001/REQ-SPAT-001 → #50/#60/#59 |
| Discrepancy/contradiction object/links | P0/P1 | REQ-EPI-004/REQ-CRIT-002 → #50/#55/#60 |
| Cross-case query/navigation | P1 | #53/#55 |
| Domain Method Profiles | scientific blocker for consequential promotion, not exploration | #60 |
| Provider-independent byte/availability resolution | P0 integration | #49/#57 |
| Rights admission | P0 before relevant external processing | #56 |
| OCR/HTR real path | need-triggered | #52 |
| Persistent implementation / product-code boundary | architecture decision after slice | #48/#58/#59 |
| Pilot #86 fresh-context closure | pilot hygiene | #89 → #86/#85 |

---

## 12. Audit conclusion

The project is **not conceptually underdesigned**. In several areas it is already more rigorously specified than the current product implementation needs.

The primary risk is now the opposite: continuing to expand governance/Markdown case structures while the common Research State remains implicit.

The next value-bearing integration should therefore be:

> **make one small cross-case part of the already-defined canonical Research State real, shared and reusable, then prove that two different Research Work Contexts can read/write it without epistemic loss.**

No graph database, RDF stack, SQL store, ontology platform or new agent framework is implied by this conclusion. The storage choice remains an architecture question after the cross-case semantics and acceptance are demonstrated.
