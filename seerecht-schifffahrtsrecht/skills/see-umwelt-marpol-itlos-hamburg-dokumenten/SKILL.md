---
name: see-umwelt-marpol-itlos-hamburg-dokumenten
description: "SEE Umwelt Marpol Itlos Hamburg Dokumenten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Umwelt Marpol Itlos Hamburg Dokumenten

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Umwelt Marpol Itlos Hamburg Dokumenten** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-018-umwelt-und-marpol` | Schiff hat Oel oder Chemikalien ins Meer eingeleitet; Strafanzeige und Bussgeldsverfahren. MARPOL Annex I (Oel) / II (Chemikalien) / VI (Abgase SOx/NOx); OelSG §§ 1-12; SeeUG § 11; StGB §§ 324/326 (Gewaesserschutz). Oil Record Book; Falscheintrag; US APPS Act. Output: Strafverteidigungs-Vermerk und Beweissicherungs-Checkliste. |
| `see-019-itlos-hamburg-und-unclos` | Flaggenstaatstreit oder Prompt-Release-Antrag vor dem ITLOS in Hamburg: UNCLOS Art. 292 (Prompt Release); Art. 290 (Vorlaeufige Massnahmen); ITLOS-Statute Annex VI. Relevante Faelle: M/V Saiga Nr. 2; Arctic Sunrise Nr. 22; Juno Trader Nr. 13; Ukraine vs. Russia Nr. 26. Output: ITLOS-Verfahrensstrategie und Sicherheitsleistungs-Kalkulation. |
| `see-020-dokumenten-cockpit-schiff` | Mandant benoetigt Uebersicht aller schiffsrelevanten Dokumente: Registerauszug; Hypothekenurkunden; Zertifikate (Klasse; ISM/DOC/SMC; MLC/DMLC; ISPS/ISSC); Flaggenzertifikat; Charter; Konnossements-Template. SchRG §§ 2/8-74; FlaggRG §§ 3-5; ISM-Code; MLC 2006 Titel 5; ISPS-Code. Output: Dokumenten-Cockpit-Matrix und Faelligkeits-Kalender. |
| `see-021-schiffshypothek-register-pruefen` | Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank prueft Seeschiffsregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte. |
| `see-022-schiffshypothek-hypothek-bestellen` | Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines hypothekenbelastetes Seeschiff. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Umwelt Marpol Itlos Hamburg Dokumenten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-018-umwelt-und-marpol`

**Fokus:** Schiff hat Oel oder Chemikalien ins Meer eingeleitet; Strafanzeige und Bussgeldsverfahren. MARPOL Annex I (Oel) / II (Chemikalien) / VI (Abgase SOx/NOx); OelSG §§ 1-12; SeeUG § 11; StGB §§ 324/326 (Gewaesserschutz). Oil Record Book; Falscheintrag; US APPS Act. Output: Strafverteidigungs-Vermerk und Beweissicherungs-Checkliste.

# Umwelt und MARPOL – Öleinleitung und Strafverfolgung

## Mandantenfall
Ein Kapitän soll auf der Elbe Bilgenwasser eingeleitet haben; die Küstenwache hat das Oil Record Book beschlagnahmt; Strafanzeige läuft. Eine Reederei erhält nach Anlaufen eines US-Hafens eine Klagekopie wegen falscher ORB-Einträge; US-Attorney ermittelt wegen magic-pipe-Manipulationen. Ein Tanker verliert nach Grundberührung Rohöl in der Nordsee.

## Erste Schritte
1. Sachverhaltsermittlung: Oil Record Book beschaffen; Motortagebuch; GPS-Tracks; AIS-Daten sichern.
2. MARPOL-Verstöße klassifizieren: Annex I = Öl; Annex II = Chemikalien; Annex VI = Luftschadstoffausstoß.
3. Strafbarkeit nach deutschem Recht: StGB § 324 (Gewässerverschmutzung); § 326 (unerlaubter Abfall); OelSG § 3.
4. Meldepflichten prüfen: MARPOL Annex I Reg. 11 – unverzügliche Meldung; SeeUG § 11.
5. Verteidigungsstrategie: Notfall-Ausnahme (MARPOL Annex I Reg. 4); Unabwendbarkeit; technischer Defekt.
6. Koordination mit P&I-Club: Pollution-Deckung aktivieren; Anwalt- und Kautionskosten.

