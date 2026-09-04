# Orlagau Source Ledger – Sachenbacher 2022 Reconciliation Delta

**Status:** `source-ledger-delta / reconciled-reference / not-canonical-source-home`  
**Work Owner:** #46  
**Protocol:** `docs/research/source-identity-protocol.md`, #45  
**Stand:** 2026-09-04  
**Branch:** `research/sachenbacher-clean-room-20260903`

## 0. Reconciliation decision

This file is **not** a second canonical source ledger. It is a bounded PR #76 delta for Sachenbacher-specific routing, model-check notes and inspected/candidate representations.

Canonical rule for merge:

```text
canonical Sachenbacher source identity
→ belongs in docs/research/cases/orlagau-source-ledger.md

this file
→ may reference that canonical source_id and carry route/status deltas until folded in or explicitly superseded
```

The inspected `main` `orlagau-source-ledger.md` did not expose a Sachenbacher entry in this run. If a newer/parallel canonical source identity exists before merge, this file must be mapped to that existing ID rather than creating another `SRC-SEC-SACHENBACHER-2022` truth. One fact / one canonical home applies.

Recommended canonical ID if no existing one is present at merge time: `SRC-SEC-SACHENBACHER-2022`.

---

## 1. Canonical source identity candidate / reference

| Field | Value |
|---|---|
| canonical_source_id | `SRC-SEC-SACHENBACHER-2022` unless already assigned in the common ledger |
| source_type | Secondary publication; research-state source; model/hypothesis source; literature and primary-source router |
| canonical_citation | Peter Sachenbacher, *Thüringen östlich der Saale im Mittelalter. Archäologisch, mediävistisch, onomastisch, ethnografisch und philosophisch vergleichende Studie zum früh- und hochmittelalterlichen Landesausbau in Territorien der Germania Slavica Thuringiae*, Darmstadt: wbg Academic, 2022 |
| publisher/imprint | wbg Academic, Verlag Herder GmbH |
| print_ISBN | `978-3-534-40649-4` |
| eBook_PDF_ISBN | `978-3-534-40650-0` |
| source_status | published secondary work; not a primary medieval source; not an independent validation authority |
| Histo-Orla use | #46 model check: Landesausbaumodell, Orlagau terminology, boundary model, place/chronology matrix, source/literature routing |

---

## 2. Representation / instance separation

### DI-SACHENBACHER-2022-DDE-OATBYCO-HTML

| Field | Value |
|---|---|
| relation_to_source | digital text/HTML representation of the published work; not the historical source and not the printed book itself |
| provider / portal | OATbyCO / DDE, ULB TU Darmstadt environment |
| URL | `https://exist.ulb.tu-darmstadt.de/2/v/pa000017-0007` |
| inspected_for | full-text navigation, print-page markers, footnote-number control, model/place/term discovery |
| access_date | `2026-09-03/04` |
| reliability_boundary | suitable for working navigation; not sufficient alone for final print-page/footnote citation when page break or footnote text is ambiguous |
| search_boundary | checked terms include `Knau`, `Dreba`, `Plothen`, `Arnshaugk`, `Ranis`, `Weltwitz`, `Krölpa`, `Neunhofen`, `Orlagau`, `pagus`, `Salaveld`, `Gösselborn`, `Birkert`, `Loquitz`, `Kotschau`, `Wysburg`, `Zwackau`, `Chursdorf` |

### DI-SACHENBACHER-2022-OA-PDF

| Field | Value |
|---|---|
| relation_to_source | electronic PDF representation/instance of the published secondary work; **not** a separate source and not a medieval source |
| evidence_for_existence | the inspected imprint text states: `Elektronisch ist folgende Ausgabe erhältlich: eBook (PDF): 978-3-534-40650-0`; the same imprint states Open Access under CC BY 4.0 except images/book cover |
| publication/license boundary | OA applies to the work as stated in the imprint; images/cover are excluded by the imprint statement |
| direct_file_url | `candidate/discovered; not byte-verified in this reconciliation pass` |
| byte_fingerprint | `not computed` |
| technical_identity_status | `integrated-as-instance-record / byte-fingerprint-open` |
| allowed use in PR #76 | cite as known electronic OA/PDF representation for source identity; do not use as a page-image/findspot authority until byte identity, page count, checksum and print-page mapping are inspected |
| next verification | retrieve the stable publisher/DDE/OA PDF object or file, record landing page, direct file URL if stable, byte size, SHA-256, page count, PDF metadata, rights statement and print-page mapping |

### DI-SACHENBACHER-2022-HERDER-WBG-CATALOGUE

| Field | Value |
|---|---|
| relation_to_source | bibliographic/catalogue representation, not passage evidence |
| URL | `https://www.herder.de/wissen/shop/p8/86695-thueringen-oestlich-der-saale-im-mittelalter-gebundene-ausgabe/` |
| use | bibliographic corroboration: author, title, publisher/imprint, year, ISBN, scope statement |
| limitation | no source-passage or model-evidence authority |

