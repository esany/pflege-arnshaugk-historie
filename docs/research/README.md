# Histo-Orla – Ablage- und Ownership-Regeln für Research-Ergebnisse

## Zweck

Dieses Verzeichnis ist der kanonische Ort für **substantielle, versionierte Research-Artefakte** aus der Arbeitskette #27–#45 sowie für eigenständige, reale historische Research-Fälle, die nach #23 einen eigenen Work Owner besitzen.

GitHub Issues bleiben die **Work Owner**. Sie besitzen Auftrag, Scope, Status, Abhängigkeiten, Decision-/Blocker-Hinweise und eine kompakte Ergebniszusammenfassung. Umfangreiche Befunde, Tabellen, Research Reviews, Baselines und abgeleitete Kataloge sollen jedoch nicht dauerhaft nur in Issue-Kommentaren liegen.

Grundregel:

```text
Issue = Arbeit steuern / Status / Entscheidungen / Verweise
Markdown im Repo = substantieller kanonischer Forschungsinhalt
Code = erst konkrete technische Umsetzung
```

Damit gilt weiterhin:

> **Chat ist Werkstatt; GitHub ist Projektgedächtnis.**

und innerhalb GitHub:

> **Issues steuern Arbeit. Versionierte Research-Artefakte tragen den ausführlichen Forschungsstand.**

## Kein neues Issue für jedes Finding

Neue Issues werden nur nach #23 angelegt, wenn ein eigenständiger Research-/Decision-/Work-Scope mit eigener Definition of Done vorliegt.

Einzelne Findings, Quellenhinweise, Literaturbefunde oder kleine Korrekturen werden im zuständigen Work Package verarbeitet und – wenn substantiell – in dessen Research-Artefakt persistiert.

Keine Issue-Explosion als Ersatz für Informationsarchitektur.

## Live Research Cases

Repräsentative Use Cases aus #29/#30 dürfen als **echte historische Forschung** weitergeführt werden, wenn daraus ein eigenständiger Research-Scope mit eigener Definition of Done entsteht. In diesem Fall gilt dieselbe Ownership-Regel:

```text
Case-Issue = Work Owner / Scope / Status / nächste Aktionen
Case-Datei = ausführlicher historischer Forschungsstand / Source Ledger / Findings / Grenzen
```

Ein Live-Fall darf Capability-, Quality- und Requirement-Candidates erzeugen. Diese werden jedoch nicht allein aus einem Einzelfall zu Requirements promoviert, sondern erst über die Synthese #41/#42 und das Gate #43 geprüft.

## Wann genügt das Issue selbst?

Das Issue genügt, wenn der Arbeitsstand:

- kurz und übersichtlich bleibt,
- keinen größeren Quellen-/Literaturapparat benötigt,
- keine umfangreichen Tabellen/Registersichten enthält,
- und ohne Scroll-/Kommentarrekonstruktion vollständig verständlich bleibt.

Sobald ein Ergebnis zu einem eigenständigen Research-Artefakt wird, soll es als versionierte Datei persistiert werden.

## Geplante leane Ablagestruktur

Die Struktur wird nur erzeugt, wenn tatsächlich Inhalt anfällt. Keine leeren Future-Proof-Verzeichnisse.

Vorgesehene Pfade:

```text
docs/research/
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

  cases/
    u2-knau-orlagau-quellenbefunde.md

  synthesis/
    risks-constraints.md
    capability-map.md
    requirements-baseline.md
    architecture-readiness.md
```

Diese Dateinamen sind **Arbeitskonventionen, keine unveränderliche Architektur**. Wenn ein Artefakt zu groß oder fachlich sinnvoll teilbar wird, darf es nach tatsächlichem Bedarf aufgeteilt werden. Wenn mehrere kleine Artefakte gemeinsam lesbarer sind, dürfen sie zusammenbleiben.

## Zuordnung zur aktuellen Issue-Kette und Live Research

