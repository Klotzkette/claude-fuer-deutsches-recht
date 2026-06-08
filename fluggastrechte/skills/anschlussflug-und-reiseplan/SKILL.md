---
name: anschlussflug-und-reiseplan
description: "Prüfungslinie für anschlussflug und reiseplan im Fluggastrechte: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Anschlussflug und Reiseplan

## Grundregel — Endziel zählt

Maßgeblich ist die st. Rspr. des EuGH (Volltext jeweils auf curia.europa.eu vor Versand aufrufen):

- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — bei einheitlicher Buchung mit Anschlussflug ist die Verspätung am Endziel maßgeblich.
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — auch bei Anschlussflügen mit teilweisem Abflug außerhalb der EU.
- EuGH, Urt. v. 11.7.2019, C-502/18 (CS Flug) — bestätigend.

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

- Bei Anschlussflug mit einheitlicher Buchung: Distanz vom Abgangsort bis zum Endziel auf Großkreis-Linie (Art. 7 Abs. 1 i.V.m. Art. 5 ff. VO 261/2004).
- Konkretisierende EuGH-Linie: EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) und EuGH, Urt. v. 7.9.2017, C-559/16 — Volltext auf curia.europa.eu prüfen.

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

## Leitentscheidungen Anschlussflug (Stand Mai 2026)

Verifiziert mit Quelle curia.europa.eu (Volltext jeweils vor Versand aufrufen):

- EuGH, Urt. v. 26.2.2013, C-11/11 (Folkerts) — Endziel-Verspätung maßgeblich; auch wenn Hauptflug pünktlich war.
- EuGH, Urt. v. 31.5.2018, C-537/17 (Wegener) — einheitliche Buchung Anschluss in Drittstaat.
- EuGH, Urt. v. 11.7.2019, C-502/18 (CS Flug) — Anschlussflug-Konstellationen.
- EuGH, Urt. v. 21.12.2021, C-146/20, C-188/20, C-196/20 — Vorverlegung als Annullierung.
- EuGH, Urt. v. 9.1.2025, C-394/23 — bestätigend für Vorverlegung.
- EuGH, Urt. v. 16.10.2025, C-399/24 — Blitzschlag als außergewöhnlicher Umstand.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Hinweise

- Bei einheitlicher Buchung lohnt eine sorgfaeltige Prüfung — viele Airlines berechnen falsch.
- Bei separaten Buchungen Verlust des Anschlusses regelmäßig nicht erstattungsfähig nach VO 261 — daher bei Buchung auf Einheits-PNR achten.
