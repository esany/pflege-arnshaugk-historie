# Generic System Analysis + Finding-Driven Deep Research Prompt v3

**Version:** 2026-09-22  
**Purpose:** vendor-neutraler Analyse-/Research-Baustein für komplexe Projekte.  
**Authority:** Analyse- und Researchinstrument; keine Requirement-, Architektur-, Methoden-, Selection-, Delivery- oder Entscheidungsautorität.

---

## 0. Purpose + Hard Boundaries

Untersuche das Projekt als **sozio-technisches System** und erzeuge aus seinem empirischen Zustand die Research Agenda für eine tiefe externe Gegenprüfung.

Hauptpfad:

```text
empirische Projekt-/Systemanalyse
→ relevante Befunde und Problemcluster
→ konkurrierende Erklärungen
→ Research Agenda
→ finding-driven Deep Research
→ theoretische + methodische + empirische Vertiefung
→ Related Work / Best Practice / Gegenbefunde
→ analytische Rückbindung
→ Research Gaps / unresolved
→ STOP
```

Die Untersuchung darf Problemverständnis vertiefen, Hypothesen stärken, schwächen, reframen oder falsifizieren. Sie darf **keine** Zielarchitektur, Lösungsauswahl, Roadmap, Implementierungsreihenfolge, Tool-Adoption oder Projektpriorität ableiten.

Arbeite evidenzorientiert, nicht bestätigungsorientiert. Positive Mechanismen und Gegenbeispiele sind ebenso wichtig wie Fehler. `unresolved` ist ein gültiges Ergebnis.

---

## 1. Evidence / Current-State Reconstruction

Lies den aktuellen Projektzustand nach der vorhandenen Projekt-Governance frisch ein. Behandle frühere Audits, Reports und Diagnosen als **prior hypotheses / prior interpretations / research leads**, nicht als Wahrheit. Revalidiere sie gegen möglichst primäre oder zeitnahe Evidence.

Rekonstruiere mindestens:

- Projektintent, Nutzer-/Owner-Ziele und reale Arbeitspraktiken;
- Fachdomäne(n), Evidenz- und Qualitätsmaßstäbe;
- Requirements-/Produktlogik;
- technische Strukturen und tatsächliche Nutzung;
- Organisation, Rollen, Handoffs und Entscheidungswege;
- epistemische Architektur: Evidence, Interpretation, Authority, Unsicherheit;
- wichtige Entwicklungs-, Nutzungs-, Fehler- und Korrekturepisoden.

Trenne zentrale Aussageklassen sichtbar:

- **Project Evidence**
- **User/Owner Evidence**
- **External Research Evidence**
- **Related-System Evidence**
- **Researcher Inference**
- **Open Hypothesis**

Kennzeichne substantielle Projektbefunde nach ihrem heutigen Status:

`current-active | recurring | historical-resolved | historical-with-latent-risk | protective/recovery-mechanism | one-off/tool-specific | unresolved`

Historische Befunde dürfen nicht still als aktueller Projektzustand ausgegeben werden.

---

## 2. Empirical System Analysis

Analysiere Fachdomäne, Nutzerarbeit, Requirements/Produktlogik, Technologie, Organisation und epistemische Architektur **gleichrangig**. Reduziere das Projekt weder auf Software noch auf Fachlichkeit.

Rekonstruiere relevante Episoden nicht nur chronologisch, sondern kausal vorsichtig:

```text
Ausgangslage / Trigger
→ damals verfügbare Evidence
→ damalige Interpretation
→ Intervention / Verhalten
→ beobachtete Wirkung
→ Nebenwirkung / Korrektur / Recovery
→ heutiger Status
```

Suche dabei nach:

- wiederkehrenden oder besonders folgenreichen Friktionen;
- Near Misses, Recovery Mechanisms und positiven Gegenbeispielen;
- Spannungen zwischen lokalem Erfolg und Gesamtsystemwirkung;
- Abweichungen zwischen formaler Korrektheit und realem Nutzen;
- notwendiger versus erzeugter Komplexität.

Unterscheide, soweit empirisch möglich:

`essential domain | accidental technical | organizational | interface | governance/control | user-transferred complexity`

Keine dieser Klassen ist per se schlecht oder vermeidbar.

---

## 3. Need → System / Interface Analysis

Untersuche, wie Nutzer-/Domänenbedürfnisse, Nichtwissen, Unsicherheit, Evidenz und Constraints durch das Projekt in Requirements, Organisation, technische Strukturen und tatsächliche Nutzung übersetzt werden.

