# Akte Betreuung Schmalfeld: Kontodaten und verdächtige Verträge

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf`](gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-betreuung-schmalfeld-kontodaten-vertraege.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-betreuung-schmalfeld-kontodaten-vertraege-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-betreuung-schmalfeld-kontodaten-vertraege` (Akte) | [testakte-betreuung-schmalfeld-kontodaten-vertraege.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betreuung-schmalfeld-kontodaten-vertraege.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.

Diese Arbeitsakte gehört zum Plugin `betreuungsrecht`, Skill
`kontodaten-vertragsverdacht-pruefung`.

## Fallkern

Herbert Wilhelm Schmalfeld, geboren am 14.03.1941, lebt in Berlin. Die
Akte dokumentiert die erste Durchsicht der Vermögenssorge nach Übernahme
einer Betreuung. Vorliegen:

- Kontoauszüge 2023 bis 2025.
- Vertrags- und Belegmappe mit Alltagsverträgen, Lotterie, Kontaktportal,
  Fernwartung, Sicherheitssoftware, Vermögensverwaltung, Beteiligung,
  Auslandsimmobilienreservierung und Einzelbelegen.
- Nachgereichte Bankrückfragen, E-Mails, handschriftliche Fundstücke,
  Veranstaltungsflyer, Onlinebanking-Hinweise und eine Vertragsprüfmatrix.
- Strukturierte Verdachtsliste für das Auswertungsskript.

## Dateien

| Datei | Zweck |
| --- | --- |
| `00_aktenuebersicht.md` | Schnellüberblick für den Skill |
| `01_falldaten_schmalfeld.json` | Stammdaten, Konten, Betreuungskontext |
| `02_ordentliche_dauerpositionen.csv` | Plausible Regelzahlungen |
| `03_verdaechtige_transaktionen.csv` | Manuell kuratierte auffällige Buchungen |
| `04_vertragsregister_schmalfeld.csv` | Vertrags- und Belegregister |
| `05_schmalfeld_verdaechtige_transaktionen.json` | Eingabe für das Hilfsskript |
| `06_risikoauswertung_schmalfeld.json` | Referenzauswertung des Hilfsskripts |
| `07_erstvermerk_betreuungsgericht.docx` | Muster für sachlichen Erstvermerk |
| `08_massnahmenplan.docx` | Sofort- und Folgeaufgaben |
| `09_vertragsauszuege_pruefmappe.docx` | Vertragsauszüge, Risikokörbe, Beleglücken und priorisierte Maßnahmen |
| `10_bankrueckfrage_saldenabgleich_und_onlinebanking.docx` | Bankrückfrage, TAN-/Onlinebanking-Themen, Saldenabgleich |
| `11_telefonakquise_chronologie_und_gedaechtnisprotokolle.docx` | Telefonakquise, Haustürkontakte, Gesprächsnotizen und Gedächtnisprotokolle |
| `12_vertragsmappe_nachgereichte_unterlagen.docx` | Detailauswertung nachgereichter Vertragsauszüge |
| `13_mahnung_digitalschutz24_2026-06-15.md` | Abschrift der zweiten Mahnung von Digital-Schutz24 über 256,00 EUR mit zurückgewiesener Kündigung der Betreuerin |
| `emails/` | EML-Korrespondenz von Bank, Umfeld und Angehörigen, darunter Bankantwort vom 04.06.2026 zur Rückholung der Auslandszahlungen |
| `jpg/` | Foto- und Scanfragmente aus der Wohnungsmappe |
| `xlsx/pruefmatrix_schmalfeld_vertraege.xlsx` | Vertragsprüfmatrix mit Fristen, Beleglücken und Maßnahmen |
| `originale/` | Originalunterlagen als PDFs |
| `gesamt-pdf/` | Zusammengeführtes Gesamt-PDF der Akte |

## Auswertung mit Hilfsskript

```bash
python betreuungsrecht/scripts/betreuung_konto_vertragscheck.py \
  testakten/betreuung-schmalfeld-kontodaten-vertraege/05_schmalfeld_verdaechtige_transaktionen.json
```

Der Output muss mindestens akute Treffer für angebliche Sicherheitskautionen,
Auslandsanlage, Auslandsimmobilienreservierung, Fernwartung/Sicherheitssoftware
und Hochrisikoanlage liefern.

## Prüffokus

Der Skill soll nicht pauschal alles als unwirksam oder betrügerisch bezeichnen.
Er soll unterscheiden:

- belegte Alltagsversorgung,
- private Hilfeleistungen mit Belegbedarf,
- wirtschaftlich unplausible oder risikoreiche Geschäfte,
- technische Schutzthemen durch Fernzugriff,
- mögliche gerichtliche Schutzmaßnahmen.
