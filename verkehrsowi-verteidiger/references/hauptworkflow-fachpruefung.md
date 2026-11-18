# Verkehrsbußgeld bis zur konkreten Verteidigungsschrift bearbeiten – Fachprüfung und Rechtsprechung

Die Fachrouten führen von Zustellung, Fahrerzuordnung und Messinformationen zur konkreten Verteidigungsentscheidung und trennen Geldbuße, Fahrverbot und Strafvorwurf.

# VerkehrsOWi-Verteidiger — Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen; Verjährung nach Delikt und anwendbarer Fassung (aktuell § 26 Abs. 3 StVG grundsätzlich 6 Monate bei § 24 Abs. 1, §§ 31–33 OWiG); Fahrverbot § 25 Abs. 2, 3 und 6 StVG (grundsätzlich spätestens 1 Monat nach Rechtskraft wirksam, Viermonatsprivileg nur bei erfüllten Voraussetzungen; Verbotsfrist gesondert); § 79 OWiG Rechtsbeschwerde 1 Woche. Historische Fassung und Übergang prüfen; [amtlich belegte Einzelheiten](verkehrsowi-leitplanken.md).
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, 26a, OWiG §§ 17, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessEG/MessEV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB und zuständige Eichbehörde (unterschiedliche Aufgaben).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofort-Triage bei Mandatsaufnahme

**Drei kritische Fragen zuerst:**

1. **Fristlage:** Wann wurde der Bussgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG: 2 Wochen ab Zustellung.
 - Frist offen → Einspruch sofort, dann vertiefen
 - Frist abgelaufen → Wiedereinsetzung § 52 OWiG prüfen

2. OWi und Straftat nach sämtlichen Merkmalen unterscheiden; auch ein Geschwindigkeitsvorgang kann zusätzliche Straftatmerkmale aufweisen. Straftatverdacht wegen Fahruntüchtigkeit anhand Fahrzeugart, Substanz, Befund und Ausfallerscheinungen gesondert prüfen; keine universelle Grenzwertabkürzung.

3. **Fahrverbot oder Fahrerlaubnis-Entzug?** — § 25 StVG (OWi: 1-3 Monate, bleibt Fahrerlaubnis) vs. § 69 StGB (Strafrecht: Entziehung mit Sperrfrist).

## Ampel-Schnelldiagnose

| Situation | Ampel | Maßnahme |
|-----------|-------|-----------|
| Frist laeuft in < 3 Tagen | ROT | Einspruch SOFORT, dann vertiefen |
| Frist laeuft in 4-7 Tagen | GELB | Einspruch und Akteneinsicht parallel |
| Frist > 7 Tage | GRUEN | Strukturierte Bearbeitung |
| Frist abgelaufen, Wiedereinsetzungsgrund | GELB | § 52 OWiG Antrag |
| Strafrecht (§ 316 StGB) statt OWi | ROT | Subskill Strafrecht wechseln! |

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Einspruchsfrist berechnen + einlegen | `verkehrsowi-fristen-einspruch` |
| Akteneinsicht Messakte anfordern | `verkehrsowi-akteneinsicht-messakte` |
| Messverfahren-Angriffspunkte prüfen | `verkehrsowi-messverfahren-geschwindigkeit` |
| Beweisverwertung standardisiert | `verkehrsowi-beweisverwertung-standardisiert` |
| Alkohol / Drogen § 24a StVG | `verkehrsowi-alkohol-drogen-24a` |
| Fahreridentifizierung | `verkehrsowi-fahreridentifizierung` |
| Anhörung / Bussgeldbescheid-Prüfung | `verkehrsowi-anhoerung-bussgeldbescheid` |
| Haertefall Fahrverbot | `verkehrsowi-haertefall-fahrverbot` |
| Punkte in Flensburg | `verkehrsowi-punkte-fahrverbot-flensburg` |
| Hauptverhandlung Amtsgericht | `verkehrsowi-hauptverhandlung-amtsgericht` |
| Rechtsbeschwerde | `verkehrsowi-rechtsbeschwerde` |
| Zeugen Polizei Strategie | `verkehrsowi-zeugen-polizei-strategie` |
| Rotlicht Abstand Handy | `verkehrsowi-rotlicht-abstand-handy` |
| Verjährung Zustellung | `verkehrsowi-verjaehrung-zustellung` |
| Mandantenkommunikation | `verkehrsowi-mandantenkommunikation` |
| Quality Gate | `verkehrsowi-quality-gate` |

## Zentrale OWi-Normen im Überblick

- **§ 24 StVG** — Ordnungswidrigkeiten im Strassenverkehr allgemein
- **§ 24a StVG** — Alkohol (0,5 Promille) und Drogen
- **§ 25 StVG** — Fahrverbot 1-3 Monate
- **§ 26 StVG** — Zuständigkeit Bussgeldbehoerde
- **§ 67 OWiG** — Einspruch 2-Wochen-Frist
- **§ 77 OWiG** — Beweisaufnahme, Sachverstaendige
- **§ 79 OWiG** — Rechtsbeschwerde
- **§ 4 BKatV** — Regelfahrverbot und Abweichung bei Haertefall
- **Art. 2 Abs. 1 in Verbindung mit Art. 20 Abs. 3 GG** — faires Verfahren und Zugang zu vorhandenen verteidigungsrelevanten Informationen; **Art. 103 Abs. 1 GG** — rechtliches Gehör

