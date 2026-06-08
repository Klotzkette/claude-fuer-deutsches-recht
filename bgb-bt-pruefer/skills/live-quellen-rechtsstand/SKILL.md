---
name: live-quellen-rechtsstand
description: "Live-Quellencheck für BGB-BT: amtliche Gesetzestexte, Rechtsprechungsdatenbanken, Rechtsstand prüfen."
---

# Workflow: Live-Quellen und Rechtsstand

## Zweck

Rechtsstand und Quellen im BGB Besonderer Teil live prüfen: amtliche Gesetzestexte verifizieren, Rechtsprechungsdatenbanken abfragen, Reformstand und jüngste BGH-Entscheidungen einbeziehen.

## Normanker

- Amtliches BGB: https://www.gesetze-im-internet.de/bgb/
- Plugin-Referenz: `references/amtlicher-bgb-bt-normkern.md`
- Neuer Normcheck-Skill: `amtlicher-bgb-bt-normcheck`
- BGH-Rechtsprechungsdatenbank: https://www.bundesgerichtshof.de/
- EUR-Lex für EU-Richtlinien: https://eur-lex.europa.eu/
- dejure.org: https://dejure.org/gesetze/BGB
- OpenJur: https://openjur.de/

## Intake

- Welche Norm soll auf aktuellen Stand geprüft werden?
- Gab es in letzter Zeit bekannte Reformen (z.B. DSM-RL-Umsetzung 2022, Verbrauchsgüterkauf-Änderung)?
- Liegt ein konkretes BGH-Aktenzeichen vor, das verifiziert werden soll?
- Besteht Unsicherheit über den Reformstand einer Norm?
- Wird eine EU-Richtlinie als Auslegungsmaßstab benötigt?

## Prüfraster

1. Normtext-Verifikation: https://www.gesetze-im-internet.de/bgb/ als amtliche Primärquelle
2. Reformstand prüfen: XML-/HTML-Stand, letzte Änderungen am BGB, dokumentarisch noch nicht abgeschlossene Hinweise und Konsequenzen für die konkrete Norm
3. BGH-Rechtsprechung: Aktenzeichen, Datum, Entscheidungsform, Leitsatz über offizielle Datenbank prüfen
4. EU-Richtlinien-Umsetzung: DSM-RL 2019/770 und 2019/771 in §§ 327 ff. und 475b ff. BGB
5. Verbraucherrecht-Reformen: aktuelle Fassungen der §§ 474 ff. und 312 ff. BGB prüfen
6. Fachpresse und Gesetzgebungsvorhaben: BMJ-Website für aktuelle Gesetzgebung
7. Zitierstandards: Gericht, Datum, Aktenzeichen, Entscheidungsform, Fundstelle
8. Unsichere Normen ausdrücklich als Prüfpunkt markieren

## Fallstricke

- Normen aus Modellwissen zitieren ohne Live-Prüfung; Reformstand kann veraltet sein.
- Juris/Beck-RS-Zitate ohne Primärquelle; nicht verifizierbar.
- BGH-Entscheidungen nur mit korrektem Aktenzeichen und Datum angeben.
- EU-Richtlinien-Umsetzungsstand: Umsetzungsgesetz und BGB-Norm getrennt prüfen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Normtext-Verifikations-Protokoll
- Reformstand-Zusammenfassung
- BGH-Entscheidungs-Verifikation
- Quellenverzeichnis mit URLs

## Qualitätsregeln

- Immer amtliche Quelle als Ausgangspunkt; keine Drittzitate ohne Primärquelle.
- BGH-Entscheidungen nur mit vollständigen Metadaten verwenden.
- Reformstand-Unsicherheiten ausdrücklich markieren.

## Anschluss-Skills

- workflow-dokumentenintake
- workflow-anspruchslandkarte
- bt-fristen-erklaerungen-zugang
- amtlicher-bgb-bt-normcheck

## Quellen

- https://www.gesetze-im-internet.de/bgb/
- https://www.bundesgerichtshof.de/
- https://eur-lex.europa.eu/
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
