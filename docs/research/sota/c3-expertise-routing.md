# C3 – Expertise Routing, fachliche Kompetenzprofile und Grenzen automatisierter Expertise

**Work Owner:** #33  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** historische Fachmethodik, Historiographie, Research Design, Research Integrity.  
**Controlling competencies:** Knowledge Organization, Human Factors, Information Retrieval, AI Evaluation; je konkreter Frage die einschlägige Fachdomäne selbst.

## 1. Research Questions

RQ-C3-01 bis RQ-C3-04:

1. Was macht operational belastbare historische Fachkompetenz aus?
2. Wie funktioniert problem-/source-/method-/validation-routing?
3. Woran lässt sich regionale Expertise belegen?
4. Wo endet KI-/Tool-Unterstützung und wo beginnt unabhängige Fachvalidierung?

## 2. Search Scope / Boundary

Geprüft wurden:

- disziplinäre Kompetenz-/Methodenbeschreibungen der American Historical Association (AHA);
- aktuelle Methodendiskussion zu historischen Methoden und domäneneigenen Bewertungsmaßstäben;
- Human-AI-Guidelines für Korrektur, Unsicherheit und Explainability;
- NIST GenAI Risk Management zur Confabulation/Vertrauensproblematik;
- C1/C2 als konkrete Fachstressfälle.

Nicht beansprucht wird eine vollständige Theorie professioneller Expertise oder bereits ein vollständiger Profile-Katalog aller Histo-Orla-Disziplinen.

## 3. Inspected sources

- American Historical Association, **History Discipline Core**: https://www.historians.org/resource/history-discipline-core/
- AHA, **2013 History Discipline Core**: https://www.historians.org/resource/2013-history-discipline-core/
- AHA, **Careers for History Majors: History Discipline Core**: https://www.historians.org/resource/careers-for-history-majors-history-discipline-core/
- Johannes Westberg, 2025, **Historical methods in educational research: sources, contextualisation, periodisation and analysis**: https://www.tandfonline.com/doi/full/10.1080/00309230.2025.2473704
- Microsoft Research, **Guidelines for Human-AI Interaction**: https://www.microsoft.com/en-us/research/?p=564561
- NIST, **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)**: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST AI 600-1 PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

## 4. Findings

### F-C3-01 – Fachkompetenz ist ein Bündel aus Praktiken, Evidenzurteilen und revisionsfähiger Argumentation, nicht ein Wissensetikett

Die AHA beschreibt historische Kompetenz als mehr als Faktenwissen: Informationen sammeln und kontextualisieren, Quellen nach credibility/position/perspective/relevance beurteilen, komplexes und widersprüchliches Material ordnen und interpretieren, mehrere Perspektiven und Ursachen aushalten, Argumente anderer Historiker:innen beurteilen und eigene Analysen bei neuer Evidenz revidieren. Professionelle Standards umfassen Peer Review, Citation und die Vorläufigkeit von Wissen.

Westbergs aktuelle Methodendiskussion verstärkt diesen Punkt: historische Forschung soll auf **ihren eigenen Begriffen und Qualitätsmaßstäben** beurteilt werden; source criticism, contextualisation, periodisation, historical analysis und disciplined reading sind nicht einfach durch generische qualitative Methodensprache ersetzbar.

**Implikation:** Ein Histo-Orla-Expertise Profile muss `knowledge + vocabulary + source logic + method + inference limits + controversy + evaluation` tragen. Ein Rollenprompt oder thematischer Retrieval-Filter ist nicht ausreichend.

### F-C3-02 – Der epistemische Owner einer Regel ist die Fachdomäne, nicht der Router

Research Coordination kann erkennen, dass z. B. ein Arnshaugk-Teichproblem Archivistik + historische Geographie + Agrar-/Umweltgeschichte braucht. Aber es darf nicht selbst definieren, was in Archivistik als belastbare Provenienz oder in Diplomatik als hinreichender Quellenstatus gilt.

Daraus folgt eine Ownership-Schichtung:

```text
Research Owner
→ besitzt Erkenntnisinteresse / normative Prioritäten

Research Coordinator
→ Problemzerlegung / Vocabulary Discovery / Routing / Integrationslogik

Leading Scholarly Competency
→ besitzt Fachbegriffe, Methoden, Evidenzmaßstab, zulässige Inferenz

Controlling / Neighbor Competency
→ kontrolliert Blind Spots an Fachgrenzen

Method / Tool Support
→ Retrieval, OCR, Software, KI, Strukturierung

Independent Expert Validation
→ separate epistemische Handlung bei consequential use
```

Der Router ist **Orchestrator, nicht epistemische Oberinstanz**.

### F-C3-03 – Routing braucht mehrere Achsen statt „welcher Agent?“

