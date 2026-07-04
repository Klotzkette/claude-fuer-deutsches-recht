# hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`hausarbeitenmacher`) | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Hausarbeit BGB Übung Fortgeschrittene — Pohlmann / Leipzig / SS 26** (`hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung`) | [Gesamt-PDF lesen](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/gesamt-pdf/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung_gesamt.pdf) | [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausflügen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion.

Dieses Plugin gehört zum Marketplace mit 233 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/hausarbeitenmacher/hausarbeitenmacher-werkstatt.md" download><code>hausarbeitenmacher-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/hausarbeitenmacher/hausarbeitenmacher-schnellstart.md" download><code>hausarbeitenmacher-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Hausarbeit BGB Übung Fortgeschrittene — Pohlmann / Leipzig / SS 26: [Gesamt-PDF](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/gesamt-pdf/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung_gesamt.pdf), [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip), [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 233 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
| 1. Einstieg und Fallrouting | `anschluss-routing`, `didaktisches-erstpruefung-und-mandatsziel`, `dokumente-intake`, `einstieg-routing`, `fachgebiet-routing-zivil-oeffentlich-straf`, `hausarbeit-start`, `hausarbeit-workflow-start`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `adressaten-formular-portal-und-einreichung`, `gutachtenstil-vs-haus-fussnotenstil`, `haus-literaturrecherche-leitfaden`, `hausarbeit-quellenrecherche-rspr-literatur`, `juristische-liefert-beweislast-rechtstheorie`, `liefert-beweislast-und-darlegungslast`, `oeffentliches-quellenkarte`, `quellen-livecheck`, `quellenrecherche-rechtsprechung-literatur`, `seminararbeiten-dokumentenmatrix-und-lueckenliste`, `spezial-oeffentliches-livequellen-und-rechtsprechungscheck`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste` |
| 3. Prüfung, Anspruch und Subsumtion | `fuehrt-risikoampel-und-gegenargumente`, `haus-plagiatscheck-themaeingrenzung`, `strafrecht-tatbestand-rechtswidrigkeit-schuld`, `subsumtion-schritt-verfassungsrecht`, `verfassungsrecht-grundrechtspruefung`, `zivilrecht-anspruchsgrundlagen-pruefung` |
| 4. Gestaltung, Strategie und Verhandlung | `bearbeitungsplan-erstellen`, `gliederung-mit-tiefenstruktur`, `professor-erkennen-und-strategie`, `strategie-fehlerkatalog`, `zivilrecht-verhandlung-vergleich-und-eskalation` |
| 5. Verfahren, Behörde und Gericht | `durch-schriftsatz-brief-und-memo-bausteine`, `hausarbeiten-fristen-form-und-zustaendigkeit`, `sokratisch-behoerden-gericht-und-registerweg`, `spezial-durch-schriftsatz-brief-und-memo-bausteine` |
| 6. Ergebnis, Schreiben und Kommunikation | `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `behutsame-frech-haeufige-fehler`, `haeufige-fehler-vermeiden`, `selbstkontrolle-vor-abgabe`, `spezial-strategie-red-team-und-qualitaetskontrolle`, `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `aufgabenstellung-erfassen-fachgebiet`, `ausfluegen-didaktisches-durch`, `europarecht-anwendbarkeit-hausarbeiten`, `europarecht-interessen-fertigen-sonderfall`, `fertigen-sonderfall-und-edge-case`, `haus-fussnotenstil-spezial`, `haus-themaeingrenzung-bauleiter`, `meinungsstreit-darstellen`, `methodenlehre-auslegung-oeffentliches`, `oeffentliches-recht-statthaft-zulaessig-begruendet`, `rechtstheorie-internationaler-bezug-und-schnittstellen`, `rechtstheorie-rechtsphilosophie-seminararbeit`, `schleimerei-seminararbeiten-sokratisch`, `seminararbeit-modus`, `strafrecht-zivilrecht-rechtswidrigkeit`, `zitierweise-jura-fundstellen` |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adressaten-formular-portal-und-einreichung` | Wenn es um Adressaten: Formular, Portal und Einreichungslogik in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit So... |
| `anschluss-routing` | Wenn es um Anschluss-Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `aufgabenstellung-erfassen-fachgebiet` | Wenn es um Aufgabenstellung erfassen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `ausfluegen-didaktisches-durch` | Wenn es um Ausfluegen: Compliance-Dokumentation und Aktenvermerk in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Pr... |
| `bearbeitungsplan-erstellen` | Wenn es um Bearbeitungs-Plan erstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `behutsame-frech-haeufige-fehler` | Wenn es um Behutsame, frech-wertschätzende Rückfragen — Stil-Anleitung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoamp... |
| `didaktisches-erstpruefung-und-mandatsziel` | Wenn es um Didaktisches: Erstprüfung, Rollenklärung und Mandatsziel in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Ri... |
| `dokumente-intake` | Wenn es um Dokumentenintake in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `durch-schriftsatz-brief-und-memo-bausteine` | Wenn es um Schriftsatz-, Brief- und Memo-Bausteine (Hausarbeiten) in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwu... |
| `einstieg-routing` | Wenn es um Einstieg und Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `europarecht-anwendbarkeit-hausarbeiten` | Wenn es um Europarecht — Anwendbarkeit, Vorrang, Vorabentscheidung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| `europarecht-interessen-fertigen-sonderfall` | Wenn es um Europarecht: Mehrparteienkonflikt und Interessenmatrix in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mi... |
| `fachgebiet-routing-zivil-oeffentlich-straf` | Wenn es um Fachgebiet-Routing: Zivilrecht — Öffentliches Recht — Strafrecht in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen... |
| `fertigen-sonderfall-und-edge-case` | Wenn es um Fertigen: Sonderfall und Edge-Case-Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschr... |
| `fuehrt-risikoampel-und-gegenargumente` | Wenn es um Fuehrt: Risikoampel, Gegenargumente und Verteidigungslinien in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risi... |
| `gliederung-mit-tiefenstruktur` | Wenn es um Gliederung mit Tiefen-Struktur in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `gutachtenstil-vs-haus-fussnotenstil` | Wenn es um Gutachtenstil und Urteilsstil in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haeufige-fehler-vermeiden` | Wenn es um Häufige Fehler vermeiden — Top-20 in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haus-fussnotenstil-spezial` | Wenn es um Haus: Fussnotenstil in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haus-literaturrecherche-leitfaden` | Wenn es um Haus: Literaturrecherche in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haus-plagiatscheck-themaeingrenzung` | Wenn es um Haus: Plagiatscheck Eigenstaendigkeit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `haus-themaeingrenzung-bauleiter` | Wenn es um Haus: Themaeingrenzung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hausarbeit-quellenrecherche-rspr-literatur` | Wenn es um Fristen- und Risikoampel in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hausarbeit-start` | Wenn es um Hausarbeitenmacher — Allgemein in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `hausarbeit-workflow-start` | Wenn es um Master-Hausarbeiten- und Seminararbeitenmacher in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofort... |
| `hausarbeiten-fristen-form-und-zustaendigkeit` | Wenn es um Hausarbeiten: Fristen, Form, Zuständigkeit und Rechtsweg in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel... |
| `juristische-liefert-beweislast-rechtstheorie` | Wenn es um Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Beweislast- und Substantiierun... |
| `liefert-beweislast-und-darlegungslast` | Wenn es um Liefert: Beweislast, Darlegungslast und Substantiierung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| `meinungsstreit-darstellen` | Wenn es um Meinungsstreit darstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `methodenlehre-auslegung-oeffentliches` | Wenn es um Methodenlehre und Auslegung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `oeffentliches-quellenkarte` | Wenn es um Oeffentliches Quellenkarte in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `oeffentliches-recht-statthaft-zulaessig-begruendet` | Wenn es um Öffentliches Recht — Statthaftigkeit, Zulässigkeit, Begründetheit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen-... |
| `output-waehlen` | Wenn es um Output wählen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `professor-erkennen-und-strategie` | Wenn es um Professor erkennen und Strategie wählen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `quellen-livecheck` | Wenn es um Rechtsquellen-Livecheck in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargum... |
| `quellenrecherche-rechtsprechung-literatur` | Wenn es um Quellen-Recherche — Rechtsprechung und Literatur in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofo... |
| `rechtstheorie-internationaler-bezug-und-schnittstellen` | Wenn es um Rechtstheorie: Internationaler Bezug und Schnittstellen in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel m... |
| `rechtstheorie-rechtsphilosophie-seminararbeit` | Wenn es um Rechtstheorie und Rechtsphilosophie — Anbindung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofor... |
| `schleimerei-seminararbeiten-sokratisch` | Wenn es um Schleimerei: Mandantenkommunikation und Entscheidungsvorlage in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoam... |
| `selbstkontrolle-vor-abgabe` | Wenn es um Selbst-Kontrolle vor Abgabe in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `seminararbeit-modus` | Wenn es um Seminararbeit-Modus in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `seminararbeiten-dokumentenmatrix-und-lueckenliste` | Wenn es um Seminararbeiten: Dokumentenmatrix, Lückenliste und Nachforderung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachf... |
| `sokratisch-behoerden-gericht-und-registerweg` | Wenn es um Sokratisch: Behörden-, Gerichts- oder Registerweg in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sof... |
| `spezial-durch-schriftsatz-brief-und-memo-bausteine` | Wenn es um Durch: Schriftsatz-, Brief- und Memo-Bausteine in hausarbeitenmacher — Didaktisches Plugin für juristische geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit A... |
| `spezial-oeffentliches-livequellen-und-rechtsprechungscheck` | Wenn es um Oeffentliches: Livequellen- und Rechtsprechungscheck in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit... |
| `spezial-strategie-red-team-und-qualitaetskontrolle` | Wenn es um Strategie: Red-Team und Qualitätskontrolle in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofor... |
| `strafrecht-tatbestand-rechtswidrigkeit-schuld` | Wenn es um Strafrecht — Drei-Stufen-Aufbau: Tatbestand, Rechtswidrigkeit, Schuld in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und... |
| `strafrecht-zivilrecht-rechtswidrigkeit` | Wenn es um Strafrecht: Zahlen, Schwellenwerte und Berechnung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwelle... |
| `strategie-fehlerkatalog` | Wenn es um Strategie Fehlerkatalog in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `subsumtion-schritt-verfassungsrecht` | Wenn es um Subsumtion Schritt für Schritt in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `unterlagen-luecken` | Wenn es um Unterlagen und Lücken in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `verfassungsrecht-grundrechtspruefung` | Wenn es um Verfassungsrecht — Grundrechts-Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-chronologie-und-belegmatrix` | Wenn es um Chronologie und Belegmatrix in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Chronologie mit Belegmatrix und Widerspruchsliste. |
| `workflow-kaltstart-und-routing` | Wenn es um Kaltstart und Routing in hausarbeitenmacher — Didaktisches Plugin für juristische geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-redteam-qualitygate` | Wenn es um Red-Team Qualitygate in hausarbeitenmacher — Didaktisches Plugin für juristische geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `workflow-unterlagen-lueckenliste` | Wenn es um Unterlagen- und Lückenliste in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `zitierweise-jura-fundstellen` | Wenn es um Zitierweise in der juristischen Hausarbeit in hausarbeitenmacher — Didaktisches Plugin für juristische geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten,... |
| `zivilrecht-anspruchsgrundlagen-pruefung` | Wenn es um Zivilrecht Anspruchsgrundlagen Prüfung in hausarbeitenmacher — Didaktisches Plugin für juristische geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zivilrecht-verhandlung-vergleich-und-eskalation` | Wenn es um Zivilrecht: Verhandlung, Vergleich und Eskalation in hausarbeitenmacher — Didaktisches Plugin für juristische geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalatio... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
