# #51 – Sachenbacher Evidence-Model Falsification Spike v0

**Current status (2026-09-09):** `mechanical reproduction verified / semantic acceptance unresolved / B v0 not complete`

**Review precedence:** Section 11 supersedes the completion/PASS disposition below. Sections 1–10 preserve the original 2026-09-04 experiment report as historical execution claims, not current acceptance. No architecture or requirement delta.
**Work Owner:** #51; technical direction #48; delivery/verification #59; trace #63
**Executed:** 2026-09-04
**Requirements:** REQ-SRC-001, REQ-SRC-002, REQ-SRC-004, REQ-OCR-002
**Drivers:** G-004, G-006, N-006, P-004
**Evidence boundary:** technical experiment against a real published visual argument; no historical or methodological promotion

## 1. Falsification question

Can the existing sequence

```text
Source → Representation → Inspected Instance → Derivative
→ Findspot/Observation → Finding
```

carry a real visual scientific finding losslessly and reproducibly in a fresh context without new canonical `Page` or `Region` object classes and without parser-specific semantics?

The counter-hypothesis wins if the result depends on hidden manual convention, tool-specific IDs, silent relation errors or additional canonical object semantics.

## 2. Work context and boundary

- Primary function: architecture/development/research-software experiment.
- Historical authority remains #46/PR #76; the spike does not decide whether Sachenbacher's model is historically correct.
- #50 provides the existing source/instance/derivative/findspot contract.
- PyMuPDF 1.26.4 is only a replaceable rendering adapter.
- Excluded: Docling, OCR, IIIF, GIS, search, UI, general document pipeline, new requirements and new canonical object classes.
- Canonical persistence: this experiment report, the source-ledger instance entry, the neutral gold manifest, implementation/tests and #63 trace record.

## 3. Concrete inspected instance

The URL supplied and provider-corroborated through #46 was retrieved twice during the work cycle. The tested bytes are:

| Field | Value |
|---|---|
| Source | `SRC-LIT-0001` – Sachenbacher 2022 published monograph |
| Representation | `REP-SACHENBACHER-2022-OA-PDF` |
| Instance | `DI-SACHENBACHER-2022-KULTURKAUFHAUS-PDF-20260904` |
| SHA-256 | `41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a` |
| Bytes | 5,644,026 |
| PDF | 1.7; 20 PDF pages; uniform effective page box 481.8900146484375 × 623.6220092773438 pt |
| Scope | front matter plus printed pages 1–22 only |
| Stable landing page/PID | `unresolved` |
| Licence text inside inspected object | `unresolved` |

This is a distinct inspected digital instance, not the published Source itself and not the earlier 153-page reflowed user-provided representation. Its partial extent is material: later Orlagau/Ranis sections are absent and were not claimed as inspected through these bytes.

## 4. Human-set, tool-neutral gold slice

The full PDF pages were visually rendered first. Regions were then set manually in normalized top-left page space; no PyMuPDF text/image block or internal object ID supplied a gold box.

| Gold case | Printed/PDF page | Distinguishing evidence |
|---|---:|---|
| `G51-01-TEXT-FOOTNOTE` | 11 / index 8 | main text + separately addressable footnote |
| `G51-02-MAP-CAPTION` | 12 / index 9 | adjacent text + map + caption |
| `G51-03-MULTI-FOOTNOTE` | 15 / index 12 | dense main text + five-footnote block |
| `G51-04-PRIMARY-ZONE-MODEL` | 16–17 / indices 13–14 | text D + map A + embedded Roman-numeral key B + caption C + cross-page zone explanation |
| `G51-05-INTRO-FOOTNOTES` | 8 / index 5 | born-digital main text + two footnotes |

The primary case references the real PR-#76 model-check finding: Sachenbacher's four-zone model is authored argumentation whose text, map, caption, embedded keys and following explanation must remain jointly reachable while retaining distinct roles. The complete zone explanation continues beyond the page-17 locator; this is preserved as `ambiguous`, not silently completed.

Gold state: `tools/document_evidence/data/sachenbacher-2022-gold-v0.1.json`.

## 5. Mechanical baseline and fresh-context result

`tools.document_evidence.roundtrip` performs only deterministic checks and rendering:

1. verify instance hash, byte size and page count;
2. validate normalized locator bounds, explicit print-page states and relation references;
3. reject unexpected page geometry;
4. transform normalized coordinates to page points;
5. render every region and record a derivative crop hash;
6. report parser relations separately from human-curated relations.

Two isolated processes with an empty environment except explicit `PATH`/`PYTHONPATH` consumed only repository manifest + fingerprinted bytes. Both produced byte-identical reports:

- result: `pass`;
- 5 gold cases / 14 distinct locators rendered;
- report SHA-256: `eb7af9169451828a6086543248a0051e929b54f436e4a0082a76b36f875fd71d`;
- research-critical relations inspected: 9 (`footnote`, `caption`, `figure`, `legend`, `reading_order`); 8 correct, 1 explicitly unresolved, 0 wrong;
- parser relations emitted by the low-level baseline: 0;
- `silent_error_count = 0`;
- PyMuPDF version: 1.26.4.

