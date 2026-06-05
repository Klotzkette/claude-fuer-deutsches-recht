---
name: inv-us-auftrag
description: "Inv 010 Us Discovery, Inv 001 Auftrag Scope: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 010 Us Discovery, Inv 001 Auftrag Scope

## Arbeitsbereich

Dieser Skill bündelt **Inv 010 Us Discovery, Inv 001 Auftrag Scope** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-010-us-discovery` | Steuert das US-Discovery-Risiko bei Internal Investigations – FRCP, Attorney-Client Privilege, Work Product, Litigation Hold. |
| `inv-001-auftrag-scope` | Formuliert Untersuchungsauftrag, Scope, Ausschlüsse, Governance und Eskalation so eng wie möglich und so belastbar wie nötig. |

## Arbeitsweg

Für **Inv 010 Us Discovery, Inv 001 Auftrag Scope** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-010-us-discovery`

**Fokus:** Steuert das US-Discovery-Risiko bei Internal Investigations – FRCP, Attorney-Client Privilege, Work Product, Litigation Hold.

# US-Discovery in Cross-Border Investigations

## Rechtlicher Rahmen

US-amerikanische Discovery-Pflichten nach den Federal Rules of Civil Procedure (FRCP, insb. Rules 26, 34, 37) und in behördlichen Verfahren (DOJ, SEC) können alle Dokumente einer internen Untersuchung erfassen, die in den USA produziert oder dort gehostet wurden – unabhängig davon, ob das Unternehmen seinen Sitz in Deutschland hat. Das Attorney-Client Privilege und die Work-Product-Doctrine (Hickman v. Taylor, 329 U.S. 495 (1947)) sind die wichtigsten Schutzinstrumente, haben aber Grenzen, die im Konflikt mit deutschen Geheimhaltungsinteressen stehen.

## Ziel dieses Skills

Dieser Skill analysiert das US-Discovery-Risiko für laufende Internal Investigations, leitet Schutzmaßnahmen ab und klärt, welche Dokumente trotz Privilege-Anspruch offengelegt werden müssen.

## Arbeitsprogramm

### 1. Trigger für US-Discovery-Risiko
- US-Tochtergesellschaft als Partei in einem US-Verfahren.
- DOJ/SEC-Ermittlung wegen FCPA (Foreign Corrupt Practices Act, 15 U.S.C. § 78dd-1 ff.) oder Sanktionsverstößen.
- US-Gerichtsverfahren mit Bezug zu Unternehmenshandlungen.
- Hague Evidence Convention (HKUE) – Rechtshilfeersuchen aus den USA an deutsche Gerichte.

### 2. Litigation Hold nach FRCP 37(e)
- Ab „reasonable anticipation of litigation": alle relevanten Dokumente sichern (Electronically Stored Information, ESI).
- Failure to preserve = Spoliation; Sanktionen: adverse inference instruction, dismissal, monetary sanctions.
- Custodian-Liste und Hold-Notice nach US-Standard (ähnlich deutschem Legal Hold, aber ausdrücklich auf ESI ausgerichtet).
- Cloud-Dienste: US-CLOUD-Act (18 U.S.C. § 2713) erlaubt US-Behörden Zugriff auf Daten bei US-Providern weltweit.

### 3. Attorney-Client Privilege
- Schützt vertrauliche Kommunikation zwischen Anwalt und Mandant (hier: Unternehmen als Mandant).
- Upjohn Co. v. United States (449 U.S. 383, 1981): Privilege erfasst auch Kommunikation mit Mitarbeitern, wenn Anwalt sie im Rahmen der Rechtsberatung befragt hat.
- Waiver (Verzicht): freiwillige Offenlegung gegenüber Dritten (inkl. Behörden) kann Privilege aufheben; Selective Waiver in den USA nicht allgemein anerkannt.
- Crime-Fraud Exception: Privilege entfällt, wenn Kommunikation zur Begehung einer Straftat diente.

### 4. Work-Product Doctrine
- Hickman v. Taylor: schützt Anwaltsmaterialien, die in Erwartung eines Rechtsstreits erstellt wurden (mental impressions, conclusions, opinions).
- Stärkerer Schutz als Privilege für „opinion work product" (rechtliche Bewertungen des Anwalts).
- Schwächerer Schutz für „fact work product" (Tatsachenzusammenfassungen); kann bei substantial need überwindbar sein.
- Praktische Konsequenz: Anwalt sollte eigene rechtliche Bewertungen strikt von reinen Fakten-Summaries trennen.

### 5. Konflikt mit deutschem Datenschutzrecht
- Herausgabe personenbezogener Daten an US-Behörden: DSGVO Art. 49 Abs. 1 lit. e (Strafverfolgung) oder Standard Contractual Clauses.
- EU-Blocking-Statutes: einige EU-Länder verbieten Herausgabe bestimmter Daten; Deutschland hat kein allgemeines Blocking-Statute, aber DSGVO-Verpflichtungen gelten.
- Abstimmung mit deutsch-amerikanischen Doppelberatern zwingend.

