---
name: vzta-antrag-warennummer-hs-wto-handelspolitik
description: "Vzta Antrag Warennummer HS WTO Handelspolitik: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vzta Antrag Warennummer HS WTO Handelspolitik

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Vzta Antrag Warennummer HS WTO Handelspolitik** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-vzta-antrag-qualitaetsgate` | Verbindliche Zolltarifauskunft (vZTA) nach UZK Art. 33 ff.: Antragsqualitaet Warenbezeichnung technische Unterlagen Muster und Lieferfrist. Behoerdliche Bindungswirkung und Rechtschutz gegen ablehnenden Bescheid oder abweichende Einreihung. Qualitaetsgate vor Antragsstellung. Output: vZTA-Antragsmappe mit Sachverhaltsbeschreibung und Einreihungsbegruendung. |
| `aussenwirtschaft-warennummer-hs-cn-taric-einreihung` | Wareneinreihung nach Harmonisiertem System (HS) Kombinierter Nomenklatur (KN) und TARIC: Anwendung der Allgemeinen Vorschriften (AV 1-6) ErlBem und Einreihungsverordnungen. Typische Problemfelder wie Sets Teile Zubehoer Konfektionierung und Mischprodukte. Output: Einreihungsvermerk mit Normbegründung und TARIC-Abfrage-Dokumentation. |
| `aussenwirtschaft-wto-handelspolitik` | WTO-Handelspolitik und Schutzmassnahmenrecht als Kontext fuer Importzuschlaege Antidumping und Ausgleichszoelle: GATT Art. VI XIX XX WTO-ADA (Antidumping-Abkommen) SCM-Abkommen und SG-Abkommen. Bedeutung fuer Unternehmen bei EU-Massnahmen und Streitbeilegungsverfahren. Output: WTO-Kontext-Vermerk und handelspolitisches Risikoradar. |
| `aussenwirtschaft-zollpruefung-aussenpruefung` | Zollaußenpruefung nach §§ 196 ff. AO und UZK Art. 48: Vorbereitung auf Pruefungsankuendigung Prueferempfang Dokumentenvorlage und Nacherhebungsrisiko. Unterschied Zollaußenpruefung und BAFA-Pruefung. Typische Pruefungsschwerpunkte Zollwert Praeferenz und Verfahrens-Compliance. Output: Pruefungsvorbereitungs-Checkliste und Risikobewertungsmatrix. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Vzta Antrag Warennummer HS WTO Handelspolitik**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-vzta-antrag-qualitaetsgate`

**Fokus:** Verbindliche Zolltarifauskunft (vZTA) nach UZK Art. 33 ff.: Antragsqualitaet Warenbezeichnung technische Unterlagen Muster und Lieferfrist. Behoerdliche Bindungswirkung und Rechtschutz gegen ablehnenden Bescheid oder abweichende Einreihung. Qualitaetsgate vor Antragsstellung. Output: vZTA-Antragsmappe mit Sachverhaltsbeschreibung und Einreihungsbegruendung.

# vZTA-Antrag: Qualitaetsgate fuer verbindliche Zolltarifauskuenfte

## Mandantenfall

- Importeur moechte vZTA fuer komplexes Elektrobauteil beantragen; Antrag unvollstaendig zurueckgegeben.
- Unternehmen hat vZTA mit falschem HS-Code; abweichende Zollanmeldung und Nacherhebung.
- Exporteur benoetigt vZTA fuer Serienprodukt zur Planungssicherheit; Antrag vorbereiten.

## Erste Schritte

1. Ware vollstaendig technisch beschreiben: Zusammensetzung Funktion Verwendungszweck Herstellungsverfahren.
2. Muster oder Fotos beilegen soweit moeglich und sinnvoll.
3. Warennummer-Vorschlag nach KN/TARIC mit Begruendung (Allgemeine Vorschriften AV 1-6) formulieren.
4. Antragsformular ZOLLV (Formular 0336) vollstaendig ausfuellen.
5. Antrag beim BILDUNGSZENTRUM der Bundesfinanzverwaltung oder Hauptzollamt einreichen.
6. Bindungswirkung pruefen: vZTA gilt EU-weit 3 Jahre; Rechtschutz gegen ablehnenden Bescheid kennen.

## Rechtsrahmen

