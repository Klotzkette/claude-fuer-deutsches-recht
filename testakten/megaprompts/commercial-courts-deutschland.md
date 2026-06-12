# Megaprompt: commercial-courts-deutschland

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 57 Skills des Plugins `commercial-courts-deutschland`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting für Commercial-Courts-Verfahren in Deutschland; erkennt Forum, Sprache, Streitwe…
2. **commercial-chamber-vs-commercial-court** — Vergleicht Commercial Chamber beim Landgericht und Commercial Court beim Oberlandesgericht: Instanz, Zuständigkeit, Stre…
3. **zustandigkeit-119b-gvg-check** — Prüft, ob Commercial Court oder Commercial Chamber eröffnet ist: Wirtschaftsstreitigkeit, Streitwert, Parteivereinbarung…
4. **englische-verfahrenssprache-late-submissions** — Prüft und gestaltet die englische Verfahrenssprache: Parteivereinbarung, Schriftsätze, Anlagen, mündliche Verhandlung, P…
5. **klageschrift-english-limitation-tolling** — Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes o…
6. **contract-interpretation-de-en** — Erklärt und prüft englische Vertragsbegriffe unter deutschem Recht: reasonable efforts, best endeavours, indemnity, warr…
7. **document-production-earn-out** — Prüft Urkundenvorlage und Dokumentenherausgabe nach deutschem Prozessrecht im Commercial-Court-Kontext: § 142 ZPO, Subst…
8. **finance-banking-dispute** — Bearbeitet Finance-, Banking- und Capital-Markets-Streitigkeiten mit englischen Dokumenten: facility agreement, covenant…
9. **forumwahl-court-glossary** — Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist…
10. **post-ma-pre-litigation** — Bearbeitet Post-M&A Warranty Claims vor Commercial Courts: notice, knowledge qualifiers, baskets, caps, leakage, earn-ou…
11. **interim-relief-issues-list** — Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sic…
12. **witness-preparation-zustandigkeit-119b** — Bereitet Zeugen in englischsprachigen deutschen Verfahren vor: Wahrheitspflicht, keine Coaching-Grenzüberschreitung, Spr…
13. **english-legal-writing-for-german-courts** — Verbessert englische Schriftsätze für deutsche Gerichte: klar, zpo-tauglich, ohne US-Discovery-Duktus, mit sauberem Tats…
14. **hearing-script-english-advocacy** — Erstellt englische Hearing Scripts für deutsche Anwälte: opening, issue roadmap, witness questions, judicial questions, …
15. **bgh-english-bilingual-client** — Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Ten…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting für Commercial-Courts-Verfahren in Deutschland; erkennt Forum, Sprache, Streitwert, Parteivereinbarung, Case Management, Geheimnisschutz, Beweis, Transcript, Rechtsmittel und englischen Outputbedarf._

# Commercial Courts Deutschland — Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Commercial Courts Deutschland** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startprinzip

Beginne mit Orientierung, nicht mit Lehrbuch. Prüfe zuerst, ob der Fall überhaupt in einen deutschen Commercial Court oder eine Commercial Chamber gehört, ob Englisch wirksam gewählt werden kann und welche Prozesshandlung als nächstes ansteht.

## 90-Sekunden-Triage

| Punkt | Frage |
| --- | --- |
| Forum | Commercial Court am OLG, Commercial Chamber am LG, Schiedsgericht, normales Gericht oder Ausland? |
| Klausel | Gerichtsstand, Sprache, Eskalation, Schiedsvereinbarung, governing law, service agent? |
| Streit | M&A, Finance, Lieferkette, Joint Venture, Organhaftung, Tech, Bau/Anlage, Post-Closing? |
| Streitwert | Reicht die Schwelle nach Bundes-/Landesrecht und passt die sachliche Zuständigkeit? |
| Sprache | Englisch vollständig, teilweise, nur Schriftsätze, nur Hearing, BGH-Fortsetzung? |
| Nächster Akt | Claim, defence, CMC, evidence, confidentiality, transcript, settlement, appeal? |
| Output | Deutsch, Englisch, bilingual; Memo, pleading, order proposal, hearing script, board note? |

## Routing

| Lage | Primärskill | Ergänzung |
| --- | --- | --- |
| Unsicherheit Forum | `zustandigkeit-119b-gvg-check` | `forumwahl-commercial-court-vs-schiedsgericht` |
| Klausel für neuen Vertrag | `jurisdiction-clause-drafting-de-en` | `arbitration-clause-conflict-check` |
| Klage vorbereiten | `klageschrift-english-statement-of-claim` | `claim-intake-fakten-und-exhibits` |
| Verteidigung | `defence-answer-and-jurisdiction-objections` | `ruegelose-einlassung-und-sprache` |
| CMC/Termin | `case-management-conference` | `procedural-calendar-timetable-order` |
| Beweis/Anlagen | `evidence-map-zpo-vs-common-law` | `exhibits-translation-608-zpo` |
| Geheimnisse | `confidentiality-trade-secrets-273a-zpo` | `protective-measures-confidential-exhibits` |
| Wortprotokoll | `verbatim-transcript-613-zpo` | `hearing-script-english-advocacy` |
| Rechtsmittel | `appeal-and-revision-614-zpo` | `bgh-english-proceedings-184b-gvg` |
| Abschlusskontrolle | `redteam-commercial-court-qualitygate` | `glossary-commercial-court-de-en` |

