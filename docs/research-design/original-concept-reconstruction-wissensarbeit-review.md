# Histo-Orla – Rekonstruktion des ursprünglichen Zielbilds mit `Wissensarbeit` als Prüflinse

**Status:** `review-synthesis / candidate / no requirement or architecture authority`  
**Work Owner:** #65  
**Datum:** 2026-09-03  
**Scope:** Produkt-/Research-Design-Rekonstruktion; keine historische Forschungsaussage, keine Requirement-Promotion, keine Architekturentscheidung  
**Präzedenz:** Governance + #42 accepted Requirements + #60 Domain Method Truth + getroffene ADRs > dieses Review-Artefakt

## 1. Zweck

Dieses Artefakt rekonstruiert aus dem kontrollierten Repository-Zustand, welches ursprüngliche Produkt- und Forschungsziel hinter Histo-Orla erkennbar ist und wie die inzwischen in `esany/Wissensarbeit` formalisierten Konzepte helfen, dieses Ziel präziser zu beschreiben.

Es beantwortet insbesondere vier Fragen:

1. Was war der ursprüngliche fachliche und nutzerbezogene Kern von Histo-Orla, bevor ein großer Teil der Arbeit in Requirements-, Governance-, Research-State- und Assurance-Strukturen ausdifferenziert wurde?
2. Welche frühen Konzepte sind im heutigen akzeptierten Requirements-State bereits erhalten?
3. Welche Punkte aus #65 sind tatsächlich neue bzw. geschärfte Kandidaten und welche sind nur eine neue Formulierung bereits akzeptierter Anforderungen?
4. Welche Konzepte aus `Wissensarbeit` klären die Betriebsform, ohne Histo-Orla zu einem generischen Framework, Multi-Agent-System oder Technikprojekt umzudeuten?

## 2. Rekonstruktionsmethode und Evidenzgrenzen

Dies ist **keine Wiederherstellung eines verlorenen Chats** und kein Anspruch auf den exakten zeitlichen Wortlaut jeder frühen Idee. Rekonstruiert wird aus persistierter Repo-Evidenz.

Verwendete Evidenzklassen:

### A. Aktuell bindender Histo-Orla-Zustand

- Root `AGENTS.md`, `PROJECT_STATE.md`, `README.md`;
- #42 und die akzeptierten Requirements-Artefakte;
- aktueller Technical-Prior-Art-Stand unter `docs/architecture/prior-art-development-inputs.md`;
- aktueller Pilot-Review-Owner #65.

Diese Ebene entscheidet, was **heute** bereits accepted bzw. bindend ist.

### B. Frühe/foundational Histo-Orla-Zielbilder

Besonders aussagekräftig sind:

- #2 – persönlicher Archivar als Quellen-/Bestands-/Fundstellen-Spezialist;
- #7 – frühes langfristiges Ziel einer transdisziplinären Forschungsassistenz, inzwischen superseded, Zielidee aber ausdrücklich erhalten;
- #13 – Geschichte als transdisziplinäres Querschnittsthema und dynamisches Expertise-Routing;
- #14 – regionale Tiefenschärfe bei transregionaler/europäischer Verflechtung und Scale Expansion;
- #16 – regionalisierte Spitzenexpertise mit Fachsprache, Begriffsmodellen, Quellenwelten, Methodik, Forschungsstand und Kontroversen;
- #19 – Assistenz-Ökosystem aus Research Owner, Coordinator und fachlich eigenständigen Spezialkompetenzen; technische Umsetzung ausdrücklich offen;
- `docs/research-design/transdisziplinaerer-literaturassistent.md` als foundational human-readable design document.

Diese Ebene dient der Rekonstruktion der **ursprünglichen Intention**, ist aber der akzeptierten heutigen Requirements-Basis nachgeordnet.

### C. `Wissensarbeit` als externe Prüflinse

`esany/Wissensarbeit` ist kein semantischer Owner von Histo-Orla. Relevant sind dort insbesondere:

- `project/GOVERNING_OBJECTIVE.md`;
- `project/requirements.json`;
- `system/competence.json`;
- `system/building_blocks.json`;
- `system/authority.json`;
- `project/conversation_harvest_foundation_v1.json`;
- `pilots/generic-pilot-learnings/pilot-closure.md`.

