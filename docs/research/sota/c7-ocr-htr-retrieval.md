# C7 – OCR/HTR, historischer Volltext, Retrieval und fundstellenfähige Suche

**Work Owner:** #35  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** OCR/HTR/Digital Humanities, Document Processing, Information Retrieval, historische Sprachverarbeitung.  
**Controlling competencies:** Paläographie, Editionswissenschaft, RDM/Provenienz, Quality Engineering, RSE; jeweilige Fachdomäne für historische Begriffe/Namen.

## 1. Research Questions

RQ-C7-01 bis RQ-C7-05:

1. Welche aktuellen OCR-/HTR-Verfahren eignen sich nach Materialtyp?
2. Welche Repräsentation erhält Seite/Folio/Layout und Original↔Derivat-Rückführung?
3. Welche auditierbare historische Retrieval-Baseline ist angemessen?
4. Wann dürfen Semantic Search / Embeddings / RAG additiv zugelassen werden?
5. Welche Rolle kann Zotero im persönlichen Corpus U4 sinnvoll übernehmen?

## 2. Search Scope / Boundary

Geprüft wurden:

- aktuelle Dokumentationen etablierter Open-/Research-OCR/HTR-Werkzeuge und -Workflows;
- OCR-D-Konventionen für METS/PAGE, Seiten-/Bild-/Derivatbezug;
- aktuelle Zotero-Suche, Full-Text- und Local-/Web-API-Funktionen (Stand Juni/Juli 2026);
- etablierte historische IR-Literatur zu OCR-Fehlern, historischen Schreibvarianten, Fuzzy Matching und Query Expansion;
- aktuelle Forschung (2026) zu OCR-robusten Embeddings/semantic retrieval;
- U4 als Hauptworkflow, U1–U3 als fachliche Stressfälle.

Nicht beansprucht wird ein Benchmark auf dem späteren persönlichen Corpus; dieser ist Requirement/Evaluation für die Umsetzungsphase.

## 3. Inspected sources

### OCR / PAGE / Derivative Provenance

- OCR-D, **Conventions for PAGE**: https://ocr-d.de/en/spec/page
- OCR-D, **Requirements on handling METS/PAGE**: https://ocr-d.de/mets/
- OCR-D, **Workflow Guide**: https://ocr-d.de/en/workflows
- OCR-D, **Example METS**: https://ocr-d.de/en/example_mets.html
- OCR4all, **Workflow / Evaluation**: https://www.ocr4all.org/guide/user-guide/workflow
- OCR4all, **Scan and Image Preparation**: https://www.ocr4all.org/guide/user-guide/scan-preparation
- Kraken documentation, **Advanced Usage / standardized outputs**: https://kraken.re/5.0.0/advanced.html
- Kraken current documentation/API: https://kraken.re/6.0.0/tutorials/api.html
- Transkribus Metagrapho API: https://transkribus.eu/processing/swagger/

### Zotero current functionality

- Zotero, **Searching / Full-Text Indexing**, updated 2026-06-08: https://www.zotero.org/support/searching
- Zotero, **Local API**, updated 2026-07-29: https://www.zotero.org/support/dev/web_api/v3/local_api
- Zotero, **Web API Full-Text Content**, updated 2026-07-29: https://www.zotero.org/support/dev/web_api/v3/fulltext_content
- Zotero, **Web API v3 Basics**: https://www.zotero.org/support/dev/web_api/v3/basics

### Historical IR / OCR noise

