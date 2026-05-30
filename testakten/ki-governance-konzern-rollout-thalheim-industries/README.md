# Akte: KI-Governance Konzern-Rollout — Thalheim Industries SE

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Diese Arbeitsakte gibt es in zwei Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (Markdown-Aktenstücke, Tabellen, E-Mails, Fotos, PDFs, DOCX, XLSX) im Originalordnerlayout für eigene Auswertungen.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 704 KB) | PDF | [`gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf`](gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-ki-governance-konzern-rollout-thalheim-industries.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-governance-konzern-rollout-thalheim-industries.zip) |

Die ZIP-URL ist stabil und zeigt immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

**Arbeitsakte.** Alle Personen, Anschriften, Aktenzeichen und Unternehmen sind anonymisiert und fiktiv. Die Akte gehört fachlich zum Plugin `ki-governance`.

---

## Kurzbild

- **Mandant:** Thalheim Industries SE, August-Bebel-Ring 14, 68163 Mannheim; DAX-Mittelstand, ca. 12.000 Mitarbeiter, Anlagenbau und Energietechnik; Umsatz rd. 3,2 Mrd. EUR (2025).
- **Anlass:** KI-Verordnung (EU) 2024/1689 (KI-VO) tritt mit gestaffelten Fristen in Kraft; Thalheim muss bis 02.08.2026 alle Hochrisiko-KI-Systeme konformitätsgeprüft und registriert haben (Art. 113 KI-VO). Intern läuft das Programm unter dem Kürzel **TI-KI-2026** (Aktenzeichen TI-KI-2026-007 bis TI-KI-2026-015).
- **Interne Stichtage:** Konformitätsprüfung Recruiting-Tool 02.08.2026; AI-Literacy-Schulung (Art. 4 KI-VO) flächendeckend Q4 2025; DPIA für Recruiting-Tool einzureichen bis 30.06.2026.
- **Externe Verfahren:** BaFin GZ BJ 24-K 7102-2026/0012 (Kreditscoring-Modul); LfDI BW AZ 1-1085.51/2026/045 (DPIA Recruiting-Tool).
- **Beteiligte intern:** CEO Dr. Reinhard Thalheim-Lattermann; CIO Dr. Sigrid Wolfsbacher; CDO Marcus Petersen; CCO/Compliance Annegret Kühnhausen; Datenschutzbeauftragte Dr. Carla Eichenmüller; KI-Komitee-Vorsitz Dr. Falk Roosendaal; Betriebsratsvorsitzender Norbert Schäpers.
- **Externe Beteiligte:** OpenAI Ireland Ltd. (Vendor GenAI); Synaptec Analytics GmbH (Vendor Recruiting-Screening); CreditVision AG (Vendor Kreditscoring); Wirtschaftsprüfungsgesellschaft Hagedorn & Partner (Auditor); Kanzlei Borchmann Compliance (externe Rechtsberatung KI-VO).

---

## Fünf KI-Systeme im Scope

| System | Einsatzbereich | Klassifikation | Vendor | Frist |
|---|---|---|---|---|
| **RecruitAI** | HR / Recruiting-Screening | Hochrisiko (Anh. III Nr. 4a KI-VO) | Synaptec Analytics GmbH | 02.08.2026 |
| **CreditVision Score** | Kundenfinanzierung / Kreditscoring | Hochrisiko (Anh. III Nr. 5b KI-VO) | CreditVision AG | 02.08.2026 |
| **PredictMaint** | Predictive Maintenance Anlagen | Begrenztes Risiko | Thalheim intern | 02.08.2027 |
| **CodeAssist** | Software-Entwicklung (GenAI) | Begrenztes Risiko | OpenAI Ireland Ltd. | 02.08.2027 |
| **ServiceBot** | Kundenservice Chatbot | Transparenzpflichten (Art. 50 KI-VO) | Thalheim intern | 02.02.2025 ✓ |

---

## Konfliktstränge

