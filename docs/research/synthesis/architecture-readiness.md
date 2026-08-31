# Histo-Orla – Architecture Readiness Report

**Work Owner:** #43  
**Gate date:** 2026-08-31  
**Gate result:** `architecture-ready-with-bounded-research-debt`  
**Inputs:** #28–#42; #44 Decision Register; #45 Research Protocol; fachliche Scope-/Governance-Owner #9/#13–#16/#19/#20/#24; Live Research #46/#47.  
**Scope of this gate:** entscheidet, ob Architektur-/Designvergleich und gezielte Prototypen verantwortbar beginnen können. **Es entscheidet keine Zielarchitektur.**

---

# 1. Executive Gate Finding

Histo-Orla ist **architecture-ready-with-bounded-research-debt**.

Die architecture-driving wissenschaftlichen Invarianten, Quality-/Risk-Grenzen und Requirements sind ausreichend klar, um Architekturvarianten zu entwerfen, gegen Requirements zu vergleichen und mit reversiblen Prototypen zu diskriminieren.

Es besteht **kein aktueller #44-Blocker** und keine Owner-Decision, die vor Beginn der Architekturarbeit zwingend getroffen werden müsste.

Offene historische Forschung in #46/#47 bleibt wichtig, verändert derzeit aber nicht die fundamentalen architecture-driving Invarianten. Sie dient weiter als Live-Stress-/Falsifikationsfall und kann Requirements iterativ schärfen. Wenn ein Live-Fall später eine neue fachliche Invariante zeigt, wird die betroffene Requirement-/Architecture-Entscheidung gezielt reopened; das ist normale iterative Research Governance.

Der Readiness-Status ist bewusst **nicht `architecture-ready` ohne Zusatz**, weil mehrere Designentscheidungen noch durch konkrete Corpus-/Integration-/UX-Prototypen diskriminiert werden müssen und einige domänenspezifische Research Assets noch wachsen. Diese offenen Punkte sind klar begrenzt und dürfen nicht als Vorwand für weitere abstrakte Vorplanung dienen.

---

# 2. Gate Assessment – Problem / Need

## Q1 – Sind die wichtigsten Nutzer-/Forschungsprobleme hinreichend verstanden?

**PASS.**

#28 atomisiert Goals, Needs, Pains, Challenges, Risks, Constraints und Hypothesen. Zentrale Problems sind cross-workflow stabil:

- fehlendes Fachvokabular / fachliche Problemübersetzung;
- Expertise Routing / regionale Fachkompetenz;
- Archive/Source Discovery über Provenienz;
- Source/Representation/Findspot Control;
- OCR/HTR und historisches Retrieval;
- Source Dependence / Discrepancy;
- Entity-/Relation-/Motive-Fehlschlüsse;
- Multi-Scale / Multi-Evidence historische Analyse;
- human-readable Auditability;
- reproducible/portable Research State;
- Rights/Privacy/Provider-Grenzen.

Live Research #46/#47 bestätigt mehrere dieser Friktionen real und erzeugt keine grundsätzlich neue Problemklasse.

## Q2 – Sind Needs/Pains von Lösungen getrennt?

**PASS.**

#41/#42 halten Zotero, SQLite/FTS, Elasticsearch/Solr, RAG/Embeddings, Knowledge Graph, Multi-Agent, konkrete OCR-/HTR-Engines und UI-Technologien ausdrücklich auf Architecture-/Hypothesenstatus.

## Q3 – Decken U1–U4 die kritischsten Realfälle ab?

**PASS WITH BOUNDED DEBT.**

- U1 deckt Raum/Umwelt/Karten/Archive/Rechte/Multi-Evidence.
- U2 deckt Quellenkritik, Terminologie, Homonyme, Entity/Relation, Discrepancy, Search Boundaries.
- U3 deckt Akteur/Information/Motive/Relation/Alternativen.
- U4 deckt Ingest/OCR/Findspot/Retrieval/Portability/Automation.

U1/U2 laufen real als #47/#46. U3 besitzt noch keinen gleich tiefen Live-Goldfall; dies ist `bounded research debt`, da C5-Methode und Requirements fachlich ausreichend geklärt sind und Architektur keine spezifische U3-Lösung festlegen muss.

---

# 3. Gate Assessment – Fachlichkeit

## Q4 – Sind führende Fachdomänen und wissenschaftliche Invarianten klar?

**PASS.**

