---
name: zvg-aktenanlage-objektcockpit
description: "Aktenanlage und Objektcockpit fuer den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Pruefraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollstaendiges Objektcockpit als Arbeitsbasis fuer alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung."
---

# Aktenanlage und Objektcockpit

## Aufgabe

Eröffnet eine vollständige Zwangsverwaltungsakte mit Objektkarte, Beteiligten, Rent Roll, Lasten, Konto und Berichtsterminen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- eine neue Zwangsverwaltung übernommen wird
- Bestandsakten unvollständig sind
- Berichte und Rechnungslegung aufgebaut werden müssen

## Eingaben

- Bestellungsurkunde, Grundbuchdaten, Objektunterlagen
- Mietverträge, Betriebskosten, Versicherungen, öffentliche Lasten
- Kontodaten und Gerichtsvorgaben

## Workflow

1. **Akte aufsetzen** - Objekt, Beteiligte, Aktenzeichen, Bestallung und Zuständigkeiten erfassen.
2. **Register bauen** - Mieter/Pächter, Lasten, Verträge, Versicherungen, Dienstleister und Schlüssel erfassen.
3. **Finanzen** - Treuhandkonto, Sollmieten, Istmieten, Ausgaben und Vorschusslogik anlegen.
4. **Berichte** - Besitzerlangungsbericht, Monats- und Jahresrechnung vormerken.

## Ausgabe

- Objektkarte
- Rent Roll
- Lasten- und Versicherungsregister
- Wiedervorlagen

## Qualitätsgates

- jede Nutzungseinheit mit Sollmiete
- öffentliche Lasten separat
- Buchführung getrennt

## Rote Schwellen

- fehlende Bestallungsurkunde
- Objektzugang ungeklärt
- kein Treuhandkonto

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 2 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 19.01.2006 - IX ZB 87/04, NZI 2006, 281 — Der Zwangsverwalter hat ab Besitzerlangung sämtliche Nutzungen einzuziehen; eine vollständige Aktenanlage mit Beteiligtenverzeichnis und Mieterliste ist unverzüglich zu erstellen und dem Vollstreckungsgericht mitzuteilen.
- BGH, Beschl. v. 10.10.2013 - IX ZB 229/11, NZI 2014, 44 Rn. 8 — Die Pflichten des Zwangsverwalters umfassen die ordnungsgemäße Buchführung und Rechnungslegung; fehlende oder fehlerhafte Aktenanlage kann die Vergütung nach ZwVwV mindern.

## Paragrafenkette Aktenanlage/Objektcockpit

§ 152 ZVG (Pflichten Zwangsverwalter) → § 153 ZVG (Nutzungen) → §§ 2-5 ZwVwV (Aufgaben Verwalter) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Rechnungslegung) → § 154 ZVG (Gerichtliche Aufsicht) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 20-45 (Pflichten Zwangsverwalter)
- Böttcher ZVG 6. Aufl., § 153 Rn. 10-30 (Nutzungseinziehung und Verwalterpflichten)
- Dassler/Schiffhauer/Hintzen/Engels ZVG 15. Aufl., § 152 Rn. 30-55 (Aktenführung)

## Triage Aktenanlage

Kläre bei Übernahme:
1. Liegt die vollständige Bestellungsurkunde vor? (Pflichtdokument — ohne keine Legitimation)
2. Grundbuchauszug aktuell (max. 3 Monate alt)?
3. Alle Nutzungseinheiten mit Mietverträgen erfasst?
4. Treuhandkonto bei einer Bank eröffnet und dem Gericht benannt?
5. Etwaige Vorlasten (Grundschulden Grundpfandrechte) aus Abt. III Grundbuch erfasst?

## Output-Template Objektkarte (Auszug)

```
OBJEKTKARTE — ZWANGSVERWALTUNG
Aktenzeichen Vollstreckungsgericht: [AZ]
Bestellungsurkunde vom: [DATUM]

Objekt: [ADRESSE, GRUNDBUCHBEZEICHNUNG]
Gemarkung / Flurstück: [...]
Grundbuch: Amtsgericht [X], Blatt [Y]

BETEILIGTE
Schuldner: [NAME, ADRESSE]
Gläubiger: [NAME, ADRESSE, FORDERUNG]
Vollstreckungsgericht: AG [ORT], Richter/Rechtspfleger: [NAME]
Zwangsverwalter: [NAME, BÜRO, TELEFON]

NUTZUNGSEINHEITEN
Nr. | Lage | Mieter | Nettomiete | NK-Vorauszahlung | Vertrag vom
1   | ...  | ...    | ...        | ...               | ...

TREUHANDKONTO: [BANK, IBAN]
LETZTER GERICHT-BERICHT: [DATUM]
NÄCHSTER BERICHT FÄLLIG: [DATUM]
```
