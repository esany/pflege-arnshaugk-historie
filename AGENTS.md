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
7. bei technischen Änderungen #42/#43 sowie aktuelle Architecture Contracts/ADRs.

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

Aktuelle akzeptierte Requirements: `docs/research/synthesis/requirements-baseline.md` (#42).  
Architecture Gate: `docs/research/synthesis/architecture-readiness.md` (#43).  
Architecture Execution Owner: #48.

Regeln:

- keine technische Komponente ohne Requirement/Acceptance-Kriterium oder expliziten Owner Constraint;
- keine konkrete Technologie als Requirement tarnen;
- deterministische Invarianten deterministisch erzwingen, soweit möglich;
- Provider/Tools hinter austauschbaren Grenzen halten, wenn Lock-in wissenschaftlichen State gefährden könnte;
- Secrets/Credentials niemals in Git/Research State;
- Code/Prototypen müssen auf Work Owner, Requirement und Testziel rückführbar sein;
- jeder technische Spike dokumentiert Hypothese, Setup, Ergebnis, Failure Modes und Disposition (`adopt | adapt | reject | more-test`);
- kein MVP/Framework nur aus Präferenz; kleinste hinreichende Lösung bevorzugen.

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