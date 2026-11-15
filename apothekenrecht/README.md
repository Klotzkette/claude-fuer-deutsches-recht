# Apothekenrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`apothekenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/apothekenrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/apothekenrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/apothekenrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/apothekenrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/apothekenrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/apothekenrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Apothekenrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`apothekenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/apothekenrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`apothekenrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/apothekenrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`apothekenrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/apothekenrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Apothekenrecht: Retaxation und Kühlkette in Bremen](../testakten/apothekenrecht-retaxation-kuehlkette-bremen/README.md) | [Gesamt-PDF](../testakten/apothekenrecht-retaxation-kuehlkette-bremen/gesamt-pdf/apothekenrecht-retaxation-kuehlkette-bremen_gesamt.pdf) | [`testakte-apothekenrecht-retaxation-kuehlkette-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-apothekenrecht-retaxation-kuehlkette-bremen.zip) | [`testakte-apothekenrecht-retaxation-kuehlkette-bremen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-apothekenrecht-retaxation-kuehlkette-bremen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Super-Plugin für Apothekenrecht: Betriebserlaubnis, ApBetrO, Versand, E-Rezept, BtM, Retaxation, Aufsicht und Compliance.

## Wofür dieses Plugin da ist
Apothekenrecht zwischen ApoG, ApBetrO, AMG, AMPreisV, SGB V, HWG, BtMG, Datenschutz, Aufsicht, Versandhandel, E-Rezept und Apothekenpraxis.

Das Plugin bearbeitet Abgabe, Retaxation und Aufsichtsfragen aus den vorhandenen Rezepten, Abrechnungen und Betriebsunterlagen. Ein klarer Auftrag führt direkt zur Erwiderung, Betriebsanweisung oder Vertragsprüfung. Nur entscheidende Lücken lösen Rückfragen aus; nach der Antwort wird der begonnene Text fortgeführt.

## Typischer Workflow
1. Vorliegende Verordnung, Retaxation oder Behördenpost lesen und den beauftragten Vorgang bestimmen.
2. Rolle, maßgeblichen Abgabezeitpunkt, Frist und fehlenden Nachweis nur erfragen, soweit dies die nächste Entscheidung verändert. Unabhängige Teile weiterbearbeiten.
3. **Spezial-Skill wählen:** Das Plugin schlägt den passenden Skill vor und erklärt, welches Ergebnis damit entsteht.
4. **Live-Quellen prüfen:** Normtext, Behördenseite, EU-Text, Formular oder frei zugängliche Rechtsprechung aktualisieren.
5. **Output erzeugen:** Memo, Antrag, Stellungnahme, Vertragsklausel, Berechnung, Checkliste oder Mandantenbrief.
6. **Red-Team:** Fristen, Zuständigkeit, Zahlen, Quellen und Gegenargumente kontrollieren.

## Quellenanker
- Amtliche Gesetzestexte: gesetze-im-internet.de.
- EU-Recht: EUR-Lex und amtliche Kommissionsseiten.
- Behördenpraxis: zuständige Bundes-/Landesbehörden, Bundesnetzagentur, BaFin, BfArM, G-BA, BKartA oder Länderstellen je nach Thema.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.

## Skill-Schwerpunkte
| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Workflow | Kaltstart, Dokumentenintake, Fristen, Quellencheck, Output-Wahl, Red-Team |
| Materielle Prüfung | Tatbestände, Ausnahmen, Schwellen, Beweislast, Berechnungen, Rechtsfolgen |
| Verfahren und Kommunikation | Anträge, Anhörungen, Beschwerden, Schriftsätze, Behördenkontakt, Mandantenkommunikation |
| Spezialthemen | Branchen-, Vertrags-, Gebühren-, Aufsichts-, EU- und Edge-Case-Prüfungen |

## Quellen- und Halluzinationsschutz
Dieses Plugin soll keine nicht prüfbaren Fundstellen produzieren. Bei unsicherer oder dynamischer Rechtslage wird der Live-Quellencheck ausdrücklich vorgeschaltet.

## Lizenz
Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **66 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/kaltstart-triage/SKILL.md) |
| 2. Betrieb und Rolle | [`betrieb-und-rolle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betrieb-und-rolle-bearbeiten/SKILL.md) |
| 3. Produkt und Vorgang | [`produkt-und-vorgang-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/produkt-und-vorgang-bearbeiten/SKILL.md) |
| 4. Betriebsablauf und Nachweis | [`betriebsablauf-und-nachweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betriebsablauf-und-nachweis-bearbeiten/SKILL.md) |
| 5. Leistungs- und Aufsichtsweg | [`leistungs-und-aufsichtsweg-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/leistungs-und-aufsichtsweg-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Arbeitsprodukt: Erlaubnis- oder Anzeigeunterlage, SOP, Versorgungsvertrag, Retaxationswiderspruch, Aufsichtsantwort oder Maßnahmenplan erstellen. Vollständige Fachanweisungen und... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`betrieb-und-rolle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betrieb-und-rolle-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Betrieb und Rolle: Inhaber, Erlaubnis, Filiale, Leitung, Personal, Verantwortlichkeit und konkrete Betriebsstätte feststellen. Vollständige Fachanweisungen und lokale Vorlagen wer... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betrieb-und-rolle-bearbeiten/SKILL.md) |
| [`betriebsablauf-und-nachweis-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betriebsablauf-und-nachweis-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Betriebsablauf und Nachweis: Beschaffung, Prüfung, Lagerung, Herstellung, Beratung, Abgabe, Dokumentation und Rückruf nachvollziehen. Vollständige Fachanweisungen und lokale Vorla... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/betriebsablauf-und-nachweis-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Apothekenrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/kaltstart-triage/SKILL.md) | Für Apothekenrecht — Allgemein: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/kaltstart-triage/SKILL.md) |
| [`leistungs-und-aufsichtsweg-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/leistungs-und-aufsichtsweg-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Leistungs- und Aufsichtsweg: SGB-V-Abgabe, Retaxation, Erlaubnis, Anzeige, Beanstandung, Ordnungsverfügung oder Strafbezug trennen. Vollständige Fachanweisungen und lokale Vorlage... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/leistungs-und-aufsichtsweg-bearbeiten/SKILL.md) |
| [`produkt-und-vorgang-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/produkt-und-vorgang-bearbeiten/SKILL.md) | Für Apotheken-, Arzneimittelabgabe- und Versorgungsrecht: Produkt und Vorgang: Arzneimittel, Rezeptur, Defektur, Verschreibung, Abgabe, Substitution, Import, Versand oder Heimversorgung einordnen. Vollständige Fachanweisungen und lokale... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=apothekenrecht/skills/produkt-und-vorgang-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
