---
name: auswirkungen-marktanteile-marktbeherrschung
description: "Wie aendert sich der Marktanteil des Mandanten je nachdem wie eng oder weit der Markt abgegrenzt wird. Quantifiziert Auswirkungen alternativer Marktabgrenzungen auf Marktanteile und Marktbeherrschungsvermutungen. Normen § 18 Abs. 4 GWB 40-Prozent-Einzelmarktbeherrschungs-Vermutung § 18 Abs. 6 GWB gemeinsame Beherrschung Art. 102 AEUV. Prüfraster Marktanteilsberechnung je Marktdefinition rechtliche Konsequenzen Untersagung Missbrauch Zulassung. Output Sensitivitaets-Tabelle Marktanteil pro Szenario mit Ampelbewertung. Abgrenzung: gesamtbewertung-tragfähigkeit für das Gesamturteil."
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
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
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

Identifizierung der "kritischen Grenze": Bei welchem Marktanteil kippt das rechtliche Ergebnis?

```
Kritische Grenze: [40% / 50% / GVO-Schwelle / andere]
Marktanteil bei vorgelegter Abgrenzung: [X%]
Differenz zur kritischen Grenze: [± Z Prozentpunkte]
Robustheit: [stabil / sensitiv gegenüber Marktdefinition]
```

## Fazit

Marktdefinitionsabhängigkeit des Ergebnisses: **gering (< 5 Prozentpunkte Unterschied) / mittel / hoch (> 15 Prozentpunkte)**

## Leitentscheidungen Marktanteile / Marktbeherrschung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BKartA, Beschl. v. 01.02.2022 — B6-22/21 (Facebook/Meta) — Ueberragende Marktstellung § 18 Abs. 3a GWB; Marktanteil plus Netzwerkeffekte plus Datenzugang kumulativ.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.