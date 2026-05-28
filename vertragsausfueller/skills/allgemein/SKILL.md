---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Vertragsausfueller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Vertragsausfueller — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Vertragsausfueller**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

### 0. Stummer Upload — Dokument ohne Begleittext

Wenn der Nutzer **nur ein Dokument hochlaedt und keinen weiteren Text schreibt** (kein Auftrag, keine Frage, keine Rolle), startet dieser Skill von selbst und wartet **nicht** auf einen Prompt. Verhalte dich dann wie der diensthabende Fachanwalt am Empfang, der eine zugestellte Akte sieht und sofort sinnvoll handelt.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Dokument-Klassifikation** in einem Satz: Welche Aktenart liegt vor? (Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz der Gegenseite, Akten-Konvolut, Tabelle, Foto/Screenshot, Anhoerungsbogen, Mahnbescheid, Rechnung, AU-Bescheinigung, KBA-Auszug, Registerauszug, ...). Wenn das Dokument einen klaren Briefkopf oder Tenor hat, das woertlich nennen.
2. **Norm- und Themenzuordnung** in ein bis drei Stichworten: Welches Rechtsgebiet, welche Norm, welcher Lebenssachverhalt? (z. B. "Gebuehrenbescheid BVG — § 23 MobG BE — Umsetzung aus Bushaltestelle".)
3. **Fristen-Triage zuerst:** Pruefe sichtbare Fristen (Widerspruchsfrist, Klagefrist, Berufungsfrist, Anhoerungsfrist, Rechtsbehelfsbelehrung). Wenn eine Frist erkennbar laeuft, das **als erstes** ausgeben — vor allem anderen.
4. **Beteiligten-Notiz:** Wer ist Absender, wer ist Adressat, gibt es Aktenzeichen, Behoerde, Gericht, Gegenseite?
5. **Routing in den passenden Spezial-Skill** dieses Plugins: Nenne **genau einen** Skill als primaeren Bearbeitungs-Skill und bis zu zwei weitere als Alternativen. Wenn der primaere Skill eindeutig ist, **arbeite sofort mit diesem Skill weiter** (nicht erst nachfragen). Wenn er nicht eindeutig ist, frage **eine einzige** gezielte Klaerungsfrage — nicht die volle Intake-Liste aus Abschnitt 1.
6. **Wenn die Klassifikation scheitert** (Dokument unleserlich, nicht zuordenbar, fremdes Rechtsgebiet): genau das sagen, eine konkrete Rueckfrage stellen ("Worum geht es?" reicht **nicht** — besser: "Ist das ein Bescheid der Behoerde X gegen Sie persoenlich oder gegen Ihren Mandanten Y?").

**Was du bei stummem Upload nicht machst:**

- Keine generische Inhaltszusammenfassung des Dokuments ("Sie haben ein PDF mit drei Seiten hochgeladen ...").
- Keine vollstaendige Intake-Abfrage aus Abschnitt 1 (Rolle, Ziel, Format ...). Diese Fragen kommen nur, wenn das Routing nicht eindeutig ist.
- Kein Warten auf einen Prompt. Der Upload **ist** der Prompt.

**Antwortformat bei stummem Upload:**

