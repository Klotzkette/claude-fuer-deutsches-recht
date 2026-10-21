<!-- decimal-headings -->

# 1. Prüfung der Weserfunken-Anfechtungsunterlagen

Prüfstand: 21. Oktober 2026. Die fiktive Verfahrensakte behält ihren Aktenstand 28. September 2026 und die darin enthaltenen gerichtlichen Daten. Der Exportstand im Register des Gesamt-PDFs bezeichnet allein den technischen Neubau.

## 1.1. Bestand und Umfang

Alle 42 zuvor vorhandenen Arbeitsdateien wurden vor und nach dem Ergänzungsbau mit den gesicherten SHA-256-Werten verglichen. Sie sind bytegleich erhalten. Dies schließt Klage, K-Anlagen, gesonderte Klageerwiderung, B-Anlagen und die sieben früheren Vertiefungsdateien ein. Neue Unterlagen liegen ausschließlich unter `03_korrespondenz/05_anfechtungsunterlagen`.

| Bestandteil | Umfang | Kontrolle |
| --- | --- | --- |
| PDF-Belege | 4 Dateien, jeweils 1 Seite | Vollständiger Text und Sichtprüfung aller Seiten |
| Word-Briefe und Erinnerungsvermerke | 4 Dateien, jeweils 2 Seiten | Bearbeitbarkeit, Times New Roman 11 pt, Autor, Seitenumbrüche |
| Excel-Arbeitsmappen | 2 Dateien mit jeweils 2 Blättern | Formeln, Ergebniswerte, Datentypen, Eingabeversuche und Lesefassung |
| E-Mails | 10 Dateien; 11 eingebettete Anlagen in 7 Nachrichten | MIME-Parser, Datumsangaben, Adressen, Dateinamen und Bytevergleich |

Der Gesamtbestand umfasst damit 62 eigenständige Arbeitsdateien. Das Originalformat-ZIP enthält zusätzlich das Gesamt-PDF und die zweisprachige `README.txt`, insgesamt 64 Einträge. Das Einzel-PDF-ZIP enthält 62 PDFs und die `README.txt`. Das Gesamt-PDF hat 242 Seiten, davon drei Registerseiten. Die 65 Lesezeichen bestehen aus drei Arbeitsbereichen und 62 Einzelunterlagen. Eingebettete Anlagenkopien werden nicht als weitere Originaldokumente gezählt.

## 1.2. Inhaltliche Abgrenzungen

Als Ausgangsmaterial wurden die Fallstammdaten, Korrespondenz- und Ergänzungsfixtures sowie die vorhandenen Geschäftsbelege gelesen. Die neuen Belege erläutern die bestehenden Zahlungswege, ohne Beträge in den unveränderten Anlagen umzuschreiben. Die Zahlungseingänge bei Vellio ergeben weiterhin 590.000,00 EUR aus 18 Zinsraten und der Endtilgung. Davon entfallen 515.000,00 EUR auf die für den Belegabgleich ausgewählten letzten drei Zinsraten und die Tilgung; 505.000,00 EUR sind die beiden Schlussaufträge vom 15. April 2024. Diese ineinander enthaltenen Teilbeträge werden nicht addiert.

Die Kreditorenauswahl über 478.380,00 EUR ist kein vollständiger Finanzstatus. Die Rückabwicklung über 598.600,00 EUR ist dem 2. Mai 2024 zugeordnet und wird nicht in den April zurückgerechnet. Die neue Auskunft Krögers trennt gegenwärtig vorgenommenen Einzelkontenabgleich von eigener damaliger Wahrnehmung. Sie belegt nur die bezeichneten zwölf Posten. Lohn-, Steuer- und weitere Vertragsverpflichtungen bleiben als fehlende Eingaben sichtbar.

Die angefragte Direktzahlung an Nordkai über 42.840,00 EUR wurde ausdrücklich abgelehnt und nicht ausgeführt. Auch der erwogene Ersatz durch Lagerteile ist kein erfolgter Vermögensabfluss. Für die Bearbeitung bleibt daher zu klären, ob überhaupt eine bestimmte Rechtshandlung vorliegt; die bloße Idee begründet noch keinen Rückgewährbetrag. Der Erwerbspreis zwischen Vellio und Nexora und die ursprüngliche Kreditauszahlung sind eigene Vorgänge, keine weiteren Schuldnerzahlungen auf den streitigen Rückgewährbetrag.

