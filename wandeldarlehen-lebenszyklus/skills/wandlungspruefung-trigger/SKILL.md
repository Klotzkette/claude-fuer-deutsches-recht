---
name: wandlungspruefung-trigger
description: "Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen wenn kein qualifiziertes Finanzierungsereignis eingetreten ist. §§ 488 ff. BGB Fälligkeit. Prüfraster: Laufzeitenddatum Wandlungsrecht Wandlungspflicht Rückzahlungsalternative Preisbestimmung. Output: Prüfprotokoll Handlungsempfehlung. Abgrenzung: nicht für Qualified-Financing-Trigger (wandlungsprüfung-trigger-qualified-financing) im Wandeldarlehen Lebenszyklus."
---

# Wandlungsprüfung – Trigger Maturity (Laufzeitablauf)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Wandeldarlehensvertrag (§§ 2.1, 4.2 lit. e, 4.10)
- Startdatum der Festen Laufzeit (Datum vollständiger Unterzeichnung)
- Enddatum (Startdatum plus zwei Jahre)
- Fall-back-Bewertung aus § 4.10 (Pre-Money EUR bei Maturity)
- Darlehensbetrag + aufgelaufene Zinsen zum Maturity-Stichtag
- Ist innerhalb der Laufzeit ein Wandlungsereignis nach § 4.2 lit. b bis d eingetreten?

## Rechtlicher Rahmen

### Primärnormen
- § 2.1 Wandeldarlehensvertrag (Feste Laufzeit – kein Kündigungsrecht)
- § 4.2 lit. e Wandeldarlehensvertrag (Ablauf Feste Laufzeit als Wandlungsereignis)
- § 4.10 Wandeldarlehensvertrag (Fall-back-Bewertung bei Maturity)
- § 5 Abs. 1 GmbHG (Mindestanteilsnennwert EUR 1)
- § 271 BGB (Fälligkeit bei bestimmter Zeit)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Laufzeitprüfung
Startdatum = Datum vollständiger Unterzeichnung durch alle vier Parteien (§ 2.1). Enddatum = Startdatum + zwei Jahre (kalendarisch, keine Bankarbeitstage). Ist das aktuelle Datum ≥ Enddatum? → Maturity eingetreten.

### 2. Prüfung vorangegangener Ereignisse (§ 4.10 Satz 2)
Ist innerhalb der Laufzeit ein Liquidationsereignis (§ 4.2 lit. b bis d) eingetreten? Wenn ja: Lender hat Wahlrecht zwischen Wandlung (zu Fall-back-Bewertung) und Fälligstellung (Rückzahlung + Zinsen, § 2.5).

### 3. Fall-back-Bewertung anwenden
Wandlungspreis = Fall-back-Bewertung (Pre-Money EUR) / Anteile vor Wandlung (vollverwässert).
Wandlungssumme C = Darlehen + aufgelaufene Zinsen (Stichtag = Enddatum).
Neue Anteile = C / Wandlungspreis (aufrunden auf nächsten EUR, § 5 Abs. 1 GmbHG).

### 4. Wandlungserklärung auslösen oder Fälligstellung wählen
Falls nur Maturity ohne vorangegangenes Liquidationsereignis: automatische Wandlung, Lender erklärt Wandlung per Textform. Falls vorangegangenes Liquidationsereignis: Lender wählt innerhalb zwei Wochen.

### 5. Zinsen berechnen (Stichtag Maturity)
Zinsen = Darlehensbetrag × Zinssatz × (Tage ab Auszahlung bis Enddatum / 360). Act/360-Basis.

### 6. Übergabe an Kapitalerhöhungsprozess
Nach Wandlungserklärung: Gesellschaft beruft Gesellschafterversammlung ein (§ 4.9). Skills `gesellschafterbeschluss-kapitalerhoehung` und `notar-paket-uebermittlung` aufrufen.

## Beispielrechnung Maturity

| Parameter | Wert |
|---|---|
| Darlehensbetrag | EUR 250000 |
| Laufzeit | 2 Jahre = 730 Tage |
| Zinsen (730 Tage, fünf Prozent) | EUR 250000 × 0.05 × (730/360) = EUR 25694 |
| Wandlungssumme C | EUR 275694 |
| Fall-back-Bewertung (Pre-Money) | EUR 4000000 |
| Anteile vor Wandlung | 100 |
| Wandlungspreis | EUR 40000 je Anteil |
| Neue Anteile | 275694 / 40000 = 6.89 → 7 |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Keine Fall-back-Bewertung vereinbart | Wandlungsbetrag unbestimmt | Grobe Schätzung | Klarer EUR-Wert |
| Gesellschaft in Insolvenz bei Maturity | Wandlung blockiert, Rangrücktritt greift | Insolvenzantrag gestellt | Gesellschaft solvent |
| Lender will weder wandeln noch zahlen | Unklarheit über Rechtslage | Verhandlung läuft | Klares Wahlrecht ausgeübt |
| Laufzeitende strittig | Unterzeichnungsdatum unklar | Näherungsdatum | Unterzeichnungsdatum belegt |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 55 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 488 ff. BGB (Fälligkeit bei Maturity) → §§ 135, 143 InsO (Anfechtung Rückzahlung Gesellschafterdarlehen) → § 39 InsO (Nachrang bei Wandlung nach Insolvenz) → § 315 BGB (Wahlrecht des Darlehensgebers bei Maturity) → §§ 55, 56 GmbHG (Kapitalerhöhung nach Wandlungsausübung)

