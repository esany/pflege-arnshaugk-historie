# Histo-Orla – Research Workflows U1–U4 v0.1

**Work Owner:** #29  
**Status:** `working-research / workflow-baseline-v0.1`  
**Inputs:** #28 / `problem-baseline.md`, kanonischer Konzeptstand, dokumentierte reale Projektinteraktionen und Designfälle aus #10.  
**Regel:** Beobachtete Arbeitsweisen und rekonstruierte/angenommene Schritte werden getrennt. Unbekannte Details werden als `observation-needed` geführt und blockieren die weitere Research-/SOTA-Arbeit nicht.

## Evidenzstatus für Workflow-Schritte

- `observed` – aus konkreten bisherigen Projektinteraktionen / explizitem Nutzerwunsch belegt
- `documented-goal` – im kanonischen Projektstand als gewünschte Arbeitsweise dokumentiert
- `inferred-current` – plausible Rekonstruktion des heutigen manuellen Ablaufs; noch zu beobachten
- `future-capability` – gewünschte Assistenz, keine Aussage über heutigen Ablauf
- `observation-needed` – Detail für spätere reale Nutzungsmessung offen

---

# U1 – Historische Teich-/Niederungs-/Landnutzungsstrukturen vor 1800

## Forschungsanlass / Trigger

**Status:** `observed`

Ausgangspunkt ist eine konkrete räumliche Beobachtung im Raum Arnshaugk / Orla / Vogtland / Ostthüringen: heutige oder kartographisch erkennbare Niederungen, Teich-/Feuchtstrukturen, Dämme, Flurformen oder Gewässerzüge werfen die Frage auf, wie groß/alt eine Struktur historisch tatsächlich war und welche vormodernen Quellen sie belegen.

Der bisherige Projektverlauf zeigt ausdrücklich den Übergang von modernen/neueren Karten zu der Frage nach **vor-1800-tauglichen Quellengruppen**: Forst-, Flur-, Hutungs-, Grenz-, Jagd-/Forst- und Gutsrisse; Grenz-/Hutungs-/Triftstreitigkeiten; Teich-/Wasser-/Fischerei-/Mühlenakten; Rechnungen; Urbare/Salbücher; Gemeinheitsteilung/Separation; Kataster; ältere Karten; Luftbilder; LiDAR/DEM.

## Gewünschtes Erkenntnisergebnis

Nicht nur „auf einer Karte war ein Teich“, sondern eine quellenkritische Rekonstruktion:

```text
Welche Struktur existierte wann?
→ welche räumliche Ausdehnung / Nutzung ist belegbar?
→ welche Quelle bildet welchen Zustand und welchen Zweck ab?
→ natürliche vs. anthropogene Struktur?
→ Besitz-/Nutzungs-/Wasser-/Fischerei-/Herrschaftskontext?
→ Persistenz / Veränderung / Aufgabe?
→ welche Unsicherheiten bleiben?
```

## Heutiger / rekonstruierter Workflow

