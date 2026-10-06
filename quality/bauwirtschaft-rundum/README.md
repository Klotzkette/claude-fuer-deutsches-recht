# 1. Bauwirtschaft rundum: Liefer- und Prüfstand

Teilrelease `bauwirtschaft-rundum-v445.33.2`, unveränderter Pluginstand `445.33.1`. Zwei getrennt installierbare Seminarpakete mit jeweils acht Skills, Werkstatt-Prompt und Mini-Prompt. Die zehn Praxisfälle entsprechen den fünf Beispielen je Seminarstufe. Diese Erweiterung betrifft die Akten, nicht die Skills oder Prompts.

## 1.1. Aktenbestand

| Seminar | Fall | Originale | Davon neu | Gesamt-PDF-Seiten | Seitenzuwachs |
| --- | --- | ---: | ---: | ---: | ---: |
| Grundlagen | Begehung in Einbeck | 19 | 5 | 31 | 9 |
| Grundlagen | Baubeschreibung und LV in Detmold | 17 | 5 | 31 | 9 |
| Grundlagen | Leistungsbeschreibung und Bieterfragen in Celle | 20 | 5 | 32 | 8 |
| Grundlagen | Behinderungsanzeige in Soest | 17 | 5 | 27 | 9 |
| Grundlagen | Baugrund in Verden | 17 | 5 | 29 | 8 |
| Vertiefung | Abschlagsrechnung in Lemgo | 21 | 5 | 36 | 8 |
| Vertiefung | VgV-Bewerbung in Hameln | 21 | 5 | 36 | 9 |
| Vertiefung | Angebotsprüfung in Goslar | 21 | 5 | 35 | 9 |
| Vertiefung | Bauzeit-Claim in Minden | 21 | 5 | 33 | 8 |
| Vertiefung | Nachtrag in Northeim | 21 | 5 | 35 | 9 |

195 eigenständige Originalunterlagen, zehn Gesamt-PDFs mit zusammen 325 Seiten sowie je zehn flache Originalformat- und Einzel-PDF-ZIPs. Das sind 50 Originale und 86 Gesamt-PDF-Seiten mehr als im vorherigen Teilrelease. Die bisherigen 145 Originaldateien bleiben bytegleich erhalten. E-Mails enthalten tatsächliche, bytegleiche Anlagen. Word-Dateien, PDF-Unterlagen, bearbeitbare Excel-Dateien, CSV-Exporte, Notizen und beschriftete Skizzen werden je Fall passend eingesetzt. Interne Bewertungsrubriken bleiben außerhalb der Archive.

## 1.2. Individuelle Ergänzungen

| Fall | Zusätzliche Unterlagen und Tatsachen |
| --- | --- |
| Einbeck | Sanitär-Servicebericht, Oberflächenablesungen, Materialausgabe mit Rücklauf, Elektro-Serviceblatt und E-Mail mit zwei tatsächlichen Anlagen. |
| Detmold | Bodenöffnungsbericht, einzelne Sockelstrecken, Lieferauskunft, Aufnahme der Türöffnung und Musterlieferungs-E-Mail mit Anlage. |
| Celle | Lieferantendaten zu Leuchten, Aufnahme der Steuerleitungen, Aufmaßzugang, Rasterablesungen und Lieferauskunft per E-Mail. |
| Soest | Rohrsteg-Montageblatt, Pumpendisposition, Polierbuch, Dispositionsereignisse und Korrespondenz zum verfügbaren Pumpenfenster. |
| Verden | Kontrollnivellement, Probenannahme, geänderte Maschinenaufstellangaben, fortgesetzte Wasserablesungen und geotechnische Korrespondenz. |
| Lemgo | Pumpeneinsatzbericht, Zwischenzählerstände, Fertigungsstand der Anschlussplatten, Sockelnacharbeit und E-Mail mit Gerätenachweisen. |
| Hameln | ARGE-Leistungsabgrenzung, gebundene Planungstermine, Rückfragen des Versicherers, Personalgespräch und E-Mail zur tatsächlichen Verfügbarkeit. |
| Goslar | Elementabmessungen, Zugriffsjournal, Kapazitätsvorbehalt des Nachunternehmers, Bietererklärung zum Preisblatt und zugehörige Korrespondenz. |
| Minden | Kranmietrechnung, Gerätestunden, abgesagter Betonabruf, Kolonnenfreigabe und E-Mail zum Unterschied zwischen prognostizierten und gebuchten Stunden. |
| Northeim | Rohrlageraufnahme, Lagerexport, bedingte Rücknahmeauskunft, tatsächlicher Kolonneneinsatz und E-Mail zur Lieferbindung. |

