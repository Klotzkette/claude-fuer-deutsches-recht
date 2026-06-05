---
name: aussenwirtschaft-ersatzteile-dual-exporteur
description: "Ersatzteile Dual Exporteur: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ersatzteile Dual Exporteur

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Ersatzteile Dual Exporteur** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-ersatzteile-dual-use` | Exportkontrollpruefung fuer Ersatzteile und Komponenten mit Dual-Use-Potenzial nach VO (EU) 2021/821 und AWG: Abgrenzung Ersatzteil vs. vollstaendige Anlage, Klassifizierung nach Anhang I, Catch-All-Risiko bei Bestimmungslaendern mit Proliferationsrisiko, BAFA-Genehmigungspfad. Output: Klassifizierungsvermerk und Lieferentscheidung. |
| `aussenwirtschaft-exporteur-ausfuehrer-anmelder-rollen` | Abgrenzung der Rollen Exporteur, Ausfuehrer und Zollanmelder nach UZK Art. 1 Nr. 19 und DA Art. 1 Nr. 18 sowie AWG: Haftungsverteilung, Vollmachtserteilung an Zollagenten (direkte/indirekte Vertretung), Verantwortung bei Genehmigungspflichten. Output: Rollenmatrix und Vollmachtsvorlage. |
| `aussenwirtschaft-exportkontrolle-dual-use` | Dual-Use-Pruefung fuer Gueter, Software und Technologie nach VO (EU) 2021/821 Anhang I und AWG §§ 8 ff.: Gueterklassifizierung, Genehmigungspflicht, Catch-All nach Art. 4, Technologietransfer, BAFA-Genehmigungsantrag ueber ELAN-K2. Abgrenzung zu Rustungsguetern und Handelssanktionen. Output: Klassifizierungsdossier und Genehmigungspfad. |
| `aussenwirtschaft-f-gase-ozonstoffe` | Ein- und Ausfuhrkontrolle fuer fluorierte Treibhausgase (F-Gase) nach VO (EU) 517/2014 und ozonabbauende Stoffe nach VO (EG) 1005/2009: Quotensystem, F-Gas-Zertifizierungspflicht, Einfuhrgenehmigung beim Umweltbundesamt, TARIC-Sondervorschriften. Output: Einfuhr-Compliance-Pruefbericht und Genehmigungsantrag. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Ersatzteile Dual Exporteur**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-ersatzteile-dual-use`

**Fokus:** Exportkontrollpruefung fuer Ersatzteile und Komponenten mit Dual-Use-Potenzial nach VO (EU) 2021/821 und AWG: Abgrenzung Ersatzteil vs. vollstaendige Anlage, Klassifizierung nach Anhang I, Catch-All-Risiko bei Bestimmungslaendern mit Proliferationsrisiko, BAFA-Genehmigungspfad. Output: Klassifizierungsvermerk und Lieferentscheidung.

# Ersatzteile mit Dual-Use-Risiko: Klassifizierung und Lieferentscheidung

## Mandantenfall

- Maschinenhersteller liefert Pumpendichtungen nach Iran; Lieferkettenkontrolle zeigt Dual-Use-Potenzial.
- Elektronikunternehmen sendet Ersatzplatinen an Vertriebspartner in UAE; Weitergabe an Russland befuerchtet.
- Reparaturauftrag aus Algerien fuer Steuerungskomponente; ML-Listeneinstufung unklar.

## Erste Schritte

1. Technische Spezifikation des Ersatzteils beschaffen und mit Anhang I VO (EU) 2021/821 abgleichen.
2. Bestimmungsland und Endverwender verifizieren; Catch-All nach Art. 4 VO (EU) 2021/821 pruefen.
3. Gesamtanlage und deren Klassifizierung kennen; Ersatzteil-Klassifizierung ggf. davon abhaengig.
4. BAFA-Auskunftsverfahren bei Unklarheit einleiten (Nullbescheid oder Klassifizierungsanfrage).
5. Sanktionslisten-Screening Endverwender und Lieferkette (Re-Export-Risiko UAE/Tuerkei).
6. Entscheidung dokumentieren: Freigabe mit Beleglage oder Genehmigungsantrag.

## Rechtsrahmen

