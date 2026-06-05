---
name: see-schiffbauwerk-risiko-yachtkauf-register
description: "SEE Schiffbauwerk Risiko Yachtkauf Register: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Schiffbauwerk Risiko Yachtkauf Register

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Schiffbauwerk Risiko Yachtkauf Register** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-040-schiffbauwerk-risiko-memo-schreiben` | Schiffbauwerk: Gesamtrisikobewertung fuer Werft; Auftraggeber-Reeder; finanzierende Bank bei Schiff im Bau (Schiffbauwerk): Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Output: Risiko-Memo und Empfehlungsmatrix. |
| `see-051-yachtkauf-register-pruefen` | Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus prueft Seeschiffsregister oder Kleinfahrzeugregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte. |
| `see-052-yachtkauf-hypothek-bestellen` | Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Segel- oder Motorjacht. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. |
| `see-054-yachtkauf-arrest-vorbereiten` | Yachtkauf: Glaeubiger sichert Anspruch an Segel- oder Motorjacht durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan. |
| `see-055-yachtkauf-wrackpflicht-pruefen` | Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Segel- oder Motorjacht. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Schiffbauwerk Risiko Yachtkauf Register**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-040-schiffbauwerk-risiko-memo-schreiben`

**Fokus:** Schiffbauwerk: Gesamtrisikobewertung fuer Werft; Auftraggeber-Reeder; finanzierende Bank bei Schiff im Bau (Schiffbauwerk): Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Output: Risiko-Memo und Empfehlungsmatrix.

# Schiffbauwerk – Risiko-Memo schreiben

## Mandantenfall
Eine Bank bereitet den Vorstand auf potenzielle Kreditausfälle in der Schiffbauwerk-Flotte vor. Ein Finanzinvestor prüft den Kauf eines Kreditportfolios mit Schiffbauwerk-Hypotheken. Ein Syndikat benötigt ein gemeinsames Risikodokument für alle Banken.

## Erste Schritte
1. Schiffbauwerk-Daten zusammenfassen: IMO-Nummer; Flagge; Alter; Schiffswert; Kreditvaluta.
2. Hypothekenrang und Konkurrenzrechte darstellen.
3. Hauptrisiken identifizieren: Wertverfall; Reeder-Insolvenz; Vorrangglaeubigerrechte; Wrackpflicht.
4. Handlungsoptionen mit Kosten-Nutzen-Analyse formulieren.
5. Zeitkritische Massnahmen priorisieren: Arrest; Versicherungspruefung; ISM-Status.
6. Empfehlungsmatrix fuer Entscheidungstraeger erstellen.

## Rechtsrahmen
- SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag; InsO §§ 49-51 Absonderung; WSG §§ 1-12 Wrackpflicht; ZPO §§ 864-871 Zwangsversteigerung.

## Prüfraster
- Ist aktueller Schiffswert fuer Schiff im Bau (Schiffbauwerk) dokumentiert?
- Sind alle Vorrangglaeubigerrechte (gesetzliche Schiffsglaeubigerrechte) bekannt?
- Ist Wrackbeseitigungs-Versicherungsdeckung bestaetigt?
- Ist Insolvenzwahrscheinlichkeit des Reeders bewertet?
- Sind Handlungsoptionen mit Zeitplan und Kosten aufgelistet?

## Typische Fallstricke
- Schiffswertgutachten fuer Schiff im Bau (Schiffbauwerk) veraltet; Marktpreise schwanken stark.
- Memo ohne Priorisierung zeitkritischer Massnahmen fuehrt zu Untaetigkeit.
- Vorrangglaeubigerrechte (Besatzungsloehne/Hafengebuehren) werden unterschaetzt.

## Output
Risiko-Memo (Exekutivfassung) und Empfehlungsmatrix für Schiff im Bau (Schiffbauwerk).


