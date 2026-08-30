# Histo-Orla – Research Question Portfolio v0.1

**Work Owner:** #30  
**Status:** `research-ready / prioritized-v0.1`  
**Inputs:** #28 `problem-baseline.md`, #29 `workflows.md`, #10/#22/#45.  
**Zweck:** Präzise Fragen definieren, die durch fachwissenschaftliche/technische SOTA-Recherche beantwortet werden müssen, bevor Capabilities und Requirements belastbar werden.

## Priorisierungsregeln

**P0:** cross-cutting, wissenschaftliche Invariante, hoher Failure Impact oder Voraussetzung für mehrere spätere Requirements.  
**P1:** wesentlich, aber teilweise durch P0 informierbar oder stärker use-case-spezifisch.  
**P2:** nachgelagert / nicht architecture-driving für die erste Baseline.

---

# P0 – Quellen, Sprache, Expertise, Evidenz, Retrieval

## C1 – Quellen-/Archivlogik, Provenienz, Überlieferung

### RQ-C1-01 — Archival provenance and context

**Frage:** Welche archivwissenschaftlichen Prinzipien und aktuellen Beschreibungsmodelle sind fachlich notwendig, um Records/Bestände über Provenienz, Record Creator, Funktions-/Verwaltungskontext und Überlieferung zu verstehen, ohne Histo-Orla vorschnell an einen formalen Standard zu binden?

- linked: N-004/N-005, P-002/P-006, R-001
- Use Cases: U1–U4
- leading: Archivistik / Registraturkunde
- control: Diplomatik, RDM/Information Science
- source types: Archivstandards, Fachhandbücher, methodische Literatur, nationale/internationale Archivpraxis
- expected impact: Source identity, Archive Routing, provenance requirements
- priority: P0

### RQ-C1-02 — Archive Routing from historical administration

**Frage:** Wie rekonstruieren Historiker:innen/Archivar:innen aus historischer Verwaltungs-, Herrschafts- oder Institutionsgeschichte die wahrscheinlich zuständigen Archive, Bestände und Serien, insbesondere bei territorialen/administrativen Veränderungen?

- linked: N-004, CH-003, P-006
- Use Cases: U1–U3
- leading: Archivistik/Registraturkunde + Landes-/Verwaltungsgeschichte
- control: Diplomatik, regionale Archivkunde
- evidence: archivische Research Guides, Provenienz-/Bestandsführer, regionale Praxis
- expected impact: Archive-Routing Capability
- priority: P0

### RQ-C1-03 — Source/transmission/digital-instance distinctions

**Frage:** Welche fachlich belastbaren Unterscheidungen braucht Histo-Orla zwischen Original/Ausfertigung, Abschrift/Konzept/Kopialbuch, Regest/Edition, bibliographischer/archivalischer Identität, Digitalisat und exakt inspizierter digitaler Instanz?

- linked: N-005/N-006, K-005/K-006, R-001/R-002
- Use Cases: U1–U4
- leading: Diplomatik, Editionswissenschaft, Archivistik
- control: RDM/provenance
- expected impact: minimum source/findspot model
- priority: P0

### RQ-C1-04 — Minimum findspot/citation requirements

**Frage:** Welche minimale Information ist je Quellentyp nötig, damit ein Finding später fachlich überprüfbar auf eine konkrete Quelle/Fundstelle zurückgeführt werden kann?

- linked: N-006, R-002
- Use Cases: U1–U4
- leading: jeweilige Quellenkunde/Edition + Archivistik/Bibliographie
- expected impact: hard requirements for OCR/retrieval/research state
- priority: P0

---

## C2 – Fachliche Problemübersetzung und Terminologie

### RQ-C2-01 — From lay observation to scholarly problem formulation

**Frage:** Welche etablierten Methoden aus historischem Arbeiten, Terminologie-/Informationswissenschaft und ggf. Problem Framing erlauben, eine unscharfe Beobachtung in mehrere fachlich plausible Problemformulierungen zu überführen, ohne eine Kategorie vorschnell festzuschreiben?

