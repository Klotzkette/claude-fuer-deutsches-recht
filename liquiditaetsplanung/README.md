# Plugin Liquiditätsplanung (`liquiditaetsplanung`)

Rollierende Liquiditätsplanung und Krisenfrüherkennung nach deutschem Recht — gebündelt für Steuerberater, Sanierungsberater, GmbH-Geschäftsleitung und Insolvenzverwalter. Maßstab ist die BGH-Rechtsprechung zu § 17 InsO (BGHZ 163, 134 – 10-%-Lücke, 3-Wochen-Horizont) und die berufsständischen Verlautbarungen IDW S 6 (Sanierungskonzepte) und IDW S 11 (Insolvenzeröffnungsgründe).

> **Hinweis:** Dieses Plugin enthält schlanke **Routing-Skills** und deklariert die Plugins [`steuerberater-werkzeuge`](../steuerberater-werkzeuge/) und [`insolvenzrecht`](../insolvenzrecht/) als Abhängigkeiten. Die eigentliche Fachlogik bleibt in den Quell-Plugins; Liquiditätsplanung bietet den einheitlichen Einstieg.

## Enthaltene Skills (Bündel)

| Skill | Heimatplugin | Zweck |
|---|---|---|
| `liquiditaetsvorschau-3wochen` | `steuerberater-werkzeuge` | Kurzfrist-Test über 3 Wochen nach § 17 InsO; löst Ampel und Hinweis auf § 15a InsO-Antragspflicht aus |
| `liquiditaetsvorschau-3-6-12-monate` | `steuerberater-werkzeuge` | Rollierende 13/26/52-Wochen-Vorschau mit IDW-S-6-Fortführungsprognose und Excel-Export |
| `liquiditaetsvorschau-insolvenzrechtlich` | `insolvenzrecht` | Gerichtsfähige Liquiditätsbilanz als Beweismittel für § 17 InsO und Fortbestehensprognose § 19 InsO |

## Wann welcher Skill?

- **Wöchentliche Geschäftsführerrunde, frühe Krise**: `liquiditaetsvorschau-3wochen` als Ampel-Routine. Solange grün → kein Handeln, gelb → Engpässe planen, rot → sofort eskalieren.
- **Sanierungskonzept, Bankgespräch, StaRUG-Vorbereitung**: `liquiditaetsvorschau-3-6-12-monate` mit Best/Base/Worst-Sensitivität und IDW-S-6-Matrix.
- **Antragspflicht-Prüfung, Gläubigerantrag, gerichtliche Beweisführung**: `liquiditaetsvorschau-insolvenzrechtlich` aus dem Plugin `insolvenzrecht`.

## Rechtlicher Rahmen

- **§ 17 InsO** – Zahlungsunfähigkeit (10-%-Lücke / 3-Wochen-Horizont nach BGH BGHZ 163, 134)
- **§ 18 InsO** – drohende Zahlungsunfähigkeit (24-Monats-Prognose)
- **§ 19 InsO** – Überschuldung und Fortbestehensprognose
- **§ 15a InsO** – Insolvenzantragspflicht (3 Wochen / 6 Wochen)
- **§ 1 StaRUG** – Krisenfrüherkennungspflicht der Geschäftsleitung
- **§ 102 StaRUG** – Hinweispflicht beratender Berufe (Steuerberater)

## Leitentscheidungen

- BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 (Zahlungsunfähigkeit: 10-%-/3-Wochen-Schema)
- BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 (Indizienkatalog Zahlungsunfähigkeit)
- BGH, Urt. v. 19.11.2019 – II ZR 233/18, NJW 2020, 1809 (Fortbestehensprognose § 19 Abs. 2 InsO)
- BGH, Urt. v. 09.10.2012 – II ZR 298/11, BGHZ 195, 42 (insolvenzrechtliche vs. handelsbilanzielle Überschuldung)
- BGH, Urt. v. 26.01.2017 – IX ZR 285/14, BGHZ 213, 374 (Steuerberater-Hinweispflicht – Vorläufer § 102 StaRUG)

## Standardliteratur

- *K. Schmidt/Herchen*, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 InsO
- *Uhlenbruck/Mock*, InsO, 16. Aufl. 2024, § 19 InsO
- *Pape/Schaltke*, in: Pape/Uhländer, StaRUG, 1. Aufl. 2021, § 1 StaRUG
- **IDW S 6** – Anforderungen an die Erstellung von Sanierungskonzepten
- **IDW S 11** – Beurteilung des Vorliegens von Insolvenzeröffnungsgründen

## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.