### Strang 1 — RecruitAI: Fehlende Bias-Tests, Audit-Feststellungen
Auditor Hagedorn & Partner stellt bei der Konformitätsprüfung nach Art. 9 ff. KI-VO fest, dass Synaptec für RecruitAI keine dokumentierten Bias-Tests nach Art. 9 Abs. 7 KI-VO vorgelegt hat. Die Frist 02.08.2026 rückt; ohne bestandene Konformitätsbewertung darf das System nicht weiter betrieben werden (Art. 16 lit. f KI-VO). CIO Wolfsbacher eskaliert an CEO. Gleichzeitig fordert die LfDI BW (AZ 1-1085.51/2026/045) die Einreichung einer vollständigen DPIA nach Art. 35 DSGVO bis 30.06.2026.

### Strang 2 — CreditVision Score: BaFin-Anfrage
Die BaFin eröffnet eine Konsultation zum Kreditscoring-Modul (GZ BJ 24-K 7102-2026/0012) und fragt, ob Art. 22 DSGVO (automatisierte Einzelentscheidung) eingehalten wird, und ob eine interne Konformitätsbewertung nach Art. 43 Abs. 2 KI-VO durchgeführt wurde. Compliance-Chefin Kühnhausen muss binnen 4 Wochen Stellung nehmen. CreditVision AG liefert Unterlagen mit Verzug.

### Strang 3 — Betriebsrat blockiert Rollout
Betriebsratsvorsitzender Norbert Schäpers macht geltend, dass Einführung und Erweiterung beider Hochrisiko-Systeme (RecruitAI, CreditVision Score) nach § 87 Abs. 1 Nr. 6 BetrVG mitbestimmungspflichtig seien. Der BR verweigert die Zustimmung zum Echtbetrieb, bis eine Betriebsvereinbarung KI abgeschlossen ist. Verhandlungen stocken seit Januar 2026.

### Strang 4 — Vendor OpenAI: Unvollständige Konformitätsdokumentation
Für CodeAssist (GPT-4-basiert) hat OpenAI Ireland Ltd. keine vollständige technische Dokumentation nach Art. 11 KI-VO übermittelt. CDO Petersen moniert das fehlende Konformitätsdokument. OpenAI verweist auf seine eigene EU-AI-Act-Compliance-Seite, die jedoch keine produktspezifischen Nutzerdaten enthält.

### Strang 5 — AI Literacy (Art. 4 KI-VO): Schulungsrückstand
Die flächendeckende Schulungspflicht nach Art. 4 KI-VO ist bis Q4 2025 vorgesehen; Stand März 2026 haben erst 38 % der Mitarbeiter die Pflichtschulung absolviert. In Risikobereichen (HR, Finanzierung) besteht besonders großer Rückstand. Konzernrevision prangert dies als systemisches Compliance-Risiko an.

### Strang 6 — LfDI BW fordert DPIA für RecruitAI
Das Landesbeauftragte für Datenschutz und Informationsfreiheit Baden-Württemberg (LfDI BW, AZ 1-1085.51/2026/045) stuft den Einsatz von RecruitAI als voraussichtlich hochrisikoreich nach Art. 35 Abs. 3 lit. a DSGVO ein und ordnet die Durchführung und Vorlage einer vollständigen DPIA an. Datenschutzbeauftragte Dr. Eichenmüller koordiniert die Erstellung, die durch den laufenden Bias-Test-Mangel (Strang 1) erschwert wird.

### Strang 7 — Konzernrevision: Schatten-KI in der Marketingabteilung
Interne Revision (Leiter: Franz-Josef Brammer) entdeckt, dass die Marketingabteilung seit mind. 8 Monaten ein nicht genehmigtes GenAI-Tool (Midjourney + eigene API-Anbindung) ohne Sicherheitsfreigabe, ohne Datenschutzprüfung und ohne Registrierung im KI-Inventar betreibt. Der Marketingleiter Dr. Philipp Sonntag streitet eine wissentliche Regelverletzung ab. Vorstand erwägt arbeitsrechtliche Konsequenzen.

