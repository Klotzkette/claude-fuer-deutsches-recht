---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Fortbestehensprognose-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Fortbestehensprognose — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Fortbestehensprognose**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose.

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
| `annahmen-belastbarkeit-plausibilisieren` | Plausibilisiert die in `annahmen-sammeln-fortführung` gesammelten Annahmen. Prüfraster Konsistenz mit Vergangenheit (BWA SuSa Jahresabschluss) Marktentwicklung (Branche makroekonomisch) Konsistenz untereinander (Umsatz… |
| `annahmen-sammeln-fortfuehrung` | Sammelt die Annahmen die der Geschäftsführer der Fortbestehensprognose zu Grunde legt. Umsatzentwicklung Kostenentwicklung Personalkostenentwicklung Investitionen Working-Capital Saisonalitaet Auftragsbestand… |
| `ausloesendes-ereignis-erfassen` | Erfasst den Anlass der Fortbestehensprognose. Typische Auslöser sind Hinweis des Steuerberaters nach § 102 StaRUG Hinweis des Wirtschaftsprüfers Bekanntwerden negativen Eigenkapitals Bilanzaufstellung mit negativem EK… |
| `bilanzieller-status-aufnehmen` | Nimmt die bilanzielle Ausgangslage auf — Aktiva Passiva Eigenkapital nach HGB-Stichtagsbilanz. Prüfraster bilanzielle Überschuldung (Aktiva kleiner als Passiva). Erfasst stille Reserven und stille Lasten Sonderposten… |
| `comfortletter-weich-erzeugen` | Erzeugt einen Comfortletter — eine weiche Erklärung des Patrons oder Mutterunternehmens das Tochterunternehmen zu unterstuetzen. Im Gegensatz zur harten externen Patronatserklärung ist der Comfortletter nicht… |
| `forderungsverzicht-besserungsschein` | Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im… |
| `fortbestehensprognose-kaltstart-interview` | Kaltstart-Interview für das Fortbestehensprognose-Plugin. Stellt fest wer das Plugin nutzt (Geschäftsführer / Vorstand / Gesellschafter mit Eigenverantwortung / Finanzleiter mit Mandat) wer der Anwaltliche und… |
| `fortbestehensprognose-zusammenfuehren` | Führt alle Bausteine zusammen — bilanzieller Status Annahmen Plausibilisierung 12-Monats-Liquiditaet Sensitivitaetsszenarien — und bewertet ob die Fortbestehensprognose nach § 19 Abs. 2 InsO positiv ist. Massstab… |
| `gesellschafterdarlehen-rangruecktritt` | Erzeugt eine Erklärung zum qualifizierten Rangrücktritt für Gesellschafterdarlehen nach § 19 Abs. 2 S. 2 InsO. BGH-konforme Formulierung BGH II ZR 18/19 — der Rangrücktritt muss sich erstrecken auf Insolvenz Gläubiger… |
| `liquiditaet-12-monate` | Erstellt die rollierende Zwoelf-Monats-Liquiditaetsvorschau auf Basis der plausibilisierten Annahmen. Pro Woche oder pro Monat Aufstellung der Einzahlungen und Auszahlungen Anfangsbestand Endbestand Linieverbleib.… |
| `patronatserklaerung-extern-hart-erzeugen` | Erzeugt eine harte externe Patronatserklärung des Gesellschafters (oder eines Dritten) zugunsten der Gesellschaft. Erfasst Patron Begueneten Hoehe Bedingungen Laufzeit Insolvenzfeste Klausel. Zur Berücksichtigung im… |
| `prognose-dokumentation-stichtag` | Abschließende Selbstdokumentation der Fortbestehensprognose zum konkreten Stichtag. Enthaelt Ausgangslage Annahmen Plausibilisierung Liquiditaet Szenarien Sanierungsbausteine mit Belegen Gesamtergebnis. Dient als Beleg… |
| `sanierungsbausteine-vorschlagen` | Wenn die Fortbestehensprognose ohne Massnahmen negativ oder knapp positiv ist schlaegt dieser Skill konkrete Sanierungsbausteine vor. Auswahl Patronatserklärung hart Comfortletter Gesellschafterdarlehen mit… |
| `stundungsanfrage-glaeubiger` | Erzeugt Stundungsanfragen an Gläubiger (Lieferanten Bank Vermieter Steueramt Sozialversicherungstraeger). Erfasst pro Gläubiger Forderungshoehe Fälligkeit Stundungswunsch (neue Fälligkeit Ratenzahlung Tilgungspause)… |
| `wenn-prognose-negativ-naechste-schritte` | Wenn die Fortbestehensprognose negativ ausfaellt — Eskalations- und Pflichtenkatalog für den Geschäftsleiter. Antragspflicht § 15a InsO sechs Wochen bei Überschuldung drei Wochen bei Zahlungsunfähigkeit. Zahlungsverbot… |

## Worum geht es?

Dieses Plugin begleitet Geschaeftsfuehrer und Vorstande bei der Erstellung einer Fortbestehensprognose nach § 19 Abs. 2 InsO. Es dokumentiert Schritt fuer Schritt: ausloesende Ereignisse, bilanziellen Status, Fortfuehrungsannahmen, Plausibilisierung, rollende Zwoelf-Monats-Liquiditaet, Sensitivitaetsszenarien und Sanierungsbausteine (Patronatserklaerung, Comfortletter, Rangruecktritt, Stundung, Forderungsverzicht). Wenn die Prognose negativ ausfaellt, eskaliert das Plugin zum Pflichtenkatalog des Geschaeftsfuehrers nach §§ 15a, 15b InsO.

Das Plugin richtet sich an Eigenverantwortliche: Geschaeftsfuehrer, Vorstande und Finanzleiter — nicht als Ersatz fuer die Beauftragung eines Insolvenzrechtsanwalts.

## Wann brauchen Sie diese Skill?

- Der Steuerberater oder Wirtschaftspruefer weist auf negatives Eigenkapital oder bilanziellen Ueberschuldungsverdacht hin (§ 102 StaRUG).
- Das Unternehmen zeigt Liquiditaetsengpaesse und Sie als Geschaeftsfuehrer muessen dokumentieren, dass Sie aktiv gehandelt haben.
- Gesellschafter oder Banken verlangen eine Fortbestehensprognose als Voraussetzung fuer Unterstuetzungsmassnahmen.
- Sie pruefe Sanierungsbausteine (Gesellschafterdarlehen, Rangruecktritt, Patronatserklaerung) und wollen die insolvenzrechtliche Wirkung verstehen.
- Die Prognose ist knapp positiv oder negativ und Sie benoetigen den Pflichtenkatalog fuer die naechsten Schritte.

## Fachbegriffe (kurz erklaert)

- **Fortbestehensprognose** — Einschaetzung, ob das Unternehmen im Prognosezeitraum (ueblicherweise 12 Monate) ueberwiegend wahrscheinlich zahlungsfaehig bleiben wird (§ 19 Abs. 2 InsO, Massstab IDW S 11).
- **Ueberschuldung** — Passiva uebersteigen Aktiva nach bilanzieller Bewertung; bei positiver Fortbestehensprognose kein Insolvenzgrund nach § 19 Abs. 2 InsO.
- **Rangruecktritt** — Erklaerung des Gesellschafters, seine Darlehensforderung hinter alle anderen Glaeubiger zurueckzustellen; fuehrt zur Nichtpassivierung im insolvenzrechtlichen Status.
- **Patronatserklaerung (hart)** — Rechtsverbindliche Erklaerung des Gesellschafters oder Mutterunternehmens, die Tochtergesellschaft so auszustatten, dass sie zahlungsfaehig bleibt; beruecksichtigungsfaehig im Status.
- **Comfortletter** — Weiche Erklaerung des Patrons; nicht rechtsverbindlich; nicht ausreichend fuer insolvenzrechtlichen Status.
- **IDW S 11** — Institut der Wirtschaftspruefer, Standard 11: Massstab und Methodik fuer die Fortbestehensprognose.
- **StaRUG** — Gesetz ueber den Stabilisierungs- und Restrukturierungsrahmen; Option vor formeller Insolvenz.

## Rechtsgrundlagen

- § 17 InsO — Zahlungsunfaehigkeit (Insolvenzgrund)
- § 18 InsO — Drohende Zahlungsunfaehigkeit (nur Eigenantrag)
- § 19 InsO — Ueberschuldung und Fortbestehensprognose
- § 15a InsO — Insolvenzantragspflicht (sechs Wochen bei Ueberschuldung, drei Wochen bei Zahlungsunfaehigkeit)
- § 15b InsO — Zahlungsverbot und Haftung bei Insolvenzverschleppung
- § 43 GmbHG — Haftung des Geschaeftsfuehrers
- §§ 1-93 StaRUG — Restrukturierungsrahmen
- § 19 Abs. 2 S. 2 InsO — Qualifizierter Rangruecktritt (BGH II ZR 18/19)
- § 3a EStG — Steuerliche Behandlung Sanierungsgewinn

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Wer nutzt das Plugin (GF, Vorstand, Finanzleiter), Rechtsform, Geschaeftsjahr, Buchhaltungssystem.
2. Phase des Mandats bestimmen: Ausloeser erfassen, bilanzieller Status, Annahmen, Plausibilisierung, Liquiditaetsplanung oder Sanierungsbaustein-Erstellung.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Dreiwochenfrist Zahlungsunfaehigkeit, Sechswochenfrist Ueberschuldung nach § 15a InsO.
5. Anschluss-Skill bestimmen: Wenn Prognose negativ, sofort `wenn-prognose-negativ-naechste-schritte` und Insolvenzanwalt einbinden.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `fortbestehensprognose-kaltstart-interview` — Ersteinrichtung: Rolle, Rechtsform, Ansprechpartner, Buchhaltungssystem und Profil schreiben.

**Aufnahme und Analyse**

- `ausloesendes-ereignis-erfassen` — Dokumentiert Anlass, Datum, Hinweisgeber und Mitteilungsform der Fortbestehenspruefung.
- `bilanzieller-status-aufnehmen` — Nimmt Aktiva, Passiva, Eigenkapital und ausserbilanzielle Verpflichtungen auf; prueft bilanziellen Ueberschuldungsverdacht.
- `annahmen-sammeln-fortfuehrung` — Sammelt Fortfuehrungsannahmen zu Umsatz, Kosten, Personal, Investitionen und Working Capital.
- `annahmen-belastbarkeit-plausibilisieren` — Plausibilisiert Annahmen gegen Vergangenheit und Marktentwicklung; erzeugt Plausibilitaetsprotokoll.
- `liquiditaet-12-monate` — Rollende Zwoelf-Monats-Liquiditaetsvorschau mit Einzahlungen, Auszahlungen und Linienverbleib.

**Sanierungsbausteine (Dokumente erzeugen)**

- `sanierungsbausteine-vorschlagen` — Empfehlungsmatrix fuer Sanierungsmassnahmen nach Effekt und Umsetzungszeit.
- `patronatserklaerung-extern-hart-erzeugen` — Harte externe Patronatserklaerung als DOCX zur Unterzeichnung erzeugen.
- `comfortletter-weich-erzeugen` — Comfortletter (weich, nicht rechtsverbindlich) erstellen mit Warnhinweis zur insolvenzrechtlichen Wirkung.
- `gesellschafterdarlehen-rangruecktritt` — BGH-konforme Rangruecktrittserklaerung nach § 19 Abs. 2 S. 2 InsO erzeugen.
- `forderungsverzicht-besserungsschein` — Forderungsverzicht mit Besserungsschein erstellen mit steuerlichen Hinweisen.
- `stundungsanfrage-glaeubiger` — Stundungsanfragen an Glaeubiger (Lieferanten, Bank, Finanzamt, Sozialversicherung) individuell erstellen.

**Prognose und Dokumentation**

- `fortbestehensprognose-zusammenfuehren` — Alle Bausteine zusammenfuehren und Gesamtbewertung nach IDW S 11 erstellen.
- `prognose-dokumentation-stichtag` — Abschliessende Selbstdokumentation zum Stichtag als Haftungsbeleg.

**Eskalation**

- `wenn-prognose-negativ-naechste-schritte` — Pflichtenkatalog bei negativer Prognose: § 15a InsO, § 15b InsO, StaRUG-Option, Insolvenzanwalt.

## Worauf besonders achten

- **Selbstdokumentation ersetzt keinen Insolvenzrechtsanwalt.** Das Plugin hilft GF bei Eigenverantwortung; bei negativer oder knapp positiver Prognose ist Fachanwaltskonsultation zwingend.
- **Rangruecktritt muss BGH-konform formuliert sein.** Fehlformulierungen sind insolvenzrechtlich wirkungslos; Skill `gesellschafterdarlehen-rangruecktritt` liefert BGH-konforme Formulierung.
- **Nur harte Patronatserklaerung ist beruecksichtigungsfaehig.** Comfortletter reicht nicht aus; das Plugin weist explizit darauf hin.
- **Dreiwochenfrist laeuft ohne Hemmung.** Sobald Zahlungsunfaehigkeit eingetreten ist, laeuft § 15a InsO-Frist ohne Moeglichkeit der Verlaengerung.
- **Steuerliche Folgen von Sanierungsgewinn beachten.** Forderungsverzicht loest beim Schuldner Ertrag aus; Skill `forderungsverzicht-besserungsschein` enthaelt entsprechenden Hinweis.

## Typische Fehler

- Prognose wird auf der Basis zu optimistischer Annahmen erstellt ohne Plausibilisierung gegen Vergangenheit und Markt.
- Bilanzieller Status wird mit insolvenzrechtlichem Status gleichgesetzt; beide koennen abweichen (stille Reserven, Rangruecktritt).
- Comfortletter wird als ausreichend fuer positiven Status behandelt; fuehrt zu fehlerhafter Prognose.
- Dokumentation erfolgt nach dem Ereignis (nachtraeglich), nicht zum Stichtag; Haftungsschutz entfaellt.
- Steuerwirkung des Sanierungsgewinns (§ 3a EStG) wird nicht beachtet; unerwartete Steuerlast.

## Querverweise

- `insolvenzforderungsanmeldungspruefung` — Wenn das Verfahren eroeffnet wird und Forderungen geprueft werden muessen.
- `mittelstand-corporate-ma` — Wenn die Krise im Kontext einer M&A-Transaktion entsteht (Distressed M&A, StaRUG-Begleitung).
- `gesellschaftsrecht` — Fuer Haftungsfragen des GF und Gesellschafterbeschluesse im Krisenkontext.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (InsO, StaRUG, GmbHG, EStG, BGB)
- IDW S 11 (Fortbestehensprognose) und IDW S 6 (Sanierungskonzept) in geltender Fassung
