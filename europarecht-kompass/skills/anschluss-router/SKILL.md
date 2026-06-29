---
name: anschluss-router
description: "Einstieg, Schnelltriage und Fallrouting im Europarecht Kompass-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständi..."
---

# Europarecht-Kompass — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: AEUV Art. 263 Nichtigkeitsklage 2 Monate, Art. 265 Untätigkeitsklage 2 Monate, Art. 267 Vorlage jederzeit, Vertragsverletzungsverfahren Art. 258 unbefristet.
- Tragende Normen verifizieren: EUV, AEUV (insb. Art. 4, 5, 18, 20, 21, 34, 49, 56, 101, 102, 107, 108, 263, 267, 288, 340), GRCh, EU-VO (Beispiele 2016/679 DSGVO, 2024/1689 KI-VO, 139/2004 FKVO), EU-Richtlinien, EuGH-Rechtsprechung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: EU-Kommission, Rat, Europäisches Parlament, EuGH, EuG, Mitgliedstaaten, nationale Gerichte (Vorlage Art. 267 AEUV), Bundesregierung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Vorlagebeschluss Art. 267 AEUV, Nichtigkeitsklage, Beschwerde an EU-KOM, Stellungnahme im Vertragsverletzungsverfahren, Notifizierung, EuGH-Urteilsbeleg — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Europarecht Kompass**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting.

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
| `europarecht-beihilfen-vergaben` | Beihilfenrecht und Vergaberecht prüfen wenn staatliche Förderung oder öffentlicher Auftrag in Frage steht. Art. 107 108 AEUV Beihilfeverbote §§ 97 ff. GWB Vergaberecht. Prüfraster: Beihilfebegriff Ausnahmen… |
| `europarecht-delegierte-durchfuehrungsakte` | Delegierte Rechtsakte und Durchführungsrechtsakte der EU einordnen und deren Verbindlichkeit prüfen. Art. 290 291 AEUV Delegierung. Prüfraster: Kategorie Widerruf Einwand Verbindlichkeit nationaler Umsetzungsbedarf… |
| `europarecht-deutscher-denkfehler-scanner` | Typische deutsche Denkfehler im Umgang mit EU-Recht erkennen und korrigieren. Art. 267 AEUV Vorrangprinzip EuGH-Judikatur. Prüfraster: fehlende Europarechtskonformität verkannte Direktwirkung uebergangene… |
| `europarecht-gesetzgebung-trilog` | Europaeisches Gesetzgebungsverfahren und Trilog-Verhandlungen einordnen wenn EU-Regelung in Entstehung ist. Art. 289 294 AEUV ordentliches Gesetzgebungsverfahren. Prüfraster: Verfahrensstand Kompromisstext… |
| `europarecht-grundfreiheiten-binnenmarkt` | Grundfreiheiten des Binnenmarkts prüfen wenn grenzüberschreitende Wirtschaftstätigkeit oder nationale Beschraenkung in Frage steht. Art. 34 45 49 56 63 AEUV Warenverkehr Personenfreizuegigkeit Niederlassungsfreiheit.… |
| `europarecht-grundrechte-charta` | EU-Grundrechtecharta anwenden wenn EU-Recht vollzogen wird oder Mitgliedstaat im Anwendungsbereich des EU-Rechts handelt. Art. 51 GRC Anwendungsbereich Art. 6 EUV. Prüfraster: Anwendungsbereich Art. 51 GRC beruertes… |
| `europarecht-klagearten-eugh` | Klagemoglichkeiten vor dem EuGH und EuG einordnen und Zulassigkeitsvoraussetzungen prüfen. Art. 263 265 268 340 AEUV Nichtigkeitsklage Untätigkeitsklage Schadensersatz. Prüfraster: Klageart Klagebefugnis Fristen… |
| `europarecht-kommandocenter` | Einstiegspunkt für Europarechtsmandate: Rechtsgebiet bestimmen relevante Normen identifizieren Bearbeitungsroute festlegen. AEUV EUV GRC EU-Sekundaerrecht. Prüfraster: Sachverhalt EU-Rechtsbezug Rechtsgebiet Route… |
| `europarecht-mandantenmemo` | Mandantenmemo zu EU-Rechtsfragen verstaendlich und praxisorientiert verfassen. AEUV EUV EU-Sekundaerrecht Grundfreiheiten. Prüfraster: Sachverhaltszusammenfassung Rechtslage Handlungsoptionen Risiken Empfehlung… |
| `europarecht-nationales-verfahren-effektivitaet` | EU-Rechtsvorgaben zum effektiven nationalen Rechtsschutz prüfen wenn nationales Verfahren EU-Rechte beeintraechtigt. Art. 47 GRC Art. 19 EUV Effektivitaetsprinzip. Prüfraster: Effektivitaetsgrundsatz… |
| `europarecht-quality-gate` | EU-Rechtsgutachten oder -Schriftsatz auf typische Fehler und Luecken prüfen vor Versand. Art. 267 AEUV EuGH-Judikatur Vorrangprinzip. Prüfraster: Vorlagepflicht uebersehen Direktwirkung verkannt Normhierarchie… |
| `europarecht-richtlinie-umsetzung` | EU-Richtlinie in nationales Recht umsetzen oder Umsetzungsdefizit prüfen. Art. 288 AEUV Richtlinienwirkung Art. 267 AEUV Vorabentscheidung. Prüfraster: Umsetzungsfrist Umsetzungsdefizit Direktwirkung… |
| `europarecht-simulation-behoerde-gericht` | Verhandlung vor EU-Behörde oder nationalem Gericht mit EU-Rechtsbezug simulieren und Argumentation testen. Art. 267 AEUV Art. 263 AEUV EuGH-Verfahren. Prüfraster: Argumente Gegenargumente Vorlageentscheidung… |
| `europarecht-verordnung-beschluss-soft-law` | EU-Verordnungen Beschlüsse und Soft-Law-Instrumente einordnen und deren Verbindlichkeit prüfen. Art. 288 AEUV EU-Rechtsquellen. Prüfraster: Rechtsquellentyp Verbindlichkeit Direktwirkung nationaler Anpassungsbedarf… |
| `europarecht-vertragsverletzung-durchsetzung` | Vertragsverletzungsverfahren der EU-Kommission gegen Mitgliedstaaten einordnen oder Reaktion eines Mitgliedstaats vorbereiten. Art. 258 260 AEUV Vertragsverletzung. Prüfraster: Verletzungshandlung Mahnschreiben Klage… |
| `europarecht-vorlageverfahren-art-267` | Vorabentscheidungsersuchen nach Art. 267 AEUV vorbereiten oder Vorlagepflicht eines nationalen Gerichts prüfen. Art. 267 AEUV Vorabentscheidungsverfahren. Prüfraster: Vorlagepflicht acte-clair-Doktrin Vorlagefrage… |
| `europarecht-vorrang-unmittelbare-wirkung` | Vorrang des EU-Rechts und unmittelbare Wirkung von EU-Normen prüfen wenn nationales Recht entgegensteht. Art. 288 AEUV Costa v. ENEL Van Gend en Loos EuGH-Judikatur. Prüfraster: Vorrangprinzip Kollision nationales… |
| `europarecht-wettbewerb-kartell` | Kartell- und Wettbewerbsrecht nach Art. 101 102 AEUV prüfen wenn Absprachen Marktmissbrauch oder Zusammenschluesse in Frage stehen. Art. 101 102 AEUV § 1 GWB VO 1/2003. Prüfraster: Kartellverbot Marktabgrenzung… |

