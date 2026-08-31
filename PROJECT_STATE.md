# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Kanonische Detailwahrheit liegt in Requirements-, Research-, Method-, Architecture- und Development-Artefakten.

## 1. Aktuelle Phase

Owner-Entscheidung 31.08.2026:

> **Histo-Orla ist ein privates, leanes und agiles Forschungssystem. Die im Domain-Research-/Methodenstrang formulierten Systemanforderungen sind MVP-Akzeptanzkriterien. Das MVP wird jetzt inkrementell gebaut und im realen Forschungsgebrauch gehärtet.**

Kanonisch:

- `docs/research/synthesis/mvp-acceptance.md`
- `docs/research/synthesis/phase-reconciliation.md`
- #44 DD-001 (resolved owner decision)

Aktueller Arbeitsfluss:

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

**Architecture ist kein separates Vorab-Gate mehr, sondern evolutionäre Delivery-Arbeit.**

## 2. Baselines und aktuelle Präzedenz

Der erste Durchlauf #28–#43 bleibt als v0.1 Discovery-/SOTA-/Requirements-/Readiness-Provenienz erhalten.

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Questions – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risks/Constraints – completed
- #41 Capability/Quality – completed
- #42 Requirements Baseline v0.1 – accepted baseline + aktive MVP-Acceptance-Schärfung
- #43 früheres Gate – durch Owner-Entscheidung in **continuous/evolutionary readiness** überführt

Neue Domain-/Case-Befunde dürfen Requirements/Acceptance weiter schärfen, blockieren aber Development nicht pauschal.

## 3. Aktive fachliche Work Owner

### #46 – U2 Knau/Orlagau

`in-research / working-research`

Aktuelle Leitfrage:

> **Wie verändern sich soziale, kirchliche, dynastische, grundherrliche und administrative Organisation des Orla-Grenzraums zwischen ca. 1200 und 1400, welche älteren Rechte und Netzwerke überleben diese Veränderungen, und wie werden Boden, Wege, Kirchen, Abgaben, Wasser und Menschen in diesen Strukturen verfügbar gemacht oder geschützt?**

Kanonische Case-Artefakte unter `docs/research/cases/`.

### #47 – U1 Teich-/Feuchtkulturlandschaft

`in-research / working-research`

### #60 – Domain Method Profiles

`in-research / cross-cutting-method-work-package`

Besitzt **Method Truth**, nicht Systemarchitektur.

Erste Priorität:

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. weitere Profile problemgetrieben aus #46/#47.

Method Profiles dürfen als `method-candidate` bereits explorativ verwendet werden. Fehlende Reife muss sichtbar bleiben und darf keinen höheren epistemischen Status vortäuschen.

## 4. Requirements / MVP Acceptance

### #42

