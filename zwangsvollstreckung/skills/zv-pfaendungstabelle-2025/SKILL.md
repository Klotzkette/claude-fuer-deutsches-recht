---
name: zv-pfaendungstabelle-2025
description: "Lohnpfaendung oder Rentenpfaendung ist beantragt und der pfaendbare Betrag muss konkret berechnet werden. Pfaendungsfreigrenzenbekanntmachung 1.7.2025 gueltig bis 30.6.2026. Pruefraster: Freibetrag § 850c ZPO Unterhaltsstaffel Pfaendungsstufen P-Konto-Sockel § 850k ZPO privilegierte Berechnung § 850d ZPO Unterhalt. Output: Berechnungsprotokoll pfaendbarer Betrag mit Stufen. Abgrenzung zu zv-pfueb-arbeitsentgelt (PfUeB-Antrag) und zv-pfueb-bank (Kontopfaendung)."
---

# Pfändungstabelle 1.7.2025


## Triage zu Beginn

1. Handelt es sich um Arbeitseinkommen (§ 850c ZPO) oder selbstständiges Einkommen (§ 850i ZPO)?
2. Wie viele unterhaltsberechtigte Personen sind zu berücksichtigen?
3. Handelt es sich um privilegierte Unterhaltspfändung (§ 850d ZPO) oder reguläre Pfändung?
4. Hat der Schuldner ein P-Konto — wenn ja, Sockelbetrag und Erhöhungen (§ 850k ZPO) berechnen?

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 04.07.2018 - VII ZB 38/15, NJW 2018, 3109 — § 850c ZPO: Pfändungsfreigrenze ist nach dem Nettoeinkommen zu berechnen; auf den nächsten vollen 10-EUR-Schritt abrunden nach § 850c Abs. 5 ZPO.
- BGH, Beschl. v. 26.06.2014 - IX ZB 88/13, NJW 2014, 2738 — Drittschuldnererklärung: Bank muss korrekt über Pfändbarkeit des Kontoguthabens Auskunft geben; Fehler begründet Schadensersatz.
- BGH, Beschl. v. 10.11.2011 - VII ZB 64/10, NJW 2012, 234 — P-Konto-Bescheinigung: Schuldner hat Anspruch auf Bescheinigung über Erhöhungsbeträge; Bescheinigungsstelle muss unverzüglich ausstellen.
- BGH, Beschl. v. 01.10.2020 - IX ZB 4/20, NJW 2021, 73 — § 850d ZPO privilegierte Unterhaltspfändung: Selbstbehalt wird vom Vollstreckungsgericht festgesetzt; ohne Beschluss gilt Standardselbstbehalt nach Düsseldorfer Tabelle als Orientierung.

## Zentrale Normen

- § 850a ZPO — Unpfändbare Bezüge (Sonderzuwendungen, Aufwandsentschädigungen)
- § 850c ZPO — Pfändungsfreigrenze (Tabelle, jährlich angepasst)
- § 850d ZPO — privilegierte Unterhaltspfändung (geringerer Selbstbehalt)
- § 850f ZPO — Erhöhung durch Gericht aus persönlichen Gründen
- § 850i ZPO — Pfändung bei selbstständigem Einkommen
- § 850k ZPO — Pfändungsschutzkonto (P-Konto), Sockelbetrag und Erhöhungen

## Kommentarliteratur

- Zöller/Herget, ZPO, 35. Aufl. 2024, § 850c Rn. 1-20 (Pfändungsfreigrenze Berechnung)
- MüKo-ZPO/Smid, 6. Aufl. 2022, § 850d Rn. 1-20 (privilegierte Unterhaltspfändung)
- Thomas/Putzo, ZPO, 45. Aufl. 2024, § 850k Rn. 1-15 (P-Konto)

## Aufgabe

