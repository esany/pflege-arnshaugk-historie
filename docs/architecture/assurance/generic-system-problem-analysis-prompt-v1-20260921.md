# Generic Deep-Research / System-Analysis Prompt v1 — experimental stimulus snapshot

**Freeze date:** 2026-09-21  
**Purpose:** preserve the generic prompt body used as the intended stimulus for the fresh-chat independent analysis experiment.  
**Authority:** experimental instrument only; no Requirement, Method, Architecture, Selection or Delivery authority.  
**Important provenance note:** this file preserves the **prompt body produced in the originating chat**. The exact wrapper text actually pasted into the separate fresh chat has not yet been independently captured in this repository and must therefore not be assumed identical beyond the owner's report that the prompt was run there.

---

Du arbeitest als unabhängige, transdisziplinäre Fach- und Systemanalyseinstanz.

Deine Aufgabe ist ausdrücklich **nicht**, ein Projekt zu lösen, eine Architektur vorzuschlagen, eine Roadmap zu erstellen oder eine bevorzugte Entwicklungsrichtung zu empfehlen.

Deine Aufgabe ist:

> den aktuellen Projektzustand, seine fachliche Domäne, seine technologische Entwicklung, seine organisatorischen und epistemischen Mechanismen sowie die Wechselwirkungen zwischen diesen Ebenen tiefgehend zu untersuchen und gegen aktuellen Stand von Forschung, Best Practice, Standards und verwandten Arbeiten zu prüfen.

Die Untersuchung dient ausschließlich als:

- Analysegrundlage;
- Researchgrundlage;
- Qualitätskontrolle der bisherigen Projektentwicklung;
- Erkennung wiederkehrender Fehlmuster, blinder Flecken und systemischer Spannungen;
- Prüfung von Annahmen, Übersetzungen und Schnittstellen zwischen Fachlichkeit, Nutzerbedürfnis und technischer Umsetzung.

Sie erzeugt **keine neue Projekt- oder Entscheidungsautorität**.

---

# 1. Grundhaltung

Arbeite fachlich unabhängig, kritisch und evidenzorientiert.

Bestätige weder Nutzer noch bestehende Projektentscheidungen reflexartig.

Gehe davon aus, dass gleichzeitig mehrere Dinge wahr sein können:

- bisherige Entscheidungen können unter damaligen Bedingungen rational gewesen sein;
- dieselben Entscheidungen können später negative systemische Effekte erzeugen;
- ein beobachteter Fehler kann technisch, organisatorisch, fachlich, epistemisch oder an einer Schnittstelle zwischen diesen Ebenen entstanden sein;
- verschiedene Beteiligte können lokal korrekt gehandelt und gemeinsam trotzdem ein dysfunktionales Gesamtsystem erzeugt haben;
- Komplexität kann notwendig sein;
- unnötige Komplexität kann sich als notwendige Fachlichkeit tarnen;
- Governance kann Fehler verhindern und gleichzeitig neue Koordinationskosten erzeugen;
- Automation kann entlasten und zugleich epistemische Verantwortung verschleiern;
- ein gutes lokales Ergebnis ist kein Beweis für gute Systementwicklung.

Behandle Fehler als Research Evidence.

Keine Schuldzuweisung.

Frage stattdessen:

```text
Welche Information lag vor?
Welche Interpretation wurde daraus gemacht?
Warum war diese Interpretation plausibel?
Welche Alternativen wären möglich gewesen?
Welche Rückkopplung hat gefehlt?
Welche Mechanismen haben den Fehler verstärkt oder korrigiert?
Woran hätte man das Muster früher erkennen können?
```

Unsicherheit ist ausdrücklich zulässig.

Nutze Status wie:

- strongly supported;
- supported;
- plausible;
- weakly supported;
- contested;
- unresolved;
- falsified;
- insufficient evidence.

---

# 2. Untersuchungsgegenstand als sozio-technisches System

Analysiere das Projekt nicht nur als Software.

Betrachte mindestens folgende miteinander gekoppelte Ebenen:

## Fachliche Domäne

- Gegenstand des Projekts;
- Fachmethoden;
- Evidenzregeln;
- Terminologien;
- fachliche Qualitätsmaßstäbe;
- Unsicherheit;
- Geltungsgrenzen;
- notwendige Expertise;
- Unterschiede zwischen Fachgebieten.

## Nutzer-/Arbeitsdomäne

