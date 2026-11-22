# Luftrecht und Flughafenrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Luftrecht-Plugin für LuftVG, LuftSiG, LBA, Flughäfen, Airlines, Slots, Flugzeugpfandrechte, Beschlagnahme, Insolvenz, Drohnen und Aviation-Compliance.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`luftrecht-flughafenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/luftrecht-flughafenrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/luftrecht-flughafenrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/luftrecht-flughafenrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/luftrecht-flughafenrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/luftrecht-flughafenrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/luftrecht-flughafenrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Luftrecht und Flughafenrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`luftrecht-flughafenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/luftrecht-flughafenrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`luftrecht-flughafenrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/luftrecht-flughafenrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`luftrecht-flughafenrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/luftrecht-flughafenrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Luftrechtsakte](../testakten/luftrecht-airline-insolvenz-flugzeugpfand-flughafen/README.md) | [Gesamt-PDF](../testakten/luftrecht-airline-insolvenz-flugzeugpfand-flughafen/gesamt-pdf/luftrecht-airline-insolvenz-flugzeugpfand-flughafen_gesamt.pdf) | [`testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip) | [`testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin deckt ziviles und öffentliches Luftrecht ab: Luftfahrzeug, Flughafen, Betriebsgenehmigung, LBA, Luftsicherheit, Slots, Flugzeugfinanzierung, Registerpfandrechte, Pfändung, Airline-Krise und internationale Bezüge.

## Start

Beginne mit den vorhandenen Genehmigungen, Verträgen, Registerangaben oder Betriebsunterlagen und dem konkreten Auftrag. `luftrecht-flughafenrecht-allgemein` trennt Flughafenbetrieb, Luftfahrzeug, Finanzierung und behördlichen Rechtsschutz. Nur offene Angaben zu Rolle, Zuständigkeit oder Zeitablauf, die das Ergebnis ändern, werden erfragt. Anschließend wird das bestellte Dokument ausgearbeitet und nach neuen Belegen an der betroffenen Stelle fortgeführt.

## Arbeitsweise

- Es arbeitet mit Akten- und Fristenlogik statt mit Bauchgefühl.
- Es trennt Rechtsgrundlage, Verfahren, Beweis, Kosten, Kommunikation und Eskalation.
- Es soll Nutzer befähigen: verständliche Erklärung, präzise Rückfragen, dann belastbarer Entwurf.
- Rechtsprechung und Gesetzesstände werden nicht halluziniert, sondern als Live-Check über amtliche oder frei zugängliche Quellen markiert.

## Typische Outputs

- Kaltstart-Interview und Aktenlandkarte
- Behörden-, Gerichts- oder Gegneranschreiben
- Widerspruchs-/Klage-/Eilantragsbausteine
- Kosten-, Fristen- und Zuständigkeitsmatrix
- Dashboard/Tracker für laufende Vorgänge
- Kurzfassung für Mandant, Vorstand, Verband, Redaktion oder Bürgerin

## Quellenhygiene

