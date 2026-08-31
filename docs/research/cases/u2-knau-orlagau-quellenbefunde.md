# U2 Live Research – Knau/Orlagau: mittelalterliche Quellen-, Herrschafts- und Siedlungsbeziehungen

**Status:** `working-research / preliminary / source-collation-in-progress`  
**Work Owner:** #46  
**Methodisches Protokoll:** #45  
**Use Case:** U2 aus #29/#30  
**Stand:** 2026-08-31

---

## 1. Zweck

Dieses Artefakt hält den **substanziellen, versionierten Forschungsstand** der laufenden Quellenstudie zu Knau bei Neustadt an der Orla und seinem hoch-/spätmittelalterlichen Beziehungsraum fest.

Es verfolgt zwei gleichzeitig getrennt zu haltende Ziele:

1. **historische Forschung:** konkrete quellenkritische Befunde zu Orten, Personen, Herrschaften, Institutionen und Siedlungsentwicklung;
2. **Histo-Orla-Lernfall:** reale Friktionen, Failure Modes und Capability-/Requirement-Candidates aus einem anspruchsvollen mittelalterlichen Quellenproblem sichtbar machen.

Historische Findings sind **keine Requirements**. Requirement Candidates werden erst in #41/#42 gegen weitere Use Cases, SOTA und Risiken geprüft.

---

## 2. Forschungsfragen

1. Was ist die früheste quellenkritisch gesicherte Nennung von **Knau bei Neustadt/Orla**?
2. Was steckt hinter der in moderner Literatur wiederholten Form **`Knauwe villa`** und dem Datierungskonflikt **1374 vs. 1378**?
3. Welche mittelalterlichen Formen `Knau`, `Knewe`, `Knawe`, `Knauwe`, `Kneben`, `Knewer` gehören zu welchem Ort bzw. zu welchen Personen?
4. Gibt es einen direkten Zusammenhang zwischen **Knau nördlich Altenburgs / de Knewe** und **Knau bei Neustadt/Orla**?
5. Was ist im Verhältnis **Stange ↔ Knewe/Knau** tatsächlich Quelle, editorische Ergänzung oder spätere genealogische Interpretation?
6. Wie sind **Lobdeburg-Arnshaugk, Schleiz, Deutscher Orden, Naumburg und Saalfeld** mit dem Untersuchungsraum verbunden?
7. Welche Aussagen tragen Urkunde, Regest, Editionsregister, Archäologie, Ortsname und Besitzgeschichte jeweils zur **Siedlungschronologie**?
8. Welche Nachbarorte und Gewässer-/Flurnamen erschließen den Raum indirekt, auch wenn `Knau` selbst nicht genannt wird?

---

## 3. Führende Fachdomänen und Qualitätskontrolle

### Führend

- Diplomatik / Quellenkunde / Editionswissenschaft
- Archivistik / Provenienz / Überlieferungsgeschichte
- Mediävistik / Landes-, Herrschafts- und Verfassungsgeschichte
- Adels-/Ministerialitäts-/Lehnsforschung
- historische Philologie / Onomastik / Toponymie

### Kontrollierend

- Siedlungs-/Mittelalterarchäologie
- historische Geographie / Regionalgeschichte
- Kirchengeschichte bei Diözesan-/Klosterfragen

### Mindestchecks nach #45

- **Domain fit:** trägt die aktivierte Fachdomäne die Frage?
- **Evidence fit:** trägt die konkrete Quelle/Edition die Aussage?
- **Inference fit:** ist der Schluss zulässig oder nur Hypothese?
- **Terminology fit:** historische, editorische, archivische und moderne Begriffe getrennt?
- **Provenance fit:** konkrete Edition/Fundstelle/Überlieferungsstufe nachvollziehbar?
- **Falsification/challenge:** welche Quelle oder Gegenhypothese könnte den Befund ändern?

---

## 4. Epistemische Ebenen

Für diesen Fall zwingend getrennt:

