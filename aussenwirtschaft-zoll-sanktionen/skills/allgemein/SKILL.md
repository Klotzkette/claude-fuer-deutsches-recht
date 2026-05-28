---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Aussenwirtschaft, Zoll und Sanktionen — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Aussenwirtschaft Zoll Sanktionen**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen.

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
| `aussenwirtschaft-aml-kyc-sanktionen` | Verknuepft GwG-Risikoanalyse KYC Sanktionsscreening und interne Kontrollpflichten im Aussenhandel. Anwendungsfall Exporteur oder Haendler braucht integriertes AML- und Sanktions-Compliance-System für… |
| `aussenwirtschaft-antidumping-ausgleich` | Antidumping Antisubvention und Ausgleichsmassnahmen im EU-Aussenhandelsrecht. Anwendungsfall Import- oder Exporteur ist von Antidumping-Massnahmen betroffen oder will Erstattungsantrag stellen. Normen… |
| `aussenwirtschaft-awv-bundesbank` | Meldepflichten nach Aussenwirtschaftsverordnung AWV gegenüber Bundesbank für grenzüberschreitende Zahlungen und Beteiligungen. Anwendungsfall Unternehmen hat Zahlungen ins Ausland oder Auslandsforderungen und prüft… |
| `aussenwirtschaft-bafa-genehmigungen` | BAFA-Genehmigungsverfahren für Exporte und Dienstleistungen mit Genehmigungspflicht. Anwendungsfall Exporteur braucht BAFA-Ausfuhrgenehmigung für gueterlistenpflichtige Ware oder Technologie. Normen § 8 AWG… |
| `aussenwirtschaft-cbam-co2-zoll` | Carbon Border Adjustment Mechanism CBAM CO2-Grenzausgleich für Einfuhren aus Drittlaendern. Anwendungsfall Unternehmen importiert CBAM-pflichtige Waren Stahl Aluminium Zement Duenger Strom und muss CBAM-Pflichten… |
| `aussenwirtschaft-exportkontrolle-dual-use` | Exportkontrolle Dual-Use-Prüfung für Gueter Software Technologie und Dienstleistungen mit Doppelverwendungszweck. Anwendungsfall Exporteur prüft ob Ware oder Software unter Dual-Use-Regulierung faellt und Genehmigung… |
| `aussenwirtschaft-gueterlisten-klassifizierung` | Klassifizierungsdossier für Exportkontrolle Zolltarif und Dual-Use-Einordnung. Anwendungsfall Produkt muss für Exportkontrolle und Zoll einheitlich klassifiziert werden. Normen EU-Dual-Use-Liste Anhang I Verordnung… |
| `aussenwirtschaft-icp-kontrollsystem` | Entwurf und Haertung eines integrierten Compliance-Programms ICP für Exportkontrolle Zoll Sanktionen CBAM und AML. Anwendungsfall Unternehmen will rechtssicheres ICP aufbauen oder bestehendes System haerten. Normen AWG… |
| `aussenwirtschaft-kommandocenter` | Kommandocenter für alle Aussenhandels- Zoll- Sanktions- CBAM- und Ermittlungsmandate vom Intake bis zum Handlungsvorschlag. Anwendungsfall Anwalt oder Compliance-Beauftragter will grenzüberschreitendes Mandat schnell… |
| `aussenwirtschaft-presse-krise` | Rechtliche und kommunikative Schadensbegrenzung bei Sanktionsverstoss Behördenmassnahmen oder Lieferkettenvorwuerfen. Anwendungsfall negative Berichterstattung droht oder Behoerde hat Massnahmen eingeleitet und… |
| `aussenwirtschaft-pruefung-ermittlung` | Begleitung von Aussenwirtschaftsprüfungen Zollprüfungen Durchsuchungen und Strafverfahren. Anwendungsfall Behorde kueendigt Prüfung an oder Durchsuchung hat stattgefunden. Normen AWG § 34 Strafrecht OWiG § 19… |
| `aussenwirtschaft-sanktionen-embargos` | Prüfung von Laenderembargos personenbezogenen Sanktionen und Umgehungsrisiken im Aussenhandel. Anwendungsfall Handelspartner koennte Sanktionslistentreffer haben oder Lieferung in Sanktionsland geht. Normen… |
| `aussenwirtschaft-us-ear-itar` | US-Exportkontrolle EAR ITAR und OFAC für Unternehmen mit US-Bezug im Aussenhandel. Anwendungsfall Produkt enthaelt US-Komponenten oder unterliegt US-Recht und Reexport- oder Weitergabepflichten muessen geprüft werden.… |
| `aussenwirtschaft-verbrauchsteuer` | Verbrauchsteuerrecht für Energieerzeugnisse Strom Tabak Alkohol Bier Schaumwein und Kaffee. Anwendungsfall Hersteller oder Haendler prüft Steuerlager Steueraussetzungsverfahren oder Entlastungsantrag. Normen EnergieStG… |
| `aussenwirtschaft-vub-einfuhr-ausfuhr` | Verbote und Beschraenkungen VuB für besondere Waren wie Dual-Use Kulturgut CITES F-Gase Lebensmittel und Russland-Iranembargos. Anwendungsfall Import oder Export einer Ware koennte VuB-Beschraenkungen unterliegen.… |
| `aussenwirtschaft-wto-handelspolitik` | WTO Handelspolitik GATT GATS TRIPS und Streitbeilegung für Aussenhandelsmandate. Anwendungsfall Handelspartner klagt WTO-Verstoss oder Unternehmen ist von Schutzmassnahmen betroffen. Normen GATT 1994 GATS TRIPS DSU… |
| `aussenwirtschaft-zolltarif-vzta` | Wareneinreihung TARIC-Massnahmen und verbindliche Zolltarifauskunft VzTA. Anwendungsfall Unternehmen will CN-Code für Ware bestimmen oder VzTA-Antrag stellen. Normen UZK Art. 33-37 VzTA Kombinierte Nomenklatur VO… |
| `aussenwirtschaft-zollverfahren-bewilligungen` | Zollverfahren und Bewilligungen im Union-Zollkodex für AEO vereinfachte Anmeldung und besondere Verfahren. Anwendungsfall Unternehmen will Versandverfahren Zolllager aktive Veredelung oder AEO-Zertifizierung nutzen.… |
| `aussenwirtschaft-zollwert-ursprung` | Zollwert Warenursprung Praeferenznachweise und Lieferantenerklarungen im EU-Zollrecht. Anwendungsfall Zoll bestreitet Zollwert oder Praeferenzursprungsnachweis fehlt und Einfuhrabgaben werden nachgefordert. Normen UZK… |

