---
name: ifap-tabellenauszug-178
description: "Tabellenauszug und Feststellungswirkung nach § 178 InsO: Anwendungsfall Forderung ist festgestellt und Gläubiger fragt nach Status oder Insolvenzverwalter muss Tabellenauszug als vollstreckbaren Titel erstellen. § 178 InsO Feststellungswirkung, § 201 InsO Nachhaftung. Prüfraster Feststellungsstatus, Schuldnerwiderspruch abgrenzen, vollstreckbarer Auszug bei Schuldner-ohne-Widerspruch. Output Tabellenauszug mit Feststellungsprotokoll und Vollstreckungshinweis. Abgrenzung zu Prüfentscheidung und zu Streitige-Forderung."
---

# Tabellenauszug und Feststellungswirkung

## Aufgabe

Macht den Feststellungsstatus verständlich und trennt Schuldnerwiderspruch sauber ab.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Forderung ist festgestellt
- Gläubiger fragt nach Status
- Tabellenauszug wird benötigt

## Workflow

1. Feststellungsstatus prüfen: unbestritten, Widerspruch beseitigt, Verwalterwiderspruch, Gläubigerwiderspruch, Schuldnerwiderspruch.
2. Betrag und Rang der Feststellung dokumentieren.
3. Wirkung der Tabelleneintragung intern markieren, ohne externe Rechtsbelehrung zu überziehen.
4. Kommunikation für festgestellte und bestrittene Forderungen trennen.
5. Bei Schuldnerwiderspruch gesondert auf § 184-Spur verweisen.

## Ausgabe

- Feststellungsvermerk
- Tabellenauszug-Anschreiben
- Statusmitteilung
- Widerspruchsübersicht

## Übergabe an die Zwangsvollstreckung

Nach Aufhebung des Insolvenzverfahrens und sofern keine Restschuldbefreiung erteilt wurde, ist der
Tabellenauszug ein Vollstreckungstitel nach § 201 Abs. 2 InsO i.V.m. § 794 Abs. 1 Nr. 4a ZPO.
Für die Vollstreckung aus dem Tabellenauszug lädt das freistehende Plugin `zwangsvollstreckung`
den Skill `zv-tabellenauszug-201-inso`. Er prüft Restschuldbefreiungsstand, dreißigjährige Verjährung
§ 197 Abs. 1 Nr. 5 BGB, Klauselbedürftigkeit und steuert die anschließende PfÜB- oder
Mobiliarvollstreckung.

## Qualitätsgates

- Schuldnerwiderspruch hindert nicht dieselbe Feststellungswirkung gegenüber Verwalter und Gläubigern.
- Tabellenauszug wird nur mit korrektem Status vorbereitet.
- Kein Vollstreckungshinweis ohne Prüfung der Verbraucher-/Restschuldbefreiungsspur.

## Arbeitsstil

Freundlich, präzise, aktennah. Der Skill trennt interne Bewertung, Tabellenvermerk und Außenkommunikation. Bei echten Mandatsdaten sind Berufsgeheimnis, Datenschutz und Kanzleifreigaben zwingend zu beachten.


## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette (Kernbereich)

§ 174 InsO (Anmeldung) → § 175 InsO (Eintragung) → § 176 InsO (Pruefungstermin) → § 177 InsO (nachtraegliche Anmeldung) → § 178 InsO (Tabellenwirkung) → § 179 InsO (Bestreiten) → § 180 InsO (Feststellungsklage) → § 181 InsO (Klageumfang) → § 184 InsO (Schuldnerwiderspruch) → § 189 InsO (Verteilung bestrittene Forderungen)

## Triage

Bevor losgelegt wird, klaere:
1. **Pruefungstermin-Datum?** § 176 InsO — Ladungsfrist 7 Tage; Tabelle vollstaendig vor Termin.
2. **Rang der Forderung?** § 38 InsO (Regelrang), § 39 InsO (Nachrang), §§ 49-51 InsO (Absonderung).
3. **Masseverbindlichkeit oder Insolvenzforderung?** §§ 54-55 InsO vs. § 38 InsO — entscheidend fuer Zahlungsreihenfolge.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.