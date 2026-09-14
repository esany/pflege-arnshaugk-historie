# #51 – Sachenbacher Evidence-Model Falsification Spike v0

**Current status (2026-09-14):** `complete-PDF instance reproduced / owner visual review complete / bounded cross-page scope unresolved by design / final-head assurance pending`

**Work Owner:** #51; technical direction #48; delivery/verification #59; research authority #46; trace #63  
**Originally executed:** 2026-09-04  
**Current instance review:** 2026-09-14  
**Requirements:** REQ-SRC-001, REQ-SRC-002, REQ-SRC-004, REQ-OCR-002  
**Drivers:** G-004, G-006, N-006, P-004  
**Evidence boundary:** technical experiment against a real published visual argument; no historical, methodological, Requirement or Research-Selection promotion.

Earlier revisions and coordinates remain available in Git history. This document records the current interpretation, active inspected instance and completed human visual review.

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
- #50 provides the Source/Representation/Instance/Derivative/Findspot contract.
- PyMuPDF is a replaceable mechanical rendering adapter only.
- #51 owns this bounded document/findspot experiment, not Method Truth or historical truth.
- Excluded: OCR-engine choice, GIS, general Search/UI, new Requirements and new canonical object classes.
- A technical reference locator is not an evidence grade, truth status or scholarly validation status.

## 3. Instance history and current inspected instance

### Historical mechanical baseline – 2026-09-04

| Field | Value |
|---|---|
| Source | `SRC-LIT-0001` – Sachenbacher 2022 published monograph |
| Representation | `REP-SACHENBACHER-2022-OA-PDF` |
| Instance | `DI-SACHENBACHER-2022-KULTURKAUFHAUS-PDF-20260904` |
| SHA-256 | `41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a` |
| Bytes | 5,644,026 |
| PDF | 1.7; 20 PDF pages; 481.8900146484375 × 623.6220092773438 pt |
| Scope | partial representation; front matter plus printed pages 1–22 |

This instance remains provenance for the original mechanical run. It is not an active blocker for the owner-reviewed real slice.

### Active inspected instance – 2026-09-14

| Field | Value |
|---|---|
| Source | `SRC-LIT-0001` |
| Representation | `REP-SACHENBACHER-2022-COMPLETE-PDF` |
| Instance | `DI-SACHENBACHER-2022-COMPLETE-PDF-20260914` |
| Filename | `Sachenbacher-2022-Thüringen östlich der Saale im Mittelalter.pdf` |
| SHA-256 | `3857636c854325eddaa0b658cd7b936a47d1b7712ccd7cbbc7296141e62616a0` |
| Bytes | 23,702,386 |
| PDF | 1.3; 379 PDF pages |
| PDF metadata | Adobe InDesign 16.0 / Adobe PDF Library 15.0 |
| Public provider/PID | `unresolved`; no provider identity inferred from the upload |
| Rights text in inspected imprint | CC BY International 4.0 for the work, with images/book cover expressly excepted |

Cover/title area, title/imprint, #51 target pages and back cover were inspected. For the bounded #51 pages the zero-based PDF indices equal the printed page labels: 8, 11, 12, 15, 16 and 17. No global pagination claim is needed.

This is a distinct inspected instance. It is not asserted byte-identical with the old 20-page provider object. The source ledger preserves both identities rather than forcing equivalence.

## 4. Terminology: reference, not truth metaphor

The active technical vocabulary is:

```text
reference case
reference locator
reference manifest
human-authored reference coordinates
human-reviewed reference decision
```

The former benchmark “gold” metaphor is retired from active state because it can be mistaken for scholarly authority, evidential quality or historical truth.

Active manifest:

- `tools/document_evidence/data/sachenbacher-2022-reference-v0.3.json`

Historical/review-bridge manifests retained for provenance:

- `tools/document_evidence/data/sachenbacher-2022-reference-v0.1.json` – 20-page mechanical baseline;
- `tools/document_evidence/data/sachenbacher-2022-reference-v0.2-candidate.json` – owner-review bridge before the complete PDF became the active inspected instance.

## 5. Publication-object boundary

A visual element published as one map is not split into synthetic source/reference objects merely because a tool can crop it.

For Sachenbacher's Abb. 2:

```text
complete published map
= one reference locator: L51-04-MAP-A

Roman numerals I–IV + zone boundaries
= content inside that map

caption below map
= separately printed publication text, separately addressable

zone explanation on following page(s)
= separately addressable prose linked back to complete map
```

If attention must be directed inside the map, Histo-Orla may create a regenerable derived/highlight view. That view points back to the complete map and is not an independent source or reference locator.

The former `L51-04-KEY-B` split is not part of the active manifest.

## 6. Historical mechanical execution baseline

The 2026-09-04 run remains useful historical reproducibility evidence:

- exact 20-page instance hash/byte size/page count verified before rendering;
- normalized coordinates stayed tool-neutral;
- two isolated processes reproduced byte-identical reports;
- 14 then-declared locators were rendered;
- 9 then-declared research-critical relations: 8 `correct`, 1 `unresolved`, 0 `wrong`;
- parser semantic relations emitted by the low-level baseline: 0;
- negative tests rejected changed bytes, invalid geometry, duplicate locators, bad page indices and unevaluated parser relations.

This proved mechanical reproducibility of the then-declared inputs, not semantic completeness or human acceptance.

## 7. Owner visual review 2026-09-14

The owner reviewed visual comparison material generated from the active fingerprinted 379-page PDF instance.

