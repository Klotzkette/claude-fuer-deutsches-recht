---
name: rechnungslegung-simulation-training
description: "Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 155 ZVG Einnahmen Ausgaben § 10 ZVG Rangklassen. Prüfraster Jahresrechnung Schlussrechnung Endabrechnung Einnahme-Ausgaben-Rechnung Soll-Ist Belege Salden Verteilung. Output Gerichtsfähige Rechnungslegung mit Saldouebersicht Belegverzeichnis und Verteilungsnachweis. Abgrenzung zu zvg-konten-kassenführung (laufend) und zvg-verteilungsplan-155 im Zwangsverwaltung Zvg."
---

# Rechnungslegung

## Arbeitsbereich

Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 155 ZVG Einnahmen Ausgaben § 10 ZVG Rangklassen. Prüfraster Jahresrechnung Schlussrechnung Endabrechnung Einnahme-Ausgaben-Rechnung Soll-Ist Belege Salden Verteilung. Output Gerichtsfähige Rechnungslegung mit Saldouebersicht Belegverzeichnis und Verteilungsnachweis. Abgrenzung zu zvg-konten-kassenführung (laufend) und zvg-verteilungsplan-155. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Rechnungslegung

§ 152 ZVG (Verwalterpflichten) → § 154 ZVG (Gerichtsaufsicht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 155 ZVG (Verteilungsplan) → § 675 BGB (Rechenschaftspflicht Geschäftsbesorger) → § 667 BGB (Herausgabe)

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

