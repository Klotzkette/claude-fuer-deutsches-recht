---
name: see-schiffshypothek-arrest-wrackpflicht
description: "SEE Schiffshypothek Arrest Wrackpflicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Schiffshypothek Arrest Wrackpflicht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Schiffshypothek Arrest Wrackpflicht** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-024-schiffshypothek-arrest-vorbereiten` | Schiffshypothek: Glaeubiger sichert Anspruch an hypothekenbelastetes Seeschiff durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan. |
| `see-025-schiffshypothek-wrackpflicht-pruefen` | Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes hypothekenbelastetes Seeschiff. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk. |
| `see-026-schiffshypothek-versicherung-melden` | Schiffshypothek: Schadensereignis an hypothekenbelastetes Seeschiff melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht. |
| `see-027-schiffshypothek-local-counsel-instruie` | Schiffshypothek: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei hypothekenbelastetes Seeschiff im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste. |
| `see-028-schiffshypothek-closing-planen` | Schiffshypothek: Closing eines hypothekenbelastetes Seeschiff-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Schiffshypothek Arrest Wrackpflicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-024-schiffshypothek-arrest-vorbereiten`

**Fokus:** Schiffshypothek: Glaeubiger sichert Anspruch an hypothekenbelastetes Seeschiff durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan.

# Schiffshypothek – Arrest vorbereiten

## Mandantenfall
Ein Hypothekengläubiger will ein hypothekenbelastetes Seeschiff arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das hypothekenbelastetes Seeschiff im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des hypothekenbelastetes Seeschiff konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zustaendiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhoerung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das hypothekenbelastetes Seeschiff im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Output
Arrestantrags-Baustein (ZPO § 920) und Vollziehungs-Zeitplan für hypothekenbelastetes Seeschiff.


## Vertiefung: Internationale Seearrestpraxis
International koordinieren sich Gläubiger häufig über die 1952 Brüsseler Seearrest-Konvention (ISAC 1952) und über P&I-Club-Korrespondenten. In der EU gilt ergänzend die EuGVVO 2012 (Brüssel Ia-VO) für Vollstreckung und gegenseitige Anerkennung von Arrestbeschlüssen. In Drittstaaten gelten nationaler Seearrest-Regeln; Koordination mit Local Counsel ist unverzichtbar.

## Seeforderungen nach ISAC 1952 Art. 1
Zum Arrest berechtigende Seeforderungen umfassen: Schiffsbau- und -reparaturkosten; Schiffsausrüstung; Schifffahrtsabgaben; Frachtzahlungen; Charterzahlungen; Bergungskosten; Schiffsgläubigerrechte; Konnossementsansprüche; Kollisionshaftung; Hypothekenansprüche. Nicht erfasst sind Ansprüche aus reinem Landtransport ohne Seebezug.

## Verteidigungsstrategien des Schiffseigentümers
- **Letter of Undertaking (LOU)**: P&I-Club stellt ein formelles Versprechen aus das Schiff zu stellen; Arrest wird aufgehoben; Rechtsstreit geht weiter.
- **Gegenklage nach § 945 ZPO**: bei unberechtigtem Arrest; Schadensersatz für Liegekosten; entgangene Fracht; Reparaturkosten.
- **Sofortige Sicherheitsleistung**: Zahlung unter Vorbehalt; Bankbürgschaft; Schuldschein.


## Checkliste Arrest-Vorbereitung
- [ ] Seeforderung nach ISAC 1952 Art. 1 identifiziert und dokumentiert
- [ ] Schiff im Hafen bestätigt; Liegeplatz ermittelt
- [ ] Zuständiges Gericht bestimmt (LG am Liegeplatz; ZPO § 919)
- [ ] Arrestanspruch und Arrestgrund glaubhaft gemacht (Eidesstattliche Versicherung)
- [ ] Arrestantrag (ZPO § 920) vollständig vorbereitet
- [ ] Vollziehungsstrategie: Registereintragung (SchRegO § 67) plus physische Bewachung
- [ ] Freigabe-Optionen identifiziert: LOU des P&I-Clubs; Bankbürgschaft
- [ ] § 945-Schadensersatzrisiko bewertet

## Relevante Rechtsprechung
- LG Hamburg; OLG Hamburg zu Seearrest; Anforderungen an Arrestanspruch und -grund.
- BGH zur Haftung aus ungerechtfertigtem Arrest nach ZPO § 945.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; Verhältnismäßigkeit der Sicherheitsleistung.

## Normen im Überblick
- ZPO § 916: dinglicher Arrest; Voraussetzungen; Arrestanspruch; Arrestgrund.
- ZPO §§ 917-919: besondere Arrestgründe; örtliche Zuständigkeit (Liegeplatz).
- ZPO § 920: Arrestantrag; Form; Glaubhaftmachung.
- ZPO § 929: Vollziehungsfrist 1 Monat; Wirkungsverlust bei Nichtvollziehung.
- ZPO § 945: Schadensersatz bei unberechtigtem oder wirkungslos gewordenem Arrest.
- SchRegO § 67: Eintragung von Pfändungs- und Arrestvermerken im Schiffsregister.
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest an Schwesterschiffen; Verfahren.


## Vertiefung Arrest

### Seeforderungen und ISAC 1952
Das ISAC 1952 definiert abschließend, für welche Forderungen ein Schiffsarrest zulässig ist (Art. 1). Deutschland ist Vertragsstaat; die meisten EU-Häfen ebenfalls. Im Nicht-Vertragsstaat gilt nationales Recht; die Anforderungen können abweichen.

### Arrest vs. LOU des P&I-Clubs
In der Praxis wird der Arrest häufig durch eine Letter of Undertaking (LOU) des P&I-Clubs abgewandt. Die LOU ist ein abstraktes Schuldversprechen des Clubs; sie wird nur ausgestellt, wenn die zugrundeliegende Forderung club-covered ist.

## Normen-Synopse Arrest
| Norm | Inhalt |
|------|--------|
| ZPO § 916 | Dinglicher Arrest |
| ZPO § 920 | Arrestantrag |
| ZPO § 929 | Vollziehungsfrist |
| ZPO § 945 | Schadensersatz |
| ISAC 1952 Art. 1 | Seeforderungen |

## Quellen
- ZPO §§ 916-945: https://dejure.org/gesetze/ZPO/916.html
- SchRegO § 67: https://dejure.org/gesetze/SchRegO/67.html
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- openjur LG Hamburg Arrest: https://www.openjur.de

## 2. `see-025-schiffshypothek-wrackpflicht-pruefen`

**Fokus:** Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes hypothekenbelastetes Seeschiff. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk.

# Schiffshypothek – Wrackbeseitigungspflicht prüfen

## Mandantenfall
Ein hypothekenbelastetes Seeschiff sinkt in deutschen Gewässern; WSA ordnet Beseitigung an; Eigentümer fragt nach Haftung. Die finanzierende Bank fragt, ob sie als Hypothekengläubigerin haftet. Ein Reeder ist insolvent; Behörde will Kosten beim letzten Eigentümer eintreiben.

## Erste Schritte
1. WRC 2007 / WSG Anwendbarkeit pruefen: hypothekenbelastetes Seeschiff ab 300 BRZ in deutschen Gewaessern.
2. Verantwortlichen identifizieren: WSG § 2 - Eigentuemer des {vessel} haftet primaer.
3. Behoerdliche Meldepflicht (WRC Art. 5 / WSG § 4): unverzuegliche Meldung beim WSA.
4. Versicherungsnachweis (WRC Art. 12): Pflicht ab 300 BRZ; P&I-Club-Zertifikat vorlegen.
5. Kostenschaetzung einholen: Bergungsunternehmen; Umweltschadensrisiko bewerten.
6. Notfallmassnahmen koordinieren: BSH-Schadstoffabwehr; Buenker-Oelbergung.

## Rechtsrahmen
- WSG §§ 1-12 Wrackbeseitigungsgesetz; WRC 2007 Nairobi Art. 1-12; MARPOL Annex I Reg. 26.

## Prüfraster
- Ist der Eigentuemer des hypothekenbelastetes Seeschiff bekannt und zahlungsfaehig?
- Greift WRC 2007 (Schiff ab 300 BRZ; Gewaesser eines Vertragsstaats)?
- Ist Wrackbeseitigungs-Versicherung vorhanden (WRC Art. 12)?
- Ueberschreiten Wrackkosten den Schiffswert?
- Bestehen Umweltschadensrisiken (Bunkeröl/Chemikalien) beim hypothekenbelastetes Seeschiff?

## Typische Fallstricke
- WRC gilt auch fuer Freizeitjachten ab 14 Meter Laenge.
- Behoerdliche Ersatzvornahme begründet Kostenerstattungsanspruch mit Vorrang.
- Bei hypothekenbelastetes Seeschiff unter Auslandsflagge kommen Flaggenstaat-Pflichten hinzu.

## Output
WRC-Pflichtenanalyse und Kostenrisiko-Vermerk für hypothekenbelastetes Seeschiff.


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

## 3. `see-026-schiffshypothek-versicherung-melden`

**Fokus:** Schiffshypothek: Schadensereignis an hypothekenbelastetes Seeschiff melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht.

# Schiffshypothek – Schadensfall bei Versicherung melden

## Mandantenfall
Ein hypothekenbelastetes Seeschiff erleidet Kollisionsschäden; P&I-Club und H&M-Versicherer werden koordiniert informiert. Ein Reeder verzögert die Schadensmeldung; Versicherer beruft sich auf VVG § 28 Obliegenheitsverletzung. Eine Bank aktiviert MII-Police nach Totalverlust eines hypothekenbelasteten hypothekenbelastetes Seeschiff.

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
Meldecheckliste (P&I/H&M/MII) und Fristenübersicht für hypothekenbelastetes Seeschiff.


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

## 4. `see-027-schiffshypothek-local-counsel-instruie`

**Fokus:** Schiffshypothek: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei hypothekenbelastetes Seeschiff im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste.

# Schiffshypothek – Local Counsel instruieren

## Mandantenfall
Ein hypothekenbelastetes Seeschiff liegt in einem ausländischen Hafen; lokaler Arrest ist erforderlich. Eine Hypothekenbank braucht Auskunft zur Vollstreckbarkeit ihrer deutschen Sicherheit im Ausland. Ein P&I-Club braucht nach Unfall lokale Rechtsvertretung für das hypothekenbelastetes Seeschiff.

## Erste Schritte
1. Local Counsel auswaehlen: Empfehlung durch P&I-Club-Korrespondenten oder Netzwerk.
2. Briefing erstellen: hypothekenbelastetes Seeschiff-Daten (IMO-Nummer; Flagge); Sachverhalt; deutsches Recht.
3. Lokale Rechtslage abfragen: Vollstreckungsanforderungen; Anerkennung deutscher Titel.
4. ISAC-1952-Pruefung: Ist Hafenstaat Vertragsstaat?
5. Letter of Instruction verfassen: Weisungen; Budget; Berichtspflichten.
6. P&I-Club koordinieren: liegt LOU-Angebot vor; macht es Arrest entbehrlich?

## Rechtsrahmen
- ISAC 1952 Art. 1; EuGVVO 2012 Recast EU-Vollstreckung; UNCLOS Art. 292 Prompt Release; SchRG §§ 8-74.

## Prüfraster
- Ist der Hafenstaat ISAC-1952-Vertragsstaat?
- Sind deutsche Urteile im Hafenstaat anerkennungsfaehig?
- Hat Local Counsel Erfahrung mit Seerecht und Schiffshypothek?
- Liegt ein LOU des P&I-Clubs vor?
- Ist der Kostenrahmen fuer das Auslandsverfahren freigegeben?

## Typische Fallstricke
- Lokale Seepfandrechte koennen deutsche Hypothek im Rang ueberbieten.
- Kostenunterschaetzung: Auslandsverfahren dauern laenger und kosten mehr.
- LOU-Verhandlungen erfordern erfahrenen Local Counsel.

## Output
Local-Counsel-Briefing für hypothekenbelastetes Seeschiff und Prioritätenliste.


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

## 5. `see-028-schiffshypothek-closing-planen`

**Fokus:** Schiffshypothek: Closing eines hypothekenbelastetes Seeschiff-Kaufs oder einer Finanzierung planen: Eigentumsuebergang (SchRG § 2); Hypothekenloesung (SchRG § 19); simultane Zahlung und Eintragung; Zertifikats-Ummeldung. Output: Closing-Checkliste und Zeitplan.

# Schiffshypothek – Closing planen

## Mandantenfall
Der Kauf eines hypothekenbelastetes Seeschiff soll abgeschlossen werden; Hypotheken sind abzulösen. Ein Käufer besteht auf lastenfreier Lieferung mit gültiger Klasse und MLC-Zertifikat. Eine Bank koordiniert das Closing bei syndizierten Finanzierungen.

## Erste Schritte
1. Ablosebetraege aller Hypothekenglaeubiger anfordern; Stichtag abstimmen.
2. Loeschungsbewilligungen (SchRG § 19) beschaffen; zeitlich koordinieren.
3. Escrow-Konto einrichten: Kaufpreis gegen Loeschungsbestaetigung.
4. Eigentumsuebergang (SchRG § 2) und Hypothekenloesung gleichzeitig fuer hypothekenbelastetes Seeschiff.
5. Zertifikate (Klasse; ISM; MLC; ISPS) auf neuen Eigentuemer ummelden.
6. Registerauszug nach Closing beschaffen; Closing-Memo erstellen.

## Rechtsrahmen
- SchRG §§ 2/19; SchRegO §§ 13-19; FlaggRG §§ 3-5; ISM-Code Kap. 3 SMC-Neuzertifizierung.

## Prüfraster
- Sind alle Loeschungsbewilligungen zeitlich koordiniert?
- Ist der Escrow-Mechanismus wasserdicht gegen Insolvenz des Verkaeufers?
- Sind alle Zertifikate fuer hypothekenbelastetes Seeschiff auf neuen Eigentuemer vorbereitet?
- Ist der Flaggenwechsel (wenn vorgesehen) vorbereitet?
- Ist die Vollmacht fuer den Registerantrag aktuell?

## Typische Fallstricke
- Zahlung ohne simultane Loeschung: Hypothek bleibt trotz Zahlung eingetragen.
- ISM-/MLC-Luecke nach Eigentumsuebergang; Port-State-Detention droht.
- Nachranghypotheken blockieren Closing wenn Erstrangglaeubigerbank nicht kooperiert.

## Output
Closing-Checkliste und Zeitplan mit Abhängigkeiten für hypothekenbelastetes Seeschiff.


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
