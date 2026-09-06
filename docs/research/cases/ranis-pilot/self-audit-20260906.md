# Self-Audit 2026-09-06 – Ranis-Pilot

**Status:** `owner-feedback-response / self-audit / corrective-learning`  
**Work Owner:** #85  
**Branch:** `pilot/ranis-layered-archive-20260906`

## Anlass

Owner-Feedback: Der angelegte Ranis-Pilot könnte das im Chat entstandene, eher didaktisch/vermittelnde Nebenprojekt über das bestehende Histo-Orla-Repository stülpen, statt das Repository als Forschungsassistenz zu nutzen.

## Ergebnis der Selbstprüfung

**Ja, diese Gefahr habe ich selbst erzeugt.**

Der Branch ist technisch isoliert und hat `main` nicht verändert. Inhaltlich habe ich aber den Pilot zu stark um die Frage gerahmt, was ein „wissenschaftlich interessierter Besucher“ an der Ilsenhöhle wissen oder vor Ort erschließen kann. Damit wurde ein Vermittlungs-/Besucherziel zur primären Forschungsfrage gemacht, obwohl das bestehende Repository ein anderes Primärziel hat: eine private transdisziplinäre historische Forschungsassistenz für Quellenarbeit, Methodik, transdisziplinäre Analyse und restartbaren Research State.

Das ist kein bloßes Wording-Problem. Es verändert, welche Informationen priorisiert, wie Success definiert und welche Outputs als zentral behandelt werden.

## Konkrete Fehlleistungen

### 1. Fremdes Ziel über vorhandenes Ziel gelegt

Ich habe aus dem Chat-Kontext ein anschauliches Vor-Ort-/Vermittlungsziel abgeleitet und dieses zum aktiven Vertical Slice gemacht.

Dadurch entstand implizit:

```text
Vermittlungsfrage
→ Research-Artefakte
→ System-Learning
```

statt repository-konform:

```text
reale Forschungsfrage / Research Pain
→ Quellen-/Methodenarbeit
→ belastbarer restartbarer Research State
→ daraus optional eine Vermittlungs-/Darstellungssicht
```

Die Vermittlung darf eine **abgeleitete View** sein, nicht der Default-Owner des Research State.

### 2. #64 zu schematisch angewandt

Aus dem Audit-Befund „kleiner Vertical Slice statt Mega-Pilot“ habe ich zu schnell gefolgert, dass unser Chat-Thema selbst der richtige Pilotgegenstand sei.

#64 fordert einen engen realen Slice mit Nutzeroutput. Es sagt nicht, dass jeder lebendige Chatstrang automatisch ein neuer Research-Pilot werden soll. Vor dem Slice hätte ich zuerst prüfen müssen:

- Welcher bestehende Goal/Need/Pain des Repositories wird hier getestet?
- Ist das Ranis-Thema Forschungsgegenstand, Testfixture oder nur ein Nebenprodukt des Chats?
- Welcher konkrete Assistenz-Workflow des vorhandenen Systems soll dadurch belastet werden?

Diese Prüfung habe ich nicht sauber genug gemacht.

### 3. Vorhandenen Research State zu wenig als Primärstruktur genutzt

Das Repository besitzt bereits Source-Identity-, Finding-/Claim-, Method-, Work-Context- und Restartability-Verträge. Ich habe diese zwar referenziert, aber darüber eine neue `ranis-pilot/`-Narrativstruktur mit `5-Minuten-Handoff`, `Vertical Slices`, `field-materials` usw. gebaut.

Das kann sinnvoll sein, **wenn** es aus einem realen Research Need folgt. Hier bestand jedoch die Gefahr, dass ich eine neue lokale Mikro-Governance schaffe, die lediglich unseren Chat konserviert.

### 4. „Owner-lesbar“ mit „Vermittlung“ verwechselt

Ein owner-lesbarer Research Brief bedeutet: Forschungsstand, Evidenz, Unresolved, nächste diskriminierende Aktion schnell erfassbar.

Ich habe daraus teilweise „vor Ort sichtbar / für Besucher erschließbar“ gemacht. Das ist ein anderes Produktziel.

### 5. Zu viel Chat-Wissen vorsortiert statt zuerst Roh-Provenienz zu sichern

Ein Teil der im Branch formulierten Ranis-Synthese stammt aus unserem Dialog und bereits vorheriger Recherche. Selbst wenn die Aussagen fachlich plausibel oder korrekt sind, hätte der erste Sicherungsschritt stärker lauten müssen:

```text
welche konkreten Aussagen wollen wir bewahren?
→ woher stammen sie genau?
→ welche wurden direkt inspiziert?
→ welche sind Chat-Synthese/Hypothese?
→ was fehlt zur Promotion?
```

Erst danach sollte eine thematische Narration entstehen.

## Korrekturprinzip

Der Branch bleibt vorerst **isoliertes Experiment**, aber seine Rolle wird enger interpretiert:

> Nicht „Ranis-Vermittlungsprojekt im Histo-Orla-Repo“, sondern Test, ob ein längerer, heterogener Chat-Research-Strang sauber in den bestehenden kanonischen Research State überführt werden kann, ohne Provenienz, Unsicherheit und Restartability zu verlieren.

Der Forschungsgegenstand Ranis ist dabei **Testmaterial / realer Forschungsfall**. Eine spätere Vor-Ort- oder Vermittlungsausgabe ist höchstens eine abgeleitete View.

## Learnings für Histo-Orla

### L1 – Vor jedem neuen Pilot zuerst Goal/Need/Pain routen

Kein neuer Branch/Issue allein deshalb, weil ein Chat thematisch reich geworden ist.

Vorher explizit beantworten:

```text
existing goal / need / pain?
existing work owner?
real research task?
why is a new branch needed?
what would be lost if we only persist into existing canonical state?
```

### L2 – Research State vor Darstellung

Persistenzreihenfolge bei Chat-Übergabe:

```text
source / instance / inspection status
→ excerpts / observations
→ findings / hypotheses / unresolved
→ next research action
→ erst danach synthesis / brief / map / visitor view
```

### L3 – Abgeleitete Views dürfen kanonische Wahrheit nicht besitzen

`visitor guide`, `5-minute brief`, Karte, Storyline oder Ausstellungstext sind Views. Sie dürfen Findings lesen, aber keine eigene Research Truth etablieren.

### L4 – Ein Vertical Slice braucht einen Systembezug, nicht nur eine kleine Fachfrage

Ein guter Pilot prüft eine konkrete Assistenzfähigkeit, z. B.:

- heterogenen Chat-State in Source/Instance/Excerpt/Finding zerlegen;
- alte und neue Forschung mit unterschiedlicher Evidenztiefe sauber zusammenführen;
- user-provided field material provenance-sicher integrieren;
- widersprüchliche Altdeutungen und moderne Revision getrennt halten;
- fresh-context restart ohne alten Chat schaffen.

Die Fachfrage ist Testinhalt; die Assistenzfähigkeit ist der eigentliche Pilotzweck.

### L5 – Kein neues lokales Schema, wenn bestehende Verträge reichen

Neue Dateien/Strukturen nur dann, wenn ein realer Informationsverlust oder Bedienpain anders nicht sauber gelöst wird. Sonst bestehende kanonische Strukturen nutzen.

### L6 – Owner-Korrektur ist Product Evidence

Dieses Feedback zeigt eine reale Fehlsteuerung durch die Assistenz: Sie kann ein attraktives Nebenprodukt zum Hauptziel machen, obwohl das Repository bereits ein anderes Ziel und Governance besitzt.

Das ist ein wichtiger Produkt-/Workflow-Failure-Mode:

> **goal substitution by conversational momentum**

Mögliche spätere Guard-Idee: Vor Eröffnung eines neuen Pilot-/Work-Owner-Artefakts muss der aktuelle Goal/Need/Pain und die Beziehung zu bestehenden Work Ownern explizit aufgelöst werden. Noch kein Requirement.

## Sofortige Disposition

- `main`: unverändert lassen.
- Branch: nicht mergen und keinen PR öffnen.
- #85: als experimentellen Chat-to-Research-State-Test behandeln, nicht als neues Ranis-Programm.
- bestehende Ranis-Artefakte im Branch als **candidate / test fixture** betrachten.
- vor weiterer inhaltlicher Ausarbeitung zuerst prüfen, welche Inhalte in bestehende kanonische Orlagau-/Regional-Research-Artefakte gehören und welche nur branchlokale Testdaten bleiben.
- Vermittlungs-/Besucheroutput nicht weiter als primäres DoD verfolgen.

## Falsifikationsfrage

Der korrigierte Pilot ist nur dann gerechtfertigt, wenn er nachweisbar etwas testet oder bewahrt, das durch bloßes Weiterchatten oder direktes Anhängen an bestehende #46-Artefakte nicht gleich gut und einfacher erreichbar wäre.

Wenn diese Bedingung nicht erfüllt wird, sollte der Branch verworfen bzw. nur als Lernprovenienz archiviert werden.