## Vertiefung: Struktur des Risiko-Memos
Ein hochwertiges Risiko-Memo enthält: (1) Zusammenfassung und Handlungsempfehlung (Executive Summary; max. 1 Seite); (2) Schiffsdaten und aktueller Schiffswert (mit Gutachterquelle und -datum); (3) Kreditstatus (Valutastand; Zinsen; Fälligkeiten; Default-Events); (4) Sicherheitenanalyse (Hypothekenrang; Verwertungserlös-Prognose); (5) Gläubigerrangfolge (gesetzliche Vorrechte; Hypotheken; ungesicherte Forderungen); (6) Risikoszenarien (Best Case; Base Case; Worst Case); (7) Maßnahmenplan mit Zeitlinie und Verantwortlichen.

## Schiffswertermittlung
Schiffswerte werden bestimmt durch: Chartermarkt (aktueller T/C-Äquivalent-Erlös); Vergleichsverkäufe (comparable sales aus Baltic Exchange oder SSY); Gutachten von Shipbrokers (Clarkson; Braemar; Gibson). In der Insolvenz kann ein Notverkauf (forced sale) 10-30% unter dem Schätzwert liegen.

## Eskalationsweg und Zeitkritikalität
Zeitkritische Maßnahmen müssen sofort eingeleitet werden: Arrest bei Fluchtgefahr (sofort); Versicherungsmeldung (binnen 24 Stunden); P&I-Kündigung verhindern (laufende Prämien beobachten); ISM-DOC-Ablauf prüfen (ohne DOC kein Hafenanlauf). Das Risiko-Memo soll diese Zeitlinie explizit darstellen damit Entscheidungsträger die Prioritäten erkennen.


## Checkliste Risiko-Memo
- [ ] Schiffsdaten vollständig: IMO-Nummer; Flagge; Alter; BRZ; Schiffstyp; Klasse
- [ ] Schiffswert: Gutachterquelle; Datum; Methode (Charter-Equivalent; Comparable Sales)
- [ ] Kreditstatus: Valutastand; Zinsen; letzte Zahlung; Default-Events
- [ ] Hypothekenrang: alle Gläubiger; Beträge; Rangstellen
- [ ] Gesetzliche Vorrechte (HGB §§ 596-601): aktuelle Crew-Löhne; Hafengebühren; PSC-Bußgelder
- [ ] Versicherungsdeckung: P&I-Club-Mitgliedschaft; H&M-Police; MII; Laufzeit
- [ ] ISM-/MLC-Zertifikatsstatus: Ablaufdaten; bekannte Mängel
- [ ] Drei Szenarien: Best Case (einvernehmlicher Verkauf); Base Case (Zwangsversteigerung); Worst Case (Insolvenz + Verschrottung)
- [ ] Maßnahmenplan mit Zeitlinie und Verantwortlichen
- [ ] Executive Summary: Gesamtrisiko; Handlungsempfehlung; Nächste Schritte

## Relevante Rechtsprechung
- BGH zur Absonderung des Hypothekengläubigers in der Reederei-Insolvenz; InsO §§ 49-51.
- BGH zur Insolvenzanfechtung von Hypothekentilgungen in der Krise (InsO §§ 130-133).
- OLG Hamburg zu Schiffswertgutachten in Verwertungsverfahren; Anforderungen an die Sachverständigenqualifikation.

## Normen im Überblick
- InsO §§ 49-51: Absonderungsrecht; Hypothekengläubiger befriedigt sich vor der Insolvenzmasse.
- InsO §§ 80-92: Verwaltungs- und Verfügungsbefugnis des Insolvenzverwalters über Schiffe.
- HGB §§ 611-617: Summenhaftung; Haftungsbeschränkung des Reeders; Limits nach LLMC 1976/1996.
- ZPO §§ 864-871: Zwangsversteigerung; Mindestgebot; Erlösverteilung.
- SchRG §§ 59-74: Rangfolge bei der Erlösverteilung nach Zwangsversteigerung.


## Vertiefung Risiko-Memo

