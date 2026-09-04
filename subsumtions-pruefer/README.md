# Subsumtions-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/subsumtions-pruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/subsumtions-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/subsumtions-pruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Subsumtions-Prüfer:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Gutachtensatz: Obersatz, Definition, Subsumtion mit Sachverhaltszitat, Zwischenergebnis. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`subsumtions-pruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`subsumtions-pruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/subsumtions-pruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Revision nach abgelehntem Beweisantrag Duisburg](../testakten/strafrecht-revision-beweisantrag-lg-duisburg/README.md) | [Gesamt-PDF](../testakten/strafrecht-revision-beweisantrag-lg-duisburg/gesamt-pdf/strafrecht-revision-beweisantrag-lg-duisburg_gesamt.pdf) | [`testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-revision-beweisantrag-lg-duisburg.zip) | [`testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-revision-beweisantrag-lg-duisburg-einzelpdfs.zip) |
| [Subsumtionskontrolle / Klausurkorrektur — Übung für Fortgeschrittene BGB, Uni Bielefeld, Lehrstuhl Pohlmann-Wittfeldt, SS 2026](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/README.md) | [Gesamt-PDF](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/gesamt-pdf/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann_gesamt.pdf) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Interaktiver Mechanik-Workflow für die juristische Subsumtion nach deutschem Recht und Europarecht. Das Plugin zerlegt Normen in Tatbestandsmerkmale, führt das Vier-Schritt-Schema (Obersatz – Definition – Untersatz – Ergebnis) durch, erfasst Beweisbedarf und erzeugt Ausgabedokumente in verschiedenen Formaten.

**Dieses Plugin ist keine Rechtsberatung.** Es prüft mechanisch eine vom Nutzer behauptete Norm anhand vom Nutzer behaupteter Tatsachen. Die Auswahl der richtigen Norm, die vollständige Sachverhaltsdarstellung und die Bewertung des Ergebnisses bleiben in der Verantwortung des Nutzers und eines zugelassenen Rechtsanwalts.

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
- **Unbestimmte Rechtsbegriffe:** Nur Indiziensammlung, keine Subsumtion (`unbestimmte-rechtsbegriffe-pruefen`)
- **Offene TBM:** Fehlende Belege gefährden das Ergebnis (`beweisbedarf-und-belege-erfassen`)

## Skills (31)

### A. Triage / Workflow-Einstieg

| Skill | Funktion |
|---|---|
| `triage-rechtsfrage-oder-norm` | Interaktive Erfassung der Nutzereingabe |
| `ziel-und-rechtsweg-bestimmung` | Ziel und Rechtsweg ermitteln |
| `falsche-wiese-warnung` | Typische Fehlverortungen erkennen |
| `de-eu-recht-abgrenzung` | Nationales vs. Unionsrecht abgrenzen |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Komplexitätsgrenze erkennen, Fachanwalt empfehlen |

### B. Normbestimmung und Recherche

| Skill | Funktion |
|---|---|
| `einschlaegige-normen-vorschlagen-de` | Deutsche Normen anhand Sachverhalt vorschlagen |
| `einschlaegige-normen-vorschlagen-eu` | EU-Normen anhand Sachverhalt vorschlagen |
| `rechtsprechung-recherche-strategie` | Recherche-Strategie und Fundstellen |
| `norm-historie-und-aenderungen` | Geltende Fassung und Übergangsrecht |
| `kommentar-und-literatur-hinweis` | Standardkommentare und Literaturhinweise |

### C. Tatbestandsmerkmale und Subsumtion

| Skill | Funktion |
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

| Skill | Funktion |
|---|---|
| `rechtsfolge-bestimmen-einreden-interaktiver` | Anspruchsinhalt, Höhe, Nebenansprüche |
| `konkurrenzen-anspruchsgrundlagen` | Normkonkurrenzen und Spezialität |
| `verjaehrung-fristen-pruefen` | Verjährung, Hemmung, Neubeginn |
| `verfahrensart-bestimmen-verjaehrung` | Passende Verfahrensart und Zuständigkeit |
| `eu-vorabentscheidung-falsche-wiese` | Art. 267 AEUV — Voraussetzungen |
| `grundrechte-pruefung-de-und-grch` | GG und GRCh — Drei-Schritt-Schema |

