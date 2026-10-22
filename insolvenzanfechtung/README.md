# Insolvenzanfechtung

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Insolvenzanfechtung aus Verwalter- und Empfängersicht: Zahlungsketten, Deckung, Vorsatz, Drittleistungen, Gesellschafterfinanzierung, Bargeschäft und Rückgewähr belegt prüfen. Zehn Fachskills und ein Hauptskill führen zum ausformulierten Schreiben, Schriftsatz oder Vergleich.

Dieses Plugin gehört zum Marketplace mit 310 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`insolvenzanfechtung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/insolvenzanfechtung.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/insolvenzanfechtung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/insolvenzanfechtung.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Insolvenzanfechtung:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`insolvenzanfechtung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`insolvenzanfechtung-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) · [`insolvenzanfechtung-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`insolvenzanfechtung-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) · [`insolvenzanfechtung-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.md" download>insolvenzanfechtung-hauptproblem.md</a> · [`insolvenzanfechtung-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [5 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 310 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Weserfunken Darlehensverfahren Bremen](../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md) | [Gesamt-PDF](../testakten/fintech-darlehen-vertragsuebernahme-bremen/gesamt-pdf/fintech-darlehen-vertragsuebernahme-bremen_gesamt.pdf) | [`testakte-fintech-darlehen-vertragsuebernahme-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-fintech-darlehen-vertragsuebernahme-bremen.zip) | [`testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip) |
| [1. Blechliebe und die letzte Stahllieferung](../testakten/insolvenzanfechtung-blechliebe-bamberg/README.md) | [Gesamt-PDF](../testakten/insolvenzanfechtung-blechliebe-bamberg/gesamt-pdf/insolvenzanfechtung-blechliebe-bamberg_gesamt.pdf) | [`testakte-insolvenzanfechtung-blechliebe-bamberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-blechliebe-bamberg.zip) | [`testakte-insolvenzanfechtung-blechliebe-bamberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-blechliebe-bamberg-einzelpdfs.zip) |
| [1. Faltenwurf zwischen Familie und Werkstatt](../testakten/insolvenzanfechtung-faltenwurf-fuerth/README.md) | [Gesamt-PDF](../testakten/insolvenzanfechtung-faltenwurf-fuerth/gesamt-pdf/insolvenzanfechtung-faltenwurf-fuerth_gesamt.pdf) | [`testakte-insolvenzanfechtung-faltenwurf-fuerth.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-faltenwurf-fuerth.zip) | [`testakte-insolvenzanfechtung-faltenwurf-fuerth-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-faltenwurf-fuerth-einzelpdfs.zip) |
| [1. Testakte VeedelWende: klare Darlehensrückzahlung an den 25-Prozent-Gesellschafter](../testakten/insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln/README.md) | [Gesamt-PDF](../testakten/insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln/gesamt-pdf/insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln_gesamt.pdf) | [`testakte-insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln.zip) | [`testakte-insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln-einzelpdfs.zip) |
| [1. Testakte VeedelWende: alte Abtretung eines Gesellschafterdarlehens an einen Dritten](../testakten/insolvenzanfechtung-veedelwende-zession-koeln/README.md) | [Gesamt-PDF](../testakten/insolvenzanfechtung-veedelwende-zession-koeln/gesamt-pdf/insolvenzanfechtung-veedelwende-zession-koeln_gesamt.pdf) | [`testakte-insolvenzanfechtung-veedelwende-zession-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-veedelwende-zession-koeln.zip) | [`testakte-insolvenzanfechtung-veedelwende-zession-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/testakte-insolvenzanfechtung-veedelwende-zession-koeln-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

[Startseite](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/insolvenzanfechtung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Prüfen Sie Zahlungen, Sicherheiten und Vertragsgestaltungen aus Sicht der Insolvenzverwaltung oder des Anfechtungsgegners. Das Plugin führt von der Akte über die belegte Zahlungskette und die passenden Tatbestände zum ausformulierten Prüfvermerk, Forderungsschreiben, zur Klage, Klageerwiderung oder zum Vergleich. Es richtet sich an anwaltliche und insolvenzrechtliche Facharbeit.

Beginnen Sie mit den vorhandenen Unterlagen und einem konkreten Auftrag. Der Hauptskill übernimmt bekannte Angaben und fragt nur nach entscheidenden Lücken. Zehn Fachskills bearbeiten die jeweils benötigten Teilfragen; sie werden nicht als starre Pflichtliste abgerufen. Die eigenständigen Prompts funktionieren auch ohne Installation, wenn die gewählte Oberfläche die notwendigen Unterlagen lesen kann. Ein tatsächlicher Zugriff auf Dateien, Internetquellen oder Versanddienste wird nicht vorausgesetzt oder behauptet.

## 1. Einstieg und Downloads

Startsatz:

> Prüfen Sie die Rückforderung anhand der beigefügten Verträge, Kontoauszüge und Nachrichten aus Sicht des Empfängers. Ordnen Sie jede Zahlung, prüfen Sie Gegenleistung und Kenntnis und erstellen Sie eine ausformulierte Antwort. Fragen Sie nur nach den für das Ergebnis entscheidenden fehlenden Unterlagen.

Version: **1.1.0**. Rechtsquellenprüfung: **22.10.2026**. Änderungen stehen im [Changelog](CHANGELOG.md); die [Originalquellenreferenz](references/rechtsquellen.md) erläutert Aussage und Grenze jedes Entscheidungsankers.

| Bestandteil | Zweck | Zugang |
| --- | --- | --- |
| Plugin | Elf installierbare Skills und Referenzen | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung.zip) · [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Gesamtworkflow | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung-werkstatt.pdf) |
| Schnellstart | Kompakter eigenständiger Einstieg | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung-schnellstart.pdf) |
| Hauptproblem | Gläubigerwechsel, Empfängerzuordnung und Verteidigung | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/insolvenzanfechtung-hauptproblem.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzanfechtung-v1.1.0/insolvenzanfechtung-hauptproblem.pdf) |

