---
name: pe-esg-sfdr-lieferketten-gwg-kyc-ubo-teaser-nda-process-loi-nbo
description: "PE ESG Sfdr Lieferketten GWG KYC UBO Teaser NDA Process LOI NBO: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# PE ESG Sfdr Lieferketten GWG KYC UBO Teaser NDA Process LOI NBO

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **PE ESG Sfdr Lieferketten GWG KYC UBO Teaser NDA Process LOI NBO** im Plugin Private-Equity-Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pe-018-esg-sfdr-und-lieferketten` | Prüft ESG-Klassifizierung, SFDR-Kommunikation, CSRD-Daten, LkSG/CSDDD-Schnittstellen und Portfolio-Pflichten. |
| `pe-019-gwg-kyc-ubo-und-sanctions` | Prüft wirtschaftlich Berechtigte, Mittelherkunft, PEP, Sanktionen, Russland-/China-/Dual-Use-Risiken und Transaktionssperren. |
| `pe-021-teaser-nda-process-letter` | Prüft Verkäuferprozess von anonymisiertem Teaser bis Process Letter mit Fristen, Q&A, Datenraum und Vertraulichkeit. |
| `pe-022-loi-nbo-binding-offer` | Erstellt und prüft Non-Binding Offer, Letter of Intent und Binding Offer mit Bedingungen, Exklusivität und Break Fee. |

## Arbeitsweg

Im Plugin Private-Equity-Praxis gilt für **PE ESG Sfdr Lieferketten GWG KYC UBO Teaser NDA Process LOI NBO**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pe-018-esg-sfdr-und-lieferketten`

**Fokus:** Prüft ESG-Klassifizierung, SFDR-Kommunikation, CSRD-Daten, LkSG/CSDDD-Schnittstellen und Portfolio-Pflichten.

# ESG, SFDR und Lieferketten im PE-Mandat

## Fachkern: ESG, SFDR und Lieferketten im PE-Mandat
- **Spezialgegenstand:** ESG, SFDR und Lieferketten im PE-Mandat wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Der Skill baut keine Marketingfolie, sondern eine beweisbare ESG-Arbeitsmatrix. Themen: SFDR-Klassifizierung (Art. 6/8/9), PAI-Statement (Principal Adverse Impacts), CSRD-Reporting der Portfoliogesellschaften, LkSG/CSDDD-Sorgfaltspflichten in Wertschöpfungskette, EU-Taxonomie, ESG-Reps im SPA.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche SFDR-Kategorie ist für den Fonds vorgesehen (Art. 6, 8, 9)?
2. Ist PAI-Statement bereits veröffentlicht und konsistent mit Pre-Contractual Disclosure?
3. Welche Asset-Klasse (Buyout, VC, Infra, Debt) — Reporting-Verpflichtungen unterschiedlich?
4. CSRD-Pflicht: welche Portfoliogesellschaften fallen ab welchem GJ unter CSRD (Schwellen 250+ MA, 50 Mio. EUR Umsatz, 25 Mio. EUR Bilanzsumme)?
5. LkSG-Anwendung auf Portfoliogesellschaften (>= 1.000 Beschäftigte seit 2024)?
6. CSDDD-Übergangsregime im DE-Umsetzungsgesetz beobachten?
7. EU-Taxonomie: Alignment-Quote des Fonds bzw. der Portfolios?
8. Greenwashing-Risiko in PPM/Marketing geprüft?

## Rechtlicher und transaktionaler Rahmen

SFDR (VO (EU) 2019/2088), insb. Art. 6 (alle Fonds), Art. 8 ("light green", ESG-Promotion), Art. 9 ("dark green", Sustainable Investment Objective); SFDR Delegated Regulation (EU) 2022/1288 (Templates, PAI); EU-Taxonomie-VO (EU) 2020/852; CSRD (RL (EU) 2022/2464) mit gestuftem Anwendungsbereich seit 2024; ESRS Reporting Standards; LkSG (Lieferkettensorgfaltspflichtengesetz, seit 01.01.2024 für Unternehmen ab 1.000 Beschäftigte); CSDDD (RL (EU) 2024/1760, Umsetzungsfrist 26.07.2027); UWG/Greenwashing (BGH-Rechtsprechung zu "klimaneutral", ständige Rechtsprechung mit konkreten Aktenzeichen vom Anwender zu verifizieren).