| Schritt | Tätigkeit | Status | Friktion / Risiko | Judgment vs. Mechanik |
|---|---|---|---|---|
| U1-01 | Landschaftliche Auffälligkeit / konkrete Stelle identifizieren. | observed | Alltagssprache liefert noch keine fachliche Problemklasse. | Research Owner judgment |
| U1-02 | Neuere Karten/Meilenblätter/Topographie vergleichen und historische Ausdehnung abschätzen. | observed | Karten können zu jung, generalisiert oder für die Frage ungeeignet sein. | gemischt |
| U1-03 | Erkennen, dass klassische „Landkarten“ die Struktur nicht ausreichend beantworten. | observed | Gefahr, bei leicht verfügbaren Karten stehenzubleiben. | fachliches judgment |
| U1-04 | Passende fachliche Problembegriffe und Quellengattungen erschließen. | observed/documented-goal | Nutzer kennt Forst-/Flur-/Hutungs-/Grenzriss, Triftstreit etc. nicht zwingend vorher. | heute hoher manueller/fachlicher Aufwand; künftig assistierbar |
| U1-05 | Historische Verwaltung/Herrschaft/Gut/Amt für den Ort/Zeitstand rekonstruieren. | inferred-current | Ohne Registraturbildner/Provenienz bleiben Archive/Bestände unsichtbar. | fachliches judgment |
| U1-06 | Archive, Findmittel, Bestände, Serien und ältere Erschließungsterminologie durchsuchen. | observed-goal / inferred-current | Portale heterogen; moderne Schlagwörter unzureichend; Bestände nicht voll digital. | Suche mechanisch + fachliche Heuristik |
| U1-07 | Treffer auf tatsächliche Eignung prüfen: Karte/Akte/Rechnung/Urbar etc.; Überlieferungsstufe und Zeitstand bestimmen. | inferred-current | Katalogtreffer ≠ Quellenevidenz. | fachliches judgment |
| U1-08 | Digitalisat/Scan/Edition beschaffen bzw. Archivrecherche vorbereiten. | inferred-current | Rechte/Zugang/Bestellung/Scanqualität. | gemischt |
| U1-09 | Quelle erschließen: Lesen/OCR/HTR, Legende/Toponyme/Flurnamen, relevante Passage/Geometrie. | inferred-current | OCR/HTR, Kartenlesen, Paläographie; Findspotverlust. | spezialisierte Verfahren + Fachjudgment |
| U1-10 | Quellen unterschiedlicher Zeitstände/Zwecke räumlich vergleichen. | documented-goal | Generalisierung, Maßstab, Projektion, Verwaltungszweck, Flur-/Nutzungsänderungen. | fachliches judgment / GIS ggf. Support |
| U1-11 | Schriftliche, kartographische und ggf. geomorphologische/LiDAR-Befunde getrennt bewerten. | documented-goal | inkommensurable Evidenz nicht vorschnell verschmelzen. | mehrere Fachdomänen |
| U1-12 | Besitz-, Nutzung-, Wasser-, Fischerei-, Agrar-/Herrschaftskontext ergänzen. | documented-goal | gleicher Landschaftsbefund kann verschiedene historische Funktionen haben. | transdisziplinäres judgment |
| U1-13 | Synthese mit Zeitständen, Evidenzgrenzen, Alternativen und offenen Quellenwegen erstellen. | future-capability / teilweise heutige manuelle Arbeit | Gefahr einfacher Ursprungsgeschichte. | Fachsynthese, nicht mechanisch |

## Pains / fehlendes Wissen

Primär: P-001, P-002, P-005, P-006, P-007, P-011.  
Sekundär: P-003/P-004 bei Scans; P-012 bei mehrfach tradierten Karten-/Literaturangaben.

Besonders unsichtbare Facharbeit:

- historische Verwaltungszuständigkeit → Archiv/Bestand;
- kartographische Quellenkritik;
- historische Landschafts-/Agrar-/Wasserterminologie;
- Unterscheidung Befund vs. Nutzung/Funktion;
- Zeit-/Maßstabsvergleich;
- negative Evidenz / Überlieferungslücken.

## Candidate Automation / Support

- Fachvokabular-/Quellengattungs-Vorschläge aus Beobachtung;
- Varianten-/Archivterminologie-Expansion;
- Link-/Metadaten-/Bestandsrecherche bündeln;
- OCR/HTR und Fundstellenextraktion;
- Karten-/Quellen-Metadaten normalisieren;
- Search Log / Search Boundary automatisch führen;
- wiederkehrende Orts-/Namensvarianten vorschlagen;
- räumliche Vergleichsdaten vorbereiten.

## Nicht still automatisieren

