# DATEV-ähnliche Übergabe — Simulation Mai 2026

**Dokument-Nr.:** BUCH-2026-0004  
**Zeitraum:** Mai 2026 (01.05.2026 – 31.05.2026)  
**Erstellt:** 20.05.2026  
**Erstellt von:** Jana Reuter / Mara Klein  
**Empfänger:** Steuerkanzlei Heinemann & Partner, Potsdamer Platz 5, 10785 Berlin  
**Status:** Vorläufig — Klärfall und Entwurfsrechnung offen  

---

## 1. Zweck dieses Dokuments

Dieses Dokument simuliert die monatliche Belegübergabe an die Steuerkanzlei im Format einer DATEV-ähnlichen Aufstellung. Es enthält alle gebuchten und zu buchenden Geschäftsvorfälle des Monats Mai 2026. Die echte DATEV-Übertragung erfolgt durch die Steuerkanzlei Heinemann & Partner nach Prüfung dieses Pakets.

**Wichtig:** Dieses Dokument ersetzt keine DATEV-Buchung. Es sind keine echten Buchungen oder Bankzahlungen ausgelöst worden.

---

## 2. Ausgangsumsätze (Ausgangsrechnungen)

### 2.1 Gebuchte Ausgangsrechnungen

| Rechnungs-Nr. | Mandant | Leistungsdatum | Netto | USt 19 % | Brutto | Zahlungseingang | Sachkonto (Vorschlag) |
|--------------|---------|---------------|------:|---------:|-------:|---------------:|----------------------|
| R-2026-0004 | Nordstern Verwaltungs-UG | 05.05.2026 | 880,00 EUR | 167,20 EUR | 1.047,20 EUR | ausstehend | 8400 Erlöse Rechtsberatung |
| R-2026-0005 | Alpha Grundstücks-UG | 07.05.2026 | 1.540,00 EUR | 292,60 EUR | 1.832,60 EUR | 14.05.2026 ✓ | 8400 Erlöse Rechtsberatung |
| R-2026-0006 | Peter Sommer | 04.05.2026 | 440,00 EUR | 83,60 EUR | 523,60 EUR | 08.05.2026 ✓ | 8400 Erlöse Rechtsberatung |

**Summe gebuchte Ausgangsrechnungen:**  
Netto: 2.860,00 EUR | USt: 543,40 EUR | Brutto: 3.403,40 EUR

### 2.2 Rechnungen im Entwurfsstatus (noch nicht zu buchen)

| Rechnungs-Nr. | Mandant | Leistungsdatum | Netto | USt | Brutto | Status |
|--------------|---------|---------------|------:|----:|-------:|--------|
| R-2026-0007 | Clara Meyer | 20.05.2026 | 352,00 EUR | 66,88 EUR | 418,88 EUR | **Entwurf — Freigabe ausstehend** |

R-2026-0007 ist erst nach Freigabe durch Jana Reuter (vorgesehen: 21.05.2026) in die DATEV-Buchung aufzunehmen. Die Steuerkanzlei erhält die finale Version separat.

---

## 3. Eingangsumsätze (Eingangsrechnungen / Vorsteuer)

Vollständige Belege aus `eingangsrechnungen_register.csv`:

| Datum | Lieferant | Belegnr. | Netto | VSt 19 % | VSt 7 % | Brutto | Sachkonto (Vorschlag) |
|-------|----------|---------|------:|---------:|--------:|-------:|----------------------|
| 02.05.2026 | TechHaus GmbH, Berlin | TH-2026-0344 | 189,00 EUR | 35,91 EUR | — | 224,91 EUR | 4920 EDV-Kosten |
| 05.05.2026 | Schreibwaren Müller KG | SM-0887 | 47,00 EUR | 8,93 EUR | — | 55,93 EUR | 4930 Bürobedarf |
| 08.05.2026 | Fachmedien Decker GmbH | FD-2026-1122 | 86,00 EUR | — | 6,02 EUR | 92,02 EUR | 4940 Fachliteratur |
| 12.05.2026 | AI Vendor Ireland Ltd. | INV-2026-EU-00442 | 120,00 EUR | — (§13b) | — | 120,00 EUR | 4920 EDV-Kosten (§13b-Leistung) |
| 15.05.2026 | TechHaus GmbH, Berlin | TH-2026-0391 | 109,00 EUR | 20,71 EUR | — | 129,71 EUR | 4920 EDV-Kosten |

