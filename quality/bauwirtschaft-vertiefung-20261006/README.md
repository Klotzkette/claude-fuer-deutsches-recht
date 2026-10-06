# 1. Vertiefung der vier Bauwirtschafts-Workshopakten

Stand der Ausgabe: 6. Oktober 2026. Autor: Klotzkette.

## 1.1. Bestand und Erhaltung

| Akte | Vorher | Jetzt | Excel vorher | Excel jetzt | Gesamt-PDF |
| --- | ---: | ---: | ---: | ---: | ---: |
| Bad Salzuflen | 57 | 75 | 3 | 7 | 147 Seiten |
| Bürgerhaus Einbeck | 44 | 55 | 4 | 7 | 150 Seiten |
| Feuerwehrhaus Northeim | 32 | 45 | 5 | 8 | 83 Seiten |
| Werkhalle Warendorf | 30 | 43 | 2 | 5 | 83 Seiten |
| Gesamt | 163 | 218 | 14 | 27 | 463 Seiten |

Alle 163 historischen Originaldateien bleiben byteidentisch zum Ausgangscommit b2f0298220c9f82557206da9e5d3d086217d7467. Ergänzt werden 42 Belege und 13 XLSX. Die Gesamt-PDFs wurden neu erzeugt; sie enthalten die erweiterten Unterlagen. Einbeck wird ausdrücklich bis zum 6. Oktober 2026 fortgeführt. Die anderen drei Fälle behalten ihren bisherigen Septemberstichtag.

## 1.2. Fachliche Ergänzungen

Bad Salzuflen erhält detaillierte Leistungsnachweise, Lieferantenantworten, Rückliefer- und Zahlungsbestätigungen, Planprüfvermerke sowie eine Zahlungsbesprechung. Rechnungen, Korrekturen, Zahlungen und Freigaben werden nicht gleichgesetzt. Die zusätzliche Weser-Zahlung bleibt ungeklärt; sie wird nicht auf Rethmar verrechnet. Die alten Mappen 24, 25 und 55 werden durch vier erklärte Mappen ergänzt.

Einbeck führt Mengen, Nachtragskalkulation, Schlussrechnung, Betriebsbeobachtungen und Leistungsphasennachweise fort. Eine Teilfreigabe ersetzt weder eine vollständige Zahlung noch die Klärung streitiger Nachtragspositionen.

Northeim ergänzt Preisaufklärung, Herstellerinformationen, technische Prüfwerte, Referenzunterlagen und Aktenvorlage. Die ursprünglichen Angebote und Übermittlungsnachweise bleiben unverändert. Nachgereichte Informationen erhalten ihren belegten Zeitpunkt; technische und verfahrensrechtliche Streitfragen werden nicht als gelöst ausgegeben.

Warendorf ergänzt Lieferkette, technische Anschlussbedingungen, Abendbetrieb, Druckluftangebot und Zahlungszeitpunkte. Ein preislich berechenbares Angebot ist noch keine technische Freigabe oder Bestellung.

## 1.3. Tabellen und Prüfungen

Die 13 neuen XLSX wurden mit artifact-tool erstellt, nativ mit LibreOffice neu berechnet und mit gespeicherten Ergebnissen ausgeliefert. Eingaben, Formeln, Einheiten und Quellen werden in den Mappen erläutert. Historische Arbeitsmappen bleiben erhalten.

Die neuen Mappen bestehen insgesamt 96 gezielte native Eingabeänderungstests: Einbeck 30, Northeim 18, Warendorf 30, Bad Salzuflen 18. Geprüft wurden jeweils fachliche Ausgangswerte und geeignete Änderungen, darunter fehlende Werte, ausdrücklich null, falsche Konten, ungültige Varianten, offene Freigaben, geänderte Mengen und Preise. Die fallbezogenen Skripte dokumentieren die konkreten Eingaben und erwarteten Ergebnisse.

Zusätzlich bestehen 3.274 Prüfungen der gemeinsamen kaufmännischen Regression einschließlich 15 nativer Eingabeänderungen an den historischen Mappen. Der unveränderte zentrale Dokumentqualitätsvalidator meldet für die vier Akten 160 formale Dokumente und 218 Exportdateien ohne Fehler. Der README-Downloadvalidator besteht ebenfalls.

Die unabhängige Gegenprüfung fand und beseitigte unter anderem eine Datumsabweichung im Sanitärnachweis sowie unzulässige Nullannahmen bei Nachtragsmengen, Kontozuordnung und Variantenwahl. Die anschließende Prüfung derselben Eingabeketten ergänzte weitere Schutzformeln. Die Tests prüfen Dateirechnung und Bearbeitungslogik; sie sind keine allgemeinen Leistungsnachweise eines KI-Modells.

## 1.4. Dokumente und Auslieferung

Die neuen Word-Dokumente wurden mit dem kanonischen DOCX-Renderer und die Lesefassungen seitenweise visuell geprüft. Die Tabellenexports wurden auf lesbare Größen, fortgesetzte Überschriften und vollständige Erläuterungen kontrolliert. Dabei gefundene Umbruch- und Randprobleme wurden im Quellbuilder korrigiert.

Die Pakete enthalten die nativen Originale beziehungsweise jede Unterlage als einzelne PDF. Original-ZIPs enthalten zusätzlich das Gesamt-PDF. Archive sind flach, beginnen mit der vorgeschriebenen zweisprachigen README.txt und enthalten keine Markdown-, Prüf- oder Lösungsdateien. Die PDFs enthalten keinen vorgeschalteten Warntext.

Die Ausgabe erhält den eigenen Aktenrelease bauwirtschaft-akten-2026-10-06 mit eindeutigen Assetnamen. Die bisherigen Basisarchive zur Pluginversion bleiben erhalten. Die vier Aktenseiten, Plugin-README, Testaktenübersicht und Workshopanleitung unterscheiden aktuelle und historische Downloads. Die globale Pluginversion wird dafür nicht verändert.

Der [Paketnachweis](release-manifest.json) enthält Dateinamen, Mengen und SHA-256-Werte. Der [Bad-Salzuflen-Abschluss](bad-salzuflen-review.md) und der [Warendorf-Bericht](../warendorf-vertiefung-20261006/pruefung.md) ergänzen die fallbezogene Dokumentation.
