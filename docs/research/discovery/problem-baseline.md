# Histo-Orla – Problem-/Need-/Pain-/Risk-Baseline v0.1

**Work Owner:** #28  
**Status:** `working-research / discovery-baseline-v0.1`  
**Scope:** Konsolidierung des kanonischen Projektstands als Grundlage für #29–#43.  
**Methodik:** Aussagen aus README, Research-Design und kanonischen Issues werden atomisiert und nach Problem, Need, Goal, Pain, Challenge, Open Question, Risk, Constraint und Hypothesis getrennt. Lösungshypothesen werden nicht als Needs/Requirements behandelt.

## 1. Leseregel

Diese Datei ist das kanonische Research-Artefakt für #28. Das Issue #28 bleibt Work Owner und hält Status, Kurzsynthese, offene Punkte und nächste Aktion.

Reifegrade:

- `validated` – durch aktuellen Projektstand als belastbarer Bedarf/Ziel/Constraint getragen
- `working` – hinreichend belegt für weitere Analyse, aber durch Workflow/SOTA noch zu schärfen
- `research-needed` – Forschungsfrage muss #30/#31–#39 informieren
- `hypothesis` – mögliche Lösung/Erklärung, nicht Requirement

Use Cases:

- **U1** historische Teich-/Niederungs-/Landnutzungsstrukturen vor 1800
- **U2** Vogtei / Ministerialität / Herrschaft / mittelalterliche Beziehungen
- **U3** frühneuzeitlicher adliger Akteur / Handlungslogik
- **U4** persönliches Quellenarchiv / OCR / Retrieval / Fundstellen

---

# 2. Goals

| ID | Goal | Provenienz | Use Cases | Reife | Nächste discriminating action |
|---|---|---|---|---|---|
| G-001 | Ein funktionierendes, dauerhaft nutzbares System für transdisziplinäre historische Forschung entsteht; kein bloßes Konzeptpapier oder KI-Demonstrator. | #1, #10, Research-Design | U1–U4 | validated | Gegen reale Workflows #29 und spätere Acceptance-Fälle prüfen. |
| G-002 | Der Research Owner kann unscharf fragen; das System übersetzt die Beobachtung in fachwissenschaftlich saubere Problembegriffe, Methoden und Quellenlogiken. | #1, #16, #19, #20 | U1–U3 | validated | #32 SOTA zur Problemübersetzung; in #29 konkrete Friktionen erfassen. |
| G-003 | Jede aktivierte Fachdomäne arbeitet nach ihren eigenen Standards, Terminologien, Methoden, Evidenzregeln und Geltungsgrenzen. | #9, #15, #16, #19 | U1–U4 | validated | #33 Expertise Routing; Quality Criteria in #41. |
| G-004 | Quellen-, Literatur- und Archivarbeit bleibt bis zur konkreten Quelle/Fundstelle rückführbar. | #2, #4, #5, #6, #9 | U1–U4 | validated | #31 und #35 operationalisieren Mindestanforderungen. |
| G-005 | Regionale Tiefenschärfe wird mit territorialen, reichsweiten und europäischen Verflechtungen verbunden, wenn der historische Zusammenhang dies erfordert. | #13, #14, #16 | U1–U3 | validated | #36 Scale-Shift-/Raumkontext-SOTA. |
| G-006 | Befund, digitale Derivate, Claim, Interpretation, Synthese, Unsicherheit und Kontroverse bleiben unterscheidbar. | #9, #12, #15, #20, #21 | U1–U4 | validated | #31/#34 gegen externen SOTA prüfen; später Requirements. |
| G-007 | Wiederkehrende mechanische Arbeit wird dort automatisiert, wo sie reale Friktion oder Qualitätsgewinn adressiert. | #8, #24 | U1–U4 | validated | #29 identifiziert reale Wiederholungen; #39 allokiert Capability. |
| G-008 | Kanonischer Forschungszustand ist restartbar, providerunabhängig und ohne Chat rekonstruierbar. | #6, #8, #9, #12, docs/research/README.md | U1–U4 | validated | #39/#41 konkretisieren Portabilität/Restartability. |
| G-009 | Wissenschaftliche Komplexität ist für den Research Owner verständlich und für Fachpersonen auditierbar, ohne Fachlichkeit zu reduzieren. | #9, #12, #20 | U1–U4 | validated | #38 Research UX/Auditability. |
| G-010 | Forschung und Vermittlung bleiben getrennte Verantwortungsbereiche; Vermittlungslogik darf den Research State nicht zurückschreiben. | #20, #21 | U1–U4 | validated | #38 prüft View-Logik; spätere Übergabeschnittstelle nach Requirements. |
| G-011 | Development realisiert validierte Requirements als funktionierendes System; Technik definiert die wissenschaftlichen Needs nicht. | #1, #10, #24 | U1–U4 | validated | In #42 Architecture-driving Requirements und Freiheitsgrade explizit machen. |
| G-012 | Lean minimiert unnötige Systemkomplexität, nicht wissenschaftliche Tiefe. | #1, #10, #12, #24 | U1–U4 | validated | Technical Admission Test in #39/#43 anwenden. |

