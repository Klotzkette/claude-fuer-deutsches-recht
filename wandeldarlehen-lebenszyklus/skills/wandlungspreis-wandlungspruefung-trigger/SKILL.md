---
name: wandlungspreis-wandlungspruefung-trigger
description: "Wandlungspreis Wandlungspruefung Trigger: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Wandlungspreis Wandlungspruefung Trigger

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Wandlungspreis Wandlungspruefung Trigger** im Plugin Wandeldarlehen-Lebenszyklus. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `wandlungspreis-berechnung` | Wandlungspreis auf Basis vertraglich vereinbarter Parameter berechnen wenn Wandlung ausgelöst wird. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Bewertungsdeckel Rabatt Qualified-Financing-Preis MFN Verwasserungsschutz Rundungsregel. Output: Berechnungsnachweis Wandlungspreis neue Anteile. Abgrenzung: nicht für Cap-Table-Update (cap-table-update-pre-post). |
| `wandlungspruefung-trigger-liquidation` | Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Prüfprotokoll Liquidationsszenarien. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing). |

## Arbeitsweg

Im Plugin Wandeldarlehen-Lebenszyklus gilt für **Wandlungspreis Wandlungspruefung Trigger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `wandlungspreis-berechnung`

**Fokus:** Wandlungspreis auf Basis vertraglich vereinbarter Parameter berechnen wenn Wandlung ausgelöst wird. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Bewertungsdeckel Rabatt Qualified-Financing-Preis MFN Verwasserungsschutz Rundungsregel. Output: Berechnungsnachweis Wandlungspreis neue Anteile. Abgrenzung: nicht für Cap-Table-Update (cap-table-update-pre-post).

# Wandlungspreis-Berechnung

## Zweck

Dieser Skill führt die vollständige Wandlungspreis-Berechnung durch – von der Wandlungssumme über den Wandlungspreis nach MIN-Methode bis zur Zahl der neuen Geschäftsanteile. Phase C des Lebenszyklus.

## Eingaben

- Darlehensbetrag (EUR)
- Auszahlungsdatum und Stichtag Wandlung (für Zinsberechnung)
- Zinssatz (fünf Prozent p.a., act/360)
- Pre-Money-Bewertung der Finanzierungsrunde (oder Fall-back-Bewertung bei Maturity)
- Vollverwässerte Anteile vor Wandlung (Stammkapital + ESOP)
- Valuation Cap (EUR)
- Discount (Prozent)
- Aktuelles Stammkapital (EUR) und Nennwert je Anteil (Standard EUR 1)

## Rechtlicher Rahmen

### Primärnormen
- § 5 Abs. 1 GmbHG (Mindestanteilsnennbetrag EUR 1 – Aufrundungsregel)
- § 55 Abs. 1 GmbHG (Kapitalerhöhung durch Gesellschafterbeschluss)
- § 56 GmbHG (Sacheinlage: Forderung aus Wandeldarlehen)
- § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage nach Wandlung)
- § 9 GmbHG (Differenzhaftung bei Überbewertung der Sacheinlage)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Wandlungssumme C berechnen
C = Darlehensbetrag + Zinsen (act/360)
Zinsen = Darlehensbetrag × Zinssatz × (Anzahl Zinstage / 360)

### 2. Vollverwässerte Anteile bestimmen
Basis: Stammkapital der Gesellschaft (in EUR, entspricht Anteilszahl bei EUR 1 Nennwert je Anteil) + ausgegebene ESOP-Optionen (vollverwässert). Vor Wandlung, vor Kapitalerhöhung der neuen Investoren.

### 3. Drei Preise berechnen
Preis A = Pre-Money / Vollverwässerte Anteile
Preis B = (1 − Discount) × Pre-Money / Vollverwässerte Anteile
Preis C = Cap / Vollverwässerte Anteile

### 4. Wandlungspreis bestimmen
Wandlungspreis = MIN(Preis A, Preis B, Preis C)
Begründung MIN: Lender soll immer den günstigsten Preis (aus seiner Sicht) erhalten.

