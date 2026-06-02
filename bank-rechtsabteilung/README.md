# Bank-Rechtsabteilung



<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bank-rechtsabteilung`) | [`bank-rechtsabteilung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bank-rechtsabteilung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [`testakte-batteriespeicher-brandenburg-berlin-resilienz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akten demonstrieren dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Märkische Reserve Süd — Batteriespeicher Brandenburg/Berlin** (`batteriespeicher-brandenburg-berlin-resilienz`) | [Gesamt-PDF lesen](../testakten/batteriespeicher-brandenburg-berlin-resilienz/gesamt-pdf/batteriespeicher-brandenburg-berlin-resilienz_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-batteriespeicher-brandenburg-berlin-resilienz.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->
Rechtsabteilungs-Plugin für eine mittelgroße deutsche Bank: schnell genug für den internen Ticketkanal, sorgfältig genug für Vorstand, Aufsichtsrat, BaFin, Bundesbank, externe Kanzleien und späteren Aktenrückblick.

Es ist als Inhouse-Cockpit gedacht: nicht nur Bankrecht im engeren Sinn, sondern der ganze Alltag einer Bank-Rechtsabteilung. Aufsichtsrecht, Kredit, Sanierung, Auslagerung, DORA, Geldwäsche, AGB, Handelsvertreter, Vertrieb, Beschwerden, Organvorlagen, Hauptversammlung, Beteiligungen, Datenschutz, Kanzleisteuerung und Rechnungsreview werden in einen einzigen Routing-Workflow gebracht. Die Spezialerweiterung deckt zusätzlich ZAG-Finanztransfer, PSD2/Open Banking, PSD3/PSR-Vorschau, eWpG, Kryptowertpapierregister, MiCAR, Tokenisierung, Instant Payments und digitale Bankprodukte ab.

## Für wen

| Rolle | Typische Nutzung |
| --- | --- |
| General Counsel / Chefjustiziar | Vorstandsvorlagen, Aufsichtsrat, Eskalation, Kanzleisteuerung |
| Syndikus in Legal | Gutachten, Vertragscheck, Fachbereichsberatung, BaFin-Antworten |
| Compliance / AML / Datenschutz | GwG, Sanktionen, DORA, Richtlinien, Meldungen, Findings |
| Marktfolge / Risk / Workout | Weiterfinanzierung, Stundung, Sanierungsgutachten, Sicherheiten |
| Vorstandsreferat | Beschlussvorschläge, Q&A, HV- und Ausschussunterlagen |

## Kaltstart

Beginne mit:

```text
/bank-rechtsabteilung:allgemein
```

Der Einstieg fragt nicht erst einen langen Fragebogen ab, sondern sortiert sofort:

- Was liegt vor?
- Wer braucht das Ergebnis?
- Gibt es eine Frist oder Aufsichtsdruck?
- Ist es Kredit, Aufsicht, Vertrieb, Organ, Vertrag, Datenschutz, Litigation oder Dienstleistersteuerung?
- Welcher Spezial-Skill passt jetzt wirklich?

Wenn nur ein Dokument hochgeladen wird, behandelt der Allgemein-Skill das als Arbeitsauftrag: Fristen erkennen, Material klassifizieren, Risikoampel bauen, passenden Spezial-Skill vorschlagen oder direkt einen ersten verwertbaren Entwurf schreiben.

## Normen- und Quellenhygiene

Das Plugin ist bewusst quellenstrikt. Es soll keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate produzieren. Für tragende Aussagen sind Live-Checks gegen amtliche oder frei zugängliche Quellen vorgesehen, insbesondere:

- Gesetze im Internet: KWG, ZAG, WpHG, GwG, HGB, BGB, AktG.
- BaFin: MaRisk, DORA-Informationen, Merkblätter, Rundschreiben und Aufsichtsmitteilungen.
- Bundesbank, EZB/SSM, EBA und EUR-Lex für europäische Aufsichtsakte und Leitlinien.
- Gerichtsentscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.

Siehe auch [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Workflows

Die erste Ausbaustufe deckt den Alltag der Rechtsabteilung ab; die zweite Ausbaustufe geht tief in Zahlungsdienste, Geschäftsleiteranzeigen, elektronische Wertpapiere und Tokenisierung.


| Workflow | Start-Skill | Ergebnis |
| --- | --- | --- |
| BaFin-Schreiben liegt vor | `bafin-kommunikation-und-anhoerung` | Antwortarchitektur, Tatsachenmatrix, Freigabekette |
| Cloud-Vertrag soll freigegeben werden | `dora-ict-vertraege-vorfall` | DORA-/Auslagerungscheck, Klausellücken, Exit-Fragen |
| Kreditnehmer braucht Stundung | `stundung-standstill-waiver` | Term Sheet, Conditions, Sicherheiten- und Anfechtungsampel |
| Sanierungsgutachten kommt rein | `sanierungsgutachten-idw-s6-bewertung` | Plausibilitätsreview, Red Flags, Nachforderungsliste |
| Vorstand braucht Vorlage | `vorstandsvorlage-gutachten` | Executive Summary, Optionen, Beschlussvorschlag |
| Kanzleirechnung ist zu hoch | `anwaltliche-rechnungen-review` | Rechnungsprüfung, Rückfragen, Kürzungsvorschlag |
| Handelsvertreter kündigt | `handelsvertreter-vertriebsrecht-bank` | Statusanalyse, Ausgleichsrisiko, Verhandlungsposition |
| AGB sollen geändert werden | `agb-bankrecht-klauselkontrolle` | Klauselampel, bessere Fassung, Rollout-Hinweise |

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Bank-Rechtsabteilung (`bank-rechtsabteilung`) | [bank-rechtsabteilung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bank-rechtsabteilung.zip) |

Die URL zeigt immer auf das aktuelle Release-Asset.

## Installation in Claude Code / Cowork

1. ZIP aus dem Release herunterladen.
2. In Claude Code / Cowork unter **Customize Plugins** das ZIP installieren.
3. `bank-rechtsabteilung` aktivieren und mit `/bank-rechtsabteilung:allgemein` starten.

> Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus GitHub verwenden.

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 100 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agb-bankrecht-klauselkontrolle` | AGB-Recht für Banken: Klauseln nach §§ 305 bis 310 BGB, Preisänderungen, Zustimmungsmechanismen, Kündigung, Entgelte, Aufrechnung, Haftung und Verbrauchertransparenz prüfen. |
| `allgemein` | Einstieg und Chefjustiziar-Workflow für die Rechtsabteilung einer mittelgroßen deutschen Bank. Fragt Rolle, Ziel, Fristen, Dokumente, Aufsichtsrisiko, Kreditrisiko, Organbedarf und gewünschten Output ab und routet in passende Bank-Skills. |
| `anwaltliche-rechnungen-review` | Anwaltliche Rechnungen und Kanzlei-Budgets reviewen: Scope-Abgleich, RVG oder Honorarvereinbarung, Zeitpositionen, Auslagen, USt, Doppelarbeit, Erfolg, Billing Guidelines und Kürzungsvorschlag. |
| `app-fraud-social-engineering-bank` | APP-Fraud, PushTAN und Social Engineering aus Bankensicht prüfen: Kundenschutz, Warnpflichten, PSD2/BGB-Haftung, SCA, Empfängerbank, Freeze, Recall und Prozessstrategie. |
| `aufsichtsrat-vorlage-bank` | Aufsichtsrats- und Ausschussvorlagen einer Bank vorbereiten: Informationspflicht, Beschlusskompetenz, Risikoausschuss, Prüfungsausschuss, Vertraulichkeit, Protokollfestigkeit und Follow-up. |
| `bafin-kommunikation-und-anhoerung` | BaFin-Kommunikation und Anhörung: Antwortstrategie, Tonfall, Tatsachenklärung, Fristen, Vollständigkeit, Anerkenntnisrisiken, Aufsichtsdialog und Vorstandsinformation für Banken strukturieren. |
| `bafin-pruefung-vor-ort-management` | Vor-Ort-Prüfung, Sonderprüfung oder Aufsichtsprüfung in der Bank vorbereiten: Datenraum, Interviewliste, Kommunikationsregeln, Prüfungslog, Legal Privilege, Nachlieferungen und Abschlussbericht managen. |
| `bankaufsichtsrecht-kwg-marisk-triage` | Bankaufsichtsrechtliche Ersttriage nach KWG und MaRisk: Geschäftsorganisation, Risikomanagement, Compliance, Revision, Risikocontrolling, Leitungsbefassung und Dokumentationsbedarf für interne Vermerke prüfen. |
| `bankgeheimnis-auskunftsersuchen` | Auskunftsersuchen an Banken prüfen: Polizei, Staatsanwaltschaft, Gericht, Finanzamt, Insolvenzverwalter, Betreuer, Erben, Anwälte und Privatpersonen sicher auseinanderhalten. |
| `banking-as-a-service-white-label` | White-Label-Banking juristisch strukturieren: Bankrolle sichtbar machen, Partnerpflichten, Kundenschutz, AGB, Datenschutz, Auslagerung, Beschwerden, Vertriebsrecht und Reputationsrisiko. |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `beteiligungserwerb-bank-ma` | Beteiligungserwerb, M&A und strategische Kooperation einer Bank prüfen: Erlaubnisse, Inhaberkontrolle, Beteiligungsgrenzen, Due Diligence, Kartell, Datenschutz, Sanierung und Gremien. |
| `betriebsrat-change-projekte` | Betriebsrat und arbeitsrechtliche Schnittstellen bei Bankprojekten: Restrukturierung, IT-Einführung, Monitoring, variable Vergütung, Auslagerung, Filialschließung und Betriebsänderung prüfen. |
| `blockchain-settlement-dvp` | Blockchain-Settlement und Delivery-versus-Payment prüfen: Wertpapierseite, Geldseite, Finalität, CSD, Token Cash, Smart Contract, Fehlerkorrektur und Rechtswahl. |
| `chargeback-card-schemes-bankrecht` | Chargeback und Card-Scheme-Disputes rechtlich begleiten: Mastercard/Visa-Regeln, Zahlungsdienstehaftung, Händlerstreit, Fristen, Belege, Kundenerwartung und Kulanzgrenzen. |
| `correspondent-banking-nostro-vostro` | Korrespondenzbankbeziehungen und Nostro/Vostro-Risiken prüfen: AML, Sanktionen, Länder, Zahlungswege, Vertragsklauseln, Informationsrechte, Kündigung und Aufsichtserwartungen. |
| `covenant-waiver-credit-documentation` | Covenant Waiver und Kreditdokumentation tief prüfen: Financial Covenants, MAC, Events of Default, Informationspflichten, Cure Rights, Margin Step-up und Dokumentationsschutz. |
| `crr-crd-eigenmittel-large-exposure` | CRR-, CRD- und Großkredit-Schnittstelle für Juristen: Eigenmittelbegriffe, Large Exposure, Organkredite, Beteiligungen, Limitüberschreitungen und Governance-Freigaben verständlich prüfen. |
| `crypto-tax-reporting-dac8-car` | Krypto-Steuerreporting, DAC8 und CARF als Bank-Monitoring prüfen: Datenfelder, Meldepflichtige, CASP-Schnittstelle, Kundenkommunikation, Datenschutz und Roadmap. |
| `darlehensrecht-verbraucher-unternehmer` | Darlehensrecht für Banken: Verbraucher- und Unternehmenskredit, Pflichtangaben, Widerruf, Kündigung, Sicherheiten, Zahlungsverzug, Vorfälligkeitsfragen und Prozessrisiko prüfen. |
| `datenraum-bank-transaktion` | Datenraum für Bank-Transaktionen oder Aufsichtsprüfungen strukturieren: Dokumentenindex, Berechtigungen, Schwärzungen, Bankgeheimnis, Datenschutz, Q&A und Audit Trail. |
| `datenschutz-bankgeheimnis` | Datenschutz, Bankgeheimnis und Mandatsgeheimnis in der Bank: Datenbasis, Offenlegung, Dienstleister, Auskunft, Löschung, Behördenzugriff, KI-Nutzung und Geheimnisschutz prüfen. |
| `depotrecht-tokenisierte-wertpapiere` | Depotrecht und tokenisierte Wertpapiere prüfen: Depotvertrag, Verwahrung, Registereintragung, Abwicklung, Bestandsschutz, Anlegerauskunft, Verlustfall und Schnittstelle zu eWpG/MiFID. |
| `dlt-pilot-regime-market-infrastructure` | DLT Pilot Regime für Marktinfrastrukturen prüfen: DLT-MTF, DLT-SS, DLT-TSS, Token Settlement, Ausnahmen, Aufsicht, Depot-/CSD-Schnittstellen und Bankrollen. |
| `dora-ict-vertraege-vorfall` | DORA-IKT-Verträge und IKT-Vorfälle: Pflichtklauseln, Register, Exit, Überwachungsrechte, Suboutsourcing, Incident-Klassifizierung, Meldewege und Managementbericht prüfen. |
| `einlagensicherung-kundenhinweise` | Einlagensicherung und Kundenhinweise: gesetzliche und institutsspezifische Sicherung, Informationsbogen, Produktabgrenzung, Markenauftritt, Filialhinweise und Beschwerdekommunikation prüfen. |
| `embedded-finance-kooperation` | Embedded-Finance-Kooperationen prüfen: Händler, Plattform, Bank, Zahlungsdienstleister, Kreditangebot, Vermittlung, Scoring, Datenschutz, Provision und Erlaubnisrisiken. |
| `esg-sustainable-finance` | ESG und Sustainable Finance in der Bank: Offenlegung, Taxonomie, Green Claims, Kreditpolitik, Anlageprodukte, Reputationsrisiko und Vorstandskommunikation prüfen. |
| `ewpg-emission-elektronische-wertpapiere` | Emission elektronischer Wertpapiere nach eWpG prüfen: Zentralregister, Kryptowertpapierregister, Emissionsbedingungen, Registerangaben, Prospekt, Depot, Vertrieb und Anlegerkommunikation. |
| `ewpg-kryptowertpapierregister-erlaubnis` | Kryptowertpapierregisterführung nach eWpG und KWG prüfen: Finanzdienstleistung, § 32 KWG-Erlaubnis, Registerfunktion, Betreiberrolle, Geschäftsleiter, IT, DORA und BaFin-Merkblatt. |
| `ewpg-registerwechsel-registerfehler` | Registerwechsel, Registerfehler und Anlegerrechte bei elektronischen Wertpapieren prüfen: Berichtigung, Übertragung, Funktionsstörung, Kündigungsrechte, Haftung und Kommunikationspflichten. |
| `externe-anwaelte-steuerung` | Externe Anwälte und Kanzleien steuern: Mandatsbrief, Scope, Budget, Reporting, Privilege, Interessenkonflikte, Rechtsmeinungen, Second Opinion und internes Wissen sichern. |
| `fit-proper-eignungsmatrix-deep-dive` | Fit-and-Proper-Eignungsmatrix für Geschäftsleiter, Aufsichtsräte und Schlüsselfunktionen vertiefen: fachliche Eignung, Zuverlässigkeit, Kollektiveignung, Diversität, Interessenkonflikte und Fortbildung. |
| `fit-proper-organe-mitarbeiter` | Fit-and-Proper für Geschäftsleiter, Aufsichtsrat und Schlüsselfunktionen: Sachkunde, Zuverlässigkeit, Zeitbudget, Interessenkonflikte, Anzeigen und Nachweise vorbereiten. |
| `forbearance-npe-risikoklassifizierung` | Forbearance, NPE und Risikoklassifizierung juristisch begleiten: Zugeständnisse, Ausfallnähe, Melde- und Dokumentationsfolgen, Kreditakte und Kommunikation mit Risk sauber halten. |
| `geldwaesche-krypto-wallet-screening` | Krypto-AML und Wallet-Screening für Banken prüfen: Wallet-Risiko, Chain Analytics, Mixer, Bridges, Darknet-Indizien, PEP/Sanktionen, Verdachtsmeldung und De-Risking. |
| `geschaeftsleiter-abberufung-krise` | Abberufung, Suspendierung oder Ressortentzug von Geschäftsleitern in Banken prüfen: KWG, Organrecht, Dienstvertrag, BaFin-Risiko, Aufsichtsratskompetenz, Ad-hoc-Krise und Kommunikationsplan. |
| `geschaeftsleiter-bestellung-kwg-zag` | Geschäftsleiterbestellung nach KWG, ZAG und KAGB tief prüfen: Absichtsanzeige, Vollzugsanzeige, Zuverlässigkeit, fachliche Eignung, Zeitbudget, Lebenslauf, Führungszeugnis, Eignungsmatrix und BaFin-Kommunikation. |
| `girokonto-firmenkunden-risk-exit` | Firmenkunden-Girokonto, Risk Exit und De-Risking prüfen: Kündigung, Sperre, AML, Sanktionen, Diskriminierungsrisiko, Zahlungsverkehrsabhängigkeit und saubere Kundenkommunikation. |
| `gwg-aml-kyc-verdachtsmeldung` | GwG-, AML- und KYC-Prüfung für Banken: Risikoanalyse, wirtschaftlich Berechtigte, PEP, Sanktionen, Transaktionsmonitoring, Verdachtsmeldung und Dokumentation ohne unnötige Selbstbelastung strukturieren. |
| `handelsvertreter-vertriebsrecht-bank` | Handelsvertreter- und Vertriebsrecht für Banken: § 84 HGB, Ausgleich § 89b HGB, Vermittlerstatus, Tippgeber, Ausschließlichkeit, Provision, Kündigung und Compliance prüfen. |
| `hauptversammlung-bank-aktg` | Hauptversammlung einer Bank rechtlich vorbereiten: Tagesordnung, Beschlussvorschläge, Vorstand/Aufsichtsrat, Vergütung, Kapitalmaßnahmen, Satzung, Gegenanträge und Stimmrechtsfragen. |
| `iban-name-check-verification-payee` | Verification of Payee und IBAN-Name-Check prüfen: Matching-Logik, Haftung, Warntexte, Firmenkunden, Sammelzahlungen, Datenschutz, Fraud-Reduktion und Prozessdokumentation. |
| `insolvenz-anfechtung-bank` | Insolvenzanfechtung gegen Banken vorbeugen und verteidigen: Sicherheitenbestellung, Rückführung, Kontokorrent, inkongruente Deckung, Kenntnis, Bargeschäft und Anfechtungsgegner-Argumente prüfen. |
| `instant-payments-sepa-vo` | Instant Payments und SEPA-Echtzeitüberweisungen prüfen: Verfügbarkeit, Gebühren, Sanktionsscreening, Verification of Payee, Betrugsprävention, Kundenkommunikation und technische Umsetzungsrisiken. |
| `interne-richtlinie-policy-drafting` | Interne Richtlinien und Policies für Banken entwerfen: Normenbasis, Zielgruppe, Rollen, Kontrollen, Eskalation, Dokumentation, Versionierung, Schulung und Vorstandsbeschluss. |
| `it-sicherheit-cloud-vertraege` | IT-Sicherheit und Cloud-Verträge einer Bank prüfen: DORA, NIS2-Schnittstelle, Datenschutz, Audit-Rechte, Exit, Verschlüsselung, Incident Response, Subdienstleister und Bankaufsicht. |
| `kontokuendigung-sperre-basiskonto` | Kontokündigung, Kontosperre und Basiskonto prüfen: Vertragsrecht, AGB, GwG, Sanktionen, Pfändung, Diskriminierungsrisiko, Sozialleistungen und Kundenkommunikation ausbalancieren. |
| `kreditentscheidung-weiterfinanzierung` | Kreditentscheidung und Weiterfinanzierung: neue Auszahlung, Prolongation, Covenant-Bruch, Sanierungsphase, Risikovotum, Organpflichten und Dokumentation der Bankentscheidung prüfen. |
| `kreditsicherheiten-bestellung-verwertung` | Kreditsicherheiten bestellen, prüfen und verwerten: Grundschuld, Bürgschaft, Garantie, Globalzession, Sicherungsübereignung, Pfandrechte, Rang, Freigabe und Verwertungsschritte. |
| `kreditwesengesetz-erlaubnis-inhaberkontrolle` | KWG-Erlaubnis, Erlaubniserweiterung, Inhaberkontrolle und qualifizierte Beteiligung prüfen: Geschäftsmodell, Schwellen, Anzeige, Fit-and-Proper und BaFin-Erwartungen strukturieren. |
| `kundenbeschwerde-ombudsmann-bafin` | Kundenbeschwerden, Ombudsmann, BaFin-Beschwerde und Eskalation: Sachverhalt, Anspruch, Kulanz, Reputationsrisiko, Fristen, Ton und interne Learnings für Banken steuern. |
| `litigation-schlichtung-prozess` | Litigation, Schlichtung und Prozessführung einer Bank: Anspruch, Beweise, Kosten, Vergleich, Musterverfahren, Ombudsmann, externe Kanzlei und Vorstandsinformation steuern. |
| `ma-risk-compliance-funktion` | MaRisk-Compliance-Funktion und zweite Verteidigungslinie prüfen: Aufgaben, Unabhängigkeit, Compliance-Plan, Monitoring, Findings, Berichtslinie und Verhältnis zu Recht, Risk und Revision. |
| `marisk-auslagerungen-at9-dora` | MaRisk-Auslagerung und DORA-Schnittstelle: AT 9, § 25b KWG, Auslagerungsregister, Risikoanalyse, wesentliche Auslagerung, IKT-Drittanbieter und Exit-Plan zusammen prüfen. |
| `micar-art-emt-bank-emission` | ART- und EMT-Emission nach MiCAR für Banken prüfen: Asset-Referenced Token, E-Geld-Token, Zulassung, Whitepaper, Reserve, Rücktausch, Governance und Zahlungsdienste-Schnittstelle. |
| `micar-casp-notifikation-bank-art60` | MiCAR-CASP-Notifikation für Banken nach Art. 60 prüfen: bestehende Erlaubnis, Kryptowerte-Dienstleistung, 40-Arbeitstage-Frist, Unterlagen, BaFin/Bundesbank-Kommunikation und DORA-Schnittstelle. |
| `micar-whitepaper-marketing-bank` | MiCAR-Whitepaper und Marketing für Kryptowerte prüfen: Pflichtinhalte, Notifizierung, Werbung, Risikoangaben, Website, Social Media, Vertriebspartner und Haftungsrisiken. |
| `mifid-wphg-anlageberatung` | WpHG- und MiFID-II-Pflichten bei Anlageberatung und Vertrieb: Geeignetheit, Angemessenheit, Zielmarkt, Kosteninformation, Zuwendungen, ESG-Präferenzen und Dokumentation prüfen. |
| `notfallplan-krisenkommunikation` | Notfallplan und Krisenkommunikation für Bank-Legal: Cyberangriff, Bank Run, BaFin-Maßnahme, Medienanfrage, Whistleblowing, Großschaden oder Vorstandskrise strukturieren. |
| `operational-resilience-concentration-risk` | Operational Resilience und Konzentrationsrisiken bei Bankdienstleistern prüfen: kritische Funktionen, Auslagerungscluster, Cloud-Konzentration, DORA, Exit, Stresstest und Vorstandsvorlage. |
| `organhaftung-business-judgment` | Organhaftung und Business Judgment Rule in der Bank: Vorstand, Aufsichtsrat, Ausschüsse, Informationsgrundlage, Interessenkonflikte, Dokumentation und D&O-Risiken prüfen. |
| `organwechsel-ssm-imas-mvp` | Organwechsel bei SI, LSI und Zahlungsinstituten über SSM-IMAS, MVP oder Formulare steuern: Zuständigkeit, Einreichkanal, Fristen, Unterlagen, Nachfragen und Vorstandsbüro-Briefing. |
| `outsourcing-crypto-dlt-node-provider` | Crypto-/DLT-Dienstleister und Node Provider auslagern: DORA, MaRisk, § 25b KWG, Verwahrung, Daten, Schlüssel, Subdienstleister, Audit-Rechte und Exit in Krypto-Projekten prüfen. |
| `outsourcing-externe-dienstleister` | Externe Dienstleister außerhalb reiner IKT prüfen: Auslagerung, sonstiger Fremdbezug, Datenschutz, Bankgeheimnis, SLA, Prüfungsrechte, Kündigung, Business Continuity und Registerpflege. |
| `outsourcing-fintech-bank-as-a-service` | FinTech-Outsourcing und Bank-as-a-Service prüfen: Rollen, KWG/ZAG, White Label, Auslagerung, Vertrieb, AML, Kundenkommunikation, Haftung und Exit. |
| `pfandbriefbank-spezialdeckung` | Pfandbrief- und Spezialdeckungsfragen aus Bank-Legal-Sicht prüfen: Deckungsmasse, Treuhänder, Indeckungnahme, Immobilienfinanzierung, Register, Aufsicht und Vorstandsfreigabe. |
| `produktfreigabe-new-product-process` | New Product Process einer Bank: Produktidee, Zielmarkt, Recht, Aufsicht, Steuern, IT, Datenschutz, Vertrieb, Risiko, Operations und Vorstandfreigabe in einen sauberen NPP bringen. |
| `provisionsmodelle-vertrieb-compliance` | Provisionsmodelle und Vertriebscompliance prüfen: Zuwendungen, Interessenkonflikte, MiFID, Verbraucherschutz, Vergütungsrichtlinien, Zielvorgaben und Vorstandsvorlage für Produktvertrieb. |
| `psd2-fraud-refund-unauthorised-payment` | Unautorisierte Zahlung und Refund nach PSD2/BGB prüfen: § 675u BGB, § 675v BGB, grobe Fahrlässigkeit, Social Engineering, Beweislast, SCA-Logs und Vergleichsstrategie. |
| `psd2-open-banking-api-xs2a` | Open-Banking- und XS2A-Schnittstellen prüfen: Zugang zu Zahlungskonten, API-Verfügbarkeit, Fallback, TPP-Kommunikation, Consent, Sicherheit, Haftung und Aufsichtsbeschwerde. |
| `psd2-sca-strong-customer-authentication` | Starke Kundenauthentifizierung nach PSD2 prüfen: Zwei-Faktor-Logik, Ausnahmen, Transaktionsrisikoanalyse, App-Freigabe, Delegation, Betrugsfall und Kundenkommunikation. |
| `psd3-psr-vorschau-gap-analysis` | PSD3- und PSR-Vorschau für Banken: geplantes EU-Zahlungsdienste-Paket gegen bestehende PSD2/ZAG-Prozesse mappen, Fraud, Open Banking, Transparenz und organisatorische Gaps vorbereiten. |
| `rechtsmonitoring-bank` | Rechtsmonitoring für Banken einrichten: BaFin, Bundesbank, EBA, EZB, EU, Bundesgesetzblatt, Rechtsprechung, Verbände, Relevanzfilter und Umsetzungslog dokumentieren. |
| `restrukturierung-kreditengagement` | Restrukturierung eines Kreditengagements steuern: Strategie, Sicherheiten, Pool, StaRUG-/InsO-Schnittstelle, Sanierungsbeiträge, Kommunikation und interne Kreditakte ordnen. |
| `sanierungsgutachten-idw-s6-bewertung` | Eingehende Sanierungsgutachten nach IDW S 6 aus Bankperspektive bewerten: Krisenstadien, Fortbestehen, Leitbild, Maßnahmen, integrierte Planung, Plausibilität und Kreditentscheidung. |
| `sanktionsscreening-embargo-bank` | Sanktionsscreening und Embargo in der Bank: Treffer, False Positive, EU-Sanktionen, OFAC-Berührung, Zahlungsstopp, Kontosperre, Freigabeprozess und Kundenkommunikation steuern. |
| `schluesselfunktionen-inhaber-fit-proper` | Inhaber besonderer Schlüsselfunktionen in großen Banken prüfen: Anzeige, Eignung, Zuverlässigkeit, Zeitverfügbarkeit, Rollenabgrenzung und Eskalation an Aufsicht oder Vorstand. |
| `sepa-direct-debit-return-disputes` | SEPA-Lastschrift-Rückgaben und Mandatsstreit prüfen: Core/B2B, Mandat, Rückgabefristen, Erstattungsanspruch, Firmenkundenrisiko, Händlerkommunikation und Prozessbelege. |
| `ssm-bundesbank-aufsichtsbrief` | SSM-, EZB- und Bundesbank-Aufsichtsbriefe für Institute einordnen: Zuständigkeit, JST-Kommunikation, nationale Umsetzung, Fristen, Management Letter, Follow-up und Board-Package vorbereiten. |
| `stablecoin-payment-usecase-bank` | Stablecoin-Zahlungsusecase für Banken prüfen: EMT/ART, E-Geld, Zahlungsdienst, Wallet, Händlerakzeptanz, Reserve, Rücktausch, Sanktionsscreening und Settlement. |
| `staking-lending-token-bank` | Staking, Lending und Yield-Produkte mit Tokenbezug prüfen: Produktqualifikation, MiCAR, KWG/WpIG, AGB, Verbraucherhinweise, Verwahrung, Insolvenztrennung und Reputationsrisiko. |
| `stundung-standstill-waiver` | Stundung, Standstill, Waiver und Covenant-Reset entwerfen und prüfen: Bankinteressen, Sicherheiten, Sanierungspfad, Gleichbehandlung, Kündigungsrechte und Dokumentationsschutz. |
| `sustainability-linked-loan-greenwashing` | Sustainability-Linked Loans und Greenwashing-Risiken prüfen: KPI, SPT, Margin Ratchet, externe Verifikation, Offenlegung, Kreditdokumentation und Reputationsschutz. |
| `syndizierte-kredite-agent-security-trustee` | Syndizierte Kredite, Facility Agent und Security Trustee prüfen: Rollen, Mehrheitsentscheidungen, Sicherheitenpool, Parallel Debt, deutsches Recht, Enforcement und Sanierungsfall. |
| `tokenisierung-security-token-mica-mifid` | Tokenisierung und Security Token einordnen: MiFID-Finanzinstrument, eWpG-Kryptowertpapier, MiCAR-Kryptowert, Vermögensanlage, Prospektpflicht und Vertriebsregime trennscharf prüfen. |
| `trade-finance-sanctions-lc-guarantee` | Trade Finance, Letter of Credit und Garantien prüfen: Sanktionen, Exportkontrolle, UCP/URDG, Dokumentenstrenge, Betrugsverdacht, Boykottklauseln und Zahlungsstopp. |
| `travel-rule-krypto-transfers` | Travel Rule für Krypto-Transfers prüfen: Auftraggeber-/Begünstigtendaten, CASP-Pflichten, Wallets, unhosted Wallets, Screening, Ablehnung, Monitoring und Kundenkommunikation. |
| `verwahrung-kryptowerte-bank-custody` | Kryptowerte-Verwahrung und Custody durch Banken prüfen: MiCAR-CASP, alte KWG-Erlaubnisse, Wallet-Control, Schlüsselmanagement, Outsourcing, Haftung, DORA und Kundentrennung. |
| `vorstandsvorlage-gutachten` | Vorstandsvorlage und juristisches Gutachten für eine Bank erstellen: Entscheidungssatz, Risikoampel, Handlungsoptionen, Beschlussvorschlag, Annahmen, Quellen und Anlagenverzeichnis. |
| `wpig-wertpapierinstitut-schnittstelle` | WpIG-Schnittstellen prüfen, wenn Bankgruppe, Wertpapierinstitut, Vermittler oder Tochtergesellschaft beteiligt sind: Rollen, Erlaubnis, Eigenmittel, Auslagerung und Governance abgrenzen. |
| `zag-agenten-auslagerung-register` | ZAG-Agenten, E-Geld-Agenten und Auslagerung prüfen: Register, Haftung, Weisungen, Schulungen, AML, Kundenkommunikation, Passporting und Abgrenzung zum bloßen Dienstleister. |
| `zag-ausnahmen-limited-network-commercial-agent` | ZAG-Ausnahmen tief prüfen: begrenztes Netz, begrenzte Produktpalette, Handelsvertreterausnahme, technische Dienstleister, Konzernprivileg und digitale Plattformrisiken. |
| `zag-e-geld-institut-emoney` | E-Geld-Institut und E-Geld-Geschäft nach ZAG prüfen: Ausgabe, Rücktausch, monetärer Wert, Akzeptanzstellen, Sicherungsmittel, Eigenmittel, Vertrieb und Abgrenzung zu Gutschein, Token und Einlage. |
| `zag-erlaubnisanalyse-payment-institution` | ZAG-Erlaubnisanalyse für Zahlungsinstitute: Zahlungsdienste katalogisieren, § 10 ZAG, Eigenmittel, Geschäftsplan, Sicherung von Kundengeldern, Geschäftsleiter, Auslagerungen und BaFin-Antrag prüfen. |
| `zag-finanztransfergeschaeft-money-remittance` | Finanztransfergeschäft und Money Remittance nach ZAG prüfen: Weiterleitung von Geldbeträgen ohne Zahlungskonto, Agentenmodelle, Plattformfälle, Bargeld, Ausnahmen und BaFin-Erlaubnisrisiko. |
| `zag-kontoinformationsdienst-ais` | Kontoinformationsdienst nach ZAG und PSD2 prüfen: Registrierung, Datenzugriff, Schnittstelle, Consent, Versicherung, Datenschutz, Open-Banking-Verträge und White-Label-Modelle. |
| `zag-negativauskunft-feststellung-bafin` | ZAG-Negativauskunft oder informelle BaFin-Vorabklärung vorbereiten: Geschäftsmodell neutral beschreiben, Zahlungsfluss visualisieren, Erlaubnistatbestände abgrenzen und gefährliche Formulierungen vermeiden. |
| `zag-zahlungsausloesedienst-pis` | Zahlungsauslösedienst nach ZAG und PSD2 prüfen: Erlaubnis, starke Kundenauthentifizierung, Haftungskette, Interface, technische Dienstleister und Händlerkommunikation. |
| `zahlungsdienste-zag-psd3-psr` | Zahlungsdienste nach ZAG, PSD2-Folgefragen, PSD3- und PSR-Entwicklungen prüfen: Rollen, Erlaubnis, starke Kundenauthentifizierung, Haftung, Betrugsfälle und Beschwerdeantworten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