`Wissensarbeit` hilft vor allem dabei, **Capabilities, Kompetenzen, Authority, Systemintegration und Projektbetrieb** sauber zu benennen. Projektspezifische Historiker-, Quellen- und Forschungssemantik bleibt Histo-Orla-eigen.

## 3. Rekonstruiertes ursprüngliches Zielbild

### 3.1 Ausgangspunkt: ein aktiver Forschungsbegleiter, kein Ablagesystem

Der erkennbare Ursprung ist ein persönlicher Forschungsassistent für einen fachlich interessierten Research Owner, der nicht voraussetzen darf, dass der Nutzer bereits die richtige Fachdisziplin, Terminologie, Quellengattung oder Methode kennt.

Der persönliche Archivar war ein wichtiger früher Einstiegspunkt, wurde aber sehr schnell als **eine Spezialkompetenz** relativiert. #2 begrenzt seine Aufgabe auf Literatur-, Quellen-, Bestands-, Provenienz- und Fundstellenarbeit. #13/#16/#19 erweitern das Ziel auf ein transdisziplinäres Kompetenzsystem.

Damit ist das Ziel nicht:

> „Ich speichere Quellen und kann sie per Chat durchsuchen.“

Sondern eher:

> „Ich helfe dem Research Owner, aus einer unscharfen historischen Beobachtung eine fachlich präzise, quellenkritisch bearbeitbare Forschungsfrage zu machen, die richtigen Disziplinen und Methoden zu aktivieren, relevante Evidenz zu finden und zu prüfen, konkurrierende Erklärungen sichtbar zu halten und den nächsten sinnvollen Forschungsschritt zu bestimmen.“

Diese Formulierung ist eine **Rekonstruktion**, kein neues accepted Requirement.

### 3.2 Nutzer darf unsauber fragen; das System muss fachlich übersetzen

Ein zentraler ursprünglicher Produktwert ist die Übersetzung zwischen alltagssprachlichem Erkenntnisinteresse und fachwissenschaftlicher Problemstruktur.

Rekonstruierter Ablauf:

```text
Nutzerbeobachtung / unpräzise Frage
→ fachlich plausible Problemübersetzungen
→ fehlendes Vokabular / Begriffsmodelle sichtbar machen
→ diskriminierende Rückfragen
→ einschlägige Fachdomänen und Methoden bestimmen
→ fachtypische Quellen-/Evidence-Demands ableiten
→ Recherche und Quellenkritik
→ Findings / Alternativen / Unsicherheit
→ verständliche Rückübersetzung zum Research Owner
```

Das ist heute bereits stark in `REQ-EPI-002`, `REQ-EPI-003`, `REQ-EPI-001` sowie `REQ-RSCH-002` und den Domain-Method-Requirements abgebildet.

### 3.3 „Experten“ bedeuteten Kompetenz, nicht technische Agenten

Die frühen Begriffe „Fachassistent“, „Spezialist“, „Research Coordinator“ oder „Assistenz-Ökosystem“ beschreiben primär **fachliche Funktions- und Kompetenzgrenzen**.

#19 hält ausdrücklich offen, ob diese später technisch durch einzelne Agents, Rollenprofile, Retrieval-Kontexte, Tools oder andere Architekturen umgesetzt werden.

Der eigentliche Kompetenzbegriff ist wesentlich tiefer:

```text
Fachsprache / Terminologie
+ Begriffs- und Gegenstandsmodelle
+ Quellen- und Überlieferungslogik
+ Rechercheheuristiken
+ Methoden / Playbooks
+ Evidenz- und Inferenzregeln
+ Forschungsstand / Kontroversen
+ regionale und zeitliche Spezialisierung
+ transdisziplinäre Schnittstellen
```

`Wissensarbeit` schärft genau diese Trennung: seine Building Blocks sind **Capabilities, keine Pflicht-Agenten, Services oder Ordner**. Seine `competence.json` ergänzt außerdem die wichtige Kategorie der **Interface Competence** (`domain → data`, `domain → software`, `research → product`, `AI → domain`, `method → software`, `project → engineering`).

Daraus folgt als Rekonstruktion:

> Das ursprüngliche „Assistenz-Ökosystem“ sollte heute nicht als Multi-Agent-Zielbild gelesen werden. Es ist zuerst ein dynamisch komponierbares Kompetenz- und Funktionsmodell. Die technische Instanziierung bleibt der Requirements-/Architecture-Derivation untergeordnet.

### 3.4 Research Coordinator: Orchestrierung ohne epistemische Oberinstanz