## Antwortformat

**Short Procedural View**
- Forum: [...]
- Language: [...]
- Next procedural act: [...]
- Hard risk: [...]

**Recommended Workflow**
1. [...]
2. [...]
3. [...]

**Suggested Skills**
| Skill | Why now | Deliverable |
| --- | --- | --- |
| `...` | [...] | [...] |

---

## Skill: `commercial-chamber-vs-commercial-court`

_Vergleicht Commercial Chamber beim Landgericht und Commercial Court beim Oberlandesgericht: Instanz, Zuständigkeit, Streitwert, Verfahrenssprache, Tempo, Rechtsmittel und Mandantenstrategie im Commercial Courts Deutschland._

# Commercial Chamber oder Commercial Court

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Commercial Chamber oder Commercial Court
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Vergleich Commercial Chamber (LG) versus Commercial Court (OLG)

| Punkt | Commercial Chamber beim Landgericht | Commercial Court beim Oberlandesgericht |
| --- | --- | --- |
| Rechtsgrundlage | §§ 95, 184a GVG, jeweilige Landesverordnung | § 119b GVG (eingeführt durch Justizstandort-Stärkungsgesetz), Landesverordnung |
| Instanz | erste Instanz Landgericht | erste Instanz Oberlandesgericht |
| Streitwertschwelle | typischerweise wie LG §§ 23, 71 GVG | regelmäßig ab 500.000 EUR (Landesvorgabe) |
| Berufung | Berufung zum OLG (§ 511 ZPO) | Revision zum BGH § 184b GVG (kein OLG-Zwischenschritt) |
| Sprache | Englisch zulässig (§ 184a GVG) | Englisch zulässig (§ 184a GVG); BGH-Revision auf Englisch erstmals möglich |
| Wortprotokoll | auf Antrag (§ 613 ZPO Justizstandort-Stärkungsgesetz) | dito |
| Geheimhaltung | § 273a ZPO Vertraulichkeitsanordnung | § 273a ZPO |
| Zielmandat | Mid-Cap-Streitwerte, klassische B2B-Wirtschaftssachen | Big-Tech-, M&A-, Mega-Mandate; "deutsche Antwort auf NCC, Paris, Singapore" |

### Strategie-Trade-off

- **Commercial Court (OLG, erstinstanzlich):** spart Instanz, aber kein zweiter Tatsachenrechtszug. Wer auf Tatsachenfragen baut (z.B. komplexe Verkehrswerte), behält sich mit Commercial Chamber den Berufungszug bei.
- **Commercial Chamber (LG):** gewohnte Berufung zum OLG; aber zwei Instanzen kosten Zeit (typisch 18-30 Monate bis OLG-Urteil) und Geld.
- **Schiedsgericht:** Vertraulichkeit höher, aber Vollstreckung im EU-Inland nicht einfacher als deutsches Urteil; Aufhebungsverfahren §§ 1059 ff. ZPO selten erfolgreich.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `zustandigkeit-119b-gvg-check`

_Prüft, ob Commercial Court oder Commercial Chamber eröffnet ist: Wirtschaftsstreitigkeit, Streitwert, Parteivereinbarung, Landesrecht, OLG/LG, internationale Zuständigkeit und Rügefragen im Commercial Courts Deutschland._

# Zuständigkeit und Eingangstor

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Zuständigkeit und Eingangstor
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

Besondere Anker: § 119b GVG, Landesrechtsverordnung, Parteivereinbarung, Streitwert ab 500.000 EUR und sachgebietliche Beschränkungen. Prüfe außerdem, ob eine Commercial Chamber beim LG oder ein Commercial Court beim OLG/Obersten Landesgericht gemeint ist.

### Zuständigkeits-Check Commercial Court / Commercial Chamber

1. **Streitwertschwelle:** Commercial Court (§ 119b GVG) regelmäßig ab 500.000 EUR Streitwert; Landesverordnungen können davon abweichen. Commercial Chamber (§§ 95, 184a GVG i.V.m. Justizstandort-Stärkungsgesetz) hat keine harte Streitwertschwelle, aber sachlich-örtliche Zuständigkeit nach §§ 23, 71 GVG.
2. **Sachgebietsfilter:** B2B-Wirtschaftsstreit, kein Arbeitsrecht, kein Verbrauchersachverhalt, kein Familien-/Erbrecht. Typisch: SPA-/APA-Streit, Post-M&A-Garantieansprüche, D&O-Haftung, Lieferketten, Finanzierung.
3. **Parteivereinbarung:** § 38 ZPO Gerichtsstandsvereinbarung zwischen Kaufleuten zulässig; ausdrückliche Wahl von "Commercial Court at OLG X" empfohlen. Bei Verbraucherbeteiligung greift § 38 Abs. 1 ZPO nicht.
4. **Landesrecht prüfen:** Bisher tätige Commercial Courts/Commercial Chambers etwa in Hamburg, Stuttgart (BaWü), München (Bayern), Frankfurt (Hessen), Düsseldorf, Köln (NRW), Mannheim (BaWü). Aktuelle Liste live verifizieren — keine erfundenen Standorte.
5. **Schwellenwerte Justizstandort-Stärkungsgesetz im Blick behalten:** Berufungssumme § 511 ZPO 1.000 EUR; Amtsgerichtszuständigkeit § 23 GVG ab 2026 bis 10.000 EUR; vereinfachtes Verfahren § 495a ZPO bis 1.000 EUR. Diese Schwellen sind für die Frage Commercial Court eigentlich irrelevant, aber für die Verfahrensstrategie und Rechtsmittel wichtig.

