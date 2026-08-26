---
name: urteilsbauer-relation-start-chronologie-fristen
description: "Für Urteilsbauer und Relationsmacher — Allgemein: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Chronologie mit Beleg- und Widerspruchsmatrix."
---

# Urteilsbauer und Relationsmacher — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Urteilsbauer Relationsmacher**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO.

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
4. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
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

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Worum geht es?

Das Plugin ist eine Urteils- und Beschluss-Werkstatt für Richter, Referendare und Rechtspfleger. Es begleitet den vollstaendigen vom Aktenintake über die Relation (Entscheidungsunterlage) bis zum fertigen Urteil als DOCX-Dokument im offiziellen Gerichtslayout. Das Plugin stuetzt die Prüfung von Zulaessigkeit, Anspruchsgrundlagen, Beweiswuerdigung und Kostenentscheidung sowie Rechtsmittelbelehrung.

Spezialisierte Teilmodule decken familiengerichtliche Besonderheiten (FamFG), internationales Privatrecht (IPR), CISG-Sachverhalte, kollidierende AGB und die vorläufige Vollstreckbarkeit ab. Ausbildungsmodule unterstuetzen Referendare bei der Vollrelation nach Schulstandard.

## Wann brauchen Sie diese Skill?

- Richter hat neue Zivilakte und will Überblick gewinnen, Verfahrensstand klären und Anspruchsgrundlagen identifizieren.
- Referendar oder Assessorkandidat erstellt Relation oder Vollrelation für Examensvorbereitung.
- Richter muss Beweiswuerdigung nach § 286 ZPO verschriftlichen und dafür gegliederten Abschnitt in den Entscheidungsgruenden erzeugen.
- Gericht erstellt Beschluss (PKH, Streitwert, Hinweis nach § 139 ZPO) oder Versaumnisurteil.
- Internationaler Kaufvertrag mit CISG- oder IPR-Bezug muss rechtlich eingeordnet werden.

## Fachbegriffe (kurz erklaert)

- **Relation** — Richterliche Entscheidungsunterlage; strukturierte Zusammenfassung von Sach- und Streitstand, Beweisaufnahme und rechtlicher Wuerdigung.
- **Tatbestand (§ 313 Abs. 2 ZPO)** — Pflichtbestandteil des Urteils; sachliche Darstellung des Parteivorbringens ohne Wertung.
- **Entscheidungsgruende (§ 313 Abs. 3 ZPO)** — Rechtliche und tatsaechliche Begruendung des Tenors.
- **Tenor** — Urteilsausspruch; entscheidet über Hauptsache, Kosten und vorläufige Vollstreckbarkeit.
- **Beweiswuerdigung (§ 286 ZPO)** — Freie Wuerdigung des Ergebnisses der Beweisaufnahme; Kernaufgabe des Gerichts.
- **Vollrelation** — Ausfuehrliche Relation nach Schulstandard für Referendars- und Assessor-Prüfung.
- **FamFG** — Gesetz über das Verfahren in Familiensachen; regelt Beschlussverfahren in Familiengericht-Sachen.
- **CISG** — UN-Kaufrecht (Convention on Contracts for the International Sale of Goods); gilt für grenzueberschreitende Kaufvertraege zwischen Unternehmern aus Vertragsstaaten.

## Rechtsgrundlagen

- § 313 ZPO — Pflichtbestandteile des Zivilurteils (Tatbestand, Entscheidungsgruende, Tenor, Rubrum)
- §§ 286 287 ZPO — Freie Beweiswuerdigung, Schadensschaetzung
- § 139 ZPO — Materielle Prozessleitung; Hinweispflicht des Gerichts
- §§ 91 ff. ZPO — Kostenentscheidung
- §§ 708 ff. ZPO — Vorlaeufige Vollstreckbarkeit
- §§ 511 543 ZPO — Berufung, Revision
- §§ 313a 313b ZPO — Urteil ohne Tatbestand, Versaeumnisurteil
- FamFG — Beschluss-Verfahren im Familienrecht
- CISG — UN-Kaufrecht
- Rom I-VO, Rom II-VO — Anwendbares Recht bei grenzueberschreitenden Sachverhalten

## Schritt-für-Schritt: Einstieg ins Plugin

1. Aktenintake: Akte einlesen, Verfahrensstand und Sachverhalt strukturieren.
2. Zulaessigkeit prüfen: Gerichtliche Zuständigkeit, Rechtsschutzinteresse, Prozessvoraussetzungen.
3. Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Tenor, Tatbestand, Entscheidungsgruende, Kostenentscheidung und Rechtsmittelbelehrung nacheinander oder geblockt erstellen.

## Skill-Tour (was gibt es hier?)