- Quelle als „Beweis“ klassifizieren;
- kartographischen Unterschied kausal erklären;
- natürlichen vs. anthropogenen Ursprung behaupten;
- Besitz-/Nutzungsfunktion aus bloßer Geometrie ableiten;
- fehlenden Treffer als historische Abwesenheit werten;
- unterschiedliche Zeitstände zu einem einzigen „wahren“ Polygon verschmelzen.

## Human/Fach-Eskalation

Je nach Material: Archivistik/Registraturkunde, historische Geographie/Kartenkritik, Umwelt-/Agrargeschichte, Hydrologie/Geoarchäologie, Archäologie, Paläographie.

## Offene Beobachtungsfragen

- Welche Portale/Archive nutzt der Research Owner heute zuerst und mit welchen manuellen Notizen?
- Wie häufig werden Quellen wirklich lokal gespeichert vs. nur verlinkt?
- Welche GIS-/Kartenwerkzeuge werden bereits genutzt?
- Welche Archivkontakte/Bestellungen sind wiederkehrend?

Diese Details beeinflussen spätere UX/Integration, blockieren aber die fachliche SOTA nicht.

---

# U2 – Vogtei / Ministerialität / Herrschaft / Siedlungsbeziehungen

## Forschungsanlass / Trigger

**Status:** `documented-goal / representative-real-question-class`

Ausgangspunkt ist eine Beobachtung oder Quelle, in der ein Akteur als Vogt, Dienstmann, Ritter, Herrschaftsträger o. Ä. erscheint oder eine Besitz-/Schutz-/Gerichtsbeziehung erkennbar ist. Der Research Owner kennt die fachlich konkurrierenden Kategorien nicht zwingend im Voraus.

## Gewünschtes Erkenntnisergebnis

Nicht: „Was ist ein Vogt?“ als Lexikonfrage.

Sondern:

```text
Welche konkrete Beziehung/Funktion ist hier wann und wo belegt?
→ welche zeitgenössischen Begriffe stehen in der Quelle?
→ welche modernen Analysemodelle sind einschlägig?
→ Vogtei, Schutzvogtei, Ministerialität, Lehen, Grundherrschaft,
  Gerichtsherrschaft, Patronat, Amt etc. – was passt / was nicht?
→ welche Herrschafts-/Siedlungs-/Familienbeziehungen sind belegt?
→ welche Forschungsdebatten und regionalen Besonderheiten gelten?
```

## Workflow

| Schritt | Tätigkeit | Status | Friktion/Risiko | Judgment vs. Mechanik |
|---|---|---|---|---|
| U2-01 | Beobachtung/Quelle/ältere Darstellung formuliert eine unscharfe Beziehung. | documented-goal | Alltagssprache („Beamter“, „abhängig“, „Adliger“) kann anachronistisch sein. | Owner input |
| U2-02 | Quellentyp und Überlieferungsstufe bestimmen: Urkunde, Regest, Kopialbuch, Lehnbuch, spätere Darstellung etc. | documented-goal | Regest/Edition wird leicht mit Originalquelle verwechselt. | Diplomatik/Quellenkunde |
| U2-03 | Original-/Quellenbegriffe und Namensformen erfassen. | inferred-current | Latein/Mittelhochdeutsch/Schreibvarianten; editorische Normalisierung. | Philologie/Diplomatik |
| U2-04 | Fachliche Problembegriffe als konkurrierende Kandidaten erschließen. | documented-goal | voreilige Klassifikation führt zu falscher Recherche. | Fachjudgment, KI ggf. Candidate Support |
| U2-05 | Zeit-/Raum-/Institution-Geltungsbereich der Begriffe prüfen. | documented-goal | `Vogtei`/`Ministerialität` nicht zeitlos. | Mediävistik/Rechts-/Herrschaftsgeschichte |
| U2-06 | Personen-/Ämter-/Besitz-/Lehens-/Patronatsbezüge chronologisch sammeln. | inferred-current | Identitäten/Datierungen/Abhängigkeiten unsicher. | gemischt |
| U2-07 | Regionale Editionen, Regesten, Urkundenbücher, Archive und Forschungsliteratur recherchieren. | documented-goal | regionale Spezialbibliographie und Archivterminologie nötig. | Suche + Fachheuristik |
| U2-08 | Ältere landes-/genealogiegeschichtliche Ableitungen gegen Quellenabhängigkeit prüfen. | documented-goal | Historiographische Ketten können wie unabhängige Evidenz wirken. | Quellenkritik/Historiographie |
| U2-09 | Herrschafts-/Sozialmodell gegen konkrete Evidenz testen; Alternativen offen halten. | documented-goal | Modelllabel kann Quelle überformen. | fachliches judgment |
| U2-10 | Siedlungs-/Raumbezüge nur bei realem Evidenzbezug hinzufügen. | documented-goal | Ko-Lokalität ≠ institutionelle Beziehung. | Mediävistik + historische Geographie/Archäologie ggf. |
| U2-11 | Ergebnis als Befund + Modelle + Forschungsstand + Grenzen + nächste Quellen formulieren. | future-capability | Gefahr einfacher „Feudalismus“-Erklärung. | Fachsynthese |

