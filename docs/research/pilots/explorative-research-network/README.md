# Pilot #86 – Exploratives Forschungsnetz

**Status:** `working-pilot / branch-isolated / no-main-authority`  
**Branch:** `pilot/explorative-research-network-20260907`  
**Work Owner:** #86  
**Review:** #87  
**Prototype:** #88  
**Evaluation:** #89

## Zweck

Dieser Pilot untersucht, wie Histo-Orla **ergebnisoffene, hochgradig vernetzte Forschungsarbeit** unterstützen kann, wenn Material, Forschungsfragen, Analyse/Synthese und Maßstabswechsel nicht in einer linearen Pipeline organisiert werden.

Der Ausgangspunkt ist reale Forschungsarbeit am Raum Ranis/Orlatal: wissenschaftliche Publikationen, historische Quellen, Karten, Museumsobjekte/-beschriftungen, Fotos eines Feld-/Museumsbesuchs, Fundstellen, Forschungsgeschichte, Geologie, Archäologie, Burg-/Bauforschung und aktuelle Baustellenbeobachtungen treffen aufeinander. Ihre Relevanz ist nicht im Voraus vollständig bekannt.

Der Pilot ist **kein Vermittlungsprojekt** und verfolgt **keine einzelne historische Masterfrage**.

## Kernhypothese

Die praktikable Einheit ist nicht `eine Frage = ein Case` und nicht `Materialsammlung statt Fragen`, sondern:

> **ein gemeinsamer, provenance-sicherer Forschungszustand + modulare Research Questions + rekombinierbare Beziehungen + abgeleitete Views/Synthesen.**

Eine Forschungsfrage ist eine **Linse / ein Arbeitsmodul**, kein Container und kein Besitzer von Evidenz.

## Forschungsdynamik

```text
Material / Quelle / Beobachtung
        ↕
Identifikation / Quellenkritik / Kontext
        ↕
Analyse von Details und Relationen
        ↕
vorläufige Muster / Hypothesen
        ↕
Synthese / Überblick / Scale Shift
        ↕
neue Fragen / Gegenhypothesen / Lücken
        ↕
gezielte Detailarbeit
        ↺
```

Die Pfeile sind absichtlich bidirektional. Analyse↔Synthese und Überblick↔Detail sind dauernde Wechselbeziehungen, keine einmaligen Phasenübergänge.

## Was stabil bleiben soll

- Source-/Instance-Identität und Provenienz;
- Fundstellen-/Findspot-Rückführung;
- Trennung von Observation, Finding, Claim/Interpretation, Hypothese und Synthesis/View;
- Unsicherheit, Widerspruch und unresolved state;
- Kompetenz-/Methodenhoheit je konkreter Forschungsfrage;
- Git/GitHub-Restartability und Reviewbarkeit.

## Was flexibel bleiben soll

- Zuschnitt von Forschungsfragen;
- räumlicher und zeitlicher Maßstab;
- Reihenfolge der Arbeitsschritte;
- führende/kontrollierende Fachkompetenzen;
- Gruppierung und Projektion des Materials;
- Beziehungen, Hypothesen und Synthesen als Candidates;
- Frageoperationen wie `split`, `fuse`, `reframe`, `supersede`, `defer`.

## Repo-Passung

Der Pilot soll zunächst vorhandene Histo-Orla-Mechanismen wiederverwenden. Besonders relevant sind:

- #28/#29 – Needs/Pains und Research Workflows;
- #30 – Research Question Portfolio;
- #41 – Capability Map;
- #45 – cross-cutting Research-/Evidence-Rahmen;
- #50 – Canonical Research State / Source Identity;
- #60 – Domain Method Profiles / Method Truth;
- #63 – Value/Decision/Delivery/Feedback Assurance.

Generische Aussagen werden zusätzlich gegen `esany/Wissensarbeit` geprüft. Dort sind besonders `Canonical State`, `Context Compiler`, `Competence Discovery`, `Systemic Integration`, `Derived Views` und `Use and Learn` einschlägig. Ein neuer generischer Building Block ist **nicht** Ziel dieses Piloten.

## Dateien

- [`model.md`](model.md) – Arbeitsmodell, Invarianten, Question Modules, Relationen, Views.
- [`workflows.md`](workflows.md) – rekursive Forschungsbewegungen und Scale Shifts.
- [`stress-case-ranis-orlatal.md`](stress-case-ranis-orlatal.md) – realer Material-/Forschungsstressfall ohne neue historische Authority.
- [`review-and-eval.md`](review-and-eval.md) – Review-/Evaluationslogik und Dispositionen.
- [`learnings.md`](learnings.md) – dokumentierte Fehlrahmungen und methodische Learnings.
- [`handoff.md`](handoff.md) – expliziter Startpunkt für unabhängige Review-/Implementierungs-Chats.

## Authority

Alles in diesem Ordner ist `pilot/candidate`. Es ändert keine accepted Requirements, Method Truth, Architecture oder historischen Findings auf `main`.

Persistenz ist hier **keine Promotion**.
