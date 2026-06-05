---
name: iv-sicherung-iv-tabelle
description: "IV Sicherung IV Tabelle: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# IV Sicherung IV Tabelle

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **IV Sicherung IV Tabelle** im Plugin Insolvenzverwaltung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `iv-sicherung-betriebsfortfuehrung` | Betrieb in Insolvenz fortführen wenn Massemehrung oder Sanierung geplant ist und Lohn Lieferanten und Auftraege gesichert werden muessen. §§ 22 55 InsO Massebegrundung §§ 113 120 InsO Arbeitsverhältnisse. Prüfraster: Fortführungsziel Cash-Bridge Insolvenzgeldzeitraum kritische Lieferanten operative Risiken. Output: Fortführungsplan Liquiditaetsplan Risikoliste. Abgrenzung: nicht für Personalrecht (iv-arbeitsrecht-insolvenzgeld). |
| `iv-tabelle-pruefungstermin` | Insolvenztabelle konsolidieren und Prüfungstermin nach §§ 175 ff. InsO vorbereiten. §§ 175 176 177 InsO Tabellenführung und Widersprueche. Prüfraster: Tabellenbereinigung Doubletten Rang Zinsen Widersprueche nach Grund Betrag Rang Terminmappe. Output: Terminmappe Widerspruchserklärungen Feststellungsantrag. Abgrenzung: nicht für Forderungsanmeldungsprüfung (iv-forderungsanmeldung-prüfung). |

## Arbeitsweg

Im Plugin Insolvenzverwaltung gilt für **IV Sicherung IV Tabelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `iv-sicherung-betriebsfortfuehrung`

**Fokus:** Betrieb in Insolvenz fortführen wenn Massemehrung oder Sanierung geplant ist und Lohn Lieferanten und Auftraege gesichert werden muessen. §§ 22 55 InsO Massebegrundung §§ 113 120 InsO Arbeitsverhältnisse. Prüfraster: Fortführungsziel Cash-Bridge Insolvenzgeldzeitraum kritische Lieferanten operative Risiken. Output: Fortführungsplan Liquiditaetsplan Risikoliste. Abgrenzung: nicht für Personalrecht (iv-arbeitsrecht-insolvenzgeld).

# Sicherung und Betriebsfortführung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sicherung und Betriebsfortführung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüft und steuert, ob und wie der Geschäftsbetrieb im Eröffnungsverfahren oder eröffneten Verfahren fortgeführt werden kann.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Betrieb, Filiale, Praxis oder Werk noch aktiv ist
- Löhne, Lieferanten und Kundenaufträge offen sind
- Massemehrung durch Fortführung möglich erscheint

## Eingaben

- Auftragsbestand, Deckungsbeiträge, Liquiditätsplan
- Lohnliste, Insolvenzgeldzeitraum, Lieferantenkritikalität
- Versicherungen, Genehmigungen, Schlüsselressourcen

## Workflow

1. **Fortführungsziel** - Massemehrung, Sanierung, Verkauf oder geordnete Ausproduktion definieren.
2. **Cash-Bridge** - Einzahlungen, Auszahlungen, Insolvenzgeld, kritische Lieferanten und Steuern planen.
3. **Operative Risiken** - Versicherung, Arbeitsschutz, Umwelt, IT, Schlüsselpersonen und Genehmigungen prüfen.
4. **Entscheidungsvorlage** - Fortführung, Stilllegung oder Hybrid mit Ampel und Bedingungen ausgeben.

## Ausgabe

- Fortführungswochenplan
- Lieferanten- und Kundenampel
- Entscheidungsvorlage für Gericht oder Ausschuss

## Qualitätsgates

- kein Fortführungsbeschluss ohne Cash-Bridge
- kritische Genehmigungen geprüft
- Masseinteresse dokumentiert

## Rote Schwellen

- negative Fortführungsdeckung
- ungeklärte Versicherung
- Lohn- oder Sozialabgabenrisiko

## Interne Vorlagen

- assets/templates/betriebsfortfuehrung-wochenplan.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- §§ 21, 22, 55 InsO
- SGB III Insolvenzgeld als zu prüfende Schnittstelle

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `iv-tabelle-pruefungstermin`

**Fokus:** Insolvenztabelle konsolidieren und Prüfungstermin nach §§ 175 ff. InsO vorbereiten. §§ 175 176 177 InsO Tabellenführung und Widersprueche. Prüfraster: Tabellenbereinigung Doubletten Rang Zinsen Widersprueche nach Grund Betrag Rang Terminmappe. Output: Terminmappe Widerspruchserklärungen Feststellungsantrag. Abgrenzung: nicht für Forderungsanmeldungsprüfung (iv-forderungsanmeldung-prüfung).

# Tabelle und Prüfungstermin

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Tabelle und Prüfungstermin` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bereitet den Prüfungstermin und die Nachbereitung streitiger Forderungen mit sauberer Tabellenlogik vor.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Prüfungstermin ansteht
- Forderungen bestritten oder festgestellt werden müssen
- Tabellenauszüge und Feststellungsklagen relevant werden

## Eingaben

- Tabelle, Prüfvermerke, Anmeldungen
- Widersprüche von Verwalter, Schuldner oder Gläubigern
- Terminsverfügung und Fristen

## Workflow

1. **Tabelle konsolidieren** - Doppelte, Rang, Zinsen, Währungen und Belegstatus bereinigen.
2. **Terminmappe** - jede streitige Forderung mit Entscheidungsvorschlag vorbereiten.
3. **Widersprüche** - Bestreiten nach Grund, Betrag oder Rang klar formulieren.
4. **Nachlauf** - Tabellenauszüge, Feststellungsklagen und Wiedervorlagen steuern.

## Ausgabe

- Terminmappe
- Widerspruchsliste
- Nachlaufplan

## Qualitätsgates

- Bestreiten ist begründet
- Titel und Beweislast gesondert geprüft
- Nachlauf mit Fristen

## Rote Schwellen

- Forderung ohne Prüfung festgestellt
- Widerspruch ohne Grund
- Titelwirkung übersehen

## Interne Vorlagen

- assets/templates/forderungen-und-tabelle.md
- assets/templates/tabellenpruefung.csv

## Amtliche Erstquellen

- §§ 175 bis 180 InsO
- § 176 InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
