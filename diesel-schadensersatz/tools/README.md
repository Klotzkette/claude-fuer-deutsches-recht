# Werkzeuge

[Plugin-README](../README.md) | [Repository-Start](../../README.md) | [Download-Index](../../ASSET_INDEX.md) | [Skills](../skills/README.md) | [Fachquellen](../references/README.md) | [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/diesel-schadensersatz.zip)

Aktenstart, drei Recherchewerkzeuge und Rechtsstands-Cockpit bleiben mit der Python-Standardbibliothek nutzbar. Der Aktenstart vertieft die Textschichtprüfung mit installiertem `pypdf`; der beA-Paketprüfer sperrt ohne `pypdf` die Versandfreigabe, weil nur damit PDF-Objekt- und Stempeltiefenprüfung aktiv sind. Die internen Helfer `query_common.py`, `bgh_sources.py` und `bea_common.py` erzwingen striktes JSON, sichere Ausgaben, aktenzeichenfeste BGH-Links einschließlich amtlicher Dokumentvarianten sowie den Paketauftrag-/Manifest-/Freigabevertrag. Paketbauer und PDF-Stempel beziehen `pypdf` und `reportlab` aus der [`requirements.txt`](../../requirements.txt) des Zielrepositorys.

## Reproduzierbare Laufzeitumgebung

Die Befehle in dieser Datei werden aus der Wurzel von `claude-fuer-deutsches-recht` ausgeführt. Die lokale Umgebung wird ausschließlich aus der dort vorhandenen Root-`requirements.txt` aufgebaut; eine separate Release-Requirements-Datei ist nicht erforderlich.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Aktenstart in einem Befehl

[`diesel-aktenstart.py`](./diesel-aktenstart.py) in Version `1.2.0` inventarisiert einen Aktenordner rekursiv, ohne symbolischen Links zu folgen. Es liest reguläre Dateien größenbegrenzt und austauschungssicher, bildet SHA-256, erkennt exakte Dubletten, portable Namenskollisionen, Endungs-/Signaturwidersprüche, ausführbare Inhalte, aktive PDF-Marker und verdächtige ZIP-Container. Das JSON enthält keine absoluten Quellpfade und keinen Laufzeitstempel; Kategorien und Beweisrollen sind ausdrücklich nur Dateinamenheuristiken.

Die Standardgrenzen liegen bei 10.000 Dateisystemeinträgen, 200 MiB je Datei und 20 GiB Gesamtbestand. `--max-file-mib` und `--max-total-gib` dürfen diese Grenzen kontrolliert bis 1 GiB je Datei beziehungsweise 1 TiB gesamt anpassen; das Gesamtbudget greift vor dem Hashen. PDF- oder Office-Dateien oberhalb der 32-MiB-Tiefenprüfgrenze werden vollständig gehasht, aber ausdrücklich mit ausstehender Tiefenprüfung statt als technisch freigegeben ausgegeben.

PDF-Tiefenprüfungen laufen isoliert mit Zeit-, CPU-, Speicher-, Dateideskriptor-, Dateigrößen-, Parallelitäts- und Seitenlimit. CLI-Zahlen akzeptieren nur kanonische positive ASCII-Ganzzahlen; `--force` ohne `--output-dir` und `--format` zusammen mit einem Bundle-Ziel werden als Bedienfehler abgewiesen. Die Startkarte beginnt mit dem einheitlichen Kanzlei-Arbeitskopf; vorhandene fremde Dateien, Symlinks, Verzeichnisse oder Spezialobjekte werden auch mit `--force` nicht gelöscht.

```bash
.venv/bin/python diesel-schadensersatz/tools/diesel-aktenstart.py /pfad/zur/akte \
  --output-dir /pfad/zum/arbeitsordner/aktenstart
```

Das Bundle enthält `aktenstart-manifest.json` für Skill 01 und `aktenstart-startkarte.md` für die Sichtprüfung. Die Startkarte nennt jetzt direkt die drei Übergabeschritte und enthält den kopierfertigen Profi-Schnellstartauftrag; Bearbeiter müssen weder Skill noch Fallart bestimmen. Exitcode `0` bedeutet `STARTBEREIT`, `2` bedeutet `PRUEFUNG_NOETIG` oder `BLOCKIERT`, `1` bedeutet Aufruf- oder Systemfehler. Eine Blockierung betrifft das automatische Lesen; sie ist keine Aussage zum materiellen Beweiswert der Datei.

## Fünfjahreskorpus und kleine Modelle

