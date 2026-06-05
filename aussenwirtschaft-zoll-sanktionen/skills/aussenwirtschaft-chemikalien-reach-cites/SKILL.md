---
name: aussenwirtschaft-chemikalien-reach-cites
description: "Chemikalien Reach Cites: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Chemikalien Reach Cites

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Chemikalien Reach Cites** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-chemikalien-reach-pic` | REACH-Konformitaet und PIC-Verfahren (Prior Informed Consent) bei Im- und Export von gefaehrlichen Chemikalien: VO (EG) 1907/2006 REACH und VO (EU) 649/2012. Registrierung, Auskunftspflichten und Verbote fuer nicht-EU-Exporte. Ansprechpartner ECHA und Hauptzollamt. Output: REACH/PIC-Compliance-Checkliste und Behordenschreiben. |
| `aussenwirtschaft-cites-artenschutz` | Artenschutz-Pflichten bei Im- und Export von CITES-geschuetzten Tieren und Pflanzen: VO (EG) 338/97 und CITES-Uebereinkommen. CITES-Genehmigungsverfahren Anhang A-D, zustaendige Behoerden (BfN, Zoll), Ausnahmen und Bescheinigungen. Fallkonstellation: Kunsthaendler importiert Elfenbein-Antiken. Output: CITES-Genehmigungspaket und Artenschutzbescheinigung. |
| `aussenwirtschaft-dual-use-forschung-hochschule` | Exportkontrolle im Hochschul- und Forschungskontext: Dual-Use-Pruefung fuer akademischen Wissenstransfer, Publikationen, Konferenzbetraege, Forschungskooperationen und Software nach VO (EU) 2021/821 und AWG. Ausnahmen fuer Grundlagenforschung und oeffentlich zugaengliches Wissen. Besondere Risiken bei technischer Ausbildung auslaendischer Studierender. Output: Pruefvermerk fuer Forschungsvorhaben. |
| `aussenwirtschaft-embargo-belarus` | EU-Belarus-Sanktionsregime nach VO (EU) 765/2006 und VO (EU) 2022/576 (Russland-Belarus-Gueterembargoerweiterung): gelistete Personen und Unternehmen, Guetersanktionen, Dienstleistungsverbote und Exportbeschraenkungen. Besondere Risiken: Umgehung von Russland-Embargo ueber Belarus. Pruefung von Handelsbeziehungen mit belarussischen Parteien. Output: Embargo-Pruefungsvermerk und Screeningprotokoll. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Chemikalien Reach Cites**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-chemikalien-reach-pic`

**Fokus:** REACH-Konformitaet und PIC-Verfahren (Prior Informed Consent) bei Im- und Export von gefaehrlichen Chemikalien: VO (EG) 1907/2006 REACH und VO (EU) 649/2012. Registrierung, Auskunftspflichten und Verbote fuer nicht-EU-Exporte. Ansprechpartner ECHA und Hauptzollamt. Output: REACH/PIC-Compliance-Checkliste und Behordenschreiben.

# REACH und PIC: Chemikalien-Compliance im Aussenhandel

## Mandantenfall

- Chemie-Exporteur moechte bestimmte Pflanzenschutzmittel in Drittlaender ausliefern; PIC-Meldung klaeren.
- Importeur von Industriechemikalien fragt nach REACH-Registrierungspflicht fuer den EU-Markt.
- Lagerhalter erhaelt Zollruecklage wegen fehlender Sicherheitsdatenblatt-Dokumentation.

## Erste Schritte

1. Stoff identifizieren: REACH-Registrierung geprueft (ECHA-Datenbank) und SDS vorliegt?
2. PIC-Pflicht nach VO 649/2012 pruefen: Stoff in Anhang I (verbotene Stoffe) oder Anhang V?
3. Vorab-Benachrichtigungsverfahren (DNS) bei ECHA einleiten falls PIC-pflichtig.
4. Import: Registrierung und Sicherheitsdatenblatt-Pflicht bei Importen ueber 1 Tonne.
5. Export: Exportbenachrichtigung an ECHA und Einwilligung des Importlandes einholen.
6. ECHA-Dokumentation archivieren; Zollabfertigung mit PIC-Konformitaetsnachweis unterstuetzen.

## Rechtsrahmen