## Rechtsrahmen
- MARPOL Annex I Reg. 9-11: Verbot der Öl-Einleitung; ORB-Pflicht; Meldeverpflichtungen.
- MARPOL Annex VI Reg. 12-14: SOx-Grenzen (0/5% weltweit ab 2020; 0/1% ECA); NOx Tier III.
- OelSG §§ 1-12: deutsche Umsetzung MARPOL für Einleitung in Bundesgewaesser.
- StGB § 324: Gewässerverunreinigung; Freiheitsstrafe bis 5 Jahre.
- StGB § 326: unerlaubtes Behandeln gefährlicher Abfälle.
- SeeUG §§ 6-11: Meldepflichten und Mitwirkungspflichten bei Seeunfällen mit Umweltauswirkungen.
- UNCLOS Art. 218-220: Hafenstaat- und Küstenstaatszuständigkeit für MARPOL-Verstöße.

## Prüfraster
- Enthält das ORB Falschangaben oder Lücken die auf magic-pipe-Nutzung hindeuten?
- Ist die Einleitung in einem MARPOL-Sondergebiet (Ostsee/Nordsee als ECA) erfolgt?
- Liegt ein Notfall vor der nach MARPOL Annex I Reg. 4 die Haftung ausschließt?
- Wurde die Einleitung unverzüglich dem zuständigen Küstenstaat gemeldet?
- Ist P&I-Pollution-Deckung ausreichend für Aufräumungskosten?

## Typische Fallstricke
- ORB-Falschangaben sind eigenständige Straftat (§ 267 StGB Urkundenfälschung).
- US-Strafverfolgung bei Vergehen auf Hochsee möglich wenn Schiff US-Hafen anläuft (APPS Act).
- MARPOL-Notfallausnahme eng auszulegen; technischer Defekt allein reicht oft nicht.
- Geschäftsführerhaftung: Reeder haftet für Organisationsverschulden.

## Output
- Strafverteidigungs-Vermerk: Tatbestand; Verteidigungsansätze; Beweislage
- Beweissicherungs-Checkliste (ORB; Logbücher; GPS; AIS)
- Meldepflichten-Übersicht nach MARPOL und SeeUG


## Erweiterte Normengrundlage

### MARPOL 73/78
- MARPOL Annex I: Verhütung der Verschmutzung durch Öl; Grenzwerte; Ölfilterpflicht.
- MARPOL Annex II: Noxious Liquid Substances; Chemikalientanker-Regeln.
- MARPOL Annex IV: Abwasser; Mindestabstand zur Küste.
- MARPOL Annex V: Müll; Einleitverbote; Garbage Management Plan.
- MARPOL Annex VI: Luftverschmutzung; SOx-Grenzwerte (2020: 0/5%); NOx Tier III; ECA-Zonen.

### Nationales Recht
- OWiG §§ 9; 30; 130: Unternehmensgeldbußen für MARPOL-Verstöße des Kapitäns.
- StGB § 324: Gewässerverunreinigung; Strafbarkeit bei vorsätzlichem Einleiten.
- SeeUmwVerhV: Seeschifffahrt-Umweltverhaltensverordnung; nationale Umsetzung.

## Checkliste MARPOL-Compliance
- [ ] IOPP-Certificate (MARPOL Annex I) vorliegend; gültig
- [ ] Oil Record Book (Part I und II) vollständig; keine Lücken
- [ ] Garbage Management Plan und Garbage Record Book an Bord
- [ ] Bunker-Qualität (Schwefelgehalt max. 0/5%) nachgewiesen; BDN vorliegend
- [ ] SOx-Scrubber oder Low-Sulphur-Fuel für ECA-Zonen dokumentiert
- [ ] NOx Tier III-Compliance für Neubauten nach 2016 geprüft

## Relevante Rechtsprechung
- BGH zur Strafbarkeit des Kapitäns bei MARPOL-Verstoß; StGB § 324; vorsätzliches Einleiten.
- OLG Hamburg zur behördlichen Kontrolle durch den Hafenstaat (Port State Control); Festhalten.
- ITLOS Ukraine v. Russia No. 26 (2019): Anwendung von UNCLOS Art. 218; Hafenstaatjurisdiktion.

