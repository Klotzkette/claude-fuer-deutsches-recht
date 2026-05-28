---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Insolvenzplan Starug Planwerkstatt-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Insolvenzplan und StaRUG-Planwerkstatt — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Insolvenzplan Starug Planwerkstatt**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug.

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
| `ips-abstimmung-mehrheiten` | Abstimmungsmehrheiten für Insolvenzplan nach InsO und Restrukturierungsplan nach StaRUG simulieren und Abstimmungstermin vorbereiten. §§ 244 245 InsO Kopf- und Summenmehrheit §§ 25 26 StaRUG Klassenmehrheit.… |
| `ips-anlagenpaket` | Pflichtanlagen für Insolvenzplan oder StaRUG-Plan vollständig zusammenstellen. §§ 229 230 InsO §§ 14 15 StaRUG Planunterlagen. Prüfraster: Pflichtanlagen je Route Vermögensuebersicht Finanzplan Erklärungen… |
| `ips-asset-deals-im-plan-grundstuecke-marken-kundendaten` | Asset-Deals im Insolvenzplan strukturieren wenn Grundstuecke Marken oder Kundendaten uebertragen werden sollen. §§ 311b 398 BGB §§ 27 ff. MarkenG § 15 PatG. Prüfraster: Übertragungsgegenstand Formerfordernis Grundbuch… |
| `ips-cramdown-obstruktion` | Obstruktionsverbot und gruppenuebergreifende Mehrheitsentscheidung prüfen wenn ablehnende Gruppen oder Klassen den Plan blockieren. § 245 InsO § 27 StaRUG Cramdown. Prüfraster: Schlechterstellung angemessene… |
| `ips-darstellender-teil` | Darstellenden Teil des Insolvenzplans oder StaRUG-Plans vollständig verfassen. § 220 InsO § 6 StaRUG Darstellungspflichten. Prüfraster: Krisengeschichte Massnahmen Finanzplanung Vergleichsrechnung Sonderaktiva… |
| `ips-datenraum-register` | Planbegleitenden Datenraum aufbauen und Dokumentenregister führen damit alle Planbausteine belegbar sind. §§ 218 229 InsO §§ 14 15 StaRUG Planunterlagen. Prüfraster: Pflichtunterlagen Jahresabschluesse BWA OPOS… |
| `ips-gerichtliche-schritte` | Gerichtliche Verfahrensschritte für Insolvenzplan und StaRUG-Plan steuern von Einreichung bis Planbestätigung. §§ 231 232 248 InsO §§ 45 ff. StaRUG Gerichtsverfahren. Prüfraster: Einreichung Vorprüfung… |
| `ips-gestaltender-teil` | Gestaltenden Teil des Insolvenzplans oder StaRUG-Plans mit konkreten Rechtsaenderungen Quoten und Vollstreckungsgrundlagen formulieren. § 221 InsO § 7 StaRUG Planwirkungen. Prüfraster: Rechtsaenderungen je Gruppe… |
| `ips-gruppen-klassenbildung` | Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden. §§ 222 223 InsO §§ 9 10 StaRUG Klassenbildung. Prüfraster: Rechtsstellung Absonderung Insolvenzgläubiger Nachrang Anteilsinhaber Gruppeninterne… |
| `ips-insolvenzplan-architektur` | Vollständigen Insolvenzplan nach §§ 217 ff. InsO strukturieren und alle Pflichtbestandteile verbinden. §§ 217 220 221 InsO Planarchitektur §§ 222 229 InsO Gruppen und Anlagen. Prüfraster: Planvorlageberechtigung… |
| `ips-integrierte-planung` | Integrierte Planrechnung aus GuV Liquiditaet und Bilanz für Insolvenzplan oder StaRUG erstellen. §§ 220 229 InsO §§ 14 StaRUG Finanzplanung. Prüfraster: Ist-Zahlen Planannahmen Base-Case Stressszenarien Brückenrechnung… |
| `ips-kaltstart-interview` | Insolvenzplan- oder StaRUG-Mandat durch strukturiertes Erstgespraech aufgleisen wenn Unterlagen fehlen. §§ 13 15a InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft… |
| `ips-kommandocenter` | Insolvenzplan- oder StaRUG-Mandat starten und Verfahrensroute Ampelstatus und naechste Schritte bestimmen. §§ 217 218 InsO §§ 29 ff. StaRUG. Prüfraster: Rolle Verfahrensziel Datenraumstand Zahlenstand Stakeholder… |
| `ips-minderheitenschutz` | Schlechterstellungsrisiken opponierender Beteiligter analysieren und Planangriffe durch Minderheitenschutzprüfung abwenden. § 251 InsO § 64 StaRUG Minderheitenschutz. Prüfraster: individuelle Schlechterstellung… |
| `ips-planbetroffene-auswahl` | Planbetroffene im StaRUG-Verfahren sachgerecht auswaehlen und Nichteinbeziehung dokumentiert begründen. §§ 2 4 StaRUG Gestaltbarkeit Ausnahmen. Prüfraster: gestaltbare Rechtsverhältnisse Ausnahmen Arbeitnehmer… |
| `ips-planvollzug-monitoring` | Planvollzug nach Bestätigung ueberwachen Zahlungen kontrollieren und Abweichungen dokumentieren. §§ 248 261 InsO Planueberwachung §§ 69 72 StaRUG. Prüfraster: Bedingungen Fälligkeiten Quoten Zahlstellen Covenants… |
| `ips-redteam-qualitygate` | Insolvenzplan oder StaRUG-Plan vor Einreichung aus Gegnersicht und Gerichtssicht prüfen. §§ 231 245 251 InsO Versagungsgründe § 64 StaRUG. Prüfraster: Vollständigkeit Bewertungswiderspruch Gruppenmissbrauch fehlende… |
| `ips-sanierungskonzept` | Sanierungskonzept als wirtschaftliche Grundlage für Insolvenzplan oder StaRUG erstellen oder prüfen. §§ 220 229 InsO §§ 6 14 StaRUG Fortbestehensfähigkeit. Prüfraster: Krisenstadium Ursachen Leitbild Massnahmenpakete… |
| `ips-sicherheiten-drittsicherheiten` | Absonderungsrechte und Drittsicherheiten im Insolvenzplan und StaRUG planfest behandeln und Ausfallwerte bestimmen. §§ 49 50 51 224 InsO §§ 2 Abs. 4 StaRUG Drittsicherheiten. Prüfraster: Sicherheitenregister… |
| `ips-stabilisierung-starug` | StaRUG-Stabilisierungsmassnahmen beantragen wenn Vollstreckungsdruck die Planarbeit gefaehrdet. §§ 49 50 51 StaRUG Stabilisierungsanordnung. Prüfraster: Stabilisierungsbedarf Verhältnismäßigkeit Gläubiger Dauer… |
| `ips-stakeholder-kommunikation` | Gläubiger Banken Arbeitnehmer Lieferanten Gericht und Investoren zielgruppengerecht über Insolvenzplan oder StaRUG informieren. §§ 232 235 InsO §§ 17 20 StaRUG Gläubigerinfo. Prüfraster: Stakeholdergruppen Sorgen… |
| `ips-starug-plan-architektur` | Vollständigen StaRUG-Restrukturierungsplan strukturieren von Planbetroffenenauswahl bis Bestätigungspfad. §§ 6 7 8 StaRUG Planinhalt §§ 60 ff. StaRUG Abstimmung Gerichtsverfahren. Prüfraster: Restrukturierungsfähigkeit… |
| `ips-steuern-bilanz-folgen` | Steuerliche und bilanzielle Folgen des Plans prüfen damit Planwirkungen nicht an Nebenfolgen scheitern. §§ 3a 3c EStG Sanierungsgewinn § 8c KStG Verlustvortrag. Prüfraster: Erlass Stundung Debt-Equity-Swap Bilanzierung… |
| `ips-verfahrenswahl` | Passenden Sanierungsrahmen auswaehlen und Insolvenzplan Eigenverwaltung Schutzschirm StaRUG und außergerichtliche Einigung vergleichen. §§ 270 270d InsO §§ 29 42 StaRUG. Prüfraster: Zahlungsunfähigkeit Masse… |
| `ips-vergleichsrechnung` | Vergleichsrechnung als Herzstuck des Plans erstellen: Planfall gegen Ohne-Plan-Szenario je Gruppe oder Klasse. §§ 220 229 InsO § 6 Abs. 2 StaRUG Schlechterstellungsverbot. Prüfraster: Masse Kosten Sicherheiten… |
| `sanierungsmoderation-94-starug` | Sanierungsmoderation nach § 94 StaRUG vorbereiten und durchführen wenn außergerichtliche Einigung mit moderierender Instanz angestrebt wird. §§ 94 ff. StaRUG Sanierungsmoderation. Prüfraster: Antrag… |

