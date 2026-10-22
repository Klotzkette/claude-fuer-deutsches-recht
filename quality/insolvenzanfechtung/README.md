# 1. Prüfung des Plugins Insolvenzanfechtung

Dieses Verzeichnis dokumentiert die fachliche Quellenarbeit, die Gegenlesen, eine begrenzte Modell-Anwendungsprobe und die technischen Prüfungen für Insolvenzanfechtung 1.1.0 sowie die Anfechtungsergänzung beim Fachanwalt für Insolvenz- und Sanierungsrecht 445.35.4. Prüfstand ist der 22.10.2026.

## 2. Fachlicher Umfang

Elf Skills mit getrennten Aufgaben, drei eigenständige Prompts und zwei zusätzliche Fachanwalts-Prompts wurden geprüft. Die Werkstatt umfasst nach der Builder-Zählung 8.654 Wörter und ergibt im finalen Paket 21 PDF-Seiten in Times New Roman 11 pt. Schnellstart und Hauptproblem ergeben zwei beziehungsweise drei Seiten. Schnellstart und Hauptproblem bleiben jeweils unter 7.500 UTF-8-Bytes einschließlich CRLF. Markdown- und Textfassungen sind byteidentisch; beide Fachanwalts-Prompts stimmen mit ihren eigenständigen Anfechtungsfassungen überein.

Das Prüfprofil enthält 14 amtliche Quellenanker. Die [Quellenprüfung vom 21.10.2026](quellenpruefung-2026-10-21.md) dokumentiert die allgemeinen Anfechtungsanker, die geprüften Normtexte und konkrete Aussagegrenzen. Die [Ergänzung zu Gesellschafterdarlehen und Abtretung](quellenpruefung-2026-10-22-gesellschafterdarlehen.md) grenzt insbesondere die typisierte Jahresfrist, die zeitliche Grenze bei einem Forderungsverkauf und die Anforderungen an eine wirtschaftliche Zurechnung ab. Der vollständige aktuelle konsolidierte EuInsVO-Stand und fallbezogenes österreichisches Recht bleiben ausdrücklich offen.

Die [Gegenlese vom 21.10.2026](gegenlese-2026-10-21.md) hat insbesondere Gläubigerwechsel und Schuldnerwechsel im Bremer Fall getrennt, tatsächliches Erkennen nach § 142 InsO präzisiert und Rechtshängigkeit vom bloßen Einreichen einer Klage abgegrenzt. Die [Gegenlese zu § 135 InsO vom 22.10.2026](gegenlese-2026-10-22-135.md) dokumentiert die beiden Kölner Fälle und die nach der Gegenprüfung umgesetzten Korrekturen. Die Dokumente enthalten keinen Automatismus von Krise, Ratenplan, Drittzahlung oder persönlicher Verbindung zu einer erfolgreichen Anfechtung.

## 3. Testakten und Formate

| Akte | Originale | Gesamt-PDF | Prüfung |
| --- | ---: | ---: | --- |
| Weserfunken Bremen | 62 | 242 Seiten | 42 Bestandsdateien unverändert; 20 Ergänzungen, echte Anhänge und Tabellenrechnung |
| Blechliebe Bamberg | 24 | 24 Seiten | Raten und Vorkasse, Abtretung, Korrespondenz und Belege |
| Faltenwurf Fürth | 24 | 24 Seiten | Darlehen, Banklinie, Bürgschaft und getrennte Auslagen |
| VeedelWende Direktrückzahlung Köln | 24 | 27 Seiten | 150.000,00 EUR Gesellschafterdarlehen, 25-Prozent-Beteiligung und Rückzahlung vier Monate vor dem Antrag |
| VeedelWende Zession Köln | 24 | 29 Seiten | Forderungsverkauf 18 Monate vor dem Antrag, Zahlung an den Erwerber und offene Zurechnungsfrage |

Die vier mit dem Anfechtungsakten-Builder erzeugten Fälle umfassen zusammen 96 Originale und 104 PDF-Seiten. Zu jedem Fall werden ein Originalformat-ZIP und ein Einzel-PDF-ZIP gebaut, insgesamt acht ZIPs. Weserfunken wird über den eingeführten Bestands- und Ergänzungsweg gesondert geprüft. Alle fünf Akten werden im Komponentenrelease zusätzlich jeweils als Gesamt-PDF bereitgestellt.

Die Akten liegen ausschließlich in ihren zentralen Fallordnern. Beide ZIP-Varianten enthalten den unveränderten zweisprachigen Hinweis in `README.txt`; die PDFs enthalten keine Warnseite. Die vier vollständig generierten Akten-ZIPs sind flach und enthalten keine Markdown-Dateien. Weserfunken behält seine eingeführten Unterordner und die getrennte Verteidigerfassung.