## Quellen
- MARPOL IMO: https://www.imo.org/en/About/Conventions/Pages/International-Convention-for-the-Prevention-of-Pollution-from-Ships-(MARPOL).aspx
- OelSG: https://www.gesetze-im-internet.de/oelsg/
- StGB § 324: https://dejure.org/gesetze/StGB/324.html
- SeeUG: https://www.gesetze-im-internet.de/seeug/
- BSH Meeresumwelt: https://www.bsh.de/DE/THEMEN/Meeresumwelt/meeresumwelt_node.html

## 2. `see-019-itlos-hamburg-und-unclos`

**Fokus:** Flaggenstaatstreit oder Prompt-Release-Antrag vor dem ITLOS in Hamburg: UNCLOS Art. 292 (Prompt Release); Art. 290 (Vorlaeufige Massnahmen); ITLOS-Statute Annex VI. Relevante Faelle: M/V Saiga Nr. 2; Arctic Sunrise Nr. 22; Juno Trader Nr. 13; Ukraine vs. Russia Nr. 26. Output: ITLOS-Verfahrensstrategie und Sicherheitsleistungs-Kalkulation.

# ITLOS Hamburg und UNCLOS – Internationale Seerechtstreitigkeiten

## Mandantenfall
Ein Fischereifahrzeug eines Vertragsstaats wird von einem anderen Staat beschlagnahmt; der Flaggenstaat stellt einen Prompt-Release-Antrag nach UNCLOS Art. 292 beim ITLOS. Ein ausländisches Schiff wird unter Berufung auf MARPOL in einem deutschen Hafen festgehalten; der Flaggenstaat erwägt einstweilige Maßnahmen nach UNCLOS Art. 290. Eine Reederei nimmt an einem Annex-VII-Schiedsverfahren teil; die Gegenseite beantragt ITLOS einstweilige Maßnahmen.

## Erste Schritte
1. ITLOS-Zuständigkeit prüfen: UNCLOS Teil XV; Annex VI (ITLOS-Statut); Streitigkeit muss UNCLOS-Auslegung betreffen.
2. Prompt-Release-Voraussetzungen: UNCLOS Art. 292 – Schiff oder Crew verhaftet; angemessene Sicherheit anbieten.
3. Sicherheitsleistung kalkulieren: ITLOS-Praxis (M/V Saiga; Juno Trader) – Schiffswert; Ladungswert; Fangwert als Orientierung.
4. Antragsfristen: ITLOS-Regel 110 – Prompt Release kann sofort nach Verhaftung beantragt werden.
5. Einstweilige Maßnahmen nach Art. 290: Notlage; drohender Schaden für Parteien oder Meeresumwelt.
6. Schriftsätze vorbereiten: ITLOS Rules of the Tribunal; kurze Fristen; englisch oder französisch.

## Rechtsrahmen
- UNCLOS Art. 292: Prompt Release; Schiff und Crew unverzüglich freizulassen gegen angemessene Sicherheit.
- UNCLOS Art. 290: einstweilige Maßnahmen; sofortige Wirkung bis Entscheidung des Schiedsgerichts.
- ITLOS-Statut Annex VI: Zusammensetzung (21 Richter); Zuständigkeit; Verfahren.
- ITLOS-Regeln 110-121: Prompt-Release-Verfahren; Fristen; Schriftsätze; Sicherheiten.
- UNCLOS Art. 91-94: Flaggenstaat-Verantwortung als Ausgangspunkt für ITLOS-Klagen.
- UNCLOS Art. 220-228: Hafenstaat- und Küstenstaatszuständigkeit; ITLOS-Kontrolle.

## Prüfraster
- Ist Deutschland als Flaggen- oder Hafenstaat Partei eines UNCLOS-Streits?
- Liegt eine ITLOS-kompetenzfähige Seeforderung vor (Art. 21 ITLOS-Statut)?
- Ist die Sicherheitsleistung angemessen im Sinne der ITLOS-Praxis?
- Besteht Eile die einstweilige Maßnahmen rechtfertigt?
- Welches ITLOS-Verfahren passt: Prompt Release; Provisional Measures; Full Bench?
- Sind alle diplomatischen Wege ausgeschöpft?

