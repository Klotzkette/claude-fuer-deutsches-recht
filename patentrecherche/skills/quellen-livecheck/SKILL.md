---
name: quellen-livecheck
description: "Quellen-Live-Check für Patentrecherche (FTO, Validity, Family-Watch): prüft Normen (PatG § 3 Neuheit, § 4 Erfinderischer Schritt, EPÜ Art. 54/56, PCT) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt DPMA und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Patentrecherche** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `agentisch-fristen-form-und-zustaendigkeit` — Agentisch Fristen Form und Zustaendigkeit
- `agentische-datenbank-recherche` — Agentische Datenbank Recherche
- `depatisnet-verhandlung-vergleich-und-eskalation` — Depatisnet Verhandlung Vergleich und Eskalation
- `dpmaregister-epue-beweislast-erfinderische` — Dpmaregister Epue Beweislast Erfinderische
- `epo-opposition-strategie` — EPO Opposition Strategie
- `epo-quellenkarte` — EPO Quellenkarte
- `epue-beweislast-und-darlegungslast` — Epue Beweislast und Darlegungslast
- `erfinderische-sonderfall-und-edge-case` — Erfinderische Sonderfall und Edge Case
- `erfinderische-taetigkeit-freedom-to-ki-patent` — Erfinderische Taetigkeit Freedom TO KI Patent
- `espacenet-google-neuheit-red-team-korrektur` — Espacenet Google Neuheit RED Team Korrektur
- `freedom-to-operate-recherche` — Freedom TO Operate Recherche
- `google-risikoampel-und-gegenargumente` — Google Risikoampel und Gegenargumente
- `kaltstart-interview` — Kaltstart Interview
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (PatG §§ 1, 3, 4, 9, 10, 139, EPÜ Art. 54, 56, 64, 69, 87 ff., Straßburger IPC-Abkommen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Patentrecherche und FTO (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
