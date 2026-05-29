---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Rechtsberatungsstelle — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Rechtsberatungsstelle**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** `skill-name` — [warum dieser Skill hilft]
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
| `anleiter-pruefwarteschlange` | Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell "formelle… |
| `einarbeitung` | Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte… |
| `einfache-sprache-briefe` | Anwalts- und Behoerdenbriefe in leichte oder einfache Sprache uebersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behoerde Gericht oder Gegenseite… |
| `entwurf` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6… |
| `formular-erzeugung` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behoerde oder Gericht. BeratungsHiG Beratungsschein,… |
| `fristen` | Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard:… |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache.… |
| `mandant-aufnahme` | Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen.… |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO… |
| `mandantenbrief` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behoerde oder Gericht vorbereiten.… |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit… |
| `recherche-start` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, Quellenprüfung, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Studierende… |
| `rechtsberatungsstelle-anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG,… |
| `rechtsberatungsstelle-kaltstart-interview` | Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet… |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des… |
| `status` | Fallstatuszusammenfassung nach Zielgruppe — mandantengerichtet (verständliche Sprache), intern (für den Supervisor) oder gerichts-/behördengerichtet (formale Schriftsatzform per Verfahrensordnung). Gleiche Fakten,… |

## Worum geht es?

Das Plugin unterstuetzt studentische und gemeinnuetzige Rechtsberatungsstellen bei der RDG-konformen Durchfuehrung ihrer Beratungsarbeit. Es bildet den gesamten Lebenszyklus eines Mandats ab: von der Erstaufnahme ueber die rechtliche Analyse und Schriftstueckerstellung bis zur sauberen Semesteruebergabe.

Besonderheit gegenueber Anwaltsplugins: Studierende sind keine zugelassenen Rechtsanwaelte. Die Beratungsleistung muss im Rahmen der nach § 6 RDG erlaubten unentgeltlichen Rechtsdienstleistungen bleiben. Alle wesentlichen Dokumente beduerften einer Anleiter-Freigabe. Das Plugin beruecksichtigt diese Aufsichtsstruktur mit einer optionalen Pruefwarteschlange.

## Wann brauchen Sie diese Skill?

- Ein neuer Studierender startet seine Arbeit in der Rechtsberatungsstelle und benoetigt Einarbeitung in Struktur, RDG-Grundlagen und Tools.
- Ein Mandant meldet sich mit einem konkreten Rechtsproblem und muss mit Sachverhalt, Fristen und Interessenkonfliktpruefung aufgenommen werden.
- Sie benoetigen Schriftsaetze, Antraege oder Mandantenbriefe in verstaendlicher Sprache fuer Mandanten mit sprachlichen Einschraenkungen.
- Das Semester endet und laufende Mandate sollen sauber an die naechste Studierendenkohorte uebergeben werden.
- Sie wollen das Plugin an Ihre Hochschule und deren Rechtsgebiete anpassen.

## Fachbegriffe (kurz erklaert)

- **RDG** — Rechtsdienstleistungsgesetz; regelt, wer ausserhalb der Anwaltschaft Rechtsdienstleistungen erbringen darf.
- **§ 6 RDG** — Erlaubnisnorm fuer unentgeltliche Rechtsdienstleistungen; Grundlage fuer studentische Beratungsstellen.
- **BeratungsHiG** — Beratungshilfegesetz; ermoeglicht einkommensschwachen Personen staatlich gefoerderte Rechtsberatung.
- **Anleiter** — Zugelassener Rechtsanwalt, der die Aufsicht ueber Studierende fuehrt und Arbeitsergebnisse freigibt.
- **Gutachtenmethode** — Juristische Analyse nach dem Schema Obersatz - Norm/Definition - Subsumtion - Ergebnis.
- **Interessenkonflikt** — Situation, in der Berater oder Kanzlei bereits die Gegenpartei vertreten; muss vor Mandatsannahme geprueft werden (§ 43a Abs. 4 BRAO entsprechend).
- **Pruefwarteschlange** — Optionale Aufsichtsstruktur, in der Arbeitsergebnisse auf Anleiter-Freigabe warten, bevor sie den Mandanten oder Gerichten zugehen.

## Rechtsgrundlagen

- § 2 RDG — Rechtsdienstleistungs-Begriff
- § 3 RDG — Erlaubnisvorbehalt
- § 6 RDG — Unentgeltliche Rechtsdienstleistungen
- § 43a BRAO — Allgemeine Berufspflichten (Verschwiegenheit, Interessenkonflikt; entsprechend anwendbar)
- BeratungsHiG — Beratungshilfegesetz
- DSGVO Art. 6 Abs. 1 und Art. 13 — Datenschutz bei der Mandatsbearbeitung
- BDSG § 26 — Datenschutz bei studentischen Arbeitnehmerverhaeltnissen

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview durchfuehren und Plugin an Hochschule und Rechtsgebiete anpassen.
2. Neue Studierende einarbeiten (Semester-Start).
3. Mandanten aufnehmen: Sachverhalt, Fristen, Interessenkonflikt und Beratungsberechtigung pruefen.
4. Passenden Skill auswaehlen (Memo, Entwurf, Mandantenbrief, einfache Sprache, Formular).
5. Ergebnis in Pruefwarteschlange stellen; nach Anleiter-Freigabe versenden oder weitergeben.

## Skill-Tour (was gibt es hier?)

- `anleiter-pruefwarteschlange` — Supervisoren-Pruefwarteschlange fuer studentische Arbeitsergebnisse vor Anleiter-Freigabe.
- `einarbeitung` — Semestereinarbeitung fuer neue studentische Berater mit RDG-Grundlagen und Toolwalkthrough.
- `einfache-sprache-briefe` — Anwalts- und Behoerdenbriefe in leichte oder einfache Sprache uebersetzen fuer Mandanten mit sprachlichen Einschraenkungen.
- `entwurf` — Erstentwurf haeufiger Schriftstuecke (Widerspruch, Mietrechtsbrief, Klageschrift im Beratungshilfe-Kontext).
- `formular-erzeugung` — Formulare und Antragsdokumente fuer Behoerden oder Gerichte erstellen.
- `fristen` — Fristenmanagement fuer laufende Mandate mit Warnschwellen und Eskalation.
- `leitfaden-erstellen` — Praxisleitfaeden fuer haeufige Mandatskonstellationen in verstaendlicher Sprache erstellen.
- `mandant-aufnahme` — Strukturierter Mandantenintake mit Sachverhaltserfassung, Dringlichkeit und Interessenkonfliktpruefung.
- `mandanten-kommunikations-log` — Mandantenkommunikation datenschutzkonform dokumentieren und Kommunikations-Log fuehren.
- `mandantenbrief` — Mandantenbrief in verstaendlicher oder foermlicher Sprache verfassen.
- `memo` — Gutachten-Geruest nach Gutachtenmethode mit markierten Luecken fuer studentische Analyse erstellen.
- `recherche-start` — Recherchefahrplan fuer eine Rechtsfrage mit Normen, Rechtsprechungsbereichen und Suchbegriffen.
- `rechtsberatungsstelle-anpassen` — Plugin an spezifische Hochschule, Rechtsgebiete und Verfahrensregeln anpassen.
- `rechtsberatungsstelle-kaltstart-interview` — Erst-Konfiguration des Plugins mit Hochschule, Anleiter und Beratungsregeln.
- `semester-uebergabe` — Semesterabschluss-Uebergabe laufender Mandate mit Uebergabenotizen und Gesamtuebersicht.
- `status` — Fallstatuszusammenfassung mandantengerichtet, intern oder gerichts-/behoerdengerichtet erstellen.

## Worauf besonders achten

- **RDG-Grenze einhalten**: Studierende duerfen keine individualrechtliche Beratung ausserhalb des § 6 RDG-Rahmens erbringen; Abgrenzung zu anwaltlicher Taetigkeit ist essentiell.
- **Anleiter-Freigabe vor Versand**: Kein Schriftstuck und kein Mandantenbrief verlasst die Beratungsstelle ohne Anleiter-Freigabe.
- **Fristen besonders beobachten**: Versaeumte Fristen koennen den Mandanten seinen Anspruch kosten; der Fristen-Skill muss regelmaessig abgerufen werden.
- **Mandatsgeheimnis bei Semesteruebergabe**: Uebergabenotizen duerfen nur mit dem Einverstaendnis des Mandanten weitergegeben werden.
- **Dokumentation datenschutzkonform**: Mandantendaten duerften nicht in nicht-genehmigten KI-Systemen verarbeitet werden.

## Typische Fehler

- Interessenkonfliktpruefung vergessen: Zwei Studierende aus derselben Kohorte beraten unwissentlich Parteien desselben Konflikts.
- Memo als fertige Rechtsberatung weitergeben statt als Analyse-Grundlage fuer den Anleiter.
- Fristenliste nicht aktuell halten; Fristaenderungen durch Gericht werden nicht eingetragen.
- Bei der Semesteruebergabe Mandate ohne Uebergabenotiz an Nachfolgekohorte weitergeben.
- Einfache-Sprache-Uebersetzung nicht auf Richtigkeit pruefen lassen; Vereinfachungen koennen Rechtsinhalte veraendern.

## Querverweise

- `kanzlei-allgemein` — Vollstaendiges Kanzlei-Workflow-Plugin fuer zugelassene Anwaelte.
- `selbstvertreter-amtsgericht` — Wenn Mandanten ohne Anwalt vor dem Amtsgericht auftreten wollen.
- `aktenauszug-gerichtsverfahren` — Fuer schnelle Einarbeitung in laufende Verfahren der Beratungsstelle.
- `ki-richtlinie-kanzleien` — KI-Nutzungsrichtlinie fuer den verantwortungsvollen KI-Einsatz in der Beratungsstelle.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- RDG in der ab 2023 gueltigen Fassung
