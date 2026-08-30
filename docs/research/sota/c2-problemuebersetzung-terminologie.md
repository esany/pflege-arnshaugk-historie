# C2 – Fachliche Problemübersetzung, historische Terminologie und Begriffssysteme

**Work Owner:** #32  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** historische Semantik/Begriffsgeschichte, Fachphilologie/Sprachgeschichte, jeweilige historische Fachdomäne.  
**Controlling competencies:** Knowledge Organization/Terminologiewissenschaft, Archivistik, Information Retrieval, Research UX.

## 1. Research Questions

Primär RQ-C2-01 bis RQ-C2-04:

1. Wie wird eine Laienbeobachtung methodisch in fachliche Problemformulierungen übersetzt?
2. Wie unterscheiden wir Quellenwort, historische/institutionelle Bezeichnung, Archivsprache, modernen Analysebegriff, Historiographie und regionale/lateinische Varianten?
3. Wie trennen wir Concept Discovery von Query Expansion?
4. Wie lässt sich die Qualität dieser Übersetzung prüfen?

## 2. Search Scope / Boundary

Geprüft wurden:

- aktuelle und etablierte Literatur zu Begriffsgeschichte/historischer Semantik;
- ein aktueller methodischer Beitrag, der Wort-, Begriffs- und Diskursgeschichte explizit trennt/verbinden will;
- fachlexikographische Praxis am Deutschen Rechtswörterbuch;
- Knowledge-Organization-Standards SKOS und ISO 25964 als Vergleich für kontrollierte Relationen und IR;
- die Histo-Orla-Testfälle U1–U3.

Nicht beansprucht wird eine vollständige Geschichte der Begriffsgeschichte oder eine finale Ontologie/Thesaurusentscheidung.

## 3. Inspected sources

- ZfL Berlin, Müller/Schmieder, **Begriffsgeschichte und historische Semantik. Ein kritisches Kompendium**: https://www.zfl-berlin.org/publikationen-detail/items/begriffsgeschichte-und-historische-semantik.html
- Müller/Schmieder, **Begriffsgeschichte. Zur Einführung**: https://www.zfl-berlin.org/publikationen-detail/items/begriffsgeschichte-zur-einfuehrung.html
- Schwarzbach-Dobson, 2025, **Wort-, Begriffs- und Diskursgeschichte in Verbindung**: https://link.springer.com/article/10.1007/s41244-025-00369-2
- Deutsches Rechtswörterbuch (DRW): https://drw.hadw-bw.de/drw/info/drw_english.htm
- W3C, **SKOS Reference**: https://www.w3.org/TR/skos-reference/
- W3C, **SKOS Primer**: https://www.w3.org/TR/skos-primer/
- ISO 25964-1:2011 current published edition: https://www.iso.org/standard/53657.html
- ISO/FDIS 25964-1 Edition 2, approval stage in 2026: https://www.iso.org/standard/86713.html
- ISO 25964-2:2013: https://www.iso.org/standard/53658.html
- NISO ISO 25964 overview: https://www.niso.org/schemas/iso25964

## 4. Findings

### F-C2-01 – Fachliche Problemübersetzung darf nicht als Synonymexpansion modelliert werden

Müller/Schmieder behandeln Begriffsgeschichte und historische Semantik ausdrücklich als historisch und theoretisch umkämpfte Forschungspraktiken, nicht als neutrale technische Operation. Der 2025er Beitrag zur Verbindung von Wort-, Begriffs- und Diskursgeschichte ist zusätzlich ein nützlicher Warnhinweis: **Wortform, Begriff und Diskurs sind analytisch nicht identisch**.

Für Histo-Orla folgt:

```text
Nutzerwort / Beobachtung
≠
historischer Wortbeleg
≠
historischer Begriff / institutioneller Sachverhalt
≠
moderner Analysebegriff
≠
Archiv-Schlagwort / Erschließungssprache
≠
Suchvariante
```

**Implikation:** Problemübersetzung ist eine fachwissenschaftliche Interpretations-/Explorationsleistung mit Kandidatenstatus, nicht eine automatische Synonymliste.

### F-C2-02 – Begriffe brauchen Geltungsbereiche und Begriffstypen

