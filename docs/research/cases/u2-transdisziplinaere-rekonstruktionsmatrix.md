# U2 / Orlagau – transdisziplinäre Rekonstruktionsmatrix für Lebenswelten

**Status:** `working-research / method-extension / requirement-candidate-source`  
**Work Owner:** #46  
**Methodische Owner/Schnittstellen:** #22 Kompetenzlandkarte, #45 Research Protocol  
**Fachschnittstelle:** #47 für eigenständige Landschafts-/Gewässerfragen  
**Requirements-Schnittstelle:** #41/#42; Live-Research-Befunde werden nur als Candidates geführt, bis Cross-Use-Case-/SOTA-Prüfung erfolgt  
**Stand:** 2026-08-31

---

## 1. Anlass und Korrektur

Der bisherige Quellenlauf hat einen realen methodischen Defekt sichtbar gemacht: Auch ein kontextreiches Urkundenexzerpt und eine Zeitscheibenmatrix können die Forschung noch **zu text-, ereignis- und herrschaftszentriert** verengen.

Für Histo-Orla ist das Forschungsziel nicht die Sammlung von Datenpunkten wie `Ort – Person – Datum – Rechtsgeschäft`, sondern die **quellenkritische Rekonstruktion historischer Lebenswelten und ihrer Veränderung**. Texte sind dafür eine zentrale Evidenzklasse, aber nicht die einzige und nicht automatisch die analytische Einheit.

Verbindliche Korrektur:

```text
Quellentreffer
→ Quellen-/Instanzkritik
→ historisches Situations-/Problem-Dossier
→ Expertise Routing
→ Evidenzbedarf je Fachdomäne
→ parallele textliche, materielle, räumliche, ökologische und institutionelle Evidenzgewinnung
→ disziplinspezifische Teilanalysen
→ Cross-Evidence-Abgleich / Widersprüche / Lücken
→ konkurrierende Erklärungen
→ transdisziplinäre Rekonstruktion der Lebenswelt
```

**Der Scope wird deshalb nicht vorschnell auf die im zuerst gefundenen Text enthaltenen Kategorien begrenzt.** Eine Urkunde kann z. B. `nimia paupertas` nennen, ohne die ökologischen, ökonomischen, sozialen, institutionellen oder politischen Ursachen dieser Armut zu erklären. Gerade diese Lücke erzeugt den nächsten fachlich gerouteten Forschungsauftrag.

---

## 2. Einheit der Forschung: historisches Situations-/Problem-Dossier

Die primäre analytische Einheit ist künftig dort, wo eine Frage mehrere Evidenzlogiken berührt, ein `situation_dossier`, nicht ein einzelner Text.

Ein Dossier hält mindestens auseinander:

```text
dossier_id
anchor_question
anchor_sources / excerpts
period / phase
spatial_scales
actors / groups / institutions
rights / dependencies / obligations
resources / economy / labour
natural_environment / land-use / hydrology
settlement / built_environment / infrastructure
religious_worldview / liturgy / memoria
social_order / gender / kinship / household
mobility / markets / communication
conflict / coercion / risk / disaster candidates
material_culture / objects / images / burial
known observations
competing explanations
activated disciplines
required evidence by discipline
coverage / evidence-starvation state
contradictions / unresolved
next discriminating actions
```

Ein Dossier ist **keine fertige Gesamterzählung**. Es ist ein kontrollierter Arbeitsraum, in dem verschiedene Fachdomänen dieselbe historische Situation aus unterschiedlichen Evidenztypen untersuchen können, ohne ihre Methoden zu verschmelzen.

---

## 3. Welche Kompetenzen müssen „mit im Boot“ sein – und welches Futter brauchen sie?

Nicht jede Kompetenz wird bei jedem Dossier aktiviert. Sobald die Fragestellung ihre Evidenzlogik berührt, muss aber sichtbar werden, **was sie für eine belastbare Aussage benötigt** und was sie aus dem vorhandenen Material gerade nicht beurteilen kann.