The zero parser-relation count is intentional, not a claim of parser quality: PyMuPDF was not allowed to invent caption, legend or footnote semantics. Those relations are human-curated in the gold state. Future parsers must emit their candidates as `parser-heuristic` with explicit evaluation; the validator rejects a parser relation without that state.

Negative tests prove that changed bytes, out-of-page boxes, duplicate locator identity, unknown references/tool-specific coordinate systems and unevaluated parser relations fail closed.

## 6. Cumulative pass/fail disposition

| #51 condition | Result | Evidence / limit |
|---|---|---|
| identical bytes fingerprinted | PASS | SHA-256 + byte count checked before opening PDF |
| PDF index separate from print-page relation | PASS | separate fields; print state vocabulary includes `resolved | absent | ambiguous | unresolved` |
| manually defined neutral regions reproduce | PASS | 14 visually checked crops from normalized page space |
| multiple regions attach to one finding without flattening | PASS | primary case has five locators across two pages with explicit roles/relations |
| parser relationships stay derivative/heuristic | PASS | no parser semantic relation emitted; contract/test forbids unlabelled parser relation |
| fresh process reaches same regions | PASS | two isolated runs, byte-identical report |
| unresolved/ambiguous survives | PASS | landing/licence unresolved; full zone-explanation scope ambiguous |
| no new canonical object class required | PASS | locators remain values on existing Findspot/Observation relations |
| research-critical silent relation errors | PASS | `silent_error_count = 0`; no parser relation was promoted |

**Disposition:** `adopt existing contract / retain minimal locator representation / no promotion`. The hypothesis held for this bounded real slice. This does not establish completeness for the entire book, rotated/cropped PDFs, scans, OCR, arbitrary tables or all document genres.

## 7. Failure modes and residual debt

- The reachable OA object is only a 20-page partial representation. It is sufficient for the selected real visual model but not for the later Orlagau/Ranis research passages.
- Stable landing page/PID and exact licence statement remain unresolved. This is source-identity debt, not a blocker for byte-level local inspection of the provided OA route.
- Crop hashes are adapter/version-dependent derivative verification, not canonical locator identity.
- Cross-page continuation is expressible, but the current selected locator intentionally covers only zones I–III partially on print page 17; complete four-zone exposition remains outside the bounded region and is marked ambiguous.
- No parser benchmark was performed. Any future caption/footnote/reading-order enrichment must be compared with the independent gold and keep `silent_error_count = 0` for research-critical relations.

## 8. Systemic reconciliation

| Affected state | Disposition |
|---|---|
| #50 canonical research-state contract | `confirmed`; no contract or object-class change required |
| #51 work status | `refined`: bounded v0 executed; general pipeline remains open |
| #46 / PR #76 historical findings | `unchanged`; only a real finding anchor was referenced |
| `orlagau-source-ledger.md` | `refined` with the concrete inspected instance and partial-object limit |
| Lampe-420 work-order basis | `confirmed/refingerprinted`; additive ledger change does not alter the prior Lampe finding, and its Git-blob prerequisite was refreshed |
| REQ-SRC-001/002/004, REQ-OCR-002 coverage | `partially-satisfied` for this bounded instance/round-trip only |
| #62 structured requirement projection | `refined` for the four newly partial requirements; accepted semantics remain owned by #42 |
| REQ-SRC-003, REQ-OCR-001/003 | `unchanged`; not exercised |
| #52 OCR benchmark | `unchanged`; deliberately out of scope |
| #63 trace | `refined` with current implementation/verification record |
| `PROJECT_STATE.md` | `refined` because #51 gained a material real-test result and executable artifact |
| #44 blocker register | `unchanged`; residual items are bounded debt, not an owner decision/blocker |

## 9. Reproduction

With PyMuPDF 1.26.4 available and the downloaded instance at `<PDF>`:

```bash
PYTHONPATH=. python -m tools.document_evidence.roundtrip \
  tools/document_evidence/data/sachenbacher-2022-gold-v0.1.json \
  <PDF> <OUTPUT-DIRECTORY>

PYTHONPATH=. python -m unittest discover -s tools/document_evidence/tests -v
```

The PDF bytes and generated crops are not committed. The source URL, fingerprint, complete neutral locators, relations, uncertainty and reproduction command are committed.

## 10. Exactly one next step

Run one replaceability check with a second PDF renderer against the unchanged neutral manifest and require the same visible regions before considering any higher-level parser benchmark.


## 11. PR #90 reconciliation and review (2026-09-09)

Primary function: bounded development/verification under #51/#48/#59. Research authority remains #46; no Selection or scientific promotion. Original commit `947f6fdf57559f5f7084e4e8a570b75c23bab702` is preserved. Main `df38958cd30cf82c86da05fa9fab1485bd667f20` is integrated by merge, without rewriting its five research/method artifacts.

