# Insolvenzrecht

Für Kanzlei, Insolvenzverwaltung und Sachbearbeitung: ein gemeinsamer Einstieg für die laufende Insolvenzarbeit und drei eigenständige Spezialwerkzeuge für Forderungen, Insolvenzgründe und Pläne.

[Repository-Start](../README.md) · [Plugin-Gruppen](../plugin-gruppen/README.md) · [Skills](../SKILLS.md) · [Prompts](../docs/werkstatt-und-schnellstart-coverage.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## 1. Vier Haupteinstiege

**Für einen allgemeinen Insolvenzfall starten Sie mit dem Hauptplugin Insolvenzrecht.** Es verbindet die anwaltliche Bearbeitung mit Insolvenzverwaltung, Sachbearbeitung und Berichtserstellung. Für eine der drei klar abgegrenzten Spezialaufgaben wählen Sie das jeweilige eigenständige Plugin.

| Einstieg | Damit bearbeiten Sie | Installation |
| --- | --- | --- |
| [Insolvenzrecht – gemeinsames Hauptplugin](../insolvenzrecht/README.md) | Allgemeine Mandatsbearbeitung, Verwaltung, Sachbearbeitung und Berichte in einem Arbeitsablauf. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzrecht-v445.35.4/insolvenzrecht.zip) |
| [Forderungsanmelder](../insolvenzforderungsanmeldungspruefung/README.md) | Forderungen aus Gläubigersicht anmelden oder aus Verwaltersicht prüfen; Belege, Rang und Tabellenstand bearbeiten. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzforderungsanmeldungspruefung.zip) |
| [Zahlungsunfähigkeits- und Überschuldungsprüfer](../zahlungsunfaehigkeits-und-ueberschuldungspruefer/README.md) | Aus Kontoauszügen, offenen Posten, Verträgen und Planungsunterlagen den Eintritt der Insolvenzgründe rekonstruieren. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/zahlungsunfaehigkeits-und-ueberschuldungspruefer-v1.2.0/zahlungsunfaehigkeits-und-ueberschuldungspruefer.zip) |
| [Insolvenzplan- und StaRUG-Planwerkstatt](../insolvenzplan-starug-planwerkstatt/README.md) | Insolvenzplan oder StaRUG-Restrukturierungsplan mit Vergleichsrechnung, Gruppen, Anlagen und Vollzug bearbeiten. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |

Der **Forderungsanmelder** heißt im technischen Plugin-Verzeichnis weiterhin `insolvenzforderungsanmeldungspruefung`. Die drei Spezialwerkzeuge bleiben eigenständig installierbar und erhalten eigene Werkstatt- und Mini-Prompts sowie Testakten.

## 2. Was das gemeinsame Hauptplugin übernimmt

Das Hauptplugin führt vom Akteneingang zum konkreten Arbeitsprodukt. Zu Beginn klärt es Rolle, Verfahrensstand, Auftrag und Fristen; danach wählt es die erforderlichen Fachmodule. So können Sie innerhalb derselben Bearbeitung zwischen anwaltlicher Prüfung, Verwalteraufgabe, Sachbearbeitung und Bericht wechseln.

| Arbeitsbereich | Typische Aufgabe |
| --- | --- |
| Allgemeines Insolvenzrecht | Sachverhalt und Insolvenzgründe einordnen, Antrag und Verfahrensfragen bearbeiten. |
| Anwaltliche Mandatsführung und Sanierung | Interessen, Haftungsfragen und Sanierungswege prüfen; Beratung und Schriftsätze vorbereiten. |
| Insolvenzverwaltung | Verfahren, Masse, Sicherheiten und Beteiligte bearbeiten. |
| Insolvenzsachbearbeitung | Unterlagen auswerten, Belege zuordnen, Korrespondenz und operative Schritte vorbereiten. |
| Berichte und Abschluss | Zwischen- und Schlussberichte, Schlussrechnung und Verteilung aus der Akte entwickeln. |

Die vier ergänzenden allgemeinen Bereiche sind als Fachmodule im Hauptplugin enthalten. Eine zusätzliche Installation ihrer bisherigen Einzelpakete ist dafür nicht erforderlich. Fachmodule, Quellenprüfung und Ergebnisdarstellung bleiben auf den konkreten Auftrag ausgerichtet.

## 3. Ergänzende Spezialangebote

Diese Werkzeuge ergänzen die vier Haupteinstiege bei einem besonderen Auftrag. Der **Insolvenzforderungen-Checker bleibt ein separates Angebot** zum Prüfen von Forderungsunterlagen; er ist kein eingebauter Bestandteil des Forderungsanmelders.

<details>
<summary>Spezialangebote anzeigen</summary>

| Spezialangebot | Damit bearbeiten Sie | Installation |
| --- | --- | --- |
| [Fortbestehensprognose](../fortbestehensprognose/README.md) | Fortbestehen anhand von Planung, Finanzierungsannahmen und Szenarien beurteilen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| [Insolvenzanfechtung](../insolvenzanfechtung/README.md) | Zahlungen und andere Rechtshandlungen aus Verwalter- oder Empfängersicht untersuchen; Anfechtungsschreiben und Klagen vorbereiten. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung.zip) |
| [Insolvenzforderungen-Checker](../insolvenzforderungen-checker/README.md) | Ergänzung zum Forderungsanmelder: eingehende Forderungsunterlagen, Belege, Beträge und Rang zu einem begründeten Prüfvorschlag zusammenführen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker.zip) |
| [Krisenfrüherkennung und StaRUG](../krisenfrueherkennung-starug/README.md) | Krisensignale, Handlungsbedarf und Verantwortlichkeiten systematisch erfassen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| [Liquiditätsplanung](../liquiditaetsplanung/README.md) | Zahlungsströme planen, Liquiditätslücken darstellen und Szenarien rechnen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |
| [US Bankruptcy Code](../us-bankruptcy-code/README.md) | US-amerikanische Verfahren und deren Schnittstellen zur deutschen Bearbeitung prüfen. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/us-bankruptcy-code.zip) |
| [Verbraucherinsolvenz und Schuldenbereinigung](../verbraucherinsolvenz-schuldenbereinigung/README.md) | Schuldenbereinigung und Verbraucherinsolvenz aus Schuldnersicht vorbereiten. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherinsolvenz-schuldenbereinigung.zip) |
| [Zwangsverwaltung](../zwangsverwaltung-zvg/README.md) | Immobilien und laufende Erträge im gesonderten Zwangsverwaltungsverfahren bearbeiten. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/zwangsverwaltung-zvg.zip) |

