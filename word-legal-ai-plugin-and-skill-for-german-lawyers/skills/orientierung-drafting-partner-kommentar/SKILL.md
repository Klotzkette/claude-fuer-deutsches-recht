---
name: orientierung-drafting-partner-kommentar
description: "Einstiegs- und Triage-Skill für juristisches Drafting. Klärt Dokumenttyp, Stadium, Adressat, Stilprofil, Sprachraum und Risiko, erstellt eine Mandatsmatrix und verweist auf die einschlägigen Fachmodulen word-legal-ai-plugin-and-skill-for-german-lawyers, insbesondere Kaltstart-Kommandocenter, Kanzleistil, Word-Finish, Partnerkommentar, US/UK-English und finales Quality Gate im Word Legal Ai Plugin And Skill For German Lawyers."
---

# Orientierung und Drafting-Triage

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
| Englischer Text aus deutscher Sicht | US/UK Legal Writing | `us-uk-legal-writing-für-deutsche`, `englischer-vertrag-deutsches-recht` |
| Englischer Vertrag mit deutschem Recht | German law in English | `englischer-vertrag-deutsches-recht`, `bilingual-drafting-deutsch-englisch` |
| Versandfassung | Quality Gate | `finaler-writing-quality-gate`, `word-dokument-finish-und-layout` |

## Typische Drafting-Fehler

- **Direkter Start ohne Triage.** Führt zu falschem Register, falschem Adressaten, falscher Tiefe.
- **Stadium ignoriert.** Ein Term Sheet bekommt keine Boilerplate-Salven; ein Endentwurf hat keine offenen Platzhalter.
- **Adressat falsch.** Mandantenbriefe in Schriftsatzsprache; Schriftsätze im Coaching-Ton.
- **Frist nicht erfasst.** Drafting ohne Frist ist akademisch.
- **Kein Verweis auf Fachmodule.** Triage-Skill versucht selbst, alle Aspekte zu lösen, statt zu übergeben.

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

## Quellen (Stand 05/2026)

- § 43a BRAO und § 203 StGB für Vertraulichkeit; gesetze-im-internet.de.
- `references/methodik-buergerliches-recht.md` für Stilwahl Gutachtenstil und Urteilsstil.
- Fachmodule im Plugin `word-legal-ai-plugin-and-skill-for-german-lawyers` als Folgeartefakt; vom Nutzer zu validieren, falls die genannten Skills im konkreten Setup nicht aktiviert sind.