```text
historische Urkunde / materieller Befund
→ konkrete digitale Instanz / Scan
→ Edition / Regest / OCR / Transkription
→ editorische Ergänzung / Registeridentifikation
→ beobachteter Befund
→ Normalisierung / Orts- oder Personenidentifikation
→ Claim
→ historische Interpretation
→ transdisziplinäre Synthese
```

Spezielle Schutzregeln:

- `Regest` ist nicht die Urkunde.
- Ein Editionsregister kann eine Ortsidentifikation liefern, ist aber nicht historischer Wortlaut.
- Eckige Klammern einer Edition/Forschung können moderne Ergänzungen markieren.
- Gleichnamige oder ähnlich geschriebene Orte werden nicht ohne positive Identifikation zusammengeführt.
- `nicht gefunden` bedeutet nur innerhalb einer dokumentierten Search Boundary etwas.
- `Ersterwähnung` ist nicht automatisch `Gründungsdatum`.

---

## 5. Aktueller Quellen-/Corpus-Stand

### 5.1 Im laufenden Arbeitskontext verfügbare bzw. bereits herangezogene Editionen

| Kürzel | Werk / Material | Zeitraum / Funktion | Status im Live-Fall |
|---|---|---|---|
| NHUB II | *Urkundenbuch des Hochstifts Naumburg*, Teil 2 | 1207–1304 | vom Research Owner als Volltext bereitgestellt; systematische Varianten-/Netzwerkauswertung läuft |
| Lehnbuch 1349/50 | *Lehnbuch Friedrichs des Strengen* | 1349/50 | bildbasierte Quelle/Edition; für Besitz-/Lehnsstrukturen vorgesehen |
| CDS 1381–1395 | *Codex diplomaticus Saxoniae* | 1381–1395 | spätere Kontrollschicht für Kontinuitäten / wettinische Herrschaftsbezüge |
| DO-UB I | Karl H. Lampe (Hg.), *Urkundenbuch der Deutschordensballei Thüringen*, Bd. I | bis 1310 | zentrale bereits kontrollierte Edition für Altenburg/Schleiz/Deutschen Orden |
| Dobenecker | *Regesta diplomatica necnon epistolaria historiae Thuringiae* | Mittelalter | Leitapparat / Varianten- und Regestensuche; weitere systematische Auswertung offen |
| Schmidt | *Urkundenbuch der Vögte von Weida, Gera und Plauen* | Hoch-/Spätmittelalter | wichtig für Vogtland/Schleiz/Arnshaugk-Verflechtungen; systematische Kollation offen |
| Perlbach 1902 | Max Perlbach, Studie zu Stange | ältere Forschung / Regestenapparat | wichtig für 1315er `Heinrich [Stange] von Knewe`; editorische Ergänzung kritisch zu behandeln |

**Hinweis zur Restartability:** Die drei vom Research Owner im Chat bereitgestellten Volltexte sind noch **nicht als Dateien im Repository abgelegt**. Dieses Artefakt dokumentiert deshalb mindestens ihre bibliographische Identität und ihren Verwendungszweck. Eine spätere technische Kopplung an Zotero/Attachments ist Gegenstand der Architekturphase, nicht Voraussetzung für den aktuellen Working Research State.

### 5.2 Noch nicht hinreichend gesicherte Kernquelle

Die Primär-/Editionsquelle hinter der modernen Angabe **`Knauwe villa` 1374/1378 als Klosterhof der Benediktinerabtei Saalfeld** ist noch nicht so identifiziert, dass Datum, Aussteller, Rechtsgeschäft, Original-/Kopiarstatus und heutige Signatur belastbar angegeben werden können.

Das ist aktuell der wichtigste einzelne Source-Resolution-Task.

---

## 6. Working Findings

### Evidenzreife

- **A – edition-/urkundenbasiert stark:** konkrete wissenschaftliche Edition/Fundstelle; Überlieferungsstatus beschrieben.
- **B – gut belegt, aber indirekt/editorisch identifiziert:** z. B. Herkunftsname + Editionsregister.
- **C – ältere Forschung / Sekundärüberlieferung:** Primärstück noch zu kollationieren.
- **D – offen / widersprüchlich:** Kernquelle oder Identifikation noch nicht gesichert.

