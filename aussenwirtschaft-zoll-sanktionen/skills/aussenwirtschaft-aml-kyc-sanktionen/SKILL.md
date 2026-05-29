---
name: aussenwirtschaft-aml-kyc-sanktionen
description: "Verknuepft GwG-Risikoanalyse KYC Sanktionsscreening und interne Kontrollpflichten im Aussenhandel. Anwendungsfall Exporteur oder Haendler braucht integriertes AML- und Sanktions-Compliance-System für grenzüberschreitende Geschäfte. Normen GwG § 5 Risikoanalyse EU-Sanktionsverordnungen AWG § 34 Aussenwirtschaftsstrafrecht. Prüfraster GwG-Risikoanalyse wirtschaftlich Berechtigte KYC Sanktionsscreening Transaktionsmonitoring Schulungen Kontrollen. Output Integriertes Compliance-Handbuch mit Risikomatrix KYC-Prozess Screening-Protokoll und Schulungsplan. Abgrenzung zu aussenwirtschaft-sanktionen-embargos und geldwäsche-praevention-aml-kyc-Plugin."
---

# AML, KYC und Sanktions-Compliance

## Zweck

Dieser Skill baut ein integriertes Kontrollsystem für internationale Geschäftsmodelle.

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

## Triage vor AML-/KYC-Sanktionspruefung

Kläre vor der Pruefung:

1. Handelt es sich um eine Neukunden-Onboarding-Pruefung, laufende Transaction-Monitoring-Auswertung oder retrospektiven Verdachtsfall?
2. Welche Kundengruppe — juristischen Person mit UBO-Kette, PEP, Korrespondenzbank oder reine Privatkunde?
3. Welche Sanktionslisten wurden bereits gescreent (EU, OFAC, UN, UK OFSI)?
4. Liegt ein Sorgfaltspflichten-Treffer nach § 10 GwG (vereinfacht, standard, verstaerkt) vor?
5. Wurde eine Verdachtsmeldung nach § 43 GwG bereits abgegeben oder ist sie erforderlich?

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette AML/KYC/Sanktionen

- §§ 10-14 GwG — Kundensorgfaltspflichten (KYC), vereinfachte, standard, verstaerkte
- § 43 GwG — Verdachtsmeldepflicht an FIU
- § 56 GwG — Bussgeldtatbestaende GwG, bis 1 Mio EUR
- Art. 5-7 VO (EU) 833/2014 — Bereitstellungsverbot Finanzmittel Russland
- FATF Recommendations 10, 15, 20 — Internationale Standards KYC/AML
- 6. Geldwaesche-Richtlinie (EU) 2018/1673 — Strafbarkeit Geldwaesche

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: AML/KYC-Pruefungsvermerk

**Adressat:** Compliance-Abteilung / Vorstand — **Tonfall:** dokumentationsintensiv, risikoorientiert

```
AML/KYC-PRUEFUNGSVERMERK
Datum: [DATUM]
Kunde/Entitaet: [NAME]  Typ: [Natuerliche Person / Jur. Person]
Risikoklasse (GwG): [ ] Niedrig / [ ] Standard / [ ] Hoch / [ ] Sehr hoch (§ 15 GwG)
Bearbeiter: [NAME]

1. SANKTIONSSCREENING
   Gescreente Listen: EU / OFAC SDN / UN SC / UK OFSI / Sonstige
   Treffer: [ ] Kein Treffer / [ ] Treffer: [BEZEICHNUNG, Liste, Datum]
   Bewertung: [ ] Echttreffer — Blockierung / [ ] False Positive — Freigabe

2. KYC-SORGFALTSSTUFE
   Anwendbare Sorgfaltsstufe: § [10/13/15] GwG — Begruendung: [...]
   UBO identifiziert: [ ] Ja: [NAME, %-Anteil] / [ ] Nein — Abweichung begruendet

3. PEP-CHECK
   PEP-Status: [ ] Kein PEP / [ ] PEP — Position: [...]
   Massnahme: [ ] Verstaerkte Pruefung — Ergebnis: [...]

4. VERDACHTSMELDUNG
   Verdacht nach § 43 GwG: [ ] Nein / [ ] Ja — Gemeldet an FIU am: [DATUM]

5. ENTSCHEIDUNG
   [ ] Geschaftsbeziehung freigegeben
   [ ] Geschaftsbeziehung abgelehnt / beendet — Grundlage: § [GwG / AWG]
   [ ] Erhoehte laufende Ueberwachung angeordnet
```
