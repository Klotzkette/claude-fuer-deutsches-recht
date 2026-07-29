# Vereinsrecht und Vereinsmanager

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Vereinsrechts- und Vereinsmanagement-Plugin für eingetragene und nicht eingetragene Vereine: Gründung, Satzung, Mitgliederversammlung, Vorstand, Protokolle, Beschlüsse, Gemeinnützigkeit, Register, Haftung, Datenschutz, Finanzen, Veranstaltungen und Spezialvereine.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/vereinsrecht-vereinsmanager.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`vereinsrecht-vereinsmanager.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vereinsrecht-vereinsmanager.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vereinsrecht-vereinsmanager/vereinsrecht-vereinsmanager-werkstatt.md" download><code>vereinsrecht-vereinsmanager-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vereinsrecht-vereinsmanager/vereinsrecht-vereinsmanager-schnellstart.md" download><code>vereinsrecht-vereinsmanager-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Vereinskasse, Sponsoring und Untreue Kassel](../testakten/strafrecht-untreue-vereinskasse-kassel/README.md) | [Gesamt-PDF](../testakten/strafrecht-untreue-vereinskasse-kassel/gesamt-pdf/strafrecht-untreue-vereinskasse-kassel_gesamt.pdf) | [`testakte-strafrecht-untreue-vereinskasse-kassel.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-untreue-vereinskasse-kassel.zip) | [`testakte-strafrecht-untreue-vereinskasse-kassel-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafrecht-untreue-vereinskasse-kassel-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Arbeitsplugin für Vereinsvorstände, Schriftführer, Kassenwarte, Gründergruppen und Mitglieder: vom Kegelclub bis zum großen gemeinnützigen Träger, vom nicht eingetragenen Verein bis zum e. V. und zum seltenen wirtschaftlichen Verein.

## Arbeitsidee

- Gründung, Satzung, Register, Vorstand, Mitgliederversammlung und Protokolle.
- Satzungsänderungen, Wahlen, Umlaufbeschlüsse, hybride und virtuelle Versammlungen.
- Gemeinnützigkeit, Spenden, Mittelverwendung, Zweckbetrieb und Finanzamt.
- Konflikte, Ausschluss, Haftung, Datenschutz, Veranstaltungen und Auflösung.
- Erzeugt Einladungen, Tagesordnungen, Beschlussvorschläge, Protokolle, Registeranmeldungs-Pakete und Rundbriefe.

## Quellenhygiene

Bundesrecht, Landesrecht, kommunale Satzungen, Parteisatzungen, Vereinsregisterpraxis, Wahlleiterhinweise und Formulare müssen bei echter Verwendung live geprüft werden. Keine Literatur- oder Datenbankfundstellen aus Modellwissen.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`datenschutz-mitgliederliste`](skills/datenschutz-mitgliederliste/SKILL.md), [`verein-dokumentenpaket-politik-social-media`](skills/verein-dokumentenpaket-politik-social-media/SKILL.md), [`verein-livequellen-check`](skills/verein-livequellen-check/SKILL.md), [`vereinsvermoegen-konto-versicherung-verein`](skills/vereinsvermoegen-konto-versicherung-verein/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`haftung-vorstand-ehrenamtspauschale`](skills/haftung-vorstand-ehrenamtspauschale/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`satzung-grundstruktur`](skills/satzung-grundstruktur/SKILL.md), [`veranstaltung-planen`](skills/veranstaltung-planen/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`anfechtung-beschluss`](skills/anfechtung-beschluss/SKILL.md), [`aufloesung-liquidation-beschlussvorlagen`](skills/aufloesung-liquidation-beschlussvorlagen/SKILL.md), [`beschlussvorlagen`](skills/beschlussvorlagen/SKILL.md), [`gemeinnuetzigkeit-antrag`](skills/gemeinnuetzigkeit-antrag/SKILL.md), [`registergericht-rueckfrage`](skills/registergericht-rueckfrage/SKILL.md), [`ruecklagen-mittelverwendung-rundbrief`](skills/ruecklagen-mittelverwendung-rundbrief/SKILL.md), [`transparenzregister-gwg-umlaufbeschluss`](skills/transparenzregister-gwg-umlaufbeschluss/SKILL.md), [`umlaufbeschluss`](skills/umlaufbeschluss/SKILL.md), [`verein-als-zweckbetrieb-anfechtung-beschluss`](skills/verein-als-zweckbetrieb-anfechtung-beschluss/SKILL.md), [`vorstandswahl-vorstandswechsel-register`](skills/vorstandswahl-vorstandswechsel-register/SKILL.md), [`vorstandswechsel-register`](skills/vorstandswechsel-register/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`rundbrief-mitglieder`](skills/rundbrief-mitglieder/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`verein-redteam-qualitygate`](skills/verein-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`delegierte-abteilungen-entlastung-vorstand`](skills/delegierte-abteilungen-entlastung-vorstand/SKILL.md), [`ehrenamtspauschale-uebungsleiter`](skills/ehrenamtspauschale-uebungsleiter/SKILL.md), [`entlastung-vorstand`](skills/entlastung-vorstand/SKILL.md), [`foerdermittel-verein`](skills/foerdermittel-verein/SKILL.md), [`foerderverein-schule-fusion-vereine`](skills/foerderverein-schule-fusion-vereine/SKILL.md), [`fusion-vereine`](skills/fusion-vereine/SKILL.md), [`geschaeftsordnung-vorstand-gruendung`](skills/geschaeftsordnung-vorstand-gruendung/SKILL.md), [`gruendung-eingetragener-verein`](skills/gruendung-eingetragener-verein/SKILL.md), [`gruendung-nicht-eingetragen`](skills/gruendung-nicht-eingetragen/SKILL.md), [`hilfsverein-wohlfahrt-hybride-virtuelle`](skills/hilfsverein-wohlfahrt-hybride-virtuelle/SKILL.md), [`hybride-virtuelle-versammlung`](skills/hybride-virtuelle-versammlung/SKILL.md), [`kassenwart-finanzen`](skills/kassenwart-finanzen/SKILL.md), [`kegelclub-freizeitverein-verein-kulturverein`](skills/kegelclub-freizeitverein-verein-kulturverein/SKILL.md), [`konflikt-im-verein`](skills/konflikt-im-verein/SKILL.md), [`kulturverein`](skills/kulturverein/SKILL.md), [`minderjaehrige-verein-mitgliederversammlung`](skills/minderjaehrige-verein-mitgliederversammlung/SKILL.md), [`mitgliederversammlung-einberufung`](skills/mitgliederversammlung-einberufung/SKILL.md), [`mitgliedsbeitraege`](skills/mitgliedsbeitraege/SKILL.md), ... plus 19 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`anfechtung-beschluss`](skills/anfechtung-beschluss/SKILL.md) | Wenn es um Beschlussmängel in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufloesung-liquidation-beschlussvorlagen`](skills/aufloesung-liquidation-beschlussvorlagen/SKILL.md) | Wenn es um Auflösung und Liquidation in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beschlussvorlagen`](skills/beschlussvorlagen/SKILL.md) | Wenn es um Beschlussvorlagen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`datenschutz-mitgliederliste`](skills/datenschutz-mitgliederliste/SKILL.md) | Wenn es um Datenschutz Mitgliederliste in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`delegierte-abteilungen-entlastung-vorstand`](skills/delegierte-abteilungen-entlastung-vorstand/SKILL.md) | Wenn es um Delegierte und Abteilungen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ehrenamtspauschale-uebungsleiter`](skills/ehrenamtspauschale-uebungsleiter/SKILL.md) | Wenn es um Ehrenamtspauschale und Übungsleiter in Vereinsrecht und Vereinsmanager geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`entlastung-vorstand`](skills/entlastung-vorstand/SKILL.md) | Wenn es um Entlastung Vorstand in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`foerdermittel-verein`](skills/foerdermittel-verein/SKILL.md) | Wenn es um Fördermittel Verein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`foerderverein-schule-fusion-vereine`](skills/foerderverein-schule-fusion-vereine/SKILL.md) | Wenn es um Förderverein Schule/Kita in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fusion-vereine`](skills/fusion-vereine/SKILL.md) | Wenn es um Fusion und Zusammenschluss in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gemeinnuetzigkeit-antrag`](skills/gemeinnuetzigkeit-antrag/SKILL.md) | Wenn es um Gemeinnützigkeit Antrag in Vereinsrecht und Vereinsmanager geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`geschaeftsordnung-vorstand-gruendung`](skills/geschaeftsordnung-vorstand-gruendung/SKILL.md) | Wenn es um Geschäftsordnung Vorstand in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gruendung-eingetragener-verein`](skills/gruendung-eingetragener-verein/SKILL.md) | Wenn es um Eingetragener Verein gründen in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`gruendung-nicht-eingetragen`](skills/gruendung-nicht-eingetragen/SKILL.md) | Wenn es um Nicht eingetragener Verein in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| [`haftung-vorstand-ehrenamtspauschale`](skills/haftung-vorstand-ehrenamtspauschale/SKILL.md) | Wenn es um Haftung Vorstand in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hilfsverein-wohlfahrt-hybride-virtuelle`](skills/hilfsverein-wohlfahrt-hybride-virtuelle/SKILL.md) | Wenn es um Hilfs- und Wohlfahrtsverein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hybride-virtuelle-versammlung`](skills/hybride-virtuelle-versammlung/SKILL.md) | Wenn es um Hybride und virtuelle Versammlung in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Vereinsrecht Vereinsmanager ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-triage`](skills/kaltstart-triage/SKILL.md) | Wenn es um Vereinsrecht — Allgemein in Vereinsrecht und Vereinsmanager geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`kassenwart-finanzen`](skills/kassenwart-finanzen/SKILL.md) | Wenn es um Kassenwart und Finanzen in Vereinsrecht und Vereinsmanager geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`kegelclub-freizeitverein-verein-kulturverein`](skills/kegelclub-freizeitverein-verein-kulturverein/SKILL.md) | Wenn es um Kegelclub/Freizeitverein in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Sch... |
| [`konflikt-im-verein`](skills/konflikt-im-verein/SKILL.md) | Wenn es um Konflikt im Verein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`kulturverein`](skills/kulturverein/SKILL.md) | Wenn es um Kulturverein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`minderjaehrige-verein-mitgliederversammlung`](skills/minderjaehrige-verein-mitgliederversammlung/SKILL.md) | Wenn es um Minderjährige im Verein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mitgliederversammlung-einberufung`](skills/mitgliederversammlung-einberufung/SKILL.md) | Wenn es um Mitgliederversammlung einberufen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mitgliedsbeitraege`](skills/mitgliedsbeitraege/SKILL.md) | Wenn es um Mitgliedsbeiträge in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mitgliedschaft-aufnahme-beendigung-notarielle`](skills/mitgliedschaft-aufnahme-beendigung-notarielle/SKILL.md) | Wenn es um Mitgliedschaft und Aufnahme in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mitgliedschaft-beendigung`](skills/mitgliedschaft-beendigung/SKILL.md) | Wenn es um Austritt, Streichung, Ausschluss in Vereinsrecht und Vereinsmanager geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`notarielle-anmeldung`](skills/notarielle-anmeldung/SKILL.md) | Wenn es um Notarielle Anmeldung in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ordnungen-verein-protokoll`](skills/ordnungen-verein-protokoll/SKILL.md) | Wenn es um Vereinsordnungen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`protokoll-mitgliederversammlung`](skills/protokoll-mitgliederversammlung/SKILL.md) | Wenn es um Protokoll Mitgliederversammlung in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| [`registergericht-rueckfrage`](skills/registergericht-rueckfrage/SKILL.md) | Wenn es um Registergericht Rückfrage in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ruecklagen-mittelverwendung-rundbrief`](skills/ruecklagen-mittelverwendung-rundbrief/SKILL.md) | Wenn es um Rücklagen und Mittelverwendung in Vereinsrecht und Vereinsmanager geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`rundbrief-mitglieder`](skills/rundbrief-mitglieder/SKILL.md) | Wenn es um Rundbrief an Mitglieder in Vereinsrecht und Vereinsmanager geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`satzung-grundstruktur`](skills/satzung-grundstruktur/SKILL.md) | Wenn es um Satzung Grundstruktur in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`satzungsaenderung-satzungszweck`](skills/satzungsaenderung-satzungszweck/SKILL.md) | Wenn es um Satzungsänderung in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`satzungszweck-gemeinnuetzigkeit`](skills/satzungszweck-gemeinnuetzigkeit/SKILL.md) | Wenn es um Satzungszweck und Gemeinnützigkeit in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nä... |
| [`sonderversammlung-minderheit`](skills/sonderversammlung-minderheit/SKILL.md) | Wenn es um Sonderversammlung Minderheit in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spenden-zuwendungsbestaetigung-sportverein`](skills/spenden-zuwendungsbestaetigung-sportverein/SKILL.md) | Wenn es um Spenden und Zuwendungsbestätigung in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sponsoring-und-werbung`](skills/sponsoring-und-werbung/SKILL.md) | Wenn es um Sponsoring und Werbung in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`sportverein`](skills/sportverein/SKILL.md) | Wenn es um Sportverein in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`tagesordnung-erstellen`](skills/tagesordnung-erstellen/SKILL.md) | Wenn es um Tagesordnung erstellen in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`transparenzregister-gwg-umlaufbeschluss`](skills/transparenzregister-gwg-umlaufbeschluss/SKILL.md) | Wenn es um Transparenzregister und GwG in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`umlaufbeschluss`](skills/umlaufbeschluss/SKILL.md) | Wenn es um Umlaufbeschluss in Vereinsrecht und Vereinsmanager geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`veranstaltung-planen`](skills/veranstaltung-planen/SKILL.md) | Wenn es um Veranstaltung planen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verein-als-zweckbetrieb-anfechtung-beschluss`](skills/verein-als-zweckbetrieb-anfechtung-beschluss/SKILL.md) | Wenn es um Verein als Arbeitgeber in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verein-dokumentenpaket-politik-social-media`](skills/verein-dokumentenpaket-politik-social-media/SKILL.md) | Wenn es um Vereins-Dokumentenpaket in Vereinsrecht und Vereinsmanager geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`verein-livequellen-check`](skills/verein-livequellen-check/SKILL.md) | Wenn es um Livequellen-Check Vereinsrecht in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verein-redteam-qualitygate`](skills/verein-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Vereinsrecht in Vereinsrecht und Vereinsmanager geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verein-und-politik`](skills/verein-und-politik/SKILL.md) | Wenn es um Verein und Politik in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verein-und-social-media`](skills/verein-und-social-media/SKILL.md) | Wenn es um Social Media im Verein in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vereinsvermoegen-konto-versicherung-verein`](skills/vereinsvermoegen-konto-versicherung-verein/SKILL.md) | Wenn es um Vereinsvermögen und Konto in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`versicherung-verein`](skills/versicherung-verein/SKILL.md) | Wenn es um Versicherungen in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`vorstand-rollen`](skills/vorstand-rollen/SKILL.md) | Wenn es um Vorstand und Rollen in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`vorstandswahl-vorstandswechsel-register`](skills/vorstandswahl-vorstandswechsel-register/SKILL.md) | Wenn es um Vorstandswahl in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`vorstandswechsel-register`](skills/vorstandswechsel-register/SKILL.md) | Wenn es um Vorstandswechsel Register in Vereinsrecht und Vereinsmanager geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`wirtschaftlicher-verein`](skills/wirtschaftlicher-verein/SKILL.md) | Wenn es um Wirtschaftlicher Verein in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`zweckaenderung`](skills/zweckaenderung/SKILL.md) | Wenn es um Zweckaenderung in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`zweckbetrieb`](skills/zweckbetrieb/SKILL.md) | Wenn es um Zweckbetrieb in Vereinsrecht und Vereinsmanager geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