Diese Buchstaben sind lokale Arbeitsmarker für diesen Fall, keine universelle Histo-Orla-Evidenzskala.

---

### F-U2-001 – Altenburger `Knewe/Kneben/Knewer` bilden einen eigenständigen, dicht belegten Überlieferungskomplex

**Finding:** Im 13. Jahrhundert treten im Altenburger/Pleißenland-Kontext mehrfach `Knewer`, `Knewe` und `Kneben` auf. Die wissenschaftliche Deutschordensedition führt die einschlägigen Formen im Register unter **Knau, Dorf nördlich Altenburg** zusammen.

**Konkrete bisher kontrollierte Belege:**

| Datum | Form / Person | Fundstelle | Status / Aussage |
|---|---|---|---|
| 3. Mai 1289 | `Gothfridus dictus Knewer civis in Aldenburc` | Lampe, DO-UB I, Nr. 461; historisch HStA Dresden `Orig. Nr. 1260` | A/B – Person sicher; Ortsbindung über editorisches Register |
| 25. März 1291 | Gottfried Knewer | Lampe, DO-UB I, Nr. 496 | A/B – erneutes Altenburger Milieu |
| 20. Mai 1291 | Gottfried Knewer | Lampe, DO-UB I, Nr. 499 | A/B – erneutes Altenburger Milieu |
| 1. Nov. 1291 | `dominus Cunradus de Knewe` | ältere Edition einer Altenburger Urkunde; Dresdner Original dort angegeben | B/C – Person belegt, heutige moderne Archivsignatur noch zu sichern |
| 13. März 1294 | `Conrado de Kneben, Bernardo de Kneben, militibus` | Lampe, DO-UB I, Nr. 552; historisch HStA Dresden `Orig. Nr. 1452` | A – Ritter im Altenburger Umfeld; Ortsidentifikation im Editionsregister |

**Was dies trägt:** starke Verankerung der Namensformen im Altenburger/Pleißenland-Komplex.

**Was dies nicht trägt:** keine direkte Verbindung zu Knau bei Neustadt/Orla.

**Falsifikation / Challenge:** ein positiver, quellenkritisch gesicherter Besitz-, Herkunfts-, Lehns- oder genealogischer Beleg, der dieselben Personen/Familien mit dem Orla-Knau verbindet.

---

### F-U2-002 – Altenburger Knau und Orla-Knau dürfen derzeit nicht zusammengeführt werden

**Finding:** Der positive Altenburger Quellenkomplex ist deutlich; für Orla-Knau ist die früheste häufig genannte Nennung dagegen die noch nicht aufgelöste `Knauwe villa` 1374/1378. Ein hochmittelalterlicher direkter Zusammenhang wurde bislang nicht nachgewiesen.

**Status:** B/D – starke Evidenz für die getrennten Überlieferungslagen; offene Frage, ob spätere Quellen eine Beziehung herstellen.

**Methodische Konsequenz:** Orts-/Personen-Entity-Resolution muss nicht nur Zeichenähnlichkeit, sondern **Zeit, Raum, Herrschaftskontext, Zeugen-/Besitznetz und editorische Identifikation** berücksichtigen.

---

### F-U2-003 – `Stange ↔ Knewe` ist als Netzwerkbefund stärker als als genealogischer Befund

**Finding:** Die Familie Stange ist im Altenburger/Deutschordensmilieu sicher greifbar. 1259 erscheint `dominus Ludewicus Stango`; Heinrich Stange tritt 1294 als Ritter auf und ist in einer Serie späterer Belege fassbar.

Für 1315 druckt Max Perlbach sinngemäß **Ludwig Stango und Heinrich `[Stange] von Knewe`** als Altenburger Burgmannen. Entscheidend ist: **`[Stange]` ist editorisch ergänzt**. Der Eintrag beweist deshalb nicht aus sich heraus einen historischen zusammengesetzten Namen `Stange von Knewe`.

**Status:**

