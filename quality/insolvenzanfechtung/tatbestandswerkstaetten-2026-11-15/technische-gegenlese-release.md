# Technische Gegenlese der Releaseintegration

## 1. Umfang und Grenzen

Geprüft wurde am 15. November 2026 der Arbeitsstand der Integration für die drei Plugins Insolvenzanfechtung, Liquiditätsplanung sowie Zahlungsunfähigkeits- und Überschuldungsprüfer in Version 445.36.2. Gegenstand waren `build-skill-quality-release.py`, `release_asset_common.py`, beide betroffenen Veröffentlichungsworkflows und `test-insolvenzanfechtung.py`. Für die Assetbindung wurden zusätzlich der Werkstattexportvertrag, dessen Negativtests und der vorhandene Publisher gelesen.

Dies ist eine unabhängige Codeprüfung mit den unten genannten ausgeführten Tests. Der abschließende Renderlauf, der vollständige Releasebau, die Remote-CI und die Veröffentlichung sind eigene Prüfungen des integrierenden Agenten. Diese Notiz behauptet hierfür keinen Erfolg.

## 2. Konkrete Befunde und Bearbeitung

Der ursprüngliche Arbeitsstand erlaubte einen Scope mit Insolvenzanfechtung 445.36.2 ohne `additional_assets`. Damit hätten die drei Plugins mit ihren zehn vorhandenen Prompt-Snapshots und den beiden Metadateien als 17 Assets veröffentlicht werden können, obwohl die READMEs außerdem das Werkstatt-ZIP und den PDF-Gesamtband versprechen. Der integrierende Agent hat die Pflicht zum vollständigen Werkstattpaar für diesen Scope ergänzt. Die beiden generierten Assets und ihre wirklichen Hashes sind nach dem endgültigen Renderlauf in den Scope aufzunehmen; der erwartete Bestand erhöht sich damit auf 19 Assets.

Die ursprünglichen PR-Pfadfilter erfassten weder die neuen Werkstatt-Builder und -Validatoren noch ausschließlich geänderte PDF-/ZIP-Exporte. Dadurch wäre eine spätere Änderung allein dieser Dateien nicht von der Komponentenprüfung erfasst worden. Der integrierende Agent hat die betreffenden Pfade ergänzt. Der laufende inhaltliche PR löst die Prüfung ohnehin über die Pluginpfade aus.

Im geprüften Exportvertrag entfernte die Textnormalisierung sämtliche Satz- und Rechenzeichen. Eine unmittelbar ausgeführte Gegenprobe zeigte identische Vergleichswerte für `18.000 Euro` und `180,00 Euro`, für `10 %` und `10 ‰` sowie für `−15.000 Euro` und `15.000 Euro`. Die vorhandenen Hashprüfungen schützen unveränderte freigegebene Bytes; diese Gegenprobe betrifft zusätzlich die behauptete inhaltliche Übereinstimmung zwischen Quelle und neu gerendertem PDF. Der Befund wurde zur Korrektur an den integrierenden Agenten gemeldet. Ein späterer Nachweis dieser Korrektur muss den sinnverändernden Zeichenwechsel im echten PDF erkennen, auch wenn dessen Hash im Test aktualisiert wurde.

## 3. Ergänzter Regressionstest

`test_anfechtung_445_36_2_scope_requires_both_workshop_assets` in `scripts/test-skill-quality-release.py` verwendet ein vollständig isoliertes technisches Scope-Fixture. Das vollständige Paar durchläuft zuerst die Scopeprüfung. Danach werden das vollständig fehlende Feld, eine leere Assetliste, nur das ZIP und nur der Gesamtband jeweils zurückgewiesen. Die Fixture-Dateien werden ausdrücklich nicht als echte PDF- oder ZIP-Exporte ausgegeben; deren Inhalte prüft der gesonderte Exportvertrag anhand der tatsächlich erzeugten Dateien.

Eine zusätzliche Mutation im Arbeitsspeicher entfernte ausschließlich die neue Pflichtpaar-Schranke, ohne die Repositorydatei zu verändern. Der neue Test meldete dann vier Testfehler und keinen Ausführungsfehler. Damit ist nachgewiesen, dass die Regression das vorherige Verhalten erkennt und nicht nur eine anderweitig ungültige Fixture zurückweist. Die bestehenden Prüfungen wurden nicht abgeschwächt.

## 4. Ausgeführte Prüfungen

`test-skill-quality-release.py` bestand nach der Ergänzung mit 20 Tests. `test-source-release-candidates.py` bestand mit sechs Tests. `test-insolvenzanfechtung.py` bestand mit neun Tests, davon ein erwarteter übersprungener Test für den nicht übergebenen Releaseordner. `git diff --check` für die geänderte Testdatei meldete keinen Fehler.

## 5. Veröffentlichungs- und Bestandsschutz

Der gelesene Qualitätsrunden-Publisher verlangt den exakten sauberen Commit, dessen Zugehörigkeit zu `origin/main`, passende Scope- und Paketbytes sowie die Release-Notiz. Er verschiebt keinen vorhandenen abweichenden Tag und verweigert Änderungen an einem bereits veröffentlichten Release. Der Upload erfolgt mit `--protect-published`; anschließend werden alle Assets in ein frisches Verzeichnis heruntergeladen und erneut gegen Scope, Quellbytes und lokale Hashes geprüft. Erst danach wird der bestätigte Entwurf öffentlich geschaltet.

Der ältere Insolvenzanfechtungsworkflow behält seinen ursprünglichen 1.1.0-Veröffentlichungspfad und verlangt für manuelle Ausführung weiterhin diese Manifestversion. PR-Prüfungen neuerer Pluginversionen verwenden den Qualitätsrundenbau. Damit wird der alte 36-Asset-Release nicht unter seinem bisherigen Tag durch die neue Qualitätsrunde ersetzt. Die abschließende Bestätigung des unveränderten Remote-Bestands bleibt Teil der tatsächlichen Veröffentlichung.
