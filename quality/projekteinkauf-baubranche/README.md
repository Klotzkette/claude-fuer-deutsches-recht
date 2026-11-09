# Prüfung der Projekteinkaufsschulung

## 1 Akten und Formate

Die sechs Akten enthalten 92 Originaldateien und 101 PDF-Seiten. Die Prüfung verglich sämtliche Aktenstücke mit den ZIP-Mitgliedern. Alle 37 E-Mails enthalten eindeutige Nachrichtenkennungen. Die 21 Antwortverweise führen auf frühere Nachrichten. Alle 25 MIME-Anhänge stimmen byteweise mit dem jeweiligen Aktenstück überein und gehören zu ihrer vorgesehenen Übergabestufe. Der Builder prüft die Wiedergabe ihrer Dateinamen in den PDF-Lesefassungen.

Alle Word-Vorlagen, Akten-PDFs und konvertierten Seiten wurden im Layout geprüft. Die Nachbesprechungen liegen auf acht Seiten getrennt von der offenen Arbeitsakte. Bei den sechs Falltabellen wurden 386 Quellzellen auf 13 Blättern gegen die Falldaten abgeglichen. Der Preisspiegel berechnet für 42 mal 100 bei Status „belegt“ 4.200. Bei offenem Status, fehlender Menge oder fehlendem Preis bleibt der Wert leer. Eine tatsächlich eingegebene Null bleibt Null. Die Eingabespalte für LV-Kennungen hat Textformat.

## 2 Praktische Stichproben

Im Fassadenfall wurde der Mini-Prompt zunächst mit den Angaben der ersten Stufe bearbeitet. Die spätere Rechnung ergab für Hinterbogen 115.484,84 Euro netto unter Einbeziehung von Fracht und Bühne. Der Entwurf beließ Zufahrt, Tragfähigkeit und technische Bestätigung als Bedingungen für die Entscheidung. Die Probe arbeitete mit den Fallquelldaten und verglich das eigene Ergebnis erst anschließend mit der Nachbesprechung.

Im Innenausbau prüfte der mit den Falldaten vertraute Autor die 17 gesetzten E-Mails und ihre Anhänge. Er führte die drei Stufen zu einem Lieferantenentwurf mit 142 m² Startfläche und getrenntem kaufmännischem Entscheidungsstand fort. Die in einer externen Anlage eingebettete Aufforderung blieb als Akteninhalt dokumentiert. Die beiden Proben erfassen konkrete Arbeitswege. Eine externe Pluginoberfläche wurde dabei nicht getestet.

## 3 Bau und Verifikation

`scripts/build-projekteinkauf-baubranche-akten.py` erzeugt die Arbeitsdateien aus den beiden kuratierten JSON-Dateien. Der Aufruf benötigt die gebündelte Node-Laufzeit, deren Paketverzeichnis mit dem Artifact Tool und vier lizenzierte Times-New-Roman-TTFs. Der Release-Builder verwendet LibreOffice zur Konvertierung von Word- und Excel-Dateien. `--rebuild-pdfs` erzeugt die sechs Lesefassungen. Ohne diese Option verlangt der Builder dieselben vorhandenen Lesefassungen.

`scripts/build-projekteinkauf-baubranche-release.py --verify-only --dist <Releaseverzeichnis>` prüft alle 26 Dateien, 25 äußeren Prüfsummen und die buildergenerierten Archivbestände. Die ursprünglichen Downloadrouten der sechs durch die alphabetische Partition betroffenen Altakten wurden anhand der veröffentlichten Assets bestätigt und pro ZIP festgehalten.
