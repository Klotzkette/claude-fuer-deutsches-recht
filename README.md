# Claude für deutsches Recht

Mit diesen Plugins und Prompts für die deutsche Rechtspraxis können Kanzleien, Rechtsabteilungen und Berater Akten auswerten, Quellen prüfen und Verträge oder Schriftsätze entwerfen. Zum Ausprobieren stehen erfundene Fälle mit den zugehörigen Unterlagen bereit.

[Schnellstart](#schnellstart) · [Plugin-Katalog A–Z](#was-ist-drin) · [Skills](./SKILLS.md) · [Werkstatt-Prompts](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) · [Mini-Prompts](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) · [Testakten](./testakten/README.md) · [Installation](./INSTALLATION_EINFACH.md) · [Downloads](./ASSET_INDEX.md) · [English](#english-quick-guide)

## Schnellstart

| Was möchtest du tun? | Einstieg |
| --- | --- |
| Ein Fachgebiet regelmäßig in Claude nutzen | Wähle ein Paket im [Plugin-Katalog](#was-ist-drin). Die Installation für Claude Code steht direkt unter dieser Tabelle. |
| Eine einzelne Aufgabe im Chat erledigen | Öffne einen [Mini-Prompt](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) und gib ihn zusammen mit deinem Auftrag und den Unterlagen in den Chat ein. |
| Einen ganzen Vorgang bearbeiten | Ein [Werkstatt-Prompt](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) begleitet dich von der Akte bis zum Entwurf. Für Einzelfragen gibt es [Schwerpunkt-Prompts](./SCHWERPUNKTE.md). |
| Mit einer Übungsakte anfangen | Wähle einen Fall aus der [Workshop-Fallauswahl](./docs/grundakten-lebenswelt/README.md) oder den [Fachakten nach Rechtsgebiet](./docs/grundakten-lebenswelt/Fachakten.md). |

### Installation in Claude Code

Gib die beiden Befehle nacheinander in Claude Code ein. Der erste fügt den Marketplace hinzu, der zweite installiert beispielhaft das Plugin für Arbeitsrecht.

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht@klotzkette-german-legal-skills
```

Für ein anderes Paket ersetze `arbeitsrecht` durch den Namen aus dem [Plugin-Katalog](#was-ist-drin). Die Kennung hinter dem `@` gehört zum Marketplace.

<a id="für-einsteiger-schritt-für-schritt-anleitung"></a>

### Installation in Claude Cowork

1. Öffne im [Download-Index](./ASSET_INDEX.md) das gewünschte Plugin und lade das Einzel-ZIP herunter.
2. Lade dieses ZIP in der Plugin-Verwaltung von Claude Cowork hoch.
3. Öffne eine neue Aufgabe und wähle den passenden Skill. [Installationsanleitung für Einzelplätze und Organisationen](./INSTALLATION_EINFACH.md)

Für ChatGPT findest du den passenden Einstieg unter [Workspace, Desktop-App und Chat](#chatgpt-und-die-chatgpt-app). [Schnellstart in fünf Minuten](./QUICKSTART.md)

## Beispiel für den ersten Auftrag

Öffne die [ModeFuchs-Akte](./testakten/inkasso-zahlungsklage-modefuchs/README.md) und beginne mit den Unterlagen im Ordner `Grundakte`. Nenne die Rolle und das Ergebnis, das du brauchst.

> Ich vertrete die Anspruchstellerin. Gleiche Bestellung, Rechnung und Zahlungseingänge ab. Erstelle eine Forderungsübersicht mit Belegstellen und entwirf ein Schreiben zum noch offenen Betrag. Frage nach, wenn ein entscheidender Beleg fehlt.

## Alle vollständigen Listen von A bis Z

<!-- BEGIN HAUPTVERZEICHNIS (auto-generated) -->
| Bestand | Umfang | Kurzbeschreibung | Vollständige alphabetische Liste |
| --- | ---: | --- | --- |
| **Plugins** | 315 | Installierbare Fachpakete | [Katalog](#was-ist-drin) · [Downloads](./ASSET_INDEX.md) |
| **Skills** | 3189 | Arbeitsabläufe für einzelne Aufgaben | [Alle Skills](./SKILLS.md) · [Einzeldownloads je Plugin](./skills-index/) |
| **Werkstatt-Prompts** | 313 | Ausführliche Anweisungen für mehrstufige Vorgänge | [Werkstatt auswählen](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) |
| **Schnellstart-/Mini-Prompts** | 312 | Kurze Anweisungen für den Einstieg im Chat | [Mini-Prompt auswählen](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) |
| **Testakten** | 633 zentral / 661 gesamt | Übungsfälle mit Arbeitsaufträgen und Unterlagen | [Zentrale Sammlung](./testakten/README.md#verfügbare-akten) · [Akten einzelner Plugins](#testakten) |
<!-- END HAUPTVERZEICHNIS (auto-generated) -->

Die Prompt-Register zählen die Hauptdateien je Plugin. Zusätzliche Werkstätten gibt es unter anderem für die [neun HOAI-Leistungsphasen](./docs/bauwirtschaft-hoai-phasen.md) und die [Insolvenzanfechtung](./insolvenzanfechtung/werkstattprompts/README.md). Die [Hauptskills](./skills-index/README.md#hauptskills) führen durch einen ganzen Vorgang. Der [Werkstatt-Leitfaden](./docs/werkstatt-visualisierung.md) zeigt, wie sich Belege und Varianten bis zum Entwurf verfolgen lassen.

<details>
<summary>Weitere Werkstatt-Dateien</summary>

Werkstätten für [Betreuungsunterlagen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=betreuungsrecht/betreuungsrecht-unterlagen-werkstatt.md), [Insolvenzanfechtung im Fachanwaltsprofil](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachanwalt-insolvenz-sanierungsrecht/prompts/insolvenzanfechtung/insolvenzanfechtung-werkstatt.md), [Sachbearbeitung in der Verbraucherinsolvenz](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzsachbearbeitung/prompts/verbraucherinsolvenz/verbraucherinsolvenz-werkstatt.md) und [Umsatzsteuer-Voranmeldung](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=steuerrecht-anwalt-und-berater/ustva/werkstatt.md).

</details>

## Schwerpunkte für die deutsche Praxis

| Arbeitsbereich | Fachliche Einstiege |
| --- | --- |
| Verträge und Unternehmen | [Vertragserstellung](./vertragserstellung/README.md), [AGB-Werkstatt](./agb-werkstatt/README.md), [Corporate und M&A](./corporate-kanzlei/README.md), [Due Diligence](./due-diligence/README.md) |
| Arbeitsrecht und Altersversorgung | [Fachprofil Arbeitsrecht](./fachanwalt-arbeitsrecht/README.md), [Kündigungsschutzklage](./arbeitsrecht-kuendigungsschutzklagewerkstatt/README.md), [Betriebliche Altersversorgung im Konzern](./bav-strategie-konzern/README.md) |
| Verfahren und Schriftsätze | [Forderungsmanagement](./forderungsmanagement-klagewerkstatt/README.md), [Schriftsatz-Versand](./schriftsatz-versandwerkstatt/README.md), [15 Gerichts- und Staatsanwaltschafts-Plugins](./gerichtsplugins/README.md) |
| Immobilien, Bau und Vergabe | [Immobilienrecht](./immobilienrechtspraxis/README.md), [Bauunternehmer-Einkauf](./bauunternehmer-einkauf/README.md), [HOAI-Leistungsphasen](./docs/bauwirtschaft-hoai-phasen.md), [Bauvergabe](./bauvergabe/README.md) |
| Krise und Insolvenz | [16 eigenständige Insolvenz-Plugins](./insolvenzrecht-plugins/README.md), darunter [Forderungsanmelder](./insolvenzforderungsanmeldungspruefung/README.md), [Zahlungsunfähigkeits- und Überschuldungsprüfer](./zahlungsunfaehigkeits-und-ueberschuldungspruefer/README.md) und [Insolvenzplan- und StaRUG-Planwerkstatt](./insolvenzplan-starug-planwerkstatt/README.md) |
| Steuerrecht, Regulierung und Compliance | [Facheinstieg Steuerrecht](./fachanwalt-steuerrecht/README.md) mit dem [gemeinsamen Paket für Steueranwälte und Steuerberater](./steuerrecht-anwalt-und-berater/README.md), [Compliance im Großkonzern](./compliance-abteilung-grosskonzern/README.md), [KI-Governance](./ki-governance/README.md), [Geldwäscheprävention](./geldwaeschepraevention-aml-kyc/README.md) |
| Methode, Sprache und Ausbildung | [Methodenlehre](./methodenlehre-buergerliches-recht/README.md), [Zitierweise](./zitierweise-deutsches-recht/README.md), [Einfache und Leichte Sprache](./einfache-leichte-sprache-jura/README.md), [Jurastudium](./jurastudium/README.md) |

[Alle Fachanwaltsprofile](./_FACHANWALTSCHAFTS-PLUGINS/README.md) · [Plugin-Gruppen](./plugin-gruppen/README.md) · [Rechtsgebiete, Paketversionen und Skillzahlen](./references/rechtsgebiete-uebersicht.md) · [Klotzkettes kuratierte juristische Promptliste](./PROMPTLISTE.md)

## Testakten

Die [zentrale Sammlung](./testakten/README.md) lässt sich [nach Rechtsgebiet](./testakten/README.md#2-testakten-nach-thema-finden) durchsuchen. Jede Fallseite beschreibt den Sachverhalt, den Arbeitsauftrag und die verfügbaren Fassungen. Wähle pro Fall eine Fassung, damit Belege bei der Auswertung nur einmal gezählt werden.

| Fassung | Verwendung |
| --- | --- |
| Gesamt-PDF | Den Fall zusammenhängend lesen. |
| Einzel-PDF-ZIP | Einzelne Aktenstücke für die Prüfung auswählen. |
| Originalformat-ZIP | Mit bearbeitbaren Word-Dateien, Excel-Tabellen, E-Mails, Screenshots und anderen Originaldateien arbeiten. |
| Ordner `Grundakte` im Originalformat-ZIP, soweit vorhanden | Mit den Eingangsunterlagen beginnen. Weitere Verfahrensschritte und Übungsergebnisse lassen sich anschließend über die übrige Akte erschließen. |

<details>
<summary>Weitere Workshop- und Plugin-Akten</summary>

- [29 Workshopakten mit Beweisfragen und nachgereichten Unterlagen](./docs/releases/testakten-praxis-v1.0.0.md)
- Eigene Aktensammlungen führen außerdem das [Allgemeine Notariat](./allgemeines-notariat/testakten/README.md), der [Aktenanleger](./aktenanleger/testakten/README.md) und das [Umwandlungssteuerrecht](./umwandlungssteuerrecht/testakten/README.md).
- Pluginlokale Bestände der [Kündigungsschutzklagewerkstatt](./arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte/), des [Arbeitszeugnisgenerators](./arbeitszeugnisgenerator/testakte/), des [Arbeitszeugnisprüfers](./arbeitszeugnispruefer/testakte/), des [UN-Kaufrechts](./un-kaufrecht-cisg/testakte/) und der [Untersuchungshaft](./untersuchungshaft/testakte/)
- [Sieben Akten der Vergaberecht-Werkstatt](./vergaberecht-werkstatt/testakten/README.md) · [Übungsakten der Gerichts-Plugins über die Rollenübersicht](./gerichtsplugins/README.md) · [Weitere Beispielsammlungen](#weitere-unterlagen-zum-testen)

</details>

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

Das [Originalformat-ZIP der ModeFuchs-Akte](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-inkasso-zahlungsklage-modefuchs.zip) enthält die Belege für den [Beispielauftrag](#beispiel-für-den-ersten-auftrag).

## ChatGPT und die ChatGPT-App

| Arbeitsumgebung | Einstieg |
| --- | --- |
| ChatGPT-Workspace | Ein Workspace-Administrator importiert das öffentliche GitHub-Repository als Marketplace und prüft den Importbericht je Plugin. Als Quelle kommen `main` oder ein festgelegter Commit bzw. Tag infrage. [Workspace-Import](https://learn.chatgpt.com/docs/enterprise/plugin-management) |
| ChatGPT-Desktop-App mit Work oder Codex | Öffne das lokale Repository als Projekt und wähle im Plugin-Verzeichnis den Marketplace `klotzkette-german-legal-skills`. Für den Wechsel aus einer anderen Anwendung steht der Import in den Einstellungen zur Verfügung. [Lokale Marketplaces](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work) · [Desktop-Import](https://learn.chatgpt.com/docs/import) |
| Chat oder andere freigegebene Oberfläche | Verwende einen [eigenständigen Prompt](./docs/werkstatt-und-schnellstart-coverage.md) mit den für den Auftrag nötigen Unterlagen. |

Verfügbarkeit, Dateizugriff, Quellenzugänge und der Export von DOCX, PDF oder Excel hängen von Konto und Oberfläche ab. Die [Prüfung der Installations- und Ladewege](./quality/source-audits/2026-10-31-werkstatt/host.md) dokumentiert die getesteten Umgebungen. [Portabilität am eigenen Arbeitsplatz prüfen](./QUICKSTART.md#9-portabilität-im-eigenen-arbeitsplatz-prüfen)

## Überblick

| Kennzahl | Wert |
| --- | --- |
| **Plugins** | 315 |
| **Skills (SKILL.md)** | 3189 im Quellbestand |
| **Testakten** | 633 zentral / 661 gesamt |
| **Fachanwaltsprofile** | 24 |
| **Plugin-Version / Arbeitsstand** | `v445.35.3` als Basisversion des [Marketplace-Manifests](./.claude-plugin/marketplace.json). Die [Fachübersicht](./references/rechtsgebiete-uebersicht.md) nennt die jeweilige Version jedes Plugins. |

<details>
<summary>Sammelarchive und Prüfsummen vom 9. Oktober 2026</summary>

### Sammel-Downloads

Die Sammelarchive gehören zum veröffentlichten Bestand vom 9. Oktober 2026 mit 297 Plugins. Für ein bestimmtes Plugin, seinen Paketstand oder eine einzelne Akte führt der [Download-Index](./ASSET_INDEX.md) zum zugeordneten Download. [Release-Zuordnung und Prüfsummen](./docs/release-routing.md)

| Paket | Inhalt |
| --- | --- |
| [Plugin-Sammel-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-plugins-megazip.zip) | Einzelne installierbare ZIPs des Sammelstands. Das Archiv zuerst entpacken und daraus das gewünschte Plugin auswählen. |
| [Skill-Sammel-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-skills-markdown.zip) | Skilltexte, Markdown-Referenzen und Plugin-READMEs. Eigenständige Werkstatt- und Mini-Prompts stehen in ihren Verzeichnissen als Einzeldateien. |
| [Marketplace-Manifest des Sammelstands](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/marketplace.json) | Paketdefinition und relative Plugin-Pfade des Sammelstands. |
| [SHA-256-Prüfsummen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/checksums-sha256.txt) | Prüfsummen der veröffentlichten Dateien. |

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Paket | Inhalt |
| --- | --- |
| [Zentrale Akten in Originalformaten](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-testakten.zip) | Originalformat-ZIPs des Sammelstands. |
| [Zentrale Akten als Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-testakten-einzelpdfs.zip) | Einzel-PDF-ZIPs der zentralen Akten des Sammelstands. |
| [Pluginlokale Akten in Originalformaten](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-pluginlokalen-testakten.zip) · [als Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alle-pluginlokalen-testakten-einzelpdfs.zip) | Ergänzende Akten aus den Plugin-Ordnern des Sammelstands. |
| [Komplettpaket des Sammelstands](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/v445.35.3/alles-komplettpaket.zip) | Plugin-ZIPs, Skill-Markdown, Testakten, Marketplace-Manifest und Übersichten. |

</details>

## Berufsrecht, Datenschutz und technischer Einsatz

Die Sammlung ist ein technisches Experiment für fachlich kontrollierte Arbeitsabläufe. Prüfe Rechtsstand, Tatsachen, Fristen, Berechnungen und Quellen anhand der Originale, bevor du ein Ergebnis verwendest. Die rechtliche und technische Freigabe für echtes Mandatsmaterial liegt beim jeweiligen Nutzer. Dazu gehören insbesondere die anwaltliche Verschwiegenheit, der Dienstleisterzugang, die Auftragsverarbeitung, internationale Datenübermittlungen sowie die im konkreten Einsatz einschlägigen Anforderungen der KI-Verordnung. Für die Nutzung gilt ein Haftungsausschluss, soweit gesetzlich zulässig. Zwingende gesetzliche Haftung bleibt unberührt.

### Kontrollliste vor echtem Mandatsmaterial

Begrenze den Dateizugriff auf die erforderlichen Unterlagen. Prüfe erst mit einem erfundenen Fall, welchen Endpunkt die Oberfläche nutzt, welche Zugriffsrechte gelten und welche Dateien sie tatsächlich erzeugt. [Berufsrechtliche Vertragsprüfung für KI](./berufsrecht-ki-vertragspruefung/README.md) · [KI-Verordnung und Digital-Omnibus mit amtlichen Quellen](./references/digitaler-omnibus-2026.md)

<a id="eigene-schnittstelle-oder-zwischenanbieter-anbinden-stand-juli-2026"></a>

### Eigene Schnittstelle oder Zwischenanbieter anbinden

Die [Anleitung für Cowork mit EU-Gateway](./0_setup-cowork3p-eu-gateway/README.md) beschreibt den technischen Anschluss. Kläre vor dem Einsatz Zugang, Endpunkt, Hosting, Unterauftragnehmer, Löschfristen, Protokollierung und Widerrufsmöglichkeiten. Zugangsschlüssel gehören ausschließlich in den dafür vorgesehenen geschützten Zugang der jeweiligen Arbeitsumgebung.

## Verbindliche Zitierweise

Für entscheidungserhebliche Rechtsprechung sind Gericht, Entscheidungsform, Datum, Aktenzeichen und die konkrete Textstelle anhand einer überprüfbaren Quelle festzuhalten. Literaturfundstellen setzen bereitgestellte Quellen oder verifizierten Zugang voraus. Der Umfang einer gerichtlichen Entscheidung, die Rechtskraft im Einzelfall und eine etwaige gesetzliche Bindungswirkung sind gesondert zu prüfen. [Zitierweise](./references/zitierweise.md) · [Methodik](./references/methodik-buergerliches-recht.md) · [Leitentscheidungen als Rechercheeinstieg](./references/leitentscheidungen-anker.md)

### Formatstandard für erzeugte Dokumente

Verträge, Schriftsätze, Vermerke und Schreiben sind vollständig ausformuliert. Die Dokumente verwenden, soweit technisch möglich, **Times New Roman 11 pt** und eine dezimale Gliederung wie `1`, `1.1` und `1.1.1`. Vorrangige Formular-, Gerichts- und Mandantenvorgaben bleiben zu beachten.

## Weitere Unterlagen zum Testen

- [GVB Berlin – Reinigungsvergabe](./weitere-unterlagen/sektorenvergabe-gvb-berlin/README.md) bietet eine Reinigungsakte mit 48 Unterlagen und zehn einzeln verwendbare Markdown-Assistenten. [Installierbares Fachpaket](./gvb-reinigungsvergabe/README.md)
- [Forderungsmanagement im Immobilienunternehmen](./projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md) verbindet die Arbeit in der Rechtsabteilung mit [zehn Testakten](./projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/TESTAKTEN.md).
- [Vergaberecht-Werkstatt](./vergaberecht-werkstatt/README.md) bietet drei Arbeitsumgebungen für Vergabestelle, Bieter und Konkurrentenrechtsschutz. Für Bauleistungen gibt es die [Bauvergabe-Reihe](./bauvergabe/README.md) mit fünf Fachpaketen und zwei durchgehenden Bauakten.

Für Studium und Referendariat eignen sich die Beispielakten, Relationen und Urteilsentwürfe zur Übung und zur Kontrolle der eigenen Lösung. Bei Prüfungsleistungen gelten die Vorgaben der jeweiligen Prüfungsstelle zur zulässigen Nutzung und Kennzeichnung.

## Qualität und Mitwirkung

Das [Qualitätslabor](./QUALITY.md) dokumentiert Bestandsprüfungen, Quellenabgleiche und Modelltests mit ihrer jeweiligen Reichweite. [Rechtsprechungsprüfung der Werkstatt-Prompts](./quality/source-audits/2026-10-31-werkstatt/README.md) · [Vergleichsmethodik und Herkunft](./quality/upstream-legal/2026-11-16/README.md)

<a id="bitte-mit-testen-und-feedback-geben"></a>

Mit einer Testakte kannst du prüfen, ob ein Arbeitsablauf zu deinen Aufgaben und Quellenzugängen passt. Ein hilfreicher Fehlerbericht nennt Paket, Aufgabe, erwartetes Ergebnis und beobachtete Abweichung. Verwende dabei erfundene oder zur Veröffentlichung geeignete Beispieldaten. [Fehler melden](https://github.com/Klotzkette/claude-fuer-deutsches-recht/issues) · [Beitragsleitfaden](./CONTRIBUTING.md)

## Lizenz

Eigene Beiträge stehen nach Wahl unter **Apache License, Version 2.0** oder **MIT License** (`Apache-2.0 OR MIT`). [Lizenzhinweis](./LICENSE) · [Apache-2.0-Lizenz](./LICENSE-APACHE) · [MIT-Lizenz](./LICENSE-MIT) · [Notice](./NOTICE)

Anthropics Vorlage `claude-for-legal` steht seit dem Initialcommit unter der Apache License, Version 2.0. Für übernommenes Material gelten die Herkunfts- und Lizenzvermerke in den Dateien. [Lizenz der ursprünglichen Vorlage](https://github.com/anthropics/claude-for-legal/blob/d541734b08e67aae330a362b256d1eb6808a08f5/LICENSE)

[Changelog](./CHANGELOG.md) · [Veröffentlichungen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases)

## English Quick Guide

Plugins, focused skills and standalone prompts for working with German law. Use the collection to review records, check sources and draft contracts, pleadings and memos. The working material is mainly in German.

- **Install a plugin** for a field you work in regularly. Find the package in the [plugin catalogue](#was-ist-drin) and follow the [installation guide](./INSTALLATION_EINFACH.md) or the [ChatGPT setup guide](#chatgpt-und-die-chatgpt-app).
- **Use one skill** for a specific task. The [complete skill index](./SKILLS.md) links to per-plugin descriptions and individual Markdown files. Provide any references required by the skill.
- **Start with a prompt** if you want to work directly in a chat. Choose a [workshop prompt](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) for a detailed workflow or a [quick-start prompt](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) for a short entry point.
- **Practise with a case file.** Open the [case index](./testakten/README.md) and choose one format. Use the combined PDF for reading, the individual-PDF ZIP to select documents, or the original-format ZIP for spreadsheets, emails and editable files. Where available, start with the `Grundakte` folder for the intake documents.

The [download index](./ASSET_INDEX.md) identifies the release for each package. The aggregate archives cover the fixed collection dated 9 October 2026. File handling, source access and document export depend on your tools and workspace. Use fictitious material to test your setup and verify every substantive output before relying on it. The material is experimental and does not replace legal advice.

<a id="was-ist-drin"></a>

## Plugin-Katalog von A bis Z

Der Katalog enthält alle installierbaren Plugins des Haupt-Marketplaces. Öffne einen Buchstaben und wähle ein Paket. Jede Plugin-Seite erklärt den Einsatz und führt zu Skills, Prompts und Downloads. In der [Fachübersicht](./references/rechtsgebiete-uebersicht.md) stehen zu jedem Paket auch Version und Skillzahl.

<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->
Alphabetisch: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

<a id="a"></a>
<details>
<summary>A</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`agb-recht-pruefer`](./agb-recht-pruefer) | Gigantischer AGB-Rechtsprüfer und Klausel-Entwerfer für deutsches Recht: Paragrafen 305 bis 310 BGB, UKlaG, B2C/B2B, Branchen-AGB, Redlining, Klauselrisiko und rechtssichere Entwurfsworkflows. |
| [`agb-werkstatt`](./agb-werkstatt) | AGB für Shop, Werkstatt, Handel, Banken und Darlehen entwerfen und prüfen. Zehn Fachskills und ein Hauptskill verbinden aktuelle Quellen, Interessenlage, vollständige Klauseln und konkrete Einführung. |
| [`aktenanleger`](./aktenanleger) | Bereitet Aktenanlagen in Anwaltskanzlei, Anwaltsnotariat und Nurnotariat vor. Ordnet Eingangspost, Beteiligte, Auftrag, Fristen, Vorbefassung und getrennte Zugriffsrechte zu. |
| [`aktenaufbereiter-strafrecht`](./aktenaufbereiter-strafrecht) | Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergänzbar. Erkennt Lücken und Widersprüche. Kein Ersatz für Aktenlektüre. |
| [`aktenauszug-gerichtsverfahren`](./aktenauszug-gerichtsverfahren) | Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivorträge Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten. |
| [`aktienrecht-hauptversammlung-ag-se`](./aktienrecht-hauptversammlung-ag-se) | Hauptversammlungs-Vorbereiter, Leitfaden-Ersteller und Durchführungsplugin für kleine AG, normale AG, börsennotierte AG und SE: Einberufung, Tagesordnung, virtuelle HV, Q&A, Abstimmung, Niederschrift, Anfechtungsrisiko und Post-HV. |
| [`allgemeines-notariat`](./allgemeines-notariat) | Amtsgeschäfte deutscher Notarinnen und Notare von der ersten Anfrage bis zum Vollzug. Zehn Skills für Grundstücke, Nachfolge, Vorsorge, Erbausschlagung, Vereinsregister und GmbH-Anteile. |
| [`anlagen-zu-schriftsaetzen`](./anlagen-zu-schriftsaetzen) | Gerichtsprozess-Dokumentenproduktion bis zur beA-fertigen Versandmappe: liest Schriftsatz und Anlagenordner, führt K/B/AST/AG fort, konvertiert und stempelt jede PDF-Seite, prüft ERVV, Signatur, Dateinamen, Empfänger und Eingang und liefert Verzeichnis, Manifest und Freigabevermerk. |
| [`antidiskriminierung-agg`](./antidiskriminierung-agg) | Antidiskriminierung nach dem AGG: Bewerbungen, Arbeitsbedingungen, Beschwerden, Wohnraum und Dienstleistungen prüfen. Zehn Workflows verbinden Fristen, Indizien, Rechtfertigung und konkrete Schreiben mit kultursensibler Sachverhaltsaufnahme. |
| [`anwaltschaft-generell`](./anwaltschaft-generell) | Anwaltschaft - Mandate im Alltag: zehn Skills für wirtschaftsrechtliche Dokumentarbeit vom belegten Aktenstand über Ansprüche, Verträge, Arbeit und Datenschutz bis zum Schreiben, Vergleich oder Schriftsatz. |
| [`apothekenrecht`](./apothekenrecht) | Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance. |
| [`arbeitsrecht`](./arbeitsrecht) | Arbeitsrechtliche Workflows für Kündigung, Befristung, Urlaub, AGG, Aufhebungsvertrag, Betriebsrat, Arbeitszeit, Lohn und Expansion. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle verwendet. |
| [`arbeitsrecht-kuendigungsschutzklagewerkstatt`](./arbeitsrecht-kuendigungsschutzklagewerkstatt) | Kündigungsschutzklagen und Arbeitgeberverteidigung vom Zugang bis zum Vergleich oder Urteil: zehn Fachskills und ein Hauptskill für Fristen, Anträge, Kündigungsgründe, Beweise, Weiterbeschäftigung und Vergütung. |
| [`arbeitszeugnisgenerator`](./arbeitszeugnisgenerator) | Erstellt, prüft und berichtigt einfache, qualifizierte, Zwischen- und Ausbildungszeugnisse aus vorhandenen Unterlagen. Verknüpft Tätigkeitsbild, Tatsachenbelege, Beweislast, klare Formulierungen, Vergleich und Vollstreckung zu einem verwendbaren Arbeitsprodukt. |
| [`arbeitszeugnispruefer`](./arbeitszeugnispruefer) | Prüft Arbeitszeugnisse aus Arbeitnehmersicht: gezielte Rückfragen, vertiefte Rechtsprechung, belegbare Änderungen, kurzer Mandantenbrief und passendes Arbeitgeberschreiben. Führt den Fall bis zur Kontrolle der Neufassung; auch für Chat und Word ausgearbeitet. |
| [`aufsichtsrat-ag-se-praxis`](./aufsichtsrat-ag-se-praxis) | Praxisplugin für Aufsichtsräte in AG und SE: Überwachung, Informationsrechte, Vorstand bestellen/abberufen, Vergütung, Ausschüsse, Protokoll, Business Judgment, Haftungsvermeidung, Börse, SE und Mitbestimmung. |
| [`aussenwirtschaft-zoll-sanktionen`](./aussenwirtschaft-zoll-sanktionen) | Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen. |

</details>

<a id="b"></a>
<details>
<summary>B</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`bank-rechtsabteilung`](./bank-rechtsabteilung) | Rechtsabteilung einer mittelgroßen deutschen Bank: Aufsicht, Kredit, Avale, Bürgschaft, Garantien, Trade Finance, ZAG/PSD2, PSD3/PSR-Vorschau, eWpG, MiCAR, Tokenisierung, BaFin, Vorstand, HV und Kanzleisteuerung. |
| [`barrierefreiheit-web-checker`](./barrierefreiheit-web-checker) | Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2.0, EN 301 549 und WCAG: Scope, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Abnahme. |
| [`bautraegervertrag-pruefer`](./bautraegervertrag-pruefer) | Prüft Bauträgerverträge aus Erwerber-, Bauträger-, GdWE- und Verwaltersicht: Bausoll, MaBV-Raten, Sicherheiten, Eigentum, Abnahme, Mängel, Verjährung und Sonderkonstellationen. Zehn Arbeitswege verbinden beide Fachbibliotheken und alle bisherigen Testakten. |
| [`bauunternehmer-einkauf`](./bauunternehmer-einkauf) | Arbeitswerkstatt für Projekt- und Zentraleinkauf im Bau: 14 Skills von KI-Einstieg, Aktenauswertung, Leistungsverzeichnis und Preisrecherche über GAEB, Angebotsvergleich und Verhandlung bis Vertrag, Lieferung und Nachtrag. Mit zehn erhaltenen Einkaufsakten. |
| [`bauvergabe-bieter`](./bauvergabe/bauvergabe-bieter) | Bauvergabe Bieter für öffentliche Bauaufträge mit zehn Fachskills und einem Hauptskill vom konkreten Auftrag zum vollständigen Arbeitsergebnis. |
| [`bauvergabe-nachtragsmanagement`](./bauvergabe/bauvergabe-nachtragsmanagement) | Zehn Fachskills und ein Hauptskill für Auftragnehmer nach dem Zuschlag: Nachtragsgrund, Preise, Bauzeit, Abrechnung, Sicherung und getrennte Prüfung öffentlicher Auftragsänderungen. |
| [`bauvergabe-rechtsschutz`](./bauvergabe/bauvergabe-rechtsschutz) | Bauvergabe Rechtsschutz für öffentliche Bauaufträge mit zehn Fachskills und einem Hauptskill vom konkreten Auftrag zum vollständigen Arbeitsergebnis. |
| [`bauvergabe-unterlagen`](./bauvergabe/bauvergabe-unterlagen) | Zehn Fachskills und ein Hauptskill zur Erstellung von Bauvergabeunterlagen. Eigenständige Bauprüfung nach VOB/A mit Quellen und präzisen Fachschnittstellen. |
| [`bauvergabe-verfahren`](./bauvergabe/bauvergabe-verfahren) | Zehn Fachskills und ein Hauptskill zur Führung eines Bauvergabeverfahrens. Eigenständige Bauprüfung nach VOB/A mit Quellen und präzisen Fachschnittstellen. |
| [`bauwirtschaft`](./bauwirtschaft) | 29 Arbeitsabläufe für Bauherren, Projektentwicklung, Bauleitung und kaufmännische Teams: neun eigene HOAI-Phasen für Gebäude und Innenräume sowie Projektsteuerung, Vergabe, Bauausführung und Buchhaltung. |
| [`bauwirtschaft-anfaenger`](./bauwirtschaft-rundum/bauwirtschaft-anfaenger) | Acht Skills für den Einstieg am Bau: Begehung, LV-Abgleich, Bieterfragen, Behinderungsanzeige und Baugrundgutachten. Mit sicheren Projektquellen und einem eigenen prüfbaren Bau-Baustein. |
| [`bauwirtschaft-fortgeschrittene`](./bauwirtschaft-rundum/bauwirtschaft-fortgeschrittene) | Acht Skills für fortgeschrittene Baupraxis: Rechnungen, VgV-Bewerbungen, Angebote, Bauzeit-Claims, Nachträge, Planänderungen und geprüfte Bürostandards mit begrenzten Dateizugriffen und menschlicher Freigabe. |
| [`bav-strategie-konzern`](./bav-strategie-konzern) | Betriebliche Altersversorgung im Konzern: Versorgungsordnungen und Besitzstände prüfen; Harmonisierung, Carve-out, CTA, Rentnergesellschaft und Pensionskassenkürzung anhand belegter Unterlagen gestalten. |
| [`bea-versand`](./bea-versand) | Ein Skill für die beA-Versandvorbereitung beliebiger Dokumente: Anlagen aus Inhalt und Kontext zuordnen, PDF-Kopien erzeugen, erste Anlagenseiten stempeln und Dateien passend benennen. Mit einem Werkstatt-Prompt und der Modefuchs-Testakte. |
| [`beamtenrecht`](./beamtenrecht) | Beamtenrecht für Bund, Länder und Richterdienst: Status, Laufbahn, Besoldung, Versorgung, Konkurrentenstreit, Disziplinarrecht, Dienstunfähigkeit, Richterlaufbahn, Landesrecht und verständliche Mandatsführung. |
| [`bereicherungs-und-anfechtungsrecht-pruefer`](./bereicherungs-und-anfechtungsrecht-pruefer) | Mechanisches Durchprüfen von Bereicherungsrecht Paragrafen 812 ff. BGB, AnfG und Insolvenzanfechtung Paragrafen 129-147 InsO. Mit KI-Screening von Schuldnerakten, Paragraf 135 Gesellschafterdarlehen, Bargeschäft Paragraf 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung. |
| [`berichtspflichten-erlediger`](./berichtspflichten-erlediger) | Berichtspflichten-Erlediger für mittelständische Unternehmen: amtliche Statistik, Portale, Umwelt-, Produkt-, Steuer-, Sozial-, Lieferketten-, Datenschutz- und Aufsichtsmeldungen mit Fristenboard, Datenquellen, Plausibilitätscheck und Behördenkommunikation. |
| [`berliner-asog-polizeirecht`](./berliner-asog-polizeirecht) | Berliner Polizei- und Ordnungsrecht aus Betroffenensicht: Gefahrenabwehr, Identitätskontrolle, Platzverweis, Gewahrsam, Durchsuchung, Sicherstellung, Polizeidaten, Vollstreckung und Rechtsschutz. Zehn Fachskills und ein Hauptskill. |
| [`berliner-gewerbeaufsicht-betrieb`](./berliner-gewerbeaufsicht-betrieb) | Berliner Gewerbeaufsicht aus Betreiber- und Beratungssicht: Restaurant, Späti und radiologischer Betrieb. Zehn Fachskills und ein Hauptskill für Anzeigen, Erlaubnisse, Hygiene, Kontrolle, Arbeitsschutz, Strahlenschutz und konkrete Behördenantworten. |
| [`berliner-hochschulrecht-professoren`](./berliner-hochschulrecht-professoren) | Berliner Hochschulrecht aus Sicht von Professorinnen und Professoren: Berufung, Zusagen, Status, Forschungsfreiheit, Ausstattung, Lehre, Gremien, Drittmittel, Nachwuchs und Rechtsschutz. Zehn Fachskills und ein übergreifender Hauptproblem-Skill. |
| [`berliner-schulrecht-eltern-schueler`](./berliner-schulrecht-eltern-schueler) | Berliner Kita- und Schulrecht ausschließlich aus Eltern- und Schülersicht. Zehn Fachskills und ein Hauptskill führen Aufnahme, Schulwechsel, Bewertung, Förderung, Betreuung und Rechtsschutz bis zum ausformulierten Ergebnis. |
| [`berliner-versammlungsrecht`](./berliner-versammlungsrecht) | Berliner Versammlungsrecht für Veranstaltende und Teilnehmende: Anzeige, Kooperation, Route, Auflagen, Gegenversammlung, Protestcamp, Leitung, Polizeimaßnahmen und Rechtsschutz. Zehn Fachskills und ein Hauptskill. |
| [`berufsgerichtliche-verfahren-freie-berufe`](./berufsgerichtliche-verfahren-freie-berufe) | Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel. |
| [`berufsrecht-anwaelte`](./berufsrecht-anwaelte) | Plugin für anwaltliches Berufsrecht: BRAO, BORA, FAO, beA, Kanzleisitz, Werbung, Interessenkollision, Verschwiegenheit, KI-/Cloud-Outsourcing, Schatten-KI, Berufsausübungsgesellschaft, Gebühren, Kammeraufsicht und anwaltsgerichtliche Risiken. |
| [`berufsrecht-ki-vertragspruefung`](./berufsrecht-ki-vertragspruefung) | Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit Legal-AI-Anbietern: Paragraf 43e BRAO, Paragraf 203 StGB, Consumer-Tool-Abgrenzung, No-Training, Telemetrie, Drittstaat, KI-VO-Rollen, Art.-50-Transparenz, Schatten-KI und Klauselvorschläge. |
| [`berufsrecht-notare`](./berufsrecht-notare) | Plugin für Notarrecht: BNotO, BeurkG, DONot, Dienstaufsicht, Urkundspflichten, Neutralität, Verwahrung, Amtspflichten, Vertreter/Verwalter, Disziplinarverfahren und notarielle Berufspraxis. |
| [`berufsrecht-patentanwaelte`](./berufsrecht-patentanwaelte) | Plugin für Patentanwaltsrecht: PAO, Patentanwaltskammer, Vertretungsbefugnis, Schutzrechtsmandate, Verschwiegenheit, Interessenkollision, Werbung, Berufsausübungsgesellschaft und berufsgerichtliche Risiken. |
| [`berufsrecht-steuerberater`](./berufsrecht-steuerberater) | Plugin für Steuerberaterrecht: StBerG, BOStB, Steuerberaterkammer, Vorbehaltsaufgaben, Werbung, Verschwiegenheit, Gebühren, Geldwäsche, Berufsgericht, Berufsausübungsgesellschaft und Haftungsprävention. |
| [`berufsrecht-wirtschaftspruefer`](./berufsrecht-wirtschaftspruefer) | Plugin für Wirtschaftsprüferrecht: WPO, Berufssatzung, WPK, APAS, Unabhängigkeit, Qualitätskontrolle, Abschlussprüfung, Bestätigungsvermerk, PIE, Berufsaufsicht und berufsgerichtliche Risiken. |
| [`betaeubungsmittelrecht`](./betaeubungsmittelrecht) | Betäubungsmittelrecht-Plugin für BtMG, BtMVV, KCanG/MedCanG-Schnittstellen, Strafverfahren, Therapie, ärztliche Praxis, Apotheken und Compliance. |
| [`betreuungsrecht`](./betreuungsrecht) | Betreuungsrechtliche Skills für ehrenamtliche Familienbetreuer, Berufs- und Vereinsbetreuer: Kaltstart, Scan-Akte, Kalender, Gerichtskommunikation, Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Wunschermittlung, Kontoanalyse und Schutzplan nach BtOG und BGB. |
| [`betriebskosten-hausverwaltung`](./betriebskosten-hausverwaltung) | Betriebskosten für Mietshaus und vermietete Eigentumswohnung: zehn Skills von Belegen, Kostenabgrenzung und Heizkosten bis zur nachrechenbaren Abrechnung oder zum Antwortbrief. |
| [`bgb-at-pruefer`](./bgb-at-pruefer) | Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, Anfechtung, Stellvertretung, Fristen, Verjährung und Routing für digitale Elemente, Update- und Reparaturrecht. |
| [`bgb-bt-pruefer`](./bgb-bt-pruefer) | Großer BGB-BT-Prüfer für Schuldrecht Besonderer Teil: Kauf einschließlich Verbrauchsgüterkauf, Waren mit digitalen Elementen, Updatepflichten und Right-to-Repair-Schnittstellen, außerdem Miete, Werk, Bürgschaft, GoA, Bereicherung, Delikt und Rückabwicklung. |
| [`bieter-unternehmen`](./vergaberecht-werkstatt/bieter-unternehmen) | Bieter legen Vergabeunterlagen, Unternehmensdaten oder Portalexport ab und starten ohne Skillwahl. Das Plugin sichert Fristen, Nachweise, Qualitätsvorsprung, Angebotsfreeze, Upload, Rüge, VK und OLG. |
| [`buerokratieversteher-entbuerokratisierer`](./buerokratieversteher-entbuerokratisierer) | Allgemeiner Bürokratieversteher und Entbürokratisierer für Laien, Menschen mit Deutsch als Zweitsprache und alle, die Bescheide, Anträge, Vorladungen, Behördenbriefe, Jugendamt-, Schul-, Bau-, Sozial-, Familien- oder Kommunalverfahren verstehen und vorsichtig bearbeiten wollen. |
| [`bundesnetzagentur-verfahren`](./bundesnetzagentur-verfahren) | Großes Regulierungs-Plugin für anwaltliche Arbeit mit der Bundesnetzagentur in Energie, Telekommunikation, Post, Eisenbahn und Digital Services. |
| [`bundeswehrrecht-wehrrecht`](./bundeswehrrecht-wehrrecht) | Super-Plugin für Soldatenrecht, Wehrbeschwerde, Disziplinarrecht, Wehrpflicht, Reservisten, Versorgung und Bundeswehrverwaltung. |

</details>

<a id="c"></a>
<details>
<summary>C</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`commercial-courts-deutschland`](./commercial-courts-deutschland) | Commercial-Courts-Plugin für englischsprachige Wirtschaftsverfahren in Deutschland: Zuständigkeit, Wahlklauseln, Klage, Case Management, Beweis, Geheimnisschutz, Wortprotokoll/Transcript, Rechtsmittel, BGH, Kosten, Vollstreckung und bilingualer Schriftsatz-/Hearing-Workflow. |
| [`common-law-kompass`](./common-law-kompass) | Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| [`compliance-abteilung-grosskonzern`](./compliance-abteilung-grosskonzern) | Interne Rechts- und Compliance-Abteilung im Industriekonzern: KI-Einsatz, Richtlinien, Meldungen, Untersuchungen, Geschäftspartner, Konzernkontrollen und Organvorlagen fallbezogen bearbeiten. |
| [`corporate-contract-law`](./corporate-contract-law) | Corporate Contract Law - Wirtschaftsverträge: zwanzig Skills für deutsche B2B-Vertragsgestaltung vom Geschäftsauftrag über den vollständigen Vertrag und die Verhandlung bis zum unterschriftsreifen Entwurf. |
| [`corporate-kanzlei`](./corporate-kanzlei) | Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI. |

</details>

<a id="d"></a>
<details>
<summary>D</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`datenbankrecht`](./datenbankrecht) | Großes Plugin zum deutschen und europäischen Datenbankrecht: UrhG Paragrafen 87a ff., Datenbankrichtlinie, Investitionsschutz, automatisiertes Auslesen, API, Training digitaler Systeme, Vertrags- und Plattformkonflikte. |
| [`datenschutz-sanktionsverfahren-verteidigung`](./datenschutz-sanktionsverfahren-verteidigung) | Spezialplugin für Vertretung und Verteidigung in datenschutzrechtlichen Sanktionsverfahren: DSGVO-Bußgeld, OWiG/StPO, Art.-58-Anordnung, Verwaltungsgericht, Aufsichtsbehördenkommunikation, EuGH/EDPB und Behördenstrategie. |
| [`datenschutzrecht`](./datenschutzrecht) | DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review, Auskunft Art. 15, Datenpanne Art. 33/34, Drittlandstransfer Art. 44 ff. inkl. US-Transfer, DPF, SCC, TIA, Behördenpaket und Brückenskills zur Sanktionsverteidigung. |
| [`denkmalschutzrecht`](./denkmalschutzrecht) | Denkmalschutzrecht in Deutschland: Art. 14 und Art. 70 GG als bundesstaatlicher Rahmen plus alle sechzehn Landesgesetze. Skills für Eintragung Erlaubnis Bußgeld steuerliche Förderung nach Paragraf 7i EStG und Welterbestätten — länderübergreifende Grundlagen und Landesrecht klar getrennt. |
| [`designrecht-geschmacksmusterrecht`](./designrecht-geschmacksmusterrecht) | Eigenständiges Plugin für deutsches und europäisches Designrecht: DesignG, EU-Design, DPMA, EUIPO, WIPO-Hague, Neuheit, Eigenart, Anmeldung, Nichtigkeit, Verletzung, Eilrechtsschutz, Zoll, Plattformen und Designverträge. |
| [`deutsche-rechtsgeschichte`](./deutsche-rechtsgeschichte) | Mega-Plugin zur deutschen Rechtsgeschichte: Epochen, Quellenkritik, Rezeption, Reichsrecht, BGB, Weimar, NS-Unrecht, DDR/BRD und rechtsgeschichtliche Argumentation. |
| [`dfg-foerderantrag`](./dfg-foerderantrag) | DFG-Förderantragssteller für Sachbeihilfe, adaptive Anfänger-/Profi-Führung, kleine schnelle Anträge, große Koselleck-Strategien, elan-Formalia, Finanzplan, Reviewer-Red-Team, Forschungsdaten, KI-/Ethik-Check und Wiedereinreichung. |
| [`diesel-schadensersatz`](./diesel-schadensersatz) | Großes Dieselgate-Plugin für deutsches Recht mit acht aktiven Skills und erhaltenen Fachmodulen für Aktenstart, Beweisprüfung, Anspruchstrennung, Klage, Replik, beA-Paket und Vollstreckung. Mit geprüftem Fünfjahreskorpus, Rechtsstands-Cockpit und neun ausführlichen Testakten. |
| [`dsa-dma-digitalregulierung`](./dsa-dma-digitalregulierung) | Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und Paragraf 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege. |
| [`due-diligence`](./due-diligence) | Due Diligence für Käufer, Investoren und Verkäufer: Unternehmen, Beteiligungen, Personal, Bilanz, Verträge und Kreditportfolios belegt prüfen und Befunde in Kaufpreis, Vertragsregelungen und Vollzugsbedingungen übersetzen. |

</details>

<a id="e"></a>
<details>
<summary>E</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`e-rechnung-werkstatt`](./e-rechnung-werkstatt) | E-Rechnungen aus Word PDF Scans Tabellen E-Mails und Rechnungsdaten erstellen: ZUGFeRD mit eingebettetem XML und XRechnung. Pflichtangaben Belegabgleich Steuerlogik Formatprüfung und tatsächliche Dateiausgabe. |
| [`ecommerce-recht`](./ecommerce-recht) | Super-Plugin für Online-Shops, Plattformen, Marktplätze und digitale Verbraucherprozesse. |
| [`eigenbedarfskuendigungschecker`](./eigenbedarfskuendigungschecker) | Eigenbedarfskündigungen für Mieter und Vermieter prüfen: Bedarfsperson, Nutzungswunsch, Form, Fristen, Umwandlungsschutz und Härtewiderspruch. Zehn Skills führen zu begründeten Schreiben und tragfähigen Vereinbarungen; mit zwei vollständigen Fallakten. |
| [`einfache-leichte-sprache-jura`](./einfache-leichte-sprache-jura) | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. |
| [`einigungsvertrag-vermoegensrecht`](./einigungsvertrag-vermoegensrecht) | Einigungsvertrag-Plugin für DDR/BRD-Übergangsrecht, Volksvermögen, Parteivermögen, Treuhand, Bodenreform, Mauergrundstücke, VermG und Restitution. |
| [`email-umformulierer-berufsrecht`](./email-umformulierer-berufsrecht) | Formuliert unfreundliche, emotionale oder unsachliche E-Mails in höfliche, sachliche und berufsrechtskonform formulierte Texte um. Fokus auf BRAO/BORA-Konformität, mit Varianten für Steuerberater, Notare und allgemeine berufliche Korrespondenz. |
| [`energierecht`](./energierecht) | Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung. |
| [`enteignung-artikel-14`](./enteignung-artikel-14) | Grundstücksenteignung nach Artikel 14 GG und BauGB: Aktenaufnahme, Alternativen, Erwerbsverhandlungen, Beteiligte, Entschädigung, Anhörung, Besitzeinweisung, Beschlussvollzug und Baulandsachen. |
| [`erbbaurecht-praxis`](./erbbaurecht-praxis) | Praxisplugin für Erbbaurecht und Erbbaugrundbuch: Erbbaurechtsvertrag, Erbbauzins, Wertsicherung, Heimfall, Zustimmung, Belastung, Finanzierung, Veräußerung, Laufzeit, Entschädigung, Zwangsversteigerung, Rang und Grundbuchvollzug. |
| [`eu-sanktionspruefer`](./eu-sanktionspruefer) | EU-Sanktionen für Unternehmen und Kanzleien: Identität, Eigentum, Kontrolle, Finanzmittel, Waren, Leistungen, Ausnahmen, Meldungen und Rechtsschutz. Ein Hauptskill und neun Fachskills führen bis zum begründeten Schreiben oder Antrag. |
| [`europaeisches-prozessrecht`](./europaeisches-prozessrecht) | Europäisches Prozessrecht vor EuGH und EuG: Klagearten, Vorlage, e-Curia, Fristen, Rechtsschutz, Rechtsmittel, Intervention, Beweis, Kosten und Strategie. |
| [`europarecht-kompass`](./europarecht-kompass) | Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |

</details>

<a id="f"></a>
<details>
<summary>F</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`fachanwalt-agrarrecht`](./fachanwalt-agrarrecht) | Plugin Fachanwalt für Agrarrecht. Höferecht (HöfeO Anerbenrecht Länder) Landpachtrecht BGB Paragrafen 581 ff. GAP EU-Direktzahlungen Cross-Compliance Düngeverordnung Pflanzenschutz Tierschutz Forstrecht. Schnittstelle Plugin fachanwalt-erbrecht. |
| [`fachanwalt-arbeitsrecht`](./fachanwalt-arbeitsrecht) | Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle. |
| [`fachanwalt-bank-kapitalmarktrecht`](./fachanwalt-bank-kapitalmarktrecht) | Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit Bürgschaft Aval Bankgarantie Vermögensanlage Beratungshaftung. Schnittstellen Plugin gesellschaftsrecht regulatorisches-recht. |
| [`fachanwalt-bau-architektenrecht`](./fachanwalt-bau-architektenrecht) | Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Mängelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein. |
| [`fachanwalt-erbrecht`](./fachanwalt-erbrecht) | Plugin Fachanwalt für Erbrecht. BGB Erbrecht Paragrafen 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein. |
| [`fachanwalt-familienrecht`](./fachanwalt-familienrecht) | Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergänzend zum Plugin kanzlei-allgemein. |
| [`fachanwalt-gewerblicher-rechtsschutz`](./fachanwalt-gewerblicher-rechtsschutz) | Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO Paragraf 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezüge. Markenanmeldung DPMA EUIPO. UWG-Abmahnung Paragrafen 8 ff. UWG. Designverletzung. Einstweilige Verfügung Verletzungsklage Lizenzanaloger Schadensersatz. |
| [`fachanwalt-handels-gesellschaftsrecht`](./fachanwalt-handels-gesellschaftsrecht) | Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO Paragraf 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung Paragrafen 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich Paragraf 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. |
| [`fachanwalt-insolvenz-sanierungsrecht`](./fachanwalt-insolvenz-sanierungsrecht) | Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO Paragraf 14. InsO Eröffnung Antragspflicht Paragraf 15a Gläubigerantrag Paragraf 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung Paragrafen 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater. |
| [`fachanwalt-internationales-wirtschaftsrecht`](./fachanwalt-internationales-wirtschaftsrecht) | Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG Brüssel Ia Rom I Rom II Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Außenhandel LkSG. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-it-recht`](./fachanwalt-it-recht) | Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein. |
| [`fachanwalt-medizinrecht`](./fachanwalt-medizinrecht) | Plugin Fachanwalt für Medizinrecht. Arzthaftung Paragrafen 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Ärzte SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen Plugin fachanwalt-sozialrecht und kanzlei-allgemein. |
| [`fachanwalt-miet-wohnungseigentumsrecht`](./fachanwalt-miet-wohnungseigentumsrecht) | Miet- und Wohnungseigentumsrecht für Wohnraum, Gewerberaum, Betriebskosten und Hausverwaltung: Verträge, Beschlüsse, Mängel, Beweise, Fristen und Rechtsschutz in zusammenhängenden Arbeitswegen bearbeiten. |
| [`fachanwalt-migrationsrecht`](./fachanwalt-migrationsrecht) | Aufenthalt, Blaue Karte EU, Fachkräfte, Asyl, Dublin und GEAS, Einbürgerung und Staatenbezüge prüfen. Nachweise, Fristen und passende Schreiben ausarbeiten; bei Bedarf verständlich oder spanisch erklären. |
| [`fachanwalt-sozialrecht`](./fachanwalt-sozialrecht) | Plugin Fachanwalt für Sozialrecht nach FAO Paragraf 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch Paragraf 84 SGG Klage Paragraf 87 SGG Eilantrag Paragraf 86b SGG. Bürgergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch. |
| [`fachanwalt-sportrecht`](./fachanwalt-sportrecht) | Plugin Fachanwalt für Sportrecht. Verbandsrecht (DFB FIFA UEFA IOC DOSB) CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Veranstalterhaftung. Schnittstelle Plugin gesellschaftsrecht. |
| [`fachanwalt-strafrecht`](./fachanwalt-strafrecht) | Plugin Fachanwalt Strafrecht: StPO/StGB, Nebenstrafrecht, Verteidigung, Ermittlungsverfahren, HV, Revision, Nebenklage und Zeugenbeistand plus Strafprozess-Cockpit für Fristen, Aktenlog, U-Haft, Akteneinsicht, HV-Tagesmappe, Antragslog und Mandanteninstruktionen. |
| [`fachanwalt-transport-speditionsrecht`](./fachanwalt-transport-speditionsrecht) | Plugin Fachanwalt für Transport- und Speditionsrecht. HGB Paragrafen 407 ff. Frachtvertrag Paragrafen 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-urheber-medienrecht`](./fachanwalt-urheber-medienrecht) | Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persönlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein. |
| [`fachanwalt-vergaberecht`](./fachanwalt-vergaberecht) | Fachanwalt Vergaberecht als Vergabe-Workbench: GWB 97 ff., VgV, UVgO, SektVO, KonzVgV, VOB/A, Schwellenwerte, Vergabeakte, Rüge, vorgerichtliche Abhilfe, Nachprüfungsantrag, Vergabekammer-Sachverhalt, Paragraf 168-GWB-Abstellungsanträge, TED/eForms und Wettbewerbsregister. |
| [`fachanwalt-verkehrsrecht`](./fachanwalt-verkehrsrecht) | Plugin Fachanwalt für Verkehrsrecht. StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personen- und Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht (Paragrafen 315c 316 StGB). Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-versicherungsrecht`](./fachanwalt-versicherungsrecht) | Plugin Fachanwalt für Versicherungsrecht. VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstelle Plugin kanzlei-allgemein. |
| [`fachanwalt-verwaltungsrecht`](./fachanwalt-verwaltungsrecht) | Plugin Fachanwalt für Verwaltungsrecht. VwGO VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz Paragraf 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei- und Ordnungsrecht. Schnittstelle Plugin kanzlei-allgemein. |
| [`factoring-recht`](./factoring-recht) | Super-Plugin für Factoring, Forderungskauf, Aufsichtsrecht, Vertragsgestaltung, Debitorenkommunikation, Insolvenz- und Sanierungsfragen. |
| [`fahrgastrechte`](./fahrgastrechte) | Fahrgastrechte im Eisenbahnverkehr nach VO (EU) 2021/782 und EVO 2023: Verspätung/Ausfall einordnen, Entschädigung berechnen (25/50 Prozent), Forderung an die DB, Widerspruch, Schlichtung und Klage zum AG. Katalog DB-Ablehnungsgründe. |
| [`fashion-law-moderecht`](./fashion-law-moderecht) | Praxisplugin Fashion Law/Moderecht für Modeunternehmen, Designer, Händler und Kanzleien: IP, Designs, Marken, Textilkennzeichnung, Produktsicherheit, Nachhaltigkeit, Lieferkette, Plattformen, E-Commerce, Vertrieb, Influencer und Krisen. |
| [`festlandchina-wirtschaftsverkehr`](./festlandchina-wirtschaftsverkehr) | Mega-Plugin für wirtschaftlichen Umgang mit Festlandchina: Fabrik, Import, Export, Investition, De-Risking, Lieferkette, IP, Daten, Exportkontrolle und politisches Risiko. |
| [`fluggastrechte`](./fluggastrechte) | Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspätung prüfen, außergewöhnliche Umstände, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation. |
| [`forderungsmanagement-klagewerkstatt`](./forderungsmanagement-klagewerkstatt) | Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben. |
| [`forschungszulage-antragstellung`](./forschungszulage-antragstellung) | Forschungszulage-Antragstellung nach FZulG: adaptiver Fördercheck, BSFZ-Portaltexte mit Zeichenbudgets, Finanzamt-Antrag, FuE-Abgrenzung, Bemessungsgrundlage 2026, Auszahlung, Verlust-/Insolvenzlage, Dokumentation, Beihilfen, Einspruch und Mehrjahresroadmap. |
| [`fortbestehensprognose`](./fortbestehensprognose) | Fortbestehensprognose Paragraf 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwölf-Monats-Liquidität. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose. |
| [`franchiserecht-praxis`](./franchiserecht-praxis) | Wirtschaftsrechtliches Plugin für Franchise-Systeme: vorvertragliche Aufklärung, Handbuch, Gebühren, Gebietsschutz, Kartellrecht, Kündigung, Expansion, Streit und Insolvenz. |