Die ursprüngliche Coordinator-Idee lässt sich mit `Wissensarbeit` präziser fassen.

Der Coordinator muss nicht „der klügste Agent“ sein. Seine Funktion ist eher die Komposition von:

- Problem-/Intent-Verständnis;
- Context Compilation;
- Competence Discovery;
- fachlicher Problemübersetzung;
- Evidence-Demand-/Method-Routing;
- Integration neuer Ergebnisse gegen bestehenden Research State;
- Sichtbarmachung von Konflikten, Lücken und offenen Entscheidungen;
- Rückübersetzung in eine owner-lesbare Forschungsansicht.

Damit ist Orchestrierung eine **Support- und Integrationsfunktion**, keine neue fachliche Authority.

### 3.5 Regionale Spitzenexpertise und Multi-Scale-Erklärung

Histo-Orla war von Anfang an nicht als generische „Geschichts-KI“ angelegt. #14/#16 zeigen einen doppelten Anspruch:

1. hohe regionale Tiefenschärfe – Quellenlandschaften, Institutionen, Herrschaftsräume, Terminologien, Forschungstraditionen und Archive konkret kennen;
2. überregionale Anschlussfähigkeit – lokale Befunde bei Bedarf in Reichs-, Hof-, Universitäts-, Ordens-, Reise-, Kriegs-, Wirtschafts- und europäische Verflechtungen einordnen.

Die Region ist damit **Anker, nicht Container**.

Der Assistent soll den Maßstabswechsel selbst als möglichen methodischen Bedarf erkennen können, ohne aus räumlicher Nähe automatisch historische Relation zu machen. Diese Intention lebt heute u. a. in `REQ-SPAT-001`, `REQ-REL-001`, `REQ-ACT-001` und `REQ-SYN-001/002` weiter.

### 3.6 Quellenkritische Forschungsbasis und epistemisch getrennte Ebenen

Der frühe Wunsch nach Fundstellen, Quellen, OCR und Literatur war nicht bloß eine Retrieval-Funktion. Er sollte eine belastbare Basis schaffen, auf der historische Deutung überhaupt möglich ist.

Heute ist diese Intention wesentlich präziser formalisiert:

- Source Identity ≠ Repräsentation ≠ inspizierte Instanz ≠ Derivat;
- Findspot bleibt rekonstruierbar;
- OCR/HTR bleibt Derivat;
- Beobachtung/Finding/Claim/Interpretation/Hypothese bleiben unterscheidbar;
- Unsicherheit, Widerspruch, konkurrierende Interpretation und Evidence Gap sind gültige Zustände;
- unterschiedliche Evidenzachsen werden nicht flattenend zusammengezogen;
- AI-Ausgabe ist weder Evidenz noch unabhängige Fachvalidierung.

#65 formuliert daraus die hilfreiche Dreiteilung:

```text
Forschungsbasis
→ aktuelle Forschungsfragen / Hypothesen / Falsifikation
→ spätere Module / Produkte / Views
```

Diese Dreiteilung ist als Produkt-/Design-Linse sehr nah an der ursprünglichen Intention: **die Forschungsbasis soll länger leben als die jeweils aktuelle Frage**.

### 3.7 Transdisziplinäre Synthese heißt Differenzen erhalten

Die ursprüngliche Ambition war nicht, mehrere Fachantworten zu sammeln und durch einen Meta-Agenten zu einer einheitlichen Antwort zu glätten.

Transdisziplinäre Integration sollte sichtbar halten:

- welche Fachperspektive welche Frage beantwortet;
- welche Begriffe nicht deckungsgleich sind;
- welche Quellen-/Evidenztypen unterschiedlich belastbar sind;
- wo Methoden unterschiedliche Ergebnisse erzeugen;
- welche Erklärungen konkurrieren oder inkommensurabel bleiben;
- wo zusätzliche Expertise oder neue Evidenz nötig ist.

`Wissensarbeit` liefert hierfür eine nützliche **Integrationssprache**, die sich auf Research-State-Änderungen übertragen lässt, ohne neue Method Truth zu erzeugen:

`fuse | refine | reframe | supersede | conflict | reject | defer`

Für historische Forschung ist dies nur Review-Vokabular. Es ersetzt keine quellenkritische oder fachwissenschaftliche Begründung. Der Nutzen liegt darin, append-only Wissenswachstum und stilles Überschreiben zu vermeiden.

