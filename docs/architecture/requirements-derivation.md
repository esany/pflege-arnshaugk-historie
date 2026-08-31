# Histo-Orla – Requirements → Architecture / Technology Derivation

**Status:** `working architecture contract / lean derivation view`  
**Technical Lead:** #48  
**Requirements Owner:** #42  
**Development / Verification:** #59  
**Input structure:** `docs/research/synthesis/requirements-structure.md`

## 1. Zweck

Dieses Artefakt definiert, **wie accepted Requirements technisch untersucht werden**, ohne die Requirements selbst mit Architektur oder Technologie zu vermischen.

#48 besitzt die technische Ableitung. #42 besitzt weiterhin die Requirement Truth; #60 besitzt fachwissenschaftliche Method Truth.

Leitfluss:

```text
accepted Requirement / Requirement Cluster
→ System Responsibility / Capability
→ Architecture Concern / Quality Attribute
→ Technical Research Question
→ Existing Tools / Standards / Patterns
→ Candidate Approach
→ Dependency / Risk / Reversibility
→ Spike / Benchmark / Trade-off, falls nötig
→ Decision / ADR, falls materiell
→ Implementation #59
→ Verification
→ reale Nutzung / Delta
```

---

## 2. Warum eine eigene Derivation View nötig ist

Ein Requirement wie

> „Findspots müssen verlustfrei rückführbar bleiben“

sagt noch nicht, ob intern Dateien, SQL, Annotation-IDs, PAGE/ALTO/METS, IIIF, Web Annotation oder eine eigene kleine Referenzstruktur benötigt werden.

Eine direkte Kette

```text
Requirement → bevorzugte Technologie
```

würde Solution Bias erzeugen.

Die technische Arbeit braucht deshalb eine Zwischenschicht aus **Concerns und Research Questions**.

---

## 3. Derivation Card – Pflichtkern für materielle technische Ableitungen

### A. Input

```text
requirements
requirement roles/types
criticality
architecture significance
scope
upstream dependencies
acceptance / verification target
forbidden losses / constraints
```

### B. System Responsibility / Capability

Welche technische Verantwortung muss existieren, unabhängig von der konkreten Technologie?

Beispiele:

- canonical state persistence;
- source/instance resolution;
- findspot mapping;
- exact retrieval;
- audit rendering;
- rights admission;
- method-application provenance;
- export/restartability.

### C. Architecture Concerns

Welche Eigenschaften muss eine Lösung schützen?

Typische Concerns in Histo-Orla:

- scientific integrity / epistemic non-loss;
- data/provenance integrity;
- portability / replaceability;
- auditability / human readability;
- deterministic enforcement;
- restartability / recoverability;
- interoperability;
- search correctness / recall / traceability;
- rights/privacy/security;
- maintainability / simplicity;
- performance erst bei beobachtetem Bedarf.

### D. Quality / Failure Scenario

Für architecture-significant Requirements soll ein konkretes Szenario formuliert werden, wenn das die Entscheidung verbessert:

```text
context / environment
trigger / stimulus
betroffenes Objekt / responsibility
expected response
measurable/pass condition
failure/loss if violated
```

Das übernimmt das bewährte Quality-Attribute-Scenario-Prinzip in einer kleinen, projektspezifischen Form. Kein vollständiger ATAM-Prozess ist vorgeschrieben.

### E. Technical Research Questions

Fragen statt voreiliger Lösungen, z. B.:

- Welche vorhandenen Tools lösen diesen Teil bereits ausreichend?
- Welche Daten/IDs müssen dauerhaft stabil sein?
- Welche Operationen müssen transaktional/atomar sein?
- Welche Teile sind regenerierbar?
- Welche Schnittstellen müssen austauschbar sein?
- Welche Performance-/Corpusgröße ist real beobachtet?
- Welche Rights-/Privacy-Grenzen verändern Local-vs-Cloud?
- Welche Failure Modes sind wissenschaftlich folgenreich?
- Was muss offline/restartbar funktionieren?
- Welche formalen Invarianten sind deterministisch prüfbar?

