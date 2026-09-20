# Self-Audit 2026-09-20 – Chat → User Research → Repo-Operationalisierung

**Status:** `critical self-review / corrective audit / no new Requirement or Method authority`  
**Scope:** vollständiger in diesem Arbeitskontext verfügbarer Gesprächsverlauf zu Wissensraum, Langdiachronie, multiperspektivischen Projektionen, Quellenkontext, Zeit/Raum/Relation, Widerspruch und Modellpluralität; zugehörige Repo-Interventionen insbesondere PR #108–#115 und Kommentare unter #28/#42/#50/#60/#63/#64/#92.  
**Primary review owner:** #64 Product-/Research-Value Audit  
**Governance:** `AGENTS.md`, #10, #23, #42, #45, #48, #60, #63, #92  
**Important boundary:** Dieses Artefakt bewertet die Qualität der Assistenz-/Operationalisierungsarbeit. Es schafft keine neue historische Wahrheit, keine fachwissenschaftliche Method Truth, keine Requirement Authority und keine Architekturentscheidung.

---

## 1. Arbeits-Prompt, der für diesen Audit verwendet wurde

> **Rolle:** Unabhängiger kritischer Reviewer der eigenen Histo-Orla-Arbeit.  
> **Auftrag:** Rekonstruiere den gesamten verfügbaren Chat und alle dadurch ausgelösten Repo-Änderungen. Trenne strikt Nutzer-/Owner-Beobachtung, meine Interpretation, wissenschaftliche Einordnung, Capability-/Requirement-Kandidat, technische Hypothese und tatsächlich akzeptierten Repo-State.  
> **Prüfe pro Intervention:**  
> 1. Was hat der Owner tatsächlich gesagt bzw. als Ziel/Pain/Mental Model signalisiert?  
> 2. Was habe ich daraus zusätzlich inferiert oder interpoliert?  
> 3. War diese Inferenz durch bestehende Requirements, SOTA, Domain Method oder mindestens zwei reale Workflows gedeckt?  
> 4. Habe ich Unsicherheit, konkurrierende Lesarten und mögliche Gegenhypothesen sichtbar gehalten?  
> 5. War der gewählte kanonische Ort/Lifecycle-Owner korrekt?  
> 6. Habe ich User Research zu früh zu Scope, Requirement, Datenmodell oder Architektur promoted?  
> 7. Habe ich bestehende Pilotbefunde zu früh generalisiert?  
> 8. Habe ich externe SOTA-/Referenzmodelle nur als Challenge verwendet oder still als Histo-Orla-Semantik übernommen?  
> 9. Hat die Persistenz den State vereinfacht oder neue Meta-/Artefaktkomplexität erzeugt?  
> 10. Welche Intervention ist `sound`, `useful-but-premature`, `methodologically-wrong`, `incomplete` oder `superseded`?  
> **Bewertungsrahmen:** #10 Discovery→SOTA→Capability→Requirement→Architecture; #45 Domain/Evidence/Inference/Terminology/Provenance/Falsification; #60 Domain Method precedence; #64 Value-before-governance-complexity; #92 no pilot/generalization without disposition; Requirements Engineering; transdisciplinary integration/reflexivity; scientific pluralism; provenance/evidence modelling.  
> **Output:** klare Fehleranalyse, valide Befunde, nicht validierte Hypothesen, konkrete no-loss Korrekturen, Stop-Regeln für künftige Owner-Kommunikation und einen restartbaren Handoff.

Dieser Prompt wird in den folgenden Abschnitten direkt ausgeführt.

---

## 2. Methodische Referenzpunkte für die Selbstprüfung

### 2.1 Repo-interne bindende Maßstäbe

Bereits vor diesem Chat galten:

- #10: Discovery muss **Need/Pain/Workflow Map, keine Featureliste** erzeugen; Technik folgt erst nach Fach/SOTA/Capability/Requirement.
- #28/#29: Beobachtung, rekonstruierter Workflow und Inferenz sind zu trennen.
- #41: Live-Research-Candidates werden nur promoted, wenn SOTA/Risk/Cross-Use-Case sie stützen.
- #42: accepted Requirements entstehen nicht aus Dev-/Architecture-Convenience; Research Owner besitzt Ziel/Nutzen/Pain, nicht Method Truth.
- #45: Domain fit, Evidence fit, Inference fit, Terminology fit, Provenance fit und Falsification/Challenge.
- #48: reversible Technik darf früh gewählt werden; wissenschaftliche Bedeutung nicht.
- #60: Vision/Nutzer-Pain → Fachdomäne → SOTA → Method Profile → reale Quellen/Counterexamples → erst dann Requirement/Architecture.
- #64: Hauptrisiko ist bereits Meta-/Governance-Komplexität; generische Abstraktion erst bei realen Consumers.
- #92: `freeze on invention`, Pilot ≠ Generic Promotion, keine neue Meta-Schicht, R3/R5 erst durch reale Slices.

