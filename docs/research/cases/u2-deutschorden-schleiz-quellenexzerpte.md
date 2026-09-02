# U2 – Deutschordensballei Thüringen: Schleiz / Mönchgrün

**Status:** `working-research / corpus-dossier / first iteration`  
**Work Owner:** #46  
**Pilot interface:** #61  
**Parent register:** `docs/research/cases/u2-orlagau-suchraum-quellenexzerpte.md`  
**Source identity:** `SRC-ED-0004` in `docs/research/cases/orlagau-source-ledger.md`  
**Applicable method status:** gemeinsamer Pflichtkern aus #45 und dem bindenden Source-Identity-Protokoll; Exzerptstandard v0.2 als case-spezifische Arbeitsmethode; domänenspezifische Profile unter #60 noch nicht als `validated-method` beansprucht  
**Stand:** 2026-09-02

## Zweck und Grenze dieser Iteration

Diese erste Pilotiteration erschließt den bekannten Fall vom 5. September 1285 unmittelbar an der öffentlich zugänglichen digitalen Editionsinstanz. Sie testet Source-/Edition-/Instance-/Findspot-Treue, kontexterhaltendes Exzerpieren, getrennte Befundzustände und evidenzgeführte Rückspeisung in das Suchinventar.

Inspiziert wurden die THULB-Landingpage, das IIIF-Manifest, Titel-/Vorwortseiten und die Seitenbilder von Lampe Nr. 420 auf den Druckseiten 360–361. Nicht inspiziert wurden das im Editionsapparat genannte Original, die Abschriften oder die Parallelabdrucke. Daher werden diplomatische Echtheit, Lesarten des Originals, heutige Archivsignatur und Lampes Personen-/Ortsidentifikationen in diesem Pass nicht unabhängig validiert.

## EX-U2-0009 – Lampe Nr. 420: Eigentumsübertragung des bereits gekauften `Grune`, 5. September 1285

### Provenienz / Fundstelle

- **excerpt_id:** `EX-U2-0009`
- **source_id:** `SRC-ED-0004`
- **digital_instance_id:** `DI-THULB-HISBEST-00021244`
- **source_genre:** edierte mittelalterliche Urkunde; Verfügung/Eigentumsübertragung mit Beglaubigungsfunktion
- **source_instance_status:** `scholarly edition scan inspected; critical apparatus inspected; original/copies not inspected`
- **edition:** Karl H. Lampe (Hg.), *Urkundenbuch der Deutschordensballei Thüringen*, Bd. 1, Nr. 420.
- **date / place stated by edition and text:** Schleiz, 5. September 1285; Text: `Datum et actum in Slewicz ... nonas Septembris`.
- **printed pages:** 360–361.
- **scan / IIIF mapping:** scan 378 = Druckseite 360; scan 379 = Druckseite 361.
- **stable object:** `https://collections.thulb.uni-jena.de/receive/HisBest_cbu_00021244`; URN `urn:nbn:de:urmel-ba67ebf9-1fe1-4cfe-ba81-aa4d4879f62e6`; IIIF manifest im Source Ledger.
- **edition apparatus – original:** `HSA Dresden, Orig. No. 1104`; Pergamenturkunde, laut Lampe in den Brüchen etwas zerfallen, beschädigtes Siegel an roten Seidenfäden (`O`). Dies ist eine historische Editionssignatur, keine als aktuell verifizierte Archivsignatur.
- **edition apparatus – copies:** `HSA Dresden, Abt. XIV, A. 64, Bl. 83 (A)` mit Überschrift `Littera de bonis et villa in Grune`; außerdem `HSA Dresden, Abt. XIV, B. 160, Heft 8, No. 3 (M)`.
- **endorsement reported by edition:** `Confirmatio ville Grune dominorum de Gera`.
- **language:** Latein; editorisches Regest und Apparat Deutsch.
- **review_status:** `candidate excerpt / ready for human rereading; not independently specialist-validated`.

### Editorisches Regest – nicht Quellentext

Lampe regestiert:

> Otto `[IV.]` von Lobdeburg, genannt von Arnshaugk, und Hartmann `[XI.]`, sein Sohn, eignen dem Deutschen Hause in Schleiz das von diesem gekaufte Dorf Mönchgrün zu.

Die Ordnungszahlen in eckigen Klammern und die Identifikation `Mönchgrün` sind editorische Zusätze. Der Urkundentext nennt `Otto de Lodeburch dictus de Arnshouge`, `Hartmannus filius noster` und `villa in Grune`.

