---
name: quellen-livecheck
description: "Quellen-Live-Check für Gewerblicher Rechtsschutz (allgemein): prüft Normen (MarkenG, PatG, GeschmMG, GebrMG, UrhG, UWG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt DPMA und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Gewerblicher Rechtsschutz** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abmahnung-compliance-dokumentation-und-akte` — Abmahnung Compliance Dokumentation und Akte
- `abmahnung-urheberrecht-erfindungsmeldung` — Abmahnung Urheberrecht Erfindungsmeldung
- `anmeldung-spezial-compliance-euipo` — Anmeldung Spezial Compliance Euipo
- `anpassen` — Anpassen
- `compliance-mandantenkommunikation-entscheidungsvorlage` — Compliance Mandantenkommunikation Entscheidungsvorlage
- `dpma-fristen-form-und-zustaendigkeit` — Dpma Fristen Form und Zustaendigkeit
- `erfindungsmeldung-aufnahme` — Erfindungsmeldung Aufnahme
- `euipo-dokumentenmatrix-und-lueckenliste` — Euipo Dokumentenmatrix und Lueckenliste
- `evvollzug-auslandszustellung-ev-abmahnung` — Evvollzug Auslandszustellung EV Abmahnung
- `evvollzug-neu-001-einstweilige-verfuegung-vollziehung-frist` — Evvollzug NEU 001 Einstweilige Verfuegung Vollziehung Frist
- `evvollzug-neu-002-urteilsverfuegung-beschlussverfuegung-und-zust` — Evvollzug NEU 002 Urteilsverfuegung Beschlussverfuegung und Zust
- `evvollzug-neu-004-bea-zustellung-einstweiliger-rechtsschutz-risi` — Evvollzug NEU 004 BEA Zustellung Einstweiliger Rechtsschutz Risi
- `evvollzug-neu-005-ordnungsmittelantrag-vollstreckung-unterlassun` — Evvollzug NEU 005 Ordnungsmittelantrag Vollstreckung Unterlassun
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (UWG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Gewerblicher Rechtsschutz (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
