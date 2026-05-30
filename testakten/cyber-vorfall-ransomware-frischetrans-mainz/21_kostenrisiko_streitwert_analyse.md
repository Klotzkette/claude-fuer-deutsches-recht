# Kostenrisiko und Streitwertanalyse

**Aktenstück:** 21  
**Datum:** 13.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Bearbeiter:** RA Lukas Drosten, Fachanwalt für IT-Recht

---

## 1. Überblick Kostenrisiko-Matrix

| Komplex | Streitwert / Bußgeld | Prozesswahrscheinlichkeit | Erwartetes Kostenrisiko |
|---|---|---|---|
| A. ProcessSpark-Klage (LG Mainz) | 681.818 EUR | Hoch (falls keine Einigung) | 35.000–55.000 EUR Prozesskosten (1. Instanz) |
| B. DSGVO-Bußgeld LfDI RLP | bis 350.000 EUR | Mittel | 50.000–350.000 EUR |
| C. Kundenforderungen (Frischbäcker AG) | geschätzt 50.000–150.000 EUR | Mittel | 20.000–80.000 EUR (ggf. Versicherung) |
| D. KI-VO-Bußgeld (PalettenAuge AI) | bis 15 Mio. EUR (Art. 99) | Niedrig | 0–200.000 EUR (KMU-Staffel) |
| E. AGPL-Abmahnung (TourPlanner) | 5.000–50.000 EUR | Niedrig | 5.000–15.000 EUR |
| F. Eigene Anwaltskosten (Mandat gesamt) | — | Sicher | 80.000–150.000 EUR |
| G. IT-Wiederherstellung | — | Sicher | 180.000–230.000 EUR |
| H. Forensikkosten | — | Sicher | 45.000–65.000 EUR |
| I. Betriebsausfall (nicht versichert, Selbstbehalt) | — | Sicher | 25.000 EUR (Selbstbehalt) |

---

## 2. Streitwertanalyse ProcessSpark-Klage (LG Mainz, AZ 3 O 88/26)

### 2.1 Streitwert der Klage

Der Streitwert der geplanten Klage gegen ProcessSpark Cloud AG setzt sich zusammen aus:

| Klagepunkt | Betrag |
|---|---|
| Schadensersatz Wiederherstellung IT | 198.500 EUR |
| Schadensersatz Betriebsausfall | 387.200 EUR |
| Schadensersatz Forensik | 52.800 EUR |
| Schadensersatz Anwaltskosten (Teilforderung) | 24.800 EUR |
| Schadensersatz DSGVO-Folgekosten | 18.000 EUR |
| Vertragsstrafe | 518 EUR |
| **Klagebetrag gesamt (vorläufig)** | **681.818 EUR** |

Vorbehalt: Erhöhung des Klageantrags nach forensischem Abschlussbericht möglich (Streitwert dann ggf. bis 850.000 EUR).

### 2.2 Anwaltskosten (RVG-Berechnung, 1. Instanz LG Mainz)

**Streitwert:** 681.818 EUR

Basis: RVG-Vergütungsverzeichnis (VV RVG), Anlage 1

| Gebühr | Multiplier | Berechnungsbasis (Gebühr aus Streitwert) | Betrag |
|---|---|---|---|
| 1,3-Verfahrensgebühr (Nr. 3100 VV RVG) | 1,3 | Grundgebühr aus 681.818 EUR (= 3.668 EUR) | 4.768,40 EUR |
| 1,2-Terminsgebühr (Nr. 3104 VV RVG) | 1,2 | 3.668 EUR | 4.401,60 EUR |
| Einigungsgebühr (Nr. 1003 VV RVG, falls Vergleich) | 1,5 | 3.668 EUR | 5.502 EUR |
| Post/Telekommunikationspauschale | — | 20 EUR je | 20 EUR |
| **Gesamtgebühren RA (ca., ohne USt.)** | | | **ca. 14.000–16.000 EUR** |

**Hinweis:** Die eigenen Anwaltsgebühren der Mandantin sind im Unterliegensfall von ProcessSpark zu erstatten (§ 91 ZPO), im eigenen Unterlegensfall selbst zu tragen.

**Gerichtskosten (GKG):**

Bei einem Streitwert von 681.818 EUR:

