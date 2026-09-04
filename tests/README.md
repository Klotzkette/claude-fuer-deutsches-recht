# Funktionstests

[Startseite](../README.md) · [Skill-Verzeichnis](../SKILLS.md) · [Übungsakten](../testakten/README.md)

## 1. Manuelle und automatische Prüfung

Die [Smoke-Tests](./smoke-tests.md) beschreiben manuell auszuführende Beispielszenarien. Sie werden durch das Öffnen dieser Datei nicht ausgeführt. Vor dem Durchspielen sind Skillnamen, Unterlagen und erwartete Ergebnisse mit dem aktuellen Plugin abzugleichen; ältere Szenarien ersetzen keine fachliche Prüfung.

Die automatischen Bestands- und Paketprüfungen liegen unter [scripts](../scripts/) und werden im [Release-Ablauf](../.github/workflows/release-plugin-zips.yml) aufgerufen. Sie prüfen unter anderem Plugin-Struktur, Marketplace-Import, Dateiformate und Verzeichnislinks. Ein grüner technischer Prüflauf ist kein Nachweis der juristischen Richtigkeit sämtlicher Ausgaben.

## 2. English

The smoke-test document contains manual scenarios, not an executable test suite. Automated repository and release checks are defined in the linked workflow. Both types of checks have a limited scope and do not replace review of the actual work product.
