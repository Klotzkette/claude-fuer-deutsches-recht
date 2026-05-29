---
name: zv-pfaendungstabelle-2025
description: "Lohnpfaendung oder Rentenpfaendung ist beantragt und der pfaendbare Betrag muss konkret berechnet werden. Pfaendungsfreigrenzenbekanntmachung 1.7.2025 gueltig bis 30.6.2026. Prüfraster: Freibetrag § 850c ZPO Unterhaltsstaffel Pfaendungsstufen P-Konto-Sockel § 850k ZPO privilegierte Berechnung § 850d ZPO Unterhalt. Output: Berechnungsprotokoll pfaendbarer Betrag mit Stufen. Abgrenzung zu zv-pfueb-arbeitsentgelt (PfUeB-Antrag) und zv-pfueb-bank (Kontopfaendung)."
---

# Pfändungstabelle 1.7.2025

## Triage zu Beginn

1. Handelt es sich um Arbeitseinkommen (§ 850c ZPO) oder selbstständiges Einkommen (§ 850i ZPO)?
2. Wie viele unterhaltsberechtigte Personen sind zu berücksichtigen?
3. Handelt es sich um privilegierte Unterhaltspfändung (§ 850d ZPO) oder reguläre Pfändung?
4. Hat der Schuldner ein P-Konto — wenn ja, Sockelbetrag und Erhöhungen (§ 850k ZPO) berechnen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 850a ZPO — Unpfändbare Bezüge (Sonderzuwendungen, Aufwandsentschädigungen)
- § 850c ZPO — Pfändungsfreigrenze (Tabelle, jährlich angepasst)
- § 850d ZPO — privilegierte Unterhaltspfändung (geringerer Selbstbehalt)
- § 850f ZPO — Erhöhung durch Gericht aus persönlichen Gründen
- § 850i ZPO — Pfändung bei selbstständigem Einkommen
- § 850k ZPO — Pfändungsschutzkonto (P-Konto), Sockelbetrag und Erhöhungen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
- Pfändungsfreigrenzenbekanntmachung 2025 vom 11.4.2025 (BGBl. 2025 I Nr. 110), in Kraft 01.07.2025 bis 30.06.2026
- Quelle BGBl.: https://www.recht.bund.de/bgbl/1/2025/110/VO.html
- Quelle gesetze-im-internet: https://www.gesetze-im-internet.de/pf_ndfreigrbek_2025/BJNR06E0A0025.html
- nächste Anpassung 01.07.2026 (§ 850c Abs. 4 ZPO – jährlich am 1. Juli entsprechend der Entwicklung des Grundfreibetrags § 32a EStG)

## Gültigkeit der aktuellen Tabelle

Die Bekanntmachung gilt vom **1.7.2025 bis 30.6.2026**. Die nächste Anpassung erfolgt zum 1.7.2026 (§ 850c Abs. 4 ZPO jährlich). Der Skill prüft bei jeder Berechnung das Tagesdatum – nach dem 30.6.2026 muss `werkzeuge/pfaendungsrechner.py` aktualisiert werden.

> ⚠️ **Auto-Warnung ab 1.6.2026:** Wenn das System-Datum innerhalb von 30 Tagen vor Ablauf der Tabelle (≥ 1.6.2026) liegt, gibt der Skill und das Werkzeug einen Warntext aus, dass eine neue Pfändungsfreigrenzenbekanntmachung des BMJ veröffentlicht und in die Tabelle übernommen werden muss. Pflicht-Quellen: Pfändungsfreigrenzenbekanntmachung 2026 (BGBl. I); BMJ-Pressemitteilung; Konsultation in `juris`/`beck-online`. Verwendung der alten Eckwerte nach 30.6.2026 = Pfändungsfehler mit Aufhebungspotential.

## Eckwerte (aus Tabelle, dezimal mit Punkt)

Aktuelle Eckdaten (Tabelle 01.07.2025 bis 30.06.2026, BGBl. 2025 I Nr. 110):

- Grundfreibetrag ohne Unterhaltspflichten: 1.555,00 EUR netto / Monat (§ 850c Abs. 1 Nr. 1 ZPO i.V.m. Pfändungsfreigrenzenbekanntmachung 2025).
- Erhöhung erste unterhaltsberechtigte Person: 585,23 EUR (§ 850c Abs. 2 Satz 1 ZPO).
- Erhöhung jede weitere Person (2. bis 5. Person): 326,04 EUR (§ 850c Abs. 2 Satz 2 ZPO).
- Vollpfändungsgrenze: 4.766,99 EUR (§ 850c Abs. 3 Satz 3 ZPO).
- Netto wird vor Berechnung auf den nächsten vollen 10-EUR-Schritt abgerundet (§ 850c Abs. 5 ZPO).
- P-Konto-Sockel § 850k ZPO: 1.560,00 EUR (AG SBV-Bescheinigung Stand 01.07.2025).
- Pfändbarer Betrag wird nach unten gerundet (§ 850c Abs. 5 ZPO i.V.m. Tabellenmethode).
- Alle exakten Werte im `werkzeuge/pfaendungsrechner.py` (Single Source of Truth).

Steigerung gegenueber Vorjahresfassung:

- Grundfreibetrag von 1.491,75 EUR auf 1.555,00 EUR
- Erhoehungsbetrag 1. Unterhaltspflicht von 561,43 EUR auf 585,23 EUR
- Vollpfaendungsgrenze von 4.573,10 EUR auf 4.766,99 EUR

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

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
