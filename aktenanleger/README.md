# Aktenanleger

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Bereitet Aktenanlagen in Anwaltskanzlei, Anwaltsnotariat und Nurnotariat vor. Ordnet Eingangspost, Beteiligte, Auftrag, Fristen, Vorbefassung und getrennte Zugriffsrechte zu.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`aktenanleger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/fachaufnahme-v445.36.10/aktenanleger.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/aktenanleger.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-werkstatt.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-werkstatt.txt) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-schnellstart.md) · [TXT herunterladen / Download TXT](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-schnellstart.txt) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/aktenanleger.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

Wählen Sie eine [Übungsakte](testakten/README.md) und laden Sie zunächst nur den Ordner `Grundakte`.

> Öffnen Sie die Grundakte zur Werklohnforderung. Ordnen Sie jede Anlage einer Person und Forderung zu. Erstellen Sie die Aktenanlage, prüfen Sie den Auftrag und halten Sie im ersten Schreiben fest, welcher Nachweis noch fehlt.

Geben Sie anschließend die Nachreichung hinzu und lassen Sie die betroffene Passage im selben Entwurf überarbeiten.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`aktenanleger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/fachaufnahme-v445.36.10/aktenanleger.zip) |
| Kompakter Prompt (Schnellstart) | Markdown / identisches TXT | [`aktenanleger-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-schnellstart.md) · [`aktenanleger-schnellstart.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-schnellstart.txt) |
| Großer Prompt (Werkstatt) | Markdown / identisches TXT | [`aktenanleger-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-werkstatt.md) · [`aktenanleger-werkstatt.txt`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/aktenanleger-werkstatt.txt) |
| Zugeordnete Testakten | PDF / ZIP | [Fallauswahl und Akten-Downloads](testakten/README.md) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Eine Mail mit vier Anlagen kommt kurz vor Büroschluss. Wer hat das Büro womit beauftragt, zu welcher Sache gehören die Anlagen und wer muss heute handeln? Der Aktenanleger bereitet eine **anwaltliche Handakte, einen notariellen Vorgang oder eine interne Verwaltungsakte** vor. Im Anwaltsnotariat klärt er zuerst die Rolle und hält die Zugriffe getrennt.

## Mit einem Eingang anfangen

Geben Sie die E-Mail samt Anhängen, Umschlag oder Zustellnachweis, den bekannten Auftrag und gegebenenfalls das bisherige Zeichen. Der Hauptskill **Akte anlegen** liefert den Aktenstamm, eine belegte Rollenübersicht, die Fristenvorlage und das passende erste Schreiben. Zu jedem offenen Punkt gehören eine verantwortliche Person und der nächste Schritt. In der Kanzlei bleiben anfängliche Anfrage, angenommener Prüfauftrag und Prozessauftrag getrennt erkennbar. Im Notariat liegt die Amtsentscheidung bei der Urkundsperson.

**Beispiel für den ersten Auftrag**

> Legen Sie diesen Eingang für die heutige Übergabe an. Was ist schon belegt, wer darf für wen sprechen und welcher Termin könnte zuerst ablaufen? Formulieren Sie die eine Rückfrage, deren Antwort den nächsten Arbeitsschritt ändert.

## Akte für die lokale Weiterarbeit

Mit Python kann das mitgelieferte [Werkzeug für den lokalen Export](werkzeuge/akte_anlegen.py) aus freigegebenen Eingangsdateien und einem Aktenstamm eine ZIP-Akte bilden. Die [Musterdatei für den Aktenstamm](werkzeuge/aktenstamm-muster.json) zeigt die benötigten Angaben. Im entpackten Plugin: `python3 werkzeuge/akte_anlegen.py --stamm stamm.json --eingang eingang --ausgabe neue-akte.zip`. Der Export dient der Übergabe. Das ZIP ist unverschlüsselt. Speichern Sie es in einem zugriffsbeschränkten lokalen Ziel. Der Ordnername „Geschützter Prüfeingang“ bezeichnet den Inhalt. Berechtigungen im Dokumentenmanagementsystem werden dort gesondert gesetzt. Er bestätigt weder Eintragungen in Kanzleisoftware, Fristenkalender oder Urkundenverzeichnis noch eine tatsächliche Mandatsannahme. Hinweise zu Rollenwerten und Stammdaten stehen im Hauptskill.

## Werkstatt und Übungsakten

[Fünf Übungsfälle mit Eingangspost, Nachreichungen und bearbeitbaren Vorlagen](testakten/README.md) führen durch eine Werklohnforderung, einen Förderbescheid, eine mögliche Vorbefassung, eine Vollmachtsausfertigung und einen Archivumzug. Beginnen Sie mit der Grundakte und geben Sie nach dem ersten Aktenvermerk nur die Nachreichungen dazu. So wird sichtbar, wie sich Empfänger, Frist, Bearbeitungsrolle oder Forderungsstand durch einen einzelnen Beleg ändern.

[Rechtsquellen für die Aktenanlage](references/aktenanlage-quellen.md)


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`amt-oder-mandat-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/amt-oder-mandat-klaeren/SKILL.md), [`eingang-und-fristen-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/eingang-und-fristen-sichern/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`akte-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/akte-anlegen/SKILL.md), [`notarielle-akte-zuordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/notarielle-akte-zuordnen/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`beteiligte-und-vertretung-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/beteiligte-und-vertretung-erfassen/SKILL.md), [`forderungsvorgang-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/forderungsvorgang-anlegen/SKILL.md), [`kollision-und-vorbefassung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/kollision-und-vorbefassung-pruefen/SKILL.md), [`verwaltungsvorgang-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/verwaltungsvorgang-anlegen/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`akte-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/akte-anlegen/SKILL.md) | Legt den Eingang für Anwaltskanzlei, Anwaltsnotariat oder Nurnotariat mit Aktenstamm, Belegen, Fristen und Übergabe an. Klärt Rollen und Befugnisse und führt die Akte nach einer Nachreichung fort. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/akte-anlegen/SKILL.md) |
| [`amt-oder-mandat-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/amt-oder-mandat-klaeren/SKILL.md) | Kläre am konkreten Auftrag, ob das Büro eine Partei vertritt, ein neutrales Amtsgeschäft bearbeitet oder den eigenen Betrieb verwaltet. Ergibt einen begründeten Rollenvermerk und die passende Eingangsantwort. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/amt-oder-mandat-klaeren/SKILL.md) |
| [`beteiligte-und-vertretung-erfassen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/beteiligte-und-vertretung-erfassen/SKILL.md) | Ordnet Personen, Unternehmen, Vertreter und Empfänger aus Eingangspost und Nachweisen. Liefert ein belastbares Kurzrubrum samt noch offenen Befugnissen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/beteiligte-und-vertretung-erfassen/SKILL.md) |
| [`eingang-und-fristen-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/eingang-und-fristen-sichern/SKILL.md) | Rekonstruiert den fristauslösenden Eingang und trennt gesetzliche Frist, Zahlungsziel, Wiedervorlage und Terminwunsch. Bereitet die nachprüfbare Gegenkontrolle vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/eingang-und-fristen-sichern/SKILL.md) |
| [`forderungsvorgang-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/forderungsvorgang-anlegen/SKILL.md) | Erfasst Anspruchsinhaber, Schuldner, Einwendungen und Zahlungseingänge belegbezogen. Erstellt ein Forderungsblatt und eine Mandantenrückfrage für die Entscheidung über weitere Schritte. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/forderungsvorgang-anlegen/SKILL.md) |
| [`kollision-und-vorbefassung-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/kollision-und-vorbefassung-pruefen/SKILL.md) | Vergleicht frühere Aufträge mit dem neuen Gegenstand. Liefert einen zugriffsbeschränkten Prüfeintrag und eine für den richtigen Empfänger geeignete Antwort. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/kollision-und-vorbefassung-pruefen/SKILL.md) |
| [`notarielle-akte-zuordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/notarielle-akte-zuordnen/SKILL.md) | Ordnet das Ersuchen einer konkreten Amtsstelle, Alturkunde, Nebenakte oder Generalakte zu. Prüft Berechtigung und bereitet die neutrale Antwort und den Arbeitsvermerk vor. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/notarielle-akte-zuordnen/SKILL.md) |
| [`verwaltungsvorgang-anlegen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/verwaltungsvorgang-anlegen/SKILL.md) | Unterscheidet ein Verwaltungsmandat mit Bescheid vom internen Kanzlei- oder Amtsverwaltungsvorgang. Ordnet Zuständigkeit, Unterlagen, Frist und konkrete Übergabe zu. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=aktenanleger/skills/verwaltungsvorgang-anlegen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
