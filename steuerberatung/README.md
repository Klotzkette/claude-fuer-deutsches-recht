# Steuerberatung-Plugin

Steuerberater-nahe Krisenfrüherkennungs-Skills nach deutschem Recht (StaRUG § 102, InsO §§ 17, 19, IDW S 6/S 11). Zielgruppe: Steuerberater, Wirtschaftsprüfer mit Steuerberatungsmandat, GmbH-Geschäftsführer und Finanzleitungen in der Sanierungspraxis. Das Plugin deckt die **Krisenfrühphase** ab – Erkennung, Dokumentation und Hinweispflicht-Auslösung – bevor insolvenzrechtliche Formalverfahren notwendig werden.

## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `bwa-sus-bilanz-pruefung` | Automatisierte Prüfung von BWA, SuSa und Bilanz auf Krisensignale; Auslösung der **Hinweispflicht des Steuerberaters** nach § 102 StaRUG (BGH-Vorläufer: IX ZR 285/14, BGHZ 213, 374) |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditätsvorschau über 3, 6 und 12 Monate aus Steuerberater-Sicht; Fortführungsprognose gem. IDW S 6, dauerhafte Lebensfähigkeit |
| `liquiditaetsvorschau-3wochen` | Kurzfristige 3-Wochen-Liquiditätsvorschau als Übergabeschnittstelle zum Insolvenzrecht-Plugin; Flag 🔴 löst Hinweis auf § 15a InsO-Antragspflichtfrist aus |

## Abgrenzung zum Insolvenzrecht-Plugin

Das Plugin `steuerberatung` ist **krisenfrüh** ausgerichtet: Es erkennt Warnsignale in Finanzkennzahlen, dokumentiert die Hinweispflicht nach § 102 StaRUG und erstellt Liquiditätsvorschauen für die betriebswirtschaftliche Sanierungsbegleitung.

Das Plugin `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Es liefert die rechtlichen Subsumtionsbausteine für den formellen Nachweis von Zahlungsunfähigkeit (§ 17 InsO) oder Überschuldung (§ 19 InsO), prüft Antragspflichtfristen nach § 15a InsO und erstellt gerichtsverwertbare Liquiditätsstati.

**Übergabe:** Sobald der Skill `liquiditaetsvorschau-3wochen` ein 🔴-Flag erzeugt oder der `bwa-sus-bilanz-pruefung`-Skill eine unmittelbare Insolvenzreife indiziert, ist zum Plugin `insolvenzrecht` zu wechseln oder ein Insolvenzanwalt einzuschalten.

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

## Apache-2.0

Dieses Plugin steht unter Apache License 2.0.