### Rügelose Einlassung und Forum-Wechsel

Hat sich der Beklagte rügelos auf eine andere Kammer eingelassen (§ 39 ZPO), wird die Rüge der Commercial-Court-Zuständigkeit präkludiert. Daher: Zuständigkeitsrüge in der Klageerwiderung an erster Stelle.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `englische-verfahrenssprache-late-submissions`

_Prüft und gestaltet die englische Verfahrenssprache: Parteivereinbarung, Schriftsätze, Anlagen, mündliche Verhandlung, Protokoll, Urteil, Übersetzungen und BGH-Fortsetzung im Commercial Courts Deutschland._

# Verfahrenssprache Englisch

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Verfahrenssprache Englisch
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

Besondere Anker: § 184a GVG, §§ 606 ff. ZPO und die jeweilige Landesverordnung. Englisch muss prozessual abgesichert sein: ausdrückliche Vereinbarung, stillschweigende Vereinbarung oder rügelose Einlassung; Dritte und Übersetzungen gesondert prüfen.

### Voraussetzungen für englische Verfahrensführung

| Schritt | Norm | Was muss geschehen |
| --- | --- | --- |
| Parteivereinbarung Englisch | § 184a GVG | ausdrücklich oder konkludent; ein Antrag genügt nicht, beide Parteien müssen zustimmen |
| Antrag bei Gericht | § 184a Abs. 1 GVG | förmlicher Antrag mit Begründung; Gericht entscheidet durch Beschluss |
| Eröffnetes Verfahren | je Bundesland | nur an dafür durch Landesverordnung eingerichteten Spruchkörpern (Commercial Chamber / Commercial Court) |
| Schriftsätze und Anlagen | §§ 184, 184a GVG | können in Englisch eingereicht werden; Anlagen müssen nicht zwingend übersetzt werden, wenn beide Parteien sie verstehen |
| Mündliche Verhandlung | § 184a GVG | in Englisch zulässig, Protokoll grundsätzlich auch in Englisch (§ 184a Abs. 1 Satz 4 GVG) |
| Urteil und Tenor | § 184a Abs. 1 Satz 5 GVG | in Englisch möglich; für Vollstreckung Übersetzung nötig |
| Berufung beim OLG | § 184a GVG | nur, wenn auch dort englische Verhandlung eingerichtet |
| Revision beim BGH | § 184b GVG | erstmals seit Justizstandort-Stärkungsgesetz möglich, Voraussetzungen separat prüfen |

### Trade-off Englisch versus Deutsch

| Pro Englisch | Pro Deutsch |
| --- | --- |
| Mandant aus USA/UK versteht Verfahren | Beweismittel oft deutschsprachig |
| Vermeidung Übersetzungskosten Anlagen | Streitkultur weniger reibungsbehaftet |
| Image Justizstandort Deutschland | Vollstreckung im Inland ohne Übersetzung |
| Auch BGH-Fortführung möglich | Drittbeteiligte (Zeugen) oft nur deutsch |

Drittbeteiligte (Zeugen, Sachverständige) sind nicht an die Sprachwahl gebunden. § 185 GVG (Dolmetscherbestellung) bleibt anwendbar. Bei Sachverständigen-Gutachten häufig deutsch.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `klageschrift-english-limitation-tolling`

_Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes of action, relief sought, evidence und exhibits im Commercial Courts Deutschland._

# Statement of Claim

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Statement of Claim
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `contract-interpretation-de-en`

_Erklärt und prüft englische Vertragsbegriffe unter deutschem Recht: reasonable efforts, best endeavours, indemnity, warranty, termination, material adverse change im Commercial Courts Deutschland._

# Contract Interpretation DE/EN

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Contract Interpretation DE/EN
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Englische Vertragsbegriffe unter deutschem Recht

