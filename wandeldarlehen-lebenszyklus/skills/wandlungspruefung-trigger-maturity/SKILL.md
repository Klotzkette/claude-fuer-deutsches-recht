---
name: wandlungspruefung-trigger-maturity
description: "Pruefung ob Ablauf der Festen Laufzeit (Maturity) als Wandlungsausloeser eingetreten ist und kein qualifying event zuvor eingetreten ist. Wandlung auf Basis Fall-back-Bewertung. Default-Bewertung falls keine vereinbart. Wahlrecht Lender zwischen Wandlung und Faelligstellung bei vorangegangenem Liquidationsereignis."
---

# Wandlungsprüfung – Trigger Maturity (Laufzeitablauf)

## Zweck

Dieser Skill prüft den Maturity-Trigger: Ist die Feste Laufzeit abgelaufen, ohne dass ein qualifizierendes Wandlungsereignis eingetreten ist? Wenn ja, erfolgt Wandlung auf Basis der Fall-back-Bewertung. Phase C des Lebenszyklus.

## Eingaben

- Wandeldarlehensvertrag (§§ 2.1, 4.2 lit. e, 4.10)
- Startdatum der Festen Laufzeit (Datum vollständiger Unterzeichnung)
- Enddatum (Startdatum plus zwei Jahre)
- Fall-back-Bewertung aus § 4.10 (Pre-Money EUR bei Maturity)
- Darlehensbetrag + aufgelaufene Zinsen zum Maturity-Stichtag
- Ist innerhalb der Laufzeit ein Wandlungsereignis nach § 4.2 lit. b bis d eingetreten?

## Rechtlicher Rahmen

### Primärnormen
- § 2.1 Wandeldarlehensvertrag (Feste Laufzeit – kein Kündigungsrecht)
- § 4.2 lit. e Wandeldarlehensvertrag (Ablauf Feste Laufzeit als Wandlungsereignis)
- § 4.10 Wandeldarlehensvertrag (Fall-back-Bewertung bei Maturity)
- § 5 Abs. 1 GmbHG (Mindestanteilsnennwert EUR 1)
- § 271 BGB (Fälligkeit bei bestimmter Zeit)

### Rechtsprechung
- BGH, Urt. v. 7. März 2013 – IX ZR 7/12 (Fälligkeit und Insolvenz bei Wandeldarlehen)
- BGH, Urt. v. 29. Januar 2015 – IX ZR 279/13 (Laufzeit und Rückzahlungspflicht Wandeldarlehen)

## Vorgehen

### 1. Laufzeitprüfung
Startdatum = Datum vollständiger Unterzeichnung durch alle vier Parteien (§ 2.1). Enddatum = Startdatum + zwei Jahre (kalendarisch, keine Bankarbeitstage). Ist das aktuelle Datum ≥ Enddatum? → Maturity eingetreten.

### 2. Prüfung vorangegangener Ereignisse (§ 4.10 Satz 2)
Ist innerhalb der Laufzeit ein Liquidationsereignis (§ 4.2 lit. b bis d) eingetreten? Wenn ja: Lender hat Wahlrecht zwischen Wandlung (zu Fall-back-Bewertung) und Fälligstellung (Rückzahlung + Zinsen, § 2.5).

### 3. Fall-back-Bewertung anwenden
Wandlungspreis = Fall-back-Bewertung (Pre-Money EUR) / Anteile vor Wandlung (vollverwässert).
Wandlungssumme C = Darlehen + aufgelaufene Zinsen (Stichtag = Enddatum).
Neue Anteile = C / Wandlungspreis (aufrunden auf nächsten EUR, § 5 Abs. 1 GmbHG).

### 4. Wandlungserklärung auslösen oder Fälligstellung wählen
Falls nur Maturity ohne vorangegangenes Liquidationsereignis: automatische Wandlung, Lender erklärt Wandlung per Textform. Falls vorangegangenes Liquidationsereignis: Lender wählt innerhalb zwei Wochen.

### 5. Zinsen berechnen (Stichtag Maturity)
Zinsen = Darlehensbetrag × Zinssatz × (Tage ab Auszahlung bis Enddatum / 360). Act/360-Basis.

### 6. Übergabe an Kapitalerhöhungsprozess
Nach Wandlungserklärung: Gesellschaft beruft Gesellschafterversammlung ein (§ 4.9). Skills `gesellschafterbeschluss-kapitalerhoehung` und `notar-paket-uebermittlung` aufrufen.

## Beispielrechnung Maturity

| Parameter | Wert |
|---|---|
| Darlehensbetrag | EUR 250000 |
| Laufzeit | 2 Jahre = 730 Tage |
| Zinsen (730 Tage, fünf Prozent) | EUR 250000 × 0.05 × (730/360) = EUR 25694 |
| Wandlungssumme C | EUR 275694 |
| Fall-back-Bewertung (Pre-Money) | EUR 4000000 |
| Anteile vor Wandlung | 100 |
| Wandlungspreis | EUR 40000 je Anteil |
| Neue Anteile | 275694 / 40000 = 6.89 → 7 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine Fall-back-Bewertung vereinbart | Wandlungsbetrag unbestimmt | Grobe Schätzung | Klarer EUR-Wert |
| Gesellschaft in Insolvenz bei Maturity | Wandlung blockiert, Rangrücktritt greift | Insolvenzantrag gestellt | Gesellschaft solvent |
| Lender will weder wandeln noch zahlen | Unklarheit über Rechtslage | Verhandlung läuft | Klares Wahlrecht ausgeübt |
| Laufzeitende strittig | Unterzeichnungsdatum unklar | Näherungsdatum | Unterzeichnungsdatum belegt |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-liquidation/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 55 ff. aktualisieren.
