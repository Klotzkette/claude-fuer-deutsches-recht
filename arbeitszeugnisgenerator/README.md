# Arbeitszeugnisgenerator

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Erstellt, prüft und berichtigt einfache, qualifizierte, Zwischen- und Ausbildungszeugnisse aus vorhandenen Unterlagen. Verknüpft Tätigkeitsbild, Tatsachenbelege, Beweislast, klare Formulierungen, Vergleich und Vollstreckung zu einem verwendbaren Arbeitsprodukt.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/arbeitszeugnisgenerator.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/arbeitszeugnisgenerator-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/arbeitszeugnisgenerator-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnisgenerator.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitszeugnisgenerator.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitszeugnisgenerator:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnisgenerator.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`arbeitszeugnisgenerator-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/arbeitszeugnisgenerator-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`arbeitszeugnisgenerator-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/arbeitszeugnisgenerator-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`arbeitszeugnisgenerator-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte.zip) | [`arbeitszeugnisgenerator-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnisgenerator-testakte-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein deutsches Arbeitszeugnis Schritt für Schritt erstellen — rechtssicher, mit korrekter Zeugnissprache, in der gewünschten Notenstufe.

## Wenn du das brauchst

- **Personalabteilung** muss für einen ausscheidenden Mitarbeiter ein qualifiziertes Arbeitszeugnis erstellen und braucht passende Formeln zur Wunschnote.
- **Geschäftsführer einer kleinen Firma** schreibt zum ersten Mal ein Arbeitszeugnis und will nicht versehentlich Geheimcodes einbauen, die die Note kippen.
- **Arbeitnehmer** möchte einen sauberen Vorschlag für das Wunschzeugnis erstellen und der HR-Abteilung vorlegen.
- **Auszubildender oder Ausbilder** braucht ein Ausbildungszeugnis nach Paragraf 16 BBiG.

## Was du am Ende in der Hand hast

Ein vollständiges einfaches, qualifiziertes, Zwischen- oder Ausbildungszeugnis mit belegten Kopfdaten, individuellem Tätigkeitsbild sowie einer wahrheitsgemäßen Leistungs- und Verhaltensbeurteilung. Alternativ erhältst du eine Berichtigungsmatrix, ein Aufforderungsschreiben, einen bestimmten Klageantrag oder eine vollstreckbare Vergleichsklausel. Beendigungsgrund und Schlussformel werden nur aufgenommen, wenn sie sachlich passen.

## Der Weg dorthin

Vorhandene Unterlagen lesen → Rolle und Zeugnisart bestimmen → Rollen- und Tätigkeitsverlauf belegen → Leistungs- und Verhaltensaussagen mit Tatsachen verbinden → Gesamtformel und Beweislast prüfen → Form, freiwillige Angaben und Aussteller kontrollieren → fertiges Arbeitsprodukt ausgeben.

## Workflows

Drei Modi zur Wahl:

- **Direkt-Modus**: Vorhandene Unterlagen werden ohne Vorfrage ausgewertet und sofort in einen Entwurf oder eine Änderungsmatrix überführt. Eine gewünschte Bewertung wird an den Belegen geprüft.
- **Geführter Modus**: Nur bei fehlendem Material werden Funktion, Aufgaben, Leistungsbelege, Verhalten und Sonderzweck in einer gebündelten Rückfrage erhoben.
- **Prozess-Modus**: Eine bereits erteilte Fassung wird Satz für Satz mit Tatsachengrundlage, Beweislast und konkretem Änderungsziel bearbeitet.

## Was dich aufhält

- **Wohlwollensgrundsatz versus Wahrheitspflicht**: Beides muss eingehalten werden, kein Schönschreiben um den Preis der Wahrheit.
- **Vermeintliche Geheimcodes**: Einzelne Wendungen werden nicht nach Internetlisten übersetzt. Maßgeblich sind objektiver Empfängerhorizont, Funktion und Gesamtzusammenhang, insbesondere BAG 9 AZR 386/10.
- **Zeugnisklarheit**: Das Zeugnis wird als einheitliches Ganzes geprüft; tabellarische Schulnoten genügen für ein qualifiziertes Zeugnis regelmäßig nicht, BAG 9 AZR 262/20.
- **Äußere Form**: Briefkopf, Datum, Unterschrift, kein Knick, keine Streichungen.
- **Schlussformel**: Dank, Bedauern und Zukunftswünsche sind grundsätzlich freiwillig und werden nicht mechanisch in eine Schulnote umgerechnet, BAG 9 AZR 146/21.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## Hinweise

Entscheidungszitate werden vor einer Verwendung im Schriftsatz am amtlichen Volltext geprüft. Offene Tatsachen und nicht verifizierte Fundstellen bleiben sichtbar; sie werden nicht durch plausible Ergänzungen ersetzt.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 6. Ergebnis, Schreiben und Kommunikation | [`zeugnis-pruefen-und-berichtigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnis-pruefen-und-berichtigen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`arbeitszeugnis-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/arbeitszeugnis-erstellen/SKILL.md), [`ausbildungs-und-praktikumszeugnis-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/ausbildungs-und-praktikumszeugnis-erstellen/SKILL.md), [`leistung-und-verhalten-formulieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/leistung-und-verhalten-formulieren/SKILL.md), [`zeugnisabschluss-und-form-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnisabschluss-und-form-gestalten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 5 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 5 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitszeugnis-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/arbeitszeugnis-erstellen/SKILL.md) | Erstellt einfache, qualifizierte und Zwischenzeugnisse aus Personalunterlagen. Erfasst tatsächliche Aufgaben, Rollenwechsel und Beurteilungszeiträume und liefert einen individuellen Entwurf mit getrennten Beleglücken. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/arbeitszeugnis-erstellen/SKILL.md) |
| [`ausbildungs-und-praktikumszeugnis-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/ausbildungs-und-praktikumszeugnis-erstellen/SKILL.md) | Erstellt Ausbildungszeugnisse und Praktikumsnachweise nach dem tatsächlichen Rechtsstatus. Trennt gesetzlichen Grundinhalt, gewünschte Bewertung und Prüfungszeugnis und formuliert belegte Lernfortschritte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/ausbildungs-und-praktikumszeugnis-erstellen/SKILL.md) |
| [`leistung-und-verhalten-formulieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/leistung-und-verhalten-formulieren/SKILL.md) | Formuliert belegte Leistungs-, Führungs- und Verhaltensbeurteilungen. Gewichtet Ergebnisse und Gegenbelege, wählt passende Gesamtformeln und erhält sachliche Unterschiede statt alle Sätze auf eine Wunschnote zu bringen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/leistung-und-verhalten-formulieren/SKILL.md) |
| [`zeugnis-pruefen-und-berichtigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnis-pruefen-und-berichtigen/SKILL.md) | Prüft und berichtigt vorhandene Zeugnisse anhand von Wortlaut, Akte und Rechtslage. Liefert gezielte Änderungen oder Anspruchsschreiben und trennt Bewertungsstreit, Maßregelung, Vergleich und Vollstreckung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnis-pruefen-und-berichtigen/SKILL.md) |
| [`zeugnisabschluss-und-form-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnisabschluss-und-form-gestalten/SKILL.md) | Gestaltet Beendigungssatz und freiwilligen Zeugnisabschluss und prüft Datum, Unterzeichnung sowie Papier- oder elektronische Form. Unterscheidet persönliche Wünsche, vertragliche Zusagen und bereits erteilte Fassungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnisgenerator/skills/zeugnisabschluss-und-form-gestalten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
