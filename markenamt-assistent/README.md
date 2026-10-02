<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="markenamt-assistent--dpma-und-euipo"></a>

# 1. Markenamt-Assistent – DPMA und EUIPO

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

DPMA und EUIPO: Marken recherchieren, anmelden, verteidigen, umschreiben und nachhalten. Zehn Fachskills und ein Hauptproblem-Skill mit konkreten Rechtsprechungsankern aus 2026, optionalem freigegebenem Portalvollzug und drei Testakten.

Dieses Plugin gehört zum Marketplace mit 272 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`markenamt-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/markenamt-assistent.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/markenamt-assistent.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Alle elf Skills sind unmittelbar enthalten: zehn Fachskills und der Hauptproblem-Skill. Werkstatt, Mini und Hauptproblem-Prompt sind getrennte eigenständige Downloads. Beim Einzel-Download eines Skills müssen die verlinkten Referenzen zusätzlich verfügbar sein.

All eleven skills are directly included: ten task workflows and one main problem workflow. Workshop, mini and focus prompts are separate standalone downloads. A downloaded individual skill also needs its linked references.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/markenamt-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/markenamt-assistent.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Markenamt-Assistent – DPMA und EUIPO:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`markenamt-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/markenamt-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`markenamt-assistent-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-schnellstart.md) · [`markenamt-assistent-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`markenamt-assistent-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-werkstatt.md) · [`markenamt-assistent-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-hauptproblem.md" download>markenamt-assistent-hauptproblem.md</a> · [`markenamt-assistent-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 272 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Farbwerk – Wem gehört das Aubergine im Baumarkt?](../testakten/markenamt-farbwerk/README.md) | [Gesamt-PDF](../testakten/markenamt-farbwerk/gesamt-pdf/markenamt-farbwerk_gesamt.pdf) | [`testakte-markenamt-farbwerk.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-farbwerk.zip) | [`testakte-markenamt-farbwerk-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-farbwerk-einzelpdfs.zip) |
| [Kichererbse – Streit um das neue Supermarktregal](../testakten/markenamt-kichererbse/README.md) | [Gesamt-PDF](../testakten/markenamt-kichererbse/gesamt-pdf/markenamt-kichererbse_gesamt.pdf) | [`testakte-markenamt-kichererbse.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-kichererbse.zip) | [`testakte-markenamt-kichererbse-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-kichererbse-einzelpdfs.zip) |
| [Rumpelrad – Das Fahrrad passt in den Hausflur](../testakten/markenamt-rumpelrad/README.md) | [Gesamt-PDF](../testakten/markenamt-rumpelrad/gesamt-pdf/markenamt-rumpelrad_gesamt.pdf) | [`testakte-markenamt-rumpelrad.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-rumpelrad.zip) | [`testakte-markenamt-rumpelrad-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.28.0/testakte-markenamt-rumpelrad-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Werkstatt zum Bearbeiten und Lesen: [Word](assets/markenamt-assistent-werkstatt.docx) · [PDF](assets/markenamt-assistent-werkstatt.pdf).

<!-- decimal-anchor --> <a id="direkt-beginnen"></a>

## 1.6. Direkt beginnen

Das Plugin führt von der Zeichenidee, dem Registertreffer oder dem Amtsbescheid bis zum fertigen Antrag und zur belegten Eingangskontrolle. Es enthält genau zehn Fachskills und einen elften Hauptproblem-Skill. Portalhandlungen sind optional; Einreichung, Zahlung und Rechtsaufgabe setzen tatsächliche Befugnis und konkrete Freigabe voraus.

[Große Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-werkstatt.md) · [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-schnellstart.md) · [Hauptproblem-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/markenamt-assistent-hauptproblem.md) · [Rechtsprechungsanker](references/rechtsprechungsanker.md)

Die Werkstatt bleibt eigenständig ausführbar. Zusätzliche Lesefassungen: [Word](assets/markenamt-assistent-werkstatt.docx) und [PDF](assets/markenamt-assistent-werkstatt.pdf).

<!-- decimal-anchor --> <a id="elf-skills"></a>

## 1.7. Elf Skills

1. [Auftrag, Vertretung und Fristen klären](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenauftrag-und-fristen-klaeren/SKILL.md)
2. [Register recherchieren und Treffer einordnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenrecherche-und-treffer-pruefen/SKILL.md)
3. [Waren und Dienstleistungen formulieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverzeichnis-und-klassen-formulieren/SKILL.md)
4. [Deutsche Marke anmelden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/dpma-marke-anmelden/SKILL.md)
5. [Unionsmarke anmelden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/euipo-unionsmarke-anmelden/SKILL.md)
6. [Beanstandungen des Amts beantworten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenbeanstandung-beantworten/SKILL.md)
7. [Widerspruch und Verteidigung führen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenwiderspruch-fuehren/SKILL.md)
8. [Verfall und Nichtigkeit betreiben](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverfall-und-nichtigkeit-pruefen/SKILL.md)
9. [Inhaber, Lizenz und Registerdaten ändern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markeninhaber-und-lizenzen-umschreiben/SKILL.md)
10. [Portal, Gebühren und Bestand nachhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenportal-und-bestand-nachhalten/SKILL.md)
11. [Marke sichern trotz offener Rechte](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/marke-sichern-trotz-offener-rechte/SKILL.md)

<!-- decimal-anchor --> <a id="recht-und-verfahrensgrenzen"></a>

## 1.8. Recht und Verfahrensgrenzen

Rechtsstand 01.10.2026. Fünf anhand amtlicher Volltexte geprüfte Entscheidungen aus 2026 betreffen Verkehrsdurchsetzung, Fortbestand älterer Rechte, Benutzungsnachweise, nationale Namensrechte und täuschende Traditionsangaben. Die konkrete Aussage und ihre Grenzen stehen unmittelbar an der jeweiligen Arbeitsstation. Gebühren und Portalwege sind vor tatsächlicher Nutzung erneut zu prüfen.

Das Plugin begründet keine Anwaltszulassung und enthält keinen installierten Behördenzugang. Zugang, Identifizierung und notwendige Vertretung bleiben gesondert zu klären. DPMAdirektWeb deckt nicht jeden nachgelagerten Verfahrensschritt ab. Eine Anmeldung ist noch keine Eintragung und kein Nachweis kollisionsfreier Benutzung.

<!-- decimal-anchor --> <a id="drei-testakten"></a>

## 1.9. Drei Testakten

[Rumpelrad – Anmeldung mit Inhaberwechsel](../testakten/markenamt-rumpelrad/README.md), [Kichererbse – EUIPO-Widerspruch und Benutzungsbelege](../testakten/markenamt-kichererbse/README.md) und [Farbwerk – Farbmarke mit widersprüchlichen Befragungen](../testakten/markenamt-farbwerk/README.md) enthalten native Unterlagen, E-Mails, Tabellen, Arbeitsansichten und widersprüchliche Informationen ohne Musterlösung.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.10. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und Recherche | [`marke-sichern-trotz-offener-rechte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/marke-sichern-trotz-offener-rechte/SKILL.md), [`markenauftrag-und-fristen-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenauftrag-und-fristen-klaeren/SKILL.md), [`markenrecherche-und-treffer-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenrecherche-und-treffer-pruefen/SKILL.md) |
| 2. Schutzumfang und Anmeldung | [`markenverzeichnis-und-klassen-formulieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverzeichnis-und-klassen-formulieren/SKILL.md), [`dpma-marke-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/dpma-marke-anmelden/SKILL.md), [`euipo-unionsmarke-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/euipo-unionsmarke-anmelden/SKILL.md) |
| 3. Beanstandung und Streit | [`markenbeanstandung-beantworten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenbeanstandung-beantworten/SKILL.md), [`markenwiderspruch-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenwiderspruch-fuehren/SKILL.md), [`markenverfall-und-nichtigkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverfall-und-nichtigkeit-pruefen/SKILL.md) |
| 4. Rechte und Bestand | [`markeninhaber-und-lizenzen-umschreiben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markeninhaber-und-lizenzen-umschreiben/SKILL.md), [`markenportal-und-bestand-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenportal-und-bestand-nachhalten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.11. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`dpma-marke-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/dpma-marke-anmelden/SKILL.md) | Eine Markenanmeldung beim DPMA mit Inhaber, Darstellung, Verzeichnis, Priorität, Gebühren und Eingangskontrolle vorbereiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/dpma-marke-anmelden/SKILL.md) |
| [`euipo-unionsmarke-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/euipo-unionsmarke-anmelden/SKILL.md) | Eine EUIPO-Anmeldung mit unionsweiter Schutzstrategie, Sprachen, Inhaber, Warenverzeichnis und Gebühren steuern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/euipo-unionsmarke-anmelden/SKILL.md) |
| [`marke-sichern-trotz-offener-rechte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/marke-sichern-trotz-offener-rechte/SKILL.md) | Einen DPMA- oder EUIPO-Fall bei Fristdruck und ungeklärter Inhaber- oder Beweislage priorisieren und bis zur fertigen Anmeldung oder Verteidigung führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/marke-sichern-trotz-offener-rechte/SKILL.md) |
| [`markenauftrag-und-fristen-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenauftrag-und-fristen-klaeren/SKILL.md) | Markenverfahren beim DPMA oder EUIPO aufnehmen und Zustellung, Vollmacht, Gebühren sowie den passenden Verfahrensweg prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenauftrag-und-fristen-klaeren/SKILL.md) |
| [`markenbeanstandung-beantworten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenbeanstandung-beantworten/SKILL.md) | Formelle und materielle DPMA- oder EUIPO-Beanstandungen anhand der konkreten Waren und Belege beantworten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenbeanstandung-beantworten/SKILL.md) |
| [`markeninhaber-und-lizenzen-umschreiben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markeninhaber-und-lizenzen-umschreiben/SKILL.md) | Übertragung, Namensänderung, Lizenz, Vertretung und Berichtigungen in DPMA- und EUIPO-Registern sauber nachhalten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markeninhaber-und-lizenzen-umschreiben/SKILL.md) |
| [`markenportal-und-bestand-nachhalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenportal-und-bestand-nachhalten/SKILL.md) | Agentische DPMA- oder EUIPO-Aktionen optional vorbereiten und nach Freigabe einschließlich Verlängerung und Eingangsbelegen kontrollieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenportal-und-bestand-nachhalten/SKILL.md) |
| [`markenrecherche-und-treffer-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenrecherche-und-treffer-pruefen/SKILL.md) | DPMAregister, EUIPO und TMview für Markenrecherche nutzen und ältere Rechte sowie Grenzen der Suche dokumentieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenrecherche-und-treffer-pruefen/SKILL.md) |
| [`markenverfall-und-nichtigkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverfall-und-nichtigkeit-pruefen/SKILL.md) | Amtsverfahren wegen Nichtbenutzung oder Nichtigkeit einschließlich Beweislast, Zeiträumen und älteren nationalen Rechten führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverfall-und-nichtigkeit-pruefen/SKILL.md) |
| [`markenverzeichnis-und-klassen-formulieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverzeichnis-und-klassen-formulieren/SKILL.md) | Das Waren- und Dienstleistungsverzeichnis für DPMA oder EUIPO aus dem Geschäftsmodell präzise und begrenzt entwickeln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenverzeichnis-und-klassen-formulieren/SKILL.md) |
| [`markenwiderspruch-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenwiderspruch-fuehren/SKILL.md) | Widersprüche beim DPMA oder EUIPO mit älteren Rechten, Fristen, Verwechslungsgefahr und Benutzungsnachweisen bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=markenamt-assistent/skills/markenwiderspruch-fuehren/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
