# U2 / Sachenbacher 2022 – Clean-Room-Integration und erster Research Slice

**Status:** `working-research / secondary-publication-integration / first-slice-executed-with-boundaries`  
**Work Owner:** #46  
**Methodik:** #45, `docs/research/source-identity-protocol.md`, #60  
**Stand:** 2026-09-03  
**Branch:** `research/sachenbacher-clean-room-20260903`

---

## 1. Gelesener Bootstrap und Arbeitsrahmen

Frisch aus GitHub gelesen wurden vor dieser Bearbeitung:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `README.md`
- Issue #46 inklusive Kommentare
- Issue #60 inklusive Kommentare
- Issue #45 inklusive Kommentare
- `docs/research/source-identity-protocol.md`
- `docs/research/cases/u2-knau-orlagau-quellenbefunde.md`
- `docs/research/cases/orlagau-source-ledger.md`
- `docs/research/cases/u2-orlagau-suchraum-quellenexzerpte.md`
- `docs/research/cases/orla-saale-region-longue-duree-research-framework.md`
- `docs/research/methods/README.md`
- `docs/research/methods/domain-method-profile-contract.md`

Arbeitskonsequenz: Der bestehende #46-Research-State wird nicht als historische Wahrheit behandelt. Sachenbacher wird nicht als Autorität für Wahrheit, sondern als Sekundärquelle, Forschungsstandsquelle, Modell-/Hypothesenquelle, Literaturrouter, Primärquellenrouter und Suchinventar-Erweiterung verarbeitet.

---

## 2. Quellen-/Instanzhinweis zu Sachenbacher

Bibliographischer Arbeitsgegenstand:

> Peter Sachenbacher, *Thüringen östlich der Saale im Mittelalter. Archäologisch, mediävistisch, onomastisch, ethnografisch und philosophisch vergleichende Studie zum früh- und hochmittelalterlichen Landesausbau in Territorien der Germania Slavica Thuringiae*, Darmstadt: wbg Academic, 2022.

Die vom Nutzer bereitgestellte Datei gilt nur als Arbeitsrepräsentation. Zitierfähig ist die veröffentlichte Publikation. Zusätzlich wurde die öffentlich erreichbare OATbyCO/DDE-HTML-Repräsentation `https://exist.ulb.tu-darmstadt.de/2/v/pa000017-0007` als Kontrollinstanz genutzt. Sie enthält Druckseitenmarker und Fußnotenziffern, aber nicht in allen Passagen eine bequem isolierbare Fußnotenauflösung. Der Herder/wbg-Katalog bestätigt das Werk als 1. Auflage 2022, 378 Seiten, ISBN 978-3-534-40649-4, und als Open-Access-Publikation.

**Arbeitsgrenze:** Die nachfolgende Integration benutzt Sachenbachers Druckseiten und Fußnotenziffern aus der Kontrollinstanz. Die zugrunde liegenden Primärquellen, Editionen und Spezialstudien wurden in diesem Durchlauf nur teilweise über Katalog-/Suchnachweise identifiziert, aber nicht vollständig direkt kollationiert. Wo dies fehlt, steht der Status ausdrücklich auf `unresolved` oder `method hypothesis / not yet independently validated`.

---

## 3. Bauart des Werkes für Histo-Orla

### 3.1 Gesamtfrage und zentrales Modell

Sachenbacher untersucht den früh- und hochmittelalterlichen Landesausbau in der *Germania Slavica Thuringiae*. Sein eigener Zuschnitt gilt besonders drei Räumen: Altenburger Land/Pleißenland, Gebiet um Gera mit nördlichem Vogtland und Orlagau. Der Fokus reicht vom Auftreten slawischer Besiedlung im 8. Jahrhundert bis in das 12./13. Jahrhundert und zur Assimilation beziehungsweise Integration slawischer Gruppen im hochmittelalterlichen Herrschafts- und Siedlungsprozess.

Zentral ist ein Begriffswandel: Sachenbacher bevorzugt `Landesausbau` gegenüber `Kolonisation`, `deutsche Ostkolonisation`, `ostdeutsche Kolonisation` oder `Deutsche Ostsiedlung`, weil er den Anteil slawischer Bevölkerung vor und unter deutscher Herrschaft herausarbeiten will. Er formuliert methodisch ausdrücklich, dass ethnische Zuschreibungen archäologischer Sachkultur problematisch sind: Nicht die Keramik ist ethnisch, sondern höchstens die Menschen, die sie herstellen, gebrauchen oder tradieren; die Kurzform `slawische Keramik` bleibt eine fachliche Abkürzung, darf aber nicht zur unmittelbaren Ethnizitätsbehauptung werden.

**Status für Histo:** `extern fachlich gestützt`, aber nicht automatisch Histo-methodisch validiert. Die methodische Richtung passt stark zu #46/#60, muss aber pro Befund evidenzlogisch durchgeführt werden.

### 3.2 Zeitliche und räumliche Ordnung

Das Werk arbeitet großräumig vergleichend und zugleich regional differenziert. Für Histo-Orla relevant ist vor allem Kapitel III.3 zum hochmittelalterlichen Landesausbau unter deutscher Herrschaft im Orlagau sowie die zusammenfassende Modellierung auf Druckseiten 350–352.

Sachenbacher ordnet Saalfeld und den Orlagau in drei grobe Abschnitte:

