---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Kanzlei-Allgemein: ordnet Rolle (Anwalt, Mandant, Mitarbeitende), markiert Frist (Mandatsannahme), wählt Norm (BRAO, BORA, FAO, RVG, DSGVO) und Zuständigkeit (RAK), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Kanzlei Allgemein** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `abwesenheiten-urlaub` — Abwesenheiten Urlaub
- `akte-anlegen-und-aktenzeichen-zuordnen` — Akte Anlegen und Aktenzeichen Zuordnen
- `aktenbestand-pflege-bea-versand` — Aktenbestand Pflege BEA Versand
- `aktenzeichen` — Aktenzeichen
- `bea-journal` — BEA Journal
- `bea-versand-pruefen` — BEA Versand Pruefen
- `buchhaltung-konten-kanzlei-erechnung` — Buchhaltung Konten Kanzlei Erechnung
- `erechnung` — Erechnung
- `freundlicher-copilot-kanzlei` — Freundlicher Copilot Kanzlei
- `fristenbuch-fuehren` — Fristenbuch Fuehren
- `geburtstage-feiertage-abwesenheiten-urlaub` — Geburtstage Feiertage Abwesenheiten Urlaub
- `handelsregisterabruf` — Handelsregisterabruf
- `hr-personal-kanzlei-intake` — HR Personal Kanzlei Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Kanzlei Allgemein sind GwG, RVG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Kanzlei-Allgemein typische Eskalationsstufen: Mandatsvertrag, Honorarvereinbarung, Mandantenrundschreiben.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
