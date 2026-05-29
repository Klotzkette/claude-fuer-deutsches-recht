# Transaktionsmonitoring-Alert – Drittzahlung 187.500 EUR

**Alert-Nr.:** TM-ALERT-2026-0047  
**Generiert:** 28.04.2026, 14:52 Uhr (automatisches Monitoringsystem)  
**Geprüft von:** Thomas Eckhardt (Geldwäschebeauftragter)  
**Eskalationsdatum:** 29.04.2026  
**Status:** Eskaliert — Verdachtsmeldung eingeleitet  
**Rechtsgrundlage:** § 15 Abs. 3 GwG; § 43 GwG; FATF-Guidance on High-Risk Transactions  

---

## 1. Transaktionsdetails

| Feld | Inhalt |
|---|---|
| **Kontonummer Empfänger** | Musterholding GmbH, Commerzbank Frankfurt, IBAN DE44 5004 0000 0517 8837 00 |
| **Eingangsdatum** | 28.04.2026 |
| **Eingangszeit** | 14:37 Uhr MESZ |
| **Betrag** | 187.500,00 EUR |
| **Auftraggeber** | Adriatic Commerce Ltd., Valletta, Malta |
| **Auftraggeber-IBAN** | MT84 MALT 0110 0001 2345 MTLB 010 |
| **Auftraggeber-Bank** | Bank of Valletta p.l.c., Valletta, Malta |
| **Verwendungszweck** | "Advance Payment – Contract MH-DTS-2026-04" |
| **Zugehöriger Vertrag** | MH-DTS-2026-04 (Danube Trade Solutions SRL — noch nicht unterschrieben) |
| **Vertragspartner laut KYC** | Danube Trade Solutions SRL, Bukarest, Rumänien |
| **Vertragspartner laut Zahlung** | Adriatic Commerce Ltd., Malta — abweichend |

---

## 2. Alert-Generierung und Regelwerk

### 2.1 Ausgelöste Monitoring-Regeln

| Regel-ID | Regelbezeichnung | Schwellenwert / Kriterium | Ausgelöst? |
|---|---|---|---|
| TM-R-001 | Drittzahler-Abweichung | Zahlung von nicht-identem Vertragspartner | **Ja** |
| TM-R-002 | Betragsschwelle Hoch | Ersteingang >100.000 EUR von unbekanntem Absender | **Ja** |
| TM-R-003 | Neue-Geschäftsbeziehung + Vorauszahlung | Anzahlung vor Vertragsunterzeichnung | **Ja** |
| TM-R-004 | Hochrisikoland-Absender | Absenderland Malta (EU-Offshore-Jurisdiktion) | **Ja** |
| TM-R-005 | Verwendungszweck-Referenz offen | Vertragsnummer in VZ, aber Vertrag nicht freigegeben | **Ja** |
| TM-R-006 | Rundbetrag | Betrag exakt auf 500 EUR gerundet | Nein (187.500 = gerundet auf 2.500 EUR-Basis) |
| TM-R-007 | Knapp-Unter-Schwelle | Betrag knapp unter 200.000 EUR | **Ja** (mögliches Structuring) |

**Gesamtzahl ausgelöster Regeln:** 6 von 7 → **Automatische Hochrisiko-Eskalation**

### 2.2 Alert-Score

Das Monitoringsystem vergibt einen risikogewichteten Score (0–100):

| Kriterium | Gewichtung | Score |
|---|---|---|
| Drittzahler-Abweichung | × 2,5 | 25 |
| Betragshöhe (>100 TEUR) | × 1,5 | 15 |
| Neue Geschäftsbeziehung | × 1,5 | 15 |
| Hochrisikoland Malta | × 1,5 | 15 |
| VZ-Diskrepanz (offener Vertrag) | × 1,0 | 10 |
| Possible Structuring | × 1,0 | 10 |
| **Gesamt-Alert-Score** | | **90 / 100** |

Schwellenwert automatische Eskalation an GwB: 60. Schwellenwert Verdachtsmeldungs-Prüfung: 80. **Alert-Score 90 → Pflichtprüfung auf Verdachtsmeldung.**

---

## 3. Manuelle Analyse durch den Geldwäschebeauftragten

### 3.1 Hintergrund Adriatic Commerce Ltd.

Adriatic Commerce Ltd. ist im maltesischen Handelsregister (MFSA Registry) eingetragen (Reg. Nr. C 74891, eingetragen 09.03.2021). Geschäftszweck laut Register: "General Trading". Director: Nominee. Jahresumsatz: nicht öffentlich verfügbar. Eine geschäftliche Verbindung zu Danube Trade Solutions SRL ist nicht dokumentiert; auf Anfrage (29.04.2026) gab Andrei Moldovan (Danube Trade) an, Adriatic Commerce Ltd. sei ein "verbundenes Unternehmen", ohne weitere Details zu nennen.

### 3.2 Bewertung der Drittzahlung