Kernfrage:

> **Wo entstehen dabei empirisch erkennbare Passung, Fehlpassung, Verlust, zusätzlicher Wert, Koordinationslast oder Recovery?**

Unterscheide bei wichtigen Signalen:

```text
beobachtbares Need / Pain / Nichtwissen / Mental Model
→ fachliche Bedeutung
→ Projektinterpretation
→ Requirement / Prozess / technische Repräsentation
→ reale Wirkung
→ heutige Passfähigkeit
```

Behandle Schnittstellenprobleme als eigene Phänomene, nicht automatisch als Fehler nur einer Seite. Relevante Schnittstellen entstehen jeweils aus dem Fall; typische Beispiele sind Human↔AI, Domain↔Software, Requirement↔Implementation, Evidence↔State, Component↔System, Research↔Development und Development↔Feedback.

---

## 4. Problem Clusters + Competing Explanations

Verdichte die empirischen Beobachtungen erst **nach** der Rekonstruktion zu wenigen materiellen Problem-/Mechanismenclustern.

Für jeden Cluster dokumentiere:

- **Observed phenomenon**
- **Evidence + status**
- **Why it matters**
- **Possible mechanism(s)**
- **Competing explanations / confounders**
- **Positive or contradictory evidence**
- **What remains unexplained**
- **Current confidence**

Verwende vorhandene Fachbegriffe oder bekannte Anti-Pattern-Namen erst dann, wenn sie das beobachtete Phänomen tatsächlich besser erklären. Ein bekanntes Label ist keine Evidenz.

Ein Projekt darf auch überwiegend gut funktionieren; ein Audit muss nicht zwangsläufig Failure Patterns produzieren.

---

## 5. Research Agenda Gate

**Die Systemanalyse erzeugt die Research Agenda.** Externe Recherche beginnt für einen Problemcluster erst, wenn sein Forschungsbedarf explizit abgeleitet ist.

Für jeden wesentlichen Cluster bestimme kompakt:

| Feld | Inhalt |
|---|---|
| Project Finding | empirisch beobachteter Befund + Status |
| Unknown | was daran noch nicht verstanden ist |
| Competing Explanations | welche Erklärungen unterschieden werden müssen |
| Research Questions | Fragen, die diese Erklärungen diskriminieren können |
| Relevant Fields / Terms | passende Disziplinen + alternative Fachbegriffe |
| Theory Need | welche Erklärungsmechanismen zu prüfen sind |
| Method Need | wie das Phänomen in diesen Feldern empirisch untersucht wird |
| Evidence Need | geeignete empirische Evidenztypen / Standards |
| Related Work Need | sinnvolle Systeme, Fälle oder Infrastrukturen |
| Counterevidence Target | was die aktuelle Erklärung schwächen würde |
| Depth | Tier A / B / C |

### Research Depth

- **Tier A — central explanatory cluster:** tiefer Review/SOTA, Grundlagenliteratur, aktuelle Empirie, konkurrierende Theorie, Methodenliteratur, Gegenbefunde, Related Work/Fälle, Best-Practice-Evidence, Citation Chaining, Transferanalyse und Sättigungsprüfung.
- **Tier B — important supporting mechanism:** mehrere hochwertige Quellen plus gezielter Gegencheck und Transferanalyse.
- **Tier C — contextual point:** proportionale autoritative Verifikation.

Keine starre Mindestquellenzahl. Tiefe richtet sich nach Bedeutung und Unsicherheit des Befunds.

---

## 6. Finding-Driven Deep Research

Organisiere externe Forschung **primär nach den Problemclustern aus Phase A**, nicht nach einer vorab festgelegten Disziplinenliste.

Für jeden Tier-A-/Tier-B-Cluster untersuche proportional:

### Theory
Welche etablierten oder konkurrierenden Mechanismen erklären das Phänomen? Wie haben sich zentrale Begriffe verändert oder wurden kritisiert?

### Method
Wie prüft das jeweilige Forschungsfeld empirisch, ob der Mechanismus vorliegt? Welche Daten, Designs, Messgrößen, Validitätsrisiken und Confounder sind üblich?

### Empirical Evidence
Welche Reviews, Primärstudien, Standards oder belastbaren Fallstudien tragen, begrenzen oder widersprechen den Erklärungen?

### Related Work / Systems
Welche realen Systeme, Projekte oder Infrastrukturen bearbeiten ein vergleichbares Problem? Vergleiche Mechanismen, Bedingungen und Grenzen statt bloßer Features.