#41/#42 weisen pro Capability/Requirement führende/controlling Fachdomänen aus. Zentral:

- Fachdomäne owns method/evidence/inference;
- Problemübersetzung ≠ Synonymie;
- Quelle/Instanz/Derivat/editorial layer/Finding/Claim/Interpretation/Synthese getrennt;
- AI ≠ Evidenz / unabhängige Validation;
- Findmittel ≠ inspected source;
- abhängige Evidenz ≠ unabhängige Corroboration;
- unresolved/contradiction/controversy sind legitime States;
- Entity/Relation/Motive Promotion ist evidenzgebunden;
- historische Räume/Begriffe sind zeit-/kontextabhängig;
- mehrere Evidenzachsen behalten eigene Aussagegrenzen.

## Q5 – Sind zentrale Begriffs-/Quellen-/Evidenzfragen ausreichend SOTA-geprüft?

**PASS.**

#31–#39 wurden jeweils `sufficient-for-current-decision` abgeschlossen. Es besteht kein Hinweis, dass weitere breite SOTA-Recherche die Architekturgrundlagen materiell verändern würde. Weitere Recherche erfolgt nur bei konkreter Architecture-/Prototype-Frage.

## Q6 – Sind Kontroversen/Unsicherheiten so dokumentiert, dass Architektur sie nicht versehentlich auflöst?

**PASS.**

REQ-EPI-004, REQ-CRIT-002, REQ-ENT-001, REQ-SYN-001/002 und die entsprechenden Capabilities verlangen unresolved/candidate/alternative/contradiction states. U2 `1374/1378` ist ein konkreter Stressfall.

---

# 4. Gate Assessment – Quality / Risk

## Q7 – Sind High-Risk Failure Modes identifiziert und testbar?

**PASS.**

#40 dokumentiert 30 Failure Modes und 11 High-Risk Acceptance/Falsification Tests. Architecture-driving Critical/High-Risks sind u. a.:

- Source Laundering / Findspot Loss;
- OCR critical-token corruption;
- Retrieval blind spots / semantic displacement;
- False Equivalence / Anachronism;
- False Corroboration / Premature Harmonization;
- False Entity Merge / Proxy Relation / Motive Psychology;
- Regional Container / Domain Flattening;
- Simulated Expertise / GenAI canonical mutation;
- Provider/Format Lock-in;
- Rights-invalid processing;
- Research UX epistemic loss / Mediation back-write.

## Q8 – Sind Rights/Privacy/Provider-/Lock-in-Constraints vor Architektur bekannt?

**PASS WITH BOUNDED CASE-SPECIFIC DEBT.**

Die architecture-driving Regel ist klar: lawful access, copying/TDM, retention, external processing, publication/sharing und privacy sind getrennte Prüfbereiche. Unknown/restricted material muss Processing Admission beeinflussen.

Konkrete Archive/Lizenzen/Cloud-Service-Terms können erst bei realer Source-/Provider-Wahl abschließend bewertet werden. Das ist `external/source-specific dependency`, kein allgemeiner Gate-Blocker.

## Q9 – Existieren Acceptance-/Falsifikationsfälle für architecture-driving Requirements?

**PASS.**

#41 enthält eine Seed Suite; #42 bindet U1–U4 an Requirements. Besonders belastbar:

- Findmittel ≠ inspected source;
- U4 Findspot Roundtrip;
- U2 editorial `[Stange]` Layer;
- Altenburg-/Orla-Knau False-Merge-Test;
- bounded negative findings;
- U2 1374/1378 discrepancy;
- Knewe/Stange proxy relation;
- U3 motive test;
- provider removal;
- rights admission;
- answer→source/method audit;
- mediation no-back-write.

---

# 5. Gate Assessment – Requirements

## Q10 – Sind priorisierte Requirements traceable und verifizierbar?

**PASS.**

#42 dokumentiert pro P0/P1 Requirement Rationale, Owner, Capability, Use Case, Invariant, Acceptance, Risk und SOTA/Evidence. Die Baseline ist fein genug für Architekturvergleich, ohne Technologie vorwegzunehmen.

## Q11 – Sind echte Trade-offs und Konflikte isoliert?

**PASS.**

Aktuell keine unauflösbaren Requirement-Konflikte. Dokumentierte Design Trade-offs:

1. Automation ↔ Human Control – durch consequence-based validation lösbar;
2. Portable State ↔ Cloud Processing – portable canonical state, replaceable external processor;
3. Rich Domain Distinctions ↔ Lean Complexity – nur belegte fachliche Unterschiede modellieren;
4. Semantic ↔ Exact Search – Exact baseline; Semantic optional benchmark-admitted;
5. Zotero Integration ↔ Independent Research State – Architekturvergleich, kein fachlicher Konflikt.

## Q12 – Ist klar, welche Requirements hart und welche Designfreiheiten offen sind?

**PASS.**

Harte Bereiche sind Source/Layer/Findspot Integrity, epistemic states, deterministic promotion/invariants, auditability, portability, rights admission und provider-independent curated state.

Designfreiheit besteht u. a. bei Speichertechnologie, Search Engine, konkreten Standards/Serialisierungen, Agentenstruktur, OCR/HTR-Provider, UI Framework und local/cloud Processor Placement.

---

# 6. Gate Assessment – Technology / Lean

## Q13 – Welche vorhandene Infrastruktur/Tools müssen vor Eigenentwicklung evaluiert werden?

**PASS – Architekturauftrag klar.**

Vor Eigenentwicklung müssen problembezogen verglichen/prototypisiert werden:

### Bibliography / Source Integration

- Zotero Local/Web APIs und Attachment/Fulltext-Funktionen als starker Integrationskandidat;
- Escape-Hatch/Research-State-Grenze muss getestet werden.

### OCR/HTR / Document Processing

- bestehende OCR-/HTR- und DH-Werkzeuge aus C7, material-/corpusbezogen benchmarken;
- konkrete Engine nicht aus Präferenz wählen.

### Search / Retrieval

- kleine klassische Volltext-/Indexlösungen gegen tatsächlichen Corpus und Gold Queries vergleichen;
- Semantic/RAG erst nach Baseline-Benchmark.

### Standards / Interchange

- etablierte Repräsentations-/Provenienz-/Layoutstandards nur dort einsetzen, wo sie konkrete Requirements erfüllen; keine Standard-Maximalarchitektur.

### Gazetteer / Spatial

- vorhandene Gazetteer-/Authority-Infrastrukturen für Candidate Matching nutzen/prüfen; kein vollständiges eigenes Ortswissenssystem vor realem Bedarf.

## Q14 – Welche Entscheidungen sind reversibel und durch Prototyp diskriminierbar?

**PASS – umfangreich.**

Reversibel/testbar:

- Zotero Adapter/Boundary;
- canonical-state serialization/storage candidates;
- exact-search/index candidates;
- OCR/HTR processors;
- query-expansion implementation;
- audit-view/UI prototype;
- candidate/promotion workflow representation;
- optional semantic retrieval;
- processor adapter design;
- gazetteer matching;
- sync/job mechanism.

Diese gehören in die nächste Architecture/Prototype-Phase, nicht nach #44.

## Q15 – Welche Entscheidungen sind teuer/irreversibel/lock-in-relevant und brauchen Owner-Zulassung?

**NO CURRENT DECISION; TRIGGERS IDENTIFIED.**

Mögliche spätere #44-Triggers:

- proprietärer/cloudgebundener Processor mit überlegener Qualität, aber materiellem Kosten-/Rights-/Privacy-/Lock-in-Trade-off;
- kanonischer State in unexportierbarer Plattform;
- dauerhaft kosten-/betriebsintensive Infrastruktur ohne gleichwertig reversible Alternative;
- Source-/Archivbedingungen, die gewünschte Verarbeitung/Retention ausschließen;
- architecture-wide Material Change mit mehreren fachlich gleichwertigen, aber normativ unterschiedlichen Optionen.

Aktuell ist keine solche Wahl nötig.

---

# 7. Open Points Classification

## A. Bounded Research Debt

### BRD-01 – U1 Live Research nicht gesättigt

#47 läuft weiter. Relevant für weitere Quellen-/Raum-/Multi-Evidence-Goldfälle, aber keine heutige architecture-driving Invariante hängt von vollständiger Teichlandschaftsrekonstruktion ab.

### BRD-02 – U2 Live Research nicht gesättigt

#46 Source Resolution (u. a. `Knauwe villa` 1374/1378) läuft weiter. Methodische Requirements sind bereits durch diesen unresolved Fall gestützt.

### BRD-03 – U3 konkreter Live-Goldfall fehlt

Historical Situation Analysis ist SOTA-seitig ausreichend; konkrete Akteurstestdaten müssen vor MVP-Verifikation ergänzt werden.