Die Bremer Bestands- und Ergänzungstests sowie der [Bericht zu den vier generierten Akten](akten/README.md) dokumentieren Rechen-, MIME-, Layout- und Bestandskontrollen. Word-Dokumente, Excel-Lesefassungen und PDF-Belege wurden in den Gesamtakten geprüft. Die beiden abschließenden End-to-End-Builds lieferten byteidentische Release-Dateien.

## 4. Tatsächliche Anwendungsprobe

Die [erste anwaltliche Antwort für Raban](anwendungsprobe/blechliebe-erste-antwort.md) entstand durch einen tatsächlichen Modelllauf mit dem Mini-Prompt und den Originalunterlagen. Sie trennt die verlangten 34.140 EUR in 27.000 EUR Altzahlungen und 7.140 EUR Neulieferung, benennt das Datumsproblem der Märzrate und behandelt die vorgezogene Junizahlung gesondert. Die Probe enthält eine interne Notiz und ist nicht versandt worden.

Das ist ein enger Durchlauf innerhalb dieser Bearbeitungsumgebung mit Selbstprüfung anhand fachlicher Kriterien. Es ist kein unabhängiger Richtermodelltest und kein Live-Nachweis für Claude Cowork, Claude Code oder ChatGPT. Die übrigen Ergebnisfälle im Prüfprofil sind definierte Prüfaufträge; nur die hier bezeichnete Probe wurde tatsächlich als Modelllauf durchgeführt.

## 5. Technische Prüfungen

Die folgenden Prüfungen gehören zum abschließenden Stand:

- `python3 scripts/test-insolvenzanfechtung.py` umfasst neun Tests. Ohne `--dist` wird die distributionsabhängige bytegenaue Paketprüfung planmäßig übersprungen; der vollständige Releasebuild prüft sie gegen den gebauten Zielordner.
- `python3 scripts/test-fintech-bremen.py --assets <Aktenordner>` prüft die Bremer Bestands- und Ergänzungsassets; `python3 scripts/test-fintech-bremen-anfechtung-ergaenzung.py` prüft die Anfechtungserweiterung.
- `python3 scripts/build-insolvenzanfechtung-akten.py --package-only --dist <Aktenordner>` baut die vier vollständig generierten Akten mit 96 Originalen, 104 PDF-Seiten und acht ZIPs.
- `node scripts/validate-plugin-structure.mjs`, `node scripts/validate-marketplace-import.mjs`, `python3 scripts/validate-yaml-frontmatter.py` und `python3 scripts/audit-skill-activation.py` prüfen Struktur, Manifeste und Aktivierung.
- `python3 scripts/validate-markdown-structure.py`, `python3 scripts/validate-root-readme-overview.py`, `python3 scripts/validate-testakten-readme-downloads.py` und `python3 scripts/validate-runtime-performance.py` prüfen die zentralen Übersichten, Downloadgruppen und Laufzeitgrenzen.
- `python3 scripts/test-readme-navigation.py`, `python3 scripts/validate-readme-navigation.py`, `python3 scripts/test-quickstart-usability.py`, `python3 scripts/audit-quickstart-usability.py`, `python3 scripts/test-portable-starts.py`, `python3 scripts/test-prompt-openings.py` und `python3 scripts/test-prompt-routing-scope.py` prüfen Navigation und Prompteinstiege.
- `python3 scripts/quality_lab.py audit --require-editorial --require-workflow` und `git diff --check` schließen die redaktionelle und technische Kontrolle ab.

Der [Paketabgleich](paketpruefung.json) hält Quell- und Datei-Hashes, die bestätigten PDF-Seitenzahlen, Zeichengrenzen und den vollständigen Wortbestand fest. Die 36 Release-Dateien bestehen aus vier installierbaren Plugin-ZIPs, 15 Promptdateien, 15 Aktenassets und zwei Prüfdateien; `checksums-sha256.txt` enthält 35 Prüfsummenzeilen für alle übrigen Assets. Das [Versionsrouting](release-pakete.json) weist die Fachanwaltskomponente 445.35.4 innerhalb des Komponentenreleases 1.1.0 ausdrücklich nach.

Linux-Builds verwenden Liberation Serif als dokumentierte Ersatzschrift, wenn Times New Roman fehlt. Eine technische Grünmeldung ersetzt keine fallbezogene rechtliche Endprüfung. Der zusätzliche GitHub-Workflow führt Quellen-, Übersichts-, Paket- und Aktenprüfungen auf dem tatsächlichen PR-Stand aus; die Veröffentlichung wird erst nach diesen Prüfungen abgeschlossen.
