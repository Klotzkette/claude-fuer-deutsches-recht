# Schriftsatz-Versandwerkstatt

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fokussierte Versandwerkstatt für fertige Schriftsätze und Anlagen: konvertiert Dateien in PDF, stempelt Anlagen, prüft Dateinamen, Paketgrenzen, Absender, Signaturweg und Eingang und liefert eine kontrollierte beA-Mappe.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/schriftsatz-versandwerkstatt.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`schriftsatz-versandwerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftsatz-versandwerkstatt.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-werkstatt.md" download><code>schriftsatz-versandwerkstatt-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/schriftsatz-versandwerkstatt/schriftsatz-versandwerkstatt-schnellstart.md" download><code>schriftsatz-versandwerkstatt-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

## 1. Zweck

Dieses Plugin beginnt dort, wo die inhaltliche Arbeit beendet ist. Ein fertiger Schriftsatz und sein Beiwerk liegen in einem Ordner; die Werkstatt macht daraus getrennte, lesbare und kontrollierbare PDF-Dateien für eine elektronische Gerichtseinreichung.

Es prüft keine Anspruchsgrundlage und erfindet keinen Sachvortrag. Es ändert den Inhalt eines Schriftsatzes nur auf ausdrückliche Anweisung. Sein Ergebnis ist ein Versandordner samt Anlagenverzeichnis, Manifest, Preflight-Bericht, Freigabevermerk und Vorlage für die Eingangskontrolle.

## 2. Schnellster Einstieg

Lege Hauptdokument und Anlagen in einen Arbeitsordner. Benenne Anlagen möglichst bereits mit `Anlage_K_1_Beschreibung`, `Anlage_B_1_Beschreibung`, `Anlage_AST_1_Beschreibung` oder `Anlage_AG_1_Beschreibung`. Starte dann [`versandmappe-endfertigen`](skills/versandmappe-endfertigen/SKILL.md).

Der Skill liest zuerst den Ordner. Er fragt nur nach Angaben, die sich nicht aus den Dateien ergeben und die Produktion sperren: Empfängergericht, Aktenzeichen oder Neueingang, Frist, Nummernkreis, verantwortender Anwalt, tatsächlicher Versender und Signaturroute.

## 3. Was tatsächlich erzeugt wird

| Eingabe | Verarbeitung | Ergebnis |
| --- | --- | --- |
| DOC, DOCX, ODT oder RTF | Headless-Konvertierung mit LibreOffice | separates Hauptdokument oder Anlage als PDF |
| XLS, XLSX, ODS, PPT, PPTX oder ODP | PDF-Konvertierung und zwingende Sichtkontrolle | PDF mit protokolliertem Prüfschritt |
| JPG, JPEG oder PNG | Einpassung auf eine A4-Seite ohne Beschnitt | Bildanlage als PDF |
| EML | Absender, Empfänger, Datum, Betreff und Nachrichtentext | lesbare E-Mail-Anlage als PDF |
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

## 6. Lokales Werkzeug

Das reproduzierbare Werkzeug liegt unter [`skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py`](skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py). Es benötigt `pypdf` und `reportlab`; für Office-Dateien muss LibreOffice mit `soffice` verfügbar sein.

Erster Produktionslauf; er erzeugt die Dateien und hält die Freigabe bis zur Sichtkontrolle auf Stop:

```bash
python skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py \
  --eingang ./eingang \
  --ausgang ./ausgang \
  --hauptdokument ./eingang/Klageerwiderung.docx \
  --praefix B \
  --dokumentart Klageerwiderung \
  --gericht "Landgericht Essen" \
  --aktenzeichen "12 O 34/26" \
  --frist "2026-07-15 23:59" \
  --verantwortlich "Rechtsanwalt Max Muster" \
  --versender "Rechtsanwalt Max Muster" \
  --signaturweg persoenlich-sicher
