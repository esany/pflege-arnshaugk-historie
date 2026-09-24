# Unabhängige Gesamtanalyse Histo-Orla – 2026-09-24

**Work Owner:** #142  
**Status:** `independent-analysis-fixed-before-internal-audit-comparison`  
**Primäre Funktion:** unabhängiger transdisziplinärer Review (historische Fachwissenschaft + transdisziplinäre Integrationsmethodik + Software Engineering)  
**Evidenzstichtag:** 2026-09-24  
**Audit-Quarantäne:** Die diagnostischen Inhalte von #64, #70, #121, PR #116/#118/#120 sowie späteren Audit-Zusammenfassungen waren für diese Fassung gesperrt.  
**Wichtige Verfahrensabweichung:** Beim Abruf der chronologischen Owner-Kommentare zu #9 wurde unbeabsichtigt ein als „Audit 2026-08-31“ bezeichneter Kommentar mitgeliefert. Dessen diagnostische Aussagen werden in den Phasen 1–6 **nicht als Evidenz verwendet**. Damit ist die Blindheit gegenüber allen internen Audit-Inhalten jedoch formal nicht mehr vollständig; diese Einschränkung bleibt Teil der Ergebnisgrenze.

## Evidenznotation

- **B** – direkt im Repository oder externer Quelle beobachtet.
- **O** – erkennbar vom Owner geäußert; GitHub-Kommentare unter dem Account `esany` werden nur dann als O behandelt, wenn sie ausdrücklich Owner-Korrektur/-Constraint/-Feedback wiedergeben. Da auch diese Texte KI-formuliert sein können, bleibt die Autorenschaft im Wortlaut teilweise unsicher.
- **K** – KI-formulierte Projektstruktur/-Aussage ohne nachweisbare unabhängige menschliche Prüfung.
- **E** – externe Fachliteratur, Standards, Studien oder Vergleichssysteme.
- **F** – Folgerung dieses Reviews; immer mit Konfidenz.

---

# 1. Zusammenfassung

### Zentraler Befund 1 – der reale Intent ist stabiler als die wechselnde Projektsprache

**F / Konfidenz hoch.** Über frühe Issues, spätere Owner-Korrekturen und reale Workflow-Rückmeldungen hinweg bleibt ein Kernbedarf stabil: Der Owner möchte historische Fragen stellen können, ohne selbst alle benötigten Fachsprachen, Quellenwege und Softwaremechanismen beherrschen zu müssen, dabei aber die wissenschaftliche Nachprüfbarkeit bis zur konkreten Quelle/Fundstelle behalten. Technik soll Such-, Ordnungs-, Persistenz- und Routinearbeit übernehmen, nicht fachliche Autorität simulieren.

