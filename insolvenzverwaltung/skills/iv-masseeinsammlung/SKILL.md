---
name: iv-masseeinsammlung
description: "Massepositionen erfassen und realisieren: Bankguthaben Debitoren Herausgabeansprüche Versicherungen Rückstaende. §§ 80 148 InsO Verwaltungsbefugnis und Massezugehoerigkeit. Prüfraster: Massekarte Priorisierung realisierbare Forderungen Sicherungsrechte Drittschuldneranschreiben. Output: Massekarte Drittschuldnerschreiben Herausgabeanforderungen. Abgrenzung: nicht für aktive Massemehrung durch Verkauf oder Klage (iv-massemehrung-asset-realisation)."
---

# Masseeinsammlung

## Aufgabe

Erfasst und realisiert Massepositionen: Geld, Forderungen, Herausgabeansprüche, Versicherungen, Debitoren, Rückstände und streitige Ansprüche.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Massebestand unvollständig ist
- Banken, Kunden, Versicherer oder Drittschuldner angeschrieben werden müssen
- kurzfristig Liquidität für Kosten und Fortführung gebraucht wird

## Eingaben

- Banklisten, OPOS, Debitoren, Verträge
- Anlagenverzeichnis, Versicherungen, Prozesslisten
- Korrespondenz mit Drittschuldnern

## Workflow

1. **Massekarte** - Alle potenziellen Massepositionen mit Beleg, Schuldner, Fälligkeit und Durchsetzbarkeit anlegen.
2. **Priorisieren** - schnell realisierbare Forderungen vor streitigen Ansprüchen; Sicherheiten trennen.
3. **Anschreiben** - Drittschuldner-, Bank-, Kunden- und Herausgabeschreiben vorbereiten.
4. **Nachhalten** - Zahlungseingänge matchen, Mahnstufen und Klageoptionen steuern.

## Ausgabe

- Masseeinsammlungsregister
- Drittschuldneranschreiben
- Einziehungs- und Mahnplan

## Qualitätsgates

- Absonderungsrechte geprüft
- Fälligkeit und Anspruchsgrund dokumentiert
- Eingänge mit Forderungen gematcht

## Rote Schwellen

- Zahlung an Schuldner statt Massekonto
- ungeklärte Sicherungsabtretung
- Verjährung oder Ausschlussfrist

## Interne Vorlagen

- assets/templates/masseverzeichnis.md
- assets/templates/massenachverfolgung.csv

## Amtliche Erstquellen

- §§ 80 ff. InsO
- §§ 166 ff. InsO

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