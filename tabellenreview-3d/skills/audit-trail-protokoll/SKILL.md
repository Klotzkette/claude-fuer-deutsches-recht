---
name: audit-trail-protokoll
description: "Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprueft und geaendert. Normen: §§ 238 257 HGB Buchfuehrungspflichten. Pruefraster: Zeitstempel, Pruefer-ID, Aenderungshistorie, Versionierung. Output: Audit-Trail-Protokoll. Abgrenzung: nicht inhaltliche Pruefung (Zweck: Nachvollziehbarkeit)."
---

# /tabellenreview-3d:audit-trail-protokoll

## Triage zu Beginn

1. Fuer welches Mandat / Projekt wird der Audit-Trail gefuehrt? (M&A-DD / Immobilien / Vendor)
2. Wer ist der verantwortliche Pruefer, der jede Abnahme unterschreiben muss?
3. Muss der Audit-Trail gerichtsfest sein? → Append-only-Format (JSONL) waehlen
4. Gibt es berufsrechtliche Aufbewahrungspflichten? (§ 50 BRAO: 5 Jahre Mandatsakte)

## Rechtliche Grundlagen zur Dokumentationspflicht

- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Anwaelte sind nach § 50 BRAO verpflichtet, die Mandatsakte vollstaendig zu fuehren; fehlende Dokumentation des Beratungsvorgangs begruendet Haftungsrisiko wenn der Mandant behauptet, keine Beratung erhalten zu haben.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Die Aktenaufbewahrungspflicht des Anwalts (§ 50 Abs. 1 BRAO) betraegt grundsaetzlich 5 Jahre nach Mandatsende; bei Haftungsfragen koennen laengere Fristen geboten sein.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Dokumentation muss so beschaffen sein, dass der Buerger seine Rechtslage nachvollziehen kann; unvollstaendige oder unverstaendliche Protokolle verletzen das Gebot der Nachvollziehbarkeit.
- BGH, Urt. v. 23.05.2019 - IX ZR 143/18, NJW 2019, 2296 — Im Due-Diligence-Kontext haftet die Prueferkanzlei fuer fehlerhafte oder lueckenhafte Berichte; ein lueckenloses Audit-Trail sichert den Nachweis der ordnungsgemaessen Durchfuehrung.

## Zweck

Wer mit KI Verträge prüft muss später erklären können wie das Ergebnis zustande kam. Dieser Skill ist die Erklärung — Append-only-Log für den gesamten Lebenszyklus des Würfels.

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
