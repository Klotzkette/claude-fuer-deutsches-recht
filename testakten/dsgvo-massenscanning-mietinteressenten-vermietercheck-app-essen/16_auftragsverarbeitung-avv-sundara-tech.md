# 16 — Auftragsverarbeitung: AVV Sundara Tech Pvt. Ltd.

**Aktenzeichen:** DSB-NW-44/26 (verbunden)
**Bearbeiter:** RA Lars Drosselberg, RAin Miriam Beckenbauer
**Datum:** 29. Januar 2026
**Betreff:** Analyse des AVV mit Sundara Tech und Sanierungsplan Auftragsverarbeitungsrecht

---

## 1. Rechtsrahmen Auftragsverarbeitung

### 1.1 Art. 28 DSGVO — Auftragsverarbeiter

Art. 28 Abs. 1 DSGVO: Wenn eine Verarbeitung im Auftrag eines Verantwortlichen erfolgt, arbeitet dieser nur mit Auftragsverarbeitern, die hinreichende Garantien dafuer bieten, dass geeignete technische und organisatorische Massnahmen so durchgefuehrt werden, dass die Verarbeitung im Einklang mit den Anforderungen dieser Verordnung erfolgt.

Art. 28 Abs. 3 DSGVO: Die Verarbeitung durch einen Auftragsverarbeiter erfolgt auf der Grundlage eines Vertrags oder eines anderen Rechtsinstruments, der oder das den Auftragsverarbeiter in Bezug auf den Verantwortlichen bindet.

**Pflichtinhalte des AVV (Art. 28 Abs. 3 lit. a–h DSGVO):**
- Bindung an Weisungen des Verantwortlichen
- Vertraulichkeitspflichten
- Geeignete technische und organisatorische Massnahmen (Art. 32 DSGVO)
- Regelung ueber Unterauftragsverarbeiter
- Unterstuetzung bei Betroffenenrechten
- Loeschung oder Rueckgabe nach Auftragsende
- Auskunfts- und Kontrollrechte
- Nachweis der Konformitaet

---

## 2. Analyse des bestehenden AVV mit Sundara Tech

### 2.1 Zeitlinie des AVV-Abschlusses

| Datum | Ereignis |
|-------|---------|
| Okt 2022 | Beginn Datentransfer an Sundara Tech — **kein AVV** |
| Dez 2023 | Abschluss eines AVV (nachtraeglich, auf Initiative von DSB Kessler-Brandt) |
| Jan 2026 | Analyse AVV durch RA Drosselberg |

**Ergebnis:** Fuer den Zeitraum Oktober 2022 bis Dezember 2023 (14 Monate) erfolgte die Verarbeitung durch Sundara Tech ohne AVV — klarer Verstoss gegen Art. 28 Abs. 3 DSGVO.

### 2.2 Maeengel des AVV (Dezember 2023)

Gemaess Analyse des AVV-Dokuments (Zugang erhalten 15.01.2026) bestehen folgende Maengel:

| AVV-Klausel | Maengel | Bewertung |
|-------------|---------|-----------|
| Art. 28 Abs. 3 lit. a (Weisungsbindung) | Nur allgemeine Weisungsbindung; keine Konkretisierung fuer Produktionsdaten | Unzureichend |
| Art. 28 Abs. 3 lit. b (Vertraulichkeit) | Vertraulichkeitspflicht vorhanden; aber kein Beendigungsprotokoll | Teiweise |
| Art. 28 Abs. 3 lit. c (TOM Art. 32) | Verweis auf ISO 27001, aber Sundara Tech nicht zertifiziert | Unzureichend |
| Art. 28 Abs. 3 lit. d (Unterauftragsverarbeiter) | Klausel fehlt — Sundara Tech nutzt AWS Mumbai (Drittland!) | Fehlt |
| Art. 28 Abs. 3 lit. e (Betroffenenrechte) | Kooperationspflicht vorhanden | Ausreichend |
| Art. 28 Abs. 3 lit. f (Loeschung) | Kein Loeschungsprotokoll; Fristen unklar | Unzureichend |
| Art. 28 Abs. 3 lit. g (Nachweise) | Auditrecht vorhanden, aber nie ausgeuebt | Formal ausreichend |
| Drittlandtransfer (Art. 46 DSGVO) | **SCC fehlt vollstaendig** | Fehlt vollstaendig |

