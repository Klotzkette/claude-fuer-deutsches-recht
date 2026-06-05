---
name: aussenwirtschaft-sanktionsumgehung-red-zoll
description: "Sanktionsumgehung RED Zoll: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sanktionsumgehung RED Zoll

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Sanktionsumgehung RED Zoll** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-sanktionsumgehung-red-flags` | Erkennung und rechtliche Bewertung von Sanktionsumgehungsversuchen nach Art. 12 VO (EU) 833/2014 und BAFA-Red-Flags: ungewoehnliche Handelsrouten, Zwischenhaendler ohne erkennbares Geschaeftsmodell, ungewoehnliche Zahlungswege, bekannte Beschaffungsnetzwerke fuer Russland/Iran. Output: Red-Flags-Checkliste und Risikoprotokoll. |
| `aussenwirtschaft-zoll-straf-bussgeld-selbstkorrektur` | Zollstraf- und Bussgeldsachen sowie freiwillige Selbstkorrektur nach § 22 Abs. 4 AWG und § 22 ZollVG: Straftatbestaende (§ 18 AWG Schmuggeldelikt § 370 AO) Ordnungswidrigkeiten und Wirkung der Selbstanzeige. Strafmilderung durch Kooperation und BAFA-Praxis bei freiwilliger Offenlegung. Output: Strafbarkeits-Risikobewertung und Selbstkorrektur-Strategie. |
| `aussenwirtschaft-zollschuld-entstehung-haftung` | Zollschuldentstehung nach UZK Art. 77-87: Einfuhrzollschuld durch Ueberlassung zum zollrechtlich freien Verkehr und Sondertatbestaende (Art. 79 bei Pflichtversto) Schuldnerkreis und gesamtschuldnerische Haftung. Verjaehrungsfristen Nacherhebungsfristen und Erlaessmoeglichkeiten nach UZK Art. 116 ff. Output: Haftungsanalyse und Erlass-Antrag. |
| `aussenwirtschaft-atlas-einfuhr-abgabenbescheid` | Pruefen und Anfechten von ATLAS-Abgabenbescheiden bei der Einfuhr: Zollwert-Berechnung nach UZK Art. 69-76, Zollsatz-Anwendung und Abgabenberechnung (Zoll, EUSt). Verfahren der Einspruchseinlegung beim Hauptzollamt und Klage beim Finanzgericht. Identifiziert Fehler in Tarifierungsbescheiden und Ursprungsablehnungen. Output: Einspruchsschriftsatz und Berechnung. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Sanktionsumgehung RED Zoll**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-sanktionsumgehung-red-flags`

**Fokus:** Erkennung und rechtliche Bewertung von Sanktionsumgehungsversuchen nach Art. 12 VO (EU) 833/2014 und BAFA-Red-Flags: ungewoehnliche Handelsrouten, Zwischenhaendler ohne erkennbares Geschaeftsmodell, ungewoehnliche Zahlungswege, bekannte Beschaffungsnetzwerke fuer Russland/Iran. Output: Red-Flags-Checkliste und Risikoprotokoll.

# Sanktionsumgehung: Red Flags erkennen und bewerten

## Mandantenfall

- Bestellung von Dual-Use-Elektronik aus UAE in ungewoehnlich grosser Menge; aehnliche Bestellung vor 6 Monaten nach Russland.
- Zahlungseingang ueber kasachischen Finanzintermediaer fuer Lieferung an tuerkisches Unternehmen.
- Handelsvertreter schlaegt ungewoehnliche Lieferoute ueber Armenien vor; Preiszuschlag erklaert.

## Erste Schritte

1. BAFA-Red-Flag-Liste und EU-Kommissions-Guidance zu Art. 12g VO 833/2014 konsultieren.
2. Verdachtsausloeser systematisch durchgehen: Route, Preis, Menge, Zahlungsweg, Endverwender.
3. Lieferlandanalyse: Transitlaender und Umgehungslaender-Risiko (UAE, Tuerkei, Kasachstan, Armenien).
4. Voranfrage an Exporteur oder Zwischenhaendler mit spezifischen Red-Flag-Fragen.
5. Quellenrecherche: Pressedatenbank, BAFA-Bekanntmachungen, US-Denied-Parties.
6. Risikoprotokoll erstellen: Red Flags dokumentiert, Bewertung, Entscheidung.

## Rechtsrahmen

- **Art. 12 VO (EU) 833/2014**: Umgehungsverbot, Bereitstellungsverbot indirekt.
- **Art. 12g VO (EU) 833/2014**: No-Russia-Clause; Sorgfaltspflicht bei Drittlandslieferung.
- **AWG § 18**: Leichtfertigkeit als Strafbarkeitsmassstab.
- **Art. 4 VO (EU) 2021/821**: Catch-All wenn Umgehungsabsicht bekannt.
- **§ 130 OWiG**: Aufsichtspflichtverletzung bei unterlassenem Red-Flag-Screening.**

