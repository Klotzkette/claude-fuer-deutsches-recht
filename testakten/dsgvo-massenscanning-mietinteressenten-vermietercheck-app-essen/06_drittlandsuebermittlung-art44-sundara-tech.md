# 06 — Drittlandsuebermittlung Art. 44 ff. DSGVO: Sundara Tech Pvt. Ltd. (Bengaluru)

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RA Lars Drosselberg, RA Dr. Cornelius Specht
**Datum:** 18. Januar 2026
**Betreff:** Rechtmaessigkeit der Datenübermittlung nach Indien ohne SCC

---

## 1. Sachverhaltsdarstellung

### 1.1 Dienstleister Sundara Tech Pvt. Ltd.

- **Firma:** Sundara Tech Pvt. Ltd.
- **Sitz:** No. 42, 4th Floor, Prestige Tech Park, Sarjapur Road, Bengaluru, Karnataka 560103, Indien
- **Tätigkeit:** Softwareentwicklung und Second-Level-Support für ProspectScore Pro
- **Vertragsbeziehung:** Entwicklungsvertrag seit Oktober 2022; Auftragsverarbeitungsvertrag (AVV) seit Dezember 2023 (nachträglich)
- **Datenzugang:** Zugriff auf Produktionsdaten für Debugging und Modelltraining (Rohdaten der Mietinteressenten)

### 1.2 Art der übermittelten Daten

| Datenkategorie | Uebermittlungsweg | Verschlüsselung |
|----------------|------------------|-----------------|
| Mietinteressenten-Rohdaten (Scoring) | API-Call (REST) | TLS 1.2 |
| ML-Trainings-Datensätze | S3-Bucket (shared) | Ja (S3-SSE) |
| Support-Log-Daten mit Personenbezug | VPN-Tunnel | Ja |
| Staging-Datenbankdump (anonymisiert?) | SFTP | Nein |

Laut Penetrationstest-Bericht (s. Akte 07) enthielt der Staging-Datenbankdump nicht vollständig anonymisierte Datensätze — eine Re-Identifizierung war technisch möglich.

---

## 2. Rechtsrahmen Drittlandübermittlung

### 2.1 Grundsatz Art. 44 DSGVO

Gemaess Art. 44 DSGVO darf eine Übermittlung personenbezogener Daten, die gerade verarbeitet werden oder nach ihrer Übermittlung in ein Drittland verarbeitet werden sollen, nur erfolgen, wenn der Verantwortliche und der Auftragsverarbeiter die in Kapitel V DSGVO niedergelegten Bedingungen einhalten.

### 2.2 Angemessenheitsbeschluss für Indien?

**Stand Januar 2026:** Für Indien existiert kein Angemessenheitsbeschluss der Europäischen Kommission gemaess Art. 45 DSGVO. Das Digital Personal Data Protection Act (DPDPA) Indiens (2023) wurde bislang nicht als gleichwertig mit der DSGVO eingestuft.

Folge: Jede Datenübermittlung nach Indien bedarf geeigneter Garantien gemaess Art. 46 DSGVO.

### 2.3 Geeignete Garantien Art. 46 DSGVO

Mögliche geeignete Garantien:

| Garantie | Art. 46 Abs. | Status bei VCS |
|----------|------|---------|
| Standarddatenschutzklauseln (SCC) — EU-Kommission 2021 | Abs. 2 lit. c | **Nicht abgeschlossen** |
| Verbindliche interne Datenschutzvorschriften (BCR) | Abs. 2 lit. b | Nicht anwendbar (kein Konzern) |
| Genehmigter Verhaltenskodex mit Zusatzmassnahmen | Abs. 2 lit. e | Nicht vorhanden |
| Zertifizierung mit verbindlichen Verpflichtungen | Abs. 2 lit. f | Nicht vorhanden |
| Ad-hoc-Vertragsklauseln (Genehmigung LDI) | Abs. 3 | Nicht beantragt |

**Ergebnis:** Keine der möglichen Garantien wurde implementiert. Die Datenübermittlung an Sundara Tech erfolgte seit Oktober 2022 ohne Rechtsgrundlage nach Kapitel V DSGVO.

---

## 3. Zusätzliche Anforderungen an SCC (EDSA-Empfehlung 01/2020)

Selbst bei Abschluss von SCC wäre nach der Schrems-II-Rechtsprechung (EuGH C-311/18 — Schrems II) eine Transferfolgenabschaetzung (Transfer Impact Assessment, TIA) erforderlich, da das Rechtssystem des Empfängerlandes (Indien) auf seine Eignung bewertet werden muss.

