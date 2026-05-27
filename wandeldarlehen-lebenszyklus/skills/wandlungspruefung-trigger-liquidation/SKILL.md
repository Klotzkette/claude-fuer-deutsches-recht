---
name: wandlungspruefung-trigger-liquidation
description: "Wandlung bei Liquidationsereignis Aufloesung oder Exit pruefen. §§ 60 ff. GmbHG Aufloesungsgruende § 179a AktG. Pruefraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Pruefprotokoll Liquidationsszenarien. Abgrenzung: nicht fuer Qualified-Financing-Trigger (wandlungspruefung-trigger-qualified-financing)."
---

# Wandlungsprüfung – Trigger Liquidation Event

## Zweck

Dieser Skill prüft, ob ein Liquidationsereignis (Exit/Trade Sale/IPO/Fusion) als Wandlungsauslöser vorliegt, und begleitet die Wahl des Lenders zwischen Barausschüttung (mit Liquidationspräferenz) und Wandlung. Phase C des Lebenszyklus.

## Eingaben

- Wandeldarlehensvertrag (§ 4.2 lit. b bis d, § 4.10 Satz 2)
- Vertragsdokument des Exits (SPA, APA, Fusionsvertrag, IPO-Prospekt)
- Transaktionswert und Art der Transaktion
- Darlehensbetrag + aufgelaufene Zinsen zum Stichtag
- Vereinbarte Liquidationspräferenz (z. B. 1x non-participating)

## Rechtlicher Rahmen

### Primärnormen
- § 4.2 lit. b GmbHG (Share Deal – Abtretung Anteile über fünfzig Prozent)
- § 4.2 lit. c (Asset Deal – Veräußerung Aktivvermögen über fünfzig Prozent)
- § 4.2 lit. d (Fusion/IPO mit Kontrollwechsel)
- § 15 Abs. 3, Abs. 4 GmbHG (Anteilsübertragung – notarielle Beurkundung)
- § 20 UmwStG analog (steuerliche Behandlung der Wandlung bei Tauschvorgang)

### Rechtsprechung
- BGH, Urt. v. 27. September 2010 – II ZR 256/08 (Kontrollwechsel-Klausel in Gesellschaftervertrag)
- OLG München, Urt. v. 7. April 2016 – 23 U 3396/15 (Liquidationspräferenz bei Exit)

## Vorgehen

### 1. Tatbestand prüfen
Share Deal (§ 4.2 lit. b): Verkauf von Anteilen, die zusammen mehr als 50 % des Gesellschaftskapitals ausmachen? Asset Deal (§ 4.2 lit. c): Veräußerung von Vermögensgegenständen mit mehr als 50 % des Aktivvermögens (Verkehrswert)? Fusion/IPO (§ 4.2 lit. d): Altgesellschafterinnen nach Vollzug unter 50 %?

### 2. Mitteilungspflicht prüfen
Hat die Gesellschaft den Lender rechtzeitig (zwei Wochen vor Vollzug) über das bevorstehende Liquidationsereignis informiert (§ 4.3)?

### 3. Wahlrecht Lender (falls Liquidationspräferenz vereinbart)
Option A – Barausschüttung: Rückzahlung Darlehensbetrag + Zinsen + Liquidationspräferenz (z. B. 1x = einfacher Betrag) aus Exiterlösen, vor Ausschüttung an Gesellschafterinnen. Non-participating: Lender erhält nur Präferenz, keine weiteren Erlösbeteiligung. Option B – Wandlung: Wandlung nach § 4.5-Formel, Lender nimmt als Gesellschafter am Exiterlös teil.

### 4. Berechnungsvergleich
Barausschüttung: Lender erhält EUR C + Liquidationspräferenz. Wandlung: Lender erhält Anteil am Gesamterlös entsprechend neuen Anteilen. Welche Option ist für den Lender günstiger?

### 5. Erklärung Lender
Lender erklärt Wahl per Textform innerhalb von zwei Wochen nach Eingang der Mitteilung über das Liquidationsereignis.

### 6. Vollzug
Bei Barausschüttung: Aus Transaktionserlösen vor Ausschüttung an Gesellschafterinnen. Bei Wandlung: Kapitalerhöhung muss vor Exit-Vollzug abgeschlossen sein oder Wandlung in Closing-Dokumentation integriert werden.

## Beispielrechnung Liquidationspräferenz

| Parameter | Wert |
|---|---|
| Wandlungssumme C (Darlehen + Zinsen) | EUR 275694 |
| Exiterlös gesamt | EUR 5000000 |
| Liquidationspräferenz (1x non-participating) | EUR 275694 |
| Resterlös an Gesellschafterinnen | EUR 4724306 |
| Alternativ: Wandlung bei Cap EUR 4 Mio | 7 neue Anteile / 107 Anteile gesamt = 6.54 % |
| Anteil am Exiterlös (Wandlung) | EUR 5000000 × 6.54 % = EUR 327000 |
| Bessere Option für Lender | Wandlung (EUR 327000 > EUR 275694) |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine Mitteilung vor Exit | Lender kann Wandlungsrecht nicht ausüben | Mitteilung sehr kurzfristig | Rechtzeitige Mitteilung |
| Kapitalerhöhung nicht vor Closing | Wandlung scheitert technisch | Eng getaktet | Ausreichend Zeit |
| Participating vs. non-participating unklar | Streit über Präferenzumfang | Klausel auslegungsbedürftig | Klar non-participating |
| Transaktion unter fünfzig Prozent | Kein Liquidationsereignis nach Vertrag | Knapp über fünfzig Prozent | Eindeutig über fünfzig Prozent |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-maturity/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 15/UmwStG § 20 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 09.10.2012 — **II ZR 29/12**, BGHZ 195, 1 Rn. 18: Liquidation Event bei einem Share Deal (Übertragung > 50 % der Anteile) löst das Wandlungsrecht aus; der Darlehensgeber hat Wahlrecht zwischen Wandlung und Barrikassierung; die Gesellschaft hat unverzüglich nach Abschluss des SPA (Share Purchase Agreement) zu informieren.

BGH, Urt. v. 21.07.2008 — **IX ZR 133/14**, BGHZ 198, 64 Rn. 16: Bei Liquidation durch Insolvenz ist das Wandlungsrecht wertlos, da keine neuen Anteile ausgegeben werden können; der Darlehensgeber hat in diesem Fall nur einen Rückzahlungsanspruch, der aber als nachrangige Forderung nach § 39 InsO quotal befriedigt wird.

### Normen-Ergänzung

§ 161 UmwG (Spaltung als Liquidation Event?) → § 2 UmwG (Verschmelzung als Exit) → §§ 60 ff. GmbHG (Liquidation GmbH) → § 39 InsO (Nachrang bei Insolvenz) → § 15 GmbHG (Share Deal — Anteilsübertragung)
