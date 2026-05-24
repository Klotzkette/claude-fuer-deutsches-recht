---
name: pdf-bericht-erzeugen
description: "Erstellt einen pruefbaren PDF-Bericht aus dem 3D-Wuerfel. Struktur: Deckblatt mit Projekt Mandant Stichtag Wuerfel-Ampel; Management-Summary mit Hotspots und blockierenden Roten; pro Arbeitsblatt-Perspektive ein Abschnitt mit Aggregat und Top-Findings; Anhang mit vollstaendigen Tabellen pro Arbeitsblatt; Beleganhang mit zitierten Quellen und Datei-Hashes; Audit-Anhang mit Prompt-Versionen Modell-Version und Reviewlauf-Metadaten. Bedingte Formatierung fuer Ampelfarben. Gerichtsfaehig in dem Sinne dass jede Aussage rueckverfolgbar ist."
---

# /tabellenreview-3d:pdf-bericht-erzeugen

## Zweck

Mandanten lesen lieber PDF als Excel. Der PDF-Bericht ist die Erzählfassung des Würfels: vom Aggregat über die Perspektiven bis in die Belegkette.

## Struktur

### 1. Deckblatt

- Projektname und kurzer Anlassbezug (z. B. 'M&A-DD Erwerb der X-GmbH zum Stichtag YYYY-MM-DD')
- Mandant und anwaltlicher Prüfer
- Anzahl Dokumente Anzahl Datenpunkte Anzahl Arbeitsblatt-Perspektiven
- Würfel-Gesamtampel
- Prüfer-Abnahme-Status

### 2. Management-Summary (Ein Blatt)

- Würfel-Ampel mit Begründung in drei Sätzen
- Top-5-Hotspots (Datenpunkte mit überproportional vielen roten Zellen)
- Top-5-rote-Zeilen (Dokumente die das größte Risiko tragen)
- Top-3-Widersprüche aus `kreuzblatt-konsistenzpruefung`
- Anzahl Prüfer-Flags und Status der Abnahme

### 3. Pro Arbeitsblatt-Perspektive (ein Abschnitt)

- Perspektive (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb / Compliance)
- Arbeitsblatt-Ampel mit Begründung
- Top-Findings dieser Perspektive (max 10)
- Hinweis auf zuständigen Prüfer (Rechtsanwalt / Steuerberater / DSB usw.)

### 4. Vollständige Tabellen (Anhang A)

Pro Arbeitsblatt eine Tabelle mit allen Zeilen und Spalten. Ampelfarben als Hintergrund. Zell-Inhalt: Antwort plus Fundstelle plus Prüfer-Flag.

### 5. Belegkette (Anhang B)

Alle zitierten Quellen mit:
- Datei-ID
- Pfad
- SHA-256-Hash
- Seitenzahl bei Fundstelle
- OCR-Konfidenz pro Seite (bei gescannten Dokumenten)

### 6. Audit-Anhang (Anhang C)

- Prompt-Versionen (Spalten und Zeilen)
- Verwendete Modell-Version und Konfiguration
- Reviewlauf-Zeitstempel und Laufdauer
- Cache-Trefferquote
- Prüfer-Abnahme-Historie

## Bedingte Formatierung

- Rote Hintergrundfarbe bei roter Ampel
- Gelbe Hintergrundfarbe bei gelber Ampel
- Schwacher Grüner-Ton bei grüner Ampel (sonst zu unruhig)
- Schraffur bei Prüfer-Flag

## Sicherheit

- PDF mit eingebetteten Schriften (kein nachträgliches Ersetzen)
- Optional: Schreibschutz und Signaturfeld für den Prüfer
- Optional: Wasserzeichen 'VERTRAULICH ARBEITSERGEBNIS' bei unsignierter Fassung

## Ausgabe

- `<projekt>-bericht.pdf`
- `<projekt>-bericht-quellen.zip` (optional) — alle in der Belegkette referenzierten Quelldokumente

## Grenzen

Bei sehr großen Würfeln (mehr als 50.000 Zellen) wird der PDF unhandlich. In diesem Fall: PDF nur für Management-Summary und Anhang A pro Arbeitsblatt als separate PDFs. Vollständige Daten weiter in Excel.
