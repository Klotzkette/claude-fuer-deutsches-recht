# 09 — Finding 2: Hardcoded Werte statt Formeln

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-02
**Schwere:** Hoch
**Entdeckt:** 11. Januar 2026

---

## Sachverhalt

In den als Rechenblätter (gelb, Modellkonvention) klassifizierten Blättern wurden 47 Zellen identifiziert, in denen Formelbezüge durch direkte numerische Werte (Hardcoded) ersetzt wurden. Dies widerspricht der Modellkonvention und Best-Practice-Anforderungen.

---

## Aufstellung der schwerwiegendsten Hardcoded-Werte

| Blatt | Zelle | Hardcoded-Wert | Erwartete Formel | Auswirkung EUR |
|---|---|---|---|---|
| PLAN-GuV | F22 | 0,072 | =PARAM!B5 (Wachstumsrate Q3 2026) | ca. +38 TEUR zu optimistisch |
| PLAN-CF | H8 | 42 | =PARAM!B19 (DSO Forderungslaufzeit Tage) | ca. +95 TEUR Cashflow-Verschiebung |
| ZINS-SCHULDEN | C5 | 0,049 | =PARAM!B12 (Zinssatz) | –186 TEUR Zinslast (Finding 4) |
| LIQUIDITÄT | D11 | 350000 | =PARAM!B25 (Mindestliquidität) | Indirekte Auswirkung |
| PERSONAL | G18 | 3 | =PARAM!B31 (Abfindungsmonate) | ca. +310 TEUR fehlend (Finding 5) |

Weitere 42 Hardcoded-Werte geringerer Materialität dokumentiert im Findings-Register.

---

## Gesamtauswirkung

Die kumulierte Auswirkung der wesentlichen Hardcoded-Werte auf das Modellergebnis beläuft sich auf ca. +329 TEUR im ausgewiesenen Liquiditätsüberschuss (d.h. das Modell weist diesen Betrag zu positiv aus).

---

## Screenshot-Dokumentation

Annotierter Screenshot der Zellen `PLAN-CF!H5:H12` (Hardcoded-Werte gelb hinterlegt, Reviewer-Annotation) in `jpg/screenshot-finding-2-hardcoded.jpg`.

---

## Empfehlung

Alle 47 Hardcoded-Werte sind durch Formelbezüge auf den zentralen Parameterbereich (PARAM) zu ersetzen. Eine Vollständigkeitsprüfung ist durch den Modellentwickler schriftlich zu bestätigen.

**Verantwortlich:** CFO Pellbach-Roosendaal / externer Modellentwickler.
**Frist:** 5 Arbeitstage.

**Quellen:** FAST Financial Modelling Standard Tz. 4.2 (Input-Separation), [https://www.fast-standard.org](https://www.fast-standard.org); IDW S 11 Tz. 22 ff., [https://www.idw.de](https://www.idw.de).
