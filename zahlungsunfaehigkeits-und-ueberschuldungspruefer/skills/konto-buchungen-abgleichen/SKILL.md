---
name: konto-buchungen-abgleichen
description: "Ordnet Kontoauszüge, Buchungsjournal, offene Posten und Zahlungsbelege nach Bankkonto, Vorgang und Stichtag. Prüft Anfangs- und Endsalden, interne Umbuchungen, Rücklastschriften und fehlende Gegenbelege."
---

# 1. Bankauszüge und Buchungssätze zur Insolvenzreife abstimmen

## 1.1. Zweck und Anwendungsfall

Erstelle aus heterogenen Unterlagen eine nachrechenbare Zahlungs- und Belegspur. Das Ergebnis dient der Prüfung des § 17 InsO und der Zuordnung später zu untersuchender Zahlungen.

## 1.2. Eingaben

Erfasse Konto und Währung, jeweilige Salden, Buchungstag, Wertstellung, Zeitpunkt der Verfügbarkeit, Betrag und Vorzeichen, Verwendungszweck, Gegenkonto, Belegnummer und Originalfundstelle. Ordne Buchhaltungs- und Bankidentitäten nachvollziehbar zu.

## 1.3. Ablauf

1. Erfasse pro Konto lückenlos Anfangsbestand, Auszugfolge, alle Einzelbewegungen und Endbestand. Verprobe Anfangsbestand plus Zugänge minus Abgänge mit dem ausgewiesenen Endbestand. Unterscheide fehlenden Auszug von einem belegten Nullumsatz. Bei Fremdwährung Kurs, Zeitpunkt, Nutzbarkeit und Beleg dokumentieren.
2. Gleiche PDFs, elektronischen Bankexport und Hauptbuch über Betrag, Referenz und Datum ab. Führe Splitbuchungen, Sammelzahlungen, Gebühren, Teiltilgungen und Retouren mit Zuordnung. Bei Bedarf manuelle Gegenprüfung von OCR, abgeschnittenen Zeilen und Dezimalstellen.
3. Erkenne Eigenüberträge mit Gegenbuchung. Sie verändern den Standort der Liquidität. Bei zeitversetzter Gutschrift oder einem gesperrten Zielkonto kann die Verfügbarkeit trotzdem wechseln. Doppelzählung von Originalauszug und Duplikat ausschließen. Konten verschiedener Rechtsträger einzeln halten.
4. Gib pro Vorgang Rechtsgrund, Tilgungszuordnung und Restforderung an, soweit belegt. Trenne nur im Journal erfasste Vorgänge, später zurückgebuchte Zahlungen und tatsächlich endgültige Mittelbewegungen. Wenn ein Auszug keine Uhrzeit zeigt und derselbe Tag entscheidend ist, führe Alternativen mit Belegbedarf.

5. Führe ein Eingangsprotokoll je Datei mit Absender, Erhalt, Zeitraum und Kennzeichnung als Original, Export, Duplikat oder nachträgliche Rekonstruktion. Bewahre den unbearbeiteten Bestand. Ein Screenshot kann Buchungen zeigen, ersetzt aber den Auszug samt Salden und Folgeblättern nicht. In EML-Dateien Kopfzeilen und Anlagen getrennt erfassen; Anhang und lose Kopie über Belegnummer und Inhalt zusammenführen.
6. Erstelle einen Konten- und Periodenspiegel. Prüfe Geschäftskonten, Nebenkonten, Kasse, Fremdwährung und Zahlungsdienstleister gegen die Finanzbuchhaltung. Markiere verschwundene Auszugnummern, doppelte Exporte und manuelle Nachbuchungen. Lasse ungeklärte Beträge offen und rechne ihre mögliche Auswirkung; schließe Lücken nicht durch erfundene Zeilen.
## 1.4. Quellenpflicht

Die Rechnungen benötigen konkrete Bestände und Fälligkeiten. Originalauszüge und Kontenbestätigungen tragen die Zahlen; die Rechtsprechung ersetzt diese Belege nicht.

- [BGH, Urteil vom 19. Dezember 2017 – Az. II ZR 88/16, Rn. 20–27 und 58–59](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2016/II_ZR__88-16.pdf?__blob=publicationFile&v=1).
- [BGH, Urteil vom 28. Juni 2022 – Az. II ZR 112/21, Rn. 14–17](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2021/II_ZR_112-21.pdf?__blob=publicationFile&v=1).

Die [amtliche Quellenübersicht](../../references/insolvenzreife-quellen.md) ordnet die Volltexte und ihre Grenzen ein. Zitiere nur fallbezogen geprüfte Fundstellen. Nenne für jede entscheidende Tatsache die Belegdatei und genaue Stelle.

## 1.5. Ausgabeformat

Liefere eine Kontenabstimmung mit eindeutigen Beleg-IDs, Saldenabweichungen, ungeklärten Gegenbuchungen und Datenlücken. Formuliere in einem kurzen Begleitvermerk, welche Konten und Tage belastbar sind. Liefere zusätzlich die ungeklärten Differenzen mit dem konkret benötigten Kontoauszug oder Gegenbeleg und einer bearbeitbaren Rohdatentabelle. Zahlungseingang, Umsatz, Gewinn und verfügbarer Kassenbestand dürfen dabei nicht gleichgesetzt werden. Liefere den Vermerk gemäß der Ausformulierungspflicht in vollständigen Sätzen. Skelette, Halbsätze und reine Aufzählungen ersetzen kein Endprodukt. Der Formatstandard ist Times New Roman, 11 pt, soweit technisch möglich, mit ausschließlich dezimaler Gliederung. Die Quellenprüfung folgt den im Repository geltenden Regeln aus `references/zitierweise.md`: verifizierte Rechtsprechung mit Datum, Aktenzeichen und genauer Stelle, Literatur nur aus bereitgestellter oder tatsächlich zugänglicher Quelle.

## 1.6. Beispiel

Der CSV-Export zeigt 22.000 EUR Gutschrift. Der PDF-Auszug enthält die Gutschrift und die Rücklastschrift am Folgetag. Beide Bewegungen und die Verfügbarkeit zwischen den Buchungen müssen in der Zeitachse erscheinen.
