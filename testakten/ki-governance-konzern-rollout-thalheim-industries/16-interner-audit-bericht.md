# Interner Revisionsbericht — KI-Compliance (März/April 2026)

**Aktenzeichen:** TI-KI-2026-016
**Dokumentversion:** 1.0 (Endfassung)
**Datum:** 02. Mai 2026
**Verfasser:** Franz-Josef Brammer, Leiter Konzernrevision Thalheim Industries SE
**Verteiler:** CEO Dr. Thalheim-Lattermann; CCO Kühnhausen; CIO Dr. Wolfsbacher; CDO Petersen; KI-Komitee
**Prüfungszeitraum:** 01. März 2026 – 15. April 2026

---

## 1. Prüfungsauftrag und Methodik

Die Konzernrevision hat im Zeitraum März/April 2026 eine anlassbezogene und routinemäßige KI-Compliance-Prüfung durchgeführt. Anlassbezogener Auslöser war die Entdeckung des nicht genehmigten GenAI-Tools in der Marketingabteilung am 14.03.2026 (sog. Schatten-KI). Die Prüfung wurde auf das gesamte KI-Governance-Programm TI-KI-2026 ausgeweitet.

**Prüfungsmethoden:**
- Dokumentenanalyse (KI-Inventar, Governance-Dokumentation, Vendor-Verträge)
- Interviews mit verantwortlichen Personen (CIO, CDO, CCO, DSB, HR, Finanzierung, IT-Security)
- Technische Sichtprüfung (Systemzugriffe, Log-Analyse)
- Vergleich mit internen Richtlinien (KI-Governance-Leitlinie v2.1) und externen Anforderungen (KI-VO, DSGVO)

---

## 2. Feststellungen

### Feststellung R-001 — Schatten-KI Marketingabteilung (KRITISCH)

**Sachverhalt:** Die Marketingabteilung (Leiter: Dr. Philipp Sonntag) hat seit Juli 2025 (Beginn geschätzt auf Basis erster Log-Daten) ein nicht genehmigtes KI-Tool (Midjourney API-Integration über eigens eingerichteten Server) für Bildgenerierung und Texterstellung eingesetzt. Das Tool wurde außerhalb des zentralen CDO-verwalteten IT-Stack betrieben und war weder im KI-Inventar eingetragen noch durch den KI-Freigabeprozess genehmigt worden.

**Volumen:** Mindestens 8 Monate Betrieb; ca. 2.400 API-Anfragen (rekonstruiert aus Cloud-Kostenabrechnungen).

**Datenrisiko:** Prüfung durch DSB Dr. Eichenmüller ergab, dass in 34 von 2.400 Anfragen Nachnamen und Firmennamen von Kunden in Prompts eingegeben wurden. Diese Daten wurden an die Midjourney-Server (USA, keine adequate-level-Entscheidung für diesen Verarbeitungskontext) übermittelt. Potenzielle DSGVO-Verletzung (Art. 44 ff. DSGVO); Meldepflicht an LfDI BW wird geprüft.

**Ursachen:** (1) Fehlende technische Zugangskontrollen (API-Nutzung nicht geblockt); (2) Unzureichende Sensibilisierung der Führungskräfte (AI-Literacy-Rückstand); (3) Unklare Kommunikation der KI-Governance-Anforderungen.

**Empfehlung:** Sofortige Überprüfung und Sperrung nicht autorisierter API-Endpunkte. Arbeitsrechtliche Konsequenzen für Dr. Sonntag prüfen (nach Anhörung). Nachträgliche Datenschutzprüfung der 34 Kundendaten-Fälle. Eskalation an LfDI BW ggf. nach Art. 33 DSGVO.

---

### Feststellung R-002 — AI-Literacy-Schulungsrückstand als systemisches Risiko (HOCH)

**Sachverhalt:** Nur 38 % aller Mitarbeitenden haben Modul A abgeschlossen (Stand März 2026). In Fachbereichen mit Hochrisiko-Systemen (HR: 36 %, Finanzierung: 40 %) besonders kritisch. Der Betriebsrat hat noch keinerlei Schulung erhalten.

