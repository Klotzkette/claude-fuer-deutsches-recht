---
name: elastizitaeten-diversion-ratios
description: "Oekonomischer Gutachter oder Mandant legt Elastizitaetsdaten oder Diversion-Ratio-Analyse vor und Belastbarkeit ist zu prüfen. Prüft Eigenpreis-Elastizitaet Kreuzpreis-Elastizitaet und Diversion Ratios als Instrumente quantitativer Marktabgrenzung. Normen EU-Bekanntmachung Marktdefinition 2024 SSNIP-Test § 18 GWB Art. 102 AEUV. Prüfraster oekonometrische Methodik Datenbasis Endogenitaet Schwellenwerte Cellophane-Fallacy. Output Methodenbewertungs-Memo mit Staerken Schwaechen und prozessualer Angreifbarkeit. Abgrenzung: ssnip-test-anwendung für den SSNIP-Test selbst."
---

# Elastizitäten und Diversion Ratios

## 1. Eigenpreis-Elastizität

### Definition

\[\varepsilon_{ii} = \frac{\partial Q_i / Q_i}{\partial P_i / P_i}\]

Gibt an, um wie viel Prozent die Nachfrage nach Produkt i sinkt, wenn der Preis von i um ein Prozent steigt.

### Interpretation für Marktdefinition

- Hohe Eigenpreis-Elastizität (Betrag > 2): Starker Wettbewerb — Nachfrager weichen aus.
- Niedrige Eigenpreis-Elastizität (Betrag < 1): Geringe Ausweichmöglichkeiten — mögliche Marktmacht.

## 2. Kreuzpreis-Elastizität

### Definition

\[\varepsilon_{ij} = \frac{\partial Q_i / Q_i}{\partial P_j / P_j}\]

Positiver Wert: Produkte i und j sind Substitute. Negativer Wert: Komplementärgüter.

### Schwellenwerte

In der behördlichen Praxis gilt eine Kreuzpreis-Elastizität von > 0,5 als Indiz für Substituierbarkeit. Strenge wissenschaftliche Anforderungen verlangen Signifikanztest und Robustheitsprüfung.

## 3. Diversion Ratio

### Definition

Die Diversion Ratio D(i→j) gibt an, welcher Anteil der bei Produkt i verlorenen Umsätze zu Produkt j wechselt (bei einer Preiserhöhung für i).

\[D_{i \to j} = \frac{\Delta Q_j}{\Delta Q_i}\]

### Anwendung im SSNIP-Test

Der kritische Verlustanteil bestimmt, ab welcher Abwanderungsquote eine 5-prozentige Preiserhöhung unrentabel ist. Die Diversion Ratio zeigt, wohin die Abwanderung erfolgt — das wichtigste Substitut.

### Merger Simulation

Diversion Ratios sind Kerngröße der Merger Simulation (Upward Pricing Pressure — UPP):
- Hohes D(i→j): Fusion von i und j beseitigt starken Wettbewerbsdruck.
- Gering: Kein wesentlicher Verlust an Wettbewerb durch Fusion.

## 4. Methodische Anforderungen

### Datenbasis

- Paneldaten (zeitliche Variation in Preisen und Mengen).
- Querschnittsdaten (regionale Variation) als Alternative.
- Mindestbeobachtungszeitraum: typisch 3–5 Jahre.

### Endogenitätsproblem

Preise und Mengen werden gleichzeitig bestimmt → OLS-Schätzung verzerrt. Lösung: Instrumentvariablen (z.B. Kostengrößen als Instrument für Preise).

### Robustheitsprüfungen

- Alternative Spezifikationen testen.
- Ausreißer identifizieren (Sonderpreisperioden, Promotional Pricing herausnehmen).
- Ergebnisstabilität bei unterschiedlichen Stichproben.

## 5. Prüfprotokoll

```
Methode: [OLS / IV / BLP / andere]
Datenzeitraum: [von ... bis ...]
Endogenitätskorrektur: [ja / nein / fehlend]
Kreuzpreiselastizität i→j: [Wert]
Diversion Ratio i→j: [Wert]
Signifikanz: [p < 0,05 / nicht signifikant]
Schwächen: [...]
Bewertung: [belastbar / eingeschränkt belastbar / nicht belastbar]
```

## Leitentscheidungen Elastizitaeten / Diversion Ratios

- EK, Horizontal Merger Guidelines 2004 Rn. 22-29 — Diversion Ratios als Evidenz fuer Marktabgrenzung; hohe Diversion zwischen Produkten A und B indiziert gemeinsamen Markt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.