---
name: quellen-livecheck
description: "Quellen-Live-Check für Europarecht-Kompass: prüft Normen (AEUV/EUV, EU-Grundrechtecharta, Sekundärrecht (VO/RL)) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt EuGH und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Europarecht Kompass** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anrufung-red-team-und-qualitaetskontrolle` — Anrufung RED Team und Qualitaetskontrolle
- `anschluss-router` — Anschluss Router
- `beihilfen-drafting-europarecht` — Beihilfen Drafting Europarecht
- `charta-quellenkarte` — Charta Quellenkarte
- `denkfehler-fristen-form-und-zustaendigkeit` — Denkfehler Fristen Form und Zustaendigkeit
- `drafting-internationaler-bezug-und-schnittstellen` — Drafting Internationaler Bezug und Schnittstellen
- `er-vorlageverfahren-eur-kommissionsverfahren` — ER Vorlageverfahren EUR Kommissionsverfahren
- `eu-rechtsquellen-vorlageweiche` — EU Rechtsquellen Vorlageweiche
- `eur-anrufung-state-beihilfen-vergaben` — EUR Anrufung State Beihilfen Vergaben
- `eur-kommissionsverfahren-art-258-spezial` — EUR Kommissionsverfahren ART 258 Spezial
- `eur-mandant-uebersicht-zustaendigkeiten` — EUR Mandant Uebersicht Zustaendigkeiten
- `eur-state-aid-notifikation-spezial` — EUR State AID Notifikation Spezial
- `europarecht-beihilfen-vergaben` — Europarecht Beihilfen Vergaben
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Europarecht Kompass (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
