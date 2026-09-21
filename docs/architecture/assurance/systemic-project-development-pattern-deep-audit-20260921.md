# Histo-Orla – Systemischer Deep Audit wiederkehrender Projektentwicklungs- und Übersetzungsmuster

**Datum:** 2026-09-21  
**Work Owner:** #64 – Product-/Research-Value gegen Governance-Komplexität  
**Research Quality:** #45  
**Requirements Authority:** ausschließlich #42  
**Technical / Delivery Context:** #48 / #59 / #63 / #92  
**Repo-Baseline:** main @ ff2bc993d959afd594dff2acf772e0e608963f97  
**Status:** independent analysis / research foundation / no solution, requirement, method, selection or architecture authority

---

## 0. Zweck und harte Grenze

Dieser Audit untersucht Histo-Orla als gekoppeltes fachliches, sozio-technisches und softwaretechnisches System.

Er fragt nicht:

- Welche Zielarchitektur soll Histo-Orla bekommen?
- Welche Roadmap ist die richtige?
- Welches Framework, Tool oder Datenmodell soll gewählt werden?
- Welche neue Governance soll eingeführt werden?
- Welche Entwicklungsoption soll priorisiert werden?

Er fragt:

> Welche wiederkehrenden Mechanismen haben dazu geführt, dass bereits klar dokumentierte Nutzerbedürfnisse, Qualitätsziele und Nichtwissens-Situationen wiederholt in zusätzliche Struktur-, Governance-, Koordinations- oder Modellierungsarbeit übersetzt wurden, während der gewünschte operative Forschungsfluss hinterherlief?

Das ist eine **Research Question**, keine vorausgesetzte Diagnose.

Analytische Integration ist zulässig: Befunde dürfen als kompatibel, komplementär, widersprüchlich oder nur partiell passend bewertet werden. Es entsteht daraus **keine normative Lösungssynthese**.

---

# A. Untersuchungsrahmen

## A.1 Führende Perspektiven

Der Audit kombiniert gleichberechtigt:

- historische Forschungs- und Wissensarbeitsdomäne;
- Requirements Engineering;
- Human-Centred Design / HCI;
- CSCW / Coordination Theory;
- transdisziplinäre Wissensintegration;
- Wissenschaftstheorie / Scientific Pluralism;
- Research Software Engineering / Software Evolution;
- Safety / Human Factors / High Reliability;
- AI-assisted Software Engineering;
- Provenance / Research Data Management.

Keine dieser Disziplinen besitzt allein die Problemdefinition.

## A.2 Evidence-Klassen

### Project Evidence

Direkt aus Repository, Issues, PRs, Code, Tests, versionierten Artefakten oder CI.

### Owner Evidence

Dokumentierte Bedürfnisse, Friktionen und Workflow-Erfahrungen des Research Owners. Das ist Product-/Workflow-Evidence, keine historische Evidence.

### External Research Evidence

Peer-reviewed Literatur, Standards, offizielle Spezifikationen oder belastbare empirische Studien.

### Related-System Evidence

Beobachtungen aus realen Software-/Forschungsinfrastrukturen oder Benchmarks.

### Researcher Inference

Interpretation, die mehrere Evidenzen verbindet. Sie bleibt falsifizierbar.

### Open Hypothesis

Plausible Erklärung mit unzureichender Evidenz.

## A.3 Search Boundary

Repo-intern wurden für diesen Audit frisch bzw. direkt relevant geprüft:

- AGENTS.md;
- PROJECT_STATE.md;
- README.md;
- #28 Problem-/Need-/Pain-Baseline;
- #42 Requirements;
- #45 Research Quality;
- #48 Technical Lead;
- #59 Development & Verification;
- #61 Work Context / Method Conformance;
- #63 Value / Decision / Delivery / Feedback Assurance;
- #64 Product-/Research-Value Audit;
- #65 Wissensarbeit-Pilot-Rückfluss;
- #70 AI-Resilience Root-Cause Audit;
- #83/#84 Work-Selection-Reconciliation;
- #92 Architecture/Product Re-Baseline;
- PR #108–#119;
- chat-operationalization-self-audit-20260920.md;
- shared-research-state-audit-20260919.md;
- cross-pilot-saalfeld-1056-1071-20260920.md;
- PR #118 Deep-Research-Artefakt;
- PR #119 agentic execution plan / calibration work order;
- Source Identity Protocol;
- Requirements-/Assurance-/Operational-Contracts;
- Feedback Records FB-20260901-001, FB-20260901-002 und FB-20260902-003.

Extern wurde problemorientiert in Requirements Engineering, HCI, Coordination Theory, Boundary-Object-Forschung, Transdisziplinarität, Scientific Pluralism, Human Factors/Safety, Software Evolution, Sensemaking/Exploratory Search und aktueller AI-assisted Software Engineering recherchiert.

Dies ist keine exhaustive systematic review über alle genannten Disziplinen. Ziel ist hinreichend belastbare Evidenz zur Mechanismenprüfung.

---

# B. Bereits vorhandene Bedürfnisse: kein einfacher Requirements-Mangel

## B.1 Der zentrale Gegenbefund

**Project Evidence:** Die Problem-Baseline erfasst die später erneut artikulierten Kernbedürfnisse schon früh sehr deutlich.

Unter anderem:

- **G-001:** funktionierendes, dauerhaft nutzbares Forschungssystem, kein Konzeptpapier oder KI-Demonstrator;
- **G-002:** Research Owner darf unscharf fragen; das System soll Beobachtungen in fachwissenschaftlich saubere Problembegriffe, Methoden und Quellenlogiken übersetzen;
- **G-007:** wiederkehrende mechanische Arbeit soll bei realer Friktion automatisiert werden;
- **G-008:** Research State muss restartbar, providerunabhängig und ohne Chat rekonstruierbar sein;
- **G-009:** wissenschaftliche Komplexität muss für den Owner verständlich und fachlich auditierbar sein;
- **G-011:** Development realisiert Requirements; Technik definiert wissenschaftliche Needs nicht;
- **G-012:** Lean reduziert unnötige Systemkomplexität, nicht wissenschaftliche Tiefe;
- **N-001:** aus unscharfen Beobachtungen Fachbegriffe, Modelle und Forschungsfragen erschließen;
- **N-002:** Fachkompetenzen problemabhängig routen, weil der Nutzer die nötigen Disziplinen nicht vollständig selbst bestimmen kann;
- **N-017:** Capability-Verantwortung zwischen Owner, Fachspezialist, Software und LLM begründet verteilen;
- **N-018:** reale fachmethodische Acceptance je Capability;
- **N-020:** vorhandene Werkzeuge/Standards vor Eigenbau prüfen;
- **P-009:** mechanische Quellen-/Datei-/Sucharbeit bindet Zeit durch Medienbrüche und fehlende Workflowintegration;
- **P-010:** Chat-only-Erkenntnisse gehen verloren bzw. sind nicht auditierbar;
- **P-014:** wissenschaftlicher State kann für Nicht-Spezialisten schwer prüfbar werden;
- **P-016:** Lösungsideen können sich zu früh als Requirements verfestigen.

**Researcher Inference, strong:** Die spätere Frustration lässt sich nicht plausibel primär durch „der Nutzer hat seine Bedürfnisse nicht klar genug artikuliert“ erklären.

## B.2 Eine andere mögliche Lücke

Eine dokumentierte Need-Baseline garantiert nicht automatisch:

- dass die Needs in der Delivery-Reihenfolge dominieren;
- dass sie als observable User Experience operationalisiert werden;
- dass lokale Komponenten zusammen einen End-to-End-Flow bilden;
- dass die beim Nutzer verbleibende Koordinationslast gemessen wird;
- dass ein System erkennt, wann eine neue formale Struktur selbst Teil des Problems wird.

Damit verschiebt sich die Untersuchungsfrage von **Requirement presence** zu **Need-to-System Translation and Operational Integration**.

---

# C. Chronologische Fallrekonstruktion

