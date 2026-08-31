# Histo-Orla – Requirements Structure, Authority & Traceability

**Status:** `working contract / accepted structure direction`  
**Requirements Owner:** #42  
**Technical consumer:** #48/#59  
**Domain/Method inputs:** #46/#47/#60  
**Governance:** `AGENTS.md`, #9/#23/#45

## 1. Zweck

Dieses Artefakt definiert die **innere Struktur eines Histo-Orla-Requirements**. Es ersetzt weder die Requirements Baseline noch die accepted Extensions, sondern macht Herkunft, fachliche Autorität, Motivation, Scope, Abhängigkeiten, Kritikalität und Verifikation explizit genug, damit:

1. ein neuer Chat/Owner erkennt, **warum** ein Requirement existiert;
2. klar bleibt, **wer seine fachliche Bedeutung besitzt** und wer es nur implementiert;
3. Dependencies und Konflikte sichtbar werden;
4. technische/architektonische Ableitungen gezielt und ohne Solution Leakage erfolgen;
5. Priorisierung nicht mit wissenschaftlicher Kritikalität verwechselt wird;
6. jede Lösung auf Requirement und jede Verifikation zurück auf die Motivation tracebar bleibt.

Leitkette:

```text
Driver / Goal / Need / Pain / Risk / Constraint
→ konkrete Source / Evidence / Owner Decision
→ Domain Authority / Kompetenz
→ Capability / Quality / Scientific Invariant
→ Requirement
→ Scope + Dependencies + Criticality
→ Acceptance / Verification
→ abgeleitete Architecture Concerns / Technical Research Questions (#48)
→ Solution Candidates / Spike / ADR
→ Implementation (#59)
→ Verification
→ reale Nutzung / Delta zurück
```

`Requirement` und `technical solution` bleiben getrennte Zustände.

---

## 2. Warum die bisherige Struktur geschärft werden muss

Die Baseline v0.1 besitzt bereits viele gute Attribute:

- Type;
- Statement;
- Rationale;
- Owner;
- Capabilities;
- Use Cases;
- Acceptance;
- Risks;
- Evidence;
- Priority;
- teils Implementation freedom / Forbidden shortcut;
- Status.

Die vertieften Live-/Domain-Requirements zeigen jedoch drei Lücken:

1. **`Owner` ist überladen.** Fachliche Autorität, Requirements-Lifecycle-Owner, technische Umsetzung und Acceptance/Validation sind unterschiedliche Verantwortlichkeiten.
2. **Priorität ist überladen.** Wissenschaftliche Kritikalität, Architecture Significance und aktuelle Delivery-Reihenfolge sind nicht dasselbe.
3. **Downstream-Traceability fehlt als explizite Struktur.** Aus einem Requirement sollen Architecture Concerns und Technical Research Questions ableitbar sein, ohne Technologie in das Requirement hineinzuschreiben.

---

## 3. Referenzmuster / SOTA-Anker

Die Struktur orientiert sich lean an etablierten Requirements-Engineering-Mustern, ohne einen schweren Enterprise-Prozess zu übernehmen.

### ISO/IEC/IEEE 29148

Aktuell veröffentlichter Standard: ISO/IEC/IEEE 29148:2018; Edition 3 ist 2026 als DIS in Überarbeitung.

Referenzen:

- https://www.iso.org/standard/72089.html
- https://www.iso.org/standard/94091.html

Relevant für Histo-Orla: Requirements Engineering als interdisziplinäre Vermittlungsfunktion; Upstream-/Downstream-Traceability; strukturierte Requirement-Informationen und Verifikation/Validierung.

### IREB CPRE

IREB nennt als typische Requirement-Attribute u. a. Identification, Stakeholder Priority, Dependency, Risk, Source, Rationale, Difficulty und Type und empfiehlt, das konkrete Attributschema an die Informationsbedürfnisse des Projekts anzupassen.

Referenz: https://www.ireb.org/en/downloads

### SEBoK / INCOSE-Muster

SEBoK nennt u. a. rationale, trace to source/parent, verification success criteria, owner, category, status, criticality und priority als hilfreiche Requirement-Attribute.

Referenz: https://sebokwiki.org/wiki/System_Requirements

### Motivation / Architecture Views

