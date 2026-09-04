# Arbeitszeugnisprüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Prüft bestehende deutsche Arbeitszeugnisse Schritt für Schritt: Notenstufen, Zufriedenheits- und Verhaltensformeln, Geheimcodes, Auslassungen, Steigerungsadverbien, Schlussformel. Liefert Ampel-Einschätzung pro Satz, Gesamtnote, Aufforderungsschreiben oder Klagestrategie zur Berichtigung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/arbeitszeugnispruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/arbeitszeugnispruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/arbeitszeugnispruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Arbeitszeugnisprüfer:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Änderungsmatrix: Satz des Arbeitgebers, Problem, Rechtsanker, gewünschte Fassung, Beleg und Prozessrisiko als Tabelle ausgeben. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`arbeitszeugnispruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`arbeitszeugnispruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| Pluginlokale Akte | [Gesamt-PDF](testakte/gesamt-pdf/testakte_gesamt.pdf) | [`arbeitszeugnispruefer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte.zip) | [`arbeitszeugnispruefer-testakte-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer-testakte-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein bereits vorliegendes deutsches Arbeitszeugnis Satz für Satz prüfen — Note, Geheimcodes, Auslassungen, Schlussformel — und brauchst eine belastbare Einschätzung mit Rechtsprechungsanker.

## Wenn du das brauchst

- **Arbeitnehmer** hat ein Zeugnis erhalten und will wissen, welche Note darin codiert ist, bevor er bewirbt oder widerspricht.
- **Fachanwalt für Arbeitsrecht** prüft ein Zeugnis im Mandat auf Berichtigungsanspruch nach Paragraf 109 GewO.
- **Personalabteilung** prüft das eigene Zeugnis vor der Ausstellung gegen die Standards der BAG-Rechtsprechung.
- **Karriereberater oder Outplacement-Berater** sichten Zeugnisse aus dem Lebenslauf ihrer Klienten und brauchen eine schnelle Einordnung.

## Was du am Ende in der Hand hast

Eine Prüfung Satz für Satz mit Ampel-Einschätzung (rot, orange, grün), eine begründete Gesamtnotenspanne, eine Liste der Geheimcodes, Drift-Stellen und Auslassungen, ein Mandantenbericht in Klartext sowie auf Wunsch ein Aufforderungsschreiben an den Arbeitgeber zur Berichtigung oder eine Klagestrategie mit Vollstreckungsoption.

## Der Weg dorthin

Zeugnis einlesen → Stammdaten und Vollständigkeit prüfen → Tätigkeitsabschnitt auf Wertigkeitsdrift prüfen → Leistungssätze auf Zufriedenheitsformel und Steigerungsadverbien prüfen → Verhaltenssätze auf Personenreihenfolge und Geheimcodes prüfen → Schlussformel auf Note-Mismatch prüfen → Gesamtnote ableiten → Berichtigungspfad oder Annahme empfehlen.

## Workflows

Drei Modi zur Wahl:

- **Schnellprüfung**: Notenschätzung, Top-Drei-Auffälligkeiten, Empfehlung in wenigen Sätzen.
- **Vollprüfung**: Satzweise Einschätzungsmatrix, Geheimcode-Katalog, Drift-Bericht, Schlussformel-Analyse, Mandantenbericht.
- **Berichtigungspfad**: Vollprüfung plus Aufforderungsschreiben an den Arbeitgeber und Klagestrategie mit Beweislastverteilung nach BAG-Linie.

## Was dich aufhält

- **Geheimcodes**: Formulierungen wie bemüht sich, im großen und ganzen, lernte schnell kennen und schätzen, verstand es zählen zu unsichtbaren Notenabwertungen.
- **Auslassungen**: Fehlt die Zusammenfassungsformel, fehlen Personengruppen im Verhalten, fehlt die Schlussformel, wirkt das wie eine Abwertung.
- **Drift in der Wertigkeit**: Wenn unwichtige Aufgaben zuerst genannt werden oder Kernaufgaben fehlen, droht Schaufenster-Effekt.
- **Beweislast nach BAG 9 AZR 584.13**: Note 1 oder 2 trägt der Arbeitnehmer, Note 4 oder 5 trägt der Arbeitgeber.
- **Schlussformel-Mismatch**: Schwache Schlussformel bei sonst gutem Zeugnis zieht die Gesamtwirkung herunter.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch und Berichtigung)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## KI-Verordnung: mögliche Einstufung als Hochrisiko-KI