### Historischer Wortlaut – vollständiger relevanter Rechtsgeschäfts- und Beglaubigungszusammenhang

> `Nos Otto de Lodeburch dictus de Arnshouge et Hartmannus filius noster notum esse cupimus universis, quibus presens scriptum fuerit recitatum, quod fratres domus Theutonice in Slewicz quandam villam in Grune compararunt pro certa pecunie quantitate iusto empcionis et vendicionis titulo accedente. Nos autem ob reverenciam omnipotentis dei et gloriose virginis matris sue nec non ob remedium nostre anime et salute et progenitorum nostrorum predictam villam in Grune fratribus iam dictis in Slewicz damus in proprium et tradimus cum omni utilitate et sollempnitate iuris et facti, que in huiusmodi donacionibus requiruntur, perpetuo possidendam. Testes huius donacionis sunt: Hedinricus de Crobz, Rudolfus de Rodhe, Heinricus de Mosin, milites; Heinricus officiatus noster, Heinricus de Plauwe civis et quam plures fide digni. Ut autem premissa nostra donacio robur obtineat perpetue firmitatis, presentem litteram dari fecimus omnium predictorum in testimonium sigilli nostri munimine roboratam. Datum et actum in Slewicz anno incarnacionis domini millesimo ducentesimo octogesimo quinto, nonas Septembris.`

### Editionsvarianten / Eingriffe

Lampe druckt bzw. vermerkt unter anderem:

- Haupttext `Lodeburch`; `A: Lobeburg`.
- Haupttext `Arnshouge`; `A: Arnshauge`.
- Haupttext `Theutonice`; `O: Theteutonice`.
- die Stelle nach `anime` ist im Original laut Apparat unleserlich; die hier wiedergegebene Lesung folgt Lampes Haupttext, während `A` dort abweicht.
- `sollempnitate` und `perpetuo` enthalten editorisch markierte Ergänzungen wegen unleserlicher Stellen im Bruch des Originals.
- Haupttext `Hedinricus de Crobz`; `A: Heinricus de Crabez`.
- Haupttext `quam plures fide digni`; `A: pl. alii`.

Damit ist der Editionswortlaut verwendbar, aber nicht wie eine unmittelbar gelesene Originalausfertigung zu behandeln.

### Source-explicit observations

1. **Akteure/Rollen:** Otto `de Lodeburch dictus de Arnshouge` und sein Sohn Hartmann treten gemeinsam als Aussteller/Verfügende auf. Die Vater-Sohn-Relation ist ausdrücklich (`filius noster`).
2. **Empfänger:** die Brüder des Deutschen Hauses in Schleiz (`fratres domus Theutonice in Slewicz`).
3. **Vorausgehendes Rechtsgeschäft:** Die Brüder hatten ein Dorf `in Grune` gegen eine bestimmte, aber nicht bezifferte Geldsumme aufgrund eines Kauf-/Verkaufstitels erworben (`compararunt pro certa pecunie quantitate iusto empcionis et vendicionis titulo`). Verkäufer und Zahlungsmodalitäten nennt dieses Stück nicht.
4. **Handlung der Aussteller:** Otto und Hartmann geben und übertragen dasselbe Dorf den Brüdern als Eigentum zur dauernden Besitzung (`damus in proprium et tradimus ... perpetuo possidendam`).
5. **Umfang:** übertragen wird das Dorf mit allem Nutzen und den für solche Schenkungen erforderlichen Rechts- und Handlungssolennitäten; einzelne Rechte, Dienste, Grenzen oder Zubehörteile werden nicht aufgezählt.
6. **Explizite religiös-memoriale Begründung:** Ehrfurcht vor Gott und Maria sowie Seelenheil der Aussteller und ihrer Vorfahren werden für die Handlung Ottos und Hartmanns genannt. Der Wortlaut belegt nicht, dass dies das einzige Motiv war.
7. **Zeugen:** drei als Ritter bezeichnete Männer – Hedinricus von Crobz, Rudolf von Rodhe, Heinrich von Mosin – sowie Heinrich, `officiatus noster`, und Heinrich von Plauen, Bürger; weitere glaubwürdige Personen bleiben ungenannt.
8. **Beglaubigung:** Die Urkunde soll der dauerhaften Festigkeit der Schenkung dienen und wird ausstellerseitig mit `sigilli nostri` befestigt. Der Text ordnet das einzige Siegel keinem der beiden Aussteller individuell zu; Lampe beschreibt ein beschädigtes Siegel.
9. **Ort/Zeit:** Ausstellung und Handlung in Schleiz am 5. September 1285.