1. Saalfeld und Orlagau vor und nach der Erstnennung als Teil eines slawisch-fränkisch/karolingischen Raumes;
2. Saalfeld und Orlagau im 10./11. Jahrhundert in ottonischer und salischer Zeit;
3. Saalfeld und Orlagau im 12. Jahrhundert in staufischer Zeit.

Wichtig für Histo-Orla: Sachenbacher verwendet `Orlagau` teilweise auch als rückblickende Gebietsbezeichnung für Zeiten, in denen der Begriff selbst noch nicht zwingend quellenförmig benutzt wurde. Das bestätigt die bereits in #60 dokumentierte Begriffsvorsicht: `Orlagau` muss je Fundstelle als Quellenbegriff, historiographische Rekonstruktion oder heutiges Research-Shorthand markiert werden.

### 3.3 Disziplinäre Bauart

Sachenbachers Argumentation ist nicht monodisziplinär. Tragende Argumentteile kommen aus:

- Archäologie: Siedlungsbefunde, Burgen, Wallanlagen, Keramik, Kirchenarchäologie, ältere Grabungen und moderne Ausgrabungen;
- Mediävistik/Diplomatik/Landesgeschichte: Urkunden, Besitz- und Herrschaftszusammenhänge, Köln/Saalfeld, Mainz/Zeitz, Saalfelder Kloster, lokale Herrschaftsträger;
- Onomastik: Ortsnamen mit slawischem, deutschem oder gemischtem Deutungspotential;
- Bau- und Kunstgeschichte: Kirchenbauten, romanische/gotische Bauphasen, opus spicatum, Patrozinien- und Pfarrstrukturen;
- Forschungsgeschichte: Entwicklung der Begriffe Germania Slavica, Kolonisation, Slawenforschung, ältere national-/kolonisationsgeschichtliche Modelle.

Für Histo-Orla ist diese Bauart wertvoll, aber riskant: In der Synthese können archäologische Präsenz, Ortsnamen, politische Herrschaft, kirchliche Organisation und Siedlungskontinuität leicht zu einer eleganten, aber evidenzlogisch vermischten Erzählung verschmelzen. Genau dagegen arbeitet der vorliegende Slice.

### 3.4 Relevanz für Orla / Arnshaugk / Knau

Direkt relevant:

- Saalfeld als karolingisch-ottonisch-salisch-staufisches Zentrum westlich der Saale;
- der Orlagau als deutsch-slawische Kontakt- und Ausbauzone;
- Ranis als Burg-/Ministerialitäts- und möglicher Verwaltungspunkt im Orlaraum;
- Weltwitz als Wallanlage und onomastisch-archäologischer Fall im Orlagau;
- Kirchenorganisation mit Krölpa, Neunhofen, Langenschade, Graba, Arnshaugk und Sedessprengel Pößneck/Remda;
- Arnshaugk/Lobdeburg als östlicher Orlagau-Herrschaftskomplex im 12./13. Jahrhundert.

Nicht direkt belegt in diesem Durchlauf:

- `Knau` bei Neustadt/Orla kommt in der kontrollierten DDE-Volltextsuche nicht als relevanter Orla-Knau-Befund vor. Der Treffer `Knau, Ot. von Zetscha` gehört zum Altenburger Kontext und darf nicht mit Knau bei Neustadt/Orla verschmolzen werden.
- `Dreba` und `Plothen` ergaben in der DDE-Volltextsuche keinen Treffer.

**Search Boundary:** Kontrollierte Volltext-/Find-Läufe in der OATbyCO/DDE-Instanz: `Knau`, `Dreba`, `Plothen`, `Arnshaugk`, `Ranis`, `Weltwitz`, `Krölpa`, `Neunhofen`. Dieser Negativbefund gilt nur für diese digitale Repräsentation und Suchformen; er beweist keine historische Abwesenheit.

---

## 4. Gewählter erster Research Slice

### 4.1 Slice

**Saalfeld–Ranis–Weltwitz–Kirchenorganisation: Was trägt Sachenbacher für eine mehrschichtige Siedlungs-, Herrschafts- und Kirchenchronologie im Orlagau, und was ändert sich dadurch an #46?**

### 4.2 Begründung

Der Slice erfüllt den Clean-Room-Test besser als ein direkter Sprung zu `Knau`, weil Sachenbacher für Knau/Orla keinen direkten, kontrollierten Einzelbefund liefert. Sein Erkenntniswert liegt zunächst in einem regionalen Kontrollmodell: Wie sind archäologische Präsenz, Ortsnamen, Herrschaftszugriff und Kirchenorganisation im Orlagau methodisch zu trennen?

Dieser Slice benötigt substantiell mindestens vier Perspektiven:

1. **Archäologie / Mittelalterarchäologie** führt bei Burg-, Wallanlagen-, Keramik- und Kirchenbefunden;
2. **Diplomatik / Mediävistik / Landes- und Herrschaftsgeschichte** führt bei Urkunden, Ministerialität, Köln/Saalfeld, Mainz/Zeitz und Saalfelder Klosterrechten;
3. **Kirchengeschichte / Pfarrorganisationsgeschichte** kontrolliert Aussagen zu Urpfarreien, Archidiakonat, Sedessprengel und Slawenmission;
4. **Onomastik / historische Sprachwissenschaft** kontrolliert Ortsnamenherkunft, ohne daraus automatisch Bevölkerungsethnizität oder Gründungsdatum abzuleiten.

