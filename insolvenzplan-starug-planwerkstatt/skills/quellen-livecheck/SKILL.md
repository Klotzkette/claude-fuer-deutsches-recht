---
name: quellen-livecheck
description: "Quellen-Live-Check für Insolvenzplan / StaRUG: prüft Normen (§§ 217-269 InsO Insolvenzplan, StaRUG §§ 4-71 Restrukturierungsplan) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Insolvenzplan Starug Planwerkstatt** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `abstimmung-mehrheiten-anlagenpaket` — Abstimmung Mehrheiten Anlagenpaket
- `anlagen-mehrparteien-konflikt-und-interessen` — Anlagen Mehrparteien Konflikt und Interessen
- `anlagenpaket` — Anlagenpaket
- `asset-deals-im-plan-grundstuecke-marken-kundendaten` — Asset Deals im Plan Grundstuecke Marken Kundendaten
- `cram-formular-portal-und-einreichung` — Cram Formular Portal und Einreichung
- `cramdown-obstruktion-datenraum-register` — Cramdown Obstruktion Datenraum Register
- `darstellender-quellenkarte` — Darstellender Quellenkarte
- `darstellender-teil` — Darstellender Teil
- `datenraum-register` — Datenraum Register
- `down-red-gestaltender-gruppen` — Down RED Gestaltender Gruppen
- `gerichtliche-schritte-kommandocenter` — Gerichtliche Schritte Kommandocenter
- `gestaltender-teil` — Gestaltender Teil
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (StaRUG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Insolvenzplan Starug Planwerkstatt (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
