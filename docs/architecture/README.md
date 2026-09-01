# Histo-Orla – Technical Delivery / Evolutionary Architecture Index

**Technical Lead:** #48  
**Development / Verification:** #59  
**Requirements:** #42  
**Project Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Zweck

Dieses Verzeichnis enthält technische Research-, Delivery-, Architecture-, Assurance- und Entscheidungsartefakte für das private Histo-Orla-Forschungssystem.

Architecture ist kein separates Vorab-Gate. Sie entsteht just in time aus **akzeptierten Requirements, technischen Risiken, Goals/Needs/Pains und realer Nutzung**.

Kanonische Requirements:

- `../research/synthesis/requirements-baseline.md`
- `../research/synthesis/requirements-extensions.md`
- `../research/synthesis/requirements-structure.md`
- `../research/synthesis/requirements-responsibility-dependency-map.md`

Kanonische technische Ableitungslogik:

- `requirements-derivation.md`

Assurance:

- `assurance/requirements-assurance-harness.md` – #62 formale Requirements-QA
- `assurance/value-decision-delivery-assurance.md` – #63 Goal/Need/Pain → Requirement → Decision → Delivery → Feedback
- `../tools/requirements/README.md`
- `../tools/assurance/`

Delivery-/Verification-Coverage:

- `../development/requirements-coverage.md`

## Leitpfad

```text
Goal / Need / Pain / realer Research-Pain
→ accepted Requirement
→ Motivation / Scope / Dependencies / Criticality verstehen
→ System Responsibility / Architecture Concern
→ Technical Research Question
→ technische SOTA / Best Practice / Existing Tools / Standards
→ Candidate Approach
→ Risiko / Loss / Reversibilität
→ Decision / Implementation Trace gegen Governance (#63)
→ implement-reversible | Spike/Benchmark | ADR | #44
→ implementieren
→ fachlich + technisch verifizieren
→ reale Nutzung / Owner-Feedback
→ behalten | anpassen | Requirement-/Method-/Decision-Delta
```

Direkte Ableitung `Requirement → bevorzugte Technologie` ist zu vermeiden. Ebenso darf technische Delivery nicht nach `verified` enden, wenn die Acceptance reale Owner-/Workflow-Nutzung verlangt.

## Aktive Work Owner

### Technical Lead / Development

- **#48** – Technical Lead: lean Umsetzung, SOTA/Best Practice, evolutionäre Architektur
- **#59** – System Development & Verification

### Integration / Kernzustand

- **#49** – Zotero ↔ OneDrive Integration
- **#50** – Canonical Research State / Source Identity
- **#51** – Document-/Findspot-Pipeline

### Retrieval / Processing / Assurance

- **#52** – OCR/HTR Benchmark/Integration
- **#53** – Historical Retrieval
- **#54** – Candidate/Promotion / formal prüfbare Invarianten
- **#55** – Human-readable Audit
- **#56** – Rights / Credentials / External Processing
- **#57** – Provider Removal / Export / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff Technical Research
- **#62** – Requirements Assurance Harness / deterministische Requirements-QA
- **#63** – Value / Decision / Delivery / Feedback Assurance Spine

### Architecture Decisions

- **#58** – just-in-time ADR Support bei materiellen/schwer reversiblen Entscheidungen

### Fachliche / Value-Upstream-Schnittstelle

- **#28** – Goals / Needs / Pains / Problem baseline
- **#60** – Domain Method Profiles / Method Truth
- **#42** – accepted Requirements / Structure / Traceability
- **#46/#47** – reale Research-/Problem-/Verification-Fälle
- **Research Owner Feedback** – reale Workflow-/Nutzen-Evidenz, nicht historische Evidenz

## Requirement → Architecture Derivation

`requirements-derivation.md` definiert die #48-Sicht.

Materielle technische Arbeit beginnt mit einer Derivation Card bzw. einer entsprechend nachvollziehbaren Kurzform:

```text
Goals / Needs / Pains
→ Requirements / Scope
→ System Responsibilities
→ Architecture Concerns / Quality Attributes
→ Dependencies
→ Technical Research Questions
→ Existing Tools / Standards / Patterns
→ Candidate Approaches
→ Trade-offs / Loss / Reversibility
→ Decision Class
→ Verification Target
```

Damit bleibt die fachliche Requirement Truth unter #42 unangetastet, während #48 Lösungsräume gezielt untersuchen kann.

### Quality / Failure Scenarios

Für architecture-significant Anforderungen kann ein kleines Quality Scenario verwendet werden:

```text
context / environment
trigger / stimulus
betroffenes Objekt / responsibility
expected response
measurable pass condition
failure / scientific or technical loss
```

Das ist eine lean adaptierte Nutzung etablierter QAW/ATAM-Prinzipien, kein formales Enterprise-Gate.

## Deterministic Requirements Assurance – #62

#62 operationalisiert formal geklärte Requirements-Regeln als kleinen ausführbaren QA-Baustein:

```text
canonical Requirement Truth (#42 Markdown)
→ machine-readable QA-/Traceability-Projektion
→ JSON Schema
→ Python Cross-Record-/Repo-Validator
→ negative/positive Regressionstests
→ lokaler CLI + GitHub Actions
```

Grenze:

- Schema/Validator prüfen Struktur, IDs, Referenzen, Authority-/Dependency-/Coverage-/Lifecycle-Invarianten;
- Domain-/Fachreview prüft fachliche Bedeutung und wissenschaftliche Suffizienz;
- Skill/LLM darf Bedienoberfläche/Erklärung sein, niemals Enforcement- oder Truth-Instanz.

Aktueller CI-Realtest: Requirements-Assurance-Lauf `33479807761` erfolgreich. `REQ-TRACE-001` ist selbst in der strukturierten QA-Projektion und Delivery-Coverage enthalten.

