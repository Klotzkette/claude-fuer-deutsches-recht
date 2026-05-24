---
name: mittelstand-corporate-ma-datenqualitaet-xai-qualitaetskontrolle
description: "Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestuetzte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab."
---

# Datenqualität und XAI-Qualitätskontrolle

## Zweck

Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab.

## Arbeitsmodus

- Datenqualität, Quellenstatus, Stichprobe und Plausibilisierung festhalten.
- Explainability-Anforderungen für jedes Ergebnis markieren.
- Human-in-the-loop und Senior Review dokumentieren.
- Fehler, Annahmen und nicht geprüfte Bereiche offenlegen.

## Rote Schwellen

- Keine Belegkette.
- Nicht erklärbares Ergebnis bei hohem Risiko.
- Bias oder Datenlücke wird nicht benannt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/data-quality-gate.md
- assets/templates/xai-quality-control-log.md