- Stange ↔ Altenburg: A/B.
- Knewe ↔ Altenburg: A/B.
- Ko-Präsenz/gleiches Burgmannenmilieu: B/C.
- genealogische Identität Stange ↔ Knewe: D / nicht bewiesen.

**Methodische Konsequenz:** editorische Ergänzungen müssen maschinen- und menschenlesbar als eigene Evidenzebene erhalten bleiben. Eine Normalisierung darf sie nicht in historischen Quellentext zurückschreiben.

---

### F-U2-004 – Lobdeburg-Arnshaugk ↔ Deutscher Orden/Schleiz ist ein positiver regionaler Herrschaftsbefund

**Finding:** Die Deutschordensüberlieferung zeigt reale Verflechtungen zwischen Lobdeburg-Arnshaugk, Schleiz und dem Deutschen Orden.

**Bisherige Schlüsselpunkte:**

- **1232:** Urkunde des Naumburger Bischofs Engelhard zur Pfarrei Schleiz; später 1310 vidimiert. Sie belegt kirchenrechtliche/rechtliche Verbindungen Schleiz ↔ Naumburg und gelangte in den Deutschordensüberlieferungszusammenhang.
- **5. September 1285:** Otto IV. von Lobdeburg, genannt von Arnshaugk, und sein Sohn Hartmann XI. eignen dem Deutschen Haus zu Schleiz das Dorf Mönchgrün zu.
- **5. Dezember 1297:** Witego von Kospoth verkauft dem Schleizer Komtur Heinrich von Braunschweig eine halbe Hufe in Wüstendittersdorf.

**Status:** A/B für die regionalen Beziehungen; die genaue Einordnung in Herrschaftsbildung, Eigentum/Lehen und Ordensausbau wird weiter untersucht.

**Was dies nicht trägt:** noch keine direkte Beziehung dieser Stücke zu Knau/Orla.

---

### F-U2-005 – Homonyme sind ein bereits real beobachteter Failure Mode

**Finding:** Mehrere maschinell plausible Treffer wurden verworfen, weil die editorische/topographische Identifikation nicht zum Untersuchungsraum passt.

**Beispiele:**

- `Bucha` im kontrollierten Deutschordensband liegt südöstlich von Wiehe und ist nicht automatisch Bucha bei Knau.
- `Plottendorf` im Altenburger Kontext ist nicht `Plothen`.
- `Lintbach/Lindbach` im Altenburger Besitzkomplex ist nicht ohne positiven Beleg `Linda/Lindenbach` im Orla-Raum.
- ähnlich geschriebene Formen wie `Grifendorf` dürfen nicht allein wegen String-Nähe mit `Gräfendorf` gleichgesetzt werden.

**Status:** A/B als methodischer Befund aus dem bereits kontrollierten Corpus.

**Systemrelevanz:** False Merge ist für historische Orts-/Personenauflösung ein höheres Risiko als ein zunächst offen gebliebener Kandidat.

---

### F-U2-006 – Corpus-Negativbefunde sind nur mit Suchgrenze aussagekräftig

**Finding:** Im bereits kontrollierten DO-UB-I-Corpus ergaben moderne Formen für mehrere Zielorte keinen sicheren Treffer, u. a. Plothen/Plote, Ranis, Wernburg, Moderwitz, Dreba, Weira, Linda, Külmla, Tausa und Steinbrücken. Diese Beobachtung ist **keine Aussage über mittelalterliche Nichtexistenz**.

**Status:** B als Corpus-Negativbefund.

**Search Boundary:** ein konkreter Editionsband / dessen Volltext und Register, teilweise zunächst mit modernen Suchformen; historische Varianten und andere Corpora sind ausdrücklich noch offen.

**Konsequenz:** Negative Findings müssen Corpus, Suchvarianten, Zeitraum und Zugriffsgrenze mitführen.

---

### F-U2-007 – `Knauwe villa` 1374/1378 ist ein Discrepancy-Problem, kein Datum zum Wegentscheiden

