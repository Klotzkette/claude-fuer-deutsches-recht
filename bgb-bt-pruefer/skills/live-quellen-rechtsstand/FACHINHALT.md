---
name: live-quellen-rechtsstand
description: "Für Workflow: Live-Quellen und Rechtsstand: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Workflow: Live-Quellen und Rechtsstand

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

## Anschluss-Skills

- workflow-dokumentenintake
- workflow-anspruchslandkarte
- bt-fristen-erklaerungen-zugang
- amtlicher-bgb-bt-normcheck

## Quellen

- https://www.gesetze-im-internet.de/bgb/
- https://www.bundesgerichtshof.de/
- https://eur-lex.europa.eu/