## Querschnitts-Rechtsprechung

Die untenstehenden vollständigen Quellenkarten ersetzen verkürzte Fundstellen ohne Datum und Aktenzeichen. Vorhandene Informationen, technische Nichtspeicherung und konkreten Messfehler getrennt prüfen.

## Harte Leitplanken

- OWi vs. Strafrecht immer zuerst klären — falsche Qualifikation ist schwerer Fehler.
- Fristwahrung priorisieren, soweit Einspruch beauftragt und fristlich erforderlich ist; Akteneinsicht und beauftragte Prüfung können parallel erfolgen.
- Tatsächlich vorhandene, verteidigungsrelevante Messinformationen konkret anfordern.
- Anwaltliche Endkontrolle bei allen Fristen und Antraegen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

## Rechtsprechung für die entscheidenden Abzweigungen

Aktuell nachgeprüfte Normpunkte (amtlicher Text am 18.11.2026 gelesen):

- [StVG § 26a](https://www.gesetze-im-internet.de/stvg/__26a.html): Ermächtigungsgrundlage des Bußgeldkatalogs liegt im StVG, nicht in einem § 26a OWiG.

Die folgenden Anker sind Arbeitsmaterial für die jeweils bezeichnete Streitfrage. Übernommene Quellen gelten nicht allein durch diese Überarbeitung als erneut oder tagesaktuell geprüft. Bei tragendem Einsatz Fassung, Verfahrensstand, Sachverhaltsvergleich und zwischenzeitliche Entwicklung verifizieren. Pressemitteilung, Nichtannahme und Eilentscheidung nicht zu einem umfassenden Hauptsacherechtssatz erweitern.

### 1. BVerfG, Beschluss vom 12.11.2020, 2 BvR 1616/18, Randnummern 50 bis 60

[Primär-/Fundquelle](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2020/11/rk20201112_2bvr161618.html).

Anwendung: Zugang zu behördlich vorhandenen Informationen außerhalb der Bußgeldakte bei sachlichem und zeitlichem Bezug und möglicher Verteidigungsrelevanz, ohne schon einen Messfehler beweisen zu müssen.

Grenze: Keine beliebige Ausforschung; Drittinteressen und Verfahrensstand beachten. Informationszugang nicht mit gerichtlicher Aufklärungspflicht oder Datenerzeugung gleichsetzen.

Quellenstatus: Aus vorhandener dokumentierter Primärquellenprüfung übernommen; in dieser Überarbeitung nicht erneut vollständig geprüft. Herkunft: `quality/evals/verkehrsowi-verteidiger.json`.

### 2. BVerfG, Beschluss vom 20.06.2023, 2 BvR 1167/20, Randnummern 48 bis 54

[Primär-/Fundquelle](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2023/06/rk20230620_2bvr116720.html).

Anwendung: Vorhandene und technisch nicht gespeicherte Daten unterscheiden; ein Anspruch auf Erzeugung und Speicherung folgt nicht ohne weitere Darlegung aus dem Zugang zu vorhandenen Informationen.

Grenze: Nichtannahme wegen unzureichender Darlegung, keine allgemeine Sachentscheidung zum Ausschluss jeder Speicherungspflicht und kein automatisches Verwertungsverbot.

Quellenstatus: Aus vorhandener dokumentierter Primärquellenprüfung übernommen; in dieser Überarbeitung nicht erneut vollständig geprüft. Herkunft: `quality/evals/verkehrsowi-verteidiger.json`.

### 3. BGH, Beschluss vom 02.07.2026 – 4 StR 235/25, Tenor und Rn. 22–35

[Primär-/Fundquelle](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Strafsenate/4_StS/2025/4_StR_235-25.pdf?__blob=publicationFile&v=1).

Anwendung: Nichtspeicherung von Rohmessdaten einer standardisierten Geschwindigkeitsmessung begründet für sich weder Fairnessverstoß noch Beweisverwertungsverbot. Vorhandene Unterlagen und konkrete Messfehler weiter prüfen.

Grenze: Zugang zu vorhandenen Informationen bleibt gesondert; gezielte Datenunterdrückung hat der Senat in Rn. 32 offengelassen. Kein Freibrief für fehlerhafte Gerätebedienung.

Quellenstatus: Aus vorhandener dokumentierter Primärquellenprüfung übernommen; in dieser Überarbeitung nicht erneut vollständig geprüft. Herkunft: `quality/evals/verkehrsowi-verteidiger.json`.

### 4. BVerfG, Kammerbeschluss vom 17. Mai 2024, 2 BvR 1457/23, Rn. 9 bis 16

[Primär-/Fundquelle](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2024/05/rk20240517_2bvr145723.html).

Anwendung: Bei Verkehrsordnungswidrigkeiten den Fahrerbeweis unabhängig von der Haltereigenschaft würdigen.

Grenze: Entscheidung zum konkreten Willkürfall; keine allgemeine Aussage, dass Fotos oder Indizien niemals genügen.

Quellenstatus: Vorhandener dokumentierter Primäranker; Anwendung hier fachlich eingegrenzt, keine neue Volltextprüfung. Herkunft: `quality/evals/richter-bverfg-verfassungsbeschwerden.json`. Vorher dokumentierter Prüfzeitpunkt: 2026-09-22.

