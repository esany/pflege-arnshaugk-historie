# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk und für die Entwicklung einer **transdisziplinären historischen Forschungsassistenz**.

Der frühere Begriff „persönlicher Archivar“ bleibt als wichtige Spezialrolle erhalten, ist aber **nicht das Gesamtziel**. Ziel ist ein **funktionierendes, dauerhaft nutzbares Forschungswerkzeug**, das belastbare Quellenarbeit, fachliche Problemübersetzung, regionalisierte Spitzenexpertise, transdisziplinäre Analyse und nachvollziehbare Synthese unterstützt.

## Präzedenz

```text
konkreter Forschungsauftrag / Nutzer-Pain
→ führende Fachdomäne(n)
→ wissenschaftliche Standards / Methoden / Evidenzbedarf
→ State of the Art + internes Prior Art
→ validierte Needs / Capabilities / Quality Attributes
→ Requirements + Acceptance Criteria
→ Architektur / Design
→ Development / Integration
→ technische + wissenschaftliche Verifikation
→ reales MVP / Nutzung
→ Evaluation / Iteration
```

**Fachdomänen führen. Technologie dient.**  
**Dev informiert Requirements; Dev besitzt sie nicht.**

Lean bedeutet: **so wenig unnötige technische Komplexität wie möglich, aber so viel funktionierendes System wie nötig**, um validierte Nutzer- und Forschungsanforderungen hochwertig zu erfüllen.

## Governing Principles

- **Wissenschaft vor Convenience:** Fachstandards der jeweils aktivierten Disziplin dürfen weder durch unscharfe Nutzerfragen noch durch Technik, UI oder Vermittlungsziele abgeschwächt werden.
- **Human-in-the-loop + Auditierbarkeit:** Routinearbeit darf Assistenz/Software übernehmen; consequential work muss erklärbar, anfechtbar, stoppbar und fachlich überprüfbar bleiben.
- **Kein Wissensmonopol im Chat:** Chat ist Werkstatt; GitHub ist dauerhaftes Projektgedächtnis.
- **Research first, aber mit Delivery-Ziel:** SOTA/Requirements dienen der Umsetzung eines funktionierenden Systems, nicht einem Konzeptpapier als Selbstzweck.
- **Technische Subsidiarität:** vorhandene Werkzeuge vor Eigenentwicklung; deterministische/spezialisierte Verfahren vor generativer KI, wo sie die Aufgabe besser lösen.
- **Forschung ≠ Vermittlung:** Histo-Orla erzeugt den belastbaren Forschungszustand. Zielgruppen-/medienbezogene Vermittlung ist nachgelagert und kann z. B. an `rgk-main-ssot` übergeben werden.

## Kanonischer Einstieg

Der konsolidierte menschenlesbare Konzeptstand steht in:

`docs/research-design/transdisziplinaerer-literaturassistent.md`

Die Ablage- und Ownership-Regeln für substantielle Research-Ergebnisse stehen in:

`docs/research/README.md`

Dabei gilt:

```text
Issue = Work Owner / Scope / Status / Decisions / Verweise
Research-Datei im Repo = ausführlicher kanonischer Forschungsinhalt
Code = erst konkrete technische Umsetzung / begrenzter Prototyp
```

Nicht jedes Finding erhält ein neues Issue. Neue Issues entstehen nur für eigenständige Work-/Research-/Decision-Scope nach #23.

Kanonische Steuerungs-Issues:

- **#1** – aktueller Gesamt-/Research-Design-Stand
- **#9** – Governance / HITL / wissenschaftliche Nachvollziehbarkeit / kein Wissensmonopol
- **#10** – Research Plan: Discovery → SOTA → Capabilities → Requirements → Dev → Evaluation
- **#22** – Kompetenzlandkarte für Discovery, Requirements, Risiko, SOTA und Evaluation
- **#23** – Issue-Ownership / Traceability
- **#24** – Software-/Systemkompetenzen, Arbeitsteilung und Lean Development
- **#26** – Arbeitsplan der aktuellen Discovery-/SOTA-/Requirements-Phase
- **#27** – ausführbare autonome Issue-Kette bis Architecture Readiness
- **#44** – nur echte Decisions / Dependencies / externe Validierung
- **#45** – gemeinsames Research-/Evidence-/SOTA-Protokoll

