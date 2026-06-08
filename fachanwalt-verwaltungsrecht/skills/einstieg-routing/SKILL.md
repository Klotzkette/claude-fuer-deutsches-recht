---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Fachanwalt Verwaltungsrecht: ordnet Rolle (Bürger/Antragsteller, Behörde, Verwaltungsgericht), markiert Frist (§ 74 VwGO Klagefrist 1 Mon.), wählt Norm (VwGO, VwVfG, AO (steuerlich)) und Zuständigkeit (VG, OVG/VGH, BVerwG), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Verwaltungsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `amtshaftung-paragraf-839-bgb-art-34-gg` — Amtshaftung Paragraf 839 BGB ART 34 GG
- `anfechtungs-eilrechtsschutz-abs` — Anfechtungs Eilrechtsschutz ABS
- `anhoerung-paragraf-28-vwvfg` — Anhoerung Paragraf 28 Vwvfg
- `anordnung-quellenkarte` — Anordnung Quellenkarte
- `drittanfechtung` — Drittanfechtung
- `eilrechtsschutz-paragraf-80-vwgo` — Eilrechtsschutz Paragraf 80 Vwgo
- `einstweilige-fachanwalt-kanzlei` — Einstweilige Fachanwalt Kanzlei
- `ermessen-paragraf-40-vwvfg` — Ermessen Paragraf 40 Vwvfg
- `erstgespraech-mandatsannahme-fa-vwgo` — Erstgespraech Mandatsannahme FA Vwgo
- `fa-verwaltungsrecht-mandant-redteam-gate` — FA Verwaltungsrecht Mandant Redteam Gate
- `fa-verwaltungsrecht-start-chronologie-fristen` — FA Verwaltungsrecht Start Chronologie Fristen
- `klagefrist-paragraf-58-vwgo-bverwg-4-c-1-19` — Klagefrist Paragraf 58 Vwgo Bverwg 4 C 1 19
- `kommunalrecht-paragraf-2-go` — Kommunalrecht Paragraf 2 GO
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Verwaltungsrecht sind VwGO, VwVfG, § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Fachanwalt Verwaltungsrecht typische Eskalationsstufen: Widerspruch, Klage VG, Eilantrag § 80 V VwGO.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
