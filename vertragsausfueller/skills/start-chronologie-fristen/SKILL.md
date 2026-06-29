---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Vertragsausfueller-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig..."
---

# Vertragsausfueller — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Vertragsausfueller**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

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

### 5. Fachmodule in diesem Plugin

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
| `vaf-termsheet-mapping` | Term Sheet auf Vertragsfelder mappen: Anwendungsfall Term Sheet liegt vor und Eckdaten müssen auf Vertragsfelder übertragen werden mit Erkennung fehlender Punkte und Widersprüche. §§ 145 ff. BGB Letter of Intent,… |
| `vaf-track-changes-nur-nach-frage` | Track Changes und Redline nur nach ausdrücklicher Bestätigung erstellen: Anwendungsfall überarbeiteter Vertrag soll als Track-Changes-Fassung ausgegeben werden; Skill fragt vorher explizit nach Bestätigung. §§ 145 ff.… |

## Worum geht es?

Dieses Plugin fuehrt Anwaelte und ihre Mandanten durch den vollstaendigen zum Ausfullen, Aktualisieren und Qualitaetssichern von Vertragsvorlagen und Altvertraegen. Es erkennt automatisch den Eingabedokument-Typ (DOCX-Vorlage, Altvertrag, Term Sheet, Freitext), erstellt ein Feldinventar, fuehrt ein strukturiertes Ruckfrageninterview, trifft Klauselentscheidungen, prüft Plausibilitaet und gibt eine bereinige Clean-Version aus. Track-Changes-Fassungen werden nur nach ausdrucklicher Bestaetigung erstellt.

Das Plugin deckt alle gaengigen deutschen Vertragstypen ab: Mietvertraege, Arbeitsvertraege, Kaufvertraege, Dienstleistungsvertraege und individualvertragliche Sondergestaltungen. Es wendet AGB-Recht und Schriftformerfordernisse automatisch an.

## Wann brauchen Sie diese Skill?

- Anwalt oder Mandant uebergibt eine unbekannte DOCX-Vorlage und moechte wissen, welche Felder ausgefallt werden mussen.
- Ein Term Sheet liegt vor und soll systematisch in die entsprechende Vertragsvorlage uebertragen werden.
- Altvertrag soll auf eine neue Vorlage nachgezogen oder aktualisiert werden (Parteienwechsel, Gesetzesaenderungen).
- Gegenentwurf liegt vor und soll auf Vollstandigkeit, versteckte Änderungen und ungeklartel Klauselentscheidungen geprueft werden.
- Fertig ausgefullter Vertragsentwurf soll vor Unterschrift oder Versand auf Rechenfehler, Inkonsistenzen und AGB-Verstoeasse geprueft werden.

## Fachbegriffe (kurz erklaert)

- **Feldinventar** — Strukturierte Liste aller ausfullbaren Felder einer Vertragsvorlage mit Pflicht/Optional-Status, Quelle und Risikohinweis.
- **Term Sheet** — Vorvertragliches Eckpunktepapier; Letter of Intent oder Term Sheet werden auf Vertragsfelder gemappt.
- **Track Changes** — Dokumenten-Änderungsmarkierung in Word (DOCX); wird nur nach ausdrucklicher Bestaetigung ausgegeben.
- **AGB-Kontrolle** — Prüfung von allgemeinen Geschäftsbedingungen nach §§ 305 bis 310 BGB; strenger Maßstab bei B2C, geringer bei B2B.
- **Schriftformerfordernis** — § 550 BGB bei Mietvertraegen laenger als ein Jahr; § 125 BGB bei gesetzlicher Schriftform; Fehler macht Vertrag unwirksam.
- **Redline** — Uberarbeitete Vertragsfassung mit sichtbaren Änderungen gegenuber dem Ausgangsdokument.
- **Clean Output** — Bereinigter Vertragsentwurf ohne Platzhalter und Track-Changes für Unterzeichnung oder Versand.
- **Plausibilitaetscheck** — Prüfung von Betragen, Fristen, Querverweisen und interner Konsistenz vor Ausgabe.

## Rechtsgrundlagen

- §§ 305 bis 310 BGB — AGB-Recht; Inhaltskontrolle.
- §§ 125 ff. BGB — Schriftformerfordernisse und Nichtigkeitsfolge.
- § 550 BGB — Schriftformerfordernis bei Mietvertrag laenger als ein Jahr.
- § 622 BGB — Kundigungsfristen Arbeitsvertraege.
- § 2 NachwG — Nachweispflichten im Arbeitsvertrag (Pflichtfelder).
- § 557b BGB — Indexmiete.
- § 9 UStG — Umsatzsteueroption bei Immobilienvermietung (Vorsteuerabzug).

## Schritt-für-Schritt: Einstieg ins Plugin

