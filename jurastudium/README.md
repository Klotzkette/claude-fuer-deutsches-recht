# Jurastudium-Plugin

Lernmodus, kein Antwortmodus. Sokratisches Drilling, das *dich* fragt und unpräzises Denken zurückweist. Fallbearbeitung im Gutachtenstil, Lern-Outlines, Karteikarten, Gutachten-Bewertung, AG-/Seminar-Vorbereitung, strukturiertes Feedback auf Hausarbeiten und Seminararbeiten – ohne jemals für dich zu schreiben –, sowie Examensprognose auf Basis vergangener Prüfungen. Kalibriert auf dich: deine Fachsemester, dein Bundesland, dein Prüfungsamt (JPA), ob du gebohrt oder erklärt haben willst.

**Jede Ausgabe ist ein Lerngerüst, kein Mustergutachten. Das Plugin strukturiert dein Denken, bohrt dich sokratisch und zeigt dir, was du falsch hattest. Es schreibt nicht die Gliederung, nicht das Gutachten, nicht die Hausarbeit für dich – das würde den Lernzweck unterlaufen. Zitate in Lernmaterialien sind als zu prüfend markiert.**

## Für wen ist das

Jurastudierende ab dem 1. Semester bis zum 2. Staatsexamen:  
- **Studium (Grundstudium + Schwerpunkt):** große BGB-Übungen, kleine BGB-Übungen, Anfänger- und Fortgeschrittenenübungen, Klausuren und Hausarbeiten in allen Pflicht- und Wahlfächern.  
- **Erstes Juristisches Staatsexamen (Erste Juristische Prüfung / FJP):** schriftliche Klausuren und mündliche Prüfung nach der jeweiligen JAG (Juristenausbildungsgesetz der Länder).  
- **Referendariat und Zweites Staatsexamen:** Anwaltsklausur, Aktenvortrag, Pflichtstation-Klausuren (Zivilrecht, Strafrecht, Verwaltungsrecht, Arbeitsrecht, Wahlstation).  

## Erster Start: cold-start

Dieser Schritt dreht sich um dich: Fachsemester, Bundesland, JAG-Anforderungen, Lernstil (Drill oder Erklärung). Bringe Material mit: eigene Gliederungen, benotete Klausuren, alte Examsklausuren (vor allem vom eigenen JPA), Seminarunterlagen, Vorlesungsskripte. Zehn bis zwanzig Positionen sind das Ziel; darunter wird das Lernprofil als `WENIG MATERIAL` markiert und nachgelagerte Skills sind dünner.

```
/jurastudium:cold-start-interview
```

## Skills

Jeder Skill wird als `/jurastudium:<skill-name>` aufgerufen.

| Skill | Funktion |
|---|---|
| `/jurastudium:cold-start-interview` | Über-dich-Interview + Materialaufnahme – Fachsemester, Bundesland, JAG, Lernstil, Materialien |
| `/jurastudium:socratic-drill [Rechtsgebiet]` | Sokratisches Drilling – das Plugin fragt, du antwortest, es hakt nach. Gibt keine Antwort vor. |
| `/jurastudium:case-brief [Sachverhalt/Fall]` | Fallbearbeitung im Gutachtenstil (Obersatz – Definition – Subsumtion – Ergebnis) |
| `/jurastudium:outline-builder [Rechtsgebiet]` | Lern-Outline / Strukturen pro Rechtsgebiet aufbauen oder erweitern |
| `/jurastudium:bar-prep-questions [Rechtsgebiet]` | Examensvorbereitungs-Fragen für 1. und 2. StEx, Bundesland-spezifisch nach JAG; kennzeichnet h.M. vs. Mindermeinung |
| `/jurastudium:flashcards [Rechtsgebiet]` | Karteikarten generieren oder abfragen; Leitner-Stapel; fachgebietsweise Markdown; `--session <n>`-Modus |
| `/jurastudium:study-plan` | Langfristigen Lernplan erstellen oder anpassen – Phasen, Schwächefächer, adaptiver Tagesplan aus Sitzungshistorie |
| `/jurastudium:session <Rechtsgebiet> <n>` | Fokussierte N-Fragen-Sitzung zu einem Rechtsgebiet; aktualisiert den Lernplan mit Ergebnissen |
| `/jurastudium:gutachten-uebung` | Gutachten bewerten – Aufbau, Obersatz, Subsumtion, Ergebnis, Zitierweise. Protokolliert Muster über Sitzungen. Schreibt nie um. |
| `/jurastudium:cold-call-prep [Fall/Thema]` | AG-/Seminar-Vorbereitung – Professorenfragen vorhersagen und einüben |
| `/jurastudium:legal-writing [Pfad oder Text]` | Strukturfeedback auf jeden Entwurf – schreibt nie um, nie |
| `/jurastudium:exam-forecast [Fach/Kurs]` | Vergangene Examsklausuren analysieren; Prognose für die nächste Prüfung; JPA-Statistik |

