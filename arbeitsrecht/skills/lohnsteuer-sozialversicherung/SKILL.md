---
name: lohnsteuer-sozialversicherung
description: Beurteilt den sozialversicherungsrechtlichen Status (Scheinselbständigkeit, § 7a SGB IV) und lohnsteuerliche Fragen im Arbeitsverhältnis. Lädt, wenn ein Statusfeststellungsverfahren, Scheinselbständigkeit, Nachzahlungspflichten (§ 28e SGB IV), strafrechtliche Risiken (§ 266a StGB) oder die Abgrenzung Arbeitnehmer/Selbständiger zu prüfen ist.
language: de
triggers:
  - "Scheinselbständigkeit"
  - "Statusfeststellungsverfahren"
  - "§ 7a SGB IV"
  - "Sozialversicherungspflicht"
  - "Freier Mitarbeiter Sozialversicherung"
  - "§ 266a StGB"
  - "Nachzahlung Sozialversicherung"
  - "Arbeitnehmer oder Selbständiger"
  - "Lohnsteuer Arbeitnehmer"
  - "§ 28e SGB IV"
---

# Lohnsteuer und Sozialversicherung – Statusfeststellung und Scheinselbständigkeit

## Zweck

Dieser Skill dient der Beurteilung des sozialversicherungsrechtlichen Beschäftigtenstatus sowie damit zusammenhängender lohnsteuerlicher Fragen. Er ist einschlägig, wenn die Abgrenzung zwischen abhängiger Beschäftigung (§ 7 Abs. 1 SGB IV) und selbständiger Tätigkeit rechtlich zu klären ist, ein Statusfeststellungsverfahren nach § 7a SGB IV eingeleitet werden soll oder bereits von der Deutschen Rentenversicherung Bund (DRV) durchgeführt wird, ein Verdacht auf Scheinselbständigkeit besteht (mit Nachzahlungsrisiken nach § 28e SGB IV, § 28p SGB IV) oder strafrechtliche Risiken nach § 266a StGB zu bewerten sind. Der Skill berücksichtigt die BSG-Rechtsprechung zu den Abgrenzungskriterien sowie die steuerrechtliche Einordnung (Lohnsteuer vs. Einkommensteuer / Umsatzsteuer).

## Eingaben

1. **Vertragsgestaltung**: Freier-Mitarbeiter-Vertrag, Dienstvertrag, Werkvertrag – Vertragsurkunde
2. **Tatsächliche Durchführung**: Wie ist die Zusammenarbeit in der Praxis ausgestaltet? (Weisungen, Arbeitszeit, Ort, Eingliederung)
3. **Auftraggeberstruktur**: Wie viele Auftraggeber hat der „Selbständige"? Umsatzverteilung?
4. **Unternehmerisches Risiko**: Eigene Betriebsmittel, eigene Arbeitnehmer, Haftungsrisiko des Auftragnehmers?
5. **Bisherige steuerliche und SV-Behandlung**: Wie wurden Beiträge bisher abgeführt?
6. **Zeitraum**: Seit wann besteht die Zusammenarbeit? (Nachzahlungszeitraum!)
7. **Vorliegen eines DRV-Bescheids**: Statusfeststellungsbescheid vorhanden?
8. **Widerspruch / Klage**: Rechtsmittel eingelegt?
9. **Steuerrechtliche Einordnung**: Gewerbe- oder Freiberufler-Einordnung nach EStG, Umsatzsteuer-Behandlung

## Rechtlicher Rahmen

### Kernvorschriften

