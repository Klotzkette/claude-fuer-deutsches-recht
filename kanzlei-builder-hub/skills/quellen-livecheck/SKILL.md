---
name: quellen-livecheck
description: "Quellen-Live-Check für Kanzlei-Builder-Hub (Plugins/Skills): prüft Normen (BRAO § 43e KI-Einsatz, DSGVO, KI-VO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt RAK und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Kanzlei Builder Hub** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `automatischer-aktualisierer` — Automatischer Aktualisierer
- `builder-zahlen-schwellen-und-berechnung` — Builder Zahlen Schwellen und Berechnung
- `community-leistungsmatrix-fristennotiz` — Community Leistungsmatrix Fristennotiz
- `daten-red-team-und-qualitaetskontrolle` — Daten RED Team und Qualitaetskontrolle
- `deaktivieren` — Deaktivieren
- `deinstallieren` — Deinstallieren
- `deployment-eigenen-einsteiger` — Deployment Eigenen Einsteiger
- `eigenen-formular-portal-und-einreichung` — Eigenen Formular Portal und Einreichung
- `einsteiger-mandantenkommunikation-entscheidungsvorlage` — Einsteiger Mandantenkommunikation Entscheidungsvorlage
- `findet-gate-installiert` — Findet Gate Installiert
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Kanzlei Builder Hub (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
