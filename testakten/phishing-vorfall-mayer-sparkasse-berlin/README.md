# Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

[Testakten-Übersicht](../README.md) · [Repository-Start](../../README.md) · [Plugin-Katalog](../../README.md#was-ist-drin) · [Download-Index](../../ASSET_INDEX.md)

Dieses Aktenpaket gibt es in drei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält die nativen Originaldateien wie DOCX, Tabellen, E-Mails, Fotos und PDFs. Es enthält kein Markdown; sämtliche Dateien liegen ohne Unterordner unmittelbar auf der ZIP-Wurzelebene. Das Einzel-PDF-ZIP liefert jede Unterlage als separate, sauber gerenderte PDF unmittelbar auf der ZIP-Wurzelebene.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei) | PDF | [`gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf`](gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-phishing-vorfall-mayer-sparkasse-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-phishing-vorfall-mayer-sparkasse-berlin` (Akte) | [testakte-phishing-vorfall-mayer-sparkasse-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.

Diese Arbeitsakte gehört zum Plugin `phishing-vorfall-pruefer`.

Sie simuliert einen Online-Banking-Phishing-Fall mit Call-ID-Spoofing, pushTAN-Freigabe, streitiger grober Fahrlässigkeit, Ombudsmann-Verfahren und anschließender Klage. Die Originalunterlagen liegen als PDF im Ordner `originale/` und zusätzlich als ZIP `Mandatsakte_Mayer_vs_Sparkasse_Berlin.zip`.

## Enthaltene Arbeitsdateien

- `00_aktenuebersicht.md` - Überblick über die Unterlagen.
- `01_falldaten_mayer_sparkasse.json` - strukturierte Falldaten.
- `02_transaktionsmatrix.csv` - schadensbezogene Vorgänge.
- `03_beweis_und_log_matrix.csv` - Beweisfragen und fehlende Banklogs.
- `04_erstbewertung_675u_675v.docx` - juristischer Erstvermerk.
- `05_grobe_fahrlaessigkeit_ampel.docx` - Risikoampel zum Bankeinwand.
- `06_bankpflichten_und_tech_logs.docx` - technische Auffälligkeiten.
- `07_ombudsmann_und_klagepfad.docx` - Verfahrensstrategie.
- `08_case_gate_input.json` - Input für das Offline-Gate.
- `09_case_gate_output.json` - Beispiel-Output des Offline-Gates.
- `10_verfuegung_lg_berlin_terminierung.docx` - Abschrift der gerichtlichen Verfügung: Termin 21.04.2026, Fristen, Vorlageanordnung zu den pushTAN-Protokollen.

## Testlauf

```bash
python phishing-vorfall-pruefer/scripts/phishing_case_gate.py --input testakten/phishing-vorfall-mayer-sparkasse-berlin/08_case_gate_input.json
```

Erwartung: Der Fall wird nicht als sicherer Selbstläufer bewertet. Der Erstattungsanspruch dem Grunde nach steht gut, der Einwand grober Fahrlässigkeit ist aber erheblich und muss mit App-Dialog, Spoofing, Banklogs und Monitoring sauber angegriffen werden.
