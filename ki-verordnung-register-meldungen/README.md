# 1. KI-Verordnung Register und Meldungen

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft Register- und Meldepflichten der KI-Verordnung nach Rolle, System, Anlass und Zeitrecht. Erstellt Datensätze, Erstberichte, Ergänzungen und Anschreiben und hält Freigabe sowie tatsächlichen Eingang nach.

Dieses Plugin gehört zum Marketplace mit 310 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`ki-verordnung-register-meldungen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/ki-verordnung-register-meldungen.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/ki-verordnung-register-meldungen.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/ki-verordnung-register-meldungen.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/ki-verordnung-register-meldungen.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für 1. KI-Verordnung Register und Meldungen:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`ki-verordnung-register-meldungen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/ki-verordnung-register-meldungen.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`ki-verordnung-register-meldungen-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.md) · [`ki-verordnung-register-meldungen-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`ki-verordnung-register-meldungen-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.md) · [`ki-verordnung-register-meldungen-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.txt) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 310 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Testakte Mainbogen und der Vorfall in der Übungsleitstelle](../testakten/ki-meldung-mainbogen-notruf/README.md) | [Gesamt-PDF](../testakten/ki-meldung-mainbogen-notruf/gesamt-pdf/ki-meldung-mainbogen-notruf_gesamt.pdf) | [`testakte-ki-meldung-mainbogen-notruf.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-meldung-mainbogen-notruf.zip) | [`testakte-ki-meldung-mainbogen-notruf-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-meldung-mainbogen-notruf-einzelpdfs.zip) |
| [Testakte Fuldatal und die neue Antragspriorisierung](../testakten/ki-register-fuldatal-sozialhilfe/README.md) | [Gesamt-PDF](../testakten/ki-register-fuldatal-sozialhilfe/gesamt-pdf/ki-register-fuldatal-sozialhilfe_gesamt.pdf) | [`testakte-ki-register-fuldatal-sozialhilfe.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-fuldatal-sozialhilfe.zip) | [`testakte-ki-register-fuldatal-sozialhilfe-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-fuldatal-sozialhilfe-einzelpdfs.zip) |
| [1. Havelgrund Sozialamt mit geplanter Antragsassistenz](../testakten/ki-register-havelgrund-sozialamt/README.md) | [Gesamt-PDF](../testakten/ki-register-havelgrund-sozialamt/gesamt-pdf/ki-register-havelgrund-sozialamt_gesamt.pdf) | [`testakte-ki-register-havelgrund-sozialamt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-havelgrund-sozialamt.zip) | [`testakte-ki-register-havelgrund-sozialamt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-havelgrund-sozialamt-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

[Repository-Start](../README.md) · [Alle Skills](../SKILLS.md) · [Skill-Detailseite](../skills-index/ki-verordnung-register-meldungen.md) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md) · [Plugin-Dateien](.)

Version 445.35.2. Prüft Register- und Meldepflichten der KI-Verordnung nach Rolle, System, Anlass und Zeitrecht. Erstellt Datensätze, Erstberichte, Ergänzungen und Anschreiben und hält Freigabe sowie tatsächlichen Eingang nach.

## 1.1. Einstieg

Elf Skills: zehn Fachschritte und ein Hauptproblem-Skill. Nutzen Sie [Register und Meldungsfrage vollständig lösen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/register-und-meldung-loesen/SKILL.md), wenn der gesamte Vorgang bearbeitet werden soll. Die Werkstatt funktioniert als eigenständiger Prompt; der Mini führt denselben Entscheidungsablauf kompakt aus. Tatsächliche Portale und Versandfunktionen hängen von verfügbaren Werkzeugen und Zugängen ab. Dieses Paket behauptet keinen bereits eingebauten amtlichen Registeranschluss.

## 1.2. Prompts und Installation

- [Werkstatt lesen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.md)
- [Mini lesen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.md)
- [Hauptproblem lesen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-hauptproblem.md)
- [Plugin herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/ki-verordnung-register-meldungen.zip)

Claude nutzt die Skills im Plugin. Codex-kompatible Metadaten liegen ebenfalls bei. In ChatGPT können Sie den Mini als Projektanweisung und Werkstatt plus Referenzen als Dateien verwenden; eine tatsächliche Import- oder Portalprüfung wird dadurch nicht behauptet. [Rechtsstand und Grenzen](references/rechtsstand.md).

## 1.3. Skills

- [Anbieter und System in der EU-Datenbank registrieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/anbieter-system-registrieren/SKILL.md)
- [Ausnahmebewertung und Registrierung miteinander abstimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/ausnahme-system-registrieren/SKILL.md)
- [Öffentliche Betreiber und ihre Verwendung registrieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/oeffentliche-betreiber-registrieren/SKILL.md)
- [Registerweg und geschützte Angaben bestimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/sonderregister-und-vertraulichkeit/SKILL.md)
- [Schwerwiegende Vorfälle prüfen und melden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/schwerwiegende-vorfaelle-melden/SKILL.md)
- [Betreiberinformationen und Korrekturmaßnahmen koordinieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/betreiber-und-korrekturmeldungen/SKILL.md)
- [GPAI-Mitteilungen und Modellvorfälle bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/gpai-meldungen-bearbeiten/SKILL.md)
- [Grundrechte-Ergebnisse und Realtests übermitteln](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/fria-ergebnisse-und-realtests-melden/SKILL.md)
- [Besondere Behörden- und Stellenmeldungen prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/biometrie-und-stellenmeldungen/SKILL.md)
- [Meldungen mit Empfang und Änderungen nachhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/melderegister-und-nachverfolgung/SKILL.md)
- [Register und Meldungsfrage vollständig lösen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/register-und-meldung-loesen/SKILL.md)

