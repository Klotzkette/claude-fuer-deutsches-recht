# 1. Insolvenzforderungen-Checker

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Insolvenzforderungen vom Akteneingang bis zum begründeten Prüfvorschlag bearbeiten. Elf Skills verbinden Gläubigerklärung, Belege, Beträge, Rang, Sicherheiten und Termine mit Tabellenentwurf und Gläubigerbrief; keine automatische Feststellung oder Einreichung.

Dieses Plugin gehört zum Marketplace mit 308 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`insolvenzforderungen-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/insolvenzforderungen-checker.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Alle elf Skills sind unmittelbar enthalten: ein Hauptskill und zehn Fachskills. Werkstatt und Mini-Prompt sind eigenständige Downloads. Der optionale Exporthelfer und seine Referenz gehören zum Plugin-ZIP; einzelne Skill-Downloads benötigen diese Hilfsdateien zusätzlich.

All eleven skills are included directly: one main workflow and ten specialist skills. Workshop and mini prompt are standalone downloads. The optional export helper and its reference are bundled in the plugin ZIP; individual skill downloads need those files separately.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/insolvenzforderungen-checker.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

Wählen Sie `forderungen-pruefen-und-tabelle-vorbereiten`. Ohne Installation verwenden Sie den Mini-Prompt oder die ausführliche Werkstatt aus der Downloadtabelle.

> Eröffnungsbeschluss, zehn Forderungsanmeldungen und Belege liegen im Ordner. Gleiche Beträge, Verträge, Zahlungen und Sicherheiten ab. Erstelle begründete Tabellenvorschläge und die dazugehörigen Gläubigerbriefe. Frage nur nach entscheidenden fehlenden Unterlagen.

Das Paket arbeitet für die Insolvenzverwaltung. Es trennt angemeldete Beträge, interne Prüfung und gerichtliche Feststellung. Verspätete und nachrangige Anmeldungen sowie Sicherheiten erhalten eigene Prüfwege. Elektronische Exporte werden vorbereitet, aber nicht automatisch versandt. Dies ist ein Experiment und keine Rechtsberatung.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`insolvenzforderungen-checker.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`insolvenzforderungen-checker-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`insolvenzforderungen-checker-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 308 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Insolvenzforderungen Rheinsteg Handwerk Köln](../testakten/insolvenzforderungen-handwerk-koeln/README.md) | [Gesamt-PDF](../testakten/insolvenzforderungen-handwerk-koeln/gesamt-pdf/insolvenzforderungen-handwerk-koeln_gesamt.pdf) | [`testakte-insolvenzforderungen-handwerk-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-insolvenzforderungen-handwerk-koeln.zip) | [`testakte-insolvenzforderungen-handwerk-koeln-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-insolvenzforderungen-handwerk-koeln-einzelpdfs.zip) |
| [Insolvenzforderungen der Münchner Pistazien-Brezelbäckerei](../testakten/insolvenzforderungen-pistazienbrezeln-muenchen/README.md) | [Gesamt-PDF](../testakten/insolvenzforderungen-pistazienbrezeln-muenchen/gesamt-pdf/insolvenzforderungen-pistazienbrezeln-muenchen_gesamt.pdf) | [`testakte-insolvenzforderungen-pistazienbrezeln-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-insolvenzforderungen-pistazienbrezeln-muenchen.zip) | [`testakte-insolvenzforderungen-pistazienbrezeln-muenchen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-insolvenzforderungen-pistazienbrezeln-muenchen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Version 445.35.5. Elf unmittelbar enthaltene Skills für die Prüfung angemeldeter Forderungen: von der freigegebenen Akte zu einem begründeten Prüfvorschlag, einer Tabellenzeile und einem passenden Gläubigerbrief. Für die vorbereitende Arbeit in der Insolvenzverwaltung; bei einem Gläubigerauftrag wird die Perspektive ausdrücklich umgestellt.

Das kompakte Paket ergänzt [Insolvenzforderungsanmeldungsprüfung](../insolvenzforderungsanmeldungspruefung/README.md) und [Insolvenzverwaltung](../insolvenzverwaltung/README.md), ersetzt sie aber nicht. Sein Fokus ist die konkrete Forderungsprüfung bis zum Tabellenvorschlag und Gläubigerbrief; ein zusätzlicher Einstieg über die anderen Pakete ist nicht erforderlich.

## 1.1. Direkt beginnen

Starten Sie mit [forderungen-pruefen-und-tabelle-vorbereiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungen-pruefen-und-tabelle-vorbereiten/SKILL.md).

> Die Verfahrensakte und die Forderungsanmeldungen sind freigegeben. Prüfe jede Anmeldung mit ihren Belegen. Erstelle je Gläubiger einen begründeten Prüfvorschlag, einen Tabellenentwurf und einen passenden Briefentwurf. Trenne offene Nachweise, Sicherheiten, Rang und gerichtlichen Prüfstatus. Versende nichts.

Ohne Installation führen die eigenständige [Werkstatt](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-werkstatt.md) und der kompakte [Schnellstart](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-schnellstart.md) durch denselben Kernvorgang. Ist der Auftrag offen, wählen Sie gesamtes Prüflos, Einzeleingang, Korrespondenz oder Tabellenkontrolle. Bei einem klaren Auftrag beginnt die Prüfung unmittelbar.

Die [vierzehn Prüffälle und Musterausgaben](references/prueffaelle-und-musterausgaben.md) zeigen unterschiedliche Fehlerbilder vom fehlenden Lieferschein bis zum Teil-Titel, zur Absonderungsabrechnung, Arbeitnehmer-Sammelanmeldung und gemischten Vor- und Nacheröffnungsforderung. Jeder Fall endet mit Ergebnisstatus, konkreter Nachforderung und Tabellenfolge; vier vollständige Briefe können fallbezogen weiterbearbeitet werden.

## 1.2. Elf Skills

| Nummer | Skill | Aufgabe |
| --- | --- | --- |
| 1 | [forderungen-pruefen-und-tabelle-vorbereiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungen-pruefen-und-tabelle-vorbereiten/SKILL.md) | Gesamten Vorgang bis zur Freigabemappe bearbeiten |
| 2 | [anmeldung-und-glaeubiger-klaeren](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/anmeldung-und-glaeubiger-klaeren/SKILL.md) | Eingang, Berechtigung, Abtretungen und Doppelanmeldungen |
| 3 | [forderungsgrund-und-belege-abgleichen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungsgrund-und-belege-abgleichen/SKILL.md) | Anspruch und Leistungsnachweise |
| 4 | [zahlungen-zinsen-und-kosten-pruefen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/zahlungen-zinsen-und-kosten-pruefen/SKILL.md) | Saldo, Tilgung, Nebenforderungen und Stichtag |
| 5 | [insolvenz-und-masseforderungen-trennen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/insolvenz-und-masseforderungen-trennen/SKILL.md) | Entstehung, Fortführung und Verwalterhandeln |
| 6 | [sicherheiten-und-ausfall-pruefen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/sicherheiten-und-ausfall-pruefen/SKILL.md) | Aussonderung, Absonderung und Verteilung |
| 7 | [nachrang-und-gesellschafterdarlehen-pruefen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/nachrang-und-gesellschafterdarlehen-pruefen/SKILL.md) | Rang, Privilegien und besonderer Anmeldeaufruf |
| 8 | [verspaetete-anmeldungen-und-termine-bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/verspaetete-anmeldungen-und-termine-bearbeiten/SKILL.md) | Fristen und nachträgliche Prüfung |
| 9 | [bestreiten-titel-und-feststellung-bearbeiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/bestreiten-titel-und-feststellung-bearbeiten/SKILL.md) | Beteiligte, Titel und Verfolgung eines Widerspruchs |
| 10 | [glaeubigerbriefe-und-nachforderungen-erstellen](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/glaeubigerbriefe-und-nachforderungen-erstellen/SKILL.md) | Empfängerbezogene Schreiben zur Freigabe |
| 11 | [tabelle-und-elektronische-uebergabe-vorbereiten](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/tabelle-und-elektronische-uebergabe-vorbereiten/SKILL.md) | Datenabgleich und kontrollierte Exportvorbereitung |

## 1.3. Übungsakte und Arbeitsgrenzen

Zwei verknüpfte Übungsakten stehen bereit: [Rheinsteg Handwerk Köln](../testakten/insolvenzforderungen-handwerk-koeln/README.md) mit zehn Forderungsanmeldungen und [Pistazien-Brezelbäckerei München](../testakten/insolvenzforderungen-pistazienbrezeln-muenchen/README.md) mit fünf. Beide enthalten außerdem Kaufinteresse, einen nicht unterzeichneten Asset-Deal-Vertrag mit offenen Anlagen, Excel-Bestandslisten und die zugehörige Korrespondenz. So lässt sich derselbe Bestand für Forderungsabgleich und Vorbereitung eines Betriebskaufs nutzen. Die Vertragsentwürfe sind Arbeitsunterlagen des Falls, keine allgemeingültigen Muster und keine fertige Lösung.

Prüfvorschläge sind keine gerichtlichen Feststellungen. Eine manuelle Freigabe ersetzt weder das gerichtliche Prüfverfahren noch den Nachweis eines wirksamen Eingangs. Kein automatischer Versand, keine Auszahlung und keine Änderung von Originalunterlagen.

## 1.4. Quellen und Übergabe

Recherchestand: 22.10.2026. [Rechtsstand und Entscheidungen](references/rechtsstand-und-entscheidungen.md), [Quellenabgleich mit Rechtsprechungsgang](references/sachbearbeitung-quellen-2026-10-21.md#423-rechtsprechungsgang-und-arbeitsfolge), [Zitierweise](references/zitierweise.md), [elektronische Übergabe](references/elektronische-uebergabe.md).

Der [Exporthelfer](scripts/forderungsexport.py) wird aus dem Pluginverzeichnis mit `python3 scripts/forderungsexport.py INPUT.json OUT_DIR` aufgerufen. Interne JSON-, CSV- und neutrale XML-Entwürfe sind keine gerichtlichen XJustiz-Dateien. Der optionale XJustiz-3.6.2-Weg unterstützt ausschließlich die Erstnachricht 0300005, Ereignis 044 ohne Erklärungen, mit kontrollierter Stammdatenvorlage und amtlichem XSD-Paket. Weitere Voraussetzungen und Grenzen stehen in der technischen Referenz. PDF-Unterlagen, Zielgerichtsprüfung und gesonderte manuelle Freigabe bleiben erforderlich. Das experimentelle Paket ersetzt keine eigenverantwortliche rechtliche Prüfung.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Eingang und Belegabgleich | [`forderungen-pruefen-und-tabelle-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungen-pruefen-und-tabelle-vorbereiten/SKILL.md), [`anmeldung-und-glaeubiger-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/anmeldung-und-glaeubiger-klaeren/SKILL.md), [`forderungsgrund-und-belege-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungsgrund-und-belege-abgleichen/SKILL.md), [`zahlungen-zinsen-und-kosten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/zahlungen-zinsen-und-kosten-pruefen/SKILL.md) |
| 2. Forderungsart und Rang | [`insolvenz-und-masseforderungen-trennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/insolvenz-und-masseforderungen-trennen/SKILL.md), [`sicherheiten-und-ausfall-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/sicherheiten-und-ausfall-pruefen/SKILL.md), [`nachrang-und-gesellschafterdarlehen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/nachrang-und-gesellschafterdarlehen-pruefen/SKILL.md) |
| 3. Termin und Widerspruch | [`verspaetete-anmeldungen-und-termine-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/verspaetete-anmeldungen-und-termine-bearbeiten/SKILL.md), [`bestreiten-titel-und-feststellung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/bestreiten-titel-und-feststellung-bearbeiten/SKILL.md) |
| 4. Schreiben und Tabellenübergabe | [`glaeubigerbriefe-und-nachforderungen-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/glaeubigerbriefe-und-nachforderungen-erstellen/SKILL.md), [`tabelle-und-elektronische-uebergabe-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/tabelle-und-elektronische-uebergabe-vorbereiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 11 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 11 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anmeldung-und-glaeubiger-klaeren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/anmeldung-und-glaeubiger-klaeren/SKILL.md) | Prüft Eingang und Inhalt einer Forderungsanmeldung sowie Gläubiger, Vertretung und Rechtsübergänge. Klärt Doppelanmeldungen aus Abtretung, Bürgschaft oder Insolvenzgeld und trennt Anmeldewirksamkeit von materiellem Forderungsbestand. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/anmeldung-und-glaeubiger-klaeren/SKILL.md) |
| [`bestreiten-titel-und-feststellung-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/bestreiten-titel-und-feststellung-bearbeiten/SKILL.md) | Bereitet betrags- und rangbezogenes Bestreiten vor und ordnet die Folgen für Verwalter, Insolvenzgläubiger und Schuldner getrennt ein. Prüft Titel und Prozessfortsetzung und unterscheidet internen Prüfvorschlag, gerichtliche Feststellung... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/bestreiten-titel-und-feststellung-bearbeiten/SKILL.md) |
| [`forderungen-pruefen-und-tabelle-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungen-pruefen-und-tabelle-vorbereiten/SKILL.md) | Bearbeitet Forderungsanmeldungen vom Akteneingang bis zum begründeten Prüfvorschlag je Gläubiger mit Tabellenzeile und Briefentwurf. Trennt Betrag, Rang, Sicherheiten, Termine und gerichtlichen Prüfstatus; bereitet nur eine manuell freiz... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungen-pruefen-und-tabelle-vorbereiten/SKILL.md) |
| [`forderungsgrund-und-belege-abgleichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungsgrund-und-belege-abgleichen/SKILL.md) | Gleicht den angemeldeten Forderungsgrund mit Vertrag, Leistung, Abnahme, Rechnung und Einwendungen ab. Trennt hinreichende Individualisierung von Beweis und Schlüssigkeit und formuliert konkrete, positionsbezogene Prüfvorschläge statt pa... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/forderungsgrund-und-belege-abgleichen/SKILL.md) |
| [`glaeubigerbriefe-und-nachforderungen-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/glaeubigerbriefe-und-nachforderungen-erstellen/SKILL.md) | Erstellt konkrete Gläubigerbriefe aus dem belegten Prüfstand, etwa Belegnachforderung, Saldoklärung, Ranghinweis oder Mitteilung eines Bestreitens. Trennt Entwurf und Erklärung sowie interne Prüffrist und gesetzliche Frist; versendet nic... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/glaeubigerbriefe-und-nachforderungen-erstellen/SKILL.md) |
| [`insolvenz-und-masseforderungen-trennen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/insolvenz-und-masseforderungen-trennen/SKILL.md) | Ordnet Ansprüche nach Entstehung, Leistungszeit und Verwalterhandeln als Insolvenz- oder Masseforderung ein. Prüft fortlaufende Verträge, Erfüllungswahl und vorläufige Verwaltung, ohne aus Rechnungsdatum oder Zustimmung allein einen Mass... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/insolvenz-und-masseforderungen-trennen/SKILL.md) |
| [`nachrang-und-gesellschafterdarlehen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/nachrang-und-gesellschafterdarlehen-pruefen/SKILL.md) | Prüft gesetzliche und vereinbarte Rangstellen sowie Gesellschafterdarlehen mit Sanierungs- und Kleinbeteiligtenprivileg. Verhindert pauschalen Nachrang jeder Gesellschafterforderung und berücksichtigt den besonderen gerichtlichen Anmelde... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/nachrang-und-gesellschafterdarlehen-pruefen/SKILL.md) |
| [`sicherheiten-und-ausfall-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/sicherheiten-und-ausfall-pruefen/SKILL.md) | Prüft Eigentumsvorbehalt, Pfandrechte, Sicherungsübereignung und Sicherungsabtretung. Trennt Herausgabe, persönliche Forderung und Absonderung sowie deren Verwertung und spätere Ausfallberücksichtigung, ohne geschätzte Erlöse sofort vom... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/sicherheiten-und-ausfall-pruefen/SKILL.md) |
| [`tabelle-und-elektronische-uebergabe-vorbereiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/tabelle-und-elektronische-uebergabe-vorbereiten/SKILL.md) | Überführt begründete Prüfvorschläge in einen abgestimmten Tabellenentwurf und eine kontrollierte Übergabemappe. Trennt interne JSON-, CSV- und XML-Arbeitsdaten von schema- und zielgerichtsgeprüftem XJustiz mit PDF-Unterlagen; verlangt ma... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/tabelle-und-elektronische-uebergabe-vorbereiten/SKILL.md) |
| [`verspaetete-anmeldungen-und-termine-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/verspaetete-anmeldungen-und-termine-bearbeiten/SKILL.md) | Bearbeitet verspätete Forderungsanmeldungen und Änderungen mit dem zutreffenden Prüfweg. Unterscheidet Anmeldefrist, Prüfungstermin, Niederlegung und spätere Ausschlussfristen, ohne eine verspätete Anmeldung automatisch zurückzuweisen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/verspaetete-anmeldungen-und-termine-bearbeiten/SKILL.md) |
| [`zahlungen-zinsen-und-kosten-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/zahlungen-zinsen-und-kosten-pruefen/SKILL.md) | Rekonstruiert den angemeldeten Saldo aus Einzelrechnungen, Gutschriften und Zahlungen. Prüft Zinslauf, Tilgungsbestimmung und Kosten vor und nach Eröffnung und hält gesicherte Forderung, tatsächliche Befriedigung und geschätzten Ausfall... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/skills/zahlungen-zinsen-und-kosten-pruefen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

## 1.8. Forderungs-PDFs und vierzehn Prüffälle

Version 445.35.5 führt Eingang, Individualisierung, Belegprüfung, Teilbestreiten, Titelumfang, Schuldnerwiderspruch und tatsächlichen gerichtlichen Stand in sieben getrennten Bearbeitungsständen. Die elf bestehenden Skills und der Exporthelfer behalten ihre Identität. Die [vierzehn Prüffälle und vier vollständigen Musterbriefe](references/prueffaelle-und-musterausgaben.md) zeigen die unterschiedlichen Tabellenfolgen. Der [ergänzende Quellenabgleich](references/sachbearbeitung-quellen-2026-10-21.md#417-aktuelle-bestätigung-2026-anmelden-prüfen-bestreiten-und-identität-wahren) dokumentiert die zusätzliche amtliche Prüfung vom 22.10.2026.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Testakte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kaufhaus Katzenbogen, München](../testakten/insolvenzsachbearbeitung-kaufhaus-katzenbogen-muenchen/README.md) | [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzsachbearbeitung-kaufhaus-katzenbogen-muenchen_gesamt.pdf) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/testakte-insolvenzsachbearbeitung-kaufhaus-katzenbogen-muenchen.zip) | [ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/testakte-insolvenzsachbearbeitung-kaufhaus-katzenbogen-muenchen-einzelpdfs.zip) |

## 1.9. Komponentenrelease und Textfassungen

Der Komponentenrelease insolvenzsachbearbeitung-v1.1.0 enthält das fortgeführte Paket 445.35.5. Der Marketplace umfasst 308 Plugins. Die bisherigen Übungsakten bleiben unter ihren bisherigen Releaseadressen erreichbar.

| Bestandteil | Zugang |
| --- | --- |
| Paket 445.35.5 | [Plugin-ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker.zip) · [Portables ZIP](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker-portable.zip) |
| Werkstatt | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-werkstatt.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-werkstatt.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker-werkstatt.pdf) |
| Schnellstart | [Markdown](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-schnellstart.md) · [Text](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=insolvenzforderungen-checker/insolvenzforderungen-checker-schnellstart.txt) · [PDF](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/insolvenzsachbearbeitung-v1.1.0/insolvenzforderungen-checker-schnellstart.pdf) |

Markdown- und Textfassungen sind inhaltsgleich. Der Schnellstart bleibt einschließlich CRLF unter 7.500 UTF-8-Bytes. Für Beschlüsse, Kommission, Massebelege, Betriebsabläufe und Verbraucherinsolvenz führt [Insolvenzsachbearbeitung](../insolvenzsachbearbeitung/README.md) durch die weiteren Arbeitsprodukte.
