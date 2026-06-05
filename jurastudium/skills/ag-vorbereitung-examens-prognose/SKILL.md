---
name: ag-vorbereitung-examens-prognose
description: "AG Vorbereitung Examens Prognose: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# AG Vorbereitung Examens Prognose

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **AG Vorbereitung Examens Prognose** im Plugin Jurastudium (Klausur, AG, Examen). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ag-vorbereitung` | AG-Vorbereitung und Cold-Call-Prep für Jurastudium: Anwendungsfall Student wird im naechsten Seminar oder Arbeitsgemeinschaft aufgerufen und muss konkrete Faelle vorbereiten und Fragen des Dozenten antizipieren. BGB-AT, SchuldR, Strafrecht und öffentliches Recht Lösungsschemata, Subsumtion. Prüfraster Fachgebiet bestimmen, Fall-Schwerpunkte herausarbeiten, mögliche Dozentenfragen antizipieren, Schwachpunkte ueberarbeiten. Output Cold-Call-Voorbereitung mit Musterlösung und Argumentationsstruktur. Abgrenzung zu Prüfungsgespraech-AG für laufende AG-Diskussion und zu Examensvorbereitung-Fragen. |
| `examens-prognose` | Examensprognose auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken: Anwendungsfall Student will Lernzeit auf wahrscheinliche Themen konzentrieren und fragt welche Schwerpunkte das Justizprüfungsamt bisher prüfte. Examensvorbereitung 1. und 2. Staatsexamen, JAG Bundesland, BMJV-Statistiken. Prüfraster vergangene JPA-Klausuren analysieren, Häufigkeits-Statistik erstellen, Schwerpunktbereiche gewichten, Prognose mit Konfidenz versehen. Output gewichtete Themenliste mit Lernprioritaet und Trefferwahrscheinlichkeit je Rechtsgebiet. Abgrenzung zu Examensvorbereitung-Fragen für Uebungsklausuren und zu Lernplan. |
| `examensvorbereitung-fragen` | Examensvorbereitungs-Fragen für 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland Bayern NRW Hamburg, Subsumtion Gutachtenstil. Prüfraster Fachgebiet Zivilrecht Strafrecht öffentliches Recht, Zeitdruck-Simulation oder Verstaendnis-Training, Bundesland-spezifisch. Output Uebungsfragen mit Musterlösung und Hinweis auf Schwachstellen. Abgrenzung zu Examensprognose für Themengewichtung und zu Gutachten-Uebung für Klausur-Training. |

## Arbeitsweg

Im Plugin Jurastudium (Klausur, AG, Examen) gilt für **AG Vorbereitung Examens Prognose**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ag-vorbereitung`

**Fokus:** AG-Vorbereitung und Cold-Call-Prep für Jurastudium: Anwendungsfall Student wird im naechsten Seminar oder Arbeitsgemeinschaft aufgerufen und muss konkrete Faelle vorbereiten und Fragen des Dozenten antizipieren. BGB-AT, SchuldR, Strafrecht und öffentliches Recht Lösungsschemata, Subsumtion. Prüfraster Fachgebiet bestimmen, Fall-Schwerpunkte herausarbeiten, mögliche Dozentenfragen antizipieren, Schwachpunkte ueberarbeiten. Output Cold-Call-Voorbereitung mit Musterlösung und Argumentationsstruktur. Abgrenzung zu Prüfungsgespraech-AG für laufende AG-Diskussion und zu Examensvorbereitung-Fragen.

# AG/Seminar-Vorbereitung (Cold-Call-Prep)


## Triage zu Beginn
1. In welchem Fachgebiet findet die AG statt: Zivilrecht, Strafrecht, oeffentliches Recht?
2. Welches Thema oder welcher Fall steht auf dem AG-Plan?
3. Wie viel Zeit bis zur AG — und welche Vorbereitung ist bisher erfolgt?
4. Gibt es spezifische Fragen oder Schwachpunkte, die besonders geuebt werden sollen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 133, 157 BGB — Auslegung als AG-Dauerthema
- § 280 Abs. 1 BGB — Schadensersatz: Standard-AG-Anspruch
- §§ 32, 34 StGB — Notwehr/Notstand: AG-Klassiker Strafrecht
- §§ 40, 42 VwGO — Rechtsweg und Klagearten: AG-Grundlage oeffentliches Recht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill bereitet dich auf das **Aufrufen in der Arbeitsgemeinschaft (AG)** oder im **Seminar** vor. Die AG ist im deutschen Jurastudium ein zentrales Lernformat: ein Dozent (oft Referendar oder wissenschaftlicher Mitarbeiter) bespricht Übungsfälle mit kleinen Gruppen von Studierenden. Wer nicht vorbereitet ist, verliert wertvolle Übungszeit.