### Semantic review and acceptance boundary

- The canonical source remains `SRC-LIT-0001`. The PR76 generic OA-PDF route with unresolved bytes and the fingerprinted 20-page partial object are different instance records, not competing source identities. The later Orlagau research passages remain outside this partial object.
- The Lampe work order's ledger fingerprint matches the additive ledger change. Its historical evidence, action and unresolved questions remain unchanged; context loading retains one passed and two unresolved prerequisites.
- The earlier manifest anchor was a spike-local placeholder. PR76 sections 4–5 discuss the Orlaraum model; they did not establish an explicit canonical Finding for the four-zone figure on printed page 16. The link is now resolved through the domain-owned Finding recorded below; no historical truth is asserted.
- Original coordinates were preserved, including defects, so the original experiment remains auditable. Full-page visual inspection found that `L51-04-MAP-A` starts below the upper map edge; `L51-04-ZONE-EXPLANATION` starts below the Zone-I heading; `L51-02-TEXT`, `L51-03-TEXT` and `L51-04-TEXT-D` omit opening lines visible on their full pages. Stable cropping proves reproducibility, not coverage of the claimed semantic region.
- The original `human-curated` labels are declarations in the input. This review has no independent record of a human selecting or accepting those boxes. No AI-assisted reinspection is promoted to human gold validation.
- `silent_error_count=0` is derived from supplied relation evaluations, with zero parser relations. It is not an independent error measurement. `R51-06` remains unresolved; report outputs now preserve locator scope notes, Finding uncertainty and gold-review state.

### Technical corrections

Invalid/negative/out-of-range PDF indices are rejected before rendering (negative indices previously selected pages from the end). Missing, nonfinite or malformed geometry is rejected instead of allowing an empty `zip` check to pass. Parser evaluation vocabulary is enforced even for noncritical relations. A `fail` report now returns CLI exit status 1. Four targeted regression tests cover these failures; the original six remain.

### Verification performed

- Re-downloaded the manifest URL: 5,644,026 bytes; SHA-256 `41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a` matches the original.
- PyMuPDF 1.26.4 reproduced all 14 original regions in two separate processes with only explicit PATH/PYTHONPATH and no chat context. Reports were byte-identical. This is mechanical reproducibility only.
- Full-page visual review of PDF indices 5, 8, 9, 12, 13 and 14 exposed the bounded coverage defects above.
- Local suites: requirements 14, assurance 16, operational 27, document evidence 10 tests passed (67 total). Both formal validators passed; requirements migration warnings remain advisory.
- GitHub CI status is recorded in PR #90 for the exact committed head; it is not inferred from these local checks.

### Required return before v0 acceptance

#51/#46 must review the original crops against the six full pages, specify/accept corrected tool-neutral regions with attributable human provenance, and identify an exact existing canonical Finding or explicitly accept the missing link as a changed test scope through the proper authority. Keep the original coordinate version as provenance. Re-run mechanical and visual checks on the accepted revision. Until then the cumulative original v0 acceptance is not established, the PR stays draft, and the proposed second-renderer step is premature. No human validation or historical Finding has been fabricated to close this gate.

## 12. PR #90 continuation: finding gate closed, candidate preparation complete (2026-09-11)

The bounded #46 research finding is now persisted canonically as `F-U2-009` in `docs/research/cases/u2-knau-orlagau-quellenbefunde.md`. The manifest references that exact Finding and no longer uses the former spike-local placeholder as a substitute.

The exact inspected PDF instance was reverified before visual work: SHA-256 `41e56fb31cc2a547f83a2a55797ecbf9938e6b90a296f1d7afb85d6df3593f9a`, 5,644,026 bytes, 20 pages. Full pages at PDF indices 5, 8, 9, 12, 13 and 14 were rendered and inspected. The original v0.1 manifest remains unchanged and provenance-capable.

Candidate corrections are recorded in `tools/document_evidence/data/sachenbacher-2022-gold-v0.2-candidate.json` for `L51-02-TEXT`, `L51-03-TEXT`, `L51-04-TEXT-D`, `L51-04-MAP-A` and `L51-04-ZONE-EXPLANATION`; `L51-04-KEY-B` and `L51-04-CAPTION-C` remain explicit review targets. Each entry preserves the old bbox, candidate bbox, rationale, intended semantic unit, exclusions and uncertainty. Status is `candidate / pending-human-review`.

The reproducible review packet is generated in a temporary working directory with the exact PDF and the candidate manifest. It must contain, for each changed locator, full page, old crop and candidate crop, plus old crops for the unchanged key/caption review targets. Review images are derived artifacts and are not Research Truth or commit candidates.

**Closed:** authorized #46 Finding, exact canonical manifest link, exact PDF verification, reproducible candidate-region preparation.

**Open:** attributable human `accept | correct` for every candidate region; then promotion to an accepted gold version and a fresh mechanical roundtrip. `B v0` is not complete while this Human Gate remains open.
