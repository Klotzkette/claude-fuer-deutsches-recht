---
name: neutralitaetspruefung
description: "Prueft einen erstellten Aktenauszug auf unzulaessige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs. Massstab § 286 ZPO freie Beweiswuerdigung."
---

# Neutralitätsprüfung

## Zweck

Der Aktenauszug muss neutral formuliert sein — er gibt den Stand eines Verfahrens wieder, ohne eine Seite zu bevorzugen oder eine Erfolgsprognose abzugeben. Dieser Skill prüft einen erstellten Aktenauszug auf Neutralitätsverstöße und schlägt Korrekturen vor.

## Triage — kläre vor der Prüfung

1. Für wen ist der Aktenauszug bestimmt? (internes Arbeitsdokument / Übergabe an Mandant / Gericht)
2. Hat der Ersteller den Auftrag, die eigene Mandantsseite besonders darzustellen? (dann kein Aktenauszug, sondern Schriftsatz!)
3. Gibt es Stellen, die bewusst als subjektive Einschätzung des Anwalts markiert sind? (Diese sind zu entfernen oder zu kennzeichnen.)

## Normhintergrund

- § 286 Abs. 1 ZPO — Freie Beweiswürdigung des Gerichts; Aktenauszug darf keine Beweiswürdigungsprognosen enthalten
- § 138 ZPO — Wahrheitspflicht; auch interne Vermerke müssen den Sachverhalt korrekt abbilden
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot; gilt auch für interne Aktendokumentation

## Rechtsprechung zum Sachlichkeitsgebot und Neutralität

- BGH, Urt. v. 15.07.2021 - IX ZR 143/19, NJW 2021, 3131 — Anwaltshaftung wegen einseitiger und fehlerhafter Darstellung des Sachverhalts in internem Vermerk, der zur falschen Beratungsentscheidung führte.
- BVerfG, Beschl. v. 14.07.1987 - 1 BvR 537/81, BVerfGE 76, 171 — Zu den Anforderungen des rechtlichen Gehörs (Art. 103 Abs. 1 GG): vollständige und neutrale Darstellung des Prozessstoffs ist Grundvoraussetzung.
- BGH, Urt. v. 05.02.2009 - III ZR 164/08, NJW 2009, 987 — Interne Rechtsauskunft, die relevante Gegenargumente nicht berücksichtigt, begründet Haftung bei Fehlberatung nach § 280 Abs. 1 i.V.m. § 675 BGB.
- BGH, Beschl. v. 23.11.2017 - IX ZR 45/17, NJW 2018, 395 — Zur Sachverhaltsaufbereitung durch Anwalt: einseitige Darstellung zugunsten der eigenen Partei kann bei internen Dokumenten zur Haftung führen.

## Kommentarliteratur

- Zöller/Greger ZPO, § 286 Rn. 1 ff. (Freie Beweiswürdigung)
- Dittmann BRAO-Kommentar § 43a Rn. 1 ff. (Sachlichkeitsgebot)

## Verbotene Formulierungstypen

### Erfolgsprognosen (absolut verboten)

| Verboten | Erlaubt |
|---|---|
| „Die Klage wird Erfolg haben" | „Die Klage ist anhängig" |
| „Der Anspruch dürfte begründet sein" | „Die Klägerin macht [Anspruch] geltend" |
| „Die Verjährungseinrede greift durch" | „Die Beklagte erhebt die Verjährungseinrede" |
| „Das Gericht wird … erkennen" | „Das Gericht hat … nicht geäußert" |
| „offensichtlich unbegründet" | „nach Vortrag der Beklagten unbegründet" |

### Wertende Adjektive (zu vermeiden)

- substanzlos, unhaltbar, abwegig, überzeugend, zutreffend, unzutreffend
- zu Recht, zu Unrecht
- offensichtlich, eindeutig (ohne Quellenangabe)

### Parteiische Darstellung

- Ausführliche Wiedergabe des Vortrags einer Seite ohne entsprechende Gegenüberstellung der anderen Seite
- Formulierungen, die implizit eine Seite stärken („Trotz des klaren Wortlauts des Vertrags …")

## Prüfmethodik

### Schritt 1 — Scan auf verbotene Muster

Folgende Muster systematisch suchen:

- `dürfte`, `wird`, `sollte`, `kann davon ausgegangen werden`
- `zu Recht`, `zu Unrecht`, `offensichtlich`, `eindeutig`
- `überzeugt`, `überzeugend`, `substanzlos`, `unhaltbar`
- `Erfolgsaussichten`, `Erfolg haben`, `scheitern`

### Schritt 2 — Parteibalance prüfen

Jeder Abschnitt des Parteivortrag und der Rechtsargumente muss beide Seiten gleichgewichtig darstellen.

### Schritt 3 — Korrekturen vorschlagen

Für jede beanstandete Formulierung wird eine neutrale Ersatzformulierung vorgeschlagen.

## Ergebnis-Format

```markdown
## Neutralitätsprüfung — Ergebnis

### Beanstandungen

| Stelle | Ursprüngliche Formulierung | Ersatzformulierung |
|---|---|---|
| Zusammenfassung Satz 3 | Anspruch dürfte begründet sein | Klägerin macht den Anspruch geltend |
| Rechtsargument Zeile 4 | offensichtlich verjährt | nach Vortrag der Beklagten verjährt |

### Ergebnis

[BESTANDEN / ÜBERARBEITUNG ERFORDERLICH]

Anzahl Beanstandungen: [Zahl]
```

## Qualitätscheck — Checkliste

- [ ] Keine Erfolgsprognose enthalten?
- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteivortrag beider Seiten gleichgewichtig dargestellt?
- [ ] Fristen neutral als Tatsache, nicht als Gefahr formuliert?
- [ ] Keine implizit parteiische Darstellung?

## Hinweis

Die Neutralitätsprüfung ist kein Korrektorat des Aktenauszugs. Sie prüft ausschließlich auf Wertungen und Prognosen. Sachliche Fehler sind durch Abgleich mit der Akte zu beheben.