Drittzahlungen sind per se nicht verboten, begründen aber nach § 15 Abs. 3 Nr. 3 GwG und den BaFin-Auslegungshinweisen eine verstärkte Sorgfaltspflicht, wenn:
- keine vorige schriftliche Erklärung des Zahlenden vorliegt,
- das Verhältnis Drittzahler–Vertragspartner nicht nachvollziehbar ist,
- der Zahlende selbst einem erhöhten Länderrisiko unterliegt (Malta), und
- die Drittzahlung der ersten Transaktion in einer neuen Geschäftsbeziehung entspricht.

**Alle vier Bedingungen liegen hier kumulativ vor.**

### 3.3 Hypothesenprüfung

Der Geldwäschebeauftragte hat folgende Hypothesen geprüft:

**Hypothese 1 — Legitimer geschäftlicher Hintergrund:**  
Adriatic Commerce Ltd. könnte ein verbundenes Unternehmen sein, das aus betrieblichen Gründen (z.B. zentralisiertes Cash Management) die Zahlung übernimmt. Diese Erklärung ist ohne Nachweis einer Konzernverbindung oder einer Cash-Pool-Vereinbarung nicht nachprüfbar und daher unzureichend.

**Hypothese 2 — Strohmann-Zahlung:**  
Adriatic Commerce Ltd. könnte als Strohmann-Gesellschaft fungieren, um die eigentliche Quelle der Mittel zu verschleiern. Diese Hypothese ist durch den ungeklärten UBO von Blue Harbor Holdings Ltd. und die Offshore-Struktur beider Gesellschaften (Zypern + Malta) erhärtet.

**Hypothese 3 — Layering (Geldwäschephase):**  
Die Zahlung könnte Teil eines Layering-Prozesses sein, bei dem Gelder aus krimineller Herkunft über mehrere Gesellschaften und Jurisdiktionen verschoben werden, bevor sie in die Wirtschaft integriert werden.

**Ergebnis:** Hypothese 1 nicht belegt; Hypothesen 2 und 3 können nicht ausgeschlossen werden. Nach dem Gesamtbild überwiegen die Verdachtsmomente.

---

## 4. Reaktionsmaßnahmen

### 4.1 Sofortmaßnahmen (28.04.2026)

1. **Transaktionsstopp:** Die Buchungsabteilung wurde angewiesen, den Betrag von 187.500 EUR auf ein internes Sperrkonto zu transferieren und nicht als reguläre Kundenzahlung zu verarbeiten. Konto: Musterholding GmbH Internum, IBAN DE44 5004 0000 0517 9900 12 (Sperrkonto Compliance).
2. **Eskalation an GwB:** Automatic Alert-E-Mail an Thomas Eckhardt; Eingangsbestätigung 28.04.2026, 15:04 Uhr.
3. **Eskalation an GF:** Eckhardt informiert Brenner und Wollner am 29.04.2026, 09:00 Uhr (E-Mail zzgl. Telefonat).

### 4.2 Folgemaßnahmen (29.04.–19.05.2026)

| Maßnahme | Datum | Status |
|---|---|---|
| Anforderung Erklärung zu Drittzahlung an Danube Trade | 29.04.2026 | Keine hinreichende Antwort |
| Screening Adriatic Commerce Ltd. | 29.04.2026 | Negativscreening (kein Sanktionstreffer) |
| Abklärung Hypothesen durch GwB | 30.04.–05.05.2026 | Abgeschlossen |
| Einleitung Mittelherkunftsnachweis | 16.05.2026 | Antwort ausstehend |
| Konsultation RA Dr. Heller | 05.05.2026 | Erfolgt (Mandatsnotiz) |
| Verdachtsmeldung vorbereiten | 10.–19.05.2026 | Eingereicht 19.05.2026 |
| Transaktionsstopp aufrechterhalten | Laufend | Aktiv |

---

## 5. Verknüpfung mit weiteren Alerts und Monitored Entities

| Entität | Verbindung | Risikostatus |
|---|---|---|
| Danube Trade Solutions SRL | Vertragspartner (laufende KYC) | Hochrisiko |
| Blue Harbor Holdings Ltd. | Gesellschafter Danube Trade | Hochrisiko |
| Andrei Moldovan | GF Danube Trade; PEP-Treffer | Hochrisiko |
| MH-DTS-2026-04 | Vertragsreferenz in VZ | Geplanter Vertrag, nicht freigegeben |

---

## 6. Fazit und Entscheidung

Der Alert TM-ALERT-2026-0047 erfüllt alle Voraussetzungen der § 43 Abs. 1 GwG-Meldepflicht. Die Verdachtsmeldung VM-MH-2026-0041 wurde am 19.05.2026 über das goAML-Portal der FIU eingereicht. Der Transaktionsstopp bleibt bis zur Freigabe durch die FIU gemäß § 46 Abs. 1 GwG bestehen.

**Nächste Kontrollpunkte:**
- FIU-Eingangsbestätigung ausstehend (erwartet innerhalb 48 Stunden nach Einreichung)
- FIU-Rückmeldung gem. § 46 GwG (bis zu 3 Werktage Haltefrist)
- Vertrieb darf keine Freigabezusagen an Danube Trade machen (§ 47 GwG — Vertraulichkeit)

---

*Alert-Nr.: TM-ALERT-2026-0047 — Musterholding GmbH / Transaktionsmonitoring*  
*Aufbewahrungsfrist: 5 Jahre (§ 8 Abs. 4 GwG)*
