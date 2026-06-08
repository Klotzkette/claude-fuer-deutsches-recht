---
name: quellen-livecheck
description: "Quellen-Live-Check für Fachanwalt Insolvenz- und Sanierungsrecht: prüft Normen (InsO, StaRUG, InsVV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht (AG) und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Insolvenz Sanierungsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `absonderungsrecht-paragraf-50-inso` — Absonderungsrecht Paragraf 50 Inso
- `anfechtung-vorsatz-paragraf-133-inso-bgh-ix-zr-65-16` — Anfechtung Vorsatz Paragraf 133 Inso BGH IX ZR 65 16
- `eigenverwaltung-schutzschirm-paragraf-270b-inso` — Eigenverwaltung Schutzschirm Paragraf 270b Inso
- `eroeffnung-fachanwalt-fao-glaeubigerantrag` — Eroeffnung Fachanwalt FAO Glaeubigerantrag
- `fa-inso-sanierung-quellen-edge-case` — FA Inso Sanierung Quellen Edge Case
- `fa-schuldschein` — FA Schuldschein
- `glaeubigerantrag-insolvenzanfechtung` — Glaeubigerantrag Insolvenzanfechtung
- `glaeubigerverhandlung-sanierung-idw-s6-krypto` — Glaeubigerverhandlung Sanierung IDW S6 Krypto
- `insanw-eigenverwaltung-konzerninsolvenz` — Insanw Eigenverwaltung Konzerninsolvenz
- `insanw-fortbestehensprognose` — Insanw Fortbestehensprognose
- `insolvenz-insolvenzanfechtung-insolvenzrecht` — Insolvenz Insolvenzanfechtung Insolvenzrecht
- `insolvenzgeld-paragraf-165-sgb-iii` — Insolvenzgeld Paragraf 165 SGB III
- `insolvenzplan-paragraf-217-inso-bgh-ix-zb-66-19` — Insolvenzplan Paragraf 217 Inso BGH IX ZB 66 19
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (InsO, StaRUG, § 14, § 14 InsO, § 15a Gl, §§ 129 ff) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Insolvenz Sanierungsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
