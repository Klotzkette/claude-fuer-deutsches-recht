# 1. Bauwirtschaft rundum: Liefer- und Prüfstand

Teilrelease `bauwirtschaft-rundum-v445.33.3`, unveränderter Pluginstand `445.33.1`. Zwei getrennt installierbare Seminarpakete mit jeweils acht Skills, Werkstatt-Prompt und Mini-Prompt. Die zehn Praxisfälle entsprechen den fünf Beispielen je Seminarstufe. Diese Erweiterung ergänzt je Akte eine individuell ausgearbeitete Excel-Arbeitsmappe; Skills und Prompts bleiben unverändert.

## 1.1. Aktenbestand

| Seminar | Fall | Originale | Neue Excel-Datenzeilen | Gesamt-PDF-Seiten | Seitenzuwachs |
| --- | --- | ---: | ---: | ---: | ---: |
| Grundlagen | Begehung in Einbeck | 20 | 60 | 38 | 7 |
| Grundlagen | Baubeschreibung und LV in Detmold | 18 | 62 | 37 | 6 |
| Grundlagen | Leistungsbeschreibung und Bieterfragen in Celle | 21 | 64 | 39 | 7 |
| Grundlagen | Behinderungsanzeige in Soest | 18 | 65 | 32 | 5 |
| Grundlagen | Baugrund in Verden | 18 | 73 | 36 | 7 |
| Vertiefung | Abschlagsrechnung in Lemgo | 22 | 64 | 41 | 5 |
| Vertiefung | VgV-Bewerbung in Hameln | 22 | 63 | 41 | 5 |
| Vertiefung | Angebotsprüfung in Goslar | 22 | 142 | 44 | 9 |
| Vertiefung | Bauzeit-Claim in Minden | 22 | 61 | 37 | 4 |
| Vertiefung | Nachtrag in Northeim | 22 | 65 | 41 | 6 |

205 eigenständige Originalunterlagen, zehn Gesamt-PDFs mit zusammen 386 Seiten sowie je zehn flache Originalformat- und Einzel-PDF-ZIPs. Das sind zehn Originale und 61 Gesamt-PDF-Seiten mehr als im vorherigen Teilrelease. Die bisherigen 195 Originaldateien bleiben bytegleich erhalten. E-Mails enthalten tatsächliche, bytegleiche Anlagen. Word-Dateien, PDF-Unterlagen, bearbeitbare Excel-Dateien, CSV-Exporte, Notizen und beschriftete Skizzen werden je Fall passend eingesetzt. Interne Bewertungsrubriken bleiben außerhalb der Archive.

## 1.2. Individuelle Ergänzungen

| Fall | Zusätzliche Unterlagen und Tatsachen |
| --- | --- |
| Einbeck | Messwerte, Materialausgabe und Zugangstermine in drei verknüpfbaren Registern mit Datums- und Belegbezug. |
| Detmold | Raumbuch, einzelne Sockelstrecken und Leistungsstände mit nachvollziehbaren Flächen- und Längenberechnungen. |
| Celle | Register aller 36 Leuchten, Anschlussdaten und Betriebsfenster als Grundlage für den Unterlagenabgleich. |
| Soest | Tagesstunden, Tagesjournal und Disposition; Zeitangaben sind echte berechenbare Tabellenwerte. |
| Verden | Schichten, Höhenbuch und Kennwerte; kleine Durchlässigkeitswerte werden wissenschaftlich und nicht gerundet als Null angezeigt. |
| Lemgo | Kumulative Leistungsstände, Zahlungsverlauf und Wasserhaltung; Positionsnummern bleiben Zeichenfolgen. |
| Hameln | Einzelne Referenzleistungen, Teamkapazität und Terminbindungen mit Zuordnung zum jeweiligen Nachweis. |
| Goslar | 98 Fensterelemente, 24 Preiszeilen und 20 Verfahrenseinträge mit prüfbaren Mengen- und Datumsbezügen. |
| Minden | Bauablauf, einzelne Kranmiettage und Tagesdisposition mit belegbezogenen Zeit- und Kostenangaben. |
| Northeim | Trassenstationen, Rohrlager und Preisregister einschließlich bedingter Rücknahmewerte. |

## 1.3. Durchgeführte Prüfungen

Beide Pluginpakete wurden redaktionell gegengelesen. Die Quellenkarten dokumentieren die gezielt geprüften Normen und Entscheidungspassagen. Fachliche Ergebnistests sind spezifiziert; es wurden keine erfolgreichen Modellläufe in fremden Oberflächen behauptet.

