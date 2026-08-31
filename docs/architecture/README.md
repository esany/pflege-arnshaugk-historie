# Histo-Orla – Technical Delivery / Evolutionary Architecture Index

**Technical Lead:** #48  
**Development / Verification:** #59  
**Requirements:** #42  
**Project Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Zweck

Dieses Verzeichnis enthält technische Research-, Delivery-, Architecture-, Assurance- und Entscheidungsartefakte für das private Histo-Orla-Forschungssystem.

Architecture ist kein separates Vorab-Gate. Sie entsteht just in time aus **akzeptierten Requirements, technischen Risiken und realer Nutzung**.

Kanonische Requirements:

- `../research/synthesis/requirements-baseline.md`
- `../research/synthesis/requirements-extensions.md`

Delivery-/Verification-Coverage:

- `../development/requirements-coverage.md`

## Leitpfad

```text
accepted Requirement / realer Pain
→ technische SOTA / Best Practice / Existing Tools
→ kleinste hinreichende Option
→ bei materiellem Unknown Spike/Benchmark
→ implementieren
→ fachlich + technisch testen
→ realen Case nutzen
→ behalten | anpassen | ersetzen
```

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

### Architecture Decisions

- **#58** – just-in-time ADR Support bei materiellen/schwer reversiblen Entscheidungen

### Fachliche Upstream-Schnittstelle

- **#60** – Domain Method Profiles / Method Truth
- **#42** – accepted Requirements
- **#46/#47** – reale Research-/Problem-/Verification-Fälle

## Entscheidungsregel

### Reversible Entscheidungen

Darf #48 früh treffen und refactoren, sofern Requirements/Constraints eingehalten werden, z. B. Libraries, lokale Modulstruktur, UI/CLI-Schnitt, Test-/Build-Tooling und Adapterimplementierung.

### Explizite ADR-/Owner-Entscheidung

Nur wenn materiell, z. B. schwer reversible Persistenz-/Datenmodellentscheidung, Provider-/Privacy-Lock-in, bedeutende Migration, Security-/Rights-Konsequenz oder wissenschaftlich unterschiedliche Loss-Risiken.

## Technische Grundregeln

- akzeptierte Requirements führen;
- Fachmethode (#60) und technische Umsetzung bleiben getrennte Verantwortlichkeiten;
- keine Technologie als Requirement tarnen;
- aktueller SOTA / Best Practice / Existing Tools vor Eigenbau;
- deterministische Invarianten deterministisch, sobald fachlich/formal geklärt;
- Source/Instance/Derivative/Findspot nicht aus Convenience verschmelzen;
- Secrets/Credentials niemals im Repo;
- Provider-/Chat-Unabhängigkeit des kuratierten Research State;
- kleine fachlich korrekte Inkremente statt Infrastruktur auf Vorrat;
- keine KG/RAG/Multi-Agent/Workflow-/Policy-Plattform ohne konkreten Requirement-Trigger.

## Method Conformance

`assurance/method-conformance-work-context.md` bleibt Technical Research/Architecture Hypothesis. Formalisiert werden nur Method-/Evidence-/Handoff-Regeln, deren Semantik durch #42/#60 hinreichend geklärt ist.

## Fortschritt

```text
Requirement
+ belastbare Implementierung
+ passende Verification
+ sichtbare Debt/Uncertainty
= technischer Fortschritt
```

> **Requirements führen den Umfang. Lean/Agile optimiert die Mittel.**

> **Dev entscheidet reversible Technik früh, wissenschaftliche Bedeutung nie eigenmächtig.**
