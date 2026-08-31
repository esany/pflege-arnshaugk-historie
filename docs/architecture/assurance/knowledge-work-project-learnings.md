# Transferable Learnings für zukünftige Wissensarbeitsprojekte

**Status:** `transferable-learning / pilot-derived / non-binding`  
**Work Owner:** #61  
**Evidence Base:** `docs/architecture/assurance/live-pilot-system-analysis-chat-2026-08-31.md`, #46/#47/#60/#61  
**Requirements Owner:** #42  
**Stand:** 2026-08-31

## 1. Zweck und Geltungsgrenze

Dieses Dokument abstrahiert Learnings aus dem Histo-Orla-Live-Pilot für **zukünftige Wissensarbeitsprojekte**: Forschungsassistenz, Literatur-/Quellenarbeit, Policy-/Rechtsanalyse, wissenschaftliche Synthese, Due-Diligence-artige Recherche oder andere Arbeit, bei der Evidenz, Fachmethodik, Interpretation und Nachvollziehbarkeit wichtiger sind als bloße Textproduktion.

Die Punkte sind **keine universellen Gesetze, keine akzeptierten Histo-Orla-Requirements und keine Architekturentscheidung**. Sie sind transferierbare, durch einen realen Pilot gestützte Design-/Arbeitsprinzipien. Andere Projekte müssen sie gegen eigenen Fach-SOTA, Risiken, Nutzerabläufe und reale Piloten prüfen.

## 2. Transfer-Learnings

### L-KW-01 – Reale Wissensarbeit ist zugleich Systemanalyse

Ein Live-Case darf nicht nur als fachlicher Use Case betrachtet werden. Friktionen, Fehlversuche, Überinterpretationen, unnötige Rückfragen, verlorener Kontext und falsche Zustandsübergänge sind **Systemanalyse-Evidence**.

Konsequenz: Projekte sollten einen expliziten Pfad besitzen:

```text
live observation / pain / failure
→ betroffener Workflow / Capability / Requirement
→ existing coverage | ambiguity | gap
→ candidate
→ Generalisierungs-/SOTA-/Risk-Prüfung
→ erst dann Requirement-/Design-Entscheidung
```

### L-KW-02 – Nutzerformulierung ist Problem-Input, nicht Fachmethode

Nutzer dürfen alltagssprachlich, unvollständig oder fachlich unscharf fragen. Das System darf daraus weder Terminologie, Methode noch Requirement direkt ableiten.

Konsequenz: Zwischen Nutzerfrage und Lösung braucht es eine fachliche Übersetzungsschicht:

```text
Nutzerbeobachtung / Ziel
→ fachlich plausible Problemklassen
→ führende Fachdomäne(n)
→ fachlicher SOTA / Methode / Evidenzmaßstab
→ erst danach Analyse
```

### L-KW-03 – Kompetenzlabels reichen nicht; Method Truth ist eine eigene Schicht

„Historiker“, „Jurist“, „Ökonom“, „Archivar“, „Biologe“ oder ein Rollenprompt beweisen keine fachliche Arbeitsfähigkeit. Eine belastbare Wissensassistenz braucht für priorisierte Problemtypen operationalisierte Fachmethoden: Begriffe, Quellen-/Materiallogik, Playbook, Inferenzgrenzen, Suchsprache, QA/Falsifikation, typische Fehlschlüsse und fachliche Schnittstellen.

Konsequenz: **Kompetenzinventar ≠ operative Methode.**

### L-KW-04 – Methode und Methodenanwendung müssen getrennt werden

Ein gutes Methodenprofil beweist nicht, dass es in einem konkreten Fall korrekt angewandt wurde.

Zu unterscheiden sind mindestens:

```text
Method Profile
Method Application
Evidence / Input
Finding / Claim
Review / Validation
Prompt / Model / Tool Run
```

Damit wird später auditierbar, welche Methode in welcher Version/Statusstufe tatsächlich auf welchen Fall angewandt wurde.

### L-KW-05 – Kontextverlust upstream ist später oft irreversibel

Bei Wissensarbeit entscheidet die Materialerhebung darüber, welche Fragen später überhaupt noch beantwortbar sind. Wer beim Exzerpieren, Extrahieren oder Strukturieren nur die unmittelbar gesuchte Tatsache bewahrt, kann soziale, rechtliche, institutionelle, motivationale oder materielle Kontexte vernichten.