## C.1 Phase 1 – starke Problem- und Schutzgrundlagen

Die frühen Baselines #28–#45 bauen eine für ein privates Forschungsprojekt ungewöhnlich explizite Trennung auf:

- Need/Pain vs. Solution Hypothesis;
- fachliche Authority vs. technische Authority;
- Evidence vs. AI Output;
- Source vs. konkrete Instanz vs. Findspot;
- Unsicherheit vs. Scheinsicherheit;
- technische Freiheit vs. accepted Requirement.

Diese Schicht reagiert auf reale Risiken. Es gibt keine belastbare Evidenz dafür, dass ihre Existenz als solche ein Fehler war.

## C.2 Phase 2 – Deterministic Assurance

#62 und #63 operationalisieren formale QA:

- Requirements Records;
- Trace Records;
- Changed-Code Guard;
- Goal/Need/Pain → Requirement → Decision → Delivery → Feedback.

**Project Evidence:** Bereits #63 hält ausdrücklich fest, dass Requirements-QA allein keinen Product-/Workflow-Fit beweist.

### Owner Feedback 2026-09-01

FB-20260901-001 fordert gerade deshalb die vollständige Wertschleife statt bloßer Requirements Records.

FB-20260901-002 zeigt einen ersten **Assurance-Rebound**: gekoppelte Änderungen und doppelte Workflows erzeugen unerwünschtes Notification-/Workflow-Rauschen.

### Owner Feedback 2026-09-02

FB-20260902-003 ist besonders wichtig:

> Nach dem Lampe-PDF-Pilot ist die Research Operation das Gegenteil des gewünschten Wissensarbeitsmodells: manuelle Markdown-Textwände, alte Annotationen, wenig Workflow-Automation, kein generierter menschenlesbarer Research Workspace und zu viel Orchestrierung bei Chat/Mensch.

Der Record sagt ausdrücklich: bestehende Requirements decken die gewünschte Richtung bereits; der Delta ist primär Delivery-/Architecture-Priorisierung.

**Researcher Inference, high:** Spätestens hier war empirisch sichtbar, dass **semantische/assurance-seitige Reife und operative Nutzerentlastung auseinanderliefen**.

## C.3 Phase 3 – #70 erkennt den Governance-Akkretionsloop

#70 beginnt bereits mit dem Muster:

~~~text
KI macht Fehler
→ neue Regel
→ neue Governance-Schicht
→ mehr Kontext / mehr Handoffs
→ neue KI-Orientierungsfehler
→ noch mehr Regeln
~~~

Der Audit versucht ausdrücklich, Regeln auf Root Causes und Schutzgüter zurückzuführen und aktive Governance später wieder zu reduzieren.

Das ist für den aktuellen Audit zentral, weil es zeigt:

> Das Projekt kannte den Mechanismus bereits.

Die Forschungsfrage ist deshalb nicht bloß „warum entstand zu viel Governance?“, sondern auch:

> Warum war die vorhandene Meta-Erkenntnis nicht hinreichend, um spätere Varianten desselben Musters zu verhindern?

## C.4 Phase 4 – #108–#116: Owner Signal → Abstraktion → Persistenz

PR #108–#116 bilden ein dicht dokumentiertes Cluster.

Der Self-Audit #116 kommt selbst zum Urteil:

~~~text
Rohsignal
→ plausible Interpretation
→ generische Abstraktion
→ Repo-Persistenz
~~~

statt:

~~~text
Rohsignal
→ Klassifikation
→ Gegenlesarten
→ Fach-/SOTA-Routing
→ Test an realen Workflows
→ verdichtete Synthese
→ ggf. Promotion
~~~

### Besonders relevante Episoden

- **#108:** legitime Scope-Erweiterung wird bereits mit State-Architektur gekoppelt;
- **#109:** reale Source-ID-Fragmentierung wird zu weitergehenden Shared-State-Hypothesen;
- **#110:** stärkster Fall einer methodisch falschen Promotion von Owner-Beispielen in eine Wissensraum-/Objektstruktur;
- **#111:** explizite Reclassification zu User Research;
- **#112/#114/#115:** nützliche Differenzierungen, aber erneut schnelle Mini-Taxonomien;
- **#113:** stärkere Meta-Reformulierung ohne harte Ontologie;
- **#116:** Self-Audit benennt Mirroring-Bias, premature abstraction und over-persistence.

Die relevante Erkenntnis ist nicht, dass jede Abstraktion falsch war. Mehrere waren fachlich plausibel.

Das Problem liegt in **Lifecycle und Evidenzniveau**: plausible Interpretation wurde zu schnell zum dauerhaften Projektobjekt.

## C.5 Phase 5 – #117: empirischer Gegencheck

Der Saalfeld-Cross-Pilot begrenzt die stärkeren Hypothesen. Er stützt einen kleineren gemeinsamen Evidenz-/Identity-Untergrund stärker als eine universelle Observation-/Relation-/Event-Spine.

Das ist ein Beispiel dafür, dass reale heterogene Arbeit stärkere Architekturhypothesen diskriminieren kann.

## C.6 Phase 6 – #118: erster sozio-technischer Deep Research

PR #118 diagnostiziert Interface-/Orchestrierungsfriktion und den Owner teilweise als „Semantic Compiler / Workflow Engine“.

Der Report öffnet den theoretischen Raum deutlich und grenzt mehrere Architekturpfade als Hypothesen statt Decisions ein.

## C.7 Phase 7 – #119: Near Miss auf einer anderen Ebene

Beim ersten Retrieval-Calibration-Work-Order war bereits bekannt bzw. vermutet, dass ein realer Provenienzpfad nicht automatisch ein texttragender Retrieval-Korpus ist.

Trotzdem wurde der erste Work Order zunächst so formuliert, als könne gegen den realen #55-Sachenbacher-State produktiv Exact Retrieval gebaut werden.

Der Implementierungsagent stoppte korrekt:

- realer Provenienzpfad vorhanden;
- kein admitted text-bearing corpus;
- produktive Umsetzung hätte neue Corpus-/State-Semantik erfordert.

Danach wurden mehrfach zusätzliche Planungsfehler gefunden:

- downstream Dependency fälschlich als current unresolved;
- fehlende Acceptance-/Negative Tests;
- zu offene Implementation Choices;
- Mutation Boundary nicht eng genug;
- Repo-Ready und Runtime-Ready zunächst nicht getrennt;
- ein gehärteter Planning-Head fiel korrekt in CI wegen eines veralteten Regressionstest-Wortlauts durch.

**Researcher Inference, high:** #119 ist kein einfacher Wiederholungsfall von #110. Er zeigt einen zweiten Mechanismus: **known risk / plausible suspicion wurde nicht in ein obligatorisch verifiziertes admission prerequisite transformiert**.

---

# D. Problem-/Mechanismenkarte

## D.1 M1 – Need-to-Structure Inversion

**Working label, keine neue Projektsemantik.**

### Beobachtung

Bedürfnisse wie:

- „ich kann die zuständige Fachdomäne nicht selbst bestimmen“;
- „ich will unscharf fragen“;
- „mechanische Arbeit soll das System übernehmen“;
- „ich will nachvollziehen können, warum“;

werden korrekt dokumentiert.

Die Projektentwicklung reagiert darauf häufig mit:

- mehr expliziten Zuständen;
- mehr Authority-Grenzen;
- mehr Handoffs;
- mehr formalen Records;
- mehr strukturierter Projektsemantik.

### Möglicher Mechanismus

Formalisierung ist für Software und AI leichter überprüfbar als die schwerere Frage, ob der gesamte menschliche Arbeitsfluss tatsächlich einfacher geworden ist.

Dadurch kann ein Need nach **complexity absorption** in Maßnahmen übersetzt werden, die zunächst **complexity representation** erzeugen.

### Gegenbefund

Ohne die expliziten Zustände wären Source Laundering, AI-as-Evidence, Chat-Memory und Authority Drift schwerer kontrollierbar.

