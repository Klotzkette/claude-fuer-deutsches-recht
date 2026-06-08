---
name: quellen-livecheck
description: "Quellen-Live-Check für Fortbestehensprognose StaRUG/InsO: prüft Normen (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §§ 1/14/49, IDW S 11) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fortbestehensprognose** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (InsO, StaRUG, § 19 Abs) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fortbestehensprognose (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
