---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Mietrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amtlichen-amtsgericht-sonderfall-ausschliesslich` — Amtlichen Amtsgericht Sonderfall Ausschliesslich
- `bundesland-datenerhebung-grossstadt-mietspiegel` — Bundesland Datenerhebung Grossstadt Mietspiegel
- `klageentwurf-amtsgericht-miet-gewerbemiete-mietvertrag-bauleiter` — Klageentwurf Amtsgericht Miet Gewerbemiete Mietvertrag Bauleiter
- `lage-ausstattung-mahnung-zahlungsverzug-mandat-triage` — Lage Ausstattung Mahnung Zahlungsverzug Mandat Triage
- `miet-kuendigungsschutz-miet-mietminderung-mieteranfragen` — Miet Kuendigungsschutz Miet Mietminderung Mieteranfragen
- `mieter-mieteranfragen-mandantenentscheidung-mieterhoehungs` — Mieter Mieteranfragen Mandantenentscheidung Mieterhoehungs
- `mieterhoehung-widersprechen-mieterhoehungsverlangen-erstellen` — Mieterhoehung Widersprechen Mieterhoehungsverlangen Erstellen
- `mietpreisueberhoehung-wistrg-mietsenkungsverlangen-mietspiegel` — Mietpreisueberhoehung Wistrg Mietsenkungsverlangen Mietspiegel
- `mietrecht-mietsenkungsverlangen-international-mietspiegel` — Mietrecht Mietsenkungsverlangen International Mietspiegel
- `mr-betriebskostenabrechnung-mr-kuendigungsschutz-mr` — Mr Betriebskostenabrechnung Mr Kuendigungsschutz Mr
- `mr-einfuehrung-klageentwurf-beweislast-eigenbedarfskuendigung` — Mr Einfuehrung Klageentwurf Beweislast Eigenbedarfskuendigung
- `nebenkostenabrechnung-erstellen-faktenbank` — Nebenkostenabrechnung Erstellen Faktenbank
- `nebenkostenpruefung-prozessstrategie-mieterhoehung-quellen` — Nebenkostenpruefung Prozessstrategie Mieterhoehung Quellen

## Arbeitsweg

- Ergebnis sichten: Welche Mietrecht und WEG-Recht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 573c BGB Kündigung 3 Monate, § 558b BGB Zustimmung Mieterhöhung Ende 2. Folgemonat, § 24 Abs. 4 WEG Ladung 3 Wochen, § 556 BGB Nebenkostenabrechnung 12 Monate), notwendige Dokumente (Mietvertrag, Mieterhöhungsverlangen, Mietspiegel, Nebenkostenabrechnung, Kündigungsschreiben, Modernisierungsankündigung, WEG-Protokoll, Beschlusssammlung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Vermieter, Mieter, Hausverwaltung, WEG-Verwaltung, Amtsgericht der Belegenheit, Mieterverein, Eigentümergemeinschaft oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Mietrecht (Wohnraum/Gewerbe).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 20 WEG
- § 16 WEG
- § 5 WiStrG
- § 291 StGB
- § 45 WEG
- § 25 WEG
- § 41 GKG
- § 24 WEG
- § 21 WEG
- § 8 WiStrG
- § 9a WEG
- § 26 WEG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

