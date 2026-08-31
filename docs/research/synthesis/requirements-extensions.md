# Histo-Orla – Accepted Requirements Extensions aus Live-/Domain-Research

**Status:** `accepted / active / iterative`  
**Requirements Owner:** #42  
**Inputs:** #46/#47 Live Research, #60 Domain Method Research, Owner Constraints  
**Baseline:** `docs/research/synthesis/requirements-baseline.md`

## 1. Zweck

Dieses Artefakt ergänzt die Requirements Baseline um **inhaltlich bereits akzeptierte Systemanforderungen**, die durch die vertiefte Live- und Domain-Method-Arbeit nach der Baseline v0.1 präzisiert wurden.

Es ist **keine MVP-Schicht und keine zweite Produktdefinition**. Die aktive Systemanforderung ist die Vereinigung aus:

1. `requirements-baseline.md`;
2. diesen accepted Requirements Extensions;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints;
4. späteren explizit akzeptierten Deltas unter #42.

Fachwissenschaftliche **Method Truth** bleibt #60/SOTA-gebunden. Dieses Artefakt beschreibt, was das System tragen und überprüfbar machen muss.

## 2. Accepted Extensions

### REQ-EPI-006 – Semantische Forschungszustände bleiben unterscheidbar

Das System muss unterschiedliche epistemische/arbeitsbezogene Zustände getrennt führen können, mindestens soweit sie im realen Workflow auftreten:

`vision | work_order | source | representation | inspected_instance | derivative | findspot | excerpt | observation | finding | research_hook | historical_hypothesis | method_hypothesis | domain_method_profile | method_application | requirement_candidate | accepted_requirement | architecture_choice | prompt/model_run | review/validation`.

**Acceptance:** Kein Prompt, Katalogtreffer, Research Hook oder Hypothese kann still als Finding/Evidence erscheinen.

### REQ-INT-002 – Zotero / OneDrive / Histo-Orla besitzen getrennte Verantwortungen

Für den aktuellen privaten Workflow gilt als Owner Constraint:

