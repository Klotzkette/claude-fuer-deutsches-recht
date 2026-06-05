---
name: orientierung-drafting-partner-kommentar
description: "Orientierung Drafting Partner Kommentar: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Orientierung Drafting Partner Kommentar

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Orientierung Drafting Partner Kommentar** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `orientierung-drafting-triage` | Einstiegs- und Triage-Skill für juristisches Drafting. Klärt Dokumenttyp, Stadium, Adressat, Stilprofil, Sprachraum und Risiko, erstellt eine Mandatsmatrix und verweist auf die einschlägigen Fachmodulen word-legal-ai-plugin-and-skill-for-german-lawyers, insbesondere Kaltstart-Kommandocenter, Kanzleistil, Word-Finish, Partnerkommentar, US/UK-English und finales Quality Gate. |
| `partner-kommentar-umsetzen` | Setzt knappe Partnerkommentare und Randnotizen in echte Drafting-Schritte um. Übersetzt Hinweise wie bitte schärfen, zu lang, commercial, mehr Druck, weniger Gutachten, US counsel fragt, in eine Änderungsliste, priorisiert die Arbeit und formuliert die betroffenen Passagen neu. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Orientierung Drafting Partner Kommentar**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `orientierung-drafting-triage`

**Fokus:** Einstiegs- und Triage-Skill für juristisches Drafting. Klärt Dokumenttyp, Stadium, Adressat, Stilprofil, Sprachraum und Risiko, erstellt eine Mandatsmatrix und verweist auf die einschlägigen Fachmodulen word-legal-ai-plugin-and-skill-for-german-lawyers, insbesondere Kaltstart-Kommandocenter, Kanzleistil, Word-Finish, Partnerkommentar, US/UK-English und finales Quality Gate.

# Orientierung und Drafting-Triage

## Zweck

Jeder Drafting-Auftrag beginnt mit einer Triage. Bevor Sie eine Klausel schreiben, eine Klage entwerfen oder einen Schriftsatz strukturieren, müssen drei Dinge feststehen: welches Dokument, welches Stadium, welcher Adressat. Dieser Skill bringt Sie in zwei Rückfragen dorthin und legt sofort die Mandatsmatrix offen. Er ist der Einstiegspunkt für das Plugin `word-legal-ai-plugin-and-skill-for-german-lawyers` (Word Legal AI Plugin and Skill for German Lawyers, bis v50.6.x unter dem Slug `juristisches-drafting`).

Er ersetzt nicht die spezialisierten Skills, sondern verweist auf sie. Wenn die Anfrage wirklich diffus ist, beginnt die Arbeit mit `kaltstart-drafting-kommandocenter`. Wenn Dokumenttyp und Ziel bereits erkennbar sind, beginnt die Arbeit hier und verzweigt sofort in die Fachmodule.

Der Skill arbeitet schnell und liefert sofort ein Arbeitsergebnis. Er hält keinen Vortrag zur Drafting-Theorie. Sobald die drei Triagefragen beantwortet sind, erzeugt er eine Mandatsmatrix und schlägt die nächsten Skills vor.

## Eingaben

- Kurze Beschreibung des Mandats oder des Dokuments (ein bis drei Sätze reichen)
- Falls vorhanden: Entwurf, Vorlage, Eingangspost der Gegenseite
- Vorgabe zu Frist, Adressat, Rolle (Verteidigung, Klägerseite, beratend)
- Präferenz für Stil (Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Mandantenbrief, Schriftsatz, Memo, US/UK-English)

## Rechtlicher und methodischer Rahmen

- Anwaltsrecht: Mandatsgegenstand und Adressat klären ist Teil des anwaltlichen Sorgfaltsmaßstabs gemäß § 43a BRAO.
- Vertraulichkeit: § 43a Abs. 2 BRAO, § 203 StGB. Vor Eingabe von Mandantendaten in Cloud-Tools Auftragsverarbeitung prüfen.
- Standardmethode: Gutachtenstil für interne Memos, Urteilsstil für Schriftsätze und operative Klauseln. Siehe `references/methodik-buergerliches-recht.md`.
- Quellen: keine Pflicht für diese Triagephase. Belege folgen in den Fachmodule nach `references/zitierweise.md`.

## Ablauf / Checkliste

