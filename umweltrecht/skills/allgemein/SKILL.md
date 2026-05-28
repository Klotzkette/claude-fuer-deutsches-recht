---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Umweltrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Umweltrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `esg-greenwashing-csrd` | Unternehmen muss ESG-Bericht erstellen oder verteidigt Greenwashing-Vorwurf. CSRD VO 2022/2464 gestaffelt seit 2024 ESRS-Standards Doppelte Wesentlichkeit EU-Taxonomie VO 2020/852 SFDR. Normen UWG § 5 Irreführung BGH I… |
| `klimaklagen-verbandsklage-umwrg` | Umweltverband oder Buerger klagt gegen Genehmigung oder Klimaschutz-Versaeumnis. BVerfG 1 BvR 2656/18 Klimabeschluss UmwRG §§ 1 2 Verbandsklagebefugnis KSG. Normen UmwRG § 2 BImSchG WHG UVPG EuGH Aarhus-Konvention… |
| `lksg-csddd-lieferkettensorgfalt` | Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff.… |
| `umweltrecht-abfall-circular-economy` | Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA.… |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR.… |
| `umweltrecht-compliance-schulung` | Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster… |
| `umweltrecht-emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster… |
| `umweltrecht-immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot.… |
| `umweltrecht-kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behoerdenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster… |
| `umweltrecht-naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL… |
| `umweltrecht-stoerfall-anlagen` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung… |
| `umweltrecht-transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags… |
| `umweltrecht-umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz… |
| `umweltrecht-verfahren` | Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhoerung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis… |
| `umweltrecht-wasser-bodenschutz` | Unternehmen beantragt WHG-Erlaubnis oder hat Altlastenverantwortung oder Bodenverunreinigung. Normen WHG §§ 8 9 10 12 57 BBodSchG §§ 4 9 10 12 24 BodSchV. Prüfraster Erlaubnis-Voraussetzungen Altlasten-Haftungskette… |

## Worum geht es?

Das Plugin deckt das gesamte Umweltrecht von der Anlagengenehmigung nach BImSchG ueber den Emissionshandel (TEHG), Abfallrecht und Gewaesserschutz bis hin zu Naturschutz, Artenschutz und Stoerfallanlagen ab. Es begleitet sowohl Zulassungsverfahren als auch behordliche Ueberwachung, Bussgeldverfahren und verwaltungsgerichtliche Streitigkeiten.

Hinzu kommen neuere Rechtsgebiete: ESG-Berichtspflichten nach CSRD, Greenwashing-Abwehr, Lieferkettensorgfaltspflichten nach LkSG und CSDDD sowie Klimaklagen und Verbandsklagen nach UmwRG. Zielgruppe sind Anlagenbetreiber, Unternehmensjuristen, Umweltberater und Verwaltungsrechtler.

## Wann brauchen Sie diese Skill?

- Anlagenbetreiber will BImSchG-Genehmigung beantragen, aendern oder verteidigen, oder Nachbar klagt gegen Anlage.
- Unternehmen erhalt Bussgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will Gegenvorstellung oder Einspruch einlegen.
- M&A-Transaktion: Anwalt prueft im Datenraum umweltrechtliche Risiken (Altlasten, Genehmigungsstatus, Abfall).
- ESG-Bericht muss erstellt oder ein Greenwashing-Vorwurf abgewehrt werden.
- Unternehmen ab 1.000 Mitarbeitern muss LkSG-Sorgfaltspflichten implementieren und dokumentieren.

## Fachbegriffe (kurz erklaert)

