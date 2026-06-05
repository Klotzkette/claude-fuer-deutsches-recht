---
name: inv-accounting-cyber
description: "Inv 032 Accounting Irregularity, Inv 033 Cyber Incident: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 032 Accounting Irregularity, Inv 033 Cyber Incident

## Arbeitsbereich

Dieser Skill bündelt **Inv 032 Accounting Irregularity, Inv 033 Cyber Incident** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-032-accounting-irregularity` | Untersucht Bilanzierungsunregelmäßigkeiten und Bilanzfälschung – forensische Buchprüfung, § 331 HGB, Abschlussprüferhaftung, SEC-Meldungen. |
| `inv-033-cyber-incident` | Reagiert auf Cyber-Incidents (Ransomware, Datenleck, APT) – DSGVO-Meldepflichten, forensische Sicherung, Behördenstrategie, Strafverfolgung. |

## Arbeitsweg

Für **Inv 032 Accounting Irregularity, Inv 033 Cyber Incident** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-032-accounting-irregularity`

**Fokus:** Untersucht Bilanzierungsunregelmäßigkeiten und Bilanzfälschung – forensische Buchprüfung, § 331 HGB, Abschlussprüferhaftung, SEC-Meldungen.

# Bilanzierungsunregelmäßigkeiten und Accounting-Forensik

## Rechtlicher Rahmen

Bilanzmanipulationen sind strafbar nach § 331 HGB (Unrichtige Darstellung, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__331.html)) und § 400 AktG (Unrichtige Darstellung in Lageberichten, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__400.html)). Bei kapitalmarktorientierten Gesellschaften kommt § 38 WpHG in Verbindung mit MAR Art. 15 (Marktmanipulation) hinzu. Der Abschlussprüfer haftet nach §§ 323, 321 HGB. Bei US-Listing gelten SOX Section 302/906 (CEO/CFO-Zertifizierungspflicht) und SEC Rule 10b-5.

## Ziel dieses Skills

Dieser Skill strukturiert die forensische Buchprüfung und klärt die strafrechtlichen, regulatorischen und haftungsrechtlichen Konsequenzen von Bilanzierungsunregelmäßigkeiten.

## Arbeitsprogramm

### 1. Kategorisierung der Unregelmäßigkeit
- **Revenue Recognition Fraud**: vorzeitige oder fiktive Umsatzverbuchung (channel stuffing, bill-and-hold).
- **Expense Deferral**: Kosten in Folgejahre verschoben, um Jahresergebnis zu verbessern.
- **Asset Overstatement**: Überbewertung von Vorräten, Forderungen, immateriellen Vermögenswerten.
- **Liability Understatement**: Verbindlichkeiten oder Rückstellungen verschwiegen oder unterbewertet.
- **Round-Tripping**: Zahlungen hin und zurück, um fiktive Einnahmen zu generieren.
- **Off-Balance-Sheet Transactions**: Schulden in Zweckgesellschaften ausgelagert.

### 2. Forensische Buchprüfungsmethoden
- **Journal Entry Testing**: Analyse aller manuellen Buchungen (wer hat wann gebucht?); Ausreißer außerhalb normaler Genehmigungsprozesse.
- **Analytical Procedures**: Branchenvergleich; Margin-Analyse; Wachstumsraten; Verhältnis Forderungen zu Umsatz.
- **Three-Way-Match**: Bestellung, Lieferschein, Rechnung abgleichen.
- **Bank Reconciliation**: Banksaldo vs. Buchsaldo; zeitliche Diskrepanzen (Kiting).
- **Benford's Law**: Verteilung erster Ziffern in Buchungsbeträgen.

### 3. Schlüsseldokumente
- Buchführungsunterlagen (§ 257 HGB: 10 Jahre aufzubewahren, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__257.html)).
- Kontenpläne, Journalbücher, Hauptbuch.
- E-Mail-Kommunikation zwischen CFO, Controller, Vertrieb zu Quartalsabschlüssen.
- Abschlussprüfer-Arbeitspapiere (§ 51b WPO: Herausgabepflicht, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/wpo/__51b.html)).
- Aufsichtsratsprotokolle zu Bilanzierungsfragen.

### 4. Abschlussprüfer-Koordination
- § 321 HGB: Abschlussprüfer hat Unregelmäßigkeiten im Prüfungsbericht zu beschreiben.
- Abschlussprüfer als Zeuge: kann Arbeitspapiere vorlegen (mit Einschränkungen nach § 43 WPO – Berufsverschwiegenheit).
- Austauschmöglichkeiten: bei laufender Untersuchung direkten Kontakt mit Prüfer suchen.
- Wechsel des Abschlussprüfers: strategisches Risiko (Signal an Markt und Regulatoren).

