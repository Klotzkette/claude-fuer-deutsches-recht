# Aktenstück 16 — MDR (EU) 2017/745: Klasse IIb, Notified Body, Doppelkonformität

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 22.04.2026  
**Bearbeitung:** RAin Dr. Henrietta Vellbruck-Steinheim  
**Rechtsgrundlage:** MDR (EU) 2017/745; Art. 8 KI-VO (EU) 2024/1689

---

## 1. MDR-Einordnung MedAssist v4

### 1.1 Klasse-IIb-Klassifizierung

Nach Regel 11 Anhang VIII MDR gilt für medizinische Software: Software, die zur Kontrolle physiologischer Prozesse eingesetzt wird oder Informationen zur Diagnose, Therapie oder Prävention von Erkrankungen liefert, ist als Medizinprodukt einzustufen. MedAssist v4 klassifiziert medizinische Notfälle, schlägt Therapieressourcen (Spezialisten, Reanimationsteams) vor und priorisiert Ressourcen in lebensbedrohlichen Situationen. Dies führt nach Regel 11 Abs. 3 Anhang VIII MDR zur Klassifizierung als Klasse IIb (erhöhtes Risiko bei Fehlfunktionen; Schäden schwerwiegend, aber nicht zwangsläufig irreversibel; Verwendung in lebensbedrohlichem Umfeld).

### 1.2 Abgrenzung zu Klasse III

Klasse III (höchste Risikokategorie) wäre einschlägig, wenn das System unmittelbar lebenserhaltende Funktionen steuert (z.B. autonome Medikamentendosierung). Da MedAssist v4 dispositionsunterstützend ist und keine unmittelbare Therapiesteuerung vornimmt, verbleibt es bei Klasse IIb — sofern die menschliche Aufsicht tatsächlich wirksam ist (was aktuell bezweifelt werden muss; s. Aktenstück 09).

---

## 2. BfArM-Bescheid (Az. MED-AI-2026-0319)

Das BfArM hat mit Bescheid vom 12.01.2026 die MDR-Konformität von MedAssist v4 Klasse IIb bestätigt. Der Bescheid basiert auf:

- NB-Zertifikat TÜV SÜD NB 0123, ausgestellt 20.11.2025, gültig bis 20.11.2028
- Technischem Dossier MedAssist v4 Version 4.2.0 (Stand August 2024)
- Klinische Evaluierung nach Art. 61 MDR i.V.m. Anhang XIV MDR (klinische Daten aus Partnerkliniken 2021–2023)

**Wichtiger Hinweis im BfArM-Bescheid:**
> „Die vorliegende Feststellung beschränkt sich auf die Anforderungen der Verordnung (EU) 2017/745. Anforderungen der KI-VO (EU) 2024/1689 werden von diesem Bescheid nicht erfasst. Für eine vollständige Konformität des Produkts mit dem gesamten EU-Recht ist die Einhaltung der KI-VO durch das Unternehmen eigenverantwortlich sicherzustellen."

---

## 3. Schnittstellenanalyse MDR / KI-VO

### 3.1 Klinische Evaluierung MDR vs. Art. 9 Abs. 7 KI-VO

Die MDR-Klinische Evaluierung (Anhang XIV MDR) und das KI-VO-Testing unter realen Bedingungen (Art. 9 Abs. 7 KI-VO) überschneiden sich in der Zielsetzung, sind aber unterschiedliche rechtliche Instrumente. Empfohlen wird ein koordinierter Ansatz: Erweiterung der MDR-Klinischen Evaluierung um KI-VO-spezifische Test-Dimensionen (Bias, Robustheit, Adversarial Testing).

### 3.2 Grundlegende Sicherheits- und Leistungsanforderungen (MDR Anhang I) vs. Art. 15 KI-VO

MDR Anhang I, insbesondere Nr. 14 (allgemeine Anforderungen für Software als Medizinprodukt), verlangt ähnliche Genauigkeits- und Sicherheitsanforderungen wie Art. 15 KI-VO. Die Abweichung: Die False-Negative-Rate von 8,8 % bei Dringlichkeit 1 wirft die Frage auf, ob das MDR-Anforderungsniveau tatsächlich erfüllt ist — oder ob das NB die Klinische Evaluierung nur auf Basis der Partnerklinik-Daten (mit begrenztem Aussagewert) positiv beschieden hat.

**Empfehlung:** Überprüfung, ob das BfArM-Verfahren Anlass gibt, das NB-Zertifikat nach § 87 MDR zu überprüfen. Dies ist eine intern heikle Thematik, da eine Infragestellung des MDR-CE die Marktstellung von MedAssist v4 weiter destabilisieren würde.

### 3.3 Post-Market Surveillance MDR (Art. 83–84) vs. Art. 72 KI-VO

Beide Regime verlangen Post-Market-Überwachung. Das MDR-PMS-System (vorhanden, als Teil des NB-Verfahrens) kann als Grundlage für das KI-VO-Post-Market-Monitoring nach Art. 72 KI-VO genutzt werden, muss aber um KI-spezifische Dimensionen (Konzeptdrift, Bias-Monitoring, Accuracy-Tracking) ergänzt werden.

---

## 4. Empfehlungen zur Doppelkonformitätsstrategie

| Bereich | MDR-Anforderung | KI-VO-Anforderung | Koordinationsmaßnahme |
|---|---|---|---|
| Technische Dokumentation | Anhang II MDR | Anhang IV KI-VO | Zusammenführung in Gesamt-Technisches Dossier |
| Klinische Validierung | Anhang XIV MDR | Art. 9 Abs. 7 KI-VO | Erweiterung MDR-Klinische Evaluierung |
| Post-Market | Art. 83–84 MDR | Art. 72 KI-VO | MDR-PMS um KI-VO-Dimensionen erweitern |
| Vorfallmeldung | Art. 87 MDR (BfArM) | Art. 73 KI-VO (BNetzA) | Koordiniertes Meldemanagement einrichten |
| NB-Zertifizierung | TÜV SÜD NB 0123 (MDR) | TÜV SÜD NB 0123 (KI-VO) | Gemeinsame Prüftermine vereinbaren |

---

## 5. Gesamtbewertung MDR-Schnittstelle

Die MDR-Konformität ist formal bestätigt, inhaltlich aber in Teilen fragwürdig (angesichts der False-Negative-Rate und der Aufsichtslücke). Die Doppelkonformität ist technisch machbar, erfordert aber eine koordinierte Dokumentationsstrategie und gemeinsame Prüftermine mit TÜV SÜD. Priorität: Erweiterung MDR-Klinische Evaluierung für KI-VO-Zwecke.

---

*Heidelberg, 22.04.2026*  
*RAin Dr. Henrietta Vellbruck-Steinheim — Az. 2026-V-0427*