**Finding:** Moderne Darstellungen reproduzieren `Knauwe villa` als Saalfelder Klosterhof, nennen aber 1374 bzw. 1378. Die zugrunde liegende Primär-/Editionsquelle ist im aktuellen Working State noch nicht hinreichend bestimmt.

**Status:** D.

**Zulässige Aussage:** Es existiert eine moderne Überlieferungstradition, die eine `Knauwe villa` im Saalfelder Klosterzusammenhang nennt; Datum und diplomatische Grundlage sind noch zu sichern.

**Unzulässige Aussage:** `Knau wurde sicher 1374` oder `sicher 1378 gegründet/erstmals erwähnt`, solange die Quelle nicht aufgelöst ist.

**Nächster diskriminierender Schritt:** Saalfelder Kloster-/Herrschaftsurkunden und Kopiare 1370–1380 einschließlich Varianten `Knauwe/Knawe/Knaw/Knewe` systematisch prüfen und den Sekundärzitierpfad der modernen Angaben rückwärts verfolgen.

---

### F-U2-008 – Schriftliche Ersterwähnung und Siedlungsbeginn sind methodisch unabhängige Achsen

**Finding:** Der gegenwärtige dokumentarische Stand zu Orla-Knau ist deutlich später als archäologische Hinweise, die für den Rittergutsbereich teilweise ins 12. Jahrhundert eingeordnet werden. Diese Ebenen dürfen weder gegenseitig ersetzt noch unkritisch harmonisiert werden.

**Status:** C/D, weil der archäologische Befund in dieser Forschungsrunde noch nicht anhand des vollständigen Grabungs-/Fundkontexts kollationiert wurde.

**Konsequenz:** Für eine Siedlungschronologie sind mindestens getrennt zu führen:

- frühester sicherer **Namenbeleg**,
- frühester sicherer **schriftlicher Orts-/Besitzbeleg**,
- **archäologischer Nutzungs-/Siedlungsbefund**,
- **Bau-/Befundchronologie**,
- **Herrschafts-/Besitzkontinuität**.

---

## 7. Varianten- und Entity-Matrix v0.1

| Form | Typ | Arbeitsidentifikation | Sicherheit | Kommentar |
|---|---|---|---|---|
| Knewer / Knewerer | Personen-/Herkunftsname | Altenburg / Knau nördlich Altenburg | hoch über Lampe-Register | nicht auf Orla-Knau übertragen |
| Kneben | Herkunftsname von Rittern | Altenburg / Knau nördlich Altenburg | hoch über Lampe-Register | 1294 Konrad/Bernhard |
| Knewe | Herkunftsname | Altenburger Raum | hoch für Person; Ortsidentifikation weiter kontrollieren | 1291 Conradus de Knewe |
| Knauwe villa | Orts-/Gutsbezeichnung | wahrscheinlich Knau bei Neustadt/Orla | modern tradiert, Primärquelle offen | 1374/1378 aufzulösen |
| Knau | moderner Ortsname | mindestens zwei relevante Orte | eindeutig nur mit Kontext | Altenburg vs. Neustadt/Orla strikt trennen |
| Bucha | Ortsname | mehrere Homonyme | offen je Treffer | nicht automatisch Bucha bei Knau |
| Plottendorf | Ortsname | Altenburger Raum | positiv identifiziert | nicht Plothen |
| Plothen / Plote | Orts-/Gewässerkomplex | Orla/Vogtland-Zielraum | Suchvarianten ausbauen | `Plote/Plottenbach` etc. prüfen |
| Lintbach/Lindbach | Orts-/Gewässername | Altenburger Kontext im DO-Corpus | dort positiv | nicht automatisch Linda/Lindenbach Orla |

### Offene Variantenliste

Systematisch auszubauen für:

`Dittersdorf, Plothen, Plote/Plottenbach, Schleiz, Saalfeld, Ranis, Wernburg, Moderwitz, Meilitz, Posen, Bucha, Ziegenrück, Gräfendorf, Volkmannsdorf, Schöndorf, Külmla, Tausa, Dreba/Wenigendreba/Drebabach/Drebe, Weira, Linda/Lindenbach, Kleina, Steinbrücken`.

