# Akte Inkasso-Zahlungsklage ModeFuchs


<!-- BEGIN gesamt-pdf-section (autogen) -->
## 📕 Gesamt-PDF (alles in einer Datei)

> **Doppelt gemoppelt:** Diese Akte gibt es als ein einziges, durchsuchbares Gesamt-PDF mit allen Aktenstuecken (Schriftsaetze, Tabellen, Anhaenge) hintereinander – ideal zum Lesen oder Ausdrucken.

| Datei | Format | Groesse |
| --- | --- | --- |
| [`gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf`](gesamt-pdf/inkasso-zahlungsklage-modefuchs_gesamt.pdf) | PDF | 157 KB |

Im Release-ZIP `testakte-inkasso-zahlungsklage-modefuchs.zip` ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

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
| `originale/` | PDF-Originalunterlagen der Beispielakte (28 Dokumente). |
| `00_aktenuebersicht.md` | Sachverhalt und Dokumentenlandkarte. |
| `01_forderungsdaten_modefuchs.json` | Strukturierte Kerndaten. |
| `02_mahnlauf_modefuchs.csv` | Mahn- und Zahlungschronologie. |
| `03_anspruchsmatrix_modefuchs.csv` | Ampel je Forderungsposition. |
| `04_klagefreigabe.md` | Was darf in die Klage, was nicht. |
| `05_gerichtsort_pruefung.md` | Gerichtsort-Workflow für Nürnberg/Coburg. |
| `06_korrigierter_klageauftrag.md` | Sauberer Klageauftrag nach Gatekeeper-Logik. |
| `07_fehleranalyse_vorhandene_klage.md` | Analyse der vorhandenen Klageschrift. |
| `08_claim_gate_input.json` | Maschinelles Input-Beispiel für das Claim-Gate. |
| `09_claim_gate_output.json` | Erwarteter Gatekeeper-Output. |

## Erwartetes Testergebnis

- Hauptforderung 698,00 EUR: **ROT**, nicht einklagen.
- Mahnkosten 5,50 EUR: **GELB**, nur nach Freigabe.
- Verzugszinsen 10,80 EUR: **GELB**, nur nach Freigabe.
- Inkassokosten 83,54 EUR: **GELB**, nur nach Freigabe.
- Gericht: AG Nürnberg für die streitige Klage plausibel; zentrale Mahngerichtszuständigkeit Bayern: AG Coburg. Beides im Echtlauf online prüfen und dokumentieren.