| Kompetenz / Linse | Leitfragen an die Rekonstruktion | Benötigte Evidenz / Quellenfamilien | Typische unzulässige Verkürzung |
|---|---|---|---|
| **Diplomatik / Editionswissenschaft / historische Philologie** | Was sagt das konkrete Stück? Welche Formel ist individuell, welche gattungstypisch? Wie sicher sind Datum, Wortlaut, Überlieferung und Semantik? | Original/Kopie/Kopiar/Transsumpt, Edition/Apparat, Parallelurkunden, Formelvergleich, Sprach-/Begriffsgeschichte | Arenga oder `paupertas` unmittelbar als vollständige psychologische/kausale Erklärung lesen |
| **Archivistik / Provenienz / Registraturkunde** | Warum wurde die Information erzeugt und bewahrt? Welche Serien fehlen außerhalb des Urkundenbuchs? | Bestände, Findmittel, Kopiare, Rechnungen, Amts-/Klosterregistraturen, Memorial-/Visitations-/Prozessserien | vorhandenes Editionskorpus = historisch vollständige Überlieferung |
| **Mediävistik / Landes-, Herrschafts-, Rechts- und Verfassungsgeschichte** | Welche Rechte bestehen gleichzeitig? Wer kann worüber verfügen, richten, schützen, besteuern, bevogten, belehnen? | Urkunden, Lehnbücher, Gerichts-/Vogtei-/Patronatsbelege, Besitzserien, Herrschaftsteilungen | aus Zeugenstatus oder Ortsnähe eine geschlossene Territorialherrschaft ableiten |
| **Kirchen-, Kloster- und Ordensgeschichte** | Was für eine geistliche Institution ist der Konvent? Wem untersteht er? Welche Stiftungs-, Reform-, Versorgungs- und Patronatslogik gilt? | Gründungs-/Bestätigungsurkunden, Ordens-/Regelkontext, Diözesanakten, Visitations-/Konventsüberlieferung, päpstliche/bischöfliche Akten | `Kloster` als zeitlos einheitliche Institution behandeln |
| **Theologie / Liturgie / Frömmigkeits- und Memoriaforschung** | Welche religiösen Ziele, Pflichten und Deutungen strukturieren Handlungen? Welche Liturgien, Heiligenkulte, Memorialleistungen oder Seelsorgefunktionen sind materiell finanziert? | liturgische Bücher, Nekrologe/Obituare, Stiftungen, Altäre/Patrozinien, Anniversarien, theologische/normative Texte, Weihe-/Reliquienkontexte | religiöse Sprache nur als dekorative Formel oder umgekehrt als alleinige Ursache lesen |
| **Sozialgeschichte / historische Anthropologie / Europäische Ethnologie** | Wie lebten Gruppen tatsächlich? Welche Abhängigkeiten, Normen, Praktiken, Konflikte und sozialen Hierarchien prägten den Alltag? | Rechts- und Konfliktquellen, Abgaben/Dienste, Haushalts-/Versorgungsindikatoren, Sachkultur, Vergleichsmilieus | Elitenurkunde als vollständiges Abbild gesellschaftlicher Praxis behandeln |
| **Geschlechter-, Familien-, Verwandtschafts- und Haushaltsgeschichte** | Wer konnte eintreten, stiften, erben, verzichten, versorgt werden? Welche Rolle haben Familie, Ehe, Witwenstand und soziale Reproduktion? | Dotal-/Erb-/Stiftungsurkunden, Nekrologe, Prosopographie, Familiennetzwerke, Besitzfolgen | Frauenkonvent nur als religiösen Rückzugsort oder nur als Emanzipationsraum setzen |
| **Wirtschafts- und Agrargeschichte** | Woraus lebt die Institution? Wie groß sind Endowment, Renten, Zehnten, Naturalabgaben, Arbeitskräfte, Marktanbindung, Kosten und Risiken? | Urbare, Zins-/Rentenlisten, Rechnungen, Zehnt-/Patronatsrechte, Kauf-/Tauschserien, Mühlen, Markt-/Zollbelege, Ertragsindikatoren | `Armut` ohne Ressourcenbilanz kausal erklären |
| **historische Demographie** | Wie groß sind Konvent, Siedlung, abhängige Bevölkerung und Arbeitsbasis? Gibt es Hinweise auf Wachstum, Schrumpfung, Mortalität oder Migration? | Personenlisten, Memorialbücher, Steuer-/Zinsregister, Siedlungsarchäologie, spätere serielle Vergleichsdaten | fehlende Namenslisten = kleine Bevölkerung |
| **historische Geographie / Kulturlandschaftsforschung** | Welche Lagequalitäten, Wege, Märkte, Relief-, Boden-, Gewässer- und Nutzungsräume prägen Handlungsmöglichkeiten? | historische Karten/Risse, Topographie, Wege, Einzugsräume, Flur-/Besitzmuster, GIS, Orts-/Flurnamen, Vergleichsräume | moderne Gemeindegrenzen oder Luftlinie als historischen Raum benutzen |
| **Umweltgeschichte / historische Ökologie / Hydrologie / Klima- und Katastrophengeschichte** | Gab es Ressourcenengpässe oder Umweltstress? Welche Rolle spielten Boden, Wasser, Wetterextreme, Überschwemmung, Dürre, Feuer oder Seuchen? | zeitgenössische Berichte, Rechnungs-/Ertragsserien, Pollen/Sedimente, Dendro-/Klimaproxies, Gewässer-/Bodenbefunde, archäologische Schadenshorizonte | aus heutiger Landschaft oder allgemeiner Klimakurve eine lokale Ursache ableiten |
| **Mittelalter-, Siedlungs- und Landschaftsarchäologie / Geoarchäologie** | Wo lag die Institution genau? Welche Bau-/Nutzungsphasen, Verlagerungen, Produktions-/Entsorgungsbereiche und Siedlungsbeziehungen existierten? | Grabungsberichte, Befundpläne, Keramik/Datierungen, geophysikalische Prospektion, LiDAR, Boden-/Sedimentbefunde | schriftliche Ersterwähnung = Entstehung; heutiger Ort = mittelalterlicher Standort |
| **Bau- und Architekturgeschichte / Bauforschung / Denkmalpflege** | Welche Gebäude und Raumordnungen bestanden? Was sagen Bauphasen, Materialien, Funktionsräume, Kirche/Klausur/Infrastruktur über Ressourcen und Lebensform? | aufgehendes Mauerwerk, Bauaufnahme, Baufugen, Dendrochronologie, Stein-/Holzmaterial, ältere Pläne/Ansichten, Denkmalinventare | späterer Kirchenbau als unverändertes Bild des 13. Jh. verwenden |
| **Kunstgeschichte / Bild-, Objekt- und Sachkulturforschung** | Welche Stifter-, Status-, Kult- und Identitätsaussagen stecken in Ausstattung, Siegeln, Grabmälern, Reliquien, Bildern und liturgischen Objekten? | Inventare, erhaltene Objekte, Siegel, Grabplatten, Skulptur/Malerei, Patrozinien, Provenienzen | Objekt ohne Datierung/Provenienz dem frühen Konvent zuschreiben |
| **Onomastik / Toponymie / Sprachgeschichte** | Welche Namen bewahren Siedlungs-, Landschafts-, Besitz- oder Funktionsspuren? | historische Namensformen, Ortsnamenbücher, Flurnamen, Gewässernamen, Sprachvergleich | Namensähnlichkeit = Identität oder direkte Siedlungsdatierung |
| **Prosopographie / historische Netzwerkforschung / Mobilitätsgeschichte** | Wer vermittelt Ressourcen und Entscheidungen? Welche Familien-, Amts-, geistlichen, Handels- oder Reiseverbindungen tragen die Institution? | Zeugen-, Stifter-, Konvents-, Amts- und Verwandtschaftsserien; Reise-/Urkundungsorte | gemeinsame Zeugenliste = enge persönliche Beziehung |
| **Militär-, Konflikt- und Sicherheitsgeschichte** | Behindern Krieg, Fehde, Befestigung, Gewalt oder Unsicherheit Produktion, Mobilität, Rechtsdurchsetzung oder institutionelle Existenz? | Fehde-/Schadens-/Schlichtungsquellen, Befestigungsarchäologie, Chroniken, Gerichts-/Delegationsakte | zeitgleicher Krieg = automatisch Ursache lokalen Niedergangs |
| **Historiographie / Forschungsgeschichte** | Welche ältere Erzählung strukturiert unsere Fragen bereits? Welche Kategorien wurden revidiert? | ältere Regionalgeschichte, neuere Kritik, Spezialliteratur, Vergleichsdebatten | ältere Landesgeschichtsschreibung als neutrale Faktenablage benutzen |