## Worum geht es?

Dieses Plugin ist das spezialisierte Werkzeug fuer die Erstellung, Pruefung und Begleitung von Insolvenzplaenen nach §§ 217 ff. InsO und Restrukturierungsplaenen nach dem StaRUG (Unternehmensstabilisierungs- und -restrukturierungsgesetz). Es deckt den gesamten Planlebenszyklus ab: vom Kaltstart-Interview und der Verfahrenswahl ueber die Planarchitektur, Vergleichsrechnung und Gruppenbildung bis zur Abstimmung, dem Cramdown-Verfahren und dem Planvollzug.

Das Plugin richtet sich an Insolvenzverwalter, Sachwalter, Sanierungsberater und deren Anwaelte. Es ist kein Rechtsberatungsersatz, sondern ein strukturiertes Pruefwerkzeug fuer komplexe Sanierungsmandate. Fuer die parallele Bearbeitung einfacherer insolvenzrechtlicher Grundfragen steht das Plugin `insolvenzrecht` zur Verfuegung.

## Wann brauchen Sie diese Skill?

- Sie stehen am Beginn eines Restrukturierungsmandats und muessen zwischen Insolvenzplan, Eigenverwaltung, Schutzschirm, StaRUG und aussergerichtlicher Einigung auswaehlen.
- Sie erstellen oder pruefe den darstellenden und gestaltenden Teil eines Insolvenzplans oder StaRUG-Plans.
- Sie muessen Gruppen und Klassen nach §§ 222 f. InsO oder §§ 9 f. StaRUG sachgerecht bilden.
- Sie simulieren Abstimmungsmehrheiten oder pruefen Cramdown-Szenarien nach § 245 InsO oder § 27 StaRUG.
- Sie begleiten den Planvollzug und muessen Abweichungen von Quoten und Covenants dokumentieren.

