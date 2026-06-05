---
name: inv-us-settlement
description: "Inv 052 Us Counsel Coordination, Inv 053 Settlement Narrative: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 052 Us Counsel Coordination, Inv 053 Settlement Narrative

## Arbeitsbereich

Dieser Skill bündelt **Inv 052 Us Counsel Coordination, Inv 053 Settlement Narrative** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-052-us-counsel-coordination` | Koordiniert die Zusammenarbeit zwischen deutschem und US-amerikanischem Counsel in Cross-Border-Investigations – Privilege-Konflikte, Offenbarungspflichten, Joint-Defense. |
| `inv-053-settlement-narrative` | Entwickelt das Settlement-Narrativ für Behörden und Öffentlichkeit – DPA/NPA-Formulierungen, Faktenbasis, Schuldanerkenntnis-Grenzen, Präzedenzwirkung. |

## Arbeitsweg

Für **Inv 052 Us Counsel Coordination, Inv 053 Settlement Narrative** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-052-us-counsel-coordination`

**Fokus:** Koordiniert die Zusammenarbeit zwischen deutschem und US-amerikanischem Counsel in Cross-Border-Investigations – Privilege-Konflikte, Offenbarungspflichten, Joint-Defense.

# US-Counsel-Koordination in Cross-Border-Investigations

## Rechtlicher Rahmen

Cross-Border-Investigations mit US-Bezug (FCPA, SEC, DOJ) erfordern die enge Koordination zwischen deutschem und US-amerikanischem Anwalt. Unterschiede im Privilege-Recht (deutsches Anwaltsgeheimnis vs. US Attorney-Client Privilege), in den Discovery-Pflichten und in den Selbstbelastungsrechten erzeugen erhebliche Friktionen. Joint-Defense-Agreements schützen die Kommunikation zwischen Co-Counsel verschiedener Parteien; ohne sie riskiert jede Partei, dass Kommunikation mit anderen Verteidigern privilegienmäßig nicht geschützt ist. Der EuGH (Akzo Nobel, C-550/07 P, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE)) und das US-Recht unterscheiden sich fundamental beim Inhouse-Counsel-Privilege.

## Ziel dieses Skills

Dieser Skill strukturiert die Koordination zwischen deutschem und US-Counsel so, dass Privilege-Verluste vermieden, widersprüchliche Aussagen gegenüber Behörden verhindert und strategische Entscheidungen konsistent getroffen werden.

## Arbeitsprogramm

### 1. Aufgabenteilung zwischen deutschem und US-Counsel
- **Deutsches Recht**: deutsches Straf- und Ordnungswidrigkeitenrecht (§§ 266, 263, 299 StGB; §§ 30, 130 OWiG), Arbeitsrecht, Datenschutz, BetrVG, HinSchG.
- **US-Counsel**: FCPA, SEC-Regulierung, DOJ-Verfahren, US-Discovery, SOX, OFAC-Sanktionen.
- **Gemeinsame Felder**: Privilege-Strategie, Behördenstrategie, Berichtsstrategie, Settlement.
- Lead Counsel-Festlegung: wer kommuniziert mit welcher Behörde?

### 2. Joint-Defense-Agreement (JDA)
- Schützt Kommunikation zwischen Anwälten verschiedener Co-Defendants.
- Voraussetzung: gemeinsames Verteidigungsinteresse.
- Inhalt: Gemeinsam-nutzbarer Informationsaustausch; Verbot der unilateralen Weitergabe an Dritte; Exit-Regelung bei Interessenkonflikt.
- Deutsches Recht: vergleichbare Schutzfunktion über Berufsgeheimnis (§ 203 StGB) und § 97 StPO.
- Achtung: JDA schützt nicht, wenn eine Partei „flips" (mit Behörde kooperiert und die anderen belastet).

### 3. Privilege-Koordination
- US-Dokumente: US Attorney-Client Privilege gilt für US-Counsel-Kommunikation; Work-Product-Doctrine für Arbeitsdokumente.
- Deutsche Dokumente: § 97 StPO; kein EU-Privilege für Inhouse-Counsel (EuGH Akzo Nobel).
- Cross-Border-Problem: Dokument, das nach US-Recht privilegiert ist, kann nach deutschem Recht beschlagnahmt werden, und umgekehrt.
- Gemeinsame Privilege-Strategie: alle Beratungskommunikation über einen privilegierten Kanal laufen lassen.

### 4. Behörden-Koordination
- DOJ/SEC vs. BaFin/Staatsanwaltschaft: Widersprüchliche Aussagen gegenüber verschiedenen Behörden sind katastrophal.
- „One Voice"-Strategie: alle Aussagen gegenüber Behörden werden zentral zwischen deutschem und US-Counsel abgestimmt.
- DOJ-Kooperationsanforderungen vs. deutsches Datenschutzrecht: kein unkontrolliertes Herausgeben von DSGVO-geschützten Daten an US-Behörden.
- Simultane Kooperation: wenn DOJ und StA gleichzeitig Kooperation erwarten.

