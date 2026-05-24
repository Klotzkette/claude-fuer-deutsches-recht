---
name: corporate-kanzlei-ki-governance-berufsrecht
description: "KI-Governance und Berufsrecht: Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe."
---

# KI-Governance und Berufsrecht

## Zweck

Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe.

## Arbeitsmodus

- Datenklassen und erlaubte Tools erfassen.
- Need-to-know, Pseudonymisierung, AVV/TOMs und Verschwiegenheit dokumentieren.
- Ungeprüfte KI-Outputs und menschliche Validierung trennen.
- Mandantenhinweise und interne Freigaben vorbereiten.

## Rote Schwellen

- Mandatsgeheimnis im offenen Tool.
- Kein Dienstleister-/AVV-Status.
- KI-Output wird ohne Review nach außen gegeben.

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

- assets/templates/ai-use-disclosure-log.md
- assets/templates/confidentiality-need-to-know-log.md
