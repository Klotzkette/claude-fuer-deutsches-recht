---
name: zvg-insolvenz-schnittstelle
description: "Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klaeren. Normen § 165 InsO Absonderungsrecht § 49 InsO Grundpfandgläubiger § 155 ZVG Einnahmen. Prüfraster Insolvenzeroeffnung Absonderung Verwalterkommunikation Forderungsanmeldung Verteilungsauswirkungen. Output Koordinationsprotokoll mit Absonderungsnachweis Forderungsanmeldungsunterlagen und Abstimmungsprotokoll Insolvenzverwalter. Abgrenzung zu zvg-verteilungsplan-155 und zvg-rechnungslegung."
---

# Schnittstelle zur Insolvenz

## Aufgabe

Ordnet Fälle, in denen Zwangsverwaltung und Insolvenzverfahren zusammentreffen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- über das Vermögen des Schuldners Insolvenz beantragt oder eröffnet wird
- Insolvenzverwalter, Sachwalter oder Gläubiger Rechte anmelden
- § 165 InsO oder Absonderungsrechte relevant werden

## Eingaben

- Insolvenzeröffnungsbeschluss, IV-Kontakt
- ZVG-Beschluss, Forderungen, Grundbuch
- Mieten, Ausgaben und Verteilungsstand

## Workflow

1. **Verfahren koordinieren** - ZVG-Akte und Insolvenzakte mit Rollen, Daten und Sperren abgleichen.
2. **Rechte prüfen** - Absonderung, § 165 InsO, Forderungen und Massebezug markieren.
3. **Kommunikation** - Insolvenzverwalter, Gericht und betreibende Gläubiger abstimmen.
4. **Verteilung** - Rang und Auskehr unter Insolvenzschnittstelle prüfen.

## Ausgabe

- Schnittstellenvermerk
- Kommunikationsentwurf
- Verteilungsrisiko-Ampel

## Qualitätsgates

- Insolvenzverwalterrolle nicht mit Zwangsverwalterrolle vermischt
- Beschlüsse beider Gerichte geprüft
- Rang offen markiert

## Rote Schwellen

- doppelte Verwertung
- widersprechende Gerichtsanordnungen
- Zahlung an falsche Masse

## Interne Vorlagen

- assets/templates/insolvenz-schnittstelle.md
- assets/templates/verteilungsplan-155.md

## Amtliche Erstquellen

- § 165 InsO
- ZVG Gesamtfassung

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzschnittstelle

§ 152 ZVG i.V.m. §§ 80-82 InsO (Insolvenzbeschlag) → § 30 InsO (Anordnung Insolvenzeröffnung) → § 49 InsO (Absonderungsrecht Grundpfandrecht) → § 165 InsO (Zwangsversteigerung durch Insolvenzverwalter) → § 21 Abs. 2 Nr. 5 InsO (vorläufige Sicherungsmaßnahmen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Insolvenzschnittstelle

1. Ist Insolvenzantrag gestellt oder Insolvenzverfahren eröffnet?
2. Ist ein vorläufiger Insolvenzverwalter bestellt? (Abstimmung der Zuständigkeiten)
3. Welche Gläubiger haben Absonderungsrechte nach § 49 InsO?
4. Soll die Zwangsverwaltung fortgeführt oder aufgehoben werden?