### Quellenfunktion / Aussagegrenzen

Das Stück dokumentiert und befestigt die Eigentumsübertragung durch Otto und Hartmann nach einem bereits erfolgten Kauf der Ordensbrüder. Es ist keine vollständige Kaufurkunde, keine Besitzbeschreibung des Dorfes und keine neutrale Gesamtdarstellung der Interessen aller Beteiligten.

Der Beleg trägt direkt:

- den gemeinsamen Verfügungsakt von Otto und Hartmann;
- den Deutschen Orden in Schleiz als Empfänger;
- den vorausgesetzten entgeltlichen Erwerb eines `villa in Grune`;
- die Übertragung als Eigentum und die explizite religiös-memoriale Begründung der Aussteller;
- Zeugen, Amtsträger, Ort und Datum im Editionswortlaut.

Der Beleg trägt ohne weitere Quellen **nicht**:

- wer das Dorf zuvor an den Orden verkauft hatte oder wie hoch die Summe war;
- welche dingliche/lehnsrechtliche Position Otto und Hartmann vor dem Eigentumstransfer besaßen;
- dass der Kauf selbst religiös motiviert war;
- dass `Grune` allein aus dem Quellentext sicher modernem Mönchgrün entspricht – diese Identifikation ist hier editorisch;
- eine Gesamtstrategie des Ordens, eine Verbindung zu Knau/Orla, einen Eintritt Hartmanns in den Orden oder eine vollständige Motivpsychologie;
- eine unveränderte heutige Archivsignatur oder die Lesart des Originals.

## Befundzustände dieser Iteration

### Working findings

- `WF-U2-0009-A`: In Lampes Editionszeugnis setzt die Eigentumsübertragung vom 5. September 1285 einen bereits erfolgten entgeltlichen Erwerb des Dorfes durch die Schleizer Deutschordensbrüder voraus. Die Vorgänge `Kauf` und `Eigentumsübertragung` dürfen nicht zu einer einzigen unbestimmten Schenkung verschmolzen werden.
- `WF-U2-0009-B`: Otto und Hartmann handeln gemeinsam; die Quelle macht Hartmann nicht nur zum genealogisch genannten Sohn, sondern zum Mit-Aussteller des Verfügungsakts.
- `WF-U2-0009-C`: Die religiös-memoriale Formel bezieht sich grammatisch auf die Übertragung durch Otto und Hartmann. Sie belegt eine artikulierte Rechts-/Memoriallogik, aber kein exklusives persönliches Motiv und nicht den Grund des vorausgegangenen Kaufs.

### Unresolved

- heutige Archivsignatur und Erhaltungs-/Digitalisierungsstatus von Lampes `Orig. No. 1104`;
- Wortlaut/Lesarten am Original und Abhängigkeit der Kopien `A` und `M`;
- Verkäufer, Kaufurkunde, Kaufpreis und genaue Rechtsposition vor der Auflassung/Eigenübertragung;
- unabhängige Absicherung der editorischen Identifikation `Grune = Mönchgrün`;
- prosopographische Identität/Funktion der Zeugen und des `officiatus noster`;
- Verhältnis zu Patronatsübertragung/Bestätigung Schleiz 1284 und weiteren Schleizer Ordensrechten.

### Historical hypotheses – ausdrücklich noch nicht promoted

- Patronat 1284 und Dorferwerb/Eigentumsübertragung 1285 könnten Teile einer kurzfristigen regionalen Verdichtung von Rechten des Schleizer Hauses sein. Zeitliche und institutionelle Nähe allein beweist diese Strategie nicht.
- Die gemeinsame Ausstellung könnte auf eine für die Verfügung relevante dynastische/familienrechtliche Position Hartmanns hinweisen; Art und Reichweite dieser Position sind ohne Vorurkunden und Vergleichsstücke offen.
- Die Memoriaformel könnte neben der Rechtsübertragung eine Memorialbeziehung zum Orden etablieren; konkrete liturgische Leistungen nennt die Urkunde nicht.

### Research Hooks / nächste Iteration

