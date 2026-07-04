# Phishing-Vorfall-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`phishing-vorfall-pruefer`) | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin** (`phishing-vorfall-mayer-sparkasse-berlin`) | [Gesamt-PDF lesen](../testakten/phishing-vorfall-mayer-sparkasse-berlin/gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf) | [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB Paragraf 675u, Paragraf 675v, Paragraf 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`phishing-vorfall-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/phishing-vorfall-pruefer.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/phishing-vorfall-pruefer/phishing-vorfall-pruefer-werkstatt.md" download><code>phishing-vorfall-pruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/phishing-vorfall-pruefer/phishing-vorfall-pruefer-schnellstart.md" download><code>phishing-vorfall-pruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Akte Phishing-Vorfall Mayer ./. Sparkasse Berlin: [Gesamt-PDF](../testakten/phishing-vorfall-mayer-sparkasse-berlin/gesamt-pdf/phishing-vorfall-mayer-sparkasse-berlin_gesamt.pdf), [`testakte-phishing-vorfall-mayer-sparkasse-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin.zip), [`testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-phishing-vorfall-mayer-sparkasse-berlin-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `freistehender-erstpruefung-und-mandatsziel`, `start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `675v-quellenkarte`, `bankpflichten-beweislast-bgb`, `beweislast-mandantenkommunikation-entscheidungsvorlage`, `phishing-mit-geschaeftskonto`, `phishing-tatbestand-beweis-und-belege`, `pushtan-compliance-dokumentation-und-akte`, `quellen-livecheck`, `spezial-675v-livequellen-und-rechtsprechungscheck`, `spezial-pruefer-dokumentenmatrix-und-lueckenliste`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `arbeitnehmer-haftung-bgb-675u-phish-ceo`, `online-risikoampel-und-gegenargumente`, `phish-banking-trojaner-haftung-spezial`, `phishing-bgb-675u-haftung`, `phishing-praeventionscheckliste-strafanzeige`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `aufsicht-bafin-bank-strategie-banking-app`, `phishing-bank-strategie`, `phishing-tan-verfahren-vergleich` |
| 5. Verfahren, Behörde und Gericht | `banking-behoerden-gericht-und-registerweg`, `bgb-schriftsatz-brief-und-memo-bausteine`, `klage-fristennotiz-vorfall-phish-banking`, `phishing-zivilklage-bank`, `versicherer-cyber-phishing-vorfall-zivilklage`, `vorfall-fristen-form-und-zustaendigkeit` |
| 6. Ergebnis, Schreiben und Kommunikation | `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `fahrlaessigkeit-fehlerkatalog`, `spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `675u-675w-banking`, `675w-zahlen-schwellen-und-berechnung`, `bea-notfall-bgb-675v-erstkontakt-mandant`, `call-interessen-faelle-freistehender`, `faelle-abschlussprodukt-und-uebergabe`, `grobe-online-phishing`, `phish-ceo-fraud-konzern-spezial`, `phish-incident-meldepflichten-arten-erkennen`, `phish-meldepflichten-leitfaden`, `phishing-arten-erkennen`, `phishing-banking-app-malware`, `phishing-bgb-675v-grobfahrlaessig`, `phishing-erstkontakt-mandant`, `phishing-faelle-rentner-kryptowaehrung`, `phishing-kryptowaehrung-recovery`, `phishing-strafanzeige-vorbereiten`, `phishing-supply-chain-bec`, `phishing-tan`, ... plus 5 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `675u-675w-banking` | Wenn es um 675U: Verhandlung, Vergleich und Eskalation in Phishing-Vorfall-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `675v-quellenkarte` | Wenn es um 675v Quellenkarte in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `675w-zahlen-schwellen-und-berechnung` | Wenn es um 675W: Zahlen, Schwellenwerte und Berechnung in Phishing-Vorfall-Prüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `arbeitnehmer-haftung-bgb-675u-phish-ceo` | Wenn es um Phishing + Arbeitnehmerhaftung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufsicht-bafin-bank-strategie-banking-app` | Wenn es um BaFin-Beschwerde gegen Bank in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `banking-behoerden-gericht-und-registerweg` | Wenn es um Banking: Behörden-, Gerichts- oder Registerweg in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bankpflichten-beweislast-bgb` | Wenn es um Bankpflichten: Beweislast, Darlegungslast und Substantiierung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bea-notfall-bgb-675v-erstkontakt-mandant` | Wenn es um beA-Notfall bei Anwalts-PC in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweislast-mandantenkommunikation-entscheidungsvorlage` | Wenn es um Beweislast: Mandantenkommunikation und Entscheidungsvorlage in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bgb-schriftsatz-brief-und-memo-bausteine` | Wenn es um BGB: Schriftsatz-, Brief- und Memo-Bausteine in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `call-interessen-faelle-freistehender` | Wenn es um Call: Mehrparteienkonflikt und Interessenmatrix in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `faelle-abschlussprodukt-und-uebergabe` | Wenn es um Faelle: Abschlussprodukt und Übergabe in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fahrlaessigkeit-fehlerkatalog` | Wenn es um Fahrlaessigkeit Fehlerkatalog in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `freistehender-erstpruefung-und-mandatsziel` | Wenn es um Freistehender: Erstprüfung, Rollenklärung und Mandatsziel in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `grobe-online-phishing` | Wenn es um Grobe: Formular, Portal und Einreichungslogik in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `klage-fristennotiz-vorfall-phish-banking` | Wenn es um Klage: Fristennotiz und nächster Schritt in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `online-risikoampel-und-gegenargumente` | Wenn es um Online: Risikoampel, Gegenargumente und Verteidigungslinien in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-waehlen` | Wenn es um Output wählen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phish-banking-trojaner-haftung-spezial` | Wenn es um Phish: Banking-Trojaner Haftung in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `phish-ceo-fraud-konzern-spezial` | Wenn es um Phish: CEO-Fraud Konzern in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phish-incident-meldepflichten-arten-erkennen` | Wenn es um Phish: Incident-Triage in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phish-meldepflichten-leitfaden` | Wenn es um Phish: Meldepflichten in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-arten-erkennen` | Wenn es um Phishing-Arten erkennen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-bank-strategie` | Wenn es um Anschreiben an die Bank in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-banking-app-malware` | Wenn es um Banking-App-Malware-Faelle in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-bgb-675u-haftung` | Wenn es um Paragraf 675u BGB Prüfraster in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `phishing-bgb-675v-grobfahrlaessig` | Wenn es um Paragraf 675v Grobfahrlaessigkeitspruefung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-erstkontakt-mandant` | Wenn es um Phishing: Erstkontakt Mandant in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `phishing-faelle-rentner-kryptowaehrung` | Wenn es um Phishing-Faelle aelterer Mandanten in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-kryptowaehrung-recovery` | Wenn es um Phishing mit Kryptowaehrung in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `phishing-mit-geschaeftskonto` | Wenn es um Phishing gegen Geschäftskonto in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-praeventionscheckliste-strafanzeige` | Wenn es um Phishing-Praevention in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-strafanzeige-vorbereiten` | Wenn es um Strafanzeige Paragraf 263a StGB in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `phishing-supply-chain-bec` | Wenn es um BEC/Rechnungs-Phishing in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-tan` | Wenn es um Mandantenkommunikation in Phishing-Vorfall-Prüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `phishing-tan-verfahren-vergleich` | Wenn es um TAN-Verfahren und Haftung in Phishing-Vorfall-Prüfer geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `phishing-tatbestand-beweis-und-belege` | Wenn es um Phishing: Tatbestandsmerkmale, Beweisfragen und Beleglage in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `phishing-versicherer-cyber` | Wenn es um Cyberversicherung pruefen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `phishing-zivilklage-bank` | Wenn es um Zivilklage gegen Bank in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `pruefen` | Wenn es um Phishing-Vorfall Prüfen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `pushtan-compliance-dokumentation-und-akte` | Wenn es um Pushtan: Compliance-Dokumentation und Aktenvermerk in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `pushtan-schlichtung-sonderfall` | Wenn es um Prüfer: Dokumentenmatrix, Lückenliste und Nachforderung in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `schlichtung-sonderfall-und-edge-case` | Wenn es um Schlichtung: Sonderfall und Edge-Case-Prüfung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-675v-livequellen-und-rechtsprechungscheck` | Wenn es um 675V: Livequellen- und Rechtsprechungscheck in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-fahrlaessigkeit-red-team-und-qualitaetskontrolle` | Wenn es um Fahrlaessigkeit: Red-Team und Qualitätskontrolle in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-pruefer-dokumentenmatrix-und-lueckenliste` | Wenn es um Pruefer: Dokumentenmatrix, Lückenliste und Nachforderung in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spoofing-internationaler-bezug-und-schnittstellen` | Wenn es um Spoofing: Internationaler Bezug und Schnittstellen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `start-chronologie-fristen` | Wenn es um Phishing Vorfall Prüfer — Allgemein in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `versicherer-cyber-phishing-vorfall-zivilklage` | Wenn es um Cyberversicherung prüfen in Phishing-Vorfall-Prüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `vorfall-fristen-form-und-zustaendigkeit` | Wenn es um Vorfall: Fristen, Form, Zuständigkeit und Rechtsweg in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Phishing-Vorfall-Prüfer geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Phishing-Vorfall-Prüfer geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Phishing-Vorfall-Prüfer geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
