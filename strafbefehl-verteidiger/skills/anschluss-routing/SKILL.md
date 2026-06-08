---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Strafbefehl Verteidiger** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `deal-beweislast-einspruch-einspruchsentscheidung-folgen` — Deal Beweislast Einspruch Einspruchsentscheidung Folgen
- `einstellung-153a-hauptverhandlung-vorbereitung-strafbefehl` — Einstellung 153a Hauptverhandlung Vorbereitung Strafbefehl
- `einstellung-fahrerlaubnis-mandantenentscheidung-hauptverhandlung` — Einstellung Fahrerlaubnis Mandantenentscheidung Hauptverhandlung
- `gegen-strafbefehl-einspruch-strafbefehl-aktenanlage` — Gegen Strafbefehl Einspruch Strafbefehl Aktenanlage
- `nebenfolgen-fahrerlaubnis-strafbefehl-pflichtverteidiger` — Nebenfolgen Fahrerlaubnis Strafbefehl Pflichtverteidiger
- `nebenfolgen-strafbefehl-strafbefehls` — Nebenfolgen Strafbefehl Strafbefehls
- `rechtsmittel-nach-tagessaetze-geldstrafe-strafbefehl` — Rechtsmittel Nach Tagessaetze Geldstrafe Strafbefehl
- `stbv-einspruch-strafbefehl-fahrerlaubnis-auslaendischer-mandant` — Stbv Einspruch Strafbefehl Fahrerlaubnis Auslaendischer Mandant
- `stbv-strafbefehl-abwesenheit-vertretung-akteneinsicht` — Stbv Strafbefehl Abwesenheit Vertretung Akteneinsicht
- `strafbefehl-einlassung-deal-verstaendigung-einspruch` — Strafbefehl Einlassung Deal Verstaendigung Einspruch
- `strafbefehl-quality-gate-akteneinsicht` — Strafbefehl Quality Gate Akteneinsicht
- `tagessaetze-verstaendigung-sonderfall-verteidiger` — Tagessaetze Verstaendigung Sonderfall Verteidiger
- `verteidigung-wiedereinsetzung-zeugenstrategie-interessen` — Verteidigung Wiedereinsetzung Zeugenstrategie Interessen

## Arbeitsweg

- Ergebnis sichten: Welche Strafbefehl Verteidiger-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Strafbefehl-Verteidigung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46 StGB
- § 69 StGB
- § 40 StGB
- § 44 StGB
- § 17 StGB
- § 69a StGB
- § 1 StGB
- § 15 StGB
- § 16 StGB
- § 42 StGB
- § 43 StGB
- § 201 StGB

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