## Pruef-Raster

- [ ] BAFA-Red-Flags-Liste systematisch durchgegangen?
- [ ] Lieferkette auf Umgehungslaender geprueft?
- [ ] Zahlungsweg auf Auffaelligkeiten analysiert?
- [ ] Menge und Preis auf Abweichungen vom Marktstandard geprueft?
- [ ] Voranfrage an Handelspartner gestellt und dokumentiert?
- [ ] Risikoprotokoll mit Entscheidung archiviert?

## Typische Fallstricke

- Einzelne Red Flags koennen harmlos sein; Gesamtbild ist entscheidend.
- Spaeteres 'Nichtwissen wollen' bei offensichtlichen Red Flags reicht fuer Leichtfertigkeits-Strafbarkeit.
- Zwischenhaendler in Umgehungslaendern muessen nicht bos handelnd sein; aber Sorgfaltsmassnahmen zwingend.
- No-Russia-Clause im Vertrag genuegt nicht; aktives Monitoring der Compliance noetig.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Red-Flags-Checkliste nach BAFA-Standard, Risikoprotokoll, Voranfrage-Schreiben an Handelspartner und Entscheidungsvermerk.

## Quellen

- [BAFA Red-Flags-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [VO (EU) 833/2014 Art. 12g auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [EU-Kommissions-Guidance Umgehung](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/sanctions-policy-and-legal-framework_en)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-zoll-straf-bussgeld-selbstkorrektur`

**Fokus:** Zollstraf- und Bussgeldsachen sowie freiwillige Selbstkorrektur nach § 22 Abs. 4 AWG und § 22 ZollVG: Straftatbestaende (§ 18 AWG Schmuggeldelikt § 370 AO) Ordnungswidrigkeiten und Wirkung der Selbstanzeige. Strafmilderung durch Kooperation und BAFA-Praxis bei freiwilliger Offenlegung. Output: Strafbarkeits-Risikobewertung und Selbstkorrektur-Strategie.

# Zollstrafrecht und Selbstkorrektur: Strafbarkeit Bussgeld und Selbstanzeige

## Mandantenfall

- Unternehmen hat uber Jahre Waren unter falscher KN-Nummer eingereiht; Nachzahlung und Strafbarkeit pruefen.
- BAFA entdeckt bei Pruefung ungenehmigten Export von Dual-Use-Gut; Selbstanzeige erwagen.
- Zollfahndung ermittelt wegen Schmuggel; Verteidigungsstrategie und Schadensbegrenzung.

## Erste Schritte

1. Sachverhalt vollstaendig rekonstruieren: Zeitraum betroffene Waren Verfahren und Beteiligte.
2. Strafbarkeit einordnen: § 18 AWG (vorsaetzlicher Verstoss) oder Ordnungswidrigkeit (§ 19 AWG)?
3. Selbstkorrektur-Option pruefen: § 22 Abs. 4 AWG fuer Exportkontrolle; § 22 ZollVG fuer Zoll.
4. Schadenspotenzial quantifizieren: Zollnacherhebung Zinsen Bussgelder und moegliche Strafbarkeit.
5. Anwalt und ggf. Steuerberater einschalten; Legal Hold einrichten.
6. Selbstkorrektur-Schreiben mit vollstaendiger Offenlegung und Schadensbehebungskonzept vorbereiten.

## Rechtsrahmen

- **§ 18 AWG**: Straftatbestaende im Aussenwirtschaftsrecht (Freiheitsstrafe bis 5 Jahre).
- **§ 19 AWG**: Ordnungswidrigkeitentatbestaende mit Bussgeldbewehrung.
- **§ 22 Abs. 4 AWG**: Strafmildernde Wirkung freiwilliger Offenlegung gegenueber BAFA.
- **§ 370 AO**: Steuerhinterziehung bei Falschdeklaration im Zollrecht.
- **§ 22 ZollVG**: Nacherhebung und Selbstkorrektur-Verfahren.

## Pruef-Raster

- [ ] Strafbarkeit nach § 18 AWG oder Ordnungswidrigkeit nach § 19 AWG eingeordnet?
- [ ] Selbstkorrektur-Option geprueft und Fristen beachtet?
- [ ] Schadenspotenzial vollstaendig quantifiziert?
- [ ] Legal Hold eingerichtet und Dokumentation gesichert?
- [ ] Anwalt mit Selbstkorrektur-Erfahrung eingeschaltet?
- [ ] Offenlegungsschreiben vollstaendig und korrekt vorbereitet?

## Typische Fallstricke

- Selbstkorrektur muss vollstaendig sein; teilweise Offenlegung verschlimmert die Situation.
- Selbstanzeige wirkt nicht strafbefreiend wenn BAFA-Pruefung bereits eingeleitet.
- Keine Selbstkorrektur ohne vorherige rechtliche Beratung; Reihenfolge entscheidend.
- Konzernweite Implikationen: Andere Konzerneinheiten muessen einbezogen werden.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Strafbarkeits-Risikobewertung mit Einordnung AWG/AO, Selbstkorrektur-Strategie mit Zeitplan und Muster-Offenlegungsschreiben fuer BAFA bzw. Hauptzollamt.

## Quellen

- [§ 18 AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__18.html)
- [§ 22 AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__22.html)
- [BAFA Freiwillige Offenlegung](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Allgemeine_Informationen/allgemeine_informationen_node.html)
- [ZollVG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zollvg/index.html)
- [§ 370 AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__370.html)

## 3. `aussenwirtschaft-zollschuld-entstehung-haftung`

**Fokus:** Zollschuldentstehung nach UZK Art. 77-87: Einfuhrzollschuld durch Ueberlassung zum zollrechtlich freien Verkehr und Sondertatbestaende (Art. 79 bei Pflichtversto) Schuldnerkreis und gesamtschuldnerische Haftung. Verjaehrungsfristen Nacherhebungsfristen und Erlaessmoeglichkeiten nach UZK Art. 116 ff. Output: Haftungsanalyse und Erlass-Antrag.

# Zollschuldentstehung und Haftung: Schuldner Nacherhebung und Erlass

## Mandantenfall

- Spediteur wird als Zollschuldner in Anspruch genommen obwohl er nur Vertreter war; Haftungsabgrenzung.
- Unternehmen erhalt Nacherhebungsbescheid fuer 3 Jahre alte Zollanmeldungen; Verjaehrung pruefen.
- Transitverfahren nicht beendet; Zollschuldentstehung nach Art. 79 und Haftungsverteilung.

## Erste Schritte

1. Entstehungstatbestand identifizieren: Art. 77 (ordentliche Zollschuld) oder Art. 79 (Pflichtversto)?
2. Schuldnerkreis bestimmen: Anmelder Zollschuldner kraft Gesetz und Gesamtschuldner.
3. Nacherhebungsfrist pruefen: Art. 103 UZK 3 Jahre; 10 Jahre bei strafrechtlich relevantem Verhalten.
4. Erlass-Option pruefen: Art. 116 ff. UZK bei unabwendbarem Ereignis oder offensichtlichem Versehen.
5. Einspruch gegen Nacherhebungsbescheid vorbereiten: § 347 AO Frist 1 Monat.
6. Haftungsabgrenzung zwischen indirektem Vertreter Auftraggeber und Befoerderer dokumentieren.

## Rechtsrahmen

- **UZK Art. 77-87**: Entstehungstatbestaende und Schuldnerkreis.
- **UZK Art. 79**: Zollschuldentstehung durch Pflichtversto und Haftungskreis.
- **UZK Art. 103**: Nacherhebungsfristen 3 und 10 Jahre.
- **UZK Art. 116-123**: Erlass und Erstattung von Zollschulden.
- **§ 347 AO**: Einspruchsrecht gegen Zollbescheide.

## Pruef-Raster

- [ ] Entstehungstatbestand korrekt eingeordnet (Art. 77 oder Art. 79)?
- [ ] Schuldnerkreis vollstaendig bestimmt?
- [ ] Nacherhebungsfrist nicht verjaehrt?
- [ ] Erlass-Option geprueft?
- [ ] Einspruchsfrist beachtet?
- [ ] Haftungsabgrenzung zwischen allen Beteiligten dokumentiert?

## Typische Fallstricke

- Indirekter Vertreter haftet als Zollschuldner auch wenn Auftraggeber Fehler verursacht hat.
- 10-Jahres-Frist gilt auch ohne Strafurteil wenn strafrechtlich relevantes Verhalten vorlag.
- Erlass nach Art. 116 nur bei unverschuldetem Irrtum; leichte Fahrlassigkeit schadet bereits.
- Gesamtschuldnerische Haftung gilt unbegrenzt; Innenausgleich zwischen Schuldnern separat regeln.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Haftungsanalyse mit Schuldnerkreis-Matrix, Nacherhebungsfristen-Kalkulationsblatt, Erlass-Antragsvorlage und Einspruchs-Strategie-Memo.

## Quellen

- [UZK Art. 77 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Zollschuld](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollschuld/zollschuld_node.html)
- [§ 347 AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__347.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)

## 4. `aussenwirtschaft-atlas-einfuhr-abgabenbescheid`

**Fokus:** Pruefen und Anfechten von ATLAS-Abgabenbescheiden bei der Einfuhr: Zollwert-Berechnung nach UZK Art. 69-76, Zollsatz-Anwendung und Abgabenberechnung (Zoll, EUSt). Verfahren der Einspruchseinlegung beim Hauptzollamt und Klage beim Finanzgericht. Identifiziert Fehler in Tarifierungsbescheiden und Ursprungsablehnungen. Output: Einspruchsschriftsatz und Berechnung.

# ATLAS-Einfuhr-Abgabenbescheid: Pruefen und Anfechten

## Mandantenfall

- Importeur erhaelt Nachzollbescheid ueber abweichenden Zollwert (Lizenzgebuehren nicht einbezogen).
- Zollbescheid wendet Antidumping-Zoll an, obwohl Ursprungszeugnis auf Praeferenzursprung verweist.
- Pharma-Importeur streitet ueber die Einreihung im Zolltarif; Bescheid setzt falschen KN-Code.

## Erste Schritte

1. Abgabenbescheid vollstaendig lesen; Zollwert, KN-Code, angewendeter Zollsatz, Abgabenhoehe protokollieren.
2. Zollwertberechnung nach Transaktionswert (Art. 70 UZK) oder Methoden-Kaskade pruefen.
3. KN-Code gegenueber Warenbeschreibung und allgemeinen Einreihungsvorschriften (AEV) pruefen.
4. Einspruchsfrist beachten (§ 355 AO i.V.m. UZK Art. 44): in der Regel einen Monat nach Bekanntgabe.
5. Einspruchsschriftsatz mit Rechtsanker (KN-AEV, UZK Art. 70 ff.) und Belegen aufbereiten.
6. Gerichtliche Klage beim Finanzgericht vorbereiten falls Einspruch erfolglos.

## Rechtsrahmen

- **UZK Art. 69-76**: Zollwertmethoden (Transaktionswert, identische Waren, Schlusswert).
- **UZK Art. 44**: Einspruchsrecht des Zollschuldners.
- **§ 355 AO**: Einspruchsfrist (1 Monat).
- **KN-Systematik/AEV**: Allgemeine Einreihungsvorschriften 1-6.
- **FGO §§ 40-68**: Finanzgerichtliche Klage bei Zollbescheiden.

## Pruef-Raster

- [ ] Zollwert-Methode korrekt angewendet (Transaktionswert primae facie)?
- [ ] KN-Code stimmt mit Warenbeschreibung und AEV ueberein?
- [ ] Einspruchsfrist noch nicht abgelaufen?
- [ ] Alle wertrelevanten Hinzurechnungen (Art. 71 UZK) korrekt beruecksichtigt?
- [ ] Praeferenzstatus und Ursprung korrekt und belegt?
- [ ] Antidumping-Massnahmen-Anwendung korrekt fuer konkreten Hersteller?

## Typische Fallstricke

- Lizenzgebuehren und Preisnachlaesse nach Verkauf koennen Zollwert aendern.
- 1-Monats-Frist fuer Einspruch laeuft auch waehrend Betriebsurlaub; keine automatische Fristverlaehngerung.
- Praeferenz-Ursprungszeugnis zu spaet beigebracht: Nachpruefungsverfahren verzoeggert Erstattung.
- Finanzgericht akzeptiert nur Schriftsaetze mit vollstaendiger Beleg-Anlage.

## Arbeitsweise

Dieser Skill fuehrt strukturiert durch den Sachverhalt. Beginn mit Tatsachenerhebung:
Beteiligte (Exporteur Importeur Spediteur Zwischenhaendler Bank Endverwender), betroffene Waren
(mit HS-/KN-/TARIC-Code und Dual-Use-Klassifizierung), Laender und Routen, Vertragslage,
behordliche Vorgeschichte und Fristen. Danach Rechtsrahmen abschichten: harte Verbote zuerst,
dann Genehmigungspflichten, Meldeobliegenheiten und Dokumentationsanforderungen.
Sofortmassnahmen benennen (Stop-Ship, Legal Hold, Eskalation) bevor Genehmigungsantrag
oder Offenlegungsstrategie erarbeitet wird. Jede Entscheidung mit Quellenstand und Datum
protokollieren. Offene Punkte bleiben sichtbar und werden nicht als Freigabe getarnt.
Keine Listenlage aus Modellwissen behaupten. Nur amtliche oder frei zugaengliche Quellen
(EUR-Lex, gesetze-im-internet.de, bafa.de, zoll.de) zitieren; Abrufdatum festhalten.

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
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung fuer Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Output

Einspruchsschriftsatz mit Rechtsanker und Berechnung, Gegenuberstellung Behordenbescheid vs. eigene Kalkulation, Anlage-Uebersicht fuer Finanzgericht.

## Quellen

- [UZK Art. 69-76 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/index.html)
- [FGO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/fgo/index.html)
- [Zoll.de Rechtsbehelfe](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Rechtsbehelfe/rechtsbehelfe_node.html)
