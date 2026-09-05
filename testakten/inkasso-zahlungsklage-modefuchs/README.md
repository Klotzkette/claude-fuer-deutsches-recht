# Akte Inkasso-Zahlungsklage ModeFuchs

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten. Das Gesamt-PDF eignet sich zum Lesen und Ausdrucken. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf`](gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-inkasso-zahlungsklage-modefuchs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs-einzelpdfs.zip) |

Die ZIP-Links laden den zuletzt veröffentlichten Release. Das Gesamt-PDF ist auch im Akten-ZIP enthalten; für eine einheitliche Arbeitsfassung genügt deshalb dieses Archiv. Der hier verlinkte Repository-Stand kann zwischen Releases bereits neuer sein.

English: The original-format ZIP contains the working files directly at archive root, without subfolders or Markdown. Choose the combined PDF for reading; it is also included in that ZIP. Choose the individual-PDF ZIP to review each document separately. These are practice documents, not an installable plugin. ZIP links refer to the latest published release.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Direkt-Download |
| --- | --- |
| `testakte-inkasso-zahlungsklage-modefuchs` (Akte) | [testakte-inkasso-zahlungsklage-modefuchs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-inkasso-zahlungsklage-modefuchs.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.

Arbeitsakte für das Plugin `forderungsmanagement-klagewerkstatt`, Skill `inkasso-zahlungsklage-ersteller`.

## Kernfall

ModeFuchs GmbH verkauft Ware auf Rechnung an Gottlieb von Altenhausen. Die Rechnung über 698,00 EUR wird mehrfach angemahnt, dann an die InkassoZentrale GmbH abgetreten. Der Schuldner zahlt die Hauptforderung am 26.06.2025 direkt an ModeFuchs. Diese Zahlung ist intern spätestens am 01.07.2025 aktenkundig. Trotzdem werden später Mahnbescheid und Klage weiter über die Hauptforderung und Nebenforderungen geführt.

Der Prüffokus ist absichtlich scharf: Der Klagegenerator muss erkennen, dass die Hauptforderung nicht mehr eingeklagt werden darf. Es geht um **eindeutige Ansprüche einklagen, unsichere oder erledigte Positionen streichen**.

## Inhalt

| Datei | Zweck |
| --- | --- |
| `originale/` | PDF-Originalunterlagen der Arbeitsakte (28 Dokumente). |
| `00_aktenuebersicht.md` | Sachverhalt und Dokumentenlandkarte. |
| `01_forderungsdaten_modefuchs.json` | Strukturierte Kerndaten. |
| `02_mahnlauf_modefuchs.csv` | Mahn- und Zahlungschronologie. |
| `03_anspruchsmatrix_modefuchs.csv` | Ampel je Forderungsposition. |
| `04_klagefreigabe.docx` | Was darf in die Klage, was nicht. |
| `05_gerichtsort_pruefung.docx` | Gerichtsort-Workflow für Nürnberg/Coburg. |
| `06_korrigierter_klageauftrag.docx` | Sauberer Klageauftrag nach Gatekeeper-Logik. |
| `07_fehleranalyse_vorhandene_klage.docx` | Analyse der vorhandenen Klageschrift. |
| `08_claim_gate_input.json` | Maschinelles Input-Beispiel für das Claim-Gate. |
| `09_claim_gate_output.json` | Erwarteter Gatekeeper-Output. |
| `10_email_zahlungseingang_modefuchs_inkasso.eml` | E-Mail-Wechsel Buchhaltung ModeFuchs / InkassoZentrale vom 1. und 2. Juli 2025: verspätet gemeldete Direktzahlung, offene Restpositionen, Rückfrage zur Auskehrung. |

## Erwartetes Testergebnis

- Hauptforderung 698,00 EUR: **ROT**, nicht einklagen.
- Mahnkosten 5,50 EUR: **GELB**, nur nach Freigabe.
- Verzugszinsen 10,80 EUR: **GELB**, nur nach Freigabe.
- Inkassokosten 83,54 EUR: **GELB**, nur nach Freigabe.
- Gericht: AG Nürnberg für die streitige Klage plausibel; zentrale Mahngerichtszuständigkeit Bayern: AG Coburg. Beides im Echtlauf online prüfen und dokumentieren.
