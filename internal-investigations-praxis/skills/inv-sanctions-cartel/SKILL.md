---
name: inv-sanctions-cartel
description: "Inv 030 Sanctions Hit, Inv 031 Cartel Dawn Raid: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 030 Sanctions Hit, Inv 031 Cartel Dawn Raid

## Arbeitsbereich

Dieser Skill bündelt **Inv 030 Sanctions Hit, Inv 031 Cartel Dawn Raid** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-030-sanctions-hit` | Reagiert auf einen Sanktionstreffer – EU-Sanktionsverordnungen, OFAC, Einfrierung, Meldepflichten, Strafrisiken und Behördenstrategie. |
| `inv-031-cartel-dawn-raid` | Behandelt Kartellrechtsdurchsuchungen durch Bundeskartellamt oder EU-Kommission – Mitwirkungspflichten, Leniency, Privilege, Kronzeugenantrag. |

## Arbeitsweg

Für **Inv 030 Sanctions Hit, Inv 031 Cartel Dawn Raid** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-030-sanctions-hit`

**Fokus:** Reagiert auf einen Sanktionstreffer – EU-Sanktionsverordnungen, OFAC, Einfrierung, Meldepflichten, Strafrisiken und Behördenstrategie.

# Sanktionstreffer – Sofortmaßnahmen und Behördenstrategie

## Rechtlicher Rahmen

Sanktionsverstöße sind strafrechtlich nach § 18 AWG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__18.html)) und nach EU-Sanktionsverordnungen (z. B. VO (EU) Nr. 269/2014 Russland, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0269)) bußgeldbewehrt. EU-Sanktionen verpflichten Finanzinstitute und Unternehmen, Gelder und wirtschaftliche Ressourcen sanktionierter Personen einzufrieren (Art. 2 ff. der jeweiligen Sanktions-VO) und Treffer zu melden. US-Sanktionen (OFAC, 50 U.S.C. § 1701 ff.) haben extraterritoriale Reichweite. Ein Sanktionstreffer erfordert sofortiges, koordiniertes Handeln.

## Ziel dieses Skills

Dieser Skill definiert die Sofortmaßnahmen nach einem Sanktionstreffer und leitet die weiteren Schritte (Einfrierung, Meldung, Behördenkommunikation) ab.

## Arbeitsprogramm

### 1. Sofortmaßnahmen beim Treffer
- **Transaktion stoppen**: Zahlung oder Lieferung sofort aussetzen.
- **Einfrierung der Gelder**: Art. 2 der jeweiligen EU-Sanktions-VO; unmittelbare Pflicht, keine Verzögerung.
- **Interne Eskalation**: Compliance-Beauftragter, General Counsel, CFO informieren; keine eigenständigen Entscheidungen auf Sachbearbeiterebene.
- **Keine Warnung an Sanktionierten**: § 261 StGB (Geldwäsche) und Sanktions-VO verbieten Vorwarnung.

### 2. Überprüfung des Treffers (False Positive vs. True Positive)
- Name-Matching-Probleme: Falltreffer durch ähnliche Namen, falsche Schreibweise.
- Due-Diligence-Dokumentation: OFAC-SDN-Liste, EU-Consolidated-Sanctions-List prüfen; Screenshot und Zeitstempel sichern.
- Birthdate, Nationality, Address: alle verfügbaren Identifikatoren abgleichen.
- Zweifelhafte Treffer: OFAC-Specific-License-Antrag oder Anfrage bei Bundesamt für Wirtschaft und Ausfuhrkontrolle (BAFA).

### 3. Meldepflichten
- **EU-Meldepflichten**: Art. 8 der meisten EU-Sanktions-VO verpflichtet zur Meldung eingefrorener Gelder an nationale Behörden (in Deutschland: Deutsche Bundesbank oder BAFA, je nach Sanktionsregime).
- **OFAC Reporting**: freiwillige oder zwingende Meldung; OFAC-SDN-Treffermeldung im Rahmen des Blocked Persons Reporting.
- **Geldwäschemeldung**: § 43 GwG – Sanktionstreffer kann gleichzeitig Verdachtsmeldung auslösen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/__43.html)).
- BaFin: bei Kreditinstituten und Finanzdienstleistern gesonderte Meldepflichten.

### 4. Einfrierungs-Management
- Gesperrte Konten und Gelder separat verwalten; keine Transaktionen ohne Genehmigung.
- Zinsen und andere Erträge aus eingefrorenen Mitteln: ebenfalls einfrieren (EU-Sanktions-VO).
- Lizenzanträge: bestimmte Transaktionen können mit Genehmigung durchgeführt werden (EU Art. 5 ff.; OFAC General/Specific License).

