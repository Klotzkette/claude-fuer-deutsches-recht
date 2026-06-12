---
name: regulierung-start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im DSA DMA Digitalregulierung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eige..."
---

# DSA DMA und Digitalregulierung EU — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSA Art. 16 Notice-and-Action unverzügliche Reaktion, Art. 24 jährlicher Transparenzbericht, Art. 34 Risikoassessment jährlich/bei Bedarf, DMA Art. 11 Compliance-Bericht 6 Monate nach Benennung.
- Tragende Normen verifizieren: Digital Services Act (VO 2022/2065) Art. 4-15 (Haftung), 16-22 (Meldung), 24-32 (mittelgroße/VLOP), 33-43 (sehr große), 50-66 (Aufsicht), Digital Markets Act (VO 2022/1925) Art. 3 (Gatekeeper), 5-7 (Pflichten), DDG, TMG (außer Kraft), NetzDG (auslaufend) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter Vermittlungsdienst / Hosting / Online-Plattform / sehr große Online-Plattform (VLOP) / Suchmaschine (VLOSE), BNetzA als DSC, EU-KOM (DMA-Vollzug), nationaler Koordinator, Beschwerdeführer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: AGB nach Art. 14 DSA, Transparenzbericht, Risikoassessment, Compliance-Officer-Konzept, Streitbeilegung Art. 21 DSA, DSC-Meldung, DMA-Compliance-Bericht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **DSA DMA Digitalregulierung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege.

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
| `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` | Account-Sperre oder Inhaltsentfernung durch soziales Netzwerk anfechten: Nutzer oder Unternehmen ist von Plattform gesperrt worden. Normen: DSA (EU) 2022/2065 Art. 17 (Begründungspflicht), Art. 20 (internes… |
| `digitalregulierung-pyramide-check` | Sachverhalt den richtigen EU-Digitalregulierungs-Rechtsakten zuordnen: Anwalt oder Unternehmen fragt welche Regulierung greift. Normen: DSA (EU) 2022/2065, DMA (EU) 2022/1925, Data Act (EU) 2023/2854, DGA, AI Act (EU)… |
| `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` | Schnittstellen zwischen DSA/DMA und DSGVO, P2B-VO und § 19a GWB analysieren: Mehrere Regelwerke treffen gleichzeitig auf einen Sachverhalt. Normen: Art. 2 Abs. 4 DSA (kein Verdrangen DSGVO), Art. 1 Abs. 5 DMA, P2B-VO… |
| `dma-gatekeeper-schwellen-und-kernplattformdienste` | Gatekeeper-Designation nach Art. 3 DMA prüfen: Plattform-Betreiber will wissen ob DMA-Pflichten gelten oder Kommission hat Designation eingeleitet. Normen: DMA (EU) 2022/1925 Art. 3 (Designation-Voraussetzungen), Art.… |
| `dsa-art-34-systemische-risikobewertung` | Jaehrliche Risikobewertung nach Art. 34 DSA für VLOP/VLOSE durchführen: Große Plattform muss Risikobewertung dokumentieren oder Berater unterstuetzt Compliance-Team. Normen: DSA (EU) 2022/2065 Art. 34 (vier… |
| `dsa-art-40-forschungsdatenzugang-algorithmen` | Forschungsdatenzugang nach Art. 40 DSA beantragen oder gewaehren: Forscher will Plattformdaten erhalten oder Plattform muss Zugang einrichten. Normen: DSA (EU) 2022/2065 Art. 40 (vetted researchers, DSC-Koordinierung),… |
| `dsa-vlop-vlose-einordnung-und-pflichten` | VLOP (sehr große Online-Plattform) oder VLOSE (sehr große Suchmaschine) Einordnung und Pflichten-Katalog: Plattform prüft ob Designation droht oder besteht. Normen: DSA (EU) 2022/2065 Art. 33 (Designation… |
| `klage-gegen-vlop-einordnung-art-263-aeuv` | Nichtigkeitsklage gegen Designations-Beschluss der Kommission (VLOP nach DSA oder Gatekeeper nach DMA): Grossplattform will Designation anfechten. Normen: Art. 263 Abs. 4 AEUV (Nichtigkeitsklage EuG), Art. 33 DSA… |
| `zustellung-und-vertreter-art-13-dsa-art-37-dma` | Zustellung gegen Plattform mit Sitz außerhalb der EU und EU-Vertreter-Pflichten: Kläger will Schriftstuecke zustellen oder Behörde will Plattform erreichen. Normen: DSA (EU) 2022/2065 Art. 13… |

## Worum geht es?

Dieses Plugin ist der strukturierte Einstiegspunkt für die EU-Digitalregulierung. Es hilft dabei, den richtigen Rechtsakt für einen konkreten Sachverhalt zu identifizieren und die jeweils zuständige Pflichtenmatrix zu aktivieren. Die EU-Digitalregulierung besteht aus einem dichten Regelwerk, das sich nach Akteurstyp, Dienst-Typ, Datentyp und Risikoklasse staffelt: Digital Services Act (DSA, VO 2022/2065), Digital Markets Act (DMA, VO 2022/1925), Data Act (VO 2023/2854), Data Governance Act (DGA), AI Act (VO 2024/1689), NIS-2, DORA, CRA, eIDAS 2.0, Digitale-Dienste-Gesetz (DDG), P2B-VO und § 19a GWB.

Das Plugin richtet sich an Anwaelte, Compliance-Verantwortliche und Unternehmensjuristen, die mit der Pflichtendichte der EU-Digitalregulierung umgehen müssen. Es ist kein Rechtsberatungsersatz.

## Wann brauchen Sie diese Skill?

- Unternehmen fragt, ob es als VLOP (sehr große Online-Plattform) oder VLOSE (sehr große Suchmaschine) nach DSA einzustufen ist.
- Plattformbetreiber moechte wissen, ob eine DMA-Gatekeeper-Designation droht und welche Pflichten folgen.
- Nutzer oder Unternehmen wurde von einer Plattform gesperrt und will die DSA-Beschwerdewege nutzen.
- Anwalt muss feststellen, welche von mehreren EU-Digitalakten auf einen Sachverhalt gleichzeitig anwendbar sind.
- Grossplattform muss eine Risikobewertung nach Art. 34 DSA dokumentieren oder Forschungsdatenzugang nach Art. 40 DSA einrichten.

## Fachbegriffe (kurz erklaert)

- **DSA (Digital Services Act)** — EU-Verordnung 2022/2065; regelt Haftung und Pflichten von Vermittlungsdiensten, Online-Plattformen, VLOP und VLOSE.
- **DMA (Digital Markets Act)** — EU-Verordnung 2022/1925; regelt Pflichten für Gatekeeper bei Kernplattformdiensten.
- **VLOP** — Sehr große Online-Plattform nach Art. 33 DSA; Designierungsschwelle 45 Mio. monatlich aktive Nutzer in der EU.
- **Gatekeeper** — Designierter Kernplattformdienst-Betreiber nach Art. 3 DMA; quantitative Schwellen und qualitative Designierung durch die Kommission.
- **Kernplattformdienste** — Abschliessender Katalog in Art. 2 Nr. 2 DMA: soziale Netzwerke, App-Stores, Suchmaschinen, Werbenetzwerke usw.
- **Systemisches Risiko** — Art. 34 DSA: VLOPs müssen jaehrlich vier Risikoarten bewerten (illegale Inhalte, Grundrechte, Diskurs/Wahlen, Minderjaerige).
- **P2B-VO** — Plattform-zu-Business-Verordnung (VO 2019/1150); regelt Bedingungen in Handelsbeziehungen zwischen Plattformen und gewerblichen Nutzern.
- **DDG** — Digitale-Dienste-Gesetz; nationales Ausfuehrungsgesetz zum DSA in Deutschland.

## Rechtsgrundlagen

- DSA (EU) 2022/2065 — Digital Services Act; insb. Art. 13 (Vertreter), Art. 17 (Begruendungspflicht), Art. 20-23 (Beschwerdesystem), Art. 33-43 (VLOP-Pflichten).
- DMA (EU) 2022/1925 — Digital Markets Act; insb. Art. 2-3 (Gatekeeper), Art. 5-7 (Pflichten), Art. 37 (Vertreter).
- Art. 263 Abs. 4 AEUV — Nichtigkeitsklage gegen Designierungsbeschluss.
- P2B-VO (EU) 2019/1150 — Plattform-Nutzer-Beziehungen.
- § 19a GWB — Unterhalb DMA-Schwellen: ergaenzende nationale Regulierung besonders marktmaechtiger Unternehmen.
- DDG §§ 1 ff. — Nationales Ausfuehrungsrecht zum DSA.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Sachverhalt einordnen: Skill `digitalregulierung-pyramide-check` für die richtige Regulierungsebene.
2. Schnittstellen identifizieren: `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` bei Mehrrechtsakten.
3. Spezifischen Pflichtenkatalog aktivieren: VLOP-Check, Gatekeeper-Check, Account-Sperre oder Forschungsdatenzugang.
4. Verfahren und Klagewege klaren: Beschwerde, Klage oder Zustellungsfragen.
5. Eilrechtsschutz prüfen bei Sperren oder Designierungsbeschluessen.

## Skill-Tour (was gibt es hier?)

**Einstieg und Triage**

- `digitalregulierung-pyramide-check` — Sachverhalt den richtigen EU-Digitalregulierungs-Rechtsakten zuordnen; Routing.
- `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` — Schnittstellen zwischen DSA/DMA und DSGVO, P2B-VO, § 19a GWB analysieren.

**DSA-spezifisch**

- `dsa-vlop-vlose-einordnung-und-pflichten` — VLOP/VLOSE-Einordnung und Pflichtenkatalog Art. 33 bis 43 DSA.
- `dsa-art-34-systemische-risikobewertung` — Jaehrliche Risikobewertung nach Art. 34 DSA für VLOP/VLOSE durchfuehren.
- `dsa-art-40-forschungsdatenzugang-algorithmen` — Forschungsdatenzugang nach Art. 40 DSA beantragen oder einrichten.
- `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` — Account-Sperre anfechten; Stufenmodell Art. 17-21 DSA; Klageschrift.

**DMA-spezifisch**

- `dma-gatekeeper-schwellen-und-kernplattformdienste` — Gatekeeper-Designation nach Art. 3 DMA prüfen; Pflichtenkatalog.

**Klagewege und Verfahren**

- `klage-gegen-vlop-einordnung-art-263-aeuv` — Nichtigkeitsklage gegen Designierungsbeschluss vor EuG.
- `zustellung-und-vertreter-art-13-dsa-art-37-dma` — Zustellung gegen Plattform mit Sitz ausserhalb der EU; EU-Vertreter-Pflichten.

## Worauf besonders achten

- **DSA und DMA sind parallel anwendbar** — Eine Plattform kann gleichzeitig VLOP (DSA) und Gatekeeper (DMA) sein; die Pflichten kumulieren sich.
- **Schwellenwerte sind dynamisch** — Meldepflicht nach Art. 24 Abs. 3 DSA bei Erreichen der Nutzerschwelle; Kommission designiert unabhaengig von Meldestand.
- **DSA verdraengt DSGVO nicht** — Art. 2 Abs. 4 DSA stellt klar, dass DSGVO vorgeht; DSA-Compliance schutzt nicht vor DSGVO-Bussgeld.
- **§ 19a GWB als Luecken-Fuelung** — Unterhalb DMA-Schwellen greift das BKartA auf § 19a GWB zurueck; Unternehmen müssen beide Ebenen im Blick haben.
- **Zustellung gegen ausländische Plattformen** — EU-Vertreter-Pflicht nach Art. 13 DSA ist Voraussetzung für Zustellung; ohne Vertreter komplexes Auslandsverfahren.

## Typische Fehler

- DSA-Beschwerdepflicht nach Art. 20 DSA wird nicht ausgeschoepft, bevor Klage erhoben wird; Zulassigkeitsproblem.
- VLOP-Meldepflicht nach Art. 24 Abs. 3 DSA wird vergessen; Bussgeldrisiko.
- DMA-Gatekeeper-Designation wird mit kartellrechtlicher Marktbeherrschung gleichgesetzt; verschiedene Rechtsfragen.
- Nichtigkeitsklage nach Art. 263 AEUV wird verspaetet eingereicht; Zweimonatsfrist ab Designierungsbeschluss.
- Schnittstelle zu P2B-VO wird nicht geprueft, obwohl gewerbliche Nutzer betroffen sind.

## Quellen und Aktualitaet

- Stand: 05/2026
- DSA (EU) 2022/2065 in der geltenden Fassung
- DMA (EU) 2022/1925 in der geltenden Fassung
- P2B-VO (EU) 2019/1150 in der geltenden Fassung
- DDG in der geltenden Fassung