---

## Was diese Akte demonstriert

| Skill | Aktenstück | Demonstration |
|---|---|---|
| KI-Governance-Leitlinie und Rahmen | 01, 03, 22 | Governance-Framework, Vorstandsbeschluss, Projektabschluss |
| Risikoklassifikation nach KI-VO | 02, 14 | Anh. III-Prüfung, Risikoeinstufung, Konformitätspfade |
| Pflichtenmatrix Art. 9 ff. KI-VO | 04, 13 | Hochrisiko-Pflichten, Fachbereichs-Zuordnung, Fristen |
| AI Literacy (Art. 4 KI-VO) | 05, 10 | Curriculum, Schulungsmatrix, Rückstand, Eskalation |
| Vendor Due Diligence | 06 | OpenAI-Zertifizierung, Tech-Dok., Vertragsprüfung |
| DPIA-Integration | 07, 15 | Art. 35 DSGVO, DPIA-Bericht, LfDI-Korrespondenz |
| Incident Response KI | 08 | Playbook, Eskalationspfad, Schatten-KI |
| Verbotene Praktiken (Art. 5 KI-VO) | 09 | Rote Liste, Prüfschema, Negativbeispiele |
| KI-Komitee-Governance | 10 | Protokoll, Beschlüsse, Eskalationen Q1 2026 |
| Betriebsratsrecht (§ 87 BetrVG) | 11, 15 | Mitbestimmung, BV-Entwurf, Verhandlungsstand |
| Aufsichtsratsberichterstattung | 12 | AktG § 93, Governance-Bericht, Haftungsrisiken |
| Konformitätsprüfung Hochrisiko | 13, 14 | Art. 43 KI-VO, Prüfberichte HR/Kredit |
| Behördenkorrespondenz | 15 | LfDI BW, BaFin, Stellungnahme |
| Interner Audit | 16 | Revisionsbericht, Feststellungen, Schatten-KI |
| Vorstandseskalation | 17 | Entscheidungsvorlage, Haftung, Fristen |
| Externe Kommunikation | 18, 19 | Pressemitteilung, Q&A Kunden |
| Roadmap und Budget | 20, 21 | Konformitäts-Roadmap 2027, Governance-Budget |
| Projektabschluss | 22 | Phase-1-Bericht, Lessons Learned |

---

## Aktenstücke

