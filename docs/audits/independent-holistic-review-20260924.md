# Unabhängige ganzheitliche Analyse Histo-Orla – 2026-09-24

**Work Owner:** #138  
**Reviewtyp:** unabhängige transdisziplinäre / historische / softwaretechnische Analyse  
**Basis:** `main@65b8e8f27658e4a2480f59503eaa9064fe4c5c58`  
**Status dieser Fassung:** **PHASE-6-FREEZE – unabhängig; vor inhaltlicher Lektüre der projektinternen Audits**  
**Audit-Quarantäne bis zu diesem Commit:** #64, #70, #121, PR #116, #118, #120 sowie erkennbare spätere Wiederholungen/Zusammenfassungen wurden in Phasen 1–6 nur als Existenz-/Metadatenobjekte registriert, nicht als diagnostische Inputs gelesen.

> Diese Fassung ist absichtlich kein Selbst-Audit des Projekts. Sie rekonstruiert zuerst Primärspuren, misst soweit möglich und trennt Beobachtung, Owner-Aussage, KI-Artefakt, externe Evidenz und Analystenfolgerung.

## 1. Zusammenfassung

### 1.1 Zentraler Befund

Histo-Orla ist am Stichtag **weder bloß ein historisches Forschungsdossier noch bereits das beabsichtigte Forschungswerkzeug**. Es ist ein sehr schnell gewachsener Hybrid aus (a) realer historischer Pilotforschung, (b) detaillierter epistemischer/organisatorischer Absicherung, (c) Requirements- und Architekturarbeit und (d) kleinem, überwiegend assurance-orientiertem Python-Code.

Die stärkste Qualität liegt derzeit **in der Explizitheit epistemischer Grenzen**: Source/Representation/Instance/Derivative/Findspot/Finding/Interpretation werden getrennt; editorische Ergänzung wird nicht als Quellenwortlaut behandelt; `unresolved` und corpus-bounded negatives sind zulässige Ergebnisse; automatisierte Checks beanspruchen ausdrücklich keine fachliche Validierung. **[B, hohe Konfidenz]**

Die stärkste Schwäche ist **die fehlende unabhängige Urteilsinstanz genau dort, wo der nicht fachkundige Owner und die KI denselben Blindfleck teilen können**. Der Prozess beschreibt diese Grenze korrekt, kompensiert sie bisher aber nur punktuell; weder historische Fachvalidierung noch unabhängiger Software-Review ist im Repository für die untersuchten Änderungen nachgewiesen. **[B+O→F, hohe Konfidenz]**

Die zweite zentrale Spannung ist **Wertschöpfung versus Absicherungslast**. Die frühe Zielsetzung war von Beginn an sehr breit; Governance ist daher nicht einfach später „entgleist“. Zugleich stehen 425 Commits, 138 Issues/PRs, 400 CI-Läufe und ein großer Prozess-/Architekturanteil einem noch weitgehend nicht implementierten Kernprodukt gegenüber. Ob diese Vorleistung sich amortisiert, ist noch nicht empirisch gezeigt. **[B→F, mittlere bis hohe Konfidenz]**

### 1.2 Was nicht behauptet wird

- Kein Befund besagt, dass hohe Dokumentations- oder Governance-Menge an sich schlecht ist.
- Kein offener Primärquellenpfad wird als Fehler gewertet, wenn das Projekt ihn korrekt als offen kennzeichnet.
- Ein grüner Test ist kein Nachweis historischer Wahrheit; ein roter Test ist umgekehrt kein Nachweis schlechter Architektur.
- Die Eigentümer-Prämisse „Artefakte KI-generiert / Owner historisch und softwaretechnisch fachfremd“ wird als bestätigte Rahmenbedingung behandelt, nicht als Kausalerklärung.
- Diese Analyse bewertet nicht die psychologischen Motive des Owners.

### 1.3 Wichtigste Evidenzlücken

1. Private Chatverläufe und nicht persistierte Owner-Entscheidungen fehlen; O/K-Trennung bleibt häufig unsicher.
2. Ein lokaler Clone/Testlauf war in der Audit-Runtime wegen DNS-Auflösung nicht möglich; Code-/CI-Befunde beruhen auf GitHub-API, Repository-Inhalten und GitHub Actions.
3. Es existiert kein unabhängiges Fachgutachten im Repo, an dem historische Schlussfolgerungen kalibriert werden könnten.
4. Für zwei von acht zufällig ausgewählten historischen Aussagen konnte die zitierte Edition/Quelle bibliographisch und über das interne Exzerpt, aber in diesem Audit nicht nochmals extern auf Inhaltsebene geöffnet werden.
5. Zeitaufwand des Owners ist nicht gemessen; Repository-Aktivität ist kein valider Ersatz für menschliche Belastung.
6. Deployment-/Betriebsmetriken sind weitgehend nicht anwendbar, weil kein ausgeliefertes Produkt/Service existiert.

---

## 2. Evidenzbasis und Lücken

### 2.1 Evidenzklassen

| Klasse | Verwendung in diesem Review |
|---|---|
| **B – beobachtet** | direkt in GitHub/externem Primär- oder Fachmaterial nachweisbar |
| **O – Owner-geäußert** | Owner-Prämisse oder Owner-Korrektur; ohne Rohchat oft nur indirekt |
| **K – KI-formuliert** | Projekttext/-struktur/-entscheidung, deren menschliche fachliche Prüfung nicht nachweisbar ist |
| **E – extern** | Fachliteratur, Standards, vergleichbare Systeme |
| **F – gefolgert** | Analystenfolgerung; immer mit Konfidenz und Gegenhypothese |

Da laut Owner die Projektartefakte KI-generiert sind, werden Repository-Texte **nicht allein durch Merge oder GitHub-Autor `esany` zu O**. Ein Merge zeigt Annahme/Integration, nicht nachweislich fachliches Verstehen.

### 2.2 Repository-Inventar am Basis-Commit

GitHub REST/tree war nicht trunciert.

| Messgröße | Befund |
|---|---:|
| Dateien | **125** |
| Tree-Einträge gesamt | 161 |
| Markdown | 84 |
| Python | 22 |
| JSON | 16 |
| TXT / YAML | 2 / 1 |
| Blob-Umfang | 1,941,472 Bytes |
| Dateien `docs/` | 83 |
| Dateien `tools/` | 38 |
| Commits seit 2026-08-29 | **425** |
| Issues | **78** |
| PRs | **60** |
| GitHub-Actions-Läufe | **400** |
| CI success / failure | **313 / 87** |

Commit-Aktivität nach Montag-Woche: 2026-08-24: 26; 08-31: **238**; 09-07: 27; 09-14: 74; 09-21: 60.