### BRD-04 – Regional Gazetteer/Territory Layer unvollständig

Iterativ aus realer Forschung aufbauen; keine Full-Coverage-Vorbedingung.

### BRD-05 – Expertise Profiles noch nicht für alle Domänen voll ausgearbeitet

Architektur muss Profile/Methoden modular repräsentierbar machen; Inhalte wachsen use-case-driven.

### BRD-06 – konkrete Research UX / Accessibility-Evaluation offen

Grundanforderung Auditability/Progressive Disclosure ist klar; konkrete UI empirisch prototypisieren.

### BRD-07 – Performance-/Scale-Anforderungen unquantifiziert

Kein beobachteter Bottleneck; Messung nach realem Corpus/MVP.

## B. Technical Experiments Required

### EXP-01 – Canonical State Persistence Spike

Vergleiche kleinste hinreichende Repräsentations-/Persistenzvarianten gegen Layer/Traceability/Portability/Human Readability.

### EXP-02 – Zotero Integration Spike

Teste Item/Attachment/Fulltext/Identifiers, Offline-/Export-/Failure-Verhalten und Grenze zum kuratierten Research State.

### EXP-03 – Retrieval Baseline Benchmark

Gold Queries U1/U2/U4 gegen candidate search/index approaches; Exact + variants + filters + Query Provenance.

### EXP-04 – OCR/HTR Corpus Benchmark

Representative historical print/image/handwriting slices; critical-token + findspot tests.

### EXP-05 – Candidate/Promotion/Invariants Spike

Entity/Relation/Claim candidates, unresolved/discrepancy states, deterministic transition checks.

### EXP-06 – Research Audit View Prototype

Orientation→Finding→Source→Method→Controversy navigation from a single canonical state.

### EXP-07 – Processor Replaceability / Provider Removal Test

One external/AI processor removed/replaced without curated state loss.

### EXP-08 – Rights Admission Flow Spike

At least public-domain/open vs. restricted/unknown material routes.

## C. External Dependencies

### EXT-01 – Source-/archive-specific rights and access

Only when a concrete archival/license corpus is ingested externally/retained/shared.

### EXT-02 – External service/API capabilities/terms

Only at candidate integration evaluation.

### EXT-03 – Physical archive/source inspection

Needed for historical live research, not for architecture baseline.

## D. External Specialist Validation

**None required to start architecture.**

Later trigger: publication-level/consequential claims or domain-specific validation requirement.

## E. Owner Decisions

**None currently required.**

#44 remains empty.

## F. Architecture Choices

- canonical persistence/storage technology;
- normalized relational vs. document/file vs. graph-assisted representations (possibly combinations);
- exact-search/index engine;
- Zotero boundary/integration pattern;
- OCR/HTR processor topology;
- optional semantic layer;
- UI/application surface;
- local/external processor placement;
- standards/serialization choices;
- sync/job mechanism.

These are deliberately **not decided at this gate**.

## G. Implementation Details

IDs, concrete filenames/commands, framework libraries, table names, CLI syntax, cache paths, specific adapters etc. remain implementation freedom unless a later invariant demands otherwise.

---

# 8. Architecture Question Set – Next Phase

Each architecture question must compare alternatives against the requirements baseline and use a small reversible prototype where useful.

## AQ-01 – What is the leanest canonical Research State that preserves all epistemic layers?

Must satisfy: ADRQ-01/02/03/06/10.

Compare candidate representations without assuming DB/KG/flat-files first. Test U2 editorial layer, unresolved discrepancy, entity candidate and U4 provenance.

## AQ-02 – What is canonical vs. regenerable?

Define curated Source/Instance/Finding/Claim/Interpretation/Status/Provenance vs. index/cache/OCR intermediate/embedding/derived views. Test rebuild and provider-removal.

## AQ-03 – What role should Zotero actually own?

Evaluate bibliographic identity, attachments, fulltext, collections/tags and APIs. Determine what remains Histo-Orla canonical state and how stable references/export work.

## AQ-04 – How is the document/derivative/findspot pipeline represented?

Compare minimal patterns/standards that preserve page/folio/region, raw/corrected OCR, processor provenance and parentage. Do not standard-maximize.

## AQ-05 – Which exact/historical retrieval baseline is sufficient?

Benchmark candidate index/search approaches against U1/U2/U4 Gold Queries: exact, variants, filters, context windows, query provenance, findspots. Semantic layer only after baseline.

## AQ-06 – How are Candidate→Review→Promotion and deterministic invariants implemented?

