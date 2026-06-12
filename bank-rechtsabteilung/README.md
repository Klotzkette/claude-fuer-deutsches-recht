# Bank-Rechtsabteilung

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`bank-rechtsabteilung.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/bank-rechtsabteilung.md) (50 KB)
- Im Repo: [`testakten/megaprompts/bank-rechtsabteilung.md`](../testakten/megaprompts/bank-rechtsabteilung.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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
| **Meridian MedTech: Insiderrecht, Ad-hoc und M&A-Leak** (`insiderrecht-meridian-medtech-ad-hoc-ma-leak`) | [Gesamt-PDF lesen](../testakten/insiderrecht-meridian-medtech-ad-hoc-ma-leak/gesamt-pdf/insiderrecht-meridian-medtech-ad-hoc-ma-leak_gesamt.pdf) | [`testakte-insiderrecht-meridian-medtech-ad-hoc-ma-leak.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insiderrecht-meridian-medtech-ad-hoc-ma-leak.zip) |
| **Akte Rotorwerk: Maschinenleasing, Restwert und Insolvenzgerücht** (`leasingrecht-maschinenfleet-restwert-insolvenz`) | [Gesamt-PDF lesen](../testakten/leasingrecht-maschinenfleet-restwert-insolvenz/gesamt-pdf/leasingrecht-maschinenfleet-restwert-insolvenz_gesamt.pdf) | [`testakte-leasingrecht-maschinenfleet-restwert-insolvenz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-leasingrecht-maschinenfleet-restwert-insolvenz.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Rechtsabteilungs-Plugin für eine mittelgroße deutsche Bank: schnell genug für den internen Ticketkanal, sorgfältig genug für Vorstand, Aufsichtsrat, BaFin, Bundesbank, externe Kanzleien und späteren Aktenrückblick.

Es ist als Inhouse-Cockpit gedacht: nicht nur Bankrecht im engeren Sinn, sondern der ganze Alltag einer Bank-Rechtsabteilung. Aufsichtsrecht, Kredit, Avalrahmen, Bürgschaften, Bankgarantien, Akkreditive, Sanierung, Auslagerung, DORA, Geldwäsche, AGB, Handelsvertreter, Vertrieb, Beschwerden, Organvorlagen, Hauptversammlung, Beteiligungen, Datenschutz, Kanzleisteuerung und Rechnungsreview werden in einen einzigen Routing-Workflow gebracht. Die Spezialerweiterung deckt zusätzlich ZAG-Finanztransfer, PSD2/Open Banking, PSD3/PSR-Vorschau, eWpG, Kryptowertpapierregister, MiCAR, Tokenisierung, Instant Payments und digitale Bankprodukte ab. Der Aufsichtsrechtskern wurde um eine BaFin-/Gesetze-/EUR-Lex-gestützte Arbeitslogik für ZAG, DORA Artikel 16, AnzV, InhKontrollV und CRR erweitert.

## Für wen

| Rolle | Typische Nutzung |
| --- | --- |
| General Counsel / Chefjustiziar | Vorstandsvorlagen, Aufsichtsrat, Eskalation, Kanzleisteuerung |
| Syndikus in Legal | Gutachten, Vertragscheck, Fachbereichsberatung, BaFin-Antworten |
| Compliance / AML / Datenschutz | GwG, Sanktionen, DORA, Richtlinien, Meldungen, Findings |
| Marktfolge / Risk / Workout | Weiterfinanzierung, Stundung, Sanierungsgutachten, Sicherheiten |
| Trade Finance / Firmenkunden | Avale, Kautionsavale, Garantien, Akkreditive, Dokumenteninkasso, Abruf- und Regressfälle |
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
| Kunde braucht Kautions- oder Anzahlungsaval | `avalrahmenlinie-kautionsaval-praxis` | Avalfreigabe, Textänderungen, Limit-/Regresscheck |
| Begünstigter zieht Garantie | `garantieabruf-missbrauch-und-zahlungsstopp` | Pay/Hold/Reject-Entscheidung, Eilkommunikation, Regressplan |
| Bürgschaft auf erstes Anfordern liegt vor | `buergschaft-auf-erste-anforderung-bank` | Textauslegung, Abrufprüfung, Missbrauchsampel |
| Firmenkunde braucht Liquiditätsbrücke | `liquiditaetsbruecke-firmenkunde-bankinstrumente` | Instrumentenvergleich Aval, Linie, Factoring, Akkreditiv, Waiver |
| Sanierungsgutachten kommt rein | `sanierungsgutachten-idw-s6-bewertung` | Plausibilitätsreview, Red Flags, Nachforderungsliste |
| Vorstand braucht Vorlage | `vorstandsvorlage-gutachten` | Executive Summary, Optionen, Beschlussvorschlag |
| Kanzleirechnung ist zu hoch | `anwaltliche-rechnungen-review` | Rechnungsprüfung, Rückfragen, Kürzungsvorschlag |
| Handelsvertreter kündigt | `handelsvertreter-vertriebsrecht-bank` | Statusanalyse, Ausgleichsrisiko, Verhandlungsposition |
| AGB sollen geändert werden | `agb-bankrecht-klauselkontrolle` | Klauselampel, bessere Fassung, Rollout-Hinweise |
| Zahlungsmodell ist aufsichtsrechtlich unklar | `zag-bafin-merkblatt-payment-flow-red-team` | Flow-of-Funds, ZAG-Positivkatalog, Ausnahmen, BaFin-Red-Team |
| Kleines Finanzunternehmen will DORA pragmatisch umsetzen | `dora-art16-vereinfachter-ikt-rahmen` | Art.-16-Scope, Governance, Drittparteien, Nachweisordner |
| KWG-Anzeigen laufen quer durch HR, Legal und Vorstandsbüro | `anzv-kwg-anzeigenkalender-bafin-bundesbank` | Anzeigenkalender, Unterlagen, Einreichweg, Nachforderungslog |
| Bankbeteiligung soll erworben oder erhöht werden | `inhkontrollv-bedeutende-beteiligung-bank` | Schwellen, Erwerberkette, Finanzierung, Closing-CP |
| Kredit-/Beteiligungsfall hat Kapital- oder Großkreditfolgen | `crr-kapitalanforderungen-juristenmatrix` | Legal/Risk-Matrix, CRR-Fragen, Vorstandsvorlage |

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 119 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agb-bankrecht-organhaftung-business` | AGB-Recht für Banken: Klauseln nach §§ 305 bis 310 BGB, Preisänderungen, Zustimmungsmechanismen, Kündigung, Entgelte, Aufrechnung, Haftung und Verbrauchertransparenz prüfen im Bank-Rechtsabteilung. |
| `anwaltliche-rechnungen-review` | Anwaltliche Rechnungen und Kanzlei-Budgets reviewen: Scope-Abgleich, RVG oder Honorarvereinbarung, Zeitpositionen, Auslagen, USt, Doppelarbeit, Erfolg, Billing Guidelines und Kürzungsvorschlag im Bank-Rechtsabteilung. |
| `anzahlungs-gewaehrleistungs-und-erfuellungsgarantien` | Anzahlungs-, Gewährleistungs- und Vertragserfüllungsgarantien für Bankkunden prüfen: Sicherungszweck, Abruftext, Laufzeit, Projekt-/Baurisiko, Rückgabe, Reduzierung, Avalrahmen und Liquiditätseffekt im Bank-Rechtsabteilung. |
| `anzv-kwg-anzeigenkalender-bafin-bundesbank` | AnzV-Anzeigenkalender für KWG-Institute: Organpersonen, LEI, Beteiligungen, enge Verbindungen, Auslandsbeziehungen, Auslagerungen, Vergütung, Einreichweg und BaFin-/Bundesbank-Nachweise in einen fristfesten Legal-bringen im Bank-Rechtsab... |
| `app-fraud-aufsichtsrat-vorlage` | APP-Fraud, PushTAN und Social Engineering aus Bankensicht prüfen: Kundenschutz, Warnpflichten, PSD2/BGB-Haftung, SCA, Empfängerbank, Freeze, Recall und Prozessstrategie im Bank-Rechtsabteilung. |
| `aufsichtsrat-vorlage-bank` | Aufsichtsrats- und Ausschussvorlagen einer Bank vorbereiten: Informationspflicht, Beschlusskompetenz, Risikoausschuss, Prüfungsausschuss, Vertraulichkeit, Protokollfestigkeit und Follow-up im Bank-Rechtsabteilung. |
| `avalrahmenlinie-kautionsaval-praxis` | Avalrahmen und Kautionsaval in der Bankpraxis prüfen: Kreditgeschäft, Avalprovision, Limit, Sicherheiten, Abrufrisiko, Text der Garantie/Bürgschaft, § 1 KWG, §§ 765 ff. BGB, §§ 349 und 350 HGB und Regress sauber dokumentieren im Bank-Rec... |
| `bafin-kommunikation-und-anhoerung` | BaFin-Kommunikation und Anhörung: Antwortstrategie, Tonfall, Tatsachenklärung, Fristen, Vollständigkeit, Anerkenntnisrisiken, Aufsichtsdialog und Vorstandsinformation für Banken strukturieren im Bank-Rechtsabteilung. |
| `bafin-pruefung-vor-ort-management` | Vor-Ort-Prüfung, Sonderprüfung oder Aufsichtsprüfung in der Bank vorbereiten: Datenraum, Interviewliste, Kommunikationsregeln, Prüfungslog, Legal Privilege, Nachlieferungen und Abschlussbericht managen im Bank-Rechtsabteilung. |
| `bankaufsichtsrecht-kwg-bankgeheimnis` | Bankaufsichtsrechtliche Ersttriage nach KWG und MaRisk: Geschäftsorganisation, Risikomanagement, Compliance, Revision, Risikocontrolling, Leitungsbefassung und Dokumentationsbedarf für interne Vermerke prüfen im Bank-Rechtsabteilung. |
| `bankgeheimnis-auskunftsersuchen` | Auskunftsersuchen an Banken prüfen: Polizei, Staatsanwaltschaft, Gericht, Finanzamt, Insolvenzverwalter, Betreuer, Erben, Anwälte und Privatpersonen sicher auseinanderhalten im Bank-Rechtsabteilung. |
| `banking-as-a-service-white-label` | White-Label-Banking juristisch strukturieren: Bankrolle sichtbar machen, Partnerpflichten, Kundenschutz, AGB, Datenschutz, Auslagerung, Beschwerden, Vertriebsrecht und Reputationsrisiko im Bank-Rechtsabteilung. |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `beteiligungserwerb-bank-ma` | Beteiligungserwerb, M&A und strategische Kooperation einer Bank prüfen: Erlaubnisse, Inhaberkontrolle, Beteiligungsgrenzen, Due Diligence, Kartell, Datenschutz, Sanierung und Gremien im Bank-Rechtsabteilung. |
| `betriebsrat-change-projekte` | Betriebsrat und arbeitsrechtliche Schnittstellen bei Bankprojekten: Restrukturierung, IT-Einführung, Monitoring, variable Vergütung, Auslagerung, Filialschließung und Betriebsänderung prüfen im Bank-Rechtsabteilung. |
| `blockchain-settlement-buergschaft-erste` | Blockchain-Settlement und Delivery-versus-Payment prüfen: Wertpapierseite, Geldseite, Finalität, CSD, Token Cash, Smart Contract, Fehlerkorrektur und Rechtswahl im Bank-Rechtsabteilung. |
| `buergschaft-auf-erste-anforderung-bank` | Bürgschaft oder Garantie auf erste Anforderung aus Bankensicht prüfen: Textauslegung, Abrufmechanik, offensichtlicher Rechtsmissbrauch, einstweiliger Rechtsschutz, Regress gegen Kunden und Dokumentation der Zahlungsentscheidung im Bank-R... |
| `buergschaft-privatperson-gesellschafter-ehegatte` | Privatpersonen-, Gesellschafter- und Ehegattenbürgschaften aus Bankensicht prüfen: Schriftform, krasse finanzielle Überforderung, Sittenwidrigkeit, Verbraucherschutz, Aufklärung, Sicherheitenwert und Prozessrisiko im Bank-Rechtsabteilung. |
| `chargeback-card-schemes-bankrecht` | Chargeback und Card-Scheme-Disputes rechtlich begleiten: Mastercard/Visa-Regeln, Zahlungsdienstehaftung, Händlerstreit, Fristen, Belege, Kundenerwartung und Kulanzgrenzen im Bank-Rechtsabteilung. |
| `correspondent-banking-nostro-vostro` | Korrespondenzbankbeziehungen und Nostro/Vostro-Risiken prüfen: AML, Sanktionen, Länder, Zahlungswege, Vertragsklauseln, Informationsrechte, Kündigung und Aufsichtserwartungen im Bank-Rechtsabteilung. |
| `covenant-waiver-crr-crd-kapitalanforderungen` | Covenant Waiver und Kreditdokumentation tief prüfen: Financial Covenants, MAC, Events of Default, Informationspflichten, Cure Rights, Margin Step-up und Dokumentationsschutz im Bank-Rechtsabteilung. |
| `crr-crd-eigenmittel-large-exposure` | CRR-, CRD- und Großkredit-Schnittstelle für Juristen: Eigenmittelbegriffe, Large Exposure, Organkredite, Beteiligungen, Limitüberschreitungen und Governance-Freigaben verständlich prüfen im Bank-Rechtsabteilung. |
| `crr-kapitalanforderungen-juristenmatrix` | CRR-Juristenmatrix für Bank-Legal: Art.-4-Begriffe, Eigenmittel, Großkredite, Gruppen verbundener Kunden, Liquidität, Leverage, Sicherheiten, Garantien und Vertragsfolgen in Legal Notes und Vorstandsvorlagen übersetzen im Bank-Rechtsabte... |
| `crypto-tax-reporting-dac8-car` | Krypto-Steuerreporting, DAC8 und CARF als Bank-Monitoring prüfen: Datenfelder, Meldepflichtige, CASP-Schnittstelle, Kundenkommunikation, Datenschutz und Roadmap im Bank-Rechtsabteilung. |
| `darlehensrecht-verbraucher-unternehmer` | Darlehensrecht für Banken: Verbraucher- und Unternehmenskredit, Pflichtangaben, Widerruf, Kündigung, Sicherheiten, Zahlungsverzug, Vorfälligkeitsfragen und Prozessrisiko prüfen im Bank-Rechtsabteilung. |
| `datenraum-bank-transaktion` | Datenraum für Bank-Transaktionen oder Aufsichtsprüfungen strukturieren: Dokumentenindex, Berechtigungen, Schwärzungen, Bankgeheimnis, Datenschutz, Q&A und Audit Trail im Bank-Rechtsabteilung. |
| `datenschutz-bankgeheimnis-depotrecht` | Datenschutz, Bankgeheimnis und Mandatsgeheimnis in der Bank: Datenbasis, Offenlegung, Dienstleister, Auskunft, Löschung, Behördenzugriff, KI-Nutzung und Geheimnisschutz prüfen im Bank-Rechtsabteilung. |
| `depotrecht-tokenisierte-wertpapiere` | Depotrecht und tokenisierte Wertpapiere prüfen: Depotvertrag, Verwahrung, Registereintragung, Abwicklung, Bestandsschutz, Anlegerauskunft, Verlustfall und Schnittstelle zu eWpG/MiFID im Bank-Rechtsabteilung. |
| `dlt-pilot-regime-market-infrastructure` | DLT Pilot Regime für Marktinfrastrukturen prüfen: DLT-MTF, DLT-SS, DLT-TSS, Token Settlement, Ausnahmen, Aufsicht, Depot-/CSD-Schnittstellen und Bankrollen im Bank-Rechtsabteilung. |
| `dokumentengeschaeft-akkreditiv-inkasso-standby` | Dokumentengeschäft der Bank prüfen: Akkreditiv, Dokumenteninkasso, Standby Letter of Credit, UCP/URC/ISP-Bezug, Dokumentenstrenge, Fraud, Sanktionen, Warenfluss und Zahlungsentscheidung im Bank-Rechtsabteilung. |
| `dora-art16-vereinfachter-ikt-rahmen` | DORA Artikel 16 für kleinere oder privilegierte Finanzunternehmen: vereinfachten IKT-Risikomanagementrahmen, Governance, Asset-Inventar, Need-to-use, Business Continuity, Drittparteienrisiko, Vertragslücken und Nachweisordner prüfbar mac... |
| `dora-ict-einlagensicherung-kundenhinweise` | DORA-IKT-Verträge und IKT-Vorfälle: Pflichtklauseln, Register, Exit, Überwachungsrechte, Suboutsourcing, Incident-Klassifizierung, Meldewege und Managementbericht prüfen im Bank-Rechtsabteilung. |
| `einlagensicherung-kundenhinweise` | Einlagensicherung und Kundenhinweise: gesetzliche und institutsspezifische Sicherung, Informationsbogen, Produktabgrenzung, Markenauftritt, Filialhinweise und Beschwerdekommunikation prüfen im Bank-Rechtsabteilung. |
| `embedded-finance-kooperation` | Embedded-Finance-Kooperationen prüfen: Händler, Plattform, Bank, Zahlungsdienstleister, Kreditangebot, Vermittlung, Scoring, Datenschutz, Provision und Erlaubnisrisiken im Bank-Rechtsabteilung. |
| `esg-sustainable-finance` | ESG und Sustainable Finance in der Bank: Offenlegung, Taxonomie, Green Claims, Kreditpolitik, Anlageprodukte, Reputationsrisiko und Vorstandskommunikation prüfen im Bank-Rechtsabteilung. |
| `ewpg-emission-elektronische-wertpapiere` | Emission elektronischer Wertpapiere nach eWpG prüfen: Zentralregister, Kryptowertpapierregister, Emissionsbedingungen, Registerangaben, Prospekt, Depot, Vertrieb und Anlegerkommunikation im Bank-Rechtsabteilung. |
| `ewpg-kryptowertpapierregister-registerwechsel` | Kryptowertpapierregisterführung nach eWpG und KWG prüfen: Finanzdienstleistung, § 32 KWG-Erlaubnis, Registerfunktion, Betreiberrolle, Geschäftsleiter, IT, DORA und BaFin-Merkblatt im Bank-Rechtsabteilung. |
| `ewpg-registerwechsel-registerfehler` | Registerwechsel, Registerfehler und Anlegerrechte bei elektronischen Wertpapieren prüfen: Berichtigung, Übertragung, Funktionsstörung, Kündigungsrechte, Haftung und Kommunikationspflichten im Bank-Rechtsabteilung. |
| `externe-anwaelte-steuerung` | Externe Anwälte und Kanzleien steuern: Mandatsbrief, Scope, Budget, Reporting, Privilege, Interessenkonflikte, Rechtsmeinungen, Second Opinion und internes Wissen sichern im Bank-Rechtsabteilung. |
| `fit-proper-eignungsmatrix-deep-dive` | Fit-and-Proper-Eignungsmatrix für Geschäftsleiter, Aufsichtsräte und Schlüsselfunktionen vertiefen: fachliche Eignung, Zuverlässigkeit, Kollektiveignung, Diversität, Interessenkonflikte und Fortbildung im Bank-Rechtsabteilung. |
| `fit-proper-organe-mitarbeiter` | Fit-and-Proper für Geschäftsleiter, Aufsichtsrat und Schlüsselfunktionen: Sachkunde, Zuverlässigkeit, Zeitbudget, Interessenkonflikte, Anzeigen und Nachweise vorbereiten im Bank-Rechtsabteilung. |
| `forbearance-npe-risikoklassifizierung` | Forbearance, NPE und Risikoklassifizierung juristisch begleiten: Zugeständnisse, Ausfallnähe, Melde- und Dokumentationsfolgen, Kreditakte und Kommunikation mit Risk sauber halten im Bank-Rechtsabteilung. |
| `garantieabruf-missbrauch-garantieprovision` | Abruf aus Bankgarantie, Aval oder Bürgschaft auf erstes Anfordern im Eilfall steuern: formale Prüfung, Missbrauchseinwand, Zahlungsstopp, einstweiliger Rechtsschutz, Kundenkommunikation und Regress im Bank-Rechtsabteilung. |
| `garantieprovision-limit-und-risk-weighting` | Aval- und Garantiegeschäft wirtschaftlich-juristisch steuern: Garantieprovision, Limitnutzung, Risikoklassifizierung, Kreditäquivalent, Sicherheiten, Covenants, Forbearance, NPE und Vorstandsvorlage im Bank-Rechtsabteilung. |
| `geldwaesche-krypto-geschaeftsleiter` | Krypto-AML und Wallet-Screening für Banken prüfen: Wallet-Risiko, Chain Analytics, Mixer, Bridges, Darknet-Indizien, PEP/Sanktionen, Verdachtsmeldung und De-Risking im Bank-Rechtsabteilung. |
| `geschaeftsleiter-abberufung-krise` | Abberufung, Suspendierung oder Ressortentzug von Geschäftsleitern in Banken prüfen: KWG, Organrecht, Dienstvertrag, BaFin-Risiko, Aufsichtsratskompetenz, Ad-hoc-Krise und Kommunikationsplan im Bank-Rechtsabteilung. |
| `geschaeftsleiter-bestellung-kwg-zag` | Geschäftsleiterbestellung nach KWG, ZAG und KAGB tief prüfen: Absichtsanzeige, Vollzugsanzeige, Zuverlässigkeit, fachliche Eignung, Zeitbudget, Lebenslauf, Führungszeugnis, Eignungsmatrix und BaFin-Kommunikation im Bank-Rechtsabteilung. |
| `girokonto-firmenkunden-risk-exit` | Firmenkunden-Girokonto, Risk Exit und De-Risking prüfen: Kündigung, Sperre, AML, Sanktionen, Diskriminierungsrisiko, Zahlungsverkehrsabhängigkeit und saubere Kundenkommunikation im Bank-Rechtsabteilung. |
| `gwg-aml-kyc-verdachtsmeldung` | GwG-, AML- und KYC-Prüfung für Banken: Risikoanalyse, wirtschaftlich Berechtigte, PEP, Sanktionen, Transaktionsmonitoring, Verdachtsmeldung und Dokumentation ohne unnötige Selbstbelastung strukturieren im Bank-Rechtsabteilung. |
| `handelsvertreter-vertriebsrecht` | Handelsvertreter- und Vertriebsrecht für Banken: § 84 HGB, Ausgleich § 89b HGB, Vermittlerstatus, Tippgeber, Ausschließlichkeit, Provision, Kündigung und Compliance prüfen im Bank-Rechtsabteilung. |
| `hauptversammlung-bank-aktg` | Hauptversammlung einer Bank rechtlich vorbereiten: Tagesordnung, Beschlussvorschläge, Vorstand/Aufsichtsrat, Vergütung, Kapitalmaßnahmen, Satzung, Gegenanträge und Stimmrechtsfragen im Bank-Rechtsabteilung. |
| `iban-name-check-verification-payee` | Verification of Payee und IBAN-Name-Check prüfen: Matching-Logik, Haftung, Warntexte, Firmenkunden, Sammelzahlungen, Datenschutz, Fraud-Reduktion und Prozessdokumentation im Bank-Rechtsabteilung. |
| `inhkontrollv-bedeutende-beteiligung-bank` | Inhaberkontrollverfahren bei Banken: bedeutende Beteiligung, mittelbare Kontrolle, Erwerberkette, Finanzierung, Zuverlässigkeit, Schwellen, Übersetzungen, Closing-Condition und BaFin-/Bundesbank-Dealfahrplan prüfen im Bank-Rechtsabteilung. |
| `insolvenz-anfechtung-bank` | Insolvenzanfechtung gegen Banken vorbeugen und verteidigen: Sicherheitenbestellung, Rückführung, Kontokorrent, inkongruente Deckung, Kenntnis, Bargeschäft und Anfechtungsgegner-Argumente prüfen im Bank-Rechtsabteilung. |
| `instant-payments-interne-richtlinie-it` | Instant Payments und SEPA-Echtzeitüberweisungen prüfen: Verfügbarkeit, Gebühren, Sanktionsscreening, Verification of Payee, Betrugsprävention, Kundenkommunikation und technische Umsetzungsrisiken im Bank-Rechtsabteilung. |
| `interne-richtlinie-policy-drafting` | Interne Richtlinien und Policies für Banken entwerfen: Normenbasis, Zielgruppe, Rollen, Kontrollen, Eskalation, Dokumentation, Versionierung, Schulung und Vorstandsbeschluss im Bank-Rechtsabteilung. |
| `it-sicherheit-cloud-vertraege` | IT-Sicherheit und Cloud-Verträge einer Bank prüfen: DORA, NIS2-Schnittstelle, Datenschutz, Audit-Rechte, Exit, Verschlüsselung, Incident Response, Subdienstleister und Bankaufsicht im Bank-Rechtsabteilung. |
| `kaltstart-triage` | Agb Bankrecht Klauselkontrolle, Anwaltliche Rechnungen Review, App Fraud Social Engineering Bank, Aufsichtsrat Vorlage Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `kontokuendigung-sperre-basiskonto` | Kontokündigung, Kontosperre und Basiskonto prüfen: Vertragsrecht, AGB, GwG, Sanktionen, Pfändung, Diskriminierungsrisiko, Sozialleistungen und Kundenkommunikation ausbalancieren im Bank-Rechtsabteilung. |
| `kreditentscheidung-weiterfinanzierung` | Kreditentscheidung und Weiterfinanzierung: neue Auszahlung, Prolongation, Covenant-Bruch, Sanierungsphase, Risikovotum, Organpflichten und Dokumentation der Bankentscheidung prüfen im Bank-Rechtsabteilung. |
| `kreditsicherheiten-bestellung` | Kreditsicherheiten bestellen, prüfen und verwerten: Grundschuld, Bürgschaft, Garantie, Globalzession, Sicherungsübereignung, Pfandrechte, Rang, Freigabe und Verwertungsschritte im Bank-Rechtsabteilung. |
| `kreditwesengesetz-erlaubnis-inhaberkontrolle` | KWG-Erlaubnis, Erlaubniserweiterung, Inhaberkontrolle und qualifizierte Beteiligung prüfen: Geschäftsmodell, Schwellen, Anzeige, Fit-and-Proper und BaFin-Erwartungen strukturieren im Bank-Rechtsabteilung. |
| `kundenbeschwerde-ombudsmann-bafin` | Kundenbeschwerden, Ombudsmann, BaFin-Beschwerde und Eskalation: Sachverhalt, Anspruch, Kulanz, Reputationsrisiko, Fristen, Ton und interne Learnings für Banken steuern im Bank-Rechtsabteilung. |
| `liquiditaetsbruecke-firmenkunde-bankinstrumente` | Bankinstrumente als Liquiditätsbrücke für Firmenkunden strukturieren: Aval, Kontokorrent, Factoring, Forfaitierung, Akkreditiv, Lieferantenkredit, Stundung, Waiver und Sanierungsnähe mit Rechts- und Risikomatrix im Bank-Rechtsabteilung. |
| `litigation-schlichtung-prozess` | Litigation, Schlichtung und Prozessführung einer Bank: Anspruch, Beweise, Kosten, Vergleich, Musterverfahren, Ombudsmann, externe Kanzlei und Vorstandsinformation steuern im Bank-Rechtsabteilung. |
| `ma-risk-compliance-funktion` | MaRisk-Compliance-Funktion und zweite Verteidigungslinie prüfen: Aufgaben, Unabhängigkeit, Compliance-Plan, Monitoring, Findings, Berichtslinie und Verhältnis zu Recht, Risk und Revision im Bank-Rechtsabteilung. |
| `marisk-auslagerungen-at9-dora` | MaRisk-Auslagerung und DORA-Schnittstelle: AT 9, § 25b KWG, Auslagerungsregister, Risikoanalyse, wesentliche Auslagerung, IKT-Drittanbieter und Exit-Plan zusammen prüfen im Bank-Rechtsabteilung. |
| `micar-art-emt-casp-notifikation-whitepaper` | ART- und EMT-Emission nach MiCAR für Banken prüfen: Asset-Referenced Token, E-Geld-Token, Zulassung, Whitepaper, Reserve, Rücktausch, Governance und Zahlungsdienste-Schnittstelle im Bank-Rechtsabteilung. |
| `micar-casp-notifikation-bank-art60` | MiCAR-CASP-Notifikation für Banken nach Art. 60 prüfen: bestehende Erlaubnis, Kryptowerte-Dienstleistung, 40-Arbeitstage-Frist, Unterlagen, BaFin/Bundesbank-Kommunikation und DORA-Schnittstelle im Bank-Rechtsabteilung. |
| `micar-whitepaper-marketing-bank` | MiCAR-Whitepaper und Marketing für Kryptowerte prüfen: Pflichtinhalte, Notifizierung, Werbung, Risikoangaben, Website, Social Media, Vertriebspartner und Haftungsrisiken im Bank-Rechtsabteilung. |
| `mifid-wphg-anlageberatung` | WpHG- und MiFID-II-Pflichten bei Anlageberatung und Vertrieb: Geeignetheit, Angemessenheit, Zielmarkt, Kosteninformation, Zuwendungen, ESG-Präferenzen und Dokumentation prüfen im Bank-Rechtsabteilung. |
| `notfallplan-krisenkommunikation` | Notfallplan und Krisenkommunikation für Bank-Legal: Cyberangriff, Bank Run, BaFin-Maßnahme, Medienanfrage, Whistleblowing, Großschaden oder Vorstandskrise strukturieren im Bank-Rechtsabteilung. |
| `organhaftung-business-judgment` | Organhaftung und Business Judgment Rule in der Bank: Vorstand, Aufsichtsrat, Ausschüsse, Informationsgrundlage, Interessenkonflikte, Dokumentation und D&O-Risiken prüfen im Bank-Rechtsabteilung. |
| `organwechsel-ssm-imas-mvp` | Organwechsel bei SI, LSI und Zahlungsinstituten über SSM-IMAS, MVP oder Formulare steuern: Zuständigkeit, Einreichkanal, Fristen, Unterlagen, Nachfragen und Vorstandsbüro-Briefing im Bank-Rechtsabteilung. |
| `outsourcing-crypto-dlt-node-provider` | Crypto-/DLT-Dienstleister und Node Provider auslagern: DORA, MaRisk, § 25b KWG, Verwahrung, Daten, Schlüssel, Subdienstleister, Audit-Rechte und Exit in Krypto-Projekten prüfen im Bank-Rechtsabteilung. |
| `outsourcing-externe-dienstleister` | Externe Dienstleister außerhalb reiner IKT prüfen: Auslagerung, sonstiger Fremdbezug, Datenschutz, Bankgeheimnis, SLA, Prüfungsrechte, Kündigung, Business Continuity und Registerpflege im Bank-Rechtsabteilung. |
| `outsourcing-fintech-bank-as-a-service` | FinTech-Outsourcing und Bank-as-a-Service prüfen: Rollen, KWG/ZAG, White Label, Auslagerung, Vertrieb, AML, Kundenkommunikation, Haftung und Exit im Bank-Rechtsabteilung. |
| `outsourcing-operational-resilience-crypto-dlt` | Operational Resilience und Konzentrationsrisiken bei Bankdienstleistern prüfen: kritische Funktionen, Auslagerungscluster, Cloud-Konzentration, DORA, Exit, Stresstest und Vorstandsvorlage im Bank-Rechtsabteilung. |
| `pfandbriefbank-spezialdeckung` | Pfandbrief- und Spezialdeckungsfragen aus Bank-Legal-Sicht prüfen: Deckungsmasse, Treuhänder, Indeckungnahme, Immobilienfinanzierung, Register, Aufsicht und Vorstandsfreigabe im Bank-Rechtsabteilung. |
| `produktfreigabe-new-restrukturierung` | New Product Process einer Bank: Produktidee, Zielmarkt, Recht, Aufsicht, Steuern, IT, Datenschutz, Vertrieb, Risiko, Operations und Vorstandfreigabe in einen sauberen NPP bringen im Bank-Rechtsabteilung. |
| `psd2-fraud-refund-unauthorised-payment` | Unautorisierte Zahlung und Refund nach PSD2/BGB prüfen: § 675u BGB, § 675v BGB, grobe Fahrlässigkeit, Social Engineering, Beweislast, SCA-Logs und Vergleichsstrategie im Bank-Rechtsabteilung. |
| `psd2-open-banking-api-xs2a` | Open-Banking- und XS2A-Schnittstellen prüfen: Zugang zu Zahlungskonten, API-Verfügbarkeit, Fallback, TPP-Kommunikation, Consent, Sicherheit, Haftung und Aufsichtsbeschwerde im Bank-Rechtsabteilung. |
| `psd2-provisionsmodelle-vertrieb-fraud-refund` | Provisionsmodelle und Vertriebscompliance prüfen: Zuwendungen, Interessenkonflikte, MiFID, Verbraucherschutz, Vergütungsrichtlinien, Zielvorgaben und Vorstandsvorlage für Produktvertrieb im Bank-Rechtsabteilung. |
| `psd2-sca-strong-customer-authentication` | Starke Kundenauthentifizierung nach PSD2 prüfen: Zwei-Faktor-Logik, Ausnahmen, Transaktionsrisikoanalyse, App-Freigabe, Delegation, Betrugsfall und Kundenkommunikation im Bank-Rechtsabteilung. |
| `psd3-psr-vorschau-gap-analysis` | PSD3- und PSR-Vorschau für Banken: geplantes EU-Zahlungsdienste-Paket gegen bestehende PSD2/ZAG-Prozesse mappen, Fraud, Open Banking, Transparenz und organisatorische Gaps vorbereiten im Bank-Rechtsabteilung. |
| `rechtsabteilung-dora-auslagerung-ewpg` | Rechtsabteilungs-Fachmodul für DORA-Auslagerung bei kritischem ICT-Dienstleister: ICT-Verträge, Exit-Pläne, Register of Information und Vorstandsvorlagen werden in einem Stresscheck zusammengeführt. Mit Normen, Rechtsprechungsanker, Bele... |
| `rechtsabteilung-ewpg-tokenisierung-und-registerrisiko` | Rechtsabteilungs-Fachmodul für eWpG-Tokenisierung und Registerrisiko: Tokenisierte Wertpapiere werden auf Registerführung, Verwahrung, Vertrieb und Prospekt-/MiCAR-Schnittstelle geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und... |
| `rechtsabteilung-npl-verkauf-mit-datenschutz-und-bankgeheimnis` | Rechtsabteilungs-Fachmodul für NPL-Verkauf mit Datenschutz und Bankgeheimnis: Notleidende Forderungen werden für Abtretung, Datenraum, Schuldnerinformation und Servicing rechtssicher vorbereitet. Mit Normen, Rechtsprechungsanker, Belegma... |
| `rechtsabteilung-psd2-strong-customer-authentication-fall` | Rechtsabteilungs-Fachmodul für PSD2-Strong-Customer-Authentication-Fall: Haftung bei nicht autorisierten Zahlungsvorgängen wird mit Beweislast, Authentifizierungslog und Kulanzstrategie geprüft. Mit Normen, Rechtsprechungsanker, Belegmat... |
| `rechtsabteilung-schufa-score-und-automatisierte-kreditentscheidu` | Rechtsabteilungs-Fachmodul für Schufa-Score und automatisierte Kreditentscheidung: Kreditprozesse werden darauf geprüft, ob der Score nur Hilfsinformation oder faktisch entscheidend ist. Mit Normen, Rechtsprechungsanker, Belegmatrix und... |
| `rechtsmonitoring-bank-regress` | Rechtsmonitoring für Banken einrichten: BaFin, Bundesbank, EBA, EZB, EU, Bundesgesetzblatt, Rechtsprechung, Verbände, Relevanzfilter und Umsetzungslog dokumentieren im Bank-Rechtsabteilung. |
| `regress-forderungsuebergang-und-sicherheitenfreigabe` | Regress nach Bürgschafts-, Aval- oder Garantiezahlung prüfen: Forderungsübergang § 774 BGB, Kundenbelastung, Sicherheitenverwertung, Mitbürgen, Freigabepflichten, Insolvenz und Vergleich im Bank-Rechtsabteilung. |
| `restrukturierung-kreditengagement` | Restrukturierung eines Kreditengagements steuern: Strategie, Sicherheiten, Pool, StaRUG-/InsO-Schnittstelle, Sanierungsbeiträge, Kommunikation und interne Kreditakte ordnen im Bank-Rechtsabteilung. |
| `sanierungsgutachten-idw-s6-bewertung` | Eingehende Sanierungsgutachten nach IDW S 6 aus Bankperspektive bewerten: Krisenstadien, Fortbestehen, Leitbild, Maßnahmen, integrierte Planung, Plausibilität und Kreditentscheidung im Bank-Rechtsabteilung. |
| `sanktionsscreening-embargo-bank` | Sanktionsscreening und Embargo in der Bank: Treffer, False Positive, EU-Sanktionen, OFAC-Berührung, Zahlungsstopp, Kontosperre, Freigabeprozess und Kundenkommunikation steuern im Bank-Rechtsabteilung. |
| `schluesselfunktionen-inhaber-fit-proper` | Inhaber besonderer Schlüsselfunktionen in großen Banken prüfen: Anzeige, Eignung, Zuverlässigkeit, Zeitverfügbarkeit, Rollenabgrenzung und Eskalation an Aufsicht oder Vorstand im Bank-Rechtsabteilung. |
| `sepa-direct-debit-return-disputes` | SEPA-Lastschrift-Rückgaben und Mandatsstreit prüfen: Core/B2B, Mandat, Rückgabefristen, Erstattungsanspruch, Firmenkundenrisiko, Händlerkommunikation und Prozessbelege im Bank-Rechtsabteilung. |
| `ssm-bundesbank-stablecoin-payment-staking` | SSM-, EZB- und Bundesbank-Aufsichtsbriefe für Institute einordnen: Zuständigkeit, JST-Kommunikation, nationale Umsetzung, Fristen, Management Letter, Follow-up und Board-Package vorbereiten im Bank-Rechtsabteilung. |
| `stablecoin-payment-usecase-bank` | Stablecoin-Zahlungsusecase für Banken prüfen: EMT/ART, E-Geld, Zahlungsdienst, Wallet, Händlerakzeptanz, Reserve, Rücktausch, Sanktionsscreening und Settlement im Bank-Rechtsabteilung. |
| `staking-lending-token-bank` | Staking, Lending und Yield-Produkte mit Tokenbezug prüfen: Produktqualifikation, MiCAR, KWG/WpIG, AGB, Verbraucherhinweise, Verwahrung, Insolvenztrennung und Reputationsrisiko im Bank-Rechtsabteilung. |
| `stundung-standstill-waiver` | Stundung, Standstill, Waiver und Covenant-Reset entwerfen und prüfen: Bankinteressen, Sicherheiten, Sanierungspfad, Gleichbehandlung, Kündigungsrechte und Dokumentationsschutz im Bank-Rechtsabteilung. |
| `sustainability-linked-loan-greenwashing` | Sustainability-Linked Loans und Greenwashing-Risiken prüfen: KPI, SPT, Margin Ratchet, externe Verifikation, Offenlegung, Kreditdokumentation und Reputationsschutz im Bank-Rechtsabteilung. |
| `syndizierte-kredite-tokenisierung-security` | Syndizierte Kredite, Facility Agent und Security Trustee prüfen: Rollen, Mehrheitsentscheidungen, Sicherheitenpool, Parallel Debt, deutsches Recht, Enforcement und Sanierungsfall im Bank-Rechtsabteilung. |
| `tokenisierung-security-token-mica-mifid` | Tokenisierung und Security Token einordnen: MiFID-Finanzinstrument, eWpG-Kryptowertpapier, MiCAR-Kryptowert, Vermögensanlage, Prospektpflicht und Vertriebsregime trennscharf prüfen im Bank-Rechtsabteilung. |
| `trade-finance-sanctions-lc-guarantee` | Trade Finance, Letter of Credit und Garantien prüfen: Sanktionen, Exportkontrolle, UCP/URDG, Dokumentenstrenge, Betrugsverdacht, Boykottklauseln und Zahlungsstopp im Bank-Rechtsabteilung. |
| `travel-rule-krypto-transfers` | Travel Rule für Krypto-Transfers prüfen: Auftraggeber-/Begünstigtendaten, CASP-Pflichten, Wallets, unhosted Wallets, Screening, Ablehnung, Monitoring und Kundenkommunikation im Bank-Rechtsabteilung. |
| `verwahrung-kryptowerte-bank-custody` | Kryptowerte-Verwahrung und Custody durch Banken prüfen: MiCAR-CASP, alte KWG-Erlaubnisse, Wallet-Control, Schlüsselmanagement, Outsourcing, Haftung, DORA und Kundentrennung im Bank-Rechtsabteilung. |
| `wpig-wertpapierinstitut-schnittstelle` | WpIG-Schnittstellen prüfen, wenn Bankgruppe, Wertpapierinstitut, Vermittler oder Tochtergesellschaft beteiligt sind: Rollen, Erlaubnis, Eigenmittel, Auslagerung und Governance abgrenzen im Bank-Rechtsabteilung. |
| `zag-agenten-auslagerung-register` | ZAG-Agenten, E-Geld-Agenten und Auslagerung prüfen: Register, Haftung, Weisungen, Schulungen, AML, Kundenkommunikation, Passporting und Abgrenzung zum bloßen Dienstleister im Bank-Rechtsabteilung. |
| `zag-ausnahmen-limited-network-commercial-agent` | ZAG-Ausnahmen tief prüfen: begrenztes Netz, begrenzte Produktpalette, Handelsvertreterausnahme, technische Dienstleister, Konzernprivileg und digitale Plattformrisiken im Bank-Rechtsabteilung. |
| `zag-e-geld-institut-emoney` | E-Geld-Institut und E-Geld-Geschäft nach ZAG prüfen: Ausgabe, Rücktausch, monetärer Wert, Akzeptanzstellen, Sicherungsmittel, Eigenmittel, Vertrieb und Abgrenzung zu Gutschein, Token und Einlage im Bank-Rechtsabteilung. |
| `zag-erlaubnisanalyse` | ZAG-Erlaubnisanalyse für Zahlungsinstitute: Zahlungsdienste katalogisieren, § 10 ZAG, Eigenmittel, Geschäftsplan, Sicherung von Kundengeldern, Geschäftsleiter, Auslagerungen und BaFin-Antrag prüfen im Bank-Rechtsabteilung. |
| `zag-finanztransfergeschaeft-money-remittance` | Finanztransfergeschäft und Money Remittance nach ZAG prüfen: Weiterleitung von Geldbeträgen ohne Zahlungskonto, Agentenmodelle, Plattformfälle, Bargeld, Ausnahmen und BaFin-Erlaubnisrisiko im Bank-Rechtsabteilung. |
| `zag-kontoinformationsdienst-ais` | Kontoinformationsdienst nach ZAG und PSD2 prüfen: Registrierung, Datenzugriff, Schnittstelle, Consent, Versicherung, Datenschutz, Open-Banking-Verträge und White-Label-Modelle im Bank-Rechtsabteilung. |
| `zag-negativauskunft-feststellung-bafin` | ZAG-Negativauskunft oder informelle BaFin-Vorabklärung vorbereiten: Geschäftsmodell neutral beschreiben, Zahlungsfluss visualisieren, Erlaubnistatbestände abgrenzen und gefährliche Formulierungen vermeiden im Bank-Rechtsabteilung. |
| `zag-payment-flow-red-team` | ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben w... |
| `zag-vorstandsvorlage-gutachten-wpig` | Vorstandsvorlage und juristisches Gutachten für eine Bank erstellen: Entscheidungssatz, Risikoampel, Handlungsoptionen, Beschlussvorschlag, Annahmen, Quellen und Anlagenverzeichnis im Bank-Rechtsabteilung. |
| `zag-zahlungsausloesedienst-pis` | Zahlungsauslösedienst nach ZAG und PSD2 prüfen: Erlaubnis, starke Kundenauthentifizierung, Haftungskette, Interface, technische Dienstleister und Händlerkommunikation im Bank-Rechtsabteilung. |
| `zahlungsdienste-zag-psd3-psr` | Zahlungsdienste nach ZAG, PSD2-Folgefragen, PSD3- und PSR-Entwicklungen prüfen: Rollen, Erlaubnis, starke Kundenauthentifizierung, Haftung, Betrugsfälle und Beschwerdeantworten: Zahlungsdienste nach ZAG, PSD2-Folgefragen, PSD3- und PSR-E... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