```text
OneDrive  = Source of Bytes
Zotero    = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Das System muss diese Ebenen integrieren können, ohne Pfad, Zotero-Key oder OneDrive-ID zur alleinigen wissenschaftlichen Source-/Instance-Identität zu machen.

### REQ-MTH-001 – Domain Method Profiles sind eigenständige, versionierte Fachobjekte

Domänenspezifische Fachmethodik darf nicht nur als Rollenprompt/Disziplinlabel existieren. Das System muss Domain Method Profiles als referenzierbare, versionierbare und statusbehaftete Fachobjekte unterstützen.

### REQ-MTH-002 – Domain Method Profiles können die fachlich notwendigen Bestandteile ausdrücken

Ein Profile muss – soweit für die jeweilige Domäne relevant – ausdrücken können:

1. Geltungsbereich / Problem- und Quellentypen;
2. Fachbegriffe, Gegenstandsmodelle und konkurrierende Modelle;
3. Quellen-/Materialmodell und Biases/Überlieferungsprobleme;
4. ausführbares fachliches Playbook;
5. Inferenzvertrag: zulässige und unzulässige Schlüsse;
6. Evidence Appetite sowie Fach-/Archiv-/Suchvokabular;
7. SOTA-/Methodenliteratur und Kontroversen;
8. QA, typische Fehlschlüsse, Falsifikation/Counterexamples;
9. transdisziplinäre Handoffs / Evidence Routing;
10. Grenze Mensch ↔ Regel ↔ Spezialalgorithmus ↔ GenAI.

Die konkrete wissenschaftliche Ausprägung liefert #60, nicht Dev.

### REQ-MTH-003 – Method Status, Version und konkrete Method Application sind nachvollziehbar

Method Profiles müssen mindestens `scoping | method-candidate | working-method | validated-method | deprecated/revised` unterscheiden können. Für consequential Findings muss nachvollziehbar sein, welche konkrete Method Application und welche Profilversion/-status verwendet wurde, soweit die Methode operationalisiert ist.

### REQ-MTH-004 – Exploration bleibt offen, epistemische Promotion bleibt methoden-/evidenzgebunden

Noch nicht ausgereifte Methodik darf Exploration nicht blockieren. Fehlende Method-/Evidence-Grundlage darf aber keinen höheren epistemischen Status vortäuschen.

**Acceptance:** `method-candidate` kann explorative Analyse anleiten; bei unzureichender Evidenz bleiben Ergebnisse `candidate | unresolved | not-assessable` statt plausibel erfundener Auflösung.

### REQ-MTH-005 – Methodische Qualität umfasst Overclaim-/Counterexample-Schutz

Ein methodisches Verfahren darf nicht allein dadurch als belastbar gelten, dass es einen positiven Fall plausibel erklärt. Die System-/Review-Unterstützung muss positive Fälle ebenso wie typische Overclaims, Counterexamples und evidence-starved Situationen sichtbar prüfen können.

### REQ-RSCH-001 – Research Hook, historische Hypothese und Finding sind getrennte Zustände

Ein offener Anschlussauftrag wie „Ausstattung/Besitzentwicklung prüfen“ muss speicher- und weitergebbar sein, ohne als historische Hypothese oder Finding promoted zu werden.

### REQ-RSCH-002 – Fachdomänen/Methoden können Evidence Demand erzeugen

Aktivierte Fachdomänen und Methoden müssen Evidenzbedarf ausdrücken/routen können: relevante Quellen-/Materialklassen, Fach-/Archiv-/Suchvokabular, notwendige Vergleiche/Kontrollen sowie mögliche Falsifikation.

### REQ-RSCH-003 – Expliziter Quellenbefund und weiterer Erklärungsraum bleiben getrennt

Ein einzelner Quellentext darf nicht automatisch definieren, welche Ursachen- oder Erklärungsebenen als hinreichend untersucht gelten. Das System muss source-explicit Befund und weiterführenden fachlichen Untersuchungs-/Erklärungsraum getrennt halten können.

### REQ-RSCH-004 – Multi-Method-/Multi-Domain-Handoffs bewahren Evidenz- und Inferenzgrenzen

Beobachtungen müssen gezielt an andere Fachdomänen/Methoden übergeben werden können, ohne deren Evidenz- und Inferenzregeln still zu verschmelzen. Mehrere konkurrierende Erklärungen dürfen parallel bestehen und unresolved bleiben.

### REQ-STATE-003 – Restartability umfasst research-ready Evidence Availability

Identität, Locator und reproduzierbarer Prozess allein genügen nicht. Wenn die nächste erlaubte Aktion direkte Quelleninspektion verlangt, muss ein neuer autorisierter Work Context die konkrete benötigte Instanz tatsächlich öffnen können **oder** einen expliziten Availability-Blocker erkennen.

### REQ-UX-003 – Progressive Disclosure ohne epistemische Verdeckung

Das System soll einen einfachen privaten Forschungsfluss ermöglichen, ohne wissenschaftliche Tiefe zu verstecken. Orientierung darf zunächst kompakt sein; Quelle/Fundstelle, Evidenzstatus, Methode, Alternativen, Unsicherheit, Review und History müssen aus demselben kanonischen State bei Bedarf nachvollziehbar erreichbar sein.

## 3. Bereits durch die Baseline abgedeckte spätere Präzisierungen

Die folgenden später formulierten Acceptance-Punkte sind **keine zweite Requirement-Schicht**, sondern Präzisierungen bereits akzeptierter Requirements:

| spätere Präzisierung | kanonisches Requirement |
|---|---|
| Unsicherheit als gültiger Zustand | REQ-EPI-004 |
| AI ist keine Evidenz / unabhängige Validierung | REQ-EPI-005 |
| Source-/Representation-/Instance-/Derivative-Trennung | REQ-SRC-001/002/003/004 |
| Findspot-Roundtrip | REQ-SRC-004 |
| Exact Search ohne LLM | REQ-RET-001 |
| kontrollierte historische Varianten | REQ-RET-002 |
| OCR/HTR bleibt Derivat + research-critical Evaluation | REQ-OCR-001/002/003 |
| konkurrierende Erklärungen sichtbar halten | REQ-EPI-004 + REQ-SYN-002 |
| Human-readable Audit | REQ-UX-001/002 + REQ-MTH-003 |
| kein Chat-Wissensmonopol / portable State | REQ-STATE-001 + AGENTS.md |
| deterministische formale Guards | REQ-WF-001 |
| curated vs. regenerable | REQ-STATE-002 |
| Rights / Privacy Admission | REQ-RGT-001/002 |
| technische Subsidiarität / Existing Tools vor Eigenbau | REQ-LEAN-001 |
| unscharf fragen → fachlich sauber | REQ-EPI-002/003 + REQ-RSCH-002 |

## 4. Delivery-/Research-Entscheidungen – keine neuen Systemrequirements

Folgende Punkte bleiben wichtig, sind aber bewusst **keine eigene Requirement-Klasse**:

- `read-first` bei Zotero/OneDrive ist eine aktuelle Integrations-/Delivery-Strategie unter #49;
- erstes reales Domain Profile `Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik` ist aktuelle Priorisierung unter #60;
- privater Single-Owner-Workflow ist aktueller Projekt-/Owner-Scope;
- kleine vertikale Inkremente und evolutionäre Architektur sind Delivery-Prinzipien, keine fachliche Scope-Reduktion.

## 5. Non-Regression

`lean`, `agil`, `privat`, neue Tools, Frameworks, Phasenbegriffe oder Architekturpatterns ändern diese Requirements **nicht implizit**.

Eine materielle Reduktion/Änderung benötigt unter #42/#44:

```text
betroffenes Requirement
→ Grund
→ Konsequenz / Verlust
→ Alternative
→ explizite Owner-Entscheidung
→ Traceability
```

## 6. Leitregel

> **Requirements beschreiben, was das System wissenschaftlich und technisch leisten muss. Lean/Agile entscheidet, mit welchen möglichst einfachen, hochwertigen und reversiblen Mitteln wir das erreichen.**
