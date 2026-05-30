# Aktenstück 06 — Art. 11 KI-VO: Technische Dokumentation (Anhang IV)

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 25.03.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 11 KI-VO (EU) 2024/1689; Anhang IV KI-VO

---

## 1. Anforderungsüberblick

Art. 11 Abs. 1 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, vor dem Inverkehrbringen eine technische Dokumentation zu erstellen und fortzuführen. Der Mindestinhalt ergibt sich aus Anhang IV KI-VO. Die Dokumentation muss Marktüberwachungsbehörden eine Beurteilung der Konformität ermöglichen.

---

## 2. Anhang-IV-Checkliste MedAssist v4

| Anforderung Anhang IV | Dokument Mandant | Vollständigkeit | Befund |
|---|---|---|---|
| 1. Allgemeine Systembeschreibung | MA-TECH-DOC-2024-v4.2.3, Kap. 1 | Teilweise | Einsatzszenario vorhanden; GPAI-Komponente nicht beschrieben |
| 2. Detaillierte Beschreibung der Elemente des Systems | MA-TECH-DOC-2024-v4.2.3, Kap. 2–4 | Teilweise | NLU beschrieben; Dispositionsmodul nur rudimentär |
| 3. Überwachung, Funktion und Kontrolle des Systems | Kein separates Dokument | Fehlend | Art. 14-Elemente fehlen gänzlich |
| 4. Beschreibung von Änderungen | Change-Log MA-TECH-2023–2025 | Teilweise | Kein Verfahren für sicherheitsrelevante Änderungen |
| 5. Risikomanagementsystem | MA-RISK-2024-01 | Unvollständig | S. Aktenstück 04 |
| 6. Beschreibung der relevanten Daten (Training, Validierung, Test) | Datensatzbeschreibung MA-DATA-2023 | Unvollständig | Kein Repräsentativitätsnachweis (s. Aktenstück 05) |
| 7. Beschreibung der verwendeten Metriken und Schwellenwerte | MA-EVAL-2024-03, Anhang B | Vorhanden | Metriken sind dokumentiert |
| 8. Beschreibung der menschlichen Aufsicht | Benutzerhandbuch v4.1 (Abschn. 7) | Unvollständig | Aufsichtsmechanismus konzeptionell, nicht implementiert |
| 9. Beschreibung der Validierungsmaßnahmen | MA-EVAL-2024-03 | Teilweise | Fehlende klinische Validierungsstudie |
| 10. Logbuch/Aufzeichnungen | ATM-Spezifikation v2 | Teilweise | Datenhaltungskonzept lückenhaft (s. Aktenstück 07) |
| 11. Informationen für Nutzer | Benutzerhandbuch v4.1 | Teilweise | Fehlende Erklärbarkeits-Informationen |

**Gesamtergebnis:** Von 11 Anhang-IV-Kategorien: 1 vollständig erfüllt, 6 teilweise erfüllt, 4 fehlend oder unvollständig.

---

## 3. Kritische Lücken

### 3.1 GPAI-Basiskomponente nicht dokumentiert (Anhang IV Nr. 1, 2)

Die technische Dokumentation beschreibt MedAssist-LLM-Core v4 als eigenentwickeltes Modul, ohne die Llama-3.1-Basisarchitektur und den Fine-Tuning-Prozess offenzulegen. Dies ist aus rechtlicher Sicht unzureichend:

- Art. 11 Abs. 3 KI-VO: Sofern ein KI-System auf einem GPAI-Modell basiert, umfasst die technische Dokumentation auch die nach Art. 53 Abs. 1 KI-VO erforderlichen Informationen.
- Die Llama-Adaptation ist ein GPAI-Modell i.S.d. Art. 3 Nr. 63 KI-VO (s. Aktenstück 19); entsprechend müssen Modellarchitektur, Trainingsparameter, Systemcard und Evaluierungsergebnisse in die Dokumentation einbezogen werden.

### 3.2 Fehlende klinische Validierungsstudie (Anhang IV Nr. 9)

Eine prospektive oder retrospektive klinische Validierungsstudie in deutschen Krankenhäusern ist nicht vorgelegt worden. MA-EVAL-2024-03 enthält nur interne Testläufe. Für ein Medizinprodukt Klasse IIb mit KI-Komponente ist eine klinische Evaluierung nach Art. 61 MDR i.V.m. Anhang XIV MDR erforderlich; diese muss mit der Anforderung des Art. 9 Abs. 7 KI-VO (Testing unter realen Bedingungen) koordiniert werden.

### 3.3 Fehlende Erklärbarkeit und Interpretierbarkeit (Anhang IV Nr. 11)

Das Benutzerhandbuch v4.1 enthält keine Informationen darüber, wie das System zu seinen Klassifikations-Empfehlungen gelangt. Disponenten können die Systemempfehlung nicht auf ihre Plausibilität hin überprüfen, da keine Erklärbarkeits-Ausgabe vorhanden ist (kein Confidence-Breakdown, keine SHAP-Werte oder äquivalente Methode). Dies verstärkt das Art. 14-Defizit (s. Aktenstück 09).

---

## 4. Handlungsempfehlungen

| Maßnahme | Priorität | Frist |
|---|---|---|
| Vollständige Neufassung technische Dokumentation (Anhang-IV-konform) | Kritisch | 31.05.2026 |
| Integration GPAI-Dokumentation Llama-Adaptation | Hoch | 30.04.2026 |
| Klinische Validierungsstudie beauftragen | Hoch | Start 01.04.2026 |
| Erklärbarkeits-Modul für Benutzeroberfläche entwickeln | Hoch | 30.06.2026 |
| Change-Control-Verfahren für technische Dokumentation einführen | Mittel | 30.05.2026 |

---

## 5. Gesamtbewertung Art. 11

**Art. 11 KI-VO: Nicht konform.**  
Die technische Dokumentation ist strukturell unvollständig und deckt zentrale Anhang-IV-Anforderungen nicht ab. Bis zur Frist 02.08.2026 muss eine vollständige, Anhang-IV-konforme Dokumentation vorliegen.

---

*Heidelberg, 25.03.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
