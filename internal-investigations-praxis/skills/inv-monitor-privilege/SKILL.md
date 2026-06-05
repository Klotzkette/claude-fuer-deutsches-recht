---
name: inv-monitor-privilege
description: "Inv 046 Monitor Reporting, Inv 047 Privilege Log: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 046 Monitor Reporting, Inv 047 Privilege Log

## Arbeitsbereich

Dieser Skill bündelt **Inv 046 Monitor Reporting, Inv 047 Privilege Log** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-046-monitor-reporting` | Strukturiert das Reporting an einen externen Compliance-Monitor nach DPA/NPA oder Behördenanordnung – Anforderungen, Konfliktmanagement, Exit-Strategie. |
| `inv-047-privilege-log` | Erstellt und verwaltet das Privilege-Log für privilegierte Untersuchungsdokumente – FRCP Rule 26(b)(5), deutsche Schutzstandards, Waiver-Risiken. |

## Arbeitsweg

Für **Inv 046 Monitor Reporting, Inv 047 Privilege Log** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-046-monitor-reporting`

**Fokus:** Strukturiert das Reporting an einen externen Compliance-Monitor nach DPA/NPA oder Behördenanordnung – Anforderungen, Konfliktmanagement, Exit-Strategie.

# Externer Compliance-Monitor und Monitor-Reporting

## Rechtlicher Rahmen

Externe Compliance-Monitore werden im Rahmen von Deferred Prosecution Agreements (DPA), Non-Prosecution Agreements (NPA) oder behördlichen Anordnungen (BaFin, DOJ) eingesetzt. Im deutschen Recht kann die BaFin nach §§ 45, 46 KWG ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__46.html)) und § 4 WpHG externe Prüfer oder Sonderbeauftragte einsetzen. Im US-Recht werden Monitore nach DOJ-Policy aus unabhängigen Experten bestellt. Der Monitor hat weitgehende Zugangs- und Berichtsrechte, aber das Unternehmen kann und sollte seinen Umgang mit dem Monitor strategisch gestalten.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass das Monitor-Reporting vollständig, strategisch konsistent und nicht selbstschädigend ist.

## Arbeitsprogramm

### 1. Monitor-Mandat verstehen
- DPA/NPA-Text: was ist der genaue Untersuchungsauftrag des Monitors?
- Zugriffsrechte: auf welche Dokumente, Systeme, Mitarbeiter hat der Monitor Zugang?
- Berichtspflicht des Monitors: an wen, in welcher Häufigkeit, in welchem Format?
- Vertraulichkeit: sind Monitor-Berichte privilegiert oder können sie an Strafverfolgungsbehörden übergeben werden?

### 2. Interne Organisation für den Monitor
- Dedicated Monitor-Team: Ansprechpartner für den Monitor, kein Ad-hoc-Handling.
- Document Production: strukturiertes Verfahren für Dokumentenanfragen des Monitors.
- Information Flow: keine direkte Kontaktaufnahme von Mitarbeitern mit dem Monitor ohne Koordination durch das Monitor-Team.
- Anwalt: alle Kommunikation mit dem Monitor wird durch den Unternehmensanwalt koordiniert.

### 3. Erster Monitor-Bericht (Inception Report)
- Monitor bewertet den aktuellen Compliance-Zustand des Unternehmens.
- Eigeninteresse: Unternehmen sollte in den ersten Wochen aktiv kooperieren und eigene Mängel proaktiv kommunizieren (bevor der Monitor sie findet).
- Priorisierung: welche Bereiche des Unternehmens sind für den Monitor am kritischsten?
- Remediation-Plan vorlegen: vollständiger Plan für alle identifizierten Mängel (vgl. inv-045-remediation-plan).

### 4. Laufendes Reporting
- Fortschrittsberichte: Umsetzungsstand der Remediation-Maßnahmen dokumentieren.
- Kompetente Gesprächspartner: für jede Fachfrage den richtigen Ansprechpartner bereitstellen.
- Keine Überraschungen: Monitor nicht mit neuen Problemen konfrontieren, die das Unternehmen intern bereits kennt.
- Incident-Reporting: neue Compliance-Vorfälle während der Monitor-Periode proaktiv melden.

### 5. Umgang mit Meinungsverschiedenheiten
- Factual Disputes: wenn Monitor Sachverhalt falsch verstanden hat, sachlich und zeitnah korrigieren.
- Rechtliche Bewertung: wenn Monitor eine andere rechtliche Einschätzung hat, konstruktiv Gegenargumente vortragen.
- Eskalation: wenn Meinungsverschiedenheit nicht lösbar, Einschaltung der zuständigen Behörde (DOJ/BaFin) als Mediator.
- Dokumentation: alle Disputes und deren Lösung schriftlich festhalten.