---

# 3. Needs

| ID | Need | Warum relevant | Provenienz | Use Cases | Führende Domänen | Reife | Nächste discriminating action |
|---|---|---|---|---|---|---|---|
| N-001 | Aus unscharfen Beobachtungen relevante Fachbegriffe, konkurrierende Modelle und Forschungsfragen erschließen. | Unbekanntes Vokabular erzeugt sonst Such- und Interpretationsblindstellen. | #16, #19 | U1–U3 | historische Philologie, Begriffsgeschichte, jeweilige Fachdomänen, Knowledge Organization | validated | #32; Workflow-Signale #29. |
| N-002 | Fachkompetenzen problemabhängig routen und deren epistemische Geltungsgrenzen sichtbar halten. | Nutzer kann die nötigen Disziplinen nicht vollständig selbst bestimmen. | #13, #15, #16, #19 | U1–U4 | Research Design + jeweilige Fachdomänen | validated | #33. |
| N-003 | Regionalisierte Spitzenexpertise mit Kenntnis regionaler Quellenlandschaften, Terminologie und Forschungstraditionen aktivieren. | Generische Fachkenntnis reicht für Ostthüringen/Vogtland/Sachsen/Franken/Egerland/Lausitz nicht. | #14, #16 | U1–U3 | Landesgeschichte, Archivkunde, historische Geographie etc. | validated | #33/#36; regionale Layer in allen SOTA-Paketen. |
| N-004 | Archive, Bestände und Serien aus historischem Verwaltungs-/Provenienzkontext ableiten, nicht nur über moderne Sachschlagwörter. | Relevante Quellen können sonst systematisch unauffindbar bleiben. | #2, #19 | U1–U3 | Archivistik, Registraturkunde, Diplomatik | validated | #31. |
| N-005 | Quelle, Überlieferungsstufe, Edition, Regest, Digitalisat und konkret inspizierte Instanz unterscheiden. | Verhindert Source Laundering und falsche Belegqualität. | #4, #6, #9, #12, #21 | U1–U4 | Archivistik, Diplomatik, Editionswissenschaft, RDM | validated | #31/#34. |
| N-006 | Exakte Seiten-/Blatt-/Regest-Fundstellen erhalten und aus Such-/Analyseergebnissen zurückführen. | Ohne Fundstelle ist eine generierte Antwort kein belastbarer Quellenbefund. | #2, #4, #5 | U1–U4 | Quellenkunde, Editionswissenschaft, IR, RDM | validated | #31/#35. |
| N-007 | Bildbasierte Drucke, Scans und perspektivisch Handschriften erschließen, ohne OCR/HTR mit Originalbefund zu verwechseln. | Große Teile relevanter Quellen sind nicht zuverlässig textdurchsuchbar. | #4 | U1–U4 | OCR/HTR, DH, Paläographie, Editionswissenschaft | validated | #35. |
| N-008 | Exakte Suche plus historische Schreib-/Namensvarianten, kontrollierte Expansion und reproduzierbare Suchheuristik. | Moderne exakte Suchformen übersehen historische Lexik/Orthographie; bloß semantische Suche ist nicht ausreichend. | #5 | U1–U4 | IR, historische Sprachverarbeitung, Onomastik | validated | #35. |
| N-009 | Abhängige Quellen/Überlieferungen von unabhängiger Evidenz unterscheiden. | Verhindert falsche Mehrfachbestätigung. | #12, #21 | U1–U4 | Quellenkritik, Diplomatik, Textkritik, Historiographie | working | #34. |
| N-010 | Differenzen zwischen Quellen zunächst diagnostizieren statt vorschnell harmonisieren oder als Fehler behandeln. | Zeitstand, Zweck, Maßstab oder institutionelle Perspektive können Unterschiede erklären. | #15, #21 | U1–U4 | Quellenkritik + jeweilige Domäne | working | #34. |
| N-011 | Historische Akteurs-/Handlungssituationen evidenzbasiert rekonstruieren: Position, Ressourcen, Informationshorizont, Optionen, Zwänge, beobachtete Handlung, alternative Erklärungen. | Verhindert psychologisierende oder nachträglich elegante Motivgeschichten. | #14, #15, #21 | U2–U3 | Mikrogeschichte, historische Anthropologie, Prosopographie, Politik-/Adels-/Hofgeschichte | working | #37. |
| N-012 | Maßstab kontrolliert wechseln und historische Orts-/Territorialkontexte zeitabhängig behandeln. | Region/Territorium darf kein statischer Analysecontainer sein. | #14 | U1–U3 | Landesgeschichte, historische Geographie, Spatial History | validated | #36. |
| N-013 | Mehrere Fachperspektiven getrennt prüfen und erst danach transparent integrieren. | Unterschiedliche Evidenzlogiken dürfen nicht durch generische Synthese geglättet werden. | #13, #15, #19 | U1–U4 | Research Coordination + Fachdomänen | validated | #33/#41. |
| N-014 | Kontroversen, Evidenzlücken, Nichtwissen und konkurrierende Erklärungen als legitime Research States führen. | Wissenschaftliche Unsicherheit darf nicht in Scheinsicherheit transformiert werden. | #9, #12, #15 | U1–U4 | Research Integrity + Fachdomänen | validated | #34/#38/#41. |
| N-015 | Substantielle Research-Ergebnisse versioniert und ohne Doppelwahrheit persistieren. | Neustartbarkeit und Wissensgovernance. | #6, #9, #23, docs/research/README.md | U1–U4 | RDM, Governance | validated | laufend gemäß §14. |
| N-016 | Rechte, Lizenz-, Datenschutz- und externe-Service-Grenzen vor technischer Umsetzung kennen. | Quellen können nicht beliebig gespeichert/hochgeladen/veröffentlicht werden. | #4, #6, #22, #24 | U1–U4 | Legal/Rights/Data Governance | working | #40; konkrete Toolentscheidungen später. |
| N-017 | Capability-Verantwortung zwischen Research Owner, Fachspezialist, deterministischer Software, spezialisierten Verfahren und LLM begründet verteilen. | KI soll weder Default noch Autorität für robuste Kernaufgaben sein. | #24 | U1–U4 | RSE, AI Evaluation, Research Integrity + Fachdomänen | validated need | #39. |
| N-018 | Reale Qualitäts-/Acceptance-Kriterien je Capability aus Fachmethodik ableiten. | Sonst bleibt „funktioniert gut“ nicht prüfbar. | #9, #22, #45 | U1–U4 | Quality Engineering + Fachdomänen | validated | #31–#39 liefern domänenspezifische Checks; #41 synthetisiert. |
| N-019 | Konsequenzabhängige menschliche/externe Fachvalidierung auslösen können. | Methodenkonforme KI ist keine unabhängige Fachprüfung. | #9, #12, #15, #45 | U1–U4 | Fachdomäne, Research Integrity | validated | #33/#40/#42. |
| N-020 | Vor Eigenentwicklung vorhandene Werkzeuge, Standards und Forschungsinfrastrukturen gegen den realen Need prüfen. | Verhindert unnötige technische Komplexität. | #1, #10, #24 | U1–U4 | SOTA, RSE, jeweilige Fachdomäne | validated | #31–#39. |