### 5. Zeugenbefragungen in den USA
- US-Grand-Jury-Subpoena für deutsche Mitarbeiter: problematisch wegen Territorialitätsprinzip; Rechtshilfe-Verfahren eigentlich erforderlich.
- MLAT (Mutual Legal Assistance Treaty): Germany-US MLAT regelt formelle Rechtshilfe.
- Deutsche Mitarbeiter haben Recht auf deutschen Anwalt neben US-Anwalt.
- Testimony vor Grand Jury: erhebliches Selbstbelastungsrisiko; Fifth Amendment gilt für US-Personen, nicht für ausländische Staatsbürger.

### 6. Dritte Counsel in Drittstaaten
- UK: UK Bribery Act erfordert ggf. englischen Anwalt.
- Frankreich: französisches Droit à la preuve vs. US-Discovery.
- China: Datenlokalisierungsgesetze verbieten Transfer von Daten an ausländische Behörden.
- Koordination: Country-Counsel für jeden betroffenen Rechtsraum; Lead Counsel koordiniert.

### 7. Settlement-Koordination
- DOJ-DPA/NPA: Abstimmung zwischen US-Counsel und deutschem Anwalt.
- Deutsches OWiG-Bußgeld: parallele Verhandlung.
- Kein Widerspruch: was das Unternehmen dem DOJ zugegeben hat, kann in deutschen Strafverfahren gegen Individuen verwendet werden.

## Red-Team-Fragen

- Gibt es widersprüchliche Aussagen gegenüber DOJ und deutschen Behörden?
- Ist ein Joint-Defense-Agreement in Kraft, und schützt es die Kommunikation zwischen allen Co-Defendants?
- Wurden US-Dokumente dem DOJ übergeben, ohne die DSGVO-Rechtsgrundlage für den Transfer zu prüfen?
- Ist der „One-Voice"-Ansatz tatsächlich umgesetzt – werden alle Behördenkommunikationen koordiniert?
- Hat das Unternehmen bei der Grand-Jury-Befragung die Interessen der deutschen Mitarbeiter gewahrt?
- Gibt es Drittstaaten (UK, Frankreich, China), die eigene Counsel-Koordination erfordern?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 97 StPO | Beschlagnahmeschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html) |
| § 203 StGB | Berufsgeheimnis | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__203.html) |
| Art. 49 DSGVO | Drittstaatentransfer | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |
| 15 U.S.C. § 78dd-1 | FCPA | US Government |

## Ausgabeformate

