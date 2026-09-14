# #51 – Sachenbacher Evidence-Model Falsification Spike v0

**Current status (2026-09-14):** `mechanical baseline verified / terminology + publication-object boundary reconciled / exact-instance human acceptance still open / B v0 not complete`

**Work Owner:** #51; technical direction #48; delivery/verification #59; research authority #46; trace #63  
**Originally executed:** 2026-09-04  
**Requirements:** REQ-SRC-001, REQ-SRC-002, REQ-SRC-004, REQ-OCR-002  
**Drivers:** G-004, G-006, N-006, P-004  
**Evidence boundary:** technical experiment against a real published visual argument; no historical, methodological, Requirement or Research-Selection promotion.

Earlier revisions and their exact terminology/coordinates remain available in Git history. This file records the current interpretation of the experiment and supersedes earlier completion language.

## 1. Falsification question

Can the existing sequence

```text
Source → Representation → Inspected Instance → Derivative
→ Findspot/Observation → Finding
```

carry a real visual scientific finding losslessly and reproducibly in a fresh context without new canonical `Page` or `Region` object classes and without parser-specific semantics?

The counter-hypothesis wins if the result depends on hidden manual convention, tool-specific IDs, silent relation errors, loss of publication context or additional canonical object semantics.

## 2. Authority and scope

- Historical authority remains #46. The spike does not decide whether Sachenbacher's model is historically correct.
- #50 provides the source/representation/instance/derivative/findspot contract.
- PyMuPDF is a replaceable mechanical rendering adapter only.
- #51 owns the bounded document/findspot experiment, not Method Truth or historical truth.
- Excluded: Docling, OCR, IIIF, GIS, search, UI, general document pipeline, new Requirements and new canonical object classes.
- A technical reference locator is not an evidence grade, truth status or scholarly validation status.

## 3. Exact inspected instance used by the mechanical baseline

| Field | Value |
|---|---|
| Source | `SRC-LIT-0001` – Sachenbacher 2022 published monograph |
| Representation | `REP-SACHENBACHER-2022-OA-PDF` |
| Instance | `DI-SACHENBACHER-2022-KULTURKAUFHAUS-PDF-20260904` |
| SHA-256 | `41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a` |
| Bytes | 5,644,026 |
| PDF | 1.7; 20 PDF pages; effective page box 481.8900146484375 × 623.6220092773438 pt |
| Scope | front matter plus printed pages 1–22 only |
| Stable landing page/PID | `unresolved` |
| Licence text inside inspected object | `unresolved` |

This is a distinct inspected digital instance, not the published Source itself and not the complete 379-page PDF representation later supplied by the owner for visual review. The later Orlagau/Ranis sections are absent from this 20-page instance.

## 4. Terminology: reference, not truth metaphor

For Histo-Orla, the technical benchmark vocabulary is now:

```text
reference case
reference locator
reference manifest
human-authored reference coordinates
human-reviewed reference decision
```

The earlier benchmark metaphor is retired from the active repository state because it can be read as a statement about scholarly authority, evidential quality or historical truth. None of those follow from a human-set crop or a reproducible renderer.

This is a **technical terminology and model-boundary clarification**. It creates no new Requirement, Method Truth, historical Finding or Research Selection decision.

Active files:

- `tools/document_evidence/data/sachenbacher-2022-reference-v0.1.json`
- `tools/document_evidence/data/sachenbacher-2022-reference-v0.2-candidate.json`

The pre-reconciliation filenames and structures remain recoverable from Git history; they are not active aliases.

## 5. Publication-object boundary

A visual element that is published as one map is not split into synthetic source/reference objects merely because a tool can crop it.

For Sachenbacher's Fig. 2 this means:

```text
complete published map
= one reference locator: L51-04-MAP-A

Roman numerals I–IV + zone boundaries
= content inside that map, not separate reference locators

caption below the map
= separately printed publication text and therefore separately addressable

zone explanation on following page(s)
= separately addressable prose linked back to the complete map
```

If a reviewer needs one zone, label or boundary emphasized, Histo-Orla may create a **regenerable derived highlight view** from the complete map. Such a view must point back to `L51-04-MAP-A`, must not replace the publication object and must not become an independent evidential source.

The former `L51-04-KEY-B` split is therefore not part of the active reference manifest.

## 6. Historical mechanical execution baseline

The original 2026-09-04 execution remains useful as reproducibility evidence for the state that existed then:

- exact instance hash/byte size/page count verified before rendering;
- normalized page coordinates kept tool-neutral;
- two isolated processes reproduced byte-identical reports;
- 14 then-declared locators were mechanically rendered;
- 9 then-declared research-critical relations were inspected from supplied evaluations: 8 `correct`, 1 `unresolved`, 0 `wrong`;
- parser semantic relations emitted by the low-level baseline: 0;
- `silent_error_count = 0` meant only that no supplied research-critical relation was marked `wrong`;
- negative tests rejected changed bytes, invalid geometry, duplicate locators, bad page indices and unevaluated parser relations.

That execution proved **mechanical reproducibility of the then-declared inputs**, not semantic completeness or human acceptance. The current active reference model contains 13 locators and 8 research-critical relations because the synthetic embedded-key split has been removed. A fresh mechanical run on that current model is still required.

## 7. Owner visual review 2026-09-14

The owner reviewed visual comparison material generated from a separately supplied **complete 379-page PDF representation** of the same published work. This review is material because it establishes human preferences about semantic crop boundaries and the publication-object model, but the complete PDF was not byte-verified as identical to the fingerprinted 20-page instance.

Recorded decisions:

| Locator / object | Owner decision | Current disposition |
|---|---|---|
| `L51-02-TEXT` | proposed larger crop includes unnecessary map content; old crop is better | retain old bbox `[0.105, 0.075, 0.89, 0.155]` |
| `L51-03-TEXT` | text passes visual review | candidate bbox retained for exact-instance confirmation |
| `L51-04-TEXT-D` | text passes visual review | candidate bbox retained for exact-instance confirmation |
| `L51-04-MAP-A` | previous expansion still clipped the top; revised complete-map crop passes | revised candidate `[0.105, 0.365, 0.88, 0.865]` retained for exact-instance confirmation |
| `L51-04-ZONE-EXPLANATION` | text passes visual review | candidate bbox retained for exact-instance confirmation |
| former embedded-key subregion | rejected as an independent reference crop; zone meaning needs the whole map and its boundaries | removed from active reference model; highlights only as derived views |
| `L51-04-CAPTION-C` | still a legitimate separately printed text locator | explicit final owner acceptance not yet recorded |

These decisions are persisted in `sachenbacher-2022-reference-v0.2-candidate.json` with the representation caveat. They **do not** close exact-instance acceptance.

## 8. Active reference slice

| Reference case | Printed/PDF page | Distinguishing evidence |
|---|---:|---|
| `REF51-01-TEXT-FOOTNOTE` | 11 / index 8 | main text + separately addressable footnote |
| `REF51-02-MAP-CAPTION` | 12 / index 9 | adjacent text + intact map + separately printed caption |
| `REF51-03-MULTI-FOOTNOTE` | 15 / index 12 | dense main text + five-footnote block |
| `REF51-04-PRIMARY-ZONE-MODEL` | 16–17 / indices 13–14 | text D + complete map A with internal labels/boundaries + caption C + cross-page zone explanation |
| `REF51-05-INTRO-FOOTNOTES` | 8 / index 5 | born-digital main text + two footnotes |

The primary case links to canonical Finding `F-U2-009`. That Finding says Sachenbacher presents the four-zone arrangement as an authored secondary-source model; it does not validate the model as historical truth.

The complete prose explanation continues beyond the bounded page-17 locator and remains explicitly `ambiguous` in scope.

## 9. Current implementation contract

`tools.document_evidence.roundtrip` performs only deterministic checks and rendering:

1. verify exact instance hash, byte size and page count;
2. validate normalized reference-locator bounds, explicit print-page states and relation references;
3. reject unexpected page geometry;
4. transform normalized coordinates to page points;
5. render every active reference locator and record a derivative crop hash;
6. distinguish `human-authored` relations from `parser-heuristic` relations;
7. preserve `reference_review`, Finding limits and locator scope notes in the report.

A `human-authored` relation means a person supplied the relation. It does **not** mean the relation or geometry has passed human acceptance.

A regression test enforces the publication-object boundary for Fig. 2: the complete map locator must exist, the former embedded-key locator must not exist in the active reference case, and the cross-page explanation relates directly to the map.

## 10. Acceptance state

### Established

- canonical Finding `F-U2-009` exists and is linked;
- exact 20-page instance identity/fingerprint is recorded;
- the original execution was mechanically reproducible;
- invalid page/geometry/parser states fail closed;
- terminology no longer implies scholarly truth or benchmark authority;
- Fig. 2 is modeled as one publication map, not as an arbitrary set of evidential sub-crops;
- owner visual decisions from the complete PDF are recorded with their representation boundary.

### Still open

- render the **current** 13-locator reference manifest against the exact fingerprinted 20-page instance;
- confirm the revised candidate geometry against that exact instance rather than inferring equivalence from the complete PDF representation;
- obtain/record the remaining explicit decision for `L51-04-CAPTION-C` if exact acceptance is required;
- rerun the document-evidence suite and full applicable assurance on the final branch head;
- reconcile PR #90 with current `main` before readiness/merge;
- obtain CI on the exact final head.

Therefore `B v0` remains incomplete and PR #90 remains Draft.

## 11. Systemic reconciliation

| Affected state | Disposition |
|---|---|
| #50 canonical research-state contract | `confirmed`; existing Source/Instance/Derivative/Findspot separation remains sufficient |
| #51 | `refined`; technical references are not truth categories, and compound publication visuals remain intact by default in this slice |
| #46 / `F-U2-009` | `unchanged`; historical semantics are not modified |
| #42 Requirements | `unchanged`; no new or weakened Requirement |
| #60 Method Truth | `unchanged` |
| Research Selection | `unchanged` |
| `orlagau-source-ledger.md` | reference-manifest terminology updated only |
| document-evidence code/tests | active schema renamed to `reference_*`; publication-map non-splitting regression added |
| Git history | preserved; no force rewrite of earlier commits/terminology |

The map treatment is recorded as a bounded publication-object modeling correction learned from real owner review. It should not be generalized into a universal rule for every possible compound visual without a concrete need; the default is to preserve the published visual unit and use derived highlights when attention must be directed inside it.

## 12. Reproduction

With PyMuPDF 1.26.4 available and the exact fingerprinted instance at `<PDF>`:

```bash
PYTHONPATH=. python -m tools.document_evidence.roundtrip \
  tools/document_evidence/data/sachenbacher-2022-reference-v0.1.json \
  <PDF> <OUTPUT-DIRECTORY>

PYTHONPATH=. python -m unittest discover -s tools/document_evidence/tests -v
```

The PDF bytes and generated crops are not committed. Derived review/highlight images are regenerable views, not Research Truth.

## 13. Exactly next step

Reconcile the current reference model and candidate decisions against the exact fingerprinted 20-page instance, then rerun deterministic tests/roundtrip. Do not start the second-renderer/parser step until that exact-instance review is truthful and PR #90 is reconciled with current `main`.
