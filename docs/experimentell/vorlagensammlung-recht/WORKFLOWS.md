# Workflows für Pflege und Nutzung

Diese Datei beschreibt die praktischen Wege durch das Repository. Sie ersetzt nicht `CLAUDE.md` und `CONTRIBUTING.md`; sie ist der schnelle Arbeitszettel für Nutzer, die eine Vorlage finden, ändern, prüfen oder veröffentlichen wollen.

**Navigation:** [Startseite](README.md) · [Alle Direktdownloads](DOWNLOADS.md) · [Vorlagen nach Dokumenttyp](kategorien/) · [Prozesspakete](prozessvorlagen/) · [Gerichtsleitender Sonderbereich](vorlagen-gerichtsleitend/INDEX.md) · [Gesamtes Repository als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-gesamt.zip)

## 1. Vorlage finden

1. Den [Schnellzugriff des Gesamtindex](DOWNLOADS.md#schnellzugriff) nutzen, wenn Vorlagenname oder Suchwort bekannt sind und ODT oder Markdown unmittelbar benötigt wird. Jeder Rechtsbereich hat dort einen Sprung zum eigenen Downloadblock; `Strg+F` oder `Cmd+F` durchsucht sämtliche 981 Haupt- und 113 Sondervorlagen.
2. [Rechtsgebiet wählen](README.md#rechtsgebiete-und-dokumenttypen), wenn der fachliche Kontext klar ist, etwa Arbeitsrecht, Sozialrecht oder gewerblicher Rechtsschutz.
3. Dokumenttyp wählen, wenn der Arbeitsmodus klar ist: [vertragliche Vorlagen](kategorien/01-vertragliche-vorlagen/), [prozessuale Vorlagen und Formulare](kategorien/02-prozessuale-vorlagen-und-formulare/) oder [sonstige Vorlagen](kategorien/03-sonstige-vorlagen/).
4. [Gerichtsleitenden Gesamtindex](vorlagen-gerichtsleitend/INDEX.md) wählen, wenn ein gerichtlicher, staatsanwaltschaftlicher oder amtsanwaltschaftlicher Entwurf gesucht wird. Für den unmittelbaren Download einzelner Dateien zum [gerichtsleitenden Abschnitt des Gesamtindex](DOWNLOADS.md#gerichtsleitender-sonderbereich) wechseln.
5. Volltextsuche nutzen, wenn nur das Problem bekannt ist:

```bash
rg -n "Sperrzeit|Hilfsmittel|einstweilige Verfügung|Markenlizenz|Kosten der Unterkunft"
```

Jeder Treffer führt in einen Vorlagenordner. Dort ist die `README.md` die Menüseite: ODT lädt die editierbare Bürofassung herunter, Markdown (ZIP) die gepackte Quellenfassung; die beiden Vorschau-Links öffnen die Dateien am kanonischen Speicherort. Wer den gesamten Bestand benötigt, lädt ein [fachlich zugeschnittenes Komplettpaket](README.md#downloads), [`main` als ZIP-Archiv](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/dist/vorlagensammlung-recht-gesamt.zip) oder klont das Repository.

## 2. Vorlage benutzen

1. Zuerst die `README.md` der Vorlage lesen. Dort stehen Anwendungsbereich, Pflichtangaben, Praxisfehler, Normen und Rechtsprechungsanker.
2. Dann die ODT-Fassung öffnen, wenn menschlich in einer Office-Umgebung gearbeitet wird.
3. Die Markdown-Fassung nutzen, wenn die Vorlage maschinell geprüft, verglichen oder in einem KI-gestützten Arbeitsablauf weiterverarbeitet wird.
4. Eckige Platzhalter vollständig ersetzen oder bewusst streichen. Ein nicht ersetzter Platzhalter ist ein Entwurfsrest.
5. Rechtsprechungsanker vor Verwendung in einer Mandatsfassung noch einmal in der amtlichen oder primären Quelle prüfen.

## 3. Schnell entscheiden, ob die Vorlage passt

1. Passt der Dokumenttyp? Vertrag, Antrag, Klage, Widerspruch, Vermerk, Protokoll und gerichtlicher Entwurf folgen jeweils eigener Mechanik.
2. Passt die Rolle? Kläger, Beklagter, Antragsteller, Behörde, Gericht, Insolvenzverwalter, Arbeitgeber oder Verbraucher dürfen nicht nur sprachlich ausgetauscht werden.
3. Passt das Verfahrensstadium? Vorgerichtliches Schreiben, erster Antrag, Erwiderung, Eilverfahren, Rechtsmittel und Vollzug brauchen unterschiedliche Anträge und Anlagen.
4. Passt die Zuständigkeit? Gericht, Behörde, Rechtsweg, sachliche Zuständigkeit, Wertgrenze und Fristbeginn werden vor dem Befüllen geprüft.
5. Passt der Anlagenapparat? Jede Anlage, die im Text erwähnt wird, muss als konkrete Anlage vorhanden sein oder bewusst gestrichen werden.

## 4. Hauptvorlage ändern

1. Die Markdown-Datei der Vorlage ändern.
2. Die zugehörige ODT-Datei neu erzeugen:

```bash
python3 scripts/md-to-odt.py rechtsgebiet/vorlagen-slug/vorlagen-slug.md
```

3. Danach die Markdown-ZIPs aktualisieren:

```bash
python3 scripts/build-md-zips.py
```

4. Den vollständigen lokalen Gate ausführen:

```bash
python3 scripts/check-all.py
```

## 5. Gerichtsleitende Vorlage ändern

Der Sonderbereich `vorlagen-gerichtsleitend/` ist Markdown-only. Dort gibt es keine ODT- und ZIP-Pflicht. Nach jeder Änderung genügt der vollständige Gate:

```bash
python3 scripts/check-all.py
```

## 6. Neue Hauptvorlage anlegen

1. Unter dem fachlich passenden Rechtsgebiet einen sprechenden ASCII-Slug anlegen.
2. `<slug>.md`, `<slug>.odt`, `<slug>.md.zip`, `README.md` und `rubric.yaml` erzeugen.
3. Die Vorlage in genau eine Drei-Ordner-Sicht unter `kategorien/` eintragen.
4. ODT und ZIP bauen.
5. Den Gesamtindex aktualisieren: `python3 scripts/build-download-index.py`.
6. Den vollständigen Gate ausführen.

## 7. Release-Pakete bauen

Vor einem Release werden zusätzlich zu den Einzeldateien drei reproduzierbare Komplettpakete und ihre SHA-256-Prüfsummen erzeugt:

```bash
python3 scripts/build-release-assets.py
```

Die Dateien unter `dist/` werden nicht eingecheckt. Jedes ZIP enthält eine erzeugte `index.html`, die mehrere Suchwörter in beliebiger Reihenfolge verknüpft, Umlaute und ASCII-Umschriften angleicht und nach Rechtsgebiet sowie Dokumenttyp filtert. Zusätzlich zu Titel und Dateipfad durchsucht sie verdichtete Fachbegriffe aus der jeweiligen README. Versionsstand und Dateizahl stehen im Kopf. Der Vorlagentitel führt zu den fachlichen Hinweisen; „Datei öffnen“ führt direkt zur Arbeitsdatei. Die responsive Liste bleibt auf kleinen Bildschirmen ohne horizontales Scrollen bedienbar. Ein zusätzliches `manifest.json` erschließt denselben Bestand mit Version, Suchbegriffen, Dateigröße und SHA-256-Prüfsumme maschinenlesbar für Kanzleisuche, Dokumentenmanagement und eigene Skripte. Der Builder erzeugt zunächst alle vier Artefakte in einem Staging-Verzeichnis und ersetzt die letzte gute Fassung erst, wenn Paketbau und Prüfsummen vollständig erfolgreich waren. Die Pakete werden dem GitHub-Release als Assets beigefügt und bleiben über stabile Links unter `releases/latest/download/` erreichbar.

## 8. Release-Workflow

1. Von aktuellem `main` einen `feature/<thema>`-Branch erstellen.
2. Änderungen klein halten und nur zusammengehörige Dateien in den PR nehmen.
3. `python3 scripts/check-all.py` grün ziehen.
4. `CHANGELOG.md` voran mit der neuen Version ergänzen.
5. Commit mit dem vorgegebenen Autor setzen.
6. Branch pushen, PR gegen `main` als ready erstellen, `@codex review` kommentieren und nach Repo-Regel per Merge-Commit mergen.
7. `main` lokal fast-forward ziehen, annotierten Tag setzen und pushen. Danach das GitHub-Release als latest erstellen und `dist/vorlagensammlung-recht-odt.zip`, `dist/vorlagensammlung-recht-markdown.zip`, `dist/vorlagen-gerichtsleitend-markdown.zip` sowie `dist/SHA256SUMS.txt` als Assets hochladen.

## 9. Häufige Fehlerbilder

1. `check-md-zip-integrity` scheitert: `python3 scripts/build-md-zips.py` ausführen.
2. `check-odt-integrity` scheitert: betroffene Markdown-Datei mit `scripts/md-to-odt.py` neu in ODT wandeln.
3. `check-gliederung` scheitert: freistehende Nummern, Buchstabenlisten, römische Ziffern oder unnummerierte Gegenstandszeilen entfernen.
4. `check-kategorien-index` scheitert: Vorlage fehlt in der Drei-Ordner-Sicht oder ist mehrfach eingetragen.
5. `check-rechtsprechungshygiene` scheitert: Aktenzeichen und Entscheidung nur mit verifizierbarem Link stehen lassen.

## 10. Rechtsstands-Sanity-Check

1. Vor fachlichen Korrekturen den kurzen Prüffahrplan in [`rechtsstands-sanity-check.md`](references/rechtsstands-sanity-check.md) lesen.
2. Nicht breit ersetzen. Erst klären, ob ein Treffer wirklich eine falsche Rechtsaussage ist oder nur ein Warnbeispiel, Suchanker oder historischer Hinweis.
3. Typische Suchläufe betreffen Formvorschriften, Übergangsrecht, Datenschutz- und Plattformbegriffe, alte Verfahrensfristen, Zuständigkeitsgrenzen und überholte Aufsichtsnormen.
4. Jede fachliche Korrektur braucht eine Primärquelle und einen engen Diff. Wenn die Rechtslage nicht sicher geklärt ist, wird die Stelle als `[noch zu klären: …]` kenntlich gemacht oder in der README als Prüfhinweis geführt.