### 2.3 Reproduzierbare grobe Pfadklassifikation

Die Klassifikation ist **nur ein Proxy**, keine Qualitätsbewertung:

| Kategorie | Dateien | Bytes | Dateianteil | Byteanteil |
|---|---:|---:|---:|---:|
| konkrete historische Case-Artefakte (`docs/research/cases/**`) | 22 | 466,826 | 17.6% | 24.0% |
| Research-Methodik/SOTA/Requirements | 29 | 568,749 | 23.2% | 29.3% |
| Prozess/Architektur/Governance | 35 | 625,388 | 28.0% | 32.2% |
| ausführbares Tooling/Assurance | 39 | 280,509 | 31.2% | 14.4% |

Die Case-Dateien sind im Mittel wesentlich größer als Tooling-Dateien. Funktionsüberlappungen sind real; deshalb darf aus den Anteilen allein kein „Bloat“-Urteil folgen.

### 2.4 Audit-Quarantäneregister, nur Metadaten

Registriert, aber vor diesem Phase-6-Freeze inhaltlich nicht als Diagnoseinput verwendet:

- #64, erstellt 2026-09-01, offen;
- #70, erstellt 2026-09-03, geschlossen;
- #121, erstellt 2026-09-21, offen;
- PR #116, gemergt 2026-09-20;
- PR #118, offen;
- PR #120, offen.

Der inhaltliche Abgleich folgt **erst nach diesem Freeze** in Abschnitt 11.

---

## 3. Chronologische Rekonstruktion

### 3.1 29.–30. August: breites Zielbild vor späterer Assurance-Komplexität

