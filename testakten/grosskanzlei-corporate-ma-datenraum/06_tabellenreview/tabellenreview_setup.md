# Tabellenreview-Setup — Projekt Silberfalke

**Aktenzeichen:** MWK/2024/SIL-001  
**Dokument-Nr.:** TABREV-SETUP-001/SIL  
**Datum:** 28. November 2024  
**Verfasserin:** Katharina Pfeiffer, Senior Associate  
**Adressat:** DD-Team / Associate Tim Berger  
**Betreff:** Setup und Arbeitsanleitung Vertragsreview-Tabelle (Commercial Workstream)

---

## 1. Zweck

Dieser Vermerk beschreibt das Vorgehen für den strukturierten Tabellenreview der kommerziellen Vertragsunterlagen im Datenraum des Projekts Silberfalke. Ziel ist es, alle wesentlichen Vertragsparameter der Top-20-Verträge auf einer einheitlichen Tabelle (review_grid.csv / Excel-Workbook) zu erfassen, um:
- eine schnelle Risikoübersicht für ECP zu ermöglichen,
- SPA-Implikationen (Garantien, Freistellungen) vorzubereiten,
- Grundlage für die Commercial Due Diligence von McKinsey zu liefern.

---

## 2. Umfang der zu prüfenden Verträge

### 2.1 Priorisierungskriterien

In die Tabelle werden alle Verträge aufgenommen, die mindestens eines der folgenden Kriterien erfüllen:
- Jahresumsatz ≥ EUR 2 Mio.
- Laufzeit länger als 18 Monate nach geplantem Closing (31. März 2025)
- Explizite Change-of-Control-Klausel, Exklusivität oder Liability-Cap-Klausel
- Teil des Carve-out-Perimeters (TSA, IP-Lizenz, konzerninterner Vertrag)

### 2.2 Vertragsumfang

Für diese DD werden geprüft:
- **Kundenverträge:** Top-12 nach Umsatz (C-001 bis C-012 — bereits in commercial_contracts_sample.csv)
- **Lieferantenverträge:** Top-5 nach Kritikalität (Halbleiter, Elektromotoren, Logistik)
- **TSA-Entwürfe:** IT, HR, Treasury, Versicherung (4 Entwürfe)
- **IP-Lizenzverträge:** IP-Lizenzrahmenvertrag Holding → Target (1 Entwurf)
- **Konzernumlage:** Kostentragungsvertrag (1 laufender Vertrag)

Gesamt: ca. **24 Verträge** im ersten Review-Durchgang.

---

## 3. Tabellenspalten und Kategorien

### Blatt 1: Legal Review (Hauptblatt)

| Spalten-ID | Bezeichnung | Erläuterung |
|---|---|---|
| A | doc_id | Interne Dokumenten-ID (z. B. C-001) |
| B | partner | Vertragspartner (anonymisiert Kunde A etc.) |
| C | typ | Vertragstyp (Liefer-, Rahmen-, Entwicklungs-, Servicevertrag) |
| D | laufzeit_bis | Vertragsende |
| E | change_of_control | ja / nein / bedingt |
| F | coc_kuendigung_frist | Kündigungsfrist nach CoC (Tage) |
| G | termination_ordinary | Ordentliche Kündigungsfrist |
| H | exclusivity | ja / nein / beschränkt |
| I | liability_cap | Haftungsobergrenze (EUR oder Beschreibung) |
| J | assignment | Abtretbarkeit: ja / nein / mit Zustimmung |
| K | governing_law | Anwendbares Recht |
| L | risiko | Gering / Mittel / Hoch |
| M | beleg | Vertrags-Section als Nachweis |
| N | spa_massnahme | Empfohlene SPA-Klausel / Freistellung |
| O | kommentar | Sonstiges |

### Blatt 2: Tax Review

| Spalten-ID | Bezeichnung | Erläuterung |
|---|---|---|
| A | doc_id | Dokumenten-ID |
| B | partner | Vertragspartner |
| C | verrechnungspreis | Ja / Nein / Arm's Length |
| D | quellsteuer_risiko | Quellensteuerrisiko (Land) |
| E | umsatzsteuer | Steuerpflicht / Befreiung / Organschaft-Relevanz |
| F | bemerkung_tax | Freitext |

### Blatt 3: Commercial Review (Übergabe an McKinsey)

| Spalten-ID | Bezeichnung | Erläuterung |
|---|---|---|
| A | doc_id | Dokumenten-ID |
| B | umsatz_pa | Jahresumsatz EUR |
| C | marge_indikativ | Indikative Marge (aus CR-003) |
| D | restlaufzeit | Monate bis Vertragsende |
| E | kuendigungsrisiko_post_closing | Ja / Nein / Bedingt |
| F | retention_massnahme | Retentionsmaßnahme vor Closing empfohlen? |

### Blatt 4: PMI-Relevanz

| Spalten-ID | Bezeichnung | Erläuterung |
|---|---|---|
| A | doc_id | Dokumenten-ID |
| B | tsa_erforderlich | Ist TSA erforderlich? Ja / Nein |
| C | system_migration | IT-Systemwechsel notwendig? |
| D | personal_uebergang | § 613a BGB Übergang? |
| E | pmi_prioritaet | Hoch / Mittel / Niedrig |

---

## 4. Arbeitsablauf

1. **Zuweisung:** Tim Berger erhält die Primärarbeit an den Kundenverträgen; Katharina Pfeiffer übernimmt TSA-Entwürfe und Konzernverträge. Für steuerliche Spalten (Blatt 2) liefert Dr. Sabine Roth Input.
2. **Quellen:** VDR-Dokumente (Intralinks), identifiziert über vdr_index.csv. Bei Unklarheiten: Q&A-Frage stellen (qa_register.csv).
3. **Befüllung:** Einheitlich in review_grid.csv (Primär) und parallel im XLSX-Workbook (06_tabellenreview/review_grid.xlsx).
4. **Qualitätssicherung:** Jeder Eintrag wird von der Gegenseite gegengelesen. Red-Flag-Felder (Risikoampel HOCH) werden direkt per E-Mail an Dr. Weidemann gemeldet.
5. **Deadline:** Erster vollständiger Entwurf bis **6. Dezember 2024**, finaler Stand bis **12. Dezember 2024**.

---

## 5. Hinweise zur Interpretation

- **Change-of-Control "bedingt":** Bedeutet, dass die Klausel nur bei Überschreiten eines Schwellenwerts (> 25 % oder > 50 %) greift. Formulierung im Vertrag ist entscheidend.
- **Liability Cap "uncapped":** Bedeutet, dass keine vertragliche Haftungsbegrenzung vereinbart wurde. Dies ist aus Käufersicht besonders risikoreich, da der Verkäufer im SPA-Garantieregime diese Risiken vollständig übernehmen muss.
- **Assignment:** Vertragsübertragungs- und Abtretungsklauseln sind bei Share Deals theoretisch nicht direkt ausgelöst (die Gesellschaft bleibt Vertragspartner); trotzdem können Zustimmungsklauseln formuliert sein, die auf den Anteilserwerb abstellen.

---

*Alle in diesem Vermerk genannten Personen, Unternehmen, Zahlen und Aktenzeichen sind frei erfunden und dienen ausschließlich Schulungszwecken.*
