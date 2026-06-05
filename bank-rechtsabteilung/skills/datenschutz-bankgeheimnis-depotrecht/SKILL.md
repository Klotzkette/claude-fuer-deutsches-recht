---
name: datenschutz-bankgeheimnis-depotrecht
description: "Datenschutz Bankgeheimnis Depotrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Datenschutz Bankgeheimnis Depotrecht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Datenschutz Bankgeheimnis Depotrecht** im Plugin Bank Rechtsabteilung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `datenschutz-bankgeheimnis` | Datenschutz, Bankgeheimnis und Mandatsgeheimnis in der Bank: Datenbasis, Offenlegung, Dienstleister, Auskunft, Löschung, Behördenzugriff, KI-Nutzung und Geheimnisschutz prüfen. |
| `depotrecht-tokenisierte-wertpapiere` | Depotrecht und tokenisierte Wertpapiere prüfen: Depotvertrag, Verwahrung, Registereintragung, Abwicklung, Bestandsschutz, Anlegerauskunft, Verlustfall und Schnittstelle zu eWpG/MiFID. |
| `dlt-pilot-regime-market-infrastructure` | DLT Pilot Regime für Marktinfrastrukturen prüfen: DLT-MTF, DLT-SS, DLT-TSS, Token Settlement, Ausnahmen, Aufsicht, Depot-/CSD-Schnittstellen und Bankrollen. |
| `dokumentengeschaeft-akkreditiv-inkasso-standby` | Dokumentengeschäft der Bank prüfen: Akkreditiv, Dokumenteninkasso, Standby Letter of Credit, UCP/URC/ISP-Bezug, Dokumentenstrenge, Fraud, Sanktionen, Warenfluss und Zahlungsentscheidung. |
| `dora-art16-vereinfachter-ikt-rahmen` | DORA Artikel 16 für kleinere oder privilegierte Finanzunternehmen: vereinfachten IKT-Risikomanagementrahmen, Governance, Asset-Inventar, Need-to-use, Business Continuity, Drittparteienrisiko, Vertragslücken und Nachweisordner prüfbar machen. |

## Arbeitsweg

Im Plugin Bank Rechtsabteilung gilt für **Datenschutz Bankgeheimnis Depotrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `datenschutz-bankgeheimnis`

**Fokus:** Datenschutz, Bankgeheimnis und Mandatsgeheimnis in der Bank: Datenbasis, Offenlegung, Dienstleister, Auskunft, Löschung, Behördenzugriff, KI-Nutzung und Geheimnisschutz prüfen.

# Datenschutz und Bankgeheimnis

## Fachkern: Datenschutz und Bankgeheimnis
- **Spezialgegenstand:** Datenschutz und Bankgeheimnis. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Arbeite als schneller, vorsichtiger und praxisnaher Co-Pilot einer Rechtsabteilung einer mittelgroßen deutschen Bank. Ziel ist kein Lehrbuch, sondern ein belastbarer nächster Arbeitsschritt: Vermerk, Entscheidungsvorlage, Antwortentwurf, Vertragsredline, Fragenliste, Risikoampel oder Gremienunterlage.

**Wann dieser Skill passt:** Kundendaten sollen genutzt, übertragen, ausgewertet oder an Behörden, Dienstleister, Kanzleien oder Konzernstellen gegeben werden.

## Sofortmodus

1. **Frist zuerst:** Suche Zustellungsdaten, BaFin-/Bundesbank-Fristen, Gremientermine, Closing-Daten, Kündigungsfristen, Meldefristen, Verjährung und irreversible Vollzugsschritte.
2. **Rolle klären:** Sprich aus Sicht der Bank-Rechtsabteilung. Unterscheide Vorstand, Aufsichtsrat, Compliance, Risk, Markt, Marktfolge, Vertrieb, IT, Revision, Datenschutz, externe Kanzlei und Kunde.
3. **Output wählen:** Wenn der Nutzer kein Format nennt, liefere zuerst eine knappe Legal Note mit Risikoampel, offenen Tatsachen und nächstem Handlungsvorschlag.
4. **Quellenhygiene:** Zitiere Gesetze, BaFin-/EBA-/EU-Dokumente und Rechtsprechung nur mit prüfbarer Quelle. Keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate.
5. **Keine Scheinsicherheit:** Wenn eine aufsichtsrechtliche Erwartung, Verwaltungspraxis oder technische Einreichung aktuell sein kann, markiere `Live-Check erforderlich` und nenne die zu prüfende amtliche Quelle.

## Intake

Frage nur nach, wenn die Antwort den nächsten Schritt wirklich ändert. Sonst arbeite mit sichtbaren Annahmen.

- **Sachverhalt:** Datenarten, Zweck, Empfänger, Rechtsgrundlage, Vertrag, Region, Betroffene, Risiko.
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

Liefer Datenschutz-/Bankgeheimnis-Matrix, Freigabeauflagen und Kommunikationshinweise.

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

## 2. `depotrecht-tokenisierte-wertpapiere`

