---
name: anschluss
description: "Anschluss im Datenschutzrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin, Anschluss-Skills Router im Plugin datenschutzrecht, Chronologie und Belegmatrix im Plugin datenschutzrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anschluss

## Arbeitsbereich

**Anschluss** ordnet den Fall über die tragenden Prüfungslinien: Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin, Anschluss-Skills Router im Plugin datenschutzrecht. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `datenschutzrecht-allgemein` | Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `datenschutzrecht-allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Fachmodule dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.

### Datenschutzrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Datenschutzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review als Verantwortlicher und Auftragsverarbeiter, Auskunftsersuchen Art. 15, Datenpannenmeldung Art. 33/34, Drittlandstransfer Art. 44 ff., US-Transfer mit DPF/SCC/TIA, Behördenpaket, Drift-Monitoring.

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
- **Primärer Pfad:** `passender-datenschutz-skill` — [warum dieser Arbeitsgang hilft]
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
| `anwendungsfall-triage` | Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter… |
| `avv-pruefung` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit… |
| `datenpanne-meldung` | Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung… |
| `datenschutzrecht-anpassen` | Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen… |
| `datenschutzrecht-kaltstart-interview` | Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschaeftigtendaten. Prüfraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger… |
| `datenschutzrecht-mandat-arbeitsbereich` | Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe externe Datenschutzberatung. Output:… |
| `drittlandstransfer-pruefung` | Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment… |
| `us-transfer-tia-dokumentation` | US-Drittlandtransfer mit EU-US Data Privacy Framework, DPF-Listing, Schrems-I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures und Review-Kalender dokumentieren. |
| `standardvertragsklauseln-scc-paket` | Standardvertragsklauseln vorbereiten: Modul 1-4 wählen, Annex I-III ausfüllen, Subprozessoren, TOMs, AVV-Schnittstelle, TIA-Andockung und Unterzeichnungspaket erstellen. |
| `drittlandtransfer-behoerdenpaket-output` | Aus Transferregister, DPF/SCC/TIA, TOMs und Subprozessoren ein druckreifes Paket samt Antwortentwurf für deutsche Datenschutzaufsichtsbehörden bauen. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung.… |
| `dsfa-erstellung` | Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit… |
| `dsgvo-auskunft` | Auskunftsersuchen nach Art. 15 DSGVO prüfen und beantworten wenn Betroffener Auskunft verlangt. Art. 15 12 DSGVO Betroffenenrechte. Prüfraster: Identitätsnachweis Vollständigkeitsprüfung Auskunftsinhalt Fristen… |
| `dsgvo-auskunft-antwort` | DSGVO-Auskunftsantwort an Betroffenen vollständig und rechtskonform gestalten. Art. 15 12 Abs. 3 DSGVO Antwortpflicht. Prüfraster: Antwortinhalt Format Fristen Klarheit Weglassungsgründe Begleitschreiben. Output:… |
| `joint-controller-vereinbarung` | Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen wenn zwei oder mehr Verantwortliche gemeinsam entscheiden. Art. 26 DSGVO Gemeinsame Verantwortlichkeit. Prüfraster: gemeinsame Zwecke und Mittel… |
| `ki-verordnung-compliance` | KI-Systeme auf Anforderungen der KI-VO und Datenschutz prüfen. KI-VO Risikoklassen Art. 5 9 DSGVO Einwilligung. Prüfraster: Risikoklasse Verbote Hochrisiko-KI Dokumentationspflichten DSGVO-Schnittmengen… |
| `mandantendaten-ki` | Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei prüfen. Art. 5 6 DSGVO BRAO § 43a Verschwiegenheit. Prüfraster: Rechtsgrundlage Zweckbindung Vertraulichkeit Anwaltsprivileg… |
| `regulierungs-luecken-analyse` | Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen. Art. 5 6 24 DSGVO BDSG. Prüfraster: Bestandsaufnahme bestehender Massnahmen Soll-Ist-Abgleich Lueckenbewertung Prioritaeten.… |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Aenderungsbedarf neue Verarbeitungstätigkeiten… |
| `verarbeitungsverzeichnis-vvt-generator` | Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen… |

## Worum geht es?

Dieses Plugin unterstuetzt Rechtsanwaelte und Datenschutzbeauftragte bei der Bearbeitung datenschutzrechtlicher Mandate nach DSGVO und BDSG. Es deckt den vollstaendigen ab: von der ersten Triage ueber Auftragsverarbeitungsvertraege, Datenschutz-Folgenabschaetzungen und Auskunftsersuchen bis zu Datenpannenmeldungen, Drittlandstransfers, US-Transfer-Dokumentation und der laufenden Richtlinienpflege.

Der Anwendungsbereich umfasst Unternehmen als Verantwortliche (Art. 4 Nr. 7 DSGVO), Auftragsverarbeiter (Art. 4 Nr. 8 DSGVO) und gemeinsam Verantwortliche (Art. 26 DSGVO), sowie den Einsatz von KI-Tools im Kanzleialltag.

## Wann brauchen Sie diese Skill?

- Ein Unternehmen erhaelt ein Auskunftsersuchen nach Art. 15 DSGVO und braucht eine rechtskonforme Antwort.
- Ein Datenschutzbeauftragter muss eine Datenpanne nach Art. 33 DSGVO binnen 72 Stunden an die Aufsichtsbehoerde melden.
- Eine Kanzlei prueft, ob ein IT-Dienstleister einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO benoetigt.
- Ein Unternehmen will Daten in ein Drittland (USA, Indien) uebertragen und braucht einen Transfer-Impact-Assessment.
- Eine Aufsichtsbehoerde fragt nach US-Transfer, DPF-Listing, SCC, TIA und Schrems-II-Dokumentation.
- Eine Behörde oder Kanzlei prueft, ob KI-Werkzeuge datenschutzkonform eingesetzt werden koennen.

## Fachbegriffe (kurz erklaert)

- **DSGVO** — Datenschutz-Grundverordnung (EU 2016/679); einheitliches EU-Datenschutzrecht für Verarbeitung personenbezogener Daten.
- **BDSG** — Bundesdatenschutzgesetz; ergaenzt die DSGVO im deutschen Recht, insbesondere für Beschaeftigtendatenschutz (§ 26 BDSG).
- **TDDDG** — Telekommunikation-Digitale-Dienste-Datenschutzgesetz; Nachfolger des TTDSG, regelt Cookies und Online-Tracking.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; Pflichtvertrag, wenn ein Dritter Daten im Auftrag verarbeitet.
- **DSFA** — Datenschutz-Folgenabschaetzung (Data Protection Impact Assessment, DPIA) nach Art. 35 DSGVO; Pflicht bei hohem Risiko.
- **Drittland** — Staat ausserhalb des EWR, in den Datentransfers nur unter bestimmten Voraussetzungen zulaessig sind (Art. 44 ff. DSGVO).
- **VVT** — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO; Dokumentationspflicht für Verantwortliche und Auftragsverarbeiter.
- **DSB** — Datenschutzbeauftragter; Pflichtposition nach Art. 37 DSGVO und § 38 BDSG ab bestimmten Schwellenwerten.

## Rechtsgrundlagen

- Art. 5 DSGVO (Grundsaetze der Verarbeitung)
- Art. 6 DSGVO (Rechtmaessigkeit der Verarbeitung)
- Art. 12-23 DSGVO (Betroffenenrechte)
- Art. 26 DSGVO (Joint Controller)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 30 DSGVO (Verzeichnis der Verarbeitungstaetigkeiten)
- Art. 33-34 DSGVO (Meldepflicht bei Datenpannen)
- Art. 35-36 DSGVO (Datenschutz-Folgenabschaetzung)
- Art. 37-39 DSGVO (Datenschutzbeauftragter)
- Art. 44-49 DSGVO (Drittlandstransfer)
- § 26 BDSG (Beschaeftigtendatenschutz)
- § 38 BDSG (Pflicht zur Bestellung eines DSB)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Verantwortlicher, Auftragsverarbeiter oder gemeinsam Verantwortlicher?
2. Sachverhalt einordnen und Bearbeitungsroute bestimmen (Skill `anwendungsfall-triage`).
3. Mandat strukturieren und Arbeitsbereich abgrenzen (`datenschutzrecht-kaltstart-interview` oder `datenschutzrecht-mandat-arbeitsbereich`).
4. Passenden Fachskill auswaehlen (z. B. AVV, DSFA, Drittlandstransfer, Datenpanne).
5. Eilfristen pruefen: Datenpannenmeldung 72-Stunden-Frist, Auskunftspflicht einen Monat ab Ersuchen.

## Skill-Tour (was gibt es hier?)

- `anwendungsfall-triage` — Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen.
- `datenschutzrecht-kaltstart-interview` — Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen.
- `datenschutzrecht-mandat-arbeitsbereich` — Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen.
- `datenschutzrecht-anpassen` — Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen anpassen.
- `avv-pruefung` — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO pruefen oder erstellen.
- `joint-controller-vereinbarung` — Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen, wenn zwei oder mehr Verantwortliche gemeinsam entscheiden.
- `dsfa-erstellung` — Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchfuehren bei hohem Risiko.
- `datenpanne-meldung` — Datenpanne nach Art. 33 und 34 DSGVO melden bei Sicherheitsverletzung personenbezogener Daten.
- `dsgvo-auskunft` — Auskunftsersuchen nach Art. 15 DSGVO pruefen und Bearbeitungsstrategie bestimmen.
- `dsgvo-auskunft-antwort` — DSGVO-Auskunftsantwort an Betroffenen vollstaendig und rechtskonform gestalten.
- `drittlandstransfer-pruefung` — Datentransfer in Drittlaender ausserhalb EU und EWR auf Zulaessigkeit pruefen.
- `us-transfer-tia-dokumentation` — US-Transfer mit DPF, SCC/BCR-Ausweichpfad, TIA und ergänzenden Maßnahmen dokumentieren.
- `standardvertragsklauseln-scc-paket` — SCC-Modulwahl, Annex I-III, Subprozessoren und TOMs behördenfest vorbereiten.
- `drittlandtransfer-behoerdenpaket-output` — Deckvermerk, Anlagenverzeichnis, Behördenantwort und Maßnahmenplan ausgeben.
- `dsb-bestellungspflicht-pruefung` — Bestellungspflicht für Datenschutzbeauftragten nach Art. 37 DSGVO und § 38 BDSG pruefen.
- `verarbeitungsverzeichnis-vvt-generator` — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren.
- `ki-verordnung-compliance` — KI-Systeme auf Anforderungen der KI-VO und Datenschutz gemeinsam pruefen.
- `mandantendaten-ki` — Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei pruefen.
- `regulierungs-luecken-analyse` — Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen.
- `richtlinien-monitor` — Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformitaet monitoren.

## Worauf besonders achten

- Datenpannenmeldung nach Art. 33 DSGVO hat eine 72-Stunden-Frist ab Kenntnisnahme — keine Verzoegerung durch interne Abstimmungsrunden.
- Drittlandstransfer ohne Rechtsgrundlage (Angemessenheitsbeschluss oder Standardvertragsklauseln) ist ein bussgeldrelevanter Verstoss.
- Auftragsverarbeitungsvertraege muessen vor Beginn der Verarbeitung vorliegen — nicht erst nach Vertragsschluss.
- § 26 BDSG-Beschaeftigtendatenschutz hat engere Grenzen als die DSGVO-Generalklausel — gesondert pruefen.
- Cookies und Tracking unterliegen zusaetzlich dem TDDDG — einwilligungspflichtige Dienste nicht mit Art. 6 Abs. 1 lit. f DSGVO rechtfertigen.

## Typische Fehler

- Auftragsverarbeitungsvertrag fehlt: Unternehmen gibt Daten an Cloud-Anbieter weiter ohne AVV nach Art. 28 DSGVO.
- DSFA-Pflicht verkannt: Hochrisiko-Verarbeitung (z. B. Profilbildung, Scoring) wird ohne Folgenabschaetzung gestartet.
- Auskunftsantwort unvollstaendig: Betroffener erhaelt keine Information ueber Empfaenger oder Speicherdauer.
- Drittlandstransfer nach Schrems II nicht geprueft: Alte Safe-Harbor- oder Privacy-Shield-Grundlage wird weiter verwendet.
- DSB-Bestellungspflicht nicht erkannt: Unternehmen beschaeftigt mehr als 20 Personen mit Datenverarbeitung, bestellt aber keinen DSB.

## Querverweise

- `ki-vo-ai-act-pruefer` — KI-Systeme im Datenschutzkontext; DSGVO und KI-VO ueberschneiden sich bei Hochrisiko-KI.
- `regulatorisches-recht` — Sektorzeitige Datenschutzanforderungen für Finanzunternehmen (MaRisk, DORA).
- `vertragsrecht` — AVV und Datenschutzklauseln in Lieferanten- und SaaS-Vertraegen.
- `einfache-leichte-sprache-jura` — DSGVO verlangt verstaendliche Einwilligungserklaerungen und Datenschutzhinweise.

## Quellen und Aktualitaet

- Stand: 05/2026
- DSGVO (EU 2016/679) in der zum Stand-Datum geltenden Fassung
- BDSG in der geltenden Fassung
- TDDDG in der geltenden Fassung
- Standardvertragsklauseln der EU-Kommission (2021/914)
- EU-US Data Privacy Framework-Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023 und offizielle DPF-Participant-Search.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-anschluss-skills-router`

