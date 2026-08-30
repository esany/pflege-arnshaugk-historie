# C6 – Source Dependence, Überlieferungsbeziehungen und Discrepancy Reasoning

**Work Owner:** #34  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** historische Quellenkritik, Diplomatik, Textkritik/Editionswissenschaft, Historiographie.  
**Controlling competencies:** Archivistik, jeweilige Fachdomäne, Research Integrity; Kartenkritik/Philologie je Material.

## 1. Research Questions

RQ-C6-01 bis RQ-C6-03:

1. Wie wird abhängige Wiederholung von unabhängiger Bestätigung unterschieden?
2. Welche diagnostischen Kategorien helfen bei Abweichungen, bevor „Widerspruch“ behauptet wird?
3. Warum müssen Überlieferungs-, historische und interpretative Relationen getrennt bleiben?

## 2. Search Scope / Boundary

Geprüft wurden:

- historische Methodenliteratur zu Source Criticism, Triangulation und Kontextualisierung;
- aktuelle Reflexion über Source Criticism und ihren Frage-/Gattungsbezug;
- Textkritik/Stemmatologie als spezialisierte Tradition zur genealogischen Abhängigkeit von Textzeugen;
- TEI Critical Apparatus als etablierte Repräsentationspraxis für identifizierbare Textzeugen/Varianten;
- U1–U4 und internes Prior Art #12/#21.

Nicht beansprucht wird eine universelle algorithmische Methode, die Abhängigkeit aller historischen Quellen automatisch erkennt.

## 3. Inspected sources

- Kipping, Wadhwani, Bucheli, **Analyzing and Interpreting Historical Sources: A Basic Methodology**: https://academic.oup.com/book/4688/chapter-abstract/146885133
- Cathleen Sarti, 2024, **Source criticism for cultural history**: https://www.tandfonline.com/doi/full/10.1080/13642529.2024.2361214
- Johannes Westberg, 2025, **Historical methods in educational research**: https://www.tandfonline.com/doi/full/10.1080/00309230.2025.2473704
- Philipp Roelli (ed.), **Handbook of Stemmatology** (2020, Open Access): https://www.degruyter.com/document/doi/10.1515/9783110684384/html
- TEI P5 4.11.0, **Critical Apparatus**: https://tei-c.org/release/doc/tei-p5-doc/en/html/TC.html
- Louis Gottschalk, **Understanding History: A Primer of Historical Method**, bibliographic record: https://books.google.com/books/about/Understanding_History.html?id=c6VmAAAAMAAJ
- Review of Howell/Prevenier, **From Reliable Sources**: https://scholarworks.iu.edu/journals/index.php/tmr/article/view/15260

## 4. Findings

### F-C6-01 – Source criticism is question-relative and contextual, not a single credibility score

Kipping/Wadhwani/Bucheli structure historical source work around source criticism, triangulation and hermeneutic/contextual interpretation. Sarti’s 2024 discussion emphasizes that source criticism changes with scholarly questions and source genres, even if formal elements remain recognizable. Westberg likewise stresses source materials, contextualisation, periodisation and historical analysis on historical research’s own terms.

**Implication:** Histo-Orla must not assign one global `source reliability` number. A source can be highly useful for one question and weak/strategic/derivative for another.

A better unit is:

```text
Source / witness
+ exact claim/question
+ production/context/purpose
+ transmission/dependence
+ method used
→ evidential role for this claim
```

### F-C6-02 – Repetition is not automatically corroboration; independence is claim-specific

Classical historical method makes the key point that agreement among sources can arise from copying/influence/shared origin rather than independent observation. Modern methodology adds that triangulation should confirm **or question** interpretation, not just count matching texts.

For Histo-Orla:

- ten publications ultimately citing one archival record are not ten independent sources for the underlying event;
- two records from the same administrative reporting chain may be partially dependent;
- one source may be dependent for a factual detail but independently informative about reception, rhetoric or later historiography;
- `independence` should therefore be assessed **for a claim/evidential function**, not assigned once to an entire document.

### F-C6-03 – Textual criticism/stemmatology proves that source genealogy can be complex and contaminated

Stemmatology explicitly studies genealogical relations among copies/witnesses and modern literature includes **contamination**: witnesses may draw on more than one source/tradition. This is a useful disciplinary warning against simplistic tree assumptions.

