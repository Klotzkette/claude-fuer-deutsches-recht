---
name: dokumenten-upload-formfehler-heilungs
description: "Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrechte. Output: strukturiertes Datenmemo mit Extraktionsergebnis. Abgrenzung: Extraktion und Triage; Detailprüfung in Spezialist-Skills im Wandeldarlehen Lebenszyklus."
---

# Dokumenten-Upload und Datenextraktion

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Hochgeladene Dokumente: Term Sheet, Share Purchase Agreement (SPA), Investor Rights Agreement (IRA), Shareholders Agreement (SHA), Beteiligungsvertrag
- Gesuchte Parameter: Pre-Money, Post-Money, Investitionsvolumen, Anteilsklassen, Nennwert, Vesting, ESOP, Liquidationspräferenzen, Anti-Dilution

## Rechtlicher Rahmen

### Primärnormen
- § 15 GmbHG (Anteilsklassen und Übertragung)
- § 272 HGB (Eigenkapitalausweis nach Klassen)
- § 194 AktG analog (Wandelschuldverschreibungen und Klassen – Orientierung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel-Extrakt Term Sheet

| Parameter | Wert | Quelle |
|---|---|---|
| Pre-Money-Bewertung | EUR 6000000 | Term Sheet Cl. 2.1 |
| Investitionsvolumen | EUR 1000000 | Term Sheet Cl. 2.1 |
| Anteilsklassen | Ordinary + Series A Preferred | Term Sheet Cl. 3 |
| Liquidationspräferenz Series A | 1x non-participating | Term Sheet Cl. 4 |
| ESOP-Pool | zehn Prozent (post-money) | Term Sheet Cl. 5 |
| Anti-Dilution | Broad-based weighted average | Term Sheet Cl. 6 |
| Qualifiziertes Financing nach WDV | Pre-Money ≥ EUR 4 Mio, Vol. ≥ EUR 500000 | WDV § 4.2 lit. a |
| Ist Qualified Financing? | Ja (beide Schwellen erfüllt) | Prüfung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Term Sheet nur als Absichtserklärung | Zahlen unverbindlich | Term Sheet mit Bindungswirkung unklar | Verbindliches Term Sheet |
| ESOP-Pool post-money ohne Klarstellung | Vollverwässerte Basis falsch berechnet | Unklar ob pre/post | Eindeutig pre-money |
| Liquidationspräferenz höher als 1x | Lender-Barausschüttung bevorzugt | Participating Preferred | Non-participating 1x |
| Kein Pre-Money im Dokument | Berechnung nicht möglich | Nur Post-Money | Pre-Money explizit |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG/HGB-Eigenkapitalausweis aktualisieren.

## Vertiefung — Relevante Normen

### Normen-Ergänzung und Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen

§ 12 HGB i.V.m. § 12 HRV (elektronische Einreichung Handelsregister) → Art. 25 eIDAS-VO (qualifizierte elektronische Signatur) → § 378 FamFG (Zurückweisung bei Formmängeln) → § 40 GmbHG (Einreichungspflicht Gesellschafterliste)

