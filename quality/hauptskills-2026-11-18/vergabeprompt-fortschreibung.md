# Vergabeprompts: getrennte Fortschreibung am 18. November 2026

Die drei vorhandenen Rollen-Megaprompts wurden mit `vergaberecht-werkstatt/scripts/generate-megaprompt.py` aus dem aktuellen Modulbestand neu erzeugt. Anlass sind die überarbeiteten Hauptskills. Testaktendaten, Kurzprompts und historische Prüfberichte wurden dabei nicht geändert. Diese Fortschreibung ist ein Erzeugungs- und Integritätsnachweis; sie behauptet keine erneute vollständige Fachprüfung sämtlicher historischer Promptmodule.

[Der maschinenlesbare Nachweis](vergabeprompt-fortschreibung.json) bindet für jede Rolle den exakten Pfad, den SHA-256-Wert der bisherigen Bytes, die komprimierte Vorfassung einschließlich ihres Archivhashes und den SHA-256-Wert der neuen Bytes. Er bindet zusätzlich den unveränderten historischen Rollenrouting-Nachweis vom 14. November 2026.

`scripts/test-vergaberecht-module-routing.py` prüft alle drei Bindungen und verwirft fehlende oder doppelte Rollen, falsche Archive, falsche Generatorpfade sowie abweichende Vorher-, Nachher- und Berichtshashes. Für die zwei bereits im alten Routing-Nachweis erfassten Megaprompts rekonstruiert der Test dessen ursprüngliche Bytes aus der archivierten Vorfassung und den unveränderten historischen Deltas. Die übrigen historischen Promptnachweise werden weiter direkt gegen ihre aktuellen, unveränderten Bytes geprüft. Separat vergleicht derselbe Test die aktuellen drei Megaprompts mit der tatsächlichen Ausgabe des Generators aus den aktuellen Modulen und prüft deren ausführbare Rollenaufrufe.

Gezielte Prüfung am 18. November 2026: sieben Tests bestanden, Exitcode 0. Die Archivierung begründet keine allgemeine Hash-Ausnahme und keine Neufassung des historischen Routing-Nachweises.
