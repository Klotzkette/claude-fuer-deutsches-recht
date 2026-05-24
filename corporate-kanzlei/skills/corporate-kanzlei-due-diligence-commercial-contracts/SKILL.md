---
name: corporate-kanzlei-due-diligence-commercial-contracts
description: "Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Haendler-, SaaS-, Lizenz- und Materialvertraege auf Change of Control, Kündigung, Exklusivitaet, Haftung, IP und Preisrisiken."
---

# Kommerzielle Vertrags-DD

## Zweck

Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und Preisrisiken.

## Arbeitsmodus

- Vertragstypen clustern.
- Prüfmatrix je Vertragstyp anwenden.
- Ungewoehnliche Klauseln und Abweichungen vom Standard hervorheben.
- Disclosure Schedules und SPA-Schutz ableiten.

## Rote Schwellen

- Change-of-Control-Frage offen.
- Top-Kunde/Lieferant nicht erfasst.
- Vertragsanlage fehlt.

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

- assets/templates/commercial-contract-review-grid.md
- assets/templates/disclosure-schedules-matrix.md