- **BImSchG** — Bundes-Immissionsschutzgesetz; regelt Genehmigung und Betrieb emittierender Anlagen.
- **TEHG** — Treibhausgas-Emissionshandelsgesetz; nationaler Rahmen fuer EU-Emissionshandel.
- **Stoerfall-Anlage (Seveso III)** — Anlage mit besonderem Gefahrenpotenzial; gesonderte Pflichten nach 12. BImSchV.
- **FFH-Vertraeglichkeit** — Pruefung nach der Fauna-Flora-Habitat-Richtlinie (RL 92/43/EWG), ob ein Vorhaben ein Natura-2000-Gebiet erheblich beeintraechtigt.
- **CSRD** — Corporate Sustainability Reporting Directive (EU); erweiterte Nachhaltigkeitsberichtspflichten gestaffelt ab 2024.
- **LkSG** — Lieferkettensorgfaltspflichtengesetz; gilt seit 01.01.2024 fuer Unternehmen ab 1.000 Mitarbeiter in Deutschland.
- **UmwRG** — Umwelt-Rechtsbehelfsgesetz; ermoeglicht anerkannten Umweltverbaenden Klagen gegen Zulassungsentscheidungen.
- **UIG** — Umweltinformationsgesetz; Recht auf Zugang zu Umweltinformationen bei Behoerden.

## Rechtsgrundlagen

- BImSchG §§ 4 5 6 10 — Genehmigungspflicht und -voraussetzungen
- TEHG §§ 4 5 7 8 9 — Emissionshandel, Zuteilung, Abgabe
- KrWG — Kreislaufwirtschaftsgesetz (Abfall)
- WHG §§ 8 9 10 12 — Wasserrecht, Erlaubnis, Bewilligung
- BBodSchG — Bundesbodenschutzgesetz, Altlasten
- BNatSchG §§ 44 45 — Artenschutzverbote und Ausnahmen
- UmwRG — Umwelt-Rechtsbehelfsgesetz
- LkSG — Lieferkettensorgfaltspflichtengesetz
- CSRD (EU) VO 2022/2464 — Nachhaltigkeitsberichtspflichten

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Anlagenbetreiber, Unternehmen mit Lieferkettenpflichten, Verband oder Nachbar?
2. Phase bestimmen: Genehmigungsantrag, laufender Betrieb, Behoerdenpruefung, Bussgeld oder Klage?
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Widerspruchs- und Klagefrist gegen Genehmigung oder Bescheid (§§ 68 ff. VwGO).
5. Anschluss-Skill bestimmen: z.B. nach Bussgeld ggf. Compliance-Schulung; nach DD ggf. Transaktionsabsicherung.

## Skill-Tour (was gibt es hier?)

- `umweltrecht-kommandocenter` — Intake-Routing: neues Umweltmandat einsortieren, Anlagenkarte erstellen, naechste Schritte bestimmen.
- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigung beantragen, anfechten oder Nachbar-Drittschutz geltend machen.
- `umweltrecht-emissionshandel-tehg` — Zuteilungsantrag, Monitoring, Abgabepflicht nach TEHG; DEHSt-Sanktion abwehren.
- `umweltrecht-abfall-circular-economy` — Abfalleigenschaft, Entsorgungspflichten, Nebenprodukt, Ende-der-Abfalleigenschaft nach KrWG.
- `umweltrecht-wasser-bodenschutz` — WHG-Erlaubnis, Altlastenverantwortung, Bodensanierung nach BBodSchG.
- `umweltrecht-naturschutz-artenschutz` — FFH-Vertraeglichkeit, Artenschutzverbote nach § 44 BNatSchG, Ausnahmen.
- `umweltrecht-stoerfall-anlagen` — Seveso-III-Compliance: Stoerfall-Meldepflicht, Sicherheitsbericht, DEHSt-Verfahren.
- `umweltrecht-transaktionen-dd` — Umwelt-Due-Diligence in M&A-Transaktionen: Genehmigungen, Altlasten, Abfall, Emissionen.
- `umweltrecht-bussgeld-sanktionen` — Umwelt-Ordnungswidrigkeiten: Bussgeld-Bescheid, Einspruch, Sanktionsvermeidung.
- `umweltrecht-verfahren` — Verwaltungsgerichtliche Verfahren: Widerspruch, Klage, Eilrechtsschutz im Umweltrecht.
- `umweltrecht-umweltinformation-uig-ifg` — UIG/IFG-Antrag stellen oder Ablehnung anfechten; Informationszugang durchsetzen.
- `umweltrecht-compliance-schulung` — Compliance-Schulungsplaene und Jahresaudit fuer Immissionsschutz- und Abfallbeauftragte.
- `lksg-csddd-lieferkettensorgfalt` — LkSG-Sorgfaltspflichten implementieren; CSDDD-Vorbereitung fuer europaische Erweiterung.
- `esg-greenwashing-csrd` — CSRD-Bericht erstellen oder Greenwashing-Vorwuerfe nach UWG und Green Claims-RL abwehren.
- `klimaklagen-verbandsklage-umwrg` — Klimaklage oder Verbandsklage nach UmwRG; BVerfG-Klimabeschluss, UmwRG-Klagebefugnis.

