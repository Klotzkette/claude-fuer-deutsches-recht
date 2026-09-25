# Bearbeitung der offenen Punkte vom 25.09.2026

Die Prüfung bezieht sich auf die elf offenen Issues und vier offenen Pull Requests des Repositorys vor dieser Bearbeitung. Grundlage ist v445.3.1. Die Änderungen sind für v445.3.2 bestimmt. Sachliche Korrekturen, bereits erledigte Beiträge und reine Hinweise werden nachfolgend getrennt begründet.

## 1. Fachliche Korrekturen

| Beitrag | Ergebnis und Nachweis |
| --- | --- |
| [Issue #427](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/427) | 200 Normzeilen im Steuerberater-Plugin verweisen für Handakten nun auf Paragraf 66 StBerG. Paragraf 67 bleibt bei der Berufshaftpflichtversicherung erhalten. Beide amtlichen Normtexte wurden am 25.09.2026 geprüft; der Quellenvermerk steht im Plugin-README. |
| [Issue #415](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/415), [PR #416](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/416) | Der DeFi-Skill berücksichtigt, dass das BMF-Schreiben vom 06.03.2025 Liquidity Mining und NFT ausnimmt. Offene Tauschfragen, wirtschaftliche Zurechnung und Impermanent Loss werden bedingt geprüft. Anlage SO, Lending, Haltefrist, Meldezeitpunkt und die Abgrenzung zur Selbstanzeige sind korrigiert. Unbelegte Zuschreibungen an ein Schreiben vom 22.11.2024 sowie die fachfremden Paragraf-6a-Anker in drei Skills sind entfernt. PR #416 lieferte den Ausgangspunkt für eine Teilkorrektur und wird durch die weitergehende Fassung ersetzt. |
| [Issue #413](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/413) | Die 16 falschen Fanpage-Zuordnungen in sieben Datenschutz-Skills sind durch EuGH, Urteil vom 05.06.2018, C-210/16, ECLI:EU:C:2018:388 ersetzt. Quellen und tatsächlicher Umfang der Verifikation sind dokumentiert; C-498/16 ist die davon zu unterscheidende Schrems-Entscheidung. |
| [Issue #367](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/367) | Die Fahrgastrechte-Prüfung unterscheidet die jeweilige Anspruchsgrundlage, Artikel 60 CIV und A.9.5 BB DB von der allgemeinen BGB-Verjährung. Wirksamkeit und vorsorglicher Fristtermin werden ausdrücklich geprüft. Die Haftung bei vom Verkäufer kombinierten Fahrkarten richtet sich nach Artikel 12 Absatz 4 der Verordnung 2021/782 und der belegten Informationsausnahme. Amtliche Verordnung und DB-Bedingungen vom 24.09.2026 wurden geprüft. |
| [Issue #385](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/385) | In Urteil und Berufungsbegründung der Pohlmann-Akte endet die Berufungsfrist nach Paragraf 222 Absatz 2 ZPO am Montag, 06.09.2027. Beide DOCX und das Gesamt-PDF stimmen überein; die beiden ZIP-Varianten wurden erzeugt und geprüft. Die drei Regressionstests gleichen Zustellung, Quellen und PDF ab. Weitere materielle Unstimmigkeiten dieser Bestandsakte sind nicht Gegenstand dieses Fristenfehlers. |

## 2. Installation und Auffindbarkeit

| Beitrag | Ergebnis und Einordnung |
| --- | --- |
| [Issue #319](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/319) | Die Anleitung unterscheidet persönlichen Plugin-ZIP-Upload, Organisations-Marketplace und Claude-Code-Installation. Menübezeichnungen und Voraussetzungen wurden mit der aktuellen Anbieterdokumentation abgeglichen. Der frühere Weg über eine allgemeine Skills-Oberfläche ist kein verlässlicher Plugin-Installationsweg. |
| [Issue #369](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/369) | Struktur, Marketplace-Import und das Marketplace-Manifest bestehen die aktuellen Prüfungen. Abschnitt 8.1 der Installationshilfe beschreibt nun den konkreten Fehlertext, die Eingrenzung von Repository- und ZIP-Stand, die CLI-Prüfung und die für eine erneute Meldung nötigen Daten. Der damalige Fehler in einem fremden Benutzerkonto wurde nicht reproduziert; ein lokal gültiges Manifest ist kein Beleg für dessen erfolgreiche Installation. |
| [Issue #355](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/355) | Das Haupt-README führt zu den vorhandenen 24 Fachprofilen und erklärt den maschinenlesbaren Zugriff über Marketplace, tatsächlichen Quellpfad und Skill-Frontmatter. Die inzwischen vorhandenen Fachpakete ermöglichen die verlangte Auswahl nach Fachgebiet, ohne installierbare Pfade zu verschieben. Ein fachübergreifender Wissensgraph oder eine vollständige Zuordnung jedes ergänzenden Pakets ist damit nicht behauptet. |
| [PR #381](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/381) | Die drei vorgeschlagenen READMEs in `recherche/`, `tests/` und `uebersicht-fachanwaltschaften/` sind bereits mit ausführlicheren aktuellen Inhalten vorhanden. Der tatsächliche PR-Diff enthält entgegen dem Titel keine PDF-Linkänderung. Der Beitrag wird als überholt geschlossen. |
| [PR #317](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/317) | Das aktuelle Haupt-README enthält bereits die Prüfung der Shell-Variable und deren Grenzen. Die ursprüngliche Gleichsetzung einer leeren Variablen mit einem gesicherten direkten Anbieterzugang beziehungsweise einer gesetzten Variablen mit dem tatsächlichen GUI-Endpunkt wäre zu weitgehend. Der Beitrag wird als überholt geschlossen. |

## 3. Älterer Auditbericht

[PR #235](https://github.com/Klotzkette/claude-fuer-deutsches-recht/pull/235) wird anhand des aktuellen Bestands ausgewertet. Die geprüften früheren Description-Duplikate, unausgeglichenen Klammern, Platzhalter-Slugs, rein numerischen Slugs, gekürzten Titel und der fehlende NKR-Einstieg bestehen nicht mehr. 148 verbliebene fehlende Ziele in 88 Skill-Dateien sind auf vorhandene sachlich passende Arbeitswege umgestellt. Der Strukturvalidator prüft jetzt die 7.471 Zielverweise in 499 Fachlandkarten; kein fehlendes Ziel verbleibt. Vier Regressionstests prüfen Umbenennungen, Plugin-Grenzen, Tabellen und Dateiverweise. Der historische Bericht wird als abgearbeiteter Beitrag geschlossen; seine alten Befundzahlen werden nicht als aktueller Zustand übernommen.

## 4. Hinweise und externe Einreichung

- [Issue #298](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/298) ist entsprechend dem ausdrücklichen Schließungswunsch des Autors abgeschlossen.
- [Issue #318](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/318) ist als Mitteilung über eine bereits erfolgte Verzeichnisaufnahme zur Kenntnis genommen und abgeschlossen. Es wurde kein neues Konto eröffnet und keine externe Eigentümerverifikation vorgenommen.
- Zu [Issue #406](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/406) wurde die gewünschte einzeilige Katalogaufnahme als [PR #465 bei awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins/pull/465) eingereicht. Alphabetische Sortierung und Beitragsvalidator sind erfolgreich. Die Annahme des externen Beitrags liegt bei den dortigen Maintainern.

## 5. Prüfgrenzen

Struktur-, Import-, Quellen-, Dokument- und Regressionstests belegen jeweils ihre konkrete Prüfaufgabe. Vorbereitete Ergebnisprüffälle sind keine ausgeführten Modelltests. Die Änderungen zertifizieren weder den gesamten juristischen Altbestand noch das Verhalten sämtlicher Benutzeroberflächen. Die Quellenbelege stehen bei den betroffenen Skills und Referenzdateien. Die Release-Bereitschaftsprüfung unterscheidet nun auch bei pluralisch bezeichneten Promptdateien deren Dateigröße von einer unerlaubten Kürzung des späteren Arbeitsergebnisses; zwei bereits im Ausgangsstand auftretende Fehlmeldungen entfallen dadurch.

## 6. Ausgeführte Prüfungen

Alle 40 eindeutigen Python-Testprogramme aus dem bisherigen Release-Workflow sowie die neue Pohlmann-Regression wurden erfolgreich ausgeführt. Die unittest-basierten Programme melden zusammen 369 Tests einschließlich drei erwarteter, explizit optionaler Teiltest-Skips ohne `--assets` beziehungsweise `--render`. Die separate Fanpage-Regression besteht mit drei Tests. Die Dokumente und die korrigierten Pohlmann-Archive wurden zusätzlich visuell beziehungsweise auf Inhalt und Vollständigkeit geprüft.

Die abschließenden 19 Prüfprogramme einschließlich Import, Frontmatter, Auswahlbeschreibungen, Laufzeitbudgets, Quellen-Sperrmustern, Markdown-Struktur, Navigation und Release-Bereitschaft sind erfolgreich. Der Navigationscheck erfasst 18.152 lokale Links; der Gesamt-PDF-Validator prüft 353 zentrale Akten. Alle Textgeneratoren wurden erneut ausgeführt, ohne den vorbereiteten Git-Stand zu verändern.

Zusätzlich bestehen das Marketplace-Manifest und sämtliche 245 Plugin-Manifeste die strikte Prüfung mit der offiziellen Claude-Code-CLI 2.1.168.
