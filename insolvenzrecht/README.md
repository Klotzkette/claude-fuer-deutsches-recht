# Insolvenzrecht-Plugin

Insolvenz- und sanierungsrechtliche Skills nach deutschem Recht (InsO, StaRUG, COVInsAG-Nachwirkungen). Zielgruppe: Insolvenzverwalter, beratende Rechtsanwälte (Insolvenz-/Sanierungsrecht), Geschäftsführer, Vorstände, Sanierungsberater, Wirtschaftsprüfer (IDW-S-11-/S-6-/S-9-Praxis).

## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `zahlungsunfaehigkeit-pruefung-17-inso` | Prüfung der Zahlungsunfähigkeit gem. § 17 InsO anhand BGH-Liquiditätsstatus (10%-/3-Wochen-Schwelle) |
| `ueberschuldung-pruefung-19-inso` | Zweistufige Überschuldungsprüfung gem. § 19 InsO: Fortbestehensprognose + insolvenzrechtlicher Überschuldungsstatus |
| `liquiditaetsvorschau-insolvenzrechtlich` | Rollierende 13-/26-/52-Wochen-Liquiditätsvorschau mit Ampel als Beweismittel für § 17 InsO und Fortbestehensprognose § 19 InsO; Excel-Export |
| `antragspflicht-15a-inso` | Höchstfrist nach § 15a InsO, Haftung bei Insolvenzverschleppung, Schutz Geschäftsführer/Vorstand |
| `glaeubigerantrag-pruefung` | Prüfung Zulässigkeit/Begründetheit eines Gläubigerantrags (§ 14 InsO), Glaubhaftmachung Forderung + Eröffnungsgrund |

## Abgrenzung zu den Schwester-Plugins

- Das Plugin [`steuerberater-werkzeuge`](../steuerberater-werkzeuge/) enthält `bwa-sus-bilanz-pruefung` — Prüfung BWA/SuSa/Bilanz auf Krisensignale, **Hinweispflicht des Steuerberaters** nach § 102 StaRUG (BGH-Vorläufer IX ZR 285/14).
- Das Plugin [Liquiditätsplanung](../liquiditaetsplanung/) enthält die rollierenden Liquiditätsvorschauen 3 Wochen / 13 / 26 / 52 Wochen mit Ampel nach BGH BGHZ 163, 134 und Fortführungsprognose nach IDW S 6.

Dieses Plugin `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Es liefert die rechtlichen Subsumtionsbausteine und Beweismittel, wenn die Krise bereits eingetreten ist — Zeitpunkt der Zahlungsunfähigkeit, Überschuldungsstatus zum Stichtag, Antragspflichtfrist, Haftung Geschäftsleiter.

## Rechtlicher Rahmen (übergreifend)

- **InsO**: §§ 14, 15, 15a, 16, 17, 18, 19, 130, 131, 133, 142
- **StaRUG**: §§ 29 ff. (Restrukturierungsverfahren), § 102 (Hinweispflicht)
- **GmbHG**: § 64 a.F. (ersetzt durch § 15b InsO), § 30 (Auszahlungsverbot)
- **AktG**: § 92 Abs. 2 (Anzeigepflichten), § 93 (Sorgfaltspflicht)
- **HGB**: § 252 Abs. 1 Nr. 2 (going concern)
- **StGB**: §§ 283–283d (Bankrott, Verletzung der Buchführungspflicht), § 266a (Vorenthalten Arbeitsentgelt)

## Leitentscheidungen

- BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 (Zahlungsunfähigkeit: 10%-/3-Wochen-Schema)
- BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 (Indizienkatalog Zahlungsunfähigkeit)
- BGH, Urt. v. 13.06.2006 – IX ZR 92/04, BGHZ 168, 158 (Stundungen, Liquiditätsbilanz)
- BGH, Urt. v. 18.10.2010 – II ZR 151/09, NZG 2010, 1393 (Überschuldungsprognose)
- BGH, Urt. v. 13.07.2017 – IX ZR 290/14, NJW 2017, 3373 (insolvenzrechtl. Überschuldung)
- BGH, Urt. v. 23.06.2022 – IX ZR 75/21, NJW 2022, 3018 (Antragspflicht § 15a, Haftung)
- BGH, Urt. v. 26.01.2017 – IX ZR 285/14, BGHZ 213, 374 (Steuerberater-Hinweispflicht — Vorläufer § 102 StaRUG)

## Standardliteratur

- *Uhlenbruck*, InsO, 16. Aufl. 2024 (Hrsg. Uhlenbruck/Mock)
- *K. Schmidt*, InsO, 20. Aufl. 2023
- *MüKoInsO*, 4. Aufl. 2019 ff.
- *Pape/Uhländer*, StaRUG, 1. Aufl. 2021
- *BeckOK StaRUG*, hrsg. Skauradszun, 8. Ed. (Stand 04.2025)
- *IDW S 11* — Beurteilung des Vorliegens von Insolvenzeröffnungsgründen
- *IDW S 6* — Anforderungen an Sanierungskonzepte
- *IDW S 9* — Bescheinigungen nach §§ 50, 51 StaRUG

## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.
