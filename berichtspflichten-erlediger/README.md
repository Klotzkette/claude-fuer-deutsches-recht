# Berichtspflichten-Erlediger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berichtspflichten-erlediger`) | [`berichtspflichten-erlediger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Berichtspflichten-Erlediger für mittelständische Unternehmen: amtliche Statistik, Portale, Umwelt-, Produkt-, Steuer-, Sozial-, Lieferketten-, Datenschutz- und Aufsichtsmeldungen mit Fristenboard, Datenquellen, Plausibilitätscheck und Behördenkommunikation.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`berichtspflichten-erlediger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-werkstatt.md" download><code>berichtspflichten-erlediger-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-schnellstart.md" download><code>berichtspflichten-erlediger-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| 1. Einstieg und Fallrouting | `kaltstart-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `abfallnachweis-nachwv-api-zugang`, `arbeitsschutz-unterweisung-nachweise`, `datenminimierung-geheimnisschutz`, `fuhrpark-telemetrie-datenschutz`, `maschinen-ce-konformitaetsakte`, `mindestlohndokumentation-arbeitszeit`, `nachweisordner-dokumentenmatrix` |
| 5. Verfahren, Behörde und Gericht | `battg-batterieregister-mengen`, `behoerdenkommunikation`, `berichtspflichten-register-und-fristenboard`, `mutterschutz-gefaehrdungsbeurteilung`, `transparenzregister-gwg-ubo` |
| 6. Ergebnis, Schreiben und Kommunikation | `csrd-esrs-lagebericht`, `lksg-bafa-bericht` |
| 7. Kontrolle, Qualität und Gegenprüfung | `arbeitsunfall-dguv-audit-trail`, `audit-trail-freigabe`, `energieaudit-edl-entsendungen-a1-eudr` |
| 8. Spezialmodule und Schnittstellen | `api-portal-zugang-rollen`, `ausland-tochter-emissionshandel-tehg`, `aussenhandel-intrastat-battg`, `baugenehmigung-baustatistik`, `bauwirtschaft-soka-behg`, `behg-brennstoffemissionen`, `bundesbank-awv-z4-z5`, `bussgeld-vermeidung-heilung`, `chemikalien-reach-csddd-vorschau-csrd`, `csddd-vorschau-lieferkette`, `elektrog-ear-mengenmeldung`, `emissionshandel-tehg-dehst`, `entsendungen-a1-mindestlohn`, `eudr-entwaldung-due-diligence`, `gefahrstoffverzeichnis-gefstoffv`, `geschaeftsfuehrer-dashboard`, `handwerk-gefahrstoffe-asbest`, `hinweisgeberschutz-jahresreport-idev`, ... plus 21 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abfallnachweis-nachwv-api-zugang` | Wenn es um Abfallnachweis und Entsorgung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `api-portal-zugang-rollen` | Wenn es um Portale, APIs und Rollen sicher verwalten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitsschutz-unterweisung-nachweise` | Wenn es um Arbeitsschutz-Unterweisungen nachweisen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitsunfall-dguv-audit-trail` | Wenn es um Arbeitsunfallanzeige DGUV in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `audit-trail-freigabe` | Wenn es um Audit-Trail und Vier-Augen-Freigabe in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `ausland-tochter-emissionshandel-tehg` | Wenn es um Auslandstöchter und deutsche Berichtspflichten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- u... |
| `aussenhandel-intrastat-battg` | Wenn es um Außenhandel und Intrastat in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `battg-batterieregister-mengen` | Wenn es um Batterierecht und Mengenmeldung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `baugenehmigung-baustatistik` | Wenn es um Baugenehmigung und Baustatistik in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `bauwirtschaft-soka-behg` | Wenn es um Bauwirtschaft SOKA und Meldepflichten in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `behg-brennstoffemissionen` | Wenn es um BEHG Brennstoffemissionsbericht in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `behoerdenkommunikation` | Wenn es um Behördenkommunikation und Fristverlängerung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `berichtspflichten-register-und-fristenboard` | Wenn es um Register und Fristenboard für Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bundesbank-awv-z4-z5` | Wenn es um Bundesbank AWV Z4/Z5 Meldungen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bussgeld-vermeidung-heilung` | Wenn es um Bußgeldvermeidung und Heilung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `chemikalien-reach-csddd-vorschau-csrd` | Wenn es um REACH/CLP Bericht und Stoffdaten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `csddd-vorschau-lieferkette` | Wenn es um CSDDD Vorschau und Lieferkettenbericht in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `csrd-esrs-lagebericht` | Wenn es um CSRD/ESRS Nachhaltigkeitsbericht in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `datenminimierung-geheimnisschutz` | Wenn es um Datenminimierung und Geheimnisschutz in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `elektrog-ear-mengenmeldung` | Wenn es um ElektroG ear und Mengenmeldung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `emissionshandel-tehg-dehst` | Wenn es um TEHG Emissionsbericht und DEHSt in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `energieaudit-edl-entsendungen-a1-eudr` | Wenn es um Energieaudit EDL-G und EnEfG-Schnittstelle in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entsendungen-a1-mindestlohn` | Wenn es um Entsendung, A1 und Mindestlohnmeldungen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eudr-entwaldung-due-diligence` | Wenn es um EUDR Entwaldungsfreie Lieferketten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fuhrpark-telemetrie-datenschutz` | Wenn es um Fuhrpark, Telemetrie und Meldedaten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gefahrstoffverzeichnis-gefstoffv` | Wenn es um Gefahrstoffverzeichnis und Arbeitsschutz in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geschaeftsfuehrer-dashboard` | Wenn es um Geschäftsführer-Dashboard Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `handwerk-gefahrstoffe-asbest` | Wenn es um Handwerk: Asbest, Gefahrstoffe und Anzeigen in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `hinweisgeberschutz-jahresreport-idev` | Wenn es um HinSchG Reporting und Fallregister in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `idev-estatistik-core` | Wenn es um IDEV und eSTATISTIK.core praktisch nutzen in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und... |
| `immobilien-gebaeudeenergie-geg` | Wenn es um Gebäudeenergie und GEG-Nachweise in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `jahresabschluss-bundesanzeiger-keine` | Wenn es um Jahresabschluss und Offenlegung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `kaltstart-routing` | Wenn es um Berichtspflichten: Kaltstart und Pflichtenscan in Berichtspflichten-Erlediger geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `keine-pflicht-begruendet-ablehnen` | Wenn es um Keine Pflicht: sauber begründet ablehnen in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ki-einsatz-lohnsteuer` | Wenn es um digitale Werkzeuge zum Ausfüllen und Validieren nutzen in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständig... |
| `konjunktur-und-produktionsstatistik` | Wenn es um Konjunktur- und Produktionsstatistik in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwei... |
| `konzern-mutter-lebensmittel-haccp` | Wenn es um Konzernmatrix Mutter/Tochter in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `lebensmittel-haccp-rueckverfolgung` | Wenn es um Lebensmittel: HACCP und Rückverfolgung in Berichtspflichten-Erlediger geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `lksg-bafa-bericht` | Wenn es um LkSG BAFA-Bericht und Risikoanalyse in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `lohnsteuer-sozialversicherung-meldungen` | Wenn es um Lohnsteuer und Sozialversicherung melden in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `lucid-verpackg-maschinen-ce` | Wenn es um LUCID Registrierung und Datenmeldung in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `maschinen-ce-konformitaetsakte` | Wenn es um Maschinen CE und technische Dokumentation in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `mindestlohndokumentation-arbeitszeit` | Wenn es um Mindestlohn und Arbeitszeitdokumentation in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `mutterschutz-gefaehrdungsbeurteilung` | Wenn es um Mutterschutz Gefährdungsbeurteilung und Meldung in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `nachweisordner-dokumentenmatrix` | Wenn es um Nachweisordner und Dokumentenmatrix in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `nis2-bsi-incident` | Wenn es um NIS2/BSI Incident Reporting in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `produktsicherheit-rueckruf-market` | Wenn es um Produktsicherheit und Marktüberwachung melden in Berichtspflichten-Erlediger geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `saisonkalender-mittelstand-stichprobe` | Wenn es um Saisonkalender Mittelstand in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schwerbehindertenanzeige-sgb-verpackg` | Wenn es um Schwerbehindertenanzeige und Ausgleichsabgabe in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `statistik-anfrage-redteam` | Wenn es um Statistik-Anfrage Red-Team in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stichprobe-und-befreiung-kleine-unternehmen` | Wenn es um Stichprobe, Schwelle und Entlastung kleiner Unternehmen in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrol... |
| `transparenzregister-gwg-ubo` | Wenn es um Transparenzregister und wirtschaftlich Berechtigte in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert einen Einreichungsplan mit Form-, Portal- und Nachweisc... |
| `trinkwasser-legionellen-umsatzsteuer` | Wenn es um Trinkwasser und Legionellenmeldung in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umsatzsteuer-voranmeldung-elster` | Wenn es um Umsatzsteuer-Voranmeldung und ELSTER in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verdienststatistik-verdstatg` | Wenn es um Verdienststatistik und Entgeltdaten in Berichtspflichten-Erlediger geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächs... |
| `verpackg-vollstaendigkeitserklaerung` | Wenn es um VerpackG Vollständigkeitserklärung in Berichtspflichten-Erlediger geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `wp-stb-koordination` | Wenn es um WP/StB-Koordination bei Berichtspflichten in Berichtspflichten-Erlediger geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
