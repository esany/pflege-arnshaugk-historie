# Histo-Orla – Research Workspace Structure Candidates

**Status:** `owner-input / architecture-candidate / not-yet-accepted`  
**Date:** 2026-09-10  
**Primary routing:** #48  
**Affected work owners:** #49 Zotero integration, #50 canonical research state, #55 human-readable audit/read view  
**Inputs:** owner discussion on Zotero, Exzerpte, Regesten/Editionen, multi-topic source use and read-only workspace views; existing contracts/requirements listed below.

## 1. Purpose and authority boundary

This document persists a set of owner-driven workflow and architecture candidates that sharpen existing Histo-Orla concepts.

It is **not** an accepted Requirement, ADR, target architecture or implementation decision. It must not silently supersede #42, #50 or existing source/evidence rules. Its purpose is to preserve the user/workflow intent so #49/#50/#55 can disposition it explicitly.

## 2. Existing canonical foundations already in the repository

The following are not new proposals:

- `Source / Work / Archival Unit → Representation → Inspected Instance → Derivative → Findspot / Excerpt / Observation → Finding → Claim / Interpretation / Synthesis` are distinct layers.
- `Regest != Urkunde`, `Edition != Original`, and editorial intervention/normalization must not overwrite historical wording.
- Excerpts/findspots require precise provenance and round-trip to the used source/instance as far as the medium allows.
- AI output is not evidence or independent validation.
- OneDrive is currently the Source of Bytes.
- Zotero is currently the preferred bibliographic/archival management and reference layer.
- Histo-Orla owns the scientific research state, especially findings/claims/discrepancies/validation state.
- #55 already requires a human-readable read-only view generated from canonical state without creating a second manually maintained truth.

Relevant canonical sources:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/source-identity-protocol.md`
- `docs/architecture/contracts/canonical-research-state.md`
- #49, #50, #55

## 3. New or materially sharpened owner-input candidates

### CAND-RWS-01 — Zotero as SSOT for bibliographic/archival records

Owner intent:

> Zotero should at least be the single source of truth for bibliographic/archival **entries**.

Candidate consequence:

- Histo-Orla should not maintain a competing full bibliographic record when Zotero owns that record.
- Histo-Orla may retain the minimum provider-independent identity/provenance needed for restartability, provider removal and scientific traceability.
- The boundary between “Zotero record truth” and “minimum Histo-Orla identity snapshot/reference” remains to be specified.

This is stronger than current `REQ-INT-002` / #50 wording (“preferred bibliographic/archival management and reference layer”) and therefore requires explicit disposition before becoming binding.

### CAND-RWS-02 — Bidirectional Zotero enrichment

Candidate workflow:

```text
existing Zotero record
→ Histo-Orla reads bibliographic metadata/tags/notes
→ research use

and

