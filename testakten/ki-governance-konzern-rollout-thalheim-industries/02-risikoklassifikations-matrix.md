# Risikoklassifikationsmatrix KI-Systeme — Thalheim Industries SE

**Aktenzeichen:** TI-KI-2026-008
**Dokumentversion:** 1.4
**Erstellungsdatum:** 18. Dezember 2025
**Verfasser:** Dr. Falk Roosendaal; Marcus Petersen (CDO); Annegret Kühnhausen (CCO)
**Freigegeben durch:** KI-Komitee, 10. Januar 2026

---

## 1. Zweck

Dieses Dokument enthält die vollständige Risikoklassifikation aller im KI-Inventar der Thalheim Industries SE erfassten KI-Systeme gemäß der Verordnung (EU) 2024/1689 über künstliche Intelligenz (KI-VO). Die Klassifikation folgt dem vierstufigen Risikoschema der KI-VO (Art. 5, Art. 6 i.V.m. Anhang III, Art. 50, Minimales Risiko).

Rechtsgrundlagen:
- Art. 6 i.V.m. Anhang III KI-VO (Hochrisiko-Klassifikation): https://dejure.org/gesetze/KIVO/6.html
- Art. 5 KI-VO (Verbotene Praktiken): https://dejure.org/gesetze/KIVO/5.html
- Art. 50 KI-VO (Transparenzpflichten): https://dejure.org/gesetze/KIVO/50.html

---

## 2. Klassifikationsschema

Die Einordnung erfolgt nach einem dreistufigen Prüfschema:

**Stufe 1 — Verboten (Art. 5 KI-VO):** Fällt das System unter eine der verbotenen Praktiken? → Sofortiger Stopp, keine weitere Prüfung.

**Stufe 2 — Hochrisiko (Art. 6 i.V.m. Anh. III KI-VO):**
- Ist das System ein Sicherheitsbauteil eines Produkts nach Anhang I? → Hochrisiko.
- Fällt es unter eine der acht Kategorien des Anhangs III? → Hochrisiko, sofern es bei natürlichen Personen individuelle Entscheidungen beeinflusst oder eigenständig trifft.

**Stufe 3 — Transparenzpflichten (Art. 50 KI-VO):**
- Chatbots / Konversationssysteme → Offenlegungspflicht.
- Deep-Fake-Generatoren / synthetische Inhalte → Kennzeichnungspflicht.

Alle nicht in Stufe 1–3 fallenden Systeme gelten als Systeme mit minimalem Risiko.

---

## 3. Klassifikationsergebnisse: Fünf Kernsysteme

### 3.1 RecruitAI (Recruiting-Screening)

| Merkmal | Inhalt |
|---|---|
| Vendor | Synaptec Analytics GmbH, München |
| Einsatzbereich | HR / Personalauswahl |
| Funktion | Automatisiertes Screening von Bewerbungsunterlagen, Ranking-Score |
| Prüfung Art. 5 | Keine verbotene Praktik (kein Social Scoring, keine unterschwellige Beeinflussung) |
| Prüfung Art. 6 / Anh. III | Anh. III Nr. 4a: „KI-Systeme zur Personalauswahl, zur Priorisierung von Kandidaten" → **Hochrisiko** |
| Einstufung | **Hochrisiko** |
| Rechtsgrundlage | Art. 6 Abs. 2, Anhang III Nr. 4 lit. a KI-VO |
| Konformitätsfrist | 02. August 2026 |
| Konformitätsbewertung | Intern nach Art. 43 Abs. 2 KI-VO; Auditor: Hagedorn & Partner |
| DPIA erforderlich | Ja — Art. 35 DSGVO; Aufforderung LfDI BW AZ 1-1085.51/2026/045 |
| Verantwortlicher | Dr. Sigrid Wolfsbacher (CIO) |
| Status (März 2026) | Audit läuft; Feststellung fehlender Bias-Tests |

**Begründung:** RecruitAI trifft oder beeinflusst maßgeblich Entscheidungen über die Aufnahme oder Ablehnung von Bewerbern. Anhang III Nr. 4 lit. a KI-VO erfasst explizit KI-gestützte Systeme zur „Zulassung zu Beschäftigung" und zur „Priorisierung von Bewerbern". Die Hochrisiko-Einstufung ist eindeutig. Eine DPIA ist nach Art. 35 Abs. 3 lit. a DSGVO (systematische Bewertung persönlicher Aspekte) erforderlich. Art. 22 DSGVO (automatisierte Einzelentscheidungen) ist im Lichte von Art. 26 KI-VO zu lesen.