## Fachbegriffe (kurz erklaert)

- **Insolvenzplan** — Gestaltendes Instrument nach §§ 217 ff. InsO, mit dem Glaeubiger abweichend vom Regelverfahren befriedigt werden; besteht aus darstellendem und gestaltendem Teil plus Anlagen.
- **StaRUG-Plan** — Restrukturierungsplan nach dem StaRUG; ermoeglicht Eingriffe in Glaeubigerpositionen ausserhalb des Insolvenzverfahrens bei bloss drohender Zahlungsunfaehigkeit.
- **Vergleichsrechnung** — Kernbestandteil des Plans; zeigt je Gruppe, dass kein Beteiligter im Plan schlechter steht als ohne Plan (Schlechterstellungsverbot).
- **Cramdown** — Gruppenuebergreifende Mehrheitsentscheidung, die eine ablehnende Gruppe ueberstimmt (§ 245 InsO, § 27 StaRUG); setzt absolute Prioritaet oder angemessene Beteiligung voraus.
- **Planbetroffene** — Im StaRUG-Verfahren ausdrucklich ausgewaehlte Inhaber gestaltbarer Rechtsverhaeltnisse (§§ 2 ff. StaRUG).
- **Sanierungsmoderation** — Aussergerichtliches Verfahren nach §§ 94 ff. StaRUG mit gerichtlich bestelltem Moderator.
- **Integrierte Planung** — Verknuepfte Finanzplanung aus GuV, Liquiditaet und Bilanz als wirtschaftliche Grundlage fuer den Plan.
- **Planvollzug** — Phase nach Planbestaetigung; umfasst Zahlungen, Covenants und Monitoring nach §§ 248 und 261 InsO.

