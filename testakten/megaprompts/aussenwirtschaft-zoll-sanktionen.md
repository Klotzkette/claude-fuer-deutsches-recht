# Megaprompt: aussenwirtschaft-zoll-sanktionen

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 100 Skills des Plugins `aussenwirtschaft-zoll-sanktionen`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlag…
2. **allgemeingenehmigung-agg-antidumping** — Allgemeine Genehmigungen nach AWV: Auffinden und Pruefen der passenden Allgemeingenehmigung (AGG) für kontrollierte Ausf…
3. **asset-freeze-atlas-ausfuhranmeldung-audit** — Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftl…
4. **aussenwirtschaft-abfallverbringung** — Grenzueberschreitende Abfallverbringung nach EU-AbfVerbrV (VO 1013/2006 bzw. VO 1418/2007) und KrWG: Notifizierungsverfa…
5. **aussenwirtschaft-aeo-bewilligung-monitoring** — AEO-Zugelassener-Wirtschaftsbeteiligter-Bewilligung (Customs Simplification/Security/Full): Monitoring laufender Bewilli…
6. **aussenwirtschaft-aktive-veredelung** — Zollverfahren aktive Veredelung nach Art. 256-258 UZK und Art. 240-262 UZK-DA: Beantragung und Nutzung der Bewilligung b…
7. **aussenwirtschaft-aml-kyc-finanzsanktionen** — Schnittstelle von AML/KYC-Pflichten und Sanktionsrecht: Risikobasierte Kundenpruefung nach GwG (§§ 10-17 GwG) kombiniert…
8. **aussenwirtschaft-antidumping-ausgleich** — Antidumping-Ausgleichsmassnahmen nach EU-Grundverordnung (VO (EU) 2016/1036): Identifizierung von TARIC-Antidumping-Mass…
9. **aussenwirtschaft-antidumping-erstattung-review** — Erstattung zu viel gezahlter Antidumping-Zoelle und Auslosung von Revisionsverfahren nach Art. 11 VO (EU) 2016/1036: Rue…
10. **aussenwirtschaft-antidumping-taric-massnahmen** — Identifizierung und Anwendung handelspolitischer Schutzmassnahmen (Antidumping, Ausgleichszoll, Safeguards) im TARIC-Sys…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skil..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Aussenwirtschaft Zoll Sanktionen** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Aussenwirtschaft Zoll Sanktionen**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

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
| `aussenwirtschaft-aml-kyc-sanktionen` | Verknuepft GwG-Risikoanalyse KYC Sanktionsscreening und interne Kontrollpflichten im Aussenhandel. Anwendungsfall Exporteur oder Haendler braucht integriertes AML- und Sanktions-Compliance-System für… |
| `aussenwirtschaft-antidumping-ausgleich` | Antidumping Antisubvention und Ausgleichsmassnahmen im EU-Aussenhandelsrecht. Anwendungsfall Import- oder Exporteur ist von Antidumping-Massnahmen betroffen oder will Erstattungsantrag stellen. Normen… |
| `aussenwirtschaft-awv-bundesbank` | Meldepflichten nach Aussenwirtschaftsverordnung AWV gegenüber Bundesbank für grenzüberschreitende Zahlungen und Beteiligungen. Anwendungsfall Unternehmen hat Zahlungen ins Ausland oder Auslandsforderungen und prüft… |
| `aussenwirtschaft-bafa-genehmigungen` | BAFA-Genehmigungsverfahren für Exporte und Dienstleistungen mit Genehmigungspflicht. Anwendungsfall Exporteur braucht BAFA-Ausfuhrgenehmigung für gueterlistenpflichtige Ware oder Technologie. Normen § 8 AWG… |
| `aussenwirtschaft-cbam-co2-zoll` | Carbon Border Adjustment Mechanism CBAM CO2-Grenzausgleich für Einfuhren aus Drittlaendern. Anwendungsfall Unternehmen importiert CBAM-pflichtige Waren Stahl Aluminium Zement Duenger Strom und muss CBAM-Pflichten… |
| `aussenwirtschaft-exportkontrolle-dual-use` | Exportkontrolle Dual-Use-Prüfung für Gueter Software Technologie und Dienstleistungen mit Doppelverwendungszweck. Anwendungsfall Exporteur prüft ob Ware oder Software unter Dual-Use-Regulierung faellt und Genehmigung… |
| `aussenwirtschaft-gueterlisten-klassifizierung` | Klassifizierungsdossier für Exportkontrolle Zolltarif und Dual-Use-Einordnung. Anwendungsfall Produkt muss für Exportkontrolle und Zoll einheitlich klassifiziert werden. Normen EU-Dual-Use-Liste Anhang I Verordnung… |
| `aussenwirtschaft-icp-kontrollsystem` | Entwurf und Haertung eines integrierten Compliance-Programms ICP für Exportkontrolle Zoll Sanktionen CBAM und AML. Anwendungsfall Unternehmen will rechtssicheres ICP aufbauen oder bestehendes System haerten. Normen AWG… |
| `aussenwirtschaft-kommandocenter` | Kommandocenter für alle Aussenhandels- Zoll- Sanktions- CBAM- und Ermittlungsmandate vom Intake bis zum Handlungsvorschlag. Anwendungsfall Anwalt oder Compliance-Beauftragter will grenzüberschreitendes Mandat schnell… |
| `aussenwirtschaft-presse-krise` | Rechtliche und kommunikative Schadensbegrenzung bei Sanktionsverstoss Behördenmassnahmen oder Lieferkettenvorwuerfen. Anwendungsfall negative Berichterstattung droht oder Behörde hat Massnahmen eingeleitet und… |
| `aussenwirtschaft-pruefung-ermittlung` | Begleitung von Aussenwirtschaftsprüfungen Zollprüfungen Durchsuchungen und Strafverfahren. Anwendungsfall Behorde kueendigt Prüfung an oder Durchsuchung hat stattgefunden. Normen AWG § 34 Strafrecht OWiG § 19… |
| `aussenwirtschaft-sanktionen-embargos` | Prüfung von Länderembargos personenbezogenen Sanktionen und Umgehungsrisiken im Aussenhandel. Anwendungsfall Handelspartner koennte Sanktionslistentreffer haben oder Lieferung in Sanktionsland geht. Normen… |
| `aussenwirtschaft-us-ear-itar` | US-Exportkontrolle EAR ITAR und OFAC für Unternehmen mit US-Bezug im Aussenhandel. Anwendungsfall Produkt enthaelt US-Komponenten oder unterliegt US-Recht und Reexport- oder Weitergabepflichten muessen geprüft werden.… |
| `aussenwirtschaft-verbrauchsteuer` | Verbrauchsteuerrecht für Energieerzeugnisse Strom Tabak Alkohol Bier Schaumwein und Kaffee. Anwendungsfall Hersteller oder Haendler prüft Steuerlager Steueraussetzungsverfahren oder Entlastungsantrag. Normen EnergieStG… |
| `aussenwirtschaft-vub-einfuhr-ausfuhr` | Verbote und Beschraenkungen VuB für besondere Waren wie Dual-Use Kulturgut CITES F-Gase Lebensmittel und Russland-Iranembargos. Anwendungsfall Import oder Export einer Ware koennte VuB-Beschraenkungen unterliegen.… |
| `aussenwirtschaft-wto-handelspolitik` | WTO Handelspolitik GATT GATS TRIPS und Streitbeilegung für Aussenhandelsmandate. Anwendungsfall Handelspartner klagt WTO-Verstoss oder Unternehmen ist von Schutzmassnahmen betroffen. Normen GATT 1994 GATS TRIPS DSU… |
| `aussenwirtschaft-zolltarif-vzta` | Wareneinreihung TARIC-Massnahmen und verbindliche Zolltarifauskunft VzTA. Anwendungsfall Unternehmen will CN-Code für Ware bestimmen oder VzTA-Antrag stellen. Normen UZK Art. 33-37 VzTA Kombinierte Nomenklatur VO… |
| `aussenwirtschaft-zollverfahren-bewilligungen` | Zollverfahren und Bewilligungen im Union-Zollkodex für AEO vereinfachte Anmeldung und besondere Verfahren. Anwendungsfall Unternehmen will Versandverfahren Zolllager aktive Veredelung oder AEO-Zertifizierung nutzen.… |
| `aussenwirtschaft-zollwert-ursprung` | Zollwert Warenursprung Praeferenznachweise und Lieferantenerklarungen im EU-Zollrecht. Anwendungsfall Zoll bestreitet Zollwert oder Praeferenzursprungsnachweis fehlt und Einfuhrabgaben werden nachgefordert. Normen UZK… |

