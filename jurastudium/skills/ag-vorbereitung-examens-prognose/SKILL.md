---
name: ag-vorbereitung-examens-prognose
description: "AG-Vorbereitung und Cold-Call-Prep für Jurastudium: Anwendungsfall Student wird im naechsten Seminar oder Arbeitsgemeinschaft aufgerufen und muss konkrete Faelle vorbereiten und Fragen des Dozenten antizipieren. BGB-AT, SchuldR, Strafrecht und öffentliches Recht Lösungsschemata, Subsumtion. Prüfraster Fachgebiet bestimmen, Fall-Schwerpunkte herausarbeiten, mögliche Dozentenfragen antizipieren, Schwachpunkte ueberarbeiten. Output Cold-Call-Voorbereitung mit Musterlösung und Argumentationsstruktur. Abgrenzung zu Prüfungsgespraech-AG für laufende AG-Diskussion und zu Examensvorbereitung-Fragen im Jurastudium."
---

# AG/Seminar-Vorbereitung (Cold-Call-Prep)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. In welchem Fachgebiet findet die AG statt: Zivilrecht, Strafrecht, öffentliches Recht?
2. Welches Thema oder welcher Fall steht auf dem AG-Plan?
3. Wie viel Zeit bis zur AG — und welche Vorbereitung ist bisher erfolgt?
4. Gibt es spezifische Fragen oder Schwachpunkte, die besonders geuebt werden sollen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 133, 157 BGB — Auslegung als AG-Dauerthema
- § 280 Abs. 1 BGB — Schadensersatz: Standard-AG-Anspruch
- §§ 32, 34 StGB — Notwehr/Notstand: AG-Klassiker Strafrecht
- §§ 40, 42 VwGO — Rechtsweg und Klagearten: AG-Grundlage öffentliches Recht

## Eingaben

1. **Fall oder Thema** – als Text oder Stichworte
2. **AG-Typ** – Grundstudium / Fortgeschrittenenübung / Examens-AG / Seminar
3. **Lernprofil** (`~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`) → Fachsemester, Schwächen, Lernstil
4. Optional: **bisherige Musterlösung** oder eigene Antwort zur Besprechung

## Ablauf

### Schritt 1: Fallanalyse

Das Plugin analysiert den vorliegenden Fall / das Thema und:
- Identifiziert die **3–5 klassischen Bohrerpunkte**, an denen ein AG-Leiter einhaken wird
- Bewertet, welche Streitstände für die AG-Besprechung typisch sind
- Markiert Punkte, die erfahrungsgemäß unterschätzt werden

### Schritt 2: Simuliertes Aufrufen

Das Plugin nimmt die Rolle des AG-Leiters ein und **bohrt dich**:

> "Du bist A und behauptest einen Anspruch auf Rückzahlung. Welche Anspruchsgrundlage prüfst du zuerst, und warum nicht § 812 BGB?"

Es gibt nicht die Antwort. Es wartet auf deine Antwort und hakt nach.

Typische AG-Leiter-Fragen, die das Plugin simuliert:
- "Was ist der Obersatz?"
- "Wie definierst du [Tatbestandsmerkmal]?"
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- "Was ist die Mindermeinung, und warum folgt die h.M. nicht ihr?"
- "Kannst du den Unterschied zwischen § 280 Abs. 1 und § 280 Abs. 3 BGB erklären?"
- "Was ändert sich, wenn [Sachverhaltsmodifikation]?"

Im **Drill-Modus**: Das Plugin stellt die Fragen, ohne Hinweise zu geben.
Im **Erklärungs-Modus**: Das Plugin gibt nach der Frage einen Kontext-Hinweis.

### Schritt 3: Sachverhaltsmodifikationen

Nach der Grundbesprechung gibt das Plugin typische AG-Variationen:
- "Was ändert sich, wenn A weiß, dass B ein Minderjähriger ist?"
- "Wie wäre es, wenn A die Frist nicht gesetzt hätte?"
- "Gilt das auch, wenn es sich um Dienst- statt Kaufvertrag handelt?"

### Schritt 4: Zusammenfassung

Nach der Simulationssitzung:
- Liste der beantworteten und offenen Fragen
- Schwachstellen mit gezielten Verweisen (Norm, Kommentar, Lernplan)
- Empfehlung, welche Abschnitte vor der AG nochmals durchzuarbeiten sind

## Quellen und Zitierweise

→ `../references/zitierweise.md`

In der AG wird das **mündliche Zitieren** erwartet – kein vollständiges Literaturverzeichnis, aber:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BGH nennen: "Der BGH hat in der Entscheidung NJW [Jahr], [Seite] entschieden, dass …"
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Quellen in AGs:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispiel

**Fall:** A und B schließen einen Kaufvertrag über ein Notebook (800 €). Das Notebook ist bei Übergabe defekt (Bildschirm flimmert). B verlangt Nacherfüllung. A verweigert. B setzt eine Frist von 14 Tagen, die fruchtlos verstreicht.

**AG-Vorbereitung:**

Schwerpunktnormen: §§ 433, 434, 437, 439, 280, 281 BGB

Die 5 wahrscheinlichsten AG-Fragen:
1. "Was ist der Obersatz für den Schadensersatzanspruch?" → §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB
2. "Wann liegt ein Sachmangel vor?" → § 434 Abs. 1 BGB
3. "War die Fristsetzung wirksam?" → § 281 Abs. 1 S. 1 BGB; Frist muss angemessen sein
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. "Wie verhält sich § 280 Abs. 1 BGB zu §§ 280 Abs. 3, 281 BGB?" → Abgrenzung einfacher Schadensersatz und Schadensersatz statt der Leistung

**Simulierte AG-Frage:**
"Wir sind bei dem Schadensersatzanspruch. Du sagst, § 437 Nr. 3 BGB. Gut. Aber was ist mit dem Vertretenmüssen? Hat B das zu beweisen, oder A?"

*[Deine Antwort]*

Nachbohren: "Und wenn A beweist, dass der Defekt durch unsachgemäße Behandlung nach Übergabe entstanden ist – was passiert dann mit § 477 BGB?"

## Risiken / typische Fehler

- **Unpräziser Obersatz:** In der AG erwartet der Dozent den hypothetisch formulierten Obersatz, nicht eine Zusammenfassung des Sachverhalts.
- **Streitstände nicht kennen:** AG-Leiter bohren gezielt auf bekannte Diskussionspunkte. § 434 BGB n. F. (2022) hat den Mangelbegriff verändert – vor jeder AG auf aktuelle Gesetzeslage prüfen.
- **Sachverhaltsmodifikationen nicht antizipieren:** Fast jede AG endet mit Modifikationsfragen. Diese üben und im Lernprofil protokollieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Defensives Schweigen:** Lieber eine strukturierte Antwort auf falschem Fundament als gar keine Antwort – der AG-Leiter kann nur korrigieren, was er hört.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 242 StGB
- § 35 VwVfG
- § 15 StGB
- § 1 StGB
- § 70 VwG
- Art. 3 GG
- § 32 StGB
- § 16 StGB
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG

### Leitentscheidungen

- BGH VI ZR 116/12