Die Prompts sind eigenständige Arbeitsdateien. Das Plugin installiert keine Testakten und versendet keine E-Mails. Die verfügbaren Funktionen von Claude Cowork, Claude Code, Codex und ChatGPT hängen von der jeweiligen Umgebung ab; ein konkreter Skill lässt sich ausdrücklich als Auftrag wählen. Befehlsdateien sind zusätzliche Einstiegshilfen und müssen nicht in jeder Oberfläche als Menü erscheinen.

## 2. Elf Skills

| Skill | Arbeitsprodukt |
| --- | --- |
| [Zahlungsketten und Krisenbelege rekonstruieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) | Liefert eine belegte Vorgangsmatrix mit offenen Zuordnungen für die Insolvenzanfechtung |
| [Rechtshandlung, Zeitpunkt und Gläubigerbenachteiligung prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) | Trennt Antrag, Eröffnung und Wirksamkeit; liefert einen belegten Ausgangsvermerk und die passende Anfechtungsroute |
| [Kongruente und inkongruente Deckung unterscheiden](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) | Unterscheidet kongruente und inkongruente Deckung und erstellt eine vorgangsbezogene Anspruchs- oder Verteidigungsmatrix |
| [Benachteiligungsvorsatz und Empfängerkenntnis würdigen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) | Prüft Raten, Sanierung und Krisenwissen ohne automatischen Schluss aus Zahlungsunfähigkeit; liefert ein belastbares Vorsatzmemo |
| [Unentgeltlichkeit und Dreiecksverhältnisse auflösen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) | Rekonstruiert Leistungsbeziehungen, Forderungswert und Gegenleistung aus Empfängersicht; liefert eine begründete Dreiecksanalyse und konkrete Beweisfragen |
| [Gesellschafterdarlehen und Finanzierungshilfen prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) | Klärt Beteiligung, Einfluss, Regress und Ausnahmen; liefert eine Finanzierungschronologie mit Anspruchs- und Verteidigungsvarianten |
| [Sicherheiten, Verrechnung und Aufrechnung untersuchen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) | Trennt Entstehung, Werthaltigkeit, Erwerb und Verwertung; liefert einen Sicherheitenvermerk mit nachvollziehbarem Massevergleich |
| [Bargeschäft und unmittelbaren Leistungsaustausch prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) | Ordnet Lieferung, Vorkasse, Arbeitsentgelt und Verrechnung einzeln zu; liefert einen belastbaren Austauschvermerk |
| [Rückgewähr, Gegenleistung und Verjährung berechnen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) | Trennt Anspruchsentstehung, Kenntnis und Hemmung; liefert eine belegte Forderungsrechnung mit konkretem Handlungsbedarf |
| [Anfechtungsansprüche durchsetzen, abwehren und vergleichen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) | Ordnet Streitgegenstände, Bestreiten und Beweise zu; trennt Rechtsrisiko, Wirtschaftlichkeit und menschliche Freigabe |
| [Insolvenzanfechtung vom Akteneingang bis zum Endprodukt steuern](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) | Verbindet zehn Fachrouten, führt Vorgänge und Belege fort und liefert das bestellte Memo, Schreiben, den Schriftsatz oder Vergleich mit nachvollziehbaren Grenzen |

## 3. Rechtsprüfung mit belastbaren Grenzen

