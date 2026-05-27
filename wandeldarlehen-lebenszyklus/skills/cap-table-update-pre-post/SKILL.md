---
name: cap-table-update-pre-post
description: "Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Pruefraster: Pre-Money Post-Money Wandlungspreis neue Anteile Verwasserung bestehende Gesellschafter. Output: Cap-Table-Vergleich Pre/Post Verwasserungsrechnung. Abgrenzung: nicht fuer Wandlungsmechanik (wandlungsmechanik-konzipieren)."
---

# Cap-Table Update – Pre-Money und Post-Money

## Zweck

Dieser Skill erstellt die Pre-Money-Cap-Table (vor Wandlung und Kapitalerhöhung) und die Post-Money-Cap-Table (nach Wandlung und Kapitalerhöhung der neuen Investoren) und quantifiziert die Verwässerung der Altgesellschafterinnen. Phase C des Lebenszyklus.

## Eingaben

- Aktuelle Gesellschafterliste (§ 40 GmbHG): Name, Anteilszahl, Nennwert, Prozent
- Wandlungsberechnung aus `wandlungspreis-berechnung` (neue Anteile für Lender)
- Kapitalerhöhung neue Investoren: Investitionsbetrag, Preis je Anteil (Rundenpreis Preis A), neue Anteile
- ESOP-Pool (falls vorhanden): Anteilszahl, ausgegeben/reserviert
- Nennwert je Anteil: EUR 1 (Standard)

## Rechtlicher Rahmen

### Primärnormen
- § 40 GmbHG (Gesellschafterliste – Geschäftsführerin reicht nach Kapitalerhöhung neue Liste ein; oder Notar nach § 40 Abs. 2 GmbHG)
- § 55 Abs. 1 GmbHG (Kapitalerhöhung)
- § 5 Abs. 1 GmbHG (Mindestanteilsnennwert EUR 1)
- § 272 HGB (Eigenkapitalausweis)

### Rechtsprechung
- BGH, Urt. v. 17. November 2008 – II ZR 244/07 (Gesellschafterliste § 40 GmbHG – Eintragung und Wirkung)
- OLG Frankfurt, Beschl. v. 5. Mai 2015 – 20 W 174/13 (Gesellschafterlistenpflicht bei Kapitalerhöhung)

## Vorgehen

### 1. Pre-Money-Cap-Table erstellen
Alle aktuellen Gesellschafterinnen mit Anteilszahl, Nennwert (EUR) und Prozentanteil. Stammkapital gesamt = Summe aller Nennwerte. Vollverwässert: plus ESOP-Optionen (als eigene Zeile).

### 2. Wandlungsanteile des Lenders einrechnen
Neue Anteile Lender (aus `wandlungspreis-berechnung`). Post-Wandlung (vor Seed-Investoren): Anteile der Gesellschafterinnen unveränderter Absolutwert, aber neuer Prozentanteil nach Verwässerung durch Lender.

### 3. Kapitalerhöhung neue Seed-Investoren einrechnen
Neue Investoren: Investitionsbetrag / Rundenpreis = neue Anteile. Stammkapital nach Kapitalerhöhung = Stammkapital alt + neue Anteile Lender + neue Anteile Investoren.

### 4. Post-Money-Cap-Table vollständig aufstellen
Alle Gesellschafter mit Anteilszahl und Prozent nach Kapitalerhöhung. Verwässerungseffekt auf Altgesellschafterinnen quantifizieren: Prozentverlust = Altanteil(vor) − Altanteil(nach).

### 5. Verwässerungsdarstellung
Tabelle: Gesellschafterin / Anteile vor / Prozent vor / Anteile nach / Prozent nach / Verwässerung in Prozentpunkten.

### 6. Excel-Datei und Dokumentation
Cap-Table als Excel-Datei mit zwei Tabellenblättern (Pre-Money und Post-Money). Formatierung: Summenzeile, Prozentwerte als Dezimalzahl mit zwei Nachkommastellen.

## Beispiel Pre-Money-Cap-Table (Sonnenglas UG)

| Gesellschafter | Anteile | Nennwert (EUR) | Prozent |
|---|---|---|---|
| Dr. Mira Schöneck | 40 | 40 | 40.00 % |
| Lina Habersaat | 35 | 35 | 35.00 % |
| Treasury | 25 | 25 | 25.00 % |
| Gesamt | 100 | 100 | 100.00 % |
| Stammkapital | | EUR 100 | |

## Beispiel Post-Money-Cap-Table (nach Wandlung + Seed EUR 1 Mio / Pre-Money EUR 6 Mio)

| Gesellschafter | Anteile | EUR | Prozent |
|---|---|---|---|
| Dr. Mira Schöneck | 40 | 40 | 29.63 % |
| Lina Habersaat | 35 | 35 | 25.93 % |
| Treasury | 25 | 25 | 18.52 % |
| Northstar (Lender, Wandlung) | 7 | 7 | 5.19 % |
| Seed-Investoren (EUR 1 Mio / EUR 40000) | 25 | 25 | 18.52 % |
| ESOP (bestehend, noch frei) | 3 | 3 | 2.22 % |
| Gesamt | 135 | 135 | 100.00 % |
| Stammkapital nach KE | | EUR 135 | |

Verwässerung Schöneck: 40 % → 29.63 % = −10.37 Prozentpunkte

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| ESOP-Pool nicht einbezogen | Verwässerung unterschätzt | ESOP-Größe unbekannt | ESOP vollständig erfasst |
| Falsche Anteilszahl Lender | Cap-Table inkorrekt | Aufrundung strittig | Exakte Berechnung |
| Stammkapital-Erhöhung nicht ins HR eingetragen | Gesellschafterliste veraltet | Eintragung beantragt | Eingetragen |
| Alte Gesellschafterliste verwendet | Altdaten | Teils aktuell | Aktuelle Liste gem. § 40 GmbHG |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterliste-aktualisieren/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/gesellschafterbeschluss-kapitalerhoehung/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

BGH, Urt. v. 17.07.2012 — **II ZR 244/07**, BGHZ 194, 132 Rn. 22: Die Gesellschafterliste nach § 40 GmbHG ist unverzüglich nach Abtretung/Wandlung vom Notar oder Geschäftsführer beim Handelsregister einzureichen; bis zur Einreichung der neuen Liste gilt der bisherige Gesellschafter als legitimiert — Wandelnder erlangt erst mit Listeneintragung die formelle Gesellschafterstellung.

BGH, Urt. v. 20.09.2011 — **II ZR 234/09**, NJW 2012, 301 Rn. 16: Verwässerungsschutzklauseln (Anti-Dilution) in Wandeldarlehensverträgen sind im Kapital-Erhöhungsbeschluss zu berücksichtigen; Cap Table muss vor und nach Wandlung die vollständig verwässerten Anteile (Fully Diluted) einschließlich aller Wandelrechte abbilden.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, unverzügliche Aktualisierung nach Wandlung) → § 15 GmbHG (Abtretung Anteile) → § 17 GmbHG (Mehrfachabtretung) → § 16 GmbHG (Gesellschafterstellung, Legitimationswirkung Liste) → § 55 GmbHG (Kapitalerhöhungsbeschluss, neue Anteile)