## Pains

P-001, P-002, P-005–P-008, P-012, P-013.

## Candidate Automation / Support

- Fachbegriff-/Modell-Kandidaten mit Geltungswarnungen;
- Varianten-/Latein-/Namenssuche;
- Regesten/Editionen/Bestände priorisieren;
- chronologische Personen-/Rollen-Kandidatenliste;
- Quellenabhängigkeits-Hinweise;
- zitierfähige Fundstellen sammeln.

## Nicht still automatisieren

- Person/Institution zusammenführen;
- `ministerialis`, `miles`, `advocatus` etc. pauschal modern übersetzen;
- Rechts-/Sozialstatus aus einem Rollenwort ableiten;
- Lehens-/Dienst-/Verwandtschaftsrelation ohne Evidenz setzen;
- ältere Forschungsmeinung als aktuellen Konsens ausgeben.

## Human/Fach-Eskalation

Diplomatik, Mediävistik, Landes-/Herrschafts-/Rechtsgeschichte, ggf. Kirchen-/Patronatsgeschichte, Onomastik, Siedlungsarchäologie.

---

# U3 – Frühneuzeitlicher adliger Akteur / politische Handlungslogik

## Forschungsanlass / Trigger

**Status:** `documented-goal / representative-real-question-class`

Frage nach Verhalten/Position eines niederadligen oder höfisch-politischen Akteurs um ca. 1600–1640 zwischen lokalem Besitz, Kursachsen, Reich/Kaiserhof, Konfession, Militär, Verwandtschaft, Ämtern, Patronage und Mobilität.

## Gewünschtes Erkenntnisergebnis

Nicht eine psychologische Ein-Satz-Erklärung, sondern eine quellenkritische Situation Analysis:

```text
Akteur / Zeitpunkt
→ Rollen und institutionelle Position
→ Besitz / Ressourcen / finanzielle Interessen
→ Familie / Verwandtschaft / Patronage / Ämter
→ Konfession / Hof / Territorial- und Reichskontext
→ Kommunikation / Aufenthalte / Informationshorizont
→ zeitgenössisch erkennbare Optionen / Zwänge / Risiken
→ beobachtete Handlung
→ dokumentierte Motive / Selbstbeschreibung
→ fremde Zuschreibungen
→ mehrere Erklärungshypothesen
→ Gegenbelege / Quellenlücken
```

## Workflow