### 2.2 Externe Challenge-Referenzen – keine Histo-Orla-Authority

Diese Quellen werden hier nur als unabhängige methodische Gegenprobe verwendet:

- ISO/IEC/IEEE 29148: Requirements sind präzise Ausdrücke von Needs/Constraints; Requirements Elicitation ist ein systematischer Prozess zur Identifikation von Nutzer-/Kundenbedürfnissen.  
  https://www.iso.org/standard/72089.html  
  https://www.iso.org/standard/94091.html
- td-net / Pohl et al.: transdisziplinäre Forschung integriert verschiedene Perspektiven; Problem Framing, Knowledge Co-Production und Evaluation sind iterativ und reflexiv.  
  https://en.transdisciplinarity.ch/transdisciplinarity/principles-of-transdisciplinary-research/goals-and-principles  
  https://en.transdisciplinarity.ch/transdisciplinarity/how-is-tdr-done/research-process
- Polk 2015: Multiple Framings, Integration, Reflexivity und Usability sind eigene Herausforderungen; Co-Produktion ist kein linearer Requirements-Transfer.  
  https://doi.org/10.1016/j.futures.2014.11.001
- Lam et al. 2021: Integration kann ein offener Lernprozess ohne vorbestimmtes Ergebnis sein; Konsens ist nur eine Möglichkeit, Pluralität darf erhalten bleiben.  
  https://doi.org/10.1016/j.envsci.2020.12.005
- Scientific Pluralism: verschiedene Modelle, Methoden und Repräsentationen können partiell, interessengebunden, komplementär oder auch inkonsistent sein; Einheitlichkeit ist kein Default-Ziel.  
  https://plato.stanford.edu/entries/scientific-pluralism/
- W3C PROV-O: Provenienz unterscheidet Entity, Activity und Agent und macht Herleitung/Transformation explizit.  
  https://www.w3.org/TR/prov-o/
- CIDOC CRM: historische Beschreibung trennt Persistent Items, Events/Temporal Entities und Spacetime; Zeitgrenzen können unscharf sein.  
  https://cidoc-crm.org/sites/default/files/Documents/cidoc_crm_version_7.1.3.html
- World Historical Gazetteer v4: source-backed Attestations können widersprüchliche Namen, Geometrien, Timespans und Relationen mit Provenienz/Unsicherheit parallel tragen.  
  https://docs.whgazetteer.org/content/v4/user-guide/getting-started/concepts.html

**Wichtige Begrenzung:** Diese Referenzen bestätigen einzelne Problemklassen und Modellierungsrisiken. Sie legitimieren **keine** automatische Übernahme ihrer Ontologien oder Datenmodelle in Histo-Orla.

---

## 3. Gesamturteil

### 3.1 Kurzfassung

**Nein, ich habe nicht immer den optimalen Operationalisierungsweg gewählt.**

Die fachliche Richtung vieler Schlussfolgerungen war plausibel und teilweise stark durch bestehende Histo-Orla-Requirements/SOTA gedeckt. Der Prozess war aber wiederholt **zu affirmativ, zu schnell abstrahierend und zu persistenzfreudig**.

Der Hauptfehler war nicht Technologie-Hype. Im Gegenteil: Graph/SQL/RDF etc. habe ich weitgehend korrekt offengehalten.

Der Hauptfehler war:

> **Owner/User-Research-Signale wurden mehrfach schon nach einem einzelnen Turn zu stark synthetisiert und anschließend sofort in Foundational Design, abgeschlossene Discovery-Baseline und Downstream-Issue-Kommentare geschrieben.**

Damit habe ich genau das Risiko erzeugt, vor dem #10, #28, #41, #64 und #92 bereits warnen:

```text
Rohsignal
→ plausible Interpretation
→ generische Abstraktion
→ Repo-Persistenz
```

statt:

```text
Rohsignal
→ Klassifikation
→ Gegenlesarten / offene Fragen
→ Fach-/SOTA-Routing
→ Test an realen Workflows
→ verdichtete Synthese
→ ggf. Capability-/Requirement-Promotion
```

### 3.2 Schweregrad

**Methodisch falsch / korrigierbar:**
- PR #110: Owner-Beispiele wurden zu direkt als übergeordneter historischer Wissensraum mit konkreten Objektgruppen und Zustandsmodell in das Foundational Design geschrieben.
- mehrere frühe #42/#50-Kommentare behandelten User-Research-Signale zu früh als Requirement-/Contract-Pressure.
- vier sukzessive User-Research-Nachträge in einer abgeschlossenen #28-Baseline erzeugten Gesprächslog-Charakter statt konsolidierter Discovery.

