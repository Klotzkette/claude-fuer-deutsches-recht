---
name: stb-dba-all-country-memo-generator
description: "Generiert ein länderspezifisches DBA-Memo für jeden deutschen DBA-Staat aus Matrix, DBA-Text und Sachverhalt. Für Länder ohne eigenen Detail-Skill: Artikelroute, Einkunftsart, Methode, Quellensteuer, Beweise, Edge-Cases und offene Live-Prüfungen."
---

# DBA-All-Country-Memo-Generator

## Aufgabe

Dieser Skill erzeugt aus jedem realistischen DBA-Sachverhalt ein verwendbares Memo, auch wenn das Land noch keinen Einzel-Skill hat.

## Pflichtaufbau

1. **Sachverhalt:** Beteiligte, Staaten, Zeitraum, Beträge, Zahlungsflüsse.
2. **DBA-Status:** Matrix und live geprüfter DBA-Text.
3. **Ansässigkeit:** nationales Recht, Art. 4, Tie-Breaker.
4. **Einkunftsart:** Artikel 6 bis 21 oder Alt-DBA-Sonderartikel.
5. **Verteilung:** Besteuerungsrecht, Quellensteuerhöchstsatz, Verfahren.
6. **Methode Deutschland:** Freistellung/Anrechnung/Progressionsvorbehalt/Switch-over.
7. **Anti-Missbrauch:** § 50d EStG, Beneficial Ownership, PPT/LOB, Substanz.
8. **Belege:** konkret.
9. **Ergebnis:** Kurzantwort plus offene Prüfmarker.

## Realistische Varianten

Baue bei Bedarf Varianten:

- Arbeitnehmer mit 47 Home-Office-Tagen und Bonus für Vorjahr.
- GmbH zahlt Softwarelizenz an ausländische Schwester.
- Deutsche KG mit ausländischer Betriebsstätte und lokalen Verlusten.
- Verkauf einer Immobilien-Holding.
- Pensionär mit gesetzlicher und betrieblicher Rente.
- US-LLC mit deutschen Gesellschaftern.
- Grenzgänger mit Dienstreisen in Drittstaaten.

## Quellenregel

Wenn der DBA-Text nicht vorliegt, keine abschließenden Sätze behaupten. Ausgabe dann ausdrücklich als "Arbeitsmemo mit Live-Prüfmarkern" kennzeichnen.