Aus U1–U4 ergeben sich mindestens vier Routing-Arten:

1. **Problem Routing:** Welche Disziplin(en) können die Frage fachlich überhaupt modellieren?
2. **Source Routing:** Wer kann die konkrete Quellengattung/Überlieferungsstufe methodisch beurteilen?
3. **Method Routing:** Welche Analyseart wird gebraucht – Diplomatik, Kartenkritik, Prosopographie, IR-Evaluation etc.?
4. **Validation Routing:** Welche Kompetenz muss einen consequential Finding unabhängig prüfen?

Beispiel U2:

- Problem: Ministerialität/Vogtei → Mediävistik/Herrschafts-/Rechtsgeschichte;
- Quelle: Urkunde/Regest/Kopialbuch → Diplomatik/Editionswissenschaft;
- Name/Terminologie → historische Philologie/Onomastik;
- regionale Einordnung → Landesgeschichte;
- externe Freigabe bei publikationsnaher strittiger Einordnung → qualifizierte Fachperson.

Ein einzelner „Mediävist-Agent“ würde diese unterschiedlichen Zuständigkeiten verschleiern.

### F-C3-04 – Neighbor-Discipline Trigger lassen sich fachlich begründen

Trigger-Kategorien v0.1:

| Signal | zusätzliche Kompetenz |
|---|---|
| Überlieferungs-/Authentizitäts-/Ausfertigungsfrage | Diplomatik / Archivistik / Editionswissenschaft |
| schwer lesbare Handschrift / graphematische Unsicherheit | Paläographie / HTR |
| historischer Fachbegriff mit Rechts-/Institutionengehalt | Rechts-/Verfassungs-/Institutionengeschichte + Philologie |
| Ort/Flur/Gewässer über Zeit | historische Geographie, Kartographie/GIS, ggf. Umweltgeschichte/Archäologie |
| materielle Struktur vs. Schriftquelle | Archäologie/Geoarchäologie zusätzlich |
| Personidentität/Familie/Ämter/Mobilität | Prosopographie/Onomastik + epochen-/regionaler Fachkontext |
| Motiv/Handlungserklärung | Mikrogeschichte/historische Anthropologie/Praxeologie + konkrete Politik-/Sozialdomäne |
| mehreren Quellen stimmen auffällig gleich | Source Dependence/Textkritik/Historiographie |
| starke Abweichung zwischen Quellen | jeweilige Quellenkunde + Discrepancy Reasoning |
| regionales Modell reicht zur Erklärung nicht | Connected/Entangled/Transregional + fachlicher Kontext |
| Ergebnis soll architecture-driving/publikationsnah werden | adversarial review / ggf. unabhängige Fachvalidierung |

Diese Trigger sind **Routing-Hypothesen**, die in den jeweiligen SOTA-Paketen fachlich geschärft werden; sie sind kein automatischer Agentenplan.

### F-C3-05 – Regionale Expertise ist als Quellen-/Forschungskompetenz belegbar

Regionalexpertise darf nicht nur heißen „kennt viele Fakten über Thüringen“. C1 und #16 stützen eine operationalere Checkliste:

- historische Territorial-/Verwaltungschronologie;
- Archive, Provenienzen, Bestandsbildung und bekannte Verluste;
- regionale Editionen/Regesten/Urkundenbücher;
- Fachbibliographien, Zeitschriften, Jahrbücher, Reihen;
- regionale historische/archivische Terminologie;
- Orts-/Flurnamen-/Herrschaftsvarianten;
- zentrale Forschungstraditionen und ältere Narrative;
- typische Quellenlagen und Quellenlücken;
- reale Verflechtungsräume, in denen die regionale Grenze verlassen werden muss.

**Quality implication:** Regional expertise kann durch eine Evidence Checklist überprüft werden, nicht durch Selbstetikettierung des Modells.

### F-C3-06 – Generative KI kann methodische Assistenz leisten, aber ihre plausible Sprache erzeugt keinen unabhängigen Beleg

NIST behandelt **Confabulation** als spezifisches GenAI-Risiko: Systeme können selbstbewusst falsche Inhalte präsentieren, und scheinbare Logik oder Zitate können Nutzer zusätzlich fehlleiten. Für Histo-Orla ist das unmittelbar einschlägig, weil Fachsprache/Quellenzitate besonders autoritativ wirken können.

Microsofts Human-AI-Guidelines stützen auf Interaktionsebene:

- Korrektur/Recovery muss leicht sein;
- bei Unsicherheit Scope begrenzen/disambiguieren;
- erklären, warum das System gehandelt hat;
- Updates vorsichtig behandeln.

