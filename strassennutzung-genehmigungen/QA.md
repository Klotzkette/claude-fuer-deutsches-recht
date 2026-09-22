# 1. Qualitätsprüfung

## 1.1. Umfang

Stand: 22.09.2026. Das Plugin enthält zehn Fachskills, zwei eigenständige Markdown-Prompts und ein lokales Quellenregister. Der Schnellstart umfasst 7444 UTF-8-Bytes, die Werkstatt 29411 Bytes. Die Prompts sind keine zusätzlichen Skills und gehören nicht in das installierbare Plugin-ZIP.

Die [Schulstraßenakte](../testakten/strassenverkehrsrecht-stvo-schulstrasse-lieferzone/README.md) enthält 26 Quelldokumente, die [Lindenhof-Akte](../testakten/strassennutzung-poller-lieferzufahrt-lindenhof-muenster/README.md) 30. Die zehn übergebenen Ausgangsdateien der Schulstraßenakte sind anhand ihrer SHA-256-Prüfsummen unverändert erhalten.

## 1.2. Ausgeführte lokale Prüfungen

Die 14 Regressionstests in `scripts/test-strassennutzung.py` prüfen Skillzahl und Auswahlsignale, Manifest, Gliederung, Promptumfang, Quellenpfade, Originalprüfsummen, Dokumentformate und Zahlenabstimmung. Die Excel-Arbeitsmappe wird zellenweise mit den drei CSV-Quellen verglichen; gespeicherte Formelwerte, Druckformat und fixierte Überschriften werden gesondert geprüft.

Gesamt-PDFs und beide ZIP-Varianten wurden lokal gebaut. Die Archive enthalten keine Unterordner oder Markdown-Aktenstücke; die Einzel-PDF-Sammlungen enthalten genau 26 beziehungsweise 30 Beleg-PDFs. Beide ZIP-Varianten führen den vorgeschriebenen zweisprachigen Hinweis in einer eigenen Textdatei. Die Beleg-PDFs enthalten ihn nicht. Word-Dokumente, Tabellen, E-Mail-Darstellung und Bildanlagen wurden zusätzlich visuell geprüft.

Die strikte offizielle Plugin-CLI-Prüfung besteht für das neue Plugin sowie den vollständigen Marketplace und alle 240 Plugin-Manifeste. Die Repository-Prüfungen für Pluginstruktur, Marketplace-Import, YAML-Frontmatter, Laufzeitbudgets und Promptzuordnung bestehen ebenfalls. Das [Evaluationsprofil](../quality/evals/strassennutzung-genehmigungen.json) enthält zehn fachlich getrennte Aufgaben mit überprüfbaren Ergebniskriterien. Die Profilprüfung ist eine Strukturprüfung, kein ausgeführter Modelltest.

## 1.3. Quellenprüfung und Grenzen

Das [Quellenregister](references/strassenrecht-quellen.md) dokumentiert amtliche Normzugänge und sechs volltextgeprüfte Entscheidungen mit Randnummern. Jede Entscheidung wird nach Rechtsgebiet, Landesrecht, Verfahrensart und zeitlicher Fassung eingeordnet. Insbesondere werden das Urteil des Bundesverwaltungsgerichts vom 06.06.2024 zum Gehwegparken, die landesrechtliche Genehmigungskonzentration und die begrenzte Übertragbarkeit der historischen Pollerentscheidung auseinandergehalten.

Dies ist keine vollständige Prüfung sämtlicher Landesgesetze oder kommunaler Anordnungen. Im einzelnen Mandat bleiben die örtliche Widmung, Beschilderung, aktuelle Normfassung und einschlägige Eingriffsbefugnis zu verifizieren. Aktenmaterial ersetzt keine amtliche Quelle.

Es wurde kein interaktiver Import mit anschließender Fallbearbeitung in einer gehosteten Arbeitsoberfläche durchgeführt. Bestandene Strukturprüfungen garantieren weder die automatische Skillauswahl noch die Qualität jeder Modellantwort. Für Release-Archive ist zusätzlich das Ergebnis des jeweiligen Veröffentlichungsworkflows maßgeblich.

## 1.4. Prüfsummen der Prompts

- Schnellstart: `9998f7a7abbbffb936f5ff3046ef1c3b8e3ff384d66493e576ea37a888e7dd69`.
- Werkstatt: `5e5aef0a7b0ca858f948bebfdfdca57fbe9574ae6b880b070ff8311b30ca77f8`.
