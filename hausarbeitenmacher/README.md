# hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/hausarbeitenmacher.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/hausarbeitenmacher-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/hausarbeitenmacher-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/hausarbeitenmacher.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/hausarbeitenmacher.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Gutachtensatz: Obersatz, Definition, Subsumtion mit Sachverhaltszitat, Zwischenergebnis. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`hausarbeitenmacher-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/hausarbeitenmacher-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`hausarbeitenmacher-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/hausarbeitenmacher-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Hausarbeit BGB Übung Fortgeschrittene — Pohlmann / Leipzig / SS 26](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/README.md) | [Gesamt-PDF](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/gesamt-pdf/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung_gesamt.pdf) | [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip) | [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Freistehendes Plugin für Studenten der Rechtswissenschaft, das durch das Erstellen einer **Hausarbeit oder Seminararbeit lernfördernd** hindurchführt. Es liefert **keine fertigen Lösungen**, sondern stellt Fragen, gibt Strukturen, Methoden-Hinweise und Zitierweise — Du subsumierst selbst.

## Installation

1. Plugin-Umgebung öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `hausarbeitenmacher.zip` hochladen.
4. Mit einer konkreten Aufgabenstellung starten, zum Beispiel: `Hilf mir bei einer Hausarbeit. Sachverhalt folgt.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install hausarbeitenmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Mandatsperspektive

**Du als Studenten oder Studentenr.** Du gibst Deine Aufgabenstellung ein und gehst Schritt für Schritt durch die Lösung. Das Plugin

- fragt zu Beginn nach der **Lehrkraft** und entwickelt eine Adressaten-Strategie ohne Schleimerei,
- unterscheidet **Hausarbeit (Korrekturassistent)** und **Seminararbeit (persönliche Lektüre + Vortrag)**,
- analysiert Deine Aufgabenstellung,
- sortiert Dich in das passende Fachgebiet (Zivilrecht, Öffentliches Recht, Strafrecht — oder mehrere),
- gibt Dir die Prüfungs-Schemata,
- erklärt Dir den Gutachtenstil (Hausarbeit) bzw. den wissenschaftlichen Aufsatz-Stil (Seminararbeit),
- führt Dich durch jede Subsumtion oder jeden Erörterungs-Schritt,
- zeigt Dir typische Fehler und
- prüft am Ende, ob Du das Lernziel erreicht hast.

**Es löst die Arbeit nicht für Dich. Es lehrt Dich, sie zu lösen.**

## Adressaten-Strategie statt Schleimerei

Zu Beginn fragt das Plugin: **Von welchem Lehrstuhl stammt die Aufgabe?**

Wenn Du die Lehrkraft nennst, schlägt das Plugin eine kurze Recherche zu deren Auffassung vor (Publikationen, Kommentar-Bearbeitungen, Aufsätze). Dann kommt die ehrliche Komplizen-Frage:

> *Wollen wir nach dem Munde reden — oder die Aufgabe sauber lösen, auch wenn wir der Lehrkraft widersprechen müssen?*

Das Plugin empfiehlt **die saubere Lösung**. Selbst wenn Du der Lehrkraft am Ende widersprichst — eine begründete, mit guten Argumenten gestützte eigene Auffassung wird respektiert. **Schleim ist erkennbar und macht keine Karriere. Argumente machen Karriere.**

## Aufbau

Der Lebenszyklus einer Arbeit läuft in fünf Phasen:

```
Phase 0 — Adressaten-Klärung (Stunde 1)
  └─ Lehrkraft? → Hausarbeit oder Seminararbeit?
     → Adressaten-Strategie (kein Schleim, aber kluge Argumentation)

Phase A — Auftakt und Routing (Tag 1-3)
  └─ Aufgabenstellung erfassen → Fachgebiet identifizieren
     → Bearbeitungs-Plan festlegen

Phase B — Methodisches Fundament (Tag 4-10)
  └─ Gutachtenstil → Methodenlehre Auslegung
     → Gliederung mit Tiefenstruktur → Zitierweise
     → Quellenrecherche

