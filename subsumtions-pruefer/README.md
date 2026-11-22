# Subsumtions-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/subsumtions-pruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/subsumtions-pruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/subsumtions-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/subsumtions-pruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Subsumtions-Prüfer:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/subsumtions-pruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`subsumtions-pruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`subsumtions-pruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Revision nach abgelehntem Beweisantrag Duisburg](../testakten/strafrecht-revision-beweisantrag-lg-duisburg/README.md) | [Gesamt-PDF](../testakten/strafrecht-revision-beweisantrag-lg-duisburg/gesamt-pdf/strafrecht-revision-beweisantrag-lg-duisburg_gesamt.pdf) | [`testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip) | [`testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip) |
| [Subsumtionskontrolle / Klausurkorrektur — Übung für Fortgeschrittene BGB, Uni Bielefeld, Lehrstuhl Pohlmann-Wittfeldt, SS 2026](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/README.md) | [Gesamt-PDF](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/gesamt-pdf/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann_gesamt.pdf) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Interaktiver Mechanik-Workflow für die juristische Subsumtion nach deutschem Recht und Europarecht. Das Plugin zerlegt Normen in Tatbestandsmerkmale, führt das Vier-Schritt-Schema (Obersatz – Definition – Untersatz – Ergebnis) durch, erfasst Beweisbedarf und erzeugt Ausgabedokumente in verschiedenen Formaten.

Das Plugin unterstützt die rechtliche Prüfung, ersetzt aber keine verantwortliche Einzelfallberatung. Es prüft die vorgegebene Norm und kann bei einer offenen Rechtsfrage passende Prüfungsansätze vorschlagen. Normwahl, Auslegung und Tatsachengrundlage müssen begründet und überprüft werden; Nutzerbehauptungen sind nicht automatisch bewiesene Tatsachen.

## Für wen ist dieses Plugin

| Rolle | Primäre Anwendungsfälle |
|---|---|
| Privatpersonen | Verstehen, ob ein Anspruch dem Grunde nach bestehen könnte |
| Paralegal / Rechtsfachwirt | Strukturierte Erstsichtung vor anwaltlicher Prüfung |
| Jurastudent / Referendar | Subsumtionsübung ohne Musterlösung |
| Unternehmensjurist | Schnelle Erstprüfung einer Norm vor Mandatserteilung |
| Behördenmitarbeiter | Strukturiertes Durchprüfen von Tatbestandsvoraussetzungen |

## Abgedeckte Rechtsgebiete

- **Deutsches Recht:** BGB (Schuld-, Sachen-, Familien-, Erbrecht), HGB, StGB, StPO, ZPO, VwGO, VwVfG, GG, AO, SGB, KSchG, AGG, GWB, UWG und Nebengesetze
- **BGB AT:** Für Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, Anfechtung, Stellvertretung, Fristen und Verjährung sollte `bgb-at-pruefer` vor oder neben diesem generischen Subsumtions-Plugin geladen werden.
- **Europarecht:** AEUV, EUV, GRCh (Primärrecht); DSGVO, KI-VO, Produkthaftungsrichtlinie, Verbraucherrechterichtlinie, Vergaberichtlinien u. a. (Sekundärrecht); EuGH-Judikatur

## Workflow-Überblick

```
Einstieg
│
├─ triage-rechtsfrage-oder-norm
│   Sachverhalt / Rechtsfrage / Norm erfassen
│
├─ ziel-und-rechtsweg-bestimmung
│   Was will der Nutzer? Welches Gericht?
│
├─ falsche-wiese-warnung
│   Fehlverortungen erkennen
│
├─ de-eu-recht-abgrenzung
│   Welches Recht gilt?
│
Normbestimmung
│
├─ einschlaegige-normen-vorschlagen-de / -eu
├─ norm-historie-und-aenderungen
├─ rechtsprechung-recherche-strategie
│
Subsumtion
│
├─ norm-zerlegen-mandantenbrief
├─ ungeschriebene-merkmale-judikatur
├─ generalklauseln-pruefen
├─ unbestimmte-rechtsbegriffe-pruefen
├─ subsumtion-obersatz-rewrite-klausurton-triage
├─ beweisbedarf-und-belege-erfassen
├─ darlegungs-und-beweislast-verteilen
├─ zerlegen-risikoampel-und-gegenargumente
│
Rechtsfolgen
│
├─ rechtsfolge-bestimmen-einreden-interaktiver
├─ konkurrenzen-anspruchsgrundlagen
├─ verjaehrung-fristen-pruefen
├─ verfahrensart-bestimmen-verjaehrung
├─ eu-vorabentscheidung-falsche-wiese
├─ grundrechte-pruefung-de-und-grch
│
Ausgabe (wählbar)
│
├─ output-juristisch-gestochen-de
├─ output-alltagssprache-de
├─ output-fremdsprachig-en-fr
├─ output-antrag-beschwerde-klageschrift
├─ output-memo-und-mandantenbrief
└─ output-pruefungsdokument-mit-warnhinweisen
```

## Wichtige Warnhinweise

Das System warnt aktiv in folgenden Situationen:

- **Falsche Norm:** Sachverhalt passt nicht zur gewählten Norm (`falsche-wiese-warnung`)
- **Komplexitätsgrenze:** Sachverhalt zu komplex für mechanische Prüfung (`mandatsabbruch-empfehlung-an-fachanwalt`)
- **Generalklauseln:** Kein mechanisch abschließbares Ergebnis möglich (`generalklauseln-pruefen`)
- **Unbestimmte Rechtsbegriffe:** Begriff auslegen, belegte Umstände zuordnen und Gegenargumente abwägen; verbleibende Wertungsunsicherheit offen ausweisen (`unbestimmte-rechtsbegriffe-pruefen`).
- **Offene TBM:** Fehlende Belege gefährden das Ergebnis (`beweisbedarf-und-belege-erfassen`)

