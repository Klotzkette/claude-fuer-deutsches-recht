---
name: bwa-kapitalflussrechnung-iduk
description: "Kapitalflussrechnung nach indirekter Methode aus BWA und Bilanz. Anwendungsfall Jahresabschluss Bankreporting Sanierungskonzept Konzernabschluss. Methodik DRS 21 indirekte Ableitung aus Jahresueberschuss Mittelfluss laufende Geschäftstätigkeit Investitionstätigkeit Finanzierungstätigkeit. Output..."
---

# Kapitalflussrechnung nach DRS 21 indirekte Methode

## Fachlicher Anker

- **Normen:** § 6a, § 297 HGB, § 19 InsO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die Kapitalflussrechnung ist nach DRS 21 Pflichtbestandteil des Konzernabschlusses (§ 297 HGB) und freiwillig für Einzelabschluesse. Die indirekte Methode leitet den Cashflow aus dem Jahresueberschuss durch Eliminierung nicht-zahlungswirksamer Posten und Beruecksichtigung von Bilanzveraenderungen ab. Sie ist Bank-Standard, Bestandteil von Sanierungskonzepten nach IDW S 6 und Grundlage der Fortbestehensprognose nach § 19 InsO.

## Kaltstart-Rueckfragen

1. Welcher Anlass — Jahresabschluss Konzern, Sanierungskonzept, Bank-Reporting, freiwillige Erstellung?
2. Liegen Bilanz Anfang und Ende sowie BWA/GuV vor?
3. Welche Methode — indirekt (Standard) oder direkt (selten)?
4. Welche Konsolidierung — Einzel oder Konzern?
5. Sondereffekte (Anlagenverkauf, Sondertilgung, Kapitalerhoehung)?
6. Welcher Fonds — Liquide Mittel (Bank+Kasse), Finanzmittel weiter (incl. Wertpapiere)?
7. Welche Vorperiode wird vergleichend dargestellt?
8. Adressat — interne Steuerung, externe Veroeffentlichung, Sanierungsgutachten?

## Rechtlicher Rahmen

### Primaernormen

**§ 297 HGB** — Konzernabschluss; Kapitalflussrechnung verpflichtend.

**§ 264 HGB** — Aufstellungspflicht Einzelabschluss; Kapitalflussrechnung freiwillig.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 19 Abs. 2 InsO** — Fortbestehensprognose mit Liquiditaetsbetrachtung.

### Standards

- DRS 21 — Kapitalflussrechnung (gilt für Konzernabschluss; analog für Einzelabschluss).
- IDW S 6 — Sanierungskonzept; Cashflow-Rechnung Pflicht.
- IDW PS 305 — Risikofrueherkennung.
- IAS 7 — Cashflow Statements (bei internationaler Konzern-Reporting).

## Workflow

### Phase 1 — Datenbasis

- Bilanz Anfang und Ende (zwei Stichtage).
- GuV/BWA der Periode.
- Anlagenspiegel mit Zugaengen, Abgaengen, AfA.
- Eigenkapitalveraenderungsrechnung.
- Detail-Konten für ausserordentliche Posten.

### Phase 2 — Struktur DRS 21

