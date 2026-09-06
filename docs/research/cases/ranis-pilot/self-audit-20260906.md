# Self-Audit 2026-09-06 – Ranis-Pilot

**Status:** `owner-feedback-response / self-audit / corrective-learning`  
**Work Owner:** #85  
**Branch:** `pilot/ranis-layered-archive-20260906`

## Anlass

Owner-Feedback in zwei Stufen:

1. Der angelegte Ranis-Pilot drohte das im Chat entstandene, eher didaktisch/vermittelnde Nebenprojekt über das bestehende Histo-Orla-Repository zu stülpen.
2. Die erste Korrektur ging noch nicht weit genug: **Nicht nur der Output, sondern die Forschungsfrage selbst musste aus der Vermittlungslogik herausgelöst werden.**

## Ergebnis der Selbstprüfung

**Ja, der erste Pilot war inhaltlich falsch gerahmt.**

Der Branch war technisch isoliert, aber die aktive Frage `Was kann ein wissenschaftlich interessierter Besucher ... wissen?` machte Vermittlung zum epistemischen Zentrum. Damit wurden Auswahl der Evidenz, Gliederung, Success-Kriterien und Outputs auf einen Besucher-/Erklärkontext hin optimiert.

Das widerspricht dem Repository-Ziel. Histo-Orla ist eine Forschungsassistenz für Quellenarbeit, fachmethodische Analyse und restartbaren Research State. Vermittlung kann aus Forschung abgeleitet werden, darf aber weder Forschungsfrage noch DoD bestimmen.

## Konkrete Fehlleistungen

### 1. Goal substitution by conversational momentum

Aus der unmittelbaren Situation des Chats – Besuch in Ranis, Wunsch nach anschaulicher Einordnung, Bildern und Vor-Ort-Erklärung – wurde still ein neues Forschungsziel erzeugt.

Fehlerpfad:

```text
situativer Nutzerkontext: Besuch / Erklärung
→ attraktive Vermittlungsfrage
→ Pilot-Forschungsfrage
→ Repo-Artefakte
```

Korrekt wäre:

```text
historische/archäologische Forschungsfrage
→ Quellen / Methoden / Evidenz
→ belastbarer Research State
→ optional abgeleitete Darstellung für einen konkreten Nutzungskontext
```

### 2. Forschungsfrage und View verwechselt

`Was ist vor Ort sichtbar?` kann eine nützliche **View-Frage** sein. Sie ist aber keine hinreichende historische Forschungsfrage.

Die eigentliche Forschungsfrage muss einen Erkenntnisgegenstand adressieren, z. B.:

> Wie lässt sich die paläolithische Nutzung der Ilsenhöhle aus Alt- und Neugrabung rekonstruieren, und welche Claims hängen an der Korrelation unterschiedlicher Evidenzachsen?

Diese Frage erzeugt Quellenarbeit, Unsicherheitsanalyse, Vergleich konkurrierender Modelle und neue diskriminierende Forschungsaktionen. Eine Besucherfrage tut das nur indirekt.

### 3. #64 zu formal statt inhaltlich angewandt

Der Audit-Befund `kleiner Vertical Slice statt Mega-Pilot` wurde zu schematisch umgesetzt. Ein Slice ist nicht gut, nur weil er klein und owner-lesbar ist. Er braucht einen **realen Forschungsgegenstand und Erkenntnisgewinn**.

### 4. Existing Research State nur referenziert, nicht als Denkform genutzt

Source Identity, Findspot, Claim-/Finding-Status, Method Truth und Restartability wurden zitiert, aber die Pilotfrage blieb außerhalb dieser Logik. Dadurch entstand lokale Struktur, bevor klar war, welche fachliche Frage sie tragen sollte.

### 5. Darstellungsnähe beeinflusst Evidenzauswahl

Die frühere Logik `sichtbar | aus Befund erschließbar | nur analytisch bekannt` ist didaktisch nützlich, aber sie sortiert Evidenz nach Wahrnehmbarkeit des Besuchers statt nach wissenschaftlicher Funktion.

Für den Forschungsstate ist die bessere Ordnung:

```text
Claim
→ Source / Instance / Findspot
→ Evidenzachse
→ Kontextqualität
→ Methode
→ Unsicherheit
→ konkurrierende Erklärung
→ Finding/Hypothesis/Unresolved
```

### 6. Zu viel Chat-Synthese vor Provenienzauflösung

Ein Teil der Synthese wurde aus dem Dialog vorstrukturiert. Der Research-State muss umgekehrt wachsen: konkrete Quelleninstanz und Fundstelle zuerst, Synthese danach.

## Vollständige Zielkorrektur v0.2