### Mindestvertrag je aktivierter Kompetenz

Für ein aktives Dossier muss eine Kompetenz nicht nur als Label erscheinen. Sie muss mindestens liefern können:

```text
question_from_this_discipline
concepts / terminology needed
source_or_material_classes_needed
search vocabulary / archive vocabulary
method / comparison logic
allowed inference
known blind spots / preservation bias
what would discriminate competing explanations
what would falsify or weaken the current model
coverage status: evidence-rich | partial | evidence-starved | not-assessable
```

Damit wird **Expertise Routing zu Evidence Routing**. Ein System, das nur sagt „hier braucht man Umweltgeschichte und Archäologie“, hat die wissenschaftliche Arbeit noch nicht geleistet.

---

## 4. Pilotfall Triptis 1212: von `nimia paupertas` zur Forschungsagenda

### 4.1 Sicherer Ausgangspunkt

NHUB II Nr. 8, 14. Mai 1212, berichtet, dass Markgraf Dietrich von Meißen einen Frauenkonvent von Triptis nach Zwickau verlegte, `ob nimiam paupertatem, quam patiebantur ibidem`; die übertragenen Kirchen und Einkünfte sollten der `sustentatio` dienen. Hartmann von Lobdeburg und sein Bruder Hermann erscheinen im Zeugenverband.

**Direkt belegt ist damit:**

