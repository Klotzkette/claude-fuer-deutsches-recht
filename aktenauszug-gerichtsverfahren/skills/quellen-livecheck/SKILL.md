---
name: quellen-livecheck
description: "Quellen-Live-Check für Aktenauszüge zivilgerichtlicher Verfahren: prüft Normen (§ 299 ZPO Akteneinsicht, § 130a ZPO eA-Übermittlung, § 169 GVG Öffentlichkeit) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt AG/LG/OLG und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Aktenauszug Gerichtsverfahren** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `akten-mandantenkommunikation-entscheidungsvorlage` — Akten Mandantenkommunikation Entscheidungsvorlage
- `aktenauszug-erstellen` — Aktenauszug Erstellen
- `aktenauszug-strukturpruefung-akzg-bauleiter` — Aktenauszug Strukturpruefung Akzg Bauleiter
- `aktenauszug-tatbestand-beweis-und-belege` — Aktenauszug Tatbestand Beweis und Belege
- `aktenauszug-verfahrensidentifikation-gericht` — Aktenauszug Verfahrensidentifikation Gericht
- `akzg-aktenauszug-bauleiter` — Akzg Aktenauszug Bauleiter
- `akzg-multiparteienverfahren-konsolidierung-spezial` — Akzg Multiparteienverfahren Konsolidierung Spezial
- `akzg-vertraulichkeit-redaction-spezial` — Akzg Vertraulichkeit Redaction Spezial
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt
- `anlagenverzeichnis-extrakt` — Anlagenverzeichnis Extrakt
- `anwaltsschriftsatz-beweislast-beweismittel` — Anwaltsschriftsatz Beweislast Beweismittel
- `anwaltsschriftsatz-stilrichtlinie` — Anwaltsschriftsatz Stilrichtlinie
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Aktenauszug Gerichtsverfahren (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