**Nützlich, aber zu stark formuliert:**
- PR #109: der Cross-Pilot-Audit findet reale Fragmentierung, generalisiert aber einzelne Architekturfolgen zu früh.
- „Case = View“, „global Entity Registry“, „Observation first-class“, „Relation/Event object“ wurden teilweise von realen Problemen getragen, aber nicht in allen Fällen cross-case/SOTA-validiert.

**Methodisch gut / beibehalten:**
- Technologie nicht vorentschieden.
- Source/Representation/Instance/Derivative/Findspot-Schichten erhalten.
- echte Widersprüche nicht harmonisiert.
- Source Context von Source Interpretation getrennt.
- konkrete Claim-Konflikte von Modell-/Theoriepluralität unterschieden.
- User-Korrektur offen angenommen und historische PRs nicht gelöscht.
- Cross-case Duplicate `SRC-LIT-0001` vs. `ARS-009` als reale Fragmentierungsbeobachtung identifiziert.

---

## 4. Detaillierter Audit der Interventionen

### 4.1 Frühe Speicher-/Schema-Diskussion

**Mein Schritt:** Ich schlug früh einen generischen Kern `entities / sources / observations / relations / interpretations` sowie strukturierte kanonische Daten + Markdown-Views vor.

**Stärken:**
- reagierte korrekt auf die Grenzen rein manueller Markdown-Tabellen;
- trennte Observation und Interpretation;
- entschied keine konkrete Datenbank.

**Fehler:**
- der Vorschlag war bereits ein **Datenmodell-Framing**, obwohl der Nutzer zunächst das Forschungsarbeitsverhalten und die dynamische Verdichtung beschrieb;
- „Entity/Relation“ wurde zu früh als universelle Syntax behandelt;
- reale Cross-Case-Anforderungen waren noch nicht ausreichend diskriminiert.

**Urteil:** `useful-but-premature`.

**Besser:** zuerst Jobs/Pains/Transformationen und wissenschaftliche Invarianten erheben; erst danach minimalen logischen Kern ableiten.

---

### 4.2 „Dynamisch und iterativ erweiterbar“

**Mein Schritt:** Interpretation als append-first, versionable assessments, open/extensible schema, dynamic views; Kommentar in #103.

**Stärken:**
- Non-loss, Korrekturbarkeit, unresolved und History passen gut zu REQ-EPI-004/STATE/WF;
- ich trennte semantic append-first von physischem Event Sourcing.

**Fehler:**
- „append-first“ ist bereits eine Architektur-/State-Management-Interpretation des Owner-Signals;
- alternative Lesarten wurden nicht sichtbar gemacht: der Owner könnte primär adaptive Forschungsfragen, flexible Views oder Schema-Evolution gemeint haben;
- der Kommentar unter dem historischen Case #103 war für ein projektweites Product-Signal nicht der ideale primäre Ort.

**Urteil:** `partly-sound / over-interpreted`.

---

### 4.3 Projektweiter Wissensraum / 2000 Jahre / Region als Anker

**Mein Schritt:** Ich synthetisierte einen gemeinsamen regionalen Wissensraum und kommentierte #42 als Requirement-Delta-Candidate.

**Stärken:**
- langdiachroner, transdisziplinärer Scope war explizites Owner-Ziel;
- „Region = Anker, nicht analytische Grenze“ war bereits im Projekt angelegt;
- keine Technologie wurde daraus abgeleitet.

**Fehler:**
- „Cases sind nur Views über einen shared state“ wurde stärker formuliert als die damals validierte Evidenz trug;
- der Pilot #86/#88 war noch nicht final durch #89 geschlossen, wurde aber als „key learning“ benutzt;
- Requirement-Delta-Routing erfolgte, bevor das Signal als User Research gegen #28/#29/#41 diskriminiert wurde.

**Urteil:** `scope part sound; product-semantics premature`.

---

### 4.4 PR #108 – Long-Diachrony Scope

**Inhalt:** ungefähr 2000 Jahre, Neuere/Neueste Geschichte, DDR/Treuhand, materielle Evidenz, globaler Kontext.

**Was richtig war:**
- Owner besitzt Projektziel und Scope; diese Breite war explizit genannt;
- der bestehende foundational scope war tatsächlich zu eng;
- die Ergänzung unterschied Evidenzarten und behielt Fachmethoden getrennt.

**Was zu weit ging:**
- „Periodisierung ist Speichergrenze“/„gemeinsamer Forschungszustand“ koppelte Scope bereits an State-Architektur;
- konkrete Themenbeispiele wurden in ein foundational Dokument geschrieben, obwohl Beispiele besser als Falsifikationsmaterial dienen;
- keine ausdrückliche Trennung `owner scope statement` vs. `assistant-derived system implication`.

**Urteil:** `mostly justified scope correction, mixed with premature system inference`.

---

### 4.5 PR #109 – Shared Research State Audit