### 5. Ad-hoc-Meldepflicht
- Kapitalmarktrelevante Unregelmäßigkeiten lösen Ad-hoc-Pflicht nach Art. 17 MAR aus.
- Keine verzögerte Meldung, wenn die Information kursrelevant ist.
- Selbstbefreiung (Art. 17 Abs. 4 MAR): temporäre Verzögerung bei laufender Untersuchung möglich, wenn Offenlegung die Untersuchung gefährdet.

### 6. SEC-Meldungen (US-Listing)
- SOX Section 302/906: CEO und CFO zertifizieren Korrektheit der Finanzberichte.
- Fehlerhafter Bericht → Form 8-K und ggf. Restatement (SEC-Meldung).
- SEC Whistleblower: Mitarbeiter können Manipulation direkt der SEC melden (Prämie bis 30 %).
- DOJ/SEC-Exposure: SOX Section 807 (Strafbarkeit für Wertpapierbetrug).

### 7. Strafrechtliche und zivilrechtliche Konsequenzen
- § 331 HGB, § 400 AktG: Freiheitsstrafe bis 3 Jahre oder Geldstrafe für Vorstand/Aufsichtsrat.
- § 93 Abs. 2 AktG: Schadensersatz der Gesellschaft gegen Vorstandsmitglieder.
- D&O-Versicherung prüfen: Deckungsausschlüsse bei vorsätzlichem Handeln.
- Aktionärsklagen, Kapitalmarkthaftung nach §§ 37b, 37c WpHG.

## Red-Team-Fragen

- Wurden alle manuellen Buchungen (insb. Quartalsende, Jahresabschluss) auf Auffälligkeiten geprüft?
- Hat der Abschlussprüfer Unregelmäßigkeiten gefunden und im Prüfungsbericht dokumentiert?
- Ist die Ad-hoc-Meldepflicht ausgelöst, und wurde die Entscheidung zur Selbstbefreiung dokumentiert?
- Wurden CEO und CFO über ihre persönliche SOX-Zertifizierungshaftung informiert?
- Gibt es SEC-Whistle-Blower-Risiko (Mitarbeiter meldet direkt)?
- Ist die D&O-Versicherung informiert und deckt sie diesen Fall?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 331 HGB | Unrichtige Darstellung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__331.html) |
| § 400 AktG | Strafbarkeit Falschdarstellung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__400.html) |
| § 321 HGB | Prüfungsbericht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__321.html) |
| Art. 17 MAR | Ad-hoc-Meldepflicht | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596) |
| § 93 AktG | Haftung Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |

## Ausgabeformate