- **UZK Art. 33-37**: Verbindliche Zolltarifauskuenfte und Bindungswirkung.
- **UZK-DA Art. 19-22**: Verfahren und Anforderungen fuer vZTA-Antrag.
- **Kombinierte Nomenklatur (KN)**: Systematische Einreihungsgrundlage.
- **Allgemeine Vorschriften AV 1-6**: Regeln zur Wareneinreihung.
- **UZK Art. 44**: Rechtsschutz gegen Zollentscheidungen einschliesslich vZTA.

## Pruef-Raster

- [ ] Warenbeschreibung technisch vollstaendig und eindeutig?
- [ ] Muster oder Fotos beigefuegt?
- [ ] Warennummer-Vorschlag mit AV-Begruendung formuliert?
- [ ] Antragsformular vollstaendig ausgefuellt?
- [ ] Einreichungsstelle korrekt identifiziert?
- [ ] Geplante Nutzung der vZTA und Bindungswirkung verstanden?

## Typische Fallstricke

- Unvollstaendige technische Beschreibung fuehrt zur Rueckgabe ohne Bearbeitung.
- vZTA bindet nur fuer die beschriebene Ware; Varianten benoetigen separate vZTA.
- Ruelckgezogene oder widerrufene vZTA ohne Uebergangsfrist problematisch.
- Abweichende Einreihung in vZTA und Zollanmeldung loest Strafzoll-Risiko aus.

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

vZTA-Antragsmappe mit technischer Warenbe schreibung, Einreihungsbegruendung, Muster-Checkliste und Rechtsschutz-Hinweisblatt.

## Quellen

