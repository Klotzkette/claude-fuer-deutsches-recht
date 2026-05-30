# 08 — Finding 1: Zirkulärer Bezug Cashflow / Zinsen

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-01
**Schwere:** Kritisch
**Entdeckt:** 11. Januar 2026

---

## Sachverhalt

Im Blatt `PLAN-CF` (Cashflow-Prognose) besteht ein zirkulärer Bezug über folgende Zellkette:

```
PLAN-CF!E14 (Zinsaufwand geplant, monatlich)
  verweist auf: ZINS-SCHULDEN!D9 (kalkulierter Zinsaufwand)
    wobei D9 = ZS!C5 * LIQUIDITAET!C18
      wobei LIQUIDITAET!C18 (Kontokorrent-Inanspruchnahme) = f(PLAN-CF!B4 - PLAN-CF!E14)
```

Das Modell löst diese Zirkularität durch aktivierte Iterationsrechnung (100 Iterationen, Toleranz 0,001). Bei Standard-Excel-Einstellungen (Iteration deaktiviert) läuft das Modell in einen Fehler.

---

## Auswirkung

Bei Deaktivierung der Iteration (Standardeinstellung) nimmt `PLAN-CF!E14` den Wert 0 an. Dies führt zu:

- Zinsaufwand 2026 im Modell: 0 EUR statt korrekt ca. 248 TEUR.
- Kumulierter Liquiditätsüberschuss 2026–2027: +418 TEUR statt korrigiert ca. +170 TEUR (ohne weitere Korrekturen).
- Das Modell-Ergebnis (positiv) ist direkt von der Iterationsaktivierung abhängig. Nicht jeder Empfänger hat diese Einstellung.

---

## Rechtliche Relevanz

Eine Fortbestehensprognose, die von Konfigurationseinstellungen des aufrufenden Programms abhängt und bei Standardeinstellungen einen Fehler oder falsches Ergebnis zeigt, erfüllt nicht die Anforderungen an Nachvollziehbarkeit und Verlässlichkeit gemäß IDW S 11 Tz. 22. Zudem begründet die Iterationsabhängigkeit ein Risiko nach HGB § 252 (Grundsatz ordnungsgemäßer Buchführung).

---

## Empfehlung

**Sofortmaßnahme:** Zirkularität durch direkte Berechnung auflösen (Zweistufenmodell: Vorperioden-Inanspruchnahme als Zinsbasis verwenden). Iterationsrechnung deaktivieren. Formelkette dokumentieren.

**Zeitplan:** Fix innerhalb von 3 Arbeitstagen vor Neuvorlage beim WP.

**Verantwortlich:** CFO Pellbach-Roosendaal / externer Modellentwickler.

**Quellen:** IDW S 11 Tz. 22–24, [https://www.idw.de](https://www.idw.de); HGB § 252, [https://dejure.org/gesetze/HGB/252.html](https://dejure.org/gesetze/HGB/252.html).
