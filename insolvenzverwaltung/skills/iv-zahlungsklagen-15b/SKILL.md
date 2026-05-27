---
name: iv-zahlungsklagen-15b
description: "Zahlungsklagen nach § 15b InsO gegen Geschaeftsleiter vorbereiten wenn Zahlungen nach Insolvenzreife erfolgt sind. § 15b InsO §§ 17 19 InsO Insolvenzreife. Pruefraster: Insolvenzreifedatum Zahlungen nach Stichtag Organstellung Ausnahmen ordnungsgemaeßer Geschaeftsgang D-und-O-Deckung Vergleichsanker. Output: Haftungsanalyse Klageentwurf Vergleichsrechnung. Abgrenzung: nicht fuer Anfechtungsansprueche (iv-anfechtung-129ff)."
---

# Zahlungsklagen nach § 15b InsO

## Aufgabe

Bereitet Ansprüche gegen Geschäftsleiter wegen Zahlungen nach Insolvenzreife aus Sicht der Insolvenzmasse vor.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zahlungsunfähigkeit oder Überschuldung vor Antrag plausibel ist
- Zahlungen nach Eintritt der Insolvenzreife rekonstruiert werden
- D&O-Deckung oder Vergleich geprüft wird

## Eingaben

- Liquiditätsstatus, BWA, OPOS, Bankjournale
- Organstellung, Geschäftsverteilung, Beschlüsse
- Zahlungslisten, Steuer- und SV-Zahlungen, Fortführungsmaßnahmen

## Workflow

1. **Insolvenzreife datieren** - § 17 und § 19 InsO getrennt, stichtagsbezogen und belegbasiert prüfen.
2. **Zahlungen filtern** - Zahlungen nach Stichtag mit Empfänger, Zweck, Konto und Beleg erfassen.
3. **Ausnahmen prüfen** - ordnungsgemäßer Geschäftsgang, Antragstellung, Steuerprivileg und Masseinteresse prüfen.
4. **Klage bauen** - Anspruch, Schaden, Verjährung, D&O und Beweisangebot strukturieren.

## Ausgabe

- § 15b-Zahlungsmatrix
- Anspruchs- und Verteidigungsmatrix
- Klageentwurf oder Vergleichsvermerk

## Qualitätsgates

- Insolvenzreife nicht geschätzt, sondern begründet
- Zahlungslisten bankseitig belegbar
- Ausnahmen transparent geprüft

## Rote Schwellen

- unvollständige Bankdaten
- unklare Organstellung
- Verjährungsdruck

## Interne Vorlagen

- assets/templates/zahlungsklage-15b.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- § 15b InsO
- §§ 17, 19 InsO


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