## / Schritt für Schritt

1. SFDR-Kategorie pro Fonds dokumentiert festlegen — basis für Pre-Contractual Disclosure, Website und PPM.
2. PAI-Statement: 14 obligatorische plus mindestens 2 optionale Indikatoren; Datenerhebung aus Portfoliogesellschaften.
3. ESG Side-Letter-Klauseln standardisieren (LP-Negativlisten, Excuse Rights, Reporting-Frequenz).
4. Portfolio-Level: CSRD-Pflicht je Asset bestimmen, Datenkollektoren beauftragen (Sustainalytics, MSCI, Reprisk, ISS-ESG).
5. LkSG-Risikoanalyse für Portfoliogesellschaften >= 1.000 MA: Risk Mapping, Präventionsmaßnahmen, Beschwerdeverfahren.
6. CSDDD-Vorbereitung: zusätzliche Schwellen ab 1.000 Beschäftigte und 450 Mio. EUR Umsatz (gestaffelt bis 2029).
7. Greenwashing-Prüfung: jede ESG-Aussage muss mit Daten unterlegbar sein; "klimaneutral" nur mit dokumentiertem Pfad.
8. Reporting: ILPA ESG Data Convergence Initiative (DCI) Format als Marktstandard.

## Trade-off-Matrix

| Art. 6 SFDR | Art. 8 SFDR ("light green") | Art. 9 SFDR ("dark green") |
| --- | --- | --- |
| Minimum-Disclosure; keine ESG-Promotion | ESG-Charakteristika in Anlagestrategie | Sustainable Investment Objective verbindlich |
| Niedriger Reporting-Aufwand | Mittlerer Aufwand | Hoher Aufwand, hohe Quote sustainable investments |
| Keine Marketing-Hebel | Marktstandard für PE | Selten bei Buyout, häufiger bei Impact |

## Praktikertipps Big-Law-PE

- ESMA Greenwashing Final Report (2024) und BaFin-Verlautbarungen ziehen die Disclosure-Anforderungen straffer; Art. 8/9-Reclassification durch ESMA findet aktiv statt.
- "Sustainable Investment" nach Art. 2(17) SFDR braucht Nachweis Contribution + Do No Significant Harm + Good Governance.
- PAI-Datenerhebung in Bestandsportfolios ist Hauptengpass; vor Acquisition ESG-DD systematisch nachziehen.
- LkSG-konforme Beschwerdesysteme im Portfolio fehlen häufig — Acquisition-Day-1-Checkliste ergänzen.
- "ESG Reps & Warranties" im SPA: typisch (i) Compliance with SFDR/Taxonomy/LkSG, (ii) keine Untersuchungen wegen ESG-Verstößen, (iii) Disclosure aller PAI-relevanten Daten.
- ESG-Klauseln im Management Equity Plan (MIP) als Bonus-Trigger werden zunehmend Standard bei Top-Fonds.
- BaFin-Sanktionen bei Greenwashing 2024/2025 — keine Übertreibung in Marketing-Materialien.

## Mustertexte / SPA-Klauseln

ESG Reps & Warranties (SPA Auszug):

> Die Gesellschaft und ihre Tochterunternehmen halten alle anwendbaren ESG-Vorschriften ein, insbesondere SFDR (sofern anwendbar), EU-Taxonomie, LkSG und einschlägige Sektorregulierung. Es bestehen keine offenen Behördenverfahren, Beschwerden oder Whistleblower-Meldungen mit ESG-Bezug; etwaige Vorfälle der letzten 36 Monate sind im Disclosure Schedule [Z] vollständig dokumentiert.

PAI Excuse Right (Side Letter):

> Limited Partner kann sich von Investments excusen, die gegen seine ESG-Negativliste (Schedule [X]: Tabak, kontroverse Waffen, Kohle, Adult Entertainment, Glücksspiel) verstoßen. KVG informiert vor Investment-Entscheidung; Excuse-Notice innerhalb 10 Bankarbeitstagen.

## Typische Fehler

