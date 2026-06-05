---
name: versicherungsprodukt-agb-betriebshaftpflicht
description: "Versicherungsprodukt AGB Betriebshaftpflicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versicherungsprodukt AGB Betriebshaftpflicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versicherungsprodukt AGB Betriebshaftpflicht** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versicherungsprodukt-agb-klauselkontrolle` | AVB-Klauseln nach Transparenz, Überraschung, unangemessener Benachteiligung und VVG-Leitbild prüfen. |
| `betriebshaftpflicht-versicherungsfall-serienschaden` | Betriebshaftpflichtversicherung: Personen-/Sachschaden, Vermögensfolgeschaden, Serienschadenklausel, Nachhaftung, Ausschlüsse und Abwehrdeckung. |
| `betriebsunterbrechung-sachschaden-trigger` | Betriebsunterbrechungsversicherung: versicherter Sachschaden als Trigger, Unterbrechungsschaden, Mehrkosten, Unterversicherung, Kausalität und Zeitraum. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Versicherungsprodukt AGB Betriebshaftpflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versicherungsprodukt-agb-klauselkontrolle`

**Fokus:** AVB-Klauseln nach Transparenz, Überraschung, unangemessener Benachteiligung und VVG-Leitbild prüfen.

# Versicherungsbedingungen als AGB prüfen

## Einsatz

Für Klauselstreit und Produktentwicklung, wenn AVB unklar oder unwirksam sein könnten.

## Norm- und Quellenanker

BGB §§ 305–310; VVG; UKlaG; UWG; ZPO.

## Arbeitsfragen

1. Welche Klausel ist streitig?
2. Welches gesetzliche Leitbild wird verschoben?
3. Ist die Klausel transparent und systematisch platziert?

## Output

AGB-Prüfvermerk und Klausel-Redline.

## Red Flags

- Ausschluss versteckt
- Definition und Ausschluss widersprechen sich
- Verbraucher/B2B nicht getrennt

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `betriebshaftpflicht-versicherungsfall-serienschaden`

**Fokus:** Betriebshaftpflichtversicherung: Personen-/Sachschaden, Vermögensfolgeschaden, Serienschadenklausel, Nachhaftung, Ausschlüsse und Abwehrdeckung.

# Betriebshaftpflicht: Versicherungsfall und Serienschaden

## Einsatz

Der Skill prüft, ob der Haftpflichtversicherer abwehren, freistellen oder regulieren muss.

## Norm- und Quellenanker

VVG §§ 100–124; AVB/BHV; BGB Delikt/Vertrag; ZPO Streitverkündung.

## Arbeitsfragen

1. Welcher Haftungsvorwurf wird erhoben und wann trat der Schaden ein?
2. Ist Abwehrdeckung oder Befriedigungsdeckung im Streit?
3. Gilt eine Serienschaden- oder Erfüllungsausschlussklausel?
4. Welche Drittbeteiligten müssen eingebunden werden?

## Output

Deckungs- und Haftungsmatrix, Streitverkündungscheck, Versichereranzeige und Vergleichsstrategie.

## Red Flags

- Erfüllungsschaden als Haftpflichtschaden deklariert
- Serienschadenzeitpunkt falsch
- Abwehrdeckung unterschätzt
- Selbstregulierung ohne Zustimmung

## Anschluss-Skills

- produkthaftpflicht-rueckrufkosten
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `betriebsunterbrechung-sachschaden-trigger`

**Fokus:** Betriebsunterbrechungsversicherung: versicherter Sachschaden als Trigger, Unterbrechungsschaden, Mehrkosten, Unterversicherung, Kausalität und Zeitraum.

# Betriebsunterbrechung: Sachschaden-Trigger

## Einsatz

Der Skill prüft, ob Umsatzausfall versichert ist oder nur wirtschaftlicher Reflex ohne Sachschaden.

## Norm- und Quellenanker

VVG Schadenversicherung; FBUB/AMBUB/AVB; BGB; HGB Rechnungslegung als Schadensbasis.

## Arbeitsfragen

1. Welcher versicherte Sachschaden trat ein?
2. Wie lange dauerte technische und kaufmännische Unterbrechung?
3. Welche Fixkosten, Mehrkosten und Ersparnisse sind zu berücksichtigen?
4. Welche Summen-/Haftzeitgrenzen gelten?

## Output

BU-Schadensmodell, Belegliste für Buchhaltung, Kausalitätsmemo und Abschlagsforderung.

## Red Flags

- reiner Nachfrageausfall ohne Sachschaden
- Haftzeit überschritten
- BWA ungeordnet
- Mehrkosten nicht belegt

## Anschluss-Skills

- vvg-falligkeit-14-abschlagszahlung
- elementarschaden-starkregen-ueberschwemmung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
