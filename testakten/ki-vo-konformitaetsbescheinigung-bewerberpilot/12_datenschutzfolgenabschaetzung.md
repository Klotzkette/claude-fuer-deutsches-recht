# Datenschutz-Folgenabschaetzung (DSFA) BewerberPilot TalentRank 2.4

**Verantwortliche:** BewerberPilot Score GmbH, Koeln (Anbieterin / für Pilotbetrieb auch Auftragsverarbeiterin, soweit relevant)
**Betreiberin (Pilot):** Elbtal Klinikservice gGmbH, Dresden (datenschutzrechtlich Verantwortliche)
**Verfasserin:** Dr. Caspar Lintorf (Compliance), in Abstimmung mit dem benannten Datenschutzbeauftragten der BewerberPilot Score GmbH (Frau Dr. Selma Pesch)
**Stand:** Entwurf v0.6 vom 14.05.2026
**Prüfdatum nächste Aktualisierung:** 14.07.2026 (nach Pilotbeginn)
**Rechtsgrundlage DSFA:** Art. 35 DSGVO; ergänzt durch KI-VO Berührungspunkte (Art. 27 KI-VO).

## 1. Beschreibung der Verarbeitung

### 1.1 Datenkategorien

| Kategorie | Quellen | Zweck | Aufbewahrung |
|---|---|---|---|
| Lebenslauf, Anschreiben, Zeugnisse, Zertifikate | Upload Bewerbung | Merkmalsextraktion und Priorisierung | 24 Monate nach Bewerbungsabschluss |
| Kontaktdaten | Bewerbungsformular, Lebenslauf | Recruiterkommunikation | 6 Monate, danach Löschung wenn keine weitere Verarbeitungsgrundlage |
| Berufserfahrung, Ausbildung, Sprachkenntnisse | Lebenslauf | Score und Erklärung | 24 Monate |
| Bewerbungsstatus | Recruiter-Eingabe | Workflow | 6 Monate |
| Manuelle Recruiterkommentare | Recruiter-Eingabe | Dokumentation Entscheidung | 24 Monate |
| Systemscore und Erklaermerkmale | KI-Inferenz | Priorisierung und Audit | 24 Monate |
| Logging-Daten | System | Nachvollziehbarkeit | 18 - 24 Monate (vgl. 06_human_oversight_logging_art_12_14.md) |

### 1.2 Verarbeitungsschritte

1. Upload Bewerbungsunterlagen (HTTPS, EU-Hosting MedData Hosting GmbH Nürnberg).
2. Dokumentklassifikation und OCR (lokales Modell).
3. Extraktion strukturierter Merkmale (lokales Modell).
4. Abgleich mit Stellenprofil (Score zwischen 0 und 100, Muss-Kriterium-Flag).
5. Zusammenfassung und Interviewfragen durch GPAI-Komponente LexiCore Coordinator v3.1 (Auftragsverarbeiter LexiCore Systems Inc. über EU-Endpoint Dublin; Datenübermittlung in Drittländer ausgeschlossen durch Vertragsklausel und technische Konfiguration).
6. Anzeige im Recruiter-Dashboard.
7. Menschliche Entscheidung (kein automatisierter Ablehnungsweg).
8. Protokollierung der Entscheidung.

### 1.3 Datenfluss in Drittländer

Nach derzeitiger Konfiguration **keine** Datenübermittlung in Drittländer. Der GPAI-Endpoint von LexiCore ist auf den EU-Region-Endpoint Dublin festgelegt; die Auftragsverarbeitung erfolgt nach Standardvertragsklauseln 2021/914 Modul 2. **Prüfbedarf:** Vertragsklausel "Keine Datenübermittlung in Drittländer" muss von LexiCore schriftlich bestätigt werden (vgl. Lückenliste Nr. 4).

## 2. Risiken für die Rechte und Freiheiten Betroffener

| Risiko-ID | Risiko | Eintrittswahrscheinlichkeit | Schadensschwere | Bewertung |
|---|---|---|---|---|
| DSFA-R-01 | Diskriminierende Benachteiligung wegen unbalancierter Trainingsdaten | Mittel | Hoch | Hochrisiko |
| DSFA-R-02 | Verarbeitung besonderer Kategorien (Art. 9 DSGVO) ohne Rechtsgrundlage | Niedrig/Mittel | Hoch | Hochrisiko |
| DSFA-R-03 | Verlust der Vertraulichkeit (Cyberangriff) | Niedrig | Hoch | Hochrisiko |
| DSFA-R-04 | Fehlerhafte automatisierte Verarbeitung mit faktischer Ablehnungswirkung (Art. 22 DSGVO Berührung) | Mittel | Hoch | Hochrisiko |
| DSFA-R-05 | Mangelnde Betroffenenrechte (Auskunft, Löschung, Widerspruch) | Mittel | Mittel | Erhebliches Risiko |
| DSFA-R-06 | Unzureichende Information über den KI-Einsatz (Art. 13/14 DSGVO + Art. 13/26 KI-VO) | Mittel | Mittel | Erhebliches Risiko |
| DSFA-R-07 | Falsche Aufbewahrungsdauern | Niedrig | Mittel | Erhebliches Risiko |
| DSFA-R-08 | Verkettung mit anderen HR-Systemen (Profilbildung) | Mittel | Mittel | Erhebliches Risiko |
| DSFA-R-09 | Schluechtere oder ausschliessende Wirkung bei Nicht-Muttersprachlern und nicht-linearen Karriereverläufen | Mittel-Hoch | Hoch | Hochrisiko |

