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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agb-bankrecht-organhaftung-business` | Agb Bankrecht Klauselkontrolle, Organhaftung Business Judgment, Sanktionsscreening Embargo Bank, Crypto Tax Reporting Dac8 Car: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächste... |
| `app-fraud-aufsichtsrat-vorlage` | App Fraud Social Engineering Bank, Aufsichtsrat Vorlage Bank, Avalrahmenlinie Kautionsaval Praxis, Bafin Kommunikation Und Anhoerung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den n... |
| `bank-rechtsabteilung-kaltstart-triage` | Agb Bankrecht Klauselkontrolle, Anwaltliche Rechnungen Review, App Fraud Social Engineering Bank, Aufsichtsrat Vorlage Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `bankaufsichtsrecht-kwg-bankgeheimnis` | Bankaufsichtsrecht Kwg Marisk Triage, Bankgeheimnis Auskunftsersuchen, Banking As A Service White Label, Beteiligungserwerb Bank Ma: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nä... |
| `bankrechtsabteilung-kaltstart-routing` | Kaltstart-Routing für neue Inhouse-Anfragen in einer Bank: Sachgebiet erkennen, Eilbedarf markieren, BaFin-, Vorstand-, Kredit-, Vertrieb-, AGB-, Datenschutz- oder Prozesspfad wählen und genau die nächsten Unterlagen anfordern. |
| `blockchain-settlement-buergschaft-erste` | Blockchain Settlement Dvp, Buergschaft Auf Erste Anforderung Bank, Buergschaft Privatperson Gesellschafter Ehegatte, Chargeback Card Schemes Bankrecht: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `covenant-waiver-crr-crd-kapitalanforderungen` | Covenant Waiver Credit Documentation, Crr Crd Eigenmittel Large Exposure, Crr Kapitalanforderungen Juristenmatrix, Darlehensrecht Verbraucher Unternehmer: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `datenschutz-bankgeheimnis-depotrecht` | Datenschutz Bankgeheimnis, Depotrecht Tokenisierte Wertpapiere, Dlt Pilot Regime Market Infrastructure, Dokumentengeschaeft Akkreditiv Inkasso Standby: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage... |
| `dora-ict-einlagensicherung-kundenhinweise` | Dora Ict Vertraege Vorfall, Einlagensicherung Kundenhinweise, Embedded Finance Kooperation, Esg Sustainable Finance: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbar... |
| `ewpg-kryptowertpapierregister-registerwechsel` | Ewpg Kryptowertpapierregister Erlaubnis, Ewpg Registerwechsel Registerfehler, Fit Proper Eignungsmatrix Deep Dive, Fit Proper Organe Mitarbeiter: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `garantieabruf-missbrauch-garantieprovision` | Garantieabruf Missbrauch Und Zahlungsstopp, Garantieprovision Limit Und Risk Weighting, Kundenbeschwerde Ombudsmann Bafin, Litigation Schlichtung Prozess: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `geldwaesche-krypto-geschaeftsleiter` | Geldwaesche Krypto Wallet Screening, Geschaeftsleiter Abberufung Krise, Geschaeftsleiter Bestellung Kwg Zag, Girokonto Firmenkunden Risk Exit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lief... |
| `handelsvertreter-vertriebsrecht` | Handelsvertreter Vertriebsrecht Bank, Hauptversammlung Bank Aktg, Iban Name Check Verification Payee, Inhkontrollv Bedeutende Beteiligung Bank: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und lie... |
| `instant-payments-interne-richtlinie-it` | Instant Payments Sepa Vo, Interne Richtlinie Policy Drafting, It Sicherheit Cloud Vertraege, Kontokuendigung Sperre Basiskonto: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächste... |
| `kreditsicherheiten-bestellung` | Kreditsicherheiten Bestellung Verwertung, Kreditwesengesetz Erlaubnis Inhaberkontrolle, Liquiditaetsbruecke Firmenkunde Bankinstrumente, Ma Risk Compliance Funktion: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und R... |
| `micar-art-emt-casp-notifikation-whitepaper` | Micar Art Emt Bank Emission, Micar Casp Notifikation Bank Art60, Micar Whitepaper Marketing Bank, Mifid Wphg Anlageberatung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `outsourcing-operational-resilience-crypto-dlt` | Operational Resilience Concentration Risk, Outsourcing Crypto Dlt Node Provider, Outsourcing Externe Dienstleister, Outsourcing Fintech Bank As A Service: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `produktfreigabe-new-restrukturierung` | Produktfreigabe New Product Process, Restrukturierung Kreditengagement, Anwaltliche Rechnungen Review, Anzahlungs Gewaehrleistungs Und Erfuellungsgarantien: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrun... |
| `psd2-provisionsmodelle-vertrieb-fraud-refund` | Provisionsmodelle Vertrieb Compliance, Psd2 Fraud Refund Unauthorised Payment, Psd2 Open Banking Api Xs2a, Psd2 Sca Strong Customer Authentication: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und... |
| `rechtsabteilung-dora-auslagerung-ewpg` | Rechtsabteilung Dora Auslagerung Bei Kritischem Ict Dienstleiste, Rechtsabteilung Ewpg Tokenisierung Und Registerrisiko, Rechtsabteilung Npl Verkauf Mit Datenschutz Und Bankgeheimnis, Rechtsabteilung Psd2 Strong Customer Authentication F... |
| `rechtsmonitoring-bank-regress` | Rechtsmonitoring Bank, Regress Forderungsuebergang Und Sicherheitenfreigabe, Sanierungsgutachten Idw S6 Bewertung, Schluesselfunktionen Inhaber Fit Proper: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrund... |
| `ssm-bundesbank-stablecoin-payment-staking` | Ssm Bundesbank Aufsichtsbrief, Stablecoin Payment Usecase Bank, Staking Lending Token Bank, Stundung Standstill Waiver: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belast... |
| `syndizierte-kredite-tokenisierung-security` | Syndizierte Kredite Agent Security Trustee, Tokenisierung Security Token Mica Mifid, Trade Finance Sanctions Lc Guarantee, Travel Rule Krypto Transfers: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlag... |
| `zag-bafin-merkblatt-payment-flow-red-team` | ZAG-Red-Team nach BaFin-Arbeitslogik: Zahlungsfluss, Positivkatalog, Ausnahmen, E-Geld, Erlaubnis, Registrierung und Anzeigen so prüfen, dass Plattform-, Wallet-, Loyalty-, Agenten- und Embedded-Finance-Modelle nicht falsch freigegeben w... |
| `zag-erlaubnisanalyse-zag` | Zag Erlaubnisanalyse Payment Institution, Zag Finanztransfergeschaeft Money Remittance, Zag Kontoinformationsdienst Ais, Zag Negativauskunft Feststellung Bafin: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `zag-vorstandsvorlage-gutachten-wpig` | Vorstandsvorlage Gutachten, Wpig Wertpapierinstitut Schnittstelle, Zag Agenten Auslagerung Register, Zag Ausnahmen Limited Network Commercial Agent: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage un... |
| `zahlungsdienste-zag` | Zahlungsdienste Zag Psd3 Psr: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