---

## 5. Ausgeführte Facharbeit am Slice

### SF-U2-SAC-001 – Ranis: spätes 12. Jahrhundert als urkundlicher/personeller Befund, nicht als Gründung

**A. Was sagt Sachenbacher genau?**  
Ranis wird im letzten Drittel des 12. Jahrhunderts erstmals genannt. Sachenbacher referiert Matthias Werner: Die Urkunde sei nach Gockel, *Saalfeld*, S. 514, eindeutig 1167/80 zu datieren, am ehesten 1170/80. Darin erscheint ein Ekkehard von Ranis als Angehöriger der Dienstmannschaft des Kölner Erzbischofs. Der Ortsname sei slawischen Ursprungs und von einem Personennamen abgeleitet.

**B. Druckseite und Fußnote**  
Sachenbacher 2022, Druckseite 274, Fußnoten 238–239; 1381-Stadtnennung Fußnote 240.

**C. Befundtyp**  
Übernahme/Synthese: Sachenbacher referiert Werner, der wiederum Gockel benutzt. Der Personen-/Urkundenbefund ist nicht Sachenbachers eigener Primärbefund. Die Verbindung zu einer Saalfeld/Kölner Dienstmannschaft ist diplomatisch-prosopographisch zu überprüfen.

**D. Genannte Referenzen**  
- Matthias Werner: nach Sachenbacher maßgebliche mediävistische Zusammenfassung zu Ranis/Stadt und Umfeld, genaue bibliographische Identität im Durchlauf noch nicht vollständig aufgelöst.
- Michael Gockel, `Saalfeld`, in *Die deutschen Königspfalzen. Repertorium der Pfalzen, Königshöfe und übrigen Aufenthaltsorte der Könige im deutschen Reich des Mittelalters*, Bd. 2: Thüringen, Göttingen 1991–1998, S. 465–523; Sachenbacher/Werner verweisen konkret auf S. 514.
- Ernst Eichler für die onomastische Deutung `Ranis`; genaue Stelle noch aufzulösen.

**E. Direkt überprüft?**  
Sachenbacher-Passage und Druckseite/Fußnotenziffer wurden in der OATbyCO/DDE-Kontrollinstanz überprüft. Gockel S. 514, Werner und Eichler wurden bibliographisch/als Router identifiziert, aber in diesem Durchlauf nicht direkt kollationiert. Status: `unresolved source-collation debt`.

**F. Fachkompetenz**  
- Diplomatik/Mediävistik führt: Urkunde, Datierung 1167/80, Ekkehard, Dienstmannschaft.
- Prosopographie/Ministerialitätsforschung kontrolliert: `de Ranis` als Herkunfts-/Sitzname, Dienstmannschaft des Kölner Erzbischofs.
- Onomastik kontrolliert: Ortsname slawischen Ursprungs ≠ ethnischer Status der Bewohner im 12. Jahrhundert.
- Archäologie kontrolliert: materielle und bauliche Burgentwicklung.

**G. Was erlaubt die Evidenz?**  
Wenn Werner/Gockel korrekt sind, trägt die Urkunde einen späten 12.-Jh.-Befund: ein Ekkehard `de Ranis` gehört zur Dienstmannschaft des Kölner Erzbischofs. Das ist ein starker Hinweis auf Ranis als Sitz-/Herkunftsort eines Amtsträgers im Saalfeld/Köln-Kontext.

**H. Overclaim**  
Nicht erlaubt: `Ranis wurde 1170 gegründet`; `Ranis kontrollierte Knau`; `Ranis beweist eine geschlossene Kölner Verwaltungsorganisation über die ganze Orla-Hochfläche`; `slawischer Ortsname Ranis beweist slawische Bevölkerung des 12. Jahrhunderts`; `Herrschaft = Bevölkerung`.

**I. Alternativen / SOTA-Bedarf**  
Die alternative Deutung ist nicht eine andere `Wahrheit`, sondern eine offenere Reichweite: Ekkehard kann eine konkrete Person im Dienstverband belegen, ohne dass Umfang, Zuständigkeit und territoriale Reichweite seines Sitzes bekannt sind. Nächste diskriminierende Quelle: Gockel S. 514 und der dort verzeichnete Urkundenträger samt Original-/Editionsstatus; danach Werner/Queck-Ranis-Publikation.

**J. Änderung am #46-State**  
`F-U2-004` wird **refined/bounded**: Neben Lobdeburg-Arnshaugk/Deutschordens-Schleiz ist ein früherer Saalfeld/Köln–Ranis-Strang als regionaler Herrschafts- und Ministerialitätsrouter aufzunehmen. Keine Änderung an `F-U2-002`: kein Beleg für Altenburg-Knau ↔ Orla-Knau. Keine direkte Änderung von `Knauwe villa`.

---

### SF-U2-SAC-002 – Ranis: singulärer Keramikfund des 9. Jahrhunderts als Möglichkeit, nicht als Siedlungsbeweis

**A. Was sagt Sachenbacher genau?**  
Bei Grabungen 2001 im Torhaus der Burg Ranis fand sich in einer Schicht direkt über dem Felsen eine Keramik, die in das 9. Jahrhundert eingeordnet wird und vor allem westlich der Saale Parallelen hat. Sachenbacher betont selbst, dass der Fund singulär ist, keinem Befund sicher zugeordnet werden konnte und bislang durch keine weiteren Funde in Ranis untermauert ist. Er sieht darin eine Möglichkeit, dass bereits im 9. Jahrhundert von der curtis Saalfeld aus ostsaalisch ausgegriffen wurde und Ranis einen festen Stützpunkt gebildet haben könnte.