edition / regesta volume / source corpus
→ Histo-Orla identifies relevant addressable records
→ structured import candidates
→ duplicate/identity/uncertainty checks
→ explicitly authorized Zotero write
```

Example: a Dobenecker volume can be inspected and relevant individual regesta can become structured Zotero candidates rather than remaining only transient search hits.

This is a concrete specialization of #49 AQ-ZO-08; no Zotero write capability or write policy is accepted by this document.

### CAND-RWS-03 — Candidate-before-write for Zotero

No discovered record should silently become a Zotero item.

A write candidate should preserve at least the information necessary to review:

- target Zotero item type;
- source work/edition;
- addressable unit (e.g. regest/charter number);
- date/place where supported;
- creator/issuer/recipient roles only where methodically justified;
- exact provenance/findspot;
- proposed tags/collections;
- uncertainty/unresolved identity;
- duplicate/reconciliation key;
- generated vs. source-supplied fields.

Write requires explicit authorization and conflict/version handling.

### CAND-RWS-04 — Split by scholarly/addressable unit, not by file/book size

Do not split a large work merely because it is large.

Examples:

- a monograph such as Sachenbacher remains one bibliographic Zotero book item unless a part is independently bibliographic/citable in its own right;
- chapters/passages of the monograph are normally represented as findspots/excerpts, not duplicate bibliographic records;
- an individual regest or charter in a regesta/edition volume may be an independently addressable source/representation unit and may justify its own Zotero record if that improves scholarly retrieval and citation.

The discrimination criterion is scholarly/bibliographic addressability and identity, not page count or file boundaries.

### CAND-RWS-05 — Explicit text-representation chain

For historical source work, the practical model should make the following differences explicit where applicable:

```text
historical wording (Latin / MHG / other source language)
→ scholarly/editorial transcription or edition
→ editorial regest
→ normalization
→ translation
→ exact excerpt
→ observation
→ finding
→ interpretation / synthesis
```

A translation is a provenance-bound derivative, not historical wording. A regest is an editorial representation, not the charter itself. A verbatim quotation/excerpt must remain distinguishable from observation and interpretation.

The canonical contract already supports most of this through Representation/Derivative/Excerpt/Observation/Finding; this candidate asks for the distinctions to be operationally explicit, especially **translation**.

### CAND-RWS-06 — Excerpts belong to source/findspots, not to topics

A source or excerpt can be relevant to many research themes at once.

Candidate invariant:

```text
one canonical excerpt/findspot
→ many topic/person/place/question relations or views
```

Avoid copying the same excerpt into separate canonical topic stores such as “Saalfeld”, “Herrschaft”, “Siedlung”. Topics are relations/views over research objects, not owners of the evidence object.

Example:

```text
Excerpt E45, Sachenbacher pp. 137–139
├─ relevant_to: Saalfeld
├─ relevant_to: settlement history
├─ relevant_to: lordship
├─ relevant_to: monastic property
└─ relevant_to: Orlagau
```

Different findings may legitimately derive from the same excerpt, each with its own inference/method/uncertainty status.

### CAND-RWS-07 — Regenerable read workspace / Obsidian as one candidate implementation

Owner intent: a separate tool would be useful only as a **reading/navigation structure**, because Zotero can document much but becomes hard to navigate at research depth.

Candidate role:

```text
canonical Zotero + Histo-Orla state
→ generated read-only human workspace
→ source-centred / place-centred / person-centred / topic-centred / question-centred views
```

Obsidian is only one possible implementation because Markdown/backlinks make multi-perspective reading convenient. It must not become another SSOT or manually maintained research database.

The view should be disposable/regenerable from canonical state. Other tools or a native Histo-Orla UI remain equally valid candidates.

This candidate aligns with #55 rather than introducing a new scientific state layer.

## 4. Illustrative examples

### 4.1 Dobenecker regest

Possible layering for an individual record:

```text
Zotero bibliographic/archival record
= addressable regest/charter entry and its bibliographic identity

Representation
= Dobenecker editorial regest

Representation / Derivative
= inspected Latin/MHG edition or transcription, if available

Derivative
= modern German translation

Excerpt / Findspot
= exact relevant passage with regest/charter number, page/folio/line where available

Observation
= what is explicitly present in the text

Finding
= methodically supported historical inference

Interpretation
= broader explanation/synthesis across findings
```

A read view may display all of these together, but must not collapse their provenance/status.

### 4.2 Sachenbacher monograph

Candidate model:

```text
Zotero
└─ one Book record for the monograph

Histo-Orla
├─ Excerpt A, pp. x–y
├─ Excerpt B, pp. a–b
├─ Observation(s)
└─ Finding(s)

Read view
├─ source-centred page: all relevant excerpts/findings from Sachenbacher
├─ Saalfeld view: same excerpts where related to Saalfeld
├─ settlement view: same excerpts where related to settlement history
└─ other thematic/person/place/question views
```

No bibliographic splitting is required merely to support many research themes.

## 5. What remains deliberately unresolved

This document does not decide:

- whether `CAND-RWS-01` should amend `REQ-INT-002` or remain an owner architecture constraint;
- exactly which bibliographic/archival entities deserve their own Zotero records;
- Zotero item types or field mapping for charters/regesta;
- how source-language text, transcription, regest and translation should be represented physically;
- whether exact excerpts themselves should ever be mirrored into Zotero Notes;
- Zotero write authorization, conflict handling, audit or rollback policy;
- whether Obsidian is used at all;
- persistence technology for Histo-Orla research state;
- UI implementation.

## 6. Routing / disposition questions

### #49 — Zotero integration

- Test/disposition of Zotero-as-entry-SSOT boundary.
- Candidate-before-write and duplicate/reconciliation semantics for creating/enriching Zotero records.
- Empirical write capability/safety only after explicit authorization.

### #50 — Canonical research state

- Clarify minimum provider-independent bibliographic identity retained by Histo-Orla if Zotero owns bibliographic record truth.
- Decide whether translation deserves an explicit derivative subtype/contract language.
- Review the “one excerpt, many relations/views” principle as a cross-case invariant rather than a topic-specific convention.

### #55 — Human-readable audit/read view

- Evaluate source/person/place/topic/question-centred projections from the same canonical objects.
- Treat Obsidian/Markdown as an implementation candidate only; no second manually maintained truth.

## 7. Non-goals

- no architecture promotion from a single chat/example;
- no automatic Zotero writes;
- no requirement change by implication;
- no Obsidian adoption decision;
- no duplication of source/excerpt/finding truth for UX convenience.
