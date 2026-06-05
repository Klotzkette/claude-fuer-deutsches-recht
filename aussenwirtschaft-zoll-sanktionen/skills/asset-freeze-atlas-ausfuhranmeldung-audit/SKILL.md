---
name: asset-freeze-atlas-ausfuhranmeldung-audit
description: "Asset Freeze Atlas Ausfuhranmeldung Audit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Asset Freeze Atlas Ausfuhranmeldung Audit

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Asset Freeze Atlas Ausfuhranmeldung Audit** im Plugin Außenwirtschaft / Zoll / Sanktionen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `aussenwirtschaft-asset-freeze-sofortmassnahmen` | Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftlichen Ressourcen nach Art. 2 VO (EU) 269/2014 und Art. 4 VO (EU) 833/2014. Checkliste fuer Banken, Notare und Unternehmen: Identifizierung sanktionierbarer Vermoegen, Meldepflicht an Bundesbank/BaFin und zustaendige Behoerden. Output: Einfrierungs-Protokoll und Meldedokument. |
| `aussenwirtschaft-atlas-ausfuhranmeldung-check` | Qualitaetssicherung und Fehleranalyse von ATLAS-Ausfuhranmeldungen (EXA): Pruefung der Pflichtfelder nach UZK Art. 162-163 und DA Anhang B, Einreihung (KN-Code), Warenwerttaetigung, Verfahrenscodes, Lizenz- und Genehmigungshinweise sowie MRN-Status. Identifiziert typische Ablehnungsgruende in ATLAS. Output: Fehler-Korrekturliste und freigegebene Anmeldung. |
| `aussenwirtschaft-audit-trail-freigaben` | Aufbau und Pflege revisionssicherer Audit-Trails fuer Exportkontroll-Freigaben: Dokumentationsstandards nach AWG § 14 und AWV § 24 (Aufbewahrungsfristen) sowie Anforderungen der EU-Dual-Use-VO Art. 20. Sichert Freigabeprotokolle, Screening-Logs, Genehmigungsunterlagen und Kommunikation fuer Pruefungssituationen. Output: Audit-Trail-Struktur und Dokumentationsrichtlinie. |
| `aussenwirtschaft-ausfuhrverantwortlicher-organisation` | Benennung und Organisation des Ausfuhrverantwortlichen nach AWG § 7 und BAFA-Anforderungen: Aufgaben, Vollmachten und Haftung des Ausfuhrverantwortlichen, Einbindung in Compliance-Struktur, interne Berichtslinien und Vertretungsregeln. Fallkonstellation: KMU richtet erstmals Exportkontroll-Funktion ein. Output: Stellenbeschreibung und Organisationsvermerk. |

## Arbeitsweg

Im Plugin Außenwirtschaft / Zoll / Sanktionen gilt für **Asset Freeze Atlas Ausfuhranmeldung Audit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `aussenwirtschaft-asset-freeze-sofortmassnahmen`

**Fokus:** Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftlichen Ressourcen nach Art. 2 VO (EU) 269/2014 und Art. 4 VO (EU) 833/2014. Checkliste fuer Banken, Notare und Unternehmen: Identifizierung sanktionierbarer Vermoegen, Meldepflicht an Bundesbank/BaFin und zustaendige Behoerden. Output: Einfrierungs-Protokoll und Meldedokument.

# Asset Freeze: Sofortmassnahmen beim Einfrieren sanktionierten Vermoegens

## Mandantenfall

- Bank stellt Sanktionstreffer bei Kontoinhaber fest; internes Compliance-Team fragt nach Sofortmassnahmen.
- Notar beurkundet Immobilienkauf; Kaeufer erweist sich als UBO einer sanktionierten russischen Holdinggesellschaft.
- Unternehmen erhalt Zahlungsauftrag von Gegenpartei, die neu auf EU-Sanktionsliste aufgenommen wurde.

## Erste Schritte

1. Sanktionstreffer sofort dokumentieren: Name, Listennummer, Verordnung, Datum des Treffers.
2. Gelder/wirtschaftliche Ressourcen einfrieren; keine Auszahlung, kein Transfer, keine Verrechnung.
3. Zustaendige nationale Behoerde informieren: Bundesbank (Devisenbeschraenkungen), BaFin (Finanzsektor), BAFA (Gueter).
4. Ggf. Freistellungs- oder Genehmigungsantrag vorbereiten (Art. 6 VO 269/2014: humanitaere Ausnahme).
5. Rechtsbeistand einschalten; Haftungsrisiko der handelnden Personen absichern.
6. Legal Hold fuer alle relevanten Unterlagen erteilen.

