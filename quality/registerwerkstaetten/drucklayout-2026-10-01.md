# 1. Drucklayout-Korrektur der zwölf Registerakten

## 1.1. Anlass und Änderung

Der native Linux-Export verkleinerte einzelne Tabellen auf bis zu 4,7 pt. Die Druckkopien von genau 22 XLSX-Dateien in den zwölf neuen Registerakten erhalten deshalb feste, blattspezifische Spaltenbreiten, automatischen Wortumbruch, ausreichende Zeilenhöhen und Innenabstände. Fünf- und sechsspaltige Blätter verwenden A4 quer. Die in beiden Laufzeitumgebungen verfügbare Liberation Sans ersetzt ausschließlich in der temporären Druckkopie die bisherigen Schriften; 10 pt und identische Standard-Schriftmaße verhindern die beobachtete plattformabhängige Überverkleinerung.

Die Originaldateien werden weder überschrieben noch neu erzeugt. Der bestehende native LibreOffice-Export erstellt die Druckseiten. Die zwölf Gesamt-PDFs wurden damit neu gebaut; Versionen und Tags bleiben unverändert. Die feste Positivliste verhindert Änderungen an anderen Akten und bricht bei abweichenden Blattnamen oder Spaltenzahlen ab.

## 1.2. Integrität und automatisierte Prüfung

- Alle 280 Originalunterlagen stimmen mit dem Quellstand `v445.24.0` (`e13651fcc72f887f97f16684d399496a739e7dfd`) überein.
- Ein unabhängiger OOXML-Abgleich bestätigt für 22 Arbeitsmappen, 39 Blätter, 909 Zellen und 87 Formeln einschließlich vorhandener Cache-Inhalte die unveränderten Zellinhalte. Auch Datentypen, Zahlenformate und nicht betroffene ZIP-Bestandteile bleiben erhalten.
- Sieben Strukturtests prüfen diese Invarianten, die genaue Positivliste, Druckbereiche, erhaltene benutzerdefinierte Namen und lange deutsche Wortumbrüche. Sie sind bestanden. Die vorhandene native PDF-Regression `scripts/test-testakte-pdf-build.py` ist ebenfalls bestanden.
- Alle 22 normalen Exporte mit zusammen 39 Seiten erreichen effektiv 10,01 pt. Weitere 22 native Exporte mit um 25 % verbreiterten Spalten, entsprechend einem Puffer gegen 20 % Verkleinerung, erreichen auf allen 39 Seiten mindestens 9,81 pt.
- Der Release-Workflow führt denselben nativen Test unter Linux aus und verlangt mindestens 8 pt. Vor diesem Commit wurde die Korrektur auf macOS mit LibreOfficeDev geprüft; ein neuer Linux-Lauf wird hier nicht behauptet.

## 1.3. Sichtprüfung und Zellzuordnung

Drei getrennte Sichtberichte erfassen die konkreten neu gebauten ZIP- und PDF-Bytes. Insgesamt wurden alle 474 Gesamtseiten in Kontaktbögen sowie alle 39 Excel-Druckseiten einzeln groß angesehen. Es bestehen keine offenen Layoutbefunde. Sämtliche Tabellenzeichen der korrigierten Releasekandidaten liegen bei rund 10 pt; die zuvor problematischen Seiten sind lesbar und ohne Zellüberschneidungen.

| Bereich | Gesamtseiten | Excel-Druckseiten | Ergänzende Inhaltsprüfung |
|---|---:|---:|---|
| Transparenzregister | 122 | 12 | Auffällige Extraktionsdifferenzen gegen Originalzellen und sichtbare Zeilen geprüft; Tabellen im Gesamt-PDF zusätzlich pixelgleich zu den geprüften Einzel-PDFs. |
| Handelsregister | 122 | 13 | Alle 350 befüllten Zellen blattweise visuell zugeordnet; neun strenge PDF-Differenzmeldungen konkret aufgelöst. |
| Grundbuch und Markenamt | 230 | 14 | Alle 314 Zellen, davon 308 befüllt, einzeln anhand der tatsächlichen PDF-Zellgrenzen gegen Originalwerte, Formelergebnisse und Zahlenformate verglichen; keine Abweichung. |

Die geänderten Umbrüche ändern teilweise die Reihenfolge bei der PDF-Textextraktion. Die Freigabe beruht auf konkreten Zellen und Bildern, nicht auf identischen Zeichen- oder Token-Multimengen. Beispielsweise bleibt im Polter-Fall „kein Beschlusspunkt“ ausschließlich der Prokura Zickzack zugeordnet; die Abberufung Knautsch enthält weiterhin die Zustimmung beider Gesellschafter. Die unverändert übernommenen Zahlenformate können englische Dezimalpunkte oder Tausenderkommas enthalten.

## 1.4. Nachweis und Grenzen

Die [maschinell lesbare Prüfung](drucklayout-2026-10-01.json) enthält die geprüften Code- und Originalhashes, Exportmessungen je Arbeitsmappe sowie SHA-256 der zwölf Gesamt-PDFs, 24 ZIPs und separaten Sichtberichte. Die ursprünglichen strengen Prüfberichte bleiben unverändert; ihre konkreten Umbruchbefunde sind in den unabhängigen Folgeprüfungen aufgelöst.

Diese Prüfung betrifft Drucklayout, Exportvollständigkeit und Datenintegrität der zwölf Akten. Sie ist keine neue rechtliche Inhaltsprüfung. Öffentliche Download-Bytegleichheit und Veröffentlichung werden separat nachgewiesen.
