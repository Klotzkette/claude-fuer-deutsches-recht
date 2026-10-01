# Schriftsatz-Versandwerkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fokussierte Versandwerkstatt für fertige Schriftsätze und Anlagen: konvertiert Dateien in PDF, stempelt Anlagen, prüft Dateinamen, Paketgrenzen, Absender, Signaturweg und Eingang und liefert eine kontrollierte beA-Mappe.

Dieses Plugin gehört zum Marketplace mit 268 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`schriftsatz-versandwerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftsatz-versandwerkstatt.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/schriftsatz-versandwerkstatt.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/schriftsatz-versandwerkstatt.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/schriftsatz-versandwerkstatt.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Schriftsatz-Versandwerkstatt:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: eine Produktionsmatrix und kontrollierte Versandmappe. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`schriftsatz-versandwerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftsatz-versandwerkstatt.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`schriftsatz-versandwerkstatt-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`schriftsatz-versandwerkstatt-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 268 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Weserfunken Darlehensverfahren Bremen](../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md) | [Gesamt-PDF](../testakten/fintech-darlehen-vertragsuebernahme-bremen/gesamt-pdf/fintech-darlehen-vertragsuebernahme-bremen_gesamt.pdf) | [`testakte-fintech-darlehen-vertragsuebernahme-bremen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-fintech-darlehen-vertragsuebernahme-bremen.zip) | [`testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.26.0/testakte-fintech-darlehen-vertragsuebernahme-bremen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

## 1. Zweck

Dieses Plugin beginnt dort, wo die inhaltliche Arbeit beendet ist. Ein fertiger Schriftsatz und sein Beiwerk liegen in einem Ordner; die Werkstatt macht daraus getrennte, lesbare und kontrollierbare PDF-Dateien für eine elektronische Gerichtseinreichung.

Es prüft keine Anspruchsgrundlage und erfindet keinen Sachvortrag. Es ändert den Inhalt eines Schriftsatzes nur auf ausdrückliche Anweisung. Sein Ergebnis ist ein Versandordner samt Anlagenverzeichnis, Manifest, Preflight-Bericht, Freigabevermerk und Vorlage für die Eingangskontrolle.

## 2. Schnellster Einstieg

Lege Hauptdokument und Anlagen in einen freigegebenen Arbeitsordner. Originalnamen dürfen bleiben: `Scan_004.pdf`, `Mail vom Bauleiter.eml` und `Berechnung Müller.xlsx` müssen nicht vorher umbenannt werden. Starte [`versandmappe-endfertigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandmappe-endfertigen/SKILL.md), den Hauptskill dieses Plugins:

> Bereite aus diesem Ordner den freigegebenen Schriftsatz und seine Anlagen für den beA-Versand vor. Erhalte die Originale, ordne die Anlagen nach den Schriftsatzverweisen zu und erzeuge getrennte PDFs in einem neuen Ordner. Frage nur bei ungeklärter Fassung, Zuordnung oder Formroute nach. Nicht versenden.

Für uneinheitlich benannte Quellen führt die Werkstatt einen internen [Anlagenplan](references/ANLAGENPLAN-UND-PRODUKTION.md). Bereits vorhandene Kennungen wie `Anlage_B_7_Kaufvertrag.pdf` bleiben ebenfalls verwendbar. Unklare Dateien werden nicht still ausgelassen; interne Unterlagen erhalten einen dokumentierten Auslassungsgrund.

Der Skill liest zuerst den Ordner. Er fragt nur nach Angaben, die sich nicht aus den Dateien ergeben und die Produktion sperren: Empfängergericht, Aktenzeichen oder Neueingang, Frist, Nummernkreis, verantwortender Anwalt, tatsächlicher Versender und Signaturroute.

## 3. Was tatsächlich erzeugt wird

| Eingabe | Verarbeitung | Ergebnis |
| --- | --- | --- |
| DOC, DOCX, ODT oder RTF | Headless-Konvertierung mit LibreOffice | separates Hauptdokument oder Anlage als PDF |
| XLS, XLSX, ODS, PPT, PPTX oder ODP | PDF-Konvertierung und zwingende Sichtkontrolle | PDF mit protokolliertem Prüfschritt |
| JPG, JPEG, PNG, BMP oder mehrseitiges TIFF | Bildausrichtung und vollständige Seitenübernahme ohne Beschnitt | Bildanlage als PDF |
| EML | Kopfzeilen und Nachrichtentext; Anhänge gesondert zuordnen oder begründet ausschließen | lesbare E-Mail-Anlage und getrennte Anlagen-PDFs |
| TXT, CSV, TSV, Markdown oder HTML | paginierter Textauszug | lesbare PDF-Fassung |
| vorhandenes PDF | Prüfung, Benennung und bei Anlagen Stempelung | endgültige Versanddatei |

Proprietäre E-Mail-Container oder kennwortgeschützte Dateien werden nicht stillschweigend umgewandelt. Sie erhalten einen Stop-Befund und müssen in der Quellanwendung als überprüfbares PDF oder EML ausgegeben werden.

## 4. Dateinamensprofil

Das amtliche Maximum beträgt nach der ERVB 2025 90 Zeichen einschließlich Endung. Die Werkstatt verwendet vorsorglich höchstens 80 Zeichen, ausschließlich ASCII und Unterstriche zwischen Wörtern, zum Beispiel:

```text
00_20260714_Klageerwiderung_12_O_34_26.pdf
01_20260714_AnlageB1_Kaufvertrag.pdf
02_20260714_AnlageB2_E_Mail_Abnahme.pdf
```

Umlaute werden zu `ae`, `oe`, `ue`, das scharfe S zu `ss`. Die Einschränkung ist eine robuste Kanzleiregel; Umlaute wären nach der ERVB technisch zulässig.

## 5. Signatur und Versand

Die Werkstatt verlangt eine ausdrückliche Zuordnung:

1. Wer verantwortet den Schriftsatz?
2. Wer löst den Versand tatsächlich aus?
3. Aus welchem persönlich zugeordneten sicheren Postfach wird gesendet?
4. Wird der sichere Übermittlungsweg der verantwortenden Person genutzt oder ist eine qualifizierte elektronische Signatur erforderlich?

Sie bringt selbst keine qualifizierte elektronische Signatur an und sendet nichts. Ein grüner technischer Preflight ersetzt nicht die Freigabe durch den verantwortenden Anwalt.

Bereits elektronisch signierte Originale bleiben unverändert. Signierte Anlagen werden nicht automatisch gestempelt. Für berechtigten Personalversand mit qES und für Gesellschaftspostfächer gelten gesonderte Prüfwege; Personalversand ist nicht pauschal verboten. Die [Form- und Technikregeln](references/ERVV-ERVB-VERSANDREGELN.md) trennen gesetzliche Vorgaben, beA-Anwendungsgrenzen und das strengere Kanzleiprofil.

## 6. Lokales Werkzeug

Das reproduzierbare Werkzeug liegt unter [`skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py`](skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py). Es benötigt `pypdf`, `reportlab` und für Bilder `Pillow`; für Office-Dateien muss LibreOffice mit `soffice` verfügbar sein. Ohne passende Werkzeuge fordert der Skill einen kontrollierten Export an, statt eine erzeugte Datei zu behaupten.

Das Pluginpaket enthält auch den lokalen Helfer `office_process.py`; beim manuellen Kopieren muss er neben dem Werkzeug bleiben. Office-Konvertierungen arbeiten mit getrennten Profilen und einem Zeitlimit von 120 Sekunden pro Datei. Unter Linux und macOS beendet ein Abbruch die eigene Prozessgruppe. Fehlerhafte Anlagen werden als Stop-Befund protokolliert, während die übrigen Unterlagen weiter vorbereitet werden können. Ein Stop ist keine Versandfreigabe.

Erster Produktionslauf; er erzeugt die Dateien und hält die Freigabe bis zur Sichtkontrolle auf Stop:

```bash
python skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py \
  --eingang ./eingang \
  --ausgang ./ausgang \
  --hauptdokument ./eingang/Klageerwiderung.docx \
  --anlagenplan ./eingang/Anlagenplan.csv \
  --praefix B \
  --dokumentart Klageerwiderung \
  --gericht "Landgericht Essen" \
  --aktenzeichen "12 O 34/26" \
  --frist "2026-07-15 23:59" \
  --verantwortlich "Rechtsanwalt Max Muster" \
  --versender "Rechtsanwalt Max Muster" \
  --signaturweg persoenlich-sicher --strict
```

Status 3 hält die Freigabe bis zur Sichtkontrolle oder Klärung anderer protokollierter Hindernisse offen. Nach dem Öffnen und Vergleichen jeder endgültigen Seite die Freigabe zu genau diesen Dateihashes dokumentieren. Nicht allein für einen grünen Programmstatus erneut konvertieren und dabei die bereits geprüften Dateien ersetzen. Einzelheiten, CSV-Beispiel und Fortsetzung stehen im [Anlagenplan-Leitfaden](references/ANLAGENPLAN-UND-PRODUKTION.md). Ein tatsächlich anlagenloser Schriftsatz kann mit `--ohne-anlagen` vorbereitet werden.

## 7. Grenzen

- Kein materiellrechtlicher oder taktischer Schriftsatzcheck.
- Keine automatische Versendung.
- Keine automatische qualifizierte elektronische Signatur.
- Keine Fristlöschung ohne positive Eingangsbestätigung.
- Keine Freigabe konvertierter Dateien ohne visuelle Seitenkontrolle.

## 8. FinTech-Verfahrensakte

Die [Weserfunken-Akte aus Bremen](../testakten/fintech-darlehen-vertragsuebernahme-bremen/README.md) enthält eine 25-seitige Klage, 75 Seiten K-Anlagen, deutsch-englische Geschäftskorrespondenz und einen getrennten Ordner mit vorbereiteter Klageerwiderung samt B-Anlagen. Für die eigene rechtliche Fallanalyse diesen Antwortordner zunächst nicht laden.

Für die Versandproduktion dagegen nur `02_klageerwiderung` auswählen. Die Werkstatt bestätigt die Word-Hauptfassung und ordnet B1 bis B6 zu. Gerichtspost, K-Anlagen, Buchhaltungsdateien und interne Notizen werden nicht ungefragt mitgesendet. Der technische Produktionslauf ersetzt weder die rechtliche Bearbeitung des Falls noch die Freigabe der konkreten Anlagen durch den Anwalt.

## 9. Lizenz

Apache-2.0 OR MIT, Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag, Fassung und Anlagenzuordnung | [`versandmappe-endfertigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandmappe-endfertigen/SKILL.md), [`ordneraufnahme-und-produktionsmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/ordneraufnahme-und-produktionsmatrix/SKILL.md) |
| 2. PDF-Produktion und Anlagenkennzeichnung | [`hauptdokument-pdf-endfertigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/hauptdokument-pdf-endfertigen/SKILL.md), [`anlagen-konvertieren-und-sichtpruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-konvertieren-und-sichtpruefen/SKILL.md), [`anlagen-nummerieren-und-stempeln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-nummerieren-und-stempeln/SKILL.md) |
| 3. Dateinamen, Grenzen und Signaturroute | [`dateinamen-und-paketgrenzen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/dateinamen-und-paketgrenzen-pruefen/SKILL.md), [`signaturweg-und-absender-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/signaturweg-und-absender-pruefen/SKILL.md) |
| 4. Freigabe und Eingangskontrolle | [`versandfreigabe-und-eingang-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandfreigabe-und-eingang-sichern/SKILL.md) |
| 5. Formhindernisse und Störungen | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/juristischer-argumentationskern/SKILL.md), [`stoerung-und-nachreichung-dokumentieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/stoerung-und-nachreichung-dokumentieren/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 10 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`anlagen-konvertieren-und-sichtpruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-konvertieren-und-sichtpruefen/SKILL.md) | Konvertiert zugeordnete Anlagen aus Office-, Tabellen-, Bild-, E-Mail- und Textformaten in getrennte PDFs. Erhält Quellbezug und sämtliche Scanseiten, kontrolliert E-Mail-Anhänge und stoppt bei Beschnitt, Zeichenverlust oder fehlenden Bl... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-konvertieren-und-sichtpruefen/SKILL.md) |
| [`anlagen-nummerieren-und-stempeln`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-nummerieren-und-stempeln/SKILL.md) | Führt den vorhandenen Anlagenkreis K, B, AST oder AG ohne Kollision fort, gleicht jede Kennung mit Schriftsatz und Anlagenverzeichnis ab, stempelt die Bezeichnung gut lesbar rechts oben auf jede PDF-Seite, schützt vorhandenen Inhalt vor... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/anlagen-nummerieren-und-stempeln/SKILL.md) |
| [`dateinamen-und-paketgrenzen-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/dateinamen-und-paketgrenzen-pruefen/SKILL.md) | Vergibt robuste, sprechende beA-Dateinamen mit ASCII, Unterstrichen, logischer Reihenfolge und höchstens 80 Zeichen einschließlich Endung, prüft jede Datei gegen die ERVB-Höchstgrenze von 90 Zeichen sowie die Nachrichtengrenzen von 1.000... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/dateinamen-und-paketgrenzen-pruefen/SKILL.md) |
| [`hauptdokument-pdf-endfertigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/hauptdokument-pdf-endfertigen/SKILL.md) | Endfertigt den bereits freigegebenen Schriftsatz technisch als separates PDF: sichert die maßgebliche Quelldatei, konvertiert ohne inhaltliche Umschreibung, prüft Rubrum, Anträge, Seitenfolge, einfache Signatur, Schriften, Umbrüche, Meta... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/hauptdokument-pdf-endfertigen/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/juristischer-argumentationskern/SKILL.md) | Begründet konkrete Formhindernisse einer beA-Versandmappe anhand von Datei, Signaturroute und Eingangsbeleg. Liefert einen nachvollziehbaren Freigabe- oder Rückfragevermerk; prüft keine Ansprüche, Erfolgsaussichten oder materiellen Einwe... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/juristischer-argumentationskern/SKILL.md) |
| [`ordneraufnahme-und-produktionsmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/ordneraufnahme-und-produktionsmatrix/SKILL.md) | Liest einen vorhandenen Schriftsatz- und Anlagenordner vor jeder Rückfrage, erkennt Hauptdokument, Fassungen, bereits verwendete Anlagenkennungen, Dubletten, fehlende Belege und nicht unterstützte Formate und liefert eine konkrete Produk... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/ordneraufnahme-und-produktionsmatrix/SKILL.md) |
| [`signaturweg-und-absender-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/signaturweg-und-absender-pruefen/SKILL.md) | Prüft für eine vorbereitete Versandmappe Verantwortung, tatsächlichen Versender, Postfach und Formroute. Unterscheidet persönlichen Versand mit einfacher Signatur vom berechtigten Personalversand mit qualifizierter elektronischer Signatu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/signaturweg-und-absender-pruefen/SKILL.md) |
| [`stoerung-und-nachreichung-dokumentieren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/stoerung-und-nachreichung-dokumentieren/SKILL.md) | Erstellt bei technischer Übermittlungsstörung, ungeeignetem elektronischem Dokument oder gerichtlichem Nachreichungshinweis eine belastbare Ereignis- und Dateichronologie: sichert Fehlermeldungen, Versandversuche, Systemstatus, Ersatzweg... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/stoerung-und-nachreichung-dokumentieren/SKILL.md) |
| [`versandfreigabe-und-eingang-sichern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandfreigabe-und-eingang-sichern/SKILL.md) | Führt die letzte technische und organisatorische Freigabe der Versandmappe durch: öffnet jede Enddatei, gleicht Empfänger, Aktenzeichen, Frist, Schriftsatzfassung, Anlagenfolge, Bytes, Hashes, Signaturroute und Nachrichtenteile ab, erzeu... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandfreigabe-und-eingang-sichern/SKILL.md) |
| [`versandmappe-endfertigen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandmappe-endfertigen/SKILL.md) | Macht einen fertigen Schriftsatz mit gemischten Anlagen technisch versandbereit: PDF-Konvertierung, Anlagenstempel, Dateinamen, Paketgrenzen und Signaturroute. Liefert getrennte Versanddateien und einen Prüfbericht; ersetzt keine inhaltl... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=schriftsatz-versandwerkstatt/skills/versandmappe-endfertigen/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
