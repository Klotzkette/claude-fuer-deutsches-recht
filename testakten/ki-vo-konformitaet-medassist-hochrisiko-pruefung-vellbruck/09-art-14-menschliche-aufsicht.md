# Aktenstück 09 — Art. 14 KI-VO: Menschliche Aufsicht — Kernbefund

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 04.04.2026  
**Bearbeitung:** RAin Dr. Henrietta Vellbruck-Steinheim  
**Rechtsgrundlage:** Art. 14 KI-VO (EU) 2024/1689

---

## 1. Rechtlicher Rahmen Art. 14 KI-VO

Art. 14 KI-VO ist das zentrale Schutzinstrument der Hochrisiko-KI-Regulierung. Es verpflichtet Anbieter, Hochrisiko-KI-Systeme so zu gestalten, dass sie während des Betriebs wirksam von natürlichen Personen überwacht werden können. Die Anforderungen im Einzelnen:

- Das System muss so konzipiert sein, dass Betreiber es überwachen können (Art. 14 Abs. 1)
- Es müssen Werkzeuge zur Überwachung bereitgestellt werden (Art. 14 Abs. 2)
- Das System muss identifizierbar als KI-System sein (Art. 14 Abs. 2 lit. a)
- Es müssen Mechanismen vorhanden sein, damit Betreiber eingreifen, übersteuern oder das System stoppen können (Art. 14 Abs. 4 lit. e)
- Für Systeme nach Anhang III mit besonders erhöhtem Risiko: vollständige Überprüfung vor jeder Output-Umsetzung, sofern technisch zumutbar (Art. 14 Abs. 5)

---

## 2. Der Kernbefund: Strukturelle Aufsichtslücke

Dies ist der gravierendste Einzelbefund der gesamten Konformitätsprüfung.

**Sachverhalt:** In 14 der 18 Krankenhäuser, in denen MedAssist v4 im Einsatz ist, gibt es keinen technisch erzwungenen Quittierungsschritt vor der Umsetzung der Systemempfehlung. Das Leitstellen-Dashboard zeigt die Empfehlung an (Dringlichkeitsstufe, Kategorie, Ressourcenzuweisung), jedoch übernehmen Disponenten die Empfehlung in der Praxis durch bloße Weiterleitung an die jeweilige Station — ohne expliziten Bestätigungsklick im System und ohne protokollierte Überprüfung.

In den verbleibenden 4 Kliniken (Universitätsklinikum Freiburg, Klinikum Stuttgart, Klinikum Nürnberg-Nord, Kreisklinik Ravensburg) wurde ein Bestätigungsmechanismus als Pilotfunktion (Beta) implementiert. Dort ist ein ausdrücklicher „Bestätigen"-Button erforderlich, bevor die Ressourcenzuweisung aktiviert wird.

**Rechtliche Einschätzung:** Die Situation in den 14 Kliniken verstößt gegen Art. 14 Abs. 4 lit. e KI-VO. Der Anbieter (MedAssist AI GmbH) ist verpflichtet, technische Maßnahmen bereitzustellen, die wirksame menschliche Aufsicht ermöglichen. Die bloße konzeptionelle Vorstellung, dass Disponenten überwachen, ohne dass dies technisch erzwungen oder protokolliert wird, erfüllt die Anforderung nicht.

---

## 3. Risikobeurteilung

### 3.1 Automatisierungsverzerrung (Automation Bias)

Psychologische Forschung und medizinische Studien belegen, dass in Hochstress-Umgebungen (Notfalldisposition) Automation Bias besonders stark ausgeprägt ist: Operatoren übernehmen Systemempfehlungen unkritisch, wenn keine explizite Überprüfungsaufforderung besteht (vgl. Parasuraman & Manzey, Ergonomics 53:1354–1366, 2010). Bei MedAssist v4 bedeutet dies:

- Die 8,8 % False-Negative-Rate bei Dringlichkeit 1 wird in der Praxis nicht durch menschliche Korrekturen aufgefangen
- Der konzeptionelle Override wird zur Fiktion