## Worum geht es?

Das Plugin deckt das gesamte Aussenwirtschafts- und Zollrecht ab: von der Exportkontrolle fuer Dual-Use-Gueter und Ruestungsgueter ueber Sanktionen und Embargos bis hin zu Zolltarifrecht, Warenursprung, Praeferenznachweisen und dem Carbon Border Adjustment Mechanism (CBAM). Es begleitet Unternehmen beim Aufbau interner Compliance-Programme (ICP) und stuetzt Anwaelte und Compliance-Verantwortliche bei Behoerdenpruefungen und Strafverfahren.

Das Plugin integriert auch AWV-Meldepflichten gegenueber der Deutschen Bundesbank, AML/KYC-Sanktionsscreening, Antidumping sowie WTO-Handelspolitik. Zielgruppe sind Compliance-Abteilungen exportierender Unternehmen, Zollbeauftragte, Anwaelte und Steuerberater im Aussenhandel.

## Wann brauchen Sie diese Skill?

- Unternehmen exportiert Gueter mit potenziellem Dual-Use und muss pruefen, ob eine BAFA-Genehmigung erforderlich ist.
- Handelspartner steht auf Sanktionsliste oder hat Bezug zu embargierten Laendern; Transaktion muss vor Ausfuehrung geprueft werden.
- Zollbehoerde bestreitet Zollwert oder Warenursprung; Praeferenznachweis muss verteidigt werden.
- Unternehmen erhalt Ankuendigung einer Zollpruefung oder Aussenwirtschaftspruefung und muss Verfahrensvorbereitung treffen.
- CBAM-pflichtige Waren werden eingefuehrt; Zertifikatspflichten und CO2-Preisberechnungen muessen implementiert werden.

## Fachbegriffe (kurz erklaert)

