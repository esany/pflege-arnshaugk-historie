# Histo-Orla – Ablage- und Ownership-Regeln für Research-Ergebnisse

**Projekt-Bootstrap:** `/AGENTS.md` → `/PROJECT_STATE.md` → `/README.md`  
**Research Governance:** #45  
**Issue Ownership:** #23

## Zweck

Dieses Verzeichnis ist der kanonische Ort für **substantielle, versionierte Research-Artefakte** sowie eigenständige historische Live-Research-Fälle.

GitHub Issues bleiben die **Work Owner**. Sie besitzen Auftrag, Scope, Status, Abhängigkeiten, Decision-/Blocker-Hinweise und eine kompakte Ergebniszusammenfassung. Umfangreiche Befunde, Tabellen, Quellenapparate, Research Reviews, Baselines und abgeleitete Kataloge liegen versioniert im Repo.

Grundregel:

```text
Issue
= Arbeit steuern / Status / Dependencies / Entscheidungen / Verweise

Research-Datei
= substantieller kanonischer Forschungsinhalt

Chat
= Werkstatt / transient

Code
= konkrete technische Umsetzung oder begrenzter diskriminierender Prototyp
```

> **Chat ist Werkstatt; GitHub ist Projektgedächtnis.**

Repo-weite Handoff-/Persistenzregeln stehen verbindlich in `/AGENTS.md`.

## One fact / one canonical home

Wenn ein substanzielles Artefakt existiert:

- Datei = ausführlicher kanonischer Inhalt;
- Issue = Work Owner + Status + Kurzsynthese + offene Punkte + Verweis;
- `PROJECT_STATE.md` = phasenübergreifende Navigations-/Handoff-Sicht;
- Chat = transient;
- spätere Views/Reports = abgeleitete Darstellung.

Keine parallele manuelle Pflege desselben Vollinhalts in Issue und Datei.

## Kein neues Issue für jedes Finding

Neue Issues werden nur nach #23 angelegt, wenn ein eigenständiger Research-/Decision-/Work-Scope mit eigener Definition of Done entsteht.

Einzelne Findings, Quellenhinweise, Literaturbefunde oder kleine Korrekturen werden im zuständigen Work Package verarbeitet und – wenn substantiell – in dessen Artefakt persistiert.

## Bindendes Source-Identity-Protokoll

Für tragende Quellen gilt:

`docs/research/source-identity-protocol.md`

Work Owner: #45.

Es trennt mindestens:

```text
historische Source / Überlieferung
→ Edition / Katalog / Reproduktion
→ konkrete digitale/physische Instanz
→ Derivat / OCR / HTR / Transkription
→ exakte Fundstelle / Exzerpt
→ Finding / Interpretation
```

URL, Viewer-Seite oder Dateipfad allein sind keine Quellenidentität. Persistente Identifier, konkrete Instanz, Inspection Status, Print-/Scan-Seitenmapping und Derivatstatus werden proportional zur Forschungsrelevanz nachvollziehbar gehalten.

## Research-Artefaktstruktur

Aktuell vorhanden bzw. kanonisch genutzt:

```text
docs/research/
  README.md
  source-identity-protocol.md

  discovery/
    problem-baseline.md
    workflows.md
    research-questions.md

  sota/
    c1-quellen-archiv-provenienz.md
    c2-problemuebersetzung-terminologie.md
    c3-expertise-routing.md
    c4-regionalitaet-multiscale.md
    c5-akteurs-handlungslogik.md
    c6-source-dependence-discrepancy.md
    c7-ocr-htr-retrieval.md
    c8-research-state-auditability.md
    c9-capability-allocation.md

  synthesis/
    risks-constraints.md
    capability-map.md
    requirements-baseline.md
    architecture-readiness.md

  cases/
    u2-knau-orlagau-quellenbefunde.md
    u2-orlagau-suchraum-quellenexzerpte.md
    u1-orlagau-grenzraum-teichlandschaft.md
    orlagau-source-ledger.md
```

Die Struktur wächst nur bei tatsächlichem Inhalt. Keine Future-Proof-Leerstruktur.

## Zuordnung zu Work Ownern