1. Eingabedokument-Typ bestimmen: Skill `vaf-kommandocenter` erkennt Vorlage, Altvertrag, Term Sheet oder Freitext.
2. Vorlage analysieren: `vaf-template-erkennung` oder `vaf-docx-stripper` für DOCX-Dokumente.
3. Feldinventar erstellen: `vaf-feldinventar`.
4. Ruckfrageninterview für offene Felder: `vaf-rueckfrageninterview`.
5. Klauselentscheidungen treffen: `vaf-klauselentscheidung`.
6. Quality Gate und Clean Output: `vaf-quality-gate` dann `vaf-clean-output`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Routing**

- `vaf-kommandocenter` — Eingabedokument-Typ erkennen, starten, Track-Changes-Bestaetigung einholen.

**Vorlage und Dokumentanalyse**

- `vaf-template-erkennung` — Vertragstyp, Klauselstruktur, Pflichtfelder und Wahlklauseln identifizieren.
- `vaf-docx-stripper` — DOCX-Vorlage in strukturierten Text zerlegen: Absaetze, Tabellen, Platzhalter, Anlagen.
- `vaf-feldinventar` — Feldinventar erstellen: Pflichtfelder, optionale Felder, Risikofelder.

**Daten- und Inhaltserfassung**

- `vaf-rueckfrageninterview` — Ruckfrageninterview für fehlende Vertragsdaten; mandantenfreundliche Fuehrung.
- `vaf-termsheet-mapping` — Term Sheet auf Vertragsfelder mappen; Lucken und Widersprueche erkennen.

**Klauselentscheidungen**

- `vaf-klauselentscheidung` — Wahlklauseln und Klauselalternativen entscheiden (Indexierung, USt-Option, Konkurrenzschutz).

**Aktualisierung**

- `vaf-altvertrag-nachziehen` — Altvertrag auf neue Vorlage nachziehen; Gesetzesaenderungen einpflegen.
- `vaf-bsag-mietvertrag` — BSAG-Kiosk-Mietvertrag spezifisch ausfullen.

**Qualitaetssicherung und Output**

- `vaf-plausibilitaetscheck` — Betrage, Fristen, Querverweise und interne Widersprueche prüfen.
- `vaf-quality-gate` — Gesamtpruefung: alle Pflichtfelder, AGB-Zulaessigkeit, Anlagen, Freigabe.
- `vaf-clean-output` — Bereinigter finaler Vertragsentwurf mit Ausfullprotokoll und Annahmenregister.

**Redline und Track Changes**

- `vaf-redline-qa` — Redline oder Gegenentwurf auf Vollstandigkeit und versteckte Änderungen prüfen.
- `vaf-track-changes-nur-nach-frage` — Track-Changes-Fassung nur nach ausdrucklicher Bestaetigung erstellen.

## Worauf besonders achten

- **Schriftformerfordernis ist Fallstrick** — § 550 BGB bei Mietvertraegen laenger als ein Jahr; fehlende Unterschrift oder fehlende Anlage macht den Langzeitmietvertrag in ein Jahresvertrag ohne Kuendigungsschutz umzudeuten.
- **AGB oder Individualvertrag klären zuerst** — Die Intensitaet der AGB-Kontrolle haengt davon ab; ein Verhandlungsprotokoll kann Individualvertragscharakter begruenden.
- **Track-Changes-Bestaetigung nicht vergessen** — Das Plugin fragt explizit nach, bevor eine Redline erstellt wird; ohne Bestaetigung wird Clean Output ausgegeben.
- **Term Sheet ist oft unvollstaendig** — Steuerliche Punkte, USt-Option und Wettbewerbsverbote sind im Term Sheet haeufig nicht geregelt; `vaf-termsheet-mapping` markiert Lucken.
- **NachwG-Pflichtfelder bei Arbeitsvertraegen** — § 2 NachwG schreibt bestimmte Angaben vor; Fehlen kann Bussgeld ausloesen.

## Typische Fehler

- Vorlage wird direkt ausgefullt, ohne Schriftformerfordernis und AGB-Kontrolle vorab zu prüfen.
- Track-Changes-Fassung wird ausgegeben, ohne dass Quality Gate gruene Ampel gezeigt hat.
- Term Sheet wird eins zu eins uebernommen, ohne Widersprueche zur Vertragsvorlage zu prufen.
- Wahlklauseln bleiben unentschieden (Leerfelder in der Endfassung).
- Plausibilitaetscheck wird uebersprungen; Rechenfehler bei Mietbetrag oder Indexierung erst vom Mandanten bemerkt.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB §§ 125 ff. und §§ 305 bis 310 in der geltenden Fassung
- NachwG § 2 in der geltenden Fassung
- UStG § 9 in der geltenden Fassung
