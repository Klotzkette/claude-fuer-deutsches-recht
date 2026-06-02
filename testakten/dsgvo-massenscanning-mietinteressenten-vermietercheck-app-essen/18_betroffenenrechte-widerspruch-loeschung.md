# 18 — Betroffenenrechte: Widerspruch und Löschung

**Aktenzeichen:** DSB-NW-44/26 / 18 Mass 4/26
**Bearbeiter:** RAin Miriam Beckenbauer
**Datum:** 31. Januar 2026
**Betreff:** Systematische Bearbeitung von Widerspruchs- und Loeschungsantraegen

---

## 1. Betroffenenrechte im Überblick

Die DSGVO gewährt betroffenen Personen ein umfassendes Rechtssystem gegenüber Verantwortlichen:

| Recht | Artikel | Status bei VCS |
|-------|---------|----------------|
| Auskunftsrecht | Art. 15 | Nicht implementiert (s. Akten 12, 13) |
| Berichtigungsrecht | Art. 16 | Nicht implementiert |
| Löschrecht (Recht auf Vergessenwerden) | Art. 17 | Nicht implementiert |
| Einschränkung der Verarbeitung | Art. 18 | Nicht implementiert |
| Datenübertragbarkeit | Art. 20 | Nicht implementiert |
| Widerspruchsrecht | Art. 21 | Nicht implementiert |
| Widerruf der Einwilligung | Art. 7 Abs. 3 | Nicht implementiert |

Alle sieben Betroffenenrechte sind bei VCS technisch und organisatorisch nicht implementiert — ein schwerwiegendes Compliance-Defizit.

---

## 2. Widerspruchsrecht Art. 21 DSGVO

### 2.1 Widerspruchsrecht bei berechtigtem Interesse (Art. 21 Abs. 1 DSGVO)

Hat VCS sich auf Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse) als Verarbeitungsgrundlage berufen, haben betroffene Personen das Recht, aus Gründen, die sich aus ihrer besonderen Situation ergeben, jederzeit Widerspruch gegen diese Verarbeitung einzulegen.

**Rechtsfolge:** VCS muss nach Widerspruch die Verarbeitung einstellen, es sei denn, VCS kann zwingende schutzwürdige Gründe nachweisen, die die Interessen der betroffenen Person überwiegen.

**Praktische Situation:** Da Art. 6 Abs. 1 lit. f DSGVO als Grundlage bereits als unzureichend bewertet wurde (s. Akte 03), wäre ein Widerspruch ohnehin zurueckzuweisen — die Verarbeitung darf aus diesem Grunde gar nicht erfolgen.

### 2.2 Widerspruchsrecht bei Profiling (Art. 21 Abs. 2 DSGVO)

Werden personenbezogene Daten verarbeitet, um Direktwerbung zu betreiben oder Profiling für Direktwerbung durchzuführen, so hat die betroffene Person das Recht, jederzeit Widerspruch einzulegen. Nach Widerspruch duermen die Daten für diese Zwecke nicht mehr verarbeitet werden.

**Anwendbarkeit:** Profiling durch ProspectScore Pro dient nicht der Direktwerbung, sondern der Mietinteressentenbeurteilung. Art. 21 Abs. 2 DSGVO nicht einschlägig. Anwendbar ist Art. 21 Abs. 1 DSGVO.

---

## 3. Löschrecht Art. 17 DSGVO

### 3.1 Löschgründe

| Löschgrund | Art. 17 Abs. 1 | Anwendbar bei VCS |
|-------------|----------------|-------------------|
| Daten nicht mehr notwendig | lit. a | Nach Abschluss Bewerbung (wenn Vermieter Entscheidung getroffen hat) — Ja |
| Widerruf der Einwilligung | lit. b | Ja — wenn Einwilligung als Grundlage |
| Widerspruch Art. 21 Abs. 1 | lit. c | Ja |
| Rechtswidrige Verarbeitung | lit. d | Ja — nach Feststellung des Art. 6-Verstosses |
| Rechtspflicht | lit. e | Ggf. bei gesetzl. Löschpflicht |

**Ergebnis:** Gemaess Art. 17 Abs. 1 lit. d DSGVO sind sämtliche unrechtmaessig verarbeiteten Daten zu löschen. Da die Verarbeitung ohne wirksame Rechtsgrundlage erfolgte, trifft VCS eine umfassende Löschpflicht.

