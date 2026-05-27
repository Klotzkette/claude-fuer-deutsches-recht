---
name: iv-eroeffnungsgutachten
description: "Eroeffnungsgutachten als Sachverstaendiger oder vorlaeufiger Insolvenzverwalter erstellen wenn Gericht Pruefauftrag erteilt. §§ 17 18 19 InsO Eroffnungsgruende §§ 26 54 InsO Massekostendeckung. Pruefraster: Zahlungsunfaehigkeit drohende ZU Ueberschuldung Massekosten Sicherungsbedarf Fortfuehrungsempfehlung. Output: Gutachtengliederung mit Sachverhalt Ergebnis Empfehlung. Abgrenzung: nicht fuer laufende Verwaltung nach Eroeffnung (iv-regelverfahren-eroeffnung)."
---

# Eröffnungsgutachten

## Aufgabe

Erstellt die Arbeitsgliederung für ein Eröffnungsgutachten mit Sachverhalt, Eröffnungsgründen, Massekostendeckung, Sicherungsbedarf und gerichtlicher Empfehlung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- das Gericht ein Gutachten zur Verfahrenseröffnung beauftragt
- Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit oder Überschuldung zu prüfen ist
- eine Fortführung bis zur Eröffnung möglich erscheint

## Eingaben

- Antrag und Anlagen
- BWA, SuSa, OPOS, Bankdaten, Lohn- und Steuerstände
- Vermögensverzeichnis und Sicherheiten

## Workflow

1. **Sachverhalt sichern** - Antrag, Gesellschaft, Geschäftsbetrieb und Unterlagenstand darstellen.
2. **Eröffnungsgründe prüfen** - § 17, § 18 und § 19 InsO anhand konkreter Zahlen trennen.
3. **Masse prüfen** - freie Masse, Kosten, Verwertung, Vorschuss und Massearmut abgleichen.
4. **Empfehlung bauen** - Eröffnung, Abweisung, Sicherungsmaßnahmen oder weitere Aufklärung begründen.

## Ausgabe

- Gutachtengliederung
- Zahlen- und Belegliste
- Empfehlungsentwurf an das Insolvenzgericht

## Qualitätsgates

- Eröffnungsgrund und Kostendeckung getrennt
- jede Zahl mit Quelle
- fehlende Unterlagen als Aufklärungsbedarf markiert

## Rote Schwellen

- Kassenbestand nicht verifiziert
- Sicherheiten ungeklärt
- Betriebsfortführung ohne Liquiditätsbrücke

## Interne Vorlagen

- assets/templates/eroeffnungsgutachten-gliederung.md
- assets/templates/liquiditaetsstatus-kurzcheck.md

## Amtliche Erstquellen

- §§ 16 bis 19 InsO
- § 26 InsO


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
