# Strafbefehl-Verteidiger

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/strafbefehl-verteidiger.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafbefehl-verteidiger/strafbefehl-verteidiger-werkstatt.md" download><code>strafbefehl-verteidiger-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/strafbefehl-verteidiger/strafbefehl-verteidiger-schnellstart.md" download><code>strafbefehl-verteidiger-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren](../testakten/lumen-studios-insolvenz-strafverfahren/README.md) | [Gesamt-PDF](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) | [`testakte-lumen-studios-insolvenz-strafverfahren-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren-einzelpdfs.zip) |
| [Strafbefehl – Ladendiebstahl und Fahrerflucht](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/README.md) | [Gesamt-PDF](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/gesamt-pdf/strafbefehl-ladendiebstahl-fahrerflucht_gesamt.pdf) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du einen Strafbefehl verteidigen: Einspruchsfrist, Beschränkung, Akteneinsicht, Tagessätze, Fahrverbot, Nebenfolgen, Beweisrisiko und Hauptverhandlungstaktik.
Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-kommandocenter` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-polizeifilmerei-201-kug` - Film-, Foto- und Tonaufnahmen von Polizeieinsätzen
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`strafbefehls-erstpruefung-und-mandatsziel`](skills/strafbefehls-erstpruefung-und-mandatsziel/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`aktenanlage-fehlerkatalog`](skills/aktenanlage-fehlerkatalog/SKILL.md), [`akteneinsicht-behoerden-gericht-und-registerweg`](skills/akteneinsicht-behoerden-gericht-und-registerweg/SKILL.md), [`deal-beweislast-einspruch`](skills/deal-beweislast-einspruch/SKILL.md), [`pflichtverteidigung-quellenkarte`](skills/pflichtverteidigung-quellenkarte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck`](skills/spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck/SKILL.md), [`strafbefehl-aktenanlage`](skills/strafbefehl-aktenanlage/SKILL.md), [`strafbefehl-akteneinsicht-147`](skills/strafbefehl-akteneinsicht-147/SKILL.md), [`strafbefehl-dokumentenmatrix-und-lueckenliste`](skills/strafbefehl-dokumentenmatrix-und-lueckenliste/SKILL.md), [`strafbefehl-einspruch-aktenanlage`](skills/strafbefehl-einspruch-aktenanlage/SKILL.md), [`strafbefehl-quality-gate-akteneinsicht`](skills/strafbefehl-quality-gate-akteneinsicht/SKILL.md), [`strafbefehl-rechtsprechungsrecherche`](skills/strafbefehl-rechtsprechungsrecherche/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`verteidiger-formular-portal-und-einreichung`](skills/verteidiger-formular-portal-und-einreichung/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`einspruch-risikoampel-und-gegenargumente`](skills/einspruch-risikoampel-und-gegenargumente/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`stbv-strafbefehl-pruefung-bauleiter`](skills/stbv-strafbefehl-pruefung-bauleiter/SKILL.md), [`strafbefehl-inhalt-409-pruefung`](skills/strafbefehl-inhalt-409-pruefung/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`einstellung-153a-hauptverhandlung`](skills/einstellung-153a-hauptverhandlung/SKILL.md), [`hauptverhandlung-international-schnittstellen`](skills/hauptverhandlung-international-schnittstellen/SKILL.md), [`strafbefehl-hauptverhandlung-vorbereitung`](skills/strafbefehl-hauptverhandlung-vorbereitung/SKILL.md), [`verteidigung-wiedereinsetzung-zeugenstrategie`](skills/verteidigung-wiedereinsetzung-zeugenstrategie/SKILL.md), [`zeugen-befragungsstrategie-strafbefehl`](skills/zeugen-befragungsstrategie-strafbefehl/SKILL.md), [`zeugenstrategie-mehrparteien-konflikt-und-interessen`](skills/zeugenstrategie-mehrparteien-konflikt-und-interessen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`einspruchsentscheidung-und-folgen`](skills/einspruchsentscheidung-und-folgen/SKILL.md), [`stbv-einspruch-strafbefehl-fahrerlaubnis`](skills/stbv-einspruch-strafbefehl-fahrerlaubnis/SKILL.md), [`strafbefehl-einspruch-beschraenkung`](skills/strafbefehl-einspruch-beschraenkung/SKILL.md), [`strafbefehl-fristen-einspruch`](skills/strafbefehl-fristen-einspruch/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md), [`spezial-aktenanlage-red-team-und-qualitaetskontrolle`](skills/spezial-aktenanlage-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`einstellung-fahrerlaubnis`](skills/einstellung-fahrerlaubnis/SKILL.md), [`fahrerlaubnis-mandantenentscheidung`](skills/fahrerlaubnis-mandantenentscheidung/SKILL.md), [`nebenfolgen-fahrerlaubnis-strafbefehl`](skills/nebenfolgen-fahrerlaubnis-strafbefehl/SKILL.md), [`nebenfolgen-strafbefehl-strafbefehls`](skills/nebenfolgen-strafbefehl-strafbefehls/SKILL.md), [`rechtsmittel-tagessaetze-geldstrafe`](skills/rechtsmittel-tagessaetze-geldstrafe/SKILL.md), [`stbv-fahrerlaubnis-bei-strafbefehl-spezial`](skills/stbv-fahrerlaubnis-bei-strafbefehl-spezial/SKILL.md), [`stbv-strafbefehl-abwesenheit-vertretung`](skills/stbv-strafbefehl-abwesenheit-vertretung/SKILL.md), [`stbv-strafbefehl-auslaendischer-mandant-spezial`](skills/stbv-strafbefehl-auslaendischer-mandant-spezial/SKILL.md), [`strafbefehl-abwesenheit-vertretung`](skills/strafbefehl-abwesenheit-vertretung/SKILL.md), [`strafbefehl-deal-verstaendigung`](skills/strafbefehl-deal-verstaendigung/SKILL.md), [`strafbefehl-einlassung-deal-verstaendigung`](skills/strafbefehl-einlassung-deal-verstaendigung/SKILL.md), [`strafbefehl-pflichtverteidiger`](skills/strafbefehl-pflichtverteidiger/SKILL.md), [`strafbefehl-polizeifilmerei-201-kug`](skills/strafbefehl-polizeifilmerei-201-kug/SKILL.md), [`strafbefehl-quality-gate`](skills/strafbefehl-quality-gate/SKILL.md), [`strafbefehl-tagessaetze-geldstrafe`](skills/strafbefehl-tagessaetze-geldstrafe/SKILL.md), [`strafbefehl-wiedereinsetzung`](skills/strafbefehl-wiedereinsetzung/SKILL.md), [`strafbefehl-zulaessigkeit-407`](skills/strafbefehl-zulaessigkeit-407/SKILL.md), [`tagessaetze-verstaendigung-sonderfall`](skills/tagessaetze-verstaendigung-sonderfall/SKILL.md), ... plus 2 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`aktenanlage-fehlerkatalog`](skills/aktenanlage-fehlerkatalog/SKILL.md) | Wenn es um Aktenanlage Fehlerkatalog in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`akteneinsicht-behoerden-gericht-und-registerweg`](skills/akteneinsicht-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Akteneinsicht: Behörden-, Gerichts- oder Registerweg in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Strafbefehl-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`deal-beweislast-einspruch`](skills/deal-beweislast-einspruch/SKILL.md) | Wenn es um Deal: Beweislast, Darlegungslast und Substantiierung in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einspruch-risikoampel-und-gegenargumente`](skills/einspruch-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Einspruch: Risikoampel, Gegenargumente und Verteidigungslinien in Strafbefehl-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einspruchsentscheidung-und-folgen`](skills/einspruchsentscheidung-und-folgen/SKILL.md) | Wenn es um Einspruchsentscheidung, Beschränkung und Nebenfolgen beim Strafbefehl in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- u... |
| [`einstellung-153a-hauptverhandlung`](skills/einstellung-153a-hauptverhandlung/SKILL.md) | Wenn es um Einstellung des Strafbefehlsverfahrens in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`einstellung-fahrerlaubnis`](skills/einstellung-fahrerlaubnis/SKILL.md) | Wenn es um Einstellung: Compliance-Dokumentation und Aktenvermerk in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Strafbefehl-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fahrerlaubnis-mandantenentscheidung`](skills/fahrerlaubnis-mandantenentscheidung/SKILL.md) | Wenn es um Fahrerlaubnis: Mandantenkommunikation und Entscheidungsvorlage in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hauptverhandlung-international-schnittstellen`](skills/hauptverhandlung-international-schnittstellen/SKILL.md) | Wenn es um Hauptverhandlung: Internationaler Bezug und Schnittstellen in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Strafbefehl Verteidiger ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`mandantenkommunikation-redteam-qualitygate`](skills/mandantenkommunikation-redteam-qualitygate/SKILL.md) | Wenn es um Mandantenkommunikation in Strafbefehl-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`nebenfolgen-fahrerlaubnis-strafbefehl`](skills/nebenfolgen-fahrerlaubnis-strafbefehl/SKILL.md) | Wenn es um Nebenfolgen Fahrerlaubnis im Strafbefehl in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nebenfolgen-strafbefehl-strafbefehls`](skills/nebenfolgen-strafbefehl-strafbefehls/SKILL.md) | Wenn es um Nebenfolgen: Verhandlung, Vergleich und Eskalation in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Strafbefehl-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`pflichtverteidigung-quellenkarte`](skills/pflichtverteidigung-quellenkarte/SKILL.md) | Wenn es um Pflichtverteidigung Quellenkarte in Strafbefehl-Verteidiger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechtsmittel-tagessaetze-geldstrafe`](skills/rechtsmittel-tagessaetze-geldstrafe/SKILL.md) | Wenn es um Rechtsmittel nach Urteil im Strafbefehlsverfahren in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-aktenanlage-red-team-und-qualitaetskontrolle`](skills/spezial-aktenanlage-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Aktenanlage: Red-Team und Qualitätskontrolle in Strafbefehl-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck`](skills/spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Pflichtverteidigung: Livequellen- und Rechtsprechungscheck in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Strafbefehl-Verteidiger — Allgemein in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`stbv-einspruch-strafbefehl-fahrerlaubnis`](skills/stbv-einspruch-strafbefehl-fahrerlaubnis/SKILL.md) | Wenn es um StBV: Einspruch Strafbefehl in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stbv-fahrerlaubnis-bei-strafbefehl-spezial`](skills/stbv-fahrerlaubnis-bei-strafbefehl-spezial/SKILL.md) | Wenn es um StBV: Fahrerlaubnis Strafbefehl in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stbv-strafbefehl-abwesenheit-vertretung`](skills/stbv-strafbefehl-abwesenheit-vertretung/SKILL.md) | Wenn es um StBV: Strafbefehl-Prüfung in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stbv-strafbefehl-auslaendischer-mandant-spezial`](skills/stbv-strafbefehl-auslaendischer-mandant-spezial/SKILL.md) | Wenn es um StBV: Strafbefehl Ausländer in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stbv-strafbefehl-pruefung-bauleiter`](skills/stbv-strafbefehl-pruefung-bauleiter/SKILL.md) | Wenn es um StBV: Strafbefehl-Pruefung in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-abwesenheit-vertretung`](skills/strafbefehl-abwesenheit-vertretung/SKILL.md) | Wenn es um Abwesenheit in der Hauptverhandlung — Paragraf 411 Abs. 2 StPO in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`strafbefehl-aktenanlage`](skills/strafbefehl-aktenanlage/SKILL.md) | Wenn es um Aktenanlage im Strafbefehlsverfahren in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-akteneinsicht-147`](skills/strafbefehl-akteneinsicht-147/SKILL.md) | Wenn es um Akteneinsicht im Strafbefehlsverfahren — Paragraf 147 StPO in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| [`strafbefehl-deal-verstaendigung`](skills/strafbefehl-deal-verstaendigung/SKILL.md) | Wenn es um Verstaendigung im Strafbefehlsverfahren — Paragraf 257c StPO in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-dokumentenmatrix-und-lueckenliste`](skills/strafbefehl-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Strafbefehl: Dokumentenmatrix, Lückenliste und Nachforderung in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`strafbefehl-einlassung-deal-verstaendigung`](skills/strafbefehl-einlassung-deal-verstaendigung/SKILL.md) | Wenn es um Beweis und Einlassung im Strafbefehlsverfahren in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-einspruch-aktenanlage`](skills/strafbefehl-einspruch-aktenanlage/SKILL.md) | Wenn es um Gegen: Fristen, Form, Zuständigkeit und Rechtsweg in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-einspruch-beschraenkung`](skills/strafbefehl-einspruch-beschraenkung/SKILL.md) | Wenn es um Beschraenkter Einspruch gegen den Strafbefehl — Paragraf 410 Abs. 2 StPO in Strafbefehl-Verteidiger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt m... |
| [`strafbefehl-fristen-einspruch`](skills/strafbefehl-fristen-einspruch/SKILL.md) | Wenn es um Frist und Einspruch nach Paragraf 410 StPO in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-hauptverhandlung-vorbereitung`](skills/strafbefehl-hauptverhandlung-vorbereitung/SKILL.md) | Wenn es um Hauptverhandlung nach Einspruch — Paragraf 411 StPO in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`strafbefehl-inhalt-409-pruefung`](skills/strafbefehl-inhalt-409-pruefung/SKILL.md) | Wenn es um Strafbefehlsinhalt prüfen — Paragraf 409 StPO in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-pflichtverteidiger`](skills/strafbefehl-pflichtverteidiger/SKILL.md) | Wenn es um Pflichtverteidiger im Strafbefehlsverfahren in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-polizeifilmerei-201-kug`](skills/strafbefehl-polizeifilmerei-201-kug/SKILL.md) | Wenn es um Strafbefehl Nach Polizeifilmerei in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-quality-gate`](skills/strafbefehl-quality-gate/SKILL.md) | Wenn es um Quality Gate — Strafbefehl-Mandat in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-quality-gate-akteneinsicht`](skills/strafbefehl-quality-gate-akteneinsicht/SKILL.md) | Wenn es um Strafbefehl-Verteidiger — Kommandocenter in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strafbefehl-rechtsprechungsrecherche`](skills/strafbefehl-rechtsprechungsrecherche/SKILL.md) | Wenn es um Rechtsprechungsrecherche im Strafbefehlsverfahren in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`strafbefehl-tagessaetze-geldstrafe`](skills/strafbefehl-tagessaetze-geldstrafe/SKILL.md) | Wenn es um Tagessaetze und Geldstrafe — Paragrafen 40 bis 43 StGB in Strafbefehl-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und A... |
| [`strafbefehl-wiedereinsetzung`](skills/strafbefehl-wiedereinsetzung/SKILL.md) | Wenn es um Wiedereinsetzung nach versaeumter Einspruchsfrist — Paragraf 44 StPO in Strafbefehl-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortsch... |
| [`strafbefehl-zulaessigkeit-407`](skills/strafbefehl-zulaessigkeit-407/SKILL.md) | Wenn es um Zulaessigkeit des Strafbefehls — Paragraf 407 StPO in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`strafbefehls-erstpruefung-und-mandatsziel`](skills/strafbefehls-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Strafbefehls: Erstprüfung, Rollenklärung und Mandatsziel in Strafbefehl-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`tagessaetze-verstaendigung-sonderfall`](skills/tagessaetze-verstaendigung-sonderfall/SKILL.md) | Wenn es um Tagessaetze: Schriftsatz-, Brief- und Memo-Bausteine in Strafbefehl-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anl... |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verstaendigung-sonderfall-und-edge-case`](skills/verstaendigung-sonderfall-und-edge-case/SKILL.md) | Wenn es um Verstaendigung: Sonderfall und Edge-Case-Prüfung in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verteidiger-formular-portal-und-einreichung`](skills/verteidiger-formular-portal-und-einreichung/SKILL.md) | Wenn es um Verteidiger: Formular, Portal und Einreichungslogik in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verteidigung-wiedereinsetzung-zeugenstrategie`](skills/verteidigung-wiedereinsetzung-zeugenstrategie/SKILL.md) | Wenn es um Verteidigung: Tatbestandsmerkmale, Beweisfragen und Beleglage in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`wiedereinsetzung-zahlen-schwellen-und-berechnung`](skills/wiedereinsetzung-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um Wiedereinsetzung: Zahlen, Schwellenwerte und Berechnung in Strafbefehl-Verteidiger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfra... |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Strafbefehl-Verteidiger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Strafbefehl-Verteidiger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Strafbefehl-Verteidiger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zeugen-befragungsstrategie-strafbefehl`](skills/zeugen-befragungsstrategie-strafbefehl/SKILL.md) | Wenn es um Zeugen-Befragungsstrategie in der Hauptverhandlung in Strafbefehl-Verteidiger geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`zeugenstrategie-mehrparteien-konflikt-und-interessen`](skills/zeugenstrategie-mehrparteien-konflikt-und-interessen/SKILL.md) | Wenn es um Zeugenstrategie: Mehrparteienkonflikt und Interessenmatrix in Strafbefehl-Verteidiger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
