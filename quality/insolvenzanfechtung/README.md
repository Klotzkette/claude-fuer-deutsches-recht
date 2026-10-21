# 1. Prüfung des Plugins Insolvenzanfechtung

Prüfstand: 21.10.2026. Das Verzeichnis dokumentiert die fachliche Quellenarbeit, die Gegenlese, eine begrenzte Modell-Anwendungsprobe und die technischen Prüfungen für Insolvenzanfechtung 1.0.0 sowie die Anfechtungsergänzung beim Fachanwalt für Insolvenz- und Sanierungsrecht 445.35.4.

## 2. Fachlicher Umfang

Elf Skills mit getrennten Aufgaben, drei eigenständige Prompts und zwei zusätzliche Fachanwalts-Prompts wurden geprüft. Die Werkstatt enthält 8.379 Wörter und ergibt lokal 20 PDF-Seiten in Times New Roman 11 pt. Der Mini-Prompt ergibt zwei Seiten; Mini und Hauptproblem bleiben jeweils unter 7.500 UTF-8-Bytes einschließlich CRLF. Markdown- und Textfassungen sind byteidentisch; beide Fachanwalts-Prompts stimmen mit ihren eigenständigen Anfechtungsfassungen überein.

[Quellenprüfung](quellenpruefung-2026-10-21.md) dokumentiert elf tragende amtlich gelesene Entscheidungsanker einschließlich 2025 und 2026, die geprüften Normtexte und konkrete Aussagegrenzen. Der bisher zu weit gefasste Anker IX ZR 114/23 wurde im Anfechtungsskill ersetzt. Der vollständige aktuelle konsolidierte EuInsVO-Stand und fallbezogenes österreichisches Recht bleiben ausdrücklich offen.

Die [Gegenlese](gegenlese-2026-10-21.md) hat insbesondere Gläubigerwechsel und Schuldnerwechsel im Bremer Fall getrennt, tatsächliches Erkennen nach § 142 InsO präzisiert und Rechtshängigkeit vom bloßen Einreichen einer Klage abgegrenzt. Die Dokumente enthalten keinen Automatismus von Krise, Ratenplan oder Drittzahlung zu einer erfolgreichen Anfechtung.

## 3. Testakten und Formate

| Akte | Originale | Gesamt-PDF | Prüfung |
| --- | ---: | ---: | --- |
| Weserfunken Bremen | 62 | 242 Seiten | 42 Bestandsdateien unverändert; 20 Ergänzungen, echte Anhänge und Tabellenrechnung |
| Blechliebe Bamberg | 24 | 24 Seiten | Raten und neue Vorkasse, Abtretung, Korrespondenz und Belege |
| Faltenwurf Fürth | 24 | 24 Seiten | Darlehen, Banklinie, Bürgschaft und getrennte Auslagen |

Die Akten liegen ausschließlich in ihren zentralen Fallordnern. Beide ZIP-Varianten enthalten den unveränderten zweisprachigen Hinweis in README.txt; die PDFs enthalten keine Warnseite. Für die beiden neuen Akten bleiben die ZIPs flach, ohne Markdown-Dateien. Weserfunken behält seine eingeführten Unterordner und die getrennte Verteidigerfassung.

Die [Bremer Detailprüfung](../legal/fintech-bremen-anfechtung-vertiefung.md) und der [Bericht zu den beiden neuen Akten](akten/README.md) dokumentieren Rechen-, MIME-, Layout- und Bestandskontrollen. Word-Dokumente, Excel-Lesefassungen und neue PDF-Belege wurden visuell geprüft. Bei zwei Paketläufen blieben die 48 neuen Originale und die Paketbytes unverändert.

## 4. Tatsächliche Anwendungsprobe

Die [erste anwaltliche Antwort für Raban](anwendungsprobe/blechliebe-erste-antwort.md) entstand durch einen tatsächlichen Modelllauf mit dem Mini-Prompt und den Originalunterlagen. Sie trennt die verlangten 34.140 EUR in 27.000 EUR Altzahlungen und 7.140 EUR Neulieferung, benennt das Datumsproblem der Märzrate und behandelt die vorgezogene Junizahlung gesondert. Die Probe enthält eine interne Notiz und ist nicht versandt worden.

Das ist ein enger Durchlauf innerhalb dieser Bearbeitungsumgebung mit Selbstprüfung anhand fachlicher Kriterien. Es ist kein unabhängiger Richtermodelltest und kein Live-Nachweis für Claude Cowork, Claude Code oder ChatGPT. Die drei Ergebnisfälle im Prüfprofil sind definierte zukünftige Prüfaufträge; nur die hier bezeichnete Probe wurde tatsächlich durchgeführt.

## 5. Technische Prüfungen

Die folgenden Prüfungen waren am abschließenden lokalen Stand erfolgreich:

- `python3 scripts/test-insolvenzanfechtung.py --dist <Releaseordner>`: vier Prüfungen, einschließlich bytegenauer Pluginpakete, fünf vollständiger PDF-Lesefassungen, Promptgrenzen, Manifeste und Quellenprofil.
- `python3 scripts/test-fintech-bremen.py --assets <Aktenordner>`: 14 Bestandstests.
- `python3 scripts/test-fintech-bremen-anfechtung-ergaenzung.py`: fünf Erweiterungstests.
- `python3 scripts/build-insolvenzanfechtung-akten.py --package-only --dist <Aktenordner>`: zwei vollständige Wiederholungsläufe; keine Änderung der Originale.
- `node scripts/validate-plugin-structure.mjs`, `node scripts/validate-marketplace-import.mjs`, `python3 scripts/validate-yaml-frontmatter.py` und `python3 scripts/audit-skill-activation.py`.
- `python3 scripts/validate-markdown-structure.py`, `python3 scripts/validate-root-readme-overview.py`, `python3 scripts/validate-testakten-readme-downloads.py` und `python3 scripts/validate-runtime-performance.py`.
- `python3 scripts/quality_lab.py audit --require-editorial --require-workflow` und `git diff --check`.

Der [Paketabgleich](paketpruefung.json) hält Quell- und Datei-Hashes, Seitenzahlen, Zeichengrenzen und vollständigen Wortbestand fest. Die 30 Release-Dateien bestehen aus vier installierbaren ZIPs, 15 Promptdateien, neun Aktenassets und zwei Prüfdateien. Das [Versionsrouting](release-pakete.json) weist die Fachanwaltskomponente 445.35.4 innerhalb des Komponentenreleases 1.0.0 ausdrücklich nach.

Linux-Builds verwenden Liberation Serif als dokumentierte Ersatzschrift, wenn Times New Roman fehlt. Eine technische Grünmeldung ersetzt keine fallbezogene rechtliche Endprüfung. Der zusätzliche GitHub-Workflow führt Quellen-, Paket- und Aktenprüfungen auf dem tatsächlichen PR-Stand aus; die Veröffentlichung wird erst nach diesen Prüfungen abgeschlossen.
