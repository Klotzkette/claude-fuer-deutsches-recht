---
name: see-charterparty-register-hypothek-bestellen
description: "SEE Charterparty Register Hypothek Bestellen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Charterparty Register Hypothek Bestellen

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Charterparty Register Hypothek Bestellen** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-111-charterparty-register-pruefen` | Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer prueft Seeschiffsregister bleibt beim Reeder; kein Charter-Register auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte. |
| `see-112-charterparty-hypothek-bestellen` | Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Gechartertes Seeschiff unter Charterparty. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. |
| `see-114-charterparty-arrest-vorbereiten` | Charterparty: Glaeubiger sichert Anspruch an Gechartertes Seeschiff unter Charterparty durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan. |
| `see-115-charterparty-wrackpflicht-pruefen` | Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Gechartertes Seeschiff unter Charterparty. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk. |
| `see-116-charterparty-versicherung-melden` | Charterparty: Schadensereignis an Gechartertes Seeschiff unter Charterparty melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Charterparty Register Hypothek Bestellen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-111-charterparty-register-pruefen`

**Fokus:** Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer prueft Seeschiffsregister bleibt beim Reeder; kein Charter-Register auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte.

# Charterparty – Registerprüfung

## Mandantenfall
Eine finanzierende Bank prueft den Seeschiffsregister bleibt beim Reeder; kein Charter-Register vor Auszahlung eines Kredits fuer ein Gechartertes Seeschiff unter Charterparty. Ein Investor will Eigentuemerstellung und Lastenfreiheit bestaetigt haben. Ein Insolvenzverwalter erstellt die Glaeubigerliste fuer die Masse.

## Erste Schritte
1. Aktuellen Registerauszug (Seeschiffsregister bleibt beim Reeder; kein Charter-Register) beim zustaendigen Gericht beschaffen.
2. Eigentuemerstellung (Abt. I) pruefen; Verkaeufereigenschaft bestaetigen.
3. Hypothekenabteilung (Abt. II): Betrag, Rang, Glaeubiger und Faelligkeit.
4. Gesetzliche Vorrechte identifizieren (HGB §§ 596-601 oder BinSchG §§ 102-116).
5. Arrest- und Pfaendungsvermerke sichten; Zeitpunkt der Eintragung beachten.
6. Registerpruefprotokoll erstellen; Rangkarte und Risikoampel ausgeben.

## Rechtsrahmen
- HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001; SchRegO §§ 3-19 Registerführung; BGB §§ 892-893 Gutglaubensschutz im Register. Hire vs. Freight; Off-Hire-Regime; Sub-Charter; ISM-Verantwortung Bareboat.

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Verkäufer des Gechartertes Seeschiff unter Charterpartys überein?
- Sind alle Hypotheken mit aktuellem Valutierungsstand bei Gläubigern abgeglichen?
- Bestehen gesetzliche Vorrechte, die Hypotheken im Rang verdrängen?
- Gibt es Arrest- oder Pfändungsvermerke im Register?
- Sind Löschungsvoraussetzungen für alle Altlasten erfüllt?

## Typische Fallstricke
- Gesetzliche Vorrechte (Crew-Löhne, Hafengebühren) entstehen ohne Registereintragung.
- Voreintragungspflicht: Veräußerer muss im Seeschiffsregister bleibt beim Reeder; kein Charter-Register eingetragen sein.
- Bei Gechartertes Seeschiff unter Charterparty unter Auslandsflagge gilt Lex registri des Flaggenstaats.

## Output
Registerprüfprotokoll mit Abteilungsübersicht und Rangkarte für Gechartertes Seeschiff unter Charterparty.


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

## 2. `see-112-charterparty-hypothek-bestellen`

**Fokus:** Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Gechartertes Seeschiff unter Charterparty. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste.

# Charterparty – Schiffshypothek bestellen

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein Gechartertes Seeschiff unter Charterparty als Sicherheit fuer einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein Gechartertes Seeschiff unter Charterparty als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des Gechartertes Seeschiff unter Charterpartys pruefen; Eintragung im Seeschiffsregister bleibt beim Reeder; kein Charter-Register bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. Hire vs. Freight; Off-Hire-Regime; Sub-Charter; ISM-Verantwortung Bareboat.

## Prüfraster
- Ist das Gechartertes Seeschiff unter Charterparty im Seeschiffsregister bleibt beim Reeder; kein Charter-Register eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Seeschiffsregister bleibt beim Reeder; kein Charter-Register-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Output
Checkliste Hypothekenbestellung und Unterlagen-Übersicht für Gechartertes Seeschiff unter Charterparty.


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

