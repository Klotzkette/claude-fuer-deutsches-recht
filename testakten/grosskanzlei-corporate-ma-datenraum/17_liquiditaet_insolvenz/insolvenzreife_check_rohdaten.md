# Insolvenzreife-Check — Delta Service GmbH

**Aktenzeichen:** MA-2026-SF-001-R  
**Erstellt:** 15.05.2026  
**Verfasser:** Counsel D (Restrukturierung)  
**Adressat:** Deal Team / Eagle Capital Partners — Intern  
**Methodik:** Dreistufenprüfung nach §§ 17–19 InsO

> **Grundsatz:** Dieser Check gibt nicht "grün", wenn Datenlücken bestehen. Fehlende Informationen werden als Risikopositionen ausgewiesen und Nachforderungen gestellt.

---

## 1. Prüfstufe 1 — Zahlungsunfähigkeit (§ 17 InsO)

**Rechtslage:** Zahlungsunfähig ist ein Schuldner, der nicht in der Lage ist, die fälligen Zahlungspflichten zu erfüllen. Maßgeblich ist der **Stichtag** (hier: 15.05.2026). Gem. BGH-Rechtsprechung gilt: Unterdeckung von mehr als 10 % der fälligen Verbindlichkeiten und keine konkrete Erwartung der Beseitigung innerhalb von 3 Wochen → Zahlungsunfähigkeit.

### 1.1 Fälligkeitstest (Stichtag 15.05.2026)

| Fällige Verbindlichkeit | Betrag (EUR) | Quelle |
|---|---|---|
| Überfällige Lieferantenrechnungen (> 30 Tage) | 410.000 | Buchhaltung |
| Mietverbindlichkeiten (Mai, überfällig 3 Tage) | 42.000 | Mietvertrag |
| Sonstige fällige Verbindlichkeiten | 25.000 | Buchhaltung |
| **Gesamt fällig** | **477.000** | |

### 1.2 Liquiditätsdeckung

| Verfügbare Mittel | Betrag (EUR) | Einschränkung |
|---|---|---|
| Bankguthaben | 840.000 | Ohne Einschränkung |
| Kreditlinie (nominal) | 300.000 | **Covenant-Waiver fehlt → nicht anrechenbar** |
| **Effektiv verfügbar** | **840.000** | |

**Deckungsgrad:** EUR 840.000 / EUR 477.000 = **176 %** → Zahlungsunfähigkeit liegt am Stichtag 15.05.2026 **noch nicht vor**.

### 1.3 Datenlücken § 17

| Datenlücke | Risiko | Nachforderung |
|---|---|---|
| Covenant-Waiver DKB noch nicht erteilt | Kreditlinie kann plötzlich nicht gezogen werden | Waiver-Bestätigung bis 20.05.2026 |
| Lieferstopp 3 Lieferanten droht | Fällige Abnahmeverbindlichkeiten entstehen ggf. sofort | Lieferantenstatus klären bis 17.05.2026 |
| Großkundenforderung EUR 180.000 bestritten | Kein sicherer Eingang | Beleg über Einigungsgespräch |

---

## 2. Prüfstufe 2 — Drohende Zahlungsunfähigkeit (§ 18 InsO)

**Rechtslage:** Drohende Zahlungsunfähigkeit liegt vor, wenn der Schuldner voraussichtlich nicht in der Lage sein wird, die bestehenden Zahlungspflichten im **Zeitpunkt der Fälligkeit** zu erfüllen. Planungshorizont: üblicherweise 24 Monate.

### 2.1 Vorausschau 13 Wochen (aus Cash Bridge)

Gemäß Cash Bridge (cash_bridge_13_wochen.csv) tritt ein negativer Saldo erstmals in **KW 26 (Anfang Juli 2026)** auf: EUR -198.000.

| KW | Endbestand (EUR) | Bewertung |
|---|---|---|
| 21 | 678.000 | Grün |
| 22 | 365.000 | Grün |
| 23 | 132.000 | Gelb (Puffer eng) |
| 24 | 120.000 | Gelb |
| 25 | 120.000 | Gelb |
| 26 | **-198.000** | **Rot — drohende Zahlungsunfähigkeit** |

