---
name: inv-document-cost
description: "Inv 048 Document Retention, Inv 049 Cost Recovery Employee: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 048 Document Retention, Inv 049 Cost Recovery Employee

## Arbeitsbereich

Dieser Skill bündelt **Inv 048 Document Retention, Inv 049 Cost Recovery Employee** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-048-document-retention` | Definiert Dokumentenaufbewahrungs- und -vernichtungsstrategien für Internal Investigation – HGB-Fristen, DSGVO-Löschpflichten, Legal Hold. |
| `inv-049-cost-recovery-employee` | Macht Untersuchungskosten und Schäden gegen verantwortliche Mitarbeiter und Organmitglieder geltend – § 93 AktG, § 249 BGB, Verjährung. |

## Arbeitsweg

Für **Inv 048 Document Retention, Inv 049 Cost Recovery Employee** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-048-document-retention`

**Fokus:** Definiert Dokumentenaufbewahrungs- und -vernichtungsstrategien für Internal Investigation – HGB-Fristen, DSGVO-Löschpflichten, Legal Hold.

# Dokumentenaufbewahrung und -vernichtung nach Internal Investigations

## Rechtlicher Rahmen

Dokumentenaufbewahrung unterliegt einem komplexen Spannungsfeld: Handelsrechtliche Aufbewahrungspflichten (§ 257 HGB: 10 Jahre für Buchführung, 6 Jahre für Handelsbriefe, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__257.html)) und steuerrechtliche Pflichten (§ 147 AO) stehen im Konflikt mit dem DSGVO-Löschungsgebot (Art. 17 DSGVO). Im Rahmen einer Internal Investigation wird dieser Konflikt durch den Legal Hold verschärft: Dokumente müssen trotz DSGVO-Löschpflicht aufbewahrt werden, bis die Untersuchung abgeschlossen ist.

## Ziel dieses Skills

Dieser Skill definiert für alle relevanten Dokumentenkategorien klare Aufbewahrungs- und Löschregeln, die sowohl handelsrechtliche Pflichten als auch DSGVO-Anforderungen erfüllen.

## Arbeitsprogramm

### 1. Aufbewahrungspflichten-Übersicht
| Dokumentenart | Frist | Norm |
|---|---|---|
| Buchführungsunterlagen, Jahresabschlüsse | 10 Jahre | § 257 Abs. 4 HGB |
| Handelsbriefe (inkl. E-Mail) | 6 Jahre | § 257 Abs. 4 HGB |
| Steuerunterlagen | 10 Jahre | § 147 AO |
| Lohnunterlagen | 6–10 Jahre | § 147 AO |
| Personalakten (nach Austritt) | 3–5 Jahre | § 195 BGB |
| Verträge | 10 Jahre nach Vertragsende | § 195 BGB |

### 2. Legal Hold – Vorrang vor Löschpflicht
- Art. 17 Abs. 3 lit. e DSGVO: Löschungsrecht entfällt, wenn Verarbeitung zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist.
- Automatische Löschroutinen für Legal-Hold-Dokumente deaktivieren.
- Legal-Hold-Register führen: welche Dokumente stehen unter Hold, seit wann, weshalb?
- Aufhebung des Legal Hold: nach Abschluss aller Verfahren (Untersuchung, Behördenverfahren, Gerichtsverfahren).

### 3. Untersuchungsspezifische Aufbewahrung
- Interviewprotokolle: solange verfahrensrelevant; danach DSGVO-konforme Löschung.
- Forensic Images: bis zur Beendigung aller Verfahren; danach sicheres Löschen (NIST SP 800-88).
- Untersuchungsbericht (Vollbericht): strategische Entscheidung; kann dauerhaft archiviert werden, wenn er keine personenbezogenen Daten enthält; Pseudonymisierung möglich.
- Korrespondenz mit Behörden: 10 Jahre nach Abschluss des Verfahrens.

### 4. DSGVO-konforme Löschung
- Art. 17 DSGVO: Recht auf Löschung muss nach Wegfall des Legal Hold beachtet werden.
- Technisches Löschen: sichere Überschreibung oder Zerstörung von Datenträgern (NIST SP 800-88).
- Löschprotokoll: Dokumentation, was wann wie gelöscht wurde.
- Backups: Löschung muss sich auch auf Backup-Systeme erstrecken (Art. 5 Abs. 1 lit. c DSGVO).

### 5. Aufbewahrung für US-Discovery
- Dokumente unter US-Litigation-Hold: bis zum Abschluss des US-Verfahrens.
- Spoliation-Risiko: vorzeitige Vernichtung kann Sanktionen auslösen (FRCP 37(e)).
- Koordination zwischen deutschem Handelsrecht (Aufbewahrungspflicht) und DSGVO-Löschpflicht und US-Litigation-Hold.

