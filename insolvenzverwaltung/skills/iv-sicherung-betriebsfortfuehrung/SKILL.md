---
name: iv-sicherung-betriebsfortfuehrung
description: "Betrieb in Insolvenz fortführen wenn Massemehrung oder Sanierung geplant ist und Lohn Lieferanten und Auftraege gesichert werden muessen. §§ 22 55 InsO Massebegrundung §§ 113 120 InsO Arbeitsverhältnisse. Prüfraster: Fortführungsziel Cash-Bridge Insolvenzgeldzeitraum kritische Lieferanten operative Risiken. Output: Fortführungsplan Liquiditaetsplan Risikoliste. Abgrenzung: nicht für Personalrecht (iv-arbeitsrecht-insolvenzgeld)."
---

# Sicherung und Betriebsfortführung

## Aufgabe

Prüft und steuert, ob und wie der Geschäftsbetrieb im Eröffnungsverfahren oder eröffneten Verfahren fortgeführt werden kann.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Betrieb, Filiale, Praxis oder Werk noch aktiv ist
- Löhne, Lieferanten und Kundenaufträge offen sind
- Massemehrung durch Fortführung möglich erscheint

## Eingaben

- Auftragsbestand, Deckungsbeiträge, Liquiditätsplan
- Lohnliste, Insolvenzgeldzeitraum, Lieferantenkritikalität
- Versicherungen, Genehmigungen, Schlüsselressourcen

## Workflow

1. **Fortführungsziel** - Massemehrung, Sanierung, Verkauf oder geordnete Ausproduktion definieren.
2. **Cash-Bridge** - Einzahlungen, Auszahlungen, Insolvenzgeld, kritische Lieferanten und Steuern planen.
3. **Operative Risiken** - Versicherung, Arbeitsschutz, Umwelt, IT, Schlüsselpersonen und Genehmigungen prüfen.
4. **Entscheidungsvorlage** - Fortführung, Stilllegung oder Hybrid mit Ampel und Bedingungen ausgeben.

## Ausgabe

- Fortführungswochenplan
- Lieferanten- und Kundenampel
- Entscheidungsvorlage für Gericht oder Ausschuss

## Qualitätsgates

- kein Fortführungsbeschluss ohne Cash-Bridge
- kritische Genehmigungen geprüft
- Masseinteresse dokumentiert

## Rote Schwellen

- negative Fortführungsdeckung
- ungeklärte Versicherung
- Lohn- oder Sozialabgabenrisiko

## Interne Vorlagen

- assets/templates/betriebsfortfuehrung-wochenplan.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- §§ 21, 22, 55 InsO
- SGB III Insolvenzgeld als zu prüfende Schnittstelle

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.