**Ergebnis:** § 18 InsO-Schwelle ist **überschritten**. Drohende Zahlungsunfähigkeit liegt vor.

### 2.2 Datenlücken § 18

| Datenlücke | Risiko | Nachforderung |
|---|---|---|
| Fortbestehensprognose nicht formal beschlossen | Ohne Prognose kann § 19 InsO greifen | Prognose bis 01.06.2026 beschließen |
| 24-Monats-Planung fehlt | Nur 13-Wochen-Sicht vorhanden | Jahresplan 2026/2027 anfordern |
| Rangrücktritt GGD nur Entwurf | Gesellschafterdarlehen als Verbindlichkeit gezählt | Unterzeichnung bis 30.05.2026 (CP-13) |

---

## 3. Prüfstufe 3 — Überschuldung (§ 19 InsO)

**Rechtslage:** Überschuldung liegt vor, wenn das Vermögen des Schuldners die bestehenden Verbindlichkeiten nicht mehr deckt, **sofern keine positive Fortbestehensprognose** besteht.

### 3.1 Überschuldungsstatus (vereinfacht, Jahresabschluss 2024)

| Position | Buchwert (EUR) | Anmerkung |
|---|---|---|
| Bilanzielles Eigenkapital | 2.400.000 | JA 2024 testiert |
| Gesellschafterdarlehen (nachrangig nur Entwurf) | 1.800.000 | Als Fremdkapital gewertet bis Rangrücktritt final |
| Überschuldungs-relevanter Saldo | + 600.000 | Knapp positiv — **stark abhängig vom Rangrücktritt** |

**Risiko:** Wenn Rangrücktritt nicht rechtzeitig finalisiert wird, reduziert sich das Eigenkapital um EUR 1,8 Mio. → bilanziell negativ → **Überschuldung**.

### 3.2 Fortbestehensprognose

**Status:** Die Geschäftsführung hat keine dokumentierte Fortbestehensprognose beschlossen. Dies ist ein **schwerwiegender Mangel**: Ohne positive Fortbestehensprognose gilt die insolvenzrechtliche Überschuldung auch bei positiver Buchwertbilanz als gegeben (§ 19 Abs. 2 Satz 1 InsO).

**Nachforderung:** Fortbestehensprognose (12–24 Monate, durch Wirtschaftsprüfer begleitet) bis **01.06.2026** beschließen.

---

## 4. Haftungsrisiken Geschäftsführung

| Haftungsgrundlage | Tatbestand | Status |
|---|---|---|
| § 15a InsO | Verletzung der Insolvenzantragspflicht | Risiko sobald § 17 oder § 19 eingetreten |
| § 64 GmbHG a.F. / § 15b InsO | Zahlungen nach Insolvenzreife | Risiko bei Fortführung ohne Gegenmaßnahmen |
| § 823 Abs. 2 BGB i.V.m. § 15a InsO | Drittschäden durch verspäteten Antrag | Risiko gegenüber neuen Gläubigern |

---

## 5. Gesamtergebnis

| Insolvenztatbestand | Ergebnis | Begründung |
|---|---|---|
| § 17 InsO Zahlungsunfähigkeit | **Nein (aktuell)** | Bankguthaben reicht — noch |
| § 18 InsO drohende Zahlungsunfähigkeit | **Ja** | Negativsaldo ab KW 26 |
| § 19 InsO Überschuldung | **Unklar — Datenlücken** | Rangrücktritt + Fortbestehensprognose fehlen |

---

## 6. Kritische Nachforderungsliste

1. **Covenant-Waiver DKB AG** — bis 20.05.2026  
2. **Lieferantenstatus klären** (Lieferstoppdrohung) — bis 17.05.2026  
3. **Rangrücktritt GGD** finalisieren — bis 30.05.2026 (CP-13)  
4. **Fortbestehensprognose** formal beschließen (GF-Beschluss + WP) — bis 01.06.2026  
5. **24-Monats-Plan** anfordern — bis 30.05.2026  
6. **Großkunden-Forderung** eskalieren (EUR 180.000) — bis 17.05.2026  

---

*Aktenvermerk-Nr.: AV-INSO-2026-001 | Privileged & Confidential*
