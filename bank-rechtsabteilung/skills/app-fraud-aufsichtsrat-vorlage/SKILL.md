---
name: app-fraud-aufsichtsrat-vorlage
description: "APP Fraud Aufsichtsrat Vorlage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# APP Fraud Aufsichtsrat Vorlage

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **APP Fraud Aufsichtsrat Vorlage** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `app-fraud-social-engineering-bank` | APP-Fraud, PushTAN und Social Engineering aus Bankensicht prüfen: Kundenschutz, Warnpflichten, PSD2/BGB-Haftung, SCA, Empfängerbank, Freeze, Recall und Prozessstrategie. |
| `aufsichtsrat-vorlage-bank` | Aufsichtsrats- und Ausschussvorlagen einer Bank vorbereiten: Informationspflicht, Beschlusskompetenz, Risikoausschuss, Prüfungsausschuss, Vertraulichkeit, Protokollfestigkeit und Follow-up. |
| `avalrahmenlinie-kautionsaval-praxis` | Avalrahmen und Kautionsaval in der Bankpraxis prüfen: Kreditgeschäft, Avalprovision, Limit, Sicherheiten, Abrufrisiko, Text der Garantie/Bürgschaft, § 1 KWG, §§ 765 ff. BGB, §§ 349 und 350 HGB und Regress sauber dokumentieren. |
| `bafin-kommunikation-und-anhoerung` | BaFin-Kommunikation und Anhörung: Antwortstrategie, Tonfall, Tatsachenklärung, Fristen, Vollständigkeit, Anerkenntnisrisiken, Aufsichtsdialog und Vorstandsinformation für Banken strukturieren. |
| `bafin-pruefung-vor-ort-management` | Vor-Ort-Prüfung, Sonderprüfung oder Aufsichtsprüfung in der Bank vorbereiten: Datenraum, Interviewliste, Kommunikationsregeln, Prüfungslog, Legal Privilege, Nachlieferungen und Abschlussbericht managen. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **APP Fraud Aufsichtsrat Vorlage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `app-fraud-social-engineering-bank`

**Fokus:** APP-Fraud, PushTAN und Social Engineering aus Bankensicht prüfen: Kundenschutz, Warnpflichten, PSD2/BGB-Haftung, SCA, Empfängerbank, Freeze, Recall und Prozessstrategie.

# APP-Fraud Bank

## Fachkern: APP-Fraud Bank
- **Spezialgegenstand:** APP-Fraud Bank. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Kunde wurde zu autorisierter Überweisung verleitet oder Bank will Betrugsprävention und Haftung bewerten.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Timeline, Anrufe, TAN-Freigabe, Warnungen, Empfänger, Recall, Logs, Polizeianzeige, Kundenprofil.
- **Institut und Rolle:** Bank, Zahlungsinstitut, E-Geld-Institut, Wertpapierinstitut, CRR-Kreditinstitut, FinTech-Tochter, Vermittler, Agent, Registerführer, CASP, Emittent oder Dienstleister.
- **Produkt oder Vorgang:** Zahlungsdienst, E-Geld, Kredit, Wertpapier, Token, Register, Organwechsel, Auslagerung, Betrugsfall, Trade Finance oder Kooperation.
- **Aufsicht und Einreichweg:** BaFin, Bundesbank, EZB/SSM, EBA, FIU, Register, MVP, IMAS, Bundesanzeiger, Handelsregister oder interner Ausschuss.
- **Dokumente:** Produktbeschreibung, Flow-of-Funds, Vertragsentwurf, API-Doku, Token Terms, Organ-CV, Eignungsmatrix, Registerauszug, Kundenkommunikation, Logs oder Vorstandsvorlage.

## Prüfaufbau

### 1. Kurzbild

| Punkt | Klärung |
| --- | --- |
| Ergebnisbedarf | Vermerk, Freigabe, BaFin-Anfrage, Vertrag, Vorstandsvorlage oder Prozessstrategie |
| Rechtsregime | KWG, ZAG, WpHG, WpIG, eWpG, MiCAR, DORA, GwG, BGB, HGB, AktG, SEPA-/EU-Regime oder Entwurf |
| Risiko | Aufsicht, Bußgeld, Zivilhaftung, Organhaftung, Kundenstreit, AML, Datenschutz, IT oder Reputation |
| Frist | Anzeige, Launch, Antwort, Rückgabe, Register, Gremium oder Verjährung |
| Entscheidung | Go, Go mit Auflagen, Stop, BaFin-Vorabklärung oder externe Spezialprüfung |

