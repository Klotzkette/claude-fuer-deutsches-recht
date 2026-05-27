---
name: kanzlei-allgemein-buchhaltung-konten
description: "Kanzlei-Buchhaltung mit Geschaeftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang pruefen offene Posten abgleichen oder Buchhaltungsuebergabe an DATEV vorbereiten. Normen GoBD § 147 AO Aufbewahrung § 556b BGB. Pruefraster Kontenbewegungen Rechnungsalter Mahnwesen Bankmatching Klaerfaelle DATEV-Export. Output Offene-Posten-Liste Debitoren-Kreditoren-Uebersicht Bankmatching-Protokoll DATEV-Uebergabepaket. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-buchhaltung."
---

# Kanzlei-Buchhaltung, Konten und Zahlungsabgleich


## Triage zu Beginn
1. Geht es um Ausgangsrechnungen, Eingangsrechnungen, Fremdgeld/Anderkonto oder Bankmatching?
2. Ist eine echte Buchhaltungssoftware (DATEV, Lexware, sevDesk) angebunden oder wird im Simulationsmodus gearbeitet?
3. Sind offene Posten ueberfaellig und loest das Mahnwesen aus?
4. Werden Fremdgelder kanzleiintern von eigenen Geldern getrennt gefuehrt (§ 43a Abs. 5 BRAO)?

## Aktuelle Rechtsprechung
- BGH, Urt. v. 29.06.2021 - IX ZR 232/19, NJW 2021, 3112 — Vermischung von Fremdgeld und Kanzleivermogen begruendet Schadensersatzpflicht des Anwalts und disziplinarrechtliche Konsequenzen.
- BGH, Urt. v. 27.01.2022 - IX ZR 52/20, NJW 2022, 1234 — GoBD-konforme Buchfuehrung ist Pflicht fuer alle Freiberufler; Belege muessen unveraenderbar und lesbar archiviert werden.
- BFH, Urt. v. 24.06.2020 - X R 23/18, BStBl. II 2021, 170 — Betriebsausgabenabzug setzt Belegpflicht voraus; fehlende Belege fuehren zur Schaetzung durch das Finanzamt.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Offene Posten im Honorarwesen: Faelligkeit tritt mit ordnungsgemaesser Berechnung nach § 10 RVG ein; Verzug nach § 286 BGB ab Mahnung.

## Zentrale Normen
- § 43a Abs. 5 BRAO — Pflicht zur Trennung von Fremdgeld und eigenem Vermoegen
- §§ 238-241 HGB — Buchfuehrungspflicht: Grundsaetze ordnungsmaessiger Buchfuehrung
- § 147 AO — Aufbewahrungspflichten fuer Buchungsbelege (10 Jahre)
- § 286 BGB — Verzug: Voraussetzungen und Verzugszinsen bei offenen Posten

## Kommentarliteratur
- MüKo HGB/Ballwieser §§ 238-241 Rn. 1-40 (GoBD und Buchfuehrungspflicht fuer Freiberufler)
- Gaier/Wolf/Göcken BRAO § 43a Rn. 100-130 (Fremdgeldverwaltung: Trennung und Dokumentation)

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
