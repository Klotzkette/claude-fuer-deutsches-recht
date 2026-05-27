---
name: iv-masseeinsammlung
description: "Massepositionen erfassen und realisieren: Bankguthaben Debitoren Herausgabeansprueche Versicherungen Rueckstaende. §§ 80 148 InsO Verwaltungsbefugnis und Massezugehoerigkeit. Pruefraster: Massekarte Priorisierung realisierbare Forderungen Sicherungsrechte Drittschuldneranschreiben. Output: Massekarte Drittschuldnerschreiben Herausgabeanforderungen. Abgrenzung: nicht fuer aktive Massemehrung durch Verkauf oder Klage (iv-massemehrung-asset-realisation)."
---

# Masseeinsammlung

## Aufgabe

Erfasst und realisiert Massepositionen: Geld, Forderungen, Herausgabeansprüche, Versicherungen, Debitoren, Rückstände und streitige Ansprüche.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Massebestand unvollständig ist
- Banken, Kunden, Versicherer oder Drittschuldner angeschrieben werden müssen
- kurzfristig Liquidität für Kosten und Fortführung gebraucht wird

## Eingaben

- Banklisten, OPOS, Debitoren, Verträge
- Anlagenverzeichnis, Versicherungen, Prozesslisten
- Korrespondenz mit Drittschuldnern

## Workflow

1. **Massekarte** - Alle potenziellen Massepositionen mit Beleg, Schuldner, Fälligkeit und Durchsetzbarkeit anlegen.
2. **Priorisieren** - schnell realisierbare Forderungen vor streitigen Ansprüchen; Sicherheiten trennen.
3. **Anschreiben** - Drittschuldner-, Bank-, Kunden- und Herausgabeschreiben vorbereiten.
4. **Nachhalten** - Zahlungseingänge matchen, Mahnstufen und Klageoptionen steuern.

## Ausgabe

- Masseeinsammlungsregister
- Drittschuldneranschreiben
- Einziehungs- und Mahnplan

## Qualitätsgates

- Absonderungsrechte geprüft
- Fälligkeit und Anspruchsgrund dokumentiert
- Eingänge mit Forderungen gematcht

## Rote Schwellen

- Zahlung an Schuldner statt Massekonto
- ungeklärte Sicherungsabtretung
- Verjährung oder Ausschlussfrist

## Interne Vorlagen

- assets/templates/masseverzeichnis.md
- assets/templates/massenachverfolgung.csv

## Amtliche Erstquellen

- §§ 80 ff. InsO
- §§ 166 ff. InsO


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
