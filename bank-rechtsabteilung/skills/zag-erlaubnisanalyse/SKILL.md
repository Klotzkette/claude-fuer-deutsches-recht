---
name: zag-erlaubnisanalyse
description: "Zag Erlaubnisanalyse Payment Institution, Zag Finanztransfergeschaeft Money Remittance, Zag Kontoinformationsdienst Ais, Zag Negativauskunft Feststellung Bafin: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Zag Erlaubnisanalyse Payment Institution, Zag Finanztransfergeschaeft Money Remittance, Zag Kontoinformationsdienst Ais, Zag Negativauskunft Feststellung Bafin, Zag Zahlungsausloesedienst Pis

## Arbeitsbereich

Dieser Skill bündelt **Zag Erlaubnisanalyse Payment Institution, Zag Finanztransfergeschaeft Money Remittance, Zag Kontoinformationsdienst Ais, Zag Negativauskunft Feststellung Bafin, Zag Zahlungsausloesedienst Pis** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `zag-erlaubnisanalyse-payment-institution` | ZAG-Erlaubnisanalyse für Zahlungsinstitute: Zahlungsdienste katalogisieren, § 10 ZAG, Eigenmittel, Geschäftsplan, Sicherung von Kundengeldern, Geschäftsleiter, Auslagerungen und BaFin-Antrag prüfen. |
| `zag-finanztransfergeschaeft-money-remittance` | Finanztransfergeschäft und Money Remittance nach ZAG prüfen: Weiterleitung von Geldbeträgen ohne Zahlungskonto, Agentenmodelle, Plattformfälle, Bargeld, Ausnahmen und BaFin-Erlaubnisrisiko. |
| `zag-kontoinformationsdienst-ais` | Kontoinformationsdienst nach ZAG und PSD2 prüfen: Registrierung, Datenzugriff, Schnittstelle, Consent, Versicherung, Datenschutz, Open-Banking-Verträge und White-Label-Modelle. |
| `zag-negativauskunft-feststellung-bafin` | ZAG-Negativauskunft oder informelle BaFin-Vorabklärung vorbereiten: Geschäftsmodell neutral beschreiben, Zahlungsfluss visualisieren, Erlaubnistatbestände abgrenzen und gefährliche Formulierungen vermeiden. |
| `zag-zahlungsausloesedienst-pis` | Zahlungsauslösedienst nach ZAG und PSD2 prüfen: Erlaubnis, starke Kundenauthentifizierung, Haftungskette, Interface, technische Dienstleister und Händlerkommunikation. |

## Arbeitsweg