**Stärkster guter Befund:**
- konkrete reale Fragmentierung: dieselbe Sachenbacher-Publikation als `SRC-LIT-0001` und `ARS-009`;
- korrekte Bestandsaufnahme: starke Governance/Requirements/Assurance, aber kaum gemeinsamer persistenter Research-State-Runtime;
- gute Technikneutralität;
- richtiger Hinweis: Markdown trägt derzeit zu viel referentielle Integrität manuell.

**Überdehnungen:**
- aus einer Source-ID-Kollision wurde relativ direkt ein Bedarf für „global source resolution / aliasing“ als P0 formuliert; das ist plausibel, aber noch Architecture Candidate;
- „global Entity identity layer“, „Observation first-class“, „Relation/Event assertion state“, „Discrepancy object“ wurden als Gaps relativ definitiv benannt, obwohl einzelne Verantwortungen erst durch Domain-/Cross-Case-Tests hätten bestätigt werden sollen;
- „Research Question/Work Context = references evidence, does not own it“ wurde aus #86/#88 stärker generalisiert, obwohl #89 noch Closure Gate war;
- die Aussage „central missing layer is the shared Research State itself“ ist als Product-Hypothese stark, aber nicht bereits vollständiger Nachweis aller dafür angenommenen Objektklassen.

**Urteil:** `valuable audit with overconfident architecture extrapolation`.

**Status nach diesem Self-Audit:** Faktisches Inventar bleibt wertvoll; normative Zielschema-Passagen sind als `review hypothesis` zu lesen.

---

### 4.6 PR #110 – „übergeordneter historischer Wissensraum“

**Inhalt:** Zeit, Akteure, Gemeinden, Wüstungen, Häuser, Fluren, Fundstellen, Gewässer, Altstraßen, Regionen, technische Objekte; Identität vs. Zustand; globale Source IDs; State-Kette.

**Fehler:**
- stärkster Fall des vom Owner später kritisierten Musters „Input 1:1 aufnehmen und hochabstrahieren“;
- Nutzerbeispiele wurden fast zu einer Objekt-/Ontologie-Coverage-Liste;
- „muss zumindest“ war unzulässig stark ohne #42;
- Entity-/State-/Relation-/Discrepancy-Syntax wurde aus User Research statt Domain/SOTA/Cross-Case abgeleitet.

**Positiv:**
- keine physische Technologie gewählt;
- Fundstelle vs. archäologischer Fundplatz sinnvoll getrennt;
- Identität vs. zeitlicher Zustand ist eine ernstzunehmende Forschungsfrage.

**Urteil:** `methodologically-wrong promotion; later superseded by PR #111/#113`.

---

### 4.7 PR #111 – Reclassification as User Research

**Stärken:**
- direkte Korrektur des Fehlers;
- klare Klassifikation: Mental Model, Need/Pain/Feature/Solution Hypothesis unterscheiden;
- Routing zu C4/C5/C8/#60/#45;
- keine Requirement-/Architecture-Promotion;
- P-016 explizit reaktiviert.

**Restproblem:**
- statt nur zu korrigieren, wurde die abgeschlossene #28-Baseline als laufendes Gesprächsprotokoll benutzt;
- der erste User-Research-Nachtrag enthält bereits eine von mir entworfene Klassifikations-/Routinglogik, nicht nur Owner-Beobachtung;
- Rohsignal und Interpretation blieben im selben Abschnitt.

**Urteil:** `correct direction, wrong artifact lifecycle`.

---

### 4.8 PR #112 – syntaktische Achsen / Projektionen

**Stärken:**
- Owner-Signal nicht als Schema akzeptiert;
- source-near observation vs. normalized fact und projection vs. mutation sinnvoll getrennt;
- technische Optionen offen.

**Fehler:**
- ich formulierte sofort eigene Hypothesen wie „Relationen sind n-ary/event-like“ und „spatial entity vs geometry“;
- diese sind fachlich plausibel und durch CIDOC/WHG/SOTA challengebar, wurden aber nicht zuerst als externe Research-Frage behandelt;
- die Reaktion blieb zu nah an den konkreten Wörtern „Zeit/Raum/Relation“.

**Urteil:** `useful hypothesis generation, still over-literal`.

---

### 4.9 PR #113 – Meta-Level Transformability

**Stärken:**
- erste wirklich passende Synthese der vorangegangenen Inputs;
- keine privilegierte Perspektive, gemeinsame Evidenzbasis, komponierbare Views, Fachpluralität, Projection-before-Mutation;
- Beispiele explizit nur Falsifikationsmaterial;
- keine Daten-/Objekttaxonomie.

**Restunsicherheit:**
- „ein gemeinsamer evidenzgebundener Forschungszustand“ ist weiterhin eine Product-Hypothese, wenn auch stark durch bestehende REQ-STATE/SYN/UX und Owner-Signale gestützt;
- praktische Transformationen sind noch nicht in realen Owner-Workflows beobachtet.

**Urteil:** `strong working synthesis / not yet requirement-validated`.

---

