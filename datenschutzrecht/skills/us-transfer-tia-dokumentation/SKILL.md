---
name: us-transfer-tia-dokumentation
description: "US-Drittlandtransfer nach Art. 44 ff. DSGVO dokumentieren: EU-US Data Privacy Framework, DPF-Listing, Schrems I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures, Behördennachweis und Review-Kalender."
---

# US-Transfer-TIA-Dokumentation

## Zweck

Dieser Skill erstellt ein belastbares Dokumentationspaket für personenbezogene Datenübermittlungen in die USA. Er ist für Kanzleien, Datenschutzbeauftragte und Rechtsabteilungen gedacht, die gegenüber einer deutschen Aufsichtsbehörde zeigen müssen: Transfer identifiziert, Rechtsgrundlage gewählt, DPF-Listing geprüft, Alternativpfad SCC/BCR/TIA sauber dokumentiert, technische und organisatorische Maßnahmen bewertet, Wiedervorlage gesetzt.

**Wichtige Grundregel:** Safe Harbor und EU-US Privacy Shield sind keine aktuelle Transfergrundlage. Sie werden nur als historische Einordnung oder Altlastenprüfung dokumentiert. Aktuelle Pfade sind insbesondere Art. 45 DSGVO über den EU-US Data Privacy Framework-Angemessenheitsbeschluss bei teilnehmenden US-Organisationen, Art. 46 DSGVO mit Standardvertragsklauseln/BCR plus TIA oder im Ausnahmefall Art. 49 DSGVO.

## Wann verwenden?

- Ein US-SaaS-, Cloud-, KI-, Support- oder Analyseanbieter verarbeitet personenbezogene Daten.
- Ein Anbieter behauptet DPF-Zertifizierung, aber Produkt, Konzernunternehmen, HR-Daten oder Subprozessoren sind unklar.
- Eine Aufsichtsbehörde fragt nach Drittlandtransfer, Schrems-II-Prüfung oder ergänzenden Maßnahmen.
- Ein AVV, DPA, SaaS-Vertrag oder Einkaufsvorgang braucht ein dokumentiertes Transfer Impact Assessment.
- Ein Altsystem berief sich früher auf Safe Harbor oder Privacy Shield und muss bereinigt werden.

## Intake

Frage nur fehlende Punkte ab. Wenn Unterlagen vorliegen, zuerst aus den Dokumenten extrahieren.

| Punkt | Konkret abfragen oder extrahieren |
|---|---|
| Exporteur | Verantwortlicher/Auftragsverarbeiter, Sitz, zuständige Aufsichtsbehörde, Rolle im Transfer |
| Importeur | US-Rechtsträger, Adresse, Mutter-/Tochtergesellschaft, DPF-Name, Produktname |
| Daten | Kategorien personenbezogener Daten, besondere Kategorien Art. 9 DSGVO, Beschäftigtendaten, Mandantendaten |
| Zwecke | Hosting, Support, Fernwartung, Analyse, KI-Training, Ticketing, CRM, Sicherheit, Abrechnung |
| Zugriff | Speicherung USA, Remote Access, Subprozessoren, Support Level, Zugriff durch US-Personen |
| Transferpfad | DPF, SCC Modul 1-4, BCR, Art. 49, Kombination |
| Unterlagen | AVV/DPA, SCC, TOMs, Subprozessorliste, DPF-Auszug, Security Whitepaper, Datenschutzhinweise |
| Frist | Behördenfrist, Vertragsdeadline, Go-live, Incident, Audit-Termin |

## Prüf- und Arbeitsworkflow

### 1. Transferlandkarte

Erstelle zuerst eine Tabelle:

| Verarbeitung | Datenexporteur | Datenimporteur | Land | Datenarten | Zweck | Empfänger/Subprozessor | Transferinstrument | Status |
|---|---|---|---|---|---|---|---|---|

Markiere getrennt:

- Primärtransfer in die USA.
- Onward Transfers zu Subprozessoren.
- Reiner Zugriff aus den USA auf EU-gehostete Daten.
- Konzerninterne Transfers.
- Support-/Fernwartungssituationen.

### 2. DPF-Listing-Check

Prüfe und dokumentiere:

1. Exakter Name des US-Rechtsträgers in der offiziellen DPF-Liste.
2. Status aktiv/inaktiv, Zertifizierungsdatum und Re-Zertifizierungsdatum.
3. Abdeckung EU-US DPF, nicht nur Swiss-US oder UK Extension.
4. Abdeckung der relevanten Datenkategorien, insbesondere HR-Daten.
5. Abdeckung des konkreten Produkts oder Dienstes, soweit aus DPF-Eintrag, Datenschutzerklärung und Vertrag ersichtlich.
6. Beschwerdemechanismus, unabhängige Streitbeilegung und Kontaktstellen.
7. Onward-Transfer-Regeln und Subprozessoren.
8. Screenshot-/PDF-/Abrufnachweis mit Datum und Bearbeiter.

**Bewertung:**

