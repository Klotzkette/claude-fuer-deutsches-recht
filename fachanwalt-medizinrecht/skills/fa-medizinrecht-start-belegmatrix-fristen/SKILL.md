---
name: fa-medizinrecht-start-belegmatrix-fristen
description: "FA Medizinrecht Start Belegmatrix Fristen im Medizinrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin fachanwalt-medizinrecht."
---

# FA Medizinrecht Start Belegmatrix Fristen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Medizinrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Medizinrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Medizinrecht. Arzthaftung §§ 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Aerzte SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen Plugin fachanwalt-sozialrecht kanzlei-allgemein.

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
| `aufklaerungsfehler-beweisstrategie` | Strukturierte Beweisstrategie bei Aufklärungsfehlern § 630e BGB. Beweislast für ordnungsgemäße Aufklärung beim Arzt § 630h Abs. 2 BGB. Inhalts-Anforderungen Risiken Folgen Alternativen Diagnose Prognose wirtschaftliche… |
| `behandlungsfehler-anspruch-pruefen` | Strukturierte Prüfung von Ansprüchen wegen Behandlungsfehler nach §§ 630a ff. BGB iVm § 823 BGB. Behandlungsvertrag Aufklärungspflicht § 630e BGB Dokumentationspflicht § 630f BGB Beweislastregeln § 630h BGB grober… |
| `erstgespraech-mandatsannahme` | Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit. §… |
| `fachanwalt-medizinrecht-approbations-widerspruch` | Approbationswiderruf und Berufsrecht für Aerzte Apotheker Zahnaerzte: Anwendungsfall Heilberufler erhaelt Widerrufs-Bescheid oder Ruhens-Anordnung der Approbationsbehoerde. § 5 BAerztO Widerruf Unwürdigkeit… |
| `fachanwalt-medizinrecht-aufklaerungsfehler` | Aufklärungspflicht §§ 630e 630h BGB Selbstbestimmungs- und Risikoaufklärung. Form muendlich persoenlich rechtzeitig vor Eingriff. Inhalt Diagnose Verlauf Alternativen Risiken Nachteile. Beweislast § 630h Abs. 2 BGB… |
| `fachanwalt-medizinrecht-behandlungsfehler-pruefen` | Behandlungsfehler §§ 630a 630h BGB Verletzung medizinischer Standard. Diagnosefehler Therapiefehler Befunderhebungsfehler Hygienefehler. Beweisregeln § 630h BGB Vermutung Kausalität bei grobem Behandlungsfehler § 630h… |
| `fachanwalt-medizinrecht-behandlungsvertrag-630a` | Behandlungsvertrag nach §§ 630a-h BGB und Patientenrechte prüfen: Anwendungsfall Patient behauptet Behandlungsfehler oder Aufklärungsmangel oder Arzt braucht Vertragsdokumentation. §§ 630a-h BGB Behandlungsvertrag, §… |
| `fachanwalt-medizinrecht-gutachterkommission-aek-schlichtung` | Gutachterkommissionen und Schlichtungsstellen der Aerztekammern bei Arzthaftung nutzen: Anwendungsfall Patient oder Anwalt erwägt Schlichttungsverfahren vor Aerztekammer als kostenguenstige Alternative zur Klage. §… |
| `fachanwalt-medizinrecht-honorarvertrag-kv` | Honorarstreitigkeiten mit Kassenärztlicher Vereinigung begleiten: Anwendungsfall Vertragsarzt erhaelt Honorar-Bescheid mit Kuestzungen oder Wirtschaftlichkeits- oder Plausibilitaetsprüfung laeuft. EBM Einheitlicher… |
| `fachanwalt-medizinrecht-kassenarztrecht` | Kassenarztrecht Vertragsarztzulassung und KV-Streitigkeiten: Anwendungsfall Arzt beantragt Vertragsarztzulassung hat Zulassungsprobleme oder streitet mit KV um Honorar Berechtigung oder Zulassungsstatus. § 95 SGB V… |
| `fachanwalt-medizinrecht-off-label-use-erstattung-gkv-long-covid` | Off-Label-Use und GKV-Erstattungsstreitigkeiten insbesondere Long-Covid: Anwendungsfall Patient benoetigt nicht zugelassenes Medikament oder Therapie und GKV verweigert Erstattung. § 12 SGB V Wirtschaftlichkeitsgebot,… |
| `fachanwalt-medizinrecht-orientierung` | Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Arzthaftung §§ 630a ff. BGB (Patientenrechtegesetz seit 2013) Vertragsarztrecht SGB V Berufsrecht Aerzte… |
| `mandat-triage-medizinrecht` | Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate. Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklärungspflicht-Verletzung Honorarstreit… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Arzthaftungsklage und KV-Streit: Anwendungsfall Medizinrechts-Anwalt muss vollwertigen Schriftsatz in Arzthaftungssache Sozialgericht oder Berufsrechtsbeschwerde verfassen. § 630a… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlung und Einigungsstrategie im Medizinrecht: Anwendungsfall Arzthaftungssache KV-Streit oder Berufsrechtsbeschwerde eignet sich für außergerichtliche Einigung. § 630a BGB Behandlungsvertrag, § 253 BGB… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-medizinrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

### Chronologie und Belegmatrix

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-medizinrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

### Fristen- und Risikoampel

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Typische Fristen Medizinrecht
- Verjährung Arzthaftungsansprüche: drei Jahre kenntnisabhängig (§§ 195, 199 BGB); 30-Jahres-Höchstgrenze ab Behandlung bei Personenschäden.
- Dokumentationspflichten § 630f BGB Aufbewahrungsdauer zehn Jahre.
- Patientenrechtegesetz: Einsichtsrecht in Patientenakte § 630g BGB binnen angemessener Frist.
- Schlichtungsverfahren ÄK: hemmt Verjährung nach § 204 Abs. 1 Nr. 4 BGB ab Antragsschriftsatz.
- Approbations-/Berufsgerichtsverfahren: Widerspruchsfrist ein Monat ab Bekanntgabe (§ 70 VwGO).
- Kassenarzt-Honorarbescheid: Widerspruch ein Monat, Klage SG; Honorarausschluss-Beschwerden Zulassungsgremien.
- Strafanzeige Patient → Strafverfolgung Körperverletzung: § 78 StGB Verfolgungsverjährung beachten.

## Trade-off
- Schlichtungsverfahren (kostengünstig, verzögert) vs. direkte Klage (zeitnah, kostspielig, Rufrisiko).
- Beweislastumkehr nach § 630h BGB nur bei groben Behandlungsfehlern, Befunderhebungsversäumnis, voll beherrschbaren Risiken — bei einfachen Fehlern Beweislast Patient.

## 4. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin fachanwalt-medizinrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## 5. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin fachanwalt-medizinrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

### Red-Team Qualitygate

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## 6. `spezial-arzthaftung-fristen-form-und-zuständigkeit`

**Fokus:** Arzthaftung: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt medizinrecht.

### Arzthaftung: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachkern: Arzthaftung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Arzthaftung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

