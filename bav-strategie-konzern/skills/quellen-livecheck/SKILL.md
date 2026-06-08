---
name: quellen-livecheck
description: "Quellen-Live-Check für Betriebliche Altersversorgung im Konzern: prüft Normen (BetrAVG, § 1 BetrAVG Zusage, § 16 BetrAVG Anpassung) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BaFin (PSV) und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Bav Strategie Konzern** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `altersversorgung-boutique-fristennotiz-psv` — Altersversorgung Boutique Fristennotiz PSV
- `bav-cta-treuhand-spezial` — BAV CTA Treuhand Spezial
- `bav-erstattung-fuenftelregelung` — BAV Erstattung Fuenftelregelung
- `bav-grenzueberschreitend-mobil-spezial` — BAV Grenzueberschreitend Mobil Spezial
- `bav-konzern-design-workflow` — BAV Konzern Design Workflow
- `bav-pensionsfond-rueckdeckung-spezial` — BAV Pensionsfond Rueckdeckung Spezial
- `benefits-mandantenkommunikation-entscheidungsvorlage` — Benefits Mandantenkommunikation Entscheidungsvorlage
- `betrieblichen-drei-duesseldorfer-sonderfall` — Betrieblichen Drei Duesseldorfer Sonderfall
- `boutique-fristennotiz-und-naechster-schritt` — Boutique Fristennotiz und Naechster Schritt
- `buyout-ma-country-by-cta-contractual` — Buyout MA Country BY CTA Contractual
- `buyouts-quellenkarte` — Buyouts Quellenkarte
- `country-by-country-benefits-matrix-konzern` — Country BY Country Benefits Matrix Konzern
- `cta-contractual-trust-arrangement-strukturierung` — CTA Contractual Trust Arrangement Strukturierung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Bav Strategie Konzern (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
