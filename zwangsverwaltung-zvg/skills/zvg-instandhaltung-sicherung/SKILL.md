---
name: zvg-instandhaltung-sicherung
description: "Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht BauO-Laender. Prüfraster Verkehrssicherungspflicht Notmassnahmen Reparaturen Genehmigung Budget Dokumentation Gerichtszustimmung. Output Massnahmenprotokoll mit Kosten Begründung Genehmigungsantrag und Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-versicherungen-gefahren."
---

# Instandhaltung, Sicherung und Gefahrenabwehr

## Aufgabe

Steuert notwendige Maßnahmen zur Erhaltung und sicheren Nutzung des Objekts.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Schäden, Mängel oder Gefahren gemeldet werden
- Reparaturen oder Notmaßnahmen nötig sind
- Budget oder gerichtliche Zustimmung unklar ist

## Eingaben

- Mängelmeldung, Fotos, Kostenvoranschläge
- Versicherung, Mietereinwendungen, Behördenpost
- Kontostand und Vorschusslage

## Workflow

1. **Gefahr einstufen** - akute Gefahr, Substanzerhalt, Komfort oder Modernisierung trennen.
2. **Budget und Zustimmung** - Kosten, Liquidität, Vorschuss und Zustimmungsvorbehalte prüfen.
3. **Beauftragung** - Dienstleister, Leistungsumfang, Dokumentation und Abnahme vorbereiten.
4. **Bericht** - Gericht und Beteiligte über wesentliche Maßnahmen informieren.

## Ausgabe

- Gefahren- und Maßnahmenvermerk
- Beauftragungsentwurf
- Berichtsbaustein

## Qualitätsgates

- Notmaßnahme begründet
- Kosten plausibilisiert
- Fotos und Belege gesichert

## Rote Schwellen

- Verkehrssicherungsrisiko
- Brandschutzmangel
- fehlende Versicherung

## Interne Vorlagen

- assets/templates/instandhaltung-gefahrensicherung.md
- assets/templates/versicherung-und-lasten.md

## Amtliche Erstquellen

- § 1 ZwVwV
- § 9 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Instandhaltung/Sicherung

§ 152 ZVG (Pflicht ordnungsgemäße Verwaltung) → §§ 8-9 ZwVwV (Instandhaltungsmaßnahmen) → § 154 ZVG (Genehmigung größerer Maßnahmen) → § 823 Abs. 1 BGB (Verkehrssicherungspflicht) → § 836 BGB (Haftung Grundstücksbesitzer) → § 278 BGB (Erfüllungsgehilfe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Instandhaltung/Sicherung

1. Liegen akute Gefahrenstellen vor? (Sofortmaßnahme ohne Genehmigung möglich)
2. Sind größere Maßnahmen geplant? (Gerichtsgenehmigung erforderlich ab ca. 2.000 EUR netto)
3. Ist die Gebäudeversicherung aktiv und ausreichend?
4. Wer führt die Instandhaltungsarbeiten durch? (Auftragnehmer-Vertrag mit Vergabe-Dokumentation)

## Output-Template Gerichtsantrag Instandhaltung

**Adressat:** Amtsgericht — Tonfall formell-antragend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
AZ: [X]

Antrag auf Genehmigung einer Instandhaltungsmaßnahme

Sehr geehrte Damen und Herren,

in der Zwangsverwaltung [ADRESSE] beantrage ich die Genehmigung folgender Maßnahme:

Maßnahme: [BESCHREIBUNG]
Grund: [SCHADENSURSACHE, DRINGLICHKEIT]
Kosten: [ANGEBOTE ANLIEGEND — ANLAGE 1-3]
Empfohlenes Angebot: [BIETER, BETRAG]

Die Maßnahme ist zur Abwehr weiterer Schäden und zur Erfüllung der
Verkehrssicherungspflicht unaufschiebbar.

[DATUM, UNTERSCHRIFT]
```
