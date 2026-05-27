---
name: zvg-bestellung-beschlagnahme
description: "Prueft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprueft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Pruefraster Beschluss Bestallung Objekt Schuldner Glaeubiger Rang Umfang Weisungen des Gerichts. Output Pruefliste Beschluss mit Vollstaendigkeitsvermerk und naechsten Schritten fuer Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit."
---

# Bestellung und Beschlagnahme

## Aufgabe

Prüft die gerichtliche Grundlage der Zwangsverwaltung und den Umfang der Beschlagnahme.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Anordnungs- oder Beitrittsbeschluss eingeht
- Bestallungsurkunde ausgestellt wurde
- unklar ist, welche Rechte und Forderungen erfasst sind

## Eingaben

- Anordnungsbeschluss, Beitritte, Bestallung
- Grundbuch, Forderungsaufstellung, Gläubigerangaben
- gerichtliche Weisungen

## Workflow

1. **Beschlussdaten** - Gericht, Aktenzeichen, Objekt, Schuldner, Gläubiger und Forderung erfassen.
2. **Umfang** - Grundstück, Zubehör, Nutzungen, Forderungen und Rechte bestimmen.
3. **Rang und Beitritt** - betreibende Gläubiger und spätere Beitritte dokumentieren.
4. **Weisungen** - gerichtliche Weisungen und Zustimmungsvorbehalte vormerken.

## Ausgabe

- Beschlussprüfvermerk
- Beschlagnahmeumfang
- Rang- und Gläubigerliste

## Qualitätsgates

- Objektbezeichnung stimmt mit Grundbuch
- Bestellung nicht überdehnt
- Beitritte separat geführt

## Rote Schwellen

- falsches Objekt
- unklare Ranglage
- fehlende Bestallung

## Interne Vorlagen

- assets/templates/bestellungs-und-beschlagnahmecheck.md
- assets/templates/zvg-objektkarte.md

## Amtliche Erstquellen

- § 150 ZVG
- § 2 ZwVwV

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 02.12.2010 - IX ZB 120/09, NZI 2011, 108 Rn. 12 — Die Beschlagnahme des Grundstücks wird mit Zustellung des Anordnungsbeschlusses an den Schuldner wirksam; ab diesem Zeitpunkt sind Verfügungen des Schuldners über das Grundstück und dessen Früchte dem Gläubiger gegenüber unwirksam.
- BGH, Beschl. v. 17.07.2003 - IX ZB 525/02, NJW 2003, 3347 — Mieten aus dem Grundstück fallen mit Beschlagnahme unter die Verwaltungsmasse; Zahlungen des Mieters an den Schuldner nach Beschlagnahme haben schuldbefreiende Wirkung nur wenn der Mieter keine Kenntnis von der Beschlagnahme hatte.

## Paragrafenkette Bestellung/Beschlagnahme

§ 146 ZVG (Anordnung Zwangsverwaltung) → § 147 ZVG (Beschlagnahme) → § 148 ZVG (Wirkung Beschlagnahme) → § 150 ZVG (Besitzeinweisung) → § 20 ZVG (Wirkung auf Verfügungen) → § 23 ZVG (Beschlagnahme Früchte) → § 57 ZVG (Mieterschutz bei Beschlagnahme)

## Kommentarliteratur

- Stöber ZVG 22. Aufl., §§ 146-150 Rn. 1-50 (Anordnung und Beschlagnahme)
- Böttcher ZVG 6. Aufl., § 147 Rn. 5-25 (Beschlagnahmewirkung)
- Dassler/Schiffhauer/Hintzen/Engels ZVG 15. Aufl., § 148 Rn. 10-40 (Umfang Beschlagnahme)

## Triage Bestellung/Beschlagnahme

1. Datum des Zustellungsbeschlusses und Datum der Zustellung an Schuldner? (Beschlagnahme ab Zustellung)
2. Wurden Mieter über die Beschlagnahme informiert? (Zahlungspflicht Miete an Zwangsverwalter)
3. Hat Schuldner vor Beschlagnahme Mieten im Voraus vereinnahmt? (§ 153 ZVG Rückforderung prüfen)
4. Liegt eine eingetragene Grundschuld oder Hypothek vor? (Gläubiger-Rang für Ausschüttungen)

## Output-Template Mieter-Benachrichtigung nach Beschlagnahme

**Adressat:** Mieter — Tonfall sachlich-erklärend

```
[ZWANGSVERWALTER, ADRESSE]

An [MIETER NAME]
[ADRESSE MIETWOHNUNG]

[ORT], [DATUM]

Betreff: Zwangsverwaltung — Zahlungsanweisung für Miete

Sehr geehrte/r Herr/Frau [NAME],

über das Grundstück [ADRESSE, GRUNDBUCHBEZEICHNUNG] wurde durch Beschluss
des Amtsgerichts [ORT] vom [DATUM] (AZ [X]) die Zwangsverwaltung angeordnet.
Ich wurde zum Zwangsverwalter bestellt.

Ab sofort ist die monatliche Miete von [BETRAG] EUR ausschließlich auf
folgendes Treuhandkonto zu zahlen:
IBAN: [X], BIC: [Y], Bank: [Z], Verwendungszweck: [AZ + IHRE EINHEIT]

Zahlungen an den Eigentümer haben nach Beschlagnahme keine schuldbefreiende
Wirkung mehr (§ 148 ZVG).

Mit freundlichen Grüßen
[ZWANGSVERWALTER]
```
