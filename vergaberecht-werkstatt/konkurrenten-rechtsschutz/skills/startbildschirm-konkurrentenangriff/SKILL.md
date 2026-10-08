---
name: startbildschirm-konkurrentenangriff
description: 'Stellt nach der Triage des Konkurrenten-Orchestrators Fristen, Angriff, Fundstellen, Beweise, Akteneinsichtslücken, Antrag und nächste Handlung als kompaktes Dashboard dar. Kein eigenständiger Kaltstart für Ordner oder ZIP; keine neue Sachprüfung. Nutzt Sof Medica sowie OLG Düsseldorf Verg 2/24, Verg 34/20 und Verg 36/23.'
---

# Startbildschirm Konkurrentenangriff

**Arbeitsname:** Geprüfte Triage rein, klarer Streitbildschirm und nächste Handlung raus.

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Eingaben nach der Triage

Dieser Skill erhält vom `konkurrenzrechtsschutz-orchestrator` bereits geprüfte Felder: Rolle, Phase, Regime, Fristen, stärkster Angriff, Fundstellen, Belege, Kausalität, Zuschlagschance, Rechtsfolge und empfohlener Output. Fehlt eines dieser Felder, nicht selbst den Ordner neu prüfen, sondern die konkrete Triage-Lücke benennen und zum Orchestrator zurückleiten.

## Dashboard-Aufbau

1. Nur gesicherte Tatsachen und ausdrücklich markierte Hypothesen übernehmen.
2. Fristen nach Dringlichkeit sortieren; Startpunkt und Aktenbeleg sichtbar lassen.
3. Den stärksten Angriff mit Norm, Fundstelle, Beleg, Gegenargument, Kausalität und Antrag in eine Zeile verdichten.
4. Höchstens zwei Reserveangriffe anzeigen; schwache Verdachtslinien ausblenden.
5. Mit genau einer nächsten Zustellungs-, Beweis-, Akteneinsichts- oder Freigabehandlung enden.

## Bedienlogik

- Starte mit einer Ein-Bildschirm-Lage: Kurzlage, rote Fristen, stärkster Angriff, vorhandene Belege, offene Lücken, empfohlener Output.
- Biete höchstens drei Output-Optionen an und markiere genau eine Empfehlung.
- Nutze Entscheidungsfragen nur als Weiche: Rüge, VK-Antrag, Zuschlagssperre, Akteneinsicht, OLG-Beschwerde, Vergleich, Kostenmemo.
- Bei Portal-, LV- oder Systemdaten immer nächsten Bedienhandlungspunkt ausgeben: Zugangsgrund prüfen, Original sichern, Arbeitskopie/Transformation hashen, Tatsachenkern bilden, Gegenhypothese prüfen, Anlage/Schwärzung vorbereiten.
- Keine Textwüste: Jede Antwort muss eine Tabelle, Fristenampel, Belegmatrix oder einen ausformulierten Schriftsatzbaustein enthalten.

## Routing

| Lage | Skill |
| --- | --- |
| Hersteller-, Typ-, Material-, System-, Schnittstellen- oder Gleichwertigkeitsvorgabe | `produktneutralitaet-und-leistungsbeschreibung` |
| Unterlagen oder LV fehlerhaft | `unterlagen-lv-formatangriff` |
| Uploadquittung, Portalnachricht, Zeitstempel, Hash, Dateiversion, Screenshot oder Zustellnachweis betroffen | `beweisstrategie-und-portalnachweise` |
| SAP, ERP, AVA, DMS, Portal, API oder MCP als Systemquelle betroffen | `legacy-systeme-integration` |
| Bekanntmachung, Frist oder Zugang fehlerhaft | `bekanntmachung-fristen-und-zugang` |
| Rüge nötig | `ruege-konkurrent-160-gwb` |
| VK-Antrag nötig | `nachpruefungsantrag-konkurrent-vk` |
| Zuschlag droht | `eilantrag-zuschlagssperre-169` |
| Wertung oder Dokumentation fehlerhaft | `wertungsangriff-und-dokumentationsluecken` |
| Billigstes Angebot gewinnt trotz Qualitäts-, Tempo- oder Lebenszyklusrelevanz | `billigzuschlag-angreifen` |
| Konkurrent nicht geeignet oder auszuschließen | `eignungs-und-ausschlussangriff-konkurrent` |
| Akteneinsicht nötig | `akteneinsicht-schwaerzung-belegmatrix` |
| Ohne Ausschreibung, Direktauftrag, Interimsauftrag, Vertrag unterschrieben, Leistung läuft, Verlängerung, Nachtrag oder Vertragsänderung | `de-facto-vergabe-135-gwb` |
| Abhilfe, Rückversetzung, Fristverlängerung, Vergleich oder Reparatur als Einigung denkbar | `vergleich-und-abstellungsstrategie` |
| Gebühren, Streitwert, Vorschuss, Kostenerstattung, Schadensersatz oder entgangener Gewinn | `kosten-und-schadensersatzrisiko` |
| VK verloren oder OLG nötig | `sofortige-beschwerde-olg-vergabesenat` |

