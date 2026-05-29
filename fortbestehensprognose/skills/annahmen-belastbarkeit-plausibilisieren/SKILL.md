---
name: annahmen-belastbarkeit-plausibilisieren
description: "Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Personal) und Risikokategorisierung. Plausibilitaetsband für jede Annahme. Erzeugt Plausibilitaetsprotokoll. Annahmen mit niedriger Belastbarkeit werden als Modellannahme markiert und im Sensitivitaetsszenario gegengerechnet."
---

# Annahmen plausibilisieren

## Prüfraster pro Annahme

### 1. Vergangenheits-Vergleich

- Stimmt die Annahme mit den **letzten drei Jahren** der BWA / SuSa / Jahresabschluss überein?
- Bei Abweichung: ist die Veränderung **konkret begründet** (neuer Kunde Standortschliessung Tariferhöhung)?
- Bei stark abweichender Optimismus-Annahme **ohne neuen Anlass**: Reduktion auf historisches Niveau im Plausi-Szenario.

### 2. Markt- und Branchenentwicklung

- **Branchenindex** vorhanden? (z. B. ifo Geschäftsklimaindex DESTATIS Branchenkennzahlen).
- **Auftragsbestand der Branche** rückschau.
- **Makro-Indikatoren** Konjunktur Zinsen Energiepreise.

### 3. Interne Konsistenz

- Umsatz steigt, aber Materialkosten bleiben gleich? Konsistenz prüfen.
- Personalkosten steigen, aber Personalstand sinkt? Begründung erforderlich (Tariferhöhung + Reduzierung gleichzeitig).
- Working Capital verbessert sich rapide? Begründung notwendig.

### 4. Belegbarkeit der Maßnahmen

- Sanierungsmaßnahmen mit Effekt — ist der Effekt **belegt** (Vergleichswerte historisch Kostenrechnung)?
- Zeitplan realistisch (z. B. Standortschliessung in 60 Tagen)?
- Einmalkosten realistisch erfasst?

### 5. Drittvereinbarungen

- Patronatserklärungen / Comfortletter: bereits unterzeichnet oder nur in Verhandlung?
- Gesellschafterdarlehen mit Rangrücktritt: notarielle Urkunde vorhanden?
- Bankenzusage: schriftlich oder mundlich?

## Plausibilitätsband pro Annahme

```yaml
plausibilisierung:
  - annahme-id: umsatz-hauptsegment
    band: realistisch  # konservativ / realistisch / ambitioniert / nicht-belastbar
    begruendung: |
      Auftragsbestand bis 09/2026 belegt; ab 10/2026 Modellfortschreibung
      auf Basis Vorjahr +3%
    risiko: mittel
    sensitivitaet-szenario:
      negativ: 10% Umsatzrückgang ab 10/2026
      effekt-eur: -190000 (kumuliert)
      
  - annahme-id: kostensenkung-standort
    band: ambitioniert
    begruendung: |
      Kündigung Standortmietvertrag erfordert 9-Monats-Kündigungsfrist;
      Schliessung bis 08/2026 nur möglich wenn Mieter Aufhebung akzeptiert.
      Aktuell in Verhandlung — nicht belegt.
    risiko: hoch
    sensitivitaet-szenario:
      negativ: Schliessung gelingt nicht im Planhorizont
      effekt-eur: 50000 monatliche Mehrkosten

  - annahme-id: bankenzusage-erhöhung-kreditlinie
    band: nicht-belastbar
    begruendung: |
      Verhandlung mit Bank laeuft. Bisher keine schriftliche Zusage.
      Bank verweist auf laufendes Rating-Verfahren.
    risiko: hoch
    sensitivitaet-szenario:
      negativ: Kreditlinie wird nicht erhöht
      effekt-eur: keine zusätzliche Liquidität 80000 EUR
```

## Konservativer Maßstab

Eine Fortbestehensprognose ist nicht der Ort für Optimismus. **IDW S 11** und **BGH-Rspr.** verlangen einen vorsichtigen objektiven Maßstab.

- Bei Zweifeln: **konservative** Annahmen wählen.
- Wenn eine Annahme **ambitioniert** oder **nicht-belastbar** ist und entscheidend für das Prognoseergebnis ist: das Ergebnis ist **nicht verwertbar** als positive Fortbestehensprognose. Maßnahme: entweder Belegbarkeit nachholen oder Annahme entfernen.

## Sensitivitätsszenarien

```yaml
szenarien:
  basisszenario:
    annahmen: alle wie in annahmen.yaml
    ergebnis-12-monate-liquiditaet: positiv
    bemerkung: Plan-Szenario
    
  negativ-szenario:
    annahmen: alle ambitioniert-Annahmen reduziert auf konservativ
    ergebnis-12-monate-liquiditaet: knapp positiv  # vor Maßnahmen
    bemerkung: Risiko-Szenario; bei Eintritt sind Zusatzmaßnahmen erforderlich
    
  stress-szenario:
    annahmen: zusätzlich Wegfall Top-Kunde
    ergebnis-12-monate-liquiditaet: negativ
    bemerkung: Reines Stress-Szenario; in der Plausibilisierung
      als unwahrscheinlich eingeschaetzt
```

## Sonderfälle

### Stille Reserven die zur Plausibilisierung herangezogen werden

Wenn der Status stille Reserven enthält (Skill `bilanzieller-status-aufnehmen`) muss die Liquidität auch realistisch über Verkauf erzielbar sein:

- Verkehrswert-Gutachten vorhanden?
- Realistisch verkaufbar im Planhorizont?
- Auswirkung auf den Betrieb (z. B. Verkauf einer Maschine führt zu Produktionsausfall)?

### Comfortletter

- **Weicher Comfortletter** (Best Effort) ist im Status **nicht** zu berücksichtigen.
- **Harte externe Patronatserklärung** mit Forderungsverzicht im Insolvenzfall ist berücksichtigungsfähig — siehe Skill `patronatserklaerung-extern-hart-erzeugen`.

## Ausgabe

- `plausibilisierung.md` mit jeder Annahme bewertet (Band Risiko Sensitivitaet).
- Drei Szenarien (Basis Negativ Stress) mit Endergebnis.
- Empfehlung: bei mehr als zwei nicht-belastbaren oder ambitionierten Annahmen die das Ergebnis tragen ist die Prognose **nicht positiv** zu werten.
- Liste konkreter Maßnahmen zur Verbesserung der Belastbarkeit (Belegnachholung Verhandlungsabschluss Drittvereinbarung).


## Aktuelle Leitentscheidungen — Annahmen-Plausibilitaet

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Annahmen-Plausibilitaet

§ 19 Abs. 2 InsO (Fortbestehensprognose) → § 15b InsO (Haftung bei fehlerhafter Prognose) → IDW S 11 Rn. 45 ff. (Annahmen-Qualitaet) → IDW S 6 Rn. 90 ff. (Plausibilitaetspruefung Sanierungskonzept)

## Triage — Annahmen-Check

Bevor losgelegt wird, klaere:

1. **Konsistenz-Test:** Passt Umsatzwachstum zu Personalkosten und Material? (Umsatz +10% ohne Personal-Aufstockung bei Vollauslastung → inkonsistent)
2. **Vergangenheits-Abgleich:** Welche Wachstumsraten wurden in den letzten 3 Jahren tatsaechlich erreicht? Neue Annahmen muessen daraus ableitbar sein.
3. **Sensitivity-Test:** Welche Annahme ist am kritischsten? Was passiert wenn Haupt-Kunden 20% weniger abnimmt?
4. **Worst-Case-Szenario:** Prognose auch bei pessimistischsten Annahmen noch positiv?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.