---

## 3. Route deltas retained from PR #76

These entries are retained as source/literature routing tasks, not as completed source collation.

| ID | Type | Route / use | Status |
|---|---|---|---|
| `SRC-LIT-GOCKEL-SAALFELD` | Fachliteratur / Pfalzenrepertorium | Saalfeld, 899/1013/1071, Dienstrecht, Ranis-router | `identified / not directly collated` |
| `SRC-LIT-BUENZ-ORLAGAU-2007` | Kirchengeschichte / Pfarrorganisation | Sedessprengel Pößneck/Remda, Krölpa/Neunhofen/Langenschade | `identified / not directly collated` |
| `SRC-LIT-RANIS-2006-WERNER-QUECK` | Spezialliteratur | Ranis only as discriminating example, not current focus | `unresolved bibliographic identity / deferred` |
| `SRC-LIT-EICHLER-ONOMASTIK-ORLAGAU` | Onomastik | Ortsnamendeutung Ranis/Weltwitz/Graba etc. | `unresolved / method-critical` |
| `SRC-LIT-MUELLER-DORFKIRCHEN-2001-2007` | Bau-/Kirchengeschichte | Dorfkirchen / romanische Kerne / Kirchenorganisation | `unresolved / high relevance` |
| `SRC-PRIMARY-899-SAALFELD-CURTIS` | Primär-/Editionsquelle | Saalfeld `curtis Salauelda` | `source-collation-open` |
| `SRC-PRIMARY-1013-SAALFELD-PROVINCIA` | Primär-/Editionsquelle | `provincia Salaveld`, `castellum` | `source-collation-open / terminology-critical` |
| `SRC-PRIMARY-1056-1057-RICHEZA-KOELN-IN-ORLA` | Primär-/Edition | Richeza/Köln, `in Orla` | `identified by Histo-state / direct collation open` |
| `SRC-PRIMARY-1071-GRENZBESCHREIBUNG-COBURGER-COPIALBUCH` | Kopialüberlieferung / Fälschungsdiskussion | Grenzmodell Gösselborn–Triptis/Birkert, Orlamünde–Rennsteig | `high-risk / high-value / no polygon promotion` |
| `SRC-PRIMARY-1074-KOELN-BESITZUEBERSICHT` | Primär-/Editionsquelle | Besitz-/Orts-/Hufenliste | `source-collation-open / model-critical` |
| `SRC-PRIMARY-SAALFELDER-DIENSTRECHT` | Rechts-/Wirtschaftsquelle | Wald, Rodung, Fischerei, Markt, Zoll, Dienste | `source-collation-open / high priority for #46/#47 interface` |
| `SRC-LIT-WANDSLEB-ORLAGAU-1911` | Historiographie | ältere Kolonisations-/Orlagau-Deutung | `historiography / direct collation open` |
| `SRC-LIT-KAUFMANN-ORLAGAU-1959-1963` | ältere Archäologie/Landeskunde | Fundstellen-/Kartierungsgrundlage | `foundational / needs update-control` |
| `SRC-LIT-REMPEL-EBERHARD-ORLAGAU` | Archäologie/Onomastik | Ortsnamen/Fundstellen/1071/1074-Orte | `model-critical / direct collation open` |
| `SRC-LIT-ROSENKRANZ-EICHLER-ULBRICHT-WALTHER` | Onomastik/Dialektgeographie | Ortsnamenschichten, Lobensteiner Schranke etc. | `method-critical / direct collation open` |
| `SRC-LIT-LANDSCHAFTEN-76-ORLATAL-PLOTHENER-TEICHGEBIET` | Landschaftsrouter | Plothen/Teichgebiet; #47 interface | `landscape-router / direct collation open` |
| `SRC-LIT-TLAD-QUECK-SPAZIER-HOTHER-HESSLAND` | Archäologie | Ranis, Weltwitz, Oberwellenborn, Ludwigshof, Wysburg etc. | `high priority / direct collation open` |

---

## 4. Semantic guardrails for merge/review

Do **not** merge from this file as facts:

- `Ranis as fixed 9th-century Saalfeld base`;
- `Weltwitz as proven Slavic refuge castle`;
- `Kirchenorganisation = complete Christianisation`;
- `Sachenbacher proves Knau bei Neustadt/Orla`;
- `Orlagau 1071 = timeless polygon boundary`;
- `1074 Ortsliste = complete settlement map`;
- `green CI = scientific/owner PASS`.

Allowed after reconciliation:

- Sachenbacher is a secondary model/router for #46;
- the Model-Check artefact is the current PR #76 reading guide;
- old Ranis-slice material is retained only as provenance/superseded first focus;
- unresolved/direct-collation-open states remain valid and are not automatic merge blockers unless claims are promoted beyond their evidence.
