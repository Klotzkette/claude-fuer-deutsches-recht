---
name: zvg-rechnungslegung
description: "Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss fuer Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 155 ZVG Einnahmen Ausgaben § 10 ZVG Rangklassen. Pruefraster Jahresrechnung Schlussrechnung Endabrechnung Einnahme-Ausgaben-Rechnung Soll-Ist Belege Salden Verteilung. Output Gerichtsfaehige Rechnungslegung mit Saldouebersicht Belegverzeichnis und Verteilungsnachweis. Abgrenzung zu zvg-konten-kassenfuehrung (laufend) und zvg-verteilungsplan-155."
---

# Rechnungslegung

## Aufgabe

Erstellt prüffähige Jahresrechnung, Schlussrechnung und Endabrechnung nach ZwVwV.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Kalenderjahr endet
- Zwangsverwaltung aufgehoben wird
- Gericht oder Beteiligte Auskunft verlangen

## Eingaben

- Kontoauszüge, Belege, Buchungsjournal
- Rent Roll, Anfangssaldo, Schlussbestand
- Vergütung, Gerichtskosten, Zahlungen an Gläubiger

## Workflow

1. **Daten schließen** - Zeitraum, Anfangsbestand, Endbestand, Kontoauszüge und Belege festlegen.
2. **Gliedern** - Soll-/Isteinnahmen und Ausgaben nach ZwVwV-Konten darstellen.
3. **Prüfen** - Saldo, Belege, USt-Option und Einzelbuchungen abgleichen.
4. **Einreichen** - Jahresrechnung, Schlussrechnung oder Endabrechnung mit Anlagen erstellen.

## Ausgabe

- Jahresrechnung
- Schlussrechnung
- Endabrechnung mit Belegliste

## Qualitätsgates

- Saldo rechnerisch stimmig
- Soll-Ist vollständig
- Umsatzsteuer gesondert, falls Option

## Rote Schwellen

- Konto nicht auf Null bei Endabrechnung
- fehlende Belege
- ungeklärter Anfangsbestand

## Interne Vorlagen

- assets/templates/rechnungslegung.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 14 ZwVwV
- § 15 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 25.09.2008 - IX ZB 205/06, NZI 2009, 55 Rn. 28 — Die Jahresrechnung ist dem Vollstreckungsgericht unaufgefordert nach Ablauf des Rechnungsjahres vorzulegen; sie muss alle Einnahmen und Ausgaben vollständig ausweisen und mit Belegen nachgewiesen sein.
- BGH, Beschl. v. 07.12.2007 - IX ZB 74/04, NZI 2008, 186 Rn. 15 — Die Schlussrechnung ist bei Aufhebung der Zwangsverwaltung unverzüglich und vollständig zu erstellen; ein verbleibender Restbetrag ist dem Vollstreckungsgericht zur Verteilung anzubieten.

## Paragrafenkette Rechnungslegung

§ 152 ZVG (Verwalterpflichten) → § 154 ZVG (Gerichtsaufsicht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 155 ZVG (Verteilungsplan) → § 675 BGB (Rechenschaftspflicht Geschäftsbesorger) → § 667 BGB (Herausgabe)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 70-100 (Rechnungslegung systematisch)
- Böttcher ZVG 6. Aufl., § 14 ZwVwV Rn. 1-20 (Jahresrechnung praktisch)
- Dassler/Schiffhauer/Hintzen/Engels ZVG 15. Aufl., § 15 ZwVwV Rn. 5-25 (Schlussrechnung)

## Triage Rechnungslegung

1. Jahresrechnung oder Schlussrechnung? (Jahresrechnung nach § 14 ZwVwV / Schlussrechnung bei Aufhebung)
2. Liegen alle Kontoauszüge des Rechnungszeitraums lückenlos vor?
3. Sind alle Einnahmen nach Nutzungsarten gegliedert? (Mieteinnahmen/Pachtzins/Sonstiges)
4. Sind Ausgaben nach ZwVwV-Konten kategorisiert?
5. Wird Umsatzsteuer ausgewiesen? (bei bestehender USt-Option)

## Output-Template Jahresrechnung (Schema)

```
JAHRESRECHNUNG ZWANGSVERWALTUNG
Objekt: [ADRESSE]
AZ: [X]
Rechnungszeitraum: 01.01.[JAHR] — 31.12.[JAHR]

A. EINNAHMEN
Sollmieten gesamt: [BETRAG]
Tatsächlich eingezogen: [BETRAG]
Rückstände: [BETRAG]
Sonstige Einnahmen: [BETRAG]
SUMME EINNAHMEN: [BETRAG]

B. AUSGABEN
Betriebskosten/Hausgeld: [BETRAG]
Instandhaltung: [BETRAG]
Öffentliche Lasten (Grundsteuer): [BETRAG]
Versicherungen: [BETRAG]
Verwaltervergütung (brutto): [BETRAG]
Gerichtskosten: [BETRAG]
Sonstiges: [BETRAG]
SUMME AUSGABEN: [BETRAG]

C. ERGEBNIS
Überschuss/Fehlbetrag: [BETRAG]
Anfangsbestand Treuhandkonto: [BETRAG]
Endbestand Treuhandkonto: [BETRAG]

Anlagen: Kontoauszüge K1-K[X], Belege A1-A[Y]
[ORT, DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```
