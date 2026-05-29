---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Betreuungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, routet in passende Spezial-Skills oder stellt genau eine gezielte Rückfrage."
---

<!-- konvers-stil-v1 -->

## Konversationsstil – konzis starten, schnell zum Dokument

- **Erste Antwort kurz.** Sachverhalt einordnen, höchstens **eine** unverzichtbare Rückfrage stellen, dann arbeiten.
- **Kein Lehrbuch-Intro.** Keine Norm-Wiederholung, keine Selbstankündigung – sofort einsteigen.
- **Schnell zum Dokument.** Sobald die Mindestangaben vorliegen, liefere einen ersten Entwurf mit `[noch zu klären: …]`-Platzhaltern, statt weiter abzufragen.
- **Allgemein-Skill = Einstieg, nicht Vorlesung.** Triage, Rückfrage falls nötig, dann auf die Spezial-Skills dieses Plugins verweisen oder direkt den ersten Entwurf produzieren.
- **Ausführlich nur, wenn es das Arbeitsergebnis verlangt:** echte Subsumtion im Gutachtenstil, Tabellen, Chronologien, Risiko-/Beweislastanalysen, Schriftsatz- oder Memo-Text.
- **Erklärungen nur auf Nachfrage.** Wenn der Nutzer Hintergrund will, ausführlich. Sonst nicht.



# Betreuungsrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Betreuungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Betreuungsrechtliche Skills für Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse und Verdachtsverträge nach BtOG und BGB.

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
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `betreuer-registrierung` | Erklärt die Abgrenzung beruflicher / ehrenamtlicher (privater) Betreuer nach BtOG seit 01.01.2023 sowie den Weg zur Registrierung als beruflicher Betreuer nach Paragraphen 23 ff. BtOG und der… |
| `betreuungsrecht-kaltstart-interview` | Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md mit Angaben zur Betreuerrolle (Berufsbetreuer /… |
| `genehmigungspflicht-pruefung` | Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung,… |
| `jahresbericht-betreuungsgericht` | Jahresbericht für Betreuungsgericht nach § 1840 BGB erstellen: Anwendungsfall Betreuer muss jaehrlichen Rechenschaftsbericht über persoenliche und wirtschaftliche Verhältnisse der betreuten Person beim… |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen in Betreuungsfällen auf Missbrauch prüfen: Anwendungsfall Betreuer oder Betreuungsgericht hat Verdacht auf ungewöhnliche Zahlungen verdächtige Dauerverträge oder Anlagegeschäfte zum… |
| `vermoegensverzeichnis-pruefung` | Vermögensverzeichnis für Betreuung prüfen und erstellen: Anwendungsfall Betreuer muss nach § 1835 BGB Vermögensverzeichnis aufnehmen oder bestehendes Verzeichnis auf Vollständigkeit und Richtigkeit prüfen. § 1835 BGB… |

## Worum geht es?

Das Betreuungsrecht regelt die rechtliche Fuersorge fuer Erwachsene, die ihre Angelegenheiten ganz oder teilweise nicht selbst besorgen koennen. Seit der Reform zum 01.01.2023 gilt das Betreuungsorganisationsgesetz (BtOG) neben den materiellen Normen der §§ 1814 ff. BGB. Das Reformgesetz staerkt das Selbstbestimmungsrecht der betreuten Person, praezisiert die Pflichten des Betreuers und regelt erstmals umfassend die Registrierung und Verguetung beruflicher Betreuer.

Dieses Plugin unterstuetzt Berufsbetreuer, Vereins- und Behoerdenbetreuer sowie deren Rechtsbeistande bei der taeglich anfallenden Dokumentations-, Berichts- und Genehmigungsarbeit gegenueber dem Betreuungsgericht.

## Wann brauchen Sie diese Skill?

- Sie sind neu im Betreuungsrecht und moechten einen strukturierten Einstieg in Zustaendigkeiten, Aufgabenkreise und Pflichten.
- Sie sind bereits Betreuer und wollen pruefen, welches Rechtsgeschaeft genehmigungspflichtig ist.
- Sie muessen den jaehrlichen Rechenschaftsbericht nach § 1840 BGB fuer das Betreuungsgericht erstellen.
- Sie haben Zweifel, ob Kontobewegungen oder Vertraege der betreuten Person auf Missbrauch hindeuten.
- Sie moechten wissen, ob Sie als Berufsbetreuer testamentarisch bedacht werden duerfen.

## Fachbegriffe (kurz erklaert)

- **Betreuer** — vom Betreuungsgericht bestellte Person (§ 1814 BGB), die die betreute Person in bestimmten Aufgabenkreisen rechtlich vertritt.
- **Aufgabenkreis** — der konkret durch das Gericht festgelegte Wirkungsbereich des Betreuers (z.B. Vermögenssorge, Gesundheitssorge, Aufenthaltsbestimmung).
- **Berufsbetreuer** — registrierter Betreuer nach §§ 23 ff. BtOG, der Betreuungen entgeltlich fuehrt und bestimmte Sachkundeanforderungen erfuellt.
- **Genehmigungsvorbehalt** — Rechtsgeschaefte, die der Betreuer nur mit vorheriger Zustimmung des Betreuungsgerichts vornehmen darf (§§ 1848 ff. BGB).
- **Vermögensverzeichnis** — Aufstellung aller Vermoegensgegenstaende und Verbindlichkeiten der betreuten Person bei Amtsuebernahme (§ 1835 BGB).
- **Jahresbericht** — jaehrliche Rechenschaftspflicht des Betreuers gegenueber dem Betreuungsgericht (§ 1840 BGB).
- **VBVG** — Verguetung beruflicher Betreuer nach dem Vormuendervergueturgsgesetz; stundenbasierte Pauaschaelen je nach Vermoegenslage und Wohnort der betreuten Person.

## Rechtsgrundlagen

- § 1814 BGB — Betreuerbestellung
- §§ 1816 ff. BGB — Auswahl und Eignung des Betreuers
- §§ 1835 ff. BGB — Vermögensverzeichnis und Rechnungslegung
- §§ 1839-1841 BGB — Rechnungslegungspflichten
- § 1840 BGB — Jahresbericht
- §§ 1848 ff. BGB — Genehmigungspflichtige Rechtsgeschaefte
- § 30 BtOG — Verbot des Erwerbs von Vermoegensvorteilen
- §§ 23 ff. BtOG — Registrierung als Berufsbetreuer
- VBVG — Verguetung beruflicher Betreuer

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Handelt es sich um einen Berufsbetreuer, einen ehrenamtlichen Betreuer oder um Angehoerige, die einen Betreuer einsetzen lassen wollen?
2. Phase des Mandats bestimmen: Ersteinrichtung (Registrierung, Vermögensverzeichnis), laufende Betreuung (Jahresbericht, Genehmigungen) oder Krisenfall (Missbrauchsverdacht, Erbschaftsfragen)?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Genehmigungsantraege nach §§ 1848 ff. BGB sind vor der Massnahme einzuholen; Jahresbericht hat gerichtliche Einreichungsfristen.
5. Anschluss-Skill bestimmen: Nach Jahresbericht ggf. Vermoegensverzechnis-Pruefung; nach Missbrauchsverdacht ggf. Genehmigungspflicht-Pruefung.

## Skill-Tour (was gibt es hier?)

- `betreuungsrecht-kaltstart-interview` — Ersteinrichtung des Plugins: Praxisprofil mit Betreuerrolle, Gericht und Aufgabenkreisen anlegen.
- `betreuer-registrierung` — Erklaert Registrierungsweg, Sachkundeanforderungen und Berufshaftpflicht fuer Berufsbetreuer nach BtOG.
- `genehmigungspflicht-pruefung` — Prueft, ob ein konkretes Rechtsgeschaeft der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB).
- `jahresbericht-betreuungsgericht` — Erstellt den vollstaendigen Jahresbericht nach § 1840 BGB fuer das Betreuungsgericht.
- `vermoegensverzeichnis-pruefung` — Erstellt und prueft das Vermögensverzeichnis nach § 1835 BGB bei Amtsuebernahme oder Kontrollpruefung.
- `kontodaten-vertragsverdacht-pruefung` — Forensische Pruefung von Kontobewegungen und Vertraegen auf Missbrauch zum Nachteil der betreuten Person.
- `betreuer-als-erbe` — Beraet zur Zulaessigkeit testamentarischer Zuwendungen an Berufsbetreuer nach § 30 BtOG.

