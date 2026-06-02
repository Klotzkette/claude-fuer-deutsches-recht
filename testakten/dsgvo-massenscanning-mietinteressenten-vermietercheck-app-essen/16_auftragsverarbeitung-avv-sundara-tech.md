# 16 — Auftragsverarbeitung: AVV Sundara Tech Pvt. Ltd.

**Aktenzeichen:** DSB-NW-44/26 (verbunden)
**Bearbeiter:** RA Lars Drosselberg, RAin Miriam Beckenbauer
**Datum:** 29. Januar 2026
**Betreff:** Analyse des AVV mit Sundara Tech und Sanierungsplan Auftragsverarbeitungsrecht

---

## 1. Rechtsrahmen Auftragsverarbeitung

### 1.1 Art. 28 DSGVO — Auftragsverarbeiter

Art. 28 Abs. 1 DSGVO: Wenn eine Verarbeitung im Auftrag eines Verantwortlichen erfolgt, arbeitet dieser nur mit Auftragsverarbeitern, die hinreichende Garantien dafür bieten, dass geeignete technische und organisatorische Massnahmen so durchgeführt werden, dass die Verarbeitung im Einklang mit den Anforderungen dieser Verordnung erfolgt.

Art. 28 Abs. 3 DSGVO: Die Verarbeitung durch einen Auftragsverarbeiter erfolgt auf der Grundlage eines Vertrags oder eines anderen Rechtsinstruments, der oder das den Auftragsverarbeiter in Bezug auf den Verantwortlichen bindet.

**Pflichtinhalte des AVV (Art. 28 Abs. 3 lit. a–h DSGVO):**
- Bindung an Weisungen des Verantwortlichen
- Vertraulichkeitspflichten
- Geeignete technische und organisatorische Massnahmen (Art. 32 DSGVO)
- Regelung über Unterauftragsverarbeiter
- Unterstützung bei Betroffenenrechten
- Löschung oder Rückgabe nach Auftragsende
- Auskunfts- und Kontrollrechte
- Nachweis der Konformitaet

---

## 2. Analyse des bestehenden AVV mit Sundara Tech

### 2.1 Zeitlinie des AVV-Abschlusses

| Datum | Ereignis |
|-------|---------|
| Okt 2022 | Beginn Datentransfer an Sundara Tech — **kein AVV** |
| Dez 2023 | Abschluss eines AVV (nachträglich, auf Initiative von DSB Kessler-Brandt) |
| Jan 2026 | Analyse AVV durch RA Drosselberg |

**Ergebnis:** Für den Zeitraum Oktober 2022 bis Dezember 2023 (14 Monate) erfolgte die Verarbeitung durch Sundara Tech ohne AVV — klarer Verstoss gegen Art. 28 Abs. 3 DSGVO.

### 2.2 Maeengel des AVV (Dezember 2023)

Gemaess Analyse des AVV-Dokuments (Zugang erhalten 15.01.2026) bestehen folgende Mängel:

| AVV-Klausel | Mängel | Bewertung |
|-------------|---------|-----------|
| Art. 28 Abs. 3 lit. a (Weisungsbindung) | Nur allgemeine Weisungsbindung; keine Konkretisierung für Produktionsdaten | Unzureichend |
| Art. 28 Abs. 3 lit. b (Vertraulichkeit) | Vertraulichkeitspflicht vorhanden; aber kein Beendigungsprotokoll | Teiweise |
| Art. 28 Abs. 3 lit. c (TOM Art. 32) | Verweis auf ISO 27001, aber Sundara Tech nicht zertifiziert | Unzureichend |
| Art. 28 Abs. 3 lit. d (Unterauftragsverarbeiter) | Klausel fehlt — Sundara Tech nutzt AWS Mumbai (Drittland!) | Fehlt |
| Art. 28 Abs. 3 lit. e (Betroffenenrechte) | Kooperationspflicht vorhanden | Ausreichend |
| Art. 28 Abs. 3 lit. f (Löschung) | Kein Loeschungsprotokoll; Fristen unklar | Unzureichend |
| Art. 28 Abs. 3 lit. g (Nachweise) | Auditrecht vorhanden, aber nie ausgeübt | Formal ausreichend |
| Drittlandtransfer (Art. 46 DSGVO) | **SCC fehlt vollständig** | Fehlt vollständig |

**Gesamtergebnis:** Der AVV ist in sechs von acht relevanten Bereichen unzureichend oder fehlerhaft. Ein vollständig sanierter AVV mit SCC ist zu erstellen.

---

## 3. Sanierungsplan AVV

### 3.1 Neuabschluss eines konformen AVV

