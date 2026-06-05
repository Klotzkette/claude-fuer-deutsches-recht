---
name: chn-lieferantenmapping-tier-single-source
description: "CHN Lieferantenmapping Tier Single Source: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CHN Lieferantenmapping Tier Single Source

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **CHN Lieferantenmapping Tier Single Source** im Plugin Festlandchina Wirtschaftsverkehr. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `chn-006-lieferantenmapping-tier-1-bis-tier-n` | Systematisches Lieferantenmapping bis Tier-3/Tier-n für China-Lieferketten: Datenerhebung, Tier-Klassifizierung, China-Exponiertheits-Score, LkSG-Risikoanalyse §§ 5-7, BAFA-Relevanzprüfung, Forced-Labour-Screening (XUAR). Output: Lieferanten-Mapping-Vorlage mit Risikoscore und Prüfungsplan. |
| `chn-007-single-source-risk` | Bewertung und Minderung von Single-Source-Risiken bei China-Lieferanten: Identifikation monopolartiger Bezugsquellen, Kritikalitätsbewertung nach CRMA und LkSG § 5, Notfallplanung, Dual-Sourcing-Optionen, vertragliche Absicherung (Force-Majeure, Lieferpflichten). Output: Single-Source-Risikobericht mit Handlungsoptionen. |
| `chn-008-dual-sourcing-und-china-plus-one` | Planung und Umsetzung von Dual-Sourcing-Strategien und China-Plus-One-Modellen: Alternativstandorte (Vietnam/Indien/Mexiko), Make-or-Buy-Analyse, LkSG-Konformität neuer Lieferanten, Kostenmodell, Vertragsstruktur Parallellieferanten, BAFA-Freigabe für Technologietransfer. Output: Dual-Sourcing-Businessplan und Lieferantenvertragsgerüst. |
| `chn-009-fabrikbetrieb-in-china` | Rechtlicher und operativer Rahmen für Fabrikbetrieb in der VR China: Betriebsgenehmigungen, Umweltauflagen (chinesisches Umweltschutzgesetz), Arbeitssicherheit (Work Safety Law CN), Datenlokalisierung (Cybersecurity Law Art. 37), LkSG-Sorgfaltspflichten aus Deutschland, Notfallplanung. Output: Operations-Compliance-Checkliste und Behörden-Mapping. |

## Arbeitsweg

Im Plugin Festlandchina Wirtschaftsverkehr gilt für **CHN Lieferantenmapping Tier Single Source**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `chn-006-lieferantenmapping-tier-1-bis-tier-n`

**Fokus:** Systematisches Lieferantenmapping bis Tier-3/Tier-n für China-Lieferketten: Datenerhebung, Tier-Klassifizierung, China-Exponiertheits-Score, LkSG-Risikoanalyse §§ 5-7, BAFA-Relevanzprüfung, Forced-Labour-Screening (XUAR). Output: Lieferanten-Mapping-Vorlage mit Risikoscore und Prüfungsplan.

# Lieferantenmapping Tier-1 bis Tier-n: China-Exposition erfassen

## Fachkern: Lieferantenmapping Tier-1 bis Tier-n: China-Exposition erfassen
- **Spezialgegenstand:** Lieferantenmapping Tier-1 bis Tier-n: China-Exposition erfassen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Automobilzulieferer muss nach LkSG nachweisen, dass er seine mittelbaren Lieferanten in China kennt.

**Fall 2:** Ein Elektronikhersteller will prüfen, ob Tier-2-Lieferanten Komponenten aus XUAR beziehen.

**Fall 3:** Eine Beschaffungsabteilung sucht eine Vorlage für strukturiertes Lieferantenmapping für China-Einkauf.

## Erste Schritte

