# Juristische Presseberichterstattung

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Plugin für juristische Presseberichterstattung: Gerichtsbericht, Entscheidungsnews, Verdachtsbericht, Pressemitteilung, Headline, Bildprüfung, Quellenmatrix und Redaktionsschluss-Qualitygate.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`juristische-presseberichterstattung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/juristische-presseberichterstattung.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/juristische-presseberichterstattung.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/juristische-presseberichterstattung-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/juristische-presseberichterstattung-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/juristische-presseberichterstattung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/juristische-presseberichterstattung.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Juristische Presseberichterstattung:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Quellenmatrix: Aussage, Aussagetyp, Aktenfund, Gegenposition, Stellungnahme, Identifizierungsrisiko, Freigabestatus und Formulierung. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`juristische-presseberichterstattung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/juristische-presseberichterstattung.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`juristische-presseberichterstattung-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/juristische-presseberichterstattung-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`juristische-presseberichterstattung-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/juristische-presseberichterstattung-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Juristische Presseberichterstattung — Verdachtsberichterstattung im Wirtschaftsverfahren Köln](../testakten/pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln/README.md) | [Gesamt-PDF](../testakten/pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln/gesamt-pdf/pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln_gesamt.pdf) | [`testakte-pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln.zip) | [`testakte-pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-pressebericht-verdachtsberichterstattung-wirtschaftsverfahren-koeln-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du dieses Plugin öffnest, willst du aus juristischem Material schnell einen sauberen journalistischen Text bauen: Meldung, Gerichtsbericht, Entscheidungsbericht, Hintergrundstück, Pressemitteilung, FAQ, Headline-Set oder Redaktionsvermerk.

Das Plugin arbeitet mit Quellenmatrix, Statussprache und Veröffentlichungsrisiko. Es trennt Tatsachen, Verdacht, Verfahrensstand, Zitat, Bewertung, Bildfrage und Gegendarstellung, damit der Text zügig erscheint und trotzdem belastbar bleibt.

## Kaltstart

1. Welches Format: Meldung, Bericht, Analyse, Pressemitteilung, FAQ, Liveblog oder Social-Thread?
2. Welcher Status: Ermittlungsverfahren, Anklage, Hauptverhandlung, Urteil, Beschluss, Vergleich, Behördenentscheidung oder Gesetzgebung?
3. Welche Quelle trägt den ersten Satz?
4. Wer ist betroffen und wurde Stellungnahme angefragt?
5. Welche Namen, Bilder und Details sind wirklich nötig?
6. Was muss bis Redaktionsschluss fertig sein?

## Arbeitsprodukt zuerst

Starte mit einem verwertbaren Entwurf oder einer kurzen Redaktionsmatrix. Wenn Fakten fehlen, markiere sie als offen und formuliere eine konkrete Nachforderung statt den Text zu blockieren.

## Quellenanker

- Grundgesetz Artikel 5: Meinungs-, Presse- und Berichterstattungsfreiheit.
- Kunsturhebergesetz Paragraf 22 und Paragraf 23: Bildnis, Einwilligung und Zeitgeschichte.
- Bürgerliches Gesetzbuch Paragraf 823 und Paragraf 1004 analog: Persönlichkeitsrechtliche Abwehr- und Unterlassungslinien.
- Pressekodex: Wahrhaftigkeit, Sorgfalt, Unschuldsvermutung, Schutz der Persönlichkeit, Trennung von Werbung und Redaktion.
- Bundesverfassungsgericht, Beschluss vom 03.11.2025, 1 BvR 573/25: Pressefreiheit und Verdachtsberichterstattung im wirtschaftlichen Kontext als aktueller Suchanker.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`kaltstart-redaktionsauftrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/kaltstart-redaktionsauftrag/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`faktencheck-quellenmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faktencheck-quellenmatrix/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/juristischer-argumentationskern/SKILL.md), [`korrektur-gegendarstellung-risiko`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/korrektur-gegendarstellung-risiko/SKILL.md), [`verdachtsberichterstattung-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verdachtsberichterstattung-pruefung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`wirtschaftsverfahren-compliance-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/wirtschaftsverfahren-compliance-bericht/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`entscheidung-meldung-und-urteilsbericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/entscheidung-meldung-und-urteilsbericht/SKILL.md), [`gerichtstermin-sitzungsbericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/gerichtstermin-sitzungsbericht/SKILL.md), [`liveblog-ticker-gericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/liveblog-ticker-gericht/SKILL.md), [`pressemitteilung-kanzlei-behoerde`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/pressemitteilung-kanzlei-behoerde/SKILL.md), [`strafverfahren-unschuldsvermutung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/strafverfahren-unschuldsvermutung/SKILL.md), [`verwaltungsgericht-politikrecht-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verwaltungsgericht-politikrecht-bericht/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`familien-erbrecht-diskret-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/familien-erbrecht-diskret-bericht/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`redaktionsschluss-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/redaktionsschluss-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`anonymisierung-identifizierbarkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/anonymisierung-identifizierbarkeit/SKILL.md), [`bildunterschrift-foto-kug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/bildunterschrift-foto-kug/SKILL.md), [`faq-explainer-rechtsfrage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faq-explainer-rechtsfrage/SKILL.md), [`headline-und-vorspann`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/headline-und-vorspann/SKILL.md), [`interview-fragekatalog-juristisch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/interview-fragekatalog-juristisch/SKILL.md), [`persoenlichkeitsrecht-abwaegung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/persoenlichkeitsrecht-abwaegung/SKILL.md), [`social-media-thread-recht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/social-media-thread-recht/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 21 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anonymisierung-identifizierbarkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/anonymisierung-identifizierbarkeit/SKILL.md) | Für Anonymisierung und Identifizierbarkeit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/anonymisierung-identifizierbarkeit/SKILL.md) |
| [`bildunterschrift-foto-kug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/bildunterschrift-foto-kug/SKILL.md) | Für Bildunterschrift und Foto KUG: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/bildunterschrift-foto-kug/SKILL.md) |
| [`entscheidung-meldung-und-urteilsbericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/entscheidung-meldung-und-urteilsbericht/SKILL.md) | Für Entscheidung Meldung und Urteilsbericht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/entscheidung-meldung-und-urteilsbericht/SKILL.md) |
| [`faktencheck-quellenmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faktencheck-quellenmatrix/SKILL.md) | Für Faktencheck Quellenmatrix: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faktencheck-quellenmatrix/SKILL.md) |
| [`familien-erbrecht-diskret-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/familien-erbrecht-diskret-bericht/SKILL.md) | Für Diskrete Berichterstattung Familienrecht und Erbrecht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/familien-erbrecht-diskret-bericht/SKILL.md) |
| [`faq-explainer-rechtsfrage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faq-explainer-rechtsfrage/SKILL.md) | Für FAQ und Explainer Rechtsfrage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/faq-explainer-rechtsfrage/SKILL.md) |
| [`gerichtstermin-sitzungsbericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/gerichtstermin-sitzungsbericht/SKILL.md) | Für Gerichtstermin Sitzungsbericht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/gerichtstermin-sitzungsbericht/SKILL.md) |
| [`headline-und-vorspann`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/headline-und-vorspann/SKILL.md) | Für Headline und Vorspann: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/headline-und-vorspann/SKILL.md) |
| [`interview-fragekatalog-juristisch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/interview-fragekatalog-juristisch/SKILL.md) | Für Interview Fragekatalog juristisch: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/interview-fragekatalog-juristisch/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Juristische Presseberichterstattung ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-redaktionsauftrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/kaltstart-redaktionsauftrag/SKILL.md) | Für Kaltstart Redaktionsauftrag: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/kaltstart-redaktionsauftrag/SKILL.md) |
| [`korrektur-gegendarstellung-risiko`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/korrektur-gegendarstellung-risiko/SKILL.md) | Für Korrektur Gegendarstellung Risiko: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/korrektur-gegendarstellung-risiko/SKILL.md) |
| [`liveblog-ticker-gericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/liveblog-ticker-gericht/SKILL.md) | Für Liveblog Ticker Gericht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/liveblog-ticker-gericht/SKILL.md) |
| [`persoenlichkeitsrecht-abwaegung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/persoenlichkeitsrecht-abwaegung/SKILL.md) | Für Persönlichkeitsrecht Abwägung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/persoenlichkeitsrecht-abwaegung/SKILL.md) |
| [`pressemitteilung-kanzlei-behoerde`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/pressemitteilung-kanzlei-behoerde/SKILL.md) | Für Pressemitteilung Kanzlei Behörde: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/pressemitteilung-kanzlei-behoerde/SKILL.md) |
| [`redaktionsschluss-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/redaktionsschluss-qualitygate/SKILL.md) | Für Redaktionsschluss Qualitygate: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/redaktionsschluss-qualitygate/SKILL.md) |
| [`social-media-thread-recht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/social-media-thread-recht/SKILL.md) | Für Social Media Thread Recht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/social-media-thread-recht/SKILL.md) |
| [`strafverfahren-unschuldsvermutung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/strafverfahren-unschuldsvermutung/SKILL.md) | Für Strafverfahren und Unschuldsvermutung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/strafverfahren-unschuldsvermutung/SKILL.md) |
| [`verdachtsberichterstattung-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verdachtsberichterstattung-pruefung/SKILL.md) | Für Verdachtsberichterstattung Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verdachtsberichterstattung-pruefung/SKILL.md) |
| [`verwaltungsgericht-politikrecht-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verwaltungsgericht-politikrecht-bericht/SKILL.md) | Für Verwaltungsgericht und Politikrecht Bericht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/verwaltungsgericht-politikrecht-bericht/SKILL.md) |
| [`wirtschaftsverfahren-compliance-bericht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/wirtschaftsverfahren-compliance-bericht/SKILL.md) | Für Wirtschaftsverfahren Compliance Bericht: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=juristische-presseberichterstattung/skills/wirtschaftsverfahren-compliance-bericht/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