| Position | Betrag (geschätzt) |
|---|---|
| 3,0-fache Gerichtsgebühr (GKG Anlage 1, Klage streitig) | ca. 10.500 EUR |
| Mindest-Vorschuss bei Klageeinreichung (mind. 3-fach) | ca. 10.500 EUR |

### 2.3 Kostenrisiko Prozessverlust

Im Falle eines vollständigen Unterliegens vor dem LG Mainz trüge die Mandantin:
- Eigene Anwaltskosten: ca. 14.000–16.000 EUR
- Gerichtskosten: ca. 10.500 EUR
- Anwaltskosten der Gegenseite (ProcessSpark): ca. 14.000–16.000 EUR

**Gesamtrisiko im Unterliegensfall (1. Instanz):** ca. 38.500–42.500 EUR

**Einschätzung:** Das Prozessrisiko ist angesichts der guten Beweislage überschaubar. Die Klageandrohung ist wirtschaftlich gerechtfertigt.

---

## 3. DSGVO-Bußgeld — Schätzung

### 3.1 Bußgeldrahmen (Art. 83 DSGVO)

- Art. 83 Abs. 3 DSGVO: Verstoß gegen Art. 32 DSGVO (unzureichende TOMs) → max. 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes (Frischetrans: 38 Mio. EUR × 2 % = 760.000 EUR)

### 3.2 Bußgeldbemessung (Art. 83 Abs. 2 DSGVO — Zumessungskriterien)

| Faktor | Bewertung | Einfluss auf Bußgeld |
|---|---|---|
| Art und Schwere des Verstoßes | Gesundheitsdaten betroffen, hohe Schwere | Erhöhend |
| Fahrlässigkeit | Eher mittelbar (durch ProcessSpark verursacht) | Mildernd |
| Schadensbegrenzungsmaßnahmen | Sofortige Reaktion, vollständige Kooperation | Stark mildernd |
| Kooperationsbereitschaft mit LfDI | Hoch (fristgerechte Meldung, DSFA eingeleitet) | Stark mildernd |
| Vorherige Verstöße | Keine | Mildernd |
| Kategorien betroffener Daten | Gesundheitsdaten (Art. 9) | Erhöhend |
| Anzahl betroffener Personen | 298 Personen | Erhöhend |
| Unternehmensgröße | KMU (280 MA) | Mildernd |

**Schätzung Bußgeld:** 30.000–200.000 EUR

---

## 4. Gesamtkostenplanung (Liquiditätsbedarf Mandantin)

| Ausgabeblock | Zeitraum | Betrag |
|---|---|---|
| Sofortkosten (Forensik, IT-Notfall) | Mai 2026 | 220.000 EUR |
| Anwaltskosten lfd. Mandat | Mai–Aug. 2026 | 80.000 EUR |
| IT-Wiederherstellung (vollständig) | Mai–Juni 2026 | 210.000 EUR |
| DSGVO-Compliance-Maßnahmen | Mai–Aug. 2026 | 45.000 EUR |
| KI-VO-Compliance (PalettenAuge) | Juni–Aug. 2026 | 30.000 EUR |
| Open-Source-Compliance | Mai–Juni 2026 | 10.000 EUR |
| PR/Krisenkommunikation | Mai 2026 | 15.000 EUR |
| Selbstbehalt Versicherung | sofort | 25.000 EUR |
| **Gesamtliquiditätsbedarf (Eigenmittel, vor Versicherungsleistung)** | | **635.000 EUR** |

**Erwartete Versicherungsleistung (CyberCovered AG):** ca. 450.000–700.000 EUR  
**Erwarteter Schadensersatz ProcessSpark (nach Einigung/Klage):** ca. 400.000–600.000 EUR  
**Netto-Belastung Frischetrans (Schätzung):** ca. 0–200.000 EUR (sofern Versicherung und Regressansprüche planmäßig funktionieren)

---

## 5. Empfehlung zur Liquiditätssicherung

RA Drosten empfiehlt der Mandantin, mit ihrer Hausbank (Sparkasse Mainz) eine Kreditlinie von mindestens 500.000 EUR für die Dauer des Krisenmanagements zu vereinbaren, um Liquiditätsengpässe zu überbrücken, bis Versicherungsleistungen und Schadensersatz fließen.
