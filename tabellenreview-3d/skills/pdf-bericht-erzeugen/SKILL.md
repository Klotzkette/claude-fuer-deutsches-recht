---
name: pdf-bericht-erzeugen
description: "3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Pruefraster: Vollstaendigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview. Abgrenzung: nicht Excel-Export."
---

# /tabellenreview-3d:pdf-bericht-erzeugen


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
