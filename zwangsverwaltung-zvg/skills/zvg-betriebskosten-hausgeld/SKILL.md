---
name: zvg-betriebskosten-hausgeld
description: "Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten pruefen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld BetrKV Betriebskostenarten. Pruefraster Nebenkosten Dienstleister WEG-Hausgeld Versorger Wirtschaftlichkeit Abrechnung Zahlungsplan Belegpflicht. Output Betriebskosten-Uebersicht mit Abrechnungsprotokoll und Zahlungsplan fuer Gericht. Abgrenzung zu zvg-konten-kassenfuehrung und zvg-rechnungslegung."
---

# Betriebskosten, Hausgeld und laufende Objektkosten

## Aufgabe

Verhindert, dass laufende Objektkosten, Hausgeld und Versorgerleistungen die Verwaltung destabilisieren.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- WEG-Hausgeld, Betriebskosten oder Versorgerrechnungen eingehen
- Abrechnungen erstellt oder geprüft werden müssen
- Liquiditätsengpass bei laufender Verwaltung entsteht

## Eingaben

- Hausgeldabrechnung, Wirtschaftsplan, Versorgerverträge
- Betriebskostenbelege, Dienstleisterrechnungen
- Mieter-Vorauszahlungen und Leerstände

## Workflow

1. **Kosten erfassen** - laufende Kosten, öffentliche Lasten, Hausgeld, Dienstleister und Versorger trennen.
2. **Umlage prüfen** - umlagefähige und nicht umlagefähige Positionen markieren.
3. **Liquidität** - Fälligkeiten mit Mieten und Vorschussbedarf abgleichen.
4. **Abrechnung** - Betriebskosten- oder WEG-Schnittstellen für Bericht vorbereiten.

## Ausgabe

- Kostenmatrix
- Zahlungsplan
- Abrechnungsvorbereitung

## Qualitätsgates

- öffentliche Lasten separat
- Umlagefähigkeit geprüft
- Fälligkeit belegt

## Rote Schwellen

- Versorgungssperre
- Hausgeldrückstand mit Verwalterdruck
- unwirtschaftlicher Dienstleister

## Interne Vorlagen

- assets/templates/betriebskosten-hausgeld.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- §§ 9, 13, 15 ZwVwV
- § 155 ZVG

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 04.11.2004 - IX ZB 64/02, NZI 2005, 161 Rn. 18 — Betriebskosten und Hausgeldvorauszahlungen der WEG-Einheit sind laufende Ausgaben der Zwangsverwaltung und bevorzugt aus der Verwaltungsmasse zu bestreiten; rückständiges Hausgeld aus der Zeit vor Beschlagnahme ist Masseschuld.
- BGH, Beschl. v. 21.11.2013 - IX ZB 23/12, NZI 2014, 194 — Hausgeld-Rückstände die während der Zwangsverwaltung entstehen sind nach § 10 Abs. 1 Nr. 2 ZVG vorrangig zu befriedigen; der Verwalter darf Hausgeld nicht aus eigenen Mitteln vorschießen ohne Genehmigung des Gerichts.

## Paragrafenkette Betriebskosten/Hausgeld

§ 153 ZVG (laufende Ausgaben) → § 155 ZVG (Verteilungsplan) → § 10 Abs. 1 Nr. 2 ZVG (Rangklasse Hausgeld) → §§ 8-10 ZwVwV (Ausgaben Verwaltung) → § 16 Abs. 2 WEG (Kostentragung Wohnungseigentuemer) → §§ 556-556d BGB (Betriebskosten Mietverhältnis)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 155 Rn. 15-45 (Rangklassen Betriebskosten Hausgeld)
- Böttcher ZVG 6. Aufl., § 153 Rn. 30-55 (laufende Ausgaben)
- Baermann WEG 15. Aufl., § 16 Rn. 50-80 (Hausgeld und Zwangsverwaltung)

## Triage Betriebskosten/Hausgeld

1. Handelt es sich um eine WEG-Einheit? (Hausgeld-Rückstände haben Vorrang in § 10 ZVG)
2. Sind laufende Betriebskostenvorauszahlungen in den Mietverträgen ausgewiesen?
3. Welche Betriebskosten zahlt der Zwangsverwalter direkt? (Versicherung Grundsteuer Energie)
4. Liegen Hausgeld-Rückstände aus der Zeit vor Beschlagnahme vor?

## Schritt-für-Schritt-Workflow Betriebskostenabrechnung ZVG

1. Alle Kostenpositionen mit Belegen erfassen (Heizung Wasser Müll Hausmeister)
2. Umlageschlüssel aus Mietverträgen und WEG-Beschlüssen prüfen
3. Abrechnungszeitraum festlegen (Kalenderjahr oder Verwaltungszeitraum)
4. Soll-Vorauszahlungen der Mieter gegen tatsächliche Kosten abgleichen
5. Nachzahlungen oder Guthaben berechnen und Mieter informieren
6. Überschüsse in Verteilungsplan nach § 155 ZVG einbeziehen