| Englischer Begriff | Common-Law-Bedeutung | Anwendung unter §§ 133, 157 BGB |
| --- | --- | --- |
| **best endeavours** | höchste Anstrengung | typische Auslegung: wirtschaftlich zumutbare Anstrengung; nicht: alles unter Verschleiß eigener Existenz |
| **reasonable efforts / reasonable endeavours** | zumutbare Anstrengung | ähnlich § 242 BGB Verkehrssitte; objektivierte Bemühenspflicht |
| **commercially reasonable efforts** | kaufmännisch zumutbar | kaufmännischer Maßstab § 347 HGB; orientiert sich an Geschäftsbranche |
| **indemnity (Freistellung)** | Schadlosstellung | Garantievertrag oder selbständige Schuldübernahme; § 257 BGB Freistellungsanspruch |
| **warranty** | Garantie | § 443 BGB selbständige Garantie; verschuldensunabhängige Haftung |
| **representation** | Zusicherung | unter altem Schuldrecht relevant; unter neuem Schuldrecht meist als Garantie zu lesen oder § 311 Abs. 2 BGB c.i.c. |
| **covenant** | (Unter-)Verpflichtung | meist Tun/Unterlassen § 241 Abs. 1 BGB |
| **material adverse change (MAC)** | wesentlich nachteilige Veränderung | strikt zu definieren; ohne Definition Auslegung über § 313 BGB Wegfall der Geschäftsgrundlage |
| **liquidated damages** | pauschalierter Schadensersatz | bei Verbraucherbeteiligung § 309 Nr. 5 BGB AGB-Kontrolle; bei B2B § 307 BGB |
| **time is of the essence** | Termin als Hauptpflicht | bei Verletzung Rücktritt ohne Nachfrist § 323 Abs. 2 Nr. 2 BGB |
| **entire agreement clause** | abschließende Vereinbarung | wirksam, aber Auslegung § 133 BGB bleibt anwendbar; vorvertragliche Verhandlungen können relevant sein |
| **good faith** | Treu und Glauben | direkt § 242 BGB |
| **termination for cause** | außerordentliche Kündigung | § 314 BGB Dauerschuldverhältnis, wichtiger Grund |
| **termination for convenience** | ordentliche Kündigung ohne Grund | abhängig vom Vertragstyp; bei Werk-/Dienstvertrag in Schranken (§§ 627, 649 BGB) |
| **force majeure** | höhere Gewalt | § 275 Abs. 1 BGB Unmöglichkeit; sehr restriktive deutsche Praxis (Pandemie meist nicht) |
| **gross negligence** | grobe Fahrlässigkeit | § 277 BGB diligentia quam in suis; in AGB Haftungsbeschränkung unwirksam § 309 Nr. 7 BGB |
| **wilful misconduct** | Vorsatz | § 276 Abs. 3 BGB Haftung kann nicht ausgeschlossen werden |
| **specific performance** | tatsächliche Erfüllung | gesetzlicher Regelfall in Deutschland § 241 Abs. 1 BGB; Käufer kann auf Nacherfüllung bestehen § 439 BGB |
| **consequential damages** | Folgeschäden | unter BGB ohne Ausschluss erstattbar § 252 BGB; vertragliche Beschränkung üblich |

### Trade-off und Praktiker-Tipp

- **Doppeldeutige englische Klauseln:** Bei Streit immer auf § 133 BGB ("wirklicher Wille") und § 157 BGB ("Verkehrssitte") abstellen. Bei englischen Vertragsgewohnheiten Sachverständigengutachten möglich.
- **Deutsche Übersetzung als Hilfsmittel:** Bei Zweideutigkeit oft hilfreich. Aber: bei "governing law: German law" gilt deutsche Auslegung der englischen Begriffe.
- **AGB-Kontrolle:** englische Vertragsklauseln in B2B-AGB unterliegen §§ 305 ff. BGB. Asymmetrische Klauseln (z.B. "best endeavours" nur einer Partei) werden über § 307 BGB überprüft.
- **Vorvertragliche Verhandlungen:** entire-agreement-Klauseln schließen Schriftverkehr nicht als Auslegungshilfe aus (BGH ständige Rechtsprechung zur Auslegung).

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `document-production-earn-out`

_Prüft Urkundenvorlage und Dokumentenherausgabe nach deutschem Prozessrecht im Commercial-Court-Kontext: § 142 ZPO, Substantiierung, Geheimnisse, proportionality im Commercial Courts Deutschland._

# Document Production

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Document Production
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Vorlageanker im deutschen Prozessrecht:** § 142 ZPO Anordnung der Urkundenvorlage durch Partei (Ermessen des Gerichts, Substantiierungspflicht); § 144 ZPO Vorlage von Augenscheinsobjekten und Sachverständigengutachten; §§ 421-432 ZPO Vorlageantrag gegen Gegner und Dritte mit materiellrechtlichem Anspruch (§ 810 BGB Einsichtsrecht); § 422 ZPO bei Vorlagepflicht aus materiellem Recht; § 423 ZPO bei Bezugnahme der Gegenseite auf die Urkunde.
3. **Substantiierung Antrag § 142 ZPO:** Konkrete Bezeichnung der Urkunde (Datum, Ersteller, Inhalt, Empfänger); Tatsachen, für die die Urkunde Beweis sein soll; Hinweis auf Besitz oder erleichternde Besitzvermutung; konkrete Relevanz für die anstehende Beweisaufnahme. Bloße "fishing expedition" ist unzulässig — deutscher Zivilprozess kennt keine US-Discovery (§ 138 ZPO Wahrheitspflicht und § 282 ZPO Zurückweisung verspäteten Vorbringens).
4. **Geheimnisschutz und Verhältnismäßigkeit:** § 174 Abs. 3 GVG Ausschluss der Öffentlichkeit, § 16 GeschGehG Schutz von Geschäftsgeheimnissen im Prozess (sog. "Hamburger Verfahren" mit Geheimhaltungsverpflichtung der Verfahrensbeteiligten); bei DSGVO-relevanten Daten zusätzliche Abwägung Art. 6 Abs. 1 lit. f DSGVO. Trade-off: weite Vorlageanordnung erleichtert Beweis, gefährdet aber Vertraulichkeit.
5. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären. Nächsten Schritt: konkreter § 142-Antrag mit Anlage K-Nummer, Geheimnisschutzantrag § 16 GeschGehG, Frist für Vorlage durch Gegenseite festlegen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `finance-banking-dispute`

