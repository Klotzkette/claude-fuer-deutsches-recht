---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage."
---

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Liquiditaetsplanung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau mit BGH-Passiva-II- und 10-Prozent-Schema, 13/26/52-Wochen-Forecast, Excel-Export mit Quote/Luecken-Ampel, Padlet/JSON-Round-Trip, Integration mit Fortbestehensprognose und Sanierungsplanung auf IDW-S-6-Niveau. Krisen-GmbH, Bugwellenrechtsprechung.

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
| `idw-s6-integrierte-sanierungsplanung` | Wenn aus einer Liquiditätsvorschau eine Sanierungsplanung werden soll: GuV, Planbilanz, Cashflow, Maßnahmenwirkung, Annahmenregister, Sensitivitäten und Sanierungsfähigkeits-Ampel. |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditätsvorschau über 13/26/52 Wochen für GmbH/UG/AG. Erstellt zwingend eine Excel-Tabelle nach der hinterlegten Vorlage und auf Wunsch ein interaktives HTML-Padlet oder Markdown-Artefakt, das mit jeder… |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Drei-Wochen-Liquiditätsvorschau nach § 17 InsO. Erstellt zwingend eine Excel-Tabelle auf Wochenbasis und auf Wunsch ein interaktives HTML-Padlet oder Markdown-Artefakt zur fortlaufenden Pflege. Wendet… |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfähige Liquiditätsbilanz und Liquiditätsvorschau für die Prüfung der Zahlungsunfähigkeit (§ 17 InsO) und die Fortbestehensprognose (§ 19 InsO). Standardergebnis ist eine Excel-Tabelle auf Wochenbasis; auf… |

## Worum geht es?

Das Plugin unterstuetzt Steuerberater, Rechtsanwaelte und Geschäftsführer bei der Erstellung und Prüfung von Liquiditaetsvorschauen nach deutschem Recht. Im Mittelpunkt stehen die kurzfristige Drei-Wochen-Vorschau nach § 17 InsO sowie rollierende Forecasts über 13, 26 und 52 Wochen. Das Plugin erzeugt Excel-Tabellen nach dem BGH-Passiva-II- und 10-Prozent-Schema und integriert eine Quote-Luecken-Ampel.

Zielgruppe sind Berater und Organe von GmbH, UG und AG in wirtschaftlichen Krisensituationen, insbesondere wenn Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit oder Ueberschuldung geprueft werden muss. Die Instrumente unterstuetzen auch die Fortbestehensprognose sowie die Bugwellenrechtsprechung des BGH.

## Wann brauchen Sie diese Skill?

- Geschäftsführer oder Steuerberater benoetigt eine gerichtsfaehige Liquiditaetsvorschau zur Insolvenzantragspflicht-Prüfung nach § 15a InsO.
- Der Mandant prüft, ob Zahlungsunfaehigkeit nach § 17 InsO oder drohende Zahlungsunfaehigkeit nach § 18 InsO vorliegt.
- Zur Vorbereitung eines StaRUG-Restrukturierungsverfahrens, Insolvenzplanverfahrens oder Sanierungskonzepts wird ein mehrstufiger Forecast mit GuV-/Bilanz-Brücke benoetigt.
- Im Rahmen einer M&A-Transaktion oder einer Distressed-Situation ist eine nachvollziehbare Liquiditaetsplanung erforderlich.
- Der Berater muss die Drei-Wochen-Deckungsluecke nach dem BGH-Passiva-II-Schema berechnen und dokumentieren.

## Fachbegriffe (kurz erklaert)