**B. Druckseite und Fußnote**  
Sachenbacher 2022, Druckseite 277, Fußnote 248.

**C. Befundtyp**  
Archäologischer Einzelfund plus Sachenbacher-Interpretation. Die Datierung und kulturelle Zuordnung stammen aus archäologischer Typologie/Parallelen, die historische Reichweite ist eine Hypothese.

**D. Genannte Referenzen**  
Fußnote 248 verweist auf die archäologische Einordnung dieses Fundes; die genaue Literatur-/Fundberichtidentität muss aus Sachenbachers Literaturapparat beziehungsweise der Ranis-/TLAD-Dokumentation aufgelöst werden.

**E. Direkt überprüft?**  
Sachenbacher-Passage überprüft. Der Grabungsbericht, Fundkatalog, stratigraphische Dokumentation und Originalfund wurden nicht direkt geprüft. Status: `method hypothesis / still source-bound`.

**F. Fachkompetenz**  
- Archäologie führt: Stratigraphie, Fundkontext, Keramiktypologie, Datierung, Vergleichsfunde.
- Historische Geographie/Herrschaftsgeschichte kontrolliert: Ob aus dem Fund ein Saalfeld→Ranis-Ausgreifen modelliert werden darf.
- Diplomatik kontrolliert: Schriftquellenlage im 9./10. Jahrhundert und Grenzen des Schweigens.

**G. Was erlaubt die Evidenz?**  
Erlaubt ist: Auf Burg Ranis wurde ein singulärer keramischer Fund beobachtet, der typologisch ins 9. Jahrhundert eingeordnet und westsaalisch/fränkisch-karolingisch verglichen wird. Er ist ein Forschungsanker für mögliche frühere Kontakte oder Präsenz.

**H. Overclaim**  
Nicht erlaubt: `Ranis war im 9. Jahrhundert sicher ein dauerhafter Saalfelder Stützpunkt`; `westsaalische Keramik = westsaalische Bewohner`; `ein Fund = Siedlung`; `Fundlücke im 10. Jahrhundert = historische Abwesenheit`; `Ranis erklärt direkt Knau/Plothen`.

**I. Alternativen / SOTA-Bedarf**  
Alternative 1: verlagertes/sekundär eingebrachtes Material. Alternative 2: kurzzeitiger Kontakt/Transfer statt dauerhafter Stützpunkt. Alternative 3: ein noch nicht erkanntes frühmittelalterliches Nutzungsniveau. Benötigt werden vollständige Grabungsdokumentation, Fundverbleib, Vergleichskeramik, ggf. naturwissenschaftliche Datierung geeigneter Begleitfunde und Nachgrabungsdaten.

**J. Änderung am #46-State**  
`F-U2-008` wird **bounded**: Archäologie kann Schriftlücken vor der Ersterwähnung öffnen, aber der Ranis-Fund zeigt gerade die Aussagegrenze eines singulären Materials. Für Knau/Orla bestätigt dies methodisch: Keramik im Rittergutsbereich kann frühe Nutzung zeigen, aber nicht Name, Rechtsform, Gründung oder Klosterhof beweisen.

---

### SF-U2-SAC-003 – Weltwitz: Wallanlage und `slawische` Keramik ohne automatische ethnopolitische Gleichsetzung

**A. Was sagt Sachenbacher genau?**  
Weltwitz liegt auf den südlichen Höhen über der Orlasenke zwischen Neustadt und Triptis; der Ort wird 1264 im Zusammenhang mit Heinrich von Welewicz genannt. Der Ortsname ist nach Ernst Eichler slawischen Ursprungs. Die Wallanlage `Burgstadt` wurde 1990/1992 vermessen beziehungsweise untersucht. Das keramische Material gehört zur mittelslawischen Ware des 10./11. Jahrhunderts. Sachenbacher hält eine genuin slawische Fluchtburg unter der Annahme bestehender deutscher Herrschaft im Orlagau nicht für plausibel; die Anlage wird damit zum Fall, an dem materielle Kultur, politische Herrschaft und ethnische Deutung getrennt werden müssen.

**B. Druckseite und Fußnote**  
Sachenbacher 2022, Druckseiten 277–278, Fußnoten 249–252.

**C. Befundtyp**  
Archäologische Fund-/Befundsynthese plus onomastische Deutung plus herrschaftsgeschichtliche Interpretation. Sachenbacher nutzt hier keine einzelne Primärurkunde allein, sondern verschränkt Fund, Name und Herrschaftsmodell.

**D. Genannte Referenzen**  
- Ernst Eichler für die Namensdeutung `Weltwitz`/`Welewicz`.
- Grabung/Vermessung 1990/1992, unter anderem Thomas Queck bzw. TLAD-Kontext, genau aufzulösen.
- 1264-Beleg Heinrich von Welewicz: Edition/Regest/Original noch zu identifizieren.

**E. Direkt überprüft?**  
Sachenbacher-Passage und Suchfund wurden geprüft. Die Grabungspublikation und der 1264er Beleg wurden noch nicht direkt kollationiert. Status: `unresolved`.

