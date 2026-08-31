# Histo-Orla – Methodische Wissensbasis / Status- und Ownership-Karte

**Status:** `working-method-governance / v0.1`  
**Work Owner:** #60  
**Bindende Oberregeln:** `AGENTS.md`, #45, `docs/research/source-identity-protocol.md`  
**Accepted Requirements:** #42 / `docs/research/synthesis/requirements-baseline.md`  
**Stand:** 2026-08-31

## 1. Zweck

Diese Datei beantwortet eine einzige Governance-Frage:

> **Wo lebt welche Art methodischer Wahrheit – und welchen epistemischen Status besitzt sie?**

Sie verhindert, dass Vision, fachwissenschaftliche Methode, Arbeitsauftrag, Hypothese, Requirement, Architekturentscheidung und Prompt still miteinander verschmelzen.

Histo-Orla entwickelt gleichzeitig reale historische Forschung und ein Forschungssystem. Diese Ebenen dürfen sich gegenseitig informieren, aber nicht gegenseitig als Evidenz ersetzen.

---

## 2. Präzedenz der methodischen Wahrheit

Für methodische Fragen gilt innerhalb des Repositorys:

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

Wichtig:

- Eine ältere bindende Regel kann durch einen neueren **akzeptierten** methodischen Beschluss ersetzt werden; bloß jüngere Prosa besitzt nicht automatisch Vorrang.
- Case Learning darf generische Methodik challengen, wird aber nicht allein durch Formulierung zu bindender Methodik.
- Nutzerformulierungen beschreiben Erkenntnisinteresse, gewünschte Qualität und Pains. Sie sind kein Ersatz für die fachwissenschaftliche Operationalisierung.

---

## 3. Kanonische Orte und ihre Bedeutung

| Zustand | Kanonischer Owner / Ort | Bedeutung | Darf daraus unmittelbar Architektur folgen? |
|---|---|---|---|
| **Governance / wissenschaftliche Invarianten** | `AGENTS.md`, #9, #23, #45 | bindende Arbeits-/Evidenz-/Handoff-Regeln | nur über Requirements/Constraints |
| **Source-/Fundstellenmethode** | `docs/research/source-identity-protocol.md` unter #45 | bindender Umgang mit Quelle, Instanz, Derivat, Fundstelle, Zitation | nur soweit bereits Requirement/Constraint |
| **Vision / fachliches Zielniveau** | #16, #19 | beschreibt, welche Art Spitzenexpertise gewünscht und wissenschaftlich nötig ist | nein |
| **Kompetenzinventar / Routing-Scope** | #22 | welche Meta- und Fachkompetenzen grundsätzlich benötigt werden | nein |
| **Accepted Requirements** | #42 + `requirements-baseline.md` | verifizierbare Systemanforderungen; einzig kanonischer Ort für akzeptierte Requirements | ja, als Input für #48ff |
| **Domain Method Profile** | `docs/research/methods/` unter #60 | domänenspezifisch operationalisierte, SOTA-belegte Fachmethodik | zunächst Capability/Acceptance; Requirement nur nach Promotion |
| **Historical Work Owner** | #46/#47 etc. | Forschungsfrage, Scope, Status, nächste Arbeit, kurze Synthese | nein |
| **Historical Evidence/Findings** | jeweilige Case-Artefakte + Source Ledger/Exzerpte | Quellenbefund, Evidenz, Hypothesen, Synthese | nur indirekt als Requirement Evidence |
| **Method Candidate aus Live Case** | Case-Artefakt, explizit `candidate/working-method` | beobachtete Verbesserung/Friktion, die gegen #60/#45 geprüft werden muss | nein |
| **Architecture / Solution** | #48ff, Contracts, ADRs | technische Realisierung akzeptierter Needs/Requirements | bereits downstream |
| **Prompt** | Ausführungsartefakt / transient | Hilfsmittel zur Durchführung; keine wissenschaftliche Autorität | nein |

---

## 4. Status-Taxonomie – Begriffe nicht vermischen

### `vision`