---

### 3.2 CreditVision Score (Kreditscoring-Modul)

| Merkmal | Inhalt |
|---|---|
| Vendor | CreditVision AG, Frankfurt am Main |
| Einsatzbereich | Kundenfinanzierung / Kreditentscheidung |
| Funktion | Scoring-Modell zur Bonitätsbewertung von Privat- und Gewerbekunden |
| Prüfung Art. 5 | Keine verbotene Praktik |
| Prüfung Art. 6 / Anh. III | Anh. III Nr. 5b: „KI-Systeme zur Bewertung der Kreditwürdigkeit natürlicher Personen" → **Hochrisiko** |
| Einstufung | **Hochrisiko** |
| Rechtsgrundlage | Art. 6 Abs. 2, Anhang III Nr. 5 lit. b KI-VO |
| Konformitätsfrist | 02. August 2026 |
| Konformitätsbewertung | Intern nach Art. 43 Abs. 2 KI-VO; Auditor: Hagedorn & Partner |
| DPIA erforderlich | Prüfung läuft (hohe Wahrscheinlichkeit) |
| Verantwortlicher | Marcus Petersen (CDO) |
| Status (März 2026) | Offene BaFin-Anfrage GZ BJ 24-K 7102-2026/0012; Unterlagen CreditVision AG ausstehend |

