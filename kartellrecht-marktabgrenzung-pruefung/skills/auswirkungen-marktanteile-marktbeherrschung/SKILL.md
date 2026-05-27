---
name: auswirkungen-marktanteile-marktbeherrschung
description: "Wie aendert sich der Marktanteil des Mandanten je nachdem wie eng oder weit der Markt abgegrenzt wird. Quantifiziert Auswirkungen alternativer Marktabgrenzungen auf Marktanteile und Marktbeherrschungsvermutungen. Normen § 18 Abs. 4 GWB 40-Prozent-Einzelmarktbeherrschungs-Vermutung § 18 Abs. 6 GWB gemeinsame Beherrschung Art. 102 AEUV. Pruefraster Marktanteilsberechnung je Marktdefinition rechtliche Konsequenzen Untersagung Missbrauch Zulassung. Output Sensitivitaets-Tabelle Marktanteil pro Szenario mit Ampelbewertung. Abgrenzung: gesamtbewertung-tragfaehigkeit fuer das Gesamturteil."
---

# Auswirkungen auf Marktanteile und Marktbeherrschung

## Zweck

Die Wahl der Marktdefinition ist selten neutral: Sie bestimmt, welcher Marktanteil ausgewiesen wird, und damit, ob Marktbeherrschungsvermutungen greifen oder Eingriffsschwellen überschritten werden. Dieser Skill macht diese Auswirkungen sichtbar und quantifiziert sie.

## Grundstruktur der Analyse

### 1. Marktanteilsmatrix

| Marktdefinition | Marktgröße (Umsatz/Menge) | Marktanteil des geprüften Unternehmens |
|----------------|--------------------------|----------------------------------------|
| Vorgelegte Abgrenzung | [Wert] | [X%] |
| Engere Alternative | [Wert] | [Y%] |
| Weitere Alternative | [Wert] | [Z%] |

### 2. Rechtliche Konsequenzen je Marktanteilsband

| Marktanteil | Rechtliche Folge | Rechtsgrundlage |
|-------------|-----------------|----------------|
| < 25% | Keine FKVO-Bedenken bei Fusion | EU-Fusionsleitlinien 2004 |
| < 30% | GVO-Freistellung Vertikales (je Partei) | VO 2022/720 |
| 40% | Marktbeherrschungsvermutung Deutschland | § 18 Abs. 4 GWB |
| 50% | AKZO-Vermutung Marktmacht | EuGH Rs. C-62/86 |
| > 50% (kumuliert 3 Unternehmen) | Oligopol-Vermutung | § 18 Abs. 6 Nr. 1 GWB |
| > 66⅔% (kumuliert 5 Unternehmen) | Oligopol-Vermutung | § 18 Abs. 6 Nr. 2 GWB |

### 3. Szenario-Analyse Fusionskontrolle

HHI-Berechnung (Herfindahl-Hirschman-Index):
```
HHI = Summe der quadrierten Marktanteile aller Marktteilnehmer
Delta HHI = HHI nach Fusion - HHI vor Fusion
```

Richtwerte EU-Praxis:
- Delta HHI < 150: In der Regel keine Bedenken.
- Delta HHI > 150 und HHI > 1000: Vertiefte Prüfung.
- Delta HHI > 250 und HHI > 2000: Starke Bedenken.

Auswirkung alternativer Marktdefinition:
```
HHI (vorgelegte Abgrenzung): [Wert]
HHI (enge Alternative): [Wert]
HHI (weite Alternative): [Wert]
```

### 4. Szenario-Analyse Missbrauchsverfahren

- Marktanteil > 40%: Prüfung Marktbeherrschung obligatorisch.
- Marktanteil 40–50%: Weitere Faktoren entscheidend.
- Marktanteil > 50%: Marktbeherrschung sehr wahrscheinlich.
- Marktanteil < 40%: Marktbeherrschung unwahrscheinlich (aber nicht ausgeschlossen, z.B. bei Datenzugang).

### 5. Schaltereffekte

Identifizierung der „kritischen Grenze": Bei welchem Marktanteil kippt das rechtliche Ergebnis?

```
Kritische Grenze: [40% / 50% / GVO-Schwelle / andere]
Marktanteil bei vorgelegter Abgrenzung: [X%]
Differenz zur kritischen Grenze: [± Z Prozentpunkte]
Robustheit: [stabil / sensitiv gegenüber Marktdefinition]
```

## Fazit

Marktdefinitionsabhängigkeit des Ergebnisses: **gering (< 5 Prozentpunkte Unterschied) / mittel / hoch (> 15 Prozentpunkte)**

## Leitentscheidungen Marktanteile / Marktbeherrschung

- EuGH, Urt. v. 13.02.1979 — Rs. 85/76 (Hoffmann-La Roche), Slg. 1979, 461 — Marktanteil als primaerer Indikator Marktbeherrschung; Stabilitaet des Marktanteils ueber Zeit als Verstaerker.
- BGH, Beschl. v. 07.11.2023 — KZR 67/21, WuW 2024, 90 — Widerlegung Marktbeherrschungsvermutung; trotz 40 Prozent Marktanteil wesentlicher Wettbewerb nachweisbar; Gesamtwuerdigung aller Faktoren.
- BKartA, Beschl. v. 01.02.2022 — B6-22/21 (Facebook/Meta) — Ueberragende Marktstellung § 18 Abs. 3a GWB; Marktanteil plus Netzwerkeffekte plus Datenzugang kumulativ.

## Kommentarliteratur

- Bechtold/Bosch GWB § 18 Rn. 40-70 (Vermutungsregel, Faktoren, Marktanteil)
