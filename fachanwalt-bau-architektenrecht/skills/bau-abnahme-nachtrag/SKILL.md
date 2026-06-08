---
name: bau-abnahme-nachtrag
description: "Abnahme Nachtrag im Plugin Fachanwalt Bau Architektenrecht: prüft konkret Einstieg, Schnelltriage und Fallrouting im Fachanwalt Bau, Abnahme, Nachtragsmanagement."
---

# Abnahme Nachtrag

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `allgemein`

**Fokus:** Einstieg, Schnelltriage und Fallrouting im Fachanwalt Bau Architektenrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Fachmodule oder stellt genau eine gezielte Rückfrage.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fachanwalt Bau Architektenrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Maengelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein.

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
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
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
| `erstgespraech-mandatsannahme` | Erstgespraeches-Aufnahme im Bau- und Architektenrecht: Sachverhalt, Vertragstyp, Mangelbild. Normen: §§ 631 633 650a ff. BGB, VOB/B. Prüfraster: Werkvertrag vs. Bauvertrag, Mangelkatalog, Fristen, Interessenlage.… |
| `fachanwalt-bau-architektenrecht-abnahme-mit-vorbehalt` | Abnahme des Bauwerks unter Vorbehalt von Maengeln erklären: Maengelvorbehalt, Sicherungsrechte. Normen: §§ 640 641 BGB, § 12 VOB/B. Prüfraster: Abnahmeprotokoll, Maengelruege, Vorbehalt-Wirkung, Gefahruebergang.… |
| `fachanwalt-bau-architektenrecht-abnahme-verweigerung` | Abnahme des Bauwerks verweigern: wesentliche Maengel als Verweigerungsgrund, Begründungspflicht. Normen: § 640 Abs. 1 S. 2 BGB, § 12 Abs. 3 VOB/B. Prüfraster: wesentlicher Mangel-Begriff, Dokumentation, Fristsetzung,… |
| `fachanwalt-bau-architektenrecht-bauablauf-vbg` | Bauzeitverzoegerung und Bauablaufstoerung nach VOB/B prüfen und geltend machen. Normen: §§ 6 6e VOB/B, §§ 280 286 BGB. Prüfraster: Behinderungsanzeige, Kausalität, Nachweis der Verzoegerung, Schadensberechnung. Output:… |
| `fachanwalt-bau-architektenrecht-bautraeger-insolvenz` | Insolvenz des Bautraegers: Ansprüche des Erwerbers, Schutzrechte, Sicherheitsleistungen. Normen: §§ 648 650u BGB, MaBV, InsO. Prüfraster: Buergschaft oder Grundschuld, Insolvenzforderungsanmeldung,… |
| `fachanwalt-bau-architektenrecht-hoai-honorar-mindestsaetze` | HOAI-Honorar für Architekten und Ingenieure berechnen und Mindestsaetze-Unterschreitung prüfen. Normen: HOAI, §§ 650p ff. BGB. Prüfraster: Leistungsphasen, anrechenbare Kosten, Mindestsaetze nach EuGH-Entscheidung.… |
| `fachanwalt-bau-architektenrecht-kontaminierter-baugrund-bbodschg` | Kontaminierter Baugrund: Haftung, Sanierungspflicht und Kostenverteilung nach BBodSchG. Normen: §§ 4 9 BBodSchG, §§ 633 634 BGB. Prüfraster: Verursacherhaftung, Zustandsstoerer, Sanierungskosten, Gewaehrleistung.… |
| `fachanwalt-bau-architektenrecht-orientierung` | Orientierungs-Skill Bau- und Architektenrecht: richtigen Skill anhand Sachverhalt auswaehlen. Normen: §§ 631 ff. 650a ff. BGB, VOB/B, HOAI. Prüfraster: Vertragstyp, Schadenstyp, Phase Planung/Bau/Abnahme. Output:… |
| `fachanwalt-bau-architektenrecht-vob-schiedsgutachten-schlichtung` | VOB/B-Schiedsgutachten und Schlichtung als Alternative zum Bauprozess nutzen. Normen: §§ 18 Abs. 3 18b VOB/B, §§ 1025 ff. ZPO. Prüfraster: Schiedsgutachter-Auswahl, Bindungswirkung, Fristen, Abgrenzung… |
| `fachanwalt-bau-architektenrecht-werkmangel-pruefen` | Werkmaengel an Bauwerk nach BGB und VOB/B prüfen: Beschaffenheitsvereinbarung, Ist-Zustand, Ursache. Normen: §§ 633 634 640 BGB, § 13 VOB/B. Prüfraster: Mangeldefinition, Dokumentation, Fristsetzung Nacherfuellung,… |
| `mandat-triage-bau-architektenrecht` | Ersteinordnung neuer Mandate im Bau- und Architektenrecht: Mangeltyp, Vertragsgrundlage. Normen: §§ 631 ff. 650a ff. BGB, VOB/B. Prüfraster: Vertragstyp, Beteiligte, Schadenstyp, Fristen, Dringlichkeit. Output:… |
| `nachtragsmanagement-650b` | Nachtragsforderungen des Unternehmers nach § 650b BGB anmelden: Mehrverguetung bei Aenderungsanordnung. Normen: §§ 650b 650c BGB, §§ 1 2 VOB/B. Prüfraster: Aenderungsanordnung, Mehr- oder Minderkosten,… |
| `schriftsatzkern-substantiierung` | Schriftsatzkern im Bau- und Architektenrecht substantiieren: Mangeldarstellung, Normzitate, Beweisangebot. Normen: §§ 253 138 ZPO, §§ 633 634 BGB. Prüfraster: Mangelbezeichnung, Beweismittel, Schluessigkeit. Output:… |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlung im Bau- und Architektenrecht strategisch vorbereiten: Gutachtenlage, Haftungsquoten. Normen: §§ 779 BGB, § 278 ZPO. Prüfraster: Streitpunkte, Gutachtenlage, Vergleichsspielraum, Fristen. Output:… |
| `werkmangel-vob-bgb-pruefen` | Werkmaengel sowohl nach VOB/B als auch nach BGB-Werkvertragsrecht prüfen: Abgrenzung und Parallelprüfung. Normen: §§ 633 634 640 BGB, § 13 VOB/B. Prüfraster: BGB-Mangel vs. VOB/B-Mangel, Gewaehrleistungsfristen,… |

