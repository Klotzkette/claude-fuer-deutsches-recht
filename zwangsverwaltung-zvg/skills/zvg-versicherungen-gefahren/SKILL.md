---
name: zvg-versicherungen-gefahren
description: "Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB Verkehrssicherungspflicht VVG Versicherungsrecht. Pruefraster Gebaeudeversicherung Haftpflicht Beitragsrueckstaende Schadenmeldung Deckungspruefung Notmassnahmen Sicherung. Output Versicherungspruefbericht mit Deckungsnachweis Schadenmeldung und Sicherungsmassnahmen. Abgrenzung zu zvg-instandhaltung-sicherung und zvg-konten-kassenfuehrung."
---

# Versicherungen und Gefahren

## Aufgabe

Prüft und sichert den Versicherungsschutz des verwalteten Objekts.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Versicherungsstatus unklar ist
- Schadensfall, Beitragsrückstand oder Kündigung droht
- Besitzerlangung einen Gefahrenpunkt zeigt

## Eingaben

- Policen, Beitragsrechnungen, Schadenmeldungen
- Objektzustand, Fotos, Dienstleisterberichte
- Konto- und Vorschusslage

## Workflow

1. **Status klären** - Police, Versicherungsnehmer, Objekt, Deckung, Prämien und Rückstände erfassen.
2. **Lücke schließen** - Zahlung, Deckungsbestätigung, Nachversicherung oder Gerichtsinformation vorbereiten.
3. **Schaden** - Schadenanzeige, Belege, Sicherungsmaßnahmen und Anspruchsverfolgung steuern.
4. **Monitoring** - Wiedervorlagen für Prämien und Deckungsänderungen setzen.

## Ausgabe

- Versicherungsregister
- Deckungs- und Schadenvermerk
- Sofortschreiben

## Qualitätsgates

- Deckungsbestätigung belegt
- Rückstände geprüft
- Schaden dokumentiert

## Rote Schwellen

- keine Gebäudeversicherung
- gekündigte Police
- Leitungswasser- oder Brandschaden

## Interne Vorlagen

- assets/templates/versicherung-und-lasten.md
- assets/templates/instandhaltung-gefahrensicherung.md

## Amtliche Erstquellen

- § 3 Abs. 1 Nr. 4 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 28.06.2012 - IX ZB 183/09, NZI 2012, 690 Rn. 18 — Der Zwangsverwalter hat ab Besitzerlangung die Verkehrssicherungspflicht für das Objekt; bei Verletzung dieser Pflicht und Schäden an Dritten haftet er persönlich nach § 823 BGB bzw. § 280 BGB; eine ausreichende Gebäudehaftpflichtversicherung ist zwingend.
- BGH, Beschl. v. 19.01.2006 - IX ZB 87/04, NZI 2006, 281 Rn. 16 — Der Zwangsverwalter ist verpflichtet, das Objekt gegen die typischen Risiken (Brand Leitungswasser Sturm) zu versichern; fehlender Versicherungsschutz begründet Pflichtverletzung und Schadensersatzrisiko.

## Paragrafenkette Versicherungen/Gefahren

§ 152 ZVG (ordnungsgemäße Verwaltung) → § 823 BGB (Verkehrssicherungspflicht) → § 836 BGB (Gebäudeeigentümerhaftung) → § 280 BGB (Pflichtverletzung) → § 9 ZwVwV (Versicherung und Gefahren) → VVG (Versicherungsvertragsrecht allgemein)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., § 152 Rn. 80-100 (Versicherungspflichten)
- Palandt/Sprau § 836 BGB Rn. 5-20 (Gebäudehaftung)
- Böttcher ZVG 6. Aufl., § 9 ZwVwV Rn. 1-15 (Versicherung und Sicherung)

## Triage Versicherungen/Gefahren

1. Ist die Gebäudeversicherung (Feuer Leitungswasser Sturm) aktiv?
2. Ist eine Grundstückshaftpflichtversicherung vorhanden?
3. Sind Prämien laufend bezahlt? (Beitragsrückstand → Deckungsausschluss)
4. Liegen akute Gefahrenstellen vor? (Sofortmaßnahme erforderlich)
5. Wurde nach Besitzerlangung eine Objektbegehung auf Gefahrenstellen durchgeführt?

## Sofortmaßnahmen-Checkliste Gefahren

| Gefahrenstelle | Maßnahme | Priorität | Erledigt |
|---|---|---|---|
| Undichtes Dach | Notreparatur/Plane | SOFORT | [ ] |
| Umgestürzter Baum | Entfernung/Absperrung | SOFORT | [ ] |
| Loser Balkon/Balkongeländer | Absperrung/Reparatur | SOFORT | [ ] |
| Fehlende Heizung Winter | Notversorgung | SOFORT | [ ] |
| Wasserschaden | Absperrung/Trocknung | SOFORT | [ ] |
| Einbruchsschäden | Sicherung/Schlösser | HOCH | [ ] |
| Elektrische Mängel | Elektrofachkraft | HOCH | [ ] |