Einziger Owner akzeptierter Systemanforderungen und MVP-Akzeptanzkriterien.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/mvp-acceptance.md`

Owner-Regel:

> **Alle Systemanforderungen aus dem Domain-Research-/Methodenstrang gelten für den privaten Scope als MVP-Akzeptanzkriterien.**

Sie werden inkrementell implementiert und getestet. Method Truth selbst bleibt trotzdem #60-Eigentum und darf technisch nicht erfunden werden.

## 5. Technical Lead / Delivery

### #48 – Lean MVP Delivery / Technical Lead

Auftrag:

- technischen Backlog nach Nutzerwert, Risiko, Dependency und kleinster nutzbarer Lieferung priorisieren;
- SOTA/Best Practice **just in time** für konkrete Entscheidungen prüfen;
- vorhandene Tools/Standards vor Eigenbau;
- reversible technische Entscheidungen früh treffen und refactorbar halten;
- Integrationen/Spikes direkt in nutzbare Slices überführen;
- evolutionäre Architektur;
- Acceptance/Regression/Invariant Tests laufend ausbauen.

Authority Boundary:

- Dev besitzt keine fachwissenschaftliche Method Truth;
- Dev darf Acceptance Criteria nicht still abschwächen;
- irreversible/teure/lock-in-relevante Entscheidungen brauchen explizite Begründung/ADR/ggf. #44;
- keine Infrastruktur auf Vorrat.

### #59 – MVP Development & Verification

**Aktiv.** Ziel ist jetzt ein real nutzbarer Walking Skeleton, nicht erst eine spätere Implementierung nach einem großen Architecture Gate.

Erster Slice-Kandidat:

```text
Zotero / Source Metadata
→ OneDrive Source Bytes oder Testdatei
→ Source / inspected Instance / Findspot
→ Text/OCR soweit verfügbar
→ Exact + Variant Search
→ Excerpt / Observation
→ Finding / Historical Hypothesis / Research Hook
→ Method-/Evidence-Status
→ Audit / Persistenz / Handoff
```

### #58 – Architecture Decisions / ADRs

Nicht mehr Blocking-Gate. Wird **just in time** benutzt, wenn eine materielle technische Entscheidung Vergleich/ADR braucht.

## 6. Technische Teilpakete

- **#49** – Zotero ↔ OneDrive, read-first Integration
- **#50** – Canonical Research State / Source Identity
- **#51** – Document-/Findspot-Pipeline
- **#52** – OCR/HTR Benchmark/Integration
- **#53** – Historical Retrieval
- **#54** – Promotion / deterministic invariants
- **#55** – Human-readable Audit
- **#56** – Rights / Credentials / External Processing
- **#57** – Provider Removal / Export / Restartability
- **#61** – Work-Context / Method-Conformance / Handoff Technical Research; parallel hardening, kein globaler Development-Blocker

Diese Pakete sollen bevorzugt als kleine verticale Produktinkremente statt isolierte Architekturstudien umgesetzt werden.

## 7. MVP Acceptance – zentrale Kriterien

Vollständiger Owner-accepted Overlay:

`docs/research/synthesis/mvp-acceptance.md`

Kern:

- wissenschaftliche Zustandsarten getrennt;
- Source/Instance/Derivative/Findspot-Roundtrip;
- AI ≠ Evidence;
- unresolved/not-assessable möglich;
- Domain Method Profiles + konkrete Method Application/Status;
- Evidence Demand / Research Hooks / Multi-Domain-Handoffs;
- Exact/Variant Retrieval ohne LLM-Pflicht;
- OCR/HTR bleibt Derivat;
- Audit bis Quelle/Fundstelle/Methode/Unsicherheit/Review;
- portable/restartable/chat-unabhängige State;
- Zotero/OneDrive/Histo-Orla-Verantwortung;
- formale Invarianten deterministisch, soweit formal geklärt;
- private, progressive, human-readable UX.

`usable increment` darf früher existieren; `MVP complete` erst bei bestandenem Acceptance-Overlay für den privaten Scope.

## 8. Source / Storage Responsibility

```text
OneDrive = Source of Bytes
Zotero   = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht Source-/Instance-Identität.

## 9. Blocker / Owner Decisions

#44 ist Decision/Dependency Register.

Aktuell:

- **DD-001 resolved:** privates lean/agiles Delivery-Modell; Domain-Systemanforderungen = MVP-Akzeptanzkriterien; Build jetzt, wissenschaftlich/technisch im realen Einsatz härten.

Kein allgemeiner Development-Blocker aus #42/#43/#60/#61.

## 10. Nächste ausführbare Aktionen

### Delivery

1. #48/#59 Walking Skeleton konkretisieren und implementieren.
2. minimalen projekt-/testbaren technischen Stack auswählen – reversibel, vorhandene Tools bevorzugt.
3. #49 zuerst soweit nötig: Zotero read-only + OneDrive/Test-Byte-Auflösung.
4. #50/#51: kleinsten persistenten Source/Instance/Findspot-State für den Slice implementieren.
5. #53: Exact Search früh nutzbar machen; Varianten danach inkrementell.
6. #55: einfache menschenlesbare Audit-Ausgabe aus demselben State.
7. #54: nur bereits formal klare Invarianten automatisiert testen.

### Parallel Domain

8. #46/#47 reale Forschung fortführen.
9. #60 Diplomatik-/Editions-Profil SOTA-basiert härten und direkt im laufenden MVP-Workflow testen.
10. neue fachliche Anforderungen direkt als Acceptance-Deltas an #42 zurückgeben; kein monatelanges Warten auf vollständige Fachprofile.

### Just-in-time Architecture

11. #58/ADR nur aufrufen, wenn eine Entscheidung materiell, schwer reversibel oder wissenschaftlich folgenreich wird.

## 11. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- aktuelles MVP-Ziel und Acceptance Criteria;
- primäre Funktion/Authority;
- laufenden Delivery-Slice;
- Method-/Evidence-Status;
- offene technische/fachliche Debt;
- nächste Aktion und Persistenzort.

Leitformeln:

> **Privat, lean, agil: früh nutzbar werden, im realen Forschen härten.**

> **Architecture is a means, not a phase gate.**

> **Fachdomänen führen. Technologie dient.**