[`diesel-fuenfjahre-query.py`](./diesel-fuenfjahre-query.py) filtert 135 Entscheidungen und Statusakten von EuGH bis LG/Verwaltungsgericht nach Ebene, Gericht, Aktenzeichen, Thema, Status, Richtung, Quellenrang und Verifikation. `--arbeitsset` liefert höchstens sechs ausgewogene Treffer einschließlich Gegenlinie und Verwendungsgrenze. Ohne Angabe werden höchstens 25 Treffer ausgegeben; `--limit 0` gibt alle aus. `--stats` zählt stets das vollständige Filterergebnis und wird nicht vom Ausgabelimit gekürzt.

## Rechtsstand vor der Arbeit prüfen

[`rechtsstand-monitor.py`](./rechtsstand-monitor.py) prüft lokal Korpusstand, neueste Sachentscheidung, Quellenränge und die individuellen Prüfdaten anhängiger Verfahren. `--strict` stoppt, sobald Korpus oder Statusprüfungen älter als die gewählte Grenze sind. Das Werkzeug ruft keine Websites ab und ersetzt deshalb nie die Live-Prüfung produktiv zitierter Fundstellen.

```bash
.venv/bin/python diesel-schadensersatz/tools/rechtsstand-monitor.py --strict --format markdown
.venv/bin/python diesel-schadensersatz/tools/rechtsstand-monitor.py --as-of 2026-08-26 --max-age-days 45 --format json
```

```bash
.venv/bin/python diesel-schadensersatz/tools/diesel-fuenfjahre-query.py --stats
.venv/bin/python diesel-schadensersatz/tools/diesel-fuenfjahre-query.py --query EA288 --arbeitsset --format markdown
.venv/bin/python diesel-schadensersatz/tools/diesel-fuenfjahre-query.py --ebene LG --quelle-rang A --format json
```

## Obergerichte, BGH und EuGH

[`diesel-rechtsprechung-query.py`](./diesel-rechtsprechung-query.py) filtert die kuratierte Matrix nach Ebene, Gericht, Aktenzeichen, Thema, Status, Richtung, Quellenart und Jahr. Standard sind 25 Treffer; `--limit 0` hebt nur das Ausgabelimit auf, nicht die Quellen- und Statushinweise.

```bash
.venv/bin/python diesel-schadensersatz/tools/diesel-rechtsprechung-query.py --stats
.venv/bin/python diesel-schadensersatz/tools/diesel-rechtsprechung-query.py --gericht Stuttgart --format markdown
.venv/bin/python diesel-schadensersatz/tools/diesel-rechtsprechung-query.py --thema Nutzungsanrechnung --status hoechstrichterlich --format json
```

## EA288-Instanzkorpus

[`ea288-corpus-query.py`](./ea288-corpus-query.py) filtert das anonymisierte Nutzermaterial nach Typ, Gericht, Aktenzeichen, Modell, Einrichtung, Norm, Jahr und Betrag. Alle drei Abfragen begrenzen Suchtexte, akzeptieren nur kanonische ASCII-Jahre und -Limits, kennzeichnen gekürzte sowie leere Ergebnisse einheitlich und beenden sich bei geschlossener Pipe ohne Traceback.

```bash
.venv/bin/python diesel-schadensersatz/tools/ea288-corpus-query.py --limit 0 --format json
.venv/bin/python diesel-schadensersatz/tools/ea288-corpus-query.py --gericht Stuttgart --einrichtung umgebungsdruck --format markdown
```

## beA-Paket und Anlagenstempel

[`bea-paket-bauer.py`](./bea-paket-bauer.py) ist der reguläre Einstieg für die Output-Produktion. Er validiert `bea-paketauftrag.json`, sperrt Quellen oder Pakete oberhalb von 200 MB vor dem vollständigen Einlesen, prüft den freigegebenen Hauptdokument-Hash und jeden Anlagen-Hash, stempelt nur Kopien und erzeugt atomar die vollständige Original-, Arbeits-, Versand- und Kontrollspur. Die technisch vollständige Eigenprüfung geschieht einmal vor der atomaren Veröffentlichung; ihr Bericht liegt bereits im veröffentlichten Paket. Das Ergebnis bleibt bis zur visuellen/inhaltsbezogenen Abnahme `FREIGABE_AUSSTEHEND`.

```bash
.venv/bin/python diesel-schadensersatz/tools/bea-paket-bauer.py bea-paketauftrag.json --output bea-paket
```