</details>

<a id="g"></a>
<details>
<summary>G</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`gebrauchsmusterrecht`](./gebrauchsmusterrecht) | Eigenständiges Plugin für deutsches Gebrauchsmusterrecht: GebrMG, DPMA-Anmeldung, Recherche nach Paragraf 7 GebrMG, Abzweigung, Neuheitsschonfrist, Verletzung, Löschung, BPatG-Beschwerde, Lizenz, FTO und Schnellschutz für technische Produkte. |
| [`geldwaeschebeauftragter`](./geldwaeschebeauftragter) | Geldwäschebeauftragte im Unternehmen, in Anwaltskanzlei und Notariat: zehn Fachabläufe und ein Hauptproblem-Skill für Organisation, KYC, Kontrolle, Immobilien, FIU, Vertraulichkeit, Aufsicht und Nachverfolgung. |
| [`geldwaeschepraevention-aml-kyc`](./geldwaeschepraevention-aml-kyc) | Geldwäscheprüfung in Kanzlei, Unternehmen und Notariat: 20 Fachabläufe für Verpflichtetenstatus, KYC, UBO, Immobilienzahlungen, FIU-Meldung, Kontrollen und EU-Umstellung. Geltendes Recht 2026 und Pflichten ab 2027 bleiben getrennt. |
| [`gesellschafterstreit`](./gesellschafterstreit) | Gesellschafterstreit in GmbH und UG bearbeiten: Stimmverbote, Kapitalerhöhung, Geschäftsführer, Wettbewerb, Darlehen, Einziehung und Rechtsschutz mit belegt begründeten Anträgen und Vergleich. |
| [`gesellschaftervereinbarung`](./gesellschaftervereinbarung) | Gesellschaftervereinbarungen für GmbHs entwerfen, verhandeln und ändern. Zehn Fachskills und ein Hauptskill verbinden Kapital, Mitspracherechte, Anteilsverkauf, Gründerbindung und notariellen Vollzug. |
| [`gesellschaftsgruender`](./gesellschaftsgruender) | Gründungsassistent für deutsche Gesellschaften: Rechtsformwahl, Satzung, Notar, Handelsregister, Bank/KYC, Steuerstart, IP, Erlaubnisse, erste Verträge, Budget und Streitprävention. |
| [`gesellschaftsrecht`](./gesellschaftsrecht) | Gesellschaftsrecht für GmbH, AG und Personengesellschaften: Beschlüsse, Gesellschafterliste, Satzung, Organhaftung, Streit, Kapitalerhaltung, Umwandlung, Register und Transaktionen. |
| [`gesellschaftsrecht-legal-english`](./gesellschaftsrecht-legal-english) | Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English für Big-Law-Anfänger. Dealroom: Cap Table vs Gesellschafterliste; Term Sheet; SHA; Vesting; Drag/Tag; Liquidation Preference; Anti-Dilution; SPA; DD; Notar/HR; Multi-Format-Auswertung; Frankfurt-Startup-Akte. |
| [`gesellschaftsrechtliche-treuepflicht`](./gesellschaftsrechtliche-treuepflicht) | Großes Prüfplugin zur gesellschaftsrechtlichen Treuepflicht in GmbH, AG, SE, Personengesellschaft, Familiengesellschaft und Konzern: Stimmrecht, Minderheitenschutz, Gesellschafterliste, Einziehung, Ausschluss, Konkurrenz, Sanierung, Treuepflichtverletzung und Rechtsfolgen. |
| [`gewerblicher-rechtsschutz`](./gewerblicher-rechtsschutz) | Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen. |
| [`gmbh-gesellschafterversammlung`](./gmbh-gesellschafterversammlung) | Gesellschafterversammlungen für GmbH und UG: fünf Fachskills plus Hauptproblem-Skill für Unterlagen, Einladung, Nachträge, Stimmen, Leitfaden, Protokoll und Vollzug. Mit eigenständiger Werkstatt, Mini-Prompt und exaktem Stimmenprüfer. |
| [`goae-gebuehrenordnung-aerzte`](./goae-gebuehrenordnung-aerzte) | Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten. |
| [`grosskanzlei-corporate-ma`](./grosskanzlei-corporate-ma) | Corporate/M&A-Plugin für Kanzlei- und Inhouse-Praxis: Deal-Intake, Datenraum, Legal DD, SPA/APA, Kaufpreis, W&I, Regulatory, Signing, Closing, Integration, Board Papers und Spezial-Workflows. |
| [`grundbuchamt-assistent`](./grundbuchamt-assistent) | Grundbuchvorgänge von Einsicht und Urkundennachweis über Erbberichtigung, Rang und Briefaufgebot bis zur Zwischenverfügung und zum dokumentierten Vollzug. Zehn Fachskills und ein Hauptproblem-Skill mit klaren Notar- und Zugriffsgrenzen. |
| [`grundbuchamt-praxis`](./grundbuchamt-praxis) | Praxisplugin für Grundbuchamt, Grundbuchauszug und grundbuchtaugliche Nachweise: Abteilung I/II/III lesen, Bewilligung, Antrag, Auflassung, Rang, Zwischenverfügung, Beschwerde, Grundschuldbrief, Aufgebot, Dienstbarkeiten, Vormerkung, Vorkaufsrecht, Teilung und Vollzug. |
| [`grundsteuerrecht`](./grundsteuerrecht) | Grundsteuer von der Immobilie bis zum richtigen Rechtsbehelf: zehn Arbeitswege zu Lage, Landesmodell, Wert, Messbetrag, Hebesatz, Einspruch und Eilrechtsschutz mit nachrechenbaren Ergebnissen. |
| [`grundstuecksrecherche`](./grundstuecksrecherche) | Lokale App für Grundstücksrecherche in deutschen Städten: amtliche Quellen entdecken, NRW-Flurstücke verifiziert auswählen oder manuell erfassen und vier Auskunftsentwürfe als DOCX und ZIP vorbereiten. Kein automatischer Versand. |
| [`gvb-reinigungsvergabe`](./gvb-reinigungsvergabe) | Reinigungsvergaben im Berliner Nahverkehr: zehn aufeinander abgestimmte Skills für Bedarf, Leistungsverzeichnis, Vertrag, Bekanntmachung, Angebote, Rügen, Wertung, Zuschlag und Nachprüfung. |

