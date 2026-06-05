---
name: inv-bank-gdpr
description: "Inv 040 Bank Regulatory Finding, Inv 041 Gdpr Fine Parallel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 040 Bank Regulatory Finding, Inv 041 Gdpr Fine Parallel

## Arbeitsbereich

Dieser Skill bündelt **Inv 040 Bank Regulatory Finding, Inv 041 Gdpr Fine Parallel** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-040-bank-regulatory-finding` | Reagiert auf BaFin-Prüfungsfeststellungen und aufsichtsrechtliche Findings – Mängelbeseitigungspflicht, Anordnungsbefugnisse, Internal Investigation als Reaktion. |
| `inv-041-gdpr-fine-parallel` | Koordiniert parallele DSGVO-Bußgeldverfahren mit Internal Investigations – Aufsichtsbehörden-Kommunikation, Selbstbelastungsschutz, Kooperation. |

## Arbeitsweg

Für **Inv 040 Bank Regulatory Finding, Inv 041 Gdpr Fine Parallel** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-040-bank-regulatory-finding`

**Fokus:** Reagiert auf BaFin-Prüfungsfeststellungen und aufsichtsrechtliche Findings – Mängelbeseitigungspflicht, Anordnungsbefugnisse, Internal Investigation als Reaktion.

# BaFin-Prüfungsfeststellungen und Bankregulatorik

## Rechtlicher Rahmen

Die BaFin hat weitgehende Aufsichts- und Eingriffsbefugnisse nach dem KWG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/)), dem WpHG, dem GwG und dem VAG. Prüfungsfeststellungen der BaFin verpflichten das betroffene Institut zur Mängelbeseitigung (§ 25a Abs. 1 KWG: Anforderungen an die ordnungsgemäße Geschäftsorganisation, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25a.html)) und können Anordnungen nach § 45 KWG (Maßnahmen zur Verbesserung der Eigenkapital- und Liquiditätslage) oder § 46 KWG (Maßnahmen bei Gefahr) auslösen. Nicht-Behebung kann zu Abberufung von Organmitgliedern führen (§ 36 KWG).

## Ziel dieses Skills

Dieser Skill strukturiert die Reaktion auf BaFin-Prüfungsfeststellungen: Internal Investigation als Reaktionsmechanismus, Maßnahmenplanung und behördliche Kommunikation.

## Arbeitsprogramm

### 1. Kategorisierung der Prüfungsfeststellung
- **Kritische Feststellung** (MaRisk/MaComp-Verstöße): systemic deficiencies in Risikomanagement, IKS, Compliance.
- **Erhebliche Feststellung**: Einzelverstöße gegen WpHG, GwG, MiFID II.
- **Anzeigepflichtige Ereignisse**: §§ 24, 25a KWG (z. B. wesentliche Änderungen der Geschäftsorganisation).
- **Schwere Verstöße**: Straftat-Verdacht (§ 25h KWG: Pflicht zur Verdachtsmeldung, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25h.html)).

### 2. Sofortmaßnahmen nach Prüfungsfeststellung
- Feststellungs-Protokoll vollständig auswerten; alle Mängel inventarisieren.
- Interne Eskalation: Vorstand, Aufsichtsrat, Prüfungsausschuss informieren.
- Rechtsberater hinzuziehen: wann ist eine Stellungnahme gegenüber BaFin erforderlich?
- Fristen prüfen: BaFin setzt regelmäßig Fristen zur Mängelbeseitigung; Fristversäumnisse können Anordnungen auslösen.

### 3. Internal Investigation als Reaktion
- Bei Hinweisen auf individuelle Pflichtverletzungen (z. B. Händler hat interne Limits verletzt): Investigation einleiten.
- Scope: welche Personen, welche Transaktionen, welcher Zeitraum?
- Ergebnisse der Investigation in BaFin-Stellungnahme einbeziehen (kontrollierte Offenbarung).
- Arbeitsrechtliche Konsequenzen nach Abschluss.

### 4. MaRisk und MaComp-Anforderungen
- MaRisk (Mindestanforderungen an das Risikomanagement, Bundesbank/BaFin-Rundschreiben): IKS, Risikosteuerung, Compliance-Funktion.
- MaComp (Mindestanforderungen an Compliance, BaFin-Rundschreiben): Wertpapierdienstleistungsunternehmen.
- AT 9 MaRisk: Outsourcing-Kontrollen; bei Feststellungen zu Drittparteien.
- Compliance-Funktion (§ 25a Abs. 1 S. 3 Nr. 3c KWG): unabhängig, ressourcenstark, direkter Zugang zum Vorstand.

