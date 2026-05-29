---
name: iv-forderungsanmeldung-pruefung
description: "Eingehende Forderungsanmeldungen nach § 174 InsO prüfen und Tabelle für Prüfungstermin vorbereiten. §§ 174 175 176 InsO §§ 38 39 InsO Rang. Prüfraster: Schriftform Beleg Grund Betrag Rang Absonderungsrechte vorsaetzlich unerlaubte Handlung Nachrang. Output: Tabellenvermerke Bestreitenserklärungen Nachforderungen. Abgrenzung: nicht für Prüfungstermin selbst (iv-tabelle-prüfungstermin) oder allgemeine Masseeinsammlung."
---

# Forderungsanmeldungen prüfen

## Aufgabe

Prüft eingehende Forderungsanmeldungen so, dass Tabelle, Bestreiten und Prüfungstermin belastbar vorbereitet werden.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Forderungsanmeldungen eingehen
- Belege fehlen oder Rang unklar ist
- vbuH-, Steuerstraf- oder Unterhaltskennzeichen auftauchen

## Eingaben

- Anmeldung, Belege, Rechnungen, Titel
- Schuldnerbuchhaltung, OPOS, Verträge
- Rangangaben und Sicherungsrechte

## Workflow

1. **Form prüfen** - Schriftform oder elektronisches Dokument, Grund, Betrag und Belege erfassen.
2. **Materiell prüfen** - Buchhaltung, Vertrag, Titel, Zinsen, Rang und Absonderungsrechte abgleichen.
3. **Entscheidung** - feststellen, vorläufig bestreiten, endgültig bestreiten oder Nachforderung stellen.
4. **Dokumentieren** - Tabellenvermerk mit Grund, Betrag, Rang und Belegstatus erzeugen.

## Ausgabe

- Prüfvermerk je Forderung
- Nachforderungsschreiben
- Tabellenimportliste

## Qualitätsgates

- Betrag und Grund getrennt geprüft
- Rang nicht aus Gläubigerangabe übernommen
- vbuH nur mit Tatsachen geprüft

## Rote Schwellen

- fehlende Urkunden
- doppelte Anmeldung
- Forderung als Masseverbindlichkeit fehlklassifiziert

## Interne Vorlagen

- assets/templates/forderungen-und-tabelle.md
- assets/templates/tabellenpruefung.csv

## Amtliche Erstquellen

- § 174 InsO
- § 175 InsO

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