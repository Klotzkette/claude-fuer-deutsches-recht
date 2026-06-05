---
name: see-schiffshypothek-klagepfad-risiko
description: "SEE Schiffshypothek Klagepfad Risiko: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Schiffshypothek Klagepfad Risiko

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Schiffshypothek Klagepfad Risiko** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-029-schiffshypothek-klagepfad-waehlen` | Schiffshypothek: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um hypothekenbelastetes Seeschiff: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose. |
| `see-030-schiffshypothek-risiko-memo-schreiben` | Schiffshypothek: Gesamtrisikobewertung fuer Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank bei hypothekenbelastetes Seeschiff: Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: Risiko-Memo und Empfehlungsmatrix. |
| `see-031-schiffbauwerk-register-pruefen` | Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank prueft Schiffbauwerksregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte. |
| `see-032-schiffbauwerk-hypothek-bestellen` | Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Schiff im Bau (Schiffbauwerk). SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. |
| `see-034-schiffbauwerk-arrest-vorbereiten` | Schiffbauwerk: Glaeubiger sichert Anspruch an Schiff im Bau (Schiffbauwerk) durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Schiffshypothek Klagepfad Risiko**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-029-schiffshypothek-klagepfad-waehlen`

**Fokus:** Schiffshypothek: Glaeubiger oder Reeder waehlt Klagepfad bei Streit um hypothekenbelastetes Seeschiff: Zwangsversteigerung (ZPO §§ 864-871); Arrest; einvernehmlicher Verkauf; Insolvenzantrag. Rangfolge und Erloesprognose. Output: Klagepfad-Analyse und Erloesprognose.

# Schiffshypothek – Klagepfad wählen

## Mandantenfall
Eine Bank will nach Kreditausfall aus der Hypothek am hypothekenbelastetes Seeschiff vollstrecken. Mehrere Gläubiger streiten um den Versteigerungserlös des hypothekenbelastetes Seeschiff. Ein Reeder prüft, ob ein freiwilliger Verkauf günstiger ist als die Zwangsversteigerung.

## Erste Schritte
1. Schiffswert des hypothekenbelastetes Seeschiff ermitteln: aktuelles Schätzgutachten beschaffen.
2. Glaeubigerrangfolge aufstellen: gesetzliche Vorrechte dann Hypotheken nach Rang.
3. ZPO §§ 864-871 Zwangsversteigerung: Zeitaufwand; Kosten; erwarteter Erloes.
4. Einvernehmlichen Verkauf pruefen: schneller und guenstiger wenn Reeder kooperiert.
5. Insolvenzantrag als taktisches Mittel: Arrests anderer Glaeubiger stoppen.
6. Schiedsklausel im Kreditvertrag pruefen: London Arbitration oder deutsches Gericht?

## Rechtsrahmen
- ZPO §§ 864-871 Zwangsversteigerung; InsO §§ 49-51 Absonderung; HGB §§ 596-601 Vorrangrechte; SchRG §§ 59-74 Rang.

## Prüfraster
- Uebersteigt Schiffswert des hypothekenbelastetes Seeschiff die Kreditvaluta?
- Gibt es erstrangige Vorrechte die den Erloes aufzehren?
- Ist einvernehmlicher Verkauf moeglich?
- Droht auslaendische Vollstreckung das deutsche Verfahren zu unterlaufen?
- Ist Insolvenzantrag taktisch sinnvoll?

## Typische Fallstricke
- Gesetzliche Schiffsglaeubigerrechte (Crew-Loehne/Hafen) fressen Erloes vor Hypotheken.
- Zwangsversteigerung dauert; Schiffswert sinkt durch Stillstand im Hafen.
- Auslaendische Arrests parallel zum deutschen Verfahren.

## Output
Klagepfad-Analyse und Erlösprognose (Tabelle Kosten vs. Erlös) für hypothekenbelastetes Seeschiff.


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

## 2. `see-030-schiffshypothek-risiko-memo-schreiben`

**Fokus:** Schiffshypothek: Gesamtrisikobewertung fuer Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank bei hypothekenbelastetes Seeschiff: Kreditausfall; Hypothekenrang; Schiffsglaeubigerrechte; Wrackpflicht; Insolvenzrisiko; Handlungsoptionen. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: Risiko-Memo und Empfehlungsmatrix.

# Schiffshypothek – Risiko-Memo schreiben

## Mandantenfall
Eine Bank bereitet den Vorstand auf potenzielle Kreditausfälle in der Schiffshypothek-Flotte vor. Ein Finanzinvestor prüft den Kauf eines Kreditportfolios mit Schiffshypothek-Hypotheken. Ein Syndikat benötigt ein gemeinsames Risikodokument für alle Banken.

## Erste Schritte
1. Schiffshypothek-Daten zusammenfassen: IMO-Nummer; Flagge; Alter; Schiffswert; Kreditvaluta.
2. Hypothekenrang und Konkurrenzrechte darstellen.
3. Hauptrisiken identifizieren: Wertverfall; Reeder-Insolvenz; Vorrangglaeubigerrechte; Wrackpflicht.
4. Handlungsoptionen mit Kosten-Nutzen-Analyse formulieren.
5. Zeitkritische Massnahmen priorisieren: Arrest; Versicherungspruefung; ISM-Status.
6. Empfehlungsmatrix fuer Entscheidungstraeger erstellen.

