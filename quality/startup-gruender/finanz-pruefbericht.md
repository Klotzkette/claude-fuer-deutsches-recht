# Finanzunterlagen Schnittflug – Herstellungs- und Prüfbericht

Stand: 28.09.2026. Dieser Bericht gehört nicht in die Arbeitsakte.

## 1 Herstellung

Die drei Arbeitsmappen wurden mit dem gebündelten Node und `@oai/artifact-tool` erstellt, berechnet und gerendert. Der verbindliche Artefaktmarker wurde unmittelbar vor der ersten Herstellung einmal erfolgreich mit erwarteter Ausgabezahl drei gesetzt. Keine Arbeitsmappen wurden mit openpyxl, xlsxwriter oder pandas geschrieben. Openpyxl wurde ausschließlich zum Lesen und Prüfen verwendet.

Reproduzierbarer Builder: `scripts/build-startup-gruender-finanz.mjs`. Eingaben: unveränderter gemeinsamer Fallstamm und `scripts/data/startup-gruender/finanz.json`. Die Druckmetadaten wurden anschließend in den standardisierten OOXML-Elementen ergänzt; Zellwerte und Formeln wurden dabei nicht verändert. Alle Originalrechnungen erzeugt der gesonderte Aktenbuilder aus derselben Finanzdatenliste.

Die Tabellen verwenden Arial 11 pt statt der Grundschrift juristischer Vertragsdokumente. Das begründet sich durch ihre Tabellenfunktion, begrenzten Spaltenbreiten und konsistente Darstellung in Excel/LibreOffice. Das Format bleibt innerhalb der für Tabellenlayouts zugelassenen Abweichung.

## 2 Quellen und Fallstand

Alle Personen, Rollen, nominalen Beteiligungen und Finanzierungsvarianten stammen aus `scripts/data/startup-gruender/fallstamm.json`. Die Auslagen sind ausdrücklich fiktive Aktenbelege, keine recherchierten realen Rechnungen. Die gemeinsame Akteninformation zum Raum wurde nachgereicht: monatlich 595 EUR angebotenes persönliches Raumangebot plus 833 EUR Reserve, zusätzlich 600 EUR geplante Kaution. Quellen in der Akte: E-Mails 06 und 24 sowie Raumentwurf 76. Keine Gesellschaftszahlung und kein abgeschlossener Raumvertrag wurden behauptet.

Echte Nennbeträge werden in vollen EUR geführt; Auslagenbeträge in der Quelldatei als ganze Cent. Planungsrunden sind von Kapitalvollzug getrennt. VSOP ist rein virtuell und ohne Stimmrechte. Die Abstimmungsmappe trifft keine Aussage zum sozialversicherungsrechtlichen Status oder zur Wirksamkeit eines Beschlusses. Die rechtliche Würdigung gehört zum Pluginauftrag.

## 3 Berechnungsprüfung

- Summe Gründung 25.000 EUR; nominale Planstände nach Seed 30.000 EUR, nach A 40.000 EUR und nach B 60.000 EUR.
- Preise je 1 EUR Nominal: 120 EUR, 240 EUR und 90 EUR. Agio: 595.000 EUR, 2.390.000 EUR und 1.780.000 EUR.
- Pre-/Post-Money unabhängig aus Nominalbetrag und Preis berechnet und mit gesonderten Gesprächseingaben verglichen. Die drei Kontrolldifferenzen sind null.
- Ottilie hält bei Gründung 21 Prozent; im rein investorenfinanzierten Plan nach B 8,75 Prozent. Virtueller Pool nach Erweiterung genau 10 Prozent, keine zusätzlichen echten Nennbeträge oder Stimmen.
- Zwölf Rechnungen und eine negative Gutschrift: netto 2.612,80 EUR, ausgewiesene Umsatzsteuer 496,43 EUR, brutto 3.109,23 EUR. Privat nach Rückzahlung finanziert 2.395,23 EUR; unbezahlt 714,00 EUR; Erstattung durch Gesellschaft 0 EUR.
- Letzte Cashfassung einschließlich 600 EUR Kaution: Ende Oktober 8.666 EUR, Ende November −175 EUR, Ende März −55.170 EUR. Seed/A/B in diesem Plan mit null Zufluss angesetzt; 25.000 EUR Oktober sind eine unbestätigte Annahme.
- Abstimmungsfälle 1, 2, 4 und 5 geprüft. 71 Prozent Ja bei acht Prozent Abwesenheit sind 71/92 = 77,173913 Prozent der gültig abgegebenen Stimmen, aber nur 71 Prozent des Gesamtkapitals. Keine gültige Stimme erzeugt „n.a.“ und keine scheinbar erreichte Mehrheit.
- B-Zeichnung: Investor allein, alle bisherigen Beteiligten anteilig und nur Ottilie anteilig geprüft. Bei neuer Nominale 20.001 EUR wird Ottilies Zeichnung auf 2.625 volle EUR abgerundet; der offen ausgewiesene Bruchteil verschwindet nicht. Der Investor übernimmt im Modell 17.376 volle EUR. Diese Zuteilung ist eine offene Gestaltungsannahme, keine rechtliche Empfehlung.

