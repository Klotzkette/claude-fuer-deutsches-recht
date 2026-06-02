# 07 — Review-Achse 3: Formelarchitektur / Zirkularität

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Datum:** 11./12. Januar 2026

---

## Prüfgegenstand

Die Formelarchitektur-Prüfung untersucht:
- Zirkuläre Bezüge (Circular References) und deren Behandlung.
- Verwendung volatiler Funktionen (INDIRECT, OFFSET, NOW, TODAY).
- Hardcoded-Werte in Rechenbereichen.
- Namenskonventionen und Dokumentation der Named Ranges.
- VBA-Makros und deren Einfluss auf Modellintegrität.

---

## Zirkuläre Bezüge

Excel-Iterationsrechnung ist im Modell v23 aktiviert (Maximaliterationen: 100, Änderungstoleranz: 0,001). Dies ist eine verbreitete, aber riskante Methode zur Behandlung von Zirkularbezügen in Finanzmodellen.

**Identifizierter Zirkularbezug (Finding 1):**

```
PLAN-CF!E14 (Zinsaufwand CF-Planung)
    = ZINS-SCHULDEN!D9 (Zinsberechnung auf Kontokorrentbasis)
    = f(LIQUIDITAET!C18, ZINS-SCHULDEN!C5)
    wobei LIQUIDITAET!C18 = f(PLAN-CF!E14)
```

Der Zirkularbezug ist nur durch Iterationsrechnung lösbar. Bei Deaktivierung der Iteration springt das Modell auf Fehlerwert #WERT! bzw. auf den Wert 0 in `PLAN-CF!E14`, was zu einem um ca. 186 TEUR zu hohen Cashflow führt.

---

## Volatile Funktionen

37 volatile Funktionen gefunden. Volatile Funktionen werden bei jeder Berechnung neu ausgewertet und können zu instabilem Modellverhalten führen.

| Funktion | Anzahl Vorkommen | Blatt | Risiko |
|---|---|---|---|
| INDIRECT | 22 | PLAN-GuV, SZENARIEN | Mittel: Verweisbruch bei Umbenennung |
| OFFSET | 12 | LIQUIDITÄT, PLAN-CF | Mittel: Bereichsverschiebung |
| NOW / TODAY | 3 | DECKBLATT | Niedrig: nur Datumsanzeige |

---

## Hardcoded-Werte in Rechenbereichen

47 Hardcoded-Werte wurden in Blättern identifiziert, die gemäß Modellkonvention als Rechenblätter (gelb) klassifiziert sind. Die Verwendung von Hardcoded-Werten in Rechenbereichen verstößt gegen Good-Practice-Anforderungen von Finanzmodellen und erschwert die Nachvollziehbarkeit (Finding 2, detailliert in Aktenstück 09).

---

## Named-Range-Qualität

| Kriterium | Befund |
|---|---|
| Konvention | Gemischt (Camelcase und GROSSBUCHSTABEN, nicht einheitlich) |
| Dokumentation | 84 Named Ranges; Beschreibungsfeld leer bei 61 von 84 |
| Redundanzen | 3 doppelt definierte Ranges identifiziert |
| Verwaiste Ranges | 7 Ranges referenzieren gelöschte Bereiche |

---

## VBA-Makro (Finding 9)

Ein VBA-Modul `Module1` enthält eine Prozedur `UpdateSollwerte`, die beim Öffnen der Datei ausgeführt wird und Planwerte in `PLAN-GuV` und `LIQUIDITAET` überschreibt. Dies untergräbt die Modellintegrität (Finding 9, detailliert in Aktenstück 16).

---

## Gesamtbewertung Formelarchitektur

Die Formelarchitektur weist multiple strukturelle Schwächen auf. Die Kombination aus Zirkularbezug mit Iterationsrechnung, volatilen Funktionen, Hardcoded-Werten und einem aktiven VBA-Makro macht das Modell v23 in seiner aktuellen Form als Grundlage für eine IDW-S-11-konforme Fortbestehensprognose ungeeignet.

**Quellen:** IDW S 11 Tz. 22–42, [https://www.idw.de](https://www.idw.de); FAST Financial Modelling Standard, [https://www.fast-standard.org](https://www.fast-standard.org).