### 3.2 Ausnahmen vom Löschrecht (Art. 17 Abs. 3 DSGVO)

Löschung ist nicht verpflichtend, soweit die Verarbeitung erforderlich ist:
- zur Ausübung des Rechts auf freie Meinungsaesserung und Information (lit. a) — nicht einschlägig
- zur Erfüllung einer rechtlichen Verpflichtung (lit. b) — möglich für Aufbewahrungsfristen
- aus Gründen des öffentlichen Interesses (lit. c–d) — nicht einschlägig
- für die Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen (lit. e) — einschlägig für Verfahrenssicherung (Beweiszwecke im laufenden Verfahren)

**Konsequenz:** Im Rahmen der laufenden Verfahren (LDI NRW, VDuG, LG Essen, StA Essen) ist eine vollständige Löschung bis zum Verfahrensabschluss nicht möglich (Art. 17 Abs. 3 lit. e DSGVO — Rechtsansprüche). Die Daten sind jedoch einzuschränken (Art. 18 DSGVO) — nur für Verfahrensverteidigung zugreifbar.

---

## 4. Datenübertragbarkeit Art. 20 DSGVO

Art. 20 DSGVO gewährt betroffenen Personen das Recht, die sie betreffenden personenbezogenen Daten in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten, wenn:
- die Verarbeitung auf Einwilligung (Art. 6 Abs. 1 lit. a) oder Vertrag (Art. 6 Abs. 1 lit. b) beruht, und
- die Verarbeitung mithilfe automatisierter Verfahren erfolgt.

**Anwendbarkeit für VCS:** Da die Einwilligung als unwirksam eingestuft wurde, ist Art. 20 DSGVO einschlägig — aber die Verarbeitungsgrundlage war unwirksam. Ob Art. 20 DSGVO bei von Anfang an unwirksamer Einwilligung greift, ist rechtlich umstritten. Im Zweifel ist das Portabilitaetsrecht zu gewähren.

---

## 5. Implementierungsplan Betroffenenrechte

### 5.1 Technische Implementierung (Zieldatum 28.02.2026)

**Online-Portal „Meine Daten" auf vermietercheck.de:**
- Anmeldung per E-Mail-Verifizierung
- Auskunft: Anzeige aller gespeicherten Daten (ProspectScore, Datenkategorien, Empfänger) — JSON-Export
- Widerspruch: One-Click-Widerspruchsformular mit Eingangsbestätigung
- Löschung: Antrag mit 30-Tage-Bearbeitung und Nachweisprotokoll
- Datenportabilität: Export als JSON/CSV nach Art. 20 DSGVO
- Widerruf Einwilligung: Dedizierter Button

### 5.2 Prozessimplementierung

- SLA: 1-Monat-Frist Art. 12 Abs. 3 DSGVO für Auskunft, Berichtigung, Löschung
- Verlängerungsprozess: Automatische E-Mail an Betroffenen bei Fristverlängerung
- Ablehnung: Schriftliche Begründung mit Hinweis auf Beschwerderecht LDI NRW

---

## 6. Massenbearbeitung (VDuG-Kontext)

Im Rahmen des VDuG-Verfahrens (LG Essen 18 Mass 4/26) ist zu erwarten, dass 8.200 Kläger Loeschungsantraege stellen. Die technische Kapazität für die Massenbearbeitung ist sicherzustellen:
- Batch-Löschfunktionalität in der Datenbank implementieren
- Löschdokumentation für jede betroffene Person (Zertifikat mit Datum und Datenreferenz)
- Kapazität: mindestens 500 Anträge/Woche bearbeitbar

---

## Quellen

- DSGVO Art. 7, 12, 15, 16, 17, 18, 20, 21 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EDSA-Leitlinien 05/2019 (Datenuebertragbarkeit) — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052019-right-data-portability_de)
- EuGH C-307/22 (Kopienrecht Art. 15 Abs. 3 DSGVO) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0307)
- LG Frankfurt, Beschl. v. 18.09.2020 — 2-13 O 131/20 (Widerspruchsrecht Scoring) — [openjur.de](https://openjur.de)