**F. Fachkompetenz**  
- Archäologie führt: Wallanlage, Haus-/Innenbefunde, Keramik, Datierung, Funktion.
- Onomastik kontrolliert: Ortsname slawisch ≠ ethnische Kontinuität.
- Herrschaftsgeschichte kontrolliert: deutsche Herrschaft im 10./11. Jahrhundert ≠ Bevölkerungszusammensetzung.
- Siedlungsgeschichte kontrolliert: Ort 1264 ≠ Wallanlage 10./11. Jahrhundert ≠ durchgehende Ortskontinuität.

**G. Was erlaubt die Evidenz?**  
Die Evidenz erlaubt eine Wallanlage mit mittelslawischer Keramik im Orlagau und einen späteren Orts-/Personennamenbefund von 1264. Sie erlaubt die These, dass slawische materielle Traditionen im Gebiet nicht automatisch politisch autonome slawische Herrschaft bedeuten.

**H. Overclaim**  
Nicht erlaubt: `Weltwitz beweist eine slawische Fluchtburg`; `Weltwitz 1264 beweist Siedlungskontinuität seit dem 10. Jahrhundert`; `slawischer Name + Keramik = ethnische Identität`; `deutsche Herrschaft = deutsche Bevölkerung`.

**I. Alternativen / SOTA-Bedarf**  
Alternativen: kurzzeitige Befestigung, lokale Schutz-/Herrschaftsanlage, ältere Anlage mit späterer Ortsnamenslandschaft ohne direkte Kontinuität, oder Nutzung durch Gruppen unterschiedlicher sprachlich-kultureller Herkunft. Diskriminierend wären stratigraphisch gesicherte Binnenbefunde, Nachweise ständiger Besiedlung, Vergleich der Verkehrslage und vollständige Edition des 1264er Belegs.

**J. Änderung am #46-State**  
`F-U2-008` wird **reframed/refined**: Sachenbacher liefert ein starkes Beispiel für die notwendige Trennung von archäologischer Präsenz, materieller Kultur, Ortsnamenschicht und politischer Herrschaft. Für Knau/Dreba/Plothen wird dadurch kein neuer Einzelbeleg erzeugt, aber die negative Regel `Ortsname ≠ Ethnizität` und `Keramiktyp ≠ Ethnie` wird für den konkreten Orlagau sachlich unterfüttert.

---

### SF-U2-SAC-004 – Kirchenorganisation: frühe Pfarrkirchen als kirchenrechtliche Struktur, nicht als Vollbeweis lokaler Christianisierung

**A. Was sagt Sachenbacher genau?**  
Saalfeld und der Orlagau gehören bis zur Reformation zu den Sedessprengeln Pößneck und Remda des Erfurter Archidiakonats Beatae Mariae Virginis im Mainzer Erzbistum. Sachenbacher nimmt eine Kirchenorganisation im Orlagau bereits im 10. Jahrhundert an, weil der Orlagau 968 nicht dem neu gegründeten Bistum Zeitz einbezogen wurde. Für 1071 nennt er Krölpa, Neunhofen und Langenschade als älteste Pfarrkirchen im Orlagau, die dem Saalfelder Kloster inkorporiert werden. Weitere Kirchen seien pauschal genannt; Arnshaugk werde als alte Kirche in diese Zeit eingeordnet. Er deutet die Quellenrede von roher/heidnischer Bevölkerung und halbheidnischem Land nicht als Anfangszustand völliger Unchristlichkeit, sondern eher als Hinweis auf bereits fortgeschrittene Kirchenorganisation bei fortdauerndem Missions-/Integrationsprozess.

**B. Druckseite und Fußnote**  
Sachenbacher 2022, Passage nach Druckseitenmarker 285, Arbeitszitation Druckseiten ca. 286–287, Fußnoten 269–276. Die DDE/HTML-Repräsentation zeigt zwischen Druckseiten 285 und 293 nicht alle Seitenumbrüche einzeln; genaue Seitenbruchkontrolle am Druck/PDF-Bild bleibt vor externer Zitation nötig. Die Fußnotenziffern sind in der Passage sichtbar: 269 für Gockel/Graba, 270 für die 1071er Pfarrkirchen/Inkorporation, 271 für Arnshaugk, 272–274 für Enno Bünz und dessen Grundlagen, 275–276 für Rainer Müller.

**C. Befundtyp**  
Mediävistisch-kirchengeschichtliche Synthese aus Schriftquellen, kirchenrechtlicher Raumordnung, Bauforschung, Archäologie und Namenkunde.

**D. Genannte Referenzen**  
- Michael Gockel: Saalfeld/Graba und frühkirchliche Einordnung.
- 1071er Saalfelder Kloster-/Inkorporationsüberlieferung: genaue Urkunden-/Editionsidentität noch direkt aufzulösen.
- Enno Bünz, `Die mittelalterliche Kirchenorganisation im Orlagau`, in Peter Sachenbacher/Hans-Jürgen Beier (Hg.), *Der Orlagau im frühen und hohen Mittelalter*, Langenweißbach 2007, S. 65–82.
- Hannappel 1941, Eberhard 1989, Gockel 2000 als Grundlagen bei Bünz/Sachenbacher.
- Rainer Müller, Arbeiten zu Dorfkirchen im Archidiakonat St. Marien zu Erfurt, 2001/2007; genaue Titel/Stellen noch zu identifizieren.

