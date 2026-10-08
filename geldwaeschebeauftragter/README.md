# Geldwäschebeauftragter

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Geldwäschebeauftragte im Unternehmen, in Anwaltskanzlei und Notariat: zehn Fachabläufe und ein Hauptproblem-Skill für Organisation, KYC, Kontrolle, Immobilien, FIU, Vertraulichkeit, Aufsicht und Nachverfolgung.

Dieses Plugin gehört zum Marketplace mit 291 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`geldwaeschebeauftragter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/geldwaeschebeauftragter.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/geldwaeschebeauftragter.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/geldwaeschebeauftragter.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/geldwaeschebeauftragter.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Geldwäschebeauftragter:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: die Verpflichtetenrolle und den Zahlungsstand dieses Vorgangs klären, die konkrete Melde- beziehungsweise Vollzugsfrage begründen und das benötigte Anschreiben vollständig entwerfen. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`geldwaeschebeauftragter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/geldwaeschebeauftragter.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`geldwaeschebeauftragter-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-schnellstart.md) · [`geldwaeschebeauftragter-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`geldwaeschebeauftragter-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.md) · [`geldwaeschebeauftragter-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-hauptproblem.md" download>geldwaeschebeauftragter-hauptproblem.md</a> · [`geldwaeschebeauftragter-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/geldwaeschebeauftragter-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Die neue Komponente 445.34.0 wird über das oben verlinkte Einzel-ZIP ausgeliefert. Ältere Sammelarchive enthalten dieses Plugin noch nicht. Weitere Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md).

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Erfurt Eine Maschine und zwei Umschläge](../testakten/aml-unternehmen-werkzeughandel-erfurt/README.md) | [Gesamt-PDF](../testakten/aml-unternehmen-werkzeughandel-erfurt/gesamt-pdf/aml-unternehmen-werkzeughandel-erfurt_gesamt.pdf) | [`testakte-aml-unternehmen-werkzeughandel-erfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-unternehmen-werkzeughandel-erfurt.zip) | [`testakte-aml-unternehmen-werkzeughandel-erfurt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-unternehmen-werkzeughandel-erfurt-einzelpdfs.zip) |
| [Berlin Die Käuferin hinter der Hofgesellschaft](../testakten/aml-kanzlei-grundstueck-berlin/README.md) | [Gesamt-PDF](../testakten/aml-kanzlei-grundstueck-berlin/gesamt-pdf/aml-kanzlei-grundstueck-berlin_gesamt.pdf) | [`testakte-aml-kanzlei-grundstueck-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-kanzlei-grundstueck-berlin.zip) | [`testakte-aml-kanzlei-grundstueck-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-kanzlei-grundstueck-berlin-einzelpdfs.zip) |
| [Würzburg Die Quittung in der Keksdose](../testakten/aml-notariat-kaufpreis-wuerzburg/README.md) | [Gesamt-PDF](../testakten/aml-notariat-kaufpreis-wuerzburg/gesamt-pdf/aml-notariat-kaufpreis-wuerzburg_gesamt.pdf) | [`testakte-aml-notariat-kaufpreis-wuerzburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-notariat-kaufpreis-wuerzburg.zip) | [`testakte-aml-notariat-kaufpreis-wuerzburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/geldwaeschebeauftragter-v445.34.0/testakte-aml-notariat-kaufpreis-wuerzburg-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Version **445.34.0**. Zehn Fachskills und ein Hauptproblem-Skill unterstützen den Alltag der Geldwäschefunktion im Unternehmen, in der Anwaltskanzlei und im Notariat. Aus einer ungeordneten Akte werden Rollenvermerk, Beteiligtenbild, Zahlungsabgleich, begründete Entscheidung und vollständig formulierte Schreiben. Der Ablauf führt nach neuen Unterlagen an der offenen Stelle weiter.

## 1. Einstieg

Beginnen Sie mit: „Ich bearbeite diesen Vorgang als Geldwäschebeauftragte. Lesen Sie die Akte, bestimmen Sie meine Rolle und erstellen Sie den nächsten notwendigen Vermerk sowie das dazugehörige Schreiben. Heute soll folgende Handlung stattfinden: …“ Bei klarer Einzelaufgabe wählen Sie den passenden Fachskill direkt. Der Hauptproblem-Skill verbindet die Schritte und führt offene Fragen, Zuständigkeiten und Nachweise fort.

Das vorhandene Plugin [Geldwäscheprävention AML/KYC](../geldwaeschepraevention-aml-kyc/README.md) bleibt erhalten. Dieses neue Paket konzentriert sich auf den laufenden Arbeitsvorrat und die Entscheidungen der verantwortlichen Funktion. Es umfasst genau elf Skills und drei eigenständig verwendbare Prompts.

## 2. Was der Ablauf unterscheidet

| Situation | Arbeitsprodukt | Wesentliche Trennung |
| --- | --- | --- |
| Unternehmen nimmt ungewöhnliche Zahlungen an | Rollenvermerk, KYC und Zahlungsabgleich | Verpflichtetenstatus, Risikomanagement, Sorgfaltspflichten und Meldeanlass |
| Kanzlei begleitet einen Grundstückskauf | Kontrollstruktur, Informationsherkunft, Entscheidungsvermerk | Transaktionsmitwirkung, geschützte Beratung und konkrete Meldepflicht |
| Notariat soll den Kaufvertrag vollziehen | Zahlungsnachweise und Vollzugsvermerk | Beurkundung, Zahlungsmittelverbot, Meldetatbestand und Eigentumsumschreibung |
| Aufsicht fordert Unterlagen | Anlagenverzeichnis, Antwort und Maßnahmenplan | Tatsächlich vorhandener Nachweis, spätere Verbesserung und noch offene Aufgabe |

**Eine Rolle im Plugin begründet keine gesetzliche Bestellung oder Befugnis.** Nicht jedes Unternehmen und nicht jedes anwaltliche Mandat ist gleich verpflichtet. Zuständige Aufsicht, konkrete Tätigkeit und mögliche Anordnungen werden zuerst bestimmt. BaFin-Vorgaben werden nicht pauschal auf jede Kanzlei übertragen.

**Kein Geschäftsführer-Veto gegen die unabhängige Meldeentscheidung des Geldwäschebeauftragten.** Die gesetzliche Unabhängigkeit nach § 7 Absatz 5 GwG bleibt erhalten. Eine konkrete menschliche Anweisung vor einem technisch ausgeführten Versand kann vom zuständigen Geldwäschebeauftragten selbst kommen.

## 3. Computerzugriff und echte Meldungen

Das Paket enthält Arbeitsanweisungen und Quellen, keine eigene FIU-Schnittstelle und keine Portalzugangsdaten. Es kann in einer geeigneten Umgebung Unterlagen lesen, Tabellen und Entwürfe erstellen und bestehende Arbeitsschritte fortsetzen. Tatsächlicher Portalzugriff hängt von der verwendeten Anwendung, angeschlossenen Werkzeugen und Ihren eigenen Berechtigungen ab.

**FIU-Meldungen, Registermeldungen und externe E-Mails haben reale Folgen.** Vor ihrer Ausführung müssen Inhalt, Empfänger, Anlagen, Befugnis und konkrete Anweisung feststehen. Kundenschreiben werden von internen Meldevermerken getrennt. Das Informationsverbot nach § 47 GwG ist vor jeder Mitteilung zu prüfen. Kennwörter und Mehrfaktordaten gehören nicht in Prompts, Fallregister oder Aktenprotokolle. Ohne tatsächlichen Eingangsbeleg wird kein erfolgreicher Versand behauptet.

Ein vollständiger Entwurf kann sofort fertiggestellt werden, ohne dafür erst eine Versandfreigabe zu verlangen. Zeitkritische gesetzliche Pflichten dürfen durch unnötige interne Freigaberunden nicht verzögert werden.

## 4. Verwendung in Claude, Codex und ChatGPT

Das Plugin-ZIP enthält die elf Skills, gemeinsame Referenzen sowie Claude- und Codex-Manifeste. Importieren Sie es nur in einer Umgebung, die das jeweilige Pluginformat unterstützt. Die vorhandene Oberfläche und die automatische Auswahl einzelner Skills hängen vom Client ab.

In ChatGPT kann der Mini-Prompt als Arbeitsanweisung verwendet werden; für umfangreiche Vorgänge wählen Sie die Werkstatt und laden die benötigten Akten hinzu. Eine normale Chat-Unterhaltung bekommt dadurch keinen zusätzlichen Computer- oder Portalzugriff. Der Fallstand wird dort als kurzer Statusblock fortgeführt. Verwenden Sie einen passenden Prompt pro Auftrag; alle drei gleichzeitig sind nicht erforderlich.

| Fassung | Zweck | Datei |
| --- | --- | --- |
| Mini-Prompt | Schneller erster Arbeitsstand | [Markdown](geldwaeschebeauftragter-schnellstart.md) · [Text](geldwaeschebeauftragter-schnellstart.txt) |
| Werkstatt-Prompt | Ausführlicher Ablauf vom Tagesstart bis zur Aufsicht | [Markdown](geldwaeschebeauftragter-werkstatt.md) · [Text](geldwaeschebeauftragter-werkstatt.txt) |
| Hauptproblem-Prompt | Widersprüchliche Unterlagen vor einer Transaktion | [Markdown](geldwaeschebeauftragter-hauptproblem.md) · [Text](geldwaeschebeauftragter-hauptproblem.txt) |

## 5. Drei Übungsakten

Die Fälle haben jeweils E-Mails mit echten Datei-Anhängen, PDF-Belege, bearbeitbare Word-Dokumente und eine Excel-Arbeitsmappe. Unterschiedliche Erinnerungen und unvollständige Nachweise gehören zum Sachverhalt. Die Akten enthalten keine vorweggenommene Meldeentscheidung.

| Akte | Alltagssituation | Besonderheit |
| --- | --- | --- |
| [Erfurt: Eine Maschine und zwei Umschläge](../testakten/aml-unternehmen-werkzeughandel-erfurt/README.md) | Werkzeughändler, zwei Barteilzahlungen und bevorstehende Abholung | Zusammengehörige Zahlungen, Vertreterrolle, plausible Herkunftserklärung und Vertriebsdruck |
| [Berlin: Grundstückskauf in der Kanzlei](../testakten/aml-kanzlei-grundstueck-berlin/README.md) | Gesellschaft erwirbt ein Grundstück | Kontrollstruktur, PEP-Bezug, Registerabweichung und getrennte vertrauliche Beratung |
| [Würzburg: Kaufpreis im Notariat](../testakten/aml-notariat-kaufpreis-wuerzburg/README.md) | Eigentumsumschreibung wird verlangt | Bankabgänge, Drittzahlerin und widersprüchliche angebliche Barquittung |

## 6. Quellen und Prüfgrenzen

Rechtsstand der Erstellung: **08.10.2026**. Die Quellenreferenzen dokumentieren tatsächlich gelesene amtliche Normtexte und gerichtliche Randnummern: [Organisation, KYC und Sanktionen](references/organisation-quellen.md) sowie [Meldung, Immobilien und Notariat](references/meldung-notariat-quellen.md). Darunter sind die EuGH-Entscheidungen vom 12.03.2026, C-84/24, und vom 21.05.2026, C-483/23, zur Sanktionskontrolle. Ihre Reichweite wird ausdrücklich von der Ermittlung wirtschaftlich Berechtigter nach dem GwG getrennt.

Die 2026 anwendbare GwGMeldV über Form und Inhalt wird nicht mit der GwGMeldV-Immobilien verwechselt. Geltendes Recht und die grundsätzlich ab 10.07.2027 anwendbare AML-Verordnung bleiben getrennt. Aktuelle Listen, konkrete Aufsichtsanordnungen, Identitätsangaben und der Normstand sind bei realer Anwendung erneut zu prüfen. Eine technische Vollständigkeitsprüfung ist kein fachliches Gütesiegel für jeden Einzelfall.

Der [Prüfbericht](../quality/geldwaeschebeauftragter/README.md) nennt durchgeführte Kontrollen und Grenzen. Die Ausgabevorgaben verlangen vollständig ausformulierte Dokumente in Times New Roman, 11 pt, mit dezimaler Gliederung; Textausgaben nennen den Formatwunsch gesondert.

## 7. Komponentenrelease

[Veröffentlichung 445.34.0](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/geldwaeschebeauftragter-v445.34.0) enthält Plugin, separate Prompts, Lesefassungen und alle drei Akten. Die älteren allgemeinen Sammel-ZIPs enthalten dieses neue Paket noch nicht. Maßgeblich sind die Einzel-Downloads dieser Komponente.

## 8. Lesefassungen

[Handbuch aller elf Skills](../docs/handbuecher/geldwaeschebeauftragter-skills-handbuch.pdf) (45 Seiten) · [Werkstatt als PDF](../docs/handbuecher/geldwaeschebeauftragter-werkstatt-lesefassung.pdf) (11 Seiten). Die bearbeitbaren Prompts stehen oben als MD und TXT. Beide Lesefassungen wurden in Times New Roman gesetzt.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 2. Unterlagen, Sachverhalt und Quellen | [`dokumentation-kontrollen-schulung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/dokumentation-kontrollen-schulung/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`aufsichtspruefung-maengel-beheben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/aufsichtspruefung-maengel-beheben/SKILL.md), [`risikoanalyse-massnahmen-planen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/risikoanalyse-massnahmen-planen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`geldwaescheproblem-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/geldwaescheproblem-loesen/SKILL.md), [`identifizierung-kyc-durchfuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/identifizierung-kyc-durchfuehren/SKILL.md), [`immobilientransaktionen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/immobilientransaktionen-pruefen/SKILL.md), [`notarielle-vorgaenge-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/notarielle-vorgaenge-pruefen/SKILL.md), [`pep-sanktionen-risiken-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/pep-sanktionen-risiken-pruefen/SKILL.md), [`verdachtsfaelle-meldungen-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verdachtsfaelle-meldungen-steuern/SKILL.md), [`verpflichtung-organisation-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verpflichtung-organisation-klaeren/SKILL.md), [`wirtschaftlich-berechtigte-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/wirtschaftlich-berechtigte-klaeren/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`aufsichtspruefung-maengel-beheben`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/aufsichtspruefung-maengel-beheben/SKILL.md) | Bereitet Geldwäscheaufsichtsprüfungen vor, prüft Auskunftsverlangen und erstellt belegte Antworten sowie einen wirksamen Maßnahmenplan. Trennt Kooperation, Berufsgeheimnis, Selbstbelastungsfragen und laufende Meldepflichten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/aufsichtspruefung-maengel-beheben/SKILL.md) |
| [`dokumentation-kontrollen-schulung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/dokumentation-kontrollen-schulung/SKILL.md) | Erstellt prüffähige Geldwäschedokumentation, risikobezogene Kontrollen und konkrete Mitarbeiterschulungen. Verbindet Belegregister, Aufbewahrung, Schulungsnachweise und Mängelnachverfolgung, ohne Verdachtsinformationen unzulässig zu verb... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/dokumentation-kontrollen-schulung/SKILL.md) |
| [`geldwaescheproblem-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/geldwaescheproblem-loesen/SKILL.md) | Steuert den konkreten Geldwäschefall im Unternehmen, in der Anwaltskanzlei oder im Notariat von der Rollenklärung über Beteiligte und Zahlungen zur begründeten Entscheidung, zum fertigen Schreiben und zur Nachverfolgung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/geldwaescheproblem-loesen/SKILL.md) |
| [`identifizierung-kyc-durchfuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/identifizierung-kyc-durchfuehren/SKILL.md) | Führt die geldwäscherechtliche Kundenidentifizierung mit Personendaten, Identitätsnachweisen, Vertretungsmacht und Geschäftsbeziehungszweck zusammen. Erstellt KYC-Vermerk, gezielte Nachforderung und belastbaren Bearbeitungsstatus für Unt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/identifizierung-kyc-durchfuehren/SKILL.md) |
| [`immobilientransaktionen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/immobilientransaktionen-pruefen/SKILL.md) | Prüft Grundstückskäufe und Immobilienbeteiligungen auf Geldwäscherisiken, Zahlungswege und typisierte Meldetatbestände. Erstellt eine belegte Transaktionsprüfung mit offenen Nachweisen und übergibt Meldungs- oder notarielle Vollzugsfrage... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/immobilientransaktionen-pruefen/SKILL.md) |
| [`notarielle-vorgaenge-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/notarielle-vorgaenge-pruefen/SKILL.md) | Führt die Geldwäscheprüfung im Notariat vom vorbereiteten Erwerbsvorgang bis zum Vollzug. Trennt Beurkundungshindernisse, Zahlungsnachweise, Meldung und Grundbuchantrag und erstellt konkrete Vermerke, Nachforderungen und Übergaben. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/notarielle-vorgaenge-pruefen/SKILL.md) |
| [`pep-sanktionen-risiken-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/pep-sanktionen-risiken-pruefen/SKILL.md) | Prüft politisch exponierte Personen, Namens- und Sanktionstreffer sowie erhöhte Geldwäscherisiken. Trennt PEP-Status, Sanktionskontrolle und Verdachtsentscheidung und erstellt Treffervermerk, Herkunftsprüfung und eine konkrete Entscheidu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/pep-sanktionen-risiken-pruefen/SKILL.md) |
| [`risikoanalyse-massnahmen-planen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/risikoanalyse-massnahmen-planen/SKILL.md) | Erstellt und aktualisiert eine geschäftsspezifische Geldwäsche-Risikoanalyse mit Kontrollen, Verantwortlichen, Belegen und Maßnahmenplan. Trennt Unternehmensrisiken, einzelne Kundenrisiken und akute Verdachtsfälle und bereitet die Leitun... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/risikoanalyse-massnahmen-planen/SKILL.md) |
| [`verdachtsfaelle-meldungen-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verdachtsfaelle-meldungen-steuern/SKILL.md) | Bearbeitet konkrete Geldwäschehinweise bis zur begründeten Meldeentscheidung, erstellt FIU-Meldungsentwürfe und verfolgt Versand, Aufschub und Rückfragen. Trennt Berufsgeheimnis, Informationsverbot und unabhängige Entscheidung des Geldwä... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verdachtsfaelle-meldungen-steuern/SKILL.md) |
| [`verpflichtung-organisation-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verpflichtung-organisation-klaeren/SKILL.md) | Klärt die geldwäscherechtliche Verpflichtung und Aufsicht für Unternehmen, Kanzleien und Notariate. Erstellt eine begründete Tätigkeitszuordnung, eine Bestellungsprüfung und eine ausführbare Zuständigkeitsordnung mit Vertretung und unabh... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/verpflichtung-organisation-klaeren/SKILL.md) |
| [`wirtschaftlich-berechtigte-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/wirtschaftlich-berechtigte-klaeren/SKILL.md) | Ermittelt wirtschaftlich Berechtigte aus Beteiligungen, Stimmrechten, Kontrolle und Treuhand. Gleicht eigene Erhebungen mit dem Transparenzregister ab, begründet offene Kontrollfragen und bereitet eine getrennte Prüfung von Unstimmigkeit... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=geldwaeschebeauftragter/skills/wirtschaftlich-berechtigte-klaeren/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