### 6. Exit-Strategie
- DPA/NPA-Ablaufdatum: was muss bis dahin erreicht sein?
- Monitor-Abschlussbericht: Grundlage für DOJ/Behörde-Entscheidung über Abschluss des Verfahrens.
- Attestierung: Monitor bescheinigt, dass Compliance-Programm angemessen und effektiv ist.
- Post-Monitor: Wie wird das Compliance-Programm ohne Monitor aufrechterhalten?

### 7. BaFin-Sonderbeauftragter (deutsches Recht)
- § 45c KWG: BaFin kann Sonderbeauftragten einsetzen; weitgehende Eingriffsrechte.
- Kosten: Unternehmen trägt die Kosten des Sonderbeauftragten.
- Zeitraum: unbegrenzt, solange BaFin es für erforderlich hält.
- Strategie: proaktive Kooperation, Fortschrittsberichte, klare Milestones für Exit.

## Red-Team-Fragen

- Versteht das Monitor-Team das genaue Mandat des Monitors, einschließlich Zugriffsrechten und Berichtspflichten?
- Gibt es neue Compliance-Vorfälle, die dem Monitor noch nicht proaktiv gemeldet wurden?
- Wurden alle Dokumentenanfragen des Monitors zeitnah und vollständig beantwortet?
- Ist das Unternehmen auf den Abschlussbericht des Monitors vorbereitet, oder gibt es Risiken bei der Attestierung?
- Gibt es ungelöste faktische oder rechtliche Disputes mit dem Monitor, die eskaliert werden müssen?
- Ist das Compliance-Programm nach Monitor-Ende nachhaltig genug, um ohne externe Aufsicht zu bestehen?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| §§ 45, 46 KWG | BaFin-Anordnungsbefugnisse | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__46.html) |
| § 45c KWG | Sonderbeauftragter | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/kredwg/__45c.html) |
| § 130 OWiG | Aufsichtspflichtverletzung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/owig/__130.html) |
| BGH II ZR 234/09 | Siemens/Neubürger CMS | [openjur.de](https://openjur.de/o/577696.html) |

## Ausgabeformate

- **Monitor-Koordinations-Handbuch** (internes Verfahren)
- **Dokumentenanfrage-Tracking-Vorlage**
- **Fortschrittsbericht-Template** für Monitor
- **Disputes-Log** (Meinungsverschiedenheiten und Lösungen)
- **Exit-Checkliste** (Attestierungsvoraussetzungen)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-047-privilege-log`

**Fokus:** Erstellt und verwaltet das Privilege-Log für privilegierte Untersuchungsdokumente – FRCP Rule 26(b)(5), deutsche Schutzstandards, Waiver-Risiken.

# Privilege-Log in Internal Investigations

## Rechtlicher Rahmen

Das Privilege-Log ist das zentrale Instrument zur Dokumentation aller zurückgehaltenen privilegierten Dokumente. Im US-amerikanischen Recht ist es zwingend nach FRCP Rule 26(b)(5) für alle als „privileged" zurückgehaltenen Dokumente zu erstellen. Im deutschen Recht gibt es keine vergleichbare Formvorschrift, aber der Beschlagnahmeschutz nach § 97 StPO ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html)) setzt voraus, dass die Unterlagen als privilegiert identifizierbar sind. Das Privilege-Log schützt vor dem Vorwurf, Dokumente willkürlich zurückgehalten zu haben.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass das Privilege-Log vollständig, korrekt und US-FRCP-konform ist und den Privilegeschutz im Verfahren sichert.

## Arbeitsprogramm

### 1. FRCP Rule 26(b)(5) – Anforderungen
- Jedes zurückgehaltene Dokument muss im Log enthalten sein.
- Pflichtangaben: Datum, Autor (inkl. Funktion), Empfänger, CC/BCC, Dokumententyp, kurze Beschreibung (ohne Offenbarung des privilegierten Inhalts), Basis des Privilege (Attorney-Client, Work Product).
- Keine „Blanket" Privilege-Behauptungen ohne spezifische Begründung.
- Privilege-Log ist selbst kein privilegiertes Dokument (Existenz des Logs muss offengelegt werden).

### 2. Attorney-Client Privilege – Voraussetzungen
- Kommunikation zwischen Mandant und Anwalt (in anwaltlicher Eigenschaft).
- Zweck: Rechtsberatung (nicht rein geschäftliche Kommunikation).
- Vertraulichkeit: Kommunikation war und blieb vertraulich (kein Teilen mit Dritten außerhalb des Privilege-Kreises).
- Upjohn-Erweiterung (US): auch Kommunikation mit Mitarbeitern, wenn im Rahmen der Rechtsberatung des Unternehmens.

### 3. Work-Product Doctrine
- Dokumente des Anwalts, die in Erwartung eines Rechtsstreits erstellt wurden.
- Stärkerer Schutz für „opinion work product" (rechtliche Bewertungen, mentale Eindrücke).
- Schwächerer Schutz für „fact work product" (Tatsachenzusammenfassungen); kann bei substantial need überwindbar sein.
- Nicht auf Mandantenbeziehung angewiesen (auch Anwaltsdokumente ohne direkte Mandantenkommunikation).

### 4. Deutsches Recht – § 97 StPO
- Schutz: schriftlicher Verkehr zwischen Beschuldigtem und Verteidiger.
- Anwaltliche Arbeitsunterlagen: grundsätzlich schutzwürdig, wenn in mandatlicher Eigenschaft erstellt.
- Grenzen: Unternehmen als potenziell Beschuldigter wird anders behandelt als natürliche Person als Beschuldigter (BGH, Beschl. v. 5.4.2017 – StB 3/17, [bgh.de](https://www.bgh.de/)).
- Kennzeichnung: Dokumente sollten als „Anwaltliche Arbeitsunterlagen – Vertraulich" gekennzeichnet sein.

### 5. Waiver-Risiken
- Voluntary Disclosure: freiwillige Weitergabe an Dritte (inkl. Behörden) hebt Privilege auf.
- Selective Waiver: in den USA nicht allgemein anerkannt; Weitergabe an DOJ ohne entsprechende Vereinbarung kann zum Subject-Matter-Waiver führen.
- Crime-Fraud Exception: Privilege entfällt, wenn Dokument zur Unterstützung einer Straftat diente.
- Inadvertent Disclosure: versehentliche Weitergabe; FRCP Rule 26(b)(5)(B) ermöglicht Claw-Back.

### 6. Privilege-Log-Erstellung in der Praxis
- Einsatz von eDiscovery-Plattformen (Relativity, Reveal) für automatische Privilege-Identifikation.
- Überprüfung durch Anwalt: jedes als privilegiert getaggte Dokument muss von Anwalt bestätigt werden.
- Stichwortlisten für automatische Erkennung: Anwaltsnamen, Kanzleinamen, „privileged", „attorney-client", „attorney work product".
- Regelmäßige Aktualisierung: Privilege-Log wächst mit dem Untersuchungsumfang.

### 7. Reaktion auf Privilege-Anfechtungen
- Gegenseite ficht Privilege an: Klausel zu In-Camera-Überprüfung durch Gericht (§ 97 Abs. 2 StPO analog; FRCP Rule 26(b)(5)).
- Begründung des Privilege für jedes angegriffene Dokument vorbereiten.
- Keine Teiloffenbarung ohne Strategie (Subject-Matter-Waiver-Risiko).

## Red-Team-Fragen

- Enthält das Privilege-Log alle zurückgehaltenen Dokumente, oder fehlen bestimmte Kategorien?
- Sind alle Privilege-Ansprüche mit konkreten Begründungen versehen – keine Blanket-Behauptungen?
- Gibt es Dokumente, die an Behörden weitergegeben wurden, für die kein Selective-Waiver-Schutz vereinbart wurde?
- Wurden versehentlich offenbarte privilegierte Dokumente sofort per Claw-Back zurückgefordert?
- Ist das Privilege-Log im FRCP Rule 26(b)(5)-konformen Format erstellt?
- Haben Nicht-Anwälte (Wirtschaftsprüfer, IT-Forensiker) Dokumente erstellt, die fälschlicherweise als privilegiert getaggt sind?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 97 StPO | Beschlagnahmeschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__97.html) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |
| FRCP Rule 26(b)(5) | US Privilege Log Requirements | US Federal Courts |

## Ausgabeformate

- **Privilege-Log-Template** (FRCP Rule 26(b)(5)-konform)
- **Privilege-Prüfprotokoll** für Dokument-Reviewer
- **Claw-Back-Vorlage** bei inadvertent disclosure
- **Privilege-Anfechtungs-Verteidigung** (In-Camera-Memo)
- **Attorney-Client-Privilege-Prüfliste** (Voraussetzungen im Einzelfall)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