</details>

Die gerichtliche Perspektive finden Sie gesondert bei [Insolvenz- und Restrukturierungsgericht](../gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung/README.md). Dieses Gerichtsplugin gehört zur [Gerichtsgruppe](../gerichtsplugins/README.md).

## 4. Werkstatt, Mini-Prompt und Testakten

Ohne Plugin-Installation können Sie mit dem [Werkstatt-Prompt Insolvenzrecht](../insolvenzrecht/insolvenzrecht-werkstatt.md) oder dem [Mini-Prompt Insolvenzrecht](../insolvenzrecht/insolvenzrecht-schnellstart.md) arbeiten. Beide sind eigenständige Markdown-Dateien; sie stehen neben dem Plugin und sind keine zusätzlichen Skills.

Für spezielle Aufgaben und Übungsunterlagen öffnen Sie die jeweilige Anleitung:

- [Forderungsanmelder: Anleitung, Prompts und Testakten](../insolvenzforderungsanmeldungspruefung/README.md).
- [Zahlungsunfähigkeits- und Überschuldungsprüfer: Anleitung, Prompts und Testakten](../zahlungsunfaehigkeits-und-ueberschuldungspruefer/README.md), einschließlich der Fälle aus Cottbus, Zehlendorf und Prenzlau.
- [Insolvenzplan- und StaRUG-Planwerkstatt: Anleitung, Prompts und Testakten](../insolvenzplan-starug-planwerkstatt/README.md).
- [Insolvenzanfechtung: Anleitung und zugeordnete Übungsakten](../insolvenzanfechtung/README.md).

Die [zentrale Testaktenübersicht](../testakten/README.md) führt zu den Fallbeschreibungen und Downloads. Für die Arbeit ohne vorweggenommenes Ergebnis wählen Sie den dort beschriebenen Grundaktenordner im lebensnahen ZIP, soweit die jeweilige Akte ihn enthält. Hinweise zu Inhalt und Übungsstand stehen in der Aktenanleitung.

## 5. Bisherige Einzelpakete und bestehende Links

Für die allgemeine Arbeit ist das gemeinsame Hauptplugin der Einstieg. Die vier früher getrennt angebotenen allgemeinen Pakete bleiben für bestehende Installationen und gezielte Einzelverwendung erreichbar. Ihre Arbeitsbereiche sind zugleich im Hauptplugin gebündelt.

<details>
<summary>Bisherige allgemeine Einzelpakete anzeigen</summary>

| Einzelpaket | Arbeitsbereich im Hauptplugin | Bestehendes Einzelpaket |
| --- | --- | --- |
| [Fachanwalt Insolvenz- und Sanierungsrecht](../fachanwalt-insolvenz-sanierungsrecht/README.md) | Anwaltliche Mandatsführung und Sanierungsberatung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/fachanwalt-insolvenz-sanierungsrecht.zip) |
| [Insolvenzsachbearbeitung](../insolvenzsachbearbeitung/README.md) | Operative Aktenarbeit, Korrespondenz, Belege, Masse und Verteilung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzsachbearbeitung.zip) |
| [Insolvenzverwaltung](../insolvenzverwaltung/README.md) | Verfahrensführung aus Sicht von Verwaltung, Sachwaltung und vorläufiger Verwaltung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzverwaltung.zip) |
| [Insolvenzverwaltung – Berichtsersteller](../insolvenzverwaltung-berichtsersteller/README.md) | Zwischenbericht, Schlussbericht, Schlussrechnung und Verteilung. | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzverwaltung-berichtsersteller-v1.1.0/insolvenzverwaltung-berichtsersteller.zip) |

</details>

Dieses Fachverzeichnis umfasst **16 bestehende Fachplugins**, geordnet in vier Haupteinstiege, acht ergänzende Spezialangebote und vier bisherige allgemeine Einzelpakete. Das Gerichtsplugin ist separat verlinkt. Bestehende Quellpfade, Paketnamen und Downloadwege bleiben erhalten. Der Oberordner bündelt die Orientierung; das installierbare gemeinsame Paket heißt **Insolvenzrecht**.

Die [Installationshilfe](../INSTALLATION_EINFACH.md) erläutert die Verwendung der ZIP-Pakete. Alle einzelnen Pakete bleiben auch im [alphabetischen Gesamtkatalog](../README.md#was-ist-drin) auffindbar. Hinweise zu Nutzung und Verantwortung stehen in der [Haupt-README](../README.md).

## 6. English help

Choose the combined **Insolvency Law** plugin for general legal, administrator, casework and reporting tasks. Three tools remain separate: creditor claims, insolvency-ground reconstruction and insolvency/restructuring plans. Optional specialist tools and the four compatible legacy general packages are listed below the four main entry points. This directory is the topic overview; install the individual package linked above or use its standalone workshop or mini prompt.