| Schritt | Tätigkeit | Status | Friktion/Risiko | Judgment vs. Mechanik |
|---|---|---|---|---|
| U3-01 | Akteur und konkrete Handlung/Entscheidung zeitlich begrenzen. | documented-goal | biographische Gesamtdeutung verwischt Situation. | Owner/Fachjudgment |
| U3-02 | Personidentität, Namensvarianten, Titel, Ämter, Besitz und Verwandtschaft sammeln. | inferred-current | Entity-Merge-Risiko; Status ändert sich über Zeit. | gemischt |
| U3-03 | Primär-/nahe Quellen und unabhängige Perspektiven identifizieren: Korrespondenzen, Rats-/Hofakten, Rechnungen, Militär-/Diplomatiequellen, Selbst-/Fremdzeugnisse. | documented-goal | Quellenräume sind verteilt; politische Überlieferung perspektivisch. | Archiv-/Fachheuristik |
| U3-04 | Aufenthalte, Reisen, Gesandtschaften, Hof-/Universitäts-/Militärkontakte chronologisch rekonstruieren. | documented-goal | Ko-Präsenz ist keine Beziehung; Reisezweck variabel. | Prosopographie + Quellenkritik |
| U3-05 | Belegte Relationen von bloßer Gleichzeitigkeit/Ko-Lokalität trennen. | documented-goal | Netzwerkvisualisierung kann überbehaupten. | Fachjudgment |
| U3-06 | Historische Institutionen/Entscheidungsräume rekonstruieren: Hof, Geheimer Rat, Ämter, Reich/territoriale Politik, Konfession etc. | documented-goal | moderne Institutionen-/Parteiannahmen anachronistisch. | Fachjudgment |
| U3-07 | Informationshorizont begrenzen: Was konnte der Akteur zu diesem Zeitpunkt wissen? | documented-goal | retrospektives Wissen erzeugt Rationalitätsillusion. | Fachjudgment |
| U3-08 | Ressourcen/Zwänge/Anreize erfassen, aber nicht automatisch als Motive setzen. | documented-goal | Besitz/Familie/Konfession korrelieren, beweisen Motiv aber nicht. | Fachjudgment |
| U3-09 | Dokumentierte Motive, Selbstbeschreibung und Fremdzuschreibung getrennt erfassen. | documented-goal | Quellen sind strategische Kommunikation. | Quellenkritik |
| U3-10 | Mehrere alternative Erklärungen formulieren und gezielt Gegenbelege suchen. | documented-goal | Generative Synthese tendiert zu einer kohärenten Story. | adversarial Facharbeit |
| U3-11 | Multi-Scale-Kontext nur soweit erklärungsrelevant erweitern: lokal ↔ Kursachsen ↔ Reich/Hof ↔ europäische Kriegs-/Diplomatieräume. | documented-goal | Scope kann explodieren. | Scale judgment |
| U3-12 | Forschungsstand/Hof-/Adels-/Diplomatie-/Konfessions-/Militärtraditionen vergleichen. | documented-goal | einzelne Fachtradition kann dominante Erklärung liefern. | transdisziplinär |
| U3-13 | Synthese mit Evidenzstatus und Alternativen. | future-capability | false certainty / psychologizing. | Fachsynthese |

## Pains

P-001/P-002/P-007/P-008/P-011–P-014.

## Candidate Automation / Support

- Personen-/Namens-/Ämter-Kandidaten und chronologische Tabellen;
- Quellen-/Archivräume aus Rollen/Institutionen ableiten;
- Reise-/Aufenthaltsdaten strukturieren;
- relation candidates mit Belegstatus;
- Quellenabhängigkeit markieren;
- alternative Erklärungsfragen generieren;
- Timeline/Context View als abgeleitete Sicht.

## Nicht still automatisieren

- Motiv aus Netzwerk/Position/Religion/Verwandtschaft ableiten;
- Beziehung aus Ko-Präsenz erzeugen;
- politische „Lager“ als moderne Parteien behandeln;
- Informationshorizont mit retrospektivem Wissen auffüllen;
- mehrere plausible Erklärungen zu einer glatten Biographie verschmelzen.

## Human/Fach-Eskalation