Need explicit transitions for Entity/Relation/Claim/Validation/Discrepancy while avoiding bureaucratic workflow over-modeling.

## AQ-07 – How are domain-specific models preserved without one giant ontology?

Test whether a small common epistemic kernel plus domain-owned extensible profiles/fields/views is sufficient. Reject any model that collapses U1/U2/U3 distinctions.

## AQ-08 – How are relation/proxy/network views derived safely?

Need provenance-backed edges/proxies, temporal validity and view disclosure without assuming a graph database.

## AQ-09 – How are human-readable audit views derived from one state?

Prototype progressive disclosure without duplicating truth. Test Research Owner and expert-review paths.

## AQ-10 – What processor/service boundary gives replaceability with low complexity?

OCR/HTR/AI/search/gazetteer services should be replaceable where beneficial while deterministic core stays stable. Compare simplest adapter strategy.

## AQ-11 – How is rights/privacy admission enforced without creating legal-workflow bureaucracy?

Define minimum rights metadata/status/policy gates; route unknown/high-risk cases to human decision only when necessary.

## AQ-12 – What is the deployment/locality model?

Derive local vs. external processing from rights, performance, cost, availability and portability; do not assume everything local or cloud.

## AQ-13 – How is Research↔Mediation handoff kept one-way/auditable?

Only boundary/traceability required initially; exact export/API deferred until downstream need is concrete.

---

# 9. Architecture-Phase Admission Rules

Architecture work must obey:

1. no component without mapped Requirement/Quality/Risk;
2. existing tools/infrastructures before custom build;
3. reversible prototype before durable choice where possible;
4. no Semantic/RAG/KG/Multi-Agent by default;
5. no provider-owned canonical state;
6. deterministic enforcement for formal invariants;
7. scientific domain model may not be weakened for technical convenience;
8. architecture variants must be tested with U1–U4, not only toy examples;
9. new live-domain requirement can reopen a decision if it falsifies an assumption;
10. expensive/irreversible/rights-sensitive choices go to #44 only when they become concrete.

---

# 10. Gate Decision

## Result

`architecture-ready-with-bounded-research-debt`

## Why not `not-ready`?

No central scientific invariant, high-risk control, user goal or architecture-driving Requirement remains undefined enough to force architecture to guess the research method.

## Why not unconditional `architecture-ready`?

Corpus-/integration-/UX choices still require concrete reversible experiments, and live U1/U2 plus a future U3 Gold Case should continue to test the architecture. These debts are bounded and do not justify more abstract planning before architecture/prototyping.

## Why not `decision-required`?

#44 contains no genuine blocker. Current open choices are testable/reversible architecture choices, not normative Research-Owner choices.

---

# 11. Next Executable Phase

The next phase should begin with **architecture alternatives + thin vertical prototypes**, not additional generic SOTA.

Recommended sequence:

```text
Architecture principles from Requirements
→ 2–3 lean architecture variants
→ explicit trade-off matrix against ADRQ-01..12
→ EXP-01..08 targeted spikes / thin vertical slices
→ select smallest sufficient architecture
→ ADRs for material choices
→ MVP slice using U2/U4 first, U1/U3 controls
→ deterministic + scholarly verification
→ real-use evaluation
```

A useful first vertical slice should prove at least:

`bibliographic/source identity → inspected instance/derivative → OCR/text → exact+variant search → findspot excerpt → candidate/finding → audit view → portable state`

with U2 homonym/editorial-discrepancy tests and U4 findspot/provider-removal tests.

This is an **architecture/prototype assignment**, not yet an implementation stack decision.

---

# 12. #45 / Gate Quality Check

- **Domain fit:** architecture-driving requirements retain disciplinary ownership.
- **Evidence fit:** gate is based on completed Discovery/SOTA/Risk/Capability/Requirements artifacts and live stress cases.
- **Inference fit:** ongoing historical research is not treated as completed, but its incompleteness is not confused with architecture unreadiness.
- **Terminology fit:** Research Debt, Technical Experiment, External Dependency, Owner Decision, Architecture Choice and Implementation Detail are separated.
- **Provenance fit:** each gate area maps to #28–#42 and #46/#47 where relevant.
- **Falsification/challenge:** readiness can be reopened if a live use case falsifies an architecture assumption; next-phase experiments are explicit.

**Restartability:** a new competent architecture/research engineer can begin the next phase from repository state without needing this chat.