1. Die vorausgehende Kaufurkunde bzw. den Verkäufer über Lampes Register, benachbarte Stücke, Schmidt, Alberti und Dobenecker identifizieren.
2. Moderne Archivkonkordanz zu `HSA Dresden, Orig. No. 1104` und den Kopien ermitteln; Originalbild/Abschriften prüfen.
3. `Grune` onomastisch/topographisch und über Editionsregister/Parallelüberlieferung unabhängig absichern; Suchformen `Grune`, `Gruna`, `Grün`, `Mönchgrün` getrennt führen.
4. Otto und Hartmann sowie die Zeugen `Crobz/Crabez`, `Rodhe`, `Mosin`, den `officiatus noster` und `Heinricus de Plauwe civis` im zeitnahen Corpus verfolgen.
5. Nr. 420 mit der Schleizer Patronatsbestätigung von 1284 (`EX-U2-0008`) und späteren Besitz-/Rechtssicherungen vergleichen; Ko-Präsenz/zeitliche Nähe zunächst nur als Research Hook.
6. Für menschliches Gegenlesen besonders prüfen: Transkription der beschädigten/ergänzten Stellen, Reichweite von `in proprium`, syntaktische Reichweite der Memoriaformel und ausreichender Exzerptumfang.

## Pilotbeobachtung für #61

Der Lauf war aus Repo-State restartbar, nachdem Work Owner, Source-Identity-Protokoll, Zielartefakte und nächste diskriminierende Aktion gemeinsam gelesen worden waren. Reale Friktion: Die bekannte Quelle war im Findings-Artefakt bereits als Fakt genannt, aber die konkrete digitale Editionsinstanz fehlte im Source Ledger und ein fundstellenfähiges Exzerpt fehlte vollständig. Der Pilot schließt diese Lücke für Nr. 420, zeigt aber zugleich, dass ein bloßer vorhandener Finding-Satz weder Evidence Availability noch Excerpt-/Findspot-Fidelity garantiert.

Disposition: `refine` vorhandenes F-U2-004; keine neue Requirement- oder Architecture-Promotion aus diesem Einzelfall.

---

## Zweite Pilotiteration – allgemeiner Bandlauf an der bereitgestellten PDF-Instanz

**Instanz:** `DI-IA-THRINGISCHEGES10`

**Suchreihenfolge:** Band-/Registerstruktur und breites Varianteninventar zuerst; Nr. 420 erst danach als Kontrolltreffer.
**Status:** `candidate excerpts / working observations; human rereading pending; no independent specialist validation`

### Search / inspection boundary

Durchsucht wurden der OCR-Textlayer des gesamten 832-seitigen PDF, der Namenweiser und die dort rückverwiesenen Editionsstellen. Verwendet wurden moderne Nutzerformen, belegte historische Varianten sowie aus Treffern neu gewonnene Formen, darunter `Arnshaugk / Arnshoge / Marnshoge`, `Lobdeburg / Lodeburch`, `Schleiz / Slewicz / Slowicz / Slovwicz`, `Grüne / Grune / Mönchgrün`, `Dittersdorf / Ditherichesdorf / Dytherichsdorph`, `Wetterau / Wederowe`, Personen- und Amtsformen sowie Deutschordenshaus-/Patronatskontexte. Relevante Seiten wurden am Scan kontrolliert. Der Lauf ist keine Vollkollation aller 783 Nummern und kein Beleg regionalhistorischer Vollständigkeit.

Der Namenweiser bündelt für `DOH. Schleiz` insbesondere Nr. 266, 420, 526, 602, 604, 664–666, 671–672 und 681; für die Schleizer Pfarrkirche Nr. 404–405, 473, 604, 670–671 und 783. Für Otto `[IV.]` von Arnshaugk verweist er zusätzlich auf Nr. 122, 252, 383, 394 und 404–405. Diese Registerrelationen sind editorische Retrieval-Hilfen, keine historischen Aussagen.

### EX-U2-0010 – Schleizer Patronatsübertragung und bischöfliche Bestätigung, Lampe Nr. 404–405

#### Provenienz / Fundstelle

- **source_id / instance:** `SRC-ED-0004` / `DI-IA-THRINGISCHEGES10`
- **source_genre:** zwei edierte Urkunden: Übertragung eines Patronatsrechts; bischöfliche Bestätigung.
- **date / place:** Nr. 404 `[vor 1284 Dez. 10]`, ohne Datum im Text; Nr. 405 Naumburg, 10. Dezember 1284.
- **printed / PDF pages:** 341–343 / PDF 361–363.
- **edition transmission:** Nr. 404: laut Lampe Original `HSA Dresden, Orig. No. 1089`, Abschriften `A. 64, Bl. 99` und `B. 160, Heft 8, No. 1`; Nr. 405: Original `Orig. No. 1085`, Abschriften `A. 64, Bl. 99b` und `B. 160, Heft 8, No. 2`. Historische, nicht aktuell verifizierte Signaturen.
- **review_status:** `candidate excerpt; scan and apparatus inspected; originals/copies not inspected`.