</details>

<a id="h"></a>
<details>
<summary>H</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`handelsrecht-hgb`](./handelsrecht-hgb) | Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG. |
| [`handelsregister-assistent`](./handelsregister-assistent) | Handelsregister recherchieren und Registervorgänge vollziehen: Auszüge, Gesellschafterlisten, Auslandsvertretung, Organwechsel, Anmeldung, Zwischenverfügung und Datenschutz. Zehn Fachworkflows und ein Hauptproblem-Skill führen zu konkreten Dokumenten und nachgewiesenem Vollzugsstand. |
| [`handelsregister-praxis`](./handelsregister-praxis) | Praxisplugin für den Umgang mit dem Handelsregister: Anmeldung, Registergericht, Rechtspfleger, Registerrichter, Beanstandung, Zwischenverfügung, Beschwerde, Gesellschafterliste, Kapitalmaßnahmen, Firma, Vertretung, Prokura, Löschung, Insolvenzvermerk und registerfeste Nachweise. |
| [`handelsvertreterrecht`](./handelsvertreterrecht) | Handelsvertreterrecht nach HGB: Status, Provision, Buchauszug, Kündigung, Ausgleich Paragraf 89b, Wettbewerbsverbot Paragraf 90a und Vertriebsmodelle. |
| [`hausarbeitenmacher`](./hausarbeitenmacher) | Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion. |
| [`haushaltsrecht-bho-bund-laender`](./haushaltsrecht-bho-bund-laender) | Großes Haushaltsrecht-Plugin für BHO, HGrG, Bundeshaushalt, Länderhaushalte, Titelanalyse, Umschichtung, Sondervermögen, Szenarien und Dashboard. |
| [`hinweisgeberschutz-compliance`](./hinweisgeberschutz-compliance) | Hinweisgeberschutzgesetz in der Praxis: interne/externe Meldestelle, NDA-Konflikte, Repressalien, Untersuchungen, Datenschutz und Governance. |
| [`hoai-leistungsphasen-praxis`](./hoai-leistungsphasen-praxis) | Großplugin für HOAI-Leistungsphasen 1 bis 9: Grundlagenermittlung, Vorplanung, Entwurf, Genehmigung, Ausführungsplanung, Vergabe, Bauüberwachung, Objektbetreuung, Honorar, Vertrag, Haftung, Nachträge und Bauprojektsteuerung. |
| [`hochschulrecht-laender`](./hochschulrecht-laender) | Hochschulrecht der Länder: Hochschulgesetze, Satzungen, Gremien, Zulassung, Exmatrikulation, Berufung, Drittmittel, Promotion und Aufsicht. |

