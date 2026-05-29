---
name: zvg-glaeubiger-schuldner-kommunikation
description: "Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kündigung § 535 BGB Mietrecht. Prüfraster Adressat Anlass Normbezug Ton Fristen Dokumentation. Output Schreibenpaket mit Vorlagen für alle typischen Kommunikationsanlaesse in der Zwangsverwaltung. Abgrenzung zu zvg-berichtswesen-gericht (nur Gericht) und zvg-miet-und-pachtverwaltung."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Gläubiger-Schuldner-Kommunikation

§ 154 ZVG (Aufsicht durch Gericht) → § 153 Abs. 2 ZVG (Auskunftspflicht) → §§ 13-15 ZwVwV (Buchführung Rechnungslegung) → § 20 ZwVwV (Vergütung und Rechenschaft) → § 242 BGB (Treu und Glauben, Auskunftsanspruch analog)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