**Scholarly implication:** Selbst eine methodisch saubere, toolgestützte KI-Antwort ist nur Assistenz. Unabhängige Validierung braucht unabhängig erzeugte Evidenz oder eine qualifizierte Fachperson.

### F-C3-07 – Expertise Profiles müssen versionierbar und research-question-relative sein

Forschung und Fachstand ändern sich; ein Profile darf deshalb nicht als zeitloses Persona-Dokument behandelt werden. Die AHA beschreibt Disziplinkompetenz selbst als evolving set of practices/tools und Wissen als provisional.

Daraus folgt:

- Profile haben Scope/Version/Quellenbasis;
- nicht jede Kompetenz gilt für jede Epoche/Region;
- methodische Kontroversen gehören in das Profile;
- neue SOTA kann Profile ändern;
- Änderungen an fachlichen Kernregeln sind material changes, nicht stille Promptupdates.

## 5. Expertise Profile Specification v0.1

Je priorisierter Fachkompetenz mindestens:

1. **Identity / scope** – Fachgebiet, Epoche, Region, Problemklassen.
2. **Professional vocabulary** – zentrale Begriffe + Terminology Layers nach C2.
3. **Concept/object models** – fachliche Gegenstandsmodelle und konkurrierende Modelle.
4. **Source universe** – typische Quellengattungen, Überlieferungslogik, Archive/Editionen.
5. **Research heuristics** – Wie findet die Disziplin relevante Evidenz?
6. **Methods / playbooks** – fachliche Analyseverfahren.
7. **Evidence rules** – was kann welcher Quellen-/Befundtyp stützen?
8. **Permitted inference** – zulässige Schlussarten und Grenzen.
9. **Typical fallacies/failure modes**.
10. **Historiography / controversies** – Forschungsdebatten, veraltete/umstrittene Modelle.
11. **Regional/temporal specialization** – inklusive regionaler Evidence Checklist.
12. **Neighbor interfaces / routing triggers**.
13. **Quality checks / falsification patterns**.
14. **Reference basis** – Handbücher, Standards, Journals, Bibliographien, Archive, Datenbanken.
15. **AI/tool support boundary** – was darf assistiert/automatisiert werden?
16. **External validation trigger**.
17. **Version / evidence maturity / revisit trigger**.

## 6. Beispielprofile – Minimal-Stresstest

### Archivistik / Registraturkunde

Muss Provenienz, Registratur-/Bestandsbildung, Beschreibungskontext, Findmittel, historische Administration und Source-vs-Discovery-Status tragen. Ein generisches „Archivsuche“-Profil genügt nicht.

### Mediävistische Herrschafts-/Landesgeschichte

Muss Begriffe wie Vogtei/Ministerialität/Lehen/Grundherrschaft etc. historisieren, Quellengattungen und Rechts-/Herrschaftsmodelle unterscheiden, regionale Forschungstraditionen kennen und Diplomatik triggern können.

### Historische Geographie / Kulturlandschaft

Muss Karten-/Maßstabs-/Entstehungszweckkritik, Persistenz/Transformation, Flur-/Wege-/Gewässerstrukturen und Schnittstellen zu Archäologie/Umweltgeschichte tragen.

### Frühneuzeitliche Adels-/Hof-/Reichsgeschichte

Muss Rollen/Ämter/Hof/Patronage/Reichs-/Territorialkontext, Quellen der politischen Kommunikation und Risiken modernisierender Partei-/Motivmodelle kennen; Prosopographie/Diplomatie/Konfession/Militär bei Bedarf routen.

Der Stresstest zeigt: Ein einheitliches Persona-Schema kann die Struktur teilen, aber **Inhalt und Qualitätsregeln müssen disziplinspezifisch sein**.

## 7. Validation-Level-Modell v0.1

### L0 – Candidate / Exploration

- KI/Tool darf Begriffe, Quellen, Hypothesen vorschlagen.
- klare Kennzeichnung als Kandidat.
- kein Promotion in gesicherten Research State.

### L1 – Method-compliant working research

- zuständige Fachdomäne/Methodik aktiviert;
- Evidenz und Fundstellen nachvollziehbar;
- Alternativen/Unsicherheit geprüft;
- #45 Basis-QA bestanden.

### L2 – Consequential / architecture-driving

Zusätzlich:

- adversarialer Gegencheck;
- relevante Neighbor Competency;
- SOTA-/Research Traceability;
- Acceptance-/Falsification Case.

### L3 – Independent expert validated

- tatsächliche qualifizierte externe/independent Fachperson oder unabhängige fachliche Evidenzprüfung;
- Person/Qualifikation/Scope der Prüfung nachvollziehbar;
- KI-Mehrfachprüfung zählt nicht als L3.

Nicht jede Aufgabe braucht L3. Validierungsstärke folgt Konsequenz und Fachstandard.