</details>

<a id="i"></a>
<details>
<summary>I</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`immobilienrechtspraxis`](./immobilienrechtspraxis) | Werkzeuge für immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragsprüfung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Prüfung. Rechtsprechung nur nach Live-Verifikation. |
| [`influencer-recht`](./influencer-recht) | Plugin für Influencer, Creator, Agenturen und Unternehmen: Werbekennzeichnung, Steuer, Umsatzsteuer, Sachleistungen, Plattformrecht, Medienrecht, Marken, Urheberrecht, Datenschutz und Verträge. |
| [`informationsfreiheit-presseauskunft`](./informationsfreiheit-presseauskunft) | IFG-, Transparenz-, UIG-, VIG- und Presseauskunfts-Plugin für Bund, Länder und Behörden: Antrag, Kosten, Fristen, Widerspruch, Klage und Tracking. |
| [`insiderrecht-compliance`](./insiderrecht-compliance) | Insiderrecht- und Marktmissbrauchs-Compliance nach MAR, WpHG und BaFin-Praxis: Insiderinformationen, Ad-hoc, Insiderlisten, Handelsverbote, Aufschub, Directors Dealings, Aufklärung und Verteidigung. |
| [`insolvenzanfechtung`](./insolvenzanfechtung) | Insolvenzanfechtung aus Verwalter- und Empfängersicht: Zahlungsketten, Deckung, Vorsatz, Drittleistungen, Gesellschafterfinanzierung, Bargeschäft und Rückgewähr belegt prüfen. Zehn Fachskills und ein Hauptskill führen zum ausformulierten Schreiben, Schriftsatz oder Vergleich. |
| [`insolvenzforderungen-checker`](./insolvenzforderungen-checker) | Insolvenzforderungen vom Akteneingang bis zum begründeten Prüfvorschlag bearbeiten. Elf Skills verbinden Gläubigerklärung, Belege, Beträge, Rang, Sicherheiten und Termine mit Tabellenentwurf und Gläubigerbrief; keine automatische Feststellung oder Einreichung. |
| [`insolvenzforderungsanmeldungspruefung`](./insolvenzforderungsanmeldungspruefung) | Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, Paragraf 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung. |
| [`insolvenzplan-starug-planwerkstatt`](./insolvenzplan-starug-planwerkstatt) | Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| [`insolvenzrecht`](./insolvenzrecht) | Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag. |
| [`insolvenzsachbearbeitung`](./insolvenzsachbearbeitung) | Insolvenzsachbearbeitung vom Beschluss bis zur Verteilung vorbereiten. Zehn Fachskills und ein Hauptskill verbinden Forderungen, Korrespondenz, Eigentum, Sicherheiten, Massebelege, Betrieb und Verbraucherinsolvenz mit belegten, ausformulierten Arbeitsprodukten. |
| [`insolvenzverwaltung`](./insolvenzverwaltung) | Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, Paragraf 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. |
| [`insolvenzverwaltung-berichtsersteller`](./insolvenzverwaltung-berichtsersteller) | Zwischenberichte, Schlussberichte, Schlussrechnung und Verteilung in Insolvenzverfahren belegt erstellen. Zehn Fachskills und ein Hauptskill führen Akte, Stichtage, Masse, Forderungen, Kosten, Prozesse und Freigaben zu gerichtstauglichen Produkten zusammen. |
| [`internal-investigations-praxis`](./internal-investigations-praxis) | Internal-Investigations-Praxisplugin für Kanzleien und Unternehmen: Untersuchungsauftrag, Scope, Interviews, Arbeitsrecht, Datenschutz, Privilege-Risiko, StPO-Beschlagnahme, HinSchG, Dokumentation und Verteidigung. |
| [`internationales-handelsrecht-lex-mercatoria`](./internationales-handelsrecht-lex-mercatoria) | Mega-Plugin für internationales Handelsrecht, CISG, Incoterms, UNIDROIT Principles, Lex Mercatoria, Schiedsverfahren, Trade Finance und Lieferkettenverträge. |

