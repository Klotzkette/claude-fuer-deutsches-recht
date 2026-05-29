---
name: zvg-oeffentliche-lasten
description: "Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Ausgaben. Prüfraster Grundsteuer Abgaben Rang Fälligkeiten Zahlung Nachweis Belegpflicht. Output Lasten-Übersicht mit Rangfolge Zahlungsplan und Nachweis für Gerichtsbericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung."
---

# Öffentliche Lasten und grundstücksbezogene Abgaben

## Aufgabe

Ordnet Grundsteuer, Gebühren, Beiträge und sonstige objektbezogene Lasten in der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Grundsteuer, Gebühren oder Beitragsbescheide eingehen
- Lasten im Besitzerlangungsbericht fehlen
- Verteilung oder Rechnungslegung vorbereitet wird

## Eingaben

- Bescheide, Lastenregister, Kontoauszüge
- Objektdaten, Grundsteuer, Gebühren, WEG-Unterlagen
- Fälligkeiten und Zahlungsnachweise

## Workflow

1. **Lasten erfassen** - Art, Zeitraum, Betrag, Fälligkeit und Behörde aufnehmen.
2. **Rang und Zweck** - öffentliche Last, Betriebskosten, Verwaltungsausgabe oder Schuldneraltlast trennen.
3. **Zahlungsplan** - Liquidität, Vorschussbedarf und Verteilungsauswirkung prüfen.
4. **Nachhalten** - Bescheide, Widerspruchsfristen und Belege ablegen.

## Ausgabe

- Lastenregister
- Zahlungsplan
- Berichtsbaustein

## Qualitätsgates

- Zeitraum sauber abgegrenzt
- Fälligkeit belegt
- Zahlung buchhalterisch zugeordnet

## Rote Schwellen

- Zwangsmaßnahmen der Kommune
- Doppelzahlung
- Beitragsbescheid mit kurzer Frist

## Interne Vorlagen

- assets/templates/versicherung-und-lasten.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 3 Abs. 1 Nr. 5 ZwVwV
- § 15 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Öffentliche Lasten

§ 10 Abs. 1 Nr. 3 ZVG (Vorrang öffentlicher Lasten) → § 12 GrStG (Grundsteuerpflicht) → §§ 10-12 ZwVwV (Ausgaben und Rangfolge) → § 155 ZVG (Verteilungsplan) → § 80 AO (Steuerpflichten bei Vermögensverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Öffentliche Lasten

1. Ist die laufende Grundsteuer erfasst und im Zahlungsplan aufgenommen?
2. Bestehen Rückstände bei öffentlichen Lasten aus der Zeit vor Beschlagnahme?
3. Liegen weitere öffentliche Lasten vor (Anliegerbeiträge Erschließungskosten)?
4. Ist eine Umsatzsteueroption für das Grundstück vorhanden? (Auswirkung auf Vorsteuer)

## Ausgaben-Checkliste Öffentliche Lasten

| Posten | Fälligkeit | Betrag | Bezahlt |
|---|---|---|---|
| Grundsteuer Q1 | 15.02. | [...] | [ ] |
| Grundsteuer Q2 | 15.05. | [...] | [ ] |
| Grundsteuer Q3 | 15.08. | [...] | [ ] |
| Grundsteuer Q4 | 15.11. | [...] | [ ] |
| Erschließungs-/Anliegerbeiträge | gem. Bescheid | [...] | [ ] |
| Müllgebühren/Straßenreinigung | gem. Bescheid | [...] | [ ] |
| Kanalgebühren/Wasserversorgung | gem. Bescheid | [...] | [ ] |
