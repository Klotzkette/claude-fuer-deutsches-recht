# AGB-Werkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

AGB für Shop, Werkstatt, Handel, Banken und Darlehen entwerfen und prüfen. Zehn Fachskills und ein Hauptskill verbinden aktuelle Quellen, Interessenlage, vollstaendige Klauseln und konkrete Einfuehrung.

Dieses Plugin gehört zum Marketplace mit 308 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`agb-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/phishing-v445.35.4/agb-werkstatt.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/agb-werkstatt.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-schnellstart.md) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-hauptproblem.md" download>MD herunterladen / Download MD</a> |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/agb-werkstatt.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/agb-werkstatt.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für AGB-Werkstatt:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`agb-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/phishing-v445.35.4/agb-werkstatt.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`agb-werkstatt-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`agb-werkstatt-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-werkstatt.md) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-hauptproblem.md" download>agb-werkstatt-hauptproblem.md</a> |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 308 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kettenglück: AGB für die Fahrradwerkstatt](../testakten/agb-fahrradwerkstatt-kettenglueck-leipzig/README.md) | [Gesamt-PDF](../testakten/agb-fahrradwerkstatt-kettenglueck-leipzig/gesamt-pdf/agb-fahrradwerkstatt-kettenglueck-leipzig_gesamt.pdf) | [`testakte-agb-fahrradwerkstatt-kettenglueck-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-fahrradwerkstatt-kettenglueck-leipzig.zip) | [`testakte-agb-fahrradwerkstatt-kettenglueck-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-fahrradwerkstatt-kettenglueck-leipzig-einzelpdfs.zip) |
| [Pfotenproviant: AGB für Laden und Onlinehandel](../testakten/agb-tierbedarf-pfotenproviant-nuernberg/README.md) | [Gesamt-PDF](../testakten/agb-tierbedarf-pfotenproviant-nuernberg/gesamt-pdf/agb-tierbedarf-pfotenproviant-nuernberg_gesamt.pdf) | [`testakte-agb-tierbedarf-pfotenproviant-nuernberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-tierbedarf-pfotenproviant-nuernberg.zip) | [`testakte-agb-tierbedarf-pfotenproviant-nuernberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-tierbedarf-pfotenproviant-nuernberg-einzelpdfs.zip) |
| [Funkwerk: AGB für einen Webshop](../testakten/agb-webshop-funkwerk-berlin/README.md) | [Gesamt-PDF](../testakten/agb-webshop-funkwerk-berlin/gesamt-pdf/agb-webshop-funkwerk-berlin_gesamt.pdf) | [`testakte-agb-webshop-funkwerk-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-webshop-funkwerk-berlin.zip) | [`testakte-agb-webshop-funkwerk-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-webshop-funkwerk-berlin-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Version: 445.35.4

Allgemeine Geschäftsbedingungen für ein konkretes Geschäft entwerfen, prüfen und einführen: vom Webshop über den Reparaturbetrieb und gemischten Handel bis zu Bank- und Darlehensbedingungen. Zehn Fachskills und ein Hauptskill führen von vorhandenen Unterlagen über die nötigen Rückfragen zur vollständigen Fassung. Anbieterfreundlich, ausgewogen oder kundenfreundlich ist eine bewusste Gestaltungswahl, kein Freibrief für unwirksame Klauseln.

## 1 Einstieg

Geben Sie Geschäftsmodell, vorhandene Bedingungen und den gewünschten Einsatz vor, beispielsweise: „Hier sind Shopablauf und Preislisten. Erstellen Sie ausgewogene AGB samt Kundeninformationen.“ Der Hauptskill liest zuerst die Unterlagen, klärt nur entscheidende Lücken und arbeitet anschließend bis zu AGB, gesonderten Pflichtinformationen und konkreten Einführungs- oder Bestelltexten weiter.

Der bestehende AGB-Recht-Prüfer bleibt unverändert. Dieses kleinere Paket ist auf Gestaltung und Einführung ausgerichtet. Es braucht keinen dauerhaften Computerzugriff; Dateien, Recherche und Veröffentlichung stehen nur zur Verfügung, soweit die jeweilige Oberfläche diese Werkzeuge tatsächlich freigibt. Eine Veröffentlichung im Shop erfolgt nicht automatisch.

## 2 Downloads

| Unterlage | Zweck | Download |
| --- | --- | --- |
| Plugin | Elf einzeln aufrufbare Skills samt Quellenkarten | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/phishing-v445.35.4/agb-werkstatt.zip) |
| Portables Paket | Dasselbe Plugin mit äußerem Paketordner | [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/phishing-v445.35.4/agb-werkstatt-portable.zip) |
| Werkstatt | Ausführlicher eigenständiger Arbeitsablauf ohne Plugininstallation | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-werkstatt.md" download>Werkstatt als Markdown</a> |
| Schnellstart | Kompakter eigenständiger Auftrag unter 7500 Zeichen und Bytes | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-schnellstart.md" download>Mini-Prompt als Markdown</a> |
| Hauptproblem | Aus verstreuten Unterlagen verwendbare AGB erstellen | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/agb-werkstatt-hauptproblem.md" download>Hauptproblem-Prompt als Markdown</a> |

