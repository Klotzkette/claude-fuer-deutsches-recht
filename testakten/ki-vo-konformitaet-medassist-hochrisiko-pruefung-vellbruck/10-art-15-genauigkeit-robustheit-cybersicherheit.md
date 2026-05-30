# Aktenstück 10 — Art. 15 KI-VO: Genauigkeit, Robustheit und Cybersicherheit

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 08.04.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 15 KI-VO (EU) 2024/1689; ISO/IEC 27001:2022

---

## 1. Anforderungen Art. 15 KI-VO

Art. 15 KI-VO verlangt, dass Hochrisiko-KI-Systeme angemessene Genauigkeits-, Robustheitss- und Cybersicherheitsniveaus erreichen und während des gesamten Lebenszyklus aufrechterhalten. Im Einzelnen:

- **Genauigkeit (Art. 15 Abs. 1):** Angemessene Genauigkeitsniveaus unter Berücksichtigung des Einsatzbereichs; Angabe im Anhang IV und in der Betreiberanleitung
- **Robustheit (Art. 15 Abs. 3):** Widerstandsfähigkeit gegen Fehler, Ausfälle, Inkonsistenzen; Resilienz gegen Manipulation
- **Cybersicherheit (Art. 15 Abs. 4–5):** Schutz vor Angriffen, die zu unerwünschten Systemverhalten führen; Anforderungen entsprechend NIS-2-Richtlinie und einschlägiger Normen

---

## 2. Genauigkeit

### 2.1 Ist-Stand (aus MA-EVAL-2024-03)

| Metrik | Wert | Benchmark | Einschätzung |
|---|---|---|---|
| Overall Accuracy Dringlichkeit | 84,3 % | > 95 % (klinischer Standard) | Unzureichend |
| Recall Dringlichkeitsstufe 1 (lebensbedrohlich) | 91,2 % | > 98 % (Sicherheitsgrenzwert) | Unzureichend |
| False-Negative-Rate Dringlichkeit 1 | 8,8 % | < 2 % | Kritisch |
| Accuracy psychiatrische Notfälle | 62,1 % | > 80 % | Kritisch |
| Accuracy pädiatrische Notfälle | 71,4 % | > 85 % | Nicht ausreichend |
| Accuracy Traumata | 88,2 % | > 90 % | Grenzwertig |

### 2.2 Fehlende Genauigkeitsangaben im Benutzerhandbuch

Die Accuracy-Daten aus MA-EVAL-2024-03 sind nicht im Benutzerhandbuch und nicht in der Technischen Dokumentation ausgewiesen. Disponenten haben damit keinen Zugang zu den tatsächlichen Leistungsgrenzen des Systems — was die Transparenz-Anforderungen nach Art. 13 und die Aufsichtsanforderungen nach Art. 14 zusätzlich verletzt.

### 2.3 Konzeptdrift

Das Dispositionsmodul (XGBoost) wurde auf Daten 2020–2023 trainiert. Ein Monitoring auf Konzeptdrift (Performance-Verschlechterung durch veränderte Datenverteilung im Produktionseinsatz 2023–2026) findet nicht statt. Die Accuracy-Daten aus 2024 könnten den tatsächlichen Produktionsstand bereits überoptimistisch darstellen.

---

## 3. Robustheit

### 3.1 Technische Robustheit

| Szenario | Getestet | Befund |
|---|---|---|
| Hintergrundlärm (Notfallambiente) | Ja | Performance-Abfall bei > 70 dB Hintergrundlärm auf 74,2 % Accuracy |
| Fremdsprachige Anrufer | Nein | Ungetestet — erhebliches Risiko |
| Starker Dialekt (bayer., schwäb.) | Teilweise | Leichter Performance-Abfall (–3,1 %) |
| Systemüberlastung (> 50 parallele Notrufe) | Ja | Latenzüberschreitung 95. Pz. 1.240 ms |
| Modell-Adversarial Inputs | Nein | Kein Adversarial Testing dokumentiert |
| Netzwerkausfall (Teilausfall) | Ja | Graceful Degradation implementiert |

### 3.2 Fallback bei Systemausfall

Wie in Aktenstück 08 festgestellt, fehlt ein dokumentiertes Fallback-Verfahren. Der 47-minütige Ausfall im Klinikum Freiburg-Süd (2025) demonstriert das reale Ausfallrisiko.

---

## 4. Cybersicherheit

### 4.1 ISO/IEC 27001:2022 Zertifizierung

MedAssist AI GmbH ist seit 2022 nach ISO/IEC 27001:2022 zertifiziert (Zertifikat TÜV Rheinland, ausgestellt 14.06.2022, gültig bis 13.06.2025). **Das Zertifikat ist am 13.06.2025 abgelaufen und wurde bislang nicht erneuert.** CTO Krishnamurthy hat bestätigt, dass die Rezertifizierung verschoben wurde.

**Rechtliche Einschätzung:** Ein abgelaufenes ISO 27001-Zertifikat stellt keine ausreichende Grundlage für den Nachweis der Cybersicherheitsanforderungen nach Art. 15 Abs. 4 KI-VO dar. Die Rezertifizierung ist vordringlich.

### 4.2 KI-spezifische Angriffsvektoren

Art. 15 Abs. 5 KI-VO adressiert ausdrücklich KI-spezifische Angriffe (Adversarial Attacks, Datenvergiftung, Modell-Evasion). Für MedAssist v4 ist kein Penetrationstest mit KI-spezifischen Angriffsvektoren dokumentiert. Insbesondere:

- **Adversarial Inputs auf NLU:** Manipulierte Sprachsequenzen, die das NLU-Modell zur Falschklassifikation verleiten (z.B. Echtzeit-Audio-Manipulation), sind ungetestet
- **Datenvergiftung:** Da Kliniken prinzipiell lokale Instanzen betreiben, ist eine dezentrale Angriffsfläche vorhanden, die im Sicherheitskonzept nicht adressiert wird

### 4.3 NIS-2-Bezug

Krankenhäuser ab einer bestimmten Größe sind als „wichtige Einrichtungen" i.S.d. NIS-2-Umsetzungsgesetzes (NIS2UmsuCG) klassifiziert. MedAssist AI GmbH als KRITIS-naher Softwareanbieter muss prüfen, ob eigene NIS-2-Pflichten bestehen (als wesentlicher Lieferant). Diese Prüfung steht aus.

---

## 5. Handlungsempfehlungen

| Maßnahme | Priorität | Frist |
|---|---|---|
| Rezertifizierung ISO/IEC 27001:2022 | Kritisch | 31.05.2026 |
| Adversarial Testing NLU-Modul | Hoch | 30.06.2026 |
| Implementierung Konzeptdrift-Monitoring | Hoch | 30.06.2026 |
| Test fremdsprachige Anrufer / Dialekte | Mittel | 30.06.2026 |
| NIS-2-Eigenprüfung als Lieferant | Mittel | 31.05.2026 |
| Dokumentation Accuracy-Daten in Benutzerhandbuch | Hoch | 31.05.2026 |

---

## 6. Gesamtbewertung Art. 15

**Art. 15 KI-VO: Nicht konform.**  
Unzureichende Genauigkeit für kritischen Einsatzbereich, abgelaufene Cybersicherheitszertifizierung, fehlendes Adversarial Testing.

---

*Heidelberg, 08.04.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
