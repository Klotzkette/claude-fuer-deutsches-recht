---
name: anschluss-routing
description: "Anschluss-Routing für Zwangsvollstreckung: wählt den nächsten Spezial-Skill nach Engpass (Erinnerung § 766 ZPO 2 Wochen, Vollstreckungstitel, Pfändungs- und Überweisungsbeschluss (PfÜB), Gerichtsvollzieher-Protokoll), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Zwangsvollstreckung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `765a-fehlerkatalog` — 765a Fehlerkatalog
- `802l-verhandlung-vergleich-und-eskalation` — 802l Verhandlung Vergleich und Eskalation
- `abwehr-schuldner` — Abwehr Schuldner
- `arbeit-schriftsatz-brief-und-memo-bausteine` — Arbeit Schriftsatz Brief und Memo Bausteine
- `bank-haertefall-inso` — Bank Haertefall Inso
- `elektronische-zustellung-eu` — Elektronische Zustellung EU
- `eu-kontenpfaendung-655-2014` — EU Kontenpfaendung 655 2014
- `haertefall-mandantenkommunikation-entscheidungsvorlage` — Haertefall Mandantenkommunikation Entscheidungsvorlage
- `inso-internationaler-bezug-und-schnittstellen` — Inso Internationaler Bezug und Schnittstellen
- `kommandocenter` — Kommandocenter
- `kontenpfaendung-notar-interessen-online` — Kontenpfaendung Notar Interessen Online
- `kontensuche-drittschuldner` — Kontensuche Drittschuldner
- `kontensuche-quellenkarte` — Kontensuche Quellenkarte
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Zwangsvollstreckung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Zwangsvollstreckung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