## Rechtsgrundlagen

- §§ 217 bis 269 InsO — Insolvenzplan (Architektur, Gruppen, Anlagen, Abstimmung, Bestaetigung, Vollzug).
- §§ 244 und 245 InsO — Abstimmungsmehrheiten und Obstruktionsverbot (Cramdown).
- § 251 InsO — Minderheitenschutz.
- §§ 261 und 268 InsO — Planueberwachung.
- §§ 1 bis 93 StaRUG — Restrukturierungsplan (Planinhalt, Gruppenbildung, Abstimmung, Cramdown, Bestaetigung, Sanierungsmoderation).
- §§ 3a und 3c EStG — Sanierungsgewinn und steuerliche Folgen.
- § 8c KStG — Verlustvortraege bei Anteilsuebertragung.

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Kaltstart-Interview durchfuehren: Skill `ips-kaltstart-interview` fuer fehlende Unterlagen.
2. Verfahrenswahl treffen: Skill `ips-verfahrenswahl` (InsO-Plan, StaRUG, aussergerichtlich).
3. Planarchitektur aufbauen: `ips-insolvenzplan-architektur` oder `ips-starug-plan-architektur`.
4. Vergleichsrechnung und Gruppen: `ips-vergleichsrechnung` und `ips-gruppen-klassenbildung`.
5. Red-Team-Pruefung vor Einreichung: `ips-redteam-qualitygate`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Steuerung**

- `ips-kommandocenter` — Mandat starten, Verfahrensroute und Ampelstatus bestimmen.
- `ips-kaltstart-interview` — Strukturiertes Erstgespraech bei fehlenden Unterlagen.
- `ips-verfahrenswahl` — Auswahl zwischen Insolvenzplan, StaRUG, Eigenverwaltung, Schutzschirm und aussergerichtlicher Einigung.

**Planarchitektur**

- `ips-insolvenzplan-architektur` — Vollstaendigen Insolvenzplan nach §§ 217 ff. InsO strukturieren.
- `ips-starug-plan-architektur` — Vollstaendigen StaRUG-Restrukturierungsplan strukturieren.
- `ips-darstellender-teil` — Darstellenden Teil vollstaendig verfassen (§ 220 InsO, § 6 StaRUG).
- `ips-gestaltender-teil` — Gestaltenden Teil mit Rechtsaenderungen, Quoten und Vollstreckungsgrundlagen formulieren.
- `ips-anlagenpaket` — Pflichtanlagen vollstaendig zusammenstellen.

**Gruppen und Klassen**

- `ips-gruppen-klassenbildung` — Abstimmungsgruppen nach InsO und Klassen nach StaRUG sachgerecht bilden.
- `ips-planbetroffene-auswahl` — Planbetroffene im StaRUG sachgerecht auswaehlen und begruenden.

**Wirtschaftliche Grundlagen**

- `ips-sanierungskonzept` — Sanierungskonzept als wirtschaftliche Grundlage erstellen oder pruefen.
- `ips-integrierte-planung` — Integrierte Planrechnung aus GuV, Liquiditaet und Bilanz erstellen.
- `ips-vergleichsrechnung` — Vergleichsrechnung (Planfall vs. Ohne-Plan-Szenario) je Gruppe erstellen.
- `ips-steuern-bilanz-folgen` — Steuerliche und bilanzielle Folgen des Plans pruefen.

**Sicherheiten und Dritte**

- `ips-sicherheiten-drittsicherheiten` — Absonderungsrechte und Drittsicherheiten planfest behandeln.
- `ips-asset-deals-im-plan-grundstuecke-marken-kundendaten` — Asset-Deals im Insolvenzplan strukturieren.

**Abstimmung und Durchsetzung**