Wird dieses Plugin im Personalwesen produktiv eingesetzt, kann es ein Hochrisiko-KI-System nach Artikel 6 Absatz 2 in Verbindung mit Anhang III Nummer 4 Buchstabe b der Verordnung (EU) 2024/1689 (KI-Verordnung) sein. Anhang III Nummer 4 Buchstabe b erfasst KI-Systeme, die bestimmungsgemäß für Entscheidungen über die Bedingungen von Arbeitsverhältnissen, für die Bewertung der Arbeitsleistung und des Arbeitsverhaltens oder für vergleichbare Personalentscheidungen verwendet werden. Eine automatisierte Prüfung eines Arbeitszeugnisses, etwa zur Bewertung der Notenstufe oder zur Steuerung von Berichtigungsansprüchen, betrifft genau diese Bewertungs- und Bedingungsdimension. Anhang III Nummer 4 Buchstabe a erfasst dagegen die Personalauswahl und Bewerbungsphase und greift hier in der Regel nicht.

Folgen einer Einstufung als Hochrisiko-KI können sein: Pflicht zu menschlicher Aufsicht, Dokumentations- und Transparenzpflichten, Risikomanagement, Information der Beschäftigten beziehungsweise des Betriebsrats und gegebenenfalls eine Grundrechte-Folgenabschätzung. Die genaue Reichweite hängt vom Einsatzkontext, von der Rolle als Anbieter oder Betreiber und vom Geltungsbeginn nach Artikel 113 KI-VO ab. Diese Hinweise sind keine Rechtsberatung; im Zweifel ist eine arbeitsrechtliche und KI-rechtliche Bewertung im Einzelfall geboten.

## Hinweise

