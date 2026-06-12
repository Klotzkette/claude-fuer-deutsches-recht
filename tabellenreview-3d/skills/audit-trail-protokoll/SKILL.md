---
name: audit-trail-protokoll
description: "Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Änderungshistorie, Versionierung. Output: Audit-Trail-Protokoll. Abgrenzung: nicht inhaltliche Prüfung (Zweck: Nachvollziehb..."
---

# /tabellenreview-3d:audit-trail-protokoll

## Triage zu Beginn

1. Für welches Mandat / Projekt wird der Audit-Trail gefuehrt? (M&A-DD / Immobilien / Vendor)
2. Wer ist der verantwortliche Prüfer, der jede Abnahme unterschreiben muss?
3. Muss der Audit-Trail gerichtsfest sein? → Append-only-Format (JSONL) waehlen
4. Gibt es berufsrechtliche Aufbewahrungspflichten? (§ 50 BRAO: 5 Jahre Mandatsakte)

## Rechtliche Grundlagen zur Dokumentationspflicht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ereignistypen

### Würfel-Lebenszyklus

- `würfel.erstellt` — Würfel-Schema neu angelegt
- `würfel.dimension-erweitert` — Spalte / Zeile / Arbeitsblatt hinzugefügt
- `würfel.dimension-gekuerzt` — Spalte / Zeile / Arbeitsblatt entfernt
- `würfel.archiviert` — Würfel abgeschlossen

### Prompts

- `prompt.erstellt` — neuer Spalten- oder Zeilenprompt definiert
- `prompt.geändert` — Prompt-Wortlaut geändert (Versions-ID erhöht)
- `prompt.deaktiviert` — Prompt aus aktivem Schema genommen

### Reviewlauf

- `lauf.gestartet` — Reviewlauf begonnen, mit Würfel-Snapshot-Hash
- `lauf.beendet` — Reviewlauf beendet, mit Ergebnis-Hash
- `lauf.fehler` — Reviewlauf abgebrochen, mit Fehlermeldung

### Caching

- `cache.treffer` — Zelle aus Cache übernommen, Quell-Zell-ID
- `cache.invalidiert` — Cache-Eintrag verworfen weil Prompt-Version geändert

### Prüfer-Workflow

- `prüferflag.gesetzt` — Zelle braucht menschliche Prüfung, Grund
- `prüferabnahme.eingegeben` — Prüfer hat abgehakt, Prüfer-ID und Entscheidung
- `prüfer.kommentar` — Prüfer-Kommentar zu Zelle

### Belegkette

- `datei.gehasht` — Hash einer Quelldatei berechnet
- `hash-bruch` — Quelldatei-Hash weicht vom registrierten Hash ab (Manipulationsverdacht)

## Pflichtfelder pro Eintrag

```json
{
 "zeitstempel": "2026-05-20T14:23:11Z",
 "aktion": "lauf.beendet",
 "verantwortlicher": "system",
 "würfel-version": "v3",
 "prompt-version": "p12",
 "modell-version": "claude-opus-4-7",
 "eingangs-hash": "sha256:...",
 "ausgangs-hash": "sha256:...",
 "anzahl-zellen": 4176,
 "anzahl-prüferflag": 87,
 "begründung": "Standardlauf nach Schema-Änderung Spalte 'MAC'"
}
```

## Ablage

- `audit-trail.jsonl` — append-only, eine JSON-Zeile pro Ereignis. Nie ändern, nur anhängen.
- `audit-trail.md` — periodisch zu menschenlesbarem Markdown verdichtet (z. B. wochenweise).

## Integritaet

- Jeder Eintrag enthält den Hash des vorherigen Eintrags (Chain-of-Trust). Wer einen Eintrag ändert bricht die Kette.
- Optional: kryptografische Signatur des Prüfers bei Abnahme-Ereignissen.

## Verwendung

- Pflicht vor jeder Mandatsübergabe — der Prüfer signiert den letzten Audit-Stand.
- Bei Beschwerden Aufsicht oder Haftungsfrage rückverfolgbar nachweisen welcher Reviewlauf welchen Output produziert hat.
- Verhindert dass Prompts schleichend geändert werden und alte Zellen `nicht mehr nachvollziehbar` sind.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 2 JVEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- § 29 VwVfG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