Aktuelle ausführbare Work Packages:

- **#28–#30** – Problem-/Need-Baseline, reale Research Workflows, Research-Question-Portfolio
- **#31–#39** – gezielte fachliche und technische SOTA-Stränge C1–C9
- **#40** – Risk / Constraint / Rights / Failure Review
- **#41** – Capability Map + Quality Attributes
- **#42** – Requirements Baseline + Acceptance Criteria
- **#43** – Architecture-Readiness-Gate

Fachlicher Scope / Qualitätsanforderungen:

- **#13** – transdisziplinäres Querschnittsthema / Expertise Routing
- **#14** – regional verankert, europäisch verflochten
- **#15** – fachliche Tiefe, Kontroversen und Unsicherheit
- **#16** – regionalisierte Spitzenexpertise
- **#19** – Fachkompetenz: Sprache, Modelle, Quellen und Methoden
- **#20** – Forschungszustand ↔ Vermittlung / Übergabegrenze

Quellen-/Infrastrukturthemen:

- **#2** persönlicher Archivar – Spezialrolle
- **#3** Zotero – Hypothese
- **#4** OCR/HTR/Volltext – validierter Bedarf
- **#5** Retrieval / historische Query Expansion / Fundstellen – validierter Bedarf
- **#6** Git-/Provenienzprinzip – Umsetzung offen
- **#8** Automatisierung / KI-Unabhängigkeit – Zielvorgabe, Architektur offen

## Interne Referenzprojekte / Analyseschnittstellen

### `paleo-type` – #12

Prior Art für Forschungsgovernance, Evidenz/Provenienz, Human-in-the-loop, Operational Ownership, Progressive Disclosure, Restartability, proportionale Validierung, Lean und technische Subsidiarität.

### `rgk-main-ssot` – #21

Prior Art für relationale Modellmuster, Claim → Evidence → Interpretation, projektbezogene Quellenfunktionen, Discrepancy Reasoning, Zeit-/Raum-/Akteursbezug sowie die Grenze Forschung ↔ Vermittlung.

Gemeinsamer Transferpfad:

```text
Prior-Art-Befund
→ exakte Herkunft / Ursprungsproblem
→ Relevanz für Histo-Orla
→ führende Fachdomäne(n)
→ externer State of the Art
→ Nutzerwert / Risiko / Capability
→ Quality Criterion / Requirement Candidate
→ erst dann lean technische Realisierung
```

**Keine direkte Kante `Referenzprojekt → Implementation`.**

## Repräsentative reale Designfälle

#10 hält konkrete Testfälle fest, darunter:

- historische Teich-/Niederungs-/Landnutzungsstrukturen vor 1800 mit Forst-/Flur-/Hutungs-/Grenzrissen, Wasser-/Teich-/Mühlenakten, Rechnungen, Kataster/Flurbüchern, älteren Karten und räumlichen Vergleichsdaten;
- mittelalterliche Vogtei-/Ministerialitäts-/Herrschaftsfragen;
- frühneuzeitliche adlige Akteurs-/Handlungslogik in regionalen und europäischen Verflechtungen;
- OCR-/Retrieval-/Fundstellenarbeit im persönlichen Quellenbestand.

## Konsolidierte historische Issues

- **#7** superseded
- **#11** completed alter Concept Audit
- **#17** superseded – Vokabular/Begriffsmodelle integriert
- **#18** superseded – Expertise-/Method Packs integriert
- **#25** abgeschlossener Wissensmonopol-/Restartability-Audit

## Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Fachdomänen führen. Technologie dient.**

> **Lean hält Entwicklung auf den konkreten Forschungsauftrag und nachweisbaren Nutzerwert fokussiert.**

> **Regionaler Fokus für Tiefenschärfe – europäischer Horizont für Erklärung.**

> **Kein Wissensmonopol im Chat.**