## Worum geht es?

Das Plugin deckt das gesamte Aussenwirtschafts- und Zollrecht ab: von der Exportkontrolle für Dual-Use-Gueter und Ruestungsgueter ueber Sanktionen und Embargos bis hin zu Zolltarifrecht, Warenursprung, Praeferenznachweisen und dem Carbon Border Adjustment Mechanism (CBAM). Es begleitet Unternehmen beim Aufbau interner Compliance-Programme (ICP) und stuetzt Anwaelte und Compliance-Verantwortliche bei Behördenpruefungen und Strafverfahren.

Das Plugin integriert auch AWV-Meldepflichten gegenueber der Deutschen Bundesbank, AML/KYC-Sanktionsscreening, Antidumping sowie WTO-Handelspolitik. Zielgruppe sind Compliance-Abteilungen exportierender Unternehmen, Zollbeauftragte, Anwaelte und Steuerberater im Aussenhandel.

## Wann brauchen Sie diese Skill?

- Unternehmen exportiert Gueter mit potenziellem Dual-Use und muss pruefen, ob eine BAFA-Genehmigung erforderlich ist.
- Handelspartner steht auf Sanktionsliste oder hat Bezug zu embargierten Ländern; Transaktion muss vor Ausfuehrung geprueft werden.
- Zollbehoerde bestreitet Zollwert oder Warenursprung; Praeferenznachweis muss verteidigt werden.
- Unternehmen erhalt Ankuendigung einer Zollpruefung oder Aussenwirtschaftspruefung und muss Verfahrensvorbereitung treffen.
- CBAM-pflichtige Waren werden eingefuehrt; Zertifikatspflichten und CO2-Preisberechnungen muessen implementiert werden.

## Fachbegriffe (kurz erklaert)

- **Dual-Use** — Gueter, Software und Technologien mit ziviler und militaerischer Verwendungsmoeglichkeit; unterstehen der EG Dual-Use-Verordnung (VO (EG) 428/2009, jetzt VO (EU) 2021/821).
- **BAFA** — Bundesamt für Wirtschaft und Ausfuhrkontrolle; zentrale Genehmigungs- und Pruefungsbehoerde für Exportkontrolle.
- **Sanktionen / Embargos** — Wirtschaftliche Massnahmen der EU, UN oder USA gegen Länder oder Personen; Umgehung ist Straftat.
- **TARIC** — Integrierter Zolltarif der EU; kombiniert CN-Code mit handelspolitischen Massnahmen.
- **Zollwert** — Basis für die Berechnung der Eingangsabgaben; grundsaetzlich Transaktionswert nach UZK-Zollwertmethoden.
- **Warenursprung** — Praeferenzielle und nichtpraeferenzielle Herkunft einer Ware; Grundlage für Praeferenzzollsaetze und Antidumping.
- **CBAM** — Carbon Border Adjustment Mechanism; CO2-Grenzausgleich für Einfuhren aus Drittlaendern seit 01.10.2023 (Uebergangsphase).
- **ICP** — Internal Compliance Programme; strukturiertes internes Exportkontroll-Kontrollsystem nach BAFA-Anforderungen.
- **AWV** — Aussenwirtschaftsverordnung; regelt Meldepflichten gegenueber Bundesbank für grenzueberschreitende Zahlungen und Kapitalverkehr.
- **AEO** — Zugelassener Wirtschaftsbeteiligter; EU-weite Bewilligung für vereinfachte Zollverfahren und schnellere Abfertigung.

## Rechtsgrundlagen

- AWG — Aussenwirtschaftsgesetz
- AWV — Aussenwirtschaftsverordnung
- VO (EU) 2021/821 — Dual-Use-Verordnung
- UZK (VO (EU) 952/2013) — Unionszollkodex
- VO (EU) 2022/2449 — CBAM-Uebergangsverordnung
- GwG — Geldwaeschegesetz (AML/KYC)
- OFAC-Vorschriften (USA) — US-Sanktionsrecht (extraterritorial relevant)
- 15 CFR (EAR), 22 CFR (ITAR) — US-Exportkontrollrecht

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Exporteur, Importeur, Handelspartner-Sanktionspruefung oder Behördenverfahren?
2. Regulierungsrahmen bestimmen: EU-Recht, nationales AWG/AWV oder US-Recht (EAR/ITAR/OFAC) relevant?
3. Gueterklassifizierung pruefen: CN-Code, Dual-Use-Einstufung und Gueterlisten-Nummer festlegen.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Fristen pruefen: BAFA-Antragsfristen, AWV-Meldefristen (sieben Werktage), CBAM-Quartalsberichte.

## Skill-Tour (was gibt es hier?)

