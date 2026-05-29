---
name: expansion-auftakt
description: 'Startet die Planung einer Neueinstellung in einem weiteren Bundesland oder einem neuen Zielland — erhebt die relevanten Eckdaten, rahmt die Entscheidung AÜG-Modell / EOR / eigene Gesellschaft, entwirft abteilungsübergreifende Fragen und legt einen persistenten Tracker an. Lädt, wenn jemand sagt "wir stellen in [Land/Region] ein", "Expansion nach [Land]" oder "erste Einstellung in [Land]".'

---

# Expansions-Kickoff (Arbeitsrecht)

## Zweck

Diese Skill startet ein strukturiertes Expansionsprojekt für eine neue
Einstellungsregion oder ein neues Land. Sie erhebt alle relevanten Ausgangsdaten,
erarbeitet die Entscheidungsgrundlage zwischen AÜG-Lösung/EOR und eigener
rechtlicher Einheit, formuliert die richtigen Fragen für Steuerberatung, Finanzen,
HR und externe Arbeitsrechtler und legt eine persistente Trackerdate an.

Die Skill setzt voraus, dass die Expansionsentscheidung grundsätzlich gefallen ist.
Sie ist kein Entscheidungsrahmen für "sollen wir überhaupt expandieren?".

Lädt, wenn eine Einstellung in einer neuen Jurisdiktion begonnen wird — typische
Auslöser: "erste Einstellung in Spanien", "Expansion nach Polen",
"brauchen wir eine GmbH in den Niederlanden?".

## Eingaben

- Zielland oder Zielbundesland
- Geplante Rollen / Stellenprofile
- Geplante Headcount-Zahl (12-Monats-Horizont)
- Wunschtermin für die erste Einstellung
- Bestehendes rechtliches Vehikel im Zielland (ja/nein)
- Strategische Stoßrichtung (Markteinstieg / langfristiger Aufbau)
- Entscheidungsträger auf Unternehmensseite (CFO, GF, HR-Leitung)

## Rechtlicher Rahmen

**Kernvorschriften:**

- §§ 611a, 613 BGB: Arbeitnehmereigenschaft, Unübertragbarkeit der Arbeitsleistung
- § 7 SGB IV: Beschäftigungsverhältnis, Scheinselbständigkeit
- §§ 1–19 AÜG: Arbeitnehmerüberlassungsgesetz — Erlaubnispflicht, Höchstüberlassungsdauer (§ 1 Abs. 1b AÜG: 18 Monate), Equal-Pay-Gebot (§ 8 AÜG)
- §§ 17, 18 KSchG: Massenentlassungsanzeige (relevant ab bestimmtem Schwellenwert)
- Art. 8 Rom I-VO: Arbeitsvertragsstatut bei grenzüberschreitenden Verhältnissen
- RL 2008/104/EG: Leiharbeits-Richtlinie

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Erfurter Kommentar/Wank, 24. Aufl. 2024, § 611a BGB Rn. 1 ff.: Arbeitnehmerbegriff, Weisungsgebundenheit als zentrales Merkmal
- Schüren/Hamann, AÜG, 5. Aufl. 2022, § 1 Rn. 50 ff.: Erlaubnispflicht und Folgen unerlaubter Arbeitnehmerüberlassung
- Thüsing, Leiharbeitsrecht, 4. Aufl. 2023, § 8 AÜG Rn. 12 ff.: Equal-Pay-Grundsatz und Ausnahmen durch TV
- Rieble/Junker (Hrsg.), Münchener Handbuch zum Arbeitsrecht, Bd. 1, 5. Aufl. 2021, § 19 Rn. 5 ff.: Grenzüberschreitende Arbeitsverhältnisse

## Ablauf

**Schritt 1 — Kontextladen**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Eskalationstabelle, bestehende Expansionsnotizen.

**Schritt 2 — Prüfung bestehender Tracker**

Existiert bereits eine Tracker-Datei `expansion-[slug].yaml` für dieses Land?
Falls ja: "Für [Land] existiert bereits ein Expansions-Tracker. Nutzen Sie
`/arbeitsrecht:expansion-aktualisierung [Land]` für eine Aktualisierung oder bestätigen
Sie den Neustart."

**Schritt 3 — Strukturierte Informationserhebung**

Frage alle nachfolgenden Punkte in einem einzigen Block ab:

> Zur Erstellung des Expansionsplans werden folgende Angaben benötigt:
>
> **Die Expansion**
> - Welches Land / welches Bundesland?
> - Welche Rollen? (Stellenprofil ist entscheidend — ein Vertriebsmitarbeiter
>   mit Abschlussvollmacht erzeugt anderes Risiko als eine Entwicklerstelle)
> - Wie viele Einstellungen im 12-Monats-Horizont?
> - Wann soll die erste Person starten?
>
> **Ausgangssituation**
> - Besteht bereits eine rechtliche Einheit im Zielland?
> - Wird ein EOR-Anbieter erwogen oder bereits genutzt?
> - Sind Steuerberatung und Finance bereits eingebunden?
> - Gibt es externe Arbeitsrechtler im Zielland?
>
> **Strategischer Kontext**
> - Langfristiger Aufbau oder Markttest (eine bis zwei Einstellungen)?
> - Wer ist der Entscheidungsträger für die Strukturentscheidung (GF, CFO)?

**Schritt 4 — Übergabe an `internationale-expansion`**

Lade die Referenz-Skill `internationale-expansion` und führe den vollständigen
Ablauf aus (Schritte 2–5).

**Schritt 5 — Tracker anlegen**

Lege `expansion-[slug].yaml` an und bestätige die Erstellung.

## Ausgabeformat

```
Expansions-Kickoff: [Land] — [Datum]

Erste Einstellung angestrebt: [Datum]
Headcount (12 Monate): [N]
Rollen: [Liste]
Tracker: expansion-[slug].yaml

EOR vs. Gesellschaft: [Einschätzung mit Fragen für Steuer/Finance]
Scheinselbständigkeitsrisiko: [Flag wenn zutreffend]

Offene Punkte ([N] gesamt):
| # | Punkt | Verantwortung | Status |
|---|---|---|---|
| 1 | ... | ... | Offen |
```

## Beispiel

```
/arbeitsrecht:expansion-auftakt Polen
```

```
/arbeitsrecht:expansion-auftakt
(Skill fragt nach dem Zielland)
```

Ausgabe bei Einstellung von zwei Vertriebsmitarbeitern in Polen:

> PE-Risiko: Vertriebsrollen mit Abschlussbefugnis können auch ohne
> polnische GmbH eine steuerliche Betriebsstätte begründen. Frage an
> Steuerberatung vor der ersten Einstellung klären.

## Risiken und typische Fehler

- **Scheinselbständigkeit § 7 SGB IV**: Freie Mitarbeiter im Ausland, die
  faktisch weisungsgebunden und eingegliedert sind, gelten als Arbeitnehmer.
  Nachzahlungsrisiko Sozialversicherung bis zu vier Jahre rückwirkend.
- **AÜG-Falle bei EOR**: Wird ein EOR ohne AÜG-Erlaubnis genutzt und liegt
  echte Arbeitnehmerüberlassung vor, kann kraft Gesetzes ein Arbeitsverhältnis
  zum Entleiher entstehen (§ 10 Abs. 1 AÜG).
- **18-Monats-Grenze**: Die gesetzliche Höchstüberlassungsdauer beträgt
  18 Monate (§ 1 Abs. 1b AÜG). Überschreitung ohne tarifvertragliche Ausnahme
  ist bußgeldbewehrt.
- **Fehlende Vorabklärung Betriebsstättenrisiko**: Vertriebsmitarbeiter mit
  Vertretungsmacht können in vielen Ländern steuerlich eine Betriebsstätte
  begründen — Steuerberatung vor Einstellungsbeginn zwingend.
- **Arbeitsvertrag nach dem Recht des Stammlandes**: Art. 8 Rom I-VO schützt
  Arbeitnehmer vor Abwahl zwingender Schutzvorschriften des
  Beschäftigungsstaats. Reine Rechtswahl zugunsten deutschen Rechts schützt
  nicht vor Mindeststandards des Einsatzlandes.

## Quellenpflicht

Jede Ausgabe dieser Skill muss bei Structural-Empfehlungen zitieren:

- § 7 SGB IV (Scheinselbständigkeit), §§ 1, 8, 10 AÜG
- Art. 8 Rom I-VO bei grenzüberschreitenden Konstellationen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Schüren/Hamann, AÜG, 5. Aufl. 2022, wenn AÜG-Erlaubnis relevant ist

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