- **Art. 3 VO (EU) 2021/821**: Genehmigungspflicht fuer gelistete Dual-Use-Gueter.
- **Art. 4 VO (EU) 2021/821**: Catch-All-Genehmigungspflicht bei Kenntnislagen.
- **Anhang I VO (EU) 2021/821**: Gueterliste inkl. Ersatzteile und Komponenten.
- **§ 18 AWG**: Strafbarkeit unerlaubter Ausfuhr.
- **AWV § 8 ff.**: Genehmigungsverfahren und Ausnahmen.

## Pruef-Raster

- [ ] Technische Parameter des Ersatzteils vollstaendig bekannt?
- [ ] Abgleich mit allen relevanten Kategorien des Anhangs I VO (EU) 2021/821 erfolgt?
- [ ] Bestimmungsland und Endverwender verifiziert, Catch-All ausgeschlossen?
- [ ] Re-Export-Risiko ueber Drittlaender geprueft?
- [ ] Sanktionslistenscreening aller Beteiligten durchgefuehrt?
- [ ] Entscheidung mit technischer Begruendung dokumentiert?

## Typische Fallstricke

- Ersatzteile koennen hoeherer Kategorie angehoeren als die Anlage selbst.
- Sammellieferungen von Ersatzteilen koennen zusammen eine vollstaendige Anlage darstellen.
- UAE und Tuerkei gelten als Umgehungslaender; Catch-All-Risiko erhoht.
- BAFA-Nullbescheid gilt nur fuer die beschriebene Konfiguration, nicht fuer Varianten.

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

Klassifizierungsvermerk mit technischer Begruendung, Catch-All-Pruefergebnis, Lieferentscheidung und bei Bedarf BAFA-Genehmigungsantrag.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Dual-Use-Ausfuhrkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA ELAN-K2 Antragsportal](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ELAN_K2/elan_k2_node.html)

## 2. `aussenwirtschaft-exporteur-ausfuehrer-anmelder-rollen`

**Fokus:** Abgrenzung der Rollen Exporteur, Ausfuehrer und Zollanmelder nach UZK Art. 1 Nr. 19 und DA Art. 1 Nr. 18 sowie AWG: Haftungsverteilung, Vollmachtserteilung an Zollagenten (direkte/indirekte Vertretung), Verantwortung bei Genehmigungspflichten. Output: Rollenmatrix und Vollmachtsvorlage.

# Exporteur, Ausfuehrer, Anmelder: Rollen und Haftungsverteilung im Aussenhandel

## Mandantenfall

- Spediteur stellt Ausfuhranmeldung in eigenem Namen; Exporteur-Haftung unklar.
- Konzerntochter unterschreibt Genehmigung, Lieferung laeuft ueber Mutter; Zurechnung problematisch.
- Zollagent hat Vollmacht, macht aber Fehler in Anmeldung; wer haftet?

## Erste Schritte

1. Vertragsstruktur analysieren: Wer ist Eigentuemer der Ware beim Ausfuhrmoment?
2. UZK-Definitionen anwenden: Exporteur nach UZK-DA, Ausfuehrer, Zollanmelder trennen.
3. Vollmachtsdokument pruefen: direkte oder indirekte Vertretung; Haftungsfolgen beachten.
4. Genehmigungspflicht dem richtigen Rechtssubjekt zuordnen (Inhaber der Exportgenehmigung).
5. Haftungsverteilung vertraglich regeln (Spediteurvertrag, ICP-Vertrag mit Zollagenten).
6. Rollenmatrix dokumentieren und im ICP hinterlegen.

## Rechtsrahmen

- **UZK Art. 1 Nr. 19, DA Art. 1 Nr. 18**: Definition des Ausfuehrers.
- **UZK Art. 18-19**: Direkte und indirekte Zollvertretung.
- **AWG § 2**: Definition Auslaender, Inlaender und Exporteur.
- **§ 5 AWV**: Pflichten des Ausfuehrers bei Genehmigungen.
- **§ 18 AWG**: Strafbarkeit des Ausfuehrers und Bevollmaechtigten.

## Pruef-Raster

- [ ] Ausfuehrer nach UZK-Definition korrekt bestimmt?
- [ ] Vollmacht fuer Zollanmelder (direkt/indirekt) schriftlich erteilt?
- [ ] Genehmigungsinhaber und Ausfuehrer personenidentisch oder Uebertragung dokumentiert?
- [ ] Haftungsverteilung im Spediteurvertrag geregelt?
- [ ] Bei indirekter Vertretung: Zollagent in voller Haftung?
- [ ] ICP-Rollenmatrix aktuell?