### 5. Rückwirkende Analyse
- Historische Transaktionen prüfen: gab es frühere Zahlungen an dieselbe Person/Entität?
- Sanktionslisten rückwirkend anwenden: ab wann stand die Person auf der Liste?
- Kumulierter Schadensbetrag für OFAC-Penalty-Berechnung.

### 6. OFAC-Voluntary Disclosure
- Substantieller Selbstanzeigeeffekt: Basisstrafe wird halbiert.
- Inhalt: vollständige Chronologie, betroffene Transaktionen, Namen, Beträge, Maßnahmen.
- Timing: schnell, aber nach vollständiger interner Untersuchung.
- Gleichzeitig prüfen: DOJ-Exposure bei strafrechtlicher Relevanz.

### 7. Remediation
- Sanktionsscreening verbessern (Fuzzy Matching, Phonetic Matching, PEP-Screening).
- Compliance-Programm-Update: neue Sanktionsregime implementieren (z. B. nach neuen EU-Verordnungen).
- Training: alle relevanten Mitarbeiter.
- Externe Überprüfung: OFAC Compliance Commitment-Dokument oder EU-Compliance-Programm-Assessment.

## Red-Team-Fragen

- Wurde die Transaktion sofort gestoppt, oder gab es eine Verzögerung durch interne Entscheidungsprozesse?
- Ist der Treffer ein True Positive? Wurden alle verfügbaren Identifikatoren geprüft?
- Wurden alle Meldepflichten (EU-Behörde, BAFA, BaFin, OFAC) innerhalb der vorgesehenen Fristen erfüllt?
- Gibt es historische Transaktionen mit derselben sanktionierten Entität, die eine kumulierte OFAC-Penalty begründen?
- Hat das Compliance-Team den sanktionierten Kunden vorgewarnt? (Verbotsverstoß!)
- Ist eine OFAC-Voluntary Disclosure sinnvoll, und wurde die Entscheidung dokumentiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 18 AWG | Straftatbestände Sanktionsverstoß | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/__18.html) |
| § 43 GwG | Geldwäsche-Verdachtsmeldung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/__43.html) |
| VO (EU) Nr. 269/2014 | Russland-Sanktionen | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0269) |
| BAFA | Behördeninfos Sanktionen | [bafa.de](https://www.bafa.de/) |

## Ausgabeformate

- **Sanktionstreffer-Sofortprotokoll** (Ausfüllvorlage)
- **True/False-Positive-Prüfcheckliste**
- **Meldepflichten-Matrix** (EU-Behörde, BAFA, BaFin, OFAC)
- **OFAC-Voluntary-Disclosure-Vorlage**
- **Remediation-Plan** Sanktions-Compliance

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-031-cartel-dawn-raid`

**Fokus:** Behandelt Kartellrechtsdurchsuchungen durch Bundeskartellamt oder EU-Kommission – Mitwirkungspflichten, Leniency, Privilege, Kronzeugenantrag.

# Kartell-Dawn-Raid und Leniency

## Rechtlicher Rahmen

Kartellrechtliche Durchsuchungen durch das Bundeskartellamt (§ 59 GWB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__59.html)) oder die EU-Kommission (Art. 20 VO (EG) Nr. 1/2003, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32003R0001)) sind unter Wettbewerbsrecht besonders mächtig: weitgehende Befugnisse, kurze Reaktionszeiten und der Zeitdruck des Kronzeugenprogramms erzeugen eine Ausnahmesituation. Zuwiderhandlungen gegen Art. 101 AEUV oder § 1 GWB können Bußgelder bis 10 % des weltweiten Konzernumsatzes auslösen (Art. 23 VO 1/2003; § 81 GWB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__81.html)).

## Ziel dieses Skills

Dieser Skill stellt das korrekte Verhalten bei Kartell-Nachprüfungen sicher, schützt Privilege-Rechte und analysiert die Kronzeugen-Option zeitkritisch.

## Arbeitsprogramm

### 1. Sofortmaßnahmen beim Erscheinen der Behörde
- Nachprüfungsberechtigte feststellen: EU-Kommission (Inspektoren) oder Bundeskartellamt (Beamte)?
- Prüfungsmandat verlangen (Art. 20 VO 1/2003 oder § 59 GWB).
- Anwalt sofort benachrichtigen; kein Interview ohne Anwalt.
- Mitarbeiter anweisen: keine Aussagen zur Sache; keine Dokumente verschieben oder löschen.
- Zeuge hinzuziehen (§ 106 StPO analog / § 60 GWB).

### 2. Besonderheiten der EU-Kommissions-Nachprüfung
- Art. 20 VO 1/2003: Kommissionsbeamte können Büroräume betreten, Bücher und Unterlagen prüfen, kopieren, versiegeln.
- Anwaltszugang: Unternehmen hat Recht auf sofortigen Zugang zum Anwalt, aber Nachprüfung wird nicht aufgehalten.
- Privilege: nur externe Anwälte (nicht Inhouse Counsel) nach EuGH C-550/07 P (Akzo Nobel, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE)) geschützt.
- Versiegelung: Kommissionsbeamte können Räume versiegeln; Verstöße sind bußgeldbewehrt.

### 3. Kronzeugenprogramm (Leniency)
- **EU-Kronzeugenmitteilung**: vollständige Immunität für erstes antragstellendes Unternehmen; erhebliche Bußgeldreduktion für nachfolgende.
- **Bundeskartellamt Bonusregelung**: analog; vollständige Bußgeldfreiheit für Erstantragsteller.
- **Race to the regulator**: Kronzeugenantrag muss zeitlich vor Wettbewerbern gestellt werden.
- Inhalt des Antrags: vollständige Beschreibung des Kartells (Dauer, Teilnehmer, Marktgebiete, Absprachen), verfügbare Beweise.
- Marker-System: Sicherung des Vorrangs durch vorläufigen Antrag.

### 4. Während der Nachprüfung
- Zugangskontrolle: Beamte nur in Bereichen, die das Mandat deckt.
- Kopien: von allem, was kopiert oder beschlagnahmt wird, eigene Kopien anfertigen.
- Privilegierungsanspruch: alle Anwaltsdokumente kennzeichnen und Anspruch sofort erklären.
- Keine falschen Aussagen gegenüber Behörde: Strafbarkeit nach nationalem Recht; bei EU-Kommission: Bußgeld nach Art. 23 Abs. 1 lit. c VO 1/2003.
- Pflicht zur Vorlage: Dokumente müssen vorgelegt werden, aber Auskunft auf Tatsachen beschränkt (kein Selbstbelastungszwang).

### 5. Parallele nationale Ermittlungen
- Bei Unternehmensgeldbußen: § 30 OWiG; individuelle Strafbarkeit leitender Mitarbeiter nach §§ 298, 263 StGB.
- Koordination der Selbstdarstellung zwischen Bundeskartellamt- und EU-Kommissions-Verfahren.
- Private Schadensersatzklagen: nach Bußgeldbescheid sind Dritte berechtigt, Schadensersatz einzuklagen (§ 33a GWB, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__33a.html)).

### 6. Post-Raid-Maßnahmen
- Vollständige Dokumentation der Nachprüfung (vgl. inv-021-dawn-raid-playbook).
- Anforderung einer Kopie des vollständigen Nachprüfungsprotokolls.
- Entscheidung über Kronzeugenantrag: zeitkritisch; nach Raid nur noch reduzierte Immunität möglich.
- Interne Compliance-Untersuchung: parallel einleiten, um Sachverhalt vollständig zu erfassen.

### 7. Remediation und Settlement
- EU-Settlement-Verfahren: reduziertes Bußgeld gegen Eingeständnis und schnelleres Verfahren (Art. 10a VO (EG) Nr. 773/2004, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0773)).
- Compliance-Programm als strafmildernder Faktor.
- Remediation-Maßnahmen dokumentieren für Bußgeldbemessung.

## Red-Team-Fragen

- Wurde die Kronzeugen-Option bereits vor dem Raid analysiert und eine Entscheidung getroffen?
- Haben Beamte Zugang zu Anwaltsdokumenten gehabt, ohne dass Widerspruch eingelegt wurde?
- Gibt es parallele Ermittlungen in anderen Ländern, und ist die Kronzeugenstrategie koordiniert?
- Hat das Unternehmen die Nachprüfung vollständig protokolliert?
- Wurden private Schadensersatzklagen nach dem Bußgeldbescheid antizipiert?
- Wurden alle betroffenen Mitarbeiter über ihre Rechte und Pflichten informiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 59 GWB | Nachprüfungsbefugnis Bundeskartellamt | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__59.html) |
| § 81 GWB | Bußgelder | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__81.html) |
| § 33a GWB | Schadensersatz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwb/__33a.html) |
| Art. 20 VO 1/2003 | EU-Nachprüfung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32003R0001) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **Kartell-Raid-Sofortprotokoll**
- **Kronzeugenantrag-Checkliste** (EU + Bundeskartellamt)
- **Privilege-Widerspruchs-Formulierung**
- **Post-Raid-Dokumentationsvorlage**
- **Settlement-Entscheidungsmatrix**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
