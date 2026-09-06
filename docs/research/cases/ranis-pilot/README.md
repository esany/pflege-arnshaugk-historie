# Ranis Pilot – geschichtetes Archiv

**Status:** `pilot / working-research / branch-isolated / no-main-authority`  
**Work Owner:** #85  
**Branch:** `pilot/ranis-layered-archive-20260906`  
**Methodik:** #45, `docs/research/source-identity-protocol.md`; fachliche Methoden nur soweit im konkreten Slice tatsächlich angewandt  
**Stand:** 2026-09-06

## 5-Minuten-Handoff

### Worum geht es?

Ranis wird hier als **historischer und archäologischer Forschungsfall** behandelt, nicht als Vermittlungs- oder Besucherprojekt. Der Branch prüft an einem realen Gegenstand, ob Histo-Orla heterogene Evidenz aus Altgrabung, Neugrabung, Archäologie, Naturwissenschaft, Forschungsgeschichte, Schriftquellen und Feldmaterial quellenkritisch in einen restartbaren Research State überführen kann.

Eine spätere Darstellung für Besuch, Museum oder Öffentlichkeit wäre höchstens eine abgeleitete View. Sie besitzt keine eigene Research Truth und definiert nicht die Forschungsfrage.

### Aktive Forschungsfrage v0.2

> **Wie lässt sich die paläolithische Nutzung der Ilsenhöhle in Ranis aus der Kombination von Hülle-Altgrabung und Neugrabung 2016–2022 belastbar rekonstruieren, und welche Aussagen hängen von der nachträglichen Korrelation unterschiedlicher Evidenzachsen ab?**

Unterfragen:

1. Welche stratigraphischen Einheiten der Alt- und Neugrabung lassen sich tatsächlich miteinander korrelieren?
2. Welche menschlichen, lithischen und faunistischen Funde gehören mit welcher Sicherheit in die LRJ-Horizonte?
3. Welche Aussagen beruhen auf direktem archäologischem Befund, welche auf Proteomik, Radiokarbonmodell, Sediment-DNA, Isotopenanalyse oder aDNA?
4. Welche Nutzungsmodelle der Höhle werden durch Taphonomie und Funddichte gestützt oder geschwächt?
5. Welche Unsicherheiten entstehen gerade dadurch, dass ein erheblicher Teil des Materials aus der 1930er-Altgrabung stammt?
6. Welche ältere Forschungsaussage wird durch die 2024er Arbeiten bestätigt, präzisiert oder revidiert?

### Warum diese Frage für das Repo geeignet ist

Sie testet keine Vermittlung, sondern mehrere Kernfähigkeiten von Histo-Orla gleichzeitig:

- Source/Instance/Findspot sauber trennen;
- Alt- und Neuforschung mit unterschiedlicher Kontextqualität zusammenführen;
- archäologische und naturwissenschaftliche Evidenzachsen getrennt halten;
- Working Finding, Hypothese und offene Provenienzprobleme sichtbar halten;
- einen belastbaren Research State erzeugen, der ohne alten Chat fortsetzbar ist.

### Belastbarer Arbeitsstand

1. Die zentrale moderne Fundphase wurde 2016–2022 ausgegraben und 2024 in mehreren Fachartikeln publiziert.
2. Das LRJ ist in Ranis direkt mit **Homo sapiens** verbunden; die entscheidenden LRJ-Layer 9 und 8 liegen modelliert ungefähr bei 47.500–45.770 bzw. 46.820–43.260 cal BP.
3. Die Höhle war **kein dauerhaftes menschliches Wohnlager**. Zooarchäologie, Sediment-DNA und Taphonomie sprechen für intensive Nutzung durch Höhlenbären und Hyänen und nur episodische menschliche Aufenthalte.
4. Die menschlichen Reste sind überwiegend kleine Knochenfragmente. Proteomik, Radiokarbondatierung und aDNA sind zentral dafür, die Fragmente taxonomisch und populationsgeschichtlich einzuordnen.
5. Ein erheblicher Teil der menschlichen Reste wurde erst in Hülles Altfunden erkannt; deshalb ist die Korrelation von Altgrabungsbezeichnungen und moderner Stratigraphie selbst Teil des Erkenntnisproblems.
6. Die Umwelt während der LRJ-Nutzung war kalt und offen; die Isotopenstudie rekonstruiert eine kalte Steppe/Tundra und einen ausgeprägten Kälteeinbruch um ca. 45.000–43.000 cal BP.
7. Die Genomstudie verbindet Raniser Individuen mit Zlatý kůň und ordnet sie einer kleinen frühen Homo-sapiens-Population zu. Sie belegt **keine** Begegnung oder Vermischung von Neandertalern und Homo sapiens in der Ilsenhöhle selbst.
8. Die genaue frühere Höhlengeometrie bleibt unresolved, solange keine belastbare publizierte Vermessung/3D-Rekonstruktion direkt inspiziert ist.