Werkstatt, Mini und Hauptproblem sind separate Alternativen. Sie werden nicht zusätzlich als versteckte Wrapper-Skills installiert. Im Plugin ist der Hauptproblemlöser ein echter Fachworkflow mit gezielten Übergaben.

## 3 Aufgaben und Grenzen

Die Bankprüfung unterscheidet Änderungszustimmung, Gebührenkontrolle und individuelle Rückforderungen. Die Kreditprüfung trennt Verbraucher- und Unternehmerdarlehen sowie Händler und Kreditgeber. Beim Shop sind Bestellbutton, Kündigungsbutton und elektronische Widerrufsfunktion drei verschiedene Prüfungen. Die Werkstattbedingungen regeln Diagnose, Freigabe zusätzlicher Arbeiten, Abnahme und Abholung.

Rechtsstand der Ausgangsrecherche: 9. Oktober 2026. Die Quellenkarten nennen tragende Aussagen und Grenzen sowie Unterschiede zwischen Volltext, Leitsatz und Pressemitteilung. Vor jeder konkreten Gestaltung ist die aktuelle Entwicklung zu prüfen. Das Paket verspricht weder vollständige Rechtsprechungskenntnis noch garantierte Rechtssicherheit; fachliche Endprüfung bleibt erforderlich.

## 4 Arbeitsakten

Die drei Mandate enthalten konkrete Geschäftsdaten, alte Entwürfe, E-Mails mit echten Dateianhängen, Rechnungen und laufende Beschwerden. Sie enthalten keine Musterlösung. Personen und Unternehmen sind erfunden; Kontakte nutzen reservierte Beispieldomains.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Fall | Gesamt-PDF | Einzel-PDFs | Originalformate |
| --- | --- | --- | --- |
| [Funkwerk: Webshop](../testakten/agb-webshop-funkwerk-berlin/README.md) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/agb-webshop-funkwerk-berlin_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-webshop-funkwerk-berlin-einzelpdfs.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-webshop-funkwerk-berlin.zip) |
| [Kettenglück: Fahrradreparatur](../testakten/agb-fahrradwerkstatt-kettenglueck-leipzig/README.md) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/agb-fahrradwerkstatt-kettenglueck-leipzig_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-fahrradwerkstatt-kettenglueck-leipzig-einzelpdfs.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-fahrradwerkstatt-kettenglueck-leipzig.zip) |
| [Pfotenproviant: Laden und Versand](../testakten/agb-tierbedarf-pfotenproviant-nuernberg/README.md) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/agb-tierbedarf-pfotenproviant-nuernberg_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-tierbedarf-pfotenproviant-nuernberg-einzelpdfs.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/agb-werkstatt-v1.0.0/testakte-agb-tierbedarf-pfotenproviant-nuernberg.zip) |

## 5 English Overview

This package drafts and reviews German standard terms for online shops, repair businesses, mixed retail, banking and credit. Ten specialist skills and one lead skill turn existing business records into complete terms, separate customer information and implementation texts. The workflow asks only for missing decisions and checks the applicable law and relevant case law before finalisation.

The workshop, compact prompt and lead-problem prompt are standalone Markdown alternatives. Practice files are separate downloads, not plugin contents. No automatic publication, legal-certainty guarantee or untested cross-client compatibility is claimed.

## 6 Navigation