### 6. Aufbewahrung in der Praxis
- Dokumentenmanagement-System: automatische Fristen und Erinnerungen.
- Records-Management-Policy: welche Dokumente werden wie lange aufbewahrt?
- Jährliche Aufbewahrungs-Reviews: abgelaufene Dokumente identifizieren und vernichten.
- Ausnahmen dokumentieren: warum wird ein Dokument über die Standardfrist hinaus aufbewahrt?

### 7. Vernichtungsstrategie nach Untersuchungsabschluss
- Nach Aufhebung des Legal Hold: Überprüfung jedes Dokuments auf verbleibende Aufbewahrungspflichten.
- Priorisierung: personenbezogene Daten zuerst löschen (DSGVO-Sensibilität).
- Keine selektive Vernichtung: alle Kopien (lokal, Cloud, Backup) müssen erfasst sein.
- Zeuge der Vernichtung: Protokollierung der sicheren Löschung durch IT-Abteilung.

## Red-Team-Fragen

- Wurden alle automatischen Löschroutinen für Legal-Hold-Dokumente deaktiviert?
- Gibt es US-Litigation-Hold-Pflichten, die mit dem deutschen DSGVO-Löschungsgebot kollidieren?
- Ist das Löschprotokoll nach Aufhebung des Legal Holds vollständig und deckt alle Speicherorte ab (inkl. Backups)?
- Wurden Interviewprotokolle und forensische Images nach Verfahrensabschluss datenschutzgerecht gelöscht?
- Ist die handelsrechtliche Aufbewahrungspflicht für alle relevanten Untersuchungsdokumente geprüft?
- Gibt es verbleibende personenbezogene Daten in den Untersuchungsunterlagen, die unter DSGVO gelöscht werden müssen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 257 HGB | Aufbewahrungspflichten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__257.html) |
| § 147 AO | Steuerrechtliche Aufbewahrung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__147.html) |
| Art. 17 DSGVO | Recht auf Löschung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 5 DSGVO | Datensparsamkeit | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| FRCP Rule 37(e) | Spoliation Sanctions | US Federal Courts |

## Ausgabeformate