## Typische Fallstricke

- Indirekte Vertretung stellt Zollagenten als Ausfuehrer in die Haftung, wird aber oft nicht erkannt.
- Genehmigung auf falschen Rechtstraeger ausgestellt, Lieferung laeuft ueber anderen.
- Sammelausfuhren erfordern klare Zuordnung jeder Position zu einem Ausfuehrer.
- BAFA-Pruefung fragt nach tatsaechlichem Ausfuehrer, nicht nach Anmelder.

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

Rollenmatrix mit Haftungszuordnung, Vollmachtsvorlage fuer Zollagenten (direkte/indirekte Vertretung), Checkliste fuer ICP-Verankerung.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Zollverfahren Ausfuhr](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren/Ausfuhr/ausfuhr_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 3. `aussenwirtschaft-exportkontrolle-dual-use`

**Fokus:** Dual-Use-Pruefung fuer Gueter, Software und Technologie nach VO (EU) 2021/821 Anhang I und AWG §§ 8 ff.: Gueterklassifizierung, Genehmigungspflicht, Catch-All nach Art. 4, Technologietransfer, BAFA-Genehmigungsantrag ueber ELAN-K2. Abgrenzung zu Rustungsguetern und Handelssanktionen. Output: Klassifizierungsdossier und Genehmigungspfad.

# Dual-Use-Ausfuhrkontrolle: Klassifizierung und Genehmigungspfad

## Mandantenfall

- Maschinenbauunternehmen exportiert CNC-Fraesmaschine nach China; HS-Code liegt in Grauzone der ML-Liste.
- Software-Unternehmen uebertragt Verschluesselungsmodul ueber Cloud-Download an iranischen Kunden.
- Forschungseinrichtung gibt Technologieunterstuetzung an auslaendischen Gastwissenschaftler; Catch-All geprueft?

## Erste Schritte

1. Ware/Software/Technologie technisch vollstaendig beschreiben (Parameter, Spezifikation, Verwendungszweck).
2. Anhang I VO (EU) 2021/821 durchsuchen: alle 10 Kategorien und relevante Eintraege pruefen.
3. KN-Code bestimmen und TARIC-Doppelverwendungshinweise beachten.
4. Catch-All nach Art. 4 VO (EU) 2021/821 pruefen: Bestimmungsland, Endverwender, Kenntnislage.
5. Bei Listentreffer: Allgemeine EU-Genehmigung pruefen, sonst Einzelgenehmigung BAFA via ELAN-K2.
6. Klassifizierungsergebnis und Genehmigungsstatus dokumentieren.

## Rechtsrahmen

- **Art. 3 VO (EU) 2021/821**: Genehmigungspflicht fuer Anhang-I-Gueter.
- **Art. 4 VO (EU) 2021/821**: Catch-All bei WMD-/Militaer-Endverwendung.
- **Anhang I VO (EU) 2021/821**: Dual-Use-Gueterliste (Kategorien 0-9).
- **§ 8 AWV**: Genehmigungsfreie Ausfuhren, Ausnahmen.
- **§ 18 Abs. 1 AWG**: Strafbarkeit bis 5 Jahre bei unerlaubter Ausfuhr.

## Pruef-Raster

- [ ] Alle 10 Kategorien des Anhangs I systematisch durchsucht?
- [ ] Technische Parameter mit Listenschwellenwerten verglichen?
- [ ] KN-Code und TARIC-Hinweise beachtet?
- [ ] Catch-All-Kriterien geprueft (Bestimmungsland, Endverwender, Kenntnislage)?
- [ ] Allgemeine Genehmigung EU001-EU008 anwendbar?
- [ ] Klassifizierung mit technischer Begruendung archiviert?

## Typische Fallstricke

- Reine Beschreibung des Verwendungszwecks ersetzt keine Listenpruefung nach technischen Parametern.
- Catch-All wird haufig unterschaetzt; Red Flags des Endverwenders uebersehen.
- Allgemeine Genehmigungen haben Ausschlusslisten fuer Bestimmungslaender.
- Technologietransfer durch Wissensweitergabe (E-Mail, Schulung) faellt ebenfalls unter Genehmigungspflicht.

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

Klassifizierungsdossier mit Listenpruefung je Kategorie, Catch-All-Ergebnis, Genehmigungspfad (AGG/Einzelgenehmigung) und BAFA-Antragsunterlagen.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Dual-Use](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [TARIC-Datenbank EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## 4. `aussenwirtschaft-f-gase-ozonstoffe`

**Fokus:** Ein- und Ausfuhrkontrolle fuer fluorierte Treibhausgase (F-Gase) nach VO (EU) 517/2014 und ozonabbauende Stoffe nach VO (EG) 1005/2009: Quotensystem, F-Gas-Zertifizierungspflicht, Einfuhrgenehmigung beim Umweltbundesamt, TARIC-Sondervorschriften. Output: Einfuhr-Compliance-Pruefbericht und Genehmigungsantrag.

# F-Gase und Ozonschutzstoffe: Einfuhrkontrolle und Quotenmanagement

## Mandantenfall

- Klimaanlagenimporteur kauft R-410A aus China; F-Gas-Quotenpflicht und Importregistrierung unklar.
- Kaelteanlagen-Wartungsunternehmen verwendet HFKW; Zertifizierungspflicht und Bussgelrisiko geprueft.
- Pharmaunternehmen importiert FCKW-haltigen Inhalator; Ausnahme nach VO 1005/2009?

## Erste Schritte

1. Stoff identifizieren: F-Gas (HFK/HFKW/PFK/SF6) nach Anhang I VO (EU) 517/2014 oder ODS nach VO (EG) 1005/2009.
2. Quotenpflicht pruefen: F-Gas-Quotenregister der EU-Kommission (HFKW-Einfuhrquoten).
3. Importeur-Zertifizierungspflicht und F-Gas-Zertifikat nach VO (EU) 2015/2067 pruefen.
4. TARIC-Massnahmen fuer F-Gas-Einfuhren abrufen.
5. Genehmigungsantrag beim Umweltbundesamt stellen (ODS) oder Quotenzuteilung beantragen.
6. Kuehlmittelprotokoll und Aufzeichnungspflichten sicherstellen.

## Rechtsrahmen

- **VO (EU) 517/2014**: F-Gas-Verordnung, Quotensystem fuer HFK-Importe.
- **VO (EG) 1005/2009**: Ozonschutzverordnung, Verbote und Genehmigungen fuer ODS.
- **§§ 14 ff. ChemOzonSchichtV**: Nationale Umsetzung Ozonschutz.
- **UZK Art. 56**: Verbote und Beschraenkungen bei Einfuhr.
- **§ 69 KrWG**: Bussgeldbewehrung bei Verstoss gegen Einfuhrverbote.

## Pruef-Raster

- [ ] Stoff korrekt nach VO (EU) 517/2014 Anhang I oder VO (EG) 1005/2009 eingeordnet?
- [ ] Quotenzuteilung fuer F-Gas-Importe vorhanden und ausreichend?
- [ ] F-Gas-Zertifizierung des Importeurs aktuell?
- [ ] TARIC-Massnahmen abgerufen und beachtet?
- [ ] Aufzeichnungspflichten (Logbuch, Mengennachweis) erfuellt?
- [ ] Genehmigung Umweltbundesamt fuer ODS vorhanden?

## Typische Fallstricke

- F-Gas-Quoten werden jaehrlich zugeteilt; Ueberschreitung fuehrt zu Beschlagnahme.
- Vorgeladene Klimaanlagen mit F-Gas werden wie Direktimport des Kaeltemittels behandelt.
- Kaelteanlagentechniker ohne F-Gas-Zertifikat machen Unternehmen bussgeldpflichtig.
- Ozonabbauende Stoffe in kleinen Mengen fuer Laboranalysen koennen Sonderausnahmen haben.

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

Einfuhr-Compliance-Pruefbericht mit Quotenstatus, Genehmigungsantrag Umweltbundesamt, Zertifizierungsnachweis-Checkliste und TARIC-Auszug.

## Quellen

- [VO (EU) 517/2014 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0517)
- [VO (EG) 1005/2009 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32009R1005)
- [Umweltbundesamt F-Gase](https://www.umweltbundesamt.de/themen/klima-energie/treibhausgase/f-gase)
- [Zoll.de Verbote und Beschraenkungen](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/verbote-beschraenkungen_node.html)
