# PDF-Layoutprüfung mit Abschlussbefund

**Abschlussstand vom 8. Oktober 2026:** Die zu kleine Tabellenschrift und der Würzburger Standversatz sind behoben. Die abschließende technische Prüfung aller 179 Seiten, der vollständige Abgleich von 384 Tabellen-Textzellen und die erneute Sichtprüfung sind in Abschnitt 8 dokumentiert. Für die dort identifizierten finalen Dateien besteht kein offener wesentlicher Layoutbefund. Die Abschnitte 1 bis 7 halten die vorherige Zwischenprüfung als Prüfspur fest; deren offene Befunde sind durch Abschnitt 8 abgeschlossen.

## 1. Historischer Stand und Ergebnis der Erstprüfung

Geprüft am 8. Oktober 2026: drei Gesamt-PDFs der neuen AML-Testakten und die beiden Lesefassungen des Plugins. Die Prüfung erfasst **179 Seiten technisch und 14 tatsächlich gerenderte Seiten visuell**. Sie bezieht sich auf die unten anhand ihrer SHA-256-Werte identifizierten Zwischenstände. Ein abschließender Neubau ist angekündigt; dieser Bericht ist keine Layoutfreigabe der späteren Release-Dateien.

In keinem geprüften PDF wurden Textbegrenzungen außerhalb der jeweiligen Seite, leere Seiten oder die untersuchten Ersatz- und Quadratzeichen festgestellt. Die gerenderten Belegseiten, Word-Seiten und Handbuchseiten zeigen keine abgeschnittenen Zeilen, sichtbaren fehlenden Glyphen oder überlagerten Texte.

**Offener Befund: Die verkleinerten Excel-Druckseiten sind für einen Ausdruck zu klein.** Die Schrift der Zahlungszeilen beträgt nur 5.10 pt. Die vollständige Textübernahme allein genügt hier nicht für eine gut nutzbare Lesefassung. Der verantwortliche Bearbeiter hat eine gezielte Korrektur der Druckdarstellung angekündigt. Nach dem Neubau sind mindestens die geänderten Tabellen, sämtliche Seitenbegrenzungen und die Textvollständigkeit erneut zu prüfen.

## 2. Prüfverfahren und Grenzen

Die Ausgangsdateien wurden für diese Prüfung unverändert in einen lokalen Prüfungsordner kopiert. Die SHA-256-Werte beziehen sich auf diese Kopien. Poppler `pdftoppm` renderte die ausgewählten Seiten mit 120 dpi. Die ausgegebenen PNG-Dateien wurden tatsächlich geöffnet und visuell geprüft. PyMuPDF 1.28.2 prüfte auf jeder Seite alle extrahierten Text-Spans einschließlich ihrer Begrenzungsrechtecke; eine Überschreitung des Seitenrechtecks um mehr als 0.5 pt wurde als Auffälligkeit gezählt. Die Prüfung erfolgte ohne Beschränkung der Textextraktion auf die MediaBox.

Zusätzlich wurden die Texte auf U+FFFD, U+25A1, U+25A0 und U+0000 untersucht, die kleinsten Schriftgrößen erfasst und nichtleere Textzellen der nativen Excel-Arbeitsmappen mit den zugehörigen Druckseiten verglichen. Beim Textvergleich wurde ausschließlich Leerraum vereinheitlicht. Zahlenformatierungen und Datumsdarstellungen wurden in diesem ergänzenden Textzellenvergleich nicht pauschal umgedeutet.

Die Begrenzungsprüfung erkennt seitlichen oder vertikalen Textüberlauf, ersetzt aber keine Sichtprüfung aller Seiten. Die Glyphenprüfung ist eine technische Auffälligkeitskontrolle; sie beweist nicht allein die optisch richtige Darstellung jedes Zeichens. Die Sichtprüfung deckt die ausdrücklich genannten 14 Seiten ab. Fachliche Rechtsprüfung und die rechnerische Prüfung der nativen Tabellen sind getrennte Kontrollen.

## 3. Umfang und Sichtprobe

Alle Seitenangaben bezeichnen die fortlaufende PDF-Seite, nicht eine gegebenenfalls abweichende gedruckte Seitenzählung.

