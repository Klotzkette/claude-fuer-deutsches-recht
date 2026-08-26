---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Strafrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Strafrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `workflow-redteam-qualitygate` — Adhaesionsverfahren Ermittlungsverfahren
- `strafrecht-spezial-aussagepsychologie-staatsanwaltschaft-replik` — Aussagepsychologie Staatsanwaltschaft
- `chatcontrol-csam-anwaltsgeheimnis-53-stpo` — Chatcontrol Csam Einlassung Vorbereiten
- `ergaenzt-mandantenkommunikation-entscheidungsvorlage` — Ergaenzt Fachanwalt Insolvenzantrag RED Team Korrektur
- `fa-strafrecht-quellen-frist-next` — FA Strafrecht Quellen Frist Next
- `freiheitsstrafe-paragraf-57-stgb` — Freiheitsstrafe Paragraf 57 STGB
- `hauptverhandlung-quellenkarte` — Hauptverhandlung Quellenkarte
- `strafrecht-spezial-koerperverletzung-223-stgb-grund` — Koerperverletzung STGB Todesfolge
- `mandat-triage-strafrecht` — Mandat Triage Plaedoyer Vorbereitung
- `nebenklage-compliance-dokumentation-und-akte` — Nebenklage Nebenstrafrecht Opfervertretung
- `notwehr-paragraf-32-stgb` — Notwehr Paragraf 32 STGB
- `orientierung-mandat-fachanwaltschaft` — Orientierung
- `strafrecht-spezial-raub-249-stgb` — Raub Rechtsbeugung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Strafrecht und Strafprozessrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 341 StPO Revisionseinlegung 1 Woche, § 314 StPO Berufungseinlegung 1 Woche, § 345 StPO Revisionsbegründung 1 Monat nach Urteilszustellung, § 116 StPO HBÜ-Überprüfung 3/6 Monate, § 121 StPO 6-Monats-Grenze U-Haft), notwendige Dokumente (Haftbefehl, Anklageschrift, Eröffnungsbeschluss, Protokoll der Hauptverhandlung, Urteil, Revisionsantrag, Beweisantrag, Haftbeschwerde, Akteneinsicht-Akte), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Beschuldigter, Strafverteidiger, Staatsanwaltschaft, Ermittlungsrichter, Vorsitzender, Schöffen, Zeuge, Nebenkläger, JVA oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
