# Gesellschaftsrecht-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Gesellschaftsrecht für GmbH, AG und Personengesellschaften: Beschlüsse, Gesellschafterliste, Satzung, Organhaftung, Streit, Kapitalerhaltung, Umwandlung, Register und Transaktionen.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`gesellschaftsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/gesellschaftsrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/gesellschaftsrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/gesellschaftsrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/gesellschaftsrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/gesellschaftsrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/gesellschaftsrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Gesellschaftsrecht-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`gesellschaftsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/gesellschaftsrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`gesellschaftsrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/gesellschaftsrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`gesellschaftsrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/gesellschaftsrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [12 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

[Grundakten für Gesellschaftsrecht mit Eingangspost, Rückfragen und Belegen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/docs/grundakten-lebenswelt/Fachakten.md#gesellschaftsrecht)

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Erbrecht — Unternehmernachfolge und Testamentsvollstrecker in Würzburg](../testakten/erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg/README.md) | [Gesamt-PDF](../testakten/erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg/gesamt-pdf/erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg_gesamt.pdf) | [`testakte-erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg.zip) | [`testakte-erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-erbrecht-unternehmernachfolge-testamentsvollstrecker-wuerzburg-einzelpdfs.zip) |
| [NeuroChain Labs — Gründung eines digitale Systeme/Krypto-Startups in Berlin, Musterprotokoll vs. individuelle Satzung](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll/gesamt-pdf/gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll_gesamt.pdf) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll.zip) | [`testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-ki-krypto-startup-berlin-musterprotokoll-einzelpdfs.zip) |
| [Röschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation](../testakten/gesellschaftsgruender-streit-roeschen-tech/README.md) | [Gesamt-PDF](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) | [`testakte-gesellschaftsgruender-streit-roeschen-tech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsgruender-streit-roeschen-tech-einzelpdfs.zip) |
| [Zwei Blätter, ein falscher Name · Kontorwerft eGbR](../testakten/gesellschaftsrecht-egbr-grundbuch-register-bremen/README.md) | [Gesamt-PDF](../testakten/gesellschaftsrecht-egbr-grundbuch-register-bremen/gesamt-pdf/gesellschaftsrecht-egbr-grundbuch-register-bremen_gesamt.pdf) | [`testakte-gesellschaftsrecht-egbr-grundbuch-register-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsrecht-egbr-grundbuch-register-bremen.zip) | [`testakte-gesellschaftsrecht-egbr-grundbuch-register-bremen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/gesellschaftsrecht-egbr-grundbuch-v1.0.0/testakte-gesellschaftsrecht-egbr-grundbuch-register-bremen-einzelpdfs.zip) |
| [Akte Kometenfalter Systems GmbH — Series A Project Comet Moth](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/README.md) | [Gesamt-PDF](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/gesamt-pdf/gesellschaftsrecht-legal-english-frankfurt-startup_gesamt.pdf) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gesellschaftsrecht-legal-english-frankfurt-startup-einzelpdfs.zip) |
| [Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/README.md) | [Gesamt-PDF](../testakten/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona/gesamt-pdf/handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona_gesamt.pdf) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona-einzelpdfs.zip) |
| [Mandatsbeziehung Nordstern BioTherapeutics — Kanzlei Falkenried](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/README.md) | [Gesamt-PDF](../testakten/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech/gesamt-pdf/mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech_gesamt.pdf) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech.zip) | [`testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mandatsbeziehung-kanzlei-rechtsabteilung-nordstern-biotech-einzelpdfs.zip) |
| [Codeforst / Sonnenklee - RouteLuchs](../testakten/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen/README.md) | [Gesamt-PDF](../testakten/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen/gesamt-pdf/softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen_gesamt.pdf) | [`testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen.zip) | [`testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-softwarerecht-saas-ki-lizenzstreit-codeforst-muenchen-einzelpdfs.zip) |
| [Statusfeststellungsakte GmbH-Geschäftsführer Minderheitsbeteiligung Erlangen](../testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen/README.md) | [Gesamt-PDF](../testakten/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen/gesamt-pdf/statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen_gesamt.pdf) | [`testakte-statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen.zip) | [`testakte-statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-statusfeststellung-gmbh-geschaeftsfuehrer-minderheit-erlangen-einzelpdfs.zip) |
| [Steuerrecht: Kleine Heizungsbau-GmbH und Gesellschafternähe in Bamberg](../testakten/steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg/README.md) | [Gesamt-PDF](../testakten/steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg/gesamt-pdf/steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg_gesamt.pdf) | [`testakte-steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg.zip) | [`testakte-steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-steuer-heizungsbau-gmbh-vga-lohnsteuer-bamberg-einzelpdfs.zip) |
| [Speichenraum GbR in Leipzig](../testakten/vertragserstellung-gbr-fahrradwerkstatt-leipzig/README.md) | [Gesamt-PDF](../testakten/vertragserstellung-gbr-fahrradwerkstatt-leipzig/gesamt-pdf/vertragserstellung-gbr-fahrradwerkstatt-leipzig_gesamt.pdf) | [`testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig.zip) | [`testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragserstellung-gbr-fahrradwerkstatt-leipzig-einzelpdfs.zip) |
| [Suppenfaden UG in Regensburg](../testakten/vertragserstellung-ug-eventkueche-regensburg/README.md) | [Gesamt-PDF](../testakten/vertragserstellung-ug-eventkueche-regensburg/gesamt-pdf/vertragserstellung-ug-eventkueche-regensburg_gesamt.pdf) | [`testakte-vertragserstellung-ug-eventkueche-regensburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragserstellung-ug-eventkueche-regensburg.zip) | [`testakte-vertragserstellung-ug-eventkueche-regensburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragserstellung-ug-eventkueche-regensburg-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Gesellschaftsrecht für GmbH, AG oder Personengesellschaft bearbeiten: Beschluss, Satzung, Gesellschafterliste, Organhaftung, Streit, Kapital, Umwandlung oder Register.
Abläufe für gesellschaftsrechtliche Mandate in deutschen Kanzleien und Rechtsabteilungen: M&A-Transaktionen, Organe und Protokollwesen, Gesellschafts-Compliance und Unternehmensführung. Aktiviere nur die Module, die für deine Praxis relevant sind. Ein Praxisprofil kann die wiederkehrende Arbeit unterstützen. Ein klarer Auftrag mit Satzung, Beschlussunterlagen oder Datenraum wird jedoch direkt bearbeitet; nur entscheidende fehlende Angaben werden nachgefragt und Antworten im begonnenen Dokument umgesetzt.

**Jedes Ergebnis ist ein Entwurf zur anwaltlichen Überprüfung – zitiert, markiert und gesperrt – kein Rechtsgutachten.** Das Plugin übernimmt die Arbeit: liest Dokumente, wendet dein Playbook an, findet die Issues, erstellt den Bericht. Ein Rechtsanwalt prüft, verifiziert und entscheidet. Zitate sind mit Quellen gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu prüfen sind. Mandantengeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) wird konservativ gewahrt. Folgenreiche Handlungen – Einreichung, Versendung, Beurkundung – werden durch ausdrückliche Bestätigung gesperrt.


## Für wen

| Rolle | Aktive Module |
|---|---|
| **M&A-Anwalt (Kanzlei oder Inhouse)** | M&A |
| **Gesellschaftssekretär / Corporate Secretary** | Organe & Protokoll |
| **General Counsel, Aktiengesellschaft** | M&A + Börse/Kapitalmarkt + Organe & Protokoll |
| **General Counsel, GmbH** | M&A + Organe & Protokoll + Gesellschafts-Compliance |
| **Legal Ops / Solo-GC** | Nach Bedarf – beliebige Kombination |

## Erster Start

```
/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: kaltstart-interview
```

Optional für die Einrichtung wiederkehrender Mandate; kein Pflichtschritt vor einem konkreten Dokumentauftrag. Schreibt bei gewünschter Einrichtung ein modulares Praxisprofil nach:
`~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/CLAUDE.md`

Deine Konfiguration bleibt dort und übersteht Plugin-Updates.

Dealspezifisches Setup (nur M&A-Modul):

```
/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: kaltstart-interview --neues-mandat
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: kaltstart-interview` | Modulares Kaltstart oder `--neues-mandat` / `--modul [m&a \| organe \| boerse \| compliance]` |
| `/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: dd-findings-extraktion [ordner]` | Datenraum-Dokumente lesen, Issues im Hauskatalog extrahieren |
| `/gesellschaftsrecht:register-und-vollzug-bearbeiten Thema: tabellenpruefung` | Tabellarisches Review – eine Zeile pro Dokument, eine Spalte pro Datenpunkt, jede Zelle mit Fundstelle, Excel-Ausgabe |
| `/gesellschaftsrecht:organe-und-vertretung-bearbeiten Thema: wesentliche-vertraege-anlage` | Wesentliche-Verträge-Anlage (Disclosure Schedule) aus DD-Findings |
| `/gesellschaftsrecht:register-und-vollzug-bearbeiten Thema: vollzugs-checkliste` | Vollzugscheckliste – was blockiert den Closing, kritischer Pfad |
| `/gesellschaftsrecht:gruendung-und-gesellschaftsvertrag-bearbeiten Thema: gesellschafterbeschluss` | Gesellschafterbeschluss im schriftlichen Verfahren § 48 II GmbHG, Muster mit Unterzeichner-Tracker |
| `/gesellschaftsrecht:gruendung-und-gesellschaftsvertrag-bearbeiten Thema: gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – init, Bericht, Update, Audit, Export |
| `/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: integrations-management` | Post-Closing-Integrationsplan, Zustimmungsregister, Vertragsübertragung, Statusberichte |
| `/gesellschaftsrecht:arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten Thema: mandat-arbeitsbereich-gesr-corporate` | Mandatsarbeitsbereiche verwalten (Mehrmandat-Kanzleien) – neu, liste, wechsel, schließ, keins |
| `/gesellschaftsrecht:gruendung-und-gesellschaftsvertrag-bearbeiten Thema: gmbh-gruendung` | GmbH-Gründung Schritt-für-Schritt: Gesellschaftsvertrag, Notar, Handelsregister |
| `/gesellschaftsrecht:haftung-und-gesellschaftsstreit-bearbeiten Thema: handelsregisteranmeldung-integrations` | Handelsregisteranmeldungen: HRB/HRA, Änderungen, Kapitalmaßnahmen |

## Voraussetzungen

Mehrere Funktionen verweisen auf Slack, Google Drive, SharePoint, Box, Datasite- oder VDR-Integrationen. Diese erfordern MCP-Server in deiner Umgebung – sie sind **nicht im Plugin enthalten**. Ohne sie greift das Plugin auf lokale Dateiausgabe zurück (Entwürfe lokal gespeichert statt in einen Kanal gepostet, Tracker-Dateien auf Festplatte statt in einem verbundenen Repository).

MCP-Server konfigurieren unter `.mcp.json` auf Repo- oder Benutzerebene. Skills und Agenten erkennen zur Laufzeit, was verfügbar ist, und passen ihr Verhalten an.

## Skills

| Skill | Modul | Zweck |
|---|---|---|
| **kaltstart-interview** | Alle | Modulares Interview – aktiviert nur relevante Abschnitte |
| **dd-findings-extraktion** | M&A | Datenraum-Dokumente → Issues im Hauskatalog, nach Kategorie |
| **tabellarisches-review** | M&A | Dokumentensatz gegen typisiertes Spaltenformat prüfen; Zellen mit Fundstelle; `.xlsx` / `.csv` / Markdown; speist wesentliche-verträge-anlage |
| **dealteam-zusammenfassung** | M&A | Stufenbriefings: Geschäftsführung / Deal-Lead / Arbeitsteam |
| **wesentliche-verträge-anlage** | M&A | Disclosure Schedule gemäß SPA-Definition |
| **vollzugs-checkliste** | M&A | Selbstaktualisierend: nimmt Einträge aus DD und Schedule-Builds auf |
| **ki-werkzeug-übergabe** | M&A | Luminance/Kira-Integration – Massenextraktion + QA-Schicht |
| **aufsichtsrat-protokoll** | Organe & Protokoll | Kalendererkennung für Sitzungen → Protokollentwurf im Hausformat (AG-Aufsichtsrat: Paragraf 107 AktG; GmbH-Aufsichtsrat: Paragraf 52 GmbHG und Satzung, nicht die Gesellschafterversammlung nach Paragraf 48 GmbHG) |
| **gesellschafterbeschluss** | Organe & Protokoll | Beschlüsse im schriftlichen Verfahren § 48 II GmbHG mit Mustersuche aus dem Beschluss-Repository; Hinweis bei wesentlichen Einzelmaßnahmen |
| **gesellschafts-compliance** | Gesellschafts-Compliance | Compliance-Kalender-Tracker (YAML); Einreichungsfristen nach Rechtsträger; Bilanzpublizität § 325 HGB; Transparenzregister § 20 GwG; Gesundheitsaudit; CSV-Export |
| **post-merger-integration** | M&A | Post-Closing-Integrationsplan; phasenweiser Arbeitsplan (Tag 1/30/90/180); Zustimmungsregister mit SPA-Fristen; Vertragsübertragung; Wochenstatusberichte |
| **mandat-arbeitsbereich** | Alle | Mandatsarbeitsbereiche erstellen, auflisten, wechseln und schließen für Mehrmandat-Kanzleien; isoliert jeden Mandanten/Auftrag, damit Kontext nicht übergreift |
| **gmbh-gründung** | Compliance | GmbH-Gründung: Gesellschaftsvertrag, Stammkapital, Notar, Handelsregister, IHK, Gewerbe |
| **gesellschafterbeschluss-vorlagen** | Organe | Beschlussvorlagen GmbH/AG, Beschlussfähigkeit, Mehrheiten, Anfechtungsklage |
| **handelsregisteranmeldung** | Compliance | HRB/HRA-Anmeldungen, Änderungen, Kapitalmaßnahmen, notarielle Form |

## Interaktive Befehle vs. geplante Agenten

Die Befehle laufen auf deinen Auftrag für das aktive Mandat. Eine wiederkehrende Überwachung setzt eine ausdrücklich beauftragte und tatsächlich eingerichtete Zeitplanung sowie erreichbare Datenquellen voraus. Die Installation allein startet keinen Hintergrundlauf:

| Agent | Modul | Was er beobachtet | Standard-Rhythmus |
|---|---|---|---|
| **datenraum-monitor** | M&A | VDR auf neue Dokumenten-Uploads; markiert Uploads, die zu Hochprioritätskategorien passen; aktualisiert Vollzugschecklisten-Status | Wöchentlich |

## Integrationen

**Verbinde zuerst ein Recherchetool – die Zitier-Absicherung hängt davon ab.** Ohne eines wird jedes Zitat mit `[prüfen]` markiert und der Prüfer-Hinweis über jedem Ergebnis vermerkt, dass Quellen nicht verifiziert wurden. Skills funktionieren in beiden Fällen; ein Recherchetool (amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang, Westlaw DE) verlagert Verifikationsarbeit aus deiner Hand.

Als mögliche externe Anbindungen beschrieben, nicht als mitgelieferte Dienste oder erteilte Zugriffsrechte:

- **Slack** – Nachrichten suchen, Kanäle lesen, Diskussionen finden
- **Google Drive** – Dokumente suchen, lesen und abrufen
- **Box** – Datenraum und Dokumentenverwaltung

Datasite, Intralinks und weitere VDR-Connectoren können in `.mcp.json` ergänzt werden, wenn Partner-URLs verfügbar sind.

## Recht und Quellen

Maßgebliche Gesetze dieses Plugins:

- **GmbHG** – Gesetz betreffend die Gesellschaften mit beschränkter Haftung
- **AktG** – Aktiengesetz
- **HGB** – Handelsgesetzbuch (§§ 238 ff. Buchführung, §§ 290 ff. Konzernabschluss, § 325 Bilanzpublizität)
- **UmwG** – Umwandlungsgesetz (Verschmelzung, Spaltung, Formwechsel)
- **WpÜG** – Wertpapiererwerbs- und Übernahmegesetz (öffentliche Übernahmen, Pflichtangebote)
- **MoPeG** – Gesetz zur Modernisierung des Personengesellschaftsrechts (GbR-Reform 2024)
- **WEG** – Wohnungseigentumsgesetz (soweit gesellschaftsrechtlich relevant)
- **GwG** – Geldwäschegesetz (Transparenzregister § 20 GwG)

Zitierweise nach `../references/zitierweise.md` (BGH-Stil). Punktuell am 16.10.2026 zusätzlich [Paragraf 52 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__52.html) gelesen: Für den GmbH-Aufsichtsrat sind dessen Verweisungen und die Satzung maßgeblich, nicht pauschal das Recht der Gesellschafterversammlung. Zusätzlich wurden am 16.10.2026 [Paragraf 110 AktG](https://www.gesetze-im-internet.de/aktg/__110.html), [Paragraf 130 AktG](https://www.gesetze-im-internet.de/aktg/__130.html) und [Paragraf 48 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__48.html) vollständig gelesen: keine allgemeine 14-Tage-Mindestladung aus Paragraf 110, begrenzte Ausnahme zur notariellen Niederschrift in Paragraf 130 Absatz 1 Satz 3 und unterschriebene Niederschrift der Einpersonengesellschaft nach Paragraf 48 Absatz 3. Die entsprechenden Prüf- und Musterstellen im Protokoll-Skill sind korrigiert; seine übrigen aktienrechtlichen Detailregeln wurden nicht vollständig neu verifiziert.

## Lernen

Dein Praxisprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/CLAUDE.md` ist nicht statisch – es verbessert sich mit der Nutzung des Plugins. Skills informieren dich, wenn ein Ergebnis einen Standard verwendet, den du anpassen solltest. Du kannst das Setup erneut ausführen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine neue Position zu speichern.

## M&A-Hinweise

- Die Issue-Extraktion wendet Wesentlichkeitsschwellen an – nicht jedes Dokument wird gelesen, wenn die Schwelle Top-N nach Wert vorschreibt.
- Käufer- und Verkäuferseite werden beide unterstützt. Das Praxisprofil erfasst, welche Seite für dieses Mandat gilt; Skills passen ihre Haltung entsprechend an.
- Due Diligence nutzt insbesondere Datenraum, Fragen und Antworten sowie die Offenlegungserklärung. Materielle Auskunfts- oder Einsichtsansprüche benötigen eine eigene Grundlage, etwa bei Vorliegen der Voraussetzungen des Paragrafen 810 BGB. Paragraf 142 und 144 ZPO betreffen gerichtliche Anordnungen im Prozess; das selbständige Beweisverfahren nach Paragraf 485 ff. ZPO ist ein eigener, voraussetzungsgebundener Weg. Die Stufenklage nach Paragraf 254 ZPO schafft keinen materiellen Auskunftsanspruch. Den punktuellen amtlichen Normabgleich vom 16.10.2026 mit Quellen und Grenzen dokumentiert der [DD-Fachskill](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/dd-findings-extraktion/FACHINHALT.md).
- KI-Tool-Übergabe (Luminance/Kira) ist optional. Wenn das Praxisprofil kein Tool angibt, läuft alle Extraktion über den direkten Skill.
- Die Vollzugscheckliste wird aus dem SPA initialisiert und aktualisiert sich selbst, wenn die DD Zustimmungserfordernisse aufdeckt.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **118 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Gründung und Gesellschaftsvertrag | [`gruendung-und-gesellschaftsvertrag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) |
| 3. Organe und Vertretung | [`organe-und-vertretung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/organe-und-vertretung-bearbeiten/SKILL.md) |
| 4. Gesellschafter und Beschlussfassung | [`gesellschafter-und-beschlussfassung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) |
| 5. Kapital und Strukturmaßnahmen | [`kapital-und-strukturmassnahmen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) |
| 6. Register und Vollzug | [`register-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/register-und-vollzug-bearbeiten/SKILL.md) |
| 7. Haftung und Gesellschaftsstreit | [`haftung-und-gesellschaftsstreit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) |
| 8. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 9. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/einstieg-routing/SKILL.md) | Für eine konkrete Gesellschaftsmaßnahme: verbindet Beschluss, Vertretungsnachweis, Vertrag und Registervollzug und liefert die dafür beauftragten Entwürfe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/einstieg-routing/SKILL.md) |
| [`gesellschafter-und-beschlussfassung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Gesellschafter und Beschlussfassung: Einladung, Stimmrecht, Mehrheiten, Informationsrecht, Treuepflicht und Minderheitenschutz im konkreten Konflikt bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gesellschafter-und-beschlussfassung-bearbeiten/SKILL.md) |
| [`gruendung-und-gesellschaftsvertrag-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Gründung und Gesellschaftsvertrag: Rechtsform, Kapital, Satzung, Beteiligung und Vollzug bis zum abgestimmten Gründungstext führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/gruendung-und-gesellschaftsvertrag-bearbeiten/SKILL.md) |
| [`haftung-und-gesellschaftsstreit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Haftung und Gesellschaftsstreit: Pflichtverletzung, Anspruchsinhaber, Darlegung, Eilrechtsschutz und Einigung zu einem begründeten Arbeitsprodukt führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/haftung-und-gesellschaftsstreit-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/juristischer-argumentationskern/SKILL.md) | Gesellschaftsrechtlichen Fall bis zum Beschluss oder Anspruch lösen. Wertet vorhandene Unterlagen aus, entscheidet die fachlichen Weichen und liefert vollständigen Vertrags-, Beschluss- oder Schriftsatzentwurf mit tragender Hauptlinie, G... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kapital-und-strukturmassnahmen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Kapital und Strukturmaßnahmen: Finanzierung, Kapitalerhaltung, Umwandlung, Übertragung und Ausscheiden mit den Vertrags- und Registerunterlagen abgleichen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/kapital-und-strukturmassnahmen-bearbeiten/SKILL.md) |
| [`organe-und-vertretung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/organe-und-vertretung-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Organe und Vertretung: Geschäftsführung, Aufsichtsrat, Bestellung, Abberufung, Vollmacht und Vertretungsmacht anhand der Beschlüsse prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/organe-und-vertretung-bearbeiten/SKILL.md) |
| [`register-und-vollzug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/register-und-vollzug-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Register und Vollzug: Anmeldung, Gesellschafterliste, Publizität, Nachweise und Zwischenverfügung bis zum einreichbaren Dokument bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/register-und-vollzug-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Gesellschaftsrechtliche Fallprüfung: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für neue gesellschaftsrechtliche Aufträge: bestimmt Rechtsform, Mandantenrolle, Vertretung, maßgebliche Fassungen und anstehende Entscheidungen oder Fristen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gesellschaftsrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
