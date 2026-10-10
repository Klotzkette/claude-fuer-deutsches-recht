# Prüfbericht DD – Due Diligence 1.0.1

Dieser Bericht dokumentiert den Aufbau und die Prüfung des Plugins, der drei Prompts und der drei Testakten. Er trennt technische Bestandstests, redaktionelle Fachprüfung und die noch offene Bewertung späterer KI-Ergebnisse. Prüfdatum: 10.10.2026.

## 1. Umfang und Ablauf

Zehn Fachskills und ein koordinierender Hauptskill führen von Auftrag und Datenraum über Gesellschaft, Personal, Bilanz, Verträge und Kreditportfolio bis zu Rückfragen, Kaufpreisfolgen, Vertragsentwurf und Vollzugsbedingungen. Käufer, Investor und Verkäufer werden als unterschiedliche Auftragsperspektiven behandelt. Ein schneller Befund wird nicht als Vollprüfung ausgegeben.

Der Werkstatt-Prompt umfasst 25 Kapitel mit konkreten Rückfragen, Rechen- und Quellenkontrollen sowie vollständig ausformulierten Textbeispielen. Mini- und Hauptproblem-Prompt bleiben jeweils unter 7.500 UTF-8-Bytes. Ihre MD-/TXT-Fassungen sind byteidentisch. Die jeweiligen Hashes stehen im [Prüfprofil](../evals/due-diligence.json).

## 2. Quellen und fachliche Reichweite

Die tatsächlich gelesenen amtlichen Quellen, Entscheidungsrandnummern, Anwendung und Grenzen sind im [Rechtsquellenregister](../../due-diligence/references/rechtsquellen.md) dokumentiert. Verifiziert wurden insbesondere Datenraum-Offenlegung, Betriebsübergang und Arbeitnehmerzuordnung, Forderungsübertragung, Verbraucherdarlehen, Insolvenzvollstreckung sowie die deutsche Zweigstelle der englischen Bank und das Kreditzweitmarktgesetz.

Die Rechtsprechungsanker sind BGH, Urteil vom 15.09.2023 – V ZR 77/22, BAG, Urteil vom 21.03.2024 – 2 AZR 79/23, und der ausdrücklich historische Anker BGH, Teilversäumnisurteil und Schlussurteil vom 19.01.2016 – XI ZR 103/15. Jeder Anker enthält „Trägt“ und „Trägt nicht“. Ein beliebiges Aktenzeichen aus 2026 wird nicht als Ersatz für einschlägige Rechtsprechung ergänzt. Historische Verträge erfordern die damals maßgebliche Normfassung.

Weitere Steuer-, Aufsichts-, Datenschutz- und Spezialfragen sind konkrete Rechercheaufträge, keine pauschal als vollständig geprüft behaupteten Fachgebiete. Die Aktenunterlagen sind fiktiver Sachverhalt und keine verifizierte Rechtsquelle.

## 3. Spiegelung der beiden bestehenden Akten

Das [SHA-256-Protokoll](spiegelung.json) belegt 166 unverändert gespiegelte Originaldateien: 110 aus der Berliner Arbeitsvertragsakte und 56 aus Silberfalke. Der bestehende zentrale Exportfilter gibt davon 110 beziehungsweise 55 Arbeitsdateien aus; die ausgeschlossene historische MAR-Prüffassung ist im Spiegelungsprotokoll ausdrücklich ausgewiesen. Der Filter wurde nicht geändert.

Die Originalakten wurden weder gelöscht noch verändert. Historische Datierungen bleiben erhalten. Silberfalke enthält bereits frühere DD-Bewertungen und Erwartungskarten. Die Akte ist deshalb eine Lern- und Überarbeitungsakte, kein blinder Leistungstest. Jede neue Bearbeitung muss Befunde aus Originalbelegen rekonstruieren und eigene Ergebnisse getrennt speichern.

## 4. Bankfiliale Erfurt

Die neue Akte enthält 95 Arbeitsoriginale: 23 Word-Dateien, 45 PDFs, 26 E-Mails und eine Excel-Arbeitsmappe. Zwanzig Darlehensverträge sind mit Kontojournal, Brief und E-Mail einzeln ausgebaut. Fünf E-Mails tragen echte PDF-Anhänge. Die Excel-Datei enthält 1.000 eindeutig bezeichnete Forderungen und 240 Monatsbuchungen zu den 20 Detailakten.

Die 20 Detailfälle wurden gezielt problemorientiert ausgewählt; die übrigen 980 Einträge sind knappe Verkäuferdaten. Eine statistische Hochrechnung ist nicht zulässig. Buchungssaldo, Buchwert, Preisannahme und rechtlich durchsetzbare Forderung werden getrennt. Insolvenz, bestrittene Kosten, Zahlungszuordnung, Kündigung, Identitäts- und Adresskonflikte sowie fehlende Urkunden bleiben als konkrete Prüfgegenstände sichtbar.