| PDF | Seiten insgesamt | Gerenderte und gesichtete Seiten | Ergebnis der Sichtprobe |
| --- | ---: | --- | --- |
| Erfurt, Gesamtakte | 41 | 15: Zahlungen; 23: Telefonnotiz U-D03; 27: Auftragsbestätigung U-P01 | Word und Beleg sauber; Zahlungsübersicht vollständig, aber erheblich zu klein |
| Berlin, Gesamtakte | 41 | 15: Zahlungen; 23: Telefonnotiz K-D03; 27: Kaufvertragsauszug K-P01 | Word und Beleg sauber; Zahlungsübersicht vollständig, aber erheblich zu klein |
| Würzburg, Gesamtakte | 41 | 15: Zahlungen; 23: Telefonnotiz N-D03; 27: Kaufvertragsauszug N-P01 | Word und Beleg sauber; Zahlungsübersicht vollständig, aber erheblich zu klein |
| Skills-Handbuch | 45 | 1, 20, 44 | Ruhiger Satz, lesbare Quellenangaben, keine erkennbaren abgeschnittenen Zeilen |
| Werkstatt-Lesefassung | 11 | 1, 10 | Lesbarer Text; Tabelle auf Seite 1 vollständig, teils enge Wortumbrüche |

Alle fünf Dateien haben jeweils **0 Text-Spans außerhalb der Seite, 0 untersuchte Ersatz-/Quadratzeichen und 0 Leerseiten**. Auf den Handbuchseiten wurden keine Text-Spans unter 8 pt gefunden.

## 4. Historischer Befund an den Tabellen, inzwischen behoben

Die folgenden Schriftgrößen treten in allen drei Gesamtakten auf:

| PDF-Seite im geprüften Zwischenstand | Arbeitsblatt | Gemessene Schriftgröße des Tabelleninhalts |
| ---: | --- | ---: |
| 14 | Übersicht | 7.41 pt |
| 15 | Zahlungen | 5.10 pt |
| 16 | Beteiligte | 5.89 pt |
| 17 | Verlauf | 5.89 pt |

Die Zahlungsseiten nutzen eine breite Tabelle mit neun Spalten. Trotz großer freier Fläche unter der Tabelle wird der gesamte Tabelleninhalt auf die Seitenbreite verkleinert. In der Sichtprobe lassen sich die Zeichen bei starker Vergrößerung erkennen, auf einem Ausdruck in Originalgröße ist der Satz zu klein.

Empfohlen ist eine Druckdarstellung mit mindestens 9 pt, besser 9.5 bis 11 pt. Die Zahlungsangaben können in zwei Teiltafeln mit wiederholter Vorgang-ID oder in je einen Kopf mit Vorgang-ID, Datum, Betrag und Nachweisstand sowie einen zugehörigen Detailblock für Zahler, Empfänger, Beleg und Zuordnung aufgeteilt werden. Umbruch und zusätzliche Zeilenhöhe sollen die Informationen aufnehmen; eine weitere Verkleinerung würde den Befund nicht beheben. Die nativen Daten, Formeln, Belegstatus und Betragskategorien müssen erhalten bleiben.

## 5. Historischer Abgleich der Tabelleninhalte und Standversatz

Für Erfurt wurden alle 124 nichtleeren Textzellen und für Berlin alle 132 nichtleeren Textzellen in den vier Druckseiten wiedergefunden. Für Würzburg sind Übersicht, Zahlungen und Beteiligte vollständig enthalten: 106 nichtleere Textzellen. Während der Prüfung wurde die native Würzburger Chronologie bereits fortgeschrieben. Sechs der nun 22 Textzellen dieses Arbeitsblatts unterscheiden sich deshalb vom gesicherten PDF-Zwischenstand, unter anderem die getrennten Nachweise zu den Bankabgängen von 110.000 EUR und 450.000 EUR sowie die präzisierten E-Mail-Bezüge.

Dieser Befund wird als **Standversatz zwischen aktueller XLSX und älterer PDF-Kopie** geführt, nicht als nachgewiesener Textbeschnitt. Der endgültige Neubau muss alle aktuellen Textzellen übernehmen; danach ist der Abgleich erneut durchzuführen.