## Aufgaben bei der Subsumtion

Die Tabellen zeigen fachliche Aufgaben. Die [Fachbibliothek](FACHMODULE.md) ordnet die Vertiefungen den [auswählbaren Skills](../skills-index/subsumtions-pruefer.md) zu.

### A. Triage / Workflow-Einstieg

| Thema | Funktion |
|---|---|
| `triage-rechtsfrage-oder-norm` | Interaktive Erfassung der Nutzereingabe |
| `ziel-und-rechtsweg-bestimmung` | Ziel und Rechtsweg ermitteln |
| `falsche-wiese-warnung` | Typische Fehlverortungen erkennen |
| `de-eu-recht-abgrenzung` | Nationales vs. Unionsrecht abgrenzen |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Komplexitätsgrenze erkennen, Fachanwalt empfehlen |

### B. Normbestimmung und Recherche

| Thema | Funktion |
|---|---|
| `einschlaegige-normen-vorschlagen-de` | Deutsche Normen anhand Sachverhalt vorschlagen |
| `einschlaegige-normen-vorschlagen-eu` | EU-Normen anhand Sachverhalt vorschlagen |
| `rechtsprechung-recherche-strategie` | Recherche-Strategie und Fundstellen |
| `norm-historie-und-aenderungen` | Geltende Fassung und Übergangsrecht |
| `kommentar-und-literatur-hinweis` | Standardkommentare und Literaturhinweise |

### C. Tatbestandsmerkmale und Subsumtion

| Thema | Funktion |
|---|---|
| `norm-zerlegen-mandantenbrief` | TBM-Liste mit Definitionen |
| `ungeschriebene-merkmale-judikatur` | Richterrechtlich entwickelte Merkmale |
| `generalklauseln-pruefen` | Generalklauseln — Indizien und Fallgruppen |
| `unbestimmte-rechtsbegriffe-pruefen` | Auslegungsmaßstäbe für unbestimmte Begriffe |
| `subsumtion-obersatz-rewrite-klausurton-triage` | Vier-Schritt-Schema je TBM |
| `beweisbedarf-und-belege-erfassen` | Beweismittel-Katalog und Tracking |
| `darlegungs-und-beweislast-verteilen` | Beweislast pro TBM |
| `zerlegen-risikoampel-und-gegenargumente` | Einwendungen und Einreden |

### D. Rechtsfolgen, Konkurrenzen, Verfahren

| Thema | Funktion |
|---|---|
| `rechtsfolge-bestimmen-einreden-interaktiver` | Anspruchsinhalt, Höhe, Nebenansprüche |
| `konkurrenzen-anspruchsgrundlagen` | Normkonkurrenzen und Spezialität |
| `verjaehrung-fristen-pruefen` | Verjährung, Hemmung, Neubeginn |
| `verfahrensart-bestimmen-verjaehrung` | Passende Verfahrensart und Zuständigkeit |
| `eu-vorabentscheidung-falsche-wiese` | Art. 267 AEUV — Voraussetzungen |
| `grundrechte-pruefung-de-und-grch` | GG und GRCh — Drei-Schritt-Schema |

### E. Output-Erzeugung

| Thema | Funktion |
|---|---|
| `output-juristisch-gestochen-de` | Schriftsatzstil, Rubrum, Tenor |
| `output-alltagssprache-de` | Verständliche Sprache für Betroffene |
| `output-fremdsprachig-en-fr` | Englisch und Französisch (nicht-amtlich) |
| `output-antrag-beschwerde-klageschrift` | Formale Dokument-Bausteine |
| `output-memo-und-mandantenbrief` | Aktennotiz und Mandantenbrief |
| `output-pruefungsdokument-mit-warnhinweisen` | Vollständiges Dokument mit allen Warnhinweisen |

## Lizenz

Apache-2.0 OR MIT — siehe LICENSE im Repository-Root.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **59 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Fallfrage | [`fallfrage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fallfrage-bearbeiten/SKILL.md) |
| 3. Aufbau | [`aufbau-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/aufbau-bearbeiten/SKILL.md) |
| 4. Subsumtion | [`subsumtion-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-bearbeiten/SKILL.md) |
| 5. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 6. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 7. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Arbeitsprodukt: Gutachten, Hausarbeit mit Fußnoten oder Lernübersicht in bewertungssicherer Form ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`aufbau-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/aufbau-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Aufbau: Anspruchsgrundlagen in sinnvoller Reihenfolge, Hilfsgutachten und Schwerpunktsetzung anlegen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/aufbau-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md) |
| [`fallfrage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fallfrage-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Fallfrage: Aufgabenstellung, Bearbeitervermerk, Rollenzuweisung und begehrte Rechtsfolge exakt erfassen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fallfrage-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md) | Juristische Begründung bis zur tragfähigen Schlusskette prüfen. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach neuen Angabe... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`subsumtion-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Subsumtion: Obersatz, Definition, Subsumtion, Ergebnis je Merkmal in ganzen Sätzen durchführen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Subsumtions-Prüfer: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Prüfen Sie jedes Merkmal anhand eines bezeichneten Aktenbelegs und führen Sie die stärkste Gegenposition aus. Rechtsprechung zu verwandten Normen ist als begrenztes Argument und nicht als Ersatz des konkreten Tatbestands einzusetzen.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