Die Fallgeneratoren und das deterministische Datenmodell liegen unter `scripts/build-dd-bankakte.py`, `scripts/build-dd-bankakte-excel.mjs` und `scripts/data/dd-bankakte.json`. Die Prüfung stimmt die Salden centgenau ab, einschließlich der gesonderten Buchwertbrücke. Sie bestätigt keine rechtliche Berechtigung aller Verkäuferpositionen.

## 5. Fachprobe und spätere Ergebnistests

Die [unabhängige redaktionelle Fachprobe](fachprobe.md) prüft fünf Szenarien: Personalübernahme, historische Unternehmensakte, Bankfiliale mit 20 von 1.000 Forderungen, doppelte Kaufpreisanrechnung und Fortsetzung nach widersprüchlicher Antwort. Dabei wurden Produktkennungen, Datumsfelder, die Insolvenzprüfung und der BAG-Anker präzisiert.

Das Prüfprofil enthält fünf konkrete Ergebnisfälle mit 22 Kriterien. Die drei Rubriken enthalten Bestandsprüfungen und zusammen 21 offene fachliche Bewertungskriterien. Diese Kriterien gelten einer erst später zu erzeugenden Bearbeitung. Es wurde kein beobachteter Live-Modelllauf in Claude, Cowork, Codex oder ChatGPT durchgeführt. Importierbare Dateien und Anweisungen sind keine Garantie identischen Verhaltens dieser unterschiedlichen Clients.

## 6. Technische Prüfung und Lesefassungen

Der Komponentenbuilder erzeugt genau 21 Dateien: zwei Plugin-ZIPs, drei Prompts in jeweils MD/TXT/PDF, drei Akten in jeweils Originalformat-ZIP/Einzel-PDF-ZIP/Gesamt-PDF und eine Prüfsummenliste. Plugin-ZIPs enthalten keine personenbezogenen Testakteninhalte. Die Gesamt-PDFs werden aus genau den Einzel-PDFs aufgebaut; Seitenzahl und Textbestand werden gegeneinander geprüft.

Word-Dokumente und die Office-Unterlagen der gespiegelten Akten werden nativ mit der gebündelten Headless-LibreOffice-Laufzeit gerendert. Die breite Bankarbeitsmappe erhält eine separate Druckansicht aus ihren geprüften Zellwerten: lesbare Spaltengruppen mit wiederholter Darlehenskennung und gegebenenfalls Buchungsdatum, ohne Kürzung der Zeilen oder Veränderung der XLSX. Die Desktop-Anwendung des Nutzers wird nicht verwendet. Word-Quellen verwenden Times New Roman 11 pt; eine technische Ersatzschrift der Renderumgebung wird offengelegt. Die Prompt-Lesefassungen verwenden auf diesem Rechner Times New Roman 11 pt. Die PDF-Akten enthalten keine Warnseiten; die Hinweise stehen auf den Downloadseiten und in der README.txt jedes ZIPs.

Die konkreten Excel-Nachrechnungen stehen im [Excel-Prüfprotokoll](bank-excel-pruefung.json), die nativen Einzelunterlagen im [PDF-Prüfprotokoll](bank-pdf-pruefung.json). Die [Sichtprüfung der Gesamtdateien](pdf-qa.md) hält Erstbefund und gezielte Nachkontrolle getrennt fest.

## 7. Abschlussstand der ersten Paketfassung 1.0.0

Die finale Paketprüfung `python3 scripts/test-due-diligence.py --dist /tmp/dd-release-publish` hat alle **17 Tests ohne Überspringen** bestanden. Sie prüft unter anderem elf Skills, drei Promptpaare, die unveränderte Spiegelung, 1.000 eindeutige Kreditkennungen, 240 Monatsketten, Cent-Salden, MIME-Anhänge, interne Plugin-Links, ZIP-Bestand, PDF-Inhaltsgleichheit und sämtliche Prüfsummen.

Beim Promptabgleich wurde außerdem ein Fehlalarm durch Zeilenumbrüche innerhalb langer amtlicher URLs behoben. Der Test prüft jede vollständige URL zeichengetreu ohne Umbruch-Leerraum und zählt anschließend den übrigen Textbestand; Quellenadressen dürfen nicht fehlen.

Die Bankarbeitsmappe enthält 14.633 nichtleere Zellen. Der korrigierte Druck bildet alle Zellen, sämtliche Zeilen und ihre Beträge in nachvollziehbaren Spaltengruppen ab. Tabellen verwenden 11 pt, Fußzeilen 9 pt; die Original-XLSX bleibt bytegleich. Der gefundene Kleindruckfehler ist damit behoben. Die Werkstattüberschriften bleiben beim folgenden Absatz, damit keine isolierte Unterüberschrift am Seitenende steht.

