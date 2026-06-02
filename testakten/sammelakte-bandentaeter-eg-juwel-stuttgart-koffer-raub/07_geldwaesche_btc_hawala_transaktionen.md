# Aktenstück 07 — Geldwaesche: BTC-Wallets (Chain-Analysis), Hawala-Transaktionen

**Verfahren:** StA Stuttgart 4 Js 18.422/26  
**Bearbeitung:** Gemeinsam alle Verteidiger; Schwerpunkt RA Dr. Schorlemmer (Korbiel) und RA Krämer (Iordache)  
**Ermittlungsstrang:** Geldwaesche § 261 StGB, Einziehung § 73 ff. StGB  
**Stand:** 27.01.2026

---

## 1. Sichergestellte Wertbeute

Die Wertbeute am 18.10.2025 umfasste laut Sicherstellungsprotokoll LKA BW EG Juwel 2025-1018:

| Kategorie | Anzahl | Wert (Schätzung SV Gruben) |
|----------|--------|---------------------------|
| Rolex-Uhren (versch. Modelle) | 14 Stück | ca. 420.000 EUR |
| Patek-Philippe-Uhren | 6 Stück | ca. 780.000 EUR |
| Bulgari-Halsketten (18k Gold, Diamantbesatz) | 22 Stück | ca. 390.000 EUR |
| Sonstige Schmuckstücke | 37 Stück | ca. 110.000 EUR |
| **Gesamtbeute** | — | **ca. 1.700.000 EUR** |

Davon sichergestellt: 0 EUR / 0 Stück (keine Beute bei Verhaftung, Fluchtwagen ohne Ware). Die gesamte Beute gilt als verschleppt. Drebenstedt konnte mit Fluchtwagen entkommen (bis zu seiner spaetlichen Festnahme in Bad Cannstatt am 22.10.2025).

**Verbleib Beute:** Nach Auswertung der Chain-Analysis und Hawala-Informationen (s.u.) wird die Beute als bereits teilweise "gewaschen" eingestuft.

---

## 2. BTC-Wallets — Chain-Analysis

### 2.1 Hintergrund

Die EG Juwel hat in Kooperation mit der Financial Intelligence Unit (FIU) des Zolls und dem BKA-Dezernat SOK eine Chain-Analysis (Blockchain-Transaktionsanalyse) auf der Grundlage identifizierter Wallet-Adressen durchgeführt.

**Dienstleister:** Chainalysis Inc. (US-Unternehmen), Kooperation BKA, Auftrag vom 25.10.2025

### 2.2 Identifizierte Wallets

| Wallet-ID (anonymisiert) | Bezeichnung laut EG | Saldo (Schnappschuss 30.10.2025) | Verbindung |
|--------------------------|--------------------|---------------------------------|----------|
| bc1q...koffer77 | "Wallet Korbiel" | 3,4 BTC (ca. 210.000 EUR) | Transaktion von "Wallet Iordache" am 20.10.2025 |
| bc1q...redking | "Wallet Iordache" | 14,2 BTC (ca. 880.000 EUR) | Eingehende TX von OTC-Broker (Dubai) am 22.10.2025 |
| bc1q...ldrive22 | "Wallet Drebenstedt" | 1,1 BTC (ca. 68.000 EUR) | Empfang von "Wallet Iordache" |

**Technische Grundlage:** Die Wallet-Zuordnung basiert auf:
1. Adressreferenzen in SkyECC-Nachrichten ("MK_Koffer": "meine Adresse ist bc1q...koffer77")
2. IP-Logging eines OTC-Brokers in Dubai (Rechtshilfeersuchen läuft noch)
3. Transaktionsmuster (Clustering-Analyse)

### 2.3 Beschlagnahme und Sicherstellung

Die Staatsanwaltschaft hat am 03.11.2025 eine Krypto-Beschlagnahme ("Krypto-Sicherstellung") durch den Beschluss AG Stuttgart Az. 2025-3012 BK eingeleitet. Die technische Sicherstellung ist jedoch noch nicht abgeschlossen (fehlende Private Keys). Die BTC befinden sich noch in den Wallets, sind aber durch Monitoring blockiert (Kooperation Chainalysis).

