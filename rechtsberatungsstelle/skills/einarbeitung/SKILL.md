---
name: einarbeitung
description: "Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermittelt es interaktiv. Lädt, wenn ein neuer studentischer Berater „Einarbeitung starten\", „ich bin neu in der Klinik\", „Einführung\" sagt oder zu Semesterbeginn gestartet wird; `--karte` für die einseitige Referenzkarte."
---

# Einarbeitung: Semestereinarbeitung

## Zweck

Jedes Semester verliert die Rechtsberatungsstelle ihre gesamte studentische Belegschaft und baut sie neu auf. Neue Studierende müssen Verfahrensabläufe, Mandatsverwaltung, Einreichungskonventionen und Rechtsgebiet-Grundlagen kennenlernen, bevor sie produktiv arbeiten können. Traditionell kostet das Wochen mit PDF-Lektüre und immer wiederkehrenden Fragen an den Supervisor.

Diese Skill ist der geführte Walkthrough. Sie liest, was der Supervisor beim Kalt-Start hinterlegt hat — das Handbuch, Einreichungsanleitungen, Verfahrensregeln — und vermittelt es interaktiv, mit Übungsaufgaben in einem sicheren Rahmen, bevor ein echter Mandant betroffen ist.

**Zielgruppe: Studierende.** Supervisoren nutzen `/kalt-start-interview`.

## Eingaben

Keine aktiven Eingaben — die Skill liest die Klinik-Konfiguration (CLAUDE.md) und das hinterlegte Handbuch.

Falls die Konfigurationsdatei fehlt oder noch Platzhalter enthält: „Die Beratungsstelle ist noch nicht eingerichtet. Bitten Sie [Supervisor] zuerst `/kalt-start-interview` auszuführen."

## Rechtlicher Rahmen

### Kernvorschriften für die Einarbeitung

- **§ 6 Abs. 1 RDG** — Unentgeltliche Rechtsdienstleistung: Studierende dürfen im Rahmen der Rechtsberatungsstelle Rechtsberatung erbringen, soweit sie unentgeltlich erfolgt und unter Aufsicht eines Rechtsanwalts/einer Rechtsanwältin steht.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht des begleitenden Rechtsanwalts/der begleitenden Rechtsanwältin: Die Aufsichtsperson muss zur Rechtsanwaltschaft zugelassen sein; die Aufsicht muss inhaltlich effektiv sein (kein Formalia-Supervisor).
- **§ 43a Abs. 2 BRAO, § 203 Abs. 3 StGB** — Mandatsgeheimnis und Verschwiegenheitspflicht: Gilt sinngemäß für Studierende als berufsmäßig tätige Gehilfen. Alle Mandantendaten, Fallnotizen und Korrespondenz sind vertraulich. Kein Austausch über Mandate außerhalb der Beratungsstelle.
- **§§ 1, 2 BerHG** — Beratungshilfe: Häufig in der Mandatsarbeit relevant; Studierende müssen wissen, wann ein Beratungshilfe-Schein vor Leistungsbeginn einzuholen ist.
- **§§ 114 ff. ZPO** — Prozesskostenhilfe (PKH): Voraussetzungen und typisches Prozedere in der Mandatsarbeit.

### Leitentscheidungen

- BGH, Urt. v. 26.10.2017 – IX ZR 285/16, NJW 2018, 314 Rn. 10 — Haftung des aufsichtführenden Rechtsanwalts für Fehler in der Mandatsbearbeitung durch nachgeordnete Personen; sinngemäß für Supervisoren der Beratungsstelle.
- BVerfG, Beschl. v. 14.07.1987 – 1 BvR 537/81, NJW 1988, 191 — Recht auf anwaltliche Erstberatung; Grundlage für das Beratungshilfe-System.
- BGH, Urt. v. 15.04.2010 – IX ZR 189/09, NJW 2010, 2050 Rn. 8 — Verschwiegenheitspflicht im Mandatsverhältnis; keine Weitergabe ohne Einwilligung des Mandanten.
- BAG, Urt. v. 08.05.2014 – 2 AZR 75/13, NZA 2014, 1248 Rn. 14 — Vertragliche Schweigepflicht und § 203 StGB; auf Ausbildungsverhältnisse sinngemäß anwendbar.

### Kommentarliteratur

