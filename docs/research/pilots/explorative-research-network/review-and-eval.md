# Review- und Evaluationsrahmen für Pilot #86

## 1. Zweck

Der Pilot darf nicht allein deshalb bestehen bleiben, weil das Modell sprachlich überzeugend wirkt. Er muss gegen vorhandene Histo-Orla-Mechanismen, die generische Wissensarbeit-Basis und reale Forschungsnutzung geprüft werden.

Work Owner:

- #86 Pilot / Gesamtdisposition
- #87 unabhängiges Review
- #88 minimaler Prototyp nach Review
- #89 Evaluation unter Restart-/Rekombinationsstress

## 2. Review-Reihenfolge

### Schritt A – frischen Repo-Zustand lesen

Reviewer liest mindestens:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. Root `README.md`
4. `docs/research/README.md`
5. `docs/research/source-identity-protocol.md`
6. `docs/research/methods/README.md`
7. #86 und diese Pilotdateien
8. die jeweils einschlägigen kanonischen Artefakte aus #28/#29/#30/#41/#45/#50/#60/#63.

Für generische Aussagen zusätzlich frischer `main`-Stand von `esany/Wissensarbeit`, insbesondere Governing Objective, Lifecycle, Authority, Competence, Material State, Building Blocks und Pilot-Learnings.

### Schritt B – bestehende Abdeckung zuerst

Für jedes Element des Pilotmodells muss zuerst geprüft werden:

- existiert die Fähigkeit bereits?
- ist nur eine andere View/Komposition nötig?
- entsteht tatsächlich neue fachliche/systemische Semantik?
- würde eine neue Struktur eine zweite Wahrheit erzeugen?

### Schritt C – wissenschaftliche Methodenprüfung

Je materialem Forschungsmodul prüfen:

- welche Fachkompetenz führt?
- welches Method Profile ist validiert/working/fehlend?
- welche Evidenz trägt welchen Schluss?
- welche Schlüsse sind verboten oder nur Hypothese?
- welche Scale-Shift-/Vergleichsannahmen werden gemacht?

### Schritt D – Minimalität

Jede zusätzliche Datei, ID, Relation oder Statusklasse muss eine reale Friktion lösen. Future-Proof-Struktur ist ein Negativbefund.

## 3. Review-Dispositions

Jedes wesentliche Element erhält genau eine Candidate-Disposition:

- `reuse-existing` – vorhandener Mechanismus reicht.
- `adapt-case-specific` – sinnvoll im Ranis/Orlatal-Pilot, nicht generisch.
- `requirement-candidate` – wiederkehrender Histo-Orla-Systemneed möglich; Authority #42 erforderlich.
- `generic-learning-candidate` – potenziell für `Wissensarbeit`, aber nur nach Generic-Fit und wiederholter Friktion.
- `reject` – methodisch/organisatorisch unnötig oder schädlich.
- `defer` – nicht genug Evidenz für eine Entscheidung.

Keine Disposition ist durch diese Datei selbst accepted.

## 4. Kernfragen für #87

1. Ist `Question as lens, not container` mit Histo-Orla vereinbar oder nur neue Terminologie für bestehende Mechanismen?
2. Braucht der gemeinsame Research State neue persistente Relationstypen oder reichen referenzierte Research-Artefakte/Derived Views?
3. Welche Frageoperationen (`split/fuse/reframe/...`) sind bereits durch bestehende Lifecycle-/Integration-Mechanismen abgedeckt?
4. Reicht die bestehende Capability Map für materialgetriebene Exploration, oder fehlt ein nachweisbarer Need?
5. Wie verhindert der Pilot Taxonomie-/Graph-Overengineering?
6. Welche Teile müssen unter #60 fachmethodisch geprüft werden, bevor sie als Workflow gelten dürfen?

## 5. Evaluation #89

### E1 Restartability

Ein neuer Bearbeiter muss ohne Altchat rekonstruieren können:

- wozu der Pilot existiert;
- welche Materialklassen/Friktionen ihn auslösten;
- welche Fragen aktiv/offen sind;
- welche Evidenz/Provenienz stabil ist;
- welche Teile Candidate sind;
- welche nächsten Aktionen erlaubt sind.

### E2 Rekombination

Eine einzelne Source-/Observation-Identität wird in mindestens zwei verschiedenen Research Modules referenziert. PASS nur, wenn keine duplizierte Truth entsteht und beide Module unterschiedliche zulässige Interpretationskontexte haben.

### E3 Analyse↔Synthese

Mindestens ein Ablauf muss zeigen:

`Detailfinding → Synthese-Candidate → kritische Annahme → neue Detailfrage`.

### E4 Überblick↔Detail / Scale Shift

Mindestens ein Ablauf wechselt zwischen Fundstelle und regionaler Ebene. PASS nur, wenn der Maßstabswechsel explizit ist und keine historische Beziehung aus bloßer Nähe folgt.

### E5 Ergebnisoffenheit

Mindestens eine Forschungsfrage wird begründet `split`, `reframe`, `fuse`, `supersede` oder `defer`, ohne Verlust ihrer bisherigen Inputs/Outputs.

### E6 Kompetenzrouting

Mindestens zwei Module müssen unterschiedliche führende Kompetenzen besitzen; fachliche Führung und controlling competence müssen begründet sein.

### E7 Non-loss / epistemic hygiene

Alte Museumslabels, unsichere OCR, Nutzerfoto-Observationen und aktuelle Fachliteratur dürfen nicht in dieselbe Evidence-Klasse fallen.

### E8 Lean fit

Reviewer identifiziert ausdrücklich, welche Pilotstrukturen nicht benötigt wurden. Ein Pilot, der nur durch zunehmende Meta-Struktur funktioniert, gilt als problematisch.

## 6. Zwei-Chat-Test

Nach einem eventuellen Prototyp #88:

- **Chat A – Detail:** bearbeitet eine enge Frage aus dem gemeinsamen Bestand.
- **Chat B – Synthese:** bearbeitet unabhängig eine übergreifende/Scale-Shift-Frage aus demselben Bestand.

Beide starten ausschließlich aus GitHub. Danach vergleichen:

- Source-/Instance-Identitäten;
- verwendete Findings und deren Status;
- neue Relationen/Fragen;
- Widersprüche;
- versteckte Annahmen;
- Abhängigkeit von nicht persistiertem Chatwissen.

## 7. Abschlussentscheidung

#86 endet mit genau einer Hauptdisposition:

- `archive pilot`
- `keep case-specific`
- `promote Histo-Orla requirement candidate`
- `return generic learning candidate to Wissensarbeit`

Kombinationen sind möglich, aber jede Teilpromotion braucht ihren zuständigen Owner/Authority-Pfad. Kein Merge des Pilotbranches allein gilt als wissenschaftliche oder systemische Acceptance.
