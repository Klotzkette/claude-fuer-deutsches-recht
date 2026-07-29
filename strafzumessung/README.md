# Strafzumessung

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur großen Strafkammer. Paragraf 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewährung Paragraf 56 Paragraf 49 Regelbeispiele besonders schwerer Fall Verständigung Paragraf 257c StPO TOA Paragraf 46a Gesamtstrafe Paragraf 55 JGG.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/strafzumessung.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strafzumessung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafzumessung/strafzumessung-werkstatt.md" download><code>strafzumessung-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafzumessung/strafzumessung-schnellstart.md" download><code>strafzumessung-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Strafzumessung Bankert — Untreue, LG Frankfurt / BGH Revision](../testakten/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung/README.md) | [Gesamt-PDF](../testakten/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung/gesamt-pdf/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung_gesamt.pdf) | [`testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip) | [`testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Strafrahmen, Strafzumessungstatsachen, Geständnis, Vorbelastungen, Einziehung, Bewährung, Nebenfolgen und Rechtsmittelrisiken sauber strukturieren.
Plugin für die **Strafzumessung nach deutschem Strafrecht** — vom Strafbefehl bis zur großen Strafkammer. Adressaten: Strafverteidiger und Staatsanwaltschaft.

## Worum geht es?

Strafzumessung ist die zentrale richterliche Aufgabe nach Schuldspruch: Bestimmung von Strafart und Strafhöhe innerhalb des gesetzlichen Strafrahmens auf Grundlage der **Schuld** (§ 46 Abs. 1 Satz 1 StGB), unter Berücksichtigung der **präventiven Wirkungen** (§ 46 Abs. 1 Satz 2 StGB), nach den **Strafzumessungstatsachen** des § 46 Abs. 2 StGB und unter Beachtung des **Doppelverwertungsverbots** (§ 46 Abs. 3 StGB).

Das Plugin deckt die Strafzumessung vom Strafbefehlsverfahren über die Hauptverhandlung bis zur Vollstreckung ab, inklusive Bewährung, Strafmilderung, Regelbeispielen, Gesamtstrafenbildung, Verständigung und Jugendstrafrecht.

## Schnellstart

1. Mit `orientierung-strafzumessung-triage` einsteigen.
2. Rolle (Strafverteidigung, Staatsanwaltschaft) und Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachträgliche Gesamtstrafe) angeben.
3. Den vom Triage-Skill empfohlenen Spezial-Skill aktivieren.
4. Bei Bedarf parallel mit den Plugins `strafbefehl-verteidiger` oder `fachanwalt-strafrecht` arbeiten.

## Enthaltene Skills

### Block A — Orientierung und Grundlagen
- `orientierung-strafzumessung-triage` — Einstieg, Triage, Spezial-Skill-Routing.
- `paragraph-46-stgb-grundsatz-strafzumessung` — § 46 StGB, Schuld als Grundlage.
- `strafzumessungs-tatsachen-46-ii-stgb` — Katalog § 46 Abs. 2 StGB.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik vor jeder Zumessung.

### Block B — Geldstrafe
- `geldstrafe-tagessatzanzahl-bestimmen` — § 40 Abs. 1 StGB, Tagessatzanzahl als Schuldgröße.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — § 40 Abs. 2 StGB, Nettoeinkommen / 30.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe; § 47 StGB.

### Block C — Freiheitsstrafe und Bewährung
- `freiheitsstrafe-strafmass-pruefen` — Konkrete Zumessung im Strafrahmen.
- `bewaehrung-56-stgb-positive-sozialprognose` — § 56 StGB.
- `bewaehrung-auflagen-und-weisungen-56b-c-stgb` — §§ 56b, 56c StGB.
- `bewaehrungswiderruf-56f-stgb` — § 56f StGB.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — U-Haft-Anrechnung § 51 StGB, Reststrafenaussetzung § 57 StGB.

### Block D — Strafmilderung und Schärfung
- `strafmilderung-49-stgb-zwingend-fakultativ` — § 49 StGB.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Strafrahmen-Modifikation.
- `regelbeispiele-rechtsprechung` — § 243 StGB, § 263 Abs. 3 StGB u.a.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — § 46a StGB; BGH 4 StR 232/25.

### Block E — Strafbefehl und kleine Verfahren
- `strafbefehl-strafzumessung-407-stpo` — Strafzumessung im Strafbefehl.
- `153a-stpo-einstellung-gegen-auflage` — Einstellung mit Auflage.