**Fokus:** Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor.

### Anschluss-Skills Router

## Aufgabe
Dieses Modul bearbeitet: Anschluss-Skills Router im Plugin datenschutzrecht: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor..

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

## 3. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

### Chronologie und Belegmatrix

## Aufgabe
Dieses Modul bearbeitet: Chronologie und Belegmatrix im Plugin datenschutzrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen..

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

## 4. `workflow-fristen-und-risikoampel`

**Fokus:** Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen.

### Fristen- und Risikoampel

## Aufgabe
Dieses Modul bearbeitet: Fristen- und Risikoampel im Plugin datenschutzrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen..

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

## Datenschutz-typische Fristen
- **Art. 33 DSGVO** – Meldung Datenpanne an Aufsichtsbehörde: **72 Stunden** ab Kenntnis.
- **Art. 34 DSGVO** – Benachrichtigung Betroffener: **unverzüglich** bei hohem Risiko.
- **Art. 12 Abs. 3 DSGVO** – Antwort auf Betroffenenanfragen (Art. 15 ff.): **1 Monat**, ggf. Verlängerung um zwei Monate.
- **Art. 36 DSGVO** – Vorherige Konsultation Aufsichtsbehörde bei DSFA mit hohem Restrisiko, Antwort der Behörde **8 Wochen** (verlängerbar).
- **Bußgeldrahmen**: Art. 83 Abs. 5 DSGVO bis **20 Mio. EUR oder 4 %** weltweiter Jahresumsatz.