**E. Direkt überprüft?**  
Sachenbacher-Passage und Katalog-/Suchnachweise zu Bünz wurden überprüft. Die 1071er Urkunde/Edition und Müller/Gockel-Stellen wurden noch nicht direkt kollationiert. Status: `extern fachlich gestützt`, aber nicht `Histo-methodisch abschließend abgesichert`.

**F. Fachkompetenz**  
- Kirchengeschichte führt: Archidiakonat, Sedessprengel, Pfarrei, Inkorporation, Pfarrrechte, Slawenmission.
- Diplomatik/Quellenkritik kontrolliert: 1071er Urkunde, Formelhaftigkeit, spätere Überlieferung, Rechtsgeschäft.
- Bau-/Kirchenarchäologie kontrolliert: Bauphasen, romanische Kerne, Ausgrabungslücken.
- Onomastik kontrolliert: slawischer oder deutscher Ortsname einer Pfarrkirche ≠ Ethnizität der Gemeinde.

**G. Was erlaubt die Evidenz?**  
Erlaubt ist eine starke Arbeitsthese: Im 11. Jahrhundert bestanden im Orlagau kirchliche Strukturen, die über einzelne Ortsnennungen hinausreichen. Krölpa, Neunhofen und Langenschade sind als frühe Pfarrkirchen/Urpfarreien ein prioritäres Kontrollcorpus für die regionale Siedlungs- und Kirchenlandschaft.

**H. Overclaim**  
Nicht erlaubt: `alle Einwohner waren 1071 christlich`; `Kirchenorganisation = vollständige Missionierung`; `Pfarrei = Dorfgründung`; `frühe Pfarrkirche = direkte Zuständigkeit für Knau`; `slawische Ortsnamen der Pfarrorte = slawische Pfarreien`; `deutscher Ortsname Neunhofen = deutsche Bevölkerung`.

**I. Alternativen / SOTA-Bedarf**  
Die zentrale Alternative ist graduell: Kirchenrechtliche Besetzung und Missionierung können gleichzeitig existieren, ohne dass soziale Praxis, Bestattung, Memorialkultur und Pfarrbindung vollständig durchgesetzt sind. Diskriminierende Quellen: Urkundenwortlaut 1071/1074, Archidiakonats-/Sedessprengelquellen, Patrozinien, Kirchenbauphasen, Friedhofs-/Bestattungsarchäologie, spätere Visitationsprotokolle als Rückprojektionskontrolle.

**J. Änderung am #46-State**  
`F-U2-008` wird **confirmed/refined**: Ersterwähnung bleibt von Siedlungsbeginn getrennt; Kirchenorganisation ist eine eigene Achse. `F-U2-004` wird **expanded/bounded**: Neben Deutschordens-/Naumburg-/Schleiz-Belegen muss die Saalfeld/Mainz/Krölpa-Neunhofen-Langenschade-Schicht als eigener, früher kirchlich-herrschaftlicher Raumrouter geführt werden. Direkter Knau-Beleg: `unchanged / unresolved`.

---

### SF-U2-SAC-005 – Negativ-/Nichtdirektbefund für Knau, Dreba, Plothen in Sachenbacher

**A. Was sagt Sachenbacher genau?**  
In der kontrollierten DDE-Volltextsuche ergab `Knau` einen Treffer zu `Knau, Ot. von Zetscha` im Altenburger Land: 1970 erkannte Peter Weise rechteckige Grubenverfärbungen; Vogt datiert sie ins 10.–11. Jahrhundert. Dies gehört nicht zum Orla-Knau. `Dreba` und `Plothen` ergaben keine Treffer.

**B. Druckseite und Fußnote**  
`Knau, Ot. von Zetscha`: Sachenbacher 2022, Druckseitenbereich um den Altenburger Siedlungsabschnitt, DDE-Passage mit Fußnote 61. Exakte Druckseite im Durchlauf nicht nach Bildseite kontrolliert; nicht für Orla-Knau verwenden.

**C. Befundtyp**  
Archäologischer Siedlungsbefund im Altenburger Land; für #46 nur als Homonym-/Nicht-Merge-Warnung relevant.

**D. Genannte Referenz**  
H.-J. Vogt / Corpus beziehungsweise Fundmeldung zu Knau OT Zetscha, genaue bibliographische Stelle aus Sachenbachers Literaturapparat noch aufzulösen.

**E. Direkt überprüft?**  
Nur Sachenbacher/DDE-Suchbefund; keine Originalfundmeldung.

**F. Fachkompetenz**  
Archäologie führt beim Altenburger Befund; Entity Resolution/Onomastik kontrolliert den Ortsbezug; #46-Diplomatik/Quellenkritik verhindert die Verschmelzung mit Orla-Knau.

**G. Was erlaubt die Evidenz?**  
Sie erlaubt nur: Sachenbacher enthält einen `Knau`-Treffer, der zum Altenburger/Zetscha-Komplex gehört. Das stützt indirekt die #46-Regel, gleichnamige/ähnliche Orte nicht zu verschmelzen.

**H. Overclaim**  
Nicht erlaubt: `Sachenbacher belegt Knau bei Neustadt/Orla im 10./11. Jahrhundert`; `Altenburger Knau-Siedlungsbefund erklärt Orla-Knau`; `kein Dreba/Plothen-Treffer = historische Abwesenheit`.