- `aktenintake-zivil` — Eingehende Zivilakte strukturieren und Überblick gewinnen.
- `zulaessigkeit-pruefen` — Zulaessigkeit der Zivilklage systematisch prüfen: Zuständigkeit, Prozessfaehigkeit, Rechtsschutzinteresse.
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bei Anspruchskonkurrenz bestimmen.
- `relation-zivil` — Zivilrechtliche Relation nach klassischer Relationstechnik erstellen (Kurz- oder Langfassung).
- `vollrelation-langfassung` — Vollstaendige Relation im Schulstandard für Referendar- und Assessorpruefung.
- `beweiswuerdigung-mit-richter-input` — Strukturierte Beweiswuerdigung nach § 286 ZPO mit Richter-Input ausformulieren.
- `beweisbeschluss-vorbereiten` — Beweisbeschluss nach § 359 ZPO vorbereiten.
- `tatbestand-zivil-schreiben` — Tatbestand nach § 313 Abs. 2 ZPO sachlich und knapp ausformulieren.
- `entscheidungsgruende-zivil-schreiben` — Entscheidungsgruende im Urteilsstil schreiben.
- `tenor-bauen-zivil` — Tenor konstruieren: Hauptsache, Kosten, vorläufige Vollstreckbarkeit.
- `kostenentscheidung-bauen` — Kostenentscheidung nach §§ 91 ff. ZPO erstellen und Kostenquote bestimmen.
- `vorläufige-vollstreckbarkeit` — Richtige Anordnung zur vorläufigen Vollstreckbarkeit nach §§ 708 ff. ZPO bestimmen.
- `rechtsmittelbelehrung-zivil` — Rechtsmittelbelehrung nach §§ 232 ff. 511 ff. 567 ff. ZPO korrekt formulieren.
- `beschluss-bauen-zpo` — Zivilrechtliche Beschlüsse erstellen: PKH, Streitwert, § 139 ZPO-Hinweis, Kostenfestsetzung.
- `berufungsfest-pruefen` — Fertiges Urteil gegen haeufigste Aufhebungsgruende selbst prüfen.
- `revisionsfest-pruefen` — Revision-Zulassung und absolute Revisionsgruende nach § 547 ZPO prüfen.
- `familienrichter-spezifika` — FamFG-Besonderheiten für Beschluss statt Urteil; Familiengericht-spezifische Normen.
- `cisg-pruefen` — UN-Kaufrecht auf Anwendbarkeit und Eingreifen prüfen.
- `internationales-privatrecht` — Anwendbares Recht bei grenzueberschreitenden Sachverhalten bestimmen (Rom I, Rom II).
- `incoterms-und-gefahruebergang` — Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag prüfen.
- `kollidierende-agb-pruefen` — Battle of the Forms bei beiderseitigen AGB im B2B-Verkehr loesen.
- `dsgvo-rechtswidriges-produkt` — Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen.
- `dokumente-rendern-urteil-docx` — Fertiges Urteil als DOCX im offiziellen Gerichtslayout rendern.
- `schulung-urteilsbauer` — Schulungs-Trainerleitfaden für Ausbilder von Proberichtern und Referendaren.

## Worauf besonders achten

- Tatbestand darf keine Wertungen enthalten; jede Aussage muss einem Beteiligten zugeordnet sein.
- Tenor muss vollstreckbar sein: Ein unklarer oder unbestimmter Tenor fuehrt zur Aufhebung in der Berufung.
- Rechtsmittelbelehrung muss nach Urteilsart (Berufung, Revision, Beschwerde) differenzieren; Fehler fuehren zur Fristerstreckung.
- Vollrelation im Schulstandard folgt strikter Gliederungsreihenfolge; Abweichungen werdenstark benotet.
- IPR-Prüfung muss vor CISG und nationaler Anspruchspruefung erfolgen; falscher Prüfungsrahmen ist Revisionsfehler.

## Typische Fehler

- Tenor ohne Zinslauf: Verzugszinsen müssen Ausgangsbetrag, Zinssatz und Startdatum enthalten; fehlende Angaben sind vollstreckungsrechtlich problematisch.
- Tatbestand mit kopierten Schriftsatzpassagen: Unbearbeitete Uebernahme ohne Zusammenfassung ist nicht tatbestandsgemaess.
- Kostenentscheidung vergessen: Urteil ohne Kostenentscheidung ist unvollstaendig; nachholen nur in Ergaenzungsurteil möglich.
- Hinweispflicht nach § 139 ZPO nicht dokumentiert: Fehlendes Protokoll eines wesentlichen Hinweises ist absolute Berufungsruege.
- FamFG-Beschluss als Urteil erlassen: In Familiensachen ist Urteil unzulaessig; nur Beschluss nach FamFG.

## Quellen und Aktualitaet

- Stand: 05/2026
- ZPO, FamFG, CISG, Rom I-VO, Rom II-VO in aktuell geltender Fassung
- § 511 Abs. 2 Nr. 1 ZPO: Berufungsbeschwer 1.000 EUR (Anhebung durch Justizstandort-Staerkungsgesetz, ab 01.01.2026)
