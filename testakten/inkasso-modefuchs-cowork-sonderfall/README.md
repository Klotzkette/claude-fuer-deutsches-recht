# Akte Inkasso ModeFuchs – Cowork-Sonderfall (unsortierter Desktop-Ordner)

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/inkasso-modefuchs-cowork-sonderfall_gesamt.pdf`](gesamt-pdf/inkasso-modefuchs-cowork-sonderfall_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-inkasso-modefuchs-cowork-sonderfall.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-modefuchs-cowork-sonderfall.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-inkasso-modefuchs-cowork-sonderfall-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-modefuchs-cowork-sonderfall-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Sonderfall-Goodie zum Ausprobieren der Claude Cowork-Funktion. Diese Akte simuliert einen typischen Übergabeordner auf dem Desktop eines Inkasso-Sachbearbeiters: E-Mails als echte `.eml`-Dateien, Mahnungen als Scans ohne Textebene, ein Handyfoto des Einlieferungsbelegs, ein rohes Forderungskonto als Excel und ein Klageentwurf als Word-Datei – alles mit absichtlich nichtssagenden Dateinamen wie `Scan007.pdf`, `mail (2).eml` oder `Dokument1.pdf`.

Zugeordnetes Plugin: `forderungsmanagement-klagewerkstatt` (die Akte funktioniert aber auch ganz ohne Plugin als reine Cowork-Demo).

## Kernfall

Die ModeFuchs GmbH verkauft am 03.04.2025 Ware über 698,00 EUR auf Rechnung an Gottlieb von Altenhausen. Rechnung, Zahlungserinnerung und E-Mail-Mahnungen bleiben unbezahlt; zwei Mahnungen gehen zusätzlich per Post. Am 08.06.2025 wird die Forderung an die InkassoZentrale GmbH abgetreten. Der Schuldner meldet sich erst am 27.06.2025: Er habe von Rechnung und Mahnungen nie etwas gesehen, sein Spamfilter habe alles aussortiert und nach 10 Tagen automatisch gelöscht. Den Warenwert will er zahlen, Zinsen, Mahngebühren und Inkassokosten verweigert er, da er nie in Verzug gewesen sei.

Der Klageentwurf der InkassoZentrale liegt als Word-Datei bereit und verweist bereits auf die Anlagen K 1 bis K 7 – nur zusammengestellt, benannt und gestempelt ist noch nichts.

## Die Cowork-Aufgabe

Den Ordner (Akten-ZIP entpacken) in Claude Cowork öffnen und zum Beispiel Folgendes verlangen:

1. **In jede Datei hineinschauen und sprechend umbenennen** – aus `Scan007.pdf` wird etwa `2025-05-22_zweite_mahnung_modefuchs.pdf`.
2. **Anlagen zur Klage zusammenstellen**: Die im Klageentwurf referenzierten Anlagen K 1 bis K 7 aus den E-Mails, Scans und dem Foto zusammensuchen, jede Anlage als PDF aufbereiten und oben rechts als „Anlage K 1" usw. stempeln – versandfertig für beA oder eBO.
3. **Klageentwurf finalisieren** nach der Vorlage in der Word-Datei.
4. **Forderungsaufstellung prüfen** oder als saubere Excel-Tabelle neu aufbauen (Hauptforderung, Mahngebühren, Verzugszinsen, Inkassokosten).

Beispiel-Prompt:

> Sichte alle Dateien in diesem Ordner, benenne sie sprechend nach Datum und Inhalt um, stelle die im Klageentwurf genannten Anlagen K 1 bis K 7 als gestempelte PDF-Dateien zusammen und lege eine Forderungsaufstellung als Excel-Tabelle an.

## Inhalt

| Datei | Was wirklich drinsteckt |
| --- | --- |
| `mail.eml` | Bestellbestätigung vom 03.04.2025 (Auftrag MF-20250403-1749). |
| `mail (2).eml` | Rechnung R-20250406-3098 vom 06.04.2025 mit PDF-Anhang. |
| `mail (3).eml` | Zahlungserinnerung vom 20.04.2025. |
| `AW Re dringend Ihre Zahlungsaufforderung.eml` | Antwort des Schuldners vom 27.06.2025 mit der Spamfilter-Einlassung. |
| `Scan_20250610_113247.pdf` | Erste Mahnung vom 05.05.2025 (Scan ohne Textebene). |
| `Scan007.pdf` | Zweite Mahnung vom 22.05.2025 mit Inkasso-Ankündigung (Scan ohne Textebene). |
| `Dokument1.pdf` | Abtretungserklärung vom 08.06.2025 (Scan ohne Textebene). |
| `IMG_2047.jpg` | Handyfoto des Einlieferungsbelegs zum Einwurf-Einschreiben vom 22.05.2025. |
| `unbenannt.xlsx` | Rohes Forderungskonto mit Zinsberechnung, Stand 05.07.2025. |
| `Entwurf Klage MODEFUCHS FINAL v3 (2).docx` | Klageentwurf der InkassoZentrale mit Anlagenverzeichnis K 1 bis K 7. |

## Erwartetes Testergebnis

- Alle zehn Dateien sind inhaltlich korrekt erkannt und sprechend umbenannt.
- Die Anlagen K 1 bis K 7 sind vollständig und richtig zugeordnet: K 1 Abtretung (`Dokument1.pdf`), K 2 Bestellbestätigung (`mail.eml`), K 3 Rechnung nebst E-Mail (`mail (2).eml`), K 4 Zahlungserinnerung (`mail (3).eml`), K 5 erste Mahnung (`Scan_20250610_113247.pdf`), K 6 zweite Mahnung nebst Einlieferungsbeleg (`Scan007.pdf` + `IMG_2047.jpg`), K 7 Schuldner-E-Mail (`AW Re dringend….eml`).
- Jede Anlage liegt als PDF mit Stempel „Anlage K n" vor; E-Mails sind als lesbare PDF gerendert, der Rechnungsanhang aus `mail (2).eml` ist extrahiert.
- Die Forderungsaufstellung stimmt mit dem Klageentwurf überein: 698,00 EUR Hauptforderung, 5,50 EUR Mahngebühren, 10,80 EUR Verzugszinsen, 83,54 EUR Inkassokosten.
- Bonus: Das Spannungsfeld um den Zugang der E-Mail-Rechnung (Spamfilter, § 130 BGB, Verzugsbeginn § 286 Abs. 3 BGB) wird als offener Streitpunkt erkannt und nicht stillschweigend zugunsten einer Seite aufgelöst.

## Bezug zur Hauptakte

Die ausführliche Arbeitsakte zum selben Fallkreis mit Gatekeeper-Matrix und 28 PDF-Originalunterlagen liegt unter [`inkasso-zahlungsklage-modefuchs/`](../inkasso-zahlungsklage-modefuchs/). Diese Sonderfall-Akte erzählt eine eigenständige Variante: Hier zahlt der Schuldner nicht, und der Streit dreht sich um den Zugang elektronischer Rechnungen und Mahnungen.