- linked: N-001, P-001/P-007, R-005
- Use Cases: U1–U3
- leading: jeweilige historische Fachdomäne + historische Semantik/Begriffsgeschichte
- control: Knowledge Organization / Information Science
- expected impact: Problem-Translation Method
- priority: P0

### RQ-C2-02 — Terminology layers and validity

**Frage:** Wie sollen historischer Quellenbegriff, zeitgenössische institutionelle/rechtliche Bezeichnung, archivische Erschließungssprache, moderne analytische Kategorie, ältere Historiographie, regionale Sonderterminologie und fremdsprachig/lateinische Varianten unterschieden und mit Zeit-/Raum-/Institutionsgültigkeit behandelt werden?

- linked: N-001/N-003, CH-002/CH-005, R-005
- Use Cases: U1–U3
- leading: historische Semantik/Begriffsgeschichte, Fachphilologie
- control: Archivistik, jeweilige Fachdomäne, Knowledge Organization
- expected impact: terminology/value-domain requirements
- priority: P0

### RQ-C2-03 — Concept discovery vs query expansion

**Frage:** Wo endet fachliche Concept Discovery und wo beginnt IR-Query-Expansion; welche Beziehungen (Synonymie, Ober-/Unterbegriff, historische Form, related term, contested concept) dürfen für Suche genutzt werden, ohne fachliche Gleichsetzung zu behaupten?

- linked: N-001/N-008, P-005, R-004/R-005
- Use Cases: U1–U4
- leading: Knowledge Organization + IR + historische Fachdomänen
- expected impact: search/vocabulary separation
- priority: P0

### RQ-C2-04 — Evaluation of problem translation

**Frage:** Wie kann geprüft werden, ob ein System relevante unbekannte Fachbegriffe/Modelle tatsächlich entdeckt, Anachronismen vermeidet und konkurrierende Modelle angemessen offenhält?

- linked: N-018, CH-008
- Use Cases: U1–U3
- leading: Quality Engineering + jeweilige Fachdomänen
- expected impact: acceptance tests / gold cases
- priority: P0

---

## C3 – Expertise Routing und Kompetenzprofile

### RQ-C3-01 — What constitutes operational scholarly expertise?

**Frage:** Welche Bestandteile müssen ein operationales Expertise Profile tragen, damit es mehr ist als ein Rollenprompt: Fachsprache, Gegenstandsmodelle, Quellenlogik, Methoden, zulässige Inferenz, Kontroversen, Region/Epoche, Referenzwerke, Failure Modes und Schnittstellen?

- linked: N-002/N-003, R-013
- Use Cases: U1–U4
- leading: Fachmethodik/Historiographie/Research Design
- control: Knowledge Organization, Research Integrity
- expected impact: Expertise Profile Specification
- priority: P0

### RQ-C3-02 — Routing and neighbor-discipline triggers

**Frage:** Welche fachlich begründbaren Signale zeigen, dass eine zusätzliche Nachbardisziplin aktiviert werden muss, und wie trennt man problem-, source-, method- und validation-routing?

- linked: N-002/N-013, CH-006
- Use Cases: U1–U4
- leading: Research Design + Fachdomänen
- expected impact: routing logic / escalation triggers
- priority: P0

### RQ-C3-03 — Regional expertise evidence

**Frage:** Woran lässt sich regionale Spitzenexpertise praktisch festmachen: regionale Archive, Editionen, Bibliographien, Zeitschriften, Verwaltungs-/Territorialchronologie, Forschungstraditionen, Terminologie und Quellenverluste?

- linked: N-003, CH-003/CH-005
- Use Cases: U1–U3
- leading: Landesgeschichte + regionale Archiv-/Bibliographiekenntnis
- expected impact: regional expertise checklist
- priority: P0

