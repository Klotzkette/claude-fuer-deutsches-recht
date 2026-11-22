# Allgemeines Notariat

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Amtsgeschäfte deutscher Notarinnen und Notare von der ersten Anfrage bis zum Vollzug. Zehn Skills für Grundstücke, Nachfolge, Vorsorge, Erbausschlagung, Vereinsregister und GmbH-Anteile.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`allgemeines-notariat.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v1.0.0/allgemeines-notariat.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/allgemeines-notariat.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-schnellstart.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/allgemeines-notariat.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

Öffnen Sie die [Notariatsakten](testakten/README.md), wählen Sie einen Fall und laden Sie zunächst nur dessen Ordner `Grundakte`. Arbeiten Sie mit dem Hauptskill `amtsgeschaeft-fuehren` oder mit dem eigenständigen Mini-Prompt.

> Prüfen Sie für die Notarin den Willen der Beteiligten und die vorliegenden Nachweise. Entwerfen Sie das Schreiben, das wir heute an die Beteiligten richten können. Nennen Sie im getrennten Vermerk die Entscheidungen, die noch das persönliche Gespräch oder einen weiteren Nachweis erfordern.

Geben Sie anschließend eine Nachreichung aus derselben Akte hinzu und lassen Sie die betroffene Passage im Entwurf anpassen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`allgemeines-notariat.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v1.0.0/allgemeines-notariat.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`allgemeines-notariat-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-schnellstart.md) · [`allgemeines-notariat-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`allgemeines-notariat-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-werkstatt.md) · [`allgemeines-notariat-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/allgemeines-notariat-werkstatt.txt) |
| Zugeordnete Testakten | PDF / ZIP | [Fallauswahl und Akten-Downloads](testakten/README.md) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Eine Familie will den Hof übergeben, eine Bank verspricht die Löschung ihrer Grundschuld oder ein Verein schickt zwei Fassungen seines Wahlprotokolls. Das Plugin unterstützt Notarinnen und Notare dabei, aus solchen Unterlagen ein Beteiligtenanschreiben, einen Urkundenentwurf und eine begründete Entscheidung für den nächsten Schritt zu erarbeiten. Ausgangspunkt sind der Wille aller Beteiligten und die Nachweise in der konkreten Akte. [§ 14 BNotO](https://www.gesetze-im-internet.de/bnoto/__14.html) · [§ 17 BeurkG](https://www.gesetze-im-internet.de/beurkg/__17.html)

## Einen Vorgang bearbeiten

Starten Sie mit dem Hauptskill [Amtsgeschäft führen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/amtsgeschaeft-fuehren/SKILL.md). Geben Sie den Auftrag und die vorhandenen Unterlagen ein. Benennen Sie das gewünschte Arbeitsergebnis, etwa ein neutrales Anschreiben an die Erschienenen, eine beurkundungsfähige Regelungsvariante oder eine Vollzugsanweisung mit noch ausstehenden Nachweisen. Beim Nachreichen eines Dokuments kann derselbe Vorgang fortgesetzt werden. Persönliche Belehrung, Wahrnehmungen im Termin und amtliche Freigaben liegen bei der Notarin oder dem Notar.

## Die Testakten im Kurs einsetzen

Die [Fallauswahl mit allen 20 Akten](testakten/README.md) enthält sieben alltägliche Amtsgeschäfte und dreizehn weitere Notariatsvorgänge. Beginnen Sie im Ordner `Grundakte`. Öffnen Sie bei den sieben Amtsgeschäften die Nachreichungen erst, wenn der erste Entwurf steht. So lässt sich zum Beispiel am Stuttgarter Wohnungskauf prüfen, welche Passage nach der Auskunft der Tiefgaragenverwaltung neu formuliert werden muss.

Für den Einstieg eignet sich dieser Auftrag: „Lesen Sie die Grundakte. Welche Angaben können wir beiden Seiten bereits bestätigen, was muss die Notarin selbst klären, und welchen Brief kann das Notariat heute verschicken? Formulieren Sie ihn.“

## Verwandte Arbeitsplätze

Die [Mitarbeiterwerkstatt](../notariat-alltag/README.md) begleitet Auftragsaufnahme, Unterlagenanforderung und Vorlage an das Notariat. Das [Berufsrecht der Notare](../berufsrecht-notare/README.md) vertieft eigenständige berufsrechtliche Fragen.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 4. Gestaltung, Strategie und Verhandlung | [`testament-und-erbvertrag-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/testament-und-erbvertrag-gestalten/SKILL.md), [`wohnungskauf-und-lastenausgleich-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/wohnungskauf-und-lastenausgleich-gestalten/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`vereinsvorstand-zum-register-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vereinsvorstand-zum-register-anmelden/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`amtsgeschaeft-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/amtsgeschaeft-fuehren/SKILL.md), [`beteiligte-und-vertretung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/beteiligte-und-vertretung-pruefen/SKILL.md), [`erbausschlagung-fuer-minderjaehrige-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/erbausschlagung-fuer-minderjaehrige-pruefen/SKILL.md), [`gmbh-anteilskauf-und-liste-vollziehen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/gmbh-anteilskauf-und-liste-vollziehen/SKILL.md), [`ueberlassung-und-wohnungsrecht-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/ueberlassung-und-wohnungsrecht-gestalten/SKILL.md), [`vollzug-und-freigaben-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vollzug-und-freigaben-steuern/SKILL.md), [`vorsorgevollmacht-beurkunden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vorsorgevollmacht-beurkunden/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`amtsgeschaeft-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/amtsgeschaeft-fuehren/SKILL.md) | Führt die persönliche notarielle Prüfung bei Grundstück, Gesellschaft, Familie, Verein und Nachlass. Erarbeitet aus dem konkreten Begehren einen neutralen Entwurf, eine begründete Amtsentscheidung und den nächsten Vollzugsschritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/amtsgeschaeft-fuehren/SKILL.md) |
| [`beteiligte-und-vertretung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/beteiligte-und-vertretung-pruefen/SKILL.md) | Klärt für den konkreten Akt Identität, Vertretungsmacht, ausländische Nachweisketten und Verfahrensform. Entwirft die erforderliche Anforderung oder Genehmigung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/beteiligte-und-vertretung-pruefen/SKILL.md) |
| [`erbausschlagung-fuer-minderjaehrige-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/erbausschlagung-fuer-minderjaehrige-pruefen/SKILL.md) | Prüft Berufungsgrund, Ausschlagungsfrist, elterliche Vertretung und familiengerichtliche Genehmigung. Erstellt Erklärung, Genehmigungsantrag oder fristbezogene Unterlagenanforderung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/erbausschlagung-fuer-minderjaehrige-pruefen/SKILL.md) |
| [`gmbh-anteilskauf-und-liste-vollziehen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/gmbh-anteilskauf-und-liste-vollziehen/SKILL.md) | Bereitet Verpflichtung, Abtretung und Zustimmungen beim GmbH-Anteilskauf vor und bestimmt den belegten Zeitpunkt für die neue Gesellschafterliste. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/gmbh-anteilskauf-und-liste-vollziehen/SKILL.md) |
| [`testament-und-erbvertrag-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/testament-und-erbvertrag-gestalten/SKILL.md) | Ermittelt den persönlichen letzten Willen, prüft Vorbindungen und entwirft für Patchworkfamilien Erbeinsetzung, Ersatz, Vermächtnis und Änderungsbefugnis. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/testament-und-erbvertrag-gestalten/SKILL.md) |
| [`ueberlassung-und-wohnungsrecht-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/ueberlassung-und-wohnungsrecht-gestalten/SKILL.md) | Ordnet Flurstücke, Gegenleistungen und Versorgung bei einer Übergabe. Entwirft Überlassungsvertrag, Wohnungsrecht, Rangregelung und erforderliche Nachforderungen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/ueberlassung-und-wohnungsrecht-gestalten/SKILL.md) |
| [`vereinsvorstand-zum-register-anmelden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vereinsvorstand-zum-register-anmelden/SKILL.md) | Prüft Satzung, Einladung, Wahl, Annahme und Vertretungsregel bei einem e. V. Erstellt Anmeldung, Belegverzeichnis und gezielte Berichtigungsanfrage. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vereinsvorstand-zum-register-anmelden/SKILL.md) |
| [`vollzug-und-freigaben-steuern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vollzug-und-freigaben-steuern/SKILL.md) | Hält nach dem Termin Rangstellen, Bedingungen, Treuhandauflagen und Registeranträge auseinander. Erstellt die nächste zulässige Vollzugshandlung oder die konkrete Nachforderung. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vollzug-und-freigaben-steuern/SKILL.md) |
| [`vorsorgevollmacht-beurkunden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vorsorgevollmacht-beurkunden/SKILL.md) | Bereitet ein persönliches, barrieregerechtes Vollmachtsgespräch vor und entwirft Umfang, Kontrollen, Ausfertigungsregeln und das geeignete Beurkundungsverfahren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/vorsorgevollmacht-beurkunden/SKILL.md) |
| [`wohnungskauf-und-lastenausgleich-gestalten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/wohnungskauf-und-lastenausgleich-gestalten/SKILL.md) | Bereitet einen Bestandswohnungskauf vom Grundbuch- und Entwurfsabgleich bis zur gesicherten Kaufpreisfälligkeit und Eigentumsumschreibung vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=allgemeines-notariat/skills/wohnungskauf-und-lastenausgleich-gestalten/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