- `DPF tragfähig`: Exakter Importeur ist aktiv gelistet und der konkrete Transfer ist abgedeckt.
- `DPF nur teilweise tragfähig`: Konzernmutter gelistet, Produkt/Tochter/HR-Daten/Subprozessoren unklar.
- `DPF nicht tragfähig`: Kein aktiver Eintrag oder Transfer außerhalb der Abdeckung.

### 3. Schrems-Historie sauber einordnen

Für die Akte:

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EU-US Data Privacy Framework: aktueller Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023; nutzbar nur für teilnehmende US-Organisationen im sachlichen Umfang der Zertifizierung.

Formuliere nie, dass Safe Harbor oder Privacy Shield heute eine gültige Rechtsgrundlage seien.

### 4. Alternativpfad SCC/BCR/TIA

Wenn DPF nicht eindeutig trägt, prüfe:

- SCC Modul 1: Verantwortlicher an Verantwortlichen.
- SCC Modul 2: Verantwortlicher an Auftragsverarbeiter.
- SCC Modul 3: Auftragsverarbeiter an Auftragsverarbeiter.
- SCC Modul 4: Auftragsverarbeiter an Verantwortlichen.
- BCR, wenn konzerninterne genehmigte Regeln nachweislich passen.
- Art. 49 DSGVO nur eng und ausnahmsweise; nicht als Dauerlösung.

Verweise für die konkrete SCC-Ausarbeitung auf `standardvertragsklauseln-scc-paket`.

### 5. Transfer Impact Assessment

Dokumentiere entlang dieser Struktur:

| Kapitel | Inhalt |
|---|---|
| A. Transferbeschreibung | Wer übermittelt was, wohin, zu welchem Zweck, wie oft und über welche Infrastruktur? |
| B. Transferinstrument | DPF, SCC/BCR oder Ausnahme; Begründung und Nachweise |
| C. Drittlandsrecht und Praxis | Relevante Zugriffsbefugnisse, Importeurangaben, Transparenzberichte, Warrant-Canary/Policy, tatsächliche Zugriffserfahrung |
| D. Risiko für Betroffene | Datenart, Sensibilität, Menge, Identifizierbarkeit, Schutzbedarf, mögliche Schäden |
| E. Ergänzende Maßnahmen | Verschlüsselung, Key Management in EU/EWR, Pseudonymisierung, Zugriffsbeschränkung, Logging, Challenge Policy, Transparenz |
| F. Restrestrisiko | Ampel, Begründung, offene Punkte, Entscheidungsträger |
| G. Wiedervorlage | Trigger: Zertifizierungsablauf, neue Subprozessoren, Produktänderung, Behördenpraxis, EuGH/EDSA-Update |

### 6. Ergebnislogik

Gib immer ein klares Ergebnis aus:

- **Freigabe möglich:** Transferinstrument trägt, Dokumente vollständig, Restrestrisiko vertretbar.
- **Freigabe mit Auflagen:** Nachbesserungen nötig, z. B. SCC-Anlagen, Key Management, Subprozessor-Auskunft, DPF-Nachweis.
- **Stop bis Klärung:** Importeur nicht identifizierbar, DPF nicht tragfähig, keine SCC, hohes ungemindertes Risiko.
- **Legacy-Bereinigung:** Alte Safe-Harbor-/Privacy-Shield-Dokumentation ablösen, neue Grundlage festlegen.

## Output-Paket

Erzeuge auf Wunsch ein zusammenhängendes Paket:

1. **Kurzvermerk für Geschäftsführung oder Mandant** mit Entscheidung und Restfragen.
2. **Transferregister-Auszug** nach Verarbeitungstätigkeit.
3. **DPF-Prüfvermerk** mit Abrufdatum, Treffer, Scope und Lücken.
4. **TIA-Vollvermerk** mit Maßnahmenmatrix.
5. **SCC/BCR-Verweisblatt** mit Modulwahl und Anlagenstatus.
6. **TOM- und Supplementary-Measures-Anlage**.
7. **Antwortbaustein für Aufsichtsbehörde**.
8. **Wiedervorlage- und Monitoringplan**.

## Qualitätsregeln

- Keine erfundenen DPF-Listungen. Wenn nicht live geprüft, Ausgabe als `nicht verifiziert` kennzeichnen.
- Keine pauschale Aussage "USA immer unzulässig" oder "DPF immer ausreichend".
- Keine SCC umschreiben. Die offiziellen Klauseln unverändert verwenden; nur Modulwahl, Anlagen und Dokumentation vorbereiten.
- Beschäftigtendaten und Mandats-/Berufsgeheimnisdaten gesondert markieren.
- Bei KI-Diensten zusätzlich `mandantendaten-ki`, `ki-verordnung-compliance` oder `ki-vo-ai-act-pruefer` vorschlagen.

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 44-49.
- EU-Kommission: EU-US Data Privacy Framework, Angemessenheitsbeschluss vom 10.07.2023.
- Offizielle DPF-Liste: Data Privacy Framework Program, Participant Search.
- EU-Kommission: Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914.
- EDSA: Recommendations 01/2020 zu ergänzenden Maßnahmen, Final Version 18.06.2021.