- ein Frauenkonvent in Triptis vor/um 1212;
- in der Quelle ausdrücklich behauptete erhebliche Armut am Triptiser Standort;
- Verlegung nach Zwickau;
- kirchliche Einkünfte als Mittel institutioneller Versorgung;
- markgräfliches, bischöfliches und klösterliches Handeln im Rechtsgeschäft;
- Lobdeburger Präsenz im hochrangigen Zeugenmilieu.

**Nicht direkt belegt ist die Ursache der Armut.**

### 4.2 Konkurrierende Erklärungsfamilien – alle zunächst `hypothesis-to-test`

| Hypothese | Welche Kompetenz führt? | Was müsste gesucht werden? | Was würde sie schwächen? |
|---|---|---|---|
| **H-T-01: zu kleine/fehlerhafte Erstausstattung** | Kloster-, Rechts-, Wirtschafts-, Herrschaftsgeschichte | frühere Stiftung/Bestätigung, Güter-/Zehnt-/Patronatsausstattung, spätere Nachstiftungen, Besitzverluste | nachweislich ausreichende und realisierbare Einkünfte vor 1212 |
| **H-T-02: geringe reale Produktivität / Ressourcenschwäche** | Agrargeschichte, historische Geographie, Umwelt-/Geoarchäologie | Böden, Nutzflächen, Wasser, Ertrag/Abgaben, Siedlungsdichte, Landschaftsrekonstruktion | gute Ressourcenausstattung plus andere konkrete Verlustursache |
| **H-T-03: ungünstige Markt-/Verkehrs- und Versorgungsanbindung** | Wirtschafts-, Verkehrs-/Mobilitätsgeschichte, historische Geographie | Wege, Marktorte, Zoll/Geleit, Distanz zu Besitzungen, Zwickau-Vergleich | dichte lokale Märkte/Verkehrsnetze und problemlose Versorgung |
| **H-T-04: Konflikt, Gewalt oder politische Instabilität** | Konflikt-/Militär-/Herrschaftsgeschichte | Fehden, Schäden, Rechtsstreit, Schutz-/Befestigungsmaßnahmen, Reise-/Gerichtsstörungen | keine passende lokale Konfliktlage und stabile Besitznutzung |
| **H-T-05: Naturereignis / Umweltkrise** | Umwelt-/Klima-/Katastrophengeschichte, Archäologie | lokale Schadenshorizonte, Chroniken, Dendro-/Klima-/Sedimentindikatoren, Ertrags-/Preisreaktionen | fehlende lokale Koinzidenz oder zeitliche Fehlpassung |
| **H-T-06: soziale/demographische oder interne Versorgungsbelastung** | Sozial-/Demographie-/Gender-/Klostergeschichte | Konventsgröße, Aufnahme-/Versorgungspflichten, abhängige Personen, Memorial-/Familiennetz | kleine stabile Gemeinschaft mit ausreichender Ausstattung |
| **H-T-07: institutionell-rechtliche Abhängigkeiten entziehen Ressourcen** | Rechts-, Kirchen-, Patronats-, Herrschaftsgeschichte | Vogtei, Zehntrechte, Patronat, Abgaben, Schutzleistungen, konkurrierende Anspruchsträger | weitgehende Verfügungshoheit ohne erkennbare Belastungen |
| **H-T-08: Verlegung ist zugleich strategische institutionelle Neuordnung** | Kloster-/Kirchen-, Stadt-, Herrschafts-, Wirtschafts- und Netzwerkgeschichte | Zwickauer Aufnahmebedingungen, neue Einkünfte, Markt/Urbanität, Stifter-/Patronatsnetz, vergleichbare Transfers | Verlegung ohne strukturelle Verbesserung oder nur kurzfristige Nothilfe |
| **H-T-09: religiöse/reformbezogene Gründe wirken zusätzlich** | Theologie, Liturgie, Ordens-/Kirchengeschichte | institutionelle Zugehörigkeit, Regel, Reformbewegungen, bischöfliche/päpstliche Vorgaben, geistliche Netzwerke | keinerlei zeitgenössische institutionelle/reformbezogene Anhaltspunkte |

Diese Hypothesen sind **nicht vollständig und nicht gleich wahrscheinlich**. Die Matrix verhindert lediglich, dass die erste plausible Erklärung zur stillen Wahrheit wird.

### 4.3 Rekonstruktionsfragen zur Lebenswelt des Konvents

Für Triptis genügt künftig nicht `Konvent – arm – 1212 verlegt`. Zu rekonstruieren ist, soweit die Evidenz reicht:

- **Standort:** Wo genau lag der Konvent? Relation zu Siedlung, Kirche, Burg/Herrensitz, Wasser, Wegen, Acker-/Wiesen-/Waldflächen?
- **Gebäude:** Welche Kirche/Klausur/Wirtschaftsbauten gab es? Welche Kapazität und Bauphasen?
- **Gemeinschaft:** Welche geistliche Lebensform, welcher Regel-/Ordenskontext, wie viele Frauen, welche Herkunfts- und Familienmilieus?
- **Versorgung:** Welche Güter, Renten, Zehnten, Arbeitsleistungen, Mühlen, Gärten, Vieh-/Weide-/Holz-/Wasserrechte standen zur Verfügung?
- **Alltag und Materialität:** Ernährung, Arbeit, Kleidung, liturgische Ausstattung, Handwerk, Räume, Bestattung – soweit archäologisch/objektgeschichtlich fassbar.
- **Religiöse Funktion:** Gebet, Memoria, Liturgie, Patronate, mögliche Seelsorge-/Stiftungsfunktionen; was wurde von wem erwartet?
- **Macht und Abhängigkeit:** Wer schützte, bevogtete, bestätigte, besteuerte oder konnte Besitz disponieren? Welche Handlungsspielräume hatten Konvent und einzelne Frauen?
- **Umwelt:** Welche Nutzbarkeit und Risiken hatte die lokale Landschaft? Welche Aussagen sind tatsächlich historisch/proxybasiert und welche nur heutige Plausibilität?
- **Netzwerke/Mobilität:** Beziehungen zu Meißen, Naumburg, Bosau, Lobdeburg, Zwickau, Familien/Stiftern, Märkten und Verkehrswegen.
- **Krise und Verlegung:** Was änderte sich unmittelbar vor 1212, was nach der Verlegung? Welche Ressourcen kamen neu hinzu und welche blieben zurück?

Erst die Verbindung dieser Ebenen erlaubt ein **Greifbarwerden historischer Lebenswelt**, ohne die Lücken mit Erzählung zu füllen.

---

## 5. Suchinventar erweitern: vom Keyword-Inventar zur Evidence-Demand-/Coverage-Matrix

Das bisherige Master-Suchinventar für Orte, Varianten, Personen und Sachbegriffe bleibt notwendig, reicht aber für Rekonstruktion nicht aus. Es bekommt eine zweite, orthogonale Ebene.

### 5.1 Neues Arbeitsinstrument: Evidence Demand / Coverage Register

Für jedes Dossier und jede relevante Hypothese wird geführt:

```text
dossier_id
research_question
competing_hypothesis_id
discipline
required_evidence
source_or_material_class
historical_search_terms
archival_search_terms
modern_scholarly_terms
repositories / archives / collections / databases
time_range
spatial_scale
expected_discriminating_signal
detectability / preservation / taphonomic limits
source_identity_status
inspected_instances / source_ids
positive / negative / unresolved result
search_boundary
impact_on_hypothesis
next_action
```

Das Source Ledger bleibt kanonischer Ort für **Quellenidentität**. Diese Matrix besitzt dagegen die Frage: **Haben wir überhaupt das fachlich benötigte Evidenzspektrum gesucht und in welcher Tiefe?**

### 5.2 Quellen-/Materialklassen, die der Suchplan aktiv routen können muss

Je Dossier problemabhängig mindestens prüfbar:

- Urkunden, Regesten, Kopiare, Lehnbücher;
- Kloster-/Stifts-/Ordensüberlieferung, Statuten/Regeln, päpstliche/bischöfliche Akten;
- Nekrologe, Obituare, Memorial- und liturgische Quellen;
- Urbare, Zins-/Zehntregister, Rechnungen, Käufe/Tausche, Markt-/Zoll-/Geleitquellen;
- Gerichts-, Streit-, Fehde-, Schadens-, Schlichtungs- und Schutzquellen;
- Pfarr-/Patronats-/Visitations- und Kirchenrechnungen;
- Karten, Grenz-/Forst-/Flur-/Guts-/Hutungsrisse, Kataster, Gelände-/Wegeinformation;
- Orts-, Flur-, Gewässernamen;
- archäologische Grabungs-/Prospektionsberichte, Fundinventare, Datierungen, LiDAR/Geophysik;
- Bauaufnahme, Bauforschung, Dendrochronologie, Denkmalinventare, historische Ansichten/Pläne;
- Kunst-/Sachkultur-, Siegel-, Grabmal-, Reliquien- und Ausstattungsinventare;
- paläoökologische, geoarchäologische, hydrologische und lokale Klima-/Katastrophenproxies;
- demographische/personelle Serien, Prosopographie, Stifter-/Verwandtschaftsnetze;
- narrative Quellen/Chroniken nur mit quellenkritischer Funktionsprüfung;
- Forschungsliteratur zu Institution, Region, Methode und Vergleichsfällen.

### 5.3 Literaturanalyse nicht als ein einziger „Review“

Für komplexe Rekonstruktionsdossiers werden mindestens folgende **Review-Lanes** unterschieden:

1. **Historiographie-/Kontroversen-Lane** – ältere Meistererzählungen, Revisionen, Begriffs- und Forschungstraditionen.
2. **Regional-/Institutionen-SOTA-Lane** – aktueller Forschungsstand zu Triptis, Orla, Lobdeburg, geistlichen Frauenkommunitäten usw.
3. **Methoden-Lane je Fachdomäne** – z. B. Monastic Archaeology, historische Ökologie, Bauarchäologie, Memoriaforschung: Welche Evidenz trägt welche Schlussart?
4. **Source-/Archive-Discovery-Lane** – Editionen, Bestände, Serien, Findmittel, Digitalisate und Überlieferungslücken.
5. **Vergleichs-/Comparanda-Lane** – nur historisch/methodisch passende andere Konvente, Siedlungen oder Krisenfälle; Vergleich dient der Hypothesenbildung/-prüfung, nicht dem Ersatz lokaler Evidenz.
6. **Material-/Umwelt-/Raum-Lane** – archäologische, geographische, bauhistorische, kunsthistorische und naturwissenschaftliche Fachpublikationen/Daten.

Sättigung wird pro Lane und Forschungsfrage begründet. Eine gut gesättigte Urkundenrecherche kompensiert **nicht** fehlende archäologische oder wirtschaftsgeschichtliche Evidenz, wenn gerade diese für die Kausalfrage erforderlich ist.

---

## 6. Methodischer Ablauf und Abhängigkeiten

### Gate 0 – Anchor / Source Identity

- konkreten Ausgangsbefund verifizieren;
- Original/Überlieferung/Edition/Instanz/Fundstelle sichern;
- explizite Quelle von editorischem und eigenem Schluss trennen.

**Abhängigkeit:** Ohne Gate 0 keine consequential Kausalanalyse.

### Gate 1 – Zeit-/Raum-/Entitätsauflösung

- betroffene Orte/Standorte/Institutionen/Personen identifizieren;
- Zeitphase statt unscharfer Jahrhundertprojektion;
- historische Raumskalen und Rechte trennen.

**Abhängigkeit:** Umwelt-, Bau- und Archäologieevidenz ist wertlos, wenn sie dem falschen Standort oder der falschen Phase zugeordnet wird.

### Gate 2 – Expertise Routing → Evidence Demand

- relevante Fachdomänen aktivieren;
- je Domäne Frage, Evidenzbedarf, Methode, Suchvokabular und Inferenzgrenze formulieren;
- `evidence-starved` ausdrücklich zulassen.

### Gate 3 – Parallele Evidenzgewinnung

Nach Gate 0/1 können viele Stränge parallel laufen: Archiv/Literatur, Archäologie, Bau/Kunst, Umwelt, Ökonomie, Theologie/Liturgie, Prosopographie usw. Ergebnisse bleiben fachlich getrennt.

### Gate 4 – Disziplinspezifische Mikroanalyse

Jede Domäne prüft ihre Evidenz nach eigenem Standard. Keine transdisziplinäre Synthese darf schwache domänenspezifische Evidenz durch Plausibilität „auffüllen“.

### Gate 5 – Cross-Evidence Alignment

Abgleichen:

- gleiche/abweichende Datierung;
- gleicher/anderer Raum;
- gleiche/abhängige Quelleninformation;
- Kompatibilität oder Widerspruch zwischen Text, Material, Umwelt, Raum und Institution;
- Preservation-/Taphonomy-/Überlieferungsbias.

### Gate 6 – Kausales Hypothesentesten

Explizite Quellenmotivation, beobachtbare Konstellation und historische Kausalerklärung bleiben getrennt. Competing hypotheses werden mit **diskriminierender Evidenz** getestet, nicht nach erzählerischer Plausibilität ausgewählt.

### Gate 7 – Lebenswelt-Rekonstruktion

Das Syntheseprodukt enthält je Dimension:

```text
reconstructed_dimension
status: direct | strongly-supported-inference | competing | unknown
supporting evidence across disciplines
counterevidence / limits
spatial scope
period / phase
confidence / maturity
```

### Gate 8 – Systemlernen / Requirements

Erst jetzt wird geprüft, welche beobachtete Friktion eine Capability-/Quality-/Requirement-Änderung begründet. Ein historischer Einzelfall wird nicht als Technologieanforderung getarnt.

---

## 7. Requirement Candidates aus diesem Stressfall

Die folgenden Candidates sind **noch keine akzeptierten Requirements**. Zuerst ist zu prüfen, ob sie bereits durch #41/#42 hinreichend abgedeckt sind, nur stärkere Acceptance Criteria benötigen oder tatsächlich eine Baseline-Erweiterung rechtfertigen.

### RC-U2-09 – Expertise Routing muss Evidence Demand erzeugen