### Drei-Szenarien-Analyse
Ein gutes Risiko-Memo enthält immer drei Szenarien: (1) Best Case: freiwilliger Verkauf zum Marktwert; vollständige Schuldenablösung; (2) Base Case: Zwangsversteigerung mit 15-20% Abschlag; teilweise Restschuld; (3) Worst Case: Insolvenz des Reeders; Schiff liegt fest; Erlös nach Kosten nur Teilbefriedigung.

### Zeitlinie
Die Dauer eines Seearrests bis zur Zwangsversteigerung beträgt in Deutschland typischerweise 3-6 Monate; in anderen Jurisdiktionen kürzer (Singapore: 4-6 Wochen; Panama: 2-3 Monate).

## Normen-Synopse Risiko-Memo
| Norm | Inhalt |
|------|--------|
| HGB § 596 | Gesetzliche Vorrechte |
| InsO § 49 | Absonderungsrecht |
| ZPO § 864 | Zwangsversteigerung |
| SchRG § 59 | Rangfolge |

## Quellen
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- InsO §§ 49-51: https://www.gesetze-im-internet.de/inso/__49.html
- BSH: https://www.bsh.de

## 2. `see-051-yachtkauf-register-pruefen`

**Fokus:** Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus prueft Seeschiffsregister oder Kleinfahrzeugregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte.

# Yachtkauf – Registerprüfung

## Mandantenfall
Eine finanzierende Bank prueft den Seeschiffsregister oder Kleinfahrzeugregister vor Auszahlung eines Kredits fuer ein Segel- oder Motorjacht. Ein Investor will Eigentuemerstellung und Lastenfreiheit bestaetigt haben. Ein Insolvenzverwalter erstellt die Glaeubigerliste fuer die Masse.

## Erste Schritte
1. Aktuellen Registerauszug (Seeschiffsregister oder Kleinfahrzeugregister) beim zustaendigen Gericht beschaffen.
2. Eigentuemerstellung (Abt. I) pruefen; Verkaeufereigenschaft bestaetigen.
3. Hypothekenabteilung (Abt. II): Betrag, Rang, Glaeubiger und Faelligkeit.
4. Gesetzliche Vorrechte identifizieren (HGB §§ 596-601 oder BinSchG §§ 102-116).
5. Arrest- und Pfaendungsvermerke sichten; Zeitpunkt der Eintragung beachten.
6. Registerpruefprotokoll erstellen; Rangkarte und Risikoampel ausgeben.

## Rechtsrahmen
- BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m; SchRegO §§ 3-19 Registerführung; BGB §§ 892-893 Gutglaubensschutz im Register. CE-Kennzeichnung; Fahrterlaubnis BSH; VAT-Status EU; MCA Cat..

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Verkäufer des Segel- oder Motorjachts überein?
- Sind alle Hypotheken mit aktuellem Valutierungsstand bei Gläubigern abgeglichen?
- Bestehen gesetzliche Vorrechte, die Hypotheken im Rang verdrängen?
- Gibt es Arrest- oder Pfändungsvermerke im Register?
- Sind Löschungsvoraussetzungen für alle Altlasten erfüllt?

## Typische Fallstricke
- Gesetzliche Vorrechte (Crew-Löhne, Hafengebühren) entstehen ohne Registereintragung.
- Voreintragungspflicht: Veräußerer muss im Seeschiffsregister oder Kleinfahrzeugregister eingetragen sein.
- Bei Segel- oder Motorjacht unter Auslandsflagge gilt Lex registri des Flaggenstaats.

## Output
Registerprüfprotokoll mit Abteilungsübersicht und Rangkarte für Segel- oder Motorjacht.


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

## 3. `see-052-yachtkauf-hypothek-bestellen`

**Fokus:** Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Segel- oder Motorjacht. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste.

