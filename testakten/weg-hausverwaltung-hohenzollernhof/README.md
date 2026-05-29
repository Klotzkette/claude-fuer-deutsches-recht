# Testakte: WEG Hohenzollernhof — Hausverwaltung unter Druck

Fiktive Testakte fuer das Plugin `weg-hausverwaltung`. Stand: 27.05.2026 (vor Eigentuemerversammlung am 17.06.2026).

Die Akte simuliert eine **realistische Berliner Mittel-WEG** mit 38 Wohnungen und 2 Gewerbeeinheiten am Hohenzollerndamm 180. Sie ist bewusst **unordentlich** und enthaelt **mehrere Fehlerquellen** (CO2-Aufteilung versaeumt, formal angreifbare Beschlussvorlagen, schlechter Verteilungsschluessel bei der geplanten Sonderumlage, Hausgeldrueckstand mit verspaeteten Mahnungen).

## Schluessel-Konflikte Stichtag 27.05.2026

1. **Balkonsanierung 12 Balkone Hofseite** — 180.000-240.000 EUR, drei Handwerker-Angebote
2. **Sonderumlage** geplant 240.000 EUR (Beirat: zu hoch, falscher Verteilungsschluessel)
3. **Steckersolar** — 5 Antraege § 20 II Nr. 5 WEG
4. **Wallbox** WE 19 Yildiz — § 20 II Nr. 2 WEG mit Antragsanspruch
5. **Hausgeldrueckstand Pasternak** WE 3 — 3.420 EUR, Mahnbescheid in Vorbereitung
6. **Heizung Buderus** — Schwankungen, ggf. Tausch (GEG-Bezug)
7. **CO2-Aufteilung 2023/2024/2025** — Verwalter hat Stufenmodell ignoriert
8. **Anwaltsschreiben Eigentuemer Mautz** — droht mit Beschlussersetzungs-Klage

## Akten-Dokumente

| Datei | Inhalt |
|-------|--------|
| `00-stammdaten.md` | Stammdaten WEG, Eigentuemerliste, Verwalterin, Beirat |
| `01-verwaltungsbeirat-notiz.md` | Beiratsnotiz mit Prioritaeten und Stimmungslage |
| `02-einladung-eigentuemerversammlung-entwurf.md` | Rohentwurf Einladung 17.06.2026 |
| `03-handwerkerangebote-balkone-und-dach.md` | Drei Handwerkerangebote (178-235 TEUR) |
| `04-jahresabrechnung-2025-rohpruefung.md` | Jahresabrechnung 2025 mit Rueckfragen |
| `05-eigentuemer-und-mieterbeschwerden.md` | Beschwerdemails, Hausordnungsstreit |
| `06-beschlussliste-alt-und-neu.md` | Beschlusssammlung |
| `07-teilungserklaerung-auszug.md` | TE-Auszuege Sondereigentum / Gemeinschaftseigentum / Sondernutzung |
| `08-verwaltervertrag-auszug.md` | Verwaltervertrag-Schluesselklauseln, Pflichtverletzungen markiert |
| `09-wirtschaftsplan-2026-entwurf.md` | Wirtschaftsplan 287.450 EUR + Sonderumlage-Varianten A/B |
| `10-beschlussvorlagen-eigentuemerversammlung.md` | Beschlussvorlagen aller TOPs der EV 17.06.2026 |
| `11-co2kostaufg-aufteilungspruefung.md` | CO2KostAufG-Stufenmodell mit Berechnung (Stufe 5 fuer Hohenzollernhof) |
| `12-anfechtungsrisiko-matrix.md` | Anfechtungs-Risiko pro TOP, BGH V ZR-Bezuege |
| `13-hausgeldmahnung-pasternak-WE3.md` | Mahnschreiben + Mahnbescheid-Entwurf |
| `14-fristen-kalender-2026.md` | Fristen-Kalender (3-Wochen-EV-Frist, Anfechtungsfristen, Sonderumlage-Raten) |
| `15-anwaltsschreiben-eigentuemer-balkone-droht-klage.md` | Drohbrief Anwalt Eigentuemer Mautz |
| `16-protokoll-eigentuemerversammlung-vergangene.md` | Protokoll EV 25.10.2024 |
| `17-wallbox-antrag-yildiz-WE19.md` | Wallbox-Antrag mit technischer Beschreibung |
| `mandant.yaml` | Mandanten-Stammdaten strukturiert |

## Verwendung mit den Skills

Diese Akte ist ideal, um die folgenden Skills aus `weg-hausverwaltung` zu testen:

- `eigentuemerversammlung-vorbereiten` (Einladung Frist 27.05.2026!)
- `einladung-tagesordnung-fristen` (3-Wochen-Frist § 24 IV WEG)
- `beschlussvorlagen-erstellen` (8 TOPs mit Risiko-Matrix)
- `beschlussanfechtung-risiko` (Risiko-Matrix pro TOP, BGH V ZR-Linie)
- `wirtschaftsplan-jahresabrechnung-28-weg` (Plan mit Sonderumlage-Variante A/B)
- `betriebskosten-nebenkostenabrechnung` (CO2-Aufteilung Stufe 5)
- `hausgeld-sonderumlage-liquiditaet` (Sonderumlage-Varianten, Verteilungs-Aenderung)
- `bauliche-veraenderungen-20-weg` (Wallbox + Steckersolar)
- `steckersolar-wallbox-barrierefreiheit` (§ 20 II Nr. 2/5 WEG)
- `handwerker-beauftragung-vergabe` (3 Angebote, Vergleich)
- `verwalterpflichten-26-27-weg` (Verwalter-Vertragsverletzungen markiert)
- `beirat-controlling-verwalter` (Beirats-Anmerkungen integriert)
- `eskalation-anwalt-amtsgericht` (Anwaltsschreiben Mautz, Klage-Drohung)
- `eigentuemerkommunikation-beschwerde` (Beschwerde-Mails)
- `beschlusssammlung-protokoll` (Beschluesse 2024 protokolliert)
- `mandat-objekt-triage` (Schluessel-Konflikt-Liste am Stichtag)

## Ziel

Die Akte ist **ohne Musterloesung** zu nutzen. Gute Tests:

- **Eigentuemerversammlung vollstaendig vorbereiten** (Einladung formgerecht, Beschlussvorlagen anfechtungssicher).
- **Anfechtungs-Risiko** der vorbereiteten Beschluesse bewerten.
- **Sonderumlage** optimal strukturieren (Verteilungs-Aenderung BGH V ZR 236/23, sachlicher Grund).
- **Wallbox- und Steckersolar-Antraege** rechtssicher beschluss-faehig machen.
- **CO2-Aufteilung** korrekt nachvollziehen und Korrektur bewirken.
- **Hausgeldrueckstand Pasternak** durch Mahnbescheid und ggf. Klage durchsetzen.
- **Verwalter-Eskalation** bei Pflichtverletzungen (CO2, Berichts-Pflicht) erwaegen.
- **Anwaltsschreiben Mautz** angemessen beantworten.

## Realismus

Die Akte ist **frei erfunden**. Namen, Adressen, Aktenzeichen, Polizei-Nummern, Bankverbindungen sind erfunden und gehoeren niemandem zu. Hohenzollerndamm 180 existiert in Berlin als gewoehnliches Wohnhaus; jegliche Aehnlichkeit mit der dortigen WEG ist unbeabsichtigt.