</details>

<a id="j"></a>
<details>
<summary>J</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`jugendmedienschutz-und-medienangebote`](./jugendmedienschutz-und-medienangebote) | Jugendschutz für Browsergames, KI-Szenarien, Medienangebote und Nutzerkommunikation. Zehn Skills prüfen JuSchG, JMStV, MStV und Schnittstellen zu DSA, Datenschutz und KI-Verordnung bis zum konkreten Dokument. |
| [`jura-in-einfacher-sprache`](./jura-in-einfacher-sprache) | Juristische Texte in einfache Sprache und zurück in juristische Standardsprache übertragen, erklären, schreiben und beantworten. Fünf Skills bewahren Bedingungen, Fristen und Rechtsfolgen. Keine erfundenen Ergänzungen bei fehlendem Original. |
| [`jurastudium`](./jurastudium) | Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. |
| [`juristische-praesentationen`](./juristische-praesentationen) | Juristische PowerPoint-Präsentationen für Kanzlei und Rechtsabteilung: zehn Kernskills von Urteil, Fachvortrag und Laienerklärung bis Folien, Sprechernotizen und Probe. Zwei optionale Bonus-Skills für seriöse Animation und jugendgerechte Sprache. Mit neutraler Vorlage. |
| [`juristische-presseberichterstattung`](./juristische-presseberichterstattung) | Plugin für juristische Presseberichterstattung: Gerichtsbericht, Entscheidungsnews, Verdachtsbericht, Pressemitteilung, Headline, Bildprüfung, Quellenmatrix und Redaktionsschluss-Qualitygate. |
| [`juristische-sprache-deutsch-als-zweitsprache`](./juristische-sprache-deutsch-als-zweitsprache) | Plugin für Menschen im deutschen Recht mit anderer Herkunftssprache: einfache Erklärungen, Juristendeutsch, Bescheide, Schriftsätze, Grammatik, Fristen und Verfahrenslogik. |
| [`jveg-kostenpruefer`](./jveg-kostenpruefer) | Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |

</details>

