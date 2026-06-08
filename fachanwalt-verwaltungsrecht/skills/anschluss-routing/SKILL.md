---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Verwaltungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anfechtungs-eilrechtsschutz-abs-eilrechtsschutz` — Anfechtungs Eilrechtsschutz Abs Eilrechtsschutz
- `einstweilige-fachanwalt-kanzlei` — Einstweilige Fachanwalt Kanzlei
- `erstgespraech-mandatsannahme-fa-vwgo-anfechtungsklage` — Erstgespraech Mandatsannahme Fa Vwgo Anfechtungsklage
- `fachanwalt-verwaltungsrecht-drittanfechtung-einstweiliger` — Fachanwalt Verwaltungsrecht Drittanfechtung Einstweiliger
- `fachanwalt-verwaltungsrecht-verwaltungsakt-rechtsbehelf-vwgo` — Fachanwalt Verwaltungsrecht Verwaltungsakt Rechtsbehelf Vwgo
- `normenkontrolle-ordnungsrecht-interessen-orientierung-sonderfall` — Normenkontrolle Ordnungsrecht Interessen Orientierung Sonderfall
- `normenkontrolle-vwgo-orientierung-vwgo-behoerde` — Normenkontrolle Vwgo Orientierung Vwgo Behörde
- `polizei-polizei-filmen-rechtsschutz-beweislast` — Polizei Polizei Filmen Rechtsschutz Beweislast
- `schnittstelle-verpflichtungsklage-verwaltungsrecht` — Schnittstelle Verpflichtungsklage Verwaltungsrecht
- `verwr-folgenbeseitigung-planfeststellung-grossvorhaben` — Verwr Folgenbeseitigung Planfeststellung Grossvorhaben
- `verwr-verwaltungsverfahren-eilantrag-abs-energietrassen` — Verwr Verwaltungsverfahren Eilantrag Abs Energietrassen
- `vorläufiger-vwvfg-vergleichsverhandlung-strategie` — Vorlaeufiger Vwvfg Vergleichsverhandlung Strategie
- `vwr-eilrechtsschutz-widerspruch-klage` — Vwr Eilrechtsschutz Widerspruch Klage

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Verwaltungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Verwaltungsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
