---
name: fluggastrechte-anlagen-bauen
description: "Für Fluggastrechte-Anlagen bauen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Fluggastrechte-Anlagen bauen

Dieser Skill baut aus den Belegen eines Fluggastrechte-Mandats ein Anlagenpaket, das zum Forderungsschreiben, zur Mahnung oder zur Klage vor dem Amtsgericht passt. Er achtet darauf, dass die Anlagen die Anspruchsvoraussetzungen aus der Fluggastrechte-VO tragen: Buchung, betroffener Flug, Ankunftsverspaetung oder Annullierung, Entfernung, Airline-Zustaendigkeit, Abtretung oder Vollmacht und vorgerichtliche Korrespondenz.

## Normenanker

- Art. 5, 6, 7, 8, 9 und 14 VO (EG) Nr. 261/2004.
- Art. 3 VO (EG) Nr. 261/2004 fuer Anwendungsbereich, Abflugort und ausfuehrendes Luftfahrtunternehmen.
- §§ 253, 130a ZPO fuer Klageschrift und elektronische Einreichung.
- § 294 ZPO nur bei glaubhaft zu machenden Nebenpunkten, nicht als Ersatz fuer substantiierten Vortrag.

## Arbeitsgang

1. Ordne zuerst die Kernbelege: Buchungsbestaetigung, Ticket oder Boardingpass, Flugstatus, Verspaetungsnachweis, Airline-Schreiben.
2. Fuege danach Nebenbelege hinzu: Mehrkosten, Hotel, Verpflegung, Taxi, Ersatzflug, Abtretung, Vollmacht.
3. Vergib die Anlagen in der Reihenfolge, in der der Schriftsatz sie nennt.
4. Nutze `werkzeuge/build_fluggast_anlagen.py`, wenn Dateien lokal vorliegen und gestempelt oder zu einem Sammel-PDF verbunden werden sollen.

## Ergebnis

Gib eine Anlagenmatrix aus und nenne fehlende Belege konkret. Wenn der Anspruch noch nicht belegbar ist, wird kein fertiges Anlagenpaket behauptet, sondern eine Nachforderungsliste erstellt.
