---
name: iv-aktenanlage-verfahrenscockpit
description: "Neue Verfahrensakte anlegen und Verfahrenscockpit strukturieren wenn Insolvenzverwalter oder Sachwalter bestellt wird. §§ 56 80 InsO Verwalterbestellung und Verwaltungsbefugnis. Prüfraster: Aktenzeichen Beteiligtenregister Ordnerplan Massekonto Forderungstabelle Fristen Workstreams. Output: vollständiges Verfahrens-Cockpit mit Gliederung Rollenplan und Fristenliste. Abgrenzung: nicht für laufende Berichterstattung (iv-berichte) oder Forderungsprüfung (iv-forderungsanmeldung-prüfung)."
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