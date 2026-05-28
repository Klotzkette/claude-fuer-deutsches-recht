---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Krisenfrueherkennung Starug-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Krisenfrueherkennung und StaRUG-Management — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Krisenfrueherkennung Starug**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung.

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
| `cross-class-cram-down-und-absolute-priority` | Cross-Class-Cram-Down und Absolute-Priority-Rule im StaRUG-Plan: Gericht soll Plan gegen ablehnende Gläubiger-Gruppen bestätigen. Normen: § 26 StaRUG (Cram-Down-Voraussetzungen), § 30 StaRUG… |
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokollierung der Geschäftsführung für Haftungsschutz: GmbH-Geschäftsführer oder AG-Vorstand will Entscheidungen in der Krise dokumentieren. Normen: § 43 GmbHG (Sorgfaltspflicht und Haftung), § 93 Abs. 2 S. 2… |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Drohende Zahlungsunfähigkeit nach § 18 InsO feststellen: Berater oder GF prüft ob StaRUG-Zugangsberechtigung besteht. Normen: § 18 InsO (drohende ZU), § 17 InsO (aktuelle ZU), § 19 InsO (Überschuldung), § 1 StaRUG… |
| `fortbestehensprognose-zweistufig` | Zweistufige Fortbestehensprognose nach IDW S 11 erstellen: Unternehmen ist möglicherweise ueberschuldet und braucht positive Fortführungsprognose. Normen: § 19 InsO (Überschuldungsbegriff modifiziert), IDW S 11… |
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS… |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Geschäftsführerhaftung bei Krisenversagen prüfe und begrenzen: GF oder Berater will Haftungsrisiken einschaetzen und Enthaftungsstrategien entwickeln. Normen: § 43 GmbHG (Sorgfaltspflicht), § 93 AktG… |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | Insolvenzantragspflicht nach § 15a InsO und Drei-Wochen-Frist: GF prüft ob Insolvenzantrag gestellt werden muss. Normen: § 15a InsO (Antragspflicht), § 15a Abs. 4 InsO (Strafbarkeit), § 18 InsO (drohende ZU als… |
| `integrierte-planung-guv-bilanz-cashflow` | Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB… |
| `kennzahlenset-und-ampelsystem-starug-konform` | StaRUG-konformes KPI-Set und Ampelsystem für Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte für Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F.… |
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW-S-6-Krisenstadien diagnostizieren und Handlungskorridore bestimmen: Berater oder GF will Krisenstadium und passende Massnahmen ermitteln. Normen: IDW S 6 (Sanierungsstandard: Stakeholder-, Strategie-, Produkt-,… |
| `mandantenbrief-warnung-paragraph-102-starug-template` | § 102-StaRUG-Warnbrief für Berater erstellen: Steuerberater oder Anwalt muss Mandanten formal warnen und Pflichterfuellung dokumentieren. Normen: § 102 StaRUG (Warnpflicht Rechtsberater), § 43 GmbHG, BGH IX ZR 285/14… |
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Krisenfrueherkenungspflicht und 24-Monats-Horizont erklären und umsetzen: GF oder Berater fragt was StaRUG konkret verlangt. Normen: § 1 StaRUG (Frueherkennungspflicht GmbH/AG), § 18 InsO (drohende ZU als… |
| `paragraph-102-starug-warnpflicht-bei-rechtsberatern` | § 102 StaRUG Warnpflicht für Rechtsberater rechtlich bewerten: Steuerberater, WP oder Anwalt prüft eigene Haftungsrisiken bei Krisenmandat. Normen: § 102 StaRUG (Hinweis- und Warnpflicht), BGH IX ZR 285/14… |
| `pflichtenkollision-und-shift-of-fiduciary-duties` | Shift of Fiduciary Duties in der Unternehmenskrise analysieren: GF prüft ob Pflichten nun Gläubigern gegenüber bestehen. Normen: EuGH C-594/14 Kornhaas (Gläubigerschutz EU), § 43 GmbHG, § 93 AktG. Prüfraster: Wandel… |
| `restructuring-lounge-impulsvortrag-toolkit` | Toolkit für Impulsvorträge zu Krisenfrüherkennung und StaRUG: Foliensatz-Gliederung, Talking-Points, juristische Kernbotschaften, Q-und-A-Fallnetz, Formathinweise für Veranstaltungen wie Branchenlounge-Formate. |
| `restrukturierungsbeauftragter-und-sachwalter` | Restrukturierungsbeauftragter und Sachwalter nach § 73 StaRUG: GF oder Gläubigervertreter prüft Bestellung und Aufgaben. Normen: § 73 StaRUG (Restrukturierungsbeauftragter), §§ 74-77 StaRUG (Pflichtbeauftragung), § 76… |
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | StaRUG-Restrukturierungsplan nach §§ 7 ff. StaRUG architektieren: Schuldner oder Berater plant außergerichtliche Sanierung unter StaRUG. Normen: §§ 7 ff. StaRUG (Planbestandteile), § 9 StaRUG (Gruppenbildung), § 25… |
| `rollierende-liquiditaetsplanung-24-monate-template` | Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), IDW S 11 (Fortbestehensprognose), IDW S 6… |
| `stabilisierungsanordnung-und-vollstreckungssperre` | Stabilisierungsanordnung und Vollstreckungssperre nach §§ 49-59 StaRUG beantragen: Schuldner braucht Schutz vor Einzelvollstreckung waehrend Restrukturierung. Normen: §§ 49-59 StaRUG (Stabilisierungsanordnung), § 51… |

## Worum geht es?

Das Unternehmensstabilisierungs- und -restrukturierungsgesetz (StaRUG) verpflichtet Geschaeftsfuehrer und Vorstande, ein Fruehwarnsystem mit 24-Monats-Horizont zu unterhalten (§ 1 StaRUG). Daneben trifft Rechtsberater (Steuerberater, Wirtschaftspruefer, Rechtsanwaelte) bei Anzeichen einer Unternehmenskrise eine eigenstaendige Hinweis- und Warnpflicht nach § 102 StaRUG.

Das Plugin deckt den gesamten Krisenmanagement-Zyklus ab: vom Fruehwarnsystem und der Krisenstadien-Diagnose ueber Insolvenzantragspflicht und Fortbestehensprognose bis hin zur Restrukturierungsplan-Architektur, dem Cross-Class-Cram-Down und der Stabilisierungsanordnung. Zielgruppe sind Restrukturierungsberater, Steuerberater, Wirtschaftspruefer und Unternehmensjuristen.

## Wann brauchen Sie diese Skill?

- Ein Mandant zeigt erste Krisenzeichen (sinkende Liquiditaetsreichweite, Covenant-Verletzung, Umsatzeinbruch) und Sie wollen das Krisenstadium nach IDW S 6 einordnen.
- Ein Geschaeftsfuehrer fragt, ob und bis wann er Insolvenz anmelden muss (§ 15a InsO, Drei-Wochen-Frist).
- Als Steuerberater oder Anwalt wollen Sie Ihre Warnpflicht nach § 102 StaRUG dokumentieren, um eigene Haftungsrisiken zu begrenzen.
- Ein Restrukturierungsplan soll nach §§ 7 ff. StaRUG aufgestellt werden und das Gericht soll den Plan gegen ablehnende Glaeubiger bestaetigen.
- Ein Schuldner benoetigt eine Stabilisierungsanordnung nach §§ 49 ff. StaRUG, um Vollstreckungsversuche zu stoppen.

## Fachbegriffe (kurz erklaert)

- **Drohende Zahlungsunfaehigkeit** — Zugangsberechtigung zum StaRUG: Wahrscheinlichkeit, dass das Unternehmen kuenftig nicht mehr zahlen kann (§ 18 InsO), abzugrenzen von der aktuellen ZU nach § 17 InsO.
- **Fortbestehensprognose** — zweistufige Pruefung nach IDW S 11 (Fortfuehrungswille + Fortfuehrungsfaehigkeit), die bei Ueberschuldung (§ 19 InsO) die Insolvenzantragspflicht ausloesen oder verhindern kann.
- **Cram-Down** — gerichtliche Planbestaetigung gegen ablehnende Glaeubiger-Gruppen nach § 26 StaRUG (Cross-Class-Cram-Down).
- **Shift of Fiduciary Duties** — Verschiebung der Treuepflichten vom Eigentuemer-Interesse zum Glaeubiger-Interesse bei drohender Insolvenz.
- **Restrukturierungsbeauftragter** — vom Gericht bestellter Sachwalter nach § 73 StaRUG; Pflicht-Bestellung bei bestimmten Plantypen.
- **DSCR** — Debt Service Coverage Ratio; einer der zentralen Krisenfruehindikator-KPIs.
- **IDW S 6** — Standard des Instituts der Wirtschaftspruefer fuer Sanierungskonzepte.

## Rechtsgrundlagen

- § 1 StaRUG — Krisenfrueherkennung und -management (24-Monats-Pflicht)
- § 18 InsO — drohende Zahlungsunfaehigkeit (Zugangstatbestand StaRUG)
- § 19 InsO — Ueberschuldung
- § 15a InsO — Insolvenzantragspflicht (Drei-Wochen-Frist)
- §§ 7 ff. StaRUG — Restrukturierungsplan
- §§ 49-59 StaRUG — Stabilisierungsanordnung
- § 73 StaRUG — Restrukturierungsbeauftragter
- § 102 StaRUG — Warnpflicht bei Rechtsberatern
- § 43 GmbHG — Sorgfaltspflicht und Haftung des GmbH-Geschaeftsfuehrers
- § 93 AktG — Vorstandshaftung

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Geschaeftsfuehrer/Vorstand, Rechtsberater, Glaeubiger oder Restrukturierungsberater?
2. Phase des Mandats bestimmen: Fruehwarnung (Krisenstadium Eins bis Drei), drohende ZU/StaRUG-Zugangsberechtigung, Restrukturierungsplan oder Insolvenznaehe (§ 15a InsO)?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: § 15a InsO — maximale Antragsfrist drei Wochen bei ZU oder Ueberschuldung; kein Aufschub moeglich.
5. Anschluss-Skill bestimmen: Nach Krisenstadium-Diagnose zu Liquiditaetsplanung und ggf. Warnbrief; bei StaRUG-Zugang zu Planarchitektur.

## Skill-Tour (was gibt es hier?)

- `paragraph-1-starug-pflichten-und-24-monats-horizont` — Erklaert § 1 StaRUG: Adressatenkreis, Planungshorizont und Haftungsfolgen bei Pflichtverletzung.
- `fruehwarnsystem-architektur-zwei-jahres-horizont` — StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont, KPI-Kaskade und Eskalationsstufen aufbauen.
- `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Dashboard-Template mit numerischen Schwellenwerten und gruen/gelb/rot-Ampel.
- `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` — IDW-S-6-Krisenstadien diagnostizieren und Massnahmenkorridore bestimmen.
- `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — StaRUG-Zugangsberechtigung nach § 18 InsO pruefen und dokumentieren.
- `fortbestehensprognose-zweistufig` — Zweistufige Fortbestehensprognose nach IDW S 11 (Fortfuehrungswille + Faehigkeit) erstellen.
- `integrierte-planung-guv-bilanz-cashflow` — Konsistentes Drei-Statement-Modell (GuV/Bilanz/Cashflow) fuer StaRUG-Planung erstellen.
- `rollierende-liquiditaetsplanung-24-monate-template` — 24-Monats-Liquiditaets-Forecast mit woechentlicher Granularitaet und Stresstests.
- `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Triggerlogik § 15a InsO, Maximalfrist drei Wochen, Handlungsoptionen.
- `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — Haftungsrisiken des GF bei Krisenversagen und Enthaftungsstrategien.
- `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Krisenprotokoll-Templates und Sitzungsvorlagen fuer Haftungsschutz.
- `pflichtenkollision-und-shift-of-fiduciary-duties` — Shift of Fiduciary Duties: wann Glaeubigerinteressen Vorrang haben.
- `paragraph-102-starug-warnpflicht-bei-rechtsberatern` — Eigene Haftungsrisiken des Beraters bei Krisenmandat und Warnpflicht-Ausloeser.
- `mandantenbrief-warnung-paragraph-102-starug-template` — Warnbrief-Templates fuer alle drei Eskalationsstufen nach § 102 StaRUG.
- `restrukturierungsplan-architektur-paragraph-7ff-starug` — StaRUG-Restrukturierungsplan aufbauen: Planbestandteile, Gruppenbildung, Mehrheiten.
- `cross-class-cram-down-und-absolute-priority` — Gerichtliche Planbestaetigung gegen ablehnende Glaeubiger-Gruppen nach § 26 StaRUG.
- `stabilisierungsanordnung-und-vollstreckungssperre` — Vollstreckungsschutz nach §§ 49-59 StaRUG beantragen.
- `restrukturierungsbeauftragter-und-sachwalter` — Bestellung, Aufgaben und Honorar des Restrukturierungsbeauftragten nach § 73 StaRUG.
- `restructuring-lounge-impulsvortrag-toolkit` — Toolkit fuer Impulsvortraege zu Krisenfrueherkennung und StaRUG.

## Worauf besonders achten

- **Drei-Wochen-Frist ist absolut**: Bei eingetretener ZU oder Ueberschuldung laeuft die Insolvenzantragspflicht nach § 15a InsO unabhaengig davon, ob Sanierungsverhandlungen laufen. Kein Aufschub durch blosse Hoffnung.
- **StaRUG setzt drohende ZU voraus**: Der Zugang zum StaRUG-Verfahren benoetigt § 18 InsO als Tatbestand; bei bereits eingetretener ZU ist § 17 InsO gegeben und nur InsO anwendbar.
- **Beraterneutralitaet vs. Berater-Warnpflicht**: § 102 StaRUG verpflichtet den Berater zur eigenen Warnung; Schweigen aus Mandantenruecksicht ist eine Pflichtverletzung.
- **Business Judgment Rule in der Krise eingeschraenkt**: Die BJR (§ 93 AktG) schuetzt den Vorstand nur bei informierter Entscheidung auf Basis vollstaendiger Dokumentation.
- **Absolute-Priority-Rule beim Cram-Down**: Das Gericht bestaetigt den Plan nur, wenn kein Glaeubiger schlechter gestellt ist als bei der besten Alternativentscheidung (§ 30 StaRUG).

## Typische Fehler

- Krisenstadien werden uebersprungen: Ohne Diagnose nach IDW S 6 fehlt die Grundlage fuer das Massnahmenkonzept; Gerichte und Glaeubigerausschuesse erwarten die Stadien-Einordnung.
- Fruehwarnsystem nur auf dem Papier: § 1 StaRUG verlangt ein funktionierendes System, nicht nur ein Dokument; fehlende Protokolle belegen die Pflichtverletzung.
- Warnbrief ohne Quittung: Ohne Empfangsbestaetigung laesst sich die Pflichterfuellung nach § 102 StaRUG im Haftungsprozess nicht beweisen.
- Liquiditaetsplanung zu grob: Monatliche Granularitaet genuegt fuer die naechsten drei Monate nicht; woechentliche Granularitaet ist Mindeststandard in der akuten Krise.
- Cram-Down ohne Schlechterstellungsverbot-Nachweis beantragt: Das Gericht wird den Antrag zurueckweisen, wenn der Schlechterstellungstest nicht dokumentiert ist.

## Querverweise

- `arbeitsrecht` — Wenn Massenentlassungen (§ 17 KSchG) oder Betriebsaenderungen (§ 111 BetrVG) im Restrukturierungsplan vorgesehen sind.
- `prozessrecht` — Fuer Vollstreckungsabwehr und anfechtungsrechtliche Fragen im Umfeld der Sanierung.
- `gewerblicher-rechtsschutz` — Wenn IP-Rechte im Restrukturierungsplan einer Verwertung zugefuehrt oder lizenziert werden sollen.

## Quellen und Aktualitaet

- Stand: 05/2026
- StaRUG in geltender Fassung
- InsO §§ 15a, 17, 18, 19 in geltender Fassung
- GmbHG § 43, AktG § 93 in geltender Fassung
- IDW S 6 (Sanierungskonzept), IDW S 11 (Fortbestehensprognose), IDW PS 340 n.F.
