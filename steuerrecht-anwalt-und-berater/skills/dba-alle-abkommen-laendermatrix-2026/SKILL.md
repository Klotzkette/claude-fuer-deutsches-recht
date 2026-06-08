---
name: dba-alle-abkommen-laendermatrix-2026
description: "DBA-Ländermatrix Deutschland 2026 nach BMF-Stand 01.01.2026. Routet alle deutschen DBA und Sonderfälle nach Staat, Region, Abkommensart, MLI, Erbschaftsteuer-DBA, Amtshilfe, Zeitraum und passendem Detail-Skill. Keine DBA-Antwort ohne konkrete Text- und Quellenprüfung."
---

# DBA-Ländermatrix 2026

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DBA-Ländermatrix 2026` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill ist der Einstieg in alle DBA-Fälle, auch wenn es noch keinen länderspezifischen Einzel-Skill gibt. Er lädt bei Bedarf `references/dba-laendermatrix-2026.md`, bestimmt den Staat und zwingt danach zur konkreten DBA-Textprüfung.

## Einstieg

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

## Praktiker-Tipps "Schnell zum Bescheid"

- **Matrix als Ausgangspunkt, DBA-Text als Endpunkt**: nie eine Mandantenanfrage allein auf Basis der Matrix beantworten — DBA-Text in der BGBl-II-Fundstelle ist verbindlich. Im Memo immer BGBl-Stelle nennen.
- **Schnellnavigation auf bundesfinanzministerium.de**: "Internationales Steuerrecht > Doppelbesteuerung > Liste der Staaten mit DBA" — pro Land PDF zum Originaltext + Aenderungsprotokolle + Konsultationsvereinbarungen.
- **MLI-Status getrennt zum DBA pruefen**: OECD-MLI-Matching-Database (oecd.org/tax/treaties/mli-matching-database.htm) zeigt, welche Klauseln des MLI bei einem konkreten DBA durchschlagen. Wirksamkeitsdatum pro Norm separat.
- **Russland-Suspendierung 30.12.2023**: bis auf weiteres keine BZSt-Entlastung; Memo entsprechend kennzeichnen (siehe `stb-dba-russland-suspendierung-2024`).
- **VAE und Saudi-Arabien**: kein umfassendes DBA (kuendigung VAE 31.12.2021; Saudi-Arabien nicht im Einkommensteuer-DBA-Netz). Nur Spezialabkommen pruefen.
- **Belarus / Iran / Syrien**: Sanktionsrechtliche Beschraenkungen (EU-Sanktionsregimes) gehen DBA vor — pruefen.
- **Ehemalige UdSSR-Staaten**: einzelne DBA mit Fortwirkung (Russland, Ukraine, Belarus, Kasachstan, Usbekistan, Aserbaidschan etc.); pruefen, ob nationales Recht der Fortwirkung folgt.
- **Ehemalige Jugoslawien-Staaten**: Fortwirkung Jugoslawien-DBA für Bosnien-Herzegowina, Nordmazedonien, Kosovo; eigene DBA für Slowenien, Kroatien, Serbien-Montenegro, Albanien — Fortgeltung im Einzelfall.

## Trade-off-Tabelle

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Allgemeiner Skill (dieser) vs. Landeseinzel-Skill | Routing ueber Matrix; Hinweis auf live Pruefung | Detail-Skill mit Subsumtion | bei vorhandenem Landeseinzel-Skill immer diesen vorziehen |
| Drittstaat ohne aktuellen DBA-Text | Memo mit "kein DBA / DBA suspendiert" pruefen | Fachmodul (Russland, Belarus, VAE) | bei Sonderlagen Fachmodul nutzen |
| MLI-modifiziertes DBA vs. unmodifizierter DBA-Text | OECD-MLI-Synopse abrufen | nur DBA-Text | bei Veranlagungszeitraum ab 2019/2020 stets MLI-Synopse abrufen |

## Was Reviewer/Pruefer triggert

- **Memo schreibt "DBA gilt", ohne BGBl-Stelle zu nennen**.
- **MLI-Status nicht erwaehnt**, obwohl beide Staaten ratifiziert haben und Wirksamkeitsdatum erreicht ist.
- **Fortwirkungs-DBA (UdSSR/Jugoslawien) nicht geprueft** bei Nachfolgestaaten.
- **Suspendierung Russland uebersehen** für Veranlagungszeitraeume ab 2024.
- **Sanktionsrecht (EU, US-OFAC, BAFA) nicht beruecksichtigt** bei Iran, Belarus, Russland.
- **Erbschaftsteuer-DBA mit Einkommensteuer-DBA verwechselt** — getrennte Abkommensreihen.
- **EU/EWR-Status falsch**: Norwegen/Island/Liechtenstein sind EWR, aber nicht EU — MTRL/ZinsLizenzRL gelten nicht direkt.

## Routing-Beispiel (Mustertabelle)

| Mandanten-Frage | Staat | Einkunftsart | Empfohlener Skill (Hauptpfad) | Querverweis |
|---|---|---|---|---|
| GmbH zahlt Dividende an US-Holding | USA | Dividenden | `stb-dba-usa-1989-protokoll-2006` | `stb-dba-dividenden-quellensteuer-art-10`, `stb-dba-quellensteuer-erstattung-bzst-50c-estg` |
| Grenzgaenger CH mit 70 Home-Office-Tagen | Schweiz | Arbeitslohn | `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` | `stb-dba-home-office-pandemie-folgeregelung` |
| Lizenz von DE an irische Konzerngesellschaft | Irland | Lizenzen | `stb-dba-irland` | `stb-dba-lizenzgebuehren-art-12-bzst` |
| Rente Wohnsitz Portugal NHR | Portugal | Pensionen | `stb-dba-portugal` | `stb-dba-rentner-pensionen-art-18` |
| BS-Bauausfuehrung Tuerkei | Tuerkei | Unternehmensgewinn | `stb-dba-tuerkei-2011` | `stb-dba-betriebsstaette-art-5-musterabkommen` |
| Drittland ohne Fachmodul (z.B. Mexiko) | Mexiko | Diverse | `stb-dba-regionenrouter-nichteu` + `stb-dba-all-country-memo-generator` | DBA-Text bundesfinanzministerium.de |

## Output (erweitert)

- **DBA-Routingblatt**: Staat, Zeitraum, Abkommensart, BGBl-Stelle, MLI-Status, Fortwirkung.
- **Liste der anzuwendenden Artikel** mit Verweis auf Originaltext.
- **Noch live zu pruefende Punkte**: BMF-Schreiben, MLI-Notifications, Konsultationsvereinbarungen.
- **Empfohlene Folgeskills** (Hauptpfad + Querskill).
- **Warnhinweis** bei Sanktionsrechts-Bezug, Suspendierung, Fortgeltung.

## Konkretes Routingbeispiel: Verfahrensweg pro Konstellation

| Sachverhaltstyp | Erste Anlaufstelle (Skill) | Querverweis |
|---|---|---|
| Quellensteuer-Erstattung | `stb-dba-quellensteuer-erstattung-bzst-50c-estg` | `stb-dba-dividenden-quellensteuer-art-10`, `stb-dba-lizenzgebuehren-art-12-bzst` |
| BS im Ausland | `stb-dba-betriebsstaette-art-5-musterabkommen` | Land-Skill, `stb-dba-methodenartikel-anrechnung-vs-freistellung` |
| Wegzug § 6 AStG | `stb-dba-ansaessigkeit-tie-breaker-rules` | Land-Skill, `stb-dba-rentner-pensionen-art-18` |
| Doppelbesteuerung trotz DBA | `stb-dba-map-eu-streitbeilegung` | `stb-dba-grundprinzip-oecd-musterabkommen` |
| Hybridgesellschaft (LLC, LP) | `stb-dba-edge-cases-playbook` | Land-Skill, `stb-dba-grundprinzip-oecd-musterabkommen` |
| Home-Office-Grenzgaenger | `stb-dba-home-office-pandemie-folgeregelung` | Land-Grenzgaenger-Skill |
| Kuenstler/Sportler-Auftritt | `stb-dba-kuenstler-sportler-art-17-ma` | `stb-dba-quellensteuer-erstattung-bzst-50c-estg` |
| Drittstaat ohne Fachmodul | `stb-dba-regionenrouter-nichteu` + `stb-dba-all-country-memo-generator` | `stb-dba-quellensteuer-atlas-weltweit` |

## Vorgehen bei nicht gefundenen Fachmodule

1. **Matrix abrufen** und Staat eintragen.
2. **DBA-Text** ueber bundesfinanzministerium.de beziehen.
3. **MLI-Status** ueber OECD-Matching-Database pruefen.
4. **Regionenrouter-Skill** als Pfad B nutzen.
5. **All-Country-Memo-Generator** für das Memo selbst.
6. **Querverweis auf relevante Querschnitts-Skills** (Methodenartikel, Quellensteuer, MAP).

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
