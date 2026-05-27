---
name: iv-anfechtung-129ff
description: "Insolvenzanfechtungsansprueche nach §§ 129 ff. InsO pruefen und verfolgen wenn Zahlungen oder Sicherheiten vor Insolvenzantrag verdaechtig sind. §§ 130 131 133 135 InsO Deckungsanfechtung Vorsatzanfechtung Bargeschaeft. Pruefraster: Tatbestand Frist Empfaengerkenntnis Gegenleistung Anspruchshoehe Vergleichspotenzial. Output: Anfechtungsschreiben Klageentwurf Vergleichsrechnung. Abgrenzung: nicht fuer § 15b-Haftungsklagen (iv-zahlungsklagen-15b) oder allgemeine Forderungspruefung."
---

# Insolvenzanfechtung §§ 129 ff. InsO

## Aufgabe

Prüft und verfolgt Insolvenzanfechtungsansprüche strukturiert aus Verwaltersicht.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zahlungen oder Sicherheiten vor Antrag verdächtig sind
- Anfechtungsschreiben oder Klage vorbereitet wird
- Vergleichsverhandlungen mit Anfechtungsgegnern laufen

## Eingaben

- Zahlungsjournal, OPOS, Kontoauszüge
- Kommunikation, Mahnungen, Ratenvereinbarungen
- Insolvenzreife-Zeitpunkt und Gläubigerkenntnis

## Workflow

1. **Sachverhalt clustern** - Zahlung, Rechtshandlung, Datum, Gegenleistung, Kenntnisindizien und Empfänger erfassen.
2. **Tatbestand wählen** - §§ 130 bis 135 InsO, § 133 InsO und Bargeschäft sauber trennen.
3. **Anspruch rechnen** - Hauptforderung, Zinsen, Gegenrechte, Durchsetzbarkeit und Vergleichsanker berechnen.
4. **Output** - Anfechtungsschreiben, Klagegerüst oder Vergleichsvorlage erstellen.

## Ausgabe

- Anfechtungsmatrix
- Anspruchsberechnung
- Schreiben oder Klagegerüst

## Qualitätsgates

- kein Tatbestand ohne Zeitraum
- Kenntnisindizien belegbasiert
- Bargeschäft gesondert geprüft

## Rote Schwellen

- drohende Verjährung
- unvollständige Kontoauszüge
- wirtschaftlich sinnloser Prozess

## Interne Vorlagen

- assets/templates/anfechtungsmatrix-129ff.md
- assets/templates/anfechtungsschreiben.md

## Amtliche Erstquellen

- §§ 129 bis 147 InsO
- § 146 InsO


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