<a id="k"></a>
<details>
<summary>K</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`kanzlei-allgemein`](./kanzlei-allgemein) | Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten. |
| [`kanzlei-builder-hub`](./kanzlei-builder-hub) | Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung. |
| [`kanzlei-management`](./kanzlei-management) | Mega-Plugin für Kanzlei-Management: Managing Partner, Management Committee, Cashflow, Pricing, UBT, FTE, Utilization, WIP, Associates, Partnerkreis und Dashboards. |
| [`kanzlei-mandant-lifecycle`](./kanzlei-mandant-lifecycle) | Lifecycle-Plugin für Kanzlei, Mandant und Rechtsabteilung: Mandatsstart, OCG, Budget, Dashboard, Rechnung, Litigation, Erwartungsmanagement und Relationship-Governance. |
| [`kanzlei-website-redaktion`](./kanzlei-website-redaktion) | Kanzlei-Website mit zehn Skills betreiben: Blog, Rechtsprechungsnews, Teamprofile, Fotos, Kontakte und Quellenbeobachtung. Mit Vorschau, Artikel-50-Prüfung, konkreten Freigaben und kontrollierter Veröffentlichung. |
| [`kartellrecht-marktabgrenzung-pruefung`](./kartellrecht-marktabgrenzung-pruefung) | Globales Kartellrecht/Competition Law: GWB, Art 101/102 AEUV, Fusionskontrolle, BKartA, DG Competition, FTC/DOJ, ICN-Jurisdiktionen, Dawn Raids, Marktabgrenzung, Missbrauch, Private Enforcement. |
| [`ki-governance`](./ki-governance) | EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. |
| [`ki-halluzinationsreduzierer`](./ki-halluzinationsreduzierer) | Juristische Fundstellen am zugänglichen Originalvolltext prüfen: Existenz, Identität, Fundpunkt, Aussagekraft und Fallübertragbarkeit getrennt belegen. Zehn Fachskills und ein Hauptskill liefern Prüfbericht, offene Befunde und nachvollziehbare Korrekturfassung. |
| [`ki-native-kanzlei`](./ki-native-kanzlei) | Kanzleibetrieb mit acht Arbeitswegen und 30 Fachmodulen: Posteingang, Fristen, Rechtsarbeit, Dokumente, Beweise, Vergleich, Kosten und Vollstreckung. Kontrollierter Computerlauf mit konkreten Freigaben und lebensnahen Übungsakten. |
| [`ki-richtlinie-kanzleien`](./ki-richtlinie-kanzleien) | Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwälten und Syndikus-Anwälten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen. |
| [`ki-verordnung-hochrisiko-pruefer`](./ki-verordnung-hochrisiko-pruefer) | Prüft Artikel 6 KI-Verordnung: Produktpfad, sämtliche Anhang-III-Felder, vier Ausnahmen und Profiling. Zehn Fachskills und ein Hauptproblem-Skill führen zu Einstufung, Nachforderung und Entscheidung; mit Fällen zu Recruiting, Justiz und Medizinprodukt. |
| [`ki-verordnung-konformitaet`](./ki-verordnung-konformitaet) | Prüft die Konformität konkreter KI-Systeme: Verfahrenswahl, Risikomanagement, Qualitätsmanagement, Daten, Aufsicht, Nachweise, Erklärung und Änderungen. Erstellt ein belastbares Dossier mit begründeten offenen Punkten. |
| [`ki-verordnung-register-meldungen`](./ki-verordnung-register-meldungen) | Prüft Register- und Meldepflichten der KI-Verordnung nach Rolle, System, Anlass und Zeitrecht. Erstellt Datensätze, Erstberichte, Ergänzungen und Anschreiben und hält Freigabe sowie tatsächlichen Eingang nach. |
| [`ki-verordnung-transparenzpruefer`](./ki-verordnung-transparenzpruefer) | Artikel 50 KI-Verordnung praktisch prüfen: Rollen, Kanzleientwürfe, öffentliche Texte, redaktionelle Kontrolle, KI-Chat und Telefon, Deepfakes, technische Markierung und Biometrie. Mit verwendbaren Hinweisen, Anbieteranfragen und Freigabevermerken. |
| [`ki-verordnung-verbotene-praktiken`](./ki-verordnung-verbotene-praktiken) | Verbotene KI-Praktiken nach Artikel 5 prüfen: konkrete Funktionen, Schutzbedürftigkeit, soziale Bewertung, biometrische Verfahren und neue Inhaltsverbote mit belegter Subsumtion und Maßnahmen. |
| [`ki-vo-ai-act-pruefer`](./ki-vo-ai-act-pruefer) | Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung, Konformitäts-Evidence-Pack, KI-Kompetenz, Shadow-AI, Berufsrecht, Hochschul- und Behördenpraxis. |
| [`kommunale-haftpflicht`](./kommunale-haftpflicht) | Kommunale Schäden belegt bearbeiten: Gebäude, Straßen, Winterdienst, Fahrzeuge, Bäder, Antrags- und Bauentscheidungen, Leitungen und Krankenhaus-Großschäden; Haftung, Schadenhöhe, Deckung und internen Ausgleich trennen. |
| [`kommunalrecht-laender`](./kommunalrecht-laender) | Großes Kommunalrecht-Plugin für Gemeinden, Städte, Landkreise, Satzungen, Räte, Bürgerbegehren, Kommunalfinanzen, Aufsicht und Landesrecht. |
| [`konkurrenten-rechtsschutz`](./vergaberecht-werkstatt/konkurrenten-rechtsschutz) | Konkurrenten legen Unterlagen, Informationsschreiben oder Portalbelege ab und starten ohne Skillwahl. Das Plugin sichert Rüge- und Zuschlagsfristen, Angriff, Beweiskette, Akteneinsicht, VK, OLG und Kosten. |
| [`krankenhaus-it-ki`](./krankenhaus-it-ki) | Krankenhaus-IT und KI: elf Skills für Datenschutz, Cloud, TIA, DSFA, Medizinprodukte, Forschung und sicheren Betrieb; mit eigenständigen Prompts und einer Thüringer Klinikakte. |
| [`krankenhausrecht`](./krankenhausrecht) | Super-Plugin für deutsches Krankenhausrecht: Planung, Finanzierung, Entgelte, Reform, Qualität, MD-Prüfung, Klinikbetrieb und Rechtsstreit. |
| [`krankenkassenrecht-krankenversicherung`](./krankenkassenrecht-krankenversicherung) | Plugin für GKV, PKV, Beihilfe-Schnittstellen und Krankenversicherungsrecht: Leistungen, Beiträge, Krankengeld, Hilfsmittel, Widerspruch, MD, Versicherungsvertrag und Kostenerstattung. |
| [`kriegsdienstverweigerung-wehrdienst`](./kriegsdienstverweigerung-wehrdienst) | Praxisplugin für Kriegsdienstverweigerung und Wehrdienst aus Gewissensgründen: Art. 4 Abs. 3 GG, KDVG n. F. 2026, Antrag über BAPersBw, BAFzA-Entscheidung, Gewissensbegründung, Soldaten, Reservisten, Rechtsschutz und saubere Abgrenzung zur Totalverweigerung. |
| [`krisenfrueherkennung-starug`](./krisenfrueherkennung-starug) | Krisenfrüherkennung nach Paragraf 1 StaRUG, Warnpflicht bei Jahresabschlusserstellung nach Paragraf 102 StaRUG, 24-Monats-Prognose nach Paragraf 18 InsO, Haftung, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. |

</details>

<a id="l"></a>
<details>
<summary>L</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`leasingrecht-praxis`](./leasingrecht-praxis) | Wirtschaftsrechtliches Praxisplugin für Leasing, Sale-and-lease-back, Equipment Finance, Fahrzeugflotten, IT-Leasing, Insolvenz, Restwert, Sicherheiten und Vertragsgestaltung. |
| [`legistik-werkstatt`](./legistik-werkstatt) | Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden. |
| [`liquiditaetsplanung`](./liquiditaetsplanung) | Liquiditätsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Lücken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation. |
| [`lizenzvertragsersteller`](./lizenzvertragsersteller) | IP-Lizenzverträge für Urheberrecht, Patente, Marken, Designs, Gebrauchsmuster, Geschäftsgeheimnisse und Know-how gestalten. Rechte, Vergütung, Quellcode-Escrow, Insolvenz und internationale Schnittstellen abstimmen; deutsche und englische Fassungen erstellen. |
| [`lobbyregister-bundestag`](./lobbyregister-bundestag) | Lobbyregister-Bundestag-Superplugin mit neun aktiven Skills und erhaltenen Fachmodulen für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstößen und Fristen nach LobbyRG. |
| [`luftrecht-flughafenrecht`](./luftrecht-flughafenrecht) | Luftrecht-Plugin für LuftVG, LuftSiG, LBA, Flughäfen, Airlines, Slots, Flugzeugpfandrechte, Beschlagnahme, Insolvenz, Drohnen und Aviation-Compliance. |

</details>

<a id="m"></a>
<details>
<summary>M</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`mandantenanfragen-assistent`](./mandantenanfragen-assistent) | Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt förmlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. |
| [`markenamt-assistent`](./markenamt-assistent) | DPMA und EUIPO: Marken recherchieren, anmelden, verteidigen, umschreiben und nachhalten. Zehn Fachskills und ein Hauptproblem-Skill mit konkreten Rechtsprechungsankern aus 2026, optionalem freigegebenem Portalvollzug und drei Testakten. |
| [`markenrecht-fashion-luxus`](./markenrecht-fashion-luxus) | Großes Markenrechts-Plugin für DE/EU/US und internationale Portfolios: DPMA, EUIPO, WIPO/Madrid, USPTO, Markenarten, Schutzhindernisse, Benutzung, Widerspruch, Verfall/Nichtigkeit, Enforcement, Plattformen, Zoll, Lizenzen und Luxus-Fashion-Spezialfälle. |
| [`meinungspruefer`](./meinungspruefer) | Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, Paragraf 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik. |
| [`memorandums-ersteller`](./memorandums-ersteller) | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher. |
| [`methodenlehre-buergerliches-recht`](./methodenlehre-buergerliches-recht) | Methodenlehre und Rechtsanwendung im deutschen bürgerlichen Recht aus Anwaltsperspektive: Anspruchsaufbau, Auslegung, Abwägung, Präzedenzarbeit, Rechtsfortbildung, Methodenwahl, EU-Methodik und methodenehrliche Begründungskontrolle. |
| [`mietchecker`](./mietchecker) | Miethöhen für Mieter und Vermieter nachvollziehbar prüfen: örtlicher Mietspiegel, Landesverordnung, Neuvermietung und Mieterhöhung. Zehn Skills führen von Belegen zu Berechnung und sachlicher Klärung; mit Fällen aus Berlin und Regensburg. |
| [`mietrecht`](./mietrecht) | Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Datenerhebung Mieterhöhungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht. |
| [`mittelstand-corporate-ma`](./mittelstand-corporate-ma) | Freistehendes Mittelstandsmandat-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |

</details>

<a id="n"></a>
<details>
<summary>N</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`nachbarschaftsstreit-pruefer`](./nachbarschaftsstreit-pruefer) | Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich. |
| [`nda-abgleich`](./nda-abgleich) | Gleicht NDA-Entwurf der Gegenseite gegen eigenen Standard ab und setzt Haltelinien chirurgisch im Word-Änderungsmodus durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Tracked Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen. |
| [`nda-verschwiegenheit-generator-checker`](./nda-verschwiegenheit-generator-checker) | Allgemeiner NDA-Ersteller und NDA-Prüfer für deutsche und internationale Verschwiegenheitsvereinbarungen: Entwurf, Redline, GeschGehG, HinSchG, AGB, Arbeitsrecht, M&A, Forschung, Software, Datenraum und Verletzungsreaktion. |
| [`nis2-cybersecurity-compliance`](./nis2-cybersecurity-compliance) | NIS-2, BSIG 2025, BSI, IT-Grundschutz, Cloud, Incident Response und technische Security-Compliance für Geschäftsleitung, CISO und Legal. |
| [`normenkontrolle-bauleitplanung`](./normenkontrolle-bauleitplanung) | Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach Paragraf 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung. |
| [`normenkontrollrat-nkr`](./normenkontrollrat-nkr) | Plugin für den Nationalen Normenkontrollrat (NKR): Prüfung von Referentenentwürfen Formulierungshilfen und Gesetzentwürfen auf Erfüllungsaufwand Erforderlichkeit Verhältnismäßigkeit One-in-one-out Digitalcheck Mittelstandsfreundlichkeit und Praktikabilität im Vollzug. |
| [`notariat-alltag`](./notariat-alltag) | Notariatswerkstatt für Mitarbeiter: Kundenordner, Bauträgerkauf, Grundschuld, Beglaubigung, GmbH-Gründung, Kapitalerhöhung, Geschäftsführerwechsel und Anteilsgeschäfte bis zur Vorlage an den Notar. |

</details>

<a id="o"></a>
<details>
<summary>O</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`oeffentliches-wirtschaftsrecht`](./oeffentliches-wirtschaftsrecht) | Öffentliches-Wirtschaftsrecht-Plugin für Scheinprivatisierung, ÖPP, Projektfinanzierung, kommunale Unternehmen, Beihilfen, Vergabe und Regulierung. |
| [`ordnungswidrigkeitenrecht`](./ordnungswidrigkeitenrecht) | Allgemeines OWiG-Plugin für Bußgeldverfahren: Anhörung, Bescheid, Einspruch, Behörde, Akteneinsicht, Gericht, Verjährung, Einziehung und Nebenfolgen. |

</details>

<a id="p"></a>
<details>
<summary>P</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`parteienrecht-parteiorganisation`](./parteienrecht-parteiorganisation) | Parteienrechts- und Parteiorganisations-Plugin für formale Parteiarbeit: Parteiengesetz, Satzung, Mitgliederrechte, Parteitage, Kreis- und Bezirksversammlungen, Kandidatenaufstellung, Wahlvorschläge, Parteigerichte, Spenden, Rechenschaft, Abgeordnetenrecht und Wahlleiterkommunikation. |
| [`patentrecherche`](./patentrecherche) | Patentrecherche für Patentanwälte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit Paragraf 3 PatG Art. 54 EPÜ erfinderische Tätigkeit Paragraf 4 PatG Art. 56 EPÜ Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht. |
| [`patentrecht`](./patentrecht) | Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen. |
| [`pflegerecht-sgb-xi`](./pflegerecht-sgb-xi) | Pflegeversicherung nach SGB XI: Pflegegrad, Begutachtung, häusliche Leistungen, Ersatzpflege, Wohnumfeld, Heimkosten, Pflegepersonen, Beiträge und Rechtsbehelfe. Zehn spezialisierte Skills vom Beleg zum Antrag oder Schriftsatz. |
| [`phishing-vorfall-pruefer`](./phishing-vorfall-pruefer) | Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB Paragraf 675u, Paragraf 675v, Paragraf 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage. |
| [`playbook-pruefer`](./playbook-pruefer) | Verträge regelweise an freigegebenen Kanzlei-Playbooks prüfen: Themen, Ausgangspositionen, Kompromisse und rote Linien mit Originalzitaten und Word-Bericht. |
| [`preussisches-allgemeines-landrecht-pralr`](./preussisches-allgemeines-landrecht-pralr) | PrALR-Plugin zum Allgemeinen Landrecht für die Preußischen Staaten: Quellenkritik, Textzeugen, Zivilrecht, Staats-/Polizeirecht, Strafrecht, Ständerecht, Aufopferung und Rezeptionsgeschichte. |
| [`private-equity-praxis`](./private-equity-praxis) | Private-Equity-Praxis-Plugin für deutsche Kanzleien, Investoren, Fonds, Family Offices und Unternehmen: Fund Formation, KAGB/AIF, ELTIF, Deal Execution, Private Credit, Schuldschein, LMA, NPL, Portfolio, Exit und Distressed. |
| [`produktrecht`](./produktrecht) | Produkthaftung und Produktrecht: Produktsicherheit, GPSR, ProdHaftG, deliktische Produzentenhaftung, Right to Repair, Software-/OTA-Updates, digitale Produktlebenszyklen, Rückruf, Marktüberwachung und Launch-Review. |
| [`prozessrecht`](./prozessrecht) | Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze. |
| [`pruefungsrecht-hochschule`](./pruefungsrecht-hochschule) | Hochschulprüfungsrecht: Prüfungsordnung, Bewertungsspielraum, Akteneinsicht, Krankheit, Nachteilsausgleich, Täuschung, KI, Drittversuch und Eilrechtsschutz. |