- [UZK Art. 33 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de vZTA](https://www.zoll.de/DE/Fachthemen/Zoelle/Zolltarif/Verbindliche-Zolltarifauskunft/verbindliche-zolltarifauskunft_node.html)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)

## 2. `aussenwirtschaft-warennummer-hs-cn-taric-einreihung`

**Fokus:** Wareneinreihung nach Harmonisiertem System (HS) Kombinierter Nomenklatur (KN) und TARIC: Anwendung der Allgemeinen Vorschriften (AV 1-6) ErlBem und Einreihungsverordnungen. Typische Problemfelder wie Sets Teile Zubehoer Konfektionierung und Mischprodukte. Output: Einreihungsvermerk mit Normbegründung und TARIC-Abfrage-Dokumentation.

# Wareneinreihung HS/KN/TARIC: Allgemeine Vorschriften und Problemfelder

## Mandantenfall

- Importeur meldet Elektromotoren unter falscher KN-Nummer an; Hauptzollamt stellt abweichende Einreihung fest.
- Unternehmen fragt ob Set aus Maschine und Ersatzteilen zusammen eingereiht werden muss.
- Lebensmittel-Exporteur muss TARIC-Code fuer verarbeitetes Produkt bestimmen; mehrere KN-Positionen moeglich.

## Erste Schritte

1. Ware vollstaendig beschreiben: Beschaffenheit Zusammensetzung Funktion und Verwendungszweck.
2. AV 1 anwenden: Einreihung nach Wortlaut der Positionen und Anmerkungen.
3. AV 2 bis 6 schrittweise pruefen: unvollstaendige Waren Sets Gemische spezifischere Bestimmung.
4. EZT-online (Elektronischer Zolltarif) und TARIC-Datenbank konsultieren.
5. Erlaeuterungen zur KN (ErlBem) und Einreihungsverordnungen zum HS-Code pruefen.
6. Einreihungsvermerk erstellen mit Normbegruendung und TARIC-Abfrage-Dokumentation.

## Rechtsrahmen

- **VO (EWG) 2658/87 (KN-VO)**: Kombinierte Nomenklatur als EU-Zolltarif.
- **Allgemeine Vorschriften (AV) 1-6 KN**: Einreihungsregeln.
- **HS-Erlaeuterungen (WCO)**: Internationale Auslegungshilfen zum Harmonisierten System.
- **Einreihungsverordnungen EU**: Verbindliche Einreihungsentscheidungen der Kommission.
- **UZK Art. 56**: Zolltarif und Einreihungspflicht des Anmelders.

## Pruef-Raster

- [ ] Ware vollstaendig und technisch beschrieben?
- [ ] AV 1 bis 6 schrittweise angewendet?
- [ ] EZT-online und TARIC konsultiert?
- [ ] ErlBem und Einreihungsverordnungen geprueft?
- [ ] Einreihungsvermerk mit Normbegruendung erstellt?
- [ ] TARIC-Abfrage mit Datum dokumentiert?

## Typische Fallstricke

- Sets und Garnituren werden oft faelschlicherweise aufgeteilt; AV 3 beachten.
- Teile und Zubehoer haben eigene Positionen; Zuordnung zum Hauptprodukt nicht automatisch.
- Software als integraler Bestandteil einer Maschine aendert Einreihung moeglicherweise.
- Beschriftung und Verpackung koennen Einreihung beeinflussen (AV 5).

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

Einreihungsvermerk mit AV-Begruendung, TARIC-Abfrage-Dokumentation mit Datum, Empfehlung fuer vZTA bei Unsicherheiten und Checkliste fuer Folgesendungen.

## Quellen

- [TARIC-Datenbank EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [Zoll.de EZT-online](https://www.zoll.de/DE/Fachthemen/Zoelle/Zolltarif/EZT-Online/ezt-online_node.html)
- [KN-VO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31987R2658)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)

## 3. `aussenwirtschaft-wto-handelspolitik`

**Fokus:** WTO-Handelspolitik und Schutzmassnahmenrecht als Kontext fuer Importzuschlaege Antidumping und Ausgleichszoelle: GATT Art. VI XIX XX WTO-ADA (Antidumping-Abkommen) SCM-Abkommen und SG-Abkommen. Bedeutung fuer Unternehmen bei EU-Massnahmen und Streitbeilegungsverfahren. Output: WTO-Kontext-Vermerk und handelspolitisches Risikoradar.

# WTO-Handelspolitik: GATT Schutzmassnahmen und EU-Handelsverteidigung

## Mandantenfall

- Importeur fragt nach Rechtmaeßigkeit neuer EU-Antidumping-Massnahme und WTO-Streitbeilegungsoptionen.
- Exporteur in Drittland ist von EU-Ausgleichszoll betroffen; WTO-rechtliche Einwendungen pruefen.
- Unternehmen moechte in EU-Schutzmassnahme-Untersuchung als interessierte Partei auftreten.

## Erste Schritte

1. Massnahme identifizieren: Antidumping Ausgleichszoll oder Schutzmasnahme? EU-Amtsblatt und TARIC pruefen.
2. WTO-Rechtsgrundlage bestimmen: ADA SCM-Abkommen oder SG-Abkommen.
3. Unternehmensbeteiligung: Als Einfulirer Exporteur oder Produzent von der Massnahme betroffen?
4. Verfahrensrechte in EU-Untersuchung: Fragebogen Auskunftspflicht Akteneinsicht Anhoerung.
5. WTO-Streitbeilegung: Nur Staatsebene moeglich; nationales Unternehmen kann nur Regierung um Klage bitten.
6. Risikoradar erstellen: Laufende WTO-Streitverfahren gegen EU und potenzielle Massnahmen.

## Rechtsrahmen

- **GATT Art. VI**: Antidumping und Ausgleichszoelle.
- **GATT Art. XIX**: Schutzmasnahmenklausel (Safeguards).
- **WTO-Antidumping-Abkommen (ADA)**: Verfahrens- und Substanzregeln fuer AD-Massnahmen.
- **VO (EU) 2016/1036 (EU-AD-GVO)**: EU-Antidumpingverfahren.
- **VO (EU) 2015/478 (EU-SG-VO)**: EU-Schutzmasnahmenverfahren.

## Pruef-Raster

- [ ] Massnahmen-Art korrekt identifiziert (AD/AS/SG)?
- [ ] WTO-Rechtsgrundlage geprueft?
- [ ] Unternehmen als interessierte Partei im EU-Verfahren angemeldet?
- [ ] Fragebogen-Antwort fristgerecht und vollstaendig eingereicht?
- [ ] WTO-Streitbeilegungsoptionen auf Regierungsebene bewertet?
- [ ] Handelspolitisches Risikoradar fuer kuenftige Massnahmen erstellt?

## Typische Fallstricke

- Fristen fuer Fragebogen-Einreichung in EU-Verfahren sind kurz; Verpaessung schliesst von Verfahren aus.
- WTO-Streitbeilegung nur durch Staaten; Unternehmen haben keinen direkten Klagezugang.
- Schutzmassnahmen und Antidumping-Zoelle koennen kumulativ auf dieselbe Ware angewendet werden.
- Circumvention-Ermittlungen koennen Massnahmen auf Drittland-Exporteure ausdehnen.

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

WTO-Kontext-Vermerk mit Massnahmen-Analyse, Verfahrensrechte-Checkliste und handelspolitisches Risikoradar fuer laufende und potenzielle Massnahmen.

## Quellen

- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [WTO Antidumping](https://www.wto.org/english/tratop_e/adp_e/adp_e.htm)
- [EU-Kommission Trade Defence](https://trade.ec.europa.eu/access-to-markets/en/trade-defence)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 4. `aussenwirtschaft-zollpruefung-aussenpruefung`

**Fokus:** Zollaußenpruefung nach §§ 196 ff. AO und UZK Art. 48: Vorbereitung auf Pruefungsankuendigung Prueferempfang Dokumentenvorlage und Nacherhebungsrisiko. Unterschied Zollaußenpruefung und BAFA-Pruefung. Typische Pruefungsschwerpunkte Zollwert Praeferenz und Verfahrens-Compliance. Output: Pruefungsvorbereitungs-Checkliste und Risikobewertungsmatrix.

# Zollaußenpruefung: Vorbereitung Prueferempfang und Risikobegrenzung

## Mandantenfall

- Hauptzollamt kuendigt Zollaußenpruefung an; Unternehmen hat 4 Wochen Vorbereitungszeit.
- Pruefung fokussiert auf Zollwert von Konzerntransaktionen; Verrechnungspreisdokumentation bereitstellen.
- Nach Pruefung Nacherhebungsbescheid fuer Zollwert-Unterdeklaration; Einspruch vorbereiten.

## Erste Schritte

1. Pruefungsankuendigung analysieren: Pruefungszeitraum Pruefungsschwerpunkte zustaendige Pruefstelle.
2. Dokumentenarchiv aufbauen: Zollanmeldungen Rechnungen Ursprungsdokumente Genehmigungen.
3. Interne Vorabpruefung: Typische Schwachstellen (Zollwert Praeferenz KN-Einreihung) analysieren.
4. Prueferempfang vorbereiten: Ansprechpartner bestimmen Auskunftspersonen schulen.
5. Nacherhebungsrisiko kalkulieren und Rueckstellungen pruefen.
6. Rechtsberatung einschalten fuer komplexe Sachverhalte und Einspruchsstrategie.

## Rechtsrahmen

- **§§ 196-207 AO**: Außenpruefung als Verfahren.
- **UZK Art. 48**: Zollkontrolle und Nachpruefungsrecht der Zollbehoerden.
- **§ 21 ZollVG**: Auskunftspflichten gegenueber Zollbehoerden.
- **UZK Art. 108**: Zollschuldnacherhebung nach Pruefung.
- **§ 347 AO**: Einspruch gegen Steuerbescheide auch Zollbescheide.

## Pruef-Raster

- [ ] Pruefungsankuendigung vollstaendig analysiert?
- [ ] Dokumentenarchiv fuer Pruefungszeitraum vollstaendig?
- [ ] Interne Vorabpruefung auf Schwachstellen abgeschlossen?
- [ ] Ansprechpartner und Auskunftspersonen bestimmt und geschult?
- [ ] Nacherhebungsrisiko quantifiziert und Rueckstellungen geprueft?
- [ ] Rechtsberatung fuer Einspruchsstrategie eingeschaltet?

## Typische Fallstricke

- Freiwillige Offenlegung von Fehlern vor Pruefungsbeginn wirkt strafmildernd; danach nicht mehr.
- Auskunftspersonen ohne Vorbereitung machen unbedachte Aussagen die Nacherhebungen auslosen.
- Unvollstaendige Dokumentation wird als Verschulden gewertet.
- Pruefungsschwerpunkte koennen sich auf weitere Jahre ausweiten.

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

Pruefungsvorbereitungs-Checkliste mit Dokumentenanforderungen, Risikobewertungsmatrix fuer Pruefungsschwerpunkte und Einspruchs-Strategie-Memo.

## Quellen

- [§ 196 AO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__196.html)
- [UZK Art. 48 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Zollpruefung](https://www.zoll.de/DE/Fachthemen/Zoelle/zoll_node.html)
- [ZollVG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zollvg/index.html)
