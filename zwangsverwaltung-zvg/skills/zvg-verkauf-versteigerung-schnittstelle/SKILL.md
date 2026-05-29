---
name: zvg-verkauf-versteigerung-schnittstelle
description: "Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG Aufhebung der Verwaltung §§ 85 ff. ZVG Versteigerungsverfahren. Prüfraster Objektinformationen Besichtigungen Werterhalt Mieterlage Bieterfragen Übergabeprotokoll Aufhebung. Output Übergabebericht für Versteigerungsverfahren mit Objektzustand Mietlage und Schnittstellen-Dokumentation. Abgrenzung zu zvg-rechnungslegung (Abschluss) und zvg-bieterangebot-bewertung."
---

# Schnittstelle zu Verkauf und Zwangsversteigerung

## Aufgabe

Unterstützt die Zwangsverwaltung, wenn parallel Versteigerung, freihändiger Verkauf oder Objektverwertung vorbereitet wird.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zwangsversteigerung parallel läuft
- Bieter oder Sachverständige Objektinformationen anfragen
- Verwaltung auf Zuschlag oder Aufhebung zuläuft

## Eingaben

- Versteigerungsakte, Wertgutachten, Besichtigungstermine
- Mieterliste, Objektzustand, laufende Kosten
- Gerichtliche Terminsdaten

## Workflow

1. **Informationspaket** - Objektzustand, Mieterlage, Versicherungen, Lasten und Rückstände zusammenstellen.
2. **Besichtigung** - Zutritt, Mieterkommunikation, Datenschutz und Protokoll steuern.
3. **Werterhalt** - notwendige Maßnahmen bis Zuschlag oder Aufhebung priorisieren.
4. **Übergang** - Aufhebung, Schlussrechnung, Endabrechnung und Übergabe planen.

## Ausgabe

- Objektinfopaket
- Besichtigungsplan
- Übergabe- und Aufhebungscheck

## Qualitätsgates

- Mieterrechte beachtet
- Daten nicht unnötig offengelegt
- Schlussrechnung vorbereitet

## Rote Schwellen

- Bieterzugang ohne Abstimmung
- Objektwertgefährdung
- Aufhebung ohne Endabrechnungspfad

## Interne Vorlagen

- assets/templates/besitzuebernahme-protokoll.md
- assets/templates/schlussrechnung-aufhebung.md

## Amtliche Erstquellen

- ZVG Gesamtfassung
- § 12 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Versteigerungsschnittstelle

§ 180 ZVG (Anordnung Zwangsversteigerung parallel) → § 55 ZVG (Zuschlag Wirkungen) → § 56 ZVG (Übergabepflicht) → § 57 ZVG (Mieterschutz Ersteher) → § 57a ZVG (Sonderkündigung Ersteher) → §§ 566 BGB (Kauf bricht nicht Miete) → § 155 ZVG (Schlussrechnung bei Zuschlag)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Versteigerungsschnittstelle

1. Läuft parallel ein Zwangsversteigerungsverfahren?
2. Wann ist der Versteigerungstermin? (Schlussrechnung vorzubereiten)
3. Liegen alle Mietvertragsdaten für die Bieterinformation vor?
4. Sind Mietkautions-Guthaben der Mieter dokumentiert? (Übertragung auf Ersteher)

## Workflow bei Zuschlag

1. Zuschlagsdatum und Ersteher festhalten
2. Nutzungen bis Zuschlagsdatum verbuchen
3. Schlussrechnung nach § 15 ZwVwV erstellen
4. Kontostand an Vollstreckungsgericht melden
5. Mietverhältnisse und Kautionen an Ersteher übergeben
6. Abschluss-Bericht an Gericht und Gläubiger
