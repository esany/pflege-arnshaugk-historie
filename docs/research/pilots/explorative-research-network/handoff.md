# Handoff – unabhängiger Review oder Umsetzung durch neuen Chat

## Status

Dieses Dokument ist der explizite Einstieg für einen **neuen, unabhängigen Chat/Bearbeiter**, der den bisherigen Gesprächsverlauf nicht kennen soll.

Pilot: #86  
Branch: `pilot/explorative-research-network-20260907`

## 1. Pflicht-Bootstrap

Lies **frisch vom Repository**, nicht aus Erinnerung oder Zusammenfassungen:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. Root `README.md`
4. `docs/research/README.md`
5. `docs/research/source-identity-protocol.md`
6. `docs/research/methods/README.md`
7. Issue #86
8. diesen Pilotordner vollständig

Danach je Auftrag:

- Review: #87
- Prototype/Umsetzung: #88, aber **erst nach abgeschlossenem Review #87**
- Evaluation: #89, nach ggf. vorhandenem Prototyp

Für generische Aussagen zusätzlich frischen Stand von `esany/Wissensarbeit` lesen, mindestens:

- `README.md`
- `project/GOVERNING_OBJECTIVE.md`
- `project/CURRENT_STATE.md`
- `project/requirements.json`
- `system/lifecycle.json`
- `system/authority.json`
- `system/competence.json`
- `system/material_state.json`
- `system/building_blocks.json`
- `pilots/generic-pilot-learnings/pilot-closure.md`

## 2. Auftrag für Review-Chat (#87)

Arbeite als unabhängiger Reviewer. **Nicht implementieren.**

Prüfe das Pilotmodell gegen den tatsächlichen aktuellen Repo-Stand.

Für jedes wesentliche Element gib genau eine Candidate-Disposition:

`reuse-existing | adapt-case-specific | requirement-candidate | generic-learning-candidate | reject | defer`

Mindestens prüfen:

- shared research state;
- Research Question als Linse statt Container;
- Question Operations `split/fuse/reframe/supersede/defer`;
- Relationschichten;
- Views als abgeleitete Projektionen;
- modulbezogenes Kompetenzrouting;
- rekursive Analyse↔Synthese- und Überblick↔Detail-Bewegungen;
- Scale Shift;
- Umgang mit materialgetriebenem Eingang ohne vorab bekannte Forschungsfrage.

Dokumentiere konkret, wo Histo-Orla dies bereits kann. Eine neue Struktur ist kein Erfolg, wenn vorhandene Mechanismen reichen.

## 3. Auftrag für Implementierungs-Chat (#88)

Nur starten, wenn #87 die Fortsetzung empfiehlt oder #86 dies ausdrücklich freigibt.

Baue die **kleinste hinreichende, reversible** Demonstration. Kein neues Backend/Framework aus Eigeninteresse.

Der Prototyp soll zeigen:

1. eine stabile Source-/Materialidentität wird von mindestens zwei Research Modules referenziert;
2. mindestens eine Frageoperation ist nachvollziehbar;
3. mindestens ein Scale Shift ist explizit;
4. mindestens zwei Module routen unterschiedliche führende Kompetenzen;
5. zwei Views nutzen denselben Research State ohne Truth-Duplikat;
6. ein rekursiver Pfad `Detail → Synthese → neue Detailfrage` bleibt tracebar;
7. unresolved/uncertain states werden nicht wegmodelliert.

Bei jeder neuen Struktur angeben:

`existing mechanism reused | case adaptation | temporary pilot construct`.

## 4. Auftrag für Evaluations-Chats (#89)

Mindestens zwei **unabhängige** Chats erhalten denselben GitHub-Startpunkt.

### Chat A – Detail

Wähle aus dem gemeinsamen Bestand eine enge, materialgestützte Frage. Arbeite quellenkritisch und dokumentiere neue Findings/Questions/Unresolved States.

### Chat B – Überblick/Synthese

Wähle aus demselben Bestand eine übergreifende oder Scale-Shift-Frage. Nutze nur persistierten Research State; keine Annahmen aus einem früheren Chat.

Danach vergleichen:

- wurden Source-/Instance-Identitäten konsistent verwendet?
- entstand Duplikatwahrheit?
- blieben epistemische Ebenen getrennt?
- konnten unterschiedliche Fragen denselben Bestand sinnvoll rekombinieren?
- blieben widersprüchliche/unsichere Befunde sichtbar?
- war ein alter Chat für die Arbeit nötig?

## 5. Verbotene Abkürzungen

Ein neuer Chat darf **nicht**:

- Vermittlung oder Besuchererlebnis zum Ziel erklären;
- eine einzelne Ranis-/Ilsenhöhle-Frage zum Masterziel machen;
- annehmen, dass alles Material bereits vollständig erfasst ist;
- Nutzerfoto = materielles Objekt setzen;
- Museumslabel = aktueller wissenschaftlicher Konsens setzen;
- OCR/unsichere Lesung glätten;
- räumliche Nähe = historische Beziehung setzen;
- Synthese/View als neuen Source of Truth behandeln;
- Expertise durch Rollenprompt simulieren;
- eine Graphdatenbank/Ontologie/Agentenarchitektur als Voraussetzung annehmen;
- Pilot-Candidates still in accepted Requirements/Method Truth überführen.

## 6. Erwarteter Review-Stil

Arbeite adversarial und evidenznah:

- Was ist Beobachtung?
- Was ist bereits im Repo akzeptiert?
- Was ist nur Pilot-Hypothese?
- Was ist redundant?
- Wo geht Information verloren?
- Wo erzeugt Struktur selbst falsche Semantik?
- Welche Fachkompetenz müsste den jeweiligen Claim prüfen?
- Was wäre die einfachste Alternative?

## 7. Erfolgsbedingung des Handoffs

Dieser Pilot ist erst dann wirklich restartbar, wenn ein neuer Chat nach obigem Bootstrap **ohne diese ursprüngliche Konversation** Ziel, Risiken, offene Entscheidungen und nächste erlaubte Aktionen korrekt rekonstruieren kann.

Wenn das nicht gelingt, ist das ein Pilotbefund und muss in #86/#89 dokumentiert werden – nicht durch zusätzliche geheime Chatkontexte kompensiert werden.
