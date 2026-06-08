---
name: quellen-livecheck
description: "Quellen-Live-Check für Datenschutzrecht DSGVO/BDSG: prüft Normen (DSGVO Art. 5/6/13/15/28/32/33/35, BDSG, TTDSG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BfDI Bund und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Datenschutzrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `anschluss` — Anschluss
- `anwendungsfall-triage` — Anwendungsfall Triage
- `art-9-besondere-kategorien` — ART 9 Besondere Kategorien
- `art-besondere-aufnahme-statusinformation` — ART Besondere Aufnahme Statusinformation
- `aufnahme-statusinformation` — Aufnahme Statusinformation
- `auskunft-behoerden-gerichts-registerweg` — Auskunft Behoerden Gerichts Registerweg
- `avv-art-26-joint-controllership-deutsch` — AVV ART 26 Joint Controllership Deutsch
- `avv-art-28-dsgvo-grundtatbestand` — AVV ART 28 DSGVO Grundtatbestand
- `avv-art-28-mindestinhalte-checkliste` — AVV ART 28 Mindestinhalte Checkliste
- `avv-audit-und-kontrollrechte` — AVV Audit und Kontrollrechte
- `avv-cloud-und-subverarbeitung-art-28-iv` — AVV Cloud und Subverarbeitung ART 28 IV
- `avv-eu-kommission-musterklauseln-2021-915` — AVV EU Kommission Musterklauseln 2021 915
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (Art. 15, Art. 33, Art. 44, BDSG, DSGVO, TDDDG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Datenschutzrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