ArchiMate trennt Motivationselemente wie Stakeholder, Driver, Goal, Requirement und Constraint von der Lösungsarchitektur. Histo-Orla übernimmt **das Denkprinzip**, nicht zwingend ArchiMate als Tool oder internes Format.

Referenz: https://www.opengroup.org/archimate

---

## 4. Requirement Record – Pflichtkern

Für neue oder materiell geänderte akzeptierte Requirements soll mindestens Folgendes rekonstruierbar sein.

### A. Identität / Lifecycle

```text
id
title
status
version / changed-by decision where material
```

`#42` bleibt der **kanonische Lifecycle-Owner** aller accepted Requirements.

### B. Role / Type

Ein Requirement kann mehrere Rollen haben. Zulässige Arbeitskategorien sind zunächst:

- `functional` – Systemverhalten/Fähigkeit;
- `information/data/provenance` – Informationsstruktur, Herkunft, Identität, Lebenszyklus;
- `quality` – messbare/prüfbare Qualität;
- `scientific/epistemic` – wissenschaftliche Aussage-/Methoden-/Evidenzgrenze;
- `invariant/guard` – formal zu schützende Regel;
- `integration/interface` – externe Grenze/Interoperabilität;
- `rights/policy/constraint` – harte externe oder normative Grenze;
- `human-control/ux` – menschliche Nachvollziehbarkeit/Kontrolle;
- `workflow/restartability` – Prozess-/Fortsetzungs-/Recovery-Verhalten.

Die Rolle beschreibt **welche Art Systempflicht** vorliegt, nicht welche Technologie sie umsetzt.

### C. Motivation / Driver

Mindestens:

```text
driver_type = goal | need | pain | risk | scientific_invariant | governance_constraint | rights_constraint | owner_constraint
motivation / rationale
```

Die Motivation beantwortet: **Welchen Verlust, Pain oder wissenschaftlichen Fehler verhindert bzw. welchen Nutzen ermöglicht das Requirement?**

### D. Origin / Source

`source` bedeutet hier die konkrete Herkunft des Requirements, nicht die technische Quelle im System.

Mindestens eine exakte Referenz auf z. B.:

- Goal/Need/Pain aus #28/#29;
- Capability/Quality aus #41;
- SOTA-Finding #31–#39;
- Live-Research-Finding/Pain #46/#47;
- Domain-Method-Finding #60;
- Governance #9/#45/AGENTS.md;
- Rights-/Legal-Finding #40/#56;
- explizite Owner-Entscheidung #44;
- technisches Feasibility-Finding, **wenn** es einen realen Requirement-Constraint offenlegt.

Technische Präferenz allein ist keine gültige Requirement Source.

### E. Authority / Kompetenzen

Die bisherige einzelne Eigenschaft `Owner` wird semantisch getrennt:

```text
canonical_requirement_owner = #42
originating_domain / originating_competence
domain_authority / controlling_competence
acceptance_authority
technical_delivery_owner
verification_authority
```

Bedeutung:

- **originating_domain/competence** – aus welcher Fach-/Arbeitskompetenz das Need/Finding stammt;
- **domain_authority** – wer die fachliche Bedeutung/Invariante korrigieren oder validieren darf;
- **acceptance_authority** – wer den Systembedarf für Histo-Orla akzeptiert; im privaten Projekt typischerweise Owner/#42, bei bindenden Rechten/Governance entsprechend constrained;
- **technical_delivery_owner** – #48/#59 bzw. Teilpaket, besitzt die Lösung, nicht die fachliche Semantik;
- **verification_authority** – wer/welches Verfahren einen Pass tatsächlich beurteilen darf: Softwaretest, Domain Review, Owner Acceptance, unabhängige Fachvalidierung etc.

Keine dieser Rollen darf still in eine andere übergehen.

### F. Scope / Applicability

Mindestens proportional zur Relevanz:

```text
applies_to = use cases / workflow stages / source types / domains / data classes
scope
exclusions / non-goals
trigger / condition, falls conditional
```

So wird z. B. eine Rights-Anforderung nicht unnötig auf Material angewandt, für das sie nicht greift, und eine quellentypspezifische Methode wird nicht universell gemacht.

### G. Dependencies / Relations

Minimaler kontrollierter Relationstyp:

- `derived_from` – fachlich/motivational abgeleitet aus;
- `requires` – logische/praktische Voraussetzung;
- `refines` – schärft ein allgemeineres Requirement;
- `constrains` – begrenzt die Lösungsfreiheit eines anderen Requirements/Clusters;
- `conflicts_with` – kann nicht gleichzeitig ohne Trade-off erfüllt werden;
- `supersedes` – ersetzt explizit;
- `related_to` – nur wenn keine stärkere Relation sauber belegbar ist.

Downstream-Beziehungen wie `realized_by` oder `verified_by` werden in Delivery-/Architecture-Views geführt, damit die Requirement Truth nicht mit Implementierungsdetails vermischt wird.

### H. Criticality / Architecture Significance / Delivery Priority

Diese drei Dinge werden getrennt.

#### `criticality`

Warum/mit welcher Konsequenz darf das Requirement nicht verletzt werden?

Arbeitswerte:

- `hard-constraint` – Rechte/Governance/wissenschaftliche Integrität oder nicht akzeptabler Datenverlust;
- `fundamental` – zentral für den Forschungsmodus/Systemkern;
- `important` – hoher fachlicher Nutzen/Qualität, aber kein Kernintegritätsbruch bei temporärem Fehlen;
- `enhancement` – nützlich, aber nicht für den aktuellen Systemanspruch fundamental.

#### `architecture_significance`

- `cross-cutting` – beeinflusst mehrere Komponenten/Entscheidungen;
- `bounded` – betrifft klar begrenzten Verantwortungsbereich;
- `local` – überwiegend lokale Implementierungsentscheidung;
- `unknown/research-needed`.

#### `delivery_priority`

**Keine stabile Requirement-Eigenschaft.** Sie wird unter #48/#59 dynamisch aus fachlichem Nutzen, Dependency, Risiko, Research-Pain, Reversibilität und Aufwand bestimmt.

Damit gilt:

> Ein fundamental Requirement muss nicht automatisch das erste Feature sein; ein niedriger bewerteter Enabler kann zuerst geliefert werden, wenn andere Requirements davon abhängen.

### I. Acceptance / Verification

Mindestens:

```text
acceptance / success criterion
failure / forbidden shortcut where important
verification_method
verification_fixture / real case / benchmark
```

Mögliche Verification Methods:

- deterministic unit/invariant test;
- integration/roundtrip test;
- benchmark/gold corpus;
- real-case acceptance;
- domain-method review;
- owner workflow acceptance;
- independent qualified specialist validation, wenn fachlich erforderlich;
- rights/security review.

`Acceptance` beschreibt das gewünschte beobachtbare Ergebnis, nicht die technische Umsetzung.

### J. Risks / Assumptions / Open Questions

Proportional:

```text
risks
assumptions
open_questions / research_needed
```

Ein offener technischer oder fachlicher Punkt darf sichtbar bleiben und muss nicht durch eine Scheinpräzision geschlossen werden.

---

## 5. Kompakter Requirement-Record

Für den normalen Fall soll ein Record lesbar bleiben:

```text
ID / Title
Role / Type
Statement
Motivation / Driver
Origin / Evidence
Domain Authority / Acceptance Authority
Scope / Exclusions
Dependencies
Criticality / Architecture Significance
Acceptance / Verification
Risks / Forbidden Shortcuts
Status
```

Nicht jedes Requirement benötigt in jedem Feld lange Prosa. Die Struktur dient der Traceability, nicht der Formularproduktion.

---

## 6. Downstream: Technical Derivation ist eine eigene Sicht

Aus einem accepted Requirement darf #48 systematisch technische Fragen ableiten, aber keine technische Wahl zurück in das Requirement schreiben.

```text
Requirement
→ impacted Capability / System Responsibility
→ Architecture Concern / Quality Attribute
→ Technical Research Question
→ Existing Tool / Standard / Pattern Candidates
→ Option / Hypothesis
→ Spike / Benchmark / Trade-off
→ ADR falls materiell
→ Implementation
→ Verification
```

Kanonischer technischer Vertrag dazu:

`docs/architecture/requirements-derivation.md`

---

## 7. Beispiel – REQ-SRC-004 Findspot-Roundtrip

### Requirement Truth