Schwerpunkte:
- Fallbesprechungs-AGs im Grundstudium (BGB, StGB, ÖffR)
- Übungsklausur-AGs in der Examensvorbereitung
- Seminargespräche mit sokratischen Dozentenbohrern
- Lehrveranstaltungen, in denen aktive Teilnahme benotet wird (Große Übung, BGB-Übung)

Das Plugin sagt **nicht**, was der Dozent fragen wird – es bohrt die Fragen, die ein erfahrener AG-Leiter wahrscheinlich stellen wird, und lässt dich antworten.

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

## Ausgabeformat

### AG-Vorbereitung (Steckbrief)

```
**Fall / Thema:** [Kurzzusammenfassung]
**AG-Typ:** [Grundstudium / Fortgeschrittene / Examens-AG]
**Schwerpunktnormen:** [§§]
**Kernstreitstand:** [1–2 Sätze]

**Die 5 wahrscheinlichsten AG-Fragen:**
1. [Frage] → [Hinweis auf relevanten Kommentarabschnitt]
2. [Frage] → [Normbezug]
3. [Frage] → [Streitstand mit Belegen]
4. [Frage] → [Sachverhaltsmodifikation]
5. [Frage] → [Vertiefungsfrage]

**Sachverhaltsmodifikationen:**
- Was ändert sich, wenn …?
- Wie ist es, wenn …?

**Vorbereiten bis:** [gezielte Seiten/Randnummern aus dem Kommentar]
```

### Simulierte AG-Sitzung

```
[AG-Leiter-Modus]
Frage: "[Konkrete Frage im AG-Stil]"

[Nutzerantwort]

Nachbohren: "[Präzisierungsfrage oder Sachverhaltsmodifikation]"
```

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

## 2. `examens-prognose`

**Fokus:** Examensprognose auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken: Anwendungsfall Student will Lernzeit auf wahrscheinliche Themen konzentrieren und fragt welche Schwerpunkte das Justizprüfungsamt bisher prüfte. Examensvorbereitung 1. und 2. Staatsexamen, JAG Bundesland, BMJV-Statistiken. Prüfraster vergangene JPA-Klausuren analysieren, Häufigkeits-Statistik erstellen, Schwerpunktbereiche gewichten, Prognose mit Konfidenz versehen. Output gewichtete Themenliste mit Lernprioritaet und Trefferwahrscheinlichkeit je Rechtsgebiet. Abgrenzung zu Examensvorbereitung-Fragen für Uebungsklausuren und zu Lernplan.

# Examensprognose / JPA-Statistik

## Zweck

Dieser Skill analysiert **vergangene Examsklausuren** desselben Justizprüfungsamts (JPA) und erstellt eine **gewichtete Prognose** für kommende Prüfungen. Er hilft dabei, Lernzeit auf examensrelevante Themen zu konzentrieren, statt gleichmäßig über alle Rechtsgebiete zu verteilen.

Grundlage:
- Vom Nutzer hochgeladene **JPA-Klausuren** aus dem Lernprofil
- Öffentlich bekannte **Statistiken des BMJV** (Bundesministerium der Justiz) zur Bestehensquote und Fächerverteilung
- **JPA-spezifische Schwerpunkte** (bekannte Präferenzen einzelner Prüfungsämter)
- **Aktuelle Rechtsentwicklungen** (z. B. BGB-Reformen, neue BGH-Leitentscheidungen)

**Wichtiger Vorbehalt:** Eine Prognose ist eine Gewichtungshilfe für die Lernzeitplanung, keine Vorhersage. Alle Prognosepunkte werden mit `[UNSICHER – Prognose]` markiert.

## Eingaben

1. Lernprofil (`~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`) → Bundesland/JPA, Prüfungsziel, hochgeladene Klausuren
2. Optional: Pfad zu spezifischen Altklausuren (selbes JPA oder vergleichbares JPA)
3. Optional: `--statistik` → zeigt BMJV-Statistiken und bekannte Bundesland-Daten
4. Rechtsgebiet (Argument oder interaktiv)