## Rechtsrahmen

- **Art. 2 VO (EU) 269/2014**: Bereitstellungsverbot und Einfrierungspflicht (Russland-Finanzsanktionen).
- **Art. 4 VO (EU) 833/2014**: Sektorales Embargo und wirtschaftliche Ressourcen.
- **Art. 11 VO (EU) 269/2014**: Meldepflicht bei eingefrorenen Geldern an Mitgliedstaaten.
- **§ 18 AWG**: Strafbewehrte Bereitstellung sanktionierten Vermogens.
- **§ 22 Abs. 4 AWG**: Freiwillige Selbstanzeige als Mildernungsmoeglichkeit.

## Pruef-Raster

- [ ] Trefferidentitaet eindeutig verifiziert (kein False Positive)?
- [ ] Einfrierungsmassnahmen sofort und vollstaendig umgesetzt?
- [ ] Zustaendige Behoerde (Bundesbank/BaFin/BAFA) rechtzeitig informiert?
- [ ] Freistellungsantrag fuer genehmigte Transaktionen vorbereitet?
- [ ] Legal Hold erteilt und Unterlagen gesichert?
- [ ] Strafrecht-/Haftungsrisiko bewertet und Rechtsberatung eingeholt?

## Typische Fallstricke

- 50/50-Regel bei Eigentum: Auch indirekt sanktionierten Gesellschaften muss eingefroren werden.
- Einfrierung muss vollstaendig sein; Teilauszahlungen oder Verrechnung verstoessen gegen Bereitstellungsverbot.
- Meldepflicht ist unverzueglich; Versaeumnis fuehrt zu eigenem Sanktionsrisiko.
- Humanitaere Ausnahmen erfordern explizite Genehmigung; nicht eigenmaechtig handeln.

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

Einfrierungs-Protokoll mit Treffernachweis, Meldeschreiben an Bundesbank/BaFin/BAFA, Freistellungsantrag-Entwurf und Legal-Hold-Anweisung.

## Quellen

