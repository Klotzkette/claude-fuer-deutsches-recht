---
name: anschluss-routing
description: "Anschluss-Routing für Gewerblicher Rechtsschutz (allgemein): wählt den nächsten Spezial-Skill nach Engpass (Markenwiderspruch 3 Monate, Markenregisterauszug, Patentschrift, Geschmacksmusterurkunde), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Gewerblicher Rechtsschutz** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


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
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Gewerblicher Rechtsschutz-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Gewerblicher Rechtsschutz (allgemein).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