Die frühesten Spuren (#1–#4) zeigen bereits:

- transdisziplinäre historische Forschung statt einzelner Datenbankaufgabe;
- unscharfe Nutzerfragen sollen in fachlich bearbeitbare Fragen übersetzt werden;
- Quellen/Literatur/Archive, exakte Fundstellen, OCR, Varianten, Archivrouting;
- langlebiger, providerunabhängiger, restartbarer Zustand;
- Automatisierung mechanischer Arbeit;
- Technologie ausdrücklich dienend und als Hypothese, nicht als Requirement.

**Befund [B]:** Die Breite des Solls ist **ursprünglich**, nicht erst Ergebnis späterer Governance.

### 3.2 Erste Septemberwoche: intensive Problem-/Requirements-/Pilotbildung

45 der 78 Issues wurden bereits in der Startwoche angelegt. Gleichzeitig beginnt reale U2-Forschung (`docs/research/cases` hat 54 Commit-Touches in der Woche ab 31.08.). Die Entwicklung ist also nicht einfach „Meta statt Forschung“; beides entsteht parallel.

### 3.3 Live Research

**#46 U2 Knau/Orlagau** entwickelt konkrete Quellenbefunde: Homonyme Altenburg/Orla, Knewe/Kneben/Knewer, Lobdeburg-Arnshaugk/Deutschorden, discrepante `Knauwe villa`-Datierungen. Quellen-/Editions-/Instanzgrenzen werden zunehmend explizit.

**#47 U1 Grenzraum/Teichlandschaft** ist deutlich unreifer: überwiegend Such-/Arbeitsrahmen und archivalische Kandidaten, weniger ausgebauter Quellenbefund.

**#103 Anno/Richeza/Saalfeld** arbeitet observation-first mit atomaren O-IDs und trennt Sekundärbericht, Edition, spätere Memoria und unresolved Primärpfade.

### 3.4 Requirements und Architektur

Die Problem-Baseline kodifiziert 12 Goals, 20 Needs, 16 Pains und Risiken. Die Requirements-Baseline + Extensions umfassen **53 Anforderungen**. Form und Traceability sind stark; der Delivery-Ledger ist dagegen bewusst konservativ: die meisten Requirements sind `not-started` oder `research-needed`.

### 3.5 Code und Assurance

Der Python-Bestand bleibt relativ klein; er konzentriert sich auf Requirements-/Assurance-Validation, operational execution, research-state references und document-evidence roundtrip. OCR, breite Retrieval-UX, Providerintegration und die eigentliche Forschungsarbeitsoberfläche sind nicht geliefert.

GitHub Actions scheiterten 87/400-mal. Stichproben in Logs zeigen echte Regressionen, u. a. eine unerlaubte Human-Review-Zustandsänderung, untracebare kontrollierte Codeänderungen und Coverage-Inkonsistenzen. Automatisierte Assurance findet damit reale formale Fehler.

### 3.6 Prior-Art-Linie

Zugänglich und zeitlich älter:

- `esany/rgk-main-ssot` (2026-06-14);
- `esany/Wissensarbeit` (2026-08-05);
- `esany/paleo-type` (2026-08-26);
- Histo-Orla (2026-08-29).

Gemeinsame Muster sind sichtbar: Git als Projektgedächtnis, kleine Work Orders, AI ≠ Evidenz, kanonische Owner, technische Subsidiarität. Da die Repositories danach parallel weiterentwickelt wurden, ist nicht für jede heutige Formulierung eine einseitige Ableitung beweisbar.

---

## 4. Intent und Bedürfnisse

| Element | Ebene | Herkunft / Evidenz | Symptom-Test | Folgerung |
|---|---|---|---|---|
| „historische Fragen zuverlässig beantworten“ | Grundwunsch | #1/#46/#47/#103, K mit Owner-Annahme | nein | eigentlicher Produktzweck |
| unscharfe Frage → fachlich bearbeitbare Frage | Bedürfnis | #1, Problem-Baseline N001/N002, K | nein | kompensiert fehlendes Domänenvokabular |
| persönliche Bibliotheks-/Archivassistenz | Wunsch + Need | #2–#4, K | teilweise | dient Quellenzugang, nicht Selbstzweck |
| exakte Fundstellen / Wiederauffindbarkeit | Need | frühe Issues + reale Pilotfriktion, B/K | nein | realer Forschungsengpass |
| OCR/HTR | Capability-Wunsch | #4, K | teilweise | Mittel gegen image-only Quellen; konkrete Engine keine Anforderung |
| restartbarer Zustand ohne alten Chat | Need | frühe Ziele + Repo-Praxis, B/K | nein | realer KI-Kontextverlust-Pain |
| Provider-/Modellunabhängigkeit | Qualitätsbedarf | #1/#3, K | nein | reduziert Lock-in |
| immer detailliertere Governance/Assurance | operationalisierte Lösung | viele spätere Artefakte + Tools, B/K | **ja, potenziell** | reagiert auf tieferes Bedürfnis nach verlässlicher Delegation/State/Authority |
| unabhängige fachliche Validierung | latentes/teilweise explizites Need | AI-non-evidence Regeln + Owner-Prämisse, O/K→F | nein | notwendige Kompensation doppelter Fachblindheit |

### 4.1 Verborgener Bedarf H1

**F:** Der Kernbedarf ist weniger „eine Software bauen“ als **epistemische Handlungsfähigkeit trotz fehlender eigener Fachsprache und Prüfroutine**: relevante Quellen finden, Aussagen bis zur Evidenz verfolgen, Unsicherheit verstehen und Arbeit nach KI-Kontextwechsel fortsetzen.

**Konfidenz:** hoch.  
**Gegenhypothese:** Der Owner will primär ein wiederverwendbares Forschungsframework bauen; historische Antworten sind nur Pilotdomäne.  
**Falsifikation:** Frühe Owner-Primärspuren, die Framework-/Softwarebau ausdrücklich über historische Erkenntnis stellen.

### 4.2 Symptomkette H2

**F:** Ein Teil der immer feineren Governance ist wahrscheinlich Symptom einer tieferen Friktion: **KI kann schnell viel plausible Struktur erzeugen, aber der Owner kann deren fachliche/technische Richtigkeit nicht vollständig prüfen**. Das Projekt ersetzt deshalb wiederholte implizite Urteilssituationen durch persistente Grenzen, Validatoren und Work Orders.

**Konfidenz:** mittel-hoch.  
**Gegenhypothese:** Die Formalisierung ist schlicht vernünftige Vorinvestition und wird sich in späteren Research-Wellen amortisieren.  
**Falsifikation:** Messbarer Rückgang von Rework/Meta-Aufwand bei gleichzeitig deutlich steigendem geprüftem Forschungsertrag.

---

## 5. Soll, Ist, Genese

### 5.1 Soll

Das rekonstruierte Soll ist ein **leanes, evidenzgebundenes persönliches Forschungsassistenzsystem**, das Domänenmethoden aktiviert, Quellen/Instanzen/Fundstellen sauber trennt, mechanische Recherchearbeit automatisiert, menschliches/fachliches Urteil nicht simuliert und aus Git/zugänglichen Quellen ohne Chat fortsetzbar ist.

### 5.2 Ist

Das Ist ist ein **stark dokumentierter Research-/Assurance-Prototyp** mit drei verschiedenen Reifestufen:

1. **Historische Forschung:** reale, teils gute Working Research, aber noch begrenzte Primärquellensättigung und ohne unabhängige Fachabnahme.
2. **Epistemische/organisatorische Infrastruktur:** sehr weit ausgebaut, teilweise ausführbar.
3. **Nutzerprodukt:** Kernfähigkeiten wie generisches Retrieval, OCR/HTR, Providerintegration und Arbeitsoberfläche überwiegend noch nicht implementiert.

### 5.3 Genese – beobachtbare Mechanismen

- sehr breites Start-Soll;
- 45 Issues in der Startwoche;
- parallele Pilotforschung und Requirements-/Architekturarbeit;
- Übernahme/Adaption von Prior-Art-Mustern;
- reale Fehlerfälle werden in persistente Regeln/Validatoren übersetzt;
- starke AI-Produktionsgeschwindigkeit;
- PRs häufig als Integrationsgefäß statt als langsamer Peer-Review-Schritt.

**F:** Diese Kombination begünstigt **Korrekturkaskaden**: ein Fehler erzeugt nicht nur eine lokale Korrektur, sondern leicht eine generalisierte Regel, ein Schema, einen Validator, Tests und neue Traceability. Das kann sinnvoll sein, wenn der Failure Mode wiederkehrt; ohne Benefit-/Stop-Messung kann es aber Prozesslast selbst erzeugen.

**Konfidenz:** mittel.  
**Gegenhypothese:** Die ersten vier Wochen sind absichtlich Infrastruktur-Frontloading; spätere Amortisation ist noch nicht beobachtbar.  
**Falsifikation:** zeitbasierte Daten zeigen sinkenden Meta-Anteil pro geprüftem Research-Ergebnis.

### 5.4 Nachhaltigkeit

425 Commits in 26 Tagen, 138 Issue/PR-Objekte und 400 CI-Läufe sind für ein Einzelprojekt außergewöhnlich hohe Änderungsdichte. **Das ist kein Zeitaufwandsmaß des Owners**, weil KI einen Großteil der Produktion automatisiert. Es ist aber ein belastbarer Proxy für die Menge an Zustand, die verstanden, geprüft und langfristig gepflegt werden muss.

**F:** Nachhaltigkeitsrisiko **mittel-hoch**, solange kein messbarer Rückgang der Meta-/Reconciliation-Arbeit und kein stabiler Owner-Workflow nachgewiesen ist.

---

## 6. Qualitätsbefunde

Schweregrade: **kritisch** = Kernvertrauenswürdigkeit unmittelbar invalidiert; **hoch** = systematisches materielles Risiko; **mittel** = bedeutsam, aber begrenzt/mitigiert; **niedrig** = Hygiene/kleine Abweichung; **Hinweis** = neutraler Reife-/Kontextbefund.

### 6.1 Sprach- und Strukturmuster KI-generierter Artefakte

| Kriterium | Beobachtung | Klasse | Grad | Auswirkung / Konfidenz |
|---|---|---|---|---|
| Strukturwiederholung | viele Statusköpfe, Owner-/Scope-/Non-goal-/Acceptance-/STOP-Blöcke, Tabellen und kontrollierte IDs | B | Hinweis | erhöht Restartbarkeit; hoch |
| Begriffsschöpfung | projektspezifische Begriffe wie Work Owner, Method Truth, Research State, Assurance werden stark systematisiert | B | mittel | kann reale Grenzen präzisieren, aber fachliche Reife sprachlich überzeichnen; hoch |
| semantische Stabilität | wichtige Konzepte werden korrigiert statt nur akkumuliert, z. B. Zotero-Rolle | B | positiv | Lernfähigkeit vorhanden; hoch |
| Dokumenttiefe vs. Erkenntnis | einige Artefakte tragen echte Methodengrenzen; andere beschreiben primär Prozess | B→F | mittel | Gefahr ausgearbeiteter Selbstbeschreibung ohne proportionalen Research-Gewinn; mittel |
| Sprachliche Autorität | hochformale normative Sprache kann bei KI-generiertem Inhalt den Anschein geprüfter Authority erzeugen | O+B→F | hoch | besonders relevant bei fachfremdem Owner; hoch |

### 6.2 Transdisziplinäre Qualität

Externe Referenzen: Bergmann et al. 2005 (ISOE), Pohl/Hirsch Hadorn 2007, Boix Mansilla 2005/2006, Belcher et al. 2016.

| Kriterium | Befund | Klasse | Grad | Konfidenz |
|---|---|---|---|---|
| Problemkonstitution | Needs/Pains/Goals sind explizit und früh; Problem ist realweltlich und wissenschaftlich/technisch übersetzt | B | positiv | hoch |
| System-/Ziel-/Transformationswissen | im Material vorhanden, aber nicht immer als drei Wissensarten getrennt | B→F | niedrig | mittel |
| Rückübersetzung zum Nutzer | Human-readable Audit/Handoff ist Ziel, reale Endnutzer-UX kaum geliefert | B | mittel | hoch |
| disziplinäre Fundierung | Quellenkritik und Provenienz stark operationalisiert; weitere Domänenmethoden teils noch working/method-debt | B | mittel | hoch |
| Methodenwahl | explizit gegen One-size-fits-all; reale Piloten falsifizieren Methoden | B | positiv | hoch |
| Integrationsleistung | Source→Instance→Findspot→Finding ist ein tragfähiges Grenzobjekt zwischen History/RSE | B→F | positiv | hoch |
| Integrationsebenen | kognitiv/methodisch/technisch stark; sozial-organisatorisch kaum echte Mehrakteurs-/Fachcommunity-Integration | B→F | hoch | hoch |
| Konflikte | unresolved/disputed und konkurrierende Provenienzpfade sind vorgesehen | B | positiv | hoch |
| Zuständigkeit | Rollen sind dokumentiert, aber qualifizierte externe Urteilsinstanz fehlt praktisch | B | **hoch** | hoch |
| delegierte Urteile | AI non-evidence und Review-Klassen werden begrifflich getrennt | B | positiv | hoch |
| tatsächliches Peer Review | kein Fachpeer-Review nachgewiesen | B | **hoch** | hoch |
| Unsicherheit | sehr gut repräsentiert | B | positiv | hoch |
| Reflexivität | außergewöhnlich hoch; teilweise selbst zum großen Arbeitsgegenstand geworden | B→F | mittel | hoch |
| Lernfähigkeit | reale Fehler führen zu veränderten Regeln/Tests, nicht nur Textkorrekturen | B | positiv | hoch |
| Technik als Dienst | explizites Prinzip und in Architektur häufig eingehalten; dennoch Assurance vor Kernnutzen weit fortgeschritten | B→F | mittel | hoch |
| Anschlussfähigkeit | Markdown/JSON, stabile IDs, offene Quellenpfade; gutes Human/Tool-Interchange | B | positiv | hoch |
| Ergebnis-Relevanz | historisch relevante Pilotfragen, aber nur Teilantworten | B | Hinweis | hoch |
| Glaubwürdigkeit | gute Statusdisziplin, aber fehlende externe Fachvalidierung und offene Primärpfade | B→F | hoch | hoch |
| Legitimität | für persönliches Projekt Stakeholder-Inklusion teilweise N/A; fachliche Mitprüfung fehlt | B→F | mittel-hoch | mittel |
| Wirksamkeit | tatsächlicher Erkenntnisnutzen vorhanden, Gesamtsystemwirkung noch nicht belegt | B | mittel | hoch |

**Gesamtinterpretation ohne Score:** Das Projekt zeigt **starke transdisziplinäre Design- und Integrationsabsicht**, aber der reale Prozess ist derzeit eher **AI-vermittelte interdisziplinäre/integrative Einzelarbeit** als vollwertige transdisziplinäre Zusammenarbeit mit unabhängigen disziplinären und lebensweltlichen Wissensträgern.

### 6.3 Historische Fachqualität

#### Quellenarbeit

Stärken:
- klare Trennung Original/Edition/Regest/Sekundärquelle;
- konkrete Findspots und digitale Instanzen bei reiferen Fällen;
- editorische Ergänzungen werden als solche markiert;
- negative Befunde haben Search Boundaries;
- `unresolved` wird nicht wegentschieden.

Grenzen:
- viele Working Findings beruhen noch auf Edition/Sekundärliteratur; Originale/Archivalien sind häufig nicht inspiziert;
- moderne Archivkonkordanzen älterer Editionssignaturen sind mehrfach noch offen;
- unabhängige diplomatische/landesgeschichtliche Fachprüfung fehlt.

#### Forschungsstand

Lampe, Dobenecker, Schmidt/Urkundenbuch der Vögte, regionale Literatur und digitale Angebote sind erkannt. Das U2-Artefakt sagt jedoch selbst, Dobenecker/Schmidt und weitere regionale Pfade seien **nicht vollständig** durchsucht. Eine Vollständigkeits- oder Neuheitsbehauptung wäre daher verfrüht.

#### Standards und Eigenbau

- TEI wird als möglicher Referenzrahmen erwähnt, aber nicht implementiert; bei den aktuellen Working Notes ist Markdown nicht per se unangemessen.
- Für archivische Beschreibung ist 2026 **Records in Contexts (RiC)** der aktuelle ICA-Rahmen; RiC-CM 1.0 ersetzt ausdrücklich ISAD(G), ISAAR(CPF), ISDF und ISDIAH. Histo-Orla sollte daher bei künftiger Formalisierung nicht auf ältere ISAD(G)-Begriffe fossilisiert werden.
- Das eigene Source/Representation/Instance/Findspot-Modell ist kein etablierter editionswissenschaftlicher Standard, aber es löst reale Provenienzprobleme und ist mit PROV-/RiC-/TEI-Denken kompatibel. Sein fachlicher Status bleibt projektspezifischer Contract, nicht Disziplinstandard.

**Befund:** Quellenkritische Prozessqualität **deutlich stärker als Reife der historischen Ergebnisse**. Das ist für Working Research legitim, solange Statusgrenzen erhalten bleiben. **[B→F, hohe Konfidenz]**

### 6.4 Softwaretechnische Qualität

#### Zweckmäßigkeit

Ein Großteil des aktuellen Codes adressiert nachweisbare Probleme (Traceability, Reference Integrity, exact document evidence, bounded execution). Zugleich existiert noch kein vollständiger Nutzerpfad für die Hauptbedürfnisse. **[B, mittel]**

#### Requirements Engineering

Positiv:
- eindeutige IDs, Rationale, Acceptance, Risks, Ownership, Dependencies;
- Trennung von Requirements und Technologiehypothesen;
- Delivery-Status konservativ.

Risiko:
- die **formale Traceability ist stärker als die Autoritätsqualität der Quellen**. Viele Requirements leiten sich aus KI-generierten Projektartefakten ab. Ein Validator kann Konsistenz prüfen, nicht Notwendigkeit oder fachliche Richtigkeit.

**Grad:** hoch für Authority-/Validation-Risiko; nicht für Syntax/Traceability.

#### Architektur

Positiv:
- Requirements→Responsibilities→Questions→Candidates→Trade-offs→Decision;
- explizite Reversibilität und Deferred Decisions;
- Canonical Research State Contract ist technologieunabhängig;
- aktuelle WP1-Grenze vermeidet DB/Graph/Workflow-Engine und andere Vorbauten.

Risiken:
- Architektur-/Assurance-Dokumentation ist groß im Verhältnis zum gelieferten Produkt;
- viele interne Begriffe/Contracts erhöhen Lernlast;
- Nutzen der gesamten Schicht ist noch nicht gegen Owner-Aufwand gemessen.

#### Codequalität

Lexikalische Messung der 22 Python-Dateien:
- Produktions-LOC ca. **2,221**;
- Test-LOC ca. **1,494**;
- Test/Prod-LOC ≈ **0.67**;
- keine sichtbare TODO/FIXME-Halde;
- nur ein breiter `except Exception`, kein bare except.

Auffällig sind einzelne große Kontrollfunktionen, z. B. `render_audit_view` (~187 Zeilen) und `validate_execution_order` (~93 Zeilen) mit hoher Verzweigungsdichte. Das ist Wartbarkeitsrisiko, kein Defektnachweis.

CI enthält **keinen nachgewiesenen Linter/Typechecker** und keine Mutation-Test-Stufe. **Grad mittel.**

#### Test und Verifikation

- 87/400 CI-Failures beweisen, dass die Suite reale Änderungen zurückweist.
- Logs zeigen echte Regressionserkennung.
- Tests prüfen überwiegend **formale/contractspezifische Eigenschaften**; ihre Orakel stammen oft aus denselben akzeptierten Projektcontracts.
- `document_evidence` markiert ausdrücklich `semantic_validation:not-performed`; das ist positiv.
- Mutation Testing nicht nachgewiesen.
- lokale Wiederholung dieses Audits war runtimebedingt nicht möglich; GitHub-Runners liefern aber clean-environment evidence.

**Befund:** gute deterministische Verifikation innerhalb ihres Geltungsbereichs; **keine Validierung historischen Inhalts**. [B, hoch]

#### Daten

- Markdown/JSON sind offen und langfristig lesbar.
- Schema-/ID-Trennung und Providerneutralität sind gut.
- keine DB-Migrationen, weil keine DB.
- Source Bytes liegen konzeptionell außerhalb Git; Backup/Restore der Gesamtkette ist nicht als geübter Owner-Prozess nachgewiesen.
- 10-Jahres-Lesbarkeit der kuratierten Textdaten gut; externe Byte-/Provider-Verfügbarkeit bleibt eigenes Risiko.

#### Sicherheit / Recht / Lieferkette

- `main` ist am Stichtag **unprotected**; GitHub Branch API: `protected:false`.
- Repository Rulesets: leer.
- Workflow-Actions sind als Major-Tags (`actions/checkout@v7`, `setup-python@v7`) statt Full-SHA gepinnt.
- Python-Abhängigkeit `jsonschema>=4.23,<5`; kein vollständiger Lockfile-/SBOM-Nachweis.
- CodeQL/Dependabot/Secret-Scanning-Status konnte über den verfügbaren Connector nicht geprüft werden.
- OWASP ASVS ist mangels Webanwendung derzeit nur sehr begrenzt passend.
- SLSA 1.2 ist 2026 aktueller als 1.1 und enthält einen Source Track; dessen Review-/Source-Control-Prinzipien sind für dieses Repo eher relevant als Enterprise-Deployment-Controls.
- Rechte/Cloud-Processing sind als Requirement/Contract modelliert, aber nicht vollständig umgesetzt.

**Grad:** mittel; Branch-/Review-Control für kanonische Änderungen hoch relevant.

#### Build/Betrieb

Es gibt kein deploybares Produkt. GitHub Actions baut eine frische Python-Testumgebung reproduzierbar genug für die aktuellen Validatoren. Ein Human-Setup-/Recovery-Run durch den nichttechnischen Owner ist **nicht nachgewiesen** und muss als nicht geprüft gelten.

#### Dokumentation

Dokumentation ist umfangreich, meist aktuell verlinkt und maschinen-/menschenlesbar. Gleichzeitig ist der Dokumentationsumfang für ein 2.2-KLOC-Produkt sehr hoch, und Zielgruppen „Forschen“, „Betreiben“, „Entwickeln“ sind noch nicht als schlanke Nutzerwege getrennt. **Grad mittel.**

#### Wartbarkeit/Nachhaltigkeit

Technischer Bus-Factor: faktisch **1 Owner + austauschbare KI-Werkzeuge**. Ein anderer Mensch könnte aus dem Repo viel rekonstruieren, muss aber eine große projektspezifische Begriffswelt lernen. Owner-eigene Reparaturfähigkeit ist nicht belegt. **Grad hoch als Kontinuitätsrisiko; Konfidenz mittel-hoch.**

### 6.5 Entwicklungsprozess

| Kriterium | Befund | Klasse | Grad |
|---|---|---|---|
| Commits | hohe Frequenz; Nachrichten überwiegend aussagekräftig | B | Hinweis |
| Branch/PR | 60 PRs, 49 merges; kurzlebig | B | positiv/neutral |
| unabhängiger Review | alle 60 PRs vom selben Account; 10-PR-Stichprobe ohne submitted reviews | B | **hoch** |
| Reviewzeit | Median PR-Eröffnung→Merge ca. **44 s** | B | **hoch** als Hinweis gegen echte Reviewfunktion |
| Batchgröße | Stichprobe enthält z. B. PR #132: +893/-100 in ~115 s; #79: +392/-8 in ~88 s | B | hoch für Prüfbarkeit |
| CI | 313 success /87 failure; rot findet reale Regelverletzungen | B | positiv |
| DoD | Work Orders/Acceptance/STOP häufig explizit | B | positiv |
| technische Schuld | offen/unresolved häufig sichtbar | B | positiv |
| WIP | 52 offene Issues, 6 offene PRs; viele davon deferred/owner items, daher nicht = aktives WIP | B | Hinweis |
| Stop-Kriterien | lokal stark; projektweiter „genug“-Nutzen/Amortisation nicht operational gemessen | B→F | mittel |
| DORA | nicht sinnvoll als Produktionsbenchmark: kein ausgelieferter Service | E+B | N/A |

DORA definiert 2026 fünf Produktionsmetriken; für Histo-Orla wären derzeit eher **Research lead time, rework und verified-result throughput** passend als Deployment Frequency.

### 6.6 KI-gestützte Entwicklung

| Kriterium | Befund | Grad |
|---|---|---|
| Herkunft | laut Owner alle Artefakte KI-generiert; Git zeigt nicht pro Artefakt Modell/Session | mittel |
| menschliche Prüfung | Merge/Account-Aktion beweist nicht Verstehen; keine ausreichende Evidenz | **hoch** |
| Existenzprüfung | mehrere externe Standards/Quellen werden tatsächlich verifiziert; aber keine globale Garantie | mittel |
| Konsistenz über Sitzungen | viele stabile IDs/Contracts; zugleich wiederholte Reconciliation-Arbeit | mittel |
| Änderungsumfang | einzelne große PRs werden in Sekunden/Minuten gemergt | **hoch** |
| Kontextverlust | sehr stark technisch adressiert; Kosten sind große Persistenz-/Governance-Schicht | mittel |
| AI als Evidenz | explizit verboten und technisch teilweise abgesichert | positiv |
| unabhängige Instanz | anderes Modell/Prompt ist keine unabhängige fachliche Validierung | **hoch** |

---

## 7. Ergebnisse der Prüfverfahren

### 7.1 Reproduzierbare Stichprobe historischer Aussagen

Auswahl vor Inhaltsprüfung, stratified 4+4, Pseudorandom-Seed = numerischer Wert des Basis-SHA `65b8e8...`.

Ausgewählt:
- U2: `F-U2-003`, `F-U2-007`, `F-U2-004`, `F-U2-001`;
- #103: `O-018`, `O-023`, `O-006`, `O-007`.

| ID | Prüfergebnis | externe/konkrete Gegenprüfung | Status |
|---|---|---|---|
| F-U2-003 | Perlbach-Druck zeigt tatsächlich `Ludewicus Stango` und `Heinrich [Stange] von Knewe`; Projekt interpretiert Klammer korrekt als editorisch | MGH-Bibliothek Scan, S. 117 | **bestätigt** |
| F-U2-007 | moderne Sekundär-/Ortsdarstellungen nennen 1374 **und** 1378; Projekt macht daraus keinen Primärbefund | Wikipedia/Ortsdarstellungen als Traditionsnachweis, nicht als Primärbeleg | **bestätigt als Diskrepanz** |
| F-U2-004 | Lampe Bd.1 existiert; internes Exzerpt dokumentiert THULB-Scans 378–379 und begrenzt Aussage auf Edition; externe Inhalts-Reinspektion in diesem Audit technisch nicht gelungen | ISGV/HOV + Sächs. Archiv bestätigen Werk; Repo-Exzerpt exakt | **nicht unabhängig vollinhaltlich revalidiert** |
| F-U2-001 | Lampe existiert; konkrete Nr.461/496/499/552 sind intern fundstellengenau; externe Inhalts-Reinspektion nicht vollständig gelungen | ISGV/HOV + Werkexistenz | **nicht unabhängig vollinhaltlich revalidiert** |
| O-018 | Ezzos Tod 1034 in Saalfeld und Erbfolge Otto werden durch Deutsche Biographie / regionale Fachliteratur gestützt | Deutsche Biographie | **bestätigt auf Sekundärniveau** |
| O-023 | Hlawitschka S. 242–243 sagt explizit: 1056 verabredet, Sommer 1057 endgültig; Fußnoten nennen Fundatio/Rhein. UB/Oediger | MGH-PDF | **bestätigt als Aussage Hlawitschkas** |
| O-006 | Robinsons Lampert-Übersetzung S.152 berichtet Vertreibung der Kanoniker und Mönche aus Siegburg/St. Pantaleon | publizierter Preview / TCD Metadaten | **bestätigt** |
| O-007 | Robinson dokumentiert Lamperts 14-wöchige Anwesenheit teils Saalfeld, teils Siegburg | publizierter Preview | **bestätigt** |

**Fehlerquote:** In den **6 extern auf Inhaltsebene revalidierten** Aussagen wurde **0 direkte inhaltliche Fehlwiedergabe** gefunden. Zwei weitere sind nicht als Fehler zu zählen, sondern blieben im Audit auf Inhalts-Reinspektionsebene offen. Das erlaubt **keine** Hochrechnung „0 % Fehler im Projekt“: n=8 ist klein, Working Findings wurden gesampelt, und zwei konnten nicht vollständig extern überprüft werden.

### 7.2 Zitat-/Werkexistenz

In der Stichprobe existieren die verwendeten Werke (Lampe, Perlbach, Robinson, Hlawitschka). Historische Archivsignaturen werden im Projekt erfreulich oft ausdrücklich als **nicht modern verifiziert** markiert. Kein erfundener Titel/Autor wurde in der Stichprobe entdeckt.

### 7.3 Literaturabgleich

Der Abgleich zeigt, dass Histo-Orla relevante Standard-/Regionalwerke kennt (Dobenecker, Schmidt, Lampe etc.), sie aber selbst als noch nicht vollständig kollationiert bezeichnet. Deshalb ist die Eignung dieses Verfahrens **hoch**, aber sein aktuelles Ergebnis lautet: Forschungsstand **noch nicht gesättigt**.

### 7.4 Gegenprüfung durch ein anderes KI-System

Als Verfahren nur **bedingt geeignet**. Es kann Inkonsistenzen, Halluzinationsrisiken und alternative Suchpfade finden, ist aber wegen korrelierter Trainings-/Sprachmuster keine unabhängige historische Fachinstanz. Besonders gefährlich wäre „zwei Modelle stimmen überein“ als Corroboration.

### 7.5 Einfache Kennzahlen

- konkrete Case-Dateien: 17.6 % der Files / 24.0 % der Bytes;
- Research-Methodik: 23.2 % / 29.3 %;
- Prozess/Architektur/Governance: 28.0 % / 32.2 %;
- Tooling/Assurance: 31.2 % / 14.4 %.
- Kern-Requirements: 53; Mehrzahl noch nicht gestartet/research-needed.
- historische Zufallsstichprobe: 6/8 extern inhaltlich revalidiert, 0/6 direkte Widersprüche, 2/8 auditseitig nicht voll revalidierbar.

**Eignung:** Kennzahlen sind gut gegen Selbsttäuschung, aber dürfen Kategorienqualität und menschlichen Zeitaufwand nicht vortäuschen.

### 7.6 Minimaler externer Prüfauftrag

**Historisch:** Eine qualifizierte Person für mittelalterliche thüringisch-sächsische Landesgeschichte/Diplomatik sollte **nicht das ganze System auditieren**, sondern (a) die acht Stichprobenclaims und zwei strittige Identitäten/Datierungen bis Edition/Original prüfen, (b) Quellenhierarchie/Aussagestärke markieren und (c) fünf fehlende Standardwerke/Bestände nennen. 2–4 Stunden qualifizierter Review hätten mehr Kalibrierwert als ein weiteres internes Meta-Audit.

Geeignete Typen: zuständiges Landes-/Staatsarchiv, Lehrstuhl/Arbeitsstelle Landesgeschichte/Mediävistik, erfahrene Bearbeiterin eines Urkunden-/Regestenprojekts oder regionaler Geschichtsverein **mit** belegter Quellenkompetenz.

**Technisch:** Eine erfahrene Python/RSE-Person sollte in einem frischen Checkout (a) Setup nach Doku, (b) Tests/Lint/Typecheck, (c) drei zentrale Module, (d) Dependency/Actions-Pinning, (e) Restore/Handoff prüfen und nur konkrete Findings liefern. Ebenfalls 2–4 Stunden.

---

## 8. Externe Maßstäbe und Vergleich

### 8.1 Transdisziplinarität

- Bergmann et al. 2005, ISOE: formative, diskursive Qualitätsbewertung für transdisziplinäre Projekte; betont, dass rein disziplinäre Evaluation nicht ausreicht.  
  https://www.isoe.de/en/publication/quality-criteria-of-transdisciplinary-research-a-guide-for-the-formative-evaluation-of-research-projects
- Pohl & Hirsch Hadorn 2007: Problemstrukturierung, Perspektivenvielfalt, gesellschaftlicher Kontext und adaptive Methoden über Phasen. DOI 10.14512/9783962388638.
- Belcher et al. 2016: Relevanz, Glaubwürdigkeit, Legitimität, Wirksamkeit. DOI 10.1093/reseval/rvv025.
- Boix Mansilla 2005: disziplinäre Standards bleiben Voraussetzung für gute Integration; Interdisziplinarität darf nicht disziplinäre Fundierung ersetzen.

**Übertragungsgrenze:** Histo-Orla ist ein persönliches Forschungsprojekt ohne klassische Stakeholder-Ko-Produktion. Kriterien sozialer Repräsentation dürfen daher nicht mechanisch als Defizit gewertet werden; fachliche Mehrperspektivität und unabhängige Urteilsautorität bleiben trotzdem relevant.

### 8.2 Historische / DH-Standards

- ICA Records in Contexts: RiC-CM 1.0 (2023) ersetzt ISAD(G), ISAAR(CPF), ISDF, ISDIAH; RiC-O 1.1 seit 2025.  
  https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-conceptual-model/
- TEI P5 ist 2026 bei Version 4.12.0.  
  https://www.tei-c.org/guidelines/p5/

**Übertragungsgrenze:** Histo-Orla ediert derzeit nicht primär einen Textkorpus. TEI/RiC als Pflichtformat zu verlangen wäre selbst Overengineering. Sie sind Referenzrahmen für Interoperabilität und Terminologie, wenn die jeweilige Capability real entsteht.

### 8.3 Software Engineering

- ISO/IEC 25010:2023: aktuelles Produktqualitätsmodell mit neun Eigenschaften.
- ISO/IEC/IEEE 29148:2018: 2024 bestätigt und weiterhin aktuell.
- OWASP ASVS 5.0.0: relevant erst bei tatsächlicher Webanwendung.
- SLSA: aktuelle Spezifikation **v1.2** (Nov. 2025), inklusive Source Track.
- DORA 2026: fünf Delivery-Metriken; explizit auf ausgelieferte Anwendung/Service bezogen.

**Übertragungsgrenze:** Enterprise-Controls dürfen nicht zum Selbstzweck eines kleinen Forschungsprojekts werden. Relevanter als Voll-Compliance sind kleine, konkrete Risiken: ungeschützter main, fehlender unabhängiger Review, ungepinnte Actions, reproduzierbare Dependencies, Restore.

### 8.4 Empirische KI-Forschung – Gegenevidenz in beide Richtungen

Die externe Evidenz ist **nicht einheitlich**:

- Noy & Zhang (Science 2023): bei mittleren professionellen Schreibaufgaben durchschnittlich 40 % weniger Zeit, 18 % höhere Qualität.
- Dell’Acqua et al. (BCG/HBS, publiziert Organization Science 2026): innerhalb der AI-capability frontier ~25 % schneller und >40 % höhere Qualität; außerhalb einer ähnlich wirkenden Frontier-Aufgabe waren AI-Nutzende 19 Prozentpunkte seltener korrekt.
- Peng et al. (Copilot, 2023): kontrollierte kleine Programmieraufgabe 55.8 % schneller.
- METR (2025): erfahrene Open-Source-Entwickler auf ihren eigenen reifen Repos **19 % langsamer** mit frühen 2025-AI-Tools; sie glaubten dennoch, schneller gewesen zu sein.
- DORA 2025/2026: AI wirkt als „amplifier“; Erstellzeit kann sinken, während Audit-/Verifikationszeit und Instabilität steigen.

**Übertragung:** Diese Befunde passen besonders gut zur Histo-Orla-Risikolage: KI kann Produktion stark beschleunigen, aber **Prüfkosten und Frontier-Erkennung** werden zur Engstelle. Keiner dieser Befunde validiert KI als historische Fachinstanz.

---

## 9. Hypothesen und Gegenhypothesen

### H1 – Epistemische Handlungsfähigkeit ist der eigentliche Produktkern
**F, hoch.** Siehe 4.1.  
**Gegenhypothese:** wiederverwendbares Framework ist primär.  
**Falsifikation:** frühe Owner-Primärspuren mit umgekehrter Priorität.

### H2 – Assurance-Wachstum ist teils rationale Fehlerreaktion, teils selbstverstärkungsfähig
**F, mittel-hoch.** Reale Failure Modes werden in Regeln/Validatoren überführt; Änderungsdichte und Meta-Anteil sind hoch.  
**Gegenhypothese:** einmaliges Foundation-Frontloading.  
**Falsifikation:** sinkende Prozesskosten je geprüftem Ergebnis bei realer Nutzung.

### H3 – Epistemische Scaffolding-Qualität übersteigt historische Ergebnisreife
**F, hoch.** Quellen-/Unsicherheitsmodell ist stark; Primärpfade und Fachvalidation bleiben offen.  
**Gegenhypothese:** Working Research soll gerade unfertig sein; Vergleich ist unfair.  
**Falsifikation:** breitere Zufallsstichprobe zeigt mehrheitlich primärquellennahe, fachlich gegengeprüfte Endbefunde.

### H4 – Requirements sind formal stark, aber authority-fragil
**F, hoch.** Traceability/Acceptance ist gut; Ursprung vieler Requirements ist KI-formulierter Projektzustand.  
**Gegenhypothese:** reale Owner-Pains sind korrekt transportiert und Requirements werden durch Pilotforschung falsifiziert.  
**Falsifikation:** unabhängiger RE-/Domänenreview bestätigt Notwendigkeit, Priorität und Semantik weitgehend.

### H5 – Deterministische Assurance ist sinnvoll begrenzt, kann aber keine Fachvalidation ersetzen
**F, hoch.** Das Projekt sagt dies selbst; Tests belegen formale Fehlerfunde.  
**Gegenhypothese:** Es besteht kein Problem, weil Assurance nie mehr beansprucht.  
**Falsifikation der Risikoseite:** konsequente UI/Reports verhindern nachweislich, dass formale PASSes als fachliche Freigabe gelesen werden.

### H6 – Prior Art beschleunigt und importiert zugleich Komplexität
**F, mittel.** Gemeinsame Patterns und zeitliche Vorgänger sind belegt.  
**Gegenhypothese:** übernommene Controls passen wegen identischer Failure Modes exakt.  
**Falsifikation:** jeder importierte Mechanismus lässt sich auf realen Histo-Orla-Pain und messbaren Nutzen zurückführen.

### H7 – Unabhängige Review-Lücke ist das zentrale Qualitätslimit
**F, hoch.** Kein Fachpeer-Review; GitHub-PR-Review in Stichprobe absent; Owner kann per Prämisse beide Fachdomänen nicht selbst voll prüfen.  
**Gegenhypothese:** Blind-/Adversarial-AI-Audits reduzieren Fehler ausreichend für den privaten Working-State-Zweck.  
**Falsifikation:** unabhängige menschliche Stichprobe findet keine materiellen Fehler und bestätigt Methoden-/Architekturpassung; wiederholt über Zeit.

### Unerklärte Beobachtungen

- Warum genau in der Startwoche 45 Issues benötigt wurden, ist aus Git allein nicht kausal rekonstruierbar.
- PR-Median 44 Sekunden kann Automationsfluss erklären, aber nicht, wie viel Prüfung außerhalb GitHub stattfand.
- Owner-Verstehen/Approval lässt sich aus Merge-Aktionen nicht messen.
- Das Verhältnis von realer Owner-Zeit zu KI-generierter Repository-Menge ist unbekannt.

---

## 10. Anerkennung – was trägt und erhaltenswert ist

1. **Uncertainty as result:** `unresolved` wird praktisch verwendet.
2. **Source identity discipline:** Quelle, Repräsentation, konkrete Instanz und Fundstelle werden sauber getrennt.
3. **Editorial-layer preservation:** z. B. `[Stange]` wird nicht zum historischen Namen umgeschrieben.
4. **Bounded negatives:** „nicht gefunden“ wird an Suchraum gebunden.
5. **Status-Ehrlichkeit:** der Delivery-Ledger erklärt Kernfähigkeiten nicht vorzeitig für fertig.
6. **Deterministische Assurance mit Geltungsgrenze:** Tests finden reale formale Fehler und behaupten keine Semantik.
7. **Offene/reversible Datenhaltung:** Markdown/JSON, providerneutrale IDs, keine vorschnelle Datenbank.
8. **One-fact/one-home und Restartability:** für KI-gestützte Langzeitarbeit ein reales, wertvolles Problem.
9. **Technische Subsidiarität als explizites Korrektiv:** aktuelle WP1-Entscheidungen zeigen, dass große Plattformoptionen auch aktiv abgelehnt/deferred werden.
10. **Quellenarbeit verbessert sich über Piloten:** #103 und reife Teile von U2 zeigen deutlich bessere Aussagegrenzen als bloße generische Recherche.

---

## 11. Abgleich mit projektinternen Audits

**NOCH NICHT DURCHGEFÜHRT IN DIESER FASSUNG.**

Diese Leerstelle ist absichtlich Teil des Phase-6-Freeze. Erst der nächste Commit darf die quarantänisierten Audit-Inhalte lesen und hier ergänzen. Der unabhängige Befund in Abschnitten 1–10 und 13 wird dann nicht nachträglich umgeschrieben.

---

## 12. Empfehlungen

**NOCH NICHT FINALISIERT.** Empfehlungen werden nach dem getrennten Phase-7-Abgleich ergänzt und bleiben rückführbar auf die unabhängigen Befunde.

---

## 13. Reflexion der eigenen Analyse

### 13.1 Eigene Befangenheit

Dieser Review wird von einem KI-System über ein vollständig KI-generiertes Projekt durchgeführt. Daraus folgen korrelierte Risiken:

- ähnliche Präferenz für explizite Taxonomien, Verträge, Tabellen und „saubere“ Trennungen;
- Tendenz, textliche Kohärenz mit methodischer Qualität zu verwechseln;
- mögliche Sympathie für maschinenprüfbare Governance;
- gleiche blinde Flecken bei historischen oder softwaretechnischen Details.

Gegenmaßnahmen dieses Reviews:
- Primärspuren vor Selbstbeschreibung;
- quantitative Repo-Metriken;
- zufällige Claim-Stichprobe;
- externe Original-/Fachquellen;
- gegensätzliche empirische AI-Studien;
- interne Audit-Quarantäne bis Phase 6;
- keine Gesamtscores.

### 13.2 Grenzen

- Kein Ersatz für Diplomatik-/Landesgeschichte-Peer-Review.
- Kein Ersatz für lokalen Security-/Dependency-/Mutation-Test-Audit.
- Keine Aussage über private Chats oder nicht persistierte Owner-Arbeit.
- Keine belastbare Messung menschlicher Zeit.
- Kleine historische Stichprobe.
- Das Projekt ist jung; Nachhaltigkeits- und Wirksamkeitsurteile sind deshalb notwendigerweise vorläufig.

### 13.3 Reproduzierbarkeit

Reproduzierbare Kerndaten:
- Basis-SHA: `65b8e8f27658e4a2480f59503eaa9064fe4c5c58`;
- Work Owner: #138;
- Zufallsstichprobe: Seed aus Basis-SHA, 4 U2-Findings + 4 #103 Observations;
- Pfadklassifikation in §2.3;
- GitHub Actions/PR/Issue-Metriken aus GitHub REST am 2026-09-24;
- Phase-6-Freeze als eigener Git-Commit.

Ein Folge-Reviewer kann damit den unabhängigen Stand von jedem späteren Phase-7-Abgleich unterscheiden.
