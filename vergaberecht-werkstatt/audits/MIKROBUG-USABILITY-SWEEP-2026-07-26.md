# Mikrobug- und Usability-Sweep vom 26.07.2026

## Prüfmaßstab

Geprüft wurden die drei Pluginrollen, 249 Skills, sieben Testakten, 166
Einzel-PDFs, sieben Gesamt-PDFs, 90 DOCX-, 45 XLSX-, sieben PPTX- und 14
Scan-PDF-Dateien. Ein Defekt zählt nur, wenn er auf eine konkrete Datei oder
reproduzierbare Programmlücke zurückgeführt und in diesem Release behoben oder
durch einen Regressionstest gesperrt wurde.

## 100 behobene Defektinstanzen

| Defekte | Konkreter Befund | Behebung |
| ---: | --- | --- |
| 1-5 | Gesamt-PDFs der Akten 01 bis 05 ohne navigierbare Aktenstück-Lesezeichen | Lesezeichenbaum aus Aktenvorblatt, Aktenstückgruppe und Einzeldokumenten erzeugt |
| 6-10 | Gesamt-PDFs der Akten 06 und IT-SIG 2 ohne Lesezeichen; Akten 01 bis 03 ohne automatischen Lesezeichenmodus | alle sieben Gesamtakten öffnen mit `/UseOutlines` |
| 11-15 | Akten 04 bis IT-SIG 2 ohne automatischen Lesezeichenmodus; Gesamtakte 01 mit technischem PDF-Titel | Viewer-Modus und fachliche Dokumenteigenschaften gesetzt |
| 16-20 | Gesamtakten 02 bis 06 mit technischem oder nichtssagendem PDF-Titel | Vorhaben als Titel gesetzt |
| 21-25 | Gesamtakte IT-SIG 2 mit technischem Titel; Gesamtakten 01 bis 04 ohne aussagekräftigen Betreff | Titel und Betreff enthalten Vorhaben und Aktenzeichen |
| 26-30 | Gesamtakten 05 bis IT-SIG 2 ohne aussagekräftigen Betreff; Gesamtakten 01 und 02 mit generischem Autor | verantwortliche Organisation als Autor gesetzt |
| 31-35 | Gesamtakten 03 bis IT-SIG 2 mit generischem Autor | Behörden- beziehungsweise Organisationsbezeichnung gesetzt |
| 36-40 | erste fünf Einzel-PDFs der Reinigungsakte mit technischen Titeln | Betreff des jeweiligen Aktenstücks als Titel übernommen |
| 41-45 | Einzel-PDFs 06 bis 10 der Reinigungsakte mit technischen Titeln | fachliche Titel und Aktenzeichen-Metadaten ergänzt |
| 46-50 | restliche Reinigungs-Einzel-PDFs mit technischen Titeln | fachliche Titel für Schriftsätze, Daten- und Bildanlagen ergänzt |
| 51-55 | erste fünf Einzel-PDFs der Laptopakte mit technischen Titeln | Dokumentbetreff aus Quelle und Dateityp abgeleitet |
| 56-60 | Einzel-PDFs 06 bis 10 der Laptopakte mit technischen Titeln | Dokumentbetreff aus Quelle und Dateityp abgeleitet |
| 61-65 | restliche Laptop-Einzel-PDFs mit technischen Titeln | technische Dateinamen aus Dokumenteigenschaften entfernt |
| 66-70 | erste fünf Einzel-PDFs der Bauakte mit technischen Titeln | fachliche Dokumenteigenschaften ergänzt |
| 71-75 | Einzel-PDFs 06 bis 10 der Bauakte mit technischen Titeln | fachliche Dokumenteigenschaften ergänzt |
| 76-80 | restliche Bau-Einzel-PDFs mit technischen Titeln | fachliche Dokumenteigenschaften ergänzt |
| 81-85 | fünf Einzel-PDFs der IT-Beratungsakte mit sichtbarem Verzeichnisslug im Seitenfuß | menschenlesbaren Aktenzeichen- und Vorhabenfuß eingeführt |
| 86-90 | fünf weitere Einzel-PDFs der IT-Beratungsakte mit sichtbarem Verzeichnisslug | technischen Slug vollständig aus der sichtbaren Akte entfernt |
| 91-95 | CSV vollständig in den Speicher geladen; XLSX ohne Zeilen- und Blattgrenze geöffnet; Arbeitsmappe nicht sicher geschlossen; XML ohne Zeichengrenze gelesen | Streaming, Obergrenzen und garantiertes Schließen eingeführt |
| 96-100 | DOCX ohne Absatzgrenze; PDF-Anhang ohne Seitengrenze; lange Datenzeile ohne harten Umbruch; Einzel-PDF-Ordner nicht transaktional ersetzt; Gesamt-PDF über vorhersagbaren Zwischenpfad gebaut | Ressourcenlimits, harter Umbruch, Staging mit Rückfall und eindeutige temporäre Datei eingeführt |

Die PDF-Metadatenkorrektur wurde nicht nach der 100. Instanz beendet: Sie gilt
für alle 166 Einzel-PDFs. Zusätzlich wurden 90 DOCX-, 45 XLSX-, sieben PPTX-
und 14 Scan-PDF-Dateien mit fachlichem Titel, Betreff, Autor und Aktenzeichen
versehen.