### 2. Subsumtion und Geschäftsmodell

Arbeite in dieser Reihenfolge:

1. Lebenssachverhalt und Rollen in einfachen Sätzen festhalten.
2. Geld-, Daten-, Wertpapier- oder Tokenfluss als Tabelle beschreiben.
3. Tatbestandsmerkmale einzeln prüfen.
4. Ausnahmen, Privilegierungen, Bestandsschutz, Übergangsregeln oder Entwurfsstand gesondert behandeln.
5. Gegenargumente und Red-Team-Sicht der Aufsicht formulieren.
6. Praktische Auflagen für Launch, Fortführung, Korrektur oder Ablehnung schreiben.

### 3. Beleg- und Unterlagenliste

| Frage | Beleg | Fehlt | Owner | Wirkung |
| --- | --- | --- | --- | --- |
| Wer erbringt welche Leistung? | Vertrag, Produktbild, Prozess | ... | Legal/Produkt | Regimewahl |
| Fließen Kundengelder oder Kryptowerte? | Flow-of-Funds, Wallet-/Kontoauszug | ... | Operations/Risk | Erlaubnis/Haftung |
| Gibt es Aufsichtskontakt? | Schreiben, Ticket, Portalnachweis | ... | Legal/Compliance | Frist/Strategie |
| Sind Kunden betroffen? | AGB, FAQ, Beschwerde, Marketing | ... | Vertrieb/Legal | Transparenz/Haftung |

### 4. Ergebnis

Erzeuge Haftungsanalyse, Sofortmaßnahmen, Kundenantwort, Beweisfragen und Präventions-Backlog.

Baue das Ergebnis mit diesen Elementen:

- **Entscheidungssatz:** Ein Satz, der intern zitiert werden kann.
- **Risikoampel:** Rot/Gelb/Grün mit kurzer Begründung.
- **Auflagen:** Welche Bedingungen müssen vor Go-Live oder vor Antwort erfüllt sein?
- **Offene Punkte:** konkrete Rückfragen statt allgemeiner Rechercheaufträge.
- **Anschluss-Skills:** passende Skills aus `bank-rechtsabteilung` nennen, insbesondere `bafin-kommunikation-und-anhoerung`, `bankaufsichtsrecht-kwg-marisk-triage`, `dora-ict-vertraege-vorfall`, `gwg-aml-kyc-verdachtsmeldung`, `vorstandsvorlage-gutachten` oder `produktfreigabe-new-product-process`.

## Spezialhinweise

- **PSD3/PSR:** Als EU-Gesetzgebungsvorschau behandeln, bis finaler Text und nationale Umsetzung/Anpassung greifbar sind. Keine Scheingeltung behaupten.
- **eWpG/MiCAR:** Immer zuerst trennen, ob der Token ein Finanzinstrument, elektronisches Wertpapier, Kryptowert, E-Geld-Token, vermögenswertreferenzierter Token oder etwas anderes ist.
- **ZAG:** Zahlungsfluss und Besitz an Kundengeldern sind zentral. Grafische Flow-of-Funds-Logik in Worte übersetzen.
- **Geschäftsleiter/FAP:** Nicht nur Einzelperson prüfen, sondern Kollektiveignung, Zeitverfügbarkeit, Interessenkonflikte und Einreichkanal.
- **Tokenisierung:** Keine Technikromantik. Rechtsposition, Register, Verwahrung, Übertragung, Verlustfall, Kundenschutz und Aufsicht zuerst.