## Worum geht es?

Dieses Plugin korrigiert typische deutsche Denkfehler im Umgang mit EU-Recht und unterstuetzt Anwaelte, Berater und Behörden bei der systematischen Bearbeitung europarechtlicher Mandate. Es deckt die Kernbereiche des EU-Primaerrechts (AEUV, EUV, GRC) und des Sekundaerrechts (Verordnungen, Richtlinien, Beschlüsse, Soft Law) ab.

Schwerpunkte sind: Vorrangprinzip und unmittelbare Wirkung, Richtlinienumsetzung und -konforme Auslegung, Grundfreiheiten des Binnenmarkts, EU-Grundrechtecharta, Beihilfen- und Vergaberecht, Vorlageverfahren nach Art. 267 AEUV, Klagearten vor EuGH und EuG sowie effektiver nationaler Rechtsschutz. Das Plugin richtet sich ausdrucklich gegen die Tendenz, EU-Recht durch nationale Brillen zu lesen.

## Wann brauchen Sie diese Skill?

- Ein nationales Gericht oder eine Behörde wendet nationales Recht an, das moeglicherweise EU-Recht widerspricht.
- Sie wollen prüfen, ob eine EU-Richtlinie in Deutschland korrekt umgesetzt wurde oder ob ein Umsetzungsdefizit besteht.
- Sie begleiten ein Unternehmen mit grenzueberschreitender Taetigkeit und müssen Grundfreiheitsverstoss prüfen.
- Ein nationales Gericht steht vor der Frage, ob es den EuGH nach Art. 267 AEUV anrufen muss.
- Sie arbeiten ein EU-Rechtsgutachten oder einen Schriftsatz und wollen es vor Versand auf typische Fehler prüfen.

