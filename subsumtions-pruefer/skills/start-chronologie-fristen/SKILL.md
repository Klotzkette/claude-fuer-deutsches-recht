---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Subsumtions Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage im Subsumtions Pruefer."
---

# Subsumtions-Pruefer — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Subsumtions Pruefer**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Interaktiver Subsumtions-für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung.

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
| `beweisbedarf-und-belege-erfassen` | Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich… |
| `darlegungs-und-beweislast-verteilen` | Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss… |
| `de-eu-recht-abgrenzung` | Klaert die Abgrenzung zwischen nationalem deutschen Recht und Unionsrecht: wann gilt AEUV/EUV/GRCh/Verordnung/Richtlinie unmittelbar, wann richtlinienkonforme Auslegung, wann Vorabentscheidungsersuchen Art. 267 AEUV… |
| `einschlaegige-normen-vorschlagen-de` | Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Prüfungsreihenfolge und Hinweise auf Spezialitaet und… |
| `einschlaegige-normen-vorschlagen-eu` | Schlaegt einschlaegige Normen des Unionsrechts vor: AEUV, EUV, GRCh (Primaerrecht) sowie EU-Verordnungen und Richtlinien (Sekundaerrecht). Gibt Hinweise auf EuGH-Judikatur und Fundstellen bei curia.europa.eu. Klaert… |
| `eu-vorabentscheidung-pruefen` | Prüft die Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV: Vorlagebefugnis und -pflicht, CILFIT-Ausnahmen (acte clair/eclaire), Consorzio-Erweiterung, Vorlagepflicht letzter Instanz, Formulierung der… |
| `falsche-wiese-warnung` | Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen… |
| `gegen-tbm-und-einreden-pruefen` | Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte… |
| `generalklauseln-pruefen` | Prüft Generalklauseln wie Treu und Glauben (§ 242 BGB), gute Sitten (§ 138 BGB), billiges Ermessen, öffentliches Interesse und Verhältnismäßigkeit. Gibt Indizien und Fallgruppen statt mechanischer Subsumtion. Warnt vor… |
| `grundrechte-pruefung-de-und-grch` | Prüft Grundrechte nach GG (Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung) und GRCh (Art. 51/52 GRCh). Unterscheidet Abwehr-, Leistungs- und Schutzpflichtdimension. Verhältnismäßigkeitsprüfung mit Zweck,… |
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
| `konkurrenzen-anspruchsgrundlagen` | Klaert Konkurrenzfragen zwischen Anspruchsgrundlagen: Anspruchskonkurrenz, Anspruchsgrundlagenkonkurrenz, Spezialitaet, Subsidiaritaet, lex specialis/posterior/superior. Klaert Verhältnis von Vertrags- zu Deliktsrecht,… |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Erkennt Indikatoren für Komplexitaetsgrenzen des mechanischen Prüfens und empfiehlt Abbruch sowie Weiterleitung an Fachanwalt, Notar, Steuerberater oder Behörde. Warnt bei Strafrecht, Verfassungsrecht, internationalem… |
| `norm-historie-und-aenderungen` | Prüft die Norm-Historie: geltende Fassung zum massgeblichen Zeitpunkt, Übergangsvorschriften, intertemporales Recht, aenderungsrelevante Gesetzgebungsverfahren. Warnt bei Normen, die seit dem Wissensstand des Systems… |
| `norm-zerlegen-in-tatbestandsmerkmale` | Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion… |
| `output-alltagssprache-de` | Gibt das Subsumtionsergebnis in verstaendlicher Alltagssprache aus: ohne Fachbegriffe oder mit Erklärung, für Mandanten, Betroffene oder Behördenmitarbeiter. Behaelt die Strukturierung bei, vermeidet aber Lateinismen… |
| `output-antrag-beschwerde-klageschrift` | Erzeugt Tenor-Bausteine, Rubrum und formale Mindestanforderungen für Antrag, Beschwerde und Klageschrift nach ZPO, VwGO, SGG, FGO und BVerfGG. Gibt Pflichtangaben, Fristen und Einreichungshinweise. Kein anwaltlicher… |
| `output-fremdsprachig-en-fr` | Gibt das Subsumtionsergebnis auf Englisch oder Franzoesisch aus. Enthaelt obligatorischen Hinweis auf nicht-amtliche Übersetzung und Abweichung von deutschen Originalnormen. Nuetzlich für internationale Mandanten,… |
| `output-juristisch-gestochen-de` | Erzeugt Ausgaben im juristischen Schriftsatzstil auf Deutsch: Antrag-Begründung-Beweismittel-Struktur, Subsumtionsdarstellung im Vier-Schritt, Zitierweise nach BGH-Standard, Rubrum, Tenor. Für Schriftsaetze,… |
| `output-memo-und-mandantenbrief` | Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo für interne Nutzung mit juristischer Tiefe; Mandantenbrief für Betroffene in verstaendlicher… |
| `output-pruefungsdokument-mit-warnhinweisen` | Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und… |
| `rechtsfolge-bestimmen` | Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Hoehe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprüche. Gibt… |
| `rechtsprechung-recherche-strategie` | Gibt eine Strategie für die Rechtsprechungsrecherche: wann systeminternes Wissen genuegt, wann Web-Suche bei BVerfG/BGH/BAG/BSG/BVerwG/OLG/EuGH noetig ist. Nennt Fundstellen: curia.europa.eu, dejure.org, openjur,… |
| `subsumtion-obersatz-definition-untersatz-ergebnis` | Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt… |
| `triage-rechtsfrage-oder-norm` | Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill… |
| `unbestimmte-rechtsbegriffe-pruefen` | Prüft unbestimmte Rechtsbegriffe: wesentlich, erheblich, zumutbar, geeignet, angemessen, erforderlich. Gibt Auslegungsmassstaeibe aus Rechtsprechung und h.M., Indizien und Fallgruppen. Warnt vor der Grenze mechanischer… |
| `ungeschriebene-merkmale-judikatur` | Identifiziert judicativ entwickelte ungeschriebene Tatbestandsmerkmale: Verkehrspflichten, teleologische Reduktion und Extension, richterrechtliche Fortbildung, Analogie. Warnt vor Grenzen der mechanischen Prüfung bei… |
| `verfahrensart-bestimmen` | Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und… |
| `verjaehrung-fristen-pruefen` | Prüft Verjährungsfristen: Regelfrist 3 Jahre (§§ 195/199 BGB), kenntnisabhaengige Fristen, absolute 10- und 30-Jahresfristen, Hemmung (§§ 203 ff. BGB), Neubeginn (§ 212 BGB), prozessuale Notfristen und… |
| `ziel-und-rechtsweg-bestimmung` | Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG.… |

