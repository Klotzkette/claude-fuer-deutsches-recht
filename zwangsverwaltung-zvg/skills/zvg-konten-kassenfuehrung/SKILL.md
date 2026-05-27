---
name: zvg-konten-kassenfuehrung
description: "Kontenfuehrung und Buchfuehrung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. Pruefraster Treuhandkonto Soll Ist Einnahmen Ausgaben Belege Vorschuss Auskunft Gerichtsbericht. Output Kontenspiegel mit Saldouebersicht Belegverzeichnis und monatlichem Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-rechnungslegung."
---

# Konten, Kasse und Buchführung

## Aufgabe

Führt die Finanzverwaltung mit getrenntem Treuhandkonto und prüffähiger Soll-Ist-Buchführung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Treuhandkonto einzurichten ist
- Zahlungen eingehen oder Ausgaben freigegeben werden
- Jahres- oder Schlussrechnung vorbereitet wird

## Eingaben

- Kontoauszüge, Belege, Rent Roll, Ausgaben
- Vorschussanforderungen, Gerichtskosten, Vergütung
- Vorjahressaldo und offene Posten

## Workflow

1. **Konto einrichten** - gesondertes Treuhandkonto und Zahlungsregeln dokumentieren.
2. **Buchen** - Soll- und Isteinnahmen, Ausgaben, Belege und Salden erfassen.
3. **Abgleichen** - Rent Roll, Konto, Belege und Vorschuss laufend abstimmen.
4. **Auskunft** - gerichtsfeste Auskunft und Unterlagenpaket vorbereiten.

## Ausgabe

- Konto- und Kassenbuch
- Soll-Ist-Abgleich
- Belegliste

## Qualitätsgates

- Masse getrennt von Eigenbeständen
- Einzelbuchungen ausgewiesen
- Belege zu jeder Buchung

## Rote Schwellen

- privates Konto
- nicht zuordenbare Bareinnahme
- fehlende Kontoauszüge

## Interne Vorlagen

- assets/templates/konto-kassenbuch.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- § 13 ZwVwV
- § 14 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 14.06.2007 - IX ZB 170/04, NZI 2007, 598 Rn. 16 — Der Zwangsverwalter muss die Verwaltungsgelder auf einem gesonderten Treuhandkonto führen; eine Vermischung mit eigenem Vermögen ist verboten und begründet Schadensersatzpflicht; das Treuhandkonto muss als solches gegenüber der Bank ausgewiesen sein.
- BGH, Beschl. v. 25.09.2008 - IX ZB 205/06, NZI 2009, 55 Rn. 22 — Alle Einnahmen aus Nutzungen und alle Ausgaben sind zeitnah und vollständig zu verbuchen; eine nachträgliche Rekonstruktion der Buchführung ist zwar zulässig aber erhöht das Haftungsrisiko.

## Paragrafenkette Konten/Kassenführung

§ 153 ZVG (Einnahmen aus Nutzungen) → § 152 ZVG (Pflichten Verwaltung) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Jahresrechnung) → § 675 BGB (Geschäftsbesorgungsvertrag) → § 667 BGB (Herausgabe Treuhandgelder) → § 280 BGB (Schadensersatz Treuhandvermischung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 60-80 (Treuhandkonto Buchführung)
- Böttcher ZVG 6. Aufl., § 13 ZwVwV Rn. 1-20 (Buchführungspflichten)
- Palandt/Sprau § 675 BGB Rn. 30-45 (Treuhand Rechenschaftspflicht)

## Triage Konten/Kassenführung

1. Ist das Treuhandkonto eindeutig als solches bei der Bank benannt?
2. Ist die Buchführung tagesaktuell oder bestehen Rückstände?
3. Werden Einnahmen und Ausgaben kontengetrennt nach Einnahmenarten geführt?
4. Ist ein Kassenbuch oder Buchhaltungsprogramm im Einsatz?

## Output-Template Kassenbuch-Schema (Auszug)

```
Buchungsjournal Zwangsverwaltung [ADRESSE]
AZ: [X] — Treuhandkonto: [IBAN]

Datum | Buchungstext | Einnahme | Ausgabe | Saldo | Beleg-Nr.
[D] | Miete Jan [MIETER] Einheit 1 | [BETRAG] | — | [X] | K01
[D] | Versicherungsprämie [ANBIETER] | — | [BETRAG] | [X] | A01
[D] | Grundsteuer Vorauszahlung | — | [BETRAG] | [X] | A02

Saldo per [DATUM]: [BETRAG] EUR
Rücklage laufende Kosten: [BETRAG] EUR
Ausschüttungsfähiger Betrag: [BETRAG] EUR
```