- `aussenwirtschaft-kommandocenter` — Mandats-Intake und Routing für alle Aussenhandels- Zoll- Sanktions- und Ermittlungsmandate.
- `aussenwirtschaft-exportkontrolle-dual-use` — Dual-Use-Pruefung für Gueter, Software und Technologie mit Doppelverwendungszweck.
- `aussenwirtschaft-gueterlisten-klassifizierung` — Klassifizierungsdossier für Exportkontrolle, Zolltarif und Dual-Use-Einordnung erstellen.
- `aussenwirtschaft-bafa-genehmigungen` — BAFA-Genehmigungsverfahren für genehmigungs-pflichtige Exporte begleiten.
- `aussenwirtschaft-sanktionen-embargos` — Länderembargos und personenbezogene Sanktionen pruefen; Umgehungsrisiken identifizieren.
- `aussenwirtschaft-aml-kyc-sanktionen` — GwG-Risikoanalyse, KYC-Pruefung und Sanktionsscreening im Aussenhandel verknuepfen.
- `aussenwirtschaft-zolltarif-vzta` — Wareneinreihung nach TARIC und verbindliche Zolltarifauskunft (VzTA) beantragen.
- `aussenwirtschaft-zollwert-ursprung` — Zollwert, Warenursprung, Praeferenznachweise und Lieferantenerklarungen klaeren und verteidigen.
- `aussenwirtschaft-zollverfahren-bewilligungen` — Zollverfahren nach UZK und Bewilligungen (AEO, vereinfachte Anmeldung) beantragen.
- `aussenwirtschaft-cbam-co2-zoll` — CBAM-Compliance: CO2-Grenzausgleich für Einfuhren berechnen und Zertifikatspflichten erfuellen.
- `aussenwirtschaft-awv-bundesbank` — AWV-Meldepflichten gegenueber Bundesbank für grenzueberschreitende Zahlungen umsetzen.
- `aussenwirtschaft-verbrauchsteuer` — Verbrauchsteuerrecht für Energie, Strom, Tabak und Alkohol im Aussenhandel.
- `aussenwirtschaft-vub-einfuhr-ausfuhr` — Verbote und Beschraenkungen (VuB) für besondere Waren: Dual-Use, CITES, F-Gase, Russland/Iran.
- `aussenwirtschaft-antidumping-ausgleich` — Antidumping- und Antisubventionsmassnahmen; Ausgleichszoelle pruefen und anfechten.
- `aussenwirtschaft-wto-handelspolitik` — WTO-Regelwerk, GATT/GATS/TRIPS und Streitbeilegung für Aussenhandelsmandate.
- `aussenwirtschaft-us-ear-itar` — US-Exportkontrolle EAR/ITAR und OFAC für Unternehmen mit US-Bezug oder US-Waren-Anteilen.
- `aussenwirtschaft-icp-kontrollsystem` — Internes Compliance-Programm (ICP) für Exportkontrolle, Zoll, Sanktionen und AML entwerfen.
- `aussenwirtschaft-pruefung-ermittlung` — Begleitung von Zollpruefungen, Aussenwirtschaftspruefungen, Durchsuchungen und Strafverfahren.
- `aussenwirtschaft-presse-krise` — Kommunikative und rechtliche Schadensbegrenzung bei Sanktionsverstoss oder öffentlichem Vorwurf.

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

## Quellen und Aktualitaet

- Stand: 05/2026
- AWG, AWV, UZK, Dual-Use-VO (EU) 2021/821, CBAM-VO (EU) 2023/956, GwG in aktuell geltender Fassung
- BAFA-Merkblaetter und TARIC-Datenbank (Stand 05/2026)

---

## Skill: `allgemeingenehmigung-agg-antidumping`

_Allgemeine Genehmigungen nach AWV: Auffinden und Pruefen der passenden Allgemeingenehmigung (AGG) für kontrollierte Ausfuhren ohne Einzelgenehmigung. Beruecksichtigt EU-Ausfuhrgenehmigungen (001-009 VO 2021/821), nationale AGGs der AWV und BAFA-Merkblaetter. Mandant liefert Ware/Technologie und Z..._

# Allgemeine Genehmigungen: Finder und Nutzungsbedingungen für Exportkontrolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Maschinenhersteller moechte Ersatzteile in USA liefern; Frage ob EU001 (NATO) anwendbar.
- Elektroniklieferant fragt, ob EU007 (Forschung und Entwicklung) für Technologielieferung in die Schweiz gilt.
- KMU prueft, ob nationale AGG 29 für Lieferung bestimmter Gueter nach Israel nutzbar ist.

## Erste Schritte

1. Gueterlistenklassifizierung feststellen (Anhang I VO 2021/821, ECCN, Dual-Use-Code).
2. Zielland und Endverwender (Regierung, Zivil, Militaer) bestimmen.
3. Alle EU-Allgemeingenehmigungen EU001-EU009 systematisch durchpruefen.
4. Nationale Allgemeingenehmigungen (AWV) für nicht von EU-Regelung erfasste Faelle pruefen.
5. Bedingungen der anwendbaren AGG pruefen: Ausschluesse, Exporteurdokumentation, Registrierung.
6. Registrierungspflicht beim BAFA beachten und Nutzungslog anlegen.

## Rechtsrahmen

- **Art. 12 VO (EU) 2021/821**: Rahmenbedingungen EU-Allgemeingenehmigungen (EU001-EU009).
- **Anhang II VO (EU) 2021/821**: Texte der einzelnen EU-Ausfuhrgenehmigungen.
- **§§ 2, 8 AWG**: Genehmigungstatbestand und Ausnahmen für genehmigte Ausfuhr.
- **§§ 8 ff. AWV**: Nationale Allgemeingenehmigungen.
- **BAFA-Merkblatt Allgemeine Genehmigungen**: Anwendungshinweise.

## Pruef-Raster

- [ ] Gueterlistencode vollstaendig ermittelt?
- [ ] Zielland-Ausschlusslisten jeder AGG einzeln geprueft?
- [ ] Endverwender-Einschraenkungen der AGG (kein Militaer, keine WMD-Nutzung) geprueft?
- [ ] Registrierungspflicht beim BAFA beachtet?
- [ ] Nachweisdokumentation für Compliance-Zwecke angelegt?
- [ ] AGG-Nutzung im Export-Management-System vermerkt?

## Typische Fallstricke