- Deckenbrock/Henssler, RDG, 5. Aufl. 2021, § 6 Rn. 1 ff. — Voraussetzungen der unentgeltlichen Rechtsdienstleistung; Anforderungen an die Aufsicht.
- Kleine-Cosack, BRAO, 8. Aufl. 2022, § 43a Rn. 15 ff. — Verschwiegenheitspflicht; Umfang und Ausnahmen.
- Brenneke/Lux, Recht der Rechtsdienstleistungen, 2. Aufl. 2022, § 6 RDG Rn. 33 ff. — Studentische Rechtsberatungsstellen; praktische Anforderungen.
- Schütz, Das Recht der Beratungshilfe, 3. Aufl. 2020, § 1 BerHG Rn. 5 ff. — Voraussetzungen; Verfahren.

## Ablauf

### Begrüßung

> Willkommen in der [Name der Beratungsstelle]. Ich führe Sie durch die Arbeitsweise dieser Beratungsstelle und die verfügbaren Tools — ca. zwanzig Minuten, Pause jederzeit möglich. Am Ende haben Sie eine Übungsberatung durchgeführt, einen Übungsentwurf erstellt und einen Recherchefahrplan erarbeitet.
>
> Ein wichtiger Grundsatz vorab: Alles, was ich erzeuge, ist ein Ausgangspunkt. Die rechtliche Analyse kommt von Ihnen. [Supervisor] prüft Ihre Arbeit [entsprechend dem Supervisionsmodell]. Ich übernehme die Formatierung und den Erstentwurf, damit Ihre Zeit der juristischen Denkarbeit zugute kommt.
>
> Was Sie als Studierender nach § 6 RDG dürfen und was nicht: Sie beraten unter Aufsicht und unentgeltlich. Sie erstellen keine selbständigen Rechtsprodukte ohne Supervisoren-Freigabe. Jedes nach außen gehende Schriftstück und jede Mandantenauskunft zu strittigen Rechtsfragen wird vom Supervisor freigegeben.

### Teil 1: Diese Beratungsstelle (5 Min)

Aus der Klinik-Konfiguration und dem hinterlegten Handbuch. Interaktiv abarbeiten:

- **Rechtsgebiete** — Was berät die Klinik? Was nicht? (Und wohin verweisen, wenn jemand mit einem nicht abgedeckten Problem kommt?)
- **Mandanten** — Wer kommt? Welche besonderen Umstände gibt es (Sprache, Vulnerable Gruppen, unbegleitete Minderjährige)?
- **Zuständiges Gericht / Behörden** — Welche Gerichte und Behörden sind für die Klinik regelmäßig relevant? Lokale Besonderheiten?
- **Mandatsverwaltung** — Wie werden Mandate geführt, wo liegen Akten, was ist ein gut dokumentierter Fall?
- **Supervision** — Wie läuft die Prüfung ab (entsprechend dem Supervisionsmodell). Konkret: „Bevor etwas zum Mandanten oder an ein Gericht geht, [kommt es in die Prüfwarteschlange / sprechen Sie mit Frau/Herrn X / etc.]"

Kein Monolog — Verständnis überprüfen: „Wenn ein Mandant mit einem Räumungsbegehren und gleichzeitig einem Aufenthaltsrechtsproblem kommt — was tun Sie?" (Antwort: Beide Fragen in der Aktennotiz festhalten; das Aufenthaltsrechtsproblem ggf. an spezialisierte Flüchtlingsberatung weiterleiten oder dem Supervisor flaggen, je nach Tätigkeitsbereich der Klinik.)

### Teil 2: Die Befehle (5 Min)

| Befehl | Wann verwenden | Was Sie bekommen |
|---|---|---|
| `/mandanten-aufnahme` | Beratungsgespräch | Strukturierte Fallzusammenfassung mit erkannten Rechtsfragen, Interessenkollisionsprüfung, Triage |
| `/entwurf [Schriftstücktyp]` | Erstentwurf eines häufigen Schriftstücks | Rechtsgebiet-Muster aus den Fallnotizen — *Ausgangspunkt, nicht fertig* |
| `/memo` | Interne Fallanalyse | Gutachten-Gerüst nach Gutachtenmethode mit gekennzeichneten Recherchelücken |
| `/recherche-start [Frage]` | Einstieg in Rechtsrecherche | Recherchefahrplan: Normen, Rspr.-Bereiche, Suchbegriffe — *Hinweise, keine geprüften Belege* |
| `/status [Zielgruppe]` | Jemanden über einen Fall informieren | Zusammenfassung für Mandant / Supervisor / Gericht |
| `/mandantenbrief [typ]` | Routine-Korrespondenz | Terminbestätigung, Unterlagenbitte, Statusupdate aus Mustern |