### RQ-C3-04 — AI assistance vs independent expertise validation

**Frage:** Welche Aufgaben darf methodisch geführte KI innerhalb eines Expertise Profiles unterstützen, und wann verlangt die wissenschaftliche Konsequenz unabhängige menschliche Fachvalidierung?

- linked: N-019, R-008/R-012/R-013
- Use Cases: U1–U4
- leading: Research Integrity + Fachdomäne
- control: Human Factors, AI Evaluation
- expected impact: validation-level model
- priority: P0

---

## C6 – Source Dependence / Discrepancy Reasoning

### RQ-C6-01 — Source dependence and independent corroboration

**Frage:** Welche Methoden aus Quellenkritik, Diplomatik, Textkritik, Historiographie und Editionswissenschaft erlauben, Abschrift/Auszug/Edition/Regest/Zitat/gemeinsame Vorlage/historiographische Abhängigkeit zu erkennen und unabhängige Bestätigung von bloßer Wiederholung zu unterscheiden?

- linked: N-009, P-012, R-006
- Use Cases: U1–U4
- leading: Quellenkritik/Diplomatik/Textkritik
- control: Historiographie, jeweilige Fachdomäne
- expected impact: independence/corroboration rules
- priority: P0

### RQ-C6-02 — Discrepancy diagnostics before contradiction

**Frage:** Welche fachlich belastbaren Kategorien helfen, Unterschiede zuerst nach Zeitstand, Quellengattung, Überlieferungsstufe, Zweck, institutioneller Perspektive, Maßstab, Terminologie, Mess-/Darstellungslogik oder Interesse zu diagnostizieren, bevor ein echter Widerspruch behauptet wird?

- linked: N-010, R-007
- Use Cases: U1–U4
- leading: historische Quellenkritik + jeweilige Fachdomäne
- expected impact: discrepancy method
- priority: P0

### RQ-C6-03 — Relation layer separation

**Frage:** Welche methodischen Gründe sprechen für eine harte Trennung zwischen Überlieferungsrelationen, historischen Akteurs-/Ereignisrelationen und interpretativen/researcher-asserted Relationen?

- linked: R-006/R-009/R-014
- Use Cases: U1–U4
- leading: Quellenkritik, historische Methodik
- control: Information Modeling erst nach fachlicher Klärung
- expected impact: scientific invariant before data model
- priority: P0

---

## C7 – OCR/HTR, Corpus, Retrieval, Fundstellen

### RQ-C7-01 — OCR/HTR SOTA by material type

**Frage:** Welche aktuellen Verfahren/Workflows sind für historische deutsche Drucke (inkl. Fraktur), heterogene Scan-PDFs und Handschriften jeweils geeignet, und welche Qualitätsmetriken sind für Namen, Orte, Zahlen und Fachtermini nötig?

- linked: N-007/N-018, R-003
- Use Cases: U4 primary; U1–U3 stress cases
- leading: OCR/HTR/DH
- control: Paläographie/Philologie, Quality Engineering
- expected impact: OCR/HTR decision matrix
- priority: P0

### RQ-C7-02 — Findspot-preserving text representation

**Frage:** Welche Repräsentationen/Standards erhalten Seite/Folio/Regest, Layout und Original↔Derivat-Rückführung so, dass Suche und Zitation belastbar bleiben, ohne unnötige Formatkomplexität einzuführen?

- linked: N-006/N-007, R-002/R-003
- Use Cases: U4 + U1/U2
- leading: DH/document processing/RDM
- expected impact: minimum derivative/findspot requirements
- priority: P0

### RQ-C7-03 — Auditable historical retrieval baseline

**Frage:** Welche Kombination aus Exact Search, Phrasen, Filtern, Fuzzy Matching, historischen Schreibvarianten, linguistischer Expansion und Ranking bietet eine robuste, reproduzierbare Baseline für historische deutsche Korpora?

