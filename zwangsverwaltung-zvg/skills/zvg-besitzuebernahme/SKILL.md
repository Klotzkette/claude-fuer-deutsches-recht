---
name: zvg-besitzuebernahme
description: "Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhältnisse. Prüfraster Vor-Ort-Termin Objektbeschreibung Nutzungen Rechte Mobilien Forderungen Lasten Ausgaben Schluessel. Output Besitzerlangungsbericht mit Objektprotokoll Fotodokumentation Schluesselliste und Meldung ans Gericht. Abgrenzung zu zvg-aktenanlage-objektcockpit und zvg-berichtswesen-gericht."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Besitzübernahme

§ 150 ZVG (Besitzeinweisung durch Gericht) → § 152 ZVG (Rechte und Pflichten ab Besitzerlangung) → § 3 ZwVwV (Besitzerlangung und Bericht) → § 858 BGB (verbotene Eigenmacht) → § 869 BGB (Besitzschutz Zwangsverwalter) → § 154 ZVG (Gerichtshilfe bei Verweigerung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
