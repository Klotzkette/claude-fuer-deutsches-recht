# 1. Prüfung der vier generierten Anfechtungsakten

Dieser Bericht dokumentiert Bestand, Lesefassungen, Rechenkontrollen und Paketbau der Akten Blechliebe Bamberg, Faltenwurf Fürth sowie der beiden VeedelWende-Fälle in Köln. Prüfstand ist der 22.10.2026. Die vier Akten umfassen zusammen 96 Originaldateien und 104 PDF-Seiten. Die JSON-Dateien in diesem Ordner halten Originaldateien, SHA-256-Werte, Einzel- und Startseiten fest; sie gehören nicht in die Akten-ZIPs.

## 1.1. Inhalt und Formate

| Akte | DOCX | PDF | EML | XLSX | TXT | Originale | Gesamt-PDF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Blechliebe Bamberg | 6 | 7 | 7 | 2 | 2 | 24 | 24 Seiten |
| Faltenwurf Fürth | 6 | 8 | 6 | 2 | 2 | 24 | 24 Seiten |
| VeedelWende Direktrückzahlung Köln | 10 | 6 | 5 | 2 | 1 | 24 | 27 Seiten |
| VeedelWende Zession Köln | 10 | 7 | 4 | 2 | 1 | 24 | 29 Seiten |
| Gesamt | 32 | 28 | 22 | 8 | 6 | 96 | 104 Seiten |

Die E-Mails besitzen MIME-Köpfe, reservierte Kontaktadressen und bei bezeichneten Anlagen die tatsächlichen Originalbytes. Eingebettete Dateien wurden gegen die selbständigen Originale verglichen. Der Versandvermerk vom 12.05.2026 in der Sicherungsabtretung vom 08.05.2026 ist ausdrücklich als nachträglicher Vermerk ausgewiesen. Minna Eberlein arbeitet in der Insolvenzkanzlei; Alina Kessel bleibt die Buchhalterin der Faltenwurf GmbH. Beide Rollen werden nicht vermischt.

Der direkte Kölner Rückzahlungsfall trennt Darlehensauszahlung, Beteiligung, Rückzahlung, Masseabfluss und den nicht unterzeichneten Serviceentwurf. Der Zessionsfall trennt Forderungskauf, Kaufpreiszahlung, Abtretungsanzeige, Gläubigerwechsel, spätere Informationsweitergabe und Rückzahlung. In beiden Fällen bleiben Tatsachen, Rechtsbehauptungen und offene Beweisfragen unterscheidbar.

## 1.2. Gegenlese der Kölner Fälle

Die [fachliche Gegenlese zu § 135 InsO](../gegenlese-2026-10-22-135.md) dokumentiert drei behobene QA-Funde:

| Befund | Korrigierter Stand |
| --- | --- |
| Die Chronologie von Kaufpreis und Anzeige war nicht durchgehend eindeutig. | Quast zahlt den Kaufpreis am 06.12.2024; die Abtretung wird der Schuldnerin danach am 07.12.2024 angezeigt. Die Bestätigung des Gläubigerwechsels folgt am 09.12.2024. |
| Der belegte Kontakt zwischen Zech und Quast konnte sprachlich als Drängen Zechs erscheinen. | Die Akte bezeichnet nur die belegte Informationsweitergabe. Quast verlangt die Zahlung anschließend selbst; ein Drängen, eine Treuhand oder eine fortbestehende Erlösberechtigung Zechs werden nicht als Tatsache behauptet. |
| Die Zahlung am 03.04.2026 lag vor Ablauf der vierwöchigen Frist am 17.04.2026. | Klageentwurf, Risikomemo und Klageerwiderung würdigen die vorzeitige Zahlung ausdrücklich eigenständig. Sie ist ein gesondert zu prüfender Umstand, beweist aber für sich keine wirtschaftliche Zurechnung zur früheren Gesellschafterin. |

Im direkten Rückzahlungsfall ist die Bezeichnung der Anlage K5 vereinheitlicht: Klageschrift und Anlagenverzeichnis nennen sie jeweils als Kontoauszug, erstellt am 04.02.2026, über die Rückzahlung vom 03.02.2026. Damit stimmen Beweisangebot, Anlagenzuordnung und Originaldatei überein.

## 1.3. Excel und Lesefassungen

Die acht Arbeitsmappen enthalten Formeln und erläutern Eingaben, Rechenweg und Reichweite. Die Bamberger und Fürther Berechnungen ergeben 8.700,00 EUR offene Lieferantenforderungen, 34.140,00 EUR Zahlungseingänge, 200.000,00 EUR verbleibende Darlehens- und Auslagenkonten sowie 17.000,00 EUR Bankrestkapital. Die Kölner Arbeitsmappen gleichen die Direktrückzahlung über 150.000,00 EUR sowie den Forderungskauf über 48.000,00 EUR und die spätere Zahlung über 96.000,00 EUR mit den jeweiligen Belegen ab.

Datumszellen enthalten echte Excel-Datumswerte; Beträge bleiben numerisch. Das explizite deutsche Zahlenformat wurde in den Office-Lesefassungen kontrolliert. Der Vorschau-Renderer kann Datumsserien und Gebietsschema abweichend darstellen; für die Sichtkontrolle waren deshalb die tatsächlichen Office-Lesefassungen maßgeblich. Die Arbeitsmappen werden jeweils vollständig einschließlich ihrer Erläuterungen ausgegeben.

Die 32 Word-Dateien wurden gerendert. Die vier Gesamtakten wurden seitenweise kontrolliert; die JSON-Prüfmanifeste ordnen alle 96 Originale mit ihren Einzel- und Startseiten den insgesamt 104 PDF-Seiten zu. Kein Original-PDF und keine PDF-Lesefassung enthalten den Testakten-Warnhinweis. Dieser steht vor den Downloads und in der `README.txt` jedes ZIPs.

## 1.4. Wiederholbarer Paketbau

`python3 scripts/build-insolvenzanfechtung-akten.py --package-only --dist <Zielordner>` benötigt LibreOffice und die Python-Bibliotheken des Repositorys, jedoch weder artifact-tool noch einen Node-Lauf. Word und Excel werden aus den vorhandenen Originalen nativ konvertiert; E-Mail- und Text-Lesefassungen entstehen aus den gespeicherten Originalbytes. Die JSON-Vorlage bestimmt Dateiauswahl und Katalogbeschreibung. E-Mail-Anlagen werden nicht doppelt in das Gesamt-PDF übernommen.

Zwei abschließende End-to-End-Builds lieferten byteidentische Release-Dateien. Jedes der acht ZIPs enthält genau 24 Unterlagen sowie eine `README.txt`; die ZIPs bleiben flach und enthalten keine Markdown-Dateien. Die Originaldateien stimmen mit den SHA-256-Werten der Prüfmanifeste überein. Die vier Gesamt-PDFs und die Einzel-PDF-ZIPs enthalten jeweils 24 Dokumente mit zusammen 104 Seiten.