### 4.10 PR #114 – Quellenkontext und multiple Temporalitäten

**Stärken:**
- sehr wichtige Trennung: direkt dokumentierbarer Source Context ≠ Interpretation von Motivation, Publikum, Interessenlage, Deutungshoheit;
- Research-Zeit von historischer Zeit zu trennen ist methodisch wertvoll;
- Forschungsfragen/Antworten nicht als historische Fakten behandelt.

**Fehler:**
- die Liste von acht Temporalitäten ist eine von mir erzeugte Mini-Taxonomie ohne vorangegangenen eigenen #45-SOTA-Block;
- `historical occurrence / validity / periodization / recurrence / production / reference / transmission / research time` ist plausibel, aber nicht als Histo-Orla-Semantik validiert;
- Relationsfamilien wurden ebenfalls ad hoc kategorisiert;
- erneut wurde ein einzelner User-Turn sofort als neuer Discovery-Abschnitt persisted.

**Urteil:** `scientifically promising, insufficiently researched and over-persisted`.

**Externe Challenge:** CIDOC CRM, PROV-O und WHG zeigen tatsächlich, dass temporale, provenance- und attestation-bezogene Unterscheidungen wichtig sind. Sie belegen aber nicht genau diese achtteilige Histo-Orla-Taxonomie.

---

### 4.11 PR #115 – konkrete Widersprüche vs. Modell-/Theoriepluralität

**Stärken:**
- epistemisch wichtige Unterscheidung;
- korrekt: „Quelle A Dresden / Quelle B Oppurg“ ist nicht dieselbe Problemklasse wie konkurrierende Landesausbau-Modelle;
- Modellpluralität wurde nicht als einfacher `contradiction` normalisiert;
- Routing an #60/Historiographie/CAP-16 ist korrekt.

**Fehler:**
- ich erzeugte sofort eine neunfache Discrepancy-Liste; wiederum plausibel, aber nicht SOTA-validiert;
- Begriffe/Modelle/Theorien als Research-State-Objekte wurden als naheliegende Modellierung formuliert, obwohl zunächst Domain Research zu Historiographie/Begriffsgeschichte/Modellgebrauch nötig ist;
- „Answer/Synthesis as Research-State object“ ist teilweise inferiert; der Owner sagte explizit „Forschungsfrage ist Objekt“, nicht bereits eine vollständige Lifecycle-Semantik für Antworten.

**Urteil:** `good conceptual distinction, premature taxonomy/object promotion`.

---

## 5. Cross-cutting Fehler meiner Kommunikation und Arbeitsweise

### F1 – Bestätigungs-/Mirroring-Bias

Ich begann mehrere Antworten mit sinngemäß „Genau“, „Damit wird klar“, „Das ist der Kern“. Dadurch habe ich Owner-Signale oft **bestätigt, bevor ich sie adversarial geprüft** habe.

Das ist bei User Research gefährlich: gute Assistenz muss die Bedeutung hinter einer Formulierung rekonstruieren, nicht die Formulierung automatisch verstärken.

**Korrektur:** Erst paraphrasieren + alternative Lesarten + Routing; Zustimmung erst zur tatsächlich gestützten Ebene.

### F2 – Rohsignal und Interpretation nicht getrennt persistiert

Die Repo-Nachträge enthalten kaum eine explizite Struktur:

```text
Owner observation
Assistant interpretation
Alternative interpretation
Confidence
What would falsify?
Promotion status
```

Stattdessen wurden Beobachtung und meine analytische Verdichtung in denselben Absatz geschrieben.

**Korrektur:** User Research erhält dieselbe Evidenzdisziplin wie historische Forschung: Beobachtung ≠ Finding ≠ Requirement.

### F3 – Zu häufige Repo-Mutation

PR #111–#115 folgten in sehr kurzer Folge. Vier User-Research-Abschnitte stehen inzwischen in der abgeschlossenen #28-Baseline.

Das erzeugt:
- Artefakt-Churn;
- anchoring durch frühere Zwischeninterpretationen;
- Meta-Last;
- erschwerte Handoff-Lesbarkeit;
- Widerspruch zu #64/#92.

**Korrektur:** Session-/Themenweise synthetisieren; nicht turnweise persistieren.

### F4 – Falscher Lifecycle-Ort

`docs/research/discovery/problem-baseline.md` ist eine abgeschlossene Baseline v0.1. Sie kann korrigiert werden, aber sollte nicht zum append-only User-Research-Log werden.

**Korrektur:** Die vier Nachträge werden in diesem PR zu **einer** post-baseline Working Synthesis konsolidiert. Die Git-Historie/PRs bleiben als provenance erhalten.

### F5 – Premature Requirement Pressure

Mehrere frühe Kommentare an #42 formulierten Requirement-Delta-Druck, bevor User Research/SOTA ausreichend diskriminiert waren.

