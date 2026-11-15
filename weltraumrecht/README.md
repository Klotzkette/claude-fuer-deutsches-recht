# Weltraumrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Großes Plugin für deutsches, europäisches und internationales Weltraumrecht: Raumfahrtverträge, Satelliten, Haftung, Weltraumbahnhof, Raketen, Raumstationen, Frequenzen, Exportkontrolle und Space Property.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`weltraumrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/weltraumrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/weltraumrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/weltraumrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/weltraumrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/weltraumrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/weltraumrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Weltraumrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`weltraumrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/weltraumrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`weltraumrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/weltraumrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`weltraumrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/weltraumrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Nordlicht-Orbit: Satellitenschwarm, Küstenstartplatz und Absturzrisiko](../testakten/weltraumrecht-satellitenschwarm-startplatz-kueste/README.md) | [Gesamt-PDF](../testakten/weltraumrecht-satellitenschwarm-startplatz-kueste/gesamt-pdf/weltraumrecht-satellitenschwarm-startplatz-kueste_gesamt.pdf) | [`testakte-weltraumrecht-satellitenschwarm-startplatz-kueste.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-weltraumrecht-satellitenschwarm-startplatz-kueste.zip) | [`testakte-weltraumrecht-satellitenschwarm-startplatz-kueste-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-2-v445.35.3/testakte-weltraumrecht-satellitenschwarm-startplatz-kueste-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **181 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/kaltstart-triage/SKILL.md) |
| 2. Mission und Rollen | [`mission-und-rollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/mission-und-rollen-bearbeiten/SKILL.md) |
| 3. Genehmigung und Aufsicht | [`genehmigung-und-aufsicht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/genehmigung-und-aufsicht-bearbeiten/SKILL.md) |
| 4. Registrierung und Kontrolle | [`registrierung-und-kontrolle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/registrierung-und-kontrolle-bearbeiten/SKILL.md) |
| 5. Haftung und Störung | [`haftung-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/haftung-und-stoerung-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Weltraumrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. Vollständige Fachanweisungen... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Für Weltraumrecht: Arbeitsprodukt: Missionsrechtsmatrix, Genehmigungsfahrplan, Registermeldung, Haftungsmemo, Startvertrag, Frequenzvermerk oder Behördenanfrage erstellen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt n... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`genehmigung-und-aufsicht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/genehmigung-und-aufsicht-bearbeiten/SKILL.md) | Für Weltraumrecht: Genehmigung und Aufsicht: nationale Zuständigkeit, private Tätigkeit, Sicherheitsprüfung, Erdfernerkundung, Frequenz und Exportkontrolle trennen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/genehmigung-und-aufsicht-bearbeiten/SKILL.md) |
| [`haftung-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/haftung-und-stoerung-bearbeiten/SKILL.md) | Für Weltraumrecht: Haftung und Störung: Schadensort, Startstaaten, Gefährdungs- oder Verschuldensmaßstab, Kausalität, Weltraummüll, Kollisionswarnung und Konsultation prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden geziel... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/haftung-und-stoerung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Weltraumrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/kaltstart-triage/SKILL.md) | Ordnet ein Raumfahrtvorhaben anhand von Mission, Betreiber, Start- und Registerstaat ein. Beginnt mit vorhandenen Unterlagen, klärt entscheidende Lücken und führt die Bearbeitung zum benötigten Antrag, Vertragsentwurf oder Haftungsvermer... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/kaltstart-triage/SKILL.md) |
| [`mission-und-rollen-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/mission-und-rollen-bearbeiten/SKILL.md) | Für Weltraumrecht: Mission und Rollen: Betreiber, Eigentümer, Hersteller, Startdienstleister, Startstaat, Registerstaat, Nutzlast, Orbit und Bodenstation erfassen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/mission-und-rollen-bearbeiten/SKILL.md) |
| [`registrierung-und-kontrolle-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/registrierung-und-kontrolle-bearbeiten/SKILL.md) | Für Weltraumrecht: Registrierung und Kontrolle: Weltraumgegenstand, Startdaten, Registereintrag, Hoheitsgewalt, Eigentumswechsel und Rückgabeanspruch dokumentieren. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/registrierung-und-kontrolle-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Weltraumrecht: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=weltraumrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Ermitteln Sie den tatsächlichen räumlichen und sachlichen Anwendungsbereich, bevor Sie aus dem technischen Gefahrenniveau eine KI-VO-Kategorie ableiten. Produktpfad, ziviler Einsatz und Systemfunktion brauchen eigene Belege.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