Phase C — Fachgebiet-spezifische Prüfungsschemata (Tag 11-30)
  └─ Zivilrecht: Anspruchsgrundlagen-Reihenfolge
     ÖR: Statthaftigkeit → Zulässigkeit → Begründetheit
     Strafrecht: Tatbestand → Rechtswidrigkeit → Schuld
     Europarecht: Anwendungs-Vorrang Vorabentscheidung
     Verfassungsrecht: Grundrechts-Schema
     Rechtstheorie/-philosophie: Anbindung

Phase D — Schreiben, Reflektieren, Polieren (Tag 31-40)
  └─ Subsumtions-Übung → Meinungsstreit darstellen
     → Häufige Fehler vermeiden → Selbstkontrolle
     → Abgabe-Vorbereitung
     → Bei Seminararbeit: Vortrag und Disputation
```

## Enthaltene Skills (23)

### Phase 0 — Adressaten-Klärung (2 Skills)

| Slug | Beschreibung |
|---|---|
| `professor-erkennen-und-strategie` | Fangfrage Lehrkraft Kurz-Recherche Adressaten-Strategie ohne Schleim |
| `seminararbeit-modus` | Spezifika der Seminararbeit Forschungsfrage eigene These Vortrag Disputation |

### Phase A — Auftakt (3 Skills)

| Slug | Beschreibung |
|---|---|
| `aufgabenstellung-erfassen` | Falltext zerlegen Wesentliche/Unwesentliche unterscheiden Bearbeitungsvermerk verstehen |
| `fachgebiet-routing-zivil-oeffentlich-straf` | Welches Fachgebiet? Gemischte Konstellationen erkennen Reihenfolge bei Mix |
| `bearbeitungsplan-erstellen` | Zeitplan Stoff-Aufteilung Lern-Ziele für die Arbeit |

### Phase B — Methodisches Fundament (6 Skills)

| Slug | Beschreibung |
|---|---|
| `gutachtenstil-vs-urteilsstil` | Obersatz-Definition-Subsumtion-Ergebnis vs. begründungs-knapp Urteilsstil |
| `methodenlehre-auslegung` | Wortlaut-Systematik-Geschichte-Sinn-Zweck + verfassungs-/EU-konform |
| `gliederung-mit-tiefenstruktur` | A. B. C. → I. II. III. → 1. 2. 3. → a) b) c) — Tiefe richtig setzen |
| `zitierweise-jura-fundstellen` | Rspr. Kommentare Aufsätze BGH BVerfG amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang |
| `quellenrecherche-rechtsprechung-literatur` | Bibliothek amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang Google-Scholar Suchstrategie |
| `subsumtion-schritt-fuer-schritt` | Wie subsumiere ich richtig? Häufige Fehler |

### Phase C — Fachgebiet-Schemata (6 Skills)

| Slug | Beschreibung |
|---|---|
| `zivilrecht-anspruchsgrundlagen-pruefung` | V-C-G-D-D-B Reihenfolge BGB-Anspruch prüfen |
| `oeffentliches-recht-statthaft-zulaessig-begruendet` | VwGO §§ 40 42 47 113 Schemata Verwaltungsklage |
| `strafrecht-tatbestand-rechtswidrigkeit-schuld` | Schema 3-Stufen-Verbrechensaufbau |
| `verfassungsrecht-grundrechtspruefung` | Schutzbereich-Eingriff-verfassungsrechtliche Rechtfertigung |
| `europarecht-anwendbarkeit-vorrang-vorabentscheidung` | Art. 267 AEUV RL-Auslegung EuGH-Bezug |
| `rechtstheorie-rechtsphilosophie-anbindung` | Kelsen Hart Dworkin Radbruch Naturrecht Positivismus |

### Phase D — Schreiben und Reflektieren (4 Skills)

| Slug | Beschreibung |
|---|---|
| `meinungsstreit-darstellen` | h.M. — a.A. — eigene Stellungnahme strukturiert |
| `haeufige-fehler-vermeiden` | Top-20 typische Hausarbeit-Fehler |
| `selbstkontrolle-vor-abgabe` | Checkliste vor Abgabe Lernziel-Selbstprüfung |
| `behutsame-frech-wertschaetzende-rueckfragen` | Stil-Anleitung für das Plugin selbst: trocken-ketzerische Würze am Rande |

Plus der Master-Skill **`hausarbeit-workflow-start`** als Einstiegs-Schiene.

## Bedienungs-Hinweis

Das Plugin ist freistehend nutzbar und benötigt keine anderen Plugins. Für vertiefte methodische Fragen kann das Plugin `methodenlehre-buergerliches-recht` ergänzend geladen werden, für Lösungsschemata `jurastudium`, für die Zitierweise das Reference-Plugin `zitierweise-deutsches-recht`.

## Lern-Prinzip — Sokratische Methode

Das Plugin folgt der **sokratischen Methode**:

- Statt "Hier ist die Lösung" → "Welche Anspruchsgrundlage kommt zuerst in Betracht?"
- Statt "Subsumiere wie folgt" → "Welche Tatbestandsmerkmale müssen Sie prüfen?"
- Statt "Die h.M. sagt X" → "Welche Stimmen haben Sie gefunden? Wer argumentiert wie?"
- Statt "Schreibe diesen Absatz" → "Welche Struktur ist hier sinnvoll? Welche Definition brauchen Sie?"

Das Plugin liefert **Methoden, Schemata, Fragen, Quellen-Hinweise, Strukturen** — aber **niemals den Volltext einer Lösung**. Das Lernen erfolgt durch eigenständige Subsumtion oder eigenständige Erörterung.

## Dialog-Stil

Der Grundton des Plugins ist **sokratisch, gentle, ermutigend**. In Aufwärtsphasen erlaubt sich das Plugin gelegentlich — höchstens alle 5-7 Schritte — eine **behutsam-trockene, frech-wertschätzende Rückfrage**: ein leicht ironisches Staunen, eine alltagsphilosophische Beobachtung, eine selbstironische Wendung, eine scheinbar naive Nachfrage.

Beispiele für den Ton:

- *"Hmm. § 985 BGB als erste Anspruchsgrundlage. Mutig. Was hat denn der gute alte Vertrag Dir je angetan?"*
- *"Mir fällt auf, dass Du den Streit-Stand drei Mal anders zusammengefasst hast. Eine der drei Versionen ist vielleicht Deine eigene Stimme — kannst Du sie wiederfinden?"*

**Niemals herablassend, niemals zynisch, niemals besserwisserisch.** Bei Frust oder Lebensbelastung der lernenden Person wechselt das Plugin sofort in den klassisch warm-fragenden Modus zurück.

→ Skill `behutsame-frech-wertschaetzende-rueckfragen` regelt diesen Stil detailliert.

## Bei Unsicherheit

Wenn die Aufgabenstellung mehrdeutig ist, frage zuerst die Lehrkraft. Wenn die Bibliothek nicht ausreicht, ist das Plugin keine Ersatz-Bibliothek. Wenn die Klausur in 14 Tagen ist, ist das Plugin keine Last-Minute-Lösung.

**Das Plugin ist Dein Lern-Begleiter, kein Spickzettel.**

## ⚠️ Vorsicht: hiermit bitte nicht mogeln im Studium

Das Plugin ist ein **Lern- und Trainingswerkzeug** für Studenten, Tutoren und Lehrkräfte. Es ist ausdrücklich **nicht** dafür gedacht, irgendeinen vom Plugin generierten Text (Subsumtion, Gliederungs-Vorschlag, Argumentations-Skizze, Probe-Gutachten) **als eigene Leistung** in einer Hausarbeit, Seminararbeit, Klausur, Aktenklausur, mündlichen Prüfung oder im juristischen Vorbereitungsdienst einzureichen. Das wäre ein **Täuschungsversuch** im Sinne der jeweiligen Prüfungsordnung der Universitäten bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder. Folge ist regelmäßig **Nichtbestehen, Aberkennung der Prüfung oder disziplinarrechtliche Konsequenzen**. Der erlaubte Lernweg: erst selbst denken und schreiben, dann mit dem Plugin gegenprüfen, hinterfragen und verbessern lassen.

## Verbotenes (Eigen-Einschränkung)

Das Plugin

- gibt **keinen** Arbeits-Volltext aus,
- löst **keine** konkreten Subsumtionen oder Erörterungen für Dich,
- liefert **keine** fertigen Gutachten- oder Aufsatz-Texte zum Kopieren,
- ersetzt **keine** Lehrkraft.

Das Plugin

- erklärt Methoden, Schemata, Strukturen,
- stellt Fragen und Hilfsfragen,
- verweist auf Literatur und Rechtsprechung,
- prüft Deine Reflexion,
- unterstützt Deine eigene Lösungs-Findung.

## Sprachform und Du-/Sie-Form

Die Skills sprechen Dich teils mit "Du", teils mit "Sie" an — je nach Sprach-Konvention des betreffenden Rechtsgebiets (BGH-Stil eher Sie, Skript-Stil eher Du). Eine bewusste Mischform.

## Zitierweise

Sämtliche Zitierweise-Vorgaben folgen `references/zitierweise.md` des übergeordneten Repositories `claude-fuer-deutsches-recht`. Plus: Hausarbeits- und Seminararbeits-spezifische Standards (z.B. Sigel-Verzeichnis, bei Seminararbeit erweiterte Literaturschau).

## Tipps für die Bearbeitung

1. **Plane Zeit ein**: Hausarbeiten und Seminararbeiten brauchen Wochen, nicht Stunden. Plane sechs Wochen für eine Anfänger-/Fortgeschrittenenübung, drei Monate für eine Examenshausarbeit oder Seminararbeit.

2. **Lies den Sachverhalt mindestens dreimal**: Erst Überblick, dann Detail, dann Skizze der Beteiligten/Akten. Bei Seminararbeit: das Thema mit verwandter Literatur einlesen, dann die eigene Forschungsfrage scharf machen.

3. **Bearbeitungs-Vermerk genau lesen**: Was wird geprüft (Gutachten/Hilfsgutachten)? Welcher Standpunkt (Antragsteller/Antragsgegner)?

4. **Anspruchsgrundlagen-Reihenfolge wahren**: Bei Zivilrecht V-C-G-D-D-B (Vertrag-c.i.c.-GoA-Dinglich-Delikt-Bereicherung).

5. **Methodenlehre einbeziehen**: Nicht nur subsumieren, sondern bei Streit auch auslegen.

6. **Quellen sortieren**: Rechtsprechung vor Literatur, neueste zuerst, Bearbeiter-Name beachten.

7. **Selbstkontrolle vor Abgabe**: Mindestens zwei Durchgänge — einmal inhaltlich, einmal formal.

8. **Bei Seminararbeit zusätzlich**: Vortrag mindestens zweimal proben, Schwachstellen der Arbeit kennen, für die Disputation vorbereitet sein.

## Königsklasse

Eine Arbeit, die die Lehrkraft beeindruckt, **gerade weil Du gegen sie argumentiert hast** — aber mit so guten Argumenten, dass sie es Dir nicht übel nimmt, sondern respektiert. Das ist die Königsklasse. Sie ist erlernbar.


<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/anschluss-routing/SKILL.md), [`didaktisches-erstpruefung-und-mandatsziel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/didaktisches-erstpruefung-und-mandatsziel/SKILL.md), [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/dokumente-intake/SKILL.md), [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/einstieg-routing/SKILL.md), [`fachgebiet-routing-zivil-oeffentlich-straf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fachgebiet-routing-zivil-oeffentlich-straf/SKILL.md), [`hausarbeit-start`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-start/SKILL.md), [`hausarbeit-workflow-start`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-workflow-start/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`adressaten-formular-portal-und-einreichung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/adressaten-formular-portal-und-einreichung/SKILL.md), [`gutachtenstil-vs-haus-fussnotenstil`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gutachtenstil-vs-haus-fussnotenstil/SKILL.md), [`haus-literaturrecherche-leitfaden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-literaturrecherche-leitfaden/SKILL.md), [`hausarbeit-quellenrecherche-rspr-literatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-quellenrecherche-rspr-literatur/SKILL.md), [`juristische-liefert-beweislast-rechtstheorie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristische-liefert-beweislast-rechtstheorie/SKILL.md), [`liefert-beweislast-und-darlegungslast`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/liefert-beweislast-und-darlegungslast/SKILL.md), [`oeffentliches-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-quellenkarte/SKILL.md), [`quellen-livecheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellen-livecheck/SKILL.md), [`quellenrecherche-rechtsprechung-literatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellenrecherche-rechtsprechung-literatur/SKILL.md), [`seminararbeiten-dokumentenmatrix-und-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeiten-dokumentenmatrix-und-lueckenliste/SKILL.md), [`spezial-oeffentliches-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-oeffentliches-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`fuehrt-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fuehrt-risikoampel-und-gegenargumente/SKILL.md), [`haus-plagiatscheck-themaeingrenzung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-plagiatscheck-themaeingrenzung/SKILL.md), [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristischer-argumentationskern/SKILL.md), [`strafrecht-tatbestand-rechtswidrigkeit-schuld`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-tatbestand-rechtswidrigkeit-schuld/SKILL.md), [`subsumtion-schritt-verfassungsrecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/subsumtion-schritt-verfassungsrecht/SKILL.md), [`verfassungsrecht-grundrechtspruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/verfassungsrecht-grundrechtspruefung/SKILL.md), [`zivilrecht-anspruchsgrundlagen-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-anspruchsgrundlagen-pruefung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`bearbeitungsplan-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/bearbeitungsplan-erstellen/SKILL.md), [`gliederung-mit-tiefenstruktur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gliederung-mit-tiefenstruktur/SKILL.md), [`professor-erkennen-und-strategie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/professor-erkennen-und-strategie/SKILL.md), [`strategie-fehlerkatalog`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strategie-fehlerkatalog/SKILL.md), [`zivilrecht-verhandlung-vergleich-und-eskalation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`durch-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/durch-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`hausarbeiten-fristen-form-und-zustaendigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeiten-fristen-form-und-zustaendigkeit/SKILL.md), [`sokratisch-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/sokratisch-behoerden-gericht-und-registerweg/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`behutsame-frech-haeufige-fehler`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/behutsame-frech-haeufige-fehler/SKILL.md), [`haeufige-fehler-vermeiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haeufige-fehler-vermeiden/SKILL.md), [`selbstkontrolle-vor-abgabe`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/selbstkontrolle-vor-abgabe/SKILL.md), [`spezial-strategie-red-team-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-strategie-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`aufgabenstellung-erfassen-fachgebiet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/aufgabenstellung-erfassen-fachgebiet/SKILL.md), [`ausfluegen-didaktisches-durch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/ausfluegen-didaktisches-durch/SKILL.md), [`europarecht-anwendbarkeit-hausarbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-anwendbarkeit-hausarbeiten/SKILL.md), [`europarecht-interessen-fertigen-sonderfall`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-interessen-fertigen-sonderfall/SKILL.md), [`fertigen-sonderfall-und-edge-case`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fertigen-sonderfall-und-edge-case/SKILL.md), [`haus-fussnotenstil-spezial`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-fussnotenstil-spezial/SKILL.md), [`haus-themaeingrenzung-bauleiter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-themaeingrenzung-bauleiter/SKILL.md), [`meinungsstreit-darstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/meinungsstreit-darstellen/SKILL.md), [`methodenlehre-auslegung-oeffentliches`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/methodenlehre-auslegung-oeffentliches/SKILL.md), [`oeffentliches-recht-statthaft-zulaessig-begruendet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-recht-statthaft-zulaessig-begruendet/SKILL.md), [`rechtstheorie-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-internationaler-bezug-und-schnittstellen/SKILL.md), [`rechtstheorie-rechtsphilosophie-seminararbeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-rechtsphilosophie-seminararbeit/SKILL.md), [`schleimerei-seminararbeiten-sokratisch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/schleimerei-seminararbeiten-sokratisch/SKILL.md), [`seminararbeit-modus`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeit-modus/SKILL.md), [`strafrecht-zivilrecht-rechtswidrigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-zivilrecht-rechtswidrigkeit/SKILL.md), [`zitierweise-jura-fundstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zitierweise-jura-fundstellen/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 59 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`adressaten-formular-portal-und-einreichung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/adressaten-formular-portal-und-einreichung/SKILL.md) | Für Adressaten: Formular, Portal und Einreichungslogik: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/adressaten-formular-portal-und-einreichung/SKILL.md) |
| [`anschluss-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/anschluss-routing/SKILL.md) | Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/anschluss-routing/SKILL.md) |
| [`aufgabenstellung-erfassen-fachgebiet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/aufgabenstellung-erfassen-fachgebiet/SKILL.md) | Für Aufgabenstellung erfassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/aufgabenstellung-erfassen-fachgebiet/SKILL.md) |
| [`ausfluegen-didaktisches-durch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/ausfluegen-didaktisches-durch/SKILL.md) | Für Ausflügen: Compliance-Dokumentation und Aktenvermerk: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/ausfluegen-didaktisches-durch/SKILL.md) |
| [`bearbeitungsplan-erstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/bearbeitungsplan-erstellen/SKILL.md) | Für Bearbeitungs-Plan erstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/bearbeitungsplan-erstellen/SKILL.md) |
| [`behutsame-frech-haeufige-fehler`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/behutsame-frech-haeufige-fehler/SKILL.md) | Für Behutsame, frech-wertschätzende Rückfragen — Stil-Anleitung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/behutsame-frech-haeufige-fehler/SKILL.md) |
| [`didaktisches-erstpruefung-und-mandatsziel`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/didaktisches-erstpruefung-und-mandatsziel/SKILL.md) | Für Didaktisches: Erstprüfung, Rollenklärung und Mandatsziel: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/didaktisches-erstpruefung-und-mandatsziel/SKILL.md) |
| [`dokumente-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/dokumente-intake/SKILL.md) | Für Dokumentenintake: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/dokumente-intake/SKILL.md) |
| [`durch-schriftsatz-brief-und-memo-bausteine`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/durch-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Für Schriftsatz-, Brief- und Memo-Bausteine (Hausarbeiten): erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/durch-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/einstieg-routing/SKILL.md) |
| [`europarecht-anwendbarkeit-hausarbeiten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-anwendbarkeit-hausarbeiten/SKILL.md) | Für Europarecht — Anwendbarkeit, Vorrang, Vorabentscheidung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-anwendbarkeit-hausarbeiten/SKILL.md) |
| [`europarecht-interessen-fertigen-sonderfall`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-interessen-fertigen-sonderfall/SKILL.md) | Für Europarecht: Mehrparteienkonflikt und Interessenmatrix: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/europarecht-interessen-fertigen-sonderfall/SKILL.md) |
| [`fachgebiet-routing-zivil-oeffentlich-straf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fachgebiet-routing-zivil-oeffentlich-straf/SKILL.md) | Für Fachgebiet-Routing: Zivilrecht — Öffentliches Recht — Strafrecht: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fachgebiet-routing-zivil-oeffentlich-straf/SKILL.md) |
| [`fertigen-sonderfall-und-edge-case`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fertigen-sonderfall-und-edge-case/SKILL.md) | Für Fertigen: Sonderfall und Edge-Case-Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fertigen-sonderfall-und-edge-case/SKILL.md) |
| [`fuehrt-risikoampel-und-gegenargumente`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fuehrt-risikoampel-und-gegenargumente/SKILL.md) | Für Führt: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/fuehrt-risikoampel-und-gegenargumente/SKILL.md) |
| [`gliederung-mit-tiefenstruktur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gliederung-mit-tiefenstruktur/SKILL.md) | Für Gliederung mit Tiefen-Struktur: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gliederung-mit-tiefenstruktur/SKILL.md) |
| [`gutachtenstil-vs-haus-fussnotenstil`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gutachtenstil-vs-haus-fussnotenstil/SKILL.md) | Für Gutachtenstil und Urteilsstil: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/gutachtenstil-vs-haus-fussnotenstil/SKILL.md) |
| [`haeufige-fehler-vermeiden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haeufige-fehler-vermeiden/SKILL.md) | Für Häufige Fehler vermeiden — Top-20: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haeufige-fehler-vermeiden/SKILL.md) |
| [`haus-fussnotenstil-spezial`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-fussnotenstil-spezial/SKILL.md) | Für Haus: Fussnotenstil: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-fussnotenstil-spezial/SKILL.md) |
| [`haus-literaturrecherche-leitfaden`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-literaturrecherche-leitfaden/SKILL.md) | Für Haus: Literaturrecherche: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-literaturrecherche-leitfaden/SKILL.md) |
| [`haus-plagiatscheck-themaeingrenzung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-plagiatscheck-themaeingrenzung/SKILL.md) | Für Haus: Plagiatscheck Eigenständigkeit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-plagiatscheck-themaeingrenzung/SKILL.md) |
| [`haus-themaeingrenzung-bauleiter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-themaeingrenzung-bauleiter/SKILL.md) | Für Haus: Themeneingrenzung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/haus-themaeingrenzung-bauleiter/SKILL.md) |
| [`hausarbeit-quellenrecherche-rspr-literatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-quellenrecherche-rspr-literatur/SKILL.md) | Für Fristen- und Risikoampel: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-quellenrecherche-rspr-literatur/SKILL.md) |
| [`hausarbeit-start`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-start/SKILL.md) | Für Hausarbeitenmacher — Allgemein: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-start/SKILL.md) |
| [`hausarbeit-workflow-start`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-workflow-start/SKILL.md) | Für Master-Hausarbeiten- und Seminararbeitenmacher: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeit-workflow-start/SKILL.md) |
| [`hausarbeiten-fristen-form-und-zustaendigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeiten-fristen-form-und-zustaendigkeit/SKILL.md) | Für Hausarbeiten: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/hausarbeiten-fristen-form-und-zustaendigkeit/SKILL.md) |
| [`juristische-liefert-beweislast-rechtstheorie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristische-liefert-beweislast-rechtstheorie/SKILL.md) | Für Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristische-liefert-beweislast-rechtstheorie/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Hausarbeitenmacher ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/juristischer-argumentationskern/SKILL.md) |
| [`liefert-beweislast-und-darlegungslast`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/liefert-beweislast-und-darlegungslast/SKILL.md) | Für Liefert: Beweislast, Darlegungslast und Substantiierung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/liefert-beweislast-und-darlegungslast/SKILL.md) |
| [`meinungsstreit-darstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/meinungsstreit-darstellen/SKILL.md) | Für Meinungsstreit darstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/meinungsstreit-darstellen/SKILL.md) |
| [`methodenlehre-auslegung-oeffentliches`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/methodenlehre-auslegung-oeffentliches/SKILL.md) | Für Methodenlehre und Auslegung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/methodenlehre-auslegung-oeffentliches/SKILL.md) |
| [`oeffentliches-quellenkarte`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-quellenkarte/SKILL.md) | Für Öffentliches Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-quellenkarte/SKILL.md) |
| [`oeffentliches-recht-statthaft-zulaessig-begruendet`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-recht-statthaft-zulaessig-begruendet/SKILL.md) | Für Öffentliches Recht — Statthaftigkeit, Zulässigkeit, Begründetheit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/oeffentliches-recht-statthaft-zulaessig-begruendet/SKILL.md) |
| [`output-waehlen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/output-waehlen/SKILL.md) | Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/output-waehlen/SKILL.md) |
| [`professor-erkennen-und-strategie`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/professor-erkennen-und-strategie/SKILL.md) | Für Professor erkennen und Strategie wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Verhandlungs- oder Eskalationslinie. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/professor-erkennen-und-strategie/SKILL.md) |
| [`quellen-livecheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellen-livecheck/SKILL.md) | Für Rechtsquellen-Livecheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellen-livecheck/SKILL.md) |
| [`quellenrecherche-rechtsprechung-literatur`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellenrecherche-rechtsprechung-literatur/SKILL.md) | Für Quellen-Recherche — Rechtsprechung und Literatur: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/quellenrecherche-rechtsprechung-literatur/SKILL.md) |
| [`rechtstheorie-internationaler-bezug-und-schnittstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-internationaler-bezug-und-schnittstellen/SKILL.md) | Für Rechtstheorie: Internationaler Bezug und Schnittstellen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-internationaler-bezug-und-schnittstellen/SKILL.md) |
| [`rechtstheorie-rechtsphilosophie-seminararbeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-rechtsphilosophie-seminararbeit/SKILL.md) | Für Rechtstheorie und Rechtsphilosophie — Anbindung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/rechtstheorie-rechtsphilosophie-seminararbeit/SKILL.md) |
| [`schleimerei-seminararbeiten-sokratisch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/schleimerei-seminararbeiten-sokratisch/SKILL.md) | Für Schleimerei: Mandantenkommunikation und Entscheidungsvorlage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/schleimerei-seminararbeiten-sokratisch/SKILL.md) |
| [`selbstkontrolle-vor-abgabe`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/selbstkontrolle-vor-abgabe/SKILL.md) | Für Selbst-Kontrolle vor Abgabe: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/selbstkontrolle-vor-abgabe/SKILL.md) |
| [`seminararbeit-modus`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeit-modus/SKILL.md) | Für Seminararbeit-Modus: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeit-modus/SKILL.md) |
| [`seminararbeiten-dokumentenmatrix-und-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeiten-dokumentenmatrix-und-lueckenliste/SKILL.md) | Für Seminararbeiten: Dokumentenmatrix, Lückenliste und Nachforderung: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/seminararbeiten-dokumentenmatrix-und-lueckenliste/SKILL.md) |
| [`sokratisch-behoerden-gericht-und-registerweg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/sokratisch-behoerden-gericht-und-registerweg/SKILL.md) | Für Sokratisch: Behörden-, Gerichts- oder Registerweg: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/sokratisch-behoerden-gericht-und-registerweg/SKILL.md) |
| [`spezial-oeffentliches-livequellen-und-rechtsprechungscheck`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-oeffentliches-livequellen-und-rechtsprechungscheck/SKILL.md) | Für Öffentliches: Livequellen- und Rechtsprechungscheck: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-oeffentliches-livequellen-und-rechtsprechungscheck/SKILL.md) |
| [`spezial-strategie-red-team-und-qualitaetskontrolle`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-strategie-red-team-und-qualitaetskontrolle/SKILL.md) | Für Strategie: Red-Team und Qualitätskontrolle: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/spezial-strategie-red-team-und-qualitaetskontrolle/SKILL.md) |
| [`strafrecht-tatbestand-rechtswidrigkeit-schuld`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-tatbestand-rechtswidrigkeit-schuld/SKILL.md) | Für Strafrecht — Drei-Stufen-Aufbau: Tatbestand, Rechtswidrigkeit, Schuld: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-tatbestand-rechtswidrigkeit-schuld/SKILL.md) |
| [`strafrecht-zivilrecht-rechtswidrigkeit`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-zivilrecht-rechtswidrigkeit/SKILL.md) | Für Strafrecht: Zahlen, Schwellenwerte und Berechnung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strafrecht-zivilrecht-rechtswidrigkeit/SKILL.md) |
| [`strategie-fehlerkatalog`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strategie-fehlerkatalog/SKILL.md) | Für Strategie Fehlerkatalog: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Verhandlungs- oder Eskalationslinie. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/strategie-fehlerkatalog/SKILL.md) |
| [`subsumtion-schritt-verfassungsrecht`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/subsumtion-schritt-verfassungsrecht/SKILL.md) | Für Subsumtion Schritt für Schritt: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/subsumtion-schritt-verfassungsrecht/SKILL.md) |
| [`unterlagen-luecken`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/unterlagen-luecken/SKILL.md) | Für Unterlagen und Lücken: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/unterlagen-luecken/SKILL.md) |
| [`verfassungsrecht-grundrechtspruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/verfassungsrecht-grundrechtspruefung/SKILL.md) | Für Verfassungsrecht — Grundrechts-Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/verfassungsrecht-grundrechtspruefung/SKILL.md) |
| [`workflow-chronologie-und-belegmatrix`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Für Chronologie und Belegmatrix: ordnet Akte, Belege und Lücken; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-chronologie-und-belegmatrix/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-kaltstart-und-routing/SKILL.md) |
| [`workflow-redteam-qualitygate`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-redteam-qualitygate/SKILL.md) | Für Red-Team Qualitygate: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-redteam-qualitygate/SKILL.md) |
| [`workflow-unterlagen-lueckenliste`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-unterlagen-lueckenliste/SKILL.md) | Für Unterlagen- und Lückenliste: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| [`zitierweise-jura-fundstellen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zitierweise-jura-fundstellen/SKILL.md) | Für Zitierweise in der juristischen Hausarbeit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zitierweise-jura-fundstellen/SKILL.md) |
| [`zivilrecht-anspruchsgrundlagen-pruefung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-anspruchsgrundlagen-pruefung/SKILL.md) | Für Zivilrecht Anspruchsgrundlagen Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-anspruchsgrundlagen-pruefung/SKILL.md) |
| [`zivilrecht-verhandlung-vergleich-und-eskalation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-verhandlung-vergleich-und-eskalation/SKILL.md) | Für Zivilrecht: Verhandlung, Vergleich und Eskalation: entwickelt Ziel, Vergleich und Eskalation; Ergebnis: Verhandlungs- oder Eskalationslinie. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=hausarbeitenmacher/skills/zivilrecht-verhandlung-vergleich-und-eskalation/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