## 8. Routing Logic v0.1

```text
Nutzerfrage / Finding
→ Problem Translation (C2)
→ welche Fachdomäne besitzt das Problem?
→ welche Quellengattung liegt vor?
→ welche Methode ist nötig?
→ welche Neighbor-Domain wird durch Material/Relation/Scale getriggert?
→ gewünschter Consequence Level?
→ passende Validation Level
→ Research Brief + Evidence Requirements
```

Der Router soll seine Entscheidung erklärbar machen: **warum diese Kompetenz, wofür, und welche Grenze hat sie?**

## 9. Capability Candidates

- `CAP-EXPERTISE-PROFILE`: versionierte, evidenzgebundene Fachkompetenzprofile verfügbar machen.
- `CAP-EXPERTISE-ROUTING`: Problem/Source/Method/Validation problemabhängig routen.
- `CAP-NEIGHBOR-TRIGGER`: fachliche Schnittstellen/Blind Spots erkennen.
- `CAP-REGIONAL-EXPERTISE`: regionale Quellen-/Forschungslandschaft als Teil von Expertise aktivieren.
- `CAP-VALIDATION-LEVEL`: method compliance und unabhängige Fachvalidierung unterscheiden.
- `CAP-ROUTING-EXPLANATION`: dem Research Owner erklären, welche Kompetenz warum aktiv ist.

## 10. Quality / Requirement Candidates

- REQ-C3-A: Jede consequential Analyse muss eine führende Fachdomäne und deren methodischen Scope erkennen lassen.
- REQ-C3-B: Expertise darf nicht allein durch Persona/Rollenprompt behauptet werden; Profile brauchen nachprüfbare Methoden-/Quellen-/Qualitätsbasis.
- REQ-C3-C: Router muss Neighbor-/Escalation-Triggers unterstützen und darf keine epistemische Superrolle besitzen.
- REQ-C3-D: Regionale Expertise muss über nachvollziehbare Quellen-/Forschungsressourcen und Geltungsgrenzen gestützt werden.
- REQ-C3-E: `independent expert validated` darf nur bei tatsächlicher unabhängiger Fachprüfung vergeben werden.
- REQ-C3-F: Fachprofile müssen versionierbar/revisit-able sein; material fachliche Änderungen dürfen nicht still erfolgen.

## 11. Challenge interner Annahmen

#19 wird fachlich bestätigt, aber technisch enger gefasst: **fachliche Modularität ist Requirement, technische Agentenpluralität nicht**. Ein Profile ist kein „Prompt Pack“, sondern ein dokumentierter epistemischer Vertrag, der Retrieval/Tools/KI steuern kann.

Das `paleo-type`-Prinzip proportionaler Validierung wird bestätigt und auf fachliches Routing erweitert. RGK liefert keine Expertise-Architektur; seine Views/Modelle müssen jeweils durch die zuständige Kompetenz kontrolliert werden.

## 12. Open Questions / bounded debt

- Die vollständigen Inhalte jedes regionalisierten Expertise Profiles werden use-case- und SOTA-getrieben aufgebaut; keine Vollbibliothek vor Architektur nötig.
- Kosten/Verfügbarkeit externer Fachprüfung ist späteres Operations-/Governance-Thema, sofern kein aktueller consequential Claim sie verlangt.
- Technische Form (single assistant + profiles, retrieval contexts, tools, modules, agents) bleibt #39/#43 offen.

## 13. #45 Quality Check

- **Domain fit:** historische Fachmethodik/Research Integrity führen; AI/UX nur unterstützend.
- **Evidence fit:** AHA/aktuelle historische Methodenliteratur stützen disziplinäre Praktiken; NIST/Microsoft nur die AI-/Interaction-Grenzen.
- **Inference fit:** Kompetenzbildungsrahmen werden nicht als vollständige Definition professioneller Spitzenexpertise missverstanden, sondern als Mindestbeleg für methodische/epistemische Komponenten.
- **Terminology fit:** method compliance, expert validation, routing und persona werden getrennt.
- **Provenance fit:** Quellenbasis und Grenzen sind dokumentiert.
- **Falsification/challenge:** vier stark unterschiedliche Profile zeigen, ob ein generisches Schema fachliche Unterschiede tragen kann; externe Fachvalidierung bleibt eigener Status.

## 14. Sättigungsbegründung

Für die Systemanforderung ist genügend Evidenz vorhanden: historische Fachkompetenz ist methoden-, quellen-, kontext- und argumentationsgebunden; generative KI kann sie unterstützen, aber nicht durch Rollenetikett oder fluente Ausgabe ersetzen. Die genaue fachliche Ausfüllung der Profile ist laufende Research Content Work und kein Blocker für die Capability-/Requirements-Ableitung.