## 6. Prüfnachweise und lokale Screenshots

Die 14 PNG-Dateien, die fünf unveränderten PDF-Prüfkopien und die technischen Messdaten liegen lokal unter `/tmp/aml-pdf-layout-20261008/`. Sie werden nicht pauschal in das Repository aufgenommen. Die Messdatei heißt `layout-metrics.json`.

| Bildpräfix | Vorhandene PNG-Seiten |
| --- | --- |
| `aml-unternehmen-werkzeughandel-erfurt_gesamt` | `-p15.png`, `-p23.png`, `-p27.png` |
| `aml-kanzlei-grundstueck-berlin_gesamt` | `-p15.png`, `-p23.png`, `-p27.png` |
| `aml-notariat-kaufpreis-wuerzburg_gesamt` | `-p15.png`, `-p23.png`, `-p27.png` |
| `geldwaeschebeauftragter-skills-handbuch` | `-p01.png`, `-p20.png`, `-p44.png` |
| `geldwaeschebeauftragter-werkstatt-lesefassung` | `-p01.png`, `-p10.png` |

Die geprüften Dateistände sind durch folgende SHA-256-Werte festgehalten:

| PDF | SHA-256 |
| --- | --- |
| Erfurt, Gesamtakte | `56515575326c5ed3e6902409983e700aade686fd4c5317f258893fd10c0809e4` |
| Berlin, Gesamtakte | `d365e98f270885df75ff8a8e2ba2b5fdc676f12e708974d7960928df824a2d4e` |
| Würzburg, Gesamtakte | `0be4060f10da4502a38bf8b50a63379226b96166c8ac48f37e5324d8357ad884` |
| Skills-Handbuch | `bc0d63484b48af16c0ac39985ed82cb1cbfa713a43c99feeb714908c0d0a2e15` |
| Werkstatt-Lesefassung | `7619331a33d2c12bc84ebeca91c7b6939f4e4adeb7c76f6374a27ae63d872d6d` |

## 7. Damals angeforderte Abschlussprüfung

Nach dem angekündigten Neubau sind die finalen SHA-256-Werte und Seitenzahlen zu erfassen, alle Seitenbegrenzungen erneut zu prüfen, alle aktuellen Tabellen-Textzellen abzugleichen und mindestens die veränderten Tabellen vollständig neu zu rendern und anzusehen. Der offene Befund darf erst nach tatsächlich geprüfter Lesbarkeit geschlossen werden. Bereits gesichtete Zwischenstände werden dadurch nicht rückwirkend als endgültige Dateien ausgegeben.

## 8. Abschließende Prüfung der finalen Dateien

Die drei neu gebauten Gesamtakten umfassen weiterhin jeweils 41 Seiten. Am 8. Oktober 2026 wurden alle 179 Seiten der fünf finalen Dateien erneut mit demselben Begrenzungs- und Glyphenverfahren geprüft. Ergebnis: **0 Text-Spans außerhalb der Seite, 0 untersuchte Ersatz-/Quadratzeichen, 0 Leerseiten und keine Text-Spans unter 8 pt.**

Die zwölf Tabellenblätter in den Gesamt-PDFs verwenden nun Times New Roman mit 9.5 pt für die Tabelleninhalte; Begleittext ist 11 pt groß. Die tatsächlich eingebetteten Textfonts heißen `TimesNewRomanPSMT` und `TimesNewRomanPS-BoldMT`. Die laufenden Kopf- und Fußzeilen haben 9 pt, die Abschnittsüberschriften 14 pt. Die Zahlungsvorgänge erscheinen jeweils als eigener Kopf mit zugehörigem Detailblock. Die Schrift wird nicht mehr auf 5.10 pt verkleinert. Sämtliche vier Tabellenblätter jedes Falls wurden technisch auf Schriftgrößen und Textübernahme geprüft.

### 8.1. Vollständigkeit der aktuellen Tabellen

Alle nichtleeren Textzellen der drei aktuellen nativen Excel-Arbeitsmappen wurden im jeweils zugehörigen finalen Druckblatt wiedergefunden. Der Vergleich vereinheitlichte Leerraum, ohne die Wörter oder Belegkennungen umzudeuten.

