---
name: corporate-kanzlei-spa-apa-entwurf
description: "SPA/APA-Entwurf: Erstellt und strukturiert Kaufvertragsentwuerfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur."
---

# SPA/APA-Entwurf

## Zweck

Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur.

## Arbeitsmodus

- Deal-Struktur in Vertragstopologie übersetzen.
- Garantien, Covenants, Closing Conditions, Kaufpreismechanik, Haftung und Tax-Klauseln vorstrukturieren.
- DD-Findings in spezifische Schutzmechanismen überführen.
- Offene Rechts- und Business-Entscheidungen als Key Issues ausgeben.

## Rote Schwellen

- Kaufpreismechanik unklar.
- DD-Finding ohne vertragliche Konsequenz.
- Haftungsregime oder W&I-Setup offen.

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

- assets/templates/spa-apa-term-sheet-map.md
- assets/templates/spa-draft-outline.md