### F. Candidate Approaches

Kandidaten erhalten explizit den Status `solution-hypothesis`, nicht Requirement.

Pro Kandidat mindestens:

```text
approach
requirements covered
benefit
complexity
scientific/technical loss risk
lock-in / reversibility
existing tool / standard leverage
unknowns
verification / spike needed
```

### G. Decision Class

- `implement-reversible` – geringe Folgekosten, Requirement klar, leicht refactorbar;
- `spike/benchmark` – materielles Unknown lässt sich klein diskriminieren;
- `ADR` – mehrere tragfähige Optionen mit relevantem Trade-off;
- `#44 owner decision` – normative, teure, irreversible, rights-/scope-relevante Entscheidung.

---

## 4. Dependency-Arten für technische Planung

Technische Reihenfolge wird nicht aus `P0/P1` allein abgeleitet.

Mindestens berücksichtigen:

1. **semantic prerequisite** – fachliche Bedeutung eines abhängigen Requirements braucht zuerst Klarheit;
2. **data prerequisite** – benötigter State/Identity muss vorher verfügbar sein;
3. **runtime prerequisite** – technische Fähigkeit benötigt eine andere zur Ausführung;
4. **verification prerequisite** – Test/Benchmark braucht Fixture/Corpus/Instrumentation;
5. **integration prerequisite** – externer Zugriff/Auth/Dateiavailability;
6. **risk prerequisite** – gefährliche Entscheidung braucht vorher Spike/ADR;
7. **enabler** – kleine Fähigkeit erschließt mehrere andere Requirements.

#48 darf dadurch ein Requirement früher implementieren, das fachlich weniger kritisch ist, wenn es ein echter Enabler ist. Die fachliche Kritikalität bleibt unverändert.

---

## 5. Funktions- vs. Architektur- vs. Technologieableitung

Diese Ebenen bleiben getrennt:

### Functional / System Responsibility

> Was muss das System tun oder tragen?

Beispiel:

`Source/Instance/Findspot persistent referenzieren und wiederauflösen.`

### Architecture Concern / Concept

> Welche Verantwortungsgrenzen und Qualitätsmechanismen sind nötig?

Beispiel:

`stabile interne Identität`, `Provider-Adapter`, `kuratierter vs. regenerierbarer State`, `Roundtrip-Test`.

### Technology Candidate

> Mit welchen konkreten Mitteln könnte das erreicht werden?

Beispielkandidaten:

`Markdown/YAML`, `SQLite`, `PostgreSQL`, `FTS`, `Lucene`, `Zotero API`, `Microsoft Graph`, `IIIF`, `W3C PROV`, `RO-Crate`, `PAGE/ALTO/METS`, etc.

Technologie wird erst hier diskutiert und bleibt Kandidat bis zur Entscheidung.

---

## 6. SOTA-/Best-Practice-Referenzmuster

### Requirements / Traceability

- ISO/IEC/IEEE 29148: Requirements lifecycle and traceability;
- IREB CPRE: attribute schema, source/rationale/dependency/risk/priority;
- ReqIF 1.2 als möglicher **Interchange-Standard**, falls später Tool-Austausch echten Nutzen hat; nicht als interner Pflichtspeicher.

### Motivation / Architecture Trace

ArchiMate-Motivationselemente (`Stakeholder`, `Driver`, `Goal`, `Requirement`, `Constraint`) sind ein nützliches Referenzvokabular für Why→What-Traceability. Kein ArchiMate-Tool ist dadurch vorgegeben.

### Quality Architecture

SEI QAW/ATAM-Pattern: konkrete Quality Scenarios und Trade-offs sind nützlich für architecture-significant Requirements. Histo-Orla verwendet davon nur die kleinste hilfreiche Form, kein Enterprise-Gate.

### Research State / Provenance