---

# 4. Pains – konkrete Friktionen des Forschungsalltags

| ID | Pain | Ursache / heutige Friktion | Provenienz | Use Cases | Reife | Nächste discriminating action |
|---|---|---|---|---|---|---|
| P-001 | Der Nutzer kennt den einschlägigen Fachbegriff häufig noch nicht. | Recherche beginnt mit alltagssprachlicher Beobachtung; Fachliteratur/Archive verwenden andere Begriffe. | #16, #19 | U1–U3 | validated | #29 konkretisieren; #32. |
| P-002 | Relevante Quellen sind über viele Archive, Bestände, Editionen, Portale und lokale Dateien verteilt. | Zuständigkeiten folgen historischer Verwaltung, Provenienz und Überlieferung, nicht Nutzerlogik. | #2, #19 | U1–U4 | validated | #29/#31. |
| P-003 | Bild-PDFs, Scans und ältere Drucke sind nicht zuverlässig durchsuchbar. | Fehlende/fehlerhafte Textlayer, Fraktur, Layout, historische Orthographie. | #4 | U1–U4 | validated | #35. |
| P-004 | Suchtreffer verlieren leicht Seite/Blatt/Regest und damit Belegfähigkeit. | OCR/Exports/Semantic Search können Fundstellenbezug zerstören. | #4, #5 | U1–U4 | validated | #35. |
| P-005 | Historische Schreibweisen, Synonyme und regionale/institutionelle Begriffe erzeugen Retrieval-Blindspots. | Exakte moderne Query deckt historischen Wortschatz nicht ab. | #5, #16, #19 | U1–U4 | validated | #32/#35. |
| P-006 | Moderne Archivsuche über Sachbegriffe reicht für ältere Quellen häufig nicht. | Bestände folgen Registraturbildnern, alten Institutionen und Findbuchsprache. | #2, #19 | U1–U3 | working | #31, in U1 konkret testen. |
| P-007 | Nutzer müsste ansonsten selbst wissen, welche Disziplin zuständig ist und wie diese arbeitet. | Hohe fachliche Einstiegshürde und Gefahr falscher Methodenwahl. | #13, #19 | U1–U4 | validated | #29/#33. |
| P-008 | Generische KI-Antworten können flüssig klingen, ohne fachlich/evidenziell belastbar zu sein. | False authority, fehlende Quellen-/Methodenpfade. | #9, #15, #24 | U1–U4 | validated | #33/#38/#39. |
| P-009 | Wiederkehrende mechanische Quellen-/Datei-/Sucharbeit bindet Zeit, die nicht fachliches Urteil erfordert. | Manuelle Repetition, Medienbrüche, fehlende Workflowintegration. | #2, #8, #24 | U1–U4 | working | #29 beobachtungsnah spezifizieren. |
| P-010 | Chat-only Erkenntnisse gehen bei Neustart verloren oder sind nicht auditierbar. | Transienter Kontext als impliziter Wahrheitsspeicher. | #6, #9, #25 | U1–U4 | validated | durch §14 bereits mitigiert; weiter überwachen. |
| P-011 | Regionale Forschung kann in statischen Territorial-/Regionalcontainern stecken bleiben. | Überregionale Mobilität, Herrschaft und Kommunikation werden sonst nicht erklärt. | #14 | U2–U3 | validated | #36. |
| P-012 | Mehrfach wiederholte/abgeschriebene Aussage kann wie unabhängige Bestätigung wirken. | Source dependence ist im normalen Literaturworkflow oft unsichtbar. | #12, #21 | U1–U4 | working | #34. |
| P-013 | Akteursnetzwerke und Ko-Präsenz verführen zu unbelegten Beziehungs-/Motivbehauptungen. | Graphische/plausible Nähe ersetzt keine historische Evidenz. | #14, #21 | U2–U3 | working | #37. |
| P-014 | Wissenschaftlicher Forschungsstand kann für Nicht-Spezialisten schwer prüfbar werden. | Fachsprache, Evidenzstatus, Methoden und Kontroversen sind komplex. | #9, #20 | U1–U4 | validated | #38. |
| P-015 | Provider-/Tool-Abhängigkeit kann Basisfunktionen oder Forschungswissen unzugänglich machen. | Cloud-/AI-/Plugin-Lock-in. | #8, #24 | U4 + systemweit | validated goal/risk | #39/#40. |
| P-016 | Technische Lösungsideen können sich zu früh als vermeintliche Requirements verfestigen. | Solution Bias: Zotero/SQLite/Graph/RAG/Multi-Agent etc. | #1, #3, #6, #8, #24 | systemweit | validated | #28 trennt Hypothesen; #42 Traceability. |