### Block F — Hauptverhandlung und Verständigung
- `verstaendigung-257c-stpo-strafzumessung` — § 257c StPO; BVerfG 2 BvR 2628/10; BGH 1 StR 525/11.
- `gestaendnis-und-strafmilderung` — Geständnis als Strafmilderungsgrund.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Strafurteil-Begründung.

### Block G — Gesamtstrafenbildung
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — §§ 53, 54 StGB.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — § 55 StGB, Zäsurwirkung, § 460 StPO.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — BGH-ständige Linie.

### Block H — Sonderfälle
- `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` — JGG; § 105 JGG Heranwachsende.

## Querverweise zu anderen Plugins

- `strafbefehl-verteidiger` — Spezial-Plugin Strafbefehlsverfahren.
- `fachanwalt-strafrecht` — Strafrechts-Gesamtverteidigung, Plädoyer, Revision.
- `verkehrsowi-verteidiger` — Verkehrs-OWi-Strafzumessung.
- `urteilsbauer-relationsmacher` — Urteilsverfassung.
- `subsumtions-pruefer` — vor Schuldspruch.

## Hinweise zur Anwendung

- **Quellenregel beachten**: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Aktenzeichen vor Zitat in **dejure.org** oder **openjur.de** verifizieren. Lizenzierte Datenbanken nur bei vorhandenem Zugang.
- **Keine Präjudizienbindung** (Ausnahme § 31 BVerfGG). BGH-Linien sind argumentationsstützend, nicht bindend.
- **Mandantengeheimnis** wahren (§ 43a Abs. 2 BRAO; § 203 StGB).
- **Aktueller BGH-Anker** zum TOA: BGH, Urteil vom 20.11.2025 — 4 StR 232/25 (friedensstiftender kommunikativer Prozess und eindeutige Verantwortungsübernahme).
- **BVerfG zur Verständigung**: 2 BvR 2628/10 vom 19.03.2013.
- **BGH-Belehrungspflicht**: 1 StR 525/11 vom 07.02.2012.

## Stand

- 05/2026.
- §§ 38 ff. StGB, §§ 407 ff. StPO, JGG, BtMG.
- Aktualitätsprüfung jährlich empfohlen.

## Lizenz