## APP-Fraud-Spezifika
- Autorisierte vs. nicht autorisierte Zahlung: § 675u BGB (nicht autorisiert, Bank haftet) vs. § 675v BGB (Mitverschulden bei autorisierter Zahlung). Bei APP-Fraud regelmäßig "autorisiert" — Erstattung nur nach AGB oder ex gratia.
- Warnpflichten: Risikohinweise bei verdächtigem Empfänger/Betrag/Verhalten; nach PSD3/PSR-Entwurf ggf. erweiterte Refund-Pflichten — als Roadmap-Risiko markieren.
- SCA-Befreiung: keine Erleichterung, wenn Kunde aktiv getäuscht wurde; SCA-Logs trotzdem zu Beweiszwecken vorhalten (Art. 97 PSD2 iVm RTS 2018/389).
- Recall/SEPA Recall: über RTS SEPA Credit Transfer Recall Request — sofortige Anfrage Empfängerbank, Frist regelmäßig 10 Bankarbeitstage; Mitwirkungsklausel in AGB nutzen.
- Praktiker-Tipp: APP-Fraud-Playbook mit Eingangsmeldung (Hotline, App-Reporting), Polizeianzeige, Recall innerhalb 24 h, parallel BaFin-Meldung bei Massenfall (MaRisk AT 7.2, BAIT, ggf. § 24 KWG); Schadensquote und Refund-Politik dokumentieren — wird bei BaFin-Prüfungen abgefragt.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 2. `aufsichtsrat-vorlage-bank`

**Fokus:** Aufsichtsrats- und Ausschussvorlagen einer Bank vorbereiten: Informationspflicht, Beschlusskompetenz, Risikoausschuss, Prüfungsausschuss, Vertraulichkeit, Protokollfestigkeit und Follow-up.

# Aufsichtsrat und Ausschüsse

## Fachkern: Aufsichtsrat und Ausschüsse
- **Spezialgegenstand:** Aufsichtsrat und Ausschüsse. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Ein Thema muss in Aufsichtsrat, Risikoausschuss, Prüfungsausschuss oder Nominierungsausschuss.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Thema, Kompetenz, Unterlagen, Vorstandsbeschluss, Risiko, Frist, gewünschte Kenntnisnahme oder Zustimmung.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Liefer Agenda-Punkt, Vorlage, Beschlussformulierung, Protokollhinweis und Q&A für Organmitglieder.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.

## 3. `avalrahmenlinie-kautionsaval-praxis`

**Fokus:** Avalrahmen und Kautionsaval in der Bankpraxis prüfen: Kreditgeschäft, Avalprovision, Limit, Sicherheiten, Abrufrisiko, Text der Garantie/Bürgschaft, § 1 KWG, §§ 765 ff. BGB, §§ 349 und 350 HGB und Regress sauber dokumentieren.

# Avalrahmenlinie und Kautionsaval

## Fachkern: Avalrahmenlinie und Kautionsaval
- **Spezialgegenstand:** Avalrahmenlinie und Kautionsaval. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite Avale als echtes Bankgeschäft, nicht als dekoratives Vertragsanhängsel. Das Ergebnis soll Legal, Marktfolge, Risk und Firmenkundenbetreuung helfen, eine Avalrahmenlinie oder ein Einzelaval schnell, sauber und mit Blick auf Abruf, Regress und Aufsicht zu entscheiden.

**Wann nutzen:** Der Firmenkunde braucht Mietaval, Gewährleistungsaval, Vertragserfüllungsaval, Anzahlungsaval, Zoll-/Steueraval oder Prozess-/Bietungsaval; ein Begünstigter verlangt einen geänderten Text; Risk fragt, ob das noch im Limit ist; ein Aval wird gezogen.

## Sofortfragen

1. **Welche Art von Aval?** Kautionsaval, Anzahlungsaval, Gewährleistungsaval, Vertragserfüllungsaval, Zollaval, Steueraval, Prozessbürgschaft oder Sondertext.
2. **Wer ist Begünstigter?** Vermieter, Auftraggeber, öffentliche Hand, Zoll, Finanzamt, Gericht, Generalunternehmer, Lieferant oder Konzernpartei.
3. **Rechtsform des Sicherungsmittels:** Bürgschaft, Garantie, Schuldversprechen, Patronat, Standby Letter of Credit oder Mischtext.
4. **Abrufmechanik:** einfacher Abruf, erstes Anfordern, Dokumentenbedingung, Frist, Originalurkunde, Teilabruf, automatische Verlängerung.
5. **Bankrisiko:** Limit, Avalprovision, Besicherung, Rückgriff, Gegenkaution, Cash Cover, Covenants, Sanierungsnähe, Insolvenzanfechtung.

## Normen- und Regimekarte