## Value / Decision / Delivery / Feedback Assurance – #63

#63 operationalisiert die formale Non-Regression-/Traceability-Schicht zwischen Nutzer-/Forschungsursprung und technischer Delivery:

```text
Goal / Need / Pain / Constraint
→ accepted Requirement
→ Decision bzw. begründete reversible Direktumsetzung
→ Implementation
→ Verification
→ reale Nutzung / Owner-Feedback
→ Delta
```

Bausteine:

- `../tools/assurance/trace-record.schema.json`
- `../tools/assurance/governance-registry.json`
- `../tools/assurance/policy.json`
- `../tools/assurance/data/trace-records.json`
- `../tools/assurance/validate.py`
- `../tools/assurance/tests/`
- `../.github/workflows/project-assurance.yml`

Harte formale Checks umfassen u. a. Requirement-/Driver-/Governance-Referenzen, Decision→Implementation-Referenzintegrität, Verification-Evidence, Feedback-Deltas und einen Changed-Code-Guard für kontrollierte technische Pfade.

Ein alter `verified` Implementation-Record darf einen Pfad nicht dauerhaft freischalten; neue Änderungen brauchen einen aktuellen aktiven/implementierten Trace-Kontext.

Reale Owner-/Nutzer-Rückmeldung ist Product-/Workflow-Evidence. Sie darf weder historische Evidence noch Fachvalidation simulieren. Negative Rückmeldung erzeugt einen sichtbaren Delta-Pfad; `owner-workflow-acceptance` kann nicht durch einen technischen Selbsttest erfüllt werden.

Aktueller CI-Realtest: Project-Assurance-Lauf `33479807679` erfolgreich; 15 Project-Assurance-Regressionstests plus 14 Requirements-Regressionstests bestanden. Die anschließende Synchronisierung von `REQ-TRACE-001` bestand erneut beide CI-Pfade (`33479807679` / Requirements `33479807761`).

Keine OPA-/CUE-/Workflow-Engine-Pflicht; zusätzliche Policy-Technik erst bei nachgewiesenem Bedarf.

## Dependency-getriebene Planung

Technische Reihenfolge wird nicht allein aus P0/P1 abgeleitet. #48 berücksichtigt mindestens:

- semantic prerequisite;
- data prerequisite;
- runtime prerequisite;
- verification prerequisite;
- integration prerequisite;
- risk prerequisite;
- enabler relationship.

Ein kleiner Enabler darf vor einem wissenschaftlich kritischeren Requirement geliefert werden, wenn dadurch dessen belastbare Umsetzung erst möglich wird. Die fachliche Kritikalität ändert sich dadurch nicht.

## Entscheidungsregel

### Reversible Entscheidungen

Darf #48 früh treffen und refactoren, sofern Requirements/Constraints eingehalten werden, z. B. Libraries, lokale Modulstruktur, UI/CLI-Schnitt, Test-/Build-Tooling und Adapterimplementierung. Auch diese Änderungen bleiben proportional auf Requirement/Driver/Governance rückführbar.

### Explizite ADR-/Owner-Entscheidung

Nur wenn materiell, z. B. schwer reversible Persistenz-/Datenmodellentscheidung, Provider-/Privacy-Lock-in, bedeutende Migration, Security-/Rights-Konsequenz oder wissenschaftlich unterschiedliche Loss-Risiken.

## Technische Grundregeln

- Goals/Needs/Pains bleiben upstream Produkt-/Research-Ursprung;
- akzeptierte Requirements führen die Systempflichten;
- Requirement Source, Domain Authority, Acceptance Authority und technische Umsetzung nicht vermischen;
- Fachmethode (#60) und technische Umsetzung bleiben getrennte Verantwortlichkeiten;
- keine Technologie als Requirement tarnen;
- aktueller SOTA / Best Practice / Existing Tools vor Eigenbau;
- deterministische Invarianten deterministisch, sobald fachlich/formal geklärt;
- neue materielle technische Änderungen nicht untracebar in kontrollierte Pfade einbringen;
- reale Nutzung/Owner-Feedback als eigener Rückkanal, nicht als wissenschaftliche Evidenz;
- Source/Instance/Derivative/Findspot nicht aus Convenience verschmelzen;
- Secrets/Credentials niemals im Repo;
- Provider-/Chat-Unabhängigkeit des kuratierten Research State;
- kleine fachlich korrekte Inkremente statt Infrastruktur auf Vorrat;
- keine KG/RAG/Multi-Agent/Workflow-/Policy-Plattform ohne konkreten Requirement-Trigger.

## Method Conformance

`assurance/method-conformance-work-context.md` bleibt Technical Research/Architecture Hypothesis. Formalisiert werden nur Method-/Evidence-/Handoff-Regeln, deren Semantik durch #42/#60 hinreichend geklärt ist.

## Fortschritt

```text
Goal / Need / Pain
+ accepted Requirement
+ nachvollziehbare technische Derivation
+ formale Requirements Assurance
+ Decision / Implementation Trace
+ belastbare Implementierung
+ passende Verification
+ reale Nutzung / Owner-Feedback
+ sichtbare Debt/Uncertainty
= technischer Fortschritt
```

> **Needs/Pains/Goals begründen das Warum. Requirements operationalisieren das Was. Architecture/Dev entscheidet das Wie. Reale Nutzung schließt die Schleife.**

> **Schema prüft Form; Validator prüft formale Invarianten; Fach-/Owner-Review prüft Bedeutung und Nutzen.**

> **Criticality ist nicht Delivery-Reihenfolge.**

> **Dev entscheidet reversible Technik früh, wissenschaftliche Bedeutung nie eigenmächtig.**