## Worauf besonders achten

- **Genehmigung vor der Massnahme**: Genehmigungspflichtige Rechtsgeschaefte (§§ 1848 ff. BGB) darf der Betreuer erst nach Erteilung der Genehmigung vornehmen; ein nachtraegliches Genehmigungsverfahren ist nur in engen Ausnahmefaellen moeglich.
- **Sachkundenachweis bei Berufshaftpflicht**: Berufsbetreuer muessen 250.000 EUR Deckung je Schadensfall und 1.000.000 EUR jaehrlich nachweisen (§ 23 BtOG); Luecken in der Versicherung gefaehrden die Registrierung.
- **Subsidiaritaet**: Ein Berufsbetreuer darf nur bestellt werden, wenn geeignete ehrenamtliche oder Angehoerigenbetreuer nicht zur Verfuegung stehen (§ 1816 Abs. 5 BGB).
- **Trennung von Betreuervermoegen und eigenem Vermoegen**: Einnahmen und Ausgaben der betreuten Person sind lueckenlos zu dokumentieren; Verminschung mit eigenem Vermoegen ist ein Haftungsrisiko nach § 1833 BGB.
- **§ 30 BtOG-Verbot**: Berufsbetreuer duerfen sich von der betreuten Person keine Vermoegensvorteile versprechen oder gewähren lassen; Verstoss ist berufsrechtlich relevant.

## Typische Fehler

- Jahresbericht und Rechnungslegung werden zusammengeworfen: § 1840 BGB (Jahresbericht zur persoenlichen Situation) und §§ 1841 ff. BGB (Rechnungslegung ueber das Vermoegen) sind getrennte Pflichten.
- Genehmigungen werden nach der Massnahme beantragt: Insbesondere bei Grundstuecksveraeusserungen und Heimvertraegen laeuft der Betreuer in eine Unwirksamkeitsfalle.
- Vermögensverzeichnis wird bei Amtsantritt vergessen oder unvollstaendig aufgestellt: Das Gericht kann spaeter keine Veraenderungen mehr nachvollziehen.
- Berufsrechtliche Konsequenzen von § 30 BtOG werden unterschaetzt: Ein Testament zugunsten des Betreuers ist zivilrechtlich nicht automatisch nichtig (OLG Nuernberg 19.07.2023), kann aber berufsrechtliche Folgen nach § 27 BtOG ausloesen.
- Subsidiaritaetsprinzip wird nicht geprueft: Wenn ein geeigneter Angehoeriger vorhanden ist, darf kein Berufsbetreuer bestellt werden.

## Querverweise

- `arbeitsrecht` — Fragen zur Verguetung des Betreuers und zur sozialversicherungsrechtlichen Einordnung beruflicher Betreuer.
- `prozessrecht` — Wenn eine betreute Person selbst Klage erhebt oder verklagt wird und der Betreuer als gesetzlicher Vertreter auftritt.
- `schriftform-und-textform-bgb` — Formanforderungen fuer betreuungsrechtlich relevante Erklaerungen (z.B. Kuendigungen von Mietvertraegen).

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB §§ 1814 ff. in der Fassung ab 01.01.2023 (BtOG-Reform)
- BtOG in der Fassung ab 01.01.2023
- VBVG in der aktuellen Fassung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
