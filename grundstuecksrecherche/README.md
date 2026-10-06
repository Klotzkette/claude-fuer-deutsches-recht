<!-- decimal-headings -->
<!-- decimal-anchor --> <a id="grundstücksrecherche"></a>

# 1. Grundstücksrecherche

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="lokale-app-starten"></a>

## 1.1. Lokale App starten

**Version:** `445.33.0`

Die Grundstücksrecherche ist ein App-only-Plugin mit zwei begleitenden Skills. Die Bedienoberfläche läuft im Browser über einen lokalen Python-Server. Die Plugin-Installation allein startet die App nicht. Eine native Einbettung in Cowork ist nicht garantiert.

Starten Sie im Verzeichnis `grundstuecksrecherche` mit Python 3 und einer virtuellen Umgebung:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r app/requirements.txt
python3 app/server.py --port 8765
```

Öffnen Sie anschließend [die lokale App](http://127.0.0.1:8765/). Ist der Port belegt, wählen Sie einen freien Port und passen die URL entsprechend an. Beenden Sie den Server im Terminal mit `Ctrl+C`. Stellen Sie den lokalen Dienst nicht öffentlich ins Netz.

Mit erlaubter Codeausführung und Browserzugriff kann der Skill `grundstuecksrecherche-starten` den Server starten und die App öffnen. Fehlt eine dieser Möglichkeiten, erläutert er die konkrete Grenze und den lokalen Startweg; er behauptet keine laufende oder eingebettete App.

[Plugin als ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundstuecksrecherche.zip) · [Plugin-Dateien](.) · [Repository](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/grundstuecksrecherche.md) · [Download-Index](../ASSET_INDEX.md)

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
