---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Gewerblicher Rechtsschutz** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abmahnung-urheberrecht-erfindungsmeldung-aufnahme-evvollzug` — Abmahnung Urheberrecht Erfindungsmeldung Aufnahme Evvollzug
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anmeldung-spezial-compliance-euipo` — Anmeldung Compliance Euipo
- `evvollzug-auslandszustellung-ev-abmahnung-abschlussschreiben` — Evvollzug Auslandszustellung Ev Abmahnung Abschlussschreiben
- `evvollzug-zustellung-durch-bea-einstweiliger` — Evvollzug Zustellung Durch Bea Einstweiliger
- `freedom-gewerblicher-markenrecherche` — Freedom Gewerblicher Markenrecherche
- `fto-triage-gewerblicher-rechtsschutz-mandat-arbeitsbereich` — Fto Triage Gewerblicher Rechtsschutz Mandat Arbeitsbereich
- `gewerblicher-rechtsschutz-kaltstart-interview` — Gewerblicher Rechtsschutz Kaltstart Interview
- `gewr-einstweilige-dpma-spezial-fristen` — Gewr Einstweilige Dpma Fristen
- `gewr-geschaeftsgeheimnisgesetz-markenanmeldung-bauleiter-uwg` — Gewr Geschaeftsgeheimnisgesetz Markenanmeldung Bauleiter Uwg
- `gw-einfuehrung-gw-einstweilige-mandat-triage` — Gw Einfuehrung Gw Einstweilige Mandat Triage
- `markenanmeldung-dpma-markenrecherche-open-source` — Markenanmeldung Dpma Markenrecherche Open Source
- `open-operate-reaktion` — Open Operate Reaktion
- `rechtsschutz-review-sonderfall-source-red` — Rechtsschutz Review Sonderfall Source Red

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