Verlässlich pfändbare Beträge berechnen. Falsche Pfändungsfreigrenzen sind der häufigste Vollstreckungsfehler – Skill kapselt die aktuelle Tabelle und das zugehörige Python-Werkzeug.

## Startet bei

- Lohnpfändung in Vorbereitung (`zv-pfueb-arbeitsentgelt`)
- Kontopfändung mit P-Konto-Berechnung (`zv-pfueb-bank` + § 850k ZPO)
- Schuldnerseite verlangt Anpassung der Freibeträge (`zv-abwehr-schuldner`)

## Rechtsgrundlagen

- § 850c ZPO – Pfändungsfreigrenze für Arbeitseinkommen
- § 850d ZPO – Unterhaltsforderungen (privilegiert, geringerer Freibetrag, vom Gericht festgesetzt)
- § 850f ZPO – Erhöhung durch Gericht aus persönlichen Gründen
- § 850k ZPO – Pfändungsschutzkonto, Sockelbetrag und Erhöhungen
- Pfändungsfreigrenzenbekanntmachung 2025 vom 11.4.2025 (BGBl 2025 I Nr. 110)
- nächste Anpassung 1.7.2026 (§ 850c Abs. 4 ZPO – jährlich am 1. Juli entsprechend der Entwicklung des Grundfreibetrags § 32a EStG)

## Gültigkeit der aktuellen Tabelle

Die Bekanntmachung gilt vom **1.7.2025 bis 30.6.2026**. Die nächste Anpassung erfolgt zum 1.7.2026 (§ 850c Abs. 4 ZPO jährlich). Der Skill prüft bei jeder Berechnung das Tagesdatum – nach dem 30.6.2026 muss `werkzeuge/pfaendungsrechner.py` aktualisiert werden.

> ⚠️ **Auto-Warnung ab 1.6.2026:** Wenn das System-Datum innerhalb von 30 Tagen vor Ablauf der Tabelle (≥ 1.6.2026) liegt, gibt der Skill und das Werkzeug einen Warntext aus, dass eine neue Pfändungsfreigrenzenbekanntmachung des BMJ veröffentlicht und in die Tabelle übernommen werden muss. Pflicht-Quellen: Pfändungsfreigrenzenbekanntmachung 2026 (BGBl. I); BMJ-Pressemitteilung; Konsultation in `juris`/`beck-online`. Verwendung der alten Eckwerte nach 30.6.2026 = Pfändungsfehler mit Aufhebungspotential.

## Eckwerte (aus Tabelle, dezimal mit Punkt)

Aktuelle Eckdaten (Tabelle 1.7.2025):

- Grundfreibetrag ohne Unterhaltspflichten: 1.555,00 EUR netto / Monat (§ 850c Abs. 1 Nr. 1 ZPO i.V.m. Pfändungsfreigrenzenbekanntmachung 2025).
- Erhöhung erste unterhaltsberechtigte Person: 585,23 EUR (§ 850c Abs. 2 Satz 1 ZPO).
- Erhöhung jede weitere Person (2. bis 5. Person): 326,04 EUR (§ 850c Abs. 2 Satz 2 ZPO).
- Vollpfändungsgrenze: 4.766,99 EUR (§ 850c Abs. 3 Satz 3 ZPO).
- Pfändbarkeitsquote im Tabellenbereich – unterhaltsabhängig nach § 850c Abs. 3 Sätze 1 und 2 ZPO: 0 Unterhaltspflichten 7/10; 1 UP 5/10; 2 UP 4/10; 3 UP 3/10; 4 UP 2/10; 5 UP 1/10. Ab der 6. Person Anpassung durch das Vollstreckungsgericht (§ 850f ZPO); das Werkzeug rechnet ab 6 UP mit den Tabellenwerten für 5 Personen und gibt einen Hinweis aus.
- Netto wird vor Berechnung auf den nächsten vollen 10-EUR-Schritt abgerundet (§ 850c Abs. 5 ZPO).
- P-Konto-Sockel § 850k ZPO: 1.560,00 EUR (AG SBV-Bescheinigung Stand 1.7.2025).
- Pfändbarer Betrag wird nach unten gerundet (§ 850c Abs. 5 ZPO i.V.m. Tabellenmethode).
- Alle exakten Werte im `werkzeuge/pfaendungsrechner.py` (Single Source of Truth).

