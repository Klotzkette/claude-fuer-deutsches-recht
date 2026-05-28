---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Betreuungsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Betreuungsrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Betreuungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Betreuungsrechtliche Skills für Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse und Verdachtsverträge nach BtOG und BGB.

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
| `betreuer-als-erbe` | Beraet zur Frage, ob ein Berufsbetreuer testamentarisch bedacht werden darf und welche Folgen sich aus Paragraph 30 BtOG ergeben. Verweist auf Leitentscheidung OLG Nuernberg Beschluss 19.07.2023 Az. 15 Wx 988/23… |
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
- OLG Nuernberg, Beschluss 19.07.2023, Az. 15 Wx 988/23 (§ 30 BtOG und Testierfreiheit)
