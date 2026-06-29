---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordne..."
---

# Umweltrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BImSchG § 10 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist 1 Monat, BBodSchG Sanierungsuntersuchung 1 Jahr, Störfall-Anzeige unverzüglich.
- Tragende Normen verifizieren: BImSchG, KrWG, WHG, BNatSchG, UVPG, BBodSchG, ChemG, StörfallV (12. BImSchV), TA Luft, TA Lärm, EU-IED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger, Genehmigungsbehörde, Umweltverbände (BUND, NABU), VG, OVG, BVerwG (7. Senat), EU-KOM, Sachverständige.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Immissionsschutzrechtliche Genehmigung, UVP-Bericht, FFH-Verträglichkeitsstudie, Sanierungsplan, Verbandsklage, Einwendung, TA-Luft-/TA-Lärm-Berechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Umweltrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

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

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `lksg-csddd-lieferkettensorgfalt` | Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff.… |
| `umweltrecht-abfall-circular-economy` | Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA.… |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhörung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR.… |
| `umweltrecht-compliance-schulung` | Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster… |
| `umweltrecht-emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster… |
| `umweltrecht-immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot.… |
| `umweltrecht-kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behördenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster… |
| `umweltrecht-naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL… |
| `umweltrecht-stoerfall-anlagen` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung… |
| `umweltrecht-transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags… |
| `umweltrecht-umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz… |
| `umweltrecht-verfahren` | Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhörung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis… |
| `umweltrecht-wasser-bodenschutz` | Unternehmen beantragt WHG-Erlaubnis oder hat Altlastenverantwortung oder Bodenverunreinigung. Normen WHG §§ 8 9 10 12 57 BBodSchG §§ 4 9 10 12 24 BodSchV. Prüfraster Erlaubnis-Voraussetzungen Altlasten-Haftungskette… |

## Worum geht es?

Das Plugin deckt das gesamte Umweltrecht von der Anlagengenehmigung nach BImSchG über den Emissionshandel (TEHG), Abfallrecht und Gewaesserschutz bis hin zu Naturschutz, Artenschutz und Stoerfallanlagen ab. Es begleitet sowohl Zulassungsverfahren als auch behordliche Ueberwachung, Bussgeldverfahren und verwaltungsgerichtliche Streitigkeiten.

Hinzu kommen neuere Rechtsgebiete: ESG-Berichtspflichten nach CSRD, Greenwashing-Abwehr, Lieferkettensorgfaltspflichten nach LkSG und CSDDD sowie Klimaklagen und Verbandsklagen nach UmwRG. Zielgruppe sind Anlagenbetreiber, Unternehmensjuristen, Umweltberater und Verwaltungsrechtler.

## Wann brauchen Sie diese Skill?

- Anlagenbetreiber will BImSchG-Genehmigung beantragen, ändern oder verteidigen, oder Nachbar klagt gegen Anlage.
- Unternehmen erhalt Bussgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will Gegenvorstellung oder Einspruch einlegen.
- M&A-Transaktion: Anwalt prüft im Datenraum umweltrechtliche Risiken (Altlasten, Genehmigungsstatus, Abfall).
- ESG-Bericht muss erstellt oder ein Greenwashing-Vorwurf abgewehrt werden.
- Unternehmen ab 1.000 Mitarbeitern muss LkSG-Sorgfaltspflichten implementieren und dokumentieren.

## Fachbegriffe (kurz erklaert)

