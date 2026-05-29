---
name: aussenwirtschaft-cbam-co2-zoll
description: "Carbon Border Adjustment Mechanism CBAM CO2-Grenzausgleich für Einfuhren aus Drittlaendern. Anwendungsfall Unternehmen importiert CBAM-pflichtige Waren Stahl Aluminium Zement Duenger Strom und muss CBAM-Pflichten erfuellen. Normen EU-CBAM-Verordnung 2023/956 EU-ETS-Richtlinie 2003/87/EG Zollrecht UZK. Prüfraster CBAM-Waren Anmelderstatus Emissionsdaten Standardwerte Drittland-CO2-Preis Zertifikate Register Lieferantendaten Zollschnittstellen. Output CBAM-Prüfprotokoll mit Emissionsberechnung Zertifikatsbedarf und Meldungsplan. Abgrenzung zu aussenwirtschaft-zolltarif-vzta und aussenwirtschaft-vub-einfuhr-ausfuhr."
---

# CBAM und CO2-Grenzausgleich

## Zweck

Dieser Skill strukturiert CBAM-Pflichten seit dem definitiven Zeitraum und trennt harte Daten von Platzhaltern.

## Wann verwenden

- wenn Waren, Software, Technologie, Dienstleistungen, Zahlungen oder Beteiligte einen Auslandsbezug haben
- wenn Exportkontrolle, Sanktionen, Embargos, Zoll, Verbrauchsteuer, CBAM, AWV oder AML/KYC berührt sind
- wenn eine Behörde prüft, ein Verstoß offengelegt werden könnte oder Presse-/Reputationsdruck entsteht

## Arbeitsweise

1. **Sachverhalt einfrieren.** Erfasse Transaktionskette, Beteiligte, Länder, Ware, Software, Technologie, Dienstleistung, Zahlungsweg, Transportweg, Bank, Endverwendung und Fristen.
2. **Datenlücken markieren.** Trenne belegte Tatsachen von Annahmen. Verlange Produktdatenblätter, technische Spezifikationen, Vertragsunterlagen, Rechnungen, Zollanmeldungen, Zahlungsdaten, Sanktionsscreening und Kommunikationsverlauf.
3. **Offizielle Quellen prüfen.** Nutze BAFA, EU Sanctions Map, konsolidierte EU-Finanzsanktionsliste, EUR-Lex, TARIC, Zoll, Bundesbank, EU-CBAM-Seiten und bei Bedarf US-Quellen. Protokolliere URL, Abrufdatum und Aussage.
4. **Verbote vor Genehmigungen.** Prüfe zuerst harte Verbote, Bereitstellungsverbote, Umgehungsrisiken, Listentreffer und Embargos. Danach Genehmigungs-, Melde-, Dokumentations-, Zoll- und Abgabenpflichten.
5. **Sofortmaßnahmen ausgeben.** Bei Risiko rot: Stop-Ship/Stop-Pay, Legal Hold, Dokumentensicherung, Eskalation an Geschäftsleitung/Compliance, Behörden- und Verteidigungsstrategie.
6. **Arbeitsprodukt erstellen.** Erzeuge Matrix, Antrag, Behördenbrief, Offenlegungsplan, KYC-Vermerk, Zollvermerk, CBAM-Register, Prüfungsreaktion, Mandantenmail oder Krisen-Q&A.
7. **Qualitätstor.** Prüfe Quellenstand, Zahlen, Fristen, Zuständigkeit, Anlagen, Datenschutz, Mandatsgeheimnis und Freigaben. Unsichere Punkte bleiben sichtbar.

## Rückfragen, wenn unklar

- Welche Ware, Software, Technologie, Dienstleistung oder Zahlung ist betroffen?
- Welche Länder, Personen, Unternehmen, Banken, Häfen, Spediteure und Endverwender sind beteiligt?
- Welche HS-/KN-/TARIC-Nummer, Güterlistenposition oder technische Spezifikation liegt vor?
- Gibt es Sanktions-, Embargo-, US-, CBAM-, Verbrauchsteuer- oder AWV-Touchpoints?
- Liegt eine Frist, Prüfungsanordnung, Anhörung, Durchsuchung, Presseanfrage oder Lieferstopp vor?

## Ausgabeformat

- Kurzlage mit Ampel und Sofortmaßnahmen
- Quellenprotokoll mit Abrufdatum und offizieller Quelle
- Prüfmatrix mit offenen Datenpunkten, Annahmen und Zuständigkeiten
- behörden- oder mandantenfähiger Entwurf
- Review-Liste für Berufsträger, Compliance, Zoll, Steuer und Geschäftsleitung

## Typische Fehler vermeiden

- Keine Sanktionsentscheidung ohne aktuelle Quellenprüfung und Trefferlog.
- Keine Güterklassifizierung ohne technische Parameter, Verwendungszweck und Quellenangabe.
- Keine Zolltarifnummer ohne TARIC-/EZT-Prüfung und Begründung.
- Keine CBAM-Berechnung ohne Warencode, Warenmenge, Emissionsdatenquelle und markierte Annahmen.
- Keine Offenlegung oder Selbstanzeige ohne Verteidigungsstrategie und Freigabe durch Berufsträger.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.

## Triage vor CBAM-Pruefung

Kläre vor der Pruefung:

1. Handelt es sich um CBAM-Pflichtware — Zement, Aluminium, Duenger, Eisen/Stahl, Strom, Wasserstoff?
2. Wer ist CBAM-Anmelder (zugelassener CBAM-Anmelder ab Definitivphase Pflicht; vorher EU-Importeur oder indirekter Zollvertreter)?
3. Liegt ein Zertifikat einer akkreditierten Pruefstelle für die eingebetteten Emissionen des Drittlandsherstellers vor?
4. Mengenrelevanz: Liegt die Einfuhr über der De-minimis-Schwelle von 50 Tonnen jährlich (ab Definitivphase 2026)?
5. Besteht ein Karbonpreismechanismus im Ursprungsland, der auf CBAM-Abgaben angerechnet werden kann?

## Aktualität CBAM Definitivphase

Stand 05/2026:

- **Definitivphase seit 01.01.2026:** Wer über 50 t/Jahr CBAM-pflichtige Waren einführt, muss Status "zugelassener CBAM-Anmelder" besitzen. Ca. 90 % der Importeure fallen damit aus dem Anwendungsbereich; ca. 99 % der grauen Emissionen werden weiterhin erfasst.
- **Zollanmeldung:** Dokumentcode für Status (unter Schwelle / zugelassen / Antrag gestellt) bei Einfuhrzollanmeldung pflichtig.
- **Zertifikatserwerb** ab 01.02.2027 möglich.
- **Erste verbindliche CBAM-Erklärung:** Abgabe bis 30.09.2027 für alle CBAM-relevanten Einfuhren des Jahres 2026.
- **Sanktionen:** Sanktionsmechanismus für nicht abgegebene/abgegebene Zertifikate bei verspäteter Erklärung — vor Mandantenberatung tagesaktuell über [taxation-customs.ec.europa.eu](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en) und [zoll.de CBAM](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/Schutz-der-Umwelt/CO2-Grenzausgleichssystem-CBAM/co2-grenzausgleichssystem-cbam_node.html) verifizieren.

## Vertiefung: Rechtsprechung und Leitsaetze

Rechtsprechung im Mandat live verifizieren über [curia.europa.eu](https://curia.europa.eu/) — keine Aktenzeichen aus Modellwissen.

- VO (EU) 2023/956 (CBAM-Grundverordnung) — [EUR-Lex 32023R0956](https://eur-lex.europa.eu/eli/reg/2023/956/oj)
- DurchführungsVO (EU) 2023/1773 — CBAM-Übergangszeitraum 2023-2025 — [EUR-Lex 32023R1773](https://eur-lex.europa.eu/eli/reg_impl/2023/1773/oj)
- Folgeakte zur Definitivphase über EUR-Lex und EU-Kommissionsseite tagesaktuell prüfen.

## Normen-Kette CBAM

- VO (EU) 2023/956 — CBAM-Grundverordnung (Produkte, Berichtspflicht, Zertifikate ab 2026)
- Durchfuehrungs-VO (EU) 2023/1773 — Ubergangszeitraum 2023-2025, Berichtsformat
- Art. 14 VO (EU) 2023/956 — Emissionsverifizierung durch akkreditierte Pruefstelle
- § 3 BEHG — Brennstoffemissionshandelsgesetz als nat. Karbonpreis (anrechenbar)
- Art. 30 AEUV, Art. 110 AEUV — Verbot gleichwirkender Abgaben und diskriminierender Besteuerung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: CBAM-Berichtspruefung

**Adressat:** Importeur / Nachhaltigkeitsbeauftragter — **Tonfall:** technisch-klimabezogen, normkonform

```
CBAM-PRUEFUNGSVERMERK
Datum: [DATUM]
Quartal/Jahr: [Q/YYYY]
Importeur (CBAM-Anmelder): [FIRMA]
Bearbeiter: [NAME]

1. CBAM-PFLICHTIGE WAREN IM BERICHTSZEITRAUM
   KN-Nr. | Bezeichnung | Ursprungsland | Menge [t] | Eingebettete Emissionen [tCO2e]
   --------|-------------|--------------|-----------|--------------------------------
   [NR.]   | [BEZ.]      | [LAND]       | [MENGE]   | [EMISSIONEN]

2. EMISSIONSNACHWEIS
   Pruefstelle akkreditiert: [ ] Ja (Bescheinigung anliegend) / [ ] Nein — Standardwert angewendet
   Methode: [ ] Tatsaechliche Emissionen / [ ] Standardwert EU-Kommission

3. KARBONPREIS-ANRECHNUNG
   Karbonpreis im Ursprungsland: [LAND — Preis: EUR/tCO2e]
   Anrechenbar gemaess Art. 9 VO 2023/956: [ ] Ja — Betrag: [EUR] / [ ] Nein

4. BERICHTSSTATUS (UBERGANGSZEITRAUM 2023-2025)
   Bericht eingereicht via CBAM-Meldeportal: [ ] Ja, am [DATUM] / [ ] Ausstehend, Frist: [DATUM]
   Fehler/Korrekturbedarf: [ ] Nein / [ ] Ja: [Beschreibung]

5. NAECHSTE SCHRITTE (AB 2026 VOLLPFLICHT)
   - CBAM-Zertifikate kaufen: geschaetzter Bedarf [ANZAHL] Zertifikate a EUR [PREIS]
   - Akkreditierte Pruefstelle beauftragen bis: [DATUM]
```
