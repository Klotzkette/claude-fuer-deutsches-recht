---
name: kanzlei-allgemein-buchhaltung-konten
description: "Kanzlei-Buchhaltung mit Geschäftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang prüfen offene Posten abgleichen oder Buchhaltungsuebergabe an DATEV vorbereiten. Normen GoBD § 147 AO Aufbewahrung § 556b BGB. Prüfraster Kontenbewegungen Rechnungsalter Mahnwesen Bankmatching Klaerfaelle DATEV-Export. Output Offene-Posten-Liste Debitoren-Kreditoren-Übersicht Bankmatching-Protokoll DATEV-Übergabepaket. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-buchhaltung."
---

# Kanzlei-Buchhaltung, Konten und Zahlungsabgleich

## Triage zu Beginn
1. Geht es um Ausgangsrechnungen, Eingangsrechnungen, Fremdgeld/Anderkonto oder Bankmatching?
2. Ist eine echte Buchhaltungssoftware (DATEV, Lexware, sevDesk) angebunden oder wird im Simulationsmodus gearbeitet?
3. Sind offene Posten ueberfaellig und loest das Mahnwesen aus?
4. Werden Fremdgelder kanzleiintern von eigenen Geldern getrennt gefuehrt (§ 43a Abs. 5 BRAO)?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 5 BRAO — Pflicht zur Trennung von Fremdgeld und eigenem Vermoegen
- §§ 238-241 HGB — Buchfuehrungspflicht: Grundsaetze ordnungsmaessiger Buchfuehrung
- § 147 AO — Aufbewahrungspflichten fuer Buchungsbelege (10 Jahre)
- § 286 BGB — Verzug: Voraussetzungen und Verzugszinsen bei offenen Posten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt die operative Kanzlei-Buchhaltung als Vorbereitung: Ausgangsrechnungen, Eingangsrechnungen, offene Posten, Geschäftskonto, Zahlungseingänge, Zahlungsausgänge, Bankmatching, Mahnwesen und Klärfälle. Er bucht nicht verbindlich und löst keine Bankzahlungen aus.

## Leitplanken

- Echte Geschäftskonto-Anbindung nur nach ausdrücklicher Freigabe.
- Keine Bankzugangsdaten, TANs, PINs oder API-Secrets im Chat speichern.
- Keine Zahlungsaufträge ohne separate Freigabe.
- Keine endgültige Buchung ohne Buchhaltungs- oder Steuerkanzlei-Fachsystem.
- Fremdgeld, Anderkonto, Gerichtskosten und Auslagen getrennt prüfen.
- DATEV-ähnliche Übergabe nur als strukturierte Exportvorbereitung oder Simulation, nicht als echte DATEV-Buchung behaupten.

## Datenquellen

- Ausgangsrechnungen und E-Rechnungen.
- Eingangsrechnungen.
- Kontoauszüge, CSV, CAMT, MT940, PDF oder Bank-Screenshot.
- Zahlungsavise.
- Rechtsschutz-Zahlungen.
- Fremdgeldvermerke.
- Mahnungen und Zahlungserinnerungen.
- Storno, Gutschrift, Korrekturrechnung.

## Offene-Posten-Workflow

1. Ausgangsrechnung in Debitorenregister übernehmen.
2. Fälligkeit, Zahlungsziel und Mahnstufe setzen.
3. Alterung berechnen: nicht fällig, 0-30, 31-60, 61-90, über 90 Tage.
4. Zahlungseingänge importieren oder simulieren.
5. Matching vorschlagen.
6. Klärfälle markieren.
7. Mahnvorschlag oder Rückfrage erzeugen.
8. Zahlungsstatus an Rechnung, UStVA und GoBD-Protokoll zurückgeben.

## Matching-Regeln

Starkes Match:

- Rechnungsnummer im Verwendungszweck.
- Betrag stimmt.
- Zahler passt zu Rechnungsempfänger oder Kostenschuldner.
- Zahlung innerhalb erwarteter Frist.

Schwaches Match:

- Betrag stimmt, aber Rechnungsnummer fehlt.
- Zahler ist abweichender Dritter, Rechtsschutz oder Mandant.
- Teilzahlung.
- Sammelzahlung.
- Rundungs- oder Bankgebührenabweichung.

Klärfall:

- Betrag passt zu keiner Rechnung.
- Zahlung auf falsche Akte.
- Doppelzahlung.
- Fremdgeldverdacht.
- Rücklastschrift.
- Name ähnlich, aber unsicher.

## Geschäftskonto-Simulation

Wenn kein Bankzugang besteht:

> Das Geschäftskonto ist nicht angeschlossen. Soll ich einen Import aus CSV/CAMT/MT940 vorbereiten, eine manuelle Kontoauszugsliste nutzen oder einen simulierten Zahlungslauf für die Testakte durchführen?

Im Simulationsmodus:

- Jede Zahlung als simuliert markieren.
- Keine echte Bankverbindung behaupten.
- Keine echten Kontostände behaupten.
- Matching-Entscheidungen nur als Vorschlag ausgeben.

## Ausgabe

- `assets/templates/buchhaltung-kontoauszug.md`.
- `assets/templates/offene-posten-debitoren.md`.
- `assets/templates/zahlungseingang-matching.md`.
- `assets/templates/mahn-und-klaerfallregister.md`.
- `assets/templates/datev-uebergabe-simulation.md`.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)