### E. Output-Erzeugung

| Skill | Funktion |
|---|---|
| `output-juristisch-gestochen-de` | Schriftsatzstil, Rubrum, Tenor |
| `output-alltagssprache-de` | Verständliche Sprache für Betroffene |
| `output-fremdsprachig-en-fr` | Englisch und Französisch (nicht-amtlich) |
| `output-antrag-beschwerde-klageschrift` | Formale Dokument-Bausteine |
| `output-memo-und-mandantenbrief` | Aktennotiz und Mandantenbrief |
| `output-pruefungsdokument-mit-warnhinweisen` | Vollständiges Dokument mit allen Warnhinweisen |

## Lizenz

Apache-2.0 OR MIT — siehe LICENSE im Repository-Root.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/dokumente-intake/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md), [`interaktiver-erstpruefung-und-mandatsziel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interaktiver-erstpruefung-und-mandatsziel/SKILL.md), [`mandatsabbruch-empfehlung-beweisbedarf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/mandatsabbruch-empfehlung-beweisbedarf/SKILL.md), [`start-chronologie-fristen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/start-chronologie-fristen/SKILL.md), [`subsumtion-obersatz-rewrite-klausurton-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-obersatz-rewrite-klausurton-triage/SKILL.md), [`triage-rechtsfrage-oder-norm`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/triage-rechtsfrage-oder-norm/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`anwenden-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/anwenden-quellenkarte/SKILL.md), [`beweisbedarf-und-belege-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/beweisbedarf-und-belege-erfassen/SKILL.md), [`darlegungs-und-beweislast-verteilen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/darlegungs-und-beweislast-verteilen/SKILL.md), [`einreden-compliance-dokumentation-und-akte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einreden-compliance-dokumentation-und-akte/SKILL.md), [`kandidatenloesung-subsumtion-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kandidatenloesung-subsumtion-pruefen/SKILL.md), [`output-pruefungsdokument-mit-warnhinweisen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-pruefungsdokument-mit-warnhinweisen/SKILL.md), [`rechtsprechung-recherche-strategie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsprechung-recherche-strategie/SKILL.md), [`spezial-anwenden-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-anwenden-livequellen-und-rechtsprechungscheck/SKILL.md), [`subsumtions-tatbestand-beweis-und-belege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-tatbestand-beweis-und-belege/SKILL.md), [`tbm-grundrechte-grch-kandidatenloesung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tbm-grundrechte-grch-kandidatenloesung/SKILL.md), [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-luecken/SKILL.md), [`waehlen-rechtsprechung-recherche-europarecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/waehlen-rechtsprechung-recherche-europarecht/SKILL.md), [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`einschlaegige-normen-vorschlagen-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-de/SKILL.md), [`einschlaegige-normen-vorschlagen-eu`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-eu/SKILL.md), [`eu-abgrenzung-einschlaegige-normen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-abgrenzung-einschlaegige-normen/SKILL.md), [`grundrechte-pruefung-de-und-grch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/grundrechte-pruefung-de-und-grch/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md), [`konkurrenzen-anspruchsgrundlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/konkurrenzen-anspruchsgrundlagen/SKILL.md), [`norm-historie-und-aenderungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-historie-und-aenderungen/SKILL.md), [`norm-zerlegen-mandantenbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-zerlegen-mandantenbrief/SKILL.md), [`schema-schritt-subsumtions`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schema-schritt-subsumtions/SKILL.md), [`selbst-vorgelegte-subsumtion-zerlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/selbst-vorgelegte-subsumtion-zerlegen/SKILL.md), [`subsumtions-rewrite-klausurton`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-rewrite-klausurton/SKILL.md), [`tatbestandsmerkmale-vier-zerlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tatbestandsmerkmale-vier-zerlegen/SKILL.md), [`workflow-fristen-und-risikoampel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-fristen-und-risikoampel/SKILL.md), [`zerlegen-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/zerlegen-risikoampel-und-gegenargumente/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`generalklauseln-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/generalklauseln-pruefen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`europarecht-fristen-form-und-zustaendigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/europarecht-fristen-form-und-zustaendigkeit/SKILL.md), [`output-antrag-beschwerde-klageschrift`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-antrag-beschwerde-klageschrift/SKILL.md), [`schritt-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schritt-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`verfahrensart-bestimmen-verjaehrung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verfahrensart-bestimmen-verjaehrung/SKILL.md), [`verjaehrung-fristen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verjaehrung-fristen-pruefen/SKILL.md), [`vier-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/vier-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-alltagssprache-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-alltagssprache-de/SKILL.md), [`output-fremdsprachig-en-fr`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-fremdsprachig-en-fr/SKILL.md), [`output-juristisch-gestochen-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-juristisch-gestochen-de/SKILL.md), [`output-memo-und-mandantenbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-memo-und-mandantenbrief/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`fehlerklasse-bgb-at-training`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fehlerklasse-bgb-at-training/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`eu-vorabentscheidung-falsche-wiese`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-vorabentscheidung-falsche-wiese/SKILL.md), [`falsche-wiese-warnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/falsche-wiese-warnung/SKILL.md), [`interessen-rechtsberatung-rechtsfolgen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interessen-rechtsberatung-rechtsfolgen/SKILL.md), [`kommentar-literatur-konkurrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kommentar-literatur-konkurrenzen/SKILL.md), [`rechtsberatung-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsberatung-internationaler-bezug-und-schnittstellen/SKILL.md), [`rechtsfolge-bestimmen-einreden-interaktiver`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolge-bestimmen-einreden-interaktiver/SKILL.md), [`rechtsfolgen-zahlen-schwellen-und-berechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolgen-zahlen-schwellen-und-berechnung/SKILL.md), [`spezial-pruefen-mehrparteien-konflikt-und-interessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-pruefen-mehrparteien-konflikt-und-interessen/SKILL.md), [`unbestimmte-rechtsbegriffe-ungeschriebene`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unbestimmte-rechtsbegriffe-ungeschriebene/SKILL.md), [`ungeschriebene-merkmale-judikatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ungeschriebene-merkmale-judikatur/SKILL.md), [`ziel-und-rechtsweg-bestimmung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ziel-und-rechtsweg-bestimmung/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 59 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anwenden-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/anwenden-quellenkarte/SKILL.md) | Für Anwenden Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/anwenden-quellenkarte/SKILL.md) |
| [`beweisbedarf-und-belege-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/beweisbedarf-und-belege-erfassen/SKILL.md) | Für Beweisbedarf und Belege erfassen: ordnet Akte, Belege und Lücken; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/beweisbedarf-und-belege-erfassen/SKILL.md) |
| [`darlegungs-und-beweislast-verteilen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/darlegungs-und-beweislast-verteilen/SKILL.md) | Für Darlegungs- und Beweislast verteilen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/darlegungs-und-beweislast-verteilen/SKILL.md) |
| [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/dokumente-intake/SKILL.md) | Für Dokumentenintake: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/dokumente-intake/SKILL.md) |
| [`einreden-compliance-dokumentation-und-akte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einreden-compliance-dokumentation-und-akte/SKILL.md) | Für Einreden: Compliance-Dokumentation und Aktenvermerk: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einreden-compliance-dokumentation-und-akte/SKILL.md) |
| [`einschlaegige-normen-vorschlagen-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-de/SKILL.md) | Für Einschlägige Normen vorschlagen — Deutsches Recht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-de/SKILL.md) |
| [`einschlaegige-normen-vorschlagen-eu`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-eu/SKILL.md) | Für Einschlägige Normen vorschlagen — Unionsrecht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einschlaegige-normen-vorschlagen-eu/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/einstieg-routing/SKILL.md) |
| [`eu-abgrenzung-einschlaegige-normen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-abgrenzung-einschlaegige-normen/SKILL.md) | Für Deutsches Recht und Unionsrecht — Abgrenzung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-abgrenzung-einschlaegige-normen/SKILL.md) |
| [`eu-vorabentscheidung-falsche-wiese`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-vorabentscheidung-falsche-wiese/SKILL.md) | Für EU-Vorabentscheidung prüfen (Art. 267 AEUV): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/eu-vorabentscheidung-falsche-wiese/SKILL.md) |
| [`europarecht-fristen-form-und-zustaendigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/europarecht-fristen-form-und-zustaendigkeit/SKILL.md) | Für Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/europarecht-fristen-form-und-zustaendigkeit/SKILL.md) |
| [`falsche-wiese-warnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/falsche-wiese-warnung/SKILL.md) | Für Falsche-Wiese-Warnung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/falsche-wiese-warnung/SKILL.md) |
| [`fehlerklasse-bgb-at-training`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fehlerklasse-bgb-at-training/SKILL.md) | Für Fehlerklassen im BGB-AT-Training: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/fehlerklasse-bgb-at-training/SKILL.md) |
| [`generalklauseln-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/generalklauseln-pruefen/SKILL.md) | Für Generalklauseln prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/generalklauseln-pruefen/SKILL.md) |
| [`grundrechte-pruefung-de-und-grch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/grundrechte-pruefung-de-und-grch/SKILL.md) | Für Grundrechte prüfen — GG und GRCh: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/grundrechte-pruefung-de-und-grch/SKILL.md) |
| [`interaktiver-erstpruefung-und-mandatsziel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interaktiver-erstpruefung-und-mandatsziel/SKILL.md) | Für Interaktiv: Erstprüfung, Rollenklärung und Mandatsziel: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interaktiver-erstpruefung-und-mandatsziel/SKILL.md) |
| [`interessen-rechtsberatung-rechtsfolgen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interessen-rechtsberatung-rechtsfolgen/SKILL.md) | Für Mehrparteienkonflikt und Interessenmatrix: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/interessen-rechtsberatung-rechtsfolgen/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Subsumtions Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`kandidatenloesung-subsumtion-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kandidatenloesung-subsumtion-pruefen/SKILL.md) | Für Kandidatenlösung auf Subsumtion prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kandidatenloesung-subsumtion-pruefen/SKILL.md) |
| [`kommentar-literatur-konkurrenzen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kommentar-literatur-konkurrenzen/SKILL.md) | Für Quellenhinweis ohne Blindzitate: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/kommentar-literatur-konkurrenzen/SKILL.md) |
| [`konkurrenzen-anspruchsgrundlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/konkurrenzen-anspruchsgrundlagen/SKILL.md) | Für Konkurrenzen und Anspruchsgrundlagen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/konkurrenzen-anspruchsgrundlagen/SKILL.md) |
| [`mandatsabbruch-empfehlung-beweisbedarf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/mandatsabbruch-empfehlung-beweisbedarf/SKILL.md) | Für Mandatsabbruch-Empfehlung: Weiterleitung an Fachanwalt: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/mandatsabbruch-empfehlung-beweisbedarf/SKILL.md) |
| [`norm-historie-und-aenderungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-historie-und-aenderungen/SKILL.md) | Für Norm-Historie und Änderungen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-historie-und-aenderungen/SKILL.md) |
| [`norm-zerlegen-mandantenbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-zerlegen-mandantenbrief/SKILL.md) | Für Norm zerlegen in Tatbestandsmerkmale: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/norm-zerlegen-mandantenbrief/SKILL.md) |
| [`output-alltagssprache-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-alltagssprache-de/SKILL.md) | Für Output: Alltagssprache (Deutsch): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-alltagssprache-de/SKILL.md) |
| [`output-antrag-beschwerde-klageschrift`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-antrag-beschwerde-klageschrift/SKILL.md) | Für Output: Antrag, Beschwerde, Klageschrift: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-antrag-beschwerde-klageschrift/SKILL.md) |
| [`output-fremdsprachig-en-fr`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-fremdsprachig-en-fr/SKILL.md) | Für Output: Fremdsprachig (Englisch und Französisch): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-fremdsprachig-en-fr/SKILL.md) |
| [`output-juristisch-gestochen-de`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-juristisch-gestochen-de/SKILL.md) | Für Output: Juristisch gestochen (Deutsch): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-juristisch-gestochen-de/SKILL.md) |
| [`output-memo-und-mandantenbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-memo-und-mandantenbrief/SKILL.md) | Für Output: Memo und Mandantenbrief: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-memo-und-mandantenbrief/SKILL.md) |
| [`output-pruefungsdokument-mit-warnhinweisen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-pruefungsdokument-mit-warnhinweisen/SKILL.md) | Für Output: Prüfungsdokument mit Warnhinweisen: ordnet Akte, Belege und Lücken; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/output-pruefungsdokument-mit-warnhinweisen/SKILL.md) |
| [`rechtsberatung-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsberatung-internationaler-bezug-und-schnittstellen/SKILL.md) | Für Rechtsberatung: Internationaler Bezug und Schnittstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsberatung-internationaler-bezug-und-schnittstellen/SKILL.md) |
| [`rechtsfolge-bestimmen-einreden-interaktiver`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolge-bestimmen-einreden-interaktiver/SKILL.md) | Für Rechtsfolge bestimmen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolge-bestimmen-einreden-interaktiver/SKILL.md) |
| [`rechtsfolgen-zahlen-schwellen-und-berechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolgen-zahlen-schwellen-und-berechnung/SKILL.md) | Für Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung: rechnet Beträge, Schwellen und Varianten; Ergebnis: Berechnungstabelle mit Annahmen und Kontrollfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsfolgen-zahlen-schwellen-und-berechnung/SKILL.md) |
| [`rechtsprechung-recherche-strategie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsprechung-recherche-strategie/SKILL.md) | Für Rechtsprechung-Recherche-Strategie: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Verhandlungs- oder Eskalationslinie. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/rechtsprechung-recherche-strategie/SKILL.md) |
| [`schema-schritt-subsumtions`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schema-schritt-subsumtions/SKILL.md) | Für Schema: Verhandlung, Vergleich und Eskalation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schema-schritt-subsumtions/SKILL.md) |
| [`schritt-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schritt-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Für Schriftsatz-, Brief- und Memo-Bausteine: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/schritt-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| [`selbst-vorgelegte-subsumtion-zerlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/selbst-vorgelegte-subsumtion-zerlegen/SKILL.md) | Für Selbst vorgelegte Subsumtion zerlegen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/selbst-vorgelegte-subsumtion-zerlegen/SKILL.md) |
| [`spezial-anwenden-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-anwenden-livequellen-und-rechtsprechungscheck/SKILL.md) | Für Anwenden: Livequellen- und Rechtsprechungscheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-anwenden-livequellen-und-rechtsprechungscheck/SKILL.md) |
| [`spezial-pruefen-mehrparteien-konflikt-und-interessen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-pruefen-mehrparteien-konflikt-und-interessen/SKILL.md) | Für Prüfen: Mehrparteienkonflikt und Interessenmatrix: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/spezial-pruefen-mehrparteien-konflikt-und-interessen/SKILL.md) |
| [`start-chronologie-fristen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/start-chronologie-fristen/SKILL.md) | Für Subsumtions-Prüfer — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/start-chronologie-fristen/SKILL.md) |
| [`subsumtion-obersatz-rewrite-klausurton-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-obersatz-rewrite-klausurton-triage/SKILL.md) | Für Subsumtion: Obersatz – Definition – Untersatz – Ergebnis: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtion-obersatz-rewrite-klausurton-triage/SKILL.md) |
| [`subsumtions-rewrite-klausurton`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-rewrite-klausurton/SKILL.md) | Für Subsumtion im Klausurton neu schreiben: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-rewrite-klausurton/SKILL.md) |
| [`subsumtions-tatbestand-beweis-und-belege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-tatbestand-beweis-und-belege/SKILL.md) | Für Subsumtion: Tatbestandsmerkmale, Beweisfragen und Beleglage: ordnet Akte, Belege und Lücken; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/subsumtions-tatbestand-beweis-und-belege/SKILL.md) |
| [`tatbestandsmerkmale-vier-zerlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tatbestandsmerkmale-vier-zerlegen/SKILL.md) | Für Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tatbestandsmerkmale-vier-zerlegen/SKILL.md) |
| [`tbm-grundrechte-grch-kandidatenloesung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tbm-grundrechte-grch-kandidatenloesung/SKILL.md) | Für Gegen-TBM und Einreden prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/tbm-grundrechte-grch-kandidatenloesung/SKILL.md) |
| [`triage-rechtsfrage-oder-norm`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/triage-rechtsfrage-oder-norm/SKILL.md) | Für Triage: Rechtsfrage oder Norm?: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/triage-rechtsfrage-oder-norm/SKILL.md) |
| [`unbestimmte-rechtsbegriffe-ungeschriebene`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unbestimmte-rechtsbegriffe-ungeschriebene/SKILL.md) | Für Unbestimmte Rechtsbegriffe prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unbestimmte-rechtsbegriffe-ungeschriebene/SKILL.md) |
| [`ungeschriebene-merkmale-judikatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ungeschriebene-merkmale-judikatur/SKILL.md) | Für Ungeschriebene Merkmale und Judikatur: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ungeschriebene-merkmale-judikatur/SKILL.md) |
| [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-luecken/SKILL.md) | Für Unterlagen und Lücken: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/unterlagen-luecken/SKILL.md) |
| [`verfahrensart-bestimmen-verjaehrung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verfahrensart-bestimmen-verjaehrung/SKILL.md) | Für Verfahrensart bestimmen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verfahrensart-bestimmen-verjaehrung/SKILL.md) |
| [`verjaehrung-fristen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verjaehrung-fristen-pruefen/SKILL.md) | Für Verjährung und Fristen prüfen: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/verjaehrung-fristen-pruefen/SKILL.md) |
| [`vier-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/vier-behoerden-gericht-und-registerweg/SKILL.md) | Für Behörden-, Gerichts- und Registerweg: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/vier-behoerden-gericht-und-registerweg/SKILL.md) |
| [`waehlen-rechtsprechung-recherche-europarecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/waehlen-rechtsprechung-recherche-europarecht/SKILL.md) | Für Rechtsprechung, Recherche und Europarechtsbezug wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/waehlen-rechtsprechung-recherche-europarecht/SKILL.md) |
| [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Für Chronologie und Belegmatrix für Subsumtion: ordnet Akte, Belege und Lücken; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-chronologie-und-belegmatrix/SKILL.md) |
| [`workflow-fristen-und-risikoampel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-fristen-und-risikoampel/SKILL.md) | Für Fristen- und Risikoampel für Subsumtion: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-fristen-und-risikoampel/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-kaltstart-und-routing/SKILL.md) |
| [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-unterlagen-lueckenliste/SKILL.md) | Für Unterlagen- und Lückenliste: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: Subsumtions-Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| [`zerlegen-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/zerlegen-risikoampel-und-gegenargumente/SKILL.md) | Für Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/zerlegen-risikoampel-und-gegenargumente/SKILL.md) |
| [`ziel-und-rechtsweg-bestimmung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ziel-und-rechtsweg-bestimmung/SKILL.md) | Für Ziel- und Rechtsweg-Bestimmung: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=subsumtions-pruefer/skills/ziel-und-rechtsweg-bestimmung/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
