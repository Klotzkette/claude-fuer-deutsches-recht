---
name: psd2-provisionsmodelle-vertrieb-fraud-refund
description: "Psd2 Provisionsmodelle Vertrieb Fraud Refund: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Psd2 Provisionsmodelle Vertrieb Fraud Refund

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Psd2 Provisionsmodelle Vertrieb Fraud Refund** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `provisionsmodelle-vertrieb-compliance` | Provisionsmodelle und Vertriebscompliance prüfen: Zuwendungen, Interessenkonflikte, MiFID, Verbraucherschutz, Vergütungsrichtlinien, Zielvorgaben und Vorstandsvorlage für Produktvertrieb. |
| `psd2-fraud-refund-unauthorised-payment` | Unautorisierte Zahlung und Refund nach PSD2/BGB prüfen: § 675u BGB, § 675v BGB, grobe Fahrlässigkeit, Social Engineering, Beweislast, SCA-Logs und Vergleichsstrategie. |
| `psd2-open-banking-api-xs2a` | Open-Banking- und XS2A-Schnittstellen prüfen: Zugang zu Zahlungskonten, API-Verfügbarkeit, Fallback, TPP-Kommunikation, Consent, Sicherheit, Haftung und Aufsichtsbeschwerde. |
| `psd2-sca-strong-customer-authentication` | Starke Kundenauthentifizierung nach PSD2 prüfen: Zwei-Faktor-Logik, Ausnahmen, Transaktionsrisikoanalyse, App-Freigabe, Delegation, Betrugsfall und Kundenkommunikation. |
| `psd3-psr-vorschau-gap-analysis` | PSD3- und PSR-Vorschau für Banken: geplantes EU-Zahlungsdienste-Paket gegen bestehende PSD2/ZAG-Prozesse mappen, Fraud, Open Banking, Transparenz und organisatorische Gaps vorbereiten. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **Psd2 Provisionsmodelle Vertrieb Fraud Refund**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `provisionsmodelle-vertrieb-compliance`

**Fokus:** Provisionsmodelle und Vertriebscompliance prüfen: Zuwendungen, Interessenkonflikte, MiFID, Verbraucherschutz, Vergütungsrichtlinien, Zielvorgaben und Vorstandsvorlage für Produktvertrieb.

# Provision und Vertriebscompliance

## Fachkern: Provision und Vertriebscompliance
- **Spezialgegenstand:** Provision und Vertriebscompliance. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Neue Incentives, Kampagnen, Vermittlervergütung oder variable Vergütung sollen freigegeben werden.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Modell, Produkt, Zielgruppe, Vergütungsparameter, Interessenkonflikte, Kontrollprozess.
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

Liefer Compliance-Review, Anpassungsvorschläge, Freigabeauflagen und Kommunikation an Vertrieb.

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

## 2. `psd2-fraud-refund-unauthorised-payment`

**Fokus:** Unautorisierte Zahlung und Refund nach PSD2/BGB prüfen: § 675u BGB, § 675v BGB, grobe Fahrlässigkeit, Social Engineering, Beweislast, SCA-Logs und Vergleichsstrategie.

# Unautorisierte Zahlung und Fraud

## Fachkern: Unautorisierte Zahlung und Fraud
- **Spezialgegenstand:** Unautorisierte Zahlung und Fraud. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Kunde verlangt Erstattung wegen Phishing, PushTAN, Call-ID-Spoofing, APP-Fraud oder Kartenmissbrauch.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Zahlungen, Authentifizierung, Kundenvortrag, Warnhinweise, Logs, Gerät, Bankkommunikation, Anzeige.
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

Liefer Anspruchsprüfung, Beweislastmatrix, Kundenantwort, Prozessrisiko und Vergleichskorridor.

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

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 3. `psd2-open-banking-api-xs2a`

**Fokus:** Open-Banking- und XS2A-Schnittstellen prüfen: Zugang zu Zahlungskonten, API-Verfügbarkeit, Fallback, TPP-Kommunikation, Consent, Sicherheit, Haftung und Aufsichtsbeschwerde.

# PSD2 Open Banking API

## Fachkern: PSD2 Open Banking API
- **Spezialgegenstand:** PSD2 Open Banking API. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank muss Drittanbietern Schnittstellenzugang geben oder verteidigt API-Ausfälle, Sperren oder technische Barrieren.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** API-Dokumentation, TPP, Logs, Sperrgrund, Consent, SLA, Incident, Beschwerden.
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