#### Historischer Wortlaut – sachlich tragender Zusammenhang

Nr. 404:

> `Otto de Arnshoge ... ius patronatus ecclesie parrochialis in Slewiz, quod ad nos pertinebat, Nuwemburgensis dyocesis cum heredum nostrorum consensu et unanimi voluntate eisdem fratribus sive ordini ipsorum liberaliter dedimus, tradidimus et contulimus cum omnibus proventibus et pertinenciis iam habitis proprietatis tytulo perpetuis temporibus possidendum.`

Nr. 405:

> `Ex litteris patentibus nobilis viri domini Ottonis de Marnshowe nobis directis ... legitime nobis constitit, quod idem nobilis ius patronatus ecclesie parrochialis in Slewiz nostre dyocesis canonice eisdem fratribus et ordini contulit ... eandem collacionem ... dyocesana auctoritate ... confirmamus.`

#### Source-explicit observations / Quellenfunktion

1. Nr. 404 stellt Otto als bisherigen Träger des Schleizer Patronatsrechts dar; die Übertragung erfolgt mit ausdrücklich behauptetem einmütigem Erbenkonsens und umfasst bestehende Einkünfte/Zubehör.
2. Nr. 405 ist keine Wiederholung desselben Rechtsakts, sondern die Bestätigung durch den Naumburger Bischof nach Ottos Schreiben und Bitten des Deutschmeisters Konrad von Feuchtwangen und weiterer Brüder.
3. Die religiösen Begründungen gehören zur Selbstdarstellung und Rechts-/Memorialfunktion der Stücke. Sie beweisen weder Alleinmotiv noch eine umfassende Ordensstrategie.
4. Lampes Datierung von Nr. 404 auf 1284 ist editorische Argumentation im Zusammenhang mit Nr. 405; der Text von Nr. 404 selbst ist undatiert.

#### Working finding / unresolved / hooks

- **WF-U2-0010:** Der Editionsbefund trägt eine zweistufige Rechtssequenz `Übertragung durch Otto → diözesane Bestätigung`, die spätestens am 10. Dezember 1284 abgeschlossen war.
- **unresolved:** exakter Ausstellungszeitpunkt Nr. 404; Rechtsherkunft des Patronats; Identität/Reichweite des genannten Erbenkonsenses; Original-/Kopienlesarten und aktuelle Archivsignaturen.
- **hook:** Nr. 404–405 mit Nr. 420 vergleichen, aber zeitliche Nähe nicht als Gesamtstrategie promoten; außerdem das von Lampe zu Nr. 404 gestellte Schleizer Pfarrstück von 1232 und dessen Vidimus von 1310 gesondert exzerpieren.

#### Nutzerverständlicher Zugang – abgeleitete Sicht, keine zweite Research Truth

Otto von Arnshaugk überließ dem Deutschen Orden das Recht, die Schleizer Pfarrstelle zu besetzen. Der Naumburger Bischof bestätigte diese Übertragung spätestens am 10. Dezember 1284. Relevant ist die gestufte Absicherung eines wichtigen kirchlichen Rechts. Offen bleiben vor allem das genaue Datum der ersten Urkunde, die Vorgeschichte des Rechts und ob daraus zusammen mit späteren Erwerbungen eine übergreifende Strategie abgeleitet werden darf.

### EX-U2-0011 – Kauf, Auflassung und Eigentumsbestätigung in Wüstendittersdorf, Lampe Nr. 602/604

#### Provenienz / Fundstelle

- **date:** 5. und 13. Dezember 1297.
- **printed / PDF pages:** 515–518 / PDF 535–538.
- **transmission:** Nr. 602 laut Lampe Original `Orig. No. 1558`; Nr. 604 Original `Orig. No. 1560`; jeweils Abschriften in `A. 64` und `B. 160`. Originale/Kopien nicht inspiziert.
- **source_genre:** städtische Bezeugung eines Kauf-/Resignationsgeschäfts; landgräfliche Eigentumsübertragung/Bestätigung.

#### Historischer Wortlaut – zentrale Passagen

