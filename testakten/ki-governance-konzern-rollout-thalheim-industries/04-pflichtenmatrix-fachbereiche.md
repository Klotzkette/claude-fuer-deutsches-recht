# Pflichtenmatrix — Betreiberpflichten nach Art. 9 ff. KI-VO je Fachbereich

**Aktenzeichen:** TI-KI-2026-009
**Dokumentversion:** 1.2
**Erstellungsdatum:** 20. Januar 2026
**Verfasser:** Annegret Kühnhausen (CCO); Dr. Falk Roosendaal
**Stand:** März 2026

---

## 1. Einleitung

Diese Pflichtenmatrix weist die Betreiberpflichten (Deployer-Pflichten) nach Art. 9 ff. KI-VO sowie Art. 26 KI-VO für die Hochrisiko-KI-Systeme der Thalheim Industries SE den verantwortlichen Fachbereichen zu. Die Matrix dient als Arbeitsgrundlage für die Konformitätsherstellung bis 02.08.2026.

**Rechtsgrundlagen (Auszug):**
- Art. 9 KI-VO — Risikomanagementsystem: https://dejure.org/gesetze/KIVO/9.html
- Art. 26 KI-VO — Pflichten von Betreibern: https://dejure.org/gesetze/KIVO/26.html
- Art. 35 DSGVO — Datenschutz-Folgenabschätzung: https://dejure.org/gesetze/DSGVO/35.html

**Fokus:** RecruitAI (Hochrisiko, Anh. III Nr. 4a) und CreditVision Score (Hochrisiko, Anh. III Nr. 5b). Für PredictMaint, CodeAssist und ServiceBot gelten vereinfachte Anforderungen (vgl. Abschnitt 5).

---

## 2. Pflichtenkatalog Hochrisiko-Systeme

### 2.1 Pflichtensteckbrief RecruitAI

**System:** RecruitAI — Recruiting-Screening-Tool
**Vendor:** Synaptec Analytics GmbH
**Betreiber (Deployer):** Thalheim Industries SE, Fachbereich HR
**Interne Systemverantwortliche:** Barbara Trenkmann (Leiterin HR-Systeme)

| Art. KI-VO | Pflicht | Verantwortlich | Frist | Status (März 2026) |
|---|---|---|---|---|
| Art. 9 | Risikomanagementsystem dokumentieren und aufrechterhalten | HR / Compliance | 02.06.2026 | In Bearbeitung |
| Art. 9 Abs. 7 | Bias-Tests durchführen (Diskriminierung, Fairness) | HR / IT / Audit | 02.06.2026 | **Offen — Mangel festgestellt** |
| Art. 10 | Daten-Governance prüfen (Trainings- u. Testdaten) | CDO / HR | 30.04.2026 | Teilweise erledigt |
| Art. 11 | Technische Dokumentation vollständig? (Vendor-Dokument) | CIO / Vendor | 30.04.2026 | Synaptec-Unterlagen angefordert |
| Art. 12 | Protokollierungspflicht aktiviert | IT / CIO | 31.03.2026 | Umgesetzt |
| Art. 13 | Gebrauchsanweisung vorhanden und verständlich? | HR | 30.04.2026 | Vorhanden (DE-Version Synaptec) |
| Art. 14 | Menschliche Aufsicht implementiert (technisch + organisatorisch) | HR / IT | 30.06.2026 | Konzept in Erarbeitung |
| Art. 14 Abs. 4 | HR-Entscheider kann System abschalten / überstimmen | HR | 30.06.2026 | Technisch möglich, SOP fehlt |
| Art. 15 | Genauigkeit, Robustheit und Cybersicherheit testen | IT-Security / CIO | 30.06.2026 | Pentest ausstehend |
| Art. 26 Abs. 4 | Betreiber informiert Behörden bei Vorfällen (Art. 73 KI-VO) | CCO | Laufend | Prozess definiert |
| Art. 26 Abs. 7 | Betreiber meldet Konformitätsmängel an Marktüberwachung | CCO | Laufend | Keine Meldepflicht aktuell |
| Art. 35 DSGVO | DPIA durchgeführt und vorliegend | DSB Dr. Eichenmüller | 30.06.2026 | In Erarbeitung |
| Art. 22 DSGVO | Automatisierte Entscheidung: Recht auf Erklärung umgesetzt | HR / DSB | 30.06.2026 | Kandidatenmitteilung angepasst |
| § 87 BetrVG | Mitbestimmung: Betriebsvereinbarung abgeschlossen? | CCO / Betriebsrat | Vor Rollout | **Offen — BR blockiert** |

---

### 2.2 Pflichtensteckbrief CreditVision Score

