---
name: iv-vorlaeufige-verwaltung
description: "Erste Massnahmen als vorlaeufliger Insolvenzverwalter nach § 21 InsO umsetzen: Bankkonten Besitz Post Drittschuldner Betrieb. § 21 InsO Sicherungsmassnahmen § 22 InsO Pflichten des vorl. Verwalters. Prüfraster: Beschlussumfang Zustimmungsvorbehalt Postsperre Bankensicherung Drittschuldneranschreiben Kommunikation. Output: Tagesplan Sicherungsprotokoll Kommunikationsschreiben. Abgrenzung: nicht für laufendes Regelverfahren (iv-regelverfahren-eroeffnung)."
---

# Vorläufige Insolvenzverwaltung

## Aufgabe

Führt die ersten Tage nach Bestellung als vorläufiger Insolvenzverwalter mit Zustimmungsvorbehalt oder starker Verwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Beschluss nach § 21 InsO vorliegt
- Banken, Kasse, Post und Drittschuldner sofort gesichert werden müssen
- der Betrieb bis zur Entscheidung fortgeführt wird

## Eingaben

- Sicherungsbeschluss
- Bank- und Kassenstände
- Debitoren, Kreditoren, Arbeitnehmer, Lieferanten

## Workflow

1. **Befugnisse lesen** - Beschlussumfang, Zustimmungsvorbehalt, Postsperre und Verfügungsverbote auswerten.
2. **Masse sichern** - Banken, Kasse, Forderungen, Warenlager und Schlüssel kontrollieren.
3. **Kommunikation** - Schuldner, Banken, Drittschuldner, Arbeitnehmer und Gericht informieren.
4. **Tagessteuerung** - Zahlungen nur nach Freigabe, Beleg und Masseinteresse dokumentieren.

## Ausgabe

- Sofortmaßnahmenliste
- Bank- und Kassenprotokoll
- Zahlungsfreigabeprotokoll

## Qualitätsgates

- Beschlussbefugnisse werden wörtlich beachtet
- jede Zahlung hat Zweck, Beleg und Freigabe
- Drittschuldner sind informiert

## Rote Schwellen

- Zahlungen außerhalb des Freigabeprozesses
- fehlender Kassensturz
- unklare Eigentums- oder Sicherungsrechte

## Interne Vorlagen

- assets/templates/vorlaeufige-verwaltung-checkliste.md
- assets/templates/zahlungslauf-freigabe.md

## Amtliche Erstquellen

- § 21 InsO
- § 22 InsO

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