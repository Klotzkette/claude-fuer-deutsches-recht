---
name: anschlussflug-und-reiseplan
description: "Behandelt Reiseplaene mit Anschlussfluegen (Connecting Flights) und mehreren Etappen. Massgeblich ist die Ankunftsverspaetung am Endziel der Reise (EuGH C-11/11 Folkerts und C-559/16 Wegener). Pruefraster eine Buchung mit einer PNR oder mehrere Buchungen. Codeshare-Sonderfaelle. Bei Verspaetung am Anschlussflughafen die zu Verpassen des Anschlusses fuehrt — Anspruch wird nach Endziel-Verspaetung berechnet. Bei separaten Buchungen je Strecke Einzelanspruch."
---

# Anschlussflug und Reiseplan

## Grundregel — Endziel zählt

EuGH C-11/11 (Folkerts 26.02.2013) und C-559/16 (Wegener 31.05.2018):

- Bei einer **einheitlichen Buchung** mit Anschlussflug ist maßgeblich die **Verspätung am Endziel** — nicht am Anschlussflughafen.
- Anspruch besteht auch wenn der erste Flug puenktlich war aber der Anschlussflug ausfällt und das Endziel mehr als drei Stunden verspätet erreicht wird.
- Umgekehrt: erster Flug verspätet aber kurz vor der Drei-Stunden-Schwelle aber Anschluss noch erreicht — kein Anspruch.

## Prüfraster

### 1. Wie ist gebucht?

- **Eine Buchung** (ein PNR mit allen Strecken) → Reise als ein Vorgang. Anspruch nach Endzielverspätung.
- **Separate Buchungen** (verschiedene PNRs gebucht z. B. weil mit verschiedenen Plattformen) → jeder Flug für sich; bei Verpassen des Anschlusses wegen Verspätung des ersten Flugs **keine Mitversicherung** im VO 261-Sinn. Anspruch nur für den **konkret betroffenen** Flug.

### 2. Wer ist Vertragspartner?

- **Operating Carrier** (ausführendes Luftfahrtunternehmen) ist Anspruchsgegner nach VO 261/2004.
- Bei Codeshare ist das ausführende Luftfahrtunternehmen anspruchsverpflichtet (Art. 2 lit. b VO 261/2004).
- **Vermarktendes Luftfahrtunternehmen** (Marketing Carrier) ist im Allgemeinen NICHT der Anspruchsgegner nach VO 261/2004 — auch wenn der Vertrag aus dem PNR mit ihm besteht.
- Bei Streit kann der Passagier **wahlweise** auch das vermarktende Luftfahrtunternehmen nach BGB-Vertragsregeln in Anspruch nehmen — anderer Anspruch (Reisevertrag).

### 3. Wo wird die Distanz gemessen?

EuGH C-559/16 (Wegener) und C-832/18 (Airhelp / SAS): bei einheitlicher Buchung **Gesamtdistanz** vom ersten Abflugflughafen bis zum letzten Zielflughafen — auf Direktdistanz-Basis (nicht Umweg).

### Beispiel

- **Berlin BER — Madrid MAD — Buenos Aires EZE** mit einheitlicher Buchung.
- Erster Flug BER-MAD puenktlich. Anschlussflug MAD-EZE annulliert. Ersatz am nächsten Tag.
- Endzielverspätung 28 Stunden.
- Distanz BER-EZE auf Großkreis 11.940 km nicht-innergemeinschaftlich.
- Stufe 3 — 600 EUR pro Passagier.

## Reiseverträge über Reiseveranstalter

- Bei **Pauschalreise** (§§ 651a ff. BGB) zusätzliche Ansprueche gegen den Reiseveranstalter (Minderung Schadensersatz nach BGB).
- VO 261/2004 Anspruch bleibt davon unberuehrt; Anspruchsgegner bleibt operating carrier.
- Doppelanspruch (Reiseveranstalter und Airline) — Vorteilsausgleich prüfen.

## Sonderfall Umsteigen über Drittstaat

Wenn die Reise innerhalb der EU mit Umsteigen in einem **Drittstaat** stattfindet (z. B. BER-IST-VIE bei Turkish Airlines):

- VO 261/2004 gilt nach Art. 3 für den **Abflug aus der EU** auch mit Nicht-EU-Carrier.
- Anschlussflug ab Drittstaat zurück in die EU mit Nicht-EU-Carrier: **VO 261 gilt NICHT**.
- Konsequenz: nur Anspruch für Abflug-Etappe ab EU.

## Eingaben

- Buchungsbestätigung mit allen Etappen.
- PNR-Kennung pro Etappe.
- IATA-Codes der drei oder mehr Flughaefen.
- Tatsächliche Abflug- und Ankunftszeiten je Etappe.

## Ausgabe

```
Anschlussflug-Analyse
Buchung: eine PNR (ABC123) über Lufthansa
Etappen: 
  1. BER 12.05.2026 08:00 → MAD 12.05.2026 11:30 (LH 1234)
  2. MAD 12.05.2026 13:00 → EZE 13.05.2026 06:00 (LH 5678)

Stoerung:
  Etappe 2 annulliert
  Ersatz: EZE Ankunft 14.05.2026 10:00
  
Endzielverspätung: 28 Stunden
Distanz BER-EZE (Endziel): 11.940 km nicht-innergemeinschaftlich
Stufe: 3 → 600 EUR pro Passagier

Anspruchsgegner: Lufthansa (operating carrier Etappe 2)
```

## Leitentscheidungen Anschlussflug

- EuGH, Urt. v. 26.02.2013 — C-11/11 (Folkerts), NJW 2013, 1291 — Anschlussflug; massgeblich Ankunftsverspaetung am Endziel nicht am Anschlussflughafen; einheitliche Buchung entscheidend.
- EuGH, Urt. v. 31.05.2018 — C-559/16 (Wegener), NJW 2018, 2261 — Gesamtdistanz vom ersten Abflughafen bis Endziel; nicht Umwegdistanz; Grosskeiis-Rechnung.
- EuGH, Urt. v. 12.09.2013 — C-509/11 (OERVar-OAE), NJW 2013, 3086 — Codeshare-Fluege; operating carrier haftet; vermarktendes LFU haftet nicht nach VO 261/2004.
- BGH, Urt. v. 26.09.2023 — X ZR 109/22, NJW 2023, 3654 — Einheitliche Buchung bei verschiedenen PNR; tatsaechliche Verknuepfung der Fluege muss ausdruecklich erkennbar sein; Schliessung Luecke durch ergaenzende Auslegung.

## Kommentarliteratur

- Staudinger/Arnold BGB-Fluggastrechte Art. 7, 3 VO 261/2004 (Ausgleich, Anwendungsbereich)
- Grigoleit VO 261/2004 Art. 3 Rn. 10-40 (Anwendungsbereich, Buchungsvertraege)

## Hinweise

- Bei einheitlicher Buchung lohnt eine sorgfaeltige Prüfung — viele Airlines berechnen falsch.
- Bei separaten Buchungen Verlust des Anschlusses regelmäßig nicht erstattungsfähig nach VO 261 — daher bei Buchung auf Einheits-PNR achten.
