---
name: zvg-oeffentliche-lasten
description: "Oeffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschliessungsgebuhren oder Beitraege werden faellig und Zwangsverwalter muss pruefen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Ausgaben. Pruefraster Grundsteuer Abgaben Rang Faelligkeiten Zahlung Nachweis Belegpflicht. Output Lasten-Uebersicht mit Rangfolge Zahlungsplan und Nachweis fuer Gerichtsbericht. Abgrenzung zu zvg-konten-kassenfuehrung und zvg-rechnungslegung."
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

- BGH, Beschl. v. 04.11.2004 - IX ZB 64/02, NZI 2005, 161 Rn. 22 — Öffentliche Lasten (insbesondere Grundsteuer) sind nach § 10 Abs. 1 Nr. 3 ZVG vorrangig aus den Nutzungen zu bestreiten; ihre Nicht-Zahlung durch den Zwangsverwalter kann zu persönlicher Haftung führen.
- BGH, Beschl. v. 21.11.2013 - IX ZB 23/12, NZI 2014, 194 Rn. 15 — Der Anspruch auf Grundsteuer ist eine öffentliche Last, die dingliches Grundstücksrecht hat; der Zwangsverwalter hat sie in Rangklasse 3 nach § 10 ZVG vorrangig zu bedienen.

## Paragrafenkette Öffentliche Lasten

§ 10 Abs. 1 Nr. 3 ZVG (Vorrang öffentlicher Lasten) → § 12 GrStG (Grundsteuerpflicht) → §§ 10-12 ZwVwV (Ausgaben und Rangfolge) → § 155 ZVG (Verteilungsplan) → § 80 AO (Steuerpflichten bei Vermögensverwaltung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 10 Rn. 30-50 (Öffentliche Lasten Rangklasse)
- Böttcher ZVG 6. Aufl., § 10 Rn. 15-35 (Grundsteuer ZVG)
- Tipke/Lang Steuerrecht 24. Aufl., § 12 GrStG (Grundsteuer Verwaltung)

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
