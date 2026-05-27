---
name: jveg-fahrtkosten
description: "Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, oeffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Pruefraster: Wegstrecke, Verkehrsmittelwahl, Parkgebuehren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Uebernachtungskosten."
---

# JVEG-Fahrtkosten

## Aufgabe
Prüfe geltend gemachte Fahrtkosten auf Normkonformität nach §§ 5–7 JVEG: Verkehrsmittelwahl, Kilometersatz, Wirtschaftlichkeit und Belegpflicht.

## Triage — kläre vor der Prüfung

1. **Verkehrsmittel:** Eigenes Kfz, Bahn, Flug oder sonstiges Verkehrsmittel?
2. **Personengruppe:** Sachverständiger (§ 5 Abs. 1 JVEG) oder Zeuge (§ 5 Abs. 2 JVEG — niedrigerer Kilometersatz)?
3. **Strecke:** Tatsächlich gefahrene Strecke belegt (Routennachweis, Google Maps, Maut)?
4. **Wirtschaftlichkeit:** Wäre ein günstigeres Verkehrsmittel zumutbar gewesen?
5. **Auslandsanreise:** Liegt ein grenzüberschreitender Reiseweg vor (§ 7 JVEG)?

## Speziallogik: Kilometersatz Zeugen
- Sachverständige: § 5 Abs. 1 JVEG — 0,42 EUR/km (Stand 2021).
- Zeugen: § 5 Abs. 2 JVEG — 0,35 EUR/km (Stand 2021).
- Keine Gleichsetzung; Rollenabgrenzung vor Berechnung zwingend.

## Zentrale Normen
- § 5 JVEG (Fahrtkostenersatz: Kfz, Bahn)
- § 6 JVEG (Reisekosten bei Flügen und Fernreisen)
- § 7 JVEG (Auslandsreise)
- § 19 JVEG (Zeugenfahrtkosten — Verweis auf § 5)
- § 23 JVEG (Dreimonatsfrist)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Fahrtkosten sind nur in Höhe des notwendigen Aufwands erstattungsfähig; Umwege ohne sachlichen Grund werden gekürzt.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Dreimonatsfrist des § 23 JVEG gilt auch für Fahrtkostenerstattungsansprüche; spätere Nachforderung ist ausgeschlossen.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Fahrtkosten sind auf das wirtschaftlichste Verkehrsmittel (in der Regel Bahn 2. Klasse) begrenzt; Mehrkosten durch Kfz-Nutzung nur bei nachgewiesener Notwendigkeit.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Parkkosten sind als Nebenkosten des Fahrtkostenersatzes nur mit Beleg erstattungsfähig.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, §§ 5–7 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 5–7 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 5 Rn. 1 ff.

## Startet bei
Fahrtkosten-Position in Rechnung oder Kostenfestsetzungsantrag.

## Arbeitsweise
1. Verkehrsmittel und Personengruppe identifizieren.
2. Kilometersatz nach § 5 Abs. 1 oder Abs. 2 JVEG zuordnen.
3. Strecke und Belege prüfen.
4. Wirtschaftlichkeitsvergleich (Bahn vs. Kfz).
5. Auslandsanteil nach § 7 JVEG gesondert prüfen.

## Output-Template

| Position | Geltend (EUR) | Norm | Befund | Anerkannt (EUR) |
|---|---|---|---|---|
| Kfz [X km × Y EUR] | 00,00 | § 5 Abs. 1/2 JVEG | [Befund] | 00,00 |
| Bahn (Belege) | 00,00 | § 5 Abs. 1 JVEG | [Befund] | 00,00 |
| Parkkosten (Beleg) | 00,00 | § 5 Abs. 1 JVEG | [Befund] | 00,00 |
| Auslandsanteil | 00,00 | § 7 JVEG | [Befund] | 00,00 |
| **Gesamt** | **00,00** | | | **00,00** |

## Ausgabe
Positionsgenaue Fahrtkostenprüfung mit Kilometersatz, Befund und anerkanntem Betrag.

## Leitplanken
- Zeugen-Kilometersatz (§ 5 Abs. 2 JVEG) niedriger als Sachverständigen-Satz.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
