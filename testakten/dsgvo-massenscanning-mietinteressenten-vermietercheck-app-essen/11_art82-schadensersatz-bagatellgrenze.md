# 11 — Art. 82 DSGVO: Schadensersatz und Bagatellgrenze

**Aktenzeichen:** LG Essen 18 Mass 4/26
**Bearbeiter:** RA Dr. Cornelius Specht
**Datum:** 24. Januar 2026
**Betreff:** Analyse der Schadensersatzpflicht Art. 82 DSGVO und Bagatellgrenzen-Argumentation

---

## 1. Tatbestand Art. 82 DSGVO

Art. 82 Abs. 1 DSGVO: Jede Person, der wegen eines Verstosses gegen diese Verordnung ein materieller oder immaterieller Schaden entstanden ist, hat Anspruch auf Schadenersatz gegen den Verantwortlichen oder gegen den Auftragsverarbeiter.

Art. 82 Abs. 2 DSGVO: Verantwortliche haften für sämtliche Schäden aus DSGVO-Verstoessen, sofern sie nicht nachweisen, dass sie in keiner Weise für den Umstand, durch den der Schaden eingetreten ist, verantwortlich sind.

---

## 2. Höherentwicklung der EuGH-Rechtsprechung

### 2.1 EuGH C-300/21 (Österreichische Post, 04.05.2023)

**Leitsatz:** Art. 82 DSGVO setzt einen tatsächlichen Schaden voraus. Jede Verletzung der DSGVO führt nicht automatisch zu einem Schadensersatzanspruch. Das Schadenserfordernis — auch für immaterielle Schäden — besteht als eigene Haftungsvoraussetzung neben dem Vorliegen eines Verstosses und dem Kausalzusammenhang.

**Konsequenz für VCS:** Betroffene müssen darlegen und beweisen, dass ihnen tatsächlich ein (auch immaterieller) Schaden entstanden ist. Die blosse Tatsache des Datenschutzvestosses genügt nicht.

### 2.2 EuGH C-456/22 (Gemeinde Ummendorf, 14.12.2023)

**Leitsatz:** Der Begriff des immateriellen Schadens schliesst nicht jede Unzufriedenheit oder jede empfundene Unannehmlichkeit ein. Es muss eine messbare Beeinträchtigung vorliegen.

**Konsequenz für VCS:** Pauschale Behauptungen, man fühle sich unwohl, genügen nicht.

### 2.3 BGH VI ZR 10/24 (18.11.2024)

**Leitsatz:** Der BGH hat nach dem EuGH-Urteil C-300/21 klargestellt, dass auch der Kontrollverlust über eigene Daten einen immateriellen Schaden darstellen kann, wenn die betroffene Person den Verlust der Kontrolle tatsächlich wahrgenommen hat und nicht lediglich abstrakt behauptet. Die Angst vor Missbrauch kann genügen, wenn sie nicht nur rein hypothetisch ist.

**Konsequenz für VCS:** Bei 142.300 geleakten Datensätzen (CVE-2026-0188) liegt ein tatsächlicher Datenverlust vor. Für diese Betroffenen ist ein Schaden leichter zu begründen als für reine Profiling-Betroffene ohne Datenpanne.

### 2.4 OLG Hamm, Urt. v. 15.08.2023 — 7 U 19/23

Das OLG Hamm hat in einem vergleichbaren DSGVO-Schadensersatzfall (Kreditscoring) einen Schadensersatz von 2.000 EUR für immaterielle Schäden zugesprochen, wo eine konkrete Ablehnung wegen fehlerhafter Schufa-Eintragung nachgewiesen war.

---

## 3. Analyse der 8.200 Kläger-Ansprüche

### 3.1 Segmentierung der Kläger nach Schadenslage

| Segment | Anzahl | Schadenslage | Bewertung |
|---------|--------|-------------|-----------|
| A: Wohnungsablehnung nachweislich wegen ROT-Score | Geschätzt 800 | Stark (direkte Kausalität) | Anspruch wahrscheinlich |
| B: Datenleak-Betroffene (142.300 gesamt, davon Kläger) | Geschätzt 2.100 | Mittel (Kontrollverlust belegt) | Anspruch möglich |
| C: Profiling-Betroffene ohne Datenleak, mit GRÜN/GELB-Score | Geschätzt 3.400 | Schwach (kein konkreter Schaden) | Anspruch zweifelhaft |
| D: Betroffene ohne nachweisliche Auswirkung | Geschätzt 1.900 | Minimal | Anspruch unwahrscheinlich |

