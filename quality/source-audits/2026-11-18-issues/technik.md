# 1. Technische Nachprüfung der Issues 515, 518 und 519

Prüfdatum: 18. November 2026. Vollständige Issue-Texte und jeweils ein Kommentar wurden über den GitHub-Connector gelesen. Geprüft wurde der aktuelle Arbeitsstand auf Basis von `e458e111f94ce0bcd9788e192beeb61a81d20812`. Es wurden keine fremden Änderungen übernommen und für diese drei Issues keine Programmänderungen benötigt.

## 1.1. Issue 515 – schreibende Generatorhilfe

[Issue 515](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/515). Der Kernfehler ist behoben: Alle 19 genannten Skripte verarbeiten Hilfe und ungültige Argumente vor dem schreibenden Einstieg. `parse_generator_cli` verwendet eine ausdrückliche Argumentprüfung ohne Kurzform-Abkürzungen. Der Regressionstest prüft je Skript sechs Aufrufe in einer isolierten Struktur einschließlich Inhalts-Hashes aller Dateien: `--help` und `-h` enden mit 0; `--check`, ein Tippfehler, `--he` und ein Positionsargument enden mit 2. Keine Datei wird verändert. Ein zweiter Test bestätigt den weiterhin schreibenden argumentlosen Einstieg.

Der zusätzlich vorgeschlagene echte `--check`-Modus ist ausdrücklich nicht implementiert. Die Hilfe erklärt dies. Das ist ein nicht umgesetzter Funktionsvorschlag, kein verbliebener Schreibfehler: Ein abgelehntes `--check` wird nicht als erfolgreiche Konsistenzprüfung ausgegeben. Das Issue kann hinsichtlich des beschriebenen Fehlverhaltens als erledigt behandelt werden, ohne einen echten Prüfmodus zu behaupten.

Prüfung: `scripts/test-generator-cli.py`, 2 Tests einschließlich 114 isolierter Flag-Aufrufe, erfolgreich. Der Test ist im Pull-Request-Workflow `rechtsstand-pruefen.yml` eingebunden.

## 1.2. Issue 518 – Schwerpunkt und erster Prüffall

[Issue 518](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/518). Erledigt. Der Schwerpunkt wird aus `selection.target_skill` ermittelt und durch `focus_review` an die konkrete Datei gebunden. Der erste Testfall muss fachlich nicht dieselbe Zielroute haben. Deshalb wäre ein bloßes Angleichen zweier unterschiedlicher, sinnvoller Rollen falsch gewesen.

Prüfung: Der vollständige `scripts/test-schwerpunkt-coverage.py` lief mit 12 Tests erfolgreich. Die Schwerpunkt- und Vertragsregressionen sind in `compatibility-release.yml` für Pull Requests eingebunden; Änderungen unter `quality/evals/**` lösen diesen Workflow aus. Der ältere Kommentar über 14 weitere Download-/Zitierregelbefunde beschreibt nicht mehr den aktuellen Testerfolg.

## 1.3. Issue 519 – veraltete Prüfhashes

[Issue 519](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues/519). Der technische Kern und die Nachprüfungsdokumentation sind erledigt. `validate_file_hashes` vergleicht alle aktiven Werte in `skill_hashes`, `reviewed_file_hashes` und `artifact_hashes` mit den tatsächlichen Bytes. Ungültige Werte, fremde Pfade und aus dem Repository führende Symlinks werden zurückgewiesen. Die Regression verändert gezielt Prüfsummen und verlangt anschließend einen Auditfehler.

Die ursprünglich 27 Einträge sind in den mittlerweile 31 historischen Angaben erhalten: 20 bei Corporate Contract Law, die fünf ursprünglich bezeichneten Wirtschaftsberaterdateien sowie dort zusätzlich der Schnellstart, die Gesellschafterstreit-README sowie dort zusätzlich zwei Prompts und der allgemeine Anwaltschafts-Werkstattprompt sowie dort zusätzlich der Schnellstart. Alle vier Profile haben inzwischen einen Abschlussstatus `reviewed`, nicht mehr den im Kommentar vom 8. November beschriebenen offenen Stand.

Technisch nachgeprüft wurden historische Dateiumfänge, eindeutige Einzelzuordnung, gebundene Abschlussbelege, die darin bezeichneten Berichte und die heutigen Datei-Hashes. Die drei späteren Werkstatt-Visualisierungen bestehen den eng begrenzten `visual_block_only`-Nachweis. Die historischen Hashes wurden weder ersetzt noch rückdatiert. Die zugehörigen Abschlussbelege sind:

- `quality/source-audits/2026-11-14-nachpruefung/completed/corporate-contract-law.json` – 20 Dateien.
- `quality/plugin-consolidation/2026-11-15/navigation-reviews/wirtschaftsanwalt.json` – 6 Dateien.
- `quality/plugin-consolidation/2026-11-15/navigation-reviews/gesellschafterstreit.json` – 3 Dateien.
- `quality/source-audits/2026-11-14-nachpruefung/completed/anwaltschaft-generell.json` – 2 Dateien.

Alle aktiven Hashfelder und alle Abschlussketten der vier Profile bestehen die vorhandene Validierung; `pending_file_reviews` gibt jeweils eine leere Liste zurück. Die datierten Einzelbefunde und ihre Prüfgrenzen wurden gelesen. Dies ist ein technischer Provenienzabgleich, keine erneute vollständige juristische Nachprüfung aller 31 Inhalte und kein Live-Modelltest.

Prüfung: Der vollständige `scripts/test-quality-lab.py` lief mit 81 Tests erfolgreich. Im isolierten Test erscheint einmal die Git-Meldung über ein nicht vorhandenes Repository; der Code behandelt den fehlenden Revisionswert, der Testlauf endet mit Exit 0 und `OK`.

## 1.4. Umgebung und Reichweite

Verwendet wurde die vorhandene Release-Prüfumgebung unter `../tmp/plugin-merge-2026-11-15/release-clean-env/bin/python`, weil der Systeminterpreter für den Schwerpunkt-Test `markdown_it` nicht bereitstellt. Es wurden keine Tests übersprungen. Diese Ergebnisse ersetzen nicht die abschließenden Prüfungen nach Integration des neuen Jugendmedienschutz-Plugins und weiterer Fachänderungen. Kein GitHub-Kommentar und keine Issue-Schließung wurde in diesem Teilauftrag ausgeführt.