---

# 5. Challenges

| ID | Challenge | Beschreibung | Provenienz | Use Cases | Status / nächste Aktion |
|---|---|---|---|---|---|
| CH-001 | Heterogene Evidenzlogiken | Urkunden, Akten, Rechnungen, Karten, archäologische Befunde, Ortsnamen, OCR usw. tragen unterschiedliche Aussagen. | #13, #15, #19 | U1–U4 | working → #31/#33/#34. |
| CH-002 | Historische Begriffe sind zeit-, raum- und institutionsabhängig. | Synonymisierung oder moderne Übersetzung kann anachronistisch sein. | #16, #19 | U1–U3 | working → #32. |
| CH-003 | Regionale Verwaltung und Territorialität verändern sich über Zeit. | Zuständiges Archiv/Institution/Ort kann nicht statisch modelliert werden. | #14, #16 | U1–U3 | research-needed → #31/#36. |
| CH-004 | Überlieferung ist lückenhaft und asymmetrisch. | Nichtfinden ist kein historischer Negativbeweis; Completeness Claims brauchen Search Boundary. | #9, #12, #45 | U1–U4 | validated challenge → alle SOTA-Pakete. |
| CH-005 | Fachliche Forschungstraditionen sind selbst historisch/umstritten. | Alte Meistererzählungen und Begriffe müssen historiographisch kontrolliert werden. | #13, #15, #16 | U1–U3 | research-needed → #32/#33/#36/#37. |
| CH-006 | Transdisziplinäre Integration ohne epistemische Nivellierung | Gleiche Begriffe/Befunde können in Disziplinen unterschiedliche Bedeutung haben. | #13, #19 | U1–U4 | working → #33/#41. |
| CH-007 | Maßstabswechsel ist interpretativ | Mikro-, Territorial- und europäische Perspektiven können verschiedene Erklärungen erzeugen. | #14 | U1–U3 | research-needed → #36. |
| CH-008 | Qualität offener semantischer Unterstützung messen | Problemübersetzung, Expertise Routing und Synthese haben keine einfache einzelne Metrik. | #22, #45 | U1–U4 | research-needed → #32/#33/#38/#39. |
| CH-009 | Rechte und Zugänge sind quellen-/anbieterabhängig | Speicherung, OCR, Cloudverarbeitung und Veröffentlichung können unterschiedlich zulässig sein. | #4, #6, #24 | U1–U4 | research-needed → #40 / tool-spezifisch später. |
| CH-010 | Unabhängige Fachvalidierung ist knapp/teuer | Nicht jede Arbeit kann extern geprüft werden; Prüfintensität muss proportional sein. | #9, #12, #15, #45 | U1–U4 | working → #33/#40/#42. |
| CH-011 | Wissenschaftliche Invarianten technisch erzwingen, ohne Fachmodell zu überformen | Einige Regeln sind formal, andere interpretationsabhängig. | #24 | systemweit | research-needed → #39/#41/#42. |

