# Fortbestehensprognose

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwölf-Monats-Liquidität. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`fortbestehensprognose.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fortbestehensprognose/fortbestehensprognose-werkstatt.md" download><code>fortbestehensprognose-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fortbestehensprognose/fortbestehensprognose-schnellstart.md" download><code>fortbestehensprognose-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Fortbestehensprognose Paragrafix GmbH: [Gesamt-PDF](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf), [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip), [`testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `annahmen-behoerden-gericht-und-registerweg` | Annahmen: Behörden-, Gerichts- oder Registerweg im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Per... |
| `annahmen-sammeln-bilanzieller-status` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt-... |
| `anschluss-routing` | Anschluss-Routing für Fortbestehensprognose StaRUG/InsO: wählt den nächsten Spezial-Skill nach Engpass (Antragsfrist 3 Wochen § 15a InsO, Liquiditätsplan 24 Monate, Erfolgsplan, Bilanz), dokumentiert Router-Entscheidung mit Begründung. |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass... |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle... |
| `bilanzstatus-risikoampel-und-gegenargumente` | Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien im Fortbestehensprognose. |
| `comfortletter-sonderfall-edge` | Comfortletter: Internationaler Bezug und Schnittstellen im Fortbestehensprognose. |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzb... |
| `dokumente-intake` | Dokumentenintake für Fortbestehensprognose StaRUG/InsO: sortiert Liquiditätsplan 24 Monate, Erfolgsplan, Bilanz, prüft Datum, Absender, Frist und Beweiswert (Bankbestätigungen, Forderungslisten); markiert Lücken; berücksichtigt Mandatsge... |
| `einstieg-routing` | Einstieg, Triage und Routing für Fortbestehensprognose StaRUG/InsO: ordnet Rolle (Geschäftsführung, Wirtschaftsprüfer, Insolvenzverwalter), markiert Frist (Antragsfrist 3 Wochen § 15a InsO), wählt Norm (§ 18 InsO drohende Zahlungsunfähig... |
| `eskalation-sonderfall-und-edge-case` | Eskalation: Sonderfall und Edge-Case-Prüfung im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `fbp-bankenkommunikation-waiver-integrierte` | Spezialfall Bankenkommunikation und Waiver / Standstill bei drohender Zahlungsunfaehigkeit: Konsortium, Sicherheitenpool, MAC-Klausel. Prüfraster für Geschäftsleitung und Treuhaender im Fortbestehensprognose. |
| `fbp-integrierte-planung-bauleiter` | Bauleiter integrierte Planung GuV, Bilanz, Cashflow für IDW S 11. Prüfraster für Planungsschritte, Annahmen, Sensitivitaeten. Mustertext Annahmenverzeichnis im Fortbestehensprognose. |
| `fbp-stresstest-szenarien-leitfaden` | Leitfaden Stresstest- und Szenarien-Aufbau für Fortbestehensprognose: Basis-, Stress- und Worst-Case, KPIs, Trigger für Maßnahmen. Prüfraster für Beraterhand und Geschäftsleitung im Fortbestehensprognose. |
| `fbp-zahlungsunfaehigkeit` | Spezialfall Abgrenzung Zahlungsunfaehigkeit und Ueberschuldung § 17 / § 19 InsO: Liquiditaetsstatus 21-Tage-Frist, Fortfuehrungsprognose, BGH-Rechtsprechung. Prüfraster für Geschäftsleitung im Fortbestehensprognose. |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die ve... |
| `forderungsverzicht-mandantenentscheidung` | Forderungsverzicht: Mandantenkommunikation und Entscheidungsvorlage im Fortbestehensprognose. |
| `fortbestehensdokumentation-insolvenzrecht` | Fortbestehensdokumentation mit insolvenzrechtlicher Tragfähigkeit: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Fortbestehensprognose. |
| `fortbestehensprognose-erstpruefung-und-mandatsziel` | Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel im Fortbestehensprognose. |
| `fp-cash-flow-modell-spezial` | Spezialfall Cash-Flow-Modell: monatliche Liquiditaetsplanung mindestens für 12 Monate, Plausibilitaetskontrollen, Sensitivitaetsanalysen. Pflichten Geschäftsführer und Prüfer. Prüfraster und Praxistipps im Fortbestehensprognose. |
| `fp-dokumentation-gerichtsfaehigkeit` | Spezialfall Dokumentation und Gerichtsfaehigkeit: was muss in der Akte, wann ist die Prognose strafrechts- und haftungsfest, Aktualisierung bei wesentlicher Änderung. Standard für Auditoren-Akzeptanz und Insolvenzverwalter-Prüfung im For... |
| `fp-einfuehrung-pflicht-und-zweck` | Fortbestehensprognose einfuehrend: Pflicht zur Erstellung bei Anhaltspunkten für Zahlungsunfaehigkeit, Geltung im Sinne § 19 InsO Ueberschuldungspruefung, Verzahnung mit Krisenfrueherkennung StaRUG § 1. Wer muss erstellen, wann, wozu im... |
| `fp-zeitraum-und-szenarien-praxis` | Fortbestehensprognose-Zeitraum 12 Monate seit SanInsFoG, ueblicher Praxis-Korridor: konservativ, mittel, optimistisch. Aufbau Szenarienrechnung in der Praxis. IDW S 11 Ueberschuldung und IDW S 6 Sanierungskonzept Bezug im Fortbestehenspr... |
| `geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Geschäftsführer: Fristen, Form, Zuständigkeit und Rechtsweg im Fortbestehensprognose. |
| `gesellschafterdarlehen-rangruecktritt` | Gesellschafterdarlehen Rangruecktritt: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Fortbestehensprognose. |
| `inso-tatbestand-beweis-und-belege` | InsO: Tatbestandsmerkmale, Beweisfragen und Beleglage im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner... |
| `liquiditaet-12-monate` | Liquiditaet 12 Monate: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Fortbestehensprognose. |
| `liquiditaet-patronatserklaerung-interessen` | Liquiditaet: Zahlen, Schwellenwerte und Berechnung im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `mandantenkommunikation-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Fortbestehensprognose. |
| `monats-quellenkarte` | Monats Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `negativer-fristennotiz-ausloesendes-ereignis` | Negativer: Fristennotiz und nächster Schritt im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Fortbestehensprognose StaRUG/InsO: stimmt Adressat (Geschäftsführung, Wirtschaftsprüfer, Insolvenzverwalter), Frist (Antragsfrist 3 Wochen § 15a InsO) und Form auf den Zweck ab — typische Outputs: Fortbestehensprognose ID... |
| `patronatserklaerung-extern-hart-erzeugen` | Patronatserklaerung Extern Hart Erzeugen: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Fortbestehensprognose. |
| `patronatserklaerung-mehrparteien-konflikt-und-interessen` | Patronatserklaerung: Mehrparteienkonflikt und Interessenmatrix im Fortbestehensprognose. |
| `plausibilisierung-schriftsatz-brief-und-memo-bausteine` | Plausibilisierung: Schriftsatz-, Brief- und Memo-Bausteine im Fortbestehensprognose. |
| `prognose-stichtag-stundungsanfrage-glaeubiger` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Gesc... |
| `quellen-livecheck` | Quellen-Live-Check für Fortbestehensprognose StaRUG/InsO: prüft Normen (§ 18 InsO drohende Zahlungsunfähigkeit, StaRUG §§ 1/14/49, IDW S 11) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Insolvenzgericht und Que... |
| `rangruecktritt-sanierungsbausteine` | Rangruecktritt: Formular, Portal und Einreichungslogik im Fortbestehensprognose. |
| `sanierungsbausteine-compliance-dokumentation-und-akte` | Sanierungsbausteine: Compliance-Dokumentation und Aktenvermerk im Fortbestehensprognose. |
| `sanierungsbausteine-vorschlagen-annahmen` | Wenn die Fortbestehensprognose ohne Maßnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinba... |
| `selbstdokumentation-dokumentenmatrix-und-lueckenliste` | Selbstdokumentation: Dokumentenmatrix, Lückenliste und Nachforderung im Fortbestehensprognose. |
| `spezial-geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Geschaeftsfuehrer: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `spezial-monats-livequellen-und-rechtsprechungscheck` | Monats: Livequellen- und Rechtsprechungscheck. |
| `spezial-rangruecktritt-formular-portal-und-einreichung` | Rangruecktritt: Formular, Portal und Einreichungslogik. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `starug-beweislast-stundung-red-zwoelf` | StaRUG: Beweislast, Darlegungslast und Substantiierung im Fortbestehensprognose. |
| `stundung-red-team-und-qualitaetskontrolle` | Stundung: Red-Team und Qualitätskontrolle im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheit... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fortbestehensprognose StaRUG/InsO: trennt fehlende Tatsachen von fehlenden Belegen (Liquiditätsplan 24 Monate, Erfolgsplan, Bilanz), nennt pro Lücke Beweisthema, Beschaffungsweg (Insolvenzgericht), Frist... |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter: Antragspflicht § 15a InsO sechs Woche... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Fortbestehensprognose. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Fortbestehensprognose. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Fortbestehensprognose. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Maßstab ueberwiegende Wahrscheinl... |
| `zwoelf-verhandlung-vergleich-und-eskalation` | Zwoelf: Verhandlung, Vergleich und Eskalation im Fortbestehensprognose. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