## Fachbegriffe (kurz erklaert)

- **Vorrang des EU-Rechts** — EU-Recht geht nationalem Recht vor; entgegenstehendes nationales Recht ist unanwendbar (Costa v. ENEL, EuGH 1964).
- **Unmittelbare Wirkung** — EU-Normen können Rechte und Pflichten für Einzelne begruenden, ohne nationalem Umsetzungsrecht zu beduerfan (Van Gend en Loos, EuGH 1963); Richtlinien nur vertikal unmittelbar wirksam.
- **Richtlinienkonforme Auslegung** — Nationales Recht ist so weit wie möglich im Licht des Wortlauts und Zwecks der Richtlinie auszulegen.
- **Francovich-Staatshaftung** — Mitgliedstaat haftet für Schaden durch fehlerhafte oder ausgebliebene Richtlinienumsetzung.
- **Vorlagepflicht** — Letztinstanzliche Gerichte müssen EU-Rechtsfragen dem EuGH vorlegen (Art. 267 Abs. 3 AEUV); Ausnahme: acte-clair-Doktrin.
- **Grundfreiheiten** — Warenverkehr (Art. 34 AEUV), Personenfreizuegigkeit (Art. 45 AEUV), Niederlassungsfreiheit (Art. 49 AEUV), Dienstleistungsfreiheit (Art. 56 AEUV), Kapitalverkehr (Art. 63 AEUV).
- **Art. 51 GRC** — EU-Grundrechtecharta gilt nur, wenn Mitgliedstaat EU-Recht vollzieht oder im Anwendungsbereich des EU-Rechts handelt.
- **Beihilfeverbot** — Art. 107 AEUV verbietet staatliche Beihilfen, die den Wettbewerb verfaelschen; notifizierungspflichtig bei Kommission.

## Rechtsgrundlagen

- Art. 267 AEUV — Vorlageverfahren; Vorabentscheidung des EuGH.
- Art. 258 und 260 AEUV — Vertragsverletzungsverfahren der Kommission.
- Art. 263 und 265 AEUV — Nichtigkeitsklage und Untaetigkeitsklage vor EuGH/EuG.
- Art. 288 AEUV — Rechtsquellen: Verordnung, Richtlinie, Beschluss, Empfehlung.
- Art. 289 und 294 AEUV — Ordentliches Gesetzgebungsverfahren und Trilog.
- Art. 290 und 291 AEUV — Delegierte Rechtsakte und Durchfuehrungsrechtsakte.
- Art. 34 und 36 AEUV — Warenverkehrsfreiheit und Rechtfertigungsgruende.
- Art. 51 und 52 GRC — Anwendungsbereich und Schranken der EU-Grundrechtecharta.
- Art. 107 und 108 AEUV — Beihilfeverbot und Notifizierungspflicht.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandat aufgleisen: Skill `europarecht-kommandocenter` für EU-Rechtsbezug, Rechtsgebiet und Route.
2. Deutschen Denkfehler ausschliessen: `europarecht-deutscher-denkfehler-scanner`.
3. Rechtsquelle einordnen: `europarecht-verordnung-beschluss-soft-law` oder `europarecht-richtlinie-umsetzung`.
4. Materielles Rechtsproblem prüfen: Grundfreiheiten, Charta, Beihilfen, Kartell je nach Mandat.
5. Verfahren bestimmen: Vorlage, Klage, Vertragsverletzung, Simulation je nach Konstellation.

## Skill-Tour (was gibt es hier?)

**Einstieg und Qualitaetssicherung**

- `europarecht-kommandocenter` — Rechtsgebiet bestimmen, relevante Normen identifizieren, Bearbeitungsroute festlegen.
- `europarecht-deutscher-denkfehler-scanner` — Typische deutsche Fehler im EU-Recht erkennen und korrigieren.
- `europarecht-quality-gate` — EU-Rechtsgutachten oder Schriftsatz auf Fehler und Luecken prüfen.
- `europarecht-mandantenmemo` — Mandantenmemo zu EU-Rechtsfragen praxisorientiert verfassen.

**Rechtsquellen und Normenhierarchie**