### Status

**Supported as recurring mechanism; causality still partial.**

---

## D.2 M2 – Semantic Decomposition → Coordination Rebound

### Beobachtung

Histo-Orla trennt wissenschaftlich sinnvoll:

- Requirements Authority;
- Method Authority;
- Research Owners;
- Technical Lead;
- Development;
- Assurance;
- Source/Instance/Findspot;
- Retrieval;
- Audit;
- Availability;
- Rights.

Diese Trennung schützt Semantik.

Gleichzeitig erzeugt sie operative Dependencies und Übergänge.

### External Research Fit

Malone & Crowston definieren Coordination als Management von Dependencies zwischen Aktivitäten. Spezialisierung beseitigt Koordinationsbedarf nicht; sie erzeugt gerade neue Dependencies.

Boundary-Object-Forschung zeigt, dass heterogene Spezialisten nicht vollständige Semantik teilen müssen, aber funktionsfähige gemeinsame Interfaces brauchen.

### Möglicher Mechanismus

Eine semantisch korrekte Verantwortungszerlegung wurde teilweise zu eng mit der operativen Arbeitszerlegung gekoppelt.

### Alternative Erklärung

Die Handoffs könnten nur während der Aufbauphase hoch sein und später durch stabile Interfaces verschwinden.

### Status

**Strongly supported current burden; long-term necessity unresolved.**

---

## D.3 M3 – Governance Accretion through Error Response

### Beobachtung

#70 dokumentiert explizit:

Fehler → Gegenregel → mehr Kontext/Handoffs → neue Orientierungsfehler.

### External Research Fit

Reason unterscheidet Person- und Systemansatz. Fehler am „sharp end“ sind häufig Symptome tieferer latenter Systembedingungen.

Rasmussen argumentiert für systemorientierte, cross-level Analyse und gegen rein strukturelle Zerlegung einzelner Fehlerhandlungen.

High-Reliability-Forschung betrachtet Near Misses als Lerngelegenheiten und fordert „reluctance to simplify“.

### Möglicher Mechanismus

Ein lokaler Fehler erzeugt eine sichtbare, einfach formulierbare Regel. Die Regel ist sofort persistierbar und testbar. Eine tiefere Änderung an Interface, Runtime oder Arbeitsfluss ist teurer und unsicherer.

Damit existiert ein struktureller Bias zugunsten **rule addition** gegenüber **system redesign or removal of coordination demand**.

### Gegenbefund

#70 selbst enthält bereits Retirement-/Simplification-Regeln. Das Projekt besitzt also einen Mechanismus gegen blinde Akkretion.

### Offene Frage

Warum reicht dieser Mechanismus nicht aus? Mögliche Faktoren:

- Regeln werden retrospektiv auditiert, nicht bei jeder neuen Interpretationsbewegung automatisch;
- Product Utility ist schwächer deterministisch messbar als Regelkonformität;
- Chat/AI kann pro Turn lokal vollständig wirken, während kumulative Koordinationslast erst später sichtbar wird.

### Status

**Strong pattern, causal decomposition unresolved.**

---

## D.4 M4 – Meta-Persistence Loop

### Beobachtung

#116 beschreibt, dass einzelne Owner-Turns wiederholt direkt in versionierte Discovery-/Design-Artefakte wanderten.

### Vorteil

Persistenz schützt gegen Wissensverlust.

### Nachteil

Persistenz verändert die ökonomische und kognitive Bedeutung einer Idee:

Eine temporäre Hypothese wird:

- auffindbar;
- referenzierbar;
- downstream verlinkbar;
- später als „bereits bestehender Projektstate“ wahrgenommen.

Damit kann Persistenz unbeabsichtigt **epistemisches Gewicht simulieren**.

### External Research Fit

W3C PROV zeigt, wie wichtig Herkunft und Transformation sind, sagt aber nicht, dass jedes Zwischenurteil kanonischer State werden muss.

Scientific Pluralism und transdisziplinäre Integration sprechen für vorläufige, revidierbare und nebeneinander bestehende Repräsentationen statt vorschneller Vereinheitlichung.

### Status

**Strongly supported for #108–#116; generality beyond this cluster plausible but not proven.**

---

## D.5 M5 – Local Verification / Global Utility Gap

### Beobachtung

Histo-Orla besitzt:

- formal grüne Assurance;
- Source-/Identity-Contracts;
- traceable Requirements;
- tested Work Context;
- Audit Renderer.

Parallel sagt FB-20260902-003:

- manuelle Textwände;
- wenig Workflowautomation;
- kein owner-readable Research Workspace;
- zu viel Orchestrierung durch Chat/Mensch.

### External Research Fit

ISO 9241-210 behandelt Human-Centred Design als Life-Cycle-Aktivität für die Qualität der Human-System-Interaktion.

Requirements Standards fordern strukturierte Requirements-Prozesse, aber Requirements-Konformität ist nicht identisch mit tatsächlichem Nutzungserfolg.

Aktuelle AI-Evaluationsforschung zeigt ein analoges Messproblem:
- SWE-benchartige Benchmarks liefern skalierbare Signale;
- reale längere Entwicklungsarbeit kann sich anders verhalten;
- OpenAI erklärte 2026 SWE-bench Verified wegen fehlerhafter Tests und Kontamination als ungeeignet für Frontier-Messung;
- SWE-Bench Pro wurde gerade geschaffen, um realistischere long-horizon Tasks abzubilden.

### Möglicher Mechanismus

Leicht messbare lokale Conformance wird zum dominanten Fortschrittssignal, während End-to-End-Utility seltener und teurer beobachtet wird.

### Status

**Strongly supported gap; no evidence that formal QA itself caused low utility.**

---

## D.6 M6 – Readiness Conflation / Assumption Laundering

### Beobachtung

#119 zwang nach dem Fehlstart die explizite Trennung:

~~~text
real provenance chain
!= text-bearing input
!= current corpus availability
!= provider-independent byte resolver
~~~

und später:

~~~text
repository-ready
!= execution-environment-ready
~~~

### Mechanismus

Mehrere semantisch nahe Zustände werden im Arbeitsfluss als implizite Folgebeziehung behandelt:

„existiert“ → „ist zugreifbar“ → „ist verwendbar“ → „ist für diese Operation geeignet“.

Das ist eine Form von **assumption laundering**: eine plausible Zwischenannahme wird im nächsten Arbeitsschritt wie etablierte Voraussetzung behandelt.

### Interne Gegenregel

Source Identity Protocol und #57 trennen Identity/Availability grundsätzlich bereits.

### Bedeutung

Der Fehler liegt daher nicht nur in fehlender Semantik, sondern in der **Nichtanwendung vorhandener Differenzierung an einer konkreten Execution Boundary**.

### Status

**Strongly supported by #119.**

---

## D.7 M7 – Mirroring / Affirmative Abstraction Bias

### Beobachtung

#116 identifiziert kommunikative Muster wie „Genau“, „das ist der Kern“ vor ausreichender adversarialer Prüfung.

Owner-Metaphern zu Wissensraum, Perspektiven, Relationen oder Temporalität wurden teilweise zu schnell strukturell interpretiert.

### Möglicher AI-spezifischer Mechanismus

LLMs sind stark darin, lokale Kohärenz herzustellen und plausible konzeptuelle Fortsetzungen zu bilden. In einem Projekt mit hoher Persistenzfähigkeit kann diese Stärke zum Risiko werden:

~~~text
ambiguous owner signal
→ coherent interpretation
→ polished structure
→ apparent confidence
→ persisted artifact
~~~

### External Evidence

Aktuelle AI-Software-Engineering-Evidence warnt allgemein vor Übertragung von Benchmark-/Task-Erfolg auf reale Arbeit.

