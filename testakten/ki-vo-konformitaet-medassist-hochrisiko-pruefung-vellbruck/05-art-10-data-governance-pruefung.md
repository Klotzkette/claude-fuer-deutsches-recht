# Aktenstück 05 — Art. 10 KI-VO: Prüfung Daten-Governance und Trainingsdaten

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 22.03.2026  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Rechtsgrundlage:** Art. 10 KI-VO (EU) 2024/1689; DSGVO Art. 9, 22, 35

---

## 1. Anforderungen Art. 10 KI-VO

Art. 10 KI-VO normiert für Hochrisiko-KI-Systeme qualitative Mindeststandards für Trainings-, Validierungs- und Testdatensätze:

- Geeignete Datenverwaltungspraktiken (Art. 10 Abs. 1)
- Kriterien für Datenselektion, Datenerhebungsmethoden und -verfahren (Art. 10 Abs. 2 lit. a–c)
- Repräsentativitätsprüfung für den Einsatzkontext (Art. 10 Abs. 2 lit. f)
- Prüfung auf Bias und Datendefizite, die zu Grundrechtsverletzungen führen könnten (Art. 10 Abs. 2 lit. g)
- Schutzmaßnahmen bei Verarbeitung besonderer Kategorien personenbezogener Daten (Art. 10 Abs. 5), einschließlich der KI-VO-spezifischen Voraussetzungen für Bias-Prüfungen

---

## 2. Prüfung Trainingsdatensätze

### 2.1 MIMIC-IV Emergency Dataset (PhysioNet)

**Herkunft:** Massachusetts Institute of Technology / Beth Israel Deaconess Medical Center (Boston, USA). Datenbasis: US-amerikanische Notaufnahmedaten 2008–2019 aus einem einzigen Universitätsklinikum.

**Wesentliche Defizite:**

| Defizit | KI-VO-Anforderung | Bewertung |
|---|---|---|
| Keine dokumentierte Eignung für deutschen Rettungsdienstkontext | Art. 10 Abs. 2 lit. f | Nicht erfüllt |
| Abweichendes Klassifikationsschema (ESI vs. Manchester Triage System) | Art. 10 Abs. 2 lit. c | Nicht erfüllt |
| US-spezifische Diagnosecodierung (ICD-10-CM ≠ ICD-10-GM) | Art. 10 Abs. 2 lit. c | Nicht erfüllt |
| Kein EU-Datenschutzregime (PHI nach HIPAA, kein DSGVO-Pendant) | DSGVO Art. 9 Abs. 2 | Risiko: fehlende Rechtsgrundlage für Nachnutzung |
| Keine demografische Repräsentativitätsanalyse für EU-Bevölkerung | Art. 10 Abs. 2 lit. g | Nicht erfüllt |

**Feststellung:** Die Verwendung von MIMIC-IV ohne dokumentierte Validierung für den deutschen Einsatzkontext stellt einen Verstoß gegen Art. 10 Abs. 2 lit. f KI-VO dar.

### 2.2 NEMSIS 3.5 Dataset (NHTSA, USA)

**Herkunft:** National Highway Traffic Safety Administration (US Federal Government). Datenbasis: ca. 2,1 Mio. EMS-Datensätze (Emergency Medical Services) aus 48 US-Bundesstaaten, 2019–2022.

**Wesentliche Defizite:**

| Defizit | KI-VO-Anforderung | Bewertung |
|---|---|---|
| Rettungsdienst-Strukturen USA ≠ Deutschland (Notarzt-System vs. Paramedic-System) | Art. 10 Abs. 2 lit. f | Nicht erfüllt |
| Dominanz ruraler US-Gebiete, fehlende Großstadt-Äquivalenz zu deutschen Metropolregionen | Art. 10 Abs. 2 lit. f | Nicht erfüllt |
| Keine Bias-Analyse (Rasse, Ethnizität als US-Kategorien nicht auf DE-Kontext übertragbar) | Art. 10 Abs. 2 lit. g | Nicht erfüllt |
| Keine DSGVO-Rechtsgrundlage; PhysioNet-Lizenz keine Grundlage für EU-Deployment | Art. 10 Abs. 1; DSGVO Art. 9 | Kritisch |

### 2.3 Klinikinterne Trainingsdaten (BW)

**Herkunft:** Drei Partnerkliniken in Baden-Württemberg (anonymisiert übermittelt). Ca. 18.000 Einsatzprotokolle, 2021–2023.