| Nr. | Datei | Inhalt |
|---|---|---|
| 01 | [`01-governance-leitlinie-entwurf.md`](01-governance-leitlinie-entwurf.md) | Entwurf KI-Governance-Leitlinie Thalheim Industries SE |
| 02 | [`02-risikoklassifikations-matrix.md`](02-risikoklassifikations-matrix.md) | Risikoklassifikation der 5 KI-Systeme nach Anh. III KI-VO |
| 03 | [`03-vorstandsbeschluss.md`](03-vorstandsbeschluss.md) | Vorstandsbeschluss KI-Governance-Programm TI-KI-2026 |
| 04 | [`04-pflichtenmatrix-fachbereiche.md`](04-pflichtenmatrix-fachbereiche.md) | Pflichtenmatrix Art. 9 ff. KI-VO je Fachbereich |
| 05 | [`05-ai-literacy-curriculum.md`](05-ai-literacy-curriculum.md) | AI-Literacy-Curriculum und Schulungsplan (Art. 4 KI-VO) |
| 06 | [`06-vendor-due-diligence-openai.md`](06-vendor-due-diligence-openai.md) | Vendor Due Diligence OpenAI Ireland Ltd. / CodeAssist |
| 07 | [`07-dpia-recruiting-tool.md`](07-dpia-recruiting-tool.md) | DPIA RecruitAI (Art. 35 DSGVO) — Entwurf |
| 08 | [`08-incident-response-playbook.md`](08-incident-response-playbook.md) | KI-Incident-Response-Playbook Thalheim Industries |
| 09 | [`09-rote-listen-verbotene-praktiken.md`](09-rote-listen-verbotene-praktiken.md) | Rote Liste — Verbotene KI-Praktiken nach Art. 5 KI-VO |
| 10 | [`10-protokoll-ki-komitee-quartal1.md`](10-protokoll-ki-komitee-quartal1.md) | Protokoll KI-Komitee Q1 2026 (14.03.2026) |
| 11 | [`11-betriebsratsvereinbarung-entwurf.md`](11-betriebsratsvereinbarung-entwurf.md) | Entwurf Betriebsvereinbarung KI-Systeme |
| 12 | [`12-aufsichtsrat-bericht.md`](12-aufsichtsrat-bericht.md) | Aufsichtsratsbericht KI-Governance Q1 2026 |
| 13 | [`13-konformitaetspruefung-hr-system.md`](13-konformitaetspruefung-hr-system.md) | Konformitätsprüfung RecruitAI — Auditbericht |
| 14 | [`14-konformitaetspruefung-kreditscoring.md`](14-konformitaetspruefung-kreditscoring.md) | Konformitätsprüfung CreditVision Score |
| 15 | [`15-stellungnahme-datenschutzbehoerde.md`](15-stellungnahme-datenschutzbehoerde.md) | Stellungnahme gegenüber LfDI BW (DPIA RecruitAI) |
| 16 | [`16-interner-audit-bericht.md`](16-interner-audit-bericht.md) | Interner Revisionsbericht KI-Compliance (März 2026) |
| 17 | [`17-eskalation-vorstandsvorsitz.md`](17-eskalation-vorstandsvorsitz.md) | Eskalationsvorlage an CEO Dr. Thalheim-Lattermann |
| 18 | [`18-pressemitteilung-entwurf.md`](18-pressemitteilung-entwurf.md) | Pressemitteilungsentwurf: Thalheim startet KI-Governance |
| 19 | [`19-q-and-a-kundenanfragen.md`](19-q-and-a-kundenanfragen.md) | Q&A zu Kundenanfragen zum KI-Einsatz |
| 20 | [`20-roadmap-konformitaet-2027.md`](20-roadmap-konformitaet-2027.md) | Konformitäts-Roadmap 2025–2027 |
| 21 | [`21-budgetplan-governance-funktion.md`](21-budgetplan-governance-funktion.md) | Budgetplan KI-Governance-Funktion 2026/2027 |
| 22 | [`22-abschlussbericht-projektphase-1.md`](22-abschlussbericht-projektphase-1.md) | Abschlussbericht Projektphase 1 (Bestandsaufnahme) |

---

## Anhänge

### DOCX

| Datei | Inhalt |
|---|---|
| [`vorstandsvorlage-ki-governance-rahmen.docx`](vorstandsvorlage-ki-governance-rahmen.docx) | Vorstandsvorlage: KI-Governance-Rahmen Thalheim Industries SE |
| [`richtlinie-ki-einsatz-thalheim-v3-2.docx`](richtlinie-ki-einsatz-thalheim-v3-2.docx) | Interne Richtlinie KI-Einsatz v3.2 (Entwurf) |
| [`betriebsvereinbarung-ki-entwurf.docx`](betriebsvereinbarung-ki-entwurf.docx) | Betriebsvereinbarungs-Entwurf KI-Systeme (Verhandlungsstand) |

### XLSX

| Datei | Inhalt |
|---|---|
| [`risikoklassifikation-ki-systeme.xlsx`](risikoklassifikation-ki-systeme.xlsx) | Risikoklassifikationstabelle 25 KI-Systeme nach KI-VO |
| [`pflichtenmatrix-art-9-ff-kivo.xlsx`](pflichtenmatrix-art-9-ff-kivo.xlsx) | Pflichtenmatrix Art. 9 ff. KI-VO je KI-System |