## 1.3. Durchgeführte Prüfungen

Beide Pluginpakete wurden redaktionell gegengelesen. Die Quellenkarten dokumentieren die gezielt geprüften Normen und Entscheidungspassagen. Fachliche Ergebnistests sind spezifiziert; es wurden keine erfolgreichen Modellläufe in fremden Oberflächen behauptet.

Die Originalbuilder prüfen Tabellen, E-Mail-Anhänge und fallbezogene Zahlenbeziehungen. In den Fortgeschrittenenakten wurden 79 Formeln und deren Cachewerte kontrolliert. Ein erkannter Exportfehler bei Positionsnummern ist korrigiert: `01.010` bleibt eine Zeichenfolge und wird nicht zur Zahl `1.01`. Ein unabhängiger Regressionstest vergleicht zusätzlich die Rechnungszahlungen mit dem Kreditorenexport.

Native Dokumente, Tabellen und Skizzen wurden gerendert und visuell geprüft. Der Paketbau vergleicht Originaldateien bytegenau, prüft den vollständigen Einzel-PDF-Bestand, flache Archivpfade und die zweisprachigen Herkunftshinweise. Die Gesamt-PDFs selbst enthalten diese Hinweise nicht; sie stehen auf den Downloadseiten.

Die Erweiterung wurde anhand der bestehenden Projektangaben gegengelesen. Gesonderte Zahlenprüfungen betreffen unter anderem Sockellängen, Wasserhöhen, Lagerbestände, Gerätestunden und bedingte Rücknahmewerte. Neun zentrale Regressionstests prüfen zusätzlich die Aktenverzeichnisse, den Zuwachs je Fall und die Übernahme vollständiger Originalabsätze in die Gesamt-PDFs. Bewusst unterschiedliche Angaben von Beteiligten bleiben als solche erhalten; die Akten liefern keine abschließende Bewertung.

Ein zusätzlicher Abgleich der fertigen Einzel-PDF-ZIPs prüft alle 195 PDF-Dateien und 444 Textabschnitte aus ihren Originalen. Ein Vergleich mit dem vorherigen Git-Stand bestätigt außerdem die Bytegleichheit der 145 Bestandsoriginale. Die Dokumentqualitätsprüfung und die Prüfungen für CSV-Struktur, Downloadverweise, Navigation sowie beide Plugin- und Marketplace-Validatoren sind bestanden.

## 1.4. Reproduktion

Die Quelldaten stehen in `scripts/bau_rundum_basis_daten.py` und `scripts/bau_rundum_vertiefung_daten.py`. Die zugehörigen Originalbuilder erzeugen nur die zehn zugewiesenen Akten. `scripts/package-bauwirtschaft-rundum.py` baut anschließend beide Plugin-ZIPs, vier separate Markdown-Prompts und die drei Ausgabeformen jeder Akte. `pakete.json` enthält die tatsächlichen Bestandszahlen und SHA-256-Werte.

Mit `--new-only` ergänzen die Originalbuilder ausschließlich fehlende Dateien und prüfen den unveränderten Altbestand. Änderungen am Text einer bereits vorhandenen Originaldatei erfordern weiterhin einen vollständigen oder gezielten Neubau; `--new-only` ist kein Aktualisierungsmodus für solche Dateien.

Die gezielten Prüfungen stehen in `scripts/test-bauwirtschaft-rundum.py`. Zusätzlich gelten die unveränderten zentralen Prüfungen für Pluginstruktur, Marketplace-Import, YAML-Frontmatter, Dokumentqualität, Navigation und Qualitätsprofile. Der automatisierte Seminarcheck läuft für Änderungen an den neuen Paketen und Akten.

Dieses Teilrelease enthält keine neu gebauten Sammelarchive des gesamten Repositorys. Die neuen Einzelpakete sind über ihre ausdrücklich zugeordneten Release-Adressen erreichbar.
