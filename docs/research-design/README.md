# Research Design – Status und Präzedenz

**Stand:** 2026-08-31  
**Governance:** #1/#9/#10/#23  
**Projekt-Handoff:** `/AGENTS.md` + `/PROJECT_STATE.md`

## Status

`transdisziplinaerer-literaturassistent.md` bleibt das **foundational design document** für Zielbild, Governing Principles, fachlichen Scope und die Grundidee einer transdisziplinären historischen Forschungsassistenz.

Es ist jedoch **nicht mehr der alleinige aktuelle operative Projektstand**.

Die Datei wurde zuletzt grundlegend am 30.08.2026 konsolidiert. Seitdem wurden Discovery, SOTA, Risk/Constraints, Capability Map, Requirements und Architecture Readiness in #28–#43 substantiell weiterentwickelt und abgeschlossen. Seit #48 läuft die Architektur-/Designphase.

Daher gilt:

```text
Foundational Design / Zielbild
  docs/research-design/transdisziplinaerer-literaturassistent.md
        ↓
aktuelle Research-/SOTA-Befunde
  docs/research/...
        ↓
Requirements
  docs/research/synthesis/requirements-baseline.md  (#42)
        ↓
Architecture Readiness
  docs/research/synthesis/architecture-readiness.md (#43)
        ↓
aktuelle Architecture Contracts / Spikes / ADRs
  docs/architecture/... + #48ff
```

## Was aus dem Design-Dokument weiterhin bindend/tragend ist

Insbesondere:

- Fachdomänen führen; Technologie dient.
- Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.
- Rückübersetzung vereinfacht Sprache, nicht Wissenschaft.
- Chat ist Werkstatt; GitHub ist Projektgedächtnis.
- kein Wissensmonopol in Chat/Modellzustand.
- Human-in-the-loop, Auditierbarkeit und Challengeability.
- Quelle/Instanz/Derivat/Befund/Interpretation nicht still vermischen.
- regionale Tiefenschärfe + kontrollierter Multi-Scale-Horizont.
- Dev informiert Requirements; Dev besitzt sie nicht.
- Lean/technische Subsidiarität.
- Forschung und Vermittlung bleiben getrennt.

## Was dort als historischer/überholter Arbeitsstand zu lesen ist

Abschnitte, die noch davon sprechen, dass Discovery/SOTA/Requirements **erst als Nächstes** zu erledigen seien, sind durch #28–#43 überholt.

Ebenso ist die alte Issue-Landkarte nicht vollständig: aktuelle aktive Architektur-Work-Owner sind mindestens #48, #49 und #50 sowie die laufenden Live-Research-Fälle #46/#47.

Technologiehypothesen im Dokument bleiben Hypothesen, sofern sie nicht später durch Requirements/Architecture/ADR promoted wurden.

## Bootstrap-Regel

Kein neuer Bearbeiter soll dieses Verzeichnis allein als Projekt-Handoff verwenden.

Pflicht-Einstieg:

1. `/AGENTS.md`
2. `/PROJECT_STATE.md`
3. `/README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

## Pflege

Das monolithische Design-Dokument wird nicht bei jedem operativen Fortschritt komplett umgeschrieben. Materielle Änderungen am Zielbild/Governing Principles werden dort oder in einem expliziten Nachfolger konsolidiert; laufender State bleibt in `PROJECT_STATE.md`, Issues und fach-/architekturspezifischen Artefakten.

Damit vermeiden wir sowohl ein veraltetes Monolith-Dokument als auch parallele Wahrheitsspeicher.