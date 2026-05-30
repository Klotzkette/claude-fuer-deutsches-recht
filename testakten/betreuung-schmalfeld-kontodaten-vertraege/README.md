# Akte Betreuung Schmalfeld: Kontodaten und verdächtige Verträge


<!-- BEGIN gesamt-pdf-section (autogen) -->
## 📕 Gesamt-PDF (alles in einer Datei)

> **Doppelt gemoppelt:** Diese Akte gibt es als ein einziges, durchsuchbares Gesamt-PDF mit allen Aktenstuecken (Schriftsaetze, Tabellen, Anhaenge) hintereinander – ideal zum Lesen oder Ausdrucken.

| Datei | Format | Groesse |
| --- | --- | --- |
| [`gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf`](gesamt-pdf/betreuung-schmalfeld-kontodaten-vertraege_gesamt.pdf) | PDF | 376 KB |

Im Release-ZIP `testakte-betreuung-schmalfeld-kontodaten-vertraege.zip` ist das Gesamt-PDF mit enthalten.

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
Akte simuliert die erste Durchsicht der Vermögenssorge nach Übernahme
einer Betreuung. Vorliegen:

- Kontoauszüge 2023 bis 2025.
- Vertrags- und Belegmappe mit Alltagsverträgen, Lotterie, Kontaktportal,
  Fernwartung, Sicherheitssoftware, Vermögensverwaltung, Beteiligung,
  Auslandsimmobilienreservierung und Einzelbelegen.
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
| `06_risikoauswertung_schmalfeld.json` | Erwartete Skriptauswertung |
| `07_erstvermerk_betreuungsgericht.md` | Muster für sachlichen Erstvermerk |
| `08_massnahmenplan.md` | Sofort- und Folgeaufgaben |
| `09_vertragsauszuege_pruefmappe.md` | Vertragsauszüge, Risikokörbe, Beleglücken und priorisierte Maßnahmen |
| `originale/` | Originale Beispielunterlagen als ZIP und PDFs |

## Erwarteter Testlauf

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