- **Aufbewahrungsfristen-Matrix** (Dokumententyp × Norm × Frist)
- **Legal-Hold-Register-Vorlage**
- **Löschprotokoll-Vorlage**
- **Records-Management-Policy-Template**
- **Aufbewahrungskonzept** für Untersuchungsunterlagen

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-049-cost-recovery-employee`

**Fokus:** Macht Untersuchungskosten und Schäden gegen verantwortliche Mitarbeiter und Organmitglieder geltend – § 93 AktG, § 249 BGB, Verjährung.

# Kostenerstattung und Schadensersatz gegen Mitarbeiter

## Rechtlicher Rahmen

Das Unternehmen kann die Kosten einer Internal Investigation und den durch den Verstoß verursachten Schaden von den verantwortlichen Mitarbeitern und Organmitgliedern zurückfordern. Rechtsgrundlagen: § 93 Abs. 2 AktG (Schadensersatz Vorstand, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html)), § 43 Abs. 2 GmbHG (Schadensersatz Geschäftsführer), § 249 BGB (allgemeiner Schadensersatz, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__249.html)), § 823 BGB (Haftung wegen Verletzung absoluter Rechte). Verjährung: 5 Jahre für Organmitglieder (§ 93 Abs. 6 AktG), 3 Jahre für andere (§ 195 BGB).

## Ziel dieses Skills

Dieser Skill strukturiert Schadensersatzansprüche gegen Mitarbeiter und Organmitglieder und stellt sicher, dass Forderungen rechtzeitig geltend gemacht werden.

## Arbeitsprogramm

### 1. Schadenskomponenten
- **Direkter Schaden**: durch den Verstoß unmittelbar verursachter wirtschaftlicher Schaden (z. B. überzahlter Kickback-Betrag, durch Betrug entzogene Mittel).
- **Folgeschäden**: Untersuchungskosten (Anwalt, Forensik, Wirtschaftsprüfer), Bußgelder (soweit auf individuellem Verhalten basierend), Reputationsschäden.
- **Entgangener Gewinn**: Verträge, die wegen der Untersuchung nicht abgeschlossen werden konnten.
- Hinweis: Bußgelder nach OWiG können nicht auf Mitarbeiter abgewälzt werden, wenn sie den Charakter einer Strafe haben (BGH Linie).

### 2. Ansprüche gegen Organmitglieder
- § 93 Abs. 2 AktG: Vorstandsmitglied haftet, wenn es die ihm obliegende Sorgfalt verletzt hat; Beweislastumkehr: Vorstandsmitglied muss beweisen, dass es pflichtgemäß gehandelt hat.
- § 43 Abs. 2 GmbHG: Geschäftsführer haftet bei schuldhafter Pflichtverletzung.
- Verjährung: § 93 Abs. 6 AktG – 5 Jahre ab dem Zeitpunkt des schädigenden Ereignisses; wichtig: Hemmung (§ 204 BGB) durch Verhandlungen oder Klageerhebung.
- BGH II ZR 234/09 (Siemens/Neubürger): Vorstandsmitglied, das Compliance-Pflichtverletzungen nicht verhindert, haftet ([openjur.de](https://openjur.de/o/577696.html)).

### 3. Ansprüche gegen Mitarbeiter
- § 249 BGB: Schadensersatz bei schuldhafter Pflichtverletzung aus dem Arbeitsverhältnis.
- BAG-Rechtsprechung zur privilegierten Arbeitnehmerhaftung: bei leichter Fahrlässigkeit keine Haftung; mittlere Fahrlässigkeit anteilig; grobe Fahrlässigkeit und Vorsatz volle Haftung.
- Verrechnung mit offenen Vergütungsansprüchen: Aufrechnung nach § 387 BGB bei fälligen Forderungen.
- Strafbarkeit: wenn Straftat begangen, kann Schadensersatzklage parallel zur Strafanzeige geführt werden.

### 4. D&O-Versicherung
- D&O-Versicherung deckt Schadensersatzansprüche gegen Organmitglieder (außer bei Vorsatz).
- Versicherung muss unverzüglich benachrichtigt werden.
- Self-Retention: Eigenanteil des Versicherten (oft 10 % des Schadens, mindestens 1 Jahresfixvergütung nach VVG-Änderungen).
- Claims-Made-Basis: Schaden und Meldung müssen in der Versicherungsperiode liegen.

### 5. Schadensberechnung
- Direktschaden: dokumentiert durch forensische Buchprüfung.
- Untersuchungskosten: Anwaltsrechnung, Forensiker-Rechnung, Reisekosten – vollständig dokumentieren.
- Bußgelder: Abgrenzung, welcher Anteil auf individuellem Fehlverhalten des Organmitglieds beruht.
- Gutachten: ggf. externer Wirtschaftsschadens-Sachverständiger für komplexe Schadensberechnungen.

### 6. Sicherung der Forderung
- Arrest (§§ 916 ff. ZPO): wenn Vermögensverschleuberung oder Flucht droht.
- Pfändung: von Gehaltsansprüchen oder Bankvermögen des Mitarbeiters.
- Aufrechnung: gegen noch offene Gehalts- oder Abfindungsansprüche.
- Abtretung: D&O-Versicherungsanspruch an das Unternehmen abtreten lassen.

### 7. Verjährungs-Management
- Hemmung: durch schriftliche Aufforderung zur Verhandlung, Mahnung oder Klageerhebung.
- § 93 Abs. 6 AktG: 5 Jahre (Organmitglieder); beginnt mit Entstehung des Anspruchs.
- § 195 BGB: 3 Jahre ab Kenntnis (Mitarbeiter).
- Kein Verzicht: Hauptversammlung kann nach § 93 Abs. 4 AktG erst 3 Jahre nach Entstehung auf Ansprüche verzichten.

## Red-Team-Fragen

- Sind alle Schadenskomponenten vollständig berechnet, einschließlich der Untersuchungskosten?
- Läuft die Verjährung, und wurden Hemmungsmaßnahmen rechtzeitig eingeleitet?
- Hat die D&O-Versicherung eine ordnungsgemäße Schadensmeldung erhalten?
- Gibt es Gegenforderungen des Mitarbeiters (Gehaltsrückstände, Abfindung), die die Aufrechnung gefährden könnten?
- Besteht Flucht- oder Vermögensverschleuderungsrisiko, das einen Arrest erfordert?
- Kann das Unternehmen gegenüber der Hauptversammlung belegen, dass es Schadensersatzansprüche nicht verfrüht aufgegeben hat?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Haftung Vorstand, Verjährung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 249 BGB | Schadensersatz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__249.html) |
| § 195 BGB | Regelmäßige Verjährung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__195.html) |
| §§ 916 ff. ZPO | Arrest | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__916.html) |
| BGH II ZR 234/09 | Siemens/Neubürger | [openjur.de](https://openjur.de/o/577696.html) |

## Ausgabeformate

- **Schadensberechnungs-Vorlage** (direkter Schaden + Untersuchungskosten)
- **D&O-Schadensmeldungs-Checkliste**
- **Schadensersatzklage-Vorbereitung** (Musterstruktur)
- **Arrest-Antrag-Vorlage** (§§ 916 ff. ZPO)
- **Verjährungs-Tracking-Tabelle**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
