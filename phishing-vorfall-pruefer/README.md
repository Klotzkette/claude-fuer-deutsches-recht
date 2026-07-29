# Phishing-Vorfall-Prüfer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB Paragraf 675u, Paragraf 675v, Paragraf 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/phishing-vorfall-pruefer.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/phishing-vorfall-pruefer/phishing-vorfall-pruefer-werkstatt.md" download><code>phishing-vorfall-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/phishing-vorfall-pruefer/phishing-vorfall-pruefer-schnellstart.md" download><code>phishing-vorfall-pruefer-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin](../testakten/phishing-vorfall-mayer-sparkasse-berlin/README.md) | [Gesamt-PDF](../testakten/phishing-vorfall-mayer-sparkasse-berlin/gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) | [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) | [`testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für anwaltliche Prüfung von Online-Banking-Phishing, pushTAN-/photoTAN-Vorfällen, Call-ID-Spoofing, gefälschten Bankhotlines, Social Engineering und streitigen Erstattungsansprüchen gegen Zahlungsdienstleister.

Das Plugin arbeitet entlang des typischen Mandats:

1. Intake: Konto, Zahlungsinstrument, Schaden, Autorisierung, Sperr- und Anzeigeverlauf.
2. Rechtsrahmen: § 675u BGB, § 675v BGB, § 675w BGB, § 675l BGB, § 676b BGB und § 55 ZAG.
3. Beweisprüfung: TAN-Dialog, App-Screens, Banklogs, IP-Adressen, Device-Binding, SCA, Transaktionsmonitoring, Warnhinweise.
4. Risikomatrix: nicht autorisierter Zahlungsvorgang, grobe Fahrlässigkeit, Bankpflichtverletzung, Mitverschulden/Quotelung, Ombudsmann oder Klage.
5. Output: Erstbewertung, Bankaufforderung, Ombudsmann-Antrag, Klagegerüst, Beweisantritts- und Log-Anforderung.

## Inhalt

- `skills/phishing-vorfall-pruefen/SKILL.md` - geführter Hauptworkflow.
- `references/rechtsrahmen.md` - Arbeitsrahmen mit amtlichen Normlinks.
- `assets/checklisten/` - Intake, Beweis- und Logmatrix, grobe-Fahrlässigkeit-Ampel.
- `assets/vorlagen/` - Bankaufforderung, Ombudsmann-Antrag, Klagegerüst.
- `scripts/phishing_case_gate.py` - kleines Offline-Gate für strukturierte Fallbewertung.

## Arbeitsprinzip

Das Plugin entscheidet keinen Fall automatisch. Es zwingt zur sauberen Trennung:

- Hat der Kunde den konkreten Zahlungsvorgang autorisiert?
- Liegt ein Einwand aus § 675v BGB vor?
- Was ist bewiesen, was nur behauptet?
- Welche Banklogs müssen verlangt werden?
- Ist Schlichtung, Teilvergleich oder Klage der bessere nächste Schritt?