- EU-Allgemeingenehmigungen schliessen bestimmte Länder explizit aus; Ausschlusslisten aktuell pruefen.
- Registrierungspflicht bei EU002/EU003 wird oft vergessen.
- AGG deckt keine Embargosituationen ab; vorrangige Embargopruefen erforderlich.
- Nationale AWV-AGGs koennen durch spaeteres EU-Recht ueberholt sein.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EU) 2021/821 mit Anhang II auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021R0821)
- [BAFA Allgemeine Genehmigungen](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Allgemeine_Genehmigungen/allgemeine_genehmigungen_node.html)
- [AWV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awv_2013/index.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `asset-freeze-atlas-ausfuhranmeldung-audit`

_Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftlichen Ressourcen nach Art. 2 VO (EU) 269/2014 und Art. 4 VO (EU) 833/2014. Checkliste für Banken, Notare und Unternehmen: Identifizierung sanktionierbarer Vermoegen, Meldepflich..._

# Asset Freeze: Sofortmassnahmen beim Einfrieren sanktionierten Vermoegens

## Arbeitsbereich

Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftlichen Ressourcen nach Art. 2 VO (EU) 269/2014 und Art. 4 VO (EU) 833/2014. Checkliste für Banken, Notare und Unternehmen: Identifizierung sanktionierbarer Vermoegen, Meldepflicht an Bundesbank/BaFin und zuständige Behörden. Output: Einfrierungs-Protokoll und Meldedokument. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Bank stellt Sanktionstreffer bei Kontoinhaber fest; internes Compliance-Team fragt nach Sofortmassnahmen.
- Notar beurkundet Immobilienkauf; Kaeufer erweist sich als UBO einer sanktionierten russischen Holdinggesellschaft.
- Unternehmen erhalt Zahlungsauftrag von Gegenpartei, die neu auf EU-Sanktionsliste aufgenommen wurde.

## Erste Schritte

1. Sanktionstreffer sofort dokumentieren: Name, Listennummer, Verordnung, Datum des Treffers.
2. Gelder/wirtschaftliche Ressourcen einfrieren; keine Auszahlung, kein Transfer, keine Verrechnung.
3. Zustaendige nationale Behörde informieren: Bundesbank (Devisenbeschraenkungen), BaFin (Finanzsektor), BAFA (Gueter).
4. Ggf. Freistellungs- oder Genehmigungsantrag vorbereiten (Art. 6 VO 269/2014: humanitaere Ausnahme).
5. Rechtsbeistand einschalten; Haftungsrisiko der handelnden Personen absichern.
6. Legal Hold für alle relevanten Unterlagen erteilen.

## Rechtsrahmen

- **Art. 2 VO (EU) 269/2014**: Bereitstellungsverbot und Einfrierungspflicht (Russland-Finanzsanktionen).
- **Art. 4 VO (EU) 833/2014**: Sektorales Embargo und wirtschaftliche Ressourcen.
- **Art. 11 VO (EU) 269/2014**: Meldepflicht bei eingefrorenen Geldern an Mitgliedstaaten.
- **§ 18 AWG**: Strafbewehrte Bereitstellung sanktionierten Vermogens.
- **§ 22 Abs. 4 AWG**: Freiwillige Selbstanzeige als Mildernungsmoeglichkeit.

## Pruef-Raster

- [ ] Trefferidentitaet eindeutig verifiziert (kein False Positive)?
- [ ] Einfrierungsmassnahmen sofort und vollstaendig umgesetzt?
- [ ] Zustaendige Behörde (Bundesbank/BaFin/BAFA) rechtzeitig informiert?
- [ ] Freistellungsantrag für genehmigte Transaktionen vorbereitet?
- [ ] Legal Hold erteilt und Unterlagen gesichert?
- [ ] Strafrecht-/Haftungsrisiko bewertet und Rechtsberatung eingeholt?

## Typische Fallstricke

- 50/50-Regel bei Eigentum: Auch indirekt sanktionierten Gesellschaften muss eingefroren werden.
- Einfrierung muss vollstaendig sein; Teilauszahlungen oder Verrechnung verstoessen gegen Bereitstellungsverbot.
- Meldepflicht ist unverzueglich; Versaeumnis fuehrt zu eigenem Sanktionsrisiko.
- Humanitaere Ausnahmen erfordern explizite Genehmigung; nicht eigenmaechtig handeln.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EU) 269/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [VO (EU) 833/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0833)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)
- [Bundesbank Devisenbeschraenkungen](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/finanzsanktionen)
- [BAFA Aussenwirtschaft](https://www.bafa.de/DE/Aussenwirtschaft/aussenwirtschaft_node.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-abfallverbringung`

_Grenzueberschreitende Abfallverbringung nach EU-AbfVerbrV (VO 1013/2006 bzw. VO 1418/2007) und KrWG: Notifizierungsverfahren für Abfaelle der Gruenen/Gelben/Roten Liste, Genehmigungspflichten beim Hauptzollamt und Bundesumweltamt, AVV-Schluessel-Pruefung, Kontrolle von Empfaengerlandzustimmungen...._

# Abfallverbringung: Grenzueberschreitende Entsorgung und Notifizierungsverfahren

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Unternehmen moechte Elektronikschrott (WEEE) zur Verwertung nach Polen verschiffen; Zollabfertigung haelt die Sendung an.
- Recyclingbetrieb importiert Kunststoffabfaelle aus der Tuerkei; Bunderumweltamt fordert Notifizierungsunterlagen.
- Exporteur erhaelt Zollanmeldungsruecklage, weil AVV-Code und gruene Liste nicht uebereinstimmen.

## Erste Schritte

1. AVV-Abfallschluessel und Abfallart bestimmen; Einstufung in Gruene/Gelbe/Rote Liste (Anhaenge VO 1013/2006) pruefen.
2. Bestimmungsland identifizieren: OECD-Mitglied, Nicht-OECD, Basler-Konvention-Vertragspartei oder Verbot?
3. Notifizierungspflicht feststellen (Art. 3 ff. VO 1013/2006); bei gruener Liste vereinfachtes Verfahren?
4. Begleitformular (Anhang VII) oder Notifizierungsdokument (Anhang IA/IB) aufbereiten.
5. Zustaendige Behörden benennen: Bundesumweltamt als zust. Behörde am Versandort, Hauptzollamt für Ausfuhranmeldung.
6. Sicherheitsleistung (Art. 6 VO 1013/2006) kalkulieren und beantragen.

## Rechtsrahmen

- **VO (EG) 1013/2006** (Verbringungsverordnung): Kernrechtsrahmen für Notifizierung und Begleitdokumente.
- **VO (EG) 1418/2007**: Verbote und Einschraenkungen für Ausfuhr von gruenen Abfaellen in Nicht-OECD-Länder.
- **§§ 54-55 KrWG**: Genehmigungspflichten und Bussgeldbewehrung bei unerlaubter Verbringung.
- **Art. 36 VO 1013/2006**: Ausfuhrverbote für Abfaelle in Nicht-OECD-Staaten.
- **§ 18 AWG**: Aussenwirtschaftsrechtliche Ordnungswidrigkeit bei Umgehungsversuchen.

## Pruef-Raster

- [ ] AVV-Code korrekt und mit Abfallbeschaffenheit konsistent?
- [ ] Eingruppierung in Gruene/Gelbe/Rote Liste und Verfahren korrekt ausgewaehlt?
- [ ] Bestimmungsland hat Zustimmung erteilt (Art. 9 VO 1013/2006)?
- [ ] Begleitformular/Notifizierungsdokument vollstaendig ausgefuellt?
- [ ] Sicherheitsleistung beantragt und bestaetigt?
- [ ] Ausfuhranmeldung in ATLAS mit korrektem Verfahrenscode gestellt?
- [ ] Verbringungsnachweispflicht (Eingangsbestaetigung des Empfaengers) sichergestellt?

## Typische Fallstricke

- Fehlklassifizierung als Produkt statt Abfall: Zollamt und Umweltamt pruefen unabhaengig voneinander.
- Fehlende oder verspaetete Empfaengerbestaetigung fuehrt zu Vollzugsdefizit und Bussgelddruck.
- Kein Notifizierungsverfahren für gemischte Fraktionen ohne separate AVV-Einstufung jeder Fraktion.
- Gruene-Liste-Ausfuhr in Nicht-OECD ohne Zustimmung ist formell verboten (VO 1418/2007 Anlage).
- Sicherheitsleistung unterschaetzt: Muss Verbringungs- und Entsorgungskosten abdecken.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EG) 1013/2006 konsolidiert](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02006R1013-20230101)
- [VO (EG) 1418/2007 Ausfuhren in Nicht-OECD](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32007R1418)
- [KrWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/krwg/index.html)
- [Bundesumweltamt: Abfallverbringung](https://www.umweltbundesamt.de/themen/abfall-ressourcen/abfallverbringung)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-aeo-bewilligung-monitoring`

_AEO-Zugelassener-Wirtschaftsbeteiligter-Bewilligung (Customs Simplification/Security/Full): Monitoring laufender Bewilligungsbedingungen nach Art. 38-39 UZK und AEOC/AEOS/AEOF. Prueft regelmäßige Selbstevaluation, Ereignismeldepflichten an Hauptzollamt, Aenderungen in Haftungsverhaeltnissen, Comp..._

# AEO-Bewilligung: Monitoring laufender Bedingungen und Meldepflichten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Spediteur mit AEOS-Status stellt Veraenderung in der Geschaeftsfuehrung fest; Frage: Meldepflicht an Hauptzollamt?
- Hersteller mit AEOC erhaelt Hinweis aus Zollpruefung auf mangelhafte Compliance-Dokumentation.
- Konzernmutter moechte AEO-Status auf neue Tochtergesellschaft nach Fusion ausdehnen.

## Erste Schritte

1. Bewilligungstext und erteilte AEO-Kategorie (AEOC/AEOS/AEOF) sichten; Auflagen und Bedingungen identifizieren.
2. Ereignis-/Aenderungslog für die letzten 12 Monate erstellen: Personalwechsel, IT-Systeme, Sicherheitskonzept, Eigentuemerstruktur.
3. Meldepflicht nach Art. 23 Abs. 2 UZK-IA und Hauptzollamt-Merkblatt bewerten; Meldefrist kalkulieren.
4. Selbstevaluationsformular des Hauptzollamts aufrufen und aktuellen Erfuellungsgrad feststellen.
5. Etwaige Versaumnisse dokumentieren und Nachbesserungsplan mit Terminen festlegen.
6. Monatlichen Monitoring-Rhythmus mit Verantwortlichen und Eskalationspfad einrichten.

## Rechtsrahmen

- **Art. 38-39 UZK (VO (EU) 952/2013)**: Grundvoraussetzungen und Kategorien der AEO-Zulassung.
- **Art. 24-35 UZK-DA (VO (EU) 2015/2446)**: Beurteilungskriterien für Compliance, Buchfuehrung, Solvenz, Sicherheit.
- **Art. 23 Abs. 2 UZK-IA (VO (EU) 2015/2447)**: Meldepflicht bei aenderungsrelevanten Ereignissen.
- **§ 10 ZollVG**: Nationale Kontrollbefugnisse des Hauptzollamts.
- **Art. 27-28 UZK-DA**: Aussetzung und Widerruf der AEO-Bewilligung.

## Pruef-Raster

- [ ] Alle in der Bewilligung genannten Standorte und Prozesse unveraendert oder Aenderungen gemeldet?
- [ ] Geschaeftsfuehrung, UBO und Haftungsverhaeltnisse ohne meldepflichtige Aenderung?
- [ ] Solvenzanforderungen (Art. 26 UZK-DA) erneut geprueft?
- [ ] IT- und Sicherheitskonzept dem aktuellen AEOS/AEOC-Standard entsprechend?
- [ ] Interne Audits durchgefuehrt und dokumentiert?
- [ ] Korrespondierende Behordenkommunikation mit Datum und Aktenzeichen abgelegt?

## Typische Fallstricke

- Meldepflicht nach Art. 23 Abs. 2 UZK-IA wird bei Unternehmensumstrukturierungen oft uebersehen.
- AEO-Status wird nicht automatisch auf Tochtergesellschaften uebertragen; neuer Antrag noetig.
- Versaumnisse bei regelmäßiger Selbstevaluation fuehren zu Aussetzungsverfahren.
- Compliance-Luecken bei Subunternehmern im Sicherheitskonzept werden unterschaetzt.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [UZK Art. 38-39 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de AEO-Merkblatt](https://www.zoll.de/DE/Fachthemen/Zoelle/AEO/aeo_node.html)
- [ZollVG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zollvg/index.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-aktive-veredelung`

_Zollverfahren aktive Veredelung nach Art. 256-258 UZK und Art. 240-262 UZK-DA: Beantragung und Nutzung der Bewilligung beim Hauptzollamt, Mengenueberwachung (INF-Blatt), Ausbeute- und Aequivalenzwarensystem, Gesamtabrechnung und Ausfuhr veredelter Erzeugnisse. Prueft wirtschaftliche Voraussetzung..._

# Aktive Veredelung: Bewilligung, Mengenueberwachung und Abschlussabrechnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Maschinenbauer moechte importierte Komponenten verarbeiten und als Endprodukt exportieren ohne Einfuhrzoll zu zahlen.
- Textilfirma hat Bewilligung, aber die Ausbeute-Koeffizientenberechnung stimmt nicht mit ATLAS-Buchfuehrung ueberein.
- Pharmaunternehmen beantragt aktive Veredelung für Wirkstoffimport aus Indien zur Weiterverarbeitung und EU-Ausfuhr.

## Erste Schritte

1. Wirtschaftliche Voraussetzungen pruefen (Art. 211 Abs. 3 lit. a UZK): Interessentest und Ausfuhrnachweis.
2. Beantragung der Bewilligung beim oertlich zuständigen Hauptzollamt (Muster: DEK/INT/AV).
3. Buchfuehrungsanforderungen klaren: Lagerbuchhaltungssystem, Mengenueberwachung, Ausbeute-Koeffizienten.
4. INF-Blatt-Verfahren für Mehrniederlassungsveredelung pruefen.
5. Aequivalenzwaren-Option bewerten: Gleiche oder gleichartige Waren als Ersatz.
6. Gesamtabrechnung mit Frist planen: Ausbeute-Ist vs. Soll, Fehlmengenbehandlung.

## Rechtsrahmen

- **Art. 256-258 UZK (VO (EU) 952/2013)**: Anwendungsbereich und Bewilligungsvoraussetzungen.
- **Art. 240-262 UZK-DA (VO (EU) 2015/2446)**: Technische Bedingungen, Ausbeute, Aequivalenz.
- **Art. 321-330 UZK-IA (VO (EU) 2015/2447)**: Buchfuehrungs- und Abschlusspflichten.
- **Art. 212-214 UZK**: Bewilligungsantrag und wirtschaftliche Voraussetzungen.
- **§ 10 ZollVG**: Hauptzollamtliche Kontrolle.

## Pruef-Raster

- [ ] Wirtschaftlicher Interessentest dokumentiert und bestanden?
- [ ] Bewilligung aktuell gueltig und Standorte vollstaendig erfasst?
- [ ] Lagerbuchhaltung mit Ausbeute-Koeffizienten und Mengenueberwachung eingerichtet?
- [ ] INF-Blatt für Mehrparteienverfahren beantragt?
- [ ] Gesamtabrechnung fristgerecht (Erledigungsfrist aus Bewilligung) erstellt?
- [ ] Nicht veredelter Restbestand korrekt behandelt (Wiederausfuhr, Ueberfuehung in freien Verkehr)?

## Typische Fallstricke

- Ausbeute-Koeffizient zu hoch angesetzt fuehrt zu Zollschuldrisiko bei Gesamtabrechnung.
- Fristversaeumnis bei Erledigungsfrist loest Zollschuld für Gesamtmenge aus.
- Aequivalenzwaren ohne spezifische Bewilligungsgrundlage unzulaessig.
- Buchfuehrungs-Luecken bei Unterauftragsvergabe (Lohnveredelung) oft nicht erkannt.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [UZK konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [UZK-DA auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32015R2446)
- [Zoll.de: Aktive Veredelung](https://www.zoll.de/DE/Fachthemen/Zoelle/Besondere-Zollverfahren/Veredelungsverkehr/Aktive-Veredelung/aktive-veredelung_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-aml-kyc-finanzsanktionen`

_Schnittstelle von AML/KYC-Pflichten und Sanktionsrecht: Risikobasierte Kundenpruefung nach GwG (§§ 10-17 GwG) kombiniert mit Sanktionsscreening nach EU-Finanzsanktionsrecht (VO 269/2014 und andere). Identifizierung wirtschaftlich Berechtigter (UBO), Pruefung von PEP-Status und Hochrisikoindikator..._

# AML/KYC und Sanktionen: Risikobasierte Kundenpruefung und Sanktionsscreening

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Bank erhalt Zahlungsauftrag aus UAE mit unklaren UBO-Angaben; Fragestellung Sanktions-Treffer moeglich?
- Handelsunternehmen onboardet neuen Kunden aus der Tuerkei; interne KYC-Abteilung fordert enhanced due diligence.
- Finanzdienstleister prueft, ob Russe mit Oligarchen-Nahbeziehung unter Art. 2 VO 269/2014 faellt.

## Erste Schritte

1. Identifizierungspflicht ausloesen: Ist Geschaeftsbeziehung gemaess §§ 10 GwG begruendet?
2. UBO-Ermittlung nach § 3 GwG und Art. 3 Nr. 6 4. EU-GwRL (AMLD4): Eigentums- und Kontrollstrukturen bis zum natuerllichen Endbegünstigten aufloesen.
3. Sanktionsscreening in konsolidierter EU-Finanzsanktionsliste (OFAC, UK-HMT optional ergaenzend).
4. PEP-Status pruefen (§ 1 Abs. 12 GwG) und erweiterte Sorgfaltspflichten aktivieren.
5. Risikobewertung nach geldwaescherechtlicher Risikoanalyse erstellen.
6. Entscheidung: Kundenbeziehung freigeben, einschraenken oder ablehnen; Meldung an FIU pruefen.

## Rechtsrahmen

- **§§ 10-17 GwG**: Kundensorgfaltspflichten, UBO-Ermittlung, Hochrisikofaelle.
- **Art. 2 VO (EU) 269/2014**: Bereitstellungsverbot für gelistete Personen/Unternehmen (Russland-Sanktionen).
- **Art. 11 VO (EU) 269/2014**: Meldepflicht bei eingefrorenen Geldern.
- **§ 43 GwG**: Verdachtsmeldepflicht an FIU.
- **Zahlungsdiensteaufsichtsgesetz (ZAG)**: Erweiterter Anwendungsbereich für Zahlungsdienstleister.

## Pruef-Raster

- [ ] UBO vollstaendig und belegt ermittelt (25 %-Schwelle und Kontrollpruefung)?
- [ ] Sanktionsscreening mit Trefferprotokoll durchgefuehrt?
- [ ] PEP-Status und Hochrisikoindikatoren bewertet?
- [ ] Abweichende/unklare Angaben des Kunden dokumentiert?
- [ ] Risikoklasse korrekt eingestuft und Massnahmen angemessen?
- [ ] Meldepflicht an FIU geprueft?

## Typische Fallstricke

- Indirektes Eigentum ueber Offshore-Strukturen wird unterschaetzt; nur direkte Anteilseigner pruefen reicht nicht.
- 'Fuzzy Match' bei abweichender Schreibweise des Namens fuehrt zu Nichtentdeckung.
- PEP-Status laeuft nach Amt-Ende weiter (mindestens 12 Monate); kein automatischer Wegfall.
- Sanktions- und GwG-Pruefung werden organisatorisch getrennt durchgefuehrt und kommunizieren nicht.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [GwG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/gwg_2017/index.html)
- [VO (EU) 269/2014 konsolidiert auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0269)
- [EU Finanzsanktionsliste (FSDB)](https://eeas.europa.eu/topics/sanctions-policy/8442/consolidated-list-sanctions_en)
- [BaFin Merkblatt Geldwaeschegesetz](https://www.bafin.de/DE/Aufsicht/Geldwaeschebekaempfung/geldwaeschebekaempfung_node.html)
- [AWG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/awg_2013/index.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-antidumping-ausgleich`

_Antidumping-Ausgleichsmassnahmen nach EU-Grundverordnung (VO (EU) 2016/1036): Identifizierung von TARIC-Antidumping-Massnahmen, Berechnung endgueltiger Antidumping-Zoelle, Ueberpruefen von Ursprungsnachweis und Hersteller-TARIC-Code (Einzelzoll vs. Restzoll). Fallkonstellation: Importeur prueft A..._

# Antidumping-Ausgleich: TARIC-Massnahmen und Herstellerzuordnung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Importeur kauft Solarpaneele aus China; TARIC-Abfrage zeigt Antidumping-Massnahmen. Welcher Zollsatz gilt?
- Stahlhaendler erhaelt Nachzollbescheid, weil Ursprungsnachweise des chinesischen Lieferanten nicht anerkannt.
- Unternehmen importiert Keramik aus Vietnam; fragt nach Antidumping-Risiko und Nullzoll-Optionen.

## Erste Schritte

1. TARIC-Datenbank (ec.europa.eu/taxation_customs/dds2/taric) aufrufen: Massnahmen für KN-Code und Ursprungsland pruefen.
2. Hersteller-ID und TARIC-Unternehmenscode (TARIC ADD-Code) des Lieferanten ermitteln.
3. Individualzoll vs. Restzoll klaeren; Ursprungszeugnis und EU-Anerkennungsstatus pruefen.
4. Antidumping-Zoll auf CIF-Wert berechnen; Vergleich mit eventueller Preisverpflichtung (Price Undertaking).
5. Ueberpruefen ob Befreiungsantrag moeglich (Art. 11 VO 2016/1036: Auslaufrevision).
6. Zollwertdeklaration und Ursprungsdokumentation für Audit-Compliance sicherstellen.

## Rechtsrahmen

- **VO (EU) 2016/1036**: EU-Antidumping-Grundverordnung (Methodik und Verfahren).
- **Art. 1-2 VO 2016/1036**: Dumping-Definition und Schadenstest.
- **UZK Art. 56-63**: Zolltarifanwendung und Praeferenzketten.
- **VO (EU) 952/2013 Art. 59-63**: Ursprungsbestimmung für Antidumpingzwecke.
- **AWG § 21**: Verfahrensbeteiligung bei Handelspolitikuntersuchungen.

## Pruef-Raster

- [ ] TARIC-Massnahmen für exakten KN-Code und Ursprungsland aktuell geprueft?
- [ ] Hersteller-TARIC-Code gueltig und anerkannt?
- [ ] Ursprungsnachweis zulaessig und nachweisbar?
- [ ] CIF-Wert korrekt für Antidumping-Berechnungsgrundlage?
- [ ] Preisverpflichtung (Price Undertaking) aktiv und nutzbar?
- [ ] Rueckerstattungsantrag bei Dumping-Margin-Review moeglich?

## Typische Fallstricke

- TARIC-Massnahmen aendern sich durch Revisionen und Auslaufverfahren laufend; immer tagesaktuelle Abfrage.
- Zusammengesetzte Waren: Antidumpingzoll kann an Bestandteil haengen, nicht am Endprodukt.
- Hersteller-ID des Lieferanten nicht geprueft: Restzoll statt Individualzoll wird faellig.
- Umgehungsrisiko bei Transhipment ueber Drittlaender.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [TARIC-Datenbank Europaeische Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [UZK auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [Zoll.de Antidumping](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollrechtliche-Einfuhrbestimmungen/Besondere-Einfuhrabgaben/besondere-einfuhrabgaben_node.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 AWG
- § 22 AWG
- § 130 OWiG
- § 22 ZollVG
- § 14 AWG
- § 19 AWG
- § 10 ZollVG
- § 10-17 GwG
- § 21 ZollVG
- § 43 GwG
- § 9 AWG
- § 25 UmwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `aussenwirtschaft-antidumping-erstattung-review`

_Erstattung zu viel gezahlter Antidumping-Zoelle und Auslosung von Revisionsverfahren nach Art. 11 VO (EU) 2016/1036: Rueckerstattungsantrag (Art. 11 Abs. 8), Interim-Review und Sunset-Review. Prueft Fristen beim Hauptzollamt und EU-Kommission. Fallkonstellation: Importeur hat ueberhohten Antidump..._

# Antidumping-Erstattung und Review: Margenkorrektur und Rueckforderung

## Arbeitsbereich

Erstattung zu viel gezahlter Antidumping-Zoelle und Auslosung von Revisionsverfahren nach Art. 11 VO (EU) 2016/1036: Rueckerstattungsantrag (Art. 11 Abs. 8), Interim-Review und Sunset-Review. Prueft Fristen beim Hauptzollamt und EU-Kommission. Fallkonstellation: Importeur hat ueberhohten Antidumping-Zoll gezahlt und moechte Erstattung oder Margenkorrektur. Output: Erstattungsantrag mit Kalkulationsnachweis. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Importeur hat in den letzten drei Jahren Antidumping-Zoelle gezahlt; moechte pruefen, ob tatsaechliches Dumping nachgewiesen wurde.
- Hersteller in China hat Dumping-Marge signifikant reduziert; Lieferant moechte Review-Antrag stellen.
- Massnahme gegen bestimmten Warenwert laeuft in 12 Monaten aus; Frage nach Sunset-Review und Auswirkungen.

## Erste Schritte

1. Pruefen ob Erstattungsantrag nach Art. 11 Abs. 8 VO 2016/1036 in Frage kommt (Zoll bezahlt, Exportpreis gestiegen).
2. Antrag auf Erstattung beim Hauptzollamt (DE) und koordiniert mit EU-Kommission einreichen.
3. Interim-Review-Antrag (Art. 11 Abs. 3) bei geaenderter Dumping-Situation des Exporteurs.
4. Sunset-Review-Antrag (Art. 11 Abs. 2) bei Auslauf der Massnahme vorbereiten.
5. Preisvergleich und Dumping-Margin-Dokumentation für Review aufbereiten.
6. Fristen beachten: Erstattungsantrag innerhalb 6 Monate nach Zollzahlung.

## Rechtsrahmen

- **Art. 11 VO (EU) 2016/1036**: Erstattung, Interim-Review, Sunset-Review und Neuzulassung.
- **Art. 11 Abs. 8 VO 2016/1036**: Erstattungsantragsverfahren bei gesunkenem Exportpreis.
- **UZK Art. 116-123**: Allgemeines Zollerstattungsrecht.
- **Art. 21 UZK-IA**: Antragstellung und Fristen für Zollerstattung.
- **§ 21 ZollVG**: Nationale Kontrollbefugnisse.

## Pruef-Raster

- [ ] Zollzahlung dokumentiert und innerhalb der Erstattungsfrist (6 Monate)?
- [ ] Exportpreis nach Erhebung des Antidumping-Zolls gestiegen?
- [ ] Dumping-Margin-Berechnung und Preisvergleich aufbereitet?
- [ ] Interim-Review-Antrag oder Sunset-Review-Antrag sinnvoll?
- [ ] Koordination mit EU-Kommission eingeplant?
- [ ] Zollbescheide und Einfuhrdokumentation vollstaendig gesichert?

## Typische Fallstricke

- Erstattungsantrag muss koordiniert mit Hauptzollamt und Kommission gestellt werden.
- Sunset-Review-Antrag hat strenge Fristen; bei Versaeumnis bleiben Massnahmen automatisch in Kraft.
- Beweislast für gesunkenem Exportpreis liegt beim Importeur; unzureichende Dokumentation fuehrt zu Ablehnung.
- Preisverpflichtungsbruch des Exporteurs kann Erstattungsantrag gefaehrden.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [UZK Art. 116-123 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0952)
- [EU Kommission Antidumping-Verfahren](https://ec.europa.eu/trade/policy/accessing-markets/trade-defence/actions-against-imports-into-the-eu/anti-dumping/)
- [Zoll.de Erstattungen](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollanmeldung-Zollverfahren/Erstattung-Erlass/erstattung-erlass_node.html)

---

## Skill: `aussenwirtschaft-antidumping-taric-massnahmen`

_Identifizierung und Anwendung handelspolitischer Schutzmassnahmen (Antidumping, Ausgleichszoll, Safeguards) im TARIC-System: Zuordnung der KN-Position, Ursprungsland und Hersteller zu geltenden Massnahmen. Ermittelt TARIC-Zusatzcode, Preisverpflichtungen und Schwellenwerte für relevante Waren. Ou..._

# TARIC-Massnahmen: Antidumping und Ausgleichszoelle in der Zollabfertigung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Mandantenfall

- Zollagent findet beim Import von Stahlrohren aus China drei konkurrierende Massnahmen-Codes in TARIC.
- Importeur zahlt falsche Antidumping-Zoelle weil Hersteller-TARIC-Code veraltet.
- Unternehmen importiert Fahrraeder aus Kambodscha; Frage ob EU-Antiumgehungsmassnahme greift.

## Erste Schritte

1. KN-8-Steller und Ursprungsland klar bestimmen; TARIC-Abfrage mit aktueller Fassung.
2. Alle gueltigen Massnahmen (ADD, CVD, Safeguard, Surveillance) für den Code auflisten.
3. Hersteller-Code (TARIC ADD-Zusatzcode) beim Lieferanten erfragen und validieren.
4. Preisverpflichtungen (Price Undertakings) und Mindestimportpreise pruefen.
5. Freimengen und Zollkontingente (TRQ) pruefen, falls Massnahme-Ausnahmen bestehen.
6. Massnahmen-Stand in Dokumentation vermerken (Datum, TARIC-Version).

## Rechtsrahmen

- **UZK Art. 56 Abs. 2**: Massnahmen des Gemeinsamen Zolltarifs inkl. Antidumping.
- **VO (EU) 2016/1036**: Antidumping-Grundverordnung.
- **VO (EU) 2016/1037**: Ausgleichszoll-Grundverordnung (Subventionen).
- **VO (EU) 2015/478**: Gemeinsame Einfuhrregelung und Safeguards.
- **Durchfuehrungsverordnungen**: Einzelne ADD- und CVD-Massnahmen per Durchfuehrungs-VO.

## Pruef-Raster

- [ ] KN-Code und Ursprungsland korrekt für TARIC-Abfrage?
- [ ] Alle aktiven Massnahmen (ADD, CVD, Safeguard) aufgelistet?
- [ ] Hersteller-TARIC-Code validiert und nicht gesperrt?
- [ ] Preisverpflichtungs-Compliance dokumentiert?
- [ ] Freimengen/Kontingente (TRQ) geprueft?
- [ ] Massnahmen-Stand mit Datum protokolliert?

## Typische Fallstricke

- TARIC-Datenbank mit Stand-Datum nutzen; keine Offline-Auszuege aus Vormonat.
- Mehrere parallele Massnahmen (ADD + CVD + Safeguard) sind kumulativ anwendbar.
- Hersteller-ID kann sich durch Fusionen oder Rueckzug der Anerkennung aendern.
- Massnahmen gelten per Einreihung; marginale Unterschiede im KN-Code vermeiden.

## Schnittstellen zu anderen Skills

Dieser Skill kann mit thematisch benachbarten Skills kombiniert werden, insbesondere:
- Sanktionsscreening und Listenpruefung: `aussenwirtschaft-sanktionsscreening-fuzzy-match`
- Exportkontrollklassifizierung: `aussenwirtschaft-gueterlisten-klassifizierung`
- Freiwillige Offenlegung gegenueber BAFA oder Hauptzollamt: `aussenwirtschaft-freiwillige-offenlegung-bafa-zoll`
- Interne Compliance-Programme: `aussenwirtschaft-icp-kontrollsystem`

## Qualitaetsanforderungen

- Sachverhalt vollstaendig: Alle Beteiligten inklusive UBO/Eigentum/Kontrolle erfasst?
- Normverweise konkret: Artikel und Absatz zitiert, nicht nur Verordnungsnummer?
- Quellenstand datiert: Sanktionslisten, TARIC, Gueltigkeitsdaten dokumentiert?
- Sofortmassnahmen klar: Stop-Ship, Hold, Eskalation explizit benannt wenn Risiko rot?
- Audit-Trail vollstaendig: Entscheidung, Begruendung, Verantwortlicher, Frist?
- Output mandantentauglich: Kein Fachwort ohne Erlaeuterung für Compliance und Business?
- Vertraulichkeit: Mandatsgeheimnisse nicht in ungesicherte externe Systeme eingeben.

## Quellen

- [TARIC-Datenbank der EU-Kommission](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp)
- [VO (EU) 2016/1036 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1036)
- [VO (EU) 2016/1037 auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R1037)
- [Zoll.de Besondere Einfuhrabgaben](https://www.zoll.de/DE/Fachthemen/Zoelle/Zollrechtliche-Einfuhrbestimmungen/Besondere-Einfuhrabgaben/besondere-einfuhrabgaben_node.html)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