## Ablauf

### Schritt 1: Materialprüfung

Das Plugin prüft, welche JPA-Klausuren vorliegen:
- Weniger als 5 Klausuren vom selben JPA → Ausgabe mit `WENIG MATERIAL`-Hinweis
- Klausuren von einem anderen JPA desselben Bundeslandes → verwendbar, aber mit Hinweis
- Keine eigenen Klausuren → reine BMJV-Statistik und bekannte Muster, stark generisch

### Schritt 2: Klausuranalyse

Für jede vorliegende Klausur:
- Welches Rechtsgebiet? Welche Normen stehen im Mittelpunkt?
- Welcher Aufbautyp (Anspruchsgrundlagenprüfung / Straftatprüfung / Verwaltungsakt)?
- Welche Streitstände wurden abgefragt?
- Wiederholungsmuster: Was kam in 2 oder mehr Klausuren vor?

### Schritt 3: Gewichtungsmatrix

Das Plugin erstellt eine gewichtete Themenmatrix:

| Thema | Häufigkeit (eigene Klausuren) | BMJV-Relevanz | Letzte Prüfung | Gewicht |
|---|---|---|---|---|
| § 280 Abs. 1 BGB – Schadensersatz | hoch | hoch | 2023 | ⬆⬆ |
| § 823 Abs. 1 BGB – Deliktsrecht | mittel | hoch | 2022 | ⬆ |
| § 812 BGB – Bereicherungsrecht | niedrig | mittel | 2021 | ↔ |
| § 985 BGB – Herausgabeanspruch | niedrig | niedrig | 2020 | ⬇ |

`[UNSICHER – Prognose]` auf alle Gewichtungen.

### Schritt 4: Aktuelle Rechtsentwicklungen

Das Plugin prüft bekannte aktuelle Themen:
- **BGB-Reform 2022** (Sachmangelbegriff § 434, Verbrauchsgüterkauf): examensrelevant seit 2022/2023
- **DSA/DDG:** relevant in Medien- und IT-rechtlichen Schwerpunkten
- **BGH-Leitentscheidungen** der letzten 2 Jahre im jeweiligen Rechtsgebiet

Alle aktuellen Angaben: `[Modellwissen – prüfen; Stand des Trainings kann veraltet sein]`

### Schritt 5: Lernempfehlung

Auf Basis der Gewichtungsmatrix:
- **Priorität A:** Themen mit hoher Häufigkeit + hoher BMJV-Relevanz → höchste Lernzeit
- **Priorität B:** Mittel-Häufigkeit + aktuelle BGH-Relevanz → zweite Lernphase
- **Priorität C:** Selten + bereits gut beherrscht → nur Auffrischung nötig

## Quellen und Zitierweise

→ `../references/zitierweise.md`

**Für Prognosearbeit relevante Quellen:**
- BMJV, *Statistik der Rechtspflege* (jährlich, online), Bestehensquoten und Fächerverteilung
- NJW: jährliche Examensbesprechungen und Berichte zu Schwerpunktthemen
- JuS: regelmäßige Aufsätze zu examensrelevanten Problemkreisen
- RÜ (Repetitorium – Examensfälle): aktuelle Fallbesprechungen aus echten Examensklausuren

**Für Bundesland-spezifische Daten:**
- JPA-Websites (Bayern: www.justizexamen.de; NRW: www.jpa.nrw.de; BW: www.justiz.bwl.de)
- Öffentlich zugängliche Klausurensammlungen der Universitäten

**Für inhaltliche Kontrolle:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

### Examensprognose (Vollformat)

```
**Examensprognose – [Rechtsgebiet] – [Bundesland] / JPA [X]**
Stand: [Datum der Analyse]

⚠️ Hinweis: Diese Prognose ist eine Lernzeit-Gewichtungshilfe, keine Vorhersage.
Alle Punkte mit [UNSICHER – Prognose] markiert.

**Datenbasis:**
- [N] eigene JPA-Klausuren analysiert [WENIG MATERIAL falls <5]
- BMJV-Statistik [Jahr]
- Bekannte JPA-Präferenzen [Bundesland]

**Gewichtungsmatrix:**
[Tabelle]

**Priorität A – Schwerpunkt Lernzeit:**
1. [Thema]: [Begründung] [UNSICHER – Prognose]
2. [Thema]: …

**Priorität B – Zweite Lernphase:**
[…]

**Aktuelle Rechtsentwicklungen die du kennen solltest:**
- [Thema]: [Kurzbeschreibung] [Modellwissen – prüfen]

**Verknüpfte Skills:**
→ /jurastudium:lernplan (Prognose in Lernplan übertragen)
→ /jurastudium:examensvorbereitung-fragen --bundesland [X] [Rechtsgebiet]
```