- linked: N-008, R-004/R-015
- Use Cases: U1–U4
- leading: IR + historische Sprachverarbeitung
- expected impact: retrieval baseline
- priority: P0

### RQ-C7-04 — Admission test for semantic retrieval / RAG

**Frage:** Unter welchen nachweisbaren Bedingungen verbessert semantische Suche/RAG Recall oder Discovery gegenüber der auditierbaren Baseline, ohne exakte Namens-/Fundstellenrecherche zu verschlechtern?

- linked: H-004, R-015
- Use Cases: U4 + U1–U3
- leading: IR/AI Evaluation
- control: Fachdomänen/Research Integrity
- expected impact: optional-layer admission criteria
- priority: P0

### RQ-C7-05 — Personal corpus integration / Zotero hypothesis

**Frage:** Welche Rolle kann Zotero im realen U4-Workflow sinnvoll übernehmen – bibliographische Referenzschicht, Attachments/Volltext, Suche/Annotations/API – und wo braucht es ergänzende, aber nicht redundante Infrastruktur?

- linked: H-001, OQ-016
- Use Cases: U4
- leading: Research Workflow/Bibliographie/Information Management
- control: RSE/IR
- expected impact: Zotero hypothesis disposition
- priority: P0, aber nach methodischem OCR/IR-Baselinebefund finalisieren

---

# P1 – Raum, Handlung, Research UX, Capability Allocation

## C4 – Regionalität / Multi-Scale / Connected History

### RQ-C4-01 — Scale-shift methods

Welche methodischen Kriterien aus Landesgeschichte, Mikrogeschichte, Connected/Entangled/Transregional History und Spatial History rechtfertigen einen Wechsel von lokal/regional zu territorial/reichsweit/europäisch – und wann wäre dies bloß Kontextakkumulation?

- linked: N-012, R-011
- Use Cases: U1–U3
- priority: P1

### RQ-C4-02 — Temporal places and territories

Wie sollen historisch wandelnde Orte, Herrschaften, Verwaltungsräume und Territorien als Kontext behandelt werden, ohne eine moderne Grenzgeometrie zur Wahrheit zu machen?

- linked: CH-003, N-012
- Use Cases: U1–U3
- priority: P1

### RQ-C4-03 — Co-presence vs relationship

Welche methodischen Mindestanforderungen gelten, bevor gemeinsamer Ort, Universität, Hof oder Zeitfenster als historische Beziehung interpretiert werden darf?

- linked: R-009
- Use Cases: U2/U3
- priority: P1

### RQ-C4-04 — Regional research infrastructure

Welche regionalen Archive, Editionen, Bibliographien, Reihen, Gazetteers und Forschungsinfrastrukturen sind für die priorisierten Histo-Orla-Räume methodisch/operativ besonders wichtig?

- linked: N-003/N-004
- Use Cases: U1–U3
- priority: P1; regionaler Layer teilweise parallel zu C1/C3

---

## C5 – Historische Akteurs-/Handlungslogik

### RQ-C5-01 — Historical situation analysis

Welche methodischen Ansätze aus Mikrogeschichte, historischer Anthropologie, Praxeologie, Prosopographie, Institutionen-/Politik-/Adels-/Hofgeschichte eignen sich, Handlungssituationen mit Rollen, Ressourcen, Zwängen, Informationshorizont und zeitgenössisch möglichen Optionen zu rekonstruieren?

- linked: N-011, R-010
- Use Cases: U3 primary / U2 secondary
- priority: P1

### RQ-C5-02 — Motive and attribution distinctions

Wie werden beobachtete Handlung, dokumentiertes Motiv/Selbstbeschreibung, fremde Zuschreibung, struktureller Anreiz/Zwang und Analystenhypothese quellenkritisch getrennt?

- linked: R-010
- Use Cases: U3/U2
- priority: P1

### RQ-C5-03 — Alternative explanation / falsification