[Repository](../README.md) · [Alle Skills](../SKILLS.md) · [Skill-Einzeldownloads](../skills-index/agb-werkstatt.md) · [Download-Index](../ASSET_INDEX.md) · [Alle Testakten](../testakten/README.md) · [Plugin-Dateien](.)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`agb-auftrag-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-auftrag-klaeren/SKILL.md) | Erfasst den konkreten AGB-Auftrag aus Shop, Laden oder Dienstleistung und trennt Verbraucher, Unternehmer und Vertriebswege. Nutzt vorhandene Unterlagen und fragt gezielt nach der gewünschten Interessenlage. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-auftrag-klaeren/SKILL.md) |
| [`agb-bank-zahlungsverkehr`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-bank-zahlungsverkehr/SKILL.md) | Prüft Bankentgelte, Änderungszustimmung und Zahlungsdienstbedingungen anhand aktueller Entscheidungen. Trennt Klauselgestaltung von Rückforderung und ordnet Kontoart, Buchungen und Zustimmung zeitlich zu. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-bank-zahlungsverkehr/SKILL.md) |
| [`agb-darlehen-finanzierung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-darlehen-finanzierung/SKILL.md) | Gestaltet Darlehens- und Finanzierungsbedingungen mit Prüfung von Bearbeitungsentgelten, Pflichtangaben, Zinsänderung und vorzeitiger Rückzahlung. Trennt Kreditgeber, Händler und Vermittler sowie B2B und Verbraucherkredit. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-darlehen-finanzierung/SKILL.md) |
| [`agb-endfassung-einfuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-endfassung-einfuehren/SKILL.md) | Führt AGB, Kundeninformationen und Bestelltexte zu einer konsistenten Endfassung zusammen. Prüft Einbeziehung, Versionierung und Bestandskundenänderung und bereitet die konkrete Umsetzung ohne eigenmächtige Veröffentlichung vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-endfassung-einfuehren/SKILL.md) |
| [`agb-haftung-maengel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-haftung-maengel/SKILL.md) | Prüft Haftungsausschlüsse, Gewährleistung und Verjährung nach Vertragsart und Kundenkreis. Erstellt verständliche Ersatzklauseln mit zwingenden Ausnahmen statt pauschaler Freizeichnungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-haftung-maengel/SKILL.md) |
| [`agb-handel-eigentumsvorbehalt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-handel-eigentumsvorbehalt/SKILL.md) | Erstellt abgestimmte Bedingungen für Laden, Versand und Wiederverkäufer. Prüft Lieferung, Eigentumsvorbehalt, Sicherungsumfang und Mängelanzeigen getrennt für Verbraucher und kaufmännische Kunden. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-handel-eigentumsvorbehalt/SKILL.md) |
| [`agb-hauptproblem-loesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-hauptproblem-loesen/SKILL.md) | Erstellt aus Geschäftsmodell, Altbedingungen, Preislisten und Beschwerden vollständige passende AGB samt Einführungstexten. Steuert zehn Fachskills gezielt, fragt entscheidende Lücken nach und prüft aktuelle Normen und Rechtsprechung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-hauptproblem-loesen/SKILL.md) |
| [`agb-preise-laufzeit-aenderung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-preise-laufzeit-aenderung/SKILL.md) | Gestaltet Preisänderung, Verlängerung und Kündigung für laufende Leistungen. Trennt neue Verträge von Bestandsverträgen und verhindert unbegrenzte Zustimmungsfiktionen oder versteckte Entgelte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-preise-laufzeit-aenderung/SKILL.md) |
| [`agb-rechtsprechung-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-rechtsprechung-abgleichen/SKILL.md) | Gleicht konkrete AGB-Klauseln mit geltendem Gesetz und neuer Rechtsprechung ab. Trennt tragende Aussagen von Pressemitteilungen und überprüft Vertragsart, Kundengruppe und zeitliche Anwendbarkeit vor dem Entwurf. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-rechtsprechung-abgleichen/SKILL.md) |
| [`agb-reparatur-werkstatt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-reparatur-werkstatt/SKILL.md) | Gestaltet AGB für Fahrradreparaturen und vergleichbare Werkleistungen: Diagnose, Kostenrahmen, Zusatzfreigabe, Abnahme, Abholung und Mängel. Unterscheidet Terminreservierung und verbindlichen Fernabsatzauftrag. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-reparatur-werkstatt/SKILL.md) |
| [`agb-webshop-checkout`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-webshop-checkout/SKILL.md) | Entwirft Verkaufsbedingungen für Webshops und stimmt Vertragsschluss, Widerruf, Lieferung und digitale Waren mit dem tatsächlichen Checkout ab. Liefert auch Bestelltexte statt allein abstrakter Klauseln. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=agb-werkstatt/skills/agb-webshop-checkout/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
