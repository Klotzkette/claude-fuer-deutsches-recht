# Verbraucher im Rechtsstaat Alltag

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Kleines, hilfreiches Plugin für Verbraucher: E-Commerce, Kaufrecht, Reparaturen, kleine Dienstleistungen, Rechnungen, Inkasso, Plattformen, Behördenbriefe und Gerichtspost verständlich einordnen und vorsichtig reagieren.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/verbraucher-rechtsstaat-alltag.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`verbraucher-rechtsstaat-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucher-rechtsstaat-alltag.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/verbraucher-rechtsstaat-alltag/verbraucher-rechtsstaat-alltag-werkstatt.md" download><code>verbraucher-rechtsstaat-alltag-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/verbraucher-rechtsstaat-alltag/verbraucher-rechtsstaat-alltag-schnellstart.md" download><code>verbraucher-rechtsstaat-alltag-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Kaufrecht — Wallbox, Firmware und Lastmanagement in Essen](../testakten/kaufrecht-wallbox-firmware-lastmanagement-essen/README.md) | [Gesamt-PDF](../testakten/kaufrecht-wallbox-firmware-lastmanagement-essen/gesamt-pdf/kaufrecht-wallbox-firmware-lastmanagement-essen_gesamt.pdf) | [`testakte-kaufrecht-wallbox-firmware-lastmanagement-essen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kaufrecht-wallbox-firmware-lastmanagement-essen.zip) | [`testakte-kaufrecht-wallbox-firmware-lastmanagement-essen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kaufrecht-wallbox-firmware-lastmanagement-essen-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Kleines, hilfreiches Plugin für Verbraucher: E-Commerce, Kaufrecht, Reparaturen, kleine Dienstleistungen, Rechnungen, Inkasso, Plattformen, Behördenbriefe und Gerichtspost verständlich einordnen und vorsichtig reagieren.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## Installation

ZIP aus dem aktuellen Release laden und in Plugin-Umgebung oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`dokumentenintake-und-aktenlog`](skills/dokumentenintake-und-aktenlog/SKILL.md), [`kaltstart-routing`](skills/kaltstart-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`behoerdenformular-verstehen-bescheid`](skills/behoerdenformular-verstehen-bescheid/SKILL.md), [`datenschutz-auskunft-loeschung`](skills/datenschutz-auskunft-loeschung/SKILL.md), [`kleiner-kauf-konto-gesperrt-mandanten`](skills/kleiner-kauf-konto-gesperrt-mandanten/SKILL.md), [`konto-gesperrt-bank`](skills/konto-gesperrt-bank/SKILL.md), [`paket-verloren-plattformkonto-sperre-probeabo`](skills/paket-verloren-plattformkonto-sperre-probeabo/SKILL.md), [`plattformkonto-sperre`](skills/plattformkonto-sperre/SKILL.md), [`quellen-rspr-fristen`](skills/quellen-rspr-fristen/SKILL.md), [`rechnung-quittung-beleg`](skills/rechnung-quittung-beleg/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`gerichtspost-familiengericht-laiencheck`](skills/gerichtspost-familiengericht-laiencheck/SKILL.md), [`gerichtspost-laiencheck`](skills/gerichtspost-laiencheck/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`online-bewertung-abmahnung`](skills/online-bewertung-abmahnung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`vergleichsangebot-pruefen`](skills/vergleichsangebot-pruefen/SKILL.md), [`vertrag-unterschrieben-abo-falle`](skills/vertrag-unterschrieben-abo-falle/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`baubehoerde-nachbarbrief`](skills/baubehoerde-nachbarbrief/SKILL.md), [`bescheid-brief-verstehen`](skills/bescheid-brief-verstehen/SKILL.md), [`frist-und-zustaendigkeit-cockpit`](skills/frist-und-zustaendigkeit-cockpit/SKILL.md), [`fristkalender-laie`](skills/fristkalender-laie/SKILL.md), [`gerichtlicher-mahnbescheid-laie`](skills/gerichtlicher-mahnbescheid-laie/SKILL.md), [`inkasso-mahnung-vollstreckung`](skills/inkasso-mahnung-vollstreckung/SKILL.md), [`kindergeld-kinderzuschlag-bescheid`](skills/kindergeld-kinderzuschlag-bescheid/SKILL.md), [`schriftsatz-vermerk-und-mustertext`](skills/schriftsatz-vermerk-und-mustertext/SKILL.md), [`schulbehoerde-ordnungsmassnahme`](skills/schulbehoerde-ordnungsmassnahme/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`inkasso-brief-erste-hilfe`](skills/inkasso-brief-erste-hilfe/SKILL.md), [`jugendamt-schreiben-verstehen`](skills/jugendamt-schreiben-verstehen/SKILL.md), [`mandanten-oder-beteiligtenkommunikation`](skills/mandanten-oder-beteiligtenkommunikation/SKILL.md), [`reise-flug-reparatur-statt-vermerk-mustertext`](skills/reise-flug-reparatur-statt-vermerk-mustertext/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`red-team-qualitygate`](skills/red-team-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abo-falle-kuendigung`](skills/abo-falle-kuendigung/SKILL.md), [`abo-kuendigung-fitness-streaming`](skills/abo-kuendigung-fitness-streaming/SKILL.md), [`arzt-rechnung-bankentgelte-zustimmungsfiktion`](skills/arzt-rechnung-bankentgelte-zustimmungsfiktion/SKILL.md), [`bankentgelte-zustimmungsfiktion`](skills/bankentgelte-zustimmungsfiktion/SKILL.md), [`ecommerce-kauf-fahrradreparatur`](skills/ecommerce-kauf-fahrradreparatur/SKILL.md), [`entscheidungsvorlage`](skills/entscheidungsvorlage/SKILL.md), [`fahrradreparatur-dienstleistung`](skills/fahrradreparatur-dienstleistung/SKILL.md), [`fahrradreparatur-nachbesserung-fake-shop`](skills/fahrradreparatur-nachbesserung-fake-shop/SKILL.md), [`fake-shop-und-chargeback`](skills/fake-shop-und-chargeback/SKILL.md), [`fitnessstudio-rueckzahlung-schliessung`](skills/fitnessstudio-rueckzahlung-schliessung/SKILL.md), [`garantie-vs-gebrauchtkauf-privat`](skills/garantie-vs-gebrauchtkauf-privat/SKILL.md), [`gebrauchtkauf-privat-maengel`](skills/gebrauchtkauf-privat-maengel/SKILL.md), [`handwerkerrechnung-zu-hoch`](skills/handwerkerrechnung-zu-hoch/SKILL.md), [`hotel-maengel-inkasso-erste-mahnung`](skills/hotel-maengel-inkasso-erste-mahnung/SKILL.md), [`inkassokosten-konzerninkasso-jugendamt`](skills/inkassokosten-konzerninkasso-jugendamt/SKILL.md), [`kita-platz-kleinanzeige-betrug-kleine`](skills/kita-platz-kleinanzeige-betrug-kleine/SKILL.md), [`kleinanzeige-betrug`](skills/kleinanzeige-betrug/SKILL.md), [`kleine-dienstleistung-schlecht`](skills/kleine-dienstleistung-schlecht/SKILL.md), ... plus 19 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 67 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abo-falle-kuendigung`](skills/abo-falle-kuendigung/SKILL.md) | Prüft eine behauptete Abo-Falle vom Bestellbutton bis zur Kündigung: liest Bestätigung, Preis-, Laufzeit- und Widerrufsinformation, trennt fehlenden Vertragsschluss, Widerruf, Kündigung und Rückzahlung, verarbeitet EuGH C-249/21 und C-56... |
| [`abo-kuendigung-fitness-streaming`](skills/abo-kuendigung-fitness-streaming/SKILL.md) | Bearbeitet Kündigung und Zahlungsstreit bei Fitnessstudio- und Streaming-Abos: trennt Nutzungsausfall, Probephase, Laufzeit, automatische Verlängerung, Kündigungsbutton und Inkasso, prüft BGH XII ZR 64/21 sowie EuGH C-249/21 und C-565/22... |
| [`arzt-rechnung-bankentgelte-zustimmungsfiktion`](skills/arzt-rechnung-bankentgelte-zustimmungsfiktion/SKILL.md) | Prüft eine private Arztrechnung für einen Patienten: ordnet jede GOÄ-Position, Faktorbegründung, Analogbewertung, Auslage und Honorarvereinbarung der erbrachten Leistung zu, trennt Fälligkeit von Erstattungsfragen und liefert Rechnungspr... |
| [`bankentgelte-zustimmungsfiktion`](skills/bankentgelte-zustimmungsfiktion/SKILL.md) | Prüft und beziffert Rückforderungen nach unwirksamer Zustimmungsfiktion bei Bankentgelten: rekonstruiert Preisverzeichnisse, Änderungsmitteilungen, ausdrückliche Zustimmung, Belastungen und Verjährung, verarbeitet BGH XI ZR 26/20, XI ZR... |
| [`baubehoerde-nachbarbrief`](skills/baubehoerde-nachbarbrief/SKILL.md) | Erstellt einen belastbaren Nachbarbrief an die Baubehörde: liest Baugenehmigung, Bekanntgabe, Pläne, Lageplan und Fotos zuerst, trennt bloße Rechtswidrigkeit von drittschützender Norm, prüft Akteneinsicht, Klage- und Eilrechtsschutz und... |
| [`behoerdenformular-verstehen-bescheid`](skills/behoerdenformular-verstehen-bescheid/SKILL.md) | Wenn es um Behördenformular verstehen in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bescheid-brief-verstehen`](skills/bescheid-brief-verstehen/SKILL.md) | Wenn es um Bescheid oder Brief verstehen in Verbraucher im Rechtsstaat Alltag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`datenschutz-auskunft-loeschung`](skills/datenschutz-auskunft-loeschung/SKILL.md) | Wenn es um Datenschutz Auskunft und Löschung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumentenintake-und-aktenlog`](skills/dokumentenintake-und-aktenlog/SKILL.md) | Wenn es um Dokumentenintake und Aktenlog in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ecommerce-kauf-fahrradreparatur`](skills/ecommerce-kauf-fahrradreparatur/SKILL.md) | Wenn es um E-Commerce Kauf und Widerruf in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`entscheidungsvorlage`](skills/entscheidungsvorlage/SKILL.md) | Wenn es um Entscheidungsvorlage in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fahrradreparatur-dienstleistung`](skills/fahrradreparatur-dienstleistung/SKILL.md) | Wenn es um Fahrradreparatur und kleine Dienstleistungen in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fahrradreparatur-nachbesserung-fake-shop`](skills/fahrradreparatur-nachbesserung-fake-shop/SKILL.md) | Wenn es um Fahrradreparatur und Nachbesserung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fake-shop-und-chargeback`](skills/fake-shop-und-chargeback/SKILL.md) | Wenn es um Fake-Shop und Chargeback in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fitnessstudio-rueckzahlung-schliessung`](skills/fitnessstudio-rueckzahlung-schliessung/SKILL.md) | Wenn es um Fitnessstudio Rückzahlung Schließung in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken un... |
| [`frist-und-zustaendigkeit-cockpit`](skills/frist-und-zustaendigkeit-cockpit/SKILL.md) | Wenn es um Fristen- und Zuständigkeitscockpit in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fristkalender-laie`](skills/fristkalender-laie/SKILL.md) | Wenn es um Fristkalender für Laien in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`garantie-vs-gebrauchtkauf-privat`](skills/garantie-vs-gebrauchtkauf-privat/SKILL.md) | Wenn es um Garantie versus Gewährleistung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gebrauchtkauf-privat-maengel`](skills/gebrauchtkauf-privat-maengel/SKILL.md) | Wenn es um Gebrauchtkauf privat mit Mängeln in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`gerichtlicher-mahnbescheid-laie`](skills/gerichtlicher-mahnbescheid-laie/SKILL.md) | Wenn es um Gerichtlicher Mahnbescheid für Laien in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gerichtspost-familiengericht-laiencheck`](skills/gerichtspost-familiengericht-laiencheck/SKILL.md) | Wenn es um Gerichtspost Familiengericht verstehen in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken... |
| [`gerichtspost-laiencheck`](skills/gerichtspost-laiencheck/SKILL.md) | Wenn es um Gerichtspost Laiencheck in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`handwerkerrechnung-zu-hoch`](skills/handwerkerrechnung-zu-hoch/SKILL.md) | Wenn es um Handwerkerrechnung zu hoch in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hotel-maengel-inkasso-erste-mahnung`](skills/hotel-maengel-inkasso-erste-mahnung/SKILL.md) | Wenn es um Hotelmängel und Bewertung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`inkasso-brief-erste-hilfe`](skills/inkasso-brief-erste-hilfe/SKILL.md) | Wenn es um Inkasso-Brief erste Hilfe in Verbraucher im Rechtsstaat Alltag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`inkasso-mahnung-vollstreckung`](skills/inkasso-mahnung-vollstreckung/SKILL.md) | Wenn es um Inkasso, Mahnung und Vollstreckung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`inkassokosten-konzerninkasso-jugendamt`](skills/inkassokosten-konzerninkasso-jugendamt/SKILL.md) | Wenn es um Inkassokosten Konzerninkasso Verzug in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| [`jugendamt-schreiben-verstehen`](skills/jugendamt-schreiben-verstehen/SKILL.md) | Wenn es um Jugendamt-Schreiben verstehen in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Verbraucher Rechtsstaat Alltag ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-routing`](skills/kaltstart-routing/SKILL.md) | Wenn es um Allgemeiner Kaltstart und Routing in Verbraucher im Rechtsstaat Alltag geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kindergeld-kinderzuschlag-bescheid`](skills/kindergeld-kinderzuschlag-bescheid/SKILL.md) | Wenn es um Kindergeld und Kinderzuschlag Bescheid in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kita-platz-kleinanzeige-betrug-kleine`](skills/kita-platz-kleinanzeige-betrug-kleine/SKILL.md) | Wenn es um Kita-Platz abgelehnt in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kleinanzeige-betrug`](skills/kleinanzeige-betrug/SKILL.md) | Wenn es um Kleinanzeige Betrug in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kleine-dienstleistung-schlecht`](skills/kleine-dienstleistung-schlecht/SKILL.md) | Wenn es um Kleine Dienstleistung schlecht in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwei... |
| [`kleiner-kauf-konto-gesperrt-mandanten`](skills/kleiner-kauf-konto-gesperrt-mandanten/SKILL.md) | Wenn es um Kleiner Kauf und Mängelrechte in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`konto-gesperrt-bank`](skills/konto-gesperrt-bank/SKILL.md) | Wenn es um Konto gesperrt durch Bank in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mandanten-oder-beteiligtenkommunikation`](skills/mandanten-oder-beteiligtenkommunikation/SKILL.md) | Wenn es um Beteiligtenkommunikation in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mietkaution-rueckzahlung-mitgliedschaft`](skills/mietkaution-rueckzahlung-mitgliedschaft/SKILL.md) | Wenn es um Mietkaution Rückzahlung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mitgliedschaft-verein-streit`](skills/mitgliedschaft-verein-streit/SKILL.md) | Wenn es um Mitgliedschaft im Verein Streit in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`nebenkostenabrechnung-verbraucher`](skills/nebenkostenabrechnung-verbraucher/SKILL.md) | Wenn es um Nebenkostenabrechnung Verbraucher in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`online-bestellbutton-zahlungspflicht`](skills/online-bestellbutton-zahlungspflicht/SKILL.md) | Wenn es um Online-Bestellbutton Und Zahlungspflicht in Verbraucher im Rechtsstaat Alltag geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`online-bewertung-abmahnung`](skills/online-bewertung-abmahnung/SKILL.md) | Wenn es um Online-Bewertung und Abmahnung in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| [`online-shop-liefert-nicht`](skills/online-shop-liefert-nicht/SKILL.md) | Wenn es um Online-Shop liefert nicht in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`paket-verloren-plattformkonto-sperre-probeabo`](skills/paket-verloren-plattformkonto-sperre-probeabo/SKILL.md) | Wenn es um Paket verloren oder beim Nachbarn in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`plattformkonto-sperre`](skills/plattformkonto-sperre/SKILL.md) | Wenn es um Plattformkonto gesperrt in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`probeabo-widerruf-kuendigung`](skills/probeabo-widerruf-kuendigung/SKILL.md) | Wenn es um Probeabo Widerruf Kündigung in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`protokoll-nachbereitung-rechnung`](skills/protokoll-nachbereitung-rechnung/SKILL.md) | Wenn es um Protokoll und Nachbereitung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-rspr-fristen`](skills/quellen-rspr-fristen/SKILL.md) | Wenn es um Quellen- und Rechtsprechungscheck in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechnung-ohne-auftrag`](skills/rechnung-ohne-auftrag/SKILL.md) | Wenn es um Rechnung ohne Auftrag in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`rechnung-quittung-beleg`](skills/rechnung-quittung-beleg/SKILL.md) | Wenn es um Rechnung, Quittung und Beleg in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`red-team-qualitygate`](skills/red-team-qualitygate/SKILL.md) | Wenn es um Red-Team-Qualitygate in Verbraucher im Rechtsstaat Alltag geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`reise-flug-reparatur-statt-vermerk-mustertext`](skills/reise-flug-reparatur-statt-vermerk-mustertext/SKILL.md) | Wenn es um Reise, Flug und Zug Problem in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`reparatur-statt-neukauf-right-to-repair`](skills/reparatur-statt-neukauf-right-to-repair/SKILL.md) | Wenn es um Reparatur statt Neukauf und Right to Repair in Verbraucher im Rechtsstaat Alltag geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`schriftsatz-vermerk-und-mustertext`](skills/schriftsatz-vermerk-und-mustertext/SKILL.md) | Wenn es um Schriftsatz, Vermerk und Mustertext in Verbraucher im Rechtsstaat Alltag geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schufa-eintrag-scoring-negativeintrag`](skills/schufa-eintrag-scoring-negativeintrag/SKILL.md) | Wenn es um SCHUFA-Eintrag prüfen in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schufa-scoring-negativeintrag-dsgvo`](skills/schufa-scoring-negativeintrag-dsgvo/SKILL.md) | Wenn es um SCHUFA Scoring Negativeintrag DSGVO in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schulbehoerde-ordnungsmassnahme`](skills/schulbehoerde-ordnungsmassnahme/SKILL.md) | Wenn es um Schulbehörde Ordnungsmaßnahme in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sitzungs-terminvorbereitung-strom-gas-telefon`](skills/sitzungs-terminvorbereitung-strom-gas-telefon/SKILL.md) | Wenn es um Sitzungs- und Terminvorbereitung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`strom-gas-preiserhoehung`](skills/strom-gas-preiserhoehung/SKILL.md) | Wenn es um Strom- und Gaspreiserhöhung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`telefon-internet-stoerung`](skills/telefon-internet-stoerung/SKILL.md) | Wenn es um Telefon und Internet Störung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unfall-fahrrad-verbraucherschlichtung`](skills/unfall-fahrrad-verbraucherschlichtung/SKILL.md) | Wenn es um Kleiner Unfall Fahrrad und Auto in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verbraucherschlichtung`](skills/verbraucherschlichtung/SKILL.md) | Wenn es um Verbraucherschlichtung in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vergleichsangebot-pruefen`](skills/vergleichsangebot-pruefen/SKILL.md) | Wenn es um Vergleichsangebot prüfen in Verbraucher im Rechtsstaat Alltag geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`versicherung-lehnt-vorladung-polizei-zahnarzt`](skills/versicherung-lehnt-vorladung-polizei-zahnarzt/SKILL.md) | Wenn es um Versicherung lehnt ab in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vertrag-unterschrieben-abo-falle`](skills/vertrag-unterschrieben-abo-falle/SKILL.md) | Wenn es um Vertrag unterschrieben und bereut in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vorladung-polizei-zeuge-beschuldigter`](skills/vorladung-polizei-zeuge-beschuldigter/SKILL.md) | Wenn es um Vorladung Polizei: Zeuge oder Beschuldigter in Verbraucher im Rechtsstaat Alltag geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits... |
| [`zahnarzt-kostenvoranschlag`](skills/zahnarzt-kostenvoranschlag/SKILL.md) | Wenn es um Zahnarzt Kostenvoranschlag in Verbraucher im Rechtsstaat Alltag geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
