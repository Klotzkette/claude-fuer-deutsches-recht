---
name: forderungen-interessen-matrix
description: "Strukturierte Gegenueberstellung mehrerer Forderungen eines Mandanten gegen einen oder mehrere Schuldner. Erfasst Hauptforderung Nebenforderung Zinsen Kosten Faelligkeit Beleg Verjährung. Pinpoints ZPO 260 Klagenhaeufung ZPO 33 Aufrechnungswiderklage BGB 366 Tilgungsreihenfolge. Liefert priorisierte Liste mit Empfehlung welche Forderung zuerst klagen und welche bundeln."
---

# Forderungen-Interessen-Matrix

Wenn Mandant mehrere Forderungen gegen denselben oder verschiedene Schuldner hat braucht es eine Reihung und Bundelungs-Entscheidung.

## Matrix-Schema

| Forderung | Hauptsumme Euro | Faellig seit | Verjährung in Monaten | Beleg | Aussicht | Kostenprognose | Empfehlung |
|---|---|---|---|---|---|---|---|
| Werklohn Bauvorhaben A | 24500 | 2024-09-15 | 18 | Rechnung Abnahme | hoch | mittel | sofort Klage |
| Restkaufpreis Maschine | 8200 | 2025-03-01 | 26 | Kaufvertrag Lieferschein | hoch | gering | Mahnbescheid |
| Schadensersatz Stornogebuehr | 3100 | 2024-12-10 | 9 | E-Mail-Kette | mittel | gering | erst aussergerichtlich |
| Honorar Beratung 2022 | 4800 | 2022-10-01 | -2 verjaehrt | Rechnung | aussichtslos | hoch | nicht klagen |

## Bundelungs-Optionen

| Konstellation | Werkzeug | Norm |
|---|---|---|
| Mehrere Anspruchsgruende gegen denselben Beklagten | Objektive Klagehaeufung | ZPO 260 |
| Mehrere Beklagte aus derselben Lieferkette | Streitgenossenschaft | ZPO 59 ZPO 60 |
| Gegenforderung Beklagter | Widerklage | ZPO 33 |
| Tilgungsverrechnung bei mehreren Forderungen | Tilgungsreihenfolge | BGB 366 BGB 367 |

## Kostenmehrwert pruefen

Bundelung lohnt wenn alle Forderungen in dieselbe Zuständigkeit fallen GVG 23 oder GVG 71. Bei Mischung von AG- und LG-Forderungen kann Zusammenrechnung der Streitwerte nach ZPO 5 ein einheitliches LG-Verfahren ergeben.

## Tilgungsreihenfolge ohne Bestimmung BGB 366 Abs. 2

1. Faellige Schuld vor nicht faelliger
2. Unter mehreren faelligen die geringer gesicherte
3. Unter gleich gesicherten die laestigere
4. Bei gleicher Laestigkeit die aeltere
5. Bei gleichem Alter anteilig
6. Innerhalb einer Forderung Kosten vor Zinsen vor Hauptforderung BGB 367

## Norm-Pinpoints

- ZPO 5 Wertaddition mehrere Anspruechen
- ZPO 33 Widerklage
- ZPO 59 60 Streitgenossen
- ZPO 260 Klagenhaeufung
- BGB 366 367 Tilgung

## Quellen

- [ZPO 260](https://www.gesetze-im-internet.de/zpo/__260.html)
- [BGB 366](https://www.gesetze-im-internet.de/bgb/__366.html)
