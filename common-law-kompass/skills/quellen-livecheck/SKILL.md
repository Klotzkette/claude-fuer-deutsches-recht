---
name: quellen-livecheck
description: "Quellen-Live-Check für Common Law Kompass: prüft Normen (UK/US/Commonwealth common law, Restatements (US), ECHR/EU-CFR) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt UK Supreme Court, US Supreme Court und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Common Law Kompass** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `begriffe-uebersetzung-bilingual-contract` — Begriffe Uebersetzung Bilingual Contract
- `bilingual-contract-review` — Bilingual Contract Review
- `bilinguale-client-commercial-sonderfall` — Bilinguale Client Commercial Sonderfall
- `cl-discovery-doc-production-spezial` — CL Discovery DOC Production Spezial
- `cl-mandantenuebersicht-cl-prozesskostenrisiko` — CL Mandantenuebersicht CL Prozesskostenrisiko
- `cl-prozesskostenrisiko-each-party-bears-own` — CL Prozesskostenrisiko Each Party Bears OWN
- `cl-spezial-precedent-vs-statute` — CL Spezial Precedent VS Statute
- `cl-vertragsklauseln-vertragsbegriffe-cl` — CL Vertragsklauseln Vertragsbegriffe CL
- `client-explainer` — Client Explainer
- `client-mandantenkommunikation-entscheidungsvorlage` — Client Mandantenkommunikation Entscheidungsvorlage
- `commercial-sonderfall-und-edge-case` — Commercial Sonderfall und Edge Case
- `common-consideration-discovery` — Common Consideration Discovery
- `consideration-behoerden-gericht-und-registerweg` — Consideration Behoerden Gericht und Registerweg
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Regelungs- und Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `UCC § 2-201` — Statute of Frauds für Warenkauf.
- `UCC § 2-313` — express warranties.
- `UCC § 2-314` — implied warranty of merchantability.
- `Restatement (Second) of Contracts § 17` — formation by bargain.
- `Restatement (Second) of Contracts § 71` — consideration.
- `Restatement (Second) of Contracts § 90` — promissory estoppel.
- `CISG Art. 14` — Angebot.
- `CISG Art. 18` — Annahme.
- `CISG Art. 25` — wesentliche Vertragsverletzung.
- `CISG Art. 35` — Vertragsmaessigkeit der Ware.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Common Law Kompass (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