---

# 6. Risks / Failure Modes Seed

| ID | Risk / Failure Mode | Folge | Provenienz | Use Cases | Status | Nächste Aktion |
|---|---|---|---|---|---|---|
| R-001 | Source Laundering | Katalog/Regest/OCR/Snippet erscheint als direkt inspizierte Primärevidenz. | #9, #12 | U1–U4 | high | #31/#34/#40. |
| R-002 | Verlorene/ungenaue Fundstelle | Aussage wird faktisch nicht nachprüfbar. | #4, #5 | U1–U4 | high | #31/#35/#40. |
| R-003 | OCR/HTR-Fehler bei Namen, Orten, Zahlen, Fachtermini | Falsche Retrieval-/Entity-/Interpretationsergebnisse. | #4 | U1–U4 | high | #35/#40. |
| R-004 | Retrieval Blind Spot | Relevante Quelle bleibt wegen historischer Variante/Terminologie unsichtbar. | #5, #19 | U1–U4 | high | #32/#35/#40. |
| R-005 | Anachronistische Begriffsgleichsetzung | Falsche Problemdefinition und Suche. | #16, #19 | U1–U3 | high | #32/#40. |
| R-006 | False corroboration durch abhängige Quellen | Evidenzstärke wird überschätzt. | #12, #21 | U1–U4 | high | #34/#40. |
| R-007 | Widersprüche werden vorschnell harmonisiert | Erkenntnispotenzial und Unsicherheit verschwinden. | #15, #21 | U1–U4 | high | #34/#40. |
| R-008 | Falsche Entity-Zusammenführung | Personen/Orte/Institutionen werden historisch falsch verbunden. | #14, #24 | U2–U3 | high | spätere ER-SOTA/Requirement; #40. |
| R-009 | Ko-Präsenz/Netzwerkmetrik wird als Beziehung oder Motiv gewertet | Historische Überinterpretation. | #14, #21 | U2–U3 | high | #37/#40. |
| R-010 | Presentistische Motivpsychologie | Akteursanalyse erzeugt elegante, aber unbelegte Erklärung. | #15, #21 | U2–U3 | high | #37/#40. |
| R-011 | Regionaler Container-Bias | Relevante transregionale Ursachen/Quellen bleiben außen. | #14 | U2–U3 | medium-high | #36/#40. |
| R-012 | False consensus durch mehrere KI-Ausgaben | Modellkorrelation erscheint als unabhängige Expertenmeinung. | #15, #24 | U1–U4 | high | #33/#39/#40. |
| R-013 | Fachrollen sind nur unterschiedliche Prompts | Simulierte statt methodisch gestützte Expertise. | #15, #16, #19 | U1–U4 | high | #33/#40. |
| R-014 | Technisches Datenmodell schreibt Fachkategorien vor | Wissenschaftliche Differenzen werden technisch nivelliert. | #16, #19, #24 | systemweit | high | #39/#41/#42. |
| R-015 | Semantische Suche ersetzt exakte Quellenrecherche | Namen/Termini/Fundstellen werden schlechter auditierbar. | #5, #8, #24 | U1–U4 | high | #35/#39/#40. |
| R-016 | Generative KI mutiert kanonischen Zustand still | Provenienz/Verlässlichkeit sinkt. | #24 | systemweit | high | #39/#40/#42. |
| R-017 | Provider-/Format-/Plugin-Lock-in | Forschungszustand wird nicht restartbar. | #8, #24 | systemweit | medium-high | #39/#40. |
| R-018 | Stille Daten-/Modellmigration | Semantik/Provenienz verändert sich unbemerkt. | #12, #24 | systemweit | high | #39/#40/#42. |
| R-019 | Rechteverletzung durch Speicherung/Cloud-OCR/LLM-Upload | Rechtliches/ethisches Risiko, Quellenverlust durch Sperren. | #4, #6, #24 | U1–U4 | high | #40; konkrete Anbieter später. |
| R-020 | Research UX vereinfacht wissenschaftliche Unterschiede | Nutzer erhält verständliche, aber falsche Eindeutigkeit. | #9, #20 | U1–U4 | high | #38/#40. |
| R-021 | Vermittlungsnarrativ schreibt in Research State zurück | Forschungszustand wird adressatenspezifisch verzerrt. | #20, #21 | U1–U4 | high | #38/#40/#42. |
| R-022 | Nutzer muss technische/fachliche Routine mikromanagen | System verfehlt Assistenznutzen. | #9, #12 | U1–U4 | medium-high | #29/#38/#39. |
| R-023 | Zu frühe Architektur-/Agenten-/Ontologieentscheidung | Lock-in und Solution Bias vor validierten Requirements. | #1, #10, #19, #24 | systemweit | high | durch Execution-Gates mitigieren; #43. |
| R-024 | „Nicht gefunden“ wird als Vollständigkeit/Abwesenheit interpretiert | Falscher historischer Negativschluss. | #12, #45 | U1–U4 | high | Search Boundary Pflicht; #40. |
| R-025 | Qualitätskontrolle wird generische QA statt fachgebunden | Fachmethodik wird durch Checklistenformalismus ersetzt. | #9, #45 | systemweit | high | Domain-fit-Regel in #45; #41. |