- **Bankgeschäft:** § 1 Abs. 1 Satz 2 Nr. 2 KWG, wenn Kredit durch Aval/Kreditgewährung im bankaufsichtlichen Sinn relevant wird; interne Kreditkompetenz und MaRisk-Kreditprozess zusätzlich prüfen.
- **Bürgschaft:** §§ 765 bis 778 BGB, insbesondere Schriftform § 766 BGB, Umfang § 767 BGB, Einreden §§ 768 bis 771 BGB, Forderungsübergang § 774 BGB.
- **Kaufmännischer Kontext:** §§ 343 ff., 349, 350 HGB; bei Handelsgeschäft des Bürgen keine Einrede der Vorausklage nach § 349 HGB und keine Schriftform nach § 350 HGB für die dort genannten Erklärungen.
- **Garantie/Schuldversprechen:** §§ 780, 781 BGB, AGB-Kontrolle §§ 305 ff. BGB, Transparenz und überraschende Klauseln.
- **Schnittstellen:** InsO bei Krise, Anfechtung und Regress; Datenschutz/Bankgeheimnis bei Begünstigtenkommunikation; Sanktionen/Exportkontrolle bei grenzüberschreitenden Avalen.

## Prüfworkflow

### 1. Aval-Steckbrief

| Punkt | Eintrag |
| --- | --- |
| Kunde / Gruppe | Schuldner, Mutter, Projektgesellschaft, Konsortialbezug |
| Begünstigter | Name, Land, Rolle, Streitnähe |
| Betrag / Währung | Nennbetrag, Teilabruf, Kumulation mit anderen Linien |
| Laufzeit | fest, unbefristet, auto-renewal, Kündigungsfenster |
| Texttyp | Bankformular, Begünstigtenformular, FIDIC/öffentliche Hand/Sondertext |
| Sicherheiten | Cash Cover, Grundschuld, Globalzession, Patronat, Rang |
| Abrufrisiko | niedrig, mittel, hoch mit Grund |

### 2. Textprüfung

Prüfe den Avaltext in dieser Reihenfolge:

1. **Sicherungszweck:** exakt genug oder gefährlich offen?
2. **Betrag:** Maximalbetrag, Währung, Zinsen, Kosten, Nebenforderungen.
3. **Abrufvoraussetzungen:** Dokumente, Erklärungstext, Frist, Original, elektronische Einreichung.
4. **Einwendungen:** normales Bürgschaftsmodell, selbständige Garantie oder erstes Anfordern?
5. **Verlängerung:** automatische Verlängerung, evergreen clause, Kündigungsfenster, Rückgabe Originalurkunde.
6. **Rechtswahl/Gerichtsstand:** deutsches Recht, ausländisches Recht, Schiedsgericht, zwingende öffentliche Vorgaben.
7. **Bankstandard:** weicht der Text vom Muster ab, und wer darf das freigeben?

### 3. Liquiditäts- und Regresslogik

Avale schmieren Liquidität, weil der Kunde keine Barkaution bindet. Genau deshalb muss die Bank prüfen:

- Wird ein echter Liquiditätsvorteil geschaffen oder nur ein unkontrollierter Eventualkredit?
- Reicht die Avalprovision risikoadäquat aus?
- Ist ein Abruf sofort liquiditätswirksam, und hat der Kunde im Regressfall Mittel?
- Ist Cash Cover geboten, oder genügt die bestehende Sicherheitenstruktur?
- Muss der Abruf im Sanierungsfall mit Forbearance, NPE und Insolvenzanfechtung verknüpft werden?

### 4. Ergebnis

Liefere eine **Avalfreigabe-Notiz**:

- Entscheidung: Freigabe, Freigabe mit Textänderungen, Cash Cover, externe Prüfung oder Stop.
- Textänderungen mit konkretem Klauselvorschlag.
- Limit-/Sicherheitenauswirkung.
- Abruf- und Regressplan.
- Owner: Markt, Marktfolge, Legal, Risk, Operations.

## Red Flags

- Bürgschaft oder Garantie wird sprachlich vermischt.
- "Auf erstes Anfordern" steht versteckt in Begünstigtenformularen.
- Laufzeit ist faktisch unbefristet, weil Rückgabe Originalurkunde nicht erreichbar ist.
- Ausländisches Recht oder Gerichtsstand wird ohne Spezialprüfung akzeptiert.
- Begünstigter kann ohne Bezug zum gesicherten Vertrag ziehen.
- Kunde ist in Krise, und Avalabruf würde sofort Zahlungsunfähigkeit auslösen.

## Anschluss-Skills

