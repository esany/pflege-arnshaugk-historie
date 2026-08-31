# Histo-Orla – Methodische Wissensbasis / Status- und Ownership-Karte

**Status:** `working-method-governance / v0.1`  
**Work Owner:** #60  
**Bindende Oberregeln:** `AGENTS.md`, #45, `docs/research/source-identity-protocol.md`  
**Accepted Requirements:** #42 / `requirements-baseline.md` + `requirements-extensions.md`  
**Stand:** 2026-08-31

## 1. Zweck

Diese Datei beantwortet:

> **Wo lebt welche Art methodischer Wahrheit – und welchen epistemischen Status besitzt sie?**

Sie verhindert, dass Vision, fachwissenschaftliche Methode, Arbeitsauftrag, Hypothese, Requirement, Architekturentscheidung und Prompt still miteinander verschmelzen.

## 2. Präzedenz der methodischen Wahrheit

```text
bindende Research-Governance / akzeptierte Requirements
→ validierte domänenspezifische Method Profiles
→ bindender cross-cutting Research-/Source-Identity-Rahmen
→ working-method / SOTA-backed method candidates
→ case-spezifische methodische Adaptionen und Hypothesen
→ strategische Vision / Kompetenzlandkarte
→ technische Lösungshypothesen
→ Prompts / Chat / Modellwissen
```

Case Learning darf generische Methodik challengen, wird aber nicht allein durch Formulierung zu bindender Methodik. Nutzerformulierungen definieren Erkenntnisinteresse, Qualitätsanspruch und Needs, nicht automatisch die fachwissenschaftliche Operationalisierung.

## 3. Kanonische Orte

| Zustand | Kanonischer Owner / Ort | Bedeutung |
|---|---|---|
| Governance / wissenschaftliche Invarianten | `AGENTS.md`, #9, #23, #45 | bindende Arbeits-/Evidenz-/Handoff-Regeln |
| Source-/Fundstellenmethode | `docs/research/source-identity-protocol.md` | bindender Umgang mit Quelle, Instanz, Derivat, Fundstelle |
| Vision / fachliches Zielniveau | #16, #19 | gewünschte Forschungsfähigkeit / Spitzenexpertise |
| Kompetenzinventar | #22 | welche Kompetenzen benötigt werden |
| Accepted Requirements | #42 + `requirements-baseline.md` + `requirements-extensions.md` | was das System leisten muss |
| Domain Method Profile | `docs/research/methods/` unter #60 | SOTA-belegte domänenspezifische Fachmethodik |
| Historical Work Owner | #46/#47 etc. | Forschungsfrage, Scope, Status, nächste Arbeit |
| Historical Evidence/Findings | Case-Artefakte + Source Ledger/Exzerpte | Quellenbefund, Evidenz, Hypothesen, Synthese |
| Method Candidate aus Live Case | Case-Artefakt, explizit `candidate/working-method` | gegen #60/#45 zu prüfende methodische Friktion/Verbesserung |
| Architecture / Solution | #48ff, Contracts, ADRs | technische Realisierung akzeptierter Requirements |
| Prompt | transient | Ausführungshilfe, keine wissenschaftliche Autorität |

## 4. Status-Taxonomie

### `vision`
Gewünschte Forschungsfähigkeit oder Qualitätsambition. Keine konkrete Methode oder Requirement.

### `work_order`
Konkreter Forschungs-/Validierungsauftrag mit Frage, Owner, Inputs, Method/Quality Frame, Scope, Outputs, Dependencies und DoD.

### `observation`
Quellen-/materialnahes Merkmal mit Fundstellenbezug.

### `finding`
Durch benannte Fachmethode aus Evidenz gestützter Befund mit Geltungsbereich und Grenzen.

### `historical_hypothesis`
Falsifizierbare historische Erklärung oder Beziehungshypothese mit supporting observations, competing explanations und Falsifikationsbedingungen.

### `method_hypothesis`
Zu prüfende Annahme über fachwissenschaftliches Vorgehen.

### `system/solution_hypothesis`
Zu prüfende technische/organisatorische Lösungsidee.