### 5. GwG-Feststellungen
- § 25h KWG: Verdachtsmeldepflicht bei Geldwäsche-Hinweisen aus BaFin-Prüfung.
- GwG §§ 43, 44: Pflicht zur Meldung an FIU (Financial Intelligence Unit).
- Sonderprüfungen: BaFin kann bei konkretem GwG-Verdacht Sonderprüfer (§ 44 KWG) einsetzen.

### 6. Kommunikation mit BaFin
- Stellungnahme: sachlich, vollständig, kein Herunterspielen von Mängeln.
- Maßnahmenplan: konkrete Schritte mit Verantwortlichen und Fristen; BaFin erwartet Umsetzungsberichte.
- Eskalation: wenn BaFin eine formelle Anordnung erwägt, sofort externe Anwälte einschalten.
- Anwaltsgeheimnis: Stellungnahme-Entwürfe über Anwalt kommunizieren, um Privilege zu wahren.
- Self-Reporting: bei eigenständig entdeckten Verstößen proaktive Meldung vor BaFin-Entdeckung ([bafin.de](https://www.bafin.de/)).

### 7. Organhaftung und persönliche Konsequenzen
- § 36 KWG: BaFin kann Abberufung eines Geschäftsleiters verlangen, wenn er für Mängel verantwortlich ist.
- § 56 KWG: Bußgelder für Organmitglieder bei schwerwiegenden Verstößen.
- § 93 AktG i. V. m. BGH II ZR 234/09: Vorstand haftet intern bei schuldhafter Nichtbehebung von Compliance-Mängeln.
- D&O-Versicherung: Deckungsschutz für Untersuchungskosten und Abwehrmaßnahmen prüfen.

## Red-Team-Fragen

- Sind alle BaFin-Feststellungen vollständig inventarisiert und priorisiert?
- Gibt es unter den Feststellungen Hinweise auf individuelle Pflichtverletzungen, die eine separate Internal Investigation erfordern?
- Ist die Kommunikation mit der BaFin in allen Punkten präzise und vollständig – keine Halbwahrheiten?
- Wurden alle erforderlichen GwG-Verdachtsmeldungen abgegeben?
- Ist der Maßnahmenplan realistisch und wurden die Fristen eingehalten?
- Haben Organmitglieder persönliche Abberufungsrisiken (§ 36 KWG), und wurde die D&O-Deckung geprüft?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 25a KWG | Ordnungsgemäße Geschäftsorganisation | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25a.html) |
| § 36 KWG | Abberufung Geschäftsleiter | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__36.html) |
| § 25h KWG | Verdachtsmeldung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25h.html) |
| § 43 GwG | Geldwäsche-Verdachtsmeldung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/__43.html) |
| BaFin | Aufsichtspraxis | [bafin.de](https://www.bafin.de/) |

## Ausgabeformate

- **Feststellungs-Inventar** (Kritische / erhebliche / sonstige Mängel)
- **Maßnahmenplan** mit Verantwortlichen und Fristen
- **BaFin-Stellungnahmen-Template**
- **GwG-Verdachtsmeldungs-Prüfcheckliste**
- **Organhaftungs-Risikoanalyse** (§ 36 KWG, D&O)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-041-gdpr-fine-parallel`

**Fokus:** Koordiniert parallele DSGVO-Bußgeldverfahren mit Internal Investigations – Aufsichtsbehörden-Kommunikation, Selbstbelastungsschutz, Kooperation.

# Parallele DSGVO-Bußgeldverfahren

## Rechtlicher Rahmen

DSGVO-Verstöße können Bußgelder bis 20 Mio. EUR oder 4 % des weltweiten Jahresumsatzes auslösen (Art. 83 DSGVO, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)). Die Datenschutzaufsichtsbehörden der Länder (z. B. BayLDA, HmbBfDI, BfDI) führen eigene Verfahren und können parallel zu einer Internal Investigation Untersuchungen einleiten. Der Konflikt zwischen kooperativer Behördenstrategie und Selbstbelastungsschutz ist besonders scharf, weil die DSGVO einerseits Kooperation honoriert (Art. 83 Abs. 2 DSGVO), aber keine formelle Kronzeugenregel kennt.

## Ziel dieses Skills

Dieser Skill koordiniert die parallele Führung von Internal Investigation und DSGVO-Aufsichtsverfahren und minimiert das Risiko, dass die Untersuchungsergebnisse das behördliche Verfahren unkontrolliert beeinflussen.

## Arbeitsprogramm

### 1. Parallelität identifizieren
- Liegt bereits eine Beschwerde bei der Datenschutzbehörde vor?
- Hat die Behörde von Amts wegen Ermittlungen eingeleitet (Art. 57 Abs. 1 lit. a DSGVO)?
- Ist eine Datenpanne gemeldet worden (Art. 33 DSGVO), die nun zum Ausgangspunkt einer Untersuchung wird?
- Timeline: wann wurde welche Behörde auf welchem Weg informiert?

### 2. Selbstbelastungsschutz (nemo tenetur) im DSGVO-Verfahren
- Unternehmen: kein formelles nemo-tenetur-Recht, aber Verhältnismäßigkeitsgrundsatz und Verfahrensrechte.
- Stellungnahmen gegenüber Aufsichtsbehörde können in späteren Bußgeldverfahren verwendet werden.
- Vorsicht: übermäßige Selbstoffenbarung kann eigene Interessen schädigen; Abstimmung mit Anwalt zwingend.
- EuGH-Rechtsprechung: Kooperationspflicht hat Grenzen bei der Offenbarung von Informationen, die strafbar sind.

### 3. Koordination Internal Investigation und Aufsichtsverfahren
- Paralleluntersuchung muss dieselben Fakten klären, aber unterschiedliche Adressaten bedienen.
- Internal Investigation: vollständige Sachverhaltsaufklärung für das Unternehmen.
- Aufsichtsverfahren: kontrollierte Kommunikation, keine Vorwegnahme von Ergebnissen ohne Strategie.
- Kein vollständiger Untersuchungsbericht an Aufsichtsbehörde ohne Privilegierungsanalyse.

### 4. Art. 83 DSGVO – Bußgeldbemessung und Kooperationsanreize
- Art. 83 Abs. 2 lit. f DSGVO: Zusammenarbeit mit der Aufsichtsbehörde zur Abhilfe des Verstoßes ist strafmildernder Faktor.
- Proaktive Meldung nach Art. 33 DSGVO vor Behördenentdeckung: Kooperationsbonus.
- Art. 83 Abs. 2 lit. c: Kategorie personenbezogener Daten und Schwere des Schadens als Erschwernis.
- Gegenmaßnahmen und Remediation bereits während der Untersuchung einleiten.

### 5. Grenzüberschreitende Verfahren (One-Stop-Shop)
- Art. 56 DSGVO: federführende Aufsichtsbehörde ist die des Hauptsitzes des Unternehmens (One-Stop-Shop).
- Art. 60 DSGVO: Kohärenzverfahren zwischen Aufsichtsbehörden; Europäischer Datenschutzausschuss (EDSA).
- Bei mehreren betroffenen Mitgliedstaaten: koordinierte Strategie für alle nationalen Behörden.

### 6. Betroffenenrechte im Parallelverfahren
- Betroffene können Auskunftsrecht (Art. 15 DSGVO) geltend machen – auch zu Untersuchungsdokumenten.
- § 29 BDSG: Einschränkung des Auskunftsrechts während laufender Untersuchung.
- Kein Recht auf Akteneinsicht im Aufsichtsverfahren für Betroffene, aber Recht auf Stellungnahme.
- Koordination: keine widersprüchlichen Aussagen gegenüber Betroffenen und Behörde.

### 7. DSGVO-Compliance-Remediation
- Unmittelbare Behebung des Verstoßes (Art. 83 Abs. 2 lit. f DSGVO honoriert dies ausdrücklich).
- Datenschutz-Folgenabschätzung (Art. 35 DSGVO) für betroffene Prozesse.
- Verfahrensverzeichnis (Art. 30 DSGVO) aktualisieren.
- Schulung und Awareness-Programm.
- DSB mit ausreichenden Ressourcen ausstatten (Art. 38 Abs. 2 DSGVO).

## Red-Team-Fragen

- Gibt es Stellungnahmen gegenüber der Datenschutzbehörde, die im Bußgeldverfahren gegen das Unternehmen verwendet werden könnten?
- Wurde die Kooperation mit der Behörde als Bußgeld-mildernder Faktor bewusst eingesetzt?
- Sind alle Betroffenen-Rechts-Anfragen (Art. 15 DSGVO) korrekt beantwortet – und sind die Antworten konsistent mit den Behördenaussagen?
- Hat das Unternehmen die Datenpanne rechtzeitig gemeldet (Art. 33: 72 Stunden), oder liegt eine Verletzung der Meldepflicht vor?
- Wurde die federführende Aufsichtsbehörde (One-Stop-Shop, Art. 56) korrekt identifiziert?
- Sind die Remediation-Maßnahmen bereits eingeleitet und dokumentiert?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 83 DSGVO | Bußgelder | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 33 DSGVO | Datenpannenmeldung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 56 DSGVO | One-Stop-Shop | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 29 BDSG | Einschränkung Auskunftsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__29.html) |

## Ausgabeformate

- **Parallelverfahren-Koordinationsplan** (Investigation × Aufsichtsverfahren)
- **Behördenkommunikations-Strategie** (kontrollierte Offenbarung)
- **Bußgeldbemessungs-Analyse** (Art. 83 Faktoren)
- **Remediation-Nachweis** für Aufsichtsbehörde
- **Art.-15-Anfragen-Antwortprotokoll**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