## Qualitätsversprechen

- Arbeite schnell, aber nicht hektisch.
- Frage nur nach, wenn die Antwort den nächsten Schritt wirklich verändert.
- Mache Annahmen sichtbar und halte sie knapp.
- Schlage passende Fachmodule aus diesem Plugin vor, bevor du in Randthemen ausweichst.
- Liefere am Ende immer einen klaren nächsten Schritt.

---

Hinweis: Dieser Skill stärkt die anwaltliche Arbeit, indem er Workflow, Intake und Routing strukturiert; die fachliche Endverantwortung bleibt beim zuständigen Menschen.

## 2. `bau-abnahme-checkliste-workflow`

**Fokus:** Abnahme: technische Abnahme gegen rechtliche Abnahme § 640 BGB, Abnahmevoraussetzungen, Verweigerungsrechte bei wesentlichen Maengeln, fiktive Abnahme § 640 Abs. 2 BGB. Pruefraster und Mustertext für Abnahmeerklaerung.

### Bau: Abnahme-Workflow

## Spezialwissen: Bau: Abnahme-Workflow
- **Normen-/Quellenanker:** BGB.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `bau-nachtrag-workflow`

**Fokus:** Nachtragsmanagement: § 650b BGB Anordnungsrecht, Vergueng nach § 650c BGB, Soll-Ist-Abgleich, Dokumentation Stoerung. Mustertext für Nachtragsschreiben und Schriftsatzbausteine.

### Bau: Nachtrag-Workflow

## Spezialwissen: Bau: Nachtrag-Workflow
- **Normen-/Quellenanker:** BGB.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 4. `workflow-chronologie-und-belegmatrix`

**Fokus:** Chronologie und Belegmatrix im Plugin fachanwalt-bau-architektenrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen.

### Chronologie und Belegmatrix

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

