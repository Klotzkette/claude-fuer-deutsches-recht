# 03 — Modellarchitektur: Eingangsblätter, Rechenblätter, Ausgabe

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Datum:** 09. Januar 2026

---

## Überblick Blattstruktur

Das Modell `PFX-FoBP-Modell-v23-final.xlsx` enthält 18 Arbeitsblätter, davon 2 versteckt (Finding 6). Farblegende CFO: grün = Eingabe, gelb = Berechnung, blau = Ausgabe.

| Nr. | Blattname | Typ | Bemerkung |
|---|---|---|---|
| 1 | DECKBLATT | Ausgabe | Versionskontrolle, Inhaltsverzeichnis |
| 2 | PARAM | Eingabe | Zentrale Parameter (Zinsen, Wachstumsraten, FTE) |
| 3 | ANNAHMEN | Eingabe | Narrative Annahmen, Sanierungsmaßnahmen |
| 4 | IST-GuV | Eingabe | Ist-GuV 2023, 2024, 2025 (vorläufig) |
| 5 | IST-BILANZ | Eingabe | Ist-Bilanzen 2023–2025 |
| 6 | IST-CF | Eingabe | Ist-Cashflow-Statements |
| 7 | PLAN-GuV | Berechnung | Plan-GuV 2026–2027, monatlich |
| 8 | PLAN-BILANZ | Berechnung | Plan-Bilanzen 12/2026, 12/2027 |
| 9 | PLAN-CF | Berechnung | Cashflow-Prognose monatlich (Finding 1: Zirkularität) |
| 10 | LIQUIDITAET | Berechnung | Monatliche Liquiditätsplanung, Kontokorrententwicklung |
| 11 | ZINS-SCHULDEN | Berechnung | Zinslastberechnung (Finding 4: falsche Annahme) |
| 12 | PERSONAL | Berechnung | FTE-Plan, Personalkosten, Abfindungen |
| 13 | INVESTITIONEN | Berechnung | Capex-Plan, AfA |
| 14 | SZENARIEN | Berechnung | Basisszenario (Finding 8: kein Stressszenario) |
| 15 | ZUSAMMENFASSUNG | Ausgabe | KPI-Dashboard, Kennzahlen |
| 16 | BRIDGE | Ausgabe | Plan-zu-IST-Bridge |
| 17 | _BACKUP_PARAM | **versteckt** | Finding 6: Alte Parametersätze v19 |
| 18 | _RESTPOSTEN | **versteckt** | Finding 6: Nicht aufgelöste Differenzposten |

---

## Datenflüsse zwischen Blättern

```
PARAM + ANNAHMEN
    |
    +---> PLAN-GuV ---> ZUSAMMENFASSUNG
    |         |               ^
    +---> PLAN-BILANZ         |
    |         |               |
    +---> ZINS-SCHULDEN ------+
    |         |
    +---> PLAN-CF (ZIRKULARITÄT mit ZINS-SCHULDEN — Finding 1)
    |         |
    +---> LIQUIDITAET -> BRIDGE
    |
    +---> PERSONAL -> PLAN-GuV
    |
    +---> INVESTITIONEN -> PLAN-BILANZ
```

Der kritische Zirkularbezug zwischen `PLAN-CF` (Zelle CF!E14) und `ZINS-SCHULDEN` (Zelle ZS!D9) ist in Finding 1 detailliert dokumentiert.

---

## Größenordnung

| Kennzahl | Wert |
|---|---|
| Gesamt-Zellen mit Inhalt | ca. 14.200 |
| Formeln gesamt | ca. 2.400 |
| Davon volatile Formeln (INDIRECT, OFFSET) | 37 |
| Hardcoded Werte in Rechenbereichen | 47 (Finding 2) |
| Externe Verknüpfungen | 0 (korrekt) |
| Makros (VBA) | 1 Modul (Finding 9) |
| Benannte Bereiche (Named Ranges) | 84 |
| Versteckte Blätter | 2 (Finding 6) |

---

## Strukturbewertung (Vorläufig)

**Positiv:**
- Klare Blattfarbtrennung Eingabe/Berechnung/Ausgabe.
- Keine externen Verknüpfungen (kein Link-Risiko).
- Named Ranges durchgehend verwendet.

**Negativ:**
- Zirkulärer Bezug zwischen CF und Zinsblatt (kritisch, Finding 1).
- 47 Hardcoded-Werte in Rechenbereichen (Finding 2).
- Versteckte Blätter mit unaufgelösten Differenzen (Finding 6).
- Stress-Szenario fehlt (Finding 8).
- VBA-Makro mit Sollwertüberschreibung (Finding 9).

**Quellen:** IDW S 11, Tz. 22 ff. (Anforderungen an Modellarchitektur), abrufbar unter [https://www.idw.de](https://www.idw.de).