## Was „Lernmodus" bedeutet

Mehrere Skills (socratic-drill, case-brief im Drill-Modus, cold-call-prep, gutachten-uebung, legal-writing) sind bewusst so gebaut, dass sie dir die Antwort **nicht geben** und das Gutachten **nicht für dich schreiben**. Der Zweck ist, dass du durch eigenes Tun lernst. Wenn du eine fertige Antwort oder einen Entwurf willst, nimm ein anderes Tool. Dieses Plugin ist für den Kampf.

**legal-writing ist der strengste Skill.** Er liest deinen Entwurf und sagt dir, was schwach ist, schreibt aber nicht um. Die Bitte umzuschreiben wird mit einer höflichen Ablehnung und einem Angebot für gezieltes Strukturfeedback beantwortet. Das ist ein Feature, kein Fehler.

**outline-builder und case-brief folgen derselben Regel in weicherer Form.** outline-builder liefert Gerüste – Themenbaum, Unterthemenslots, Normplatzhalter – und stellt sokratische Fragen, während du die Regeln aus deinen eigenen Mitschriften füllst. Er generiert keine bevölkerte Gliederung aus einem Vorlesungsplan allein. case-brief funktioniert genauso: der Skill gibt die Vorlage vor und hakt nach, was du geschrieben hast; er briefed den Fall nicht für dich.

## Gutachtenstil als Pflichtstandard

Alle Gutachten, Fallbearbeitungen und Übungsklausuren folgen dem deutschen **Gutachtenstil**:

1. **Obersatz** – Benennung der möglichen Rechtsfolge als Hypothese (z. B. „A könnte gegen B einen Anspruch auf Schadensersatz gemäß § 280 Abs. 1 BGB haben.")
2. **Definition** – Abstrakte Tatbestandsmerkmale der Norm (ggf. mit Zitat aus Kommentar oder Lehrbuch)
3. **Subsumtion** – Anwendung der Definition auf den konkreten Sachverhalt
4. **Ergebnis** – Bejahung oder Verneinung der Rechtsfolge

**IRAC ist die US-amerikanische Form** dieses Schemas (Issue – Rule – Application – Conclusion) und hat im deutschen Jurastudium keine eigenständige Bedeutung. Das Plugin verwendet ausschließlich das deutsche Schema.

## Kommentare und Aufsätze zitieren – warum es im Examen entscheidend ist

Im deutschen Recht sind Kommentare und Aufsätze argumentativ **tragend**, nicht nur ergänzend. Im Ersten Juristischen Staatsexamen und in Hausarbeiten ist das Zitieren relevanter Literatur ein eigenständiges Bewertungskriterium:

**Standardkommentare:**
- Grüneberg (hrsg.), *Bürgerliches Gesetzbuch*, 84. Aufl. 2025 (zit. *Grüneberg/Bearbeiter*)
- Säcker/Rixecker/Oetker/Limperg (hrsg.), *Münchener Kommentar zum BGB* (MüKo), 9. Aufl. 2021 ff. (zit. *Bearbeiter, in: MüKoBGB, § X Rn. Y*)
- BeckOK BGB, hrsg. v. Hau/Poseck (zit. *Bearbeiter, in: BeckOK BGB, Ed., § X Rn. Y*)
- Staudinger, *Kommentar zum BGB* (zit. *Bearbeiter, in: Staudinger, BGB, § X Rn. Y*)
- Soergel, Erman, NK-BGB je nach Fachgebiet

**Ausbildungszeitschriften (für Studium und Examen besonders relevant):**
- NJW (Neue Juristische Wochenschrift) – Leitentscheidungen mit Anmerkungen
- JuS (Juristische Schulung) – studienbegleitende Aufsätze und Fälle
- JURA – ausbildungsorientiert
- RÜ (Repetitorium Examensfälle, Beck) – Examensfallbesprechungen
- ZJS (Zeitschrift für das Juristische Studium) – open access, examensrelevant

**Lehrbücher (zitierbar als Sekundärquelle):**
- Medicus/Petersen, *Bürgerliches Recht*, 27. Aufl. 2019 (Schuldrecht/Sachenrecht)
- Brox/Walker, *Allgemeines Schuldrecht*, 47. Aufl. 2023; *Besonderes Schuldrecht*, 47. Aufl. 2023
- Wertenbruch, *BGB Allgemeiner Teil*, 5. Aufl. 2023
- Roth, *Sachenrecht*, je nach Auflage
- Hippel, *Einführung in die Jurisprudenz*, aktuellste Aufl.
- Wandtke/Bullinger, *Praxiskommentar zum Urheberrecht*, 6. Aufl. 2022 (für UrhR-Schwerpunkte)

Zitierregeln: → `../references/zitierweise.md`

## Akademische Integrität

Bevor du dieses Plugin für benotete Arbeiten verwendest – Hausarbeiten, Seminararbeiten, Take-Home-Klausuren –, prüfe die Prüfungsordnung deines Fachbereichs und die Vorgaben deines Prüfers zur KI-Nutzung. Viele Hochschulen verbieten oder beschränken den KI-Einsatz bei benoteten Leistungen. Das Plugin ist für Übung und Vorbereitung gedacht; es dort einzusetzen, wo deine Hochschule es verbietet, verstößt gegen die Prüfungsordnung – und die Konsequenzen trägst du, nicht das Tool.

## Konfidenzmarkierungen

Inhaltlich erzeugende Skills kennzeichnen ihre Konfidenz inline:

- `[PRÜFEN: Aussage – Quelle checken]` – wahrscheinlich korrekt, vor dem Examen aber gegen Kommentar, Lehrbuch oder Primärquelle prüfen
- `[UNSICHER: konkreter Grund]` – der Skill ist bei diesem speziellen Punkt nicht sicher (Mindermeinung, Streitstand, unklare JAG-Regelung)
- `[LÜCKE – aus Vorlesungsmitschrift füllen]` – outline-builder-Marker, wo der Skill keine verlässliche Quelle hat
- `[RSPR FEHLT – Norm benannt, aber kein Leitfall]` – outline-builder-Marker
- `[VGL. MITSCHRIFT – Dozentenbetonung hier relevant]` – outline-builder-Marker
- `[AUSNAHME UNKLAR – Ausnahme bekannt, Voraussetzungen offen]` – outline-builder-Marker
- `[UNSICHER – Prognose]` – exam-forecast-Marker: eine Einschätzung für die Lernzeitgewichtung, keine Vorhersage

## Speicherung

Dein Lernprofil liegt unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` und übersteht Plugin-Updates. Alles Weitere im Arbeitsverzeichnis:

```
jurastudium/
├── karteikarten/
│   └── [fach]/karten.md
├── gutachten-sitzungen/
│   └── [name]/
│       ├── [datum]-[thema].md
│       └── tracker.md
├── writing-feedback/
│   └── [name]/
│       ├── [datum]-[aufgabe].md
│       └── tracker.md
└── examensprognosen/
    └── [fach]/
        └── prognose-[JJJJ-MM-TT].md
```

## Wie das Plugin dazulernt

Dein Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` ist nicht statisch – es verbessert sich mit jeder Nutzung. Skills teilen dir mit, wenn eine Ausgabe auf einem Standard basiert, den du anpassen solltest. Du kannst das Setup erneut durchführen, die Datei direkt bearbeiten oder einem Skill sagen, er soll eine neue Position festhalten.

## Hinweise

- Drill-Modus oder Erklärungs-Modus wird beim cold-start festgelegt; du kannst pro Sitzung wechseln.
- Fallbearbeitungen und Gliederungen verwenden **dein** Format. Wenn du eigene Gliederungen hast, weise cold-start darauf hin.
- Examensvorbereitung zielt auf deine Schwächfächer gemäß Lernprofil. Das Plugin kommt immer wieder auf sie zurück.
- Jeder inhaltlich erzeugende Skill markiert Unsicherheiten. Vertrau den Markierungen mehr als ihrer Abwesenheit – eine unmarkierte Regelaussage ist etwas, woran der Skill sicher ist; prüfe trotzdem deine Quelle vor dem Examen.