Welche Methoden helfen, mehrere historische Erklärungen systematisch offen zu halten und durch Gegenbelege, alternative Quellen oder abweichende Kontexte zu testen?

- linked: N-014, #12 Falsification principle
- Use Cases: U3
- priority: P1

---

## C8 – Human-readable Research State / Auditability

### RQ-C8-01 — Progressive disclosure for scholarly state

Welche Human-Factors-/Research-UX-Muster erlauben, von verständlicher Kurzsynthese zu Fachbegriff, Methode, Finding, Quelle/Fundstelle, Unsicherheit und Alternative zu navigieren, ohne mehrere Wahrheiten zu erzeugen?

- linked: G-009, P-014, R-020
- Use Cases: U1–U4
- priority: P1

### RQ-C8-02 — Challengeability interfaces

Welche minimalen Audit-/Challenge-Aktionen braucht der Research Owner bzw. Fachprüfer: Warum? Quelle? Methode? Alternative? Was fehlt? Wie validiert?

- linked: G-009, N-019
- Use Cases: U1–U4
- priority: P1

### RQ-C8-03 — Uncertainty/controversy presentation

Wie lassen sich Evidenzstatus, Unsicherheit, Kontroversen und Research Debt verständlich darstellen, ohne numerische Scheingenauigkeit oder Eindeutigkeit zu erzeugen?

- linked: N-014, R-020
- Use Cases: U1–U4
- priority: P1

### RQ-C8-04 — Research vs mediation views

Wie lassen sich mehrere Forschungs-/Audit-Sichten aus einem kanonischen Research State ableiten, während adressatenspezifische Vermittlung außerhalb des Core bleibt und nicht zurückschreibt?

- linked: K-003, R-021, H-009
- Use Cases: U1–U4
- priority: P1

---

## C9 – Capability Allocation / Automation / AI / Technical Subsidiarity

### RQ-C9-01 — Allocation rules

Welche Kriterien entscheiden zuverlässig zwischen Research Owner, Fachspezialist, deterministischer Software, spezialisiertem Algorithmus/ML und generativer KI?

- linked: N-017, R-016/R-023
- Use Cases: U1–U4
- priority: P1; final synthesis after C1–C8

### RQ-C9-02 — Candidate→Review→Promotion

Für welche probabilistischen/LLM-gestützten Aufgaben ist ein Candidate→Review→Promotion-Muster fachlich/technisch sinnvoll und welche Promotion-Regeln sind erforderlich?

- linked: H-007, R-008/R-016
- Use Cases: U2–U4
- priority: P1

### RQ-C9-03 — AI-negative deterministic core

Welche wissenschaftlich/technisch formalisierbaren Invarianten müssen deterministisch erzwungen werden (IDs, Provenienz, Fundstellen, Status, Rechteflags, Original/Derivat etc.)?

- linked: K-005/K-006, R-016/R-018
- Use Cases: U1–U4
- priority: P1

### RQ-C9-04 — Reuse/build/integrate and portability

Welche vorhandenen Werkzeuge/Standards decken validierte Capabilities ausreichend ab; wo wäre Eigenentwicklung gerechtfertigt und welche Portabilitäts-/Lock-in-Grenzen gelten?

- linked: G-008/G-012, N-020, R-017/R-023
- Use Cases: U1–U4
- priority: P1

### RQ-C9-05 — Rights/data-governance admission

Welche Rechte-/Datenschutz-/Nutzungsbedingungen müssen als technische Admission Criteria behandelt werden, bevor Quellen an Cloud-/AI-/OCR-Dienste gesendet oder dauerhaft gespeichert werden?

- linked: N-016, R-019
- Use Cases: U1–U4
- leading: Legal/Rights/Data Governance + RSE
- priority: P1; Detailprüfung tool-/source-spezifisch später

---

# P2 / bounded research debt for first architecture baseline

Diese Punkte bleiben sichtbar, sollen aber die erste SOTA-/Requirements-Baseline nicht unnötig blockieren:

1. Vollständiger produktiver Workflow sämtlicher potenzieller Quellenarten.
2. Erschöpfende regionale Bestandskartierung aller angrenzenden europäischen Räume.
3. Finale technische Übergabe Histo-Orla → RGK/Public History.
4. Finale Ontologie/Knowledge-Graph-/Event-/Relationrepräsentation.
5. Performance-/Scale-Optimierung ohne beobachtete Bestandsgrößen-Bottlenecks.
6. Vollständige External-Expert-Service-/Kostenstrategie.

---

# Dependency Map

```text
C1 Provenienz/Quellen ─────┐
                           ├→ C6 Source Dependence → Capability/Evidence Requirements
C2 Problem/Terminologie ───┤
                           ├→ C3 Expertise Routing → Kompetenz-/Validation Requirements
                           └→ C7 Retrieval

C1 + C2 + C3 ───────────────→ C4 Regional/Multi-Scale
C3 + C6 ────────────────────→ C5 Akteurslogik
C1 + C3 + C6 ───────────────→ C8 Research State/Auditability
C1–C8 Findings ─────────────→ C9 Capability Allocation

alle ─→ #40 Risk/Constraints ─→ #41 Capabilities/Quality ─→ #42 Requirements ─→ #43 Gate
```

# Competency Routing Matrix

| Cluster | Leading competencies | Controlling / neighboring |
|---|---|---|
| C1 | Archivistik, Registraturkunde, Diplomatik, Editionswissenschaft | RDM, Bibliographie, Landes-/Verwaltungsgeschichte |
| C2 | historische Semantik/Begriffsgeschichte, Fachphilologie, jeweilige Fachdomäne | Knowledge Organization, IR, Archivistik |
| C3 | Fachmethodik, Historiographie, Research Design | Research Integrity, Human Factors, Knowledge Organization, AI Eval |
| C4 | Landesgeschichte, historische Geographie, Connected/Entangled History | Prosopographie, GIS/Spatial Humanities, Archivkunde |
| C5 | Mikrogeschichte, historische Anthropologie/Praxeologie, Prosopographie | Adels-/Hof-/Politik-/Sozial-/Wirtschafts-/Konfessionsgeschichte |
| C6 | Quellenkritik, Diplomatik, Textkritik/Editionswissenschaft | Historiographie, jeweilige Fachdomäne |
| C7 | OCR/HTR/DH, IR, historische Sprachverarbeitung | Paläographie, RDM, Quality Engineering, RSE |
| C8 | Human Factors/Research UX, Information Architecture | Research Integrity, Accessibility, Fachdomänen |
| C9 | RSE/Software Architecture, IR/OCR/ML, AI Evaluation | Research Integrity, Quality, Legal/Rights, jeweils fachlicher Owner |

# Research Protocol / Quality

Alle RQs werden gemäß #45 recherchiert. Insbesondere:

- authoritative disciplinary sources vor Produkt-/Toollisten;
- externe SOTA-Prüfung von `paleo-type`/#12 und RGK/#21;
- regionale Ebene dort, wo Problem/Quellenlogik davon abhängt;
- Search Boundaries für negative Findings;
- keine Behauptung aus Snippet/Abstract als gelesener Fachinhalt;
- Findings → Capability/Quality/Requirement implication getrennt halten.

## Sättigungsbegründung WP-C

Das Portfolio ist research-ready, weil alle high-impact Open Questions aus #28 mindestens einem RQ-Owner zugeordnet sind, U1–U4 abgedeckt werden und solution choices bewusst offenbleiben. Weitere Fragen dürfen während SOTA entstehen; sie werden in den bestehenden Work Owner integriert, sofern kein eigenständiger Scope nach #23 entsteht.

## Nächste Aktion

P0-SOTA parallel beginnen: #31 C1, #32 C2, #33 C3, #34 C6, #35 C7. #45 gilt als gemeinsames Research Protocol.