1. **Erkennen Sie das Dokument.** Erste Rückfrage falls unklar: handelt es sich um Vertrag, Schriftsatz, Anwaltsschreiben, Memo oder AGB.
2. **Bestimmen Sie das Stadium.** Term Sheet, Erstentwurf, Review fremden Entwurfs, Markup, Unterzeichnungsreife. Diese Information bestimmt, wie tief gedraftet wird.
3. **Identifizieren Sie den Adressaten.** Mandant, Gegenseite, Gericht, Behörde, interne Rechtsabteilung. Bestimmt Register und Stil.
4. **Prüfen Sie die Frist.** Frist ist Drafting-Treiber Nummer eins. Notieren Sie sie in der Matrix.
5. **Kalibrieren Sie den Stil.** Großkanzlei, Boutique, Kleinkanzlei, Inhouse, Gericht oder US/UK-Korrespondenz.
6. **Prüfen Sie das Risiko.** Pauschal: niedrig, mittel, hoch. Auch ohne tiefe Prüfung ist eine erste Einordnung möglich.
7. **Erstellen Sie die Mandatsmatrix.** Tabelle, höchstens zehn Zeilen. Siehe Beispiel unten.
8. **Verweisen Sie weiter.** Nennen Sie zwei bis fünf Skills aus dem Plugin, die als nächste anzuwenden sind.
9. **Liefern Sie bei klarer Faktenlage einen Skelettentwurf.** Wenn die Triagefragen klar sind, kann ein erster Strukturentwurf direkt mitgeliefert werden.

### Triage-Tabelle Dokumenttyp zu Skill

| Dokument | Stadium | Empfohlene Skills |
|---|---|---|
| Vertrag | Erstentwurf | `dokumentarchitektur-vertrag-und-schriftsatz`, `definitionen-klauseln-stringent`, `boilerplate-klauseln-katalog` |
| Vertrag | Review | `verweis-und-querverweis-technik`, `haftungsausschluss-und-haftungsbegrenzung` |
| Klage | Erstentwurf | `klage-drafting-253-zpo`, `dokumentarchitektur-vertrag-und-schriftsatz` |
| Klageerwiderung | Erstentwurf | `klageerwiderung-substantiiertes-bestreiten` |
| NDA | Eingehend | `geheimhaltung-nda-vertraulichkeit`, `boilerplate-klauseln-katalog` |
| AGB | Erstentwurf | `agb-konforme-klauseln-305-310-bgb`, `transparenzgebot-307-bgb` |
| Anwaltsschreiben | Erstmahnung | `anwaltsschreiben-aussergerichtlich`, `stil-und-ton-juristische-texte` |
| Memo | Intern | `gutachten-memo-internes-drafting` |
| Vertragsentwurf der Gegenseite | Review mit Verteidigungshaltung | `defensive-drafting-fallen-erkennen`, `verweis-und-querverweis-technik` |
| Term Sheet / LoI | Übersetzung in Vertrag | `term-sheet-zu-vertrag-uebersetzung`, `dokumentarchitektur-vertrag-und-schriftsatz` |
| Vertrag DE/EN | Bilingual | `bilingual-drafting-deutsch-englisch`, `definitionen-klauseln-stringent` |
| Klauselbedarf konkret | Baustein abrufen | `klausel-bibliothek-katalog`, `boilerplate-klauseln-katalog` |
| Auftrag diffus | Kaltstart | `kaltstart-drafting-kommandocenter`, dann Fachmodul |
| Stil oder Kanzleiregister unklar | Stilkalibrierung | `deutscher-kanzleistil-kalibrieren`, `stil-und-ton-juristische-texte` |
| Partnernotizen / Randkommentare | Umsetzung in Draft | `partner-kommentar-umsetzen`, `revisions-prozess-redlines-comparison` |
| Mandantenmemo / Partnerupdate | Entscheidungsvorlage | `mandantenmemo-und-partner-update`, `argumentationsarchitektur-schreiben` |
| Schriftsatz ist zu lang oder unklar | Richterlesbarkeit | `schriftsatz-ueberarbeiten-richterlesbar`, `argumentationsarchitektur-schreiben` |
| Englischer Text aus deutscher Sicht | US/UK Legal Writing | `us-uk-legal-writing-fuer-deutsche`, `englischer-vertrag-deutsches-recht` |
| Englischer Vertrag mit deutschem Recht | German law in English | `englischer-vertrag-deutsches-recht`, `bilingual-drafting-deutsch-englisch` |
| Versandfassung | Quality Gate | `finaler-writing-quality-gate`, `word-dokument-finish-und-layout` |

## Typische Drafting-Fehler

- **Direkter Start ohne Triage.** Führt zu falschem Register, falschem Adressaten, falscher Tiefe.
- **Stadium ignoriert.** Ein Term Sheet bekommt keine Boilerplate-Salven; ein Endentwurf hat keine offenen Platzhalter.
- **Adressat falsch.** Mandantenbriefe in Schriftsatzsprache; Schriftsätze im Coaching-Ton.
- **Frist nicht erfasst.** Drafting ohne Frist ist akademisch.
- **Kein Verweis auf Fachmodule.** Triage-Skill versucht selbst, alle Aspekte zu lösen, statt zu übergeben.

## Ausgabeformat

