# Lohnpfändung - Berechnung Tabelle 1.7.2025

Berechnet mit `zwangsvollstreckung/werkzeuge/pfaendungsrechner.py`. Tabelle gültig vom 1.7.2025 bis 30.6.2026.

## Bernd Mueller (Geschäftsführer Mueller Küchen GmbH)

| Position | Wert |
| --- | --- |
| Drittschuldner | Mueller Küchen GmbH (AG Krefeld HRB 14 432) |
| Nettogehalt | 4.200,00 EUR / Monat |
| Unterhaltspflichten | 3 (Ehefrau Dorothea, Kinder Vincent und Leah) |
| Freibetrag Paragraf 850c | 2.792,31 EUR |
| Pfaendbarkeitsquote (Paragraf 850c Abs. 3 ZPO, 3 UP) | 3/10 |
| Pfändbar / Monat | 422,30 EUR |
| Schuldneranteil | 3.777,70 EUR |

Aufruf:

```
python3 werkzeuge/pfaendungsrechner.py --netto 4200 --unterhalt 3
```

Anmerkung: Da Bernd Mueller zugleich Geschäftsführer und mittelbarer Gesellschafter (60 Prozent) ist, droht die Gefahr, dass das Gehalt im Lichte des Paragraf 826 BGB / Paragraf 850h ZPO als verschleiertes Arbeitsentgelt zu hoch bemessen ist. Verdacht: keine - das Gehalt entspricht laut Anmerkung der Steuerberaterin der branchenüblichen Bandbreite. Eine Korrektur nach Paragraf 850h ZPO ist daher nicht erforderlich.

## Dorothea Mueller (Helios Klinik Krefeld GmbH)

| Position | Wert |
| --- | --- |
| Drittschuldnerin | Helios Klinik Krefeld GmbH |
| Nettogehalt | 2.350,00 EUR / Monat (75 Prozent Stelle Krankenschwester) |
| Unterhaltspflichten | 2 (Kinder Vincent und Leah) |
| Freibetrag Paragraf 850c | 2.466,27 EUR |
| Pfändbar / Monat | 0,00 EUR |
| Schuldneranteil | 2.350,00 EUR |

Aufruf:

```
python3 werkzeuge/pfaendungsrechner.py --netto 2350 --unterhalt 2
```

Anmerkung: Dorothea Mueller liegt unter dem Freibetrag. Die Lohnpfändung gegen sie würde ergebnislos verlaufen. Aus wirtschaftlichen Gründen empfiehlt sich, **gegen sie nur die Kontopfändung DKB** zu betreiben (mit P-Konto-Korrektur), nicht die Lohnpfändung.

## P-Konto-Freibetrag

| Position | Wert |
| --- | --- |
| Bernd Mueller (3 Unterhalt) | 2.797,31 EUR / Monat |
| Dorothea Mueller (2 Unterhalt) | 2.471,27 EUR / Monat |
| Sockel ohne Unterhaltsbescheinigung | 1.560,00 EUR / Monat |

Beide Schuldner benötigen für den höheren Schutz eine Bescheinigung der Familienkasse oder anerkannten Schuldnerberatung. Sonst greift nur der Sockelbetrag 1.560,00 EUR.

## Wirtschaftliche Konsequenz

| Strang | Erwarteter Ertrag / Monat |
| --- | --- |
| Lohnpfändung Bernd Mueller (GmbH) | 422,30 EUR |
| Kontopfändung Postbank (Eingänge über Gehaltsauszahlung) | aufgehend in der Lohnpfändung, keine doppelte Belastung |
| Kontopfändung DKB Dorothea | nur Spitzenwerte über 1.560 EUR P-Konto-Sockel; nach Familienkasse-Bescheinigung 2.471,27 EUR |
| Lohnpfändung Dorothea Mueller | 0 EUR - nicht durchführen |

Tilgung allein aus Lohnpfändung B. Mueller braucht ca. 634 Monate für 267.569,33 EUR (422,30 EUR/Monat). Die dingliche ZVG-Vollstreckung in das Grundstueck (Grundschuld 380.000 EUR) ist damit der wirtschaftlich entscheidende Strang, die Lohnpfändung sichert nur die laufende Verzinsung ab.