Generischer Prüfstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Prüfbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`intake-und-stammdaten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/intake-und-stammdaten-pruefen/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`beweislast-bag-9-azr-584-13`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beweislast-bag-9-azr-584-13/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`klagestrategie-und-vollstreckung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/klagestrategie-und-vollstreckung/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aeussere-form-und-briefkopf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aeussere-form-und-briefkopf/SKILL.md), [`aufforderungsschreiben-berichtigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aufforderungsschreiben-berichtigung/SKILL.md), [`mandantenbericht-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/mandantenbericht-erstellen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`zeugnisklarheit-objektiver-empfaengerhorizont`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`ampel-einschaetzung-pro-satz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/ampel-einschaetzung-pro-satz/SKILL.md), [`auslassungen-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/auslassungen-erkennen/SKILL.md), [`beendigungsgrund-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beendigungsgrund-pruefen/SKILL.md), [`doppelboeden-und-verneinungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/doppelboeden-und-verneinungen/SKILL.md), [`einfuehrung-pruefauftrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einfuehrung-pruefauftrag/SKILL.md), [`frequenzadverbien-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/frequenzadverbien-pruefen/SKILL.md), [`fuehrungskraft-verhalten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/fuehrungskraft-verhalten-pruefen/SKILL.md), [`geheimcodes-katalog`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/geheimcodes-katalog/SKILL.md), [`note-1-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-1-formeln-erkennen/SKILL.md), [`note-2-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-2-formeln-erkennen/SKILL.md), [`note-3-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-3-formeln-erkennen/SKILL.md), [`note-4-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-4-formeln-erkennen/SKILL.md), [`note-5-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-5-formeln-erkennen/SKILL.md), [`notenstufen-bag-9-azr-386-10`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/notenstufen-bag-9-azr-386-10/SKILL.md), [`personenreihenfolge-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/personenreihenfolge-pruefen/SKILL.md), [`rollen-und-modus-wahl`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/rollen-und-modus-wahl/SKILL.md), [`schaufenster-und-drift-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schaufenster-und-drift-erkennen/SKILL.md), [`schlussformel-notenwirkung-bewerten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schlussformel-notenwirkung-bewerten/SKILL.md), ... plus 5 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 31 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 31 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`aeussere-form-und-briefkopf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aeussere-form-und-briefkopf/SKILL.md) | Für Äußere Form und Briefkopf prüfen: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aeussere-form-und-briefkopf/SKILL.md) |
| [`ampel-einschaetzung-pro-satz`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/ampel-einschaetzung-pro-satz/SKILL.md) | Für Ampel-Einschätzung pro Satz: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/ampel-einschaetzung-pro-satz/SKILL.md) |
| [`aufforderungsschreiben-berichtigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aufforderungsschreiben-berichtigung/SKILL.md) | Für Aufforderungsschreiben Berichtigung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/aufforderungsschreiben-berichtigung/SKILL.md) |
| [`auslassungen-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/auslassungen-erkennen/SKILL.md) | Für Auslassungen erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/auslassungen-erkennen/SKILL.md) |
| [`beendigungsgrund-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beendigungsgrund-pruefen/SKILL.md) | Für Beendigungsgrund prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beendigungsgrund-pruefen/SKILL.md) |
| [`beweislast-bag-9-azr-584-13`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beweislast-bag-9-azr-584-13/SKILL.md) | Für Beweislast nach BAG 9 AZR 584.13: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/beweislast-bag-9-azr-584-13/SKILL.md) |
| [`doppelboeden-und-verneinungen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/doppelboeden-und-verneinungen/SKILL.md) | Für Doppelböden und Verneinungen erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/doppelboeden-und-verneinungen/SKILL.md) |
| [`einfuehrung-pruefauftrag`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einfuehrung-pruefauftrag/SKILL.md) | Für Einführung in den Prüfauftrag: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/einfuehrung-pruefauftrag/SKILL.md) |
| [`frequenzadverbien-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/frequenzadverbien-pruefen/SKILL.md) | Für Frequenzadverbien prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/frequenzadverbien-pruefen/SKILL.md) |
| [`fuehrungskraft-verhalten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/fuehrungskraft-verhalten-pruefen/SKILL.md) | Für Führungskraft-Verhalten prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/fuehrungskraft-verhalten-pruefen/SKILL.md) |
| [`geheimcodes-katalog`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/geheimcodes-katalog/SKILL.md) | Für Geheimcodes-Katalog: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/geheimcodes-katalog/SKILL.md) |
| [`intake-und-stammdaten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/intake-und-stammdaten-pruefen/SKILL.md) | Für Intake und Stammdaten prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/intake-und-stammdaten-pruefen/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Arbeitszeugnisprüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`klagestrategie-und-vollstreckung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/klagestrategie-und-vollstreckung/SKILL.md) | Für Klagestrategie und Vollstreckung: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/klagestrategie-und-vollstreckung/SKILL.md) |
| [`mandantenbericht-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/mandantenbericht-erstellen/SKILL.md) | Für Mandantenbericht erstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/mandantenbericht-erstellen/SKILL.md) |
| [`note-1-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-1-formeln-erkennen/SKILL.md) | Für Note-1-Formeln erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-1-formeln-erkennen/SKILL.md) |
| [`note-2-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-2-formeln-erkennen/SKILL.md) | Für Note-2-Formeln erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-2-formeln-erkennen/SKILL.md) |
| [`note-3-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-3-formeln-erkennen/SKILL.md) | Für Note-3-Formeln erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-3-formeln-erkennen/SKILL.md) |
| [`note-4-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-4-formeln-erkennen/SKILL.md) | Für Note-4-Formeln erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-4-formeln-erkennen/SKILL.md) |
| [`note-5-formeln-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-5-formeln-erkennen/SKILL.md) | Für Note-5-Formeln erkennen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/note-5-formeln-erkennen/SKILL.md) |
| [`notenstufen-bag-9-azr-386-10`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/notenstufen-bag-9-azr-386-10/SKILL.md) | Für Notenstufen nach BAG 9 AZR 386.10: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/notenstufen-bag-9-azr-386-10/SKILL.md) |
| [`personenreihenfolge-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/personenreihenfolge-pruefen/SKILL.md) | Für Personenreihenfolge prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/personenreihenfolge-pruefen/SKILL.md) |
| [`rollen-und-modus-wahl`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/rollen-und-modus-wahl/SKILL.md) | Für Rollen- und Moduswahl vor der Zeugnisprüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/rollen-und-modus-wahl/SKILL.md) |
| [`schaufenster-und-drift-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schaufenster-und-drift-erkennen/SKILL.md) | Für Schaufenster- und Drift-Erkennung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schaufenster-und-drift-erkennen/SKILL.md) |
| [`schlussformel-notenwirkung-bewerten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schlussformel-notenwirkung-bewerten/SKILL.md) | Für Schlussformel-Notenwirkung bewerten: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schlussformel-notenwirkung-bewerten/SKILL.md) |
| [`schlussformel-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schlussformel-pruefen/SKILL.md) | Für Schlussformel prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/schlussformel-pruefen/SKILL.md) |
| [`steigerungsadverbien-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/steigerungsadverbien-pruefen/SKILL.md) | Für Steigerungsadverbien prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/steigerungsadverbien-pruefen/SKILL.md) |
| [`taetigkeitsabschnitt-wertigkeit-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/taetigkeitsabschnitt-wertigkeit-pruefen/SKILL.md) | Für Tätigkeitsabschnitt und Wertigkeit prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/taetigkeitsabschnitt-wertigkeit-pruefen/SKILL.md) |
| [`verhaltensabschnitt-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/verhaltensabschnitt-pruefen/SKILL.md) | Für Verhaltensabschnitt prüfen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/verhaltensabschnitt-pruefen/SKILL.md) |
| [`zeugnisklarheit-objektiver-empfaengerhorizont`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) | Für Zeugnisklarheit nach dem objektiven Empfängerhorizont (BAG 9 AZR 352.04; 9 AZR 386.10): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zeugnisklarheit-objektiver-empfaengerhorizont/SKILL.md) |
| [`zusammenfassungsformel-erkennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zusammenfassungsformel-erkennen/SKILL.md) | Für Zusammenfassungsformel erkennen und decodieren: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=arbeitszeugnispruefer/skills/zusammenfassungsformel-erkennen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
