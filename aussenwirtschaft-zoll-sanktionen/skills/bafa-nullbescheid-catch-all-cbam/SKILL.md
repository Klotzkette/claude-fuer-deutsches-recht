---
name: bafa-nullbescheid-catch-all-cbam
description: "Bafa Nullbescheid Catch ALL Cbam: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bafa Nullbescheid Catch ALL Cbam

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Bafa Nullbescheid Catch ALL Cbam** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-bafa-nullbescheid-azg` | Nullbescheid und Auskunfts-Zollanmeldung (AZG): Verfahren zur verbindlichen Feststellung der Genehmigungsfreiheit einer Ausfuhr durch BAFA. Einsatz bei Unsicherheit ueber Listenpflichtigkeit oder Catch-All-Relevanz. Fragestellung, Antragsinhalt und Rechtsnatur des Nullbescheids. Abgrenzung zur VZTA. Output: Nullbescheid-Antrag und Verfahrensprotokoll. |
| `aussenwirtschaft-catch-all-pruefung` | Catch-All-Pruefung nach Art. 4 VO (EU) 2021/821: Genehmigungspflicht fuer nicht-gelistete Dual-Use-Gueter bei Kenntnis militaerischer Endverwendung oder WMD-Proliferationsgefahr. Identifikation von Catch-All-Ausloesetatbestaenden (positive Kenntnis, Informationspflicht), Konsequenzen und BAFA-Meldepflicht. Output: Catch-All-Pruefungsvermerk und Eskalationsentscheidung. |
| `aussenwirtschaft-cbam-berichtspflichten-uebergang` | CBAM-Berichtspflichten in der Uebergangsphase (2023-2025) nach VO (EU) 2023/956: Vierteljährliche Berichte fuer Zement, Aluminium, Duenger, Eisen/Stahl, Elektrizitaet und Wasserstoff. Erfassung eingebetteter Emissionen, Verwendung von CBAM-Standardwerten und Fehlerquellen. Output: CBAM-Quartalsbericht mit Emissionsdaten und Quellendokumentation. |
| `aussenwirtschaft-cbam-lieferantendaten-emissionen` | Beschaffung und Validierung von Emissionsdaten bei CBAM-pflichtigen Lieferanten: Anforderungen an Drittland-Produzenten fuer Berechnung eingebetteter direkter und indirekter Emissionen nach VO (EU) 2023/956. Lieferanten-Datenanforderung, Verifizierung durch akkreditierten Prufer und Notfallszenarien (Standardwerte). Output: Lieferanten-Datenanforderungspaket und Emissionsverifikationsprotokoll. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Bafa Nullbescheid Catch ALL Cbam**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-bafa-nullbescheid-azg`

**Fokus:** Nullbescheid und Auskunfts-Zollanmeldung (AZG): Verfahren zur verbindlichen Feststellung der Genehmigungsfreiheit einer Ausfuhr durch BAFA. Einsatz bei Unsicherheit ueber Listenpflichtigkeit oder Catch-All-Relevanz. Fragestellung, Antragsinhalt und Rechtsnatur des Nullbescheids. Abgrenzung zur VZTA. Output: Nullbescheid-Antrag und Verfahrensprotokoll.

# BAFA-Nullbescheid: Verbindliche Feststellung der Genehmigungsfreiheit

## Mandantenfall

- Exporteur ist unsicher ob Maschine mit bestimmten Parametern unter Dual-Use-Gueterliste faellt; Nullbescheid-Option pruefen.
- Unternehmen moechte sichere Dokumentationsbasis vor Export in Dual-Use-Grauzone.
- Zollagent benoetigt Beleg fuer ATLAS, dass Ware nicht genehmigungspflichtig ist.

## Erste Schritte

1. Sachverhalt skizzieren: technische Daten, Gueterlisten-Code (vorlaeuefig), Bestimmungsland, Endverwender.
2. Begruendung aufbereiten, warum Genehmigungsfreiheit vermutet wird (Listenschwellenwerte, Catch-All-Fehlen).
3. Nullbescheid-Antrag an BAFA stellen (formloser Antrag mit vollstaendiger Sachverhaltsdarstellung).
4. BAFA-Entscheidung (Bestaetigungs- oder Genehmigungspflichtigkeitsbescheid) abwarten.
5. Positive Entscheidung (Nullbescheid) archivieren; fuer nachfolgende Ausfuhren als Beleg nutzen.
6. Aenderungen in Warenbeschreibung oder Verwendungszweck koennen Nullbescheid ungueltig machen.