Die Werte sind dimensions- und kommageführt im Werkzeug Single-Source-of-Truth; dieses SKILL.md nennt sie zur Orientierung. Komma-Zahlen sind im Body erlaubt, nicht im Frontmatter `description`.

## Workflow

1. **Inputs einholen**: Nettoeinkommen, Anzahl unterhaltsberechtigter Personen, ggf. Sonderzuwendungen, Privileg § 850d ZPO ja/nein.
2. **Python-Werkzeug aufrufen**: `python zwangsvollstreckung/werkzeuge/pfaendungsrechner.py --netto 2500 --unterhalt 1`.
3. **Output**: Freibetrag, pfändbarer Betrag, Pfändungsstufen, Hinweise zu § 850a ZPO Sonderzuwendungen.
4. **§ 850d ZPO privilegiert**: separat berechnen lassen mit `--privileg unterhalt --selbstbehalt 1450` o.ä.
5. **P-Konto** § 850k ZPO: Sockel und Erhöhungsbeträge ausgeben.
6. **Antragstext** für den PfÜB ergänzen.

## Privilegierte Unterhaltspfändung § 850d ZPO

- Selbstbehalt wird vom Vollstreckungsgericht festgelegt – Werte orientieren sich an der Düsseldorfer Tabelle (Selbstbehalt aktuell 1.450 EUR Erwerbstätiger gegenüber minderjährigen Kindern, Stand Tabelle 2025).
- Skill gibt eine Größenordnung an, weist aber auf die richterliche Festsetzung hin.

## P-Konto-Schutz § 850k ZPO – Erhöhungen

Erhöhungen müssen durch Bescheinigung (Schuldnerberatung, anerkannter Berater, Arbeitgeber, Familienkasse, Sozialleistungsträger) belegt werden:

- pro unterhaltsberechtigter Person
- Kindergeld
- einmalige Sozialleistungen
- Nachzahlungen

## Leitentscheidungen

- BGH 4.7.2018 – VII ZB 38/15 (Berechnung § 850c)
- BGH 26.6.2014 – IX ZB 88/13 (Drittschuldnererklärung)
- BGH 10.11.2011 – VII ZB 64/10 (P-Konto-Bescheinigung)

## Ausgabeformat

```
PFÄNDUNGSBERECHNUNG (Tabelle 1.7.2025)

Netto:                 EUR x
Unterhaltspflichten:   n
Pfändbar regulär:      EUR y / Monat
Pfändbar privilegiert: EUR z (§ 850d ZPO, Selbstbehalt EUR a)
P-Konto-Sockel:        EUR b / Monat (+ Erhöhungen)
Hinweis Sonderzuw.:    [§ 850a Nr. 3/4 ZPO]

Tabelle gültig bis:    30.6.2027
```

## Qualitätsgates

- Niemals Tabellenwerte 2019, 2021, 2022, 2023 verwenden.
- Niemals Bruttobetrag in die Tabelle einsetzen.
- Niemals § 850d ZPO ohne richterliche Festsetzung als feste Zahl ausgeben.
- Bei selbstständigem Einkommen Berechnung § 850i ZPO statt § 850c ZPO.
- Bei Sozialleistungen § 54 SGB I prüfen.

## Querverweise

- `zv-pfueb-arbeitsentgelt`, `zv-pfueb-bank`
- `zv-abwehr-schuldner`
- `werkzeuge/pfaendungsrechner.py`
- `forderungsmanagement-klagewerkstatt/skills/inkasso-zahlungsklage-ersteller`
