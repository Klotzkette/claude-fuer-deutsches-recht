---
name: anlagen-konvertieren-und-sichtpruefen
description: "Konvertiert zugeordnete Anlagen aus Office-, Tabellen-, Bild-, E-Mail- und Textformaten in getrennte PDFs. Erhält Quellbezug und sämtliche Scanseiten, kontrolliert E-Mail-Anhänge und stoppt bei Beschnitt, Zeichenverlust oder fehlenden Blättern. Signierte Originale bleiben unangetastet."
---

# Anlagen konvertieren und sichtprüfen

## 1. Grundsatz

Eine erfolgreich erzeugte PDF ist noch keine freigegebene Anlage. Jede Konvertierung bleibt bis zum Seitenvergleich im Status `prüfen`.

Signierte Originale samt gegebenenfalls abgesetzter Signaturdatei nicht konvertieren, optimieren oder per OCR verändern. Die technische Zuordnung und den Einreichungsweg gesondert klären. Bei nicht darstellbaren Zeichen einen Export mit geeigneten Schriften anfordern; keine Namen oder Nachrichtentexte durch Fragezeichen ersetzen.

## 2. Formatroute

| Quelle | Route | besondere Kontrolle |
| --- | --- | --- |
| DOC, DOCX, ODT, RTF | LibreOffice nach PDF | Kommentare, Änderungen, Kopf-/Fußzeilen, Seitenumbruch |
| XLS, XLSX, ODS | LibreOffice nach PDF | alle Tabellenblätter, Druckbereiche, Spalten, Formelergebnisse, wiederholte Kopfzeilen |
| PPT, PPTX, ODP | LibreOffice nach PDF | Folgenreihenfolge, Notizen nur bei ausdrücklichem Auftrag |
| JPG, JPEG, PNG, BMP, TIFF | A4-PDF ohne Beschnitt | Orientierung, Auflösung, Transparenz und alle Seiten mehrseitiger Scans |
| EML | Kopfzeilen plus Nachrichtentext | Absender, Empfänger, Datum, Betreff, Text und Hinweis auf Anhänge |
| TXT, CSV, TSV, Markdown, HTML | paginierte Textfassung | Zeichensatz, Spaltentrenner, Zeilenumbrüche, Vollständigkeit |
| PDF | technische Prüfung | Verschlüsselung, aktive Inhalte, Leerseiten, Lesbarkeit |

## 3. E-Mail

Für jede EML-Datei müssen Von, An, Cc, Datum, Betreff und Nachrichtentext sichtbar sein. Liste eingebettete Anhänge im PDF-Kopf. Anhänge werden nicht unsichtbar Teil der E-Mail-PDF; erforderliche Anhänge sind als eigene Anlagenquelle bereitzustellen.

Jeden eingebetteten Anhang unverändert exportieren und im Anlagenplan aufnehmen oder mit einem konkreten Grund ausschließen. Ein gleicher Dateiname reicht nicht als Identitätsnachweis. Inline-Bilder und HTML-Layout mit der Nachricht vergleichen, weil ein Textauszug deren Darstellung nicht zuverlässig erhält.

MSG, PST, MBOX und vergleichbare Container werden nicht improvisiert ausgelesen. Verlange einen Export als EML oder überprüfbares PDF und die benötigten Anhänge separat.

## 4. Tabellen

Stoppe, wenn Spalten abgeschnitten, Formeln als Fehlerwerte dargestellt, Tabellenblätter ausgelassen oder Zahlen durch wissenschaftliche Schreibweise verändert erscheinen. Eine Tabelle darf auf Querformat oder mehrere Seiten verteilt werden, muss aber ihre Kopfzeilen und Zuordnung behalten.

## 5. Protokoll

| Anlage | Quelle | Quellhash | Konverter | Zielseiten | Sichtkontrolle | Abweichung |
| --- | --- | --- | --- | --- | --- | --- |

Keine Quelle überschreiben. Bewahre nur die Versand-PDF im Versandordner auf; Quell- und Prüfdateien bleiben intern. Übergib freigegebene PDFs an `anlagen-nummerieren-und-stempeln`.
