# Review #87 – wissenschaftliche und repo-methodische Prüfung von #86

**Work Owner:** #87  
**Pilot Owner:** #86  
**Review-Branch:** `pilot/explorative-research-network-20260907`  
**Status:** `review-complete / candidate-dispositions / no-requirement-or-method-promotion`  
**Reviewdatum:** 2026-09-07  
**Reviewbasis:** frischer GitHub-Zustand; keine Rekonstruktion des Ursprungs-Chats.

## Reviewgrenze und Authority

Dieses Review bewertet den Pilot #86 gegen den frisch gelesenen persistierten Zustand von `main`, die aktuellen Work Owner und – nur für generische Wissensarbeitsmechanismen – `esany/Wissensarbeit`.

Authority-Reihenfolge für dieses Review:

1. `AGENTS.md`, #45 und `docs/research/source-identity-protocol.md`;
2. accepted Requirements unter #42 einschließlich `requirements-extensions.md`;
3. fachliche Method Truth unter #60;
4. kanonische Research-/Architecture-Contracts, insbesondere #41, #50, #61, #63;
5. reale Live-Research-/Workflow-Evidence aus #46/#47/#63;
6. Pilot #86 und seine Branch-Artefakte als Candidate;
7. `esany/Wissensarbeit` nur für generische Lifecycle-/State-/Integration-/Competence-/Learning-Mechanismen, nicht für historische oder archäologische Fachmethodik.

`PROJECT_STATE.md` ist ein Snapshot vom 2026-09-03 und wird für jüngere Pilotarbeit nicht als alleinige aktuelle Authority behandelt. Die jüngeren Issues #85–#89 und der Pilotbranch sind daher zusätzlich frisch gelesen worden.

---

# Rekonstruktion vor Bewertung

## A. Welches reale Need/Pain/Goal führte zu #86?

Der persistierte Zustand zeigt **nicht** primär einen Need für einen Graphen, eine neue Ontologie oder einen neuen Case-Typ. Der reale Pain ist enger:

- heterogenes Material kann zunächst vorliegen, bevor eine stabile Forschungsfrage feststeht;
- dieselbe Quelle/Instanz/Beobachtung kann später für verschiedene Fragen relevant werden;
- Analyse erzeugt neue Fragen und verändert Synthesen;
- Synthesen und Überblickssichten erzeugen neue Detailprüfungen;
- räumlicher/zeitlicher Maßstab und führende Fachkompetenz können sich verschieben;
- dabei dürfen Evidenzidentität, Provenienz, Unsicherheit, Methodengrenzen und Restartability nicht verloren gehen;
- frühere Pilot-/Workflow-Friktionen zeigen zusätzlich, dass statische Strukturierung leicht das eigentliche Erkenntnisziel ersetzt.

Dieser Need ist bereits in mehreren älteren Histo-Orla-Strängen sichtbar: #46 arbeitet quellen- und fragestellungsgeführt mit wachsendem Suchinventar; #47 führt eine eigene Quellenlogik bei gemeinsamem Source Ledger; #61 beschreibt seit 2026-09-02 ausdrücklich einen iterativen Zyklus aus Research Questions/Suchinventar → Quelle → Source/Instance/Findspot → Observation/Finding → neue Namen/Begriffe/Fragen → nächste Runde → Hypothese/Synthese; #63 dokumentiert zusätzlich reale Friktion durch zu statische Modulbildung.

## B. Was behauptet der Pilot?

Der Pilot behauptet als Arbeitshypothese:

- ein gemeinsamer provenance-sicherer Research-/Evidence-State ist primär;
- Forschungsfragen sollen diesen State referenzieren, nicht besitzen;
- Fragen sollen als flexible Linsen/temporäre Arbeitszuschnitte funktionieren;
- derselbe Forschungszustand soll mehrere abgeleitete Views/Synthesen tragen;
- Analyse↔Synthese und Überblick↔Detail sind rekursiv;
- Scale Shift und Kompetenzrouting können sich während der Arbeit ändern;
- Frageänderungen könnten mit `split | fuse | reframe | supersede | defer` nachvollziehbar werden;
- Relationstypen sollen epistemische Unterschiede sichtbar halten.

## C. Was behauptet der Pilot ausdrücklich nicht?

Der Pilot behauptet ausdrücklich **nicht**:

- eine historische Kontinuität zwischen den heterogenen Ranis-/Orlatal-Schichten;
- eine Masterfrage zur Ilsenhöhle/Ranis;
- eine lineare Pipeline;
- einen Graphdatenbank-, Ontologie-, Agenten- oder neuen Backend-Bedarf;
- dass Museumslabels aktuellen Forschungsstand wiedergeben;
- dass Nutzerfotos die fotografierten materiellen Objekte sind;
- dass OCR/unsichere Lesung Originalwortlaut ist;
- dass Views/Synthesen neue Evidence Stores werden;
- dass Pilotbegriffe bereits accepted Requirements oder Method Truth sind.

Diese Non-goals sind wissenschaftlich sinnvoll und überwiegend mit bestehender Governance konsistent.

## D. Herkunftstypen der Pilotbestandteile