## Typische Fallstricke
- ITLOS-Prompt-Release gilt nur für Schiffe; nicht für Personen.
- Sicherheitsleistung zu niedrig angesetzt; ITLOS kann Antrag zurückweisen.
- ITLOS-Schriftsätze müssen präzise UNCLOS-Normen zitieren; allgemeine Menschenrechtsargumente reichen nicht.
- M/V Saiga Case No. 2: Guinea hatte keinen Anspruch auf Verhaftung in der AWZ für Zollvergehen.

## Output
- ITLOS-Verfahrensstrategie (Prompt Release oder Provisional Measures)
- Sicherheitsleistungs-Kalkulation nach ITLOS-Praxis
- Schriftsatz-Struktur für Prompt-Release-Antrag
- Normübersicht UNCLOS Art. 292/290/220-228


## Erweiterte Normengrundlage

### UNCLOS
- UNCLOS Art. 2-32: Territorialmeer; Küstenmeer; Durchfahrtsrecht.
- UNCLOS Art. 55-75: AWZ; Rechte des Küstenstaates; Fischereirechte; Umweltschutz.
- UNCLOS Art. 91-94: Staatszugehörigkeit; genuine link; Flaggenstaat-Pflichten.
- UNCLOS Art. 218-228: Hafenstaatjurisdiktion; Strafverfolgung bei MARPOL-Verstößen.
- UNCLOS Art. 290-292: einstweilige Maßnahmen; Prompt Release; ITLOS-Zuständigkeit.

### ITLOS
- ITLOS Statut Art. 21: sachliche Zuständigkeit; Vertragsstaatenstreitigkeiten.
- ITLOS Statut Art. 25: einstweilige Maßnahmen; Aussetzung; Freilassung.
- ITLOS Statut Annex VI: Prompt-Release-Verfahren; beschleunigtes Verfahren.

## Checkliste ITLOS-Verfahren
- [ ] Staatszugehörigkeit der Parteien bestätigt; UNCLOS-Vertragsstaaten
- [ ] Zuständigkeitsgrundlage identifiziert (UNCLOS Part XV; Annex VII Schiedsgericht)
- [ ] Erschöpfung innerstaatlicher Rechtsmittel geprüft (bei MSchG-Fällen)
- [ ] Prompt-Release-Verfahren nach UNCLOS Art. 292 erwogen
- [ ] Angemessene Sicherheitsleistung (bond) quantifiziert

## Relevante Rechtsprechung
- ITLOS M/V Saiga No. 2 (Saint Vincent v. Guinea 1999): genuine link; Flaggenstaat-Verantwortung.
- ITLOS Arctic Sunrise No. 22 (Netherlands v. Russia 2013): einstweilige Maßnahmen; Freilassung.
- ITLOS Juno Trader No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; verhältnismäßige Sicherheit.
- ITLOS Ukraine v. Russia No. 26 (2019): Kriegsschiffe; Immunität; Aussetzung.

## Quellen
- ITLOS Fallübersicht: https://www.itlos.org/en/main/cases/list-of-cases/
- UNCLOS Text: https://www.un.org/Depts/los/convention_agreements/texts/unclos/unclos_e.pdf
- ITLOS Statut Annex VI: https://www.un.org/Depts/los/convention_agreements/texts/unclos/annex6.htm
- BSH UNCLOS: https://www.bsh.de
- ITLOS Arctic Sunrise Case No. 22: https://www.itlos.org/en/main/cases/list-of-cases/

## 3. `see-020-dokumenten-cockpit-schiff`

**Fokus:** Mandant benoetigt Uebersicht aller schiffsrelevanten Dokumente: Registerauszug; Hypothekenurkunden; Zertifikate (Klasse; ISM/DOC/SMC; MLC/DMLC; ISPS/ISSC); Flaggenzertifikat; Charter; Konnossements-Template. SchRG §§ 2/8-74; FlaggRG §§ 3-5; ISM-Code; MLC 2006 Titel 5; ISPS-Code. Output: Dokumenten-Cockpit-Matrix und Faelligkeits-Kalender.

# Dokumenten-Cockpit Schiff – Vollständigkeitsprüfung

## Mandantenfall
Ein neuer Schiffsfinancier übernimmt ein Schiffsportfolio und benötigt eine sofortige Übersicht aller schiffsrelevanten Dokumente und deren Laufzeiten. Eine Reederei bereitet ein Schiff auf eine Charter vor und muss gegenüber dem Charterer alle Zertifikate nachweisen. Ein Port-State-Control-Inspektor hat Mängel festgestellt; welche Dokumente fehlen oder sind abgelaufen?