## 4 Neuberechnung

Der Builder verändert und restauriert repräsentative Eingaben tatsächlich: Seed-Nominale 6.000 EUR statt 5.000 EUR, virtueller Pool null statt 10 Prozent, zusätzliche März-Finanzierung 100.000 EUR, Erstattung privater Auslagen, Abstimmungsfälle und B-Zeichnungsvariante einschließlich Rundungsgrenze. Anschließend wurden die finalen Arbeitsmappen erneut berechnet und Formelfehler gesucht. Alle drei Fehlerberichte enthalten null Treffer.

Die drei Enddateien und drei geänderte Prüffassungen wurden zusätzlich mit der ausschließlich gebündelten LibreOfficeDev-Installation nativ geöffnet und als XLSX neu berechnet. 25 konkrete native Assertions prüfen ursprüngliche und veränderte Ergebnisse. Alle Zellen sämtlicher sechs nativer Dateien wurden auf Fehlerwerte gescannt: keine Formelfehler. Nachweise: `native-qa.mjs`, `verify-native.py`, `native-results.json` und `native-qa.log`. Die nativen Prüffassungen bleiben unter `/tmp`; sie ersetzen die Originaldateien nicht.

## 5 Sichtprüfung und Grenzen

Alle zehn Tabellenblätter wurden als Artifact-Tool-Bilder geöffnet und visuell geprüft. Gefundene Probleme bei Datumsformaten, langen Bezeichnungen und Druckmetadaten wurden korrigiert. Betroffene Ansichten wurden nach der Änderung erneut geprüft. Zusätzlich wurden alle drei Arbeitsmappen nativ in PDF exportiert, die Texte sämtlicher Seiten auf nichtleeren Inhalt untersucht und repräsentative Seiten geöffnet. Keine pauschale pixelweise Prüfung jeder nativen PDF-Seite wird behauptet. Die eigentliche konsolidierte Akten-PDF erzeugt der zentrale Aktenbuilder; deren Schlussprüfung ist ein eigener Schritt.

Es wurden keine nativen Excel-Desktop-Makros, Datenbankverbindungen, VBA-Funktionen oder Microsoft-Excel-Anwendungstests behauptet. Die Arbeitsmappen enthalten normale lokale Formeln und Datenvalidierungen. Die Outputs sind prüfbare Planungsdateien; Änderungen der rechtlichen Annahmen benötigen weiterhin die konkrete Mandatsprüfung.


## 6 Abschließende Druckkorrektur nach Praxistest

Die Druckmetadaten aller zehn Blätter enthalten jetzt passende Wiederholungszeilen. Bei den zwei Eingabeblättern beginnt der zweite Tabellenblock auf einer eigenen Seite; im Abstimmungsblatt beginnt der Mehrheitenvergleich auf der zweiten Seite mit wiederholter Fallkennung. Die Preisbezeichnung „Preis / EUR nominal“ ist durch eine gezielt verbreiterte Spalte vollständig sichtbar. Die virtuellen Recheneinheiten erhalten zusätzlichen Spaltenabstand; die Stimmtexte stehen zentriert mit Abstand zum Nennbetrag. Finanzwerte, Formeln und Inhalte wurden nicht geändert.

Der Vergleich sämtlicher belegter Zellen aller zehn Blätter mit den zuvor gesicherten Enddateien bestätigt identische Werte, Formeln und Datentypen; Datenvalidierungen, Zellverbindungen, bedingte Formatierungen und fixierte Fenster sind ebenfalls unverändert. Nachweis: `print-preservation.json`.

Die drei Mappen wurden aus dem angepassten Builder neu erzeugt, mit dem Artifact Tool neu berechnet und die drei geänderten Tabellenansichten erneut visuell geprüft. Anschließend wurden die nativen Original- und Mutationstests erneut ausgeführt: alle 25 Assertions bestanden, null Formelfehler in den sechs nativen Prüffassungen. Sämtliche 21 Seiten der frisch exportierten nativen Mappen-PDFs wurden geöffnet und visuell geprüft (8 + 7 + 6 Seiten). Die beanstandete Preisbezeichnung, der VSOP-Abstand und die fortgesetzten Tabellenköpfe sind jetzt lesbar. Die Seitenzahl ist unverändert.

Stabile abschließende Datei- und Builderhashes stehen in `print-final-hashes.json`, die drei aktuellen Mappenhashes zusätzlich im QA-Manifest. Das Akteninventar `quality/startup-gruender/akten-herstellung.json` wurde ausschließlich hinsichtlich dieser drei Mappen und des Finanzbuilders aktualisiert. Gesamt-PDF und Download-ZIP werden anschließend vom Hauptauftrag neu erzeugt.