**Einziehungsrechtliche Grundlage:** § 73 Abs. 1 StGB (Einziehung von Taterträgen); § 76a Abs. 4 StGB (selbständige Einziehung ohne Verurteilung möglich, falls Iordache nicht gefasst wird); § 111b Abs. 1 StPO (vorläufige Sicherstellung).

---

## 3. Hawala-Transaktionen

### 3.1 Hawala-System — Erklärung

Das Hawala-System ist ein informelles Wertüberweisungsnetz ohne physische Geldtransfers. Beträge werden durch Vertrauen und Gegenkonten zwischen Hawaladaren verrechnet. Es ist in Deutschland nach § 10 ZAG genehmigungspflichtig, aber häufig ungenehmigt (Strafbarkeit § 54 Abs. 1 Nr. 2 ZAG).

### 3.2 Erkenntnisse im vorliegenden Verfahren

Aus den SkyECC-Nachrichten und einer VP-Aussage (Identität unter § 96 StPO gesperrt) ergibt sich:

**Hawala-Kette (rekonstruiert):**
- Iordache zahlte an "Hamid" (Hawaladaer Stuttgart, Identität ermittelt aber nicht angeklagt) ca. 180.000 EUR cash, gemünzt auf Weiterleitung nach Rumänien
- "Hamid" veranlasste Gegenabbuchung bei rumänischem Hawaladaer "Radu" (Bukarest, Identität unbekannt)
- "Radu" leitete Gegenwert in RON (rumänische Leu) an Familienangehörige Iordaches weiter

**Nachweis:** TKUe-Gespräch G-58 ("schick das an die Adresse, Hamid weiss wo..."), Observation LKA ("Hamid"-Treffen am 19.10.2025 im Stuttgarter Westend, Person identifiziert als Mehmet H., 49).

### 3.3 Strafbarkeit § 261 StGB

Die Schmuckbeute und BTC-Transaktionen sind tatgegenstaendlich i.S.d. § 261 Abs. 1 StGB (Verschleiern der Herkunft aus bandenmaessigem Raub als Vortat i.S.d. § 261 Abs. 1 Nr. 1 StGB). Taterträge aus dem Raub gelten als "kriminell kontaminiert".

**Strafrechtliche Wertung:** Iordache: Haupttäter § 261 StGB; Korbiel: Ggf. Gehilfe (Wallet-Empfang); Drebenstedt: Ggf. § 261 Abs. 6 StGB (leichtfertig); Krasniqi: Keine Geldwaesche-Erkenntnisse vorhanden.

---

## 4. Abwehrmassnahmen Verteidigung

### 4.1 Korbiel (Dr. Schorlemmer)

- Bestreitet Kenntnis der Wallet-Adresse "bc1q...koffer77"
- Bestreitet, diese Adresse in EncroChat-Nachrichten kommuniziert zu haben (vgl. Verwertbarkeitsproblem AS 03)
- Antrag auf Offenlegung der Chain-Analysis-Methodik (proprietärer Algorithmus Chainalysis — Verteidigung zweifelt an Reproduzierbarkeit)

### 4.2 Drebenstedt (RA Steinbach)

- Wallet "bc1q...ldrive22" durch RA Steinbach bestritten — Zuordnung nur indirekt über SkyECC (vgl. EncroChat-Verwertbarkeit)
- BTC-Saldo von 68.000 EUR wird als rechtmaessige Erwerbe aus selbständiger Tätigkeit erklärt

### 4.3 Einziehungs-Gegenargument

Sollte die EncroChat/SkyECC-Verwertbarkeit (AS 03) scheitern, fehlt die Grundlage für die Wallet-Zuordnung. Die Einziehung nach § 73 StGB setzt den Tatverdacht voraus.

**Quellen:** § 261 StGB, § 73 StGB, § 76a StGB (dejure.org); § 111b StPO (dejure.org); § 10 ZAG (dejure.org); BGH 1 StR 432/21 (Kryptowaesche); FATF Guidance on Virtual Assets 2021.
