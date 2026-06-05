---
name: direktanspruch-pflichtversicherung-eiopa
description: "Direktanspruch Pflichtversicherung Eiopa: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Direktanspruch Pflichtversicherung Eiopa

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Direktanspruch Pflichtversicherung Eiopa** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `direktanspruch-pflichtversicherung-115-vvg` | Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen. |
| `eiopa-grenzueberschreitender-vertrieb` | Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten. |
| `gewerbe-betriebsschliessung-infektionsschutz` | Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Direktanspruch Pflichtversicherung Eiopa**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `direktanspruch-pflichtversicherung-115-vvg`

**Fokus:** Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen.

# Direktanspruch in Pflichtversicherung § 115 VVG

## Einsatz

Für Geschädigte, die nicht nur den Schädiger, sondern direkt den Versicherer in Anspruch nehmen wollen.

## Norm- und Quellenanker

VVG § 115; PflVG; Pflichtversicherungsnormen je Berufsgruppe; BGB Delikt/Vertrag; ZPO.

## Arbeitsfragen

1. Welche Pflichtversicherung eröffnet § 115 VVG?
2. Welche Einwendungen kann der Versicherer dem Geschädigten entgegenhalten?
3. Welche Deckungssumme und Selbstbehalt gelten?
4. Welche Parteien müssen verklagt oder beteiligt werden?

## Output

Direktanspruchsprüfung, Anspruchsschreiben, Klageparteienmatrix und Deckungssummencheck.

## Red Flags

- freiwillige Haftpflicht als Pflichtversicherung behandelt
- Selbstbehalt gegen Geschädigten falsch angewandt
- Schädiger insolvent
- Berufshaftpflichtnorm nicht identifiziert

## Anschluss-Skills

- betriebshaftpflicht-versicherungsfall-serienschaden
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `eiopa-grenzueberschreitender-vertrieb`

**Fokus:** Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten.

# EIOPA und grenzüberschreitender Versicherungsvertrieb

## Einsatz

Für internationale Policen, InsurTechs, EU-Vermittler und deutsche Kunden ausländischer Versicherer.

## Norm- und Quellenanker

VAG; IDD; Solvency II; EIOPA-Veröffentlichungen live prüfen; Rom-I/Brüssel-Ia bei Vertrag und Gerichtsstand.

## Arbeitsfragen

1. Wer ist Home-State-Aufsicht, wer Host-State?
2. Welche Vertriebsform und Kundengruppe?
3. Welche Pflichtinformationen in welcher Sprache?
4. Welches Gericht/Recht ist für Individualstreit zuständig?

## Output

EU-Vertriebscheck, Aufsichtslandkarte, Beschwerdeweg und Vertragsrechtsnotiz.

## Red Flags

- ausländische Aufsicht als BaFin-Ersatz missverstanden
- Gerichtsstandsklausel gegenüber Verbrauchern unwirksam
- Pflichtinformationen nur englisch
- Passporting nicht geprüft

## Anschluss-Skills

- vag-bafin-aufsicht-beschwerde-missstand
- deckungsprozess-zustaendigkeit-215-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `gewerbe-betriebsschliessung-infektionsschutz`

**Fokus:** Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich.

# Betriebsschließungsversicherung und Infektionsschutz

## Einsatz

Für Gewerbebetriebe nach behördlichen Eingriffen oder hygienerechtlichen Betriebsschließungen.

## Norm- und Quellenanker

VVG §§ 1, 14, 28; AVB Betriebsschließung; IfSG als Sachrecht; BGB AGB-Kontrolle.

## Arbeitsfragen

1. Welche Behörde ordnete was genau an?
2. Verweist die AVB statisch oder dynamisch auf IfSG-Listen?
3. Lag vollständige oder teilweise Betriebsschließung vor?
4. Wie berechnet sich der versicherte Schaden?

## Output

Deckungsmemo, AVB-Auslegung, Schadensberechnung und Vergleichsvorschlag.

## Red Flags

- Allgemeinverfügung und Einzelverfügung verwechselt
- Umsatzausfall ohne Kostenersparnis
- Klauseltransparenz nicht geprüft
- Vergleich ohne Nachberechnung

## Anschluss-Skills

- betriebsunterbrechung-sachschaden-trigger
- deckungsprozess-zustaendigkeit-215-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