- **Dual-Use** — Gueter, Software und Technologien mit ziviler und militaerischer Verwendungsmoeglichkeit; unterstehen der EG Dual-Use-Verordnung (VO (EG) 428/2009, jetzt VO (EU) 2021/821).
- **BAFA** — Bundesamt fuer Wirtschaft und Ausfuhrkontrolle; zentrale Genehmigungs- und Pruefungsbehoerde fuer Exportkontrolle.
- **Sanktionen / Embargos** — Wirtschaftliche Massnahmen der EU, UN oder USA gegen Laender oder Personen; Umgehung ist Straftat.
- **TARIC** — Integrierter Zolltarif der EU; kombiniert CN-Code mit handelspolitischen Massnahmen.
- **Zollwert** — Basis fuer die Berechnung der Eingangsabgaben; grundsaetzlich Transaktionswert nach UZK-Zollwertmethoden.
- **Warenursprung** — Praeferenzielle und nichtpraeferenzielle Herkunft einer Ware; Grundlage fuer Praeferenzzollsaetze und Antidumping.
- **CBAM** — Carbon Border Adjustment Mechanism; CO2-Grenzausgleich fuer Einfuhren aus Drittlaendern seit 01.10.2023 (Uebergangsphase).
- **ICP** — Internal Compliance Programme; strukturiertes internes Exportkontroll-Kontrollsystem nach BAFA-Anforderungen.
- **AWV** — Aussenwirtschaftsverordnung; regelt Meldepflichten gegenueber Bundesbank fuer grenzueberschreitende Zahlungen und Kapitalverkehr.
- **AEO** — Zugelassener Wirtschaftsbeteiligter; EU-weite Bewilligung fuer vereinfachte Zollverfahren und schnellere Abfertigung.

## Rechtsgrundlagen

- AWG — Aussenwirtschaftsgesetz
- AWV — Aussenwirtschaftsverordnung
- VO (EU) 2021/821 — Dual-Use-Verordnung
- UZK (VO (EU) 952/2013) — Unionszollkodex
- VO (EU) 2022/2449 — CBAM-Uebergangsverordnung
- GwG — Geldwaeschegesetz (AML/KYC)
- OFAC-Vorschriften (USA) — US-Sanktionsrecht (extraterritorial relevant)
- 15 CFR (EAR), 22 CFR (ITAR) — US-Exportkontrollrecht

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Exporteur, Importeur, Handelspartner-Sanktionspruefung oder Behoerdenverfahren?
2. Regulierungsrahmen bestimmen: EU-Recht, nationales AWG/AWV oder US-Recht (EAR/ITAR/OFAC) relevant?
3. Gueterklassifizierung pruefen: CN-Code, Dual-Use-Einstufung und Gueterlisten-Nummer festlegen.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Fristen pruefen: BAFA-Antragsfristen, AWV-Meldefristen (sieben Werktage), CBAM-Quartalsberichte.

## Skill-Tour (was gibt es hier?)

