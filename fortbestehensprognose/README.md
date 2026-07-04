# Fortbestehensprognose

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fortbestehensprognose`) | [`fortbestehensprognose.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fortbestehensprognose Paragraf 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwölf-Monats-Liquidität. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fortbestehensprognose.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fortbestehensprognose/fortbestehensprognose-werkstatt.md" download><code>fortbestehensprognose-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fortbestehensprognose/fortbestehensprognose-schnellstart.md" download><code>fortbestehensprognose-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Fortbestehensprognose Paragrafix GmbH: [Gesamt-PDF](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf), [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip), [`testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Prüfablauf Bilanzstatus Annahmen Plausibilisierung 12-Monats-Liquidität. Sanierungsbausteine harte Patronatserklärung Comfortletter Gesellschafterdarlehen Rangrücktritt Stundung Forderungsverzicht. IDW S 11 S 6 StaRUG. Funktioniert allein; empfohlene Begleitplugins liquiditätsplanung (wochenbasierte Liquidität) und insolvenzrecht (§ 17 § 18 InsO Antragspflicht).

## Installation in der Plugin-Umgebung

1. ZIP herunterladen (Link oben).
2. Plugin-Menü öffnen, `Install from .zip` wählen und die Datei auswählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortfuehrung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Ums… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalität Auftragsbestand Kunden… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem … |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposte… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstützen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechts… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrec… |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquidität Sensitivitätsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Maßstab ueb… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steu… |
| `liquiditaet-12-monate` | Erstellt die rollierende Zwölf-Monats-Liquiditätsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib. Pru… |
| `patronatserklaerung-extern-hart-erzeugen` | Erzeugt eine harte externe Patronatserklärung des Gesellschafters (oder eines Dritten) zugunsten der Gesellschaft. Erfasst Patron Begueneten Höhe Bedingungen Laufzeit Insolvenzfeste Klausel. Zur Berücksichtigung im… |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthält Ausgangslage Annahmen Plausibilisierung Liquidität Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Bel… |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Maßnahmen negativ oder knapp positiv ist schlägt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrück… |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungsträger). Erfasst pro Gläubiger Forderungshöhe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspaus… |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfällt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsv… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `fortbestehensprognose-erstpruefung-und-mandatsziel`, `kaltstart-interview`, `start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `fortbestehensdokumentation-insolvenzrecht`, `fp-dokumentation-gerichtsfaehigkeit`, `inso-tatbestand-beweis-und-belege`, `monats-quellenkarte`, `quellen-livecheck`, `sanierungsbausteine-compliance-dokumentation-und-akte`, `selbstdokumentation-dokumentenmatrix-und-lueckenliste`, `spezial-monats-livequellen-und-rechtsprechungscheck`, `spezial-rangruecktritt-formular-portal-und-einreichung`, `starug-beweislast-stundung-red-zwoelf`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `annahmen-sammeln-bilanzieller-status`, `bilanzieller-status-aufnehmen`, `bilanzstatus-risikoampel-und-gegenargumente`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `fbp-integrierte-planung-bauleiter`, `rangruecktritt-sanierungsbausteine`, `sanierungsbausteine-vorschlagen-annahmen`, `zwoelf-verhandlung-vergleich-und-eskalation` |
| 5. Verfahren, Behörde und Gericht | `annahmen-behoerden-gericht-und-registerweg`, `geschaeftsfuehrer-fristen-form-und-zustaendigkeit`, `negativer-fristennotiz-ausloesendes-ereignis`, `plausibilisierung-schriftsatz-brief-und-memo-bausteine`, `spezial-geschaeftsfuehrer-fristen-form-und-zustaendigkeit` |
| 6. Ergebnis, Schreiben und Kommunikation | `fbp-bankenkommunikation-waiver-integrierte`, `mandantenkommunikation-redteam`, `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `annahmen-belastbarkeit-plausibilisieren`, `stundung-red-team-und-qualitaetskontrolle`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `ausloesendes-ereignis-erfassen`, `comfortletter-sonderfall-edge`, `comfortletter-weich-erzeugen`, `eskalation-sonderfall-und-edge-case`, `fbp-stresstest-szenarien-leitfaden`, `fbp-zahlungsunfaehigkeit`, `forderungsverzicht-besserungsschein`, `forderungsverzicht-mandantenentscheidung`, `fp-cash-flow-modell-spezial`, `fp-einfuehrung-pflicht-und-zweck`, `fp-zeitraum-und-szenarien-praxis`, `gesellschafterdarlehen-rangruecktritt`, `liquiditaet-12-monate`, `liquiditaet-patronatserklaerung-interessen`, `patronatserklaerung-extern-hart-erzeugen`, `patronatserklaerung-mehrparteien-konflikt-und-interessen`, `prognose-stichtag-stundungsanfrage-glaeubiger`, `stundungsanfrage-glaeubiger`, ... plus 2 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `annahmen-behoerden-gericht-und-registerweg` | Wenn es um Annahmen: Behörden-, Gerichts- oder Registerweg in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `annahmen-belastbarkeit-plausibilisieren` | Wenn es um Annahmen plausibilisieren in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `annahmen-sammeln-bilanzieller-status` | Wenn es um Annahmen sammeln (Fortführung) in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `anschluss-routing` | Wenn es um Anschluss-Routing in Fortbestehensprognose geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausloesendes-ereignis-erfassen` | Wenn es um Auslösendes Ereignis erfassen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bilanzieller-status-aufnehmen` | Wenn es um Bilanzieller Status aufnehmen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `bilanzstatus-risikoampel-und-gegenargumente` | Wenn es um Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien in Fortbestehensprognose geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `comfortletter-sonderfall-edge` | Wenn es um Comfortletter: Internationaler Bezug und Schnittstellen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `comfortletter-weich-erzeugen` | Wenn es um Comfortletter (weich) in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `dokumente-intake` | Wenn es um Dokumentenintake in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `einstieg-routing` | Wenn es um Einstieg und Routing in Fortbestehensprognose geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `eskalation-sonderfall-und-edge-case` | Wenn es um Eskalation: Sonderfall und Edge-Case-Prüfung in Fortbestehensprognose geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `fbp-bankenkommunikation-waiver-integrierte` | Wenn es um FBP: Bankenkommunikation Waiver in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fbp-integrierte-planung-bauleiter` | Wenn es um FBP: Integrierte Planung Bauleiter in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fbp-stresstest-szenarien-leitfaden` | Wenn es um FBP: Stresstest-Szenarien in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fbp-zahlungsunfaehigkeit` | Wenn es um FBP: Zahlungsunfaehigkeit Ueberschuldung in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderungsverzicht-besserungsschein` | Wenn es um Forderungsverzicht mit Besserungsschein in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `forderungsverzicht-mandantenentscheidung` | Wenn es um Forderungsverzicht: Mandantenkommunikation und Entscheidungsvorlage in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fortbestehensdokumentation-insolvenzrecht` | Wenn es um Fortbestehensdokumentation mit insolvenzrechtlicher Tragfähigkeit in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nac... |
| `fortbestehensprognose-erstpruefung-und-mandatsziel` | Wenn es um Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel in Fortbestehensprognose geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschrit... |
| `fp-cash-flow-modell-spezial` | Wenn es um FP: Cash-Flow-Modell in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `fp-dokumentation-gerichtsfaehigkeit` | Wenn es um FP: Dokumentation-Gerichtsfaehigkeit in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `fp-einfuehrung-pflicht-und-zweck` | Wenn es um FP: Pflicht und Zweck in Fortbestehensprognose geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `fp-zeitraum-und-szenarien-praxis` | Wenn es um FP: Zeitraum und Szenarien in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Wenn es um Geschäftsführer: Fristen, Form, Zuständigkeit und Rechtsweg in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gesellschafterdarlehen-rangruecktritt` | Wenn es um Gesellschafterdarlehen — qualifizierter Rangrücktritt in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `inso-tatbestand-beweis-und-belege` | Wenn es um InsO: Tatbestandsmerkmale, Beweisfragen und Beleglage in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierungsmatrix. |
| `kaltstart-interview` | Wenn es um /fortbestehensprognose:fortbestehensprognose-kaltstart-interview in Fortbestehensprognose geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `liquiditaet-12-monate` | Wenn es um Zwölf-Monats-Liquidität in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `liquiditaet-patronatserklaerung-interessen` | Wenn es um Liquiditaet: Zahlen, Schwellenwerte und Berechnung in Fortbestehensprognose geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen. |
| `mandantenkommunikation-redteam` | Wenn es um Mandantenkommunikation in Fortbestehensprognose geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Mandantennachricht oder Entscheidungsvorlage. |
| `monats-quellenkarte` | Wenn es um Monats Quellenkarte in Fortbestehensprognose geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `negativer-fristennotiz-ausloesendes-ereignis` | Wenn es um Negativer: Fristennotiz und nächster Schritt in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `output-waehlen` | Wenn es um Output wählen in Fortbestehensprognose geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `patronatserklaerung-extern-hart-erzeugen` | Wenn es um Harte Patronatserklärung prüfen und erzeugen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `patronatserklaerung-mehrparteien-konflikt-und-interessen` | Wenn es um Patronatserklaerung: Mehrparteienkonflikt und Interessenmatrix in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `plausibilisierung-schriftsatz-brief-und-memo-bausteine` | Wenn es um Plausibilisierung: Schriftsatz-, Brief- und Memo-Bausteine in Fortbestehensprognose geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und... |
| `prognose-stichtag-stundungsanfrage-glaeubiger` | Wenn es um Prognose-Dokumentation Stichtag in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in Fortbestehensprognose geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `rangruecktritt-sanierungsbausteine` | Wenn es um Rangrücktritt: Formular, Portal und Einreichungslogik in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sanierungsbausteine-compliance-dokumentation-und-akte` | Wenn es um Sanierungsbausteine: Compliance-Dokumentation und Aktenvermerk in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näc... |
| `sanierungsbausteine-vorschlagen-annahmen` | Wenn es um Sanierungsbausteine vorschlagen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `selbstdokumentation-dokumentenmatrix-und-lueckenliste` | Wenn es um Selbstdokumentation: Dokumentenmatrix, Lückenliste und Nachforderung in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `spezial-geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Wenn es um Geschaeftsfuehrer: Fristen, Form, Zuständigkeit und Rechtsweg in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-monats-livequellen-und-rechtsprechungscheck` | Wenn es um Monats: Livequellen- und Rechtsprechungscheck in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `spezial-rangruecktritt-formular-portal-und-einreichung` | Wenn es um Rangruecktritt: Formular, Portal und Einreichungslogik in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `start-chronologie-fristen` | Wenn es um Fortbestehensprognose — Allgemein in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `starug-beweislast-stundung-red-zwoelf` | Wenn es um StaRUG: Beweislast, Darlegungslast und Substantiierung in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stundung-red-team-und-qualitaetskontrolle` | Wenn es um Stundung: Red-Team und Qualitätskontrolle in Fortbestehensprognose geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stundungsanfrage-glaeubiger` | Wenn es um Stundungsanfrage Gläubiger in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wenn-prognose-negativ-naechste-schritte` | Wenn es um Wenn Prognose Negativ Naechste Schritte in Fortbestehensprognose geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-fristen-und-risikoampel` | Wenn es um Fristen- und Risikoampel in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in Fortbestehensprognose geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in Fortbestehensprognose geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in Fortbestehensprognose geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `zusammenfuehren` | Wenn es um Fortbestehensprognose zusammenführen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zwoelf-verhandlung-vergleich-und-eskalation` | Wenn es um Zwoelf: Verhandlung, Vergleich und Eskalation in Fortbestehensprognose geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