### `requirement_candidate`
Aus Need/Pain/Finding abgeleiteter möglicher Systembedarf, noch nicht akzeptiert.

### `accepted_requirement`
Nur ein im Requirements-Owner #42 akzeptierter, tracebarer und prüfbarer Systembedarf.

### `architecture_choice / ADR`
Technische Entscheidung unter #48ff; darf wissenschaftliche Methode nicht neu definieren.

### `prompt`
Austauschbarer Ausführungsmechanismus; kann Methode unterstützen, ist aber nicht die Methode.

## 5. Was derzeit bindend ist

1. `AGENTS.md` – Repository-/Handoff-/Präzedenzregeln.
2. #45 – cross-cutting Research-/Evidence-Rahmen.
3. `source-identity-protocol.md` – Quellen-/Instanz-/Fundstellen-/Digitalisat-/Zitiertrennung.
4. #42 – akzeptierte Systemanforderungen, einschließlich `REQ-EPI-001` sowie der neuen Method-/Research-Extensions in `requirements-extensions.md`.

Noch nicht ausreichend als generische Fachmethodik operationalisiert sind die konkreten Playbooks, Inferenzregeln, Evidence Appetite, fachlichen Stop-/Falsifikationsregeln und SOTA-Bibliographien der priorisierten Disziplinen. Diese Lücke ist Scope von #60.

## 6. Status bestehender strategischer und Live-Artefakte

- #16/#19 = `vision / strategic requirement source`.
- #22 = `competence map / research workframe`.
- #45 = `binding cross-cutting research protocol`.
- #46/#47 = `live historical research + method stress cases`.
- `u2-transdisziplinaere-rekonstruktionsmatrix.md` = case-derived method extension / candidate.
- `u2-quellenerschliessung-sota-best-practice.md` = SOTA-backed working method candidate; in #60 domänenspezifisch zu prüfen.

## 7. Schutz vor KI-Sumpf

Eine Methode ist höchstens Hypothese/Candidate, wenn sie nicht beantworten kann:

- welche Fachtradition/Methode sie begründet;
- für welchen Problem-/Quellentyp sie gilt;
- welche maßgebliche Literatur/Standards sie tragen;
- welche Evidenz für welchen Schluss benötigt wird;
- welche Schlüsse verboten sind;
- wodurch sie falsifiziert/als unzureichend erkannt wird;
- wie sie an realen Quellen getestet wurde;
- welche Teile Regel, Spezialalgorithmus, Fachurteil oder AI-Heuristik sind.

**Sprachliche Plausibilität ist kein Methodennachweis.**

## 8. Operativer Methodenweg

```text
#16/#19 Vision
    ↓
#22 relevante Kompetenz
    ↓
#60 Domain Method Profile aus fachlichem SOTA
    ↓
#45 Qualitäts-/Provenienzregeln
    ↓
#46/#47 reale Quellen-/Befundtests
    ↓
adopt | adapt | reject | remain-case-specific
    ↓
Requirement-/Acceptance-Delta
    ↓
falls akzeptiert: #42 Requirements
    ↓
#48/#59 technische Umsetzung / Verification
```

Damit ist Fachmethodik die Mittelschicht zwischen Kompetenzinventar und technischer Umsetzung; sie ist keine separate Produktphase.

## 9. Priorität

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. anschließend problemgetrieben Herrschaft/Recht/Sozialstruktur, Kirche/Kloster/Orden/Memoria, Prosopographie/Netzwerke, Familie/Gender/Besitz, Wirtschaft/Ressourcen, Raum/Archäologie;
5. für U1 parallel die tatsächlich aktivierten Landschafts-/Umwelt-/Hydrologie-/Kartographieprofile.

## 10. Leitregel

> **Die Vision sagt, was für Forschung wir ermöglichen wollen. Die Fachwissenschaft sagt, wie man dafür methodisch arbeitet. Requirements machen den notwendigen Systembedarf prüfbar. Technik realisiert ihn mit möglichst einfachen, hochwertigen Mitteln.**
