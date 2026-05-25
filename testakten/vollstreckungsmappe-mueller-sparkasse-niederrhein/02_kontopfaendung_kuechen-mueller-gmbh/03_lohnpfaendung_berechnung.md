# Lohnpfaendung - Berechnung Tabelle 1.7.2025

Berechnet mit `zwangsvollstreckung/werkzeuge/pfaendungsrechner.py`. Tabelle gueltig vom 1.7.2025 bis 30.6.2026.

## Bernd Mueller (Geschaeftsfuehrer Mueller Kuechen GmbH)

| Position | Wert |
| --- | --- |
| Drittschuldner | Mueller Kuechen GmbH (AG Krefeld HRB 14 432) |
| Nettogehalt | 4.200,00 EUR / Monat |
| Unterhaltspflichten | 3 (Ehefrau Dorothea, Kinder Vincent und Leah) |
| Freibetrag Paragraf 850c | 2.797,30 EUR |
| Pfaendbar / Monat | 981,89 EUR |
| Schuldneranteil | 3.218,11 EUR |

Aufruf:

```
python3 werkzeuge/pfaendungsrechner.py --netto 4200 --unterhalt 3
```

Anmerkung: Da Bernd Mueller zugleich Geschaeftsfuehrer und mittelbarer Gesellschafter (60 Prozent) ist, droht die Gefahr, dass das Gehalt im Lichte des Paragraf 826 BGB / Paragraf 850h ZPO als verschleiertes Arbeitsentgelt zu hoch bemessen ist. Verdacht: keine - das Gehalt entspricht laut Anmerkung der Steuerberaterin der branchenueblichen Bandbreite. Eine Korrektur nach Paragraf 850h ZPO ist daher nicht erforderlich.

## Dorothea Mueller (Helios Klinik Krefeld GmbH)

| Position | Wert |
| --- | --- |
| Drittschuldnerin | Helios Klinik Krefeld GmbH |
| Nettogehalt | 2.350,00 EUR / Monat (75 Prozent Stelle Krankenschwester) |
| Unterhaltspflichten | 2 (Kinder Vincent und Leah) |
| Freibetrag Paragraf 850c | 2.471,26 EUR |
| Pfaendbar / Monat | 0,00 EUR |
| Schuldneranteil | 2.350,00 EUR |

Aufruf:

```
python3 werkzeuge/pfaendungsrechner.py --netto 2350 --unterhalt 2
```

Anmerkung: Dorothea Mueller liegt unter dem Freibetrag. Die Lohnpfaendung gegen sie wuerde ergebnislos verlaufen. Aus wirtschaftlichen Gruenden empfiehlt sich, **gegen sie nur die Kontopfaendung DKB** zu betreiben (mit P-Konto-Korrektur), nicht die Lohnpfaendung.

## P-Konto-Freibetrag

| Position | Wert |
| --- | --- |
| Bernd Mueller (3 Unterhalt) | 2.797,31 EUR / Monat |
| Dorothea Mueller (2 Unterhalt) | 2.471,27 EUR / Monat |
| Sockel ohne Unterhaltsbescheinigung | 1.560,00 EUR / Monat |

Beide Schuldner benoetigen fuer den hoeheren Schutz eine Bescheinigung der Familienkasse oder anerkannten Schuldnerberatung. Sonst greift nur der Sockelbetrag 1.560,00 EUR.

## Wirtschaftliche Konsequenz

| Strang | Erwarteter Ertrag / Monat |
| --- | --- |
| Lohnpfaendung Bernd Mueller (GmbH) | 981,89 EUR |
| Kontopfaendung Postbank (Eingaenge ueber Gehaltsauszahlung) | aufgehend in der Lohnpfaendung, keine doppelte Belastung |
| Kontopfaendung DKB Dorothea | nur Spitzenwerte ueber 1.560 EUR P-Konto-Sockel; nach Familienkasse-Bescheinigung 2.471,27 EUR |
| Lohnpfaendung Dorothea Mueller | 0 EUR - nicht durchfuehren |

Tilgung allein aus Lohnpfaendung B. Mueller braucht 272 Monate fuer 267.569,33 EUR - die dingliche ZVG-Vollstreckung ist der wirtschaftlich entscheidende Strang.