| Locator / object | Owner decision | Active disposition |
|---|---|---|
| `L51-02-TEXT` | larger candidate took unnecessary map content; old crop better | `[0.105, 0.075, 0.89, 0.155]` |
| `L51-03-TEXT` | text passes | `[0.105, 0.045, 0.89, 0.79]` |
| `L51-04-TEXT-D` | text passes | `[0.105, 0.045, 0.89, 0.39]` |
| `L51-04-MAP-A` | earlier candidate still clipped top; revised whole-map crop passes | `[0.105, 0.365, 0.88, 0.865]` |
| `L51-04-ZONE-EXPLANATION` | text passes | `[0.105, 0.04, 0.89, 0.91]` |
| former embedded-key subregion | rejected as independent reference crop; zone meaning requires whole map/boundaries | removed; highlight only as derived view |
| `L51-04-CAPTION-C` | final visual crop passes | `[0.2, 0.87, 0.82, 0.91]`; `human-accepted` |

The owner therefore accepted all selected primary review crops against the active complete-PDF instance. This is human acceptance of the reference geometry/publication-object treatment, not historical validation of Sachenbacher's model.

`R51-06` remains deliberately `unresolved`: the full four-zone prose explanation continues beyond the bounded page-17 locator. That unresolved state concerns scope, not a failed human review.

## 8. Active reference slice

| Reference case | Printed page / active PDF index | Distinguishing evidence |
|---|---:|---|
| `REF51-01-TEXT-FOOTNOTE` | 11 / 11 | main text + separate footnote |
| `REF51-02-MAP-CAPTION` | 12 / 12 | adjacent text + intact map + caption |
| `REF51-03-MULTI-FOOTNOTE` | 15 / 15 | dense main text + footnote block |
| `REF51-04-PRIMARY-ZONE-MODEL` | 16–17 / 16–17 | text + complete map with internal labels/boundaries + accepted caption + cross-page explanation |
| `REF51-05-INTRO-FOOTNOTES` | 8 / 8 | main text + two footnotes |

The primary case links to canonical Finding `F-U2-009`: Sachenbacher presents the four-zone arrangement as an authored secondary-source model. It is not historical validation.

## 9. Current implementation contract and complete-PDF reproduction

`tools.document_evidence.roundtrip` deterministically:

1. verifies exact instance hash, byte size and page count;
2. validates normalized locator bounds, print-page states and relation references;
3. rejects unexpected page geometry;
4. converts normalized coordinates to page points;
5. renders each active locator and hashes each crop;
6. preserves human-authored vs parser-heuristic authority and unresolved states.

The active `v0.3` manifest was executed against `DI-SACHENBACHER-2022-COMPLETE-PDF-20260914` before and after final caption acceptance:

- SHA-256 matched `3857636c854325eddaa0b658cd7b936a47d1b7712ccd7cbbc7296141e62616a0`;
- byte size matched 23,702,386;
- page count matched 379;
- all 13 active locators rendered with expected page geometry;
- mechanical result: `pass`;
- after final caption acceptance the only unresolved research-critical relation is `R51-06`, the intentionally bounded cross-page prose scope.

The exact final GitHub head still requires Project Assurance after this acceptance-state commit. A green run remains technical/formal verification only.

## 10. Acceptance state

### Established

- canonical Finding `F-U2-009` exists and is linked;
- complete uploaded publication PDF has its own inspected-instance identity and fingerprint;
- active 13-locator model reproduces mechanically against those exact bytes;
- all selected primary text/map/caption reference crops have explicit owner visual acceptance;
- Fig. 2 remains one publication map rather than synthetic evidential sub-crops;
- the 20-page provider object is retained as historical provenance, not an artificial blocker;
- invalid page/geometry/parser states remain fail-closed through the existing tool/tests;
- `R51-06` remains unresolved by design and does not represent an unclosed human-review gate.

### Still open before Ready

- Project Assurance on the exact post-acceptance branch head;
- confirm branch remains reconciled with current `main`.

No remaining human visual-review gate exists for the bounded #51 Sachenbacher slice.

## 11. Systemic reconciliation

| Affected state | Disposition |
|---|---|
| #50 canonical research-state contract | `confirmed`; distinct inspected instances solve the byte-identity problem without conflation |
| #51 | `refined`; active real slice uses the instance actually inspected by the owner; selected reference geometry accepted |
| #46 / `F-U2-009` | `unchanged`; historical semantics not modified |
| #42 Requirements | `unchanged`; no new/weakened Requirement |
| #60 Method Truth | `unchanged` |
| Research Selection | `unchanged` |
| source ledger | complete-PDF inspected instance recorded; old partial instance retained as provenance |
| document-evidence tests | active manifest v0.3; complete-PDF fingerprint/page mapping, map non-splitting and final caption acceptance covered |

The map treatment is a bounded publication-object modeling correction learned from real owner review. It is not automatically generalized into a universal rule for every compound visual; the default here is to preserve the published visual unit and use derived highlights when attention must be directed inside it.

## 12. Reproduction

With the exact user-provided complete PDF at `<PDF>`:

```bash
PYTHONPATH=. python -m tools.document_evidence.roundtrip \
  tools/document_evidence/data/sachenbacher-2022-reference-v0.3.json \
  <PDF> <OUTPUT-DIRECTORY>

PYTHONPATH=. python -m unittest discover -s tools/document_evidence/tests -v
```

PDF bytes and generated crops are not committed. Derived review/highlight images are regenerable views, not Research Truth.

## 13. Exactly next step

Run Project Assurance on the exact post-acceptance head and recheck `main` reconciliation. If both pass, PR #90 may leave Draft. Do not reopen the old 20-page instance as a blocker unless a future question specifically requires reproducing that historical instance itself.