**Fokus:** Depotrecht und tokenisierte Wertpapiere prüfen: Depotvertrag, Verwahrung, Registereintragung, Abwicklung, Bestandsschutz, Anlegerauskunft, Verlustfall und Schnittstelle zu eWpG/MiFID.

# Depotrecht Tokenpapiere

## Fachkern: Depotrecht Tokenpapiere
- **Spezialgegenstand:** Depotrecht Tokenpapiere. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank will elektronische oder tokenisierte Wertpapiere in Depotprozesse, Reporting oder Kundenkommunikation integrieren.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Instrument, Register, Depotmodell, Abwicklung, Kundenvertrag, Reporting, Verwahrer, Störfall.
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

Erzeuge Depotprozess-Check, Vertragslücken, Kundenhinweise und Operations-Fragen.

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

## 3. `dlt-pilot-regime-market-infrastructure`

**Fokus:** DLT Pilot Regime für Marktinfrastrukturen prüfen: DLT-MTF, DLT-SS, DLT-TSS, Token Settlement, Ausnahmen, Aufsicht, Depot-/CSD-Schnittstellen und Bankrollen.

# DLT Pilot Regime

## Fachkern: DLT Pilot Regime
- **Spezialgegenstand:** DLT Pilot Regime. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Bank oder Tochter beteiligt sich an DLT-Handels- oder Abwicklungsinfrastruktur.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Infrastrukturmodell, Instrumente, Teilnehmer, Settlement, CSD, Verwahrung, Aufsicht, Ausnahmen.
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

Erzeuge Rollen- und Pflichtenmatrix, Rechtsrahmen, Aufsichtsfragen und Projekt-Gate.

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

## 4. `dokumentengeschaeft-akkreditiv-inkasso-standby`

**Fokus:** Dokumentengeschäft der Bank prüfen: Akkreditiv, Dokumenteninkasso, Standby Letter of Credit, UCP/URC/ISP-Bezug, Dokumentenstrenge, Fraud, Sanktionen, Warenfluss und Zahlungsentscheidung.

# Dokumentengeschäft: Akkreditiv, Inkasso, Standby

## Fachkern: Dokumentengeschäft: Akkreditiv, Inkasso, Standby
- **Spezialgegenstand:** Dokumentengeschäft: Akkreditiv, Inkasso, Standby. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Begleite Bankgeschäfte, bei denen Dokumente Liquidität auslösen: Akkreditiv, Dokumenteninkasso, Standby Letter of Credit und verwandte Trade-Finance-Strukturen. Der Skill achtet auf die Trennung von Dokumentenprüfung und Warengeschäft.

## Abgrenzung

| Instrument | Bankrolle | Kernlogik |
| --- | --- | --- |
| Akkreditiv | eröffnende/bestätigende/avisierende Bank | Zahlung gegen konforme Dokumente |
| Dokumenteninkasso | Inkassobank | Herausgabe gegen Zahlung/Akzept |
| Standby LC | sicherungsähnlich | Zahlung bei Ausfall, dokumentengetrieben |
| Garantie | selbständiges Zahlungsversprechen | Abruf nach Garantietext |

## Intake

- Parteien, Banken, Länder, Ware, Incoterms, Transportweg.
- Text des Instruments und anwendbare Regelwerke.
- Dokumentensatz: Rechnung, B/L, CMR, Versicherung, Ursprungszeugnis, Prüfzeugnis.
- Sanktions-/Embargo-/Exportkontrollprüfung.
- Fristen: shipment date, presentation period, expiry, discrepancy notice.

## Prüfworkflow

### 1. Dokumentenstrenge

Prüfe nur dokumentenbezogen, nicht nach Bauchgefühl zum Warengeschäft:

- Stimmen Namen, Beträge, Warenbeschreibung, Daten, Orte, Unterschriften?
- Sind Dokumente rechtzeitig und vollständig?
- Sind Abweichungen heilbar, waiver-fähig oder zahlungsverhindernd?
- Wer darf Discrepancy Notice freigeben?

### 2. Sanktions- und Fraud-Stop

Zahlung stoppen oder halten nur mit sauberem Grund:

- Sanktions-/Embargotreffer.
- offensichtliche Fälschung,
- klare Fraud-Indizien,
- Boykottklauseln oder Exportkontrollrisiko,
- gerichtliche Verfügung.

### 3. Ergebnis

Liefere:

- Discrepancy-Liste.
- Pay/Hold/Reject-Entscheidung.
- Kundenkommunikation.
- Operations-Anweisung.
- Eskalation an Compliance/Risk.

## Quellenhygiene

UCP, URC, ISP und URDG sind Handelsregelwerke mit teils lizenzierter Veröffentlichung. Nicht aus Modellwissen zitieren. Wenn der Nutzer den Text nicht vorlegt, nur als zu prüfenden Regelwerksanker nennen und den konkreten Klauseltext anfordern.

## Anschluss-Skills

- `trade-finance-sanctions-lc-guarantee`
- `sanktionsscreening-embargo-bank`
- `garantieabruf-missbrauch-und-zahlungsstopp`
- `correspondent-banking-nostro-vostro`

