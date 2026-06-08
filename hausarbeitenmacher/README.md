# hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`hausarbeitenmacher`) | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Hausarbeit BGB Übung Fortgeschrittene — Pohlmann / Leipzig / SS 26** (`hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung`) | [Gesamt-PDF lesen](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/gesamt-pdf/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung_gesamt.pdf) | [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für Studierende der Rechtswissenschaft, das durch das Erstellen einer **Hausarbeit oder Seminararbeit lernfördernd** hindurchführt. Es liefert **keine fertigen Lösungen**, sondern stellt Fragen, gibt Strukturen, Methoden-Hinweise und Zitierweise — Du subsumierst selbst.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
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

**Du als Studierende oder Studierender.** Du gibst Deine Aufgabenstellung ein und gehst Schritt für Schritt durch die Lösung. Das Plugin

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

Das Plugin ist ein **Lern- und Trainingswerkzeug** für Studierende, Tutor/-innen und Lehrkräfte. Es ist ausdrücklich **nicht** dafür gedacht, irgendeinen vom Plugin generierten Text (Subsumtion, Gliederungs-Vorschlag, Argumentations-Skizze, Probe-Gutachten) **als eigene Leistung** in einer Hausarbeit, Seminararbeit, Klausur, Aktenklausur, mündlichen Prüfung oder im juristischen Vorbereitungsdienst einzureichen. Das wäre ein **Täuschungsversuch** im Sinne der jeweiligen Prüfungsordnung der Universitäten bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder. Folge ist regelmäßig **Nichtbestehen, Aberkennung der Prüfung oder disziplinarrechtliche Konsequenzen**. Der erlaubte Lernweg: erst selbst denken und schreiben, dann mit dem Plugin gegenprüfen, hinterfragen und verbessern lassen.

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


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adressaten-formular-portal-und-einreichung` | Adressaten: Formular, Portal und Einreichungslogik im Hausarbeitenmacher. |
| `anschluss-routing` | Anschluss-Routing für Jura-Hausarbeiten: wählt den nächsten Spezial-Skill nach Engpass (Hausarbeits-Abgabefrist, Sachverhalt, Literaturverzeichnis, Gliederung), dokumentiert Router-Entscheidung mit Begründung. |
| `aufgabenstellung-erfassen-fachgebiet` | Student erhaelt Hausarbeit-Aufgabenstellung und will den Sachverhalt strukturiert erfassen. Drei-Lese-Methode zerlegt Sachverhalt in wesentliche Tatsachen Beteiligte Zeitschiene. Bearbeitungsvermerk identifizieren wer fragt was wird gepr... |
| `ausfluegen-didaktisches-durch` | Ausfluegen: Compliance-Dokumentation und Aktenvermerk im Hausarbeitenmacher. |
| `bearbeitungsplan-erstellen` | Student erstellt Zeitplan und Arbeitsplan für juristische Hausarbeit: Recherche Gliederung Rohfassung Endfassung Korrektur. Differenziert nach Hausarbeitstyp Anfaengeruebung Fortgeschrittenenuebung Examenshausarbeit. Normen Prüfungsordnu... |
| `behutsame-frech-haeufige-fehler` | Stil-Anleitung für den Dialog-Ton des Plugins: behutsam unterhaltsam ketzerisch wertschaetzend niemals herablassend. Trockenes Staunen alltagsphilosophische Beobachtung selbstironische Wendung scheinbar naive Nachfrage. Kein Dauerton nur... |
| `didaktisches-erstpruefung-und-mandatsziel` | Didaktisches: Erstprüfung, Rollenklärung und Mandatsziel im Hausarbeitenmacher. |
| `dokumente-intake` | Dokumentenintake für Jura-Hausarbeiten: sortiert Sachverhalt, Literaturverzeichnis, Gliederung, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `durch-schriftsatz-brief-und-memo-bausteine` | Durch: Schriftsatz-, Brief- und Memo-Bausteine im Hausarbeitenmacher. |
| `einstieg-routing` | Einstieg, Triage und Routing für Jura-Hausarbeiten: ordnet Rolle (Studierender, Korrektor), markiert Frist (Hausarbeits-Abgabefrist), wählt Norm (BGB AT/BT, StGB AT/BT, GG, ZPO/StPO/VwGO) und Zuständigkeit (Universitäre Prüfungsämter), l... |
| `europarecht-anwendbarkeit-hausarbeiten` | Student bearbeitet Hausarbeit mit Europarecht-Bezug: Anwendungsvorrang Verordnung direkt anwendbar Richtlinie richtlinienkonforme Auslegung Vorabentscheidungsverfahren. Art. 267 AEUV Marleasing EuGH-Linien Grundfreiheiten Grundrechte-Cha... |
| `europarecht-interessen-fertigen-sonderfall` | Europarecht: Mehrparteienkonflikt und Interessenmatrix im Hausarbeitenmacher. |
| `fachgebiet-routing-zivil-oeffentlich-straf` | Student weiss nicht in welches Fachgebiet die Hausarbeit faellt: Zivilrecht öffentliches Recht Strafrecht oder Mix. Routing-Skill klaert Fachgebiet anhand Indikatoren. Normen allgemein BGB HGB VwGO StGB je nach Gebiet. Prüfraster Fachgeb... |
| `fertigen-sonderfall-und-edge-case` | Fertigen: Sonderfall und Edge-Case-Prüfung im Hausarbeitenmacher. |
| `fuehrt-risikoampel-und-gegenargumente` | Fuehrt: Risikoampel, Gegenargumente und Verteidigungslinien im Hausarbeitenmacher. |
| `gliederung-mit-tiefenstruktur` | Student erstellt Gliederung für juristische Hausarbeit mit korrekter Tiefenstruktur A Roemisch Arabisch Kleinbuchstaben. Anspruchsgrundlagen-Reihenfolge Zivilrecht öffentlich-rechtlicher Aufbau Strafrecht Drei-Stufen. Normen §§ 133 157 B... |
| `gutachtenstil-vs-haus-fussnotenstil` | Student ist unsicher ob Gutachtenstil oder Urteilsstil anzuwenden ist. Gutachtenstil Obersatz Definition Subsumtion Ergebnis konjunktivisch prüfend. Urteilsstil indikativ direkt begründungsknapp. Normen Methodenlehre Aufsatz-Tradition. P... |
| `haeufige-fehler-vermeiden` | Student will typische Fehler in juristischen Hausarbeiten vermeiden: methodische stilistische formale Fehler. Liste der 20 häufigsten Fehler mit Korrekturhinweisen. Normen Methodenlehre Zitierstandards. Prüfraster Fehlertypen-Scan Selbst... |
| `haus-fussnotenstil-spezial` | Spezialfall Fussnotenstil deutsche Jurahausarbeit: Erstzitat, Folgezitat, ebenda, aaO, Mehrfachverweis. Pruefraster für einheitliche Zitierweise im Hausarbeitenmacher. |
| `haus-literaturrecherche-leitfaden` | Leitfaden Literaturrecherche: Kommentar, Lehrbuch, Aufsatz, Rechtsprechung dejure.org / openjur.de. Pruefraster für Querschnitts- und Spezialthemen im Hausarbeitenmacher. |
| `haus-plagiatscheck-themaeingrenzung` | Spezialfall Plagiatscheck und Eigenstaendigkeitserklaerung: Selbstplagiat, KI-Nutzung, Pruefungsrecht, Tools. Pruefraster für Pruefungsamt und Studierende im Hausarbeitenmacher. |
| `haus-themaeingrenzung-bauleiter` | Bauleiter Themaeingrenzung Hausarbeit: Forschungsfrage, Gliederungsentwurf, Literatursichtung. Pruefraster für Erstsemester und Examenskandidaten im Hausarbeitenmacher. |
| `hausarbeit-quellenrecherche-rspr-literatur` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Hausarbeitenmacher. |
| `hausarbeit-start` | Einstieg, Schnelltriage und Fallrouting im Hausarbeitenmacher-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `hausarbeit-workflow-start` | Student beginnt Hausarbeit und braucht vollständige Begleitung von Anfang bis Abgabe. Master-Prüfungslinie: Fangfrage Lehrkraft Aufgabenstellung Routing Methode Fachgebiet Subsumtion Endkontrolle. Normen je nach… im Hausarbeitenmacher. |
| `hausarbeiten-fristen-form-und-zustaendigkeit` | Hausarbeiten: Fristen, Form, Zuständigkeit und Rechtsweg im Hausarbeitenmacher. |
| `juristische-liefert-beweislast-rechtstheorie` | Juristische: Tatbestandsmerkmale, Beweisfragen und Beleglage im Hausarbeitenmacher. |
| `liefert-beweislast-und-darlegungslast` | Liefert: Beweislast, Darlegungslast und Substantiierung im Hausarbeitenmacher. |
| `meinungsstreit-darstellen` | Student muss Meinungsstreit in Hausarbeit darstellen: herrschende Meinung Mindermeinungen Argumente pro contra eigene Stellungnahme. Normen Methodenlehre wissenschaftliche Argumentation. Prüfraster Meinungs-Katalog Argument-Zuordnung Ste... |
| `methodenlehre-auslegung-oeffentliches` | Student braucht Anleitung zu den vier Auslegungsmethoden grammatikalisch systematisch historisch teleologisch plus verfassungs- und EU-rechtskonforme Auslegung. Rechtsfortbildung Analogie teleologische Reduktion. Normen §§ 133 157 BGB Ar... |
| `oeffentliches-quellenkarte` | Oeffentliches Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `oeffentliches-recht-statthaft-zulaessig-begruendet` | Student bearbeitet öffentlich-rechtliche Klage in der Hausarbeit: Statthaftigkeit Zulässigkeit Begründetheit. VwGO §§ 40 42 47 113 BVerfGG Verfassungsbeschwerde Normenkontrolle. Prüfraster Klagearten Anfechtungs- Verpflichtungs- Leistung... |
| `output-waehlen` | Output-Wahl für Jura-Hausarbeiten: stimmt Adressat (Studierender, Korrektor), Frist (Hausarbeits-Abgabefrist) und Form auf den Zweck ab — typische Outputs: Gutachten im Gutachtenstil, Literaturverzeichnis, Gliederung. |
| `professor-erkennen-und-strategie` | Student fragt sich ob er der Lehrmeinung des Professors folgen soll oder eigenständig argumentieren. Fangfrage zu Beginn wer die Hausarbeit bewertet. Kurze Recherche zur Lehrmeinung. Normen Wissenschaftsfreiheit Art. 5 GG. Prüfraster Leh... |
| `quellen-livecheck` | Quellen-Live-Check für Jura-Hausarbeiten: prüft Normen (BGB AT/BT, StGB AT/BT, GG, ZPO/StPO/VwGO) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Universitäre Prüfungsämter und Quellenhygiene nach references/quell... |
| `quellenrecherche-rechtsprechung-literatur` | Student sucht juristische Quellen für Hausarbeit: amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang dejure openJur EUR-Lex Bibliotheksbestand. Frei verfuegbare Alternativen ohne Zugang. Normen Zitierstandards.... |
| `rechtstheorie-internationaler-bezug-und-schnittstellen` | Rechtstheorie: Internationaler Bezug und Schnittstellen im Hausarbeitenmacher. |
| `rechtstheorie-rechtsphilosophie-seminararbeit` | Student schreibt Hausarbeit mit rechtstheoretischem Bezug: Positivismus Naturrecht Kelsen Hart Dworkin Radbruch Alexy. Geltungsgrund Rechtsbegriff Auslegung Gerechtigkeit. Normen Art. 20 GG Rechtsstaatsprinzip. Prüfraster Theorien-Zuordn... |
| `schleimerei-seminararbeiten-sokratisch` | Schleimerei: Mandantenkommunikation und Entscheidungsvorlage im Hausarbeitenmacher. |
| `selbstkontrolle-vor-abgabe` | Student prüft Hausarbeit vor Abgabe auf inhaltliche und formale Vollständigkeit. Zwei Durchgaenge Lernziel-Selbstprüfung Plagiat-Check Aktualitaet Zitierweise Gliederung. Normen Zitierstandards Prüfungsordnungen. Prüfraster Inhalt-Checkl... |
| `seminararbeit-modus` | Student schreibt Seminararbeit mit persönlicher Lekture durch Lehrkraft: Forschungsfrage Literaturschau eigene These Disputation. Unterschied zur Hausarbeit hoehere Eigenständigkeit wissenschaftliche Tiefe Vortragspflicht. Normen Wissens... |
| `seminararbeiten-dokumentenmatrix-und-lueckenliste` | Seminararbeiten: Dokumentenmatrix, Lückenliste und Nachforderung im Hausarbeitenmacher. |
| `sokratisch-behoerden-gericht-und-registerweg` | Sokratisch: Behörden-, Gerichts- oder Registerweg im Hausarbeitenmacher. |
| `strafrecht-tatbestand-rechtswidrigkeit-schuld` | Student prüft Strafbarkeit in der Hausarbeit: Drei-Stufen-Schema Tatbestand Rechtswidrigkeit Schuld. Objektiver subjektiver Tatbestand Rechtfertigungsgründe Schuldfähigkeit. §§ 242 263 223 212 StGB Versuch § 22 StGB Rücktritt § 24 StGB K... |
| `strafrecht-zivilrecht-rechtswidrigkeit` | Strafrecht: Zahlen, Schwellenwerte und Berechnung im Hausarbeitenmacher. |
| `strategie-fehlerkatalog` | Strategie Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `subsumtion-schritt-verfassungsrecht` | Student uebrt die Subsumtion Schritt für Schritt: Tatbestandsmerkmal Definition Sachverhalts-Tatsache Ergebnis sauber trennen. Sokratisches Führen statt Vorgeben gentle Umlenkung bei Fehlern. Normen Methodenlehre §§ 133 157 BGB. Prüfrast... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Jura-Hausarbeiten: trennt fehlende Tatsachen von fehlenden Belegen (Sachverhalt, Literaturverzeichnis, Gliederung), nennt pro Lücke Beweisthema, Beschaffungsweg (Universitäre Prüfungsämter), Frist und Er... |
| `verfassungsrecht-grundrechtspruefung` | Student prüft Grundrechte in der Hausarbeit: Schutzbereich Eingriff verfassungsrechtliche Rechtfertigung Verhältnismäßigkeit. Art. 1-19 GG Drittwirkung mittelbar Schranken-Schranken. Normen GG Art. 1 2 3 4 5 8 12 14. Prüfraster Drei-Schr... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Hausarbeitenmacher. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Hausarbeitenmacher. |
| `zitierweise-jura-fundstellen` | Zitierweise für juristische Hausarbeiten mit strikter Quellenprüfung. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle. Literatur, Kommentare, Lehrbücher und Aufsätze nur, wenn der Student... |
| `zivilrecht-anspruchsgrundlagen` | Zivilrecht Anspruchsgrundlagen im Juristische Hausarbeit im Hausarbeitenmacher. |
| `zivilrecht-verhandlung-vergleich-und-eskalation` | Zivilrecht: Verhandlung, Vergleich und Eskalation im Hausarbeitenmacher. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
