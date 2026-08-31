# Histo-Orla – Requirements Baseline v0.1

**Work Owner:** #42  
**Status:** `completed-synthesis / requirements-baseline-v0.1`  
**Inputs:** #28–#41; fachliche Requirements-/Scope-Owner #9/#13–#16/#19/#20/#24; Live-Research Requirement Candidates #46/#47.  
**Methodik:** Scholarly Requirements Engineering; fachgebundene Quality/Acceptance gemäß #45.  
**Zweck:** architecture-driving Anforderungen definieren, **ohne Architektur/Technologie vorwegzunehmen**.  
**Aktuelle innere Struktur / Authority / Traceability für neue bzw. materiell bearbeitete Requirements:** `docs/research/synthesis/requirements-structure.md`.

---

# 1. Leseregel

Diese Datei bleibt die **accepted Baseline v0.1 und historische Provenienz**. Die ursprünglichen Requirements werden nicht per Big-Bang umgeschrieben. Bei neuer oder materieller Bearbeitung gelten zusätzlich die Strukturregeln aus `requirements-structure.md`, insbesondere die Trennung von Requirement Source, Domain Authority, canonical Requirement Owner, Acceptance/Verification Authority, Scope, Dependencies, Criticality und Architecture Significance.

Requirement-Status:

- `accepted-v0.1` – ausreichend traceable, fachlich/SOTA-/risk-seitig gestützt und verifizierbar für Architekturarbeit;
- `accepted-constraint` – harte fachliche/rechtliche/Governance-Grenze; konkrete Implementation offen;
- `deferred-research` – plausibel, aber für v0.1 noch nicht hinreichend oder nicht architecture-blocking;
- `architecture-choice` – keine Anforderung, sondern später zu vergleichende Lösung.

Historische Priorität der Baseline:

- **P0** – architecture-driving / wissenschaftlich fundamental / cross-cutting;
- **P1** – zentrale analytische Funktion nach Grundkern;
- **P2** – später iterativ vertiefbar.

Wichtig ab `requirements-structure.md`:

> **Diese historische P0/P1/P2-Klassifikation ist nicht alleinige Delivery-Reihenfolge.** Wissenschaftliche Kritikalität, Architecture Significance und aktuelle Delivery-Priorität werden künftig getrennt betrachtet.

Jedes Requirement folgt soweit relevant:

`Need/Pain → Capability → Invariante → Requirement → Acceptance/Test → Risk → SOTA`.

Die aktuelle erweiterte Traceability lautet für aktiv bearbeitete Requirements:

`Driver/Motivation → Origin/Evidence → Domain Authority → Capability/Invariante → Requirement → Scope/Dependencies/Criticality → Acceptance/Verification → technische Derivation #48 → Implementation/Verification #59`.

---

# 2. Scientific / Epistemic Requirements

## REQ-EPI-001 – Fachdomäne besitzt Methode und Evidenzmaßstab