Siehe [`references/QUELLEN.md`](./references/QUELLEN.md). Dieses Plugin gibt keine endgültige Rechtsberatung, sondern robuste Arbeitsfassungen, Prüfpfade und Dokumentationshilfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **240 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/kaltstart-triage/SKILL.md) |
| 2. Unternehmen und Luftfahrzeug | [`unternehmen-und-luftfahrzeug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/unternehmen-und-luftfahrzeug-bearbeiten/SKILL.md) |
| 3. Flughafen und Bodenbetrieb | [`flughafen-und-bodenbetrieb-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flughafen-und-bodenbetrieb-bearbeiten/SKILL.md) |
| 4. Flugbetrieb und Personal | [`flugbetrieb-und-personal-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flugbetrieb-und-personal-bearbeiten/SKILL.md) |
| 5. Sicherheit und besondere Einsätze | [`sicherheit-und-besondere-einsaetze-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/sicherheit-und-besondere-einsaetze-bearbeiten/SKILL.md) |
| 6. Beförderung und Haftung | [`befoerderung-und-haftung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/befoerderung-und-haftung-bearbeiten/SKILL.md) |
| 7. Umwelt und internationale Regeln | [`umwelt-und-internationale-regeln-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/umwelt-und-internationale-regeln-bearbeiten/SKILL.md) |
| 8. Verfahren und Rechtsschutz | [`verfahren-und-rechtsschutz-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/verfahren-und-rechtsschutz-bearbeiten/SKILL.md) |
| 9. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erk... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`befoerderung-und-haftung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/befoerderung-und-haftung-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Beförderung und Haftung: Passagier, Gepäck, Fracht, Reise, Unfall und Versicherung mit Leistungs- und Schadensbelegen prüfen. Vollständige Fachanweisungen und lokale Vorlagen werden g... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/befoerderung-und-haftung-bearbeiten/SKILL.md) |
| [`flugbetrieb-und-personal-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flugbetrieb-und-personal-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Flugbetrieb und Personal: Betrieb, Besatzung, Lizenz, Arbeitszeit, Wartung und technische Lufttüchtigkeit nach dem richtigen Regime prüfen. Vollständige Fachanweisungen und lokale Vor... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flugbetrieb-und-personal-bearbeiten/SKILL.md) |
| [`flughafen-und-bodenbetrieb-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flughafen-und-bodenbetrieb-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Flughafen und Bodenbetrieb: Flughafenrecht, Slots, Bodenabfertigung, Infrastruktur, Entgelte und Zugang am konkreten Standort bearbeiten. Vollständige Fachanweisungen und lokale Vorla... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/flughafen-und-bodenbetrieb-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/juristischer-argumentationskern/SKILL.md) | Luftrechtlichen Vorgang bis zum belastbaren Antrag führen. Verarbeitet vorhandene Unterlagen, prüft entscheidende Fachfragen und führt den Auftrag zum vollständig formulierten Ergebnis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/kaltstart-triage/SKILL.md) | Für Luftrecht und Flughafenrecht - Allgemeiner Einstieg: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/kaltstart-triage/SKILL.md) |
| [`sicherheit-und-besondere-einsaetze-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/sicherheit-und-besondere-einsaetze-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Sicherheit und besondere Einsätze: Luftsicherheit, Zuverlässigkeit, Gefahrgut, Drohnen, Hubschrauber und besondere Flüge getrennt bearbeiten. Vollständige Fachanweisungen und lokale V... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/sicherheit-und-besondere-einsaetze-bearbeiten/SKILL.md) |
| [`umwelt-und-internationale-regeln-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/umwelt-und-internationale-regeln-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Umwelt und internationale Regeln: Emissionen, Klimaregeln, Verkehrsrechte, internationales Abkommen und grenzüberschreitende Aufsicht abgleichen. Vollständige Fachanweisungen und loka... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/umwelt-und-internationale-regeln-bearbeiten/SKILL.md) |
| [`unternehmen-und-luftfahrzeug-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/unternehmen-und-luftfahrzeug-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Unternehmen und Luftfahrzeug: Betriebsgenehmigung, Eigentum, Register, Leasing, Zulassung und Finanzierung von Airline oder Luftfahrzeug prüfen. Vollständige Fachanweisungen und lokal... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/unternehmen-und-luftfahrzeug-bearbeiten/SKILL.md) |
| [`verfahren-und-rechtsschutz-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/verfahren-und-rechtsschutz-bearbeiten/SKILL.md) | Für Luftverkehrs-, Flughafen- und Luftaufsichtsrecht: Verfahren und Rechtsschutz: Behörde, Antrag, Nachforderung, Sanktion, Zuständigkeit und Rechtsbehelf bis zum konkreten Schreiben bearbeiten. Vollständige Fachanweisungen und lokale Vo... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=luftrecht-flughafenrecht/skills/verfahren-und-rechtsschutz-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
