---
name: zvg-insolvenz-schnittstelle
description: "Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klaeren. Normen § 165 InsO Absonderungsrecht § 49 InsO Grundpfandglaeubiger § 155 ZVG Einnahmen. Pruefraster Insolvenzeroeffnung Absonderung Verwalterkommunikation Forderungsanmeldung Verteilungsauswirkungen. Output Koordinationsprotokoll mit Absonderungsnachweis Forderungsanmeldungsunterlagen und Abstimmungsprotokoll Insolvenzverwalter. Abgrenzung zu zvg-verteilungsplan-155 und zvg-rechnungslegung."
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

- BGH, Beschl. v. 05.03.2015 - IX ZB 79/13, NZI 2015, 455 Rn. 18 — Bei Eröffnung des Insolvenzverfahrens über das Vermögen des Schuldners während laufender Zwangsverwaltung geht die Verwaltungs- und Verfügungsbefugnis auf den Insolvenzverwalter über; die Zwangsverwaltung bleibt aber bestehen und wird nicht automatisch aufgehoben.
- BGH, Beschl. v. 22.03.2007 - IX ZB 143/05, NZI 2007, 406 — Das Verhältnis von Insolvenzverwalter und Zwangsverwalter ist kollusionsfrei zu koordinieren; beide haben Auskunftspflichten gegenüber dem anderen.

## Paragrafenkette Insolvenzschnittstelle

§ 152 ZVG i.V.m. §§ 80-82 InsO (Insolvenzbeschlag) → § 30 InsO (Anordnung Insolvenzeröffnung) → § 49 InsO (Absonderungsrecht Grundpfandrecht) → § 165 InsO (Zwangsversteigerung durch Insolvenzverwalter) → § 21 Abs. 2 Nr. 5 InsO (vorläufige Sicherungsmaßnahmen)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 40-70 (Insolvenz und Zwangsverwaltung)
- Uhlenbruck InsO 15. Aufl., § 49 Rn. 20-50 (Absonderungsberechtigte im Insolvenzverfahren)
- Böttcher ZVG 6. Aufl., Vor § 146 Rn. 25-45 (Verhältnis zu Insolvenzverfahren)

## Triage Insolvenzschnittstelle

1. Ist Insolvenzantrag gestellt oder Insolvenzverfahren eröffnet?
2. Ist ein vorläufiger Insolvenzverwalter bestellt? (Abstimmung der Zuständigkeiten)
3. Welche Gläubiger haben Absonderungsrechte nach § 49 InsO?
4. Soll die Zwangsverwaltung fortgeführt oder aufgehoben werden?