- Gotscharek et al., **Towards information retrieval on historical document collections: The role of matching procedures and special lexica** (IJDAR 2011), DOI 10.1007/s10032-010-0132-6.
- Gotscharek et al., **Enabling information retrieval on historical document collections** (2009), DOI 10.1145/1568296.1568309.
- Hauser/Schulz, **Unsupervised Learning of Edit Distance Weights for Retrieving Historical Spelling Variations**.
- Reffle/Ringlstetter, **Unsupervised profiling of OCRed historical documents** (Pattern Recognition 2013), DOI 10.1016/j.patcog.2012.10.002.
- Järvelin et al., **Information retrieval from historical newspaper collections in highly inflectional languages: A query expansion approach** (JASIST 2015), DOI 10.1002/asi.23379.
- Boros et al., **Alleviating Digitization Errors in Named Entity Recognition for Historical Documents** (CoNLL 2020): https://aclanthology.org/2020.conll-1.35/
- Michail et al., 2026, **A Recipe for Adapting Multilingual Embedders to OCR-Error Robustness and Historical Texts**: https://aclanthology.org/2026.lrec-1.71/

## 4. Findings

### F-C7-01 – OCR/HTR ist material- und workflowabhängig; es gibt keinen universellen „besten OCR-Stack“

OCR4all, Kraken und Transkribus repräsentieren unterschiedliche Stärken:

- **OCR4all** ist auf historische Drucke und einen nachvollziehbaren, korrigierbaren Workflow ausgerichtet; die Dokumentation integriert Ground-Truth-/Evaluation-Schritte und PAGE XML.
- **Kraken** ist ein trainierbares OCR-System für historische und nichtlateinische Materialien und kann standardisierte Outputs wie ALTO, PageXML und hOCR mit Layout-/Bounding-Box-/Confidence-Information erzeugen.
- **Transkribus** bietet cloudbasierte OCR/HTR-Modelle/API und liefert u. a. PAGE XML und ALTO; Modell-, Kosten-, Rechte- und Cloudfragen sind getrennt in C9/#40 zu bewerten.

**Scholarly implication:** Histo-Orla braucht eine **Material/Quality Decision Capability**, keine harte Engine-Festlegung vor dem Corpus-Benchmark.

Materialkategorien v0.1:

1. born-digital text;
2. PDF mit brauchbarem Textlayer;
3. historischer Druck / Antiqua;
4. historischer Druck / Fraktur/heterogene Typographie;
5. komplexes Layout (Spalten, Tabellen, Marginalien, Regesten);
6. Handschrift/HTR;
7. Karte/Plan mit textuellen Elementen – eher Sonderworkflow als „OCR-Dokument“.

### F-C7-02 – Findspot-preserving OCR braucht Seiten-/Bild-/Derivatbezug, nicht nur Plain Text

OCR-Ds PAGE-Konventionen sind für Histo-Orla methodisch besonders stark:

- **eine PAGE-Datei entspricht einer Seite des Originaldokuments**;
- `imageFilename` soll auf das **Originalbild** verweisen und zwischen Processing-Schritten nicht still wechseln;
- abgeleitete Bilder werden als `AlternativeImage` behandelt;
- METS kann verschiedene File Groups/Processing Stages derselben physischen Seite zuordnen;
- Textregionen/Zeilen besitzen Koordinaten.

Der konkrete OCR-D-Standard muss nicht Histo-Orlas Format werden. Aber die wissenschaftliche Invariante ist klar:

```text
Source / exact digital instance
→ physical page / folio
→ image / region
→ OCR/HTR derivative + processing state
→ recognized text
→ corrected/normalized derivative
→ search hit
→ exact back-reference to page/region
```

Plain Text allein ist als kanonisches OCR-Artefakt für consequential use unzureichend, wenn dadurch Seiten-/Regionbezug verloren geht.

### F-C7-03 – Originalreferenz und Processing Provenance müssen auch bei technisch schwierigen Transformationen sichtbar bleiben

OCR-Ds Workflow-Dokumentation zeigt eine reale technische Grenze: bei Dewarping/Cropping können Koordinatentransformationen so komplex sein, dass direkte Originalkoordinaten nicht immer trivial erhalten werden. Das ist wichtig, weil eine naive harte Forderung „jede Koordinate muss immer exakt auf Originalpixel zeigen“ technisch zu absolut wäre.

