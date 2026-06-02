# Fortbestehensprognose

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fortbestehensprognose`) | [`fortbestehensprognose.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Fortbestehensprognose nach § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Prüfablauf Bilanzstatus Annahmen Plausibilisierung 12-Monats-Liquidität. Sanierungsbausteine harte Patronatserklärung Comfortletter Gesellschafterdarlehen Rangrücktritt Stundung Forderungsverzicht. IDW S 11 S 6 StaRUG. Funktioniert allein; empfohlene Begleitplugins liquiditätsplanung (wochenbasierte Liquidität) und insolvenzrecht (§ 17 § 18 InsO Antragspflicht).

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fortbestehensprognose (`fortbestehensprognose`, dieses Plugin) | [fortbestehensprognose.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fortbestehensprognose.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Zum Ausprobieren: Beispielakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

[testakte-fortbestehensprognose-paragrafix-gmbh.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip)

Fiktive Akte einer mittelständischen GmbH (Paragrafix GmbH) zur Erstellung einer Fortbestehensprognose nach § 19 II InsO: BWA, SuSa, Bilanz, Planungsrechnung, Markt-Annahmen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortfuehrung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Ums… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalität Auftragsbestand Kunden… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem … |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposte… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstützen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechts… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrec… |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquidität Sensitivitätsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueb… |
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

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Per... |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt-... |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass... |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle... |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzb... |
| `fbp-bankenkommunikation-waiver-spezial` | Spezialfall Bankenkommunikation und Waiver / Standstill bei drohender Zahlungsunfaehigkeit: Konsortium, Sicherheitenpool, MAC-Klausel. Pruefraster fuer Geschaeftsleitung und Treuhaender. |
| `fbp-integrierte-planung-bauleiter` | Bauleiter integrierte Planung GuV, Bilanz, Cashflow fuer IDW S 11. Pruefraster fuer Planungsschritte, Annahmen, Sensitivitaeten. Mustertext Annahmenverzeichnis. |
| `fbp-stresstest-szenarien-leitfaden` | Leitfaden Stresstest- und Szenarien-Aufbau fuer Fortbestehensprognose: Basis-, Stress- und Worst-Case, KPIs, Trigger fuer Massnahmen. Pruefraster fuer Beraterhand und Geschaeftsleitung. |
| `fbp-zahlungsunfaehigkeit-ueberschuldungsabgrenzung-spezial` | Spezialfall Abgrenzung Zahlungsunfaehigkeit und Ueberschuldung § 17 / § 19 InsO: Liquiditaetsstatus 21-Tage-Frist, Fortfuehrungsprognose, BGH-Rechtsprechung. Pruefraster fuer Geschaeftsleitung. |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die ve... |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner... |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrschein... |
| `fp-cash-flow-modell-spezial` | Spezialfall Cash-Flow-Modell: monatliche Liquiditaetsplanung mindestens fuer 12 Monate, Plausibilitaetskontrollen, Sensitivitaetsanalysen. Pflichten Geschaeftsfuehrer und Pruefer. Pruefraster und Praxistipps. |
| `fp-dokumentation-gerichtsfaehigkeit-spezial` | Spezialfall Dokumentation und Gerichtsfaehigkeit: was muss in der Akte, wann ist die Prognose strafrechts- und haftungsfest, Aktualisierung bei wesentlicher Aenderung. Standard fuer Auditoren-Akzeptanz und Insolvenzverwalter-Pruefung. |
| `fp-einfuehrung-pflicht-und-zweck` | Fortbestehensprognose einfuehrend: Pflicht zur Erstellung bei Anhaltspunkten fuer Zahlungsunfaehigkeit, Geltung im Sinne § 19 InsO Ueberschuldungspruefung, Verzahnung mit Krisenfrueherkennung StaRUG § 1. Wer muss erstellen, wann, wozu. |
| `fp-zeitraum-und-szenarien-praxis` | Fortbestehensprognose-Zeitraum 12 Monate seit SanInsFoG, ueblicher Praxis-Korridor: konservativ, mittel, optimistisch. Aufbau Szenarienrechnung in der Praxis. IDW S 11 Ueberschuldung und IDW S 6 Sanierungskonzept Bezug. |
| `gesellschafterdarlehen-rangruecktritt` | Workflow-Skill zu gesellschafterdarlehen rangruecktritt. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `liquiditaet-12-monate` | Workflow-Skill zu liquiditaet 12 monate. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `patronatserklaerung-extern-hart-erzeugen` | Workflow-Skill zu patronatserklaerung extern hart erzeugen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Gesc... |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinb... |
| `spezial-annahmen-behoerden-gericht-und-registerweg` | Annahmen: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-bilanzstatus-risikoampel-und-gegenargumente` | Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-comfortletter-internationaler-bezug-und-schnittstellen` | Comfortletter: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-eskalation-sonderfall-und-edge-case` | Eskalation: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-forderungsverzicht-mandantenentscheidung` | Forderungsverzicht: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fortbestehensdokumentation-insolvenzrecht` | Fortbestehensdokumentation mit insolvenzrechtlicher Tragfähigkeit: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-fortbestehensprognose-erstpruefung-und-mandatsziel` | Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Geschaeftsfuehrer: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-inso-tatbestand-beweis-und-belege` | InsO: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-liquiditaet-zahlen-schwellen-und-berechnung` | Liquiditaet: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-monats-livequellen-und-rechtsprechungscheck` | Monats: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-negativer-fristennotiz-und-naechster-schritt` | Negativer: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-patronatserklaerung-mehrparteien-konflikt-und-interessen` | Patronatserklaerung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-plausibilisierung-schriftsatz-brief-und-memo-bausteine` | Plausibilisierung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rangruecktritt-formular-portal-und-einreichung` | Rangruecktritt: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-sanierungsbausteine-compliance-dokumentation-und-akte` | Sanierungsbausteine: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-selbstdokumentation-dokumentenmatrix-und-lueckenliste` | Selbstdokumentation: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-starug-beweislast-und-darlegungslast` | StaRUG: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stundung-red-team-und-qualitaetskontrolle` | Stundung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zwoelf-verhandlung-vergleich-und-eskalation` | Zwoelf: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheit... |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsverbot § 15b InsO. Prüfun... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fortbestehensprognose: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fortbestehensprognose: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fortbestehensprognose: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fortbestehensprognose: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fortbestehensprognose: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fortbestehensprognose: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fortbestehensprognose: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fortbestehensprognose: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fortbestehensprognose: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fortbestehensprognose: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