- Art. 9 SFDR-Klassifizierung ohne dokumentierte Sustainable-Investment-Quote — Downgrade-Risiko durch BaFin.
- PAI-Daten in PPM behauptet, aber nicht beschaffbar — Greenwashing.
- LkSG-Risikoanalyse fehlt für Portfoliogesellschaften >= 1.000 MA.
- CSRD-Vorbereitung zu spät — Audit-Schock im ersten Reporting-Jahr.
- ESG-Side-Letter-Klauseln kollidieren mit Anlagebedingungen — Anlegerstreit.

## Querverweise

- pe-005 für Spezial-AIF-Anlagebedingungen.
- pe-006 für ELTIF und ESG.
- pe-010 für Marketing-Compliance.
- pe-011 für Side Letter.
- pe-023 für ESG-DD.

## Quellen Stand 06/2026

- SFDR (VO (EU) 2019/2088) und Delegated Regulation (EU) 2022/1288.
- EU-Taxonomie-VO (EU) 2020/852.
- CSRD (RL (EU) 2022/2464); ESRS Standards (Stand 2024).
- LkSG (BGBl. I 2021 Nr. 46) seit 01.01.2024 für Unternehmen ab 1.000 Beschäftigte.
- CSDDD (RL (EU) 2024/1760).
- ESMA Greenwashing Final Report (vom Anwender mit aktuellem Stand zu prüfen).
- ILPA ESG Data Convergence Initiative (Stand vom Anwender zu prüfen).

## 2. `pe-019-gwg-kyc-ubo-und-sanctions`

**Fokus:** Prüft wirtschaftlich Berechtigte, Mittelherkunft, PEP, Sanktionen, Russland-/China-/Dual-Use-Risiken und Transaktionssperren.

# GwG, KYC, UBO und Sanktionen

## Fachkern: GwG, KYC, UBO und Sanktionen
- **Spezialgegenstand:** GwG, KYC, UBO und Sanktionen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Pflicht vor Mandatsannahme, Zeichnung, Closing, Portfolio-Add-on und NPL-Kauf. Der Skill liefert die KYC-Matrix: wirtschaftlich Berechtigte (UBO), Eigentumskette, Quellen-Nachweise (Source of Wealth / Source of Funds), PEP-Status, Sanktions-Screening (EU 833/2014 Russland, EU 269/2014, US OFAC), Dual-Use-Güter (EG 2021/821), Transaktionssperren.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Phase (Mandatsannahme, Subscription, Closing, Portfolio-Add-on, Distressed Acquisition)?
2. Identität der Vertragspartner und vollständige Eigentumskette?
3. UBO-Identifikation: > 25 Prozent direkt/indirekt halten oder Kontrolle anderweitig?
4. PEP-Status (politisch exponiert) und Naher-Verwandter-Status?
5. Quelle des Vermögens und Source of Funds dokumentiert?
6. Russland-/Belarus-/Iran-Bezug auf irgendeiner Ebene der Eigentumskette?
7. Dual-Use-Risiko (Halbleiter, AI, Quantum, Biotech)?
8. Branchenrisiko (Glücksspiel, Krypto, Edelmetalle, Antiquitäten, Real Estate Schwellenländer)?

## Rechtlicher und transaktionaler Rahmen

GwG (Geldwäschegesetz, neueste Fassung), insb. §§ 10–15 (Sorgfaltspflichten), § 11 (Identifizierung), §§ 18–24 (UBO und Transparenzregister), § 43 (Verdachtsmeldung); Transparenzregister-Pflicht für alle deutschen Gesellschaften (TPLG); EU-Geldwäscheregeln: AMLD VI (RL (EU) 2024/1640), AMLR (VO (EU) 2024/1624 anwendbar ab Juli 2027, mit Übergangsregelungen); AWG/AWV; EU-Russland-Sanktionen (VO (EU) 833/2014 mit zahlreichen Amendments, vom Anwender mit aktuellem Stand zu prüfen); EU-Iran (VO 267/2012), EU-Belarus (VO 765/2006); US OFAC SDN List; UK Sanctions OFSI; Dual-Use-VO (EU) 2021/821; HRR § 6 Abs. 1 GmbHG für Konzernlisten.

## / Schritt für Schritt

