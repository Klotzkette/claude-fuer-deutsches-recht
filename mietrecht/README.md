# Mietrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Datenerhebung Mieterhöhungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`mietrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/mietrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/mietrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/mietrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/mietrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/mietrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/mietrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Mietrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: eine Anspruchs- und Fristenmatrix mit nächstem Schreiben. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`mietrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/mietrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`mietrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/mietrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`mietrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/mietrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [7 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Betriebskosten 2025: Eigenverwaltung eines Berliner Mietshauses](../testakten/betriebskosten-2025-mietshaus-schoeneberg/README.md) | [Gesamt-PDF](../testakten/betriebskosten-2025-mietshaus-schoeneberg/gesamt-pdf/betriebskosten-2025-mietshaus-schoeneberg_gesamt.pdf) | [`testakte-betriebskosten-2025-mietshaus-schoeneberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-betriebskosten-2025-mietshaus-schoeneberg.zip) | [`testakte-betriebskosten-2025-mietshaus-schoeneberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-betriebskosten-2025-mietshaus-schoeneberg-einzelpdfs.zip) |
| [Betriebskosten 2025: Vermietete Eigentumswohnung in Berlin-Schöneberg](../testakten/betriebskosten-2025-weg-schoeneberg/README.md) | [Gesamt-PDF](../testakten/betriebskosten-2025-weg-schoeneberg/gesamt-pdf/betriebskosten-2025-weg-schoeneberg_gesamt.pdf) | [`testakte-betriebskosten-2025-weg-schoeneberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-pflegerecht-v1.0.0/testakte-betriebskosten-2025-weg-schoeneberg.zip) | [`testakte-betriebskosten-2025-weg-schoeneberg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-betriebskosten-2025-weg-schoeneberg-einzelpdfs.zip) |
| [Eigenbedarf, Gesundheit und Ersatzwohnung in Regensburg](../testakten/eigenbedarf-haerte-ersatzwohnung-regensburg/README.md) | [Gesamt-PDF](../testakten/eigenbedarf-haerte-ersatzwohnung-regensburg/gesamt-pdf/eigenbedarf-haerte-ersatzwohnung-regensburg_gesamt.pdf) | [`testakte-eigenbedarf-haerte-ersatzwohnung-regensburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-eigenbedarf-haerte-ersatzwohnung-regensburg.zip) | [`testakte-eigenbedarf-haerte-ersatzwohnung-regensburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-eigenbedarf-haerte-ersatzwohnung-regensburg-einzelpdfs.zip) |
| [Eigenbedarf nach Umwandlung in Berlin](../testakten/eigenbedarf-umwandlung-berlin/README.md) | [Gesamt-PDF](../testakten/eigenbedarf-umwandlung-berlin/gesamt-pdf/eigenbedarf-umwandlung-berlin_gesamt.pdf) | [`testakte-eigenbedarf-umwandlung-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-eigenbedarf-umwandlung-berlin.zip) | [`testakte-eigenbedarf-umwandlung-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-eigenbedarf-umwandlung-berlin-einzelpdfs.zip) |
| [Wohnfläche und Ausstattung in Regensburg](../testakten/mietchecker-flaeche-kueche-regensburg/README.md) | [Gesamt-PDF](../testakten/mietchecker-flaeche-kueche-regensburg/gesamt-pdf/mietchecker-flaeche-kueche-regensburg_gesamt.pdf) | [`testakte-mietchecker-flaeche-kueche-regensburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mietchecker-flaeche-kueche-regensburg.zip) | [`testakte-mietchecker-flaeche-kueche-regensburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mietchecker-flaeche-kueche-regensburg-einzelpdfs.zip) |
| [Neuvermietung in Berlin](../testakten/mietchecker-neuvermietung-berlin/README.md) | [Gesamt-PDF](../testakten/mietchecker-neuvermietung-berlin/gesamt-pdf/mietchecker-neuvermietung-berlin_gesamt.pdf) | [`testakte-mietchecker-neuvermietung-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mietchecker-neuvermietung-berlin.zip) | [`testakte-mietchecker-neuvermietung-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mietchecker-neuvermietung-berlin-einzelpdfs.zip) |
| [Mietstreit Tannenkamp / Strassburger Immobilien GmbH — Altbau Leipzig-Plagwitz, Modernisierung und Mietminderung](../testakten/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp/README.md) | [Gesamt-PDF](../testakten/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp/gesamt-pdf/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp_gesamt.pdf) | [`testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip) | [`testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Prüfe Mietforderung, Mieterhöhung, Betriebskosten, Kündigung oder WEG-Streit aus den vorhandenen Unterlagen und erstelle das beauftragte Schreiben oder den Klageentwurf. Die Perspektive von Mieter, Vermieter, Eigentümer oder Verwaltung bestimmt den passenden Arbeitsweg.
Mietrecht für Mieter und Vermieter sowie Wohnungseigentumsrecht mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Workflows für Datenerhebung, Mieterhöhungs-Widerspruch, Mietsenkungsverlangen, Nebenkostenprüfung, Mieteranfragen, Kündigung, Kaution, WEG-Beschlussklage und Klageentwurf Amtsgericht.

## Rechtsstand und Quellen-Gate

Die `/mietrecht:rechtsschutz-und-einigung-bearbeiten Thema: rechtsstand-mai-2026-faktenbank` bietet datierte Ausgangsquellen zu Mietpreisbremse, Modernisierung, Steckersolargeräten, virtueller Eigentümerversammlung, Verwalterabberufung, WEG-baulichen Veränderungen und Störerhaftung. Ihr Name oder ein früherer Prüfvermerk bestätigt keine heutige Vollständigkeit. Prüfe nur die für den konkreten Auftrag tragenden Normfassungen, örtlichen Regelungen und Entscheidungen aktuell; der Quellenabruf ersetzt nicht die Arbeit am verlangten Dokument.

Keine BeckRS-, juris-, Kommentar- oder Aufsatzzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle; Mietspiegel nur aus amtlicher kommunaler Quelle oder der mitgelieferten Mietspiegel-Referenz.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Upload plugin` wählen und die Datei auswählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Fragt Rolle (Vermieter/Mieter/WEG/Verwalter), Ziel, Fristen, Unterlagen und Risiken ab und schlägt passende Spezial-Skills vor. Bei stummem Upload reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehörige Haushaltsangehörige) konkrete Begründ… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift in einer Mietsache. Wohnraummiete gehört nach Paragraf 23 Nummer 2a GVG streitwertunabhängig zum Amtsgericht; dort besteht in erster Instanz kein Anwaltszwang. Gewerberaummiete läuft über die Wertzuständigkeit nach Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG. |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnfläche Bad Küche Heizung Wohnungsausstattung Gebäudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot frist… |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klärt Mandantenrolle (Vermieter/Mieter/WEG-Eigentümer/Verwalter), Gegenstand (Wohnraum/Gewerbe/WEG) und Sachgebiet (Kündigung, Mieterhöhung, Mietminderung, Modernisierung, Nebenkosten, Mietkaution, Eigenbedarf, Räumung, WEG-Beschluss, WEG-Hausgeld). Fristen-Sofort-Check (§ 573c BGB, § 721 ZPO, § 45 WEG, § 558b BGB). Eskalations-Pfad bei laufenden Fristen. |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schönheitsreparaturen Hausordnung Kaution Eigenb… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhöhungsverlangen nach ortsüblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. P… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhöhungsverlangen auf ortsübliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen).… |
| `mietkaution-rueckforderung` | Mietersicht — Workflow zur Rückforderung der Mietkaution nach Beendigung des Mietverhältnisses. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum und Aktenzeichen. |
| `mietpreisueberhoehung-wistrg-1954-mietwucher` | Dreistufige Prüfung überhöhter Wohnraummiete: Mietpreisbremse, § 5 WiStrG 1954 als Ordnungswidrigkeit und § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rückforderungs- und Behördenpfad. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung) und § 291 StGB (Mietwucher). Erzeugt ein… |
| `mietspiegel-quellen` | Verweist auf die mitgelieferte Referenz references/mietspiegel-quellen.md mit ausschließlich amtlichen Mietspiegel-Quellen (Bundesländer Top-Städte Universitätsstädte). Nutze diese Referenz immer wenn die ortsüb… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwölf Monate) Umlagefähigkeit Verteilerschlüssel Heizk… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwölf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschlüssel rechnerische Richtig… |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate: Mietpreisbremse, Modernisierung, Steckersolargeräte, virtuelle Eigentümerversammlung, Verwalterabberufung, WEG-bauliche Veränderung und freie BGH-/Normquellen |
| `weg-beschluss-anfechten` | WEG-Sicht — Prüfraster für die Beschlussanfechtung in der Wohnungseigentümergemeinschaft nach §§ 44 ff. WEG (Reform 2020). Beschluss-, Anfechtungs-, Nichtigkeits- und Feststellungsklage. Prüft formelle Mängel (Ladung, Tagesordnung, Beschlussfähigkeit, Mehrheit, Stimmrechtsausschluss) und materielle Mängel (ordnungsmäßige Verwaltung, Treu und Glauben). Klagefrist ein Monat ab Beschluss (§ 45 WEG). |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **11 auswählbare Skills**. Die **64 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Mietvertrag und Gebrauchsrechte | [`mietvertrag-und-gebrauchsrechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mietvertrag-und-gebrauchsrechte-bearbeiten/SKILL.md) |
| 3. Miete und Betriebskosten | [`miete-und-betriebskosten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/miete-und-betriebskosten-bearbeiten/SKILL.md) |
| 4. Mangel und Instandhaltung | [`mangel-und-instandhaltung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mangel-und-instandhaltung-bearbeiten/SKILL.md) |
| 5. Kündigung und Rückgabe | [`kuendigung-und-rueckgabe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/kuendigung-und-rueckgabe-bearbeiten/SKILL.md) |
| 6. WEG und Beschlüsse | [`weg-und-beschluesse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/weg-und-beschluesse-bearbeiten/SKILL.md) |
| 7. Rechtsschutz und Einigung | [`rechtsschutz-und-einigung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/rechtsschutz-und-einigung-bearbeiten/SKILL.md) |
| 8. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 9. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. Vollständ... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Mietrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/einstieg-routing/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/juristischer-argumentationskern/SKILL.md) | Mietstreit von Vertrag und Verlauf zum fertigen Schreiben führen. Nutzt vorhandene Falldaten, entscheidet die maßgeblichen rechtlichen Abzweigungen und verbindet passende Fachprüfungen mit einem vollständig ausgearbeiteten Ergebnis einsc... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kuendigung-und-rueckgabe-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/kuendigung-und-rueckgabe-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Kündigung und Rückgabe: Kündigung, Eigenbedarf, Zahlungsrückstand, Räumung, Rückgabe und Kaution bis zum Schreiben oder Antrag führen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/kuendigung-und-rueckgabe-bearbeiten/SKILL.md) |
| [`mangel-und-instandhaltung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mangel-und-instandhaltung-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Mangel und Instandhaltung: Mangel, Minderung, Erhaltung, Modernisierung und Schadensersatz mit Zustand und Zugang abgleichen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mangel-und-instandhaltung-bearbeiten/SKILL.md) |
| [`miete-und-betriebskosten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/miete-und-betriebskosten-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Miete und Betriebskosten: Miethöhe, Erhöhung, Mietpreisbremse, Index, Staffel, Abrechnung und Umlageschlüssel rechnerisch prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/miete-und-betriebskosten-bearbeiten/SKILL.md) |
| [`mietvertrag-und-gebrauchsrechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mietvertrag-und-gebrauchsrechte-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Mietvertrag und Gebrauchsrechte: Vertrag, Parteien, Wohnraum oder Gewerbe, Überlassung und Nutzungsgrenzen konkret prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem kon... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/mietvertrag-und-gebrauchsrechte-bearbeiten/SKILL.md) |
| [`rechtsschutz-und-einigung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/rechtsschutz-und-einigung-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Rechtsschutz und Einigung: Anspruch, Beweis, Frist, Klage, Eilrechtsschutz und Vergleich bis zum nutzbaren Prozess- oder Einigungstext bearbeiten. Vollständige Fachanweisungen und lokale Vorlagen wer... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/rechtsschutz-und-einigung-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen und lokale Vorl... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`weg-und-beschluesse-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/weg-und-beschluesse-bearbeiten/SKILL.md) | Für Miet- und Wohnungseigentumsrecht: WEG und Beschlüsse: Gemeinschaft, Eigentümer, Versammlung, Stimmrecht, Beschlussfassung und Anfechtung auf die konkrete Maßnahme anwenden. Vollständige Fachanweisungen und lokale Vorlagen werden gezi... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/weg-und-beschluesse-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Mietrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=mietrecht/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