Gewünschte Forschungsfähigkeit, Qualitätsambition oder Nutzererlebnis.

Beispiel: „Das System soll wie ein Team regionaler Spitzenexpert:innen denken können.“

**Nicht:** konkrete Methode, historische Hypothese oder Requirement.

### `work_order`

Konkreter Auftrag, der Forschung oder Validierung erzeugen soll.

Mindestform:

```text
question / objective
owner
inputs
method / quality frame
outputs
scope / exclusions
dependencies
Definition of Done
```

Ein Work Order besitzt keinen Wahrheitswert über seinen Gegenstand.

### `observation`

Quellen-/materialnah erhobenes Merkmal mit Fundstellenbezug. Muss zwischen source-explicit, editorial-explicit, source-structural usw. unterscheiden können.

### `finding`

Durch eine benannte Fachmethode aus Evidenz gestützter Forschungsbefund. Enthält Geltungsbereich und Grenzen.

### `historical_hypothesis`

Falsifizierbare historische Erklärung oder Beziehungshypothese.

Muss mindestens besitzen:

```text
hypothesis
supporting observations
competing explanations
what would strengthen it
what would weaken/falsify it
scope
status
```

### `method_hypothesis`

Annahme darüber, welches fachwissenschaftliche Vorgehen für einen Problemtyp angemessen ist. Muss gegen Methoden-SOTA und reale Cases geprüft werden.

### `system/solution_hypothesis`

Annahme darüber, wie eine Capability technisch/organisatorisch umgesetzt werden könnte. Gehört nicht in den fachlichen Wahrheitskern.

### `requirement_candidate`

Aus beobachtetem Need/Pain/Finding abgeleiteter möglicher Systembedarf. Noch nicht akzeptiert.

### `accepted_requirement`

Nur ein im Requirements-Owner #42 akzeptierter, tracebarer und prüfbarer Systembedarf.

### `architecture_choice / ADR`

Entscheidung über technische Umsetzung unter #48ff. Darf wissenschaftliche Methode nicht neu definieren.

### `prompt`

Austauschbarer Ausführungsmechanismus. Ein Prompt kann eine bereits definierte Methode operational ausführen helfen; er **ist nicht die Methode**.

---

## 5. Was derzeit wirklich bindende Methodik ist

Aktuell bindend/canonical:

1. `AGENTS.md` – Repository-/Handoff-/Präzedenzregeln.
2. #45 – gemeinsamer Research-/Evidence-Rahmen: Domain/Evidence/Inference/Terminology/Provenance/Falsification fit, Search Boundaries, Sättigung, Evidenzstatus.
3. `docs/research/source-identity-protocol.md` – Quellen-/Instanz-/Fundstellen-/Digitalisat-/Zitiertrennung.
4. #42 – akzeptierte wissenschaftliche Systemanforderungen, insbesondere `REQ-EPI-001`: consequential analysis benötigt nachvollziehbare führende Domänen, domänenspezifische Methoden, Evidenzmaßstäbe und zulässige Schlussarten; ein Rollenprompt ist ausdrücklich kein Beleg fachlicher Expertise.

Noch **nicht** ausreichend als generische bindende Methodik operationalisiert:

- die vollständigen methodischen Playbooks der einzelnen historischen Fachdomänen;
- die genaue Ersterschließungsmethode je Quellengattung über den gemeinsamen Kern hinaus;
- die domänenspezifischen Stop-/Falsifikations-/Negativbefundregeln für alle priorisierten Disziplinen;
- die konkrete Evidence Appetite / Search Vocabulary / SOTA-Bibliographie je Fach.

Diese Lücke ist Work Scope von #60.

---

## 6. Status bestehender strategischer und Live-Research-Artefakte

### #16 / #19

**Status:** `vision / strategic requirement source`.

Sie definieren mit großer fachlicher Schärfe das Zielniveau: eigene Fachsprache, Begriffsmodelle, Quellenwelten, Methoden, Forschungsstand, Regionalisierung und transdisziplinäre Schnittstellen. Sie sind jedoch **keine fertigen Domain Method Profiles**.