**I. Alternativen / SOTA-Bedarf**  
Weitere Suchformen können in Sachenbacher noch indirekte Treffer liefern: historische Namen, Gewässernamen, Nachbarorte, Pfarreien, Herrschaftsträger. Eine kontrollierte Lemmaliste aus Ortsnamenbüchern bleibt nötig.

**J. Änderung am #46-State**  
`F-U2-002` wird **confirmed/unchanged**: Altenburger Knau und Orla-Knau dürfen nicht zusammengeführt werden. `F-U2-007` bleibt **unresolved**: `Knauwe villa` 1374/1378 wird durch Sachenbacher nicht aufgelöst. `F-U2-008` bleibt **refined**: archäologische Befunde sind orts- und instanzgenau zu führen.

---

## 6. Zusammenführung der Fachperspektiven ohne Evidenzvermischung

Für den Slice ergibt sich kein lineares Modell `slawische Wildnis → deutsche Eroberung → Kirchen/Mönche → Dörfer/Teiche`. Die belastbarere, aber weiterhin bounded formulierte Struktur lautet:

```text
Saalfeld als frühes Herrschafts-/Kirchenzentrum
→ Orlagau als Kontakt- und Ausbauraum mit slawischen und deutschen Elementen
→ Ranis als möglicher Saalfeld/Köln-Ministerialitäts- und Herrschaftspunkt im 12. Jh.
→ Weltwitz als archäologisch-onomastischer Grenzfall von materieller Kultur, Herrschaft und Siedlungsdeutung
→ frühe Pfarr-/Kirchenorganisation als eigene Raumachse
→ lokale Orte wie Knau/Dreba/Plothen bleiben separat quellenkritisch zu belegen
```

Damit werden folgende Achsen ausdrücklich getrennt:

| Achse | Was Sachenbacher beiträgt | Was nicht folgt |
|---|---|---|
| Archäologische Präsenz | Ranis 9.-Jh.-Einzelfund; Ranis 12.–14./15.-Jh.-Burgmaterial; Weltwitz 10./11.-Jh.-Keramik | keine sichere Orts-/Herrschafts-/Bevölkerungskontinuität |
| Materielle Kultur | westsaalische/fränkisch-karolingische Parallelen; mittelslawische Ware | keine automatische Ethnizität |
| Ortsnamenschicht | Ranis/Weltwitz slawisch gedeutet | kein Gründungsdatum, keine ethnische Zusammensetzung |
| Politische Herrschaft | Ekkehard von Ranis als Kölner Dienstmannschaft, wenn Werner/Gockel korrekt | keine direkte Zuständigkeit für Knau/Plothen |
| Kirchliche Organisation | 1071 Krölpa/Neunhofen/Langenschade; Mainz/Erfurt/Pößneck/Remda | keine vollständige Christianisierung jeder lokalen Gruppe |
| Siedlungsplatz | Weltwitz/Altenburg-Zetscha/Ranis als jeweilige Orte/Fundorte | keine unkontrollierte Übertragung auf Orla-Knau |
| Ortskontinuität | teils plausibel, teils offen | nicht aus Name + Keramik allein beweisbar |
| Ersterwähnung | Ranis 1167/80 bzw. Stadt 1381; Weltwitz 1264 | nicht Gründung |

---

## 7. Konkrete Disposition bestehender #46-Findings

| #46 Finding | Disposition durch Sachenbacher-Slice | Begründung |
|---|---|---|
| F-U2-001 Altenburger `Knewe/Kneben/Knewer` | `unchanged` | Sachenbacher liefert keinen neuen Beleg zur DO-/Altenburger Personenserie. |
| F-U2-002 Altenburger Knau ≠ Orla-Knau | `confirmed/refined` | Der `Knau`-Treffer bei Sachenbacher gehört zu Zetscha/Altenburger Land; nicht zu Knau bei Neustadt/Orla. |
| F-U2-003 Stange ↔ Knewe Netzwerk statt Genealogie | `unchanged` | Kein neuer Stange/Knewe-Beleg. |
| F-U2-004 Lobdeburg-Arnshaugk ↔ DO/Schleiz regionaler Herrschaftsbefund | `expanded/bounded` | Sachenbacher ergänzt ältere Saalfeld/Köln–Ranis- und Mainz/Saalfeld-Kirchenachsen; keine direkte Knau-Beziehung. |
| F-U2-005 False merges | `confirmed` | Sachenbacher selbst erzeugt einen neuen Homonym-Fall: `Knau` OT Zetscha darf nicht Orla-Knau werden. |
| F-U2-006 Corpus-Negativbefunde | `confirmed` | `kein Treffer` für Dreba/Plothen in DDE ist nur Suchboundary, keine historische Abwesenheit. |
| F-U2-007 `Knauwe villa` 1374/1378 | `unchanged/unresolved` | Sachenbacher löst die Datierungs-/Quellenfrage nicht. |
| F-U2-008 Ersterwähnung ≠ Siedlungsbeginn | `confirmed/refined` | Sachenbacher liefert mehrere regionale Beispiele, die Archäologie, Ortsname, Kirche und Erstnennung trennen. |

---

## 8. Neue Quellen-, Literatur- und Suchinventar-Hooks

### 8.1 Prioritäre direkte Prüfungen