- § 7 Abs. 1 SGB IV: Definition der Beschäftigung (nicht selbständige Arbeit; Merkmale: Weisungsgebundenheit, Eingliederung in fremde Organisation)
- § 7a SGB IV: Statusfeststellungsverfahren bei der DRV Bund; Antrag möglich, aber kein Muss; Bescheid mit aufschiebender Wirkung in laufenden Beschäftigungen (§ 7a Abs. 6 SGB IV)
- § 28e SGB IV: Haftung des Arbeitgebers für Gesamtsozialversicherungsbeitrag (Arbeitgeber- und Arbeitnehmeranteil; bei Scheinselbständigkeit: Arbeitgeber trägt Nachzahlung alleine, kein Rückgriff auf Arbeitnehmer für > 3 Monate zurückliegende Zeiträume)
- § 28p SGB IV: Prüfbefugnis der Rentenversicherungsträger bei Arbeitgebern (Betriebsprüfung)
- § 266a StGB: Vorenthalten und Veruntreuen von Arbeitsentgelt (bei vorsätzlichem Nichtabführen von SV-Beiträgen; Strafbarkeit des Arbeitgebers)
- § 19 Abs. 1 EStG: Einkünfte aus nichtselbständiger Arbeit → Lohnsteuerpflicht
- § 15, § 18 EStG: Gewerbliche bzw. freiberufliche Einkünfte bei Selbständigen
- § 41a EStG: Lohnsteuer-Anmeldungspflicht des Arbeitgebers
- §§ 1, 3 LStDV: Arbeitnehmer-Begriff im Lohnsteuerrecht (enger gefasst als SV-Recht, aber in der Praxis weitgehend parallel)

### Leitentscheidungen (BGH-Stil)

- **Abgrenzungskriterien abhängige Beschäftigung / Selbständigkeit:**
  BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R, NZS 2019, 940 Rn. 14 ff.: Für die Beurteilung des sozialversicherungsrechtlichen Status ist das Gesamtbild der Tätigkeit maßgeblich; abzustellen ist auf die tatsächlichen Verhältnisse der Durchführung (nicht nur den Vertragswortlaut); Weisungsgebundenheit hinsichtlich Zeit, Dauer, Ort und Art der Tätigkeit sowie Eingliederung in die Organisation des Auftraggebers sprechen für eine abhängige Beschäftigung; allein ein Freier-Mitarbeiter-Vertrag genügt nicht für die Annahme von Selbständigkeit.

- **Einzelfallabwägung / unternehmerisches Risiko:**
  BSG, Urt. v. 14.03.2018 – B 12 R 3/17 R, NZS 2018, 668 Rn. 18 ff.: Das unternehmerische Risiko – insbesondere der Einsatz eigenen Kapitals und eigener Betriebsmittel mit dem Risiko des Verlusts – ist ein gewichtiges Indiz für Selbständigkeit; das Fehlen eigener Arbeitnehmer oder eigener Betriebsmittel spricht hingegen für abhängige Beschäftigung. Der bloße Wille der Parteien zur Selbständigkeit ist für sich allein nicht maßgeblich, wenn die tatsächlichen Verhältnisse dagegen sprechen.

- **Rückwirkung des Statusfeststellungsbescheids:**
  BSG, Urt. v. 11.03.2009 – B 12 R 11/07 R, BSGE 103, 17 = NZS 2009, 558 Rn. 24: Der Statusfeststellungsbescheid der DRV Bund entfaltet keine Rückwirkung auf abgeschlossene Zeiträume; für diese gelten die allgemeinen Verjährungs- und Verwirkungsregeln; ab Einleitung des Statusfeststellungsverfahrens können SV-Beiträge bis zur Entscheidung im Falle der Feststellung als Beschäftigter nachgefordert werden.

- **§ 266a StGB / Vorsatz:**
  BGH, Urt. v. 15.10.1996 – 1 StR 205/96, BGHSt 42, 268 = NJW 1997, 265 Rn. 11: Das Vorenthalten von SV-Beiträgen nach § 266a StGB setzt (bedingten) Vorsatz voraus; wer ernsthaft zweifelt, ob ein Beschäftigungsverhältnis vorliegt, und es auf die gerichtliche Klärung ankommen lässt, handelt nicht strafbar, sofern keine offensichtliche Pflichtwidrigkeit vorliegt.

### Kommentarliteratur