Inputvertrag und Beispiel: [`bea-paketauftrag.schema.json`](../assets/schemas/bea-paketauftrag.schema.json) und [`bea-paketauftrag-beispiel.json`](../assets/examples/bea-paketauftrag-beispiel.json). Der Paketbauer akzeptiert absichtlich nur finale PDFs und überschreibt weder Quellen noch vorhandene Zielordner.

[`bea-paket-pruefer.py`](./bea-paket-pruefer.py) kontrolliert das flache `versand/`-Verzeichnis auf genau ein Hauptdokument, lückenlose Anlagenfolge auch oberhalb von 99, ASCII-/Längenregeln, Auftrag/Manifest, Bezugnahmen, Fingerprint, hashgebundene Freigabe, stabil gelesene Dateien, tatsächliche PDF-Seitenzahlen, PDF-Kopf/-Ende, 1.000-Dateien-/200-MB-Grenze und erkennbare Scripts, Aktionen, eingebettete Objekte, Verschlüsselung oder Signaturhinweise. Unterordner, Zusatzdateien, Hashabweichungen, Unicode-Steuer-/Formatzeichen, Hardlink-Dubletten, symbolische Links und unplausibel zukünftige Produktions- oder Freigabezeiten sperren das Paket. Der Fingerprint bindet einschließlich `created_at` alle freigaberelevanten Manifestdaten.

```bash
.venv/bin/python diesel-schadensersatz/tools/bea-paket-pruefer.py bea-paket \
  --role K --anlagen-prefix K --start 12 \
  --expected-az "16 O 123/24" --report bea-paket/kontrolle/pruefbericht.json
```

Exitcode `0` bedeutet `VERSANDFERTIG`, `2` bedeutet `FREIGABE_AUSSTEHEND`, `1` bedeutet `NICHT_VERSANDFERTIG`. Ohne gültiges Paketmanifest kann ein bloß sauber benannter Ordner nie versandfertig werden. Die Freigabevorlage wird erst nach tatsächlicher visueller und anwaltlicher Kontrolle als `kontrolle/freigabe.json` vervollständigt; sie ist kein Signatur- oder Versandnachweis.

[`bea-anlagenstempel.py`](./bea-anlagenstempel.py) schreibt `Anlage K12` oder `Anlage B4` rechts oben auf eine neue Versandkopie und protokolliert Original-/Ausgabe-Hash. Es liest und hasht Quellen race-sicher und begrenzt, parst Ein- und Ausgabe strikt und sperrt Original-/Ausgabe-/Audit-Kollisionen, Hard- und Symlinks, Quellenänderungen, ungültige Rotation, übergroße Seiten, mehr als 5.000 Seiten, mehr als 200 MB, nicht endliche Layoutwerte sowie Signaturhinweise. Anlagenlabels erlauben 1 bis 6 ASCII-Großbuchstaben und eine Nummer von 1 bis 999999. Eine vollständig geprüfte Ausgabe wird atomar veröffentlicht; vorhandene Ausgabe- oder Auditdateien bleiben ohne das bewusst gesetzte `--force` unverändert.

```bash
.venv/bin/python diesel-schadensersatz/tools/bea-anlagenstempel.py original/Kaufvertrag.pdf \
  --label "Anlage K12" --output arbeit/01_Anlage_K12_Kaufvertrag.pdf \
  --audit kontrolle/K12_stempel.json
```

Jede gestempelte PDF muss anschließend gerendert und visuell auf verdeckte Inhalte, Vollständigkeit und Orientierung geprüft werden.

## Selbsttests

```bash
.venv/bin/python diesel-schadensersatz/tools/diesel-rechtsprechung-query.py --selftest
.venv/bin/python diesel-schadensersatz/tools/diesel-fuenfjahre-query.py --selftest
.venv/bin/python diesel-schadensersatz/tools/ea288-corpus-query.py --selftest
.venv/bin/python diesel-schadensersatz/tools/rechtsstand-monitor.py --selftest
.venv/bin/python diesel-schadensersatz/tools/diesel-aktenstart.py --selftest
.venv/bin/python diesel-schadensersatz/tools/bea-paket-pruefer.py --selftest
.venv/bin/python diesel-schadensersatz/tools/bea-paket-bauer.py --selftest
.venv/bin/python diesel-schadensersatz/tools/bea-anlagenstempel.py --selftest
```

Ausgaben sind Such- und Arbeitslisten. Vor Schriftsatzverwendung bleiben Volltext, Status, Folgeentwicklung, technische Vergleichbarkeit und konkrete Fahrzeugzuordnung zu prüfen.
