---
name: konten-kassenfuehrung-miet-pachtverwaltung
description: "Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. Prüfraster Treuhandkonto Soll Ist Einnahmen Ausgaben Belege Vorschuss Auskunft Gerichtsbericht. Output Kontenspiegel mit Saldouebersicht Belegverzeichnis und monatlichem Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-rechnungslegung im Zwangsverwaltung Zvg."
---

# Konten, Kasse und Buchführung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Konten/Kassenführung

§ 153 ZVG (Einnahmen aus Nutzungen) → § 152 ZVG (Pflichten Verwaltung) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Jahresrechnung) → § 675 BGB (Geschäftsbesorgungsvertrag) → § 667 BGB (Herausgabe Treuhandgelder) → § 280 BGB (Schadensersatz Treuhandvermischung)

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

