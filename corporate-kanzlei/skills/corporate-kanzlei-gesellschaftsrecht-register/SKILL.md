---
name: corporate-kanzlei-gesellschaftsrecht-register
description: "Corporate Housekeeping und Register: Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschluesse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals."
---

# Corporate Housekeeping und Register

## Zweck

Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals.

## Arbeitsmodus

- Registerdaten mit Datenraum und SPA-Angaben abgleichen.
- Vertretungsmacht, Satzung, Gesellschafterliste und Beschlusslage prüfen.
- Fehlende Handelsregisterabrufe als To-do ausgeben.
- Closing Deliverables ableiten.

## Rote Schwellen

- Vertretungsmacht ungeprüft.
- Gesellschafterliste veraltet.
- Transparenzregister/UBO offen.

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

- assets/templates/handelsregister-corporate-housekeeping.md
- assets/templates/closing-deliverables-register.md
