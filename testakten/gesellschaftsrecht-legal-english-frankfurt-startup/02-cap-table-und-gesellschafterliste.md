# 02 Cap Table und Gesellschafterliste

## Gesellschaft

Kometenfalter Systems GmbH
Sitz: Frankfurt am Main
Stammkapital: 30.000 EUR
Geschäftsanteile: lfd. Nr. 1 bis 30.000, jeweils 1 EUR Nennbetrag
Gegenstand: Entwicklung und Vertrieb von Software zur automatisierten Energieoptimierung in Gewerbeimmobilien

## Aktuelle Gesellschafterliste laut Notarentwurf vom 18.05.2026

| Gesellschafter | Geschäftsanteile | Nennbetrag | Prozent nominal |
| --- | --- | ---: | ---: |
| Kunigunde Reiter | Nr. 1 bis 12.000 | 12.000 EUR | 40,00 % |
| Meinhard Voss | Nr. 12.001 bis 21.000 | 9.000 EUR | 30,00 % |
| Walburga Stein | Nr. 21.001 bis 27.000 | 6.000 EUR | 20,00 % |
| Stahlauge Ventures GmbH | Nr. 27.001 bis 30.000 | 3.000 EUR | 10,00 % |

## Interner Cap Table der Gesellschaft

| Beteiligter | Current Shares | Current % | Notizen |
| --- | ---: | ---: | --- |
| Kunigunde Reiter | 12.000 | 40,00 % | Gründerin CEO |
| Meinhard Voss | 9.000 | 30,00 % | Gründer CTO |
| Walburga Stein | 6.000 | 20,00 % | Gründerin Product |
| Stahlauge Ventures GmbH | 3.000 | 10,00 % | Seed-Investor, 1x non-participating preference im Seed-SHA behauptet |

## Geplante Series A

- Northbridge Growth III SCS: Investment 4.800.000 EUR.
- Siegfried Krämer Angel Pool: Investment 400.000 EUR.
- Pre-money valuation laut Term Sheet: 12.000.000 EUR.
- Option Pool soll "increased to 12 percent on a fully diluted pre-money basis" werden.
- Bestehendes VSOP-Programm: 900 virtuelle Anteile zugesagt, davon 360 vested.
- Wandeldarlehen von Tante Ermelind Capital UG: 600.000 EUR principal, 8 Prozent Zins, 20 Prozent Discount, Valuation Cap 10.000.000 EUR, Wandlung bei Qualified Financing über 3.000.000 EUR.

## Offene Punkte

1. Der Cap Table der CFO-Datei enthält bereits "Series A Shares", obwohl die Kapitalerhöhung noch nicht beschlossen ist.
2. Der Option Pool ist in der Gesellschafterliste nicht sichtbar.
3. Das Wandeldarlehen ist in der Gesellschafterliste ebenfalls nicht sichtbar.
4. Northbridge rechnet den Option Pool pre-money, Kunigunde hatte post-money verstanden.
5. Der Seed-Investor verlangt, dass seine Seed-Präferenz in der Series-A-Dokumentation bestätigt wird.

## Cap Table v19 — saubere Trennung nach Slack-Thread

### V19a Current Cap Table, Stand 28.05.2026

| Position | Geschaeftsanteile | Prozent stamm | Bemerkung |
| --- | ---: | ---: | --- |
| Kunigunde Reiter | 12.000 | 40,00 | Stammanteile |
| Meinhard Voss | 9.000 | 30,00 | Stammanteile |
| Walburga Stein | 6.000 | 20,00 | Stammanteile |
| Stahlauge Ventures GmbH | 3.000 | 10,00 | Seed-Vorzugsanteile, 1x non-participating preference |
| **Summe ausgegeben** | **30.000** | **100,00** | entspricht Stammkapital 30.000 EUR |

VSOP: 900 virtuelle Anteile zugesagt, davon 360 vested. Keine echten Geschaeftsanteile. Cap-Table-Block separat, nicht in Summe oben.

Wandeldarlehen Tante Ermelind: Principal 600.000 EUR plus aufgelaufene Zinsen ca. 100.000 EUR per Stand 28.05.2026. Convertible, nicht in Summe oben.

### V19b Projected Post-Closing Cap Table (Szenario 1: Pool 12 Prozent pre-money)

Annahmen Szenario 1:

- Pre-Money 12.000.000 EUR auf fully diluted Basis.
- Pool wird **vor** Investment auf 12 Prozent fully diluted pre-money erweitert.
- Tante-Ermelind-Wandlung greift Valuation-Cap (10 Mio. EUR pre-money fully diluted).
- Series-A-Subscription 5.200.000 EUR.
- Pre-Money implizit nach Pool-Aufstockung und Convertible-Wandlung etwa 12 Mio. EUR.

