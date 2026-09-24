# Histo-Orla – Bestandsaufnahme Intent, Erkenntnislücken und offene Punkte

**Stand:** 2026-09-24  
**Basis:** main@65b8e8f27658e4a2480f59503eaa9064fe4c5c58 plus ausdrücklich gekennzeichnete nicht gemergte Branch-/PR-Inputs  
**Status:** Bestandsaufnahme / read-only Analyse / keine Promotion  
**Auftrag:** Owner-Auftrag vom 2026-09-24; kein neuer Work Owner, kein Requirement-, Method-, Architecture- oder Governance-Delta  
**Einziges Persistenzziel dieses Auftrags:** diese Datei

## 1. Kurzfassung

Die aktuelle Projektlogik besitzt bereits einen großen Teil der vom Owner gewünschten Kette, aber noch nicht in der heute formulierten Form. Das Repo kann relativ gut von Goals/Needs/Pains über Capabilities und accepted Requirements bis zu Implementation, Verification und Feedback rückverfolgen. Es kann jedoch zwei heute zentrale Größen noch nicht als eigene, sauber relationierte Ebenen ausdrücken: **Intent** und die **Erkenntnislücke hinter dem Intent**. Der aktuelle formale Motor beginnt deshalb praktisch bei G/N/P, obwohl der Owner am 24.09.2026 ausdrücklich eine vorgelagerte Schicht beschreibt: Intent → Erkenntnislücke → das ganze Netz.

Die stärkste Kontinuität über die Projektgeschichte ist nicht eine bestimmte Architektur, sondern ein Nutzerproblem: Ein fachlich nicht spezialisierter Research Owner will reale historische Fragen verfolgen können, ohne die einschlägigen Fachbegriffe, Fachdomänen, Methoden, Quellenlogiken und technischen Mechanismen selbst vollständig beherrschen zu müssen. Der jüngste Owner-Input schärft dies erheblich: Der Initiator beschreibt sich als „fachlich doppelt blind“ – sowohl gegenüber den fachwissenschaftlichen als auch den technologischen transdisziplinären Wissensgebieten. Das System soll diese Blindheit nicht durch eine vereinfachende Black Box verdecken, sondern einen **Informationsraum** schaffen, der an die Kompetenzen des Owners anschlussfähig ist und in dem die letzte Erkenntnislücke „in meinem kopf“ geschlossen wird.

Dazu passt ein zweiter stabiler Strang: Unsicherheit, Provenienz, Evidenz und wissenschaftliche Standards sind keine Gegenpole zur Nutzbarkeit. Der Owner sagt dies am 24.09. ausdrücklich. Ältere Repo-Artefakte bilden diesen Schutzraum bereits stark ab: Source/Representation/Instance/Derivative/Findspot werden getrennt; unresolved ist zulässig; AI ist keine Evidenz; Fachmethodik soll domänenspezifisch sein. Der aktuelle Mangel liegt weniger in diesen Schutzregeln als darin, dass ihr Ergebnis noch nicht durchgängig als owner-tauglicher Informationsraum erscheint.

Die Entwicklung der Nutzeroberfläche bzw. des sichtbaren Forschungsprodukts zeigt eine klare Schärfung. Früh stand ein allgemeines menschenlesbares Research State/Audit-Ziel. Am 03.09. wurde ein statisches „Modul“-Denkschema ausdrücklich als NOT PASS verworfen. Am 23.09. war der technisch korrekte Auditpfad dem Owner „sehr kryptisch und eher maschinentauglich als forschungsrelevant“. Die zunächst daraus abgeleitete Idee einer visuellen Derived View wurde wenige Minuten später selbst als „too narrow“ korrigiert. Der aktuelle repo-interne Arbeitsstand ist excerpt-zentriert: exakte Quelle/Instanz/Fundstelle, Originaltext bzw. Bildkontext, Unsicherheit und Finding/Interpretation müssen zusammen inspectable bleiben; eine visuelle Darstellung ist nur eine Projektion. Anhang A schärft dies nochmals: Eine Karte statt Koordinaten ist ein Beispiel für Informationsraum, aber der Owner will „kein ui, das ich hinbekommen mus und dann wieder selbst hermetisch ist“.

Ein weiterer stabiler Strang ist die Trennung von **Motorraum** und sichtbarem Forschungsraum. Schon früh sollte Technik dienen und mechanische Arbeit automatisieren. Reales Owner-Feedback vom 02./03.09. kritisierte, dass der Mensch/Chat weiterhin zu viel Context-, Markdown- und Workflow-Orchestrierung trägt. Der Bounded-Execution-Contract vom 23./24.09. verbessert inzwischen den Entwicklungsprozess für Repository-Arbeit. Er baut aber noch nicht den eigentlichen Forschungs-Motor. Auf main existiert lauffähiger Code vor allem für Requirements-/Trace-Assurance, Context/Resume, Mutation Guards, Bounded Execution, Document-Evidence-Roundtrip, Research-State-Referenzen und Audit-Projektion. Nicht allgemein geliefert sind dagegen Zotero/OneDrive-Resolver, OCR/HTR, historisches Retrieval, wissenschaftliche Promotion/Transition, Rights Admission, Provider Removal/Restore und ein owner-facing Research Workspace/Informationsraum.

Die größte Nachzieh-Lücke liegt deshalb nicht darin, dass das Repo gar keine Needs oder Requirements hätte. Im Gegenteil: Viele jüngere Aussagen sind bereits teilweise durch G/N/P, CAP-17, REQ-UX-001/003, REQ-STATE, REQ-EPI, REQ-MTH, REQ-TRACE und die Source-/Findspot-Regeln abgedeckt. Die Lücke ist, dass die **heutige Intent-Genealogie und ihre Relation zu Erkenntnislücken nicht explizit** ist. Die Problem-Baseline enthält zwar einen Post-baseline-Owner-Research-Abschnitt vom 20.09., aber nicht die Schärfungen vom 23./24.09. Das Capability Map stammt im Kern vom 31.08. Die Requirements enthalten bewusst nicht automatisch jedes Owner-Signal. README und PROJECT_STATE zeigen die Delivery-/Assurance-Kette, aber nicht das aktuelle Intent→Erkenntnislücke→Informationsraum-Modell. Das ist als Bestandsbefund zu lesen, nicht als automatische Forderung nach neuen Requirements.