## 3. `see-114-charterparty-arrest-vorbereiten`

**Fokus:** Charterparty: Glaeubiger sichert Anspruch an Gechartertes Seeschiff unter Charterparty durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan.

# Charterparty – Arrest vorbereiten

## Mandantenfall
Ein Hypothekengläubiger will ein Gechartertes Seeschiff unter Charterparty arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Gechartertes Seeschiff unter Charterparty im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Gechartertes Seeschiff unter Charterparty konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zustaendiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhoerung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Gechartertes Seeschiff unter Charterparty im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Output
Arrestantrags-Baustein (ZPO § 920) und Vollziehungs-Zeitplan für Gechartertes Seeschiff unter Charterparty.


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

## 4. `see-115-charterparty-wrackpflicht-pruefen`

**Fokus:** Charterparty: Reeder; Time Charterer; Voyage Charterer; Bareboat Charterer analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Gechartertes Seeschiff unter Charterparty. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. HGB §§ 527-569 Reise- und Zeitfrachtvertrag; NYPE 2015; Baltime 2001. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk.

# Charterparty – Wrackbeseitigungspflicht prüfen

## Mandantenfall
Ein Gechartertes Seeschiff unter Charterparty sinkt in deutschen Gewässern; WSA ordnet Beseitigung an; Eigentümer fragt nach Haftung. Die finanzierende Bank fragt, ob sie als Hypothekengläubigerin haftet. Ein Reeder ist insolvent; Behörde will Kosten beim letzten Eigentümer eintreiben.

## Erste Schritte
1. WRC 2007 / WSG Anwendbarkeit pruefen: Gechartertes Seeschiff unter Charterparty ab 300 BRZ in deutschen Gewaessern.
2. Verantwortlichen identifizieren: WSG § 2 - Eigentuemer des {vessel} haftet primaer.
3. Behoerdliche Meldepflicht (WRC Art. 5 / WSG § 4): unverzuegliche Meldung beim WSA.
4. Versicherungsnachweis (WRC Art. 12): Pflicht ab 300 BRZ; P&I-Club-Zertifikat vorlegen.
5. Kostenschaetzung einholen: Bergungsunternehmen; Umweltschadensrisiko bewerten.
6. Notfallmassnahmen koordinieren: BSH-Schadstoffabwehr; Buenker-Oelbergung.

## Rechtsrahmen
- WSG §§ 1-12 Wrackbeseitigungsgesetz; WRC 2007 Nairobi Art. 1-12; MARPOL Annex I Reg. 26.

## Prüfraster
- Ist der Eigentuemer des Gechartertes Seeschiff unter Charterparty bekannt und zahlungsfaehig?
- Greift WRC 2007 (Schiff ab 300 BRZ; Gewaesser eines Vertragsstaats)?
- Ist Wrackbeseitigungs-Versicherung vorhanden (WRC Art. 12)?
- Ueberschreiten Wrackkosten den Schiffswert?
- Bestehen Umweltschadensrisiken (Bunkeröl/Chemikalien) beim Gechartertes Seeschiff unter Charterparty?

## Typische Fallstricke
- WRC gilt auch fuer Freizeitjachten ab 14 Meter Laenge.
- Behoerdliche Ersatzvornahme begründet Kostenerstattungsanspruch mit Vorrang.
- Bei Gechartertes Seeschiff unter Charterparty unter Auslandsflagge kommen Flaggenstaat-Pflichten hinzu.

## Output
WRC-Pflichtenanalyse und Kostenrisiko-Vermerk für Gechartertes Seeschiff unter Charterparty.


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

## 5. `see-116-charterparty-versicherung-melden`

**Fokus:** Charterparty: Schadensereignis an Gechartertes Seeschiff unter Charterparty melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht.

# Charterparty – Schadensfall bei Versicherung melden

## Mandantenfall
Ein Gechartertes Seeschiff unter Charterparty erleidet Kollisionsschäden; P&I-Club und H&M-Versicherer werden koordiniert informiert. Ein Reeder verzögert die Schadensmeldung; Versicherer beruft sich auf VVG § 28 Obliegenheitsverletzung. Eine Bank aktiviert MII-Police nach Totalverlust eines hypothekenbelasteten Gechartertes Seeschiff unter Charterparty.

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
Meldecheckliste (P&I/H&M/MII) und Fristenübersicht für Gechartertes Seeschiff unter Charterparty.


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
