# Berichtspflichten-Erlediger

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Berichtspflichten-Erlediger für mittelständische Unternehmen: amtliche Statistik, Portale, Umwelt-, Produkt-, Steuer-, Sozial-, Lieferketten-, Datenschutz- und Aufsichtsmeldungen mit Fristenboard, Datenquellen, Plausibilitätscheck und Behördenkommunikation.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/berichtspflichten-erlediger.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`berichtspflichten-erlediger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-werkstatt.md" download><code>berichtspflichten-erlediger-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-schnellstart.md" download><code>berichtspflichten-erlediger-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Praxisplugin für mittelständische Betriebe, die ihre Berichtspflichten nicht lieben müssen, sie aber elegant, fristgerecht und belegbar erledigen wollen. Es sammelt Pflichten aus Statistik, Steuer, Sozialversicherung, Umwelt, Produktrecht, Lieferkette, Datenschutz, Arbeitsschutz und Aufsicht in einem operativen Workflow.

## Leitplanke

Das Plugin ist kein Bürokratie-Jubelchor. Es hilft, Berichtspflichten zu vermeiden, wenn sie nicht bestehen, und sie sauber zu erledigen, wenn sie bestehen. Keine freiwillige Übererfüllung, keine Fantasiezahlen, keine Portalabgabe ohne menschliche Freigabe.

## Was dieses Plugin gut kann

- Pflichten schnell identifizieren: Muss ich wirklich melden, an wen, bis wann, mit welchen Daten?
- Fristen, Portale, Rollen, Datenquellen und Versandnachweise in ein Board bringen.
- Meldungen vorbereiten, plausibilisieren, freigeben und dokumentieren.
- Überzogene oder freiwillige Datenanforderungen höflich, aber bestimmt begrenzen.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`kaltstart-routing`](skills/kaltstart-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`abfallnachweis-nachwv-api-zugang`](skills/abfallnachweis-nachwv-api-zugang/SKILL.md), [`arbeitsschutz-unterweisung-nachweise`](skills/arbeitsschutz-unterweisung-nachweise/SKILL.md), [`datenminimierung-geheimnisschutz`](skills/datenminimierung-geheimnisschutz/SKILL.md), [`fuhrpark-telemetrie-datenschutz`](skills/fuhrpark-telemetrie-datenschutz/SKILL.md), [`maschinen-ce-konformitaetsakte`](skills/maschinen-ce-konformitaetsakte/SKILL.md), [`mindestlohndokumentation-arbeitszeit`](skills/mindestlohndokumentation-arbeitszeit/SKILL.md), [`nachweisordner-dokumentenmatrix`](skills/nachweisordner-dokumentenmatrix/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`battg-batterieregister-mengen`](skills/battg-batterieregister-mengen/SKILL.md), [`behoerdenkommunikation`](skills/behoerdenkommunikation/SKILL.md), [`berichtspflichten-register-und-fristenboard`](skills/berichtspflichten-register-und-fristenboard/SKILL.md), [`mutterschutz-gefaehrdungsbeurteilung`](skills/mutterschutz-gefaehrdungsbeurteilung/SKILL.md), [`transparenzregister-gwg-ubo`](skills/transparenzregister-gwg-ubo/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`csrd-esrs-lagebericht`](skills/csrd-esrs-lagebericht/SKILL.md), [`lksg-bafa-bericht`](skills/lksg-bafa-bericht/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`arbeitsunfall-dguv-audit-trail`](skills/arbeitsunfall-dguv-audit-trail/SKILL.md), [`audit-trail-freigabe`](skills/audit-trail-freigabe/SKILL.md), [`energieaudit-edl-entsendungen-a1-eudr`](skills/energieaudit-edl-entsendungen-a1-eudr/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`api-portal-zugang-rollen`](skills/api-portal-zugang-rollen/SKILL.md), [`ausland-tochter-emissionshandel-tehg`](skills/ausland-tochter-emissionshandel-tehg/SKILL.md), [`aussenhandel-intrastat-battg`](skills/aussenhandel-intrastat-battg/SKILL.md), [`baugenehmigung-baustatistik`](skills/baugenehmigung-baustatistik/SKILL.md), [`bauwirtschaft-soka-behg`](skills/bauwirtschaft-soka-behg/SKILL.md), [`behg-brennstoffemissionen`](skills/behg-brennstoffemissionen/SKILL.md), [`bundesbank-awv-z4-z5`](skills/bundesbank-awv-z4-z5/SKILL.md), [`bussgeld-vermeidung-heilung`](skills/bussgeld-vermeidung-heilung/SKILL.md), [`chemikalien-reach-csddd-vorschau-csrd`](skills/chemikalien-reach-csddd-vorschau-csrd/SKILL.md), [`csddd-vorschau-lieferkette`](skills/csddd-vorschau-lieferkette/SKILL.md), [`elektrog-ear-mengenmeldung`](skills/elektrog-ear-mengenmeldung/SKILL.md), [`emissionshandel-tehg-dehst`](skills/emissionshandel-tehg-dehst/SKILL.md), [`entsendungen-a1-mindestlohn`](skills/entsendungen-a1-mindestlohn/SKILL.md), [`eudr-entwaldung-due-diligence`](skills/eudr-entwaldung-due-diligence/SKILL.md), [`gefahrstoffverzeichnis-gefstoffv`](skills/gefahrstoffverzeichnis-gefstoffv/SKILL.md), [`geschaeftsfuehrer-dashboard`](skills/geschaeftsfuehrer-dashboard/SKILL.md), [`handwerk-gefahrstoffe-asbest`](skills/handwerk-gefahrstoffe-asbest/SKILL.md), [`hinweisgeberschutz-jahresreport-idev`](skills/hinweisgeberschutz-jahresreport-idev/SKILL.md), ... plus 21 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`abfallnachweis-nachwv-api-zugang`](skills/abfallnachweis-nachwv-api-zugang/SKILL.md) | Wenn es um Abfallnachweis und Entsorgung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`api-portal-zugang-rollen`](skills/api-portal-zugang-rollen/SKILL.md) | Wenn es um Portale, APIs und Rollen sicher verwalten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitsschutz-unterweisung-nachweise`](skills/arbeitsschutz-unterweisung-nachweise/SKILL.md) | Wenn es um Arbeitsschutz-Unterweisungen nachweisen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitsunfall-dguv-audit-trail`](skills/arbeitsunfall-dguv-audit-trail/SKILL.md) | Wenn es um Arbeitsunfallanzeige DGUV in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`audit-trail-freigabe`](skills/audit-trail-freigabe/SKILL.md) | Wenn es um Audit-Trail und Vier-Augen-Freigabe in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`ausland-tochter-emissionshandel-tehg`](skills/ausland-tochter-emissionshandel-tehg/SKILL.md) | Wenn es um Auslandstöchter und deutsche Berichtspflichten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- u... |
| [`aussenhandel-intrastat-battg`](skills/aussenhandel-intrastat-battg/SKILL.md) | Wenn es um Außenhandel und Intrastat in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`battg-batterieregister-mengen`](skills/battg-batterieregister-mengen/SKILL.md) | Wenn es um Batterierecht und Mengenmeldung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| [`baugenehmigung-baustatistik`](skills/baugenehmigung-baustatistik/SKILL.md) | Wenn es um Baugenehmigung und Baustatistik in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`bauwirtschaft-soka-behg`](skills/bauwirtschaft-soka-behg/SKILL.md) | Wenn es um Bauwirtschaft SOKA und Meldepflichten in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`behg-brennstoffemissionen`](skills/behg-brennstoffemissionen/SKILL.md) | Wenn es um BEHG Brennstoffemissionsbericht in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`behoerdenkommunikation`](skills/behoerdenkommunikation/SKILL.md) | Wenn es um Behördenkommunikation und Fristverlängerung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`berichtspflichten-register-und-fristenboard`](skills/berichtspflichten-register-und-fristenboard/SKILL.md) | Wenn es um Register und Fristenboard für Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bundesbank-awv-z4-z5`](skills/bundesbank-awv-z4-z5/SKILL.md) | Wenn es um Bundesbank AWV Z4/Z5 Meldungen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bussgeld-vermeidung-heilung`](skills/bussgeld-vermeidung-heilung/SKILL.md) | Wenn es um Bußgeldvermeidung und Heilung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`chemikalien-reach-csddd-vorschau-csrd`](skills/chemikalien-reach-csddd-vorschau-csrd/SKILL.md) | Wenn es um REACH/CLP Bericht und Stoffdaten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`csddd-vorschau-lieferkette`](skills/csddd-vorschau-lieferkette/SKILL.md) | Wenn es um CSDDD Vorschau und Lieferkettenbericht in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`csrd-esrs-lagebericht`](skills/csrd-esrs-lagebericht/SKILL.md) | Wenn es um CSRD/ESRS Nachhaltigkeitsbericht in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| [`datenminimierung-geheimnisschutz`](skills/datenminimierung-geheimnisschutz/SKILL.md) | Wenn es um Datenminimierung und Geheimnisschutz in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`elektrog-ear-mengenmeldung`](skills/elektrog-ear-mengenmeldung/SKILL.md) | Wenn es um ElektroG ear und Mengenmeldung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`emissionshandel-tehg-dehst`](skills/emissionshandel-tehg-dehst/SKILL.md) | Wenn es um TEHG Emissionsbericht und DEHSt in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`energieaudit-edl-entsendungen-a1-eudr`](skills/energieaudit-edl-entsendungen-a1-eudr/SKILL.md) | Wenn es um Energieaudit EDL-G und EnEfG-Schnittstelle in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`entsendungen-a1-mindestlohn`](skills/entsendungen-a1-mindestlohn/SKILL.md) | Wenn es um Entsendung, A1 und Mindestlohnmeldungen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`eudr-entwaldung-due-diligence`](skills/eudr-entwaldung-due-diligence/SKILL.md) | Wenn es um EUDR Entwaldungsfreie Lieferketten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fuhrpark-telemetrie-datenschutz`](skills/fuhrpark-telemetrie-datenschutz/SKILL.md) | Wenn es um Fuhrpark, Telemetrie und Meldedaten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gefahrstoffverzeichnis-gefstoffv`](skills/gefahrstoffverzeichnis-gefstoffv/SKILL.md) | Wenn es um Gefahrstoffverzeichnis und Arbeitsschutz in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`geschaeftsfuehrer-dashboard`](skills/geschaeftsfuehrer-dashboard/SKILL.md) | Wenn es um Geschäftsführer-Dashboard Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`handwerk-gefahrstoffe-asbest`](skills/handwerk-gefahrstoffe-asbest/SKILL.md) | Wenn es um Handwerk: Asbest, Gefahrstoffe und Anzeigen in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`hinweisgeberschutz-jahresreport-idev`](skills/hinweisgeberschutz-jahresreport-idev/SKILL.md) | Wenn es um HinSchG Reporting und Fallregister in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`idev-estatistik-core`](skills/idev-estatistik-core/SKILL.md) | Wenn es um IDEV und eSTATISTIK.core praktisch nutzen in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| [`immobilien-gebaeudeenergie-geg`](skills/immobilien-gebaeudeenergie-geg/SKILL.md) | Wenn es um Gebäudeenergie und GEG-Nachweise in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`jahresabschluss-bundesanzeiger-keine`](skills/jahresabschluss-bundesanzeiger-keine/SKILL.md) | Wenn es um Jahresabschluss und Offenlegung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Berichtspflichten Erlediger ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`kaltstart-routing`](skills/kaltstart-routing/SKILL.md) | Wenn es um Berichtspflichten: Kaltstart und Pflichtenscan in Berichtspflichten-Erlediger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`keine-pflicht-begruendet-ablehnen`](skills/keine-pflicht-begruendet-ablehnen/SKILL.md) | Wenn es um Keine Pflicht: sauber begründet ablehnen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ki-einsatz-lohnsteuer`](skills/ki-einsatz-lohnsteuer/SKILL.md) | Wenn es um digitale Werkzeuge zum Ausfüllen und Validieren nutzen in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständig... |
| [`konjunktur-und-produktionsstatistik`](skills/konjunktur-und-produktionsstatistik/SKILL.md) | Wenn es um Konjunktur- und Produktionsstatistik in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwei... |
| [`konzern-mutter-lebensmittel-haccp`](skills/konzern-mutter-lebensmittel-haccp/SKILL.md) | Wenn es um Konzernmatrix Mutter/Tochter in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`lebensmittel-haccp-rueckverfolgung`](skills/lebensmittel-haccp-rueckverfolgung/SKILL.md) | Wenn es um Lebensmittel: HACCP und Rückverfolgung in Berichtspflichten-Erlediger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| [`lksg-bafa-bericht`](skills/lksg-bafa-bericht/SKILL.md) | Wenn es um LkSG BAFA-Bericht und Risikoanalyse in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`lohnsteuer-sozialversicherung-meldungen`](skills/lohnsteuer-sozialversicherung-meldungen/SKILL.md) | Wenn es um Lohnsteuer und Sozialversicherung melden in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`lucid-verpackg-maschinen-ce`](skills/lucid-verpackg-maschinen-ce/SKILL.md) | Wenn es um LUCID Registrierung und Datenmeldung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| [`maschinen-ce-konformitaetsakte`](skills/maschinen-ce-konformitaetsakte/SKILL.md) | Wenn es um Maschinen CE und technische Dokumentation in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`mindestlohndokumentation-arbeitszeit`](skills/mindestlohndokumentation-arbeitszeit/SKILL.md) | Wenn es um Mindestlohn und Arbeitszeitdokumentation in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`mutterschutz-gefaehrdungsbeurteilung`](skills/mutterschutz-gefaehrdungsbeurteilung/SKILL.md) | Wenn es um Mutterschutz Gefährdungsbeurteilung und Meldung in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| [`nachweisordner-dokumentenmatrix`](skills/nachweisordner-dokumentenmatrix/SKILL.md) | Wenn es um Nachweisordner und Dokumentenmatrix in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`nis2-bsi-incident`](skills/nis2-bsi-incident/SKILL.md) | Wenn es um NIS2/BSI Incident Reporting in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`produktsicherheit-rueckruf-market`](skills/produktsicherheit-rueckruf-market/SKILL.md) | Wenn es um Produktsicherheit und Marktüberwachung melden in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`saisonkalender-mittelstand-stichprobe`](skills/saisonkalender-mittelstand-stichprobe/SKILL.md) | Wenn es um Saisonkalender Mittelstand in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schwerbehindertenanzeige-sgb-verpackg`](skills/schwerbehindertenanzeige-sgb-verpackg/SKILL.md) | Wenn es um Schwerbehindertenanzeige und Ausgleichsabgabe in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`statistik-anfrage-redteam`](skills/statistik-anfrage-redteam/SKILL.md) | Wenn es um Statistik-Anfrage Red-Team in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`stichprobe-und-befreiung-kleine-unternehmen`](skills/stichprobe-und-befreiung-kleine-unternehmen/SKILL.md) | Wenn es um Stichprobe, Schwelle und Entlastung kleiner Unternehmen in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrol... |
| [`transparenzregister-gwg-ubo`](skills/transparenzregister-gwg-ubo/SKILL.md) | Wenn es um Transparenzregister und wirtschaftlich Berechtigte in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweisc... |
| [`trinkwasser-legionellen-umsatzsteuer`](skills/trinkwasser-legionellen-umsatzsteuer/SKILL.md) | Wenn es um Trinkwasser und Legionellenmeldung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`umsatzsteuer-voranmeldung-elster`](skills/umsatzsteuer-voranmeldung-elster/SKILL.md) | Wenn es um Umsatzsteuer-Voranmeldung und ELSTER in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verdienststatistik-verdstatg`](skills/verdienststatistik-verdstatg/SKILL.md) | Wenn es um Verdienststatistik und Entgeltdaten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| [`verpackg-vollstaendigkeitserklaerung`](skills/verpackg-vollstaendigkeitserklaerung/SKILL.md) | Wenn es um VerpackG Vollständigkeitserklärung in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`wp-stb-koordination`](skills/wp-stb-koordination/SKILL.md) | Wenn es um WP/StB-Koordination bei Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
