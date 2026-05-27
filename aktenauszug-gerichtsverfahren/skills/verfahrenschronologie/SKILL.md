---
name: verfahrenschronologie
description: "Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben. Normen §§ 222 517 520 ZPO Fristberechnung."
---

# Verfahrenschronologie

## Zweck

Die Verfahrenschronologie erfasst alle prozessualen Schritte in zeitlicher Reihenfolge. Sie unterscheidet sich von der Sachverhaltschronologie dadurch, dass sie ausschließlich innerhalb des Verfahrens liegende Handlungen und Ereignisse abbildet.

## Triage — kläre vor Erstellung

1. Liegt die Zustellungsurkunde der Klageschrift vor? (Fristbeginn für Klageerwiderung)
2. Wurden alle Urteile zugestellt? (Berufungsfrist läuft ab Zustellung!)
3. Haben beide Parteien Schriftsätze vorgelegt? Welche?
4. Sind Vollstreckungsmaßnahmen eingeleitet? (Pfändungsbeschluss, Zwangshypothek)

## Zentrale Normen (Verfahrensrecht)

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung im Verfahren
- §§ 517-520 ZPO — Berufung und Begründung (Fristen: 1 Monat / 2 Monate)
- §§ 548-551 ZPO — Revision (Fristen: 1 Monat / 2 Monate)
- § 329 ZPO — Verkündung von Beschlüssen
- § 310 ZPO — Verkündung des Urteils
- § 929 Abs. 2 ZPO — Vollziehungsfrist bei einstweiliger Verfügung (1 Monat)
- §§ 704-945 ZPO — Zwangsvollstreckung

## Rechtsprechung zu Verfahrensfristen und Zustellung

- BGH, Beschl. v. 14.01.2020 - VIII ZB 4/19, NJW 2020, 757 — Zur Berechnung der Berufungsfrist: Fristbeginn ist der Tag der Zustellung, nicht der Tag der Kenntnisnahme; Zustellungsurkunde ist massgeblicher Nachweis.
- BGH, Beschl. v. 22.05.2019 - VII ZB 53/17, NJW 2019, 2479 — Fehlerhafte Zustellung setzt Fristlauf nicht in Gang; Partei kann sich auf Fehler der Zustellung berufen auch wenn tatsächliche Kenntnis vorhanden war.
- BGH, Beschl. v. 26.11.2019 - VIII ZB 67/18, NJW 2020, 384 — Zur Schriftsatzfrist des § 132 Abs. 3 ZPO: richterliche Verlängerung setzt erhebliche Gründe voraus; wiederholte Verlängerung erhöht Anforderungen.
- BGH, Urt. v. 05.03.2015 - III ZR 55/14, NJW 2015, 1872 — Prozessuale Fristen nach Urteilsverkündung: Revisionsfrist läuft auch wenn schriftliches Urteil noch nicht vorliegt; Verkündung allein reicht aus.

## Kommentarliteratur

- Thomas/Putzo ZPO, § 222 Rn. 1 ff. (Fristberechnung)
- Zöller/Heßler ZPO, § 517 Rn. 1 ff. (Berufungsfrist)
- MüKo ZPO/Rimmelspacher § 548 Rn. 1 ff. (Revisionsfrist)

## Was gehört hinein

- Klageeingang / Antragseingang beim Gericht
- Zahlung des Gerichtskostenvorschusses
- Zustellung der Klageschrift / des Arrestgesuchs
- Klageerwiderung und alle weiteren Schriftsätze (mit Datum)
- Richterliche Verfügungen und Hinweisbeschlüsse
- Beweisbeschlüsse
- Terminsladungen
- Mündliche Verhandlungen (mit Ergebnis / Protokollvermerk)
- Beweisaufnahme (Zeugenvernehmung, Sachverständigengutachten)
- Eingang von Gutachten
- Urteile und Beschlüsse (mit Tenor)
- Rechtsmittelfristen und Einlegung von Rechtsmitteln
- Vollstreckungsmaßnahmen

## Was nicht hinein gehört

- Außerprozessuale Ereignisse (→ Sachverhaltschronologie)
- Rechtliche Bewertungen der Schriftsätze

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des prozessualen Schritts] (Fundstelle: [Blatt])
- ** TT.MM.JJJJ — FRIST:** [Fristbezeichnung — z. B. Berufungsfrist] (Fundstelle: [Blatt])
```

## Hervorhebung von Fristen

Jede prozessrelevante Frist wird hervorgehoben und ans Ende der Chronologie als eigener Block wiederholt:

```
## Fristen und Termine (Übersicht)

| Frist / Termin | Datum | Status |
|---|---|---|
| Berufungsfrist (§ 517 ZPO) | TT.MM.JJJJ | laeuft |
| Begründungsfrist (§ 520 ZPO) | TT.MM.JJJJ | laeuft |
| Nächste mündliche Verhandlung | TT.MM.JJJJ | angesetzt |
```

## Beispiele

```
- **08.02.2023** Eingang der Klageschrift beim Landgericht Frankfurt am Main (Bl. 1)
- **15.02.2023** Anforderung des Gerichtskostenvorschusses (Bl. 5)
- **22.02.2023** Einzahlung des Gerichtskostenvorschusses durch Klägerin (Bl. 7)
- **03.03.2023** Zustellung der Klageschrift an Beklagte (Bl. 9)
- **14.04.2023** Eingang der Klageerwiderung (Bl. 12-45)
- **20.06.2023** Terminsladung zur mündlichen Verhandlung am 15.09.2023 (Bl. 48)
- **15.09.2023** Mündliche Verhandlung; Beweisbeschluss über Einholung Sachverständigengutachten (Bl. 60-62)
- **10.01.2024** Eingang des Sachverständigengutachtens (Bl. 80-140)
- **05.04.2024** Verkündung des Urteils; Klage abgewiesen (Bl. 200-215)
- **05.05.2024 — FRIST:** Berufungsfrist gemäß § 517 ZPO (einen Monat ab Zustellung)
```

## Besonderheiten nach Verfahrensart

**Eilverfahren:** Vollziehungsfrist des § 929 Abs. 2 ZPO besonders hervorheben.

**Strafverfahren:** Eröffnungsbeschluss, Ladungen, Hauptverhandlungstermine, Einlegung von Rechtsmitteln nach § 333 ff. StPO.

**Verwaltungsverfahren:** Widerspruchsverfahren als vorgelagerte Phase einschließen; Klagefrist des § 74 VwGO.

## Qualitätscheck

- [ ] Alle prozessualen Schritte erfasst?
- [ ] Chronologisch sortiert?
- [ ] Fristen hervorgehoben?
- [ ] Fristentabelle vorhanden?
- [ ] Keine außerprozessualen Ereignisse enthalten?
- [ ] Zustellungsdaten als Grundlage der Fristberechnung angegeben?