- Segebrecht, in: jurisPK-SGB IV, 4. Aufl. 2021 (Stand 15.03.2024), § 7a Rn. 1 ff. (Statusfeststellungsverfahren, Antragstellung, Bindungswirkung, Rückwirkungsproblematik).
- Plagemann, in: Hauck/Noftz, SGB IV, 3. Lfg. 2023, § 7a Rn. 5 ff. (Verfahrensablauf, aufschiebende Wirkung, Verhältnis zur Betriebsprüfung).
- Schlegel, in: jurisPK-SGB IV, 4. Aufl. 2021 (Stand 01.01.2024), § 28e Rn. 1 ff. (Gesamtsozialversicherungsbeitrag, Haftung, Rückgriff).
- Fischer, in: Fischer, StGB, 71. Aufl. 2024, § 266a Rn. 5 ff. (Tatbestandsmerkmale, Vorsatz, Täterschaft, Strafbarkeit des faktischen Geschäftsführers).

## Ablauf

### Schritt 1 – Abgrenzungsprüfung: Abhängige Beschäftigung oder Selbständigkeit?

**Prüfschema (Gesamtbildbetrachtung nach § 7 Abs. 1 SGB IV):**

| Kriterium | Für abhängige Beschäftigung | Für Selbständigkeit |
|---|---|---|
| Weisungsgebundenheit | Weisungen zu Zeit, Ort, Art der Tätigkeit | Freie Zeiteinteilung, eigene Methodenfreiheit |
| Eingliederung | In Betriebsorganisation eingebunden; Dienstplan, Arbeitskleidung, IT des AG | Eigene Betriebsstruktur, eigene IT |
| Eigene Betriebsmittel | Fehlen wesentlicher eigener Betriebsmittel | Erhebliche eigene Investitionen |
| Unternehmerisches Risiko | Monatlich fixer Vergütungsanspruch | Variables Entgelt, Verlustrisiko |
| Mehrere Auftraggeber | Nur ein Auftraggeber (Indiz für Scheinselbständigkeit) | Viele Auftraggeber |
| Eigene Arbeitnehmer | Keine eigenen AN | Beschäftigt eigene AN |
| Auftreten am Markt | Kein Auftritt als Unternehmer | Eigene Werbung, Kunden etc. |

- Maßgeblich ist das **Gesamtbild** (BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R, NZS 2019, 940 Rn. 14); kein einzelnes Merkmal ist allein entscheidend.
- **Vertragswortlaut ist nicht maßgeblich**, wenn tatsächliche Durchführung abweicht.

### Schritt 2 – Statusfeststellungsverfahren (§ 7a SGB IV)

- **Antragsberechtigt**: Auftraggeber oder Auftragnehmer, ggf. Einzugsstelle.
- **Zuständig**: Deutsche Rentenversicherung Bund (DRV Bund), Clearingstelle.
- **Verfahrensablauf**: Antragstellung → Anhörung beider Parteien → Bescheid; aufschiebende Wirkung für laufende Aufträge bis Entscheidung (§ 7a Abs. 6 SGB IV, kein Beitragsrisiko für Übergangszeit, wenn Antrag rechtzeitig gestellt).
- **Bindungswirkung**: Bescheid bindet alle Sozialversicherungsträger; Widerspruch und Klage zum Sozialgericht (§§ 84, 87 SGG) möglich.
- **Strategische Empfehlung**: Proaktive Antragstellung bei Zweifeln minimiert Nachzahlungsrisiko und strafrechtliche Exposition.

### Schritt 3 – Folgen bei Feststellung als abhängige Beschäftigung

**Sozialversicherung:**
- Nachzahlungspflicht für Gesamtsozialversicherungsbeitrag (Arbeitgeber- + Arbeitnehmeranteil) nach § 28e SGB IV; **Verjährung: 4 Jahre** (§ 25 Abs. 1 SGB IV), bei Vorsatz 30 Jahre.
- Kein Rückgriff des Arbeitgebers auf den Arbeitnehmer für mehr als **3 Monate** rückwirkend (§ 28g Satz 3 SGB IV).
- Säumniszuschläge § 24 SGB IV (1 % pro angefangenem Kalendermonat).

