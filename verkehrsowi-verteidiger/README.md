# VerkehrsOWi-Verteidiger

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/verkehrsowi-verteidiger.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`verkehrsowi-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/verkehrsowi-verteidiger/verkehrsowi-verteidiger-werkstatt.md" download><code>verkehrsowi-verteidiger-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/verkehrsowi-verteidiger/verkehrsowi-verteidiger-schnellstart.md" download><code>verkehrsowi-verteidiger-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Norderhof-Tannenmoor — Abstandsverstoß Section Control BAB 7 Bispingen, Bußgeld und Fahrverbot](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/README.md) | [Gesamt-PDF](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/gesamt-pdf/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof_gesamt.pdf) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof-einzelpdfs.zip) |
| [VerkehrsOWi – Qualifizierter Rotlichtverstoß, Tempoüberschreitung und Fahrverbot](../testakten/verkehrsowi-rotlicht-tempo/README.md) | [Gesamt-PDF](../testakten/verkehrsowi-rotlicht-tempo/gesamt-pdf/verkehrsowi-rotlicht-tempo_gesamt.pdf) | [`testakte-verkehrsowi-rotlicht-tempo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo.zip) | [`testakte-verkehrsowi-rotlicht-tempo-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du eine Verkehrsordnungswidrigkeit verteidigen: Anhörung, Bußgeldbescheid, Messakte, Einspruch, Fahrverbot, Punkte, Verjährung, Beweisrisiken und Terminstrategie.
Ein freistehender Verteidigungsassistent für Verkehrsordnungswidrigkeiten: vom Anhörungsbogen über Einspruch, Akteneinsicht, Messakte und Punkte bis zur Amtsgerichtsverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `verkehrsowi-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `verkehrsowi-kommandocenter` - VerkehrsOWi-Kommandocenter
- `verkehrsowi-aktenanlage` - Aktenanlage und Dokumentenregister
- `verkehrsowi-anhoerung-bussgeldbescheid` - Anhörung und Bußgeldbescheid prüfen
- `verkehrsowi-fristen-einspruch` - Fristen und Einspruch
- `verkehrsowi-verjaehrung-zustellung` - Verjährung und Zustellung
- `verkehrsowi-akteneinsicht-messakte` - Akteneinsicht und Messakte
- `verkehrsowi-messverfahren-geschwindigkeit` - Geschwindigkeitsmessung
- `verkehrsowi-rotlicht-abstand-handy` - Rotlicht, Abstand und Handy
- `verkehrsowi-alkohol-drogen-24a` - Alkohol und Drogen nach § 24a StVG
- `verkehrsowi-fahreridentifizierung` - Fahreridentifizierung
- `verkehrsowi-punkte-fahrverbot-flensburg` - Punkte, Fahrverbot und Flensburg
- `verkehrsowi-haertefall-fahrverbot` - Härtefall beim Fahrverbot
- `verkehrsowi-beweisverwertung-standardisiert` - Beweisverwertung und Standardisierung
- `verkehrsowi-zeugen-polizei-strategie` - Zeugen- und Polizeibefragung
- `verkehrsowi-hauptverhandlung-amtsgericht` - Hauptverhandlung vor dem Amtsgericht
- `verkehrsowi-rechtsbeschwerde` - Rechtsbeschwerde
- `verkehrsowi-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `verkehrsowi-mandantenkommunikation` - Mandantenkommunikation
- `verkehrsowi-simulation-training` - Simulation und Training
- `verkehrsowi-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/verkehrsowi-mandatskarte.md` - VerkehrsOWi-Mandatskarte
- `assets/templates/frist-und-verjaehrung.md` - Fristen- und Verjährungsblatt
- `assets/templates/anhoerungsbogen-check.md` - Anhörungsbogen-Check
- `assets/templates/bussgeldbescheid-pruefung.md` - Bußgeldbescheid-Prüfung
- `assets/templates/einspruch-owig-67.md` - Einspruch nach § 67 OWiG
- `assets/templates/akteneinsicht-messakte.md` - Akteneinsicht und Messakte
- `assets/templates/messverfahren-checkliste.md` - Messverfahren-Checkliste
- `assets/templates/fahreridentifizierung.md` - Fahreridentifizierung
- `assets/templates/punkte-fahrverbot-matrix.md` - Punkte- und Fahrverbotsmatrix
- `assets/templates/haertefall-fahrverbot.md` - Härtefallpaket Fahrverbot
- `assets/templates/zeugen-polizei-fragenkatalog.md` - Zeugen- und Polizeifragen
- `assets/templates/hauptverhandlung-amtsgericht.md` - Hauptverhandlung Amtsgericht
- `assets/templates/rechtsbeschwerde-check.md` - Rechtsbeschwerde-Check
- `assets/templates/rechtsprechungsrecherche.md` - Rechtsprechungsrecherche
- `assets/templates/mandantenanschreiben.md` - Mandantenanschreiben
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/verkehrsowi-rotlicht-tempo`. Sie wird im Release als `testakte-verkehrsowi-rotlicht-tempo.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`verkehrsowi-erstpruefung-und-mandatsziel`](skills/verkehrsowi-erstpruefung-und-mandatsziel/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`abstand-quellenkarte`](skills/abstand-quellenkarte/SKILL.md), [`akteneinsicht-internationaler-bezug-und-schnittstellen`](skills/akteneinsicht-internationaler-bezug-und-schnittstellen/SKILL.md), [`alkohol-compliance-dokumentation-und-akte`](skills/alkohol-compliance-dokumentation-und-akte/SKILL.md), [`alkohol-drogen-beweisverwertung`](skills/alkohol-drogen-beweisverwertung/SKILL.md), [`bussgeldbescheid-tatbestand-beweis-und-belege`](skills/bussgeldbescheid-tatbestand-beweis-und-belege/SKILL.md), [`einspruch-dokumentenmatrix-und-lueckenliste`](skills/einspruch-dokumentenmatrix-und-lueckenliste/SKILL.md), [`hauptverhandlung-sonderfall-messakte-messung`](skills/hauptverhandlung-sonderfall-messakte-messung/SKILL.md), [`messakte-formular-portal-und-einreichung`](skills/messakte-formular-portal-und-einreichung/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-abstand-livequellen-und-rechtsprechungscheck`](skills/spezial-abstand-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`verkehrsowi-aktenanlage`](skills/verkehrsowi-aktenanlage/SKILL.md), [`verkehrsowi-akteneinsicht-messakte`](skills/verkehrsowi-akteneinsicht-messakte/SKILL.md), [`verkehrsowi-beweisverwertung-standardisiert`](skills/verkehrsowi-beweisverwertung-standardisiert/SKILL.md), [`verkehrsowi-rechtsprechungsrecherche`](skills/verkehrsowi-rechtsprechungsrecherche/SKILL.md), [`verteidiger-beweislast-verkehrsowi`](skills/verteidiger-beweislast-verkehrsowi/SKILL.md), [`vowi-akteneinsicht-rohmessdaten-leitfaden`](skills/vowi-akteneinsicht-rohmessdaten-leitfaden/SKILL.md), [`vowi-handyverstoss-akteneinsicht-alkohol`](skills/vowi-handyverstoss-akteneinsicht-alkohol/SKILL.md), ... plus 2 weitere |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`vowi-bussgeldbescheid-pruefung-bauleiter`](skills/vowi-bussgeldbescheid-pruefung-bauleiter/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`geschwindigkeit-verhandlung-vergleich-und-eskalation`](skills/geschwindigkeit-verhandlung-vergleich-und-eskalation/SKILL.md), [`verkehrsowi-hauptverhandlung-amtsgericht`](skills/verkehrsowi-hauptverhandlung-amtsgericht/SKILL.md), [`verkehrsowi-zeugen-polizei-strategie`](skills/verkehrsowi-zeugen-polizei-strategie/SKILL.md), [`zeugenstrategie-fehlerkatalog`](skills/zeugenstrategie-fehlerkatalog/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`amtsgericht-drogen-interessen-einspruch`](skills/amtsgericht-drogen-interessen-einspruch/SKILL.md), [`anhoerung-verkehrsowi-einspruch-messverfahren`](skills/anhoerung-verkehrsowi-einspruch-messverfahren/SKILL.md), [`rotlicht-schriftsatz-brief-und-memo-bausteine`](skills/rotlicht-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`spezial-anhoerung-fristen-form-und-zustaendigkeit`](skills/spezial-anhoerung-fristen-form-und-zustaendigkeit/SKILL.md), [`verkehrsowi-anhoerung-bussgeldbescheid`](skills/verkehrsowi-anhoerung-bussgeldbescheid/SKILL.md), [`verkehrsowi-fristen-einspruch`](skills/verkehrsowi-fristen-einspruch/SKILL.md), [`verkehrsowi-messverfahren-geschwindigkeit`](skills/verkehrsowi-messverfahren-geschwindigkeit/SKILL.md), [`vowi-bussgeldbescheid-verkehrsowi-quality`](skills/vowi-bussgeldbescheid-verkehrsowi-quality/SKILL.md), [`vowi-tempomessverfahren-bussgeldbescheid`](skills/vowi-tempomessverfahren-bussgeldbescheid/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md), [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md), [`spezial-zeugenstrategie-red-team-und-qualitaetskontrolle`](skills/spezial-zeugenstrategie-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`drogen-mehrparteien-konflikt-und-interessen`](skills/drogen-mehrparteien-konflikt-und-interessen/SKILL.md), [`fahrverbot-geschwindigkeit-handy`](skills/fahrverbot-geschwindigkeit-handy/SKILL.md), [`handy-zahlen-schwellen-und-berechnung`](skills/handy-zahlen-schwellen-und-berechnung/SKILL.md), [`messung-fahrverbot-punkte`](skills/messung-fahrverbot-punkte/SKILL.md), [`punkte-rotlicht-verkehrsowi`](skills/punkte-rotlicht-verkehrsowi/SKILL.md), [`simulation-training-verjaehrung-zustellung`](skills/simulation-training-verjaehrung-zustellung/SKILL.md), [`verkehrsowi-fahreridentifizierung`](skills/verkehrsowi-fahreridentifizierung/SKILL.md), [`verkehrsowi-haertefall-fahrverbot`](skills/verkehrsowi-haertefall-fahrverbot/SKILL.md), [`verkehrsowi-kommandocenter`](skills/verkehrsowi-kommandocenter/SKILL.md), [`verkehrsowi-punkte-fahrverbot`](skills/verkehrsowi-punkte-fahrverbot/SKILL.md), [`verkehrsowi-quality-gate`](skills/verkehrsowi-quality-gate/SKILL.md), [`verkehrsowi-rechtsbeschwerde`](skills/verkehrsowi-rechtsbeschwerde/SKILL.md), [`verkehrsowi-rotlicht-abstand-handy`](skills/verkehrsowi-rotlicht-abstand-handy/SKILL.md), [`verkehrsowi-verjaehrung-zustellung`](skills/verkehrsowi-verjaehrung-zustellung/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abstand-quellenkarte`](skills/abstand-quellenkarte/SKILL.md) | Wenn es um Abstand Quellenkarte in VerkehrsOWi-Verteidiger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`akteneinsicht-internationaler-bezug-und-schnittstellen`](skills/akteneinsicht-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Akteneinsicht: Internationaler Bezug und Schnittstellen in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfra... |
| [`alkohol-compliance-dokumentation-und-akte`](skills/alkohol-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Alkohol: Compliance-Dokumentation und Aktenvermerk in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| [`alkohol-drogen-beweisverwertung`](skills/alkohol-drogen-beweisverwertung/SKILL.md) | Wenn es um Alkohol und Drogen — Paragraf 24a StVG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`amtsgericht-drogen-interessen-einspruch`](skills/amtsgericht-drogen-interessen-einspruch/SKILL.md) | Wenn es um Amtsgericht: Mandantenkommunikation und Entscheidungsvorlage in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anhoerung-verkehrsowi-einspruch-messverfahren`](skills/anhoerung-verkehrsowi-einspruch-messverfahren/SKILL.md) | Wenn es um Anhörung: Fristen, Form, Zuständigkeit und Rechtsweg in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in VerkehrsOWi-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`bussgeldbescheid-tatbestand-beweis-und-belege`](skills/bussgeldbescheid-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Bussgeldbescheid: Tatbestandsmerkmale, Beweisfragen und Beleglage in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`drogen-mehrparteien-konflikt-und-interessen`](skills/drogen-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Drogen: Mehrparteienkonflikt und Interessenmatrix in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einspruch-dokumentenmatrix-und-lueckenliste`](skills/einspruch-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Einspruch: Dokumentenmatrix, Lückenliste und Nachforderung in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in VerkehrsOWi-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fahrverbot-geschwindigkeit-handy`](skills/fahrverbot-geschwindigkeit-handy/SKILL.md) | Wenn es um Fahrverbot: Behörden-, Gerichts- oder Registerweg in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geschwindigkeit-verhandlung-vergleich-und-eskalation`](skills/geschwindigkeit-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Geschwindigkeit: Verhandlung, Vergleich und Eskalation in VerkehrsOWi-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`handy-zahlen-schwellen-und-berechnung`](skills/handy-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Handy: Zahlen, Schwellenwerte und Berechnung in VerkehrsOWi-Verteidiger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`hauptverhandlung-sonderfall-messakte-messung`](skills/hauptverhandlung-sonderfall-messakte-messung/SKILL.md) | Wenn es um Hauptverhandlung: Sonderfall und Edge-Case-Prüfung in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Verkehrsowi Verteidiger ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`mandantenkommunikation`](skills/mandantenkommunikation/SKILL.md) | Wenn es um Mandantenkommunikation im OWi-Mandat in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md) | Wenn es um Mandantenkommunikation in VerkehrsOWi-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`messakte-formular-portal-und-einreichung`](skills/messakte-formular-portal-und-einreichung/SKILL.md) | Wenn es um Messakte: Formular, Portal und Einreichungslogik in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`messung-fahrverbot-punkte`](skills/messung-fahrverbot-punkte/SKILL.md) | Wenn es um Messung, Punkte, Fahrverbot und Verteidigungsziel im Verkehrs-OWi in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und N... |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in VerkehrsOWi-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`punkte-rotlicht-verkehrsowi`](skills/punkte-rotlicht-verkehrsowi/SKILL.md) | Wenn es um Punkte: Risikoampel, Gegenargumente und Verteidigungslinien in VerkehrsOWi-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in VerkehrsOWi-Verteidiger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`rotlicht-schriftsatz-brief-und-memo-bausteine`](skills/rotlicht-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Rotlicht: Schriftsatz-, Brief- und Memo-Bausteine in VerkehrsOWi-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlage... |
| [`simulation-training-verjaehrung-zustellung`](skills/simulation-training-verjaehrung-zustellung/SKILL.md) | Wenn es um Simulationstraining OWi-Mandate in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-abstand-livequellen-und-rechtsprechungscheck`](skills/spezial-abstand-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Abstand: Livequellen- und Rechtsprechungscheck in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-anhoerung-fristen-form-und-zustaendigkeit`](skills/spezial-anhoerung-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Anhoerung: Fristen, Form, Zuständigkeit und Rechtsweg in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-zeugenstrategie-red-team-und-qualitaetskontrolle`](skills/spezial-zeugenstrategie-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Zeugenstrategie: Red-Team und Qualitätskontrolle in VerkehrsOWi-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um VerkehrsOWi-Verteidiger — Allgemein in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-aktenanlage`](skills/verkehrsowi-aktenanlage/SKILL.md) | Wenn es um Aktenanlage OWi-Mandat in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-akteneinsicht-messakte`](skills/verkehrsowi-akteneinsicht-messakte/SKILL.md) | Wenn es um Akteneinsicht und Messakte im OWi-Verfahren in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-anhoerung-bussgeldbescheid`](skills/verkehrsowi-anhoerung-bussgeldbescheid/SKILL.md) | Wenn es um Anhörung und Bussgeldbescheid — Paragrafen 55 und 66 OWiG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-beweisverwertung-standardisiert`](skills/verkehrsowi-beweisverwertung-standardisiert/SKILL.md) | Wenn es um Standardisiertes Messverfahren und Beweisverwertung in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-erstpruefung-und-mandatsziel`](skills/verkehrsowi-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Verkehrsowi: Erstprüfung, Rollenklärung und Mandatsziel in VerkehrsOWi-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-fahreridentifizierung`](skills/verkehrsowi-fahreridentifizierung/SKILL.md) | Wenn es um Fahreridentifizierung im OWi-Verfahren in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-fristen-einspruch`](skills/verkehrsowi-fristen-einspruch/SKILL.md) | Wenn es um Einspruchsfrist und Einspruch — Paragraf 67 OWiG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-haertefall-fahrverbot`](skills/verkehrsowi-haertefall-fahrverbot/SKILL.md) | Wenn es um Haertefall-Argumentation beim Fahrverbot — Paragraf 25 StVG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-hauptverhandlung-amtsgericht`](skills/verkehrsowi-hauptverhandlung-amtsgericht/SKILL.md) | Wenn es um Hauptverhandlung OWi am Amtsgericht in VerkehrsOWi-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`verkehrsowi-kommandocenter`](skills/verkehrsowi-kommandocenter/SKILL.md) | Wenn es um VerkehrsOWi-Verteidiger — Kommandocenter in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-messverfahren-geschwindigkeit`](skills/verkehrsowi-messverfahren-geschwindigkeit/SKILL.md) | Wenn es um Geschwindigkeitsmessung OWi-Verfahren in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-punkte-fahrverbot`](skills/verkehrsowi-punkte-fahrverbot/SKILL.md) | Wenn es um Punkte und Fahrverbot — Fahreignungsregister Flensburg in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-quality-gate`](skills/verkehrsowi-quality-gate/SKILL.md) | Wenn es um Quality Gate — OWi-Mandat in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`verkehrsowi-rechtsbeschwerde`](skills/verkehrsowi-rechtsbeschwerde/SKILL.md) | Wenn es um Rechtsbeschwerde im OWi-Verfahren — Paragraf 79 OWiG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-rechtsprechungsrecherche`](skills/verkehrsowi-rechtsprechungsrecherche/SKILL.md) | Wenn es um Rechtsprechungsrecherche OWi-Verkehrsrecht in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-rotlicht-abstand-handy`](skills/verkehrsowi-rotlicht-abstand-handy/SKILL.md) | Wenn es um Rotlicht, Abstand und Handy — Paragrafen 23. 37. 4 StVO in VerkehrsOWi-Verteidiger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| [`verkehrsowi-verjaehrung-zustellung`](skills/verkehrsowi-verjaehrung-zustellung/SKILL.md) | Wenn es um Verfolgungsverjaehrung und Zustellungsmaengel — Paragraf 31 OWiG in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verkehrsowi-zeugen-polizei-strategie`](skills/verkehrsowi-zeugen-polizei-strategie/SKILL.md) | Wenn es um Polizeibeamten als Zeugen im OWi-Verfahren in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verteidiger-beweislast-verkehrsowi`](skills/verteidiger-beweislast-verkehrsowi/SKILL.md) | Wenn es um Verteidiger: Beweislast, Darlegungslast und Substantiierung in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vowi-akteneinsicht-rohmessdaten-leitfaden`](skills/vowi-akteneinsicht-rohmessdaten-leitfaden/SKILL.md) | Wenn es um Vowi Akteneinsicht Rohmessdaten Leitfaden in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`vowi-bussgeldbescheid-pruefung-bauleiter`](skills/vowi-bussgeldbescheid-pruefung-bauleiter/SKILL.md) | Wenn es um VOWi: Bussgeldbescheid-Pruefung in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vowi-bussgeldbescheid-verkehrsowi-quality`](skills/vowi-bussgeldbescheid-verkehrsowi-quality/SKILL.md) | Wenn es um VOWi: Bussgeldbescheid-Prüfung in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vowi-handyverstoss-akteneinsicht-alkohol`](skills/vowi-handyverstoss-akteneinsicht-alkohol/SKILL.md) | Wenn es um VOWi: Handyverstoss in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`vowi-tempomessverfahren-bussgeldbescheid`](skills/vowi-tempomessverfahren-bussgeldbescheid/SKILL.md) | Wenn es um VOWi: Tempomessverfahren in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in VerkehrsOWi-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in VerkehrsOWi-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in VerkehrsOWi-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zeugenstrategie-fehlerkatalog`](skills/zeugenstrategie-fehlerkatalog/SKILL.md) | Wenn es um Zeugenstrategie Fehlerkatalog in VerkehrsOWi-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