Nr. 602:

> `Witego de Cossebode ... dimidium mansum cum curia attinente in Diterichesdorf ... pro duabus marcis et dimidia conparavit ... eorundemque bonorum subsides usum lignorum pascueque ... idem Witego bona eadem ... libere resignavit.`

Nr. 604:

> `dimidium mansum in villa dicta Ditherichesdorf situm cum iure lignorum seu silvestri pascuorum ... quem Wethego de Kozzeboden a nobis tytulo feudi habuit et fratribus ... pro duabus marcis et dimidia argenti ... vendidit et nobis libere et voluntarie resignavit, apropriavimus ecclesie et domui ... in Slowicz.`

#### Source-explicit observations / Quellenfunktion

1. Nr. 602 nennt Verkäufer, Käufer, Kaufpreis, Hof/Halbhufe, Holz-/Weiderechte, weitere Dienste und die Auflassung durch Witego; außerdem eine Rückabwicklungs-/Sicherungsklausel für den Fall verweigerter landgräflicher Eigentumsübertragung.
2. Nr. 604 erklärt die vorgelagerte Rechtsposition: Witego hielt das Gut vom Landgrafen zu Lehen, verkaufte an das Schleizer Haus und resignierte es an den Landgrafen; dieser übertrug es anschließend als Eigentum.
3. Die acht Tage auseinanderliegenden Stücke dokumentieren verschiedene Ebenen desselben Geschäfts und dürfen nicht zu einer bloßen Schenkung verkürzt werden.

#### Working finding / unresolved / hooks

- **WF-U2-0011:** Für Wüstendittersdorf ist die Kette `Lehen Witegos → Verkauf für 2½ Mark → Resignation an den Lehnsherrn → landgräfliche Appropriation an das Schleizer Haus` im Editionswortlaut ausdrücklich rekonstruierbar.
- **unresolved:** Bedeutung/Umfang der `serviciis diversimodis`; genaue Lage; aktuelle Signaturen; Verhältnis zur 1232 genannten Schleizer Filialkapelle Dittersdorf.
- **hook:** Die vollständige Kauf-/Auflassungskette ist ein diskriminierendes Comparandum für das bei Nr. 420 fehlende Verkäufer-/Vorbesitzglied.

#### Nutzerverständlicher Zugang

Hier lässt sich der Rechtsweg viel genauer erkennen als bei Mönchgrün: Witego von Kospoth verkaufte dem Schleizer Deutschordenshaus eine halbe Hufe mit Hof sowie Holz- und Weiderechten für zweieinhalb Mark. Weil er das Gut als Lehen vom Landgrafen hielt, gab er es zunächst an diesen zurück; der Landgraf übertrug es danach dem Orden als Eigentum. Genau dieser Zwischenschritt fehlt bei Nr. 420 und zeigt, wonach dort weitergesucht werden muss.

### EX-U2-0012 – weitere Wüstendittersdorfer Erwerbssequenz, Lampe Nr. 664–666

#### Provenienz / Fundstelle

- **date:** 21. und 24. Juni 1302.
- **printed / PDF pages:** 557–559 / PDF 577–579.
- **transmission:** Nr. 664 Original `Orig. No. 1706`; Nr. 665 Original `Orig. No. 1707`; Nr. 666 nur die im Apparat genannte Abschrift/Transsumptreferenz. Nicht unabhängig geprüft.

#### Historischer Wortlaut – zentrale Passagen

Nr. 664:

> `duos mansos ... in campis ville Dytherichsdorph ... quos iure feodali a dominis Ottone seniore et Ottone iuniore dictis de Bergowe habuimus et quos Theodericus Balistarius dictus de Trebene a nobis iure hereditario possedit, qui prefatos mansos fratribus domus Theuthonice in Slewiz vendidit pro quinque marcis et coram nobis libere resignavit.`

Nr. 665:

> `duos mansos ... quos ... Albertus et Heinricus de Brandenstein ... in feodo tenuerunt ... fratribus domus Theutonice in Slewicz ... concedimus, dotamus et appropriamus cum omni iure tam in pascuis, silvis, aquis, tam pratis quam agris.`

#### Source-explicit observations / Quellenfunktion