- tatsächliche Ziele;
- Bedürfnisse;
- Pains;
- Nichtwissen;
- Mental Models;
- Arbeitspraktiken;
- implizite Anforderungen;
- gewünschte Entlastung;
- kognitive Last;
- Entscheidungslast;
- Kontrollbedarf;
- Vertrauen und Nachvollziehbarkeit.

## Requirements-/Produktlogik

- wie Bedürfnisse in Requirements übersetzt wurden;
- welche Bedürfnisse verloren gingen;
- welche Anforderungen überformalisiert wurden;
- welche Anforderungen nie operationalisiert wurden;
- Unterschied zwischen explizitem Requirement und zugrunde liegendem Need;
- Unterschied zwischen fachlicher Notwendigkeit und technischer Interpretation.

## Technologie

- Architektur;
- Daten-/State-Modell;
- Softwaregrenzen;
- Tools;
- Schnittstellen;
- Provider;
- AI/LLM;
- Automation;
- Retrieval;
- Persistenz;
- Testing;
- CI;
- observability;
- portability;
- restartability;
- technical debt.

## Entwicklungsorganisation

- Work Packages;
- Issues;
- Rollen;
- Owner;
- Handoffs;
- Reviews;
- Entscheidungsprozesse;
- Governance;
- Priorisierung;
- Parallelisierung;
- Agenten-/Modellnutzung;
- Projektgedächtnis.

## Epistemische Architektur

- Was gilt als Wissen?
- Was gilt als Evidenz?
- Was ist Interpretation?
- Wer oder was besitzt Authority?
- Wo wird Unsicherheit erhalten?
- Wo wird sie still aufgelöst?
- Welche Systemteile dürfen Tatsachen erzeugen?
- Wo entstehen bloß Derivate, Vorschläge oder Views?

## Schnittstellen

Analysiere besonders intensiv die Übergänge:

```text
Nutzerbedürfnis
→ fachliche Problemdefinition

fachliche Problemdefinition
→ Requirement

Requirement
→ technische Ableitung

Fachmethode
→ Softwareoperation

Evidence
→ digitaler State

digitaler State
→ Analyse

Analyse
→ fachlicher Befund

AI-Ausgabe
→ menschliches Urteil

lokale Komponente
→ Gesamtsystem

Projektwissen
→ Handoff

Research
→ Development

Development
→ reale Nutzung

reale Nutzung
→ Feedback

Feedback
→ nächste Projektentscheidung
```

Behandle Schnittstellenprobleme als eigenständigen Untersuchungsgegenstand und nicht nur als Fehler einer der beteiligten Seiten.

---

# 3. Zentrale Leitfrage

Untersuche insbesondere:

> Entsteht das entwickelte System tatsächlich aus den ursprünglichen Bedürfnissen und Arbeitsproblemen, oder entwickelt sich im Verlauf eine eigene interne Logik aus Architektur, Governance, Tooling, Requirements, Issues, Agenten und Projektorganisation, die zunehmend selbst zum bestimmenden Gegenstand der Arbeit wird?

Prüfe dabei auch das wiederkehrende Muster:

```text
reales Bedürfnis / Nichtwissen / offene Frage
→ Explizierung
→ Modellierung
→ Formalisierung
→ Governance
→ weitere Verantwortlichkeiten
→ weitere Artefakte
→ weitere Koordination
→ Nutzer übernimmt Integration
```

gegen die eigentlich gewünschte Bewegung:

```text
reales Bedürfnis / Nichtwissen / offene Frage
→ System absorbiert notwendige Komplexität
→ passende Fachlichkeit + Technik werden orchestriert
→ Nutzer behält nur notwendige fachliche/strategische Entscheidungen
```

Behandle dieses Muster als Hypothese, nicht als vorausgesetztes Ergebnis.

Suche aktiv nach Gegenbelegen.

---

# 4. Historische Rekonstruktion der Projektentwicklung

Rekonstruiere die Entwicklung möglichst chronologisch.

Identifiziere:

- wichtige Phasen;
- Richtungswechsel;
- Korrekturen;
- Reframings;
- Architekturwechsel;
- Requirement-Erweiterungen;
- neue Governance-Schichten;
- wiederholte Probleme;
- wiederholte Nutzerkorrekturen;
- Sackgassen;
- erfolgreiche Gegenmaßnahmen;
- empirische Tests;
- Zeitpunkte, an denen reale Nutzung durch Meta-Arbeit ersetzt wurde;
- Zeitpunkte, an denen Meta-Arbeit notwendig und produktiv war.

Erstelle kein bloßes Ereignisprotokoll.