**Verteidigungsansatz:** Differenzierte Auseinandersetzung mit den Segmenten A bis D. Zugeständnis bei Segment A und B (Vergleichsangebot), Abwehr bei C und D.

### 3.2 Höhe des immateriellen Schadens

Art. 82 DSGVO enthält keine gesetzliche Schadenshoeheproblematik — die Berechnung erfolgt nach nationalen Grundsätzen. Referenzpunkte:

| Gericht | Fall | Zugesprochener Betrag |
|---------|------|-----------------------|
| OLG Hamm 7 U 19/23 | Schufa-Scoring-Fehler | 2.000 EUR |
| LG Frankfurt 2-27 O 100/21 | Datenleak Facebook | 500–1.000 EUR |
| LG Düsseldorf 4 O 267/21 | Whatsapp-Datenpanne | 100 EUR |
| BGH VI ZR 10/24 | Datenleak mit Kontrollverlust | 1.200 EUR |

**Klaegerforderung:** 1.500 EUR — am oberen Ende des realistischen Spektrums für reine Profiling-Fälle ohne Datenpanne.

**Gegenargument VCS:** Für Segment C und D liegt kein anspruchsbegruendender Schaden vor. Selbst für Segment A und B ist 1.500 EUR übersetzt; realistisch sind 300–800 EUR.

---

## 4. Bagatellgrenzen-Argumentation

### 4.1 Bagatellschwelle nach EuGH und BGH

Der BGH hat in VI ZR 10/24 keine explizite Bagatellgrenze eingeführt, aber betont, dass ein minimaler, unbedeutender Schaden nicht ausreicht. Das OLG Stuttgart (2 U 63/21) hat eine Bagatellschwelle von ca. 100 EUR als Untergrenze diskutiert.

### 4.2 VCS-Argumentation

Für Betroffene des Segments C (Profiling, GRÜN/GELB-Score, keine Wohnungsablehnung):
- Kein Datenleak (nicht Teil der 142.300 exfiltrierten Datensätze)
- Keine negative Scoring-Auswirkung (GRÜN/GELB = positive/neutrale Bewertung)
- Keine belegbare Angst oder psychische Belastung vorgetragen

**Argument:** Schadensersatzanspruch scheitert an der Voraussetzung eines tatsächlichen (nicht bloss behaupteten) immateriellen Schadens.

---

## 5. Haftungsbefreiung Art. 82 Abs. 3 DSGVO

Art. 82 Abs. 3 DSGVO: Verantwortliche können sich von der Haftung befreien, wenn sie nachweisen, dass sie in keinerlei Hinsicht für den Umstand verantwortlich sind, durch den der Schaden entstanden ist.

**Anwendbarkeit für VCS:** Begrenzt. VCS ist als Verantwortlicher direkt für den Verstoss verantwortlich. Eine Entlastung kommt allenfalls in Betracht, wenn Sundara Tech als Auftragsverarbeiter den Datenleak verursacht hat (was die Forensik noch nicht klärt).

---

## 6. Gesamtbewertung und Vergleichsstrategie

**Bestes Ergebnis für VCS:** Abweisung der Klagen der Segmente C und D (ca. 5.300 Betroffene x 1.500 EUR = 7.950.000 EUR entlastet). Vergleich mit Segmenten A und B bei 600 EUR je Person = 1.740.000 EUR.

**Realistisches Vergleichsangebot:** 500.000 EUR Pauschalbetrag für Schlichtungsfonds, verwaltet von der VZ NRW. Verteilung an Betroffene nach Schadensnachweisstufe.

---

## Quellen

- DSGVO Art. 82 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- EuGH C-300/21 (Oesterreichische Post) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0300)
- EuGH C-456/22 (Gemeinde Ummendorf) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0456)
- BGH VI ZR 10/24 — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- OLG Hamm 7 U 19/23 — [openjur.de](https://openjur.de)
- BGB § 254 — [dejure.org/gesetze/BGB](https://dejure.org/gesetze/BGB)