- **Forensic-Accounting-Analyse-Template** (Journal-Entry-Tests, Benford, Ratio-Analyse)
- **Unregelmäßigkeits-Klassifizierungsmatrix**
- **Ad-hoc-Meldungs-Entscheidungsbaum**
- **Abschlussprüfer-Kommunikations-Protokoll**
- **Restatement-Szenarioanalyse**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-033-cyber-incident`

**Fokus:** Reagiert auf Cyber-Incidents (Ransomware, Datenleck, APT) – DSGVO-Meldepflichten, forensische Sicherung, Behördenstrategie, Strafverfolgung.

# Cyber-Incident-Response und forensische Untersuchung

## Rechtlicher Rahmen

Cyber-Incidents lösen eine Vielzahl von Rechtspflichten aus: DSGVO Art. 33 (Meldung binnen 72 Stunden bei Datenpanne, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)), NIS2-Richtlinie (Meldepflicht für kritische Infrastrukturen und wichtige Einrichtungen, RL (EU) 2022/2555), BSI-Gesetz (§§ 8a, 8b BSIG) und ggf. sektorspezifische Pflichten (§ 25a KWG für Banken, [bafin.de](https://www.bafin.de/)). Strafbarkeit der Täter nach §§ 202a ff. StGB; Ansprüche des Unternehmens aus §§ 823, 826 BGB.

## Ziel dieses Skills

Dieser Skill strukturiert die unmittelbare Incident-Response, die forensische Beweissicherung und alle Meldepflichten bei einem Cyber-Incident.

## Arbeitsprogramm

### 1. Incident-Klassifizierung
- **Ransomware**: Verschlüsselung von Systemen; Erpressung; oft mit Datenexfiltration kombiniert.
- **APT (Advanced Persistent Threat)**: staatlich gesponserter Angreifer; langfristiger Zugriff auf Systeme.
- **Insider-Threat**: Mitarbeiter oder ehem. Mitarbeiter mit Zugriff auf Systeme.
- **Phishing/BEC**: Business E-Mail Compromise; Überweisungsbetrug.
- **Data Leak**: unbeabsichtigte oder vorsätzliche Offenlegung personenbezogener Daten.

### 2. Sofortmaßnahmen (Incident-Response)
- Netzwerktrennung kompromittierter Systeme (Containment); keine vollständige Abschaltung, wenn forensische Spuren auf flüchtigen Daten (RAM) verloren gehen würden.
- Incident-Response-Team aktivieren (IT-Security, CISO, Anwalt, Kommunikation, Management).
- BSI informieren (§ 8b Abs. 4 BSIG) bei kritischer Infrastruktur oder erheblichem Incident.
- Logs sichern: alle relevanten Event-Logs, Netzwerk-Logs, Firewall-Logs mit Hash-Wert sichern.
- Kein Löschen von Systemen vor forensischer Sicherung.

### 3. Forensische Untersuchung
- Memory-Forensik: RAM-Dump vor Systemabschaltung; flüchtige Daten gehen bei Ausschalten verloren.
- Disk-Forensik: Forensic Imaging aller betroffenen Systeme (vgl. inv-015-forensic-imaging).
- Netzwerkanalyse: Firewall-Logs, DNS-Logs, Proxy-Logs; welche IPs kommuniziert, welche Daten exfiltriert?
- Malware-Analyse: Reverse Engineering der Schadsoftware; Command-and-Control-Server identifizieren.
- Timeline-Rekonstruktion: wann hat der Angreifer erstmals Zugriff erlangt?

### 4. DSGVO-Meldepflichten (Art. 33/34)
- 72-Stunden-Frist: Meldung bei der Aufsichtsbehörde, auch wenn noch nicht alle Fakten bekannt sind; Updates möglich.
- Inhalt der Meldung: Art der Verletzung, Kategorien und Anzahl betroffener Personen, Folgen, Maßnahmen.
- Art. 34: Information der Betroffenen, wenn hohes Risiko für Rechte und Freiheiten.
- DSB einbinden (Art. 37–39 DSGVO).

### 5. Sektorspezifische Meldepflichten
- **Banken/Finanzdienstleister**: § 25a KWG, BaFin-Rundschreiben IT-Sicherheit, EZB-Meldung bei signifikanten IT-Vorfällen.
- **Kritische Infrastruktur**: NIS2-Richtlinie (RL (EU) 2022/2555, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022L2555)); Meldung innerhalb von 24 Stunden (Early Warning).
- **Energiesektor, Gesundheitssektor**: eigene Meldepflichten nach Sektorrecht.

### 6. Strafverfolgung und behördliche Zusammenarbeit
- Strafanzeige: §§ 202a, 202c, 303a, 303b StGB; ZAC (Zentrale Ansprechstelle Cybercrime der LKAs).
- BKA: bei erheblichen Angriffen auf kritische Infrastruktur.
- Europol/FBI: bei transnationalen Angreifern.
- Beweise sichern für Strafverfolgung: Chain of Custody, Hash-Werte.
- Lösegeld zahlen? Rechtliche Risiken: Sanktionsrisiko (OFAC), Geldwäscherisiko; keine Garantie der Entschlüsselung.

### 7. Remediation und Kommunikation
- Systeme bereinigen und neu aufbauen (clean-room recovery).
- Schwachstellen schließen, die den Incident ermöglicht haben.
- Mitarbeiterkommunikation: was ist passiert, was tut das Unternehmen?
- Kundenkommunikation: falls Kundendaten betroffen.
- Pressekommunikation (vgl. inv-051-press-strategy): kontrollierte Information, keine Spekulation.

## Red-Team-Fragen

- Wurden RAM-Dump und forensische Images vor der Systembereinigung gesichert?
- Ist die 72-Stunden-DSGVO-Meldepflicht eingehalten, auch wenn noch nicht alle Fakten klar sind?
- Gibt es sektorspezifische Meldepflichten (BaFin, BSI, NIS2), die separat erfüllt werden müssen?
- Wurde vor einer Lösegeldzahlung das OFAC-Sanktionsrisiko geprüft?
- Ist der Zeitpunkt des Erstzugriffs des Angreifers bekannt, und wurden alle Aktivitäten seitdem rekonstruiert?
- Wurden Strafverfolgungsbehörden (ZAC, BKA) einbezogen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 33 DSGVO | Datenpannen-Meldung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| §§ 8a, 8b BSIG | BSI-Meldepflichten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bsig_2009/) |
| §§ 202a ff. StGB | Computerstrafrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__202a.html) |
| RL (EU) 2022/2555 | NIS2-Richtlinie | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022L2555) |
| § 25a KWG | IT-Sicherheit Banken | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__25a.html) |

## Ausgabeformate

- **Incident-Response-Checkliste** (Containment, Forensik, Meldung)
- **DSGVO-Meldungsvorlage** Art. 33 (72-Stunden)
- **Forensik-Beauftragungstemplate** für Cyber-IR
- **Behördenmeldungs-Matrix** (BSI, BaFin, LKA, DSGVO-Behörde)
- **Kommunikationsplan** (intern, Kunden, Presse)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