| Lesefassung | Seiten |
| --- | ---: |
| `dd-arbeitsvertraege-innovation-berlin_gesamt.pdf` | 296 |
| `dd-bankfiliale-verbraucherdarlehen-erfurt_gesamt.pdf` | 349 |
| `dd-corporate-silberfalke_gesamt.pdf` | 197 |
| `due-diligence-hauptproblem.pdf` | 3 |
| `due-diligence-schnellstart.pdf` | 2 |
| `due-diligence-werkstatt.pdf` | 15 |

Sämtliche Textspans der sechs finalen PDF-Dateien liegen innerhalb der MediaBox; die Prüfung fand weder das Ersatzzeichen U+FFFD noch U+25A0. Die [Hashes und Einzelbefunde](lesefassungen.json) begrenzen den tatsächlich geprüften Stand. Repräsentative Seiten wurden visuell angesehen. Eine kosmetische leere Schlussseite der historischen Silberfalke-Kaufvertragsfassung wurde als übernommenes Umbruchartefakt dokumentiert; die unveränderte Spiegelung bleibt erhalten.

Weitere abgeschlossene Prüfungen:

- `node scripts/validate-plugin-structure.mjs`: bestanden.
- `node scripts/validate-marketplace-import.mjs`: 299 Plugins, 23.270 Skills, bestanden.
- `python3 scripts/validate-yaml-frontmatter.py`: keine Fehler oder Warnungen.
- `python3 scripts/audit-skill-activation.py`: bestanden.
- `python3 scripts/quality-lab.py audit --require-editorial --require-workflow`: 299 vollständige Profile; keine Behauptung eines Modell-Passes.
- `python3 scripts/validate-root-readme-overview.py`: Bestandszahlen und Register konsistent.
- `python3 scripts/validate-markdown-structure.py`: bestanden.
- `python3 scripts/validate-testakten-readme-downloads.py`: Downloadhinweise und Verknüpfungen bestanden.
- `python3 scripts/test-scoped-release-routing.py`: elf Tests bestanden; [öffentlicher Downloadnachweis](download-routing.json) für verschobene Altakten.
- `python3 scripts/build-due-diligence-release.py --dist /tmp/dd-release-publish`: 21 Dateien erzeugt.
- `git diff --check`: bestanden.

Die erste Komponentenfassung `due-diligence-v1.0.0` wurde veröffentlicht und alle 21 hochgeladenen Dateien durch erneuten Download bytegenau geprüft. Das bestehende Gesamtrelease und seine Sammelarchive blieben unverändert. Die danach abgeschlossene strenge Herstellerprüfung fand den in Abschnitt 8 beschriebenen Importfehler.

## 8. Importkorrektur 1.0.1

Die GitHub-Herstellerprüfung der ersten Fassung meldete fehlendes YAML-Frontmatter in den vier DD-Startbefehlen. Version 1.0.1 ergänzt jeweils eine Beschreibung, einen Argumenthinweis und die ausdrückliche Verarbeitung von `$ARGUMENTS`. Der Regressionstest scheitert an den vier alten Befehlen und besteht mit den korrigierten Dateien. Die übrigen Skills und fachlichen Prompttexte bleiben unverändert.

Am 10.10.2026 wurden folgende Prüfungen ausgeführt:

- `claude plugin validate due-diligence --strict`: bestanden, keine Warnung.
- `python3 scripts/build-due-diligence-release.py --dist /tmp/dd-release-101`: 21 Dateien erzeugt.
- `python3 scripts/test-due-diligence.py --dist /tmp/dd-release-101`: alle 18 Tests bestanden, kein Test übersprungen.
- Struktur-, Marketplace-, Qualitätsprofil-, Markdown-, Übersichts- und Downloadrouting-Prüfungen: bestanden.

Die drei Gesamt-PDFs sind byteidentisch mit der Fassung 1.0.0. Die Prompt-PDFs tragen die neue Versionsfußzeile; Seitenzahlen und Textbestand sind unverändert. Die neu berechneten Hashes stehen in `lesefassungen.json`; sämtliche Textspans bleiben innerhalb der Seiten, ohne die geprüften Ersatzzeichen. Die erste Werkstattseite einschließlich neuer Fußzeile wurde erneut visuell angesehen.

Aktuelle Manifeste, Marktverzeichnis, Akten-READMEs, Downloadzuordnungen, Übersichten, Builder und Komponentenworkflow verwenden 1.0.1. Die veröffentlichte Fassung 1.0.0 und ihr Tag werden nicht überschrieben. Die Freigabe von 1.0.1 erfolgt nach der GitHub-Kompatibilitätsprüfung und erneutem Downloadabgleich aller 21 Release-Dateien. Diese technischen Prüfungen sind kein beobachteter Live-Modelllauf.