</details>

<a id="r"></a>
<details>
<summary>R</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`rechtsabteilung-forderungsmanagement-immobilienunternehmen`](./rechtsabteilung-forderungsmanagement-immobilienunternehmen) | Rechtsabteilung Forderungsmanagement Immobilienunternehmen: 50 Arbeitswege für Mietkonto, Kündigung, Mieterhöhung, Klage, Verteidigung, Kosten und Vollstreckung. Ordnerstart für Fachangestellte mit Quellen-, Rollen- und Freigabeprüfung. |
| [`rechtsberatungsstelle`](./rechtsberatungsstelle) | Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. |
| [`rechtstheorie-rechtsphilosophie`](./rechtstheorie-rechtsphilosophie) | Rechtstheorie- und Rechtsphilosophie-Plugin für juristische Praxis: Rechtsbegriff, Kelsen-orientierte Normgeltung, Demokratie, Rechtsrealismus, Systemdenken, Besitzdogmatik, Law-and-Economics, Hayek-Wissensproblem, spontane Ordnung, Machtkritik und anti-dezisionistische Red-Team-Prüfung. |
| [`regulatorisches-recht`](./regulatorisches-recht) | Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest. |
| [`relationstechnik-zivilrecht`](./gerichtsplugins/relationstechnik-zivilrecht) | Relationstechnik Zivilrecht: Klägerstation, Beklagtenstation, Beweisstation und Entscheidungsstation mit Schlüssigkeit, Erheblichkeit, Beweislast, Hinweisen und Urteilsvotum. |
| [`rentenpruefer`](./rentenpruefer) | Rentenprüfer für Arbeitnehmer: DRV-Kontenklärung, Alters- und Erwerbsminderungsrente, Betriebsrente, private Renten, Versorgungswerk-Schnittstellen, Bescheid, Widerspruch und Klage. |
| [`richter-amtsgericht-handelsregister`](./gerichtsplugins/richter-amtsgericht-handelsregister) | Handelsregisterrichter und Rechtspfleger: Ersteintragung Änderungen Löschung Zwischenverfügung Beschwerde Eintragungsfähigkeit Firmenrecht Vertretungsmacht Liquidation und Löschung von Amts wegen |
| [`richter-amtsgericht-insolvenz-restrukturierung`](./gerichtsplugins/richter-amtsgericht-insolvenz-restrukturierung) | Insolvenz- und Restrukturierungsgericht: Eröffnungsverfahren Sicherungsmaßnahmen Verwalterauswahl Gläubigerversammlung Prüfungstermin Schlusstermin Restschuldbefreiung Restrukturierungssache nach StaRUG mit Stabilisierungsanordnung und Planbestätigung |
| [`richter-amtsgericht-straf`](./gerichtsplugins/richter-amtsgericht-straf) | Strafrichter Amtsgericht: Eröffnungsentscheidung Hauptverhandlung Beweiswürdigung Strafzumessung Urteilsbegründung Rechtsmittelbelehrung Strafbefehl beschleunigtes Verfahren mit Tenorvorschlag |
| [`richter-amtsgericht-zivil`](./gerichtsplugins/richter-amtsgericht-zivil) | Amtsrichter Zivilsachen: Schlüssigkeit Erheblichkeit Beweis Tenor Kostenentscheidung Streitwertbeschluss vorläufige Vollstreckbarkeit Rechtsmittelbelehrung Versäumnisurteil und Anerkenntnisurteil mit echter Relation und Entscheidungsvorschlag |
| [`richter-arbeitsgericht`](./gerichtsplugins/richter-arbeitsgericht) | Arbeitsgericht: Gütetermin Kammertermin Kündigungsschutzklage Zahlungsklage einstweilige Verfügung Beschlussverfahren Betriebsverfassung Streitwert mit Tenorvorschlag |
| [`richter-bverfg-verfassungsbeschwerden`](./gerichtsplugins/richter-bverfg-verfassungsbeschwerden) | BVerfG Kammer und wissenschaftliche Mitarbeiter: Annahmeprüfung Verfassungsbeschwerde Paragraf 93a BVerfGG Substantiierung Subsidiarität Grundrechtsverletzung Rechtswegerschöpfung Voten Kammerbeschluss Nichtannahmebeschluss |
| [`richter-familiengericht`](./gerichtsplugins/richter-familiengericht) | Familiengericht: Ehesachen Scheidung Versorgungsausgleich Kindschaftssachen elterliche Sorge Umgang Kindesunterhalt Trennungs- und Ehegattenunterhalt Gewaltschutz Adoption Vormundschaft Betreuungsteile mit Verfahrenskostenhilfe und Tenorvorschlag |
| [`richter-finanzgericht`](./gerichtsplugins/richter-finanzgericht) | Finanzgericht: Sachprüfung Anfechtungsklage Verpflichtungsklage Aussetzung der Vollziehung Paragraf 69 FGO Beweiswürdigung im Amtsermittlungsgrundsatz und Urteilsentwurf mit Tenorvorschlag |
| [`richter-landgericht-strafkammer`](./gerichtsplugins/richter-landgericht-strafkammer) | Strafkammer LG: Eröffnungsentscheidung Hauptverhandlung Beweiswürdigung Strafzumessung schwere und mittlere Kriminalität Berufung gegen Amtsgerichtsurteil Sicherungsverwahrung und Maßnahmen mit Tenorvorschlag |
| [`richter-landgericht-zivilkammer`](./gerichtsplugins/richter-landgericht-zivilkammer) | Zivilkammer LG: erste Instanz und Berufung, große Relation, Schlüssigkeit Erheblichkeit Beweis, Hinweisverfügung Paragraf 139 ZPO, Beweisbeschluss, Sachverständigenbeweis, Urteil Paragraf 313 ZPO, Berufungsentscheidung Paragrafen 522-540 ZPO mit Tenorvorschlag |
| [`richter-sozialgericht`](./gerichtsplugins/richter-sozialgericht) | Sozialgericht: Klagearten Anfechtungs- und Leistungsklage einstweiliger Rechtsschutz Paragraf 86b SGG Amtsermittlung sozialrechtliche Prüfungsschemata Krankenversicherung Rente Unfall Bürgergeld Schwerbehinderung Urteilsentwurf mit Tenorvorschlag |
| [`richter-verwaltungsgericht`](./gerichtsplugins/richter-verwaltungsgericht) | Verwaltungsgericht: Sachprüfung Anfechtungs- und Verpflichtungsklage einstweiliger Rechtsschutz Paragraf 80 Abs. 5 VwGO Hauptsacheentscheidung Beweiswürdigung im Amtsermittlungsgrundsatz und Tenorvorschlag |
| [`robotik-recht`](./robotik-recht) | Robotik-Recht Deutschland/EU: Maschinenverordnung, KI-VO, Produkthaftung, ProdSG, Datenschutz, CRA, Data Act, CE, Marktüberwachung, Unfälle, Rückruf, Verträge und Robotik-Testakte. |
| [`roemisch-katholisches-kirchenrecht`](./roemisch-katholisches-kirchenrecht) | Großes, lehramts- und papsttreues Arbeitsplugin zum Recht der römisch-katholischen Kirche: CIC, Katechismus, Sakramente, Ehe, Kirchenaustritt, Verfahren, Disziplin, Pfarrei, Diözese, Kurie und mehrsprachige Kommunikation. |
| [`roemisches-recht`](./roemisches-recht) | Mega-Plugin zum römischen Recht: Zwölftafelgesetz, Institutionensystem, Sachenrecht, Obligationen, Aktionenrecht, Erbrecht, Juristenrecht, Justinian, byzantinisches Recht und Rezeption. |

</details>

<a id="s"></a>
<details>
<summary>S</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`schadensregulierung`](./schadensregulierung) | Schadensabwicklung für Unternehmen und Haftpflichtversicherer: Personen-, Sach- und Abschleppschäden, Haftung, Deckung, Besichtigung, Regress und kontrollierte Regulierung. Zehn fokussierte Arbeitswege mit getrennten internen Vorlagen und Außenbriefen. |
| [`schoeffen-handelsrichter-praxis`](./schoeffen-handelsrichter-praxis) | Plugin für Schöffen, Jugendschöffen, ehrenamtliche Richter und Handelsrichter: Rolle, Rechte, Pflichten, Sitzung, Beratung, Befangenheit, Beweiswürdigung, Handelskammer, Verwaltungsgericht und sichere praktische Orientierung. |
| [`schriftform-und-textform-bgb`](./schriftform-und-textform-bgb) | Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation. |
| [`schriftsatz-versandwerkstatt`](./schriftsatz-versandwerkstatt) | Fokussierte Versandwerkstatt für fertige Schriftsätze und Anlagen: konvertiert Dateien in PDF, stempelt Anlagen, prüft Dateinamen, Paketgrenzen, Absender, Signaturweg und Eingang und liefert eine kontrollierte beA-Mappe. |
| [`schriftsatzwerkstatt-bea`](./schriftsatzwerkstatt-bea) | Technische Versandwerkstatt der Immobilien-Rechtsabteilung: neun Schritte vom fachlich fertigen Ordner zu Einzel-PDFs, Anlagenfolge, Signaturentscheidung und geprüftem Übergabepaket. Keine Inhaltsprüfung und kein eigener Versand. |
| [`schulrecht-laender`](./schulrecht-laender) | Schulrecht der Länder: Schulpflicht, Aufnahme, Inklusion, Noten, Versetzung, Ordnungsmaßnahmen, Datenschutz, Elternrechte und Eilrechtsschutz. |
| [`seerecht-schifffahrtsrecht`](./seerecht-schifffahrtsrecht) | See- und Schifffahrtsrecht-Plugin für Schiffskauf, Schiffbau, Werften, Schiffshypothek, Schiffsregister, Arrest, Wrack, Bergung, Charter und ITLOS. |
| [`sektorenvergabe-workflow`](./sektorenvergabe-workflow) | Sektorenvergabe aus Auftraggebersicht: fünf Skills für Vergabeunterlagen, fünf für Verfahrensführung und ein Hauptskill. Von Reinigungsbedarf und Leistungsverzeichnis über Bekanntmachung, Rügen und Wertung bis Zuschlag und Nachprüfung. |
| [`selbstvertreter-amtsgericht`](./selbstvertreter-amtsgericht) | Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, Paragraf23 GVG/Paragraf511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung. |
| [`selbstvertreter-sozialgericht`](./selbstvertreter-sozialgericht) | Selbstvertretung vor Sozialbehörden Krankenkassen Pflegekassen BG Versorgungsamt Jobcenter Rente Familienkasse und Sozialgericht: Anhörung Akteneinsicht Mitwirkung Widerspruch Klage Eilantrag Pflegegrad Hilfsmittel Krankengeld EM-Rente GdB Bürgergeld Wohngeld Eingliederungshilfe. |
| [`softwarerecht-de-eu-us`](./softwarerecht-de-eu-us) | Softwarerecht Deutschland/EU/International/USA: Entwicklung, Lizenzen, SaaS, Open Source, Arbeitnehmer/Freelancer, Softwarepatente, AI-Code und Streit. |
| [`solo-selbststaendige-praxis`](./solo-selbststaendige-praxis) | Praxisplugin für Solo-Selbstständige in Deutschland: Start, Anmeldung, Steuern, Verträge, Rechnungen, Datenschutz, Statusfeststellung, KSK, Versicherungen, Zahlungsausfall, Krise, Wachstum und Alltag ohne juristische Überforderung. |
| [`sozialrecht-fuer-laien`](./sozialrecht-fuer-laien) | Sozialrecht für den eigenen Fall: Briefe verstehen, Tatsachen klären, Fristen prüfen und Anträge, Widersprüche oder Gerichtsschreiben vorbereiten. Zehn kurze Arbeitswege in einfacher Sprache mit klaren Grenzen und Wegen zu persönlicher Hilfe. |
| [`sozialversicherungspflicht-pruefer`](./sozialversicherungspflicht-pruefer) | Sozialversicherungsstatus und Versicherungspflicht: 14 Skills für Beschäftigung, Geschäftsführer, Lehrkräfte, freie Mitarbeit, Plattformen, KSVG, Auslandsbezug, Versorgungswerke und Beiträge. Mit eigenständiger Werkstatt, Mini-Prompt und 13 zugeordneten Fallakten. |
| [`staatsanwaltschaft-amtsanwaltschaft`](./gerichtsplugins/staatsanwaltschaft-amtsanwaltschaft) | Staatsanwaltschaft und Amtsanwaltschaft: Ermittlungsführung, Durchsuchung, Haft, Einstellung, Strafbefehl, Anklage, Einziehung, Plädoyer, Rechtsmittel und Vollstreckung. |
| [`staatsanwaltschaft-praxis-einstieg`](./gerichtsplugins/staatsanwaltschaft-praxis-einstieg) | Praxisplugin für neue Staatsanwälte: Aktenstart, Anfangsverdacht, Ermittlungsauftrag, Eingriffe, Anklage, Strafbefehl, Einstellung, Sitzungsdienst, Rechtsmittel und OWiG. |
| [`startup-gruender`](./startup-gruender) | Startup-Gründer: 18 Skills für eine zügige UG- oder GmbH-Gründung mit Satzung und Gesellschaftervereinbarung DE/EN. Cap Table, Geschäftsführung, Statusprüfung, Beirat, Geldwäsche und Vollzug; Seed bis Serie B als Folgerouten. Mit Werkstatt und Schnittflug-Testakte. |
| [`startup-hr-personalabteilung-berlin`](./startup-hr-personalabteilung-berlin) | Personalabteilungs- und HR-Operations-Plugin für ein Berliner Start-up mit ca. 100 Beschäftigten: Arbeitsverträge, Payroll/DATEV-Schnittstelle, Personalakten, Datenschutz, AGG-Vorfälle, Betriebsrat, Benefits, Fehlzeiten, Kündigungen, Happiness-Management und Chef-Briefings. |
| [`status-navigator-step-plan`](./status-navigator-step-plan) | Dokumentenlagen in eine Excel-Arbeitsmappe mit Überblick, vorhandenen und fehlenden Unterlagen sowie nächsten Arbeitsschritten überführen. Optional eine interaktive Übersicht erzeugen, wenn die Oberfläche dies unterstützt. Keine rechtliche Bewertung. |
| [`steuerrecht-anwalt-und-berater`](./steuerrecht-anwalt-und-berater) | Steuerrecht für Anwalt (anw- FAO Paragraf 9) und Steuerberater (stb-): Einspruch Klage FG Außenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss. |
| [`strafanzeige-vorbereiter`](./strafanzeige-vorbereiter) | Vorsichtiger Strafanzeigen-Vorbereiter: prüft Anfangsverdacht, Beweise, Strafantrag, Risiken falscher Verdächtigung, Alternativen und erstellt nur bei tragfähiger Tatsachengrundlage eine nüchterne Strafanzeige. |
| [`strafbefehl-verteidiger`](./strafbefehl-verteidiger) | Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| [`strafvollzug-jva`](./strafvollzug-jva) | Strafvollzug in der JVA aus Sicht von Gefangenen, Angehörigen, Anwälten, Anstalt und Gericht bearbeiten. Landesrecht, Grundrechte, Alltag, Lockerungen und gerichtlichen Rechtsschutz prüfen und konkrete Anträge, Bescheide oder Entscheidungsentwürfe erstellen. |
| [`strafzumessung`](./strafzumessung) | Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur großen Strafkammer. Paragraf 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewährung Paragraf 56 Paragraf 49 Regelbeispiele besonders schwerer Fall Verständigung Paragraf 257c StPO TOA Paragraf 46a Gesamtstrafe Paragraf 55 JGG. |
| [`strassennutzung-genehmigungen`](./strassennutzung-genehmigungen) | Öffentliches Straßen- und Straßenverkehrsverwaltungsrecht: zehn Skills für Zufahrt, Parken, Laden, Poller, Schulstraßen, Fahrräder, Sondernutzung, Ausnahmen und Rechtsschutz. |
| [`strassenrecht-infrastruktur`](./strassenrecht-infrastruktur) | Straßenrecht-Plugin für Bundesfernstraßen, Landesstraßen, Gemeindestraßen, Widmung, Planfeststellung, Sondernutzung, Baulast und Erhaltung. |
| [`strassenverkehrsrecht-stvo`](./strassenverkehrsrecht-stvo) | StVO-/Straßenverkehrsrecht-Plugin für Verkehrsregeln, Zeichen, Anordnungen, Ausnahmegenehmigungen, Fahrerlaubnis, Bußgeld-Schnittstellen und Behördenpraxis. |
| [`subsumtions-pruefer`](./subsumtions-pruefer) | Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung. |

