# 10 — Finding 3: Falsche Summenformel Bilanzsumme

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-03
**Schwere:** Hoch
**Entdeckt:** 11. Januar 2026

---

## Sachverhalt

Im Blatt `PLAN-BILANZ` enthält die Zelle `PB!B44` (Bilanzsumme Aktiva 2026) eine fehlerhafte SUM-Formel:

```
IST-Formel:  =SUM(PB!B12:PB!B42)
Korrekt:     =SUM(PB!B12:PB!B43)
```

Die Zelle `PB!B43` enthält "Sonstige Vermögensgegenstände" mit einem Planwert von 127 TEUR für 2026 und wurde bei der letzten Formelanpassung (Einfügen einer neuen Zeile) nicht in den Summenbereich aufgenommen.

---

## Auswirkung

| Position | Wert im Modell v23 | Korrekter Wert | Abweichung |
|---|---|---|---|
| Bilanzsumme Aktiva 2026 (TEUR) | 6.820 | 6.947 | –127 TEUR |
| Bilanzsumme Passiva 2026 (TEUR) | 6.947 | 6.947 | 0 |
| Differenz Aktiva/Passiva | –127 TEUR | 0 | Bilanz nicht ausgeglichen |

Die Bilanz ist in Modell v23 nicht ausgeglichen. Dies ist ein fundamentaler Fehler, der eine HGB-konforme Darstellung unmöglich macht.

---

## Historischer Kontext

Gemäß Versionshistorie war diese Zelle in v19 zuletzt vollständig geprüft worden; v20 wurde eine neue Zeile (sonstige Vermögensgegenstände) eingefügt, ohne den SUM-Bereich anzupassen. Dieser Fehler ist seitdem in v20–v23 vorhanden.

---

## Empfehlung

Sofortige Korrektur `PB!B44` auf `=SUM(PB!B12:PB!B43)`. Parallelprüfung: alle weiteren SUM-Formeln in `PLAN-BILANZ` auf korrekte Bereichsabgrenzung prüfen (insbesondere `PB!F44` für 2027 und Passiva-Saldo `PB!B78`).

**Verantwortlich:** CFO / Modellentwickler.
**Frist:** 1 Arbeitstag (sofortiger Fix, minimaler Aufwand).

**Quellen:** HGB § 266 (Bilanzgliederung): [https://dejure.org/gesetze/HGB/266.html](https://dejure.org/gesetze/HGB/266.html); IDW S 11 Tz. 27, [https://www.idw.de](https://www.idw.de).
