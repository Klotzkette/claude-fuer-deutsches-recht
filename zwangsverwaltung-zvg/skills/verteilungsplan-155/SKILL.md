---
name: verteilungsplan-155
description: "Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen § 154 ZVG Kosten Verwalterverguetung. Prüfraster Nutzungen Ausgaben Kosten Gläubigerzahlungen Vorschuesse Rang Auszahlung Restbetrag. Output Verteilungsplan mit Rangfolge Betraegen Auszahlungsnachweis und Gerichtsbericht. Abgrenzung zu zvg-rechnungslegung (Gesamtabrechnung) und zvg-konten-kassenführung im Zwangsverwaltung Zvg."
---

# Verteilungsplan § 155 ZVG

## Arbeitsbereich

Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und muessen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung § 10 ZVG Rangklassen § 154 ZVG Kosten Verwalterverguetung. Prüfraster Nutzungen Ausgaben Kosten Gläubigerzahlungen Vorschuesse Rang Auszahlung Restbetrag. Output Verteilungsplan mit Rangfolge Betraegen Auszahlungsnachweis und Gerichtsbericht. Abgrenzung zu zvg-rechnungslegung (Gesamtabrechnung) und zvg-konten-kassenführung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
[...] | [...] | [...] | [...]

[ORT, DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```

