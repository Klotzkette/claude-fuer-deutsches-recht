---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Aktenauszüge zivilgerichtlicher Verfahren: ordnet Rolle (Mandant, Gegenpartei, Gericht), markiert Frist (Akteneinsicht im laufenden Verfahren jederzeit), wählt Norm (§ 299 ZPO Akteneinsicht, § 130a ZPO eA-Übermittlung, § 169 GVG Öffentlichkeit) und Zuständigkeit (AG/LG/OLG), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Aktenauszug Gerichtsverfahren** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `akten-mandantenkommunikation-entscheidungsvorlage` — Akten Mandantenkommunikation Entscheidungsvorlage
- `aktenauszug-erstellen` — Aktenauszug Erstellen
- `aktenauszug-strukturpruefung-akzg-bauleiter` — Aktenauszug Strukturpruefung Akzg Bauleiter
- `aktenauszug-tatbestand-beweis-und-belege` — Aktenauszug Tatbestand Beweis und Belege
- `aktenauszug-verfahrensidentifikation-gericht` — Aktenauszug Verfahrensidentifikation Gericht
- `akzg-aktenauszug-bauleiter` — Akzg Aktenauszug Bauleiter
- `akzg-multiparteienverfahren-konsolidierung-spezial` — Akzg Multiparteienverfahren Konsolidierung Spezial
- `akzg-vertraulichkeit-redaction-spezial` — Akzg Vertraulichkeit Redaction Spezial
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt
- `anlagenverzeichnis-extrakt` — Anlagenverzeichnis Extrakt
- `anwaltsschriftsatz-beweislast-beweismittel` — Anwaltsschriftsatz Beweislast Beweismittel
- `anwaltsschriftsatz-stilrichtlinie` — Anwaltsschriftsatz Stilrichtlinie
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Aktenauszug Gerichtsverfahren sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Aktenauszüge zivilgerichtlicher Verfahren typische Eskalationsstufen: Aktenauszug mit Inhaltsverzeichnis, Chronologie, Beweisindex.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
