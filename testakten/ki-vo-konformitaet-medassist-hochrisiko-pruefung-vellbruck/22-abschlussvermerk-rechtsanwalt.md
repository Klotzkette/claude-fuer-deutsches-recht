# Aktenstück 22 — Abschlussvermerk Rechtsanwältin

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 30.06.2026  
**Verfasserin:** RAin Dr. Henrietta Vellbruck-Steinheim  
**Kanzlei:** Vellbruck & Partner mbB, Erbprinzenstraße 14, 69117 Heidelberg  
**Gegenstand:** Abschlussvermerk KI-VO-Konformitätsprüfung MedAssist v4

---

## 1. Mandat und Auftrag

Die Kanzlei Vellbruck & Partner mbB wurde am 03.03.2026 durch die MedAssist AI GmbH mandatiert, eine vollständige Konformitätsprüfung des KI-Systems MedAssist v4 nach der Verordnung (EU) 2024/1689 (KI-VO) durchzuführen und bei der Herstellung der Konformität bis zur Frist 02.08.2026 (Art. 113 Abs. 1 KI-VO) zu beraten.

---

## 2. Zusammenfassung der Prüfungsergebnisse

### 2.1 Einstufung

MedAssist v4 ist eindeutig als Hochrisiko-KI-System nach Art. 6 Abs. 2 KI-VO i.V.m. Anhang III Nr. 7 KI-VO einzustufen. Diese Einstufung ist rechtlich nicht anfechtenswert. Zugleich ist MedAssist v4 Medizinprodukt Klasse IIb nach MDR (EU) 2017/745 (bestätigt durch BfArM, Az. MED-AI-2026-0319). Die MDR-Konformität ist formal bestätigt, materiell jedoch in einzelnen Punkten zu hinterfragen (Accuracy-Niveau, menschliche Aufsicht).

### 2.2 Identifizierte Defizite (Prüfungsbeginn März 2026)

Bei Aufnahme des Mandats bestanden kritische Verstöße gegen:
- Art. 9 KI-VO (kein funktionsfähiges, kontinuierliches RMS)
- Art. 10 KI-VO (US-Trainingsdaten ohne Repräsentativitätsnachweis; keine Bias-Analyse)
- Art. 11 KI-VO (unvollständige technische Dokumentation)
- Art. 12 KI-VO (keine Disponenten-ID-Protokollierung in 14 Kliniken)
- Art. 14 KI-VO (fehlender Quittierungsschritt; schwerster Befund)
- Art. 15 KI-VO (unzureichende Accuracy; abgelaufene ISO 27001-Zertifizierung)
- Art. 16, 17 KI-VO (kein QMS; keine Vorfallmeldungen)
- Art. 43, 47, 48, 49 KI-VO (Konformitätsbewertung, Erklärung, CE, Registrierung nicht eingeleitet)

### 2.3 Stand der Maßnahmen (30.06.2026)

| Maßnahme | Status |
|---|---|
| Quittierungsschritt Roll-out 18 Kliniken | Abgeschlossen (30.04.2026) |
| Disponenten-ID-Protokollierung 18 Kliniken | Abgeschlossen (07.05.2026) |
| DPIA an BfDI | Übermittelt (01.05.2026); BfDI-Rückmeldung ausstehend |
| Disponenten-Schulung | Durchgeführt (31.05.2026, 18 Kliniken) |
| TÜV SÜD beauftragt | 16.05.2026; Prüfung läuft |
| Technische Dokumentation (Anhang IV) | Fertiggestellt (28.05.2026); bei TÜV SÜD |
| QMS nach Art. 17 KI-VO | Errichtet und dokumentiert (01.06.2026) |
| RMS aktualisiert | Abgeschlossen (30.04.2026) |
| Bias-Analyse | Abgeschlossen (15.06.2026); Befunde positiv (keine kritischen Biases, aber leichte Unterrepräsentation älterer Patienten dokumentiert) |
| ISO 27001:2022 Rezertifizierung | In Bearbeitung; Zertifikat erwartet 15.07.2026 |
| Adversarial Testing NLU | Abgeschlossen (29.06.2026); kein kritischer Befund |
| Benutzerhandbuch v4.2 | Fertiggestellt (31.05.2026) |
| Erklärbarkeits-Modul Dashboard | Live (28.06.2026) |
| Llama-3.1 System Card integriert | Abgeschlossen (27.05.2026) |
| Selbstmeldung Vorfälle 2025 an BNetzA | Erfolgt (07.05.2026) |
| NB-Zertifikat TÜV SÜD (KI-VO) | Erwartet Mitte Juli 2026 |
| EU-Konformitätserklärung | Ausstehend (nach NB-Zertifikat) |
| CE-Kennzeichnung KI-VO | Ausstehend |
| EU-Datenbank-Registrierung | Ausstehend |

