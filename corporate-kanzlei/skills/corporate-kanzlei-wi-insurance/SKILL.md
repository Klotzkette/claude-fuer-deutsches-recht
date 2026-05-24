---
name: corporate-kanzlei-wi-insurance
description: "W&I-Versicherung: Bereitet W&I-Prozess, Underwriting, DD-Berichte, AI-DD-Transparenz und Deckungsausschluesse vor."
---

# W&I-Versicherung

## Zweck

Bereitet W&I-Prozess, Underwriting, DD-Berichte, AI-DD-Transparenz und Deckungsausschlüsse vor.

## Arbeitsmodus

- Versicherbare Garantien und bekannte Risiken aus DD ableiten.
- Underwriting Pack strukturieren.
- KI-Anteile in der DD transparent machen: Tool, Scope, Stichprobe, menschliche Validierung.
- Underwriting Call vorbereiten.

## Rote Schwellen

- Nicht validierte KI-DD wird als voll geprüft dargestellt.
- Bekanntes Risiko nicht offengelegt.
- Deckungsausschluss nicht in SPA/W&I abgestimmt.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `corporate-kanzlei-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/wi-underwriting-pack.md
- assets/templates/wi-ai-dd-disclosure-log.md
