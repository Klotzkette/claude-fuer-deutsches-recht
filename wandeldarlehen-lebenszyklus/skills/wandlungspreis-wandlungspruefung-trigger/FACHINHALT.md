---
name: wandlungspreis-wandlungspruefung-trigger
description: "Für Wandlungspreis-Berechnung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Wandlungspreis-Berechnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Darlehensbetrag (EUR)
- Auszahlungsdatum und Stichtag Wandlung (für Zinsberechnung)
- Vertraglicher Zinssatz, Zinstagekonvention, Zinsbeginn, Zinsende und Einbeziehung der Zinsen in die Wandlung; keine Standardannahme von fünf Prozent oder act/360
- Pre-Money-Bewertung der Finanzierungsrunde (oder Fall-back-Bewertung bei Maturity)
- Vertraglicher Bewertungsnenner einschließlich vereinbarter Behandlung von Optionspool, anderen Darlehen und neuen Anteilen; tatsächliches Stammkapital gesondert erfassen
- Valuation Cap (EUR)
- Discount (Prozent)
- Aktuelles Stammkapital (EUR) und Nennwert je Anteil (Standard EUR 1)

## Rechtlicher Rahmen

### Primärnormen
- [Paragraf 5 Absätze 2 und 3 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__5.html): Nennbeträge in vollen Euro und Übereinstimmung ihrer Summe mit dem Stammkapital; keine gesetzliche Aufrundung eines wirtschaftlichen Wandlungsquotienten
- [Paragraf 55 Absatz 1 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__55.html): notarielle Aufnahme oder Beglaubigung der Übernahmeerklärung; Beschlussform gesondert nach Paragraf 53 Absatz 3 GmbHG
- § 56 GmbHG (Sacheinlage: Forderung aus Wandeldarlehen)
- [Paragraf 272 Absatz 2 HGB](https://www.gesetze-im-internet.de/hgb/__272.html): Ausgabeaufgeld nach Nummer 1 von anderen Zuzahlungen nach Nummer 4 unterscheiden
- § 9 GmbHG (Differenzhaftung bei Überbewertung der Sacheinlage)

## Vorgehen

### 1. Wandlungssumme C berechnen
C = vertraglich einzubeziehender Darlehensbetrag + mitwandelnde Zinsen. Bei vereinbarter einfacher Verzinsung: Zinsen = Kapital × vertraglicher Jahreszinssatz × Zinstage / vereinbarter Jahresnenner. Tilgungen, verschiedene Auszahlungen und abweichende Zinsabschnitte getrennt berechnen; fehlende Zinsabrede als offene Eingabe ausweisen.

### 2. Vollverwässerte Anteile bestimmen
Den Nenner aus der konkreten Vertragsdefinition zum vereinbarten Zeitpunkt herleiten. Stammkapital in Euro entspricht nur bei Geschäftsanteilen zu je einem Euro deren Anzahl. Optionspool, andere Wandeldarlehen und neue Finanzierungsanteile nur nach der jeweiligen Definition einbeziehen; keine rechtlich bereits entstandenen Anteile aus bloßen Rechengrößen ableiten.

### 3. Drei Preise berechnen
Bei entsprechend vereinbartem gemeinsamen Nenner: Preis A = Pre-Money / Nenner; Preis B = (1 − Discount) × Preis A; Preis C = Cap / Nenner. Abweichende Nenner oder eine nachrangige Anwendung des Discounts aus dem Vertrag übernehmen, nicht vereinheitlichen.

### 4. Wandlungspreis bestimmen
Nur bei vertraglich vereinbarter Alternativbegünstigung gilt Wandlungspreis = MIN(Preis A, Preis B, Preis C). Die konkrete Vorrangregel entscheidet; Discount nicht zusätzlich auf den Cap-Preis anwenden, sofern dies nicht vereinbart ist. Trigger einschließlich Mindestfinanzierungsvolumen und erforderlicher Erklärungen anhand der Belege feststellen.

### 5. Anteilszahl und Bruchteilsbehandlung prüfen
Rohwert = C / Wandlungspreis
Eine Rundung, Restzahlung oder verbleibende Forderung nur bei belegter Vereinbarung berücksichtigen. Ohne Regelung Rohwert und offene Bruchteilsbehandlung ausweisen; nicht eigenmächtig aufrunden oder einen Forderungsrest erlassen. Nennbetrag = vereinbarte Zahl neuer Geschäftsanteile × vereinbarter Nennbetrag; Paragraf 5 Absätze 2 und 3 GmbHG begründet keinen Anspruch auf Aufrundung.

### 6. Kapitalrücklage berechnen
Bei vollständig eingebrachtem, werthaltigem Wandlungsbetrag und Ausgabe neuer Anteile: Ausgabebetrag abzüglich Nennbetrag = Ausgabeaufgeld nach Paragraf 272 Absatz 2 Nummer 1 HGB. Forderungsrest, Werthaltigkeit und vereinbarte Einbringungsmechanik gesondert prüfen; ohne geklärten Vollzug keine endgültige Buchungsfreigabe erteilen.

## Vollständige Beispielrechnung (Qualified Financing, Cap-Trigger)

| Schritt | Formel | Wert |
|---|---|---|
| Darlehensbetrag | — | EUR 250000 |
| Vereinbarte Verzinsung | fünf Prozent, act/365, nach Vertrag 730 Zinstage, Zinsen wandeln mit | 730 Tage |
| Zinsen | 250000 × 0.05 × 730/365 | EUR 25000 |
| Wandlungssumme C | 250000 + 25000 | EUR 275000 |
| Vertraglicher Nenner | 25000 Geschäftsanteile zu EUR 1; kein Optionspool oder weiteres Darlehen | 25000 |
| Preis A (Pre-Money EUR 6 Mio) | 6000000 / 25000 | EUR 240 |
| Preis B (zwanzig Prozent Discount) | 0.8 × 240 | EUR 192 |
| Preis C (Cap EUR 4 Mio) | 4000000 / 25000 | EUR 160 |
| Vertraglich vereinbarte Alternativbegünstigung | MIN(240; 192; 160) | EUR 160 |
| Rohwert neuer Anteile | 275000 / 160 | 1718.75 |
| Bruchteilsregel fehlt | keine gesetzliche Aufrundung auf 1719 | Vereinbarung erforderlich |
| Nennbetrag und Ausgabeaufgeld | erst nach geklärter Anteilszahl und Restbehandlung | noch nicht freigegeben |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Vollverwaesserte Anteile falsch ermittelt | Falsche Preisberechnung | ESOP-Pool strittig | Vollständig dokumentiert |
| Zinsen nicht einbezogen | Wandlungssumme zu gering | Zinsen geschätzt | Exakt berechnet |
| Cap unter Preis A und B | Cap ohne Prüfung der Vertragsrangfolge angewandt | Rangfolge offen | Preiswahl entspricht belegter Vertragsregel |
| Differenzhaftung bei Überbewertung | Gesellschafter persönlich haftbar (§ 9 GmbHG) | Wertgutachten fehlt | Werthaltigkeitsprüfung vorhanden |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 5 und 55 ff. sowie HGB § 272 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Normen-Ergänzung

Paragraf 5 Absätze 2 und 3 sowie Paragraf 55 Absatz 4 GmbHG regeln die Nennbeträge, nicht die wirtschaftliche Rundung. Paragraf 272 Absatz 2 Nummer 1 HGB betrifft das Ausgabeaufgeld. Zinslauf, Preiswahl und Bruchteilsbehandlung bleiben anhand des Darlehensvertrags nachzuweisen; rechnerisches Ergebnis und rechtlicher Vollzug sind getrennte Freigabepunkte.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
