---
name: anschluss-routing
description: "Anschluss-Routing für Common Law Kompass: wählt den nächsten Spezial-Skill nach Engpass (Statutes of Limitations je Jurisdiction, Pleadings, Discovery requests, Affidavits), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Common Law Kompass** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


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
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

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

