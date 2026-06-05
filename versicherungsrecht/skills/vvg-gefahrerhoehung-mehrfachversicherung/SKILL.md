---
name: vvg-gefahrerhoehung-mehrfachversicherung
description: "VVG Gefahrerhoehung Mehrfachversicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# VVG Gefahrerhoehung Mehrfachversicherung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **VVG Gefahrerhoehung Mehrfachversicherung** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vvg-gefahrerhoehung-23-27` | Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausalitätsprüfung in Sach-, Haftpflicht- und Personenversicherungen. |
| `vvg-mehrfachversicherung-78` | Mehrfachversicherung und Doppelversicherung: Innenausgleich, Anzeige, Überversicherung, Regress und Taktik bei mehreren Versicherern. |
| `vvg-obliegenheit-28-quotelung-kausalitaet` | § 28 VVG nach Eintritt des Versicherungsfalls: Anzeige, Aufklärung, Rettung, Mitwirkung, Kausalitätsgegenbeweis, Vorsatz/grobe Fahrlässigkeit und Quotierung. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **VVG Gefahrerhoehung Mehrfachversicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vvg-gefahrerhoehung-23-27`

**Fokus:** Gefahrerhöhung vor und nach Vertragsschluss: willentlich/unwillentlich, Anzeige, Kündigung, Leistungsfreiheit und Kausalitätsprüfung in Sach-, Haftpflicht- und Personenversicherungen.

# Gefahrerhöhung §§ 23–27 VVG

## Einsatz

Für Fälle, in denen der Versicherer behauptet, das Risiko sei nach Vertragsschluss gefährlicher geworden: Leerstand, Nutzungsänderung, Sicherungen, Gesundheitsrisiko, gewerblicher Betrieb.

## Norm- und Quellenanker

VVG §§ 23–27, 81; BGB §§ 133, 157; AVB.

## Arbeitsfragen

1. Welche Risikobeschreibung stand bei Vertragsschluss fest?
2. Welche Änderung trat wann ein und wer wusste davon?
3. Ist die Änderung gefahrerheblich oder nur normaler Lebensverlauf?
4. Wurde angezeigt und wie reagierte der Versicherer?
5. War die Gefahrerhöhung kausal für den Schaden?

## Output

Gefahrerhöhungsprüfvermerk mit Zeitleiste, Kausalitätsargumenten und Versichererantwort.

## Red Flags

- bloße Wertsteigerung als Gefahrerhöhung verkauft
- Nutzungsänderung nicht kausal
- Versicherer kannte die Änderung
- AVB verschieben gesetzliche Wertungen unangemessen

## Anschluss-Skills

- wohngebaeude-leitungswasser-sturm-hagel-brand
- kfz-kasko-grobe-fahrlaessigkeit-entwendung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `vvg-mehrfachversicherung-78`

**Fokus:** Mehrfachversicherung und Doppelversicherung: Innenausgleich, Anzeige, Überversicherung, Regress und Taktik bei mehreren Versicherern.

# Mehrfachversicherung § 78 VVG

## Einsatz

Für Schäden mit mehreren Policen: Hausrat/Gebäude, Cyber/D&O, Betriebsunterbrechung/Sach, Kreditversicherung/Factoring.

## Norm- und Quellenanker

VVG §§ 77–79, 78, 86; BGB Gesamtschuld analog; AVB.

## Arbeitsfragen

1. Welche Policen decken denselben Gefahrbereich und dasselbe Interesse?
2. Liegt echte Mehrfachversicherung oder nur Deckungslücke nebeneinander vor?
3. Wer zahlt zuerst und wer nimmt Regress?
4. Welche Anzeigeobliegenheiten bestehen?

## Output

Deckungslandkarte mehrerer Versicherer, Ausgleichsplan und Musterschreiben.

## Red Flags

- Versicherer schieben sich Zuständigkeit zu
- Interessen nicht identisch
- Summenversicherung mit Schadenversicherung verwechselt
- Regress bedroht schnelle Liquidität

## Anschluss-Skills

- subrogation-regress-86-vvg
- cyberversicherung-ransomware-sanktionsrecht

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `vvg-obliegenheit-28-quotelung-kausalitaet`

**Fokus:** § 28 VVG nach Eintritt des Versicherungsfalls: Anzeige, Aufklärung, Rettung, Mitwirkung, Kausalitätsgegenbeweis, Vorsatz/grobe Fahrlässigkeit und Quotierung.

# Obliegenheitsverletzung § 28 VVG und Quotierung

## Einsatz

Der Skill trennt echte Obliegenheit von bloßer Mitwirkungsbitte und verhindert automatische Totalablehnungen.

## Norm- und Quellenanker

VVG §§ 28, 30, 31, 82, 86; AVB; BGB § 242; ZPO.

## Arbeitsfragen

1. Welche Obliegenheit ist vertraglich oder gesetzlich normiert?
2. Wurde der Versicherungsnehmer korrekt über Folgen belehrt?
3. War die Verletzung vorsätzlich, grob fahrlässig oder einfach fahrlässig?
4. Ist der Kausalitätsgegenbeweis möglich?
5. Welche Quote ist sachgerecht und belegbar?

## Output

Obliegenheitsmatrix mit Beweislast, Verschuldensgrad, Kausalität, Quote und Schriftsatzbaustein.

## Red Flags

- keine Rechtsfolgenbelehrung
- Obliegenheit erst nach Schaden erfunden
- Kausalität pauschal behauptet
- Quote ohne Tatsachenbasis

## Anschluss-Skills

- vers-deckungsablehnung-redteam
- vergleich-abfindung-entschaedigungsquittung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