| Issue | Work Owner | kanonisches Artefakt / Bereich |
|---|---|---|
| #28 | Problem-/Need-/Pain-Baseline | `discovery/problem-baseline.md` |
| #29 | Workflows U1–U4 | `discovery/workflows.md` |
| #30 | Research-Question-Portfolio | `discovery/research-questions.md` |
| #31 | SOTA C1 | `sota/c1-quellen-archiv-provenienz.md` |
| #32 | SOTA C2 | `sota/c2-problemuebersetzung-terminologie.md` |
| #33 | SOTA C3 | `sota/c3-expertise-routing.md` |
| #34 | SOTA C6 | `sota/c6-source-dependence-discrepancy.md` |
| #35 | SOTA C7 | `sota/c7-ocr-htr-retrieval.md` |
| #36 | SOTA C4 | `sota/c4-regionalitaet-multiscale.md` |
| #37 | SOTA C5 | `sota/c5-akteurs-handlungslogik.md` |
| #38 | SOTA C8 | `sota/c8-research-state-auditability.md` |
| #39 | SOTA C9 | `sota/c9-capability-allocation.md` |
| #40 | Risk/Constraint Review | `synthesis/risks-constraints.md` |
| #41 | Capability/Quality Synthesis | `synthesis/capability-map.md` |
| #42 | Requirements Baseline | `synthesis/requirements-baseline.md` |
| #43 | Architecture Readiness | `synthesis/architecture-readiness.md` |
| #45 | Research-/Evidence-/Source-Protokoll | `source-identity-protocol.md` + Issue-Protokoll |
| #46 | Live Research U2 Knau/Orlagau | `cases/u2-knau-orlagau-quellenbefunde.md`, `cases/u2-orlagau-suchraum-quellenexzerpte.md` |
| #47 | Live Research U1 Teich-/Feuchtlandschaft | `cases/u1-orlagau-grenzraum-teichlandschaft.md` |
| #46/#47 | gemeinsamer Source-Identity-Ledger | `cases/orlagau-source-ledger.md` |

Architekturartefakte ab #48ff liegen **nicht** unter `docs/research/`, sondern werden über `docs/architecture/README.md` indexiert.

## Live Research Cases

Repräsentative Use Cases aus #29/#30 dürfen als **echte historische Forschung** weiterlaufen, wenn ein eigenständiger Scope/DoD besteht.

```text
Case Issue
= Work Owner / Scope / Status / nächste Aktionen

Case-Datei
= historischer Forschungsstand / Findings / Grenzen / Search Boundaries

Source Ledger / Exzerptregister
= Quellenidentität bzw. fundstellenfähiges Material
```

Live Cases dürfen Capability-/Quality-/Requirement-Candidates erzeugen. Ein Einzelfall allein erzwingt keine Systemarchitektur. Materiell neue generalisierbare Invarianten werden gegen #41/#42 und die laufende Architektur geprüft.

Aktuell laufen #46 und #47 weiterhin `in-research / working-research`.

## Was bleibt im Issue?

Mindestens:

- aktueller Status;
- Scope / Research Question;
- führende Fachdomänen;
- Abhängigkeiten;
- Link/Pfad zum kanonischen Artefakt;
- kurze Ergebniszusammenfassung;
- wichtigste offene Punkte;
- Sättigungs-/Abschlussstatus;
- Blocker bzw. Verweis auf #44;
- nächste Aktion.

Das Issue spiegelt nicht den vollständigen Artefaktinhalt.

## Was gehört in die Research-Datei?

Je nach Arbeitspaket insbesondere:

- genaue Research Questions und Scope;
- Suchstrategie / Search Boundaries;
- Fachbegriffe und konkurrierende Modelle;
- geprüfte Quellen/Literatur mit exakten Referenzen;
- Findings und Grenzen;
- Kontroversen / Alternativen;
- domänenspezifische Methoden-/Qualitätsbefunde;
- Risiken / Failure Modes;
- Capability-/Quality-/Requirement-Implikationen;
- verworfene Ansätze, wenn für spätere Entscheidungen relevant;
- Sättigungsbegründung.

## Register und Tabellen

Markdown ist Default, solange lesbar.

TSV/CSV/strukturierte Formate erst, wenn:

- ein Register deutlich tabellarisch wächst;
- maschinelle Verarbeitung realen Nutzen bringt;
- oder Konsistenz/Filterung in Markdown unverhältnismäßig wird.

Kein Schema-/Datenbankbau aus Vorsorge.

## Handoff-Check für Research

Vor `reviewable/completed` oder vor einem materiellen Chat-Handoff:

1. substantieller Stand im kanonischen Artefakt?
2. Issue-Status und nächste Aktion aktuell?
3. Quellen/Fundstellen/Provenienz ausreichend sichtbar?
4. Search Boundaries und Unsicherheit dokumentiert?
5. echte Blocker in #44?
6. `PROJECT_STATE.md` nur dann nachgezogen, wenn sich phasenübergreifender State/Ownership/Dependency materiell geändert hat?
7. kann ein neuer Bearbeiter ohne Chat fortsetzen?

Wenn nein: Handoff ist nicht vollständig.