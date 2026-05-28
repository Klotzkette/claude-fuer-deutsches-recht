---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Verkehr Infrastrukturrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext startet der Skill von selbst: klassifiziert die Aktenart, routet in den passenden Spezial-Skill oder stellt eine gezielte Rueckfrage statt einer generischen Antwort."
---

# Verkehrs- und Infrastrukturrecht — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Verkehr Infrastrukturrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende.

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
| `verkehr-infrastrukturrecht-foerderung-vergabe` | Foerderrecht und Vergabe für Verkehrsinfrastruktur-Projekte: Kommune oder Vorhabentraeger beantragt GVFG-Mittel oder schreibt öffentlichen Auftrag aus. Normen: GVFG (Bundesanteil und Laenderanteil), BHO §§ 23 und 44… |
| `verkehr-infrastrukturrecht-kommandocenter` | Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht: Neues Mandat im Bereich Verkehrsinfrastruktur, Routing auf passenden Subskill. Normen: FStrG, AEG, PBefG, StVO, BauGB, FStrG, GWB (je nach Sachgebiet).… |
| `verkehr-infrastrukturrecht-ladeinfrastruktur` | Ladeinfrastruktur für Elektromobilitaet rechtlich begleiten: Betreiber plant Ladepunkte oder Netzanschluss wird verweigert. Normen: AFIR-VO (EU) 2023/1804 (Mindestanforderungen Ladeinfrastruktur), Ladesaeulenverordnung… |
| `verkehr-infrastrukturrecht-parkraumbewirtschaftung` | Parkraumbewirtschaftung kommunalrechtlich gestalten und anfechten: Kommune einführt Bewohnerparkausweis oder Abschleppung wird angefochten. Normen: § 45 StVO (Bewohnerparkausweis, Verkehrszeichen), StVG § 12… |
| `verkehr-infrastrukturrecht-planfeststellung` | Planfeststellung für Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten: Vorhabentraeger benoetigt Planfeststellungsbeschluss oder Anlieger klagt dagegen. Normen: § 17 FStrG (Bundesstrasse),… |
| `verkehr-infrastrukturrecht-schulwegsicherheit` | Schulwegsicherheit rechtlich verbessern oder Amtshaftung geltend machen: Schule, Eltern oder Kommune will Schulwegplan umsetzen oder gegen Unfall auf Schulweg vorgehen. Normen: § 45 StVO (Schulweghelfer, Schulstrassen,… |
| `verkehr-infrastrukturrecht-sondernutzung` | Sondernutzung öffentlicher Strassenflaechen beantragen und anfechten: Unternehmen braucht Erlaubnis für Aussengastronomie, Ladesaeule oder Baustelle. Normen: § 8 FStrG (Bundesstrassenrecht), § 16 StrWG NW… |
| `verkehr-infrastrukturrecht-strassenbahn` | Strassenbahn- und OEPNV-Infrastrukturrecht: Betreiber beantragt Konzession oder Planfeststellung, oder Gemeinde will Linie neu planen. Normen: § 9 PBefG (Konzession), § 28 PBefG (Planfeststellung Strassenbahn), § 39… |
| `verkehr-infrastrukturrecht-verfahren` | Anhoerung, Widerspruch, Klage und Eilverfahren im Verkehrsinfrastrukturrecht vorbereiten: Mandant hat Bescheid erhalten oder will in laufendes Verfahren eingreifen. Normen: § 45 StVO (Verkehrsanordnungen), § 46 StVO… |
| `verkehr-infrastrukturrecht-verkehrsplanung` | Verkehrsplanung rechtlich begleiten: Kommune oder Verband plant Strassen- oder Radverkehrs-Massnahme und muss Beteiligung und Beschluss vorbereiten. Normen: § 45 StVO (Verkehrsanordnungen), FStrG, StrWG (Landesrecht),… |
| `verkehr-infrastrukturrecht-verkehrswende` | Verkehrswende-Massnahmen rechtssicher gestalten: Kommune plant Fussgaengerzone, Tempo-30-Zone oder Radverkehrs-Foerderung. Normen: § 45 Abs. 1 StVO (Fussgaengerzone, Tempo-30), ERA 2010 (Empfehlungen Radverkehr), VwGO… |
| `verkehr-infrastrukturrecht-wirtschaftsverkehr` | Wirtschaftsverkehr und Lieferverkehr in der Stadt rechtlich gestalten: Logistikunternehmen oder Kommune plant Lieferzonen, Beschilderung oder Ausnahmegenehmigungen. Normen: § 12 StVO (Haltverbot), § 45 StVO… |

## Worum geht es?

Das Plugin begleitet rechtliche Fragestellungen rund um Verkehrsplanung und Infrastrukturprojekte auf kommunaler und ueberregionaler Ebene. Es deckt das gesamte Spektrum vom Planfeststellungsverfahren fuer Strassenbau und Schienenstrecken ueber Ladeinfrastruktur fuer Elektromobilitaet bis hin zu Parkraumbewirtschaftung, Sondernutzung oeffentlicher Strassenflaechen und Schulwegsicherheit ab.

Zielgruppe sind Verwaltungsjuristen, Kommunalrechtler, Anwaelte von Verkehrstragern und OEPNV-Betreibern sowie Unternehmen, die Foerdergelder oder Vergabe-Auftraege im Infrastrukturbereich benoetigen. Das Plugin unterstuetzt sowohl die angreifende als auch die verteidigenden Seite bei Planfeststellung und Verwaltungsstreitverfahren.

## Wann brauchen Sie diese Skill?

- Vorhabentraeger oder Behoerde leitet ein Planfeststellungsverfahren fuer Strassenneubau, Schieneninfrastruktur oder OEPNV ein und braucht verfahrensrechtliche Begleitung.
- Betreiber plant Ladepunkte fuer Elektrofahrzeuge und muss Netzanschluss, Foerderungsantrag und Genehmigungsrecht klaeren.
- Kommune fuehrt Bewohnerparkausweis oder Tempo-30-Zone ein und muss Rechtmaessigkeit und Anfechtungsrisiken beachten.
- Unternehmen beantragt Sondernutzungserlaubnis fuer Aussengastronomie, Lieferzone oder Baustelle im oeffentlichen Strassenraum.
- OEPNV-Betreiber oder Gemeinde will Strassenbahnlinie errichten oder Konzession verteidigen.

## Fachbegriffe (kurz erklaert)

- **Planfeststellung** — Foermliches Verwaltungsverfahren nach §§ 72 ff. VwVfG, das Bau und Betrieb von Infrastrukturanlagen konzentriert genehmigt und private Einwendungen ausschliessen kann.
- **GVFG** — Gemeindeverkehrsfinanzierungsgesetz; Bundesfoerderung fuer kommunale Strassenbahnprojekte und OEPNV-Infrastruktur.
- **Sondernutzung** — Nutzung oeffentlicher Strassen, die ueber den Gemeingebrauch hinausgeht (z.B. Werbeanlagen, Aussengastronomie, Baustellenflaeche) und einer besonderen Erlaubnis bedarf.
- **Planungshoheit** — Kommunale Selbstverwaltungsrecht bei der Bauleit- und Verkehrsplanung (Art. 28 Abs. 2 GG).
- **Konzession (PBefG)** — Genehmigung zum Betrieb von Strassenbahnlinien nach dem Personenbefoerderungsgesetz.
- **Verkehrswende** — Stadtplanerische und rechtliche Massnahmen zur Foerderung umweltfreundlicher Mobilitaet (Fussgaengerzonen, Radwege, Tempo-30-Zonen).
- **Schulwegsicherung** — Amtspflichten der Gemeinde und des Strassenverkehrsrechts zum Schutz von Schulkindern im Strassenverkehr; relevant fuer Amtshaftung.

## Rechtsgrundlagen

- §§ 72 ff. VwVfG — Planfeststellungsverfahren
- FStrG, StrWG der Laender — Bundesfernstrassenrecht und Landesstrassenrecht
- PBefG — Personenbefoerderungsgesetz (Strassenbahn, Linienverkehr)
- BNatSchG — Naturschutz bei Infrastrukturvorhaben
- GVFG — Gemeindeverkehrsfinanzierungsgesetz
- § 45 StVO — Verkehrsbeschraenkungen (Tempo-30, Spielstrasse)
- VwGO — Verwaltungsgerichtliche Verfahren, Eilrechtsschutz

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Vorhabentraeger, Behoerde, Anlieger oder Verband?
2. Phase des Mandats bestimmen: Planungsphase, Genehmigungsverfahren, Foerderantrag oder Streitverfahren?
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Widerspruchs- und Klagefrist gegen Planfeststellungsbeschluss (§ 74 VwVfG, §§ 70 74 VwGO).
5. Anschluss-Skill bestimmen: Nach Genehmigungsverfahren ggf. Foerderantrag oder Vergabe pruefen.

## Skill-Tour (was gibt es hier?)

- `verkehr-infrastrukturrecht-kommandocenter` — Zentrales Steuerungsmodul fuer neue Verkehrsinfrastruktur-Mandate mit Routing auf passende Skills.
- `verkehr-infrastrukturrecht-planfeststellung` — Planfeststellungsverfahren fuer Strassenbau, Schienenstrecken und OEPNV-Infrastruktur begleiten oder anfechten.
- `verkehr-infrastrukturrecht-strassenbahn` — Strassenbahn- und OEPNV-Infrastrukturrecht: Konzession, Planfeststellung, Linienplanung nach PBefG.
- `verkehr-infrastrukturrecht-ladeinfrastruktur` — Ladepunkte fuer Elektromobilitaet: Netzanschluss, Genehmigung und Foerderrecht.
- `verkehr-infrastrukturrecht-parkraumbewirtschaftung` — Bewohnerparkausweis, Abschleppanordnungen und kommunale Parkraummassnahmen rechtssicher gestalten und anfechten.
- `verkehr-infrastrukturrecht-foerderung-vergabe` — GVFG-Foerderantrag und Vergabeverfahren fuer Infrastrukturprojekte begleiten.
- `verkehr-infrastrukturrecht-sondernutzung` — Sondernutzungserlaubnis fuer Aussengastronomie, Werbeanlagen und Baustellenflaechen beantragen und anfechten.
- `verkehr-infrastrukturrecht-schulwegsicherheit` — Schulwegsicherung rechtlich verbessern; Amtshaftungsansprueche pruefen und geltend machen.
- `verkehr-infrastrukturrecht-verkehrsplanung` — Strassenverkehrs- und Radverkehrsplanung rechtlich begleiten; Beteiligungspflichten und Abwaegungsfehler.
- `verkehr-infrastrukturrecht-verkehrswende` — Fussgaengerzonen, Tempo-30-Zonen und Radverkehrsfoerderung rechtssicher gestalten.
- `verkehr-infrastrukturrecht-verfahren` — Anhoerung, Widerspruch, Klage und Eilverfahren im Verkehrsinfrastrukturrecht vorbereiten.
- `verkehr-infrastrukturrecht-wirtschaftsverkehr` — Lieferzonen, Wirtschaftsverkehrskonzepte und Logistikrecht im staedtischen Raum.

## Worauf besonders achten

- Planfeststellungsbeschluesse werden bestandskraeftig, wenn keine rechtzeitige Klage erhoben wird; Klagefrist beachten (§ 74 Abs. 1 VwVfG i.V.m. VwGO).
- Einwendungsausschluss (§ 73 Abs. 4 VwVfG): Wer im Anhoerungsverfahren keine Einwendungen erhebt, verliert Klagebefugnis fuer diese Punkte.
- GVFG-Foerderantraege erfordern fruehzeitige Abstimmung mit Behoerden; spaetere Aenderungen am Vorhaben koennen Foerderausschluss ausloesen.
- Vergaberechtliche Anforderungen gelten ab definierten Schwellenwerten (EU-Schwellenwerte nach VgV); Unterschwellenverfahren unterliegen den Landesvergabeordnungen.
- Verkehrswende-Massnahmen (Sperrungen, Geschwindigkeitsbeschraenkungen) muessen auf § 45 StVO gestuetzt sein; fehlerhafte Begruendung macht Anordnung angreifbar.

## Typische Fehler

- Einwendungsfrist im Planfeststellungsverfahren versaeumt: Nach Ablauf ist Einwendungsausschluss bindend.
- Foerderantrag zu spaet gestellt: GVFG-Mittel werden jedes Haushaltsjahr kontingentiert; verspaetest gestellte Antraege gehen leer aus.
- Konzessionspflicht uebersehen: Linienbusverkehr und Strassenbahn beduerften zwingend PBefG-Genehmigung; Betrieb ohne Konzession ist Ordnungswidrigkeit.
- Sondernutzungsgebueher nicht einkalkuliert: Kommunale Sondernutzungssatzungen erheben Gebuehren; fehlende Berechnungsgrundlage fuehrt zu Nachforderungen.
- Amtshaftungsansprueche bei Schulwegsicherung versaeumen: Dreijaehrige Verjaeehrungsfrist nach § 195 BGB ab Kenntnis des Schadens.

## Querverweise

- Plugin `umweltrecht` — Naturschutz, FFH-Vertraeglichkeit und Artenschutz bei Infrastrukturvorhaben.
- Plugin `aussenwirtschaft-zoll-sanktionen` — Bei EU-kofinanzierter Infrastruktur Beihilferecht und Subventionskontrolle beachten.
- Plugin `grosskanzlei-corporate-ma` — Bei Privatisierung oder Konzessionsmodellen fuer Infrastruktur M&A-Aspekte pruefen.

## Quellen und Aktualitaet

- Stand: 05/2026
- VwVfG, FStrG, PBefG, StVO, GVFG in aktuell geltender Fassung
- EU-Schwellenwerte nach VgV/SektVO gemaess aktueller EU-Kommissions-Verordnung