**Gesamtergebnis:** Der AVV ist in sechs von acht relevanten Bereichen unzureichend oder fehlerhaft. Ein vollstaendig sanierter AVV mit SCC ist zu erstellen.

---

## 3. Sanierungsplan AVV

### 3.1 Neuabschluss eines konformen AVV

Es wird empfohlen, den bestehenden AVV vollstaendig zu ersetzen durch:

**Neuer AVV Sundara Tech v2.0 (Zieldokument):**
1. Praezise Weisungsbindung fuer jeden Verarbeitungsschritt (ML-Training, Support-Zugriff, Entwicklung)
2. Vollstaendige Vertraulichkeitsverpflichtungen inklusive Beendigungsprotokoll
3. TOM-Anlage: Spezifische Sicherheitsanforderungen fuer Produktionsdaten (End-to-End-Verschluesselung, Zugangsbeschraenkung, Logging)
4. Unterauftragsverarbeiter-Regelung: Sundara Tech nutzt AWS Mumbai — eigene Unterauftragsverarbeitervertrag mit AWS India erforderlich
5. Betroffenenrechte-Prozess: Klarer Workflow fuer Weiterleitung von Auskunftsersuchen und Loeschungsantraegen
6. Loeschungsprotokoll: Definierte Fristen und Nachweispflichten

**Drittlandabsicherung:**
7. SCC (Modul 2: Controller-to-Processor) gemaess EU-Kommissionsbeschluss 2021/914
8. Transfer Impact Assessment (TIA) Indien
9. Zusatzmassnahmen: Pseudonymisierung aller Trainings-Datensaetze vor Transfer

### 3.2 Zeitplan

| Massnahme | Verantwortlich | Frist |
|-----------|---------------|-------|
| Entwurf AVV v2.0 | RA Drosselberg | 10.02.2026 |
| Abstimmung mit Sundara Tech | VCS Rechtsabteilung | 20.02.2026 |
| TIA Indien | extern: RA Mehta & Associates | 28.02.2026 |
| Unterzeichnung AVV v2.0 + SCC | GF VCS + Sundara Tech CEO | 05.03.2026 |
| Loeschungsbestaetigung alte Daten | Sundara Tech | 10.03.2026 |

---

## 4. Haftung fuer Zeitraum ohne AVV (Okt 2022–Dez 2023)

### 4.1 Haftung VCS gegenueber Betroffenen

Fuer den Zeitraum ohne AVV haftet VCS als Verantwortlicher vollstaendig fuer alle Schaeden, die durch die Verarbeitung bei Sundara Tech entstanden sind. Art. 82 Abs. 2 DSGVO sieht eine verschuldensunabhaengige Haftung vor; VCS kann sich nur durch Nachweis entlasten, dass sie in keinerlei Hinsicht fuer den Schaden verantwortlich sind (Art. 82 Abs. 3 DSGVO) — was angesichts des fehlenden AVV nicht moeglich ist.

### 4.2 Regress gegen Sundara Tech

In dem Zeitraum ohne AVV ist Sundara Tech moeglicherweise als eigenverantwortlicher Verantwortlicher einzustufen (kein AVV = kein Weisungsverhaeltnis). Gesamtschuldnerische Haftung VCS + Sundara Tech gemaess Art. 82 Abs. 4 DSGVO ist moeglich. Der Regressanspruch VCS gegen Sundara Tech (Art. 82 Abs. 5 DSGVO) muss vertraglich gesichert werden.

**Massnahme:** Einbeziehung von Regressklausel in AVV v2.0 fuer den historischen Zeitraum.

---

## 5. Unterauftragsverarbeiter-Kette: AWS Mumbai

### 5.1 Problem

Sundara Tech betreibt seine Entwicklungsinfrastruktur auf AWS Mumbai (ap-south-1 Region). Damit ergibt sich eine weitere Drittlandsuebermittlung (Indien → AWS in Indien — kein EU-Bezug). Da AWS Inc. ein US-Unternehmen ist, koennte auch US-Recht (CLOUD Act) relevant werden.

### 5.2 Loesungsansatz

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
