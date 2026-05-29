---
name: zvg-kommandocenter
description: "Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen Workflow starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Beschlagnahme Besitz Mietverwaltung Konto Bericht Rechnungslegung Verteilung freistehende Objekte Risiken. Output Routing-Übersicht mit Statusampel zu allen laufenden Zwangsverwaltungen und Tagesaufgaben. Abgrenzung zu zvg-quality-gate (Qualitaetsprüfung vor Abschluss) und zvg-simulation-training."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Kommandocenter

§ 154 ZVG (Gerichtliche Aufsicht) → § 20 ZwVwV (Vergütung und Rechenschaft) → §§ 13-15 ZwVwV (Buchführung und Berichte) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