Die Prüfung trennt Rechtshandlung, zeitliche Zuordnung, objektive Benachteiligung, besondere Tatbestände und Rechtsfolgen. Eine Krise ist kein automatischer Vorsatzbeweis; eine Drittzahlung ist nicht automatisch unentgeltlich; ein Ratenplan beantwortet nicht alle Kenntnisfragen. Gegenleistung, werthaltige Sicherheiten und entlastende Kommunikation werden gleichrangig erfasst.

Die Referenz berücksichtigt amtlich gelesene Entscheidungen bis 2026. Insbesondere wird das EuGH-Verfahren C-43/25 nicht als noch offene Vorlage dargestellt. Entscheidungen enthalten jeweils „Trägt“ und „Trägt nicht“. Nicht zugängliche Quellen oder ungeklärte Tatsachen bleiben ausdrücklich offen. Das Plugin erfindet keine Randnummern und leitet aus einem Präzedenzfall keine allgemeine Bindung anderer Gerichte ab.

Für § 135 Abs. 1 Nr. 2 InsO unterscheidet der Workflow jetzt ausdrücklich den einfachen Rückzahlungsfall vom Forderungserwerb. Bei direkter Befriedigung innerhalb des Jahres werden Krise und Empfängerkenntnis nicht als zusätzliche Voraussetzungen behandelt; § 129 Abs. 1 InsO bleibt zu prüfen. Bei Abtretung werden Wirksamkeit und Jahresgrenze nach BGH IX ZR 32/12 sowie konkrete besondere Zurechnungstatsachen nach BGH IX ZR 173/23 offengelegt. Eine ältere echte Zession wird nicht aus dem ursprünglichen Gesellschafterbezug allein erfasst.

[Arbeitsweise](references/arbeitsweise.md) · [Zitierweise](references/zitierweise.md) · [Übergaben und Belegstruktur](references/belege-und-uebergaben.md)

## 4. Fünf Testakten

Die Fälle liegen getrennt im zentralen Testaktenordner. Die jeweiligen README-Seiten enthalten Gesamt-PDF, Einzel-PDFs und Originaldateien sowie die genaue Aufgabenbeschreibung. Sie können zunächst nur Aktenunterlagen bereitstellen und die Prüfhinweise für die spätere Auswertung zurückhalten.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Testakte | Schwerpunkt | Zugang |
| --- | --- | --- |
| Fintech-Darlehen und Vertragsübernahme, Bremen | Gläubigerwechsel, Zustimmung, Zahlungsweg und Empfängerzuordnung | [Akte und Downloads](../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md) |
| Blechliebe Bamberg | Ratenplan, alte Rückstände, Neulieferung, Bargeschäft und wechselndes Krisenwissen | [Akte und Downloads](../testakten/insolvenzanfechtung-blechliebe-bamberg/README.md) |
| Faltenwurf Fürth | Familie, Gesellschafterfinanzierung, Sicherung, Minderheitsbeteiligung und Bankgarantie | [Akte und Downloads](../testakten/insolvenzanfechtung-faltenwurf-fuerth/README.md) |
| VeedelWende: direkte Rückzahlung, Köln | Einfacher Anspruch aus der Rückzahlung eines Darlehens an einen Gesellschafter mit 25 Prozent Beteiligung vier Monate vor dem Antrag | [Akte und Downloads](../testakten/insolvenzanfechtung-veedelwende-direktrueckzahlung-koeln/README.md) |
| VeedelWende: Zession, Köln | Abtretung an einen außenstehenden Erwerber achtzehn Monate vor dem Antrag, bewusst riskante Klage und ausführliche Verteidigung | [Akte und Downloads](../testakten/insolvenzanfechtung-veedelwende-zession-koeln/README.md) |

[Übungswege und Auswertung](references/testakten-und-arbeitsauftraege.md) erläutern, welche Produkte aus den Unterlagen entstehen sollen. Die Akten sind fiktiv; ihre Tatsachen und eingebauten Vorprüfungen sind keine Rechtsquellen.

## 5. Freigaben und Fachanwaltsanschluss

Interne Sichtung, Quellenabgleich, Berechnung und Entwurf laufen innerhalb des Auftrags weiter. Versand, Einreichung, Anerkenntnis, Verzicht und Vergleichsannahme benötigen eine konkrete menschliche Freigabe für Person, Fassung und Handlung. Ein erzeugter Entwurf gilt nicht als versandt. Für Endprodukte gelten vollständige Ausformulierung, dezimale Gliederung und soweit technisch möglich Times New Roman, 11 pt.