- [VO (EU) 269/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [VO (EU) 833/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [Bundesbank Devisenbeschraenkungen](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/finanzsanktionen)
- [BAFA Aussenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)

## 2. `aussenwirtschaft-atlas-ausfuhranmeldung-check`

**Fokus:** Qualitaetssicherung und Fehleranalyse von ATLAS-Ausfuhranmeldungen (EXA): Pruefung der Pflichtfelder nach UZK Art. 162-163 und DA Anhang B, Einreihung (KN-Code), Warenwerttaetigung, Verfahrenscodes, Lizenz- und Genehmigungshinweise sowie MRN-Status. Identifiziert typische Ablehnungsgruende in ATLAS. Output: Fehler-Korrekturliste und freigegebene Anmeldung.

# ATLAS-Ausfuhranmeldung: Qualitaetscheck und Fehlerkorrektur

## Mandantenfall

- ATLAS-Anmeldung wird mit Fehlercode H7A7 zurueckgewiesen; Exporteur weiss nicht warum.
- Zollagent stellt fest, dass Genehmigungshinweis (BAFA-Nr.) in der Anmeldung fehlt.
- Ausfuhranmeldung mit falschem Verfahrenscode (10 00 statt 10 21) erstellt; Rueckforderung droht.

## Erste Schritte

1. ATLAS-Fehlerprottokoll und MRN-Status sichten; Fehlercode-Glossar des Zolls heranziehen.
2. Pflichtfelder Anhaenge B UZK-DA pruefen: KN-Code, Ursprung, Wert, Menge, Empfaenger, Verfahren.
3. Genehmigungshinweise (BAFA-Genehmigungsnummer, Verwendungszweck) korrekt eingetragen?
4. Verfahrenscode und Unterverfahrenscode gegenueber Warenfluss und Bewilligungen pruefen.
5. Statistischer Wert und Zollwert gegenueber Rechnung abgleichen.
6. Korrekturmoeglichkeiten in ATLAS nutzen; bei Abgangsanmeldung Korrekturfenster beachten.

## Rechtsrahmen

- **UZK Art. 162-163**: Pflichtfelder und Form der Ausfuhranmeldung.
- **UZK-DA Anhang B**: Datensatz der Ausfuhranmeldung.
- **UZK-IA Art. 221-236**: Elektronische Ausfuhranmeldungspflichten.
- **§ 11a ZollVG**: Auskunftspflichten bei ATLAS-Fehler.
- **AWV § 77**: Statistikmeldepflicht (Intrastat) bei EU-internem Verbringen.

## Pruef-Raster

- [ ] Alle Pflichtfelder laut DA-Anhang B ausgefuellt?
- [ ] KN-Code und Beschreibung konsistent?
- [ ] Genehmigungsnummer korrekt und gueltiger Zeitraum?
- [ ] Verfahrenscode und Unterverfahrenscode korrekt?
- [ ] Statistischer Wert plausibel gegenueber Rechnung?
- [ ] MRN-Status und Abfertigungsergebnis geprueft?

## Typische Fallstricke

- Falscher KN-Code loest falsche TARIC-Massnahmen und Genehmigungserfordernisse aus.
- Fehlendes Genehmigungshinweis-Feld fuehrt zur Ablehnung kontrollpflichtiger Waren.
- Verfahrenscode 10 00 bei Veredelungsgutern falsch; richtig ist spezifischer Bewilligungscode.
- Statistischer Wert muss Incoterms-bereinigter FOB-Wert sein; oft unrichtig.

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

Fehler-Korrekturliste mit Feld-Referenz und Korrekturvorschlag, freigegebene Anmeldungs-Datei und Freigabe-Protokoll fuer Compliance.

## Quellen

- [UZK-DA Anhang B auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de ATLAS-Ausfuhr](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Elektronische-Zollanmeldung/ATLAS/atlas_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [BAFA Genehmigungsdokumentation](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)

## 3. `aussenwirtschaft-audit-trail-freigaben`

**Fokus:** Aufbau und Pflege revisionssicherer Audit-Trails fuer Exportkontroll-Freigaben: Dokumentationsstandards nach AWG § 14 und AWV § 24 (Aufbewahrungsfristen) sowie Anforderungen der EU-Dual-Use-VO Art. 20. Sichert Freigabeprotokolle, Screening-Logs, Genehmigungsunterlagen und Kommunikation fuer Pruefungssituationen. Output: Audit-Trail-Struktur und Dokumentationsrichtlinie.

# Audit-Trail: Revisionssichere Freigabedokumentation im Aussenhandel

## Mandantenfall

- BAFA prueft Exporteur nach wiederholten Genehmigungsantraegen; Auditoren verlangen vollstaendigen Freigabe-Trail.
- Hauptzollamt fordert bei Aussen-pruefung lueckenlosen Nachweis fuer Sanktionsscreening der letzten 3 Jahre.
- Unternehmensberatung hilft KMU beim Aufbau ersttauglicher Exportkontroll-Dokumentation fuer ICP.

## Erste Schritte

1. Pflicht zur Aufbewahrung von Exportkontrolldokumentation nach AWV § 24 und UZK Art. 51 feststellen (in der Regel 5-10 Jahre).
2. Kategorien von Freigabedokumenten inventarisieren: Screening-Logs, Klassifizierungsdossiers, Genehmigungen, Endverwendungserklaerungen.
3. Elektronisches Ablagesystem mit Zeitstempeln und Versionierung aufbauen.
4. Freigabeprozess mit Vier-Augen-Prinzip und Unterschriftenregelung etablieren.
5. Automatische Backup- und Loeschroutinen gem. DSGVO abstimmen.
6. Regelmaessige interne Audit-Tests zum Vollstaendigkeitsnachweis einplanen.

## Rechtsrahmen

- **AWV § 24**: Aufzeichnungs- und Aufbewahrungspflichten.
- **UZK Art. 51**: Aufbewahrung zollrelevanter Unterlagen (3 Jahre + Verlaehngerung).
- **Art. 20 VO (EU) 2021/821**: Aufzeichnungspflichten des Ausfuehrers.
- **§ 14 AWG**: Auskunftspflichten und Kontrollbefugnisse der Behoerden.
- **GoBD (BMF-Schreiben 2019)**: Grundsaetze ordnungsmaessiger Buchfuehrung fuer digitale Unterlagen.

## Pruef-Raster

- [ ] Aufbewahrungspflicht je Dokument-Kategorie bekannt und umgesetzt?
- [ ] Zeitstempel und Versionierung fuer alle elektronischen Dokumente sichergestellt?
- [ ] Vier-Augen-Prinzip bei Freigabeentscheidungen dokumentiert?
- [ ] Zugriffsberechtigungen und Protokollierung eingerichtet?
- [ ] Backup und Wiederherstellbarkeit getestet?
- [ ] DSGVO-Kompatibilitaet der Langzeitarchivierung sichergestellt?

## Typische Fallstricke

- Papier-Dokumente ungeschuetzt archiviert; im Pruefungsfall nicht auffindbar.
- Screening-Logs ohne Datum oder Quellangabe sind als Nachweis wertlos.
- Zugriffsberechtigungen nicht protokolliert; Manipulationsrisiko im Audit.
- Aufbewahrungsfristen je Dokumenttyp verschieden; pauschale 5-Jahres-Regel reicht nicht.

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

Audit-Trail-Konzept mit Dokumentenkategorien und Aufbewahrungsfristen, Prozess-Flussdiagramm, Muster-Freigabeprotokoll und Pruefungs-FAQ fuer Auditoren.

## Quellen

- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [VO (EU) 2021/821 Art. 20 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [UZK Art. 51 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [BAFA Kontrollpflichten](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/ausfuhrkontrolle_node.html)

## 4. `aussenwirtschaft-ausfuhrverantwortlicher-organisation`

**Fokus:** Benennung und Organisation des Ausfuhrverantwortlichen nach AWG § 7 und BAFA-Anforderungen: Aufgaben, Vollmachten und Haftung des Ausfuhrverantwortlichen, Einbindung in Compliance-Struktur, interne Berichtslinien und Vertretungsregeln. Fallkonstellation: KMU richtet erstmals Exportkontroll-Funktion ein. Output: Stellenbeschreibung und Organisationsvermerk.

# Ausfuhrverantwortlicher: Funktion, Haftung und Organisation

## Mandantenfall

- KMU erhalt BAFA-Anfrage und stellt fest, dass kein benannter Ausfuhrverantwortlicher existiert.
- Konzernmutter prueft, ob Ausfuhrverantwortlicher-Rolle in shared-service-Struktur zentralisiert werden kann.
- Neugegrundetes Tech-Unternehmen mit Dual-Use-Produkten muss Exportkontroll-Funktion aufbauen.

## Erste Schritte

1. Gesetzliche Pflicht zur Benennung pruefen: § 7 AWG, BAFA-Merkblatt Exportverantwortung.
2. Geeignete Person identifizieren: Kenntnisse im Exportkontrollrecht, Erreichbarkeit, Befugnisse.
3. Stellenbeschreibung erstellen: Aufgaben, Berichtslinie an Geschaeftsfuehrung, Vertretung.
4. Interne Vollmacht und Entscheidungskompetenzen dokumentieren (Freigabe, Hold, Eskalation).
5. Schulungsplan fuer initialen und laufenden Wissenserhalt erstellen.
6. BAFA ueber Benennung informieren falls explizit gefordert; Dokumentation im ICP ablegen.

## Rechtsrahmen

- **§ 7 AWG**: Verantwortlichkeit des Ausfuhrers.
- **BAFA-Merkblatt 'Exportverantwortung'**: Anforderungen an Ausfuhrverantwortlichen.
- **Art. 9 VO (EU) 2021/821**: Interne Compliance-Programme (ICP) und Verantwortlichkeit.
- **§ 130 OWiG**: Aufsichtspflichtverletzung durch Geschaeftsfuehrung.
- **§ 18 AWG**: Haftungsrahmen fuer unerlaubte Ausfuhr.

## Pruef-Raster

- [ ] Ausfuhrverantwortlicher schriftlich benannt?
- [ ] Person qualifiziert und mit Entscheidungsbefugnissen ausgestattet?
- [ ] Vertretungsregel fuer Urlaub und Krankheit geregelt?
- [ ] Berichtslinie an Geschaeftsfuehrung dokumentiert?
- [ ] Zugang zu aktuellen Gueterlisten und Sanktionslisten sichergestellt?
- [ ] ICP-Dokumentation vollstaendig und dem Ausfuhrverantwortlichen uebergeben?

## Typische Fallstricke

- Ausfuhrverantwortlicher ohne reale Entscheidungsbefugnis ist haftungsrechtlich wertlos.
- Vertretungsluecken bei Urlaub gefaehrden laufende Exportvorgaenge.
- Fehlende Schulung fuehrt zu unbewussten Verstossen und hoeherer persoenlicher Haftung.
- Konzernstrukturen erfordern klare Zustaendigkeitsabgrenzung je Rechtseinheit.

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

Stellenbeschreibung Ausfuhrverantwortlicher, Vollmachts-Urkunde, Organisationsdiagramm Exportkontroll-Funktion und BAFA-Meldungsvorlage.

## Quellen

- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [BAFA Exportkontrolle Interne Compliance](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Interne_Compliance/interne_compliance_node.html)
- [VO (EU) 2021/821 Art. 9 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [OWiG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig_1968/index.html)