---

# 7. Constraints

| ID | Constraint | Provenienz | Reife | Konsequenz |
|---|---|---|---|---|
| K-001 | Fachstandards dürfen durch Technik, UI, Nutzerformulierung oder Vermittlungswunsch nicht abgeschwächt werden. | #9, #20 | validated | Harte wissenschaftliche Invariante. |
| K-002 | Chat darf kein unverzichtbarer Wahrheitsspeicher sein. | #9, §14 / docs/research/README.md | validated | Substantielle Ergebnisse persistent dokumentieren. |
| K-003 | Research State und Vermittlung bleiben getrennt. | #20 | validated | Keine RGK-/Public-History-Anforderungen als Core-Truth. |
| K-004 | KI-Ausgabe ist keine Evidenzklasse und keine unabhängige Fachvalidierung. | #9, #12, #15, #45 | validated | Evidence/validation status explizit. |
| K-005 | Original, digitale Instanz, Derivat und Interpretation dürfen nicht still zusammenfallen. | #4, #6, #9, #12 | validated | Provenienz-/Statusmodell muss Trennung ermöglichen. |
| K-006 | Exakte Fundstellen müssen erhalten bleiben, soweit sie bekannt/ableitbar sind. | #4, #5 | validated | OCR/Retrieval/Exports müssen Findspot-preserving sein. |
| K-007 | Kein neues Issue pro Finding; one fact / one canonical home. | #23, docs/research/README.md | validated | Issue = Work Owner; Research-Datei = Vollinhalt. |
| K-008 | Keine Technologie wird Requirement nur aufgrund Verfügbarkeit/Attraktivität. | #1, #10, #24 | validated | Solution-neutral Requirements. |
| K-009 | Reversible/bounded Research Debt darf Weiterarbeit nicht unnötig blockieren. | #27, #44 | validated | Nur echte Decisions/Dependencies eskalieren. |
| K-010 | Rechte/Datenschutz/Nutzungsbedingungen können technische Optionen ausschließen. | #22, #24 | working | Vor tool-specific Architecture klären. |
| K-011 | Regionaler Fokus ist Anker, nicht geschlossene geografische Systemgrenze. | #14 | validated | Scope dynamisch nach historischer Relevanz. |

---

# 8. Open Questions