1. Direkte Lieferanten (Tier-1) identifizieren: Vertragspartner mit China-Bezug.
2. Tier-2 ermitteln: Selbstauskunft Tier-1 oder Einkaufsberichte anfordern.
3. Tier-3 und tiefer: Fokus auf Rohstoffquellen und XUAR-Bezüge.
4. China-Expositions-Score je Lieferant berechnen: Umsatzanteil, Substituierbarkeit, XUAR-Bezug.
5. LkSG-Risikoindikatoren ergänzen: Menschenrechts-, Umwelt-, Arbeitsrechtsrisiken.
6. BAFA-Relevanzprüfung: Dual-Use-Güter in der Lieferkette identifizieren.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- §§ 5-7 LkSG: Risikoanalyse, unmittelbare und mittelbare Zulieferer.
- § 10 LkSG: Beschwerdeverfahren für Lieferkettenrisiken.
- EU CSDDD (2024/1760) Art. 8: Sorgfaltspflichten für mittelbare Geschaeftsbeziehungen.
- XUAR-Bezug: Uyghur Forced Labor Prevention Act (USA) als Compliance-Referenz (kein DE-Recht).
- BAFA-Merkblatt Dual-Use: Güter in Lieferkette auf AL-Listung prüfen.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Sind alle Tier-1-Lieferanten mit China-Bezug identifiziert?
- Gibt es Hinweise auf XUAR-Ursprung von Materialien (Baumwolle, Polysilizium, Aluminium)?
- Sind kritische Single-Source-Lieferanten in der Mapping-Matrix markiert?
- Werden LkSG-Risikoindikatoren für jeden Lieferanten dokumentiert?
- Gibt es Lücken im Mapping unterhalb Tier-2?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Tier-1-Fokus als LkSG-Fehler: Mittelbare Zulieferer müssen bei konkreten Hinweisen ebenfalls geprüft werden.
- Selbstauskünfte ungeprüft übernommen: Lieferanten-Fragebogen ohne Audit ist unzureichend.
- XUAR-Bezug schwer nachweisbar: Kein Zertifikat belegt zweifelsfrei XUAR-Freiheit.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Output

Lieferanten-Mapping-Vorlage (Tier-1 bis Tier-n), China-Expositions-Score, Risiko-Ampel, Prüfungsplan, LkSG-Risikomatrix.

Der Output ist als direktes Arbeitsprodukt nutzbar: Memo, Klausel, Checkliste oder Board-Paper.
Unsicherheiten werden sichtbar gemacht; Live-Check-Bedarf wird markiert.

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU CSDDD EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1760)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)
- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)

## 2. `chn-007-single-source-risk`

**Fokus:** Bewertung und Minderung von Single-Source-Risiken bei China-Lieferanten: Identifikation monopolartiger Bezugsquellen, Kritikalitätsbewertung nach CRMA und LkSG § 5, Notfallplanung, Dual-Sourcing-Optionen, vertragliche Absicherung (Force-Majeure, Lieferpflichten). Output: Single-Source-Risikobericht mit Handlungsoptionen.

# Single-Source-Risiko China: Bewertung und Notfallplanung

## Fachkern: Single-Source-Risiko China: Bewertung und Notfallplanung
- **Spezialgegenstand:** Single-Source-Risiko China: Bewertung und Notfallplanung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Pharmaunternehmen bezieht 80 Prozent eines API-Wirkstoffs ausschließlich von einem chinesischen Hersteller.

**Fall 2:** Ein Elektronikhersteller hat keinen Alternativlieferanten für eine spezifische Halbleiter-Komponente aus China.

**Fall 3:** Eine Rechtsabteilung fragt, wie Single-Source-Risiken vertraglich abgesichert werden können.

## Erste Schritte

