---
name: beweislast-und-offenlegung-produkthaftung
description: "Prüft Beweislast, Indizien, Offenlegung technischer Unterlagen, Kausalität und Schwierigkeiten komplexer Robotiksysteme."
---

# Beweislast und Offenlegung in der Robotik-Produkthaftung

## Fachkern: Beweislast und Offenlegung in der Robotik-Produkthaftung
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Die neue Produkthaftungs-RL VO (EU) 2024/2853 reagiert auf die Beweisnot von Geschädigten bei komplexen, vernetzten und KI-gestützten Produkten mit (i) Offenlegungspflichten technischer Unterlagen vor und im Prozess (Art. 9 RL), (ii) Vermutungen zur Fehlerhaftigkeit (Art. 10) und (iii) Vermutungen zur Kausalität (Art. 10 Abs. 4). Parallel bleibt nationales Prozessrecht (§§ 142, 144, 421-432 ZPO, § 810 BGB, § 242 BGB, Auskunfts- und Stufenklage § 254 ZPO) anwendbar. Dieser Skill bearbeitet die Tools, prioritisiert sie und gibt Schriftsatzpassagen für beide Seiten.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Geschädigter/Anspruchsteller, Hersteller-Verteidigung, Versicherer, Sachverständiger, Gericht.
2. **Vorfall:** Personen-, Sach- oder Datenschaden; Robotik-System komplex (KI, Cloud, OTA-Updates)?
3. **Zeitlicher Rahmen:** Vor oder nach 09.12.2026 (Anwendungsbeginn der neuen ProdHaftRL)?
4. **Stand:** Vorgerichtlich, vor Klage, im Prozess, Berufung?
5. **Unterlagen:** Welche technische Dokumentation, Logs, SBOM, Wartungsprotokolle sind dem Geschädigten zugänglich?

## Rechtlicher Rahmen

- **ProdHaftG** (national, vor 09.12.2026): Beweislast Geschädigter für Fehler, Schaden, Kausalität (§ 1 Abs. 4 ProdHaftG); Hersteller für Befreiungstatbestände § 1 Abs. 2 ProdHaftG.
- **VO (EU) 2024/2853 (neue ProdHaftRL)**: Art. 9 Disclosure of evidence; Art. 10 Vermutungen.
- **ZPO** §§ 142, 144 (Anordnung der Vorlage), §§ 421-432 (Urkunden), § 286 freie Beweiswürdigung.
- **§ 810 BGB** Einsicht in Urkunden bei rechtlichem Interesse.
- **§ 242 BGB** Auskunft als Nebenpflicht.
- **§ 254 ZPO** Stufenklage.
- **Data Act** VO (EU) 2023/2854 (Datenzugang bei vernetzten Produkten ab 12.09.2025) als Hilfsinstrument.
- **DSGVO** Art. 15 Auskunftsrecht.
- **§ 99 PatG / § 145a MarkenG** für Geschäftsgeheimnisschutz im Disclosure-Verfahren (GeschGehG).

## Schritt für Schritt

1. **Beweissicherung vor Klage.** Logs, Fotos, Zeugenaussagen, Sachverständigengutachten privat; Hash-Sicherung.
2. **Disclosure-Antrag** nach neuer ProdHaftRL (für Schäden ab 09.12.2026): Antrag auf Vorlage konkret bezeichneter Unterlagen, "necessary and proportionate"; Schutz von Geschäftsgeheimnissen Art. 9 Abs. 4 RL i. V. m. GeschGehG.
3. **Nationaler Hilfsweg (§ 142 ZPO).** Anordnung der Vorlage, wenn Partei darauf Bezug genommen hat; § 144 ZPO Augenschein.
4. **Vermutungen Art. 10 RL.** Bei Verletzung der Disclosure-Pflicht oder bei "übermäßiger technischer Komplexität" Vermutung des Fehlers/Kausalität.
5. **Kausalkette technisch aufbereiten.** Sensorik – Software – KI-Modell – Aktorik – Schadensereignis; Schwachstellen jedes Glieds.
6. **Sachverständigenbeweis** ZPO §§ 402 ff.: Robotik-Sachverständiger mit Forensik-Expertise.
7. **Schutz von Geschäftsgeheimnissen** im Disclosure-Verfahren: in-camera-Verfahren, Geheimhaltungsanordnung, Schwärzungen; § 16 ff. GeschGehG.
8. **Strafrechtliche Schiene** zurückhaltend: § 230 StGB fahrlässige Körperverletzung; nur wenn Indizien dies tragen.

