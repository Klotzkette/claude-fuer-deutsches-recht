# Nachbarschaftsstreit-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/nachbarschaftsstreit-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`nachbarschaftsstreit-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/nachbarschaftsstreit-pruefer/nachbarschaftsstreit-pruefer-werkstatt.md" download><code>nachbarschaftsstreit-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/nachbarschaftsstreit-pruefer/nachbarschaftsstreit-pruefer-schnellstart.md" download><code>nachbarschaftsstreit-pruefer-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Nachbarschaftsstreit Rosengartenstraße](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/README.md) | [Gesamt-PDF](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/gesamt-pdf/nachbarschaftsstreit-horrorfall-rosengarten_gesamt.pdf) | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip) | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten-einzelpdfs.zip) |
| [Akte Wusterhagen: Mühlenstau, Chaussee und Aufopferung](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/README.md) | [Gesamt-PDF](../testakten/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung/gesamt-pdf/preussisches-landrecht-wusterhagen-muehlenstau-aufopferung_gesamt.pdf) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung.zip) | [`testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-preussisches-landrecht-wusterhagen-muehlenstau-aufopferung-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für Nachbarrecht und eskalierte Grundstückskonflikte: Überbau, Überhang, Äste und Wurzeln, Grenzbäume, Einfriedung, Zaun, Mauer, Hecke, Immissionen, Vertiefung, drohender Einsturz, Notweg, Hammerschlags- und Leiterrecht, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung, Klage und Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt strukturierte Prüfungen, Entwürfe und Workflows zur anwaltlichen Kontrolle. Landesnachbarrecht, Baumschutzsatzungen, Bebauungspläne und örtliche Satzungen müssen im konkreten Fall geprüft werden.

## Start

```
/nachbarschaftsstreit-pruefer:allgemein
```

Der Einstieg fragt in kurzer Zeit ab: Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Beweislage, bisherige Schreiben, gewünschter Ton und Ziel. Danach routet er zu den Spezialskills.

## Skills (20)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Fristen-/Gefahrenscan, Routing und Arbeitsplan |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme des Konflikts mit Bundesland, Grundstück, Beteiligten und Risiko |
| `akten-und-grundstuecksaufnahme` | Grundbuch, Liegenschaftskarte, Baulast, Dienstbarkeit, Fotos und Chronologie erfassen |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchsgrundlagen nach BGB und Landesrecht sortieren |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB, Widerspruch, Duldung, Rente, Abkauf |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, Wurzeln, Fristsetzung, Selbsthilfe nach § 910 BGB |
| `grenzbaum-und-grenzanlage` | Grenzbaum, Grenzsträucher und gemeinschaftliche Grenzanlagen §§ 921-923 BGB |
| `einfriedung-zaun-mauer-hecke` | Zaun, Mauer, Hecke, Kosten, Standort, Ortsüblichkeit und Landesrecht |
| `immissionen-laerm-geruch-rauch-licht` | Geräusche, Gerüche, Rauch, Licht, Erschütterungen, § 906 BGB |
| `vertiefung-baugrube-stuetzverlust` | Baugrube, Unterfangung, Stütze des Nachbargrundstücks, § 909 BGB |
| `drohender-einsturz-gefahranlage` | Gefährliche Anlagen und Einsturzrisiken, §§ 907, 908 BGB |
| `notweg-zufahrt-wegerecht` | Notweg, Zufahrt, Grunddienstbarkeit, Baulast, §§ 917, 918 BGB |
| `hammerschlags-und-leiterrecht` | Betreten des Nachbargrundstücks für Bau-/Instandhaltungsarbeiten nach Landesrecht |
| `landesnachbarrecht-router` | Bundesland auswählen und landesrechtliche Prüfmodule planen |
| `beweissicherung-ortstermin-fotos` | Ortstermin, Fotoplan, Messpunkte, Sachverständige und selbständiges Beweisverfahren |
| `selbsthilfe-und-eskalationsgrenzen` | Was darf man selbst tun, was nicht, und wann drohen Besitz-/Eigentumsverletzungen? |
| `aufforderungsschreiben-nachbar` | Sachliches, druckvolles Anspruchs- und Fristsetzungsschreiben |
| `einstweilige-verfuegung-und-klage` | Eilrechtsschutz, Unterlassung, Beseitigung, Duldung, Feststellung, Streitwert |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich, Nutzungsregelung, Rückschnittplan, Kosten- und Zugangslösung |
| `horrorfall-aktenauswertung` | Große unordentliche Nachbarschaftsakte auswerten und in Arbeitsstränge zerlegen |

## Quellenstand

Stand: 05/2026. Kernnormen: BGB §§ 903, 906-923, 823, 862, 1004; Landesnachbarrechtsgesetze und kommunale Satzungen nach Bundesland/Gemeinde.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-router`](skills/anschluss-router/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`kaltstart-abschlussprodukt-und-uebergabe`](skills/kaltstart-abschlussprodukt-und-uebergabe/SKILL.md), [`landesnachbarrecht-router`](skills/landesnachbarrecht-router/SKILL.md), [`nachbarrecht-erstpruefung-und-mandatsziel`](skills/nachbarrecht-erstpruefung-und-mandatsziel/SKILL.md), [`nachbarrecht-kaltstart-triage`](skills/nachbarrecht-kaltstart-triage/SKILL.md), [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`akten-und-grundstuecksaufnahme`](skills/akten-und-grundstuecksaufnahme/SKILL.md), [`aufforderung-beweise-red-grenzbaum`](skills/aufforderung-beweise-red-grenzbaum/SKILL.md), [`beweissicherung-ortstermin-fotos`](skills/beweissicherung-ortstermin-fotos/SKILL.md), [`fristennotiz-naechster-ueberbau-akten`](skills/fristennotiz-naechster-ueberbau-akten/SKILL.md), [`horrorfall-aktenauswertung`](skills/horrorfall-aktenauswertung/SKILL.md), [`immissionen-compliance-dokumentation-und-akte`](skills/immissionen-compliance-dokumentation-und-akte/SKILL.md), [`klage-beweislast-nachbarrecht`](skills/klage-beweislast-nachbarrecht/SKILL.md), [`mauer-quellenkarte`](skills/mauer-quellenkarte/SKILL.md), [`nachbarschaftsstreit-tatbestand-beweis-und-belege`](skills/nachbarschaftsstreit-tatbestand-beweis-und-belege/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-mauer-livequellen-und-rechtsprechungscheck`](skills/spezial-mauer-livequellen-und-rechtsprechungscheck/SKILL.md), [`spezial-ueberhang-dokumentenmatrix-und-lueckenliste`](skills/spezial-ueberhang-dokumentenmatrix-und-lueckenliste/SKILL.md), [`ueberhang-dokumentenmatrix-und-lueckenliste`](skills/ueberhang-dokumentenmatrix-und-lueckenliste/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`aeste-risikoampel-und-gegenargumente`](skills/aeste-risikoampel-und-gegenargumente/SKILL.md), [`anspruchslandkarte-bgb-aufforderungsschreiben`](skills/anspruchslandkarte-bgb-aufforderungsschreiben/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`nachbarschaftsstreit-fristen-risiko-mandant`](skills/nachbarschaftsstreit-fristen-risiko-mandant/SKILL.md), [`spezial-pruefer-fristennotiz-und-naechster-schritt`](skills/spezial-pruefer-fristennotiz-und-naechster-schritt/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`vergleich-mediation-nachbarschaftsfrieden`](skills/vergleich-mediation-nachbarschaftsfrieden/SKILL.md), [`vergleich-sonderfall-und-edge-case`](skills/vergleich-sonderfall-und-edge-case/SKILL.md), [`zaun-verhandlung-vergleich-und-eskalation`](skills/zaun-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`einstweilige-verfuegung-und-klage`](skills/einstweilige-verfuegung-und-klage/SKILL.md), [`grenzbaum-schriftsatz-brief-und-memo-bausteine`](skills/grenzbaum-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`ueberbau-fristen-form-und-zustaendigkeit`](skills/ueberbau-fristen-form-und-zustaendigkeit/SKILL.md), [`wurzeln-behoerden-gericht-und-registerweg`](skills/wurzeln-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`aufforderungsschreiben-nachbar`](skills/aufforderungsschreiben-nachbar/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md), [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`beweise-red-team-und-qualitaetskontrolle`](skills/beweise-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`drohender-einsturz-einfriedung-zaun`](skills/drohender-einsturz-einfriedung-zaun/SKILL.md), [`einfriedung-zaun-mauer-hecke`](skills/einfriedung-zaun-mauer-hecke/SKILL.md), [`grenzbaum-grenzanlage-hammerschlags`](skills/grenzbaum-grenzanlage-hammerschlags/SKILL.md), [`hammerschlags-und-leiterrecht`](skills/hammerschlags-und-leiterrecht/SKILL.md), [`hammerschlagsrecht-hecke-immissionen`](skills/hammerschlagsrecht-hecke-immissionen/SKILL.md), [`hecke-zahlen-schwellen-und-berechnung`](skills/hecke-zahlen-schwellen-und-berechnung/SKILL.md), [`immissionen-laerm-landesnachbarrecht`](skills/immissionen-laerm-landesnachbarrecht/SKILL.md), [`laermimmissionen-mediation-vorrang`](skills/laermimmissionen-mediation-vorrang/SKILL.md), [`nach-grenzbebauung-ueberhang-spezial`](skills/nach-grenzbebauung-ueberhang-spezial/SKILL.md), [`nach-mediation-vorrang-leitfaden`](skills/nach-mediation-vorrang-leitfaden/SKILL.md), [`nach-nachbarrechtsuebersicht-bauleiter`](skills/nach-nachbarrechtsuebersicht-bauleiter/SKILL.md), [`notweg-ueberhang-sonderfall-edge`](skills/notweg-ueberhang-sonderfall-edge/SKILL.md), [`notweg-zufahrt-selbsthilfe-eskalationsgrenzen`](skills/notweg-zufahrt-selbsthilfe-eskalationsgrenzen/SKILL.md), [`selbsthilfe-und-eskalationsgrenzen`](skills/selbsthilfe-und-eskalationsgrenzen/SKILL.md), [`ueberbau-ueberhang-aeste-mediation`](skills/ueberbau-ueberhang-aeste-mediation/SKILL.md), [`ueberhang-aeste-wurzeln`](skills/ueberhang-aeste-wurzeln/SKILL.md), [`vertiefung-baugrube-stuetzverlust`](skills/vertiefung-baugrube-stuetzverlust/SKILL.md), [`vertiefung-interessen-wurzeln-zaun`](skills/vertiefung-interessen-wurzeln-zaun/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`aeste-risikoampel-und-gegenargumente`](skills/aeste-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Aeste: Risikoampel, Gegenargumente und Verteidigungslinien in Nachbarschaftsstreit-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`akten-und-grundstuecksaufnahme`](skills/akten-und-grundstuecksaufnahme/SKILL.md) | Wenn es um Akten- und Grundstücksaufnahme in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`anschluss-router`](skills/anschluss-router/SKILL.md) | Wenn es um Nachbarschaftsstreit-Prüfer — Allgemein in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anspruchslandkarte-bgb-aufforderungsschreiben`](skills/anspruchslandkarte-bgb-aufforderungsschreiben/SKILL.md) | Wenn es um Anspruchslandkarte BGB-Nachbarrecht in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`aufforderung-beweise-red-grenzbaum`](skills/aufforderung-beweise-red-grenzbaum/SKILL.md) | Wenn es um Aufforderung: Mandantenkommunikation und Entscheidungsvorlage in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufforderungsschreiben-nachbar`](skills/aufforderungsschreiben-nachbar/SKILL.md) | Wenn es um Aufforderungsschreiben an den Nachbarn in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweise-red-team-und-qualitaetskontrolle`](skills/beweise-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Beweise: Red-Team und Qualitätskontrolle in Nachbarschaftsstreit-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweissicherung-ortstermin-fotos`](skills/beweissicherung-ortstermin-fotos/SKILL.md) | Wenn es um Beweissicherung, Ortstermin und Fotos in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drohender-einsturz-einfriedung-zaun`](skills/drohender-einsturz-einfriedung-zaun/SKILL.md) | Wenn es um Drohender Einsturz und gefährliche Anlage in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`einfriedung-zaun-mauer-hecke`](skills/einfriedung-zaun-mauer-hecke/SKILL.md) | Wenn es um Einfriedung, Zaun, Mauer und Hecke in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächst... |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Nachbarschaftsstreit-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstweilige-verfuegung-und-klage`](skills/einstweilige-verfuegung-und-klage/SKILL.md) | Wenn es um Einstweilige Verfügung und Klage in Nachbarschaftsstreit-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`fristennotiz-naechster-ueberbau-akten`](skills/fristennotiz-naechster-ueberbau-akten/SKILL.md) | Wenn es um Prüfer: Fristennotiz und nächster Schritt in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`grenzbaum-grenzanlage-hammerschlags`](skills/grenzbaum-grenzanlage-hammerschlags/SKILL.md) | Wenn es um Grenzbaum und Grenzanlage in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`grenzbaum-schriftsatz-brief-und-memo-bausteine`](skills/grenzbaum-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Grenzbaum: Schriftsatz-, Brief- und Memo-Bausteine in Nachbarschaftsstreit-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| [`hammerschlags-und-leiterrecht`](skills/hammerschlags-und-leiterrecht/SKILL.md) | Wenn es um Hammerschlags- und Leiterrecht in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| [`hammerschlagsrecht-hecke-immissionen`](skills/hammerschlagsrecht-hecke-immissionen/SKILL.md) | Wenn es um Hammerschlagsrecht: Formular, Portal und Einreichungslogik in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hecke-zahlen-schwellen-und-berechnung`](skills/hecke-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Hecke: Zahlen, Schwellenwerte und Berechnung in Nachbarschaftsstreit-Prüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`horrorfall-aktenauswertung`](skills/horrorfall-aktenauswertung/SKILL.md) | Wenn es um Horrorfall-Aktenauswertung in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`immissionen-compliance-dokumentation-und-akte`](skills/immissionen-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Immissionen: Compliance-Dokumentation und Aktenvermerk in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| [`immissionen-laerm-landesnachbarrecht`](skills/immissionen-laerm-landesnachbarrecht/SKILL.md) | Wenn es um Immissionen: Lärm, Geruch, Rauch, Licht in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Nachbarschaftsstreit Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-abschlussprodukt-und-uebergabe`](skills/kaltstart-abschlussprodukt-und-uebergabe/SKILL.md) | Wenn es um Kaltstart: Abschlussprodukt und Übergabe in Nachbarschaftsstreit-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`klage-beweislast-nachbarrecht`](skills/klage-beweislast-nachbarrecht/SKILL.md) | Wenn es um Klage: Beweislast, Darlegungslast und Substantiierung in Nachbarschaftsstreit-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung un... |
| [`laermimmissionen-mediation-vorrang`](skills/laermimmissionen-mediation-vorrang/SKILL.md) | Wenn es um Nach: Laermimmissionen in Nachbarschaftsstreit-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`landesnachbarrecht-router`](skills/landesnachbarrecht-router/SKILL.md) | Wenn es um Landesnachbarrecht-Router in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mauer-quellenkarte`](skills/mauer-quellenkarte/SKILL.md) | Wenn es um Mauer Quellenkarte in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`nach-grenzbebauung-ueberhang-spezial`](skills/nach-grenzbebauung-ueberhang-spezial/SKILL.md) | Wenn es um Nach: Grenzbebauung Überhang in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nach-mediation-vorrang-leitfaden`](skills/nach-mediation-vorrang-leitfaden/SKILL.md) | Wenn es um Nach: Mediation Gueteverfahren in Nachbarschaftsstreit-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`nach-nachbarrechtsuebersicht-bauleiter`](skills/nach-nachbarrechtsuebersicht-bauleiter/SKILL.md) | Wenn es um Nach: Nachbarrecht-Übersicht in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachbarrecht-erstpruefung-und-mandatsziel`](skills/nachbarrecht-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Nachbarrecht: Erstprüfung, Rollenklärung und Mandatsziel in Nachbarschaftsstreit-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachbarrecht-kaltstart-triage`](skills/nachbarrecht-kaltstart-triage/SKILL.md) | Wenn es um Nachbarrecht-Kaltstart-Triage in Nachbarschaftsstreit-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachbarschaftsstreit-fristen-risiko-mandant`](skills/nachbarschaftsstreit-fristen-risiko-mandant/SKILL.md) | Wenn es um Fristen- und Risikoampel in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nachbarschaftsstreit-tatbestand-beweis-und-belege`](skills/nachbarschaftsstreit-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Nachbarschaftsstreit: Tatbestandsmerkmale, Beweisfragen und Beleglage in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`notweg-ueberhang-sonderfall-edge`](skills/notweg-ueberhang-sonderfall-edge/SKILL.md) | Wenn es um Notweg: Internationaler Bezug und Schnittstellen in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`notweg-zufahrt-selbsthilfe-eskalationsgrenzen`](skills/notweg-zufahrt-selbsthilfe-eskalationsgrenzen/SKILL.md) | Wenn es um Notweg, Zufahrt und Wegerecht in Nachbarschaftsstreit-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Nachbarschaftsstreit-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`selbsthilfe-und-eskalationsgrenzen`](skills/selbsthilfe-und-eskalationsgrenzen/SKILL.md) | Wenn es um Selbsthilfe und Eskalationsgrenzen in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-mauer-livequellen-und-rechtsprechungscheck`](skills/spezial-mauer-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Mauer: Livequellen- und Rechtsprechungscheck in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-pruefer-fristennotiz-und-naechster-schritt`](skills/spezial-pruefer-fristennotiz-und-naechster-schritt/SKILL.md) | Wenn es um Pruefer: Fristennotiz und nächster Schritt in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-ueberhang-dokumentenmatrix-und-lueckenliste`](skills/spezial-ueberhang-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Ueberhang: Dokumentenmatrix, Lückenliste und Nachforderung in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ueberbau-fristen-form-und-zustaendigkeit`](skills/ueberbau-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Ueberbau: Fristen, Form, Zuständigkeit und Rechtsweg in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ueberbau-ueberhang-aeste-mediation`](skills/ueberbau-ueberhang-aeste-mediation/SKILL.md) | Wenn es um Überbau-Prüfung in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`ueberhang-aeste-wurzeln`](skills/ueberhang-aeste-wurzeln/SKILL.md) | Wenn es um Überhang, Äste und Wurzeln in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ueberhang-dokumentenmatrix-und-lueckenliste`](skills/ueberhang-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Überhang: Dokumentenmatrix, Lückenliste und Nachforderung in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vergleich-mediation-nachbarschaftsfrieden`](skills/vergleich-mediation-nachbarschaftsfrieden/SKILL.md) | Wenn es um Vergleich, Mediation und Nachbarschaftsfrieden in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`vergleich-sonderfall-und-edge-case`](skills/vergleich-sonderfall-und-edge-case/SKILL.md) | Wenn es um Vergleich: Sonderfall und Edge-Case-Prüfung in Nachbarschaftsstreit-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`vertiefung-baugrube-stuetzverlust`](skills/vertiefung-baugrube-stuetzverlust/SKILL.md) | Wenn es um Vertiefung Baugrube Stuetzverlust in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vertiefung-interessen-wurzeln-zaun`](skills/vertiefung-interessen-wurzeln-zaun/SKILL.md) | Wenn es um Vertiefung: Mehrparteienkonflikt und Interessenmatrix in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-anschluss-skills-router`](skills/workflow-anschluss-skills-router/SKILL.md) | Wenn es um Anschluss-Skills Router in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Nachbarschaftsstreit-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-mandantenkommunikation`](skills/workflow-mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation in Nachbarschaftsstreit-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Nachbarschaftsstreit-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Nachbarschaftsstreit-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`wurzeln-behoerden-gericht-und-registerweg`](skills/wurzeln-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Wurzeln: Behörden-, Gerichts- oder Registerweg in Nachbarschaftsstreit-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zaun-verhandlung-vergleich-und-eskalation`](skills/zaun-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Zaun: Verhandlung, Vergleich und Eskalation in Nachbarschaftsstreit-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