- `europarecht-vorrang-unmittelbare-wirkung` — Vorrang des EU-Rechts und unmittelbare Wirkung von EU-Normen prüfen.
- `europarecht-richtlinie-umsetzung` — Umsetzungsdefizit prüfen, Direktwirkung, richtlinienkonforme Auslegung, Francovich.
- `europarecht-verordnung-beschluss-soft-law` — Verordnungen, Beschlüsse und Soft-Law einordnen und Verbindlichkeit prüfen.
- `europarecht-delegierte-durchfuehrungsakte` — Delegierte Rechtsakte und Durchfuehrungsrechtsakte einordnen.

**Grundfreiheiten und Grundrechte**

- `europarecht-grundfreiheiten-binnenmarkt` — Grundfreiheiten prüfen bei grenzueberschreitender Taetigkeit oder nationaler Beschraenkung.
- `europarecht-grundrechte-charta` — EU-Grundrechtecharta anwenden; Anwendungsbereich Art. 51 GRC.

**Wettbewerb und Beihilfen**

- `europarecht-wettbewerb-kartell` — Kartell- und Wettbewerbsrecht nach Art. 101 und 102 AEUV.
- `europarecht-beihilfen-vergaben` — Beihilfenrecht Art. 107 und 108 AEUV und Vergaberecht §§ 97 ff. GWB.

**Verfahren vor EuGH und nationalem Gericht**

- `europarecht-vorlageverfahren-art-267` — Vorabentscheidungsersuchen nach Art. 267 AEUV vorbereiten oder Vorlagepflicht prüfen.
- `europarecht-klagearten-eugh` — Klagemoeglichkeiten vor EuGH und EuG; Nichtigkeitsklage, Untaetigkeit, Schadensersatz.
- `europarecht-vertragsverletzung-durchsetzung` — Vertragsverletzungsverfahren einordnen und Reaktion vorbereiten.
- `europarecht-nationales-verfahren-effektivitaet` — Effektivitaets- und Äquivalenzgrundsatz im nationalen Verfahren.
- `europarecht-simulation-behoerde-gericht` — Argumentation vor EU-Behörde oder nationalem Gericht simulieren.

**Gesetzgebung**

- `europarecht-gesetzgebung-trilog` — EU-Gesetzgebungsverfahren und Trilog-Verhandlungen einordnen.

## Worauf besonders achten

- **Richtlinie ist kein Gesetz** — Eine nicht umgesetzte Richtlinie wirkt nur vertikal (gegen den Staat), nicht horizontal zwischen Privaten; die direkte Anwendbarkeit gegenueber Privaten ist kein Automatismus.
- **Vorlagepflicht ernst nehmen** — Letztinstanzliche Gerichte müssen vorlegen; die acte-clair-Doktrin ist eng auszulegen; Ablehnung ohne Vorlagepruefung ist ein Verfahrensfehler.
- **GRC-Anwendungsbereich prüfen** — Die EU-Grundrechtecharta gilt nicht bei rein nationalem Sachverhalt; Art. 51 GRC ist Anwendungsvoraussetzung, nicht Option.
- **Beihilfe: Notifizierung vor Auszahlung** — Nicht notifizierte Beihilfen können zurueckgefordert werden; der Vertrauensschutz des Beguenstigten ist eng.
- **Soft Law und Durchfuehrungsrechtsakte unterscheiden** — Empfehlungen und Leitlinien sind nicht verbindlich, haben aber Auslegungsrelevanz; delegierte Rechtsakte und Durchfuehrungsrechtsakte hingegen sind verbindlich.

## Typische Fehler

- Richtlinienkonforme Auslegung wird nicht versucht, obwohl das nationale Recht noch Auslegungsspielraum lässt.
- Vorlage nach Art. 267 AEUV wird verweigert, obwohl acte-clair-Kriterien nicht erfullt sind.
- GRC wird angewendet, obwohl kein EU-Recht vollzogen wird (rein nationaler Sachverhalt).
- Beihilfe wird ausgezahlt, ohne Notifizierungspflicht nach Art. 108 Abs. 3 AEUV zu prüfen.
- Delegierter Rechtsakt und Durchfuehrungsrechtsakt werden verwechselt, was zu falschen Widerrufsfristen fuehrt.

## Quellen und Aktualitaet

- Stand: 05/2026
- AEUV und EUV in der geltenden Fassung
- GRC (EU-Grundrechtecharta) in der geltenden Fassung
- EuGH-Rechtsprechung bis 05/2026

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 267 AEUV
- Art. 263 AEUV
- Art. 258 AEUV
- Art. 288 AEUV
- Art. 265 AEUV
- Art. 19 EUV
- Art. 6 EUV
- Art. 260 AEUV
- Art. 294 AEUV
- Art. 108 AEUV
- Art. 228 AEUV
- Art. 227 AEUV

### Leitentscheidungen

- EuGH C-6/64
