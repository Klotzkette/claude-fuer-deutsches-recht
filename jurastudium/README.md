# Jurastudium-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung.

Dieses Plugin gehört zum Marketplace mit 315 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`jurastudium.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/jurastudium.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/jurastudium.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/jurastudium-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/jurastudium-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/jurastudium.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Installation](../INSTALLATION_EINFACH.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/jurastudium.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Jurastudium-Plugin:

> Sichte den ausgewählten Ordner intern, ohne seine Inhalte ungefragt aufzulisten. Lies die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: einen fachbezogenen Erststand mit Ergebnisrichtung, Kernbeleg und nächstem Dokument. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage gezielt nach entscheidenden offenen Punkten und arbeite an den unabhängigen Teilen weiter. Verarbeite die Antwort im bestehenden Entwurf; weitere Rückfragen nur bei neuen entscheidenden Lücken.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`jurastudium.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/paketpflege-20261122-v445.36.9/jurastudium.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`jurastudium-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/jurastudium-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`jurastudium-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/jurastudium-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [2 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 315 Plugins. Das Sammelpaket [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) enthält seinen veröffentlichten Stand, nicht zwingend spätere Einzelpakete. Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Examensbegleitung Roosendaal-Tinnefeld — 1. Staatsexamen Bonn, Frühjahr 2027](../testakten/jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027/README.md) | [Gesamt-PDF](../testakten/jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027/gesamt-pdf/jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027_gesamt.pdf) | [`testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027.zip) | [`testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027-einzelpdfs.zip) |
| [Akte Jana Mondsee - Drittversuch, digitale Systeme-Vorwurf und Masterarbeit](../testakten/pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee/README.md) | [Gesamt-PDF](../testakten/pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee/gesamt-pdf/pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee_gesamt.pdf) | [`testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/grundakten-sammlung-v1.0.0/testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee.zip) | [`testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/akten-v445.35.3/testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Lernmodus, kein Antwortmodus. Prüfungsgespräch nach AG-Tradition, das *dich* fragt und unpräzises Denken zurückweist. Fallbearbeitung im Gutachtenstil, Lern-Outlines, Karteikarten, Gutachten-Bewertung, AG-/Seminar-Vorbereitung, strukturiertes Feedback auf Hausarbeiten und Seminararbeiten – ohne jemals für dich zu schreiben –, sowie Examensprognose auf Basis vergangener Prüfungen. Kalibriert auf dich: deine Fachsemester, dein Bundesland, dein Prüfungsamt (JPA), ob du gebohrt oder erklärt haben willst.

**Jede Ausgabe ist ein Lerngerüst, kein Mustergutachten. Das Plugin strukturiert dein Denken, bohrt dich sokratisch und zeigt dir, was du falsch hattest. Es schreibt nicht die Gliederung, nicht das Gutachten, nicht die Hausarbeit für dich – das würde den Lernzweck unterlaufen. Zitate in Lernmaterialien sind als zu prüfend markiert.**

## Für wen ist das

Jurastudierende ab dem 1. Semester bis zum 2. Staatsexamen:
- **Studium (Grundstudium + Schwerpunkt):** große BGB-Übungen, kleine BGB-Übungen, Anfänger- und Fortgeschrittenenübungen, Klausuren und Hausarbeiten in allen Pflicht- und Wahlfächern.
- **Erstes Juristisches Staatsexamen (Erste Juristische Prüfung / FJP):** schriftliche Klausuren und mündliche Prüfung nach der jeweiligen JAG (Juristenausbildungsgesetz der Länder).
- **Referendariat und Zweites Staatsexamen:** Anwaltsklausur, Aktenvortrag, Pflichtstation-Klausuren (Zivilrecht, Strafrecht, Verwaltungsrecht, Arbeitsrecht, Wahlstation).

## Erster Start: Kaltstart

Eine konkrete Lernfrage, dein eigener Lösungsversuch oder eine Klausur genügt zum Start. Das Plugin liest vorhandenes Material und beginnt direkt mit der gewünschten Erklärung, Übung oder Rückmeldung; nur dafür entscheidende Angaben werden nachgefragt. Ein ausführlicheres Lernprofil zu Semester, Bundesland und Lernstil ist optional. Es gibt keine Mindestmenge an Unterlagen. Neue Antworten führen die begonnene Übung weiter, statt erneut ein Aufnahmegespräch auszulösen.

```
/jurastudium:fallfrage-bearbeiten Thema: kaltstart-interview
```

## Skills

Jeder Skill wird als `/jurastudium:<skill-name>` aufgerufen.

| Skill | Funktion |
|---|---|
| `/jurastudium:fallfrage-bearbeiten Thema: kaltstart-interview` | Über-dich-Interview + Materialaufnahme – Fachsemester, Bundesland, JAG, Lernstil, Materialien |
| `/jurastudium:fallfrage-bearbeiten Thema: pruefungsgespraech-ag-rechtsgeschichte [Rechtsgebiet]` | Prüfungsgespräch nach AG-Tradition – das Plugin fragt, du antwortest, es hakt nach. Gibt keine Antwort vor. |
| `/jurastudium:arbeitsprodukt-bearbeiten Thema: fall-zusammenfassung-gliederungs-baukasten [Sachverhalt/Fall]` | Fallbearbeitung im Gutachtenstil (Obersatz – Definition – Subsumtion – Ergebnis) |
| `/jurastudium:fallfrage-bearbeiten Thema: gliederungs-baukasten [Rechtsgebiet]` | Lern-Outline / Strukturen pro Rechtsgebiet aufbauen oder erweitern |
| `/jurastudium:fallfrage-bearbeiten Thema: examensvorbereitung-fragen [Rechtsgebiet]` | Examensvorbereitungs-Fragen für 1. und 2. StEx, Bundesland-spezifisch nach JAG; kennzeichnet h.M. vs. Mindermeinung |
| `/jurastudium:fallfrage-bearbeiten Thema: karteikarten-lernplan-lernsitzung [Rechtsgebiet]` | Karteikarten generieren oder abfragen; Leitner-Stapel; fachgebietsweise Markdown; `--session <n>`-Modus |
| `/jurastudium:fallfrage-bearbeiten Thema: lernplan` | Langfristigen Lernplan erstellen oder anpassen – Phasen, Schwächefächer, adaptiver Tagesplan aus Sitzungshistorie |
| `/jurastudium:fallfrage-bearbeiten Thema: lernsitzung <Rechtsgebiet> <n>` | Fokussierte N-Fragen-Sitzung zu einem Rechtsgebiet; aktualisiert den Lernplan mit Ergebnissen |
| `/jurastudium:arbeitsprodukt-bearbeiten Thema: gutachten-uebung` | Gutachten bewerten – Aufbau, Obersatz, Subsumtion, Ergebnis, Zitierweise. Protokolliert Muster über Sitzungen. Schreibt nie um. |
| `/jurastudium:fallfrage-bearbeiten Thema: ag-vorbereitung-examens-prognose [Fall/Thema]` | AG-/Seminar-Vorbereitung – Professorenfragen vorhersagen und einüben |
| `/jurastudium:subsumtion-bearbeiten Thema: juristisches-schreiben [Pfad oder Text]` | Strukturfeedback auf jeden Entwurf – schreibt nie um, nie |
| `/jurastudium:fallfrage-bearbeiten Thema: examens-prognose [Fach/Kurs]` | Vergangene Examsklausuren analysieren; Prognose für die nächste Prüfung; JPA-Statistik |
| `/jurastudium:subsumtion-bearbeiten Thema: subsumtionslehre [Norm/Sachverhalt]` | Subsumtion als Königsdisziplin üben – Trennung Obersatz/Definition/Subsumtion/Ergebnis, Pushback bei Subsumtionssprüngen, vorweggenommener Würdigung und vermischtem Stil |
| `/jurastudium:fallfrage-bearbeiten Thema: methodenlehre-grundlagen [Norm]` | Vier Auslegungsmethoden (Savigny), Analogie, teleologische Reduktion, verfassungs- und unionsrechtskonforme Auslegung – mit Argumentationslast |
| `/jurastudium:fallfrage-bearbeiten Thema: methodenlehre-zivilrecht [Fall]` | AGL-Reihenfolge, Konkurrenzen, Auslegung von Willenserklärungen (§§ 133, 157 BGB), Auslegung von AGB – Drill-Modus |
| `/jurastudium:fallfrage-bearbeiten Thema: methodenlehre-strafrecht [Sachverhalt]` | Dreistufiger Verbrechensaufbau, Trennung objektiver/subjektiver Tatbestand, Konkurrenzen, Analogieverbot Art. 103 II GG |
| `/jurastudium:fallfrage-bearbeiten Thema: methodenlehre-oeffentliches-strafrecht [Fall]` | Schichtenprüfung der Grundrechte, Verhältnismäßigkeit, Ermessen, VA-Qualität, Klageart, Vorrang des Unionsrechts |
| `/jurastudium:fallfrage-bearbeiten Thema: rechtsgeschichte [Epoche/Thema]` | Fünf historische Linien: römisches Recht und BGB-Genese, NS-Unrechtsjustiz und Radbruchsche Formel, SED-Unrecht und Mauerschützen, GG 1949, Unionsrecht von EGKS bis Lissabon |
| `/jurastudium:fallfrage-bearbeiten Thema: lernstrategien-loesungsschemata-methodenlehre` | Evidenzbasierte Lernmethoden für Jura – aktiver Abruf, Spaced Repetition, Interleaving, Elaboration, Klausurtaktik unter Zeitdruck |
| `/jurastudium:subsumtion-bearbeiten Thema: tatbestaende-lernen [§ / Rechtsgebiet]` | Tatbestände zerlegen, Definitionen abrufbar machen, Streitstände am Merkmal verankern; integriert mit `karteikarten` |
| `/jurastudium:fallfrage-bearbeiten Thema: loesungsschemata [Norm/Rechtsgebiet]` | Klassische Schemata (Anspruchsprüfung, Verbrechensaufbau, Grundrechtsprüfung, EBV, Bereicherung) – mit ehrlichem Disclaimer: nicht dogmatisch zwingend, aber Verständniskatalysator; whatever works |

## Was "Lernmodus" bedeutet

Mehrere Skills (prüfungsgespräch-ag, fall-zusammenfassung im Drill-Modus, ag-vorbereitung, gutachten-übung, juristisches-schreiben, subsumtionslehre, methodenlehre-*, tatbestände-lernen) sind bewusst so gebaut, dass sie dir die Antwort **nicht geben** und das Gutachten **nicht für dich schreiben**. Der Zweck ist, dass du durch eigenes Tun lernst. Wenn du eine fertige Antwort oder einen Entwurf willst, nimm ein anderes Tool. Dieses Plugin ist für den Kampf.

**juristisches-schreiben ist der strengste Skill.** Er liest deinen Entwurf und sagt dir, was schwach ist, schreibt aber nicht um. Die Bitte umzuschreiben wird mit einer höflichen Ablehnung und einem Angebot für gezieltes Strukturfeedback beantwortet. Das ist ein Feature, kein Fehler.

**gliederungs-baukasten und fall-zusammenfassung folgen derselben Regel in weicherer Form.** gliederungs-baukasten liefert Gerüste – Themenbaum, Unterthemenslots, Normplatzhalter – und stellt sokratische Fragen, während du die Regeln aus deinen eigenen Mitschriften füllst. Er generiert keine bevölkerte Gliederung aus einem Vorlesungsplan allein. fall-zusammenfassung funktioniert genauso: der Skill gibt die Vorlage vor und hakt nach, was du geschrieben hast; er briefed den Fall nicht für dich.

## Gutachtenstil als Pflichtstandard

Alle Gutachten, Fallbearbeitungen und Übungsklausuren folgen dem deutschen **Gutachtenstil**:

1. **Obersatz** – Benennung der möglichen Rechtsfolge als Hypothese (z. B. "A könnte gegen B einen Anspruch auf Schadensersatz gemäß § 280 Abs. 1 BGB haben.")
2. **Definition** – Abstrakte Tatbestandsmerkmale der Norm (nur mit bereitgestellter Quelle oder verifizierter Rechtsprechung)
3. **Subsumtion** – Anwendung der Definition auf den konkreten Sachverhalt
4. **Ergebnis** – Bejahung oder Verneinung der Rechtsfolge

**IRAC ist die US-amerikanische Form** dieses Schemas (Issue – Rule – Application – Conclusion) und hat im deutschen Jurastudium keine eigenständige Bedeutung. Das Plugin verwendet ausschließlich das deutsche Schema.

## Quellen sauber nutzen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

**Quellenregel:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Ausbildungszeitschriften:**
Nur mit konkret bereitgestelltem Aufsatz oder lizenziert verifizierter Fundstelle verwenden; keine Aufsatzfundstellen aus Modellwissen.

**Lehrbücher und Sekundärquellen:**
Nur nennen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff die Angabe verifiziert.

Zitierregeln: → `../references/zitierweise.md`

## Akademische Integrität

Bevor du dieses Plugin für benotete Arbeiten verwendest – Hausarbeiten, Seminararbeiten, Take-Home-Klausuren –, prüfe die Prüfungsordnung deines Fachbereichs und die Vorgaben deines Prüfers zur KI-Nutzung. Viele Hochschulen verbieten oder beschränken den KI-Einsatz bei benoteten Leistungen. Das Plugin ist für Übung und Vorbereitung gedacht; es dort einzusetzen, wo deine Hochschule es verbietet, verstößt gegen die Prüfungsordnung – und die Konsequenzen trägst du, nicht das Tool.

## Konfidenzmarkierungen

Inhaltlich erzeugende Skills kennzeichnen ihre Konfidenz inline:

- `[PRÜFEN: Aussage – Quelle checken]` – wahrscheinlich korrekt, vor dem Examen aber gegen Kommentar, Lehrbuch oder Primärquelle prüfen
- `[UNSICHER: konkreter Grund]` – der Skill ist bei diesem speziellen Punkt nicht sicher (Mindermeinung, Streitstand, unklare JAG-Regelung)
- `[LÜCKE – aus Vorlesungsmitschrift füllen]` – gliederungs-baukasten-Marker, wo der Skill keine verlässliche Quelle hat
- `[RSPR FEHLT – Norm benannt, aber kein Leitfall]` – gliederungs-baukasten-Marker
- `[VGL. MITSCHRIFT – Dozentenbetonung hier relevant]` – gliederungs-baukasten-Marker
- `[AUSNAHME UNKLAR – Ausnahme bekannt, Voraussetzungen offen]` – gliederungs-baukasten-Marker
- `[UNSICHER – Prognose]` – examens-prognose-Marker: eine Einschätzung für die Lernzeitgewichtung, keine Vorhersage

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

- Drill oder Erklärung wird aus deinem Auftrag übernommen; nur bei Unklarheit wird nachgefragt. Du kannst während der Sitzung wechseln.
- Fallbearbeitungen und Gliederungsfeedback orientieren sich an deinem vorhandenen Format. Eigene Gliederungen können unmittelbar zum konkreten Auftrag gegeben werden; der Lernmodus bleibt erhalten.
- Examensvorbereitung zielt auf deine Schwächfächer gemäß Lernprofil. Das Plugin kommt immer wieder auf sie zurück.
- Jeder inhaltlich erzeugende Skill markiert Unsicherheiten. Vertrau den Markierungen mehr als ihrer Abwesenheit – eine unmarkierte Regelaussage ist etwas, woran der Skill sicher ist; prüfe trotzdem deine Quelle vor dem Examen.

<!-- BEGIN FACHMODULE-NAVIGATION -->

Das Plugin bietet **8 auswählbare Skills**. Die **58 vollständigen Fachmodule** und ihre Hilfsdateien bleiben in der [Fachbibliothek](FACHMODULE.md) zugänglich. Wählen Sie den Arbeitsweg nach dem gewünschten Ergebnis; er führt zu den passenden Vertiefungen.

<!-- END FACHMODULE-NAVIGATION -->

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Auftrag und bewährte Fachwerkzeuge | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/einstieg-routing/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/juristischer-argumentationskern/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Fallfrage | [`fallfrage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/fallfrage-bearbeiten/SKILL.md) |
| 3. Subsumtion | [`subsumtion-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/subsumtion-bearbeiten/SKILL.md) |
| 4. Arbeitsprodukt | [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| 5. Unterlagen und Quellen auswerten | [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| 6. Arbeitsprodukt ausarbeiten und kontrollieren | [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 8 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 8 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) | Ausbildung im Jurastudium: Arbeitsprodukt ausarbeiten und kontrollieren: Den verlangten Text oder die Berechnung fertigstellen, Gegenposition, Quellenstatus und offene Punkte prüfen und die nächste Handlung erklären. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-ausarbeiten-und-kontrollieren-bearbeiten/SKILL.md) |
| [`arbeitsprodukt-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-bearbeiten/SKILL.md) | Ausbildung im Jurastudium: Arbeitsprodukt: Gutachten, Hausarbeit mit Fußnoten oder Lernübersicht in bewertungssicherer Form ausformulieren. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/arbeitsprodukt-bearbeiten/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Jurastudium. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/einstieg-routing/SKILL.md) |
| [`fallfrage-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/fallfrage-bearbeiten/SKILL.md) | Ausbildung im Jurastudium: Fallfrage: Aufgabenstellung, Bearbeitervermerk, Rollenzuweisung und begehrte Rechtsfolge exakt erfassen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/fallfrage-bearbeiten/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/juristischer-argumentationskern/SKILL.md) | Juristischen Lernfall schrittweise lösen und erklären. Verarbeitet vorhandene Unterlagen, verbindet entscheidende Fachprüfungen und belegte Quellen, erstellt das beauftragte Ergebnis und führt denselben Vorgang nach neuen Angaben fort. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/juristischer-argumentationskern/SKILL.md) |
| [`subsumtion-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/subsumtion-bearbeiten/SKILL.md) | Ausbildung im Jurastudium: Subsumtion: Obersatz, Definition, Subsumtion, Ergebnis je Merkmal in ganzen Sätzen durchführen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/subsumtion-bearbeiten/SKILL.md) |
| [`unterlagen-und-quellen-auswerten-bearbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) | Ausbildung im Jurastudium: Unterlagen und Quellen auswerten: Akte, Belege, Chronologie, Recherche und entscheidende Lücken für den konkreten Fachauftrag nachvollziehbar erschließen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/unterlagen-und-quellen-auswerten-bearbeiten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Jurastudium. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=jurastudium/skills/workflow-kaltstart-und-routing/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