## 3. Massnahmen zur Risikominderung

### 3.1 Technisch

- EU-Hosting bei MedData Hosting GmbH (Auftragsverarbeiter, AVV vorhanden).
- Verschlüsselung in transit (TLS 1.3) und at rest (AES-256).
- MFA für Recruiter und Administratoren.
- Pen-Test im Q2/2026 (durchgeführt 18.04.2026, Bericht im QMS).
- Maskierung von sensiblen Angaben in Bewerbungsunterlagen (Geburtsdatum, Foto, Religion).

### 3.2 Organisatorisch

- Bias-Auditbericht mit Überprüfung der Trainings- und Validierungsdaten (Lückenliste Nr. 2 und 3).
- Recruiter-Schulung zu KI-Vorschlägen mit Verständnisfragen (Lückenliste Nr. 5).
- Verbotsklauseln im Pilotvertrag (keine automatisierte Ablehnung).
- Beschwerdemanagement (Art. 19 KI-VO und Art. 12-22 DSGVO).

### 3.3 Rechtsgrundlagen Pruefung

- Verarbeitung beruht beim Betreiber (Elbtal Klinikservice gGmbH) auf:
  - Art. 6 Abs. 1 lit. b) DSGVO (Anbahnung des Arbeitsvertrags) und/oder
  - § 26 Abs. 1 BDSG (Bewerbungsverhältnis als beschaeftigungsrechtliche Beziehung)
  - Art. 9 Abs. 2 lit. b) DSGVO bei zwingender Erforderlichkeit besonderer Kategorien (z.B. Pflegezeugnisse mit Gesundheitsangaben).

- Eine besondere Einwilligung nach Art. 9 Abs. 2 lit. a) DSGVO wird nicht eingeholt; sensible Angaben werden grundsätzlich maskiert.

## 4. Konsultation des Datenschutzbeauftragten

Dr. Selma Pesch (DSB der BewerberPilot Score GmbH) hat am 06.05.2026 Stellung genommen:

> "Das Vorhaben ist datenschutzrechtlich begleitbar. Voraussetzung ist:
> (1) die abschliessende Bias-Pruefung mit Massnahmen zu DSFA-R-09,
> (2) die LexiCore-Nachweise zur EU-Region-Verarbeitung,
> (3) die Information der Bewerbenden über den KI-Einsatz mit klarer Sprache,
> (4) eine wirksame Widerspruchsmöglichkeit bei Score-Verwendung.
> Eine vorherige Konsultation der Aufsichtsbehörde nach Art. 36 DSGVO ist Stand heute nicht erforderlich, weil die in Ziffer 3 genannten Massnahmen das Restrisiko unter die Schwelle 'hohes Risiko ohne Risikominderung' bringen sollen."

## 5. Information der Bewerbenden (Art. 13 DSGVO + Art. 26 KI-VO)

Bewerbende erhalten beim Upload folgende Information (Auszug):

> "Ihre Bewerbungsunterlagen werden mit Unterstützung eines KI-Systems (BewerberPilot TalentRank) gesichtet. Das System hilft Recruiterinnen und Recruitern, die Reihenfolge der Bearbeitung festzulegen und Qualifikationen sichtbar zu machen. Die Entscheidung über Einladung oder Ablehnung trifft eine menschliche Person. Sie haben das Recht, gegen die Verwendung des KI-Systems Widerspruch einzulegen; in diesem Fall wird Ihre Bewerbung ohne KI-Unterstützung bearbeitet."

Diese Information ist in 09_eu_konformitaetserklaerung_anhang_v_entwurf.md mit dem Hinweis zur menschlichen Entscheidung konsistent.

## 6. Verbleibendes Risiko

Selbst nach Umsetzung aller Massnahmen besteht ein **Restrisiko** bei DSFA-R-01 und DSFA-R-09 (diskriminierende Wirkung trotz Bias-Tests). Dieses Risiko ist nicht vollständig auszuschliessen. Die Anbieterin und die Betreiberin verpflichten sich:

- Quartalsweise Bias-Berichte (Lückenliste Nr. 2 und 3).
- Post-Market-Monitoring mit Indikatoren für Auswahlquoten je Stellenkategorie und Bewerberprofil.
- Korrektur bei messbaren Diskriminierungseffekten.

## 7. Entscheidung

Die DSFA kommt zu dem Ergebnis, dass der Pilotbetrieb **nach Schliessung der Lückenliste** datenschutzrechtlich tragbar ist. Eine vorherige Konsultation der Aufsichtsbehörde ist nicht erforderlich. Die DSFA wird quartalsweise aktualisiert und nach Pilotabschluss erneut bewertet.
