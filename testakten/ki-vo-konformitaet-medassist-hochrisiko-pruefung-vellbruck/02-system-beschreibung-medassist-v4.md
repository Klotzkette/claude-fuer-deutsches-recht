# Aktenstück 02 — Systembeschreibung MedAssist v4

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 12.03.2026 (nach Übermittlung technischer Unterlagen durch CTO Krishnamurthy)  
**Bearbeitung:** RA Dr. Mark Roosendaal  
**Grundlage:** Technische Dokumentation MedAssist v4, Version 2.3 (interne Kennung: MA-TECH-DOC-2024-v4.2.3), übermittelt 08.03.2026

---

## 1. Systemidentität

| Merkmal | Angabe |
|---|---|
| Systemname | MedAssist v4 |
| Versionsnummer | 4.2.3 (Produktionsstand 18 Krankenhäuser) |
| Interne Kennung Anbieter | MA-SYS-2023-001 |
| Anbieter (Art. 3 Nr. 3 KI-VO) | MedAssist AI GmbH, Im Neuenheimer Feld 580, 69120 Heidelberg |
| Verwendungszweck | Automatisierte Notrufdisposition in Krankenhäusern — Klassifikation eingehender Notrufe, Dringlichkeitspriorisierung, Ressourcenzuweisung |
| Einsatzbereich | Notaufnahme-Leitstellen, Rettungskoordinationszentren in Krankenhäusern |
| Aktuelle Deployments | 18 Krankenhäuser in BW (12) und Bayern (6); Standorte s. Anhang A |
| Sprache (System) | Deutsch, mit begrenzter Englisch-Unterstützung (Notfallkommunikation) |
| Entwicklungszeitraum | 2021–2023 (v4); kontinuierliche Updates seit 2023 |

---

## 2. Systemarchitektur

MedAssist v4 besteht aus drei Hauptkomponenten, die über eine interne REST-API miteinander kommunizieren:

### 2.1 Sprachverarbeitungsmodul (NLU)
- **Funktion:** Echtzeit-Transkription und Semantikanalyse eingehender Notrufe
- **Basis:** Llama-3.1-70B-Instruct, fine-tuned auf medizinischen Notfalldatensatz (s. Aktenstück 05)
- **Bezeichnung intern:** „MedAssist-LLM-Core v4"
- **GPAI-Status:** Die Llama-Adaptation stellt eine GPAI-Modell-Nutzung i.S.d. Art. 3 Nr. 63 KI-VO dar; Anbieter-Dokumentation nach Art. 53 KI-VO ausstehend (s. Aktenstück 19)
- **Latenz:** < 800 ms für Transkription/Klassifikation
- **Ausgabe:** Strukturierter JSON-Datensatz mit Dringlichkeitsstufe (1–5), erkannter Kategorie (Herznotfall, Trauma, pädiatrisch, psychiatrisch, sonstig), Konfidenzwert (0–1)

### 2.2 Dispositionsmodul (DEM)
- **Funktion:** Zuweisung verfügbarer Notfallressourcen basierend auf NLU-Ausgabe, Echtzeit-Kapazitätsdaten der Stationen und historischen Verfügbarkeitsprofilen
- **Methode:** Gradient Boosting (XGBoost v2.0), trainiert auf 3 Jahre Krankenhausdaten (2020–2023)
- **Ausgabe:** Empfohlene Ressourcenzuweisung mit Konfidenzwert und alternativen Optionen (Top-3)
- **Menschliche Schnittstelle:** Vorschlag wird im Leitstellen-Dashboard angezeigt; Übernahme-Button durch Disponent erforderlich (konzeptionell)

### 2.3 Audit-Trail-Modul (ATM)
- **Funktion:** Protokollierung aller Systemereignisse (Eingabe, Klassifikation, Disposition, Bedieneraktion, Zeitstempel)
- **Datenhaltung:** 5 Jahre (intern definiert), verschlüsselt auf Klinikum-Infrastruktur
- **Schnittstelle:** Export-API für Behördenanfragen (BNetzA, BfArM)

---

## 3. Datenfluss (vereinfacht)

```
Eingehender Notruf (Audio)
        ↓
   NLU-Modul (Llama-Adaptation)
   — Transkription
   — Klassifikation (Dringlichkeit, Kategorie, Konfidenz)
        ↓
   Dispositionsmodul (XGBoost)
   — Kapazitätsabgleich Echtzeitdaten
   — Top-3-Empfehlung
        ↓
   Leitstellen-Dashboard
   — Anzeige Empfehlung
   — [Disponent: Übernahme / Ablehnung]  ← kritische Aufsichtslücke (Art. 14)
        ↓
   Audit-Trail-Modul
   — Protokollierung
```