_Bearbeitet Finance-, Banking- und Capital-Markets-Streitigkeiten mit englischen Dokumenten: facility agreement, covenants, events of default, security, notices im Commercial Courts Deutschland._

# Finance Disputes

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Finance Disputes
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Finance-/Banking-Streit — Anspruchstypen und Verteidigungsfelder

| Streittyp | Norm | Klassische Streitfragen |
| --- | --- | --- |
| Darlehensvertrag (Schuldnerseite klagt) | §§ 488 ff. BGB | Wirksamkeit, Schriftform, Aufklärung über Risiken, Sittenwidrigkeit § 138 BGB |
| Kreditkündigung | § 490 BGB | wichtiger Grund, Verhältnismäßigkeit, Vertragstreue § 242 BGB |
| Sicherheitenverwertung | §§ 1233 ff. BGB (Pfandrecht), §§ 1257, 854 ZPO; § 14 InsO | Werthaltigkeit, Übersicherung, Anfechtung §§ 129 ff. InsO |
| Covenants / Loan Documentation | LMA/MUSTER; im DE: §§ 305 ff. BGB AGB-Kontrolle | financial covenants Verletzung; Material Adverse Effect |
| Cash Sweeps / Equity Cure | Vertragsrecht | Berechnungsstreit, Reporting-Verstoß |
| Events of Default | Vertragsbedingungen | Trigger-Bestimmung, Heilungsfrist, Cross-Default |
| Acceleration | Vertragsbedingungen | Verhältnismäßigkeit, Treu und Glauben |
| Schadensersatz wegen Falschberatung | §§ 280, 311 Abs. 2 BGB (c.i.c.) | Aufklärungspflicht, Kausalität, Mitverschulden § 254 BGB |
| Beraterhaftung (Investor) | § 280 BGB i.V.m. § 31 WpHG | Geeignetheit, Risikoaufklärung |
| Anfechtung Schenkung an Geschäftsführer | § 134 InsO | Insolvenzanfechtungsanspruch |

### Spezialthemen Banking

| Thema | Norm/Praxis |
| --- | --- |
| KWG-Erlaubnis | §§ 32, 54 KWG; BaFin-Praxis |
| MiCAR (Krypto) | EU-VO 2023/1114, geltend seit 30.12.2024 |
| MaRisk | BaFin-Rundschreiben; relevant für Klagen wegen Aufsichtsverstößen |
| Bankgeheimnis | Vertragliche Schweigepflicht; § 383 ZPO Zeugnisverweigerung |
| § 675u BGB (Phishing) | Haftung Bank bei nicht autorisierter Zahlung; Grenzen § 675v BGB (grobe Fahrlässigkeit Kunde) |

### Beweissicherung

- **Documents of Title:** Wechsel, Schuldscheine, Hypothekenbriefe — physische Sicherung kritisch.
- **Loan File:** alle Auszahlungs-Notices, Statements, Reporting-Reports.
- **Communication Trail:** E-Mails über Verhandlungen, Renegotiations, Standstills.
- **Beratungsprotokolle § 34 WpHG** (für Anlageberatung) — bei Beraterhaftungsklage entscheidend.

### Trade-off und Praktiker-Tipp

- **Bank-Auflage:** Bei Klage durch Kunde gegen Bank: Auflage zur Vorlage des Beratungsprotokolls § 142 ZPO; bei Verweigerung Beweisvereitelung § 286 ZPO.
- **Großforderungen mit ESM/EFSF-Bezug:** spezielle Immunitätsregeln beachten.
- **Forum mit Sachkenntnis:** Commercial Court bei OLG Frankfurt mit hoher Finanz-Expertise; Mannheim für IP/Patent.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `forumwahl-court-glossary`

_Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist eine Vorstandsvorlage mit Empfehlung im Commercial Courts Deutschland._

# Forumwahl gegenüber Schiedsgericht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Forumwahl gegenüber Schiedsgericht
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Forum-Vergleich (Vorstandsvorlage)

