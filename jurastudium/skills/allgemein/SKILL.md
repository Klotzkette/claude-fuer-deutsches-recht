---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Jurastudium-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Jurastudium — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Jurastudium**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung.

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
| `ag-vorbereitung` | AG-Vorbereitung und Cold-Call-Prep für Jurastudium: Anwendungsfall Student wird im naechsten Seminar oder Arbeitsgemeinschaft aufgerufen und muss konkrete Faelle vorbereiten und Fragen des Dozenten antizipieren.… |
| `examens-prognose` | Examensprognose auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken: Anwendungsfall Student will Lernzeit auf wahrscheinliche Themen konzentrieren und fragt welche Schwerpunkte das Justizprüfungsamt bisher prüfte.… |
| `examensvorbereitung-fragen` | Examensvorbereitungs-Fragen für 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland… |
| `fall-zusammenfassung` | Juristischen Fall zusammenfassen und strukturieren: Anwendungsfall Student oder Referendar muss langen Sachverhalt oder Urteil in praegnante Fallzusammenfassung fassen und Kernprobleme herausarbeiten. Gutachtenstil,… |
| `gliederungs-baukasten` | Gliederungs-Baukasten für juristische Hausarbeiten und Seminararbeiten: Anwendungsfall Student erstellt Gliederung für Hausarbeit Seminararbeit oder wissenschaftliche Arbeit und braucht strukturierten Aufbau.… |
| `gutachten-uebung` | Gutachten Uebung für Jurastudium und Examensvorbereitung: Anwendungsfall Student bearbeitet Uebungsfall und soll Klausurtechnik Gutachtenstil Subsumtion und Zeitmanagement trainieren. Gutachtenstil mit Obersatz… |
| `jurastudium-anpassen` | Lernprofil im Jurastudium anpassen und aktualisieren: Anwendungsfall Student wechselt Lernstil, aendert Studienschwerpunkte, wechselt Bundesland oder aktualisiert Prüfungsziel von Zwischenprüfung auf Examen. 1. und 2.… |
| `jurastudium-kaltstart-interview` | Jurastudium-Einstieg und Lernprofil-Aufnahme: Anwendungsfall Student startet erstmals Jurastudium-Skill und muss Lernprofil Semester Bundesland Prüfungsziel und Lernstil konfigurieren. 1. StEx und 2. StEx, JAG… |
| `juristisches-schreiben` | Juristisches Schreiben trainieren für Klausur und Seminararbeit: Anwendungsfall Student will Schreibstil verbessern und benoetigt Feedback zu Formulierungen Argumentationsstruktur und Praegnanz. Gutachtenstil,… |
| `karteikarten` | Karteikarten für Jurastudium und Examensvorbereitung erstellen: Anwendungsfall Student will Definitionen Tatbestaende Normen und Klausurrelevante Faelle als Lernkarten strukturieren. Lösungsschemata, Tatbestaende,… |
| `lernplan` | Erstellt oder aktualisiert einen strukturierten Lernplan für das Erste Staatsexamen, das Referendariat oder das Zweite Staatsexamen — phasenbezogen, nach Schwächen gewichtet, adaptiv nach Lernverlauf. Berücksichtigt… |
| `lernsitzung` | Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion,… |
| `lernstrategien` | Lernstrategien für Jurastudium und Examensvorbereitung entwickeln: Anwendungsfall Student sucht effektive Lernmethoden für Examensvorbereitung und will Zeit und Energie optimal einsetzen. Examensvorbereitung 1. und 2.… |
| `loesungsschemata` | Stellt klassische Lösungsschemata für die deutsche Juristenklausur bereit — Anspruchsprüfung, Verbrechensaufbau, Grundrechtsprüfung, Verhältnismäßigkeit, Klageart-Bestimmung, EBV, Bereicherung, GoA, c.i.c.,… |
| `methodenlehre-grundlagen` | Übt die juristische Methodenlehre für Studierende — Auslegung nach Wortlaut/Systematik/Historie/Telos, Analogie, teleologische Reduktion, Auslegung gegen den Wortlaut, verfassungskonforme und unionsrechtskonforme… |
| `methodenlehre-oeffentliches-recht` | Übt die öffentlich-rechtliche Methodenlehre — Schichtenprüfung bei Grundrechten, Verhältnismäßigkeit, Ermessen und Ermessensfehler, Verwaltungsaktqualität, prozessuale Methodik der Klagearten, unionsrechtskonforme… |
| `methodenlehre-strafrecht` | Übt die strafrechtliche Methodenlehre — dreistufiger Verbrechensaufbau (Tatbestand, Rechtswidrigkeit, Schuld), Trennung objektiver/subjektiver Tatbestand, Konkurrenzlehre (Tateinheit § 52, Tatmehrheit § 53,… |
| `methodenlehre-zivilrecht` | Übt die zivilrechtliche Methodenlehre für Studierende — Anspruchsgrundlagen-Schema, AGL-Reihenfolge (vertraglich, vertragsähnlich, dinglich, deliktisch, bereicherungsrechtlich), Konkurrenzen, Auslegung von… |
| `pruefungsgespraech-ag` | Prüfungsgespraech und Sokrates-Methode in Arbeitsgemeinschaft simulieren: Anwendungsfall Student will AG-Diskussion oder Dozentengespraeach simulieren und Argumentation trainieren. Subsumtion, Lösungsschemata,… |
| `rechtsgeschichte` | Übt deutsche und europäische Rechtsgeschichte für Studierende — römisches Recht und die BGB-Entstehung 1900, NS-Unrechtsjustiz und die Folgen der Radbruchschen Formel, SED-Unrecht und Mauerschützenprozesse, Entstehung… |
| `subsumtionslehre` | Übt die Subsumtion als Königsdisziplin der deutschen Klausur — Trennung Obersatz/Definition/Subsumtion/Ergebnis, Tatbestandsmerkmal für Tatbestandsmerkmal, mit Pushback bei Subsumtionssprüngen, vorweggenommener… |
| `tatbestaende-lernen` | Tatbestaende lernen für Jurastudium und Examensvorbereitung: Anwendungsfall Student muss Tatbestaende und Definitionen sicher beherrschen für Klausuren und Examen. Lösungsschemata Tatbestandsmerkmale BGB Strafrecht… |

## Worum geht es?

Dieses Plugin unterstuetzt Jurastudenten und Referendare bei allen Phasen der juristischen Ausbildung: von der Einuebung des Gutachtenstils und der Subsumtion ueber die Methodenlehre in allen drei Hauptrechtsgebieten bis hin zur strukturierten Examensvorbereitung. Es orientiert sich an der AG-Tradition (Arbeitsgemeinschaft) und an den Anforderungen des Ersten und Zweiten Staatsexamens in deutschen Bundeslaendern.

Das Plugin ist kein Rechtsgutachten-Generator fuer echte Mandate, sondern ein Lernassistent: interaktive Uebungen, Feedback zu Gutachten, Karteikarten, Lernplaene und Pruefungsgespraeche stehen im Vordergrund.

## Wann brauchen Sie diese Skill?

- Sie bereiten sich auf eine Klausur oder das Erste Staatsexamen vor und benoetigen strukturierte Uebungsaufgaben mit Feedback.
- Sie wollen den Gutachtenstil, die Subsumtion oder die juristische Methodenlehre gezielt trainieren.
- Sie muessen einen Lernplan fuer die Examensvorbereitung erstellen und nach Schwaechen gewichten.
- Sie bereiten sich auf ein Pruefungsgespraeach oder eine AG-Diskussion vor und wollen moegliche Dozentenfragen antizipieren.
- Sie suchen Loesungsschemata fuer Zivilrecht, Strafrecht oder oeffentliches Recht als Orientierungsrahmen fuer die Klausurbearbeitung.

## Fachbegriffe (kurz erklaert)

- **Gutachtenstil** — Der klassische juristische Schreibstil mit Obersatz, Definition, Subsumtion und Ergebnis je Tatbestandsmerkmal.
- **Urteilsstil** — Umgekehrte Reihenfolge: Ergebnis zuerst, dann Begruendung; im Urteil und in bestimmten Klausurteilen.
- **Subsumtion** — Einordnung des Sachverhalts unter die Definition eines Tatbestandsmerkmals.
- **Loesungsschema** — Strukturierter Pruefungsaufbau fuer ein Rechtsgebiet (z.B. Anspruchspruefungsschema BGB, Verbrechensaufbau StGB).
- **AG** — Arbeitsgemeinschaft; Kleingruppenveranstaltung im Jurastudium mit Sokrates-Methode und Fallbearbeitung.
- **JPA** — Justizpruefungsamt; prueft das Erste Staatsexamen (Erste Juristische Pruefung).
- **Repetitorium** — Kommerzielle Vorbereitungskurse fuer das Erste oder Zweite Staatsexamen (z.B. Alpmann, Hemmer, Kaiser).

## Rechtsgrundlagen

- §§ 133, 157 BGB — Auslegung von Willenserklaerungen
- §§ 195 ff. BGB — Verjaehrung (klausurrelevant)
- §§ 305 ff. BGB — AGB-Recht (Auslegungsfragen)
- Art. 103 Abs. 2 GG — Analogieverbot im Strafrecht
- §§ 52, 53 StGB — Tateinheit, Tatmehrheit (Konkurrenzlehre)
- Art. 267 AEUV — Vorabentscheidungsverfahren (Methodenlehre EU-Recht)
- JAG der jeweiligen Bundeslaender — Zugelassene Hilfsmittel, Themenbereiche Staatsexamen

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Welche Ausbildungsphase (Studium, Repetitorium, Referendariat, Zweites Staatsexamen), welches Bundesland, welche Schwerpunkte.
2. Phase des Mandats bestimmen: Konfiguration, Lernplanung, Uebung, Klausurtraining oder Pruefungsgespraeach.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Lernprofil konfigurieren mit `jurastudium-kaltstart-interview` wenn Plugin erstmals genutzt wird.
5. Anschluss-Skill bestimmen: nach Lernplan typischerweise Lernsitzung oder Gutachten-Uebung; nach Examens-Prognose gezieltes Thementraining.

## Skill-Tour (was gibt es hier?)

**Konfiguration**

- `jurastudium-kaltstart-interview` — Ersteinrichtung: Lernprofil, Semester, Bundesland, Pruefungsziel und Lernstil aufnehmen.
- `jurastudium-anpassen` — Lernprofil aktualisieren: Lernstil aendern, Schwerpunkte anpassen, Bundesland wechseln.

**Lernplanung**

- `lernplan` — Strukturierten Lernplan erstellen fuer Erstes Staatsexamen, Referendariat oder Zweites Staatsexamen; phasenbezogen und nach Schwaechen gewichtet.
- `lernstrategien` — Effektive Lernmethoden entwickeln: Spaced-Repetition, aktives Erinnern, Priorisierung nach Pruefungsrelevanz.
- `examens-prognose` — Gewichtete Themenliste mit Lernprioritaet auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken.

**Lernen und Ueben**

- `lernsitzung` — Interaktive Lernsitzung zu bestimmtem Thema mit Erklaerungen, Uebungsaufgaben und sofortigem Feedback.
- `karteikarten` — Karteikarten fuer Definitionen, Tatbestaende und Normen fuer Spaced-Repetition erstellen.
- `tatbestaende-lernen` — Tatbestaende und Definitionen sicher einueben mit Abgrenzungshinweisen und Examensrelevanz.
- `fall-zusammenfassung` — Langen Sachverhalt oder Urteil in praegnante Fallzusammenfassung fassen.

**Gutachten und Klausurtechnik**

- `gutachten-uebung` — Gutachten-Uebung: Klausurtechnik, Gutachtenstil, Subsumtion und Zeitmanagement trainieren.
- `juristisches-schreiben` — Schreibstil verbessern: Feedback zu Formulierungen, Argumentationsstruktur und Praegnanz.
- `gliederungs-baukasten` — Gliederung fuer Hausarbeiten und Seminararbeiten strukturiert aufbauen.
- `examensvorbereitung-fragen` — Uebungsfragen fuer Erstes und Zweites Staatsexamen mit Musterloesungen und Schwachstellen-Hinweis.

**Pruefungsgespraeach und AG**

- `pruefungsgespraech-ag` — AG-Diskussion oder Dozentengespraeach simulieren und Argumentation mit Sokrates-Methode trainieren.
- `ag-vorbereitung` — Cold-Call-Vorbereitung: Faelle fuer Seminar oder AG aufbereiten und Dozentenfragen antizipieren.

**Methodenlehre**

- `subsumtionslehre` — Subsumtion als Koenigsdisziplin der deutschen Klausur einueben; Pushback bei Subsumtionsspruengen.
- `methodenlehre-grundlagen` — Juristische Methodenlehre: Wortlaut, Systematik, Historie, Telos, Analogie, teleologische Reduktion.
- `methodenlehre-zivilrecht` — Zivilrechtliche Methodenlehre: AGL-Reihenfolge, Willenserklaerungs-Auslegung, AGB-Auslegung.
- `methodenlehre-strafrecht` — Strafrechtliche Methodenlehre: dreistufiger Verbrechensaufbau, Konkurrenzlehre, Analogieverbot.
- `methodenlehre-oeffentliches-recht` — Oeffentlich-rechtliche Methodenlehre: Grundrechtspruefung, Verhaeltnismaessigkeit, Ermessen, Klageart.

**Loesungsschemata und Rechtsgeschichte**

- `loesungsschemata` — Klassische Loesungsschemata: Anspruchspruefung, Verbrechensaufbau, Grundrechtspruefung und weitere.
- `rechtsgeschichte` — Deutsche und europaeische Rechtsgeschichte: roemisches Recht, BGB-Entstehung, NS-Justiz, SED-Unrecht, GG-Genese.

## Worauf besonders achten

- **Lernprofil zu Beginn konfigurieren.** Skill `jurastudium-kaltstart-interview` muss vor anderen Skills ausgefuehrt werden; ohne Bundesland und Pruefungsziel sind Empfehlungen unscharf.
- **Schemata sind keine Dogmatik.** Loesungsschemata koennen das Verstaendnis unterstuetzen, sind aber nie zwingend; Abweichungen und Kontroversen erkennen.
- **Zeitmanagement in der Klausur.** Ein haeufiger Fehler ist Ueberschreiten der Zeit im Oberteil; Skill `gutachten-uebung` simuliert Zeitlimit.
- **Bundesland-Varianten beachten.** JAG-Anforderungen und zugelassene Hilfsmittel variieren; Prognosen und Lernplaene immer bundesland-spezifisch konfigurieren.
- **Subsumtionsspruenge erkennen.** Das Plugin gibt aktiv Pushback, wenn Definition und Sachverhalt uebersprungen werden.

## Typische Fehler

- Gutachten beginnt mit dem Ergebnis statt mit dem Obersatz; Urteilsstil und Gutachtenstil werden vermischt.
- Definitionen werden aus dem Kopf formuliert statt aus herrschender Meinung und Rechtsprechung abgeleitet.
- Einreden und Gegenansprueche werden nicht geprueft; Subsumtion endet bei der anspruchsbegruendenden Norm.
- Zeitlimit wird nicht simuliert; in der echten Klausur fehlt Zeit fuer spaetere Punkte.
- Rechtsgeschichte und Methodenlehre werden als prueflungsirrelevant abgetan; beide koennen im Staatsexamen gefragt werden.

## Querverweise

- `subsumtions-pruefer` — Fuer vertiefte mechanische Subsumtion von Normen ausserhalb des Lernkontexts.
- `verfassungsrecht` — Fuer vertiefte Verfassungsrechtsfragen im oeffentlichen Recht.
- `gesellschaftsrecht` — Wenn gesellschaftsrechtliche Faelle im Studium behandelt werden.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (BGB, StGB, GG, ZPO, VwGO, HGB, AEUV)
- Repetitoriumskalender: Alpmann, Hemmer, Jura Intensiv, Kaiser-Skripten in aktueller Auflage
