---
name: start-chronologie-fristen
description: "Start Chronologie Fristen im Sportrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Chronologie und Belegmatrix im Plugin fachanwalt-sportrecht, Fristen- und Risikoampel im Plugin fachanwalt-sportrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Start Chronologie Fristen

## Arbeitsbereich

**Start Chronologie Fristen** ordnet den Fall über die tragenden Prüfungslinien: Einstieg, Schnelltriage und Fallrouting im Fachanwalt, Chronologie und Belegmatrix im Plugin fachanwalt-sportrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Sportrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-sportrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-sportrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: WADC Art. 17 Verfolgungsverjährung 10 Jahre, CAS-Anrufung 21 Tage, DFB-RVO 7-Tage-Berufung, FAO § 5 36 Monate Praxiszeit.
- Tragende Normen verifizieren: FAO § 14n (Sportrecht), AntiDopG, NADC, WADC, BGB §§ 25 ff. (Verein), 705 ff., DFB-Satzung/Rechts- und Verfahrensordnung, FIFA-Statuten, CAS-Code, ArbGG (Spielerverträge) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Verein, Spieler, Verband (DFB/DFL/DOSB), Bundessportgericht, CAS (Lausanne), NADA, ArbG/LAG, Schiedsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Spielervertrag, Lizenzantrag, Sportgerichtsentscheidung, Schiedsspruch CAS, Anti-Doping-Protokoll, Verbandsstatut, Transferanmeldung TMS — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Sportrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

# Fachanwalt Sportrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Sportrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Sportrecht. Verbandsrecht (DFB FIFA UEFA IOC DOSB) CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Veranstalterhaftung. Schnittstelle Plugin gesellschaftsrecht.

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
| `cas-berufung-vorbereiten` | Sportler oder Verein will Entscheidung eines Sportverbands vor dem Court of Arbitration for Sport Lausanne anfechten. Art. R49 CAS Code Frist 21 Tage Sprache Englisch. Normen CAS Code Art. R49 R52 R57 WADA-Code Art. 13… |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Sport- und Sponsoringrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren` | Sportler Verein oder Verband wird in Schiedsverfahren vor CAS DIS oder Verbands-Schiedsgericht involviert. WADA-Code Anti-Doping FIFA Players Status Committee. Normen CAS Code Art. R27 ff.… |
| `fachanwalt-sportrecht-doping-cas-berufung` | Athlet muss Doping-Sperre vor CAS anfechten oder WADA/NADA legt Berufung gegen Freispruch ein. WADA-Code strict liability Therapeutic Use Exemption Sanktion 2-4 Jahre. Normen WADA-Code Art. 2 10 13 CAS Code AntiDopG §… |
| `fachanwalt-sportrecht-doping-verfahren` | Athlet steht vor NADA-Disziplinarverfahren wegen positivem Dopingtest und braucht Verteidigung. NADA-Code WADA-Code strict liability Art. 2 Abs. 1 WADA-Code Beweislastumkehr no fault Art. 10 Abs. 5. Normen AntiDopG § 4… |
| `fachanwalt-sportrecht-esports-vereinsrecht-dosb-anerkennung` | eSports-Organisator oder Verein fragt ob DOSB-Anerkennung möglich und wie steuerliche Gemeinnuetzigkeit erreichbar ist. § 52 AO Gemeinnuetzigkeit § 21 BGB Vereinsrecht. Normen §§ 21 ff. BGB § 52 AO DOSB-Satzung.… |
| `fachanwalt-sportrecht-orientierung` | Anwalt will Fachanwaltschaft Sportrecht erwerben oder Mandat im Sportrecht bearbeiten und braucht Orientierung. FAO-Voraussetzungen typische Mandate Fristen. Normen BGB §§ 21 ff. Vereinsrecht CAS Code WADA-Code… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `fachanwalt-sportrecht-stadion-hausverbot` | Fan erhaelt bundesweites Stadion-Hausverbot und will dieses anfechten. AGB-Prüfung Vereinsrecht Fanrechte Datenschutz. Normen §§ 305 ff. BGB AGB-Kontrolle BGH Bundesliga-Hausverbot § 25 BGB Vereinsrecht DSGVO… |
| `fachanwalt-sportrecht-transferklausel` | Profi-Sportler will Verein wechseln und braucht Prüfung von Transfervertrag Ausstiegsklausel Transferperiode. FIFA/UEFA-Statuten Wechselgebühr. Normen FIFA RSTP Art. 17 18 UEFA-Transferregeln DFB-Lizenzordnung.… |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `mandat-triage-sportrecht` | Sportrechtliches Mandat eintrifft und muss strukturiert erfasst werden: Mandantenrolle Sachgebiet Sofort-Fristen. Verbandsfrist gegen Sanktion typisch 1-2 Wochen. Normen je nach Routing. Prüfraster Mandanten-Typ… |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage ordentliches Gericht/Sportgericht, CAS-/DIS-Schiedsantrag, Antidoping: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge,… |
| `verbandsstrafe-anfechten` | Prüfraster für die Anfechtung von Verbandsstrafen im Sport. Spannungsfeld Verbandsautonomie Art. 9 GG vs. gerichtliche Inhaltskontrolle vereinsrechtlich § 25 BGB Schiedsklauseln § 1029 ZPO CAS-Schiedsgerichtsbarkeit… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Sport- und Sponsoringrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-sportrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

# Chronologie und Belegmatrix

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin fachanwalt-sportrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

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

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin fachanwalt-sportrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

# Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin fachanwalt-sportrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Schlüsselfristen Sportrecht
- Verbandsrechtliche Berufungsfristen: typischerweise sieben bis 14 Tage ab Bescheid; abhängig von Verbandsstatuten (DFB, DOSB, FIFA, IOC).
- Anti-Doping Whereabouts-Pflichten nach NADA-Code; Result Management-Fristen.
- Berufung CAS Lausanne: 21 Tage ab Bescheid (Art. R49 CAS-Code); deutscher Sportler kann ergänzend Schiedsklage nach § 1059 ZPO erheben.
- Spielerstatus FIFA: Transferfenster, RSTP; Berufung CAS gegen FIFA-Disziplinarentscheidungen.
- DSGVO bei Athletendaten: 30 Tage Auskunftsfrist Art. 12 Abs. 3 DSGVO.

## Trade-off
- Verbandsgerichtsbarkeit (schnell, fachkundig) vs. staatliche Gerichte (BGH Pechstein-Entscheidung anerkennt grds. Verbandsschiedsgerichtsbarkeit mit Kartellrechtskorrektiv): einseitige Wahl-Klauseln können kartellrechtlich unwirksam sein.
- WADC-Suspendierung: einstweilige Suspendierung ist möglich; B-Probe-Beantragung binnen kurzer Frist ab A-Probe-Mitteilung.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.