## Worum geht es?

Dieses Plugin fuehrt Juristen, Referendare und rechtlich Interessierte durch den klassischen juristischen Pruefungsaufbau: Tatbestandsmerkmale werden systematisch zerlegt, jede Norm wird im Vier-Schritt (Obersatz — Definition — Untersatz — Ergebnis) durchlaufen, Einreden und Rechtsfolgen werden getrennt erarbeitet. Das Plugin deckt deutsches Recht (BGB, HGB, StGB, ZPO, VwGO, GG und zahlreiche Nebengesetze) sowie Europarecht (AEUV, EUV, GRCh, EU-Verordnungen, Richtlinien) ab.

Der Schwerpunkt liegt auf mechanisch nachvollziehbarer Subsumtion — nicht auf freier Rechtsberatung. Alle Ausgaben enthalten einen Pflicht-Disclaimer, der auf die Grenzen automatisierter Pruefung hinweist.

## Wann brauchen Sie diese Skill?

- Sie haben einen konkreten Lebenssachverhalt und wollen wissen, welche Normen einschlaegig sein koennten.
- Sie wollen eine Norm systematisch in ihre Tatbestandsmerkmale zerlegen und Schritt für Schritt subsumieren.
- Sie muessen Beweislast, Einreden oder Verjährung pruefen und suchen eine strukturierte Abarbeitungshilfe.
- Sie benoetigen eine Ausgabe für einen Schriftsatz, ein Memo oder einen Mandantenbrief in verschiedenen Sprachstilen.
- Sie wollen eine Rechtsfrage mit EU-Bezug klaeren und pruefen, ob ein Vorabentscheidungsersuchen in Betracht kommt.

## Fachbegriffe (kurz erklaert)

