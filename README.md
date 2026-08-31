# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk/Orla und für die Entwicklung einer **privaten, transdisziplinären historischen Forschungsassistenz**.

Ziel ist ein **früh nutzbares, dauerhaft belastbares Forschungswerkzeug**, das Quellenarbeit, fachliche Problemübersetzung, domänenspezifische Methoden, transdisziplinäre Analyse und einen nachvollziehbaren, restartbaren Forschungszustand unterstützt.

## Pflicht-Bootstrap / Handoff

Vor substantieller Arbeit:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. dieses `README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

## Produktmodus

Histo-Orla ist **privat, lean und agil**.

Owner-Entscheidung vom 31.08.2026:

- die im Domain-Research-/Methodenstrang formulierten **Systemanforderungen sind MVP-Akzeptanzkriterien**;
- Development startet jetzt inkrementell;
- fachlicher SOTA, technische SOTA/Best Practice, Requirements-Schärfung und Architekturentwicklung laufen parallel zum realen Einsatz;
- keine monatelange Vorab-Architektur als Voraussetzung für Nutzung;
- wissenschaftliche Schutzinvarianten bleiben hart.

Kanonisch:

- `docs/research/synthesis/mvp-acceptance.md`
- `docs/research/synthesis/phase-reconciliation.md`

## Aktuelle Phase

```text
Owner-accepted MVP Acceptance Criteria (#42)
        ↓
Walking Skeleton / Lean MVP Delivery (#48/#59)
        ↕
Live Research (#46/#47)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↕
Requirements-/Acceptance-Schärfung (#42)
        ↕
Just-in-time Technical SOTA / Architecture (#48/#58)
        ↓
kontinuierliche technische + wissenschaftliche Verification
```

**Architecture is a means, not a phase gate.**

## MVP

Der MVP ist das private System, das die owner-accepted Domain-Akzeptanzkriterien tatsächlich im Forschungsworkflow trägt.

Frühe nutzbare Inkremente sind ausdrücklich erwünscht. `MVP complete` wird erst behauptet, wenn die Kriterien aus `docs/research/synthesis/mvp-acceptance.md` für den privaten Scope erfüllt sind.

Erster Walking-Skeleton-Kandidat:

```text
Zotero / Source Metadata
→ OneDrive Source Bytes oder kontrollierte Testdatei
→ Source / inspected Instance / Findspot
→ Text/OCR soweit verfügbar
→ Exact + Variant Search
→ Excerpt / Observation
→ Finding / Historical Hypothesis / Research Hook
→ Method-/Evidence-Status
→ Audit / persistenter Research State / Handoff
```

## Aktive Owner

### Domain / Research

- **#46** – U2 Knau/Orlagau Live Research
- **#47** – U1 Teich-/Feuchtkulturlandschaft Live Research
- **#60** – Domain Method Profiles / fachwissenschaftliche Method Truth
- **#42** – accepted Requirements + MVP Acceptance Criteria

### Technical Lead / Delivery

- **#48** – Lean MVP Delivery / Technical Lead / evolutionary Architecture
- **#59** – aktive MVP-Implementierung und Verification
- **#58** – just-in-time Architecture Decisions / ADRs nur bei materiellen Entscheidungen

### Technische Teilpakete

- **#49** – Zotero ↔ OneDrive Integration
- **#50** – Canonical Research State / Source Identity
- **#51** – Document-/Findspot-Pipeline
- **#52** – OCR/HTR Benchmark / Integration
- **#53** – Historical Retrieval
- **#54** – Promotion / deterministische Invarianten
- **#55** – Human-readable Audit
- **#56** – Rights / Credentials / External Processing
- **#57** – Provider Removal / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff Technical Research; unterstützt Delivery, blockiert sie nicht pauschal

## Dev Authority Boundary

Dev darf reversible technische Entscheidungen früh treffen, bestehende Tools/Standards bevorzugen und refactoren.

Dev darf **nicht**:

- Fachsemantik oder Method Truth erfinden;
- owner-accepted Akzeptanzkriterien still abschwächen;
- AI zur Evidenz-/Truth-Instanz machen;
- wissenschaftliche Unsicherheit aus Convenience eliminieren;
- irreversible/teure/lock-in-relevante Entscheidungen ohne explizite Begründung treffen.

Leitregel:

> **Dev entscheidet reversible Technik früh, wissenschaftliche Bedeutung nie eigenmächtig.**

## Method Truth

#60 operationalisiert Fachmethoden SOTA-basiert. Das System muss auch unfertige Methodik ehrlich tragen können:

```text
method-candidate
→ Exploration möglich
→ consequential Promotion bleibt begrenzt
→ Profile wird im realen Case gehärtet
→ neue Version kann Review alter Findings auslösen
```

Method Truth ist kein Vorab-Blocker für das gesamte Development, sondern ein parallel wachsender fachlicher Bestandteil des MVP.

## Quellen-/Storage-Verantwortung

```text
OneDrive = Source of Bytes
Zotero   = bibliographische/archivische Verwaltung + Attachment-Referenzen
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht die wissenschaftliche Source-/Instance-Identität.

## Kanonische Einstiege

### Research / Requirements / MVP

- `docs/research/README.md`
- `docs/research/source-identity-protocol.md`
- `docs/research/methods/`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/mvp-acceptance.md`
- `docs/research/synthesis/phase-reconciliation.md`

### Technical Delivery

- `docs/architecture/README.md`
- `docs/architecture/contracts/canonical-research-state.md`
- `docs/architecture/assurance/method-conformance-work-context.md`

## Governing Principles

- **Privat, lean, agil: früh nutzbar werden, im realen Forschen härten.**
- Fachdomänen führen. Technologie dient.
- Domain-Anforderungen sind MVP-Akzeptanzkriterien.
- Method Truth kommt aus Fach-SOTA, nicht aus Prompt/Technik.
- Kein Wissensmonopol im Chat.
- Exploration offen; wissenschaftliche Promotion bleibt evidenz-/methodengebunden.
- vorhandene Tools/Standards vor Eigenbau;
- Provider-Unabhängigkeit des kuratierten Research State;
- Architecture ist Mittel zur Lieferung, kein Selbstzweck.

## Handoff-Test

Ein neuer kompetenter Bearbeiter muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat aktuelle Aufgabe, Authority, Acceptance Criteria, Methodenstatus, Evidenz, nächste erlaubte Aktion und Persistenzort rekonstruieren können.