---

## 3. Rechtliche Prognose

Auf der Grundlage des Fortschrittstands vom 30.06.2026 und der zu erwartenden TÜV-SÜD-Prüfungsdauer (4–5 Wochen) ist die Wahrscheinlichkeit einer fristgerechten Konformität bis 02.08.2026 als hoch einzustufen, sofern:

1. Das TÜV-SÜD-NB-Zertifikat bis spätestens 21.07.2026 ausgestellt wird
2. Keine gravierenden Nachforderungen durch TÜV SÜD entstehen
3. Die ISO 27001-Rezertifizierung bis 15.07.2026 abgeschlossen ist

**Restrisiken:**
- BfDI-Rückmeldung zur DPIA könnte ergänzende Maßnahmen verlangen
- Bias-Befund (leichte Unterrepräsentation älterer Patienten) wird in DPIA und technischer Dokumentation adressiert; formelle Beanstandung durch BfDI nicht auszuschließen
- D&O-Versicherung: Allianz SE hat nach Vorlage des Handlungsplans Verlängerung bis 30.09.2026 gewährt; endgültige Entscheidung nach NB-Zertifikat

---

## 4. Haftungsrechtlicher Hinweis

Dieser Abschlussvermerk dokumentiert den Stand der rechtlichen Beratung zum 30.06.2026. Er ersetzt nicht die eigenverantwortliche unternehmerische Entscheidung des Mandanten. Die vollständige Konformität mit der KI-VO ist erst nach Vorlage des NB-Zertifikats, Ausstellen der EU-Konformitätserklärung, Anbringen der CE-Kennzeichnung und Registrierung in der EU-Datenbank gegeben. Bis dahin befindet sich MedAssist AI GmbH in einem Übergangsstatus, der durch die dokumentierten Fortschritte und die eingereichten Behördenberichte abgesichert ist.

Die Kanzlei Vellbruck & Partner mbB haftet nach Maßgabe des Anwaltsvertrags und der BRAO; eine Garantie für den Ausgang behördlicher oder gerichtlicher Verfahren kann nicht gegeben werden.

---

## 5. Fortführung des Mandats

Die Kanzlei empfiehlt, das Mandat über den 02.08.2026 hinaus fortzuführen für:
- Begleitung des TÜV-SÜD-Abschlussverfahrens
- Überwachung des BfDI-Verfahrens
- Laufende KI-VO-Compliance-Beratung (Post-Market-Monitoring, Art. 72)
- Verteidigung im BNetzA-Verfahren bis zur Verfahrenseinstellung

---

*Heidelberg, 30.06.2026*

RAin Dr. Henrietta Vellbruck-Steinheim  
Vellbruck & Partner mbB  
Erbprinzenstraße 14  
69117 Heidelberg  
Telefon: 06221 / 84 90-0  
E-Mail: h.vellbruck-steinheim@vellbruck-partner.de

*Aktenzeichen: 2026-V-0427*
