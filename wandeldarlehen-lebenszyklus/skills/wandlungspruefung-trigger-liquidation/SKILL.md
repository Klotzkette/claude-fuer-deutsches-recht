---
name: wandlungspruefung-trigger-liquidation
description: "Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Prüfprotokoll Liquidationsszenarien. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing) im Wandeldarlehen Lebenszyklus: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Wandlungsprüfung – Trigger Liquidation Event

## Arbeitsbereich

Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung Zahlungsreihenfolge. Output: Prüfprotokoll Liquidationsszenarien. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing). Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