## Rechtsrahmen

- **AWG § 21 Abs. 4**: Auskunfts- und Beratungsfunktion des BAFA.
- **Art. 4 VO (EU) 2021/821**: Catch-All-Tatbestand der Genehmigungspflicht.
- **§ 23 VwVfG**: Verwaltungsverfahren und Antragstellung.
- **§ 9 AWV**: Genehmigungsfreiheitsmerkmale.
- **Zollanmeldung ATLAS**: Genehmigungsfreiheitsvermerk im EXA-Datensatz.

## Pruef-Raster

- [ ] Technische Parameter und Gueterlisten-Vergleich vollstaendig?
- [ ] Catch-All-Indizien geprueft und ausgeschlossen?
- [ ] Antrag mit vollstaendiger Sachverhaltsdarstellung gestellt?
- [ ] Nullbescheid als offizielles Dokument archiviert?
- [ ] Aenderungsmoeglichkeiten (neuer Endverwender, neues Zielland) kommuniziert?
- [ ] Fristen fuer Gueltigkeit des Nullbescheids bekannt?

## Typische Fallstricke

- Nullbescheid gilt nur fuer exakten Sachverhalt; Aenderungen erfordern neuen Antrag.
- Kein Schutz vor Strafverfolgung wenn Antragssteller wesentliche Tatsachen verschwiegen hat.
- Praeprudizielle Wirkung des Nullbescheids nur fuer Antragssteller, nicht allgemein bindend.
- Verwaltungsgericht kann BAFA-Wertung auf Ermessensfehler nachpruefen.

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

Nullbescheid-Antrag mit technischer Dokumentation und Gueterlisten-Argumentation, Verfahrensprotokoll, Archivierungsblatt.

## Quellen

