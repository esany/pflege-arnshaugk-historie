# U2 / Sachenbacher 2022 – Landesausbaumodell, Orlagau-Raumbegriffe und Orts-/Chronologiematrix

**Status:** `working-research / model-check / secondary-publication-integration / bounded-systematic-pass`  
**Work Owner:** #46  
**Methodik:** #45, `docs/research/source-identity-protocol.md`, #60  
**Stand:** 2026-09-03  
**Branch:** `research/sachenbacher-clean-room-20260903`  
**Current focus:** Dieses Artefakt ist die maßgebliche Sachenbacher-Leseführung im PR #76. Der frühere Ranis-Slice ist als überholter erster Testlauf archiviert.

---

## 1. Zweck und Schwerpunktkorrektur

Dieses Artefakt beantwortet die Owner-Korrektur vom 2026-09-03:

> Ranis ist nur ein Einzelbeispiel. Sachenbacher soll systematisch über sein Landesausbaumodell, seine Orlagau-Raumbegriffe und sein Orts-/Chronologiematerial prüfbar gemacht werden.

Die zentrale Prüflogik lautet daher:

```text
Modell
→ erwartbares historisches Muster
→ konkrete Orte / Evidenz
→ Passung | Widerspruch | Lücke
→ konkurrierende Erklärung
```

Einzelorte wie Ranis, Weltwitz, Zwackau oder Herschdorf werden nur dort vertieft, wo sie eine tragende Modellannahme tatsächlich diskriminieren.

Dieses Dokument ist kein Endbefund zur Geschichte des Orlagaues. Es ist ein `working-research`-Artefakt, das Sachenbachers interdisziplinäre Synthese in eine überprüfbare Histo-Orla-Arbeitsform überführt.

---

## 2. Gelesener kanonischer Arbeitsrahmen

Vor dieser Schwerpunktkorrektur wurden frisch aus GitHub gelesen:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `README.md`
- Issue #46 inklusive Kommentare
- Issue #60 inklusive Kommentare
- Issue #45
- `docs/research/source-identity-protocol.md`
- `docs/research/cases/u2-knau-orlagau-quellenbefunde.md`
- `docs/research/cases/u2-orlagau-begriffskritik.md`
- `docs/research/cases/orlagau-source-ledger.md`
- `docs/research/cases/u2-orlagau-suchraum-quellenexzerpte.md`
- PR #76, weil die Sachenbacher-Integration derzeit auf diesem Branch liegt

Arbeitskonsequenzen aus dem Bootstrap:

1. Historische Findings bleiben unter #46.
2. Methodenlernen bleibt unter #60 und darf nicht als fertiges Domain Method Profile ausgegeben werden.
3. Sachenbacher ist Sekundärquelle, Forschungsstandsquelle, Modellquelle und Quellen-/Literaturrouter, aber keine Wahrheitsautorität.
4. Raumbegriffe bleiben quellen-, überlieferungs- und forschungsgeschichtlich zu unterscheiden.
5. `Ersterwähnung`, `Siedlungsbeginn`, `archäologische Präsenz`, `Ortsname`, `Herrschaft`, `Kirche` und `Wüstung` bleiben getrennte Evidenzachsen.

---

## 3. Benutzte Instanzen, Fundstellen und Grenzen

### 3.1 Sachenbacher-Instanz

Bibliographischer Arbeitsgegenstand:

> Peter Sachenbacher, *Thüringen östlich der Saale im Mittelalter. Archäologisch, mediävistisch, onomastisch, ethnografisch und philosophisch vergleichende Studie zum früh- und hochmittelalterlichen Landesausbau in Territorien der Germania Slavica Thuringiae*, Darmstadt: wbg Academic, 2022.

Arbeits-/Kontrollinstanz:

- OATbyCO/DDE-HTML-Repräsentation: `https://exist.ulb.tu-darmstadt.de/2/v/pa000017-0007`
- Verlags-/Katalogkontrolle: Herder/wbg-Seite zu Autor, Titel, Ausgabe, Jahr, Umfang, ISBN, Open-Access-Hinweis.