- `aussenwirtschaft-kommandocenter` — Mandats-Intake und Routing fuer alle Aussenhandels- Zoll- Sanktions- und Ermittlungsmandate.
- `aussenwirtschaft-exportkontrolle-dual-use` — Dual-Use-Pruefung fuer Gueter, Software und Technologie mit Doppelverwendungszweck.
- `aussenwirtschaft-gueterlisten-klassifizierung` — Klassifizierungsdossier fuer Exportkontrolle, Zolltarif und Dual-Use-Einordnung erstellen.
- `aussenwirtschaft-bafa-genehmigungen` — BAFA-Genehmigungsverfahren fuer genehmigungs-pflichtige Exporte begleiten.
- `aussenwirtschaft-sanktionen-embargos` — Laenderembargos und personenbezogene Sanktionen pruefen; Umgehungsrisiken identifizieren.
- `aussenwirtschaft-aml-kyc-sanktionen` — GwG-Risikoanalyse, KYC-Pruefung und Sanktionsscreening im Aussenhandel verknuepfen.
- `aussenwirtschaft-zolltarif-vzta` — Wareneinreihung nach TARIC und verbindliche Zolltarifauskunft (VzTA) beantragen.
- `aussenwirtschaft-zollwert-ursprung` — Zollwert, Warenursprung, Praeferenznachweise und Lieferantenerklarungen klaeren und verteidigen.
- `aussenwirtschaft-zollverfahren-bewilligungen` — Zollverfahren nach UZK und Bewilligungen (AEO, vereinfachte Anmeldung) beantragen.
- `aussenwirtschaft-cbam-co2-zoll` — CBAM-Compliance: CO2-Grenzausgleich fuer Einfuhren berechnen und Zertifikatspflichten erfuellen.
- `aussenwirtschaft-awv-bundesbank` — AWV-Meldepflichten gegenueber Bundesbank fuer grenzueberschreitende Zahlungen umsetzen.
- `aussenwirtschaft-verbrauchsteuer` — Verbrauchsteuerrecht fuer Energie, Strom, Tabak und Alkohol im Aussenhandel.
- `aussenwirtschaft-vub-einfuhr-ausfuhr` — Verbote und Beschraenkungen (VuB) fuer besondere Waren: Dual-Use, CITES, F-Gase, Russland/Iran.
- `aussenwirtschaft-antidumping-ausgleich` — Antidumping- und Antisubventionsmassnahmen; Ausgleichszoelle pruefen und anfechten.
- `aussenwirtschaft-wto-handelspolitik` — WTO-Regelwerk, GATT/GATS/TRIPS und Streitbeilegung fuer Aussenhandelsmandate.
- `aussenwirtschaft-us-ear-itar` — US-Exportkontrolle EAR/ITAR und OFAC fuer Unternehmen mit US-Bezug oder US-Waren-Anteilen.
- `aussenwirtschaft-icp-kontrollsystem` — Internes Compliance-Programm (ICP) fuer Exportkontrolle, Zoll, Sanktionen und AML entwerfen.
- `aussenwirtschaft-pruefung-ermittlung` — Begleitung von Zollpruefungen, Aussenwirtschaftspruefungen, Durchsuchungen und Strafverfahren.
- `aussenwirtschaft-presse-krise` — Kommunikative und rechtliche Schadensbegrenzung bei Sanktionsverstoss oder oeffentlichem Vorwurf.

## Worauf besonders achten

- Dual-Use-Pruefung umfasst nicht nur physische Gueter, sondern auch Software, Technologieue und Know-how-Transfer (auch muendlich).
- US-Exportkontrollrecht (EAR/ITAR/OFAC) kann extraterritorial wirken; EU-Unternehmen mit US-Waren-Anteilen oder US-Mitarbeitern sind betroffen.
- AWV-Meldepflichten haben kurze Fristen (z.T. sieben Werktage nach Zahlung); verspaetest gestellte Meldungen sind Ordnungswidrigkeit.
- CBAM-Uebergangsphase laeuft bis Ende 2025; ab 2026 gelten volle Zertifikatspflichten mit Quartalsmeldungen.
- Sanktions-Screening muss alle Vertragsparteien, Endabnehmer und Zwischenhaendler erfassen; alleinige Zahlungsstrom-Pruefung genuegt nicht.

## Typische Fehler

- Genehmigungspflicht uebersehen: Dual-Use-Einordnung ohne Gueterlisten-Check; Export ohne erforderliche BAFA-Genehmigung ist Straftat.
- Praeferenznachweis nicht rechtzeitig eingeholt: Lieferantenerklarung muss vor Ausfuhr vorliegen; nachtragliche Anforderung wird oft abgelehnt.
- Zollwert-Anpassungen vergessen: Lizenzgebuehren und Verguetungen koennen zum Zollwert hinzugerechnet werden (Art. 71 UZK).
- US-Sanktions-Nexus uebersehen: Transaktionen in USD oder mit US-Kreditinstituten koennen OFAC-Pflichten ausloesen.
- ICP nur auf dem Papier: BAFA bewertet Wirksamkeit des ICP in der Praxis; fehlende Schulungen und fehlende Dokumentation fuehren zu Nachforderungen.

## Querverweise

- Plugin `umweltrecht` — CBAM hat Schnittstellen zu TEHG-Emissionshandel; Doppel-Compliance pruefen.
- Plugin `grosskanzlei-corporate-ma` — Bei M&A-Transaktionen mit Auslandstoechtern: Exportkontroll-DD und Sanktions-Screening als Teil der Legal DD.
- Plugin `patentrecherche` — Bei Technologietransfer-Mandaten koennen Exportkontroll- und Patentlizenz-Fragen zusammenfallen.

## Quellen und Aktualitaet

- Stand: 05/2026
- AWG, AWV, UZK, Dual-Use-VO (EU) 2021/821, CBAM-VO (EU) 2023/956, GwG in aktuell geltender Fassung
- BAFA-Merkblaetter und TARIC-Datenbank (Stand 05/2026)