- **VO (EG) 1907/2006 (REACH)**: Registrierung, Bewertung, Zulassung und Beschraenkung.
- **VO (EU) 649/2012 (PIC)**: Verfahren der vorherigen Zustimmung bei bestimmten Chemikalien.
- **Art. 56-67 VO 1907/2006**: Zulassungspflicht und Export-Einschraenkungen.
- **CLP-VO (EG) 1272/2008**: Einstufung, Kennzeichnung, Verpackung.
- **§ 6 ChemVerbotsV**: Nationale Chemikalienverbote.

## Pruef-Raster

- [ ] Stoff in ECHA-REACH-Datenbank registriert?
- [ ] PIC-Anhang I oder V-Listencheck durchgefuehrt?
- [ ] Sicherheitsdatenblatt (SDS) aktuell und korrekt?
- [ ] Exportbenachrichtigung an ECHA durchgefuehrt?
- [ ] Einwilligung des Importlandes nachgewiesen?
- [ ] Zolldokumentation mit PIC-Konformitaetsnachweis vollstaendig?

## Typische Fallstricke

- PIC-Verfahren dauert Monate; Liefertermine muessen eingeplant werden.
- Fehlende SDS-Dokumentation fuehrt zu Zollruecklage; nicht nachreichbar ohne Neulieferung.
- REACH-Registrierung verfaellt bei Jahres-Mengenunterschreitung.
- Weiterverkauf registrierter Stoffe in EU erfordert eigene Downstream-User-Pflichten.

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

REACH/PIC-Compliance-Checkliste, Exportbenachrichtigungsschreiben an ECHA, SDS-Pruef-Protokoll und Zolldokumentationstemplate.

## Quellen