Spätere Kommentare korrigierten dies, aber die Issue-Historie bleibt schwer lesbar.

**Korrektur:** Ein finaler Consolidation/Supersession-Kommentar soll klarstellen, welche früheren Kommentare nur historische Working Hypotheses sind.

### F6 – Premature Architecture Pressure

Ähnlich unter #50/#92: „global source identity“, „Entity layer“, „Observation first-class“, „query/view algebra“ sind teils wertvolle technische Forschungsfragen, aber keine bereits akzeptierten Architekturverantwortungen.

**Korrektur:** #50 konsumiert nur accepted Requirement-Invarianten. User-Research-Modelle bleiben Challenge/Test-Input.

### F7 – Pilot-Generalisierung

Der Ranis-Pilot #86/#88 wurde als „key learning“ zitiert, obwohl #89 Closure/Fresh-context noch offen war.

**Korrektur:** `pilot evidence / promising pattern`, nicht `project principle`, bis Disposition abgeschlossen oder Owner-Signal unabhängig bestätigt.

### F8 – SOTA zu spät für eigene Taxonomien

Meine Temporalitäts- und Discrepancy-Listen wurden vor einem dedizierten fachlichen Research-Paket formuliert.

#45/#60 verlangen bei architecture-/method-signifikanter Semantik stärkere fachliche Gegenprüfung.

**Korrektur:** Listen nur als illustrative questions, nicht als Taxonomie; relevante SOTA-Referenzen künftig im Research-Artefakt persistieren.

### F9 – External Reference Leakage

WHG/CIDOC/PROV wurden im Chat als hilfreiche Modelle herangezogen. Wenn diese Modelle materielle Systemsemantik beeinflussen, müssen Search Boundary, genaue Referenz und Limits im Repo nachvollziehbar werden.

**Korrektur:** Dieses Self-Audit dokumentiert sie erstmals als Challenge-Referenzen; sie erhalten weiterhin keine Histo-Orla-Authority.

### F10 – „Neutraler Fakt“ zu schnell normalisiert

Meine Korrektur zu „source-near observation“ war sinnvoll, aber kann textzentriert wirken. Archäologische/bauhistorische/naturwissenschaftliche Befunde sind nicht immer „source wording“.

**Bessere Arbeitsformel:** `evidence-near observation / Befund`, mit quellentyp-/materialtypischer Methode und Provenienz.

### F11 – Zu geringe Gegenhypothesen-Dichte

Beispiele:
- Shared State kann nötig sein, aber „eine globale Registry“ ist nicht die einzige Lösung.
- Doppelte Source IDs können Alias-/Scope-/Migration-Probleme sein, nicht automatisch ein neues Entity-System.
- „Questions are views“ kann richtig sein, aber Questions besitzen eventuell eigenen Research-State/Lifecycle.
- Projektion kann nicht immer rein read-only sein; manche Re-Kontextualisierung erzeugt neue Research Assertions.

**Korrektur:** Pro neue generische Hypothese mindestens eine plausible Gegenlesart/Failure Case dokumentieren.

---

## 6. Was aus dem Chat als belastbares User-/Product-Signal stehen bleibt

Nach Entfernung meiner zu starken Interpolationen bleiben folgende Signale gut gestützt:

1. **Langdiachroner Scope:** ungefähr 2000 Jahre, mehrere historische Epochen.
2. **Transdisziplinäre Evidenzbreite:** Schriftquellen, Karten, serielle Quellen, Archäologie, Baugeschichte, Gutachten, naturwissenschaftliche/technische Studien usw.
3. **Regionaler Entwicklungsfokus mit offenem Kontext:** Region als Forschungsanker; überregionale/globale Kontexte bei sachlicher Relevanz.
4. **Dynamische Verdichtung statt Case-Silos:** neue Forschung soll vorhandenes Wissen wiederverwenden und weiter verdichten.
5. **Multiperspektivisches Arbeitserleben:** derselbe Wissensstand soll unter wechselnden Fragen/Perspektiven untersuchbar sein.
6. **Quellen-/Evidenzkontext bleibt erreichbar:** Views auf Wissensstand und Quellenebene müssen miteinander navigierbar sein.
7. **Widersprüche dürfen bestehen:** konkurrierende Claims werden diagnostiziert, nicht erzwungen harmonisiert.
8. **Modell-/Theoriepluralität ist nicht dasselbe wie Claim-Widerspruch:** komplexe fachwissenschaftliche Modelle können partiell, komplementär oder konkurrierend sein.
9. **Forschungsfrage ist selbst dokumentierbarer Forschungsgegenstand:** sie gehört zum Research Process/State, nicht zur historischen Welt.
10. **Zeit/Raum/Relation sind komplex:** Owner-Signale zeigen klar, dass einfache Felder/monolithische Perspektiven fachlich nicht hinreichen; genaue Semantik bleibt zu erforschen.