Konsequenz: **Kontextverlust ist Informationsverlust.** Welche Kontextdimensionen bei der Erhebung bewahrt werden müssen, ist eine fachmethodische Frage und darf nicht erst bei der späteren Synthese gestellt werden.

### L-KW-06 – Exploration offen, Promotion fail-closed

Unsichere Methode oder unvollständige Evidenz darf Exploration nicht unnötig blockieren. Sie darf aber nicht durch plausible KI-Prosa zu einem höherwertigen Wissensstatus werden.

Robustes Muster:

```text
exploration / candidate / hypothesis
→ erlaubt bei sichtbarer Unsicherheit

consequential / accepted / validated
→ nur bei erfüllten Method-/Evidence-/Review-Voraussetzungen
```

Das schützt Kreativität **und** epistemische Qualität.

### L-KW-07 – KI darf ihre eigene Autorität nicht durch Sprache erzeugen

Ein leistungsfähiges Sprachmodell kann methodisch klingende Erklärungen produzieren und dadurch den Eindruck fachlicher Legitimation erzeugen.

Deshalb braucht Systemanalyse explizite Negativtests gegen mindestens:

- Rollenprompt oder Disziplinlabel als Methodennachweis;
- KI-Ausgabe als Evidenz;
- mehrere korrelierte KI-Prüfungen als unabhängige Fachvalidierung;
- Candidate als accepted/validated State;
- fehlende Evidenz/Fundstelle hinter plausibler Synthese;
- erzwungene Eindeutigkeit statt `unresolved` / `not-assessable`.

### L-KW-08 – Interne Governance darf nicht zur Nutzerlast werden

Work Owner, Method IDs, Statusklassen, Authority-Grenzen und Handoff-Felder können intern wichtig sein. Der Fachnutzer sollte diese Verwaltungsstruktur aber nicht kennen oder manuell bedienen müssen, soweit sie aus Auftrag und kanonischem State ableitbar ist.

Konsequenz: **wissenschaftlich strenge Innenstruktur, geringe Bedienlast außen.** Rückfragen nur bei materieller Ambiguität, nicht für intern deterministisch lösbare Verwaltung.

### L-KW-09 – Fresh-context Restartability ist ein funktionaler Acceptance Test

Dokumente zu besitzen ist nicht dasselbe wie handoff-fähig zu sein. Ein neuer kompetenter Bearbeiter oder neuer KI-Kontext muss ohne alten Chat korrekt rekonstruieren können:

- aktuelle Aufgabe und Scope;
- Authority / Work Owner;
- geltende Methode(n) und Status;
- verfügbare Evidenz;
- erlaubte nächste Aktion;
- offene Unsicherheit;
- Handoff-/Return-Bedingung;
- kanonischen Persistenzort.

Wenn das praktisch nicht gelingt, ist der Wissenszustand nicht restartbar.

### L-KW-10 – Kanonisches Projektgedächtnis darf nicht im Chat liegen

Chats sind nützliche Werkstätten, aber schlechte alleinige Projektgedächtnisse: transient, kontextabhängig und schwer auditierbar.

Transferierbares Muster:

```text
Chat / Agent Context = Arbeitsraum
versionierter kanonischer State = Projektgedächtnis
Issue / Work Item = Verantwortung / Status / nächste Aktion
```

Continuation-critical Wissen wird außerhalb des Chats persistiert.

### L-KW-11 – Evidence, Finding, Interpretation, Requirement und Design sind verschiedene Wahrheitsklassen

Viele Wissenssysteme scheitern nicht an fehlender Information, sondern an stiller Statusvermischung. Ein Quellenbefund ist keine Interpretation; eine Interpretation ist kein Requirement; ein einzelner Pain ist kein akzeptiertes Requirement; eine technische Hypothese ist keine Architekturentscheidung.

Konsequenz: Zustandsarten müssen semantisch und prozessual unterscheidbar bleiben.

### L-KW-12 – Live Evidence muss Gates wieder öffnen können

Ein früher Requirements- oder Architecture-Gate ist keine Einbahnstraße. Wenn reale Nutzung eine zuvor unsichtbare fachliche oder produktbezogene Lücke zeigt, muss das Projekt die Möglichkeit haben, einen Gate-Status kontrolliert zurückzunehmen.

Konsequenz: **Fortschritt ist nicht das Festhalten an einer früheren Readiness-Annahme, sondern die Fähigkeit, sie bei besserer Evidenz zu korrigieren.**

