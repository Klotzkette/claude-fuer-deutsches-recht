# Strafbefehl-Verteidiger

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/strafbefehl-verteidiger.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/strafbefehl-verteidiger.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/strafbefehl-verteidiger-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/strafbefehl-verteidiger-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/strafbefehl-verteidiger.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/strafbefehl-verteidiger.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Strafbefehl-Verteidiger:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/strafbefehl-verteidiger.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`strafbefehl-verteidiger-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/strafbefehl-verteidiger-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`strafbefehl-verteidiger-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/strafbefehl-verteidiger-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren](../testakten/lumen-studios-insolvenz-strafverfahren/README.md) | [Gesamt-PDF](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-lumen-studios-insolvenz-strafverfahren.zip) | [`testakte-lumen-studios-insolvenz-strafverfahren-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-lumen-studios-insolvenz-strafverfahren-einzelpdfs.zip) |
| [Strafbefehl – Ladendiebstahl und Fahrerflucht](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/README.md) | [Gesamt-PDF](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/gesamt-pdf/strafbefehl-ladendiebstahl-fahrerflucht_gesamt.pdf) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafbefehl-ladendiebstahl-fahrerflucht-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Strafbefehl verteidigen: Einspruchsfrist, Beschränkung, Akteneinsicht, Tagessätze, Fahrverbot, Nebenfolgen, Beweisrisiko und Hauptverhandlungstaktik.
Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin benötigt keine anderen Plugins. Ohne Anschluss an Register oder Kanzleisoftware werden bereitgestellte Unterlagen ausgewertet und fehlende Aktenbestandteile gezielt angefordert. Ein ausdrücklich bestellter Übungsmodus verwendet erkennbar fiktive Daten; diese ersetzen niemals Belege im echten Mandat.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-quality-gate-akteneinsicht`, dem Einstieg in die Mandatssteuerung, starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nachfordern und fristbezogene Entwürfe auf belegter Grundlage weiterbearbeiten. Simulation nur für einen getrennten, ausdrücklich beauftragten Übungsfall verwenden.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-quality-gate-akteneinsicht` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-polizeifilmerei-201-kug` - Film-, Foto- und Tonaufnahmen von Polizeieinsätzen
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **61 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Tatvorwurf und materielles Recht | [`tatvorwurf-und-materielles-recht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) |
| 3. Beweis und Aktenanalyse | [`beweis-und-aktenanalyse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) |
| 4. Anklage und Hauptverhandlung | [`anklage-und-hauptverhandlung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) |
| 5. Entscheidung und Rechtsmittel | [`entscheidung-und-rechtsmittel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) |
| 6. Sanktion und Vollstreckung | [`sanktion-und-vollstreckung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anklage-und-hauptverhandlung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Anklage und Hauptverhandlung: Anklage, Zwischenverfahren, Einlassung, Beweisantrag, Verhandlung und Verständigung bis zum Schriftsatz vorbereiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/anklage-und-hauptverhandlung-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`beweis-und-aktenanalyse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Beweis und Aktenanalyse: Akteninhalt, Aussage, Sachverständige, digitale Daten und Beweisverwertung mit Widersprüchen und Grenzen auswerten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/beweis-und-aktenanalyse-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Strafbefehl-Verteidiger. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/einstieg-routing/SKILL.md) |
| [`entscheidung-und-rechtsmittel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Entscheidung und Rechtsmittel: Einstellung, Strafbefehl, Urteil, Strafzumessung, Berufung und Revision mit Form und Frist bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/entscheidung-und-rechtsmittel-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Strafbefehl Verteidiger ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/juristischer-argumentationskern/SKILL.md) |
| [`sanktion-und-vollstreckung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) | Für Strafrecht und Strafverfahren: Sanktion und Vollstreckung: Strafe, Bewährung, Maßregel, Einziehung, Vollzug und nachträgliche Entscheidungen getrennt prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem ko... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/sanktion-und-vollstreckung-bearbeiten/SKILL.md) |
| [`tatvorwurf-und-materielles-recht-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Tatvorwurf und materielles Recht: Tatbestand, Beteiligung, Irrtum, Rechtfertigung, Schuld und Konkurrenz am belegten Geschehen prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/tatvorwurf-und-materielles-recht-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Strafbefehl-Verteidiger: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Strafbefehl-Verteidiger. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=strafbefehl-verteidiger/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