Das DRW zeigt praktisch, wie stark historische Fachsemantik diachron und regional variieren kann: Es verfolgt rechtlich relevante Termini über sehr lange Zeiträume und unterschiedliche westgermanische Regionen und verbindet sprachliche/lexikographische mit rechtsvergleichenden Methoden.

Für Histo-Orla muss ein Concept Candidate deshalb mindestens nach folgenden Dimensionen befragbar sein:

- Begriffstyp / Funktion im Research;
- historische Zeitgültigkeit;
- regionale Gültigkeit;
- institutioneller/rechtlicher Kontext;
- Quellengattung / Sprachregister;
- historiographischer Status;
- Relation zu moderner Analysebezeichnung;
- dokumentierte Quellenformen/Schreibvarianten.

Nicht jedes Feld muss technisch permanent gespeichert werden; fachlich muss diese Prüfung möglich sein.

### F-C2-03 – Knowledge Organization liefert nützliche Relationsarten, aber keine historische Wahrheit

SKOS unterscheidet u. a.:

- `broader` / `narrower`;
- `related`;
- `exactMatch`;
- `closeMatch`;
- `broadMatch` / `narrowMatch` / `relatedMatch`.

Besonders relevant ist, dass `closeMatch` bewusst nicht transitiv ist, während `exactMatch` deutlich stärkere Austauschbarkeit ausdrückt. Das illustriert eine Histo-Orla-Invariante:

> **„für Suche ähnlich genug“ ist nicht dasselbe wie „fachlich identisch“.**

SKOS/ISO 25964 sind deshalb gute Referenzen für kontrollierte Vokabular-/Mappinglogik, aber sie definieren weder mittelalterliche Herrschaftskategorien noch frühneuzeitliche Akteursbegriffe.

### F-C2-04 – Concept Discovery und Query Expansion müssen getrennte Outputs sein

Aus C2 und C7 folgt eine harte semantische Trennung:

#### Concept Discovery

Fragt:

- Welche fachwissenschaftlichen Problemmodelle könnten die Beobachtung erklären?
- Welche Begriffe sind konkurrierend, über-/untergeordnet, historisch begrenzt oder umstritten?
- Welche Quellengattungen/Methoden folgen daraus?

#### Query Expansion

Fragt:

- Welche Schreibweisen, Flexionsformen, OCR-Varianten, historische Wortformen, alternative Benennungen oder kontrollierten related terms sollen für einen konkreten Suchlauf zusätzlich verwendet werden?

Ein Begriff darf für Retrieval expandiert werden, ohne dass Histo-Orla behauptet, er sei fachlich äquivalent.

### F-C2-05 – Aktueller Standardsstatus spricht gegen voreilige technische Festlegung

ISO 25964-1:2011 ist im August 2026 weiterhin die publizierte aktuelle Ausgabe; eine zweite Edition liegt als **Final Draft International Standard** in der Approval-Phase vor. Part 2 von 2013 zur Interoperabilität ist ebenfalls publiziert, aber in Revision.

Das bestätigt die Lean-Entscheidung:

- Relations-/Mappingprinzipien aus etabliertem KO-SOTA nutzen;
- jetzt keine eigene Ontologie und keinen spezifischen Standard zum Requirement machen;
- konkrete Exchange-/Schemaentscheidung erst nach Capability/Architecture.

### F-C2-06 – Problemübersetzung braucht mehrere Kandidaten + Gründe + Warnungen

Für U1–U3 ist ein methodisch besseres Output-Muster als „gemeinter Fachbegriff“:

```text
Beobachtung / Nutzerformulierung
→ mögliche fachliche Problemklassen
→ pro Kandidat: warum einschlägig?
→ konkurrierende / benachbarte Modelle
→ historische Quellenbegriffe / Belege, soweit bekannt
→ moderne Analysebegriffe
→ archivische Recherchebegriffe
→ regionale / lateinische / Schreibvarianten
→ anachronistische oder problematische Gleichsetzungen
→ relevante Fachdomänen
→ passende Quellengattungen / Methoden
→ discriminating questions: Was müsste belegt sein, damit Modell A statt B passt?
```

