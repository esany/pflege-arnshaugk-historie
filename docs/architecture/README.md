# Histo-Orla – Technical Delivery / Evolutionary Architecture Index

**Technical Lead / Delivery Owner:** #48  
**MVP Development:** #59  
**Requirements / Acceptance:** #42  
**Project Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Zweck

Dieses Verzeichnis enthält technische Delivery-, Architecture-, Assurance- und Entscheidungsartefakte für ein **privates, leanes und agiles Forschungssystem**.

Architecture ist kein separates Vorab-Gate. Sie entsteht **just in time** aus realen MVP-Akzeptanzkriterien, technischen Risiken und laufender Nutzung.

Kanonische MVP-Akzeptanz:

`../research/synthesis/mvp-acceptance.md`

## Leitpfad

```text
Acceptance Criterion / realer Pain
→ kleinste nutzbare technische Option
→ vorhandene Tools/Standards prüfen
→ bei materiellem Risiko kurzer Spike/Benchmark
→ implementieren
→ realen Case testen
→ behalten | anpassen | ersetzen
```

## Aktive Work Owner

### Delivery / Technical Lead

- **#48** – Lean MVP Delivery, Technical Lead, evolutionäre Architektur
- **#59** – aktive MVP-Implementierung und Verification

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

### Architecture Decisions

- **#58** – just-in-time Architecture Decision / ADR Support; kein globales Blocking-Gate

### Fachliche Upstream-Schnittstelle

- **#60** – Domain Method Profiles / Method Truth
- **#42** – accepted Requirements / MVP Acceptance Criteria

## Walking Skeleton

Erster nutzbarer Slice-Kandidat:

```text
Zotero / Source Metadata
→ OneDrive Source Bytes oder kontrollierte Testdatei
→ Source / inspected Instance / Findspot
→ Text/OCR soweit verfügbar
→ Exact + Variant Search
→ Excerpt / Observation
→ Finding / Historical Hypothesis / Research Hook
→ Method-/Evidence-Status
→ Audit / Persistenz / Handoff
```

Der Slice darf inkrementell entstehen. Jeder Teil soll so früh wie möglich real nutzbar sein.

## Entscheidungsregel

### Reversible Entscheidungen

Darf #48 früh treffen und bei Bedarf refactoren, sofern Acceptance/Constraints eingehalten werden, z. B.:

- Library-/Framework-Auswahl ohne schweren Lock-in;
- lokale Modulstruktur;
- UI-/CLI-Prototyp;
- Test-/Build-Tooling;
- Adapterimplementierung.

### Explizite ADR-/Owner-Entscheidung

Nur wenn materiell, z. B.:

- schwer reversible Persistenz-/Datenmodellentscheidung;
- Cloud-/Provider-/Kosten-/Privacy-Lock-in;
- bedeutende Migration;
- Security-/Rights-Konsequenz;
- zwei Optionen mit verschiedenen wissenschaftlichen Verlust-/Integritätsfolgen.

## Technische Grundregeln

- Domain-Akzeptanzkriterien führen;
- Fachmethode (#60) und technische Umsetzung bleiben getrennte Verantwortlichkeiten;
- keine Technologie als Requirement tarnen;
- vorhandene Tools/Standards vor Eigenbau;
- deterministische Invarianten deterministisch, sobald formal geklärt;
- fail closed on wissenschaftlicher Promotion, nicht auf offene Exploration;
- Source/Instance/Derivative/Findspot nicht aus Convenience verschmelzen;
- read-first bei externen Integrationen;
- Secrets/Credentials niemals im Repo;
- Provider muss entfernbar bleiben, soweit Research-State-Integrität betroffen ist;
- kleine vertikale Produktinkremente vor isolierten Architekturstudien;
- keine KG/RAG/Multi-Agent/Workflow-/Policy-Plattform ohne konkreten Trigger.

## Method Conformance

`assurance/method-conformance-work-context.md` bleibt Technical Research/Architecture Hypothesis.

Es darf den MVP parallel härten, blockiert Development aber nicht pauschal. Formalisiert werden nur Method-/Evidence-/Handoff-Regeln, deren Semantik durch #42/#60 ausreichend geklärt ist.

## Delivery-Fortschritt

```text
nutzbarer Slice
+ bestandene Acceptance-/Regression-/Invariant-Tests
+ sichtbare Debt/Uncertainty
= realer Fortschritt
```

Nicht nötig ist ein monatelanger Vorab-Architekturabschluss.

## Leitformeln

> **Architecture is a means, not a phase gate.**

> **Dev entscheidet reversible Technik früh, wissenschaftliche Bedeutung nie eigenmächtig.**

> **Früh nutzbar, fachlich ehrlich, technisch austauschbar.**