## Ampelkriterien
- **Rot**: 72-Std-Frist (Art. 33) läuft, Bußgeldbescheid zugestellt, behördliche Anordnung, Drittlandstransfer ohne Garantien Art. 44 ff.
- **Gelb**: DSFA fehlt für ein bekanntes Hochrisiko-Verfahren, AVV unvollständig, Verzeichnis Art. 30 nicht aktuell.
- **Grün**: Rechtsgrundlage Art. 6/9 dokumentiert, Verzeichnis Art. 30 aktuell, DSFA durchgeführt, AVV + TOM vorhanden.

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

## 5. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

### Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin datenschutzrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Mandantenkommunikation Datenschutz
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre datenschutzrechtliche Anfrage"
- **Sachstand kurz:** welche Daten, welche Rolle (Verantwortlich Art. 4 Nr. 7 / Auftragsverarbeiter Art. 4 Nr. 8), welche Rechtsgrundlage Art. 6/9 DSGVO einschlägig.
- **Empfehlung:** zentral umsetzbarer nächster Schritt (z. B. "DSFA durchführen, AVV nachverhandeln, Aufsichtsbehörde melden, Betroffene benachrichtigen").
- **Risikoampel** mit Bezug auf konkrete Bußgeldhöhe (Art. 83 Abs. 4: 10 Mio./2 %; Abs. 5: 20 Mio./4 %).
- **Frist:** insb. 72 Stunden (Art. 33), 1 Monat (Art. 12 Abs. 3), 13 Monate (Art. 17 Vergessen) konkret nennen.
- **Kostenhinweis:** RVG/Honorarvereinbarung.
- **Datenschutz-Hinweis intern:** keine Mandantendaten in unverschlüsselter E-Mail; bei Bedarf verschlüsselter Versand oder Datenraum.

## Praxis-Tipp
Bei Betroffenenanfragen die Mandantschaft frühzeitig über die Antwortpflicht aufklären — der häufigste Fehler ist Ablehnung "wir geben keine Daten heraus" ohne Rechtsgrundlage. Das löst regelmäßig Beschwerde bei der Aufsichtsbehörde und Bußgeldverfahren aus. Antwortverweigerung nur nach Art. 12 Abs. 5 (Missbrauch) oder § 34 BDSG (gesetzliche Ausnahme).

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

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.
