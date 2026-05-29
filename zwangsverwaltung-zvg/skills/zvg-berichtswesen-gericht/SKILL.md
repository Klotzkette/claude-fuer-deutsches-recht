---
name: zvg-berichtswesen-gericht
description: "Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben § 161 ZVG Rechnungslegung. Prüfraster Besitzerlangung Sachstand Einnahmen Ausgaben Mieter offene Fragen Gerichtsbeschluss-Bedarf. Output Gerichtskonformer Bericht mit Darstellung Einnahmen Ausgaben Mietsituation und Handlungsempfehlungen. Abgrenzung zu zvg-rechnungslegung (Jahresrechnung) und zvg-gläubiger-schuldner-kommunikation."
---

# Berichtswesen an das Vollstreckungsgericht

## Aufgabe

Erstellt klare, vollständige und belegbare Berichte an das Vollstreckungsgericht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Besitzerlangungsbericht fällig ist
- Gericht Sachstand oder Entscheidungsvorlage verlangt
- wesentliche Ereignisse im Objekt auftreten

## Eingaben

- Objektkarte, Besitzprotokoll, Rent Roll
- Kontostand, Rückstände, Maßnahmen, Risiken
- gerichtliche Verfügung

## Workflow

1. **Adressat und Anlass** - Berichtstyp, Zeitraum und konkrete gerichtliche Frage bestimmen.
2. **Faktenblock** - Objekt, Nutzung, Mieten, Lasten, Maßnahmen, Konto und Risiken aktualisieren.
3. **Entscheidungsbedarf** - Zustimmung, Vorschuss, Maßnahme oder Verteilung klar herausstellen.
4. **Anlagen** - Fotos, Konto, Belege und Tabellen referenzieren.

## Ausgabe

- Besitzerlangungsbericht
- Sachstandsbericht
- Gerichtliche Entscheidungsvorlage

## Qualitätsgates

- § 3 ZwVwV-Bericht vollständig
- Zahlen mit Anlagen
- offene Ermittlungen benannt

## Rote Schwellen

- Gefahr oder Versicherungslücke nicht gemeldet
- Vorschussbedarf verschwiegen
- Bericht ohne Kontostand

## Interne Vorlagen

- assets/templates/monatsbericht-gericht.md
- assets/templates/besitzuebernahme-protokoll.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Berichtswesen

§ 153 ZVG (Pflichten laufende Verwaltung) → § 154 ZVG (Gerichtliche Aufsicht) → § 3 ZwVwV (Besitzerlangungsbericht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 20 ZwVwV (Vergütung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Berichtswesen

1. Wann war der Besitzerlangungstermin? (2-Wochen-Frist für Besitzerlangungsbericht)
2. Welche Berichtsfrequenz hat das Gericht vorgegeben? (Monatlich / Quartalsweise / Jährlich)
3. Sind alle Mieter und Nutzungseinheiten im Bericht vollständig erfasst?
4. Wurden wesentliche Veränderungen (Leerstand Kündigung Mietausfall) zeitnah gemeldet?

## Output-Template Besitzerlangungsbericht (Auszug)

**Adressat:** Amtsgericht / Vollstreckungsgericht — Tonfall formell-berichtend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
Aktenzeichen: [AZ]

Besitzerlangungsbericht
Zwangsverwaltung [ADRESSE]

Sehr geehrte Damen und Herren,

gemäß § 3 ZwVwV erstattet der Unterzeichner Bericht über die Besitzerlangung
am [DATUM]:

1. Zustand des Objekts: [BESCHREIBUNG]
2. Nutzungseinheiten: [TABELLE MIETER/EINHEITEN]
3. Vorgefundene Mängel/Sofortmaßnahmen: [LISTE]
4. Laufende Verträge (Versicherung Dienstleister): [LISTE]
5. Besondere Vorkommnisse: [GGFS. SCHULDNER ANWESEND / ZUGANG VERWEIGERT]
6. Treuhandkonto: Eröffnet bei [BANK], IBAN [X].

[DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```