## Trade-off-Matrix

| Schritt | Geschädigter | Hersteller | Empfehlung |
|---|---|---|---|
| Frühe Disclosure | wertvoll, kostet Aufwand | Geschäftsgeheimnis-Risiko | präzise gefasste Anträge; nicht "alles" |
| Sachverständiger | überzeugt Gericht | bestritten | gemeinsamen SV vorschlagen |
| Vergleich | begrenzt Risiko | Reputationsschutz | bei klarem Indizienbild realistisch |
| Strafanzeige | Druckmittel | Reputationsschaden | nur bei klaren Anhaltspunkten |

## Praxistipps

- **Logs sichern, bevor sie überschrieben werden** – innerhalb 24-48 h.
- **SBOM und Software-Versionsstand** zum Zeitpunkt des Vorfalls anfordern.
- **Wartungstickets** der letzten 12 Monate.
- **Update-Historie** der KI-Modelle.
- **Kommunikation mit Marktüberwachung** parallel verfolgen.

## Mustertexte

**Antrag auf Vorlage (Auszug Klageschrift):**

> Die Beklagte hat gemäß Art. 9 RL (EU) 2024/2853 i. V. m. § 142 ZPO die folgenden Unterlagen offenzulegen: (1) Risikobeurteilung des Roboters Typ X, Seriennummer Y, Stand zum [Datum des Inverkehrbringens]; (2) Logauszug vom [Datum 24h vor Vorfall] bis [Datum Vorfall+1h]; (3) SBOM und Software-Versionsstand zum Vorfallszeitpunkt; (4) Wartungstickets der vergangenen 12 Monate. Vorgeschlagen wird ein in-camera-Verfahren unter Schwärzung sensibler Geschäftsgeheimnisse gemäß §§ 16 ff. GeschGehG.

**Verteidigungsantwort (Hersteller, Auszug):**

> Die mit Klageschrift vom [Datum] beantragte Vorlage ist teilweise unverhältnismäßig: Die SBOM enthält Geschäftsgeheimnisse über Drittlieferanten. Wir bieten Vorlage in geschwärzter Fassung und Bestätigung durch unabhängige IT-Forensik (TÜV) an. Die Risikobeurteilung legen wir wie beantragt vor (Anlage B1). Bezüglich Logauszug schlagen wir eine zeitliche Eingrenzung auf 2 Stunden vor/nach dem Vorfall sowie technische Schwärzung personenbezogener Telemetrie vor.

## Typische Fehler

- **Disclosure-Antrag pauschal** ("sämtliche Unterlagen"); Gericht reduziert oder lehnt ab.
- **Logs überschrieben**, weil keine sofortige Sicherung erfolgt ist.
- **GeschGehG nicht beachtet** – im Prozess Schutzlücke.
- **Vermutungen Art. 10** nicht ausgenutzt durch Geschädigte (Komplexitäts-Argument).
- **Sachverständiger ohne Robotik-Expertise** – Gutachten wenig verwertbar.

## Querverweise

- `betreiber-mitverschulden-und-fehlbedienung`
- `deliktische-haftung-paragraph-823-bgb`
- `data-act-roboterdaten`

## Quellen Stand 06/2026

- VO (EU) 2024/2853 (neue ProdHaftRL), Art. 9, 10, 11.
- ProdHaftG.
- ZPO §§ 142, 144, 286, 402 ff., 421-432.
- § 810 BGB; § 242 BGB; § 254 ZPO.
- VO (EU) 2023/2854 (Data Act).
- GeschGehG §§ 16-20.
- VO (EU) 2024/1689 (KI-VO), Art. 12, 19 (Logs).
- Live-Verifikation auf eur-lex.europa.eu, bundesgerichtshof.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
