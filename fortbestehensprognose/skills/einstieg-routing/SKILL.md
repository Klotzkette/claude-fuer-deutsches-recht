---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Fortbestehensprognose StaRUG/InsO: ordnet Rolle (Geschäftsführung, Wirtschaftsprüfer, Insolvenzverwalter), markiert Frist (Antragsfrist 3 Wochen § 15a InsO), wählt Norm (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §§ 1/14/49, IDW S 11) und Zuständigkeit (Insolvenzgericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fortbestehensprognose** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `annahmen-behoerden-gericht-und-registerweg` — Annahmen Behoerden Gericht und Registerweg
- `annahmen-belastbarkeit-plausibilisieren` — Annahmen Belastbarkeit Plausibilisieren
- `annahmen-sammeln-bilanzieller-status` — Annahmen Sammeln Bilanzieller Status
- `ausloesendes-ereignis-erfassen` — Ausloesendes Ereignis Erfassen
- `bilanzieller-status-aufnehmen` — Bilanzieller Status Aufnehmen
- `bilanzstatus-risikoampel-und-gegenargumente` — Bilanzstatus Risikoampel und Gegenargumente
- `comfortletter-sonderfall-edge` — Comfortletter Sonderfall Edge
- `comfortletter-weich-erzeugen` — Comfortletter Weich Erzeugen
- `eskalation-sonderfall-und-edge-case` — Eskalation Sonderfall und Edge Case
- `fbp-bankenkommunikation-waiver-integrierte` — FBP Bankenkommunikation Waiver Integrierte
- `fbp-integrierte-planung-bauleiter` — FBP Integrierte Planung Bauleiter
- `fbp-stresstest-szenarien-leitfaden` — FBP Stresstest Szenarien Leitfaden
- `fbp-zahlungsunfaehigkeit` — FBP Zahlungsunfaehigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fortbestehensprognose sind InsO, StaRUG, § 19 Abs. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Fortbestehensprognose StaRUG/InsO typische Eskalationsstufen: Fortbestehensprognose IDW S 11, Restrukturierungsplan, Gutachten.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