### 6. DOJ/SEC-Kooperationsanreize und Discovery-Risiko
- DOJ Corporate Enforcement Policy: Selbstoffenbarung und Kooperation kann Ermessen bei Strafverfolgung beeinflussen.
- SEC Whistleblower Program: Hinweisgeber können direkt bei der SEC melden; Unternehmen kann nicht verhindern, dass interne Ermittlungsergebnisse bei SEC landen.
- Privilege Review vor jeder freiwilligen Herausgabe an US-Behörden.

### 7. eDiscovery-Prozess
- EDRM (Electronic Discovery Reference Model): Identification → Preservation → Collection → Processing → Review → Production.
- Keyword-Suche und Technologiegestützte Überprüfung (Technology-Assisted Review, TAR) für große Datenmengen.
- Privilege-Log: für alle zurückgehaltenen Dokumente (FRCP Rule 26(b)(5)); Anforderungen an Format und Inhalt.
- Redaktion (Schwärzung) sensibler Drittdaten vor Produktion.

## Red-Team-Fragen

- Gibt es US-Bezüge (Tochtergesellschaft, US-Cloud, FCPA-Risiko), die ein US-Discovery-Risiko begründen?
- Wurde ein Litigation Hold nach US-Standard ausgelöst, sobald ein US-Verfahren absehbar war?
- Ist jedes Dokument, das als „privileged" zurückgehalten wird, im Privilege-Log erfasst?
- Hat die freiwillige Herausgabe von Teilen des Berichts an das DOJ zu einem Subject-Matter-Waiver geführt?
- Wurden alle US-Cloud-Dienste auf CLOUD-Act-Risiken geprüft?
- Sind die deutschen und US-amerikanischen Anwälte koordiniert – insbesondere bei widersprüchlichen Pflichten?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| FRCP Rule 26 | General Discovery Obligations | US Federal Courts |
| FRCP Rule 37(e) | Spoliation Sanctions | US Federal Courts |
| 15 U.S.C. § 78dd-1 | FCPA Anti-Bribery | US Government |
| 18 U.S.C. § 2713 | US CLOUD Act | US Government |
| Art. 49 DSGVO | Drittstaaten-Transfer | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| EuGH C-550/07 P | Akzo Nobel / Inhouse Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **US-Discovery-Risikoampel** (Trigger × Privilegeschutz × Handlungsbedarf)
- **Litigation-Hold-Notice** nach US-Standard
- **Privilege-Log-Vorlage** (FRCP Rule 26(b)(5))
- **DSGVO-/US-Discovery-Konfliktanalyse**
- **DOJ-Kooperationsstrategie**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-001-auftrag-scope`

**Fokus:** Formuliert Untersuchungsauftrag, Scope, Ausschlüsse, Governance und Eskalation so eng wie möglich und so belastbar wie nötig.

# Untersuchungsauftrag und Scope

## Rechtlicher Rahmen

Der Untersuchungsauftrag legt die normative Grundlage jeder Internal Investigation fest. Ohne präzise Scope-Definition drohen Beweismittelüberschuss, Privilegverlust und Verwertungsprobleme. Die Pflicht des Vorstands zur Einleitung einer Untersuchung folgt aus § 93 Abs. 1 AktG (Business Judgment Rule) in Verbindung mit der BGH-Linie „Siemens/Neubürger" (BGH, Urt. v. 10.7.2012 – II ZR 234/09; [openjur](https://openjur.de/o/577696.html)), wonach der Vorstand ein Compliance-Management-System einzurichten hat, das Verstöße verhindert und aufklärt. Bei Verstößen durch Leitungspersonen greift § 130 OWiG (Aufsichtspflichtverletzung) gegenüber der Gesellschaft, Sanktion nach § 30 OWiG (Verbandsgeldbuße bis 10 Mio. EUR, zuzüglich Abschöpfung nach § 17 Abs. 4 OWiG); vgl. [gesetze-im-internet.de/owig/__130.html](https://www.gesetze-im-internet.de/owig/__130.html) und [gesetze-im-internet.de/owig/__30.html](https://www.gesetze-im-internet.de/owig/__30.html).

## Ziel dieses Skills

Dieser Skill erzwingt eine prüfbare Arbeitsspur: Sachverhalt → Norm → Tatbestandsmerkmal → Subsumtion → Gegenargument → Beleg → Ergebnis. Schematische Vorlagen werden bewusst vermieden; stattdessen werden Entscheidungsgabeln dokumentiert, die vor Gericht, der BaFin oder einem US-amerikanischen DOJ-Monitor standhalten.

## Arbeitsprogramm

### 1. Auftraggeber und Interessenlage
- Wer erteilt den Auftrag – Vorstand, Aufsichtsrat, Audit Committee, Sonderpruefungsausschuss?
- Liegt ein Interessenkonflikt beim Auftraggeber selbst vor (Betroffener im eigenen Verfahren)?
- Ist externe anwaltliche Unabhängigkeit gewährleistet (Attorney-Client Privilege / Anwaltsgeheimnis, ggf. nach EuGH Akzo Nobel, C-550/07 P, [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE))?

### 2. Scope-Festlegung
- Tatvorwurf präzise benennen: welche Norm (z. B. § 266 StGB Untreue, § 299 StGB Bestechung, FCPA, UK Bribery Act), welcher Zeitraum, welche Organisationseinheit, welche Personen?
- Nicht-Fragen schriftlich ausschließen, um späteren Scope Creep zu verhindern.
- Berichtspflichten nach HinSchG (Hinweisgeberschutzgesetz 2023, [gesetze-im-internet.de/hinschg/](https://www.gesetze-im-internet.de/hinschg/)) und EU-Hinweisgeberrichtlinie 2019/1937 ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019L1937)) berücksichtigen.

### 3. Governance und Eskalation
- Wer erhält Zwischenberichte, wer den Abschlussbericht?
- Welche Organe müssen informiert werden (Aufsichtsrat gem. § 111 AktG, Prüfungsausschuss)?
- Eskalationsmatrix: bei Verdacht auf Straftat → Strafanzeige, bei BaFin-Pflichten → Self-Reporting-Schwelle definieren.

### 4. Ressourcen und Zeitplan
- Welche Wirtschaftsprüfer, IT-Forensiker, Arbeitsrechtler werden beigezogen?
- Milestones für Legal Hold, Forensic Imaging, Interviewphase, Berichtsentwurf.
- Kostendokumentation für spätere Regressansprüche gegen Schadensverursacher (§ 249 BGB, § 93 Abs. 2 AktG).

### 5. Datenschutz von Anfang an
- DSGVO-Rechtsgrundlage für jede Datenverarbeitung vorab festlegen (§ 26 BDSG für Beschäftigtendaten, [gesetze-im-internet.de/bdsg_2018/__26.html](https://www.gesetze-im-internet.de/bdsg_2018/__26.html); Art. 6 Abs. 1 lit. f DSGVO bei berechtigtem Interesse).
- Datenminimierungsgebot (Art. 5 Abs. 1 lit. c DSGVO) in Scope-Dokument explizit verankern.
- Betriebsrat frühzeitig einbinden (§§ 80, 87 BetrVG); Verwertungsverbote bei fehlender Mitbestimmung prüfen.

## Red-Team-Fragen

- Ist der Scope eng genug, oder entsteht ein Beweisordner, der Behörden, Gegner oder US-Discovery nützt?
- Wer ist Mandant, wer Berichtsadressat, wer potenziell Beschuldigter – und kollidiert das mit Anwaltsgeheimnis, Berufsrecht oder Organpflichten?
- Welche Daten müssen gesichert werden, welche dürfen nicht breit kopiert werden, und wo greift Datenminimierung?
- Sind Interviewrolle, arbeitsrechtliche Mitwirkungspflicht, Schweigerecht, Betriebsratsbeteiligung und Protokollstandard vor Beginn geklärt?
- Welche Berichtsversion kann beschlagnahmt (§§ 94 ff. StPO), herausverlangt, geleakt oder in einem Parallelverfahren verwendet werden?
- Löst die Untersuchung Meldepflichten aus (HinSchG § 12 ff., WpHG § 119, DSGVO Art. 33)?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Sorgfaltspflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 111 AktG | Aufgaben Aufsichtsrat | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__111.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| § 30 OWiG | Verbandsgeldbuße | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__30.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| HinSchG | Hinweisgeberschutz 2023 | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |
| BGH II ZR 234/09 | Siemens/Neubürger | [openjur.de](https://openjur.de/o/577696.html) |

## Ausgabeformate

Erzeuge je nach Bedarf:
- **Untersuchungsplan** (Scope-Dokument mit Nicht-Fragen, Governance, Zeitplan)
- **Board Memo** (einseitige Zusammenfassung für Aufsichtsrat)
- **Risikoampel** (Rot/Gelb/Grün je Tatvorwurf, Norm und Eskalationsstufe)
- **Interviewleitfaden** (differenziert nach Zeugen, Betroffenen, Leitungspersonen)
- **Verteidigungsdossier** (Gegenargumente zu jedem Tatbestandsmerkmal)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Weiterführende Hinweise

- Der Untersuchungsauftrag ist kein statisches Dokument; er muss bei wesentlichen neuen Erkenntnissen angepasst und die Anpassung dokumentiert werden.
- Kostenkontrolle: Untersuchungsbudget realistisch planen; Überschreitungen müssen dem Auftraggeber rechtzeitig kommuniziert werden.
- Parallelverfahren: wenn zeitgleich strafrechtliche oder aufsichtsrechtliche Verfahren laufen, muss der Untersuchungsauftrag diese berücksichtigen und Informationsflüsse kontrollieren.
- Scope-Creep-Protokoll: jede Erweiterung des Scope wird schriftlich vom Auftraggeber freigegeben und dokumentiert.
