---
name: bestellung-beschlagnahme
description: "Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prüfraster Beschluss Bestallung Objekt Schuldner Gläubiger Rang Umfang Weisungen des Gerichts. Output Prüfliste Beschluss mit Vollständigkeitsvermerk und naechsten Schritten für Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit im Zwangsverwaltung Zvg."
---

# Bestellung und Beschlagnahme

## Arbeitsbereich

Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prüfraster Beschluss Bestallung Objekt Schuldner Gläubiger Rang Umfang Weisungen des Gerichts. Output Prüfliste Beschluss mit Vollständigkeitsvermerk und naechsten Schritten für Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bestellung/Beschlagnahme

§ 146 ZVG (Anordnung Zwangsverwaltung) → § 147 ZVG (Beschlagnahme) → § 148 ZVG (Wirkung Beschlagnahme) → § 150 ZVG (Besitzeinweisung) → § 20 ZVG (Wirkung auf Verfügungen) → § 23 ZVG (Beschlagnahme Früchte) → § 57 ZVG (Mieterschutz bei Beschlagnahme)

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