Die Erinnerungen von Grothe, Kröger und Wendt sind bewusst nicht deckungsgleich. Eigene Wahrnehmung, zeitnahe Notiz, spätere Rekonstruktion und fehlender Zugang werden getrennt bezeichnet. Wendts fehlende konkrete Zahl in einer nicht wörtlichen Telefonnotiz beweist nicht, dass niemals eine Zahl fiel. Grothes heutige Erinnerung beweist umgekehrt keinen damaligen Zugang sämtlicher Unterlagen bei Vellio oder Nexora. Der Nachforderungsbrief ist als noch nicht versandter Entwurf gekennzeichnet. Die Unterlagen enthalten keine neuen gerichtlichen Entscheidungszitate und keine vorgegebene Musterlösung.

## 1.3. Rechen- und Formatprüfung

Die Arbeitsmappen wurden mit Artifact Tool erstellt, neu berechnet, inspiziert und exportiert. Die gespeicherten Formelergebnisse wurden unabhängig mit einem XLSX-Leser kontrolliert. Die erste Mappe weist aus den ausgewählten Belegen 42.520,00 EUR für April und minus 693.980,00 EUR für Mai aus; beide Größen sind ausdrücklich keine abschließende Feststellung der Zahlungsfähigkeit. Eine fehlende Eingabe zusätzlicher Verpflichtungen liefert `offen`. Der Test mit 10.000,00 EUR liefert 32.520,00 EUR, ein ausdrücklich eingegebener Nullbetrag 42.520,00 EUR. Danach wurde die Eingabe wieder gelöscht. Die Auslieferungsfassung enthält die offenen Eingaben.

In der zweiten Mappe ergab die testweise Erhöhung einer Zinsrate um 100,00 EUR einen Gesamtbetrag von 590.100,00 EUR. Nach Rücksetzung war der gespeicherte Wert erneut 590.000,00 EUR. Gezählt werden 19 tatsächlich ausgeführte Schuldneraufträge. Der bloße Drittzahlungsvorschlag bleibt davon ausgeschlossen. Datumsspalten enthalten echte numerische Excel-Datumswerte; Beträge sind numerisch und Formeln bleiben Formeln.

Alle vier neuen PDF-Seiten und alle acht Word-Lesefassungsseiten wurden visuell geprüft. Beim Excel-Export wurden die Zeilenhöhen überarbeitet, damit jedes Blatt eine vollständig lesbare Seite erhält; beide Arbeitsmappen ergeben jeweils zwei Seiten. Die finale Office-Lesefassung wurde auf allen vier Seiten geprüft: deutsche Zahlen- und Datumsdarstellung, vollständige Erläuterungen, kein abgeschnittener Tabelleninhalt und keine leere Folgeseite. Die drei Registerseiten wurden vollständig angesehen. Artifact-Tool-Vorschauen stellten Datumswerte teilweise als Seriennummern dar; maßgeblich gegengeprüft wurden deshalb zusätzlich die Datentypen des nativen XLSX und die korrekt formatierten Office-PDFs.

Die MIME-Anlagen wurden jeweils bytegenau mit den eigenständigen Dateien verglichen. Die angehängte weitergeleitete Nachricht bleibt eine vollständige EML-Datei; der MIME-Typ `application/octet-stream` erhält deren Bytes unverändert. E-Mail-Kontakte verwenden reservierte `.example`-Domains. Die Akten wurden weder versandt noch in ein reales Gerichts- oder Banksystem importiert.

## 1.4. Ausgeführte Prüfungen

```text
python3 scripts/build-fintech-bremen-anfechtung-ergaenzung.py --qa-dir /tmp/weserfunken-anfechtung-qa
python3 scripts/build-fintech-bremen-pakete.py
python3 scripts/test-fintech-bremen.py --assets /tmp/insolvenzanfechtung-20261021/dist-akten
python3 scripts/test-fintech-bremen-anfechtung-ergaenzung.py
```

Ergebnis: 14 bestehende Fall- und Archivtests sowie 5 ergänzende Tests bestanden. Die bestehenden Tests wurden ausschließlich hinsichtlich des Gesamtumfangs und der zusätzlichen Register-/Exportkontrollen erweitert; der 35-Dateien-Grundbestand und die sieben bisherigen Ergänzungen behalten ihre eigenen Prüfungen. Beide ZIPs wurden mit den jeweiligen `build_single`-Funktionen der zentralen Releasebuilder erzeugt. Der Archivvergleich kontrolliert Inhalt, Originalbytes, sämtliche PDF-Lesbarkeit und die konkreten Seitenzahlen auch der neuen Unterlagen.

Verwendet wurden die bereitgestellten Python-, Node- und Office-Laufzeiten. Zusätzliche allgemeine Builderbibliotheken lagen separat unter `/tmp`; globale Laufzeitdateien wurden nicht geändert. Vorschauen und temporäre Inspektionsdateien liegen außerhalb der Testakte. Eine technische Prüfung ist keine menschliche juristische Freigabe und bestätigt keinen realen Versand. Die fachlichen Rechtsquellen bleiben im gesonderten Quellenvermerk dokumentiert.