| Kriterium | Commercial Court (OLG) | Commercial Chamber (LG) | Schiedsgericht (DIS, ICC, LCIA) | Ordentliches LG (KfH) |
| --- | --- | --- | --- | --- |
| Rechtsgrundlage | § 119b GVG | §§ 95, 184a GVG | §§ 1029 ff. ZPO | §§ 95 ff. GVG |
| Streitwert | regelmäßig ab 500.000 EUR | ohne harte Schwelle | ohne | nach GVG-Schwellen |
| Sprache | DE/EN | DE/EN | frei wählbar | DE |
| Vertraulichkeit | § 273a ZPO Anordnung möglich | dito | grundsätzlich gegeben | öffentliche Verhandlung |
| Beweisaufnahme | richterliche Prozessleitung | dito | flexibler; nahe Common Law möglich | dito |
| Dauer (erste Instanz) | ca. 12-18 Monate | ca. 18-30 Monate | ca. 12-24 Monate (Institut) | ca. 18-30 Monate |
| Berufung / Rechtsmittel | nur Revision § 184b GVG zum BGH | Berufung OLG, Revision BGH | nur Aufhebung § 1059 ZPO | dito ordentliche Wege |
| Vollstreckung Ausland | EuGVVO/Brüssel Ia EU; sonst Anerkennungsverfahren | dito | New York Convention 1958 weltweit | dito |
| Kosten | GKG + RVG | dito | Schiedsrichterhonorare + Institut + Anwälte | GKG + RVG |
| Anwaltszwang | ja | ja | abhängig von Schiedsordnung | ja |
| Wahl der Richter | nein | nein | ja (party-appointed) | nein |
| Eilrechtsschutz | §§ 916, 935 ZPO Arrest/eV | dito | sehr eingeschränkt; staatliche Gerichte daneben § 1033 ZPO | dito |

### Trade-off Argumente

| Pro Commercial Court / Chamber | Pro Schiedsgericht |
| --- | --- |
| Günstiger Streitwert ab 5-10 Mio. EUR (gedeckelte GKG) | Vertraulichkeit zentral (kein Filing, keine Pressepräsenz) |
| BGH-Revision als Rechtssicherheit | freie Schiedsrichterwahl, Branchen-Expertise |
| Schnellere mündliche Verhandlung | weltweite Vollstreckung New York Convention |
| Staatliche Autorität bei renitentem Gegner | bei Cross-Border-Fällen ohne EU-Bezug oft schneller |
| Wortprotokoll § 613 ZPO neu | Sprachwahl ohne § 184a GVG-Beschluss |
| Klare Anwendung deutschen materiellen Rechts | Verfahrensautonomie (UNCITRAL-Model) |

### Empfehlung je Fallkonstellation

| Konstellation | Empfehlung |
| --- | --- |
| Inhouse-Streit, Beschlussmängelklage GmbH | Commercial Chamber LG (BGH-Rspr. "Schiedsfähigkeit II" zu Schiedsklauseln im Gesellschaftsvertrag beachten) |
| Post-M&A Warranty Claim 5-50 Mio. EUR | Commercial Court OLG oder Schiedsgericht (W&I-Versicherer hat Mitspracherecht) |
| Cross-Border-Lieferkette, Vollstreckung in USA/Asien | Schiedsgericht (NYC Convention) |
| Massive Geheimhaltung (Patente, Trade Secrets) | Schiedsgericht oder Commercial Court mit § 273a ZPO |
| Schnelles Urteil mit hoher Reputationswirkung | Commercial Court OLG (Publicity) |
| Lieferantenstreit unter 5 Mio. EUR | KfH LG (kosten- und schnellgerecht) |

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `post-ma-pre-litigation`

_Bearbeitet Post-M&A Warranty Claims vor Commercial Courts: notice, knowledge qualifiers, baskets, caps, leakage, earn-out, accounts and expert determination im Commercial Courts Deutschland._

# Post-M&A Warranty Claims

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Post-M&A Warranty Claims
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Post-M&A Warranty Claim — Prüfraster

| Schritt | Inhalt | Norm/SPA-Bezug |
| --- | --- | --- |
| 1. Notice-Frist | im SPA meist 30-60 Tage ab Kenntnis; absolute Survival meist 18-24 Monate für General Warranties, 5-7 Jahre für Tax/Fundamental | § 437 BGB als gesetzliches Pendant; Vertragsfrist hat Vorrang |
| 2. Notice-Inhalt | Anspruchsgrundlage (Garantienennung), Sachverhalt, Höhe (Bandbreite), Anlagen | Vertragsanforderungen strikt einhalten |
| 3. Knowledge-Qualifier | "to the Seller's Knowledge" — Personenkreis genau bestimmen (Disclosure Schedule, Drittwissen?) | typischer Streitpunkt: Wissen vs. Wissenmüssen |
| 4. Disclosure Letter | hat Garantie qualifiziert? "Disclosed Matters" entlasten Verkäufer | Lex specialis vor Garantietext |
| 5. Baskets (De-minimis & Threshold) | Bagatellsumme einzeln (z.B. 50.000 EUR), Gesamtschwelle (z.B. 1 Mio. EUR) | Tipping-Basket versus Excess-Basket prüfen |
| 6. Cap | Haftungsobergrenze meist 10-20 % des Kaufpreises | Fundamental: 100 %, Tax: 100 %, General: limitiert |
| 7. Schadenberechnung | direkter Schaden / lost profits / consequential damages — was deckt SPA? | § 252 BGB i.V.m. § 249 BGB als gesetzlicher Maßstab, oft contractually limited |
| 8. W&I-Versicherung | parallelle Meldung Versicherer, Tail-Coverage einhalten | Underwriting-Liste mit Ausschlüssen prüfen |
| 9. Mitigationspflicht | § 254 BGB i.V.m. SPA-Klausel; Käufer muss Schaden minimieren | Beweislast trägt Verkäufer |
| 10. Verjährung | Vertragslaufzeit (Survival) versus § 195 BGB drei Jahre | Vertragslaufzeit ist meist Ausschlussfrist, nicht Verjährung |
| 11. Earn-Out und Locked-Box | parallele Anpassungsstreitigkeiten | § 315 BGB Leistungsbestimmung, Expert Determination |
| 12. Streitbeilegung | SPA-Klausel: Schiedsgericht oder Commercial Court? | § 1029 ZPO versus § 119b GVG / §§ 184a GVG |

