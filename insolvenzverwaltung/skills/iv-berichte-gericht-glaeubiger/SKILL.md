---
name: iv-berichte-gericht-glaeubiger
description: "Zwischenberichte Sachstandsberichte und Beschlussvorlagen für Insolvenzgericht Gläubiger­ausschuss und Gläubiger­versammlung erstellen. §§ 58 66 79 InsO Berichtspflichten. Prüfraster: Stichtag Massestand Tabelle Verwertung Prozesse Personal Steuern Risiken. Output: strukturierter Bericht Entscheidungsvorlage Ampelbericht. Abgrenzung: nicht für Schlussbericht und Schlussrechnung (iv-verteilung-schlussrechnung)."
---

# Berichte an Gericht und Gläubigerorgane

## Aufgabe

Erzeugt klare, prüfbare Berichte für Insolvenzgericht, Gläubigerausschuss und Gläubigerversammlung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zwischenbericht, Sachstandsbericht oder Ausschussbericht fällig ist
- wichtige Verwertungs- oder Fortführungsentscheidungen anstehen
- Gläubigerkommunikation konsistent werden muss

## Eingaben

- Verfahrensstatus, Masse, Tabelle, Verwertung
- Prozess- und Anfechtungsstand, Fortführung, Kosten
- gerichtliche Verfügung oder Ausschussagenda

## Workflow

1. **Berichtsstand** - Stichtag, Zeitraum und Adressat festlegen.
2. **Faktenblock** - Masse, Tabelle, Verwertung, Prozesse, Personal, Steuern und Risiken aktualisieren.
3. **Entscheidungen** - Beschlussbedarf, Optionen und Empfehlung formulieren.
4. **Belege** - Anlagen, Tabellen und Nachweise referenzieren.

## Ausgabe

- Zwischenbericht
- Ausschussbericht
- Beschlussvorlage mit Anlagenliste

## Qualitätsgates

- keine Bewertung ohne Zahlenstand
- Adressatengerechte Tiefe
- offene Punkte klar markiert

## Rote Schwellen

- Masseunzulänglichkeit verschwiegen
- Quote ohne Basis
- Interessenkonflikt bei Verwertung

## Interne Vorlagen

- assets/templates/zwischenbericht.md
- assets/templates/glaeubigerausschuss-bericht.md

## Amtliche Erstquellen

- InsO Berichtspflichten nach Verfahrenslage
- § 156 InsO als Berichtstermin-Schnittstelle

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