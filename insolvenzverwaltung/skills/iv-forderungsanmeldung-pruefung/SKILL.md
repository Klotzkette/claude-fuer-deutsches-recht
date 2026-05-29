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

## Rechtliche Grundlagen und BGH-Leitentscheidungen (Stand Mai 2026)

- **BGH IX ZR 114/23 vom 19.12.2024** — Anforderungen an die Forderungsanmeldung (§ 174 Abs. 2 InsO); bei Abtretung müssen Zedent und Zessionar die abgetretene Forderung jeweils gesondert anmelden und einen eigenen Prüfungstermin durchlaufen. Wirksame Anmeldung setzt hinreichende Individualisierung voraus, nicht aber eine schlüssige Rechtsbegründung.
  <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=19.12.2024&Aktenzeichen=IX+ZR+114/23>
- **BGH IX ZR 127/24 vom 13.11.2025** (Wirecard) — Kapitalmarktrechtliche Schadensersatzforderungen geschädigter Aktionäre sind keine einfachen Insolvenzforderungen iSd § 38 InsO; sie treten hinter die einfachen Insolvenzgläubiger zurück. Bedeutung: Bei Prüfung von Aktionärsforderungen Rangfrage konkret einordnen, Bestreiten der einfachen Insolvenzforderungseigenschaft regelmäßig geboten.
  Quelle: BGH-Pressemitteilung 2025/211; <https://www.lto.de/recht/kanzleien-unternehmen/k/bgh-ixzr12724-wirecard-insolvenzmasse-forderungen-aktionaere-urteil>
- Weitere BGH-Linien zur Individualisierung der Forderung, zur Vorsatzfeststellung nach § 174 Abs. 2 / § 302 Nr. 1 InsO vor Ausgabe über dejure.org / openjur.de verifizieren.

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