### 5. Anteilszahl berechnen und aufrunden
Rohwert = C / Wandlungspreis
Neue Anteile = ⌈Rohwert⌉ (aufrunden auf nächste ganze Zahl gemäß § 5 Abs. 1 GmbHG; Nennwert muss mindestens EUR 1 je Anteil betragen)
Nennbetrag neue Anteile = Neue Anteile × EUR 1

### 6. Kapitalrücklage berechnen
Wandlungssumme C − Nennbetrag neue Anteile = Einlage in Kapitalrücklage (§ 272 Abs. 2 Nr. 4 HGB). Der Lender bringt seine Forderung in Höhe von C ein; der den Nennbetrag übersteigende Betrag geht in die Kapitalrücklage.

## Vollständige Beispielrechnung (Qualified Financing, Cap-Trigger)

| Schritt | Formel | Wert |
|---|---|---|
| Darlehensbetrag | — | EUR 250000 |
| Zinstage | 01.06.2025 bis 31.05.2027 = 730 Tage | 730 |
| Zinsen | 250000 × 0.05 × 730/360 | EUR 25694 |
| Wandlungssumme C | 250000 + 25694 | EUR 275694 |
| Vollverwaesserte Anteile | Stammkapital EUR 100 → 100 Anteile | 100 |
| Preis A (Rundenpreis, Pre-Money EUR 6 Mio) | 6000000 / 100 | EUR 60000 |
| Preis B (zwanzig Prozent Discount) | 0.8 × 6000000 / 100 | EUR 48000 |
| Preis C (Cap EUR 4 Mio) | 4000000 / 100 | EUR 40000 |
| Wandlungspreis (MIN) | MIN(60000; 48000; 40000) | EUR 40000 |
| Rohwert Anteile | 275694 / 40000 | 6.892 |
| Neue Anteile (aufgerundet) | ⌈6.892⌉ | 7 |
| Nennbetrag neue Anteile | 7 × EUR 1 | EUR 7 |
| Kapitalrücklage | 275694 − 7 | EUR 275687 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Vollverwaesserte Anteile falsch ermittelt | Falsche Preisberechnung | ESOP-Pool strittig | Vollständig dokumentiert |
| Zinsen nicht einbezogen | Wandlungssumme zu gering | Zinsen geschätzt | Exakt berechnet |
| Cap unter aktuellem Preis A und B | Cap immer massgeblich | Cap leicht unter | Cap deutlich unter |
| Differenzhaftung bei Überbewertung | Gesellschafter persönlich haftbar (§ 9 GmbHG) | Wertgutachten fehlt | Werthaltigkeitsprüfung vorhanden |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/sacheinlagebericht-werthaltigkeit/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 5 und 55 ff. sowie HGB § 272 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 5 Abs. 1 GmbHG (Mindest-Nennbetrag 1 EUR pro Anteil, Aufrundung) → § 56 Abs. 2 GmbHG (Differenzhaftung bei Unterschreitung Sachwert) → § 272 Abs. 2 Nr. 4 HGB (Kapitalrücklage für Wandlungsagio) → §§ 488 ff. BGB (Zinslauf bis Wandlungsstichtag) → § 138 BGB (Sittenwidrigkeit bei Preis-Manipulation)

## 2. `wandlungspruefung-trigger-liquidation`

**Fokus:** Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Prüfprotokoll Liquidationsszenarien. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing).

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

*(Keine verifizierten BGH-Entscheidungen zum Wandlungsrecht bei Liquidation Event in der Rechtsprechungsdatenbank nachweisbar; frühere Zitate entfernt.)*

### Normen-Ergänzung

§ 161 UmwG (Spaltung als Liquidation Event?) → § 2 UmwG (Verschmelzung als Exit) → §§ 60 ff. GmbHG (Liquidation GmbH) → § 39 InsO (Nachrang bei Insolvenz) → § 15 GmbHG (Share Deal — Anteilsübertragung)

<!-- AUDIT 27.05.2026
Geprüfte AZ (task_254.json, 3 Probleme):
Alle Löschungen gemäß Reparaturregel "bei Zweifel löschen". Frontmatter unverändert.
-->
