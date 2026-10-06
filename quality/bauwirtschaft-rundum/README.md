# 1. Bauwirtschaft rundum: Liefer- und Prüfstand

Teilrelease `bauwirtschaft-rundum-v445.33.1`, Pluginstand `445.33.1`. Zwei getrennt installierbare Seminarpakete mit jeweils acht Skills, Werkstatt-Prompt und Mini-Prompt. Die zehn Praxisfälle entsprechen den fünf Beispielen je Seminarstufe. Vorhandene Fachpakete bleiben erhalten.

## 1.1. Aktenbestand

| Seminar | Fall | Originale | Gesamt-PDF-Seiten |
| --- | --- | ---: | ---: |
| Grundlagen | Begehung in Einbeck | 14 | 22 |
| Grundlagen | Baubeschreibung und LV in Detmold | 12 | 22 |
| Grundlagen | Leistungsbeschreibung und Bieterfragen in Celle | 15 | 24 |
| Grundlagen | Behinderungsanzeige in Soest | 12 | 18 |
| Grundlagen | Baugrund in Verden | 12 | 21 |
| Vertiefung | Abschlagsrechnung in Lemgo | 16 | 28 |
| Vertiefung | VgV-Bewerbung in Hameln | 16 | 27 |
| Vertiefung | Angebotsprüfung in Goslar | 16 | 26 |
| Vertiefung | Bauzeit-Claim in Minden | 16 | 25 |
| Vertiefung | Nachtrag in Northeim | 16 | 26 |

145 eigenständige Originalunterlagen, zehn Gesamt-PDFs mit zusammen 239 Seiten sowie je zehn flache Originalformat- und Einzel-PDF-ZIPs. E-Mails enthalten tatsächliche, bytegleiche Anlagen. Word-Dateien, PDF-Unterlagen, bearbeitbare Excel-Dateien, CSV-Exporte, Notizen und beschriftete Skizzen werden je Fall passend eingesetzt. Interne Bewertungsrubriken bleiben außerhalb der Archive.

## 1.2. Durchgeführte Prüfungen

Beide Pluginpakete wurden redaktionell gegengelesen. Die Quellenkarten dokumentieren die gezielt geprüften Normen und Entscheidungspassagen. Fachliche Ergebnistests sind spezifiziert; es wurden keine erfolgreichen Modellläufe in fremden Oberflächen behauptet.

Die Originalbuilder prüfen Tabellen, E-Mail-Anhänge und fallbezogene Zahlenbeziehungen. In den Fortgeschrittenenakten wurden 79 Formeln und deren Cachewerte kontrolliert. Ein erkannter Exportfehler bei Positionsnummern ist korrigiert: `01.010` bleibt eine Zeichenfolge und wird nicht zur Zahl `1.01`. Ein unabhängiger Regressionstest vergleicht zusätzlich die Rechnungszahlungen mit dem Kreditorenexport.

Native Dokumente, Tabellen und Skizzen wurden gerendert und visuell geprüft. Der Paketbau vergleicht Originaldateien bytegenau, prüft den vollständigen Einzel-PDF-Bestand, flache Archivpfade und die zweisprachigen Herkunftshinweise. Die Gesamt-PDFs selbst enthalten diese Hinweise nicht; sie stehen auf den Downloadseiten.

## 1.3. Reproduktion

Die Quelldaten stehen in `scripts/bau_rundum_basis_daten.py` und `scripts/bau_rundum_vertiefung_daten.py`. Die zugehörigen Originalbuilder erzeugen nur die zehn zugewiesenen Akten. `scripts/package-bauwirtschaft-rundum.py` baut anschließend beide Plugin-ZIPs, vier separate Markdown-Prompts und die drei Ausgabeformen jeder Akte. `pakete.json` enthält die tatsächlichen Bestandszahlen und SHA-256-Werte.

Die gezielten Prüfungen stehen in `scripts/test-bauwirtschaft-rundum.py`. Zusätzlich gelten die unveränderten zentralen Prüfungen für Pluginstruktur, Marketplace-Import, YAML-Frontmatter, Dokumentqualität, Navigation und Qualitätsprofile. Der automatisierte Seminarcheck läuft für Änderungen an den neuen Paketen und Akten.

Dieses Teilrelease enthält keine neu gebauten Sammelarchive des gesamten Repositorys. Die neuen Einzelpakete sind über ihre ausdrücklich zugeordneten Release-Adressen erreichbar.
