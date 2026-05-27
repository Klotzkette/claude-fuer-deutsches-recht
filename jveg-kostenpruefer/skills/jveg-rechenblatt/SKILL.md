---
name: jveg-rechenblatt
description: "JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Pruefraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgrenzung: nicht Antragsgenerator."
---

# JVEG-Rechenblatt

## Aufgabe
Erstelle ein vollständig nachvollziehbares Rechenblatt für JVEG-Vergütungsansprüche mit Normbezug, Eingabewert, Kappungsgrenze, Belegverweis und Rechenergebnis je Position.

## Triage — kläre vor der Erstellung

1. **Positionen:** Welche Vergütungspositionen sollen im Rechenblatt erfasst werden?
2. **Honorargruppe:** Bei Sachverständigen — welche Honorargruppe nach § 9 JVEG?
3. **Zeitnachweise:** Liegen dokumentierte Zeitangaben (Beginn/Ende) für die Tätigkeit vor?
4. **Kappungsgrenzen:** Gibt es Höchstbeträge (z.B. Tagesgeld, Übernachtungspauschale)?
5. **Vorschussabzug:** Ist ein bereits ausgezahlter Vorschuss in Abzug zu bringen?

## Zentrale Normen
- § 8 JVEG (Sachverständigenvergütung — Stundensatz)
- § 9 JVEG (Honorargruppen-Tabelle)
- § 10 JVEG (Reisezeit)
- § 5 JVEG (Fahrtkosten — Kilometer × Satz)
- § 11 JVEG (Übernachtungsgeld — Kappungsgrenze)
- § 12 JVEG (Tagegeld)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Das Rechenblatt muss die erforderliche Zeit nachvollziehbar begründen; nicht die tatsächlich aufgewandte, sondern die objektiviert notwendige Zeit ist maßgeblich.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Bei der Berechnung sind Kappungsgrenzen strikt einzuhalten; eine Überschreitung löst nicht automatisch § 8a-Konsequenzen aus, ist aber nicht erstattungsfähig.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Fahrtkostenberechnungen müssen die Ausgangspunkte und Streckenlängen transparent dokumentieren.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Jede Position im Rechenblatt braucht einen Belegverweis; nicht belegte Positionen können nicht festgesetzt werden.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, § 8 Rn. 1 ff., § 9 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 8–12 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 9 Rn. 1 ff.

## Startet bei
Fertigstellung der Positionserfassung (jveg-aktenstripper); vor Antragserstellung.

## Arbeitsweise
1. Jede Position mit Eingabewert und Norm erfassen.
2. Kappungsgrenzen anwenden.
3. Rechenweg Schritt für Schritt dokumentieren.
4. Belegverweis pro Zeile eintragen.
5. Summe bilden; Vorschuss abziehen; Restforderung ausweisen.

## Output-Template

| Position | Norm | Eingabewert | Kappung | Rechenschritt | Beleg | Ergebnis (EUR) |
|---|---|---|---|---|---|---|
| Stunden Honorar [X Std. × Y EUR] | § 8 i.V.m. § 9 JVEG | X Std. | — | X × Y = | Anlage 1 | 00,00 |
| Reisezeit [X Std. × Y EUR] | § 10 JVEG | X Std. | — | X × Y = | Anlage 2 | 00,00 |
| Fahrtkosten [X km × Y EUR] | § 5 JVEG | X km | — | X × Y = | Anlage 3 | 00,00 |
| Übernachtung | § 11 JVEG | 1 Nacht | 00,00 EUR | Beleg | Anlage 4 | 00,00 |
| **Brutto** | | | | | | **00,00** |
| ./. Vorschuss | § 3 JVEG | | | | | -00,00 |
| **Restforderung** | | | | | | **00,00** |

## Ausgabe
Vollständiges Rechenblatt; dient als Anlage zum Festsetzungsantrag.

## Leitplanken
- Jede Zeile braucht Norm + Beleg; leere Felder blockieren die Ausgabe.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
