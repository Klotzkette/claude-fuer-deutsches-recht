---
name: pruefer-uebergabe-paket
description: "Übergabepaket für Prüferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Prüfraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Übergabedokument für naechsten Prüfer. Abgrenzung: nicht Audit-Trail."
---

# /tabellenreview-3d:prüfer-übergabe-paket

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

- `begleitschreiben.md` — eine Seite. Was wurde gemacht. Wie viele Dokumente. Wie viele Hotspots. Wie viele Prüfer-Flags. Erwartete Prüfdauer. Ablauf der Abnahme.

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
