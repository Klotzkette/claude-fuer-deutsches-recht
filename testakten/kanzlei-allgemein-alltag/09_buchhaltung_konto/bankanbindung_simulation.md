# Aktenvermerk — Geschäftskonto-Simulation

**Vermerk-Nr.:** BUCH-2026-0003  
**Datum:** 20.05.2026  
**Verfasserin:** Jana Reuter  
**Zweck:** Dokumentation der simulierten Bankanbindung für die Testakte; Beschreibung des erwarteten Workflows und der Systemgrenzen

---

## 1. Ausgangslage

Die Kanzlei Jana Reuter führt ein Geschäftskonto bei der Commerzbank AG (fiktiv: IBAN DE12 1004 0048 0012 3456 78, BIC COBADEFFXXX). Eine direkte technische Anbindung des Kontos an die Kanzleisoftware oder an ein Buchhaltungsprogramm besteht derzeit nicht.

Für die Zwecke der Testakte wird das Konto durch die CSV-Datei `geschaeftskonto_mai_2026.csv` simuliert, die typische Kontobewegungen des Monats Mai 2026 enthält (Zahlungseingänge von Mandanten, Daueraufträge, Ausgangsüberweisungen, ungeklärte Eingänge).

---

## 2. Systemgrenzen (was die Simulation nicht kann)

| Einschränkung | Erläuterung |
|--------------|-------------|
| Keine echten Bankzugangsdaten | Es werden keine PIN/TAN, keine API-Tokens oder PSD2-Zugänge verwendet |
| Keine Zahlungsaufträge | Ausgehende Zahlungen können in der Simulation nicht ausgelöst werden |
| Keine Echtzeit-Daten | Der CSV-Datensatz ist statisch; er spiegelt den Stand 19.05.2026, 23:59 Uhr |
| Keine Buchungsendgültigkeit | Alle Zuordnungen sind Vorschläge; echte Buchung erfolgt durch Steuerberater oder DATEV |
| Kein SEPA-Lastschriftmandat | Automatischer Einzug von Mandantenforderungen nicht möglich |

---

## 3. Workflow — Schritte der Zahlungsabstimmung (Matching)

### Schritt 1 — Kontoauszug importieren

Die Datei `geschaeftskonto_mai_2026.csv` wird in die Arbeitsmappe geladen. Sie enthält folgende Spalten:

- Buchungsdatum
- Wertstellungsdatum
- Auftraggeber / Empfänger
- Verwendungszweck
- Betrag (positiv = Eingang, negativ = Ausgang)
- Saldo nach Buchung

### Schritt 2 — Offene Posten laden

Die Datei `offene_posten_debitoren.csv` enthält alle ausgestellten und noch nicht bezahlten Rechnungen:

| Rechnungs-Nr. | Mandant | Betrag (Brutto) | Fällig am |
|--------------|---------|----------------:|----------|
| R-2026-0004 | Nordstern Verwaltungs-UG | 1.047,20 EUR | 05.05.2026 |
| R-2026-0007 | Clara Meyer | 418,88 EUR | 03.06.2026 (Entwurf) |

### Schritt 3 — Automatisches Matching

Das System (oder der Bearbeiter manuell) gleicht Zahlungseingänge im Kontoauszug gegen offene Posten ab, primär anhand des Verwendungszwecks (Rechnungsnummer) und Betrags:

| Kontoeingang | Betrag | Matched mit | Konfidenz |
|-------------|-------:|------------|:---------:|
| 14.05.2026 — Alpha Grundstücks-UG, VWZ: R-2026-0005 | 1.832,60 EUR | R-2026-0005 | hoch |
| 08.05.2026 — Peter Sommer, VWZ: Meyer Rechnung | 523,60 EUR | R-2026-0006 | mittel (VWZ unscharf) |
| 16.05.2026 — unbekannt, VWZ: "Beratung April" | 228,00 EUR | kein Match | ungeklärt |

### Schritt 4 — Klärfälle bearbeiten

**Klärfall 228,00 EUR:**  
Eingang am 16.05.2026, Auftraggeber: "W. Lindner, Savignyplatz 11, 10627 Berlin", Verwendungszweck: "Beratung April". Kein offener Posten in dieser Höhe. Mögliche Szenarien:

- Mandant aus früherer Beratung, Rechnung nicht vollständig erfasst — Rechnungsarchiv April prüfen.
- Fremdgeld (Weiterleitung für Mandant erwartet) — sofort auf separates Anderkonto oder zumindest buchhalterisch trennen. Fremdgeldverdacht vermerken.
- Irrtümliche Überweisung eines Dritten — Rückfrage erforderlich.

**Maßnahme:** Jana Reuter prüft Rechnungsarchiv April 2026. Bis zur Klärung: Betrag als "ungeklärt" im DATEV-Übergabeblatt markieren.

### Schritt 5 — Schwache Matches und manuelle Korrekturen

Schwache Matches (Konfidenz "mittel" oder "niedrig") werden manuell durch Jana Reuter oder Mara Klein bestätigt. Kein automatischer Buchungsabschluss.

### Schritt 6 — DATEV-Übergabe vorbereiten

Nach Abschluss des Matchings wird ein Übergabe-Paket für die Steuerkanzlei Heinemann & Partner vorbereitet. Dieses enthält:
- Kontoauszug CSV (unveränderter Original-Export)
- Matching-Ergebnis als Tabelle
- Klärfall-Liste
- Offene-Posten-Liste nach Abstimmung

---

## 4. Erwartetes Verhalten bei echter Bankanbindung (Zielzustand)

In einem vollständig integrierten System (z. B. DATEV-Online, Lexware, sevDesk) würde die Bankanbindung folgendes ermöglichen:

- Automatischer MT940/CAMT.053-Import täglich
- Regelbasiertes Matching anhand Verwendungszweck, IBAN, Betrag
- Automatische Buchen nach Freigabe
- Echtzeit-Saldoanzeige in der Kanzleisoftware
- Liquiditätsplanung auf Basis offener Forderungen und Kontostand

Die Testakte simuliert diesen Zielzustand mit statischen Dateien, um den Workflow abzubilden, ohne echte Bankdaten zu verwenden.

---

## 5. Datenschutz und Datensicherheit

Die CSV-Dateien im Ordner `09_buchhaltung_konto/` enthalten ausschließlich erfundene Testdaten. In einer echten Implementierung gelten folgende Anforderungen:

- Zugriffsschutz: Bankkontodaten nur für Jana Reuter und autorisierte Personen (Steuerberater)
- Verschlüsselung: Kontoauszüge verschlüsselt ablegen (AES-256 oder vergleichbar)
- Aufbewahrung: § 147 Abs. 1 AO — 10 Jahre
- Löschung: Testdaten können jederzeit gelöscht werden; echte Daten nicht ohne Prüfung der Aufbewahrungsfrist

---

*Aktenvermerk BUCH-2026-0003 — Erstellt: 20.05.2026 — Jana Reuter, Kanzlei Reuter Rechtsanwälte, Lindenstraße 14, 10969 Berlin. Testdaten.*
