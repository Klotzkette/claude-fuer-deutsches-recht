# Aktenstück 19 — GPAI-Basiskomponente: Llama-Adaptation, Art. 53 KI-VO, Systemcard

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 28.04.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 3 Nr. 63, Art. 51–55 KI-VO (EU) 2024/1689 (GPAI-Modelle)

---

## 1. Rechtlicher Rahmen: GPAI-Modelle nach KI-VO

Die KI-VO reguliert in Kapitel V (Art. 51–55) erstmals explizit sogenannte Allzweck-KI-Modelle (GPAI — General Purpose AI). Ein GPAI-Modell i.S.d. Art. 3 Nr. 63 KI-VO ist ein KI-Modell, das mit einer großen Datenmenge trainiert wurde, auf breiter Basis verfügbar ist und eine Vielzahl von Aufgaben erfüllen kann.

**Relevanz für MedAssist v4:** Die NLU-Kernkomponente „MedAssist-LLM-Core v4" basiert auf Llama-3.1-70B-Instruct von Meta AI, das durch Fine-Tuning auf medizinische Notfalldaten angepasst wurde. Llama-3.1 ist ein anerkanntes GPAI-Modell; das Fine-Tuning ändert nichts an dieser Grundnatur.

---

## 2. GPAI-Anbieterpflichten (Art. 53 KI-VO)

Art. 53 KI-VO verpflichtet GPAI-Modellanbieter zu:

| Pflicht | Art. 53 Abs. | Erfüllungsort bei MedAssist v4 |
|---|---|---|
| Technische Dokumentation des Modells (Systemcard) | Art. 53 Abs. 1 lit. a | Meta AI (Llama-Anbieter) — nicht MedAssist |
| Informationen für nachgelagerte Anbieter | Art. 53 Abs. 1 lit. b | Meta AI; zu prüfen ob MedAssist weiterverpflichtet |
| Urheberrechtsrichtlinien-konformes Training | Art. 53 Abs. 1 lit. c | Meta AI (Training Llama-3.1) |
| Zusammenfassung Trainingsinhalte (öffentlich) | Art. 53 Abs. 1 lit. d | Meta AI |

### 2.1 Differenzierung: Meta AI vs. MedAssist AI GmbH als GPAI-Anbieter

**Grundsatz:** Der GPAI-Anbieter ist die Partei, die das Modell trainiert und in Verkehr bringt. Bei reinem Downstream-Fine-Tuning (Anpassung des vortrainierten Modells) stellt sich die Frage, ob der Fine-Tuner selbst zum GPAI-Anbieter wird.

**Rechtseinschätzung:** Nach Art. 3 Nr. 63 i.V.m. Art. 51 Abs. 2 KI-VO: Wer ein GPAI-Modell durch Fine-Tuning wesentlich modifiziert, übernimmt die Anbieterstellung für das modifizierte Modell, sofern das Resultat weiterhin als GPAI-Modell einzustufen ist (d.h. generalistische Verwendbarkeit wäre erhalten).

**MedAssist AI GmbHs Position:** Das Fine-Tuning wurde ausschließlich auf medizinische Notfallkommunikation ausgerichtet. MedAssist-LLM-Core v4 hat damit keine generalistische Verwendbarkeit mehr — es ist ein spezialisiertes Anwendungsmodell, kein GPAI-Modell. Damit entfallen die GPAI-Anbieterpflichten nach Art. 53 KI-VO für MedAssist AI GmbH.

**Jedoch (kritischer Befund):** Die Nutzung des GPAI-Modells Llama-3.1 als Basis verpflichtet MedAssist AI GmbH als nachgelagerter Anbieter nach Art. 11 Abs. 3 KI-VO, die vom Llama-Anbieter (Meta AI) bereitgestellten Informationen in die eigene technische Dokumentation zu integrieren. Dies ist bislang nicht erfolgt.

---

## 3. Verfügbare Llama-3.1-GPAI-Dokumentation von Meta AI

Meta AI hat für Llama-3.1 folgende Dokumentation veröffentlicht (Stand April 2026):

- **System Card Llama 3.1:** https://ai.meta.com/llama — enthält Trainingsarchitektur, Datenanmerkungen, Evaluierungsergebnisse, Sicherheitsbewertungen
- **Acceptable Use Policy:** Einschränkungen für Hochrisiko-Anwendungen (u.a. medizinische Diagnose ohne menschliche Aufsicht explizit eingeschränkt)
- **RAIL-Lizenzbedingungen:** Nutzungseinschränkungen für bestimmte Anwendungsfälle

**Kritischer Befund:** Die Acceptable Use Policy von Llama-3.1 schließt die eigenständige medizinische Diagnose ohne menschliche Aufsicht aus. MedAssist v4 bewegt sich in einem Grenzbereich: Die Notrufdisposition ist keine „Diagnose" im klinischen Sinne, enthält aber klassifikatorische Urteile mit medizinischem Charakter. Die fehlende menschliche Aufsicht (Art. 14-Defizit) könnte auch eine Verletzung der Meta-Lizenzbedingungen darstellen — was rechtlich komplizierte Konsequenzen hätte.

---

## 4. Systemcard-Anforderungen nach Art. 52 KI-VO

Art. 52 Abs. 1 KI-VO: GPAI-Modellanbieter mit systemischem Risiko (Trainingsrechenaufwand > 10^25 FLOP) haben erweiterte Pflichten, einschließlich Model Evaluation (Red Teaming) und Systemcard mit erweitertem Inhalt. Llama-3.1-70B: Der Trainingsaufwand liegt bei ca. 6,4 × 10^23 FLOP — damit unterhalb der Systemrisiko-Schwelle. Die erweiterten Art. 52-Pflichten gelten nicht für Llama-3.1-70B.

---

## 5. Handlungsempfehlungen

| Maßnahme | Priorität | Frist |
|---|---|---|
| Integration Llama-3.1 System Card in technische Dokumentation MedAssist v4 | Hoch | 30.05.2026 |
| Rechtliche Prüfung Meta RAIL-Lizenz auf Vereinbarkeit mit Notrufdisposition ohne vollständige Aufsicht | Hoch | 15.05.2026 |
| Fine-Tuning-Dokumentation (Trainingsparameter, Datensatz, Evaluierungsergebnisse) erstellen | Hoch | 31.05.2026 |
| Klärung mit Meta AI, ob Deployment in kritischer Infrastruktur zulässig | Mittel | 31.05.2026 |

---

## 6. Gesamtbewertung GPAI-Komponente

**GPAI-Anbieterstellung von MedAssist AI GmbH: Nicht gegeben** (da Fine-Tuning zur Spezialisierung führt). **Pflicht zur Integration der Llama-Upstream-Dokumentation: Nicht erfüllt.** Lizenzrechtliche Risiken durch fehlende Aufsicht: Erheblich. Sofortige Integration in technische Dokumentation und rechtliche Lizenzprüfung erforderlich.

---

*Heidelberg, 28.04.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
