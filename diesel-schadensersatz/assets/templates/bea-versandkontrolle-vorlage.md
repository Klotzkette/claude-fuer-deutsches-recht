# beA-Versandkontrolle

## Vorgang

| Feld | Wert |
| --- | --- |
| Gericht | [OFFEN] |
| Aktenzeichen oder Neueingang | [OFFEN] |
| Parteirolle | [OFFEN] |
| Schriftsatzart | [OFFEN] |
| Frist | [OFFEN] |
| Verantwortliche Person | [OFFEN] |
| Signatur-/Versandweg | [OFFEN] |
| Paket-Fingerprint | [NACH PAKETBAU] |

## Paketabgleich

- [ ] Hauptdokument ist die anwaltlich freigegebene Endfassung.
- [ ] Rubrum, Anträge, Gericht, Aktenzeichen und Datum sind kontrolliert.
- [ ] Jede Anlagenbezugnahme hat genau eine Versanddatei.
- [ ] Jede Versanddatei steht im Anlagenverzeichnis und ist im Schriftsatz zugeordnet.
- [ ] Nummer, Stempel, Dateiname und Verzeichnis sind deckungsgleich.
- [ ] Seitenzahl, Orientierung, Lesbarkeit und OCR wurden visuell geprüft.
- [ ] Originale und Versandkopien sind getrennt; SHA-256-Werte sind dokumentiert.
- [ ] Paketauftrag, Manifest, Dateihashes und Anlagenverzeichnis sind deckungsgleich.
- [ ] `bea-paket-pruefer.py` meldet `BESTANDEN`, null Fehler und null Warnungen.

## beA-Handkontrolle

- [ ] Richtiger Empfänger und richtige Nachrichtart im beA ausgewählt.
- [ ] Aktenzeichen/Neueingang und Betreff korrekt eingetragen.
- [ ] Verantwortende Person, einfache/qES-Signatur und persönlicher Versandweg passen zusammen.
- [ ] Alle und nur die freigegebenen Dateien angehängt.
- [ ] Nach Versand automatisierte gerichtliche Eingangsbestätigung geprüft und gespeichert.
- [ ] Bestätigte Dateinamen, Empfänger, Status und Zeitpunkt stimmen mit dem Auftrag überein.

## Freigabe

**Status:** `FREIGABE_AUSSTEHEND`

Offene Punkte: [OFFEN]

Anwaltliche Freigabe durch: [OFFEN]

Datum/Uhrzeit: [OFFEN]

Die Freigabe wird in `kontrolle/freigabe.json` auf den Paket-Fingerprint gebunden. Sie ist interner Kontrollnachweis, keine elektronische Signatur und kein Versandnachweis.