Diese Punkte sind **User-/Product-Evidence**, keine automatische Method-/Requirement-/Architecture-Truth.

---

## 7. Was weiterhin Hypothese / unresolved bleiben muss

### 7.1 Shared canonical state

Stark gestützt, aber noch praktisch zu falsifizieren:

> mehrere Research Contexts können denselben evidenziellen Untergrund ohne Copy/semantic drift nutzen.

### 7.2 Case/Question as View

Plausibel und Owner-kompatibel, aber nicht absolut:

- Question hat vermutlich eigenen Lifecycle/Scope/Answer History;
- „View“ darf nicht heißen, dass Question-spezifische Assertions keinen eigenen State erzeugen können.

### 7.3 Source identity

Reale Duplicate-ID-Evidenz existiert. Offen bleibt die kleinste Lösung:

- global canonical ID;
- alias/reconciliation layer;
- bibliographic Work ID + representation/instance IDs;
- externe authority + local identity;
- Kombination.

### 7.4 Entity / Event / Relation / Observation model

Notwendige Differenzierungen sind teilweise accepted (REQ-ENT/REL/SPAT/EPI), aber ein universeller interner Objektkatalog ist **nicht** validiert.

### 7.5 Temporalities

Sicher ist nur: ein einzelnes `date` reicht nicht für alle Problemklassen. Exakte gemeinsame Typologie bleibt Domain-/SOTA-Frage.

### 7.6 Model/Theory objects

Sicher ist: Histo-Orla muss Forschungstraditionen, konkurrierende Begriffe/Modelle und regionale Anwendbarkeit nachvollziehbar behandeln können. Ob dies eigene first-class objects, Claims, Method-Profile-Komponenten oder bibliographisch verknüpfte Research Notes werden, ist offen.

---

## 8. Vollständigkeitslücken meiner bisherigen Arbeit

Meine Arbeit war **nicht vollständig**. Insbesondere fehlen:

1. **Systematische User-Research-Methodik** für Owner-Signale selbst: Rohbeobachtung, Interpretation, Alternativen, Confidence, Trigger, Promotion.
2. **Reale Workflow-Validierung** der multiperspektivischen Transformationen; bisher überwiegend Gesprächs-/Konzeptsignal.
3. **Historiographie-/Wissenschaftstheorie-SOTA** für Begriffe, Modelle, Theorien, Forschungsprogramme und Modellpluralität im historischen Arbeiten.
4. **Spezifische Temporal-/Spatiotemporal-SOTA** für historische Forschung über C4 hinaus, bevor gemeinsame State-Semantik beschlossen wird.
5. **Argumentations-/Research-Question-/Answer-Modellierung**: Welche Beziehungen zwischen Frage, Hypothese, Teilfrage, Finding, Synthese und Revision sind tatsächlich nötig?
6. **Cross-disciplinary evidence alignment** zwischen Text, Archäologie, Baugeschichte, Naturwissenschaft etc. auf realem Material.
7. **Reale Source→Finding→Question→Answer Reverse Navigation** als Product Slice.
8. **Owner-Acceptance-Test**: Wird der Forschungsworkflow tatsächlich einfacher, oder nur das Modell eleganter?
9. **Cross-case identity test** mit #46/#103 oder vergleichbarem realen Kollisionsfall.
10. **Artifact economy test**: Welche neuen Strukturen können generiert werden, statt manuell gepflegt zu werden?

---

## 9. Korrektur des Repo-State in diesem Audit

Dieser Audit führt bewusst **keine** neue Ontologie, Requirement oder Architecture ein.

Korrigiert werden nur von mir erzeugte Operationalisierungsprobleme:

1. Die vier sukzessiven User-Research-Nachträge in `docs/research/discovery/problem-baseline.md` werden zu **einer** Working Synthesis konsolidiert.
2. Rohsignal, Interpretation und offene Hypothese werden darin expliziter getrennt.
3. Detailtaxonomien (acht Temporalitäten, neun Discrepancy-Arten) werden aus dem kanonischen Discovery-Text zurückgenommen und zu **Research Questions / illustrative examples** degradiert.
4. Der ältere Audit `shared-research-state-audit-20260919.md` erhält einen Supersession-/Caution-Hinweis: factual inventory bleibt nutzbar; generische Zielobjekte sind Review Hypotheses.
5. Dieses Self-Audit wird im Architecture-Assurance-Index verlinkt.
6. Frühere PRs/Kommentare werden **nicht gelöscht**; sie bleiben Research-/Decision-History.

---

## 10. Künftiges Operating Protocol für Owner-Kommunikation

### 10.1 Vor jeder Persistenz

```text
Owner statement
→ Observation / Scope / Goal / Need / Pain / Mental Model / Example?
→ meine Interpretation separat
→ mindestens eine alternative Lesart, wenn materiell
→ bestehende G/N/P/CAP/REQ-Abdeckung prüfen
→ führende Fachdomäne / SOTA-Routing
→ ist Persistenz jetzt wirklich handoff-relevant?
```

