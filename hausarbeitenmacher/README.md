# hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion.

Dieses Plugin gehört zum Marketplace mit 235 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Direktnavigation: [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/hausarbeitenmacher.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/hausarbeitenmacher/hausarbeitenmacher-werkstatt.md" download><code>hausarbeitenmacher-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/hausarbeitenmacher/hausarbeitenmacher-schnellstart.md" download><code>hausarbeitenmacher-schnellstart.md</code></a> |
| Zugeordnete Testakten | PDF / ZIP | [eine zugeordnete Akte](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

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

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`anschluss-routing`](skills/anschluss-routing/SKILL.md), [`didaktisches-erstpruefung-und-mandatsziel`](skills/didaktisches-erstpruefung-und-mandatsziel/SKILL.md), [`dokumente-intake`](skills/dokumente-intake/SKILL.md), [`einstieg-routing`](skills/einstieg-routing/SKILL.md), [`fachgebiet-routing-zivil-oeffentlich-straf`](skills/fachgebiet-routing-zivil-oeffentlich-straf/SKILL.md), [`hausarbeit-start`](skills/hausarbeit-start/SKILL.md), [`hausarbeit-workflow-start`](skills/hausarbeit-workflow-start/SKILL.md), [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`adressaten-formular-portal-und-einreichung`](skills/adressaten-formular-portal-und-einreichung/SKILL.md), [`gutachtenstil-vs-haus-fussnotenstil`](skills/gutachtenstil-vs-haus-fussnotenstil/SKILL.md), [`haus-literaturrecherche-leitfaden`](skills/haus-literaturrecherche-leitfaden/SKILL.md), [`hausarbeit-quellenrecherche-rspr-literatur`](skills/hausarbeit-quellenrecherche-rspr-literatur/SKILL.md), [`juristische-liefert-beweislast-rechtstheorie`](skills/juristische-liefert-beweislast-rechtstheorie/SKILL.md), [`liefert-beweislast-und-darlegungslast`](skills/liefert-beweislast-und-darlegungslast/SKILL.md), [`oeffentliches-quellenkarte`](skills/oeffentliches-quellenkarte/SKILL.md), [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md), [`quellenrecherche-rechtsprechung-literatur`](skills/quellenrecherche-rechtsprechung-literatur/SKILL.md), [`seminararbeiten-dokumentenmatrix-und-lueckenliste`](skills/seminararbeiten-dokumentenmatrix-und-lueckenliste/SKILL.md), [`spezial-oeffentliches-livequellen-und-rechtsprechungscheck`](skills/spezial-oeffentliches-livequellen-und-rechtsprechungscheck/SKILL.md), [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md), [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md), [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`fuehrt-risikoampel-und-gegenargumente`](skills/fuehrt-risikoampel-und-gegenargumente/SKILL.md), [`haus-plagiatscheck-themaeingrenzung`](skills/haus-plagiatscheck-themaeingrenzung/SKILL.md), [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md), [`strafrecht-tatbestand-rechtswidrigkeit-schuld`](skills/strafrecht-tatbestand-rechtswidrigkeit-schuld/SKILL.md), [`subsumtion-schritt-verfassungsrecht`](skills/subsumtion-schritt-verfassungsrecht/SKILL.md), [`verfassungsrecht-grundrechtspruefung`](skills/verfassungsrecht-grundrechtspruefung/SKILL.md), [`zivilrecht-anspruchsgrundlagen-pruefung`](skills/zivilrecht-anspruchsgrundlagen-pruefung/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`bearbeitungsplan-erstellen`](skills/bearbeitungsplan-erstellen/SKILL.md), [`gliederung-mit-tiefenstruktur`](skills/gliederung-mit-tiefenstruktur/SKILL.md), [`professor-erkennen-und-strategie`](skills/professor-erkennen-und-strategie/SKILL.md), [`strategie-fehlerkatalog`](skills/strategie-fehlerkatalog/SKILL.md), [`zivilrecht-verhandlung-vergleich-und-eskalation`](skills/zivilrecht-verhandlung-vergleich-und-eskalation/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`durch-schriftsatz-brief-und-memo-bausteine`](skills/durch-schriftsatz-brief-und-memo-bausteine/SKILL.md), [`hausarbeiten-fristen-form-und-zustaendigkeit`](skills/hausarbeiten-fristen-form-und-zustaendigkeit/SKILL.md), [`sokratisch-behoerden-gericht-und-registerweg`](skills/sokratisch-behoerden-gericht-und-registerweg/SKILL.md), [`spezial-durch-schriftsatz-brief-und-memo-bausteine`](skills/spezial-durch-schriftsatz-brief-und-memo-bausteine/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`output-waehlen`](skills/output-waehlen/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`behutsame-frech-haeufige-fehler`](skills/behutsame-frech-haeufige-fehler/SKILL.md), [`haeufige-fehler-vermeiden`](skills/haeufige-fehler-vermeiden/SKILL.md), [`selbstkontrolle-vor-abgabe`](skills/selbstkontrolle-vor-abgabe/SKILL.md), [`spezial-strategie-red-team-und-qualitaetskontrolle`](skills/spezial-strategie-red-team-und-qualitaetskontrolle/SKILL.md), [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`aufgabenstellung-erfassen-fachgebiet`](skills/aufgabenstellung-erfassen-fachgebiet/SKILL.md), [`ausfluegen-didaktisches-durch`](skills/ausfluegen-didaktisches-durch/SKILL.md), [`europarecht-anwendbarkeit-hausarbeiten`](skills/europarecht-anwendbarkeit-hausarbeiten/SKILL.md), [`europarecht-interessen-fertigen-sonderfall`](skills/europarecht-interessen-fertigen-sonderfall/SKILL.md), [`fertigen-sonderfall-und-edge-case`](skills/fertigen-sonderfall-und-edge-case/SKILL.md), [`haus-fussnotenstil-spezial`](skills/haus-fussnotenstil-spezial/SKILL.md), [`haus-themaeingrenzung-bauleiter`](skills/haus-themaeingrenzung-bauleiter/SKILL.md), [`meinungsstreit-darstellen`](skills/meinungsstreit-darstellen/SKILL.md), [`methodenlehre-auslegung-oeffentliches`](skills/methodenlehre-auslegung-oeffentliches/SKILL.md), [`oeffentliches-recht-statthaft-zulaessig-begruendet`](skills/oeffentliches-recht-statthaft-zulaessig-begruendet/SKILL.md), [`rechtstheorie-internationaler-bezug-und-schnittstellen`](skills/rechtstheorie-internationaler-bezug-und-schnittstellen/SKILL.md), [`rechtstheorie-rechtsphilosophie-seminararbeit`](skills/rechtstheorie-rechtsphilosophie-seminararbeit/SKILL.md), [`schleimerei-seminararbeiten-sokratisch`](skills/schleimerei-seminararbeiten-sokratisch/SKILL.md), [`seminararbeit-modus`](skills/seminararbeit-modus/SKILL.md), [`strafrecht-zivilrecht-rechtswidrigkeit`](skills/strafrecht-zivilrecht-rechtswidrigkeit/SKILL.md), [`zitierweise-jura-fundstellen`](skills/zitierweise-jura-fundstellen/SKILL.md) |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Jeder Skillname öffnet die zugehörige `SKILL.md`; Beschreibungen stammen aus deren `description`-Feld.

| Skill | Beschreibung |
| --- | --- |
| [`adressaten-formular-portal-und-einreichung`](skills/adressaten-formular-portal-und-einreichung/SKILL.md) | Wenn es um Adressaten: Formular, Portal und Einreichungslogik in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit So... |
| [`anschluss-routing`](skills/anschluss-routing/SKILL.md) | Wenn es um Anschluss-Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`aufgabenstellung-erfassen-fachgebiet`](skills/aufgabenstellung-erfassen-fachgebiet/SKILL.md) | Wenn es um Aufgabenstellung erfassen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`ausfluegen-didaktisches-durch`](skills/ausfluegen-didaktisches-durch/SKILL.md) | Wenn es um Ausfluegen: Compliance-Dokumentation und Aktenvermerk in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| [`bearbeitungsplan-erstellen`](skills/bearbeitungsplan-erstellen/SKILL.md) | Wenn es um Bearbeitungs-Plan erstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`behutsame-frech-haeufige-fehler`](skills/behutsame-frech-haeufige-fehler/SKILL.md) | Wenn es um Behutsame, frech-wertschätzende Rückfragen — Stil-Anleitung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoamp... |
| [`didaktisches-erstpruefung-und-mandatsziel`](skills/didaktisches-erstpruefung-und-mandatsziel/SKILL.md) | Wenn es um Didaktisches: Erstprüfung, Rollenklärung und Mandatsziel in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Ri... |
| [`dokumente-intake`](skills/dokumente-intake/SKILL.md) | Wenn es um Dokumentenintake in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`durch-schriftsatz-brief-und-memo-bausteine`](skills/durch-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Schriftsatz-, Brief- und Memo-Bausteine (Hausarbeiten) in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwu... |
| [`einstieg-routing`](skills/einstieg-routing/SKILL.md) | Wenn es um Einstieg und Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`europarecht-anwendbarkeit-hausarbeiten`](skills/europarecht-anwendbarkeit-hausarbeiten/SKILL.md) | Wenn es um Europarecht — Anwendbarkeit, Vorrang, Vorabentscheidung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| [`europarecht-interessen-fertigen-sonderfall`](skills/europarecht-interessen-fertigen-sonderfall/SKILL.md) | Wenn es um Europarecht: Mehrparteienkonflikt und Interessenmatrix in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mi... |
| [`fachgebiet-routing-zivil-oeffentlich-straf`](skills/fachgebiet-routing-zivil-oeffentlich-straf/SKILL.md) | Wenn es um Fachgebiet-Routing: Zivilrecht — Öffentliches Recht — Strafrecht in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen... |
| [`fertigen-sonderfall-und-edge-case`](skills/fertigen-sonderfall-und-edge-case/SKILL.md) | Wenn es um Fertigen: Sonderfall und Edge-Case-Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| [`fuehrt-risikoampel-und-gegenargumente`](skills/fuehrt-risikoampel-und-gegenargumente/SKILL.md) | Wenn es um Fuehrt: Risikoampel, Gegenargumente und Verteidigungslinien in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risi... |
| [`gliederung-mit-tiefenstruktur`](skills/gliederung-mit-tiefenstruktur/SKILL.md) | Wenn es um Gliederung mit Tiefen-Struktur in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`gutachtenstil-vs-haus-fussnotenstil`](skills/gutachtenstil-vs-haus-fussnotenstil/SKILL.md) | Wenn es um Gutachtenstil und Urteilsstil in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haeufige-fehler-vermeiden`](skills/haeufige-fehler-vermeiden/SKILL.md) | Wenn es um Häufige Fehler vermeiden — Top-20 in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haus-fussnotenstil-spezial`](skills/haus-fussnotenstil-spezial/SKILL.md) | Wenn es um Haus: Fussnotenstil in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haus-literaturrecherche-leitfaden`](skills/haus-literaturrecherche-leitfaden/SKILL.md) | Wenn es um Haus: Literaturrecherche in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haus-plagiatscheck-themaeingrenzung`](skills/haus-plagiatscheck-themaeingrenzung/SKILL.md) | Wenn es um Haus: Plagiatscheck Eigenstaendigkeit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`haus-themaeingrenzung-bauleiter`](skills/haus-themaeingrenzung-bauleiter/SKILL.md) | Wenn es um Haus: Themaeingrenzung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hausarbeit-quellenrecherche-rspr-literatur`](skills/hausarbeit-quellenrecherche-rspr-literatur/SKILL.md) | Wenn es um Fristen- und Risikoampel in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hausarbeit-start`](skills/hausarbeit-start/SKILL.md) | Wenn es um Hausarbeitenmacher — Allgemein in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`hausarbeit-workflow-start`](skills/hausarbeit-workflow-start/SKILL.md) | Wenn es um Master-Hausarbeiten- und Seminararbeitenmacher in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| [`hausarbeiten-fristen-form-und-zustaendigkeit`](skills/hausarbeiten-fristen-form-und-zustaendigkeit/SKILL.md) | Wenn es um Hausarbeiten: Fristen, Form, Zuständigkeit und Rechtsweg in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel... |
| [`juristische-liefert-beweislast-rechtstheorie`](skills/juristische-liefert-beweislast-rechtstheorie/SKILL.md) | Wenn es um Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierun... |
| [`juristischer-argumentationskern`](skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Hausarbeitenmacher ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. |
| [`liefert-beweislast-und-darlegungslast`](skills/liefert-beweislast-und-darlegungslast/SKILL.md) | Wenn es um Liefert: Beweislast, Darlegungslast und Substantiierung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| [`meinungsstreit-darstellen`](skills/meinungsstreit-darstellen/SKILL.md) | Wenn es um Meinungsstreit darstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`methodenlehre-auslegung-oeffentliches`](skills/methodenlehre-auslegung-oeffentliches/SKILL.md) | Wenn es um Methodenlehre und Auslegung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`oeffentliches-quellenkarte`](skills/oeffentliches-quellenkarte/SKILL.md) | Wenn es um Oeffentliches Quellenkarte in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`oeffentliches-recht-statthaft-zulaessig-begruendet`](skills/oeffentliches-recht-statthaft-zulaessig-begruendet/SKILL.md) | Wenn es um Öffentliches Recht — Statthaftigkeit, Zulässigkeit, Begründetheit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen-... |
| [`output-waehlen`](skills/output-waehlen/SKILL.md) | Wenn es um Output wählen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`professor-erkennen-und-strategie`](skills/professor-erkennen-und-strategie/SKILL.md) | Wenn es um Professor erkennen und Strategie wählen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`quellen-livecheck`](skills/quellen-livecheck/SKILL.md) | Wenn es um Rechtsquellen-Livecheck in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargum... |
| [`quellenrecherche-rechtsprechung-literatur`](skills/quellenrecherche-rechtsprechung-literatur/SKILL.md) | Wenn es um Quellen-Recherche — Rechtsprechung und Literatur in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| [`rechtstheorie-internationaler-bezug-und-schnittstellen`](skills/rechtstheorie-internationaler-bezug-und-schnittstellen/SKILL.md) | Wenn es um Rechtstheorie: Internationaler Bezug und Schnittstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| [`rechtstheorie-rechtsphilosophie-seminararbeit`](skills/rechtstheorie-rechtsphilosophie-seminararbeit/SKILL.md) | Wenn es um Rechtstheorie und Rechtsphilosophie — Anbindung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofor... |
| [`schleimerei-seminararbeiten-sokratisch`](skills/schleimerei-seminararbeiten-sokratisch/SKILL.md) | Wenn es um Schleimerei: Mandantenkommunikation und Entscheidungsvorlage in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoam... |
| [`selbstkontrolle-vor-abgabe`](skills/selbstkontrolle-vor-abgabe/SKILL.md) | Wenn es um Selbst-Kontrolle vor Abgabe in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`seminararbeit-modus`](skills/seminararbeit-modus/SKILL.md) | Wenn es um Seminararbeit-Modus in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`seminararbeiten-dokumentenmatrix-und-lueckenliste`](skills/seminararbeiten-dokumentenmatrix-und-lueckenliste/SKILL.md) | Wenn es um Seminararbeiten: Dokumentenmatrix, Lückenliste und Nachforderung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachf... |
| [`sokratisch-behoerden-gericht-und-registerweg`](skills/sokratisch-behoerden-gericht-und-registerweg/SKILL.md) | Wenn es um Sokratisch: Behörden-, Gerichts- oder Registerweg in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| [`spezial-durch-schriftsatz-brief-und-memo-bausteine`](skills/spezial-durch-schriftsatz-brief-und-memo-bausteine/SKILL.md) | Wenn es um Durch: Schriftsatz-, Brief- und Memo-Bausteine in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit A... |
| [`spezial-oeffentliches-livequellen-und-rechtsprechungscheck`](skills/spezial-oeffentliches-livequellen-und-rechtsprechungscheck/SKILL.md) | Wenn es um Oeffentliches: Livequellen- und Rechtsprechungscheck in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| [`spezial-strategie-red-team-und-qualitaetskontrolle`](skills/spezial-strategie-red-team-und-qualitaetskontrolle/SKILL.md) | Wenn es um Strategie: Red-Team und Qualitätskontrolle in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofor... |
| [`strafrecht-tatbestand-rechtswidrigkeit-schuld`](skills/strafrecht-tatbestand-rechtswidrigkeit-schuld/SKILL.md) | Wenn es um Strafrecht — Drei-Stufen-Aufbau: Tatbestand, Rechtswidrigkeit, Schuld in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und... |
| [`strafrecht-zivilrecht-rechtswidrigkeit`](skills/strafrecht-zivilrecht-rechtswidrigkeit/SKILL.md) | Wenn es um Strafrecht: Zahlen, Schwellenwerte und Berechnung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwelle... |
| [`strategie-fehlerkatalog`](skills/strategie-fehlerkatalog/SKILL.md) | Wenn es um Strategie Fehlerkatalog in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`subsumtion-schritt-verfassungsrecht`](skills/subsumtion-schritt-verfassungsrecht/SKILL.md) | Wenn es um Subsumtion Schritt für Schritt in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`unterlagen-luecken`](skills/unterlagen-luecken/SKILL.md) | Wenn es um Unterlagen und Lücken in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`verfassungsrecht-grundrechtspruefung`](skills/verfassungsrecht-grundrechtspruefung/SKILL.md) | Wenn es um Verfassungsrecht — Grundrechts-Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-chronologie-und-belegmatrix`](skills/workflow-chronologie-und-belegmatrix/SKILL.md) | Wenn es um Chronologie und Belegmatrix in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| [`workflow-kaltstart-und-routing`](skills/workflow-kaltstart-und-routing/SKILL.md) | Wenn es um Kaltstart und Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-redteam-qualitygate`](skills/workflow-redteam-qualitygate/SKILL.md) | Wenn es um Red-Team Qualitygate in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`workflow-unterlagen-lueckenliste`](skills/workflow-unterlagen-lueckenliste/SKILL.md) | Wenn es um Unterlagen- und Lückenliste in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| [`zitierweise-jura-fundstellen`](skills/zitierweise-jura-fundstellen/SKILL.md) | Wenn es um Zitierweise in der juristischen Hausarbeit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| [`zivilrecht-anspruchsgrundlagen-pruefung`](skills/zivilrecht-anspruchsgrundlagen-pruefung/SKILL.md) | Wenn es um Zivilrecht Anspruchsgrundlagen Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| [`zivilrecht-verhandlung-vergleich-und-eskalation`](skills/zivilrecht-verhandlung-vergleich-und-eskalation/SKILL.md) | Wenn es um Zivilrecht: Verhandlung, Vergleich und Eskalation in hausarbeitenmacher — Didaktisches Plugin für juristische geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalatio... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
