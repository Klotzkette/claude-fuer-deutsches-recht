<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="weserfunken-darlehensverfahren-bremen"></a>

# 1. Weserfunken Darlehensverfahren Bremen

<!-- BEGIN gesamt-pdf-section (autogen) -->
<!-- decimal-anchor --> <a id="akte-komplett-herunterladen"></a>

## 1.1. Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Die Verfahrensakte gibt es in drei Formaten. Beide ZIPs erhalten die getrennten Ordner für Eingang, Klageerwiderung und Korrespondenz. Das Originalformat-ZIP enthält PDF, Word, E-Mail, Text und CSV, aber kein Markdown. Das Einzel-PDF-ZIP enthält jede Unterlage als eigenes PDF. Das Gesamt-PDF enthält auch die Klageerwiderung; sein Register und seine Lesezeichen führen zu den getrennten Arbeitsbereichen.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/fintech-darlehen-vertragsuebernahme-bremen_gesamt.pdf`](gesamt-pdf/fintech-darlehen-vertragsuebernahme-bremen_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-fintech-darlehen-vertragsuebernahme-bremen.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.21.0/testakte-fintech-darlehen-vertragsuebernahme-bremen.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.21.0/testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip) |

Die ZIP-Links laden den zur angegebenen Marketplace-Version gehörenden Akten-Begleitrelease. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: This project-file edition preserves its subfolders in both ZIP formats. The original-format ZIP contains editable working documents and supporting records, without Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the case companion release for the stated marketplace version.

<!-- END gesamt-pdf-section (autogen) -->

<!-- decimal-anchor --> <a id="zwei-getrennte-arbeitswege"></a>

## 1.2. Zwei getrennte Arbeitswege

Eine Insolvenzverwalterin nimmt eine österreichische Bank vor dem Landgericht Bremen in Anspruch. Die Unterlagen betreffen einen gewerblichen Kredit, seine Übertragung, Zahlungswege und die vorausgegangene deutsch-englische Korrespondenz. Aktenstand ist der 28.09.2026; die Frist zur Klageerwiderung läuft bis zum 29.10.2026.

Für die eigene Fallbearbeitung zunächst nur `01_eingang` und `03_korrespondenz` bereitstellen. `02_klageerwiderung` enthält bereits eine gesondert ausgearbeitete Verteidigerfassung und deren Anlagen. Sie ist ausdrücklich keine Musterlösung und keine gerichtliche Entscheidung, sondern der angeforderte Schriftsatz einer Partei. Das Gesamt-PDF enthält alle drei Bereiche einschließlich dieses Schriftsatzes.

Für den reinen Produktionslauf im Plugin `schriftsatz-versandwerkstatt` den Ordner `02_klageerwiderung` wählen: Hauptdokument in Word, Anlagen B1 bis B6 und vorhandene Belegbezeichnungen. Zuerst Fassung und Versandverantwortung bestätigen; dann getrennte PDFs erzeugen, Anlagenverweise abgleichen und eine Sichtkontrolle durchführen. Die Versandwerkstatt erarbeitet keine rechtliche Klageerwiderung und sendet nichts selbst.

English: Use the incoming file and correspondence folders for independent analysis. The separate defence folder contains an already drafted pleading and its exhibits for document production. The combined PDF also includes that draft. No filing or legal approval is implied.

<!-- decimal-anchor --> <a id="inhalt-und-abgrenzung"></a>

## 1.3. Inhalt und Abgrenzung

Die Eingangsakte umfasst die Klage mit 25 Seiten und zwölf Anlagen mit zusammen 75 Seiten. Hinzu kommen die gerichtliche Verfügung und der Zustellungsrücklauf. Die englischen Kreditunterlagen und deutschsprachigen Geschäftsunterlagen bleiben eigenständige Dokumente. Buchungen werden zusätzlich als maschinenlesbarer CSV-Export bereitgestellt.