TEI’s Critical Apparatus requires identified witnesses and can associate readings with specific witnesses. The important Histo-Orla lesson is not “use TEI everywhere”, but:

> **A reading/finding should know which concrete witness/source supports it; a source family/dependency relation must not be collapsed into the claim itself.**

### F-C6-04 – Source relation and historical relation are different epistemic objects

Three relation layers are methodically distinct:

#### A. Transmission / derivation relation

Examples:

- A copies B;
- edition E transcribes manuscript M;
- regest R summarizes charter U;
- article S cites older study T;
- two texts derive from common Vorlage X;
- OCR O derives from scan I.

This relation answers: **Wie gelangte Information/Text von einer Repräsentation zur anderen?**

#### B. Historical relation

Examples:

- person P served office O;
- actor P corresponded with Q;
- estate E belonged to X;
- mill M used watercourse W.

This answers: **Welche Beziehung bestand historisch?**

#### C. Interpretive/research relation

Examples:

- researcher infers that finding F supports hypothesis H;
- two records are treated as discrepant for a defined claim;
- historian classifies an actor as ministerial candidate.

This answers: **Welche analytische Beziehung behauptet die Forschung?**

A graph/software representation may later store all three, but **the relation type and evidence status must not silently mix them**.

### F-C6-05 – „Discrepancy“ should be a diagnostic process, not a euphemism that removes contradiction

RGK’s prior-art intuition „Abweichung vor Konflikt“ is methodically defensible **only** as a first diagnostic move. A difference between two records can arise from:

1. different **referent/object**;
2. different **time state**;
3. different **spatial scale/boundary**;
4. different **source genre/function**;
5. different **institutional producer/perspective**;
6. different **audience/purpose/rhetoric**;
7. different **terminology/semantic regime**;
8. different **measurement/counting/representation rule**;
9. different **transmission/editorial/OCR state**;
10. different **knowledge/information horizon**;
11. selective survival / archival loss;
12. actual factual contradiction or incompatible claim.

The method must be allowed to end at **real contradiction / unresolved conflict**. „Discrepancy“ is not a harmonization mandate.

### F-C6-06 – Agreement and disagreement both need provenance-sensitive interpretation

Agreement is stronger when evidence chains are sufficiently independent; disagreement is more informative when we can rule out different time states, referents, genres or transmission errors.

Therefore Histo-Orla should not start from:

```text
source A statement = source B statement
→ confirmed
```

or:

```text
A != B
→ one is wrong
```

Instead:

```text
exact claims extracted
→ source/witness identities
→ production + transmission context
→ dependency hypothesis
→ referent/time/scale/purpose alignment
→ compare
→ corroborates | differs-explainably | genuinely-conflicts | unresolved
```

### F-C6-07 – Dependency itself is often a research hypothesis

Whether two sources share a Vorlage, whether a 19th-century historian copied a predecessor, or whether two administrative reports derive from one original report may be uncertain.

Histo-Orla must therefore support statuses such as:

- `directly documented dependence`
- `strongly inferred dependence`
- `possible/common-source hypothesis`
- `appears independent for claim X`
- `independence unknown`

Unknown dependence must not be silently promoted to independence.

## 5. Discrepancy Diagnostic Method v0.1

For two or more apparently comparable findings:

### Step 1 – Normalize the research question, not the source

What exact claim is being compared?

### Step 2 – Check identity/referent

Same person/place/object/institution/event?

### Step 3 – Align temporal state

Same date/period/version/state?

### Step 4 – Identify source/genre/function

Why and by whom was each source produced?

### Step 5 – Check transmission/dependence

Original/copy/regest/edition/citation/common template/shared administrative chain?

### Step 6 – Check vocabulary/representation

Same semantic category, measurement, map scale, boundary rule, editorial normalization?

### Step 7 – Assess evidential role for the exact claim

Direct observation? report? legal assertion? accounting entry? retrospective narrative? cartographic convention?

### Step 8 – Compare

Disposition candidates:

- `not actually comparable`
- `same claim, likely dependent repetition`
- `independent corroboration plausible`
- `different time/state/purpose explains difference`
- `substantive contradiction`
- `unresolved / more evidence needed`

### Step 9 – Define discriminating evidence

What new source, witness, edition, chronology or expert method would resolve/clarify the discrepancy?

## 6. U1–U4 stress tests

### U1 Maps / ponds