Histo-Orla braucht deshalb den wissenschaftlich robusteren Requirement-Kern:

- Parent/Source Instance bleibt identifizierbar;
- Seite/Folio bleibt stabil;
- Transformation/Processing Stage ist bekannt;
- wenn Region-/Pixelmapping nicht exakt erhalten bleibt, muss diese Loss/Transformation sichtbar sein.

**Kein stiller Precision Loss.**

### F-C7-04 – CER/WER allein reichen nicht für Histo-Orla-Qualität

OCR4all unterstützt Ground Truth und Fehlerraten; klassische CER/WER bleiben sinnvoll. Für historische Forschung muss zusätzlich gemessen werden, ob **research-critical tokens** erhalten bleiben:

- Personen- und Ortsnamen;
- Flur-/Gewässernamen;
- Jahreszahlen, Geld-/Maßangaben, Seiten-/Regestnummern;
- historische Fachtermini;
- Tabellen-/Spaltenzuordnung;
- Marginalien/Überschriften, wenn sie Research-Relevanz besitzen.

Daraus folgt ein zweistufiges Evaluationsmodell:

```text
allgemeine OCR accuracy (CER/WER etc.)
+
research-critical token / layout / findspot loss checks
```

Ein Corpus kann einen akzeptablen Gesamt-CER haben und für Namens-/Prosopographie- oder Rechnungsrecherche trotzdem unzureichend sein.

### F-C7-05 – Historische Retrieval-Probleme entstehen aus mindestens zwei unabhängigen Noise-Kanälen

Die historische IR-Literatur unterscheidet praktisch:

1. **historische Sprach-/Schreibvariation**;
2. **OCR-/Digitalisierungsfehler**.

Dazu kommen im Histo-Orla-Kontext:

3. Namen-/Toponymvarianten;
4. Flexion/Komposition;
5. fachliche/historische Terminologieverschiebung (C2).

Standard-Exact Search allein verliert Recall. Aber pauschales Fuzzy Matching löst das Problem ebenfalls nicht: ältere Arbeiten zeigen, dass angepasste historische Lexika, edit-distance/matching rules und corpus-/fehlerbezogene Profile nützlich sind und dass Qualität bei sehr verrauschtem OCR die Retrievalleistung begrenzt.

**Implication:** Query Expansion soll reason-coded und schichtweise erfolgen.

### F-C7-06 – Auditierbare Retrieval-Baseline v0.1

Bevor Semantic Search zugelassen wird, muss Histo-Orla mindestens leisten:

#### Layer 0 – Identity / filters

Quelle, Sammlung, Zeitraum, Typ, Sprache, ggf. Region/Collection/Tags.

#### Layer 1 – Exact lexical

- exakte Wörter/Phrasen;
- Groß-/Kleinschreibung/Unicode sinnvoll normalisiert;
- Trefferkontext + exakter Findspot.

#### Layer 2 – orthographic/name variants

- dokumentierte Schreibvarianten;
- historische Orthographie;
- reguläre Namens-/Toponymvarianten;
- C2 Concept-vs-Search-Layer getrennt.

#### Layer 3 – fuzzy / OCR-aware matching

- Edit Distance / confusion-aware matching;
- transparentes Threshold/Rule Set;
- warum Treffer erzeugt wurde sichtbar.

#### Layer 4 – linguistic expansion

- Lemmatisierung/Flexion/Komposita, soweit Sprache/Periode Verfahren trägt;
- kontrollierte historische Lexika/Regeln.

#### Layer 5 – conceptual expansion

Aus C2 abgeleitete related concepts / archival terms, **nicht als Synonyme**, sondern getrennte Queries mit Reason Code.

Jeder Suchlauf sollte mindestens rekonstruierbar machen:

```text
original query
→ expansions + reason/type
→ filters/corpus boundary
→ retrieval method/version
→ ranked hits
→ exact source/findspot
```

