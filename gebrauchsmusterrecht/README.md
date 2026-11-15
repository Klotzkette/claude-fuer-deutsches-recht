# gebrauchsmusterrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Eigenständiges Plugin für deutsches Gebrauchsmusterrecht: GebrMG, DPMA-Anmeldung, Recherche nach Paragraf 7 GebrMG, Abzweigung, Neuheitsschonfrist, Verletzung, Löschung, BPatG-Beschwerde, Lizenz, FTO und Schnellschutz für technische Produkte.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`gebrauchsmusterrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/gebrauchsmusterrecht.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/gebrauchsmusterrecht.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/gebrauchsmusterrecht-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/gebrauchsmusterrecht-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/gebrauchsmusterrecht.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/gebrauchsmusterrecht.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für gebrauchsmusterrecht:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`gebrauchsmusterrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/gebrauchsmusterrecht.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`gebrauchsmusterrecht-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/gebrauchsmusterrecht-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`gebrauchsmusterrecht-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/gebrauchsmusterrecht-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Schnellverschluss S-14: Sensorhalter, Gebrauchsmusterabzweigung und Messeoffenbarung](../testakten/gebrauchsmusterrecht-schnellverschluss-sensorhalter/README.md) | [Gesamt-PDF](../testakten/gebrauchsmusterrecht-schnellverschluss-sensorhalter/gesamt-pdf/gebrauchsmusterrecht-schnellverschluss-sensorhalter_gesamt.pdf) | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip) | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Dieses Plugin behandelt das deutsche Gebrauchsmuster als schnelles, ungeprüft eingetragenes technisches Schutzrecht. Es führt durch Anmeldung, Recherche, Abzweigung, Schutzfähigkeit, Verletzung und Löschung, ohne die gefährliche Abkürzung zu nehmen: Eintragung ist noch kein belastbarer Rechtsbestand.

## Arbeitsmodus

Aus Gebrauchsmusterschrift, Registerauszug, Produktunterlagen und bekanntem Stand der Technik wird zuerst die konkrete Aufgabe bestimmt: Anmeldung, Rechtsbestandsprüfung, Löschung oder Verletzung. Nur entscheidende fehlende Angaben zu Schutzanspruch, Priorität, Offenbarung oder angegriffenem Produkt werden nachgefragt. Bei klarem Auftrag beginnt unmittelbar der verlangte Entwurf; nachgereichte Belege werden an der betroffenen Anspruchs- oder Merkmalsprüfung eingearbeitet. Die Eintragung ersetzt keine Prüfung der Schutzfähigkeit.

## Praxisblöcke

| Block | Wofür? |
| --- | --- |
| Kaltstart | Technik, Produkt, Frist, Offenbarung, Patentbezug und Ziel klären |
| Anmeldung | Formalien, Ansprüche, Beschreibung, Zeichnungen, Abzweigung und Schonfrist |
| Rechtsbestand | Neuheit, erfinderischer Schritt, Ausschlüsse, Recherche und Löschung |
| Durchsetzung | Verletzung, eV, Abmahnung, Klage, Auskunft und Schadensersatz |
| Verwertung | Lizenzen, Übertragung, Insolvenz, Start-up-Strategie und internationale Alternativen |

## Quellen- und Zitierhygiene

- Offizielle Normtexte, Amtsinformationen und Register zuerst: keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate, keine Paywall-Literatur als scheinbare Quelle.
- Register-, Gebühren-, Formular- und Fristenfragen immer live prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher oder amtlicher Quelle verwenden.
- Bei ausländischem Recht Local-Counsel-Prüfbedarf offen kennzeichnen.

## Verhältnis zu anderen Plugins

- `markenrecht-fashion-luxus` für tiefe Marken-, Plattform- und Counterfeit-Fragen.
- `gewerblicher-rechtsschutz` und `fachanwalt-gewerblicher-rechtsschutz` für breiten IP-Kontext.
- `patentrecht` und `gebrauchsmusterrecht` für technische Schutzrechte.
- `produktrecht`, `ecommerce-recht` und `datenschutzrecht` für Produkt-, Shop- und Datenfragen.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **51 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/kaltstart-triage/SKILL.md) |
| 2. Schutzweg und Frist | [`schutzweg-und-frist-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzweg-und-frist-bearbeiten/SKILL.md) |
| 3. Schutzgegenstand | [`schutzgegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzgegenstand-bearbeiten/SKILL.md) |
| 4. Rechtsbestand | [`rechtsbestand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/rechtsbestand-bearbeiten/SKILL.md) |
| 5. Schutzbereich und Verletzung | [`schutzbereich-und-verletzung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzbereich-und-verletzung-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. Vollständige Fachanwe... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Arbeitsprodukt: Anmeldung, Abzweigungserklärung, Rechercheauftrag, Löschungsantrag, Abmahnung, Klage oder Verfügungsantrag erstellen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konk... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Gebrauchsmusterrecht ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/kaltstart-triage/SKILL.md) | Für Allgemein: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: gebrauchsmusterrecht. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/kaltstart-triage/SKILL.md) |
| [`rechtsbestand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/rechtsbestand-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Rechtsbestand: Recherche, Neuheit, erfinderischen Schritt, Offenbarung, Erweiterung und Löschungsangriff dokumentieren. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten Auftrag... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/rechtsbestand-bearbeiten/SKILL.md) |
| [`schutzbereich-und-verletzung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzbereich-und-verletzung-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Schutzbereich und Verletzung: Anspruch, Beschreibung, Zeichnungen, angegriffene Ausführung, Ausnahmen und Einreden vergleichen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzbereich-und-verletzung-bearbeiten/SKILL.md) |
| [`schutzgegenstand-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzgegenstand-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Schutzgegenstand: technische Lehre, zulässiger Sachanspruch, ausgeschlossene Verfahren und klare Anspruchsmerkmale bestimmen. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach dem konkreten Au... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzgegenstand-bearbeiten/SKILL.md) |
| [`schutzweg-und-frist-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzweg-und-frist-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Schutzweg und Frist: Eigenanmeldung oder Abzweigung, Priorität, Erledigung der Patentanmeldung, Schonfrist und maximale Schutzdauer sichern. Vollständige Fachanweisungen und lokale Vorlagen werden gezielt nach d... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/schutzweg-und-frist-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Für Gebrauchsmusterrecht: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. Vollständige Fachanweisungen und lokale Vorlagen werden... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=gebrauchsmusterrecht/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
