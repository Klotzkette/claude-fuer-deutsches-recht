---
name: iv-vorlaeufige-verwaltung
description: "Erste Massnahmen als vorlaeufliger Insolvenzverwalter nach § 21 InsO umsetzen: Bankkonten Besitz Post Drittschuldner Betrieb. § 21 InsO Sicherungsmassnahmen § 22 InsO Pflichten des vorl. Verwalters. Pruefraster: Beschlussumfang Zustimmungsvorbehalt Postsperre Bankensicherung Drittschuldneranschreiben Kommunikation. Output: Tagesplan Sicherungsprotokoll Kommunikationsschreiben. Abgrenzung: nicht fuer laufendes Regelverfahren (iv-regelverfahren-eroeffnung)."
---

# Vorläufige Insolvenzverwaltung

## Aufgabe

Führt die ersten Tage nach Bestellung als vorläufiger Insolvenzverwalter mit Zustimmungsvorbehalt oder starker Verwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Beschluss nach § 21 InsO vorliegt
- Banken, Kasse, Post und Drittschuldner sofort gesichert werden müssen
- der Betrieb bis zur Entscheidung fortgeführt wird

## Eingaben

- Sicherungsbeschluss
- Bank- und Kassenstände
- Debitoren, Kreditoren, Arbeitnehmer, Lieferanten

## Workflow

1. **Befugnisse lesen** - Beschlussumfang, Zustimmungsvorbehalt, Postsperre und Verfügungsverbote auswerten.
2. **Masse sichern** - Banken, Kasse, Forderungen, Warenlager und Schlüssel kontrollieren.
3. **Kommunikation** - Schuldner, Banken, Drittschuldner, Arbeitnehmer und Gericht informieren.
4. **Tagessteuerung** - Zahlungen nur nach Freigabe, Beleg und Masseinteresse dokumentieren.

## Ausgabe

- Sofortmaßnahmenliste
- Bank- und Kassenprotokoll
- Zahlungsfreigabeprotokoll

## Qualitätsgates

- Beschlussbefugnisse werden wörtlich beachtet
- jede Zahlung hat Zweck, Beleg und Freigabe
- Drittschuldner sind informiert

## Rote Schwellen

- Zahlungen außerhalb des Freigabeprozesses
- fehlender Kassensturz
- unklare Eigentums- oder Sicherungsrechte

## Interne Vorlagen

- assets/templates/vorlaeufige-verwaltung-checkliste.md
- assets/templates/zahlungslauf-freigabe.md

## Amtliche Erstquellen

- § 21 InsO
- § 22 InsO


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