**Summe Eingangsumsätze:**  
Netto: 551,00 EUR | VSt 19 %: 65,55 EUR | VSt 7 %: 6,02 EUR | §13b: 22,80 EUR (Steuer und Vorsteuer saldieren sich)

---

## 4. Zahlungseingänge (Kontoabstimmung)

Aus `geschaeftskonto_mai_2026.csv` — Abstimmung mit Rechnungen:

| Datum | Auftraggeber | Verwendungszweck | Betrag | Match | Status |
|-------|-------------|-----------------|-------:|-------|--------|
| 08.05.2026 | Peter Sommer | Meyer Rechnung | 523,60 EUR | R-2026-0006 | matched (mittel) — bestätigt |
| 14.05.2026 | Alpha Grundstücks-UG | R-2026-0005 Alpha | 1.832,60 EUR | R-2026-0005 | matched (hoch) — bestätigt |
| 16.05.2026 | W. Lindner | Beratung April | **228,00 EUR** | **kein Match** | **Klärfall — ungeklärt** |

**Klärfall 228,00 EUR:**  
Auftraggeber: W. Lindner, Savignyplatz 11, 10627 Berlin. Kein offener Posten in dieser Höhe. Fremdgeldverdacht wird geprüft. Sachkonto: vorerst "9000 Durchlaufende Posten / Klärungen". Endgültige Buchung nach Klärung.

---

## 5. Fehlende Angaben — DATEV-Prüfliste

Folgende Angaben fehlen noch und müssen vor der echten DATEV-Übermittlung ergänzt werden:

| Nr. | Fehlendes Element | Betrifft | Verantwortlich |
|----|------------------|---------|---------------|
| 1 | Beleglinks (PDF-Scan) | alle Eingangsrechnungen | Mara Klein / Tom Berger (nach Rückkehr) |
| 2 | Sachkonten Eingangsrechnungen | TechHaus, Schreibwaren Müller, Fachmedien Decker | Steuerkanzlei prüft und bestätigt |
| 3 | Steuerschlüssel DATEV-Codes | alle Buchungssätze | Steuerkanzlei |
| 4 | Klärfall 228,00 EUR | Konto-Eingänge | Jana Reuter |
| 5 | Freigabe und Endbuchung R-2026-0007 | Ausgangsumsatz | Jana Reuter (Freigabe 21.05.2026) |
| 6 | §13b-Buchungssatz AI Vendor | Eingangsrechnung | Steuerkanzlei Heinemann |
| 7 | Kassen-Journal Mai (falls Barzahlungen) | Kassenbuch | Mara Klein |

---

## 6. Nicht enthaltene Positionen

| Thema | Begründung |
|-------|-----------|
| Keine echte DATEV-Übertragung | Kanzlei hat kein DATEV-Connector-Abo; manuelle Übergabe an Steuerkanzlei |
| Keine endgültige Buchung | Alle Buchungen sind Vorschläge; Steuerkanzlei führt DATEV aus |
| Keine Bankzahlung ausgelöst | Zahlungsaufträge werden separat durch Jana Reuter im Online-Banking erstellt |
| Kein Kassenbuch | Kanzlei führt nur unbare Zahlungen; keine Barkasse |
| Kein Anlagevermögen | Im Berichtszeitraum keine Anlagezugänge oder -abgänge |

---

## 7. Zusammenfassung Monatsabschluss Mai 2026 (vorläufig)

| Position | Betrag |
|----------|-------:|
| Ausgangsumsätze Netto (ohne R-2026-0007) | 2.860,00 EUR |
| Umsatzsteuer auf Ausgangsumsätze | 543,40 EUR |
| Eingangsumsätze Netto | 551,00 EUR |
| Vorsteuer gesamt | 71,57 EUR (65,55 + 6,02) |
| §13b-Steuer (Eingang AI Vendor) | + 22,80 EUR |
| §13b-Vorsteuer (Eingang AI Vendor) | − 22,80 EUR |
| **Vorläufige Zahllast USt Mai 2026** | **ca. 471,83 EUR** |
| Klärfall (nicht gebucht) | 228,00 EUR |

---

*Dokument BUCH-2026-0004 — Erstellt: 20.05.2026 — Jana Reuter / Mara Klein, Kanzlei Reuter Rechtsanwälte, Lindenstraße 14, 10969 Berlin. Testdaten — keine echte DATEV-Buchung.*
