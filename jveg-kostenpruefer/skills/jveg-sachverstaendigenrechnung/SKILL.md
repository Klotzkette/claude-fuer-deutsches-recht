---
name: jveg-sachverstaendigenrechnung
description: "Sachverstaendigenrechnung nach JVEG pruefen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Pruefraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverstaendigenrechnung. Abgrenzung: nicht Zeugenentschaedigung."
---

# JVEG-Sachverstaendigenrechnung

## Aufgabe
Prüfe Sachverständigenrechnungen vollständig nach §§ 8–10 JVEG: Honorargruppe, erforderliche Zeit, Reisezeit, Nebenkosten, § 8a-Kürzungsrisiken und Vorschusssaldo.

## Triage — kläre vor der Prüfung

1. **Honorargruppe:** Welcher Honorargruppe nach § 9 JVEG ist der Sachverständige zugeordnet?
2. **Erforderliche Zeit:** Wie viele Stunden werden abgerechnet — sind diese als erforderlich belegt?
3. **Reisezeit:** Werden Reisezeiten nach § 10 JVEG getrennt abgerechnet?
4. **§ 8a-Risiken:** Gibt es Anhaltspunkte für Gutachtenmängel, fehlende Hinweise oder Vorschussüberschreitung?
5. **Nebenkosten:** Werden Schreibauslagen, Kopien, Literatur oder sonstige Kosten geltend gemacht?

## Zentrale Normen
- § 8 JVEG (Sachverständigenvergütung — Stundensatz)
- § 8a JVEG (Kürzung/Wegfall)
- § 9 JVEG (Honorargruppen)
- § 10 JVEG (Reisezeit)
- § 12 JVEG (Nebenkosten)
- § 3 JVEG (Vorschuss)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Die abgerechnete Zeit eines Sachverständigen ist am Maßstab eines erfahrenen Gutachters auf dem jeweiligen Fachgebiet zu messen; überlange Bearbeitungszeiten werden objektiviert gekürzt.
2. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — § 8a JVEG rechtfertigt Kürzung, wenn das Gutachten wesentliche Mängel aufweist, die auf unzureichende Sorgfalt zurückgehen.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Reisezeiten nach § 10 JVEG sind von der Gutachtenarbeitszeit strikt zu trennen; Vermischung führt zur Kürzung.
4. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Vorschussüberschreitungen ohne vorherigen Hinweis an das Gericht führen zur Nichterstattung des übersteigenden Betrags.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, §§ 8–10 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 8–10 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 8 Rn. 1 ff.

## Startet bei
Eingang einer Sachverständigenrechnung zur Festsetzung nach § 4 JVEG.

## Arbeitsweise
1. Honorargruppe und Stundensatz verifizieren.
2. Erforderliche Zeit objektiv bewerten.
3. Reisezeit separat prüfen (§ 10 JVEG).
4. Nebenkosten auf Notwendigkeit und Belege prüfen.
5. § 8a-Risiken bewerten; Vorschusssaldo berechnen.

## Output-Template

| Position | Geltend (EUR) | Norm | Befund | Anerkannt (EUR) |
|---|---|---|---|---|
| Honorar [X Std. × Y EUR, Gr. Z] | 00,00 | § 8 i.V.m. § 9 JVEG | [Befund] | 00,00 |
| Reisezeit [X Std. × Y EUR] | 00,00 | § 10 JVEG | [Befund] | 00,00 |
| Nebenkosten | 00,00 | § 12 JVEG | [Befund] | 00,00 |
| **Brutto** | **00,00** | | | **00,00** |
| ./. Vorschuss | | § 3 JVEG | | -00,00 |
| **Restforderung** | **00,00** | | | **00,00** |

**§ 8a-Risikoeinschätzung:** [Keine / Teilkürzung / Vollkürzung]

## Ausgabe
Positionsgenaues Prüfergebnis mit § 8a-Risikoeinschätzung und Vorschusssaldo.

## Leitplanken
- Honorargruppe immer zuerst prüfen; falscher Ansatz infiziert gesamte Berechnung.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