### F-C7-07 – Semantic Search / Embeddings sind nützlich, aber kein Default-Ersatz für historische IR

Aktuelle 2026er Forschung zeigt, dass moderne multilingual embeddings auf OCR-verrauschten historischen Dokumenten **messbar degradieren** und durch spezielle OCR-/historical adaptation verbessert werden können. Das ist gerade ein Argument **gegen** die Annahme, dass generische Embeddings automatisch robust seien.

Semantic Search kann sinnvoll sein für:

- konzeptuelle Discovery, wenn Nutzer die Wortform nicht kennt;
- thematische Similarity über Varianten hinaus;
- cross-lingual/heterogene Corpora;
- Ranking zusätzlicher Kandidaten.

Sie darf erst als additive Schicht admitted werden, wenn Gold Queries zeigen:

1. zusätzlicher Recall für relevante Fälle;
2. keine inakzeptable Verschlechterung exakter Namen/Fundstellen;
3. Treffer bleiben auf konkrete Source/Findspot zurückführbar;
4. Modell/Embedding-Version und Corpus sind bekannt;
5. Retrieval lässt sich gegen lexical baseline vergleichen;
6. hallucinated „answers“ werden nicht mit Retrievaltreffern verwechselt.

**RAG ist eine Antwort-/Syntheseschicht auf Retrieval, keine Fundstellenmethode an sich.**

### F-C7-08 – Zotero ist 2026 eine starke Integrationsschicht, aber kein vollständiges Histo-Orla-Research-System

Aktuelle Zotero-Dokumentation zeigt:

- automatische Volltextindexierung für PDF/EPUB/HTML/plain text;
- Quick/Advanced Search über Attachment Content;
- Rebuild/Reindex und sichtbaren Indexstatus;
- Web API v3 und **Local API** auf `localhost`, offline und ohne API-Rate-Limit;
- Full-Text-Content-Endpunkte mit `indexedPages/totalPages` bzw. Zeichenangaben;
- lokale API kann Attachment-Dateien referenzieren und Volltext schreiben/lesen.

Damit ist H-001 deutlich stärker als reine Bibliographie-Hypothese:

> **Zotero ist ein sehr plausibler bibliographischer/Attachment-/Metadata-/Basic-Fulltext Integration Hub.**

Aber aktuell belegt die Dokumentation nicht, dass Zotero allein alle Histo-Orla-Anforderungen erfüllt:

- historische/archivische Query Expansion nach C2;
- explizite Raw-OCR vs corrected/normalized derivative lineage;
- page/region-stable scholarly findspot model über heterogene Derivate;
- Search Boundary/Query Provenance;
- Source Dependence/Claim/Evidence Research State;
- domänenspezifische Evaluation.

**Disposition H-001:** `adapt / strong integration candidate`, nicht „Zotero = vollständige Source of Truth“.

### F-C7-09 – OCR-Korrektur muss derivative/revision sein, nicht stiller Ersatz

Historische IR profitiert von besserem OCR; gleichzeitig kann Korrektur historische Schreibvariation fälschlich normalisieren. Deshalb mindestens unterscheiden:

```text
original image
raw OCR/HTR
corrected transcription/OCR
normalized/search form (optional)
```

Jede Ebene kann für andere Aufgaben nützlich sein. Search darf normalisierte Formen nutzen, muss aber zum Original-/Transkriptionsbefund zurückführen.

## 5. OCR/HTR Decision Matrix v0.1

| Material | Default direction | Quality emphasis | Notes |
|---|---|---|---|
| born-digital / guter Textlayer | übernehmen + validieren | Findspot/encoding | kein OCR erzwingen |
| moderner/historischer Druck, sauber | bestehender OCR/Textlayer oder OCR engine benchmark | CER/WER + critical tokens | günstigster robuste Weg |
| Fraktur/früher Druck | OCR4all/Kraken/geeignete Modelle benchmarken | critical names/terms + layout | Training/adaptation möglich |
| komplexer historischer Druck | layout-aware workflow + human correction | regions/reading order/findspots | sequential workflow oft sinnvoll |
| Handschrift | HTR model/workflow (z. B. Transkribus/Kraken je Material) | CER + paleographic uncertainty | fachliche Ground Truth nötig |
| Karten/Pläne | spezialisierte text-/layout extraction nur wenn sinnvoll | labels/coordinates/source image | nicht in linearen Volltext zwingen |