Es wird empfohlen, den bestehenden AVV vollständig zu ersetzen durch:

**Neuer AVV Sundara Tech v2.0 (Zieldokument):**
1. Präzise Weisungsbindung für jeden Verarbeitungsschritt (ML-Training, Support-Zugriff, Entwicklung)
2. Vollständige Vertraulichkeitsverpflichtungen inklusive Beendigungsprotokoll
3. TOM-Anlage: Spezifische Sicherheitsanforderungen für Produktionsdaten (End-to-End-Verschlüsselung, Zugangsbeschränkung, Logging)
4. Unterauftragsverarbeiter-Regelung: Sundara Tech nutzt AWS Mumbai — eigene Unterauftragsverarbeitervertrag mit AWS India erforderlich
5. Betroffenenrechte-Prozess: Klarer Workflow für Weiterleitung von Auskunftsersuchen und Loeschungsantraegen
6. Loeschungsprotokoll: Definierte Fristen und Nachweispflichten

**Drittlandabsicherung:**
7. SCC (Modul 2: Controller-to-Processor) gemaess EU-Kommissionsbeschluss 2021/914
8. Transfer Impact Assessment (TIA) Indien
9. Zusatzmassnahmen: Pseudonymisierung aller Trainings-Datensätze vor Transfer

### 3.2 Zeitplan

| Massnahme | Verantwortlich | Frist |
|-----------|---------------|-------|
| Entwurf AVV v2.0 | RA Drosselberg | 10.02.2026 |
| Abstimmung mit Sundara Tech | VCS Rechtsabteilung | 20.02.2026 |
| TIA Indien | extern: RA Mehta & Associates | 28.02.2026 |
| Unterzeichnung AVV v2.0 + SCC | GF VCS + Sundara Tech CEO | 05.03.2026 |
| Loeschungsbestaetigung alte Daten | Sundara Tech | 10.03.2026 |

---

## 4. Haftung für Zeitraum ohne AVV (Okt 2022–Dez 2023)

### 4.1 Haftung VCS gegenüber Betroffenen

Für den Zeitraum ohne AVV haftet VCS als Verantwortlicher vollständig für alle Schäden, die durch die Verarbeitung bei Sundara Tech entstanden sind. Art. 82 Abs. 2 DSGVO sieht eine verschuldensunabhaengige Haftung vor; VCS kann sich nur durch Nachweis entlasten, dass sie in keinerlei Hinsicht für den Schaden verantwortlich sind (Art. 82 Abs. 3 DSGVO) — was angesichts des fehlenden AVV nicht möglich ist.

### 4.2 Regress gegen Sundara Tech

In dem Zeitraum ohne AVV ist Sundara Tech möglicherweise als eigenverantwortlicher Verantwortlicher einzustufen (kein AVV = kein Weisungsverhältnis). Gesamtschuldnerische Haftung VCS + Sundara Tech gemaess Art. 82 Abs. 4 DSGVO ist möglich. Der Regressanspruch VCS gegen Sundara Tech (Art. 82 Abs. 5 DSGVO) muss vertraglich gesichert werden.

**Massnahme:** Einbeziehung von Regressklausel in AVV v2.0 für den historischen Zeitraum.

---

## 5. Unterauftragsverarbeiter-Kette: AWS Mumbai

### 5.1 Problem

Sundara Tech betreibt seine Entwicklungsinfrastruktur auf AWS Mumbai (ap-south-1 Region). Damit ergibt sich eine weitere Drittlandsuebermittlung (Indien → AWS in Indien — kein EU-Bezug). Da AWS Inc. ein US-Unternehmen ist, könnte auch US-Recht (CLOUD Act) relevant werden.

### 5.2 Lösungsansatz

1. AWS Mumbai als Unterauftragsverarbeiter in den AVV aufnehmen
2. Pruefung: AWS Datenverarbeitungsnachtrag (AWS DPA) + AWS SCC — AWS stellt diese standardmaessig bereit
3. Sicherstellung: Keine Speicherung der Produktionsdaten ausserhalb der EU/EWR ohne explizite Genehmigung

---

## Quellen

- DSGVO Art. 28, 32, 44, 46, 82 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EU-Kommissionsbeschluss 2021/914 (SCC Modul 2) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0914)
- EDSA-Leitlinien 07/2020 (Auftragsverarbeiter) — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-072020-concepts-controller-and-processor-gdpr_de)
- US CLOUD Act — [congress.gov](https://www.congress.gov/bill/115th-congress/senate-bill/2383/text)
- OLG Duesseldorf, Urt. v. 22.03.2022 — I-15 U 2/21 (Auftragsverarbeitungsvertrag) — [openjur.de](https://openjur.de)