Erzeuge Schnittstellenprüfung, TPP-Antwort, Aufsichtsrisiko, technische Nachfragen und Maßnahmenplan.

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

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 4. `psd2-sca-strong-customer-authentication`

**Fokus:** Starke Kundenauthentifizierung nach PSD2 prüfen: Zwei-Faktor-Logik, Ausnahmen, Transaktionsrisikoanalyse, App-Freigabe, Delegation, Betrugsfall und Kundenkommunikation.

# PSD2 SCA

## Fachkern: PSD2 SCA
- **Spezialgegenstand:** PSD2 SCA. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Online-Banking, Karten, App, PIS, Händlerzahlung oder Fraud-Fall berührt starke Kundenauthentifizierung.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Authentifizierungsverfahren, Betrag, Kanal, Ausnahme, Fraud, Logs, Kundenvortrag, Dienstleister.
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

Liefer SCA-Check, Beweismatrix, Haftungsampel, technische Fragen und Antworttext.

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

## SCA-Spezifika (PSD2)
- Rechtsgrundlagen: Art. 97 PSD2 (RL 2015/2366) iVm § 55 ZAG, Delegierte VO (EU) 2018/389 RTS SCA (Regulatory Technical Standards), EBA Final Report on RTS Amendments, EBA Opinions zu SCA.
- Drei-Faktoren-Modell: Wissen (PIN/Passwort), Besitz (Karte/Smartphone), Inhärenz (Biometrie); zwei unabhängige Faktoren aus verschiedenen Kategorien zwingend; "Independence" und "Dynamic Linking" (Art. 5 RTS) bei Überweisungen — Betrag und Empfänger müssen in Auth integriert sein.
- Ausnahmen (Art. 10-18 RTS): Kontoabfragen 90-Tage-Regel (Art. 10 — Anpassung durch Delegierte VO 2022/2360 unter strengeren Bedingungen), Niedrigwertige Zahlungen (Art. 16 — bis 30 EUR/100 EUR kumulativ), Trusted Beneficiary (Art. 13), Transaktionsanalyse mit niedrigem Risk Score (Art. 18); jede Ausnahme dokumentieren und Risiko-Monitoring.
- Haftung: § 675v BGB iVm § 675w BGB — bei fehlender SCA Bank haftet (außer Vorsatz/grobe Fahrlässigkeit Kunde); bei korrekter SCA Beweislast für Authentifizierungsmangel beim Zahler.
- Praktiker-Tipp: Reporting nach Art. 96 PSD2 zu Major Incidents an BaFin/Bundesbank (über MVP); Phishing-Resilience prüfen (Push-Notification-Spam, OAuth-Phishing), Kundenkommunikation klare SCA-Erläuterungen ohne irreführende Versprechen; Bei Reklamation forensische Logs (Device-Fingerprint, Geolocation, Zeitstempel) für Gerichtsverfahren bereithalten.

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?

## 5. `psd3-psr-vorschau-gap-analysis`

**Fokus:** PSD3- und PSR-Vorschau für Banken: geplantes EU-Zahlungsdienste-Paket gegen bestehende PSD2/ZAG-Prozesse mappen, Fraud, Open Banking, Transparenz und organisatorische Gaps vorbereiten.

# PSD3/PSR Vorschau

## Fachkern: PSD3/PSR Vorschau
- **Spezialgegenstand:** PSD3/PSR Vorschau. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Legal soll heute schon wissen, welche Zahlungsdiensteprozesse bei PSD3/PSR wahrscheinlich anzupassen sind.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Bestehende ZAG-Prozesse, Fraud-Prozess, API, Gebühren, AGB, Kundenkommunikation, Roadmap.
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

Erzeuge Gap-Tracker mit Status Entwurf, Monitoring-Punkten, Ownern und Umsetzungsvorbereitung ohne Scheingeltung.

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

## Qualitätsgate

Vor Ausgabe prüfen:

- Steht klar da, was geltendes Recht ist und was Entwurf/Monitoring ist?
- Sind BaFin-/EBA-/EUR-Lex-Quellen als Live-Check markiert, wenn sie tragen?
- Gibt es eine konkrete Unterlagenliste?
- Ist die Bankentscheidung dokumentationsfest?
- Sind keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate enthalten?