| Issue | Work Owner | bevorzugtes Research-Artefakt bei substantiellem Umfang |
|---|---|---|
| #28 | Problem-/Need-/Pain-/Risk-Baseline | `docs/research/discovery/problem-baseline.md` |
| #29 | Workflows U1–U4 | `docs/research/discovery/workflows.md` |
| #30 | Research-Question-Portfolio | `docs/research/discovery/research-questions.md` |
| #31 | SOTA C1 | `docs/research/sota/c1-quellen-archiv-provenienz.md` |
| #32 | SOTA C2 | `docs/research/sota/c2-problemuebersetzung-terminologie.md` |
| #33 | SOTA C3 | `docs/research/sota/c3-expertise-routing.md` |
| #34 | SOTA C6 | `docs/research/sota/c6-source-dependence-discrepancy.md` |
| #35 | SOTA C7 | `docs/research/sota/c7-ocr-htr-retrieval.md` |
| #36 | SOTA C4 | `docs/research/sota/c4-regionalitaet-multiscale.md` |
| #37 | SOTA C5 | `docs/research/sota/c5-akteurs-handlungslogik.md` |
| #38 | SOTA C8 | `docs/research/sota/c8-research-state-auditability.md` |
| #39 | SOTA C9 | `docs/research/sota/c9-capability-allocation.md` |
| #40 | Risk/Constraint Review | `docs/research/synthesis/risks-constraints.md` |
| #41 | Capability/Quality Synthesis | `docs/research/synthesis/capability-map.md` |
| #42 | Requirements Baseline | `docs/research/synthesis/requirements-baseline.md` |
| #43 | Architecture Readiness | `docs/research/synthesis/architecture-readiness.md` |
| #46 | Live Research U2: Knau/Orlagau | `docs/research/cases/u2-knau-orlagau-quellenbefunde.md` |

## Was bleibt im Issue?

Auch wenn eine Datei existiert, hält das Issue mindestens:

- aktuellen Status;
- Scope / Research Question;
- führende Fachdomänen;
- Abhängigkeiten;
- Link/Pfad zum kanonischen Research-Artefakt;
- kurze Ergebniszusammenfassung;
- wichtigste offene Punkte;
- Sättigungs-/Abschlussstatus;
- Blocker bzw. Verweis auf #44;
- nächste Aktion.

Das Issue soll **nicht** den vollständigen Artefaktinhalt spiegeln.

## Was gehört in die Research-Datei?

Je nach Arbeitspaket insbesondere:

- Problem-/Need-/Pain-Einträge und deren Provenienz;
- genaue Research Questions und Scope;
- Suchstrategie / Search Boundaries;
- Fachbegriffe und konkurrierende Modelle;
- geprüfte Quellen/Literatur mit exakten Referenzen;
- Findings und Grenzen;
- Kontroversen / Alternativen;
- domänenspezifische Methoden-/Qualitätsbefunde;
- Risiken / Failure Modes;
- Capability-/Quality-Implikationen;
- Requirement Candidates;
- verworfene Ansätze und Begründungen, wenn für spätere Entscheidungen relevant;
- Sättigungsbegründung.

## Register und Tabellen

Markdown ist der Default, solange es lesbar bleibt.

TSV/CSV oder andere strukturierte Formate werden erst eingesetzt, wenn:

- ein Register deutlich tabellarisch wächst,
- maschinelle Verarbeitung einen realen Nutzen bringt,
- oder Konsistenz/Filterung mit Markdown unverhältnismäßig wird.

Kein Schema-/Datenbankbau nur aus Vorsorge.

## Code und technische Artefakte

Research-Ergebnisse gehören **nicht in Anwendungscode**.

Code entsteht erst, wenn eine technische Capability/Requirement umgesetzt oder ein begrenzter Prototyp/Test zur Diskriminierung einer technischen Frage benötigt wird.

Technische Tests/Prototypen müssen auf Requirements/Research Findings zurückverweisen; sie werden nicht zum Ersatz für den fachlichen Research State.

## Entscheidungen

Echte Blocker/Owner-Decisions werden nach #44 geführt. Architekturentscheidungen/ADRs entstehen erst in der entsprechenden späteren Phase.

Ein Research-Artefakt darf eine Empfehlung enthalten, aber eine Empfehlung ist noch keine getroffene Entscheidung.

## One fact / one canonical home

Wenn ein substanzielles Artefakt existiert:

- Datei = ausführlicher kanonischer Inhalt;
- Issue = Work Owner + Status + Kurzsynthese + Verweis;
- Chat = transient;
- spätere Views/Reports = abgeleitete Darstellung.

Keine parallele manuelle Pflege desselben Vollinhalts in Issue und Datei.