- **Role:** `information/data/provenance + quality + invariant/guard`;
- **Motivation:** Ein Finding ohne reproduzierbare Fundstelle ist wissenschaftlich nicht auditierbar;
- **Origin:** N-006/P-004, C1/C7, U4, #45;
- **Domain authority:** RDM + Quellenkunde/Diplomatik/Edition; IR controlling für Suchtreffer;
- **Canonical owner:** #42;
- **Scope:** alle evidenziellen Findings/Exzerpte/Suchtreffer, soweit die Quelle eine präzisere Fundstelle erlaubt;
- **requires:** REQ-SRC-001/002; für OCR-Quellen zusätzlich REQ-OCR-001/002;
- **criticality:** `hard-constraint/fundamental`;
- **architecture significance:** `cross-cutting`;
- **Acceptance:** Source/Instance → Derivative → Hit/Excerpt → Citation roundtrip führt auf dieselbe korrekte Seite/Folio/Regest-/Archivfundstelle zurück.

### Abgeleitete technische Fragen – nicht Teil der Requirement Truth

- Wie werden stabile Findspot-Referenzen modelliert, wenn Dateien/OCR-Versionen wechseln?
- Brauchen wir Page-/Region-Identifier oder reicht zunächst Seiten-/Folio-Mapping?
- Welche bestehenden Standards/Modelle sind passend: PAGE/ALTO/METS, IIIF/Web Annotation, TEI-Stand-off etc. – abhängig vom konkreten Material?
- Wie testen wir Roundtrip und Migration deterministisch?

Erst #48/#51/#52 vergleichen die kleinste passende Lösung.

---

## 8. Beispiel – REQ-MTH-003 Method Status / Application

### Requirement Truth

- **Role:** `scientific/epistemic + provenance + workflow`;
- **Motivation:** Ein Finding darf nicht so aussehen, als sei eine Fachmethode angewandt/validiert worden, wenn nur ein Prompt oder Method Candidate existierte;
- **Origin:** #60 Live-Domain-Method-Lücke;
- **Domain authority:** jeweilige Fachdomäne + Research Integrity;
- **Canonical owner:** #42;
- **Scope:** consequential Method Applications/Findings, sobald ein Domain Method Profile operationalisiert ist;
- **requires:** REQ-MTH-001/002; REQ-EPI-001; REQ-VAL-001;
- **criticality:** `fundamental`;
- **architecture significance:** `cross-cutting`;
- **Acceptance:** Profilversion/-status und konkrete Anwendung sind nachvollziehbar; `method-candidate` kann nicht still als `validated-method` erscheinen.

### Abgeleitete technische Fragen

- Wie versionieren/referenzieren wir Method Profiles und Applications lean?
- Muss eine Profiländerung automatisch `review-needed` für abhängige Findings markieren?
- Welche Übergänge sind formal genug für Validatoren und welche bleiben Domain Review?
- Wie wird die History auditierbar ohne Event-Sourcing-Plattform?

---

## 9. Einführung / Migration

Keine Big-Bang-Umschreibung aller bestehenden Requirements.

Vorgehen:

1. dieses Strukturmodell gilt für neue und materiell geänderte Requirements;
2. bestehende 39 Baseline-Requirements + 13 Extensions werden **clusterweise** nachgezogen, wenn #42/#48 sie für technische Ableitung oder Verification aktiv bearbeitet;
3. zuerst P0/cross-cutting Cluster: Source/Provenance, State/Restartability, Method/Research, Audit/Validation, Retrieval;
4. bestehende `Priority: P0/P1/P2` bleibt historische Provenienz, wird aber nicht mehr allein als Delivery-Reihenfolge interpretiert;
5. `docs/development/requirements-coverage.md` bleibt Delivery-/Verification-Sicht und erhält später nur die für Delivery nötigen abgeleiteten Felder/Links;
6. keine neue Requirements-Datenbank oder Spezialsoftware, solange Markdown + kleine strukturierte Projektion ausreichen.

---

## 10. Leitregeln

> **Source sagt, woher ein Requirement kommt. Domain Authority sagt, wer seine fachliche Bedeutung besitzt. #42 besitzt seinen Lifecycle. #48 besitzt die technische Ableitung. #59 implementiert und verifiziert.**

> **Criticality ist nicht Delivery-Reihenfolge.**

> **Requirement beschreibt das notwendige Ergebnis und seine Grenzen; Architektur beschreibt die Mittel.**

> **Traceability läuft in beide Richtungen: von Motivation/Evidenz zum Requirement und vom Requirement zu Entscheidung, Implementierung und Test.**