Der Bestand umfasst 42 eigenständige Arbeitsdateien: Die bisherigen 35 Originaldateien bleiben bytegleich erhalten; sieben vertiefende Unterlagen kommen hinzu. Der neue Unterordner enthält eine englische Vollzugsbestätigung und eine Posteingangs-/Fristenkontrolle in Word, zwei Excel-Arbeitsmappen mit Buchungsabgleichen sowie drei E-Mails. Zwei E-Mails führen insgesamt drei echte MIME-Anlagen mit, deren Bytes den separat abgelegten Word-/Excel-Dateien entsprechen. Diese eingebetteten Kopien zählen nicht als zusätzliche eigenständige Dokumente.

Die Ergänzungen erläutern bereits dokumentierte Abläufe und ändern keine K-/B-Anlagen, Vertragssummen oder Schriftsätze. Später zusammengestellte Tabellen sind als solche datiert. Historische Kontobewegungen, die ausgewählte Kreditorenliste und der gesonderte Vorgang vom 2. Mai bleiben zeitlich getrennt. Die englische Vollzugsbestätigung ist nicht der zwölfseitige Übernahmevertrag; aus ihrer Ablage folgt nicht, dass die Klägerin diesen Vertrag vor Klageerhebung kannte.

Die gesonderte Klageerwiderung enthält das Rubrum, Anträge, eine nach Anspruchsgruppen gegliederte Zuständigkeitsrüge, streitigen Sachvortrag, rechtliche Verteidigung und konkrete Beweisangebote. Ihre Anlagen haben einen eigenen B-Nummernkreis. Die bei der Bank eingegangenen K-Anlagen werden nicht stillschweigend als eigene Anlagen neu bezeichnet.

Dieselbe zentrale Akte ist der `forderungsmanagement-klagewerkstatt` für die fachliche Bearbeitung der Forderungen und der `schriftsatz-versandwerkstatt` für die technische Endfertigung zugeordnet. Für die eigene Forderungsprüfung zunächst nur `01_eingang` und `03_korrespondenz` verwenden; der getrennte Antwortordner bleibt dem beschriebenen Produktionslauf vorbehalten. Die beiden Zuordnungen erzeugen keinen zweiten Fallbestand. Aus einem technisch erzeugten PDF folgt weder eine inhaltliche Freigabe noch eine wirksame elektronische Einreichung.

<!-- decimal-anchor --> <a id="herkunft-und-hinweise"></a>

## 1.4. Herkunft und Hinweise

<!-- reserved-example-contacts -->

Sämtliche Beteiligten, Unternehmen, Kontodaten, Registerangaben und Geschäftsabläufe sind für diese Übung erfunden. Genannte Städte und Gerichte existieren; die enthaltenen Verfügungen und Registerauszüge sind keine echten Behördenurkunden. E-Mail-Adressen verwenden reservierte `.example`-Domains. Es werden keine echten Unterschriften, Siegel oder Bankzugänge verwendet. Rechtsquellen sind von den erfundenen Parteibehauptungen zu unterscheiden.

Die Herkunftshinweise stehen unmittelbar bei den Downloads und in der Datei `README.txt` beider ZIPs. Sie sind nicht in die einzelnen Arbeitsdokumente eingebaut. Die ausdrücklich bestellte Trennung von Eingang und vorbereiteter Klageerwiderung bleibt in beiden ZIPs als Unterordnerstruktur erhalten.

<!-- decimal-anchor --> <a id="nachvollziehbarkeit"></a>

## 1.5. Nachvollziehbarkeit

Die fallbezogenen Quellen stehen im [Quellenvermerk](../../quality/legal/fintech-bremen-quellen.md). Er gehört nicht zum Originalformat-ZIP. Der Originalbuilder lautet `scripts/build-fintech-bremen-akte.py`; der PDF-Builder `scripts/build-testakte-gesamt-pdf.py fintech-darlehen-vertragsuebernahme-bremen` erhält die Arbeitsbereiche, erzeugt ein Dokumentenregister und setzt Lesezeichen. Die zentralen ZIP-Builder erzeugen die beiden Archivfassungen.

