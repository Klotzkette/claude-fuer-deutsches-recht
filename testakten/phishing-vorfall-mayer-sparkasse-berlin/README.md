# Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin


<!-- BEGIN gesamt-pdf-section (autogen) -->
## 📕 Gesamt-PDF (alles in einer Datei)

> **Doppelt gemoppelt:** Diese Akte gibt es als ein einziges, durchsuchbares Gesamt-PDF mit allen Aktenstuecken (Schriftsaetze, Tabellen, Anhaenge) hintereinander – ideal zum Lesen oder Ausdrucken.

| Datei | Format | Groesse |
| --- | --- | --- |
| [`gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf`](gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) | PDF | 222 KB |

Im Release-ZIP `testakte-phishing-vorfall-mayer-sparkasse-berlin.zip` ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

## ⬇️ Direkt-Download

| Akte | Direkt-Download |
| --- | --- |
| `testakte-phishing-vorfall-mayer-sparkasse-berlin` (Akte) | [testakte-phishing-vorfall-mayer-sparkasse-berlin.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |

Diese Akte wird separat als ZIP-Datei aus dem GitHub-Release bereitgestellt. Das ZIP enthält die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für die Bearbeitung.


Diese Beispielakte gehört zum Plugin `phishing-vorfall-pruefer`.

Sie simuliert einen Online-Banking-Phishing-Fall mit Call-ID-Spoofing, pushTAN-Freigabe, streitiger grober Fahrlässigkeit, Ombudsmann-Verfahren und anschließender Klage. Die Originalunterlagen liegen als PDF im Ordner `originale/` und zusätzlich als ZIP `Mandatsakte_Mayer_vs_Sparkasse_Berlin.zip`.

## Enthaltene Arbeitsdateien

- `00_aktenuebersicht.md` - Überblick über die Unterlagen.
- `01_falldaten_mayer_sparkasse.json` - strukturierte Falldaten.
- `02_transaktionsmatrix.csv` - schadensbezogene Vorgänge.
- `03_beweis_und_log_matrix.csv` - Beweisfragen und fehlende Banklogs.
- `04_erstbewertung_675u_675v.md` - juristischer Erstvermerk.
- `05_grobe_fahrlaessigkeit_ampel.md` - Risikoampel zum Bankeinwand.
- `06_bankpflichten_und_tech_logs.md` - technische Auffälligkeiten.
- `07_ombudsmann_und_klagepfad.md` - Verfahrensstrategie.
- `08_case_gate_input.json` - Input für das Offline-Gate.
- `09_case_gate_output.json` - Beispiel-Output des Offline-Gates.

## Testlauf

```bash
python phishing-vorfall-pruefer/scripts/phishing_case_gate.py --input testakten/phishing-vorfall-mayer-sparkasse-berlin/08_case_gate_input.json
```

Erwartung: Der Fall wird nicht als sicherer Selbstläufer bewertet. Der Erstattungsanspruch dem Grunde nach steht gut, der Einwand grober Fahrlässigkeit ist aber erheblich und muss mit App-Dialog, Spoofing, Banklogs und Monitoring sauber angegriffen werden.
