---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Gesellschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Gesellschaftsrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gesellschaftsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen.

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
| `aufsichtsrat-protokoll` | Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat. Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt… |
| `dd-findings-extraktion` | Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum prüfen, DD-Issues extrahieren aus [Ordner],… |
| `dealteam-zusammenfassung` | Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update,… |
| `geschaeftsfuehrer-haftung-43-gmbhg` | Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG.… |
| `gesellschafterbeschluss` | Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG… |
| `gesellschafterstreit-loesungsstrategie` | Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38… |
| `gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach… |
| `gesellschaftsrecht-anpassen` | Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A /… |
| `gesellschaftsrecht-kaltstart-interview` | Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen,… |
| `gesellschaftsrecht-mandat-arbeitsbereich` | Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats sauber von jedem anderen trennen. Wird von allen… |
| `gmbh-gruendung` | Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei… |
| `handelsregisteranmeldung` | Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen;… |
| `integrations-management` | Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste.… |
| `ki-werkzeug-uebergabe` | KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer „Luminance\", „Kira\", „KI-Prüfung\", „automatische Extraktion\" oder „Massenprüfung\" erwähnt oder der Datenraum mehr als ~50… |
| `mandat-triage-gesellschaftsrecht` | Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert… |
| `schriftliche-beschlussfassung` | Entwirft Beschlüsse im schriftlichen Verfahren (§ 48 Abs. 2 GmbHG) oder Umlaufbeschlüsse im Hausstil mit Präzedenzsuche im Beschlussarchiv. Bei der AG: Hinweis, dass HV-Beschlüsse Präsenz oder virtuelle HV (§ 118a… |
| `tabellenpruefung` | Tabellarisches Vertragsreview als Prompt-Matrix — pro Spalte ein Extraktionsprompt (was wird gefragt), pro Zeile ein dokumentspezifischer Prompt (wie wird dieses Dokument behandelt). Eine Zeile pro Dokument, eine… |
| `vollzugs-checkliste` | Vollzugscheckliste für M&A-Transaktionen nach deutschem Recht – was blockiert den Vollzug (Closing), kritischer Pfad, Tage bis Vollzug. Selbstaktualisierend: nimmt neue Einträge aus DD-Findings und Anlage-Erstellung… |
| `wesentliche-vertraege-anlage` | Erstellt das Verzeichnis wesentlicher Verträge (Material Contracts Schedule) aus Due-Diligence-Erkenntnissen auf Grundlage der SPA-Definition und des Anhangformats. Berücksichtigt Change-of-Control-Klauseln… |

## Worum geht es?

Dieses Plugin unterstuetzt Anwaelte und Wirtschaftsjuristen bei laufenden gesellschaftsrechtlichen Mandaten: GmbH- und AG-Governance, Personengesellschaften, M&A-Due-Diligence ohne Discovery, Gesellschafterbeschluesse, Handelsregisteranmeldungen, Closing-Checklisten und Compliance-Fristen. Es deckt sowohl die laufende Gesellschaftsverwaltung als auch transaktionsbezogene Mandate ab.

Das Plugin ist auf eine pruefende und beratende Kanzleipraxis ausgerichtet. Es enthaelt einen Kaltstart-Workflow fuer die Einrichtung des Praxisprofils sowie Mandats-Workspaces fuer Mehrfachmandatsbetrieb.

## Wann brauchen Sie diese Skill?

- Sie beraten eine GmbH bei Beschlussfassung, Geschaeftsfuehrer-Haftung oder Gesellschafterstreit.
- Sie begleiten eine M&A-Transaktion auf der Rechtspruefungsseite (Due Diligence, Q&A, Datenraum, Closing Checklist).
- Sie muessen Handelsregisteranmeldungen vorbereiten (Geschaeftsfuehrerwechsel, Prokura, Sitzverlegung, Kapitalmanahmen).
- Sie verwalten gesellschaftsrechtliche Compliance-Fristen (Jahresabschluss, Transparenzregister, Bilanzpublizitaet).
- Ein Gesellschafterstreit droht oder eine Patt-Situation ist eingetreten und Sie benoetigen eine Konfliktstrategie.

## Fachbegriffe (kurz erklaert)

- **Business Judgment Rule** — Haftungsprivileg fuer Geschaeftsfuehrer und Vorstande bei unternehmerischen Entscheidungen (analog § 93 Abs. 1 S. 2 AktG, § 43 GmbHG).
- **Drag-Along** — Mitnahmerecht: Mehrheitsgesellschafter kann Minderheitsgesellschafter zum Verkauf zwingen.
- **Tag-Along** — Mitveraeuserungsrecht: Minderheitsgesellschafter kann beim Verkauf mitziehen.
- **Closing Checklist** — Checkliste aller bis zum Vollzug einer Transaktion zu erfuellenden Bedingungen und Handlungen.
- **Umlaufbeschluss** — Gesellschafterbeschluss ohne Versammlung; bei GmbH nach § 48 Abs. 2 GmbHG zulaessig mit Zustimmung aller Gesellschafter.
- **Prokura** — Umfassende Handlungsvollmacht nach §§ 48 ff. HGB; bedarf der Handelsregistereintragung.
- **Change of Control** — Klausel in Vertraegen, die bei Wechsel der Gesellschafterstruktur besondere Rechte (z.B. Kuendigung) ausloest.

## Rechtsgrundlagen

- §§ 35-43 GmbHG — Geschaeftsfuehrung und Haftung
- §§ 46-49 GmbHG — Gesellschafterversammlung und Beschluesse
- §§ 93 ff. AktG — Vorstandshaftung, Business Judgment Rule
- §§ 107 ff. AktG — Aufsichtsrat (Protokoll, Beschluesse)
- §§ 241, 246 AktG — Nichtigkeits- und Anfechtungsklage (analog GmbH)
- §§ 12 ff. HGB — Handelsregister und Registeranmeldung
- §§ 48 ff. HGB — Prokura
- §§ 15 HGB — Wirkung der Handelsregistereintragung
- § 613a BGB — Betriebsuebergang bei Post-Merger-Integration
- §§ 18 ff. GwG — Transparenzregister

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Gesellschaftsform, Mandantenrolle (Gesellschafter, GF, Aufsichtsrat, Kaeufer, Investor), Sachgebiet.
2. Phase des Mandats bestimmen: Governance, Transaktion (DD, Closing), Streit oder Compliance.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Insolvenzantragspflicht § 15a InsO, Anfechtungsklagefrist § 246 AktG analog (ein Monat), WEG-Klagefrist.
5. Anschluss-Skill bestimmen: nach Due-Diligence-Extraktion folgt Deal-Team-Briefing und Closing Checklist.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `gesellschaftsrecht-kaltstart-interview` — Ersteinrichtung des Praxisprofils: Taetigkeitsbereiche, Wesentlichkeitsschwellen, Hausstil, Eskalationsmatrix.
- `gesellschaftsrecht-anpassen` — Praxisprofil aktualisieren: Risikoprofil, Module, Schwellenwerte, Workspace-Pfade.
- `gesellschaftsrecht-mandat-arbeitsbereich` — Mandats-Workspaces verwalten fuer Mehrfachmandatsbetrieb.
- `mandat-triage-gesellschaftsrecht` — Eingangs-Abfrage fuer gesellschaftsrechtliche Mandate mit Fristen-Ampel und Routing.

**Gesellschafterbeschluesse und Governance**

- `gesellschafterbeschluss` — Erstellung, Pruefung und Anfechtung von Gesellschafterbeschluessen in GmbH und AG.
- `schriftliche-beschlussfassung` — Umlaufbeschluesse im Hausstil mit Stimmverboten und Mehrheitserfordernissen.
- `aufsichtsrat-protokoll` — Protokolle von Vorstandssitzungen, Aufsichtsratssitzungen und GV im Hausformat.

**Haftung und Konflikt**

- `geschaeftsfuehrer-haftung-43-gmbhg` — Prueft persoenliche Haftung des GF nach § 43 GmbHG mit Business Judgment Rule und D&O-Versicherung.
- `gesellschafterstreit-loesungsstrategie` — Konflikt- und Mediationsstrategie bei Gesellschafterstreit, Patt-Situation und Einziehungsverfahren.

**Due Diligence und M&A**

- `dd-findings-extraktion` — Extraktion von DD-Issues aus Datenraum-Dokumenten nach Hauskategorien und Wesentlichkeitsschwellen.
- `dealteam-zusammenfassung` — Gestaffelte Deal-Briefings fuer GF, Deal-Lead und Arbeitsteam aus DD-Findings.
- `vollzugs-checkliste` — Vollzugscheckliste fuer M&A-Transaktionen: kritischer Pfad, CPs, Tage bis Closing.
- `wesentliche-vertraege-anlage` — Verzeichnis wesentlicher Vertraege (Material Contracts Schedule) aus DD-Erkenntnissen.
- `ki-werkzeug-uebergabe` — KI-Tool-Uebergabe fuer Massenvertragsprüfungen an Luminance oder Kira.
- `tabellenpruefung` — Tabellarisches Vertragsreview als Prompt-Matrix pro Dokument und Datenpunkt.

**Register und Compliance**

- `handelsregisteranmeldung` — Vorbereitung von HRB/HRA/GnR/PartGR-Anmeldungen mit Pflichtanmeldungen und Wirkung nach § 15 HGB.
- `gmbh-gruendung` — GmbH-Gruendung von der Satzung bis zur Handelsregistereintragung mit UG-Variante.
- `gesellschafts-compliance` — Compliance-Tracker fuer Einreichungsfristen, Bilanzpublizitaet und Transparenzregister.

**Post-Merger-Integration**

- `integrations-management` — PMI-Tracker: Phasenplan, Zustimmungsverfolgung, § 613a BGB und BetrVG-Mitbestimmung.

## Worauf besonders achten

- **Anfechtungsfrist beachten.** Die Analogie zu § 246 AktG fuer GmbH-Beschluesse setzt typischerweise eine einmonatige Klagefrist; nach laengerer Zeit droht Verwirkung.
- **Insolvenzantragspflicht parallel pruefen.** Sobald der GF Insolvenzanzeichen erkennt, laeuft die Antragspflicht nach § 15a InsO; sofort an `fortbestehensprognose`-Plugin verweisen.
- **Change-of-Control-Klauseln in DD.** Bei M&A-Due-Diligence muessen alle wesentlichen Vertraege auf Change-of-Control-Klauseln durchleuchtet werden; Closing kann sonst scheitern.
- **Umlaufbeschluss erfordert Einstimmigkeit.** Bei GmbH muss jeder Gesellschafter zustimmen (§ 48 Abs. 2 GmbHG); fehlende Stimmen machen Beschluss unwirksam.
- **Transparenzregister und Gesellschafterliste aktuell halten.** Jede Aenderung der Gesellschafterstruktur loest eine Meldepflicht aus (§ 20 GwG).

## Typische Fehler

- GF-Haftung wird nur nach § 43 GmbHG geprueft ohne § 15b InsO Zahlungsverbot bei Insolvenzreife.
- Protokolle von Gesellschafterversammlungen sind unvollstaendig; Abstimmungsergebnisse fehlen oder Stimmverbote werden nicht beachtet.
- Closing-Checklist wird zu spaet aufgebaut; Regulatory-Fristen wurden verpasst.
- Betriebsuebertragung nach § 613a BGB wird in Post-Merger-Integration nicht fristgemaess kommuniziert.
- DD-Findings werden nicht in die SPA-Garantien und Disclosure Schedules uebersetzt.

## Querverweise

- `mittelstand-corporate-ma` — Fuer vollstaendige M&A-Transaktionsbegleitung von DD bis PMI.
- `gesellschaftsgruender` — Fuer Gruendungsfragen vor der laufenden Gesellschaftsverwaltung.
- `insolvenzforderungsanmeldungspruefung` — Bei Insolvenz der Gesellschaft und Forderungsanmeldeverfahren.
- `fortbestehensprognose` — Wenn Insolvenzreife geprueft werden muss.
- `subsumtions-pruefer` — Fuer Einzelnorm-Analysen im gesellschaftsrechtlichen Kontext.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (GmbHG, AktG, HGB, BGB, InsO, GwG, BetrVG)
