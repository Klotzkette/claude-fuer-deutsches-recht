---
name: excel-multi-sheet-export
description: "Exportiert den dreidimensionalen Wuerfel in eine einzige Excel-Datei mit mehreren Tabellenblaettern — ein Reiter pro Arbeitsblatt-Perspektive (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb / Compliance). Jede Tabelle: Zeilen = Dokumente Spalten = Datenpunkte Zellinhalt = Antwort plus woertliches Zitat plus Fundstelle plus Ampel-Farbcode. Zusatzreiter: 'Uebersicht' (Aggregat) 'Hotspots' (Spalten-Top-N) 'Widersprueche' (aus Kreuzblatt) 'Pruefer-Flags' 'Belegkette' (Hash-Tabelle) 'Prompt-Versionen' (Audit). Geeignet als finales Pruefer-Paket zur menschlichen Endabnahme."
---

# /tabellenreview-3d:excel-multi-sheet-export

## Zweck

Excel ist das Lingua Franca der Mandatsübergabe. Der 3D-Würfel wird in Excel nativ abgebildet: jedes Arbeitsblatt ist ein Tabellenreiter — genau das was die dritte Dimension visuell darstellt.

## Aufbau der Excel-Datei

### Reiter 1 bis N — Pro Arbeitsblatt-Perspektive

Jede Tabelle hat dieselbe Struktur:
- Zeilen: Dokumente aus `zeilen-inventar.yaml`
- Spalten: aus `spaltenprompts.yaml` plus Arbeitsblatt-spezifische Zusatzspalten
- Zellinhalt: Antwort + wörtliches Zitat + Fundstelle (Datei-ID + Seite + Absatz)
- Zell-Hintergrundfarbe: rot / gelb / grün aus Ampel
- Zell-Kommentar: Prüfer-Flag (falls gesetzt) und Prompt-Version

### Reiter 'Übersicht'

- Würfel-Gesamtampel oben
- Arbeitsblatt-Ampel pro Reiter
- Spalten-Hotspots (Top-N)
- Prüfer-Flag-Anzahl

### Reiter 'Hotspots'

Pro Spalte: Anzahl rot / gelb / grün über den Stapel. Sortiert absteigend nach Rot-Anteil.

### Reiter 'Widersprüche'

Aus `kreuzblatt-konsistenzpruefung`. Spalten: Zeile-ID, Spalte, Arbeitsblatt-A-Antwort, Arbeitsblatt-B-Antwort, Konflikt-Klassifikation, empfohlene Aktion.

### Reiter 'Prüfer-Flags'

Liste aller Zellen mit Prüfer-Flag. Spalten: Zeile, Arbeitsblatt, Spalte, Grund (OCR-Konfidenz / Mehrdeutigkeit / Hash-Bruch / Konflikt), Antwortvorschlag, Prüfer-Entscheidung (leer).

### Reiter 'Belegkette'

Tabelle aller Dokumente mit: Datei-ID, Pfad, SHA-256-Hash, Seitenzahl, OCR-Konfidenz. Damit ist jede Fundstelle im Würfel rückverfolgbar auf den exakten Dateistand.

### Reiter 'Prompt-Versionen'

Spalten-Prompts und Zeilen-Prompts mit jeweiliger Version-ID und Änderungsdatum (aus `prompt-versionierung`). Damit ist jede Zelle reproduzierbar.

### Reiter 'Audit-Trail'

Reviewlauf-Zeitstempel, verwendete Modell-Version, Laufdauer, Anzahl Zellen, Anzahl Cache-Treffer, Prüfer-Abnahme-Status. Aus `audit-trail-protokoll`.

## Technische Hinweise

- Format: `.xlsx`
- Bedingte Formatierung für Ampel-Farben
- Zell-Kommentare für Prüfer-Flags
- Hyperlinks von 'Fundstelle' zur Datei (relativ zum Projektordner)
- Spalte einfrieren (`Zeile-ID`) und Kopfzeile einfrieren

## Ausgabe

- `<projekt>-wuerfel.xlsx` mit allen Reitern
- `<projekt>-würfel-anhang.zip` (optional) mit allen referenzierten Quelldokumenten zur autarken Mandantenübergabe (Achtung: Geheimhaltungs- und DSGVO-Pflichten beachten)

## Grenzen

Excel kann große Stapel handeln; ab 100.000 Zellen sind PDF und CSV pro Reiter zu erwägen (siehe Skill `pdf-bericht-erzeugen`).