- **Zahlungsunfaehigkeit (§ 17 InsO)** — Schuldner kann faellige Zahlungspflichten nicht mehr erfuellen; BGH-Formel: Deckungsluecke über 10 Prozent der faelligen Verbindlichkeiten.
- **Drohende Zahlungsunfaehigkeit (§ 18 InsO)** — Schuldner wird voraussichtlich nicht in der Lage sein, bestehende Zahlungspflichten bei Faelligkeit zu erfuellen.
- **BGH-Passiva-II-Schema** — Gerichtlich anerkannte Methode zur Berechnung der Liquiditaetsluecke; unterscheidet zwischen faelligen und nicht faelligen Verbindlichkeiten.
- **10-Prozent-Schwelle** — Liegt die Liquiditaetsluecke dauerhaft bei mehr als 10 Prozent der faelligen Gesamtverbindlichkeiten, indiziert das Zahlungsunfaehigkeit.
- **Rollierende Vorschau** — Fortlaufend aktualisierte Liquiditaetsplanung über 13, 26 oder 52 Wochen (3, 6 oder 12 Monate).
- **Fortbestehensprognose** — Beurteilung, ob das Unternehmen mit ueberwiegender Wahrscheinlichkeit fortbestehen wird; relevant für Ueberschuldungspruefung nach § 19 InsO.
- **Sanierungsplanung** — Integrierte Verbindung aus Liquidität, GuV, Bilanz, Maßnahmen und Annahmen; zeigt, ob eine kurzfristig zahlungsfähige Gesellschaft auch nachhaltig sanierungsfähig wird.
- **Bugwellenrechtsprechung** — BGH-Rechtsprechung zur aufgeschobenen Faelligkeit von Verbindlichkeiten, die erst bei Vorliegen eines Insolvenzgrunds entfallen.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit
- § 18 InsO — Drohende Zahlungsunfaehigkeit
- § 19 InsO — Ueberschuldung
- § 15a InsO — Insolvenzantragspflicht
- §§ 64, 43 GmbHG a.F. bzw. § 15b InsO n.F. — Haftung bei Zahlungen nach Insolvenzreife
- §§ 238 ff. HGB — Buchfuehrungspflichten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Krisensituation des Mandanten klären: Liegt Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit oder Ueberschuldung vor oder wird sie geprueft?
2. Erforderlichen Zeitraum bestimmen: Drei-Wochen-Vorschau (kurzfristig/insolvenzrechtlich) oder rollierender 13/26/52-Wochen-Forecast.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfrist prüfen: Bei konkretem Verdacht auf Zahlungsunfaehigkeit laeuft die Drei-Wochen-Antragsfrist des § 15a InsO.
5. Anschluss-Skill bestimmen: Nach Erstellung der Vorschau ggf. Fortbestehensprognose oder StaRUG-Prüfung.

## Skill-Tour (was gibt es hier?)

- `idw-s6-integrierte-sanierungsplanung` — Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung mit Maßnahmen-Brücke und Annahmenlog.
- `liquiditaetsvorschau-3wochen` — Wochenaktuelle Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Excel-Tabelle und Deckungsluecken-Ampel.
- `liquiditaetsvorschau-3-6-12-monate` — Rollierende Liquiditaetsvorschau über 13/26/52 Wochen für GmbH/UG/AG als Excel-Export mit Quote-Luecken-Ampel.
- `liquiditaetsvorschau-insolvenzrechtlich` — Gerichtsfaehige Liquiditaetsbilanz und Vorschau zur Prüfung der Zahlungsunfaehigkeit nach § 17 InsO und der Ueberschuldung.

## Worauf besonders achten

- Die Drei-Wochen-Frist des § 15a InsO ist eine echte Maximalfrist; bei konkretem Anfangsverdacht auf Zahlungsunfaehigkeit beginnt sie zu laufen.
- Das BGH-Passiva-II-Schema erfordert saubere Trennung zwischen faelligen und nicht faelligen Verbindlichkeiten; Fehler hier fuehren zu falschen Ergebnissen.
- Excel-Exporte müssen reproduzierbar und nachvollziehbar sein, da sie im Insolvenzverfahren als Beweismittel vorgelegt werden können.
- Die 10-Prozent-Schwelle ist eine Indizwirkung, kein automatischer Ausloeser; die Gesamtumstaende sind zu wuerdigen.
- Keine Vermischung von Zahlungsunfaehigkeits- und Ueberschuldungspruefung — beide Insolvenzgruende haben eigene Prüfschemas.

## Typische Fehler

- Faellige Verbindlichkeiten werden nicht vollstaendig erfasst (z.B. gestundete Lieferantenforderungen oder Steuerruckstaende vergessen).
- Liquide Mittel werden zu optimistisch angesetzt (z.B. nicht verfuegbare Kreditlinien als liquide gewertet).
- Drei-Wochen-Vorschau wird mit rollierender Mehrmonatsplanung vermischt; beide dienen unterschiedlichen Zwecken.
- Fortbestehensprognose wird ohne belastbares Sanierungskonzept positiv bewertet.
- Eine 13-Wochen-Vorschau wird als Sanierungskonzept behandelt, obwohl GuV, Planbilanz, Maßnahmenwirkung und nachhaltige Sanierungsfähigkeit fehlen.
- Haftungsrisiken des Geschäftsführers nach § 15b InsO werden nicht kommuniziert.

## Quellen und Aktualitaet

- Stand: 05/2026
- InsO in der Fassung des SanInsFoG (in Kraft seit 01.01.2021); § 15b InsO ersetzt § 64 GmbHG a.F.
- BGH-Urteil zur Passiva-II-Methode (Leitsatz: Deckungsluecke dauerhaft über 10 Prozent indiziert Zahlungsunfaehigkeit)
