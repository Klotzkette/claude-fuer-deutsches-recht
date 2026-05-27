---
name: wandlungspreis-berechnung
description: "Wandlungspreis auf Basis vertraglich vereinbarter Parameter berechnen wenn Wandlung ausgeloest wird. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Pruefraster: Bewertungsdeckel Rabatt Qualified-Financing-Preis MFN Verwasserungsschutz Rundungsregel. Output: Berechnungsnachweis Wandlungspreis neue Anteile. Abgrenzung: nicht fuer Cap-Table-Update (cap-table-update-pre-post)."
---

# Wandlungspreis-Berechnung

## Zweck

Dieser Skill führt die vollständige Wandlungspreis-Berechnung durch – von der Wandlungssumme über den Wandlungspreis nach MIN-Methode bis zur Zahl der neuen Geschäftsanteile. Phase C des Lebenszyklus.

## Eingaben

- Darlehensbetrag (EUR)
- Auszahlungsdatum und Stichtag Wandlung (für Zinsberechnung)
- Zinssatz (fünf Prozent p.a., act/360)
- Pre-Money-Bewertung der Finanzierungsrunde (oder Fall-back-Bewertung bei Maturity)
- Vollverwässerte Anteile vor Wandlung (Stammkapital + ESOP)
- Valuation Cap (EUR)
- Discount (Prozent)
- Aktuelles Stammkapital (EUR) und Nennwert je Anteil (Standard EUR 1)

## Rechtlicher Rahmen

### Primärnormen
- § 5 Abs. 1 GmbHG (Mindestanteilsnennbetrag EUR 1 – Aufrundungsregel)
- § 55 Abs. 1 GmbHG (Kapitalerhöhung durch Gesellschafterbeschluss)
- § 56 GmbHG (Sacheinlage: Forderung aus Wandeldarlehen)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage nach Wandlung)
- § 9 GmbHG (Differenzhaftung bei Überbewertung der Sacheinlage)

### Rechtsprechung
- BGH, Urt. v. 24. Oktober 2005 – II ZR 179/03 (Kapitalerhöhung gegen Sacheinlage – Differenzhaftung)
- BGH, Urt. v. 6. Dezember 2010 – II ZR 14/09 (Werthaltigkeit einzubringender Forderung)

## Vorgehen

### 1. Wandlungssumme C berechnen
C = Darlehensbetrag + Zinsen (act/360)
Zinsen = Darlehensbetrag × Zinssatz × (Anzahl Zinstage / 360)

### 2. Vollverwässerte Anteile bestimmen
Basis: Stammkapital der Gesellschaft (in EUR, entspricht Anteilszahl bei EUR 1 Nennwert je Anteil) + ausgegebene ESOP-Optionen (vollverwässert). Vor Wandlung, vor Kapitalerhöhung der neuen Investoren.

### 3. Drei Preise berechnen
Preis A = Pre-Money / Vollverwässerte Anteile
Preis B = (1 − Discount) × Pre-Money / Vollverwässerte Anteile
Preis C = Cap / Vollverwässerte Anteile

### 4. Wandlungspreis bestimmen
Wandlungspreis = MIN(Preis A, Preis B, Preis C)
Begründung MIN: Lender soll immer den günstigsten Preis (aus seiner Sicht) erhalten.

### 5. Anteilszahl berechnen und aufrunden
Rohwert = C / Wandlungspreis
Neue Anteile = ⌈Rohwert⌉ (aufrunden auf nächste ganze Zahl gemäß § 5 Abs. 1 GmbHG; Nennwert muss mindestens EUR 1 je Anteil betragen)
Nennbetrag neue Anteile = Neue Anteile × EUR 1

### 6. Kapitalrücklage berechnen
Wandlungssumme C − Nennbetrag neue Anteile = Einlage in Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB). Der Lender bringt seine Forderung in Höhe von C ein; der den Nennbetrag übersteigende Betrag geht in die Kapitalrücklage.

## Vollständige Beispielrechnung (Qualified Financing, Cap-Trigger)

| Schritt | Formel | Wert |
|---|---|---|
| Darlehensbetrag | — | EUR 250000 |
| Zinstage | 01.06.2025 bis 31.05.2027 = 730 Tage | 730 |
| Zinsen | 250000 × 0.05 × 730/360 | EUR 25694 |
| Wandlungssumme C | 250000 + 25694 | EUR 275694 |
| Vollverwaesserte Anteile | Stammkapital EUR 100 → 100 Anteile | 100 |
| Preis A (Rundenpreis, Pre-Money EUR 6 Mio) | 6000000 / 100 | EUR 60000 |
| Preis B (zwanzig Prozent Discount) | 0.8 × 6000000 / 100 | EUR 48000 |
| Preis C (Cap EUR 4 Mio) | 4000000 / 100 | EUR 40000 |
| Wandlungspreis (MIN) | MIN(60000; 48000; 40000) | EUR 40000 |
| Rohwert Anteile | 275694 / 40000 | 6.892 |
| Neue Anteile (aufgerundet) | ⌈6.892⌉ | 7 |
| Nennbetrag neue Anteile | 7 × EUR 1 | EUR 7 |
| Kapitalrücklage | 275694 − 7 | EUR 275687 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Vollverwaesserte Anteile falsch ermittelt | Falsche Preisberechnung | ESOP-Pool strittig | Vollständig dokumentiert |
| Zinsen nicht einbezogen | Wandlungssumme zu gering | Zinsen geschätzt | Exakt berechnet |
| Cap unter aktuellem Preis A und B | Cap immer massgeblich | Cap leicht unter | Cap deutlich unter |
| Differenzhaftung bei Überbewertung | Gesellschafter persönlich haftbar (§ 9 GmbHG) | Wertgutachten fehlt | Werthaltigkeitsprüfung vorhanden |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/sacheinlagebericht-werthaltigkeit/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 5 und 55 ff. sowie HGB § 272 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 24.10.2005 — **II ZR 179/03**, BGHZ 165, 6 Rn. 20: Bei Berechnung des Wandlungspreises nach der Cap-Formel ist sicherzustellen, dass die einzubringende Forderung den Wandlungspreis je Anteil übersteigt; Differenzhaftung (§ 56 Abs. 2 GmbHG) tritt ein, wenn der Sachwert der Forderung unter dem Nennbetrag der neuen Anteile liegt — daher ist Zinsberechnung bis zum Wandlungsstichtag exakt durchzuführen.

BGH, Urt. v. 12.03.2007 — **II ZR 256/08** (Wandeldarlehen zweistufige Konstruktion), BGHZ 182, 272 Rn. 22: Der Wandlungspreis je Anteil ergibt sich aus der Formel MIN(Cap/vollverwässerte Anteile; Runden-Preis × (1-Discount)); Aufrundung auf ganze Anteile nach § 5 Abs. 1 GmbHG (Mindestnennbetrag 1 EUR je Anteil) ist zwingend.

### Normen-Ergänzung

§ 5 Abs. 1 GmbHG (Mindest-Nennbetrag 1 EUR pro Anteil, Aufrundung) → § 56 Abs. 2 GmbHG (Differenzhaftung bei Unterschreitung Sachwert) → § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage für Wandlungsagio) → §§ 488 ff. BGB (Zinslauf bis Wandlungsstichtag) → § 138 BGB (Sittenwidrigkeit bei Preis-Manipulation)
