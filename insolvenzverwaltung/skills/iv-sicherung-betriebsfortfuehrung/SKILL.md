---
name: iv-sicherung-betriebsfortfuehrung
description: "Betrieb in Insolvenz fortfuehren wenn Massemehrung oder Sanierung geplant ist und Lohn Lieferanten und Auftraege gesichert werden muessen. §§ 22 55 InsO Massebegrundung §§ 113 120 InsO Arbeitsverhaeltnisse. Pruefraster: Fortfuehrungsziel Cash-Bridge Insolvenzgeldzeitraum kritische Lieferanten operative Risiken. Output: Fortfuehrungsplan Liquiditaetsplan Risikoliste. Abgrenzung: nicht fuer Personalrecht (iv-arbeitsrecht-insolvenzgeld)."
---

# Sicherung und Betriebsfortführung

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

- BGH, Urt. v. 19.02.2009 — IX ZR 2/08, NZI 2009, 389 — Verwalterhaftung § 60 InsO: IV haftet persoenlich fuer schuldhafte Pflichtverletzungen; Massstab ordentlicher und gewissenhafter Insolvenzverwalter; Glaeubigerausschuss muss informiert werden.
- BGH, Urt. v. 22.09.2005 — IX ZB 55/04 — Verwalterpflichten Betriebsfortfuehrung: IV haftet fuer Verluste aus pflichtwidrig fortgefuehrtem Betrieb; Massebeeintraechtigung verboten; Fortfuehrungsentscheidung muss dokumentiert sein.
- BGH, Urt. v. 08.10.2009 — IX ZR 178/08, NZI 2010, 51 — Zusammenarbeit mit Glaeubigerausschuss: IV muss § 69 InsO-Berichte zeitgerecht erstatten; Zustimmung § 160 InsO bei bedeutsamen Massnahmen einholen; Pflichtverletzung = Haftung § 60.
- BGH, Urt. v. 25.09.2014 — IX ZR 252/13, NZI 2015, 31 — Dokumentationspflichten: IV muss alle Verwaltungshandlungen dokumentieren; nachtraegliche Rekonstruktion heilt Luecken nicht; Schlussrechnung § 66 InsO muss vollstaendig und richtig sein.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Kommentarliteratur

- MüKo InsO/Ganter §§ 56-66 InsO — Insolvenzverwalter-Recht.
- Uhlenbruck/Zipperer §§ 60-61 InsO — Verwalterhaftung im Detail.
- Jaeger/Gerhardt § 66 InsO — Rechnungslegung und Schlussrechnung.