### 3.8 Der Assistent sollte aktiv forschen helfen, nicht nur Zustand verwalten

#65 macht einen Punkt wieder besonders sichtbar, der in der heutigen Governance-/State-Struktur weniger prominent erscheint, aber zum ursprünglichen Zielbild passt: **aktive wissenschaftliche Assistenz**.

Dazu gehören als Kandidaten:

- nächste Recherche-/Prüfschritte vorschlagen;
- Hypothesen und Gegenhypothesen explizit erzeugen;
- fehlende Evidenz und Widersprüche markieren;
- alternative Erklärungsräume aufspannen;
- Falsifikationsmöglichkeiten vorschlagen;
- offene Fragen nach Informationsgewinn priorisieren;
- owner-lesbare Research-/Decision-Briefs erzeugen.

Wichtig ist die epistemische Trennung:

```text
Vorschlag ≠ Finding
Hypothese ≠ Evidenz
Plausibilität ≠ Validierung
AI-Konsens ≠ unabhängige Fachprüfung
```

Diese Aktivität ist nicht dasselbe wie autonome Promotion. Das System darf proaktiv **denken helfen**, ohne selbst fachliche Wahrheit zu autorisieren.

### 3.9 Human-in-the-loop, aber nicht Human-as-Workflow-Engine

Der ursprüngliche Wunsch nach Transparenz und Owner-Steuerung ist mit `Wissensarbeit` besser operationalisierbar:

- mechanische und wiederkehrende Arbeit maximal automatisieren;
- Context Compilation, Routineklassifikation, Validierung, Ableitungen und Repository-Hygiene nicht dem Owner aufbürden;
- den Menschen dort einbeziehen, wo Bedeutung, Priorität, Forschungsrichtung, Risiko oder irreversible Konsequenz materiell sind;
- Fachvalidierung dort von Owner-Akzeptanz unterscheiden, wo specialist authority nötig ist.

Das passt zu `REQ-UX-002`: challenge/correct/demote soll möglich sein, ohne Routine-Micromanagement.

### 3.10 Forschungszustand ist nicht Vermittlungsprodukt

Ein früher Kommentar zu #19 hält bereits fest:

```text
Quellen / Befunde / Evidenz
→ fachliche Einordnung / Claims / Unsicherheit / Relationen
→ kanonischer Forschungszustand
→ kontextabhängige Views / Vermittlung
```

Das ist heute durch `REQ-BND-001` und die State-/UX-Requirements teilweise formalisiert.

Für die Rekonstruktion bedeutet dies:

> Histo-Orla war als Forschungsumgebung gedacht, aus der verschiedene Research-, Audit-, Lern-, Explorations- oder spätere Vermittlungsansichten abgeleitet werden können. Die Ansicht ist nicht die Wahrheitsschicht.

## 4. Rekonstruierter Kernworkflow

Aus frühen Histo-Orla-Zielbildern und der saubereren Betriebssemantik von `Wissensarbeit` ergibt sich folgender **Produkt-/Research-Loop** als Rekonstruktionsmodell:

```text
1. Research Owner äußert Beobachtung, Frage, Pain oder Erkenntnisinteresse
      ↓
2. Fachliche Problemübersetzung
   - Begriffe / Gegenmodelle
   - historische vs. moderne Terminologie
   - diskriminierende Rückfragen
      ↓
3. Competence Discovery / Routing
   - führende Fachdomänen
   - Methoden
   - regionale / zeitliche Expertise
   - Interface Competence
      ↓
4. Evidence Demand
   - Quellengattungen
   - Archive / Bestände / Findmittel
   - Suchvokabular / Varianten
   - Vergleiche / Kontrollen / Falsifikation
      ↓
5. Quellen-/Literaturarbeit
   - Source / Instance / Findspot
   - OCR/HTR/Derivate
   - genaue Exzerpte / Provenienz
      ↓
6. Fachliche Analyse
   - Observations / Findings / Claims
   - Relationen / Proxy-Befunde
   - Interpretationen
   - Hypothesen / Gegenhypothesen
   - Unsicherheit / Konflikt / Evidence Gaps
      ↓
7. Transdisziplinäre Integration
   - Perspektiven getrennt halten
   - neue Aspekte gegen bestehenden State prüfen
   - fuse/refine/reframe/conflict/defer/... nur als Integrationsdisposition
      ↓
8. Aktive Research Guidance
   - nächste diskriminierende Prüfung
   - Rechercheprioritäten
   - Falsifikationsvorschläge
   - benötigte zusätzliche Kompetenz
      ↓
9. Owner-lesbare Synthese / Research Brief
   - Kernaussage
   - Evidenz
   - Alternativen / Unsicherheit
   - offene Entscheidungen
      ↓
10. Persistierter Research State + Research History
      ↓
11. Derived Views / spätere Module
      ↓
12. reale Nutzung / Feedback / neue Frage → zurück in den Loop
```