Gegenhypothese: Die starke Wiederholung dieses Zielbilds kann teilweise Ergebnis KI-generierter Selbstbeschreibung sein. Dagegen spricht, dass konkrete Owner-Korrekturen wiederholt technische oder konzeptionelle Vorschläge zurückweisen: `Zotero = alleiniger Source of Truth` wurde verworfen (#3), „MVP“ als zusätzliche Steuerung wurde entfernt (#9/#44), ein statisches Modulkonzept im U2-Fall wurde ausdrücklich als NOT PASS markiert (#63), und eine maschinenorientierte Auditansicht wurde nach realer Nutzung als zu kryptisch zurückgewiesen (#63).

### Zentraler Befund 2 – Histo-Orla ist derzeit stärker ein Forschungs-/Assurance-Systembauprojekt als ein historisches Forschungsprojekt

**F / Konfidenz hoch.** Die Issue-Chronologie zeigt eine sehr große Dichte an Governance-, SOTA-, Requirements-, Architecture-, Assurance- und Delivery-Work-Ownern (#1–#63), während die eigentliche historische Live-Forschung zunächst in #46/#47 und später u. a. #85/#86/#103 konzentriert ist. Die Repository-Dokumentation und der aktuelle Code bestehen zu einem erheblichen Teil aus Regeln, Traceability, Validatoren, Work-Context-, Requirements- und Assurance-Mechanismen.

Eine exakte Datei-/Zeilen-/Commitquote „Forschung vs. Meta“ konnte mit dem verfügbaren GitHub-Connector nicht reproduzierbar erhoben werden, weil keine vollständige Tree-/LOC-Schnittstelle verfügbar war. Der qualitative Befund ist deshalb stark, eine Prozentzahl wäre erfunden.

Gegenhypothese: Ein großer Teil dieser Meta-Arbeit ist notwendige Infrastruktur, weil der Owner doppelt fachfremd ist und wechselnde KI-Kontexte sonst State, Authority und Evidenz verwechseln. Diese Gegenhypothese wird durch reale Fehlerfunde der Validatoren und Owner-Korrekturen gestützt. Sie widerlegt aber nicht die Kostenfrage.

### Zentraler Befund 3 – die stärkste Qualität liegt in der expliziten Trennung epistemischer Ebenen; die schwächste in unabhängiger fachlicher Validierung und proportionaler Prozesslast

**F / Konfidenz hoch.** Source/Instance/Derivative/Findspot/Excerpt/Finding/Interpretation werden im Source-Identity-Protokoll und in den Live-Cases ungewöhnlich konsequent getrennt. U2 dokumentiert beispielsweise editorische Ergänzung versus historischen Wortlaut, Homonym-Risiken, bounded negative findings und eine offene 1374/1378-Diskrepanz statt sie wegzuentscheiden. #103 markiert nicht inspizierte Editionen und sekundäre Synthesen sichtbar als solche.

Demgegenüber ist kein belastbarer Nachweis vorhanden, dass die zentralen historischen Findings bereits durch unabhängige qualifizierte Fachhistoriker:innen, Archivar:innen oder Diplomatiker:innen geprüft wurden. Das Projekt erkennt diese Grenze selbst an; Anerkennung ersetzt die externe Prüfung nicht.

### Zentraler Befund 4 – die Software ist klein und formal diszipliniert, aber ihr Nutzennachweis ist jünger und schwächer als ihr Assurance-Apparat

**F / Konfidenz hoch.** Die inspizierten Python-Validatoren sind überschaubar, lesbar und haben klar begrenzte Zuständigkeiten. Tests enthalten positive und negative Fälle; ein dokumentierter realer Failure-Fall (REQ007 beim WP1-Handoff) zeigt, dass die Checks nicht nur dekorativ sind. Gleichzeitig ist die technische Hauptleistung bislang überwiegend Assurance/State/Traceability, nicht die vom Owner ursprünglich gewünschte breite Forschungsassistenz (Retrieval, Quellenarbeit, nutzernahe Forschungsoberfläche). Reales Owner-Feedback vom 2026-09-23 bestätigt, dass ein technisch korrekter WP1-Output noch nicht die benötigte research-facing Form hatte.

### Zentraler Befund 5 – die Genese zeigt wiederholte Korrekturkaskaden

**F / Konfidenz mittel-hoch.** Muster: ein plausibles Konzept wird formuliert → reale Nutzung/Owner-Korrektur zeigt einen semantischen oder Workflow-Mismatch → das Projekt ergänzt Governance, Traceability, neue Work Owner oder Validatorregeln. Beispiele sind Zotero-Rollenklärung, Work-Context/Handoff, Value→Delivery→Feedback-Assurance, CI-Noise-Korrektur, Demotion des Modulkonzepts und die Korrektur von audit-/maschinenzentrierter Darstellung hin zu excerpt-zentrierter Quellenarbeit.

Gegenhypothese: Dies ist normale agile Lernarbeit. Das stimmt teilweise; problematisch wird das Muster erst, wenn die Korrekturkosten überwiegend neue Meta-Strukturen erzeugen und der Forschungsnutzen nicht proportional steigt.

### Wichtigste Evidenzlücken

1. keine vollständige maschinelle Repository-Tree-/LOC-Inventur im verfügbaren Connector;
2. keine vollständige, unabhängige Verifikation aller historischen Zitate/Signaturen;
3. keine unabhängige fachwissenschaftliche Peer-Review der Live-Findings;
4. keine belastbaren DORA-Metriken im Sinn eines laufenden Produktionssystems;
5. keine belastbare Messreihe „Zeit von Forschungsfrage bis geprüftem Ergebnis“;
6. Owner-vs.-KI-Autorenschaft vieler Repository-Texte ist trotz Account-Provenienz nicht sicher trennbar;
7. `Wissensarbeit` war nur teilweise zugänglich (README, keine Root-Governance-Dateien unter erwarteten Pfaden); `paleo-type` und `rgk-main-ssot` waren teilweise zugänglich.

---

# 2. Evidenzbasis und Lücken

## 2.1 Repository-Inventar

**B.** Repository: `esany/pflege-arnshaugk-historie`, öffentlich, Default Branch `main`, GitHub-Metadaten-Größe 1557 KB. Issues reichen mindestens von #1 bis #142 mit Nummernlücken durch PRs. Die Connector-Suche lieferte die Projekt-Issues #1–#68, #70, #85–#89, #92, #103, #121, #138 und den Review-Owner #142.

**B.** Aktuelle kanonische Einstiege wurden frisch gelesen: `AGENTS.md`, `PROJECT_STATE.md`, `README.md`, #45 und `docs/research/source-identity-protocol.md`. Für diesen Review wurde #142 als Work Owner angelegt.

**B.** Inspizierte Forschungsartefakte umfassen mindestens:
- `problem-baseline.md`;
- U2 Knau/Orlagau Findings und Exzerptregister;
- U1 Teich-/Feuchtkulturlandschaft;
- #103 Anno/Richeza/Saalfeld Observation-/Relationsregister und Source Ledger.

**B.** Inspizierte technische Artefakte umfassen mindestens:
- Requirements Baseline/Extensions und Coverage;
- `tools/requirements/validate.py`;
- `tools/assurance/validate.py`;
- `tools/operational/core.py` und Execution-Order-Logik;
- Requirements-/Assurance-Regressionstests;
- `.github/workflows/project-assurance.yml`;
- Operational Execution Architecture und Prior-Art-Input.

## 2.2 Interne Audits – nur Existenzregistrierung vor Phase 7

**B.** Vorhanden sind mindestens #64 „Product- und Research-Value gegen Governance-Komplexität absichern“, #70 „AI-resilientes Projekthandling …“, #121 „Independent blind replication audit of project development“ sowie PRs #116/#118/#120. #138 trägt den Titel „Ganzheitliche Analyse von Intent, Forschung, Technik und Genese“. Diagnostischer Inhalt wurde für diese Fassung nicht als Evidenz benutzt.

## 2.3 Prior Art

**B.** `paleo-type`: Governing Objective, AGENTS und README zugänglich. Es besitzt bereits stark ausgearbeitete Trennungen von Evidence/Plausibility, Observation/Reading/Normalization/Identification/Interpretation, Human Owner vs. Specialist und canonical vs. derived state.

**B.** `Wissensarbeit`: README zugänglich; erwartete Root-Dateien `GOVERNING_OBJECTIVE.md` und `AGENTS.md` waren über die geprüften Pfade nicht zugänglich/nicht vorhanden. README beschreibt Git-native, KI-gestützte Wissensarbeit mit Operational Spine und deterministischen Guards.

**B.** `rgk-main-ssot`: README und AGENTS zugänglich; stark task-/SSOT-orientierter Arbeitsmodus.

**F / mittel-hoch.** Histo-Orla hat aus Prior Art nicht bloß Code, sondern vor allem Governance- und Zustandsmuster übernommen. Die dokumentierte Absicht, Prior Art nur als Challenge Input zu verwenden, ist klar; dennoch erhöht die strukturelle Ähnlichkeit das Risiko, dass vorhandene Lösungsmuster den Problemraum vorstrukturieren.

---

# 3. Chronologische Rekonstruktion

## Phase A – frühe Produktidee

**B.** #1–#10 zeigen einen Start aus konkreten Bedürfnissen: persönlicher Archivar, OCR/Volltext, fundstellenfähige Suche, Zotero, Git-Provenienz, KI-Unabhängigkeit und ein breiterer transdisziplinärer Assistent. Früh ist bereits die Spannung zwischen konkreter Quellenarbeit und großem Assistenz-Zielbild sichtbar.

**O/K unsicher.** Der Owner korrigiert #3 später explizit: OneDrive = Source of Bytes, Zotero = bibliographisch/archivische Verwaltung, Histo-Orla = wissenschaftlicher Research State. Dies ist ein konkreter, prüfbarer Workflow-Constraint und stärker als die frühere Lösungshypothese.

## Phase B – Problem-/SOTA-/Requirements-Expansion

**B.** #28–#45 zerlegen das Projekt in Problem-/Need-/Pain-Baseline, reale Workflows, neun SOTA-Stränge, Risk Review, Capability/Quality Catalogue, Requirements, Architecture Readiness und Research Protocol.

**F / hoch.** Diese Phase verbessert begriffliche Trennschärfe und Traceability, verschiebt aber den Schwerpunkt stark von „historisch forschen“ zu „ein System definieren, das korrekt forschen können soll“.

## Phase C – Live Research als Realitätstest

**B.** #46/#47 beginnen konkrete historische Arbeit. U2 enthält überprüfbare Editions-/Quellenbezüge, offene Diskrepanzen, Homonym-Fehlerfälle, Search Boundaries und explizite Grenzen der Aussagekraft. #47 erweitert die Forschung in Kulturlandschaft/Feuchtgebiete.

**F / hoch.** Erst hier entstehen belastbare Hinweise, welche abstrakten Regeln tatsächlich gebraucht werden. Live Research fungiert gleichzeitig als Forschung und als System-Testfixture; diese Doppelrolle ist produktiv, birgt aber die Gefahr, Forschungsfragen nach Systemtest-Nutzen auszuwählen.

## Phase D – technische Operationalisierung und Assurance

**B.** #48–#63 führen Technical Lead, Zotero/OneDrive-Spike, Canonical State, Document/Findspot, Retrieval, Promotion, Audit View, Rights, Restartability, Domain Method Profiles, Work-Context Assurance, Requirements Harness und Value/Decision/Delivery/Feedback Assurance ein.

**B.** Die inspizierten Validatoren prüfen explizit nur formale Invarianten und deklarieren, keine historische Wahrheit oder Methodensuffizienz zu beurteilen.

**O.** Reales Owner-Feedback dokumentiert CI-Noise, manuelle/chat-orchestrierte Research-Arbeit, einen NOT-PASS für ein zu statisches Modulkonzept und später die Unzulänglichkeit einer kryptischen Auditdarstellung als research-facing Oberfläche.

## Phase E – Pilot-/Reframing-Schleifen

**B/O.** #85 zeigt einen Pilot, der zunächst in Richtung Besucher-/Vermittlungsslice driftete und nach Owner-Feedback korrigiert wurde. #103 zeigt einen neueren Research-Strang, der Source Ledger, unresolved states und source-first Erweiterbarkeit stärker betont.

**F / hoch.** Die Projektgenese ist nicht linear. Sie besteht aus wiederholter Reframing-Arbeit, bei der frühere Konzepte erhalten, superseded, demoted oder enger gerahmt werden.

---

# 4. Intent und Bedürfnisse

| Gegenstand | Ebene | Herkunft/Evidenz | Symptom-Test | Konfidenz |
|---|---|---|---|---|
| Historische Fragen ohne vollständige eigene Fachausbildung bearbeiten | zugrunde liegendes Bedürfnis | O/B: wiederkehrende Owner-Korrekturen + #1/#2 | kein Symptom; Kernbedarf | hoch |
| Quellen/Fundstellen zuverlässig wiederfinden | Need | B: #2/#4/#5, Live Research | direktes Forschungsproblem | hoch |
| unscharfe Alltagssprache in Fachfragen übersetzen | Need | O/B: #9 + Problem Baseline | direktes Kompetenzproblem | hoch |
| Zotero-Kopplung | Lösung/Capability | O/B: #3 korrigiert | Symptom einer Bibliographie-/Datei-/State-Trennung | hoch |
| GitHub als Projektgedächtnis | organisatorische Lösung | B/K/O | Reaktion auf Kontextverlust/Restartability-Pain | hoch |
| umfangreiche Work-Owner-/Handoff-Governance | Lösung/Assurance | B/K/O | Reaktion auf KI-Kontext- und Authority-Drift | hoch |
| Requirements Harness / Assurance Spine | technische Lösung | B | Reaktion auf stale/inkonsistente technische Zustände | hoch |
| Domain Method Profiles | Capability/Qualitätssicherung | B | Reaktion auf Gefahr generischer KI-Fachprosa | hoch |
| research-facing visuelle/excerpt-zentrierte Ansicht | Need/UX | O: reale WP1-Nutzung | Reaktion auf zu maschinenzentrierte Darstellung, aber selbst realer Workflow-Bedarf | hoch |
| Multi-Agent-/Rollenökosystem | Lösungshypothese | K/B, mehrfach begrenzt | eher Symptom des Kompetenzrouting-Problems | mittel |
| maximale Governance-Dichte | kein belegter Owner-Bedarf | F | wahrscheinlich Nebenprodukt von Fehlerkorrektur/AI-State-Sicherung | mittel |

### Verborgene Bedürfnisse

**F / hoch:** Der Owner braucht nicht primär „Autonomie der KI“, sondern **delegierbare Arbeit ohne delegierte epistemische Letztentscheidung**. Falsifikation: Wenn reale Nutzung zeigt, dass der Owner bewusst Black-Box-Antworten ohne Quellen-/Challenge-Pfad bevorzugt, wäre diese Hypothese falsch.

**F / mittel-hoch:** Ein zweites verborgenes Bedürfnis ist **kognitive Entlastung**. Viele Regeln adressieren zwar wissenschaftliche Sicherheit, Owner-Feedback lehnt aber kryptische oder verwaltungszentrierte Oberflächen ab. Falsifikation: Wenn der Owner im realen Forschungsalltag die vollständige technische Trace-Ansicht als primäre Arbeitsoberfläche bevorzugt.

**F / mittel:** Ein drittes Bedürfnis ist **Schutz vor den Fehlern des eigenen KI-Entwicklungsprozesses**. Das Projekt baut zunehmend Mechanismen gegen Chatverlust, falsche Promotion, stale State und Authority Drift. Gegenhypothese: Diese Mechanismen wären auch ohne KI nötig; teilweise stimmt das, die Dichte und Terminologie sind jedoch stark auf KI-Kontextwechsel zugeschnitten.

---

# 5. Soll, Ist, Genese

## 5.1 Soll

**B.** Früh und aktuell soll Histo-Orla kein bloßes Konzeptpapier sein, sondern ein dauerhaft nutzbares privates Forschungswerkzeug: Quellen erschließen, historische Fragen fachlich übersetzen, domänenspezifische Methoden aktivieren, Forschung restartbar halten und Ergebnisse bis zur Evidenz zurückführen.

## 5.2 Ist

**B/F hoch.** Das Repository ist aktuell zugleich:
1. historisches Research Repository;
2. Requirements-/Governance-System;
3. Architecture-/RSE-Labor;
4. Assurance-/Traceability-System;
5. Pilotfeld für KI-gestützte Wissensarbeit.

Diese Rollen sind dokumentiert getrennt, konkurrieren aber um dieselbe Einzelpersonen-Kapazität.

### Forschungsinhalt vs. Meta-Arbeit

Eine exakte Prozentmessung ist wegen fehlender vollständiger Tree-/LOC-Schnittstelle nicht seriös möglich. Qualitativ ist die Asymmetrie deutlich: Zwischen #28 und #63 liegen mehr als dreißig überwiegend methodische, Requirements-, Architecture- oder Assurance-Work-Owner; die historischen Kern-Live-Owner sind in diesem Abschnitt #46/#47. Später kommen weitere Research-/Pilotowner hinzu.

**F / hoch:** Prozesslast ist derzeit ein wesentlicher Teil des Produkts geworden.

## 5.3 Genese

### Mechanismus A – Solution hypothesis → correction → formal guard

Beispiele: Zotero-SoT-Hypothese → klare Dreiteilung; Requirements-QA → zusätzliche Value/Feedback Assurance; Audit View → research-facing UX-Korrektur.

### Mechanismus B – KI-Kontextverlust → explizitere Repository-Governance

GitHub wird zum kanonischen Gedächtnis, dann kommen Work Owner, Bootstrap, Handoff, Work Context, Traceability und Validatoren.

### Mechanismus C – abstraktes Design → Live Case → semantische Korrektur

Live Research deckt auf, dass generische Begriffe („Modul“, „Audit View“, relationale Kurzform) für konkrete Quellenarbeit zu grob oder zu technisch sein können.

### Mechanismus D – Prior Art als Beschleuniger und möglicher Attraktor

`paleo-type` und `Wissensarbeit` liefern starke Muster. Das spart Neuerfindung, kann aber auch dazu führen, dass Histo-Orla Probleme in bereits bekannten Kategorien formuliert.

## 5.4 Nachhaltigkeit für eine Einzelperson

**F / Konfidenz hoch:** Der aktuelle Umfang ist langfristig nur tragbar, wenn ein großer Teil der Governance/Traceability **automatisch und unsichtbar** funktioniert. Als manuell zu pflegendes System ist die Last für eine einzelne fachfremde Person unverhältnismäßig.

Externe DH-Literatur beschreibt genau die langfristige Belastung durch individuelle Software, Formate, Plattformen, Wartung und institutionelle Abhängigkeiten; nachhaltige Projekte benötigen bewusste Reduktion und Wartungsplanung (Barats/Schafer/Fickers 2020; King’s Digital Lab 2019).

---

# 6. Qualitätsbefunde

## 6.3 Sprach- und Strukturmuster KI-generierter Artefakte

### Q-AI-01 – hohe Template- und Taxonomie-Dichte
- **Beobachtung:** wiederkehrende Formen wie Status/Owner/Scope/Non-goals/DoD/Stop Rule, Pfeilketten, ID-Taxonomien und mehrstufige Authority-Klassen.
- **Klasse:** B/K.
- **Schwere:** mittel.
- **Auswirkung:** erhöht Restartability, kann aber semantische Stabilität vortäuschen und Leselast erzeugen.
- **Konfidenz:** hoch.
- **Gegenhypothese:** standardisierte Formen sind gerade bei KI-Kontextwechsel nützlich; das ist nachweisbar der Fall.

### Q-AI-02 – Begriffe werden häufiger präzisiert als gelöscht
- **Beobachtung:** neue Schichten entstehen oft als Präzisierung/Supersession älterer Begriffe.
- **Klasse:** B/F.
- **Schwere:** mittel.
- **Auswirkung:** historisch nachvollziehbar, aber kumulative Komplexität.
- **Konfidenz:** mittel-hoch.

## 6.4 Transdisziplinäre Qualität

### TD-01 – Problemkonstitution
- **Beobachtung:** Problem Baseline trennt Goals, Needs, Pains, Challenges, Risks und Lösungshypothesen; reale Fälle U1/U2 dienen als Test.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Auswirkung:** starke explizite Problemrahmung.
- **Konfidenz:** hoch.

### TD-02 – Wissensarten
- **Beobachtung:** Systemwissen, Zielwissen und Transformationswissen werden nicht mit diesen klassischen Begriffen durchgängig geführt, funktional aber über Research State, Goals/Requirements und Delivery getrennt.
- **Klasse:** F.
- **Schwere:** niedrig.
- **Konfidenz:** mittel.

### TD-03 – disziplinäre Fundierung
- **Beobachtung:** Domain Method Profiles sollen Fachstandards operationalisieren; mehrere sind noch im Aufbau. Live Research ist methodisch vorsichtig, aber unabhängige Fachvalidierung fehlt.
- **Klasse:** B/F.
- **Schwere:** hoch.
- **Auswirkung:** transdisziplinäre Integration kann nicht stärker sein als die disziplinäre Validität ihrer Teile.
- **Konfidenz:** hoch.

### TD-04 – Integration
- **Beobachtung:** U2 verbindet Diplomatik, Archivistik, Landesgeschichte, Onomastik und Archäologie, hält Evidenztypen getrennt.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Grenze:** bislang mehr koordinierte Mehrperspektivität als extern validierte integrative Erkenntnis.

### TD-05 – epistemische Rollen
- **Beobachtung:** Owner, Domain Authority, Technical Delivery und Specialist Validation werden ausdrücklich getrennt.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Restproblem:** dieselbe KI erzeugt häufig Research, Requirements, Architektur und Review; formale Rollentrennung ist keine echte personelle Unabhängigkeit.

### TD-06 – Reflexivität
- **Beobachtung:** reale Korrekturen führen nachweislich zu verändertem Vorgehen.
- **Klasse:** B/O.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Gegenbefund:** Korrekturen erzeugen häufig zusätzliche Regeln; Lernfähigkeit und Regelwachstum sind gekoppelt.

### TD-07 – Technik als soziotechnisches System
- **Beobachtung:** Technik wird explizit als subsidiär bezeichnet; der aktuelle technische Schwerpunkt liegt dennoch stark auf Projekt-/Assurance-Mechanik.
- **Klasse:** B/F.
- **Schwere:** mittel-hoch.
- **Konfidenz:** hoch.

### Externer Maßstab
ISOE/Bergmann et al. behandeln Qualität transdisziplinärer Forschung als eigenständige formative Evaluationsfrage. Belcher et al. bündeln Qualität in Relevanz, Glaubwürdigkeit, Legitimität und Wirksamkeit; Boix Mansilla/Duraisingh betonen disziplinäre Fundierung, Integrationsfortschritt und kritische Reflexivität. Histo-Orla ist bei Reflexivität/Explizitheit stark, bei unabhängiger disziplinärer Glaubwürdigkeit und nachgewiesener Wirksamkeit noch schwach.

## 6.5 Historische Forschung

### HIST-01 – Belegpraxis und Fundstellen
- **Beobachtung:** U2 nennt Edition, Nummer, Datum und teils historische Archivangabe; #103 Source Ledger trennt Inspektionsstatus.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### HIST-02 – Quellenhierarchie
- **Beobachtung:** Original/Edition/Regest/Register/Sekundärliteratur/OCR werden ausdrücklich getrennt.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### HIST-03 – Quellenkritik
- **Beobachtung:** U2 erkennt editorische Ergänzung `[Stange]`, Registeridentifikation und Überlieferungsstatus als eigene Ebenen; #103 markiert Lampert als narrative Quelle mit rhetorischem Bias.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### HIST-04 – Nachprüfbarkeit
- **Beobachtung:** Mehrere tragende U2-Belege sind bibliographisch präzise, aber heutige Archivkonkordanzen/Originalinspektion bleiben teilweise offen.
- **Klasse:** B.
- **Schwere:** mittel.
- **Konfidenz:** hoch.

### HIST-05 – Negativbefunde
- **Beobachtung:** U2 F-U2-006 begrenzt „nicht gefunden“ auf konkreten Editionsband und Suchvarianten.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### HIST-06 – 1374/1378 Knau
- **Beobachtung:** U2 behandelt den Konflikt ausdrücklich als unresolved. Externe Webquellen reproduzieren tatsächlich beide Daten: Wikipedia 1374; Naturpark Thüringer Schiefergebirge 1378.
- **Klasse:** B/E.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Auswirkung:** gutes Beispiel dafür, dass das Projekt einen realen Widerspruch nicht künstlich glättet.

### HIST-07 – externe Stichprobe Lampert 1071
- **Beobachtung:** #103 nennt Lamperts 1071er Saalfeld/Siegburg-Bezug; Deutsche Biographie bestätigt die Informationsreise 1071, und eine zugängliche Robinson-Edition/Preview gibt die Passage zu Saalfeld, Kanonikern und Mönchen aus Siegburg/St. Pantaleon wieder.
- **Klasse:** B/E.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### HIST-08 – externe Stichprobe Richeza/Saalfeld
- **Beobachtung:** #103 führt Richezas Saalfeld/Coburg-Übertragung als moderne Synthese mit offener Primärquellenkollation. Deutsche Biographie bestätigt die moderne Forschungsdarstellung, dass Saalfeld/Coburg 1056 unter lebenslänglicher Nutzung an Köln übertragen wurden.
- **Klasse:** B/E.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch für die moderne Forschungsdarstellung, nicht für die ungeprüfte Primärquellenkette.

### HIST-09 – nicht vollständig verifizierte U2-Editionszitate
- **Beobachtung:** Websuche konnte mehrere exakte DO-UB-/Perlbach-Zitate (Knewer/Kneben/Stange) nicht unabhängig in einer authoritative Online-Edition auflösen.
- **Klasse:** F/E.
- **Schwere:** mittel.
- **Auswirkung:** kein Gegenbeweis; aber die verlangte 5–10er Zufallsprüfung kann nicht als vollständig bestanden gelten.
- **Konfidenz:** hoch.

### HIST-10 – etablierte Standards
- **Beobachtung:** Source Identity orientiert sich an fachlichen Zitier-/Archivprinzipien, verwendet aber überwiegend eigene Markdown-/ID-Strukturen. TEI ist nicht als allgemeines Muss sinnvoll; für editionsnahe Textkodierung wäre TEI P5 der etablierte Interchange-Standard. ISAD(G) bleibt ein etablierter Referenzstandard für archivische Beschreibung.
- **Klasse:** B/E/F.
- **Schwere:** niedrig-mittel.
- **Konfidenz:** hoch.
- **Bewertung:** Eigenbau ist nicht per se Fehler; problematisch würde er, wenn echte Editions-/Archivdaten exportiert oder ausgetauscht werden sollen und Standard-Mappings fehlen.

## 6.6 Softwaretechnische Qualität

### SW-01 – Zweckmäßigkeit
- **Beobachtung:** Validatoren adressieren reale Fehlerklassen: unbekannte Requirement-Referenzen, Zyklen, fehlende Verification Evidence, nicht autorisierte geänderte technische Pfade.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### SW-02 – Requirements Engineering
- **Beobachtung:** 39 Baseline + 14 Extensions werden angegeben; strukturierte Records und Coverage werden formal abgeglichen.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Grenze:** formale Konsistenz sagt nichts über Notwendigkeit/Vollständigkeit der Requirements aus; der Code kennzeichnet diese Grenze korrekt.

### SW-03 – Architekturangemessenheit
- **Beobachtung:** Architekturtexte betonen reversible, kleine Lösungen und kein Framework auf Vorrat. Gleichzeitig existiert für ein kleines Einzelprojekt ein großer Architecture-/Assurance-Apparat.
- **Klasse:** B/F.
- **Schwere:** mittel-hoch.
- **Konfidenz:** hoch.

### SW-04 – Codequalität
- **Beobachtung:** inspizierte Python-Dateien sind modular, typisiert/annotiert, mit klaren Fehlermeldungen und begrenzten Verantwortlichkeiten. Keine belastbare zyklomatische/duplikationsweite Messung möglich.
- **Klasse:** B.
- **Schwere:** niedrig.
- **Konfidenz:** mittel-hoch.

### SW-05 – Tests/Testorakel
- **Beobachtung:** Tests verwenden explizite positive und negative Fixtures; Orakel sind Regeldefinitionen, nicht der geprüfte Produktionscode. Das ist für formale Invarianten angemessen.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Grenze:** Tests validieren formale Regeln, nicht historische Richtigkeit.

### SW-06 – reale Fehlerfindung
- **Beobachtung:** #63 dokumentiert, dass ein Handoff-Versuch korrekt an REQ007 scheiterte, als fünf Requirements vorschnell auf `partial` gesetzt wurden.
- **Klasse:** O/B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### SW-07 – CI/Supply Chain
- **Beobachtung:** GitHub Actions verwendet `actions/checkout@v7` und `actions/setup-python@v7`, also Major-Version-Tags statt unveränderlicher Commit-SHAs.
- **Klasse:** B.
- **Schwere:** mittel.
- **Auswirkung:** schwächer als SLSA-orientierte Pinning-Praxis; Supply-Chain-Reproduzierbarkeit ist nicht maximal.
- **Konfidenz:** hoch.

### SW-08 – statische Analyse
- **Beobachtung:** im inspizierten Workflow sind Unit-Tests und Validatoren sichtbar, aber kein dedizierter Linter/Type-Checker.
- **Klasse:** B.
- **Schwere:** niedrig-mittel.
- **Konfidenz:** mittel, da andere Workflows nicht vollständig inventarisiert werden konnten.

### SW-09 – Build/Betrieb
- **Beobachtung:** Python 3.12 + Requirements-Datei werden in CI reproduzierbar eingerichtet. Ein vollwertiger Produktbetrieb existiert noch nicht; daher sind Recovery/Observability/DORA nur begrenzt anwendbar.
- **Klasse:** B/F.
- **Schwere:** Hinweis/nicht voll prüfbar.
- **Konfidenz:** hoch.

### SW-10 – Datenhoheit
- **Beobachtung:** offene Text-/JSON-/Markdown-Strukturen und providerunabhängige IDs sind ein starkes Langzeitmerkmal.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

## 6.7 Entwicklungsprozess

### DEV-01 – Review-Unabhängigkeit
- **Beobachtung:** PR-/CI-Prozess existiert; aber Projektartefakte sind laut Owner vollständig KI-generiert, und es gibt keinen Nachweis eines regelmäßig unabhängigen menschlichen Code-Reviews.
- **Klasse:** O/B/F.
- **Schwere:** hoch.
- **Auswirkung:** „Review“ kann dieselbe Fehlerfamilie reproduzieren.
- **Konfidenz:** hoch.

### DEV-02 – CI als Stop
- **Beobachtung:** dokumentierte fehlgeschlagene formale Handoff-Prüfung und erfolgreiche Korrektur.
- **Klasse:** B/O.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.

### DEV-03 – WIP/Parallelität
- **Beobachtung:** zahlreiche aktive Owner/Teilpakete bei einer Einzelperson.
- **Klasse:** B/F.
- **Schwere:** hoch.
- **Auswirkung:** Koordinations- und Kontextkosten.
- **Konfidenz:** hoch.

### DEV-04 – Stopp-Kriterien
- **Beobachtung:** viele Issues besitzen DoD/Stop Rules. Gleichzeitig entstehen wiederholt neue Folgefragen/Assurance-Schichten.
- **Klasse:** B/F.
- **Schwere:** mittel.
- **Konfidenz:** hoch.

## 6.8 KI-gestützte Entwicklung

### AI-DEV-01 – Herkunft
- **Beobachtung:** Owner bestätigt vollständige KI-Generierung.
- **Klasse:** O.
- **Schwere:** hoch als Review-Risiko, nicht als Qualitätsurteil.
- **Konfidenz:** hoch.

### AI-DEV-02 – menschliche Prüfbarkeit
- **Beobachtung:** Owner korrigiert reale Fehlrichtungen; dies zeigt aktive Steuerung. Es gibt aber keinen Nachweis, dass jede Code-/Methodenänderung vom fachfremden Owner inhaltlich verstanden werden kann.
- **Klasse:** O/F.
- **Schwere:** hoch.
- **Konfidenz:** hoch.

### AI-DEV-03 – Kontextverlust
- **Beobachtung:** Repository-Bootstrap, canonical state und Handoff sind explizite Gegenmaßnahmen.
- **Klasse:** B.
- **Schwere:** Hinweis positiv.
- **Konfidenz:** hoch.
- **Trade-off:** die Gegenmaßnahme selbst erzeugt erhebliche Struktur- und Pflegekosten.

### AI-DEV-04 – externe Empirie
- **E.** METR fand 2025 in einem RCT mit 16 erfahrenen Open-Source-Entwicklern und 246 Tasks auf vertrauten Repositories eine **19 % längere** Bearbeitungszeit mit damaligen AI-Tools; die Übertragbarkeit auf einen fachfremden Einzel-Owner und neuere Modelle ist begrenzt. Der Befund widerlegt jedenfalls die Annahme, KI-Nutzung sei automatisch ein Produktivitätsgewinn.

---

# 7. Ergebnisse der Prüfverfahren

## 7.1 Stichprobenprüfung historischer Aussagen

Geprüfte Stichprobe (opportunistisch statt echter Zufallsstichprobe, da keine maschinell vollständige Claim-Liste verfügbar war):

1. Knau 1374/1378 – **bestätigt als reale externe Diskrepanz**, Primärquelle weiter offen.
2. Lampert 1071 Saalfeld/Siegburg – **extern bestätigt**.
3. Richeza/Saalfeld/Coburg moderne Forschungsdarstellung – **extern bestätigt**, Primärquellenkette offen.
4. U2 Knewer 1289 – **nicht unabhängig online verifiziert**.
5. U2 Kneben 1294 – **nicht unabhängig online verifiziert**.
6. U2 Stange/Knewe 1315 – **nicht unabhängig online verifiziert**.
7. U2 Arnshaugk/Deutscher Orden 1285 – **nicht unabhängig online verifiziert**.

**Ergebnis:** 3/7 konnten in dieser Arbeitsumgebung extern gegengeprüft werden; 4/7 blieben wegen fehlender/ nicht auffindbarer authoritative Volltextinstanz unresolved. **Fehlerquote kann daraus nicht seriös berechnet werden.** „Nicht verifiziert“ ist kein Fehlernachweis.

**Eignung:** sehr hoch, sofern konkrete Editionsdigitalisate/Archivzugänge verfügbar sind. Für den Owner selbst praktikabel, wenn das System automatisch die Stichprobe und direkten Findspots bereitstellt.

## 7.2 Zitatprüfung

Die #103-Ledger-Einträge zu Deutscher Biographie, Lampert/Robinson und Hlawitschka sind bibliographisch plausibel und teilweise extern auffindbar. Mehrere U2-Urkundenbuchstellen benötigen direkte Editionsinspektion. Eignung hoch.

## 7.3 Literaturabgleich

Der aktuelle Review konnte regionale Standardwerke nicht vollständig gegen alle Claims abgleichen. Dobenecker und das Urkundenbuch der Vögte sind im Projekt als relevante Leitwerke erkannt, ihre systematische Vollständigkeitsprüfung ist aber offen. Eignung hoch; Durchführung unvollständig.

## 7.4 Gegenprüfung durch anderes KI-System

Nicht durchgeführt: In dieser Umgebung steht keine unabhängige zweite Modellinstanz mit garantierter methodischer Unabhängigkeit zur Verfügung. Selbst wenn verfügbar, wäre sie nur adversariale Fehlersuche, keine unabhängige Fachvalidierung.

## 7.5 Einfache Kennzahlen

- Anteil Primärquellenbelege: nicht belastbar repo-weit messbar.
- Forschungs- vs. Prozessarbeit: qualitativ klar prozesslastig, quantitativ nicht belastbar messbar.
- Zeit Frage→geprüftes Ergebnis: keine standardisierte Messreihe vorhanden.

## 7.6 Minimaler externer Fachreview

Höchste Aussagekraft hätte ein kleiner Reviewauftrag an eine Person mit **mittelalterlicher Landesgeschichte Mitteldeutschlands + Diplomatik/Quellenkunde**, idealerweise mit Kenntnis der Thüringer/Sächsischen Editions- und Archivlandschaft. Minimalauftrag: 10 zufällig ausgewählte consequential Findings aus #46/#103, jeweils Source Identity, Edition/Originalstatus, Fundstelle, Schlussstärke und Alternativerklärung prüfen.

Für U1 wäre zusätzlich historische Geographie/Umweltgeschichte nötig.

## 7.7 Minimaler technischer Review

Eine erfahrene Research Software Engineer/Softwareentwicklerin sollte nicht „das ganze System“ reviewen, sondern:
1. Setup aus clean checkout;
2. alle Tests/Validatoren;
3. 5 reale Trace-/State-Änderungen;
4. Dependency-/Supply-Chain-Pinning;
5. Datenexport/Restore;
6. Aufwand für eine kleine fachliche Änderung ohne KI.
Das würde Nutzbarkeit, Wartbarkeit und Prozesslast besser testen als ein reines Code-Style-Review.

---

# 8. Externe Maßstäbe und Vergleich

## 8.1 Transdisziplinarität

- Bergmann et al., *Quality Criteria of Transdisciplinary Research* (ISOE, 2005): formative Qualitätsprüfung; passt als Prozessmaßstab, aber Histo-Orla ist kein klassisches Multi-Stakeholder-Nachhaltigkeitsprojekt.
- Belcher et al. 2016: Relevanz, Glaubwürdigkeit, Legitimität, Wirksamkeit. Gut übertragbar als Meta-Raster; „Legitimität“ muss hier weniger politisch-partizipativ und stärker als transparente Authority-/Wissensrollen gelesen werden.
- Boix Mansilla/Duraisingh 2007: disciplinary grounding, advancement through integration, critical awareness. Sehr gut für die epistemische Integrationsqualität übertragbar, obwohl Ursprung Hochschullehre ist.

## 8.2 Historische/DH-Standards

- TEI P5 ist etablierter Standard für Text Encoding/Interchange; sinnvoll, wenn Histo-Orla editionsnahe strukturierte Texte austauschen muss, nicht automatisch für jeden Research-State-Datensatz.
- ISAD(G) ist etablierter archivischer Beschreibungsstandard; Histo-Orlas Source Ledger sollte bei Archivgut kompatibel/mappbar bleiben, ohne ISAD(G) vollständig intern nachzubauen.
- Fachliche Editions-/Diplomatikstandards sind stärker quellentypabhängig als ein universelles Schema.

## 8.3 Software Engineering

- ISO/IEC 25010:2023 definiert ein Produktqualitätsmodell mit neun Qualitätsmerkmalen. Als Checkliste brauchbar, aber vollständige Enterprise-Metrisierung wäre für dieses Einzelprojekt unverhältnismäßig.
- ISO/IEC/IEEE 29148:2018 ist aktueller Requirements-Engineering-Referenzstandard; Histo-Orlas Traceability/Verifiability passt gut, die Menge formaler Metaattribute sollte aber am tatsächlichen Änderungsrisiko gemessen werden.
- ATAM ist für Trade-offs zwischen Qualitätsattributen gedacht. Vollständige ATAM-Zeremonie wäre überdimensioniert; konkrete Quality-Attribute-Szenarien sind übertragbar.
- OWASP Top 10:2025 ist nur relevant, sobald Web-/App-Angriffsflächen existieren.
- SLSA-Prinzipien sind für Supply Chain relevant; Major-Tag-Actions sind schwächer als immutable Pinning.
- DORA-Metriken sind für laufende Delivery-Systeme nützlich; bei einem privaten Forschungsrepo ohne Produktionsdienst sind sie nur eingeschränkt sinnvoll.

## 8.4 Vergleich mit Digital Humanities

DH-Sustainability-Literatur warnt vor der langfristigen Last individueller Tools und Infrastrukturen. King’s Digital Lab musste rund 100 ältere DH-Projekte wegen technischer und finanzieller Nachhaltigkeitsprobleme systematisch sanieren. Für Histo-Orla spricht dies **für offene Daten und kleine technische Kerne**, aber **gegen unnötige eigene Infrastruktur**.

## 8.5 KI-gestützte Entwicklung

Empirische Ergebnisse sind gemischt und stark kontextabhängig. METR 2025 zeigt für erfahrene Entwickler auf vertrauten Repositories sogar Verlangsamung. Für Histo-Orla ist die Übertragbarkeit begrenzt, weil der Owner fachfremd ist und KI zugleich Entwickler, Analyst und Forschungsassistent ist. Gerade deshalb ist unabhängige Validierung wichtiger, nicht weniger.

---

# 9. Hypothesen und Gegenhypothesen

## H1 – Das eigentliche Produkt ist delegierbare wissenschaftliche Arbeit, nicht ein bestimmtes Software-System
- **Belege:** wiederkehrende Owner-Korrekturen; Quellen-/Fundstellenbedarf; Ablehnung technikzentrierter Oberfläche.
- **Gegenhypothese:** Der Owner will langfristig sehr wohl eine eigenständige Anwendung.
- **Falsifikation:** reale Nutzung zeigt, dass vorhandene Standardtools + Chat/Repo die Bedürfnisse vollständig erfüllen.
- **Konfidenz:** hoch.

## H2 – Governance-Wachstum ist teilweise eine Kompensationsreaktion auf KI-bedingte Kontext-/Authority-Fehler
- **Belege:** Handoff-, Work-Context-, Assurance- und Feedback-Mechanismen folgen beobachteten Fehlrichtungen.
- **Gegenhypothese:** dieselben Mechanismen wären in jedem hochwertigen Forschungssoftwareprojekt nötig.
- **Falsifikation:** vergleichbares nicht-KI-Einzelprojekt benötigt denselben Regelumfang bei gleicher Größe.
- **Konfidenz:** mittel-hoch.

## H3 – Das Projekt hat einen „Assurance Ratchet“
- **Definition:** Fehler führen eher zu zusätzlicher Sicherungsschicht als zur Entfernung/Vereinfachung vorhandener Struktur.
- **Belege:** Requirements Harness → Assurance Spine → Work Context → Execution Contract; mehrere Korrekturen erzeugen neue formale Artefakte.
- **Gegenhypothese:** spätere Reconciliation konsolidiert tatsächlich und entfernt Doppelungen.
- **Falsifikation:** über mehrere Iterationen sinken Artefakt-/Regelzahl und Pflegeaufwand bei gleicher oder besserer Fehlererkennung.
- **Konfidenz:** mittel.

## H4 – Live Research ist die verlässlichste Quelle für echte Requirements
- **Belege:** wichtige Korrekturen entstehen aus Lampe-/Sachenbacher-/WP1-/Ranis-/Saalfeld-Nutzung.
- **Gegenhypothese:** Live Cases können overfitten und seltene Spezialprobleme übergewichten.
- **Falsifikation:** mehrere unabhängige Fälle zeigen, dass die aus einem Live Case abgeleiteten Needs nicht generalisieren.
- **Konfidenz:** hoch.

## H5 – Die historische Forschungsqualität ist methodisch vorsichtig, aber noch nicht extern hinreichend validiert
- **Belege:** gute Source-/Inference-Grenzen; offene direkte Kollationen; keine unabhängige Fachreview.
- **Gegenhypothese:** die Editionen und Sekundärliteratur sind so klar, dass externe Prüfung wenig ändern würde.
- **Falsifikation:** qualifizierte Stichprobe findet keine materiellen Fehler und bestätigt Schlussstärken.
- **Konfidenz:** hoch.

## Unerklärte Beobachtungen

1. Warum ist der Governance-/Assurance-Apparat trotz expliziter Lean-Regel so stark gewachsen?
2. Welche Mechanismen führen tatsächlich zu weniger Owner-Aufwand statt nur zu besserer Auditierbarkeit?
3. Wie viele der 53 akzeptierten Requirements wurden aus realer wiederholter Forschungsfriktion versus einmaliger KI-/Designanalyse abgeleitet?
4. Welche historischen Findings sind nach externer Fachprüfung stabil?
5. Wie hoch ist die tatsächliche Wartungszeit pro Forschungsstunde?

---

# 10. Anerkennung – was trägt und erhaltenswert ist

1. **Epistemische Trennung** von Quelle, Instanz, Derivat, Fundstelle, Exzerpt, Finding und Interpretation.
2. **Unresolved als legitimer Zustand**, sichtbar am 1374/1378-Fall.
3. **Bounded negative findings** statt „nicht gefunden = existiert nicht“.
4. **Owner-Korrekturen mit realer Wirkung**; das Projekt kann Fehlrichtungen zurücknehmen.
5. **Formale Validatoren mit klarer Authority-Grenze** statt „CI = wissenschaftliche Wahrheit“.
6. **Offene, langfristig lesbare Formate** und Provider-Unabhängigkeit.
7. **Reale negative Tests** und mindestens ein dokumentierter echter Guard-Fund.
8. **Trennung von Product-/Workflow-Feedback und historischer Evidenz**.
9. **Prior-Art-Challenge statt nominell blindem Copying** als erklärte Regel.
10. **Live Research als Falsifikation des Systemdesigns** – konzeptionell der stärkste Entwicklungsmechanismus des Projekts.

---

# FIXIERUNG DER UNABHÄNGIGEN ANALYSE

Die Abschnitte 1–10 sind hiermit als **Phase-1–6-Fassung fixiert**. Spätere Lektüre projektinterner Audits darf diese Abschnitte nicht rückwirkend ändern. Abweichungen und Übereinstimmungen werden ausschließlich in Abschnitt 11 ergänzt.

Externe Quellen für diese Fassung:
- ISOE: Bergmann et al. (2005), Quality Criteria of Transdisciplinary Research: https://www.isoe.de/en/publication/quality-criteria-of-transdisciplinary-research-a-guide-for-the-formative-evaluation-of-research-projects
- Belcher et al. (2016), Research Evaluation 25(1): https://academic.oup.com/rev/article/25/1/1/2362728
- Boix Mansilla & Duraisingh (2007): https://eric.ed.gov/?id=EJ754100
- ISO/IEC 25010:2023: https://www.iso.org/standard/78176.html
- ISO/IEC/IEEE 29148:2018: https://committee.iso.org/standard/72089.html
- CMU/SEI ATAM: https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/
- DORA metrics: https://dora.dev/guides/dora-metrics/
- OWASP Top 10:2025: https://top10.owasp.org/2025/
- TEI P5 Guidelines: https://www.tei-c.org/release/doc/tei-p5-doc/en/html/index.html
- ICA ISAD(G): https://www.ica.org/en/isadg-general-international-standard-archival-description-second-edition
- METR 2025 RCT: https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf
- Digital Humanities Quarterly sustainability review: https://www.digitalhumanities.org/dhq/vol/14/3/000484/000484.html


---

# 11. Abgleich mit projektinternen Audits – Phase 7

**Regel:** Dieser Abschnitt wurde erst nach der Fixierung der Abschnitte 1–10 erstellt. Er ändert die unabhängige Analyse nicht.

## 11.1 Übereinstimmungen

### A. Meta-/Governance-Komplexität

#64 beschreibt das Risiko, dass das Meta-System den Value Stream überholt, zu viele Work Owner operative Handoffs erzeugen und Assurance-Erfolg mit Produkt-Erfolg verwechselt wird. Das stimmt eng mit den unabhängig formulierten Befunden 2, 4, SW-03, DEV-03 und Hypothese H3 überein.

**Abgleich:** starke Konvergenz.

### B. Korrekturkaskade / Fehler→Regel-Schleife

#70 formuliert explizit die Gefahr `KI macht Fehler → neue Regel → mehr Governance → mehr Kontext/Handoffs → neue Orientierungsfehler`. Die unabhängige Analyse beschreibt denselben Mechanismus vorsichtiger als „Assurance Ratchet“ und Korrekturkaskade.

**Abgleich:** starke Konvergenz, aber #70 ist kausal expliziter. Die unabhängige Fassung hält die Kausalität nur bei mittlerer Konfidenz, weil nicht jede neue Regel nachweislich denselben Mechanismus hat.

### C. reale Forschung als Delivery-/Falsifikationseinheit

#64 empfiehlt vollständige Vertical Research Slices. Die unabhängige Analyse kommt ohne Nutzung dieses Audits zu H4: Live Research ist die verlässlichste Quelle für echte Requirements.

**Abgleich:** starke Konvergenz.

### D. formale Qualität ≠ wissenschaftlicher/Owner-Nutzen

#64 trennt technische Verification von Research/Product Acceptance. #70 trennt lokale formale Ziele von globalem Owner-Nutzen. Die unabhängige Analyse beobachtet dasselbe an WP1 und den Validatorgrenzen.

**Abgleich:** sehr starke Konvergenz.

### E. Prior-Art-/AI-Muster

#70 analysiert AI-spezifische Mechanismen, lokale Objective Functions, Persistenzträgheit und die niedrigeren Produktionskosten kohärenter Strukturen gegenüber realer Falsifikation. Die unabhängige Analyse findet ebenfalls Prior-Art-Attraktion, KI-Kontextkompensation und hohe Strukturproduktionsdichte.

**Abgleich:** mittlere bis starke Konvergenz. Die interne Analyse ist hier detaillierter; die unabhängige Analyse kann die AI-spezifische Kausalität nicht direkt messen.

## 11.2 Abweichungen

### A. Historische Fachqualität

Die internen Audits #64/#70 konzentrieren sich primär auf Product/Governance/AI-Resilience. Die unabhängige Analyse legt deutlich mehr Gewicht auf die **fachhistorische Stichprobe**, die teilweise gute Quellenkritik bestätigt, aber bei 4/7 geprüften U2-Aussagen keine unabhängige Online-Verifikation der Editionsstellen erreichen konnte.

**Nur in dieser Analyse stärker:** konkrete Trennung zwischen methodischer Vorsicht und noch fehlender externer fachwissenschaftlicher Validierung.

### B. Software-Supply-Chain und statische Analyse

Die unabhängige Analyse markiert Major-Tag-Actions statt immutable SHA-Pinning sowie fehlende sichtbare Linter/Type-Checker im inspizierten Workflow. Diese Punkte sind in den gelesenen internen Audits nicht zentral.

### C. Transdisziplinäre Ergebnisqualität

Die unabhängige Analyse trennt Prozessqualität von Ergebnisqualität anhand ISOE/Belcher/Boix Mansilla und bewertet die Integration derzeit eher als gut strukturierte Mehrperspektivität als als bereits extern validierte transdisziplinäre Erkenntnis. Die internen Audits behandeln stärker Projekt-/Systemintegration.

### D. Blindheitsproblem

#121 selbst definiert bereits ein Blind-Replication-Verfahren, scheint nach dem zugänglichen Issue-Stand aber seine angekündigten Artefakte an den dort genannten Pfaden nicht bereitgestellt zu haben. #138 definiert nahezu denselben aktuellen Auftrag wie #142; #142 wurde deshalb als Duplicate geschlossen.

## 11.3 Was die internen Audits zusätzlich sichtbar machen

1. #64 differenziert später zwischen schützender Loss-Boundary-Formalization und potenziell problematischer Problem-Partition-Formalization. Diese feinere Typisierung ist nützlich und verhindert die zu grobe Formel „weniger Formalisierung = besser“.
2. #70 macht deutlich, dass **dokumentiertes Wissen kein Control Mechanism** ist: Ein Anti-Pattern kann bekannt sein und an einer konkreten Admission-Grenze trotzdem erneut auftreten.
3. #70 beschreibt lokale Objective Functions als möglichen Mechanismus: lokale Vollständigkeit/Traceability ist leichter prüfbar als globale Owner-Entlastung.
4. Interne Audits dokumentieren Recovery-Fälle und Near Misses ausführlicher als die unabhängige Fassung.

## 11.4 Wie Abweichungen erklärbar sind

- Die internen Audits hatten Zugang zu einer dichteren Projektgenealogie und fokussierten AI-/Governance-Mechanismen.
- Die unabhängige Analyse wurde absichtlich breiter über historische Fachqualität, transdisziplinäre Standards und Software Engineering angelegt.
- Gleiche KI-/Sprachfamilien können zu ähnlichen Taxonomien und Diagnosen führen; Konvergenz ist daher **kein unabhängiger Wahrheitsbeweis**.
- Die starke Übereinstimmung erhöht die Plausibilität der beobachteten Muster, ersetzt aber weder quantitative Prozessmessung noch externe Fachreview.

---

# 12. Empfehlungen – getrennt vom Befund

Jede Empfehlung ist als Handlungsvorschlag, nicht als neue Requirement-/Governance-Truth zu lesen.

## R1 – Für eine begrenzte Zeit keine neue Governance-Schicht ohne empirischen Failure Case

**Basis:** Befund 2, H3, DEV-03; Konvergenz mit #64/#70.

Neue Regeln/Owner/Validatoren nur dann, wenn ein konkreter wiederholbarer Fehler nicht bereits durch vorhandene Mechanismen abgedeckt ist. Bevor eine neue Regel entsteht, zuerst prüfen: bestehende Regel vereinfachen, ableiten, automatisieren oder entfernen.

## R2 – Fortschritt primär an 3–5 vollständigen historischen Research Slices messen

**Basis:** H4, HIST-Befunde, Owner-Feedback WP1.

Für jeden Slice messen:
- Startfrage in Owner-Sprache;
- Zeit bis zu prüfbarem Ergebnis;
- Zahl manueller Handoffs/Meta-Schritte;
- Anteil der Claims mit direkt prüfbarer Fundstelle;
- Zahl notwendiger Owner-Korrekturen;
- offene Unsicherheit;
- tatsächlicher Forschungsnutzen.

Damit wird „funktioniert das System?“ nicht durch Repo-/CI-Reife ersetzt.

## R3 – Externe Fachprüfung jetzt klein, aber real durchführen

**Basis:** HIST-09, TD-03, AI-DEV-02.

Nicht das ganze Projekt reviewen lassen. 10 zufällig gezogene consequential Findings aus #46/#103 an eine qualifizierte Person für mittelalterliche Landesgeschichte/Diplomatik/Quellenkunde geben. Fehlerklassen dokumentieren. Das hat derzeit höheren Erkenntniswert als weitere interne Methodenaudits.

## R4 – Research-facing Oberfläche vor weiterer Assurance-Ausweitung validieren

**Basis:** reales Owner-Feedback 2026-09-23; Zentralbefund 4.

Den excerpt-zentrierten Workflow mit realen Quellen testen: Exzerpt/Text/Bild zuerst, Provenienz und epistemischer Status drill-down-fähig, technische Traceability im Hintergrund. Erst wenn dies im Alltag trägt, breitere UI-/Workflow-Infrastruktur erwägen.

## R5 – Semantische Ownership von operativer Work-Topologie entkoppeln

**Basis:** DEV-03, #64-Abgleich.

Viele fachliche Authorities dürfen existieren, ohne dass jede einen separaten manuellen Handoff erzeugt. Wo State deterministisch ableitbar ist, automatisch zusammenführen. Owner nur für echte Bedeutung/Priorität/Fachurteil/Acceptance beanspruchen.

## R6 – Requirements-Bestand empirisch challengen

**Basis:** 53 accepted Requirements, H4, offene Frage 3.

Nicht pauschal reduzieren. Stattdessen jeden Requirement-Cluster gegen reale Research Slices markieren:
- wiederholt gebraucht;
- einmalig gebraucht;
- noch nie in realer Forschung ausgelöst;
- rein schützende Invariante;
- potenziell durch Standardtool/Format ersetzbar.

Das ist eine Evidenzprüfung, keine automatische De-Scope-Aktion.

## R7 – kleine technische Hygiene-Deltas

**Basis:** SW-07/SW-08.

Proportional prüfen:
- GitHub Actions auf immutable Commit-SHAs pinnen;
- einen leichten Linter/Type-Check ergänzen, sofern er ohne nennenswerte Pflegekosten läuft;
- Dependency-/License-/Vulnerability-Check für tatsächlich verwendete Python-Abhängigkeiten;
- Backup/Restore/Export-Test erst dort, wo persistenter Runtime-State existiert.

## R8 – Audit-Sättigung definieren

**Basis:** #64/#70/#121/#138 plus diese Analyse.

Weitere ganzheitliche Meta-Audits sollten erst stattfinden, wenn neue **empirische** Evidenz vorliegt: externe Fachreview, mehrere neue Research Slices, messbarer Owner-Aufwand oder ein materieller Failure. Sonst droht Audit über Audit ohne neue diskriminierende Information.

---

# 13. Reflexion der eigenen Analyse

## 13.1 Befangenheit

Dieser Review wurde von einem KI-System durchgeführt, das strukturell ähnliche Fähigkeiten und Sprachmuster besitzt wie die Systeme, die das Repository erzeugt haben. Risiken:

- gleiche Präferenz für Taxonomien, Trennungen und Governance;
- gleiche Tendenz, Kohärenz als Qualität zu überschätzen;
- gleiche Blindstellen bei fachhistorischen Details;
- gleiche Neigung, komplexe Probleme in strukturierte Frameworks zu überführen.

Gegenmaßnahmen waren: Primärspuren vor Synthesen, externe Standards, konkrete Source-/Code-Stichproben, Gegenhypothesen und die Audit-Quarantäne.

## 13.2 Verfahrensgrenze

Die Blindheit war **nicht perfekt**: Ein #9-Kommentar-Abruf lieferte vor Fixierung unbeabsichtigt einen internen Audit-Kommentar. Dessen Diagnosen wurden nicht als Evidenz der Abschnitte 1–10 verwendet. Trotzdem ist ein vollständig blindes Experiment damit nicht mehr behauptbar.

## 13.3 Messgrenzen

- keine vollständige Repository-Tree-/LOC-Auswertung;
- keine echte Zufallsstichprobe aller historischen Claims;
- keine lokale Ausführung der Tests in dieser Chat-Umgebung;
- keine vollständige PR-/CI-Statistik;
- keine unabhängige Spezialistenprüfung;
- keine sichere Trennung menschlich formulierter von KI-formulierter GitHub-Prosa.

## 13.4 Schlussgrenze

Die belastbarste Aussage ist nicht „Histo-Orla ist gut/schlecht“, sondern:

> Histo-Orla besitzt ungewöhnlich starke explizite epistemische und formale Schutzmechanismen und zeigt reale Lernfähigkeit. Gleichzeitig ist empirisch sichtbar, dass diese Schutzmechanismen und ihre Koordination selbst zu einem erheblichen Teil der Arbeit geworden sind, während unabhängige fachhistorische Validierung und research-facing End-to-End-Nutzen noch weniger stark belegt sind. Die nächste Qualitätssteigerung ist daher vor allem durch reale Forschungsnutzung und externe Stichprobenprüfung zu erwarten, nicht durch eine weitere Verfeinerung der Selbstbeschreibung.

---

# Handoff-Check

1. **Materiell geändert:** unabhängige Gesamtanalyse erstellt; Phase-7-Abgleich und getrennte Empfehlungen ergänzt.
2. **Kanonischer Ort:** dieses Artefakt; Work Owner #138.
3. **Work-Owner-Status:** muss nach Integration auf `review-complete`/äquivalent aktualisiert werden.
4. **Evidenz/Begründung/Trade-offs:** in Abschnitten 1–13.
5. **Offene Punkte:** externe Fachreview, quantitative Repository-/Workflow-Metrik, vollständige Claim-Stichprobe.
6. **#44-Blocker:** kein neuer echter Owner-Blocker festgestellt.
7. **PROJECT_STATE.md:** dieser Review ändert keine Phase, Selection, Requirement, Method oder Architecture; eine Current-State-Änderung ist daher nicht automatisch erforderlich. Ein Pointer kann bei Integration sinnvoll sein, falls #138 als handoff-relevanter Review geführt wird.
8. **Restartability:** #138 + dieses Artefakt reichen für Fortsetzung ohne Chat; #142 ist als Duplicate geschlossen.