| Position | Anteile vor Series A nach Pool-Shuffle | Prozent pre-money fully diluted | Anteile nach Series A | Prozent post-money fully diluted |
| --- | ---: | ---: | ---: | ---: |
| Kunigunde Reiter | 12.000 | 28,8 | 12.000 | 20,4 |
| Meinhard Voss | 9.000 | 21,6 | 9.000 | 15,3 |
| Walburga Stein | 6.000 | 14,4 | 6.000 | 10,2 |
| Stahlauge Ventures GmbH | 3.000 | 7,2 | 3.000 | 5,1 |
| Option Pool reserviert | 5.000 | 12,0 | 5.000 | 8,5 |
| Tante Ermelind aus Wandlung | 6.700 | 16,1 | 6.700 | 11,4 |
| Series A Northbridge | 0 | 0 | 13.640 | 23,2 |
| Series A Kraemer Angels | 0 | 0 | 1.135 | 1,9 |
| **Fully Diluted Summe** | **41.700** | **100,00** | **58.475** | **100,00** |

Berechnungslogik (Skizze, Senior-Review erforderlich):

- Bestehende Anteile 30.000.
- Pool-Reservierung 12 Prozent auf fully diluted **vor** Series A: Pool/(30.000 + Pool + Convertible-Anteile) = 0,12. Mit Convertible-Anteilen ca. 6.700 ergibt sich Pool ca. 5.000 Anteile.
- Convertible Wandlung zum Valuation Cap 10 Mio. EUR fully diluted: ca. 6.700 Anteile fuer Tante Ermelind.
- Series-A-Preis ca. 287,80 EUR je Anteil bei 12 Mio. EUR Pre-Money und 41.700 Anteilen fully diluted pre-money. Bei 5,2 Mio. EUR Investment ca. 18.075 zusaetzliche Anteile post-Pool. Aufteilung Northbridge zu Kraemer im Verhaeltnis 4,8 zu 0,4.

Hinweis: Diese Zahlen sind eine **Skizze**. Die exakten Wandlungs- und Pool-Anteile sind im Excel-Modell auszurechnen. Adelheid hat ausdruecklich verboten, sie ohne Verifikation an Northbridge zu kommunizieren.

### V19c Projected Post-Closing Cap Table (Szenario 2: Pool 12 Prozent post-money)

Annahmen Szenario 2:

- Pool wird **post-money** 12 Prozent fully diluted. Mathematisch traegt Northbridge den Pool anteilig mit.
- Series-A-Subscription unveraendert 5,2 Mio. EUR.

Wirtschaftlicher Effekt: Bestandsgesellschafter haben hier rund 1,5 Prozentpunkte hoehere Quoten als in Szenario 1, Northbridge etwas weniger. Vorrechnung im Excel-Modell, mit Mandantin am Tisch durchgehen.

## Stueck-fuer-Stueck-Rechnung mit Pruefschritten

Schritt 1: Stammkapital und ausgegebene Anteile (entspricht V19a oben).

Schritt 2: VSOP-Block separat ausweisen. Virtuelle Anteile fuehren nicht zu Geschaeftsanteilen. Cap-Table-Behandlung haengt vom Series-A-SHA ab.

Schritt 3: Wandeldarlehen mit Discount-Variante und Valuation-Cap-Variante rechnen, niedrigere Conversion Price greift. Annahme bei Series-A-Pre-Money 12 Mio. EUR: Valuation Cap wirkt.

Schritt 4: Pool-Shuffle ausrechnen, beide Szenarien (Pre-Money und Post-Money).

Schritt 5: Series-A-Preis je Anteil bestimmen, Subscription Amount durch Preis je Anteil teilen, Aufteilung Lead und Co-Investor nach Subscription-Anteilen.

Schritt 6: Fully-diluted-Summe pruefen, Quoten ausrechnen, Konsistenz mit Term-Sheet-Erwartung (etwa 25 Prozent Northbridge post-money fully diluted) verifizieren.

## Was Kunigunde wissen muss

- **Gesellschafterliste** ist die offizielle Liste der eingetragenen Geschaeftsanteile.
- **Cap Table** ist das interne Bild, das alles abbildet: Anteile, Optionen, Convertibles, virtuelle Beteiligungen.
- **Pre-Money-Pool-Shuffle** trifft wirtschaftlich die Gruender, weil die zusaetzlichen Pool-Anteile aus dem Pre-Money-Bestand herausgerechnet werden.
- **Wandeldarlehen Tante Ermelind** bekommt rechnerisch mehr Anteile als Investoren, die zum gleichen Zeitpunkt frisches Geld einbringen, weil Discount oder Valuation Cap greifen.
- **VSOP** verwaessert ebenfalls, sobald virtuelle Anteile in Vergleichsmechaniken einbezogen werden.

## Senior-Review-Gate vor jeder Aussenkommunikation

Kein Cap-Table-Zahlenwert geht an Northbridge oder Brackenmuir, bevor Adelheid die V19 abgezeichnet hat. Excel-Modell mit Pruefblatt, das alle Inputs gegen Quelldokumente verlinkt.