1. Customer Due Diligence Level bestimmen: Standard, Simplified (§ 14 GwG) oder Enhanced (§ 15 GwG bei PEP, High Risk Country, komplexe Strukturen).
2. UBO-Kette aufrollen: Direkter/indirekter Halt > 25 Prozent oder Kontrolle? Stiftungen, Trusts, Holding-Strukturen detailliert.
3. Identifikation gem. § 11 GwG: Ausweisdokument bzw. Handelsregisterauszug, qualifizierter Vertrauensdiensteanbieter.
4. Sanktions-Screening über alle Beteiligten (Vertragspartner, UBO, Geschäftsleitung, Beneficiaries) gegen EU/US/UK Lists.
5. Mittelherkunft: Bankauszüge, Verkaufsverträge, Erbschein, Lohnabrechnungen, Audit Reports — abhängig vom Ticket.
6. PEP-Listen-Screening (World-Check, LexisNexis, Dow Jones); enhanced DD bei Hit.
7. Transparenzregister-Eintragung prüfen (für alle DE-Gesellschaften zwingend seit GwG-Reform 2021); Diskrepanzmeldung nach § 23a GwG.
8. Verdachtsmeldung an FIU (§ 43 GwG) bei Indikatoren; Verfahrensvermerk auch bei "nicht verdächtig" dokumentieren.

## Trade-off-Matrix

| Standard CDD | Simplified CDD | Enhanced CDD |
| --- | --- | --- |
| Regelfall | Geringes Risiko (z. B. EU-börsennotierter LP) | PEP, Hochrisikoland, komplexe Struktur |
| Identifizierung + UBO | Reduziert dokumentiert | Plus Mittelherkunft, periodische Überprüfung |
| Update alle 24 Monate | Update bei Anlass | Update jährlich |

| Asset-Frost (Verkauf gestoppt) | Distressed Wind-Down | Notlizenz beantragt |
| --- | --- | --- |
| EU 833/2014 Art. 5b | Genehmigung BAFA | Einzelfall |
| Klassischer Russland-Halt | Wind-Down innerhalb von 6 Monaten | Aufwendiger Prozess |

## Praktikertipps Big-Law-PE

- AMLR (EU-Geldwäschepaket 2024) bringt zentrale Anti-Money-Laundering Authority (AMLA) — bis Anwendung 2027 schon Vorbereitungen einplanen.
- Transparenzregister-Diskrepanzmeldung (§ 23a GwG) ist Pflicht bei Abweichung; viele Sponsoren übersehen das beim Sub-Doc-Eingang.
- PEP-Status auch bei deutschen Politikern und deren Familie zu prüfen; "near-PEP" für Sportler-, Medien-, Hochfinanz-Prominenz.
- Russland-Sanktionen: Beneficial Ownership unter 50 Prozent kann ausreichen, wenn Kontrolle vorliegt — Substance-over-Form-Doktrin der EU-Kommission.
- "No-Russia"-Klausel im SPA: standardisierter Marktstandard für Cross-Border-Deals seit 2022.
- Dual-Use: bei Halbleitern, KI, Quantum-Technologie zusätzliche AWG-Meldung; mehrstufige Genehmigungspfade.
- Whistleblower-System (HinSchG) integriert mit GwG-Meldungen — interne Compliance-Architektur.

## Mustertexte / SPA-Klauseln

No-Russia / No-Sanctions Reps (SPA EN/DE):

> The Seller and the Target Group are in compliance with all applicable sanctions, including EU, UK and US sanctions. Neither the Seller nor the Target nor any of their direct or indirect beneficial owners is a Sanctioned Person. No Target funds derive from or are destined for any Sanctioned Person or Sanctioned Country.

> Der Verkäufer und die Zielgesellschaftsgruppe halten alle anwendbaren Sanktionen ein, insbesondere EU-, UK- und US-Sanktionen. Weder der Verkäufer noch die Zielgesellschaft noch deren direkte oder indirekte wirtschaftlich Berechtigte sind sanktionierte Personen.

UBO-Erklärung (KYC Form):

> Hiermit erkläre ich, dass die in beiliegender Eigentumskette ausgewiesenen wirtschaftlich Berechtigten (i) alle Personen umfassen, die mittelbar oder unmittelbar > 25 Prozent der Stimmrechte/Kapitalanteile halten, (ii) alle Personen umfassen, die anderweitige Kontrolle ausüben, und (iii) keine sanktionierten oder PEP-relevanten Personen verschweigen.

