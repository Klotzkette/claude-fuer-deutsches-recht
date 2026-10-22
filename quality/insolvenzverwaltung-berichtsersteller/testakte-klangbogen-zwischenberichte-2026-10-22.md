# Qualitätsnachweis Testakte Klangbogen

Stand: 22. Oktober 2026

## 1. Gegenstand

Dieser Nachweis beschreibt das feste Prüfprofil der vollständig fiktiven Testakte `insolvenzverwaltung-klangbogen-buehnentechnik-bamberg`. Der Aktenlauf betrifft eine Gesellschaft für Bühnen-, Akustik- und Probenraumtechnik. Er dient dazu, aus einer langen Folge turnusmäßiger Zwischenberichte den Verfahrensgang, die Rechenstände, offene Belege und die zuletzt erreichte Schlussreife zu rekonstruieren und anschließend einen eigenständigen Schlussbericht zu entwerfen.

Die Akte enthält bewusst keinen fertigen Schlussbericht. Menschliche Freigaben, gerichtliche Zustimmungen, Zahlungsvollzug und Verfahrensaufhebung dürfen aus dem letzten Zwischenbericht nicht hinzuerfunden werden.

## 2. Dateiprofil

| Bestandteil | Anzahl | Prüfziel |
| --- | ---: | --- |
| Turnusmäßige Zwischenberichte als einzelne PDFs | 22 | fortgeschriebener Verfahrensgang und zeitbezogene Beleglage |
| Berichtsseiten | 233 | feste Seitenfolge je Bericht und vollständiger Nachweislauf |
| Gesonderte Beleg-PDFs | 15 mit zusammen 30 Seiten | gerichtliche, steuerliche, bankseitige und abrechnungsbezogene Gegenprüfung |
| EML-Dateien | 8 | tatsächliche MIME-Anlagen, Absender, Empfänger, Datum und Betreff |
| XLSX-Rechenmappe | 1 | Berichtsperioden, Kontenjournal, Forderungen, Belegmatrix und Schlussreife |
| TXT-Arbeitsnotizen | 3 | Arbeitsauftrag, offene Punkte und Chronologieabgleich |

Die 37 Quell-PDFs werden zu einem 263-seitigen Gesamt-PDF zusammengeführt. Darin folgen auf die 233 Berichtsseiten 30 gesonderte Belegseiten. Acht EML-Dateien, eine XLSX-Rechenmappe und drei TXT-Arbeitsnotizen bleiben als bearbeitbare beziehungsweise strukturierte Arbeitsunterlagen erhalten; einschließlich README, Rubrik und Gesamt-PDF enthält der Aktenordner 52 Dateien.

Der Einzel-PDF-Bestand und das aus den freigegebenen Quelldateien erzeugte Gesamt-PDF sind getrennt zu prüfen. Die ZIP-Pakete müssen auf ihrer Wurzelebene mit dem vorgeschriebenen zweisprachigen Hinweis beginnen.

## 3. Berichtsfolge

| Bericht | Datum | Seiten |
| ---: | ---: | ---: |
| 1 | 28.05.2016 | 9 |
| 2 | 02.12.2016 | 8 |
| 3 | 03.06.2017 | 9 |
| 4 | 27.11.2017 | 9 |
| 5 | 28.05.2018 | 8 |
| 6 | 07.12.2018 | 10 |
| 7 | 28.05.2019 | 11 |
| 8 | 25.11.2019 | 10 |
| 9 | 24.05.2020 | 9 |
| 10 | 20.11.2020 | 8 |
| 11 | 23.05.2021 | 8 |
| 12 | 29.11.2021 | 8 |
| 13 | 23.05.2022 | 51 |
| 14 | 05.02.2023 | 8 |
| 15 | 05.11.2023 | 9 |
| 16 | 30.03.2024 | 9 |
| 17 | 28.05.2024 | 9 |
| 18 | 25.11.2024 | 9 |
| 19 | 18.05.2025 | 9 |
| 20 | 08.11.2025 | 9 |
| 21 | 05.06.2026 | 8 |
| 22 | 28.11.2026 | 5 |
| Summe | 3.836 Tage zwischen erstem und letztem Bericht | 233 |

Die Verfahrenseröffnung liegt am 22.11.2015 und damit 188 Tage vor dem ersten Zwischenbericht. Die Abstände zwischen sämtlichen Berichtsdaten sind Bestandteil der automatisierten Chronologiekontrolle. Bericht 13 muss einschließlich seines Nachweislaufs 51 Seiten umfassen. Bericht 22 bleibt auf fünf Seiten beschränkt und enthält keine nur der Form halber wiederholten Finanzanlagen.

## 4. Rechenprofil

| Kontrollgröße | Sollwert | Bedeutung |
| --- | ---: | --- |
| Schlussbestand | 538.776,34 EUR | Ausgangswert der vorläufigen Schlussrechnung |
| Festgestellte Forderungen | 1.764.825,62 EUR | Nenner der vorläufigen Quote |
| Reserven | 119.776,27 EUR | vor einer Verteilung noch zurückzubehaltende Beträge |
| Vorläufige Verteilungsmasse | 419.000,07 EUR | Schlussbestand abzüglich Reserven |
| Vorläufige Quote | 23,741726 Prozent | ungerundete Arbeitsquote auf sechs Dezimalstellen gerundet |

Die Rechenmappe muss die Berichtsperioden mit den Zwischenberichten verbinden und die Schlussreife als eigenen Kontrollbereich ausweisen. Formelwerte dürfen weder durch fest eingetippte Ergebniswerte ersetzt noch mit einem bereits vollzogenen Verteilungslauf verwechselt werden.

## 5. Technische Abnahme

Die technische Abnahme umfasst mindestens folgende Kontrollen:

1. Die 22 Einzelberichte liegen in der festgelegten Reihenfolge vor; die Seitenzahlen entsprechen Abschnitt 3 und ergeben zusammen 233 Seiten.
2. Sämtliche PDFs lassen sich öffnen, enthalten Text und weisen keine leeren oder abgeschnittenen Seiten auf.
3. Die acht EML-Dateien lassen sich mit einem Standardparser öffnen; angekündigte Anlagen stimmen bytegenau mit den beigefügten Dateien überein.
4. Die XLSX-Datei lässt sich öffnen, enthält die sechs vorgesehenen Tabellenblätter und zeigt keine Formel- oder Darstellungsfehler.
5. Das Gesamt-PDF enthält mindestens repräsentative Inhalte aus Bericht 1, Bericht 13, Bericht 22 und den gesonderten Belegen.
6. Lokale README-Verweise zeigen auf vorhandene Dateien; die veröffentlichten ZIP-Verweise verwenden für diese Akte den Komponentenstand `insolvenzverwaltung-berichtsersteller-v1.1.0`.
7. Die Warnhinweise stehen ausschließlich an den vorgeschriebenen Downloadstellen und in den ZIP-Wurzeldateien, nicht in den Berichts- oder Beleg-PDFs.

## 6. Fachliche Abnahme

Die fachliche Prüfung muss den Schlussbericht als eigenes, aus der Akte abgeleitetes Produkt behandeln. Sie gleicht mindestens Verfahrenschronologie, Aktiv- und Passivmasse, Verwertung, Prozesse, Steuern, Forderungstabelle, Schlussbestand, Reserven und vorläufige Quote ab. Widersprüche oder fehlende Belege werden als offene Punkte ausgewiesen. Der Arbeitslauf endet an einem benannten Freigabegate; er behauptet weder einen Vergütungsbeschluss noch eine gerichtliche Verteilungszustimmung oder eine bereits erfolgte Auszahlung.