# Yachtkauf – Schiffshypothek bestellen

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein Segel- oder Motorjacht als Sicherheit fuer einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein Segel- oder Motorjacht als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des Segel- oder Motorjachts pruefen; Eintragung im Seeschiffsregister oder Kleinfahrzeugregister bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. CE-Kennzeichnung; Fahrterlaubnis BSH; VAT-Status EU; MCA Cat..

## Prüfraster
- Ist das Segel- oder Motorjacht im Seeschiffsregister oder Kleinfahrzeugregister eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Seeschiffsregister oder Kleinfahrzeugregister-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Output
Checkliste Hypothekenbestellung und Unterlagen-Übersicht für Segel- oder Motorjacht.


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

## 4. `see-054-yachtkauf-arrest-vorbereiten`

**Fokus:** Yachtkauf: Glaeubiger sichert Anspruch an Segel- oder Motorjacht durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan.

# Yachtkauf – Arrest vorbereiten

## Mandantenfall
Ein Hypothekengläubiger will ein Segel- oder Motorjacht arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Segel- oder Motorjacht im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Segel- oder Motorjacht konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zustaendiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhoerung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Segel- oder Motorjacht im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Output
Arrestantrags-Baustein (ZPO § 920) und Vollziehungs-Zeitplan für Segel- oder Motorjacht.


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

## 5. `see-055-yachtkauf-wrackpflicht-pruefen`

**Fokus:** Yachtkauf: Privater Kaeufer; Haendler; Flaggenregistrierung und Zollstatus analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Segel- oder Motorjacht. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. BGB §§ 433-479 Kaufrecht; SchRG §§ 8-74 wenn eingetragen; WRC 2007 ab 14 m. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk.

# Yachtkauf – Wrackbeseitigungspflicht prüfen

## Mandantenfall
Ein Segel- oder Motorjacht sinkt in deutschen Gewässern; WSA ordnet Beseitigung an; Eigentümer fragt nach Haftung. Die finanzierende Bank fragt, ob sie als Hypothekengläubigerin haftet. Ein Reeder ist insolvent; Behörde will Kosten beim letzten Eigentümer eintreiben.

## Erste Schritte
1. WRC 2007 / WSG Anwendbarkeit pruefen: Segel- oder Motorjacht ab 300 BRZ in deutschen Gewaessern.
2. Verantwortlichen identifizieren: WSG § 2 - Eigentuemer des {vessel} haftet primaer.
3. Behoerdliche Meldepflicht (WRC Art. 5 / WSG § 4): unverzuegliche Meldung beim WSA.
4. Versicherungsnachweis (WRC Art. 12): Pflicht ab 300 BRZ; P&I-Club-Zertifikat vorlegen.
5. Kostenschaetzung einholen: Bergungsunternehmen; Umweltschadensrisiko bewerten.
6. Notfallmassnahmen koordinieren: BSH-Schadstoffabwehr; Buenker-Oelbergung.

## Rechtsrahmen
- WSG §§ 1-12 Wrackbeseitigungsgesetz; WRC 2007 Nairobi Art. 1-12; MARPOL Annex I Reg. 26.

## Prüfraster
- Ist der Eigentuemer des Segel- oder Motorjacht bekannt und zahlungsfaehig?
- Greift WRC 2007 (Schiff ab 300 BRZ; Gewaesser eines Vertragsstaats)?
- Ist Wrackbeseitigungs-Versicherung vorhanden (WRC Art. 12)?
- Ueberschreiten Wrackkosten den Schiffswert?
- Bestehen Umweltschadensrisiken (Bunkeröl/Chemikalien) beim Segel- oder Motorjacht?

## Typische Fallstricke
- WRC gilt auch fuer Freizeitjachten ab 14 Meter Laenge.
- Behoerdliche Ersatzvornahme begründet Kostenerstattungsanspruch mit Vorrang.
- Bei Segel- oder Motorjacht unter Auslandsflagge kommen Flaggenstaat-Pflichten hinzu.

## Output
WRC-Pflichtenanalyse und Kostenrisiko-Vermerk für Segel- oder Motorjacht.


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
