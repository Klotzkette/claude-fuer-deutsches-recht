---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Zwangsverwaltung ZVG: ordnet Rolle (Gläubiger, Schuldner Eigentümer, Zwangsverwalter), markiert Frist (Beschwerde gegen Anordnung), wählt Norm (ZVG §§ 146 ff., BGB §§ 1135 ff. Pflichten) und Zuständigkeit (Amtsgericht Vollstreckungsgericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Zwangsverwaltung Zvg** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `aktenanlage-objektcockpit` — Aktenanlage Objektcockpit
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `berichtswesen-besitzuebernahme-bestellung` — Berichtswesen Besitzuebernahme Bestellung
- `beschlagnahme-fristen-form-und-zustaendigkeit` — Beschlagnahme Fristen Form und Zustaendigkeit
- `beschlagnahme-mietverwaltung-start` — Beschlagnahme Mietverwaltung Start
- `beschlagnahme-oeffentliche-lasten` — Beschlagnahme Oeffentliche Lasten
- `besitz-dokumentenmatrix-und-lueckenliste` — Besitz Dokumentenmatrix und Lueckenliste
- `besitzuebernahme` — Besitzuebernahme
- `bestellung-beschlagnahme` — Bestellung Beschlagnahme
- `betriebskosten-hausgeld-bieterangebot` — Betriebskosten Hausgeld Bieterangebot
- `bieterangebot-bewertung` — Bieterangebot Bewertung
- `bieterangebote-mieten-oeffentliche` — Bieterangebote Mieten Oeffentliche
- `gate-fehlerkatalog` — Gate Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Zwangsverwaltung Zvg sind ZVG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Zwangsverwaltung ZVG typische Eskalationsstufen: Anordnungsantrag, Verwalterbericht, Erinnerung gegen Anordnung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
