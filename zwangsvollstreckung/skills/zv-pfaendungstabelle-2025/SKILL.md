---
name: zv-pfaendungstabelle-2025
description: "Berechnet pfändbare Beträge nach Pfändungsfreigrenzenbekanntmachung 1.7.2025 (gültig bis 30.6.2027). Liefert Freibetrag nach § 850c ZPO inklusive Unterhaltsstaffel, Pfändungsstufen, P-Konto-Sockel § 850k ZPO und privilegierte Berechnung § 850d ZPO. Ruft das Python-Werkzeug werkzeuge/pfaendungsrechner.py auf. Lädt bei jeder Berechnung pfändbarer Bezüge."
---

# Pfändungstabelle 1.7.2025

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

## Eckwerte (aus Tabelle, dezimal mit Punkt)

Aktuelle Eckdaten (Tabelle 1.7.2025):

- Grundfreibetrag ohne Unterhaltspflichten: 1.559,99 EUR netto / Monat (§ 850c Abs. 1 ZPO i.V.m. Aufrundung Abs. 5).
- Erhöhung erste unterhaltsberechtigte Person: 585,23 EUR.
- Erhöhung jede weitere Person: 326,04 EUR.
- Vollpfändungsgrenze: 4.766,99 EUR.
- Pfändbar nur der den Freibetrag übersteigende Teil, stufenweise mit den Quoten 3/10, 5/10, 7/10 bis zur Kappungsgrenze (alle exakten Werte im `werkzeuge/pfaendungsrechner.py`).
- P-Konto-Sockel § 850k ZPO: 1.560,00 EUR (AG SBV-Bescheinigung Stand 1.7.2025).

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