**Observed pain:** Eine bloße Liste aktivierter Disziplinen verhindert nicht, dass die Materialsammlung faktisch wieder text-/ereigniszentriert bleibt.

**Candidate:** Bei consequential transdisziplinären Fragen muss Expertise Routing je aktiver Domäne mindestens benötigte Evidenzklassen, Methoden, Suchvokabular, zulässige Schlussarten und Evidenzlücken erzeugen.

**Likely relation:** Verschärfung/Operationalisierung von CAP-02 und REQ-EPI-001, nicht zwingend neues Top-Level-Requirement.

### RC-U2-10 – Historische Situation ist cross-media, nicht text-only

**Candidate:** Ein historisches Situationsdossier muss textliche, materielle, archäologische, räumliche, bau-/kunsthistorische und Umwelt-Evidenz als getrennte Klassen an derselben historischen Frage ausrichten können, ohne sie epistemisch zu flatten.

**Likely relation:** Historical Situation Analysis / Transdisciplinary Synthesis + Domain Non-flattening.

### RC-U2-11 – Search Coverage wird nach Evidenzbedarf gemessen

**Candidate:** Suchvollständigkeit/Sättigung darf bei transdisziplinären Fragen nicht allein über Suchbegriffe oder Textcorpora bestimmt werden; Coverage muss gegen die aktivierten fachlichen Evidence Demands und deren Search Boundaries sichtbar sein.

**Likely relation:** CAP-03/CAP-07 + REQ-SRC-005; neue Acceptance Dimension.

### RC-U2-12 – Kausalerklärungen benötigen konkurrierende Modelle

**Candidate:** Ein consequential `warum`-Claim muss explizite Quellenaussage, beobachtbare Konstellation und konkurrierende historische Kausalhypothesen trennen und die jeweils diskriminierende Evidenz dokumentieren.

**Likely relation:** Evidence Layering / Discrepancy / Historical Situation Analysis; ggf. Requirement-Erweiterung.

### RC-U2-13 – Evidence-starved ist ein eigener fachlicher Zustand

**Candidate:** Wenn eine aktivierte Disziplin für eine relevante Teilfrage keine hinreichende Evidenz besitzt, muss `evidence-starved / not-assessable` persistierbar sein; die Synthese darf die Lücke nicht mit anderen Evidenzklassen kaschieren.

**Likely relation:** REQ-EPI-004 Unsicherheit/Nichtwissen + Expertise Routing; Acceptance-Erweiterung.

### RC-U2-14 – Multi-scale / phase alignment vor Cross-Evidence-Synthese

**Candidate:** Cross-Evidence-Claims müssen explizite Zeitphase und Raumskala besitzen; Site, Dorf, Besitzkomplex, Herrschaftsraum und Region sowie Bauphase, Ereignis und Zeitscheibe dürfen nicht still gleichgesetzt werden.

**Likely relation:** Multi-Scale Context + REQ-EPI-003.

### RC-U2-15 – Negative Befunde berücksichtigen Detectability und Preservation Bias

**Candidate:** Für archäologische, bauliche, ökologische und objektbezogene Negative Findings reicht eine textliche Search Boundary nicht; Nachweisbarkeit, Erhaltungsbedingungen, Grabungs-/Prospektionsabdeckung und Taphonomie müssen Teil der Grenze sein.

**Likely relation:** CAP-07 Search Boundary; fachliche Erweiterung jenseits reiner Retrievalgrenzen.

### RC-U2-16 – Lebenswelt-Rekonstruktion braucht dimensionale Evidenztraceability

**Candidate:** Ein synthetischer Lebenswelt-Befund muss pro Dimension sichtbar machen, was direkt, inferiert, konkurrierend oder unbekannt ist und auf welche disziplinspezifischen Evidenzen er zurückgeht.

**Likely relation:** CAP-08 Evidence Layering, Human-readable Audit, Transdisciplinary Synthesis.

### RC-U2-17 – Literatur-/SOTA-Prozess benötigt methodenspezifische Review-Lanes

**Candidate:** Für transdisziplinäre Dossiers muss die Literaturarbeit getrennte historiographische, regionale, methodische, source-discovery-, comparative und material/environmental Review-Lanes unterstützen, statt eine flache Trefferliste als „Literaturanalyse“ zu behandeln.

**Likely relation:** CAP-01/CAP-02/CAP-03; #45-Suchstrategie; möglicherweise Workflow-/Acceptance-Erweiterung.

### RC-U2-18 – Folgequellen entstehen aus fachlichen Erklärungslücken

**Candidate:** Aus einem Quellenexzerpt müssen Folgeabfragen nicht nur über darin genannte Namen/Orte, sondern über fachlich erkannte Erklärungslücken erzeugt werden können, z. B. `paupertas` → Endowment/Ertrag/Umwelt/Versorgung/Abhängigkeiten/Institution/Materialität.

