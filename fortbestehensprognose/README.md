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

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
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
| `annahmen-behoerden-gericht-und-registerweg` | Annahmen: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägigen... |
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz vs Material vs Per... |
| `annahmen-sammeln-bilanzieller-status` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand Kunden-Konzentration Markt-... |
| `anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK Liquiditaetsengpass... |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten und außerbilanzielle... |
| `bilanzstatus-risikoampel-und-gegenargumente` | Bilanzstatus: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret... |
| `comfortletter-sonderfall-edge` | Comfortletter: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einsc... |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht rechtsverbindlich durchsetzb... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `eskalation-sonderfall-und-edge-case` | Eskalation: Sonderfall und Edge-Case-Prüfung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägigen Ta... |
| `fbp-bankenkommunikation-waiver-integrierte` | Spezialfall Bankenkommunikation und Waiver / Standstill bei drohender Zahlungsunfaehigkeit: Konsortium, Sicherheitenpool, MAC-Klausel. Pruefraster für Geschaeftsleitung und Treuhaender im Fortbestehensprognose: prüft konkret die einschlä... |
| `fbp-integrierte-planung-bauleiter` | Bauleiter integrierte Planung GuV, Bilanz, Cashflow für IDW S 11. Pruefraster für Planungsschritte, Annahmen, Sensitivitaeten. Mustertext Annahmenverzeichnis im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale,... |
| `fbp-stresstest-szenarien-leitfaden` | Leitfaden Stresstest- und Szenarien-Aufbau für Fortbestehensprognose: Basis-, Stress- und Worst-Case, KPIs, Trigger für Massnahmen. Pruefraster für Beraterhand und Geschaeftsleitung im Fortbestehensprognose: prüft konkret die einschlägig... |
| `fbp-zahlungsunfaehigkeit` | Spezialfall Abgrenzung Zahlungsunfaehigkeit und Ueberschuldung § 17 / § 19 InsO: Liquiditaetsstatus 21-Tage-Frist, Fortfuehrungsprognose, BGH-Rechtsprechung. Pruefraster für Geschaeftsleitung im Fortbestehensprognose: prüft konkret die e... |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die ve... |
| `forderungsverzicht-mandantenentscheidung` | Forderungsverzicht: Mandantenkommunikation und Entscheidungsvorlage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkr... |
| `fortbestehensdokumentation-insolvenzrecht` | Fortbestehensdokumentation mit insolvenzrechtlicher Tragfähigkeit: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Fortbestehensprognose: prüft konkret die einschlägige... |
| `fortbestehensprognose-erstpruefung-und-mandatsziel` | Fortbestehensprognose: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret... |
| `fp-cash-flow-modell-spezial` | Spezialfall Cash-Flow-Modell: monatliche Liquiditaetsplanung mindestens für 12 Monate, Plausibilitaetskontrollen, Sensitivitaetsanalysen. Pflichten Geschaeftsfuehrer und Pruefer. Pruefraster und Praxistipps im Fortbestehensprognose: prüf... |
| `fp-dokumentation-gerichtsfaehigkeit` | Spezialfall Dokumentation und Gerichtsfaehigkeit: was muss in der Akte, wann ist die Prognose strafrechts- und haftungsfest, Aktualisierung bei wesentlicher Aenderung. Standard für Auditoren-Akzeptanz und Insolvenzverwalter-Pruefung im F... |
| `fp-einfuehrung-pflicht-und-zweck` | Fortbestehensprognose einfuehrend: Pflicht zur Erstellung bei Anhaltspunkten für Zahlungsunfaehigkeit, Geltung im Sinne § 19 InsO Ueberschuldungspruefung, Verzahnung mit Krisenfrueherkennung StaRUG § 1. Wer muss erstellen, wann, wozu im... |
| `fp-zeitraum-und-szenarien-praxis` | Fortbestehensprognose-Zeitraum 12 Monate seit SanInsFoG, ueblicher Praxis-Korridor: konservativ, mittel, optimistisch. Aufbau Szenarienrechnung in der Praxis. IDW S 11 Ueberschuldung und IDW S 6 Sanierungskonzept Bezug im Fortbestehenspr... |
| `geschaeftsfuehrer-fristen-form-und-zustaendigkeit` | Geschaeftsfuehrer: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die... |
| `gesellschafterdarlehen-rangruecktritt` | Prüfungslinie für gesellschafterdarlehen rangruecktritt: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Fortbestehensprognose: prüft konkret di... |
| `inso-tatbestand-beweis-und-belege` | InsO: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschl... |
| `kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und steuerliche Ansprechpartner... |
| `liquiditaet-12-monate` | Prüfungslinie für liquiditaet 12 monate: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Fortbestehensprognose: prüft konkret die einschlägigen... |
| `liquiditaet-patronatserklaerung-interessen` | Liquiditaet: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägi... |
| `mandantenkommunikation-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec... |
| `monats-quellenkarte` | Monats Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `negativer-fristennotiz-ausloesendes-ereignis` | Negativer: Fristennotiz und nächster Schritt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägigen Ta... |
| `output-waehlen` | Output wählen im Plugin Fortbestehensprognose: Diese Output-Weiche für Fortbestehensprognose entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `patronatserklaerung-extern-hart-erzeugen` | Prüfungslinie für patronatserklaerung extern hart erzeugen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle im Fortbestehensprognose: prüft konkret... |
| `patronatserklaerung-mehrparteien-konflikt-und-interessen` | Patronatserklaerung: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret di... |
| `plausibilisierung-schriftsatz-brief-und-memo-bausteine` | Plausibilisierung: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die ei... |
| `prognose-stichtag-stundungsanfrage-glaeubiger` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg gegenüber dem Gesc... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rangruecktritt-sanierungsbausteine` | Rangruecktritt: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einsch... |
| `sanierungsbausteine-compliance-dokumentation-und-akte` | Sanierungsbausteine: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret di... |
| `sanierungsbausteine-vorschlagen-annahmen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit Rangrücktritt Stundungsvereinb... |
| `selbstdokumentation-dokumentenmatrix-und-lueckenliste` | Selbstdokumentation: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konk... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `starug-beweislast-stundung-red-zwoelf` | StaRUG: Beweislast, Darlegungslast und Substantiierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einsch... |
| `stundung-red-team-und-qualitaetskontrolle` | Stundung: Red-Team und Qualitätskontrolle; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägigen Tatbe... |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause) Begründung Sicherheit... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `wenn-prognose` | Wenn Prognose im Plugin Fortbestehensprognose im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Ar... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Li... |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Lief... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Fortbestehensprognose: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefe... |
| `zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab ueberwiegende Wahrschein... |
| `zwoelf-verhandlung-vergleich-und-eskalation` | Zwoelf: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Fortbestehensprognose: prüft konkret die einschlägigen T... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