Für **Zag Erlaubnisanalyse Payment Institution, Zag Finanztransfergeschaeft Money Remittance, Zag Kontoinformationsdienst Ais, Zag Negativauskunft Feststellung Bafin, Zag Zahlungsausloesedienst Pis** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `bank-rechtsabteilung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `zag-erlaubnisanalyse-payment-institution`

**Fokus:** ZAG-Erlaubnisanalyse für Zahlungsinstitute: Zahlungsdienste katalogisieren, § 10 ZAG, Eigenmittel, Geschäftsplan, Sicherung von Kundengeldern, Geschäftsleiter, Auslagerungen und BaFin-Antrag prüfen.

# ZAG-Erlaubnisanalyse Zahlungsinstitut

## Worum es geht

Dieser Skill prüft, ob ein Geschäftsmodell der Erlaubnispflicht nach dem ZAG unterliegt, welcher Zahlungsdienst nach § 1 ZAG einschlägig ist und welche Mindestanforderungen für den BaFin-Antrag erfüllt sein müssen. Kapital, Sicherung von Kundengeldern, Geschäftsleiter-Eignung und Auslagerungen werden normseitig verankert. Abgrenzung zu Bankerlaubnis (KWG) und E-Geld-Erlaubnis wird durchgeführt.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 ZAG** – Katalog der Zahlungsdienste Nr. 1–8: Einzahlungs-/Auszahlungsgeschäft, Zahlungsgeschäft (Nr. 3–5), Zahlungsauslösung (Nr. 7), Kontoinformation (Nr. 8); Abgrenzungslinien zu § 1 Abs. 10 ZAG Ausnahmen
- **§ 10 Abs. 1 ZAG** – Erlaubnispflicht für Zahlungsinstitute; schriftlicher Antrag bei BaFin; Inhalt (Geschäftsplan, Sicherungskonzept, IT, Organigramm)
- **§ 11 ZAG** – Versagungsgründe: Nr. 1 Anfangskapital, Nr. 3 Zuverlässigkeit Geschäftsleiter, Nr. 4 fehlender Geschäftsplan, Nr. 5 Hauptverwaltung nicht in Deutschland
- **§ 17 ZAG** – Eigenmittelanforderungen: Anfangskapital nach Dienstart – Zahlungsauslösung (Nr. 7) 50 TEUR, sonstige Zahlungsdienste (Nr. 1–6) 125 TEUR, Finanztransfer (Nr. 6) 20 TEUR; laufende Eigenmittel-Methoden A, B, C
- **§ 16 ZAG** – Sicherung der Kundengelder: Treuhandkonto oder Versicherung/Bürgschaft; Sicherungspflicht ab Entgegennahme
- **§ 12 ZAG** – Geschäftsleiter: mindestens zwei Personen; Zuverlässigkeit, fachliche Eignung analog § 25c KWG; Absichtsanzeige
- **§ 13 ZAG** – Inhaberkontrolle bei qualifizierten Beteiligungen analog § 2c KWG; Schwellen 10/20/30/50 %
- **§ 24 ZAG** – Auslagerung wesentlicher Funktionen: Vorab-Risikoanalyse, Anzeigepflicht, Prüfungs- und Weisungsrechte; BaFin-Merkblatt Auslagerung ZAG

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 ZAG): Welcher Zahlungsdienst Nr. 1–8 liegt vor? Greift eine Ausnahme (§ 1 Abs. 10 ZAG, z.B. Handelsnetz, begrenzte Netze)?
2. **Abgrenzung KWG/ZAG**: Zahlungsdienst + Kreditvergabe aus Eigenmitteln = KWG § 1 Abs. 1 Nr. 2 (Kreditgeschäft); reine Durchleitung = ZAG.
3. **Anfangskapital** (§ 17 ZAG): Dienstart bestimmen, Kapitaluntergrenze ablesen; 20 TEUR (Finanztransfer), 50 TEUR (PIS), 125 TEUR (sonstige).
4. **Sicherungskonzept** (§ 16 ZAG): Treuhandkonto-Nachweis oder Versicherungspolice; Sicherungspflicht ab erstem Kundengeld-Eingang.
5. **Geschäftsleiter-Eignung** (§ 12 ZAG, EBA/GL/2021/06): Mindestens zwei Geschäftsleiter, Zuverlässigkeit, Ressort-Eignung, Zeitbudget.
6. **Inhaberkontrolle** (§ 13 ZAG): Schwellen-Check wie bei KWG; Vorab-Anzeige bei BaFin.
7. **Auslagerungsanzeige** (§ 24 ZAG): Wesentliche Funktionen (IT-Plattform, Compliance, AML) anzeigepflichtig; Vertrag mit Prüfungsrecht.
8. **Antragspaket** (§ 10 ZAG): Geschäftsplan, Eigenmittelnachweis, Sicherungskonzept, IT-Konzept, Inhabernachweis, Geschäftsleiter-Unterlagen.

## Typische Fallkonstellationen

- FinTech baut App für Kontoüberweisungen: § 1 Abs. 1 Satz 2 Nr. 3 ZAG Zahlungsgeschäft, § 10 ZAG Erlaubnisantrag, Anfangskapital 125 TEUR
- Marktplatz-Betreiber mit Zahlungsabwicklung: § 1 Abs. 10 Nr. 14 ZAG begrenztes Netz prüfen; sonst § 10 ZAG Erlaubnis erforderlich
- PIS-Provider (Zahlungsauslösung): § 1 Abs. 1 Satz 2 Nr. 7 ZAG, Anfangskapital 50 TEUR (§ 17 ZAG), Haftpflichtversicherung statt Sicherungskonzept (§ 16 Abs. 3 ZAG)
- Passporting aus EU-Staat: § 38 ZAG-Notifizierung; BaFin-Prüfung ob Hauptverwaltung wirklich im Herkunftsstaat
- ZAG-Institut erweitert um Kreditvergabe: Grenze zu § 1 Abs. 1 Nr. 2 KWG; ggf. KWG-Erlaubnis erforderlich

## Output

Erlaubnisantrags-Checkliste nach § 10 ZAG; Anfangskapital-Tabelle nach Dienstart; Sicherungskonzept-Muster; Eigenmittelberechnung Methode A/B/C; Fit-and-Proper-Unterlagenliste für Geschäftsleiter.

## Quellenregel

gesetze-im-internet.de (ZAG, KWG), bafin.de (Merkblatt Zahlungsinstitute, Erlaubnisantrag-Formular ZAG), eur-lex.europa.eu (PSD2 Richtlinie 2015/2366). Live-Check: BaFin-Merkblatt ZAG-Erlaubnis, PSD3-Entwurf COM(2023)366 (noch nicht in Kraft).

## 2. `zag-finanztransfergeschaeft-money-remittance`

**Fokus:** Finanztransfergeschäft und Money Remittance nach ZAG prüfen: Weiterleitung von Geldbeträgen ohne Zahlungskonto, Agentenmodelle, Plattformfälle, Bargeld, Ausnahmen und BaFin-Erlaubnisrisiko.

# Finanztransfergeschäft / Money Remittance nach ZAG

## Worum es geht

Dieser Skill prüft das Finanztransfergeschäft nach § 1 Abs. 1 Satz 2 Nr. 6 ZAG (Money Remittance): Weiterleitung von Geldbeträgen ohne Eröffnung eines Zahlungskontos. Er deckt Erlaubnisanforderungen, Geldwäscheprävention, FATF-Vorgaben und die Travel-Rule-Pflichten ab. Besonderheiten bei Bargeld, Krypto-Remittance und Agentennetzen werden adressiert.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 Nr. 6 ZAG** – Finanztransfergeschäft: Dienst zur Übermittlung von Geldbeträgen; kein Zahlungskonto erforderlich; Ausführung der Transaktion über das Netz des Anbieters
- **§ 10 ZAG** – Erlaubnispflicht; Anfangskapital nach § 17 ZAG: 20 TEUR (geringstes Anfangskapital aller Zahlungsdienste); Geschäftsplan, Sicherungskonzept, Organigramm
- **§ 17 ZAG** – Anfangskapital 20 TEUR für Finanztransfer; laufende Eigenmittel Methode A, B oder C nach Zahlungsvolumen
- **§ 25 ZAG** – Agenten: Registrierung, Haftung des Hauptinstituts, Schulungspflichten, AML-Einbindung; Eintrag im BaFin-Agenten-Register
- **GwG §§ 3–10** – KYC-Pflichten: Identifizierung ab 15 Euro Bargeldtransaktion (§ 10 Abs. 3 Nr. 2 GwG), vereinfachte Sorgfalt nicht anwendbar beim Finanztransfer
- **GwG § 15** – Verstärkte Sorgfaltspflichten: Hochrisiko-Länder (FATF-Liste), PEP-Kunden, ungewöhnliche Transaktionsmuster; Transaktionsmonitoring
- **FATF Recommendation 16 (Travel Rule)** – Pflicht zur Übermittlung von Auftraggeber- und Empfängerinformationen bei Überweisungen; Umsetzung in EU durch Geldtransfer-VO 2015/847 (ab 2024 MiCA-Erweiterung VO 2023/1113)
- **GwG § 43** – Verdachtsmeldepflicht bei Geldwäscheverdacht; FIU-Meldung; Durchführungsverbot vor FIU-Freigabe

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 Nr. 6 ZAG): Wird Geld weitergeleitet ohne eigenes Zahlungskonto des Empfängers? Bargeld-zu-Bargeld, Bargeld-zu-Konto, Online-Remittance?
2. **Erlaubnisantrag** (§ 10 ZAG): Anfangskapital 20 TEUR; Geschäftsplan mit Volumen-Projektion, Agentenstruktur, AML-Konzept.
3. **KYC-Pflichten** (GwG §§ 3–10): Identifizierung aller Auftraggeber; ab 1000 Euro erhöhte Sorgfalt; bei Bargeld-Einzahlung ab 15 Euro Identifizierungspflicht.
4. **Travel Rule** (Geldtransfer-VO 2015/847): Auftraggeber-Daten (Name, Konto/IBAN oder eindeutige Kennung, Adresse) mit jeder Überweisung übermitteln; Empfängerinstitut prüft Vollständigkeit.
5. **Hochrisiko-Check** (GwG § 15, FATF-Länderliste): Transaktionen in/aus Hochrisikoländern; verstärkte Sorgfalt; ggf. Einzel-Genehmigung GF.
6. **Agentennetz** (§ 25 ZAG): Jeder Agent registrieren; Schulung AML/KYC; Haftung des Instituts sicherstellen; Monitoring der Agentenaktivitäten.
7. **Verdachtsmeldung** (GwG § 43): Transaktionsmonitoring-System; Schwellenwerte und Muster festlegen; FIU-Meldung innerhalb Frist.
8. **Krypto-Remittance**: Ab VO 2023/1113 gilt Travel Rule auch für Kryptowert-Transfers; VASP-Status nach MiCAR prüfen.

## Typische Fallkonstellationen

- Western-Union-Modell (Bargeld-Einzahlung, Auszahlung im Ausland): § 1 Abs. 1 Satz 2 Nr. 6 ZAG, § 10 ZAG Erlaubnis, GwG KYC, Travel Rule
- Online-Remittance-Plattform (Bank-zu-Bank ohne eigenes Konto): § 1 Abs. 1 Satz 2 Nr. 6 ZAG; Abgrenzung zu Zahlungsgeschäft Nr. 3 (Kundenkonto vorhanden = Nr. 3)
- Krypto-Remittance (BTC-Überweisung als Geldwert): MiCAR VASP + VO 2023/1113 Travel Rule; ggf. ZAG-Erlaubnis parallel
- Transaktionen in FATF-gelistetes Land: GwG § 15 verstärkte Sorgfalt; Einzelgenehmigung Geschäftsleitung; Transaktionslimit erwägen
- Agentenausfall mit Kundengeldverlust: § 25 ZAG Institut-Haftung, § 16 ZAG Sicherungspflicht, BaFin-Meldepflicht

## Output

Erlaubnisantrags-Checkliste § 10 ZAG für Money Remittance; KYC-Pflichten-Matrix (Schwellenwerte, Dokumente); Travel-Rule-Compliance-Check; AML-Transaktionsmonitoring-Konzept; Agenten-Überwachungs-Protokoll.

## Quellenregel

gesetze-im-internet.de (ZAG, GwG), eur-lex.europa.eu (Geldtransfer-VO 2015/847, VO 2023/1113 Travel Rule), fatf-gafi.org (Recommendation 16, VASP Guidance 2021), bafin.de (Merkblatt Finanztransfer, AML-Hinweise). Live-Check: VO 2023/1113 gilt ab 30.12.2024; FATF-Länderliste wird laufend aktualisiert.

## 3. `zag-kontoinformationsdienst-ais`

**Fokus:** Kontoinformationsdienst nach ZAG und PSD2 prüfen: Registrierung, Datenzugriff, Schnittstelle, Consent, Versicherung, Datenschutz, Open-Banking-Verträge und White-Label-Modelle.

# Kontoinformationsdienst (AIS) nach ZAG und PSD2

## Worum es geht

Dieser Skill prüft Kontoinformationsdienste (Account Information Services, AIS) nach § 1 Abs. 1 Satz 2 Nr. 8 ZAG und Art. 67 PSD2. AIS-Provider unterliegen einem Light-Registrierungsregime (§ 34 ZAG) statt einer vollständigen Erlaubnis. Datenzugriffsrechte, Consent-Management, Haftungskette und die Anforderungen aus RTS-SCA Art. 36 (dedizierte Schnittstellen) werden normseitig verankert.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 Nr. 8 ZAG** – Definition Kontoinformationsdienst: Online-Dienst zur Bereitstellung konsolidierter Informationen über ein oder mehrere Zahlungskonten; kein Zahlungsvorgang, nur Datenabruf
- **§ 34 ZAG** – Registrierungspflicht (nicht Erlaubnis); erleichtertes Verfahren; Mindestanforderungen: Berufshaftpflichtversicherung oder gleichwertige Garantie
- **§ 50 ZAG** – Zugangsrecht des AIS-Providers zu Kontoinformationen beim kontoführenden Zahlungsdienstleister; Nicht-Diskriminierungsgebot
- **§ 51 ZAG** – Haftungskette: AIS-Provider haftet für Schäden durch unbefugten Datenzugriff oder Datenweitergabe; Nachweis autorisierter Sitzung Voraussetzung
- **§ 46 ZAG i.V.m. RTS-SCA Art. 10** – SCA auch beim AIS-Datenabruf: erstmaliger Zugang und alle 90 Tage erneute SCA (Art. 10 Abs. 2 RTS-SCA VO 2018/389)
- **Art. 67 PSD2** (Richtlinie 2015/2366) – Rechte und Pflichten des AIS-Providers: Zugang nur auf explizite Zustimmung des Nutzers, Verbot der Verwendung für andere Zwecke als Informationsbereitstellung, keine Datenanreicherung ohne Einwilligung
- **RTS-SCA Art. 36** (VO 2018/389) – AIS-spezifische Schnittstellenanforderungen: kontoführender PSP muss AIS denselben Zugang gewähren wie dem Kontoinhaber; Fallback-Mechanismus
- **DSGVO Art. 6 Abs. 1 lit. a** – Rechtsgrundlage Einwilligung für AIS-Datenzugriff; Zweckbindung, Datensparsamkeit; Schnittstelle zu § 25 DSGVO Datenschutz by Design

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 Nr. 8 ZAG): Nur Kontoinfos oder auch Zahlungsauslösung? Kombi-Dienst erfordert PIS-Erlaubnis (§ 10 ZAG) zusätzlich.
2. **Registrierung** (§ 34 ZAG): Berufshaftpflichtversicherung beschaffen (EBA-Mindestdeckung: 0,5 Mio. Euro pro Schaden); Registrierungsantrag BaFin.
3. **Consent-Mechanismus**: Explizite Einwilligung des Nutzers nach Art. 67 Abs. 2 lit. a PSD2; DSGVO-konforme Consent-UI; Scope klar begrenzen.
4. **SCA-Implementierung** (§ 46 ZAG, RTS-SCA Art. 10): 90-Tage-Erneuerungs-SCA; erstmaliger Zugang mit vollständiger SCA.
5. **API-Anforderungen** (RTS-SCA Art. 36, § 50 ZAG): Kontoführer muss Zugang ermöglichen; Qualitätsmessung gem. EBA-Leitlinie EBA/GL/2018/07 (jetzt RTS Art. 32).
6. **Datenschutz-Check** (DSGVO, Bundesdatenschutzgesetz): Zweckbindung (nur Kontoinformation), Speicherbegrenzung, Auskunftsrechte des Nutzers.
7. **Haftung** (§ 51 ZAG): Schadensersatzpflicht bei unbefugtem Zugriff; Nachweis gültiger Sitzung und Nutzer-Consent als Haftungsbefreiung.

## Typische Fallkonstellationen

- PFM-App (Personal Finance Management): § 1 Abs. 1 Satz 2 Nr. 8 ZAG, § 34 Registrierung, DSGVO Consent, 90-Tage-SCA-Erneuerung
- White-Label AIS für Kreditprüfung: § 50 ZAG Datenzugang, DSGVO Art. 22 Profilierungsverbot prüfen, Zweckbindung dokumentieren
- Kontoführer verweigert AIS-Zugang: § 50 ZAG Diskriminierungsverbot, RTS-SCA Art. 36, EBA-Eskalationsverfahren
- AIS-Dienstleister gibt Daten weiter: § 51 ZAG Haftung, DSGVO Art. 83 Abs. 4 Bußgeld bis 10 Mio. Euro
- Kombi AIS+PIS: Erlaubnis § 10 ZAG (PIS) + Registrierung § 34 ZAG (AIS) kombinieren

## Output

Registrierungsantrag-Checkliste § 34 ZAG; Consent-Framework-Template nach PSD2/DSGVO; SCA-Flow-Diagram für 90-Tage-Erneuerung; Haftungsanalyse-Vermerk; Datenschutz-Impact-Assessment Outline.

## Quellenregel

gesetze-im-internet.de (ZAG, BDSG), eur-lex.europa.eu (PSD2 2015/2366, RTS-SCA VO 2018/389), bafin.de (Merkblatt AIS-Registrierung), eba.europa.eu (EBA/GL/2018/07 API-Qualität, Q&A). Live-Check: PSD3-Entwurf COM(2023)366 verschärft Datenzugangsregeln; eba.europa.eu Q&A-Datenbank.

## 4. `zag-negativauskunft-feststellung-bafin`

**Fokus:** ZAG-Negativauskunft oder informelle BaFin-Vorabklärung vorbereiten: Geschäftsmodell neutral beschreiben, Zahlungsfluss visualisieren, Erlaubnistatbestände abgrenzen und gefährliche Formulierungen vermeiden.

# ZAG-Feststellung und Negativauskunft

## Fachkern: ZAG-Feststellung und Negativauskunft
- **Spezialgegenstand:** ZAG-Feststellung und Negativauskunft; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
- **Normen-/Quellenanker:** KWG, ZAG, WpHG, WpIG, MaRisk/BAIT-DORA-Schnittstellen, BGB/AGB, HGB, GwG, BaFin-Praxis, Sanierung/InsO/StaRUG.
- **Entscheidende Weiche:** Bankgeschäft, Erlaubnis, Vorstandsvorlage, Risikoappetit, Kundenschutz, Sicherheiten, Aufsichtskommunikation und externe Kanzleisteuerung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Bearbeite diesen Spezialfall aus Sicht einer Bank-Rechtsabteilung. Das Ergebnis muss intern verwendbar sein: als Legal Note, Vorstandsvorlage, BaFin-Fragenpaket, Produktfreigabe, Vertragscheck, Red-Team-Vermerk oder Umsetzungs-Backlog.

**Wann nutzen:** Die Bank oder ein Partner will vor Launch wissen, ob ZAG-Erlaubnis, Registrierung oder Ausnahme greift.

## Schnellmodus

1. **Eilpunkt erkennen:** Fristen, Anzeigewege, Launch-Termine, Register-/Portal-Einreichung, Aufsichtskontakt, Kundenkommunikation und irreversible Vollzugsschritte zuerst markieren.
2. **Regime sauber trennen:** Geltendes Recht, Verwaltungspraxis, EU-Entwurf/Vorschau und reine Produktidee nicht vermischen. Bei PSD3/PSR oder Roadmap-Themen ausdrücklich als Monitoring oder Gap-Vorschau kennzeichnen.
3. **Tatbestand vor Meinung:** Erst Geschäftsmodell, Zahlungsfluss, Tokenrecht, Organrolle oder Registerfunktion sauber beschreiben, dann rechtlich einordnen.
4. **Quellenhygiene:** Gesetze, BaFin, Bundesbank, EBA, EZB und EUR-Lex bevorzugen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier oder amtlicher Quelle.
5. **Bankrealität:** Nicht nur sagen, ob etwas erlaubt ist. Immer mitliefern: wer entscheidet, welche Unterlagen fehlen, welcher Fachbereich Owner ist und wie die Bank das dokumentiert.

## Intake

Frage nur nach, wenn ohne Antwort ein falscher nächster Schritt droht. Andernfalls mit Annahmen arbeiten und sie sichtbar markieren.

- **Kerninformationen:** Produktbeschreibung, Flow of Funds, Kundengelder, Rollen, Verträge, technische Abläufe, wirtschaftlicher Zweck.
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

Liefer BaFin-taugliche Darstellung, Rechtsfragen, Abgrenzung, Anlagenliste und defensiven Fragenkatalog.

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

## 5. `zag-zahlungsausloesedienst-pis`

**Fokus:** Zahlungsauslösedienst nach ZAG und PSD2 prüfen: Erlaubnis, starke Kundenauthentifizierung, Haftungskette, Interface, technische Dienstleister und Händlerkommunikation.

# Zahlungsauslösedienst (PIS) nach ZAG und PSD2

## Worum es geht

Dieser Skill prüft Zahlungsauslösedienste (Payment Initiation Services, PIS) nach § 1 Abs. 1 Satz 2 Nr. 7 ZAG und Art. 66 PSD2. Er deckt die Erlaubnisanforderungen, die starke Kundenauthentifizierung (SCA), die Haftungskette zwischen PIS-Provider und kontoführender Bank sowie die technischen Schnittstellenanforderungen nach der RTS-SCA (Delegierte VO 2018/389) ab.

## Kernnormen

- **§ 1 Abs. 1 Satz 2 Nr. 7 ZAG** – Definition Zahlungsauslösedienst: Dienst zur Auslösung eines Zahlungsauftrags auf Veranlassung des Zahlungsdienstnutzers vom Zahlungskonto bei einem anderen Zahlungsdienstleister
- **§ 10 ZAG** – Erlaubnispflicht; Anfangskapital für PIS nach § 17 ZAG: 50 TEUR (alternativ Berufshaftpflichtversicherung nach § 16 Abs. 3 ZAG)
- **§ 49 ZAG** – Pflichten und Rechte des kontoführenden Zahlungsdienstleisters gegenüber PIS-Providern: Schnittstellenbereitstellung, Nicht-Diskriminierung, Authentifizierungs-Weiterleitung
- **§ 55 ZAG** – Anmeldepflichten des PIS-Providers; Registrierung im BaFin-Zahlungsinstituts-Register
- **§ 46 ZAG** – Starke Kundenauthentifizierung (SCA): Pflicht zur SCA bei elektronischen Zahlungsvorgängen; Ausnahmen nach RTS-SCA Art. 10–18
- **§ 27 ZAG** – Haftung des PIS-Providers: bei nicht autorisierten Zahlungen Haftung gegenüber kontoführender Bank; Regress bei Verschulden des PIS-Providers
- **Art. 66 PSD2** (Richtlinie 2015/2366) – Rechte des Zahlungsauslösedienstleisters: Zugang zum Zahlungskonto, Informationspflichten, Authentifizierungsweiterleitung, Verbot Speicherung von Zahlungsdaten
- **Delegierte VO 2018/389 (RTS-SCA)** – technische Standards für SCA und sichere Kommunikation: Art. 4 SCA-Elemente, Art. 10–18 SCA-Ausnahmen, Art. 19–32 sichere Kommunikation (API/Fallback-Interface), Art. 33–36 dedizierte Schnittstelle

## Prüfschritte

1. **Dienst-Klassifikation** (§ 1 Abs. 1 Satz 2 Nr. 7 ZAG): Löst der Dienst tatsächlich einen Zahlungsauftrag aus (nicht nur Weiterleitung), vom Konto bei einem Dritten?
2. **Erlaubnis** (§ 10 ZAG): Anfangskapital 50 TEUR oder Berufshaftpflichtversicherung (Deckungssumme nach EBA-Orientierung 0,5 Mio. Euro pro Schaden, 1 Mio. Euro pro Jahr).
3. **SCA-Pflicht** (§ 46 ZAG, RTS-SCA Art. 4): Prüfe ob Ausnahme greift (geringer Betrag Art. 16, vertrauenswürdige Empfänger Art. 13, Unternehmenstransaktionen Art. 17).
4. **Schnittstellenrecht** (§ 49 ZAG, RTS-SCA Art. 30): Kontoführer muss API bereitstellen; Fallback nur wenn dedizierte Schnittstelle nicht verfügbar.
5. **Haftungskette** (§ 27 ZAG): PIS-Provider haftet unmittelbar bei Verschulden; Beweislast: Kontoführer muss Autorisierung nachweisen (§ 675w BGB).
6. **Informationspflichten** (Art. 66 Abs. 3 PSD2): Transaktionsreferenz, Betrag, Empfänger; keine Speicherung von Authentifizierungsdaten.
7. **Registrierung** (§ 55 ZAG): Eintragung im BaFin-Zahlungsinstituts-Register; Passporting in andere EWR-Staaten via § 38 ZAG-Notifizierung.

## Typische Fallkonstellationen

- E-Commerce-Händler integriert PIS-API: § 1 Abs. 1 Satz 2 Nr. 7 ZAG Erlaubnispflicht des PIS-Providers; Händler selbst erlaubnisfrei
- Bank verweigert API-Zugang: § 49 ZAG Diskriminierungsverbot; EBA-Beschwerdeverfahren; RTS-SCA Art. 33 Qualitätsanforderungen
- SCA-Ausnahme für Dauerauftrag: RTS-SCA Art. 14 (wiederkehrende Transaktionen gleicher Betrag/Empfänger); Erstauslösung mit SCA
- Unbefugter Zahlungsvorgang über PIS: § 27 ZAG Haftung PIS; § 675u BGB Erstattungsanspruch Zahler gegen Kontoführer; Regress
- Cross-Border-Betrieb (Deutschland + Frankreich): § 38 ZAG Notifizierung; RTS-SCA einheitlich anwendbar im EWR

## Output

Erlaubnisantrags-Checkliste PIS (50 TEUR oder Versicherung); SCA-Ausnahmen-Matrix mit RTS-SCA-Artikeln; Haftungs-Analyse-Vermerk; API-Anforderungs-Checkliste nach RTS-SCA Art. 30–33; Passporting-Checkliste.

## Quellenregel

gesetze-im-internet.de (ZAG), eur-lex.europa.eu (PSD2 Richtlinie 2015/2366, RTS-SCA VO 2018/389), bafin.de (Merkblatt PIS, FAQ Open Banking), eba.europa.eu (EBA Opinion on SCA-Ausnahmen, Q&A-Datenbank). Live-Check: RTS-SCA läuft unter PSD3/PSR-Reform (Entwurf COM(2023)366); eba.europa.eu für aktuelle Q&A.