METR fand in einer 2025-RCT bei 16 erfahrenen OSS-Entwicklern auf ihren eigenen Repositories eine 19% längere Bearbeitungszeit mit damaligen AI-Tools, obwohl die Entwickler subjektiv Beschleunigung erwarteten und wahrnahmen. METR bezeichnet dieses Resultat inzwischen selbst als historischen Snapshot und berichtet 2026, dass neuere Experimente durch Selection Bias kein sauberes aktuelles Signal liefern.

Das ist **kein direkter Nachweis von Mirroring Bias**. Es ist aber relevante Gegen-Evidence gegen die Annahme, wahrgenommene lokale AI-Unterstützung entspreche zuverlässig realer Systemproduktivität.

### Status

**Strongly evidenced internally; external causal literature for this exact project pattern remains incomplete.**

---

## D.8 M8 – Context/Handoff Protection can become Context/Handoff Work

### Beobachtung

AGENTS verlangt zurecht restartbare Work Contexts und persistierte Handoffs.

Gleichzeitig entstehen:

- Bootstrap-Sequenzen;
- Work Orders;
- fingerprints;
- owner routing;
- handoff records;
- review gates.

Diese reduzieren Context Loss, sind aber selbst Arbeit.

### External Research Fit

Coordination Theory: jede Dependency braucht Koordinationsprozesse.

Distributed/socio-technical cognition: kognitive Arbeit kann produktiv auf Menschen, Artefakte und Systeme verteilt werden; entscheidend ist nicht, ob Koordination existiert, sondern **wo die kognitive Last liegt**.

### Offene Frage

Welche Teile dieser Koordination sind unvermeidbare epistemische Arbeit, welche nur derzeit manuelle Systemarbeit?

### Status

**Observed burden; classification essential vs accidental unresolved.**

---

# E. Warum die Mechanismen rational entstanden

Eine professionelle Fehlerkultur darf die heutige Diagnose nicht rückwirkend in ein einfaches „wir hätten es wissen müssen“ verwandeln.

## E.1 Scientific risk justified explicit boundaries

Histo-Orla bearbeitet historische Forschung mit:

- heterogenen Quellen;
- unsicheren Identitäten;
- widersprüchlichen Befunden;
- Fachmethoden;
- AI-generierten Vorschlägen;
- langfristigem Research State.

Damit sind Source Laundering, premature certainty und Chat-State reale Risiken.

## E.2 AI unreliability justified deterministic guards

P-008 war validiert: generische AI-Antworten können flüssig und unzuverlässig sein.

Daher sind deterministic guards für **settled invariants** rational.

## E.3 Restartability justified persistence

P-010 und G-008 begründen Git-/Repo-Persistenz.

Ein rein conversational system hätte ein noch größeres Kontinuitätsproblem.

## E.4 Specialization justified authority separation

N-002/N-013 und die Fachdomänenstruktur sprechen gegen eine einzige generische Epistemik.

Scientific Pluralism unterstützt, dass unterschiedliche Methoden und Ontologien koexistieren können.

## E.5 Counterfinding

**Researcher Inference, high:** Das Problem ist deshalb nicht plausibel als „zu viel Sorgfalt“ oder „zu viel Wissenschaftlichkeit“ beschreibbar.

Präziser ist:

> notwendige fachliche und epistemische Differenzierung wurde nicht immer durch eine entsprechend starke Integrations- und Nutzungsschicht ergänzt.

---

# F. Essential vs. Accidental Complexity

Die Trennung ist nicht vollständig objektiv; folgende Klassifikation ist analytisch.

| Komplexität | Beispiel | vorläufige Einordnung |
|---|---|---|
| Quellenkritik | Source/Instance/Edition/Findspot unterscheiden | überwiegend essential domain complexity |
| Method Plurality | unterschiedliche Fachdomänen / Evidenzlogiken | essential epistemic complexity |
| Unsicherheit | unresolved, competing explanations | essential epistemic complexity |
| Provider / Bytes | Zotero, OneDrive, lokale Dateien | teils environmental / technical |
| IDs / Provenienz | stabile interne vs externe Referenzen | notwendige technical mediation |
| viele manuelle Handoffs | Owner verbindet #49/#51/#53/#55/#57 | überwiegend coordination/interface complexity |
| wiederholte Meta-Reconciliation | neue Artefakte erklären vorherige Artefakte | überwiegend accidental / governance complexity, fallabhängig |
| CI/Assurance | settled invariants deterministisch prüfen | protective complexity; Nutzen/Burden empirisch zu beobachten |
| Work Orders | bounded execution ohne semantische Drift | protective coordination mechanism; Kosten real |
| Chat als Integrator | Mensch hält implizite Capability-Kette zusammen | accidental complexity / missing integration candidate |
| Taxonomien aus Owner-Metaphern | #110/#114/#115 | premature representational complexity |

**Unsicherheit:** „accidental“ bedeutet hier nicht automatisch „leicht entfernbar“. Akkumulierte accidental complexity kann später selbst strukturelle Dependencies erzeugen.

---

# G. Schnittstellenanalyse

## G.1 User Need → Problem Framing

### Stärke

Needs sind explizit und differenziert.

### Failure Mode

Owner-Formulierungen können als Systemstruktur interpretiert werden, bevor alternative Lesarten geprüft sind.

### Externe Passfähigkeit

Human-Centred Design verlangt Kontext-/Nutzungsorientierung über den Lebenszyklus. Transdisziplinarität behandelt Problem Framing als iterativ, nicht als einmalige Übergabe.

### Fit

**Strong fit** zur internen Diagnose.

---

## G.2 Problem Framing → Requirement

### Stärke

#42 trennt Requirement Lifecycle von Domain Authority.

### Failure Mode

Nicht jede wiederholte Friktion erfordert neuen Requirement-Text. FB-20260902-003 zeigt, dass ein Pain trotz bereits passender Requirements bestehen kann.

### Bedeutung

Eine Requirements-Schicht kann korrekt sein und trotzdem keine hinreichende Delivery-Steuerung darstellen.

### Fit

**Strongly supported.**

---

## G.3 Requirement → Technical Work

### Stärke

#48/#59 verlangen SOTA, Reversibilität und Traceability.

### Failure Mode

Die technisch sichtbaren Issues zerlegen den Capability-Raum; Integration wird dadurch nicht automatisch zu einem User Flow.

### Coordination-Theory Fit

**Strong fit:** Spezialisierte Aktivitäten erzeugen Dependencies, die explizit gemanagt werden müssen.

---

## G.4 Evidence → Digital State

### Stärke

Source Identity Protocol ist fachlich sauber und schützt gegen Source Laundering.

### Failure Mode

