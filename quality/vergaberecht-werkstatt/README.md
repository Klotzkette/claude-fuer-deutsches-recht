# 1. Übernahmeprüfung Vergaberecht-Werkstatt

## 1.1. Gegenstand und Herkunft

Übernommen wird die Arbeitskopie des Quellstands `b0bd885bb25dcf50a238c29be6ae43794ddc6e91`, Version 2.19.0. Das Ursprungsrepository und seine Historie bleiben unverändert. Die öffentliche Kopie liegt unter `vergaberecht-werkstatt/`, ihre Herkunft und die drei Rollen sind in `source-import.json` festgehalten. Die Lizenzen und Urheberhinweise werden nicht entfernt.

## 1.2. Prüfung auf Veröffentlichungsrisiken

Am 8. Oktober 2026 wurden die 990 versionierten Quelldateien gesondert gelesen beziehungsweise container- und metadatenbezogen geprüft. Erfasst wurden 98 DOCX-, 53 XLSX- und acht PPTX-Dateien mit zusammen 3.116 Container-Einträgen, 197 PDFs mit 567 Seiten, zehn eigenständige Bilder und 27 E-Mail-Dateien. 21 reine Bildseiten der PDFs wurden zusätzlich per lokaler Texterkennung geprüft. Es wurden keine tatsächlichen Zugangsdaten, privaten Schlüssel, Makros, aktiven PDF-Aktionen, eingebetteten ausführbaren Nutzlasten oder bestätigten privaten Mandatsdaten gefunden. Die Angaben in den Fällen waren mit den als künstlich dokumentierten Übungsakten vereinbar.

Die Prüfung ist keine Garantie für die Fehlerfreiheit jedes Inhalts. Einzelne künstliche Kontaktdaten sehen wie zustellbare Adressen aus: nicht anschreiben oder anrufen. Der ursprüngliche MIT-Hinweis enthält die bewusst veröffentlichte Kontaktangabe des Urhebers und bleibt erhalten.

## 1.3. Betriebsgrenzen

Ein manuell auslösbarer Quell-Releaseworkflow setzte einen Tag unmittelbar in Shellcode ein. Die Kopie wird auf eine Übergabe als Umgebungsvariable umgestellt. Der verschachtelte Workflow ist im Hauptrepository ohnehin inaktiv; der neue Root-Workflow prüft und veröffentlicht das Komponentenrelease. Prüfjob und Veröffentlichung haben getrennte Berechtigungen.

Das optionale Entwicklungsskript `llm-judge-eval.py` übermittelt ausdrücklich übergebene Texte an einen externen Dienst, wenn es mit passender Laufzeit und Zugangsdaten gestartet wird. Weder der Import noch die Plugin-Installation führt diesen Aufruf aus. Für diese Veröffentlichung werden keine externen Modellbewertungen ausgeführt.

## 1.4. Reproduzierbare Prüfungen

`scripts/test-vergaberecht-import.py` prüft Rollenpfade, Bestand, Promptgrenzen und Downloadziele. Mit `--dist` prüft es zusätzlich Installationsgrenzen, flache Fallaktenarchive und die vollständige Bereitstellung der auf den Komponenten-READMEs verlinkten Assets. `scripts/package-vergaberecht-werkstatt.py` ruft die Komponenten-Builder auf und erstellt erst nach den Archivprüfungen die SHA-256-Prüfsummen.

Die bestehenden Struktur-, YAML-, Navigations-, Fachstand- und Smoke-Prüfungen der Werkstatt werden weiter ausgeführt. Die drei Rollen erhalten eigene redaktionelle Evaluationsprofile im Qualitätslabor. Vorbereitete Fälle stehen ausdrücklich auf `not_run`; eine Live-Prüfung in fremden Clients wird damit nicht behauptet. Die Übernahmeprüfung ist insbesondere keine neue Vollprüfung sämtlicher Rechtsbehauptungen der Ausgangskopie.

## 1.5. Abgegrenzter Restbefund

Der zusätzliche globale Prompt-Sprachscan meldet sechs bereits vorhandene Produktnennungen in den drei Prompts der anderen Kanzlei-Komponente. Die importierten Vergaberollen verursachen nach dem redaktionellen Abgleich keine entsprechenden Meldungen. Die bestehenden Kanzleiprompts werden für diesen Kopierauftrag nicht umgeschrieben. Struktur-, Marketplace-Import- und YAML-Prüfung bestehen auch mit diesem abgegrenzten sprachlichen Restbefund; ein vollständig grüner globaler Sprachscan wird nicht behauptet.
