# Vertragsausfüller

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/vertragsausfueller.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/vertragsausfueller.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/vertragsausfueller-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/vertragsausfueller-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/vertragsausfueller.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/vertragsausfueller.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Vertragsausfüller:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/vertragsausfueller.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`vertragsausfueller-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/vertragsausfueller-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`vertragsausfueller-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/vertragsausfueller-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Vertragsausfüller - BSAG Kiosk Huckelriede](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/README.md) | [Gesamt-PDF](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-vertragsausfueller-bsag-kiosk-huckelriede-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Cowork-Plugin für workflowgestütztes Ausfüllen von Vertragsvorlagen und Altverträgen. Ein Nutzer lädt eine Word-Vorlage, einen alten Vertrag, ein Term Sheet oder Freitextdaten hoch. Das Plugin strippt das Dokument, erkennt Felder und Klauseln, fragt fehlende Daten ab, mappt Term-Sheet-Daten auf Vertragsfelder und erstellt daraus einen neuen Vertragsentwurf.

Der BSAG-Mietvertrag und das Term Sheet Kiosk Huckelriede sind als Beispielakte eingebunden.

## Installation

1. Plugin-Umgebung öffnen.
2. **Customize → Plugins** bzw. **Personal plugins** wählen.
3. **Upload plugin** und `vertragsausfueller.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Fülle diesen Mietvertrag mit den Daten aus dem Term Sheet aus.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vertragsausfueller@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` enthalten.

## Workflow

1. Vorlage oder alten Vertrag hochladen.
2. Dokument strippen: Absätze, Tabellen, Platzhalter, Klauseln, Anlagen und Signaturen erkennen.
3. Term Sheet, E-Mail oder Freitextdaten danebenlegen.
4. Feldinventar und Mapping erzeugen.
5. Fehlende Daten freundlich abfragen oder als offene Platzhalter markieren.
6. Clean-Vertrag erstellen.
7. Nur auf ausdrückliche Nachfrage zusätzlich Track Changes oder Redline vorbereiten.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| kommandocenter-mehrsprachige-vertraege | steuert den gesamten Workflow von den Unterlagen bis zum neuen Vertragsentwurf. |
| docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| template-erkennung-format-track-changes | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| feldinventar-fragebogen-input | baut die zentrale Datenmatrix für den Vertrag. |
| termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| rueckfrageninterview | füllt nur entscheidungserhebliche Datenlücken. |
| bsag-mietvertrag-klauselentscheidung | setzt den Huckelriede-Fall in die BSAG-Vorlage um. |
| klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| plausibilitaetscheck-termsheet | härtet den Entwurf vor Versand oder Verhandlung. |
| clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| quality-gate-redline-qa | ist die letzte Kontrolle vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `bsag-mietvertrag-klauselentscheidung` ordnet daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung zu.

## Track-Changes-Regel

Eine ausdrücklich bestellte Track-Changes- oder Redline-Fassung wird ohne erneute Bestätigungsfrage erstellt, soweit die Dateifunktionen dies ermöglichen. Ist sie nicht beauftragt, bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll; eine zusätzliche Vergleichsfassung wird nur nach Zustimmung erzeugt. Fehlende technische Änderungsverfolgung wird als Exportgrenze benannt.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **60 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/juristischer-argumentationskern/SKILL.md), [`kommandocenter-mehrsprachige-vertraege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/kommandocenter-mehrsprachige-vertraege/SKILL.md) |
| 2. Abschluss Parteien und Auslegung | [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| 3. Leistung Vergütung und Abwicklung | [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| 4. Geheimnis Daten und Rechte | [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| 5. Haftung Sicherheiten und Störung | [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| 6. Laufzeit Beendigung und Streit | [`laufzeit-beendigung-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) | Vertragsausfüller: Abschluss Parteien und Auslegung: Vertragspartner, Abschluss, Vollmacht, Form und maßgeblichen Inhalt anhand des Fassungsverlaufs prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Vertragsausfüller: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) | Vertragsausfüller: Geheimnis Daten und Rechte: Geheimnisse, Daten, Nutzungsrechte und Weitergabe im tatsächlichen Geschäftsvorgang absichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) | Vertragsausfüller: Haftung Sicherheiten und Störung: Haftung, Mängel, Sicherheit, Leistungsstörung und wirtschaftliche Risikozuordnung gestalten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Vertragsausfüller ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/juristischer-argumentationskern/SKILL.md) |
| [`kommandocenter-mehrsprachige-vertraege`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/kommandocenter-mehrsprachige-vertraege/SKILL.md) | Für Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Vertragsausfüller. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/kommandocenter-mehrsprachige-vertraege/SKILL.md) |
| [`laufzeit-beendigung-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) | Vertragsausfüller: Laufzeit Beendigung und Streit: Laufzeit, Kündigung, Abwicklung, Rückgabe und Streitbeilegung mit den übrigen Klauseln abstimmen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) |
| [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) | Vertragsausfüller: Leistung Vergütung und Abwicklung: Leistung, Gegenleistung, Abnahme, laufende Pflichten und Abrechnung konkret ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Vertragsausfüller: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=vertragsausfueller/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