Das ist eine **Research Translation Card**, keine ontologische Wahrheit.

## 5. Testfälle

### U1 „alter Teich / Sumpf / Wasserfläche“

Problemübersetzung darf nicht bei `Teich` stehenbleiben. Kandidaten/Anschlussbegriffe können je nach Befund u. a. sein:

- Teichwirtschaft / Fischerei / Besatz / Fischmeister;
- Teichbau / Damm / Flutbett / Wehr / Wasserbau;
- Fischwasser / Bachnutzung;
- Wasser-/Nutzungs-/Besitzrechte;
- Hutung/Trift/Grenze, wenn die Landschaftsfunktion konfliktbezogen ist;
- Mühlen-/Staukontext;
- Flur-/Guts-/Amts-/Kirchenbesitz;
- Niederung/Feuchtgebiet als moderne geomorphologische Beschreibung.

C1 hat gezeigt, dass unterschiedliche Funktionsbegriffe zu unterschiedlichen Archivserien führen.

### U2 „Vogt / abhängig / Beamter / Adliger?“

Kandidaten können Vogtei/Schutzvogtei, Ministerialität/Dienstmannschaft, Lehen, Grundherrschaft, Gerichtsherrschaft, Patronat, Amt/Funktionsrolle usw. umfassen. Diese Begriffe dürfen nicht als Synonyme behandelt werden. Discriminating evidence muss u. a. Zeit, Quelle, Rechts-/Herrschaftskontext und tatsächliche Relationsbelege prüfen.

### U3 „politische Loyalität / Lager?“

Statt moderner Lager-/Parteikategorie müssen je Situation Kandidaten wie Amt, Patronage/Klientel, Verwandtschaft, Lehns-/Besitzinteresse, Hofbindung, Konfession, Diplomatie-/Gesandtschaftsrolle, Militärdienst, regionale Herrschaftsverflechtung geprüft werden. Kein Kandidat ist automatisch Motiv.

## 6. Problem-Translation Method v0.1

### Schritt A – Beobachtung konservieren

Originale Nutzerformulierung unverändert halten. Noch keine fachliche Normalisierung als Wahrheit.

### Schritt B – Domain Routing Kandidaten

Welche Fachdomänen könnten die Beobachtung sinnvoll problematisieren?

### Schritt C – Concept Candidates

Mehrere fachliche Kandidaten mit:

- Kurzdefinition im aktuellen Research Context;
- zeitlich/räumlich/institutioneller Geltung;
- warum passend / warum möglicherweise nicht;
- verwandten und konkurrierenden Begriffen;
- typischen Quellen/Evidenzarten;
- typischen Fehlschlüssen.

### Schritt D – Terminology Layers

Für jeden relevanten Kandidaten nach Bedarf unterscheiden:

1. `user-language`
2. `source-term`
3. `contemporary-institutional/legal-term`
4. `archival-description/search-term`
5. `modern-analytical-term`
6. `historiographic-term`
7. `regional-term`
8. `foreign/latin-equivalent`
9. `orthographic/name/search-variant`

### Schritt E – Discriminating Questions

Nicht nur Begriffe erklären, sondern sagen, welche Evidenz die konkurrierenden Modelle auseinanderhalten würde.

### Schritt F – Retrieval Expansion getrennt erzeugen

Aus dem fachlichen Modell eine Suchstrategie ableiten, aber Search Expansions als solche kennzeichnen.

### Schritt G – verständliche Rückübersetzung

Dem Nutzer erklären, warum die Alltagssprache unzureichend sein kann und welche Modelle offen sind; Komplexität erklären, nicht ausblenden.

## 7. Evaluation / Gold-Case Design

Problem Translation lässt sich nicht sinnvoll nur mit „richtiger Begriff gefunden: ja/nein“ messen. Für U1–U3 braucht es Fachrubriken:

1. **Coverage:** wurden wesentliche plausible Fachmodelle erkannt?
2. **False equivalence:** wurden nicht-äquivalente Begriffe fälschlich synonymisiert?
3. **Anachronism control:** wurden zeit-/raumfremde Kategorien als passend ausgegeben?
4. **Layering:** sind Quellen-, Archiv-, Analyse- und Suchbegriffe unterscheidbar?
5. **Discriminating value:** liefert die Übersetzung Folgefragen/Quellen, die Modelle auseinanderhalten?
6. **Neighbor routing:** werden relevante Disziplinen/Quellengattungen aktiviert?
7. **Transparency:** kann Research Owner verstehen, warum ein Kandidat vorgeschlagen wurde?

