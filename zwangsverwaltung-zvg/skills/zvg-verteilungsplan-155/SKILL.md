---
name: zvg-verteilungsplan-155
description: "Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen § 154 ZVG Kosten Verwalterverguetung. Prüfraster Nutzungen Ausgaben Kosten Gläubigerzahlungen Vorschuesse Rang Auszahlung Restbetrag. Output Verteilungsplan mit Rangfolge Betraegen Auszahlungsnachweis und Gerichtsbericht. Abgrenzung zu zvg-rechnungslegung (Gesamtabrechnung) und zvg-konten-kassenführung."
---

# Verteilungsplan § 155 ZVG

## Aufgabe

Bereitet die Verteilung der Nutzungen und Erlöse unter Berücksichtigung von Ausgaben, Kosten und Rang vor.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- auskehrbare Überschüsse vorhanden sind
- Gläubiger Zahlung verlangen
- Schlussrechnung oder laufende Auszahlungen anstehen

## Eingaben

- Kontostand, Einnahmen, Ausgaben, Kosten
- Gläubigerforderungen, Rang, Gerichtskosten
- Rücklagen und absehbare Objektkosten

## Workflow

1. **Verteilungsmasse** - verfügbare Nutzungen nach Abzug laufender Ausgaben und Rücklagen bestimmen.
2. **Rang prüfen** - Gläubiger, Gerichtskosten, Verwaltervergütung und öffentliche Lasten einordnen.
3. **Plan erstellen** - Auszahlungsbeträge, Rückbehalte und Begründung darstellen.
4. **Freigabe** - Gericht oder Beteiligte informieren und Zahlung dokumentieren.

## Ausgabe

- Verteilungsplan
- Auszahlungsliste
- Berichtsbaustein

## Qualitätsgates

- keine Verteilung ohne Rücklagencheck
- Rang und Kosten geprüft
- Zahlungen belegt

## Rote Schwellen

- Auskehr trotz offener Notkosten
- falscher Gläubiger
- ungeklärte öffentliche Last

## Interne Vorlagen

- assets/templates/verteilungsplan-155.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- § 155 ZVG
- §§ 11, 12 ZwVwV

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Verteilungsplan

§ 155 ZVG (Verteilungsplan) → § 10 ZVG (Rangklassen) → § 11 ZwVwV (Vorschüsse) → § 12 ZwVwV (Auszahlungen) → § 154 ZVG (Gerichtsgenehmigung bei Zweifeln) → § 20 ZwVwV (Vergütung als Ausgabe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Verteilungsplan

1. Wie hoch ist der ausschüttungsfähige Betrag nach Abzug laufender Ausgaben und Rücklage?
2. Welche Gläubiger sind zu befriedigen und in welchem Rang?
3. Hat das Vollstreckungsgericht Auszahlungen bereits genehmigt?
4. Sind Gerichtskosten und Verwaltervergütung einbezogen?

## Output-Template Verteilungsplan (Schema)

```
VERTEILUNGSPLAN nach § 155 ZVG
Objekt: [ADRESSE]
AZ: [X]
Verteilungsmasse per [DATUM]: [BETRAG] EUR

ABZÜGE VOR VERTEILUNG
Laufende Ausgaben (Rücklage 3 Monate): [BETRAG]
Gerichtskosten: [BETRAG]
Verwaltervergütung (brutto): [BETRAG]
Sonstige dringende Ausgaben: [BETRAG]
VERBLEIBENDE VERTEILUNGSMASSE: [BETRAG]

RANGFOLGE (§ 10 ZVG)
Nr. 1 Kosten des Verfahrens: [BETRAG]
Nr. 2 Öff. Lasten lfd. Jahr: [BETRAG]
Nr. 3 Öff. Lasten Rückstände: [BETRAG]
Nr. 4 Grund-/Rentenschuld: [BETRAG an GLÄUBIGER X]
Nr. 5 Weitere Hypotheken: [ggf.]

AUSZAHLUNGSLISTE
Empfänger | Betrag | Bankverbindung | Datum
[...]     | [...]  | [...]          | [...]

[ORT, DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```
