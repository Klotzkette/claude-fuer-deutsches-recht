---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Common Law Kompass** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `begriffe-uebersetzung-bilingual-contract-client-explainer` — Begriffe Uebersetzung Bilingual Contract Client Explainer
- `bilinguale-client-commercial-sonderfall` — Bilinguale Client Commercial Sonderfall
- `cl-mandantenuebersicht-cl-prozesskostenrisiko-cl-precedent` — Cl Mandantenuebersicht Cl Prozesskostenrisiko Cl Precedent
- `cl-vertragsklauseln-vertragsbegriffe-cl-discovery` — Cl Vertragsklauseln Vertragsbegriffe Cl Discovery
- `common-consideration-discovery` — Common Consideration Discovery
- `contract-formation-false-friends-governing-jurisdiction` — Contract Formation False Friends Governing Jurisdiction
- `drafting-interessen-explainer-beweislast-false-friends` — Drafting Interessen Explainer Beweislast False Friends
- `friends-indemnity-quality` — Friends Indemnity Quality
- `humor-coach-interpretation-precedent-common-law` — Humor Coach Interpretation Precedent Common Law
- `litigation-discovery-ma-commercial-quality-gate` — Litigation Discovery Ma Commercial Quality Gate
- `rechtsvergleichender-begriffscheck-reviews-suretyship` — Rechtsvergleichender Begriffscheck Reviews Suretyship
- `remedies-damages-representations-warranties-simulation` — Remedies Damages Representations Warranties Simulation
- `surety-guarantee-ucc-sales-us-vs` — Surety Guarantee Ucc Sales Us Vs

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

- Ergebnis sichten: Welche Common Law Kompass-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Common Law Kompass.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 29 VwVfG
- Art. 267 AEUV
- § 31 BVerfGG
- § 4 EuRAG
- Art. 15 DSGVO

### Leitentscheidungen

- BGH XI ZR 39/04

