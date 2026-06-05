---
name: wandlungspruefung-trigger
description: "Wandlungspruefung Trigger: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wandlungspruefung Trigger

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Wandlungspruefung Trigger** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wandlungspruefung-trigger-maturity` | Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen wenn kein qualifiziertes Finanzierungsereignis eingetreten ist. §§ 488 ff. BGB Fälligkeit. Prüfraster: Laufzeitenddatum Wandlungsrecht Wandlungspflicht Rückzahlungsalternative Preisbestimmung. Output: Prüfprotokoll Handlungsempfehlung. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing). |
| `wandlungspruefung-trigger-qualified-financing` | Wandlung bei qualifizierter Finanzierungsrunde prüfen wenn neue Investitionsrunde als Trigger definiert ist. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Qualified-Financing-Definition Mindestbetrag Lead-Investor Wandlungspflicht oder -recht Preisbestimmung. Output: Prüfprotokoll Wandlungsberechnung. Abgrenzung: nicht für Maturity-Trigger (wandlungsprüfung-trigger-maturity). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Wandlungspruefung Trigger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wandlungspruefung-trigger-maturity`

**Fokus:** Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen wenn kein qualifiziertes Finanzierungsereignis eingetreten ist. §§ 488 ff. BGB Fälligkeit. Prüfraster: Laufzeitenddatum Wandlungsrecht Wandlungspflicht Rückzahlungsalternative Preisbestimmung. Output: Prüfprotokoll Handlungsempfehlung. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing).

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 488 ff. BGB (Fälligkeit bei Maturity) → §§ 135, 143 InsO (Anfechtung Rückzahlung Gesellschafterdarlehen) → § 39 InsO (Nachrang bei Wandlung nach Insolvenz) → § 315 BGB (Wahlrecht des Darlehensgebers bei Maturity) → §§ 55, 56 GmbHG (Kapitalerhöhung nach Wandlungsausübung)

## 2. `wandlungspruefung-trigger-qualified-financing`

**Fokus:** Wandlung bei qualifizierter Finanzierungsrunde prüfen wenn neue Investitionsrunde als Trigger definiert ist. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Qualified-Financing-Definition Mindestbetrag Lead-Investor Wandlungspflicht oder -recht Preisbestimmung. Output: Prüfprotokoll Wandlungsberechnung. Abgrenzung: nicht für Maturity-Trigger (wandlungsprüfung-trigger-maturity).

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 55 GmbHG (Kapitalerhöhung durch neue Einlagen) → §§ 241, 242 BGB (Treu und Glauben, Information des Darlehensgebers) → § 280 BGB (Schadensersatz bei Verweigerung der Information) → § 5 Abs. 1 GmbHG (Mindest-Nennbetrag, Aufrundung) → §§ 195, 199 BGB (Verjährung Wandlungsrecht)