### Best Practice
Untersuche Praktiken nur als Evidenzobjekt:

```text
evidence base
→ population / context
→ observed benefit
→ costs / failure modes
→ preconditions
→ countercases / controversy
→ transferability
```

Keine Adoption Recommendation.

### Adversarial Research
Suche aktiv nach Gegenbefunden, alternativen Terminologien, konkurrierenden Schulen und Kontexten, in denen die vermutete Erklärung oder Praxis nicht trägt.

### Research Quality
Bevorzuge Primärliteratur, aktuelle Reviews, Standards und offizielle/technische Primärdokumentation passend zur Frage. Kennzeichne, ob Volltext/Primärquelle, Abstract/Metadata oder nur Discovery inspiziert wurde. Nutze bei zentralen Mechanismen backward/forward citation chaining, soweit sinnvoll.

Dokumentiere Search Boundaries bei negativen oder Vollständigkeitsbehauptungen.

Beende einen Cluster nicht, weil bereits eine kohärente Erzählung entstanden ist, sondern wenn zusätzliche hochwertige Suche überwiegend Wiederholung liefert, wesentliche Gegenpositionen geprüft sind und verbleibende Unsicherheit benannt werden kann.

---

## 7. Analytical Reconnection

Binde die externe Forschung zurück an den ursprünglichen Projektbefund. Sie darf dessen Framing verändern.

Für jeden zentralen Cluster bewerte mit Begründung:

`strengthened | weakened | reframed | contradicted | partial | conditional | unresolved`

Zusätzlich:

- Was erklärt externe Forschung besser als die ursprüngliche Projektanalyse?
- Welche Projektannahme wurde geschwächt oder falsifiziert?
- Welche Übertragungsgrenze verhindert einen direkten Schluss?
- Welche empirische Prüfung wäre nötig, um verbleibende Erklärungen zu unterscheiden?

Das ist **analytische Rückbindung**, keine Lösungsableitung.

---

## 8. Cross-Finding Tensions / Counterfindings

Prüfe clusterübergreifend:

- gemeinsame Mechanismen ohne sie vorschnell zu vereinheitlichen;
- Widersprüche zwischen Befunden;
- Trade-offs und Bedingungen, unter denen dasselbe Verhalten nützlich oder schädlich ist;
- positive Mechanismen, Recovery und starke Gegenbeispiele;
- Stellen, an denen externe Forschung das Projekt besser dastehen lässt als die Ausgangshypothese;
- Stellen, an denen der Projektzustand problematischer ist als frühere Audits angenommen hatten.

Kein einzelnes Gesamtnarrativ erzwingen.

---

## 9. Research Gaps / Unresolved

Halte sichtbar:

- nicht ausreichend erklärte Projektbefunde;
- konkurrierende Erklärungen ohne diskriminierende Evidence;
- unzugängliche oder schwache externe Evidenz;
- fehlende empirische Daten im Projekt;
- nicht übertragbare Best Practices;
- Forschungsfragen, bei denen weitere Suche voraussichtlich keinen Erkenntnisgewinn ohne neue Projektdaten liefert.

`unresolved` ist ein gültiger Abschluss.

---

## 10. Coverage + Evidence Matrix

Der Bericht endet mit einer kompakten Coverage-Sicht:

| Project Finding | Status | Research Questions | Depth | External Evidence | Related Work | Counterevidence | Reconnection | Remaining Uncertainty |
|---|---|---|---|---|---|---|---|---|

Prüfe vor Abschluss genau zwei systematische Fehlmodi:

1. **Unresearched Major Finding:** Ein zentraler Projektbefund wurde extern nicht proportional untersucht.
2. **Unanchored Research:** Ein substanzieller Research-Block besitzt keinen materiellen Projektbefund als Ausgangspunkt.

Wenn einer dieser Fälle vorliegt, recherchiere nach oder markiere die Lücke explizit.

---

## Abschlussgrenze

Beende mit:

1. den am stärksten belegten Projekt-/Problembefunden;
2. den wichtigsten Gegenbefunden und Reframings;
3. den wesentlichen Spannungen;
4. den größten verbleibenden Unsicherheiten;
5. den offenen Research Gaps.

**STOP vor Lösungsentwicklung.**

Keine Zielarchitektur. Keine Tool-/Framework-Empfehlung. Keine Roadmap. Keine Implementierungspriorität. Keine neue Governance. Keine Adoption-Entscheidung.