- **Tatbestandsmerkmal (TBM)** — Einzelnes Element einer Rechtsnorm, das vorliegen muss, damit die Rechtsfolge eintritt.
- **Subsumtion** — Der gedankliche Vorgang, bei dem der Sachverhalt unter die Definition des TBM eingeordnet wird.
- **Obersatz** — Erster Schritt der Vier-Schritt-Subsumtion; nennt die Norm und die daran geknuepfte Rechtsfolge.
- **Anspruchskonkurrenz** — Mehrere Normen begruenden nebeneinander denselben Anspruch; jede wird selbstaendig geprueft.
- **Sekundaere Darlegungslast** — Erleichterung der Beweislast der beweispflichtigen Partei, wenn die andere Partei Tatsachen aus ihrem Bereich klaeren koennte.
- **Anwendungsvorrang** — Europarecht geht im Kollisionsfall nationalem Recht vor; nationales Recht wird verdraengt, nicht nichtig.
- **Vorabentscheidungsverfahren** — Verfahren nach Art. 267 AEUV: nationale Gerichte legen dem EuGH Auslegungsfragen des Unionsrechts vor.

## Rechtsgrundlagen

- §§ 195 ff. BGB — Verjährung
- §§ 241 ff. BGB — Schuldrecht (Pflichten, Stoerungen)
- §§ 355 ff. ZPO — Beweisrecht
- Art. 267 AEUV — Vorabentscheidungsverfahren EuGH
- Art. 51 ff. GRCh — Anwendungsbereich und Schranken der Grundrechtecharta
- § 138 BGB — Sittenwidrigkeit (Generalklausel)
- § 242 BGB — Treu und Glauben (Generalklausel)
- Art. 103 Abs. 2 GG — Analogieverbot im Strafrecht

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Handelt es sich um eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung?
2. Phase des Mandats bestimmen: Normensuche, Tatbestandsanalyse, Subsumtion, Rechtsfolge oder Output-Erstellung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Verjährungsfristen (§ 195 BGB), prozessuale Notfristen.
5. Anschluss-Skill bestimmen: nach Subsumtion typischerweise Rechtsfolge bestimmen und dann Output-Skill auswaehlen.

## Skill-Tour (was gibt es hier?)

**Einstieg und Triage**

- `triage-rechtsfrage-oder-norm` — Interaktiver Einstieg; erfasst ob ein Sachverhalt, eine Rechtsfrage oder eine Norm vorliegt und leitet weiter.
- `ziel-und-rechtsweg-bestimmung` — Ermittelt Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag) und leitet den einschlaegigen Rechtsweg ab.
- `verfahrensart-bestimmen` — Bestimmt die passende Verfahrensart: ZPO, einstweilig, Mahnverfahren, VwGO, StPO und andere.

**Normensuche**

- `einschlaegige-normen-vorschlagen-de` — Schlaegt einschlaegige Normen des deutschen Rechts zu einem Lebenssachverhalt vor.
- `einschlaegige-normen-vorschlagen-eu` — Schlaegt einschlaegige Normen des Unionsrechts vor mit EuGH-Judikatur und curia-Fundstellen.
- `de-eu-recht-abgrenzung` — Klaert wann nationales Recht und wann Unionsrecht unmittelbar gilt oder richtlinienkonforme Auslegung greift.
- `eu-vorabentscheidung-pruefen` — Prueft Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV.
- `norm-historie-und-aenderungen` — Prueft Norm-Geltungsfassung, Uebergangsvorschriften und intertemporales Recht.

**Tatbestandsanalyse**

- `norm-zerlegen-in-tatbestandsmerkmale` — Zerlegt eine Norm systematisch in TBM mit Definitionen und Pruefungsreihenfolge.
- `unbestimmte-rechtsbegriffe-pruefen` — Prueft unbestimmte Rechtsbegriffe mit Auslegungsmasssstaeben und Fallgruppen aus Rechtsprechung.
- `ungeschriebene-merkmale-judikatur` — Identifiziert judicativ entwickelte ungeschriebene TBM, Verkehrspflichten und teleologische Reduktion.
- `generalklauseln-pruefen` — Prueft Generalklauseln (§ 242 BGB, § 138 BGB) mit Indizien und Fallgruppen.
- `grundrechte-pruefung-de-und-grch` — Prueft Grundrechte nach GG und GRCh im Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung.
- `falsche-wiese-warnung` — Warnt vor typischen Falschverortungen (Vertrag statt Delikt, Verwaltungsakt vs. Realakt usw.).

**Subsumtion**