**Keine Engine wird ohne Corpus-Test zum Requirement.**

## 6. Minimum Derivative / Findspot Requirements

Jedes consequential OCR-/HTR-Artefakt muss mindestens rekonstruierbar machen:

- Parent source / exact inspected digital instance;
- Seite/Folio/Page ID;
- Derivattyp;
- Processing tool/model/version soweit material;
- raw vs corrected vs normalized status;
- mapping zur Seite und wenn verfügbar Region/line coordinates;
- bekannte Loss/Transformation;
- Qualitäts-/Confidence-/Reviewstatus;
- keine Überschreibung des Originalderivats.

## 7. Retrieval Evaluation Plan v0.1

Gold Query Set muss verschiedene Fälle enthalten:

1. exakte seltene Namen;
2. bekannte historische Namensvarianten;
3. OCR-typische Fehler;
4. Flexions-/Kompositionsformen;
5. historischer Begriff vs moderner Analysebegriff;
6. U1 Wasser-/Teich-/Fischerei-/Hutungsbegriffe;
7. U2 lateinisch/deutsche Personen-/Herrschaftsbegriffe;
8. U3 Personen/Ämter/Orte/Korrespondenz;
9. negative queries / bekannte Nichttreffer.

Metriken:

- Recall@relevant set / miss rate;
- Precision@k für Forschungsworkflow;
- exact-name recall separat;
- findspot correctness;
- expansion transparency;
- false-positive class by expansion layer;
- latency/interaction cost nur sekundär.

Semantic layer wird nur admitted, wenn sie gegen Baseline messbar zusätzlichen Nutzen liefert.

## 8. Capability Candidates

- `CAP-DOCUMENT-INSPECTION`: Ausgangslage/Textlayer/Materialtyp erkennen.
- `CAP-OCR-HTR`: materialgeeignetes OCR/HTR mit Ground-Truth-/Reviewpfad.
- `CAP-DERIVATIVE-PROVENANCE`: Original/Raw OCR/Korrektur/Normalisierung getrennt führen.
- `CAP-FINDSPOT-PRESERVATION`: Seite/Folio/Region beim Processing/Search erhalten.
- `CAP-HISTORICAL-LEXICAL-SEARCH`: Exact + historische Varianten + OCR-aware + linguistische Suche.
- `CAP-QUERY-PROVENANCE`: Expansionen/Reason Codes/Corpus Boundary reproduzierbar machen.
- `CAP-SEMANTIC-RETRIEVAL-OPTION`: semantische Retrievalschicht nur benchmark-admitted.
- `CAP-ZOTERO-INTEGRATION`: Zotero Items/Attachments/Fulltext/API nutzen, ohne Forschungszustand darin zu monopolisieren.

## 9. Quality / Requirement Candidates

- REQ-C7-A: OCR/HTR darf Source/Original nicht überschreiben; Derivatstatus muss sichtbar sein.
- REQ-C7-B: Seite/Folio muss durch OCR/HTR/Retrieval stabil rückführbar bleiben; unvermeidbare Mapping-Losses müssen explizit sein.
- REQ-C7-C: OCR/HTR-Evaluation muss neben CER/WER research-critical tokens/layout/findspots prüfen.
- REQ-C7-D: Basissuche muss ohne semantische KI Exact Search + kontrollierte Varianten/Filter unterstützen.
- REQ-C7-E: Jede Query Expansion muss Typ/Grund nachvollziehbar machen; Concept Expansion darf keine Synonymie behaupten.
- REQ-C7-F: Semantic Search/RAG darf nur als additive evaluierte Schicht admitted werden.
- REQ-C7-G: Retrievaltreffer müssen konkrete Source/Findspot-Evidenz liefern; generierte Antwort allein genügt nicht.
- REQ-C7-H: Zotero-Integration soll bestehende Bibliographie/Attachments/APIs wiederverwenden, darf aber fehlende Research-State-Funktionen nicht durch implizite Doppelwahrheiten kompensieren.