Gold Cases sollten von Fachdomänen konstruiert/validiert werden und bewusst nahe, aber falsche Alternativen enthalten.

## 8. Capability Candidates

- `CAP-PROBLEM-TRANSLATION`: Nutzerbeobachtung in mehrere fachlich begründete Problemkandidaten übersetzen.
- `CAP-TERMINOLOGY-LAYERS`: historische/archivische/analytische/historiographische/search layers unterscheiden.
- `CAP-CONCEPT-VALIDITY`: zeitliche, regionale, institutionelle und fachliche Geltungsgrenzen sichtbar machen.
- `CAP-DISCRIMINATING-QUESTIONS`: konkurrierende Modelle durch nächste Belegfragen operationalisieren.
- `CAP-VOCABULARY-TO-SEARCH`: fachliches Concept Model kontrolliert in Retrieval-Expansion übersetzen.

## 9. Quality / Requirement Candidates

- REQ-C2-A: Problem Translation muss mehrere plausible Fachmodelle offenhalten können und darf keinen Einzelbegriff ohne Begründung als Wahrheit setzen.
- REQ-C2-B: Historischer Quellenbegriff, Archivbegriff, moderner Analysebegriff und Search Variant müssen unterscheidbar sein.
- REQ-C2-C: Begriffskandidaten müssen Geltungsgrenzen/Unsicherheit und typische Fehlgleichsetzungen abbilden können.
- REQ-C2-D: Query Expansion darf keine fachliche Synonymie implizieren.
- REQ-C2-E: Problem Translation muss gegen domänenspezifische Gold Cases evaluierbar sein, insbesondere auf Coverage, Anachronismus und False Equivalence.

## 10. Challenge interner Annahmen

#16/#19 werden im Kern bestätigt: Fachsprache/Begriffsmodelle sind Teil von Expertise. Korrigiert wird jedoch jede Tendenz zu einem zentralen „Begriffsnetz“ als voreilige Systemarchitektur. Der fachliche Need ist **relations- und geltungsbewusste Problem-/Terminologiearbeit**; Thesaurus/Ontologie/Graph sind spätere technische Optionen.

## 11. Open Questions / bounded debt

- Domänenspezifische Gold Cases müssen mit C3-Expertise Profiles gekoppelt werden.
- Regionale Fachvokabulare und konkrete Archivbegriffslisten entstehen problem-/quellenbezogen, nicht als vorab vollständiges Lexikon.
- Technische Repräsentation von Term Cards/Concept Relations bleibt #39/#41/#42 vorbehalten.

## 12. #45 Quality Check

- **Domain fit:** historische Semantik/Begriffsgeschichte und Fachdomänen führen; KO/IR kontrollieren die Informations-/Suchseite.
- **Evidence fit:** aktuelle Fachliteratur, offizielles DRW und etablierte KO-Standards wurden direkt geprüft.
- **Inference fit:** SKOS-/ISO-Relationen werden als Organisations-/IR-Referenz, nicht als historische Ontologie interpretiert.
- **Terminology fit:** Wort/Begriff/Diskurs sowie source/archive/analysis/search layers sind ausdrücklich getrennt.
- **Provenance fit:** Quellen und aktueller ISO-Reifestatus sind dokumentiert.
- **Falsification/challenge:** U1–U3 und geplante Gold Cases können false equivalence/anachronism sichtbar machen.

## 13. Sättigungsbegründung

Für Capability/Requirements ist die Kernfrage ausreichend beantwortet: SOTA aus historischer Semantik und Knowledge Organization konvergiert auf die Notwendigkeit, Begriffe relational, kontext- und geltungsbewusst statt als Synonymliste zu behandeln. Weitere Begriffsgeschichtsdebatten würden Fachprofile vertiefen, ändern aber die architecture-driving Invarianten derzeit nicht.
