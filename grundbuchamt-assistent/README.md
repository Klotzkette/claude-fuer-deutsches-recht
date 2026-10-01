<!-- decimal-headings -->

<!-- decimal-anchor --> <a id="grundbuchamt-assistent"></a>

# 1. Grundbuchamt-Assistent

<!-- BEGIN direkt-loslegen (autogen) -->
<!-- decimal-anchor --> <a id="was-ist-das-hier"></a>

## 1.1. Was ist das hier?

Grundbuchvorgänge von Einsicht und Urkundennachweis über Erbberichtigung, Rang und Briefaufgebot bis zur Zwischenverfügung und zum dokumentierten Vollzug. Zehn Fachskills und ein Hauptproblem-Skill mit klaren Notar- und Zugriffsgrenzen.

Dieses Plugin gehört zum Marketplace mit 268 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

<!-- decimal-anchor --> <a id="welche-datei-wofür--which-file-should-i-use"></a>

## 1.2. Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`grundbuchamt-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-assistent.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/grundbuchamt-assistent.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-schnellstart.txt) |
| Schwerpunkt-Prompt | Eigenständiger, eng abgegrenzter Mandatsauftrag bis 7500 Zeichen. Der zugehörige Fachskill ist auch im Plugin vorhanden. | Standalone workflow for one demanding practice problem, up to 7500 characters. Its corresponding skill is also part of the plugin. | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-hauptproblem.md" download>MD herunterladen / Download MD</a> · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-hauptproblem.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Alle elf Skills sind unmittelbar enthalten: zehn Fachskills und der Hauptproblem-Skill. Werkstatt, Mini und Hauptproblem-Prompt sind getrennte eigenständige Downloads. Beim Einzel-Download eines Skills müssen die verlinkten Referenzen zusätzlich verfügbar sein.

All eleven skills are directly included: ten task workflows and one main problem workflow. Workshop, mini and focus prompts are separate standalone downloads. A downloaded individual skill also needs its linked references.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/grundbuchamt-assistent.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

<!-- decimal-anchor --> <a id="in-30-sekunden-starten"></a>

## 1.3. In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/grundbuchamt-assistent.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Grundbuchamt-Assistent:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

<!-- decimal-anchor --> <a id="downloads"></a>