**Bewertung:** Das Vorkommnis mit der Schatten-KI in der Marketingabteilung ist unmittelbar auf den Schulungsrückstand zurückzuführen. Dr. Sonntag und sein Team wussten nicht um die KI-Freigabepflicht. Dies zeigt: der Schulungsrückstand ist kein administratives Problem, sondern ein systemisches Compliance-Risiko.

**Empfehlung:** Sofortprogramm AI Literacy mit Führungskräftepflicht. Monatliches Reporting an KI-Komitee. Kopplung der Freigabe neuer KI-Tools an Schulungsnachweis des Antragstellers.

---

### Feststellung R-003 — Keine vollständige Vendor-Vertragsrevision nach KI-VO (MITTEL)

**Sachverhalt:** Die Bestandsverträge mit Synaptec Analytics GmbH und CreditVision AG enthalten keine KI-VO-spezifischen Klauseln (Bias-Test-Pflichten, Meldepflichten bei Incidents, technische Dokumentations-SLA). Der OpenAI-Vertrag enthält ebenfalls keine EU-AI-Act-Klausel.

**Bewertung:** Thalheim trägt als Betreiber die Verantwortung dafür, dass die Vendor-Systeme die KI-VO-Anforderungen erfüllen. Fehlende vertragliche Absicherung erhöht das Haftungsrisiko.

**Empfehlung:** Alle Vendor-Verträge bis 30.06.2026 um KI-VO-Klauseln ergänzen (Nachtragsvereinbarung). Dabei insbesondere: Bias-Test-Pflicht, techn. Dokumentations-SLA, Incident-Meldepflicht 24h, Konformitätserklärung-Pflicht vor Inbetriebnahme neuer Modellversionen.

---

### Feststellung R-004 — Fehlende SOP für menschliche Aufsicht RecruitAI (MITTEL)

**Sachverhalt:** Es gibt keine schriftlich dokumentierte SOP (Standard Operating Procedure) für HR-Business-Partner, wann und wie sie RecruitAI-Empfehlungen überstimmen sollen. Schulungsmaterial ist vorhanden, aber kein verbindliches Protokollierungsverfahren für Override-Entscheidungen.

**Empfehlung:** SOP bis 30.04.2026 erstellen und in LMS einbinden. Jede Override-Entscheidung in SAP SuccessFactors dokumentieren.

---

### Feststellung R-005 — KI-Inventar unvollständig (NIEDRIG)

**Sachverhalt:** Das KI-Inventar enthält 23 Systeme. Im Rahmen der Bereichsbefragung im April 2026 wurden weitere 4 Systeme gemeldet, die noch nicht eingetragen waren (darunter 1 weiteres Marketing-Tool, 2 Analyse-Tools im Vertrieb, 1 KI-basierter Outlook-Assistent).

**Empfehlung:** Inventar-Kampagne wiederholen. Bis 30.06.2026 alle Meldungen verarbeiten und Inventar abschließen.

---

## 3. Bewertungsübersicht

| Feststellung | Kritikalität | Status (April 2026) | Frist |
|---|---|---|---|
| R-001 Schatten-KI Marketing | Kritisch | Abgeschaltet; Aufarbeitung läuft | 31.05.2026 |
| R-002 AI-Literacy-Rückstand | Hoch | Maßnahmenpaket verabschiedet | 31.10.2026 |
| R-003 Vendor-Vertragsrevision | Mittel | In Vorbereitung | 30.06.2026 |
| R-004 SOP menschliche Aufsicht | Mittel | In Erarbeitung | 30.04.2026 |
| R-005 KI-Inventar unvollständig | Niedrig | Kampagne geplant | 30.06.2026 |

---

## 4. Managementreaktion

CCO Kühnhausen hat den Bericht am 28.04.2026 entgegengenommen und alle Empfehlungen akzeptiert. Die Konzernrevision wird den Umsetzungsstand der Maßnahmen im Rahmen der nächsten Routineprüfung (Q3 2026) nachverfolgen.

---

*Revisionsbericht R-2026-005. Aktenzeichen: TI-KI-2026-016. Leiter Konzernrevision: Franz-Josef Brammer. 02.05.2026.*