### 3.1 Rechtslage Indien (TIA-Punkte)

| Prüfkriterium | Bewertung |
|----------------|-----------|
| Geheimdienstzugriff auf Daten | Potenziell gegeben (Section 69 IT Act) |
| Rechtsstaatlichkeit bei Datenschutz | Teilweise (DPDPA 2023, noch nicht vollständig in Kraft) |
| Effektive Rechtsbehelfe | Eingeschränkt (kein EuGH-Äquivalent) |
| Unabhängige Aufsicht | DPBI (Data Protection Board of India) — noch nicht voll operativ |

**Ergebnis TIA:** Erhöhte Risiken; Zusatzmassnahmen erforderlich (End-to-End-Verschlüsselung, Pseudonymisierung vor Transfer).

---

## 4. Bewertung des HinSchG-Hinweises

Die anonyme HinSchG-Meldung vom 08.11.2025 thematisiert explizit den fehlenden SCC-Abschluss. Der Hinweisgeber — vermutlich ein ehemaliger DevOps-Mitarbeiter — beschreibt den Sachverhalt detailliert und zutreffend.

**Rechtliche Bewertung der VCS-Reaktion:**
- Die Meldung wurde laut interner Dokumentation als „nicht pruefrelevant" eingestuft und nicht weitergeleitet
- Versäumnis der Bearbeitung einer HinSchG-Meldung stellt eine Pflichtverletzung nach § 14 HinSchG dar
- Kein Rueckmeldefristversaeumnis nach § 17 HinSchG: Keine Rückmeldung an Hinweisgeber innerhalb von 3 Monaten

---

## 5. Ordnungswidrigkeitenrechtliche Bewertung

Der Verstoss gegen Art. 44 ff. DSGVO ist gemaess Art. 83 Abs. 5 lit. c DSGVO eine schwerwiegende Ordnungswidrigkeit (Bussgeld bis 20.000.000 EUR oder 4% des weltweiten Jahresumsatzes).

Nach dem EuGH-Urteil C-311/18 (Schrems II, 16.07.2020) und dem darauf basierenden EuGH-Urteil C-645/19 (Facebook Ireland, 15.06.2021) ist die Aufsichtsbehörde bei Kenntnis eines solchen Verstosses verpflichtet, die Übermittlung zu untersagen und Sanktionen zu verhängen.

---

## 6. Sanierungsplan Drittlandtransfer

### Sofortmassnahmen (bis 31.01.2026)

1. **Datentransfer-Stop** — Keine weiteren Datenübermittlungen an Sundara Tech bis zur SCC-Implementierung
2. **Löschung Staging-Datenbankdumps** bei Sundara Tech — nachweislich dokumentiert
3. **Verschlüsselung sämtlicher API-Calls** auf TLS 1.3 angehoben

### Mittelfristige Massnahmen (bis 28.02.2026)

4. **SCC-Abschluss** gemaess EU-Kommissionsbeschluss 2021/914 (Modul 2: Controller-to-Processor)
5. **Transfer Impact Assessment (TIA)** für Indien mit externer Expertise (RA Kanzlei Mehta & Associates, Mumbai)
6. **Pseudonymisierungsprotokoll** für ML-Trainingsdaten vor Weitergabe an Sundara Tech
7. **Update AVV** — Einbeziehung der SCC-Konformitätsanforderungen

---

## 7. Stellungnahme gegenüber LDI NRW

Im Rahmen des Aufsichtsverfahrens DSB-NW-44/26 wird VCS folgende Position einnehmen:

- Einräumen des Verstosses mit Verweis auf Sanierungsplan
- Begrenzung des Bussgelds durch Hinweis auf:
  - Freiwillige Offenlegung (Art. 83 Abs. 2 lit. e DSGVO)
  - Kooperationsbereitschaft (Art. 83 Abs. 2 lit. f DSGVO)
  - Kein vorsätzliches Handeln (Art. 83 Abs. 2 lit. b DSGVO — blosse Unkenntnis der SCC-Pflicht)
  - Umsatz des KMU (Art. 83 Abs. 2 DSGVO — wirtschaftliche Lage)

---

## Quellen

- DSGVO Art. 44, 45, 46, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EuGH C-311/18 (Schrems II), Urt. v. 16.07.2020 — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62018CJ0311)
- EU-Kommissionsbeschluss 2021/914 (SCC) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0914)
- EDSA-Empfehlung 01/2020 (Zusatzmassnahmen) — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_de)
- HinSchG §§ 14, 17 — [dejure.org/gesetze/HinSchG](https://dejure.org/gesetze/HinSchG)
