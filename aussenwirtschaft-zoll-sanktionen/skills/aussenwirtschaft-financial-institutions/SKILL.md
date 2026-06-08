---
name: aussenwirtschaft-financial-institutions
description: "Sanktions-Compliance für Banken und Finanzinstitute im Korrespondenzbankgeschaeft: Sanktionsscreening von Transaktionen und Gegenparteien nach VO (EU) 2580/2001 und sektorspezifischen Sanktionsverordnungen, SWIFT-Ausschluss-Implikationen, Correspondent-Banking-Due-Diligence. Output: Transaktions-Pruefprotokoll und Risikoklassifizierung im Außenwirtschaft/Zoll/Sanktionen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung."
---

# Korrespondenzbankgeschaeft: Sanktions-Compliance und Transaktionsscreening

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Deutsche Korrespondenzbank erhaelt USD-Zahlung ueber US-Korrespondenten aus Russland; OFAC-Exposure.
- Bank soll Akkreditiv für iranischen Importeur eroeffnen; Gegenpartei nicht in SDN-Liste, aber enge Verbindungen zum Staat.
- Finanzinstitut prueft neue Korrespondenzbankbeziehung mit Tuerkei; Sanktionsumgehungsrisiko Russland.

## Erste Schritte

1. Transaktionsparteien und Zahlungsweg vollstaendig erfassen (Auftraggeber, Beguenstigter, alle Intermediare).
2. Screening gegen konsolidierte EU-Sanktionsliste, OFAC SDN und sektorspezifische Listen.
3. Eigentums- und Kontrollpruefung (50-%-Regel) aller Parteien.
4. Korrespondenzbank-Risikoklassifizierung: CDD-Dokumente, Sanktionsprogramme des Partnerlandes.
5. Bei Risikoindikatoren: Enhanced Due Diligence, Rueckfragen, ggf. Ablehnung.
6. Transaktionsentscheidung mit Quellenprotokoll und Datum dokumentieren.

## Rechtsrahmen

- **VO (EU) 2580/2001**: Terrorismusfinanzierungs-Sanktionen.
- **VO (EU) 833/2014 Art. 5 ff.**: Finanzierungsverbote Russland.
- **VO (EU) 267/2012 Art. 23**: Finanzsanktionen Iran.
- **§§ 3 ff. GwG**: Sorgfaltspflichten bei Verdacht auf Sanktionsverstoesse.
- **§ 18 AWG i.V.m. § 17 AWV**: Bereitstellungsverbot im Zahlungsverkehr.

## Pruef-Raster

- [ ] Alle Transaktionsparteien inkl. Intermediare gescreent?
- [ ] 50-%-Eigentums-/Kontrollregel für alle juristischen Personen geprueft?
- [ ] OFAC-Exposure bei USD-Transaktionen beachtet?
- [ ] Korrespondenzbank-CDD-Dokumentation vollstaendig?
- [ ] Sektorspezifische Verbote (Finanzierung, Anleihen) geprueft?
- [ ] Transaktionsentscheidung mit Datum und Quellenstand protokolliert?

## Typische Fallstricke

- Indirekte Sanktionsexponierung durch Korrespondenzbank-Kette wird unterschaetzt.
- OFAC-Jurisdiktion bei USD-Transaktionen gilt unabhaengig von EU-Sanktionsstatus.
- 50-%-Regel für Eigentum und Kontrolle wird bei komplexen Holdingstrukturen nicht vollstaendig angewendet.
- SWIFT-Ausschluss russischer Banken schliesst nicht alle Transfermoeglichkeiten aus.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [EU-Finanzsanktionsliste FSAP](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [VO (EU) 833/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [BAFA Finanzsanktionen](https://www.bafa.de/DE/Aussenwirtschaft/Finanzsanktionen/finanzsanktionen_node.html)

