# Histo-Orla – Phase Reconciliation: Lean/Agile MVP Delivery

**Status:** `owner-resolved / build-admitted / 2026-08-31`  
**Requirements / Acceptance Owner:** #42  
**Technical Lead / Delivery Owner:** #48  
**MVP Development:** #59  
**Domain Method Research:** #60  
**Live Research:** #46/#47

## 1. Owner-Entscheidung

Histo-Orla ist ein **privates, leanes und agiles Forschungssystem**. Time-to-first-use ist ein harter Produktwert. Das Projekt soll nicht erst nach monatelanger Vorab-Research-/Architecture-Phase nutzbar werden.

Der Research Owner hat am 31.08.2026 verbindlich präzisiert:

1. Die im Domain-Research-/Methodenstrang formulierten **Systemanforderungen sind Owner-accepted MVP-Akzeptanzkriterien**.
2. Das MVP wird **jetzt inkrementell gebaut** und im realen Forschungsgebrauch gehärtet.
3. Fachmethodischer SOTA, technische SOTA/Best Practice, Requirements-Schärfung und Architekturentwicklung laufen **parallel und rückgekoppelt**, soweit sie konkrete Entscheidungen oder Qualitätsrisiken tragen.
4. Nicht jede methodische oder technische Ungewissheit blockiert Development. Sie muss als Status/Research Debt sichtbar bleiben und darf wissenschaftliche Promotion nicht vortäuschen.
5. Architektur ist **evolutionär / just-in-time**: so viel Design vor einer Entscheidung wie für Reversibilität, Integrität, Sicherheit und wissenschaftliche Qualität nötig; nicht mehr.

Diese Entscheidung hebt die wissenschaftlichen Schutzinvarianten nicht auf. Sie ändert den Delivery-Modus.

## 2. Korrektur des vorigen Re-Gate-Modells

Die vorherige Reconciliation hatte #42/#43 so stark als Vorab-Gates interpretiert, dass produktive Entwicklung bis zu einer erneuten vollständigen Readiness-Prüfung blockiert wurde. Für den privaten, leanen Projektkontext ist das zu schwergewichtig.

Der richtige Modus ist:

```text
Owner-accepted MVP Acceptance Criteria (#42 + Domain-Inputs)
        ↓
Walking Skeleton / kleinster nutzbarer Vertical Slice (#59/#48)
        ↕
Live Research (#46/#47) + Domain Method SOTA (#60)
        ↕
Requirements-/Acceptance-Schärfung (#42)
        ↕
Just-in-time Technical SOTA / Feasibility / Architecture (#48)
        ↓
inkrementelle nutzbare Slices
        ↓
kontinuierliche technische + wissenschaftliche Verification
```

Kein separates monatelanges Architecture-Vorprojekt.

## 3. Was weiterhin hart gilt

Mindestens:

- Source / Representation / inspected Instance / Derivative / Findspot / Finding / Interpretation nicht still verschmelzen;
- AI output ist keine Evidenz und keine unabhängige Fachvalidierung;
- Unsicherheit / unresolved / contradiction sind zulässige Zustände;
- Findspots und Provenienz müssen erhalten bleiben;
- formal prüfbare Invarianten sollen deterministisch erzwungen werden;
- kuratierter Research State soll chat-/providerunabhängig, exportierbar und restartbar sein;
- exakte/auditierbare Retrieval-Baseline darf nicht von LLM abhängen;
- Rights/Privacy/External Processing bleiben explizit;
- Research und Mediation bleiben getrennt;
- Domain Method Truth bleibt Eigentum der Fachdomäne (#60), nicht des Dev-Stacks.

Diese Regeln begrenzen die Implementierung, blockieren aber nicht den Start eines kleinen nutzbaren Systems.

## 4. MVP-Akzeptanzlogik

Kanonischer Acceptance Overlay:

`docs/research/synthesis/mvp-acceptance.md`

Grundsatz:

> **Die Domain-Anforderungen sind Akzeptanzkriterien des Systems.**

Das bedeutet nicht, dass vor dem ersten Start sämtliche Fachprofile fertig erforscht sein müssen. Das System muss jedoch den geforderten wissenschaftlichen Arbeitsmodus **tragen, sichtbar machen und schrittweise vollständig erfüllen können**.

Wichtige Unterscheidung:

```text
usable increment
= real nutzbarer Teil des Systems mit bestandenen Slice-Akzeptanztests

MVP complete
= alle owner-accepted MVP-Akzeptanzkriterien sind für den vereinbarten privaten Scope erfüllt
```

So kann Nutzung sofort beginnen, ohne die Qualitätsdefinition des MVP zu verwässern.

## 5. Führender Dev-/Engineering-Owner #48

#48 ist ab jetzt **Technical Lead / Lean MVP Delivery & Architecture Owner**.

### Darf / soll

- den technischen Backlog nach Nutzerwert, Risiko, Dependency und kleinster nutzbarer Lieferung priorisieren;
- SOTA/Best Practice **just in time** für konkrete technische Entscheidungen prüfen;
- vorhandene Tools/Standards vor Eigenbau evaluieren;
- reversible Technologieentscheidungen selbstständig treffen und bei Bedarf refactoren;
- Walking Skeleton und kleine Vertical Slices implementieren;
- Integrationen/Spikes direkt in nutzbare Produktinkremente überführen, wenn Acceptance Tests bestehen;
- technische Debt sichtbar halten statt vorab alles zu lösen;
- Architektur evolutionär aus realer Nutzung entwickeln;
- bei jeder Iteration technische und wissenschaftliche Akzeptanztests automatisieren, soweit formal möglich.

### Darf nicht

- Fachsemantik oder Method Truth aus technischer Convenience definieren;
- owner-accepted Akzeptanzkriterien still abschwächen;
- wissenschaftliche Unsicherheit durch Datenmodell/UI eliminieren;
- irreversible/teure/lock-in-relevante Entscheidungen ohne explizite Begründung/ADR treffen;
- KI als kanonischen Truth Store oder Evidenzinstanz verwenden;
- Infrastruktur ohne konkreten aktuellen Nutzen auf Vorrat bauen.

Leitregel:

> **Dev entscheidet reversible Technik früh, wissenschaftliche Bedeutung nie eigenmächtig.**

## 6. Agile technische Entscheidungsregel

Vor einer technischen Entscheidung nur so viel Research wie nötig:

```text
konkretes Acceptance Criterion / Pain
→ bestehende Lösung / Standard prüfen
→ kleinste plausible Option
→ falls Risiko/Ungewissheit materiell: kurzer Spike/Benchmark
→ implementieren
→ im realen Case testen
→ behalten | anpassen | ersetzen
```

### ADR nur wenn nötig

Expliziter ADR/Owner-Entscheid insbesondere bei:

- schwer reversibler Persistenz-/Datenmodellentscheidung;
- relevantem Provider-/Cloud-/Kosten-/Privacy-Lock-in;
- bedeutender Migration;
- Security-/Rights-Konsequenz;
- konkurrierenden Optionen mit materiell verschiedenen wissenschaftlichen Folgen.

Reversible Library-/Framework-/UI-Entscheidungen brauchen keinen großen Vorab-Gate-Prozess.

## 7. Domain Research und Development laufen parallel

#60 muss weiter fachliche Methoden härten. Das blockiert nicht pauschal den MVP-Bau.

Beispiel:

```text
heute verfügbares Diplomatik-Profil = method-candidate
→ System kann es als Candidate referenzieren/anwenden
→ Ergebnisse bleiben entsprechend candidate/exploratory
→ Profile wird durch #60 verbessert
→ System übernimmt neue Version
→ betroffene Findings können review-needed werden
```

So wird wissenschaftliche Unsicherheit **modelliert**, statt Development anzuhalten oder falsche Sicherheit zu erzeugen.

## 8. Erste Delivery-Priorität

Der erste Walking Skeleton soll den unmittelbaren privaten Forschungsworkflow nutzbar machen:

```text
Zotero / Source Metadata
→ OneDrive Source Bytes oder kontrollierte Testdatei
→ Source / Instance / Findspot
→ Text/OCR soweit verfügbar
→ exakte/variantenfähige Suche
→ Observation / Excerpt
→ Finding / Hypothesis / Research Hook mit Status
→ Method-/Evidence-Bezug soweit verfügbar
→ Audit / Handoff / persistenter Research State
```

Nicht alles muss im ersten Commit vollständig sein. Aber jeder Slice muss real benutzbar und rückführbar auf MVP-Akzeptanzkriterien sein.

## 9. Architekturstatus

Histo-Orla bleibt technisch Greenfield, aber **Greenfield ist kein Grund für Delivery-Stopp**.

Aktuell nicht vorab festgelegt:

- endgültiger Runtime-/UI-/Backend-Stack;
- endgültige Persistenz-/Search-/OCR-/Workflow-Technologie;
- KG/RAG/Multi-Agent/Workflow-Plattform.

Diese Entscheidungen entstehen aus konkreten Slices und werden nur dort gehärtet, wo Reversibilität/Qualität es verlangt.

## 10. Leitformeln

> **Privat, lean, agil: früh nutzbar werden, im realen Forschen härten.**

> **Alle Domain-Systemanforderungen sind MVP-Akzeptanzkriterien.**

> **Architecture is a means, not a phase gate.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert und implementiert Requirements; Dev besitzt Method Truth nicht.**