```
KAPITALFLUSSRECHNUNG nach DRS 21 (indirekte Methode)

I. CASHFLOW AUS LAUFENDER GESCHAEFTSTAETIGKEIT
 Jahresueberschuss/Fehlbetrag [X]
 +/- Abschreibungen/Zuschreibungen Anlagevermoegen [X]
 +/- Veraenderung Rueckstellungen [X]
 +/- Sonstige nicht-zahlungswirksame Aufwendungen/Ertraege [X]
 +/- Veraenderung Vorraete [X]
 +/- Veraenderung Forderungen LuL [X]
 +/- Veraenderung sonstige Aktiva [X]
 +/- Veraenderung Verbindlichkeiten LuL [X]
 +/- Veraenderung sonstige Passiva [X]
 +/- Gezahlte/Erstattete Ertragsteuern [X]
 = Cashflow aus laufender Geschaeftstaetigkeit [X]

II. CASHFLOW AUS INVESTITIONSTAETIGKEIT
 - Auszahlungen für Investitionen Sachanlagen [X]
 - Auszahlungen für Investitionen immat. WG [X]
 - Auszahlungen für Investitionen Finanzanlagen [X]
 + Einzahlungen aus Abgang Sachanlagen [X]
 + Einzahlungen aus Abgang Finanzanlagen [X]
 = Cashflow aus Investitionstaetigkeit [X]

III. CASHFLOW AUS FINANZIERUNGSTAETIGKEIT
 + Einzahlungen aus Kapitalerhoehung [X]
 + Aufnahme Darlehen Kreditinstitute [X]
 - Tilgung Darlehen Kreditinstitute [X]
 - Ausschuettungen an Gesellschafter [X]
 = Cashflow aus Finanzierungstaetigkeit [X]

IV. VERAENDERUNG FINANZMITTELFONDS [X]
 + Finanzmittelfonds zu Beginn der Periode [X]
 = Finanzmittelfonds am Ende der Periode [X]
```

### Phase 3 — Ableitung Bewegungen

| Posten | Ermittlung |
|---|---|
| Veraenderung Vorraete | Vorraete Ende minus Vorraete Anfang (Aktiva-Erhoehung mindert Cashflow) |
| Veraenderung Forderungen | Forderungen Ende minus Anfang (Erhoehung mindert Cashflow) |
| Veraenderung Verbindlichkeiten | Verbindlichkeiten Ende minus Anfang (Erhoehung erhoeht Cashflow) |
| Abschreibungen | Aus Anlagenspiegel; nicht-zahlungswirksam → wird zurueckaddiert |
| Veraenderung Rueckstellungen | Rueckstellungen Ende minus Anfang; nicht-zahlungswirksam |

### Phase 4 — Sondereffekte

- Anlagenverkauf: Differenz Buchwert/Verkaufserloes als Sonderposten; Buchgewinn aus laufendem Cashflow herausrechnen.
- Sondertilgung: in Finanzierungstaetigkeit, nicht in laufender Geschäftstaetigkeit.
- Kapitalerhoehung: in Finanzierungstaetigkeit, nicht Ergebnis.
- Ausschuettungen: in Finanzierungstaetigkeit, kein Aufwand.

### Phase 5 — Plausibilitaetspruefung

- Endsaldo Finanzmittelfonds = Bilanzposten "Liquide Mittel" zum Endstichtag? (Mussmatch sein.)
- Vergleich Vorjahr: aussergewoehnliche Veraenderungen kenntlich machen.
- Zusammenwirken mit Bewegungsbilanz prüfen.

### Phase 6 — Erläuterung und Versand

- Erläuterung wesentlicher Posten in Anhang (insb. Investitionstaetigkeit).
- Bei Bank-/Investor-Reporting Praesentationsformat (eine Seite plus Erläuterung).
- Sanierungskonzept IDW S 6: integriert mit Plan-Cashflow 24 Monate.

## Strategie und Praxis-Tipps

- Bei Mittelstand: Kapitalflussrechnung auf Wunsch des Bank-Partners als Standard.
- Konzernabschluss: Pflicht nach DRS 21 — nicht verhandelbar.
- Bei IFRS-orientierten Konzernen: parallel IAS 7 darstellen.
- Praxis-Tipp: Cashflow aus laufender Geschäftstaetigkeit ist Indikator für organische Ertragskraft; deutlich unter Jahresueberschuss = Working-Capital-Problem.
- StBVV: Kapitalflussrechnung als separater Auftrag (Anhang Jahresabschluss).
- DATEV-Tipp: DATEV Konzernabschluss/Jahresabschluss-Modul mit Kapitalflussrechnung; bei Einzelabschluss manuelle Erstellung.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6, IDW PS 305.
- IAS 7 (international).
- InsO § 19.