- Bei Sicherheitenpaket: `kreditsicherheiten-bestellung-verwertung`.
- Bei Abruf oder Betrugsverdacht: `garantieabruf-missbrauch-und-zahlungsstopp`.
- Bei Sanierungsnähe: `restrukturierung-kreditengagement`, `forbearance-npe-risikoklassifizierung`, `insolvenz-anfechtung-bank`.
- Bei grenzüberschreitendem Trade-Finance-Bezug: `trade-finance-sanctions-lc-guarantee`.

## 4. `bafin-kommunikation-und-anhoerung`

**Fokus:** BaFin-Kommunikation und Anhörung: Antwortstrategie, Tonfall, Tatsachenklärung, Fristen, Vollständigkeit, Anerkenntnisrisiken, Aufsichtsdialog und Vorstandsinformation für Banken strukturieren.

# BaFin-Anhörung und Aufsichtsschreiben

## Fachkern: BaFin-Anhörung und Aufsichtsschreiben
- **Spezialgegenstand:** BaFin-Anhörung und Aufsichtsschreiben. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Ein Schreiben der BaFin, Bundesbank, EZB oder eines Prüfers liegt vor oder eine freiwillige Kontaktaufnahme wird erwogen.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Schreiben, Frist, Aktenzeichen, angefragte Tatsachen, interne Verantwortliche, frühere Korrespondenz, gewünschte Haltung.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Erstelle Antwortarchitektur, Tatsachenmatrix, Freigabekette, Entwurfston und rote Linien.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.

## 5. `bafin-pruefung-vor-ort-management`

**Fokus:** Vor-Ort-Prüfung, Sonderprüfung oder Aufsichtsprüfung in der Bank vorbereiten: Datenraum, Interviewliste, Kommunikationsregeln, Prüfungslog, Legal Privilege, Nachlieferungen und Abschlussbericht managen.

# Prüfung vor Ort managen

## Fachkern: Prüfung vor Ort managen
- **Spezialgegenstand:** Prüfung vor Ort managen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Prüfer kündigen sich an, fordern Daten oder führen Interviews mit Vorstand, Markt, Marktfolge, Compliance, IT oder Revision.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Prüfungsanordnung, Themenkatalog, Fristenplan, Ansprechpartner, Datenraumstruktur, bestehende Findings.
- **Institut:** Rechtsform, Erlaubnisstatus, SSM-/LSI-Status, Geschäftsmodell, Konzernbezug, relevante Tochter oder Zweigniederlassung.
- **Dokumente:** Vertrag, Aufsichtsschreiben, Kreditakte, Sanierungsgutachten, Richtlinie, Vorstandsvorlage, Rechnung, Beschwerde, Registerauszug, Datenraum oder Screenshot.
- **Frist und Forum:** BaFin, Bundesbank, EZB/SSM, FIU, Gericht, Ombudsstelle, Vorstand, Aufsichtsrat, HV, Prüfung, Closing oder interne Deadline.
- **Risikodimension:** Aufsicht, Zivilrecht, Straf-/OWi-Risiko, Organhaftung, Datenschutz, Bankgeheimnis, Reputation, Kosten, Operational Risk.

## Prüfworkflow

### 1. Kurzbild

Fasse in fünf bis acht Zeilen zusammen:

| Punkt | Inhalt |
| --- | --- |
| Vorgang | Was liegt auf dem Tisch? |
| Entscheider | Wer muss freigeben oder informiert werden? |
| Frist | Was läuft wann ab? |
| Primärrecht | Welche Normen oder Behördenstandards tragen die Prüfung? |
| Risiko | Rot, Gelb oder Grün mit einem Satz Begründung. |
| Nächster Schritt | Was sollte die Bank jetzt konkret tun? |

### 2. Rechts- und Governance-Karte

Prüfe je nach Fall insbesondere:

- **Bankaufsicht:** KWG, MaRisk, DORA, CRR/CRD, WpHG, WpIG, ZAG, GwG, BaFin-/Bundesbank-/EBA-/EZB-Vorgaben.
- **Zivilrecht:** BGB-Vertrag, AGB-Kontrolle, Darlehen, Kündigung, Sicherheiten, Haftung, Datenschutz, Geschäftsgeheimnis und Bankgeheimnis.
- **Gesellschaftsrecht:** AktG, GmbHG, Satzung, Geschäftsordnung, Vorstand, Aufsichtsrat, Ausschüsse, HV, Interessenkonflikte und Business Judgment Rule.
- **Kredit und Krise:** Sanierungsgutachten, Fortbestehensprognose, Liquiditätsplanung, Forbearance, Sicherheiten, Insolvenzanfechtung, StaRUG-/InsO-Schnittstelle.
- **Vertrieb:** Handelsvertreterrecht, Vermittler, Provision, WpHG-Vertriebspflichten, Beschwerden, Ombudsmann, Produktfreigabe.
- **Operations:** Auslagerung, IT, Cloud, DORA, Dienstleistersteuerung, interne Richtlinien, Datenraum, Rechnungsreview, Litigation.

