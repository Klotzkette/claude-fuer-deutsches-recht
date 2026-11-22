# NDA-Abgleich

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Gleicht NDA-Entwurf der Gegenseite gegen eigenen Standard ab und setzt Haltelinien chirurgisch im Word-Änderungsmodus durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Tracked Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`nda-abgleich.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/nda-abgleich.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/nda-abgleich.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/nda-abgleich-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/nda-abgleich-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/nda-abgleich.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/nda-abgleich.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für NDA-Abgleich:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`nda-abgleich.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/nda-abgleich.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`nda-abgleich-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/nda-abgleich-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`nda-abgleich-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/nda-abgleich-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Waldkrone HealthTech GmbH - NDA, Meldekanal und Lieferantenhinweis](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/README.md) | [Gesamt-PDF](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/gesamt-pdf/hinweisgeberschutz-nda-meldekanal-waldkrone_gesamt.pdf) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone-einzelpdfs.zip) |
| [NDA-Vertragsabgleich Windsysteme Norderhof AG / Eickmann Wirtschaftspartner Pte. Ltd. — Joint Venture, GeschGehG, Exportkontrolle](../testakten/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft/README.md) | [Gesamt-PDF](../testakten/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft/gesamt-pdf/nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft_gesamt.pdf) | [`testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft.zip) | [`testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-nda-vertragsabgleich-jointventure-windsysteme-eickmann-wirtschaft-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
NDA-Verhandlungshilfe für die empfangende Seite. Vergleicht den Entwurf der Gegenseite mit dem belegten eigenen Standard und formuliert möglichst gezielte Änderungen. Der Auftrag bestimmt, ob ein Standard aus eigenen Fassungen gewonnen oder ein konkreter Gegenentwurf bearbeitet wird. Die Ampelmatrix erläutert die Verhandlungsposition, ersetzt aber nicht den bestellten Änderungstext.

Echte Word-Änderungsverfolgung wird nur zugesagt, wenn sie mit verfügbaren Werkzeugen erzeugt und geprüft werden kann. Sonst werden genaue Fundstellen und vollständige Ersatztexte geliefert, keine angebliche DOCX-Datei. Keine pauschale Neufassung fremder Absätze; notwendige Abweichungen vom engen Änderungsauftrag werden konkret benannt.

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Upload plugin` wählen und die Datei auswählen.
3. Plugin aktivieren und eine neue Aufgabe öffnen; den passenden Skill ausdrücklich auswählen.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `nda-abgleich` | NDA-Verhandlungshilfe für die empfangende Seite. Zwei Modi: (A) Standard-Destillation aus 1 bis n eigenen NDAs und frei beschreibbarer Erfahrung in einen konsolidierten Haltelinien-Standard mit Ampelmatrix ROT/GELB/G… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **10 auswählbare Skills**. Die **91 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Abschluss Parteien und Auslegung | [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| 3. Leistung Vergütung und Abwicklung | [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| 4. Geheimnis Daten und Rechte | [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| 5. Haftung Sicherheiten und Störung | [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| 6. Laufzeit Beendigung und Streit | [`laufzeit-beendigung-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) |
| 7. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abschluss-parteien-und-auslegung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) | NDA-Abgleich: Abschluss Parteien und Auslegung: Vertragspartner, Abschluss, Vollmacht, Form und maßgeblichen Inhalt anhand des Fassungsverlaufs prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/abschluss-parteien-und-auslegung-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | NDA-Abgleich: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/einstieg-routing/SKILL.md) | Für eine vorgelegte Geheimhaltungsvereinbarung: bewertet konkrete Abweichungen vom Standard und erstellt begründete, ausformulierte Änderungen mit zulässigen Verhandlungsalternativen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/einstieg-routing/SKILL.md) |
| [`geheimnis-daten-und-rechte-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) | NDA-Abgleich: Geheimnis Daten und Rechte: Geheimnisse, Daten, Nutzungsrechte und Weitergabe im tatsächlichen Geschäftsvorgang absichern. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/geheimnis-daten-und-rechte-bearbeiten/SKILL.md) |
| [`haftung-sicherheiten-und-stoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) | NDA-Abgleich: Haftung Sicherheiten und Störung: Haftung, Mängel, Sicherheit, Leistungsstörung und wirtschaftliche Risikozuordnung gestalten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/haftung-sicherheiten-und-stoerung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/juristischer-argumentationskern/SKILL.md) | NDA-Fassungen bis zur verhandlungsfähigen Änderungsfassung abgleichen. Nutzt vorhandene Falldaten, entscheidet die maßgeblichen rechtlichen Abzweigungen und verbindet passende Fachprüfungen mit einem vollständig ausgearbeiteten Ergebnis... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/juristischer-argumentationskern/SKILL.md) |
| [`laufzeit-beendigung-und-streit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) | NDA-Abgleich: Laufzeit Beendigung und Streit: Laufzeit, Kündigung, Abwicklung, Rückgabe und Streitbeilegung mit den übrigen Klauseln abstimmen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/laufzeit-beendigung-und-streit-bearbeiten/SKILL.md) |
| [`leistung-verguetung-und-abwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) | NDA-Abgleich: Leistung Vergütung und Abwicklung: Leistung, Gegenleistung, Abnahme, laufende Pflichten und Abrechnung konkret ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/leistung-verguetung-und-abwicklung-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | NDA-Abgleich: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/workflow-kaltstart-und-routing/SKILL.md) | Für einen NDA-Vergleich: identifiziert Fremdentwurf, maßgeblichen Standard, Austauschzweck und eigene Rolle; markiert fehlende Vorgaben vor dem Klauselabgleich. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=nda-abgleich/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<a id="fachliche-ki-prüfung"></a>

## 1. Fachliche KI-Prüfung

[Normen, technische Nachweise, Rechtsprechungsgrenzen und Übungsakte](references/ki-normen-und-fallpruefung.md): Prüfen Sie, welche technische Information für Kontrolle, Auskunft oder Behördenprüfung gebraucht wird. Eine Geheimhaltungsklausel muss notwendige gesetzliche Offenlegungen zulassen, ohne unnötig Modell- oder Kundendaten offenzulegen.

Aktuelle KI-Fachvertiefung: Komponentenfassung 445.35.2 im [KI-Verordnungsrelease](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/tag/ki-verordnung-v445.35.2). Ältere Sammelarchive enthalten diese Ergänzung noch nicht.
