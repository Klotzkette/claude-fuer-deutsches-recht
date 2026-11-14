---
name: buchhaltung-konten-kanzlei-erechnung
description: "Für Kanzlei-Buchhaltung, Konten und Zahlungsabgleich: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Kanzlei-Buchhaltung, Konten und Zahlungsabgleich

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Geht es um Ausgangsrechnungen, Eingangsrechnungen, Fremdgeld/Anderkonto oder Bankmatching?
2. Ist eine echte Buchhaltungssoftware (DATEV, Lexware, sevDesk) angebunden oder wird im Simulationsmodus gearbeitet?
3. Sind offene Posten ueberfaellig und loest das Mahnwesen aus?
4. Werden Fremdgelder kanzleiintern von eigenen Geldern getrennt gefuehrt (§ 43a Abs. 5 BRAO)?

## Zentrale Normen
- § 43a Abs. 5 BRAO — Pflicht zur Trennung von Fremdgeld und eigenem Vermögen
- §§ 238-241 HGB — Buchfuehrungspflicht: Grundsaetze ordnungsmäßiger Buchfuehrung
- § 147 AO — Aufbewahrungspflichten für Buchungsbelege (10 Jahre)
- § 286 BGB — Verzug: Voraussetzungen und Verzugszinsen bei offenen Posten

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
