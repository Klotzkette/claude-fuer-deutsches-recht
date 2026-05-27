---
name: zvg-raeumung-kuendigung
description: "Raeumung Kuendigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kuendigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB fristlose Kuendigung § 573 BGB ordentliche Kuendigung § 721 ZPO Raeumungsfrist. Pruefraster Schuldnerwohnrechte Mieterrechte Kuendigungsgruende Zutrittsrechte gerichtlicher Klageweg Raeumungsantrag. Output Kuendigungsschreiben und Raeumungsklage-Baustein mit Disclaimer. Abgrenzung zu zvg-mieteinzug-rueckstaende und zvg-glaeubiger-schuldner-kommunikation."
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

- BGH, Beschl. v. 12.01.2012 - IX ZB 258/10, NZI 2012, 250 Rn. 14 — Der Zwangsverwalter ist im Rahmen seiner Verwaltungsbefugnis berechtigt, bei erheblichem Zahlungsverzug des Mieters die außerordentliche Kündigung nach § 543 Abs. 2 Nr. 3 BGB auszusprechen; er muss die Verhältnismäßigkeit wahren und das Gericht informieren.
- BGH, Beschl. v. 04.10.2007 - IX ZB 220/06, NZI 2007, 726 Rn. 19 — Bei der Räumung des Schuldners aus dem Objekt ist § 149 ZVG zu beachten; der Schuldner genießt besonderen Schutz, wenn er die Wohnung als Eigenheimbesitzer selbst nutzt; das Gericht entscheidet über die Zulässigkeit der Räumung.

## Paragrafenkette Räumung/Kündigung ZVG

§ 543 BGB (außerordentliche Kündigung Zahlungsverzug) → § 546 BGB (Räumungsanspruch) → § 149 ZVG (Schutz Schuldnerwohnraum) → §§ 5-6 ZwVwV (Besitzkonflikte) → §§ 885-886 ZPO (Räumungsvollstreckung) → § 940a ZPO (Räumungsverfügung einstweiliger Rechtsschutz)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 149 Rn. 5-25 (Schuldnerwohnraum Schutz)
- Böttcher ZVG 6. Aufl., § 149 Rn. 10-30 (Räumungsrecht Zwangsverwaltung)
- Schmidt-Futterer Mietrecht 15. Aufl., § 543 BGB Rn. 80-120 (fristlose Kündigung Verwaltung)

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
