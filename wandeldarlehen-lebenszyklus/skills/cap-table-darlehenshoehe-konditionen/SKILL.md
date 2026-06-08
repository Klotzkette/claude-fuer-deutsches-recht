---
name: cap-table-darlehenshoehe-konditionen
description: "Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money Wandlungspreis neue Anteile Verwasserung bestehende Gesellschafter. Output: Cap-Table-Vergleich Pre/Post Verwasserungsrechnung. Abgrenzung: nicht für Wandlungsmechanik (wandlungsmechanik-konzipieren) im Wandeldarlehen Lebenszyklus."
---

# Cap-Table Update – Pre-Money und Post-Money

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, unverzügliche Aktualisierung nach Wandlung) → § 15 GmbHG (Abtretung Anteile) → § 17 GmbHG (Mehrfachabtretung) → § 16 GmbHG (Gesellschafterstellung, Legitimationswirkung Liste) → § 55 GmbHG (Kapitalerhöhungsbeschluss, neue Anteile)