Frühneuzeitforschung, Adels-/Hof-/Reichs-/Territorialgeschichte, Diplomatie, Konfession, Militär, Prosopographie/Netzwerk-/Mobilitätsgeschichte; bei consequential interpretation ggf. externe Fachprüfung.

---

# U4 – Persönliches Quellenarchiv / OCR / Retrieval / Fundstellen

## Forschungsanlass / Trigger

**Status:** `observed/documented-goal`

Eine Edition, ein Regestenwerk, PDF, Scan oder anderes Quellen-/Literaturartefakt soll im persönlichen Forschungsbestand zuverlässig wiedergefunden, erschlossen, durchsucht und mit exakter Fundstelle für spätere Forschung verwendet werden.

## Gewünschtes Erkenntnisergebnis / Job-to-be-done

```text
Quelle/Literatur sicher identifizieren
→ digitale Instanz übernehmen/referenzieren
→ vorhandenen Volltext erkennen
→ fehlenden Volltext als Derivat erzeugen
→ Seite/Folio/Regest erhalten
→ historische Varianten durchsuchen
→ relevante Passage finden
→ Passage zurück auf konkrete Quelle/Fundstelle führen
→ Befund in weitere Forschung übernehmen
→ später reproduzierbar wiederfinden
```

## Workflow

| Schritt | Tätigkeit | Status | Friktion/Risiko | Judgment vs. Mechanik |
|---|---|---|---|---|
| U4-01 | Literatur/Quelle bibliographisch bzw. archivalisch identifizieren. | observed/documented-goal | Dubletten/Editionen/Instanzen; nichtklassische Quellentypen. | gemischt |
| U4-02 | Quelle in Zotero bzw. aktuellem persönlichen Bestand referenzieren/finden. | documented current preference; exact practice observation-needed | Zotero-Keys/Attachments/externe Dateien können heterogen sein. | mechanisch + bibliographisches judgment |
| U4-03 | Konkrete digitale Instanz/Attachment/Scan bestimmen. | documented-goal | URL/Item ≠ tatsächlich inspizierte Datei. | mechanisch/provenance |
| U4-04 | Prüfen: born-digital Text, PDF-Textlayer, Bild-PDF, Seitenbilder, Handschrift. | documented-goal | falsche Annahme über Textlayer. | deterministisch/spezialisiert |
| U4-05 | Falls nötig OCR/HTR als getrenntes Derivat erzeugen. | documented-goal | Qualitäts-/Layout-/Rechtefragen. | spezialisierte Verfahren |
| U4-06 | Seiten-/Folio-/Regeststruktur und Provenienz erhalten. | documented-goal | Text-Export kann Findspots verlieren. | deterministisch erzwingbar + Quellentypwissen |
| U4-07 | Exact Search / Phrase / Filter verwenden. | documented-goal | historische Schreibvarianten fehlen. | deterministisch/IR |
| U4-08 | Kontrollierte Varianten-/Namens-/Terminologie-Expansion hinzufügen. | documented-goal | Query Expansion kann falsche Synonyme erzeugen. | IR + Fachvokabular |
| U4-09 | Treffer mit Kontext, Fundstelle, Textstatus und Suchheuristik anzeigen. | future-capability | semantische Antwort ohne Fundstelle = Source Laundering. | Software/UX |
| U4-10 | Relevanten Befund/Excerpt kuratieren und auf Source/Fundstelle zurückverweisen. | documented-goal | doppelte Wahrheiten/Copy-Paste-Verlust. | Human + deterministic provenance |
| U4-11 | Spätere Frage an Bestand beantwortet sich zuerst über Treffer/Evidenz, dann Interpretation. | future-capability | Chat-with-PDF kann Synthese vor Befund stellen. | Retrieval + Fachjudgment |
| U4-12 | Verarbeitungszustand/Index bei Dateiänderung reproduzierbar aktualisieren. | architecture goal | technische Details offen. | mechanisch/software |

## Pains

P-002–P-005, P-008–P-010, P-015/P-016.

