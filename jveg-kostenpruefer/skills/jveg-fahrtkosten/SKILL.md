---
name: jveg-fahrtkosten
description: "Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernachtungskosten."
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
- Sachverständige und Dolmetscher: § 5 Abs. 1 JVEG — 0,42 EUR/km (unveraendert nach KostRAeG 2025; siehe auch dort die Erhoehung der Stundensaetze).
- Zeugen und Dritte: § 5 Abs. 2 JVEG — 0,35 EUR/km.
- Keine Gleichsetzung; Rollenabgrenzung vor Berechnung zwingend.
- Quelle Norm: https://www.gesetze-im-internet.de/jveg/__5.html

## Rechtsstand 2025/2026 — KostRAeG 2025

Mit dem Kosten- und Betreuungsrechtsaenderungsgesetz 2025 (KostRAeG 2025) sind zum 01.06.2025 die Honorarsaetze des JVEG fuer Sachverstaendige in Anlage 1 zu § 9 JVEG pauschal um 9 Prozent erhoeht worden. Die neuen Saetze gelten nur fuer Auftraege ab 01.06.2025; in Altverfahren bleiben die alten Saetze.

- Synopse JVEG 2025: https://ifsforum.de/fileadmin/user_upload/Aktuelles/Synopse_JVEG__2025.pdf
- Praxis-Hinweis Sachverstaendigenverguetung: https://praxis-grundstuecksbewertung.de/wissenswert/gesetzgebung/jveg-verguetung-sachverstaendige/

## Zentrale Normen
- § 5 JVEG (Fahrtkostenersatz: Kfz, Bahn)
- § 6 JVEG (Reisekosten bei Flügen und Fernreisen)
- § 7 JVEG (Auslandsreise)
- § 19 JVEG (Zeugenfahrtkosten — Verweis auf § 5)
- § 23 JVEG (Dreimonatsfrist)
- § 9 JVEG i.V.m. Anlage 1 (Sachverstaendigen-Stundensaetze, KostRAeG 2025)

## Rechtsprechung
- Aktuelle Rechtsprechung zu § 5 JVEG vor Ausgabe ueber https://dejure.org pruefen.
- BGH-Linie Sachverstaendigenverguetung: Senat fuer Anwaltssachen sowie I., VII., IV. Zivilsenat zustaendig je nach Sachgebiet; Aktenzeichen vor Uebernahme verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
