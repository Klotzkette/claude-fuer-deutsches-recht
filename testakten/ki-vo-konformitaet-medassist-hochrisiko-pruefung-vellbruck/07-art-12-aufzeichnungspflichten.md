# Aktenstück 07 — Art. 12 KI-VO: Aufzeichnungspflichten und Logging

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 28.03.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 12 KI-VO (EU) 2024/1689

---

## 1. Anforderungen Art. 12 KI-VO

Art. 12 Abs. 1 KI-VO verlangt, dass Hochrisiko-KI-Systeme technische Möglichkeiten zur automatischen Aufzeichnung von Ereignissen (Logs) während des Betriebs bieten. Art. 12 Abs. 2 KI-VO konkretisiert: die Aufzeichnungsfähigkeit soll mindestens die Überwachung des Systembetriebs hinsichtlich Ereignissen ermöglichen, die Risiken darstellen oder zu wesentlichen Veränderungen führen. Art. 12 Abs. 3 KI-VO legt für Hochrisiko-KI unter Anhang III besondere Aufzeichnungsanforderungen fest:
- Zeitraum jeder Verwendung (Start/Ende)
- Referenzdatenbank, anhand derer Eingabedaten abgeglichen wurden
- Datum, Zeitpunkt, Ergebnis (inkl. Konfidenzwert) jedes Output
- Identität der natürlichen Person, die das System überwacht hat

---

## 2. Bestandsaufnahme Audit-Trail-Modul (ATM) MedAssist v4

Das Audit-Trail-Modul ist die Logging-Komponente von MedAssist v4 (s. Aktenstück 02, Abschn. 2.3). Technische Spezifikation: ATM-Spezifikation v2, Stand Oktober 2024.

### 2.1 Was wird aufgezeichnet

| Ereignis | Aufgezeichnet | Format | Bewertung |
|---|---|---|---|
| Zeitpunkt Notruf-Eingang | Ja | ISO 8601 | Konform |
| Transkriptionsstart/-ende | Ja | ISO 8601 | Konform |
| NLU-Klassifikation (Dringlichkeit, Kategorie) | Ja | JSON | Konform |
| Konfidenzwert NLU-Ausgabe | Ja | Float 0–1 | Konform |
| DEM-Empfehlung (Top-1 und Alternativen) | Teilweise | JSON (nur Top-1) | Nicht vollständig |
| Identität des Disponenten (Override-Aktion) | Nur in 4 von 18 Kliniken | — | Nicht konform |
| Zeitpunkt Disponent-Aktion | Nur in 4 von 18 Kliniken | — | Nicht konform |
| Systemausfälle / Anomalien | Ja | Syslog | Konform |
| Modellversion (NLU, DEM) | Nein | — | Fehlt |

### 2.2 Datenhaltungsdauer

ATM-Spezifikation v2 sieht eine Datenhaltung von 5 Jahren vor. Art. 12 KI-VO legt keine exakte Mindestfrist fest, verweist aber auf zweckadäquate Aufbewahrung. Für medizinische Kontexte ist eine Mindesthaltung von 10 Jahren nach § 630f BGB (Dokumentationspflicht Behandlungsunterlagen) bzw. §§ 28, 36 Berufsordnungen zu erwägen. Die Diskrepanz zwischen 5-Jahre-Logging-Frist (KI-VO) und 10-Jahre-Dokumentationspflicht (Medizinrecht) ist zu koordinieren.

### 2.3 Zugriff und Export

Eine Export-API für Behördenanfragen ist vorhanden (REST, JSON-Format). Im BNetzA-Marktüberwachungsverfahren (Az. 1-101.05-2026/MA-008) wurde am 01.03.2026 ein erstes Auskunftsersuchen gestellt. MedAssist AI GmbH hat am 15.03.2026 Teile der Logs exportiert und übermittelt. Der BNetzA-Inspektor hat mit Schreiben vom 22.03.2026 moniert, dass die Disponenten-Identitätsdaten in den Logs fehlten.

---

## 3. Kritische Befunde

### 3.1 Fehlende Disponenten-Identität (Art. 12 Abs. 3 lit. d)

In 14 der 18 Kliniken wird die Identität des Disponenten, der das System überwacht oder eine Entscheidung getroffen hat, nicht protokolliert. Dies ist ein direkter Verstoß gegen Art. 12 Abs. 3 lit. d KI-VO. Gleichzeitig ist dies eng verbunden mit dem Art. 14-Defizit: Wenn nicht einmal protokolliert wird, wer die Überwachung ausgeübt hat, ist eine retrospektive Beurteilung der menschlichen Aufsicht unmöglich.

### 3.2 Fehlende Modellversion im Log (Art. 12 Abs. 2)

Die Protokollierung der Modellversion ist für Nachvollziehbarkeit bei Audit-Anfragen der BNetzA unerlässlich. Ohne Versions-Logging kann nicht festgestellt werden, welche Modellversion zum Zeitpunkt eines Vorfalls aktiv war. Dies ist bei den drei schwerwiegenden Vorfällen aus 2025 bereits problematisch geworden.

### 3.3 Inkomplette DEM-Top-3-Aufzeichnung

Das Dispositionsmodul protokolliert nur die Top-1-Empfehlung, nicht die Alternativen (Top-2, Top-3). Für die Überprüfung, ob dem Disponenten relevante Alternativen präsentiert wurden, sind aber auch die nicht gewählten Optionen relevant.

---

## 4. Handlungsempfehlungen

| Maßnahme | Priorität | Frist |
|---|---|---|
| Roll-out Disponenten-ID-Logging auf alle 18 Kliniken | Kritisch | 30.04.2026 |
| Ergänzung Modellversionierung in ATM | Kritisch | 30.04.2026 |
| Erweiterung DEM-Logging auf Top-3-Empfehlungen | Mittel | 31.05.2026 |
| Abstimmung Datenhaltungsdauer mit medizinrechtlichen Anforderungen | Hoch | 15.05.2026 |
| Aktualisierung ATM-Spezifikation v3 | Hoch | 31.05.2026 |

---

## 5. Gesamtbewertung Art. 12

**Art. 12 KI-VO: Teilweise konform (mit kritischen Lücken).**  
Die Logging-Grundinfrastruktur ist vorhanden. Die Nichtprotokollierung der Disponenten-Identität in 14 Kliniken und die fehlende Modellversionierung sind kritische Verstöße, die für das BNetzA-Marktüberwachungsverfahren unmittelbaren Klärungsbedarf auslösen.

---

*Heidelberg, 28.03.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
