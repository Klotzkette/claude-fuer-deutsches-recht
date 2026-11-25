# Rechtsabteilung Forderungsmanagement Immobilienunternehmen

Die interne Immobilien-Rechtsabteilung bearbeitet Mietforderungen, Mieterhöhungen, Klagen und Vollstreckung. Für die Arbeit stehen das Fachplugin, zwei eigenständige Prompts und die technische beA-Werkstatt zur Wahl. Neun Übungsfälle und der Berliner Mietspiegel dienen zur Einarbeitung. Das Quellarchiv v5.27.1 dokumentiert die Herkunft aller 373 getrackten Quelldateien.

## 1. Welchen Einstieg brauche ich?

| Aufgabe | Öffnen |
|---|---|
| Mietforderung, Kündigung, Mieterhöhung, Klage, Verteidigung, Kosten oder Vollstreckung bearbeiten | [Fachplugin für das Immobilien-Forderungsmanagement](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md) |
| Dasselbe ohne Plugin-Installation bearbeiten | [Werkstatt](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-werkstatt.md) oder [Schnellstart](../../rechtsabteilung-forderungsmanagement-immobilienunternehmen/rechtsabteilung-forderungsmanagement-immobilienunternehmen-schnellstart.md) |
| Fachlich fertige Schriftsätze und Anlagen in ein technisches Versandpaket überführen | [beA-Begleitwerkstatt mit neun Skills](../../schriftsatzwerkstatt-bea/README.md) |
| Testen oder Schulung vorbereiten | [Übungsfälle und Mietspiegel als Gesamt-PDF, Arbeits-ZIP und Einzel-PDF-ZIP](./TESTAKTEN.md) |
| Herkunft, Vollständigkeit und abweichende Arbeitsfassung prüfen | [Dateiverzeichnis mit SHA-256](./herkunft.json) |

Für den ersten Fall genügt: `Hier ist die Akte. Gleiche Mietkonto, Zahlungen und Korrespondenz ab und erstelle das nächste erforderliche Schreiben.` Das Plugin liest zuerst, sichert Fristen und fragt nur nach entscheidenden Lücken. Für denselben Fall nicht zusätzlich beide Einzelprompts aktivieren.

## 2. Vollkopie und Paket

Das **Quellarchiv** dokumentiert die Originalpfade, Bezeichnungen, Prüfskripte, Fallquellen, Gesamt-PDFs, Anleitungen und Lizenzen von v5.27.1. Git-Historie, Zugangsdaten und lokale Arbeitsausgaben sind ausgenommen. Die öffentlichen Arbeitsdateien und Downloads sind hier aufgelistet und ohne Zugriff auf das Herkunftsrepository nutzbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Zweck |
|---|---|
| [Vollständiger Quellstand v5.27.1](./quellstand-v5.27.1.zip) | Unveränderte Sicherung aller 373 Dateien; im entpackten Ordner beginnen. Kein Installations-ZIP. |
| [Angepasstes vollständiges Projektpaket](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/rechtsabteilung-immobilien-v445.33.1/rechtsabteilung-forderungsmanagement-immobilienunternehmen-vollstaendig.zip) | Beide Plugins, Prompts, zehn Akten in allen drei Formen, Herkunft und Originalquellstand. Kein weiteres Marketplace-Plugin. |

Für die vollständige Projektkopie einschließlich aller Arbeitsakten verwenden Sie das Projektpaket in der Tabelle.

## 3. Aufgaben und Arbeitsweise

- Für jeden Fall prüft die Rechtsabteilung Vermieterin, Unternehmenszugehörigkeit, Vertretung und Vollmacht anhand der Akte.
- Die Fachmodule erschließen die Arbeitsschritte von der Aufnahme bis zur Vollstreckung. Der Einstieg klärt die tatsächliche Rolle und die Befugnisse des Bearbeiters.
- Der Werkstatt-Prompt und der Schnellstart sind jeweils eigenständig. Für denselben Auftrag genügt ein Einstieg.
- Die Pluginpakete enthalten Rechtsquellen und technische Referenzen mit jeweils eigenem Prüfstand.
- Die beA-Begleitwerkstatt bereitet fachlich fertige Schriftsätze technisch für den Versand vor. Wählen Sie für ein Versandpaket einen Versandweg.
- Arbeits-ZIPs enthalten die Aktenstücke in ihren Originalformaten, darunter Word, Excel und PDF. Beide ZIP-Formen enthalten den zweisprachigen Experimenthinweis in der Datei `README.txt`.

## 4. Grenzen und Pflege

Der Quellstand datiert vom 30.09.2026. Die Herkunftsdokumentation führt den Import vom 07.10.2026. Für eine rechtliche Aussage ist der Prüfstand der jeweiligen Fachreferenz maßgeblich. Im realen Fall sind Unternehmensbefugnis, Rechtsquellen, Freigabe, Signatur und Einreichung gesondert zu prüfen.

Dateiliste und Prüfsumme erlauben den Abgleich mit dem dokumentierten Quellstand. Fachliche Pflege erfolgt in den beiden aktiven Pluginverzeichnissen. Jede archivierte Fassung hat ein eigenes Quellarchiv mit Herkunftsnachweis.

Reproduzierbarer Akten- und Paketbau aus dem Repository-Root:

```bash
uv run --with-requirements requirements.txt python scripts/build-rechtsabteilung-immobilien.py --cases
uv run --with-requirements requirements.txt python scripts/test-rechtsabteilung-immobilien.py
```

[Zur Startseite der Rechtssammlung](../../README.md) · [Downloadverzeichnis](../../ASSET_INDEX.md)