Nicht nur moderne Formen suchen; Ableitung aus Ortsnamenbüchern, Editionsregistern, Latein und regionaler Schreibpraxis ist eigener Arbeitsschritt.

---

## 8. Beziehungs-/Claim-Matrix v0.1

| Relation / Claim | Arbeitsstatus | Evidenzlage |
|---|---|---|
| Knewe/Kneben/Knewer ↔ Knau nördlich Altenburg | stark belegt | editorisches Register + mehrere Urkundenpersonen |
| Stange ↔ Altenburg | stark belegt | mehrere Urkunden-/Regestenbelege |
| Stange ↔ Deutscher Orden Altenburg | stark belegt | gemeinsames Urkundenmilieu |
| Stange ↔ Knewe genealogisch | **nicht bewiesen** | 1315er `[Stange]` editorische Ergänzung; Ko-Präsenz reicht nicht |
| Knewe/Knau Altenburg ↔ Knau/Orla | **kein positiver Beleg im bisherigen Stand** | getrennte positive Überlieferungskomplexe |
| Lobdeburg-Arnshaugk ↔ Deutscher Orden Schleiz | positiv belegt | u. a. 1285 Mönchgrün |
| Schleiz ↔ Naumburg | positiv belegt | 1232/1310 Pfarr-/Vidimus-Komplex |
| Saalfelder Benediktinerkloster ↔ `Knauwe villa` | plausibler moderner Traditionskern, Quelle offen | 1374/1378 zu kollationieren |
| späte Ersterwähnung ↔ späte Besiedlung | **unzulässige Gleichsetzung** | unterschiedliche Evidenztypen |

---

## 9. Source-Resolution Queue

### P0 – höchste diskriminierende Wirkung

1. **`Knauwe villa` 1374/1378**
   - Provenienz: Benediktinerkloster / Herrschaft Saalfeld
   - Suchfenster: 1370–1380, danach Zitierpfad rückwärts
   - Varianten: `Knauwe, Knawe, Knaw, Knewe`, ggf. lateinische Ortskontexte
   - Zieloutput: Datum, Aussteller, Empfänger, Rechtsgeschäft, Wortlaut, Original/Kopie/Kopiar, Edition/Regest, heutige Signatur.

2. **1315 Knewe/Stange**
   - zugrunde liegende Urkunde/Abschrift hinter Perlbach/Huth/Liebe sichern
   - historischer Wortlaut vs. `[Stange]`-Ergänzung exakt trennen.

3. **1291 `Conradus de Knewe`**
   - moderne Edition/Archivkonkordanz und heutige Dresdner Signatur bestimmen.

4. **Bosauer / ältere Altenburg-Nennungen**
   - angebliche frühe Formen (`Chewe`, `Knowe?`) am tatsächlichen Überlieferungsträger/Edition prüfen; keine Ortschronik als Endbeleg.

### P1 – regionales Netz

5. Naumburger UB / Schmidt / Dobenecker systematisch für Schleiz–Arnshaugk–Ziegenrück–Ranis–Weira–Dreba–Plothen und Nachbarorte abarbeiten.
6. Zeugenlisten nicht nur auf Hauptakteure, sondern auf wiederkehrende Personencluster auswerten.
7. Lehnbuch 1349/50 auf Besitzgruppen, Lehnsherren/-nehmer und Ortscluster im Orla-/Vogtlandraum prüfen.
8. CDS 1381–1395 als spätere Kontrollschicht für fortwirkende Besitz-/Herrschaftsstrukturen nutzen.

---

## 10. Capability-/Quality-/Requirement-Candidates aus dem Live-Fall

Diese Kandidaten sind **noch nicht promoted**. Sie gehen erst über #41/#42.

### RC-U2-01 – Source Layer Preservation

**Beobachteter Pain:** `Heinrich [Stange] von Knewe` kann bei flacher Textnormalisierung fälschlich als historischer Originalname erscheinen.

**Candidate:** Das System muss historischen Wortlaut, editorische Ergänzung, Normalisierung und Interpretation getrennt halten und sichtbar machen können.

