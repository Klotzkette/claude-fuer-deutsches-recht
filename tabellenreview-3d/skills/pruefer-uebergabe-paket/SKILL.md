---
name: pruefer-uebergabe-paket
description: "Schnuert das vollstaendige Pruefer-Paket nach Abschluss eines Wuerfellaufs — Excel-Wuerfel-Datei aus Skill `excel-multi-sheet-export` PDF-Bericht aus `pdf-bericht-erzeugen` Belegketten-CSV aus `belegkette-rueckverfolgung` Audit-Trail-Auszug aus `audit-trail-protokoll` Prompt-Versionen aus `prompt-versionierung` Widerspruchsbericht aus `kreuzblatt-konsistenzpruefung` Ampel-Aggregat aus `risikoampel-aggregation` Pruefer-Flag-Arbeitsliste. Erzeugt ein ZIP-Paket plus Begleitschreiben. Pflichtschritt vor Mandatsabnahme. Ohne Pruefer-Unterschrift kein Versand an Mandant."
---

# /tabellenreview-3d:prüfer-übergabe-paket

## Zweck

Das Plugin liefert nicht das fertige Mandatsergebnis. Es liefert das Prüfer-Paket — alles was der zugelassene Rechtsanwalt braucht um in vertretbarer Zeit die Endabnahme machen zu können. Dieser Skill schnuert das Paket.

## Bestandteile

### 1. Hauptdatei

- `<projekt>-wuerfel.xlsx` aus `excel-multi-sheet-export` mit allen Tabellenreitern.

### 2. Erzählfassung

- `<projekt>-bericht.pdf` aus `pdf-bericht-erzeugen` mit Deckblatt Management-Summary und Anhang.

### 3. Belegkette

- `belegkette.csv` aus `belegkette-rueckverfolgung` — Pflichtanhang für Reproduzierbarkeit.

### 4. Audit

- `audit-trail-auszug.md` aus `audit-trail-protokoll` — die letzten N Ereignisse, mindestens aber Lauf-Start Lauf-Ende Prompt-Versionen und Prüfer-Flags.

### 5. Prompt-Versionen

- `prompt-historie.yaml` aus `prompt-versionierung` — welche Versionen aktiv waren beim Lauf.

### 6. Widersprüche

- `widerspruchsbericht.md` aus `kreuzblatt-konsistenzpruefung` — Konflikte zwischen Arbeitsblättern.

### 7. Ampel-Aggregat

- `ampel-aggregat.md` aus `risikoampel-aggregation` — Gesamtbild auf Würfel- Arbeitsblatt- Spalten- und Zeilenebene.

### 8. Prüfer-Flag-Arbeitsliste

- `pruefer-flags.xlsx` — Liste aller Zellen die menschliche Prüfung brauchen. Spalten: Zeile Arbeitsblatt Spalte Grund Antwortvorschlag Entscheidung (leer).

### 9. Begleitschreiben

- `begleitschreiben.md` — eine Seite. Was wurde gemacht. Wie viele Dokumente. Wie viele Hotspots. Wie viele Prüfer-Flags. Erwartete Pruefdauer. Ablauf der Abnahme.

## Zusammenstellung

Alles in einem ZIP: `<projekt>-prüfer-paket-<zeitstempel>.zip`

## Abnahme

Der Prüfer:

1. Liest das Begleitschreiben.
2. Geht die Prüfer-Flag-Arbeitsliste durch — Entscheidung pro Flag.
3. Stichprobenprüfung an gelben und grünen Zellen.
4. Prüfung der roten Zellen und Hotspots vollständig.
5. Unterschrift im Audit-Trail (`prüferabnahme.eingegeben`).

## Erst nach Abnahme

Erst nach dokumentierter Prüfer-Abnahme darf das Paket (oder Auszüge davon) an den Mandanten gehen. Das Plugin sperrt die Mandantenausgabe per Schwellenwert: ohne `prüferabnahme.eingegeben` im Audit-Trail wird der Skill `mandant-versenden` (sofern in der Praxis vorgesehen) verweigert.

## Begründung

- BRAO Paragraph 43a Absatz 2 — Verschwiegenheit
- StGB Paragraph 203 — Privatgeheimnisse
- RDG Paragraph 2 — Rechtsdienstleistung darf nur durch Rechtsanwalt erbracht werden — der Würfel ist Vorbereitung, die Abnahme ist die Rechtsdienstleistung