## Rechtsrahmen
- SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte; InsO §§ 49-51 Absonderung; WSG §§ 1-12 Wrackpflicht; ZPO §§ 864-871 Zwangsversteigerung.

## Prüfraster
- Ist aktueller Schiffswert fuer hypothekenbelastetes Seeschiff dokumentiert?
- Sind alle Vorrangglaeubigerrechte (gesetzliche Schiffsglaeubigerrechte) bekannt?
- Ist Wrackbeseitigungs-Versicherungsdeckung bestaetigt?
- Ist Insolvenzwahrscheinlichkeit des Reeders bewertet?
- Sind Handlungsoptionen mit Zeitplan und Kosten aufgelistet?

## Typische Fallstricke
- Schiffswertgutachten fuer hypothekenbelastetes Seeschiff veraltet; Marktpreise schwanken stark.
- Memo ohne Priorisierung zeitkritischer Massnahmen fuehrt zu Untaetigkeit.
- Vorrangglaeubigerrechte (Besatzungsloehne/Hafengebuehren) werden unterschaetzt.

## Output
Risiko-Memo (Exekutivfassung) und Empfehlungsmatrix für hypothekenbelastetes Seeschiff.


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

## 3. `see-031-schiffbauwerk-register-pruefen`

**Fokus:** Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank prueft Schiffbauwerksregister auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte.

# Schiffbauwerk – Registerprüfung

## Mandantenfall
Eine finanzierende Bank prueft den Schiffbauwerksregister vor Auszahlung eines Kredits fuer ein Schiff im Bau (Schiffbauwerk). Ein Investor will Eigentuemerstellung und Lastenfreiheit bestaetigt haben. Ein Insolvenzverwalter erstellt die Glaeubigerliste fuer die Masse.

## Erste Schritte
1. Aktuellen Registerauszug (Schiffbauwerksregister) beim zustaendigen Gericht beschaffen.
2. Eigentuemerstellung (Abt. I) pruefen; Verkaeufereigenschaft bestaetigen.
3. Hypothekenabteilung (Abt. II): Betrag, Rang, Glaeubiger und Faelligkeit.
4. Gesetzliche Vorrechte identifizieren (HGB §§ 596-601 oder BinSchG §§ 102-116).
5. Arrest- und Pfaendungsvermerke sichten; Zeitpunkt der Eintragung beachten.
6. Registerpruefprotokoll erstellen; Rangkarte und Risikoampel ausgeben.

## Rechtsrahmen
- SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag; SchRegO §§ 3-19 Registerführung; BGB §§ 892-893 Gutglaubensschutz im Register. Baufortschritt; Refund Guarantee; Bauabnahme.

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Verkäufer des Schiff im Bau (Schiffbauwerk)s überein?
- Sind alle Hypotheken mit aktuellem Valutierungsstand bei Gläubigern abgeglichen?
- Bestehen gesetzliche Vorrechte, die Hypotheken im Rang verdrängen?
- Gibt es Arrest- oder Pfändungsvermerke im Register?
- Sind Löschungsvoraussetzungen für alle Altlasten erfüllt?

## Typische Fallstricke
- Gesetzliche Vorrechte (Crew-Löhne, Hafengebühren) entstehen ohne Registereintragung.
- Voreintragungspflicht: Veräußerer muss im Schiffbauwerksregister eingetragen sein.
- Bei Schiff im Bau (Schiffbauwerk) unter Auslandsflagge gilt Lex registri des Flaggenstaats.

## Output
Registerprüfprotokoll mit Abteilungsübersicht und Rangkarte für Schiff im Bau (Schiffbauwerk).


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

## 4. `see-032-schiffbauwerk-hypothek-bestellen`

**Fokus:** Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Schiff im Bau (Schiffbauwerk). SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste.

# Schiffbauwerk – Schiffshypothek bestellen

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein Schiff im Bau (Schiffbauwerk) als Sicherheit fuer einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein Schiff im Bau (Schiffbauwerk) als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des Schiff im Bau (Schiffbauwerk)s pruefen; Eintragung im Schiffbauwerksregister bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. Baufortschritt; Refund Guarantee; Bauabnahme.

## Prüfraster
- Ist das Schiff im Bau (Schiffbauwerk) im Schiffbauwerksregister eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Schiffbauwerksregister-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Output
Checkliste Hypothekenbestellung und Unterlagen-Übersicht für Schiff im Bau (Schiffbauwerk).


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

## 5. `see-034-schiffbauwerk-arrest-vorbereiten`

**Fokus:** Schiffbauwerk: Glaeubiger sichert Anspruch an Schiff im Bau (Schiffbauwerk) durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan.

# Schiffbauwerk – Arrest vorbereiten

## Mandantenfall
Ein Hypothekengläubiger will ein Schiff im Bau (Schiffbauwerk) arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Schiff im Bau (Schiffbauwerk) im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Schiff im Bau (Schiffbauwerk) konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zustaendiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhoerung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Schiff im Bau (Schiffbauwerk) im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Output
Arrestantrags-Baustein (ZPO § 920) und Vollziehungs-Zeitplan für Schiff im Bau (Schiffbauwerk).


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