| Akte | Übersicht | Zahlungen | Beteiligte | Verlauf | Fehlende Textzellen |
| --- | ---: | ---: | ---: | ---: | ---: |
| Erfurt | 27 | 38 | 43 | 16 | 0 |
| Berlin | 29 | 38 | 49 | 16 | 0 |
| Würzburg | 28 | 38 | 40 | 22 | 0 |
| Gesamt | 84 | 114 | 132 | 54 | 0 |

Damit sind alle **384 Textzellen** erfasst. Die aktualisierte Würzburger Chronologie enthält insbesondere die getrennten Bankabgänge über 110.000 EUR und 450.000 EUR sowie die präzisierten Belegbezüge. Der in Abschnitt 5 festgehaltene Standversatz ist geschlossen.

### 8.2. Erneute Sichtprüfung

Erneut mit Poppler bei 120 dpi gerendert, geöffnet und angesehen wurden Würzburg, PDF-Seiten 14 bis 17, sowie Erfurt und Berlin, jeweils PDF-Seite 15. Diese sechs Seiten zeigen lesbare Tabellen, vollständige Textblöcke und ausreichend Abstand zu Seitenrändern und Fußzeilen. Es wurden keine abgeschnittenen Zeilen, fehlenden Glyphen oder Textüberlagerungen festgestellt. Der Befund aus Abschnitt 4 ist behoben.

Das Skills-Handbuch erhielt inzwischen einen neuen Dateistand. Deshalb wurden neben der technischen Prüfung aller 45 Seiten auch seine Seiten 1, 20 und 44 erneut gerendert und angesehen. Auch dort besteht kein neuer Layoutbefund. Die Werkstatt-Lesefassung ist anhand ihres unveränderten SHA-256-Wertes identisch mit der bereits gesichteten Fassung; die Sichtprobe aus Abschnitt 3 gilt für diese Datei fort. Ihre elf Seiten wurden zusätzlich nochmals technisch geprüft.

Die Schlussprüfung umfasst damit **neun neu gerenderte und tatsächlich gesichtete Seiten**, ergänzend zu den 14 Seiten der historischen Erstprüfung. Die Sichtprüfung bleibt eine begrenzte Stichprobe; die Begrenzungs- und Glyphenkontrolle erfasst dagegen alle 179 finalen Seiten.

### 8.3. Finale Dateien und Nachweise

Die finalen PDF-Prüfkopien, neun PNG-Dateien und die aktualisierten Messdaten liegen lokal unter `/tmp/aml-pdf-layout-20261008-final/`. Die technischen Ergebnisse einschließlich sämtlicher Schriftgrößen und Textzellen-Zählungen stehen dort in `layout-metrics.json`. Die historischen Nachweise unter `/tmp/aml-pdf-layout-20261008/` bleiben als getrennte Prüfspur erhalten. Keine Screenshot-Sammlung wird pauschal in das Repository aufgenommen.

| Finale PDF-Datei | Seiten | SHA-256 |
| --- | ---: | --- |
| `aml-unternehmen-werkzeughandel-erfurt_gesamt.pdf` | 41 | `f5be6ee9fb08fd17a1dccf655ad08166e72484da7abb5c84de8bd8a35dd29634` |
| `aml-kanzlei-grundstueck-berlin_gesamt.pdf` | 41 | `997f434705a96401ec50b5d06d20b9cd473645892ab73a46ac59633d59f708b3` |
| `aml-notariat-kaufpreis-wuerzburg_gesamt.pdf` | 41 | `b89f25c3156b2bd89fec12ebf8b0e04bb4cd4453ad3b356fcb7f8c8ffcb1ca65` |
| `geldwaeschebeauftragter-skills-handbuch.pdf` | 45 | `9eca32ac248e2960257c771cfa677682d3676345450ca8489e66f589b9a7be55` |
| `geldwaeschebeauftragter-werkstatt-lesefassung.pdf` | 11 | `7619331a33d2c12bc84ebeca91c7b6939f4e4adeb7c76f6374a27ae63d872d6d` |
