---
name: stb-dba-alle-abkommen-laendermatrix-2026
description: "DBA-Ländermatrix Deutschland 2026 nach BMF-Stand 01.01.2026. Routet alle deutschen DBA und Sonderfälle nach Staat, Region, Abkommensart, MLI, Erbschaftsteuer-DBA, Amtshilfe, Zeitraum und passendem Detail-Skill. Keine DBA-Antwort ohne konkrete Text- und Quellenprüfung."
---

# DBA-Ländermatrix 2026

## Zweck

Dieser Skill ist der Einstieg in alle DBA-Fälle, auch wenn es noch keinen länderspezifischen Einzel-Skill gibt. Er lädt bei Bedarf `references/dba-laendermatrix-2026.md`, bestimmt den Staat und zwingt danach zur konkreten DBA-Textprüfung.

## Kaltstart

1. Welche Staaten sind beteiligt?
2. Welcher Veranlagungszeitraum oder Zahlungszeitpunkt?
3. Welche Einkunftsart?
4. Natürliche Person, Kapitalgesellschaft, Personengesellschaft, Stiftung, Fonds oder Betriebsstätte?
5. Geht es um Quellensteuer, Veranlagung, Lohnsteuer, Erbschaftsteuer, Amtshilfe oder Streitbeilegung?
6. Gibt es EU/EWR-Bezug, MLI, Russland/Belarus/VAE-Status oder Alt-DBA?

## Workflow

1. Matrix öffnen und Staat zuordnen.
2. Prüfen, ob bereits länderspezifischer Skill existiert.
3. Falls ja: diesen laden und mit Matrix gegenprüfen.
4. Falls nein: `stb-dba-regionenrouter-nichteu` und `stb-dba-all-country-memo-generator` verwenden.
5. Bei Quellensteuer zusätzlich `stb-dba-quellensteuer-atlas-weltweit`.
6. Bei Doppelbesteuerung trotz DBA zusätzlich `stb-dba-map-eu-streitbeilegung`.

## Output

- DBA-Routingblatt mit Staat, Zeitraum, Abkommensart, Fundstellen-Prüfhinweis.
- Liste der anzuwendenden Artikel.
- Noch live zu prüfende Punkte.
- Empfohlene Folgeskills.

## Quellenpflicht

Keine Quellensteuersätze, Grenzgängergrenzen, Pensionsschwellen oder MLI-Wirkungen aus dem Gedächtnis. Immer DBA-Text und BMF/BZSt/OECD-Status prüfen.