## Erste Schritte
1. Registerdokumente beschaffen: Seeschiffsregisterauszug; Hypothekenurkunde; Eigentumsnachweis.
2. Sicherheits-Zertifikate sichten: Klasse-Zertifikat (Classification Certificate); Sicherheitszeugnis (Safety Certificate) nach SOLAS.
3. ISM-Dokumente: DOC (Document of Compliance) für Reederei; SMC (Safety Management Certificate) für Schiff; Gültigkeitsdaten prüfen.
4. MLC-Dokumente: DMLC (Declaration of Maritime Labour Compliance) Part I und Part II; MLC-Zertifikat.
5. Umweltzertifikate: IOPP (International Oil Pollution Prevention) Certificate; IAPP (Air Pollution Prevention); Ballastwasser-Zertifikat.
6. Flaggenzertifikat und Fahrterlaubnis: FlaggRG §§ 3-5; BSH-Fahrterlaubnisnachweis; Schiffssicherheitsfunkzeugnis.

## Rechtsrahmen
- SchRG §§ 2/8-74: Eigentums- und Hypothekendokumentation im Schiffsregister.
- FlaggRG §§ 3-5: Flaggenzertifikat als Nachweis des Flaggenführungsrechts.
- ISM-Code Kap. 1-13: DOC (Reederei) und SMC (Schiff) als Pflicht-Zertifikate nach SOLAS Kap. IX.
- MLC 2006 Titel 5 Reg. 5.1.3: MLC-Zertifikat und DMLC als Pflichtunterlagen.
- ISPS-Code: ISSC (International Ship Security Certificate) als Nachweis des Sicherheitsplans.
- MARPOL Annex I/II/VI: IOPP-; IONPP-; IAPP-Zertifikate für Umweltzertifizierung.

## Prüfraster
- Sind alle SOLAS-Pflichtzertifikate gültig und aktuell?
- Ist das ISM-DOC auf das richtige Unternehmen ausgestellt?
- Stimmen DMLC Part I (Flaggenstaat) und Part II (Reeder) überein?
- Sind alle Zertifikate für das aktuelle Fahrtgebiet gültig?
- Ist ein Faelligkeits-Kalender mit allen Erneuerungsdaten vorhanden?

## Typische Fallstricke
- DOC auf falsches Unternehmen ausgestellt; ISM-Verantwortung liegt tatsächlich woanders.
- MLC-Zertifikat abgelaufen; PSC-Detention droht beim ersten Hafenanlauf.
- IOPP-Zertifikat nicht aktualisiert nach Maschinenraumänderungen.
- Ballastwasser-Zertifikat fehlt; seit 2017 IMO-Pflicht für alle internationalen Fahrten.

## Output
- Dokumenten-Cockpit-Matrix: Dokument; Ausstelldatum; Ablaufdatum; Aussteller; Status
- Fälligkeits-Kalender für alle 12 Monate
- Checkliste Dokumente für PSC-Inspektion
- Lücken-Report mit Maßnahmenplan


## Erweiterte Normengrundlage

### Zertifizierungspflichten
- ISM-Code Kap. 3-4: DOC für den Reeder; SMC für das Schiff; Prüfungsintervalle.
- MLC 2006 Reg. 5.1.3: DMLC Part I (Behörde) und Part II (Reeder); Gültigkeit; Erneuerung.
- ISPS-Code Part B § 1.3: ISSC-Ausstellung durch Flaggenstaat oder RO.

### Klassenwesen
- SOLAS Kap. II-1 Reg. 3-1: Klassenpflicht; periodische Besichtigung (Annual; Special; Drydock).
- Kl-Reg. (DNV/BV/LR/ABS): Klassen-Statuten; Auflagen; Conditionen.

## Checkliste Dokumenten-Cockpit
- [ ] Klassenzertifikat: Ausstellungsdatum; Ablaufdatum; nächste Annual Survey
- [ ] ISM DOC: Reeder; Gültigkeitsdauer; letztes Audit
- [ ] ISM SMC: Schiff; Gültigkeitsdauer; letztes Audit
- [ ] DMLC Part I und II: gültig; ggf. Endorsement nach Flaggenwechsel
- [ ] ISSC (ISPS): gültig; letzter PFSO-Kontakt
- [ ] IOPP Certificate (MARPOL): gültig
- [ ] ENG1-/MED-Zeugnisse der Besatzung aktuell
- [ ] Klassen-Auflagen (Conditions of Class) dokumentiert und erfüllt

