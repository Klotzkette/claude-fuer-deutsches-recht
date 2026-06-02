# Subsumtions-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`subsumtions-pruefer`) | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Subsumtionskontrolle / Klausurkorrektur — Übung für Fortgeschrittene BGB, Uni Bielefeld, Lehrstuhl Pohlmann-Wittfeldt, SS 2026** (`subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann`) | [Gesamt-PDF lesen](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/gesamt-pdf/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann_gesamt.pdf) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Interaktiver Mechanik-Workflow für die juristische Subsumtion nach deutschem Recht und Europarecht. Das Plugin zerlegt Normen in Tatbestandsmerkmale, führt das Vier-Schritt-Schema (Obersatz – Definition – Untersatz – Ergebnis) durch, erfasst Beweisbedarf und erzeugt Ausgabedokumente in verschiedenen Formaten.

**Dieses Plugin ist keine Rechtsberatung.** Es prüft mechanisch eine vom Nutzer behauptete Norm anhand vom Nutzer behaupteter Tatsachen. Die Auswahl der richtigen Norm, die vollständige Sachverhaltsdarstellung und die Bewertung des Ergebnisses bleiben in der Verantwortung des Nutzers und eines zugelassenen Rechtsanwalts.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Subsumtions-Prüfer (`subsumtions-pruefer`, dieses Plugin) | [subsumtions-pruefer.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |

Die URL ist stabil. Alle weiteren Plugins sind unter [Releases](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases) verfügbar.

### Installation

1. ZIP herunterladen (Link oben).
2. Im KI-System: **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP verwenden.

## Für wen ist dieses Plugin

| Rolle | Primäre Anwendungsfälle |
|---|---|
| Privatpersonen | Verstehen, ob ein Anspruch dem Grunde nach bestehen könnte |
| Paralegal / Rechtsfachwirt | Strukturierte Erstsichtung vor anwaltlicher Prüfung |
| Jurastudent / Referendar | Subsumtionsübung ohne Musterlösung |
| Unternehmensjurist | Schnelle Erstprüfung einer Norm vor Mandatserteilung |
| Behördenmitarbeiter | Strukturiertes Durchprüfen von Tatbestandsvoraussetzungen |

## Abgedeckte Rechtsgebiete

- **Deutsches Recht:** BGB (Schuld-, Sachen-, Familien-, Erbrecht), HGB, StGB, StPO, ZPO, VwGO, VwVfG, GG, AO, SGB, KSchG, AGG, GWB, UWG und Nebengesetze
- **BGB AT:** Für Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, Anfechtung, Stellvertretung, Fristen und Verjährung sollte `bgb-at-pruefer` vor oder neben diesem generischen Subsumtions-Plugin geladen werden.
- **Europarecht:** AEUV, EUV, GRCh (Primärrecht); DSGVO, KI-VO, Produkthaftungsrichtlinie, Verbraucherrechterichtlinie, Vergaberichtlinien u. a. (Sekundärrecht); EuGH-Judikatur

## Workflow-Überblick

```
Einstieg
│
├─ triage-rechtsfrage-oder-norm
│   Sachverhalt / Rechtsfrage / Norm erfassen
│
├─ ziel-und-rechtsweg-bestimmung
│   Was will der Nutzer? Welches Gericht?
│
├─ falsche-wiese-warnung
│   Fehlverortungen erkennen
│
├─ de-eu-recht-abgrenzung
│   Welches Recht gilt?
│
Normbestimmung
│
├─ einschlaegige-normen-vorschlagen-de / -eu
├─ norm-historie-und-aenderungen
├─ rechtsprechung-recherche-strategie
│
Subsumtion
│
├─ norm-zerlegen-in-tatbestandsmerkmale
├─ ungeschriebene-merkmale-judikatur
├─ generalklauseln-pruefen
├─ unbestimmte-rechtsbegriffe-pruefen
├─ subsumtion-obersatz-definition-untersatz-ergebnis
├─ beweisbedarf-und-belege-erfassen
├─ darlegungs-und-beweislast-verteilen
├─ gegen-tbm-und-einreden-pruefen
│
Rechtsfolgen
│
├─ rechtsfolge-bestimmen
├─ konkurrenzen-anspruchsgrundlagen
├─ verjaehrung-fristen-pruefen
├─ verfahrensart-bestimmen
├─ eu-vorabentscheidung-pruefen
├─ grundrechte-pruefung-de-und-grch
│
Ausgabe (wählbar)
│
├─ output-juristisch-gestochen-de
├─ output-alltagssprache-de
├─ output-fremdsprachig-en-fr
├─ output-antrag-beschwerde-klageschrift
├─ output-memo-und-mandantenbrief
└─ output-pruefungsdokument-mit-warnhinweisen
```

## Wichtige Warnhinweise

Das System warnt aktiv in folgenden Situationen:

- **Falsche Norm:** Sachverhalt passt nicht zur gewählten Norm (`falsche-wiese-warnung`)
- **Komplexitätsgrenze:** Sachverhalt zu komplex für mechanische Prüfung (`mandatsabbruch-empfehlung-an-fachanwalt`)
- **Generalklauseln:** Kein mechanisch abschließbares Ergebnis möglich (`generalklauseln-pruefen`)
- **Unbestimmte Rechtsbegriffe:** Nur Indiziensammlung, keine Subsumtion (`unbestimmte-rechtsbegriffe-pruefen`)
- **Offene TBM:** Fehlende Belege gefährden das Ergebnis (`beweisbedarf-und-belege-erfassen`)

## Skills (31)

### A. Triage / Workflow-Einstieg

| Skill | Funktion |
|---|---|
| `triage-rechtsfrage-oder-norm` | Interaktive Erfassung der Nutzereingabe |
| `ziel-und-rechtsweg-bestimmung` | Ziel und Rechtsweg ermitteln |
| `falsche-wiese-warnung` | Typische Fehlverortungen erkennen |
| `de-eu-recht-abgrenzung` | Nationales vs. Unionsrecht abgrenzen |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Komplexitätsgrenze erkennen, Fachanwalt empfehlen |

### B. Normbestimmung und Recherche

| Skill | Funktion |
|---|---|
| `einschlaegige-normen-vorschlagen-de` | Deutsche Normen anhand Sachverhalt vorschlagen |
| `einschlaegige-normen-vorschlagen-eu` | EU-Normen anhand Sachverhalt vorschlagen |
| `rechtsprechung-recherche-strategie` | Recherche-Strategie und Fundstellen |
| `norm-historie-und-aenderungen` | Geltende Fassung und Übergangsrecht |
| `kommentar-und-literatur-hinweis` | Standardkommentare und Literaturhinweise |

### C. Tatbestandsmerkmale und Subsumtion

| Skill | Funktion |
|---|---|
| `norm-zerlegen-in-tatbestandsmerkmale` | TBM-Liste mit Definitionen |
| `ungeschriebene-merkmale-judikatur` | Richterrechtlich entwickelte Merkmale |
| `generalklauseln-pruefen` | Generalklauseln — Indizien und Fallgruppen |
| `unbestimmte-rechtsbegriffe-pruefen` | Auslegungsmaßstäbe für unbestimmte Begriffe |
| `subsumtion-obersatz-definition-untersatz-ergebnis` | Vier-Schritt-Schema je TBM |
| `beweisbedarf-und-belege-erfassen` | Beweismittel-Katalog und Tracking |
| `darlegungs-und-beweislast-verteilen` | Beweislast pro TBM |
| `gegen-tbm-und-einreden-pruefen` | Einwendungen und Einreden |

### D. Rechtsfolgen, Konkurrenzen, Verfahren

| Skill | Funktion |
|---|---|
| `rechtsfolge-bestimmen` | Anspruchsinhalt, Höhe, Nebenansprüche |
| `konkurrenzen-anspruchsgrundlagen` | Normkonkurrenzen und Spezialität |
| `verjaehrung-fristen-pruefen` | Verjährung, Hemmung, Neubeginn |
| `verfahrensart-bestimmen` | Passende Verfahrensart und Zuständigkeit |
| `eu-vorabentscheidung-pruefen` | Art. 267 AEUV — Voraussetzungen |
| `grundrechte-pruefung-de-und-grch` | GG und GRCh — Drei-Schritt-Schema |

### E. Output-Erzeugung

| Skill | Funktion |
|---|---|
| `output-juristisch-gestochen-de` | Schriftsatzstil, Rubrum, Tenor |
| `output-alltagssprache-de` | Verständliche Sprache für Betroffene |
| `output-fremdsprachig-en-fr` | Englisch und Französisch (nicht-amtlich) |
| `output-antrag-beschwerde-klageschrift` | Formale Dokument-Bausteine |
| `output-memo-und-mandantenbrief` | Aktennotiz und Mandantenbrief |
| `output-pruefungsdokument-mit-warnhinweisen` | Vollständiges Dokument mit allen Warnhinweisen |

## Lizenz

Apache-2.0 OR MIT — siehe LICENSE im Repository-Root.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Subsumtions Pruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `beweisbedarf-und-belege-erfassen` | Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich spaeter'-Markierung setzen. Struk... |
| `darlegungs-und-beweislast-verteilen` | Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss was beweisen. |
| `de-eu-recht-abgrenzung` | Klaert die Abgrenzung zwischen nationalem deutschen Recht und Unionsrecht: wann gilt AEUV/EUV/GRCh/Verordnung/Richtlinie unmittelbar, wann richtlinienkonforme Auslegung, wann Vorabentscheidungsersuchen Art. 267 AEUV und Anwendungsvorrang. |
| `einschlaegige-normen-vorschlagen-de` | Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Prüfungsreihenfolge und Hinweise auf Spezialitaet und konkurrierende Anspruchsgru... |
| `einschlaegige-normen-vorschlagen-eu` | Schlaegt einschlaegige Normen des Unionsrechts vor: AEUV, EUV, GRCh (Primaerrecht) sowie EU-Verordnungen und Richtlinien (Sekundaerrecht). Gibt Hinweise auf EuGH-Judikatur und Fundstellen bei curia.europa.eu. Klaert unmittelbare Wirkung... |
| `eu-vorabentscheidung-pruefen` | Prüft die Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV: Vorlagebefugnis und -pflicht, CILFIT-Ausnahmen (acte clair/eclaire), Consorzio-Erweiterung, Vorlagepflicht letzter Instanz, Formulierung der Vorlagefrage, curi... |
| `falsche-wiese-warnung` | Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwen... |
| `gegen-tbm-und-einreden-pruefen` | Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte Gegenprüfung nach Ans... |
| `generalklauseln-pruefen` | Prüft Generalklauseln wie Treu und Glauben (§ 242 BGB), gute Sitten (§ 138 BGB), billiges Ermessen, öffentliches Interesse und Verhältnismäßigkeit. Gibt Indizien und Fallgruppen statt mechanischer Subsumtion. Warnt vor der Grenzen automa... |
| `grundrechte-pruefung-de-und-grch` | Prüft Grundrechte nach GG (Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung) und GRCh (Art. 51/52 GRCh). Unterscheidet Abwehr-, Leistungs- und Schutzpflichtdimension. Verhältnismäßigkeitsprüfung mit Zweck, Geeignetheit, Erforderlich... |
| `kommentar-und-literatur-hinweis` | Quellenhinweis für vertiefte Subsumtion. Gibt keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen aus. Markiert, welche Normen vertieft in Literatur oder Datenbanken zu prüfen sind, und fordert Nutzerquellen oder lizenzi... |
| `konkurrenzen-anspruchsgrundlagen` | Klaert Konkurrenzfragen zwischen Anspruchsgrundlagen: Anspruchskonkurrenz, Anspruchsgrundlagenkonkurrenz, Spezialitaet, Subsidiaritaet, lex specialis/posterior/superior. Klaert Verhältnis von Vertrags- zu Deliktsrecht, nationalem zu Unio... |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Erkennt Indikatoren für Komplexitaetsgrenzen des mechanischen Prüfens und empfiehlt Abbruch sowie Weiterleitung an Fachanwalt, Notar, Steuerberater oder Behoerde. Warnt bei Strafrecht, Verfassungsrecht, internationalem Privatrecht und Ex... |
| `norm-historie-und-aenderungen` | Prüft die Norm-Historie: geltende Fassung zum massgeblichen Zeitpunkt, Übergangsvorschriften, intertemporales Recht, aenderungsrelevante Gesetzgebungsverfahren. Warnt bei Normen, die seit dem Wissensstand des Systems geaendert worden sei... |
| `norm-zerlegen-in-tatbestandsmerkmale` | Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion je TBM. |
| `output-alltagssprache-de` | Gibt das Subsumtionsergebnis in verstaendlicher Alltagssprache aus: ohne Fachbegriffe oder mit Erklärung, für Mandanten, Betroffene oder Behoerdenmitarbeiter. Behaelt die Strukturierung bei, vermeidet aber Lateinismen und Fachterminologi... |
| `output-antrag-beschwerde-klageschrift` | Erzeugt Tenor-Bausteine, Rubrum und formale Mindestanforderungen für Antrag, Beschwerde und Klageschrift nach ZPO, VwGO, SGG, FGO und BVerfGG. Gibt Pflichtangaben, Fristen und Einreichungshinweise. Kein anwaltlicher Schriftsatz ohne anwa... |
| `output-fremdsprachig-en-fr` | Gibt das Subsumtionsergebnis auf Englisch oder Franzoesisch aus. Enthaelt obligatorischen Hinweis auf nicht-amtliche Übersetzung und Abweichung von deutschen Originalnormen. Nuetzlich für internationale Mandanten, grenzüberschreitende Sa... |
| `output-juristisch-gestochen-de` | Erzeugt Ausgaben im juristischen Schriftsatzstil auf Deutsch: Antrag-Begründung-Beweismittel-Struktur, Subsumtionsdarstellung im Vier-Schritt, Zitierweise nach BGH-Standard, Rubrum, Tenor. Für Schriftsaetze, Klageschriften, Widersprueche... |
| `output-memo-und-mandantenbrief` | Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo für interne Nutzung mit juristischer Tiefe; Mandantenbrief für Betroffene in verstaendlicher Sprache. Beide mit Pfl... |
| `output-pruefungsdokument-mit-warnhinweisen` | Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer. |
| `rechtsfolge-bestimmen` | Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Hoehe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprüche. Gibt Berechnungshinweise für Schadensers... |
| `rechtsprechung-recherche-strategie` | Gibt eine Strategie für die Rechtsprechungsrecherche: wann systeminternes Wissen genuegt, wann Web-Suche bei BVerfG/BGH/BAG/BSG/BVerwG/OLG/EuGH noetig ist. Nennt Fundstellen: curia.europa.eu, dejure.org, openjur, rechtsprechung-im-intern... |
| `spezial-anwenden-livequellen-und-rechtsprechungscheck` | Anwenden: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-einreden-compliance-dokumentation-und-akte` | Einreden: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-europarecht-fristen-form-und-zustaendigkeit` | Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-interaktiver-erstpruefung-und-mandatsziel` | Interaktiver: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefen-mehrparteien-konflikt-und-interessen` | Pruefen: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsberatung-internationaler-bezug-und-schnittstellen` | Rechtsberatung: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsfolgen-zahlen-schwellen-und-berechnung` | Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schema-verhandlung-vergleich-und-eskalation` | Schema: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schritt-schriftsatz-brief-und-memo-bausteine` | Schritt: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-subsumtions-tatbestand-beweis-und-belege` | Subsumtions: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-tatbestandsmerkmale-dokumentenmatrix-und-lueckenliste` | Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-vier-behoerden-gericht-und-registerweg` | Vier: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zerlegen-risikoampel-und-gegenargumente` | Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `subsumtion-obersatz-definition-untersatz-ergebnis` | Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pr... |
| `triage-rechtsfrage-oder-norm` | Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor... |
| `unbestimmte-rechtsbegriffe-pruefen` | Prüft unbestimmte Rechtsbegriffe: wesentlich, erheblich, zumutbar, geeignet, angemessen, erforderlich. Gibt Auslegungsmassstaeibe aus Rechtsprechung und h.M., Indizien und Fallgruppen. Warnt vor der Grenze mechanischer Subsumtion bei wer... |
| `ungeschriebene-merkmale-judikatur` | Identifiziert judicativ entwickelte ungeschriebene Tatbestandsmerkmale: Verkehrspflichten, teleologische Reduktion und Extension, richterrechtliche Fortbildung, Analogie. Warnt vor Grenzen der mechanischen Prüfung bei richterrechtlich ge... |
| `verfahrensart-bestimmen` | Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mi... |
| `verjaehrung-fristen-pruefen` | Prüft Verjährungsfristen: Regelfrist 3 Jahre (§§ 195/199 BGB), kenntnisabhaengige Fristen, absolute 10- und 30-Jahresfristen, Hemmung (§§ 203 ff. BGB), Neubeginn (§ 212 BGB), prozessuale Notfristen und EU-Verjährungsregeln. Ergebnis: ver... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin subsumtions-pruefer: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin subsumtions-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin subsumtions-pruefer: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin subsumtions-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin subsumtions-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin subsumtions-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `ziel-und-rechtsweg-bestimmung` | Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfa... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
