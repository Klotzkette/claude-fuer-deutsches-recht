# Marketplace und öffentliche Downloads

Die Prüfung vom 16. November 2026 erfasst den Katalog mit 311 aktiven Plugins, seine veröffentlichten Einzelpakete und die Downloadtabellen. Ausgangspunkt war der Commit [`b6f3df2149`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/commit/b6f3df21493250508646a385354447a9893c72ab). Für die Vergleichsprüfung der Prompt-Downloads war der tatsächlich öffentliche GitHub-Pages-Stand [`4f53df7bfc`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/actions/runs/43770613360) maßgeblich.

| Prüfung | Ergebnis |
| --- | --- |
| Verweise auf Release-Dateien in READMEs und Download-Index | 1.767 verschiedene Ziele nach der Korrektur, verteilt auf 59 öffentliche Releases. Dateiname, Veröffentlichungsstatus, Uploadstatus und positive Dateigröße bestätigt. |
| Ausdrückliche Release-Zuordnungen | 1.592 Ziele im [Routing-Register](../../../scripts/scoped-release-assets.json) im veröffentlichten Tagbestand gefunden. |
| Aktive Plugin-ZIPs | Alle 311 primären ZIPs ohne Anmeldung heruntergeladen. Größe und SHA-256 mit GitHub abgeglichen, ZIP-Prüfsummen kontrolliert und Namen sowie Versionen der enthaltenen Manifeste mit dem Katalog verglichen. Die Pakete enthalten insgesamt 3.153 Skill-Dateien. In 54 ZIPs waren beide Manifestformate enthalten. |
| Direktdownloads von Prompts über GitHub Pages | Alle 789 Markdown- und TXT-Dateien für Werkstatt, Schnellstart und Hauptproblem byteweise mit dem bereitgestellten Pages-Commit verglichen. Ein HTTP 503 war beim gezielten Wiederabruf behoben. |
| Testaktendownloads und Hinweise | Die Quellprüfung meldet 631 zentrale Akten, 5.679 Treffer in den Downloadseiten, 396 weitere Downloadgruppen und 29 HTML-Seiten. Deren 52 Release-Ziele sind vorhanden. Die vier umgeleiteten Einzel-PDF-ZIPs antworteten auch bei anonymem Abruf jeweils mit HTTP 200. |

Vier Einzel-PDF-ZIPs waren in der ersten Ausgabe des Begleitreleases veröffentlicht, während die Linkberechnung durch später hinzugekommene Akten auf die zweite Ausgabe verwies. Die Links zu Industrieanlage, Windpark Moorbach, Lagerleiterunfall und Unterhaltsberechnung verweisen jetzt auf den tatsächlich veröffentlichten Tag. Für insgesamt 344 bisher aus dem aktuellen Verzeichnisbestand errechnete historische Akten-Ziele fixiert das Routing-Register den aus GitHub belegten Tag.

Bei CISG verwies eine erzeugte Tabellenzeile auf zwei nie veröffentlichte Sammel-ZIPs. Der aktuelle Generator erzeugt die korrigierte Tabelle mit den drei vorhandenen, einzeln verlinkten Akten. Der Oberordner Insolvenzrecht verlinkt elf Plugins auf dieselben Paketstände wie deren eigene Einstiegsseiten.

Die Änderungen in `testakten/` betreffen ausschließlich Downloadadressen in vier Akten-READMEs und im zentralen Inhaltsverzeichnis. Aktenbestandteile und Archive stimmen mit dem Ausgangscommit überein.

## 1. Prüfung wiederholen

```sh
node scripts/validate-marketplace-import.mjs
python3 scripts/validate-readme-navigation.py
python3 scripts/validate-testakten-readme-downloads.py
python3 scripts/validate-public-downloads.py --github-cli
```

Der letzte Befehl nutzt die angemeldete GitHub CLI für das größere API-Budget. Er lehnt private Repositorys, Entwürfe, fehlende und unvollständige Uploads ab. Ohne Option bleibt der anonyme Abruf für einzelne Downloadseiten möglich. Paket- und Quellenprüfungen belegen die geprüften Dateien und ihre Erreichbarkeit. Ob ein bestimmtes Konto das Paket installieren und einen konkreten Arbeitsablauf ausführen kann, hängt zusätzlich von den Funktionen und Freigaben des jeweiligen Hosts ab.