**Positive Feststellungen:**
- Auftragsverarbeitungsvertrag nach Art. 28 DSGVO liegt vor
- Anonymisierungsverfahren ist dokumentiert (Pseudonymisierung + k-Anonymität k=5)
- Daten bilden deutschen Rettungsdienstkontext ab

**Verbleibende Defizite:**
- Umfang (18.000 Datensätze) im Vergleich zu US-Datensätzen (2,5 Mio.) marginal — starkes Ungleichgewicht führt zur faktischen Dominanz des US-Musters
- Drei Partnerkliniken decken nicht die geographische und demographische Vielfalt der 18 Zielhäuser ab
- Keine Repräsentativitätsanalyse für Bayern (6 der 18 Kliniken liegen in Bayern; Trainingsdaten sind ausschließlich aus BW)

---

## 3. Bias-Prüfung (Art. 10 Abs. 2 lit. g)

Art. 10 Abs. 2 lit. g KI-VO verlangt die Überprüfung von Trainings-, Validierungs- und Testdaten auf mögliche Bias, die zu diskriminierenden Ausgaben führen können, insbesondere in Bezug auf Merkmale nach Art. 14 GRCh (u.a. Geschlecht, Alter, ethnische Herkunft).

**Feststellung:** Der Mandant hat keine Bias-Prüfung durchgeführt. CTO Krishnamurthy bestätigte im Gespräch vom 18.03.2026, dass entsprechende Analysen „geplant, aber noch nicht umgesetzt" seien.

**Risikobewertung:** Medizinische KI-Systeme mit ungeprüften Biases führen nachweislich zu Unterversorgung vulnerabler Gruppen. Für den Notfallkontext ist dokumentiert, dass weibliche Patienten mit Herzinfarkten systematisch unterklassifiziert werden (vgl. wissenschaftliche Literatur: Obermeyer et al., Science 366:447–453, 2019). Ohne Bias-Prüfung besteht erhebliches Haftungsrisiko und Verstoß gegen Art. 10 Abs. 2 lit. g KI-VO.

---

## 4. Datenschutzrechtliche Dimension (DSGVO Art. 9, 35)

Die bei der Inferenz verarbeiteten Patientendaten (eingehende Notrufe, Echtzeit-Stationsdaten) sind besondere Kategorien personenbezogener Daten nach Art. 9 Abs. 1 DSGVO (Gesundheitsdaten). Die Verarbeitung ist nur unter den Voraussetzungen des Art. 9 Abs. 2 DSGVO zulässig, insbesondere Art. 9 Abs. 2 lit. h (medizinische Versorgung). Dies ist grundsätzlich erfüllbar, aber in den AVV der 18 Kliniken noch nicht einheitlich abgebildet.

Die BfDI hat mit Schreiben vom 15.02.2026 (Az. 13-3120/004#0117) eine Datenschutz-Folgenabschätzung nach Art. 35 DSGVO verlangt. Die Anforderung ist berechtigt: Art. 35 Abs. 3 lit. a DSGVO verlangt eine DPIA bei systematischer, umfangreicher Verarbeitung besonderer Kategorien. Die DPIA steht aus (s. auch Aktenstück 17).

---

## 5. Handlungsempfehlungen

| Maßnahme | Priorität | Frist | Verantwortlich |
|---|---|---|---|
| Vollständige Bias-Analyse aller Trainingsdatensätze (Geschlecht, Alter) | Kritisch | 30.04.2026 | CTO Krishnamurthy |
| Validierungsstudie US-Datensätze für deutschen Einsatzkontext | Kritisch | 15.05.2026 | CTO Krishnamurthy |
| Erweiterung klinikinterne Trainingsdaten auf Bayern-Stichprobe | Hoch | 30.06.2026 | CTO Krishnamurthy |
| DPIA erstellen und BfDI vorlegen | Hoch | 01.05.2026 | Dr. Roosendaal (federführend) |
| AVV-Überprüfung 18 Kliniken re Art. 9 DSGVO | Mittel | 31.05.2026 | Dr. Roosendaal |
| Dokumentation Repräsentativitätsprüfung | Hoch | 30.05.2026 | CTO Krishnamurthy |

---

## 6. Gesamtbewertung Art. 10

**Art. 10 KI-VO: Nicht konform.**  
Kritische Defizite bei Repräsentativität der US-Trainingsdaten, fehlende Bias-Analyse, unklare DSGVO-Rechtsgrundlage für US-Daten-Nachnutzung. Höchste Priorität im Handlungsplan.

---

*Heidelberg, 22.03.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