**Quality test:** Ein Reviewer kann für jedes Token/Segment erkennen, ob es Quelle, Edition oder spätere Ergänzung ist, soweit die Edition diese Information bietet.

---

### RC-U2-02 – Contextual Entity Resolution mit False-Merge-Schutz

**Beobachteter Pain:** Knau/Altenburg vs. Knau/Orla sowie Bucha/Plottendorf/Lintbach zeigen reale Homonym-/String-Similarity-Fallen.

**Candidate:** Orts-/Personenkandidaten dürfen nicht allein über String-/Embedding-Ähnlichkeit promoted werden; Zeit, Raum, Quelle, Herrschafts-/Beziehungs- und editorische Identifikation müssen als prüfbare Kontextmerkmale einfließen.

**Quality test:** bekannte Homonyme werden nicht automatisch zusammengeführt; unsichere Fälle bleiben Kandidaten.

---

### RC-U2-03 – Variant Search über mehrere Terminologieebenen

**Beobachteter Pain:** moderne Ortsnamen allein liefern unzureichenden Recall.

**Candidate:** Suchläufe müssen kontrolliert historische Schreibformen, editorische Normalformen, lateinische/regionale Varianten sowie ggf. Personen-Herkunftsnamen einbeziehen können, ohne diese als semantisch identisch auszugeben.

**Quality test:** Query Log zeigt, welche Varianten warum verwendet wurden und welche Treffer jede Variante erzeugte.

---

### RC-U2-04 – Witness-/Context-Network Retrieval

**Beobachteter Pain:** Ein relevanter Ort/Person kann nur in Zeugenlisten oder über Mitzeugen sichtbar werden; Regest/Hauptinhalt allein reicht nicht.

**Candidate:** Recherche muss Zeugenreihen, Mitakteure und wiederkehrende Kontextcluster erschließen können, ohne Ko-Präsenz automatisch als soziale/genealogische Beziehung zu interpretieren.

**Quality test:** bekannte Knewe-/Stange-Belege werden als Ko-Präsenz findbar, aber nicht automatisch als Genealogie promoted.

---

### RC-U2-05 – Corpus-bounded Negative Findings

**Beobachteter Pain:** `kein Treffer` wird leicht zu `Ort existierte nicht` überdehnt.

**Candidate:** Negative Findings brauchen maschinen-/menschenlesbare Search Boundaries: Corpus, Zeitraum, Suchformen, Suchfelder, Zugang/Indexstatus.

**Quality test:** Kein Negativclaim kann ohne dokumentierte Boundary den Status `working finding` oder höher erhalten.

---

### RC-U2-06 – Discrepancy State statt erzwungener Harmonisierung

**Beobachteter Pain:** 1374/1378 ist aktuell nicht auflösbar; eine Software könnte eine Zahl wählen oder Mehrheitsnennung als Wahrheit behandeln.

**Candidate:** widersprüchliche Datierungen/Identifikationen müssen als unresolved discrepancy mit konkurrierenden Provenienzpfaden persistierbar sein.

**Quality test:** beide Datierungen bleiben mit Quelle/Status sichtbar, bis diskriminierende Evidenz vorliegt.

---

### RC-U2-07 – Multi-Evidence Settlement Chronology

**Beobachteter Pain:** schriftliche Ersterwähnung, archäologischer Befund, Bauchronologie und Ortsname haben unterschiedliche Aussagekraft.

**Candidate:** Siedlungsfragen müssen mehrere Evidenzachsen getrennt darstellen können; keine implizite Gleichung `first mention = foundation`.

**Quality test:** eine Siedlungs-Timeline kann parallele Zeitachsen/Belegtypen anzeigen und deren Aussagegrenzen beschreiben.

---

### RC-U2-08 – Bibliographic/Archival Identity of User-Supplied Corpus

**Beobachteter Pain:** im Chat bereitgestellte Volltexte sind für die laufende Forschung nutzbar, aber ein späterer Bearbeiter muss bibliographisch erkennen können, welche konkrete Edition gemeint war.