- **Type:** Scientific/Epistemic.
- **Statement:** Für jede consequential fachliche Analyse muss nachvollziehbar sein, welche Fachdomäne(n) führen und welche domänenspezifischen Methoden, Evidenzmaßstäbe und zulässigen Schlussarten gelten; technische/AI-Komponenten dürfen diese nicht eigenmächtig ersetzen oder abschwächen.
- **Rationale:** G-003; N-002/N-018; #9/#15/#16/#19.
- **Owner:** jeweilige Fachdomäne; Research Integrity kontrollierend.
- **Capabilities:** CAP-02, CAP-16, CAP-18.
- **Use Cases:** U1–U4.
- **Acceptance:** Ein U1/U2/U3 Research Brief nennt führende/controlling Domänen und Methoden; ein generischer AI-Output ohne Fachrouting kann nicht als consequential validated State promoted werden.
- **Risks:** RISK-13/-14/-27.
- **Evidence:** C3/C9 (#33/#39), #45.
- **Priority:** P0.
- **Implementation freedom:** Kompetenzprofile, Routing-Regeln, Tooling offen.
- **Forbidden shortcut:** Rollenprompt als alleiniger Beleg fachlicher Expertise.
- **Status:** `accepted-v0.1`.

## REQ-EPI-002 – Fachliche Problemübersetzung statt Synonymersetzung

- **Type:** Functional + Scientific.
- **Statement:** Das System muss unscharfe Nutzerbeobachtungen in mehrere fachlich plausible Problem-/Concept Candidates, Terminologieebenen und diskriminierende Folgefragen übersetzen können, ohne ähnliche Begriffe als identisch auszugeben.
- **Rationale:** N-001; P-001; G-002.
- **Owner:** jeweilige Fachdomäne + historische Semantik/KO.
- **Capabilities:** CAP-01.
- **Use Cases:** U1–U3.
- **Acceptance:** U2-Near Concepts (`Vogtei`, `Ministerialität`, `Lehen`, `Grundherrschaft`) bleiben getrennt und werden mit Geltungs-/Prüffragen erläutert; U1 erhält fachliche+archivische Problembegriffe statt nur Synonyme für `Teich`.
- **Risks:** RISK-04/-05/-13.
- **Evidence:** C2 (#32).
- **Priority:** P0.
- **Forbidden shortcut:** generische Synonymliste als fachliche Problemübersetzung.
- **Status:** `accepted-v0.1`.

## REQ-EPI-003 – Terminologieebenen und Geltungsbereiche bleiben unterscheidbar

- **Type:** Data/Scientific.
- **Statement:** Historischer Quellenbegriff, zeitgenössische institutionelle/rechtliche Bezeichnung, editorische/archivische Form, moderner Analysebegriff, Historiographiebegriff und Suchvariante müssen unterscheidbar und mit relevantem Zeit-/Raum-/Institutionskontext führbar sein.
- **Rationale:** N-001/N-008; G-003/G-006.
- **Owner:** jeweilige Fachdomäne + historische Philologie/Archivistik.
- **Capabilities:** CAP-01, CAP-06, CAP-11.
- **Acceptance:** Normalisierte Orts-/Fachform überschreibt historische Form nicht; U2 `Knewe/Kneben/Knewer` bleibt als beobachtete Form erhalten.
- **Risks:** RISK-05/-08/-14.
- **Evidence:** C2/C4 (#32/#36), #46.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-EPI-004 – Unsicherheit, Nichtwissen und Kontroverse sind kanonische Zustände

- **Type:** Scientific/Data.
- **Statement:** Das System muss unresolved identity, unresolved discrepancy, genuine contradiction, competing interpretation, hypothesis und evidence gap als persistierbare Zustände zulassen und darf sie nicht zur Vollständigkeit/Harmonie zwingen.
- **Rationale:** N-010/N-014; G-006/G-009.
- **Owner:** Fachdomäne + Research Integrity.
- **Capabilities:** CAP-10, CAP-16, CAP-18.
- **Acceptance:** U2 `1374/1378` bleibt mit beiden Provenienzpfaden unresolved; keine Mehrheits-/LLM-Entscheidung wird automatisch `resolved`.
- **Risks:** RISK-07/-13/-23.
- **Evidence:** C6/C8 (#34/#38), #46.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-EPI-005 – AI-Ausgabe ist weder Evidenz noch unabhängige Validierung

- **Type:** Scientific/Governance.
- **Statement:** Generative AI-Ausgaben dürfen weder als Evidenzklasse noch allein oder durch mehrere korrelierte AI-Instanzen als unabhängige fachliche Validierung klassifiziert werden.
- **Rationale:** #9/#12/#15/#24/#45.
- **Owner:** Research Integrity + Fachdomäne.
- **Capabilities:** CAP-18.
- **Acceptance:** Systemstatus `independent expert validated` benötigt extern unabhängige qualifizierte Prüfung/evidenzielle Grundlage; AI-Zusammenfassung bleibt Assistenzprodukt.
- **Risks:** RISK-01/-13/-16/-27.
- **Evidence:** C3/C9 (#33/#39).
- **Priority:** P0.
- **Status:** `accepted-constraint`.

---

# 3. Source / Provenance / Findspot Requirements

## REQ-SRC-001 – Source Identity ist von Repräsentation getrennt

- **Type:** Data/Provenance.
- **Statement:** Bibliographische/archivalische Source Identity muss von Edition, Regest, Digitalisat, OCR/HTR und weiteren Repräsentationen/Derivaten unterscheidbar bleiben.
- **Rationale:** N-005; G-004/G-006.
- **Owner:** Archivistik/Diplomatik/Edition/RDM.
- **Capabilities:** CAP-04, CAP-08.
- **Acceptance:** `Regest` kann technisch/fachlich nicht als `Originalurkunde` erscheinen; U2 user-supplied edition ist bibliographisch identifizierbar.
- **Risks:** RISK-01/-14.
- **Evidence:** C1/C6 (#31/#34), RC-U2-08.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-SRC-002 – Konkrete inspizierte Instanz und Inspection Status sind nachvollziehbar

- **Type:** Provenance.
- **Statement:** Wo eine konkrete digitale/physische Instanz tatsächlich inspiziert wurde, muss ihr Status von bloßer Katalog-/Findmittel-/Zitieridentität unterscheidbar sein; eine URL/Signatur ersetzt nicht die Identität des inspizierten Exemplars und umgekehrt.
- **Rationale:** N-005/N-015.
- **Owner:** Archivistik/RDM.
- **Capabilities:** CAP-04.
- **Acceptance:** U1 Findbuchtreffer 1556–1557 bleibt `catalog/find-aid discovery`, solange die Akte nicht inspiziert wurde.
- **Risks:** RISK-01/-17.
- **Evidence:** C1 (#31), #40 T-RISK-01.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-SRC-003 – Editorische Eingriffe und Normalisierungen überschreiben Quellentext nicht

- **Type:** Scientific/Data.
- **Statement:** Editorische Ergänzungen, Normalisierungen, Identifikationen und spätere Korrekturen müssen getrennt vom historischen Wortlaut speicher- und darstellbar sein.
- **Rationale:** G-006; Live Pain RC-U2-01.
- **Owner:** Editionswissenschaft/Diplomatik/Fachdomäne.
- **Capabilities:** CAP-04, CAP-08.
- **Acceptance:** `Heinrich [Stange] von Knewe`: `[Stange]` bleibt als editorische Ergänzung markiert; kein Export/View darf es still als historischen Wortlaut ausgeben.
- **Risks:** RISK-01/-05/-14.
- **Evidence:** #46, C1/C6.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-SRC-004 – Fundstellen-Rückführung ist verlustfrei soweit quellenseitig möglich

- **Type:** Data/Quality.
- **Statement:** Findings, Suchtreffer und Exzerpte müssen zu Seite/Folio/Regestnummer/Archivalieneinheit bzw. der präzisesten verfügbaren Fundstelle zurückführbar sein.
- **Rationale:** N-006; P-004; G-004.
- **Owner:** Quellenkunde/RDM/IR.
- **Capabilities:** CAP-04, CAP-05, CAP-06, CAP-17.
- **Acceptance:** U4 source page → OCR → search hit → excerpt → citation roundtrip liefert dieselbe korrekte Fundstelle und Parent-Derivatkette.
- **Risks:** RISK-02/-23.
- **Evidence:** C1/C7 (#31/#35), T-RISK-02.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-SRC-005 – Archive Routing unterstützt Provenienz-/Funktionslogik

- **Type:** Functional/Scientific.
- **Statement:** Quellenrecherche muss historische Registraturbildner, Verwaltungs-/Herrschaftsfunktionen, Bestands-/Serienkontexte und Archivsprache neben moderner Pertinenzsuche berücksichtigen können.
- **Rationale:** N-004; P-002/P-006.
- **Owner:** Archivistik/Registraturkunde + regionale Fachdomäne.
- **Capabilities:** CAP-03.
- **Acceptance:** U1-Landschaftsfrage erzeugt relevante Suchpfade zu Rechnungen, Fischerei, Mühlen, Hutung/Trift, Grenzen/Forst/Gut zusätzlich zu Karten.
- **Risks:** RISK-04/-11/-12.
- **Evidence:** C1 (#31), #47.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

---

# 4. OCR / Derivative Requirements

## REQ-OCR-001 – OCR/HTR bleibt versioniertes Derivat mit Parentage

- **Type:** Data/Provenance.
- **Statement:** OCR/HTR/Textlayer und Korrekturen müssen als Derivate mit Herkunft/Processor-/Version-/Parent-Bezug geführt werden; sie dürfen keinen Originalstatus annehmen.
- **Rationale:** N-007; G-006.
- **Owner:** OCR/HTR/DH + RDM.
- **Capabilities:** CAP-05.
- **Acceptance:** raw OCR, corrected OCR und manuelle Transkription sind unterscheidbar; Processor/Version für consequential Output rekonstruierbar.
- **Risks:** RISK-01/-03/-18.
- **Evidence:** C7 (#35).
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-OCR-002 – Seiten-/Folio-/Region-Mapping überlebt Texttransformation

- **Type:** Quality/Data.
- **Statement:** Textderivate müssen die Zuordnung zur Quellseite/Folio und, soweit für Layoutquellen nötig, zur relevanten Region so erhalten, dass Exzerpte/Fundstellen auditierbar bleiben.
- **Rationale:** N-006/N-007.
- **Owner:** DH/RDM/IR.
- **Capabilities:** CAP-05.
- **Acceptance:** T-RISK-02 U4 Roundtrip; Seitenverschiebung/Regionverlust wird als Fehler erkannt.
- **Risks:** RISK-02/-03.
- **Evidence:** C7 (#35).
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-OCR-003 – OCR/HTR-Evaluation misst research-critical Fehler

- **Type:** Quality.
- **Statement:** Systematisch eingesetzte OCR/HTR-Verfahren müssen auf repräsentativem Material nicht nur mit CER/WER, sondern zusätzlich auf Namen, Orte, Zahlen/Daten, Fachtermini, Layout-/Findspotverlust und domänenkritische Tokens evaluiert werden.
- **Rationale:** N-018; RISK-03.
- **Owner:** OCR/HTR + Fachdomäne/Quality.
- **Capabilities:** CAP-05, CAP-18.
- **Acceptance:** Engine-/Modellpromotion setzt dokumentierten Corpus-Goldtest voraus; kritische Namen-/Zahlfehler werden separat ausgewiesen.
- **Evidence:** C7 (#35).
- **Priority:** P1 vor massenhafter Verarbeitung; P0 als Architekturunterstützung.
- **Status:** `accepted-v0.1`.

---

# 5. Retrieval / Search Requirements

## REQ-RET-001 – Exakte/auditierbare Suche ist Baseline und funktioniert ohne LLM

- **Type:** Functional/Quality.
- **Statement:** Der Forschungsbestand muss exakte Wörter/Phrasen und nachvollziehbare Filter/Fundstellen ohne generative AI oder semantische Retrievalschicht suchen können.
- **Rationale:** N-008; G-004/G-008.
- **Owner:** IR/RSE.
- **Capabilities:** CAP-06.
- **Acceptance:** bekannte U2/U4 Exact Queries liefern stabile Hits/Fundstellen bei deaktivierter AI-/Semantic-Komponente.
- **Risks:** RISK-15/-17.
- **Evidence:** C7/C9 (#35/#39).
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-RET-002 – Historische Varianten-/Query Expansion ist kontrolliert und erklärbar

- **Type:** Functional/Scientific.
- **Statement:** Suche muss fachlich/onomastisch begründete historische Schreib-/Namens-/Sprach-/Archivvarianten verwenden können; jede Expansion muss als Suchentscheidung nachvollziehbar bleiben und darf Varianten nicht automatisch ontologisch gleichsetzen.
- **Rationale:** N-001/N-008; P-005.
- **Owner:** IR + Fachphilologie/Onomastik/Fachdomäne.
- **Capabilities:** CAP-01, CAP-06.
- **Acceptance:** U2 Query Log zeigt `Knewe/Kneben/Knewer/...` und Herkunft der Varianten; bekannte Homonyme werden nicht durch Expansion gemerged.
- **Risks:** RISK-04/-05/-08.
- **Evidence:** C2/C7 (#32/#35), RC-U2-03.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-RET-003 – Query-/Corpus-Provenienz ist reproduzierbar

- **Type:** Data/Quality.
- **Statement:** Für relevante Suchläufe müssen Query/Expansion, Filter, Corpus-/Indexgrenze und relevante Processor-/Ranking-Version so dokumentierbar sein, dass Ergebnisbedingungen rekonstruierbar sind.
- **Rationale:** N-015/N-018.
- **Owner:** IR/RDM/RSE.
- **Capabilities:** CAP-06, CAP-07, CAP-19.
- **Acceptance:** derselbe gespeicherte Gold Query kann mit dokumentiertem Corpus/Index reproduziert oder Unterschiede nach Corpus-/Processoränderung erklärt werden.
- **Risks:** RISK-18/-19.
- **Evidence:** C7/C9, #40.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-RET-004 – Negative Findings brauchen Search Boundary

- **Type:** Scientific/Data.
- **Statement:** Ein Negativbefund mit `working research` oder höher muss mindestens Corpus/Bestände, Zeitraum, relevante Suchvarianten/-felder und bekannte Zugangs-/Indexgrenzen benennen.
- **Rationale:** N-014; Live Pain RC-U2-05.
- **Owner:** Fachdomäne + IR/Archivistik.
- **Capabilities:** CAP-07.
- **Acceptance:** `kein Treffer im DO-UB` kann nicht zu `Ort existierte nicht` promoted werden; Boundary bleibt am Finding sichtbar.
- **Risks:** Retrieval/Completeness Overclaim.
- **Evidence:** #45, C1/C7, #46/#47.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-RET-005 – Semantische Suche/RAG ist nur additive, benchmark-admitted Schicht

- **Type:** Quality/Architecture constraint.
- **Statement:** Semantische Retrieval-/RAG-Verfahren dürfen die exakte/auditierbare Baseline nicht ersetzen und dürfen consequential verwendet werden, wenn ein repräsentativer Gold-Query-Test einen relevanten Zusatznutzen ohne unvertretbaren Recall-/Grounding-Verlust zeigt.
- **Rationale:** N-020; G-012.
- **Owner:** IR/AI Evaluation + Fachdomäne.
- **Capabilities:** CAP-06, CAP-18.
- **Acceptance:** T-RISK-06; jeder semantische Hit bleibt auf Source/Findspot rückführbar.
- **Risks:** RISK-15/-28.
- **Evidence:** C7/C9.
- **Priority:** P1 Constraint; Implementierung optional.
- **Status:** `accepted-constraint`.

---

# 6. Source Criticism / Entity / Relation Requirements

## REQ-CRIT-001 – Source Dependence ist claim-spezifisch prüfbar

- **Type:** Scientific/Data.
- **Statement:** Für Corroboration muss dokumentierbar sein, ob Evidenz für den konkreten Claim unabhängig, abhängig, wahrscheinlich abhängig oder unklar ist; dokumentarische/editionelle/historiographische Ableitungen dürfen nicht still mehrfach zählen.
- **Rationale:** N-009.
- **Owner:** Quellenkritik/Diplomatik/Textkritik.
- **Capabilities:** CAP-09.
- **Acceptance:** T-RISK-04 Urkunde→Regest→Edition→Artikel wird nicht als vier unabhängige Evidenzketten gewertet.
- **Risks:** RISK-06.
- **Evidence:** C6 (#34).
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-CRIT-002 – Discrepancies werden vor Harmonisierung diagnostiziert

- **Type:** Scientific/Functional.
- **Statement:** Abweichende Aussagen/Datierungen/Identifikationen müssen nach Zeitstand, Überlieferungsstufe, Zweck, Institution, Terminologie, Maßstab, Interessen und Abhängigkeit vergleichbar sein; ungelöste Widersprüche bleiben möglich.
- **Rationale:** N-010/N-014.
- **Owner:** Fachdomäne + Quellenkritik.
- **Capabilities:** CAP-10.
- **Acceptance:** U2 1374/1378 bleibt unresolved, bis diskriminierende Evidenz vorliegt; keine automatische Majority Resolution.
- **Risks:** RISK-07.
- **Evidence:** C6, RC-U2-06.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-ENT-001 – Entity Resolution nutzt Candidate→Promotion mit False-Merge-Schutz

- **Type:** Scientific/Data/Workflow.
- **Statement:** Orts-/Personen-/Institutionsidentitäten dürfen als Kandidaten vorgeschlagen werden, aber Promotion muss Evidenz-/Kontextkriterien berücksichtigen und unresolved/rejected-homonym unterstützen; generative AI darf keinen direkten kanonischen Merge ausführen.
- **Rationale:** U2 Live Pain; N-008/N-014/N-017.
- **Owner:** Fachdomäne/Onomastik/Prosopographie + deterministische Promotion Controls.
- **Capabilities:** CAP-11, CAP-18.
- **Acceptance:** T-RISK-07 plus U2 Altenburg-Knau vs. Orla-Knau; bekannte Homonyme werden nicht automatisch vereinigt.
- **Risks:** RISK-08/-16.
- **Evidence:** C2/C4/C9, RC-U2-02.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-REL-001 – Proxy/Ko-Präsenz ist von historischer Relation getrennt

- **Type:** Scientific/Data.
- **Statement:** Zeugen-Kopräsenz, gleicher Ort, gleiche Institution/Universität/Hof oder zeitliche Nähe dürfen als Kontext-/Proxy-Befund gespeichert/gesucht, aber nicht ohne zusätzliche Evidenz als soziale, politische, genealogische oder motivationale Relation promoted werden.
- **Rationale:** N-011/N-013.
- **Owner:** Netzwerk-/Prosopographie/Fachdomäne.
- **Capabilities:** CAP-12, CAP-14.
- **Acceptance:** U2 Knewe/Stange gemeinsame Zeugen-/Burgmannenkontexte bleiben Proxy; U3 gemeinsame Hofpräsenz wird keine Patronagekante ohne Evidenz.
- **Risks:** RISK-09/-10/-24.
- **Evidence:** C4/C5, RC-U2-04.
- **Priority:** P1, architecture-driving für relationale Modelle.
- **Status:** `accepted-v0.1`.

---

# 7. Space / Actor / Cross-Evidence Requirements

## REQ-SPAT-001 – Orte/Territorien sind zeitabhängige Kontexte, keine statischen Container

- **Type:** Scientific/Data.
- **Statement:** Orts-/Territorialkontexte und Zugehörigkeiten müssen zeitbezogen und von modernen Navigations-/Gemeindegrenzen unterscheidbar sein; Scale Expansion benötigt einen expliziten historischen Relation-/Verwaltungs-/Mobilitäts-/Vergleichstrigger.
- **Rationale:** N-012; G-005.
- **Owner:** Landesgeschichte/historische Geographie.
- **Capabilities:** CAP-13.
- **Acceptance:** U1 Grenzraum erweitert sich über heutige `Teichplatte`, wenn Quellen-/Nutzungs-/Herrschaftsbeziehungen dies tragen; U2 Altenburg wird nicht allein wegen Namensähnlichkeit in Orla-Kontext integriert.
- **Risks:** RISK-11/-12.
- **Evidence:** C4, #46/#47.
- **Priority:** P1.
- **Status:** `accepted-v0.1`.

## REQ-ACT-001 – Akteursanalyse trennt Handlung, Motive, Zuschreibung und Struktur

- **Type:** Scientific/Functional.
- **Statement:** Für historische Akteursanalyse müssen beobachtete Handlung, zeitgebundene Rollen/Ressourcen/Relationen, Informationshorizont, mögliche Optionen/Zwänge, Selbstbeschreibung, Fremdzuschreibung, Motivhypothese und alternative Erklärungen unterscheidbar bleiben.
- **Rationale:** N-011/N-014.
- **Owner:** jeweilige Akteurs-/Periodenfachdomäne.
- **Capabilities:** CAP-14.
- **Acceptance:** U3 office+confession+network ohne Motivevidence kann keinen validierten Motive Claim erzeugen; T-RISK-05.
- **Risks:** RISK-09/-10/-13.
- **Evidence:** C5 (#37).
- **Priority:** P1.
- **Status:** `accepted-v0.1`.

## REQ-SYN-001 – Verschiedene Evidenzachsen bleiben getrennt vergleichbar

- **Type:** Scientific/Data/Functional.
- **Statement:** Wenn ein Problem mehrere Evidenzarten benötigt, müssen diese mit ihrer eigenen Datierung, Methode, Aussagekraft und Grenze getrennt geführt und vergleichbar dargestellt werden können.
- **Rationale:** N-013/N-014.
- **Owner:** beteiligte Fachdomänen.
- **Capabilities:** CAP-15.
- **Acceptance:** U2 `Ersterwähnung != Gründung`: Schriftbeleg, Archäologie, Onomastik und Besitzgeschichte stehen auf getrennten Achsen; U1 direkte Teichquelle ≠ retrospektiver Rezess/LiDAR-Hinweis.
- **Risks:** RISK-07/-14/-23.
- **Evidence:** C4/C6/C8, RC-U2-07, #47.
- **Priority:** P1.
- **Status:** `accepted-v0.1`.

## REQ-SYN-002 – Transdisziplinäre Synthese bewahrt Quellen-/Fachperspektiven und Alternativen

- **Type:** Scientific/Functional.
- **Statement:** Eine Synthese muss auf ihre Teilbefunde/Fachperspektiven rückführbar sein und konkurrierende oder inkommensurable Erklärungen sichtbar halten; sie darf keine einheitliche Scheinsicherheit erzeugen.
- **Rationale:** N-013/N-014; G-009.
- **Owner:** beteiligte Fachdomänen; Research Coordination integrativ.
- **Capabilities:** CAP-16.
- **Acceptance:** Reviewer kann für jede wesentliche Syntheseaussage erkennen, welche Fachperspektive/Evidenz sie trägt und welche Alternative offen bleibt.
- **Risks:** RISK-13/-14/-23.
- **Evidence:** C3/C6/C8.
- **Priority:** P1.
- **Status:** `accepted-v0.1`.

---

# 8. Human Control / Research UX / Validation Requirements

## REQ-UX-001 – Antwort→Finding→Quelle/Fundstelle→Methode ist navigierbar

- **Type:** Workflow/Human-control/Quality.
- **Statement:** Eine wesentliche Forschungsausgabe muss aus derselben kanonischen Datenbasis über progressive Sichten bis zu Finding, Quelle/Fundstelle, Evidenzstatus, Methode/Kompetenz, Unsicherheit/Kontroverse und Research History nachvollziehbar sein.
- **Rationale:** G-009; N-015/N-018.
- **Owner:** Research UX + Fachdomäne/RDM.
- **Capabilities:** CAP-17.
- **Acceptance:** T-RISK-10; Reviewer benötigt keine Chat-Historie zur Rekonstruktion.
- **Risks:** RISK-23/-24/-30.
- **Evidence:** C8 (#38).
- **Priority:** P0 architecture-driving.
- **Status:** `accepted-v0.1`.

## REQ-UX-002 – Research Owner kann challenge/correct/demote ohne Routine-Micromanagement

- **Type:** Human-control.
- **Statement:** Das System muss wesentliche Findings/Promotions anfechtbar, korrigierbar und demotierbar machen, zugleich aber mechanische Routine und deterministische Quality Checks ohne permanente Nutzerüberwachung ausführen können.
- **Rationale:** G-007/G-009; P-008/P-009; #9/#12.
- **Owner:** Governance/Human Factors + Fachdomäne/RSE.
- **Capabilities:** CAP-17, CAP-18, CAP-19.
- **Acceptance:** User muss keinen Index/OCR-Job einzeln freigeben, kann aber consequential Entity/Claim/Interpretation prüfen/korrigieren; Exceptions werden sichtbar.
- **Risks:** RISK-26/-27.
- **Evidence:** C3/C8/C9.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-VAL-001 – Validation Levels sind consequence-based und sichtbar

- **Type:** Validation/Workflow.
- **Statement:** Mindestens Candidate/Exploratory, Working Research, Consequential/Adversarial Review und Independent Expert Validated müssen unterscheidbar sein; Promotionstiefe richtet sich nach Risiko/Fachstandard.
- **Rationale:** N-019; #45.
- **Owner:** Fachdomäne + Research Integrity.
- **Capabilities:** CAP-18.
- **Acceptance:** ein offener Homonym-Candidate kann ohne Fachreview nicht dieselbe Stufe wie validated identity erhalten; Routinecandidate kann dennoch maschinell geprüft werden, wenn Regel formal hinreichend ist.
- **Risks:** RISK-08/-13/-16/-27.
- **Evidence:** C3/C9.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-VAL-002 – Externe Fachvalidierung wird nur dort verlangt/behauptet, wo sie real vorliegt oder fachlich erforderlich ist

- **Type:** Validation/Governance.
- **Statement:** Das System muss Trigger/Status für notwendige unabhängige Fachvalidierung unterstützen und darf diese nicht vortäuschen; nicht jede Working-Research-Aussage benötigt externen Review.
- **Rationale:** N-019; Lean QA.
- **Owner:** Fachdomäne/Research Integrity.
- **Capabilities:** CAP-02, CAP-18.
- **Acceptance:** `independent expert validated` enthält unabhängigen Reviewer/Provenienz; ansonsten Status bleibt niedriger; publikationsnahe consequential Claims können Reviewpflicht erzeugen.
- **Risks:** RISK-13/-27/-29.
- **Evidence:** C3, #45.
- **Priority:** P1.
- **Status:** `accepted-v0.1`.

---

# 9. Workflow / Canonical State / Technical Quality Requirements

## REQ-WF-001 – Formal prüfbare Invarianten werden deterministisch erzwungen

- **Type:** Technical quality / Scientific safeguard.
- **Statement:** Wo eine wissenschaftliche/technische Invariante formal prüfbar ist (z. B. erforderliche Parentage, erlaubter Statusübergang, kein direkter AI-Merge, Findspot-Referenz), darf ihre Verlässlichkeit nicht allein von Prompt-/LLM-Compliance abhängen.
- **Rationale:** N-017; #24.
- **Owner:** RSE/Validation Engineering; Fachdomäne besitzt Invariante.
- **Capabilities:** CAP-18, CAP-19.
- **Acceptance:** adversarial invalid candidate kann Promotion nicht durch generativen Text erzwingen; T-RISK-07.
- **Risks:** RISK-16/-28.
- **Evidence:** C9 (#39), #24.
- **Priority:** P0 architecture-driving.
- **Status:** `accepted-v0.1`.

## REQ-WF-002 – Processing/Search Workflows sind reproduzierbar und restartbar

- **Type:** Quality/Workflow.
- **Statement:** Wiederholbare mechanische Verarbeitung muss relevante Inputs/Outputs/Parameter/Processor-Versionen/Fehlerzustände so dokumentieren, dass sie reproduziert oder kontrolliert fortgesetzt werden kann.
- **Rationale:** G-007/G-008; N-015/N-017.
- **Owner:** RSE/RDM.
- **Capabilities:** CAP-19.
- **Acceptance:** unterbrochener OCR/Index/Search-Run kann ohne stillen Partial State fortgesetzt werden; consequential Output zeigt Processor-Kontext.
- **Risks:** RISK-18/-19/-26.
- **Evidence:** C7/C9.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-STATE-001 – Kanonischer Research State ist provider-/chat-unabhängig und portabel

- **Type:** Data/Portability/Interoperability.
- **Statement:** Kuratierte Sources/Findings/Claims/Interpretationen/Status/Provenienz müssen in einem dokumentierten, exportier-/wiederherstellbaren Zustand existieren, der nicht von Chat-Historie oder einem einzelnen AI-/Tool-/Cloud-Provider abhängt.
- **Rationale:** G-008; N-015/N-017.
- **Owner:** RDM/RSE/Governance.
- **Capabilities:** CAP-20.
- **Acceptance:** T-RISK-08 Provider removal; neuer Bearbeiter kann ohne Chat fortsetzen; RC-U2-08 bibliographische Corpus-Identität bleibt rekonstruierbar.
- **Risks:** RISK-17/-18/-19/-30.
- **Evidence:** C9, #12/#24, §14.
- **Priority:** P0 architecture-driving.
- **Status:** `accepted-v0.1`.

## REQ-STATE-002 – Kuratierter Zustand ist von regenerierbaren Indizes/Caches/Embeddings/Processor-Artefakten getrennt

- **Type:** Data/Architecture constraint.
- **Statement:** Das System muss wissenschaftlich kuratierten kanonischen Zustand von regenerierbaren technischen Artefakten unterscheiden können; Verlust/Rebuild eines Index/Cache/Embedding darf kuratierte Evidenz/Findings nicht zerstören.
- **Rationale:** G-008/G-012; #6/#12/#24.
- **Owner:** RDM/RSE.
- **Capabilities:** CAP-19, CAP-20.
- **Acceptance:** Suchindex kann gelöscht/rebuilt werden; curated Finding/Source links bleiben erhalten.
- **Risks:** RISK-17/-18/-28.
- **Evidence:** C9.
- **Priority:** P0 architecture-driving.
- **Status:** `accepted-v0.1`.

## REQ-INT-001 – Integrationen besitzen Escape Hatch / ersetzen nicht den kanonischen State

- **Type:** Interoperability.
- **Statement:** Externe Bibliographie-, OCR-, Archiv-, Such- oder AI-Dienste müssen so integrierbar sein, dass relevante Daten/Referenzen exportiert oder ersetzt werden können; ein externer Dienst darf nicht der einzige unexportierbare Träger kuratierten Forschungswissens werden.
- **Rationale:** N-020; G-008/G-012.
- **Owner:** RSE/RDM.
- **Capabilities:** CAP-20.
- **Acceptance:** Zotero-/Provider-/Processor-Wechsel ist möglich, ohne kuratierte Findings/Provenienz zu verlieren; spezifische Integration wird später prototypisch getestet.
- **Risks:** RISK-17.
- **Evidence:** C7/C9.
- **Priority:** P0.
- **Status:** `accepted-v0.1`.

## REQ-LEAN-001 – Neue technische Komponenten benötigen einen nachweisbaren Capability-/Quality-Mehrwert

- **Type:** Architecture governance / Quality.
- **Statement:** Eine neue technische Komponente/Abhängigkeit darf nur eingeführt werden, wenn sie auf priorisierte Requirements zurückführbar ist, die kleinste hinreichende Lösung geprüft wurde und ihr Nutzen gegenüber einer einfacheren/bestehenden Lösung verifizierbar ist.
- **Rationale:** G-011/G-012; N-020.
- **Owner:** Architecture/RSE; Requirement-/Fachowner kontrollierend.
- **Capabilities:** cross-cutting.
- **Acceptance:** KG/RAG/Multi-Agent/Vector DB etc. kann nicht allein wegen Verfügbarkeit in Architektur gelangen; Architecture Review dokumentiert Requirement, Alternative, Test, Komplexität/Lock-in.
- **Risks:** RISK-28/-29.
- **Evidence:** #1/#10/#24, C9.
- **Priority:** P0 Gate Constraint.
- **Status:** `accepted-constraint`.

---

# 10. Rights / Privacy / Boundary Requirements

## REQ-RGT-001 – External Processing benötigt source-/purpose-/service-spezifische Rights Admission

- **Type:** Rights/Security/Privacy constraint.
- **Statement:** Vor externer Verarbeitung von Material mit eingeschränktem/unklarem Status muss prüfbar sein, ob Access, Copy/TDM, Retention, External Processing, Publication/Sharing und ggf. Archiv-/Lizenzbedingungen die konkrete Operation erlauben oder eine Entscheidung nötig ist.
- **Rationale:** N-016.
- **Owner:** Legal/Rights/Data Governance + Research Owner bei nicht ableitbaren Fällen.
- **Capabilities:** CAP-21.
- **Acceptance:** T-RISK-09; `restricted/unknown` wird nicht ungeprüft an Cloud-/AI-Service übertragen.
- **Risks:** RISK-20/-21.
- **Evidence:** #40 current legal/rights evidence.
- **Priority:** P0 architecture-driving constraint.
- **Status:** `accepted-constraint`.

## REQ-RGT-002 – Privacy Screening bleibt für neuere/hybrid historische Materialien möglich

- **Type:** Privacy constraint.
- **Statement:** Das System muss Quellen/Bestände mit möglichem Bezug auf lebende Personen oder andere Datenschutz-/Schutzfrist-Risiken kennzeichnen und vor Verarbeitung/Sharing geeignete Policy-/Review-Schritte auslösen können.
- **Rationale:** N-016.
- **Owner:** Data Protection/Legal.
- **Capabilities:** CAP-21.
- **Acceptance:** moderner Quellenbestand mit lebender Person kann nicht allein wegen Projektlabel `historisch` als privacy-free markiert werden.
- **Risks:** RISK-22.
- **Evidence:** #40.
- **Priority:** P1, P0 wenn entsprechende Materialien aufgenommen werden.
- **Status:** `accepted-constraint`.

## REQ-BND-001 – Vermittlung darf kanonischen Research State nicht zurückschreiben

- **Type:** Governance/Data boundary.
- **Statement:** Downstream Vermittlungs-/Darstellungsprodukte dürfen Research Findings nicht außerhalb des normalen Research-/Promotionpfads mutieren; Rückverfolgung zur Forschungsbasis soll möglich bleiben.
- **Rationale:** G-010; #20.
- **Owner:** Governance/RSE.
- **Capabilities:** CAP-22.
- **Acceptance:** T-RISK-11; RGK-/Public-History-Edit verändert kein Histo-Orla-Finding.
- **Risks:** RISK-25.
- **Evidence:** C8, #20/#21.
- **Priority:** P0 Boundary; konkrete Übergabeschnittstelle P2.
- **Status:** `accepted-constraint`.

---

# 11. Architecture-driving Requirements Shortlist

Diese Requirements müssen Architekturvarianten explizit erfüllen/vergleichen:

1. **ADRQ-01 Source/Research Layer Integrity:** REQ-SRC-001/002/003/004 + REQ-EPI-004.
2. **ADRQ-02 Canonical State / Portability:** REQ-STATE-001/002 + REQ-INT-001.
3. **ADRQ-03 Deterministic Promotion/Invariant Boundary:** REQ-WF-001 + REQ-ENT-001 + REQ-VAL-001.
4. **ADRQ-04 Findspot-preserving Document Pipeline:** REQ-OCR-001/002 + REQ-SRC-004.
5. **ADRQ-05 Historical Retrieval Baseline:** REQ-RET-001/002/003/004; REQ-RET-005 as optional admission gate.
6. **ADRQ-06 Evidence/Criticism Model:** REQ-CRIT-001/002 + REQ-EPI-004 + REQ-EPI-005.
7. **ADRQ-07 Human-readable Audit from One State:** REQ-UX-001/002.
8. **ADRQ-08 Rights-aware Processing Boundary:** REQ-RGT-001/002.
9. **ADRQ-09 Replaceable Processor/Service Architecture:** REQ-WF-002 + REQ-STATE-002 + REQ-INT-001.
10. **ADRQ-10 Domain Non-flattening:** REQ-EPI-001/003 + REQ-SYN-001/002 + REQ-SPAT-001/REQ-ACT-001.
11. **ADRQ-11 Lean Admission:** REQ-LEAN-001.
12. **ADRQ-12 Research/Mediation Separation:** REQ-BND-001.

Diese Shortlist bleibt historische/inhaltliche Architektur-Clusterung der Baseline. Die aktuelle technische Ableitung nutzt zusätzlich `docs/architecture/requirements-derivation.md` mit expliziten Concerns, Dependencies, Research Questions und Candidate Approaches.

---

# 12. Requirement Dependency Map

```text
REQ-EPI-001/002/003
        ↓
REQ-SRC-005 Discovery
        ↓
REQ-SRC-001/002/003/004
        ↓↘
REQ-OCR-001/002/003     REQ-RET-001/002/003/004
        ↘                    ↙
          REQ-CRIT-001/002
              ↓↘
        REQ-ENT-001  REQ-REL-001
              ↓       ↓
      REQ-SPAT-001  REQ-ACT-001
              ↘       ↙
          REQ-SYN-001/002
                ↓
          REQ-UX-001/002
                ↕
          REQ-VAL-001/002

Cross-cutting:
REQ-WF-001/002
REQ-STATE-001/002
REQ-INT-001
REQ-RGT-001/002
REQ-BND-001
REQ-LEAN-001
REQ-EPI-004/005
```

Diese v0.1-Map ist **eine erste inhaltliche Abhängigkeitssicht**, nicht die vollständige technische Build-Reihenfolge. Neue Relationstypen `requires | refines | constrains | conflicts_with | supersedes` werden gemäß `requirements-structure.md` bei aktiver Bearbeitung präzisiert.

---

# 13. Traceability Matrix – Need/Pain → Capability → Requirement → Acceptance

| Need/Pain | Capability | Requirements | primary Acceptance/Falsification |
|---|---|---|---|
| N-001/P-001 unknown vocabulary | CAP-01 | EPI-002/003 | U2 near-concepts; U1 archive/problem vocabulary |
| N-002/003/P-007 expertise gap | CAP-02 | EPI-001, VAL-002 | U1/U2/U3 routing Gold Cases |
| N-004/P-002/006 archive discovery | CAP-03 | SRC-005 | U1 Arnshaugk multi-series routing |
| N-005 source status | CAP-04/08 | SRC-001/002/003 | Findmittel≠source; `[Stange]` layer |
| N-006/P-004 findspot | CAP-04/05/06 | SRC-004, OCR-002 | U4 findspot roundtrip |
| N-007/P-003 OCR | CAP-05 | OCR-001/002/003 | critical-token + page Gold Corpus |
| N-008/P-005 variants | CAP-06 | RET-001/002/003 | U2 variant recall/query log |
| negative/completeness risk | CAP-07 | RET-004 | U2 bounded negative finding |
| N-009 dependency | CAP-09 | CRIT-001 | charter→regest→edition lineage |
| N-010 discrepancy | CAP-10 | CRIT-002/EPI-004 | 1374/1378 unresolved |
| homonym pain | CAP-11 | ENT-001 | Altenburg/Orla Knau no auto-merge |
| N-011 relation/motive | CAP-12/14 | REL-001/ACT-001 | Knewe/Stange; U3 motive test |
| N-012 multi-scale | CAP-13 | SPAT-001 | #47 Grenzraum relation-triggered scale |
| N-013/014 multi-evidence | CAP-15/16 | SYN-001/002 | first mention≠foundation; U1 evidence layers |
| G-009/N-018 audit | CAP-17 | UX-001/002 | reviewer without chat |
| N-019 validation | CAP-18 | VAL-001/002/EPI-005 | AI≠L3; candidate promotion |
| G-007/N-017 automation | CAP-19 | WF-001/002 | restartable processing; no AI canonical mutation |
| G-008/N-015 portability | CAP-20 | STATE-001/002/INT-001 | provider removal/restore |
| N-016 rights | CAP-21 | RGT-001/002 | restricted material admission |
| G-010 mediation | CAP-22 | BND-001 | downstream no back-write |

---

# 14. Conflict / Trade-off Register

No unresolved **requirement conflict** currently requires #44. Relevant design trade-offs are bounded:

## T-01 Automation vs. Human Control

Not a contradiction. REQ-UX-002/VAL-001 define proportional control: automate mechanics; review consequential judgment.

## T-02 Portability vs. Cloud/External Processing

Not a contradiction. REQ-STATE-001 requires portable canonical state, not exclusively local computation. External processors may be replaceable if REQ-RGT-001/INT-001 hold.

## T-03 Rich Domain Modeling vs. Lean

Not a contradiction. REQ-EPI/SYN require enough representation to preserve domain distinctions; REQ-LEAN-001 forbids complexity without validated distinction/quality benefit.

## T-04 Semantic Search vs. Exact Search

Not a contradiction. Exact/auditable is baseline; semantic layer optional and benchmark-admitted.

## T-05 Zotero integration vs. independent Research State

Architecture question, not requirement conflict. Zotero is strong integration candidate; architecture must prove how bibliographic identity/integration coexists with portable curated Research State.

---

# 15. Deferred / Research-needed Requirement Candidates

These do **not** block architecture comparison:

1. complete regional Gazetteer/Territorial chronology – iterative corpus asset, not prerequisite;
2. full Expertise Profiles for all possible disciplines – build by prioritized use cases;
3. exact L3 external specialist triggers for every domain – refine per domain/publication consequence;
4. concrete UI accessibility metrics/components – prototype/research UX phase;
5. exact performance/scale SLOs – no observed corpus bottleneck yet;
6. final Histo-Orla→RGK exchange format – only boundary requirement accepted;
7. corpus-specific OCR/HTR engine choice – benchmark question;
8. map OCR/layout special cases – benchmark after representative material;
9. specific archive/license processing policies – source/service-specific at integration time;
10. U3 domain-specific Gold Situation Template – live case needed but method requirement already stable.

---

# 16. Explicit Architecture Choices – NOT Requirements

- files vs. SQLite vs. PostgreSQL vs. graph store;
- FTS5 vs. Lucene/Solr/Elasticsearch/etc.;
- Zotero-first vs. Zotero-adapter details;
- TEI/PAGE/ALTO/METS/RiC exact adoption choices;
- vector database / embeddings / RAG;
- Knowledge Graph / ontology scope;
- single assistant vs. multi-agent;
- local vs. cloud OCR/HTR/LLM processor;
- web/desktop/CLI application framework;
- sync/job orchestration technology.

Diese bleiben technische Kandidaten. Ihre Prüfung folgt aktuell `docs/architecture/requirements-derivation.md` und nicht einem separaten Vorab-Gate.

---

# 17. U1–U4 Acceptance Coverage

## U1 – historische Teich-/Feucht-/Landnutzungslandschaft

Covers: archive routing, historical terminology, source status, multi-scale, retrospective evidence, rights, cross-evidence synthesis, audit.

Critical tests: SRC-005, RET-004, SPAT-001, SYN-001, UX-001.

## U2 – mittelalterliche Knau/Orlagau Quellenbeziehungen

Covers: source/editorial layers, entity resolution, variants, negative findings, discrepancy, relations/proxies, settlement chronology, restartability.

Critical tests: SRC-003, RET-002/004, CRIT-002, ENT-001, REL-001, SYN-001, STATE-001.

## U3 – frühneuzeitlicher adliger Akteur

Covers: expertise routing, relation evidence, temporal context, actor situation, motives, alternatives, validation.

Critical tests: EPI-001, REL-001, ACT-001, SYN-002, VAL-001.

## U4 – persönliches Quellenarchiv / OCR / Retrieval

Covers: source identity, derivative/page mapping, exact search, query provenance, portability/restartability, automation, rights.

Critical tests: SRC-004, OCR-001/002/003, RET-001/003/005, WF-002, STATE-001/002, RGT-001.

**Coverage conclusion:** All architecture-driving clusters have at least one representative acceptance case; most cross-cutting invariants have two or more.

---

# 18. #45 Quality Check

- **Domain fit:** fachliche Owner pro Requirement explizit; Software bleibt beratend/umsetzend.
- **Evidence fit:** Requirements derive from #28–#41; Live-Candidates only where cross-supported.
- **Inference fit:** Requirements do not promote unresolved historical findings; they encode observed method/quality needs.
- **Terminology fit:** Requirement/Capability/Constraint/Architecture Choice separated.
- **Provenance fit:** each requirement points to Needs/Capabilities/SOTA/Risks/Use Cases.
- **Falsification/challenge:** every P0/P1 requirement has an acceptance criterion or named test family.

## Sättigung

`Sufficient for Architecture Readiness assessment.`

Diese historische Sättigungsbegründung bleibt Provenienz des v0.1-Durchlaufs. Die aktuelle iterative Requirements-Arbeit läuft weiter über `requirements-extensions.md` und `requirements-structure.md`; technische Ableitungen werden just in time nach `docs/architecture/requirements-derivation.md` geprüft.
