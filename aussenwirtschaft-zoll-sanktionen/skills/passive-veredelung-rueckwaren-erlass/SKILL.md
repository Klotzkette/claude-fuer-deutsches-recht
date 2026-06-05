---
name: passive-veredelung-rueckwaren-erlass
description: "Passive Veredelung Rueckwaren Erlass: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Passive Veredelung Rueckwaren Erlass

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Passive Veredelung Rueckwaren Erlass** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-passive-veredelung` | Passive Veredelung nach UZK Art. 259-262 und DA Art. 240-244: Beantragung der Bewilligung beim Hauptzollamt, Abgabenprivileg fuer Veredelungserzeugnisse, Ausgleichserzeugnisse, Warenidentitaet, Frist und Zollwertberechnungsmethoden (Abzugsmethode). Output: Bewilligungsantrag und Zollwert-Berechnungsvorlage. |
| `aussenwirtschaft-rueckwaren-erlass-erstattung` | Zollerlass und -erstattung fuer Rueckwaren nach UZK Art. 203 und Verfahren 6321: Voraussetzungen der Rueckwaren-Abgabenfreiheit, Dreijahrsfrist, Identitaetsnachweis, Abgrenzung zur aktiven und passiven Veredelung. Output: Antragsschreiben Rueckwaren-Zollerlass und Identitaetsnachweis-Dokumentation. |
| `aussenwirtschaft-technologie-transfer-cloud-download` | Exportkontrolle fuer Technologietransfer durch Cloud-Dienste und Downloads: Genehmigungspflicht nach VO (EU) 2021/821 Art. 2 Nr. 7 (technische Unterstuetzung) und Art. 22 (Brokering) bei Software-Uploads Fernzugriff und E-Mail-Uebermittlung in Drittlaender. Abgrenzung zur physischen Ausfuhr. Output: Transfer-Klassifizierung und Zugangssteuerungskonzept. |
| `aussenwirtschaft-verbrauchsteuer` | Verbrauchsteuerrecht im Aussenhandel: Energiesteuer Alkoholsteuer Tabaksteuer und ElektrizitaetssteuerG bei Ein- und Ausfuhr. Steueraussetzungsverfahren EMCS Befoerderungsdokument (e-VD) und Erstattungsansprueche bei Ausfuhr verbrauchsteuerpflichtiger Waren. Abgrenzung Zoll und Verbrauchsteuer. Output: Verbrauchsteuer-Pruefmatrix und EMCS-Eintragungsanleitung. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Passive Veredelung Rueckwaren Erlass**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-passive-veredelung`

**Fokus:** Passive Veredelung nach UZK Art. 259-262 und DA Art. 240-244: Beantragung der Bewilligung beim Hauptzollamt, Abgabenprivileg fuer Veredelungserzeugnisse, Ausgleichserzeugnisse, Warenidentitaet, Frist und Zollwertberechnungsmethoden (Abzugsmethode). Output: Bewilligungsantrag und Zollwert-Berechnungsvorlage.

# Passive Veredelung: Bewilligung, Warenidentitaet und Zollwertberechnung

## Mandantenfall

- Bekleidungshersteller schickt Stoffe zur Konfektion nach Tunesien und reimportiert fertige Kleidung.
- Maschinenbauer sendet defekte Baugruppe ins Ausland zur Reparatur; passive Veredelung als Zollverfahren.
- Juwelier schickt Edelsteine nach Thailand zum Fassen und reimportiert Schmuck; Ursprungsproblem.

## Erste Schritte

1. Passive-Veredelungs-Bewilligung beim zustendigen Hauptzollamt beantragen (Formular 0338).
2. Warenidentitaet sicherstellen: Identifizierungsmassnahmen (Seriennummern, Markierungen, Analysemethoden).
3. Bewilligungsfrist festlegen: Veredelungsfrist realistisch kalkulieren.
4. Zollwertberechnungsmethode waehlen: Abzugsmethode (Standard) oder Kostenmethode.
5. Handelswerttabelle fuer Ausgleichserzeugnisse erstellen.
6. Rueckeinfuhr im Verfahren 6121 in ATLAS anmelden; Bewilligungsnummer angeben.

## Rechtsrahmen

- **UZK Art. 259-262**: Passive Veredelung, Bedingungen und Verfahren.
- **UZK-DA Art. 240-244**: Ausfuehrungsbestimmungen und Bewilligung.
- **UZK Art. 101**: Zollwertberechnungsmethoden fuer Veredelungserzeugnisse.
- **UZK-IA Art. 256**: Abzugsmethode fuer Zollwert.
- **UZK Art. 33**: Abgabenbefreiung fuer Rueckwaren (Abgrenzung).

