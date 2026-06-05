---
name: aussenwirtschaft-embargo-syrien-endverwendung
description: "Embargo Syrien Endverwendung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Embargo Syrien Endverwendung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Embargo Syrien Endverwendung** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-embargo-syrien` | EU-Syrien-Sanktionsregime nach VO (EU) 36/2012 und laufenden Ergaenzungsverordnungen: Finanzsanktionen gelisteter Personen und Entitaeten, Waffenembargo, Guetersanktionen und Oelembargo. Post-Assad-Lockerungen 2024/2025 beachten. Fallkonstellation: Unternehmen plant Wiederaufbaulieferungen nach Syrien. Output: Syrien-Embargo-Pruefvermerk mit aktuellem Regelungsstand. |
| `aussenwirtschaft-endverwendung-endverwender-euc` | Endverwender-Pruefung und End-Use-Certificate (EUC): Identifizierung des tatsaechlichen Endverwenders, Pruefen des Endverwendungszwecks und Authentizitaet der Endverwendungserklaerung nach BAFA-Anforderungen und VO (EU) 2021/821. Besondere Risiken bei Staatsunternehmen, Forschungseinrichtungen und Zwischenhaendlern. Output: EUC-Pruefprotokoll und Vervollstaendigungsanforderung. |
| `aussenwirtschaft-eori-registrierung-stammdaten` | EORI-Nummer-Registrierung und Stammdatenpflege nach UZK Art. 9: Beantragung beim Hauptzollamt, erforderliche Informationen und Update-Pflichten. Bedeutung der EORI-Nummer in ATLAS und beim AEO-Antrag. Grenzueberschreitende EORI-Anerkennung und Probleme bei UK post-Brexit. Output: EORI-Antragsformular und Stammdaten-Pruefcheckliste. |
| `aussenwirtschaft-erp-stammdaten-kontrollpunkte` | Exportkontroll-Kontrollpunkte in ERP-Systemen (SAP GTS, Oracle GTM): Konfiguration und Qualitaetssicherung exportkontrollrelevanter Stammdaten wie Gueterklassifizierung (ECCN/Dual-Use-Code), Embargo-Blocker, Sanktionslisten-Integration und Dokumentenabruf. Identifiziert typische Konfigurationsfehler. Output: ERP-Stammdaten-Pruefbericht und Korrekturplan. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Embargo Syrien Endverwendung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-embargo-syrien`

**Fokus:** EU-Syrien-Sanktionsregime nach VO (EU) 36/2012 und laufenden Ergaenzungsverordnungen: Finanzsanktionen gelisteter Personen und Entitaeten, Waffenembargo, Guetersanktionen und Oelembargo. Post-Assad-Lockerungen 2024/2025 beachten. Fallkonstellation: Unternehmen plant Wiederaufbaulieferungen nach Syrien. Output: Syrien-Embargo-Pruefvermerk mit aktuellem Regelungsstand.

# Embargo Syrien: Sanktionsregime und Post-Assad-Lockerungen

## Mandantenfall

- Unternehmen plant Baumaterial-Lieferungen fuer Wiederaufbau nach Syrien nach 2024; welche Sanktionen gelten noch?
- Bank erhaelt Auftrag fuer Zahlung an syrisches Bauunternehmen; Listencheck und Sektorsanktionen.
- Exporteur fragt nach aktueller Lage nach Regimewechsel Ende 2024 bezueglich Guetersanktionen.

## Erste Schritte

1. VO (EU) 36/2012 aktuell aufrufen (laufende Anpassungen nach Regime-Sturz 2024/2025).
2. Personensanktionsliste auf Beteiligten screenen; Assad-Entourage und Militaer besonders beachten.
3. Waffenembargo und Ruestungsguterliste pruefen (gilt unabhaengig vom Regime-Wechsel).
4. Guetersanktionen: Oelembargo und sektorale Verbote auf aktuelle Fassung pruefen.
5. Lockerungsausnahmen fuer humanitaere Hilfe und Wiederaufbau eruieren (Art. 25 ff. VO 36/2012).
6. Exportgenehmigung beim BAFA fuer genehmigungspflichtige Gueter beantragen.

## Rechtsrahmen

- **VO (EU) 36/2012 konsolidiert**: EU-Syrien-Sanktionsregime.
- **Delegierte VO und Ergaenzungsverordnungen 2024/2025**: Aktuelle Lockerungen und Anpassungen.
- **Art. 25 ff. VO 36/2012**: Ausnahmen fuer humanitaere Hilfe.
- **AWG § 18**: Strafbarkeit bei Embargo-Verstoss.
- **UZK Art. 56**: Embargogueter in Zollanmeldung.

## Pruef-Raster

- [ ] VO 36/2012 in aktueller Fassung geprueft?
- [ ] Personensanktionsliste aktuell gescreent?
- [ ] Waffenembargo und Ruestungsguterliste geprueft?
- [ ] Oelembargo und sektorale Verbote aktuell?
- [ ] Humanitaere Ausnahmen und Wiederaufbau-Lockerungen geprueft?
- [ ] BAFA-Genehmigung beantragt falls erforderlich?

## Typische Fallstricke

- Regime-Wechsel Ende 2024 fuehrt zu laufenden Lockerungen; keine statische Pruefliste verwenden.
- Assad-nahe Entitaeten bleiben trotz Regime-Sturz auf Sanktionsliste; weiter screenen.
- Waffenembargo gilt unabhaengig vom Regime.
- Humanitaere Ausnahmen sind eng und erfordern Genehmigung.

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

Syrien-Embargo-Pruefvermerk mit aktuellem Regelungsstand, Personensanktions-Screeningprotokoll, Gueterlisten-Pruefung und Genehmigungsantrag-Entwurf.

## Quellen

- [VO (EU) 36/2012 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0036)
- [EU Sanctions Map Syrien](https://www.sanctionsmap.eu/#/main/details/41)
- [BAFA Syrien-Embargo](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 2. `aussenwirtschaft-endverwendung-endverwender-euc`

**Fokus:** Endverwender-Pruefung und End-Use-Certificate (EUC): Identifizierung des tatsaechlichen Endverwenders, Pruefen des Endverwendungszwecks und Authentizitaet der Endverwendungserklaerung nach BAFA-Anforderungen und VO (EU) 2021/821. Besondere Risiken bei Staatsunternehmen, Forschungseinrichtungen und Zwischenhaendlern. Output: EUC-Pruefprotokoll und Vervollstaendigungsanforderung.

# Endverwender-Pruefung und EUC: Authentizitaet und Risikoeinschaetzung

## Mandantenfall

- Exporteur erhalt EUC von unbekannter Firma in Pakistan; Authentizitaet zweifelhaft.
- BAFA fordert Nachweise ueber tatsaechlichen Endverwender; Lieferant hat nur Handelsgesellschaft angegeben.
- Technologie-Transfer an staatliches Forschungsinstitut in sensitivem Land; EUC-Pruefung noetig.

## Erste Schritte

1. EUC-Formular auf Vollstaendigkeit pruefen: Endverwender-Name und -Adresse, Verwendungszweck, Unterschrift und Firmenstempel.
2. Authentizitaetspruefung: Unternehmensregister, Web-Praesenz, Gegencheck mit Handelspartnern.
3. Abgleich der EUC-Angaben mit technischer Spezifikation; plausibel fuer zivilen Verwendungszweck?
4. Red Flags der BAFA-Checkliste abarbeiten: Staatsunternehmen, Ruestungsnaeehe, ungewoehnliche Spezifikation.
5. BAFA-Anfrage an Exporteur oder Nachfrage-Schreiben an Endverwender wenn Luecken.
6. Ergebnis und Entscheidung im Compliance-System dokumentieren.

## Rechtsrahmen

- **Art. 10 Abs. 1 lit. g VO (EU) 2021/821**: EUC als Genehmigungsbestandteil.
- **BAFA-Merkblatt Endverwendung**: Anforderungen an EUC-Inhalt und Authentizitaet.
- **AWG § 9**: Genehmigungsvoraussetzungen inkl. Endverwender-Nachweis.
- **§ 18 AWG**: Strafbarkeit bei Falschangaben zur Endverwendung.
- **Art. 4 Abs. 1 VO (EU) 2021/821**: Catch-All bei Kenntnis militaerischer Endverwendung.

## Pruef-Raster

- [ ] EUC vollstaendig ausgefuellt und unterschrieben?
- [ ] Endverwender-Identitaet verifiziert?
- [ ] Endverwendungszweck plausibel und zivil?
- [ ] Red Flags der BAFA-Checkliste negativ?
- [ ] Dokumentation archiviert und mit Freigabeentscheidung verknuepft?
- [ ] Catch-All-Tatbestand ausgeschlossen?

## Typische Fallstricke

- Zwischenhaendler als angeblicher Endverwender reicht nicht; tatsaechliche Nutzung muss identifizierbar sein.
- Staatlliche Forschungseinrichtungen in Hochrisikolaendern haben oft Dual-Use-Kapazitaeten.
- EUC-Faelschungen durch Lieferanten nehmen zu; Gegenverifizierung ueber unabhaengige Kanaele noetig.
- Nachtraegliche EUC-Einholung nach Lieferung schutzt nicht vor Strafverfolgung.

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

EUC-Pruefprotokoll mit Authentizitaetsnachweis, Red-Flag-Checkliste, Vervollstaendigungs-Anforderungsschreiben und Freigabe-/Sperrprotokoll.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Endverwendung und EUC](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 3. `aussenwirtschaft-eori-registrierung-stammdaten`

**Fokus:** EORI-Nummer-Registrierung und Stammdatenpflege nach UZK Art. 9: Beantragung beim Hauptzollamt, erforderliche Informationen und Update-Pflichten. Bedeutung der EORI-Nummer in ATLAS und beim AEO-Antrag. Grenzueberschreitende EORI-Anerkennung und Probleme bei UK post-Brexit. Output: EORI-Antragsformular und Stammdaten-Pruefcheckliste.

# EORI-Registrierung: Beantragung und Stammdatenpflege

## Mandantenfall

- Neugegründetes Unternehmen moechte erstmalig exportieren; EORI-Nummer beantragen.
- UK-Tochtergesellschaft nach Brexit hat keine EU-EORI; Regelungsalternativen.
- Unternehmen hat Sitzverlegung nicht gemeldet; Zollanmeldungen werden abgelehnt.

## Erste Schritte

1. EORI-Antragsformular beim Hauptzollamt herunterladen und vollstaendig ausfuellen.
2. Erforderliche Belege zusammenstellen: Handelsregisterauszug, Steuernummer, Adresse.
3. Antrag online einreichen (zoll.de Antragsformular oder Zoll-Portal).
4. EORI-Nummer in alle relevanten Systeme (ATLAS, Zollagent, Bankinstrument) eintragen.
5. Stamdaten-Update-Pflicht nach UZK Art. 9 Abs. 3 bei Aenderungen von Anschrift, Rechtsform oder GF.
6. UK-Tochtergesellschaft: Separate UK-EORI bei HMRC beantragen (kein EU-EORI nach Brexit).

## Rechtsrahmen

- **UZK Art. 9**: EORI-Registrierungspflicht fuer Wirtschaftsbeteiligte.
- **UZK-DA Art. 3**: Informationspflichten fuer EORI-Registrierung.
- **UZK-IA Art. 7**: Elektronische Systeme und EORI-Datenbank.
- **§ 10 ZollVG**: Nationale Erweiterung fuer EORI-Verfahren.
- **UZK Art. 5 Nr. 27**: Definition des Wirtschaftsbeteiligten mit EORI-Pflicht.

## Pruef-Raster

- [ ] EORI-Registrierung vollstaendig und aktuell?
- [ ] Stammdaten nach jeder relevanten Aenderung aktualisiert?
- [ ] EORI in ATLAS und Zollsystemen korrekt hinterlegt?
- [ ] UK-Tochtergesellschaft separat mit UK-EORI ausgestattet?
- [ ] Vertretungsbefugnis fuer EORI-Nutzung durch Bevollmaechtigte geregelt?
- [ ] EORI-Nummer in Shipping-Dokumenten korrekt angegeben?

## Typische Fallstricke

- Veraltete Stammdaten fuehren zu Ablehnungen in ATLAS.
- UK-EORI und EU-EORI nach Brexit nicht kompatibel; separate Registrierungen noetig.
- EORI-Delegation an Zollagenten bedarf korrekter Vollmachtserteilung.
- Konzerngesellschaften benoetigen je eine eigene EORI-Nummer.

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

EORI-Antragsformular, Stammdaten-Pruefcheckliste, Update-Protokoll fuer Aenderungen und UK-EORI-Antragshilfe.

## Quellen

- [UZK Art. 9 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de EORI-Registrierung](https://www.zoll.de/DE/Fachthemen/Zoelle/EORI-Nummer/eori-nummer_node.html)
- [ZollVG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zollvg/index.html)

## 4. `aussenwirtschaft-erp-stammdaten-kontrollpunkte`

**Fokus:** Exportkontroll-Kontrollpunkte in ERP-Systemen (SAP GTS, Oracle GTM): Konfiguration und Qualitaetssicherung exportkontrollrelevanter Stammdaten wie Gueterklassifizierung (ECCN/Dual-Use-Code), Embargo-Blocker, Sanktionslisten-Integration und Dokumentenabruf. Identifiziert typische Konfigurationsfehler. Output: ERP-Stammdaten-Pruefbericht und Korrekturplan.

# ERP-Stammdaten fuer Exportkontrolle: Konfiguration und Qualitaetssicherung

## Mandantenfall

- SAP GTS gibt bei Bestellung aus Iran keine Sperrwarnung; Konfigurationsfehler suchen.
- Gueterklassifizierungen in ERP wurden seit 2 Jahren nicht aktualisiert; Dual-Use-Liste geaendert.
- ERP-System hat veraltete Sanktionsliste; Freigabe trotz aktuellem Listentreffer.

## Erste Schritte

1. Bestandsaufnahme aller exportkontrollrelevanten Stammdaten-Felder im ERP.
2. Gueterklassifizierungs-Korrektheit pruefen: ECCN, Dual-Use-Code, ALnr (Aussenwirtschaftslistennummer).
3. Embargo-Lander-Tabelle auf Aktualitaet pruefen.
4. Sanktionslisten-Update-Prozess validieren: Frequenz und Quellenverifizierung.
5. Dokumentenablage fuer EUC, Genehmigungen und Screening-Ergebnisse im ERP konfiguriert?
6. Test-Szenarien fuer bekannte Sperr-Faelle durchfuehren und Ergebnisse protokollieren.

## Rechtsrahmen

- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflicht fuer Exportkontrolldokumentation.
- **BAFA-Merkblatt ICP**: Anforderungen an IT-seitige Kontrollsysteme.
- **AWV § 24**: Aufbewahrungspflichten.
- **§ 14 AWG**: Auskunftspflichten gegenueber Behoerden (BAFA-Audit).
- **GoBD**: Anforderungen an digitale Buchfuehrungs- und Archivsysteme.

## Pruef-Raster

- [ ] Alle Dual-Use-Codes und ECCNs aktuell und korrekt eingetragen?
- [ ] Embargo-Laender-Tabelle tagesaktuel?
- [ ] Sanktionslisten-Update-Frequenz ausreichend (taglich/wochentlich)?
- [ ] Test-Szenarios fuer Sperr-Faelle bestanden?
- [ ] Dokumentenablage fuer EUC und Genehmigungen konfiguriert?
- [ ] Audit-Log fuer alle exportkontrollrelevanten ERP-Aenderungen vorhanden?

## Typische Fallstricke

- Gueterklassifizierungen werden bei neuen Produkten nicht automatisch gepflegt.
- Sanktionslisten-Update abonniert, aber Importfehler nicht erkannt.
- Dual-Use-Codes nach EU-Liste-Revision (jaehrlich) nicht nachgezogen.
- Komplexe Produktkonfigurationen mit Dual-Use-Komponenten nicht als Ganzes klassifiziert.

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

ERP-Stammdaten-Pruefbericht mit Fehleranalyse, Korrekturplan mit Prioritaeten und Zeitplan, Test-Protokoll und Konfigurationsempfehlungen.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA ICP-Merkblatt](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