**Zitierregel:** Zitierfähig ist die veröffentlichte Publikation. Die DDE/OATbyCO-Instanz dient in diesem Durchlauf zur Volltextnavigation, Druckseitenmarker-/Fußnotenziffer-Kontrolle und zur Erzeugung von Prüfaufträgen.

### 3.2 Kontrollierte Sachenbacher-Schwerpunkte

Kontrolliert wurden insbesondere:

- theoretisch-methodologische Grundlagen, Druckseitenbereich um S. 15 und um S. 40 ff.;
- slawische Besiedlung / Orlagau, Druckseitenbereich ca. S. 148–163;
- III.3 `Der hochmittelalterliche Landesausbau unter deutscher Herrschaft im Orlagau`, Druckseitenbereich ca. S. 262–314;
- IV-Zusammenfassung zum Orlagau, Druckseitenbereich ca. S. 321–322;
- Fußnotenziffern in den relevanten Passagen: u. a. 205–217, 222–223, 238–252, 253–267, 269–302, 307.

**Grenze:** Die DDE-HTML-Fassung liefert nicht in allen Bereichen eine komfortable Fußnotenauflösung und nicht alle Seitenumbrüche sind für externe Zitation ohne Druck-/PDF-Bildkontrolle sicher genug. Deshalb bleiben einige Angaben als `print-page range / footnote-number checked, source behind footnote not yet collated`.

### 3.3 Externe Methodenkontrolle in diesem Pass

Proportional gegen fachlichen SOTA kontrolliert, aber nicht vollständig als Domain Method Profile validiert:

- Frühgeschichtliche Archäologie / Ethnizität: Brather 2004 und spätere Slawenarchäologie stützen die Vorsicht, archäologische Kulturen/Sachgüter nicht direkt als ethnische Gruppen zu lesen.
- Historische Raum-/Gau-Begriffe: aktuelle begriffsgeschichtliche Forschung zu `Gau/pagus` stützt die Histo-Regel, `pagus`, `comitatus`, moderne `Gau`-Namen und rekonstruierte Raumgrenzen nicht zu verschmelzen.
- Kirchengeschichte / Pfarrorganisation: Sachenbacher routet auf Bünz 2007 und Rainer Müller; diese sind identifiziert, aber noch direkt zu kollationieren.
- Onomastik: Sachenbacher routet stark auf Rosenkranz, Eichler, Ulbricht, Walther; die einzelnen Ortsnamendeutungen sind noch nicht hinreichend direkt kontrolliert.

Status: `extern fachlich gestützt / method hypothesis / not fully Histo-validated`.

---

## 4. Sachenbachers Landesausbaumodell für den Orlaraum

### 4.1 Modellkern

Sachenbacher beschreibt den Orlagau nicht als lineare Abfolge:

```text
slawische Wildnis → deutsche Eroberung → deutsche Siedlung
```

Sondern als überlagerte, räumlich ungleichzeitige Entwicklung:

```text
frühmittelalterliche slawisch-fränkisch/karolingische Kontakt- und Herrschaftszone
→ Saalfeld als frühes Herrschafts-, Wirtschafts- und Kirchenzentrum
→ 10./11. Jh. ottonisch-salische, ezzonisch-richezanische, kölnische und mainzische Einbindung
→ 1071/1074 verdichtete Kirchen-, Besitz- und Grenzüberlieferung
→ 12. Jh. kölnisches Dienstrecht, staufische Rückbindung, Burgen, Kirchen, Orte und lokale Herrschaftsträger
→ 13./14. Jh. Erreichen des heutigen Siedlungsstandes, weitere Ausdehnung in Randräume, territoriale Fragmentierung und Wüstungsprozesse
```

Sachenbacher setzt dafür drei Hauptabschnitte an:

1. Saalfeld und der Orlagau vor und nach der Erstnennung als Teil eines slawisch-fränkisch/karolingischen Raumes.
2. Saalfeld und der Orlagau im 10./11. Jahrhundert in ottonischer und salischer Zeit.
3. Saalfeld und der Orlagau im 12. Jahrhundert in staufischer Zeit.

