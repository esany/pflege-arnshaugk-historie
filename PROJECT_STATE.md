# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1 Gesamtstand; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Sie ersetzt weder Requirements, Research-Artefakte noch Architecture Contracts, sondern verweist auf deren kanonische Orte.

## 1. Aktuelle Phase

Die Discovery-/SOTA-/Requirements-Kette #28–#43 ist abgeschlossen.

Architecture Gate #43:

**`architecture-ready-with-bounded-research-debt`**

Aktuelle Hauptphase:

```text
Requirements
→ Architecture Contracts / Invariants
→ reversible Integrations-/Technik-Spikes
→ Thin Vertical Slice
→ Architekturvarianten + Trade-offs
→ ADRs
→ MVP-Schnitt
→ Development / Verification
```

Architecture Execution Owner: **#48**.

## 2. Abgeschlossene Baselines / Gates

- #28 Problem-/Need-/Pain-Baseline – completed
- #29 Workflows U1–U4 – completed
- #30 Research Question Portfolio – completed
- #31–#39 SOTA C1–C9 – completed
- #40 Risk / Constraint / Rights – completed
- #41 Capability Map + Quality Catalogue – completed
- #42 Requirements Baseline v0.1 – completed
- #43 Architecture Readiness – completed
- #27 frühere Execution Control bis Gate – completed

Kanonische Artefakte:

- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/risks-constraints.md`
- `docs/research/synthesis/capability-map.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md`

## 3. Aktive Work Owner

### Laufende historische Forschung / Falsifikation

- **#46** – U2 Knau/Orlagau, `in-research / working-research`
- **#47** – U1 Orlagau Teich-/Feuchtkulturlandschaft, `in-research / working-research`

Diese Cases sind **nicht abgeschlossen**. Sie dürfen neue Requirement-/Architecture-Candidates erzeugen. Sie blockieren die Architektur nicht pauschal, können aber eine architecture-driving Invariante falsifizieren und damit gezieltes Reopening auslösen.

### Architektur / Integration

- **#48** – Architecture Execution Control
- **#49** – Zotero ↔ OneDrive ↔ Histo-Orla Integration Spike, read-first
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten

Kanonischer Contract #50:

`docs/architecture/contracts/canonical-research-state.md`

## 4. Aktuelle cross-cutting Owner Constraints

### Source / Storage Responsibility

```text
OneDrive
= Source of Bytes / primärer physischer Speicher der Quellen-/Literaturdateien

Zotero
= bibliographische/archivische Verwaltung, Collections, Tags, Notes, Attachment-Referenz

Histo-Orla
= wissenschaftlicher Research State: Evidenz, Findings, Claims, Discrepancies,
  Validation, Provenienz-/Findspot-Bezug
```

Keine dieser externen Schichten ist alleiniger kanonischer Research-State-Owner.

### Source Identity

Bindendes Forschungsprotokoll:

`docs/research/source-identity-protocol.md`

Grundtrennung:

```text
Source / Überlieferung
→ Representation / Edition / Katalog / Reproduktion
→ konkrete inspizierte Instanz
→ Derivative / OCR / HTR / Transkription
→ Findspot / Excerpt / Observation
→ Finding
→ Claim / Interpretation / Synthesis
```

### Chat / Handoff

`AGENTS.md` ist bindender Repo-Vertrag.

Kein continuation-critical State darf ausschließlich in Chat/Modellzustand verbleiben.

## 5. Aktuelle Blocker / Decisions

**#44 enthält derzeit keinen Gate-blockierenden Owner-/Rights-/External-Validation-Fall.**

Normale offene Forschung, reversible Architekturfragen und technische Experimente sind keine #44-Blocker.

## 6. Aktueller kritischer Architekturpfad

```text
#50 Canonical State / Identity Contract
        ↓
#49 Zotero/OneDrive Source Resolver
        ↓
Document / Findspot Pipeline
        ↓
OCR/HTR + Historical Retrieval
        ↓
Candidate→Review→Promotion + Audit
        ↓
Rights / Provider Removal / Restartability
        ↓
Architecture Variants / ADRs / MVP Cut
```

Parallel möglich:

- read-only Zotero/API-Probing;
- synthetische Invariant-/Promotion-Tests;
- Rights-Admission-Contract;
- OCR/HTR Benchmark-Harness auf isoliertem Testmaterial;
- Audit-View-Contract;
- Live Research #46/#47.

## 7. Research-Design-Dokument: Status

`docs/research-design/transdisziplinaerer-literaturassistent.md` bleibt ein **foundational design document** mit weiterhin gültigen Governing Principles und fachlichem Zielbild.

Es ist **nicht mehr der alleinige aktuelle Operations-/Requirements-/Architecture-State**, weil seine letzte grundlegende Konsolidierung vor Abschluss von #28–#43 liegt.

Für aktuelle Detailfragen gilt:

```text
Research Design Principles
→ aktuelle Research/SOTA-Artefakte
→ #42 Requirements
→ #43 Gate
→ #48ff Architecture Contracts / Spikes / ADRs
```

Siehe `docs/research-design/README.md`.

## 8. Technischer Entwicklungsstand

Bis #43 war technische Implementierung bewusst nachgeordnet; deshalb enthält das Repository bislang wenig Anwendungscode.

Das ist **für die abgeschlossene Research-/Requirements-Phase erklärbar**, darf ab der aktuellen Architekturphase aber nicht zu einem dauerhaften Delivery-Defizit werden.

Technische Arbeit wird ab jetzt als eigenständige testbare Work Packages geführt. Der aktuelle technische Kern ist noch **Architecture/Spike**, nicht produktiver MVP-Code.

Vor Implementierung sind insbesondere zu bearbeiten:

1. Canonical State / Identity Contract (#50)
2. Zotero/OneDrive Integration (#49)
3. Document/Findspot Pipeline
4. OCR/HTR Benchmark & Processor Boundary
5. Historical Retrieval Baseline
6. Candidate/Promotion & deterministic invariant enforcement
7. Research Audit View
8. Rights Admission / Credential Boundary
9. Provider Removal / Export / Restartability
10. Architecture Variants + ADR + MVP Cut

Die eigenständigen technischen Work Owner werden unter #48 geführt.

## 9. Nächste ausführbare Aktionen

Case-unabhängig zuerst:

1. #50 Contract gegen #42/#45 reviewen und synthetische Invariant-Tests spezifizieren.
2. #49 read-only Zotero/OneDrive Mapping und Identifier-/Locator-Grenzen prüfen.
3. technische Work Packages aus #43/#48 als eigenständige Issues mit DoD sichtbar machen.
4. Architecture-/Development-Index im Repo führen.

Danach bzw. parallel:

5. U1/U2/U4 als reale Falsifikation für Source/Instance/Findspot/OCR/Retrieval verwenden.
6. 2–3 Architekturvarianten vergleichend bewerten.
7. ADRs und kleinsten hinreichenden MVP-Schnitt ableiten.
8. erst dann produktiven Implementationspfad festziehen.

## 10. Handoff-Test

Ein neuer Chat/Bearbeiter soll nach Lesen von:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. zuständigem Work-Owner-Issue + dessen Artefakt

ohne vorherige Chat-Historie produktiv fortsetzen können.

Wenn dies nach einer materiellen Änderung nicht mehr stimmt, muss dieser State vor Abschluss der Arbeit nachgezogen werden.