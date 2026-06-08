# Jurastudium-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`jurastudium`) | [`jurastudium.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jurastudium.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Examensbegleitung Roosendaal-Tinnefeld — 1. Staatsexamen Bonn, Frühjahr 2027** (`jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027`) | [Gesamt-PDF lesen](../testakten/jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027/gesamt-pdf/jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027_gesamt.pdf) | [`testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-jurastudium-leitfaden-1-staatsexamen-roosendaal-bonn-vorbereitung-2027.zip) |
| **Akte Jana Mondsee - Drittversuch, KI-Vorwurf und Masterarbeit** (`pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee`) | [Gesamt-PDF lesen](../testakten/pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee/gesamt-pdf/pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee_gesamt.pdf) | [`testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-pruefungsrecht-drittversuch-ki-taeuschung-masterarbeit-mondsee.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Lernmodus, kein Antwortmodus. Prüfungsgespräch nach AG-Tradition, das *dich* fragt und unpräzises Denken zurückweist. Fallbearbeitung im Gutachtenstil, Lern-Outlines, Karteikarten, Gutachten-Bewertung, AG-/Seminar-Vorbereitung, strukturiertes Feedback auf Hausarbeiten und Seminararbeiten – ohne jemals für dich zu schreiben –, sowie Examensprognose auf Basis vergangener Prüfungen. Kalibriert auf dich: deine Fachsemester, dein Bundesland, dein Prüfungsamt (JPA), ob du gebohrt oder erklärt haben willst.

**Jede Ausgabe ist ein Lerngerüst, kein Mustergutachten. Das Plugin strukturiert dein Denken, bohrt dich sokratisch und zeigt dir, was du falsch hattest. Es schreibt nicht die Gliederung, nicht das Gutachten, nicht die Hausarbeit für dich – das würde den Lernzweck unterlaufen. Zitate in Lernmaterialien sind als zu prüfend markiert.**

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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ag-vorbereitung-examens-prognose` | AG-Vorbereitung und Cold-Call-Prep für Jurastudium: Anwendungsfall Student wird im naechsten Seminar oder Arbeitsgemeinschaft aufgerufen und muss konkrete Faelle vorbereiten und Fragen des Dozenten antizipieren. BGB-AT, SchuldR, Strafrec... |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Jurastudium-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Up... |
| `dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `examens-prognose` | Examensprognose auf Basis bisheriger JPA-Klausuren und BMJV-Statistiken: Anwendungsfall Student will Lernzeit auf wahrscheinliche Themen konzentrieren und fragt welche Schwerpunkte das Justizprüfungsamt bisher prüfte. Examensvorbereitung... |
| `examensvorbereitung-fragen` | Examensvorbereitungs-Fragen für 1. und 2. Staatsexamen erstellen: Anwendungsfall Student will Examenswissen durch gezielte Uebungsfragen trainieren und Schwachstellen erkennen. 1. StEx und 2. StEx, JAG Bundesland Bayern NRW Hamburg, Subs... |
| `fall-zusammenfassung-gliederungs-baukasten` | Juristischen Fall zusammenfassen und strukturieren: Anwendungsfall Student oder Referendar muss langen Sachverhalt oder Urteil in praegnante Fallzusammenfassung fassen und Kernprobleme herausarbeiten. Gutachtenstil, Tatbestandsmerkmale,... |
| `gliederungs-baukasten` | Gliederungs-Baukasten für juristische Hausarbeiten und Seminararbeiten: Anwendungsfall Student erstellt Gliederung für Hausarbeit Seminararbeit oder wissenschaftliche Arbeit und braucht strukturierten Aufbau. Methodenlehre, Gutachtenstil... |
| `gutachten-uebung` | Gutachten Uebung für Jurastudium und Examensvorbereitung: Anwendungsfall Student bearbeitet Uebungsfall und soll Klausurtechnik Gutachtenstil Subsumtion und Zeitmanagement trainieren. Gutachtenstil mit Obersatz Definiton Subsumtion Ergeb... |
| `gutachtenstil-internationaler-bezug-und-schnittstellen` | Gutachtenstil: Internationaler Bezug und Schnittstellen; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen T... |
| `juristisches-schreiben` | Juristisches Schreiben trainieren für Klausur und Seminararbeit: Anwendungsfall Student will Schreibstil verbessern und benoetigt Feedback zu Formulierungen Argumentationsstruktur und Praegnanz. Gutachtenstil, Lösungsschemata, Subsumtion... |
| `juristisches-schreiben-jus` | Lernprofil im Jurastudium anpassen und aktualisieren: Anwendungsfall Student wechselt Lernstil, aendert Studienschwerpunkte, wechselt Bundesland oder aktualisiert Prüfungsziel von Zwischenprüfung auf Examen. 1. und 2. Staatsexamen, JAG B... |
| `jus-klausurtraining-leitfaden` | Leitfaden Klausurtraining: Sachverhaltsanalyse, Aufbau, Zeitmanagement, typische Fehler. Pruefraster für Klausurenkurs Z1 / Z2 / Examen im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechu... |
| `jus-referendariat-stationen-staatsexamen` | Spezialfall Referendariatsstationen Strafrecht / Zivilrecht / Verwaltung / Anwalt / Wahl: Aufgaben, Beurteilung, Aktenvortrag. Pruefraster für Referendar im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Beleg... |
| `jus-staatsexamen-vorbereitung-spezial` | Spezialfall Staatsexamensvorbereitung: Lernplan zwoelf Monate, Karteikartensystem, Probeklausuren, gesundheitliche Aspekte. Pruefraster für Examenskandidaten im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, B... |
| `jus-studienplan-bauleiter` | Bauleiter Studienplan Jura: Pflichtfaecher, Schwerpunktbereich, Examensvorbereitung, Auslandssemester. Pruefraster für typische Pruefungsordnungen im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und R... |
| `kaltstart-interview` | Jurastudium-Einstieg und Lernprofil-Aufnahme: Anwendungsfall Student startet erstmals Jurastudium-Skill und muss Lernprofil Semester Bundesland Prüfungsziel und Lernstil konfigurieren. 1. StEx und 2. StEx, JAG Bundesland-Varianten, Metho... |
| `karteikarten-lernplan-lernsitzung` | Karteikarten für Jurastudium und Examensvorbereitung erstellen: Anwendungsfall Student will Definitionen Tatbestaende Normen und Klausurrelevante Faelle als Lernkarten strukturieren. Lösungsschemata, Tatbestaende, Definitionen Buergerlic... |
| `klausurkorrektur-formular-portal-und-einreichung` | Klausurkorrektur: Formular, Portal und Einreichungslogik; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen... |
| `klausurkorrektur-lernplanung-red-team-korrektur` | Jurastudium: Mandantenkommunikation und Entscheidungsvorlage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägi... |
| `lernplan` | Erstellt oder aktualisiert einen strukturierten Lernplan für das Erste Staatsexamen, das Referendariat oder das Zweite Staatsexamen — phasenbezogen, nach Schwächen gewichtet, adaptiv nach Lernverlauf. Berücksichtigt Repetitoriumskalender... |
| `lernplanung-red-team-und-qualitaetskontrolle` | Lernplanung: Red-Team und Qualitätskontrolle; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatbestandsm... |
| `lernsitzung` | Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Lösungsschemata Zivilre... |
| `lernstrategien-livecheck-sonderfall` | Lernstrategien: Compliance-Dokumentation und Aktenvermerk; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen... |
| `lernstrategien-loesungsschemata-methodenlehre` | Lernstrategien für Jurastudium und Examensvorbereitung entwickeln: Anwendungsfall Student sucht effektive Lernmethoden für Examensvorbereitung und will Zeit und Energie optimal einsetzen. Examensvorbereitung 1. und 2. Staatsexamen, Metho... |
| `livecheck-sonderfall-und-edge-case` | Livecheck: Sonderfall und Edge-Case-Prüfung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatbestandsme... |
| `loesungsschemata` | Stellt klassische Lösungsschemata für die deutsche Juristenklausur bereit — Anspruchsprüfung, Verbrechensaufbau, Grundrechtsprüfung, Verhältnismäßigkeit, Klageart-Bestimmung, EBV, Bereicherung, GoA, c.i.c., culpa-Strukturen. Mit ehrliche... |
| `loesungsschemata-mehrparteien-konflikt-und-interessen` | Loesungsschemata: Mehrparteienkonflikt und Interessenmatrix; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägig... |
| `methodenlehre-grundlagen` | Übt die juristische Methodenlehre für Studierende — Auslegung nach Wortlaut/Systematik/Historie/Telos, Analogie, teleologische Reduktion, Auslegung gegen den Wortlaut, verfassungskonforme und unionsrechtskonforme Auslegung, Argumentation... |
| `methodenlehre-oeffentliches-strafrecht` | Übt die öffentlich-rechtliche Methodenlehre — Schichtenprüfung bei Grundrechten, Verhältnismäßigkeit, Ermessen und Ermessensfehler, Verwaltungsaktqualität, prozessuale Methodik der Klagearten, unionsrechtskonforme Auslegung, Vorrang des... |
| `methodenlehre-rechtsgeschichte-referendariat` | Methodenlehre: Behörden-, Gerichts- oder Registerweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatb... |
| `methodenlehre-strafrecht` | Übt die strafrechtliche Methodenlehre — dreistufiger Verbrechensaufbau (Tatbestand, Rechtswidrigkeit, Schuld), Trennung objektiver/subjektiver Tatbestand, Konkurrenzlehre (Tateinheit § 52, Tatmehrheit § 53, Gesetzeskonkurrenz), Analogiev... |
| `methodenlehre-zivilrecht` | Übt die zivilrechtliche Methodenlehre für Studierende — Anspruchsgrundlagen-Schema, AGL-Reihenfolge (vertraglich, vertragsähnlich, dinglich, deliktisch, bereicherungsrechtlich), Konkurrenzen, Auslegung von Willenserklärungen (§§ 133/157... |
| `oeffentliches-quellenkarte` | Oeffentliches Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `output-waehlen` | Output wählen im Jurastudium: Diese Output-Weiche für Jurastudium entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `pruefungsgespraech-ag-rechtsgeschichte` | Prüfungsgespraech und Sokrates-Methode in Arbeitsgemeinschaft simulieren: Anwendungsfall Student will AG-Diskussion oder Dozentengespraeach simulieren und Argumentation trainieren. Subsumtion, Lösungsschemata, Tatbestaende Zivilrecht Str... |
| `pruefungsgespraech-fristen-form-und-zustaendigkeit` | Pruefungsgespraech: Fristen, Form, Zuständigkeit und Rechtsweg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlä... |
| `pruefungsgespraech-muendlich` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priori... |
| `quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsgeschichte` | Übt deutsche und europäische Rechtsgeschichte für Studierende — römisches Recht und die BGB-Entstehung 1900, NS-Unrechtsjustiz und die Folgen der Radbruchschen Formel, SED-Unrecht und Mauerschützenprozesse, Entstehung des Grundgesetzes n... |
| `rechtsgeschichte-zahlen-schwellen-und-berechnung` | Rechtsgeschichte: Zahlen, Schwellenwerte und Berechnung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen T... |
| `rechtsquellen-beweislast-darlegungslast` | Rechtsquellen: Quellenprüfung; Beweislast, Darlegungslast und Substantiierung: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `referendariat-tatbestand-beweis-und-belege` | Referendariat: Tatbestandsmerkmale, Beweisfragen und Beleglage; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlä... |
| `strafrecht-studium-subsumtionslehre` | Strafrecht: Verhandlung, Vergleich und Eskalation; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatbest... |
| `studium-erstpruefung-und-mandatsziel` | Studium: Erstprüfung, Rollenklärung und Mandatsziel; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatbe... |
| `subsumtionslehre` | Übt die Subsumtion als Königsdisziplin der deutschen Klausur — Trennung Obersatz/Definition/Subsumtion/Ergebnis, Tatbestandsmerkmal für Tatbestandsmerkmal, mit Pushback bei Subsumtionssprüngen, vorweggenommener Würdigung und vermischtem... |
| `subsumtionslehre-risikoampel-und-gegenargumente` | Subsumtionslehre: Risikoampel, Gegenargumente und Verteidigungslinien; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die e... |
| `tatbestaende-lernen` | Tatbestaende Lernen im Jurastudium im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `tradition-zivilrecht-subsumtionslehre` | Tradition: Dokumentenmatrix, Lückenliste und Nachforderung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägige... |
| `unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Out... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prio... |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert prioris... |
| `zivilrecht-schriftsatz-brief-und-memo-bausteine` | Zivilrecht: Schriftsatz-, Brief- und Memo-Bausteine; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung im Jurastudium: prüft konkret die einschlägigen Tatbe... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