### E-Mails (.eml)

| Datei | Inhalt |
|---|---|
| [`email-cio-an-vorstand-projektstart.eml`](email-cio-an-vorstand-projektstart.eml) | CIO Dr. Wolfsbacher an Vorstand: Projektstart TI-KI-2026 |
| [`email-betriebsrat-mitbestimmung.eml`](email-betriebsrat-mitbestimmung.eml) | BR-Vorsitzender Schäpers: Mitbestimmung nach § 87 BetrVG |
| [`email-bafin-anfrage-kreditscoring.eml`](email-bafin-anfrage-kreditscoring.eml) | BaFin GZ BJ 24-K 7102-2026/0012: Anfrage Kreditscoring |
| [`email-konzernrevision-feststellungen.eml`](email-konzernrevision-feststellungen.eml) | Konzernrevision: Feststellungen Schatten-KI Marketing |
| [`email-openai-vendor-zertifizierung.eml`](email-openai-vendor-zertifizierung.eml) | OpenAI Ireland: Antwort zu Konformitätsdokumentation |

### PDFs

| Datei | Inhalt |
|---|---|
| [`eu-leitlinien-zusammenfassung.pdf`](eu-leitlinien-zusammenfassung.pdf) | Zusammenfassung EU-Leitlinien zur KI-Verordnung |
| [`gutachten-externer-kanzlei-ki-vo-anwendung.pdf`](gutachten-externer-kanzlei-ki-vo-anwendung.pdf) | Gutachten Kanzlei Borchmann: Anwendung KI-VO auf Thalheim-Systeme |

### Bilder (JPG)

| Datei | Inhalt |
|---|---|
| [`whiteboard-risikomatrix.jpg`](whiteboard-risikomatrix.jpg) | Whiteboard-Foto: Risikomatrix Workshop (interne Aufnahme) |
| [`org-chart-governance-funktion.jpg`](org-chart-governance-funktion.jpg) | Org-Chart KI-Governance-Funktion Thalheim Industries |
| [`screenshot-dashboard-konformitaet.jpg`](screenshot-dashboard-konformitaet.jpg) | Screenshot: Compliance-Dashboard KI-Systeme (Stand März 2026) |

---

## Verfahrensstand

**Stichtag dieser Akte: März 2026**
**Programmstart: Oktober 2025**

| Verfahrensstrang | Status |
|---|---|
| Vorstandsbeschluss TI-KI-2026 | Gefasst 15.10.2025 |
| KI-Inventarisierung | Abgeschlossen (Phase 1); 23 Systeme erfasst |
| Risikoklassifikation | 2 Hochrisiko, 3 begrenztes Risiko, 1 minimales Risiko bestätigt |
| RecruitAI — Konformitätsprüfung | Audit läuft; Bias-Test-Mangel festgestellt; Frist 02.08.2026 |
| RecruitAI — DPIA | In Bearbeitung; LfDI BW fordert Vorlage bis 30.06.2026 |
| CreditVision Score — BaFin | Offene BaFin-Anfrage; Antwortfrist 15.05.2026 |
| Betriebsvereinbarung KI | Verhandlungen stocken seit Jan. 2026; Einigung ausstehend |
| OpenAI / CodeAssist Doku | Nachforderung läuft; OpenAI-Frist 30.04.2026 |
| AI Literacy Schulung | 38 % abgeschlossen (Stand März 2026); Ziel: 100 % bis 31.10.2026 |
| Schatten-KI Marketing | Identifiziert; Marketingleiter angehört; arbeitsrechtl. Prüfung läuft |

Bearbeitung: **Dr. Falk Roosendaal**, KI-Komitee-Vorsitz, Thalheim Industries SE
Externe Beratung: **Kanzlei Borchmann Compliance**, Frankfurt am Main
Aktenzeichen intern: **TI-KI-2026-007 bis TI-KI-2026-015**