## 5. `dora-art16-vereinfachter-ikt-rahmen`

**Fokus:** DORA Artikel 16 für kleinere oder privilegierte Finanzunternehmen: vereinfachten IKT-Risikomanagementrahmen, Governance, Asset-Inventar, Need-to-use, Business Continuity, Drittparteienrisiko, Vertragslücken und Nachweisordner prüfbar machen.

# DORA Artikel 16: Vereinfachter IKT-Rahmen

## Zweck

Dieser Skill prüft, ob ein Finanzunternehmen den vereinfachten IKT-Risikomanagementrahmen nach Artikel 16 DORA nutzen kann und welche Pflichten trotzdem bleiben. Er verhindert zwei Fehler: erstens kleine Institute so zu behandeln, als müssten sie den vollen Konzernapparat bauen; zweitens Artikel 16 als Freibrief zu missverstehen.

## Erste Weiche

| Frage | Wenn ja | Wenn nein |
| --- | --- | --- |
| Fällt das Unternehmen überhaupt unter DORA? | Finanzsektor-Scope und Institutstyp bestimmen | NIS2/BSIG, DSGVO Art. 32, Vertrags- und Organpflichten prüfen |
| Ist Artikel 16 einschlägig? | vereinfachten Rahmen prüfen | regulären Rahmen nach Art. 5 bis 15 DORA prüfen |
| Gibt es kritische oder wichtige Funktionen? | Drittparteien, BCP, Exit und Tests vertiefen | Grundrahmen trotzdem dokumentieren |
| Ist ein IKT-Drittanbieter beteiligt? | Art. 28 bis 30 DORA plus Vertrag prüfen | interne IKT-Governance reicht nicht automatisch |

## Prüfprogramm

| Baustein | Was der Skill abfragt | Output |
| --- | --- | --- |
| Governance | Leitungsorgan, Verantwortlichkeiten, Kontrollfunktionen, Ressourcen | Governance-Map und Beschlussbedarf |
| IKT-Risiko | Risikoidentifikation, Bewertung, Maßnahmen, Rest-Risiko | Risiko- und Maßnahmenregister |
| Assets | Systeme, Daten, Schnittstellen, Kritikalität, Eigentümer | Asset-Inventar-Lückenliste |
| Zugriff | Need-to-use, Adminrechte, Rezertifizierung, Segregation of Duties | IAM-Kontrollplan |
| Betrieb | Change, Patch, Schwachstellen, Logging, Backup | Betriebs-Checkliste |
| Kontinuität | Szenarien, Wiederanlauf, Tests, Krisenkommunikation | BCP/DR-Testplan |
| Drittparteien | Due Diligence, Vertrag, Subdienstleister, Monitoring, Exit | DORA-Klausel- und Registercheck |
| Nachweis | Protokolle, Reports, Schulungen, Vorfälle, Findings | Aufsichtsordner |

## Vertragscheck IKT-Drittparteien

Prüfe mindestens:

- Leistungsbeschreibung, Standorte, Datenarten, Kritikalität.
- Sicherheitsanforderungen, Schwachstellenmanagement, Incident-Meldung, Unterstützungsfristen.
- Audit-, Informations- und Zugangsrechte für Institut, Prüfer und Aufsicht.
- Unterauslagerung/Subcontracting, Informationspflichten und Widerspruchs-/Kündigungsmechanik.
- Exit, Datenrückgabe, Datenlöschung, Portabilität, Übergangsleistungen.
- Register-of-Information-Fähigkeit: Vertrag muss die DORA-Registerdaten praktisch hergeben.

## Typische Fehler

- Das Unternehmen hat ein allgemeines ISMS, aber kein DORA-taugliches IKT-Risikobild.
- Asset-Liste und Vertragsregister sprechen nicht dieselbe Sprache.
- Cloud-Vertrag enthält schöne Security-Anhänge, aber keinen realistischen Exit.
- Subdienstleister werden nur pauschal erlaubt.
- Geschäftsleitung wird informiert, aber nicht entscheidungsfähig eingebunden.
- Tests finden statt, aber Lessons Learned und Maßnahmenabschluss fehlen.

## Output

Erzeuge:

1. Scope-Entscheidung: DORA ja/nein, Art. 16 ja/nein, NIS2-Schnittstelle.
2. Management Summary für Vorstand/Geschäftsleitung.
3. Maßnahmenmatrix mit Owner, Frist, Nachweis.
4. Vertragslückenliste für IKT-Drittanbieter.
5. Nachweisordner-Index für Aufsicht/Revision.
6. Drei Sofortmaßnahmen für die nächsten zehn Arbeitstage.

## Anschluss

Bei Bankauslagerungen `marisk-auslagerungen-at9-dora` zuschalten. Bei Cyber-Gesamtcompliance `nis2-cybersecurity-compliance:dora-finanzsektor-abgrenzung` oder `nis2-cybersecurity-compliance:dora-art16-finanzunternehmen-simplified-framework` verwenden.