Für jeden Befehl: was er tut, was er ausdrücklich nicht tut, was der/die Studierende vor dem Verwenden prüft.

### Teil 3: Übungsaufgaben (8–10 Min)

**Ohne Risiko. Fiktiver Mandant. Echte Tools.**

**Übung 1 — Übungsaufnahme:**
> Hier ist ein fiktives Szenario: [Rechtsgebiet-angepasste Aufgabe — z. B. für eine Mietrechtsklinik: „Frau Erdem hat letzte Woche eine fristlose Kündigung erhalten. Sie ist mit zwei Monatsmieten im Rückstand, nachdem sie ihren Job verloren hat. Die Heizung ist seit November defekt. Sie hat zwei Kinder."]
>
> Führen Sie `/mandanten-aufnahme` aus und sprechen Sie mit mir wie mit Frau Erdem. Ich antworte wie Frau Erdem. Schauen Sie am Ende auf die erzeugte Fallzusammenfassung: Welche Rechtsfragen wurden erkannt? Wurde die Mängeleinrede (§ 536 BGB) als mögliche Verteidigung erkannt?

Nachbesprechung: Was die Aufnahme erfasst hat, wo der Studierende tiefer hätte bohren sollen, was dem Supervisor zu flaggen ist.

**Übung 2 — Übungsentwurf:**
> Verwenden Sie Frau Erdems Aufnahme und führen Sie `/entwurf widerspruch-kuendigung` aus. Sie erhalten einen Erstentwurf.
>
> Lesen Sie ihn kritisch. Was ist richtig? Was ist falsch? Was würden Sie vor Vorlage an [Supervisor] ändern?

Ziel: Der Entwurf ist kompetent, aber nicht abschließend. Der Studierende lernt, kritisch zu lesen statt blind zu akzeptieren.

**Übung 3 — Recherchefahrplan:**
> Führen Sie `/recherche-start "Mietminderung wegen Heizungsausfall nach § 536 BGB"` aus. Sie erhalten einen Fahrplan — Normen, Rspr.-Bereiche, Suchbegriffe.
>
> Nichts davon ist geprüft. Das ist so gewollt. Nennen Sie eine Norm aus dem Fahrplan und beschreiben Sie, wie Sie deren Aktualität und Einschlägigkeit prüfen würden.

Ziel: `/recherche-start` ist ein Startpunkt, keine Quelle. Der Studierende forscht selbst.

### Teil 4: Verifikationsgewohnheiten (2 Min)

Die entscheidenden Gewohnheiten:

- **Jede Ausgabe ist ein Ausgangspunkt.** Wenn etwas den Mandanten oder ein Gericht erreicht, ohne dass Sie es kritisch gelesen haben, ist etwas schiefgelaufen.
- **Jede Quelle verifizieren**, bevor sie in ein Schriftstück fließt. `/recherche-start` gibt Hinweise, keine Belege.
- **Rechtsgebiet-spezifische Details prüfen.** Die Konfiguration kennt Ihr Bundesland; lokale Besonderheiten ändern sich — aktuell gültige Regeln gegenprüfen.
- **UNSICHER-Flags ernst nehmen.** Ein `[UNSICHER: ...]`-Flag ist ein Rechercheauftrag oder ein Thema für den Supervisor, kein zu löschender Fehler.
- **Mandatsgeheimnis immer.** Keine Fallinformationen außerhalb der Beratungsstelle weitergeben, auch nicht zum „Erklären" — § 203 StGB.
- **[Supervisionshinweis entsprechend dem Klinik-Modell]** — was wird geprüft, bevor es die Klinik verlässt, und wie.

### Abschluss

> Das war es. Sie haben eine Aufnahme durchgeführt, einen Entwurf erstellt und einen Recherchefahrplan erarbeitet. Ihr erster echter Fall wird ähnlich ablaufen — mit dem Unterschied, dass der Mandant real ist und der Supervisor Ihre Arbeit liest.
>
> Die einseitige Referenzkarte: `/einarbeitung --karte`

## `/einarbeitung --karte`

Erzeugt die einseitige Studentenreferenzkarte. Inhalt:

- Die Befehle (Tabelle aus Teil 2, komprimiert)
- Was die KI leisten kann / was nicht (Ausgangspunkte ja, fertige Arbeitsergebnisse nein, geprüfte Quellen nein)
- Verifikationsgewohnheiten (Punkte aus Teil 4)
- Wen fragen bei Unklarheiten (Supervisorenname aus CLAUDE.md)
- **RDG-Kurzhinweis:** Was Studierende nach § 6 RDG dürfen und was nicht

Druckfähig. Eine Seite. Am ersten Tag aushändigen.

## Risiken und typische Fehler

- **Einarbeitung als Formalität behandeln:** Die Übungsaufgaben sind der Kern. Studierende, die sie überspringen, gehen mit falscher Sicherheit ins erste echte Mandat.
- **RDG-Grenzen nicht verinnerlicht:** Studierende müssen wissen, dass sie nur unter Aufsicht und unentgeltlich tätig sind. Kein eigenständiges Handeln ohne Supervisoren-Rückkopplung.
- **Mandatsgeheimnis vergessen:** Bereits in der Übungsphase: Fallhypothetika enthalten keine echten Mandantendaten. In der echten Arbeit: strikte Vertraulichkeit nach § 203 StGB.
- **Supervisor nicht eingerichtet:** Wenn die CLAUDE.md Platzhalter enthält, ist die Einarbeitung zu stoppen und dem Supervisor zur Einrichtung zu übergeben.

## Quellenpflicht

Die Einarbeitung selbst enthält keine zitierpflichtigen Belege — die RDG-Normen und Grundsätze werden im Überblick vermittelt. Sobald echte Mandate bearbeitet werden, gilt die Quellenpflicht aus den jeweiligen Skills (`/memo`, `/entwurf`, `/recherche-start`).

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall und keine juristische Ausbildung. Die inhaltliche Einführung in das Rechtsgebiet übernimmt der Supervisor, nicht dieses Tool.

## Ausgabeformat

Die Einarbeitung läuft interaktiv — keine einmalige Ausgabe, sondern ein geführtes Gespräch in vier Teilen (Klinik-Kontext, Befehle, Übungsaufgaben, Verifikationsgewohnheiten). Jeder Teil schließt mit einer Verständnisfrage oder einer Übung, bevor zum nächsten Teil übergegangen wird.

`/einarbeitung --karte` erzeugt eine druckbare, einseitige Referenzkarte (Markdown, ggf. in PDF exportierbar) mit den wesentlichen Befehlen, Verifikationsgewohnheiten und dem RDG-Kurzhinweis.

## Beispiel

**Szenario:** Neue Studierende Hofer betritt die Mietrechtsklinik zu Beginn des Wintersemesters. Sie führt `/einarbeitung` aus.

Teil 1: Klinik-Konfiguration wird gelesen; Hofer erfährt, dass die Klinik Mietrecht und Verbraucherrecht abdeckt, nicht aber Strafrecht (Verweisung an Rechtsberatungsstelle der Strafrechts-Vertiefung). Supervisorin: Rechtsanwältin Dr. Weber.

Teil 2: Befehlsübersicht. Hofer fragt: „Was macht `/memo`?" → Erklärung: Gutachten-Gerüst nach Gutachtenmethode, kein fertiges Gutachten.

Teil 3, Übung 1: Fiktiver Fall „Frau Erdem — Heizung defekt seit November". Hofer führt `/mandanten-aufnahme` durch, identifiziert Mietminderung (§ 536 BGB) und Mangel (§ 535 BGB) als Fragen. Nachbesprechung: Hofer hätte nach dem Datum der Mängelanzeige fragen sollen.

Übung 2: `/entwurf widerspruch-kuendigung` — Hofer liest den Entwurf kritisch: „Der Entwurf nennt die Frist als 10.05.2026, aber die Kündigung war am 09.04. zugegangen — ich muss die Dreiwochenfrist für Kündigungsschutz prüfen."

Übung 3: `/recherche-start "§ 536 BGB Mietminderung Heizungsausfall"` → Fahrplan mit ungeprüften Normen. Hofer wählt § 536c BGB und erklärt: Prüfung über juris mit Aktualitätsdatum.

Teil 4: Verifikationsgewohnheiten besprochen. Abschluss: `/einarbeitung --karte` aufgerufen.