- **BImSchG** — Bundes-Immissionsschutzgesetz; regelt Genehmigung und Betrieb emittierender Anlagen.
- **TEHG** — Treibhausgas-Emissionshandelsgesetz; nationaler Rahmen für EU-Emissionshandel.
- **Stoerfall-Anlage (Seveso III)** — Anlage mit besonderem Gefahrenpotenzial; gesonderte Pflichten nach 12. BImSchV.
- **FFH-Vertraeglichkeit** — Prüfung nach der Fauna-Flora-Habitat-Richtlinie (RL 92/43/EWG), ob ein Vorhaben ein Natura-2000-Gebiet erheblich beeintraechtigt.
- **CSRD** — Corporate Sustainability Reporting Directive (EU); erweiterte Nachhaltigkeitsberichtspflichten gestaffelt ab 2024.
- **LkSG** — Lieferkettensorgfaltspflichtengesetz; gilt seit 01.01.2024 für Unternehmen ab 1.000 Mitarbeiter in Deutschland.
- **UmwRG** — Umwelt-Rechtsbehelfsgesetz; ermoeglicht anerkannten Umweltverbaenden Klagen gegen Zulassungsentscheidungen.
- **UIG** — Umweltinformationsgesetz; Recht auf Zugang zu Umweltinformationen bei Behörden.

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

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Anlagenbetreiber, Unternehmen mit Lieferkettenpflichten, Verband oder Nachbar?
2. Phase bestimmen: Genehmigungsantrag, laufender Betrieb, Behördenpruefung, Bussgeld oder Klage?
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen prüfen: Widerspruchs- und Klagefrist gegen Genehmigung oder Bescheid (§§ 68 ff. VwGO).
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
- `umweltrecht-compliance-schulung` — Compliance-Schulungsplaene und Jahresaudit für Immissionsschutz- und Abfallbeauftragte.
- `lksg-csddd-lieferkettensorgfalt` — LkSG-Sorgfaltspflichten implementieren; CSDDD-Vorbereitung für europaische Erweiterung.
- `esg-greenwashing-csrd` — CSRD-Bericht erstellen oder Greenwashing-Vorwuerfe nach UWG und Green Claims-RL abwehren.
- `klimaklagen-verbandsklage-umwrg` — Klimaklage oder Verbandsklage nach UmwRG; BVerfG-Klimabeschluss, UmwRG-Klagebefugnis.

## Worauf besonders achten

- BImSchG-Genehmigungen sind anlagenbezogen, nicht personenbezogen; Betreiberwechsel erfordert Anzeige, kann Genehmigungspflicht ausloesen.
- LkSG-Sorgfaltspflichten gelten ab 01.01.2024 auch für Unternehmen ab 1.000 Mitarbeitern; Verstoss loest BAFA-Bussgelder aus.
- FFH-Vertraeglichkeitspruefung ist eigenstaendiger Schritt vor Planfeststellung; Fehler fuehren regelmaessig zur Aufhebung in der Revision.
- Emissionshandel hat harte Abgabefristen (30. April des Folgejahres); Versaeumnis loest automatische Strafzahlungen aus.
- CSRD-Berichte müssen von einem Wirtschaftspruefer oder Umweltgutachter beglaubigt werden; Fehler bei Wesentlichkeitsanalyse sind Haftungsrisiko.

## Typische Fehler

- BImSchG-Genehmigung nicht rechtzeitig geaendert: Wesentliche Änderungen an genehmigten Anlagen beduerften gesonderter Genehmigung (§ 16 BImSchG); ungenehmigte Änderung ist illegal.
- Altlasten in M&A-Transaktionen unterschaetzt: Bodensanierungspflicht geht auf Kaeufer über; kein Haftungsausschluss ohne vollstaendige DD.
- UmwRG-Klagebefugnis uebersehen: Nur anerkannte Umweltverbaende können nach § 3 UmwRG klagen; Private beduerften eigener Rechtsverletzung.
- Greenwashing-Aussagen ohne Substanz: EU Green Claims-Richtlinie (Entwurf) und § 5 UWG erfordern prüfbare Belege für Umweltaussagen.
- Verfristete LkSG-Risikoberichte: Jaehrliche Dokumentationspflicht mit gesetzlicher Frist; fehlendes Reporting loest BAFA-Maßnahmen aus.

## Quellen und Aktualitaet

- Stand: 05/2026
- BImSchG, TEHG, KrWG, WHG, BBodSchG, BNatSchG, UmwRG, UIG, LkSG in aktuell geltender Fassung
- CSRD (EU VO 2022/2464) gestaffelt ab 2024/2025/2026 in Kraft