**Lohnsteuer:**
- Pflicht zur Lohnsteuer-Anmeldung (§ 41a EStG); Nachzahlung mit Haftung des Arbeitgebers (§ 42d EStG).
- Bereits gezahlte Einkommensteuer des Auftragnehmers wird angerechnet.

**Strafrechtlich:**
- § 266a StGB: Strafbarkeit des Arbeitgebers (Geschäftsführer, Vorstand) bei vorsätzlichem Vorenthalten von Beiträgen; Freiheitsstrafe bis zu 5 Jahren oder Geldstrafe.
- Strafbarkeit nur bei Vorsatz (BGH, Urt. v. 15.10.1996 – 1 StR 205/96, BGHSt 42, 268 Rn. 11); fahrlässiges Handeln genügt nicht.
- Selbstanzeige / Nachentrichten: Bei § 266a StGB existiert – anders als bei § 371 AO – keine strafbefreiende Selbstanzeige; freiwillige Nachzahlung ist aber strafmildernd.

### Schritt 4 – Gestaltungsoptionen und Risikominimierung

1. **Vertragsgestaltung anpassen**: Weisungsrechte vertraglich und praktisch reduzieren, mehrere Auftraggeber fördern.
2. **Statusfeststellungsverfahren proaktiv stellen** → schützt vor rückwirkenden Forderungen für Zeitraum ab Antragstellung.
3. **Umwandlung in Arbeitsverhältnis**: Wenn Scheinselbständigkeit nahe liegt, geordnete Überführung in abhängige Beschäftigung mit klaren Verträgen.
4. **Betriebsprüfung (§ 28p SGB IV)**: Auf kommende Prüfungen durch DRV vorbereiten; Dokumentation der tatsächlichen Verhältnisse.
5. **Steuerberatung**: Lohnsteuerliche Folgen (§§ 41a, 42d EStG) mit Steuerberater abstimmen.

### Schritt 5 – Besonderheiten Freiberufler

- Freiberufler nach § 18 EStG unterliegen keiner Gewerbesteuer, jedoch ggf. der SV-Pflicht als Beschäftigte, wenn Eingliederung vorliegt.
- Künstlerische und publizistische Tätigkeiten → Künstlersozialversicherung (KSVG) prüfen: Abgabepflicht des Auftraggebers (§§ 24, 25 KSVG).
- Honorarärzte: besondere BSG-Rechtsprechung (BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R, NZS 2019, 940 Rn. 30 ff.) → Eingliederung in Krankenhausorganisation besonders gewichtig.

## Ausgabeformat

- **Standardausgabe**: Rechtliches Memo (Gutachtenstil) mit tabellarischer Kriterienprüfung und Risikoabschätzung.
- **Auf Anforderung**: Antrag auf Statusfeststellung nach § 7a SGB IV (Entwurf).
- **Auf Anforderung**: Checkliste Kriterien Scheinselbständigkeit als Tabelle.
- **Auf Anforderung**: Strafbarkeitsrisiko § 266a StGB als separate Bewertung.

## Beispiel

**Sachverhalt:** Unternehmen U-GmbH beschäftigt seit 3 Jahren Herr F als „freien IT-Berater" auf Honorarbasis (Monatshonorar 7.500 €). F arbeitet ausschließlich für U-GmbH, nutzt U-GmbHs IT-Infrastruktur, ist in den Projektmanagementprozess eingebunden und erhält Weisungen vom Projektleiter der U-GmbH. Ein eigenes Büro oder eigene Arbeitnehmer hat F nicht.

**Ergebnis:** Erhebliche Indizien sprechen für abhängige Beschäftigung, Scheinselbständigkeit liegt nahe.

**Bewertung:**
*Weisungsgebundenheit:* F erhält Weisungen vom Projektleiter der U-GmbH hinsichtlich Arbeitsinhalt, Ort (IT-Infrastruktur) und Einbindung in Prozesse. Das spricht nach BSG, Urt. v. 04.06.2019 – B 12 R 11/18 R, NZS 2019, 940 Rn. 14 für eine abhängige Beschäftigung.