### 3. Beleg- und Lückenmatrix

Erstelle eine Tabelle:

| Behauptung oder Risiko | Beleg vorhanden? | Fehlender Beleg | Warum wichtig? | Owner |
| --- | --- | --- | --- | --- |
| ... | ja/nein | ... | ... | ... |

### 4. Entscheidungsvorbereitung

Baue Prüfungsfahrplan, Dokumentenregister, Interview-Briefing, Nachforderungslog und Escalation Memo.

Baue das Ergebnis so, dass ein Syndikus es intern weitergeben kann:

- **Für Vorstand:** stark verdichtete Entscheidung, Optionen, Risiko, Empfehlung, Kosten und Zeitplan.
- **Für Fachbereich:** klare To-dos, keine juristische Überwältigung, aber präzise rote Linien.
- **Für Aufsicht:** faktenstark, vollständig, konsistent, ohne unnötige Selbstbezichtigung oder Spekulation.
- **Für externe Kanzlei:** enger Scope, konkrete Fragen, Budget, Deadline und erwartetes Arbeitsergebnis.

## Stilregeln

- Kurz starten, dann sauber vertiefen.
- Keine Textwüste: Tabellen, Ampeln, Checklisten und Entscheidungssätze nutzen.
- Bei hoher Unsicherheit die Unsicherheit verwertbar machen: welche Tatsache fehlt, wer kann sie liefern, bis wann.
- Keine pauschalen Haftungsausschlüsse in jedem Absatz. Einmal sauber markieren, dann arbeiten.
- Rechtsprechung nur verwenden, wenn Gericht, Entscheidungsform, Datum, Aktenzeichen und freie oder amtliche Quelle geprüft sind.

## Ausgabeformate

Wähle passend oder biete maximal drei Optionen an:

1. **Legal Note** mit Kurzbild, Prüfung, Risikoampel, Empfehlung.
2. **Vorstandsvorlage** mit Beschlussvorschlag und Alternativen.
3. **BaFin-/Bundesbank-Antwortentwurf** mit Tatsachenmatrix.
4. **Vertrags- oder Klauselcheck** mit Änderungsvorschlägen.
5. **Unterlagenliste** für Fachbereich, Kanzlei, Prüfer oder Datenraum.
6. **Red-Team-Check** gegen Aufsicht, Prozessgegner, Verwalter oder interne Revision.


### Anschluss-Skills

- Bei ungeklärter Ausgangslage: `bankrechtsabteilung-kaltstart-routing`.
- Bei Aufsichtsbezug: `bankaufsichtsrecht-kwg-marisk-triage`, `bafin-kommunikation-und-anhoerung` oder `ssm-bundesbank-aufsichtsbrief`.
- Bei Kredit- und Krisenbezug: `kreditentscheidung-weiterfinanzierung`, `stundung-standstill-waiver`, `sanierungsgutachten-idw-s6-bewertung` oder `restrukturierung-kreditengagement`.
- Bei Gremienbezug: `vorstandsvorlage-gutachten`, `aufsichtsrat-vorlage-bank` oder `organhaftung-business-judgment`.
- Bei Dienstleistern und Kanzleien: `outsourcing-externe-dienstleister`, `externe-anwaelte-steuerung` oder `anwaltliche-rechnungen-review`.


## Quellenanker

Nutze vor tragenden Aussagen bevorzugt amtliche oder frei zugängliche Quellen: Gesetze im Internet für KWG, ZAG, WpHG, GwG, HGB, BGB und AktG; BaFin für MaRisk, Merkblätter und Aufsichtsinformationen; EUR-Lex für DORA, CRR/CRD und MiFID; EBA/EZB/Bundesbank für Leitlinien und Aufsichtspraxis. Das Quellenverzeichnis des Plugins liegt in `references/QUELLEN.md`.