### Trade-off Settlement versus Litigation

- **Vorzeitiges Settlement:** spart Kosten und Reputation; aber kostet auch Recht auf weitere Claims.
- **Litigation:** in Deutschland kostengünstig, aber langsam (oft 2-4 Jahre bis OLG-Urteil).
- **W&I-Versicherer:** drängt häufig auf Vergleich vor mündlicher Verhandlung; Mandant muss Verzichtserklärungen aufmerksam prüfen.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `interim-relief-issues-list`

_Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sicherheitsleistung und Vollziehung im Commercial Courts Deutschland._

# Interim Relief

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Interim Relief
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Einstweiliger Rechtsschutz — Übersicht

| Maßnahme | Norm | Schutzobjekt | Voraussetzungen | Zuständig |
| --- | --- | --- | --- | --- |
| Arrest | § 916 ZPO | Geldforderung | Arrestanspruch + Arrestgrund (Vereitelungsgefahr) | LG/AG je nach Streitwert; bei Commercial Court Streit i.V.m. § 119b GVG |
| Einstweilige Verfügung — Sicherungsverfügung | § 935 ZPO | Anspruch außer Geld (Sicherung des Streitgegenstands) | Verfügungsanspruch + Verfügungsgrund | dito |
| Einstweilige Verfügung — Regelungsverfügung | § 940 ZPO | vorläufige Regelung eines Rechtsverhältnisses | Verfügungsanspruch + Verfügungsgrund | dito |
| Einstweilige Verfügung — Leistungsverfügung | gewohnheitsrechtlich (BGH ständige Rechtsprechung); § 935 ZPO analog | vorübergehende Befriedigung (z.B. Wettbewerbsverstoß) | strenge Anforderungen | dito |
| ARRest auf Patentstreit, Pre-Trial | § 916 ZPO i.V.m. ZPO Spezialnormen | Geldforderung | strenge Anforderungen Geheimhaltung | LG-Patentkammer |

### Verfügungsgrund / Eilbedürftigkeit

| Argument | Inhalt | Praxis |
| --- | --- | --- |
| Vermögenswerteflucht | Vermögensentzug, Verschiebung ins Ausland | bei Auslandsbezug stark |
| Drohende Verkaufshandlung | irreversibler Verlust des Schutzguts | typisch IP-Verletzung |
| Insolvenznähe der Gegenseite | Schutzbedürfnis vor anderen Gläubigern | Insolvenzantragspflicht § 15a InsO |
| Verstreichen einer Klage- oder Verjährungsfrist | Anspruch verfällt | für Eilbedürftigkeit relevant |
| Vorgreifliche Tatsachen | Beweismittel würden verloren gehen | § 485 ZPO selbständiges Beweisverfahren parallel |

### Trade-off und Praxistipp

- **Sicherheitsleistung § 921 ZPO:** Bei eV regelmäßig Sicherheitsleistung verlangt; Bürgschaft einer deutschen Großbank typisch (5-25 % der Forderungssumme).
- **Schadensersatzrisiko § 945 ZPO:** Bei nachträglicher Aufhebung der eV trägt Antragsteller verschuldensunabhängige Schadenshaftung. Daher: vorher gründlich prüfen.
- **Mündliche Verhandlung oder Beschluss:** Bei Antrag ohne mündliche Verhandlung schneller; Gegner kann jedoch Widerspruch nach § 924 ZPO einlegen, dann doch Verhandlung.
- **Internationale Wirkung:** Brüssel Ia-VO Art. 36 ermöglicht Anerkennung in EU. Für USA/Asien: dort eigenes Eilverfahren notwendig.
- **Vollziehungsfrist § 929 Abs. 2 ZPO:** Beschluss muss binnen einem Monat ab Erlass dem Gegner zugestellt sein, sonst Wirkungsverlust. KRITISCH bei Auslandsstoff (Haager Zustellungsübereinkommen, mehrere Wochen).

### Schutzschrift § 945a ZPO

Wer Eilanträge gegen sich erwartet (z.B. nach Abmahnung), kann eine Schutzschrift einreichen: Vorabverteidigung, die das Gericht vor Erlass des eV-Beschlusses berücksichtigen muss. Hinterlegt zentral beim Schutzschriftenregister.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `witness-preparation-zustandigkeit-119b`

