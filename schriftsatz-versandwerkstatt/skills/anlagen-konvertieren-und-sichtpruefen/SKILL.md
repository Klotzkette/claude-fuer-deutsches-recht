---
name: anlagen-konvertieren-und-sichtpruefen
description: "Konvertiert bereits ausgewählte Anlagen aus Office-, Tabellen-, Bild-, E-Mail-, Text- und Webformaten in getrennte PDFs, ohne Beweisinhalt zu verändern: protokolliert Quelle und Hash, erhält Absender- und Zeitangaben, meldet Anhänge und nicht unterstützte Container, vergleicht jede Ausgabeseite visuell und stoppt bei Beschnitt, fehlenden Blättern oder."
---

# Anlagen konvertieren und sichtprüfen

## 1. Grundsatz

Eine erfolgreich erzeugte PDF ist noch keine freigegebene Anlage. Jede Konvertierung bleibt bis zum Seitenvergleich im Status `prüfen`.

## 2. Formatroute

| Quelle | Route | besondere Kontrolle |
| --- | --- | --- |
| DOC, DOCX, ODT, RTF | LibreOffice nach PDF | Kommentare, Änderungen, Kopf-/Fußzeilen, Seitenumbruch |
| XLS, XLSX, ODS | LibreOffice nach PDF | alle Tabellenblätter, Druckbereiche, Spalten, Formelergebnisse, wiederholte Kopfzeilen |
| PPT, PPTX, ODP | LibreOffice nach PDF | Folgenreihenfolge, Notizen nur bei ausdrücklichem Auftrag |
| JPG, JPEG, PNG | A4-PDF ohne Beschnitt | Orientierung, Auflösung, Farbinhalt, mehrere Bilder als getrennte Quellen |
| EML | Kopfzeilen plus Nachrichtentext | Absender, Empfänger, Datum, Betreff, Text und Hinweis auf Anhänge |
| TXT, CSV, TSV, Markdown, HTML | paginierte Textfassung | Zeichensatz, Spaltentrenner, Zeilenumbrüche, Vollständigkeit |
| PDF | technische Prüfung | Verschlüsselung, aktive Inhalte, Leerseiten, Lesbarkeit |

## 3. E-Mail

Für jede EML-Datei müssen Von, An, Cc, Datum, Betreff und Nachrichtentext sichtbar sein. Liste eingebettete Anhänge im PDF-Kopf. Anhänge werden nicht unsichtbar Teil der E-Mail-PDF; erforderliche Anhänge sind als eigene Anlagenquelle bereitzustellen.

MSG, PST, MBOX und vergleichbare Container werden nicht improvisiert ausgelesen. Verlange einen Export als EML oder überprüfbares PDF und die benötigten Anhänge separat.

## 4. Tabellen

Stoppe, wenn Spalten abgeschnitten, Formeln als Fehlerwerte dargestellt, Tabellenblätter ausgelassen oder Zahlen durch wissenschaftliche Schreibweise verändert erscheinen. Eine Tabelle darf auf Querformat oder mehrere Seiten verteilt werden, muss aber ihre Kopfzeilen und Zuordnung behalten.

## 5. Protokoll

| Anlage | Quelle | Quellhash | Konverter | Zielseiten | Sichtkontrolle | Abweichung |
| --- | --- | --- | --- | --- | --- | --- |

Keine Quelle überschreiben. Bewahre nur die Versand-PDF im Versandordner auf; Quell- und Prüfdateien bleiben intern. Übergib freigegebene PDFs an `anlagen-nummerieren-und-stempeln`.