Dieses Modell ist **kein neuer Lifecycle und keine technische Workflow Engine**. Es ist eine Rekonstruktion dessen, welches nutzbare Gesamtverhalten die bereits getrennten Capabilities gemeinsam ermöglichen sollten.

## 5. Abgleich gegen den heutigen accepted State

| Rekonstruiertes Element | Heutige Abdeckung | Review-Befund |
|---|---|---|
| Nutzerfrage → fachliche Problemübersetzung | `REQ-EPI-002/003` | **accepted / stark abgedeckt** |
| dynamisches Fach-/Methodenrouting | `REQ-EPI-001`, `REQ-MTH-001/002`, `REQ-RSCH-002/004` | **accepted / stark abgedeckt** |
| persönlicher Archivar als Spezialkompetenz | #2 + Source-/Retrieval-Requirements | **designseitig erhalten; keine Oberrolle** |
| regionale Tiefe + Scale Expansion | `REQ-SPAT-001`, `REQ-REL-001`, #14/#16 | **accepted/präzisiert** |
| Source-/Instance-/Findspot-/Derivative-Treue | `REQ-SRC-*`, `REQ-OCR-*` | **accepted / stark abgedeckt** |
| Unsicherheit/Kontroverse/Hypothese | `REQ-EPI-004`, `REQ-RSCH-001/003/004` | **accepted / stark abgedeckt** |
| Motive/Handlung/Struktur trennen | `REQ-ACT-001` | **accepted** |
| Multi-Evidence / transdisziplinäre Synthese | `REQ-SYN-001/002` | **accepted** |
| Research Owner challenge/correct/demote | `REQ-UX-001/002/003` | **accepted** |
| Chat-/Provider-unabhängiger Research State | `REQ-STATE-001/002/003` | **accepted** |
| Forschungszustand ≠ Vermittlungsprodukt | `REQ-BND-001` + #19 Design | **accepted boundary, Produktmodell teilweise implizit** |
| Forschungsbasis ≠ aktuelle Frage ≠ spätere Module | #65 Candidate + bestehende State/Boundary-Regeln | **plausible Präzisierung; nicht als eigener accepted Dreischritt formalisiert** |
| aktive Vorschläge für nächste Forschungs-/Falsifikationsschritte | #65 Candidate; indirekt `REQ-RSCH-002`, Method Profiles | **ursprünglicher Produktwert sichtbar, aber als explizites Gesamtverhalten schwächer formalisiert** |
| Assistenz-Ökosystem = technische Multi-Agent-Architektur | explizit offen; `REQ-LEAN-001`; Wissensarbeit Building-Block-Prinzip | **nicht Requirement; technische Festlegung wäre Fehlrekonstruktion** |
| vier gekoppelte „Netze“ aus #65 | epistemische Trennungen accepted, technische Repräsentation offen | **fachliche Analyseoption; kein Graph-Entscheid** |

## 6. Disposition der #65-Kandidaten aus dieser Rekonstruktion

Diese Disposition ist **Review-Empfehlung**, keine Promotion.

### 6.1 Korrektur U2/Moxa/Knaus

**Disposition:** `remain research question / already case-owned`

Keine Systemableitung nötig. Die getrennte Führung und unresolved relation folgt bereits accepted epistemischen Regeln.

### 6.2 Forschungsbasis / aktuelle Fragen / spätere Module

**Disposition:** `refine → adopt as product/research-design invariant candidate`

Begründung:

- entspricht dem frühen Prinzip Research State ≠ Vermittlung;
- schützt vor Pilot-/Question Overfitting;
- ist mit `REQ-STATE-*` und `REQ-BND-001` kompatibel;
- kann helfen, die Produktintention lesbarer zu machen.

**Noch nicht ableiten:** neues Datenmodell, Modulframework oder Storage-Layer.