1. Theoderich Armbruster von Treben hatte die zwei Hufen erblich von den Brüdern von Brandenstein; diese hielten sie lehnsrechtlich von den Herren von Burgau.
2. Theoderich verkaufte für fünf Mark und resignierte vor den Brandensteinern; diese übertrugen ihre Rechte, anschließend bestätigten die Burgauer Herren die Appropriation.
3. Genannt werden Weiden, Wälder, Wasser, Wiesen und Äcker. Dies trägt einen Ressourcen-/Landschaftsbezug, aber keine konkrete Grenzrekonstruktion.

#### Working finding / unresolved / hooks

- **WF-U2-0012:** Auch 1302 erscheint der Schleizer Erwerb nicht als einstufige Schenkung, sondern als mehrgliedrige Kette aus erblich ausgeübtem Besitz, Lehen, Verkauf, Resignation und gestufter Zustimmung/Eigentumsübertragung.
- **unresolved:** genaue Rechtsbedeutung des erblichen Besitzes Theoderichs; Identität von `Trebene`; heutige Signaturen; Verhältnis zu Nr. 602/604.
- **hook:** Wüstendittersdorf als Mikroserie untersuchen; Personen `Brandenstein`, `Bergowe/Wergowe/Burgau`, `Trebene`, `Grevendorph`, `Oberniz` und die Schleizer Ordensbrüder weiterverfolgen.

#### Nutzerverständlicher Zugang

1302 kaufte der Orden in Wüstendittersdorf zwei weitere Hufen. Der Besitz war rechtlich über mehrere Ebenen verteilt: Theoderich Armbruster nutzte ihn erblich, die Brandensteiner hielten ihn als Lehen, darüber standen Herren von Burgau. Mehrere Urkunden machten den Übergang deshalb nacheinander rechtssicher. Das ist für die Rekonstruktion mittelalterlicher Herrschaft wichtiger als die verkürzte Aussage „der Orden bekam Land“.

### EX-U2-0013 – Wetterau: Verkäufer und Ressourcenrechte, Lampe Nr. 671

#### Provenienz / Fundstelle

- **date / place:** Wartburg, 18. Februar 1303.
- **printed / PDF pages:** 561–562 / PDF 581–582.
- **transmission:** laut Lampe Original `Orig. No. 1722`; Abschriften `A. 64, Bl. 81b–82b` und `B. 160, Heft 8, No. 10`; nicht unabhängig geprüft.

#### Historischer Wortlaut – zentrale Passage

> `fratres ordinis domus Theutonicorum in Slowicz villam, que vocatur Wederowe, a Gunderamo nostro castellano et ab Hermanno dicto Sengene civi nostro in Slowicz compararunt pro certa pecunie quantitate ... prefatam villam Wederowe ac novalia inter Thechsrot et nemus ... damus, dotamus et appropriamus cum omni iure, honore, utilitate et proprietate lignorum, aquarum et pascuorum.`

#### Source-explicit observations / Quellenfunktion

1. Anders als Nr. 420 nennt Nr. 671 zwei Verkäufer: den landgräflichen Kastellan Gunderam und den Schleizer Bürger Hermann Senge; die Summe bleibt unbeziffert.
2. Der Landgraf überträgt das bereits gekaufte Dorf und zusätzlich Neuland mit Holz-, Wasser- und Weiderechten.
3. Die Formulierung ähnelt strukturell Nr. 420 (`Kauf` vor `Appropriation`), bietet aber mehr Verkäufer- und Ressourcenkontext.

#### Working finding / unresolved / hooks

- **WF-U2-0013:** Wetterau 1303 liefert ein weiteres Schleizer Muster `vorausgehender Kauf → herrschaftliche Eigentumsübertragung`, diesmal mit ausdrücklich genannten Verkäufern und Landschaftsressourcen.
- **unresolved:** Lage von `Thechsrot/Techsrod`, Reichweite der Neulandgrenzen, Rechtsposition der Verkäufer und Verhältnis zur älteren Wetterauer Hufe Nr. 604.
- **hook:** Nr. 604, 670 und 671 als Wetterau-Serie kollationieren; Landschafts-/Wasser-/Weidebefund kontrolliert an #47 übergeben.

#### Nutzerverständlicher Zugang

1303 bestätigte Landgraf Albrecht einen bereits erfolgten Kauf des Dorfes Wetterau durch das Schleizer Deutschordenshaus. Hier nennt die Quelle die Verkäufer und fügt Neuland sowie Holz-, Wasser- und Weiderechte hinzu. Die Stelle ist deshalb ein gutes Vergleichsstück zu Mönchgrün und zugleich eine Spur für die Landschafts- und Ressourcengeschichte.

