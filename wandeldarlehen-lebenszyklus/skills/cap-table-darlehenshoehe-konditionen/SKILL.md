---
name: cap-table-darlehenshoehe-konditionen
description: "CAP Table Darlehenshoehe Konditionen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CAP Table Darlehenshoehe Konditionen

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **CAP Table Darlehenshoehe Konditionen** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cap-table-update-pre-post` | Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money Wandlungspreis neue Anteile Verwasserung bestehende Gesellschafter. Output: Cap-Table-Vergleich Pre/Post Verwasserungsrechnung. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren). |
| `darlehenshoehe-konditionen` | Darlehenshoehe Zinsen Laufzeit und Konditionen für Wandeldarlehen verhandeln und dokumentieren. §§ 488 491 BGB Darlehensvertrag §§ 246 247 BGB Zinsen. Prüfraster: Darlehenshoehe Zinssatz Disagio Laufzeit Fälligkeit Sicherheiten Rangrücktritt. Output: Term-Sheet Konditionenblatt Vertragsklauseln. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **CAP Table Darlehenshoehe Konditionen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cap-table-update-pre-post`

**Fokus:** Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money Wandlungspreis neue Anteile Verwasserung bestehende Gesellschafter. Output: Cap-Table-Vergleich Pre/Post Verwasserungsrechnung. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren).

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, unverzügliche Aktualisierung nach Wandlung) → § 15 GmbHG (Abtretung Anteile) → § 17 GmbHG (Mehrfachabtretung) → § 16 GmbHG (Gesellschafterstellung, Legitimationswirkung Liste) → § 55 GmbHG (Kapitalerhöhungsbeschluss, neue Anteile)

## 2. `darlehenshoehe-konditionen`

**Fokus:** Darlehenshoehe Zinsen Laufzeit und Konditionen für Wandeldarlehen verhandeln und dokumentieren. §§ 488 491 BGB Darlehensvertrag §§ 246 247 BGB Zinsen. Prüfraster: Darlehenshoehe Zinssatz Disagio Laufzeit Fälligkeit Sicherheiten Rangrücktritt. Output: Term-Sheet Konditionenblatt Vertragsklauseln. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren).

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Darlehensbetrag festhalten
EUR-Betrag in Ziffern und in Worten (z. B. "EUR 250000 (in Worten: zweihundertfünfzigtausend Euro)"). Keine Tausenderpunkte in Zifferndarstellung, um Verwechslungen zu vermeiden.

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

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 488, 491 ff. BGB (Darlehensvertrag) → § 490 BGB (Kündigung, vertraglich ausgeschlossen) → § 314 BGB (Kündigung wichtiger Grund, unberührt) → § 138 BGB (Sittenwidrigkeit überhöhter Zins) → §§ 135, 143 InsO (Anfechtung Rückzahlung Gesellschafterdarlehen) → § 119 InsO (Unwirksamkeit insolvenzabhängiger Lösungsklauseln) → §§ 3, 4 StaRUG (Restrukturierungsrahmen)
