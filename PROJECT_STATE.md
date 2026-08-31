# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-08-31  
**State Owner:** #1; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Kanonische Detailwahrheit liegt in Requirements-, Research-, Method-, Architecture- und Development-Artefakten.

## 1. Aktuelle Phase / Owner-Klärung

Histo-Orla ist ein **privates, leanes und agiles Forschungssystem**.

Verbindlich gilt:

> **Die gesamte bereits gemeinsam erarbeitete und akzeptierte Requirements-/Quality-/Governance-Basis bleibt für den privaten MVP aktiv. Domain-/Live-Research- und Methodenanforderungen ergänzen und schärfen diese Basis.**

> **Lean optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value – nicht den Anspruch. Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/mvp-acceptance.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/mvp-coverage.md` – Delivery-Coverage, keine zweite Requirement Truth
- `docs/research/synthesis/phase-reconciliation.md`
- #44 DD-001 + Non-Regression-Amendment

Aktueller Arbeitsfluss:

```text
vollständige aktive MVP Acceptance (#42)
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

## 2. Non-Regression / Qualitätsinterpretation

Die Begriffe `lean`, `agil`, `privat`, `MVP`, `Walking Skeleton`, `Greenfield`, neue Tools/Frameworks oder neue Phasen dürfen bestehenden accepted Scope **nicht implizit superseden**.

Für den privaten MVP gilt mindestens die Vereinigung aus:

1. accepted Requirements aus `requirements-baseline.md`;
2. `mvp-acceptance.md`;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints;
4. owner-accepted Systemanforderungen aus #46/#47/#60;
5. späteren expliziten Acceptance-Deltas unter #42.

Materielle Scope-/Qualitätsreduktion benötigt ein explizites Requirement-/Acceptance-Delta mit Grund, Konsequenz/Loss, Alternative und Owner-Entscheidung.

`nicht im aktuellen Slice` bedeutet **nicht** `nicht MVP`.

Ein Slice darf klein in der Breite sein, muss innerhalb seines behaupteten Scopes aber wissenschaftlich und technisch korrekt sein. Fehlende Fähigkeiten werden sichtbar als fehlend/partial/research-needed geführt und nicht durch vereinfachte Semantik simuliert.

State of the Art und Best Practice bleiben Basis der wissenschaftlichen und technischen Mittelwahl. Just-in-time Research reduziert Vorlauf, nicht Qualitätsanspruch.

## 3. Baselines und aktuelle Präzedenz

Der erste Durchlauf #28–#43 bleibt als v0.1 Discovery-/SOTA-/Requirements-/Readiness-Provenienz erhalten.

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Questions – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risks/Constraints – completed
- #41 Capability/Quality – completed
- #42 Requirements Baseline v0.1 – accepted baseline + aktive MVP-Acceptance-/Coverage-Schärfung
- #43 früheres Gate – in continuous/evolutionary readiness überführt

Neue Domain-/Case-Befunde dürfen Requirements/Acceptance weiter schärfen, blockieren Development nicht pauschal und reduzieren alte Acceptance nicht still.

## 4. Aktive fachliche Work Owner

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

Method Profiles dürfen als `method-candidate` explorativ verwendet werden. Fehlende Reife muss sichtbar bleiben und darf keinen höheren epistemischen Status vortäuschen.

## 5. Requirements / MVP Acceptance – #42

#42 ist einziger Owner akzeptierter Systemanforderungen und MVP-Akzeptanzkriterien.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/mvp-acceptance.md`
- `docs/governance/lean-agile-non-regression.md`

Delivery Coverage:

- `docs/development/mvp-coverage.md` – **39/39 Baseline-Requirements + 38/38 MVP-Overlay-Kriterien repräsentiert**; Status-/Implementation-/Verification-Sicht, keine zweite Requirement Truth.

#42 führt die vollständige Acceptance-Basis monoton weiter, bis ein Kriterium explizit geändert/superseded/owner-deferred wird.

Pflichtstatus je aktivem Kriterium für Delivery:

```text
not-started
in-progress
implemented
verified
partial
blocked
research-needed
owner-deferred
```

`owner-deferred` erfordert explizite Owner-Entscheidung.

## 6. Technical Lead / Delivery

### #48 – Lean MVP Delivery / Technical Lead

Auftrag:

- vollständige Acceptance-Coverage sichtbar halten;
- technischen Backlog nach Nutzerwert, Risiko, Dependency und kleinster nutzbarer Lieferung priorisieren;
- SOTA/Best Practice und Existing Tools **just in time** für konkrete Entscheidungen prüfen;
- reversible technische Entscheidungen früh treffen und refactorbar halten;
- Integrationen/Spikes direkt in nutzbare Slices überführen;
- evolutionäre Architektur;
- Acceptance/Regression/Invariant Tests laufend ausbauen.

Authority Boundary:

- Dev besitzt keine fachwissenschaftliche Method Truth;
- Dev darf Acceptance Criteria nicht still abschwächen, streichen oder zu `nicht MVP` umdeuten;
- irreversible/teure/lock-in-relevante Entscheidungen brauchen explizite Begründung/ADR/ggf. #44;
- keine Infrastruktur auf Vorrat;
- keine Prototyp-/Happy-Path-Qualität als erfüllte Acceptance deklarieren.

### #59 – MVP Development & Verification

**Aktiv.** `docs/development/mvp-coverage.md` ist die aktuelle Delivery-Coverage-Sicht. Noch existiert kein produktiver Anwendungscode; die Coverage ist daher überwiegend `not-started/research-needed`, mit einigen Governance-/Delivery-Kriterien bereits `in-progress`.

Ziel ist ein real nutzbarer Walking Skeleton als erster Vertical Slice und danach inkrementelle Erfüllung der vollständigen privaten MVP-Acceptance.

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

Der Skeleton ist Lieferreihenfolge, nicht Scope-Reduktion.

### #58 – Architecture Decisions / ADRs

Nicht Blocking-Gate. Wird just in time benutzt, wenn eine materielle technische Entscheidung Vergleich/ADR braucht.

## 7. Technische Teilpakete

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

Diese Pakete werden bevorzugt als kleine vertikale Produktinkremente umgesetzt. Ihre Reihenfolge bestimmt #48 nach Dependency/Risiko/Nutzerwert; ihre Priorisierung hebt accepted Scope nicht auf.

## 8. MVP Acceptance – Kern

Vollständiger Overlay: `docs/research/synthesis/mvp-acceptance.md`. Baseline bleibt zusätzlich gültig.

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
- private, progressive, human-readable UX;
- technische Lösung auf SOTA/Best Practice, Existing Tools und kleinste hinreichende Architektur zurückführen.

`usable increment` darf früher existieren; `MVP complete` erst bei bestandener **vollständiger aktiver Acceptance** für den privaten Scope.

## 9. Source / Storage Responsibility

```text
OneDrive = Source of Bytes
Zotero   = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht Source-/Instance-Identität.

## 10. Blocker / Owner Decisions

#44 ist Decision/Dependency Register.

Aktuell:

- **DD-001 resolved + Amendment:** build now / harden while using; vollständige bestehende Acceptance bleibt aktiv; Lean/Agile reduziert Scope/Qualität nicht.

Kein allgemeiner Development-Blocker aus #42/#43/#60/#61.

## 11. Nächste ausführbare Aktionen

### Delivery

1. **ERLEDIGT:** initiale Acceptance-Coverage erstellt: `docs/development/mvp-coverage.md` mit 39/39 Baseline-Requirements und 38/38 MVP-Overlay-Kriterien.
2. daraus ersten wissenschaftlich/technisch korrekten Vertical Slice unter #48/#59 implementieren.
3. minimalen technischen Stack auswählen – reversibel, SOTA/Best Practice prüfen, Existing Tools bevorzugen.
4. #49: Zotero read-only + OneDrive/Test-Byte-Auflösung soweit für Slice nötig.
5. #50/#51: persistenten Source/Instance/Findspot-State für den Slice implementieren.
6. #53: Exact Search früh nutzbar machen; Varianten inkrementell nachziehen.
7. #55: menschenlesbare Audit-Ausgabe aus demselben State.
8. #54: formal klare Invarianten automatisiert testen.
9. jede materielle Implementierungsänderung aktualisiert `mvp-coverage.md`; weitere aktive Acceptance nach Dependency/Risiko/Nutzerwert nachziehen, nicht als `später = nicht MVP` behandeln.

### Parallel Domain

10. #46/#47 reale Forschung fortführen.
11. #60 Diplomatik-/Editions-Profil SOTA-basiert härten und im laufenden MVP-Workflow testen.
12. neue fachliche Systemanforderungen als Acceptance-Deltas an #42 zurückgeben und in Coverage ergänzen.

### Just-in-time Architecture / Research

13. #58/ADR nur bei materiellen, schwer reversiblen oder wissenschaftlich folgenreichen Entscheidungen.
14. technische/fachliche SOTA-Recherche proportional zur konkreten Entscheidung; keine monatelange Vorstudie, aber auch kein Raten.

## 12. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- vollständige aktive MVP-Acceptance;
- `docs/development/mvp-coverage.md` und den aktuellen Coverage-Status;
- aktuellen Slice;
- primäre Funktion/Authority;
- Method-/Evidence-Status;
- was implementiert/verifiziert/partial/blocked/research-needed ist;
- welche Anforderungen später priorisiert, aber nicht gestrichen sind;
- nächste Aktion und Persistenzort.

Leitformeln:

> **Lean heißt kleinste hinreichende Lösung – nicht kleinster Anspruch.**

> **Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**

> **Fachdomänen führen. Technologie dient.**