| Bestandteil | Herkunftstyp | Authority |
|---|---|---|
| heterogener Ranis-/Orlatal-Materialeingang | reale Nutzung / Pilot-Stressfall | Case-/Workflow-Evidence; historische Einzelbehauptungen nicht automatisch validiert |
| Source/Representation/Instance/Derivative/Findspot-Trennung | bestehende Histo-Orla-Semantik | bindend über #45, Source-Identity-Protokoll, #42/#50 |
| Observation/Finding/Interpretation/Hypothese/Synthese-Trennung | bestehende Histo-Orla-Semantik | accepted/validated über #41/#42; Method Truth domänenspezifisch #60 |
| gemeinsamer Research State | bestehende Histo-Orla-Semantik | accepted Requirement + working Architecture Contract (#42/#50) |
| Research Question als Nicht-Eigentümer von Evidenz | weitgehend bestehende Semantik, als Pilot neu formuliert | Candidate-Formulierung; kompatibel mit one fact/one canonical home und #46/#47 |
| persistentes `Research Module` als eigene strukturelle Einheit | Pilot-Hypothese | keine Authority; durch jüngeres Owner-Feedback #63 ausdrücklich zu challengen |
| `split/fuse/reframe/supersede/defer` als eigener Question-Lifecycle | Pilot-Hypothese / teilweise generisches Integrationsvokabular | keine Histo-Orla-Question-Lifecycle-Authority |
| modulbezogenes Kompetenzrouting | neue Benennung eines bestehenden Mechanismus | fachlich bereits CAP-02/REQ-EPI-001/#60/#61; Begriff `module` nicht nötig |
| sechs explizite Relationsschichten | Pilot-Hypothese / methodischer Candidate | Teilsemantiken existieren; vollständige Taxonomie nicht akzeptiert |
| rekursives Analyse↔Synthese / Überblick↔Detail | bestehende Histo-Orla-Method-/Workflow-Semantik | CAP-08/16/17; #60/#61 |
| Scale Shift | bestehende Histo-Orla-Semantik | CAP-13, REQ-SPAT-001, RQ-C4 |
| Views als Projektionen | bestehende Histo-Orla-Semantik | CAP-17, REQ-UX-001/003, #50; generisch BB-DERIVE |
| Friktions-/Learning-Log | organisatorischer Pilot-Candidate | case-spezifisch sinnvoll; Product-/Workflow-Evidence unter #63, keine historische Evidenz |
| mögliche generische Wissensarbeit-Aussage | Generic-Fit-Candidate | nur nach Wiederholbarkeit; aktuelle Blocks decken Mechanismen bereits |

## E. Authority der fraglichen Teile

Wichtigster adversarialer Befund: #86 ist **nicht** der erste persistierte Ort, an dem iterative, rekursive und fragenveränderliche Research Work beschrieben wird. #61 hatte dies bereits am 2026-09-02 als Live-Pilotschnitt formuliert und ausdrücklich gegen vorhandene Requirements/Contracts eingeordnet.

Noch wichtiger: #63 enthält am 2026-09-03 einen expliziten `NOT PASS` aus Owner-/Workflow-Feedback zum früheren „modularen Forschungs- und Suchinventar“. Dort wird das Modulkonzept als Leitkonzept für U2 als zu statisch demotiert. Der als passfähig bezeichnete Arbeitsmodus lautet:

`Quelle → Aussage → Reichweite → Unsicherheit → Anschlussfrage → nächste Prüfspur`.

Das ist Product-/Workflow-Evidence, keine historische Evidenz. Es verbietet nicht jede informelle Gliederung oder jede Forschungsfrage. Es macht aber ein neues persistentes `Research Module` als Default-Struktur **beweispflichtig**. Der Pilot darf die ältere Fehlrahmung nicht unter einem eleganteren Modulbegriff wieder einführen.

## F. Welche Pilotbegriffe sind wahrscheinlich nur neue Namen?

- `shared evidence/research state` → Canonical Research State (#42/#50);
- `question as lens` → Work Context / aktuelle Research Question / Research Hook, die auf denselben State referenzieren (#46/#61);
- `module competence routing` → problem-/claim-/work-context-bezogenes Expertise Routing (CAP-02, #60/#61);
- `derived views` → CAP-17 / REQ-UX-001/003 / #55 / BB-DERIVE;
- `recursive research network` → bereits beschriebene iterative Source-/Question-/Evidence-Demand-Schleife in #46/#61;
- `scale shift` → CAP-13 / REQ-SPAT-001;
- mehrere der Question-Operationen → teilweise normale Git-/Work-Item-History bzw. generische `fuse/refine/reframe/supersede/defer`-Integrationsdispositionen in `Wissensarbeit`, nicht automatisch ein wissenschaftlicher Question-Lifecycle.

---

# Executive Verdict

## `reframe`

Der Pilot sollte **nicht** als neues „exploratives Forschungsnetz“- oder `Research Module`-Modell fortgeführt werden. Sein wissenschaftlich tragfähiger Kern ist kleiner:

> Ein gemeinsamer provenance-sicherer kanonischer Research State wird durch wechselnde, referenzierende Forschungsfragen/Work Contexts, fachlich kontrollierte Scale Shifts und abgeleitete Views benutzt. Neue Quellenbefunde können Fragen, Scope, Methode, Kompetenzbedarf und Synthesen verändern, ohne die Evidenz umzuschreiben oder zu duplizieren.

Diese Kernfähigkeit ist in Histo-Orla bereits zu einem großen Teil als Capability, Requirement, Method-/Work-Context-Contract und Live-Workflow vorhanden. Die Restfrage ist **Operationalisierung und reale Kompositionsfriktion**, nicht die Einführung einer neuen wissenschaftlichen Ontologie.

Der Pilot besitzt dennoch Wert als realer Stresstest, weil Ranis/Orlatal heterogene, multiskalige und fachlich wechselnde Forschung erzwingt. Dieser Wert bleibt erhalten, wenn der Pilot auf einen kleinen Falsifikationstest reduziert wird: Kann der bestehende State tatsächlich dieselbe Evidenz unter wechselnden Fragen wiederverwenden, ohne manuelle Duplikation, Scope-/Method-Drift oder Verlust?

---

# Was der Pilot richtig erkannt hat

1. **Evidenz darf nicht einer Forschungsfrage gehören.** Das folgt aus one fact / one canonical home, Source Identity und dem gemeinsamen Source Ledger von #46/#47.
2. **Ergebnisoffenheit ist notwendig.** #42 erlaubt `unresolved`, Hypothese, Research Hook und konkurrierende Interpretation; #60/#61 erlauben Exploration bei Method Debt.
3. **Analyse und Synthese sind rekursiv.** #60 beschreibt die Erkenntniskette von quellenkritischer Beobachtung über Befundkomplex und konkurrierende Hypothesen zur problemorientierten Synthese, ohne automatische Promotion; #61 beschreibt die Rückschleife zu neuen Fragen/Evidence Demand.
4. **Überblick und Detail müssen reversibel aufeinander verweisen.** CAP-17 und die progressive Leselogik unter #60 verlangen genau diesen Drill-down.
5. **Scale Shift ist eine fachliche Forschungsentscheidung.** CAP-13/REQ-SPAT-001 verbieten stillen Maßstabswechsel und moderne/statische Raumcontainer.
6. **Kompetenzen können sich mit dem konkreten Problem ändern.** CAP-02, REQ-EPI-001 und #60/#61 unterscheiden leading/controlling Domains und Method Applicability.
7. **Views dürfen keine zweite Wahrheit werden.** CAP-17, REQ-UX-001/003, #50 und `Wissensarbeit` BB-DERIVE decken dies bereits.
8. **Ranis/Orlatal ist ein guter Stressfall**, sofern der Case keine historische Kontinuität behauptet und die tatsächlichen Quellen-/Instanzgrenzen erhalten bleiben.
9. **Persistenz ist nicht Promotion.** Dies ist sowohl Histo-Orla- als auch `Wissensarbeit`-Grundregel.

---

# Was bereits in Histo-Orla vorhanden ist

| Pilotidee | vorhandener Mechanismus | Referenz | Deckung |
|---|---|---|---|
| gemeinsamer provenance-sicherer Research State | Canonical Research State / portable curated state | CAP-20; REQ-STATE-001; #50 | vollständig als Responsibility/Requirement |
| Source/Representation/Instance/Derivative/Findspot | Source Identity + inspected-instance control | CAP-04/05; REQ-SRC-001..004; #45; Source-Identity-Protokoll; #50 | vollständig als wissenschaftliche Invariante |
| Observation/Finding/Interpretation/Hypothese/Synthese getrennt | Evidence Layering + semantic research states | CAP-08/10/16; REQ-EPI-004/006; REQ-RSCH-001; REQ-SYN-002 | weitgehend vollständig |
| Material kann vor stabiler Frage aufgenommen werden | source-driven iterative research + Research Hooks | #46; #61; REQ-RSCH-001/002 | vollständig für Exploration, bei consequential work weiter Work Context nötig |
| Frage referenziert Evidenz statt sie zu besitzen | shared source ledger / one fact one home / Work Context references | AGENTS; #46/#47; #50/#61 | semantisch vollständig; kein neues Module-Objekt nötig |
| Frage/Scope können sich verändern | Work Context + Research Hook + Git/Issue history; offene Exploration | #61; REQ-EPI-004/006; REQ-RSCH-001 | funktional vorhanden, eigener Question-Lifecycle nicht bewiesen nötig |
| Kompetenzrouting pro aktuellem Problem | Expertise Routing + Method Truth/Conformance | CAP-02; REQ-EPI-001; #60/#61 | vollständig als Responsibility, konkrete Domain Profiles teils noch Candidate |
| Scale Shift | Temporal/Multi-Scale Context | CAP-13; REQ-SPAT-001; RQ-C4-01/03 | vollständig als Invariante |
| Ko-Präsenz ≠ historische Relation | proxy/context vs historical relation | CAP-12; REQ-REL-001; RQ-C6-03 | vorhanden, teils working-validated |
| rekursives Analyse↔Synthese | Transdisciplinary Synthesis + Method chain | CAP-16; REQ-SYN-002; #60/#61 | vollständig als Zielsemantik |
| rekursives Überblick↔Detail | Human-readable Audit / progressive views | CAP-17; REQ-UX-001/003; #60 | vollständig als Zielsemantik |
| Views über denselben State | derived views, no second truth | CAP-17; #50/#55; REQ-UX-001/003 | vollständig als Responsibility |
| neue Evidenz verändert Suchinventar/Fragen | iterative Evidence Demand / live source loop | REQ-RSCH-002/004; #46; #61 | explizit vorhanden |
| Lern-/Friktionsrückfluss | Product-/Workflow feedback + traceability | REQ-TRACE-001; #63 | vorhanden |
| generische Rekombination/Integration | Systemic Integration / Reconciliation | `Wissensarbeit`: BB-INTEGRATE, lifecycle, `system/reconciliation.json` | generisch bereits vorhanden; keine historische Method Authority |

## Besonders entscheidende Vorbefunde

- #46/#47 verwenden bereits **gemeinsame Source Identity** über unterschiedliche Research Owner/Fragen hinweg. Damit ist die Kernthese „dieselbe Evidenz darf mehreren Fragen dienen“ nicht neu.
- #61 beschreibt bereits vor #86 einen iterativen, rekursiven Quellen-/Fragen-/Evidence-Demand-Zyklus und ordnet ihn vorhandenen Requirements/Contracts zu.
- #63 dokumentiert, dass ein **Modul als Leitkonzept** in realer U2-Nutzung gerade nicht passte. Das ist direkte Falsifikation eines zu starken `Research Module`-Rahmens.

---

# Wo echte zusätzliche Friktion bleibt

Nach Abzug des Bestehenden bleiben nur engere, empirisch zu prüfende Restfragen:

1. **Low-burden Rekombination im tatsächlichen Arbeitsbetrieb.** Die Semantik ist vorhanden; offen ist, ob ein Research Owner dieselbe Source/Observation/Finding-Identität praktisch unter wechselnden Fragen referenzieren kann, ohne manuelle Markdown-Duplikation oder Chat-Orchestrierung. #63/FB-20260902-003 zeigt reale Delivery-Friktion, aber kein neues wissenschaftliches Requirement.
2. **Question-/Scope-Reframe ohne stale Interpretation.** Ein realer Reframe kann alte Findings in einem anderen Scope oder mit anderer Method Application stehen lassen. Zu prüfen ist, ob vorhandener Work Context + History + Research Hooks dies ausreichend sichtbar machen. Erst wenn nicht, entsteht ein enger State-/Trace-Candidate.
3. **Multi-Method Composition.** #60/#61 führen Method Applicability und Multi-Method Composition weiterhin als fachmethodische Research-Frage. Das ist keine Rechtfertigung für ein neues Forschungsnetzmodell.
4. **Nichttextliche / archäologische / naturwissenschaftliche Evidenz.** Der Pilot darf den dokumentzentrierten Pfad `source → representation → ...` nicht universal auf materielles Objekt, Grabungsbefund, Geologie oder naturwissenschaftliche Messung projizieren. CAP-15/REQ-RSCH-004 erlauben heterogene Evidenzachsen; die konkrete Method Truth und Modellanwendung für Paläolithikum, Geoarchäologie, Taphonomie, Paläoanthropologie usw. ist nur soweit belastbar, wie #60 bzw. qualifizierte Fachvalidierung dies trägt.
5. **Fresh-context Evidence Availability.** Für #88 genügt es nicht, dass Nutzerfotos oder Publikationen benannt sind. REQ-STATE-003 verlangt, dass ein neuer autorisierter Context die konkret benötigte Instanz öffnen kann oder einen Availability-Blocker erkennt.

Diese Punkte sind Operationalisierungs-/Method-Friktionen. Keiner verlangt derzeit einen neuen generischen Research-Graph oder Building Block.

---

# Wissenschaftliche Risiken

## Provenienz und Evidence Layering

- **Nutzerfoto ≠ fotografiertes materielles Objekt.** Foto/Datei ist konkrete Repräsentation/Instanz; das Objekt und dessen museale/archäologische Identität benötigen eigene Evidenz.
- **Museumslabel ≠ aktueller Forschungsstand.** Es kann als museale/forschungsgeschichtliche Aussage untersucht werden, nicht als stiller Konsensbeleg.
- **OCR/unsichere Lesung ≠ Originalwortlaut.** OCR bleibt Derivat; Unsicherheit und Fundstelle müssen erhalten bleiben.
- **historische Ausstellungsaussage ≠ heutige wissenschaftliche Position.** Zeit-/Autor-/Institution-/Ausstellungskontext muss erhalten bleiben.
- **Fragenübergreifende Wiederverwendung ≠ unabhängige Bestätigung.** Dieselbe Quelle in zwei Fragen bleibt dieselbe Evidenz; CAP-09/Source Dependence darf durch Rekombination nicht verwischt werden.

## Ergebnisoffenheit

Die Pilotstruktur wird wissenschaftlich problematisch, sobald sie eine feste Liste von Modulen, Relationstypen oder Operationsereignissen verlangt. Ergebnisoffenheit bedeutet auch, dass eine neue Beobachtung **keine** neue Forschungsfrage oder Relation erzeugen muss. `unresolved`, `not-assessable`, `note for later` und „für diese Frage nicht relevant“ sind legitime Zustände.

## Relationssemantik

Die Relationstypen dürfen nicht als Future-Proof-Ontologie formalisiert werden.

| Relation | bereits vorhandene Semantik | persistieren? | Reviewdisposition |
|---|---|---|---|
| Überlieferung / Provenienz | #45, Source-Identity-Protokoll, CAP-04/09, #50 | ja, wenn für Identität/Abhängigkeit/Findspot relevant | vorhandene Mechanismen nutzen |
| räumlich / chronologisch | CAP-13, REQ-SPAT-001 | nur als fachlich qualifizierter Kontext/Bezug, nicht als historische Kante | vorhandene Mechanismen nutzen |
| historische Relation | CAP-12, REQ-REL-001 | nur evidenzbasiert und claim-spezifisch | vorhandene Mechanismen nutzen |
| typologisch / vergleichend | CAP-15, Scale-Shift-/Comparanda-Logik | oft als Analyse-/Methodenkontext ausreichend | keine generische Edge-Klasse vorab |
| researcher-asserted / interpretativ | CAP-08/10/16, Hypothese/Interpretation | ja, wenn materiell – aber als Hypothese/Interpretation mit Provenienz | keine Gleichsetzung mit historischer Relation |
| Research-Relevance / used-in-question | Work Context / Research Hook / Referenz auf State | Referenz genügt, solange realer Test nichts anderes zeigt | keinen neuen Relationstyp vorab |

Risiko einer umfassenden Relationstaxonomie: sie erweckt Vollständigkeit, zwingt ambige Beziehungen in Klassen und erzeugt administrative Arbeit. RQ-C6-03 verlangt Schichtentrennung; es verlangt **keine** vollständige Ontologie.

## Scale Shift

Scale Shift ist zulässig, aber nur mit fachlichem Trigger. Zu kontrollieren:

- Objekt → Sammlung/Vitrine ist Sammlungs-/Museumsbezug, nicht automatisch historischer Funktionszusammenhang;
- Fundstelle → Ranis ist räumlicher Kontext, nicht automatisch gemeinsamer historischer Prozess;
- Ranis → Orlatal ist eine Maßstabserweiterung, die durch Vergleichs-, Landschafts-, Überlieferungs- oder andere fachliche Fragen begründet werden muss;
- Orlatal → regionaler Vergleich braucht kontrollierte Comparanda und Methode;
- zeitliche Nachbarschaft oder gleiche Objektklasse erzeugt keine Beziehung;
- unterschiedliche Evidenztypen dürfen nicht in einen gemeinsamen Confidence-Wert nivelliert werden.

## Method Authority

Kompetenzrouting muss claim-/problem-/quellenbezogen erfolgen, nicht über Rollenlabels. Für die im Stressfall genannten Disziplinen gilt:

- **leading** ist die Fachdomäne, deren Methode die konkrete Aussage prüft;
- **controlling** sind Domänen, die zentrale Inferenz-/Quellen-/Messgrenzen kontrollieren;
- Method Status kommt aus #60 bzw. einschlägiger SOTA-/Fachvalidierung, nicht aus einem Pilotrecord;
- wenn für Paläolithikumsforschung, Geoarchäologie, Taphonomie, Paläoanthropologie, Archäogenetik/Proteomik/Isotopenmethoden oder Bauarchäologie kein hinreichend operationalisiertes Histo-Orla-Profile vorliegt, bleiben consequential Aussagen `candidate | unresolved | external-validation-required`;
- mehrere AI-Rollen sind keine unabhängige Fachvalidierung.

## Zusätzliche Failure Modes

Neben den im Pilot genannten sind besonders zu ergänzen:

1. **module reification / authority drift** – ein temporärer Fragenzuschnitt wird zum quasi-kanonischen Besitzer des Research State;
2. **question-operation cargo cult** – ein Eval erzwingt `split/fuse/...`, obwohl reale Forschung keinen solchen Schritt benötigt;
3. **relation-class completeness illusion** – eine Liste von Relationsarten erscheint vollständig und verdrängt `unresolved`;
4. **scope laundering via view** – eine View erweitert Corpus/Zeitraum/Raum, ohne Search Boundary/Scale-Trigger anzupassen;
5. **method-status laundering** – `specialist-needed` oder ein Disziplinlabel wird mit tatsächlicher Method Applicability verwechselt;
6. **question-history duplication** – separater Question-Lifecycle wird zweiter Truth Store neben Work Context, Issue-/Git-History und Research Hooks;
7. **stale-scope interpretation** – nach Reframe wird ein altes Finding unter neuer Fragestellung gelesen, ohne ursprünglichen Scope/Method Application zu erhalten;
8. **synthetic recombination proof** – zwei künstlich konstruierte Fragen um dieselbe Quelle beweisen keinen realen Nutzerwert;
9. **networkability selection bias** – ein kuratierter Ranis-Ausschnitt überbetont vernetzbare Materialien; fehlende Relation darf nicht als fehlender Forschungswert gelten;
10. **document-centric overreach** – archäologisches Objekt/Befund oder naturwissenschaftliche Messung wird still als bloße Variante einer Textquelle modelliert.

---

# Forschungsfragen als Linsen – Prüfung der Candidate-Operationen

Die Aussage **„Forschungsfrage ist Linse, nicht Evidenzcontainer“** ist methodisch sinnvoll, wenn sie als Negativregel verstanden wird: Die Frage besitzt die Evidenz nicht. Sie rechtfertigt jedoch noch keinen neuen `Research Module`-Artefakttyp.

| Operation | wissenschaftlich sinnvoll? | bereits gedeckt? | eigene persistierte Semantik jetzt nötig? | Urteil |
|---|---|---|---|---|
| `split` | ja, wenn eine Frage fachlich zu breit/heterogen wird | Work-Item-/Question-Reframing, neue Hooks, Git history | nein belegt | defer |
| `fuse` | manchmal, aber hohes Risiko, Scope/Methodenunterschiede zu glätten | Synthese/Integration kann Bezüge herstellen, ohne Questions zu verschmelzen | nein | defer |
| `reframe` | zentral für Ergebnisoffenheit | Problem Translation, Work Context, Issue/Git History | voraussichtlich keine eigene Klasse | defer als formaler Question-Op |
| `supersede` | sinnvoll für überholte Fragen | Status-/History-/Supersession-Pattern vorhanden | kein eigener Question-Lifecycle bewiesen | defer |
| `defer` | sinnvoll | Research Hook / open question / generische Integration `defer` | keine neue Semantik nötig | defer als formaler Question-Op |

Wichtig: Das **Verhalten** ist teilweise schon möglich; die Disposition `defer` bezieht sich auf die Pilotidee eines eigenen persistierten Question-Operationsmodells.

---

# Generic Fit gegen `esany/Wissensarbeit`

Der frische Stand von `Wissensarbeit` enthält bereits:

- `BB-STATE` – Canonical State;
- `BB-CONTEXT` – task-/work-item-relevanter Context;
- `BB-COMPETENCE` – situative Kompetenzentdeckung;
- `BB-INTEGRATE` – neue Aspekte gegen den Gesamtzustand dispositionieren;
- `BB-DERIVE` – Views aus canonical state ohne parallele Wahrheit;
- `BB-LEARN` – reale Nutzung/Friktion zurückführen;
- Lifecycle-Dispositions `fuse | refine | reframe | supersede | conflict | reject | defer`;
- `system/reconciliation.json`: materieller Zustand ist erst systemisch integriert, wenn Auswirkungen auf relevante Zustandsflächen explizit dispositioniert sind; `unchanged` ist gültig, Schweigen nicht;
- ausdrückliche Regel: **neue generische Building Blocks benötigen wiederholte reale Friktion**, nicht Architektur-Spekulation.

Disposition des Generic Fit:

- gemeinsamer State / Rekombination / Context / Competence / Views / Learn = **A: bereits gedeckt**;
- historische Relation-, Scale-, Evidence- und Methodensemantik = **B: Histo-Orla-spezifisch**;
- Ranis/Orlatal = **C: zusätzlicher realer Stressfall**;
- ein neuer wiederholbarer generischer Need = **D: derzeit nicht belegt**.

Es ist **kein neuer Building Block** und kein neues generisches Requirement gerechtfertigt.

---

# Disposition Matrix

Jeder wesentliche Pilotbestandteil erhält genau eine Candidate-Disposition.

| # | Pilotbestandteil | Disposition | Begründung / konkrete Repo-Evidenz | vorhandener Mechanismus | wissenschaftliches Risiko | Authority / nächste erlaubte Aktion |
|---|---|---|---|---|---|---|
| 1 | gemeinsamer Research-/Evidence-State | **reuse-existing** | CAP-20, REQ-STATE-001 und #50 definieren bereits denselben kanonischen State | #50 + Source Identity + Evidence Layering | zweiter Truth Store bei parallelem Pilot-Ledger | #50 nur bei realem Responsibility-Gap; im Pilot nur referenzieren |
| 2 | Materialeingang ohne vorab bekannte Forschungsfrage | **reuse-existing** | #46/#61 erlauben source-driven Exploration und Research Hooks vor stabiler Frage | REQ-RSCH-001/002; iterative Source-Loop | „questionless“ wird zum dauerhaften unbounded corpus claim | Material identifizieren/inspektieren; consequential Analyse erhält bounded Work Context |
| 3 | Research Question als Linse statt Container | **reuse-existing** | one fact/one home; #46/#47 teilen Source Ledger; #61 Work Context referenziert Evidence | Work Context / Research Question / Research Hook | Begriff `module` kann Linse reifizieren | Linse als Negativregel behalten; keinen neuen Module-Typ anlegen |
| 4 | Question `split/fuse/reframe/supersede/defer` | **defer** | normales Reframing/History und generische Integrationsdispositionen existieren; kein realer Nachweis für eigenen Question-Lifecycle | Git/Issue History, Work Context, Research Hooks; `Wissensarbeit` lifecycle | Operations-Cargo-Cult, zweiter History-Store | #88 höchstens **einen real auftretenden** Reframe testen; erst Friktion dokumentieren |
| 5 | modulbezogenes Kompetenzrouting | **reuse-existing** | CAP-02, REQ-EPI-001, #60/#61 routen leading/controlling Domains pro Problem/Work Context | Expertise Routing + Method Profile/Application | Rollenlabel als Expertise; Modulbegriff bindet Routing unnötig | als problem-/claim-/work-context-bezogen formulieren; Method Truth #60 |
| 6 | explizite Relationsschichten | **defer** | Provenienz, Proxy/Historical Relation und Scale sind bereits getrennt; vollständige Taxonomie nicht akzeptiert | CAP-09/12/13, REQ-REL-001, RQ-C6-03, #50 | Future-Proof-Ontologie, Zwangsklassifikation | nur vorhandene Relationssemantik nutzen; neue Klasse nur nach konkretem Friktionsbeleg + Domain Review |
| 7 | rekursives Analyse↔Synthese | **reuse-existing** | CAP-08/16, REQ-SYN-002, #60 Erkenntniskette, #61 Iterationszyklus | Evidence Layering + Synthesis | Synthese wird Evidenz / verliert Alternativen | vorhandene Traceability im realen Slice testen |
| 8 | rekursives Überblick↔Detail | **reuse-existing** | CAP-17 und #60 progressive Leselogik mit Drill-down | Derived/Audit Views | Overview erzeugt Scope-/Completeness-Overclaim | #55/#61-Komposition testen, keine neue Struktur |
| 9 | Scale Shift | **reuse-existing** | CAP-13, REQ-SPAT-001, RQ-C4; #47 warnt vor Raumverschmelzung | temporal/multi-scale context | Ko-Lokalität/Kontinuität, moderne Grenzcontainer | Scale-Trigger + Search Boundary im Slice sichtbar machen |
| 10 | Views/Synthesen als Projektionen desselben States | **reuse-existing** | CAP-17, REQ-UX-001/003, #50/#55, BB-DERIVE | Derived Views | zweiter Truth Store / Back-write | zwei abgeleitete Views sind zulässiger Test, sofern rein referenziert/derivebar |
| 11 | Rekombination desselben Materials über mehrere Forschungsfragen | **reuse-existing** | gemeinsames Source Ledger #46/#47 belegt Identität über mehrere Research Owner; one fact/one home | stabile IDs/Refs + Work Context | gleiche Evidenz wird als Mehrfachbestätigung gezählt | im Prototyp nur Referenzwiederverwendung testen, keine Duplikate |
| 12 | Friktions-/Learning-Log | **adapt-case-specific** | #63 besitzt Product-/Workflow-Evidence und REQ-TRACE-001; Pilot kann lokale Friktion sammeln | #63 Feedback/Trace; BB-LEARN | Learning wird historische Evidenz oder Requirement | branchlokal führen; nur wiederholte materielle Friktion an #42/#63 routen |
| 13 | Ranis/Orlatal als Stressfixture | **adapt-case-specific** | #85/#86 liefern realen heterogenen Stressraum; keine generische Authority | bestehende Pilot-/Live-Research-Governance | Fixture wird zur Masterfrage/Corpus-/Kontinuitätsbehauptung | kleinen repräsentativen Ausschnitt verwenden; historische Claims nur über zuständige Fachmethodik |

**Keine** der 13 Positionen ist derzeit `requirement-candidate` oder `generic-learning-candidate`. Das ist ein Ergebnis, kein Mangel: Nach Deduplikation bleibt noch kein ausreichend belegter neuer Requirement- oder Generic-Core-Need.

---

# Minimaler Sollzustand

Die kleinste hinreichende Struktur nach dem Review ist:

```text
bestehender Canonical Research State
  Source / Representation / Inspected Instance / Derivative / Findspot
  Observation / Finding / Interpretation / Hypothesis / Unresolved
  Method-/Work-Context-Provenienz soweit consequential

        ↑ referenziert von

aktuelle Research Question / Work Context
  objective/question
  bounded scope + Search Boundary
  leading/controlling Domains
  applicable Method Profile / Status
  input refs
  offene Research Hooks / nächste diskriminierende Evidenz

        ↓ erzeugt

Findings / Hypothesen / offene Fragen
  zurück in denselben State

        ↓ abgeleitet

Views / Synthesen
  ohne eigenen Truth Store
```

Nicht erforderlich:

- kein `Research Module` als neuer kanonischer Artefakttyp;
- kein Pflicht-`question_id`, wenn vorhandener Work-Owner-/Work-Context-Bezug reicht;
- keine vollständige Question-State-Machine;
- keine Pflichtausführung aller fünf Question-Operationen;
- keine neue Relationsontologie;
- keine neue `network`-Persistenzschicht;
- keine neuen Agentenrollen;
- kein neuer Wissensarbeit-Building-Block.

Der Pilot darf neue persistente Semantik erst hinzufügen, wenn ein realer Slice zeigt: **Mit vorhandenen IDs/Refs, Work Context, Research Hooks, History und Views geht ein materieller Zustand sonst verloren oder wird systematisch falsch.**

---

# Owner / Authority Routing

| offene/kommende Entscheidung | zuständige Authority / Owner |
|---|---|
| Source/Instance/Findspot/Evidence Layering | #45 + Source-Identity-Protokoll; accepted Requirements #42; State-Responsibility #50 |
| historische/archäologische/naturwissenschaftliche Method Truth | #60 + jeweilige Fachdomäne; ggf. unabhängige qualifizierte Fachperson |
| Method Applicability / Multi-Method Composition | #60; Conformance-Folge #61 |
| Work Context / Handoff / Restartability | #61, unter accepted Requirements #42 |
| Derived Views / Audit UX | #55, aus demselben State |
| echter neuer State-Responsibility-Gap | #50, aber nur nach nachgewiesener Friktion |
| neuer/geschärfter accepted Requirement Candidate | #42; Origin aus realer Friktion, keine automatische Promotion |
| Product-/Workflow-Learning und Nutzenfriktion | #63 / REQ-TRACE-001 |
| technische Lösung nach akzeptierter Anforderung | #48/#59, nicht #86/#87 |
| Pilot-Disposition | #86 nach diesem Review |
| Prototype-Ausführung | #88 erst nach Scope-Korrektur gemäß Review |
| spätere Evaluation | #89, aber Evaluationskriterien müssen den reframed Pilot statt das verworfene Module-Modell testen |
| echte Owner-Entscheidung/Blocker | #44 nur falls eine nicht ableitbare materielle Entscheidung entsteht; derzeit kein solcher Blocker |

---

# Empfehlung für #88

## `nur eingeschränkt freigeben`

Der aktuelle #88-Text ist nach diesem Review **zu präskriptiv**. Er verlangt bereits:

- `Research Modules` als Struktur;
- alle fünf Question-Operationen;
- explizite Relationstypisierung;
- Kompetenzrouting „per module“.

Damit würde der Prototyp genau die Hypothese implementieren, die #87 erst falsifizieren soll und die durch #63 teilweise bereits adversarial belastet ist.

### Minimal zulässiger Prototyp

Nur ein kleiner, reversibler Test mit echtem Material:

1. **ein kleiner Ranis/Orlatal-Ausschnitt** mit sauberer Source/Representation/Instance/Observation-Trennung und tatsächlicher Evidence Availability;
2. **dieselbe Source-/Observation-/Finding-ID in zwei unterschiedlichen aktuellen Research Questions/Work Contexts referenzieren**, ohne Kopie;
3. **ein realer source-/statement-led Pfad**:
   `Quelle/Observation → Finding → Synthese-Candidate → Anschlussfrage → nächste Prüfspur`;
4. wenn die reale Arbeit tatsächlich einen Reframe erzeugt, **genau diesen einen** Reframe mit vorhandener Work-/Git-History nachvollziehbar machen; kein künstliches `split/fuse/...`;
5. **ein begründeter Scale Shift** mit explizitem fachlichem Trigger und Grenze `context/comparison ≠ historical relation`;
6. **mindestens ein Kompetenzwechsel oder -handoff**, aber nur soweit ein konkreter Claim unterschiedliche leading/controlling Domain Method benötigt; Method Status sichtbar, ggf. `external-validation-required`;
7. **zwei abgeleitete Views** über denselben State, ohne duplizierte Facts;
8. ein **Friktionslog**, das ausschließlich festhält, was mit den vorhandenen Mechanismen nicht natürlich ging.

### Im Prototyp ausdrücklich nicht zulässig

- keinen neuen `ResearchModule`-Datentyp nur zur Erfüllung von #88;
- keine neue Relationstaxonomie;
- keine Pflicht-Question-State-Machine;
- keine Behauptung, dass ein Graph erforderlich ist;
- keine Domain-Methodik erfinden;
- keine historischen Aussagen aus Museumslabel, Nutzerfoto, OCR oder räumlicher Nähe promoten;
- keinen neuen Requirement-/Architecture-State erzeugen.

#88 sollte vor Ausführung durch einen Scope-Kommentar oder eine Issue-Präzisierung auf diese Reviewgrenze gestellt werden. Das ist Review-/Work-Routing, keine Umsetzung.

---

# Offene Fragen

Nur folgende Fragen sind für den nächsten Schritt noch relevant:

1. Reicht der vorhandene Work Context/Research-Hook-/Git-History-Pfad für **einen realen Question Reframe**, ohne neue Question-Objektsemantik?
2. Sind die für den Minimalprototyp benötigten Ranis-/Orlatal-Instanzen – insbesondere user-provided Fotos – für einen frischen autorisierten Context tatsächlich verfügbar, oder muss REQ-STATE-003 einen Availability-Blocker ausweisen?
3. Welche Domain Method Profiles sind für den gewählten kleinen Ausschnitt tatsächlich `working-method`/`validated-method`, und wo ist nur explorative Candidate-Arbeit oder externe Fachvalidierung zulässig?
4. Zeigt ein nichttextlicher archäologischer/geologischer Gegenstand im Prototyp eine echte Lücke im bestehenden Source-/Evidence-State, oder reicht CAP-15/REQ-RSCH-004 plus domänenspezifische Methodik?

Alles andere sollte erst aus realer Friktion entstehen.

---

# Restartability-Befund

Für **dieses Review** ist #86 ausreichend restartbar: Issue, sieben Branch-Artefakte, Handoff und Review-/Eval-Gate erlauben die Rekonstruktion der Pilot-Hypothese und ihrer Non-goals ohne Ursprungs-Chat.

Nicht belegt ist damit die Restartability der **historischen Ranis-Forschung selbst**. Der #86-Branch ist ausdrücklich ein Modell-/Stressfixture und enthält nicht automatisch alle konkret inspizierbaren Quellenbytes/Instanzen. #88 muss deshalb Evidence Availability real prüfen statt aus der Modellbeschreibung abzuleiten.

---

# Abschlussantwort

> Braucht Histo-Orla tatsächlich ein neues Modell für explorative, hochgradig vernetzte, ergebnisoffene Forschungsarbeit – oder zeigt der Ranis/Orlatal-Fall hauptsächlich, dass vorhandene Research-State-, Question-, Competence-, Integration- und Evidence-Mechanismen anders bzw. konsequenter komponiert werden müssen?

**Reviewantwort:** Histo-Orla braucht nach dem frisch gelesenen Repository-Zustand **derzeit kein neues übergeordnetes Forschungsnetz-/Research-Module-Modell**.

Der Ranis/Orlatal-Fall zeigt hauptsächlich, dass bereits vorhandene Mechanismen konsequenter und mit geringerer manueller Last komponiert und real getestet werden müssen:

`Canonical Research State + Source Identity + Evidence Layering + Work Context/Research Question + Expertise/Method Routing + Scale Shift + Synthesis + Derived Views + Restartability + Use/Learn`.

Die zentrale neue Pilotformulierung „Question = Linse, nicht Evidenzcontainer“ ist als **Negativregel** sinnvoll, aber inhaltlich weitgehend bereits durch one fact / one canonical home, shared Source Identity und Work-Context-Semantik gedeckt. Die zusätzliche strukturelle Idee eines `Research Module` ist dagegen nicht belegt und steht in Spannung zu jüngerem realem Owner-Feedback aus #63.

Deshalb: **Pilot reframe, #88 nur eingeschränkt freigeben, keine neue Requirement-/Method-/Architecture-Promotion.** Ein späterer enger Candidate ist erst zulässig, wenn der Minimalprototyp einen konkreten, wiederholbaren Zustand nachweist, der mit den vorhandenen Mechanismen nicht verlustfrei und restartbar geführt werden kann.