### Frühere Arnshaugk-Spuren – Discovery Notes, noch keine ausgewählten Exzerpte

- **Lampe Nr. 122, Druckseite 92 / PDF 112 (1252):** Otto von Lobdeburg, genannt von Arnshaugk (`Marnshoge`), erscheint als zustimmender Erbe in einem Bosauer Patronatsgeschäft; zwei Deutschordensangehörige sind Zeugen. Das belegt Ko-Präsenz in einem Rechtsakt, nicht bereits eine institutionelle Arnshaugk–Orden-Allianz.
- **Lampe Nr. 252, Druckseiten 197–198 / PDF 217–218 (1273):** Otto von Arnshaugk wird als `avunculus` des Burggrafen Otto von Kirchberg in einer Sicherung für einen Waldverkauf an das Deutschordenshaus Zwätzen genannt. Relevanz: explizite Verwandtschafts- und Bürgschafts-/Sicherungsbeziehung; kein Schleizer Erwerb.
- **Lampe Nr. 394, Druckseiten 331–332 / PDF 351–352 (angeblich 1284):** angebliche Übertragung der Straßberger Kapelle durch Otto von Arnshaugk; Lampe hält das Stück aus Überlieferungs-, Besitz-, Wortlaut- und Zeugenproblemen für eine Fälschung. Es darf nicht als gleichrangiger positiver Beleg verwendet werden.

### Kontrolltreffer Nr. 420

Nr. 420 wurde erst nach dem Band-/Registerlauf kontrolliert. PDF-Seiten 380–381 entsprechen Druckseiten 360–361 und bestätigen Inhalt, Apparat und Seitenübergang von `EX-U2-0009`. Der OCR-Textlayer enthält Fehler; maßgeblich blieb die Bildseite. Kein neues historisches Finding wurde allein aus dem Kontrolltreffer erzeugt.

## Pilotvergleich Durchlauf 1 ↔ Durchlauf 2

| Dimension | Durchlauf 1: THULB/IIIF, gezielt Nr. 420 | Durchlauf 2: bereitgestelltes Gesamt-PDF |
|---|---|---|
| Einstieg | Portal-, Metadaten-, Manifest- und Canvas-Auflösung vor Quellenlektüre | Datei sofort lokal durchsuchbar; kurzer technischer/Provenienzcheck nötig |
| Suchbreite | bekannte Einzelstelle; kein allgemeiner Bandlauf | Vollband-OCR + Namenweiser + Rücksprung in Quelltexte; mehrere zusätzliche Serien |
| Fundstelle | sehr starke persistente Canvas-/IIIF-Referenz | stabile Druck-/PDF-Seitenzuordnung, aber temporärer Uploadpfad |
| Textqualität | visuell zuverlässig, automatisierte Vollbandsuche umständlicher | OCR sehr effizient für Discovery, aber fehlerhaft und stets bildseitig zu kontrollieren |
| Kontext | zwei Zielseiten | zusammenhängender Band, Register, Apparat, Vor-/Nachstücke und Berichtigungen verfügbar |
| Arbeits-/Tokeneffizienz | hoher Aufwand bis zur einen Stelle | deutlich mehr fachlicher Ertrag pro Zugriff; breite Trefferlisten müssen diszipliniert eingegrenzt werden |
| Restartability | institutioneller PID/URN/IIIF-Zugang | wissenschaftlicher State restartbar; konkrete Upload-Datei noch nicht dauerhaft verfügbar |

**Qualitative Disposition:** Für breit angelegte Banderschließung ist ein lokal verfügbares, textdurchsuchbares Gesamt-PDF der effizientere Arbeitszugang. Für dauerhafte Zitierbarkeit, Rechteklärung und seitenexakte Wiederauffindbarkeit bleibt die institutionelle THULB-Instanz überlegen. Der robuste Standardweg ist daher kein Entweder-oder, sondern `lokale PDF-Discovery und Kontextarbeit → institutionelle Instanz/Identifier für kanonische Identität und tragende Fundstellen`, sofern beide verfügbar sind.

**System-/Workflow-Evidence:** Die verständliche deutsche Sicht kann aus demselben Source-/Excerpt-/Finding-State abgeleitet werden, ohne eine zweite Forschungswahrheit zu schaffen. Der Pilot stärkt bestehende `REQ-UX-003`, `REQ-SRC-001..004`, `REQ-STATE-003` und `REQ-RSCH-001..003`; er promotet kein neues Requirement und keine Architektur.