1. Single-Source-Güter identifizieren: Produktgruppen ohne alternativen Lieferanten.
2. Kritikalitätsbewertung: Produktionsausfall bei Lieferstop, Zeithorizont Substitution.
3. Lieferantenrisiken prüfen: Staatsbeteiligung, XUAR-Bezug, Finanzkraft, Compliance-Status.
4. Vertragliche Analyse: Bestehen Force-Majeure-, Lieferpflicht- und Pönale-Klauseln?
5. Dual-Sourcing-Optionen identifizieren: Kosten, Qualität, Vorlaufzeit.
6. Notfallplan erstellen: Lagerhaltung, Substitutionsplan, Kommunikationspflichten.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- § 5 LkSG: Risikoanalyse muss Abhängigkeiten von einzelnen Lieferanten erfassen.
- Critical Raw Materials Act EU 2024: Strategische Rohstoffe dürfen nicht über 65 Prozent aus einem Drittland bezogen werden.
- § 313 BGB: Wegfall der Geschäftsgrundlage bei Lieferausfall.
- § 275 BGB: Unmöglichkeit der Leistung bei Exportverbot Ursprungsland.
- Force-Majeure-Klauseln in Verträgen nach CISG Art. 79.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Welche Güter haben keinen außerchinesischen Alternativlieferanten?
- Wie lange kann die Produktion ohne den China-Lieferanten aufrechterhalten werden?
- Sind Puffer-Lagerbestände definiert und finanziert?
- Bestehen vertragliche Lieferverpflichtungen gegenüber Kunden, die gefährdet sind?
- Gibt es regulatorische Diversifizierungspflichten (CRMA, LkSG)?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Scheinvielfalt: Mehrere chinesische Lieferanten aus dem gleichen Ort/Konzern sind kein Dual-Sourcing.
- Force-Majeure-Lücke: Exportverbote werden in vielen Klauseln nicht als Force Majeure anerkannt.
- Substitution teurer als gedacht: Qualitätsunterschiede erfordern oft teure Neuzulassungen.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Output

Single-Source-Risikobericht (Güter, Kritikalität, Optionen), Dual-Sourcing-Roadmap, Notfallplan-Vorlage, Vertragsklausel-Empfehlung.

Der Output ist als direktes Arbeitsprodukt nutzbar: Memo, Klausel, Checkliste oder Board-Paper.
Unsicherheiten werden sichtbar gemacht; Live-Check-Bedarf wird markiert.

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [Critical Raw Materials Act EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1252)
- [BGB Volltext §§ 275 und 313](https://www.gesetze-im-internet.de/bgb/)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)
- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)

## 3. `chn-008-dual-sourcing-und-china-plus-one`

**Fokus:** Planung und Umsetzung von Dual-Sourcing-Strategien und China-Plus-One-Modellen: Alternativstandorte (Vietnam/Indien/Mexiko), Make-or-Buy-Analyse, LkSG-Konformität neuer Lieferanten, Kostenmodell, Vertragsstruktur Parallellieferanten, BAFA-Freigabe für Technologietransfer. Output: Dual-Sourcing-Businessplan und Lieferantenvertragsgerüst.

# Dual-Sourcing und China-Plus-One: Planung und Umsetzung

## Fachkern: Dual-Sourcing und China-Plus-One: Planung und Umsetzung
- **Spezialgegenstand:** Dual-Sourcing und China-Plus-One: Planung und Umsetzung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Elektronikhersteller will Vietnam als Alternativstandort zu Shenzhen aufbauen und benötigt rechtliche Strukturierung.

**Fall 2:** Ein Automobilzulieferer prüft, ob er seine China-Produktion zu 30 Prozent nach Indien verlagern kann.

**Fall 3:** Eine Beschaffungsabteilung sucht einen Mustervertrag für Parallellieferanten mit technischen Spezifikationen.

## Erste Schritte