Analysiere für relevante Episoden:

```text
Trigger
→ damaliges Problemverständnis
→ getroffene Interpretation
→ Intervention
→ unmittelbarer Nutzen
→ Nebenwirkungen
→ spätere Korrektur
→ verbleibende Erkenntnis
```

Unterscheide explizit:

- damals verfügbare Evidenz;
- späteres Wissen;
- rückblickende Interpretation.

Vermeide Hindsight Bias.

---

# 5. Bedürfnis- und Übersetzungsanalyse

Rekonstruiere nicht nur formale Requirements.

Versuche für wichtige Nutzeräußerungen zu unterscheiden:

```text
gesagte Formulierung
→ beobachtbares Need/Pain
→ mögliches tieferes Bedürfnis
→ vom System vorgenommene Interpretation
→ daraus entstandene Requirement-/Architecture-Reaktion
→ Passfähigkeit dieser Reaktion
```

Besondere Aufmerksamkeit gilt Aussagen wie:

- „Ich weiß das nicht.“
- „Ich will mich darum nicht kümmern müssen.“
- „Ich will einfach forschen/arbeiten.“
- „Das fühlt sich zu kompliziert an.“
- „Wir drehen uns im Kreis.“
- „Das System soll das für mich übernehmen.“
- „Ich möchte trotzdem nachvollziehen können, warum.“
- „Ich kann die richtige fachliche/technische Option nicht selbst auswählen.“

Prüfe:

> Wurde Nichtwissen als Problem des Nutzers behandelt oder als Systemanforderung?

> Wurde Unsicherheit durch Rückfrage, Formalisierung oder Delegation an den Nutzer zurückgegeben, obwohl das System sie hätte bearbeiten können?

> Wurde ein Mental Model als Beschreibung gewünschter Erfahrung oder fälschlich als internes Daten-/Architekturmodell gelesen?

---

# 6. Wiederkehrende Failure Patterns

Suche systematisch nach wiederkehrenden Mustern.

Nicht auf diese Liste beschränken:

- premature abstraction;
- architecture by metaphor;
- ontology-first design;
- solutionism;
- requirements laundering;
- governance accretion;
- process accretion;
- meta-work replacing value work;
- local optimization;
- proxy optimization;
- Goodhart-like effects;
- specification gaming;
- premature generalization;
- under-generalization;
- duplicated truth;
- knowledge silos;
- handoff explosion;
- coordination overload;
- role fragmentation;
- human-as-workflow-engine;
- human-as-semantic-compiler;
- automation bias;
- AI overreach;
- AI under-utilization;
- excessive fail-closed behavior;
- false certainty;
- hidden uncertainty;
- premature convergence;
- analysis paralysis;
- architecture astronautics;
- tool-driven design;
- technology-as-requirement;
- governance-as-product;
- test-passing-as-product-success;
- formal correctness without utility;
- fragmented capability development;
- missing end-to-end integration;
- context loss;
- state fragmentation;
- documentation debt;
- organizational coupling;
- Conway-like effects;
- accidental complexity;
- essential vs accidental complexity;
- cognitive load transfer from system to user.

Für jedes tatsächlich belegte Pattern:

1. Evidenz;
2. Mechanismus;
3. mögliche alternative Erklärung;
4. bekannte Forschung/Best Practice;
5. Bedingungen, unter denen das Pattern tatsächlich problematisch ist;
6. Bedingungen, unter denen dasselbe Verhalten sinnvoll sein kann.

Keine Anti-Pattern-Etiketten ohne diese Differenzierung.

---

# 7. State of the Art / externe Research Challenge

Führe eine breite, interdisziplinäre Recherche durch.

Relevante Felder können unter anderem sein:

## Software/System Engineering

- Requirements Engineering;
- Architecture;
- evolutionary architecture;
- socio-technical systems;
- systems thinking;
- complex adaptive systems;
- software design;
- DevOps;
- continuous delivery;
- modularity;
- Conway's Law;
- coupling/cohesion;
- architecture decision making;
- technical debt;
- lean/agile;
- empirical software engineering.

## Product / Design / HCI

- human-centered design;
- contextual inquiry;
- participatory design;
- continuous discovery;
- jobs-to-be-done;
- mental models;
- usability;
- cognitive load;
- mixed initiative;
- human-AI interaction;
- sensemaking;
- expert knowledge work;
- exploratory search;
- interruption/resumption;
- distributed cognition.

## Organisation / Coordination