1. **Gockel, `Saalfeld`, S. 514**: Urkunde 1167/80, Ekkehard von Ranis, Überlieferungsstatus, Wortlaut, Datierung, Dienstmannschaft.
2. **Matthias Werner zu Ranis**: genaue Publikation, Zitatkontext, Beziehung Werner ↔ Gockel, eventuelle Original-/Regestenangaben.
3. **Thomas Queck / TLAD zu Burg Ranis**: Grabungen ab 2000/2001, Torhausfund, Stratigraphie, Fundverbleib, Keramikparallelen.
4. **Weltwitz/Burgstadt**: Grabungs-/Vermessungspublikationen 1990/1992, Keramiktypologie, 1264er Beleg Heinrich von Welewicz.
5. **1071er Saalfeld-/Pfarrkirchenüberlieferung**: Urkundenedition, Original/Kopiar, Rechtsgeschäft, Wortlaut zu Krölpa, Neunhofen, Langenschade, weiteren Kirchen, Kirchenerrichtungsverbot, `halbheidnisch`.
6. **Bünz 2007, S. 65–82**: mittelalterliche Kirchenorganisation im Orlagau, Kriterien, Sedessprengel, Urpfarreien, Quellenbasis.
7. **Rainer Müller 2001/2007**: Dorfkirchen im Archidiakonat St. Marien zu Erfurt, romanische/gotische Bauphasen, Vergleich slawisch/deutsch benannter Orte.
8. **Eichler/Rosenkranz/Rempel**: Namendeutungen Ranis, Weltwitz, Krölpa, Graba/Gräfendorf, und methodischer Konflikt onomastischer Deutungen.

### 8.2 Suchbegriffe / Entity Hooks

`Ekkehardus de Ranis`, `Ekkehard von Ranis`, `Ranis`, `Burg Ranis`, `Museum Burg Ranis`, `Burgstadt Weltwitz`, `Welewicz`, `Heinrich von Welewicz`, `Ludwigshof`, `Graba`, `Krölpa`, `Neunhofen`, `Langenschade`, `Arnshaugk Kirche`, `Sedessprengel Pößneck`, `Sedessprengel Remda`, `Archidiakonat Beatae Mariae Virginis`, `Erzbistum Mainz`, `Bistum Zeitz 968`, `Kölner Dienstrecht Saalfeld`, `Gockel Saalfeld S. 514`, `Bünz Kirchenorganisation Orlagau`, `Rainer Müller Dorfkirchen Archidiakonat St. Marien Erfurt`, `Eichler Ranis`, `Eichler Weltwitz`, `Rempel 1071 1074 Orlagau`.

---

## 9. Methodischer Befund für #60

Dieser Slice bestätigt als methodische Arbeitsregel:

```text
Sekundärwerk-Integration muss zuerst die Bauart des Werkes erfassen,
dann einen diskriminierenden Research Slice wählen,
und jeden tragenden Befund nach Evidenzachse, Quellenschicht,
Fachzuständigkeit und Overclaim-Risiko zerlegen.
```

Insbesondere für Siedlungsgeschichte ist ein gemeinsamer Befundkomplex nur dann belastbar, wenn jede Fachperspektive ihre Referenz behält:

- Archäologie bekommt Fundstelle, Stratigraphie, Fundmaterial, Datierung und Publikation;
- Diplomatik bekommt Urkunde/Regest/Edition, Wortlaut, Datierung, Überlieferung und Rechtsgeschäft;
- Onomastik bekommt historische Form, editorische Normalisierung, Deutung, Sprachschicht und Deutungskontroverse;
- Kirchengeschichte bekommt Pfarrei, Archidiakonat, Sedessprengel, Inkorporation, Patrozinien, Kirchenbau und spätere Verwaltungsquellen;
- Histo-Orla-Synthese darf erst danach begrenzt integrieren.

Status dieses Methodenbefunds: `method hypothesis / live-test-supported / not yet promoted to working-method`.

---

## 10. Handoff-Check

1. **Materiell geändert:** Sachenbacher wurde als Publikation bauartig eingeordnet; erster Slice ausgeführt; Ranis/Weltwitz/Kirchenorganisation/Knau-Negativbefund ausgewertet; #46-Findings dispositioniert; neue Quellen-/Suchhooks gesichert.
2. **Kanonischer Ort:** Diese Datei ist ein #46-Research-Artefakt auf Branch `research/sachenbacher-clean-room-20260903`; Source-Ledger-Delta und #60-Methodenlearning werden separat im selben Branch persistiert.
3. **Work-Owner-Status:** #46 und #60 erhalten Kommentare mit Branch/PR-Verweis.
4. **Evidenz/Begründung/Trade-offs:** Pro Befund A–J dokumentiert; nicht direkt kollationierte Quellen als `unresolved` markiert.
5. **Offene Punkte/Nächste Aktionen:** Prioritäre direkte Prüfungen in Abschnitt 8.1.
6. **Blocker #44:** Kein neuer Blocker; bestehender DD-20260903-001 zu Safe Mutation/Direct Writes bleibt relevant. Deshalb Branch statt direkter Main-Mutation.
7. **PROJECT_STATE.md:** Main-`PROJECT_STATE.md` wurde in diesem Durchlauf nicht direkt geändert. Der Handoff ist über Branch/PR und Issue-Kommentare gesichert; nach Merge sollte `PROJECT_STATE.md` ggf. um den abgeschlossenen Sachenbacher-Slice ergänzt werden.
8. **Restartability:** Ein neuer Bearbeiter kann aus #46/#60-Kommentaren und den Branch-Artefakten ohne Chatwissen fortsetzen.
