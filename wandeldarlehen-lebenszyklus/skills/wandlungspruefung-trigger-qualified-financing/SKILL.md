---
name: wandlungspruefung-trigger-qualified-financing
description: "Pruefung ob qualifizierte Finanzierungsrunde im Sinne des Wandeldarlehensvertrags eingetreten ist: Mindest-Bewertungsschwelle (Pre-Money EUR 4 Mio), Mindest-Investitionsvolumen (EUR 500000), Berechnung Wandlungspreis nach Discount oder Valuation Cap (MIN-Methode), Anteilsauswahl guenstigere Methode."
---

# Wandlungsprüfung – Trigger Qualified Financing

## Zweck

Dieser Skill prüft, ob ein Qualified-Financing-Trigger eingetreten ist, und berechnet den Wandlungspreis nach der MIN-Methode (Cap vs. Discount vs. Rundenpreis). Phase C des Lebenszyklus.

## Eingaben

- Wandeldarlehensvertrag (§ 4.2 lit. a, § 4.5)
- Vertragliche Schwellenwerte: Mindest-Pre-Money-Bewertung, Mindest-Investitionsvolumen
- Term Sheet oder Beteiligungsvertrag der Finanzierungsrunde mit: Pre-Money-Bewertung, Investitionsvolumen, Anteilszahl vor Runde (vollverwässert)
- Valuation Cap und Discount aus Wandeldarlehen
- Darlehensbetrag + aufgelaufene Zinsen (Stichtag)

## Rechtlicher Rahmen

### Primärnormen
- § 4.2 lit. a Wandeldarlehensvertrag (Qualified Financing als Wandlungsereignis)
- § 55 Abs. 1 GmbHG (Kapitalerhöhungsbeschluss – Voraussetzung für Wandlung)
- § 5 Abs. 1 GmbHG (Mindestnennbetrag Anteil EUR 1)
- § 272 Abs. 2 Nr. 4 HGB (Einlage in Kapitalrücklage)

### Rechtsprechung
- BGH, Urt. v. 24. Oktober 2005 – II ZR 179/03 (Kapitalerhöhung gegen Sacheinlage – Voraussetzungen)
- OLG Frankfurt, Urt. v. 5. September 2018 – 4 U 152/17 (Wandeldarlehen und Qualified Financing Prüfung)

## Vorgehen

### 1. Schwellentest Qualified Financing
Prüfe: Ist Pre-Money-Bewertung der Runde ≥ vertraglich vereinbartem Mindestwert? Ist Investitionsvolumen ≥ vertraglich vereinbartem Mindestvolumen? Investition ohne Berücksichtigung dieses Wandeldarlehens? Wenn beide Ja: Qualified Financing liegt vor.

### 2. Vollverwässerte Anteile vor Runde berechnen
Anteile vor Runde = Stammkapital + ESOP/Optionspool (vollverwässert). Bei Sonnenglas: 100 Anteile (40 + 35 + 25).

### 3. Wandlungspreis berechnen (MIN-Methode)
Preis A (Rundenpreis) = Pre-Money / Anteile vor Runde.
Preis B (Discount-Preis) = (1 − Discount) × Pre-Money / Anteile vor Runde.
Preis C (Cap-Preis) = Cap / Anteile vor Runde.
Wandlungspreis = MIN(Preis A, Preis B, Preis C).

### 4. Anzahl neue Anteile berechnen
Wandlungssumme C = Darlehen + aufgelaufene Zinsen.
Anzahl = C / Wandlungspreis (auf nächsten ganzen Anteilswert in EUR aufrunden, § 5 Abs. 1 GmbHG).

### 5. Wandlungsmitteilung auslösen
Gesellschaft informiert Lender (§ 4.3): Investorenname, Pre-Money, Investitionsvolumen, Anteilsklassen. Zwei Wochen vor Durchführung.

### 6. Wandlungsoption ausgeübt?
Lender erklärt Wandlung per Textform innerhalb eines Monats nach Wandlungsmitteilung. Dann: `gesellschafterbeschluss-kapitalerhoehung` und `notar-paket-uebermittlung`.

## Beispielrechnung

| Parameter | Wert |
|---|---|
| Darlehensbetrag | EUR 250000 |
| Zinsen (2 Jahre, fünf Prozent p.a.) | EUR 25694 |
| Wandlungssumme C | EUR 275694 |
| Anteile vor Runde (vollverwaessert) | 100 |
| Pre-Money Seed-Runde | EUR 6000000 |
| Preis A (Rundenpreis) | EUR 60000 je Anteil |
| Preis B (zwanzig Prozent Discount) | EUR 48000 je Anteil |
| Preis C (Cap EUR 4000000) | EUR 40000 je Anteil |
| Wandlungspreis (MIN) | EUR 40000 (Cap greift) |
| Neue Anteile | 275694 / 40000 = 6.89 → 7 |
| Nennwert neue Anteile | EUR 7 (je EUR 1 Nennwert) |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Pre-Money Runde unter Mindest-Schwelle | Kein Qualified Financing | Grenzwertig | Klar über Schwelle |
| Wandlungsmitteilung nicht rechtzeitig | Fristversäumnis, Lender kann nicht wandeln | Mitteilung verspätet | Rechtzeitig |
| Vollverwässerte Anteile unklar | Wandlungspreis nicht berechenbar | ESOP-Pool unklar | Vollverwässerte Basis dokumentiert |
| Term Sheet ohne Pre-Money-Angabe | Keine Berechnungsgrundlage | Bewertung nachzuholen | Term Sheet vollständig |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 55 ff. aktualisieren.