*Eingliederung:* F ist in die Organisation der U-GmbH eingebunden (Projektmanagement, fremde IT).

*Unternehmerisches Risiko:* F hat keine eigenen Betriebsmittel und keinen eigenen Marktauftritt. Kein unternehmerisches Risiko erkennbar (BSG, Urt. v. 14.03.2018 – B 12 R 3/17 R, NZS 2018, 668 Rn. 18).

*Empfehlung:* Statusfeststellungsverfahren nach § 7a SGB IV sofort einleiten (schützt vor weiterer Beitragshaftung für Zeitraum ab Antragstellung); SV-Nachzahlung für 3 Jahre bei 7.500 €/Monat Brutto kalkulieren; strafrechtliches Risiko § 266a StGB prüfen (Segebrecht, in: jurisPK-SGB IV, 4. Aufl. 2021, § 7a Rn. 15).

## Risiken und typische Fehler

| Fehler | Konsequenz | Abhilfe |
|---|---|---|
| Kein Statusfeststellungsverfahren trotz Zweifeln | Rückwirkende Nachzahlung; § 266a StGB | Proaktiv § 7a SGB IV beantragen |
| Vertrag „Freier Mitarbeiter" ohne tatsächliche Umsetzung | Scheinselbständigkeit; Nachzahlungspflicht § 28e SGB IV | Vertragsgestaltung und tatsächliche Durchführung abstimmen |
| Vorsätzliches Nichtabführen | § 266a StGB, Freiheitsstrafe bis 5 Jahre | Sofortige Klärung und Nachentrichten |
| Vergessen: KSVG-Abgabepflicht | Nachzahlung KSVG-Abgabe | Künstler/Publizisten gesondert prüfen |
| Falsche Steuererklärung des Auftragnehmers | § 370 AO; Nachzahlung; Berichtigungspflicht | Steuerberater einschalten |
| Keine Dokumentation der tatsächlichen Verhältnisse | Beweisproblem bei Betriebsprüfung | Tatsächliche Leistungserbringung laufend dokumentieren |
| § 203 StGB / Datenschutz | Strafbarkeit bei unbefugter Datenweitergabe | Personalstammdaten nur in zulässigen Systemen |
| Rückgriff auf Arbeitnehmer > 3 Monate | § 28g Satz 3 SGB IV schließt das aus | Nur bis 3 Monate rückwirkender Rückgriff zulässig |

**Beweislast:** Im Statusfeststellungsverfahren trägt der Antragsteller die Darlegungs- und Beweislast für die tatsächlichen Verhältnisse; im Beitragsstreit trägt die DRV/Einzugsstelle die Beweislast für das Bestehen einer Versicherungspflicht (Plagemann, in: Hauck/Noftz, SGB IV, 3. Lfg. 2023, § 7a Rn. 12).

## Quellenpflicht

Jede juristische Aussage in jedem auf diesem Skill basierenden Dokument ist nach **references/zitierweise.md** zu belegen:

- Rechtsprechungsbelege im BGH-Stil; bei BSG-Entscheidungen BSGE-Fundstelle bevorzugen, hilfsweise NZS oder juris.
- Kommentarbelege mit Bearbeiter, Werk, Auflage/Edition, Jahr (ggf. Stand), §, Rn.
- Steuerrechtliche Aussagen mit BFH-Nachweis (BStBl.-Fundstelle).
- Strafrechtliche Aussagen mit BGH-Nachweis (BGHSt oder NJW-Fundstelle).
- Bei umstrittenen Fragen (z. B. Abgrenzung tatsächliche vs. vertragliche Verhältnisse) h. M. und Gegenauffassung getrennt nennen.
- Halluzinationsrisiko: Alle Aktenzeichen und Fundstellen vor Einreichung bei DRV, Sozialgericht oder Finanzgericht verifizieren.
