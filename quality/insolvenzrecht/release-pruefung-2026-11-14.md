# Paketprüfung Insolvenzrecht 445.35.4

## 1. Geprüfter Inhalt

Der lokale Build enthält sechs Releasedateien. Das installierbare ZIP enthält 426 Dateien einschließlich der 308 erzeugten Fachmoduldateien. Die 99 bestehenden auswählbaren Skills bleiben erhalten; 159 ergänzende Quellskills werden als lokale Fachreferenzen erschlossen. Die drei eigenständigen Prompts liegen außerhalb des ZIP.

ZIP-SHA-256: `7481dfeb70f21115d79182f8844a3e26a1d0c85dff82cd8ce0a11709466cb038`.

Die tatsächlichen ZIP-Inhalte wurden mit den Quellbytes verglichen und isoliert entpackt geprüft. Ein zweiter Build ist byteidentisch. Die drei gewünschten Spezialplugins bleiben eigenständig. Es wurden keine Testakten oder bestehenden Releases neu geschrieben.

## 2. Lokale Prüfungen

- Vier Repository-Pflichtprüfungen bestanden: Marketplace-Import, YAML-Frontmatter, Pluginstruktur und Gesamt-PDF-Bestand mit 628 zentralen Akten.
- Zehn Fachmodulprüfungen einschließlich des echten Release-ZIP bestanden; dabei vollständige Herkunft, getrennte Planvorlagen, lokale Referenzen, Quelldrift und unveränderte Skillanzahl geprüft.
- Acht Releaseprüfungen bestanden, darunter falscher Tag-Commit, annotierte Tags, veraltete Importkopien, geänderte ZIP-Inhalte trotz neuer Prüfsummen, manipulierte Prompts sowie fehlende oder zusätzliche Assets.
- Elf Versionsroutingtests und 51 Navigationstests bestanden. Root-Übersicht, lokale Links und aktenbezogene Downloadhinweise geprüft.
- Prompt-Einstiege, Prompt-Routing, 17 Schnellstarttests und 27 Visualisierungstests bestanden. Die synchronisierten Visualblöcke sind unverändert kanonisch.
- Laufzeitbudgets eingehalten. Qualitätsaudit aller 315 Profile bestanden; bestehende `needs_review`-Hinweise bei vier nicht bearbeiteten anderen Plugins bleiben unverändert und sind keine neue Freigabe dieser Inhalte.

## 3. Veröffentlichungsnachweis

Dieser Vermerk dokumentiert die lokale Prüfung vor Veröffentlichung. Der Workflow `insolvenzrecht-release.yml` bindet die Dateien an den geprüften Main-Commit, legt einen freien Tag ohne Force-Push an und prüft die heruntergeladenen Assets vor und nach Veröffentlichung erneut. Der erfolgreiche Workflowlauf und das öffentliche Release liefern den gesonderten Veröffentlichungsnachweis; dieser Vorabvermerk behauptet keinen bereits erfolgten Upload.

Die fachlichen Prüfgrenzen stehen im [Konsolidierungsvermerk](konsolidierung-pruefvermerk-2026-11-14.md), die Quellenzuordnung im [Fachmodulvermerk](fachmodule-pruefung-2026-11-14.md). Kein Live-Modelltest aller Anwendungsoberflächen und keine neue Vollprüfung sämtlicher juristischer Bestandsquellen.
