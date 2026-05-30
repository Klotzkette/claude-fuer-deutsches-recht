# Aktenstück 20 — Handlungsplan: Feststellungen und Maßnahmen zur KI-VO-Konformität

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 05.05.2026  
**Bearbeitung:** RAin Dr. Henrietta Vellbruck-Steinheim, RA Dr. Mark Roosendaal  
**Adressaten:** CEO Dr. Theresia Vogelkamp, CTO Aravind Krishnamurthy (MedAssist AI GmbH)  
**Vertraulich — Anwalt-Mandant-Privileg**

---

## 1. Gesamtbefund

Die Konformitätsprüfung MedAssist v4 (KI-VO Art. 6–49) ergibt folgenden Befund:

| Artikel | Befund | Schwere |
|---|---|---|
| Art. 6 + Anhang III Nr. 7 — Einstufung Hochrisiko | Eindeutig zutreffend | — |
| Art. 9 — Risikomanagementsystem | Nicht konform | Kritisch |
| Art. 10 — Daten-Governance | Nicht konform | Kritisch |
| Art. 11 — Technische Dokumentation | Nicht konform | Kritisch |
| Art. 12 — Aufzeichnungspflichten | Teilweise konform (mit krit. Lücken) | Hoch |
| Art. 13 — Transparenz | Teilweise konform | Hoch |
| Art. 14 — Menschliche Aufsicht | Nicht konform (gravierendstes Defizit) | Kritisch |
| Art. 15 — Genauigkeit/Robustheit/Cyber | Nicht konform | Hoch |
| Art. 16 + Art. 17 — Anbieterpflichten + QMS | Nicht konform | Hoch |
| Art. 43 — Konformitätsbewertung | Nicht begonnen | Kritisch |
| Art. 47 — EU-Konformitätserklärung | Entwurf; nicht finalisierbar | Hoch |
| Art. 48 — CE-Kennzeichnung KI-VO | Noch nicht anbringbar | Hoch |
| Art. 49 — EU-Datenbank-Registrierung | Nicht erfolgt | Hoch |
| MDR-Schnittstelle | Koordination erforderlich | Mittel |
| GPAI (Llama) | Teildokumentation fehlt | Mittel |

**Frist:** 02.08.2026 (Art. 113 Abs. 1 KI-VO). Verbleibende Zeit: 89 Tage.

---

## 2. Kritischer Pfad bis 02.08.2026

```
Mai 2026
├── 07.05.2026 — Antwort BNetzA Nachforderung (Disponenten-ID-Logs)
├── 12.05.2026 — BNetzA Vor-Ort-Besichtigung Klinikum Mannheim-Süd
├── 15.05.2026 — Beauftragung TÜV SÜD für KI-VO-Konformitätsbewertung
├── 01.05.2026 — DPIA an BfDI
├── 30.04.2026 — Quittierungsschritt Roll-out abgeschlossen (18 Kliniken)
└── 31.05.2026 — Disponenten-Schulung gestartet

Juni 2026
├── 01.06.2026 — Vollständige technische Dokumentation (Anhang IV) an TÜV SÜD
├── 01.06.2026 — QMS nach Art. 17 errichtet und dokumentiert
├── 15.06.2026 — Bias-Analyse abgeschlossen
├── 30.06.2026 — Erklärbarkeits-Modul Dashboard live
└── 30.06.2026 — Adversarial Testing + ISO 27001-Rezertifizierung

Juli 2026
├── Mitte Juli — TÜV SÜD NB-Zertifikat KI-VO erwartet
├── 20.07.2026 — EU-Konformitätserklärung ausgestellt
├── 25.07.2026 — CE-Kennzeichnung KI-VO angebracht
└── 30.07.2026 — Registrierung EU-Datenbank (EUID generiert)

02.08.2026 — FRIST
```

---

## 3. Detaillierter Maßnahmenkatalog

### 3.1 Sofortmaßnahmen (bis 15.05.2026)