## Typische Fehler

- UBO-Kette nur bis erste Holding aufgerollt; LUX-/Cayman-Strukturen dahinter unaufgeklärt.
- Transparenzregister-Eintragung nicht aktualisiert nach Anteilstransfer.
- Russland-Indirektbeziehung übersehen (z. B. ehemaliger russischer UBO mit jetziger EU-Staatsbürgerschaft).
- Mittelherkunft formularhaft akzeptiert ohne plausible Dokumentation.

## Querverweise

- pe-001 für Mandatsannahme.
- pe-003 für Investorprofil.
- pe-011 für Subscription / KYC im Sub-Doc.
- pe-012 für KYC bei Secondary-Buyer-Onboarding.
- pe-023 für DD inkl. Sanktionsprüfung Target.

## Quellen Stand 06/2026

- GwG (aktuelle Fassung), insb. §§ 10–15, 18–24, 43.
- AMLR (VO (EU) 2024/1624) und AMLD VI (RL (EU) 2024/1640).
- EU-Russland-Sanktionen (VO (EU) 833/2014 mit Amendments); EU-Belarus (VO (EU) 765/2006); EU-Iran (VO (EU) 267/2012).
- US OFAC SDN List; UK Sanctions OFSI.
- Dual-Use-VO (EU) 2021/821.
- AWG/AWV (deutsche Außenwirtschaftsregeln); HinSchG (Hinweisgeberschutzgesetz).
- BaFin/FIU-Hinweise zur Auslegung des GwG (vom Anwender mit aktuellem Stand zu prüfen).

## 3. `pe-021-teaser-nda-process-letter`

**Fokus:** Prüft Verkäuferprozess von anonymisiertem Teaser bis Process Letter mit Fristen, Q&A, Datenraum und Vertraulichkeit.

# Teaser, NDA und Process Letter

## Fachkern: Teaser, NDA und Process Letter
- **Spezialgegenstand:** Teaser, NDA und Process Letter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Fokus auf PE-Bieterprozesse, taktische Informationsdosierung und Haftungsbegrenzung.

## Rechts- und Praxisanker

BGB culpa in contrahendo, GeschGehG, DSGVO, Kartellrecht Clean Team.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 4. `pe-022-loi-nbo-binding-offer`

**Fokus:** Erstellt und prüft Non-Binding Offer, Letter of Intent und Binding Offer mit Bedingungen, Exklusivität und Break Fee.

# LOI, NBO und Binding Offer

## Fachkern: LOI, NBO und Binding Offer
- **Spezialgegenstand:** LOI, NBO und Binding Offer wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GmbHG, AktG, UmwG, GWB/FKVO, AWG/AWV, KAGB/AIFM-Bezug, LMA-Finanzierung, InsO/StaRUG, Steuer- und Managementbeteiligungsfragen.
- **Entscheidende Weiche:** Bestimme Dealphase, Fondsrolle, Target-Risiko, Finanzierungsstruktur, Consent/CP, Exit-Auswirkung und Konflikt zwischen Sponsor, Management, Lender und Co-Investor.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Der Skill markiert, was schon verbindlich ist und was nur Deal-Logik bleibt.

## Rechts- und Praxisanker

BGB, Kartell-/FDI-Vollzugsverbote, Break Fee, Exklusivität, Vertraulichkeit.

## Workflow

1. Rolle, Parteiperspektive, Deal-Phase und Zeitdruck klären.
2. Vorliegende Unterlagen benennen und fehlende Dokumente als konkrete Nachforderungsliste erfassen.
3. Rechtsrahmen, wirtschaftlichen Hebel und Entscheidungspunkt trennen.
4. Risikopunkte nach Deal Value, Closing-Fähigkeit, Haftung und Verhandlungshebel priorisieren.
5. Verwertbaren Output erzeugen und offene Annahmen sichtbar markieren.

## Output

- Kurz-Memo mit Ergebnis, Annahmen und nächstem Schritt.
- Issues List oder Checkliste mit Owner, Frist, Beleg und Risikoampel.
- Bei Entwurfsaufgaben: erster Draft mit Platzhaltern für fehlende Informationen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.
