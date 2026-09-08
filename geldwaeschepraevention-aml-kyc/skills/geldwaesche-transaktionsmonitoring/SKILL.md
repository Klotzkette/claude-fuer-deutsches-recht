---
name: geldwaesche-transaktionsmonitoring
description: "Untersucht auffällige Zahlungen, Teilbeträge, Rückerstattungen und Warenströme im Vergleich zum Kundenprofil. Verknüpft Kontoauszug, Vertrag und Beleg und bereitet begründete Erledigung oder zeitnahe Meldeprüfung vor."
---

# 1. Zahlungsauffälligkeit untersuchen

## 1. Zweck und Anwendungsfall

Für einen konkreten Alert oder ungewöhnlichen Zahlungslauf. Handelsbezogene Auffälligkeiten werden hier bearbeitet; kein eigener parallel laufender Einstieg.

## 2. Eingaben

Vertrag, Rechnung, Lieferbeleg, Kontoauszug und Kundenprofil. Stornos, Valuta und Buchungstag unterscheiden. Nicht aus einer Summenliste erfinden, wer tatsächlich gezahlt hat.

## 3. Ablauf

### 3.1. Zahlungsfluss rekonstruieren

Zahler, Empfänger, Zweck, Betrag, Währung, Zeit und Belegnummer aufeinander beziehen. Verbundene Teilzahlungen nach GwG Paragraf 1 Absatz 5 zusammen betrachten. Überzahlung und Rückzahlung nicht nur saldieren: Ein- und Ausgangskonten bleiben sichtbar.

### 3.2. Wirtschaftlichen Grund prüfen

Mit Kundenprofil und tatsächlicher Leistung vergleichen. Bei Warenhandel Menge, Einzelpreis, Lieferort, Vertragspartner und Transportdokument kontrollieren. Rechnungsberichtigung, Konzernzahlung oder Rückabwicklung können erklärbar sein, brauchen aber Belege. Kein Verdacht allein aufgrund internationaler Tätigkeit.

### 3.3. Verdacht rechtzeitig abzweigen

Ungewöhnliche komplexe Transaktion nach Paragraf 15 gesondert untersuchen. Sobald Tatsachen im Sinne des Paragraf 43 vorliegen, nicht auf eine abgeschlossene interne Untersuchung warten. [Meldeprüfung](../aml-verdachtsmeldung-fiu-leitfaden/SKILL.md) übernimmt; keine Rückzahlung auf ein neu genanntes Drittkonto als automatische „Bereinigung“.

## 4. Quellenpflicht

GwG Paragraf 10 Absatz 1 Nummer 5, Paragraf 15, Paragraf 43 und [Rechtsstand](../../references/rechtsstand-2026-und-eu-uebergang.md). Institutsbezogene Vorschriften wie KWG Paragraf 25h nur bei passender Verpflichtetenkategorie anwenden.

## 5. Ausgabeformat

Ausformulierter Zahlungsbefund mit chronologischer Tabelle, Beleg, plausibler Erklärung, Gegenbefund und offener Handlung. Times New Roman 11 pt, dezimale Gliederung. Keine Risikopunktzahl als alleinige Entscheidung.

## 6. Beispiele

Drei Baranzahlungen gehören zu einer Maschine; eine zusätzliche Überweisung stammt von einem anderen Unternehmen. Zusammengehörigkeit, Empfänger und gewünschte Rückerstattung aus den Originalen rekonstruieren.