```

Nach dem Öffnen und Vergleichen jeder erzeugten Seite denselben Lauf mit `--sichtpruefung-bestaetigt --strict --ueberschreiben` wiederholen. Die Bestätigung darf nicht vorweggenommen werden.

## 7. Grenzen

- Kein materiellrechtlicher oder taktischer Schriftsatzcheck.
- Keine automatische Versendung.
- Keine automatische qualifizierte elektronische Signatur.
- Keine Fristlöschung ohne positive Eingangsbestätigung.
- Keine Freigabe konvertierter Dateien ohne visuelle Seitenkontrolle.

## 8. Lizenz

Apache-2.0 OR MIT, Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`versandmappe-endfertigen`](skills/versandmappe-endfertigen/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`anlagen-konvertieren-und-sichtpruefen`](skills/anlagen-konvertieren-und-sichtpruefen/SKILL.md), [`hauptdokument-pdf-endfertigen`](skills/hauptdokument-pdf-endfertigen/SKILL.md), [`ordneraufnahme-und-produktionsmatrix`](skills/ordneraufnahme-und-produktionsmatrix/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`anlagen-nummerieren-und-stempeln`](skills/anlagen-nummerieren-und-stempeln/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`signaturweg-und-absender-pruefen`](skills/signaturweg-und-absender-pruefen/SKILL.md), [`stoerung-und-nachreichung-dokumentieren`](skills/stoerung-und-nachreichung-dokumentieren/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`dateinamen-und-paketgrenzen-pruefen`](skills/dateinamen-und-paketgrenzen-pruefen/SKILL.md), [`versandfreigabe-und-eingang-sichern`](skills/versandfreigabe-und-eingang-sichern/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 10 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`anlagen-konvertieren-und-sichtpruefen`](skills/anlagen-konvertieren-und-sichtpruefen/SKILL.md) | Konvertiert bereits ausgewählte Anlagen aus Office-, Tabellen-, Bild-, E-Mail-, Text- und Webformaten in getrennte PDFs, ohne Beweisinhalt zu verändern: protokolliert Quelle und Hash, erhält Absender- und Zeitangaben, meldet Anhänge und... |
| [`anlagen-nummerieren-und-stempeln`](skills/anlagen-nummerieren-und-stempeln/SKILL.md) | Führt den vorhandenen Anlagenkreis K, B, AST oder AG ohne Kollision fort, gleicht jede Kennung mit Schriftsatz und Anlagenverzeichnis ab, stempelt die Bezeichnung gut lesbar rechts oben auf jede PDF-Seite, schützt vorhandenen Inhalt vor... |
| [`dateinamen-und-paketgrenzen-pruefen`](skills/dateinamen-und-paketgrenzen-pruefen/SKILL.md) | Vergibt robuste, sprechende beA-Dateinamen mit ASCII, Unterstrichen, logischer Reihenfolge und höchstens 80 Zeichen einschließlich Endung, prüft jede Datei gegen die ERVB-Höchstgrenze von 90 Zeichen sowie die Nachrichtengrenzen von 1.000... |
| [`hauptdokument-pdf-endfertigen`](skills/hauptdokument-pdf-endfertigen/SKILL.md) | Endfertigt den bereits freigegebenen Schriftsatz technisch als separates PDF: sichert die maßgebliche Quelldatei, konvertiert ohne inhaltliche Umschreibung, prüft Rubrum, Anträge, Seitenfolge, einfache Signatur, Schriften, Umbrüche, Meta... |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Schriftsatz Versandwerkstatt ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`ordneraufnahme-und-produktionsmatrix`](skills/ordneraufnahme-und-produktionsmatrix/SKILL.md) | Liest einen vorhandenen Schriftsatz- und Anlagenordner vor jeder Rückfrage, erkennt Hauptdokument, Fassungen, bereits verwendete Anlagenkennungen, Dubletten, fehlende Belege und nicht unterstützte Formate und liefert eine konkrete Produk... |
| [`signaturweg-und-absender-pruefen`](skills/signaturweg-und-absender-pruefen/SKILL.md) | Klärt vor der Freigabe die verantwortende Person, den tatsächlichen Versender, das verwendete sichere Postfach und die verfahrensbezogene Formroute; unterscheidet persönlichen sicheren Versand mit einfacher Signatur von der qualifizierte... |
| [`stoerung-und-nachreichung-dokumentieren`](skills/stoerung-und-nachreichung-dokumentieren/SKILL.md) | Erstellt bei technischer Übermittlungsstörung, ungeeignetem elektronischem Dokument oder gerichtlichem Nachreichungshinweis eine belastbare Ereignis- und Dateichronologie: sichert Fehlermeldungen, Versandversuche, Systemstatus, Ersatzweg... |
| [`versandfreigabe-und-eingang-sichern`](skills/versandfreigabe-und-eingang-sichern/SKILL.md) | Führt die letzte technische und organisatorische Freigabe der Versandmappe durch: öffnet jede Enddatei, gleicht Empfänger, Aktenzeichen, Frist, Schriftsatzfassung, Anlagenfolge, Bytes, Hashes, Signaturroute und Nachrichtenteile ab, erzeu... |
| [`versandmappe-endfertigen`](skills/versandmappe-endfertigen/SKILL.md) | Orchestriert die vollständige Endfertigung eines bereits geschriebenen Schriftsatzes mit gemischten Anlagen: liest den Arbeitsordner zuerst, erzeugt eine Produktionsmatrix, konvertiert Quellen kontrolliert in PDF, stempelt und benennt An... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