## Candidate Automation / Support

- Zotero-/Bibliographie-Suche und stabile Referenzierung;
- Textlayer-Erkennung;
- OCR/HTR-Jobauslösung;
- Seiten-/Fundstellen-Mapping;
- Index-/Search-Aufbau;
- historische Varianten;
- reproduzierbare Query Logs;
- Source/Derivative-Status anzeigen;
- Excerpt/Claim-Candidate mit Provenienz erzeugen;
- Change Detection/Restart.

## Nicht still automatisieren

- OCR-Korrektur als Original überschreiben;
- zwei bibliographische/archivalische Identitäten mergen;
- Fundstelle aus einer anderen Edition/Instanz übertragen, ohne Mapping;
- semantischen Treffer als wörtlichen Quellenbeleg ausgeben;
- Lizenz-/Rechteannahmen aus Dateizugänglichkeit ableiten;
- AI-generierten Claim direkt als validiert speichern.

## Human/Fach-Eskalation

Bibliographie/Archivistik bei Identitätsfragen, Paläographie/HTR bei schwieriger Handschrift, Fachdomäne bei Interpretation; technische Routine soll nicht am Research Owner hängen.

## Offene Beobachtungsfragen

- konkrete Zotero-Organisation/Collections/Tags/Attachment-Modi;
- typische Dateimengen und Dateigrößen;
- häufigste Druckschriften/Sprachen/Handschriften;
- bestehende lokale/Cloud-Speicherpraxis;
- bevorzugte Such-/Lesewerkzeuge.

Diese Fragen sind für spätere Architektur/UX relevant, nicht notwendig für den methodischen SOTA-Start.

---

# 5. Cross-Workflow Pain ↔ Workflow Matrix

| Pain | U1 | U2 | U3 | U4 | Interpretation |
|---|:---:|:---:|:---:|:---:|---|
| P-001 fehlendes Fachvokabular | ● | ● | ● | ○ | Kernproblem für fachliche Problemübersetzung. |
| P-002 verteilte Quellenräume | ● | ● | ● | ● | Quellen-/Archive Discovery cross-cutting. |
| P-003 nicht durchsuchbare Scans | ● | ○ | ○ | ● | U4 Hauptworkflow; U1–U3 abhängig vom Material. |
| P-004 Findspot-Verlust | ● | ● | ● | ● | Harte Provenienzanforderung. |
| P-005 historische Varianten | ● | ● | ● | ● | IR + Fachterminologie. |
| P-006 moderne Archivsuche reicht nicht | ● | ● | ● | ○ | Provenienz-/Registraturkunde. |
| P-007 Nutzer muss Disziplin kennen | ● | ● | ● | ○ | Expertise Routing. |
| P-008 AI false authority | ● | ● | ● | ● | Governance/Research UX. |
| P-009 repetitive Mechanik | ● | ○ | ● | ● | #29 zeigt echte Automationskandidaten. |
| P-010 Chat-Wissensmonopol | ● | ● | ● | ● | durch §14 organisatorisch bereits adressiert. |
| P-011 regionaler Container-Bias | ○ | ● | ● | – | C4. |
| P-012 false corroboration | ● | ● | ● | ● | C6. |
| P-013 Relation/Motiv aus Ko-Präsenz | ○ | ● | ● | – | C5/C4. |
| P-014 Research State schwer prüfbar | ● | ● | ● | ● | C8. |
| P-015 Provider-/Tool-Lock-in | ○ | ○ | ○ | ● | systemisch / C9. |
| P-016 Solution Bias | ● | ● | ● | ● | Governance/Requirements. |

`●` stark relevant, `○` situationsabhängig.

---

# 6. Human Judgment / Escalation Map

## Research Owner – soll besitzen

