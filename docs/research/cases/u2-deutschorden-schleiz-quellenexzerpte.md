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
