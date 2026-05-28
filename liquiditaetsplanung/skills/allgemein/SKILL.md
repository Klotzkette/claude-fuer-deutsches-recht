---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Liquiditaetsplanung — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Liquiditaetsplanung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau mit BGH-Passiva-II- und 10-Prozent-Schema, 13/26/52-Wochen-Forecast, Excel-Export mit Quote/Luecken-Ampel, Padlet/JSON-Round-Trip, Integration mit Fortbestehensprognose. Krisen-GmbH, Bugwellenrechtsprechung.

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
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditätsvorschau über 13/26/52 Wochen für GmbH/UG/AG. Erstellt zwingend eine Excel-Tabelle nach der hinterlegten Vorlage und auf Wunsch ein interaktives HTML-Padlet oder Markdown-Artefakt, das mit jeder… |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Drei-Wochen-Liquiditätsvorschau nach § 17 InsO. Erstellt zwingend eine Excel-Tabelle auf Wochenbasis und auf Wunsch ein interaktives HTML-Padlet oder Markdown-Artefakt zur fortlaufenden Pflege. Wendet… |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfähige Liquiditätsbilanz und Liquiditätsvorschau für die Prüfung der Zahlungsunfähigkeit (§ 17 InsO) und die Fortbestehensprognose (§ 19 InsO). Standardergebnis ist eine Excel-Tabelle auf Wochenbasis; auf… |

## Worum geht es?

Das Plugin unterstuetzt Steuerberater, Rechtsanwaelte und Geschaeftsfuehrer bei der Erstellung und Pruefung von Liquiditaetsvorschauen nach deutschem Recht. Im Mittelpunkt stehen die kurzfristige Drei-Wochen-Vorschau nach § 17 InsO sowie rollierende Forecasts ueber 13, 26 und 52 Wochen. Das Plugin erzeugt Excel-Tabellen nach dem BGH-Passiva-II- und 10-Prozent-Schema und integriert eine Quote-Luecken-Ampel.

Zielgruppe sind Berater und Organe von GmbH, UG und AG in wirtschaftlichen Krisensituationen, insbesondere wenn Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit oder Ueberschuldung geprueft werden muss. Die Instrumente unterstuetzen auch die Fortbestehensprognose sowie die Bugwellenrechtsprechung des BGH.

## Wann brauchen Sie diese Skill?

- Geschaeftsfuehrer oder Steuerberater benoetigt eine gerichtsfaehige Liquiditaetsvorschau zur Insolvenzantragspflicht-Pruefung nach § 15a InsO.
- Der Mandant prueft, ob Zahlungsunfaehigkeit nach § 17 InsO oder drohende Zahlungsunfaehigkeit nach § 18 InsO vorliegt.
- Zur Vorbereitung eines StaRUG-Restrukturierungsverfahrens oder Insolvenzplanverfahrens wird ein mehrstufiger Forecast benoetigt.
- Im Rahmen einer M&A-Transaktion oder einer Distressed-Situation ist eine nachvollziehbare Liquiditaetsplanung erforderlich.
- Der Berater muss die Drei-Wochen-Deckungsluecke nach dem BGH-Passiva-II-Schema berechnen und dokumentieren.

## Fachbegriffe (kurz erklaert)

- **Zahlungsunfaehigkeit (§ 17 InsO)** — Schuldner kann faellige Zahlungspflichten nicht mehr erfuellen; BGH-Formel: Deckungsluecke ueber 10 Prozent der faelligen Verbindlichkeiten.
- **Drohende Zahlungsunfaehigkeit (§ 18 InsO)** — Schuldner wird voraussichtlich nicht in der Lage sein, bestehende Zahlungspflichten bei Faelligkeit zu erfuellen.
- **BGH-Passiva-II-Schema** — Gerichtlich anerkannte Methode zur Berechnung der Liquiditaetsluecke; unterscheidet zwischen faelligen und nicht faelligen Verbindlichkeiten.
- **10-Prozent-Schwelle** — Liegt die Liquiditaetsluecke dauerhaft bei mehr als 10 Prozent der faelligen Gesamtverbindlichkeiten, indiziert das Zahlungsunfaehigkeit.
- **Rollierende Vorschau** — Fortlaufend aktualisierte Liquiditaetsplanung ueber 13, 26 oder 52 Wochen (3, 6 oder 12 Monate).
- **Fortbestehensprognose** — Beurteilung, ob das Unternehmen mit ueberwiegender Wahrscheinlichkeit fortbestehen wird; relevant fuer Ueberschuldungspruefung nach § 19 InsO.
- **Bugwellenrechtsprechung** — BGH-Rechtsprechung zur aufgeschobenen Faelligkeit von Verbindlichkeiten, die erst bei Vorliegen eines Insolvenzgrunds entfallen.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit
- § 18 InsO — Drohende Zahlungsunfaehigkeit
- § 19 InsO — Ueberschuldung
- § 15a InsO — Insolvenzantragspflicht
- §§ 64, 43 GmbHG a.F. bzw. § 15b InsO n.F. — Haftung bei Zahlungen nach Insolvenzreife
- §§ 238 ff. HGB — Buchfuehrungspflichten

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Krisensituation des Mandanten klaeren: Liegt Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit oder Ueberschuldung vor oder wird sie geprueft?
2. Erforderlichen Zeitraum bestimmen: Drei-Wochen-Vorschau (kurzfristig/insolvenzrechtlich) oder rollierender 13/26/52-Wochen-Forecast.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfrist pruefen: Bei konkretem Verdacht auf Zahlungsunfaehigkeit laeuft die Drei-Wochen-Antragsfrist des § 15a InsO.
5. Anschluss-Skill bestimmen: Nach Erstellung der Vorschau ggf. Fortbestehensprognose oder StaRUG-Pruefung.

