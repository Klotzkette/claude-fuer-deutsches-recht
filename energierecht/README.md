# Energierecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`energierecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/energierecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/energierecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/energierecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/energierecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/energierecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/energierecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Energierecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`energierecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/energierecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`energierecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/energierecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`energierecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/energierecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin](../testakten/batteriespeicher-brandenburg-berlin-resilienz/README.md) | [Gesamt-PDF](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-batteriespeicher-brandenburg-berlin-resilienz-einzelpdfs.zip) |
| [Akte Energierecht: Stadtwerke Klotzkette AG – Quartier Hafenbogen](../testakten/energierecht-stadtwerke-quartier/README.md) | [Gesamt-PDF](../testakten/energierecht-stadtwerke-quartier/gesamt-pdf/energierecht-stadtwerke-quartier_gesamt.pdf) | [`testakte-energierecht-stadtwerke-quartier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-energierecht-stadtwerke-quartier.zip) | [`testakte-energierecht-stadtwerke-quartier-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-energierecht-stadtwerke-quartier-einzelpdfs.zip) |
| [Projekt Isarlicht — Kernfusion und Transrapid am Starnberger See](../testakten/kernfusion-transrapid-starnberger-see/README.md) | [Gesamt-PDF](../testakten/kernfusion-transrapid-starnberger-see/gesamt-pdf/kernfusion-transrapid-starnberger-see_gesamt.pdf) | [`testakte-kernfusion-transrapid-starnberger-see.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-kernfusion-transrapid-starnberger-see.zip) | [`testakte-kernfusion-transrapid-starnberger-see-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-kernfusion-transrapid-starnberger-see-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Vollständiger Energierechts-Assistent für Stadtwerke, Energieversorger, Wärmewirtschaft, energieintensive Unternehmen, Immobilienwirtschaft, Infrastrukturbetreiber, Contracting, Wasserstoff, E-Mobility, Transaktionen und Projektfinanzierung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `energierecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Fehlt ein Systemanschluss, mit vorhandenen Unterlagen oder manuellen Exporten weiterarbeiten und die verbleibende Zugriffslücke benennen. Testdaten werden nur für eine ausdrücklich gewünschte Übung erzeugt und getrennt vom realen Mandat als Simulation gekennzeichnet.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `energierecht-kommandocenter` - Energierecht-Kommandocenter
- `energierecht-infrastrukturprojekte` - Energieinfrastrukturprojekte
- `energierecht-netz-speicher-zugang` - Netz-, Speicher- und Anschlussregulierung
- `energierecht-energievertraege` - Energieverträge
- `energierecht-vertrieb-marktrollen` - Energievertrieb und Marktrollen
- `energierecht-industriekunden` - Industriekunden und Kostenoptimierung
- `energierecht-eeg-kwkg-erzeugung` - EEG, KWKG und Erzeugung
- `energierecht-waerme-quartier` - Wärme, Quartier und Fernwärme
- `energierecht-emobility-wasserstoff` - E-Mobility, Wasserstoff und Power-to-Gas
- `energierecht-wettbewerb` - Energie und Wettbewerb
- `energierecht-verfahren` - Verwaltungs- und Gerichtsverfahren Energie
- `energierecht-transaktionen-dd` - Energierechtliche Transaktions-Due-Diligence
- `energierecht-projektfinanzierung` - Erneuerbare-Energien-Projektfinanzierung

## Vorlagen

- `assets/templates/energie-mandatskarte.md` - Energierecht-Mandatskarte
- `assets/templates/energie-projektphasenplan.md` - Projektphasenplan Energieinfrastruktur
- `assets/templates/netzanschluss-zugangsmatrix.md` - Netzanschluss- und Zugangsmatrix
- `assets/templates/energieliefervertrag-check.md` - Energieliefervertrag-Check
- `assets/templates/waerme-quartier-playbook.md` - Wärme- und Quartiers-Playbook
- `assets/templates/industrie-umlagen-check.md` - Industrie-Umlagen- und Entlastungscheck
- `assets/templates/eeg-kwkg-foerdermatrix.md` - EEG/KWKG-Fördermatrix
- `assets/templates/vertrieb-marktrollen-map.md` - Vertrieb- und Marktrollenkarte
- `assets/templates/transaktions-dd-energielaw.md` - Energierechtliche DD-Matrix
- `assets/templates/verwaltungsverfahren-energie.md` - Energie-Verfahrensplan
- `assets/templates/wasserstoff-ptg-check.md` - Wasserstoff- und Power-to-Gas-Check
- `assets/templates/energie-wettbewerb-uwg-kartell.md` - Energie-Wettbewerbscheck

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **96 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Marktrolle und Anlage | [`marktrolle-und-anlage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/marktrolle-und-anlage-bearbeiten/SKILL.md) |
| 3. Regelungsstand | [`regelungsstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/regelungsstand-bearbeiten/SKILL.md) |
| 4. Technik und Daten | [`technik-und-daten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/technik-und-daten-bearbeiten/SKILL.md) |
| 5. Anspruch und Verfahren | [`anspruch-und-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/anspruch-und-verfahren-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anspruch-und-verfahren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/anspruch-und-verfahren-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Anspruch und Verfahren: Anschluss, Zugang, Entgelt, Vergütung, Abregelung, Beschwerde, Missbrauchsverfahren oder Genehmigung trennen. Vollständige Fachanweisungen und lokale Vorlagen we... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/anspruch-und-verfahren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklä... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Arbeitsprodukt: Anschlussdossier, Entgeltprüfung, Regulierungsantrag, Vertragsredline, Projekt-Risikomatrix oder Behördenstellungnahme erstellen. Vollständige Fachanweisungen und lokale... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Energierecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Energierecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`marktrolle-und-anlage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/marktrolle-und-anlage-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Marktrolle und Anlage: Betreiber, Lieferant, Anschlussnehmer, Bilanzkreis, Messstelle, Netzebene, Standort, Leistung und Inbetriebnahme feststellen. Vollständige Fachanweisungen und lok... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/marktrolle-und-anlage-bearbeiten/SKILL.md) |
| [`regelungsstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/regelungsstand-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Regelungsstand: maßgebliches Datum, EnWG- oder EEG-Fassung, Festlegung, Genehmigung, Netzbedingungen und Vertrag sichern. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/regelungsstand-bearbeiten/SKILL.md) |
| [`technik-und-daten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/technik-und-daten-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Technik und Daten: Anschlussbegehren, Kapazität, Lastgang, Einspeisung, Messung, Engpass, Netzstudie und Kosten belegen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/technik-und-daten-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Energie-, Netz-, Wärme- und Projektregulierung: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen u... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Energierecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=energierecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
