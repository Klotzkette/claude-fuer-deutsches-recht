# Testakte Phishing-Vorfall Mayer ./. Sparkasse Berlin

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
