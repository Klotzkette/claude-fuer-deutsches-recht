# Release-Routing für zentrale Testakten

## 1. Aufteilung

GitHub erlaubt [höchstens 1.000 Assets pro Release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).
`scripts/release-routes.json` benennt ausschließlich die vier neuen zentralen Akten.
Nur deren acht Einzel-ZIPs (Originalformate und Einzel-PDFs) liegen in `akten-vVERSION`.
Alle bisherigen Assets und Downloadadressen bleiben im Hauptrelease `vVERSION`.
Die Version stammt aus `.claude-plugin/marketplace.json`, nicht aus `latest`.

Alle Dateien werden zuerst unverändert in `dist` gebaut. Erst nach den vollständigen
Akten-Sammelpaketen und `alles-komplettpaket.zip` erzeugt `stage-release-assets.py`
die getrennten Verzeichnisse `release-staging/main` und `release-staging/companion`.
Die Sammelpakete enthalten weiterhin auch die vier neuen Akten. Das Staging prüft
vor der Aufteilung, dass die konfigurierten Akten-ZIPs in allen drei Sammelpaketen
an ihren vorgesehenen Archivpfaden vorhanden sind.
Die Stages verwenden Hardlinks (bei getrennten Dateisystemen Kopien); nach dem
Staging darf der Buildbestand nicht mehr verändert werden. Ein vorhandenes
Staging-Verzeichnis wird niemals gelöscht oder überschrieben.

Jeder Stage besitzt eine eigene `checksums-sha256.txt`; sie zählt beim Limit mit.
Die Hauptrelease-Prüfsummen nennen keine ausschließlichen Companion-Dateien.
Die Prüfsummen im vollständigen `dist` sind nur ein Build-Artefakt, keine Liste
der Remote-Assets eines einzelnen Releases. Bei der geplanten Gesamtzahl 1003
ergaben sich 995 Hauptrelease-Assets und 9 Companion-Assets inklusive Prüfsummen.
Weitere neue Pakete werden bei jedem Build erneut gezählt; die Aufteilung darf
die Grenze nicht lediglich aufgrund dieser historischen Beispielzahl freigeben.
Eine leere `companion_case_slugs`-Liste erzeugt nur den Hauptrelease-Stage und
behält den bisherigen Publisher-Ablauf bei; das 1000er-Limit gilt weiterhin.

## 2. Tag und Veröffentlichung

Der Workflow checkt den angeforderten Haupttag aus. `publish-release-assets.py`
vergleicht den Checkout mit dem remote aufgelösten Haupttag. Annotierte Tags
werden bis zum Commit aufgelöst. Ein fehlender Companion-Tag wird per Git-Refs-API
genau an diesem SHA angelegt, ein abweichender vorhandener Tag führt zum Abbruch.
Es gibt kein Force-Update und kein Löschen von Releases oder Tags. Der Helfer führt
keinen Git-Push aus; er liest den aktuellen Remote-Haupttag unmittelbar vor dem
Anlegen des Companion-Tags und kontrolliert beide Tags nochmals vor der Publikation.

Der Companion wird als Draft mit `--target SHA --verify-tag --latest=false`
angelegt. Vorhandene Releases werden mit `gh release view` geprüft, damit auch
Entwürfe nach ihrem Tag zuverlässig gefunden werden. Beide Stages werden mit den vorhandenen Upload- und Remote-Validatoren
hochgeladen und vollständig verifiziert. Erst danach wird der Companion mit
`--latest=false` veröffentlicht, anschließend der Hauptrelease. Der Tag
`akten-vVERSION` passt nicht auf den Workflow-Trigger `v*`.
Der Hauptrelease behält sein bisheriges Latest-Verhalten. Das Prüfen eines bereits
vorhandenen Companion-Releases ist rein lesend und ändert keine Latest-Markierung.

Wiederholungen akzeptieren identische bereits publizierte Assets; bei Abweichungen
werden publizierte Releases im Companion-Ablauf nicht verändert. Ein Upload- oder
Prüffehler verhindert jede nachfolgende Publikation. Scheitert nur die Publikation
des Hauptreleases, darf der bereits vollständige Companion bestehen bleiben;
ein erneuter Lauf setzt den Ablauf fort. Es werden keine historischen Releases
zur Platzbeschaffung gelöscht. Build-only-Aufrufe führen keine Remote-Aktionen aus.

## 3. Links und Integration

`release_routing.py` ist die gemeinsame Quelle für Fall-ZIP-URLs, Dateiauswahl
und Tags. Die vorhandenen README- und Index-Generatoren ersetzen `latest`-Platzhalter
der vier konfigurierten Akten durch versionsfeste Companion-Links, auch außerhalb
des generierten Downloadblocks. Andere Fall-, Plugin- und Sammelpaketlinks bleiben
unverändert. Der Download-Validator lehnt veraltete Companion-Versionen und
`latest`-Platzhalter dieser vier Akten ab.

Die Root-README wird in diesem Infrastrukturauftrag nicht regeneriert.
Kurzer Hinweis für die übergeordnete Integration:

> Die acht Einzel-ZIPs der vier neuen Testakten liegen wegen des GitHub-Assetlimits
> im versionsgleichen Akten-Begleitrelease. Alle Akten-Sammelpakete und das
> Komplettpaket bleiben vollständig im Hauptrelease; bestehende Links bleiben erhalten.

Offline-Regressionen: `python3 scripts/test-release-routing.py`,
`python3 scripts/test-release-assets.py` und `python3 scripts/test-readme-navigation.py`.
Keine dieser Regressionen schreibt zu GitHub.
