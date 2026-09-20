# Histo-Orla – Deep Research zur sozio-technischen Forschungsarchitektur

**Datum:** 2026-09-20  
**Work Owner / Review-Kontext:** #64  
**Architecture-/Delivery-Schnittstelle:** #48 / #59 / #92  
**Research-/Method-Schnittstelle:** #45 / #46 / #47 / #60  
**Requirements Authority:** ausschließlich #42  
**Repo-Baseline der Untersuchung:** `main` @ `ff2bc993d959afd594dff2acf772e0e608963f97` (Merge PR #117)  
**Status dieses Artefakts:** Deep-Research-/Review-Evidence und falsifizierbare Entwicklungsdiagnose. **Keine** Requirement-, Method-, Historical-, Selection- oder Architecture-Decision-Authority.

---

## Evidence-Legende

Wesentliche Aussagen werden nach Herkunft unterschieden:

- **Repo Evidence** – direkt aus aktuellem Repository-State, Issues, PR-/Commit-Chronologie oder versionierten Artefakten.
- **Owner Signal** – dokumentiertes Research-/Product-/Workflow-Feedback des Owners; keine automatische Requirement- oder Architecture-Promotion.
- **External SOTA Evidence** – externe Literatur, Standards, aktuelle offizielle Dokumentation oder belastbare System-/OSS-Evidence.
- **Researcher Inference** – aus mehreren Evidenzen abgeleitete, falsifizierbare Interpretation.
- **Recommendation** – vorgeschlagene, reversible Handlungsrichtung; keine bereits akzeptierte Entscheidung.

Die Untersuchung folgt der Reihenfolge:

```text
real Research Need / Pain
→ fachliche Methode / epistemische Grenze
→ accepted Requirement
→ vorhandenes Tool / Standard / Pattern
→ avoid
→ reuse
→ configure
→ integrate
→ thin custom layer
→ erst zuletzt custom build
```

---

# A – Executive Diagnosis

## A.1 Zentrales Problem

**Repo Evidence:** Histo-Orla besitzt bereits einen ungewöhnlich klaren Bestand an Goals/Needs/Pains, accepted Requirements, wissenschaftlichen Schutzregeln, Source-/Instance-/Findspot-Trennung, Method-Authority, Restartability- und Traceability-Anforderungen. #64, `PROJECT_STATE.md` und das reale Owner-Feedback dokumentieren inzwischen ausdrücklich, dass der Engpass **nicht primär fehlende Governance** ist, sondern die operative Integration: reale Forschung bleibt zu manuell, chat-orchestriert, textlastig und meta-systemzentriert.

**Owner Signal:** Der Owner beschreibt den Zustand in #64 als „Governance-Sumpf“, kritisiert verwaschene Piloten und verlangt einen 5-Minuten-Handoff sowie einen engen, wirklich nutzbaren Vertical Research Slice, bevor weitere Meta-Ausweitung legitim ist.

**Researcher Inference:** Das aktuelle Kernproblem ist am besten als **Interface-/Orchestrierungsdefizit zwischen epistemischen Verantwortungen** zu verstehen. Der Owner übernimmt heute teilweise die Übersetzung

```text
unscharfe Forschungsfrage
→ fachliche Problembegriffe
→ zuständige Domänen/Methoden
→ Evidence Demand
→ Tool-/Quellenzugriff
→ Source/Instance/Findspot-Sicherung
→ Identity/Reconciliation
→ Research State
→ Synthese / unresolved
→ Restart / nächster Schritt
```

und wird damit selbst zum **Semantic Compiler und Workflow Engine**. Genau diese Integrationsarbeit soll Histo-Orla laut G-002/N-001, N-002/P-007, N-017, G-007/P-009 und G-008/P-010 reduzieren.

**External SOTA Evidence:** Transdisziplinäre Integrationsliteratur beschreibt erfolgreiche Integration nicht als notwendige Vereinheitlichung, sondern als offenen, interaktiven Prozess, in dem Pluralität erhalten bleiben kann. Boundary Objects funktionieren gerade deshalb, weil sie zwischen heterogenen Perspektiven robust identifizierbar, aber lokal anpassbar bleiben. Mixed-Initiative-HCI plädiert für die Kopplung von Automation mit direkter menschlicher Kontrolle statt Totalautomation. Sensemaking-/Exploratory-Search-Arbeit zeigt, dass Expert:innen iterative Such-, Strukturierungs- und Syntheseprozesse durchlaufen und dass Resumption/Provenance Teil der Arbeitsoberfläche sein müssen.

## A.2 Warum die Entwicklung im Kreis lief

Die PR-Sequenz #108–#116 dokumentiert ein besonders dichtes Beispiel:

- #108–#110: Owner-Mental-Models und Wissensraum-Metaphern werden zunehmend in Objekt-/Architekturhypothesen übersetzt.
- #111: explizite Rückstufung auf User-Research-Signal.
- #112–#115: erneute nützliche, aber teils zu schnelle Modell-/Taxonomieverdichtung.
- #116: kritischer Self-Audit benennt das Muster `Owner signal → assistant abstraction → repo persistence`.
- #117: bewusste Rückkehr zu einem realen Cross-Pilot; dieser stützt nur einen kleineren gemeinsamen evidenziellen Untergrund und **nicht** die stärkere globale Observation-/Relation-/Event-Spine.

**Researcher Inference:** Vier Mechanismen verstärkten sich gegenseitig:

1. **Mirroring/affirmative abstraction:** plausible Owner-Metaphern wurden zu schnell als Systemstruktur gelesen.
2. **Meta-persistence:** fast jede neue Nuance erzeugte neue Repo-Artefakte und Folge-Reconciliation.
3. **Governance as compensation:** fehlende Produktintegration wurde teilweise durch immer sauberere Meta-Trennung kompensiert.
4. **Empirical lag:** Gegenlesarten, SOTA und heterogene reale Tests kamen zu spät.

## A.3 Größter Hebel

**Recommendation:** Der wahrscheinlich höchste nächste Hebel ist **kein neues universelles Datenmodell**, sondern ein integrierter, falsifizierbarer **Research Workbench Thin Slice** auf Basis der bereits akzeptierten Semantik:

1. kleiner gemeinsamer Source-/Instance-/Findspot-/Provenance-/Identity-Untergrund;
2. klar typisierte, discoverable Capabilities mit Authority-, Evidence-, Side-effect- und Failure-Verträgen;
3. regenerierbarer lokaler Query-/Read-Layer als **abgeleitete** Sicht, nicht als zweite Wahrheit;
4. Research-output-first UX:
   `Question → current synthesis → Befundkomplexe → unresolved / next evidence → provenance drill-down`;
5. Git/GitHub als Change-Control-/Review-/Provenance-Grenze für kuratierte Mutation, **nicht** als alleinige interaktive Research Runtime;
6. reale End-to-End-Messung der Owner-Arbeit, die entfällt.

Das ist zunächst eine **Hypothese**, die mit #47 und weiteren realen Aufgaben falsifiziert werden muss.

---

# B – Intent & Development Genealogy

## B.1 Stabiler Projektintent

Aus `AGENTS.md`, `README.md`, `PROJECT_STATE.md`, #28, #42, #45, #48, #50, #55, #60, #63 und #64 ergibt sich ein stabiler Intent:

- funktionierendes privates Forschungssystem statt Konzeptpapier oder KI-Demo;
- unscharfe Nutzerfrage darf unscharf bleiben; das System hilft bei fachlicher Problemübersetzung;
- Fachdomänen und Methoden besitzen wissenschaftliche Authority; AI-Ausgabe ist keine Evidenz;
- Quelle, Repräsentation, konkrete Instanz, Derivat, Fundstelle, Exzerpt/Observation, Finding, Interpretation und Synthese dürfen nicht still verschmolzen werden;
- Unsicherheit, Widerspruch und `unresolved` sind legitime kanonische Zustände;
- Restartability ohne alten Chat;
- Automation mechanischer, organisatorischer und rekonstruierbarer Arbeit;
- menschlich lesbare historische Synthese mit auditierbarem Drill-down;
- Lean = minimale unnötige Komplexität, nicht reduzierte wissenschaftliche Qualität;
- Dev implementiert accepted Requirements, erfindet nicht eigenmächtig Needs oder historische Semantik.

## B.2 Entwicklungsphasen

### Phase 1 – Problem-/Research-Discovery

#28 und foundational Research Design etablieren Goals/Needs/Pains, unscharfe Problemübersetzung und den transdisziplinären Scope.

### Phase 2 – Wissenschaftliche und technische Schutzschichten

#42, #45, #50, #60, #62, #63 trennen Authority, Requirement, Method, Source Identity, formale Assurance und Delivery Trace. Diese Trennung behebt reale frühere Risiken wie Source Laundering, Chat-State und AI-Plausibilität.

### Phase 3 – Owner-Feedback und Product-Rebaseline

#64 und #92 erkennen die Gegenbewegung: Schutzschichten funktionieren semantisch, aber der Research Owner sieht zu viel Systemprozess und zu wenig integrierten Forschungsarbeitsplatz. Der neue Maßstab wird Research Value statt Meta-Vollständigkeit.

### Phase 4 – PR-Cluster #108–#116

Eine Serie von neun konzeptionellen/korrektiven PRs versucht Wissensraum, Perspektiven, Zeit, Relationen und Modellpluralität zu operationalisieren. Mehrfach werden vorherige Abstraktionen zurückgestuft.

### Phase 5 – PR #117: empirische Rückkehr

Der Saalfeld-Cross-Pilot testet die stärkeren Hypothesen an realem Evidenzmaterial und begrenzt sie: gemeinsame Source-/Instance-/Findspot-/Provenance-Strukturen sind robuster als universelle Observation-/Relation-/Event-Semantik.

## B.3 Correction / Iteration Ledger

| PR | Trigger / Ziel | Interpretation / Intervention | Failure Class / Korrektur | Residual Lesson |
|---|---|---|---|---|
| #108 | Langdiachronie / regionaler Wissensraum | foundational scope expansion | noch keine Requirement-Promotion | Mental Model ist Forschungsinput, kein Schema |
| #109 | Shared-state Audit | starke Hypothese zu gemeinsamem State; reale ID-Kollision sichtbar | Pilot-Generalisation-Risiko | konkrete Identity-/Reuse-Pains sind stärker als Globalmodell |
| #110 | „übergreifender Wissensraum“ | explizitere globale Objekte/Strukturen | **zu starke Promotion** | Metapher ≠ Architektur |
| #111 | Owner-Korrektur | Reclassification als User Research | explizite Korrektur | Signal → Alternativen → SOTA/realer Test vor Promotion |
| #112 | Multiperspektivität | Projektionen, Zeit-/Raum-/Relationshypothesen | nützlich, aber weiterhin modellnah | Derived View ist oft sicherer als Mutation |
| #113 | Korrektur der Überwörtlichkeit | Perspektiv-/Pluralitäts-Synthese | korrektive Reframing-Arbeit | Integration ohne Universalspine möglich |
| #114 | Temporalität | temporale Differenzierungen | SOTA zu spät / Taxonomie-Risiko | Methode/Fachliteratur vor globaler Temporalität |
| #115 | Konflikt vs Modellpluralität | unterschiedliche epistemische Fälle getrennt | Taxonomie/Object-Model noch nicht belegt | Widerspruch und Pluralität nicht flatten |
| #116 | Self-Audit | komplette Chat→Repo-Operationalisierung kritisch revidiert | Meta-/Persistence-/Mirroring-Loop explizit | weniger persistieren, früher falsifizieren |
| #117 | realer Cross-Pilot | Saalfeld 1056–1071 | empirischer Gegencheck | kleiner Evidenzkern gestützt; starke Spine nicht gestützt |

### Quantifizierung

**Repo Evidence:**

- #108–#116 = **9** unmittelbar aufeinanderfolgende konzeptionelle/korrektive PRs.
- Zeitspanne #108 → #116: **16 h 26 min 01 s**.
- #110 → #111: **8 min 52 s** bis zur expliziten Reclassification/Korrektur.
- #112 → #116: **5 PRs in 40 min 05 s**.
- #116 → #117: **12 h 08 min 42 s** bis zum nächsten evidence-bearing Cross-Pilot.
- Innerhalb #108–#117 liegt damit ein sichtbares Cluster von neun Discovery-/Concept-/Audit-/Correction-Schritten vor dem empirischen Cross-Pilot #117.

Diese Zahlen sind **kein projektweiter Produktivitätsindikator**; sie beschreiben nur das dokumentierte Cluster.

### Owner-Korrekturcount – Evidenzgrenze

Eine exakte Zahl „wie oft der Owner korrigieren musste“ ist aus dem Repository **nicht belastbar rekonstruierbar**, weil nicht jede Chat-Korrektur als eigene Repo-Mutation erhalten ist.

Konservativ belegbar sind:

- **mindestens 1 explizite Owner-Korrektur** in der PR-Sequenz (#111);
- **mindestens 3 repository-visible Correction/Self-Audit-Interventionen** (#111, #113, #116);
- weitere Owner-Signale und Korrekturen sind in #64 und im Self-Audit beschrieben, lassen sich aber nicht seriös als eindeutige Einzelereignisse zählen.

**Researcher Inference:** Schon diese Untergrenze genügt für die qualitative Feststellung, dass der Owner wiederholt Framing-, Authority-, Lifecycle- und Abstraktionsarbeit übernehmen musste, die das Assistenzsystem künftig reduzieren soll.

## B.4 Das Ringen als Need-/Requirement-Evidence

Das Entwicklungsringen bestätigt insbesondere:

- **G-002 / N-001:** unscharfe Frage braucht fachliche Problemübersetzung;
- **N-002 / P-007:** Owner darf Domain Routing und Methodenauswahl nicht vollständig selbst leisten müssen;
- **N-017:** Capability Allocation muss expliziter werden;
- **P-008:** plausible KI-Synthese ohne fachliche Belastbarkeit ist Risiko;
- **P-009:** manuelle Orchestrierung ist reales Product Pain;
- **P-010:** Chat darf kein impliziter Forschungszustand sein;
- **P-014:** Komplexität muss menschlich prüfbar bleiben;
- **P-016 / AP-12:** Lösungshypothesen härten zu früh;
- **AP-10:** Human as Workflow Engine ist inzwischen nicht nur abstraktes Anti-Pattern, sondern beobachteter Prozessfehler.

**Researcher Inference:** Der wiederholte Owner-Korrekturaufwand ist deshalb plausibel als **Product-/Acceptance-Failure des aktuellen Integrationsmodus** zu behandeln. Er ist noch keine quantifizierte Baseline; genau diese muss in den nächsten realen Tasks erhoben werden.

---

# C – Root Causes

| Failure Class | Beobachtete Evidenz | Gegenlesart | Theorie/SOTA-Erklärung | Mögliche Intervention | Risiko |
|---|---|---|---|---|---|
| Schema-/Ontology-first tendency | #110, Teile #112–#115; #116 Self-Audit | Strukturierung war Versuch, echte Cross-Case-Pains zu lösen | Scientific Pluralism / Boundary Objects warnen vor erzwungener semantischer Einheit | kleinste gemeinsame Identity-/Evidence-Grenze; Domain-Semantik lokal | Untergeneralisierung |
| Mirroring / affirmative abstraction | #116 benennt es explizit | frühes Spiegeln kann Verständnis beschleunigen | User Research verlangt alternative readings und Validierung | Owner-Signal standardmäßig als Discovery-Evidence klassifizieren | zu langsame Reaktion |
| Meta-Persistence Loop | viele eng getaktete Artefakt-/PR-Schritte | Persistenz schützt Restartability | Provenienz ist wertvoll, aber nicht jede Denkbewegung ist kanonischer State | Persistenzkriterium + Derived Views + Session-Logs nur bei Nutzen | Verlust relevanter Nuance |
| Governance Accretion | #64 Owner-Feedback „Governance-Sumpf“ | Schutzschichten beheben reale Fehler | socio-technical design: Prozess muss Arbeitsziel dienen | Meta-Erklärungen komprimieren/generieren; research-first front door | Guards werden unsichtbar |
| Atomization without synthesis | #50/#55 starke Traceability, Owner-UX offen | atomare Findings sind auditierbar | Sensemaking benötigt Frames/Schemata/Synthese | Befundkomplex als zunächst **derived grouping**, nicht neues Truth-Object | abgeleitete Gruppierung kann relevante Bedeutung verstecken |
| Architecture by metaphor | Netz/Achsen/Wissensraum aus Owner-Sprache | Metaphern sind wichtige Mental-Model-Signale | HCI: Mental Model informiert Design, schreibt Implementierung nicht vor | Metapher → Bedürfnis → alternatives Lösungsset → Test | zu starke Entkopplung vom Nutzerdenken |
| Over-generalization from similar pilots | Saalfeld/Knau/Orlagau liegen methodisch relativ nah | Nähe erlaubt kontrollierte Wiederholung | Generalisierung braucht Variation der Fälle | #47 als heterogener Landscape/GIS/Archiv-Gegenfall | Methodenmangel kann Architekturtest verfälschen |
| Under-generalization / Markdown silos | ID-Kollision, inverse Navigation, case-lokale State-Fragmente | lokale Artefakte bewahren Kontext | Boundary Objects brauchen robuste gemeinsame Identität | Alias/Reconciliation + Search + Derived Backlinks zuerst | späterer Migrationsbedarf |
| Assurance vs Value | Green CI, formale Traceability, Owner Acceptance offen | Assurance verhindert echte Schäden | Verification ≠ Validation ≠ Utility | Research-Value-Metriken neben technische Checks | Messung wird selbst Bürokratie |
| Work-owner complexity | viele semantisch richtige Owner | klare Verantwortungen verhindern Authority Drift | CSCW: Koordinationskosten sind real | semantische Owner behalten, operative Handoffs generieren/komprimieren | Verantwortung wird unklar |
| Method paralysis | fail-closed Promotion | wissenschaftlich notwendig | Exploration und Promotion brauchen unterschiedliche Konsequenzgrenzen | exploratory / working / consequential Promotion klar trennen | Working State wird versehentlich zitiert |
| Architecture bootstrap paradox | Capability erst nach Bedarf, Bedarf teils erst mit Capability testbar | schützt vor Speculation | Design Science / evolutionary architecture legitimieren Bau-als-Test | reversible tracer bullets / architecture probes | Spike wird heimlich Produkt |
| Tooling treated as secondary | Zotero/Files/Research Workspace noch Adapter-Sicht | provider independence wichtig | Tooling ist Teil verteilter Kognition | konkrete Tool UX als Capability Acceptance behandeln | Lock-in |
| Human as semantic compiler | Owner verbindet Domain↔Data↔Software↔AI↔Repo | Expert judgement muss menschlich bleiben | mixed initiative: Maschine übernimmt geeignete Teilaufgaben, Mensch behält Judgement | typed capability chain + consequence-boundary approval | Automation kann falsches Framing verstärken |

---

# D – Theory / SOTA Map

## D.1 Transdisziplinarität, Boundary Objects, Trading Zones

**External SOTA Evidence:**

- Star & Griesemer (1989) zeigen, dass heterogene wissenschaftliche Akteure kooperieren können, wenn gemeinsame Objekte lokal anpassbar und zugleich identitätsstabil bleiben.
- Caccamo, Pittino & Tell (2023) analysieren 87 Arbeiten und beschreiben Boundary Objects als Schnittstellen für Knowledge Integration; die Art des Boundary Objects muss zum Integrationsproblem passen.
- Lam et al. (2021) modellieren transdisziplinäre Integration als offenen, multidimensionalen Lernprozess; Konsens ist nur ein möglicher Modus, Pluralität kann bewusst erhalten bleiben.
- Collins, Evans & Gorman (2007) unterscheiden Trading-Zone-Typen und zeigen, dass lokale Interaktionssprachen Kooperation erlauben, ohne vollständige epistemische Homogenisierung.
- Scientific-Pluralism-Literatur betont, dass unterschiedliche Modelle, Erklärungen, Methoden und Ontologien wissenschaftlich produktiv koexistieren können.

**Histo-Orla-Learning:** Der gemeinsame Kern sollte eher **Boundary-Object-Qualitäten** besitzen – Identität, Provenienz, Referenzierbarkeit, Findspot, Kontext – als die Fachsemantik aller Domänen zu besitzen.

**Grenze:** Boundary Objects rechtfertigen keine beliebige Unschärfe. Sie müssen praktisch funktionieren; deshalb ist Cross-Case- und Owner-Use-Test entscheidend.

## D.2 HCI / CSCW / Sensemaking / Expert Knowledge Work

**External SOTA Evidence:**

- Horvitz (1999): Mixed-Initiative-Systeme koppeln Automation und direkte Manipulation; menschliche und maschinelle Beiträge sollen jeweils dort liegen, wo sie passend sind.
- Marchionini (2006): Exploratory Search reicht von Lookup zu Lernen und Untersuchung; Forschung ist kein einmaliges Query→Answer.
- Pirolli & Card (2005): Sensemaking umfasst wiederholte Foraging-/Schema-/Hypothesenbewegungen; Tools sollten diese Prozesse statt nur Ergebnisobjekte unterstützen.
- Parnin & Rugaber (2009/2011) sowie DeLine & Parnin (2010): Unterbrechung erzeugt Resumption-Kosten; automatisch rekonstruierbare Aktivitäts-/Kontext-Cues können Wiederaufnahme unterstützen. Die Domäne ist Softwareentwicklung, daher ist dies **Transfer-Evidence**, kein direkter Nachweis für historische Forschung.
- Analytic-Provenance-Forschung behandelt die Rekonstruktion von Analysewegen als Grundlage für Audit, Reflection und Wiederaufnahme.

**Histo-Orla-Learning:** Restartability darf nicht nur Datenerhalt bedeuten. Die Oberfläche muss **working context, aktuelles Synthesis-Frame, offene Fragen, letzte Evidenzbewegungen und nächste diskriminierende Schritte** rekonstruierbar machen.

## D.3 Digital Humanities / Historical Infrastructure

DH-Systeme zeigen ein wiederkehrendes Muster: Gute Werkzeuge sind stark, wenn sie einen klaren epistemischen Teilbereich besitzen.

- Tropy: archival research photos, Metadata, Notes/Transcription, Suche.
- Zotero: Bibliographie/Attachments/API.
- Recogito/Pelagios: Annotation, Gazetteer-Linking, Ortsbezüge.
- WHG: source-backed place attestations mit Provenienz, Unsicherheit und Zeit.
- nodegoat: dynamische relationale, räumliche und zeitliche Modellierung.
- Heurist: flexible, evolvierbare Humanities-Datenbanken.
- ResearchSpace: CIDOC-CRM-/Knowledge-Graph-zentrierte Cultural-Heritage-Repräsentation.
- Omeka S: publizierbare Linked-Data-Sammlungen.
- Arches: enterprise-grade cultural heritage data management.
- TEI: Textrepräsentation/Edition.
- RiC-O: archivische Records-in-Contexts-Semantik.
- IIIF/Web Annotation: interoperable Präsentation/Annotation und präzise Targets.

**Histo-Orla-Learning:** Standards sollen dort verwendet werden, wo ihre Fachfunktion passt. Keiner dieser Standards ist allein ein universelles Forschungsmodell für Histo-Orla.

## D.4 Provenance / Research Objects

- W3C PROV bietet einen domänenneutralen Kern aus Entity/Activity/Agent sowie Derivation/Attribution/Association.
- RO-Crate 1.3 (2026-06-22, Recommendation) bietet portable Research-Object-Verpackung auf JSON-LD-Basis.
- Web Annotation standardisiert Body/Target/Selector und kann konkrete Text-/Bildsegmente referenzieren.
- Research-Object-Arbeit zeigt, wie Ressourcen, Provenienz und Ausführungsinformationen als transportierbares Paket zusammengehalten werden können.

**Histo-Orla-Learning:** Diese Standards können Export-, Packaging- und Provenance-Grenzen entlasten. Sie sollten **nicht** die interne historische Semantik diktieren.

## D.5 Knowledge Representation unter Unsicherheit und Pluralität

WHG und Wikibase zeigen, dass Statement-/Attestation-level Provenance, Qualifier, mehrere Aussagen und Unsicherheit praktisch tragfähig sind. Gleichzeitig setzen beide Systeme eigene Gegenstands- und Datenmodelle voraus.

**Histo-Orla-Learning:** Das Problem „widersprüchliche Aussagen brauchen Quellen, Kontext und Gültigkeitsbereich“ ist extern gut verstanden. Daraus folgt **nicht**, dass Histo-Orla Wikibase/WHG intern kopieren muss.

## D.6 Research Software Engineering / Scientific Workflows

- FAIR4RS (2022) betont eindeutige/versionierte Identität, reichhaltige Metadaten, standardisierte Zugriffsprotokolle, qualifizierte Referenzen und Wiederverwendbarkeit von Research Software.
- DataLad zeigt Git-basierte Datensatz- und Command-Provenienz, Re-Execution und git-annex-basierte große Daten.
- DVC demonstriert Git-nahe Pipeline-/Datenversionierung, ist aber primär für reproduzierbare Data/ML Pipelines gebaut.
- Nextflow/Snakemake-artige Systeme sind stark bei deterministischen, wiederholbaren Computation Pipelines; historische Interpretation ist keine solche Pipeline.
- Local-first-Prinzipien priorisieren Offline-Fähigkeit, Nutzerkontrolle, Privacy und Langzeitbesitz.
- Evolutionary Architecture verwendet Fitness Functions für objektiv prüfbare Architekturmerkmale; das passt zu deterministischen Invarianten, nicht zu wissenschaftlicher Wahrheit.

## D.7 Requirements / Product Discovery / Design Science

- ISO/IEC/IEEE 29148:2018 bleibt im September 2026 der bestätigte aktuelle Standard, während die Nachfolgefassung noch DIS ist.
- Contextual Inquiry beobachtet Arbeit im realen Kontext statt nur retrospektiver Selbstauskunft.
- Design Science (Hevner et al. 2004) behandelt Bauen und Anwenden eines Artefakts als Teil des Erkenntnisprozesses.

**Histo-Orla-Learning:** Der Bootstrap-Paradox wird nicht durch noch mehr Vorabmodellierung gelöst, sondern durch **reversible Artefakte als Experiment**, sofern ihre Erkenntnisfrage und Stop Condition explizit sind.

## D.8 AI / LLM Tooling

- MCP 2026-07-28 standardisiert discoverable Tools mit Input-/Output-Schemas, strukturierten Ergebnissen, Logging und Human-in-the-loop-Empfehlungen. Das ist ein gutes **Interface-Pattern**, nicht automatisch Histo-Orlas interne Architektur.
- MultiAgentBench (ACL 2025) findet in einem Research-Szenario Vorteile bestimmter Multi-Agent-Topologien.
- Ein 2026er Preprint zeigt dagegen unter kontrolliert gleichem Reasoning-Token-Budget Vorteile von Single-Agent-Setups bei Multi-Hop Reasoning.
- Eine Nature-Human-Behaviour-Metaanalyse (2024; 106 Experimente, 370 Effektgrößen) zeigt, dass Human+AI im Mittel nicht automatisch das bessere Einzelsystem schlägt; Nutzen hängt stark von Aufgabenteilung und Task-Typ ab.

**Histo-Orla-Learning:** „Multi-Agent“ und „Single-Agent“ sind **zu testende Orchestrierungsvarianten**, keine Produktanforderung. Für den privaten aktuellen Scope ist ein einzelner Assistent mit typisierten Tools + deterministischem Core zunächst der einfachere Falsifikationsstartpunkt.

---

# E – Related Work Matrix

| System / Standard | Eigentliche Arbeit / canonical state | Provenance / Query / Views | Semantik / Extensibility | Local/private / Burden | Transfer zu Histo-Orla | Non-Fit |
|---|---|---|---|---|---|---|
| **Zotero** | Bibliographie, Notes, Attachments; lokale SQLite-Datenbank | Suche/API; Attachment-Metadaten | Bibliographische Semantik, Plugins/API | sehr guter Local Fit; linked files brauchen externe Availability | bibliographisches SSOT + Local API Adapter | kein historischer Research State, keine Method Authority |
| **Tropy** | Forschungsfotos + Metadata + Notes/Transcription | Suche, Templates; JSON-LD/CSV/Omeka Export | flexible Source-photo-Metadaten | Desktop/local; geringer bis mittlerer Burden | Archival-photo Workspace / Annotation Adapter | ausdrücklich kein vollständiger Schreib-/Synthese-/Citation-Workflow |
| **OpenRefine** | tabellarische Datenbereinigung / Reconciliation | Kandidatenranking + Human Review | externe Identifier Spaces; iterative | lokal; gering/mittel | Identity Candidate Resolution als wiederverwendbares Pattern/Tool | kein Forschungs-SSOT; Typen kommen vom Service |
| **Recogito/Pelagios** | Text-/Bild-/Tabellenannotation + Gazetteer Linking | Annotation, Map, Export | Place/Person/Event-Annotation | webzentriert; Kollaboration/Open Data | Findspot-/Place-Annotation-Patterns | nicht der private Gesamtworkspace; Upload-/Platform-Layer |
| **WHG** | historisches Gazetteer / Attestation Model | source-backed Attestations, Certainty, Timespan | starke Place-/Attestation-Semantik | Plattformbetrieb | gutes Beispiel für provenance-aware historische Aussagen | nicht universell auf alle Histo-Domänen übertragbar |
| **Wikibase** | Knowledge Base aus Entities/Statements | Qualifier, References, Ranks, Query | generisches Property-Statement-Modell | eigener Betrieb möglich, aber erheblicher Burden | Statement-/Qualifier-/Reference-Lernmuster | zwingt globales Entity/Property-Modell; hohe Modellpflege |
| **Omeka S** | Sammlungen/Publikation | REST API, JSON-LD/RDF, Sites | Resource classes/vocabularies | Self-hosting möglich | Publishing/Exhibition Adapter | kein primärer Research Workbench / method-aware assistant |
| **nodegoat** | relationale diachrone/spatiale Humanities-Forschung | integrierte Query/Visualisierung | frei definierbare Object Models; ChronoJSON | hosted/self-hosted, mittlerer Burden | starker Vergleich für historische Space/Time Views | object/network model kann Histo-Semantik vorschnell härten |
| **Heurist** | flexible Humanities DB | Analyse/Visualisierung/Export | Strukturen iterativ änderbar | serverbasiert; mittel | Alternative zu Custom-DB bei stark strukturierten Cases | würde ohne Migration leicht zweite Wahrheit |
| **ResearchSpace** | Cultural-Heritage-Knowledge-Graph | semantic patterns/graph views | CIDOC CRM / ontology centric | hoher Semantic-/Ops-Burden | Vergleich für komplexe provenance-rich Semantik | starke ontologische Grundentscheidung zu früh |
| **Arches** | enterprise cultural heritage management | Suche/Maps/Workflows | konfigurierbare Heritage-Models | enterprise-level | möglicher Plattform-Archetyp B | für privaten Lean-Scope voraussichtlich überdimensioniert |
| **TEI P5** | digitale Textrepräsentation/Edition | strukturierte Text-/Apparatdarstellung | modular, textwissenschaftlich | dateibasiert, robust | Import/Export für geeignete Editionen | kein universeller Research State |
| **IIIF + Web Annotation** | interoperable Präsentation + präzise Annotation Targets | Canvas/Annotation/Selector | mediennah, standardisiert | Adapter-basiert | Findspot-/Image-/Text-Segment Interop | nur dort passend, wo Repräsentation/Provider es unterstützt |
| **RiC-O** | archivische Records-in-Contexts-Repräsentation | RDF/SPARQL/Inferenz möglich | archivfachliche OWL-Ontologie | Semantik-/Graph-Burden | Archival-description Adapter/Export | keine allgemeine historische Ontologie |
| **W3C PROV** | domänenneutrale Provenienz | Entity/Activity/Agent, Derivation/Attribution | bewusst extensibel | leicht als Export/Mapping | provenance vocabulary / export mapping | zu abstrakt für Source Identity allein |
| **RO-Crate 1.3** | Research Object Packaging | JSON-LD Manifest | Profile erweiterbar | sehr guter Export/Preservation Fit | portable Snapshots/Handoffs | kein interaktiver Workspace/Truth Store |
| **DataLad/git-annex** | versionierte Forschungsdaten + große Bytes | Git-History, command provenance, rerun | datei-/datasetzentriert | lokal/offline stark; Tooling-Burden mittel | große Derivate/Bytes + reproducible transforms | historische Semantik/UX nicht gelöst |
| **DVC** | Daten/ML-Pipelines | Git-nahe DAGs, repro | pipelineorientiert | lokal + remote; mittel | Pattern für reproduzierbare deterministische Processing Steps | Interpretation ≠ Pipeline; ML-Fokus |
| **eScriptorium/Kraken** | OCR/HTR-Workspace | Segmentation/Transcription | OCR/HTR-spezifisch | eigener Service möglich | Processor Adapter statt Eigenentwicklung | kein Research State |
| **Transkribus** | OCR/HTR Plattform/API | PAGE/ALTO Outputs, model IDs | HTR/OCR-spezifisch | externer Service; Privacy/Rights prüfen | external Processor Capability | Provider-/Rights-Abhängigkeit |
| **Obsidian** | lokale Note-/Backlink-Workspace | Backlinks/Search/Properties/Plugins | leichtgewichtig, Markdown | sehr guter Local UX Fit | möglicher **regenerierbarer** Derived Workspace | darf nicht still SSOT werden; Plugin-Semantik driftet |
| **Logseq** | local-first Outliner/Graph | Backlinks/Queries/PDF/Zotero | File- und neue DB-Graph-Welt | attraktiv, aber DB-Version 2026 noch beta | ebenfalls Derived-Workspace-Kandidat | 2026er DB-Migration/Beta erhöht Stabilitätsrisiko |

**Researcher Inference:** Kein untersuchtes System deckt gleichzeitig Histo-Orlas fuzzy problem framing, domain-owned method truth, source-instance-findspot fidelity, research-state restartability und owner-lesbare Synthese ab. Die externe Landschaft spricht daher stärker für **reuse + composition + thin integrity layer** als für eine vollständige Plattformübernahme.

---

# F – Transdisciplinary Technical Interfaces

## F.1 Die eigentlichen Schnittstellenprobleme

| Interface | Heute sichtbare Friktion | Ziel |
|---|---|---|
| Domain ↔ Data | Fachbegriff droht zu globalem Entity/Relation-Typ zu werden | Domain kann eigene Semantik behalten; gemeinsamer Kern referenziert nur nötige Identität/Provenienz |
| Domain ↔ Software | Methodisches Urteil wird durch Schema/Validator suggeriert | Software operationalisiert geklärte Invarianten, markiert Judgement Boundary |
| Research ↔ Product | Research-Artefakte, Systemlernen und Governance vermischt | sichtbarer Research Output zuerst; Product Learning separat |
| Method ↔ Software | fehlende Method Profiles können Exploration blockieren | Exploration erlaubt, consequential Promotion fail-closed |
| AI ↔ Domain | LLM klingt plausibel und routet implizit | AI ruft explizite Capabilities auf; Evidence/Authority im Contract |
| Project ↔ Engineering | Issue-/Owner-State wird Nutzerworkflow | Project Governance bleibt Hintergrund; Workbench zeigt Research State |

## F.2 Capability statt Agent als Basiseinheit

„Capability“ meint hier **eine fachlich/technisch abgegrenzte Leistung**, nicht zwingend Service, Agent, Prompt oder Plugin.

Mögliche Realisierungen:

- Python function / package API;
- CLI;
- lokaler Service/API;
- MCP-/Tool Contract;
- bestehendes App-/Provider-API;
- GitHub Action nur für deterministische Automation;
- Resolver;
- Context Compiler;
- read-only Derived View;
- Schema/Validator;
- externer Processor Adapter.

## F.3 Minimaler Capability Contract

Jede neue Capability sollte nur so weit formalisiert werden, wie reale Ausführung es braucht:

```text
identity / version
purpose / user pain
inputs
required evidence / context
outputs
side effects
canonical mutation? yes/no
authority class
domain / method constraints
deterministic | procedural | judgement-support
failure / unresolved semantics
provenance emitted
idempotence / retry behavior
human approval boundary
provider/tool adapter
tests / acceptance
```

MCP liefert 2026 dafür ein aktuelles externes Pattern mit Tool Discovery, JSON-Schema-Inputs/Outputs, Structured Content, Logging und Human-in-the-loop. Histo-Orla muss dafür **nicht** MCP-intern werden; MCP ist eine mögliche Adaptergrenze.

## F.4 Kandidaten – nur aus beobachteter Friktion

**Zuerst sinnvoll zu prüfen:**

- `context.compile` – aktuelles Research Goal, belastbare Findings, unresolved, nächste Evidence Demands, relevante Method Guards;
- `source.resolve` – Source Identity ↔ bibliographischer Eintrag ↔ Representation;
- `instance.resolve` / `bytes.resolve` – konkrete verfügbare Instanz/Bytes;
- `source.inspect` – strukturierter Inspektionsnachweis;
- `findspot.locate` – reproduzierbare Fundstelle/Mapping;
- `search.exact_variant` – auditable lexical/variant baseline;
- `identity.reconcile` – Alias/Kandidaten/Human Review;
- `evidence.demand` – method-aware nächste diskriminierende Evidenz;
- `view.derive_research` – synthesis/Befundkomplex/unresolved/backlinks;
- `trace.provenance` – Ableitung/Tool-/Version-/Input-Spur;
- `transition.validate` – Promotion/Mutation nur an geklärten Grenzen;
- `resume.compile` – fresh-context restart packet.

**Später nur bei Bedarf:** OCR/HTR, GIS, semantic retrieval, graph projection, external publication export.

---

# G – Git / State / Workspace Options

## G.1 Rollen statt Monolith

| Rolle | Geeigneter Owner / Mechanismus | Warum |
|---|---|---|
| bibliographisches SSOT | Zotero | bereits spezialisiertes Tool, Local API |
| Source Bytes / große Dateien | aktuelle OneDrive-/File-Grenze; ggf. später DataLad/git-annex prüfen | Git selbst ungeeignet für große Binärbestände |
| kleiner kuratierter Research State | Git-versionierte strukturierte/textuelle Artefakte | Diffs, Review, Rollback, Snapshots, Branching |
| Change Control / Promotion | GitHub PR + Checks | Mutation sichtbar und reviewbar |
| interaktive Query / Search / Backlinks | **regenerierbarer lokaler Read Model** | Git/Markdown ist hierfür schwach |
| Research Workspace | abgeleitete Workbench/View | Research-output-first, progressive disclosure |
| Processor outputs | Derivative + Provenance + External Tool Adapter | OCR/HTR/GIS nicht Eigenbau |
| Export / Handoff package | ggf. RO-Crate/PROV Mapping | portable, standardisierte Grenze |

## G.2 Architekturvarianten

### 1. Git-only canonical structured state

**Vorteil:** minimaler Stack, maximale Transparenz.  
**Risiko:** Ad-hoc-Query, inverse Navigation, Fulltext, Cross-Case Views und UX bleiben Skript-/Markdown-lastig.

### 2. Git + generated local SQLite/FTS read model

**Vorteil:** vollständig lösch-/regenerierbar; FTS5 unterstützt Fulltext, Prefix/Phrase/NEAR/Boolean; SQLite kann zusätzliche strukturierte/JSON-/RTree-Queries lokal anbieten.  
**Risiko:** Cache/Index kann zur zweiten Wahrheit werden, wenn Writeback erlaubt oder Rebuild nicht deterministisch ist.

**Recommendation als Architecture Probe:** zunächst read-only, rebuild-from-canonical, keine stillen Edits, explizite Source Pointer.

### 3. Git + RDF-/Graph-Projektion

**Vorteil:** starke relationale/semantic Queries.  
**Risiko:** erheblicher Modeling-/Ops-Burden und hohe Gefahr, Projection in canonical ontology zu verwandeln. Erst bei konkreten Query-Pains.

### 4. Git + Dokument-/Columnar-Index

Geringere Semantik als Graph; sinnvoll bei sehr großen tabellarischen/analytischen Datenmengen. Aktuell kein nachgewiesener Trigger.

### 5. Git + DataLad/git-annex/DVC-artige Referenzen

Stark für große Dateien, deterministische Processing-/Dataset-Provenienz. Nur einführen, wenn Byte-/Derivative-Scale oder reproduzierbare Pipelines den aktuellen Mechanismus tatsächlich überfordern.

### 6. Git-backed provenance + externer Runtime Store

Erlaubt leistungsfähige Runtime, erhöht aber Synchronisations-/Recovery-/Second-Truth-Risiko. Kein Startpunkt ohne gemessenen Bedarf.

## G.3 GitHub: was behalten, was entkoppeln

**Behalten:**

- PR als kontrollierte consequential Mutation;
- Diffs/Review/Rollback;
- CI für deterministische Invarianten;
- Issues als Work Owner / durable coordination;
- kleine machine-readable records und human-readable Research-Artefakte.

**Entkoppeln:**

- nicht jede Research-Interaktion braucht Issue/PR;
- Branch/PR ist **Promotion Boundary**, nicht primäre Research UX;
- abgeleitete Views sollen Governance nicht duplizieren;
- Experiment-/Candidate-State kann lokal oder auf begrenztem Branch leben, solange er nicht als kanonische Wahrheit ausgegeben wird.

## G.4 Hypothesenprüfung H1–H12

| Hypothese | Supporting Evidence | Counterevidence / Falsifier | Confidence / Folge wenn falsch |
|---|---|---|---|
| **H1 Interface/Orchestration > Ontology** | #64, Owner-Feedback, #116, #117; Mixed Initiative/Boundary Objects | integrierter Slice scheitert wiederholt an nicht repräsentierbarer Cross-Case-Semantik | **hoch**; wenn falsch: gezielte Model-Lücke erforschen |
| **H2 Owner als Semantic Compiler** | dokumentierte manuelle Chat-/Tool-/Repo-Handoffs; Korrekturschleifen | instrumentierter Task zeigt Orchestration nur kleinen Pain-Anteil | **hoch**, aber Baseline fehlt |
| **H3 kleiner Evidence/Identity Core** | #117; Source Identity; Boundary Objects | #47 braucht wiederholt identische domainübergreifende Assertion-Semantik | **mittel-hoch** |
| **H4 Git eher Change-Control als Query Runtime** | aktuelle inverse-navigation Pain; DataLad/DVC als Vergleich | Git-only + generierte einfache Sichten genügt Owner vollständig | **hoch** |
| **H5 regenerierbarer lokaler Read Model** | Query/UX-Pain + SQLite/FTS-Eignung | Rebuild/Fidelity/Owner-Nutzen unzureichend | **mittel-hoch**, experimentell |
| **H6 Derived Views für Perspektivwechsel** | #113/#117/#55; Provenance/Sensemaking | Perspektive enthält neue kuratierte wissenschaftliche Aussage | **hoch**, aber nicht jede Synthese ist derivierbar |
| **H7 Question/Work Context eigener State, kein Universalobjekt** | Restart Pain; #117 partial support | existing Issue/branch/context reicht im realen Restart vollständig | **mittel** |
| **H8 Single Assistant + typed tools zuerst** | geringere Koordination, MCP Pattern; equal-budget 2026 Preprint | matched Histo task zeigt Multi-Agent klar bessere Qualität bei gleicher Owner-Last | **mittel-hoch für aktuellen Scope**, nicht universell |
| **H9 UX: Question→Synthesis→Befunde→unresolved→Provenance** | #55/#64, Sensemaking | contextual-use test zeigt source-first Navigation besser | **mittel-hoch**, UX-Hypothese |
| **H10 Workbench Slice > weitere Meta-Dokumente** | #64/#92/Owner feedback; Design Science | Slice deckt fundamentale Semantiklücke auf | **hoch** |
| **H11 #47 heterogener Gegenfall informativer** | deutlich andere Domänen/Quellen/Space-Time-Logik | #47 methodisch so unreif, dass Architecture Signal nicht trennbar ist | **hoch**, mit Confound-Risiko |
| **H12 Requirements decken Needs weitgehend** | accepted Baseline/Extensions + Owner feedback sagt Delivery-Gap | neuer wiederholter Need lässt sich nicht sauber unter accepted Requirements fassen | **hoch** |

---

# H – Solution Archetypes

## H.1 Archetyp A – Git-backed Research Kernel + Generated Local Read Model

**Form:** kleine canonical records in Git; Zotero/Bytes über Adapter; lokaler rebuildable Query-/FTS-/Backlink-Layer; Research View abgeleitet.

**Stärken:** sehr guter Fit zu Restartability, local/private, Reversibilität, Git-Provenienz, kein sofortiger großer State-Migrationszwang.  
**Schwächen:** eigener Workbench-/Projection-Code; Rebuild-/Consistency-Tests nötig; Gefahr, Read Model zur zweiten Wahrheit zu machen.  
**Wissenschaftlicher Fit:** gut, solange Domain Semantics nicht in den Index „hochgezogen“ werden.  
**Migration:** inkrementell aus aktuellem State möglich.

## H.2 Archetyp B – Existing Research Platform + Histo-Orla Thin Integrity Layer

**Form:** nodegoat, Heurist, ResearchSpace, Arches oder ähnliches übernimmt Workspace/Views/Data Management; Histo-Orla behält Source Identity, Method Guards, Provenance und Assistenz.

**Stärken:** weniger eigene UI-/Query-Entwicklung; erprobte DH-Funktionen.  
**Schwächen:** starke Plattform-/Datenmodell-Prägung, Migration, Betriebsburden, Second-Truth-/Lock-in-Risiko.  
**Wissenschaftlicher Fit:** je Plattform sehr unterschiedlich; kein Kandidat deckt aktuellen Scope ohne erhebliche Anpassung.  
**Wann sinnvoll:** wenn ein heterogener Pilot klar zeigt, dass eine vorhandene Plattform 70–80 % des realen Workflows ohne epistemischen Verlust trägt. Diese Schwelle ist **keine akzeptierte Zielmetrik**, nur ein Entscheidungsheuristik-Beispiel; vor Nutzung wäre ein konkreter Benchmark nötig.

## H.3 Archetyp C – Capability/Skill Bus around Current Canonical State

**Form:** keine große State-Migration; schmale typed capabilities für Context, Resolve, Search, Identity, Evidence, View, Transition.

**Stärken:** geringste Migration; adressiert unmittelbar Owner-Orchestration; Provider-/Tool-Wechsel möglich.  
**Schwächen:** ohne integrierte Query-/Workspace-Sicht bleibt die Bedienung möglicherweise weiterhin chat-/CLI-zentriert.  
**Risiko:** „Capability Bus“ darf nicht zu neuem Framework/Service-Mesh werden.

## H.4 Archetyp D – Staged Hybrid C → A

**Form:** zuerst Capabilities um aktuellen State; gleichzeitig **ein** regenerierbarer lokaler Read-Model-Probe; nur bei realem Nutzen konsolidieren.

**Recommendation:** Dies ist aktuell die kleinste plausible Zielrichtung, **nicht** weil sie technisch elegant ist, sondern weil sie:

- bestehende accepted Requirements respektiert;
- keine globale Ontologie benötigt;
- Owner-Orchestration direkt adressiert;
- Git/Zotero/OneDrive-Rollen behält;
- vollständigen Rollback erlaubt;
- #47 als echten Falsifikationsfall nutzen kann;
- aus Experiment C allein wieder zurückgebaut werden kann, falls der Read Model keinen Value liefert.

---

# I – Tailored Recommendation

## I.1 Kleinste tragfähige sozio-technische Zielstruktur

```text
Owner question
  ↓
Context / competence / evidence-demand compilation
  ↓
typed capabilities
  ├─ Zotero adapter
  ├─ bytes/instance resolver
  ├─ inspect/findspot
  ├─ exact+variant search
  ├─ identity reconciliation
  ├─ OCR/HTR/GIS processor adapters when needed
  └─ provenance/transition guards
  ↓
existing canonical research state in Git
  ↓
rebuildable local read/query projection
  ↓
Research Workbench view
  Question / current synthesis
  → Befundkomplexe
  → unresolved / next evidence
  → source/findspot/provenance drill-down
  ↓
explicit consequential mutation / promotion via Git/PR
```

## I.2 Was bleibt

- #42 accepted Requirements;
- #45 Research Quality;
- #50 Source-/Research-State-Boundaries;
- #60 Domain Method Truth;
- #63 Value/Decision/Delivery trace where materially needed;
- Zotero as bibliographic SSOT;
- aktuelle Byte-/File-Grenze;
- Git/GitHub as canonical change-control;
- `unresolved` and domain-owned interpretation.

## I.3 Was verschwinden oder in den Hintergrund treten sollte

- manuelles Zusammenstellen desselben Contexts über mehrere Markdown-Dateien;
- Owner als Resolver zwischen Source IDs, Aliases, Zotero, Files und Findings;
- manuelle inverse Navigation Source → all Findings/Questions;
- Meta-Erklärungen im primären Research Handoff;
- turnweise Persistenz von Discovery-Nuancen;
- GitHub Issue-/PR-Topologie als Benutzeroberfläche.

## I.4 Was automatisch generiert werden sollte

- fresh-context Resume Packet;
- Source-/Finding-/Question-Backlinks;
- Alias-/Identity-Candidate-Liste;
- „current synthesis / unresolved / next evidence“ Research View;
- Method-/Evidence-relevanter Context;
- Coverage-/Availability-Hinweise;
- mechanische Provenance für Tool-Aufrufe und Derivate;
- technische Audit-/Trace-Sichten, soweit sie aus kanonischen Records ableitbar sind.

## I.5 Welche neue Capability wirklich fehlt

Nicht ein universeller Agent, sondern die **Komposition** der bereits implizit vorhandenen Fähigkeiten zu einem durchgehenden Research Loop. Der erste fehlende Baustein ist daher ein kleiner **Context/Research View + Resolver/Identity/Exact-Search Capability Chain**, nicht ein neues epistemisches Universalmodell.

## I.6 Was ausdrücklich noch nicht nötig ist

- Knowledge Graph / RDF als interner Pflichtkern;
- Property Graph;
- universelle Entity-/Relation-/Event-/Observation-/Temporal-Taxonomie;
- Multi-Agent-Orchestrator;
- allgemeine Workflow Engine;
- RAG/Embeddings als Baseline;
- Event Sourcing nur wegen Historie;
- neue Owner-/Issue-Schicht;
- neue Plattformmigration;
- Question als großes Universal-Domain-Object.

---

# J – Decisive Experiments & Research-Value-Metriken

## J.1 Experiment E1 – #47 End-to-End Research Workbench Thin Slice

**Hypothesis:** H1/H2/H9/H10/H11/H12.  
**Real owner task:** enger Ausschnitt aus #47, z. B. frühester belastbarer Nachweis eines konkreten Teich-/Fischerei-/Mühlen-/Hutungszusammenhangs über zwei unterschiedliche Quellentypen, inklusive räumlicher und rechtlicher Kontextgrenze.  
**Real heterogeneous evidence:** Karte/Riss oder GIS-naher Befund + schriftliche Rechts-/Rechnungs-/Archivquelle; moderne Hydrologie nur als Hypothesen-/Routing-Evidence.  
**Minimal implementation:** Context Compiler, Source/Instance Resolver, exact/variant search, Findspot/Excerpt, Research View, Restart Packet.  
**Reuse vs custom:** Zotero/API, vorhandene Source Identity/State, ggf. Tropy/IIIF/GIS; custom nur dünne glue capabilities + derived view.  
**Expected benefit:** Owner fragt fachlich; System trägt Routing, Source Identity, Kontext, unresolved und Drill-down.  
**Measured owner work removed:** manuelle Handoffs, Copy/Paste, ID-Reconciliation, Context-Aufbau, Toolwechsel.  
**Scientific acceptance boundary:** historische Synthese bleibt methodisch reviewbar; hydrologische Plausibilität ≠ historischer Beleg.  
**Failure:** Owner muss weiterhin Meta-State orchestrieren; wichtige Ungewissheit verschwindet; View kann Source/Findspot nicht verlustfrei öffnen.  
**Rollback:** Capabilities/Read Model löschen; canonical state bleibt unverändert.  
**Persistence:** Research Output unter #47; System Learning separat unter #64/#48.  
**Stop condition:** nach einem vollständigen realen Slice bewerten; keine weitere Abstraktion vor Owner-Feedback.

## J.2 Experiment E2 – Alias + Search + Derived View gegen stärkere Shared-State-Infrastruktur

**Hypothesis:** H3/H4/H6.  
**Task:** bekannte Duplicate-/Reuse-Pains wie `ARS-009` ↔ `SRC-LIT-0001` und inverse Source→Finding/Question-Navigation.  
**Minimal:** Alias mapping, exact/variant search, generated backlinks, keine globale Entity Registry.  
**Acceptance:** Duplicate wird zuverlässig erkannt/navigiert; keine Claim-/Method-Semantik wird automatisch gemerged.  
**Falsifier:** wiederholte reale Fälle brauchen stabil dieselben reicheren domainübergreifenden Assertions und können mit Alias/Context nicht sicher unterschieden werden.  
**Escalation:** zuerst Reconciliation Service/strong IDs; erst danach prüfen, ob mehr Shared State nötig ist.

## J.3 Experiment E3 – Lösch- und rebuildbarer lokaler Read Model

**Hypothesis:** H4/H5/H9.  
**Task:** schneller Cross-Case-Search, Backlinks, current synthesis, unresolved und Source Drill-down.  
**Minimal:** lokale SQLite-Datei + FTS5 als **Probe**, ausschließlich aus Repo/Zotero/read-only resolver inputs generiert.  
**Acceptance:** DB kann vollständig gelöscht und deterministisch neu aufgebaut werden; keine Information existiert nur dort; Source pointers stimmen; Owner findet Material schneller/verständlicher.  
**Falsifier:** Rebuild braucht manuelle hidden semantics, Drift entsteht oder UX-Gewinn ist gering.  
**Rollback:** DB/Builder entfernen, kein Canonical-State-Migrationsaufwand.

## J.4 Experiment E4 – Typed Capability Chain gegen freie Chat-Orchestrierung

**Hypothesis:** H2/H8/H10.  
**Task:** derselbe kleine Researchauftrag einmal mit klaren Capabilities `context → resolve → inspect/search → findspot → view → transition`, gemessen gegen die aktuelle manuelle Vorgehensweise.  
**Acceptance:** weniger Owner-Interventionen und Handoffs bei gleicher oder besserer wissenschaftlicher Nachvollziehbarkeit.  
**Falsifier:** Capability Contracts erhöhen Friktion oder schränken fachliche Exploration unzulässig ein.  
**Multi-Agent-Gegenprobe:** nur wenn ein konkreter Step nachweisbar von paralleler Spezialistenarbeit profitiert; dann matched comparison unter vergleichbarer Tool-/Compute-/Owner-Last.

## J.5 Baseline / Metriken

### Bereits numerisch belegbar

- #108–#116: 9 Concept/Correction-PRs in 16:26:01;
- #112–#116: 5 PRs in 40:05;
- #110→#111 correction latency: 8:52;
- explizit repository-visible Correction/Self-Audit ≥ 3;
- exakter Owner-Correction-Count: **unresolved**.

### Noch nicht belastbar gemessen – ab E1 automatisch erfassen

- Time to First Source-Bearing Result;
- Time to Auditable Synthesis;
- Owner Correction Count pro realem Research Task;
- manuelle Context-/Tool-/Repo-Handoffs;
- Copy/Paste-/Reconciliation-Schritte;
- Duplicate Source/Entity identities;
- Anteil mechanischer Owner-Arbeit;
- Fresh-Context Restart Success;
- Provenance Completeness;
- Erhalt von `unresolved`;
- Search→Findspot→Source Roundtrip;
- neue Meta-Artefakte pro realem Research Output;
- Verhältnis evidence-bearing work zu Governance-/Meta-Arbeit;
- Owner perceived orchestration burden;
- wissenschaftliche Overclaims, die Guards verhindern;
- neue Friktion durch Automation.

**Keine Zielwerte werden vor Baseline erfunden.** Wo möglich, sollen Capability-/Tool-Aufrufe und Git-Timestamps die Metrik automatisch erzeugen; maximal eine kurze Owner-Nutzwertfrage nach dem Task, keine neue Formularkette.

---

# K – Entwicklungsweg in drei Wellen

## Welle 1 – Remove orchestration pain

1. keinen neuen globalen State erfinden;
2. E2 (Alias/Search/Backlinks) als kleinste Pain-Probe;
3. minimalen Context/Resume Compiler auf vorhandenen kanonischen Artefakten;
4. E3 rebuildable local read model als Architecture Probe;
5. Research View auf #55-Minimumspfad ausrichten;
6. Baseline-Metrik erfassen.

**Exit:** Ein echter Research Task kann ohne manuelles Zusammensuchen von Repo-/Tool-Kontext begonnen, unterbrochen und wieder aufgenommen werden.

## Welle 2 – Prove heterogeneous reuse

1. E1 auf #47;
2. mind. zwei unterschiedliche Evidence-/Methodenpfade;
3. Tooling als realer Arbeitsplatz testen (Zotero + Source Bytes + ggf. Tropy/OCR/GIS);
4. prüfen, welche Capabilities wirklich wiederverwendet werden;
5. System Learning strikt getrennt vom historischen Research Output.

**Exit:** gleiche Capability-Kette trägt einen materiell andersartigen Fall, ohne Domain-Semantik zu flatten.

## Welle 3 – Consolidate only proven abstractions

1. nur wiederholt genutzte Utilities/Contracts in gemeinsamen Core ziehen;
2. Shared State nur dort erweitern, wo E1/E2 einen echten Falsifier geliefert haben;
3. Plattform-/Graph-/semantic-search-Optionen nur gegen gemessenen Pain;
4. ggf. RO-Crate/PROV/IIIF/TEI als Export-/Interop-Grenzen;
5. Owner-Workflow-Acceptance gegen Baseline.

**Exit:** weniger Owner-Orchestrierung und bessere Restartability sind real gemessen, nicht nur architektonisch behauptet.

---

# L – Stop / Kill List

## Jetzt stoppen / nicht bauen

- weitere globale Wissensraum-/Achsen-/Relation-/Temporal-Taxonomie ohne Domain-SOTA + heterogenen Consumer;
- Universal Observation/Relation/Event Spine;
- Knowledge Graph als Default;
- neue RDF-/Graph-/Vector-Infrastruktur ohne konkreten Query-Falsifier;
- Multi-Agent Framework ohne matched real-task evidence;
- RAG/Embeddings vor einem nachgewiesenen Recall-/Precision-Problem der exact/variant baseline;
- Workflow-/Policy Engine;
- Event Sourcing als Selbstzweck;
- neue Governance-Markdown-Schichten, die keine Capability/Guard/View freischalten;
- neue Owner-/Issue-Topologie für semantische Nuancen;
- perfektionieren von #55 ohne reale Friktion;
- manuelle Reports, die vollständig ableitbar wären.

## Kill Conditions

- **Local Read Model killen**, wenn Rebuild nicht vollständig ist oder Owner-Nutzen nicht sichtbar wird.
- **Capability Contract vereinfachen**, wenn die Contract-Pflege mehr Owner-/Dev-Arbeit erzeugt als die Capability spart.
- **Shared State Expansion verwerfen**, wenn Alias/Search/View die realen Cross-Case-Probleme ausreichend lösen.
- **Single-Agent-Annahme verwerfen**, wenn ein matched realer Histo-Orla-Task mit Multi-Agent signifikant bessere wissenschaftliche Arbeit bei nicht höherer Owner-Orchestration liefert.
- **Existing-platform-Archetyp verwerfen**, wenn Migration/semantischer Lock-in den vermiedenen Custom-Aufwand übersteigt.

---

# M – Anti-Loop Operating Rules

Diese Regeln sollen **kein neues Governance-System** werden; sie sind ein kurzes Entscheidungsfilter.

1. **Owner signal defaults to User Research.** Es wird nicht automatisch Requirement, Ontologie oder Architektur.
2. **Map before invent.** Zuerst bestehende G/N/P + accepted Requirements prüfen. Ist der Need abgedeckt, kein Requirement-Delta.
3. **Semantic claim → Domain/SOTA + real case.** Jede neue Taxonomie, die historische Bedeutung beeinflusst, braucht Gegenlesart und mindestens einen realen Falsifikationsfall.
4. **Capability only from observed friction.** Vor Custom Capability immer existierendes Tool/Standard/Pattern prüfen.
5. **Escalation ladder:** lokaler Fix → Alias/Reconciliation → exact/variant Search → Derived View → erst dann Shared-State-/Schema-Erweiterung.
6. **Abstraction threshold:** cross-cutting Abstraktion erst nach mindestens zwei materiell unterschiedlichen realen Consumern **oder** einer bereits accepted cross-cutting invariant.
7. **Persist only if handoff would lose something material.** Kein Repo-Commit für jede Denkbewegung.
8. **Spike = question + stop + rollback.** Reversible technische Probe ist erlaubt, wenn sie eine konkrete Unsicherheit diskriminiert; sie besitzt keine automatische Architecture Authority.
9. **Meta-audit stop rule:** Wenn ein weiterer Audit keine neue Evidenz/Entscheidung liefert, muss der nächste Schritt evidence-bearing Research sein.
10. **Every layer must delete owner work.** Vor Aufnahme einer neuen Schicht konkret benennen, welche Owner-Handgriffe/Handoffs sie entfernt. Keine plausible Antwort → nicht hinzufügen.
11. **Unresolved is success when evidence is insufficient.** Fail-closed gilt an Promotion-/Consequence-Boundaries, nicht für Exploration.
12. **Research output first.** Historischer Output und System Learning bleiben getrennte sichtbare Produkte.

---

# N – Bibliography / Evidence Appendix

## N.1 Search Strategy / Boundaries

Durchgeführt wurde eine breite Scoping Search mit gezielten Deep Dives über:

- transdisciplinarity / integration / boundary objects / trading zones / epistemic plurality;
- HCI / mixed initiative / exploratory search / sensemaking / interruption-resumption;
- Digital Humanities infrastructures and standards;
- provenance / research objects / annotation;
- identity reconciliation;
- Research Software Engineering / reproducible workflows / local-first;
- requirements / design science / evolutionary architecture;
- LLM tool contracts / human-AI / single- vs multi-agent;
- offizielle Dokumentation der verglichenen Systeme.

Priorisiert wurden normative Standards, peer-reviewed Literatur, offizielle Projekt-/Systemdokumentation und belastbare OSS-Evidence. Marketingtexte wurden nur zur Beschreibung der jeweiligen Produktintention verwendet, nicht als unabhängige Wirksamkeitsevidenz.

**Grenzen:** Keine vollständige systematische Review mit Datenbankexport/PRISMA-Flow; der Scope ist entscheidungsorientiert. Für eine konkrete Technologieentscheidung (z. B. SQLite vs alternative Indextechnologie, GIS Engine, OCR Engine) wäre ein separater benchmark-basierter Technical Research Step unter #48 erforderlich.

## N.2 Theoretische Kernquellen

1. Star, S. L.; Griesemer, J. R. (1989): *Institutional Ecology, 'Translations' and Boundary Objects*. Social Studies of Science 19(3), 387–420. DOI: 10.1177/030631289019003001.
2. Caccamo, M.; Pittino, D.; Tell, F. (2023): *Boundary objects, knowledge integration, and innovation management: A systematic review*. Technovation 122, 102645. DOI: 10.1016/j.technovation.2022.102645.
3. Lam, D. P. M. et al. (2021): *Conceptualising transdisciplinary integration as a multidimensional interactive process*. Environmental Science & Policy 118, 18–26. DOI: 10.1016/j.envsci.2020.12.005.
4. Collins, H.; Evans, R.; Gorman, M. (2007): *Trading zones and interactional expertise*. Studies in History and Philosophy of Science 38(4), 657–666. DOI: 10.1016/j.shpsa.2007.09.003.
5. Stanford Encyclopedia of Philosophy (rev. 2026-02-22): *Scientific Pluralism*. https://plato.stanford.edu/entries/scientific-pluralism/
6. Horvitz, E. (1999): *Principles of Mixed-Initiative User Interfaces*. CHI '99. DOI: 10.1145/302979.303030.
7. Marchionini, G. (2006): *Exploratory Search: From Finding to Understanding*. Communications of the ACM 49(4), 41–46. DOI: 10.1145/1121949.1121979.
8. Pirolli, P.; Card, S. (2005): *The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis*. ICCM.
9. Parnin, C.; Rugaber, S. (2009): *Resumption Strategies for Interrupted Programming Tasks*. ICPC. DOI: 10.1109/ICPC.2009.5090030.
10. DeLine, R.; Parnin, C. (2010): *Evaluating Cues for Resuming Interrupted Programming Tasks*. CHI. DOI: 10.1145/1753326.1753342.
11. Hevner, A. R.; March, S. T.; Park, J.; Ram, S. (2004): *Design Science in Information Systems Research*. MIS Quarterly 28(1). DOI: 10.2307/25148625.
12. Barker, M. et al. (2022): *Introducing the FAIR Principles for research software*. Scientific Data 9, 622. DOI: 10.1038/s41597-022-01710-x.
13. Kleppmann, M. et al. (2019): *Local-first software: You own your data, in spite of the cloud*. Ink & Switch. https://www.inkandswitch.com/essay/local-first/
14. ISO/IEC/IEEE 29148:2018: *Systems and software engineering — Life cycle processes — Requirements engineering*. Im September 2026 weiterhin current; Nachfolgefassung noch DIS.

## N.3 Standards / Scholarly Infrastructure

15. W3C: *PROV-O: The PROV Ontology*. Recommendation. https://www.w3.org/TR/prov-o/
16. W3C: *Web Annotation Data Model*. Recommendation. https://www.w3.org/TR/annotation-model/
17. RO-Crate 1.3 (2026-06-22): Recommendation. https://www.researchobject.org/ro-crate/specification/1.3/
18. TEI Consortium: *TEI P5 Guidelines*, Version 4.12.0, 2026-07-28. https://www.tei-c.org/release/doc/tei-p5-doc/en/html/
19. ICA EGAD: *Records in Contexts Ontology (RiC-O) 1.1*, 2025-05-22. https://www.ica.org/standards/RiC/RiC-O_1-1.html
20. IIIF Consortium: Presentation/Image APIs, aktuelle offizielle Spezifikationen unter https://iiif.io/api/

## N.4 Related Work / Tool Evidence

21. Zotero Local API: https://www.zotero.org/support/dev/web_api/v3/local_api  
22. Zotero Attachments / linked vs stored files: https://www.zotero.org/support/attaching_files  
23. Tropy Documentation: https://docs.tropy.org/  
24. Tropy Export: https://docs.tropy.org/other-features/export  
25. OpenRefine Reconciliation: https://openrefine.org/docs/manual/reconciling  
26. OpenRefine Reconciliation API: https://openrefine.org/docs/technical-reference/reconciliation-api  
27. World Historical Gazetteer v4 Concepts / Attestations: https://docs.whgazetteer.org/content/v4/user-guide/getting-started/concepts.html  
28. Wikibase Data Model: https://www.mediawiki.org/wiki/Wikibase/DataModel  
29. Omeka S REST API: https://omeka.org/s/docs/developer/api/rest_api/  
30. nodegoat About / Methodology: https://nodegoat.net/about  
31. Heurist Network: https://www.heuristnetwork.org/  
32. ResearchSpace Knowledge Graphs and Patterns: https://researchspace.org/knowledge-graph-and-patterns/  
33. Arches Project Documentation: https://www.archesproject.org/documentation/  
34. Recogito Tutorial: https://recogito.pelagios.org/help/tutorial  
35. eScriptorium Documentation: https://escriptorium.readthedocs.io/en/latest/  
36. Transkribus Processing API: https://transkribus.eu/processing/swagger/  
37. DataLad `run`: https://docs.datalad.org/en/latest/generated/man/datalad-run.html  
38. DVC: https://github.com/treeverse/dvc  
39. SQLite FTS5: https://www.sqlite.org/fts5.html  
40. Obsidian Documentation: https://help.obsidian.md/  
41. Logseq Documentation: https://docs.logseq.com/ ; aktuelle DB-Version 2026 laut Projekt-README noch beta.

## N.5 AI / Tool-Orchestration Evidence

42. Model Context Protocol Specification, Tools, 2026-07-28: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/server/tools.mdx
43. Zhu, K. et al. (2025): *MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents*. ACL 2025. DOI: 10.18653/v1/2025.acl-long.421.
44. Tran, D.; Kiela, D. (2026): *Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets*. arXiv:2604.02460. **Preprint; nicht peer-reviewed.**
45. Vaccaro, M.; Almaatouq, A.; Malone, T. (2024): *When combinations of humans and AI are useful: A systematic review and meta-analysis*. Nature Human Behaviour 8, 2293–2303. DOI: 10.1038/s41562-024-02024-1.

---


---

# O – Operative Umsetzung / Refactoring Blueprint

Dieser Abschnitt operationalisiert die Research-Befunde **innerhalb der bestehenden Owner und Requirements**. Er erzeugt keine neue Authority und keine neue Requirement-Schicht.

## O.1 Grundsatz: maximal operationalisieren, minimal neu erfinden

Die Befunde werden in vier Klassen umgesetzt:

1. **sofort refactoren**, wenn bestehende accepted Requirements und dokumentierter Owner-Pain die Änderung bereits tragen;
2. **generieren/automatisieren**, wenn heute dieselbe Information manuell zusammengesucht oder doppelt gepflegt wird;
3. **als reversiblen Architecture Probe testen**, wenn die Research-Evidence eine Richtung stützt, aber die konkrete technische Struktur noch nicht entschieden ist;
4. **nicht bauen**, wenn weder Requirement noch realer Falsifikationsbefund die zusätzliche Schicht rechtfertigt.

Die operative Leitformel lautet:

```text
Issue / Governance = Ownership + Boundary + durable coordination
Canonical Research Artifacts = research truth / evidence / curated synthesis
Product Runtime = resolve + retrieve + context + view + resume + controlled transition
Operational Support = validate + assurance + repo mutation + CI
Derived Read Model = disposable / rebuildable / read-only
Chat / Skill / UI = replaceable interaction adapter
```

## O.2 Delivery-Refactoring: Vertical Research Slice wird primäre Integrationseinheit

### Heute problematisch

Die vorhandenen technischen Work Owner #49–#57 sind semantisch sinnvoll, können aber praktisch zu seriellen Handoffs führen:

`#49 → #51 → #53 → #55 → #57`.

Wenn jeder Owner zugleich eigene Benutzeroberfläche, eigenen Kontext und eigene Delivery-Zeremonie erzeugt, wird der Research Owner wieder zum Integrator.

### Operative Änderung

**Ein realer Vertical Research Slice wird zur primären Delivery-/Integrationseinheit.**

Ein Slice darf mehrere bestehende Issues/Owner konsumieren, ohne diese zusammenzulegen:

```text
ein Owner-Researchauftrag
→ Source/Bibliography resolution (#49/#50)
→ Instance/Findspot (#51)
→ Exact/Variant Retrieval (#53)
→ Research View (#55)
→ Restartability/Availability (#57)
→ Owner Feedback (#63)
```

Praktische Konsequenz:

- **ein Integrations-Branch / PR pro realem Slice**, nicht automatisch ein PR pro Subsystem;
- bestehende Issues bleiben Scope-/Authority-Owner und erhalten nur kurze Status-/Evidence-Pointer;
- Commit-/Test-/Trace-Referenzen zeigen weiterhin, welcher Teil welchem Owner/Requirement gehört;
- der sichtbare Primäroutput des Slices ist ein **Research Output**, nicht die Issue-/PR-Kette.

Damit werden Issue-Grenzen nicht zu Code- oder UX-Grenzen.

## O.3 Issue-Refactoring: Work Owner bleibt, Forschungsoberfläche verschwindet

Issues bleiben nach `AGENTS.md`:

- Work Owner;
- Scope/Status/Dependencies;
- kurze Synthese;
- offene Punkte;
- nächste Aktion;
- Pointer auf kanonische Artefakte.

Sie werden **nicht**:

- Source Ledger;
- Exzerptregister;
- Research Notebook;
- primäre Navigation durch Findings;
- Benutzeroberfläche für die historische Forschung;
- notwendige manuelle Routingentscheidung des Owners.

Die Product Runtime soll einen Researchauftrag auf den passenden bestehenden Owner/State **auflösen**. Eine automatische Zuordnung darf einen Work Owner vorschlagen oder referenzieren, erzeugt aber keine globale `selected-current`-Selection Authority.

## O.4 Root-/Handoff-Refactoring

Das dokumentierte #64-Owner-Feedback verlangt einen 5-Minuten-Handoff. Daraus folgt ein unmittelbarer Dokumentations-Refactor ohne neue Semantik:

### `AGENTS.md`

**Behalten.** Binding Governance; keine weitere Product-/Research-Prosa hineinziehen.

### `README.md`

Auf **Front Door** reduzieren:

1. Produktzweck;
2. wie Research begonnen wird;
3. aktuelle kanonische Einstiegspunkte;
4. Pointer auf `PROJECT_STATE.md`, Research, Architecture.

Historische CI-Run-Details, Validator-Innereien und lange Assurance-Erklärungen gehören nicht in den primären Nutzer-Einstieg.

### `PROJECT_STATE.md`

Auf tatsächlichen Handoff-Zweck zurückführen:

- Current Work Selection;
- aktive Research Owner / wichtige aktuelle Findings/Unresolved nur als Pointer;
- current technical critical path;
- echte Blocker;
- nächste ausführbare Aktionen;
- Pointer auf Detailartefakte.

Ausführliche historische Run-/Implementationschronologien bleiben in ihren Owner-/Trace-Artefakten.

**Wichtig:** Diese Kürzung ändert keine Authority und keine Requirements; sie entfernt Duplikation.

## O.5 Code-Refactoring: Operational Support und Product Runtime entkoppeln

Der aktuelle `tools/operational/`-Bestand enthält zwei unterschiedliche Verantwortungsarten.

### Bleibt klar Operational Support

- `core.py` – mechanische Loader / Schema-Utilities;
- `mutation.py` – Repo-/Text-Mutationsschutz;
- `enforcement-map.json` – technische Requirement→Enforcement-Projektion;
- Requirements-/Assurance-Validatoren und CI.

Diese Komponenten unterstützen Betrieb/Assurance und sind **nicht** die Forschungsassistenz.

### Product-Capability-Kandidaten

- `context.py` / `context_spec.py` – Context/Resume;
- `audit.py` – Research View;
- #53 Retrieval;
- #49/#50 Resolver;
- #57 Evidence Availability/Resume.

Diese dürfen zunächst dort bleiben, wo sie heute testbar sind. Sie sollen aber **nicht weiter als unabhängige Tools wachsen**.

### Exakter Trigger für eine `src/histo_orla/`-Produktgrenze

Die Product-Code-Grenze wird eingeführt, sobald der erste reale Vertical Slice mindestens zwei der folgenden Runtime-Fähigkeiten über einen gemeinsamen provider-neutralen Research-State-Zugriff nutzt:

- context/resume;
- source/instance resolve;
- exact/variant retrieval;
- research view;
- evidence availability;
- controlled research-state transition.

#53 ist ein wahrscheinlicher Trigger, weil Retrieval eine echte Research-Runtime-Capability ist und mit #55/#57 denselben State lesen muss.

**Nicht Trigger:** Ordnerästhetik, zukünftige Planung oder der Deep-Research-Bericht allein.

### Kandidaten-Topologie nach Eintritt des Triggers

Keine Pflichtstruktur; kleinster sinnvoller Start:

```text
src/histo_orla/
  state.py              # read-only provider-neutral access / IDs / refs
  context.py            # context + resume compilation
  resolve.py            # source/instance/alias resolution
  retrieval.py          # exact/variant/query-log baseline
  views.py              # research/audit views
  availability.py       # research-ready evidence availability
  transitions.py        # research-state transition guard, wenn #54 real wird
  adapters/
    zotero.py
    bytes.py
    documents.py
```

Nur Module mit realem Consumer werden angelegt. Kein leeres Future-Proof-Gerüst.

`tools/operational/*` bleibt anschließend für Repo-/Assurance-/Migration-/CI-Funktionen; dünne Wrapper können Product APIs konsumieren, besitzen aber keine zweite Semantik.

## O.6 Gemeinsamer State-Zugriff vor gemeinsamem Universalmodell

Der erste technische Integrationspunkt soll **kein neues Ontologieschema**, sondern ein kleiner provider-neutraler Read Contract sein.

Er muss vorhandene #50-Rollen lesen/referenzieren können:

```text
Source
Representation
Instance
Derivative
Findspot / Excerpt
Finding
Claim / curated Synthesis
Method Application
Unresolved / Validation
```

Zusätzliche Objektklassen werden nur aufgenommen, wenn ein realer Slice sie benötigt.

Wichtig:

- **curated synthesis** ist wissenschaftlicher State und nicht automatisch derivierbar;
- Backlinks, Auditpfade, Search-Index, Resume-Paket, Coverage und Navigation sind dagegen gute **Derived Views**;
- der technische Reader darf fehlende Semantik als `missing/unresolved` zurückgeben, nicht ergänzen.

## O.7 Read-Model-Experiment: Query Runtime ohne zweiten Truth Store

E3 wird als eigener, vollständig reversibler Probe umgesetzt:

```text
canonical Git/Zotero/provider-neutral refs
        ↓ rebuild
local read model
        ↓
FTS / backlinks / inverse navigation / filters
        ↓
Research View
```

Für den ersten Probe ist SQLite/FTS eine zulässige technische Hypothese, keine Architekturentscheidung.

Harte Guardrails:

- DB wird **nicht** committed;
- DB besitzt **keinen** exklusiven Research State;
- kein fachlicher Writeback über die DB;
- vollständiger Delete→Rebuild-Test;
- CI-/Fixture-Test prüft reproduzierbare IDs/Links;
- jeder Treffer bleibt auf kanonische Source/Instance/Findspot-/Finding-IDs zurückführbar.

Wenn Rebuild hidden/manual semantics benötigt, ist der Probe gescheitert.

## O.8 Research Workbench ohne vorzeitige UI-Plattform

Der erste Workbench muss keine neue Web-App sein.

### v0 ausführbare Product Surface

Ein Chat-/Skill-/CLI-Adapter kann dieselben Product APIs aufrufen und als eine Research-Sicht ausgeben:

```text
Research question
Current curated synthesis
Key evidence complexes / findings
Unresolved / competing explanations
Next discriminating evidence
Available / unavailable evidence
Source / findspot drill-down
Method / validation status
Resume token/context
```

Die Oberfläche soll **Research first** sein. Issue-/Requirement-/Governance-IDs werden nur im Drill-down oder Audit angezeigt.

Erst reale Nutzung entscheidet, ob eine lokale GUI/Web-Workbench zusätzlichen Wert bringt.

## O.9 Capability-Contracts werden ausführbar, nicht zu neuer Dokumentation

Die Capability-Einheit wird aus dem Report in Code-/API-Verträge übersetzt. Minimal pro Capability:

```text
input
output
side effects
canonical mutation? yes/no
authority / consequence boundary
failure / unresolved result
provenance emitted
tests
```

Beispiel:

### `resolve(source_ref)`

- liefert interne Source-/Representation-/Instance-Refs + Provider refs;
- darf Alias-/Candidate-Information liefern;
- darf keine historische Identität fachlich entscheiden;
- erzeugt keinen Finding.

### `retrieve(query, corpus_scope)`

- Exact/Variant Baseline;
- Query/Expansion/Filter/Corpus-Version im Result;
- Treffer referenzieren Findspot/Derivative;
- kein LLM erforderlich;
- kein Hit wird automatisch Finding.

### `derive_view(question/work_context)`

- kombiniert curated Synthesis mit derived Backlinks/Audit/Unresolved;
- keine neue Forschungsaussage;
- fehlende Links sichtbar.

### `resume(work_context)`

- kompiliert erlaubte nächste Aktion, Evidence Availability und Stop/Handoff;
- keine Priority-/Selection Authority.

### `transition(candidate, target_status)`

- prüft formale Promotionsbedingungen;
- historische Richtigkeit bleibt Review-Judgement.

## O.10 Thin AI-/Skill-/MCP-Schicht erst über stabile Capabilities

Der Assistent soll langfristig **nicht** Governance/Methodik im Prompt nachspielen.

Adapter-Prinzip:

```text
natural-language request
→ problem/context interpretation
→ capability discovery/routing
→ typed tool calls
→ deterministic/product results
→ scholarly judgement where required
→ explicit canonical transition only at consequence boundary
```

Ein Skill/MCP-Server/Plugin darf:

- Product Capabilities discoverable machen;
- strukturierte Inputs/Outputs transportieren;
- den Owner von Tool-/Repo-Routing entlasten.

Er darf nicht:

- Requirement-/Method Truth duplizieren;
- eigenes verstecktes Memory als State führen;
- Promotion allein aus LLM-Urteil autorisieren.

## O.11 Research Output und System Learning technisch trennen

Jeder Vertical Slice liefert zwei getrennte Resultate:

### A. Research Output

Kanonischer historischer Inhalt im bestehenden Research Owner:

- Evidence;
- Findings;
- curated Synthesis;
- unresolved;
- next evidence.

### B. Product/System Learning

Separat unter #63/#64/#48:

- welche Owner-Handarbeit entfiel;
- welche Capability fehlte;
- welche Friktion neu entstand;
- welche technische Hypothese falsifiziert wurde;
- ob ein Requirement-/Method-/Architecture-Delta überhaupt nötig ist.

Die Research-Datei wird nicht zum Systemdesign-Protokoll.

## O.12 Metrics ohne neues Telemetriesystem

E1–E4 benötigen eine Baseline, aber kein Analytics-Framework.

Zunächst aus vorhandenen Quellen/kleinen Testrecords ableiten:

- Tool-/Capability Calls;
- manuelle Handoffs;
- Owner Corrections;
- Zeitpunkte Start / first source-bearing result / auditable synthesis;
- unresolved-preservation / roundtrip tests;
- #63 Owner Feedback.

Nur wenn mehrere reale Slices dieselbe Messung benötigen, wird eine kleine machine-readable Evaluation-Projektion eingeführt.

## O.13 CI-/Test-Refactoring

Neue Tests schützen nur objektiv prüfbare Grenzen:

1. derived read model ist vollständig rebuildbar;
2. kein Read-Model-only Research State;
3. Retrieval Hit roundtrips zu Findspot/Source;
4. Alias/Reconciliation verändert keine Claims;
5. Resume Context verliert kein `unresolved`;
6. Adapter-Ausfall wird `unavailable/degraded`, nicht falsche Evidenz;
7. Audit/View erzeugt keine neuen wissenschaftlichen Aussagen;
8. canonical transition bewahrt Vorgänger/History;
9. AI Output kann nicht als Evidence Class promoted werden;
10. Vertical-Slice-Fixture kann ohne alten Chat erneut geöffnet werden.

CI prüft **nicht** historische Richtigkeit oder Owner-Nutzen.

## O.14 Existing-Owner-Mapping: keine neuen Issues nötig

| Refactoring / Capability | bestehender Owner |
|---|---|
| Product Runtime / package boundary / integration | #48 / #59 |
| Source/Instance provider-neutral State | #50 |
| Zotero/Bytes resolver | #49 |
| Document/Findspot | #51 |
| Exact/Variant Retrieval | #53 |
| Research-State Transition | #54 |
| Research/Workbench View | #55 |
| Rights Admission | #56 |
| Availability/Restart | #57 |
| Method constraints | #60 |
| Context/Handoff mechanics – nur bei neuer realer Friktion | #61 |
| formal Requirements Assurance | #62 |
| Owner/Product Feedback | #63 |
| Deep-Research diagnosis / value challenge | #64 |
| integrated roadmap/disposition | #92 |

**Disposition:** Kein neues „Workbench Issue“, kein „Capability Framework Issue“ und kein neuer Meta-Owner, solange diese bestehenden Owner ausreichen.

## O.15 Konkrete Refactoring-Reihenfolge

### R0 – Sofort: Execution Admission vor Implementierung

- PR #118 Review-Evidence dispositionieren;
- Root README/PROJECT_STATE auf Handoff/Front-Door-Funktion entdoppeln;
- keine weitere Expansion von #61/#55 ohne reale Friktion;
- Vertical-Slice-PR statt Subsystem-PR als Delivery-Regel unter #48/#59 anwenden;
- vor jedem Agent-/Implementation-Slice aktuelle Prerequisites, Evidence Availability, Testbarkeit und Execution Environment **deterministisch** prüfen;
- current-stage `unresolved` blockiert; nur echte downstream Dependencies dürfen separat deferred bleiben;
- kein Implementer startet, bevor der abgeleitete Current Context `ready` ist.

### R1 – Retrieval in getrennten Admission-Stufen

1. #53 Exact-/Query-Log-Vertrag zunächst gegen vorhandene synthetische, texttragende provider-neutrale Fixtures implementieren und kalibrieren;
2. für einen **realen** #53-Slice separat einen texttragenden, findspot-gebundenen Retrieval-Input admitten:
   - Source/Representation/Instance geklärt;
   - Bytes/Derivat im aktuellen autorisierten Context tatsächlich verfügbar;
   - Parentage/Version/Fingerprint rekonstruierbar;
   - Findspot-Mapping erhalten;
   - Rights/Processing für die konkrete Operation zulässig;
3. erst danach reales Exact Retrieval gegen #51/#55-Provenienzpfad falsifizieren;
4. historische Varianten anschließend mit fachlich kontrollierter Varianten-Provenienz ergänzen;
5. gemeinsamen provider-neutralen State-Reader nur bei mindestens zwei realen Runtime-Consumern extrahieren;
6. #55 View und #57 Resume/Availability erst dann auf denselben Reader ziehen, wenn diese Wiederverwendung real belegt ist;
7. erst danach `src/histo_orla/`-Trigger neu bewerten.

**Correction evidence 2026-09-20:** Der erste #53-Agent-Calibration-Lauf stoppte korrekt, weil die reale Sachenbacher-Kette zwar Source/Instance/Findspot-Provenienz und eine regenerierbare Audit-Projektion besitzt, aber im aktuellen Repo-/Execution-State keinen admitted texttragenden Retrieval-Korpus. Der frühere Schritt „#53 gegen realen #51/#55-State beginnen“ war daher als Execution-Anweisung zu grob und wird durch die Admission-Stufen oben ersetzt.

### R2 – Heterogener #47-Slice

- explizit owner-ausgewählte kleine #47-Forschungsfrage;
- Source/Resolver + Retrieval + View + Restart in **einem** Slice;
- kein neues allgemeines Schema während der Ausführung;
- Owner-Feedback und Messwerte nach dem Slice.

### R3 – Read Model Probe

- nur wenn R1/R2 Query-/Navigation-Pain bestätigen;
- read-only SQLite/FTS-Probe;
- Delete/Rebuild/Fidelity/Owner-Value messen;
- `adopt | adapt | reject`.

### R4 – Konsolidierung

Nur nach zwei real unterschiedlichen Consumern:

- gemeinsame Product APIs stabilisieren;
- dünnen Chat/Skill/MCP-Adapter davor setzen;
- nur bewährte Module in dauerhafte Product-Code-Struktur ziehen;
- obsolete manuelle Derived Views/Meta-Erklärungen entfernen oder generieren;
- stärkeren Shared State nur bei konkretem Falsifier.

## O.16 Definition of Done für die Operationalisierung dieses Deep Research

Der Bericht gilt operativ als umgesetzt, wenn nicht nur seine Prosa gemerged ist, sondern mindestens:

1. ein Owner stellt eine reale Forschungsfrage ohne manuelles Issue-/Tool-Routing;
2. der aktuelle Work Context wird aus Repo-State komponiert;
3. Source/Instance/Findspot und Exact/Variant Retrieval laufen über denselben provider-neutralen Zugriff;
4. ein Research-first View zeigt curated synthesis, Evidence, unresolved und next evidence;
5. Drill-down führt reproduzierbar zur inspizierten Quelle/Fundstelle;
6. Unterbrechung + fresh restart funktioniert ohne alten Chat;
7. ein heterogener #47-Slice benutzt denselben Runtime-Kern ohne Domain Flattening;
8. technische Derived Layers können vollständig entfernt/rebuilt werden;
9. Research Output und System Learning sind getrennt;
10. gemessene Owner-Orchestrierung sinkt gegenüber der Baseline;
11. keine neue Governance-/Issue-/Framework-Schicht ist nötig, um den Slice zu verstehen;
12. alles, was sich nicht bewährt, wird entfernt oder als Experiment archiviert statt durch weitere Meta-Architektur gerettet.



## O.17 Agentic Execution / Model-Budget Strategy

**Status:** operative Empfehlung unter #48/#59; keine Model-/Provider-Authority und keine neue Requirement-Schicht. Modellnamen/-preise sind zeitgebundene Implementierungsdetails und müssen vor längeren Läufen neu geprüft werden.

### Ziel

Die Agentik soll **keine Needs/Requirements rekonstruieren oder komprimierend neu interpretieren müssen**. Günstigere Modelle sind nur dort vorgesehen, wo Scope, Inputs, Forbidden Loss, Acceptance und Stop/Handoff maschinenlesbar bzw. eindeutig referenziert sind.

### Execution packet je Agent

Jeder materielle Agent-Task erhält aus dem kanonischen Repo mindestens:

```text
WORK OWNER / PRIMARY FUNCTION
BOUNDED OBJECTIVE
EXACT REQUIREMENT REFS
UPSTREAM G/N/P DRIVER REFS
GOVERNANCE / METHOD / SOURCE CONTRACT REFS
SCOPE + EXCLUSIONS
MUST PRESERVE / FORBIDDEN LOSS
INPUT FILES / STATE REFS
ALLOWED MUTATIONS
ACCEPTANCE TESTS / NEGATIVE TESTS
STOP / ESCALATE CONDITIONS
RETURN CONDITION
PERSISTENCE TARGET
```

Wichtig: Requirements werden **referenziert**, nicht für jeden Agenten frei zusammengefasst. Wo komprimierter Context verwendet wird, bleibt er lossless-by-reference auf die kanonischen Quellen rückführbar.

### Consequence tiers

**Tier A — Frontier / high-reasoning required**

- neue oder geänderte Requirements-/Need-Interpretation;
- Architecture- oder Persistenzentscheidungen mit materiellen Trade-offs;
- Domain-/Method-/Evidence-Semantik;
- Cross-cutting Refactor mit möglichem Bedeutungsverlust;
- independent challenge/review eines materiellen PR;
- unklare Failure Modes oder widersprüchliche Constraints.

**Tier B — balanced implementation model**

- bounded Product-/RSE-Implementation;
- Refactoring mit vollständigen Tests und klarer no-loss-Grenze;
- Adapter-/Resolver-/Retrieval-Code gegen bestehenden Contract;
- Test-/Fixture-Erweiterung;
- Derived Views;
- migrationsarme Code-Extraktion mit kompatiblen Wrappers.

**Tier C — cheapest high-volume model**

- mechanische, deterministisch verifizierbare Änderungen;
- Format-/Link-/Index-/Generated-View-Updates;
- Fixture-Varianten aus exaktem Contract;
- klar spezifizierte Testfälle;
- repetitive bounded edits;
- Ausführung/Erklärung bereits deterministischer Checks.

Tier C darf keine neue Semantik, kein Requirement-Delta und keine fachliche Promotion erzeugen.

### Two-key rule für materielle Änderungen

Für materiellen Code-/State-Umbau gilt als empfohlener Default:

```text
strong planner/specification
→ cheaper bounded implementer
→ deterministic tests/CI
→ independent strong reviewer
→ canonical merge/handoff
```

Ein billiger Implementer darf damit umfangreiche Arbeit erledigen, aber nicht gleichzeitig seine eigene semantische Spezifikation und Abnahme erzeugen.

### Aktuelle OpenAI-Modellabbildung (2026-09-20; vor Ausführung neu prüfen)

- **GPT-5.6 Sol, High**: Tier A Default für Planung, Requirements-/Architecture-Grenzen und materielles Review.
- **GPT-5.6 Terra**: Tier B Default und bevorzugtes Preis-/Leistungsmodell für den Großteil bounded Coding/Refactoring.
- **GPT-5.6 Luna**: Tier C für mechanische/high-volume Tasks mit starken Tests; nicht Default für semantische Refactorings.
- **Sol Pro / GPT-6 Pro**: nur bei tatsächlich festgefahrenen oder außergewöhnlich schwierigen Tier-A-Aufgaben; nicht als Standard-Worker.

### Budget-/Limit-Strategie

- große Dauerläufe in kleine repo-persistierte Work Orders schneiden;
- kein Agent ist continuation-critical;
- jeder Slice endet in commit/PR + tests + handoff;
- bei Modell-/Planlimit kann ein neuer Agent vom Repo aus weiterarbeiten;
- teure Modelle nur an Semantik-/Review-Grenzen einsetzen;
- günstige Modelle erhalten minimale, präzise Context Packs statt den gesamten Repo-Verlauf;
- Context Caching / stabile Prefixes nutzen, soweit die Ausführungsumgebung dies unterstützt;
- vor einem längeren Lauf ein kleines Calibration-Set aus repräsentativen Histo-Orla-Tasks gegen Terra/Luna/Sol vergleichen.

### Admission test für ein günstigeres Modell

Ein Modell wird für eine Task-Klasse erst zugelassen, wenn es auf mindestens einem repräsentativen Calibration-Set:

1. keine Requirement-/Authority-Grenze verletzt;
2. alle deterministischen Tests besteht;
3. `unresolved`/Forbidden-Loss-Zustände erhält;
4. keine zusätzliche Owner-Korrektur gegenüber der stärkeren Referenz benötigt;
5. einen fresh-context Handoff korrekt erzeugt.

Bei Failure steigt die Task-Klasse auf ein stärkeres Modell oder der Work Order wird präzisiert; nicht die wissenschaftliche/produktseitige Anforderung wird abgesenkt.

# Schlussfolgerung

**Researcher Inference:** Histo-Orlas bisheriges Ringen ist weniger ein Beleg für ein noch nicht gefundenes „richtiges“ Universalmodell als ein Beleg dafür, dass die **transdisziplinären Übergänge selbst Produktfunktion** sind. Quelle/Instanz/Fundstelle, Domain Method Truth, Identity, Tooling, Research State, Synthese und Restartability sind bereits weitgehend als Anforderungen verstanden; sie werden aber noch nicht als durchgängiger Forschungsarbeitsplatz erlebt.

**Recommendation:** Der nächste Entwicklungsschub soll deshalb nicht „mehr Modell“ produzieren, sondern **weniger Owner-Orchestrierung**. Die kleinste derzeit begründbare Richtung ist:

```text
existing scientific invariants
+ typed, narrow capabilities
+ explicit authority/side-effect boundaries
+ generated local query/read projection
+ research-output-first workbench
+ Git as curated change-control/provenance
+ heterogeneous real-case falsification
```

Der Prüfstein bleibt für jede zusätzliche Schicht:

> **Entfernt sie reale Forschungs- und Orchestrierungsarbeit vom Research Owner – oder fügt sie nur eine weitere Schicht hinzu, die der Owner verstehen und bedienen muss?**

Wenn E1–E4 diese Entlastung nicht zeigen, ist die vorgeschlagene Richtung zu reduzieren oder zu verwerfen – nicht durch weitere Meta-Architektur zu retten.
