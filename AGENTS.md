# Histo-Orla – Repository-wide Agent & Handoff Contract

**Status:** binding repository governance  
**Scope:** gesamtes Repository  
**Governance Owner:** #9  
**Issue-/Ownership-Regeln:** #23  
**Research Quality:** #45

## 1. Oberste Arbeitsregel

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

Kein für die Fortsetzung notwendiger Forschungs-, Requirements-, Architektur-, Entwicklungs- oder Entscheidungsstand darf ausschließlich in einem Chat, verborgenem Modellzustand, Scratchpad oder einer Agentenkommunikation verbleiben.

Ein neuer kompetenter Bearbeiter muss jederzeit ohne Kenntnis früherer Chats aus dem Repository rekonstruieren können:

- Ziel und Präzedenz des Projekts;
- aktuelle Phase und aktive Work Owner;
- abgeschlossene Baselines und Entscheidungen;
- offene Fragen, Research Debt und echte Blocker;
- relevante wissenschaftliche/technische Invarianten;
- nächste ausführbare Aktionen;
- kanonische Artefakte und ihre Provenienz.

## 2. Pflicht-Bootstrap vor substantieller Arbeit

Vor jeder substantiellen Arbeit am Projekt ist **der aktuelle Repo-Zustand neu zu lesen**. Chat-Erinnerung ist kein kanonischer Input.

Mindestens in dieser Reihenfolge:

1. `AGENTS.md` – bindende Arbeits-/Handoff-Regeln;
2. `PROJECT_STATE.md` – aktueller phasenübergreifender Handoff-Snapshot;
3. `README.md` – Projektziel, Präzedenz und Einstieg;
4. zuständiges Work-Owner-Issue;
5. dort verlinkte kanonische Research-/Architecture-/Development-Artefakte;
6. bei Research zusätzlich #45 und einschlägige Fachartefakte;
7. bei technischen Änderungen #42 sowie aktuelle Architecture-/Assurance-Contracts und einschlägige Decisions/ADRs.

Wenn `PROJECT_STATE.md` erkennbar hinter jüngeren Issues/Commits zurückliegt, gilt der jüngere kanonische Work-Owner-Stand; `PROJECT_STATE.md` ist dann vor Abschluss der Arbeit zu aktualisieren, sofern die Abweichung handoff-relevant ist.

## 3. Präzedenz und kanonische Wahrheit

Repository-intern gilt für Projektwissen:

```text
bindende Governance / akzeptierte Requirements / getroffene ADRs
→ kanonische Fach-/Research-/Architecture-Artefakte
→ aktueller Work-Owner-Status im Issue
→ PROJECT_STATE.md als Handoff-/Navigationssicht
→ ältere Konzept-/Prior-Art-Dokumente
→ Chatverlauf / Modellgedächtnis
```

`docs/research-design/transdisziplinaerer-literaturassistent.md` ist ein wichtiges **foundational design document**, aber nach Abschluss von #28–#43 nicht mehr alleiniger aktueller Operations-/Requirements-Stand. Neuere Requirements, Gate-, Architecture- und ADR-Artefakte besitzen für ihre jeweilige Frage Vorrang.

## 4. Handoff Gate – vor Abschluss jeder substantiellen Arbeit

Vor dem Beenden einer substantiellen Arbeit ist zu prüfen:

1. **Was hat sich geändert?**
2. **Wo ist der kanonische Ort dieser Änderung?**
3. **Ist der Work-Owner-Status aktuell?**
4. **Sind Begründung/Evidenz/Trade-offs dort nachvollziehbar?**
5. **Sind offene Fragen und nächste Aktionen sichtbar?**
6. **Sind echte Blocker in #44 isoliert?**
7. **Kann ein neuer Bearbeiter ohne diesen Chat fortsetzen?**

Wenn eine dieser Fragen mit `nein` beantwortet wird, ist die Arbeit **handoff-incomplete** und vor Abschluss im Repo nachzuziehen.

Kann aus technischen/Rechte-Gründen nicht persistiert werden, muss im sichtbaren Ergebnis ausdrücklich stehen:

`HANDOFF INCOMPLETE` + betroffener Stand + vorgesehener kanonischer Ort.

## 5. Was zwingend persistiert werden muss

Persistenzpflicht besteht insbesondere für:

- neue oder geänderte Ziele/Constraints;
- substantive Research Findings und Search Boundaries;
- Requirement-/Capability-/Quality-Candidates mit Folgeauswirkung;
- validierte Requirements und Änderungen ihrer Traceability;
- Architekturannahmen, Contracts, Experimente und Ergebnisse;
- technische Entscheidungen/ADRs;
- Implementationsstand, relevante Tests und bekannte Failure Modes;
- Dependencies, Reihenfolgeänderungen und Blocker;
- Rights-/Credential-/Provider-Grenzen;
- verworfene Alternativen, wenn ihre Wiederholung später wahrscheinlich wäre.

Nicht jeder Gesprächssatz, Brainstorming-Schnipsel oder triviale Zwischenstand muss archiviert werden.

## 6. One fact / one canonical home

```text
Issue
= Work Owner / Scope / Status / Dependencies /
  kurze Synthese / offene Punkte / nächste Aktion

versioniertes Artefakt
= substantieller kanonischer Inhalt /
  Evidenz / Analyse / Contracts / Tests / Decisions

Chat
= transienter Arbeitsraum
```

Vollinhalte nicht parallel manuell in Issue, Datei und Chat pflegen.

## 7. Neue Issues

Ein neues Issue nur, wenn mindestens eines gilt:

1. eigenständiger Problem-/Research-Scope;
2. eigenständiges Work Package mit eigener Definition of Done;
3. unabhängig testbarer Spike/Hypothese;
4. echte Decision/ADR/Dependency;
5. eigenständiger Audit-/Review-Auftrag.

Keine Issue-Explosion für einzelne Findings oder bloße Umformulierungen.

## 8. Research-Regeln

Für Research gelten #45 und `docs/research/source-identity-protocol.md`.

Harte Grundlinien:

- Fachdomänen führen; Technologie dient.
- Quelle/Instanz/Derivat/Fundstelle/Finding/Interpretation getrennt halten.
- AI-Ausgabe ist keine Evidenz und keine unabhängige Expertenvalidierung.
- Negative Findings brauchen Search Boundaries.
- Unsicherheit, Widerspruch und `unresolved` sind gültige Zustände.
- Konsequenzielle Aussagen brauchen proportionale Validierung.

## 9. Architektur-/Development-Regeln

