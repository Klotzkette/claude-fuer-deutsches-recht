---
name: neutralitaetspruefung
description: "Prüft einen erstellten Aktenauszug auf unzulässige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs. Massstab § 286 ZPO freie Beweiswürdigung im Aktenauszug Gerichtsverfahren."
---

# Neutralitätsprüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage — kläre vor der Prüfung

1. Für wen ist der Aktenauszug bestimmt? (internes Arbeitsdokument / Übergabe an Mandant / Gericht)
2. Hat der Ersteller den Auftrag, die eigene Mandantsseite besonders darzustellen? (dann kein Aktenauszug, sondern Schriftsatz!)
3. Gibt es Stellen, die bewusst als subjektive Einschätzung des Anwalts markiert sind? (Diese sind zu entfernen oder zu kennzeichnen.)

## Normhintergrund

- § 286 Abs. 1 ZPO — Freie Beweiswürdigung des Gerichts; Aktenauszug darf keine Beweiswürdigungsprognosen enthalten
- § 138 ZPO — Wahrheitspflicht; auch interne Vermerke müssen den Sachverhalt korrekt abbilden
- § 43a Abs. 3 BRAO — Sachlichkeitsgebot; gilt auch für interne Aktendokumentation

## Rechtsprechung zum Sachlichkeitsgebot und Neutralität

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Verbotene Formulierungstypen

### Erfolgsprognosen (absolut verboten)

| Verboten | Erlaubt |
|---|---|
| "Die Klage wird Erfolg haben" | "Die Klage ist anhängig" |
| "Der Anspruch dürfte begründet sein" | "Die Klägerin macht [Anspruch] geltend" |
| "Die Verjährungseinrede greift durch" | "Die Beklagte erhebt die Verjährungseinrede" |
| "Das Gericht wird … erkennen" | "Das Gericht hat … nicht geäußert" |
| "offensichtlich unbegründet" | "nach Vortrag der Beklagten unbegründet" |

### Wertende Adjektive (zu vermeiden)

- substanzlos, unhaltbar, abwegig, überzeugend, zutreffend, unzutreffend
- zu Recht, zu Unrecht
- offensichtlich, eindeutig (ohne Quellenangabe)

### Parteiische Darstellung

- Ausführliche Wiedergabe des Vortrags einer Seite ohne entsprechende Gegenüberstellung der anderen Seite
- Formulierungen, die implizit eine Seite stärken ("Trotz des klaren Wortlauts des Vertrags …")

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

---