## 10. Tool Candidate Shortlist – nur SOTA-Input

- **Zotero:** Bibliographie/Attachments/Local API/Fulltext/search integration – sehr starker reuse candidate.
- **OCR-D/PAGE/METS patterns:** Referenz für derivative/page/layout provenance; kein Pflichtstandard.
- **OCR4all:** starker Kandidat für historische Drucke/HITL/Evaluation.
- **Kraken:** offener trainierbarer OCR/HTR-/layout-aware Kandidat mit standardisierten Outputs.
- **Transkribus:** starker HTR/OCR-Service-/Model-Kandidat; Cloud/Kosten/Rechte in C9/#40.
- **klassische IR/Fuzzy/linguistische Verfahren:** Default-Forschungsbaseline vor embeddings.
- **OCR-robuste/historisch adaptierte embeddings:** experimentelle additive Schicht, nicht Kerninvariante.

## 11. Challenge interner Annahmen

- #4/#5 werden im Bedarf bestätigt.
- #3 Zotero wird von `hypothesis` zu **strong integration candidate / adapt** aufgewertet, aber nicht zum vollständigen Source of Truth.
- #8 „script/local/AI optional“ wird durch Zotero Local API und klassische IR-SOTA technisch plausibler, bleibt Architekturfrage.
- `paleo-type` Original/Derivative/Provenance-Prinzip wird durch OCR-D-Praxis stark bestätigt.

## 12. Open Questions / bounded debt

- Corpus-spezifischer Benchmark entscheidet konkrete OCR/HTR-Engine(s), Modelle und Parameter.
- Konkrete Storage-/Indextechnologie bleibt #39/#43.
- Rechte-/Cloudentscheidung für Transkribus/andere Services gehört #40/#39.
- Zotero-Collections/Attachment-Modi des realen Nutzerbestands sind observation-needed, aber kein Blocker für die Integration-Capability.
- Karten-/Plan-OCR benötigt ggf. eigenen Spezialworkflow bei realem Bedarf.

## 13. #45 Quality Check

- **Domain fit:** OCR/HTR/IR führen; Software/AI nicht als fachliche Autorität.
- **Evidence fit:** aktuelle offizielle Tool-/Standarddokumentation und historische IR-Literatur wurden geprüft; Toolmarketing wird nicht als Qualitätsbeweis genutzt.
- **Inference fit:** keine Engine wird als allgemein „beste“ bezeichnet; ältere IR-Befunde werden als etablierte Problemlogik, nicht als aktueller Benchmark aller Methoden behandelt.
- **Terminology fit:** OCR error, historical spelling, concept expansion, fuzzy matching und semantic retrieval getrennt.
- **Provenance fit:** Links/Standards/aktuelle Zotero-Dokumentation dokumentiert.
- **Falsification/challenge:** konkreter Corpus-Benchmark + Gold Queries können Engine-/Semantic-/Zotero-Integration-Hypothesen widerlegen oder begrenzen.

## 14. Sättigungsbegründung

Für architecture-driving Requirements ist SOTA ausreichend: Der Kernbedarf ist findspot-preserving derivative provenance plus eine auditierbare lexical/historical retrieval baseline; konkrete Engines und semantische Verfahren müssen benchmark-basiert gewählt werden. Weiteres Tool-Screening vor Capability/Requirements würde derzeit eher Produktbreite als diskriminierende Erkenntnis erzeugen.