- **Counsel-Koordinationsplan** (Aufgabenteilung, Lead Counsel)
- **Joint-Defense-Agreement-Template**
- **Privilege-Matrix** (Dokument × deutsches Recht × US-Recht)
- **Behörden-Kommunikations-Protokoll** (One-Voice)
- **DSGVO-/US-Discovery-Konfliktanalyse**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-053-settlement-narrative`

**Fokus:** Entwickelt das Settlement-Narrativ für Behörden und Öffentlichkeit – DPA/NPA-Formulierungen, Faktenbasis, Schuldanerkenntnis-Grenzen, Präzedenzwirkung.

# Settlement-Narrativ und Verfahrensabschluss

## Rechtlicher Rahmen

Das Settlement-Narrativ ist die narrative Grundlage für den Abschluss eines behördlichen Verfahrens. Bei US-DOJ-DPA/NPA enthält es eine „Statement of Facts", die das Unternehmen als faktisch zutreffend anerkennt. Im deutschen OWiG-Bußgeldverfahren enthält der Bußgeldbescheid eine Sachverhaltsdarstellung. Das Narrativ hat erhebliche Bedeutung für zivilrechtliche Nachfolgeklagen (US: Private Class Actions; Deutschland: Aktionärsklagen), für die Reputationswirkung und für die Grundlage des Compliance-Monitors.

## Ziel dieses Skills

Dieser Skill gestaltet das Settlement-Narrativ so, dass es die Kooperationsanforderungen der Behörden erfüllt, die eigenen Interessen des Unternehmens schützt und keine unnötigen Schuldanerkennungen enthält.

## Arbeitsprogramm

### 1. Statement of Facts (US-DOJ)
- Inhalt: chronologischer Tatsachenbericht; was hat das Unternehmen als Tatsache anerkannt?
- Zielsetzung aus Unternehmenssicht: keine unnötigen Schuldanerkennungen; Sachverhalt möglichst präzise auf spezifische Handlungen begrenzen.
- Verhandlungspositionen: welche Formulierungen sind problematisch für private Nachfolgeklagen?
- „Knowing and willful conduct": DOJ bevorzugt diese Formulierung; Unternehmen will möglicherweise „negligent" oder „certain employees" als Subjekt.

### 2. Sachverhaltsdarstellung im deutschen Bußgeldbescheid
- Bußgeldbescheid enthält Sachverhaltsdarstellung, die das Gericht im Einspruchsverfahren überprüft.
- Einspruch: Unternehmen kann gegen Bußgeldbescheid Einspruch einlegen; riskiert höheres Bußgeld.
- Verhandlungslösung: mit Staatsanwaltschaft oder Behörde eine Sachverhaltsdarstellung aushandeln.
- § 153a StPO: Verfahrenseinstellung gegen Geldauflage bei weniger schweren Straftaten.

### 3. Schuldanerkenntnis-Grenzen
- Was das Unternehmen in einem Settlement anerkennt, kann in nachfolgenden Zivilklagen als Beweis verwendet werden.
- US: Collateral Estoppel – einmal als Tatsache anerkannt, kann es nicht mehr bestritten werden.
- Deutschland: Bußgeldbescheid als Indiz in Zivilklagen, aber nicht bindend.
- Strategische Entscheidung: ist es besser, weite Sachverhalte anzuerkennen (DOJ-Bonus), oder drohen erhebliche Folgeschäden durch Zivilklagen?

### 4. Präzedenzwirkung
- US-Settlement-DPAs: veröffentlicht; wirken als Blaupause für zukünftige DOJ-Verfahren.
- Unternehmensform: wie wird das Unternehmen im Statement of Facts bezeichnet? Als „rücksichtsloser Krimineller" oder als „Unternehmen mit Compliance-Lücken"?
- Formulierungen, die systemisches Versagen nahelegen, erhöhen Regressansprüche gegen Organmitglieder.

### 5. Koordination mit Zivilklagen-Risiko
- US Class Actions: Aktionärsklagen nach Securities Exchange Act; Settlement-Narrativ ist Munition für Kläger.
- Deutsche Aktionärsklagen: § 148 AktG (Sonderprüfung) und § 147 AktG (Geltendmachung von Schadensersatzansprüchen).
- Abwägung: schnelles Settlement mit DOJ kann Zivilklagen-Exposition erhöhen; langwieriges Verfahren erhöht DOJ-Sanktionsrisiko.

### 6. Öffentliche Kommunikation des Settlements
- Statement of Facts wird veröffentlicht; Pressemitteilung des DOJ ist häufig ungünstiger formuliert als das Settlement selbst.
- Vorbereitung: Unternehmen sollte eigene Pressemitteilung gleichzeitig mit DOJ herausgeben.
- CEO-Statement: persönliche Verantwortungsübernahme als Reputationsmaßnahme (ohne strafrechtliches Eingeständnis).
- Kundenkommunikation: key accounts und wichtige Geschäftspartner vorab informieren.

### 7. Nachfolgende Verfahren
- Monitor: Settlement enthält oft Monitor-Anforderungen (vgl. inv-046-monitor-reporting).
- Compliance-Programm-Anforderungen: häufig als Teil des DPA.
- Cooperation Obligation: Unternehmen verpflichtet sich zur weiteren Kooperation bei Ermittlungen gegen Individuen.
- Auflösungsbedingungen: was muss das Unternehmen tun, damit das DPA/NPA ausläuft?

## Red-Team-Fragen

- Enthält das Statement of Facts Formulierungen, die in einer US Class Action gegen das Unternehmen verwendet werden könnten?
- Wurden Schuldanerkennungen auf das absolut Notwendige beschränkt?
- Hat das Unternehmen eine eigene Pressemitteilung vorbereitet, die gleichzeitig mit der DOJ-Veröffentlichung herausgeht?
- Welche Organmitglieder werden im Statement of Facts namentlich oder funktional erwähnt – mit welcher Konsequenz für Regressansprüche?
- Enthält das Settlement Cooperation-Klauseln, die das Unternehmen bei der Verfolgung von Individuen binden?
- Ist das Settlement mit allen parallelen Behördenverfahren (BaFin, StA, SEC) koordiniert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 153a StPO | Verfahrenseinstellung gegen Auflage | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__153a.html) |
| § 147 AktG | Schadensersatzklage Aktionäre | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__147.html) |
| § 148 AktG | Sonderprüfung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__148.html) |
| Art. 17 MAR | Ad-hoc-Pflicht bei Settlement | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596) |

## Ausgabeformate

- **Statement-of-Facts-Analyse** (Formulierungs-Risiken, Schuldanerkennungen)
- **Verhandlungsprotokoll** für DOJ/BaFin-Settlements
- **Zivilklage-Risikoanalyse** nach Settlement
- **CEO-Statement-Vorlage** (Verantwortungsübernahme ohne strafrechtliches Geständnis)
- **Pressemitteilungs-Template** für Settlement-Ankündigung

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
