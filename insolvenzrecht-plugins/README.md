# Plugin-Gruppe Insolvenzrecht

[Hauptverzeichnis](../README.md) · [Skills](../SKILLS.md) · [Prompts](../docs/werkstatt-und-schnellstart-coverage.md) · [Downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) · [Testakten](../testakten/README.md)

## 1 Überblick

Diese Seite bündelt Insolvenz-, Sanierungs- und Krisenplugins als thematischen Einstieg. Sie ist selbst kein installierbares Plugin. Die einzelnen Plugins bleiben an ihren bestehenden Marketplace-Quellpfaden; diese Übersicht verschiebt keine Verzeichnisse und ersetzt kein Installationspaket.

## 2 Einstieg nach Rolle und Aufgabe

- Geschäftsführung und Beratung: `liquiditaetsplanung`, `fortbestehensprognose` und `krisenfrueherkennung-starug` für Planung und Krisenübersicht.
- Anwaltliche Mandatsbearbeitung: `insolvenzrecht` für den allgemeinen Einstieg und `fachanwalt-insolvenz-sanierungsrecht` für die spezialisierte Gesamtbearbeitung.
- Gläubiger: `insolvenzforderungsanmeldungspruefung` für Forderungsanmeldung und Tabellenprüfung.
- Insolvenzverwalter, Sachwalter und vorläufige Verwaltung: `insolvenzverwaltung` für die operative Verfahrensarbeit; `zwangsverwaltung-zvg` für die gesonderte Immobilienperspektive.
- Planbearbeitung: `insolvenzplan-starug-planwerkstatt` für Insolvenz- und Restrukturierungspläne.
- Privatpersonen und ehemals Selbstständige: `verbraucherinsolvenz-schuldenbereinigung` für Schuldenbereinigung und Verbraucherinsolvenz.
- Verfahren mit US-Bezug: `us-bankruptcy-code` für die US-amerikanische Perspektive.

Die gerichtliche Rolle bleibt davon getrennt: [Insolvenz- und Restrukturierungsgericht](../gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung/README.md). Ergänzende Einstiege bieten die [Rechtsberatungsstelle](../rechtsberatungsstelle/README.md), die [Selbstvertretung am Amtsgericht](../selbstvertreter-amtsgericht/README.md) und das [internationale Wirtschaftsrecht](../fachanwalt-internationales-wirtschaftsrecht/README.md).

## 3 Plugins von A bis Z

Die Tabelle ist alphabetisch nach den bestehenden Marketplace-Quellpfaden sortiert. Die Plugin-Links öffnen die jeweiligen Quelldokumentationen; die ZIP-Links führen zu den einzelnen Installationspaketen.

| Plugin | Schwerpunkt | Installation |
| --- | --- | --- |
| [`fachanwalt-insolvenz-sanierungsrecht`](../fachanwalt-insolvenz-sanierungsrecht/) | Spezialisierte anwaltliche Mandatsführung in Insolvenz und Sanierung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-insolvenz-sanierungsrecht.zip) |
| [`fortbestehensprognose`](../fortbestehensprognose/) | Fortbestehensprognose mit Planungsannahmen und Dokumentation. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| [`insolvenzforderungsanmeldungspruefung`](../insolvenzforderungsanmeldungspruefung/) | Forderungsanmeldung, Belegaufbereitung und Tabellenprüfung aus Gläubigersicht. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |
| [`insolvenzplan-starug-planwerkstatt`](../insolvenzplan-starug-planwerkstatt/) | Erstellung und Bearbeitung von Insolvenz- und Restrukturierungsplänen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |
| [`insolvenzrecht`](../insolvenzrecht/) | Allgemeiner Einstieg in die insolvenzrechtliche Fallbearbeitung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |
| [`insolvenzverwaltung`](../insolvenzverwaltung/) | Operative Verwalterpraxis mit Gutachten, Berichten und Verfahrensdokumentation. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzverwaltung.zip) |
| [`krisenfrueherkennung-starug`](../krisenfrueherkennung-starug/) | Krisenfrüherkennung und strukturierte Übersicht von Handlungsoptionen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| [`liquiditaetsplanung`](../liquiditaetsplanung/) | Liquiditätsplanung, Szenarien und tabellarische Auswertung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| [`us-bankruptcy-code`](../us-bankruptcy-code/) | US-amerikanische Insolvenzverfahren und grenzüberschreitende Bezüge. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/us-bankruptcy-code.zip) |
| [`verbraucherinsolvenz-schuldenbereinigung`](../verbraucherinsolvenz-schuldenbereinigung/) | Schuldenbereinigung und Verbraucherinsolvenz aus Schuldnersicht. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherinsolvenz-schuldenbereinigung.zip) |
| [`zwangsverwaltung-zvg`](../zwangsverwaltung-zvg/) | Zwangsverwaltung von Immobilien und Bezüge zum Insolvenzverfahren. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |

## 4 Quelldateien und Installationspakete

Das Quellverzeichnis eines Plugins enthält dessen Manifest, README, Skills und weitere Arbeitsdateien. Maßgeblich für den Skill-Bestand sind die vorhandenen Dateien unter `skills/<skill-name>/SKILL.md`; die aktuelle Übersicht steht im [Skill-Verzeichnis](../SKILLS.md). Es gibt keine zusätzlichen Schnellstart-Wrapper-Skills.

Ein installierbares Plugin-ZIP wird aus dem jeweiligen Marketplace-Quellpfad gebaut. Quellordner und ZIP haben nicht denselben Inhalt: Die eigenständigen Dateien `*-werkstatt.md` und `*-schnellstart.md` (Schnellstart- oder Mini-Prompts) sind keine Skills und bleiben ausdrücklich außerhalb des Plugin-ZIPs. Sie sind über die [Prompt-Übersicht](../docs/werkstatt-und-schnellstart-coverage.md) einzeln als Markdown verfügbar und können ohne Plugin-Installation verwendet werden.

Für die Installation dient das einzelne Plugin-ZIP aus den [Downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest); die [Installationshilfe](../INSTALLATION_EINFACH.md) erläutert den Einstieg. Die separat angebotenen Fallpakete stehen in der [Testakten-Übersicht](../testakten/README.md).

Für den Einstieg ein zur Aufgabe passendes Plugin auswählen und weitere Spezialplugins bei Bedarf ergänzen.

## 5 Nutzungshinweise

Die übergreifenden Hinweise zu experimenteller Nutzung, Verantwortung, Datenschutz und regulatorischer Einordnung stehen zentral in der [Haupt-README](../README.md). Diese Übersicht dient der Navigation und enthält keine eigene rechtliche Einordnung.

## 6 English Help

This page is a topic directory, not an installable plugin. Choose a role or topic in the alphabetical table, then open its README for skills and materials. Install an individual plugin ZIP from [downloads](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest), or use a standalone Markdown file from the [prompt index](../docs/werkstatt-und-schnellstart-coverage.md). Workshop and quick-start/mini prompts are not skills and are excluded from plugin ZIPs. See the [main README](../README.md) for usage context and the [case index](../testakten/README.md) for practice files.
