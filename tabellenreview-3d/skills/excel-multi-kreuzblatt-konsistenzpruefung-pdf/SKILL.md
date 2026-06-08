---
name: excel-multi-kreuzblatt-konsistenzpruefung-pdf
description: "3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei Multisheet-Struktur. Abgrenzung: nicht PDF-Bericht im Tabellenreview 3d."
---

# /tabellenreview-3d:excel-multi-sheet-export

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