### Zentrale Evidenzachsen

| Evidenzachse | Forschungsfunktion |
|---|---|
| Stratigraphie / Grabungsdokumentation | Korrelation Hülle ↔ 2016–2022, Fundkontext, Versturzgeschichte |
| Lithik | technologische Zuordnung zum LRJ |
| menschliche Knochen | direkte Homininen-Evidenz, aber vielfach erst analytisch identifiziert |
| Proteomik | taxonomische Identifikation kleiner Knochenfragmente |
| Radiokarbon + Bayes-Modell | Chronologie der Schichten/Funde |
| Zooarchäologie / Taphonomie | Nutzungsintensität Mensch vs. Carnivoren |
| Sediment-DNA | Faunen-/Umweltkontext unabhängig vom sichtbaren Knocheninventar |
| stabile Isotope | Klima, Vegetation, Ernährung, Mobilität |
| aDNA | biologische Verwandtschaft und Populationsgeschichte |
| Altgrabungsakten / Sammlungsprovenienz | Qualität und Grenzen der Rekonstruktion älterer Fundkontexte |

### Unresolved / offene Grenzen

- Die genaue frühere Höhlengeometrie wird nicht frei rekonstruiert.
- Layer 11 enthält alte, wenig diagnostische Artefakte; eine sichere menschliche Taxonzuweisung für diese Phase ist hier nicht gegeben.
- Altgrabungslabels und moderne Schichten dürfen nicht still gleichgesetzt werden; jede Korrelation braucht explizite Begründung.
- Die genetische Neandertaler-Admixture der Raniser Population belegt keinen lokalen Kontakt in der Ilsenhöhle.
- Der Zusammenhang zwischen paläolithischem Fundplatz und viel späterer Sagenüberlieferung ist ein eigener Forschungsstrang, keine Kontinuitätsaussage.

### Nächste diskriminierende Forschungsaktionen

1. Originalabbildungen und Supplements der vier zentralen 2024er Arbeiten vollständig figure-/panelgenau indexieren.
2. Die Korrelation `Hülle-Schichten/Labels ↔ moderne Layer 12–7` als eigene Claim-/Evidence-Matrix rekonstruieren.
3. Für jedes menschliche Fragment Herkunft, Alt-/Neugrabung, Layer/Label, Identifikationsmethode und Datierungsstatus erfassen.
4. Taphonomische Evidenz gegen die Arbeitshypothese `episodische menschliche Nutzung / dominante Carnivorennutzung` prüfen.
5. Offene Provenienzprobleme der Hülle-Sammlung gesondert markieren und nicht durch moderne Analytik verdecken.
6. Erst danach regionale Vergleichsfragen oder Forschungsgeschichte aktivieren.

## Themenqueue – bewusst nicht als fertige Synthese

- **Ranis/Ilsenhöhle:** aktive paläolithische Forschungsfrage, Alt-/Neugrabung, LRJ, Menschenreste, Tiernutzung, Klima, Genomik.
- **Gamsenberg/Rehmen:** mittelpaläolithischer Vergleichskontext.
- **Lausnitz:** Abri Theure, Lothar-/Nischenhöhle, Koleschhöhle; Funktion und Chronologie getrennt prüfen.
- **Döbritzer Schweiz:** Kniegrotte, Urdhöhle, Wüste Scheuer; jüngere paläolithische/mesolithische Vergleichshorizonte.
- **Herthahöhle / Teufelskanzel / Herdloch:** Altgrabungen, Nomenklatur- und Provenienzprobleme.
- **Börner / Goldne Schäferei:** Überlieferung, literarisch-antiquarische Bearbeitung, frühe Archäologie.
- **Burg / Torhaus / Frühmittelalter:** früher Keramikhorizont, Baubefund, hochmittelalterliche Herrschaftsgeschichte.
- **Museum / Forschungsgeschichte:** Ausstellungen und Beschriftungen als Quellen ihrer eigenen Zeit.

## Pilotgrenze

Dieser Branch erzeugt **keine** neue accepted Requirement-, Architecture- oder Method-Truth. Historische Findings bleiben proportional zu ihrer Evidenz `working`, `unresolved` oder `hypothesis`. Product-/System-Learnings werden ausschließlich in `system-learning.md` bzw. dem Self-Audit geführt.

## Navigation

- `evidence-ledger.md` – Quellen, Instanzen, Inspection-Status und Aussagegrenzen
- `vertical-slices.md` – aktive und queued Forschungs-Slices
- `field-materials.md` – Nutzerfotos / Museums- und Vor-Ort-Material als Quelleninstanzen
- `system-learning.md` – getrennte Produkt-/Systembeobachtungen
- `self-audit-20260906.md` – dokumentierte Zielkorrektur und Assistenz-Learnings
