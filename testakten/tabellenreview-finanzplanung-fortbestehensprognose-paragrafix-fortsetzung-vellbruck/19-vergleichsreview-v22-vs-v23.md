# 19 — Vergleichsreview v22 vs. v23

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Datum:** 13. Januar 2026

---

## Methodik

Der Reviewer hat beide Versionen (v22: 28.11.2025, v23: 05.01.2026) parallel geöffnet und einen systematischen Diff aller Zellen durchgeführt. Werkzeug: eigenes Python-Script auf Basis von openpyxl (xlsxdiff-Methode). Geprüft: alle Blätter außer versteckte Sheets (in v22 nicht vorhanden).

---

## Übersicht geänderter Bereiche

| Blatt | Anzahl Zellveränderungen | Davon formelrelevant | Dokumentiert im Changelog? |
|---|---|---|---|
| PLAN-GuV | 18 | 7 | Teilweise |
| ZINS-SCHULDEN | 3 | 2 | Nein (kritisch) |
| PLAN-CF | 11 | 5 | Teilweise |
| PLAN-BILANZ | 8 | 3 | Ja |
| SZENARIEN | 2 | 0 | Ja (Notiz-Update) |
| ZUSAMMENFASSUNG | 5 | 0 | Ja (Design) |
| PARAM | 0 | 0 | — |
| PERSONAL | 6 | 4 | Teilweise |

---

## Kritische Einzeldiffs

### 1. ZINS-SCHULDEN!C5 (kritisch, Finding 4)

```
v22: =PARAM!B12    (Formelverknüpfung, Wert: 6,2%)
v23: 0,049          (Hardcoded, Wert: 4,9%)
```

### 2. PLAN-CF!H8 (Finding 2)

```
v22: =PARAM!B19    (Formelbezug DSO)
v23: 42             (Hardcoded)
```

### 3. PLAN-GuV!F22 (Finding 2)

```
v22: =PARAM!B5     (Wachstumsrate Q3 2026)
v23: 0,072          (Hardcoded)
```

### 4. PLAN-BILANZ!D55 (Finding 5)

```
v22: 460 (korrekte Rückstellung)
v23: 480 + neue Zeile D56 mit 480 (Doppelbuchung)
```

### 5. VBA Module1 (Finding 9)

```
v22: nicht vorhanden
v23: vorhanden, enthält UpdateSollwerte Prozedur
```

---

## Gesamtauswirkung der v22→v23 Änderungen auf Liquiditätsergebnis

| Änderung | Auswirkung auf Liquiditätsprognose 2026–2027 |
|---|---|
| Zinssatzabsenkung ZS!C5 | +186 TEUR (zu positiv) |
| Hardcoded DSO (CF!H8) | +95 TEUR (zu positiv) |
| Hardcoded Wachstum (GuV!F22) | +38 TEUR (zu positiv) |
| Doppelrückstellung BILANZ | kein direkter Liquiditätseffekt |
| Übrige Änderungen | +22 TEUR (netto zu positiv) |
| **Summe Verzerrung v23 ggü. v22** | **+341 TEUR (zu positiv)** |

Das bedeutet: v23 weist gegenüber v22 ein um 341 TEUR besseres Liquiditätsergebnis aus, das auf methodisch nicht belastbaren Änderungen beruht.

**Quellen:** IDW S 11 Tz. 34 (Dokumentation von Modelländerungen), [https://www.idw.de](https://www.idw.de); HGB § 238 (Buchführungspflicht): [https://dejure.org/gesetze/HGB/238.html](https://dejure.org/gesetze/HGB/238.html).