Apache-2.0 OR MIT (siehe Plugin-Root).


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`orientierung-triage-paragraph-stgb-besonders`](skills/orientierung-triage-paragraph-stgb-besonders/SKILL.md), [`strafzumessung-erstpruefung-und-mandatsziel`](skills/strafzumessung-erstpruefung-und-mandatsziel/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`besonders-formular-portal-und-einreichung`](skills/besonders-formular-portal-und-einreichung/SKILL.md), [`deutschem-tatbestand-beweis-und-belege`](skills/deutschem-tatbestand-beweis-und-belege/SKILL.md), [`freiheitsstrafe-compliance-dokumentation-und-akte`](skills/freiheitsstrafe-compliance-dokumentation-und-akte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-tagessatz-livequellen-und-rechtsprechungscheck`](skills/spezial-tagessatz-livequellen-und-rechtsprechungscheck/SKILL.md), [`strafbefehl-dokumentenmatrix-und-lueckenliste`](skills/strafbefehl-dokumentenmatrix-und-lueckenliste/SKILL.md), [`tagessatz-quellenkarte`](skills/tagessatz-quellenkarte/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`grossen-risikoampel-und-gegenargumente`](skills/grossen-risikoampel-und-gegenargumente/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`spezial-grossen-risikoampel-und-gegenargumente`](skills/spezial-grossen-risikoampel-und-gegenargumente/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`](skills/haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung/SKILL.md), [`strafzumessungstatsachen-vergleich-eskalation`](skills/strafzumessungstatsachen-vergleich-eskalation/SKILL.md), [`taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung`](skills/taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`freiheitsstrafe-ohne-bewaehrung-vollstreckung`](skills/freiheitsstrafe-ohne-bewaehrung-vollstreckung/SKILL.md), [`iii-stpo-begruendungsanforderungen-strafurteil`](skills/iii-stpo-begruendungsanforderungen-strafurteil/SKILL.md), [`stgb-schriftsatz-brief-und-memo-bausteine`](skills/stgb-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`strafrecht-verfahrensstadium-strafbefehl`](skills/strafrecht-verfahrensstadium-strafbefehl/SKILL.md), [`verfahrensstadium-strafbefehl-bis-kammer`](skills/verfahrensstadium-strafbefehl-bis-kammer/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`schwerer-fehlerkatalog`](skills/schwerer-fehlerkatalog/SKILL.md), [`spezial-schwerer-red-team-und-qualitaetskontrolle`](skills/spezial-schwerer-red-team-und-qualitaetskontrolle/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`153a-stpo-iii-bewaehrung-stgb`](skills/153a-stpo-iii-bewaehrung-stgb/SKILL.md), [`bewaehrung-56-stgb-positive-sozialprognose`](skills/bewaehrung-56-stgb-positive-sozialprognose/SKILL.md), [`bewaehrung-auflagen-bewaehrungswiderruf-56f`](skills/bewaehrung-auflagen-bewaehrungswiderruf-56f/SKILL.md), [`bewaehrung-interessen-deutschem`](skills/bewaehrung-interessen-deutschem/SKILL.md), [`bewaehrungswiderruf-56f-stgb`](skills/bewaehrungswiderruf-56f-stgb/SKILL.md), [`freiheitsstrafe-strafmass-geldstrafe`](skills/freiheitsstrafe-strafmass-geldstrafe/SKILL.md), [`freiheitsstrafe-strafmass-pruefen`](skills/freiheitsstrafe-strafmass-pruefen/SKILL.md), [`geldstrafe-grossen-rechtsmittel`](skills/geldstrafe-grossen-rechtsmittel/SKILL.md), [`geldstrafe-tagessatzanzahl-bestimmen`](skills/geldstrafe-tagessatzanzahl-bestimmen/SKILL.md), [`geldstrafe-vs-freiheitsstrafe-47-stgb`](skills/geldstrafe-vs-freiheitsstrafe-47-stgb/SKILL.md), [`gesamtstrafenbildung-stgb-gestaendnis`](skills/gesamtstrafenbildung-stgb-gestaendnis/SKILL.md), [`gestaendnis-und-strafmilderung`](skills/gestaendnis-und-strafmilderung/SKILL.md), [`jgg-jugendstrafe-minder-schwerer`](skills/jgg-jugendstrafe-minder-schwerer/SKILL.md), [`minder-schwerer-fall-und-besonders-schwerer-fall`](skills/minder-schwerer-fall-und-besonders-schwerer-fall/SKILL.md), [`nachtraegliche-gesamtstrafenbildung-55-stgb`](skills/nachtraegliche-gesamtstrafenbildung-55-stgb/SKILL.md), [`paragraph-46-stgb-grundsatz-strafzumessung`](skills/paragraph-46-stgb-grundsatz-strafzumessung/SKILL.md), [`rechtsmittel-und-gesamtstrafenfolgen`](skills/rechtsmittel-und-gesamtstrafenfolgen/SKILL.md), [`regelbeispiele-rechtsprechung`](skills/regelbeispiele-rechtsprechung/SKILL.md), ... plus 13 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`153a-stpo-iii-bewaehrung-stgb`](skills/153a-stpo-iii-bewaehrung-stgb/SKILL.md) | Wenn es um Einstellung gegen Auflage — Paragraf 153a StPO in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Strafzumessung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`besonders-formular-portal-und-einreichung`](skills/besonders-formular-portal-und-einreichung/SKILL.md) | Wenn es um Besonders: Formular, Portal und Einreichungslogik in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bewaehrung-56-stgb-positive-sozialprognose`](skills/bewaehrung-56-stgb-positive-sozialprognose/SKILL.md) | Wenn es um Strafaussetzung zur Bewaehrung — Paragraf 56 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bewaehrung-auflagen-bewaehrungswiderruf-56f`](skills/bewaehrung-auflagen-bewaehrungswiderruf-56f/SKILL.md) | Wenn es um Auflagen und Weisungen — Paragrafen 56b, 56c StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bewaehrung-interessen-deutschem`](skills/bewaehrung-interessen-deutschem/SKILL.md) | Wenn es um Bewaehrung: Mehrparteienkonflikt und Interessenmatrix in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bewaehrungswiderruf-56f-stgb`](skills/bewaehrungswiderruf-56f-stgb/SKILL.md) | Wenn es um Bewaehrungswiderruf — Paragraf 56f StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`deutschem-tatbestand-beweis-und-belege`](skills/deutschem-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Strafzumessung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Strafzumessung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`freiheitsstrafe-compliance-dokumentation-und-akte`](skills/freiheitsstrafe-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Freiheitsstrafe: Compliance-Dokumentation und Aktenvermerk in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`freiheitsstrafe-ohne-bewaehrung-vollstreckung`](skills/freiheitsstrafe-ohne-bewaehrung-vollstreckung/SKILL.md) | Wenn es um Freiheitsstrafe ohne Bewaehrung — Vollstreckung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`freiheitsstrafe-strafmass-geldstrafe`](skills/freiheitsstrafe-strafmass-geldstrafe/SKILL.md) | Wenn es um Freiheitsstrafe — Strafmass prüfen in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`freiheitsstrafe-strafmass-pruefen`](skills/freiheitsstrafe-strafmass-pruefen/SKILL.md) | Wenn es um Freiheitsstrafe — Strafmass pruefen in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geldstrafe-grossen-rechtsmittel`](skills/geldstrafe-grossen-rechtsmittel/SKILL.md) | Wenn es um Geldstrafe: Zahlen, Schwellenwerte und Berechnung in Strafzumessung geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`geldstrafe-tagessatzanzahl-bestimmen`](skills/geldstrafe-tagessatzanzahl-bestimmen/SKILL.md) | Wenn es um Tagessatzanzahl der Geldstrafe — Paragraf 40 Abs. 1 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geldstrafe-vs-freiheitsstrafe-47-stgb`](skills/geldstrafe-vs-freiheitsstrafe-47-stgb/SKILL.md) | Wenn es um Geldstrafe vs. Freiheitsstrafe — Paragraf 47 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gesamtstrafenbildung-stgb-gestaendnis`](skills/gesamtstrafenbildung-stgb-gestaendnis/SKILL.md) | Wenn es um Gesamtstrafenbildung — Paragrafen 53 und 54 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gestaendnis-und-strafmilderung`](skills/gestaendnis-und-strafmilderung/SKILL.md) | Wenn es um Gestaendnis und Strafmilderung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`grossen-risikoampel-und-gegenargumente`](skills/grossen-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Großen: Risikoampel, Gegenargumente und Verteidigungslinien in Strafzumessung geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung`](skills/haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung/SKILL.md) | Wenn es um Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung in Strafzumessung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |
| [`iii-stpo-begruendungsanforderungen-strafurteil`](skills/iii-stpo-begruendungsanforderungen-strafurteil/SKILL.md) | Wenn es um Begruendung der Strafzumessung im Urteil — Paragraf 267 Abs. 3 StPO in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`jgg-jugendstrafe-minder-schwerer`](skills/jgg-jugendstrafe-minder-schwerer/SKILL.md) | Wenn es um Strafzumessung im Jugendstrafrecht in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Strafzumessung ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`minder-schwerer-fall-und-besonders-schwerer-fall`](skills/minder-schwerer-fall-und-besonders-schwerer-fall/SKILL.md) | Wenn es um Minder schwerer Fall und besonders schwerer Fall in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachtraegliche-gesamtstrafenbildung-55-stgb`](skills/nachtraegliche-gesamtstrafenbildung-55-stgb/SKILL.md) | Wenn es um Nachtraegliche Gesamtstrafenbildung — Paragraf 55 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`orientierung-triage-paragraph-stgb-besonders`](skills/orientierung-triage-paragraph-stgb-besonders/SKILL.md) | Wenn es um Strafzumessung — Orientierung und Triage in Strafzumessung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Strafzumessung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`paragraph-46-stgb-grundsatz-strafzumessung`](skills/paragraph-46-stgb-grundsatz-strafzumessung/SKILL.md) | Wenn es um Paragraf 46 StGB — Grundsatz der Strafzumessung in Strafzumessung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Strafzumessung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`rechtsmittel-und-gesamtstrafenfolgen`](skills/rechtsmittel-und-gesamtstrafenfolgen/SKILL.md) | Wenn es um Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwe... |
| [`regelbeispiele-rechtsprechung`](skills/regelbeispiele-rechtsprechung/SKILL.md) | Wenn es um Regelbeispiele in der Strafzumessung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regelbeispiele-stgb-strafbefehl`](skills/regelbeispiele-stgb-strafbefehl/SKILL.md) | Wenn es um Regelbeispiele: Internationaler Bezug und Schnittstellen in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`regelbeispiele-strafrahmenwahl`](skills/regelbeispiele-strafrahmenwahl/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`schwerer-fehlerkatalog`](skills/schwerer-fehlerkatalog/SKILL.md) | Wenn es um Schwerer Fehlerkatalog in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-grossen-risikoampel-und-gegenargumente`](skills/spezial-grossen-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Grossen: Risikoampel, Gegenargumente und Verteidigungslinien in Strafzumessung geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-schwerer-red-team-und-qualitaetskontrolle`](skills/spezial-schwerer-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Schwerer: Red-Team und Qualitätskontrolle in Strafzumessung geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-tagessatz-livequellen-und-rechtsprechungscheck`](skills/spezial-tagessatz-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Tagessatz: Livequellen- und Rechtsprechungscheck in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stgb-schriftsatz-brief-und-memo-bausteine`](skills/stgb-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Stgb: Schriftsatz-, Brief- und Memo-Bausteine in Strafzumessung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`strafbefehl-dokumentenmatrix-und-lueckenliste`](skills/strafbefehl-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Strafbefehl: Dokumentenmatrix, Lückenliste und Nachforderung in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`strafbefehl-stpo-strafmilderung-stgb`](skills/strafbefehl-stpo-strafmilderung-stgb/SKILL.md) | Wenn es um Strafzumessung im Strafbefehlsverfahren — Paragraf 407 StPO in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafkammer-strafzumessung`](skills/strafkammer-strafzumessung/SKILL.md) | Wenn es um Strafkammer: Behörden-, Gerichts- oder Registerweg in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafmilderung-49-stgb-zwingend-fakultativ`](skills/strafmilderung-49-stgb-zwingend-fakultativ/SKILL.md) | Wenn es um Strafmilderung — Paragraf 49 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafrahmen-und-strafzumessungsstufen`](skills/strafrahmen-und-strafzumessungsstufen/SKILL.md) | Wenn es um Strafrahmen und Strafzumessungsstufen in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafrecht-verfahrensstadium-strafbefehl`](skills/strafrecht-verfahrensstadium-strafbefehl/SKILL.md) | Wenn es um Strafrecht: Fristen, Form, Zuständigkeit und Rechtsweg in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafz-aufklaerungshilfe-kronzeuge`](skills/strafz-aufklaerungshilfe-kronzeuge/SKILL.md) | Wenn es um StrafZ: Aufklaerungshilfe in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafz-sicherungsverwahrung-spezial`](skills/strafz-sicherungsverwahrung-spezial/SKILL.md) | Wenn es um StrafZ: Sicherungsverwahrung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafz-strafrahmenmilderung-leitfaden`](skills/strafz-strafrahmenmilderung-leitfaden/SKILL.md) | Wenn es um StrafZ: Strafrahmenmilderung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafz-strafzumessungstatsachen`](skills/strafz-strafzumessungstatsachen/SKILL.md) | Wenn es um StrafZ: Tatsachen Bauleiter in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafzumessung-erstpruefung-und-mandatsziel`](skills/strafzumessung-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Strafzumessung: Erstprüfung, Rollenklärung und Mandatsziel in Strafzumessung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafzumessungs-tatsachen-46-ii-stgb`](skills/strafzumessungs-tatsachen-46-ii-stgb/SKILL.md) | Wenn es um Strafzumessungstatsachen — Paragraf 46 Abs. 2 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafzumessungstatsachen-vergleich-eskalation`](skills/strafzumessungstatsachen-vergleich-eskalation/SKILL.md) | Wenn es um Strafzumessungstatsachen: Verhandlung, Vergleich und Eskalation in Strafzumessung geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung`](skills/taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung/SKILL.md) | Wenn es um Taeter-Opfer-Ausgleich und Schadenswiedergutmachung — Paragraf 46a StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`tagessatz-quellenkarte`](skills/tagessatz-quellenkarte/SKILL.md) | Wenn es um Tagessatz Quellenkarte in Strafzumessung geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`tagessatzhoehe-40-ii-stgb-nettotagesverdienst`](skills/tagessatzhoehe-40-ii-stgb-nettotagesverdienst/SKILL.md) | Wenn es um Tagessatzhoehe — Paragraf 40 Abs. 2 StGB in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Strafzumessung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verfahrensstadium-strafbefehl-bis-kammer`](skills/verfahrensstadium-strafbefehl-bis-kammer/SKILL.md) | Wenn es um Strafzumessung vom Strafbefehl bis zur großen Strafkammer in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`verstaendigung-257c-stpo-strafzumessung`](skills/verstaendigung-257c-stpo-strafzumessung/SKILL.md) | Wenn es um Verstaendigung im Strafverfahren Paragraf 257c StPO und Strafzumessung in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Strafzumessung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Strafzumessung geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Strafzumessung geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