- [BAFA Auskunftsmechanismus](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [VwVfG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwvfg/index.html)

## 2. `aussenwirtschaft-catch-all-pruefung`

**Fokus:** Catch-All-Pruefung nach Art. 4 VO (EU) 2021/821: Genehmigungspflicht fuer nicht-gelistete Dual-Use-Gueter bei Kenntnis militaerischer Endverwendung oder WMD-Proliferationsgefahr. Identifikation von Catch-All-Ausloesetatbestaenden (positive Kenntnis, Informationspflicht), Konsequenzen und BAFA-Meldepflicht. Output: Catch-All-Pruefungsvermerk und Eskalationsentscheidung.

# Catch-All-Pruefung: Genehmigungspflicht fuer nicht-gelistete Gueter

## Mandantenfall

- Maschinenhersteller bekommt Hinweis, dass sein Industriekunde in Iran Gueter fuer Raketenprogramm einsetzt.
- Exporteur empfaengt E-Mail mit ungewoehnlichen Anforderungen nach bestimmten technischen Spezifikationen.
- Bank verweigert Akkreditiv und teilt mit, ein Regierungsbehorde habe Embargobezug signalisiert.

## Erste Schritte

1. Catch-All-Ausloeser bestimmen: positive Kenntnis (Art. 4 Abs. 1 VO 2021/821) oder Information durch BAFA (Art. 4 Abs. 2).
2. Gueter und Technologie beschreiben; auch nicht-gelistete Gueter koennen betroffen sein.
3. Endverwendungszweck und Endverwender ermitteln: militaer, WMD, Raketenprogramm, Embargoland?
4. BAFA unverzueglich informieren falls Anhaltspunkte fuer kontrollpflichtige Endverwendung vorliegen.
5. Lieferstopp (Stop-Ship) anordnen bis BAFA-Klaerung.
6. Interne Dokumentation und Legal Hold fuer alle relevanten Unterlagen.

## Rechtsrahmen

- **Art. 4 VO (EU) 2021/821**: Catch-All-Genehmigungspflicht.
- **Art. 4 Abs. 2 VO (EU) 2021/821**: BAFA-Informationspflicht und Informationswirkung.
- **§ 18 AWG**: Strafbarkeit bei Ausfuhr ohne Genehmigung.
- **§ 9 AWG**: Grundtatbestand des Genehmigungserfordernisses.
- **Anhang I VO (EU) 2021/821**: Ausschuss-Regime und gelistete Gueter (Abgrenzung).

## Pruef-Raster

- [ ] Positive Kenntnis oder BAFA-Hinweis vorhanden?
- [ ] Endverwender und Endverwendung vollstaendig ermittelt?
- [ ] WMD-/Militaer-/Embargoland-Nexus ausgeschlossen oder dokumentiert?
- [ ] BAFA informiert falls Catch-All-Anhaltspunkte bestehen?
- [ ] Stop-Ship-Massnahme bei Catch-All-Risiko ausgeloest?
- [ ] Dokumentation und Legal Hold eingerichtet?

## Typische Fallstricke

- Catch-All greift auch ohne Listenpflichtigkeit; 'keine ECCN' heisst nicht automatisch keine Pflicht.
- Positive Kenntnis reicht aus; keine Notwendigkeit bewussten Vorsatzes fuer Strafbarkeit.
- BAFA-Hinweis per Schreiben oder Telefongespraech kann Genehmigungspflicht ausloesen.
- Unterlassung der BAFA-Meldung bei Verdacht ist eigenstaendiger Straftatbestand.

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

Catch-All-Pruefungsvermerk mit Begruendung, BAFA-Meldungsschreiben falls erforderlich, Stop-Ship-Protokoll und Eskalationsentscheidung.

## Quellen

- [VO (EU) 2021/821 Art. 4 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Catch-All](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 3. `aussenwirtschaft-cbam-berichtspflichten-uebergang`

**Fokus:** CBAM-Berichtspflichten in der Uebergangsphase (2023-2025) nach VO (EU) 2023/956: Vierteljährliche Berichte fuer Zement, Aluminium, Duenger, Eisen/Stahl, Elektrizitaet und Wasserstoff. Erfassung eingebetteter Emissionen, Verwendung von CBAM-Standardwerten und Fehlerquellen. Output: CBAM-Quartalsbericht mit Emissionsdaten und Quellendokumentation.

# CBAM-Uebergangspflichten: Quartalsbericht fuer eingebettete Emissionen

## Mandantenfall

- Stahlimporteur hat erste CBAM-Quartalsmeldung versaeumst; Frage zu Nachmeldemoelichkeit und Bussgeld.
"- Zementhersteller fragt, ob er fuer Importe aus der Tuerkei CBAM-Standardwerte oder Lieferantendaten nutzen muss.
- Haendler importiert Aluminiumprofile aus mehreren Laendern; unterschiedliche Emissionsfaktoren je Ursprungsland.

## Erste Schritte

1. CBAM-pflichtige Waren identifizieren (Anhang I VO 2023/956): Zement, Aluminium, Eisen/Stahl, Duenger, Elektrizitaet, Wasserstoff.
2. KN-Codes je Warenkategorie pruefen.
3. Eingebettete Emissionen ermitteln: Lieferantendaten oder EU-Standardwerte (Durchfuehrungs-VO).
4. Quartalsbericht in CBAM-Transitional-Registry der EU-Kommission einstellen.
5. Fristen: Bericht bis zum Ende des Monats nach Quartalsende.
6. Fehler in vergangenen Berichten durch Nachmeldung korrigieren.

## Rechtsrahmen

- **Art. 35-37 VO (EU) 2023/956**: Berichtspflichten in der Uebergangsphase.
- **VO (EU) 2023/1773**: Durchfuehrungs-VO fuer Uebergangsberichte und Standardwerte.
- **UZK Art. 162**: Pflichten des Einführers.
- **§ 11 ZollVG**: Informationspflichten gegenueber Zollbehoerden.
- **VO (EU) 2023/956 Art. 3**: Definition eingebetteter Emissionen.

## Pruef-Raster

- [ ] Alle CBAM-pflichtigen Waren und KN-Codes identifiziert?
- [ ] Emissionsdaten vom Lieferanten eingeholt oder EU-Standardwert verwendet?
- [ ] Quartalsbericht vollstaendig und fristgerecht?
- [ ] Nachkorrektur vergangener Berichte geprueft?
- [ ] Bussgeldrisiko bei verspaeteter Meldung kalkuliert?
- [ ] Uebergangsregister-Zugang korrekt eingerichtet?

## Typische Fallstricke

- Standardwerte sind hoeher als tatsaechliche Emissionen; Lieferantendaten vermindern CBAM-Pflicht.
- Quartalsberichte koennen nachgebessert werden, aber Fristversaeumnis loest Bussgeld aus.
- CBAM gilt nicht fuer alle Laender gleich; EWR und bestimmte Laender ausgenommen.
- Mischlieferungen erfordern getrennte Emissionsermittlung je Warenart.

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

CBAM-Quartalsbericht mit Emissionsdaten und Quellenangaben, Korrekturprotokoll, Lieferanten-Datenanforderungstemplate.

## Quellen

- [VO (EU) 2023/956 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0956)
- [VO (EU) 2023/1773 Durchfuehrungs-VO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1773)
- [EU-Kommission CBAM-Portal](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
- [Zoll.de CBAM](https://www.zoll.de/DE/Fachthemen/Steuern/Einfuhrumsatzsteuer/cbam/cbam_node.html)

## 4. `aussenwirtschaft-cbam-lieferantendaten-emissionen`

**Fokus:** Beschaffung und Validierung von Emissionsdaten bei CBAM-pflichtigen Lieferanten: Anforderungen an Drittland-Produzenten fuer Berechnung eingebetteter direkter und indirekter Emissionen nach VO (EU) 2023/956. Lieferanten-Datenanforderung, Verifizierung durch akkreditierten Prufer und Notfallszenarien (Standardwerte). Output: Lieferanten-Datenanforderungspaket und Emissionsverifikationsprotokoll.

# CBAM-Lieferantendaten: Emissionsermittlung beim Produzenten

## Mandantenfall

- Importeur muss Lieferanten in Indien zur Emissionsoffenlegung auffordern; wie formulieren?
- Hersteller in der Tuerkei liefert keine vollstaendigen Emissionsdaten; Standardwerte zwingend?
- Mehrere Lieferanten fuer gleiche Ware liefern unterschiedliche Emissionswerte; Pruefmethodologie klaeren.

## Erste Schritte

1. Emissionsdaten-Anforderungsschreiben an Drittland-Produzent auf Basis VO 2023/956 Anhang IV verfassen.
2. Datenformat klaeren: direkte Emissionen (Scope 1) und indirekte (Strom), je Tonne Ware.
3. Verifikation durch akkreditierten Prufer im Drittland oder EU anfordern.
4. Empfangene Daten auf Plausibilitaet gegenueber Branchenstandards pruefen.
5. Standardwerte der EU-Kommission als Fallback vorbereiten und Mehrkosten kalkulieren.
6. Emissionsdaten in CBAM-Bericht und spaeter in CBAM-Erklaerung einarbeiten.

## Rechtsrahmen

- **Anhang IV VO (EU) 2023/956**: Methodik zur Berechnung eingebetteter Emissionen.
- **Art. 10 VO (EU) 2023/956**: Verifizierungspflicht fuer Drittlandsanlagen.
- **VO (EU) 2023/1773 Anhang IX**: Standardwerte bei fehlenden Anlagendaten.
- **ISO 14064**: Internationale Norm fuer Treibhausgasmessungen als Referenz.
- **Art. 35 Abs. 4 VO (EU) 2023/956**: Meldepflichten bei Unklarheit der Emissionsdaten.

## Pruef-Raster

- [ ] Emissionsdaten-Anforderungsschreiben an Lieferanten versendet?
- [ ] Direktemissionen (Scope 1) und Stromemissionen (Scope 2) separat ermittelt?
- [ ] Verifikation durch akkreditierten Prufer angefordert?
- [ ] Plausibilitaetspruefung gegenueber Branchenstandard durchgefuehrt?
- [ ] Standardwerte als Fallback-Szenario berechnet?
- [ ] Emissionsdaten sicher archiviert und versioniert?

## Typische Fallstricke

- Fehlende Scope-2-Emissionen (indirekter Strom) fuehrt zu systematischer Unterbewertung.
- Ohne akkreditierten Prufer werden Lieferantendaten in der Uebergangsphase moeglicherweise nicht anerkannt.
- Standardwerte sind oft signifikant hoeher als reale Emissionen.
- Produktionsprozessaenderungen beim Lieferanten erfordern Datenaktualisierung.

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

Lieferanten-Datenanforderungsschreiben, Emissionsverifikationsprotokoll, Standardwert-Vergleichstabelle und CBAM-Bericht-Datenstruktur.

## Quellen

- [VO (EU) 2023/956 Anhang IV auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R0956)
- [VO (EU) 2023/1773 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1773)
- [EU-Kommission CBAM-Leitlinien](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