**System:** CreditVision Score — Kreditscoring-Modul
**Vendor:** CreditVision AG
**Betreiber (Deployer):** Thalheim Industries SE, Fachbereich Finanzierung / Vertrieb
**Interne Systemverantwortliche:** Rolf Haselmann (Leiter Kundenfinanzierung)

| Art. KI-VO | Pflicht | Verantwortlich | Frist | Status (März 2026) |
|---|---|---|---|---|
| Art. 9 | Risikomanagementsystem | Finanzierung / Compliance | 02.06.2026 | Entwurf CreditVision erhalten |
| Art. 9 Abs. 7 | Bias-Tests Kreditvergabe | Finanzierung / CDO | 02.06.2026 | CreditVision-Auskunft ausstehend |
| Art. 10 | Daten-Governance: Kunden-Trainingsdaten geprüft? | CDO | 30.04.2026 | Nein — in Prüfung |
| Art. 11 | Technische Dokumentation (Vendor) | Finanzierung / CIO | 30.04.2026 | Unterlagen CreditVision unvollständig |
| Art. 12 | Protokollierung aktiviert | IT | 31.03.2026 | Umgesetzt |
| Art. 13 | Gebrauchsanweisung | Finanzierung | 30.04.2026 | Vorhanden |
| Art. 14 | Menschliche Aufsicht: Kreditentscheider hat Letztentscheid | Finanzierung | 30.06.2026 | Ja, prozessual verankert |
| Art. 22 DSGVO | Automatisierte Einzelentscheidung: Widerspruchsrecht informiert | Finanzierung / DSB | Sofort | Datenschutzhinweis aktualisiert |
| Art. 43 Abs. 2 | Interne Konformitätsbewertung (durch Auditor begleitet) | CCO / Hagedorn | 31.07.2026 | Audit geplant Mai 2026 |
| BaFin GZ BJ 24-K | Stellungnahme an BaFin | CCO / Borchmann | 15.05.2026 | In Vorbereitung |
| § 87 BetrVG | Mitbestimmung | CCO / Betriebsrat | Vor Rollout | **Offen — BR blockiert** |

---

## 3. Fachbereichsverantwortlichkeiten

| Fachbereich | KI-System(e) | Ansprechpartner | Kernpflicht bis 02.08.2026 |
|---|---|---|---|
| HR / Personal | RecruitAI | Barbara Trenkmann | Art. 14 Aufsicht; Art. 9 Bias-Tests |
| Kundenfinanzierung | CreditVision Score | Rolf Haselmann | Art. 14 Aufsicht; Art. 22 DSGVO |
| IT / Digital | PredictMaint, CodeAssist, ServiceBot | Marcus Petersen (CDO) | Transparenzpflichten Art. 50 |
| Compliance | Alle | Annegret Kühnhausen | Koordination, Behördenkontakt |
| Datenschutz | RecruitAI (DPIA) | Dr. Carla Eichenmüller | Art. 35 DSGVO bis 30.06.2026 |
| Revision | Alle | Franz-Josef Brammer | Interne Kontrolle, Schatten-KI |

---

## 4. Eskalationsmatrix

| Risiko | Auslöser | Eskalationspfad | Frist |
|---|---|---|---|
| Bias-Test-Mangel RecruitAI | Feststellung Auditor Hagedorn | CCO → CIO → CEO | Sofort (eskaliert am 28.02.2026) |
| BaFin-Anfrage CreditVision | Eingang 10.03.2026 | CCO → CFO → CEO, extern Borchmann | 15.05.2026 |
| BR-Blockade Rollout | BR-Schreiben 05.01.2026 | CCO → CEO → Einigung oder LAG | Dringend |
| OpenAI-Doku fehlt | CDO-Meldung 15.02.2026 | CDO → CCO → Vendor-Eskalation | 30.04.2026 |
| DPIA nicht fristgerecht | LfDI-Aufforderung 02.03.2026 | DSB → CCO → CEO | 30.06.2026 |

---

## 5. Pflichten begrenztes Risiko (ServiceBot, PredictMaint, CodeAssist)

Für Systeme mit begrenztem Risiko gelten folgende Mindestanforderungen:

| Anforderung | Grundlage | Status |
|---|---|---|
| Eintrag KI-Inventar | Interne Leitlinie | Erledigt |
| Transparenz-Hinweis (ServiceBot) | Art. 50 Abs. 1 KI-VO | Umgesetzt seit 01.02.2025 |
| Kennzeichnung KI-Inhalte (CodeAssist) | Art. 50 Abs. 2 KI-VO | Prüfung läuft |
| Datenschutzprüfung | DSB-Empfehlung | Erledigt |
| Jährliche Überprüfung | Interne Leitlinie | Geplant Q4 2026 |

---

*Aktenzeichen: TI-KI-2026-009. Verfasser: A. Kühnhausen, Dr. F. Roosendaal. Stand: März 2026.*