| ID | Open Question | Ursprung | Verknüpfte Needs/Risks | Geplanter Owner / nächste Aktion |
|---|---|---|---|---|
| OQ-001 | Welche minimale fachliche Provenienz-/Fundstelleninformation braucht Histo-Orla je Quellentyp? | #2/#4/#6 | N-004–N-006, R-001/R-002 | #31. |
| OQ-002 | Wie lässt sich Archive Routing aus historischer Verwaltung/Registratur praktisch und methodisch unterstützen? | #2/#19 | N-004, P-006 | #31. |
| OQ-003 | Wie werden historische, archivische, analytische und historiographische Begriffe methodisch getrennt und entdeckt? | #16/#19 | N-001, R-005 | #32. |
| OQ-004 | Wie misst man gute fachliche Problemübersetzung statt bloßer plausibler Synonyme? | #22/#32-Plan | N-001/N-018 | #32. |
| OQ-005 | Was macht ein operationales Expertise Profile wirklich fachlich belastbar? | #15/#16/#19 | N-002/N-003/R-013 | #33. |
| OQ-006 | Welche Trigger aktivieren Nachbardisziplinen bzw. externe Fachvalidierung? | #19/#45 | N-002/N-019 | #33. |
| OQ-007 | Wie wird Source Dependence/Corroboration methodisch operationalisiert? | #12/#21 | N-009, R-006 | #34. |
| OQ-008 | Welche Discrepancy-Kategorien sind fachlich tragfähig und nicht bloß RGK-internes Muster? | #21 | N-010, R-007 | #34. |
| OQ-009 | Welche OCR-/HTR-Verfahren und Formate passen zu den realen Materialien und erhalten Layout/Fundstellen? | #4 | N-007, R-003 | #35. |
| OQ-010 | Welche Search-Baseline liefert guten Recall bei Auditierbarkeit; wann ist semantische Suche tatsächlich additiv nützlich? | #5/#8 | N-008, R-004/R-015 | #35. |
| OQ-011 | Wie werden historische Orte/Territorien/Scale Shifts zeitabhängig und ohne Container-Bias behandelt? | #14 | N-012, R-011 | #36. |
| OQ-012 | Wie rekonstruiert man Handlungssituationen und mögliche Motive ohne presentistische Psychologisierung? | #21 | N-011, R-009/R-010 | #37. |
| OQ-013 | Welche Research-UX-/Progressive-Disclosure-Muster erlauben Laienverständlichkeit und Fachaudit zugleich? | #9/#12/#20 | N-009/N-014/G-009, R-020 | #38. |
| OQ-014 | Welche Capability gehört Mensch, deterministischer Software, spezialisierten Verfahren oder LLM? | #24 | N-017, R-016/R-017 | #39. |
| OQ-015 | Welche Rechte-/Lizenz-/Privacy-Constraints gelten für typische Quellen- und Toolklassen? | #4/#6/#24 | N-016, R-019 | #40, später tool-specific. |
| OQ-016 | Reicht Zotero als bibliographische Referenzschicht für relevante Quellentypen und Workflows? | #3 | U4, N-004/N-006/N-015 | in #29 operationalisieren; technisch/fachlich #31/#35/#39. |
| OQ-017 | Welche Daten gehören langfristig versioniert, welche sind regenerierbare Processing-Artefakte? | #6 | N-015, R-017/R-018 | #39/#41; §14 deckt Research-Artefakte bereits. |
| OQ-018 | Welche tatsächlichen Automatisierungsfriktionen sind häufig genug, um Software zu rechtfertigen? | #8/#24 | N-017/P-009 | #29, danach #39. |
| OQ-019 | Welche Capabilities sind architecture-driving und welche können als bounded Research Debt später reifen? | #10/#43 | systemweit | #41/#42/#43. |

---

# 9. Hypotheses – ausdrücklich keine Requirements

| ID | Hypothese | Ursprung | Status | Wie diskriminieren? |
|---|---|---|---|---|
| H-001 | Zotero ist die zentrale bibliographische Kopplung. | #3 | hypothesis | U4-Workflow, Quellen-/Quellentypabdeckung, API/Attachment/Keys und SOTA prüfen. |
| H-002 | Script-first/local-first/AI-optional ist geeignete technische Grundrichtung. | #8 | architecture hypothesis | #39 + spätere Architecture-Varianten gegen Requirements. |
| H-003 | SQLite/FTS5 könnte lokaler Katalog/Search-Baseline sein. | #8 | technical hypothesis | erst nach #35/#42 Benchmark/Prototyp. |
| H-004 | Embeddings/RAG liefern zusätzlichen Retrievalnutzen. | #5/#8 | hypothesis | #35: Gold Queries gegen Exact/Fuzzy/linguistic Baseline testen. |
| H-005 | Knowledge Graph ist geeignete Repräsentation für Akteure/Relationen/Räume. | #14/#19 | architecture hypothesis | #36/#37 fachlich klären; erst danach #39/#43. |
| H-006 | Multi-Agent-System ist geeignete technische Form für fachliche Modularität. | #19 | hypothesis | #33 zeigt notwendige epistemische Trennung; #39 prüft einfachere Umsetzung. |
| H-007 | Candidate→Review→Promotion ist geeigneter Standard für probabilistische/LLM-Ergebnisse. | #12/#24 | strong hypothesis | externen SOTA in #39 + Use-Case-Risiken prüfen. |
| H-008 | Kuratierte Forschungsartefakte versionieren, regenerierbare Indizes/Caches nicht zwingend. | #6/#12 | strong hypothesis | #39/#41; Rechte/Portabilität prüfen. |
| H-009 | Mehrere human-readable Views können aus einem kanonischen Research State abgeleitet werden. | #12/#20/#21 | strong hypothesis | #38; kein Back-write. |
| H-010 | RGK-Discrepancy-Pattern lässt sich als historische Diagnosemethode generalisieren. | #21 | research hypothesis | #34 gegen Quellenkritik/Textkritik/Historiographie. |
| H-011 | RGK-Akteurslogik lässt sich als historische Situation Analysis generalisieren. | #21 | research hypothesis | #37 gegen Mikrogeschichte/Praxeologie/Prosopographie etc. |

---

# 10. Problemcluster und Cross-Cutting-Abhängigkeiten