## Relevante Rechtsprechung
- OLG Hamburg zur Haftung des Reeders bei Ablauf des SMC; ISM-Code als Sorgfaltsmaßstab.
- BGH zur Relevanz des Klassenzertifikats für die H&M-Versicherungsdeckung.
- BVerwG zur Befugnis des BSH; abgelaufene Zertifikate führen zum Anhalten des Schiffes.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- ISM-Code BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/ISM_Code/ism_code_node.html
- MLC ILO: https://www.ilo.org/dyn/normlex/en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C186
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- MARPOL IMO: https://www.imo.org/en/About/Conventions/Pages/International-Convention-for-the-Prevention-of-Pollution-from-Ships-(MARPOL).aspx

## 4. `see-021-schiffshypothek-register-pruefen`

**Fokus:** Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank prueft Seeschiffsregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte.

# Schiffshypothek – Registerprüfung

## Mandantenfall
Eine finanzierende Bank prueft den Seeschiffsregister vor Auszahlung eines Kredits fuer ein hypothekenbelastetes Seeschiff. Ein Investor will Eigentuemerstellung und Lastenfreiheit bestaetigt haben. Ein Insolvenzverwalter erstellt die Glaeubigerliste fuer die Masse.

## Erste Schritte
1. Aktuellen Registerauszug (Seeschiffsregister) beim zustaendigen Gericht beschaffen.
2. Eigentuemerstellung (Abt. I) pruefen; Verkaeufereigenschaft bestaetigen.
3. Hypothekenabteilung (Abt. II): Betrag, Rang, Glaeubiger und Faelligkeit.
4. Gesetzliche Vorrechte identifizieren (HGB §§ 596-601 oder BinSchG §§ 102-116).
5. Arrest- und Pfaendungsvermerke sichten; Zeitpunkt der Eintragung beachten.
6. Registerpruefprotokoll erstellen; Rangkarte und Risikoampel ausgeben.

## Rechtsrahmen
- SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte; SchRegO §§ 3-19 Registerführung; BGB §§ 892-893 Gutglaubensschutz im Register. Rangfolge Hypotheken; Absonderung InsO §§ 49-51.

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Verkäufer des hypothekenbelastetes Seeschiffs überein?
- Sind alle Hypotheken mit aktuellem Valutierungsstand bei Gläubigern abgeglichen?
- Bestehen gesetzliche Vorrechte, die Hypotheken im Rang verdrängen?
- Gibt es Arrest- oder Pfändungsvermerke im Register?
- Sind Löschungsvoraussetzungen für alle Altlasten erfüllt?

## Typische Fallstricke
- Gesetzliche Vorrechte (Crew-Löhne, Hafengebühren) entstehen ohne Registereintragung.
- Voreintragungspflicht: Veräußerer muss im Seeschiffsregister eingetragen sein.
- Bei hypothekenbelastetes Seeschiff unter Auslandsflagge gilt Lex registri des Flaggenstaats.

## Output
Registerprüfprotokoll mit Abteilungsübersicht und Rangkarte für hypothekenbelastetes Seeschiff.


## Vertiefung: Registerrechtliche Besonderheiten
Das Schiffsregister ist ein öffentliches Register im Sinne des SchRG § 3; es gilt das Prinzip der positiven und negativen Publizität (BGB §§ 892-893 analog). Ein gutgläubiger Erwerber kann sich auf den Registerinhalt verlassen, soweit keine Eintragungsvoraussetzungen fehlen. Bei internationalen Transaktionen ist die Anerkennung ausländischer Schiffshypotheken nach dem Recht des Registerstaats (Lex registri) zu prüfen; dies gilt insbesondere für Schiffe unter Panama-, Marshall-Islands- oder Liberia-Flagge.