- Erkenntnisinteresse / Forschungsfrage / Relevanz;
- Priorität zwischen Forschungszielen;
- bewusste normative Scope-/Kosten-/Rechteentscheidungen;
- Konsequenzentscheidung für publikationsnahe Nutzung;
- Akzeptanz echter Residualrisiken.

## Fachspezialist / führende Fachdomäne – soll besitzen

- domänenspezifische Problembegriffe und Methoden;
- Evidenz-/Quellenkritik;
- zulässige Schlussarten;
- Kontroversen-/Geltungsbereich;
- consequential Interpretation;
- unabhängige Fachvalidierung, wo erforderlich.

## Deterministische Software – Kandidaten

- Datei-/Referenz-/Hash-/Versionsmechanik;
- Textlayer-/Dateityperkennung;
- exakte Suche/Filter;
- Provenienz-/Findspot-Mapping, soweit bekannt;
- Logs/Processing State;
- Validierung formaler Invarianten;
- Change Detection/Restart.

## Spezialisierte Verfahren – Kandidaten

- OCR/HTR/Layoutanalyse;
- fuzzy matching / linguistic IR;
- Gazetteer-/Entity-Candidate-Matching;
- geographische Transformation/Analyse;
- Ranking/Clustering, wenn benchmarkbar.

## LLM / generative Assistenz – Kandidaten

- Problem-/Vokabular-Kandidaten;
- Suchterminologie-/Quellengattungs-Hypothesen;
- Research Briefs;
- strukturierte Exploration und alternative Erklärungsfragen;
- verständliche Rückübersetzung bereits evidenzgebundener Befunde.

Kein stilles Promotion in kanonischen Forschungszustand.

---

# 7. Automation Candidate Seed

Priorität wird **noch nicht** als Feature-Priorität verstanden. Kandidaten müssen in #39 nach SOTA und Nutzerwert allokiert werden.

1. Source/Attachment/Textlayer Inspection
2. OCR/HTR Job + Derivative Provenance
3. Exact/Variant Search + Query Log
4. Findspot-preserving Excerpt Capture
5. Historical Name/Term Candidate Expansion
6. Archive/Bestand Research Brief aus Verwaltungskontext
7. Person/Place/Institution Candidate Matching
8. Timeline/Role/Travel Extraction als Candidate Layer
9. Search Boundary / Negative Finding Log
10. Research-Artefakt-/Issue Status Sync-Hilfe

---

# 8. Qualitätscheck #45 für WP-B

- **Domain fit:** Human Factors/Workflowanalyse führt; Fachdomänen wurden dort aktiviert, wo ein Judgment Point sie tatsächlich verlangt.
- **Evidence fit:** Die Workflows beanspruchen nur dort `observed`, wo der bisherige Projektverlauf dies trägt; andere Schritte sind `inferred-current`, `documented-goal` oder `observation-needed`.
- **Inference fit:** Rekonstruierte heutige Abläufe werden nicht als beobachtete Tatsachen ausgegeben.
- **Terminology fit:** Fachbegriffe dienen hier als Arbeitskategorien und werden in den SOTA-Paketen extern validiert.
- **Provenance fit:** Ursprung ist #10/#28 sowie dokumentierte Projektinteraktion; keine externe Forschung wird vorweggenommen.
- **Falsification/challenge:** Offene Beobachtungsfragen sind explizit; reale Nutzung kann die Journeys später korrigieren.

## Sättigungsbegründung

Für den Zweck, ein Research-Question-Portfolio zu schneiden, decken U1–U4 unterschiedliche kritische Belastungen ab: räumlich-archivalische Forschung, mediävistische Begriffs-/Quellenarbeit, erklärende Akteursforschung sowie persönliche Quellen-/Retrieval-Infrastruktur. Zusätzliche Use Cases können später ergänzt werden, sind aber nicht nötig, um #30–#39 zu starten.

## Nächster Schritt

#30: die in #28/#29 sichtbaren offenen Punkte in präzise, priorisierte und fachlich geroutete Research Questions überführen.