**Prüfpfad:** #42 nur dann als Requirement Delta, wenn reale Research-/Product-Acceptance zeigt, dass bestehende Requirements diese Trennung nicht ausreichend erzwingen.

### 6.3 Heterogene Evidenzarten

**Disposition:** `adopt principle / refine through real fixtures`

`REQ-SYN-001` trägt bereits unterschiedliche Evidenzachsen und eigene Methoden/Aussagegrenzen. Die in #65 genannten Typen – Karten, Fotos, Kunstobjekte, Münzen, Bau-/Dendro-Gutachten, quantitative Daten – sollten nicht vorschnell zu einer Universalontologie werden.

Jede neue Evidenzart wird besser über reale Research-Fälle, fachliche Methode und benötigte Source-/Findspot-/Measurement-Semantik admissioniert.

### 6.4 Gekoppelte Quellen-/Aussage-/Domänenwissen-/Hypothesennetze

**Disposition:** `refine concept / defer technical representation`

Der fachliche Kern ist sinnvoll: Provenienz, Aussagen, Domänenbegriffe und Hypothesen erfüllen unterschiedliche epistemische Funktionen und dürfen nicht still verschmolzen werden.

**Nicht daraus ableiten:** Knowledge Graph, Graphdatenbank, universelles Relationenschema oder vier physisch getrennte Stores.

Die accepted Requirements decken viele Trennungen bereits ab; Architektur bleibt unter `REQ-LEAN-001` und #48 evidenzpflichtig.

### 6.5 Aktive wissenschaftliche Assistenz

**Disposition:** `adopt as high-value product-behavior candidate / requirement-gap check recommended`

Dies ist der wichtigste zusätzliche Befund dieser Rekonstruktion.

Die heutigen Requirements sichern sehr gut **Integrität, Fachrouting, Methoden, Evidenz, State und Review**. Weniger explizit ist das zusammengesetzte Produktverhalten:

> Das System soll aus dem aktuellen Research State und den aktivierten Fachmethoden proaktiv die nächsten wissenschaftlich sinnvollen, diskriminierenden Recherche-, Prüf- oder Falsifikationsschritte vorschlagen können.

Vor einer Requirement-Promotion sollte #42 prüfen, ob dies bereits hinreichend aus `REQ-RSCH-002`, `REQ-MTH-002`, `REQ-SYN-*` und `REQ-UX-*` folgt oder ob ein expliziter Delta nötig ist.

Ein möglicher Acceptance-Frame – **noch kein Requirement** – wäre:

- aus einer realen U1/U2-Frage werden relevante Fachdomänen/Methoden nachvollziehbar aktiviert;
- der Assistant leitet daraus konkrete Evidence Demands und nächste Prüfhandlungen ab;
- Hypothesen und Gegenhypothesen sind als solche markiert;
- mindestens eine vorgeschlagene Aktion ist auf erwarteten Informations-/Diskriminierungsgewinn begründet;
- offene Widersprüche/Alternativen bleiben erhalten;
- der Owner kann verstehen, warum ein Schritt vorgeschlagen wird, ohne den Workflow manuell koordinieren zu müssen;
- kein Vorschlag wird dadurch automatisch zu Finding, Requirement oder Decision.

### 6.6 Epistemische/provenancebezogene Grundlage für spätere Module

**Disposition:** `adopt / predominantly already accepted`

Source-/Instance-/Findspot-Treue, semantische Zustände, Unsicherheit, Derivat-Parentage und transdisziplinäre Nicht-Glättung sind heute bereits umfangreich accepted. Hier sollte #65 eher auf bestehende Requirements referenzieren als eine parallele Requirement-Schicht erzeugen.

### 6.7 Wissensarbeit-Mechaniken

**Disposition:** `already integrated as technical prior art / no new Histo-Orla semantics`

Insbesondere nützlich:

- Human-in-the-loop, not human-as-workflow-engine;
- Capabilities statt Agent-/Service-Proliferation;
- Competence + Interface Competence;
- systemic integration before append;
- deterministic/procedural/judgement Trennung;
- lossless-by-reference Context Compilation;
- Conversation Harvesting;
- Use/Learn und kontrollierte Promotion.

Diese Punkte sind bereits in `docs/architecture/prior-art-development-inputs.md` eingeordnet. Sie legitimieren keine neue Architektur von selbst.

## 7. Wo der heutige Repo-Zustand die ursprüngliche Idee verdecken kann

