---
name: zvg-raeumung-kuendigung
description: "Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kündigung § 573 BGB ordentliche Kündigung § 721 ZPO Räumungsfrist. Prüfraster Schuldnerwohnrechte Mieterrechte Kündigungsgründe Zutrittsrechte gerichtlicher Klageweg Räumungsantrag. Output Kündigungsschreiben und Räumungsklage-Baustein mit Disclaimer. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-gläubiger-schuldner-kommunikation."
---

# Räumung, Kündigung und Besitzkonflikte

## Aufgabe

Prüft Konflikte um Besitz, Nutzung, Kündigung und Räumung im Rahmen der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Schuldner oder Dritte den Zutritt verweigern
- Mieter erheblich rückständig sind
- Kündigung, Räumung oder Nutzungsänderung erwogen wird

## Eingaben

- Mietvertrag, Rückstände, Objektstatus
- Schuldnerwohnräume, Beschluss, Kommunikation
- Gefahren, Fotos, Zeugen, Polizeikontakt

## Workflow

1. **Rechtsposition** - Schuldner, Mieter, Pächter, Dritter oder unbekannter Nutzer bestimmen.
2. **Maßnahme** - Zutritt, Abmahnung, Kündigung, Räumung oder gerichtliche Hilfe trennen.
3. **Verhältnismäßigkeit** - Masseinteresse, Kosten, Risiken und Alternativen prüfen.
4. **Schreiben/Antrag** - Kommunikation oder gerichtlichen Antrag vorbereiten.

## Ausgabe

- Konfliktvermerk
- Kündigungs- oder Zutrittsanschreiben
- Gerichtsbaustein

## Qualitätsgates

- Wohnraumschutz geprüft
- Kosten/Nutzen dokumentiert
- Beweise gesichert

## Rote Schwellen

- Selbsthilfe
- unberechtigter Schlosswechsel
- Schuldnerhausstand nicht beachtet

## Interne Vorlagen

- assets/templates/raeumung-kuendigung.md
- assets/templates/besitzuebernahme-protokoll.md

## Amtliche Erstquellen

- § 149 ZVG als Schuldnerwohnraum-Schnittstelle
- § 5 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Räumung/Kündigung ZVG

§ 543 BGB (außerordentliche Kündigung Zahlungsverzug) → § 546 BGB (Räumungsanspruch) → § 149 ZVG (Schutz Schuldnerwohnraum) → §§ 5-6 ZwVwV (Besitzkonflikte) → §§ 885-886 ZPO (Räumungsvollstreckung) → § 940a ZPO (Räumungsverfügung einstweiliger Rechtsschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Räumung/Kündigung

1. Wer nutzt das Objekt — Mieter oder Schuldner selbst? (§ 149 ZVG Sonderschutz für Schuldner)
2. Wie hoch ist der Rückstand? (Außerordentliche Kündigung ab 2 Monatsmieten § 543 Abs. 2 Nr. 3 BGB)
3. Liegt bereits eine Abmahnung vor? (Empfehlenswert vor Kündigung)
4. Besteht akute Gefahr für das Objekt durch den Nutzer? (Sofortmaßnahme möglich)
5. Ist gerichtliche Hilfe erforderlich? (Vollstreckungsgericht-Antrag § 154 ZVG)

## Output-Template Räumungsklage-Antrag (Auszug)

**Adressat:** Amtsgericht — Tonfall sachlich-juristisch

```
An das Amtsgericht [ORT]
Wohnungssachen / Vollstreckungsgericht
AZ Zwangsverwaltung: [X]

Räumungsklage

des Zwangsverwalters [NAME], für die Zwangsverwaltungsmasse
[ADRESSE], AZ [X]
— Kläger —
gegen
[MIETER/SCHULDNER], [ADRESSE]
— Beklagte —

Antrag:
Die Beklagte wird verurteilt, die Wohnung/das Objekt [BEZEICHNUNG] zu räumen
und geräumt an den Kläger als Zwangsverwalter herauszugeben.

Begründung:
[KÜNDIGUNG VOM DATUM, ANLAGE K1; RÜCKSTANDSNACHWEIS ANLAGE K2]
```
