# Rechtsabteilung Forderungsmanagement Immobilienunternehmen

Vollständige Übernahme des Immobilienpakets aus Version **5.27.1** in die große Rechtssammlung. Das ursprüngliche Repository bleibt bestehen. Hier liegen die unabhängig nutzbare Marketplace-Fassung, beide Einzelprompts, alle zehn Testakten und eine unveränderte Vollkopie aller 373 getrackten Quelldateien. Git-Historie, Zugangsdaten und lokale Arbeitsausgaben gehören nicht zur Kopie.

## 1. Welchen Einstieg brauche ich?

| Aufgabe | Öffnen |
|---|---|
| Mietforderung, Kündigung, Mieterhöhung, Klage, Verteidigung, Kosten oder Vollstreckung bearbeiten | [Fachplugin mit 50 Skills](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md) |
| Dasselbe ohne Plugin-Installation bearbeiten | [Werkstatt](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-werkstatt.md) oder [Schnellstart](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-schnellstart.md) |
| Fachlich fertige Schriftsätze und Anlagen in ein technisches Versandpaket überführen | [beA-Begleitwerkstatt mit neun Skills](../../schriftsatzwerkstatt-bea/README.md) |
| Testen oder Schulung vorbereiten | [Zehn Fälle mit Gesamt-PDF, Arbeits-ZIP und Einzel-PDF-ZIP](./TESTAKTEN.md) |
| Herkunft, Vollständigkeit und abweichende Arbeitsfassung prüfen | [Dateiverzeichnis mit SHA-256](./herkunft.json) |

Für den ersten Fall genügt: `Hier ist die Akte. Gleiche Mietkonto, Zahlungen und Korrespondenz ab und erstelle das nächste erforderliche Schreiben.` Das Plugin liest zuerst, sichert Fristen und fragt nur nach entscheidenden Lücken. Für denselben Fall nicht zusätzlich beide Einzelprompts aktivieren.

## 2. Vollkopie und Paket

Die Vollkopie ist ein **Quellarchiv**, kein zusätzliches Plugin. Darin bleiben die ursprünglichen Pfade, Bezeichnungen, Prüfskripte, Testaktenquellen, Gesamt-PDFs, Anleitungen und Lizenzdateien unverändert. Alte private Downloadlinks im historischen Archiv sind Herkunftsdokumentation, nicht die Einstiege dieser Arbeitsfassung. Die neuen Einstiege und Akten liegen vollständig hier; kein Zugriff auf das private Repository ist zum Arbeiten erforderlich.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Zweck |
|---|---|
| [Vollständiger Quellstand v5.27.1](./quellstand-v5.27.1.zip) | Unveränderte Sicherung aller 373 Dateien; im entpackten Ordner beginnen. Kein Installations-ZIP. |
| [Angepasstes vollständiges Projektpaket](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/rechtsabteilung-immobilien-v445.33.1/rechtsabteilung-forderungsmanagement-immobilienunternehmen-vollstaendig.zip) | Beide Plugins, Prompts, zehn Akten in allen drei Formen, Herkunft und Originalquellstand. Kein weiteres Marketplace-Plugin. |

Die ältere Gesamtsammlung des großen Repositories enthält diese Übernahme noch nicht. Bis zum nächsten Komplettrelease ausschließlich die Projektdateien und die direkten Downloads dieser Komponente verwenden.

## 3. Was wurde angepasst?

- Neuer, unternehmensneutraler Produktname: **Rechtsabteilung Forderungsmanagement Immobilienunternehmen**. Kein fester Konzernname und keine aus dem Produktnamen abgeleitete Vollmacht.
- 50 Fachskills unverändert auffindbar unter ihren bisherigen Skill-IDs. Die Triage unterstellt keine zusätzliche Rechtsfachwirtqualifikation mehr; tatsächliche Rolle und Befugnis bleiben gesonderte Prüfungen.
- Zwei autarke Prompts außerhalb des Skill-Verzeichnisses. Kein gleichzeitiges Laden von Plugin, Werkstatt und Schnellstart und kein Rückverweis auf fehlende Skills im Einzelprompt.
- Rechtsquellen und technische Referenzen liegen in den jeweiligen Pluginpaketen. Rechtliche Aussagen wurden durch die Kopie nicht pauschal als neu geprüft gekennzeichnet.
- Die beA-Begleitwerkstatt bleibt inhaltlich neutral. Andere bereits vorhandene Versandplugins werden nicht überschrieben und nicht als zusätzliche Pflichtstation eingeführt.
- Testakten bleiben inhaltlich erhalten. Arbeits-ZIPs enthalten DOCX, XLSX und PDF; beide ZIP-Formen sind flach. Nur die im Zielrepository vorgeschriebene `README.txt` mit dem zweisprachigen Experimenthinweis kommt hinzu.

## 4. Grenzen und Pflege

Der Quellstand stammt vom 30.09.2026, die Übernahme vom 07.10.2026. Jede juristische Referenz nennt ihren eigenen Prüfstand. Das Kopierdatum ist kein neuer Rechtsprechungs- oder Gesetzesabgleich. Freigabe, Unternehmensbefugnisse, aktuelle Quellen, Signatur und Einreichung müssen im realen Fall kontrolliert werden. Die technischen Tests ersetzen weder einen Cowork-Praxistest noch die fachliche Abnahme.

Der Quellimport ist durch Prüfsumme und Dateiliste fixiert. Neue Änderungen erfolgen an den beiden aktiven Pluginverzeichnissen; die historische Vollkopie wird nicht still umgeschrieben. Ein neuer Quellstand erhält ein neues Archiv und eine dokumentierte Herkunft.

Reproduzierbarer Akten- und Paketbau aus dem Repository-Root:

```bash
uv run --with-requirements requirements.txt python scripts/build-rechtsabteilung-immobilien.py --cases
uv run --with-requirements requirements.txt python scripts/test-rechtsabteilung-immobilien.py
```

[Zur Startseite der Rechtssammlung](../../README.md) · [Downloadverzeichnis](../../ASSET_INDEX.md)
