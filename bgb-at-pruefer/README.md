# BGB AT Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, Anfechtung, Stellvertretung, Fristen, Verjährung und Routing für digitale Elemente, Update- und Reparaturrecht.

Dieses Plugin gehört zum Marketplace mit 311 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`bgb-at-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/bgb-at-pruefer.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/bgb-at-pruefer.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/bgb-at-pruefer-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/bgb-at-pruefer-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/bgb-at-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/bgb-at-pruefer.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für BGB AT Prüfer:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`bgb-at-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/qualitaetsrunde-v445.36.0/bgb-at-pruefer.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`bgb-at-pruefer-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/bgb-at-pruefer-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`bgb-at-pruefer-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/bgb-at-pruefer-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [6 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 311 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Anfechtung / Irrtum — Restaurant-Kette Pohlmann-Ofenkäss, Erbenstraße Leipzig](../testakten/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig/README.md) | [Gesamt-PDF](../testakten/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig/gesamt-pdf/anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig_gesamt.pdf) | [`testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig.zip) | [`testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-anfechtung-irrtum-restaurant-kette-pohlmann-erbenstrasse-leipzig-einzelpdfs.zip) |
| [Akte BGB AT: Altfränkische Werkstatt](../testakten/bgb-at-altfraenkische-werkstatt/README.md) | [Gesamt-PDF](../testakten/bgb-at-altfraenkische-werkstatt/gesamt-pdf/bgb-at-altfraenkische-werkstatt_gesamt.pdf) | [`testakte-bgb-at-altfraenkische-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-at-altfraenkische-werkstatt.zip) | [`testakte-bgb-at-altfraenkische-werkstatt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-at-altfraenkische-werkstatt-einzelpdfs.zip) |
| [BGB BT — Holzofen, Lieferkette, Bürgschaft, GoA und Brandschaden](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/README.md) | [Gesamt-PDF](../testakten/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt/gesamt-pdf/bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt_gesamt.pdf) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt.zip) | [`testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-bt-holzofen-lieferkette-buergschaft-goa-delikt-einzelpdfs.zip) |
| [BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/README.md) | [Gesamt-PDF](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln-einzelpdfs.zip) |
| [BGB: Gartenumbau, Zusatzauftrag und Bürgschaft in Kassel](../testakten/bgb-buergschaft-gartenbau-kassel/README.md) | [Gesamt-PDF](../testakten/bgb-buergschaft-gartenbau-kassel/gesamt-pdf/bgb-buergschaft-gartenbau-kassel_gesamt.pdf) | [`testakte-bgb-buergschaft-gartenbau-kassel.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-buergschaft-gartenbau-kassel.zip) | [`testakte-bgb-buergschaft-gartenbau-kassel-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-buergschaft-gartenbau-kassel-einzelpdfs.zip) |
| [BGB: Hochzeitslocation, Schwesterbestellung und abgesagte Feier in Dresden](../testakten/bgb-vollmacht-hochzeitslocation-dresden/README.md) | [Gesamt-PDF](../testakten/bgb-vollmacht-hochzeitslocation-dresden/gesamt-pdf/bgb-vollmacht-hochzeitslocation-dresden_gesamt.pdf) | [`testakte-bgb-vollmacht-hochzeitslocation-dresden.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-bgb-vollmacht-hochzeitslocation-dresden.zip) | [`testakte-bgb-vollmacht-hochzeitslocation-dresden-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-bgb-vollmacht-hochzeitslocation-dresden-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Großes Prüfplugin zum BGB Allgemeiner Teil. Es führt durch Vertragsschluss, Willenserklärungen, Zugang, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung. Der Formteil ist mit qES, beA, § 130e ZPO und § 46h ArbGG verschaltet. Neu verschaltet sind digitale Elemente, Updatehinweise, App-/Portalzugang, Reparaturverlangen und Right-to-Repair-Fragen als allgemeinzivilrechtlicher Router in BGB-BT, AGB-Recht und Produktrecht. Ziel ist ein schöner, schneller und trotzdem präziser Workflow für Klausur, Ausbildung, Kanzleivermerk und Mandatsarbeit.

Experimentelles Werkzeug. Keine Rechtsberatung, keine Gewähr. Gesetzestext und Rechtsprechung müssen im konkreten Fall geprüft werden. Literatur- oder Kommentarstellen dürfen nur genutzt werden, wenn sie vom Nutzer bereitgestellt wurden oder über eine lizenzierte Quelle live verifiziert sind.

## Schnellstart

/plugin install bgb-at-prüfer@claude-für-deutsches-recht

Starte mit dem Skill [Kaltstart-Triage](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/kaltstart-triage/SKILL.md). Lies zuerst Erklärungen und Auftrag. Bei einer klaren Zugangs-, Form- oder Vollmachtsfrage direkt zur Prüfung und zum bestellten Text arbeiten; keine vorgeschaltete Themenkarte verlangen. Nur entscheidende Lücken klären und Antworten in den bestehenden Entwurf einarbeiten.

## Was das Plugin besonders gut kann

- aus einem unsortierten BGB-AT-Sachverhalt einen Anspruchsbaum bauen
- Angebot, Annahme, Zugang, Fristen und digitale Erklärungsketten auseinanderziehen
- Minderjährigenfälle mit §§ 104-113 BGB sauber prüfen
- Anfechtung mit Auslegung, Frist, Gegner und Folgen prüfen
- Stellvertretung, Vollmacht, Rechtsschein und § 181 BGB trennen
- Form, Nichtigkeit, Gesetzesverbot, Sittenwidrigkeit und Bedingung als Wirksamkeitsfragen einordnen
- elektronische Form, qES-Zugang, beA-Einreichung und prozessuale Formfiktion auseinanderhalten
- Waren mit digitalen Elementen, Updatehinweise, AGB-Abweichungen und Reparaturverlangen in die richtigen Spezial-Skills routen
- aus dem Ergebnis Gutachten, Mandatsmemo, Schriftsatzbaustein, Rückfragenbrief oder Trainingsfall machen

## Empfohlener Workflow

1. Fallfrage festnageln: Wer will was von wem, und auf welcher Anspruchsebene liegt das Problem?
2. Erklärungskette bauen: Jede Erklärung mit Datum, Kanal, Absender, Empfänger, Zugang und Inhalt erfassen.
3. BGB-AT-Themenkarte erstellen: Geschäftsfähigkeit, Willenserklärung, Vertragsschluss, Auslegung, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingung, Fristen.
4. Nur den zur offenen Rechtsfrage passenden Spezial-Skill heranziehen und bekannte Angaben weiterverwenden.
5. Das beauftragte Arbeitsprodukt fertigstellen: Klausurlösung, Memo, Schriftsatzbaustein oder Fristenvermerk. Ausgabeform nur bei offenem Auftrag klären; Training nicht ungefragt anschließen.

## Skill-Auswahl

Nutze für die Auswahl die automatisch gepflegte Übersicht unten. Die Skills sind als eigenständige Prüfmodule angelegt und führen jeweils mit Normankern, Prüfprogramm und Ausgabeformat durch die passende BGB-AT-Frage.

## Quellen- und Aktualitätsanker

- Aktueller BGB-Gesetzestext: https://www.gesetze-im-internet.de/bgb/
- Interne Struktur: [references/bgb-at-pruefprogramm.md](./references/bgb-at-pruefprogramm.md)
- Rechtsstandsregel: [references/rechtsstand-und-quellen.md](./references/rechtsstand-und-quellen.md)

## Gute Begleiter

- [methodenlehre-buergerliches-recht](../methodenlehre-buergerliches-recht) für Auslegung, Gutachtenstil und Anspruchsdenken.
- [subsumtions-prüfer](../subsumtions-pruefer) für generische Tatbestandsarbeit.
- [schriftform-und-textform-bgb](../schriftform-und-textform-bgb) für tiefe Form-, Textform- und Zugangskonstellationen.
- [bereicherungs-und-anfechtungsrecht-pruefer](../bereicherungs-und-anfechtungsrecht-pruefer) für Rückabwicklung nach unwirksamem Vertrag.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **9 auswählbare Skills**. Die **96 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/juristischer-argumentationskern/SKILL.md), [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/kaltstart-triage/SKILL.md) |
| 2. Rechtsgeschäft und Wirksamkeit | [`rechtsgeschaeft-und-wirksamkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/rechtsgeschaeft-und-wirksamkeit-bearbeiten/SKILL.md) |
| 3. Vertrag und Leistungsstörung | [`vertrag-und-leistungsstoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/vertrag-und-leistungsstoerung-bearbeiten/SKILL.md) |
| 4. Bereicherung und Rückabwicklung | [`bereicherung-und-rueckabwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/bereicherung-und-rueckabwicklung-bearbeiten/SKILL.md) |
| 5. Delikt und gesetzliche Ansprüche | [`delikt-und-gesetzliche-ansprueche-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/delikt-und-gesetzliche-ansprueche-bearbeiten/SKILL.md) |
| 6. Sachen Sicherung und Forderungswechsel | [`sachen-sicherung-und-forderungswechsel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/sachen-sicherung-und-forderungswechsel-bearbeiten/SKILL.md) |
| 7. Einwendungen Fristen und Durchsetzung | [`einwendungen-fristen-und-durchsetzung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/einwendungen-fristen-und-durchsetzung-bearbeiten/SKILL.md) |
| 8. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 9 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 9 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | BGB AT Prüfer: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`bereicherung-und-rueckabwicklung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/bereicherung-und-rueckabwicklung-bearbeiten/SKILL.md) | BGB AT Prüfer: Bereicherung und Rückabwicklung: Entreicherung, Leistungsbeziehung, Eingriff und Rückabwicklung nach dem richtigen Anspruch prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/bereicherung-und-rueckabwicklung-bearbeiten/SKILL.md) |
| [`delikt-und-gesetzliche-ansprueche-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/delikt-und-gesetzliche-ansprueche-bearbeiten/SKILL.md) | BGB AT Prüfer: Delikt und gesetzliche Ansprüche: Delikt, Geschäftsführung ohne Auftrag und weitere gesetzliche Ansprüche mit Zurechnung und Schaden prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/delikt-und-gesetzliche-ansprueche-bearbeiten/SKILL.md) |
| [`einwendungen-fristen-und-durchsetzung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/einwendungen-fristen-und-durchsetzung-bearbeiten/SKILL.md) | BGB AT Prüfer: Einwendungen Fristen und Durchsetzung: Einwendungen, Einreden, Fristen, Beweislast und Durchsetzung bis zum konkreten Arbeitsprodukt verbinden. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/einwendungen-fristen-und-durchsetzung-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in BGB At Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/kaltstart-triage/SKILL.md) | Für Kaltstart Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: BGB AT Prüfer. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/kaltstart-triage/SKILL.md) |
| [`rechtsgeschaeft-und-wirksamkeit-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/rechtsgeschaeft-und-wirksamkeit-bearbeiten/SKILL.md) | BGB AT Prüfer: Rechtsgeschäft und Wirksamkeit: Erklärung, Geschäftsfähigkeit, Vertretung, Form, Irrtum und Wirksamkeit anhand des Geschehens prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/rechtsgeschaeft-und-wirksamkeit-bearbeiten/SKILL.md) |
| [`sachen-sicherung-und-forderungswechsel-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/sachen-sicherung-und-forderungswechsel-bearbeiten/SKILL.md) | BGB AT Prüfer: Sachen Sicherung und Forderungswechsel: Eigentum, Besitz, Sicherung, Abtretung, Aufrechnung und Schuldwechsel anhand der Rechtsbeziehungen klären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/sachen-sicherung-und-forderungswechsel-bearbeiten/SKILL.md) |
| [`vertrag-und-leistungsstoerung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/vertrag-und-leistungsstoerung-bearbeiten/SKILL.md) | BGB AT Prüfer: Vertrag und Leistungsstörung: Vertragliche Ansprüche, Gegenleistung, Leistungsstörung, Mängel und Schadensersatz strukturiert bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=bgb-at-pruefer/skills/vertrag-und-leistungsstoerung-bearbeiten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