**Feststellung:** Das Übernahme-Interface ist in der aktuellen Produktionsversion 4.2.3 nicht vollständig implementiert. In 14 der 18 Krankenhäuser übernehmen Disponenten die Empfehlung ohne explizite Bestätigung im System — es fehlt ein erzwungener Quittierungsschritt (s. Aktenstück 09, Art. 14-Befund).

---

## 4. Trainingsdaten (Überblick)

| Datensatz | Herkunft | Umfang | Zeitraum | Repräsentativitätsdokumentation |
|---|---|---|---|---|
| MIMIC-IV Emergency | PhysioNet (US), MIT/BIDMC | ca. 430.000 Notfallprotokolle | 2008–2019 | Keine DE-spezifische Validierung |
| NEMSIS 3.5 | NHTSA (US) | ca. 2,1 Mio. EMS-Datensätze | 2019–2022 | Keine EU-Anpassung dokumentiert |
| Klinikinterne Trainingsdaten (anonymisiert) | 3 Partnerkliniken BW | ca. 18.000 Einsatzprotokolle | 2021–2023 | Begrenzte Repräsentativität |

**Kernproblem:** Die US-amerikanischen Datensätze (MIMIC-IV, NEMSIS) sind dominant und weisen strukturelle Unterschiede zum deutschen Rettungsdienstsystem auf (andere Klassifikationsschemata, abweichende Ressourcentypen, US-spezifische Terminologie). Eine dokumentierte Repräsentativitätsprüfung für den deutschen Einsatzkontext fehlt, was Art. 10 Abs. 2 lit. f KI-VO verletzt (s. Aktenstück 05).

---

## 5. Technische Leistungsparameter (nach internem Testbericht MA-EVAL-2024-03)

| Metrik | Wert | Bewertung |
|---|---|---|
| Accuracy (Dringlichkeitsstufe, gesamt) | 84,3 % | Unzureichend für klinischen Einsatz bei Fehlen menschlicher Aufsicht |
| Recall Dringlichkeit 1 (lebensbedrohlich) | 91,2 % | Positiv, aber Fehlerrate bei 8,8 % kritisch |
| False-Negative-Rate Dringlichkeit 1 | 8,8 % | Hochriskant: jede 11. lebensbedrohliche Lage wird unterklassifiziert |
| Accuracy Kategorisierung | 78,6 % | Ungenügend, v.a. psychiatrische Notfälle (62,1 %) |
| Latenz 95. Perzentile | 1.240 ms | Überschreitet internen Zielwert (< 800 ms) unter Last |
| Bias-Kennzahl (Geschlecht) | Nicht erhoben | Verstoß Art. 10 Abs. 2 lit. g KI-VO |
| Bias-Kennzahl (Alter) | Nicht erhoben | Verstoß Art. 10 Abs. 2 lit. g KI-VO |

---

## 6. Einsatzumgebung

MedAssist v4 wird auf klinikkumseitiger On-Premises-Infrastruktur betrieben. Jede Klinik hostet eine lokale Instanz; Updates werden zentral durch MedAssist AI GmbH eingespielt (Remote-Deployment-Kapazität). Die lokalen Instanzen kommunizieren nicht miteinander; Trainingsdaten werden klinikkumseitig nicht zurückgespiegelt.

**Datenschutzrechtliche Einordnung:** Jede Klinik ist Verantwortliche i.S.d. Art. 4 Nr. 7 DSGVO für die verarbeiteten Patientendaten; MedAssist AI GmbH ist Auftragsverarbeiterin i.S.d. Art. 4 Nr. 8 DSGVO. Auftragsverarbeitungsverträge gemäß Art. 28 DSGVO liegen laut Angabe des Mandanten vor, wurden jedoch noch nicht auf KI-VO-Konformität geprüft.

---

## 7. Bewertungsstand Aktenstück 02

Dieses Aktenstück fasst die von MedAssist AI GmbH übermittelte technische Dokumentation zusammen. Detailprüfungen der einzelnen Artikel-Anforderungen folgen in Aktenstücken 03–15. Die vorstehende Beschreibung stützt sich auf die technische Dokumentation v4.2.3 sowie die mündlichen Erläuterungen von CTO Krishnamurthy im Gespräch vom 08.03.2026.

---

*Heidelberg, 12.03.2026*  
*RA Dr. Mark Roosendaal — Az. 2026-V-0427*
