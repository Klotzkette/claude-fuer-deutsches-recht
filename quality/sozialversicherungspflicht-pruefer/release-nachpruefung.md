# Nachprüfung des Release-Builds

## 1. Erster GitHub-Lauf

PR #458 wurde am 30. September 2026 nach den dokumentierten lokalen Prüfungen auf `main` gemergt. Der Release-Lauf `36688262226` für `v445.16.0` wurde vor dem PDF- und ZIP-Build gestoppt: Drei Assertions in `scripts/test-release-routing.py` setzten noch vier tatsächlich konfigurierte Begleitakten beziehungsweise acht Archive voraus. Die inzwischen erweiterte Konfiguration enthält elf Akten beziehungsweise 22 Archive.

Die lokalen ersten Prüfungen fanden vor der abschließenden Erweiterung der Release-Zuordnung statt. Die vorgeschriebenen Prüfungen vor dem Push erfassen diese konkrete Testdatei nicht. Deshalb wurde der Fehler durch den Release-Lauf entdeckt; die früheren erfolgreichen Läufe sind kein Nachweis für diese zuletzt geänderte Zuordnung.

## 2. Korrektur

Die reale Release-Zuordnung und die synthetischen Grenzfälle erhalten getrennte Testdaten. Die Sollprüfung der tatsächlich vorgesehenen elf Akten bleibt bestehen. Die Grenzfälle prüfen mit einer festen Vierakten-Konfiguration weiterhin unter anderem die Aufteilung von 1.003 Ausgangsassets in 995 Haupt- und neun Begleitassets sowie die GitHub-Grenze von 1.000 Dateien. Native Akten, Skills und die beiden Prompts werden durch diese Korrektur nicht geändert.

Der bereits gesetzte Tag `v445.16.0` bleibt unverändert. Die korrigierte Veröffentlichung verwendet `v445.16.1` einschließlich der dazugehörigen Begleit-Release-Verweise.

## 3. Gezielte Nachprüfung

Die korrigierte Routing-Suite besteht mit 30 Tests. Die getrennte Release-Asset-Suite, der Abgleich der zentralen Übersichten und die Validierung sämtlicher Testakten-Downloadverweise bestehen ebenfalls. Der unabhängige Diff-Review der Testkorrektur ergab keinen Befund. Eine verbliebene sichtbare Versionsangabe im Startup-Gründer-README wurde aktualisiert; der danach erneut ausgeführte Marketplace-Importcheck besteht.