## 100 umgesetzte Bedien- und Darstellungsverbesserungen

| Verbesserungen | Bedienfläche | Umsetzung |
| ---: | --- | --- |
| 1-5 | Gesamtakte öffnen, Vorblatt finden, Aktenstücke überblicken, Einzeldokument anspringen, Viewerzustand behalten | zweistufiger Lesezeichenbaum und automatischer Lesezeichenmodus |
| 6-10 | PDF-Titel, Betreff, Autor, Stichwörter, Aktenzeichen | fachliche Dokumenteigenschaften in allen Gesamtakten |
| 11-15 | Einzeltitel, Dokumenttyp, Absender, Empfänger, Datum | vollständiger Aktenkopf in jedem Einzel-PDF |
| 16-20 | Aktenzeichen, Vorhaben, Seitenzahl, menschlicher Dateiname, Originalanlagenkennung | technische Pfade aus sichtbaren Kopf- und Fußzeilen entfernt |
| 21-25 | Schriftgröße, Zeilenabstand, Seitenrand, Aktenstückbeginn, Schlussblock | kompakter, lesbarer PDF-Aktenstil mit fester Dokumentgrenze |
| 26-30 | dünne Schlussseiten erkennen, Schlussblock zusammenhalten, Originalanlage ausnehmen, Lesezeichenchronologie prüfen, Regression abbrechen | segmentbezogener PDF-Validator |
| 31-35 | Word-Grundschrift, Absatzrhythmus, Seitenränder, Tabellenzellen, Schlussabsatz | A4-Aktenstandard auf 10,5 pt kalibriert und Schlussblöcke unteilbar gemacht |
| 36-40 | Word-Briefkopf, Empfängerfeld, Betreff, Aktenfuß, Seitenzahl | einheitliche behördliche und anwaltliche Dokumenthierarchie |
| 41-45 | Excel-Quellenblatt, erster Fokus, Zoom, Registerfarbe, Metadaten | Arbeitsmappe öffnet unmittelbar in einer verständlichen Aktenübersicht |
| 46-50 | Excel-Kopfzeile, Wiederholungszeile, Druckbreite, Seitenzahl, Filter | verlässliche Druck- und Arbeitsansicht für Tabellenanlagen |
| 51-55 | Präsentationstitel, Abschnittstitel, Tabellentitel, Tabellenfortsetzung, Zellinnenabstand | fachliche statt generischer Folientitel und Teilung nach zwölf Datenzeilen |
| 56-60 | CSV-Großdatei, XLSX-Großdatei, XML/GAEB-Großdatei, DOCX-Großdatei, PDF-Großanlage | begrenzte Darstellung mit sichtbarem Vollständigkeitshinweis |
| 61-65 | Dateifehler isolieren, Stilzustand wiederherstellen, Altbestand sichern, Ausgabe atomar ersetzen, Zwischenstand entfernen | fehlertolerante und transaktionale Build-Schritte |
| 66-70 | Repo-Sofortstart, Rollenwahl, Werkstattprompt, vertiefter Kurzprompt, Mini-Schnellstart | drei klar unterschiedene Einstiegstiefen direkt im Hauptmenü |
| 71-75 | Behörden-README, Bieter-README, Konkurrenten-README, vollständiger Skillkatalog, Zusatzdateien | wichtige Einstiege bleiben sichtbar; lange Kataloge sind einklappbar |
| 76-80 | 7.500-Zeichen-Hinweis, Kurzprompt-Bezeichnung, Mini-Bezeichnung, Direktlink, Downloadzweck | Zeichenlimit nur noch beim tatsächlichen Unified Mini Prompt ausgewiesen |
| 81-85 | Portalprotokoll, interne Weiterleitung, Dokumentenmatrix, Datenexport, PDF-Kopf | reale DOCX-, XLSX-, EML- und PDF-Namen statt interner Markdown-Quellen |
| 86-90 | fünf interne Endmarker der IT-SIG-2-Akte | Produktionshinweise aus den Aktenstücken entfernt |
| 91-95 | sechs weitere Endmarker, künftige Markerprüfung, sichtbare Umlaute, Paragrafenzeichen, technische Slugs | Akteninhalt bleibt lebensnah und frei von Redaktionsresten |
| 96-100 | 248 Gesamt-PDF-Seiten, 130 Word-Seiten, 134 Excel-Seiten, 48 Präsentationsfolien, 20 Scan-PDF-Seiten | vollständige Raster-, Rand-, Leerflächen- und Sichtprüfung ohne Überlauf |

## Ergebnis

- Die sieben Gesamtakten sind direkt navigierbar, fachlich beschriftet und frei
  von isolierten Restzeilen.
- Sämtliche 90 Word-Dokumente wurden mit LibreOffice in 130 Seiten gerendert;
  keine mehrseitige Datei endet mit weniger als 400 sichtbaren Zeichen.
- Alle 45 Excel-Arbeitsmappen wurden in 134 Druckseiten geprüft; es gibt keine
  leeren Seiten, Randkollisionen oder sichtbaren Formelfehler.
- Die Präsentationsfassungen verwenden fachliche Abschnittstitel und teilen
  lange Tabellen kontrolliert.
- Neue Unit- und Artefaktvalidatoren sperren die behobenen Fehlerklassen vor
  künftigen Releases.