_Bereitet Zeugen in englischsprachigen deutschen Verfahren vor: Wahrheitspflicht, keine Coaching-Grenzüberschreitung, Sprachsicherheit, Dokumente, Ablauf im Commercial Courts Deutschland._

# Witness Preparation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Witness Preparation
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `english-legal-writing-for-german-courts`

_Verbessert englische Schriftsätze für deutsche Gerichte: klar, zpo-tauglich, ohne US-Discovery-Duktus, mit sauberem Tatsachenvortrag und Beweisangebot im Commercial Courts Deutschland._

# English Legal Writing

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: English Legal Writing
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen. Sprache rechtlich nach §§ 184 ff. GVG i.V.m. Landesverordnung gesichert (mit Inkrafttreten Justizstandort-Stärkungsgesetz von 2024 erweitert).
2. **Struktur deutsche ZPO-Schriftsatz auf Englisch:** Anträge ("Requests for relief"), Sachverhalt ("Statement of facts" / "factual background"), rechtliche Würdigung ("legal assessment" / "legal grounds"), Beweisangebote ("offer of evidence" mit Anlagenbezeichnung K1, K2, ...). Vermeiden: "Counts" oder "Causes of action" (US-Stil), "Prayer for relief" (zu Common-Law), "Plaintiff hereby moves for..." (verkürzt).
3. **Substantiierungsstandard wahren:** Jeder Tatsachenvortrag konkret, mit Datum, Ort, Beteiligten und Bezug zu Anlage; keine "notice pleading" wie unter FRCP. Beweisangebote: Zeugen mit Name und ladungsfähiger Anschrift, Urkunden mit konkreter Bezeichnung (Anlage K-Nummer), Sachverständige mit Themenbereich, Parteivernehmung als Hilfsbeweis.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären. Tonalität: nüchtern, professionell, ohne Verstärker ("clearly", "obviously"), ohne emotional aufgeladene Sprache ("egregious", "outrageous").
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `hearing-script-english-advocacy`

_Erstellt englische Hearing Scripts für deutsche Anwälte: opening, issue roadmap, witness questions, judicial questions, closing and settlement signals im Commercial Courts Deutschland._

# English Hearing Advocacy

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: English Hearing Advocacy
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

---

## Skill: `bgh-english-bilingual-client`

_Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Tenor und Mandantenkommunikation im Commercial Courts Deutschland._

# BGH in English

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: BGH in English
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### BGH-Revision auf Englisch nach § 184b GVG

Das Justizstandort-Stärkungsgesetz hat § 184b GVG eingeführt: Revision vor dem BGH kann in englischer Sprache geführt werden, wenn die Vorinstanz (Commercial Court oder Commercial Chamber) auf Englisch verhandelt hat und beide Parteien zustimmen.

| Verfahrensschritt | Praxishinweis | Norm |
| --- | --- | --- |
| Voraussetzung erstinstanzliches Verfahren | mündliche Verhandlung und Urteil in Englisch (§ 184a GVG) | § 184b Abs. 1 GVG |
| Antrag bei BGH | förmlicher Antrag, Zustimmung beider Parteien | § 184b Abs. 1 Satz 1 GVG |
| Anwalt für BGH | nur am BGH zugelassener Rechtsanwalt § 78 ZPO Abs. 1 Satz 3 ZPO i.V.m. §§ 162 ff. BRAO | Sprachkenntnisse zwingend; Liste BGH-Anwälte sehr begrenzt |
| Revisionsbegründung | innerhalb der Frist § 551 ZPO; in Englisch zulässig | nur Rechtsfragen, kein neuer Tatsachenvortrag (§ 559 ZPO) |
| Mündliche Verhandlung | sofern BGH zulässt; oft schriftliches Verfahren | Sprache Englisch |
| Tenor und Begründung | Englisch zulässig; für Vollstreckung Übersetzung nach § 110 ZPO bzw. Brüssel Ia-VO Art. 42 | praxisrelevant |
| Veröffentlichung | BGH-Datenbank meist deutsch; englische Originalfassung als Anlage | § 169 GVG |
| Streitwert | Revisionsbeschwer § 26 Nr. 8 EGZPO (z.Zt. 20.000 EUR Mindestbeschwer für Nichtzulassungsbeschwerde) | live aktuelle Schwelle prüfen |

### Trade-off Englisch versus Übersetzung

- **Englisch bis BGH:** spart Übersetzungskosten und Brüche; aber sehr enger Anwaltskreis (BGH-Anwälte mit Englisch-Praxis).
- **Schwächen:** Anlagen aus früheren Verfahren oft Deutsch; nicht alle BGH-Senate haben Spracherfahrung; bei Aufhebung und Zurückverweisung muss Tatsacheninstanz die Sprache fortführen können.
- **Praktiker-Tipp:** Bereits in Klage und Berufung BGH-Anwalt einbinden, der später Revision führen kann.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 184a GVG
- § 184b GVG
- § 119b GVG
- § 93 AktG
- § 246 AktG
- § 43 GmbHG
- § 3a RVG
- § 169 GVG
- § 185 GVG
- § 174 GVG
- § 16 GeschGehG
- § 23 GVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

