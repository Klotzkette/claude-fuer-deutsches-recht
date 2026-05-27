---
name: stb-bwa-statische-liquiditaet-kennzahlen
description: "Statische Liquiditaetskennzahlen Liquiditaet 1 2 3 Grades aus BWA und Bilanz. Anwendungsfall Quartalsauswertung Bankreporting Krisenfrueherkennung. Methodik Working Capital Aufstellung Anlagendeckung Kennzahlen. Output Liquiditaets-Kennzahlenblatt Bewertung Ampel."
---

# Statische Liquiditaetskennzahlen — 1. 2. 3. Grades

## Kernsachverhalt

Statische Liquiditaetskennzahlen geben einen Schnappschuss der Zahlungsfaehigkeit zum Stichtag. Sie sind keine vollwertige Liquiditaetsplanung (dynamisch), aber Standardinstrument fuer Bank-Reporting, Quartals-Pruefung und erste Krisenfrueherkennung. Der Steuerberater berechnet sie aus Bilanz und SuSa und bewertet sie nach branchenueblichen Schwellenwerten. Bei Krisenmandanten ist die Liquiditaet 1. Grades unter 100 Prozent oft erster Indikator fuer § 17 InsO-Risiko.

## Kaltstart-Rueckfragen

1. Welche Stichtag — Monats-, Quartals- oder Jahresstichtag?
2. Liegt aktuelle SuSa und Bilanz vor?
3. Welche Kreditlinien (Kontokorrent, langfristig)?
4. Welche Verbindlichkeiten kurzfristig (< 1 Jahr) vs. langfristig?
5. Sind Forderungen werthaltig (keine grossen Einzelrisiken)?
6. Welche Vorraete (Umschlaghaeufigkeit)?
7. Welche Branche — branchentypische Schwellenwerte differieren?
8. Welcher Verwendungszweck — interne Steuerung, Bank, Sanierungsgutachten?

## Rechtlicher Rahmen

### Primaernormen

**§ 17 InsO** — Zahlungsunfaehigkeit (BGH BGHZ 163, 134: 10-Prozent-Luecke, 3-Wochen-Frist).

**§ 19 InsO** — Ueberschuldung mit Fortbestehensprognose.

**§ 252 HGB** — Going-concern.

**§ 102 StaRUG** — Hinweispflicht.

**§ 91 Abs. 2 AktG / analog GmbH** — Risikofrueherkennung.

### Standards

- IDW S 11 — Beurteilung Insolvenzeroeffnungsgruende.
- IDW S 6 — Sanierungskonzept.
- BBE-Branchenkennzahlen.

## Workflow

### Phase 1 — Datenbasis

- Bilanz zum Stichtag.
- SuSa mit Saldenstand kurzfristig vs. langfristig.
- OPOS-Listen Debitoren und Kreditoren.
- Kreditvertraege mit Linien-Limit und ausnutzungen.

### Phase 2 — Berechnung Kennzahlen

```
LIQUIDITAET 1. GRADES (Barliquiditaet, Cash Ratio):
  Liquide Mittel (Bank+Kasse) / kurzfristige Verbindlichkeiten

LIQUIDITAET 2. GRADES (einbeziehbare Liquiditaet, Quick Ratio):
  (Liquide Mittel + kurzfristige Forderungen) / kurzfristige Verbindlichkeiten

LIQUIDITAET 3. GRADES (gesamte kurzfristige Liquiditaet, Current Ratio):
  Umlaufvermoegen / kurzfristige Verbindlichkeiten

WORKING CAPITAL:
  Umlaufvermoegen minus kurzfristige Verbindlichkeiten
  (sollte positiv sein; bei negativ = kritisches Signal)

ANLAGENDECKUNG I:
  Eigenkapital / Anlagevermoegen

ANLAGENDECKUNG II:
  (Eigenkapital + langfristiges Fremdkapital) / Anlagevermoegen
  (sollte ueber 100 Prozent sein, sonst Fristenkongruenz verletzt)
```

### Phase 3 — Schwellenwerte und Ampel

| Kennzahl | Gruen | Gelb | Rot |
|---|---|---|---|
| Liquiditaet 1. Grades | > 20 Prozent | 10-20 Prozent | < 10 Prozent |
| Liquiditaet 2. Grades | > 100 Prozent | 80-100 Prozent | < 80 Prozent |
| Liquiditaet 3. Grades | > 200 Prozent | 120-200 Prozent | < 120 Prozent |
| Working Capital | Positiv mit Reserve | Knapp positiv | Negativ |
| Anlagendeckung II | > 110 Prozent | 100-110 Prozent | < 100 Prozent |

(Hinweis: Schwellenwerte branchenabhaengig; Handel hat oft niedrigere Liquiditaet 3. Grades wegen schnellem Lagerumschlag.)

### Phase 4 — Interpretation

- Liquiditaet 1. Grades < 10 Prozent: Achtung — bei ueber 3 Wochen anhaltend, § 17 InsO-Pruefung erforderlich.
- Working Capital negativ: Umlaufvermoegen finanziert teils Anlagevermoegen — Fristenkongruenz verletzt, akute Liquiditaets-Spannung.
- Anlagendeckung II < 100 Prozent: Anlagevermoegen wird teils mit kurzfristigem Kapital finanziert — strukturelles Risiko.
- Kreditlinien einbeziehen: ungenutzte Linien erhoehen "verfuegbare Mittel" der Liquiditaet 1. Grades.

### Phase 5 — Beratungsempfehlung

- Bei roter Ampel Liquiditaet 1. Grades: dynamische Liquiditaetsplanung (3-Wochen) sofort.
- Bei roter Ampel Anlagendeckung II: Umfinanzierung pruefen (kurzfristige in langfristige Schulden umwidmen).
- Bei negativem Working Capital: Sondergespraech mit Bank.

### Phase 6 — Reporting

- Liquiditaets-Kennzahlenblatt im Quartalsbericht.
- Bei Krisensignalen Querverweis stb-liquiditaetsvorschau-3wochen und stb-bwa-sus-bilanz-pruefung.

## Output

- Liquiditaets-Kennzahlenblatt mit Ampel.
- Erlaeuterungstext.
- Empfehlungen zur Liquiditaetssteuerung.

## Strategie und Praxis-Tipps

- Statische Kennzahlen sind Schnappschuss — bei Krisensignalen IMMER dynamische Liquiditaetsplanung ergaenzen.
- Bei Banken: Liquiditaet 1. Grades und Working Capital sind Standard-Pruefungsfelder.
- Kreditlinien-Ausnutzung mit dokumentieren — "verfuegbare Reserve" ist Steuerungsgroesse.
- StBVV: Standardkennzahlen pauschaliert, dynamische Liquiditaetsplanung als Zusatzauftrag.
- DATEV-Tipp: Kennzahlen-Modul mit Standard-Liquiditaetsformeln; bei individuellen Branchen-Schwellen Anpassung.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaet.
- `stb-liquiditaetsvorschau-3-6-12-monate` — dynamische Liquiditaetsplanung.
- `stb-liquiditaetsvorschau-3wochen` — § 17 InsO-Pruefung.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- InsO §§ 17, 19.
- HGB §§ 252, 268.
- StaRUG § 102.
- BGH BGHZ 163, 134.
- IDW S 6, IDW S 11.
- BBE-Branchenkennzahlen.