Die aktive Forschungsfrage lautet jetzt:

> **Wie lässt sich die paläolithische Nutzung der Ilsenhöhle in Ranis aus der Kombination von Hülle-Altgrabung und Neugrabung 2016–2022 belastbar rekonstruieren, und welche Aussagen hängen von der nachträglichen Korrelation unterschiedlicher Evidenzachsen ab?**

Der Schwerpunkt liegt damit auf:

- Korrelation Hülle ↔ moderne Stratigraphie;
- Kontextqualität der menschlichen, lithischen und faunistischen Funde;
- Verhältnis direkter archäologischer zu analytisch abgeleiteter Evidenz;
- Taphonomie und konkurrierende Nutzungsmodelle;
- Provenienzprobleme der Altgrabung;
- Grenzen populationsgenetischer und paläoklimatischer Aussagen am konkreten Fundplatz.

**Nicht mehr Ziel:** Besucher-Guide, Vor-Ort-Erklärung, Vermittlungserfolg oder ein `sichtbar/nicht sichtbar`-Schema.

## Learnings für Histo-Orla

### L1 – Research question before output format

Vor Artefakt-, View- oder Pilotdesign muss eine fachliche Forschungsfrage formuliert sein, die auch ohne den aktuellen Präsentationskontext sinnvoll bleibt.

Prüffrage:

> Würde diese Frage noch Sinn ergeben, wenn niemand gerade in Ranis stünde und nichts vermittelt werden müsste?

Wenn nein, ist sie wahrscheinlich eine View-/Nutzungsfrage, keine primäre Research Question.

### L2 – Context of use ≠ research goal

Ein Nutzer kann gerade vor Ort, im Archiv, im Museum oder beim Schreiben sein. Dieser Kontext darf die Form der Antwort beeinflussen, aber nicht automatisch den historischen Forschungsgegenstand umdefinieren.

### L3 – Research State before derived views

Persistenzreihenfolge:

```text
source / instance / findspot
→ excerpts / observations
→ claims / findings / hypotheses / unresolved
→ method / uncertainty / competing explanation
→ next discriminating research action
→ optional brief / map / guide / narrative
```

### L4 – Vertical slice requires epistemic work

Ein echter Slice muss mindestens einen belastbaren Erkenntnisschritt leisten: Provenienz auflösen, Korrelation prüfen, Konflikt diagnostizieren, konkurrierende Modelle unterscheiden oder neue diskriminierende Quelle bestimmen.

### L5 – Views dürfen Research Truth nicht besitzen

Visitor guide, Storyline, Karte, Museumstext oder 5-Minuten-Brief sind Projektionen. Sie lesen Research State; sie erzeugen nicht still neue historische Wahrheit.

### L6 – Goal correction must propagate to all controlling artifacts

Ein Learning-Kommentar reicht nicht. Wenn die Forschungsfrage falsch ist, müssen Work Owner, README, Slice-Definition, DoD und nächste Aktionen gemeinsam geändert werden. Sonst bleibt die alte Steuerung operativ wirksam.

### L7 – Owner correction is product evidence

Die Assistenz kann nicht nur Fakten halluzinieren; sie kann auch **Ziele halluzinieren bzw. substituieren**. Das ist ein eigenständiger Failure Mode.

> **goal substitution by conversational momentum**

Möglicher späterer Guard: Vor Eröffnung oder Reframing eines Research-Slices explizit `research question | user context | output/view | existing owner` unterscheiden. Noch kein Requirement.

## Bereits umgesetzte Korrekturen

- #85 umbenannt und inhaltlich auf Alt-/Neugrabung + Evidenzkorrelation umgestellt;
- `README.md` aktive Forschungsfrage und nächste Aktionen komplett neu gerahmt;
- `vertical-slices.md` VS1 vollständig ersetzt;
- Besucher-/Vermittlungsoutput aus dem DoD entfernt;
- `main` bleibt unverändert, kein PR/Merge.

## Falsifikationsfrage für den Pilot

Der korrigierte Pilot ist nur gerechtfertigt, wenn er zu einem überprüfbaren Research State führt, der mindestens eine der folgenden Leistungen erbringt:

- Alt-/Neugrabungs-Korrelation explizit und prüfbar macht;
- Provenienz-/Kontextunsicherheiten einzelner zentraler Funde sichtbar macht;
- konkurrierende Nutzungsmodelle der Höhle evidenzbasiert unterscheidet;
- neue diskriminierende Quellen oder offene Fundstellenprobleme identifiziert;
- ohne alten Chat fachlich fortsetzbar ist.

Wenn er nur eine bessere Erklärung von Bekanntem produziert, hat er sein Repo-Ziel verfehlt.
