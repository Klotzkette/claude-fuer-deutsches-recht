---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: verfassungsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Verfassungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-prozessarten-navigator-parteien-antraege` — Statthaftigkeit und Antragstellerrolle vor dem BVerfG klären: Verfassungsbeschwerde, § 32, Organstreit, Bund-Länder-Streit, Normenkontrollen, Wahlprüfung, Parteiverbot, Finanzierungsausschluss, Grundrechtsverwirkung und sonstige §-13-BVerfGG-Verfahren.
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Prüfen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Prüfen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhältnismäßigkeit
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Verfassungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Wenn Akte oder Nutzer nur sagt „zum Bundesverfassungsgericht“ oder wenn Parteien, Fraktionen, Abgeordnete, Bundes-/Landesorgane, Gerichte oder Gemeinden beteiligt sind, zuerst `bverfg-prozessarten-navigator-parteien-antraege` vorschalten. Nicht vorschnell als Verfassungsbeschwerde behandeln.
- Anschlussweichen identifizieren: drohende Frist (§ 93 BVerfGG Verfassungsbeschwerde 1 Monat nach Rechtswegerschöpfung / 1 Jahr bei Gesetzen, § 32 BVerfGG einstweilige Anordnung), notwendige Dokumente (Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
