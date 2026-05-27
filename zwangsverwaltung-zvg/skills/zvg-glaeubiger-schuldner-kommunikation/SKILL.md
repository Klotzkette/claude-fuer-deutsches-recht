---
name: zvg-glaeubiger-schuldner-kommunikation
description: "Schriftwechsel in der Zwangsverwaltung mit Schuldner Glaeubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kuendigung § 535 BGB Mietrecht. Pruefraster Adressat Anlass Normbezug Ton Fristen Dokumentation. Output Schreibenpaket mit Vorlagen fuer alle typischen Kommunikationsanlaesse in der Zwangsverwaltung. Abgrenzung zu zvg-berichtswesen-gericht (nur Gericht) und zvg-miet-und-pachtverwaltung."
---

# Gläubiger-, Schuldner- und Drittschuldnerkommunikation

## Aufgabe

Erstellt klare, rollenrichtige Schreiben in der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Mieter, Schuldner, Gläubiger oder Behörden informiert werden müssen
- Konflikte über Zutritt, Mieten oder Maßnahmen entstehen
- Gerichtskommunikation vorbereitet wird

## Eingaben

- Rolle und Adressat
- Beschluss, Objekt, Anlass, gewünschte Reaktion
- Frist, Belege und Tonalität

## Workflow

1. **Adressat klären** - Rolle, Rechte, Pflichten und Zustellweg bestimmen.
2. **Kernbotschaft** - Was ist passiert, was wird verlangt, bis wann, mit welcher Folge.
3. **Belege** - Beschluss, Bestallung, Konto, Fotos oder Tabellen beifügen.
4. **Nachhalten** - Wiedervorlage, Antwortauswertung und Eskalation setzen.

## Ausgabe

- Schreibenentwurf
- Anlagenliste
- Wiedervorlage

## Qualitätsgates

- keine Drohung ohne Grundlage
- Zahlstelle eindeutig
- Adressat nicht verwechselt

## Rote Schwellen

- Schuldner blockiert Objektzugang
- Mieter zahlen falsch
- Gläubiger drängt auf unzulässige Sonderzahlung

## Interne Vorlagen

- assets/templates/schuldner-glaeubiger-kommunikation.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 4 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 04.10.2007 - IX ZB 220/06, NZI 2007, 726 Rn. 11 — Der Zwangsverwalter steht im Dienst aller Beteiligten (Gläubiger und Schuldner); er ist zur gleichmäßigen Information beider verpflichtet und darf keine Partei bevorzugen.
- BGH, Beschl. v. 12.01.2006 - IX ZB 239/04, NZI 2006, 234 — Der betreibende Gläubiger hat ein Auskunftsrecht über den Stand der Verwaltung; der Zwangsverwalter ist verpflichtet, auf Anfrage der Beteiligten zeitnah zu berichten und Einsicht in die Verwaltungsunterlagen zu gewähren.

## Paragrafenkette Gläubiger-Schuldner-Kommunikation

§ 154 ZVG (Aufsicht durch Gericht) → § 153 Abs. 2 ZVG (Auskunftspflicht) → §§ 13-15 ZwVwV (Buchführung Rechnungslegung) → § 20 ZwVwV (Vergütung und Rechenschaft) → § 242 BGB (Treu und Glauben, Auskunftsanspruch analog)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 154 Rn. 5-25 (Gerichtliche Aufsicht Auskunftspflicht)
- Böttcher ZVG 6. Aufl., § 153 Rn. 40-60 (Informationspflichten)

## Triage Kommunikation

1. Wer ist betreibender Gläubiger? (Alle Gläubiger in Rangklassen nach § 10 ZVG erfassen)
2. Liegt eine Bevollmächtigung des Gläubigers vor? (Ansprechpartner/Kanzlei)
3. Kommuniziert der Schuldner kooperativ? (Verweigerung → Gerichtsantrag)
4. Haben weitere Gläubiger beigetreten?

## Output-Template Gläubigerinfo-Schreiben (Auszug)

**Adressat:** Betreibender Gläubiger — Tonfall formell-berichtend

```
An [GLÄUBIGER / BEVOLLMÄCHTIGTE KANZLEI]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]
Quartalsbericht [QUARTAL/JAHR]

Sehr geehrte Damen und Herren,

zum Stand der Zwangsverwaltung berichte ich:

Einnahmen [QUARTAL]: [BETRAG]
Ausgaben [QUARTAL]: [BETRAG]
Kontostand per [DATUM]: [BETRAG]
Ausschüttungsfähiger Betrag nach Rücklage: [BETRAG]

Besondere Vorkommnisse: [LEERSTAND REPARATUR RECHTSTREIT]

Nächster Auszahlungsantrag: [DATUM]

[UNTERSCHRIFT ZWANGSVERWALTER]
```
