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

## 1.4. Quellenpflicht

Die in BGH II ZR 88/16 Rn. 20–27 und II ZR 112/21 Rn. 14–17 behandelten Rechnungen benötigen konkrete Bestände und Fälligkeiten. Ziehe neben den Rechtsquellen die Originalauszüge und Kontenbestätigungen heran. Die [amtliche Quellenübersicht](../../references/insolvenzreife-quellen.md) führt zu Normen und Volltexten. Zitiere nur fallbezogen geprüfte Fundstellen und nenne Belegdatei und Stelle für jede entscheidende Tatsache.

## 1.5. Ausgabeformat

Liefere eine Kontenabstimmung mit eindeutigen Beleg-IDs, Saldenabweichungen, ungeklärten Gegenbuchungen und Datenlücken. Formuliere in einem kurzen Begleitvermerk, welche Konten und Tage belastbar sind. Liefere den Vermerk in vollständigen Sätzen und mit dezimaler Gliederung. Für formatierten Export verwende soweit technisch möglich Times New Roman, 11 pt.

## 1.6. Beispiel

Der CSV-Export zeigt 22.000 EUR Gutschrift. Der PDF-Auszug enthält die Gutschrift und die Rücklastschrift am Folgetag. Beide Bewegungen und die Verfügbarkeit zwischen den Buchungen müssen in der Zeitachse erscheinen.
