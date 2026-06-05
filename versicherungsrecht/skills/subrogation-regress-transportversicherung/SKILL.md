---
name: subrogation-regress-transportversicherung
description: "Subrogation Regress Transportversicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Subrogation Regress Transportversicherung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Subrogation Regress Transportversicherung** im Plugin Versicherungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `subrogation-regress-86-vvg` | Legalzession und Regress des Versicherers: Forderungsübergang, Quotenvorrecht, Beweissicherung, Vergleich, Regressabwehr und Verjährung. |
| `transportversicherung-ware-lagerung` | Transportversicherung: Güterschaden, Verlust, Lagerung, Incoterms, multimodaler Transport, Regress gegen Frachtführer und Versicherungswert. |
| `vag-bafin-aufsicht-beschwerde-missstand` | Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbraucherschutz und Grenzen individueller Leistungserzwingung. |

## Arbeitsweg

Im Plugin Versicherungsrecht gilt für **Subrogation Regress Transportversicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `subrogation-regress-86-vvg`

**Fokus:** Legalzession und Regress des Versicherers: Forderungsübergang, Quotenvorrecht, Beweissicherung, Vergleich, Regressabwehr und Verjährung.

# Regress und Legalzession § 86 VVG

## Einsatz

Der Skill klärt, wer nach Regulierung gegen wen vorgehen darf und wie der Versicherungsnehmer seine Restansprüche schützt.

## Norm- und Quellenanker

VVG § 86; BGB Abtretung/Gesamtschuld; SGB X § 116 bei Sozialversicherung; ZPO.

## Arbeitsfragen

1. Welche Forderung ging wann und in welcher Höhe über?
2. Hat der Versicherungsnehmer noch eigene Ansprüche oder Quotenvorrecht?
3. Welche Beweise wurden vor Regulierung gesichert?
4. Droht Regress gegen Versicherungsnehmer oder Dritte?

## Output

Regressmatrix, Legalzessionsvermerk, Vergleichsklauseln und Verjährungskalender.

## Red Flags

- Vergleich vernichtet Regressrechte
- Quotenvorrecht vergessen
- Sozialversicherung und Privatversicherer vermischt
- Drittanspruch verjährt

## Anschluss-Skills

- vvg-mehrfachversicherung-78
- direktanspruch-pflichtversicherung-115-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `transportversicherung-ware-lagerung`

**Fokus:** Transportversicherung: Güterschaden, Verlust, Lagerung, Incoterms, multimodaler Transport, Regress gegen Frachtführer und Versicherungswert.

# Transportversicherung: Ware, Lagerung, Lieferkette

## Einsatz

Der Skill ordnet beschädigte oder verlorene Ware zwischen Verkäufer, Käufer, Spediteur, Lagerhalter und Versicherer.

## Norm- und Quellenanker

VVG Schadenversicherung; HGB Frachtrecht §§ 407 ff.; CMR/See-/Luftfracht je nach Fall; AVB Transport.

## Arbeitsfragen

1. Wann ging Gefahr/Versicherungsinteresse über?
2. Welche Strecke, Lagerung und Beförderungsart sind betroffen?
3. Welche Schadensanzeige- und Untersuchungsfristen laufen?
4. Welche Regressgegner und Haftungsbegrenzungen gibt es?

## Output

Transport-Schadenmatrix, Regressfristen, Dokumentenliste und Versichereranzeige.

## Red Flags

- Incoterms und Versicherungsschutz verwechselt
- Lagerphase nicht gedeckt
- CMR-Fristen übersehen
- Schadensgutachten zu spät

## Anschluss-Skills

- vvg-versicherung-fuer-fremde-43-48
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `vag-bafin-aufsicht-beschwerde-missstand`

**Fokus:** Versicherungsaufsicht nach VAG: BaFin-Beschwerde, Missstandsaufsicht, Produkt-/Vertriebsaufsicht, Solvabilität, Verbraucherschutz und Grenzen individueller Leistungserzwingung.

# VAG/BaFin-Aufsicht: Beschwerde und Missstand

## Einsatz

Der Skill nutzt Aufsicht intelligent, ohne sie mit einem Zivilgericht zu verwechseln.

## Norm- und Quellenanker

VAG; BaFin-Aufsichtsrecht; VVG §§ 214 ff.; EU Solvency II/IDD; VwVfG/VwGO nur falls eigener Verwaltungsakt.

## Arbeitsfragen

1. Geht es um individuelle Leistung, systematischen Missstand oder Vertriebsproblem?
2. Welche Unterlagen braucht die BaFin, welche nicht?
3. Gibt es parallele Ombudsmann-/Klage-/Fristfragen?
4. Welche Antwort der BaFin ist realistisch?

## Output

BaFin-Beschwerde, Erwartungsmanagement, Parallelverfahrensplan und Aufsichtsmemo.

## Red Flags

- BaFin soll Einzelfallzahlung anordnen
- Datenschutz/Geschäftsgeheimnisse unnötig breit eingereicht
- Verjährung parallel unbeachtet
- Beschwerde emotional statt prüfbar

## Anschluss-Skills

- vers-ombudsmann-bafin-beschwerde-klageweg
- idd-vertrieb-beratung-dokumentation

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