**Likely relation:** Professional Problem Translation + Expertise Routing + Source Discovery.

---

## 8. Sofortige Forschungsqueue – Pilot Triptis und Übertragung auf U2

### Triptis 1212

1. Quellen-/Überlieferungskette NHUB II Nr. 8 vollständig sichern.
2. Institutionelle Identität und Typ des Triptiser Frauenkonvents auflösen; alle älteren/späteren Bezeichnungen und Überlieferungsketten erfassen.
3. Besitz-/Endowment-/Einkommensdossier vor 1212 und für die Zwickauer Neuordnung aufbauen.
4. Bau-/Standort-/Archäologie-/Denkmal-/Kunstinventar für den möglichen Triptiser Konventstandort ermitteln; Standortstatus ausdrücklich `confirmed/candidate/unresolved`.
5. historische Geographie des lokalen Versorgungsraums: Wege, Märkte, Wasser, Nutzflächen, Siedlungsstruktur – quellen-/datenbasiert, nicht aus heutiger Karte rückprojiziert.
6. Umwelt-/Krisenspuren um die relevante Phase nur über lokal/zeitlich passende Evidenz prüfen; keine Naturkatastrophe aus Allgemeinwissen ergänzen.
7. Konvents-/Gender-/Familien-/Stifternetz sowie Lobdeburg–Meißen–Naumburg–Bosau–Zwickau-Verflechtung prosopographisch und rechtlich trennen.
8. religiös-liturgische Funktion, Patrozinien, Memoria und institutionelle Erwartungen erschließen.
9. Hypothesen H-T-01…09 nach diskriminierender Evidenz neu gewichten; `unresolved` zulassen.
10. erst danach eine erste `Lebenswelt Triptiser Konvent um 1212`-Rekonstruktion formulieren.

### Übertragung auf weitere U2-Dossiers

Dasselbe Verfahren wird anschließend problemabhängig auf Schleiz/Deutschorden, Lobdeburg-Arnshaugk, Mönchgrün, Moxa, Triptis/Auma/Ziegenrück/Arnshaug und die Knau-/Orla-Siedlungsfragen angewendet. Nicht jede Dimension ist überall gleich wichtig; die **Aktivierung folgt der Forschungsfrage**.

Die eigenständige historische Teich-/Feuchtlandschaft bleibt Work Owner #47. Wenn jedoch ein U2-Situationsdossier Wasser-, Boden-, Mühlen-, Nutzungs- oder Umweltbedingungen zur Erklärung benötigt, verweist es auf dortige Evidenz bzw. erzeugt einen sauber abgegrenzten Cross-Case-Research Hook statt dieselbe Evidenz doppelt zu besitzen.

---

## 9. Definition of Done für ein transdisziplinäres Situationsdossier

Ein Dossier ist nicht `reviewable`, nur weil die zentrale Urkunde verstanden ist. Mindestens:

- [ ] Anchor-Quellenidentität und Fundstellen belastbar;
- [ ] explizite Aussage vs. Kausalerklärung getrennt;
- [ ] historische Zeit-/Raum-/Entitätsebene geklärt oder bounded unresolved;
- [ ] führende und kontrollierende Fachdomänen geroutet;
- [ ] je aktiver Domäne Evidence Demand + Method + Inference Limit dokumentiert;
- [ ] textliche und nichttextliche Evidenzklassen problemangemessen geprüft;
- [ ] Literature-/SOTA-Coverage je notwendiger Lane dokumentiert;
- [ ] Search Boundaries einschließlich Preservation/Detectability, wo einschlägig;
- [ ] konkurrierende Erklärungen und diskriminierende Tests sichtbar;
- [ ] Cross-Evidence-Abhängigkeiten/Widersprüche geprüft;
- [ ] `evidence-starved`, `unknown` und `unresolved` zulässig und sichtbar;
- [ ] Lebenswelt-Synthese pro Dimension auf konkrete Evidenz rückführbar;
- [ ] Requirement Candidates von historischen Findings getrennt;
- [ ] nächster diskriminierender Forschungsschritt dokumentiert.

---

## 10. Leitregel

> **Eine historische Quelle gibt uns einen Blick auf eine Lebenswelt; sie definiert nicht deren vollständigen Scope.**

Transdisziplinäre Forschung bedeutet deshalb nicht, nach der Textanalyse mehrere Fachbegriffe an dieselbe Zusammenfassung zu hängen. Sie bedeutet, dass die beteiligten Disziplinen **bereits bestimmen, welches Material gesammelt werden muss**, welche Erklärung überhaupt zulässig ist, welche Blindstellen bleiben und welche zusätzliche Evidenz eine historische Rekonstruktion tragen oder falsifizieren kann.