Der Regressionstest `scripts/test-fintech-bremen.py` prüft Seitenzahlen, Buchungswerte, Trennung der Arbeitsbereiche, native Dateien und die Übereinstimmung der Archive mit den Originalen. Eine menschliche juristische Freigabe oder ein Live-Versand wird durch diese Prüfungen nicht ersetzt.

Mit `scripts/build-fintech-bremen-akte.py --supplements-only --qa-dir /tmp/fintech-expansion-qa/native` lassen sich nur die sieben Ergänzungen erzeugen. Der Aufruf prüft vorher und nachher die SHA-256-Werte der 35 bestehenden Dateien. `AKTEN_NODE` und `AKTEN_NODE_MODULES` können auf den bereitgestellten Node-/Artifact-tool-Laufzeitbestand zeigen. Die Arbeitsmappen enthalten echte Formeln mit geprüften Ergebniswerten; die Vorschauen und späteren ZIP-Prüfläufe werden außerhalb des Aktenordners abgelegt.

<!-- BEGIN fintech-inventory -->
<!-- decimal-anchor --> <a id="einzelunterlagen"></a>

## 1.6. Einzelunterlagen

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Datei | Inhalt |
| --- | --- |
| [01_eingang/00_Gerichtliche_Verfuegung.pdf](01_eingang/00_Gerichtliche_Verfuegung.pdf) | Schriftliches Vorverfahren und Zustellungsunterlagen |
| [01_eingang/01_K1_Eroeffnungsbeschluss.pdf](01_eingang/01_K1_Eroeffnungsbeschluss.pdf) | Anlage K1 - Eröffnungsbeschluss vom 1. Juli 2024 |
| [01_eingang/01_Klage_20260908.pdf](01_eingang/01_Klage_20260908.pdf) | Klage |
| [01_eingang/02_K2_Loan_Agreement.pdf](01_eingang/02_K2_Loan_Agreement.pdf) | Individually Negotiated Unsecured SME Loan Agreement |
| [01_eingang/03_K3_Auszahlung.pdf](01_eingang/03_K3_Auszahlung.pdf) | Anlage K3  /  Ausführungsbestätigung |
| [01_eingang/04_K4_Kontoauszuege.pdf](01_eingang/04_K4_Kontoauszuege.pdf) | Anlage K4  /  Geschäftskonto, November 2022 bis April 2024 |
| [01_eingang/05_K5_Zahlungsaufforderungen.pdf](01_eingang/05_K5_Zahlungsaufforderungen.pdf) | Anlage K5 - Zahlungsaufforderungen vom 8. und 24. Juni 2026 |
| [01_eingang/06_K6_Antwort_Frontbank.pdf](01_eingang/06_K6_Antwort_Frontbank.pdf) | Anlage K6 - Antworten der Nexora Frontbank AG vom 18. Juni und 2. Juli 2026 |
| [01_eingang/07_K7_Kreditorenunterlagen.pdf](01_eingang/07_K7_Kreditorenunterlagen.pdf) | Anlage K7 - Offene Kreditorenposten und Buchhaltungskorrespondenz |
| [01_eingang/08_K8_Mitteilung_Vertragsuebernahme.pdf](01_eingang/08_K8_Mitteilung_Vertragsuebernahme.pdf) | Anlage K8 - Mitteilung der Vertragsübernahme, Zustimmung und Übergabebestätigung |
| [01_eingang/09_K9_Lieferantenbelege.pdf](01_eingang/09_K9_Lieferantenbelege.pdf) | Anlage K9 - Lieferantenrechnungen und Mahnungen für maritime Ventilkomponenten |
| [01_eingang/10_K10_Registerunterlagen.pdf](01_eingang/10_K10_Registerunterlagen.pdf) | Anlage K10 - Registerauszüge zu Nexora, Vellio und Weserfunken |
| [01_eingang/11_K11_Kreditangebot.pdf](01_eingang/11_K11_Kreditangebot.pdf) | Anlage K11 - Kreditangebot vom 11. Oktober 2022 |
| [01_eingang/12_K12_Mailverkehr.pdf](01_eingang/12_K12_Mailverkehr.pdf) | Anlage K12 - E-Mail-Verkehr zur Finanzierung und zur späteren Anspruchserhebung |
| [02_klageerwiderung/00_Klageerwiderung_20260928.docx](02_klageerwiderung/00_Klageerwiderung_20260928.docx) | Klageerwiderung |
| [02_klageerwiderung/01_B1_Transfer_Assumption_Agreement.docx](02_klageerwiderung/01_B1_Transfer_Assumption_Agreement.docx) | Tripartite Transfer and Assumption Agreement |
| [02_klageerwiderung/02_B2_Payment_Routing.pdf](02_klageerwiderung/02_B2_Payment_Routing.pdf) | Anlage B2 - Zahlungsanweisung und Bestätigung des Zahlungswegs |
| [02_klageerwiderung/03_B3_Vellio_Darlehenskonto.pdf](02_klageerwiderung/03_B3_Vellio_Darlehenskonto.pdf) | Anlage B3 - Vellio-Darlehenskonto und Zahlungsjournal |
| [02_klageerwiderung/04_B4_Bankabschluss.pdf](02_klageerwiderung/04_B4_Bankabschluss.pdf) | Anlage B4 - Bankseitiger Abschlussvermerk vom 14. Oktober 2022 |
| [02_klageerwiderung/05_B5_Kreditentscheidung.pdf](02_klageerwiderung/05_B5_Kreditentscheidung.pdf) | Anlage B5 - Kreditentscheidung vom 13. Oktober 2022 |
| [02_klageerwiderung/06_B6_Mandantenkorrespondenz.pdf](02_klageerwiderung/06_B6_Mandantenkorrespondenz.pdf) | Anlage B6 - Zur Vorlage freigegebene Mandantenkorrespondenz |
| [03_korrespondenz/00_Verteidigungsanzeige_20260922.pdf](03_korrespondenz/00_Verteidigungsanzeige_20260922.pdf) | Verteidigungsanzeige |
| [03_korrespondenz/01_Mail_20240312_Ratenplan_Abgleich.eml](03_korrespondenz/01_Mail_20240312_Ratenplan_Abgleich.eml) | NF-WP-221014-01 - Abgleich der Märzrate und des Schlussplans |
| [03_korrespondenz/02_Mail_20240314_Zahlungskennzeichen.eml](03_korrespondenz/02_Mail_20240314_Zahlungskennzeichen.eml) | AW: NF-WP-221014-01 - Kennzeichen bleibt unverändert |
| [03_korrespondenz/03_Mail_20240409_Ansprechpartner_Nexora.eml](03_korrespondenz/03_Mail_20240409_Ansprechpartner_Nexora.eml) | Ihre Anfrage vom 8. April - NF-WP-221014-01 |
| [03_korrespondenz/04_Mail_20240416_Endzahlung_Zuordnung.eml](03_korrespondenz/04_Mail_20240416_Endzahlung_Zuordnung.eml) | NF-WP-221014-01 - Zuordnung der Zahlung vom 15. April |
| [03_korrespondenz/05_Mail_20240418_Zahlungshistorie_Vellio.eml](03_korrespondenz/05_Mail_20240418_Zahlungshistorie_Vellio.eml) | AW: NF-WP-221014-01 - Eingang und Trennung der letzten Zahlung |
| [03_korrespondenz/06_Mail_20260610_Grothe_Vertragsgespraeche.eml](03_korrespondenz/06_Mail_20260610_Grothe_Vertragsgespraeche.eml) | WT-24-118 - Meine Erinnerung an die Rolle der Bank |
| [03_korrespondenz/07_Mail_20260616_Auskunft_Vellio.eml](03_korrespondenz/07_Mail_20260616_Auskunft_Vellio.eml) | WT-24-118 - Zahlungsempfang und Abrechnung NF-WP-221014-01 |
| [03_korrespondenz/08_Mail_20260619_Vellio_Unterlagenumfang.eml](03_korrespondenz/08_Mail_20260619_Vellio_Unterlagenumfang.eml) | AW: WT-24-118 - Ihre Anfrage zum Zahlungsempfang |
| [03_korrespondenz/09_Mail_20260707_Nexora_Buchungsabgrenzung.eml](03_korrespondenz/09_Mail_20260707_Nexora_Buchungsabgrenzung.eml) | Weserfunken - Unterlagen zur Abrechnung des Vertragswechsels |
| [03_korrespondenz/10_Mail_20260713_Vellio_Abrechnungszuordnung.eml](03_korrespondenz/10_Mail_20260713_Vellio_Abrechnungszuordnung.eml) | AW: Weserfunken - Umfang der Zahlungshistorie |
| [03_korrespondenz/20_Telefonnotiz_20240410_Terminabstimmung.txt](03_korrespondenz/20_Telefonnotiz_20240410_Terminabstimmung.txt) | Telefonnotiz vom 10. April 2024 - Gespräch mit Martin Grothe |
| [03_korrespondenz/21_Telefonnotiz_20260710_Unterlagen_Streitstand.txt](03_korrespondenz/21_Telefonnotiz_20260710_Unterlagen_Streitstand.txt) | Telefonnotiz vom 10. Juli 2026 - Gespräch mit Dr. Falk Neubauer |
| [30_Buchungsdaten_Geschaeftskonto.csv](03_korrespondenz/30_Buchungsdaten_Geschaeftskonto.csv) | Kontobuchungen mit Salden und Belegbezug |
| [03_korrespondenz/04_vertiefung/41_Completion_Confirmation_20221014.docx](03_korrespondenz/04_vertiefung/41_Completion_Confirmation_20221014.docx) | Completion Confirmation |
| [03_korrespondenz/04_vertiefung/42_Zahlungszuordnung_20260713.xlsx](03_korrespondenz/04_vertiefung/42_Zahlungszuordnung_20260713.xlsx) | Zahlungszuordnung und Abschlussabgleich |
| [03_korrespondenz/04_vertiefung/43_Kontoabgleich_20260611.xlsx](03_korrespondenz/04_vertiefung/43_Kontoabgleich_20260611.xlsx) | Kontoabgleich März und April 2024 |
| [03_korrespondenz/04_vertiefung/44_Risikorueckfrage_20240409.eml](03_korrespondenz/04_vertiefung/44_Risikorueckfrage_20240409.eml) | Weserfunken / NF-WP-221014-01: Rückfrage zu den Altunterlagen |
| [03_korrespondenz/04_vertiefung/45_Vellio_Buchungsanlagen_20260713.eml](03_korrespondenz/04_vertiefung/45_Vellio_Buchungsanlagen_20260713.eml) | Weserfunken: Zuordnungstabelle und Vollzugsbestätigung |
| [03_korrespondenz/04_vertiefung/46_Kroeger_Kontoabgleich_20260611.eml](03_korrespondenz/04_vertiefung/46_Kroeger_Kontoabgleich_20260611.eml) | NF-WP-221014-01: Kontoabgleich und Abgrenzung der offenen Posten |
| [03_korrespondenz/04_vertiefung/47_Posteingang_Fristen_20260922.docx](03_korrespondenz/04_vertiefung/47_Posteingang_Fristen_20260922.docx) | Posteingang und Fristenkontrolle |

<!-- END fintech-inventory -->