## 1.4. Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`grundbuchamt-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-assistent.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`grundbuchamt-assistent-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-schnellstart.md) · [`grundbuchamt-assistent-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`grundbuchamt-assistent-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-werkstatt.md) · [`grundbuchamt-assistent-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-werkstatt.txt) |
| Schwerpunkt-Prompt (Hauptproblem) | Markdown / identisches TXT | <a href="https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-hauptproblem.md" download>grundbuchamt-assistent-hauptproblem.md</a> · [`grundbuchamt-assistent-hauptproblem.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-hauptproblem.txt) |
| Zugeordnete Testakten | PDF / ZIP | [3 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 268 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

<!-- decimal-anchor --> <a id="zugeordnete-testakten"></a>

## 1.5. Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Die Erben im Hinterhaus](../testakten/grundbuchamt-erben-im-hinterhaus/README.md) | [Gesamt-PDF](../testakten/grundbuchamt-erben-im-hinterhaus/gesamt-pdf/grundbuchamt-erben-im-hinterhaus_gesamt.pdf) | [`testakte-grundbuchamt-erben-im-hinterhaus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-erben-im-hinterhaus.zip) | [`testakte-grundbuchamt-erben-im-hinterhaus-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-erben-im-hinterhaus-einzelpdfs.zip) |
| [Der Brief hinter dem Kopierer](../testakten/grundbuchamt-kopiererbrief/README.md) | [Gesamt-PDF](../testakten/grundbuchamt-kopiererbrief/gesamt-pdf/grundbuchamt-kopiererbrief_gesamt.pdf) | [`testakte-grundbuchamt-kopiererbrief.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-kopiererbrief.zip) | [`testakte-grundbuchamt-kopiererbrief-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-kopiererbrief-einzelpdfs.zip) |
| [Rangtausch am Kanal](../testakten/grundbuchamt-rangtausch-am-kanal/README.md) | [Gesamt-PDF](../testakten/grundbuchamt-rangtausch-am-kanal/gesamt-pdf/grundbuchamt-rangtausch-am-kanal_gesamt.pdf) | [`testakte-grundbuchamt-rangtausch-am-kanal.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-rangtausch-am-kanal.zip) | [`testakte-grundbuchamt-rangtausch-am-kanal-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-grundbuchamt-rangtausch-am-kanal-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Elf Skills führen von Einsicht, Urkunden- und Vertretungsprüfung über Erbberichtigung, Eigentumsvollzug und Rangfragen bis zum Briefaufgebot, Wiederfund und Abschluss. Zehn Fachskills ergänzen den elften Hauptproblem-Skill.

Werkstatt zum Bearbeiten und Lesen: [Word](assets/grundbuchamt-assistent-werkstatt.docx) · [PDF](assets/grundbuchamt-assistent-werkstatt.pdf).

<!-- decimal-anchor --> <a id="direkt-beginnen"></a>

## 1.6. Direkt beginnen

Starten Sie mit `grundbuchvorgang-zum-ergebnis-fuehren`. Beispiel: „Der Ersatzbrief liegt bei der Bank. Heute ist der alte Grundschuldbrief hinter dem Kopierer aufgetaucht. Lesen Sie die Akte und erstellen Sie die nötigen Schreiben.“ Vorhandene Angaben werden weiterverwendet; nur entscheidende Lücken werden erfragt.

- [Großer Werkstatt-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-werkstatt.md)
- [Mini-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-schnellstart.md)
- [Hauptproblem-Prompt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/grundbuchamt-assistent-hauptproblem.md)
- [Amtliche Rechtsprechungsanker mit Grenzen](references/rechtsprechung.md)
- [Normen und Verfahrenswege](references/normen-und-verfahren.md)

<!-- decimal-anchor --> <a id="rollen-zugriff-und-freigabe"></a>

## 1.7. Rollen, Zugriff und Freigabe

Grundbucheinsicht setzt den passenden gesetzlichen Zugang voraus; eine freie Eigentümer-Personensuche ist nicht vorgesehen. Bei einer notariellen Handlung fragt der Workflow ausdrücklich nach Notareigenschaft, Zugang und Befugnis. Er unterscheidet notarielle Einreichungs- und Prüfpflichten von eigener Einsicht, Nachweisbeschaffung und zulässiger Antragstellung.

**Vor einer externen Handlung wird gewarnt und die konkrete Fassung vorgelegt:** Empfänger, Antrag, Anlagen, Kosten und rechtliche Wirkung müssen feststehen. Einreichung, Rücknahme, kostenpflichtige Bestellung und Originalweitergabe brauchen die konkrete Freigabe. Der Agent kann weder beurkunden noch beglaubigen und behauptet ohne geeignetes Werkzeug keinen amtlichen Zugriff. Persönliche Signatur und MFA bleiben bei der berechtigten Person.

<!-- decimal-anchor --> <a id="die-elf-skills"></a>

## 1.8. Die elf Skills

| Nr. | Skill | Arbeitsprodukt |
| --- | --- | --- |
| 1 | [Grundbucheinsicht gezielt begründen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbucheinsicht-begruenden/SKILL.md) | Einsichtsbegehren, berechtigtes Interesse, Umfang und zulässigen Abrufweg bis zum fertigen Antrag bearbeiten. |
| 2 | [Grundbuch und Bezugsurkunden präzise lesen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuch-und-bezugsurkunden-lesen/SKILL.md) | Bestandsverzeichnis, Eigentümer, Belastungen, Rang und Urkundenverweise in eine belastbare Bestandsaufnahme überführen. |
| 3 | [Antrag, Bewilligung und Form auseinanderhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchantrag-und-form-pruefen/SKILL.md) | Antragsberechtigung, Betroffenenbewilligung, materielle Erklärung und Nachweisform zu einem vollziehbaren Paket ordnen. |
| 4 | [Vertretung und Urkundenkette prüfen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vertretung-und-urkundenkette-pruefen/SKILL.md) | Vollmacht, Organvertretung, Nachfolge und Identität mit den für den Vollzug erforderlichen Nachweisen abgleichen. |
| 5 | [Erbfolge und Grundbuchberichtigung bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/erbfolge-und-grundbuchberichtigung/SKILL.md) | Erbnachweise, nicht benannte Abkömmlinge, Nacherbfolge und Berichtigung bis zum Antrag oder Nachforderungsschreiben führen. |
| 6 | [Eigentum, Vormerkung und Vollzug koordinieren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/eigentum-vormerkung-und-vollzug/SKILL.md) | Eigentumsumschreibung, Vormerkung, Genehmigungen und Fälligkeitsnachweise in der vorgesehenen Reihenfolge koordinieren. |
| 7 | [Grundschuld, Rang und Löschung abstimmen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuld-rang-und-loeschung/SKILL.md) | Brief- und Buchgrundschuld, Abtretung, Rangänderung, Rückgewähr und Löschungsunterlagen fallbezogen prüfen. |
| 8 | [Briefaufgebot und Wiederfund sicher bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuldbrief-aufgebot-und-wiederfund/SKILL.md) | Verlorenen Grundschuldbrief, Aufgebot, Ersatzbrief und späteren Wiederfund vom Belegabgleich bis zur Kommunikation bearbeiten. |
| 9 | [Zwischenverfügung und Rechtsbehelf beantworten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/zwischenverfuegung-und-beschwerde/SKILL.md) | Hindernis, Nachweis, Frist, Rang und statthaften Rechtsbehelf auseinanderhalten und eine begründete Antwort erstellen. |
| 10 | [Vollzug, Kosten und Zugriff nachhalten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vollzug-kosten-und-zugriff-dokumentieren/SKILL.md) | Freigegebene Grundbuchvorgänge, Übermittlungsnachweise, Kosten, Briefverwahrung und Abschluss bis zum verifizierten Endstand verfolgen. |
| 11 | [Hauptproblem-Skill](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchvorgang-zum-ergebnis-fuehren/SKILL.md) | Führt den Gesamtvorgang mit gezielten Fragen bis zum fertigen Dokument. |

<!-- decimal-anchor --> <a id="drei-testakten"></a>

## 1.9. Drei Testakten

Die Akten sind bewusst widersprüchliche Arbeitsunterlagen ohne Musterlösung. Personen, Grundstücke, Aktenzeichen der Fallakten und Kontakte sind fiktiv; die Rechtsprechungsanker im Plugin sind reale, überprüfte Quellen.

- [Der Brief hinter dem Kopierer](../testakten/grundbuchamt-kopiererbrief/README.md): 25 Unterlagen: Verlustsuche, Bankermächtigung, Aufgebot, Beschluss, Ersatzbrief, Wiederfund und Finanzierung.
- [Die Erben im Hinterhaus](../testakten/grundbuchamt-erben-im-hinterhaus/README.md): 27 Unterlagen: öffentliches Testament, Personenstand, Familienchat, alte Vollmacht, konkrete Zweifel und Dachfinanzierung.
- [Rangtausch am Kanal](../testakten/grundbuchamt-rangtausch-am-kanal/README.md): 24 Unterlagen: Banknachfolge, unvollständige Abtretung, Briefnummernkonflikt, Rangvorbehalt und echte Wegerechtsfrage.

<!-- decimal-anchor --> <a id="quellenstand"></a>

## 1.10. Quellenstand

Stand 01.10.2026. Zwei konkrete Entscheidungen aus 2026 unterscheiden gewöhnliche Grundbucheinsicht und Versteigerungsakte. Drei weitere amtlich geprüfte Anker betreffen Erbnachweis, Verfahrensstandschaft und den wiedergefundenen kraftlosen Brief. [Dokumentierter Quellenbericht](../quality/source-audits/registerwerkstaetten-2026-10-01/grundbuchamt.md). Regionale Vollzugsvorgaben und neue Folgeentscheidungen sind vor der tatsächlichen Verwendung erneut zu prüfen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

<!-- decimal-anchor --> <a id="orientierung-nach-arbeitslogik"></a>

## 1.11. Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und Einsicht | [`grundbuchvorgang-zum-ergebnis-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchvorgang-zum-ergebnis-fuehren/SKILL.md), [`grundbucheinsicht-begruenden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbucheinsicht-begruenden/SKILL.md), [`grundbuch-und-bezugsurkunden-lesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuch-und-bezugsurkunden-lesen/SKILL.md) |
| 2. Nachweise und Erwerb | [`grundbuchantrag-und-form-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchantrag-und-form-pruefen/SKILL.md), [`vertretung-und-urkundenkette-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vertretung-und-urkundenkette-pruefen/SKILL.md), [`eigentum-vormerkung-und-vollzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/eigentum-vormerkung-und-vollzug/SKILL.md), [`erbfolge-und-grundbuchberichtigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/erbfolge-und-grundbuchberichtigung/SKILL.md) |
| 3. Grundpfandrechte und Brief | [`grundschuld-rang-und-loeschung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuld-rang-und-loeschung/SKILL.md), [`grundschuldbrief-aufgebot-und-wiederfund`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuldbrief-aufgebot-und-wiederfund/SKILL.md) |
| 4. Verfahren und Vollzug | [`zwischenverfuegung-und-beschwerde`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/zwischenverfuegung-und-beschwerde/SKILL.md), [`vollzug-kosten-und-zugriff-dokumentieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vollzug-kosten-und-zugriff-dokumentieren/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

<!-- decimal-anchor --> <a id="alle-skills-im-überblick"></a>

## 1.12. Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`eigentum-vormerkung-und-vollzug`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/eigentum-vormerkung-und-vollzug/SKILL.md) | Eigentumsumschreibung, Vormerkung, Genehmigungen und Fälligkeitsnachweise in der vorgesehenen Reihenfolge koordinieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/eigentum-vormerkung-und-vollzug/SKILL.md) |
| [`erbfolge-und-grundbuchberichtigung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/erbfolge-und-grundbuchberichtigung/SKILL.md) | Erbnachweise, nicht benannte Abkömmlinge, Nacherbfolge und Berichtigung bis zum Antrag oder Nachforderungsschreiben führen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/erbfolge-und-grundbuchberichtigung/SKILL.md) |
| [`grundbuch-und-bezugsurkunden-lesen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuch-und-bezugsurkunden-lesen/SKILL.md) | Bestandsverzeichnis, Eigentümer, Belastungen, Rang und Urkundenverweise in eine belastbare Bestandsaufnahme überführen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuch-und-bezugsurkunden-lesen/SKILL.md) |
| [`grundbuchantrag-und-form-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchantrag-und-form-pruefen/SKILL.md) | Antragsberechtigung, Betroffenenbewilligung, materielle Erklärung und Nachweisform zu einem vollziehbaren Paket ordnen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchantrag-und-form-pruefen/SKILL.md) |
| [`grundbucheinsicht-begruenden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbucheinsicht-begruenden/SKILL.md) | Einsichtsbegehren, berechtigtes Interesse, Umfang und zulässigen Abrufweg bis zum fertigen Antrag bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbucheinsicht-begruenden/SKILL.md) |
| [`grundbuchvorgang-zum-ergebnis-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchvorgang-zum-ergebnis-fuehren/SKILL.md) | Hauptproblem-Skill für Grundbuchvorgänge von der vorhandenen Akte über Einsicht, Form, Berechtigung und Rückfragen bis zum fertigen Schreiben und überprüften Vollzugsstand. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundbuchvorgang-zum-ergebnis-fuehren/SKILL.md) |
| [`grundschuld-rang-und-loeschung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuld-rang-und-loeschung/SKILL.md) | Brief- und Buchgrundschuld, Abtretung, Rangänderung, Rückgewähr und Löschungsunterlagen fallbezogen prüfen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuld-rang-und-loeschung/SKILL.md) |
| [`grundschuldbrief-aufgebot-und-wiederfund`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuldbrief-aufgebot-und-wiederfund/SKILL.md) | Verlorenen Grundschuldbrief, Aufgebot, Ersatzbrief und späteren Wiederfund vom Belegabgleich bis zur Kommunikation bearbeiten. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/grundschuldbrief-aufgebot-und-wiederfund/SKILL.md) |
| [`vertretung-und-urkundenkette-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vertretung-und-urkundenkette-pruefen/SKILL.md) | Vollmacht, Organvertretung, Nachfolge und Identität mit den für den Vollzug erforderlichen Nachweisen abgleichen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vertretung-und-urkundenkette-pruefen/SKILL.md) |
| [`vollzug-kosten-und-zugriff-dokumentieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vollzug-kosten-und-zugriff-dokumentieren/SKILL.md) | Freigegebene Grundbuchvorgänge, Übermittlungsnachweise, Kosten, Briefverwahrung und Abschluss bis zum verifizierten Endstand verfolgen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/vollzug-kosten-und-zugriff-dokumentieren/SKILL.md) |
| [`zwischenverfuegung-und-beschwerde`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/zwischenverfuegung-und-beschwerde/SKILL.md) | Hindernis, Nachweis, Frist, Rang und statthaften Rechtsbehelf auseinanderhalten und eine begründete Antwort erstellen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=grundbuchamt-assistent/skills/zwischenverfuegung-und-beschwerde/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