## Cluster A – Problemformulierung und fachliche Orientierung

Kern: P-001, P-007; N-001–N-003; R-005/R-013.  
Forschung: #32/#33.  
Ohne diesen Cluster kann der Nutzer zwar suchen, aber systematisch am fachwissenschaftlichen Problem vorbeisuchen.

## Cluster B – Quellen-/Archivfindung, Identität, Provenienz

Kern: P-002/P-006; N-004–N-006; R-001/R-002/R-024.  
Forschung: #31/#34.  
Cross-cutting für U1–U4.

## Cluster C – digitale Erschließung und Retrieval

Kern: P-003–P-005; N-007/N-008; R-003/R-004/R-015.  
Forschung: #35.  
U4 ist Hauptworkflow, U1–U3 liefern fachliche Stressfälle.

## Cluster D – epistemische Tiefe, Abhängigkeit, Kontroverse

Kern: N-009/N-010/N-013/N-014; R-006/R-007/R-012.  
Forschung: #34/#33; Synthese #41.

## Cluster E – Raum, Akteure, Erklärung

Kern: N-011/N-012; R-009–R-011.  
Forschung: #36/#37.

## Cluster F – Human Readability / Governance

Kern: G-009/G-010; P-010/P-014; R-020–R-022.  
Forschung: #38; Governance #9/#20.

## Cluster G – technische Allokation, Portabilität, Rechte

Kern: N-015–N-020; P-009/P-015/P-016; R-016–R-019/R-023.  
Forschung: #39/#40; Architektur erst nach #42/#43.

---

# 11. Spannungen, die bewusst offen bleiben

1. **Automatisierung ↔ menschliche/fachliche Kontrolle:** kein Widerspruch, solange mechanische Arbeit automatisiert und consequential judgment kontrolliert bleibt; reale Grenzfälle in #29/#39.
2. **Human Readability ↔ fachliche Tiefe:** soll durch Progressive Disclosure statt Inhaltsreduktion gelöst werden; #38.
3. **Regionaler Fokus ↔ europäischer Horizont:** kein fester geografischer Scope; Scale Shift nach historischer Relevanz; #36.
4. **Offene semantische KI ↔ Reproduzierbarkeit:** KI nur in begrenzten Rollen; kanonische Invarianten deterministisch; #39.
5. **Lean ↔ robustes System:** Lean bedeutet minimale unnötige Komplexität, nicht minimale Funktionalität; #39/#43.
6. **Zotero-Nähe ↔ provider-/toolunabhängiger Forschungszustand:** erst durch U4/SOTA bewerten; H-001.
7. **Formalisierung ↔ fachliche Pluralität:** Repräsentation darf erst aus validierten fachlichen Unterscheidungen abgeleitet werden; #41/#42.

---

# 12. Qualitätscheck #45 für WP-A

- **Domain fit:** Research Strategy, Scholarly Requirements Engineering, Human Factors, Research Integrity, Governance/RDM aktiviert; fachliche Domänen nur dort zugeordnet, wo der Problembefund dies verlangt.
- **Evidence fit:** Baseline leitet sich aus kanonischem Repo-Zustand ab; sie behauptet noch keinen externen fachlichen SOTA.
- **Inference fit:** Ziel/Need/Pain/Challenge/Risk/Hypothesis wurden getrennt; technische Kandidaten nicht als Requirements promoted.
- **Terminology fit:** Projektinterne Begriffe werden gemäß ihrer aktuellen kanonischen Bedeutung verwendet; fachwissenschaftliche Terminologie wird in #31–#39 extern geprüft.
- **Provenance fit:** Jeder Eintrag verweist auf kanonische Issues/Research-Design als Ursprung.
- **Falsification/challenge:** Für research-needed Punkte ist eine nächste discriminating action bzw. ein SOTA-Owner angegeben.

## Search / Coverage Boundary

Diese Discovery-Baseline ist **keine externe Literaturrecherche**. Abgedeckt ist der aktuelle kanonische Histo-Orla-Konzeptstand aus README, Research-Design und den aktiven fachlichen/technischen Issues, mit internen Prior-Art-Issues #12/#21 als gekennzeichnetem Input. Externe Validierung erfolgt erst in #31–#39.

## Sättigungsbegründung

Für die aktuelle Discovery-Entscheidung ist Sättigung erreicht, wenn weitere kanonische Issue-Inhalte überwiegend in die oben bestehenden Cluster fallen und keine neue Problemklasse erzeugen. Die Baseline bleibt versionierbar und kann durch #29/#30 korrigiert werden.

## Nächster Schritt

#29: U1–U4 als reale Research Workflows rekonstruieren und Pains/Judgment/Automation an konkreter Arbeit validieren. Parallel darf #30 vorbereitet werden, sobald genug Workflow-Signale vorliegen.