Existenz einer sauberen Identität kann im nächsten technischen Schritt als Availability/Operation-Readiness missverstanden werden (#119).

### Fit

**Strong internal evidence.**

---

## G.5 AI → Human Judgement

### Stärke

AI Output ist explizit keine Evidence.

### Failure Mode

Das Problem liegt weniger in direkter AI-Authority als in **AI-generated project structure**: plausible Interpretation kann Projektstate verändern, obwohl sie nicht als fachliche Wahrheit etikettiert wird.

### Status

**Important distinction.** Existing AI/Evidence guards protect content truth better than they protect project-structure accretion.

---

## G.6 Local Component → Whole Research System

### Stärke

Viele Einzelkomponenten sind testbar.

### Failure Mode

FB-20260902-003 zeigt mangelnde operative Integration trotz lokaler Fortschritte.

### External Fit

Software-evolution literature und coordination research machen plausibel, dass lokale Modulqualität keine globale Complexity-/Coordination-Kontrolle garantiert.

---

## G.7 Development → Feedback

### Stärke

#63 formalisiert Feedback.

### Failure Mode

Ein Feedback Record garantiert nicht, dass Delivery unmittelbar umpriorisiert wird oder dass das gemeldete Pain schnell verschwindet.

### Open Question

Wie groß war die tatsächliche Latenz zwischen Feedback und systemischer Reaktion? Dieser Audit quantifiziert sie noch nicht vollständig.

---

# H. Externer State of the Art – Mechanismen und Passfähigkeit

## H.1 Requirements Engineering

### Quelle

ISO/IEC/IEEE 29148 – Systems and software engineering — Requirements engineering  
https://www.iso.org/standard/94091.html

### Relevanz

Der Standard behandelt Requirements als Life-Cycle-Prozess mit definierten Information Items und systematischer Requirements-Arbeit.

### Histo-Orla Fit

- unterstützt die Trennung von Needs, Requirements und Delivery;
- widerlegt aber die Vorstellung, dass dokumentierte Requirements allein Product Fit garantieren.

### Transfergrenze

ISO 29148 ist kein HCI- oder Research-Workflow-Modell.

**Fit: partial / necessary but insufficient.**

---

## H.2 Human-Centred Design

### Quelle

ISO 9241-210 – Human-centred design for interactive systems  
https://www.iso.org/standard/77520.html

### Relevanz

Human-Centred Design adressiert Prinzipien und Aktivitäten über den Lebenszyklus interaktiver Systeme.

### Histo-Orla Fit

Die wiederholte Owner-Erfahrung ist nicht bloß „Feedback nach Implementation“, sondern Evidenz über die tatsächliche Human-System-Arbeitsteilung.

**Fit: strong.**

---

## H.3 Coordination Theory

### Quelle

Malone, T. W.; Crowston, K. (1994): The Interdisciplinary Study of Coordination. ACM Computing Surveys 26(1), 87–119. DOI 10.1145/174666.174668.

### Kernaussage

Coordination kann als Management von Dependencies zwischen Aktivitäten verstanden werden.

### Histo-Orla Fit

Sehr stark für die Beobachtung:

~~~text
mehr fachliche/technische Spezialisierung
→ mehr Dependencies
→ Integrations-/Koordinationsbedarf
~~~

Semantisch richtige Owner-Grenzen können daher operative Koordinationskosten erzeugen, ohne selbst falsch zu sein.

**Fit: strong.**

---

## H.4 Boundary Objects / Knowledge Integration

### Quellen

Star, S. L.; Griesemer, J. R. (1989): Institutional Ecology, “Translations” and Boundary Objects. Social Studies of Science 19(3), 387–420. DOI 10.1177/030631289019003001.

Caccamo, M.; Pittino, D.; Tell, F. (2023): Boundary objects, knowledge integration, and innovation management: A systematic review. Technovation 122, 102645. DOI 10.1016/j.technovation.2022.102645.

### Kernaussage

Heterogene Akteure müssen nicht vollständig vereinheitlicht werden. Boundary Objects können lokal anpassbar und zugleich identitätsstabil sein.

Der 2023 Review von 87 Beiträgen zeigt zugleich: unterschiedliche Arten von Boundary Objects passen zu unterschiedlichen Knowledge-Integration-Anforderungen; ein bloß geteiltes Artefakt ist nicht automatisch wirksam.

### Histo-Orla Fit

Sehr stark gegen zwei Extreme:

- Universalmodell als Voraussetzung für Integration;
- reine Separation ohne funktionsfähige gemeinsame Interfaces.

**Fit: strong.**

---

## H.5 Transdisziplinäre Integration

### Quelle

Lam, D. P. M. et al. (2021): Conceptualising transdisciplinary integration as a multidimensional interactive process. Environmental Science & Policy 118, 18–26. DOI 10.1016/j.envsci.2020.12.005.

### Kernaussage

Integration ist ein offener, multidimensionaler Lernprozess ohne zwingend vorbestimmtes Ergebnis. Konsens ist nur eine mögliche Form; Pluralität kann erhalten bleiben.

### Histo-Orla Fit

Stützt:

- iterative Problemübersetzung;
- keine vorschnelle Ontologie;
- Domain Plurality.

Es sagt weniger darüber, wie ein privates AI-gestütztes Softwareprojekt konkret implementiert werden soll.

**Fit: strong conceptual / weak implementation specificity.**

---

## H.6 Scientific Pluralism

### Quelle

Stanford Encyclopedia of Philosophy: Scientific Pluralism, substantive revision 2026.  
https://plato.stanford.edu/entries/scientific-pluralism/

### Kernaussage

Wissenschaftliche Praxis verwendet heterogene Methoden, Theorien, Modelle und Ontologien. Pluralität ist nicht automatisch ein Defekt, der durch ein einheitliches Framework beseitigt werden muss.

### Histo-Orla Fit

Stark gegen premature universalization von Relations-/Event-/Temporal-Modellen.

**Fit: strong epistemic challenge.**

---

## H.7 Human Factors / System Approach to Error

### Quellen

Reason, J. (2000): Human error: models and management. BMJ 320:768–770. DOI 10.1136/bmj.320.7237.768.

Rasmussen, J. (1997): Risk management in a dynamic society: a modelling problem. Safety Science 27(2–3), 183–213. DOI 10.1016/S0925-7535(97)00052-0.

### Kernaussage

Reason kontrastiert Person- und Systemansatz. Fehler am „sharp end“ entstehen oft in einem Kontext latenter Systembedingungen.

Rasmussen fordert cross-level system models und warnt vor rein struktureller Zerlegung; Verhalten wird durch Grenzen, Zwänge und Anpassung geprägt.

### Histo-Orla Fit

Stark für professionelle Fehlerkultur:

Der relevante Fehler ist nicht „der Agent hätte besser denken sollen“, wenn Auftrag, Admission, Artefaktstruktur oder Feedbacksystem den Fehler wahrscheinlicher machen.

**Fit: strong.**

---

## H.8 High-Reliability Organizing / Near Misses

### Quellen

Cantu et al. (2020): Interventions and measurements of highly reliable/resilient organization implementations: a literature review. Applied Ergonomics 90, 103241.

AHRQ PSNet: High Reliability primer.

Gnoni, M. G.; Saleh, J. H. (2017): Near-miss management systems and observability-in-depth: Handling safety incidents and accident precursors in light of safety principles. Safety Science 91, 154–167. DOI 10.1016/j.ssci.2016.08.012.

### Kernaussage

HRO-Prinzipien umfassen:

- preoccupation with failure;
- reluctance to simplify;
- sensitivity to operations;
- commitment to resilience;
- deference to expertise.

Near Misses sind wertvolle Lernquellen.

### Gegenbefund

HRO-Forschung zeigt zugleich, dass Umsetzung schwierig ist und neue Kommunikations-/Informationsprobleme entstehen können. Ein Safety-System ist nicht automatisch gut, nur weil es viele Checks hat.

### Histo-Orla Fit

#119 ist analytisch gut als Near Miss lesbar: der Agent verhinderte einen consequential Fehler; das wertvolle Datum ist der upstream Mechanismus, der den falschen Auftrag erzeugte.

**Fit: strong as error-culture lens, not as literal safety analogy.**

---

## H.9 Software Evolution / Complexity

### Quellen

Lehman, M. M. – Laws of Software Evolution; als empirische Gegenprüfung u. a. Oliveira et al. (2017), *Evaluating Lehman’s Laws of software evolution within software product lines industrial projects*, Journal of Systems and Software 131, 347–365, DOI 10.1016/j.jss.2016.07.038. Die Literatur zeigt gemischte Unterstützung einzelner Laws statt einer universell harten Gesetzmäßigkeit.

Langzeitstudien zu Lehman’s Laws formulieren u. a. die Beobachtung, dass E-Type-Systeme kontinuierlich angepasst werden und Komplexität ohne aktive Reduktionsarbeit steigt.

### Histo-Orla Fit

Plausibel für die akkretive Entwicklung von Requirements, Assurance und Artefakten.

### Transfergrenze

Lehman beschreibt Softwareevolution; Histo-Orlas Hauptkomplexität liegt teils in Repo-/Governance-/Knowledge-State, nicht nur Code.

**Fit: partial but relevant.**

---

## H.10 Mixed-Initiative Interaction

### Quellen

Horvitz, E. (1999): Principles of Mixed-Initiative User Interfaces; Mixed-Initiative Interaction. Microsoft Research / CHI / IEEE Intelligent Systems.

https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/

### Kernaussage

Nicht Totalautomation vs. totale Nutzerkontrolle, sondern flexible Verteilung: Mensch und Maschine tragen jeweils passend zum Kontext bei.

### Histo-Orla Fit

Sehr stark zu N-017.

Die aktuelle Frustration kann als Fehlallokation von Initiative gelesen werden: der Mensch übernimmt rekonstruierbare Routing-/Koordinationsarbeit, obwohl seine wertvollste Rolle im fachlichen/strategischen Urteil liegt.

### Unsicherheit

Welche Aufgaben in Histo-Orla konkret automatisierbar sind, ist eine separate empirische Frage.

**Fit: strong principle, operation unresolved.**

---

## H.11 Sensemaking / Exploratory Search

### Quellen

Pirolli, P.; Card, S. (2005): The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis.

Marchionini, G. (2006): Exploratory Search: From Finding to Understanding. Communications of the ACM 49(4), 41–46. DOI 10.1145/1121949.1121979.

### Kernaussage

Expert knowledge work ist iterativ: Information wird gesucht, organisiert, in Schemata überführt, geprüft und zu Arbeitsprodukten verdichtet.

Exploratory Search umfasst Lernen und Investigation, nicht nur Lookup.

### Histo-Orla Fit

Stützt die Beobachtung, dass „Query → Answer“ kein hinreichendes Produktmodell für historische Forschung ist.

Ebenso erklärt es, warum ein System, das nur atomaren State korrekt verwaltet, noch keine gute Forschungsoberfläche liefert.

**Fit: strong.**

---

## H.12 Provenance

### Quelle

W3C PROV-O Recommendation  
https://www.w3.org/TR/prov-o/

### Kernaussage

Provenance lässt sich explizit über Entities, Activities, Agents und Derivationen repräsentieren und domänenspezifisch spezialisieren.

### Histo-Orla Fit

Stützt die Bedeutung expliziter Herleitung.

### Gegenbefund

PROV-O sagt nicht, dass jede Denkbewegung persistent oder kanonisch sein muss.

**Fit: strong for provenance; neutral on persistence granularity.**

---

## H.13 Aktuelle AI-assisted Software Engineering Evidence

### METR 2025

Becker et al. (2025), RCT mit 16 erfahrenen OSS-Entwicklern und 246 Tasks in vertrauten Repositories:

- Entwickler erwarteten deutliche Beschleunigung;
- beobachtet wurde mit damaligen Tools eine ca. 19% längere Bearbeitungszeit.

Quelle: https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf

### METR 2026 Update

METR weist darauf hin, dass das 2025-Ergebnis inzwischen historisch ist. Ein neueres Experiment liefert wegen veränderter Teilnahmebereitschaft / Selection Bias kein sauberes aktuelles Produktivitätssignal.

Quelle: https://metr.org/blog/2026-02-24-uplift-update/

### Benchmark-Evidence

OpenAI erklärte im Februar 2026 SWE-bench Verified für Frontier-Messung als zunehmend ungeeignet, u. a. wegen fehlerhafter Tests und Trainingskontamination.

Quelle: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

SWE-Bench Pro versucht realistischere long-horizon, enterprise-nahe Tasks abzubilden.

Quelle: https://arxiv.org/abs/2509.16941

### Histo-Orla Fit

Diese Befunde beweisen keine konkrete Histo-Orla-Ursache.

Sie stützen aber zwei methodische Vorsichten:

1. AI-Wirkung ist stark kontext- und taskabhängig.
2. leicht skalierbare Benchmarks oder subjektiv empfundene Produktivität können reale längere Entwicklungsarbeit falsch repräsentieren.

**Fit: strong methodological analogy; direct causal transfer weak.**

---

# I. Warum erkanntes Wissen das Muster nicht automatisch stoppt

Dies ist die wichtigste neue Forschungsfrage gegenüber PR #118.

## I.1 Knowledge ≠ Control Mechanism

#70 wusste bereits, dass neue Regeln neue Governance erzeugen können.

#116 wusste bereits, dass Owner Signals zu schnell abstrahiert werden.

Trotzdem trat #119 als anderer Fehler derselben Familie auf.

### Researcher Inference

Ein dokumentiertes Anti-Pattern ist zunächst **descriptive knowledge**.

Es wird erst wirksam, wenn an der relevanten Ausführungsgrenze:

- der Zustand erkennbar ist;
- ein passender Trigger existiert;
- der Fehler blockiert oder sichtbar gemacht wird;
- das Signal nicht durch eine ähnlich klingende Kategorie übergangen wird.

#119 fehlte zunächst nicht die abstrakte Idee „Availability ist wichtig“, sondern die konkrete **Admission-Prüfung dieser Voraussetzung**.

## I.2 Local Objective Functions

Jeder Arbeitskontext hatte ein lokales plausibles Ziel:

- Requirement vollständig machen;
- Traceability verbessern;
- Owner-Signal sauber persistieren;
- Architekturhypothese explizieren;
- Work Order ausführbar machen.

Das globale Ziel „Owner muss weniger koordinieren“ ist schwerer lokal messbar.

**Open Hypothesis:** lokale objektive Erfüllbarkeit erzeugt einen systemischen Bias zugunsten formaler Vollständigkeit.

## I.3 Persistence creates inertia

Sobald eine Struktur persistiert ist:

- muss sie reconciliiert werden;
- andere Artefakte referenzieren sie;
- sie erzeugt Handoff-Kontext;
- ihr Entfernen wird selbst zur Arbeit.

Das kann selbst bei korrekter No-Loss-Governance zu einer **path dependence** führen.

## I.4 AI generates coherence faster than evidence

LLMs können schnell:

- Taxonomien;
- Rollenmodelle;
- Interfaces;
- Checklisten;
- Dokumente;

produzieren.

Reale Falsifikation verlangt dagegen:

- Zugriff;
- echte Daten;
- technische Umgebung;
- Domain Review;
- Owner-Nutzung.

**Researcher Inference:** Die Produktionskosten von strukturierter Erklärung sind niedriger als die Kosten von realer Integrationsevidenz. Das kann die Entwicklungsaktivität verzerren.

Status: **plausible / not directly quantified.**

---

# J. Fehlerkultur: Klassifikation statt Schuld

## J.1 PR #110

**Klasse:** methodologically wrong promotion / recoverable.

Nicht: „schlechte Idee“.

Sondern: Lifecycle-Fehler – Owner Examples wurden zu früh in Foundational Design überführt.

## J.2 PR #116

**Klasse:** successful self-detection.

Der Wert liegt darin, den Fehler offen zu benennen und historische PRs nicht zu löschen.

## J.3 PR #117

**Klasse:** empirical recovery / challenge.

## J.4 PR #119 erster Work Run

**Klasse:** near miss / fail-closed success.

Der Implementer verhinderte die Folge.

Upstream bleibt ein Planning-/Admission-Fehler.

## J.5 PR #119 zweiter Planning-CI-Fail

**Klasse:** test-detected regression in planning mechanics.

Der rote Lauf ist kein Projektversagen, sondern Evidence, dass das Gate tatsächlich wirksam war.

## J.6 Systemische Bewertung

Der zentrale professionelle Fehlerkultur-Befund ist:

> Für eine systemische Fehleranalyse reicht der Befund „rechtzeitig blockiert“ nicht aus; analytisch relevant bleiben zusätzlich die Bedingungen, unter denen derselbe Fehlertyp wiederholt entstehen kann.

---

# K. Spannungen ohne Auflösung

## K.1 Auditability ↔ Cognitive Load

Mehr Traceability verbessert Nachvollziehbarkeit und kann zugleich die Bedienlast erhöhen.

Keine Seite kann pauschal maximiert werden.

## K.2 Specialization ↔ Coordination

Fachliche Pluralität verlangt getrennte Authority.

Trennung erzeugt Dependencies.

## K.3 Restartability ↔ Meta-Persistence

Persistenz verhindert Wissensverlust.

Zu feinkörnige Persistenz kann temporäre Hypothesen verhärten und Reconciliation-Arbeit erzeugen.

## K.4 Fail-Closed ↔ Flow

Fail-closed schützt consequential state.

Zu breite Gates können Exploration lähmen oder Handoffs vermehren.

## K.5 Deterministic Assurance ↔ Real Utility

Formale Tests sind reproduzierbar.

Owner Utility ist kontextuell und seltener messbar.

## K.6 Provider Independence ↔ Practical Integration

Provider-Unabhängigkeit schützt Research State.

Praktische Forschung braucht dennoch tiefe Integration mit konkreten Werkzeugen.

## K.7 Generalization ↔ Fragmentation

Zu frühe Abstraktion flatten’t Domänen.

Zu späte Abstraktion erzeugt Silos und manuelle Reconciliation.

## K.8 AI Initiative ↔ Human Authority

Zu wenig Automation macht den Owner zum Workflow Engine.

Zu viel Automation kann epistemische Authority überschreiten.

---

# L. Compatibility / Fit Matrix

| Beobachteter Histo-Orla-Befund | Externer Mechanismus | Fit | Grenze |
|---|---|---|---|
| Needs vorhanden, Utility-Pain bleibt | HCD / context of use | strong | kein Architekturentscheid |
| viele spezialisierte Owner / Handoffs | Coordination Theory | strong | Quantifizierung fehlt |
| gemeinsamer State vs Domain Plurality | Boundary Objects | strong | kein fertiges Datenmodell |
| keine Universalontologie | Scientific Pluralism | strong | nicht jede Integration ist optional |
| Owner Signal vorschnell promoted | transdisciplinary iterative framing | strong | AI-spezifische Ursache unvollständig |
| Fehler → Regel → mehr Governance | system approach / HRO | strong | Sicherheitsdomäne nur analog |
| CI grün, Workflow schmerzhaft | local proxy vs real outcome | strong empirical project evidence | kein Beweis gegen CI |
| #119 corpus assumption | latent condition / readiness conflation | strong internal | generische Häufigkeit unbekannt |
| AI fühlt produktiv, reale Wirkung unsicher | METR / benchmark limitations | partial-strong analogy | andere Population/Tasks |
| Knowledge work nicht Lookup | Sensemaking / Exploratory Search | strong | konkrete UX bleibt offen |
| Provenance wichtig | W3C PROV | strong | Persistenzgranularität nicht vorgegeben |

---

# M. Gegenhypothesen

## M.1 „Die Komplexität ist einfach unvermeidbar“

Teilweise plausibel.

Historische Forschung ist fachlich komplex. Provider-, Rights- und Evidence-Grenzen sind real.

Gegenbefund: Owner Feedback identifiziert explizit **mechanische** Orchestrierung und Textwand-Arbeit, nicht nur fachliches Urteil.

Status: **partial explanation only**.

## M.2 „Das Projekt ist nur noch nicht weit genug“

Möglich: frühe Infrastruktur ist sichtbar, Integration folgt später.

Gegenbefund: das Pain wurde wiederholt dokumentiert und erzeugte bereits eigene Korrekturschleifen.

Status: **plausible but insufficient alone**.

## M.3 „Mehr Governance war die richtige Übergangsstrategie“

Teilweise stark gestützt: Guards verhinderten reale Fehler, einschließlich #119.

Gegenbefund: #70 und #64 zeigen, dass Governance selbst Nebenwirkungen erzeugt.

Status: **both protective and burden-producing**.

## M.4 „Der Owner korrigiert einfach besonders viel, weil der Qualitätsanspruch extrem hoch ist“

Möglich als Verstärker.

Gegenbefund: viele Korrekturen betreffen nicht zusätzliche Qualität, sondern bereits dokumentierte Kernziele wie unscharfe Fragen, Nutzerentlastung, no AI authority und reale Research Integration.

Status: **possible amplifier, weak as root explanation**.

## M.5 „Das Problem ist primär LLM-Unzuverlässigkeit“

Unzureichend.

LLM-Eigenschaften wie coherent completion und mirroring sind plausibel beteiligt. Aber auch Issue-Topologie, Persistenzregeln, lokale Fortschrittssignale und fehlende Runtime-Integration tragen.

Status: **partial mechanism, not sufficient root cause**.

## M.6 „Die Lösung wäre einfach weniger Dokumentation“

Nicht durch Evidenz gedeckt.

Dokumentation schützt Restartability und Scientific Audit.

Die relevante Frage ist Granularität, Lifecycle und Ableitbarkeit, nicht Dokumentation ja/nein.

Status: **rejected as oversimplification**.

---

# N. Am stärksten belegte Problembefunde

Diese Punkte sind Analyseergebnis, keine Lösungsempfehlung.

## N.1 Strong

Histo-Orlas zentrale Nutzerbedürfnisse waren früh und explizit vorhanden. Die wiederholte Frustration ist daher nicht hinreichend als fehlende Need-Elicitation erklärbar.

## N.2 Strong

Formale/semantische Reife und operative Nutzerentlastung liefen zeitweise auseinander. FB-20260902-003 ist dafür direkte Owner-Evidence.

## N.3 Strong

Das Projekt erzeugte wiederholt zusätzliche Koordination aus legitimer fachlicher/epistemischer Differenzierung.

## N.4 Strong

PR #108–#116 zeigen einen dokumentierten Lifecycle-Fehler: Owner/User-Research wurde teilweise zu schnell abstrahiert und persistiert.

## N.5 Strong

#119 zeigt eine zweite Fehlerklasse: eine bekannte semantische Differenzierung war vorhanden, wurde aber an einer konkreten Execution-Admission nicht angewendet.

## N.6 Strong

Fehlererkennungssysteme funktionieren teilweise gut: #116 Self-Audit, #117 Counterpilot, Terra Stop und roter Planning-CI-Lauf verhinderten bzw. korrigierten stärkere Folgen.

## N.7 Supported

Die Kombination aus niedrigen Kosten für AI-generierte Struktur und hohen Kosten realer Falsifikation kann Aktivität Richtung Meta-/Strukturarbeit verzerren.

Direkte quantitative Project Evidence dafür fehlt.

## N.8 Supported

Semantische Owner-Struktur und operative Work-Topologie sind nicht dasselbe. Ihre implizite Kopplung erzeugt Koordinationslast.

## N.9 Supported

Das wiederkehrende Muster lässt sich fachlich besser als **socio-technical translation and coordination problem** denn als reines Softwarearchitektur- oder Requirements-Problem beschreiben.

---

# O. Wichtigste Gegenbefunde

1. Die Governance entstand aus realen Fehler- und Qualitätsrisiken.
2. Deterministic Assurance hat konkrete Fehler gefunden.
3. Source-/Evidence-Trennung ist fachlich unverzichtbar.
4. Persistenz ist wegen Restartability notwendig.
5. Domain Plurality macht eine gewisse strukturelle Komplexität unvermeidbar.
6. Es gibt bereits mehrere Mechanismen zur Selbstkorrektur.
7. Der aktuelle Repo-State zeigt lernende Anpassung statt völliger Prozessstarre.
8. Noch ist nicht bewiesen, dass ein alternatives Entwicklungsmodell bei gleicher wissenschaftlicher Sicherheit tatsächlich weniger Gesamtaufwand erzeugt.

---

# P. Offene Forschungsfragen

## P.1 Translation

- An welcher Stelle wird ein Owner Need erstmals in eine Systemstruktur übersetzt?
- Welche Übersetzungen sind reversibel, welche erzeugen sofort path dependence?
- Wie lässt sich empirisch unterscheiden, ob Nichtwissen des Nutzers eine echte Owner-Decision oder eine vom System lösbare Routingfrage ist?

## P.2 Coordination Load

- Wie viele manuelle Handoffs benötigt ein realer Research Slice heute?
- Welche davon tragen fachliches Urteil?
- Welche transportieren nur bereits vorhandene Information zwischen technischen Verantwortungen?

## P.3 Complexity Transfer

- Welche kognitive Last wurde vom Fachproblem in Projekt-/Toolverständnis verschoben?
- Kann Owner Effort pro Forschungsergebnis historisch aus Issues/Chats/PRs approximiert werden?

## P.4 Persistence

- Welche Arten von Zwischenständen wurden später wirklich für Restartability gebraucht?
- Welche wurden primär Anlass weiterer Reconciliation?

## P.5 Feedback Latency

- Wie lange dauert es zwischen Owner Pain, formaler Erfassung und tatsächlicher operativer Entlastung?
- Welche Feedback-Records bleiben lange open?

## P.6 Error Recurrence

- Welche Failure Modes wiederholen sich trotz expliziter Anti-Pattern-Dokumentation?
- Fehlt jeweils Enforcement, observability, passender Trigger oder die richtige Abstraktionsebene?

## P.7 AI-specific Mechanisms

- Wie oft entstehen neue Projektobjekte aus AI-generated interpretations statt aus neuer externer Evidence?
- Wie oft korrigiert der Owner semantische Richtung vs. bloße Details?
- Sind starke Modelle besser in dieser Übersetzungsfunktion oder nur überzeugender?

## P.8 Cross-Repository Generality

Dieser Audit untersucht nur Histo-Orla.

Ob das Muster generisch ist, kann erst sauber bewertet werden, wenn andere Repositories **zunächst unabhängig** mit demselben Analyseprotokoll untersucht werden.

---

# Q. Confidence / Evidence Matrix

| Statement | Primary evidence | Confidence | Counterevidence / limitation |
|---|---|---|---|
| Needs were clear early | #28 G/N/P baseline | high | need presence != complete understanding |
| operational integration lagged | FB-20260902-003, #64 | high | later work may already improve it |
| governance can create burden | #70, #64, feedback | high | governance also prevents real errors |
| owner signals were over-promoted | #116 + PR #110/#111 | high | not every abstraction was wrong |
| readiness assumptions caused #119 stop | #53/#119 handoff history | high | fail-closed system caught it |
| local verification != utility | owner feedback + external HCD | high | no quantitative owner-throughput baseline |
| specialization creates coordination cost | owner topology + Coordination Theory | medium-high | exact Histo-Orla cost not measured |
| AI coherence encourages meta-structure | #116 + process history | medium | direct causal AI experiment absent |
| persistence increases path dependence | PR cluster / reconciliation work | medium-high | persistence also protects handoff |
| pattern is generic across projects | user reports other repos | unresolved | other repos not yet independently audited |

---

# R. Externe Referenzen / Research Register

1. ISO/IEC/IEEE DIS 29148, Systems and software engineering — Requirements engineering.  
   https://www.iso.org/standard/94091.html

2. ISO 9241-210, Human-centred design for interactive systems.  
   https://www.iso.org/standard/52075.html

3. Malone, T. W.; Crowston, K. (1994). The Interdisciplinary Study of Coordination. ACM Computing Surveys 26(1), 87–119.  
   DOI: 10.1145/174666.174668

4. Star, S. L.; Griesemer, J. R. (1989). Institutional Ecology, “Translations” and Boundary Objects. Social Studies of Science 19(3), 387–420.  
   DOI: 10.1177/030631289019003001

5. Caccamo, M.; Pittino, D.; Tell, F. (2023). Boundary objects, knowledge integration, and innovation management: A systematic review. Technovation 122, 102645.  
   DOI: 10.1016/j.technovation.2022.102645

6. Lam, D. P. M. et al. (2021). Conceptualising transdisciplinary integration as a multidimensional interactive process. Environmental Science & Policy 118, 18–26.  
   DOI: 10.1016/j.envsci.2020.12.005

7. Stanford Encyclopedia of Philosophy (2026 revision). Scientific Pluralism.  
   https://plato.stanford.edu/entries/scientific-pluralism/

8. Reason, J. (2000). Human error: models and management. BMJ 320, 768–770.  
   DOI: 10.1136/bmj.320.7237.768

9. Rasmussen, J. (1997). Risk management in a dynamic society: a modelling problem. Safety Science 27(2–3), 183–213.  
   DOI: 10.1016/S0925-7535(97)00052-0

10. Cantu, J. et al. (2020). Interventions and measurements of highly reliable/resilient organization implementations: a literature review. Applied Ergonomics 90, 103241.  
    DOI: 10.1016/j.apergo.2020.103241

11. AHRQ PSNet. High Reliability.  
    https://psnet.ahrq.gov/primer/high-reliability

12. Gnoni, M. G.; Saleh, J. H. (2017). Near-miss management systems and observability-in-depth: Handling safety incidents and accident precursors in light of safety principles. Safety Science 91, 154–167.  
    DOI: 10.1016/j.ssci.2016.08.012

13. Horvitz, E. (1999). Principles of Mixed-Initiative User Interfaces. CHI 1999.  
    https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/

14. Horvitz, E. (1999). Mixed-Initiative Interaction. IEEE Intelligent Systems.  
    https://www.microsoft.com/en-us/research/publication/mixed-initiative-interaction/

15. Pirolli, P.; Card, S. (2005). The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis.

16. Marchionini, G. (2006). Exploratory Search: From Finding to Understanding. Communications of the ACM 49(4), 41–46.  
    DOI: 10.1145/1121949.1121979

17. W3C PROV-O Recommendation.  
    https://www.w3.org/TR/prov-o/

19. Becker, J.; Rush, N.; Barnes, E.; Rein, D. (2025). Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.  
    https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf

20. METR (2026). We are Changing our Developer Productivity Experiment Design.  
    https://metr.org/blog/2026-02-24-uplift-update/

21. OpenAI (2026). Why SWE-bench Verified no longer measures frontier coding capabilities.  
    https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/

22. Deng, X. et al. (2025/2026). SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?  
    https://arxiv.org/abs/2509.16941

---

# S. Abschluss ohne Lösungssynthese

## Am stärksten belegt

- Die zentralen Nutzerbedürfnisse waren vorhanden.
- Der operative Research Flow blieb trotzdem hinter der semantischen/assurance-seitigen Reife zurück.
- Wiederkehrende Fehler entstanden an **Übersetzungs-, Koordinations- und Admission-Schnittstellen**, nicht nur innerhalb einzelner Fach- oder Softwarekomponenten.
- Das Projekt besitzt funktionierende Korrekturmechanismen, aber dokumentierte Erkenntnis allein verhindert keine Wiederholung auf einer neuen Schnittstellenebene.

## Wichtigste Gegenbefunde

- Viele Schutzmechanismen waren durch reale wissenschaftliche und AI-spezifische Risiken begründet.
- Weniger Formalisierung ist nicht automatisch besser.
- Mehr Automation ist nicht automatisch besser.
- Die Ursache ist nicht hinreichend durch „LLM schlecht“, „Requirements schlecht“ oder „Governance zu viel“ erklärt.

## Wesentliche Spannungen

- epistemische Trennung vs. operative Integration;
- Restartability vs. Meta-Persistenz;
- Determinismus vs. Forschungsfluss;
- Spezialisierung vs. Koordinationslast;
- AI-Initiative vs. menschliche Authority;
- lokale Verification vs. End-to-End-Utility.

## Größte verbleibende Unsicherheiten

- quantitativer Anteil unvermeidbarer vs. accidental coordination load;
- tatsächliche Zeit-/Korrekturkosten der wiederkehrenden Loops;
- AI-spezifischer Anteil gegenüber allgemeinem Software-/Organisationsdesign;
- Übertragbarkeit auf andere Repositories;
- welche Projektmechanismen das Muster tatsächlich verhindern statt nur dokumentieren.

Dieser Audit erzeugt bewusst **keine Lösung, keine Zielarchitektur und keine Entwicklungspriorität**. Er schafft eine Researchgrundlage für spätere Vergleiche und unabhängige Cross-Case-Analyse.