Aktuelle akzeptierte Requirements: `docs/research/synthesis/requirements-baseline.md` + `requirements-extensions.md` (#42).  
Technical Lead: #48.  
Development & Verification: #59.  
#43 ist historischer Readiness-Stand und kein aktuelles Blocking-Gate.

Regeln:

- keine technische Komponente ohne Requirement/Acceptance-Kriterium oder expliziten Owner Constraint;
- keine konkrete Technologie als Requirement tarnen;
- deterministische Invarianten deterministisch erzwingen, soweit möglich;
- Provider/Tools hinter austauschbaren Grenzen halten, wenn Lock-in wissenschaftlichen State gefährden könnte;
- Secrets/Credentials niemals in Git/Research State;
- Code/Prototypen müssen auf Work Owner, Requirement, Nutzer-/Forschungsdriver und Testziel rückführbar sein;
- jeder technische Spike dokumentiert Hypothese, Setup, Ergebnis, Failure Modes und Disposition (`adopt | adapt | reject | more-test`);
- kleinste hinreichende Lösung bevorzugen; Lean/Agile reduziert niemals still Scope oder Qualitätsmaßstab;
- formale Requirements-QA wird durch #62 operationalisiert;
- Value-/Decision-/Delivery-/Feedback-Traceability wird durch #63 operationalisiert.

## 10. Current-State-Datei

`PROJECT_STATE.md` ist die **zentrale Handoff-/Navigationssicht** des Projekts.

Sie ist keine zweite Vollwahrheit neben Research-/Architecture-Artefakten, sondern enthält nur:

- aktuelle Phase;
- zuletzt erreichte Gates;
- aktive Work Owner;
- echte Blocker;
- aktuelle cross-cutting Constraints;
- nächste ausführbare Arbeit;
- Pointer auf kanonische Artefakte.

Sie wird bei materiellen Phasen-, Ownership-, Gate-, Decision- oder Dependency-Änderungen aktualisiert.

## 11. Gültigkeit für neue Chats / Agenten

Jeder Bearbeiter, der Repository-Zugriff besitzt, soll diesen Bootstrap anwenden. Ein normaler Chat ohne automatischen Repo-Bootstrap darf **nicht behaupten**, den aktuellen Projektstand zu kennen, bevor er `AGENTS.md` und `PROJECT_STATE.md` sowie die einschlägigen Owner-Artefakte gelesen hat.

Wenn eine Plattform diese Datei nicht automatisch lädt, muss die Projekt-/Workspace-Instruktion den Bootstrap explizit verlangen.

## 12. Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert Requirements; Dev besitzt sie nicht.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Kein Handoff hängt vom Gedächtnis eines Chats ab.**

## 13. Verbindlicher Work-Context-, Methoden- und Handoff-Vertrag

Für jede **substanzielle** Arbeit reicht Repo-Bootstrap allein nicht. Vor der eigentlichen Ausführung muss der aktuelle Work Context aus Repository-State und Auftrag so bestimmt sein, dass Scope, Autorität und Methodik nicht still aus Chat-/Modellplausibilität entstehen.

Das ist ein **Arbeitsfunktionsvertrag**, keine Agentenklasse und kein neuer Truth Store.

### 13.1 Primäre Arbeitsfunktion

Ein substantieller Work Context muss zu jedem Zeitpunkt eine primäre Funktion erkennen lassen, zum Beispiel:

- Domain / Source Research;
- Cross-disciplinary Domain Review / Requirements;
- Architecture / Development / Research Software Engineering;
- Governance / Owner-Decision Support;
- Qualified Independent Specialist Review.

Mehrere Fachkompetenzen dürfen gleichzeitig aktiv sein. Entscheidend ist, dass nicht mehrere inkompatible **Autoritäten** still gleichzeitig ausgeübt werden.

Ein Rollen-/Funktionswechsel ist zulässig, muss aber an einer materiellen Authority-Grenze als expliziter Handoff oder klarer Work-Context-Wechsel erfolgen.

### 13.2 Minimaler Start-/Resume-Context

Vor substantieller Arbeit muss aus dem kanonischen State mindestens rekonstruierbar sein:

```text
PRIMARY FUNCTION
CURRENT CANONICAL TASK / WORK OWNER
PURPOSE / BOUNDED QUESTION OR TASK
SCOPE / EXCLUSIONS
LEADING + CONTROLLING DOMAINS / REQUIRED COMPETENCIES
APPLICABLE METHOD / QUALITY FRAME
REQUIRED CANONICAL CONTEXT + EVIDENCE
MAY DECIDE / DO
MUST NOT DECIDE / DO
STOP / HANDOFF WHEN
COMPLETION / RETURN CONDITION
CANONICAL PERSISTENCE TARGET
```

Diese Informationen sollen soweit möglich aus bestehenden Ownern, Artefakten und Requirements **abgeleitet** werden. Der Nutzer soll kein Verwaltungsformular ausfüllen und keine deterministisch lösbaren Rollen-/Pfad-/Validatorfragen entscheiden müssen.

Nicht jeder triviale Chat benötigt diese Zeremonie. Sobald Research-, Requirements-, Architektur-, Development-, Decision- oder andere continuation-critical Arbeit entsteht, gilt der Vertrag.

### 13.3 Domain Method Profiles und Method Status

Domänenspezifische Fachmethodik wird unter #60 / `docs/research/methods/` operationalisiert. Ein Fachlabel oder Rollenprompt ist kein Methodennachweis.

Für consequential Research gilt:

- `method-candidate` darf Exploration, Hypothesenbildung und Tests anleiten;
- als reguläre consequential operative Fachmethode darf nur `working-method` oder höher verwendet werden;
- fehlt ein hinreichend validiertes Domain Method Profile, darf die Forschung als `candidate / exploratory / method-debt` fortgeführt werden, aber **nicht durch Modellplausibilität consequential promoted** werden;
- `validated-method` darf nur behauptet werden, wenn die im Profilvertrag geforderte unabhängige/qualifizierte Validierung tatsächlich vorliegt;
- konkrete Method Application, Finding und Prompt bleiben voneinander getrennte Zustände.

Leitregel:

> **Exploration darf offen sein. Promotion ist fail-closed gegenüber fehlender Method-/Evidence-/Validation-Grundlage.**

### 13.4 Formale Invarianten vs. wissenschaftliches Urteil

Gemäß `REQ-WF-001` müssen formal prüfbare Schutzregeln technisch/deterministisch erzwungen werden, sobald die entsprechende Implementationsschicht vorhanden ist; sie dürfen nicht dauerhaft nur Prompt-Compliance bleiben.

Maschinenprüfbar sind beispielsweise – soweit im jeweiligen Contract formalisiert:

- erforderliche Referenzen/Parentage;
- Status-/Authority-Transitionen;
- zulässiger Method-Status vor consequential Promotion;
- vorhandener Work Owner / Scope / Persistence Target;
- Evidence-/Findspot-Referenz für evidenzielle Findings;
- Trennung AI-Output vs. Evidence;
- erforderliche Review-/Validation-Klasse;
- Handoff-Vollständigkeit;
- Referenzintegrität und History-Erhalt.

**Nicht** deterministisch als fachliche Wahrheit zu entscheiden sind insbesondere:

- historische Interpretation;
- Quellenlesung, soweit sie fachliches Urteil verlangt;
- Identität/Relation/Motiv, wenn Evidenz sie nicht formal entscheidet;
- fachliche Suffizienz eines Arguments jenseits formal etablierter Gates;
- unabhängige Expert:innenübereinstimmung.

Software darf wissenschaftliches Urteil strukturieren, begrenzen und auditierbar machen, aber nicht durch Validatorlogik simulieren.

### 13.5 Gerichtete Handoffs an Authority-/Kompetenzgrenzen

Ein materieller Handoff muss so viel strukturierten Zustand übertragen, dass der empfangende Work Context ohne alten Chat korrekt weiterarbeiten kann.

Mindestens proportional zur Konsequenz:

```text
FROM FUNCTION
TO FUNCTION
TRIGGER
CANONICAL TASK / OWNER
EVIDENCE / INPUT
ESTABLISHED
UNRESOLVED / NOT INVESTIGATED
APPLICABLE REQUIREMENTS / METHODS
REQUEST
MAY
MUST NOT
NON-GOALS
ACCEPTANCE / RETURN CONDITION
CANONICAL PERSISTENCE TARGET
```

Verbindliche Hauptrichtung:

```text
Domain/Source Research
→ Domain Review / Requirements
→ bei akzeptiertem technischen Bedarf: Architecture/Dev
→ technische Verifikation
→ scholarly adequacy return review
→ Research NEXT ACTION
```

Dev darf einen unklaren fachlichen Auftrag **nicht** aus technischer Convenience selbst präzisieren. Fehlt eine materiell notwendige Fachsemantik, Requirement-/Owner-Grundlage oder Acceptance-Grenze, wird die betroffene Entscheidung zurückgegeben statt erfunden.

Umgekehrt darf Domain Research keine Architekturentscheidung allein deshalb setzen, weil sie im Einzelfall plausibel erscheint.

### 13.6 Unabhängige Fachvalidierung

AI-assisted Domain Research, AI-assisted Domain Review und methodenkonforme interne Review sind **keine** unabhängige qualifizierte Fachvalidierung.

Wo Konsequenz/Fachstandard unabhängige Validierung verlangt, erfolgt ein eigener Specialist-Handoff mit exakter Evidenz, Review-Frage, Alternativen, Kontextgrenzen, Validation Scope und residualer Unsicherheit.

Der nicht-spezialisierte Research Owner wird nicht als Ersatz-Spezialist verwendet.

### 13.7 Restartability-Test

Ein Work Context gilt nicht als restartbar, nur weil Dokumente existieren.

Ein neuer kompetenter, autorisierter Bearbeiter muss aus Repository + kontrollierter Evidenz ohne alten Chat bestimmen können:

1. was die aktuelle Aufgabe ist;
2. welche primäre Funktion/Autorität gilt;
3. welche Method Profiles/Requirements gelten und welchen Status sie besitzen;
4. welche Evidenz tatsächlich verfügbar und relevant ist;
5. welche nächste Aktion erlaubt ist;
6. wann/wohin ein Handoff erfolgen muss;
7. wo der resultierende State kanonisch persistiert wird.

Wenn die aktuelle NEXT ACTION direkte Quelleninspektion verlangt, muss die benötigte konkrete Instanz im autorisierten Work Context tatsächlich erreichbar/inspectable sein; bloße Identifizierbarkeit oder theoretische Reproduzierbarkeit genügt nicht.

### 13.8 Technische Operationalisierung

Der verbindliche Governance-Vertrag definiert **was** abgesichert werden muss, nicht **welches Tool** dies implementiert.

Aktuelle Assurance-Owner:

- #61 – Work-Context / Method-Conformance / Handoff-Hardening;
- #62 – deterministische Requirements-QA;
- #63 – Value-/Decision-/Delivery-/Feedback-Traceability.

Schnittstellen bestehen zu #50 Canonical State, #54 Promotion/Invariants, #55 Audit View und #57 Restartability.

Technologie wird gegen State of the Art / Best Practice und die kleinste hinreichende Lösung geprüft. Maschinenlesbare Contracts, Provenance-/Research-Object-Standards, Policy-/Transition-Enforcement oder Validatoren sind Kandidaten; kein Standard/Framework wird allein wegen Vollständigkeit eingeführt.

## 14. Verbindliche Value-/Decision-/Delivery-/Feedback-Traceability

Die eigentliche Projektursache bleibt **Nutzer-/Forschungswert**: Goals, Needs, Pains, Erkenntnisprobleme, wissenschaftliche Constraints und reale Research-Friktion. Requirements operationalisieren daraus das erwartete Systemverhalten; technische Entscheidungen bestimmen nur die Mittel.

Für materielle technische Arbeit muss deshalb ohne Chat rekonstruierbar sein:

```text
Goal / Need / Pain / Constraint
→ accepted Requirement
→ technische Entscheidung bzw. begründete reversible Direktumsetzung
→ Implementation
→ Verification
→ reale Nutzung / Owner-Feedback
→ bestätigt | Pain bleibt | Regression | neuer Need | Requirement-/Decision-Delta
```

### 14.1 Materielle technische Entscheidungen

Jede materielle technische Entscheidung/Implementierung muss proportional zur Tragweite mindestens referenzieren:

- accepted Requirement(s) oder expliziten Owner Constraint;
- relevante `G-* / N-* / P-*` Driver bzw. deren kontrollierte Traceability;
- anwendbare Governance-/Quality-Regeln;
- technische Entscheidung oder begründete `decision_not_required`-Ausnahme für rein mechanische/reversible Arbeit;
- Implementation-/Test-/Verification-Referenzen nach tatsächlicher Umsetzung.

Eine technische Präferenz, ein Framework oder ein LLM darf diese Kette nicht ersetzen.

### 14.2 Deterministischer Guard

Formal geklärte Teile werden unter #62/#63 durch Schema, Validatoren, Regressionstests und CI geprüft. Insbesondere gilt für im Technical Scope kontrollierte Code-/Workflow-Pfade:

> **Neue materielle technische Änderungen dürfen nicht untracebar ins Repository gelangen.**

Ein früherer `verified` Implementation-Record darf einen Pfad nicht dauerhaft freischalten; neue Änderungen brauchen einen aktuellen aktiven/implementierten Trace-Kontext.

### 14.3 Nutzer-/Owner-Feedback

Reale Nutzung und Owner-Feedback schließen die Delivery-Schleife.

- Feedback zu Bedienbarkeit, Research-Pain, Nutzen, fehlender Funktion oder Fehlverhalten ist Product-/Workflow-Evidence;
- es ist **keine historische/wissenschaftliche Evidenz**;
- negatives oder scope-relevantes Feedback wird als eigener Feedback-/Delta-Pfad persistiert;
- Feedback darf Requirements, Method Truth oder Governance nicht still mutieren;
- ein daraus folgender Requirement-Delta geht an #42, Method-Delta an #60, Owner-/Scope-Entscheidung ggf. an #44;
- ein Requirement, dessen Verification ausdrücklich `owner-workflow-acceptance` verlangt, darf nicht allein durch technische Tests als `verified` gelten.

### 14.4 Skill/LLM-Rolle

Skills/LLMs dürfen Trace-Records vorbereiten, Validatoren ausführen, Ergebnisse erklären und mechanische Fixes vorschlagen. Sie dürfen niemals:

- einen nicht ausgeführten Check als PASS behaupten;
- fehlende Nutzer-/Domain-Bedeutung erfinden;
- Owner-Acceptance oder Fachvalidation simulieren;
- negative Feedback-/Delta-Pfade still schließen.

Kanonischer technischer Vertrag: `docs/architecture/assurance/value-decision-delivery-assurance.md` (#63).
