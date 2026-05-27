---
name: pruefer-uebergabe-paket
description: "Uebergabepaket fuer Prueferwechsel im 3D-Review zusammenstellen: aktueller Stand, offene Positionen. Normen: §§ 174 ff. InsO. Pruefraster: Fortschrittsstand, kritische Punkte, Dokumentation. Output: Uebergabedokument fuer naechsten Pruefer. Abgrenzung: nicht Audit-Trail."
---

# /tabellenreview-3d:prüfer-übergabe-paket


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


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
