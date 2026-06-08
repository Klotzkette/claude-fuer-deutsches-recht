---
name: quellen-livecheck
description: "Quellen-Live-Check für KI-Governance: prüft Normen (KI-VO EU 2024/1689, DSGVO, Produkthaftung) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt KI-Aufsichtsbehörde national und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Ki Governance** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anbieter-mehrparteien-konflikt-und-interessen` — Anbieter Mehrparteien Konflikt und Interessen
- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `anwendungsfall-triage` — Anwendungsfall Triage
- `case-dpia-drift` — Case Dpia Drift
- `dpia-risikoampel-und-gegenargumente` — Dpia Risikoampel und Gegenargumente
- `drift-verhandlung-vergleich-und-eskalation` — Drift Verhandlung Vergleich und Eskalation
- `dsgvo-governance-inventar` — DSGVO Governance Inventar
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `governance-compliance-dokumentation-und-akte` — Governance Compliance Dokumentation und Akte
- `gpai-modelle-ki-anbieter-arbeitsrecht` — Gpai Modelle KI Anbieter Arbeitsrecht
- `inventar-dokumentenmatrix-und-lueckenliste` — Inventar Dokumentenmatrix und Lueckenliste
- `inventar-kontrollen-konformitaetsbewertung` — Inventar Kontrollen Konformitaetsbewertung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (DSGVO) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Ki Governance (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
