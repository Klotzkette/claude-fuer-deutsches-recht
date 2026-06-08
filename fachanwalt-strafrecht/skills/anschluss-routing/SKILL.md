---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Strafrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aussagepsychologie-staatsanwaltschaft-aussagepsychologie` — Aussagepsychologie Staatsanwaltschaft Aussagepsychologie
- `chatcontrol-csam-einlassung-vorbereiten-hauptverhandlung` — Chatcontrol Csam Einlassung Vorbereiten Hauptverhandlung
- `ergaenzt-fachanwalt-insolvenzantrag-red-kanzlei-sonderfall` — Ergaenzt Fachanwalt Insolvenzantrag Red Kanzlei Sonderfall
- `fachanwalt-strafrecht-orientierung-untersuchungshaft` — Fachanwalt Strafrecht Orientierung Untersuchungshaft
- `koerperverletzung-stgb-koerperverletzung-todesfolge` — Koerperverletzung Stgb Koerperverletzung Todesfolge
- `mandat-triage-plaedoyer-vorbereitung-schriftsatzkern` — Mandat Triage Plaedoyer Vorbereitung Schriftsatzkern
- `nebenklage-nebenstrafrecht-opfervertretung-interessen-revision` — Nebenklage Nebenstrafrecht Opfervertretung Interessen Revision
- `raub-stgb-raub-todesfolge-rechtsbeugung-stgb` — Raub Stgb Raub Todesfolge Rechtsbeugung Stgb
- `steuerstrafrecht-ao-akteneinsicht-auswerten-erstgespraech` — Steuerstrafrecht Ao Akteneinsicht Auswerten Erstgespraech
- `stpo-strafrecht-strafverteidigung-zeugenbeistand-strafprozess` — Stpo Strafrecht Strafverteidigung Zeugenbeistand Strafprozess
- `strafprozess-antragslog-beweisantraege-biometrischer-cockpit` — Strafprozess Antragslog Beweisantraege Biometrischer Cockpit
- `strafprozess-instruktionen-pflichtverteidigung-beiordnung-strafr` — Strafprozess Instruktionen Pflichtverteidigung Beiordnung Strafr
- `strafr-dysfunk-befangenheitsantrag-beistandsleistung-stpo` — Strafr Dysfunk Befangenheitsantrag Beistandsleistung Stpo
- `strafr-dysfunk-darlegungslast-empirie-nutzen-erklaerungsrecht` — Strafr Dysfunk Darlegungslast Empirie Nutzen Erklaerungsrecht

## Arbeitsweg

- Ergebnis sichten: Welche Strafrecht und Strafprozessrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 341 StPO Revisionseinlegung 1 Woche, § 314 StPO Berufungseinlegung 1 Woche, § 345 StPO Revisionsbegründung 1 Monat nach Urteilszustellung, § 116 StPO HBÜ-Überprüfung 3/6 Monate, § 121 StPO 6-Monats-Grenze U-Haft), notwendige Dokumente (Haftbefehl, Anklageschrift, Eröffnungsbeschluss, Protokoll der Hauptverhandlung, Urteil, Revisionsantrag, Beweisantrag, Haftbeschwerde, Akteneinsicht-Akte), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Beschuldigter, Strafverteidiger, Staatsanwaltschaft, Ermittlungsrichter, Vorsitzender, Schöffen, Zeuge, Nebenkläger, JVA oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Strafrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46a StGB
- § 263 StGB
- § 49 StGB
- § 177 StGB
- § 46 StGB
- § 46b StGB
- § 35 BtMG
- § 261 StGB
- § 249 StGB
- § 212 StGB
- § 31 BtMG
- § 240 StGB

### Leitentscheidungen

- EuGH C-610/15
- EuGH C-527/15
- EuGH C-128/11
- EuGH C-145/10
- EuGH C-355/12