**Candidate:** jedes verwendete Nutzer-Dokument braucht mindestens stabile bibliographische/archivalische Identität plus Status der tatsächlich inspizierten Instanz; technische Attachment-Kopplung bleibt Architekturfrage.

**Quality test:** Restartability ohne Chat ist für die verwendete Quellenbasis möglich.

---

## 11. Risiken / Failure Modes aus diesem Fall

| Risiko | Beispiel | Schutzmaßnahme |
|---|---|---|
| False merge | Knau Altenburg = Knau Orla | Candidate State + Kontextprüfung |
| Source laundering | moderne Ortsseite → „Primärbeleg 1378“ | Evidenzklasse + Rückverfolgung zur Edition/Urkunde |
| Editorial laundering | `[Stange]` wird historischer Name | Layer Preservation |
| Search-form bias | nur moderne Ortsform gesucht | Varianten-/Terminologie-Layer |
| Regest bias | Zeugenname im Regest fehlt | Volltext-/Zeugenlisten-Retrieval |
| false corroboration | mehrere Seiten kopieren dieselbe Datierung | Source Dependence prüfen |
| negative overclaim | kein Treffer im DO-UB → Ort existiert nicht | Search Boundary |
| first-mention fallacy | 1378 = Dorfgründung | getrennte Evidenzachsen |
| network overclaim | gemeinsame Zeugenreihe = Familie | Relationship Promotion nur mit Evidenz |

---

## 12. Search Boundary – aktueller Stand

### Bereits vergleichsweise intensiv bearbeitet

- Deutschordensüberlieferung Altenburg/Schleiz über DO-UB I;
- Knau/Knewe/Kneben/Knewer im Altenburger Kontext;
- erste Stange-Regesten-/Forschungsspur;
- erste moderne Spur `Knauwe villa` 1374/1378;
- ausgewählte regionale Bezüge Schleiz / Arnshaugk / Mönchgrün / Wüstendittersdorf.

### Noch nicht vollständig bearbeitet

- alle vom Research Owner bereitgestellten Volltexte systematisch mit kompletter Variantenliste;
- Dobenecker vollständig über relevante Bände/Varianten;
- Schmidt vollständig;
- Lehnbuch 1349/50 bildseitenbasiert;
- CDS 1381–1395 systematisch;
- Saalfelder Kloster-/Herrschaftsüberlieferung 1370–1380;
- Archive/Kopiare außerhalb der gedruckten Editionen;
- archäologische Primär-/Grabungsdokumentation zu Knau/Orla;
- Ortsnamenbücher für vollständige Variantenmatrix.

### Bedeutung

Alle derzeitigen `kein Beleg`-Aussagen sind **auf diese Boundary beschränkt**. Es wird keine vollständige mittelalterliche Überlieferung für den Raum behauptet.

---

## 13. Sättigungsstatus

`not saturated / active source resolution`

Für eine v0.1-Synthese ist die Trennung der Altenburger und Orlaer Überlieferung bereits ein tragfähiger Working State. Nicht ausreichend gesättigt sind insbesondere:

- Primärquelle `Knauwe villa`;
- Stange/Knewe 1315 auf Original-/Vorlagenebene;
- komplette regionale Varianten-/Nachbarortmatrix;
- Siedlungschronologie aus unabhängigen archäologischen Quellen.

Der nächste Suchschritt hat weiterhin hohe diskriminierende Wirkung; deshalb ist kein Stop nach #45 gerechtfertigt.

---

## 14. Nächste Fortschreibung

Bei jeder substanziellen Recherche-Runde:

1. Source Ledger erweitern;
2. Finding mit genauer Fundstelle + Evidence Layer ergänzen;
3. Varianten-/Entity-Matrix korrigieren;
4. Claims/Relations nur nach Evidenz promoten;
5. Negativbefunde mit Boundary erfassen;
6. Discrepancies offen halten oder mit diskriminierender Evidenz auflösen;
7. neue Systemimplikationen zunächst als Candidate markieren;
8. #46 nur mit Kurzsynthese/Status fortschreiben – Vollinhalt bleibt hier.