Die offenen Punkte sind zahlreich, aber nicht gleichbedeutend mit aktivem WIP. Es gibt vier offene Feedback-Records in der Trace-Projektion, darunter zwei pain-persists/new-pain-Stränge. selection-open ist weiter gültig. Das Modul-Artefakt u2-modulares-forschungs-und-suchinventar.md liegt trotz expliziter Demotion des Modulkonzepts noch im aktiven Research-Case-Pfad und trägt im Header weiterhin working-research / modular-research-inventory. Sechs alte PRs (#118, #119, #120, #122, #123, #124) sind offen und jeweils deutlich hinter main. Der unabhängige Review #138 liegt auf einem nicht gemergten Branch genau einen Commit vor main. Daneben existieren alte divergierte Branches ohne offenen PR. Für den technischen Kern bestehen weiterhin echte Capability-Lücken, und #44 enthält weiterhin den externen Branch-Protection-Blocker DD-20260903-001.

**Arbeitsdiagnose dieser Bestandsaufnahme, ausdrücklich keine Promotion:** Das vorhandene Netz ist tragfähig genug, um nicht neu erfunden werden zu müssen. Es ist aber noch kein vollständiger Motor, weil Intent und Erkenntnislücke nicht first-class relationiert sind, Owner-Feedback nur teilweise bis in Discovery/Capability-Sichten zurückwirkt und der Informationsraum als tatsächliches Produkt noch fehlt. Die aktuelle Situation ist daher eher „starker wissenschaftlicher und formaler Unterbau + partieller technischer Motor + fragmentierte sichtbare Forschungsräume“ als ein bereits geschlossener Intent-getriebener Entwicklungszyklus.

### Herkunftsklassen dieser Bestandsaufnahme

- **Wörtliche Owner-Aussage:** nur Rohzitate aus Anhang A oder ein im Repo ausdrücklich erhaltenes Owner-Rohzitat.
- **Paraphrase einer Owner-Aussage durch die KI:** Repo-Text, der sich als Owner-Feedback/-Clarification bezeichnet, dessen Rohchat aber nicht vorliegt.
- **KI-Ableitung:** Interpretation, Synthese, Working Hypothesis, Review- oder Analysefolgerung.
- **Beobachtung im Repo:** direkt feststellbarer Artefakt-, Status-, Code-, Branch-, PR-, Commit- oder Relationstatbestand.

Ein GitHub-Commit oder der Autorname esany wird **nicht** als Beweis dafür behandelt, dass der enthaltene Wortlaut eine wörtliche Owner-Aussage ist. Diese Grenze wird zusätzlich durch den nicht gemergten unabhängigen Review #138 bestätigt.

---

## 2. Intent-Aussagen

Die Tabelle erfasst Intent-tragende Aussagen und Korrekturen chronologisch. Sie ist keine vollständige Liste jeder technischen Einzelanforderung; aufgenommen sind Aussagen, die Zweck, gewünschtes Arbeitserleben, Grenzen oder eine wesentliche Korrektur des Zielbilds ausdrücken.

| Datum | Fundstelle | Aussage | Herkunft | Unsicherheit / Einordnung |
|---|---|---|---|---|
| 2026-08-29 | Initial commit 2e56b9c | Initiales README enthielt nur den Repository-Titel; ein belastbarer Intent ist daraus nicht rekonstruierbar. | Beobachtung im Repo | Kein inhaltlicher Intent im Initial Commit. |
| 2026-08-30 | #1 Research Design | Histo-Orla soll ein funktionierendes, dauerhaft nutzbares System für transdisziplinäre historische Forschung werden; es soll einen fachlich interessierten Owner ohne vorausgesetzte Spezialausbildung unterstützen. | Paraphrase einer Owner-Aussage durch die KI / kanonischer Repo-Text | Kein Rohchat erhalten. |
| 2026-08-30 | #1 | Quellen/Literatur erschließen, Fragen fachwissenschaftlich präzisieren, fehlendes Fachvokabular erschließen, Fachkompetenzen aktivieren, Methoden/Evidenzregeln respektieren, Unsicherheit sichtbar halten, mechanische Arbeit automatisieren, dauerhaften Research State erzeugen. | Paraphrase einer Owner-Aussage durch die KI | Breites frühes Zielbild. |
| 2026-08-30 | #2 | Der persönliche Archivar ist wichtige Spezialkompetenz, aber nicht Gesamtziel oder epistemische Oberinstanz; tägliche Quellen-/Literaturarbeit soll bis zur Fundstelle unterstützt werden. | Paraphrase einer Owner-Aussage durch die KI | Bereits frühe Korrektur eines engeren Archiv-Assistentenbilds. |
| 2026-08-30 | #9 comment 5470872009 | „Der Nutzer darf unsauber fragen; das System muss trotzdem wissenschaftlich sauber arbeiten. Technik darf wissenschaftliche Anforderungen unterstützen, aber nicht ersetzen oder abschwächen.“ | KI-formulierte kanonische Leitformel; Owner-Rohwortlaut nicht belegt | Inhalt passt späteren Owner-Signalen, Wortlaut nicht als Owner-Zitat behandeln. |
| 2026-08-30 | #13/#14 | Geschichte wird transdisziplinär verstanden; regionale Tiefenschärfe ist Anker, nicht analytische Grenze; überregionale/europäische Verflechtung wird problemabhängig aktiviert. | Paraphrase einer Owner-Aussage durch die KI | Später auf lange Diachronie und bis zu globale Kontexte erweitert. |
| 2026-08-30 | #15/#16 | Gewünscht ist fachliche Tiefe mit Methoden, Quellenwelten, Kontroversen, regionaler/zeitlicher Spezialisierung; nicht „einfache historische Wahrheiten“. | Paraphrase einer Owner-Aussage durch die KI | Später durch #60 methodisch verschärft. |
| 2026-08-30 | #19 | Archivar nicht Oberrolle; mehrere eigenständige Fachkompetenzen; technische Umsetzung als Agent, Rollenprofil, Tool usw. bleibt offen. | Paraphrase einer Owner-Aussage durch die KI | Wichtig gegen spätere Fehlinterpretation „Multi-Agent als Produktintent“. |
| 2026-08-30 | #20 | Histo-Orla soll fachlich belastbaren, transdisziplinär anschlussfähigen und menschenlesbar erklärbaren Research State erzeugen; Vermittlung ist nachgelagerte Projektion und darf Research State nicht zurückschreiben. | Paraphrase einer Owner-Aussage durch die KI | Aktuell kompatibel mit Informationsraum, aber Informationsraum ist nicht identisch mit Vermittlung. |
| 2026-08-30 | #24 | Deterministische/spezialisierte Verfahren sollen Aufgaben übernehmen, wo sie robuster sind; generative KI nicht als Default. | Paraphrase einer Owner-Aussage durch die KI | Trägt Motorraum-/Automation-Linie. |
| 2026-08-31 | #3 | OneDrive = Source of Bytes; Zotero = bibliographische/archivische Verwaltung + Attachment-Referenz; Histo-Orla = wissenschaftlicher Research State. Frühere Hypothese „Zotero = alleiniger Source of Truth“ verworfen. | Paraphrase einer Owner-Aussage durch die KI | Konkrete, im Repo explizit als Owner-Präzisierung markierte Korrektur. |
| 2026-09-01 | FB-20260901-001 / #63 | Assurance darf nicht bei Requirement Records enden; Goal/Need/Pain → Requirement → Decision → Delivery → reale Nutzung/Feedback muss geschlossen werden. | Paraphrase einer Owner-Aussage durch die KI | Daraus entstand REQ-TRACE-001; Feedback-Record selbst ist noch open. |
| 2026-09-01 | FB-20260901-002 / #63 | Vermeidbare rote Zwischenstände und doppelte CI-Läufe erzeugen unerwünschten Benachrichtigungs-/Workflow-Pain. | Paraphrase einer Owner-Aussage durch die KI | Delivery-Pain, nicht Produktintent im engeren Sinn. |
| 2026-09-02 | FB-20260902-003 / #63 comment 5516893666 | Reale Lampe-PDF-Nutzung sei trotz Requirements zu manuell/chat-orchestriert: Markdown-Wände, alte Annotationen, zu wenig generierte human-readable Views und Automatisierung von Context/Trace/Derive. | Paraphrase einer Owner-Aussage durch die KI | Sehr wichtiger Übergang von „korrekter State“ zu „Owner muss weniger orchestrieren“. |
| 2026-09-03 | #64 comment 5522329568 | Governance sei „sumpfig“; Root/Handoff priorisiere Meta-System statt Forschung; ein enger Pilot müsse real question → real evidence → method → result/unresolved → owner-readable output → observed friction liefern. | Paraphrase einer Owner-Aussage durch die KI | Kommentar ist explizit Owner-Feedback, Rohchat liegt nicht vor. |
| 2026-09-03 | #63 comment 5528759900 | „bitte verwerfe das konzept des moduls, das war uns zu statisch und nicht apssfähig zu unserem zielverständnis“ | **Wörtliche Owner-Aussage** | Rohzitat im Repo erhalten. |
| 2026-09-03 | #63 comment 5528759900 | „Sichere diesen Fall als nicht PASS“ | **Wörtliche Owner-Aussage** | Rohzitat im Repo erhalten. |
| 2026-09-03 | #63 comment 5528759900 | KI-Interpretation der Korrektur: Quelle → Aussage → Reichweite → Unsicherheit → Anschlussfrage → nächste Prüfspur statt Quelle → Modul → Routing → Suchhaken. | KI-Ableitung aus Owner-Korrektur | Plausible Operationalisierung, aber nicht wörtliche Owner-Aussage. |
| 2026-09-19 | PR #111 / problem-baseline post-baseline history | Laufende Owner-Kommunikation ist zuerst User Research; Beispiele, Metaphern und gewünschte Sichten dürfen nicht direkt zu Fachwahrheit, Objektmodell, Feature oder Architektur werden. | Paraphrase einer Owner-Aussage durch die KI | Korrektur nach zu schneller Promotion eines „Wissensraum“-Mental-Models. |
| 2026-09-19 | Research-design / PR #111 | Owner-Mental-Model eines transformierbaren Wissensraums mit Zeit/Raum/Akteuren/Herrschaft/Quelle usw. wird als User-Research-Signal, nicht als Ontologie/Requirement behandelt. | Paraphrase + KI-Ableitung | Repo macht die Unsicherheit inzwischen explizit. |
| 2026-09-20 | problem-baseline „Post-baseline Owner User-Research Synthesis“ | Wiederkehrende Owner-Signale: langfristig wachsender regionaler Forschungsraum; reuse über Piloten; derselbe State unter verschiedenen Fragen/Perspektiven; keine privilegierte Zerlegung; Quellen-/Evidenzkontext erreichbar; Research Questions als State; Widersprüche dürfen unresolved bleiben. | KI-Synthese aus Owner-Signalen | Status ausdrücklich working synthesis / no new Requirement. |
| 2026-09-20 | #64 comment 5752182921 | „Histo-Orla hat inzwischen genügend konzeptionelle Bausteine. Das offene Problem ist nicht, sie weiter zu verfeinern, sondern ihre minimalen gemeinsamen Invarianten an heterogenen realen Forschungsfällen zu falsifizieren, während die historische Synthese wieder zum sichtbaren Primärprodukt wird.“ | KI-Synthese / Review input | Im Kommentar als Synthese, nicht als Roh-Owner-Zitat. |
| 2026-09-23 | #63 comment 5802074059 | Ergebnis des WP1-Realtests sei „sehr kryptisch und eher maschinentauglich als forschungsrelevant“. | Paraphrase einer Owner-Aussage durch die KI mit vermutlich wörtlich eingebetteter Phrase | Rohchat fehlt; Phrase als im Feedback erhalten, aber nicht mit Anhang-A-Sicherheit. |
| 2026-09-23 | #63 comment 5802074059 | Erste KI-Deutung: relevante Textpassagen + vollständige Karte + kurze fachliche Rahmung als visual research composition; Provenienz im Drill-down. | KI-Ableitung | Bereits 22 Minuten später ausdrücklich als zu eng korrigiert. |
| 2026-09-23 | #63 comment 5802389782 / PR #135 | „smallest visual Derived View“ war zu eng; Workflow ist nicht presentation-first. Kern soll ein provenance-bound Excerpt/Findspot-Paket an exakter Instance/Derivative/Source sein; Originaltext/-bild, Fundstelle, Unsicherheit und Finding/Interpretation inspectable; Visualisierung nur derived. | Paraphrase einer Owner-Aussage durch die KI | Aktuellster repo-interner Owner-Feedback-Stand vor Anhang A. |
| 2026-09-23 | #92 comment 5803394415 | Repo-changing Rebuild-Arbeit soll in Coding Execution wie Codex, bounded, modellagnostisch, mit minimalem Kontext/Token und deterministic-first erfolgen; kein Produkt-Agentenframework. | Paraphrase einer Owner-Aussage durch die KI | Delivery-/Bau-Intent, nicht automatisch Produkt-Laufzeitintent. |
| 2026-09-24 | Anhang A | „Es ist komplett ki generiert. Der Initiator ist fachlich doppelt blind, weder die fachlichen Domänen noch die technologischen sind ihm vertraut, und beides sind transdisziplinäre wissensgebiete. Prüfe den inten, Bedürfnisse und Anforderungen, was sind wirkliche, was sind verborgene die erst unter den eigentlichen bedarfen und Anforderungen liegen und eher Symptome sind. Genauso ist auch der repostand zu lesen, was soll es sein und wieso ist es so geworden wie es ist“ | **Wörtliche Owner-Aussage** | Jüngster expliziter Meta-Intent; schärft Owner-Kompetenzlücke erheblich. |
| 2026-09-24 | Anhang A | „Ich kann mir intents aber auch vorschlagen lassen und dann justieren - die Bedürfnisse sind ja schon da.. bzw. Das ganze netz. Was noch eine grösse wäre: erkenntnislücke hinter dem intent“ | **Wörtliche Owner-Aussage** | Führt Intent und Erkenntnislücke explizit vor G/N/P ein. |
| 2026-09-24 | Anhang A | „Und die letzte erkenntnislücke passiert in meinem kopf, weil das System mir einen informationsraum bietet in dem ich all meine erkenisdlücken schließen kann, weil sie passfähigkeit zu meinen Kompetenzen schaffen“ | **Wörtliche Owner-Aussage** | Stärkste aktuelle Beschreibung des sichtbaren Produktzwecks. |
| 2026-09-24 | Anhang A | „Unsicherheit, provienz standards an fachliche wissenschaftlichkeit und evidenz ist keine widersprüche zu meinen Bedürfnissen.“ | **Wörtliche Owner-Aussage** | Explizite Klärung: wissenschaftliche Strenge ist kein UX-Gegenpol. |
| 2026-09-24 | Anhang A | „Die Agenten erstellen die logik das System und managen es, das ist der ganze technologische wie auch der domainspezifische part aber!!!!!! Das ist der Motorraum, in den ich schon auch reinschauen kann, das Ergebnis muss aber ein informationsraum für mich sein.  Und der motorraum braucht echtes Development“ | **Wörtliche Owner-Aussage** | „Agenten“ ist hinsichtlich Produktlaufzeit vs. Bau-/Betriebsmethode noch interpretationsbedürftig. |
| 2026-09-24 | Anhang A | „Versteh mich nicht falsch, ich will dennoch eine gewisse Kontrolle über die fundamente. Kein ui, das ich hinbekommen mus und dann wieder selbst hermetisch ist und nicht mehr pflegbar. Auch wissensstrukturen können schon der erste informationsraum sein, oder entsprechend aufbereitetes wissen.. eine karte statt Koordinaten.. wir sind noch im bauen und da ganz am Anfang und die Baustelle steht im Morast..“ | **Wörtliche Owner-Aussage** | Verbindet Informationsraum, Kontrollbedürfnis, Wartbarkeit und Anti-Black-Box. |
| 2026-09-24 | Anhang A | „Der prompt soll das repo erstmal eine Bestandsaufnahme machen lassen, es gibt offene punkte. Das Problem ist auch, das frühe intents durch spätere intents konkretisiert und generalisiert bzw. Geschärft wurden, was im repo vlt. Mir nachgezogen wurde.“ | **Wörtliche Owner-Aussage** | Direkter Anlass dieser Datei. |
| 2026-09-24 | Anhang A | „Ziel diese struktur als motor“ | **Wörtliche Owner-Aussage** | Stellt die Intent-/Gap-/Need-/Req-/Feedback-Struktur selbst als zukünftige Steuerungslogik in Aussicht; keine Promotion durch diese Bestandsaufnahme. |

---

## 3. Intent-Linien mit aktuellem Stand und Entwicklung

### IL-01 – Reale historische Erkenntnis für einen nicht spezialisierten Owner → Informationsraum, in dem die letzte Lücke im Kopf geschlossen wird

**Früher Stand:** funktionierendes Werkzeug für transdisziplinäre historische Forschung, nicht Konzeptpapier; Owner ohne vorausgesetzte Spezialausbildung (#1).

**Entwicklung:**
1. Früh: menschenlesbarer, nachvollziehbarer Research State (#20, CAP-17).
2. 02./03.09.: Owner soll nicht Meta-State und Workflow orchestrieren; sichtbarer Primäroutput soll Research-Artefakt sein (#63/#64).
3. 23.09.: technisch korrekter Auditpfad ist zu kryptisch; provenance darf nicht die Primärdarstellung dominieren.
4. 24.09.: **verallgemeinert und geschärft** zum Informationsraum, der Passfähigkeit zu den Kompetenzen des Owners schafft; letzte Erkenntnislücke wird im Kopf des Owners geschlossen.

**Aktueller Stand aus Quellen:** Histo-Orla soll nicht nur korrekten Research State erzeugen, sondern Wissen so zugänglich machen, dass der Owner trotz fachlicher/technischer Blindheit historische Erkenntnis selbst bilden und beurteilen kann. Der Informationsraum ist ein Ergebnis über dem Motorraum, aber kein notwendigerweise hermetischer UI-Layer.

**Unklar:** Was genau „Passfähigkeit zu meinen Kompetenzen“ messbar bedeutet; ob Informationsraum primär strukturierte Wissensobjekte, generierte Synthesen, Karten/Timelines oder kombinierte progressive Views meint.

### IL-02 – Doppelte Blindheit kompensieren: fachliche Problemübersetzung, Expertise/Methoden und technische Verantwortung nicht dem Owner aufbürden

**Früher Stand:** G-002/N-001/N-002, CAP-01/CAP-02, #16/#19: Owner kennt Fachvokabular und notwendige Disziplinen nicht im Voraus.

**Entwicklung:**
1. Fachblindheit wurde früh explizit adressiert: unscharfe Frage → fachliche Problembegriffe, Methoden, Quellenlogik.
2. #60 schärfte: echte domänenspezifische Methodik statt Rollenprompt.
3. 02./03.09.: Owner darf auch kein Workflow-/Context-Compiler sein.
4. 24.09.: **erweitert** um technologische Blindheit; beide Wissensgebiete sind selbst transdisziplinär.

**Aktueller Stand:** System/Motor soll sowohl Fachmethodik als auch technische Umsetzung professionell tragen, während der Owner Intent, Relevanz, Feedback und kontrollierende Einsicht behält.

**Unklar:** Welche Entscheidungen trotz doppelter Blindheit beim Owner bleiben müssen und welche Form von unabhängiger menschlicher Fach-/Technikvalidierung nötig ist. Der nicht gemergte #138-Review markiert genau hier eine mögliche Review-Lücke; das ist Review-Input, keine akzeptierte Wahrheit.

### IL-03 – Wissenschaftliche Strenge ist Bestandteil der Nutzbarkeit, nicht ihr Gegenpol

**Früher Stand:** Source/Instance/Findspot, Unsicherheit, Kontroverse, AI ≠ Evidenz, domänenspezifische Standards (#9/#15/#20/#45; CAP-04/08/10/18; REQ-EPI/SRC/MTH).

**Entwicklung:** Der Repo-Aufbau hat diese Schutzregeln stark formalisiert. Reale Nutzung zeigte jedoch, dass ihre sichtbare Darstellung den Owner überlasten kann. Am 24.09. klärt der Owner ausdrücklich, dass Unsicherheit, Provenienz, wissenschaftliche Standards und Evidenz **keine Widersprüche** zu seinen Bedürfnissen sind.

**Beziehung:** **geschärft/klargestellt**, nicht ersetzt. Das Problem ist die Form der Übersetzung/Präsentation und die fehlende Informationsraum-Integration, nicht die wissenschaftlichen Anforderungen selbst.

**Aktueller Stand:** Schutzinvarianten bleiben. Der Informationsraum muss sie wirksam tragen, ohne dass der Owner zuerst den Audit-/Governance-Unterbau bedienen oder lesen muss.

### IL-04 – Quelle/Fundstelle/Exzerpt als owner-nutzbarer Evidenzanker statt abstrakter Module oder reiner Auditkette

**Früher Stand:** persönliche Archivassistenz, Source Identity, exakte Fundstellen, OCR/Retrieval; später Source/Representation/Instance/Derivative/Findspot-Trennung.

**Entwicklung:**
1. 03.09.: statische Forschungsmodule ausdrücklich NOT PASS.
2. 03.09. KI-Deutung der Korrektur: Quelle → Aussage → Reichweite → Unsicherheit → Anschlussfrage → Prüfspur.
3. #51 beweist technischen Roundtrip an konkreter Sachenbacher-Instanz.
4. 23.09.: reine Audit-/Provenienzkette owner-seitig zu kryptisch.
5. 23.09.: Visual-View-Deutung zu eng; excerpt-centered package wird aktuelle Working Interpretation.
6. 24.09.: „eine karte statt Koordinaten“ als Beispiel für aufbereitetes Wissen; zugleich keine hermetische UI.

**Aktueller Stand:** Das sichtbare Forschungsobjekt soll evidenznah und verständlich sein. Exzerpt/Fundstelle muss Originalkontext, exakte Provenienz, Unsicherheit und wissenschaftliche Anschlussobjekte erhalten. Visualisierungen sind mögliche Informationsraum-Projektionen, nicht Truth Store.

**Konkreter Widerspruch im Repo:** docs/research/cases/u2-modulares-forschungs-und-suchinventar.md steht weiterhin als working-research / modular-research-inventory im aktiven Case-Pfad und beschreibt „Netz fachlicher Forschungsmodule“, obwohl der Owner das Modulkonzept am selben Tag ausdrücklich verworfen hat. Git-Historie enthält die Korrektur, die Datei selbst wurde nicht als superseded/deprecated markiert.

### IL-05 – Langfristiger, perspektivisch transformierbarer Forschungsraum / Netz ohne erzwungene Universalontologie

**Früher Stand:** transdisziplinär, regional tief aber überregional verbunden; Quellen und Research State wiederverwendbar.

**Entwicklung:**
1. 19.09.: Wissensraum-Mental-Model wurde zu schnell kanonisiert.
2. Owner-Korrektur führte zu Re-Klassifikation als User Research / Mental Model.
3. 20.09.: problem-baseline konsolidiert: langer regionaler Forschungsraum, reuse, wechselnde Perspektiven, keine privilegierte Zerlegung; „Netz“, „orthogonal“, „kneten“ ausdrücklich Metaphern, keine Graph-/Ontologieentscheidung.
4. 24.09.: Owner spricht erneut vom „ganze netz“ und will die Struktur selbst als Motor.

**Aktueller Stand:** Das Netz ist mindestens als **kausales/epistemisches Beziehungsmodell** plausibel: Intent, Gap, Need/Pain, Capability, Requirement, Acceptance, Umsetzung, Information, Feedback. Es ist **keine** belegte technische Graph-Anforderung. Für historischen Wissensraum bleibt die minimale cross-case Semantik oberhalb Source/Findspot weiterhin unresolved.

### IL-06 – Motorraum: Agenten/Software/Fachmethodik übernehmen Konstruktion und Management; echtes Development statt Prompt-/Markdown-Betrieb

**Früher Stand:** G-007, N-017, CAP-19, #24: mechanisch Automatisierbares automatisieren; deterministic-first; Development ist echte Umsetzungsdisziplin.

**Entwicklung:**
1. 02.09.: owner pain – Mensch/Chat orchestriert zu viel.
2. 03./20.09.: Meta-/Governance-Wachstum soll reale Capability nicht ersetzen.
3. 23./24.09.: Bounded Execution macht den **Repository-Umbau** in Coding-Kontexten ausführbar.
4. 24.09.: Owner formuliert Motorraum explizit: Agenten erstellen Logik/System und managen technischen wie domainspezifischen Teil; Motorraum braucht echtes Development.

**Aktueller Stand:** Es existiert realer Motorraum-Code, aber vor allem für Assurance/State/Execution-Schutz. Der Forschungs-Motor selbst ist nur teilweise implementiert.

**Unklar:** Ob „Agenten … managen es“ nur die Bau-/Betriebsmethode meint oder auch eine spätere Produktlaufzeit. Das Repo sagt weiterhin zu Recht: mehrere Fachkompetenzen implizieren keine Produkt-Multi-Agent-Architektur. Diese Bestandsaufnahme entscheidet die Spannung nicht.

### IL-07 – Owner-Kontrolle über Fundamente ohne Black Box; Fenster in den Motorraum

**Früher Stand:** Human-in-the-loop, Challengeability, providerunabhängiger/restartbarer State, kein Chat-/Tool-Wissensmonopol, Research/Mediation-Boundary.

**Entwicklung:** Der Owner präzisiert am 24.09., dass Delegation an Motorraum nicht Kontrollverlust bedeutet. Gewünscht ist „eine gewisse Kontrolle über die fundamente“, kein UI, das nach Erstellung hermetisch und unpflegbar wird. Gleichzeitig muss nicht jede Fundamentstruktur im Primärraum sichtbar sein.

**Aktueller Stand:** Reversibilität, Git-Provenienz, offene Formate und Drill-down passen dazu. Ein explizites **Fenster-Konzept** – welche Motorraum-Aspekte der Owner wie sehen, verstehen, challengen oder reparieren können muss – ist im Repo nicht als eigener aktueller Intent beschrieben.

### IL-08 – Research-first, lean, kein Meta-Sumpf; sichtbarer Erkenntnisgewinn vor Systemselbstbeschreibung

**Früher Stand:** G-001/G-012, N-020, P-016, #24: kleinste hinreichende Technik, vorhandene Tools vor Eigenbau, kein Konzeptpapier.

**Entwicklung:**
1. 03.09.: Governance-Sumpf und verwaschene Piloten als Owner-Pain.
2. 03.09.: Modulkonzept NOT PASS.
3. 20.09.: „genügend konzeptionelle Bausteine“; Invarianten an heterogenen Fällen falsifizieren; Synthese als sichtbares Primärprodukt.
4. 23.09.: Fresh Rebuild reduziert alte Roadmap zu Prior Art und baut nur WP1 bounded.
5. 24.09.: „wir sind noch im bauen und da ganz am Anfang und die Baustelle steht im Morast“.

**Aktueller Stand:** Das Repo hat Anti-Pathology-/Lean-Regeln und bounded execution deutlich verbessert. Trotzdem bestehen viele alte offene Owner/PRs/Branches und ein sichtbares Produkt bleibt aus. Der Morast ist daher teilweise reduziert, nicht empirisch beseitigt.

### IL-09 – Die Why→What→How→Use-Schleife selbst soll zum Entwicklungs-Motor werden

**Früher Stand:** #10/#28/#41/#42 etablieren Goal/Need/Pain → Capability → Requirement; #63 ergänzt Decision → Implementation → Verification → Feedback.

**Entwicklung:** REQ-TRACE-001 macht Rückführung materieller Technik auf G/N/P maschinenprüfbar. Reales Feedback kann pain-persists/new-need/requirement-change erzeugen. Am 24.09. setzt der Owner zwei neue vorgelagerte Größen: **Intent** und **Erkenntnislücke**, und benennt „Ziel diese struktur als motor“.

**Aktueller Stand:** Der Motor ist **formal nur ab G/N/P geschlossen**. Intent und Erkenntnislücke sind nicht first-class. Der Übergang Feedback → aktualisierte Intent-/Gap-Linie ist nicht deterministisch oder systematisch operationalisiert. Genau deshalb können spätere Owner-Schärfungen in Kommentaren, Working Synthesis und Projekt-State auseinanderlaufen.

---

## 4. Nachzieh-Status

Legende: **nachgezogen** = aktueller Intent in diesem Artefakt seiner Rolle entsprechend erkennbar; **teilweise** = Kern vorhanden, jüngere Schärfung/Relation fehlt; **nicht nachgezogen** = aktuelle Linie dort nicht erkennbar; **widersprüchlich** = Artefakt trägt aktiv eine ältere, mit späterem Owner-Stand kollidierende Form.

Hinweis: „nicht nachgezogen“ bedeutet bei AGENTS/Architecture nicht automatisch Fehler; ein Artefakt kann absichtlich nicht der semantische Owner dieser Linie sein.

| Intent-Linie | G/N/P – problem-baseline | Capability Map | Requirements + Acceptance | README | AGENTS | PROJECT_STATE | Architecture / aktive Cases | Befund |
|---|---|---|---|---|---|---|---|---|
| IL-01 Informationsraum / Erkenntnis im Owner | teilweise | teilweise – CAP-17 | teilweise – UX-001/003 | teilweise | nicht nachgezogen – Governance-Zweck | teilweise | teilweise – owner-facing workplace als Capability | „Informationsraum“, Passfähigkeit zur Owner-Kompetenz und letzte Erkenntnislücke im Kopf fehlen als aktuelle explizite Semantik. |
| IL-02 doppelte Blindheit / Übersetzung | teilweise – Fachblindheit gut, Technikblindheit nicht explizit | teilweise – CAP-01/02 | teilweise – EPI/MTH/UX | teilweise | teilweise – Capability-first/Handoff | teilweise | teilweise | Jüngster Doppelblindheits-Befund vom 24.09. noch nirgends nachgezogen. |
| IL-03 Strenge ermöglicht Nutzbarkeit | nachgezogen | nachgezogen | nachgezogen | nachgezogen | nachgezogen | nachgezogen | nachgezogen | Kein sachlicher Widerspruch gefunden; Problem liegt in Sicht/Arbeitsfluss, nicht Normbasis. |
| IL-04 excerpt-zentrierte Evidenz | teilweise | teilweise – CAP-04/08/17 | teilweise – SRC/UX/EPI | teilweise | teilweise | nachgezogen – next action | teilweise; **widersprüchlich** in u2-modulares-forschungs-und-suchinventar.md | Jüngste Excerpt-Schärfung in #55/#63/#92 vorhanden; altes Modul-Artefakt weiterhin aktiv bezeichnet. |
| IL-05 transformierbarer Wissensraum / Netz | teilweise – Working Synthesis 20.09 | teilweise | teilweise; absichtlich keine Ontologie-Promotion | teilweise | nicht nachgezogen | teilweise | teilweise / unresolved | Gute Re-Klassifikation als User Research; aktuelle „ganze netz“/Motor-Verknüpfung fehlt. |
| IL-06 Motorraum / echtes Development | teilweise | teilweise – CAP-19/20 | teilweise – WF/LEAN/STATE/TRACE | teilweise | nachgezogen für Rebuild Execution | teilweise | teilweise – viel Supporting Code, Produktmotor lückenhaft | Bounded Rebuild Execution ≠ fertiger Forschungs-Motor. Agenten-Laufzeitintent unklar. |
| IL-07 Kontrolle / Fenster / nicht hermetisch | teilweise – N-015/017, P-010/015 | teilweise – CAP-17/20 | teilweise – STATE/UX/WF | teilweise | teilweise | teilweise | teilweise | Reversibilität/Drill-down vorhanden; „Fenster“ und Owner-Reparierbarkeit nicht explizit. |
| IL-08 Research-first / Anti-Meta | nachgezogen in P-016 + 20.09 Synthesis | teilweise | nachgezogen in LEAN/TRACE | teilweise | nachgezogen als Anti-Pathology/Bounded | teilweise | teilweise; alte offene Artefakte/PRs bleiben | Prozessregeln wurden stark nachgezogen, empirischer Owner-Nutzen noch offen. |
| IL-09 Struktur als Motor | teilweise | teilweise | teilweise – REQ-TRACE ab G/N/P | nachgezogen ab G/N/P | teilweise | nachgezogen ab G/N/P | teilweise | Intent + Erkenntnislücke fehlen als upstream Knoten; Feedback→Intent/Gap-Revision bleibt manuell. |

### Konkrete veraltete oder nur teilweise nachgezogene Stellen

1. **docs/research/discovery/problem-baseline.md**  
   Der Post-baseline-Abschnitt endet mit Stand 2026-09-20. Die Owner-Schärfungen vom 23./24.09. – Informationsraum, Erkenntnislücke, Motorraum/Fenster und doppelte Blindheit – fehlen. Das ist keine automatische Aufforderung zur Änderung; es ist ein Ist-Befund.

2. **docs/research/synthesis/capability-map.md**  
   CAP-17, CAP-19 und CAP-20 decken Human Readability, Automation und Restartability ab. Der neuere Intent „Informationsraum passend zu meinen Kompetenzen“ ist nicht explizit. Acceptance Seeds prüfen Audit-Navigation, nicht die Fähigkeit des Owners, seine letzte Erkenntnislücke tatsächlich zu schließen.

3. **requirements-baseline.md / requirements-extensions.md**  
   Viele jüngere Bedarfe sind bereits abgedeckt. Das Repo dokumentiert selbst, dass spätere Präzisierungen keine zweite Requirement-Schicht bilden sollen. Nicht abgebildet ist eine explizite Intent-/Erkenntnislücken-Relation. Dies kann korrekt sein, solange noch kein Requirement-Delta akzeptiert wurde.

4. **README.md**  
   Der Einstieg beschreibt das Ziel als private transdisziplinäre Forschungsassistenz und die G/N/P→Requirement→Delivery→Feedback-Kette. Der sichtbare Owner-Zweck „Informationsraum“ und die Doppelblindheit sind nicht enthalten. Der Einstieg ist stärker System-/Process-orientiert als der jüngste Owner-Wortlaut.

5. **PROJECT_STATE.md**  
   Der Delivery-/Rebuild-Stand ist aktuell. Zugleich nennt #92/PROJECT_STATE den bounded excerpt-zentrierten Sachenbacher-Test als „exakt nächste“ Rebuild-Aktion, während selection-open bestehen bleibt. Das kann als Testfixture statt Research Selection gelesen werden, ist aber für einen neuen Leser semantisch spannungsreich. Der jetzige Owner-Auftrag priorisiert zunächst diese Bestandsaufnahme; PROJECT_STATE wurde gemäß Auftrag nicht verändert.

6. **docs/research/cases/u2-modulares-forschungs-und-suchinventar.md**  
   Header weiterhin working-research / modular-research-inventory; Zweck weiterhin „Netz fachlicher Forschungsmodule“. Das kollidiert direkt mit dem wörtlich erhaltenen Owner-„nicht PASS“ vom 03.09. Keine sichtbare Deprecation/Supersession im File-Header.

7. **docs/architecture/fresh-rebuild-conception-20260923.md**  
   „owner-facing workplace is a required capability“ passt zur Richtung, ist aber noch Architekturvokabular. Der Informationsraum als owner-kognitiver Zielraum ist nicht explizit. Das Dokument sagt selbst, dass Workspace/UI nicht implementiert ist.

8. **Offene PR-/Branch-Artefakte #118–#124 und ältere divergierte Pilotbranches**  
   Sie enthalten teils Diagnose-/Lösungshypothesen aus einem früheren Stand und sind 60 bis 233 Commits hinter main. Ihre Offenheit erzeugt Leserauschen; sie besitzen laut aktuellem #92 keine automatische Authority.

---

## 5. Offene Punkte

### 5.1 Offene Feedback-/Pain-Records

| Punkt | Status | Seit | Intent-Linie | Was offen ist |
|---|---|---:|---|---|
| FB-20260901-001 | open / requirement-change | 2026-09-01 | IL-09 | Trace-Loop wurde mit REQ-TRACE-001 technisch umgesetzt, Record bleibt bis realer Nutzenbestätigung offen. |
| FB-20260901-002 | open / new-pain | 2026-09-01 | IL-06/08 | CI-/Benachrichtigungs-Pain wurde technisch reduziert; reale Bestätigung der ausreichenden Entlastung fehlt. |
| FB-20260902-003 | open / pain-persists | 2026-09-02 | IL-01/06/08 | Research-Betrieb bleibt zu manuell/chat-orchestriert; Human-readable Workspace/Automation fehlt. |
| FB-20260923-004 | open / pain-persists | 2026-09-23 | IL-01/04/07 | Provenance funktioniert, owner-facing Output ist zu maschinenorientiert; excerpt-centered Workflow noch nicht real owner-validiert. |

### 5.2 Weitere explizite offene Zustände / Debt

| Punkt | Status | Seit | Intent-Linie | Bemerkung |
|---|---|---:|---|---|
| selection-open | offen / governing state | mindestens 2026-09-10, aktuell bestätigt 23/24.09 | IL-08/09 | Kein historischer Case ist als aktuelle Selection autorisiert. |
| U2 Modulkonzept | **NOT PASS**, aber Artefakt nicht sichtbar demoted | 2026-09-03 | IL-04/08 | Wörtliche Owner-Korrektur vorhanden; aktive Datei trägt weiter working-research. |
| R51-06 | unresolved | 2026-09-14 | IL-04 | Bounded Locator deckt Vier-Zonen-Prosa nicht vollständig; kein offener Human-Gate, aber Scope-Unschärfe bleibt. |
| Domain Method Profiles #60 | method debt / nicht hinreichend operationalisiert | 2026-08-31 | IL-02/03/06 | Konkrete SOTA-Playbooks/Inferenzregeln/Evidence Appetite der priorisierten Domänen noch unvollständig. |
| Minimaler cross-case State oberhalb Source/Findspot | unresolved review question | 2026-09-20 | IL-05 | Observation/Entity/Relation/Question/Synthesis-Generalisierung ungeklärt. |
| Owner-facing Workspace/Informationsraum | unmet | spätestens 2026-09-02 | IL-01/07 | Fresh Rebuild nennt Capability, aber kein integriertes Produkt vorhanden. |
| General Zotero↔OneDrive Resolver | planned/read-first only | 2026-08-31 | IL-04/06 | Kein allgemeiner Provider Resolver. |
| OCR/HTR Runtime #52 | planned / benchmark-required | 2026-08-31 | IL-04/06 | Kein allgemeiner Processor. |
| Historical Retrieval #53 | planned; alter PR #119 stale | 2026-08-31 | IL-04/06 | Kein allgemeiner exact/variant Retrieval Runtime auf main. |
| Research Promotion Runtime #54 | planned | 2026-08-31 | IL-03/06 | Assurance existiert; generische Research-Object-Transitions nicht. |
| Rights Admission #56 | planned | 2026-08-31 | IL-03/07 | Kein operational admission evaluator. |
| Provider Removal/Restore #57 | planned | 2026-08-31 | IL-07 | Kein allgemeiner Export/Restore/Provider-removal Runtime. |
| DD-20260903-001 #44 | blocked-dependency | 2026-09-03 | IL-07/08 | main serverseitig weiter unprotected; Required PR + Project Assurance muss durch Repo-Admin gesetzt werden. |
| Requirements QA migration warnings | 45 Warnungen, 0 Fehler | 2026-09-24 aktueller Lauf | IL-09 | Bestehende Migration Debt; kein aktueller Hard Failure. |
| Unabhängige Fach-/Technikvalidierung | Review-Lücke als **nicht gemergter** #138-Befund | 2026-09-24 | IL-02/03/07 | Nicht als kanonische Wahrheit behandeln; unabhängiger Review liegt einen Commit vor main. |

### 5.3 Offene Pull Requests und nicht gemergte Branches

Alle sechs offenen PRs stammen aus dem Zeitraum 20.–21.09. und ihre Heads sind gegenüber main@65b8e8f divergiert.

| PR / Branch | Status gegen main | Intent-Bezug | Ist-Befund |
|---|---|---|---|
| #118 research/sociotechnical-deep-research-20260920 | 7 Commits ahead / 60 behind | IL-06/08 | Research-/Solution-Hypothesen; aktuelle #92-Conception ist jünger. |
| #119 dev/calibration-exact-retrieval-20260920 | 26 ahead / 60 behind; draft | IL-04/06 | Alter Retrieval-/Agent-Calibration-Pfad; #53 aktuell nicht automatisch selected. |
| #120 research/systemic-project-development-pattern-audit-20260921 | 3 ahead / 60 behind | IL-08/09 | Audit-Input, nicht Current-State Authority. |
| #122 audit/121-independent-replication-20260921 | 2 ahead / 60 behind | IL-08/09 | Independent replication/reconciliation; nicht gemergt. |
| #123 research/prompt-experiment-provenance-20260921 | 14 ahead / 60 behind | IL-06/08 | Prompt-/Execution-Research, jünger durch bounded execution überholt/zu prüfen. |
| #124 research/deepresearch-mode-replication-20260921 | 1 ahead / 60 behind | IL-06/08 | Research-Input; nicht integriert. |
| audit/independent-holistic-review-20260924 | **1 ahead / 0 behind**, kein PR | IL-01/02/03/06/07/08/09 | #138 Review-Freeze; aktuellster nicht gemergter Analyseinput. |
| delivery/61-current-context-resume | 3 ahead / 233 behind, kein PR | IL-06/07 | Stark stale; current main enthält jüngere Context-Mechanismen. |
| pilot/explorative-research-network-20260907 | 10 ahead / 162 behind, kein PR | IL-05 | Alte Pilot-/Netzhypothese; Status gegenüber Current State unklar. |
| pilot/ranis-layered-archive-20260906 | 13 ahead / 162 behind, kein PR | IL-04/05 | Alte Pilotarbeit; gegenüber #86/#89 und main stark stale. |

Alle übrigen aktuell sichtbaren Branch-Refs haben gegenüber main keine einzigartigen Commits mehr (ahead_by=0) und sind damit historische/merged Branch-Referenzen, kein eigenständiger offener Content.

### 5.4 Alle offenen Issues

„Open“ wird hier **nicht** mit „aktives WIP“ gleichgesetzt. Viele Issues sind dauerhafte Owner oder Registers. Wo der aktuelle Body keinen klaren nächsten aktiven Schritt ausweist, steht dies ausdrücklich.

| Issue | Seit offen | Kurzstatus am 24.09. | Intent-Linie |
|---|---:|---|---|
| #1 Research Design / Arbeitsstand | 2026-08-30 | dauerhafter Konzept-/State-Owner; jüngere Intent-Schärfungen nur teilweise enthalten | IL-01–09 |
| #2 Persönlicher Archivar | 2026-08-30 | validierter Need / role-scope-evolving | IL-02/04 |
| #3 Zotero-Kopplung | 2026-08-30 | validated direction; alte SSOT-Hypothese verworfen | IL-04/06/07 |
| #4 OCR/Volltext | 2026-08-30 | validated need / solution research needed | IL-04/06 |
| #5 Historical Search | 2026-08-30 | validierter Search-Need; Umsetzung unter #53 offen | IL-04/06 |
| #6 Git-Provenienz | 2026-08-30 | Arbeitsprinzip + offene Architekturfragen | IL-07/09 |
| #8 Automatisierbar/KI-unabhängig | 2026-08-30 | Zielvorgabe + Architekturhypothese | IL-06/07/08 |
| #9 Wissensgovernance/HITL | 2026-08-30 | dauerhafte Governance | IL-03/07 |
| #10 Research Plan | 2026-08-30 | Prozess-/Trace-Owner | IL-08/09 |
| #12 paleo-type Prior Art | 2026-08-30 | Prior Art; keine Histo-Orla-Authority | IL-06/07/08 |
| #13 transdisziplinäres Zielbild | 2026-08-30 | strategischer Scope | IL-02/05 |
| #14 Multi-Scale / Connected History | 2026-08-30 | strategischer Scope, 19.09 erweitert | IL-05 |
| #15 Expertenmodell / Unsicherheit | 2026-08-30 | strategische Anforderung | IL-02/03 |
| #16 regionalisierte Spitzenexpertise | 2026-08-30 | strategisches Zielbild | IL-02 |
| #19 Assistenz-Ökosystem | 2026-08-30 | strategisch; technische Agentenform ausdrücklich offen | IL-02/06 |
| #20 Research vs Vermittlung | 2026-08-30 | strategische Boundary | IL-01/03/07 |
| #21 RGK Prior Art | 2026-08-30 | Prior Art | IL-03/05 |
| #22 Kompetenzlandkarte | 2026-08-30 | Kompetenz-/Research-Workframe | IL-02/09 |
| #23 Issue Governance | 2026-08-30 | dauerhafte Governance | IL-08/09 |
| #24 Software-/Systemkompetenzen | 2026-08-30 | strategisch, architecture-research-needed | IL-06/08 |
| #26 Detailkonsolidierungs-Arbeitsplan | 2026-08-30 | alter Plan-Owner; Current-State-Relevanz nicht neu dispositioniert | IL-08/09 |
| #42 Requirements | 2026-08-30 | **kanonischer Requirements Owner, aktiv** | IL-03/09 + alle downstream |
| #44 Decision/Dependency Register | 2026-08-30 | aktiver Register; DD-20260903-001 weiter blocked | IL-07/08 |
| #45 Research Protocol | 2026-08-30 | bindender Research-/Evidence-Rahmen | IL-03 |
| #46 U2 Knau/Orlagau | 2026-08-31 | aktiver Research Owner; nicht automatisch selected | IL-04/05 |
| #47 U1 Teich-/Feuchtlandschaft | 2026-08-31 | aktiver Research Owner, unreifer als U2 | IL-01/05 |
| #48 Technical Lead | 2026-08-31 | aktiver Technical Owner | IL-06/08/09 |
| #49 Zotero↔OneDrive | 2026-08-31 | open architecture spike; kein allgemeiner Resolver | IL-04/06/07 |
| #50 Canonical Research State | 2026-08-31 | Contract-Owner; WP1 deckt nur kleinen Spine | IL-04/05/07 |
| #52 OCR/HTR | 2026-08-31 | planned / P1 / reversible benchmark | IL-04/06 |
| #53 Retrieval | 2026-08-31 | planned; aktuell nicht ausgewählter rebuild step | IL-04/06 |
| #54 Promotion/Invariants | 2026-08-31 | planned contract | IL-03/06 |
| #55 Human-readable Audit | 2026-08-31 | owner-feedback-pain-persists; excerpt-test next | IL-01/04/07 |
| #56 Rights Admission | 2026-08-31 | planned architecture contract | IL-03/07 |
| #57 Provider Removal | 2026-08-31 | planned verification spike | IL-07 |
| #58 ADRs JIT | 2026-08-31 | dauerhafte Decision-Boundary | IL-08 |
| #59 Development & Verification | 2026-08-31 | aktiver Delivery Owner | IL-06/09 |
| #60 Domain Method Profiles | 2026-08-31 | **Method Debt offen**, Profile nicht hinreichend operationalisiert | IL-02/03/06 |
| #61 Work Context/Method/Handoff | 2026-08-31 | offen; kein globaler blocker | IL-06/07 |
| #62 Requirements Assurance | 2026-09-01 | v0.1 implementiert; Issue als Assurance-Owner offen | IL-03/09 |
| #63 Value/Decision/Delivery/Feedback | 2026-09-01 | v0.1 technisch verified; feedback loop open | IL-09 |
| #64 Product/Research-Value vs Governance | 2026-09-01 | Review Owner; mehrere Hypothesen weiterhin unresolved | IL-01/08/09 |
| #65 Wissensarbeit Pilot Review | 2026-09-02 | Review input; kein automatic promotion | IL-05/08 |
| #66 Default-Branch-Schutz | 2026-09-02 | offen; hängt mit #44 DD zusammen | IL-07/08 |
| #67 Project Memory | 2026-09-02 | offen; Teile durch AGENTS/Context umgesetzt, Reststatus nicht reconciliiert | IL-07/09 |
| #85 Ranis Materialkorpus | 2026-09-06 | Pilot offen; Korpus-/Provenienzarbeit | IL-04/05 |
| #86 Shared Research State Ranis | 2026-09-07 | reframed / prototype-complete / evaluation-next | IL-05/07 |
| #89 Eval #86 | 2026-09-07 | Fresh-context Evaluation offen | IL-05/07 |
| #92 Architecture Re-baseline | 2026-09-10 | conception complete; WP1 verified; pain persists; excerpt-test next | IL-06/08/09 |
| #103 Anno/Richeza/Saalfeld | 2026-09-18 | aktiver independent-not-selected Research Owner; observation-first | IL-01/04/05 |
| #121 Independent blind audit | 2026-09-21 | Independent audit/reconciliation open; PR #122 stale | IL-08/09 |
| #138 Independent holistic review | 2026-09-24 | Review läuft auf nicht gemergtem Branch; Phase-6-Freeze vorhanden | IL-01/02/03/06/07/08/09 |

---

## 6. Erkenntnislücken je Intent-Linie

Die „Erkenntnislücke“ ist im bisherigen Repo keine first-class Entität. Die folgenden Zuordnungen sind deshalb **KI-Ableitungen aus den Quellen**, sofern nicht ausdrücklich als beobachtete historische Frage ausgewiesen.

| Intent-Linie | Historische Erkenntnislücke | Verständnis-/Urteilslücke des Owners | System-/Motorlücke | Was würde die Lücke verkleinern? |
|---|---|---|---|---|
| IL-01 Informationsraum | Je aktuellem Research Case: konkrete historische Frage bleibt teils unresolved; U1/U2/#103 besitzen eigene Lücken. | Welche Befunde sind belastbar, was bedeuten sie und was ist als Nächstes relevant, ohne Fachausbildung? | Kein integrierter Informationsraum, der Evidenz→Synthese→Alternativen→next evidence owner-tauglich verbindet. | Realer owner-facing Research Slice mit messbarer Verständlichkeit/Entscheidbarkeit und Drill-down. |
| IL-02 doppelte Blindheit | Historische Fachfragen benötigen oft Domänenwissen, das im Projekt nur teilweise als working method operationalisiert ist. | Owner kann weder fachliche noch technische Qualitätsbehauptungen vollständig selbst beurteilen. | Domain Method Profiles unvollständig; unabhängige qualifizierte Reviewpfade nur punktuell; technische Erklärbarkeit/Reparierbarkeit nicht owner-erprobt. | SOTA-belegte working methods + proportionale unabhängige Fach-/Technikstichproben + owner-kompatible Erklärung der Grenzen. |
| IL-03 Strenge als Enabler | Unsicherheit/Widerspruch/Überlieferungslücken bleiben fachlich real und dürfen nicht „geschlossen“ werden. | Owner muss verstehen können, warum ein Ergebnis unresolved oder nur working ist, ohne die ganze Governance zu lernen. | Guards existieren, aber die Übersetzung ihrer Bedeutung in den Informationsraum fehlt. | Sicht, die Unsicherheit/Evidenzstatus kontextuell erklärt statt nur Statuscodes zu zeigen. |
| IL-04 excerpt-zentriert | Bei jeder Quelle: was steht wo, mit welchem Kontext, welche Aussage trägt sie, welche nicht? | Owner braucht Quelle selbst + verständliche Einordnung; Locator allein reicht nicht. | #51 Roundtrip ist bounded; kein allgemeiner Text-/Image-Excerpt-Workflow, Retrieval und OCR fehlen. | Bounded excerpt-centered Realtest mit exakter Instance, Text/Bild, Finding/Interpretation, owner review. |
| IL-05 Wissensraum/Netz | Cross-case: welche Identitäten/Beobachtungen/Relationen sind tatsächlich wiederverwendbar und welche kontextabhängig? | Owner hat Mental Models („Netz“, transformieren), kann technische/fachliche Generalisierung aber nicht selbst validieren. | Minimale shared semantic unit oberhalb Source/Findspot offen; Query/View-Layer fehlt. | Heterogene Gegenfälle und Reuse-Experimente, die Link/Search/View gegen stärkere Shared-State-Modelle falsifizieren. |
| IL-06 Motorraum | Fachmethodische Lücken beeinflussen, was überhaupt automatisierbar ist. | Owner kann Implementation/Agentenentscheidungen nicht technisch selbst auditieren. | Viel Supporting Code, aber fehlende Kern-Capabilities; Agenten-Laufzeitrolle unklar. | Echte vertikale Capability-Implementierung mit klarer Authority, Tests und owner-visible outcome; unabhängiger Tech-Review dort, wo Konsequenz hoch ist. |
| IL-07 Kontrolle/Fenster | Historische Wahrheit bleibt fachlich unsicher; Kontrolle darf keine Scheinsicherheit erzeugen. | Welche Fundamente muss Owner verstehen/ändern können, welche darf er delegieren? | Kein expliziter „window/control“ contract; Recovery durch nichttechnischen Owner nicht belegt. | Konkreter Owner-Recovery/Challenge-Test: provenance, state, decision rationale, rollback, export verständlich und ausführbar. |
| IL-08 Research-first | Historische Programme sind noch nicht abgeschlossen; selection-open trennt Forschungsauswahl von Technikarbeit. | Owner muss erkennen können, ob neue Meta-Arbeit echten Forschungsnutzen bringt. | Viele alte offene Artefakte/PRs; Nutzen/Meta-Verhältnis wird nicht systematisch als Delivery-Signal genutzt. | Wenige reale Research Tasks mit gemessener Owner-Orchestrierung, Research lead time und Rework; alte WIP dispositionieren. |
| IL-09 Struktur als Motor | Welche historische Lücke Priorität hat, muss aus Research Context kommen, nicht aus Technik. | Owner muss Intents justieren können, ohne Requirements Engineering selbst zu betreiben. | Intent- und Gap-Knoten fehlen; Feedback→Discovery-Revision manuell; G/N/P-Baseline hinkt jüngstem Owner-State hinterher. | Ein zunächst **nur analytisch** getestetes Relationenschema/Arbeitsverfahren, das neue Owner-Signale gegen vorhandene Intent/Gaps/GNP/CAP/REQ abgleicht, bevor irgendetwas promoted wird. |

### Offene historische Erkenntnislücken, die nicht sauber einer einzelnen Intent-Linie gehören

- U2/Knau/Orlagau enthält weiterhin source- und case-spezifische unresolved Pfade; selection-open verhindert, dass daraus automatisch das aktuelle Hauptforschungsprogramm wird.
- U1/Teich-/Feuchtkulturlandschaft ist im Repo deutlich weniger weit erschlossen als U2.
- #103 enthält bewusst unresolved Primärquellen-/Identitäts-/Chronologiepfade und bleibt independent-not-selected.
- Ranis/#85–#89 enthält Availability- und Method-Debt-Grenzen; einige Bytes sind nicht inspectable.
- Der Status „welche historische Frage ist jetzt die wichtigste?“ ist selbst offen, weil selection-open gilt.

---

## 7. Motor-Netz mit Bruchstellen und Zuordnung Motorraum / Informationsraum / Fenster

### 7.1 Das heute tatsächlich vorhandene Netz

~~~text
[Owner-Signal / Gespräch / reale Nutzung]
        |
        |  teils User Research, teils Feedback
        v
[Goal / Need / Pain / Constraint]  #28
        |
        v
[Capability + Quality / Invariant] #41
        |
        v
[accepted Requirement]             #42
        |
        +--> [Acceptance / Verification]
        |
        v
[Technical Derivation]             #48
        |
        v
[Decision / Implementation]        #59 / #63
        |
        v
[Verification]
        |
        v
[real use / Owner feedback]        #63
        |
        +---- confirms / pain-persists / new-pain / new-need / req-change
        |
        └---- manuell zurück in Discovery / Requirements / Delivery
~~~

Der Owner beschreibt am 24.09. ein weiter vorgelagertes und weiter nach außen reichendes Netz:

~~~text
Intent
  ↓
Erkenntnislücke
  ↓
Goal / Need / Pain / Constraint
  ↓
Capability
  ↓
Requirement
  ↓
Acceptance
  ↓
Umsetzung / Motorraum
  ↓
Informationsraum
  ↓
Erkenntnis beim Owner
  ↓
Rückmeldung / neue oder geschärfte Erkenntnislücke
  ↺
~~~

**Beobachtung:** Die zweite Form ist heute **nicht** kanonisch operationalisiert. Sie ist Owner-Input aus Anhang A und Gegenstand dieser Bestandsaufnahme.

### 7.2 Bruchstellen

1. **Intent fehlt als eigener Knoten.**  
   Frühere „Zielbilder“, Goals, Visionen und Owner-Feedback tragen Intent, aber die Genealogie konkretisiert/verallgemeinert/ersetzt nicht maschinen- oder menschenlesbar als Relation.

2. **Erkenntnislücke fehlt als eigener Knoten.**  
   Historische Research Questions, Needs, unresolved Findings und Method Debt existieren, aber „welche Lücke im Wissen/Verstehen/System löst dieser Intent?“ ist nicht systematisch verbunden.

3. **Owner-Signal → G/N/P ist nicht aktuell geschlossen.**  
   Die problem-baseline hat einen guten Post-baseline-Syntheseabschnitt bis 20.09. Die 23./24.09-Schärfungen fehlen.

4. **G/N/P → CAP → REQ ist stark, aber historisch geschichtet.**  
   Viele spätere Präzisierungen sind absichtlich keine neuen Requirements. Das ist gut gegen Duplikation, macht aber nötig, Relationstypen wie konkretisiert/geschärft/ersetzt sichtbar zu halten.

5. **Acceptance ist oft capability-/risk-zentriert, nicht immer owner-kognitiv.**  
   Beispiel CAP-17/REQ-UX-001 prüft Navigation/Auditability. Ob der Owner dadurch die Erkenntnislücke wirklich schließen kann, wird erst durch reale Owner-Akzeptanz sichtbar.

6. **Umsetzung ist asymmetrisch.**  
   Formaler Schutz-/Execution-Motor ist weiter als Forschungs-Capabilities. Dies erzeugt die beobachtete Diskrepanz „technisch korrekt, aber maschinentauglich“.

7. **Informationsraum fehlt als integrierter Laufzeitpfad.**  
   Es gibt Markdown-Research-Artefakte, einen Audit Renderer und einzelne Derived Views, aber keinen durchgängigen owner-facing Research Workspace.

8. **Feedback hat Wirkung, aber nicht immer Rückwirkung in Discovery.**  
   #63 kann Deltas erzwingen; die semantische Aktualisierung von Intent/Gaps/GNP bleibt jedoch eine menschlich/KI-manuelle Reconciliation.

9. **Veraltete Semantik kann physisch aktiv bleiben.**  
   Das Modul-Artefakt ist das klarste Beispiel: Owner verwirft das Leitkonzept, die Datei bleibt in aktivem Research-Pfad und nennt sich working.

10. **Current Work Selection und Testfixture können verwechselt werden.**  
    selection-open ist korrekt; zugleich wird Sachenbacher als exakt nächster Workflow-Test genannt. Ohne klare Erklärung kann ein neuer Bearbeiter Testfall mit Research Selection verwechseln.

### 7.3 Motorraum / Informationsraum / Fenster – aktuelle Zuordnung

Die Begriffe stammen aus Anhang A. Folgende Zuordnung ist **KI-Ableitung für die Bestandsaufnahme**, keine neue Architektur.

| Bereich | Was laut Quellen hineinpasst | Aktueller Zustand |
|---|---|---|
| **Motorraum** | Fachmethoden, Source-/Evidence-Logik, Resolver, OCR/HTR, Retrieval, Context, State, Invariants, Rights, Agent-/Software-Ausführung, Development/Tests | Teilweise realer Code; Fachmethodik und viele Product Capabilities noch Beschreibung/Research Debt |
| **Informationsraum** | owner-lesbare Research Outputs, Exzerpte, Karten/Timelines/Strukturen, Synthesen, offene Fragen, Alternativen, Next Evidence – passend zu Owner-Kompetenz | Fragmentiert in Research Markdown/Case-Artefakten; kein integrierter Workspace |
| **Fenster** | Drill-down vom Informationsraum in Motor-/Evidence-Grundlagen: Quelle/Fundstelle, Provenienz, Methode, Unsicherheit, History, Decision/Code soweit nötig | Audit-Renderer und Git/Repo liefern Teile; aktueller Audit ist owner-seitig zu maschinenorientiert |

### 7.4 Wo tatsächlich lauffähiger Code existiert

| Fähigkeit | Code auf main | Einordnung |
|---|---|---|
| Requirements Formal QA | tools/requirements/** | lauffähig / CI-verifiziert |
| Value/Decision/Delivery Trace | tools/assurance/** | lauffähig / CI-verifiziert |
| Enforcement projection/shared mechanics | tools/operational/core.py, enforcement.py/map | lauffähig |
| Mutation guard | tools/operational/mutation.py | lauffähig, bounded/local |
| Context/Resume | tools/operational/context.py, context_spec.py | lauffähiger Prototyp / reale Lampe-Fixture |
| Bounded Rebuild Execution | tools/operational/execution_order.py + Contract | lauffähig; **Bauprozess**, nicht Produkt-Agentenruntime |
| Document/Findspot Roundtrip | tools/document_evidence/** | lauffähig, an realem Sachenbacher-Slice belegt |
| Minimal Research-State Spine | tools/research_state/** | lauffähig / WP1 verified |
| Derived Audit | tools/operational/audit.py | lauffähig, aber Owner-Pain bleibt |
| Zotero/OneDrive general Resolver | kein allgemeiner Runtime-Pfad | Beschreibung/Spike-Evidence |
| OCR/HTR | kein allgemeiner Processor | geplant/Benchmark |
| Historical Retrieval | kein allgemeiner Runtime-Pfad | geplant; alter PR #119 unmerged/stale |
| Research Promotion/Transitions | kein allgemeiner Research-Object-Runtime | geplant |
| Rights Admission | kein Evaluator | geplant |
| Provider Removal/Restore | kein allgemeiner Runtime | geplant |
| Domain Method Execution | keine vollständigen working-method Profiles + Engine | Research Debt; Regeln/Contracts vorhanden |
| Owner-facing Informationsraum | kein integriertes Produkt | unmet |
| „Fenster“/Owner Recovery | Teile über Audit/Git; kein vollständiger Owner-Test | partial |

### 7.5 Anteilige Dubletten und Schärfungen im Netz

Das Repo hat viele **gewollte vertikale Überlappungen**, keine einfachen Textdubletten:
- N-005 → CAP-04 → REQ-SRC-001/002 ist eine Ableitungskette.
- G-009/P-014 → CAP-17 → REQ-UX-001 → REQ-UX-003 ist eine Schärfung von Verständlichkeit/Audit zu Progressive Disclosure.
- REQ-STATE-003 schärft REQ-STATE-001: Restartability braucht nicht nur Identität/Locator, sondern reale Evidence Availability oder einen sichtbaren Blocker.
- REQ-EPI-006 verallgemeinert frühere Layering-Regeln auf explizite epistemische/arbeitsbezogene Zustände.
- REQ-INT-002 spezialisiert Source-Identity-/Provider-Unabhängigkeit auf Zotero/OneDrive/Histo-Orla.

Die größere Lücke ist nicht „zu viele gleiche Texte“, sondern die fehlende durchgängige Relation:
**refines / specializes / generalizes / supersedes / contradicts / confirms / partially-overlaps**. Deshalb können spätere Schärfungen neben älteren Formulierungen liegen, ohne dass ein neuer Leser weiß, ob beide noch gleichrangig gelten.

---

## 8. Vorschläge zur Justierung

**Wichtig:** Alle folgenden Formulierungen sind **Vorschläge/Kandidaten**, ausschließlich aus den Quellen abgeleitet. Sie ändern nichts. Der Owner muss auswählen, kombinieren oder verwerfen.

### IL-01 – aktueller Gesamt-/Informationsraum-Intent ist noch nicht sauber nachgezogen

**Vorschlag A:**  
Histo-Orla soll mir als fachlich und technologisch nicht spezialisiertem Research Owner einen wissenschaftlich belastbaren Informationsraum bereitstellen, in dem ich historische Erkenntnislücken selbst schließen kann, ohne die zugrunde liegende Fach- und Systemkomplexität selbst orchestrieren zu müssen.

**Vorschlag B:**  
Histo-Orla soll aus fachlich sauberem Research State verständliche, prüfbare und zu meinen Kompetenzen passende Forschungsräume erzeugen, in denen ich von einer Frage über Evidenz und Alternativen zu eigener historischer Erkenntnis gelangen kann.

**Vorschlag C:**  
Das Primärprodukt von Histo-Orla ist nicht der technische Research State, sondern ein owner-tauglicher Informationsraum; der Research State und seine Provenienz sind dessen überprüfbarer Unterbau.

### IL-02 – doppelte Blindheit ist neuer als die bestehende Baseline

**Vorschlag A:**  
Weil ich weder die fachwissenschaftlichen noch die technologischen Domänen vollständig beherrsche, muss Histo-Orla beide Kompetenzbereiche professionell aktivieren und ihre Ergebnisse so rückübersetzen, dass ich Forschungsrichtung, Relevanz und offene Unsicherheit beurteilen kann.

**Vorschlag B:**  
Der Owner gibt Erkenntnisinteresse, Kontext und Feedback; die fachliche und technische Übersetzungsarbeit wird vom System bzw. seinen qualifizierten Methoden und Werkzeugen getragen und bleibt für den Owner nachvollziehbar.

### IL-05 – „Netz/Wissensraum“ ist noch Mental Model, kein eindeutiger aktueller Intent

**Vorschlag A:**  
Histo-Orla soll einen langfristig wachsenden, wiederverwendbaren Forschungsbestand tragen, der unter wechselnden historischen Fragen und Fachperspektiven neu projiziert werden kann, ohne Quellen-, Evidenz- oder Fachlogiken zu vereinheitlichen.

**Vorschlag B:**  
Mein Intent ist kein technischer Graph, sondern ein Forschungsnetz: dieselbe belastbare Evidenz soll mehrere Fragen, Maßstäbe und Fachperspektiven unterstützen können, während ihre jeweilige Geltung und Unsicherheit erhalten bleibt.

**Vorschlag C:**  
„Netz“, „Wissensraum“ und „Transformation“ beschreiben zunächst das gewünschte Arbeitsverhalten; die technische Repräsentation soll erst aus realen wiederkehrenden Fällen abgeleitet werden.

### IL-06 – Bedeutung von „Agenten managen den Motorraum“ ist offen

**Vorschlag A:**  
Agenten/Coding-Systeme dürfen den technischen und fachmethodischen Motorraum bauen, testen und warten; daraus folgt keine Multi-Agent-Produktarchitektur. Welche agentische Laufzeitfunktion Histo-Orla selbst braucht, bleibt bedarfsgetrieben offen.

**Vorschlag B:**  
Der Motorraum soll weitgehend maschinell betrieben werden, damit ich ihn nicht manuell orchestrieren muss; Agenten sind dabei ein austauschbares Ausführungsprinzip, nicht die epistemische oder fachliche Autorität.

**Vorschlag C:**  
Ich will, dass Agenten die Komplexität von Development und Fachmethoden praktisch tragen. Der Owner muss aber die Fundamente, Grenzen und Folgen verstehen und challengen können.

### IL-07 – „gewisse Kontrolle über die Fundamente“ braucht Präzisierung

**Vorschlag A:**  
Kontrolle bedeutet für mich: Ich kann Ursprung, Evidenz, Methode, Unsicherheit und wesentliche Systementscheidungen nachvollziehen und bei Bedarf zurückrollen, ohne den Motorraum selbst administrieren zu müssen.

**Vorschlag B:**  
Der Motorraum darf komplex sein, aber nicht hermetisch: Zustände und Entscheidungen bleiben offen, portabel und reparierbar; der Informationsraum bietet ein Fenster auf die relevanten Fundamente.

**Vorschlag C:**  
Ich brauche keine vollständige technische Bedienoberfläche für den Motorraum, sondern verständliche Kontrollpunkte für Provenienz, Forschungsstatus, Änderbarkeit, Export/Recovery und wesentliche Entscheidungen.

### IL-09 – Struktur als Motor ist der jüngste, noch nicht operationalisierte Meta-Intent

**Vorschlag A:**  
Die weitere Entwicklung wird von einem Netz aus Intent → Erkenntnislücke → Need/Pain → Capability → Requirement → Acceptance → Umsetzung → Informationsraum → Feedback gesteuert; neue Arbeit beginnt nur dort, wo eine offene Verbindung in diesem Netz belegt ist.

**Vorschlag B:**  
Nicht Features oder alte Roadmaps bestimmen die nächste Arbeit, sondern die aktuell wichtigste Erkenntnislücke hinter einem Owner-Intent und die daraus belegbar abgeleiteten Needs, Capabilities und Akzeptanzgrenzen.

**Vorschlag C:**  
Feedback aus realer Nutzung schärft zuerst Intent und Erkenntnislücke; erst danach wird geprüft, ob bestehende Needs/Requirements genügen oder tatsächlich ein Delta nötig ist.

---

## 9. Fragen an mich

1. **Ist „Informationsraum“ für dich heute der primäre Produkt-Intent von Histo-Orla – also der Raum, in dem du historische Erkenntnis bildest – während Research State, Fachmethoden, Agenten und Technik primär Motorraum sind?**

2. **Wenn du sagst „Die Agenten erstellen die logik das System und managen es“: meinst du damit vor allem den Bau/Betrieb des Systems, oder soll auch das spätere Histo-Orla-Produkt zur Laufzeit agentisch Fach- und Technikarbeit orchestrieren?**

3. **Soll der langfristige „Wissensraum/das ganze Netz“ als stabiler Intent gelten („derselbe Forschungsbestand muss unter wechselnden Fragen/Perspektiven nutzbar sein“), während Graph/Objektmodell/Taxonomie ausdrücklich offen bleiben – oder ist selbst dieser Wissensraum noch nur ein zu prüfendes Mental Model?**

4. **Was bedeutet „gewisse Kontrolle über die fundamente“ für dich konkret am ehesten: verstehen/challengen können, Zustände selbst korrigieren können, Export/Restore/Rollback können, technische Entscheidungen mitsteuern – oder eine Kombination davon?**

5. **Soll der aktuell im Repo genannte excerpt-zentrierte Sachenbacher-Test nach dieser Bestandsaufnahme weiterhin der nächste reale Workflow-Test sein, oder soll selection-open jetzt tatsächlich zuerst aus dem Intent→Erkenntnislücken-Netz eine neue Test-/Forschungsquelle wählen?**

---

## 10. Grenzen der Bestandsaufnahme

### 10.1 Zugängliche Quellen

Für diese Bestandsaufnahme wurden frisch gegen GitHub gelesen bzw. inventarisiert:

- main@65b8e8f27658e4a2480f59503eaa9064fe4c5c58;
- AGENTS.md, PROJECT_STATE.md, README.md;
- der aktuelle main-Dokumentbaum (125 Blob-Dateien);
- die Discovery-, Capability-, Requirements-, Method-, Architecture-, Development- und Assurance-Kernartefakte;
- alle 78 Issues als Repository-Inventar und die für Intent/Open-State relevanten Bodies/Kommentare vertieft;
- der repo-weite Issue-Kommentarstrom, einschließlich explizit persistierter Owner-Feedback-Kommentare;
- alle 60 PRs als Inventar, mit Vertiefung der sechs aktuell offenen PRs;
- alle 425 Commits auf main vom 29.08. bis 23.09.; Commit-Historie wurde auf Intent-/Korrektur-/Reconciliation-Signale durchsucht;
- alle aktuell sichtbaren Branches, einschließlich Ahead/Behind-Vergleich für Branches mit möglichem einzigartigem Content;
- tools/assurance/data/trace-records.json vollständig;
- der nicht gemergte Branch audit/independent-holistic-review-20260924 / #138 als ausdrücklich **nicht kanonischer Review-Input**;
- Anhang A aus dem Owner-Auftrag vollständig und wörtlich.

### 10.2 Nicht zugänglich / nicht belegt

1. **Private frühere Chats** liegen nicht vollständig im Repository. Deshalb kann diese Datei nicht garantieren, jede historische Owner-Äußerung wörtlich erfasst zu haben.
2. Bei vielen Repo-Texten ist der GitHub-Autor esany, laut Anhang A sind die Artefakte jedoch vollständig KI-generiert. Ein Commit/Merge beweist deshalb **keinen wörtlichen Owner-Wortlaut und kein fachliches Verständnis**. Wo kein Rohzitat vorliegt, wurde die Herkunft entsprechend herabgestuft.
3. **Anhang B** wurde in diesem Auftrag nicht bereitgestellt. Es wurden daher keine zwei externen Analyseberichte als eigene externe Hinweisquelle eingearbeitet. Der #138-Branch ist Repository-intern und wurde getrennt als nicht gemergter Review behandelt.
4. Die Bestandsaufnahme hat **keine externe fachwissenschaftliche oder softwaretechnische Validierung** durchgeführt. Sie fragt, was das Repo und die Owner-Signale sagen, nicht ob jede bestehende Requirement-/Methodenannahme fachlich richtig ist.
5. Kein lokaler Arbeitsbaum außerhalb GitHub wurde inspiziert. Nicht gepushte lokale Änderungen sind daher nicht erfasst.
6. Alte offene Issues/Branches wurden nicht durch diese Bestandsaufnahme geschlossen oder semantisch dispositioniert. „Open“ bedeutet nicht automatisch „noch zu erledigen“; bei langlebigen Owner-Issues ist der Status teilweise absichtlich dauerhaft offen.
7. Die Vorschläge in Abschnitt 8 sind **keine** neuen Intents, Requirements oder Entscheidungen. Sie sind sprachliche Kandidaten zur Owner-Justierung.
8. Diese Datei selbst aktualisiert **keinen** Goal-, Need-, Pain-, Capability-, Requirement-, Acceptance-, Architecture-, PROJECT_STATE- oder Issue-Status. Das ist Absicht des Auftrags.
9. Die Zuordnung Motorraum / Informationsraum / Fenster ist eine **KI-Ableitung aus Anhang A und bestehendem Repo-State**. Sie ist keine neue Architektur und keine akzeptierte Terminologie.
10. Der Bericht kann zeigen, wo jüngere Befunde ältere Aussagen konkretisieren, schärfen, verallgemeinern, ersetzen oder widersprechen. Er entscheidet jedoch nicht, welche Variante künftig kanonisch sein soll. Diese Entscheidung bleibt beim Owner bzw. den bestehenden Authority-Pfaden.
