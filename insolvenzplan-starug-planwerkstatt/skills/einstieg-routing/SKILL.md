---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Insolvenzplan / StaRUG: ordnet Rolle (Schuldnerunternehmen, Gläubiger, Sachwalter), markiert Frist (Erörterungstermin), wählt Norm (§§ 217-269 InsO Insolvenzplan, StaRUG §§ 4-71 Restrukturierungsplan) und Zuständigkeit (Insolvenzgericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Insolvenzplan Starug Planwerkstatt** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `abstimmung-mehrheiten-anlagenpaket` — Abstimmung Mehrheiten Anlagenpaket
- `anlagen-mehrparteien-konflikt-und-interessen` — Anlagen Mehrparteien Konflikt und Interessen
- `anlagenpaket` — Anlagenpaket
- `asset-deals-im-plan-grundstuecke-marken-kundendaten` — Asset Deals im Plan Grundstuecke Marken Kundendaten
- `cram-formular-portal-und-einreichung` — Cram Formular Portal und Einreichung
- `cramdown-obstruktion-datenraum-register` — Cramdown Obstruktion Datenraum Register
- `darstellender-quellenkarte` — Darstellender Quellenkarte
- `darstellender-teil` — Darstellender Teil
- `datenraum-register` — Datenraum Register
- `down-red-gestaltender-gruppen` — Down RED Gestaltender Gruppen
- `gerichtliche-schritte-kommandocenter` — Gerichtliche Schritte Kommandocenter
- `gestaltender-teil` — Gestaltender Teil
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Insolvenzplan Starug Planwerkstatt sind StaRUG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Insolvenzplan / StaRUG typische Eskalationsstufen: Planentwurf, Gruppenbildungsskizze, Vergleichsrechnung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
