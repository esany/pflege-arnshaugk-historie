# Ranis/Orlatal Pilot – Materialkorpus und Ordnung

**Status:** `pilot / working-research / branch-isolated / no-main-authority`  
**Work Owner:** #85  
**Branch:** `pilot/ranis-layered-archive-20260906`  
**Methodik:** #45, `docs/research/source-identity-protocol.md`  
**Stand:** 2026-09-06

## 5-Minuten-Handoff

### Worum geht es?

Dieser Branch sammelt und ordnet das **verfügbare Material zu Ranis und dem Orlatal**. Er ist weder ein Vermittlungsprojekt noch derzeit ein enges Forschungsfrage-Projekt.

Ausgangspunkt sind zwei Materialströme:

1. bereits erschlossene wissenschaftliche, offizielle und historische Quellen;
2. die am 2026-09-06 vor Ort gesammelten Fotos, Objektansichten, Ausstellungstexte, Karten und Baustellen-/Landschaftsbeobachtungen.

Der Korpus reicht bewusst vom **Zechsteinriff und der Landschaftsgeologie** über paläolithische Fundplätze wie **Ilsenhöhle, Gamsenberg, Lausnitz und Kniegrotte** bis zu mittelalterlichen/neuzeitlichen Befunden und der **aktuellen Torhausbaustelle auf Burg Ranis**. Er soll auch größere Orlatal-Zusammenhänge sichtbar machen, ohne daraus vorschnell eine Kontinuitätsgeschichte zu bauen.

## Sammlungsauftrag v0.3

> **Welche Materialien liegen tatsächlich vor, was dokumentieren sie, auf welche Orte/Zeiten/Objekte/Forschungsstände beziehen sie sich, wie ist ihre Provenienz und Zugriffstiefe, und wie lassen sie sich so ordnen und verknüpfen, dass spätere Forschung daraus belastbar starten kann?**

Das ist bewusst **kein einzelner inhaltlicher Claim**, sondern eine kuratorische Research-State-Aufgabe.

## Ordnungsachsen

Der Korpus wird parallel entlang mehrerer Achsen erschlossen:

| Achse | Frage |
|---|---|
| Quelle / Instanz | Was ist das konkrete Dokument, Foto, Objektlabel, Artikel, Datensatz oder Fundstück? |
| Raum | Ranis, Orlasenke, Gamsenberg, Lausnitz, Döbritz/Kniegrotte, Burg zum Stein usw.? |
| Zeit | Geologie, Paläolithikum, Mesolithikum, weitere Vorgeschichte, Mittelalter, Forschungsgeschichte, Gegenwart? |
| Materialtyp | Grabungsbefund, Artefakt, Schriftquelle, Karte, Foto, Museumstext, Bauforschung, naturwissenschaftliche Analyse? |
| Inspection / Provenienz | direkt inspiziert, user-provided, OCR-Derivat, nur Metadaten, unresolved? |
| Beziehungen | gleicher Ort, gleiche Sammlung, Vergleichsplatz, spätere Revision, gemeinsamer Landschaftskontext, möglicher Research Hook? |

Wichtig: **keine dieser Achsen allein wird zur Mastererzählung**.

## Was derzeit im Korpus steckt

### Geologie / Landschaft

- Zechsteinriff und Relief als physischer Rahmen;
- Orlasenke / Orlatal als wiederkehrender Raum vieler Fundstellen;
- Höhlen-/Felsräume und spätere Burgstandorte als räumliche Knoten.

### Paläolithikum / Mesolithikum

- Ilsenhöhle/Ranis: 2024er Publikationscluster, Alt-/Neugrabung, LRJ, Fauna, Klima, Genomik;
- Gamsenberg/Rehmen: mittelpaläolithischer Vergleichskontext;
- Lausnitz: Abri Theure, Nischen-/Lotharhöhle, Koleschhöhle;
- Döbritzer Schweiz: Kniegrotte, Urdhöhle, Wüste Scheuer;
- heutige Museumsfotos zu Fundobjekten und Kontexten sollen direkt mit Publikationen/Records verknüpft werden.

### Weitere Vorgeschichte / Orlatal

- Ausstellungskarte der Orlasenke;
- Steinbeile, Äxte, Keulen und weitere vorgeschichtliche Objekte;
- Preißnitzberg/Börner-Hooks und weitere Fundstellen, soweit Material vorhanden.

### Mittelalter / Burglandschaft

- Burg Ranis / Torhaus;
- Ludwigshof/Ruppitz;
- Burg „zum Steine“ bei Pößneck;
- Wallanlagen und Rechtsdenkmale aus der Ausstellung;
- aktuelle Torhaus-Bauforschung und Baustellendokumentation.

### Forschungsgeschichte / Überlieferung

- Wilhelm Börner;
- Hülle und andere Altgrabungen;
- alte Museumsdeutungen und Karten;
- moderne Revisionen durch Naturwissenschaft, Archäologie und Bauforschung.

## Kernartefakte des Branches

- `material-index.md` – **Master-Index** nach Raum, Zeit, Materialtyp und Beziehungen;
- `evidence-ledger.md` – Quelle/Instanz/Inspection/Provenienz;
- `field-materials.md` – heutige Ausstellungs-/Feldsammlung;
- `vertical-slices.md` – nur noch abgeleitete Research Hooks; **kein aktiver Pflicht-Slice**;
- `system-learning.md` – Product-/Workflow-Learnings;
- `self-audit-20260906.md` – dokumentierte Fehlsteuerungen und Korrekturen.

## Arbeitsprinzip

```text
Material kommt hinein
→ konkrete Instanz identifizieren
→ Raum/Zeit/Typ/Provenienz zuordnen
→ mit vorhandenen Quellen/Objekten/Fundstellen verknüpfen
→ offene Auflösungsaufgaben markieren
→ erst danach Research Hooks / Hypothesen / Synthesen bilden
```

Nicht:

```text
vorher gewählte Geschichte oder Forschungsfrage
→ Material passend einsortieren
```

## Aktuelle Intake-Priorität

1. heutige Fotos und Materialien vollständig erfassen;
2. Kniegrotte-Funde und zugehörige Beschriftungen/Publikationen verbinden;
3. Zechsteinriff-/Landschaftsmaterial als eigenen Kontextcluster erfassen;
4. Orlatal-Gesamtkarten und regionale Fundverteilung einordnen;
5. Burg Ranis / Torhaus: Ausstellung, Bauforschung und aktuelle Baustelle als Gegenwarts-/Baugeschichtscluster zusammenführen;
6. danach prüfen, welche echten Forschungsfragen aus dem geordneten Korpus hervortreten.

## Schutzregeln

- Sammlung und Identifikation vor Synthese;
- Museumsbeschriftung ≠ aktueller Forschungsstand;
- user-provided Foto ≠ Objektkatalog;
- wissenschaftlicher Artikel ≠ automatisch inspizierte Supplement-Abbildung;
- OCR/HTR ≠ diplomatisch geprüfter Urtext;
- räumliche Wiederkehr im Orlatal ≠ Bevölkerungs-/Kultur-/Erinnerungskontinuität;
- fehlende Provenienz wird nicht durch plausible Interpretation ersetzt.

## Pilotgrenze

Der Branch bleibt ein isolierter Versuch, Materialordnung und Restartability zu testen. `main` bleibt unverändert; kein PR/Merge, bevor sich zeigt, dass diese Form gegenüber bloßer Chat-Sammlung einen echten Research-State-Mehrwert liefert.