### 3.2 Haftungsrechtliche Konsequenz

Die fehlende menschliche Aufsicht hat unmittelbare haftungsrechtliche Konsequenzen für die Kliniken als Betreiber. Eine Unterklassifikation (Dringlichkeit 1 → Dringlichkeit 2) mit Patientenschaden würde produkthaftungsrechtliche Ansprüche gegen MedAssist AI GmbH (Anbieter) begründen. Für die Produkthaftung nach dem Produkthaftungsgesetz (ProdHaftG) i.d.F. der Umsetzung der Richtlinie (EU) 2024/2853 ist das Vorliegen eines Produktfehlers (fehlende Sicherheit) zu bejahen, wenn das System ohne ausreichende Aufsichtsmechanismen in Verkehr gebracht wurde. Vgl. allgemein zur Produkthaftungsdogmatik bei KI-Systemen: Spickhoff, MedR 2023, 1 ff.; Detterbeck, VersR 2022, 1445 ff.

### 3.3 Verhältnis zu MDR

Nach MDR Anhang I Nr. 14.5 müssen Medizinprodukte der Klasse IIb sicherstellen, dass der Anwender Fehlalarme und Fehlfunktionen erkennen kann. Die fehlende Overriding-Möglichkeit ist auch aus MDR-Perspektive problematisch — was erklärt, warum das BfArM im Bescheid MED-AI-2026-0319 explizit auf das ausstehende KI-VO-Konformitätserfordernis hinwies.

---

## 4. Schulungsdefizit

Art. 14 Abs. 3 KI-VO verlangt, dass Betreiber Maßnahmen ergreifen, die sicherstellen, dass das Personal, das das System überwacht, ausreichend kompetent ist. MedAssist AI GmbH hat bislang keine standardisierte Schulung für Disponenten entwickelt. Die vorhandene Einweisungsunterlage (2 Seiten A4) ist nicht geeignet, das erforderliche Kompetenzniveau sicherzustellen:

- Keine Schulung zur Erkennung von Klassifikationsfehlern
- Keine Schulung zu Systemgrenzen (Accuracy-Limits, Bias-Risiken)
- Keine Übungen zum Override-Verfahren

---

## 5. Sofortmaßnahme und Chronologie

Am 04.04.2026 hat RAin Dr. Vellbruck-Steinheim CEO Dr. Vogelkamp und CTO Krishnamurthy in einem Videogespräch auf die Dringlichkeit dieses Befundes hingewiesen. CTO Krishnamurthy hat zugesagt, den Pflicht-Quittierungsschritt (Bestätigen-Button) auf alle 18 Kliniken bis 30.04.2026 auszurollen.

**Wichtig:** Der Roll-out des Quittierungsschritts allein reicht nicht aus. Zusätzlich erforderlich:

| Maßnahme | Frist |
|---|---|
| Roll-out Pflicht-Quittierungsschritt auf alle 18 Kliniken | 30.04.2026 |
| Standardisierte Disponenten-Schulung (Curriculum, 4h) | 31.05.2026 |
| Protokollierung aller Override-Aktionen inkl. Disponenten-ID | 30.04.2026 |
| Dashboard-Ergänzung: Konfidenzwert prominent + Erklärungshinweis | 30.06.2026 |
| Jährliche Schulungswiederholung einführen | Ab 01.08.2026 |

---

## 6. Gesamtbewertung Art. 14

**Art. 14 KI-VO: NICHT konform. Gravierendstes Defizit der Prüfung.**  
In 14 von 18 Kliniken fehlt die technisch erzwungene menschliche Aufsicht vollständig. Sofortmaßnahmen wurden eingeleitet. Vollständige Konformität erfordert technische Umsetzung, Schulung und Protokollierung bis 30.06.2026 (Puffer vor Frist 02.08.2026).

---

*Heidelberg, 04.04.2026*  
*RAin Dr. Henrietta Vellbruck-Steinheim — Az. 2026-V-0427*