## Antwortstandard

```markdown
## Kurzlage
[3 Sätze: Verfahren, Stand, Angriffsziel]

## Rote Fristen
| Frist | Startpunkt | Ablauf | Beleg | Sofortmaßnahme |
|---|---|---|---|---|

## Streitdashboard
| Hebel | Beleg | Risiko | Nächster Schritt |
|---|---|---|---|

## Output-Auswahl
Empfohlen: [Rüge/Nachprüfungsantrag/Eilantrag/Akteneinsicht/OLG/Kostenmemo]
Alternativen: [maximal zwei]
```

## Ankerkarte

| Thema | Sofortanker |
|---|---|
| Typ-, Produkt-, System- oder Formatverengung | EuGH C-568/24, Sof Medica; EuGH C-424/23, DYKA Plastics |
| Bestandskompatibilität | OLG Düsseldorf Verg 2/24 als mögliche Verteidigung; funktionale Alternative und Migration belegen |
| Unterlagen-/Uploadbeweis | OLG Düsseldorf Verg 47/18; § 53 VgV und Portalvorgabe; C-534/23 P/C-539/23 P Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe |
| Wertungsdaten und begrenzter Einblick | OLG Düsseldorf Verg 34/20 und Verg 36/23 |
| Direktvergabe/Exklusivität | EuGH C-578/23, Generální finanční ředitelství |
| Gegenangriff/Rechtsschutz | EuGH C-100/12 Fastweb, C-689/13 PFE, C-497/20 Randstad Italia |
| Bestwertung statt Preisautomatismus | § 127 GWB, § 58 VgV; veröffentlichte Matrix oder konkrete Sonderregel; Mara allein trägt keinen Angriff |
| Vertragsänderung | EuGH C-282/24 Polismyndigheten, C-452/23 Fastned Deutschland, C-461/20 Advania Sverige |
| Bietergemeinschaft | GA Kokott C-268/25 nur als Schlussanträge |

## Rechtsprechungsfeste Angriffskarte

| Lage | Normen | Sofortoutput |
|---|---|---|
| Billigster hat gewonnen | §§ 127, 160 GWB, § 60 VgV; Mara nur bei konkreter Sonderregel; BGH X ZB 10/16 | Getrennter Matrix-, Sonderregel- und Niedrigpreischeck; danach Rüge-/VK-Baustein |
| Typ, Maß, Produkt, Material, Schnittstelle oder Format blockiert | § 31 VgV; Sof Medica; DYKA Plastics; Verg 2/24 | LV-Fundstelle, Unvermeidbarkeit, Anschluss-/Migrationsalternative, Gleichwertigkeitsangriff, Berichtigungsantrag |
| Beweis liegt in Portal, Akteneinsicht oder Systemexport | § 41, § 53 VgV, § 165 GWB; Instituto Cervantes nur Integritätsanker für EU-Eigenvergabe; Verg 47/18, Verg 34/20, Verg 36/23 | Herkunftszone, Original-/Arbeitskopiehash, Tatsachenkern, Gegenhypothese, Akteneinsichtsziel, Anlagenpaket |
| Direktauftrag, Interimsauftrag oder Lock-in | §§ 135, 160 GWB; C-578/23 | Frist, Exklusivität, Marktalternative, Eilantrag |
| Konkurrent wirkt ungeeignet | §§ 123 bis 125 GWB; Vossloh Laeis; C-268/25 nur Schlussanträge | Akteneinsichtsziel, Beweisbedarf, Ausschlussantrag |
| Akteneinsicht wird geschwärzt | § 165 GWB; Antea, Klaipedos, Varec | Schwärzungsangriff mit entscheidungserheblicher Information |

## Ergebnis

Immer mit einem Mini-Dashboard enden: rote Fristen, stärkster Angriff, Belege, nächster Schriftsatz, Kostenrisiko, Freigabe und nächste Datei.

## Feinschliff

Nicht nur fragen, ob der Angriff materiell richtig ist. Immer entscheiden, welcher prozessuale Hebel heute ausgelöst werden muss:

1. Rüge vor Präklusion.
2. VK-Antrag vor Zuschlag.
3. Antrag auf Zuschlagssperre oder Verteidigung gegen Gestattung.
4. Akteneinsicht mit Schwärzungs- und Replikplan.
5. OLG-Notfrist mit Beschwerdeziel, Tatsachen, Beweismitteln und anwaltlicher Unterschrift.

## Nutzungscheck

Am Schluss kurz prüfen:

1. Ist die nächste Frist berechnet oder als Lücke markiert?
2. Gibt es für jeden Angriff mindestens einen Beleg oder eine konkrete Akteneinsichtslücke?
3. Ist der beantragte Rechtsschutz eindeutig?
4. Ist klar, wer welchen Schriftsatz, welche Anlage oder welchen Upload freigibt?
