<!-- decimal-headings -->
<!-- decimal-anchor --> <a id="grundstücksrecherche"></a>

# 1. Grundstücksrecherche

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="lokale-app-starten"></a>

## 1.1. Lokale App starten

**Version:** `445.35.1`

Die Grundstücksrecherche ist ein App-only-Plugin mit zwei begleitenden Skills. Es gibt zwei Betriebsarten: die App mit Python-Laufzeit und eine herunterladbare HTML-Website, deren `index.html` Sie direkt öffnen können. Beide bieten eine Karte, die Flurstücksauswahl und vier bearbeitbare Auskunftsentwürfe.

<!-- decimal-anchor --> <a id="app-im-browser-oder-in-einer-verfügbaren-app-vorschau"></a>

### 1.1.1. App im Browser oder in einer verfügbaren App-Vorschau

Eine Oberfläche mit erlaubter Codeausführung und erreichbarer Browser-Vorschau kann die App dort öffnen. Fehlt diese Möglichkeit, erhalten Sie die portable Website als ZIP. Eine Plugin-Installation allein erzeugt keine native Einbettung und startet keinen Server.

Starten Sie im Verzeichnis `grundstuecksrecherche` mit Python 3 und einer virtuellen Umgebung:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r app/requirements.txt
python3 app/server.py --port 8765
```

Öffnen Sie anschließend [die lokale App](http://127.0.0.1:8765/). Ist der Port belegt, wählen Sie einen freien Port und passen die URL entsprechend an. Beenden Sie den Server im Terminal mit `Ctrl+C`. Stellen Sie den lokalen Dienst nicht öffentlich ins Netz.

Mit erlaubter Codeausführung und Browserzugriff kann der Skill `grundstuecksrecherche-starten` den Server starten und die App öffnen. Er bietet zusätzlich den Website-Download an; er behauptet keine laufende oder eingebettete App, wenn die jeweilige Oberfläche dies nicht ermöglicht.

<!-- decimal-anchor --> <a id="website-herunterladen-und-indexhtml-öffnen"></a>

### 1.1.2. Website herunterladen und index.html öffnen

[Website als ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/grundstuecksrecherche-website.zip) oder in der laufenden App unter `Vorgang` den Befehl `Website als ZIP herunterladen` wählen. Entpacken Sie das ganze ZIP in einen Ordner und öffnen Sie darin `index.html` per Doppelklick. Lassen Sie die übrigen Dateien und den Unterordner `vendor` zusammen. Auf dem Zielcomputer werden weder Python noch Terminal oder lokaler Webserver benötigt. Öffnen Sie die Datei nicht nur in der ZIP-Vorschau des Dateimanagers.

Standardmäßig enthält die Website nur die Software und gegebenenfalls den vorbereiteten Ort. Die Auswahl `Aktuellen Vorgang ... einschließen` nimmt zusätzlich Absender, Empfänger, Flurstücke und Begründungen auf. Diese Angaben sind dann für jeden Empfänger des ZIP lesbar. Der mitgelieferte Ort oder Vorgang wird in der Website erst nach einem bewussten Klick geöffnet.

Die Formulare und die Erzeugung neuer DOCX-Entwürfe funktionieren direkt im Browser. Kartenbilder, Ortssuche sowie neue Katasterabrufe benötigen weiterhin Internet und einen vom Datenanbieter erlaubten Browserzugriff. Das ZIP ist keine Offline-Katasterdatenbank. Bei einer CORS-Sperre oder einem Dienstausfall bleiben mitgelieferte oder importierte Vorgänge, manuelle Angaben und Dokumentenexporte verfügbar. Die Adresssuche und die weitergehende Katalog- und Zuständigkeitsrecherche bleiben Aufgabe der App mit Python-Laufzeit. In der portablen Website wählen Sie den Kartenausschnitt oder setzen einen Lagehinweis; schalten Sie keine Browsersicherheitsfunktionen ab.

Der Skill kann das Website-Paket auch ohne laufenden Server im Plugin-Verzeichnis bauen:

```sh
python3 app/portable.py grundstuecksrecherche-website.zip
```

Mit `--case vorgang.json` wird dessen Ort vorbereitet; erst `--include-case` schließt ausdrücklich den vollständigen Vorgang ein. Das normale Plugin-ZIP enthält den Quellcode und die Skills. Das gesonderte Website-ZIP enthält die direkt öffnungsfähige `index.html` auf der obersten Ebene.

English: Use `Vorgang` → `Website als ZIP herunterladen`, extract the complete archive and open `index.html`. No Python or server is required on the receiving computer. Document editing and generation run in the browser; live maps and searches still require internet and provider permission for browser access. Case details are excluded unless explicitly selected.

[Plugin als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/kompatibilitaet-v445.35.1/grundstuecksrecherche.zip) · [Plugin-Dateien](.) · [Repository](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/grundstuecksrecherche.md) · [Download-Index](../ASSET_INDEX.md)

Das ZIP ist der Installationsweg nach Veröffentlichung dieser Version; der lokale Start verwendet die Dateien im Arbeitsverzeichnis.
<!-- END direkt-loslegen (autogen) -->

<!-- decimal-anchor --> <a id="stadt-und-flurstücke"></a>

## 1.2. Stadt und Flurstücke

Die App beginnt mit einer leeren Stadtauswahl. Geben Sie eine beliebige deutsche Stadt ein und bestätigen Sie bei Mehrdeutigkeit den passenden Ort. Die Quellensuche ermittelt verfügbare amtliche Angebote; sie garantiert keine bundesweit einheitliche Katasterabdeckung.

Für NRW steht die Abfrage amtlicher Katasterdienste im Vordergrund. Ein Flurstück gilt nur bei tatsächlich bestätigtem Dienstergebnis als verifiziert. Die Hintergrundkarte und ein Kartenklick allein belegen weder Flurstücksgrenzen noch Flurstückskennzeichen. Außerhalb unterstützter Dienste, bei fehlender Abdeckung oder Abruffehlern bleibt die manuelle Erfassung mit Gemarkung, Flur, Flurstück und Quellenangabe verfügbar. Manuelle Angaben bleiben als solche kenntlich.

Offene Karten liefern keine Eigentümerdaten. Die App leitet Eigentum weder aus Adresspunkten noch aus Kartengeometrien ab. Eigentümerangaben benötigen einen gesonderten, zulässig erlangten Nachweis.

<!-- decimal-anchor --> <a id="vier-entwürfe-und-zip"></a>

## 1.3. Vier Entwürfe und ZIP

Aus ausgewählten oder manuell erfassten Flurstücken sowie Ihren Angaben zu Absender, Empfängern, Zweck und Nachweisen bereitet die App vier Dokumente vor:

1. Auskunftsersuchen an die Katasterbehörde.
2. Antrag an das Grundbuchamt.
3. Prüfauftrag an eine Notarin oder einen Notar.
4. Übergabevermerk an die Rechtsabteilung.

Die Ausgabe umfasst vier echte, bearbeitbare DOCX-Dateien und ein ZIP mit diesen Dokumenten, kein als Word-Datei umbenanntes HTML. Die Schreiben bleiben Entwürfe. Prüfen Sie Zuständigkeit, Interesse, Vollmacht, Nachweise, Kosten und Unterschrift vor einer Verwendung. Die vier Dokumente sind keine Aufforderung zu parallelen Anträgen. Die App versendet nichts und reicht nichts ein.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.4. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 2 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 2 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`auskunftsentwuerfe-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundstuecksrecherche/skills/auskunftsentwuerfe-vorbereiten/SKILL.md) | Bereitet in der Grundstücksrecherche-App vier Auskunftsentwürfe für Katasterbehörde, Grundbuchamt, Notariat und Rechtsabteilung als echte DOCX-Dateien und ZIP vor. Prüft Flurstücksangaben, Zweck und Nachweise; versendet nichts. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundstuecksrecherche/skills/auskunftsentwuerfe-vorbereiten/SKILL.md) |
| [`grundstuecksrecherche-starten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundstuecksrecherche/skills/grundstuecksrecherche-starten/SKILL.md) | Startet die lokale Grundstücksrecherche-App und begleitet Stadtsuche, verifizierte NRW-Katasterauswahl oder manuelle Flurstückserfassung. Erklärt fehlende Ausführungs- oder Browsermöglichkeiten ohne eine Einbettung vorzutäuschen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundstuecksrecherche/skills/grundstuecksrecherche-starten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

Ein einzelner Skill enthält weder App noch Python-Abhängigkeiten. Verwenden Sie für die Anwendung das vollständige Plugin-Verzeichnis.

<!-- decimal-anchor --> <a id="münster-referenz"></a>

## 1.5. Münster-Referenz

Die bisherige [Münster-Referenz](examples/nrw-muenster/reference/index.html) bleibt unter `examples/nrw-muenster/reference/index.html` unverändert und ausdrücklich separat ladbar. Öffnen Sie diese HTML-Datei nur auf Wunsch im Browser. Sie ist kein voreingestellter Fall der neuen App; ihre fest hinterlegten Beispielangaben und ihr bisheriger Export ersetzen nicht den neuen DOCX-Export.

<!-- decimal-anchor --> <a id="quellen-und-grenzen"></a>

## 1.6. Quellen und Grenzen

Die [Rechtsquellen](references/rechtsquellen.md) erläutern die fachlichen Grenzen. Ein Kartenbefund ersetzt keinen Grundbuchnachweis. Die Bezeichnung „verifiziert“ betrifft ein bestätigtes Katasterergebnis, nicht Eigentum oder ein zugesichertes Auskunftsrecht. Externe Karten- und Suchdienste benötigen Netzwerkzugriff; senden Sie keine Mandatsunterlagen oder Eigentümerdaten an öffentliche Suchdienste.

[Betrieb und Prüfung](references/betrieb-und-pruefung.md) beschreibt den technischen Prüfstand, die Dienstverfügbarkeit und die Grenzen des lokalen Betriebs.