1. Alternativstandorte evaluieren: Vietnam, Indien, Mexiko, Thailand, Malaysia nach Kosten/Qualität/Risiko.
2. Make-or-Buy-Analyse: Eigenfertigung vs. neuer Lieferant im Zielland.
3. LkSG-Due-Diligence für neue Lieferanten im Alternativland.
4. BAFA prüfen: Erfordert Technologietransfer an Alternativlieferant eine Exportgenehmigung?
5. Vertragsstruktur festlegen: Technologie-Lizenzvertrag, Qualitätssicherungsvertrag, Abnahmeverpflichtung.
6. Kostenmodell erstellen: Anlaufkosten, Zertifizierungskosten, Logistikveränderungen.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- §§ 5-6 LkSG: Risikoanalyse und Präventionsmaßnahmen auch für neue Lieferanten.
- §§ 55-62a AWV: Technologietransfer an Nicht-EU-Lieferant kann AWV-Prüfpflicht auslösen.
- BAFA AL-Liste: Überprüfung ob Technologie zu Alternativlieferant genehmigungspflichtig.
- EU-VO 2021/821 (Dual-Use-VO): Neue Abnehmerstruktur muss auf Endverbleib geprüft werden.
- § 307 BGB: AGB-Kontrolle bei Lieferantenverträgen (Qualitäts- und Haftungsklauseln).

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Erfüllen Alternativlieferanten technische Mindestanforderungen (Qualität, Kapazität, Zertifizierung)?
- Sind LkSG-Risikoindikatoren für Alternativstandorte geprüft?
- Erfordert Technologietransfer BAFA-Exportgenehmigung?
- Gibt es Produkthaftungsrisiken durch Qualitätsschwankungen beim Lieferantenwechsel?
- Sind Abnahmeverpflichtungen gegenüber altem China-Lieferant vertraglich geregelt?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- China-Plus-One als Alibi: Lieferant in Vietnam bezieht Vorprodukte weiterhin aus China.
- Technologietransfer ohne BAFA-Prüfung: Rüge und ggf. Bußgeld.
- Qualitätsprobleme bei neuem Lieferant: Produktrückruf und Kundenhaftung.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Output

Dual-Sourcing-Businessplan, Alternativstandort-Bewertungsmatrix, LkSG-Checkliste für neue Lieferanten, Vertragsgerüst.