- [VO (EG) 1907/2006 REACH auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32006R1907)
- [VO (EU) 649/2012 PIC auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R0649)
- [ECHA REACH-Datenbank](https://echa.europa.eu/de/information-on-chemicals)
- [Zoll.de Gefahrgut Chemikalien](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/Chemikalien/chemikalien_node.html)

## 2. `aussenwirtschaft-cites-artenschutz`

**Fokus:** Artenschutz-Pflichten bei Im- und Export von CITES-geschuetzten Tieren und Pflanzen: VO (EG) 338/97 und CITES-Uebereinkommen. CITES-Genehmigungsverfahren Anhang A-D, zustaendige Behoerden (BfN, Zoll), Ausnahmen und Bescheinigungen. Fallkonstellation: Kunsthaendler importiert Elfenbein-Antiken. Output: CITES-Genehmigungspaket und Artenschutzbescheinigung.

# CITES-Artenschutz: Genehmigungen fuer geschuetzte Arten im Aussenhandel

## Mandantenfall

- Kunsthaendler moechte Elfenbein-Schnitzereien aus den 1960er Jahren importieren; CITES-Status klaeren.
- Reptilienhaendler exportiert Terrarien-Tiere; welche CITES-Genehmigungen erforderlich?
- Moebelhaendler bezieht Holz aus tropischen Laendern; CITES-Holzarten pruefen.

## Erste Schritte

1. Art und Anhang-Einstufung in CITES-Anhang A-D (VO 338/97) und CITES-Appendix I-III pruefen.
2. Fuer Anhang A/B: Aus- und Einfuhrgenehmigung bei zustaendiger Behoerde beantragen (BfN/Landeslbehoerden).
3. Fuer Anhang C: Exportbescheinigung des Herkunftslandes und Einfuhrnotifizierung.
4. Fuer Pre-Convention-Objekte: Herkunftsnachweis vor CITES-Listierung (Art. 2 Abs. 2 VO 338/97).
5. Zollanmeldung mit CITES-Referenz und Genehmigungsnummer.
6. Archivierung und Aufbewahrung aller CITES-Unterlagen (Lebensdauer des Exemplars).

## Rechtsrahmen

- **VO (EG) 338/97**: EU-Artenschutz-Grundverordnung.
- **VO (EG) 865/2006**: Durchfuehrung der Artenschutzverordnung.
- **CITES-Uebereinkommen**: Washingtoner Artenschutzuebereinkommen (1973).
- **§§ 71-73 BNatSchG**: Nationales Strafrecht bei Artenschutzverletzungen.
- **AWG § 18**: Aussenwirtschaftsrechtliche Strafbarkeit bei Verstoss.

## Pruef-Raster

- [ ] Art korrekt bestimmt und CITES-Anhang-Einstufung geprueft?
- [ ] Genehmigung fuer Anhang A/B beantragt und erteilt?
- [ ] Pre-Convention-Herkunftsnachweis fuer aeltere Objekte vorhanden?
- [ ] CITES-Dokumente bei Zollanmeldung beigefuegt?
- [ ] Archivierung fuer Lebensdauer des Exemplars sichergestellt?
- [ ] Straf- und Ordnungswidrigkeits-Risiko bewertet?

## Typische Fallstricke

- CITES-Anhang-Einstufung aendert sich; Jahreslisten pruefen.
- Pre-Convention-Ausnahme ist eng; Beweislast liegt beim Importeur.
- Illegale CITES-Waren koennen nicht nachtraeglich legalisiert werden.
- Zoll und Strafverfolgungsbehoerden kooperieren bei CITES-Kontrollen intensiv.

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

CITES-Genehmigungspaket mit Antragsformularen, Artbestimmungsprotokoll, Herkunftsnachweisen und Archivierungsplan.

## Quellen

- [VO (EG) 338/97 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:31997R0338)
- [Bundesamt fuer Naturschutz CITES](https://www.bfn.de/themen/cites.html)
- [Zoll.de Artenschutz](https://www.zoll.de/DE/Fachthemen/Verbote-Beschraenkungen/Artenschutz/artenschutz_node.html)
- [BNatSchG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bnatschg_2009/index.html)

## 3. `aussenwirtschaft-dual-use-forschung-hochschule`

**Fokus:** Exportkontrolle im Hochschul- und Forschungskontext: Dual-Use-Pruefung fuer akademischen Wissenstransfer, Publikationen, Konferenzbetraege, Forschungskooperationen und Software nach VO (EU) 2021/821 und AWG. Ausnahmen fuer Grundlagenforschung und oeffentlich zugaengliches Wissen. Besondere Risiken bei technischer Ausbildung auslaendischer Studierender. Output: Pruefvermerk fuer Forschungsvorhaben.

# Dual-Use in Forschung und Hochschule: Wissenstransfer und Exportkontrolle

## Mandantenfall

- Universitaet kooperiert mit chinesischem Forschungsinstitut; Frage, ob Datenuebertragung genehmigungspflichtig.
- Doktorand aus Iran erhalt Zugang zu Laboren und Geraeten; Dual-Use-Compliance pruefen.
- Professor moechte Konferenzbeitrag ueber Laserparameter veroeffentlichen; Dual-Use-Relevanz?

## Erste Schritte

1. Forschungsgegenstand und Technologie auf Dual-Use-Listeneintrag pruefen (Anhang I VO 2021/821).
2. Ausnahme fuer Grundlagenforschung (Art. 2 Nr. 9 VO 2021/821) und oeffentlich zugaengliche Info pruefen.
3. Wissenstransfer an auslaendische Beteiligte als 'Verbringung' oder 'Ausfuhr' einordnen.
4. Endverwender-Pruefung fuer Auslandsstudierende und Kooperationspartner.
5. Genehmigung bei BAFA beantragen falls kein Ausnahmetatbestand greift.
6. Hochschulleitung und Forschungsfoerderer ueber Compliance-Anforderungen informieren.

## Rechtsrahmen

- **Art. 2 Nr. 9 VO (EU) 2021/821**: Ausnahme fuer Grundlagenforschung.
- **Art. 26 Abs. 1 lit. a VO (EU) 2021/821**: Ausnahme fuer oeffentlich zugaengliche Information.
- **AWG §§ 8, 18**: Genehmigungspflicht und Strafbarkeit bei Wissenstransfer.
- **§ 9 AWV**: Genehmigungsfreie Ausfuhren (Grenzen im akademischen Bereich).
- **VO (EU) 2021/821 Anhang I Kategorie 5**: Telekommunikation/Informationssicherheit.

## Pruef-Raster

- [ ] Technologie im Dual-Use-Anhang I gelistet?
- [ ] Grundlagenforschungs-Ausnahme sachlich anwendbar?
- [ ] Publikation nicht bereits vor Genehmigung oeffentlich zugaenglich?
- [ ] Endverwender auslaendischer Partner geprueft?
- [ ] Catch-All fuer nicht-gelistete sensitive Technologien geprueft?
- [ ] Hochschulleitung und Compliance-Stelle informiert?

## Typische Fallstricke

- Technische Ausbildung (Hands-on-Training) faellt nicht unter Grundlagenforschungs-Ausnahme.
- Gemeinsame Publikation vor BAFA-Freigabe kann rechtswidrige Technologiuebertragung darstellen.
- Fernzugriff auf IT-Systeme mit sensitiver Software gilt als Ausfuhr.
- Kooperationsvertraege sichern keine Compliance; individuelle Pruefung jeder Datenuebertragung noetig.

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

Pruefvermerk fuer Forschungsvorhaben mit Listeneintrag-Analyse, Ausnahmenbegruendung und Genehmigungsempfehlung, sowie Hochschul-Leitfaden.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Technologietransfer Hochschule](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 4. `aussenwirtschaft-embargo-belarus`

**Fokus:** EU-Belarus-Sanktionsregime nach VO (EU) 765/2006 und VO (EU) 2022/576 (Russland-Belarus-Gueterembargoerweiterung): gelistete Personen und Unternehmen, Guetersanktionen, Dienstleistungsverbote und Exportbeschraenkungen. Besondere Risiken: Umgehung von Russland-Embargo ueber Belarus. Pruefung von Handelsbeziehungen mit belarussischen Parteien. Output: Embargo-Pruefungsvermerk und Screeningprotokoll.

# Embargo Belarus: Sanktionsregime und Umgehungsrisiken

## Mandantenfall

- Exporteur liefert Industriegueter nach Belarus; Frage ob VO 765/2006-Verbote greifen.
- Bank erhaelt Zahlungsauftrag von belarussischem Staatsunternehmen; Listenscreening.
- Unternehmen fragt, ob Lieferung ueber Zwischenhaendler in Belarus als Russland-Embargo-Umgehung gilt.

## Erste Schritte

1. EU-Sanktionsliste Belarus (VO 765/2006) und Finanzsanktionsliste pruefen.
2. Guetersanktionen-Katalog (Anhang VO 765/2006 und Ergaenzungsverordnungen) gegenueber KN-Code pruefen.
3. Russland-Embargo-Umgehungsrisiko: Doppelcheck ob Gueter via Belarus nach Russland umgeleitet werden (Art. 12 VO 833/2014).
4. Dienstleistungsverbote (IT, Beratung, PR) fuer belarussische Staatsunternehmen pruefen.
5. Zahlungsrouting ueber belarussische Banken auf Sanktionsliste pruefen.
6. Stop-Ship bei Unsicherheit bis vollstaendige Pruefung.

## Rechtsrahmen

- **VO (EU) 765/2006**: Restriktive Massnahmen gegen Belarus.
- **VO (EU) 2022/576 Art. 7 ff.**: Erweiterter Sanktionsrahmen und Gueterliste.
- **Art. 12 VO (EU) 833/2014**: Russland-Umgehungsverbot auch via Belarus.
- **AWG § 18**: Strafbarkeit bei Embargo-Verstoss.
- **Art. 2 VO (EU) 765/2006**: Bereitstellungsverbot fuer gelistete Personen.

## Pruef-Raster

- [ ] Partei auf EU-Sanktionsliste Belarus geprueft?
- [ ] Gueterkategorie und Anhang-Verbote geprueft?
- [ ] Russland-Umgehungsrisiko explizit ausgeschlossen?
- [ ] Dienstleistungsverbot fuer Staatsunternehmen geprueft?
- [ ] Zahlungsrouting ueber sanktionierten Kanal geprueft?
- [ ] Stop-Ship bei Risiko ausgeloest?

## Typische Fallstricke

- Belarus-Embargo und Russland-Embargo sind separate Rechtsregime; beide muessen geprueeft werden.
- Staatliche Kontrollbeteiligung in belarussischen Unternehmen loest Sanktionsrisiko auch ohne Listung aus.
- Umgehung kann strafbar sein auch ohne Listentreffer der Gegenpartei.
- Dienstleistungsverbote gelten auch fuer Unterauftragsverhaeltnisse.

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

Embargo-Pruefungsvermerk mit Sanktionslisten-Screeningprotokoll, Gueterkategorien-Uebersicht, Umgehungsanalyse und Freigabe-/Sperrempfehlung.

## Quellen

- [VO (EU) 765/2006 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32006R0765)
- [EU Sanctions Map Belarus](https://www.sanctionsmap.eu/#/main/details/4)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Belarus-Embargo](https://www.bafa.de/DE/Aussenwirtschaft/Exportkontrolle/Embargolaender/embargolaender_node.html)