### #22

**Status:** `competence map / research workframe`.

#22 beantwortet „Welche Kompetenzen müssen vorhanden sein?“. Es ersetzt nicht die Frage „Wie arbeitet diese konkrete Fachkompetenz an diesem Quellentyp methodisch korrekt?“.

### #45

**Status:** `binding cross-cutting research protocol`.

#45 gibt gemeinsame wissenschaftliche Mindestregeln vor. Es soll nicht die Methodik sämtlicher Fachdisziplinen vereinheitlichen.

### #46 / #47

**Status:** `live historical research + method stress cases`.

Dort entstehen reale Findings und methodische Friktionen. Neue methodische Schemata in Case-Dokumenten sind solange `working/candidate`, bis sie über #60 oder #45 generalisiert/promoted wurden.

Insbesondere:

- `u2-transdisziplinaere-rekonstruktionsmatrix.md` = **case-derived method extension / candidate**, kein generischer Pflichtstandard.
- `u2-quellenerschliessung-sota-best-practice.md` = **SOTA-backed working method candidate** für quellenzentrierte modulare Erschließung; muss in #60 domänenspezifisch getestet werden.

---

## 7. Schutz vor „KI-Sumpf“

Ein Artefakt ist wissenschaftlich verdächtig, wenn es hauptsächlich aus plausibel klingenden Kategorien besteht, aber nicht beantworten kann:

- welche Fachtradition/Methode diese Kategorien begründet;
- für welchen Problem-/Quellentyp sie gelten;
- welche maßgebliche Literatur/Standards sie tragen;
- welche Evidenz ein Fach für welchen Schluss benötigt;
- welche Schlüsse ausdrücklich verboten sind;
- wodurch das Vorgehen falsifiziert oder als unzureichend erkannt wird;
- wie es an einer realen Quelle getestet wurde;
- welche Teile deterministische Regeln, fachliches Urteil oder bloße AI-Heuristik sind.

Solche Artefakte dürfen höchstens `method_hypothesis` oder `working-candidate` sein.

**Sprachliche Plausibilität ist kein Methodennachweis.**

---

## 8. Domain Method Profiles – die fehlende Operationalisierung

Der operative Methodenweg lautet künftig:

```text
#16/#19 Vision
    ↓
#22 relevante Kompetenz identifizieren
    ↓
#60 Domain Method Profile aus fachlichem SOTA erarbeiten
    ↓
#45 cross-cutting Qualitäts-/Provenienzregeln anwenden
    ↓
#46/#47 an echten Quellen/Befunden testen
    ↓
adopt | adapt | reject | remain-case-specific
    ↓
Capability-/Acceptance-Delta
    ↓
falls generalisierbar: Requirement Candidate → #42
    ↓
falls akzeptiert: Architektur #48ff
```

Damit ist Fachmethodik eine eigene Schicht zwischen „Kompetenz benennen“ und „System bauen“.

---

## 9. Priorität

#60 beginnt mit den tatsächlich benötigten Profilen der Live-Forschung. Kein Versuch, vorab eine Enzyklopädie aller historischen Methoden zu erstellen.

Erste Priorität:

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. anschließend problemgetrieben Herrschaft/Recht/Sozialstruktur, Kirche/Kloster/Orden/Memoria, Prosopographie/Netzwerke, Familie/Gender/Besitz, Wirtschaft/Ressourcen, Raum/Archäologie;
5. für U1 parallel die tatsächlich aktivierten Landschafts-/Umwelt-/Hydrologie-/Kartographieprofile.

Die Reihenfolge kann durch neue discriminating findings aus #46/#47 geändert werden.

---

## 10. Leitregel

> **Die Vision sagt, was für Forschung wir ermöglichen wollen. Die Fachwissenschaft sagt, wie man dafür methodisch arbeitet. Requirements machen den notwendigen Systembedarf prüfbar. Architektur entscheidet erst danach, wie er technisch realisiert wird.**
