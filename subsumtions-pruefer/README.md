# Subsumtions-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`subsumtions-pruefer.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/subsumtions-pruefer.md) (104 KB)
- Im Repo: [`testakten/megaprompts/subsumtions-pruefer.md`](../testakten/megaprompts/subsumtions-pruefer.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

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

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 53 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anwenden-quellenkarte` | Anwenden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `beweisbedarf-und-belege-erfassen` | Erfasst pro Tatbestandsmerkmal den Beweisbedarf: Beweismittel-Katalog (Urkunden, Zeugen, Sachverständige, Augenschein, Parteivernehmung), Belege hochladen, Tatsachenbehauptung eintragen oder 'beweise ich später'-Markierung setzen. Struk... |
| `darlegungs-und-beweislast-verteilen` | Verteilt Darlegungs- und Beweislast nach Grundregel (wer Recht behauptet traegt Beweislast), Beweislastumkehr (Produkthaftung, Diskriminierung, DSGVO), sekundaerer Darlegungslast und Anscheinsbeweis. Pro TBM: wer muss was beweisen im Sub... |
| `dokumente-intake` | Dokumentenintake für Subsumtions-Prüfer (Jura): sortiert Sachverhalt, Lösungsskizze, Norm-Tatbestand, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einreden-compliance-dokumentation-und-akte` | Einreden: Compliance-Dokumentation und Aktenvermerk im Subsumtions Prüfer. |
| `einschlaegige-normen-vorschlagen-de` | Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Prüfungsreihenfolge und Hinweise auf Spezialitaet und konkurrierende Anspruchsgru... |
| `einschlaegige-normen-vorschlagen-eu` | Schlaegt einschlaegige Normen des Unionsrechts vor: AEUV, EUV, GRCh (Primaerrecht) sowie EU-Verordnungen und Richtlinien (Sekundaerrecht). Gibt Hinweise auf EuGH-Judikatur und Fundstellen bei curia.europa.eu. Klaert unmittelbare Wirkung... |
| `einstieg-routing` | Einstieg, Triage und Routing für Subsumtions-Prüfer (Jura): ordnet Rolle (Studierender, Bearbeiter), markiert Frist (keine harten Fristen), wählt Norm (BGB, StGB, GG, Methodenlehre) und Zuständigkeit (zuständige Stelle), leitet zum passe... |
| `eu-abgrenzung-einschlaegige-normen` | Klaert die Abgrenzung zwischen nationalem deutschen Recht und Unionsrecht: wann gilt AEUV/EUV/GRCh/Verordnung/Richtlinie unmittelbar, wann richtlinienkonforme Auslegung, wann Vorabentscheidungsersuchen Art. 267 AEUV und Anwendungsvorrang... |
| `eu-vorabentscheidung-falsche-wiese` | Prüft die Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV: Vorlagebefugnis und -pflicht, CILFIT-Ausnahmen (acte clair/eclaire), Consorzio-Erweiterung, Vorlagepflicht letzter Instanz, Formulierung der Vorlagefrage, cur... |
| `europarecht-fristen-form-und-zustaendigkeit` | Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg im Subsumtions Prüfer. |
| `falsche-wiese-warnung` | Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwen... |
| `fehlerklasse-bgb-at-training` | Ordnet BGB-AT-Fehler in Klausuren: Vertragsschluss, Zugang, Minderjaehrige, Stellvertretung, Anfechtung, Form und Fristen. Trainiert strukturiertes Erkennen, Gewichten und Beheben von Klausurfehlern im Subsumtions Prüfer. |
| `generalklauseln-pruefen` | Prüft Generalklauseln wie Treu und Glauben (§ 242 BGB), gute Sitten (§ 138 BGB), billiges Ermessen, öffentliches Interesse und Verhältnismäßigkeit. Gibt Indizien und Fallgruppen statt mechanischer Subsumtion. Warnt vor der Grenzen automa... |
| `grundrechte-pruefung-de-und-grch` | Prüft Grundrechte nach GG (Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung) und GRCh (Art. 51/52 GRCh). Unterscheidet Abwehr-, Leistungs- und Schutzpflichtdimension. Verhältnismäßigkeitsprüfung mit Zweck, Geeignetheit, Erforderlich... |
| `interaktiver-erstpruefung-und-mandatsziel` | Interaktiver: Erstprüfung, Rollenklärung und Mandatsziel im Subsumtions Prüfer. |
| `interessen-rechtsberatung-rechtsfolgen` | Prüfen: Mehrparteienkonflikt und Interessenmatrix im Subsumtions Prüfer. |
| `kandidatenloesung-subsumtion-pruefen` | Prüft abgegebene Klausur- oder Probandenloesungen auf Obersatz, Definition, Untersatz, Beleg, Ergebnis und typische Scheinkausalitaet. Gibt Korrekturvermerk mit Punkteindikation und Musterpassage im Subsumtions Prüfer. |
| `kommentar-literatur-konkurrenzen` | Quellenhinweis für vertiefte Subsumtion. Gibt keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen aus. Markiert, welche Normen vertieft in Literatur oder Datenbanken zu prüfen sind, und fordert Nutzerquellen oder lizenzi... |
| `konkurrenzen-anspruchsgrundlagen` | Klaert Konkurrenzfragen zwischen Anspruchsgrundlagen: Anspruchskonkurrenz, Anspruchsgrundlagenkonkurrenz, Spezialitaet, Subsidiaritaet, lex specialis/posterior/superior. Klaert Verhältnis von Vertrags- zu Deliktsrecht, nationalem zu Unio... |
| `mandatsabbruch-empfehlung-beweisbedarf` | Erkennt Indikatoren für Komplexitaetsgrenzen des mechanischen Prüfens und empfiehlt Abbruch sowie Weiterleitung an Fachanwalt, Notar, Steuerberater oder Behörde. Warnt bei Strafrecht, Verfassungsrecht, internationalem Privatrecht und Exi... |
| `norm-historie-und-aenderungen` | Prüft die Norm-Historie: geltende Fassung zum massgeblichen Zeitpunkt, Übergangsvorschriften, intertemporales Recht, aenderungsrelevante Gesetzgebungsverfahren. Warnt bei Normen, die seit dem Wissensstand des Systems geaendert worden sei... |
| `norm-zerlegen-mandantenbrief` | Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion je TBM im Subsumtion... |
| `output-alltagssprache-de` | Gibt das Subsumtionsergebnis in verstaendlicher Alltagssprache aus: ohne Fachbegriffe oder mit Erklärung, für Mandanten, Betroffene oder Behördenmitarbeiter. Behaelt die Strukturierung bei, vermeidet aber Lateinismen und Fachterminologie... |
| `output-antrag-beschwerde-klageschrift` | Erzeugt Tenor-Bausteine, Rubrum und formale Mindestanforderungen für Antrag, Beschwerde und Klageschrift nach ZPO, VwGO, SGG, FGO und BVerfGG. Gibt Pflichtangaben, Fristen und Einreichungshinweise. Kein anwaltlicher Schriftsatz ohne anwa... |
| `output-fremdsprachig-en-fr` | Gibt das Subsumtionsergebnis auf Englisch oder Franzoesisch aus. Enthaelt obligatorischen Hinweis auf nicht-amtliche Übersetzung und Abweichung von deutschen Originalnormen. Nuetzlich für internationale Mandanten, grenzüberschreitende Sa... |
| `output-juristisch-gestochen-de` | Erzeugt Ausgaben im juristischen Schriftsatzstil auf Deutsch: Antrag-Begründung-Beweismittel-Struktur, Subsumtionsdarstellung im Vier-Schritt, Zitierweise nach BGH-Standard, Rubrum, Tenor. Für Schriftsaetze, Klageschriften, Widersprueche... |
| `output-memo-und-mandantenbrief` | Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo für interne Nutzung mit juristischer Tiefe; Mandantenbrief für Betroffene in verstaendlicher Sprache. Beide mit Pfl... |
| `output-pruefungsdokument-mit-warnhinweisen` | Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer... |
| `rechtsberatung-internationaler-bezug-und-schnittstellen` | Rechtsberatung: Internationaler Bezug und Schnittstellen im Subsumtions Prüfer. |
| `rechtsfolge-bestimmen-einreden-interaktiver` | Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Höhe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprüche. Gibt Berechnungshinweise für Schadensers... |
| `rechtsfolgen-zahlen-schwellen-und-berechnung` | Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung im Subsumtions Prüfer. |
| `rechtsprechung-recherche-strategie` | Gibt eine Strategie für die Rechtsprechungsrecherche: wann systeminternes Wissen genuegt, wann Web-Suche bei BVerfG/BGH/BAG/BSG/BVerwG/OLG/EuGH noetig ist. Nennt Fundstellen: curia.europa.eu, dejure.org, openjur, rechtsprechung-im-intern... |
| `schema-schritt-subsumtions` | Schema: Verhandlung, Vergleich und Eskalation im Subsumtions Prüfer. |
| `schritt-schriftsatz-brief-und-memo-bausteine` | Schritt: Schriftsatz-, Brief- und Memo-Bausteine im Subsumtions Prüfer. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Subsumtions Prüfer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `subsumtion-obersatz-rewrite-klausurton-triage` | Führt die klassische juristische Vier-Schritt-Subsumtion durch: Obersatz (Norm und Rechtsfolge), Definition (TBM-Inhalt aus h.M./Rspr.), Untersatz (Sachverhalt unter Definition), Ergebnis (TBM erfuellt ja/nein/fraglich). Ein Durchlauf pr... |
| `subsumtions-rewrite-klausurton` | Schreibt falsche oder lueckenhafte Subsumtionen in einen knappen juristischen Klausurton um, ohne neue Tatsachen zu erfinden. Vier-Schritt-Schema: Obersatz, Definition, Subsumtion, Ergebnis je Tatbestandsmerkmal im Subsumtions Prüfer. |
| `subsumtions-tatbestand-beweis-und-belege` | Subsumtions: Tatbestandsmerkmale, Beweisfragen und Beleglage im Subsumtions Prüfer. |
| `tatbestandsmerkmale-vier-zerlegen` | Tatbestandsmerkmale: Dokumentenmatrix, Lückenliste und Nachforderung im Subsumtions Prüfer. |
| `tbm-grundrechte-grch-kandidatenloesung` | Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte Gegenprüfung nach Ans... |
| `triage-rechtsfrage-oder-norm` | Interaktiver Einstieg: Erfasst strukturiert, ob der Nutzer eine Rechtsfrage, einen Lebenssachverhalt, eine konkrete Norm oder eine Mischung davon hat. Stellt gezielte Rückfragen und leitet zum passenden naechsten Skill weiter. Warnt vor... |
| `unbestimmte-rechtsbegriffe-ungeschriebene` | Prüft unbestimmte Rechtsbegriffe: wesentlich, erheblich, zumutbar, geeignet, angemessen, erforderlich. Gibt Auslegungsmassstaeibe aus Rechtsprechung und h.M., Indizien und Fallgruppen. Warnt vor der Grenze mechanischer Subsumtion bei wer... |
| `ungeschriebene-merkmale-judikatur` | Identifiziert judicativ entwickelte ungeschriebene Tatbestandsmerkmale: Verkehrspflichten, teleologische Reduktion und Extension, richterrechtliche Fortbildung, Analogie. Warnt vor Grenzen der mechanischen Prüfung bei richterrechtlich ge... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Subsumtions-Prüfer (Jura): trennt fehlende Tatsachen von fehlenden Belegen (Sachverhalt, Lösungsskizze, Norm-Tatbestand), nennt pro Lücke Beweisthema, Beschaffungsweg (zuständige Stelle), Frist und Ersat... |
| `verfahrensart-bestimmen-verjaehrung` | Bestimmt die passende Verfahrensart: ordentlich (ZPO), einstweilig (§§ 935/940 ZPO), Mahnverfahren, FG-Verfahren, Schiedsverfahren, Insolvenzverfahren, OWi-Verfahren, Verwaltungs-, Straf- und Verfassungsgerichtsverfahren. Gibt formale Mi... |
| `verjaehrung-fristen-pruefen` | Prüft Verjährungsfristen: Regelfrist 3 Jahre (§§ 195/199 BGB), kenntnisabhaengige Fristen, absolute 10- und 30-Jahresfristen, Hemmung (§§ 203 ff. BGB), Neubeginn (§ 212 BGB), prozessuale Notfristen und EU-Verjährungsregeln. Ergebnis: ver... |
| `vier-behoerden-gericht-und-registerweg` | Behörden-, Gerichts- oder Registerweg; prüft welcher Weg zur zuständigen Behörde, zum richtigen Gericht oder zum einschlägigen Register führt. Gibt Normen, Fristen und Zuständigkeitsregeln für die vier klassischen Wege im Subsumtions Pru... |
| `waehlen-rechtsprechung-recherche-europarecht` | Output wählen: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung im Subsumtions Prüfer. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Subsumtions Prüfer. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Subsumtions Prüfer. |
| `zerlegen-risikoampel-und-gegenargumente` | Zerlegen: Risikoampel, Gegenargumente und Verteidigungslinien im Subsumtions Prüfer. |
| `ziel-und-rechtsweg-bestimmung` | Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfa... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