**Begründung:** Das Kreditscoring-Modul wird zur Bewertung der Kreditwürdigkeit natürlicher Personen eingesetzt und beeinflusst damit Entscheidungen mit erheblichen Rechts- oder vergleichbar erheblichen Folgen für die Betroffenen. Art. 22 DSGVO (https://dejure.org/gesetze/DSGVO/22.html) und Art. 6 i.V.m. Anh. III Nr. 5b KI-VO gelten kumulativ. Die BaFin prüft im Rahmen ihrer Aufsicht (GZ BJ 24-K 7102-2026/0012) die Einhaltung von Art. 22 DSGVO und die Konformitätsbewertung nach Art. 43 KI-VO.

---

### 3.3 PredictMaint (Predictive Maintenance)

| Merkmal | Inhalt |
|---|---|
| Vendor | Intern entwickelt (Thalheim Digital Lab) |
| Einsatzbereich | Produktionsanlagen / Wartungsplanung |
| Funktion | Anomalieerkennung, Verschleißprognose auf Basis von Sensordaten |
| Prüfung Art. 5 | Keine verbotene Praktik |
| Prüfung Art. 6 / Anh. III | Kein Anhang-III-Tatbestand; kein Sicherheitsbauteil i.S.v. Anhang I |
| Einstufung | **Begrenztes Risiko** |
| Transparenzpflichten | Keine nach Art. 50 KI-VO (kein Chatbot, keine synthetischen Inhalte) |
| Anmerkung | Hohe wirtschaftliche Relevanz, aber kein personenbezogener Entscheidungseinfluss |
| Verantwortlicher | Dr. Sigrid Wolfsbacher (CIO) |
| Konformitätsfrist | 02. August 2027 (freiwillige interne Überprüfung) |

**Begründung:** PredictMaint verarbeitet ausschließlich Maschinendaten und trifft keine Entscheidungen über natürliche Personen. Ein Anhang-III-Tatbestand liegt nicht vor. Das System fällt damit nicht unter die Hochrisiko-Kategorie. Empfehlung: Freiwillige Dokumentation im Rahmen des KI-Inventars und Überprüfung bis August 2027.

---

### 3.4 CodeAssist (GenAI-Coding-Assistent)

| Merkmal | Inhalt |
|---|---|
| Vendor | OpenAI Ireland Ltd., Dublin (GPT-4-basiert) |
| Einsatzbereich | Software-Entwicklung intern |
| Funktion | KI-gestützte Code-Generierung und Code-Review |
| Prüfung Art. 5 | Keine verbotene Praktik |
| Prüfung Art. 6 / Anh. III | Kein Anhang-III-Tatbestand |
| Einstufung | **Begrenztes Risiko** (Allzweck-KI-Modell nach Art. 51 ff. KI-VO) |
| Transparenzpflichten | Art. 50 Abs. 2 KI-VO: Kennzeichnung KI-generierter Inhalte (Code-Kommentare) |
| Vendor-Pflichten | OpenAI als Anbieter unterliegt Art. 53 ff. KI-VO (GPAI-Modell-Pflichten) |
| Verantwortlicher | Marcus Petersen (CDO) |
| Status (März 2026) | Konformitätsdokumentation OpenAI unvollständig; Nachforderung läuft |

**Begründung:** CodeAssist basiert auf einem Allzweck-KI-Modell (GPAI) im Sinne von Art. 3 Nr. 63 KI-VO. Als Betreiber (Deployer) ist Thalheim nach Art. 26 KI-VO verantwortlich für die zweckgerechte Nutzung. OpenAI unterliegt als Anbieter (Provider) des Basismodells den Pflichten nach Art. 53 KI-VO. Thalheim muss sicherstellen, dass die Nutzung den Nutzungsbedingungen von OpenAI entspricht und keine personenbezogenen Daten ohne Rechtsgrundlage verarbeitet werden.

---

### 3.5 ServiceBot (Kundenservice-Chatbot)

| Merkmal | Inhalt |
|---|---|
| Vendor | Intern entwickelt (Thalheim Digital Lab) |
| Einsatzbereich | Kundenservice / First-Level-Support |
| Funktion | Automatisierte Beantwortung von Kundenanfragen |
| Prüfung Art. 5 | Keine verbotene Praktik |
| Prüfung Art. 6 / Anh. III | Kein Anhang-III-Tatbestand (kein Entscheidungseinfluss auf Betroffene) |
| Einstufung | **Transparenzpflichten (Art. 50 KI-VO)** |
| Transparenzpflichten | Art. 50 Abs. 1 KI-VO: Kunden müssen informiert werden, dass sie mit einem KI-System interagieren |
| Umsetzungsstand | Hinweis implementiert seit 01.02.2025; Dokumentation in TI-KI-2026-007 |
| Verantwortlicher | Marcus Petersen (CDO) |

**Begründung:** ServiceBot ist ein konversationelles KI-System im Sinne von Art. 50 Abs. 1 KI-VO. Die Pflicht zur Offenlegung gegenüber natürlichen Personen gilt unabhängig von der Risikoklasse. Die Umsetzung erfolgte fristgerecht (Art. 113 Abs. 3 KI-VO: Anwendung von Art. 50 ab 02.02.2025). Eine vollständige Überprüfung der Umsetzung findet im Rahmen des Q2-2026-Audits statt.

---

## 4. Weitere klassifizierte Systeme (Auszug)

Zusätzlich zu den fünf Kernsystemen wurden im Rahmen der Inventarisierung (Phase 1) folgende Systeme klassifiziert:

| System | Einsatzbereich | Risikoklasse | Bemerkung |
|---|---|---|---|
| MarketingAI (Midjourney-basiert) | Marketing | Begrenztes Risiko / **ungenehmigt** | Schatten-KI; identifiziert März 2026 |
| AutoTranslate | Übersetzung intern | Minimales Risiko | Keine DPIA, keine Freigabepflicht |
| FinanceReport-AI | Controlling | Minimales Risiko | Keine Entscheidungsautomation |
| EnergyForecast | Energiemanagement | Minimales Risiko | Keine Personenbezogenheit |
| QualityVision | Qualitätskontrolle | Begrenztes Risiko | Optisches System, keine Personenerkennung |

---

## 5. Anwendungsfristen (Art. 113 KI-VO)

| Datum | Regelung |
|---|---|
| 02.02.2025 | Art. 5 (Verbote), Art. 50 (Transparenz) anwendbar |
| 02.08.2025 | Governance-Pflichten (Kapitel I, II), Art. 4 (AI Literacy) anwendbar |
| 02.08.2026 | Hochrisiko-Pflichten (Art. 6, 9–17, 43) anwendbar für neue Systeme; bestehende Hochrisiko-Systeme müssen nachkonformiert sein |
| 02.08.2027 | Hochrisiko-Systeme nach Anhang I (bestehende Produkte) |

Quelle: Art. 113 KI-VO (https://dejure.org/gesetze/KIVO/113.html).

---

*Aktenzeichen: TI-KI-2026-008. Erstellt von Dr. Falk Roosendaal, Marcus Petersen, Annegret Kühnhausen. Stand: März 2026.*