## Verfahrensablauf Registerprüfung
Die Registerprüfung erfolgt in drei Phasen:
1. **Formelle Prüfung**: Ist das Schiff eingetragen; ist die Eintragungsnummer korrekt; liegt das Schiffsregisterblatt vollständig vor?
2. **Materielle Prüfung**: Inhalt der Abteilungen I bis III; Rangfolge der Einträge; Zeitstempel.
3. **Risikoanalyse**: Bewertung der Restrisiken; gesetzliche Schiffsgläubigerrechte die außerhalb des Registers entstehen; Fristen für Löschungsanträge.

## Praktische Hinweise
Registerauszüge sind nur tagesaktuell belastbar; kurzfristige Nachtragsanfragen sicherstellen. Bei komplexen Portfolien ist ein automatisiertes Monitoring sinnvoll. Die Kosten für den Registerauszug betragen je nach Registergericht wenige Euro; Notargebühren für beglaubigte Ausfertigungen fallen zusätzlich an.


## Checkliste Registerprüfung
- [ ] Registerauszug Abteilung I: Schiffsname; IMO-Nummer; Flagge; Eigentümer; Datum der Eintragung
- [ ] Registerauszug Abteilung II: alle Hypotheken; Rangstellen; Gläubiger; Nennbeträge; Eintragungsdaten
- [ ] Registerauszug Abteilung III: Arreste; Pfändungen; sonstige Verfügungsbeschränkungen
- [ ] Gesetzliche Schiffsgläubigerrechte (HGB §§ 596-601) abgefragt: Crew-Löhne; Hafengebühren; Bergungskosten
- [ ] Valutierungsauszüge aller Hypothekengläubiger vorliegend
- [ ] Löschungsbewilligungen für alle abzulösenden Lasten gesichert
- [ ] Negativattest: keine weiteren Lasten oder Verfügungsbeschränkungen bekannt

## Relevante Rechtsprechung
- BGH zur Rangfolge von Schiffsgläubigerrechten und Hypotheken; Absonderung in der Insolvenz des Reeders.
- ITLOS M/V Saiga Case No. 2 (Saint Vincent and the Grenadines v. Guinea 1999): Flaggenstaat-Verantwortung; genuine link UNCLOS Art. 91.
- Landgericht Hamburg; Beschlüsse zu Schiffsarrest und Registervormerkung; abrufbar über openjur.de.

## Normen im Überblick
- SchRG §§ 1-7: Anwendungsbereich; Eintragungsfähigkeit; Definition Schiff.
- SchRG §§ 8-30: Schiffshypothek; Entstehung; Bestellung; Übertragung.
- SchRG §§ 31-58: Inhalt; Umfang; Erstreckung auf Zubehör und Forderungen.
- SchRG §§ 59-74: Rang und Konkurrenz mehrerer Hypotheken.
- SchRG § 75: Höchstbetragshypothek.
- SchRG §§ 76-104: Schiffbauwerkshypothek.
- HGB §§ 596-601: gesetzliche Schiffsgläubigerrechte mit gesetzlichem Pfandrecht.


## Vertiefung Registerrecht

### Schiffsregister und Grundbuchrecht im Vergleich
Das Schiffsregister folgt dem Grundbuchrecht (BGB §§ 873; 925) mit schiffsspezifischen Modifikationen durch das SchRG. Die Eintragung ist konstitutiv für die Entstehung von Schiffshypotheken. Gutgläubiger Erwerb ist möglich, wenn der Erwerber auf den Registerinhalt vertraut (SchRG § 3). Die öffentliche Urkunde (Registerauszug) gilt als Beweis für den eingetragenen Inhalt.

### Internationaler Bezug
Ausländische Schiffsregisterauszüge sind im deutschen Rechtsverkehr anerkannt, wenn sie von der zuständigen Auslandsbehörde ausgestellt und beglaubigt sind. Bei Flaggenwechsel ist die Löschung im alten Register und Neueintragung im neuen Register erforderlich (FlaggRG § 9).

## Normen-Synopse Register
| Norm | Inhalt |
|------|--------|
| SchRG § 1 | Eintragungsfähige Schiffe |
| SchRG § 8 | Entstehung der Hypothek |
| SchRegO § 8 | Eintragungsverfahren |
| HGB § 596 | Gesetzliche Vorrechte |

## Quellen
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- BSH Register: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- SchRegO: https://dejure.org/gesetze/SchRegO

## 5. `see-022-schiffshypothek-hypothek-bestellen`

**Fokus:** Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines hypothekenbelastetes Seeschiff. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste.

