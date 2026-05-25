---
name: ifap-tabellenauszug-178
description: "Erstellt Ausgaben zu Tabellenfeststellung und Tabellenauszug nach § 178 InsO mit Wirkung, Widerspruch und Kommunikationslogik."
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
