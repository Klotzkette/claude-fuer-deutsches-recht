---
name: seerecht-schifffahrtsrecht-see-charterparty-einordnen-fracht
description: "SEE Charterparty Einordnen Fracht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Charterparty Einordnen Fracht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Charterparty Einordnen Fracht** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-007-charterparty-einordnen` | Mandant legt Chartervertrag vor; Einordnung als Voyage Charter; Time Charter oder Bareboat Charter nach HGB §§ 527-569. Prueft Verantwortungsverteilung Reeder/Charterer; Besatzungspflicht; nautische vs. kommerzielle Fuehrung; ISM-Code-Zuordnung; Hire-Regime. NYPE 2015; Baltime 2001. Output: Einordnungsvermerk und Haftungsmatrix. |
| `see-008-fracht-und-konnossement` | Spediteur oder Befrachter prueft Konnossement: HGB §§ 513-525 (Ausstellung; Inhalt; Uebergabe); Haftungsgrenzen HGB §§ 498-510; Hague-Visby/Hamburg Rules fuer internationalen Transport. Reine vs. geklauselte Konnossemente; On-Board-Notation; einjährige Ausschlussfrist (HGB § 606). Output: Konnossementspruefprotokoll und Schadensabwicklungs-Leitfaden. |
| `see-009-havarie-und-kollision` | Zwei Schiffe kollidieren; Havarie-Grosse oder Besondere Havarie klaeren. HGB §§ 571-594 (Grosse Havarie; Dispache); Kollisionsuebereinkommen KSUe 1910; SeeUG § 3 (BSU-Untersuchung); York-Antwerp Rules 2016; P&I vs. H&M Kollisionshaftung. Output: Havarien-Erstbericht; Dispache-Auftrag und Klagestrategie. |
| `see-010-bergung-und-wrack` | Schiff strandet oder sinkt; Berger verlangen Bergungslohn; Wrackbeseitigung wird angeordnet. HGB §§ 574-583 (Bergung); WSG §§ 1-12 (Wrackbeseitigungsgesetz); WRC 2007 Nairobi-Uebereinkommen; LOF 2020; SCOPIC-Klausel. Output: Bergungslohn-Kalkulation; WRC-Pflichtenanalyse und Kostenrisiko-Matrix. |
| `see-011-pfaendung-und-arrest-schiff` | Glaeubigervertreter beantragt Arrest gegen Schiff im deutschen Hafen: ZPO §§ 916-945 dinglicher Arrest; Vollziehung durch Registereintragung (SchRegO § 67); ISAC 1952 Seeforderungen. Klaert Arrestanspruch; Arrestgrund; Vollziehungsfrist; Sicherheitsleistung; LOU-Strategie. Output: Arrestantrags-Baustein und Freigabe-Strategie. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Charterparty Einordnen Fracht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-007-charterparty-einordnen`

**Fokus:** Mandant legt Chartervertrag vor; Einordnung als Voyage Charter; Time Charter oder Bareboat Charter nach HGB §§ 527-569. Prueft Verantwortungsverteilung Reeder/Charterer; Besatzungspflicht; nautische vs. kommerzielle Fuehrung; ISM-Code-Zuordnung; Hire-Regime. NYPE 2015; Baltime 2001. Output: Einordnungsvermerk und Haftungsmatrix.

# Charterparty einordnen – Vertragstyp und Haftungsmatrix

## Mandantenfall
Ein Handelskonzern legt einen NYPE-Chartervertrag vor und fragt, ob er als Time Charterer für Kollisionsschäden haftet die der Kapitän verursacht hat. Ein Finanzinvestor plant den Kauf eines Schiffes und möchte es sofort verbareboaten; die Bank fragt nach ISM-Code-Pflichten. Ein Reeder prüft, ob ein Voyage Charter oder Time Charter für eine Einmalfracht vorteilhafter ist.

## Erste Schritte
1. Vertragstyp identifizieren: Voyage Charter (HGB §§ 527-535); Time Charter (HGB §§ 557-569) oder Bareboat Charter (HGB § 553 Abs. 2).
2. Nautische vs. kommerzielle Führung trennen: Reeder trägt nautische Führung auch im Time Charter; Charterer gibt kommerzielle Weisungen.
3. ISM-Code-Zuordnung: Time Charter = Reeder hat DOC/SMC; Bareboat = Bareboat-Charterer übernimmt ISM-Verantwortung.
4. Bunkerkosten-Träger: Voyage Charter = Reeder; Time Charter = Time Charterer (HGB §§ 557-559).
5. Liegegeld/Dispatch nur im Voyage Charter relevant; im Time Charter gilt Hire unabhängig davon.
6. Haftungsmatrix aufstellen: HGB § 480 – Reeder haftet für Verschulden des Kapitäns.

## Rechtsrahmen
- HGB §§ 527-535: Reisefrachtvertrag (Voyage Charter); Liegegeld; Dispatch; Frachtzahlung.
- HGB §§ 557-569: Zeitfrachtvertrag (Time Charter); Hire; Off-hire-Ereignisse; Auslieferungszustand.
- HGB § 553 Abs. 2: Überlassung des Schiffes an Dritte (Bareboat-ähnlich).
- HGB § 480: Haftung des Reeders für Verschulden des Kapitäns und der Besatzung.
- ISM-Code Kapitel 1: Definition des Unternehmens; bei Bareboat ist Bareboat-Charterer das Unternehmen.
- UNCLOS Art. 94: Flaggenstaat bleibt verantwortlich auch bei Bareboat.
- NYPE 2015 / Baltime 2001: Standardformulare; erhebliche Lücken im deutschen Recht.

## Prüfraster
- Wer trägt die nautische Führung (Kapitän = Weisungsempfänger von wem)?
- Wer zahlt Bunker; Hafengebühren; Kanalgebühren?
- Wer hält die ISM-Zertifikate (DOC/SMC)?
- Enthält der Vertrag eine employment clause (Charterer-Weisungsrecht)?
- Welches Recht gilt; Schiedsort London/Hamburg vereinbart?

## Typische Fallstricke
- Time-Charterer-Haftung für Kollisionsschäden: Reeder haftet für nautische Fehler; nicht der Time Charterer.
- Hire-Abzug wegen Off-Hire: technische Defekte oft kein Off-Hire; enge Vertragsdefinition beachten.
- ISM-Verantwortung bei Sub-Charter ohne neue DOC ist rechtswidrig.
- Bareboat-Charter ohne Flaggenwechsel: Heimatstaat verliert nicht automatisch die Kontrolle.

## Output
- Einordnungsvermerk: Vertragstyp; Rechtsrahmen; ISM-Zuordnung
- Haftungsmatrix: Reeder vs. Charterer nach Schadensart
- Red-Flag-Liste für kritische Vertragsklauseln


## Erweiterte Normengrundlage

### Charterrecht
- HGB §§ 494-569: Frachtvertrag und Vercharterung; Rechte und Pflichten.
- HGB § 527: Reisezeitverlängerung (Off-Hire); Berechnung; Nachweis.
- HGB § 559: Konnossement als Frachturkunde; Verhältnis zur Charter.

### Typische Charter-Formulare
- NYPE 1946/1993/2015: New York Produce Exchange Time Charter; Klauseln zu Off-Hire; Liens; BIMCO.
- GENCON 1994: Voyage Charter; Stalldauer (Laytime); Überliege (Demurrage).
- BARECON 2017: Bareboat Charter; Registrierung; Flagge; Instandhaltungspflichten.

## Checkliste Charterparty-Analyse
- [ ] Charter-Typ identifiziert (Time/Voyage/Bareboat/COA)
- [ ] Vertragsparteien und Sub-Charter-Kette ermittelt
- [ ] Laufzeit; Beschäftigungsgebiet; Ausnahmen dokumentiert
- [ ] Off-Hire-Klausel analysiert: Trigger; Berechnung; Benachrichtigungspflichten
- [ ] Lien-Klausel des Eigentümers auf Ladung untersucht
- [ ] Schiedsklausel identifiziert (LMAA London; SMA New York; GMAA Hamburg)
- [ ] Governing Law bestimmt; kollisionsrechtliche Anknüpfung geprüft

## Relevante Rechtsprechung
- BGH zur Anwendung englischen Rechts auf Charter-Parteien bei LMAA-Klausel.
- OLG Hamburg zur Demurrage-Berechnung bei verzögerter Abfertigung im deutschen Hafen.
- BGH zur Kündigung der Time-Charter bei Zahlungsverzug des Charterers.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 527-569: https://dejure.org/gesetze/HGB/527.html
- HGB § 480: https://dejure.org/gesetze/HGB/480.html
- ISM-Code BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/ISM_Code/ism_code_node.html
- NYPE 2015 BIMCO: https://www.bimco.org
- dejure HGB § 557: https://dejure.org/gesetze/HGB/557.html

## 2. `see-008-fracht-und-konnossement`

**Fokus:** Spediteur oder Befrachter prueft Konnossement: HGB §§ 513-525 (Ausstellung; Inhalt; Uebergabe); Haftungsgrenzen HGB §§ 498-510; Hague-Visby/Hamburg Rules fuer internationalen Transport. Reine vs. geklauselte Konnossemente; On-Board-Notation; einjährige Ausschlussfrist (HGB § 606). Output: Konnossementspruefprotokoll und Schadensabwicklungs-Leitfaden.

# Fracht und Konnossement – Prüfung und Schadensabwicklung

## Mandantenfall
Ein Importeur erhält beschädigte Ware; das Konnossement ist geklauselt; er fragt ob und wie er den Verfrachter in Anspruch nehmen kann. Eine Bank hält ein Orderkonnossement als Kreditsicherheit und fragt nach Schutz bei Insolvenz des Abladers. Ein Verfrachter wird mit einer Schadensklage konfrontiert; das Konnossement enthält den Vermerk 'said to contain'.

## Erste Schritte
1. Konnossement klassifizieren: Orderkonnossement (HGB § 513); Rektakonnossement (HGB § 524); Multimodal-Dokument.
2. Rein oder geklauselt prüfen: reines Konnossement = keine Vorbehalte; Klauselkonnossement = Haftungsrisiko für Verlader.
3. Verladungsnachweis sichern: On-Board-Notation nach HGB § 515; Frachtstücke; Gewicht; Zustand bei Annahme durch Kapitän.
4. Haftungsgrundlage ermitteln: HGB §§ 498-511 – Haftung des Verfrachters für Verlust/Beschädigung.
5. Haftungsgrenze berechnen: HGB § 502 – 666/67 SDR/Stück oder 2 SDR/kg (Hague-Visby); Hamburg Rules: 835 SDR/Stück oder 2/5 SDR/kg.
6. Fristen prüfen: HGB § 606 – Klagfrist ein Jahr ab Ablieferung; Schadensmeldung binnen drei Tagen (HGB § 604).

## Rechtsrahmen
- HGB §§ 513-525: Konnossement; Ausstellung; Inhalt; Übergang von Rechten.
- HGB §§ 498-511: Haftung des Verfrachters für Verlust und Beschädigung der Ladung.
- HGB § 502: Haftungshöchstgrenzen nach Hague-Visby-Regime.
- HGB § 604: Schadensanzeigepflicht binnen drei Tagen nach Ablieferung.
- HGB § 606: Einjährige Ausschlussfrist für Ansprüche aus dem Frachtvertrag.
- Hamburg Rules Art. 5: erhöhter Haftungsmaßstab für den Seefrachtführer.

## Prüfraster
- Ist das Konnossement rein ausgestellt oder enthält es Vorbehalte über den Ladungszustand?
- Ist die On-Board-Notation vorhanden?
- Ist die Schadensmeldung fristgerecht (binnen drei Tagen HGB § 604) erfolgt?
- Greift die einjährige Ausschlussfrist (HGB § 606)?
- Welches Haftungsregime gilt: Hague-Visby; Hamburg Rules oder nationales Recht?

## Typische Fallstricke
- Versäumte Schadensmeldung binnen drei Tagen verschiebt Beweislast; ist aber kein Rechtsverlust.
- 'Said to contain' Klausel schließt Verfrachter-Haftung für Gewicht/Inhalt aus.
- Einjährige Ausschlussfrist (HGB § 606) ist Ausschlussfrist; kein Neubeginn durch Verhandlungen.
- Mehrfachindossament von Konnossementen: bei Kollision mit Sea-Waybill gilt das Konnossement.

## Output
- Konnossementsprüfprotokoll (Dokumentenstatus; Mängel; Risiken)
- Schadensabwicklungs-Leitfaden (Anzeige; Sicherung; Klageweg)
- Haftungsgrenzen-Berechnung
- Musterbrief Schadensmeldung an Verfrachter


## Erweiterte Normengrundlage

### Konnossementsrecht
- HGB §§ 513-554: Konnossement; Ausstellung; Inhalt; Überleitung; Schadenshaftung.
- HGB § 516: Inhalt des Konnossements; Pflichtangaben; optionale Angaben.
- HGB § 520: Haftung des Verfrachters für unrichtige Angaben im Konnossement.

### Internationale Regime
- Haager Regeln 1924: Grundregime für Haftungsgrenzen und Freistellungsgründe.
- Haager-Visby-Regeln 1968: erhöhte SDR-Haftungslimits; Anwendungsvorrang in DE.
- Hamburg Rules 1978: erweiterter Anwendungsbereich; erhöhte Haftungsgrenzen; seltenere Anwendung.
- Rotterdam Rules 2009: noch nicht in Kraft; Verhandlungsrahmen für neue Verträge.

## Checkliste Konnossementsfall
- [ ] Original-Konnossement (Set of 3) vorliegend oder geklärt ob Seawaybill
- [ ] Konnossementsinhalt geprüft: Schiff; Verlader; Empfänger; Häfen; Beschreibung der Ladung
- [ ] Order-Konnossement oder Straight Bill of Lading identifiziert
- [ ] Claused oder Clean Bill of Lading festgestellt; Klauseln dokumentiert
- [ ] Anwendbares Haftungsregime (HVR/Hamburg Rules) bestimmt
- [ ] Verjährungsfrist: 1 Jahr (HVR Art. III Ziff. 6) ab Ablieferung notiert

## Relevante Rechtsprechung
- BGH zur Haftung des Verfrachters nach Haager-Visby-Regeln; Haftungsausschlüsse Art. IV.
- OLG Hamburg zu Claused Bills of Lading; Haftung des Verfrachters gegenüber Indossatar.
- BGH zum Rückgriff des Verfrachters auf den Ablader bei unrichtigen Konnossementsangaben.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB § 513: https://dejure.org/gesetze/HGB/513.html
- HGB § 502: https://dejure.org/gesetze/HGB/502.html
- HGB § 606: https://dejure.org/gesetze/HGB/606.html
- Hamburg Rules UNCTAD: https://unctad.org/system/files/official-document/aconf89d13_en.pdf
- gesetze-im-internet HGB § 513: https://www.gesetze-im-internet.de/hgb/__513.html

## 3. `see-009-havarie-und-kollision`

**Fokus:** Zwei Schiffe kollidieren; Havarie-Grosse oder Besondere Havarie klaeren. HGB §§ 571-594 (Grosse Havarie; Dispache); Kollisionsuebereinkommen KSUe 1910; SeeUG § 3 (BSU-Untersuchung); York-Antwerp Rules 2016; P&I vs. H&M Kollisionshaftung. Output: Havarien-Erstbericht; Dispache-Auftrag und Klagestrategie.

# Havarie und Kollision – Erstbericht und Haftungsklärung

## Mandantenfall
Ein Containerschiff rammt im Hamburger Hafen einen Tanker; beide Schiffe haben Schäden; der Kapitän steht im Verdacht der Trunkenheit. Ein Reeder fordert nach Sturm-Notfall auf See eine Große-Havarie-Verteilung: Ladung wurde über Bord geworfen um das Schiff zu retten. Ein Schiff erleidet bei Nebel eine Kollision mit einem unbekannten Fahrzeug.

## Erste Schritte
1. Schadens- und Hergangsermittlung: VHF-Aufzeichnungen; AIS-Daten; Brückenbuch; Maschinenlogbuch beschaffen und sichern.
2. Kollisionstyp bestimmen: Seeschiff/Seeschiff (KSÜ 1910); Seeschiff/Binnenschiff (BinSchG § 92); Seeschiff/Hafenanlagen.
3. Große Havarie vs. Besondere Havarie prüfen: HGB §§ 571-574 – Große Havarie = gemeinschaftliche Opfer zur Rettung des Abenteuers.
4. Dispache-Auftrag vorbereiten: York-Antwerp Rules (YAR 2016) oder abweichende vertragliche Vereinbarung.
5. P&I-Club und H&M-Versicherer sofort informieren; Letters of Undertaking zur Arrestvermeidung sichern.
6. Straf- und ordnungswidrigkeitenrechtliche Aspekte sichern: Wasser- und Schifffahrtsamt; BG Verkehr; Staatsanwaltschaft.

## Rechtsrahmen
- HGB §§ 571-574: Große Havarie; Begriff; Beitragspflicht; Verteilung.
- HGB §§ 575-594: Dispache; Haverei-Verfahren; Beitragsberechnung.
- KSÜ 1910 (Kollisionsübereinkommen): internationale Haftungsverteilung; Verschuldensquoten.
- SeeUG §§ 1-6: Seeunfalluntersuchung durch Bundesstelle für Seeunfalluntersuchung (BSU).
- York-Antwerp Rules 2016: Vertragsstandard für Große-Havarie-Verteilung.
- UNCLOS Art. 97: kein Strafrecht durch Drittstaaten bei Hochseekollisionen.

## Prüfraster
- Liegt ein gemeinschaftliches Opfer vor das Große Havarie begründet?
- Welches Verschulden trifft welchen Reeder; KSÜ-Verschuldensquoten?
- Sind alle Ladungsinteressenten für Beitragspflicht identifiziert?
- Ist der P&I-Club bereit ein Letter of Undertaking statt Arrest zu stellen?
- Hat die BSU Untersuchungen eingeleitet?

## Typische Fallstricke
- Unterschied Große Havarie vs. Besondere Havarie: nicht jeder Schaden rechtfertigt YAR-Verteilung.
- UNCLOS Art. 97 schützt Kapitän vor ausländischer Strafverfolgung bei Hochseekollision; gilt nicht in Küstengewässern.
- BSU-Ergebnisse haben keine Bindungswirkung in Zivilprozessen; werden aber als Beweismittel verwendet.
- P&I-Club trägt Kollisionshaftung gegen andere Schiffe nur bis zu 3/4; 1/4 liegt bei H&M.

## Output
- Havarie-Erstbericht (Hergang; Schäden; Beteiligte; Zeugen)
- Dispache-Auftrag-Muster für Große Havarie
- Klagestrategie-Vermerk
- Checkliste Sofortmaßnahmen Unfallort und Versicherung


## Erweiterte Normengrundlage

### Kollisionsrecht
- HGB §§ 570-586: Schiffszusammenstoß; Schuldhaftung; Mittäterschaft; Sacheigentümerhaftung.
- HGB § 572: Kollisionshaftung; Verschuldensprinzip; Mitverschulden.
- COLREG 1972: Kollisionsverhütungsregeln; Ausweichpflichten; Anwendung als Sorgfaltsmaßstab.

### Große Havarie
- HGB §§ 588-597: Große Havarie; York-Antwerp-Rules (YAR) als lex specialis.
- YAR 2016: Dispacheurverfahren; Beitragsberechnung; Ladungsgläubigerrecht.
- HGB § 591: Dispache; Verbindlichkeit nach Rechtskraft.

## Checkliste Havarie-/Kollisionsfall
- [ ] Unfallhergang zeitlich dokumentiert; Zeugen benennt
- [ ] Logbuch und AIS-Daten gesichert
- [ ] Sea Protest (Seeprotest) vor Notar erklärt
- [ ] P&I-Korrespondent und Klasseninspektor am Schadensort informiert
- [ ] Schuldfrage vorläufig bewertet; COLREG-Verstoß analysiert
- [ ] Average Bond und Average Guarantee (Große Havarie) eingeholt
- [ ] Dispacheur benannt; Average Adjustment eingeleitet

## Relevante Rechtsprechung
- BGH zur Abgrenzung von kleiner und großer Havarie; Opfertheorie nach YAR.
- OLG Hamburg zur Kollisionshaftung; COLREG-Verletzung als Indiz für Verschulden.
- BGH zu Average-Guarantee-Klauseln; Bindungswirkung des Dispache-Beschlusses.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 571-594: https://dejure.org/gesetze/HGB/571.html
- KSÜ 1910: https://www.gesetze-im-internet.de/intv_ks_1910/
- BSU Seeunfalluntersuchung: https://www.bsu-bund.de
- SeeUG: https://www.gesetze-im-internet.de/seeug/
- YAR 2016 BIMCO: https://www.bimco.org

## 4. `see-010-bergung-und-wrack`

**Fokus:** Schiff strandet oder sinkt; Berger verlangen Bergungslohn; Wrackbeseitigung wird angeordnet. HGB §§ 574-583 (Bergung); WSG §§ 1-12 (Wrackbeseitigungsgesetz); WRC 2007 Nairobi-Uebereinkommen; LOF 2020; SCOPIC-Klausel. Output: Bergungslohn-Kalkulation; WRC-Pflichtenanalyse und Kostenrisiko-Matrix.

# Bergung und Wrack – Bergungslohn und Beseitigungspflicht

## Mandantenfall
Ein Bergungsschlepper rettet einen havarierten Frachter in der Nordsee; der Reeder verhandelt über den Bergungslohn; der Berger droht mit Lloyd's Schiedsverfahren. Ein Schiff sinkt in der deutschen AWZ; das WSA ordnet Wrackbeseitigung an; der Eigentümer fragt nach Kostentragung. Ein P&I-Club prüft ob SCOPIC höher ist als der konventionelle Bergungslohn.

## Erste Schritte
1. Bergevertrag prüfen: LOF 2020 (Lloyd's Open Form) oder freier Bergevertrag; LOF enthält SCOPIC-Klausel.
2. Bergungslohn-Voraussetzungen: HGB § 574 – Bergungserfolg als Grundvoraussetzung.
3. Bergungslohn nach HGB §§ 577-580 berechnen: Schiffswert; Bergungsrisiko; Umweltschutz-Erfolg; Zeitaufwand.
4. WSG-Anwendbarkeit prüfen: Wrack in deutschen Gewässern; WRC 2007 ab Schiff über 300 BRZ.
5. Meldepflichten: unverzügliche Anzeige beim WSA (WRC Art. 5); Versicherungsnachweis (WRC Art. 12).
6. Schutzmaßnahmen sichern: Bunkeröl und gefährliche Stoffe sofort sichern; MARPOL-Pflichten parallel.

## Rechtsrahmen
- HGB §§ 574-583: Bergung auf See; Bergungslohn-Berechnung; Sondervergütung; Ausschlüsse.
- HGB § 577: Kriterien für Bergungslohn (Schiffswert; Gefahr; Umweltschutz-Erfolg; Zeitaufwand).
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers; Behörde auf Kosten des Eigentümers.
- WRC 2007 Nairobi-Übereinkommen: internationales Wrackbeseitigungsübereinkommen.
- LOF 2020: Lloyd's Open Form Bergungsvertrag; Schiedsort London/Lloyd's.
- SCOPIC 2020: Special Compensation P&I Clubs; Alternativvergütung zum HGB-Bergungslohn.

## Prüfraster
- Ist ein Bergevertrag (LOF oder freier Vertrag) geschlossen?
- Wurde die Bergung erfolgreich abgeschlossen (Erfolgserfordernis HGB § 574)?
- Übersteigen die Bergungskosten den Schiffswert; dann nur SCOPIC?
- Greift WRC 2007 (Schiff über 14 Meter; in Gewässern eines Vertragsstaats)?
- Ist P&I-Deckung für Wrackbeseitigungskosten bestätigt?

## Typische Fallstricke
- LOF-Schiedsklausel verpflichtet zu London Arbitration; deutsches Gericht ist nicht zuständig.
- SCOPIC-Aktivierung durch P&I-Club kann Bergungslohnanspruch nach HGB verdrängen.
- WRC gilt auch für Freizeitjachten ab 14 Meter Länge.
- Versicherungspflicht für Wrackbeseitigungskosten (WRC Art. 12) greift ab 300 BRZ.

## Output
- Bergungslohn-Kalkulation nach HGB § 577 (Faktorenmatrix)
- WRC-Pflichtenanalyse: Fristen; Meldewege; Versicherungsnachweis
- Kostenrisiko-Matrix: Bergung; Wrack; Umwelt


## Erweiterte Normengrundlage

### Bergungsrecht
- HGB §§ 574-587: Bergung; Bergungslohn; Berechnungskriterien; Verteilungsregeln.
- LOF 2011 (Lloyd's Open Form): Standard-Bergungsvertrag; SCOPIC-Klausel.
- HGB § 576: Berücksichtigung des Umweltschutzes bei der Berechnungsmethode.

### Wrackbeseitigung
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers.
- WRC 2007 Nairobi: internationales Wrackbeseitigungsübereinkommen; AWZ-Anwendung.
- MARPOL Annex I Reg. 26: Bunkerölsicherheit; Gefahrenabwehr.

## Checkliste Bergungsfall
- [ ] Gefahr für Schiff und Ladung objektiv bewertet
- [ ] Freiwilligkeit der Bergungsleistung (kein Pre-existing Duty) bestätigt
- [ ] LOF oder anderen Bergungsvertrag unterzeichnet oder mündlich vereinbart
- [ ] Schiffslagen; Schiffstyp; Ladungsart für SCOPIC-Berechnung dokumentiert
- [ ] Umweltgefährdung (Bunkeröl; gefährliche Ladung) für special award bewertet
- [ ] P&I-Club zur Kostenteilung zwischen Schiff und Ladung eingebunden

## Relevante Rechtsprechung
- BGH zum Bergungslohn nach HGB § 578; Berücksichtigung des Erfolgs.
- OLG Hamburg zu SCOPIC-Klauseln; Schutz für Bergungsunternehmen bei erfolgloser Bergung.
- BGH zur Pfandhaftung des Bergungsunternehmers an Schiff und Ladung für den Bergungslohn.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- HGB §§ 574-583: https://dejure.org/gesetze/HGB/574.html
- WSG: https://www.gesetze-im-internet.de/wsg/
- WRC 2007 IMO: https://www.imo.org/en/About/Conventions/Pages/Nairobi-International-Convention-on-the-Removal-of-Wrecks.aspx
- BSH: https://www.bsh.de
- LOF 2020: https://www.lloyds.com

## 5. `see-011-pfaendung-und-arrest-schiff`

**Fokus:** Glaeubigervertreter beantragt Arrest gegen Schiff im deutschen Hafen: ZPO §§ 916-945 dinglicher Arrest; Vollziehung durch Registereintragung (SchRegO § 67); ISAC 1952 Seeforderungen. Klaert Arrestanspruch; Arrestgrund; Vollziehungsfrist; Sicherheitsleistung; LOU-Strategie. Output: Arrestantrags-Baustein und Freigabe-Strategie.

# Pfändung und Arrest am Schiff

## Mandantenfall
Ein Konnossementsinhaber will einen in Hamburg eingelaufenen Frachter arrestieren; Reeder verweigert Frachtzahlung. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch bevor das geborgene Schiff ausfährt. Ein Gläubiger aus ausländischem Urteil will das im Hamburger Hafen liegende Schiff pfänden.

## Erste Schritte
1. Zuständigkeit klären: Landgericht am Liegeplatz (ZPO § 919); Hamburg = LG Hamburg.
2. Arrestanspruch formulieren: bestehende Forderung gegen Schiffseigentümer oder Reeder (HGB § 476).
3. Arrestgrund darlegen: Schiff verlässt Hafen bei nächster Gelegenheit; Reeder zahlungsunfähig.
4. Arrestantrag stellen: ZPO § 920 – Anspruch und Arrestgrund glaubhaft machen; ohne Anhörung möglich.
5. Vollziehung sichern: ZPO § 929 – Vollziehungsfrist 1 Monat; Eintragung im Schiffsregister (SchRegO § 67).
6. Gegenmaßnahmen einschätzen: Letter of Undertaking des P&I-Clubs; Abwendung durch Sicherheitsleistung.

## Rechtsrahmen
- ZPO §§ 916-945: dinglicher Arrest und einstweilige Verfügung; Voraussetzungen; Vollziehung; Aufhebung.
- ZPO § 929: Vollziehungsfrist 1 Monat nach Beschlusszustellung.
- SchRegO § 67: Pfändungs- und Arrestvermerk im Seeschiffsregister.
- ISAC 1952: internationales Seearrestübereinkommen; definiert Seeforderungen die Arrest berechtigen.
- HGB §§ 596-601: gesetzliche Schiffsgläubigerrechte; bevorzugte Befriedigung ohne Arrest.
- ZPO § 945: Schadensersatz bei ungerechtfertigtem Arrest.

## Prüfraster
- Ist die Forderung eine Seeforderung im Sinne des ISAC 1952 Art. 1?
- Ist das Schiff im Hafen präsent und kann es noch verhindert werden?
- Liegt ein Arrestgrund vor (konkrete Fluchtgefahr)?
- Ist die Vollziehungsfrist von einem Monat einzuhalten?
- Hat der P&I-Club ein Letter of Undertaking angeboten?
- Besteht Risiko eines § 945-Schadensersatzes?

## Typische Fallstricke
- Arrest ohne Vollziehung (Registereintragung) bleibt wirkungslos; Schiff kann auslaufen.
- LOU beendet nur den Arrest; Forderungsverfolgung geht weiter.
- ZPO § 945-Schadensersatz kann erheblich sein; besonders bei Linienschiffen.
- ISAC 1952 gilt nur für Seeforderungen; Ansprüche aus Landtransport berechtigen nicht zum Schiffsarrest.

## Output
- Arrestantrags-Baustein (ZPO § 920) mit Glaubhaftmachung
- Vollziehungsstrategie: Register-Eintragung plus physische Bewachung
- Freigabe-Strategie: LOU; Sicherheitsleistung; Gegenantrag


## Erweiterte Normengrundlage

### Arrest und Pfändung
- ZPO §§ 916-945: Einstweiliger Rechtsschutz; Arrest; Vollziehung; Aufhebung.
- ZPO §§ 864-871: Zwangsvollstreckung in eingetragene Schiffe.
- ISAC 1952: Internationales Übereinkommen über den Arrest von Seeschiffen.

### Vollziehung
- SchRegO § 67: Eintragung von Pfändungs- und Arrestvermerken im Schiffsregister.
- ZPO § 930: Vollziehung des Arrests; Formen; Fristen.
- ZPO § 945: Schadensersatz bei ungerechtfertigtem Arrest.

## Checkliste Arrest-Vorbereitung
- [ ] Seeforderung nach ISAC 1952 Art. 1 identifiziert
- [ ] Schiff im Hafen bestätigt; Liegeplatz ermittelt
- [ ] LG am Liegeplatz als zuständiges Gericht bestimmt
- [ ] Arrestantrag (ZPO § 920) mit Glaubhaftmachung vorbereitet
- [ ] LOU des P&I-Clubs als Alternative zur Vollziehung geprüft
- [ ] § 945-Schadensersatzrisiko bewertet

## Relevante Rechtsprechung
- LG Hamburg; OLG Hamburg zu Seearrest; Anforderungen an Arrestanspruch und -grund.
- BGH zur Haftung aus ungerechtfertigtem Arrest nach ZPO § 945.
- ITLOS Juno Trader No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; Verhältnismäßigkeit.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- ZPO §§ 916-945: https://dejure.org/gesetze/ZPO/916.html
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- SchRegO § 67: https://dejure.org/gesetze/SchRegO/67.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- openjur LG Hamburg Arrest: https://www.openjur.de
