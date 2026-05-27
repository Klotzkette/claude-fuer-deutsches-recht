---
name: zvg-miet-und-pachtverwaltung
description: "Miet- und Pachtverwaltung in der Zwangsverwaltung einschliesslich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhaeltnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§ 535 ff. BGB Mietrecht § 150 ZVG Vorausverfuegungen des Schuldners. Pruefraster Mietvertraege Pachtvertraege Zahlstellen Vorausverfuegungen Kautionen Nebenkosten Nutzungsregelungen. Output Mieterliste mit Vertragsuebersicht Kautionsnachweis und Zahlungsplan fuer Verteilungsrechnung. Abgrenzung zu zvg-mieteinzug-rueckstaende und zvg-raeumung-kuendigung."
---

# Miet- und Pachtverwaltung

## Aufgabe

Ordnet Miet- und Pachtverhältnisse im beschlagnahmten Objekt mit Kommunikation, Zahlstellen, Kautionen und Vertragsrisiken.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieter oder Pächter vorhanden sind
- Mietzahlungen umzuleiten sind
- Verträge, Kautionen oder Vorausverfügungen unklar sind

## Eingaben

- Miet- und Pachtverträge
- Mieterliste, Zahlungsverlauf, Kautionen
- Schreiben des Schuldners oder der Mieter

## Workflow

1. **Verträge erfassen** - Einheit, Nutzer, Miete, Nebenkosten, Laufzeit, Kaution und Sonderrechte aufnehmen.
2. **Mitteilung** - Mieter/Pächter über Zwangsverwaltung und neue Zahlstelle informieren.
3. **Vorausverfügungen** - Abtretung, Vorauszahlung, Kaution und Rückstände prüfen.
4. **Laufend verwalten** - Anpassungen, Nebenkosten, Mängel, Kündigungen und Kommunikation steuern.

## Ausgabe

- Rent Roll
- Mieterschreiben
- Vertragsrisikomatrix

## Qualitätsgates

- Soll- und Istmiete getrennt
- Kautionen nicht als freie Masse behandelt
- Vorausverfügungen geprüft

## Rote Schwellen

- Zahlung an Schuldner
- fehlender Mietvertrag
- streitiger Besitz

## Interne Vorlagen

- assets/templates/mieterliste-rent-roll.md
- assets/templates/schuldner-glaeubiger-kommunikation.md

## Amtliche Erstquellen

- §§ 4, 5, 6 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 10.10.2013 - IX ZB 229/11, NZI 2014, 44 Rn. 12 — Der Zwangsverwalter tritt mit Besitzerlangung in alle laufenden Mietverhältnisse ein und hat die mietvertraglichen Pflichten zu erfüllen; Mängel der Mietsache muss er wie ein Vermieter beseitigen, soweit die Masse dies erlaubt.
- BGH, Beschl. v. 17.07.2003 - IX ZB 525/02, NJW 2003, 3347 Rn. 10 — Mietverträge die der Schuldner nach Beschlagnahme abschließt sind dem Gläubiger gegenüber unwirksam; bereits bestehende Verträge bleiben dagegen bestehen und binden den Zwangsverwalter.

## Paragrafenkette Miet-/Pachtverwaltung ZVG

§ 152 ZVG (Rechte/Pflichten Verwalter) → § 153 ZVG (Einziehung Nutzungen) → § 57 ZVG (Schutz der Mieter) → §§ 535 566 BGB (Mietrecht) → §§ 8-9 ZwVwV (laufende Verwaltung) → § 581 BGB (Pachtvertrag) → §§ 596-599 BGB (Pächterschutz)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 57 Rn. 10-30 (Mieterschutz in Zwangsverwaltung)
- Böttcher ZVG 6. Aufl., § 152 Rn. 45-70 (Mietverhältnisse in Zwangsverwaltung)
- Schmidt-Futterer Mietrecht 15. Aufl., § 566 BGB Rn. 90-115 (Zwangsverwaltung Eigentümerwechsel)

## Triage Miet-/Pachtverwaltung

1. Liegen schriftliche Mietverträge vor? (Alle Einheiten vollständig erfasst)
2. Sind Kautionen hinterlegt? (Pflicht: auf separatem Kautionskonto)
3. Bestehen Sondermietrechte (Wohnrecht Nießbrauch)? (Im Grundbuch Abt. II prüfen)
4. Sind Pachtverhältnisse vorhanden? (Sonderregeln §§ 581 ff. BGB)

## Output-Template Verwaltungsübernahme-Schreiben Miet-/Pachtverhältnis

```
[ZWANGSVERWALTER]

An [MIETER/PÄCHTER]
[ADRESSE]

Mitteilung: Übernahme der Verwaltung

Sehr geehrte/r Herr/Frau [NAME],

ich habe die Zwangsverwaltung über das Grundstück [ADRESSE] übernommen.
Ich trete damit in Ihre/Ihre bestehenden Miet-/Pachtverhältnisse ein
und führe die Verwaltung ab [DATUM] fort.

Die Miete/Pacht ist ab sofort an folgendes Konto zu zahlen:
[IBAN, BIC, BANK, VERWENDUNGSZWECK]

Ihre vertraglichen Rechte bleiben unberührt. Mängelanzeigen richten Sie bitte an:
[KONTAKTDATEN ZWANGSVERWALTER]

[UNTERSCHRIFT]
```