# Schiffshypothek – Schiffshypothek bestellen

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein hypothekenbelastetes Seeschiff als Sicherheit fuer einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein hypothekenbelastetes Seeschiff als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des hypothekenbelastetes Seeschiffs pruefen; Eintragung im Seeschiffsregister bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. Rangfolge Hypotheken; Absonderung InsO §§ 49-51.

## Prüfraster
- Ist das hypothekenbelastetes Seeschiff im Seeschiffsregister eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Seeschiffsregister-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Output
Checkliste Hypothekenbestellung und Unterlagen-Übersicht für hypothekenbelastetes Seeschiff.


## Vertiefung: Hypothekenarten im deutschen Schiffsrecht
Das SchRG kennt die Verkehrshypothek (§§ 8-30) und die Höchstbetragshypothek (§ 75). Die Verkehrshypothek ist an eine bestimmte Forderung gebunden; die Höchstbetragshypothek sichert variable Forderungen bis zu einem eingetragenen Maximalbetrag und eignet sich für revolvierende Kreditlinien. In der Praxis der Schiffsfinanzierung dominiert die Hypothekenbestellung als erstrangige Höchstbetragshypothek zugunsten der Konsortialführerbank.

## Verfahrensablauf Hypothekenbestellung
1. **Vor der Bestellung**: Eintragungsfähigkeit prüfen; Rangstelle reservieren (SchRegO § 13); Sicherungsabrede verhandeln.
2. **Bestellung**: Notarielle Bestellungsurkunde; Unterschriften des Eigentümers; Vollmachten (ggf. notariell beglaubigt).
3. **Eintragung**: Antrag beim Registergericht; Vorlage der Bestellungsurkunde; Eintragungsgebühr.
4. **Nach der Eintragung**: Registerauszug beschaffen; Sicherungsvertrag und Registerauszug archivieren; Mortgagee's Interest Insurance prüfen.

## Praktische Hinweise
In Konsortialkrediten hält eine Sicherheitentreuhänderin (Security Trustee) die Hypothek für alle Konsortialmitglieder. Die Hypothek kann jederzeit abgetreten werden (SchRG §§ 35-58); für die Abtretung ist Briefübergabe oder Eintragung erforderlich je nach Hypothekenart.


## Checkliste Hypothekenbestellung
- [ ] Eintragungsfähigkeit des Schiffes bestätigt (SchRG § 1)
- [ ] Eigentümer mit Vollmacht zur Hypothekenbestellung legitimiert
- [ ] Sicherungsabrede (Security Agreement / Credit Agreement) unterzeichnet
- [ ] Notarielle Hypothekenbestellungsurkunde erstellt und unterzeichnet
- [ ] Eintragungsantrag beim Registergericht gestellt; Rangstelle reserviert
- [ ] Mithaftung des Zubehörs (SchRG § 31) vertraglich vereinbart
- [ ] Eintragungsbestätigung und ggf. Hypothekenbrief gesichert
- [ ] Mortgagee's Interest Insurance (MII) beantragt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit der notariellen Hypothekenbestellungsurkunde; Formerfordernisse SchRG § 17.
- BGH zur Mithaftung des Zubehörs nach SchRG § 31; Abgrenzung Schiffszubehör von persönlichem Eigentum des Kapitäns.
- OLG Hamburg zur Rangfolge bei gleichzeitig beantragten Hypotheken; Zeitpunkt der Antragstellung maßgeblich.

## Normen im Überblick
- SchRG § 8: Begründung der Schiffshypothek durch Einigung und Eintragung.
- SchRG §§ 9-14: Inhalt der Eintragungsurkunde; Form; Unterschriften.
- SchRG §§ 15-18: Eintragungsvoraussetzungen; notarielle Form.
- SchRG §§ 35-58: Übertragung der Hypothek; Abtretung; Pfändung.
- SchRG § 59: Rangfolge; ältere Hypothek geht jüngerer vor.
- SchRG § 75: Höchstbetragshypothek für revolvierende Kredite.
- InsO § 49: Absonderungsrecht des Hypothekengläubigers in der Insolvenz des Reeders.

## Quellen
- SchRG §§ 8-18: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- SchRegO §§ 13-19: https://dejure.org/gesetze/SchRegO
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- dejure SchRG § 75: https://dejure.org/gesetze/SchRG/75.html
