# Release-Routing für zentrale Testakten

## 1. Aufteilung

GitHub erlaubt [höchstens 1.000 Assets pro Release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases).
`scripts/release-routes.json` routet deshalb alle zentralen Akten in den
Begleitrelease. Je Akte liegen dort beide Einzel-ZIPs (Originalformate und
Einzel-PDFs) unter `akten-vVERSION`. Plugin-ZIPs, Marketplace und Sammelpakete
bleiben im Hauptrelease `vVERSION`.
Die Version stammt aus `.claude-plugin/marketplace.json`, nicht aus `latest`.

Alle Dateien werden zuerst unverändert in `dist` gebaut. Erst nach den vollständigen
Akten-Sammelpaketen und `alles-komplettpaket.zip` erzeugt `stage-release-assets.py`
die getrennten Verzeichnisse `release-staging/main` und `release-staging/companion`.
Die Sammelpakete enthalten weiterhin alle zentralen Akten. Das Staging prüft
vor der Aufteilung, dass die gerouteten Akten-ZIPs in allen drei Sammelpaketen
an ihren vorgesehenen Archivpfaden vorhanden sind.
Die Stages verwenden Hardlinks (bei getrennten Dateisystemen Kopien); nach dem
Staging darf der Buildbestand nicht mehr verändert werden. Ein vorhandenes
Staging-Verzeichnis wird niemals gelöscht oder überschrieben.

Jeder Stage besitzt eine eigene `checksums-sha256.txt`; sie zählt beim Limit mit.
Die Hauptrelease-Prüfsummen nennen keine ausschließlichen Companion-Dateien.
Die Prüfsummen im vollständigen `dist` sind nur ein Build-Artefakt, keine Liste
der Remote-Assets eines einzelnen Releases. Die tatsächlichen Assetzahlen werden
bei jedem Build neu ermittelt; die Aufteilung darf die Grenze nicht aufgrund einer
historischen Beispielzahl freigeben.
Das Schema 1 mit einer leeren `companion_case_slugs`-Liste bleibt für gezielte
Builds und Regressionen rückwärtskompatibel: Es erzeugt nur den Hauptrelease-Stage;
das 1000er-Limit gilt weiterhin.

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
aller zentralen Akten durch versionsfeste Companion-Links, auch außerhalb
des generierten Downloadblocks. Andere Fall-, Plugin- und Sammelpaketlinks bleiben
unverändert. Der Download-Validator lehnt veraltete Companion-Versionen und
`latest`-Platzhalter dieser Akten ab.

Root-README, Asset-Index und Pluginseiten werden mit den bestehenden Generatoren
auf die versionsfesten Companion-Links fortgeschrieben. Kurzfassung:

> Beide Einzel-ZIP-Varianten aller zentralen Testakten liegen wegen des
> GitHub-Assetlimits im versionsgleichen Akten-Begleitrelease. Alle Akten-Sammelpakete und das
> Komplettpaket bleiben vollständig im Hauptrelease; bestehende Links bleiben erhalten.

Offline-Regressionen: `python3 scripts/test-release-routing.py`,
`python3 scripts/test-release-assets.py` und `python3 scripts/test-readme-navigation.py`.
Keine dieser Regressionen schreibt zu GitHub.

## 4. Öffentliche Erreichbarkeit nach Veröffentlichung

Ein grüner Upload- oder Offline-Check bedeutet noch nicht, dass ein Besucher die
Dateien herunterladen kann. Entwürfe sind mit angemeldetem GitHub-Zugang sichtbar,
ihre öffentlichen Downloadlinks liefern jedoch HTTP 404. Wird `main` vor dem
Begleitrelease aktualisiert, besteht bis zur Veröffentlichung eine Downloadlücke.
Diese Zwischenphase nicht als fertige Veröffentlichung melden.

Nach Veröffentlichung beider Releases die Downloadtabellen ohne Anmeldung prüfen:

```sh
python3 scripts/validate-public-downloads.py
```

Für eine einzelne Pluginseite genügt beispielsweise:

```sh
python3 scripts/validate-public-downloads.py liquiditaetsplanung/README.md
```

Die Prüfung liest die öffentliche Release-API ohne Token, fasst gleiche Ziele
zusammen und berücksichtigt alle Assetseiten. Sie meldet nicht veröffentlichte
Releases, fehlende oder leere Dateien und unvollständige Uploads als Fehler.
API-Limits und Netzprobleme sind nicht erfolgreich geprüfte Downloads. Die Prüfung
ersetzt weder Prüfsummen- und Archivkontrolle noch die Navigationstests für lokale
PDFs und Markdown-Seiten. Offline-Regression: `python3 scripts/test-public-downloads.py`.

## 5. SI-native Kanzlei als Komponentenrelease

`si-native-kanzlei-v445.33.3` veröffentlicht ausschließlich die neue Kanzlei-Erweiterung: Claude/Codex-Paket, portables Paket, 24 Originalformat-ZIPs, 24 Einzel-PDF-ZIPs sowie eine eigene Sammlung dieser 24 Akten. `scripts/scoped-release-assets.json` hält die direkten Routen fest. Das Komponentenrelease wird nicht als Latest gesetzt; die bestehenden allgemeinen Sammelpakete werden dadurch nicht ersetzt.