## Pruef-Raster

- [ ] Bewilligung passive Veredelung vollstaendig und gueltig?
- [ ] Warenidentitaet durch geeignete Massnahmen sichergestellt?
- [ ] Veredelungsfrist eingehalten?
- [ ] Zollwertberechnungsmethode korrekt angewendet?
- [ ] Rueckeinfuhranmeldung mit korrektem Verfahrenscode und Bewilligungsnummer?
- [ ] Mengen- und Wertabrechnung gegenueber Hauptzollamt vollstaendig?

## Typische Fallstricke

- Veredelungsfrist laeuft ab ohne Rueckeinfuhr; Zollschuld fuer volle Ware.
- Warenidentitaet nicht ausreichend dokumentiert; Hauptzollamt akzeptiert Identifizierungsmassnahme nicht.
- Abzugsmethode falsch angewendet; Nachzoll-Risiko bei Zollpruefung.
- Passive Veredelung und Rueckwaren (Art. 203 UZK) werden verwechselt; falsche Anmeldung.

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

Bewilligungsantrag passive Veredelung, Warenidentitaets-Protokoll, Zollwert-Berechnungsvorlage (Abzugsmethode) und Abrechnungsformular.

## Quellen

- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Passive Veredelung](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren/Besondere-Verfahren/Veredelung/Passive-Veredelung/passive-veredelung_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 2. `aussenwirtschaft-rueckwaren-erlass-erstattung`

**Fokus:** Zollerlass und -erstattung fuer Rueckwaren nach UZK Art. 203 und Verfahren 6321: Voraussetzungen der Rueckwaren-Abgabenfreiheit, Dreijahrsfrist, Identitaetsnachweis, Abgrenzung zur aktiven und passiven Veredelung. Output: Antragsschreiben Rueckwaren-Zollerlass und Identitaetsnachweis-Dokumentation.

# Rueckwaren: Zollerlass und Identitaetsnachweis nach UZK Art. 203

## Mandantenfall

- Maschinenbauer exportiert Muster, die unverkauft zurueckkehren; Rueckwaren-Abgabenfreiheit beansprucht.
- Ausstellungsobjekte kehren nach Messe zuruck; mehr als 3 Jahre nach Ausfuhr.
- Ware wurde im Ausland repariert; Abgrenzung Rueckware vs. passive Veredelung unklar.

## Erste Schritte

1. Rueckware-Voraussetzungen pruefen: EU-Ursprungsstatus, Dreijahrsfrist (mit Ausnahmen), keine Bearbeitung im Ausland.
2. Identitaetsnachweis zusammenstellen: Ausfuhranmeldung, Seriennummern, Warenmerkmale.
3. Bearbeitung im Ausland pruefen: einfache Konservierung ist erlaubt; Reparatur fuehrt zu passiver Veredelung.
4. Verfahrenscode 6321 in ATLAS-Einfuhranmeldung verwenden.
5. Eventuelle Erstattungspflicht auf Exportland-MwSt pruefen.
6. Bei abgelaufener Dreijahrsfrist: Verlaengerungsantrag beim Hauptzollamt stellen.

## Rechtsrahmen

- **UZK Art. 203**: Rueckwaren, Abgabenfreiheit bei Wiedereinfuhr.
- **UZK-DA Art. 158**: Voraussetzungen fuer Rueckwaren-Status.
- **UZK Art. 204**: Verstaerkte Rueckwaren nach Bearbeitung (passive Veredelung Abgrenzung).
- **UZK-IA Art. 255**: Verfahren fuer Rueckwaren in ATLAS.
- **VO (EU) 952/2013 Art. 33**: Abgrenzung Rueckwaren von Wiedereinfuhr nach Veredelung.**

## Pruef-Raster

- [ ] EU-Ursprungsstatus der Ware bei urspruenglicher Ausfuhr bestanden?
- [ ] Dreijahrsfrist eingehalten oder Ausnahme/Verlaengerung vorhanden?
- [ ] Keine wesentliche Bearbeitung im Ausland (nur Konservierung zulassig)?
- [ ] Identitaetsnachweis vollstaendig (Ausfuhranmeldung, Merkmale, Seriennummern)?
- [ ] Verfahrenscode 6321 in ATLAS-Anmeldung verwendet?
- [ ] Abgrenzung zu passiver Veredelung geprueft?

## Typische Fallstricke

- Dreijahrsfrist abgelaufen ohne Antragsstellung; nachtraegliche Verlaengerung moeglich aber aufwendig.
- Reparatur im Ausland macht Ware zur passiven Veredelung, nicht zur Rueckware.
- Fehlender Identitaetsnachweis; urspruengliche Ausfuhranmeldung nicht mehr auffindbar.
- Rueckwaren-Verfahren ausgeschlossen bei Ware, die im EU-Ausland zollrechtlich in Frei-Verkehr gesetzt war.

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

Antragsschreiben Rueckwaren-Zollerlass an Hauptzollamt, Identitaetsnachweis-Dokumentation und Abgrenzungsvermerk passive Veredelung/Rueckware.

## Quellen

- [UZK Art. 203 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Rueckwaren](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollverfahren/Besondere-Verfahren/Rueckwaren/rueckwaren_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 3. `aussenwirtschaft-technologie-transfer-cloud-download`

**Fokus:** Exportkontrolle fuer Technologietransfer durch Cloud-Dienste und Downloads: Genehmigungspflicht nach VO (EU) 2021/821 Art. 2 Nr. 7 (technische Unterstuetzung) und Art. 22 (Brokering) bei Software-Uploads Fernzugriff und E-Mail-Uebermittlung in Drittlaender. Abgrenzung zur physischen Ausfuhr. Output: Transfer-Klassifizierung und Zugangssteuerungskonzept.

# Technologietransfer durch Cloud und Downloads: Exportkontrolle immaterieller Gueter

## Mandantenfall

- Ingenieur gibt Kollegen in Iran Fernzugriff auf CAD-Dateien fuer Dual-Use-Maschine.
- Unternehmen stellt Software-Update fuer gelistetes Produkt zum Download auf oeffentlichem Server bereit.
- Forschungsinstitut teilt technische Dokumentation ueber Cloud-Plattform mit Partnern in Russland.

## Erste Schritte

1. Art des Transfers bestimmen: Fernzugriff, Download, E-Mail-Anhang oder Cloud-Storage.
2. Technologie klassifizieren: Dual-Use-Code pruefen (VO 2021/821 Anhang I Anmerkung zu Technologie).
3. Empfaenger und Bestimmungsland identifizieren; Sanktions- und Embargocheck.
4. Genehmigungspflicht nach Art. 2 Nr. 2 (Ausfuhr) und Technologie-Anmerkung pruefen.
5. Zugangssteuerung pruefen: Wer hat tatsaechlich Zugriff auf Cloud-Ordner?
6. Zugangssteuerungskonzept mit Laender-Blacklist und Nutzer-Verifizierung dokumentieren.

## Rechtsrahmen

- **Art. 2 Nr. 2 VO (EU) 2021/821**: Definition der Ausfuhr umfasst elektronische Uebermittlung.
- **Technologie-Anmerkung (NTN) Anhang I VO 2021/821**: Kontrollierte Technologie auch als immaterielle Uebermittlung.
- **Art. 22 VO (EU) 2021/821**: Brokering-Kontrolle bei Vermittlung von Technologietransfers.
- **AWG § 2 Abs. 3**: Verbringungsbegriff umfasst auch elektronische Uebertragungen.
- **Art. 4 VO (EU) 2021/821**: Catch-All bei Kenntnis von militaerischer Endverwendung.

## Pruef-Raster

- [ ] Technologie klassifiziert und Dual-Use-Code geprueft?
- [ ] Empfaenger-Laender auf Embargo und Sanktionen geprueft?
- [ ] Zugangskontrolle fuer Cloud-Plattform mit Laender-Filter konfiguriert?
- [ ] E-Mail-Uebermittlung sensibler Technologiedaten protokolliert?
- [ ] Fernzugriff auf sensible Systeme auf Genehmigungspflicht geprueft?
- [ ] Aufzeichnung des Transfers fuer BAFA-Audit archiviert?

## Typische Fallstricke

- Oeffentliche Cloud-Ordner ohne Laendersperre gelten als weltweite Ausfuhr.
- Fernwartung von Dual-Use-Systemen in Embargo-Laendern ist genehmigungspflichtig.
- Technologie-Anmerkung gilt auch fuer allgemein zugaengliche technische Dokumente wenn sie Produktion ermoglichen.
- US-ITAR gilt extraterritorial auch fuer Technologie die auf EU-Servern liegt.

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

Transfer-Klassifizierungsvermerk, Zugangssteuerungskonzept fuer Cloud-Plattformen und Richtlinienentwurf fuer digitale Technologietransfer-Kontrolle.

## Quellen

- [VO (EU) 2021/821 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Dual-Use Technologietransfer](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Dual_Use/dual_use_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)

## 4. `aussenwirtschaft-verbrauchsteuer`

**Fokus:** Verbrauchsteuerrecht im Aussenhandel: Energiesteuer Alkoholsteuer Tabaksteuer und ElektrizitaetssteuerG bei Ein- und Ausfuhr. Steueraussetzungsverfahren EMCS Befoerderungsdokument (e-VD) und Erstattungsansprueche bei Ausfuhr verbrauchsteuerpflichtiger Waren. Abgrenzung Zoll und Verbrauchsteuer. Output: Verbrauchsteuer-Pruefmatrix und EMCS-Eintragungsanleitung.

# Verbrauchsteuer im Aussenhandel: Steueraussetzung EMCS und Erstattung

## Mandantenfall

- Brauerei exportiert Bier in Drittland; Verbrauchsteuer-Erstattungsantrag und Ausfuhrnachweise.
- Mineralolhaendler transportiert Dieselkraftstoff im Steueraussetzungsverfahren durch EU.
- Importeur von Tabakwaren muss Verbrauchsteuer bei Einfuhr anmelden und abfuehren.

## Erste Schritte

1. Ware auf Verbrauchsteuerpflicht pruefen: Energieerzeugnisse Alkohol Tabak Strom?
2. Steueraussetzungsverfahren: Ist Ware in zugelassenem Lager (Steuerlager) und EMCS aktiviert?
3. Befoerderungsdokument (elektronisches Verwaltungsdokument e-VD) in EMCS anlegen.
4. Ausfuhrerstattungsantrag: Ausfuhrnachweise (ATLAS-Ausgangsvermerk) fuer Verbrauchsteuer-Erstattung.
5. Steuerterritorium pruefen: Sondergebiete (Kanalinsel Buesingen) und Ueberschneidung mit Zollgebiet.
6. Nationale Verbrauchsteuerbehoerde (Hauptzollamt) und EMCS-Zugangsberechtigung pruefen.

## Rechtsrahmen

- **RL 2008/118/EG (Systemrichtlinie)**: Allgemeine Regelung fuer verbrauchsteuerpflichtige Waren.
- **EnergieStG**: Energiesteuer bei Mineral- und Biokraftstoffen.
- **BierStG AlkStG TabStG**: Warenbezogene Verbrauchsteuern.
- **§ 38 EnergieStG**: Steuerbefreiung bei Ausfuhr von Energieerzeugnissen.
- **UZK Art. 5 Nr. 2**: Zollgebiet abgegrenzt von Verbrauchsteuerterritorium.

## Pruef-Raster

- [ ] Ware korrekt als verbrauchsteuerpflichtig identifiziert?
- [ ] Steueraussetzungsverfahren und EMCS korrekt eroeffnet?
- [ ] e-VD vollstaendig und korrekt ausgefuellt?
- [ ] Ausfuhrnachweise fuer Erstattungsantrag vorhanden?
- [ ] Steuerterritorium-Sonderregelungen beachtet?
- [ ] Zustaendiges Hauptzollamt fuer Verbrauchsteuer korrekt bestimmt?

## Typische Fallstricke

- Verwechslung Zollgebiet und Verbrauchsteuerterritorium bei Sondergebieten wie Buesingen.
- Fehlendes e-VD fuehrt zur Steuerschuldentstehung bei Transport.
- Ausfuhrerstattung setzt lueckenlosen Ausfuhrnachweis voraus; ATLAS-Ausgangsvermerk allein meist nicht ausreichend.
- EMCS-Systemausfall muss mit Notfallverfahren ueberbrueckt werden.

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

Verbrauchsteuer-Pruefmatrix mit Waren-Einordnung, EMCS-Eintragungsanleitung, Erstattungsantrag-Muster und Abgrenzungstabelle Zoll/Verbrauchsteuer.

## Quellen

- [EnergieStG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/energiestg/index.html)
- [Zoll.de Verbrauchsteuern](https://www.zoll.de/DE/Fachthemen/Steuern/Verbrauchsteuern/verbrauchsteuern_node.html)
- [RL 2008/118/EG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32008L0118)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
