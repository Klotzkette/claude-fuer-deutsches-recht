---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Insolvenzplan Starug Planwerkstatt** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `down-red-gestaltender-gruppen` — Down Red Gestaltender Gruppen
- `insolvenzplan-intake-klassen` — Insolvenzplan Intake Klassen
- `ips-abstimmung-ips-anlagenpaket-ips-asset` — Ips Abstimmung Ips Anlagenpaket Ips Asset
- `ips-cramdown-ips-datenraum-ips-gestaltender` — Ips Cramdown Ips Datenraum Ips Gestaltender
- `ips-gerichtliche-ips-ips-steuern` — Ips Gerichtliche Ips Ips Steuern
- `ips-gruppen-ips-architektur-ips-integrierte` — Ips Gruppen Ips Architektur Ips Integrierte
- `ips-ips-sanierungskonzept-ips-sicherheiten` — Ips Ips Sanierungskonzept Ips Sicherheiten
- `ips-kaltstart-interview` — Ips Kaltstart Interview
- `ips-minderheitenschutz-ips-planbetroffene-ips-planvollzug` — Ips Minderheitenschutz Ips Planbetroffene Ips Planvollzug
- `ips-stabilisierung-ips-stakeholder-ips-plan` — Ips Stabilisierung Ips Stakeholder Ips Plan
- `ips-verfahrenswahl-restrukturierungsplan-ips-darstellender` — Ips Verfahrenswahl Restrukturierungsplan Ips Darstellender
- `ips-vergleichsrechnung-ipsplan-cram-ipsplan-gruppenbildung` — Ips Vergleichsrechnung Ipsplan Cram Ipsplan Gruppenbildung

## Arbeitsweg

- Ergebnis sichten: Welche Insolvenzplan Starug Planwerkstatt-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Insolvenzplan / StaRUG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
