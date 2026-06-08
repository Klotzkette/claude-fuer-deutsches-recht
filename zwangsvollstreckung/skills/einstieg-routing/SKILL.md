---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Zwangsvollstreckung: ordnet Rolle (Gläubiger, Schuldner, Drittschuldner (Arbeitgeber, Bank)), markiert Frist (Erinnerung § 766 ZPO 2 Wochen), wählt Norm (ZPO §§ 704-945 (Vollstreckung), GVGA, InsO) und Zuständigkeit (Vollstreckungsgericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Zwangsvollstreckung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


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
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Zwangsvollstreckung sind ZPO, § 201 InsO, ZVG, EU, § 765a H, § 800 ZPO Notar,, § 802l Kontensuche, Verm, §§ 704 ff. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Zwangsvollstreckung typische Eskalationsstufen: Vollstreckungsantrag, PfÜB, Erinnerung § 766 ZPO.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
