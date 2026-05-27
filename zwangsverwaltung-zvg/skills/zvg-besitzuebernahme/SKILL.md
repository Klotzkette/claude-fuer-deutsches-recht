---
name: zvg-besitzuebernahme
description: "Besitzerlangung ueber das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhaeltnisse. Pruefraster Vor-Ort-Termin Objektbeschreibung Nutzungen Rechte Mobilien Forderungen Lasten Ausgaben Schluessel. Output Besitzerlangungsbericht mit Objektprotokoll Fotodokumentation Schluesselliste und Meldung ans Gericht. Abgrenzung zu zvg-aktenanlage-objektcockpit und zvg-berichtswesen-gericht."
---

# Besitzerlangung und Objektaufnahme

## Aufgabe

Führt durch den Vor-Ort-Termin zur Besitzergreifung mit Bericht nach ZwVwV.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Objekt erstmals betreten oder übernommen wird
- Schlüssel, Zustand und Mieter zu erfassen sind
- Sofortmaßnahmen wegen Gefahr oder Versicherung nötig sind

## Eingaben

- Bestallung, Objektadresse, Schlüsselinfo
- Mieter- und Pächterdaten
- Fotos, Zählerstände, Versicherungen, Dienstleister

## Workflow

1. **Termin vorbereiten** - Beteiligte informieren, Zutritt, Zeugen, Kamera und Checkliste sichern.
2. **Objekt aufnehmen** - Nutzungsart, Zustand, Drittrechte, Mobilien, Forderungen, Lasten und Ausgaben protokollieren.
3. **Gefahren sichern** - Versicherung, Wasser, Strom, Brand, Verkehrssicherung und Notdienst prüfen.
4. **Bericht einreichen** - Besitzerlangungsbericht ans Gericht und Nachermittlungen vormerken.

## Ausgabe

- Besitzübernahmeprotokoll
- Objektzustandsbericht
- Sofortmaßnahmenliste

## Qualitätsgates

- § 3 ZwVwV-Punkte vollständig abgefragt
- Fotos/Belege referenziert
- Nachermittlungen terminiert

## Rote Schwellen

- akute Gefahrenstelle
- fehlende Gebäudeversicherung
- Schuldner verweigert Zugang

## Interne Vorlagen

- assets/templates/besitzuebernahme-protokoll.md
- assets/templates/instandhaltung-gefahrensicherung.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 25.09.2008 - IX ZB 205/06, NZI 2009, 55 Rn. 19 — Der Zwangsverwalter erlangt den Besitz an dem Objekt durch die Besitzeinweisung des Gerichts; ab diesem Zeitpunkt hat er alle Nutzungen einzuziehen und Ausgaben zu bestreiten; eine Verzögerung der Besitzerlangung geht zu seinen Lasten.
- BGH, Beschl. v. 14.12.2000 - IX ZB 47/00, NJW 2001, 1503 — Verweigert der Schuldner die Übergabe, kann das Vollstreckungsgericht auf Antrag des Zwangsverwalters die gewaltsame Inbesitznahme anordnen; eigenmächtiges Vorgehen des Verwalters ist verboten.

## Paragrafenkette Besitzübernahme

§ 150 ZVG (Besitzeinweisung durch Gericht) → § 152 ZVG (Rechte und Pflichten ab Besitzerlangung) → § 3 ZwVwV (Besitzerlangung und Bericht) → § 858 BGB (verbotene Eigenmacht) → § 869 BGB (Besitzschutz Zwangsverwalter) → § 154 ZVG (Gerichtshilfe bei Verweigerung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 150 Rn. 10-30 (Besitzeinweisung)
- Böttcher ZVG 6. Aufl., § 152 Rn. 5-20 (Besitzerlangung Pflichten)
- Dassler/Schiffhauer/Hintzen/Engels ZVG 15. Aufl., § 150 Rn. 15-40 (Praktische Durchführung)

## Triage Besitzübernahme

1. Liegt die Bestallungsurkunde des Gerichts vor? (Legitimation für Vor-Ort-Termin)
2. Sind alle Mieter vorab informiert worden? (Schreiben mind. 3 Tage vorher)
3. Wer begleitet den Termin? (Zeuge empfohlen bei unklarer Situation, ggf. Schlüsseldienst)
4. Sind Versicherungsnachweise bereits angefordert? (Gebäudeversicherung Pflicht ab Besitzerlangung)
5. Fotodokumentation vorbereitet? (Zustands-Beweis für spätere Haftungsfragen)

## Output-Template Besitzübernahmeprotokoll (Auszug)

```
Besitzübernahmeprotokoll
Zwangsverwaltung [ADRESSE]
Aktenzeichen: [AZ]
Datum/Uhrzeit des Termins: [DATUM] [UHRZEIT]
Anwesende: [ZWANGSVERWALTER, ZEUGE, ggf. SCHULDNER, MIETER]

1. Schlüsselübergabe: [JA/NEIN, wer übergeben, Anzahl Schlüsselsätze]
2. Zählerstände: Strom [X], Gas [Y], Wasser [Z]
3. Vorgefundene Schäden (Fotos als Anhang): [LISTE]
4. Mieter angetroffen: [JA/NEIN, Name, Einheit]
5. Sofortmaßnahmen erforderlich: [LISTE]
6. Schuldner anwesend: [JA/NEIN, Reaktion]

Unterschrift Zwangsverwalter: ___________________
Unterschrift Zeuge: ___________________
```
