# Plugin `steuerberater-werkzeuge`

Steuerberater-Werkzeugbox für die Krisenfrüherkennung nach deutschem Recht (StaRUG § 102, InsO §§ 17, 19, IDW S 6/S 11). Zielgruppe: Steuerberater, Wirtschaftsprüfer mit Steuerberatungsmandat, GmbH-Geschäftsführer und Finanzleitungen in der Sanierungspraxis. Das Plugin deckt die **Krisenfrühphase** ab – Erkennung, Dokumentation und Hinweispflicht-Auslösung – bevor insolvenzrechtliche Formalverfahren notwendig werden.

## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `bwa-sus-bilanz-pruefung` | Automatisierte Prüfung von BWA, SuSa und Bilanz auf Krisensignale; Auslösung der **Hinweispflicht des Steuerberaters** nach § 102 StaRUG (BGH-Vorläufer: IX ZR 285/14, BGHZ 213, 374) |

Die eigentliche **rollierende Liquiditätsplanung** (3-Wochen-Test, 13/26/52-Wochen-Plan, insolvenzrechtliche Sicht) ist in das eigene Plugin [`liquiditaetsplanung`](../liquiditaetsplanung/) ausgelagert, damit sie sowohl von Steuerberatern als auch von Sanierungsberatern und Insolvenzverwaltern direkt genutzt werden kann.

## Abgrenzung zu den Schwester-Plugins

- `steuerberater-werkzeuge` (dieses Plugin) ist **krisenfrüh** ausgerichtet: Es erkennt Warnsignale in Finanzkennzahlen und dokumentiert die Hinweispflicht nach § 102 StaRUG.
- `liquiditaetsplanung` liefert die **rollierenden Liquiditätsvorschauen** (3 Wochen / 13 / 26 / 52 Wochen) mit Ampel nach BGH BGHZ 163, 134 und Fortführungsprognose nach IDW S 6/S 11.
- `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Subsumtion für Zahlungsunfähigkeit (§ 17 InsO), Überschuldung (§ 19 InsO), Antragspflicht (§ 15a InsO).

**Übergabe:** Sobald der `bwa-sus-bilanz-pruefung`-Skill eine unmittelbare Insolvenzreife indiziert oder der `liquiditaetsvorschau-3wochen`-Skill aus `liquiditaetsplanung` ein 🔴-Flag erzeugt, ist zum Plugin `insolvenzrecht` zu wechseln oder ein Insolvenzanwalt einzuschalten.

## Rechtlicher Rahmen

- **StaRUG** § 102 – Hinweispflicht des Steuerberaters und beratender Berufe bei Krisensignalen
- **InsO** § 17 – Zahlungsunfähigkeit (Abgrenzungsnorm zur Krisenfrüherkennung)
- **InsO** § 19 – Überschuldung und Fortbestehensprognose (IDW S 6-Bezug)
- **IDW S 6** – Anforderungen an Sanierungskonzepte
- **IDW S 11** – Beurteilung des Vorliegens von Insolvenzeröffnungsgründen

## Leitentscheidungen

- BGH, Urt. v. 26.01.2017 – IX ZR 285/14, BGHZ 213, 374 – Steuerberater-Hinweispflicht bei Insolvenzreife (Vorläufer § 102 StaRUG)

## Standardliteratur

- *BeckOK StaRUG* (Skauradszun), 8. Ed. Stand 04.2025, § 102
- *Uhlenbruck/Mock*, InsO, 16. Aufl. 2024
- *IDW S 11* – Beurteilung des Vorliegens von Insolvenzeröffnungsgründen (jeweils aktuell)
- *IDW S 6* – Anforderungen an Sanierungskonzepte (jeweils aktuell)

## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.