- `ips-abstimmung-mehrheiten` — Abstimmungsmehrheiten simulieren und Abstimmungstermin vorbereiten.
- `ips-cramdown-obstruktion` — Obstruktionsverbot und gruppenuebergreifende Mehrheitsentscheidung pruefen.
- `ips-minderheitenschutz` — Schlechterstellungsrisiken opponierender Beteiligter analysieren.

**Gerichtliche Schritte und Stabilisierung**

- `ips-gerichtliche-schritte` — Gerichtliche Verfahrensschritte von Einreichung bis Planbestaetigung steuern.
- `ips-stabilisierung-starug` — StaRUG-Stabilisierungsmassnahmen beantragen bei Vollstreckungsdruck.

**Kommunikation und Dokumentation**

- `ips-stakeholder-kommunikation` — Glaeubiger, Banken, Arbeitnehmer und Gericht zielgruppengerecht informieren.
- `ips-datenraum-register` — Planbegleitenden Datenraum aufbauen und Dokumentenregister fuehren.

**Qualitaetssicherung und Planvollzug**

- `ips-redteam-qualitygate` — Plan vor Einreichung aus Gegnersicht und Gerichtssicht pruefen.
- `ips-planvollzug-monitoring` — Planvollzug ueberwachen, Zahlungen kontrollieren und Abweichungen dokumentieren.

**Sanierungsmoderation**

- `sanierungsmoderation-94-starug` — Sanierungsmoderation nach § 94 StaRUG vorbereiten und durchfuehren.

## Worauf besonders achten

- **Vergleichsrechnung ist Herzstuck** — Ohne belastbare Vergleichsrechnung wird der Plan nicht bestaetigt; Annahmenregister und Stressszenarien muessen dokumentiert sein.
- **StaRUG nur bei drohender Zahlungsunfaehigkeit** — § 18 InsO ist Voraussetzung; bei eingetretener Zahlungsunfaehigkeit oder Ueberschuldung ist InsO-Antragspflicht zu pruefen.
- **Cramdown-Risiko fruehzeitig managen** — Ablehnende Klassen fruhzeitig identifizieren und Planmehrwert-Argument oder absolute Prioritaet vorbereiten.
- **Steuerfolgen nicht unterschaetzen** — Sanierungsgewinn (§ 3a EStG) und Verlustvortragsbeschraenkung (§ 8c KStG) koennen den Planmehrwert aufzehren; Steuerberater fruehzeitig einbinden.
- **Artverschiedenheit InsO und StaRUG** — Planbetroffene und Gruppenbildung folgen verschiedenen Logiken; Verwechslungen fuehren zu Versagungsgruenden.

## Typische Fehler

- Vergleichsrechnung stuetzt sich auf nicht dokumentierte Annahmen; Gericht verlangt Plausibilitaetsnachweis.
- Gruppenbildung folgt nicht wirtschaftlichen Interessen, sondern praktischen Erwaegungen; Missbrauchsvorwurf.
- Anlagenpaket ist unvollstaendig bei Einreichung; Vorpruefungsversagung nach § 231 InsO.
- Planbetroffene im StaRUG umfassen Arbeitnehmer oder Deliktsglaeubiger, die ausgenommen sein muessen (§ 4 StaRUG).
- Red-Team-Pruefung wird uebersprungen; Fehler werden erst vom gegnerischen Anwalt oder Gericht erkannt.

## Querverweise

- `insolvenzrecht` — Fuer Grundfragen zu Eroeffnungsgruenden, Antragspflicht, Anfechtungsrechten.
- `bereicherungs-und-anfechtungsrecht-pruefer` — Fuer Anfechtungsansprueche gegen Zahlungen vor Antrag.
- `kartellrecht-marktabgrenzung-pruefung` — Bei Restrukturierungen mit kartellrechtlich relevantem Marktaustritt.

## Quellen und Aktualitaet

- Stand: 05/2026
- InsO §§ 217 ff. in der geltenden Fassung
- StaRUG in der geltenden Fassung
- EStG §§ 3a und 3c; KStG § 8c
