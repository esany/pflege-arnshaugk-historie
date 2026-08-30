# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk und für die Konzeption einer **transdisziplinären historischen Forschungsassistenz**.

Der frühere Begriff „persönlicher Archivar“ bleibt als wichtige Spezialrolle erhalten, ist aber **nicht mehr das Gesamtziel**. Das Zielsystem soll wissenschaftlich belastbare Quellenarbeit, fachliche Problemübersetzung, regionalisierte Spitzenexpertise, transdisziplinäre Analyse und nachvollziehbare Synthese unterstützen.

## Governing Principles

- **Wissenschaft vor Convenience:** Fachstandards der jeweils aktivierten Disziplin dürfen weder durch unscharfe Nutzerfragen noch durch Technik, UI oder Vermittlungsziele abgeschwächt werden.
- **Human-in-the-loop + Auditierbarkeit:** Routinearbeit darf die Assistenz übernehmen; konsequenzielle Arbeit muss erklärbar, anfechtbar, stoppbar und fachlich überprüfbar bleiben.
- **Kein Wissensmonopol im Chat:** Chat ist Werkstatt; GitHub ist dauerhaftes Projektgedächtnis.
- **Forschung vor Architektur:** Technik wird erst aus nachgewiesenen Forschungsbedarfen abgeleitet.
- **Forschung ≠ Vermittlung:** Histo-Orla erzeugt den belastbaren Forschungszustand. Zielgruppen-/medienbezogene Vermittlung ist eine nachgelagerte Sicht und kann z. B. an `rgk-main-ssot` übergeben werden.

## Forschungsprozess

```text
Zielbild / Forschungsalltag
        ↓
Need-/Pain-/Workflow-Analyse
        ↓
Problem-, Risiko- und Open-Question-Map
        ↓
Leane State-of-the-Art-Analyse
        ↓
Capability Map
        ↓
Kompetenzabdeckung + Expertise Profiles
        ↓
Quality / Evaluation / Requirements Traceability
        ↓
Transdisziplinäres Assistenzkonzept
        ↓
validierte Architekturentscheidungen
        ↓
Requirements / MVP / Implementation
```

## Einstieg

Der konsolidierte aktuelle Stand steht in:

`docs/research-design/transdisziplinaerer-literaturassistent.md`

Kanonische Navigation:

- **#1** – zentraler Research-Design-/Arbeitsstand
- **#9** – Governance: Human-in-the-loop, wissenschaftliche Nachvollziehbarkeit, kein Wissensmonopol
- **#10** – Research Plan: State of the Art → Capabilities → Expertise Profiles → Konzept
- **#22** – Kompetenzlandkarte für Discovery, Requirements, Risiko, SOTA, Evaluation und Systemdesign
- **#23** – Issue-Governance: kanonische Ownership, Konsolidierung und Traceability

Fachlicher Scope / Qualitätsanforderungen:

- **#13** – Geschichte als transdisziplinäres Querschnittsthema / Expertise Routing
- **#14** – regional verankert, europäisch verflochten
- **#15** – Expertenmodell mit fachlicher Tiefe, Kontroversen und Unsicherheit
- **#16** – regionalisierte Spitzenexpertise
- **#19** – Assistenz-Ökosystem mit eigener Fachsprache, Begriffsmodellen und Methoden
- **#20** – harte Grenze Forschungszustand ↔ Vermittlung / mögliche Übergabe an RGK

Interne Prior-Art-Issues:

- **#12** – `paleo-type`
- **#21** – `rgk-main-ssot`

## Interne Referenzprojekte

### `paleo-type`

Internes Prior Art für Forschungsgovernance, Evidenz, Provenienz, Human-in-the-loop, Auditierbarkeit, consequence-based validation und technische Subsidiarität. Siehe #12.

### `rgk-main-ssot`

Internes Prior Art für relationale Modellmuster, Claim → Evidence → Interpretation, projektbezogene Quellenfunktionen, Abweichungslogik und die Trennung von wissenschaftlichem Zustand und Vermittlung. Siehe #21.

Beide Projekte werden als Prior Art geprüft; konkrete Schemas oder Architekturen werden **nicht automatisch** übernommen.

## Aktuelle Quellen-/Infrastrukturbedarfe und Hypothesen

- **#2** persönlicher Archivar – Spezialrolle/Basisfunktion, nicht Gesamtziel
- **#3** Zotero als bibliographische Kopplung – Hypothese
- **#4** OCR-/Volltexterschließung – validierter Bedarf, Lösung offen
- **#5** Volltextsuche / historische Query Expansion / fundstellenfähige Recherche – validierter Bedarf
- **#6** Git-/Provenienzprinzip – konkrete Datenarchitektur offen
- **#8** Automatisierung und KI-Unabhängigkeit – Zielvorgabe, Architektur offen

## Konsolidierte historische Issues

- **#7** superseded – Zielbild in #1/#13/#15/#19 aufgegangen
- **#11** completed – Concept-Audit-Snapshot
- **#17** superseded – Fachvokabular/Begriffsmodelle in #16/#19/#22 aufgegangen
- **#18** superseded – Expertise-/Method Packs in #10/#16/#19/#22 aufgegangen

Details zur kanonischen Ownership stehen in #23.

## Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Regionaler Fokus für Tiefenschärfe – europäischer Horizont für Erklärung.**

> **Technik dient der Forschung; sie definiert ihre wissenschaftlichen Standards nicht.**

> **Issues sind Arbeits- und Entscheidungseinheiten, keine parallelen Wahrheitsspeicher.**

> **Kein Wissensmonopol im Chat.**
