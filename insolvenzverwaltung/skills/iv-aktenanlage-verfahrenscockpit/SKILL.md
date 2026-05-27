---
name: iv-aktenanlage-verfahrenscockpit
description: "Neue Verfahrensakte anlegen und Verfahrenscockpit strukturieren wenn Insolvenzverwalter oder Sachwalter bestellt wird. §§ 56 80 InsO Verwalterbestellung und Verwaltungsbefugnis. Pruefraster: Aktenzeichen Beteiligtenregister Ordnerplan Massekonto Forderungstabelle Fristen Workstreams. Output: vollstaendiges Verfahrens-Cockpit mit Gliederung Rollenplan und Fristenliste. Abgrenzung: nicht fuer laufende Berichterstattung (iv-berichte) oder Forderungspruefung (iv-forderungsanmeldung-pruefung)."
---

# Aktenanlage und Verfahrenscockpit

## Aufgabe

Eröffnet eine saubere Verfahrensakte mit eigenem Aktenzeichen, Rollen, Ordnerplan, Tabellenlogik und Workstream-Register.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- ein neuer Beschluss, Gutachtenauftrag oder Sachwalterauftrag vorliegt
- eine unstrukturierte Datenlieferung sortiert werden muss
- bestehende Akten nicht auswertbar sind

## Eingaben

- Beschluss, Antrag, Schuldnerfragebogen
- Beteiligte, Banken, Arbeitnehmer, Sicherungsgläubiger
- erste Dokumente und Dateiliste

## Workflow

1. **Aktenkern** - Gericht, Aktenzeichen, Schuldner, Verwalterrolle, Stichtage und Fristen erfassen.
2. **Ordnung** - Ordnerplan für Gericht, Masse, Tabelle, Personal, Verträge, Anfechtung und Berichte erzeugen.
3. **Register** - Beteiligtenregister, Gläubigerliste, Drittschuldnerliste und Zustellwege anlegen.
4. **Kontrollpunkte** - Wiedervorlagen und Verantwortlichkeiten setzen.

## Ausgabe

- Mandatskarte
- Ordnerplan
- Beteiligtenregister
- Fristen- und Workstreamliste

## Qualitätsgates

- keine Partei ohne Rolle
- jede Frist mit Quelle
- keine Vermischung von Masse und Kanzleidaten

## Rote Schwellen

- fehlender Bestellungsbeschluss
- unklare Zuständigkeit
- fehlender Zahlungsweg für Massekonto

## Interne Vorlagen

- assets/templates/iv-mandatskarte.md
- assets/templates/glaeubigerausschuss-bericht.md

## Amtliche Erstquellen

- InsO Gesamtfassung
- §§ 27, 28 InsO


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
