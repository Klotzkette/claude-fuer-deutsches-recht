# Nachprüfung des Release-Builds

## 1. Erster GitHub-Lauf

PR #458 wurde am 30. September 2026 nach den dokumentierten lokalen Prüfungen auf `main` gemergt. Der Release-Lauf `36688262226` für `v445.16.0` wurde vor dem PDF- und ZIP-Build gestoppt: Drei Assertions in `scripts/test-release-routing.py` setzten noch vier tatsächlich konfigurierte Begleitakten beziehungsweise acht Archive voraus. Die inzwischen erweiterte Konfiguration enthält elf Akten beziehungsweise 22 Archive.

Die lokalen ersten Prüfungen fanden vor der abschließenden Erweiterung der Release-Zuordnung statt. Die vorgeschriebenen Prüfungen vor dem Push erfassen diese konkrete Testdatei nicht. Deshalb wurde der Fehler durch den Release-Lauf entdeckt; die früheren erfolgreichen Läufe sind kein Nachweis für diese zuletzt geänderte Zuordnung.

## 2. Korrektur

Die reale Release-Zuordnung und die synthetischen Grenzfälle erhalten getrennte Testdaten. Die Sollprüfung der tatsächlich vorgesehenen elf Akten bleibt bestehen. Die Grenzfälle prüfen mit einer festen Vierakten-Konfiguration weiterhin unter anderem die Aufteilung von 1.003 Ausgangsassets in 995 Haupt- und neun Begleitassets sowie die GitHub-Grenze von 1.000 Dateien. Native Akten, Skills und die beiden Prompts werden durch diese Korrektur nicht geändert.

Der bereits gesetzte Tag `v445.16.0` bleibt unverändert. Die korrigierte Veröffentlichung verwendet `v445.16.1` einschließlich der dazugehörigen Begleit-Release-Verweise.

## 3. Gezielte Nachprüfung

Die korrigierte Routing-Suite besteht mit 30 Tests. Die getrennte Release-Asset-Suite, der Abgleich der zentralen Übersichten und die Validierung sämtlicher Testakten-Downloadverweise bestehen ebenfalls. Der unabhängige Diff-Review der Testkorrektur ergab keinen Befund. Eine verbliebene sichtbare Versionsangabe im Startup-Gründer-README wurde aktualisiert; der danach erneut ausgeführte Marketplace-Importcheck besteht.

## 4. Öffentlicher Download und Sichtprüfung von v445.16.1

Der vollständige Release-Lauf `36689390745` endete erfolgreich. Hauptrelease `v445.16.1` und Begleitrelease `akten-v445.16.1` sind veröffentlicht. Der tatsächliche öffentliche Downloadabgleich prüfte das Plugin-ZIP, zwölf Aktenarchive, beide Prüfsummenlisten und beide Pages-Prompts. Die 175 nativen Originale waren bytegleich zum Repository und zum Qualitätsmanifest. Das Plugin enthielt genau zehn Skills. Die getrennten Promptdateien stimmten mit ihren Repositoryfassungen überein.

Die öffentlichen Gesamt-PDFs haben zusammen 293 Seiten; die damals lokal erzeugten Fassungen 296. Je eine Seite Unterschied entsteht beim Druck der Excel-Mappen aus Musik-, Programmierer- und Syndikusakte. Diese Unterschiede wurden durch Textvergleich und gezielte Sichtprüfung der betreffenden Druckseiten nachvollzogen. Es wird keine Byte- oder Pixelgleichheit der abgeleiteten Office-PDFs behauptet.

Alle 293 öffentlichen Gesamtseiten wurden auf Kontaktbögen tatsächlich angesehen; gezielte Inhaltsseiten zusätzlich in voller Renderauflösung. Dabei fiel in der Berliner Anteilsübersicht ein Zusammenstoß der Tabellenköpfe auf. Die beiden GmbH-Vergütungstabellen und die Erfurter Anteilsübersicht hatten außerdem knappe Zahlen-/Textabstände. Im Programmierer-Rechnungsabgleich war „Leistungsmonat“ ungünstig umbrochen. Zahlen und Textinhalte blieben nachvollziehbar, die Darstellung war aber verbesserungsbedürftig. Diese Befunde werden nicht rückwirkend aus der Prüfung entfernt.

## 5. Gezielte Darstellungsänderung für v445.16.2

Fünf Excel-Originale und ihre beiden Builder erhalten besser getrennte Tabellenköpfe und Zahlen-/Textspalten. Anteilswerte, Gehälter, Rechnungen und Rechenformeln bleiben unverändert; der semantische Vorher/Nachher-Abgleich dokumentiert die wenigen geänderten Kopftexte gesondert. Musik-, Syndikus- und Organe-Originale sowie die fachlichen Produktanweisungen bleiben unverändert. Die drei betroffenen Gesamt-PDFs und die zugehörigen Archive werden aus dem korrigierten Stand neu gebaut. Die frühere Veröffentlichung bleibt bestehen.

Die Modellproben bezeichnen weiterhin ihre jeweils archivierten Eingabestände. Eine Formatänderung wird nicht als neue Modellprobe ausgegeben. Native Druckprüfung, Werte-/Formelabgleich und nachfolgende technische Prüfungen stehen in den gesonderten Nachweisen dieser Revision. Die öffentliche Nachkontrolle von v445.16.2 erfolgt erst nach dessen tatsächlicher Veröffentlichung.