A Meilenblatt, a 16th-century fiscal record and a LiDAR depression do not „disagree“ simply because boundaries differ. First classify time, purpose, scale and evidential type. Two later maps that copy the same cadastral basis are not independent spatial corroboration.

### U2 Urkunde / Regest / Kopialbuch / Landesgeschichte

A regest and an edition of the same charter are not independent witnesses to the event. A kopial copy can be the only surviving textual witness but remains a distinct transmission state. A later regional historian repeating the edition adds historiographic reception, not new primary corroboration.

### U3 Diplomatic report / letter / biography

A diplomat’s report and later biography may share the same correspondence. Agreement must be lineage-checked. Self-description and hostile report can genuinely disagree because of perspective/strategy; neither should be globally scored as „reliable/unreliable“.

### U4 Duplicate digital corpus

The same edition mirrored in several PDFs/sites should not multiply evidence. OCR variants from one scan are derivatives of one instance, not separate witnesses.

## 7. Independence / Corroboration Rules v0.1

1. Count **evidence chains**, not URLs/documents.
2. Independence is assessed relative to an exact claim.
3. Shared source/common reporting chain lowers independence for that claim.
4. Derivative sources can be valuable for different questions (reception, transformation, editorial practice).
5. Unknown independence remains unknown.
6. Single-source evidence is not automatically unusable; confidence/claim scope must match what survives.
7. Corroboration never replaces source criticism/context.
8. Contradictions remain first-class research objects.

## 8. Capability Candidates

- `CAP-SOURCE-DEPENDENCY`: source/witness derivation and independence hypotheses trackable by claim.
- `CAP-CORROBORATION`: distinguish independent support from repeated transmission.
- `CAP-DISCREPANCY`: diagnose differences by referent/time/purpose/scale/terminology/transmission before disposition.
- `CAP-RELATION-LAYERS`: transmission, historical and interpretive relations explicitly distinct.
- `CAP-DISCRIMINATING-EVIDENCE`: identify what evidence could resolve an unresolved discrepancy/dependency.

## 9. Quality / Requirement Candidates

- REQ-C6-A: Multiple dependent sources must not be counted as independent corroboration.
- REQ-C6-B: Dependency/independence may be claim-specific and uncertain; status must be representable.
- REQ-C6-C: Transmission relations, historical relations and interpretive relations must be distinguishable.
- REQ-C6-D: Discrepancy analysis must check referent/time/source-purpose/transmission/terminology/scale before asserting contradiction or reconciliation.
- REQ-C6-E: System must permit unresolved/genuine contradiction as valid state.
- REQ-C6-F: Derived sources may retain separate research value for questions other than the underlying factual event.

## 10. Challenge interner Prior Art

### `paleo-type`

Confirmed: source relationships themselves need evidence/status; archival/textual/historical truth are different layers. No technical schema inherited.

### RGK

Confirmed with correction: „Abweichung statt Konflikt“ is useful as **diagnostic starting rule**, not final ontology. RGK’s source-function and discrepancy patterns require claim-specific dependency and must allow a final `genuine contradiction` state.

## 11. Open Questions / bounded debt

- Automated citation-lineage detection can assist but cannot establish all historical dependency; #39 may evaluate tools later.
- Exact dependency taxonomies vary strongly by source genre. Expertise Profiles must supply genre-specific checks rather than one universal list.
- Entity resolution is related but separate; false merge risk goes to #40/#41.

## 12. #45 Quality Check

- **Domain fit:** source criticism/text criticism leads; computational graph ideas not allowed to define the method.
- **Evidence fit:** current source-criticism scholarship and established text-critical practice inspected; classical corroboration principle treated historically, not as universal mechanical law.
- **Inference fit:** no assumption that two sources must exist for every valid claim; independence is claim-specific.
- **Terminology fit:** witness/source/derivative/dependence/corroboration/discrepancy/contradiction separated.
- **Provenance fit:** method sources and scope documented.
- **Falsification/challenge:** every dependency/discrepancy disposition requires potential discriminating evidence or may remain unresolved.

## 13. Sättigungsbegründung

For architecture-driving requirements, SOTA is sufficient: historical source criticism and textual transmission studies strongly support lineage/context-sensitive evidence assessment and reject simple document-count corroboration. More genre-specific source criticism belongs in Expertise Profiles and use-case research rather than blocking the core capability definition.
