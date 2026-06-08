---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Strafbefehl-Verteidigung: ordnet Rolle (Beschuldigter, Staatsanwaltschaft, Amtsrichter), markiert Frist (§ 410 StPO Einspruch 2 Wochen), wählt Norm (§§ 407 ff. StPO, § 410 StPO Einspruch 2 Wochen) und Zuständigkeit (Amtsgericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Strafbefehl Verteidiger** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `aktenanlage-fehlerkatalog` — Aktenanlage Fehlerkatalog
- `akteneinsicht-behoerden-gericht-und-registerweg` — Akteneinsicht Behoerden Gericht und Registerweg
- `deal-beweislast-einspruch` — Deal Beweislast Einspruch
- `einspruch-risikoampel-und-gegenargumente` — Einspruch Risikoampel und Gegenargumente
- `einspruchsentscheidung-und-folgen` — Einspruchsentscheidung und Folgen
- `einstellung-153a-hauptverhandlung` — Einstellung 153a Hauptverhandlung
- `einstellung-fahrerlaubnis` — Einstellung Fahrerlaubnis
- `fahrerlaubnis-mandantenentscheidung` — Fahrerlaubnis Mandantenentscheidung
- `hauptverhandlung-international-schnittstellen` — Hauptverhandlung International Schnittstellen
- `mandantenkommunikation-redteam-qualitygate` — Mandantenkommunikation Redteam Qualitygate
- `nebenfolgen-fahrerlaubnis-strafbefehl` — Nebenfolgen Fahrerlaubnis Strafbefehl
- `nebenfolgen-strafbefehl-strafbefehls` — Nebenfolgen Strafbefehl Strafbefehls
- `pflichtverteidigung-quellenkarte` — Pflichtverteidigung Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Strafbefehl Verteidiger sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Strafbefehl-Verteidigung typische Eskalationsstufen: Einspruch, Akteneinsicht-Antrag, Verteidigungsstrategie-Memo.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
