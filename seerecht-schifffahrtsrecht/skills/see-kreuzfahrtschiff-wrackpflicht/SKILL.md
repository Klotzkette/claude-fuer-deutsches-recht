---
name: see-kreuzfahrtschiff-wrackpflicht
description: "SEE Kreuzfahrtschiff Wrackpflicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Kreuzfahrtschiff Wrackpflicht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Kreuzfahrtschiff Wrackpflicht** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-095-kreuzfahrtschiff-wrackpflicht-pruefen` | Kreuzfahrtschiff: Kreuzfahrtreeder; Passagier-Charterer; Passagierrechts-Klaeger analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Kreuzfahrtschiff oder grosses Fahrgastschiff. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. HGB §§ 536-556 Befoerderung von Reisenden; Athen-Uebereinkommen 2002; SOLAS Kap. III. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk. |
| `see-096-kreuzfahrtschiff-versicherung-melden` | Kreuzfahrtschiff: Schadensereignis an Kreuzfahrtschiff oder grosses Fahrgastschiff melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht. |
| `see-097-kreuzfahrtschiff-local-counsel-instrui` | Kreuzfahrtschiff: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei Kreuzfahrtschiff oder grosses Fahrgastschiff im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste. |
| `see-098-kreuzfahrtschiff-closing-planen` | Kreuzfahrtschiff: Closing eines Kreuzfahrtschiff oder grosses Fahrgastschiff-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan. |
| `see-099-kreuzfahrtschiff-klagepfad-waehlen` | Kreuzfahrtschiff: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um Kreuzfahrtschiff oder grosses Fahrgastschiff: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Kreuzfahrtschiff Wrackpflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-095-kreuzfahrtschiff-wrackpflicht-pruefen`

**Fokus:** Kreuzfahrtschiff: Kreuzfahrtreeder; Passagier-Charterer; Passagierrechts-Klaeger analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Kreuzfahrtschiff oder grosses Fahrgastschiff. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. HGB §§ 536-556 Befoerderung von Reisenden; Athen-Uebereinkommen 2002; SOLAS Kap. III. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk.

# Kreuzfahrtschiff – Wrackbeseitigungspflicht prüfen

## Mandantenfall
Ein Kreuzfahrtschiff oder grosses Fahrgastschiff sinkt in deutschen Gewässern; WSA ordnet Beseitigung an; Eigentümer fragt nach Haftung. Die finanzierende Bank fragt, ob sie als Hypothekengläubigerin haftet. Ein Reeder ist insolvent; Behörde will Kosten beim letzten Eigentümer eintreiben.

## Erste Schritte
1. WRC 2007 / WSG Anwendbarkeit pruefen: Kreuzfahrtschiff oder grosses Fahrgastschiff ab 300 BRZ in deutschen Gewaessern.
2. Verantwortlichen identifizieren: WSG § 2 - Eigentuemer des {vessel} haftet primaer.
3. Behoerdliche Meldepflicht (WRC Art. 5 / WSG § 4): unverzuegliche Meldung beim WSA.
4. Versicherungsnachweis (WRC Art. 12): Pflicht ab 300 BRZ; P&I-Club-Zertifikat vorlegen.
5. Kostenschaetzung einholen: Bergungsunternehmen; Umweltschadensrisiko bewerten.
6. Notfallmassnahmen koordinieren: BSH-Schadstoffabwehr; Buenker-Oelbergung.

## Rechtsrahmen
- WSG §§ 1-12 Wrackbeseitigungsgesetz; WRC 2007 Nairobi Art. 1-12; MARPOL Annex I Reg. 26.

## Prüfraster
- Ist der Eigentuemer des Kreuzfahrtschiff oder grosses Fahrgastschiff bekannt und zahlungsfaehig?
- Greift WRC 2007 (Schiff ab 300 BRZ; Gewaesser eines Vertragsstaats)?
- Ist Wrackbeseitigungs-Versicherung vorhanden (WRC Art. 12)?
- Ueberschreiten Wrackkosten den Schiffswert?
- Bestehen Umweltschadensrisiken (Bunkeröl/Chemikalien) beim Kreuzfahrtschiff oder grosses Fahrgastschiff?

## Typische Fallstricke
- WRC gilt auch fuer Freizeitjachten ab 14 Meter Laenge.
- Behoerdliche Ersatzvornahme begründet Kostenerstattungsanspruch mit Vorrang.
- Bei Kreuzfahrtschiff oder grosses Fahrgastschiff unter Auslandsflagge kommen Flaggenstaat-Pflichten hinzu.

## Output
WRC-Pflichtenanalyse und Kostenrisiko-Vermerk für Kreuzfahrtschiff oder grosses Fahrgastschiff.


## Vertiefung: Nairobi WRC 2007 im Überblick
Das Nairobi Wrack-Übereinkommen (WRC 2007) trat international 2015 in Kraft; Deutschland hat es 2013 ratifiziert und durch das Wrackbeseitigungsgesetz (WSG) umgesetzt. Es gilt für Wracks in der AWZ und dem Küstenmeer von Vertragsstaaten; für Wracks auf der Hohen See gelten nur nationale Normen. Kernpflicht: Eigentümer muss das Wrack melden; markieren; und beseitigen oder beseitigen lassen.

## Haftungsstruktur
Primär haftet der eingetragene Eigentümer; sekundär können Hypothekengläubiger oder faktische Betreiber herangezogen werden. Die Haftung ist nicht automatisch durch Schiffswert begrenzt; das Haftungsbeschränkungsrecht nach HGB §§ 611-617 oder LLMC 1976/1996 kann aber Obergrenzen setzen. P&I-Clubs decken Wrackbeseitigungskosten typischerweise im Rahmen der Pollution-Deckung ab.

## Behördliche Zuständigkeit
In Deutschland ist das Wasserstraßen- und Schifffahrtsamt (WSA) die zuständige Behörde (§ 4 WSG). Bei Gefahr für Menschenleben oder Umwelt kann das WSA sofortige Maßnahmen anordnen und auf Kosten des Eigentümers durchführen. Das BSH koordiniert Schadstoffabwehrmaßnahmen auf See.


## Checkliste Wrackpflicht-Prüfung
- [ ] Lage des Wracks bestimmt: AWZ; Küstenmeer; Binnengewässer
- [ ] Anwendbarkeit WRC 2007 / WSG geprüft: Schiff ab 300 BRZ; Vertragsstaaten-Gewässer
- [ ] Eigentümer identifiziert; Kontakt aufgenommen
- [ ] Meldung beim WSA erfolgt (WSG § 4 / WRC Art. 5)
- [ ] Wrackbeseitigungs-Versicherungsnachweis angefordert (WRC Art. 12)
- [ ] Kostenschätzung für Bergung eingeholt
- [ ] Umweltgefährdung durch Bunkeröl oder Schadstoffe bewertet
- [ ] BSH Schadstoffabwehr informiert
- [ ] Haftungsstruktur analysiert: Eigentümer; Hypothekengläubiger; Versicherer

## Relevante Rechtsprechung
- BGH zur Ersatzvornahme bei Wrackbeseitigung; Kostenerstattungsanspruch der Behörde gegen Eigentümer.
- VG Hamburg und VG Stade zur Behördenzuständigkeit für Wrackbeseitigung in der AWZ.
- ITLOS Advisory Opinion No. 17 (Seabed Disputes Chamber 2011): Pflichten der Sponsoring States für Tätigkeiten im Meeresgebiet.

## Normen im Überblick
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers; Behördenzuständigkeit; Kosten.
- WRC 2007 Art. 1-16: Definitionen; Anwendungsbereich; Meldepflichten; Versicherungspflicht; Haftung.
- MARPOL Annex I Reg. 26: Bunkeröl-Sicherheitsmaßnahmen bei Schiffskatastrophen.
- HGB § 611: Haftungsbeschränkung des Schiffseigentümers nach LLMC 1976/1996.
- InsO §§ 49-51: Absonderungsrecht des Hypothekengläubigers; Haftungsfreistellung.


## Vertiefung Wrackbeseitigung

### Behördliche Struktur
In der AWZ ist das BSH (Bundesamt für Seeschifffahrt und Hydrographie) zuständig; im Küstenmeer und den Seewasserstraßen die WSA (Wasserstraßen- und Schifffahrtsämter). Die Zuständigkeit ist für die Einschätzung des Vollzugsrisikos entscheidend.

### Versicherungspflicht nach WRC 2007
Ab 300 BRZ besteht eine Pflichtversicherung für Wrackbeseitigungskosten (WRC Art. 12); der Nachweis muss an Bord mitgeführt werden. Deutschland hat das WRC 2007 ratifiziert (BGBl. 2013 II Nr. 22).

## Normen-Synopse Wrackbeseitigung
| Norm | Inhalt |
|------|--------|
| WSG § 1 | Anwendungsbereich |
| WSG § 4 | Meldepflicht |
| WRC Art. 12 | Versicherungspflicht |
| MARPOL Annex I | Bunkerölsicherheit |

## Quellen
- WSG: https://www.gesetze-im-internet.de/wsg/
- WRC 2007 IMO: https://www.imo.org/en/About/Conventions/Pages/Nairobi-International-Convention-on-the-Removal-of-Wrecks.aspx
- BSH: https://www.bsh.de
- MARPOL IMO: https://www.imo.org/en/About/Conventions/Pages/International-Convention-for-the-Prevention-of-Pollution-from-Ships-(MARPOL).aspx

## 2. `see-096-kreuzfahrtschiff-versicherung-melden`

**Fokus:** Kreuzfahrtschiff: Schadensereignis an Kreuzfahrtschiff oder grosses Fahrgastschiff melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht.

# Kreuzfahrtschiff – Schadensfall bei Versicherung melden

## Mandantenfall
Ein Kreuzfahrtschiff oder grosses Fahrgastschiff erleidet Kollisionsschäden; P&I-Club und H&M-Versicherer werden koordiniert informiert. Ein Reeder verzögert die Schadensmeldung; Versicherer beruft sich auf VVG § 28 Obliegenheitsverletzung. Eine Bank aktiviert MII-Police nach Totalverlust eines hypothekenbelasteten Kreuzfahrtschiff oder grosses Fahrgastschiff.

## Erste Schritte
1. P&I-Club sofort informieren; Korrespondenten vor Ort aktivieren.
2. H&M-Versicherer (Kasko) unverzueglich benachrichtigen; DTV-Fristen beachten.
3. MII-Police der Bank aktivieren, sofern Hypothekenglaeubigerbank betroffen.
4. Schadensdokumentation: Fotos; Sachverstaendige; Logbuecher; Klassenachricht sichern.
5. Schadensminderungspflicht (VVG § 82): Notmassnahmen veranlassen und dokumentieren.
6. Alle Beteiligten koordinieren: P&I; H&M; MII; Klassifikator; Versicherungsmakler.

## Rechtsrahmen
- VVG §§ 28-30 Obliegenheiten; VVG § 82 Schadensminderung; DTV-Klauseln Kasko 2009; IGP&I Club Rules.

## Prüfraster
- Ist Meldung fristgerecht an alle Versicherer erfolgt?
- Sind Schadensminderungsmassnahmen dokumentiert?
- Greift MII-Police der Bank; sind alle Voraussetzungen erfuellt?
- Liegt ein Deckungswiderspruch zwischen H&M und P&I vor?
- Ist der Klassifikator informiert; droht Klasse-Suspension?

## Typische Fallstricke
- Verspaetete P&I-Meldung fuehrt zu Deckungsverlust (Club Rule: prompt notification).
- MII greift nur wenn Bank nicht als Mitversicherter in H&M-Police steht.
- H&M deckt nur 3/4 der Kollisionshaftung; P&I nimmt 1/4.

## Output
Meldecheckliste (P&I/H&M/MII) und Fristenübersicht für Kreuzfahrtschiff oder grosses Fahrgastschiff.


## Vertiefung: P&I-Club-Meldesystem
P&I-Clubs arbeiten nach dem Mutual-Insurance-Prinzip: Mitglieder (Reeder) sichern sich gegenseitig ab; Prämien werden nachträglich angepasst. Für die Deckungsauslösung entscheidend ist die prompte Meldung an den zuständigen Club-Korrespondenten im Hafenstaat. Alle 13 IG-Clubs haben weltweite Korrespondentennetzwerke; im Schadenfall sofort aktivieren.

## Koordination mehrerer Versicherer
Bei einem Schiffsunfall sind typischerweise beteiligt: H&M-Versicherer (Schaden am eigenen Schiff); P&I-Club (Drittschäden; Personenschäden; Umwelt); ggf. War-Risk-Versicherer (politische Risiken); Cargo-Versicherer der Ladung (vom Befrachter beauftragt). Koordination ist essenziell um Deckungslücken und Doppelerstattungen zu vermeiden.

## Beweissicherung nach Schadensereignis
Unmittelbare Maßnahmen: Unfallstelle fotografieren; beschädigte Teile sichern; Zeugenaussagen protokollieren; Logbücher und Stundenbücher sofort sichern und beglaubigen lassen. Externe Gutachter (Havariekommissar; Klasseninspektor; P&I-Club-Surveyor) sind unverzüglich zu bestellen. Digitale Daten (AIS; VDR; ECDIS) sichern und auf Backup-Medien kopieren.


## Checkliste Schadensmeldung
- [ ] P&I-Club-Korrespondent am Schadensort informiert (innerhalb 24 Stunden)
- [ ] H&M-Versicherer unverzüglich benachrichtigt; DTV-Fristen eingehalten
- [ ] MII-Police der Bank aktiviert (wenn Hypothekengläubiger betroffen)
- [ ] Schadensdokumentation vollständig: Fotos; Gutachter; Logbücher; Zeugenaussagen
- [ ] Schadensminderungsmaßnahmen veranlasst und dokumentiert (VVG § 82)
- [ ] Klasseninspektor bestellt; ggf. Klasse-Suspension akzeptiert
- [ ] Alle Versicherer koordiniert; Deckungsüberschneidungen geklärt
- [ ] Aufräumungskosten aus P&I-Pollution-Deckung angemeldet

## Relevante Rechtsprechung
- BGH zur Obliegenheitsverletzung (VVG § 28) bei Schiffsversicherung; Kausalitätsgegenbeweis.
- OLG Hamburg zu P&I-Deckungsversagung bei verspäteter Meldung; Club-Rule-Auslegung.
- BGH zu Mortgagee's Interest Insurance; Verhältnis zur H&M-Police; Schutzbereich.

## Normen im Überblick
- VVG § 28: Verletzung vertraglicher Obliegenheiten; Leistungsfreiheit bei Vorsatz; Leistungskürzung bei grober Fahrlässigkeit.
- VVG § 78: Mehrfachversicherung; Gesamtschuldner der Versicherer; Ausgleich.
- VVG § 82: Schadensminderungsobliegenheit; Aufwendungsersatz für Rettungskosten.
- VVG §§ 130-136: Haftpflichtversicherung; Direktklagerecht des Geschädigten.
- DTV-Klauseln Kasko 2009 § 2: versicherte Gefahren und Schäden; Selbstbehalte.


## Vertiefung Schadensmeldung

### Koordination der Versicherer
Bei einem Kaskoschaden sind in der Regel mehrere Versicherer betroffen: H&M-Versicherer für den Sachschaden; P&I-Club für die Haftpflicht gegenüber Dritten; MII für den Hypothekengläubiger. Die Koordination ist Aufgabe des Schiffsanwalts.

### Subrogation
Der H&M-Versicherer, der den Schaden reguliert hat, tritt in die Forderungen des Reeders gegen den Schädiger ein (VVG § 86). Der P&I-Club zahlt nur nach dem Pay-to-be-Paid-Prinzip; der Reeder muss den Schaden erst selbst zahlen und wird dann vom Club erstattet.

## Normen-Synopse Versicherung
| Norm | Inhalt |
|------|--------|
| VVG § 28 | Obliegenheitsverletzung |
| VVG § 82 | Schadensminderung |
| VVG § 86 | Forderungsübergang |
| DTV-Kasko 2009 | Versicherte Gefahren |

## Quellen
- VVG §§ 28-30: https://www.gesetze-im-internet.de/vvg/__28.html
- DTV-Klauseln Kasko: https://www.deutscher-transport-versicherungsverband.de
- IGP&I: https://www.igpandi.org
- openjur P&I-Streit: https://www.openjur.de

## 3. `see-097-kreuzfahrtschiff-local-counsel-instrui`

**Fokus:** Kreuzfahrtschiff: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei Kreuzfahrtschiff oder grosses Fahrgastschiff im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste.

# Kreuzfahrtschiff – Local Counsel instruieren

## Mandantenfall
Ein Kreuzfahrtschiff oder grosses Fahrgastschiff liegt in einem ausländischen Hafen; lokaler Arrest ist erforderlich. Eine Hypothekenbank braucht Auskunft zur Vollstreckbarkeit ihrer deutschen Sicherheit im Ausland. Ein P&I-Club braucht nach Unfall lokale Rechtsvertretung für das Kreuzfahrtschiff oder grosses Fahrgastschiff.

## Erste Schritte
1. Local Counsel auswaehlen: Empfehlung durch P&I-Club-Korrespondenten oder Netzwerk.
2. Briefing erstellen: Kreuzfahrtschiff oder grosses Fahrgastschiff-Daten (IMO-Nummer; Flagge); Sachverhalt; deutsches Recht.
3. Lokale Rechtslage abfragen: Vollstreckungsanforderungen; Anerkennung deutscher Titel.
4. ISAC-1952-Pruefung: Ist Hafenstaat Vertragsstaat?
5. Letter of Instruction verfassen: Weisungen; Budget; Berichtspflichten.
6. P&I-Club koordinieren: liegt LOU-Angebot vor; macht es Arrest entbehrlich?

## Rechtsrahmen
- ISAC 1952 Art. 1; EuGVVO 2012 Recast EU-Vollstreckung; UNCLOS Art. 292 Prompt Release; SchRG §§ 8-74.

## Prüfraster
- Ist der Hafenstaat ISAC-1952-Vertragsstaat?
- Sind deutsche Urteile im Hafenstaat anerkennungsfaehig?
- Hat Local Counsel Erfahrung mit Seerecht und Kreuzfahrtschiff?
- Liegt ein LOU des P&I-Clubs vor?
- Ist der Kostenrahmen fuer das Auslandsverfahren freigegeben?

## Typische Fallstricke
- Lokale Seepfandrechte koennen deutsche Hypothek im Rang ueberbieten.
- Kostenunterschaetzung: Auslandsverfahren dauern laenger und kosten mehr.
- LOU-Verhandlungen erfordern erfahrenen Local Counsel.

## Output
Local-Counsel-Briefing für Kreuzfahrtschiff oder grosses Fahrgastschiff und Prioritätenliste.


## Vertiefung: Netzwerk-Aufbau und Koordination
P&I-Clubs unterhalten weltweit Netzwerke von Korrespondenten und Local Counsel (LoC). Bei Arrestsachen ist der LoC am Liegeplatz des Schiffes entscheidend; er kennt lokale Verfahrensvorschriften und Richter. Bei Vollstreckungsurteilen ist der LoC im Staat des zu vollstreckenden Urteils zuständig. Für EU-Staaten erleichtert die EuGVVO 2012 die Anerkennung.

## Briefing-Elemente
Ein effektives LoC-Briefing enthält: Kurzdarstellung des Sachverhalts (max. 2 Seiten); Kopien der relevanten Verträge; Registerauszug; Arrestbeschluss oder Urteil; Vollmacht; Budgetrahmen; Kommunikationsweg (verschlüsselte E-Mail). Zeitkritische Fragen sofort priorisieren; Arrest läuft schnell ab.

## Kostenkontrolle und Abrechnung
LoC-Anwälte rechnen nach nationalem Recht ab: in England nach Stundensätzen; in Deutschland nach RVG oder Stundensatz. Vorab Kostenvoranschlag und Budgetgenehmigung einholen. P&I-Club trägt die Anwaltskosten in der Regel; vorher Freigabe bestätigen lassen (Club Approval).


## Checkliste Local-Counsel-Beauftragung
- [ ] Local Counsel ausgewählt (Empfehlung P&I-Club-Korrespondent)
- [ ] Erfahrung des LoC mit Seerecht im Hafenstaat bestätigt
- [ ] Vollmacht ausgestellt und übermittelt
- [ ] Briefing-Dokument erstellt: Schiffsdaten; Sachverhalt; deutsches Recht
- [ ] Budgetrahmen genehmigt (P&I-Club-Approval)
- [ ] Berichtspflichten und Eskalationsweg definiert
- [ ] Prüfung ob LOU des P&I-Clubs den Arrest entbehrlich macht
- [ ] ISAC-1952-Status des Hafenstaats geprüft

## Relevante Rechtsprechung
- ITLOS Arctic Sunrise Case No. 22 (Netherlands v. Russia 2013): einstweilige Maßnahmen nach UNCLOS Art. 290; Freilassung des Schiffes.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release nach Art. 292; angemessene Sicherheitsleistung.
- EuGH zur EuGVVO 2012; gegenseitige Anerkennung von Vollstreckungstiteln in der EU.

## Normen im Überblick
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest; Verfahren; Vertragsstaat-Liste.
- EuGVVO 2012 Recast Art. 35-57: Vollstreckung ausländischer Titel in der EU.
- UNCLOS Art. 292: Prompt Release; Schiff und Crew freizulassen gegen angemessene Sicherheit.
- ZPO §§ 722-723: Vollstreckbarerklärung ausländischer Urteile in Deutschland.
- Anerkennungs- und Vollstreckungsausführungsgesetz (AVAG): nationale Umsetzung EuGVVO.


## Vertiefung Local Counsel

### Vollmacht und Briefing
Die Vollmacht für den Local Counsel sollte eine Generalvollmacht für alle prozessualen Handlungen enthalten. Das Briefing-Memorandum muss das Kernsachverhalt auf Englisch zusammenfassen; Local Counsel im Ausland arbeitet selten auf Basis deutschsprachiger Unterlagen.

### Koordination P&I-Club
Der P&I-Club hat eigene Netzwerke von Correspondenten und Local Counsel. Die Kosten sind i.d.R. durch die P&I-Deckung gedeckt; eine vorab Budgetfreigabe ist erforderlich.

## Normen-Synopse Local Counsel
| Norm | Inhalt |
|------|--------|
| ISAC 1952 Art. 1 | Seeforderungen |
| UNCLOS Art. 292 | Prompt Release |
| EuGVVO Art. 35 | EU-Vollstreckung |
| NYÜ 1958 | Schiedssprüche |

## Quellen
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- EuGVVO: https://dejure.org/gesetze/EuGVVO
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- openjur Vollstreckung Ausland: https://www.openjur.de

## 4. `see-098-kreuzfahrtschiff-closing-planen`

**Fokus:** Kreuzfahrtschiff: Closing eines Kreuzfahrtschiff oder grosses Fahrgastschiff-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan.

# Kreuzfahrtschiff – Closing planen

## Mandantenfall
Der Kauf eines Kreuzfahrtschiff oder grosses Fahrgastschiff soll abgeschlossen werden; Hypotheken sind abzulösen. Ein Käufer besteht auf lastenfreier Lieferung mit gültiger Klasse und MLC-Zertifikat. Eine Bank koordiniert das Closing bei syndizierten Finanzierungen.

## Erste Schritte
1. Ablosebetraege aller Hypothekenglaeubiger anfordern; Stichtag abstimmen.
2. Loeschungsbewilligungen (SchRG § 19) beschaffen; zeitlich koordinieren.
3. Escrow-Konto einrichten: Kaufpreis gegen Loeschungsbestaetigung.
4. Eigentumsuebergang (SchRG § 2) und Hypothekenloesung gleichzeitig fuer Kreuzfahrtschiff oder grosses Fahrgastschiff.
5. Zertifikate (Klasse; ISM; MLC; ISPS) auf neuen Eigentuemer ummelden.
6. Registerauszug nach Closing beschaffen; Closing-Memo erstellen.

## Rechtsrahmen
- SchRG §§ 2/19; SchRegO §§ 13-19; FlaggRG §§ 3-5; ISM-Code Kap. 3 SMC-Neuzertifizierung.

## Prüfraster
- Sind alle Loeschungsbewilligungen zeitlich koordiniert?
- Ist der Escrow-Mechanismus wasserdicht gegen Insolvenz des Verkaeufers?
- Sind alle Zertifikate fuer Kreuzfahrtschiff oder grosses Fahrgastschiff auf neuen Eigentuemer vorbereitet?
- Ist der Flaggenwechsel (wenn vorgesehen) vorbereitet?
- Ist die Vollmacht fuer den Registerantrag aktuell?

## Typische Fallstricke
- Zahlung ohne simultane Loeschung: Hypothek bleibt trotz Zahlung eingetragen.
- ISM-/MLC-Luecke nach Eigentumsuebergang; Port-State-Detention droht.
- Nachranghypotheken blockieren Closing wenn Erstrangglaeubigerbank nicht kooperiert.

## Output
Closing-Checkliste und Zeitplan mit Abhängigkeiten für Kreuzfahrtschiff oder grosses Fahrgastschiff.


## Vertiefung: Closing-Mechanismus im Schiffskauf
Das Closing eines Schiffskaufs ist der Moment wo Eigentum und Risiko auf den Käufer übergehen. Technisch besteht das Closing aus: (1) Zahlung des Kaufpreises (oder freigabe aus Escrow); (2) Übergabe der Delivery Documents; (3) Eintragung des Eigentumsübergangs im Schiffsregister (SchRG § 2). Alle drei Schritte sollen simultan erfolgen; in der Praxis nutzt man Softclose-Mechanismen.

## Delivery Documents Checkliste
Folgende Originalunterlagen müssen beim Closing übergeben werden: Klasse-Zertifikat; Delivery and Acceptance Certificate; Protokoll zur Übergabe von Bunker und Schmieröl; alle Schiffszertifikate (IOPP; IAPP; MLC; ISSC; BSH-Fahrterlaubnis); Logbücher; technische Handbücher. Kopien werden bei der abgebenden Reederei archiviert.

## Nachsorge nach dem Closing
Nach dem Closing: Neuanmeldung beim Flaggenregister; Beantragung neuer DOC beim ISM-Code-Unternehmen; MLC-Erneuerung; P&I-Club-Eintritt des Käufers; Benachrichtigung aller Charterer und Hafenbehörden über den Eigentümerwechsel. Closing-Memo erstellen mit Datum; Kaufpreis; alle übergebenen Dokumente; Beteiligten.


## Checkliste Closing-Vorbereitung
- [ ] Ablösebeträge aller Hypothekengläubiger angefordert; Stichtag fixiert
- [ ] Löschungsbewilligungen (SchRG § 19) von allen Gläubigern vorliegend
- [ ] Escrow-Konto eingerichtet; Escrow-Agent benannt
- [ ] Eigentumsübergang (SchRG § 2) und Hypothekenlöschung zeitlich koordiniert
- [ ] Alle Zertifikate (Klasse; ISM/DOC/SMC; MLC/DMLC; ISSC; BSH) auf neuen Eigentümer vorbereitet
- [ ] P&I-Club-Eintritt des Käufers bestätigt
- [ ] Delivery and Acceptance Certificate vorbereitet
- [ ] Registerauszug nach Closing beauftragt
- [ ] Closing-Memo-Vorlage bereitgestellt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit des Eigentumsübergangs an Schiffen; Einigung und Eintragung als konstitutive Voraussetzungen.
- OLG Hamburg zur Auslegung von Closing-Conditions in MOA-Verträgen; Delivery-Condition-Klauseln.
- BGH zur Haftung des Verkäufers für nach Closing entstehende Schiffsgläubigerrechte; Freistellungspflicht.

## Normen im Überblick
- SchRG § 2: Eigentumsübergang durch Einigung und Eintragung; nicht durch Besitzübergabe.
- SchRG § 19: Löschung der Hypothek; Form; Zeitpunkt; Wirkung.
- SchRegO §§ 13-19: Eintragungsverfahren; Antragsteller; Fristen.
- FlaggRG §§ 3-5: Berechtigung zur Flagge; Pflichten bei Eigentumsübergang.
- ISM-Code Kap. 3: SMC-Gültigkeit und Neuausstellung nach Eigentümerwechsel.
- MLC 2006 Reg. 5.1.3: Neuausstellung MLC-Zertifikat nach Eigentumsübergang und Flaggenwechsel.


## Vertiefung Closing

### Simultaneous Closing
Das "simultaneous closing" (Zug-um-Zug-Abwicklung) ist bei Schiffsverkäufen mit Kreditfinanzierung Standard. Ablöse der Altfinanzierung; Neuhypothek für den Käufer; Eigentumsumschreibung; Kaufpreiszahlung — alles erfolgt zeitgleich über ein Escrow-Konto.

### Zertifikatsübergang
Klasse- und ISM-Zertifikate bleiben nicht automatisch mit dem Schiff verbunden; sie sind personengebunden (SMC an den Reeder; DOC an den Betreiber). Der Käufer muss rechtzeitig seine eigene ISM-Zulassung (DOC) und das SMC für das Schiff beantragen.

## Normen-Synopse Closing
| Norm | Inhalt |
|------|--------|
| SchRG § 2 | Eigentumsübergang |
| SchRG § 19 | Hypothekenlöschung |
| FlaggRG § 3 | Flagge bei Eigentümerwechsel |
| MLC Reg. 5.1.3 | MLC-Zertifikat |

## Quellen
- SchRG §§ 2/19: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- FlaggRG: https://www.gesetze-im-internet.de/flaggrg/
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- SchRegO: https://dejure.org/gesetze/SchRegO

## 5. `see-099-kreuzfahrtschiff-klagepfad-waehlen`

**Fokus:** Kreuzfahrtschiff: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um Kreuzfahrtschiff oder grosses Fahrgastschiff: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose.

# Kreuzfahrtschiff – Klagepfad wählen

## Mandantenfall
Eine Bank will nach Kreditausfall aus der Hypothek am Kreuzfahrtschiff oder grosses Fahrgastschiff vollstrecken. Mehrere Gläubiger streiten um den Versteigerungserlös des Kreuzfahrtschiff oder grosses Fahrgastschiff. Ein Reeder prüft, ob ein freiwilliger Verkauf günstiger ist als die Zwangsversteigerung.

## Erste Schritte
1. Schiffswert des Kreuzfahrtschiff oder grosses Fahrgastschiff ermitteln: aktuelles Schätzgutachten beschaffen.
2. Glaeubigerrangfolge aufstellen: gesetzliche Vorrechte dann Hypotheken nach Rang.
3. ZPO §§ 864-871 Zwangsversteigerung: Zeitaufwand; Kosten; erwarteter Erloes.
4. Einvernehmlichen Verkauf pruefen: schneller und guenstiger wenn Reeder kooperiert.
5. Insolvenzantrag als taktisches Mittel: Arrests anderer Glaeubiger stoppen.
6. Schiedsklausel im Kreditvertrag pruefen: London Arbitration oder deutsches Gericht?

## Rechtsrahmen
- ZPO §§ 864-871 Zwangsversteigerung; InsO §§ 49-51 Absonderung; HGB §§ 596-601 Vorrangrechte; SchRG §§ 59-74 Rang.

## Prüfraster
- Uebersteigt Schiffswert des Kreuzfahrtschiff oder grosses Fahrgastschiff die Kreditvaluta?
- Gibt es erstrangige Vorrechte die den Erloes aufzehren?
- Ist einvernehmlicher Verkauf moeglich?
- Droht auslaendische Vollstreckung das deutsche Verfahren zu unterlaufen?
- Ist Insolvenzantrag taktisch sinnvoll?

## Typische Fallstricke
- Gesetzliche Schiffsglaeubigerrechte (Crew-Loehne/Hafen) fressen Erloes vor Hypotheken.
- Zwangsversteigerung dauert; Schiffswert sinkt durch Stillstand im Hafen.
- Auslaendische Arrests parallel zum deutschen Verfahren.

## Output
Klagepfad-Analyse und Erlösprognose (Tabelle Kosten vs. Erlös) für Kreuzfahrtschiff oder grosses Fahrgastschiff.


## Vertiefung: Gerichtsstand und Schiedsklauseln im Seerecht
Im deutschen Seerecht gilt für Schiffsarrest die ZPO § 919 (Gericht am Liegeplatz). Für streitige Klagen über Schiffshypotheken gilt ZPO § 29c (besonderer Gerichtsstand) oder der allgemeine Gerichtsstand. International ist London Arbitration (LMAA-Schiedsordnung) der Marktstandard für Charterparty-Streitigkeiten; Hamburg Arbitration (DIS-Regeln) ist eine deutsche Alternative.

## Vollstreckung ausländischer Urteile und Schiedssprüche
Ausländische Urteile aus EU-Staaten werden nach EuGVVO 2012 automatisch anerkannt; Vollstreckbarerklärung durch deutsches Gericht nötig. Ausländische Schiedssprüche werden nach dem New Yorker Übereinkommen 1958 (NYÜ) anerkannt; Deutschland ist Vertragsstaat. Einwendungen gegen Anerkennung: ordre public; fehlende Schiedsvereinbarung; Verletzung des rechtlichen Gehörs.

## Kostenabwägung Klage vs. Schiedsverfahren
Schiedsverfahren (London/Hamburg): höhere Kosten (Schiedsrichter-Honorare); aber schneller; vertraulicher; international vollstreckbarer. Ordentliches Gericht: günstigere RVG-Gebühren; aber Öffentlichkeit; Instanzenzug; schlechtere internationale Vollstreckbarkeit. Priorität: kurzfristige Sicherungsmaßnahmen (Arrest) immer vor ordentlichem Gericht; Hauptsacheverfahren nach Klausel.


## Checkliste Klagepfad-Entscheidung
- [ ] Aktueller Schiffswert gutachterlich ermittelt
- [ ] Gläubigerrangfolge aufgestellt (gesetzliche Vorrechte; Hypotheken; ungesicherte Gläubiger)
- [ ] Insolvenzwahrscheinlichkeit des Reeders bewertet
- [ ] Optionen verglichen: Zwangsversteigerung; einvernehmlicher Verkauf; Insolvenzantrag
- [ ] Schiedsklausel geprüft; Schiedsort und Schiedsregeln identifiziert
- [ ] Zeitlinie je Option: Wochen bis zur Verwertung; Kosten; Erlösprognose
- [ ] Entscheidung dokumentiert und von Entscheidungsträger genehmigt

## Relevante Rechtsprechung
- BGH zur Zwangsversteigerung von Seeschiffen; ZPO §§ 864-871; Verteilung des Erlöses.
- BGH zur Wirkung des Insolvenzantrags auf laufende Arrests und Pfändungen; InsO § 21.
- BGH zur LMAA-Schiedsklausel; Wirksamkeit in Deutschland; Vollstreckbarerklärung nach NYÜ.

## Normen im Überblick
- ZPO §§ 864-871: Zwangsversteigerung und Zwangsverwaltung eingetragener Schiffe.
- ZPO § 864: Gegenstand der Zwangsvollstreckung; Seeschiffe als unbewegliche Gegenstände.
- ZPO § 865: Beschlagnahme; Verfügungsverbot; Wirkung auf Charter-Zahlungen.
- InsO § 103: Wahlrecht des Insolvenzverwalters bei gegenseitigen Verträgen (Charter).
- InsO §§ 129-147: Insolvenzanfechtung; Tilgungen in der Krise rückforderbar.
- New Yorker Übereinkommen 1958: Anerkennung und Vollstreckung ausländischer Schiedssprüche.


## Vertiefung Klagepfad

### Zwangsversteigerung vs. Insolvenz
Die Zwangsversteigerung (ZPO §§ 864-871) ist effizienter, wenn das Schiff noch betrieben wird und einen Marktwert über den Hypotheken hat. Der Insolvenzantrag ist sinnvoller, wenn mehrere Schiffe betroffen sind oder der Reeder persönlich in die Haftung genommen werden soll.

### Schiedsgerichtsbarkeit
Schifffahrtssachen werden häufig vor dem LMAA (London Maritime Arbitrators Association) oder dem GMAA (German Maritime Arbitration Association) ausgetragen. LMAA-Schiedssprüche sind nach NYÜ 1958 in Deutschland vollstreckbar.

## Normen-Synopse Klagepfad
| Norm | Inhalt |
|------|--------|
| ZPO § 864 | Zwangsversteigerung |
| InsO § 103 | Charter-Wahlrecht |
| InsO § 49 | Absonderungsrecht |
| NYÜ 1958 | Schiedssprüche |

## Quellen
- ZPO §§ 864-871: https://dejure.org/gesetze/ZPO/864.html
- InsO §§ 49-51: https://www.gesetze-im-internet.de/inso/__49.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- BGH Zwangsversteigerung Schiff: https://www.bgh.de
