# 1. Zwei Vorführakten zum Gesellschafterstreit

## 1.1. Auftrag und Umfang

Stand der Unterlagen: 2. Oktober 2026. Zwei voneinander unabhängige Mandate für einen gemeinsamen 60-Minuten-Termin. Sie ergänzen die bestehende Akte Zink und Zunder, ohne diese oder die Fachskills zu ersetzen. Je sieben Kernunterlagen begrenzen die Erstlektüre; weitere Originalbelege stehen für Rückfragen und Gegenprüfung bereit.

| Akte | Originaldateien | Formate | Gesamt-PDF | Einzel-PDFs |
| --- | ---: | --- | ---: | ---: |
| [Klageerwiderung im Gesellschafterstreit – Berlin](../../testakten/gesellschafterstreit-klageerwiderung-berlin/README.md) | 20 | 10 DOCX, 3 EML, 3 PDF, 2 TXT, 1 CSV, 1 XLSX | 24 Seiten | 20 |
| [Drafting Shareholder Agreement – München](../../testakten/gesellschafterstreit-shareholder-agreement-muenchen/README.md) | 18 | 8 DOCX, 6 EML, 1 PDF, 1 TXT, 1 CSV, 1 XLSX | 20 Seiten | 18 |

## 1.2. Individuelle Ausarbeitung

Berlin: Spreebogen Lichtwerk GmbH mit Bühnenauftrag, streitigem Einkauf bei der Einzelfirma eines Geschäftsführers, Rechnung und tatsächlichem Lieferverlauf. Gesellschaftsvertrag, Gesellschafterliste und Registerabruf liegen getrennt vor. Einladung, Niederschrift, Beanstandung, Antwort, Zeugenmail, Bankbewegungen und Posteingang ermöglichen die Arbeit an einer Klageerwiderung. Der gerichtliche Fristlauf ist am Aktenstichtag noch offen; spätere Vorführungen müssen diesen historischen Stichtag beibehalten.

München: Isarwinkel Gerätebau GmbH mit zwei Gründern und einem vorgesehenen Investor. Eigenständige Eckpunkte und ein nicht abgestimmter Vertragsentwurf werden durch persönliche Rückmeldungen, Chatverlauf, Geschäftsführeranstellung, Entwicklungshistorie, Bankkorrespondenz, Prüfstandbestellung und Auftragsbuch ergänzt. Die Excel-Datei bildet die vorgeschlagene Kapitalaufnahme ab, ohne einen ausgearbeiteten Zielvertrag oder eine rechtliche Bewertung vorzugeben.

Personen und Unternehmen sind erfunden; Kontaktadressen verwenden die reservierte Endung `.example`. Die Hinweise stehen auf den Downloadseiten und in den ZIP-Readmes, nicht in den Originaldokumenten. Eine fertige Klageerwiderung, ein fertiger Zielvertrag und Lösungsmatrizen sind nicht beigefügt.

## 1.3. Format- und Belegprüfung

Jede E-Mail hat vollständige, syntaktisch geprüfte Header. Ihre Anlagen stimmen bytegenau mit den eigenständigen Originaldateien überein. Beide CSV-Dateien haben mindestens vier Datenzeilen und eine konstante Spaltenzahl. Die Arbeitsmappen enthalten echte Formeln; Änderungen von Eingaben wurden mit tatsächlicher Neuberechnung geprüft und anschließend zurückgesetzt. Die Bankliste stimmt mit dem Projektkonto überein; Nennbeträge, Beteiligungsquoten, Einzahlung und Aufgeld stimmen mit den Münchner Originalunterlagen überein.

Die Word-Dokumente wurden als PDF gerendert und seitenweise visuell geprüft. Die Gesamt-PDFs wurden vollständig als Bilder kontrolliert. Register und Lesezeichen führen in Dateinummernfolge zu jeder Unterlage. Die Tabellen passen jeweils auf eine Querformatseite. Zusätzliche Trennblätter zwischen jeder Unterlage entfallen.

Beide ZIP-Arten liegen flach vor. Das Originalformat-ZIP enthält die Originaldateien, zusätzlich die Gesamt-PDF und die zweisprachige Hinweisdatei. Das Einzel-PDF-ZIP enthält genau ein PDF je Original sowie die Hinweisdatei. Es enthält keine zweite Gesamt-PDF. Markdown, Prüfrubriken und dieser Prüfbericht gehören nicht in die Arbeitsarchive.

## 1.4. Fachliche Quellenkontrolle

Der in der Berliner Klageschrift angeführte BGH-Nachweis wurde am amtlichen Volltext geprüft: Urteil vom 4. April 2017, II ZR 77/16, insbesondere Randnummern 9 bis 17. Der Text unterscheidet die tatsächlichen Voraussetzungen der Abberufung, die Stimmrechtsfrage und die gerichtliche Beschlusskontrolle. Die Fundstelle ist eine begrenzte Argumentationsquelle für einen Parteischriftsatz, keine Vorentscheidung über den erfundenen Fall.

- [Amtlicher BGH-Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2016/II_ZR__77-16.pdf?__blob=publicationFile&v=1).
- [Paragraf 38 GmbHG: Abberufung](https://www.gesetze-im-internet.de/gmbhg/__38.html).
- [Paragraf 47 GmbHG: Abstimmung](https://www.gesetze-im-internet.de/gmbhg/__47.html).
- [Paragraf 55 GmbHG: Kapitalerhöhung](https://www.gesetze-im-internet.de/gmbhg/__55.html).
- [Paragraf 276 ZPO: schriftliches Vorverfahren](https://www.gesetze-im-internet.de/zpo/__276.html).

Die Vertragsentwürfe geben teilweise widersprechende Wünsche der Beteiligten wieder. Sie sind keine als rechtlich wirksam ausgegebenen Musterverträge. Technische und redaktionelle Prüfung ersetzen nicht die fachliche Kontrolle eines in der Vorführung erzeugten Ergebnisses; ein Live-Leistungsversprechen für fremde Oberflächen wird nicht abgegeben.

## 1.5. Reproduktion und Regression

Quellentexte: `scripts/vorfuehrakte_gesellschafter_berlin.py` und `scripts/vorfuehrakte_gesellschafter_muenchen.py`. Native Dokumente: `scripts/build-gesellschafter-vorfuehrakten.py`. Arbeitsmappen: `scripts/build-gesellschafter-vorfuehrtabellen.mjs`. Die Skripte betreffen ausschließlich diese beiden Akten.

Der zentrale Gesamt-PDF-Bau ruft für beide Akten `scripts/build-gesellschafter-vorfuehrpakete.py` auf. Für die Office-Dateien ist eine layoutgetreue Konvertierung erforderlich; bei deren Ausfall wird nicht unbemerkt eine reine Textfassung veröffentlicht. ZIP-Dateien entstehen über die vorhandenen zentralen Archivfunktionen.

`scripts/test-gesellschafter-vorfuehrakten.py` enthält 18 fallbezogene Regressionstests, einschließlich der konkreten Kosten- und Vollstreckungsbelehrung in der gerichtlichen Verfügung. Mit `VORFUEHRAKTEN_ZIPS` wird zusätzlich das Verzeichnis der fertig gebauten ZIP-Dateien angegeben; ohne diesen Pfad bleibt die Archivprüfung ausdrücklich ausgelassen. Der Releaseworkflow prüft die Archive nach ihrem Bau erneut. Die neuen Rubriken prüfen den Bestand und verlangen eine gesonderte fachliche Bewertung; sie enthalten keine Musterlösung.
