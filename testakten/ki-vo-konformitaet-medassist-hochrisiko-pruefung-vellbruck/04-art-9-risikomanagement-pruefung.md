# Aktenstück 04 — Art. 9 KI-VO: Prüfung Risikomanagementsystem MedAssist v4

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 18.03.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 9 KI-VO (EU) 2024/1689

---

## 1. Anforderungen Art. 9 KI-VO

Art. 9 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, ein Risikomanagementsystem (RMS) einzurichten, das:

- kontinuierlich über den gesamten Lebenszyklus des Systems betrieben wird (Art. 9 Abs. 1),
- alle Risiken identifiziert und analysiert, die durch das System entstehen können (Art. 9 Abs. 2 lit. a),
- diese Risiken angemessen bewertet (Art. 9 Abs. 2 lit. b),
- geeignete Risikomanagementmaßnahmen ergreift (Art. 9 Abs. 2 lit. c–d),
- nach dem Stand der Technik und bekannten Best Practices ausgestaltet ist (Art. 9 Abs. 4),
- Tests und Prüfungen vor Inverkehrbringen und laufend beinhaltet (Art. 9 Abs. 5 und 7),
- Restrisiken kommuniziert (Art. 9 Abs. 6).

---

## 2. Vorgefundene Dokumentation des Mandanten

CTO Krishnamurthy übermittelte am 15.03.2026 folgende Unterlagen:

| Dokument | Stand | Bewertung |
|---|---|---|
| Risikoanalyse MedAssist v4 (intern, MA-RISK-2024-01) | März 2024 | Veraltet, vor MDR-CE-Bewertung erstellt; nicht aktualisiert |
| FMEA-Dokument NLU-Modul | Oktober 2023 | Unvollständig; fehlt Bewertung des Dispositionsmoduls |
| Testbericht MA-EVAL-2024-03 | Dezember 2024 | Vorhanden, enthält Accuracy-Daten |
| Incident-Log 2025 | Laufend | 23 gemeldete Anomalien, davon 3 als schwerwiegend klassifiziert |

---

## 3. Befunde

### 3.1 Fehlende Kontinuität des RMS (Art. 9 Abs. 1)

Das RMS wurde bei Markteinführung von MedAssist v4 (2023) einmalig etabliert, jedoch nicht kontinuierlich fortgeschrieben. Insbesondere:

- Die Risikoanalyse MA-RISK-2024-01 berücksichtigt weder die 23 im Jahr 2025 gemeldeten Anomalien noch die drei als schwerwiegend klassifizierten Vorfälle.
- Nach den drei Incident-Reports aus 2025 (Unterklassifikation von Schlaganfall-Notrufen in zwei Kliniken sowie ein Systemausfall von 47 Minuten in Klinikum Freiburg-Süd) wurde das RMS nicht angepasst.
- Es fehlt ein formelles Verfahren zur Aktualisierung des RMS bei sicherheitsrelevanten Ereignissen.

**Rechtliche Einschätzung:** Verstoß gegen Art. 9 Abs. 1 KI-VO. Die Pflicht zur kontinuierlichen Pflege des RMS ist eindeutig verletzt.

### 3.2 Unvollständige Risikoidentifikation (Art. 9 Abs. 2 lit. a)

Die FMEA deckt nur das NLU-Modul ab. Das Dispositionsmodul (XGBoost-basiert) sowie das Audit-Trail-Modul wurden nicht separat analysiert. Insbesondere fehlt:

- Analyse der Bias-Risiken (Geschlecht, Alter, ethnische Herkunft) für beide KI-Module
- Analyse des Risikos durch Konzeptdrift (Trainingsdaten 2008–2022, Deployment 2023–2026)
- Analyse der Kaskadeneffekte: Fehler des NLU-Moduls werden durch das Dispositionsmodul nicht korrigiert, sondern verstärkt

### 3.3 Fehlende Bewertung nach Schweregrad und Eintrittswahrscheinlichkeit (Art. 9 Abs. 2 lit. b)

MA-RISK-2024-01 enthält keine strukturierte Risikomatrix. Risiken werden qualitativ beschrieben, aber nicht quantitativ bewertet. Eine Priorisierung nach Schadensausmaß × Eintrittswahrscheinlichkeit fehlt vollständig.

### 3.4 Unvollständige Risikomanagementmaßnahmen (Art. 9 Abs. 2 lit. c)

Die drei schwerwiegenden Vorfälle aus 2025 haben keine dokumentierten Gegenmaßnahmen ausgelöst. RA Dr. Roosendaal hat CTO Krishnamurthy am 18.03.2026 schriftlich darauf hingewiesen, dass dies ein erhebliches Konformitätsdefizit darstellt.

### 3.5 Stand der Technik (Art. 9 Abs. 4)

Das RMS referenziert nicht den für medizinische KI-Systeme einschlägigen Stand der Technik:
- ISO 14971:2019 (Risikomanagement Medizinprodukte) liegt zwar als MDR-Anforderung vor, wird aber nicht in das KI-VO-spezifische RMS integriert.
- IEC 62304 (Software-Lebenszyklus Medizinprodukte) wird im RMS nicht erwähnt.
- ENISA-Leitlinien zur KI-Sicherheit (2023) werden nicht berücksichtigt.

### 3.6 Positive Feststellungen

- Testbericht MA-EVAL-2024-03 enthält umfangreiche Leistungsdaten (Accuracy, Latenz), die als Grundlage für ein verbessertes RMS taugen.
- Incident-Log 2025 ist vorhanden und wird laufend geführt; der Logging-Mechanismus als solcher funktioniert.

---

## 4. Handlungsempfehlungen

| Maßnahme | Priorität | Frist | Verantwortlich |
|---|---|---|---|
| Vollständige Aktualisierung RMS unter Einbeziehung aller Vorfälle 2025 | Kritisch | 30.04.2026 | CTO Krishnamurthy |
| Erweiterung FMEA auf Dispositionsmodul und ATM | Hoch | 30.04.2026 | CTO Krishnamurthy |
| Einführung quantitativer Risikomatrix (Schadensausmaß × Eintrittswahrscheinlichkeit) | Hoch | 15.05.2026 | CTO Krishnamurthy |
| Integration ISO 14971 in KI-VO-RMS | Hoch | 15.05.2026 | Dr. Roosendaal (Koordination) |
| Dokumentierte Gegenmaßnahmen für 3 schwerwiegende Vorfälle 2025 | Kritisch | 15.04.2026 | CTO Krishnamurthy |
| Formelles RMS-Update-Verfahren einführen (Change Control) | Mittel | 30.05.2026 | CTO Krishnamurthy |

---

## 5. Gesamtbewertung Art. 9

**Art. 9 KI-VO: Nicht konform.**  
Schwerwiegende Defizite in Kontinuität, Vollständigkeit und Dokumentation. Kritisches Risiko für Fristwahrung 02.08.2026. Sofortmaßnahmen erforderlich.

---

*Heidelberg, 18.03.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
