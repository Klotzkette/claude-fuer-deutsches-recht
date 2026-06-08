---
name: wpig-zag
description: "Wpig ZAG im Plugin Regulatorisches Recht im Regulatorisches Recht."
---

# Wpig ZAG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: WpHG; EnWG; HeilMWerbG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `wpig-und-zag-pruefung`

**Fokus:** WpIG und ZAG Pruefung: Wertpapierinstitutsgesetz und Zahlungsdiensteaufsichtsgesetz Voraussetzungen für Lizenz, Anwendungsbereich, Schnittstellen zu PSD3-Entwurf, Crypto-Asset-Service-Provider unter MiCAR. Pruefraster für Geschaeftsmodelle und Sandbox-Optionen.

### WpIG und ZAG: Abgrenzung und Erlaubnisraster

## Worum es geht

Dieser Skill prüft die Abgrenzung zwischen WpIG-Erlaubnis, ZAG-Erlaubnis und KWG-Erlaubnis für Geschäftsmodelle an der Schnittstelle von Wertpapierdienstleistung und Zahlungsdienst. Das WpIG setzt die IFD/IFR um und klassifiziert Wertpapierinstitute in Klassen 1, 2 und 3 mit stark unterschiedlichen Eigenmittelanforderungen. Überschneidungen mit ZAG (Zahlungsauslösung, Verwahrstellen) und MiCAR (CASP) werden systematsich erfasst.

## Kernnormen

- **WpIG § 2 Abs. 1** – abschließende Liste der Wertpapierdienstleistungen: Anlagevermittlung, Anlageberatung, Portfolioverwaltung, Eigenhandel, Abschluss- und Emissionsgeschäft; Abgrenzung zu § 1 Abs. 1a KWG Finanzdienstleistungen
- **WpIG § 15** – Erlaubnispflicht für Wertpapierinstitute: Antrag bei BaFin, Geschäftsplan, Angaben zu Inhabern, Geschäftsleitern; Erlaubnis je nach Klasse mit unterschiedlichem Umfang
- **WpIG § 17** – Eigenmittelanforderungen nach IFR-Klasse: Klasse 3 (kleine nicht-verflochtene Institute) mind. 75 TEUR; Klasse 2 mind. 150 TEUR + Kapitalzuschlag nach K-Faktoren IFR Art. 15; Klasse 1 (systemrelevant) = KWG-Institute, CRR anwendbar
- **IFR VO 2019/2033 Art. 9–15** – K-Faktoren-System: AUM (Art. 17), CMH (Art. 18), ASA (Art. 19), COH (Art. 20), DTF (Art. 21), NPR/CMG (Art. 22–23), TCD (Art. 24), ON/OFF Balance-Sheet (Art. 25); laufende Eigenmittelanforderung
- **IFR Art. 43** – Meldepflichten Wertpapierinstitute: vierteljährliche Meldung an BaFin; COREP-Schemata nach EBA-ITS; IFR-Klasse beeinflusst Meldeumfang
- **ZAG § 10** – Erlaubnis Zahlungsinstitut: kommt in Betracht wenn Wertpapierinstitut auch Zahlungsdienste erbringt (z.B. Kontoführung für Kundengelder); ggf. doppelte Erlaubnis oder WpIG-Annex-Erlaubnis
- **WpIG § 35 i.V.m. § 25c KWG** – Fit-and-Proper Geschäftsleiter Wertpapierinstitut: Zuverlässigkeit, Sachkunde analog KWG; Absichtsanzeige bei BaFin; Zeitbudget
- **MiCAR Art. 59–76** (VO 2023/1114) – Crypto-Asset-Service-Provider (CASP): Erlaubnispflicht für CASP-Dienstleistungen (Verwahrung, Handel, Transfer von Kryptowerten); Abgrenzung zu WpIG (E-Wertpapiere nach DLT-VO) und ZAG (E-Geld-Token)

## Prüfschritte

1. **Dienstleistungs-Klassifikation** (WpIG § 2 Abs. 1): Liegt eine WpIG-Wertpapierdienstleistung vor? Oder ZAG-Zahlungsdienst (§ 1 ZAG)? Oder KWG-Bankgeschäft? Überlagerungen dokumentieren.
2. **WpIG-Klassen-Bestimmung** (IFR Art. 9–12): Klasse 1 (KWG-Schwelle), Klasse 2 (Standard), Klasse 3 (small non-interconnected)? Bilanzsumme, AUM, COH, NPR, DTF prüfen.
3. **Eigenmittelberechnung** (WpIG § 17, IFR Art. 15): Mindestkapital je Klasse; K-Faktoren berechnen; Vergleich mit 25 %-Kostenkennzahl (IFR Art. 13).
4. **ZAG-Schnittstelle** (§ 10 ZAG): Erbringt das WpIG-Institut auch Zahlungsdienste (Überweisungen für Kunden, Depotkonto)? Doppel-Erlaubnis oder Ausnahme § 1 Abs. 10 ZAG?
5. **MiCAR-CASP-Prüfung** (MiCAR Art. 59): Werden Kryptowerte verwahrt, gehandelt oder übertragen? CASP-Erlaubnis parallel zu WpIG erforderlich? Abgrenzung E-Wertpapier (DLT-Pilot-VO 2022/858) vs. Kryptowert.
6. **Fit-and-Proper** (WpIG § 35, § 25c KWG, EBA/GL/2021/06): Geschäftsleiter-Eignung analog KWG; Absichtsanzeige BaFin.
7. **Meldepflichten** (IFR Art. 43, EBA-ITS): Quartalsweise COREP; Klasse 2 umfangreichere K-Faktor-Meldung; Klasse 3 vereinfacht.

## Typische Fallkonstellationen

- Neo-Broker (Anlagevermittlung ohne Eigenhandel): WpIG § 2 Abs. 1 Nr. 1, Klasse 3 wenn small, Eigenmittel 75 TEUR; keine ZAG-Erlaubnis wenn Kundengelder bei KWG-Bank gehalten
- Robo-Advisor (Portfolioverwaltung): WpIG § 2 Abs. 1 Nr. 7, Klasse 2, K-Faktor AUM anwendbar; Fit-and-Proper Algorithmus-Governance
- Krypto-Exchange mit Fiat-Zahlungen: MiCAR Art. 59 CASP-Erlaubnis + ggf. ZAG § 10 (Zahlungsauslösung oder Finanztransfer) – doppelte Regulierung
- WpIG expandiert in Kredit (z.B. Wertpapierkredit): § 1 Abs. 1 Nr. 2 KWG Kreditgeschäft; WpIG-Erlaubnis reicht nicht; KWG-Erlaubnis erforderlich
- Sandbox-Option: BaFin-Innovationsbereich-Kontakt; regulatorische Erprobung unter FinDAG § 4a; DLT-Pilot-VO 2022/858 für Marktinfrastrukturen