### 10.2 Persistenz-Stop-Regel

**Nicht** nach jedem materiellen Chat-Turn committen.

Persistieren, wenn mindestens eines gilt:

- neues stabiles Goal/Constraint wurde explizit gesetzt;
- mehrere Signale bilden ein wiederkehrendes Need/Pain-Muster;
- eine Entscheidung/Promotion wird vorbereitet;
- ein reales Workflow-/Pilot-Ergebnis ändert die Bewertung;
- ohne Persistenz wäre ein kompetenter neuer Bearbeiter beim nächsten Chat handoff-relevant schlechter gestellt.

Sonst bleibt das Signal bis zur thematischen Synthese Werkstattmaterial.

### 10.3 Promotion

```text
User Research Signal
→ Working Synthesis
→ Domain/SOTA + real case challenge
→ Capability Candidate
→ #41/#42 equivalent current path
→ accepted Requirement
→ #48 technical derivation
```

Keine direkte Kante `Owner wording → schema / ontology / architecture`.

### 10.4 Kommunikationsregel

Bei komplexem Owner-Input nicht reflexartig „Genau“ + Ausbau.

Stattdessen:

- „Ich lese darin derzeit X.“
- „Eine alternative Lesart wäre Y.“
- „Z ist Owner-Signal; A wäre bereits meine Systeminterpretation.“
- „Diesen Teil kann ich aus bestehendem SOTA stützen; dieser Teil bleibt offen.“

---

## 11. Bewertung der Detailtiefe

### Was detailliert genug war

- Repo-Audit #109 zu Requirements/Assurance/Tooling;
- konkrete Duplicate-Source-ID-Evidenz;
- Source/Instance/Findspot-Trennung;
- Hinweise auf offene Persistenz-/Runtime-Grenzen;
- Technologie-Neutralität;
- spätere Trennung Claim-Konflikt vs. Modellpluralität.

### Was zu detailliert war, obwohl Evidenz noch dünn war

- Objektlisten in PR #110;
- temporal taxonomy PR #114;
- discrepancy taxonomy PR #115;
- Architektur-Zielspine in #109;
- zahlreiche Issue-Routing-Kommentare.

### Was trotz vieler Details fehlte

- Rohsignal vs. Assistenteninterpretation;
- alternative Erklärungen;
- explizite Confidence/Maturity der User-Research-Synthese;
- realer Workflow-Test;
- Domain-SOTA für Modellpluralität;
- Stop-/Sättigungsregel für User Research.

**Fazit:** Die Arbeit war stellenweise **detailreich, aber nicht vollständig**. Detailmenge hat methodische Vollständigkeit teilweise nur simuliert.

---

## 12. Endurteil

Die Arbeit ist **nicht zu verwerfen**. Ein großer Teil der wissenschaftlichen Invarianten passt bereits sehr gut zu Histo-Orlas accepted Requirements und bestehenden SOTA-Strängen. Die User-Korrekturen haben zudem zu einer deutlich besseren Meta-Synthese geführt.

Aber der Audit zeigt ein ernstes Muster:

> Ich habe wissenschaftlich plausible Semantik mehrfach zu früh in persistente Projektsemantik umgewandelt.

Der wichtigste Lernpunkt ist daher nicht „noch besseres Datenmodell“, sondern **epistemische Disziplin im Product-/User-Research-Prozess selbst**.

Histo-Orla verlangt von historischen Claims:

```text
Quelle → Beobachtung → Finding → Interpretation
```

Für Owner-/Product-Research muss dieselbe Disziplin gelten:

```text
Owner-Signal → beobachtetes Need/Mental Model → analysierte Hypothese
→ fachlich/workflowseitig geprüfte Capability
→ akzeptiertes Requirement
→ Architektur
```

Meine Arbeit zwischen PR #108 und #115 hat diese Symmetrie erst verspätet hergestellt.

---

## 13. Handoff

### Material changed by this corrective audit

- self-audit added;
- live Owner User-Research appendages will be consolidated;
- prior audit will be explicitly qualified;
- no accepted Requirement/Method/Architecture semantics changed.

### Canonical homes

- process/user-research assessment: dieses Artefakt unter #64;
- consolidated Problem/User-Research working state: `docs/research/discovery/problem-baseline.md` under #28;
- accepted Requirements: weiterhin ausschließlich #42;
- Method Truth: weiterhin #60;
- Architecture derivation: weiterhin #48/#50;
- historical PR/comment chronology: GitHub history.

### Open next actions

1. consolidate current user-research text;
2. test the meta-hypothesis on a small real cross-pilot evidence set;
3. perform domain/SOTA work only for semantic distinctions that prove necessary;
4. then decide whether #42 needs a real Requirement delta;
5. no persistence/topology choice before that.

**No blocker requires #44.**
