---
name: aktenanlage-objektcockpit
description: "Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollständiges Objektcockpit als Arbeitsbasis für alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung im Zwangsverwaltung Zvg."
---

# Aktenanlage und Objektcockpit

## Arbeitsbereich

Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollständiges Objektcockpit als Arbeitsbasis für alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aktenanlage/Objektcockpit

§ 152 ZVG (Pflichten Zwangsverwalter) → § 153 ZVG (Nutzungen) → §§ 2-5 ZwVwV (Aufgaben Verwalter) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Rechnungslegung) → § 154 ZVG (Gerichtliche Aufsicht) → § 159 ZVG (Aufhebung Zwangsverwaltung)

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
1 | ... | ... | ... | ... | ...

TREUHANDKONTO: [BANK, IBAN]
LETZTER GERICHT-BERICHT: [DATUM]
NÄCHSTER BERICHT FÄLLIG: [DATUM]
```