Der Output ist als direktes Arbeitsprodukt nutzbar: Memo, Klausel, Checkliste oder Board-Paper.
Unsicherheiten werden sichtbar gemacht; Live-Check-Bedarf wird markiert.

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [EU Dual-Use VO 2021/821](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [AWV Volltext](https://www.gesetze-im-internet.de/awv_2013/)
- [BGB Volltext](https://www.gesetze-im-internet.de/bgb/)

## 4. `chn-009-fabrikbetrieb-in-china`

**Fokus:** Rechtlicher und operativer Rahmen für Fabrikbetrieb in der VR China: Betriebsgenehmigungen, Umweltauflagen (chinesisches Umweltschutzgesetz), Arbeitssicherheit (Work Safety Law CN), Datenlokalisierung (Cybersecurity Law Art. 37), LkSG-Sorgfaltspflichten aus Deutschland, Notfallplanung. Output: Operations-Compliance-Checkliste und Behörden-Mapping.

# Fabrikbetrieb in China: Rechtlicher Rahmen und Compliance

## Fachkern: Fabrikbetrieb in China: Rechtlicher Rahmen und Compliance
- **Spezialgegenstand:** Fabrikbetrieb in China: Rechtlicher Rahmen und Compliance wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AWG/AWV, EU-Dual-Use, Sanktionen, Zoll/USt, Incoterms, Lieferkette/LkSG/CSDDD, IP-/Know-how-Schutz, Datenschutz/Cybersecurity und lokale China-Compliance live prüfen.
- **Entscheidende Weiche:** Ordne Lieferant, Werk, Datenfluss, Zahlungsweg, Exportgut, politisches Risiko, IP-Leck und Exit-Szenario getrennt.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Dieser Skill begleitet Mandanten und Berater im Wirtschaftsverkehr mit der Volksrepublik China.
Ausgangspunkt ist der konkrete Mandantenfall; Ergebnis ist stets ein verwertbares Arbeitsprodukt.

## Mandantenfall

**Fall 1:** Ein Maschinenbauer betreibt eine eigene Fertigung in Suzhou und fragt nach aktuellen Auflagen für Umwelt und Arbeitssicherheit.

**Fall 2:** Eine Rechtsabteilung prüft, ob eine Produktionsstätte in China unter das chinesische Cybersecurity Law fällt.

**Fall 3:** Ein Finanzvorstand fragt, welche Behördengenehmigungen bei Erweiterung der Fabrik erneuert werden müssen.

## Erste Schritte

1. Betriebsgenehmigungen inventarisieren: Business License, Umweltgenehmigung, Feuerschutz, Arbeitssicherheit.
2. Umweltauflagen chinesisches Umweltschutzgesetz (Huanjing Baohu Fa) prüfen: Emissionen, Abwasser, Abfall.
3. Work Safety Law (Anquan Shengchan Fa) compliance prüfen: Unfall-Meldepflichten, Sicherheitsbeauftragter.
4. Datenlokalisierung: Cybersecurity Law Art. 37 – welche Daten dürfen die VR China nicht verlassen?
5. LkSG-Pflichten aus Deutschland: Eigene Betriebe in China sind unmittelbare Zulieferer nach § 2 LkSG.
6. Notfallplan für behördliche Inspektion und Dawn Raid erstellen.

## Rechtsrahmen

Verbindliches Recht und anerkannte Soft-Law-Quellen für diesen Skill:

- Cybersecurity Law VR China (Wangluo Anquan Fa) Art. 37: Datenlokalisierung für CII-Betreiber.
- Work Safety Law VR China (Anquan Shengchan Fa): Arbeitssicherheitspflichten.
- Umweltschutzgesetz VR China (Huanjing Baohu Fa): Genehmigungen, Meldepflichten.
- §§ 3-5 LkSG: Eigene Auslandsbetriebe zählen als unmittelbare Zulieferer im Sinne des Gesetzes.
- EU CSDDD 2024/1760 Art. 7: Sorgfaltspflichten für eigene Tätigkeiten im Ausland.

Quellen sind getrennt nach deutschem Recht, EU-Recht und chinesischem Recht zu handhaben.
Bei Widersprüchen gilt: Verbindliches Recht geht Soft Law vor; aktueller Stand ist zu prüfen.

## Prüfraster

Schritt für Schritt abzuarbeiten, Ergebnisse dokumentieren:

- Sind alle Betriebsgenehmigungen aktuell und vollständig?
- Werden Umwelt- und Arbeitssicherheitsauflagen eingehalten und dokumentiert?
- Ist Datenlokalisierung nach Cybersecurity Law implementiert?
- Sind LkSG-Sorgfaltspflichten für eigenen Betrieb in China erfüllt?
- Gibt es eine Notfall-Kommunikationskette für behördliche Inspektionen?

## Typische Fallstricke

Aus der Beratungspraxis: Diese Fehler sollten aktiv vermieden werden.

- Business License abgelaufen: Betrieb kann sofort eingestellt werden.
- Datentransfer aus China ohne Genehmigung: Cybersecurity Law verletzt, empfindliche Bußgelder.
- LkSG-Übersehen: Eigene Fabrik gilt als eigene Tätigkeit, nicht nur als Zulieferer.

## Gegenposition

Folgende Gegenargumente sind im Mandantengespräch zu adressieren:

- Behörde (BMWK/BAFA): Behältst du den Ermessensspielraum der Behörde im Blick?
- Vertragspartner China: Welche Interessen und Risikobewertungen hat die chinesische Seite?
- Investoren/Aufsichtsrat: Sind ESG- und Menschenrechts-Anforderungen berücksichtigt?
- Compliance: Wurde auf Exportkontroll- und Sanktions-Risiken geprüft?

## Output

Operations-Compliance-Checkliste, Behörden-Mapping, Datenlokalisierungs-Übersicht, LkSG-Prüfbericht eigene Tätigkeiten.

Der Output ist als direktes Arbeitsprodukt nutzbar: Memo, Klausel, Checkliste oder Board-Paper.
Unsicherheiten werden sichtbar gemacht; Live-Check-Bedarf wird markiert.

## Quellen

Nur frei prüfbare Quellen aus erlaubten Domains. Rechtsprechung nur mit Gericht und Datum.

- [LkSG Volltext](https://www.gesetze-im-internet.de/lksg/)
- [EU CSDDD EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L1760)
- [BAFA Außenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)
- [BMWK China-Strategie](https://www.bmwk.de/Redaktion/DE/Artikel/Aussenwirtschaft/china-strategie.html)
- [AWG Volltext](https://www.gesetze-im-internet.de/awg_2013/)