## Beispiel

**Anfrage:** Examensprognose BGB Schuldrecht, Bayern, basierend auf 7 JPA-Klausuren

**Ausgabe (Auszug):**

Gewichtungsmatrix (Auszug):

| Thema | Klausur-Häufigkeit | BMJV-Relevanz | Gewicht |
|---|---|---|---|
| Leistungsstörungen §§ 280, 281, 323 BGB | 6/7 | sehr hoch | ⬆⬆ `[UNSICHER – Prognose]` |
| Kaufrecht §§ 433, 434, 437 BGB n. F. | 5/7 | hoch (seit Reform 2022) | ⬆⬆ |
| Deliktsrecht § 823 BGB | 4/7 | hoch | ⬆ |
| Stellvertretung §§ 164 ff. BGB | 3/7 | mittel | ↔ |
| Bereicherungsrecht §§ 812 ff. BGB | 2/7 | mittel | ↔ |

Priorität A: Leistungsstörungsrecht – kommt in fast jeder BGB-Klausur vor. Fokus auf §§ 280 Abs. 1, 3, 281 BGB; Fristlosigkeit § 323 Abs. 2 BGB; Rücktritt vs. Schadensersatz. lizenzpflichtige Literaturquelle/Ernst, §§ 280, 281 beherrschen. `[UNSICHER – Prognose]`

Aktuelle Rechtsentwicklungen:
BGB-Reform 2022 (VerbrRRL): Neuer § 434 BGB – subjektiver, objektiver und montagebezogener Mangelbegriff. In Bayern erstmals in Klausuren ab Frühjahr 2023 abgefragt. `[Modellwissen – prüfen]`

## Risiken / typische Fehler

- **Prognose als Gewissheit behandeln:** `[UNSICHER – Prognose]` ist kein Disclaimer-Floskeln, sondern echter Vorbehalt. JPAs können spontan Schwerpunkte wechseln.
- **Altklausuren von anderem JPA als gleichwertig behandeln:** Zwischen NRW-JPA Düsseldorf und Bayern bestehen erhebliche Unterschiede im Klausurstil (NRW: sehr langer Sachverhalt; Bayern: kompakter mit vielen Prüfungspunkten).
- **Aktualitätslücken:** BGH-Entscheidungen der letzten 12 Monate sind im Modell möglicherweise nicht vollständig. Vor dem Examen: NJW und JuS der letzten zwei Hefte prüfen.
- **Nur Priorität-A-Themen lernen:** Examsklausuren enthalten bewusst seltene Normen als Differenzierungspunkte. Priorität-C-Themen nicht weglassen.
- **BMJV-Statistik fehlinterpretieren:** Bestehensquoten sagen nichts über Themenverteilung aus. Nur Klausuranalyse ergibt Themengewichtung.

## 3. `examensvorbereitung-fragen`

**Fokus:** Examensvorbereitungs-Fragen für 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland Bayern NRW Hamburg, Subsumtion Gutachtenstil. Prüfraster Fachgebiet Zivilrecht Strafrecht öffentliches Recht, Zeitdruck-Simulation oder Verstaendnis-Training, Bundesland-spezifisch. Output Uebungsfragen mit Musterlösung und Hinweis auf Schwachstellen. Abgrenzung zu Examensprognose für Themengewichtung und zu Gutachten-Uebung für Klausur-Training.

# Examensvorbereitungs-Fragen


## Triage zu Beginn
1. Welches Examen und welches Bundesland (1. StEx, 2. StEx; Bayern, NRW, Hamburg)?
2. Welches Fachgebiet soll geuebt werden (Zivilrecht, Strafrecht, oeffentliches Recht, Verfahrensrecht)?
3. Zeitdruck-Simulation oder inhaltliches Verstaendnis-Training?
4. Welche Schwachpunkte wurden in frueheren Uebungsklausuren identifiziert?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- §§ 13, 14 JAG NRW — Examensklausuren: Inhaltsanforderungen und Bewertungsmassstab (exemplarisch fuer alle Bundeslaender)
- § 195 BGB — Regelverjaehrung: Dauerklassiker in Zivilrecht-Klausuren
- § 1 Abs. 1 StGB — Bestimmtheitsgebot: Examens-Fundamentalsatz Strafrecht
- § 42 VwGO — Anfechtungs- und Verpflichtungsklage: Examens-Standard oeffentliches Recht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill generiert Übungsfragen und -klausuren für das **Erste Juristische Staatsexamen (Erste Juristische Prüfung / FJP)** sowie das **Zweite Juristische Staatsexamen (Assessorexamen)**. Er berücksichtigt:

- das jeweilige **Bundesland** und seine **JAG** (Juristenausbildungsgesetz)
- die **Prüfungsgebiete** des zuständigen **Justizprüfungsamts (JPA)**
- aktuelle **Schwerpunkte** aus JPA-Statistiken und bekannten Examensklausuren
- das individuelle **Schwächeprofil** aus dem Lernprofil

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Eingaben

1. Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` → Bundesland, JAG, Schwächefächer, Lernstil
2. Optional: `lernplan.yaml` – zeigt, welches Fach heute auf dem Plan steht und welche Teilgebiete noch schwach sind
3. Rechtsgebiet (Argument oder interaktiv erfragen)
4. Prüfungstyp: `--schriftlich` (Klausur, 5h) oder `--mündlich` (Aktenvortrag, AG-Fragen)

## Ablauf

### 1. Prüfungstyp-Gate (nicht überspringen)

Falls Bundesland/JAG oder Prüfungstyp nicht im Profil vorhanden sind, **vor der Fragengenerierung fragen**:

- "In welchem Bundesland legst du das Examen ab?"
- "1. oder 2. Staatsexamen?"
- "Schriftlich oder mündlich?"

Falsche Annahmen beim JAG-Rahmen sind der Fehler, der sich nicht aufholen lässt.

### 2. JAG-Prüfungsgebiet-Gate

Falls das Rechtsgebiet außerhalb des JAG-Prüfungsstoffs liegt oder es eine bundeslandspezifische Besonderheit gibt:

> "In [Bundesland] enthält die JAG folgende schriftliche Prüfungsfächer: [Liste]. [Rechtsgebiet] ist [enthalten / nicht enthalten / Pflicht-/Wahlstation]. Soll ich trotzdem fortfahren?"

### 3. Fragengenerierung

- Fragen gewichtet nach **Schwächeprofil** aus dem Lernprofil
- **Examenstypische Sachverhalte** (Falllösung, nicht Theoriefragen): kurze Sachverhalte mit mehreren Anspruchsgrundlagen, Streitständen und bewusstem Ablenkungspotenzial
- **Schwierigkeitsmarkierung:** `[Grundniveau]` / `[Examensniveau]` / `[Schwerpunkt]`
- **JAG-Markierung:** kennzeichnet, ob eine Regel bundeseinheitlich oder länderspezifisch ist

### 4. Auswertung

Nach jeder Antwort:
1. Struktur prüfen: War der Obersatz klar hypothetisch formuliert? Wurde die Definition zitiert?
2. Subsumtion prüfen: Wurden alle Tatbestandsmerkmale geprüft?
3. Streitstände: Wurden h.M. und Mindermeinung mit Belegen genannt?
4. Zitierweise: Entsprechen die Literaturzitate dem Standard aus `../references/zitierweise.md`?
5. Ergebnis festhalten, Muster in Fehlern protokollieren

`--session <n>` läuft N Fragen durch und schreibt anschließend eine Zusammenfassung der Fehlermuster.

## Quellen und Zitierweise

→ `../references/zitierweise.md` (maßgeblich für alle Zitate)

**Quellenregel je Rechtsgebiet:**

| Rechtsgebiet | Standardkommentar |
|---|---|
| BGB AT / Schuldrecht | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| Sachenrecht | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| BGB Allgemein | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| Handelsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| Gesellschaftsrecht | Normtext, Register-/Gesetzesquellen, bereitgestellte Materialien |
| ZPO | Normtext, amtliche Hinweise, verifizierte Rechtsprechung |
| StGB | Normtext, verifizierte Rechtsprechung, bereitgestellte Materialien |
| Verwaltungsrecht | Normtext, amtliche Materialien, verifizierte Rechtsprechung |

**Ausbildungszeitschriften:**
Nur verwenden, wenn der Nutzer den konkreten Aufsatz bereitstellt oder ein lizenzierter Live-Zugriff die Fundstelle verifiziert.

## Ausgabeformat

### Sachverhalts-Aufgabe (Klausurstil)

```
**Sachverhalt:**
[3–8 Sätze, examenstypische Verdichtung mit Ablenkungsmanövern]

