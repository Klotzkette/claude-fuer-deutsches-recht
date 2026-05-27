---
name: aussenwirtschaft-zolltarif-vzta
description: "Wareneinreihung TARIC-Massnahmen und verbindliche Zolltarifauskunft VzTA. Anwendungsfall Unternehmen will CN-Code fuer Ware bestimmen oder VzTA-Antrag stellen. Normen UZK Art. 33-37 VzTA Kombinierte Nomenklatur VO 2658/87 Vorabentscheidungsverfahren EuGH. Pruefraster Wareneinreihung Auslegungsregeln TARIC-Massnahmen Zusatzcodes Dokumentencodes VzTA-Antrag. Output Einreihungsdossier mit CN-Code Begruendungskette TARIC-Massnahmen und VzTA-Antragsunterlagen. Abgrenzung zu aussenwirtschaft-exportkontrolle-dual-use und aussenwirtschaft-zollverfahren-bewilligungen."
---

# Zolltarif, TARIC und vZTA

## Zweck

Dieser Skill macht aus Produktbeschreibung, technischen Daten und Verwendungszweck eine zolltarifliche Prüfakte.

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

## Triage vor Zolltarifpruefung

Kläre vor der Tarifierung:

1. Liegt eine technische Beschreibung, ein Datenblatt oder eine Materialanalyse der Ware vor?
2. Gibt es eine bestehende KN-Nummer, eine fruehste Einstufung oder eine auslaendische Tarifauskunft?
3. Soll eine verbindliche Zolltarifauskunft (vZTA) beantragt werden oder handelt es sich um interne Vorabpruefung?
4. Sind Antidumping- oder Ausgleichsmassnahmen fuer die fragliche KN-Position bekannt?
5. Gibt es Abweichungen zwischen EU-KN und HS-Nomenklatur auf 6-Steller-Ebene (WTO-Einheitlichkeit)?

## Vertiefung: Rechtsprechung und Leitsaetze

- EuGH, Urt. v. 06.11.1997 - C-49/96 (Otex/Hauptzollamt Hamburg) — Tarifierung gemischter Waren nach der wesentlichen Beschaffenheit (KN-Allgemeine Vorschrift 3b); das Gepraege einer Ware bestimmt die Einreihung.
- EuGH, Urt. v. 18.05.2017 - C-154/16 (Latvijas Dzelzcels) — Zur Auslegung der KN anhand der Erlauterungen zum HS und der KN-Erlauterungen der Kommission; diese binden die Zollstellen als Interpretationshilfe.
- BFH, Urt. v. 14.11.2006 - VII R 19/05, BFH/NV 2007, 545 — Bindungswirkung und Widerruf von vZTA; Inhaber kann Gultigkeit nach Ablauf von 3 Jahren nicht verlangern — muss neuen Antrag stellen.
- EuGH, Urt. v. 11.01.2007 - C-288/05 (Krupp Hoesch Stahl) — Zum Umfang des Vertrauensschutzes bei Widerruf einer vZTA infolge geaenderter Nomenklaturs-Klassifizierung; Auslauffrist von 6 Monaten ist gemeinschaftsrechtlich geboten.

## Normen-Kette Zolltarif/vZTA

- Art. 33, 34 UZK — Verbindliche Zolltarifauskunft (vZTA), Gueltigkeit 3 Jahre
- Anhang I Verordnung (EWG) 2658/87 — Kombinierte Nomenklatur (KN) mit Allgemeinen Vorschriften
- TARIC-Datenbank (EUR-Lex) — KN-Unterpositionen, Antidumping, Zollaussetzungen
- VO (EU) 952/2013 Art. 56 — Zollsaetze und zolltarifarische Einstufung
- GZT (Gemeinsamer Zolltarif) i.V.m. HS-Erlauterungen (WZO)

## Kommentarliteratur

- Gellert, Zolltarif-Kommentar, Loseblatt — KN-Einreihungspraxis
- Witte, Zollkodex-Kommentar, Art. 33-34 UZK (vZTA)

## Output-Template: Tarifierungsvermerk

**Adressat:** Zollabteilung / Buchhaltung — **Tonfall:** technisch, nomenklatur-prazise

```
TARIFIERUNGSVERMERK
Datum: [DATUM]
Ware: [HANDELSBEZEICHNUNG]
Technische Beschreibung: [KURZBESCHREIBUNG]
Bearbeiter: [NAME]

1. VORGESCHLAGENE EINREIHUNG
   KN-Nr. (8-steller): [NUMMER]
   TARIC-Code (10-steller): [NUMMER]
   Kapitel / Position: [KAP.] / [POS.]
   Begründung: Allgemeine Vorschrift Nr. [1/2/3a/3b/3c/4/5/6]
   Angewandte KN-Erlauterung: [FUNDSTELLE ABl.]

2. ZOLLSATZ
   Drittlandzollsatz: [%]
   Praferenzzollsatz (Abkommen [NAME]): [%]
   Antidumping/Ausgleichszoll: [%] (VO (EU) [NR.])

3. VZTA-STATUS
   Bestehende vZTA: [ ] Nr. [NUMMER] gueltig bis [DATUM] / [ ] Keine
   vZTA-Antrag empfohlen: [ ] Ja / [ ] Nein

4. RISIKEN
   Alternativposition: [KN-NR.] — Risiko: [BESCHREIBUNG]
   Empfehlung: [vZTA / interne Dokumentation / Anwaltliches Opinion Letter]
```
