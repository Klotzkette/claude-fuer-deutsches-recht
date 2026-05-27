---
name: zvg-instandhaltung-sicherung
description: "Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht BauO-Laender. Pruefraster Verkehrssicherungspflicht Notmassnahmen Reparaturen Genehmigung Budget Dokumentation Gerichtszustimmung. Output Massnahmenprotokoll mit Kosten Begruendung Genehmigungsantrag und Bericht ans Gericht. Abgrenzung zu zvg-betriebskosten-hausgeld und zvg-versicherungen-gefahren."
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

- BGH, Beschl. v. 04.10.2007 - IX ZB 220/06, NZI 2007, 726 Rn. 15 — Der Zwangsverwalter hat das Objekt in ordnungsgemäßem Zustand zu erhalten; dringende Instandhaltungsmaßnahmen darf er auch ohne gerichtliche Genehmigung anordnen; größere bauliche Maßnahmen bedürfen der Genehmigung des Vollstreckungsgerichts.
- BGH, Beschl. v. 28.06.2012 - IX ZB 183/09, NZI 2012, 690 — Verkehrssicherungspflichten treffen den Zwangsverwalter ab Besitzerlangung; bei Verletzung dieser Pflicht haftet er persönlich nach § 839 BGB i.V.m. Art. 34 GG, sofern er als Beliehener gilt, andernfalls nach § 280 BGB.

## Paragrafenkette Instandhaltung/Sicherung

§ 152 ZVG (Pflicht ordnungsgemäße Verwaltung) → §§ 8-9 ZwVwV (Instandhaltungsmaßnahmen) → § 154 ZVG (Genehmigung größerer Maßnahmen) → § 823 Abs. 1 BGB (Verkehrssicherungspflicht) → § 836 BGB (Haftung Grundstücksbesitzer) → § 278 BGB (Erfüllungsgehilfe)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 50-75 (Instandhaltungspflicht)
- Böttcher ZVG 6. Aufl., § 152 Rn. 30-55 (Verwalterpflichten Gebäudeerhalt)
- Palandt/Sprau § 836 BGB Rn. 5-15 (Haftung Grundstücksbesitzer)

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
