---
name: darlehenshoehe-konditionen
description: "Erfassung und Dokumentation der Darlehenskonditionen: EUR-Betrag, Laufzeit (Standard zwei Jahre Feste Laufzeit), Zinssatz (Standard fuenf Prozent p.a. pro rata temporis act/360), Auszahlungsmodus (sieben Bankarbeitstage), Bankverbindung der Gesellschaft, aufschiebende Bedingungen und Kuendigungsausschluss."
---

# Darlehensbetrag und Konditionen

## Zweck

Dieser Skill erfasst alle wirtschaftlichen Kernkonditionen des Wandeldarlehens und bereitet die Vertragsabschnitte §§ 1 bis 3 vor (Darlehensgewährung, Laufzeit, Rückzahlung, Verzinsung). Phase A des Lebenszyklus.

## Eingaben

- Darlehensbetrag in EUR (in Ziffern und in Worten)
- Laufzeit in Jahren (Standard: zwei Jahre)
- Zinssatz p.a. (Standard: fünf Prozent; Basis act/360)
- Zinsabführung: Standard keine unterjährige Zahlung, Zinsen fällig bei Rückzahlung oder Wandlung
- Auszahlungsfrist: Standard sieben deutsche Bankarbeitstage nach beidseitiger Unterzeichnung
- Bankverbindung der Gesellschaft: Kontoinhaber, IBAN, BIC, Kreditinstitut, Verwendungszweck
- Aufschiebende Bedingungen aus Term Sheet (falls vorhanden)
- Ordentliches Kündigungsrecht: ausgeschlossen (§ 2.3 Standardklausel)

## Rechtlicher Rahmen

### Primärnormen
- §§ 488 ff. BGB (Darlehensvertrag, Zinspflicht, Fälligkeit)
- § 490 Abs. 1 BGB (außerordentliche Kündigung bei Vermögensverschlechterung – wird vertraglich ausgeschlossen)
- § 314 BGB (Kündigung aus wichtigem Grund, bleibt unberührt)
- § 44 InsO, § 119 InsO (Unwirksamkeit insolvenzabhängiger Lösungsklauseln)
- §§ 3, 4 StaRUG (Einschränkung Kündigungsrechte im Restrukturierungsrahmen)

### Rechtsprechung
- BGH, Urt. v. 7. März 2013 – IX ZR 7/12 (Kongruenzdeckung Darlehensrückzahlung)
- BGH, Urt. v. 29. Januar 2015 – IX ZR 279/13 (Fälligkeitsklausel und Insolvenz)

## Vorgehen

### 1. Darlehensbetrag festhalten
EUR-Betrag in Ziffern und in Worten (z. B. „EUR 250000 (in Worten: zweihundertfünfzigtausend Euro)"). Keine Tausenderpunkte in Zifferndarstellung, um Verwechslungen zu vermeiden.

### 2. Laufzeit und Festes Ende
Startdatum: Datum vollständiger Unterzeichnung durch alle Parteien. Enddatum: Startdatum plus zwei Jahre ohne Kündigung erforderlich. Beispiel: Unterzeichnung 01.06.2025 → Ende 31.05.2027.

### 3. Zinssatz und Berechnungsbasis
Standard: fünf Prozent p.a., pro rata temporis, act/360. Formel: Zinsen = Kapital × Zinssatz × (Tage / 360). Keine unterjährige Zahlung; Zinsen aufgelaufen bis Rückzahlung oder Wandlung.

### 4. Auszahlungsmodus
Sieben deutsche Bankarbeitstage ab vollständiger Unterzeichnung. Überweisung auf die folgende Bankverbindung der Gesellschaft (Tabelle eintragen).

### 5. Aufschiebende Bedingungen
Falls Term Sheet Bedingungen enthält: genau aufführen. Falls keine: ausdrücklich klarstellen, dass keine vorliegen.

### 6. Kündigungsausschluss formulieren
Ordentliche Kündigung ausgeschlossen für alle Parteien. § 490 Abs. 1 BGB vertraglich ausgeschlossen. Wichtiger Grund (§ 314 BGB) bleibt unberührt.

## Beispielrechnung Zinsen

| Parameter | Wert |
|---|---|
| Darlehensbetrag | EUR 250000 |
| Zinssatz | fünf Prozent p.a. |
| Laufzeit | 2 Jahre (730 Tage) |
| Zinsen act/360 | EUR 250000 × 0.05 × (730/360) = EUR 25694 |
| Wandlungsbetrag | EUR 275694 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Zinssatz über zwanzig Prozent p.a. | Sittenwidrigkeitsprüfung § 138 BGB | Zehn bis zwanzig Prozent | Unter zehn Prozent |
| Auszahlung vor Unterzeichnung erfolgt | Vertrag ex post unwirksam riskant | Auszahlung auf Anweisung | Auszahlung nach Unterzeichnung |
| Keine Bankverbindung vorhanden | Auszahlung blockiert | Konto in Eröffnung | Konto bekannt |
| Laufzeit über fünf Jahre | Langfristigkeit prüfen | Drei bis fünf Jahre | Standard zwei Jahre |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungsmechanik-konzipieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/rangruecktritt-formulieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Darlehensrecht aktualisieren.