Methodisch wichtig: Er sagt ausdrücklich, dass `Orlagau` in dieser Drei-Phasen-Gliederung auch für Zeiten benutzt wird, in denen diese Bezeichnung selbst noch nicht verwendet wurde. Damit ist `Orlagau` im Modell zunächst ein moderner Arbeits-/Rekonstruktionsbegriff, nicht automatisch Quellenwort.

### 4.2 Trennung von Beobachtung, Forschung und Interpretation

| Modellbaustein | Sachenbacher-Fundstelle | Beobachtung / quellennahe Ebene | Übernommene Forschung / Router | Sachenbachers Interpretation | Status für Histo-Orla |
|---|---:|---|---|---|---|
| Begriff `Landesausbau` statt `Kolonisation` | DDE S. ca. 15, S. ca. 40 ff. | Begriffswahl und Forschungsgeschichte | Germania-Slavica-Debatte, Gringmuth-Dallmer, Thieme u. a. | `Landesausbau` erlaubt, slawische Beteiligung unter deutscher Herrschaft sichtbar zu machen | `extern fachlich gestützt`; kein einzelner Quellenbefund |
| Archäologische Ethnizitätsvorsicht | S. ca. 40 ff., insb. theoretischer Teil | Sachenbacher markiert `slawische Keramik` als fachliche Abkürzung, nicht als Ethnos der Keramik | aktuelle archäologische Methodenkritik; Brather als externer Kontrollanker | Herstellung/Gebrauch können funktional/ökonomisch statt ethnisch differenziert sein | `histo-kompatible Schutzregel`; fachmethodisch unter #60 weiter zu profilieren |
| Unterschied links/rechts der Saale | S. ca. 158–163, 310 ff. | Orlagau liegt in Kontaktzone zweier Entwicklungen | Wandsleb, Rempel, Auerbach, Fischer/Elbracht, neue Grabungen | Links der Saale eher lockere Kontinuität mit slawischer Zuwanderung; rechts der Saale nach germanischer Entsiedlung slawische Landnahme und bald fränkische/deutsche Einbindung | `method hypothesis / source-bound`; braucht archäologische Search/Preservation Boundaries |
| Saalfeld als Zentrum | S. ca. 262–267, 321–322 | 899 `curtis Salauelda`, 1013 `provincia Salaveld`, 1056/1071 Richeza/Köln/Kloster | Gockel, Königspfalzenforschung, Richeza-/Köln-Überlieferung | Saalfeld sei von Beginn Mittelpunkt und Ausgangspunkt des Landesausbaus | `plausible strong working model`, aber jeder Rechts-/Raumclaim braucht Urkundenprüfung |
| Grenzbeschreibung um 1071 | S. ca. 262, 267, 321–322 | nur in 15.-Jh.-Kopie; wahrscheinlich gefälschte Coburger Copialbuch-Urkunde; Landschafts-/Grenzpunkte | Gerhard Werner / Gockel / ältere Grenzrekonstruktion | Trotz Fälschungsstatus entspreche die Beschreibung den zeitgenössischen Verhältnissen | `high-value but high-risk`; nicht als Polygon-Grenze verwenden |
| Kirchenorganisation 10./11. Jh. | S. ca. 286–292 | 968 Zeitz-Einordnung; 1071 Krölpa, Neunhofen, Langenschade; Sedessprengel Pößneck/Remda | Bünz, Hannappel, Eberhard, Gockel, Müller | Mission und Pfarrorganisation seien im 11. Jh. bereits fortgeschritten | `extern fachlich gestützt`; 1071-Urkunde und Kirchenprofile offen |
| 12./13. Jh. Kirchen-/Burgennetz | S. ca. 282–298 | Burgen, lokale Herrschaft, romanische Dorfkirchen, Ortsneugründungen | Queck, Spazier, R. Müller, Wysburg-Dissertation, Dehio | Landesausbau unter deutscher Herrschaft erzeugt lokale Burg-/Kirchen-/Ortsnetze | `good model test set`; Einzeldatierungen häufig relativ |