| # | Maßnahme | Verantwortlich | Frist | Status |
|---|---|---|---|---|
| S-1 | Quittierungsschritt-Roll-out alle 18 Kliniken | CTO Krishnamurthy | 30.04.2026 | Eingeleitet |
| S-2 | Antwort an BNetzA re Nachforderung (Disponenten-ID) | Dr. Vellbruck-Steinheim | 07.05.2026 | Offen |
| S-3 | DPIA erstellen und an BfDI übermitteln | Dr. Roosendaal | 01.05.2026 | In Bearbeitung |
| S-4 | Beauftragung TÜV SÜD KI-VO-Prüfung | Dr. Vellbruck-Steinheim | 15.05.2026 | Offen |
| S-5 | Selbstmeldung schwerwiegende Vorfälle 2025 an BNetzA | Dr. Vellbruck-Steinheim | 07.05.2026 | Offen |
| S-6 | Eindeutige Systemkennung (MA-ID) festlegen | CTO Krishnamurthy | 30.04.2026 | Offen |

### 3.2 Kurzfristmaßnahmen (bis 30.06.2026)

| # | Maßnahme | Verantwortlich | Frist |
|---|---|---|---|
| K-1 | Vollständige technische Dokumentation (Anhang IV) erstellen | CTO Krishnamurthy / Dr. Roosendaal | 01.06.2026 |
| K-2 | QMS nach Art. 17 KI-VO errichten und dokumentieren | CEO Dr. Vogelkamp / CTO Krishnamurthy | 01.06.2026 |
| K-3 | RMS aktualisieren (alle Vorfälle 2025, FMEA alle Module) | CTO Krishnamurthy | 30.04.2026 |
| K-4 | Bias-Analyse Trainingsdaten (Geschlecht, Alter) | CTO Krishnamurthy | 15.06.2026 |
| K-5 | Disponenten-Schulungsprogramm (Curriculum 4h) + Start | Dr. Vellbruck-Steinheim (Koordination) | 31.05.2026 |
| K-6 | ISO 27001:2022 Rezertifizierung | CTO Krishnamurthy | 30.06.2026 |
| K-7 | Adversarial Testing NLU-Modul | CTO Krishnamurthy | 30.06.2026 |
| K-8 | Benutzerhandbuch v4.2 (alle Art. 13-Anforderungen) | CTO Krishnamurthy | 31.05.2026 |
| K-9 | Erklärbarkeits-Modul Dashboard implementieren | CTO Krishnamurthy | 30.06.2026 |
| K-10 | Llama-3.1 System Card in technische Dokumentation | CTO Krishnamurthy | 31.05.2026 |

### 3.3 Finalmaßnahmen (Juli 2026)

| # | Maßnahme | Verantwortlich | Frist |
|---|---|---|---|
| F-1 | NB-Zertifikat TÜV SÜD entgegennehmen | TÜV SÜD / MedAssist | Mitte Juli |
| F-2 | EU-Konformitätserklärung finalisieren und unterzeichnen | CEO Dr. Vogelkamp | 20.07.2026 |
| F-3 | CE-Kennzeichnung KI-VO anbringen | CTO Krishnamurthy | 25.07.2026 |
| F-4 | EU-Datenbank registrieren (EUID) | CTO Krishnamurthy | 30.07.2026 |

---

## 4. Risikobewertung Fristwahrung

| Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Gegenmaßnahme |
|---|---|---|---|
| TÜV SÜD benötigt > 8 Wochen (Kapazitäten) | Mittel (30 %) | Fristüberschreitung | Frühzeitige Beauftragung; Alternativ-NB identifizieren |
| Bias-Analyse zeigt kritische Befunde (Nachbesserung) | Hoch (50 %) | Verzögerung techn. Doku | Puffer einplanen; partielle Dokumentation vorab |
| BNetzA eskaliert nach Vor-Ort-Besichtigung | Niedrig (15 %) | Vorläufige Maßnahme | Kooperationsstrategie, Handlungsplan vorlegen |
| Allianz SE kündigt D&O vor Frist | Mittel (40 %) | Persönliches Haftungsrisiko Vorstand | Verhandlung Allianz, Alternativversicherer |

---

*Heidelberg, 05.05.2026*  
*RAin Dr. Henrietta Vellbruck-Steinheim / RA Dr. Mark Roosendaal — Az. 2026-V-0427*