Im [Fachanwaltsplugin Insolvenz- und Sanierungsrecht](../fachanwalt-insolvenz-sanierungsrecht/README.md) liegen zusätzlich [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachanwalt-insolvenz-sanierungsrecht/prompts/insolvenzanfechtung/insolvenzanfechtung-werkstatt.md) und [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=fachanwalt-insolvenz-sanierungsrecht/prompts/insolvenzanfechtung/insolvenzanfechtung-schnellstart.md) ausschließlich zur Insolvenzanfechtung. Der allgemeine fachanwaltliche Prompt bleibt daneben erhalten.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anfechtung-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) | Steuert die vollständige Insolvenzanfechtung aus Verwalter- oder Empfängersicht. Verbindet zehn Fachrouten, führt Vorgänge und Belege fort und liefert das bestellte Memo, Schreiben, den Schriftsatz oder Vergleich mit nachvollziehbaren Gr... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/anfechtung-steuern/SKILL.md) |
| [`bargeschaeft-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) | Prüft unmittelbare und gleichwertige Gegenleistung sowie Unlauterkeit bei der Bargeschäftsausnahme. Ordnet Lieferung, Vorkasse, Arbeitsentgelt und Verrechnung einzeln zu; liefert einen belastbaren Austauschvermerk. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/bargeschaeft-pruefen/SKILL.md) |
| [`deckung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) | Prüft die Deckungsanfechtung anhand von Anspruch, Fälligkeit, Leistungsart, Zeitraum und Empfängerwissen. Unterscheidet kongruente und inkongruente Deckung und erstellt eine vorgangsbezogene Anspruchs- oder Verteidigungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/deckung-pruefen/SKILL.md) |
| [`gesellschafterfinanzierung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) | Prüft Darlehen, darlehensgleiche Forderungen, Sicherheiten und Rückzahlungen mit Gesellschafterbezug. Klärt Beteiligung, Einfluss, Regress und Ausnahmen; liefert eine Finanzierungschronologie mit Anspruchs- und Verteidigungsvarianten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/gesellschafterfinanzierung/SKILL.md) |
| [`prozess-und-vergleich`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) | Erstellt aus belegten Anfechtungsvorgängen Forderungsschreiben, Klagen, Erwiderungen und Vergleichsentwürfe. Ordnet Streitgegenstände, Bestreiten und Beweise zu; trennt Rechtsrisiko, Wirtschaftlichkeit und menschliche Freigabe. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/prozess-und-vergleich/SKILL.md) |
| [`rechtsfolgen-verjaehrung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) | Berechnet Rückgewähr und Nebenforderungen, prüft Gegenleistung, Rechtsnachfolge und Verjährung. Trennt Anspruchsentstehung, Kenntnis und Hemmung; liefert eine belegte Forderungsrechnung mit konkretem Handlungsbedarf. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtsfolgen-verjaehrung/SKILL.md) |
| [`rechtshandlung-zeit-benachteiligung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) | Prüft die konkrete Rechtshandlung, ihre zeitliche Einordnung und die Gläubigerbenachteiligung. Trennt Antrag, Eröffnung und Wirksamkeit; liefert einen belegten Ausgangsvermerk und die passende Anfechtungsroute. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/rechtshandlung-zeit-benachteiligung/SKILL.md) |
| [`sicherheiten-aufrechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) | Analysiert Sicherungsrechte, Kontokorrent, Aufrechnungslagen und Verrechnungen. Trennt Entstehung, Werthaltigkeit, Erwerb und Verwertung; liefert einen Sicherheitenvermerk mit nachvollziehbarem Massevergleich. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/sicherheiten-aufrechnung/SKILL.md) |
| [`unentgeltlichkeit-dreieck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) | Prüft unentgeltliche Leistungen und Zahlungen auf fremde Schulden. Rekonstruiert Leistungsbeziehungen, Forderungswert und Gegenleistung aus Empfängersicht; liefert eine begründete Dreiecksanalyse und konkrete Beweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/unentgeltlichkeit-dreieck/SKILL.md) |
| [`vorsatz-und-kenntnis`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) | Würdigt Benachteiligungsvorsatz und Empfängerkenntnis anhand zeitbezogener Indizien und Gegenindizien. Prüft Raten, Sanierung und Krisenwissen ohne automatischen Schluss aus Zahlungsunfähigkeit; liefert ein belastbares Vorsatzmemo. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/vorsatz-und-kenntnis/SKILL.md) |
| [`zahlungskette-und-belege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) | Rekonstruiert Zahlungen, Vertragswechsel, Empfänger und Krisenwissen aus Bankdaten, Buchhaltung und Schriftverkehr. Liefert eine belegte Vorgangsmatrix mit offenen Zuordnungen für die Insolvenzanfechtung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzanfechtung/skills/zahlungskette-und-belege/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