Alle rechtlichen Bewertungen sind Arbeitsentwürfe und müssen durch eine qualifizierte Person geprüft werden.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`freistehender-erstpruefung-und-mandatsziel`](skills/freistehender-erstpruefung-und-mandatsziel/SKILL.md), [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`675v-quellenkarte`](skills/675v-quellenkarte/SKILL.md), [`bankpflichten-beweislast-bgb`](skills/bankpflichten-beweislast-bgb/SKILL.md), [`beweislast-mandantenkommunikation-entscheidungsvorlage`](skills/beweislast-mandantenkommunikation-entscheidungsvorlage/SKILL.md), [`phishing-mit-geschaeftskonto`](skills/phishing-mit-geschaeftskonto/SKILL.md), [`phishing-tatbestand-beweis-und-belege`](skills/phishing-tatbestand-beweis-und-belege/SKILL.md), [`pushtan-compliance-dokumentation-und-akte`](skills/pushtan-compliance-dokumentation-und-akte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`spezial-675v-livequellen-und-rechtsprechungscheck`](skills/spezial-675v-livequellen-und-rechtsprechungscheck/SKILL.md), [`spezial-pruefer-dokumentenmatrix-und-lueckenliste`](skills/spezial-pruefer-dokumentenmatrix-und-lueckenliste/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`arbeitnehmer-haftung-bgb-675u-phish-ceo`](skills/arbeitnehmer-haftung-bgb-675u-phish-ceo/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`online-risikoampel-und-gegenargumente`](skills/online-risikoampel-und-gegenargumente/SKILL.md), [`phish-banking-trojaner-haftung-spezial`](skills/phish-banking-trojaner-haftung-spezial/SKILL.md), [`phishing-bgb-675u-haftung`](skills/phishing-bgb-675u-haftung/SKILL.md), [`phishing-praeventionscheckliste-strafanzeige`](skills/phishing-praeventionscheckliste-strafanzeige/SKILL.md), [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`aufsicht-bafin-bank-strategie-banking-app`](skills/aufsicht-bafin-bank-strategie-banking-app/SKILL.md), [`phishing-bank-strategie`](skills/phishing-bank-strategie/SKILL.md), [`phishing-tan-verfahren-vergleich`](skills/phishing-tan-verfahren-vergleich/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`banking-behoerden-gericht-und-registerweg`](skills/banking-behoerden-gericht-und-registerweg/SKILL.md), [`bgb-schriftsatz-brief-und-memo-bausteine`](skills/bgb-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`klage-fristennotiz-vorfall-phish-banking`](skills/klage-fristennotiz-vorfall-phish-banking/SKILL.md), [`phishing-zivilklage-bank`](skills/phishing-zivilklage-bank/SKILL.md), [`versicherer-cyber-phishing-vorfall-zivilklage`](skills/versicherer-cyber-phishing-vorfall-zivilklage/SKILL.md), [`vorfall-fristen-form-und-zustaendigkeit`](skills/vorfall-fristen-form-und-zustaendigkeit/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`fahrlaessigkeit-fehlerkatalog`](skills/fahrlaessigkeit-fehlerkatalog/SKILL.md), [`spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle`](skills/spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`675u-675w-banking`](skills/675u-675w-banking/SKILL.md), [`675w-zahlen-schwellen-und-berechnung`](skills/675w-zahlen-schwellen-und-berechnung/SKILL.md), [`bea-notfall-bgb-675v-erstkontakt-mandant`](skills/bea-notfall-bgb-675v-erstkontakt-mandant/SKILL.md), [`call-interessen-faelle-freistehender`](skills/call-interessen-faelle-freistehender/SKILL.md), [`faelle-abschlussprodukt-und-uebergabe`](skills/faelle-abschlussprodukt-und-uebergabe/SKILL.md), [`grobe-online-phishing`](skills/grobe-online-phishing/SKILL.md), [`phish-ceo-fraud-konzern-spezial`](skills/phish-ceo-fraud-konzern-spezial/SKILL.md), [`phish-incident-meldepflichten-arten-erkennen`](skills/phish-incident-meldepflichten-arten-erkennen/SKILL.md), [`phish-meldepflichten-leitfaden`](skills/phish-meldepflichten-leitfaden/SKILL.md), [`phishing-arten-erkennen`](skills/phishing-arten-erkennen/SKILL.md), [`phishing-banking-app-malware`](skills/phishing-banking-app-malware/SKILL.md), [`phishing-bgb-675v-grobfahrlaessig`](skills/phishing-bgb-675v-grobfahrlaessig/SKILL.md), [`phishing-erstkontakt-mandant`](skills/phishing-erstkontakt-mandant/SKILL.md), [`phishing-faelle-rentner-kryptowaehrung`](skills/phishing-faelle-rentner-kryptowaehrung/SKILL.md), [`phishing-kryptowaehrung-recovery`](skills/phishing-kryptowaehrung-recovery/SKILL.md), [`phishing-strafanzeige-vorbereiten`](skills/phishing-strafanzeige-vorbereiten/SKILL.md), [`phishing-supply-chain-bec`](skills/phishing-supply-chain-bec/SKILL.md), [`phishing-tan`](skills/phishing-tan/SKILL.md), ... plus 5 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`675u-675w-banking`](skills/675u-675w-banking/SKILL.md) | Wenn es um 675U: Verhandlung, Vergleich und Eskalation in Phishing-Vorfall-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`675v-quellenkarte`](skills/675v-quellenkarte/SKILL.md) | Wenn es um 675v Quellenkarte in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| [`675w-zahlen-schwellen-und-berechnung`](skills/675w-zahlen-schwellen-und-berechnung/SKILL.md) | Wenn es um 675W: Zahlen, Schwellenwerte und Berechnung in Phishing-Vorfall-Prüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`arbeitnehmer-haftung-bgb-675u-phish-ceo`](skills/arbeitnehmer-haftung-bgb-675u-phish-ceo/SKILL.md) | Wenn es um Phishing + Arbeitnehmerhaftung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufsicht-bafin-bank-strategie-banking-app`](skills/aufsicht-bafin-bank-strategie-banking-app/SKILL.md) | Wenn es um BaFin-Beschwerde gegen Bank in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`banking-behoerden-gericht-und-registerweg`](skills/banking-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Banking: Behörden-, Gerichts- oder Registerweg in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bankpflichten-beweislast-bgb`](skills/bankpflichten-beweislast-bgb/SKILL.md) | Wenn es um Bankpflichten: Beweislast, Darlegungslast und Substantiierung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bea-notfall-bgb-675v-erstkontakt-mandant`](skills/bea-notfall-bgb-675v-erstkontakt-mandant/SKILL.md) | Wenn es um beA-Notfall bei Anwalts-PC in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`beweislast-mandantenkommunikation-entscheidungsvorlage`](skills/beweislast-mandantenkommunikation-entscheidungsvorlage/SKILL.md) | Wenn es um Beweislast: Mandantenkommunikation und Entscheidungsvorlage in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`bgb-schriftsatz-brief-und-memo-bausteine`](skills/bgb-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um BGB: Schriftsatz-, Brief- und Memo-Bausteine in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`call-interessen-faelle-freistehender`](skills/call-interessen-faelle-freistehender/SKILL.md) | Wenn es um Call: Mehrparteienkonflikt und Interessenmatrix in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`faelle-abschlussprodukt-und-uebergabe`](skills/faelle-abschlussprodukt-und-uebergabe/SKILL.md) | Wenn es um Faelle: Abschlussprodukt und Übergabe in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`fahrlaessigkeit-fehlerkatalog`](skills/fahrlaessigkeit-fehlerkatalog/SKILL.md) | Wenn es um Fahrlaessigkeit Fehlerkatalog in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`freistehender-erstpruefung-und-mandatsziel`](skills/freistehender-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Freistehender: Erstprüfung, Rollenklärung und Mandatsziel in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`grobe-online-phishing`](skills/grobe-online-phishing/SKILL.md) | Wenn es um Grobe: Formular, Portal und Einreichungslogik in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Phishing Vorfall Prüfer ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`klage-fristennotiz-vorfall-phish-banking`](skills/klage-fristennotiz-vorfall-phish-banking/SKILL.md) | Wenn es um Klage: Fristennotiz und nächster Schritt in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`online-risikoampel-und-gegenargumente`](skills/online-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Online: Risikoampel, Gegenargumente und Verteidigungslinien in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phish-banking-trojaner-haftung-spezial`](skills/phish-banking-trojaner-haftung-spezial/SKILL.md) | Wenn es um Phish: Banking-Trojaner Haftung in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| [`phish-ceo-fraud-konzern-spezial`](skills/phish-ceo-fraud-konzern-spezial/SKILL.md) | Wenn es um Phish: CEO-Fraud Konzern in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phish-incident-meldepflichten-arten-erkennen`](skills/phish-incident-meldepflichten-arten-erkennen/SKILL.md) | Wenn es um Phish: Incident-Triage in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phish-meldepflichten-leitfaden`](skills/phish-meldepflichten-leitfaden/SKILL.md) | Wenn es um Phish: Meldepflichten in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-arten-erkennen`](skills/phishing-arten-erkennen/SKILL.md) | Wenn es um Phishing-Arten erkennen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-bank-strategie`](skills/phishing-bank-strategie/SKILL.md) | Wenn es um Anschreiben an die Bank in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-banking-app-malware`](skills/phishing-banking-app-malware/SKILL.md) | Wenn es um Banking-App-Malware-Faelle in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-bgb-675u-haftung`](skills/phishing-bgb-675u-haftung/SKILL.md) | Wenn es um Paragraf 675u BGB Prüfraster in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`phishing-bgb-675v-grobfahrlaessig`](skills/phishing-bgb-675v-grobfahrlaessig/SKILL.md) | Wenn es um Paragraf 675v Grobfahrlaessigkeitspruefung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-erstkontakt-mandant`](skills/phishing-erstkontakt-mandant/SKILL.md) | Wenn es um Phishing: Erstkontakt Mandant in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`phishing-faelle-rentner-kryptowaehrung`](skills/phishing-faelle-rentner-kryptowaehrung/SKILL.md) | Wenn es um Phishing-Faelle aelterer Mandanten in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-kryptowaehrung-recovery`](skills/phishing-kryptowaehrung-recovery/SKILL.md) | Wenn es um Phishing mit Kryptowaehrung in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| [`phishing-mit-geschaeftskonto`](skills/phishing-mit-geschaeftskonto/SKILL.md) | Wenn es um Phishing gegen Geschäftskonto in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-praeventionscheckliste-strafanzeige`](skills/phishing-praeventionscheckliste-strafanzeige/SKILL.md) | Wenn es um Phishing-Praevention in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-strafanzeige-vorbereiten`](skills/phishing-strafanzeige-vorbereiten/SKILL.md) | Wenn es um Strafanzeige Paragraf 263a StGB in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`phishing-supply-chain-bec`](skills/phishing-supply-chain-bec/SKILL.md) | Wenn es um BEC/Rechnungs-Phishing in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-tan`](skills/phishing-tan/SKILL.md) | Wenn es um Mandantenkommunikation in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| [`phishing-tan-verfahren-vergleich`](skills/phishing-tan-verfahren-vergleich/SKILL.md) | Wenn es um TAN-Verfahren und Haftung in Phishing-Vorfall-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| [`phishing-tatbestand-beweis-und-belege`](skills/phishing-tatbestand-beweis-und-belege/SKILL.md) | Wenn es um Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| [`phishing-versicherer-cyber`](skills/phishing-versicherer-cyber/SKILL.md) | Wenn es um Cyberversicherung pruefen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`phishing-zivilklage-bank`](skills/phishing-zivilklage-bank/SKILL.md) | Wenn es um Zivilklage gegen Bank in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`pruefen`](skills/pruefen/SKILL.md) | Wenn es um Phishing-Vorfall Prüfen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`pushtan-compliance-dokumentation-und-akte`](skills/pushtan-compliance-dokumentation-und-akte/SKILL.md) | Wenn es um Pushtan: Compliance-Dokumentation und Aktenvermerk in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| [`pushtan-schlichtung-sonderfall`](skills/pushtan-schlichtung-sonderfall/SKILL.md) | Wenn es um Prüfer: Dokumentenmatrix, Lückenliste und Nachforderung in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`schlichtung-sonderfall-und-edge-case`](skills/schlichtung-sonderfall-und-edge-case/SKILL.md) | Wenn es um Schlichtung: Sonderfall und Edge-Case-Prüfung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-675v-livequellen-und-rechtsprechungscheck`](skills/spezial-675v-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um 675V: Livequellen- und Rechtsprechungscheck in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle`](skills/spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Fahrlaessigkeit: Red-Team und Qualitätskontrolle in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spezial-pruefer-dokumentenmatrix-und-lueckenliste`](skills/spezial-pruefer-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`spoofing-internationaler-bezug-und-schnittstellen`](skills/spoofing-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Spoofing: Internationaler Bezug und Schnittstellen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`start-chronologie-fristen`](skills/start-chronologie-fristen/SKILL.md) | Wenn es um Phishing Vorfall Prüfer — Allgemein in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`versicherer-cyber-phishing-vorfall-zivilklage`](skills/versicherer-cyber-phishing-vorfall-zivilklage/SKILL.md) | Wenn es um Cyberversicherung prüfen in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| [`vorfall-fristen-form-und-zustaendigkeit`](skills/vorfall-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Vorfall: Fristen, Form, Zuständigkeit und Rechtsweg in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-fristen-und-risikoampel`](skills/workflow-fristen-und-risikoampel/SKILL.md) | Wenn es um Fristen- und Risikoampel in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