</details>

<a id="t"></a>
<details>
<summary>T</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`tabellenreview-3d`](./tabellenreview-3d) | 3D-Tabellenreview als Würfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette. |
| [`telekommunikationsrecht`](./telekommunikationsrecht) | Großes Telekommunikationsrecht-Plugin für TKG, Bundesnetzagentur, Internetanschlüsse, Anbieterwechsel, Kundenschutz, Netzregulierung, Frequenzen, Nummerierung, Sonderkartellrecht, Datenschutz und Sicherheitsanforderungen. |
| [`tierschutzrecht`](./tierschutzrecht) | Tierschutzrecht-Plugin für TierSchG, BGB Paragraf 90a, Haltung, Zucht, Transport, Tierversuche, Behördenverfahren, Strafrecht, Bußgeld und zivilrechtliche Tierfälle. |
| [`transparenzregister-assistent`](./transparenzregister-assistent) | Transparenzregister: Kontrollketten ermitteln, Meldungen und Berichtigungen vorbereiten, Einsicht und Unstimmigkeiten bearbeiten sowie optional freigegebene Portalhandlungen begleiten. Zehn Fachskills und ein Hauptproblem-Skill mit drei Akten. |

</details>

<a id="u"></a>
<details>
<summary>U</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`umwandlungssteuerrecht`](./umwandlungssteuerrecht) | Begleitet Umstrukturierungen von der Ausgangsbilanz bis zu Anträgen und Nachweisen. Prüft steuerliche Übertragungsstichtage, Wertansätze, stille Reserven, Gegenleistungen und Sperrfristen. |
| [`umweltrecht`](./umweltrecht) | Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD. |
| [`umweltschutzverband-verbandsklage`](./umweltschutzverband-verbandsklage) | Plugin für Umweltverbände: UmwRG, Aarhus, UIG, UVP, BImSchG, Planfeststellung, Paragraf 47 VwGO, Naturschutz, Klima, Verbandsklage und Eilrechtsschutz. |
| [`un-kaufrecht-cisg`](./un-kaufrecht-cisg) | UN-Kaufrecht für internationale Warenverträge: CISG-Anwendung, Abwahl, kollidierende AGB, Lieferung, Mängelrüge, Nachbesserung, Aufhebung, Schaden und Transport. Zehn Fachskills und ein Hauptskill begleiten beide Vertragsseiten bis zum fertigen Dokument. |
| [`untersuchungshaft`](./untersuchungshaft) | Untersuchungshaft für Gericht, Staatsanwaltschaft, Verteidigung und Betroffene: zehn Skills zu Haftbefehl, Vorführung, Haftverschonung, Haftprüfung, Beschwerde, Haftdauer, Vollzugsrechten und Jugendhaft. Mit konkreten Anträgen und Entscheidungsvorlagen. |
| [`urheberrecht-de-eu`](./urheberrecht-de-eu) | Deutsches und EU-Urheberrecht für Werkhöhe, Musik, KI, TDM, Software, Lizenzen, Abmahnung, Schranken, Leistungsschutz und Rechteclearing. |
| [`urteilsbauer-relationsmacher`](./urteilsbauer-relationsmacher) | Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO. |
| [`us-bankruptcy-code`](./us-bankruptcy-code) | US Bankruptcy Code Title 11: Chapters 7/9/11/12/13/15, Automatic Stay, Claims, DIP, 363 Sales, Plans und Cross-Border. |
| [`us-copyright-registrierung-verlag`](./us-copyright-registrierung-verlag) | US Copyright Act für deutsche Verlage und Rechteinhaber: Title 17, Registrierung, Rechte, Fair Use, DMCA, Musik, AI, Litigation und Deals. |
| [`us-sanktionspruefer`](./us-sanktionspruefer) | US-Sanktionen für Unternehmen und Kanzleien: OFAC-Treffer, Eigentum, US-Bezug, Terrorismusregime, Geschäfte, Lizenzen, Meldungen und EU-Rechtskonflikte. Ein Hauptskill und neun Fachskills führen zum belegten Vermerk, Antrag oder Schreiben. |

</details>

<a id="v"></a>
<details>
<summary>V</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`venture-capital-geber`](./venture-capital-geber) | VC-Geber-Plugin für deutsche Venture-Capital-Investoren, Family Offices, Angels und junge VCs: Sourcing, Deal-Tracking, Wandeldarlehen, SAFE, Pre-Seed, Series A/B, Cap Table, Follow-on, Portfolio-Updates, KAGB/BaFin-Grenzen, EU/CH/UK/US-Brücken und legitime Deal-Taktik. |
| [`verarbeitungsverzeichnis`](./verarbeitungsverzeichnis) | Verzeichnisse von Verarbeitungstätigkeiten für Unternehmen anlegen und laufend pflegen. Rollen, Rechtsgrundlagen, Löschung, Dienstleister, Risiken und DSFA prüfen; Änderungen nachvollziehen und Excel, Word sowie strukturierte Austauschdateien erzeugen. |
| [`verbraucher-rechtsstaat-alltag`](./verbraucher-rechtsstaat-alltag) | Kleines, hilfreiches Plugin für Verbraucher: E-Commerce, Kaufrecht, Reparaturen, kleine Dienstleistungen, Rechnungen, Inkasso, Plattformen, Behördenbriefe und Gerichtspost verständlich einordnen und vorsichtig reagieren. |
| [`verbraucherinsolvenz-schuldenbereinigung`](./verbraucherinsolvenz-schuldenbereinigung) | Verbraucherinsolvenz und Schuldenbereinigung nach InsO: außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, Antrag, Restschuldbefreiung, P-Konto, ehemalige Selbstständige und lebensnahe Verfahrensführung. |
| [`verbraucherschutzrecht-pruefer`](./verbraucherschutzrecht-pruefer) | Großer Verbraucherschutz-Prüfer für BGB, EGBGB, UWG, UKlaG, VSBG, E-Commerce, digitale Produkte, Reise, Finanzen, Energie, Gesundheit und Alltag. |
| [`verbraucherschutzverband-durchsetzung`](./verbraucherschutzverband-durchsetzung) | Plugin für Verbraucherverbände: VDuG, UKlaG, UWG, Abhilfeklage, Musterfeststellung, Unterlassung, Register, Finanzierung, Vergleich und Kampagnenakte. |
| [`vereinsrecht-vereinsmanager`](./vereinsrecht-vereinsmanager) | Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine. |
| [`verfassungsrecht`](./verfassungsrecht) | Deutsches Verfassungsrecht: BVerfG-Recherche, Prozessarten-Navigator nach Paragraf 13 BVerfGG, Verfassungsbeschwerde, Paragraf 32-BVerfGG-Eilrechtsschutz, Organstreit, Bund-Länder-Streit, Parteienverfahren, Normenkontrolle, Grundrechte, EU-Grundrechte und Gesetzgebungskompetenz. |
| [`vergabestelle-behoerden`](./vergaberecht-werkstatt/vergabestelle-behoerden) | Vergabestellen legen Ordner, ZIP oder Portalexport ab und starten ohne Skillwahl. Das Plugin sichert Fristen und Regime, baut Bestangebot, LV und Uploadpaket und verteidigt Rüge, VK und OLG. |
| [`vergesellschaftung-artikel-15`](./vergesellschaftung-artikel-15) | Vergesellschaftung nach Artikel 15 GG: Gegenstände und Anteile, Landeskompetenz und Hessenrecht, gemeinwirtschaftliche Trägerschaft, Gesetzesentwurf, Entschädigung, Energienetze, Unionsrecht und Rechtsschutz aus der konkreten Akte bearbeiten. |
| [`verhaeltnismaessigkeitspruefer`](./verhaeltnismaessigkeitspruefer) | Verhältnismäßigkeit strukturiert prüfen: legitimes Ziel, Geeignetheit, Erforderlichkeit und Angemessenheit mit Grundrechten, Gegenargumenten und belegter Rechtsprechung verbinden. Deutsche, europäische und rechtsvergleichende Maßstäbe getrennt auswerten. |
| [`verkehr-infrastrukturrecht`](./verkehr-infrastrukturrecht) | Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende. |
| [`verkehrsowi-verteidiger`](./verkehrsowi-verteidiger) | Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. |
| [`verlagsrecht-buchpreisbindung`](./verlagsrecht-buchpreisbindung) | Plugin für Verlagsrecht, Verlagsgesetz, Autoren- und Herausgeberverträge, Buchpreisbindung, Titelschutz, Vertrieb, E-Book, Hörbuch und verlagsnahe Compliance. |
| [`verlagsredaktion`](./verlagsredaktion) | Verlagsdesk für juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsübergabe. |
| [`versammlungsrecht`](./versammlungsrecht) | Praxisplugin für Versammlungsrecht und Versammlungsfreiheit: Anzeige unter freiem Himmel, Landesrecht, Behörde, Fristen, Spontan- und Eilversammlung, Ordner, Kooperationsgespräch, Auflagen, Verbot, Eilrechtsschutz und Durchführung ohne vorauseilende Selbstzensur. |
| [`versicherungsrecht`](./versicherungsrecht) | Großes Versicherungsrecht-Plugin für VVG, VAG, europäische Versicherungsaufsicht, Lebensversicherung, BU, PKV, Rechtsschutz, Kreditversicherung, D&O, Cyber, Sach- und Haftpflichtdeckung. |
| [`vertragsausfueller`](./vertragsausfueller) | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten. |
| [`vertragserstellung`](./vertragserstellung) | Kompakte Vertragswerkstatt für einzelne Geschäfte zwischen Unternehmen. Zehn Skills erstellen Verträge, Klauseln und Nachträge bis zur abgestimmten Endfassung. |
| [`vertragsrecht`](./vertragsrecht) | Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB Paragrafen 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen. |

</details>

<a id="w"></a>
<details>
<summary>W</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`wahlkampfrecht-praxis`](./wahlkampfrecht-praxis) | Wahlkampfrecht und Wahlkampfpraxis für Parteien, Kandidierende und Kampagnenteams: Strategie, Plakatierung, Social Media, Datenschutz, politische Werbung, Parteienfinanzierung, Desinformation, Veranstaltungen, Schulen, Podien, Wahltag und Compliance. |
| [`wandeldarlehen-lebenszyklus`](./wandeldarlehen-lebenszyklus) | Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. |
| [`weg-hausverwaltung`](./weg-hausverwaltung) | WEG-Hausverwaltung von Belegen und Bankbewegungen über Jahresabrechnung, Eigentümerrückfragen und Mietüberleitung bis zu Beschlüssen, Handwerkeraufträgen und Schadenfällen einschließlich Diebstahl und Bettwanzen. |
| [`weltraumrecht`](./weltraumrecht) | Großes Plugin für deutsches, europäisches und internationales Weltraumrecht: Raumfahrtverträge, Satelliten, Haftung, Weltraumbahnhof, Raketen, Raumstationen, Frequenzen, Exportkontrolle und Space Property. |
| [`wirtschaftsanwalt`](./wirtschaftsanwalt) | Laufende Unternehmensberatung im Mittelstand: zehn ausführende Skills verbinden Vertrags-, Personal-, Gesellschafts-, Daten- und Liquiditätsfragen mit konkreten Geschäftsentscheidungen und fertigen Dokumenten. |
| [`word-legal-ai-plugin-and-skill-for-german-lawyers`](./word-legal-ai-plugin-and-skill-for-german-lawyers) | Word Legal AI for German Lawyers: Kaltstart, Kanzleistil, makrofreies Word-Finish, Verträge, Schriftsätze, Memos, Redlines, Klauselbibliothek, Defensive Drafting, Term Sheet, DE-EN Bilingual, US/UK Legal Writing und englische Verträge nach deutschem Recht. |

</details>

<a id="z"></a>
<details>
<summary>Z</summary>

| Plugin | Beschreibung |
| --- | --- |
| [`zahlungsunfaehigkeits-und-ueberschuldungspruefer`](./zahlungsunfaehigkeits-und-ueberschuldungspruefer) | Rekonstruiert Zahlungsunfähigkeit und insolvenzrechtliche Überschuldung aus Bank- und Buchungsunterlagen. Prüft die Dreiwochenbilanz, Zahlungseinstellung, Fortbestehensprognose, stille Reserven und Nachrang. Mit Stichtagsrechner und drei Anfechtungsakten. |
| [`zitierweise-deutsches-recht`](./zitierweise-deutsches-recht) | Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. |
| [`zugewinnausgleich`](./zugewinnausgleich) | Zugewinnausgleich bei Trennung und Scheidung: zehn Skills für die belegte Berechnung des Zugewinns, Erbschaft, Immobilien, Unternehmen, Auskunft und Vergleich bis zum beauftragten Ergebnis. |
| [`zwangsverwaltung-zvg`](./zwangsverwaltung-zvg) | Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |
| [`zwangsvollstreckung`](./zwangsvollstreckung) | Plugin Zwangsvollstreckung Paragrafen 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, Paragraf 802l Kontensuche, Vermögensauskunft, Räumung, Paragraf 800 ZPO Notar, Paragraf 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, Paragraf 765a Härtefall, Schuldnerschutz. |

</details>

<!-- END PLUGIN-KATALOG (auto-generated) -->
