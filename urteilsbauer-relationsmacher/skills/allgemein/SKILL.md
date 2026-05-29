---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Urteilsbauer Relationsmacher-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Urteilsbauer und Relationsmacher — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Urteilsbauer Relationsmacher**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Spezial-Skill aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
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
- **Primärer Pfad:** `skill-name` — [warum dieser Skill hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

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
| `aktenintake-zivil` | Eingehende Zivilakte vor erster Prüfung strukturieren: Richter oder Referendar erhalt neue Akte und muss Überblick gewinnen. Normen: § 313 ZPO (Urteilsinhalt), § 286 ZPO (freie Beweiswürdigung), § 139 ZPO (richterliche… |
| `anspruchsgrundlagen-pruefen` | Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz lösen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR… |
| `berufungsfest-pruefen` | Fertiges Urteil gegen häufigste Aufhebungsgründe selbst prüfen: Richter will vor Urteilsversand Aufhebungsrisiken minimieren. Normen: § 529 ZPO (Tatsachenfeststellung Berufung), § 546 ZPO (Rechtsverletzung), § 547 Nr.… |
| `beschluss-bauen-zpo` | Zivilrechtliche Beschluesse erstellen: PKH, Streitwert, Beweis, Hinweis nach § 139 ZPO, Kostenfestsetzung, Versaeumnis, Erledigung. Normen: §§ 127 und 329 und 358 ff. sowie 139 und 103 ff. ZPO. Prüfraster: Unterschied… |
| `beweisbeschluss-vorbereiten` | Beweisbeschluss nach § 359 ZPO vorbereiten: Richter bestimmt Beweisaufnahme nach muendlicher Verhandlung. Normen: § 359 ZPO (Inhalt Beweisbeschluss), § 286 ZPO (Beweislast), §§ 373 ff. ZPO (Zeugen), §§ 402 ff. ZPO… |
| `beweiswuerdigung-mit-richter-input` | Strukturierte Beweiswürdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgründe-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswürdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO… |
| `cisg-pruefen` | UN-Kaufrecht (CISG) auf Anwendbarkeit und Eingreifen prüfen: Internationaler Kaufvertrag mit Auslandsbezug und Vertragsstreit. Normen: CISG Art. 1-6 (Anwendungsbereich), Art. 25 (wesentliche Vertragsverletzung), Art.… |
| `dokumente-rendern-urteil-docx` | Zivilurteil als DOCX im offiziellen Gerichtslayout rendern: Richter oder Referendar will fertiges Urteil als Dokument ausgeben. Normen: § 313 ZPO (Urteilsinhalt und -form). Prüfraster: Gerichtslayout (Aktenzeichen,… |
| `dsgvo-rechtswidriges-produkt` | Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit prüfen: Richter oder Anwalt muss beurteilen ob Smartglasses oder IoT-Produkt DSGVO-konform ist. Normen: Art. 3 DSGVO (räumlicher Anwendungsbereich), Art. 5 Abs. 1 lit.… |
| `entscheidungsgruende-zivil-schreiben` | Entscheidungsgründe eines Zivilurteils im Urteilsstil schreiben: Richter hat Beweise erhoben und muss Begründung formulieren. Normen: § 313 Abs. 3 ZPO (Entscheidungsgründe), § 286 ZPO. Prüfraster: Urteilsstil (kein… |
| `familienrichter-spezifika` | FamFG-Spezifika für Familienrichter anwenden: Richter am Familiengericht muss Beschluss statt Urteil abfassen. Normen: § 38 FamFG (Beschluss), § 137 FamFG (Verbund- und Folgesachen), § 1697a BGB (Kindeswohlprüfung),… |
| `incoterms-und-gefahruebergang` | Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag prüfen: Streit über Transportschaden oder Lieferpflicht. Normen: Incoterms 2020 (FOB, CIF, EXW, DAP, DDP), CISG Art. 31 und 67 ff. (Gefahruebergang).… |
| `internationales-privatrecht` | Anwendbares Recht bei grenzüberschreitenden Vertraegen und Delikten bestimmen: Auslandsbezug im Prozess erfordert IPR-Prüfung. Normen: Rom-I-VO (vertragliche Schuldverhältnisse), Rom-II-VO (außervertragliche), Art. 4… |
| `kollidierende-agb-pruefen` | Kollidierende AGB im B2B-Verkehr (Battle of the Forms) lösen: Kaufvertrag mit beiderseitigen AGB und widerspruechen. Normen: §§ 305-310 BGB (AGB-Recht B2B), CISG Art. 19 (Annahme mit Abweichungen). Prüfraster:… |
| `kostenentscheidung-bauen` | Kostenentscheidung nach §§ 91 ff. ZPO erstellen: Richter muss Kostenquote und -grundentscheidung formulieren. Normen: § 91 ZPO (vollständiges Obsiegen), § 92 ZPO (teilweises Obsiegen), § 100 ZPO (mehrere Beklagte), §… |
| `rechtsmittelbelehrung-zivil` | Rechtsmittelbelehrung nach §§ 232 ff., 511 ff., 567 ff. ZPO korrekt formulieren: Richter muss Belehrung an Urteil oder Beschluss anfuegen. Normen: § 232 ZPO (Belehrungspflicht), § 511 ZPO (Berufung), § 567 ZPO… |
| `relation-zivil` | Zivilrechtliche Relation nach klassischer Relationstechnik erstellen: Referendar oder Richter erstellt Entscheidungsunterlage vor Urteilsabfassung. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht,… |
| `revisionsfest-pruefen` | Prüfung gegen Aufhebung in der Revision: absolute Revisionsgründe Paragraf 547 ZPO Revisionszulassung Paragraf 543 ZPO grundsaetzliche Bedeutung Rechtsfortbildung Sicherung einheitlicher Rechtsprechung.… |
| `schulung-urteilsbauer` | Schulungs-Trainerleitfaden für Plugin urteilsbauer-relationsmacher: Ausbilder plant Schulungstag für Proberichter, Assessoren oder Rechtspfleger. Normen: §§ 313 und 286 und 529 ZPO (Lernziele). Prüfraster: Lernziele,… |
| `tatbestand-zivil-schreiben` | Tatbestand eines Zivilurteils nach § 313 Abs. 2 ZPO schreiben: Richter muss den Prozessstoff sachlich und knapp wiedergeben. Normen: § 313 Abs. 2 ZPO (Tatbestand-Anforderungen), § 314 ZPO (Beweiskraft des Tatbestands).… |
| `tenor-bauen-zivil` | Tenor eines Zivilurteils konstruieren: Richter muss Hauptsache-Entscheidung, Kosten und Vollstreckbarkeit klar tenorieren. Normen: §§ 91 ff. ZPO (Kosten), §§ 708-720a ZPO (vorlaeufige Vollstreckbarkeit), § 511 ZPO… |
| `vollrelation-langfassung` | Vollständige Relation im Schulstandard für Referendar-/Assessorprüfung ausformulieren: Kandidat benoetigt Langfassung mit gutachterlichem Stil. Normen: §§ 253 ff. und 286 und 313 ZPO. Prüfraster: Sachbericht, Auslegung… |
| `vorlaeufige-vollstreckbarkeit` | Anordnung zur vorlaeufigen Vollstreckbarkeit nach §§ 708-720a ZPO bestimmen: Richter muss die richtige Vollstreckbarkeitsermaechtigungs-Formel formulieren. Normen: § 709 ZPO (Sicherheitsleistung 110%), § 711 ZPO… |
| `zulaessigkeit-pruefen` | Zulässigkeit der Zivilklage systematisch prüfen: Richter oder Referendar prüft Prüfstation Zulässigkeit. Normen: § 13 GVG (Rechtsweg), EuGVVO Bruessel Ia (internationale Zuständigkeit), §§ 12 ff. ZPO (örtliche… |

## Worum geht es?

Das Plugin ist eine Urteils- und Beschluss-Werkstatt fuer Richter, Referendare und Rechtspfleger. Es begleitet den vollstaendigen Workflow vom Aktenintake ueber die Relation (Entscheidungsunterlage) bis zum fertigen Urteil als DOCX-Dokument im offiziellen Gerichtslayout. Das Plugin stuetzt die Pruefung von Zulaessigkeit, Anspruchsgrundlagen, Beweiswuerdigung und Kostenentscheidung sowie Rechtsmittelbelehrung.

Spezialisierte Teilmodule decken familiengerichtliche Besonderheiten (FamFG), internationales Privatrecht (IPR), CISG-Sachverhalte, kollidierende AGB und die vorlaeufige Vollstreckbarkeit ab. Ausbildungsmodule unterstuetzen Referendare bei der Vollrelation nach Schulstandard.

## Wann brauchen Sie diese Skill?

- Richter hat neue Zivilakte und will Ueberblick gewinnen, Verfahrensstand klaeren und Anspruchsgrundlagen identifizieren.
- Referendar oder Assessorkandidat erstellt Relation oder Vollrelation fuer Examensvorbereitung.
- Richter muss Beweiswuerdigung nach § 286 ZPO verschriftlichen und dafuer gegliederten Abschnitt in den Entscheidungsgruenden erzeugen.
- Gericht erstellt Beschluss (PKH, Streitwert, Hinweis nach § 139 ZPO) oder Versaumnisurteil.
- Internationaler Kaufvertrag mit CISG- oder IPR-Bezug muss rechtlich eingeordnet werden.

## Fachbegriffe (kurz erklaert)

- **Relation** — Richterliche Entscheidungsunterlage; strukturierte Zusammenfassung von Sach- und Streitstand, Beweisaufnahme und rechtlicher Wuerdigung.
- **Tatbestand (§ 313 Abs. 2 ZPO)** — Pflichtbestandteil des Urteils; sachliche Darstellung des Parteivorbringens ohne Wertung.
- **Entscheidungsgruende (§ 313 Abs. 3 ZPO)** — Rechtliche und tatsaechliche Begruendung des Tenors.
- **Tenor** — Urteilsausspruch; entscheidet ueber Hauptsache, Kosten und vorlaeufige Vollstreckbarkeit.
- **Beweiswuerdigung (§ 286 ZPO)** — Freie Wuerdigung des Ergebnisses der Beweisaufnahme; Kernaufgabe des Gerichts.
- **Vollrelation** — Ausfuehrliche Relation nach Schulstandard fuer Referendars- und Assessor-Pruefung.
- **FamFG** — Gesetz ueber das Verfahren in Familiensachen; regelt Beschlussverfahren in Familiengericht-Sachen.
- **CISG** — UN-Kaufrecht (Convention on Contracts for the International Sale of Goods); gilt fuer grenzueberschreitende Kaufvertraege zwischen Unternehmern aus Vertragsstaaten.

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

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Aktenintake: Akte einlesen, Verfahrensstand und Sachverhalt strukturieren.
2. Zulaessigkeit pruefen: Gerichtliche Zustaendigkeit, Rechtsschutzinteresse, Prozessvoraussetzungen.
3. Anspruchsgrundlagen identifizieren und Pruefungsreihenfolge bestimmen.
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Tenor, Tatbestand, Entscheidungsgruende, Kostenentscheidung und Rechtsmittelbelehrung nacheinander oder geblockt erstellen.

## Skill-Tour (was gibt es hier?)

- `aktenintake-zivil` — Eingehende Zivilakte strukturieren und Ueberblick gewinnen.
- `zulaessigkeit-pruefen` — Zulaessigkeit der Zivilklage systematisch pruefen: Zustaendigkeit, Prozessfaehigkeit, Rechtsschutzinteresse.
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen identifizieren und Pruefungsreihenfolge bei Anspruchskonkurrenz bestimmen.
- `relation-zivil` — Zivilrechtliche Relation nach klassischer Relationstechnik erstellen (Kurz- oder Langfassung).
- `vollrelation-langfassung` — Vollstaendige Relation im Schulstandard fuer Referendar- und Assessorpruefung.
- `beweiswuerdigung-mit-richter-input` — Strukturierte Beweiswuerdigung nach § 286 ZPO mit Richter-Input ausformulieren.
- `beweisbeschluss-vorbereiten` — Beweisbeschluss nach § 359 ZPO vorbereiten.
- `tatbestand-zivil-schreiben` — Tatbestand nach § 313 Abs. 2 ZPO sachlich und knapp ausformulieren.
- `entscheidungsgruende-zivil-schreiben` — Entscheidungsgruende im Urteilsstil schreiben.
- `tenor-bauen-zivil` — Tenor konstruieren: Hauptsache, Kosten, vorlaeufige Vollstreckbarkeit.
- `kostenentscheidung-bauen` — Kostenentscheidung nach §§ 91 ff. ZPO erstellen und Kostenquote bestimmen.
- `vorlaeufige-vollstreckbarkeit` — Richtige Anordnung zur vorlaeufigen Vollstreckbarkeit nach §§ 708 ff. ZPO bestimmen.
- `rechtsmittelbelehrung-zivil` — Rechtsmittelbelehrung nach §§ 232 ff. 511 ff. 567 ff. ZPO korrekt formulieren.
- `beschluss-bauen-zpo` — Zivilrechtliche Beschluesse erstellen: PKH, Streitwert, § 139 ZPO-Hinweis, Kostenfestsetzung.
- `berufungsfest-pruefen` — Fertiges Urteil gegen haeufigste Aufhebungsgruende selbst pruefen.
- `revisionsfest-pruefen` — Revision-Zulassung und absolute Revisionsgruende nach § 547 ZPO pruefen.
- `familienrichter-spezifika` — FamFG-Besonderheiten fuer Beschluss statt Urteil; Familiengericht-spezifische Normen.
- `cisg-pruefen` — UN-Kaufrecht auf Anwendbarkeit und Eingreifen pruefen.
- `internationales-privatrecht` — Anwendbares Recht bei grenzueberschreitenden Sachverhalten bestimmen (Rom I, Rom II).
- `incoterms-und-gefahruebergang` — Incoterms-Klausel und Gefahruebergang in internationalem Kaufvertrag pruefen.
- `kollidierende-agb-pruefen` — Battle of the Forms bei beiderseitigen AGB im B2B-Verkehr loesen.
- `dsgvo-rechtswidriges-produkt` — Produkt aus dem Ausland auf DSGVO-Rechtswidrigkeit pruefen.
- `dokumente-rendern-urteil-docx` — Fertiges Urteil als DOCX im offiziellen Gerichtslayout rendern.
- `schulung-urteilsbauer` — Schulungs-Trainerleitfaden fuer Ausbilder von Proberichtern und Referendaren.

## Worauf besonders achten

- Tatbestand darf keine Wertungen enthalten; jede Aussage muss einem Beteiligten zugeordnet sein.
- Tenor muss vollstreckbar sein: Ein unklarer oder unbestimmter Tenor fuehrt zur Aufhebung in der Berufung.
- Rechtsmittelbelehrung muss nach Urteilsart (Berufung, Revision, Beschwerde) differenzieren; Fehler fuehren zur Fristerstreckung.
- Vollrelation im Schulstandard folgt strikter Gliederungsreihenfolge; Abweichungen werdenstark benotet.
- IPR-Pruefung muss vor CISG und nationaler Anspruchspruefung erfolgen; falscher Pruefungsrahmen ist Revisionsfehler.

## Typische Fehler

- Tenor ohne Zinslauf: Verzugszinsen muessen Ausgangsbetrag, Zinssatz und Startdatum enthalten; fehlende Angaben sind vollstreckungsrechtlich problematisch.
- Tatbestand mit kopierten Schriftsatzpassagen: Unbearbeitete Uebernahme ohne Zusammenfassung ist nicht tatbestandsgemaess.
- Kostenentscheidung vergessen: Urteil ohne Kostenentscheidung ist unvollstaendig; nachholen nur in Ergaenzungsurteil moeglich.
- Hinweispflicht nach § 139 ZPO nicht dokumentiert: Fehlendes Protokoll eines wesentlichen Hinweises ist absolute Berufungsruege.
- FamFG-Beschluss als Urteil erlassen: In Familiensachen ist Urteil unzulaessig; nur Beschluss nach FamFG.

## Querverweise

- Plugin `zwangsvollstreckung` — Vollstreckbarkeit des erlassenen Urteils und Vollstreckungsklausel pruefen.
- Plugin `forderungsmanagement-klagewerkstatt` — Klageschriften und Antraege, die zum Urteil fuehren.
- Plugin `email-umformulierer-berufsrecht` — Berufsrechtliche Korrespondenz neben dem Gerichtsverfahren.

## Quellen und Aktualitaet

- Stand: 05/2026
- ZPO, FamFG, CISG, Rom I-VO, Rom II-VO in aktuell geltender Fassung
- § 511 Abs. 2 Nr. 1 ZPO: Berufungsbeschwer 1.000 EUR (Anhebung durch Justizstandort-Staerkungsgesetz, ab 01.01.2026)