## Skill-Tour (was gibt es hier?)

- `liquiditaetsvorschau-3wochen` — Wochenaktuelle Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Excel-Tabelle und Deckungsluecken-Ampel.
- `liquiditaetsvorschau-3-6-12-monate` — Rollierende Liquiditaetsvorschau ueber 13/26/52 Wochen fuer GmbH/UG/AG als Excel-Export mit Quote-Luecken-Ampel.
- `liquiditaetsvorschau-insolvenzrechtlich` — Gerichtsfaehige Liquiditaetsbilanz und Vorschau zur Pruefung der Zahlungsunfaehigkeit nach § 17 InsO und der Ueberschuldung.

## Worauf besonders achten

- Die Drei-Wochen-Frist des § 15a InsO ist eine echte Maximalfrist; bei konkretem Anfangsverdacht auf Zahlungsunfaehigkeit beginnt sie zu laufen.
- Das BGH-Passiva-II-Schema erfordert saubere Trennung zwischen faelligen und nicht faelligen Verbindlichkeiten; Fehler hier fuehren zu falschen Ergebnissen.
- Excel-Exporte muessen reproduzierbar und nachvollziehbar sein, da sie im Insolvenzverfahren als Beweismittel vorgelegt werden koennen.
- Die 10-Prozent-Schwelle ist eine Indizwirkung, kein automatischer Ausloeser; die Gesamtumstaende sind zu wuerdigen.
- Keine Vermischung von Zahlungsunfaehigkeits- und Ueberschuldungspruefung — beide Insolvenzgruende haben eigene Pruefschemas.

## Typische Fehler

- Faellige Verbindlichkeiten werden nicht vollstaendig erfasst (z.B. gestundete Lieferantenforderungen oder Steuerruckstaende vergessen).
- Liquide Mittel werden zu optimistisch angesetzt (z.B. nicht verfuegbare Kreditlinien als liquide gewertet).
- Drei-Wochen-Vorschau wird mit rollierender Mehrmonatsplanung vermischt; beide dienen unterschiedlichen Zwecken.
- Fortbestehensprognose wird ohne belastbares Sanierungskonzept positiv bewertet.
- Haftungsrisiken des Geschaeftsfuehrers nach § 15b InsO werden nicht kommuniziert.

## Querverweise

- Plugin `grosskanzlei-corporate-ma` (Skill `grosskanzlei-ma-liquiditaetsvorschau`) — Liquiditaetsvorschau im M&A/Distressed-Kontext.
- Plugin `grosskanzlei-corporate-ma` (Skill `grosskanzlei-ma-insolvenzreife`) — Insolvenzreife-Schwellencheck.
- Plugin `zwangsvollstreckung` — Vollstreckungsabwehr bei akuter Zahlungsunfaehigkeit.
- Plugin `wandeldarlehen-lebenszyklus` — Rangruecktritt zur Vermeidung insolvenzrechtlicher Nachrangwirkung.

## Quellen und Aktualitaet

- Stand: 05/2026
- InsO in der Fassung des SanInsFoG (in Kraft seit 01.01.2021); § 15b InsO ersetzt § 64 GmbHG a.F.
- BGH-Urteil zur Passiva-II-Methode (Leitsatz: Deckungsluecke dauerhaft ueber 10 Prozent indiziert Zahlungsunfaehigkeit)
