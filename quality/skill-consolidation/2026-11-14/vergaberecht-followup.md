# 1. Vergaberecht: Rollen und vollständige Fachmodule nach der Konsolidierung

Die verschachtelte Vergaberecht-Werkstatt behält ihre drei Marktrollen. Vergabestelle und Bieter haben jeweils acht aktive Skills einschließlich ihres Hauptworkflows; beim Konkurrentenrechtsschutz bleiben zwanzig aktive Skills. Sämtliche 122, 113 und 20 ursprünglichen Fachmodule bleiben erhalten. Die aktive Auswahl umfasst damit 36 Skills, die Fachbibliothek weiterhin 255 Module.

## 1.1. Gezielte Änderungen

Die sieben zuvor zwischen Bieter- und Auftraggeberseite gleichlautenden Routenbeschreibungen sind jetzt rollenbezogen formuliert. Sie unterscheiden unter anderem Angebotsvorbereitung von Behördenentscheidung, Rügeschreiben von Vorabinformation und Bieterantrag von behördlicher Stellungnahme. Mitgliedschaften und vollständige Fachtexte wurden dabei nicht geändert.

Für diese vierzehn neu erzeugten Routen ist der lokale Dokumentstil ausdrücklich in der Registry hinterlegt. Der Renderer übernimmt den bereits bestehenden verbindlichen Ausgabeabsatz der Vergaberecht-Werkstatt: Times New Roman 11 pt, Dezimalgliederung, begrenzte Hervorhebungen und Vorrang abweichender Vorgaben der empfangenden Stelle. Sichtbare Normzitate werden mit § bzw. §§ gesetzt; technische Dateinamen bleiben unverändert. Der Discovery-Validator unterscheidet sichtbaren Linktext von dessen technischem Ziel. Negativtests sichern weiterhin die Ablehnung ausgeschriebener Normzitate im sichtbaren Text.

Ein durch die Navigationstransformation falsch verschachtelter Weblink in der KI-Referenz der Vergabestelle wurde auf seine ursprüngliche URL zurückgeführt. Die gesamte betreffende Referenzdatei ist dadurch wieder bytegleich mit ihrem Original vor der Migration. Die öffentliche Zielprüfung erlaubt außerdem nur die drei ausdrücklich benannten, lokal vorhandenen Übersichtsseiten des übergeordneten Repositorys. Beliebige komponentenfremde Ziele und verschachtelte URLs bleiben unzulässig.

Der lokale Marketplace führt die beiden migrierten Plugins mit `445.36.0`. Index und README nennen die tatsächliche aktive Auswahl. Plugin-ZIPs werden anhand der zentralen Releasezuordnung verlinkt; bestehende Sammel- und Markdown-Archive behalten ihren früheren veröffentlichten Versionsstand und sind entsprechend bezeichnet.

## 1.2. Nachweis der Erhaltung

Der [JSON-Nachweis](vergaberecht-followup.json) enthält inverse Dateiänderungen, ursprüngliche und neue Registry-Hashes sowie das inverse Renderer-Delta. Vor der Änderung wurden die vierzehn betroffenen Routen mit dem alten Renderer bytegleich reproduziert und gegen ihre SourceMap-Hashes geprüft. Bei den übrigen 1.611 Registryrouten erzeugen alter und neuer Renderer aus denselben Eingaben identische Ergebnisse. Die neuen Routen lassen sich mit dem erweiterten Renderer reproduzieren. Der ursprüngliche Quellenbestand wird nicht durch neu gesetzte Hashes ersetzt.

Die SourceMap-Prüfung einschließlich strenger Paket-Linkprüfung besteht. Alle ursprünglichen Quelldateien bleiben aus den dokumentierten Änderungen bytegleich rekonstruierbar. Eine Änderung fachlicher Inhalte oder eine neue Quellenprüfung wird daraus nicht abgeleitet. Bestehende offene Reviewstände bleiben bestehen.

## 1.3. Ausgeführte Prüfungen

Die einzelnen Prüfungen für Pluginstruktur, Frontmatter, Discovery, gemeinsame Referenzen, Rechtsstand, Systemintegration, Dokumentlinks, Navigation, öffentliche Prompt-Synchronisation und öffentliche Integration bestehen. Die Rechtsstandsprüfung erfasst weiterhin 583 Textdateien, 161 Binärartefakte und fünf Beschwerdekerne; die Systemprüfung drei Rollen und 32 Dateien. Die öffentliche Integration prüft die 36 aktiven Skills getrennt von allen 255 ursprünglichen Fachmodulen. Die Navigation prüft drei Plugins, sieben Testakten und 42 Release-Dateiverweise.

Zusätzlich bestehen 14 Migrationstests, 13 Integrationstests, 16 öffentliche Integrationstests und drei gezielte Discovery-Regressionstests. Die [einzelnen Logs](vergaberecht-followup/) und ihre Hashes sind im JSON-Nachweis verzeichnet. Der abschließende Quick-Smoke-Lauf und seine zusätzlichen Fachpfad-/Megapromptprüfungen werden nach deren Anpassung gesondert dokumentiert. Keine neue Primärquellenprüfung, Modellausführung oder Veröffentlichung wird behauptet.