## Worauf besonders achten

- BImSchG-Genehmigungen sind anlagenbezogen, nicht personenbezogen; Betreiberwechsel erfordert Anzeige, kann Genehmigungspflicht ausloesen.
- LkSG-Sorgfaltspflichten gelten ab 01.01.2024 auch fuer Unternehmen ab 1.000 Mitarbeitern; Verstoss loest BAFA-Bussgelder aus.
- FFH-Vertraeglichkeitspruefung ist eigenstaendiger Schritt vor Planfeststellung; Fehler fuehren regelmaessig zur Aufhebung in der Revision.
- Emissionshandel hat harte Abgabefristen (30. April des Folgejahres); Versaeumnis loest automatische Strafzahlungen aus.
- CSRD-Berichte muessen von einem Wirtschaftspruefer oder Umweltgutachter beglaubigt werden; Fehler bei Wesentlichkeitsanalyse sind Haftungsrisiko.

## Typische Fehler

- BImSchG-Genehmigung nicht rechtzeitig geaendert: Wesentliche Aenderungen an genehmigten Anlagen beduerften gesonderter Genehmigung (§ 16 BImSchG); ungenehmigte Aenderung ist illegal.
- Altlasten in M&A-Transaktionen unterschaetzt: Bodensanierungspflicht geht auf Kaeufer ueber; kein Haftungsausschluss ohne vollstaendige DD.
- UmwRG-Klagebefugnis uebersehen: Nur anerkannte Umweltverbaende koennen nach § 3 UmwRG klagen; Private beduerften eigener Rechtsverletzung.
- Greenwashing-Aussagen ohne Substanz: EU Green Claims-Richtlinie (Entwurf) und § 5 UWG erfordern pruefbare Belege fuer Umweltaussagen.
- Verfristete LkSG-Risikoberichte: Jaehrliche Dokumentationspflicht mit gesetzlicher Frist; fehlendes Reporting loest BAFA-Massnahmen aus.

## Querverweise

- Plugin `verkehr-infrastrukturrecht` — Umweltrecht-Aspekte bei Planfeststellungsverfahren (FFH, Artenschutz).
- Plugin `aussenwirtschaft-zoll-sanktionen` — CBAM (CO2-Grenzausgleich) hat Schnittstellen zu TEHG-Emissionshandel.
- Plugin `grosskanzlei-corporate-ma` — Umwelt-DD als Kernkomponente bei Unternehmenstransaktionen.
- Plugin `patentrecherche` — Greentech-Patentportfolios bei Umwelttechnik-Mandaten ergaenzend pruefen.

## Quellen und Aktualitaet

- Stand: 05/2026
- BImSchG, TEHG, KrWG, WHG, BBodSchG, BNatSchG, UmwRG, UIG, LkSG in aktuell geltender Fassung
- CSRD (EU VO 2022/2464) gestaffelt ab 2024/2025/2026 in Kraft