**Aufgabe:**
Prüfe alle in Betracht kommenden Ansprüche des A gegen B.
[Bundesland: Bayern / JAG-Prüfungsgebiet: Schuldrecht / Niveau: Examensniveau]
```

### Musterlösung (nach Nutzerantwort)

```
**Lösungsskizze – Gutachtenstil**

A. Ansprüche des A gegen B

I. Anspruch aus § 433 Abs. 2 BGB
 Obersatz: A könnte gegen B einen Anspruch auf Kaufpreiszahlung
 gemäß § 433 Abs. 2 BGB haben.
 Voraussetzungen: wirksamer Kaufvertrag, Fälligkeit, kein Einrederecht.
 Definition Kaufvertrag: …
 Subsumtion: …
 Ergebnis: Der Anspruch besteht / besteht nicht.

II. Anspruch aus § 280 Abs. 1 BGB
 Obersatz: …

**Literaturnachweise:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Deine Lücken diese Sitzung:** [Protokoll]
```

## Beispiel

**Sachverhalt:** Verkäufer V verkauft Käufer K sein gebrauchtes Fahrrad für 300 €. K überweist den Betrag, V liefert das Rad jedoch nicht. K setzt V eine Frist von 10 Tagen. V lässt die Frist verstreichen.

**Aufgabe:** Prüfe alle Ansprüche des K gegen V.

**Musterlösung (Auszug):**

*I. Anspruch des K gegen V auf Übereignung und Übergabe des Fahrrads gemäß §§ 433 Abs. 1 S. 1, 929 S. 1 BGB*

Obersatz: K könnte gegen V einen Anspruch auf Übereignung und Übergabe des Fahrrads gemäß § 433 Abs. 1 S. 1 BGB haben.

Definition: Ein Kaufvertrag setzt zwei übereinstimmende Willenserklärungen (Angebot und Annahme) voraus, die auf Übertragung des Eigentums gegen Entgeltzahlung gerichtet sind.

Subsumtion: V und K haben sich über Fahrrad und Preis einig, § 433 Abs. 1 S. 1 BGB. Ein Kaufvertrag liegt vor.

Ergebnis: Der Anspruch aus § 433 Abs. 1 S. 1 BGB besteht. Da V nicht geliefert hat, ist der Anspruch nicht erfüllt.

*II. Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB*

Obersatz: K könnte nach fruchtlosem Fristablauf einen Anspruch auf Schadensersatz statt der Leistung gemäß §§ 280 Abs. 1, 3, 281 Abs. 1 BGB haben.

[…] Frist wurde gesetzt und ist abgelaufen, § 281 Abs. 1 S. 1 BGB. Vertretenmüssen wird gemäß § 280 Abs. 1 S. 2 BGB vermutet; V hat sich nicht exkulpiert.

Ergebnis: Der Anspruch auf Schadensersatz statt der Leistung besteht.

*Quellenhinweis:*
Literaturfundstellen nur ergänzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff die Fundstelle verifiziert.

## Risiken / typische Fehler

- **Falscher JAG-Rahmen:** BGB-Inhalte die in einem Bundesland nicht prüfungsrelevant sind, kosten Lernzeit. Bundesland immer zuerst prüfen.
- **Urteilsstil statt Gutachtenstil:** Der Obersatz muss hypothetisch sein. "A hat einen Anspruch" ist Urteilsstil – falsch für Klausuren.
- **h.M. ohne Beleg:** "nach h.M." allein ist kein Argument. Kommentarstelle oder BGH-Urteil nennen.
- **Scheinprobleme ignorieren:** Examsklausuren enthalten bewusste Ablenkungen. Offensichtlich vorliegende Tatbestandsmerkmale kurz abarbeiten, nicht übergehen.
- **Konkurrenzprobleme:** Reihenfolge der Anspruchsgrundlagen (vertraglich vor außervertraglich) beachten – vgl. `../references/methodik-buergerliches-recht.md`.
- **Fehlende Fundstellen im Gutachten:** Im 1. StEx ist das Fehlen von Kommentarzitaten ein Bewertungsminus.