**Erkannt:** [Aktenart in einem Satz, mit Aktenzeichen/Absender wenn sichtbar]
**Rechtsgebiet:** [Norm/Thema in 1–3 Stichworten]
**Fristen-Hinweis:** [konkrete Frist mit Datum, oder "keine Frist erkennbar"]
**Primaerer Skill:** `skill-name` — [warum]
**Alternativen:** `...`, `...`
**Naechster Schritt:** [entweder direkter Arbeitsschritt ODER **eine** gezielte Rueckfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `vaf-altvertrag-nachziehen` | Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder… |
| `vaf-bsag-mietvertrag` | BSAG-Kiosk-Mietvertrag ausfüllen: Anwendungsfall BSAG-Term Sheet Huckelriede liegt vor und muss in Mietvertragsvorlage übertragen werden. §§ 535 ff. BGB Mietvertrag, § 9 UStG Umsatzsteueroption, § 550 BGB… |
| `vaf-clean-output` | Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand… |
| `vaf-docx-stripper` | DOCX-Vorlage in strukturierten Text zerlegen: Anwendungsfall Word-Vertragsdokument muss in Absätze, Tabellen, Klauseln, Platzhalter, Anlagen und Signaturblöcke zerlegt werden ohne Originaldatei zu überschreiben. §§ 305… |
| `vaf-feldinventar` | Feldinventar für Vertragsgenerator erstellen: Anwendungsfall Anwalt oder Mandant will wissen welche Felder im Vertrag auszufüllen sind bevor Rückfrageninterview startet. §§ 550 BGB Schriftformerfordernis Mietvertrag, §… |
| `vaf-klauselentscheidung` | Wahlklauseln und Klauselalternativen im Vertrag entscheiden: Anwendungsfall Vertrag enthält optionale Klauseln wie Umsatzsteueroption Indexierung Konkurrenzschutz Rückbau oder Betriebspflicht die aktiv angekreuzt oder… |
| `vaf-kommandocenter` | Vertragsausfüller Kommandocenter starten: Anwendungsfall Anwalt oder Mandant möchte Vertrag ausfüllen und gibt Eingabe-Dokument an; Skill erkennt Vorlage Altvertrag Term Sheet oder Freitext und leitet in richtigen… |
| `vaf-plausibilitaetscheck` | Plausibilitätsprüfung vor Vertragsausgabe: Zahlen Fristen Querverweise und interne Widersprüche prüfen. Anwendungsfall ausgefüllter Vertragsentwurf soll vor Ausgabe auf Rechenfehler und Inkonsistenzen geprüft werden.… |
| `vaf-quality-gate` | Quality Gate vor Vertragsausgabe: Vollständigkeit Plausibilitaet Risiken und Freigabe prüfen: Anwendungsfall vor Ausgabe des ausgefuellten Vertrags muss letzte Gesamtprüfung auf Fehler Luecken und unzulässige Klauseln… |
| `vaf-redline-qa` | Redline und Track-Changes-Fassung prüfen: Anwendungsfall Gegenentwurf oder überarbeitete Fassung liegt vor und soll auf Vollständigkeit versteckte Änderungen Formatbrüche und ungeklärte Klauselentscheidungen geprüft… |
| `vaf-rueckfrageninterview` | Rückfrageninterview für fehlende Vertragsdaten führen: Anwendungsfall Felder im Vertrag sind noch offen und Mandant muss verständnisfreundlich befragt werden. Klausel-Bibliothek, Vertragsmodule. Prüfraster offene… |
| `vaf-template-erkennung` | Vertragsvorlage und Altvertrag erkennen und analysieren: Anwendungsfall Anwalt oder Mandant gibt unbekannte Vorlage oder alten Vertrag ein und Skill soll Vertragstyp Klauselstruktur Pflichtfelder und Wahlklauseln… |
| `vaf-termsheet-mapping` | Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten muessen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent,… |
| `vaf-track-changes-nur-nach-frage` | Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff.… |

## Worum geht es?

Dieses Plugin fuehrt Anwaelte und ihre Mandanten durch den vollstaendigen Workflow zum Ausfullen, Aktualisieren und Qualitaetssichern von Vertragsvorlagen und Altvertraegen. Es erkennt automatisch den Eingabedokument-Typ (DOCX-Vorlage, Altvertrag, Term Sheet, Freitext), erstellt ein Feldinventar, fuehrt ein strukturiertes Ruckfrageninterview, trifft Klauselentscheidungen, prueft Plausibilitaet und gibt eine bereinige Clean-Version aus. Track-Changes-Fassungen werden nur nach ausdrucklicher Bestaetigung erstellt.

Das Plugin deckt alle gaengigen deutschen Vertragstypen ab: Mietvertraege, Arbeitsvertraege, Kaufvertraege, Dienstleistungsvertraege und individualvertragliche Sondergestaltungen. Es wendet AGB-Recht und Schriftformerfordernisse automatisch an.

## Wann brauchen Sie diese Skill?

- Anwalt oder Mandant uebergibt eine unbekannte DOCX-Vorlage und moechte wissen, welche Felder ausgefallt werden mussen.
- Ein Term Sheet liegt vor und soll systematisch in die entsprechende Vertragsvorlage uebertragen werden.
- Altvertrag soll auf eine neue Vorlage nachgezogen oder aktualisiert werden (Parteienwechsel, Gesetzesaenderungen).
- Gegenentwurf liegt vor und soll auf Vollstandigkeit, versteckte Aenderungen und ungeklartel Klauselentscheidungen geprueft werden.
- Fertig ausgefullter Vertragsentwurf soll vor Unterschrift oder Versand auf Rechenfehler, Inkonsistenzen und AGB-Verstoeasse geprueft werden.

## Fachbegriffe (kurz erklaert)

- **Feldinventar** — Strukturierte Liste aller ausfullbaren Felder einer Vertragsvorlage mit Pflicht/Optional-Status, Quelle und Risikohinweis.
- **Term Sheet** — Vorvertragliches Eckpunktepapier; Letter of Intent oder Term Sheet werden auf Vertragsfelder gemappt.
- **Track Changes** — Dokumenten-Aenderungsmarkierung in Word (DOCX); wird nur nach ausdrucklicher Bestaetigung ausgegeben.
- **AGB-Kontrolle** — Pruefung von allgemeinen Geschaeftsbedingungen nach §§ 305 bis 310 BGB; strenger Massstab bei B2C, geringer bei B2B.
- **Schriftformerfordernis** — § 550 BGB bei Mietvertraegen laenger als ein Jahr; § 125 BGB bei gesetzlicher Schriftform; Fehler macht Vertrag unwirksam.
- **Redline** — Uberarbeitete Vertragsfassung mit sichtbaren Aenderungen gegenuber dem Ausgangsdokument.
- **Clean Output** — Bereinigter Vertragsentwurf ohne Platzhalter und Track-Changes fuer Unterzeichnung oder Versand.
- **Plausibilitaetscheck** — Pruefung von Betragen, Fristen, Querverweisen und interner Konsistenz vor Ausgabe.

## Rechtsgrundlagen

- §§ 305 bis 310 BGB — AGB-Recht; Inhaltskontrolle.
- §§ 125 ff. BGB — Schriftformerfordernisse und Nichtigkeitsfolge.
- § 550 BGB — Schriftformerfordernis bei Mietvertrag laenger als ein Jahr.
- § 622 BGB — Kundigungsfristen Arbeitsvertraege.
- § 2 NachwG — Nachweispflichten im Arbeitsvertrag (Pflichtfelder).
- § 557b BGB — Indexmiete.
- § 9 UStG — Umsatzsteueroption bei Immobilienvermietung (Vorsteuerabzug).

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Eingabedokument-Typ bestimmen: Skill `vaf-kommandocenter` erkennt Vorlage, Altvertrag, Term Sheet oder Freitext.
2. Vorlage analysieren: `vaf-template-erkennung` oder `vaf-docx-stripper` fuer DOCX-Dokumente.
3. Feldinventar erstellen: `vaf-feldinventar`.
4. Ruckfrageninterview fuer offene Felder: `vaf-rueckfrageninterview`.
5. Klauselentscheidungen treffen: `vaf-klauselentscheidung`.
6. Quality Gate und Clean Output: `vaf-quality-gate` dann `vaf-clean-output`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Routing**

- `vaf-kommandocenter` — Eingabedokument-Typ erkennen, Workflow starten, Track-Changes-Bestaetigung einholen.

**Vorlage und Dokumentanalyse**

- `vaf-template-erkennung` — Vertragstyp, Klauselstruktur, Pflichtfelder und Wahlklauseln identifizieren.
- `vaf-docx-stripper` — DOCX-Vorlage in strukturierten Text zerlegen: Absaetze, Tabellen, Platzhalter, Anlagen.
- `vaf-feldinventar` — Feldinventar erstellen: Pflichtfelder, optionale Felder, Risikofelder.

**Daten- und Inhaltserfassung**

- `vaf-rueckfrageninterview` — Ruckfrageninterview fuer fehlende Vertragsdaten; mandantenfreundliche Fuehrung.
- `vaf-termsheet-mapping` — Term Sheet auf Vertragsfelder mappen; Lucken und Widersprueche erkennen.

**Klauselentscheidungen**

- `vaf-klauselentscheidung` — Wahlklauseln und Klauselalternativen entscheiden (Indexierung, USt-Option, Konkurrenzschutz).

**Aktualisierung**

- `vaf-altvertrag-nachziehen` — Altvertrag auf neue Vorlage nachziehen; Gesetzesaenderungen einpflegen.
- `vaf-bsag-mietvertrag` — BSAG-Kiosk-Mietvertrag spezifisch ausfullen.

**Qualitaetssicherung und Output**

- `vaf-plausibilitaetscheck` — Betrage, Fristen, Querverweise und interne Widersprueche pruefen.
- `vaf-quality-gate` — Gesamtpruefung: alle Pflichtfelder, AGB-Zulaessigkeit, Anlagen, Freigabe.
- `vaf-clean-output` — Bereinigter finaler Vertragsentwurf mit Ausfullprotokoll und Annahmenregister.

**Redline und Track Changes**

- `vaf-redline-qa` — Redline oder Gegenentwurf auf Vollstandigkeit und versteckte Aenderungen pruefen.
- `vaf-track-changes-nur-nach-frage` — Track-Changes-Fassung nur nach ausdrucklicher Bestaetigung erstellen.

## Worauf besonders achten

- **Schriftformerfordernis ist Fallstrick** — § 550 BGB bei Mietvertraegen laenger als ein Jahr; fehlende Unterschrift oder fehlende Anlage macht den Langzeitmietvertrag in ein Jahresvertrag ohne Kuendigungsschutz umzudeuten.
- **AGB oder Individualvertrag klaeren zuerst** — Die Intensitaet der AGB-Kontrolle haengt davon ab; ein Verhandlungsprotokoll kann Individualvertragscharakter begruenden.
- **Track-Changes-Bestaetigung nicht vergessen** — Das Plugin fragt explizit nach, bevor eine Redline erstellt wird; ohne Bestaetigung wird Clean Output ausgegeben.
- **Term Sheet ist oft unvollstaendig** — Steuerliche Punkte, USt-Option und Wettbewerbsverbote sind im Term Sheet haeufig nicht geregelt; `vaf-termsheet-mapping` markiert Lucken.
- **NachwG-Pflichtfelder bei Arbeitsvertraegen** — § 2 NachwG schreibt bestimmte Angaben vor; Fehlen kann Bussgeld ausloesen.

## Typische Fehler

- Vorlage wird direkt ausgefullt, ohne Schriftformerfordernis und AGB-Kontrolle vorab zu pruefen.
- Track-Changes-Fassung wird ausgegeben, ohne dass Quality Gate gruene Ampel gezeigt hat.
- Term Sheet wird eins zu eins uebernommen, ohne Widersprueche zur Vertragsvorlage zu prufen.
- Wahlklauseln bleiben unentschieden (Leerfelder in der Endfassung).
- Plausibilitaetscheck wird uebersprungen; Rechenfehler bei Mietbetrag oder Indexierung erst vom Mandanten bemerkt.

## Querverweise

- `bereicherungs-und-anfechtungsrecht-pruefer` — Wenn ausgefullter Vertrag angefochten oder rueckabgewickelt werden soll.
- `insolvenzrecht` — Wenn Vertragspartner insolvent ist und Vertragsfortsetzung oder Kuendigung zu pruefen ist.
- `europarecht-kompass` — Bei grenzueberschreitenden Vertraegen mit EU-Rechtsbezug (Richtlinien, AGB-Richtlinie).

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB §§ 125 ff. und §§ 305 bis 310 in der geltenden Fassung
- NachwG § 2 in der geltenden Fassung
- UStG § 9 in der geltenden Fassung