### L-KW-13 – Dev informiert Requirements; Dev besitzt sie nicht

Technische Exploration sollte früh beginnen: vorhandene Tools, Integrationen, Feasibility, Kosten, Lock-in, Benchmarks. Sie darf aber fehlende Fachsemantik oder Nutzeranforderungen nicht aus Convenience selbst definieren.

Robustes Muster:

```text
Domain / Live Work
→ Problem und fachliche Invarianten
↔ Technical Discovery / Feasibility
→ Requirements-Reconciliation
→ Readiness Gate
→ erst dann Architecture / MVP / Development
```

### L-KW-14 – Menschliche und unabhängige Fachvalidierung bleiben eigene Funktionen

Human-in-the-loop ist nicht gleich unabhängige fachliche Validierung. Ebenso ist eine zweite KI-Instanz keine unabhängige Expertin.

Konsequenz: Review-Klassen, Reviewer-Unabhängigkeit und Validation Scope müssen zur Konsequenz der Aussage passen und dürfen nicht semantisch zusammenfallen.

### L-KW-15 – Reuse als Pattern, nicht als Cargo Cult

Die transferierbaren Einheiten aus Histo-Orla sind Prinzipien und Prüfregeln, **nicht** konkrete Issue-Nummern, JSON-Felder, Workflow Engines, Multi-Agent-Topologien oder einzelne Tools.

Ein neues Wissensarbeitsprojekt sollte jeweils fragen:

- Welche Fachdomänen führen hier wirklich?
- Welche Zustände und Invarianten sind für diesen Kontext consequential?
- Welche davon lassen sich formalisieren?
- Welche Toolunterstützung ist die kleinste hinreichende?
- Welche Teile von Histo-Orla sind irrelevant oder sogar schädlich, wenn man sie ungeprüft überträgt?

## 3. Minimaler Start-Blueprint für neue Wissensarbeitsprojekte

Ein zukünftiges Projekt kann diese Reihenfolge als **Hypothese** testen:

```text
1. reales Nutzerproblem + reale Arbeitsprobe
2. führende Fachdomäne(n) und fachlicher SOTA
3. Evidenz-/Provenienz-/Unsicherheitsmodell
4. priorisierte Domain Methods für reale Problemtypen
5. Live-Pilot mit Friktions-/Failure-Erfassung
6. Capability-/Requirement-Candidates
7. Generalisierung + Acceptance Criteria
8. technische SOTA-/Tool-/Feasibility-Discovery
9. Readiness Gate
10. Architektur / MVP / Development
11. Fresh-context Restart-/Audit-Test
12. erneute Live-Evaluation und Reopening bei neuer Evidenz
```

Nicht jeder kleine Wissensworkflow braucht die volle Form. Die Strenge soll **proportional zur Konsequenz, Evidenzkomplexität und Dauerhaftigkeit des Wissenszustands** sein.

## 4. Was vor Cross-Project-Promotion noch geprüft werden muss

Vor einer Nutzung als organisationsweiter Standard sollten die Learnings mindestens gegen mehrere andersartige Wissensprojekte getestet werden, beispielsweise:

- quellennahe historische Forschung;
- wissenschaftliche Literatur-/Evidence-Synthese;
- Rechts-/Policy-Analyse;
- daten-/modellgestützte Fachanalyse;
- ein stärker kollaboratives Projekt mit mehreren menschlichen Fachrollen.

Besonders zu falsifizieren sind:

- ob eine explizite Method-Truth-Schicht überall nötig ist oder nur bei hoher Fach-/Evidenzkomplexität;
- wie viel Work-Context-Struktur nötig ist, ohne Bürokratie zu erzeugen;
- welche Promotion-Gates wirklich cross-domain generalisierbar sind;
- welche Restartability-Metriken sich in anderen Werkzeuglandschaften bewähren.

## 5. Leitformeln für zukünftige Projekte

> **Der Nutzer darf unscharf fragen; das System muss fachlich sauber arbeiten.**

> **Live-Arbeit ist nicht nur Nutzung, sondern Evidence über das System.**

> **Method Truth vor Modellplausibilität.**

> **Exploration offen; Promotion evidenz- und methodengebunden.**

> **Interne Strenge darf nicht zur Nutzerbürokratie werden.**

> **Ein neuer Kontext muss ohne Gedächtnis des alten Chats korrekt fortsetzen können.**

> **Übertrage Prinzipien, nicht die zufällige Form des Pilotprojekts.**