## 1.4. Testakten

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

- [Fuldatal Sozialhilfe und Registerwechsel](../testakten/ki-register-fuldatal-sozialhilfe/README.md)
- [Mainbogen Notruf und gestaffelte Vorfallkenntnis](../testakten/ki-meldung-mainbogen-notruf/README.md)

<a id="9-pdf-lesefassungen-und-prüfbericht"></a>

## 1.5. PDF-Lesefassungen und Prüfbericht

[Skills-Handbuch](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/ki-verordnung-register-meldungen-skills-handbuch.pdf) · [Werkstatt-Lesefassung](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/ki-verordnung-register-meldungen-werkstatt-lesefassung.pdf) · [Prüfbericht](../quality/ki-verordnung-2026-10-09/README.md)

<a id="10-textfassungen"></a>

## 1.6. Textfassungen

[ki-verordnung-register-meldungen: werkstatt als TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-werkstatt.txt) · [ki-verordnung-register-meldungen: schnellstart als TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-schnellstart.txt) · [ki-verordnung-register-meldungen: hauptproblem als TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/ki-verordnung-register-meldungen-hauptproblem.txt)

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.

<a id="neue-vollständige-übungsakten"></a>

<a id="11-neue-vollständige-übungsakten"></a>

## 1.7. Neue vollständige Übungsakten

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte und Aufgabe | Originaldateien | Einzel-PDFs | Gesamt-PDF |
| --- | --- | --- | --- |
| [Havelgrund Sozialamt](../testakten/ki-register-havelgrund-sozialamt/README.md): Ausnahmebewertung, Register, Betreiberprüfung und Vorfallchronologie. | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-havelgrund-sozialamt.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/ki-verordnung-v445.35.2/testakte-ki-register-havelgrund-sozialamt-einzelpdfs.zip) | [PDF](../testakten/ki-register-havelgrund-sozialamt/gesamt-pdf/ki-register-havelgrund-sozialamt_gesamt.pdf) |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anbieter-system-registrieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/anbieter-system-registrieren/SKILL.md) | Anbieter und System in der EU-Datenbank registrieren. Prüft Artikel 49 Absatz 1 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/anbieter-system-registrieren/SKILL.md) |
| [`ausnahme-system-registrieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/ausnahme-system-registrieren/SKILL.md) | Ausnahmebewertung und Registrierung miteinander abstimmen. Prüft Artikel 6 Absätze 3 und 4 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/ausnahme-system-registrieren/SKILL.md) |
| [`betreiber-und-korrekturmeldungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/betreiber-und-korrekturmeldungen/SKILL.md) | Betreiberinformationen und Korrekturmaßnahmen koordinieren. Prüft Artikel 20 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/betreiber-und-korrekturmeldungen/SKILL.md) |
| [`biometrie-und-stellenmeldungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/biometrie-und-stellenmeldungen/SKILL.md) | Besondere Behörden- und Stellenmeldungen prüfen. Prüft Artikel 5 Absätze 3 und 4 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/biometrie-und-stellenmeldungen/SKILL.md) |
| [`fria-ergebnisse-und-realtests-melden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/fria-ergebnisse-und-realtests-melden/SKILL.md) | Grundrechte-Ergebnisse und Realtests übermitteln. Prüft Artikel 27 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/fria-ergebnisse-und-realtests-melden/SKILL.md) |
| [`gpai-meldungen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/gpai-meldungen-bearbeiten/SKILL.md) | GPAI-Mitteilungen und Modellvorfälle bearbeiten. Prüft Artikel 51 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/gpai-meldungen-bearbeiten/SKILL.md) |
| [`melderegister-und-nachverfolgung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/melderegister-und-nachverfolgung/SKILL.md) | Meldungen mit Empfang und Änderungen nachhalten. Prüft Artikel 49 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/melderegister-und-nachverfolgung/SKILL.md) |
| [`oeffentliche-betreiber-registrieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/oeffentliche-betreiber-registrieren/SKILL.md) | Öffentliche Betreiber und ihre Verwendung registrieren. Prüft Artikel 49 Absatz 3 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/oeffentliche-betreiber-registrieren/SKILL.md) |
| [`register-und-meldung-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/register-und-meldung-loesen/SKILL.md) | Prüft Register- und Meldepflichten der KI-Verordnung nach Rolle, System, Anlass und Zeitrecht. Erstellt Datensätze, Erstberichte, Ergänzungen und Anschreiben und hält Freigabe sowie tatsächlichen Eingang nach. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/register-und-meldung-loesen/SKILL.md) |
| [`schwerwiegende-vorfaelle-melden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/schwerwiegende-vorfaelle-melden/SKILL.md) | Schwerwiegende Vorfälle prüfen und melden. Prüft Artikel 3 Nummer 49 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/schwerwiegende-vorfaelle-melden/SKILL.md) |
| [`sonderregister-und-vertraulichkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/sonderregister-und-vertraulichkeit/SKILL.md) | Registerweg und geschützte Angaben bestimmen. Prüft Artikel 49 Absätze 4 und 5 anhand konkreter Belege und erstellt einen begründeten Entwurf mit offenen Nachweisen und nächsten Schritten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=ki-verordnung-register-meldungen/skills/sonderregister-und-vertraulichkeit/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