#64 beschreibt bereits das aktuelle Hauptrisiko: Nicht fehlende Governance, sondern Governance-/Operationalisierungs-Komplexität kann den realen Research Value überholen.

Die Rekonstruktion verschärft diese Diagnose:

> Die heutigen State-, Requirement-, Assurance- und Architecture-Mechanismen sind **Schutz- und Betriebsinfrastruktur für den Forschungsassistenten**. Sie sind nicht selbst der Forschungsassistent.

Ein formal perfekter Research State ohne nutzbare fachliche Problemübersetzung, Competence Routing, Evidence Demand, aktive Research Guidance und owner-lesbare Synthese würde den ursprünglichen Produktzweck nicht erfüllen.

Umgekehrt darf die Rückkehr zur aktiven Assistenz die inzwischen gewonnenen wissenschaftlichen Schutzmechanismen nicht abschwächen.

Der geeignete Non-Regression-Frame ist daher:

```text
mehr aktive Assistenz
+ weniger Owner-Metaarbeit
+ gleiche oder bessere Quellen-/Methoden-/Provenienztreue
+ keine neue versteckte AI-Authority
```

## 8. Produkt-North-Star als Rekonstruktionssatz

Als **nicht-bindende Rekonstruktion** lässt sich der ursprüngliche Ansatz in einem Satz zusammenfassen:

> **Histo-Orla soll einen nicht-technischen, fachlich interessierten Research Owner wie ein transparentes, transdisziplinäres historisches Forschungsteam unterstützen: unsaubere Fragen fachlich übersetzen, benötigte Kompetenzen und Methoden aktivieren, Quellen und Evidenz quellenkritisch erschließen, regionale Tiefe mit überregionalen Verflechtungen verbinden, Befund/Hypothese/Interpretation und Unsicherheit sauber trennen, konkurrierende Erklärungen integrierbar erhalten und aktiv die nächsten sinnvollen Forschungs- und Falsifikationsschritte vorschlagen – während der dauerhafte Research State außerhalb des Chats auditierbar und restartbar bleibt.**

Dieser Satz ist **kein Ersatz** für #1/#42 und keine Requirement Truth. Sein Nutzen ist ein Prüfkriterium: Wenn eine technische oder Governance-Maßnahme hierzu keinen belegbaren Beitrag leistet oder den Research Owner stärker zum Workflow-Manager macht, muss ihre Projektpassung hinterfragt werden.

## 9. Empfohlene nächste Reviews unter bestehender Authority

1. **#65 / Product-Research Review:** diese Rekonstruktion als Review-Evidence prüfen; insbesondere „aktive wissenschaftliche Assistenz“ und „Forschungsbasis ≠ aktuelle Frage ≠ spätere Module“ dispositionieren.
2. **#42 Requirements:** nur bei bestätigter Lücke einen minimalen Requirement-Delta formulieren; keine neue Requirement-Schicht aus dem ganzen Dokument erzeugen.
3. **#60 Domain Method Truth:** prüfen, welche Art von Evidence Demand, Counterhypothesis/Falsification und Next-Step Guidance je Fachdomäne wissenschaftlich zulässig ist.
4. **#48 Technical Lead:** erst nach akzeptiertem Bedarf technische Komposition prüfen; Agents/Graph/RAG/DB bleiben Optionen, nicht Zielbild.
5. **#59/#63 Real Use:** einen vertikalen Research Slice daran messen, ob der Owner tatsächlich weniger Koordinationsarbeit leisten muss und schneller zu auditierbaren, methodisch belastbaren nächsten Erkenntnisschritten gelangt.

## 10. Handoff / Non-Regression

Dieses Review verändert bewusst **nicht**:

- accepted Requirements;
- Method Truth;
- Architecture Decisions;
- Delivery-Prioritäten;
- Source-/Research-State-Semantik;
- U1/U2 Research Findings.

Materialer neuer Befund dieses Reviews ist ausschließlich die rekonstruierte Produkt-/Research-Design-Sicht und die Dispositionsempfehlung für #65.

`PROJECT_STATE.md` benötigt dadurch zunächst kein Status-/Ownership-Delta, weil #65 dort bereits als offener Pilot-Review-Input geführt wird. Falls #65 später eine Requirement-/Method-/Architecture-Promotion auslöst, muss der jeweilige kanonische Owner den daraus folgenden State aktualisieren.
