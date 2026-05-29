---
name: iv-verteilung-schlussrechnung
description: "Abschlussphase des Insolvenzverfahrens durchführen: Schlussrechnung Schlussbericht Verteilungsverzeichnis Quote Nachtragsverteilung. §§ 196 197 InsO Schlussverteilung §§ 66 67 InsO Schlussrechnung. Prüfraster: Abschlussreife Massekonto Kosten Vergutung Rangklassen Quote Nachtragsrisiken. Output: Schlussrechnung Schlussbericht Verteilungsverzeichnis. Abgrenzung: nicht für laufende Berichte (iv-berichte-gericht-gläubiger)."
---

# Schlussbericht, Schlussrechnung und Verteilung

## Aufgabe

Führt die Abschlussphase des Verfahrens: Schlussbericht, Schlussrechnung, Verteilungsverzeichnis, Quote und Nachtragsverteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Verwertung abgeschlossen oder weitgehend abgeschlossen ist
- Schlussverteilung vorbereitet wird
- Gericht Schlussbericht oder Schlussrechnung erwartet

## Eingaben

- Massekonto, Buchhaltung, Verwertungserlöse
- Tabelle, Rangklassen, Kosten, Vergütung
- offene Prozesse und Nachtragsrisiken

## Workflow

1. **Abschlussreife** - offene Masse, Prozesse, Steuern und Verwertung prüfen.
2. **Rechnung** - Einnahmen, Ausgaben, Kosten, Vergütung und Belege konsolidieren.
3. **Verteilung** - Rang, Quote, Abschläge und Verteilungsverzeichnis erstellen.
4. **Bericht** - Schlussbericht, Anlagenliste und Nachtragsverteilungsnotiz ausgeben.

## Ausgabe

- Schlussbericht
- Schlussrechnung
- Verteilungsverzeichnis

## Qualitätsgates

- Massekonto stimmt mit Buchhaltung
- Tabelle final geprüft
- Nachtragspositionen markiert

## Rote Schwellen

- offener Prozess mit Quotenwirkung
- nicht gebuchte Kosten
- Rangfehler

## Interne Vorlagen

- assets/templates/schlussbericht-schlussrechnung.md
- assets/templates/verteilungsverzeichnis.md

## Amtliche Erstquellen

- §§ 187 ff. InsO
- §§ 196 ff. InsO

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