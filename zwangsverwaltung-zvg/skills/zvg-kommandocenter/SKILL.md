---
name: zvg-kommandocenter
description: "Kommandocenter fuer Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen Workflow starten. Normen §§ 146-161 ZVG Kernvorschriften. Pruefraster Bestellung Beschlagnahme Besitz Mietverwaltung Konto Bericht Rechnungslegung Verteilung freistehende Objekte Risiken. Output Routing-Uebersicht mit Statusampel zu allen laufenden Zwangsverwaltungen und Tagesaufgaben. Abgrenzung zu zvg-quality-gate (Qualitaetspruefung vor Abschluss) und zvg-simulation-training."
---

# Zwangsverwaltungs-Kommandocenter

## Aufgabe

Führt Zwangsverwalterinnen und Zwangsverwalter vom Bestellungsbeschluss bis zur laufenden Verwaltung und Verteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- ein Zwangsverwaltungsbeschluss eingeht
- Objekt, Mieter, Schuldner oder Gläubiger geordnet werden müssen
- unklar ist, welche Sofortmaßnahmen anstehen

## Eingaben

- Anordnungs- und Bestellungsbeschluss
- Grundstücksdaten, Gläubiger, Schuldner, Mieter
- Mietlisten, Lasten, Versicherungen, Kontoangaben

## Workflow

1. **Beschluss lesen** - Objekt, Schuldner, Gläubiger, Rang und Umfang der Beschlagnahme erfassen.
2. **Sofortplan** - Besitz, Mieterinformation, Konto, Versicherung und Lasten priorisieren.
3. **Objektcockpit** - Rent Roll, Rückstände, Ausgaben, Risiken und Gerichtswiedervorlagen anlegen.
4. **Nächste Aktion** - konkrete Schreiben, Vor-Ort-Termin oder Gerichtsanzeige ausgeben.

## Ausgabe

- Objektkarte
- Sofortmaßnahmenliste
- Kommunikationspaket

## Qualitätsgates

- Bestellung und Objekt exakt erfasst
- keine Zahlung auf Privatkonto
- Mieter und Pächter werden korrekt informiert

## Rote Schwellen

- fehlende Versicherung
- akute Gefahr am Objekt
- Mietzahlungen an Schuldner nach Beschlagnahme

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- §§ 150, 152 ZVG
- §§ 1, 3 ZwVwV

## Ergänzende Rechtsprechung

- BGH, Beschl. v. 19.01.2006 - IX ZB 87/04, NZI 2006, 281 Rn. 22 — Der Zwangsverwalter ist zur vollständigen und geordneten Führung der Verwaltungsunterlagen verpflichtet; eine systematische Übersicht über alle laufenden Verfahrenshandlungen ist Grundlage der Rechenschaftspflicht.
- BGH, Beschl. v. 07.12.2007 - IX ZB 74/04, NZI 2008, 186 — Rückstände in der Verwaltungsführung können zum Entzug des Amtes führen; das Vollstreckungsgericht prüft die ordnungsgemäße Verwaltung von Amts wegen.

## Paragrafenkette Kommandocenter

§ 154 ZVG (Gerichtliche Aufsicht) → § 20 ZwVwV (Vergütung und Rechenschaft) → §§ 13-15 ZwVwV (Buchführung und Berichte) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 154 Rn. 15-35 (Gerichtliche Kontrolle)
- Böttcher ZVG 6. Aufl., § 20 ZwVwV Rn. 5-20 (Vergütung und Pflichten)

## Checkliste Kommandocenter (Monatlich)

| Aufgabe | Fälligkeit | Erledigt |
|---|---|---|
| Sollmieten-Abgleich | Monatsanfang | [ ] |
| Rückstands-Update | Monatsmitte | [ ] |
| Ausgabenbelege gesammelt | Monatsende | [ ] |
| Kontoauszüge abgeglichen | Monatsende | [ ] |
| Gerichtsbericht erstellt (falls fällig) | Gem. Anordnung | [ ] |
| Versicherungsprämien gezahlt | Fälligkeitsdatum | [ ] |
| Grundsteuer-Vorauszahlung | 15.02./15.05./15.08./15.11. | [ ] |
| Hausgeldabrechnung WEG (falls EWZ) | Gem. WEG-Plan | [ ] |