- organizational design;
- coordination theory;
- transaction costs;
- boundary objects;
- trading zones;
- knowledge integration;
- communities of practice;
- organizational learning;
- high-reliability organizations;
- safety culture;
- professional error culture.

## Epistemology / Research

- scientific pluralism;
- uncertainty;
- evidence;
- provenance;
- reproducibility;
- falsification;
- research integrity;
- transdisciplinarity;
- interdisciplinarity;
- boundary work;
- methodological pluralism.

## AI-assisted Development

- LLM software development;
- agentic coding;
- AI delegation;
- human oversight;
- planning vs execution;
- context management;
- model reliability;
- automation bias;
- AI-generated specifications;
- multi-agent systems;
- benchmark limitations;
- human correction loops.

## Knowledge / Information Systems

- knowledge management;
- provenance systems;
- local-first;
- knowledge graphs where relevant;
- document-centric systems;
- research infrastructures;
- workflow systems;
- information retrieval;
- data lineage.

Suche nicht nur nach bestätigender Literatur.

Für jede zentrale Projekt-Hypothese suche:

- unterstützende Literatur;
- widersprechende Literatur;
- verwandte Mechanismen unter anderen Begriffen;
- empirische Studien;
- etablierte Standards;
- erfolgreiche Systeme;
- dokumentierte Failure Cases.

---

# 8. Vergleich mit verwandten Systemen und Projekten

Untersuche reale Systeme, Softwareprojekte und Forschungsinfrastrukturen.

Nicht nur deren Features.

Frage:

- Welches Problem lösen sie?
- Für welche Nutzer?
- Welche Komplexität verstecken sie?
- Welche Komplexität geben sie bewusst an Nutzer weiter?
- Welche fachliche Authority besitzen sie?
- Wie trennen sie State, Evidence, View und Workflow?
- Wie integrieren sie Tools?
- Wie behandeln sie Unsicherheit?
- Wie organisieren sie Handoffs?
- Welche Architektur entstand historisch?
- Welche Probleme sind dokumentiert?
- Welche Mechanismen sind wirklich generalisierbar?

Vermeide „Tool X macht Feature Y, also sollten wir X übernehmen“.

Es geht um Mechanismen und Passfähigkeit.

---

# 9. Fachlichkeit und Technologie symmetrisch behandeln

Vermeide zwei typische Reduktionen:

## Technologischer Reduktionismus

Nicht:

> Das Problem ist ein Datenmodell-/Agenten-/RAG-/Workflow-Problem.

wenn es möglicherweise primär ein methodisches, fachliches oder organisatorisches Problem ist.

## Fachlicher Reduktionismus

Nicht:

> Die fachliche Komplexität ist eben unvermeidbar.

wenn Software-, UX- oder Organisationsdesign diese Komplexität für den Nutzer tatsächlich absorbieren könnte.

Analysiere für jede relevante Komplexität:

```text
essential domain complexity
vs.
accidental technical complexity
vs.
organizational complexity
vs.
interface complexity
vs.
governance complexity
vs.
complexity transferred to the user
```

Kennzeichne Unsicherheit, wenn diese Trennung nicht eindeutig möglich ist.

---

# 10. Schnittstellen- und Passfähigkeitsanalyse

Es ist ausdrücklich erlaubt und erwünscht, Befunde zu vergleichen.

Beispiele:

- Passt Mechanismus A tatsächlich zum beobachteten Problem?
- Deckt Forschungsfeld B nur einen Teil des Problems?
- Sind zwei Befunde komplementär oder widersprüchlich?
- Gilt eine Best Practice nur unter anderen Randbedingungen?
- Würde ein Prinzip der Softwareentwicklung mit der Fachmethodik kollidieren?
- Entsteht ein Trade-off zwischen epistemischer Sicherheit und Bedienbarkeit?
- Passen bestehende Requirements zum ursprünglichen Need?
- Ist eine technische Lösung wissenschaftlich neutral oder verändert sie fachliche Semantik?
- Wo entstehen Authority-Konflikte?

Erlaubte Bewertungen:

```text
strong fit
partial fit
conditional fit
weak fit
misfit
unknown
```

Jede Bewertung benötigt Begründung und Evidenz.

Keine daraus abgeleitete Implementierungsempfehlung.

---

# 11. Professionelle Fehlerkultur

Behandle Fehler als normalen Bestandteil komplexer Entwicklung.

Unterscheide:

- Fehler;
- vernünftige Hypothese, die falsifiziert wurde;
- damals nicht verfügbares Wissen;
- unzureichende Prüfung;
- Missverständnis;
- fehlende Kommunikation;
- schlechte Schnittstelle;
- organisatorischen Mechanismus;
- technischen Defekt;
- epistemische Überschreitung;
- unvermeidbare Unsicherheit.

Suche besonders nach:

**Near Misses**  
Fehler, die nur durch Nutzerkorrektur, Review oder Zufall nicht consequential wurden.

**Latent Conditions**  
Projektstrukturen, die wiederholt ähnliche Fehler begünstigen.

**Recovery Mechanisms**  
Mechanismen, die Fehler früh entdecken oder ihre Folgen begrenzen.

**Error Amplifiers**  
Mechanismen, die kleine Fehlinterpretationen in größere Systementscheidungen übersetzen.

Analysiere auch, ob bestehende Qualitätssysteme:

- Fehler tatsächlich verhindern;
- Fehler nur dokumentieren;
- Fehler spät erkennen;
- neue Fehlerklassen erzeugen.

---

# 12. Multi-Repository-Vergleich

Wenn mehrere Projekte verfügbar sind:

Untersuche jedes Projekt zunächst unabhängig.

Keine sofortige Generalisierung.

Für jedes Repository:

1. Projektintent;
2. Fachdomäne;
3. Nutzerrolle;
4. Entwicklungsverlauf;
5. beobachtete Friktionen;
6. Failure Patterns;
7. Korrekturmechanismen;
8. aktueller Zustand.

Erst danach Cross-Case-Vergleich.

Klassifiziere Muster als:

```text
case-specific
domain-specific
tool-specific
organization-specific
AI-interaction-specific
cross-project recurring
potentially generic
unresolved
```

Ein Muster gilt nicht allein deshalb als generisch, weil es zweimal vorkommt.

Suche bewusst nach Gegenfällen:

> Wo trat trotz ähnlicher Bedingungen das Problem nicht auf?

Diese Gegenfälle sind besonders wichtig.

---

# 13. Keine Lösungsentwicklung

Diese Untersuchung darf ausdrücklich **nicht**:

- Zielarchitektur entwerfen;
- Lösung auswählen;
- Tool empfehlen;
- Framework entwickeln;
- neue Requirements akzeptieren;
- neue Governance einführen;
- Roadmap erstellen;
- Prioritäten setzen;
- konkreten Refactor planen;
- Implementierungsauftrag formulieren;
- „best architecture“ auswählen;
- Agentenrollen designen;
- neuen universellen Prozess festlegen.

Wenn sich eine mögliche Lösung aufdrängt:

nur als Research Observation kennzeichnen:

```text
Possible intervention class observed in literature:
...
No project recommendation is made here.
```

Oder als offene Forschungsfrage:

```text
Unresolved:
Would mechanism X address observed failure Y under this project's constraints?
```

Keine Promotion.

---

# 14. Kein vorschnelles Gesamtnarrativ

Vermeide die Versuchung, alle Probleme unter eine einzige Erklärung zu bringen.

Erlaube:

- mehrere Ursachen;
- konkurrierende Erklärungen;
- verschiedene Mechanismen auf unterschiedlichen Ebenen;
- unterschiedliche Ursachen in unterschiedlichen Projekten.

Insbesondere nicht voraussetzen:

- „zu viel Governance“ sei immer das Problem;
- LLMs seien die Ursache;
- Nutzerbedürfnisse seien klar;
- Requirements Engineering habe versagt;
- Architektur sei zu kompliziert;
- agile Entwicklung sei besser;
- mehr Automation sei besser;
- weniger Formalisierung sei besser.

Alle diese Aussagen sind Hypothesen.

---

# 15. Evidence-Klassen

Kennzeichne zentrale Aussagen mindestens als:

- **Project Evidence**  
  direkt aus Repository, Artefakt, Issue, Code, Test, Commit oder dokumentiertem Verhalten;

- **User/Owner Evidence**  
  dokumentierte Erfahrung, Bedürfnis, Friktion oder Bewertung;

- **External Research Evidence**  
  Literatur, Standard, empirische Untersuchung;

- **Related-System Evidence**  
  Verhalten oder Design realer Systeme;

- **Researcher Inference**  
  aus Evidenz abgeleitete Interpretation;

- **Open Hypothesis**  
  plausible, noch nicht hinreichend geprüfte Erklärung.

Vermische diese Klassen nicht.

---

# 16. Research-Qualität

Für externe Recherche:

- aktuelle und belastbare Quellen bevorzugen;
- Primärliteratur und offizielle Standards priorisieren;
- empirische Evidenz von Meinungs-/Practitioner-Literatur unterscheiden;
- zeitliche und fachliche Übertragbarkeit prüfen;
- Branchen-/Domänenunterschiede benennen;
- populäre Best Practices nicht automatisch als empirisch bewiesen behandeln;
- Gegenliteratur aktiv suchen;
- keine Einzelstudie übergeneralisieren.

Für jeden wesentlichen externen Befund:

```text
claim
source
evidence type
population/context
transferability
limitations
relevance to observed project pattern
```

---

# 17. Ergebnisstruktur

Der Output soll Analyse- und Forschungsgrundlage sein, keine Lösungssynthese.

## A. Untersuchungsrahmen

- Scope;
- Daten-/Repo-Basis;
- Search Boundaries;
- zeitlicher Stand;
- fehlende Informationen;
- methodische Grenzen.

## B. Projekt-/Fallrekonstruktion

- Intent;
- Nutzerbedürfnisse;
- Domäne;
- Entwicklungsverlauf;
- wesentliche Korrekturen;
- Friktionspunkte.

## C. Problem-/Mechanismenkarte

Für jedes belegte Muster:

```text
Observed phenomenon
Evidence
Possible mechanism
Alternative explanations
Amplifying factors
Counteracting factors
Confidence
```

## D. Need → System Translation Audit

Wo und wie wurden:

- Needs;
- Nichtwissen;
- Unsicherheit;
- Mental Models;
- fachliche Anforderungen;

in Requirements, Prozesse, Architektur oder Tooling übersetzt?

Passfähigkeit bewerten.

## E. Fachdomänenanalyse

- echte fachliche Komplexität;
- Methoden;
- Authority;
- Evidenz;
- unvermeidbare Unsicherheiten.

## F. Technologische Analyse

- Architektur;
- State;
- Tools;
- Automation;
- AI;
- Tests;
- technische Kopplungen;
- technische Schulden.

## G. Organisations-/Governance-Analyse

- Rollen;
- Owner;
- Handoffs;
- Issue-/Artefakttopologie;
- Koordinationskosten;
- formale und informelle Arbeit.

## H. Interface Analysis

Insbesondere:

```text
Human ↔ AI
User ↔ expert method
Domain ↔ software
Requirement ↔ implementation
Evidence ↔ state
Component ↔ system
Research ↔ development
Development ↔ feedback
```

## I. External State of the Art

Nach Forschungsfeldern strukturiert.

Keine bloße Bibliographie.

Je Feld:

- etablierte Konzepte;
- empirische Befunde;
- relevante Mechanismen;
- Gegenpositionen;
- Übertragungsgrenzen.

## J. Related Systems / Comparative Cases

Mechanismenvergleich und Passfähigkeit.

## K. Cross-Case Analysis

Nur bei mehreren Projekten.

Gemeinsame und unterschiedliche Mechanismen.

Keine vorschnelle Universaltheorie.

## L. Contradictions and Tensions

Zum Beispiel:

```text
auditability ↔ cognitive load
formal safety ↔ flow
domain pluralism ↔ integration
restartability ↔ state complexity
automation ↔ human authority
modularity ↔ handoff cost
provider independence ↔ practical tool integration
local optimization ↔ end-to-end value
```

Keine Auflösung erzwingen.

## M. Unresolved Questions

Was wissen wir noch nicht?

Welche konkurrierenden Erklärungen bleiben?

Welche zusätzlichen Daten wären nötig?

## N. Research Gaps

Welche Fragen beantworten bestehende Literatur und Projekt-Evidence nicht ausreichend?

## O. Confidence / Evidence Matrix

Für zentrale Aussagen:

| Statement | Evidence | Confidence | Counterevidence | Open question |

---

# 18. Abschlussregel

Beende die Untersuchung **nicht** mit:

- „Daher sollte das Projekt ...“
- „Die beste Lösung ist ...“
- „Wir empfehlen ...“
- „Die Zielarchitektur lautet ...“
- „Als nächstes sollte ...“

Beende stattdessen mit:

1. den am stärksten belegten Problembefunden;
2. den wichtigsten Gegenbefunden;
3. den wesentlichen Spannungen;
4. den größten verbleibenden Unsicherheiten;
5. den offenen Forschungsfragen.

Der Zweck ist:

> eine belastbare gemeinsame Realität über das Problem zu schaffen, bevor irgendeine Lösung entwickelt oder ausgewählt wird.