- Mandatsmatrix als Tabelle.
- Liste der nächsten zwei bis fünf Skills.
- Optional: Skelettentwurf mit Platzhaltern in eckigen Klammern.

## Beispiel

**Anfrage:** "Wir verhandeln eine Lieferantenvereinbarung mit einem mittelgroßen Werkzeugbauer. Der Lieferant hat einen Entwurf geschickt. Wir wollen Markup zurückspielen, Frist eine Woche."

**Mandatsmatrix:**

| Punkt | Ausprägung |
|---|---|
| Dokumenttyp | Lieferantenvereinbarung (Vertrag) |
| Stadium | Review fremden Entwurfs mit Markup |
| Rolle | Bestellerseite |
| Adressat des Markups | Gegenseite über unsere Rechtsabteilung |
| Frist | eine Woche |
| Schwerpunkt | Haftungsregime, Mängelhaftung, Schriftform |
| Risiko | mittel |

**Nächste Skills:**

1. `haftungsausschluss-und-haftungsbegrenzung` für das Haftungsregime.
2. `definitionen-klauseln-stringent` für den Defined-Terms-Apparat im Lieferantenvertrag.
3. `verweis-und-querverweis-technik` für Anlagen und interne Verweise.
4. `boilerplate-klauseln-katalog` für Schriftform, Gerichtsstand, Rechtswahl.

## Querverweise

- `dokumentarchitektur-vertrag-und-schriftsatz`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`
- `stil-und-ton-juristische-texte`
- `kaltstart-drafting-kommandocenter`
- `deutscher-kanzleistil-kalibrieren`
- `finaler-writing-quality-gate`

## Quellen (Stand 05/2026)

- § 43a BRAO und § 203 StGB für Vertraulichkeit; gesetze-im-internet.de.
- `references/methodik-buergerliches-recht.md` für Stilwahl Gutachtenstil und Urteilsstil.
- Fachmodule im Plugin `word-legal-ai-plugin-and-skill-for-german-lawyers` als Folgeartefakt; vom Nutzer zu validieren, falls die genannten Skills im konkreten Setup nicht aktiviert sind.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `partner-kommentar-umsetzen`

**Fokus:** Setzt knappe Partnerkommentare und Randnotizen in echte Drafting-Schritte um. Übersetzt Hinweise wie bitte schärfen, zu lang, commercial, mehr Druck, weniger Gutachten, US counsel fragt, in eine Änderungsliste, priorisiert die Arbeit und formuliert die betroffenen Passagen neu.

# Partner-Kommentar Umsetzen

## Zweck

Partnerkommentare sind oft kurz, schnell und mehrdeutig. Dieser Skill übersetzt sie in konkrete Arbeit: Was ist gemeint, was muss geändert werden, welche Passage bekommt welche neue Funktion?

## Eingaben

- Dokument oder Passage.
- Partnerkommentar, Randnotiz, E-Mail oder Chat.
- Rolle des Mandanten und Verhandlungsziel.
- Zeitbudget.

## Kommentar-Decoder

| Kommentar | Bedeutet meistens | Reaktion |
|---|---|---|
| "zu lang" | Ergebnis kommt zu spät | kürzen, Überschrift schärfen, Empfehlung nach vorne |
| "commercial" | rechtlich richtig, aber wirtschaftlich unbrauchbar | Geschäftsinteresse sichtbar machen |
| "mehr Druck" | Gegenseite soll merken, dass Eskalation real ist | Frist, Konsequenz, Beleg, kein Lärm |
| "zu hart" | Beziehung oder Deal gefährdet | Ton deeskalieren, Rechtsposition halten |
| "nicht gutachten" | Prüfungssprache stört | Urteilsstil oder Empfehlungssprache |
| "US counsel?" | Begriff könnte im Common Law anders verstanden werden | `us-uk-legal-writing-fuer-deutsche` zuschalten |
| "Word sauber" | Format/Markup nicht sendefähig | `word-dokument-finish-und-layout` zuschalten |

## Ablauf

1. Kommentare extrahieren und nummerieren.
2. Jeden Kommentar einer Funktion zuordnen: Kürzen, Schärfen, Risiko, Ton, Struktur, Word.
3. Konflikte erkennen: "mehr Druck" und "deeskalieren" gleichzeitig offenlegen.
4. Arbeitspakete bilden.
5. Passage neu formulieren.
6. Offene Rückfragen an Partnerin nur stellen, wenn die Umsetzung sonst riskant wäre.

## Output

- Kommentar-Register.
- Priorisierte Änderungsliste.
- Neuformulierung der betroffenen Passage.
- Kurzer Rückgabe-Text an Partnerin: "Umgesetzt; offen bleibt nur ..."

## Qualitätsmaßstab

Nicht bloß paraphrasieren. Der Skill muss den Kommentar in echtes Drafting übersetzen und eine sendefähige Fassung liefern.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
