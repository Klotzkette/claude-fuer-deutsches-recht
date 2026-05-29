# Jurastudium-Plugin

Lernmodus, kein Antwortmodus. Prüfungsgespräch nach AG-Tradition, das *dich* fragt und unpräzises Denken zurückweist. Fallbearbeitung im Gutachtenstil, Lern-Outlines, Karteikarten, Gutachten-Bewertung, AG-/Seminar-Vorbereitung, strukturiertes Feedback auf Hausarbeiten und Seminararbeiten – ohne jemals für dich zu schreiben –, sowie Examensprognose auf Basis vergangener Prüfungen. Kalibriert auf dich: deine Fachsemester, dein Bundesland, dein Prüfungsamt (JPA), ob du gebohrt oder erklärt haben willst.

**Jede Ausgabe ist ein Lerngerüst, kein Mustergutachten. Das Plugin strukturiert dein Denken, bohrt dich sokratisch und zeigt dir, was du falsch hattest. Es schreibt nicht die Gliederung, nicht das Gutachten, nicht die Hausarbeit für dich – das würde den Lernzweck unterlaufen. Zitate in Lernmaterialien sind als zu prüfend markiert.**

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Jurastudium (`jurastudium`, dieses Plugin) | [jurastudium.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jurastudium.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Für wen ist das

Jurastudierende ab dem 1. Semester bis zum 2. Staatsexamen:  
- **Studium (Grundstudium + Schwerpunkt):** große BGB-Übungen, kleine BGB-Übungen, Anfänger- und Fortgeschrittenenübungen, Klausuren und Hausarbeiten in allen Pflicht- und Wahlfächern.  
- **Erstes Juristisches Staatsexamen (Erste Juristische Prüfung / FJP):** schriftliche Klausuren und mündliche Prüfung nach der jeweiligen JAG (Juristenausbildungsgesetz der Länder).  
- **Referendariat und Zweites Staatsexamen:** Anwaltsklausur, Aktenvortrag, Pflichtstation-Klausuren (Zivilrecht, Strafrecht, Verwaltungsrecht, Arbeitsrecht, Wahlstation).  

## Erster Start: Kaltstart

Dieser Schritt dreht sich um dich: Fachsemester, Bundesland, JAG-Anforderungen, Lernstil (Drill oder Erklärung). Bringe Material mit: eigene Gliederungen, benotete Klausuren, alte Examsklausuren (vor allem vom eigenen JPA), Seminarunterlagen, Vorlesungsskripte. Zehn bis zwanzig Positionen sind das Ziel; darunter wird das Lernprofil als `WENIG MATERIAL` markiert und nachgelagerte Skills sind dünner.

```
/jurastudium:jurastudium-kaltstart-interview
```

## Skills

Jeder Skill wird als `/jurastudium:<skill-name>` aufgerufen.

| Skill | Funktion |
|---|---|
| `/jurastudium:jurastudium-kaltstart-interview` | Über-dich-Interview + Materialaufnahme – Fachsemester, Bundesland, JAG, Lernstil, Materialien |
| `/jurastudium:pruefungsgespraech-ag [Rechtsgebiet]` | Prüfungsgespräch nach AG-Tradition – das Plugin fragt, du antwortest, es hakt nach. Gibt keine Antwort vor. |
| `/jurastudium:fall-zusammenfassung [Sachverhalt/Fall]` | Fallbearbeitung im Gutachtenstil (Obersatz – Definition – Subsumtion – Ergebnis) |
| `/jurastudium:gliederungs-baukasten [Rechtsgebiet]` | Lern-Outline / Strukturen pro Rechtsgebiet aufbauen oder erweitern |
| `/jurastudium:examensvorbereitung-fragen [Rechtsgebiet]` | Examensvorbereitungs-Fragen für 1. und 2. StEx, Bundesland-spezifisch nach JAG; kennzeichnet h.M. vs. Mindermeinung |
| `/jurastudium:karteikarten [Rechtsgebiet]` | Karteikarten generieren oder abfragen; Leitner-Stapel; fachgebietsweise Markdown; `--session <n>`-Modus |
| `/jurastudium:lernplan` | Langfristigen Lernplan erstellen oder anpassen – Phasen, Schwächefächer, adaptiver Tagesplan aus Sitzungshistorie |
| `/jurastudium:lernsitzung <Rechtsgebiet> <n>` | Fokussierte N-Fragen-Sitzung zu einem Rechtsgebiet; aktualisiert den Lernplan mit Ergebnissen |
| `/jurastudium:gutachten-uebung` | Gutachten bewerten – Aufbau, Obersatz, Subsumtion, Ergebnis, Zitierweise. Protokolliert Muster über Sitzungen. Schreibt nie um. |
| `/jurastudium:ag-vorbereitung [Fall/Thema]` | AG-/Seminar-Vorbereitung – Professorenfragen vorhersagen und einüben |
| `/jurastudium:juristisches-schreiben [Pfad oder Text]` | Strukturfeedback auf jeden Entwurf – schreibt nie um, nie |
| `/jurastudium:examens-prognose [Fach/Kurs]` | Vergangene Examsklausuren analysieren; Prognose für die nächste Prüfung; JPA-Statistik |
| `/jurastudium:subsumtionslehre [Norm/Sachverhalt]` | Subsumtion als Königsdisziplin üben – Trennung Obersatz/Definition/Subsumtion/Ergebnis, Pushback bei Subsumtionssprüngen, vorweggenommener Würdigung und vermischtem Stil |
| `/jurastudium:methodenlehre-grundlagen [Norm]` | Vier Auslegungsmethoden (Savigny), Analogie, teleologische Reduktion, verfassungs- und unionsrechtskonforme Auslegung – mit Argumentationslast |
| `/jurastudium:methodenlehre-zivilrecht [Fall]` | AGL-Reihenfolge, Konkurrenzen, Auslegung von Willenserklärungen (§§ 133, 157 BGB), Auslegung von AGB – Drill-Modus |
| `/jurastudium:methodenlehre-strafrecht [Sachverhalt]` | Dreistufiger Verbrechensaufbau, Trennung objektiver/subjektiver Tatbestand, Konkurrenzen, Analogieverbot Art. 103 II GG |
| `/jurastudium:methodenlehre-oeffentliches-recht [Fall]` | Schichtenprüfung der Grundrechte, Verhältnismäßigkeit, Ermessen, VA-Qualität, Klageart, Vorrang des Unionsrechts |
| `/jurastudium:rechtsgeschichte [Epoche/Thema]` | Fünf historische Linien: römisches Recht und BGB-Genese, NS-Unrechtsjustiz und Radbruchsche Formel, SED-Unrecht und Mauerschützen, GG 1949, Unionsrecht von EGKS bis Lissabon |
| `/jurastudium:lernstrategien` | Evidenzbasierte Lernmethoden für Jura – aktiver Abruf, Spaced Repetition, Interleaving, Elaboration, Klausurtaktik unter Zeitdruck |
| `/jurastudium:tatbestaende-lernen [§ / Rechtsgebiet]` | Tatbestände zerlegen, Definitionen abrufbar machen, Streitstände am Merkmal verankern; integriert mit `karteikarten` |
| `/jurastudium:loesungsschemata [Norm/Rechtsgebiet]` | Klassische Schemata (Anspruchsprüfung, Verbrechensaufbau, Grundrechtsprüfung, EBV, Bereicherung) – mit ehrlichem Disclaimer: nicht dogmatisch zwingend, aber Verständniskatalysator; whatever works |

## Was "Lernmodus" bedeutet

Mehrere Skills (pruefungsgespraech-ag, fall-zusammenfassung im Drill-Modus, ag-vorbereitung, gutachten-uebung, juristisches-schreiben, subsumtionslehre, methodenlehre-*, tatbestaende-lernen) sind bewusst so gebaut, dass sie dir die Antwort **nicht geben** und das Gutachten **nicht für dich schreiben**. Der Zweck ist, dass du durch eigenes Tun lernst. Wenn du eine fertige Antwort oder einen Entwurf willst, nimm ein anderes Tool. Dieses Plugin ist für den Kampf.

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

- Drill-Modus oder Erklärungs-Modus wird beim Kaltstart festgelegt; du kannst pro Sitzung wechseln.
- Fallbearbeitungen und Gliederungen verwenden **dein** Format. Wenn du eigene Gliederungen hast, weise Kaltstart darauf hin.
- Examensvorbereitung zielt auf deine Schwächfächer gemäß Lernprofil. Das Plugin kommt immer wieder auf sie zurück.
- Jeder inhaltlich erzeugende Skill markiert Unsicherheiten. Vertrau den Markierungen mehr als ihrer Abwesenheit – eine unmarkierte Regelaussage ist etwas, woran der Skill sicher ist; prüfe trotzdem deine Quelle vor dem Examen.