- `subsumtion-obersatz-definition-untersatz-ergebnis` — Fuehrt den klassischen Vier-Schritt je TBM durch.
- `beweisbedarf-und-belege-erfassen` — Erfasst pro TBM den Beweisbedarf mit Beweismittel-Katalog und Belegen.
- `darlegungs-und-beweislast-verteilen` — Verteilt Darlegungs- und Beweislast nach Grundregel, Beweislastumkehr und Anscheinsbeweis.
- `verjaehrung-fristen-pruefen` — Prueft Verjährungsfristen inklusive Hemmung, Neubeginn und EU-Verjährungsregeln.

**Gegenrechte und Rechtsfolgen**

- `gegen-tbm-und-einreden-pruefen` — Prueft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden.
- `konkurrenzen-anspruchsgrundlagen` — Klaert Anspruchskonkurrenz, Spezialitaet, Subsidiaritaet und Verhaeltnis Vertrags- zu Deliktsrecht.
- `rechtsfolge-bestimmen` — Bestimmt Anspruchsinhalt, Hoehe, Tenor und Nebenforderungen nach erfolgreicher Subsumtion.

**Output und Recherche**

- `output-juristisch-gestochen-de` — Ausgabe im juristischen Schriftsatzstil mit BGH-konformer Zitierweise.
- `output-memo-und-mandantenbrief` — Erstellt Aktennotiz oder Mandantenbrief mit Pflicht-Haftungshinweis.
- `output-alltagssprache-de` — Gibt Subsumtionsergebnis in verstaendlicher Alltagssprache ohne Fachbegriffe aus.
- `output-antrag-beschwerde-klageschrift` — Erzeugt Tenor-Bausteine und Pflichtangaben für Klageschriften und Beschwerden.
- `output-fremdsprachig-en-fr` — Ausgabe auf Englisch oder Franzoesisch mit Hinweis auf nicht-amtliche Uebersetzung.
- `output-pruefungsdokument-mit-warnhinweisen` — Vollstaendiges Pruefungsdokument mit Pflicht-Kopfhinweis und Disclaimern.
- `rechtsprechung-recherche-strategie` — Strategie für die Rechtsprechungsrecherche mit Fundstellen-Hinweisen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Eskalation**

- `mandatsabbruch-empfehlung-an-fachanwalt` — Erkennt Komplexitaetsgrenzen und empfiehlt Weiterleitung an Fachanwalt, Notar oder Behörde.

## Worauf besonders achten

- **Disclaimer ist Pflicht.** Alle Ausgaben enthalten den Hinweis, dass es sich um mechanische Pruefung handelt, kein Rechtsgutachten und kein Rechtsrat.
- **Normen koennen veraendert sein.** Immer Skill `norm-historie-und-aenderungen` konsultieren, wenn der Geltungszeitpunkt unklar ist.
- **Generalklauseln und unbestimmte Rechtsbegriffe sind fehleranfaellig.** Automatisierte Subsumtion bei § 242 BGB und aehnlichen Normen immer mit Vorbehalt behandeln.
- **Anspruchskonkurrenz nicht vergessen.** Mehrere Anspruchsgrundlagen koennen nebeneinander greifen; jede separat pruefen.
- **Vorabentscheidungspflicht letzter Instanz.** Bei EU-Rechtsfragen vor dem BGH oder BVerwG besteht ggf. Vorlagepflicht; Skill `eu-vorabentscheidung-pruefen` einschalten.

## Typische Fehler

- Sachverhalt wird direkt unter Normen subsumiert ohne vorherige Zerlegung in TBM; fuehrt zu Subsumtionsspruengen.
- Einreden und Einwendungen werden vergessen; geprueft wird nur die anspruchsbegruendende Seite.
- Verjährung wird als gegeben angenommen ohne Pruefung von Hemmungstatbestaenden (§§ 203 ff. BGB).
- Deutsches Recht wird angewendet obwohl Unionsrecht Anwendungsvorrang hat; Skill `de-eu-recht-abgrenzung` hilft.
- Output wird ohne Pflicht-Disclaimer weitergegeben; das koennte als Rechtsberatung missverstanden werden.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (BGB, HGB, StGB, ZPO, VwGO, GG, AEUV, GRCh)
- Rechtsprechungsdatenbanken: bundesgerichtshof.de, bundesverfassungsgericht.de, curia.europa.eu, dejure.org