Je konkretem Requirement zu prüfen, nicht pauschal zu adoptieren:

- W3C PROV;
- RO-Crate / Run Crate;
- fach-/quellengattungsspezifische Standards wie TEI/PAGE/ALTO/METS/IIIF/Web Annotation.

### Architekturprinzip

Bestehende Werkzeuge/Standards werden gegen Requirement + Loss-/Complexity-Kriterien geprüft. Standardkonformität ist kein Selbstzweck.

---

## 7. Erste Requirement-Cluster für technische Ableitung

### Cluster A – Source / Instance / Findspot / Derivative

Requirements u. a.:

- REQ-SRC-001/002/003/004;
- REQ-OCR-001/002;
- REQ-INT-002.

Zu untersuchen:

- interne Identitäten vs. Zotero/OneDrive IDs;
- stabile File-/Instance-Fingerprints;
- Findspot-/Page-/Region-Mapping;
- parent/derivative graph;
- Roundtrip/Migration;
- geeignete Standards je Material;
- read-first Adaptergrenzen.

### Cluster B – Canonical State / Restartability / Audit

- REQ-STATE-001/002/003;
- REQ-WF-002;
- REQ-UX-001/003;
- REQ-INT-001.

Zu untersuchen:

- kleinster portable canonical store;
- human-readable + transactional Anforderungen;
- export/restore/provider-removal;
- research-ready Availability;
- Audit Views aus demselben State;
- Backup/Migration/Schema evolution.

### Cluster C – Method / Evidence / Promotion

- REQ-EPI-001/004/005/006;
- REQ-MTH-001–005;
- REQ-VAL-001/002;
- REQ-WF-001;
- REQ-RSCH-001–004.

Zu untersuchen:

- Method Profile/Application versioning;
- Evidence/Observation/Finding/Hypothesis state boundaries;
- welche Promotion Guards formalisiert werden dürfen;
- History/Demotion/Review-needed;
- Work Context/Handoff minimaler State;
- keine Workflow Engine ohne realen Bedarf.

### Cluster D – Retrieval

- REQ-RET-001–005;
- REQ-EPI-002/003;
- REQ-RSCH-002.

Zu untersuchen:

- exakte Suche / FTS / BM25 baseline;
- historische Varianten/fuzzy/linguistische Methoden;
- Query-/Corpus-Provenienz;
- Search Boundaries;
- Semantic/RAG nur benchmark-admitted;
- Gold Queries aus #46/#47.

### Cluster E – Rights / External Services

- REQ-RGT-001/002;
- REQ-INT-001/002;
- REQ-STATE-003.

Zu untersuchen:

- lokale vs. externe Verarbeitung;
- Credentials/Secrets;
- source/purpose/service-spezifische Admission;
- OneDrive/Zotero/API-Rechte;
- cloud-only file availability;
- Audit der externen Verarbeitung ohne Secrets zu persistieren.

---

## 8. Output von #48

Für ein aktiv bearbeitetes Requirement/Cluster soll #48 am Ende nicht einfach eine Technologie nennen, sondern mindestens liefern:

```text
Requirements / Scope
→ Architecture Concerns
→ relevante Dependencies
→ Technical Research Questions
→ geprüfte Existing Tools / Standards / Patterns
→ Candidate Approaches
→ Trade-offs / Loss / Reversibility
→ Entscheidungsklasse
→ gewählte nächste Aktion
→ Verification Target
```

Das Ergebnis wird in #48/#58 bzw. dem zuständigen technischen Work Package persistiert.

---

## 9. Leitregeln

> **Requirements erklären das Warum und Was. Technical Derivation klärt die Designfragen. ADRs entscheiden konkrete Mittel.**

> **Keine Technologie direkt aus einem Buzzword; keine Fachanforderung durch technische Convenience.**

> **Priorisierung folgt Nutzen + Dependencies + Risiko + Reversibilität – nicht einem einzigen P0/P1-Feld.**