Die Originalbuilder prüfen Tabellen, E-Mail-Anhänge und fallbezogene Zahlenbeziehungen. Die neuen Arbeitsmappen enthalten 30 Blätter, 719 Datenzeilen und 470 Formeln innerhalb der Datentabellen. 56 unabhängige Sollwertkontrollen prüfen die Berechnungen. In jeder Mappe wurde außerdem ein Eingabewert gezielt geändert, das erwartete Folgeergebnis nach nativer Neuberechnung geprüft und der Ausgangswert wiederhergestellt. Die abschließenden Dateien enthalten berechnete Cachewerte, keine Makros und keine externen Arbeitsmappenverknüpfungen. Positionsnummern wie `01.010` bleiben Text.

Native Dokumente, Tabellen und Skizzen wurden gerendert und visuell geprüft. Der Paketbau vergleicht Originaldateien bytegenau, prüft den vollständigen Einzel-PDF-Bestand, flache Archivpfade und die zweisprachigen Herkunftshinweise. Die Gesamt-PDFs selbst enthalten diese Hinweise nicht; sie stehen auf den Downloadseiten.

Die Erweiterung wurde anhand der bestehenden Projektangaben gegengelesen. Gesonderte Zahlenprüfungen betreffen unter anderem Sockellängen, Wasserhöhen, Lagerbestände, Gerätestunden und bedingte Rücknahmewerte. Pro Mappe bleiben zwei konkret belegbare Unstimmigkeiten bewusst erhalten. Ihre Kontrollangaben stehen nur in den redaktionellen Quelldaten, nicht in Arbeitsmappen, PDF-Dateien oder Aktenarchiven. Es gibt keine ausgeblendeten Lösungsblätter. Neun bestehende und fünf zusätzliche Regressionstests prüfen unter anderem Verzeichnisse, Formeln, Zelltypen, Druckbereiche und die vollständige Übernahme der Textfelder aller neuen Tabellenzeilen in die Gesamt-PDFs.

Der Paketbau prüft den vollständigen Bestand von 205 Einzel-PDFs und die Bytegleichheit der 205 Originaldateien in den ZIPs. Ein Vergleich mit dem vorherigen Git-Stand bestätigt zusätzlich die Bytegleichheit der 195 Bestandsoriginale. Die Dokumentqualitätsprüfung und die Prüfungen für CSV-Struktur, Downloadverweise, Navigation sowie beide Plugin- und Marketplace-Validatoren bleiben Bestandteil der Abschlusskontrolle.

## 1.4. Reproduktion

Die bisherigen Quelldaten stehen in `scripts/bau_rundum_basis_daten.py` und `scripts/bau_rundum_vertiefung_daten.py`. Die neuen Arbeitsmappen sind einzeln in `scripts/bau_rundum_excel_basis.json` und `scripts/bau_rundum_excel_vertiefung.json` beschrieben. `scripts/build-bau-rundum-excel.py` erstellt sie mit Tabellenformatierung, führt eine native Neuberechnung und die Veränderungstests durch und kann sie mit `--install` in die Akten übernehmen. Benötigt werden die Tabellenlaufzeit, LibreOffice und die Python-Prüfbibliotheken; der Laufzeitpfad ist über `--runtime` konfigurierbar.

`scripts/package-bauwirtschaft-rundum.py` baut anschließend beide Plugin-ZIPs, vier separate Markdown-Prompts und die drei Ausgabeformen jeder Akte. Hinzu kommen zehn einzeln herunterladbare Arbeitsmappen und ein flaches Excel-Sammel-ZIP. `pakete.json` enthält die tatsächlichen Bestandszahlen und SHA-256-Werte der 47 Nutzdateien; die Prüfsummenliste ist die 48. Release-Datei.

Mit `--new-only` ergänzen die Originalbuilder ausschließlich fehlende Dateien und prüfen den unveränderten Altbestand. Änderungen am Text einer bereits vorhandenen Originaldatei erfordern weiterhin einen vollständigen oder gezielten Neubau; `--new-only` ist kein Aktualisierungsmodus für solche Dateien.

Die gezielten Prüfungen stehen in `scripts/test-bauwirtschaft-rundum.py` und `scripts/test-bau-rundum-excel.py`. Zusätzlich gelten die unveränderten zentralen Prüfungen für Pluginstruktur, Marketplace-Import, YAML-Frontmatter, Dokumentqualität, Navigation und Qualitätsprofile. Der automatisierte Seminarcheck führt beide Fallprüfungen für Änderungen an den neuen Paketen und Akten aus.

Dieses Teilrelease enthält keine neu gebauten Sammelarchive des gesamten Repositorys. Die neuen Einzelpakete sind über ihre ausdrücklich zugeordneten Release-Adressen erreichbar.
