# commercial-courts-deutschland

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`commercial-courts-deutschland`) | [`commercial-courts-deutschland.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/commercial-courts-deutschland.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

> Prozessarbeitsplatz für englischsprachige Wirtschaftsverfahren vor deutschen Commercial Courts und Commercial Chambers. Das Plugin hilft bei Forumwahl, Klage, Verteidigung, Case Management, Beweis, Geheimnisschutz, Wortprotokoll, Rechtsmittel, Kosten, Vollstreckung und bilingualer Mandantenkommunikation.

## Wofür dieses Plugin gedacht ist

Commercial Courts sollen internationale Wirtschaftsverfahren in Deutschland attraktiver machen. Dieses Plugin macht daraus einen geführten Arbeitsablauf: nicht Common Law spielen, sondern deutsches Prozessrecht in englischer Arbeitssprache präzise beherrschen.

Es unterstützt insbesondere:

- englische oder zweisprachige Schriftsatzentwürfe,
- Forum- und Klauselprüfung,
- Zuständigkeits- und Sprachwahlprüfung,
- Case-Management-Termin und Timetable,
- Beweis- und Anlagenorganisation,
- Geheimnisschutz und vertrauliche Anlagen,
- Wortprotokoll/verbatim transcript,
- Rechtsmittel und BGH-Fortsetzung,
- Board- und Mandantenbriefings in DE/EN.

## Kaltstart

Der Einstieg fragt zuerst:

1. Deutsch, Englisch oder zweisprachig?
2. Commercial Court, Commercial Chamber, Schiedsgericht oder anderes Forum?
3. Welche Klausel und welcher Streitwert?
4. Was ist die nächste Prozesshandlung?
5. Welche Anlagen und Fristen liegen vor?

Danach routet er in die passenden Spezialskills.

## Typische Outputs

- English Statement of Claim / Statement of Defence
- Case Management Conference Pack
- Procedural Timetable
- Evidence Map und Exhibit Index
- Confidentiality Application
- Verbatim Transcript Request Strategy
- Hearing Script
- Settlement Term Sheet
- Appeal/Revision Memo
- Board Briefing DE/EN

## Quellenhygiene

Vor produktiver Verwendung müssen Bundesrecht, Landesrecht und Gerichtsseite live geprüft werden. Dieses Plugin nennt keine erfundenen Commercial-Court-Standorte und keine Paywall-Fundstellen. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgegeben.

## Verhältnis zu anderen Plugins

- `prozessrecht`: allgemeine ZPO-Mechanik.
- `word-legal-ai-plugin-and-skill-for-german-lawyers`: Schriftsatz- und Stilfinish.
- `gesellschaftsrecht-legal-english`: Transaktionsenglisch und Corporate-Begriffe.
- `common-law-kompass`: falsche Freunde bei Common-Law-Erwartungen.
- `zitierweise-deutsches-recht`: Quellen- und Zitierhygiene.

## Skills

| Skill | Funktion |
| --- | --- |
| `commercial-courts-deutschland-allgemein` | Einstieg, Schnelltriage und Workflow-Routing für Commercial-Courts-Verfahren in Deutschland; erkennt Forum, Sprache, Streitwert, Parteivereinbarung, Case Management, Geheimnisschutz, Beweis, Transcript, Rechtsmittel und englischen Outputbedarf. |
| `commercial-court-kaltstart-interview` | Kaltstart-Interview für neue Commercial-Court-Mandate: Parteien, Streitgegenstand, Streitwert, Gerichtsstands-/Sprachklausel, gewünschte Sprache, Unterlagen, Fristen, Output. |
| `zustandigkeit-119b-gvg-check` | Prüft, ob Commercial Court oder Commercial Chamber eröffnet ist: Wirtschaftsstreitigkeit, Streitwert, Parteivereinbarung, Landesrecht, OLG/LG, internationale Zuständigkeit und Rügefragen. |
| `commercial-chamber-vs-commercial-court` | Vergleicht Commercial Chamber beim Landgericht und Commercial Court beim Oberlandesgericht: Instanz, Zuständigkeit, Streitwert, Verfahrenssprache, Tempo, Rechtsmittel und Mandantenstrategie. |
| `forumwahl-commercial-court-vs-schiedsgericht` | Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist eine Vorstandsvorlage mit Empfehlung. |
| `englische-verfahrenssprache-184a-gvg` | Prüft und gestaltet die englische Verfahrenssprache: Parteivereinbarung, Schriftsätze, Anlagen, mündliche Verhandlung, Protokoll, Urteil, Übersetzungen und BGH-Fortsetzung. |
| `jurisdiction-clause-drafting-de-en` | Entwirft deutsch-englische Commercial-Court-Gerichtsstands- und Sprachklauseln für Verträge, AGB-nahe Konstellationen und M&A/Finance-Deals. |
| `pre-litigation-notice-and-standstill` | Bereitet Pre-Action Letter, Standstill Agreement und Verjährungshemmung vor, wenn ein Commercial-Court-Verfahren droht. |
| `claim-intake-fakten-und-exhibits` | Macht aus unordentlichen Deal-Unterlagen ein Claim Intake: Parteien, Vertrag, Breach, Damages, Exhibits, Timeline und Streitwert. |
| `klageschrift-english-statement-of-claim` | Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes of action, relief sought, evidence und exhibits. |
| `defence-answer-and-jurisdiction-objections` | Bereitet Klageerwiderung/Statement of Defence vor: Zuständigkeitsrügen, Sprachrügen, Bestreiten, Einwendungen, Counterclaim, Set-off und Beweise. |
| `ruegelose-einlassung-und-sprache` | Warnt vor rügeloser Einlassung: Zuständigkeit, Sprache, Einlassungsfrist, Verteidigungsanzeige, Prozessstrategie und Mandantenfreigabe. |
| `case-management-conference` | Bereitet Case-Management-Termin vor: issues list, timetable, evidence, confidentiality, settlement, transcript, language and hearing logistics. |
| `procedural-calendar-timetable-order` | Erstellt einen prozessualen Verfahrenskalender mit Schriftsatzfristen, Anlagen, Übersetzungen, Witness Statements, Sachverständigen und Hearing Date. |
| `issues-list-and-roadmap` | Formuliert eine Issues List für Commercial-Court-Verfahren: legal issues, factual issues, evidence issues, quantum, jurisdiction and language. |
| `evidence-map-zpo-vs-common-law` | Erklärt Mandanten den Unterschied zwischen deutscher Beweisaufnahme und Common-Law-Erwartungen; erstellt Evidence Map ohne Discovery-Fantasien. |
| `document-production-142-zpo` | Prüft Urkundenvorlage und Dokumentenherausgabe nach deutschem Prozessrecht im Commercial-Court-Kontext: § 142 ZPO, Substantiierung, Geheimnisse, proportionality. |
| `exhibits-translation-608-zpo` | Plant Anlagen, Übersetzungen und Sprache: welche Dokumente englisch bleiben können, wann Übersetzung nötig ist, wie Exhibit Index und Bundle aussehen. |
| `third-party-notice-607-zpo` | Prüft Streitverkündung, Nebenintervention und Drittbeteiligung bei englischsprachigen Commercial-Court-Verfahren. |
| `confidentiality-trade-secrets-273a-zpo` | Schützt Geschäftsgeheimnisse: Geheimhaltungsantrag, abgestufter Zugang, redacted exhibits, in camera concerns, Trade Secrets Act und Prozessstrategie. |
| `public-hearing-and-press` | Steuert Öffentlichkeit, Presse, Public Relations und sensitive Unternehmenskommunikation bei hochkarätigen Commercial-Court-Verfahren. |
| `video-hearing-128a-284-zpo` | Prüft Videoverhandlung, hybride Beweisaufnahme, ausländische Zeugen, Techniktest und Protokollierung. |
| `verbatim-transcript-613-zpo` | Plant das Wortprotokoll/verbatim transcript: Antrag, Kosten, Verhandlungsstrategie, Korrektur, Zitierfähigkeit und Nutzung im Rechtsmittel. |
| `hearing-script-english-advocacy` | Erstellt englische Hearing Scripts für deutsche Anwälte: opening, issue roadmap, witness questions, judicial questions, closing and settlement signals. |
| `witness-preparation-english-zpo` | Bereitet Zeugen in englischsprachigen deutschen Verfahren vor: Wahrheitspflicht, keine Coaching-Grenzüberschreitung, Sprachsicherheit, Dokumente, Ablauf. |
| `expert-evidence-german-court-expert` | Plant Sachverständigenbeweis: Privatgutachten, gerichtlicher Sachverständiger, Fragenkatalog, technische Anlagen, Parteigutachten und Anhörung. |
| `interim-relief-arrest-injunction` | Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sicherheitsleistung und Vollziehung. |
| `settlement-court-recorded-settlement` | Bereitet gerichtlichen Vergleich, settlement agreement, consent order, Vollstreckbarkeit und mehrsprachige Vergleichsdokumentation vor. |
| `enforcement-and-translation` | Prüft Vollstreckung aus Commercial-Court-Urteilen/Vergleichen: Titel, Klausel, Zustellung, Übersetzung, EU-/Auslandsbezug und assets. |
| `appeal-and-revision-614-zpo` | Prüft Rechtsmittel und Revision/BGH-Pfad nach Commercial-Court-Verfahren: Zulassung, Sprache, Transcript, Tatbestand, Rechtsfehler und Strategie. |
| `bgh-english-proceedings-184b-gvg` | Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Tenor und Mandantenkommunikation. |
| `costs-court-fees-risk-budget` | Erstellt Kosten- und Risikobudget: Gerichtskosten, Anwaltskosten, Übersetzung, Transcript, Sachverständige, Security, Settlement und Enforcement. |
| `service-abroad-hague-eu` | Plant Zustellung ins Ausland: EuZVO, Haager Zustellungsübereinkommen, Übersetzung, service agents, Fristen und Nachweis. |
| `cross-border-jurisdiction-brussels-ia` | Prüft internationale Zuständigkeit, Gerichtsstandsvereinbarung, Brüssel Ia, Lugano-Bezug, Drittstaaten und Anti-suit-/lis-pendens-Risiken. |
| `governing-law-rome-i-ii` | Prüft anwendbares Recht: Rom I/Rom II, Rechtswahl, Eingriffsnormen, UN-Kaufrecht, Beweis fremden Rechts und Übersetzung der Normbegriffe. |
| `post-ma-warranty-claim` | Bearbeitet Post-M&A Warranty Claims vor Commercial Courts: notice, knowledge qualifiers, baskets, caps, leakage, earn-out, accounts and expert determination. |
| `earn-out-accounting-dispute` | Strukturiert Earn-out- und Kaufpreisanpassungsstreitigkeiten: accounting principles, expert determination, disclosure, damages and procedural tactics. |
| `shareholder-board-dispute` | Bearbeitet Gesellschafter-, Organ- und Joint-Venture-Streitigkeiten mit englischen Vertragsunterlagen vor deutschen Commercial Courts. |
| `director-officer-liability-dispute` | Prüft D&O-/Organhaftungsstreitigkeiten im Commercial-Court-Kontext: business judgment, damages, insurance, privilege-like concerns and evidence. |
| `supply-chain-international-sale-dispute` | Routet Lieferketten-, Vertrieb- und CISG-nahe Streitigkeiten: delivery, defects, force majeure, limitation, governing law and evidence. |
| `finance-banking-dispute` | Bearbeitet Finance-, Banking- und Capital-Markets-Streitigkeiten mit englischen Dokumenten: facility agreement, covenants, events of default, security, notices. |
| `contract-interpretation-de-en` | Erklärt und prüft englische Vertragsbegriffe unter deutschem Recht: reasonable efforts, best endeavours, indemnity, warranty, termination, material adverse change. |
| `english-legal-writing-for-german-courts` | Verbessert englische Schriftsätze für deutsche Gerichte: klar, zpo-tauglich, ohne US-Discovery-Duktus, mit sauberem Tatsachenvortrag und Beweisangebot. |
| `bilingual-client-board-briefing` | Erstellt bilinguale Board- und Mandantenbriefings zu Commercial-Court-Verfahren: risk, timeline, budget, settlement range, next decisions. |
| `bundle-index-electronic-filing` | Organisiert elektronisches Bundle, Anlagenindex, beA/ERV-Dateinamen, PDF/A, Lesezeichen, Übersetzungen und Exhibit References. |
| `bea-erv-english-pleadings` | Prüft beA/ERV-Einreichung englischer Schriftsätze: Dateiformat, Signatur, Anlagen, Fristen, Empfangsbekenntnis und Kanzlei-Workflow. |
| `protective-measures-confidential-exhibits` | Plant Schutzmaßnahmen für vertrauliche Anlagen: redactions, confidentiality club, restricted access, sealed bundles und Verhandlungsorganisation. |
| `mediation-settlement-window` | Findet Vergleichsfenster, Mediation, judicial settlement signals und Prozessvergleichsstrategie in Commercial-Court-Verfahren. |
| `arbitration-clause-conflict-check` | Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-Court-Klauseln. |
| `limitation-and-tolling-check` | Prüft Verjährung, Hemmung, Standstill, Klageerhebung, Zustellung demnächst und internationale Limitation Issues. |
| `counterclaim-setoff-claim-amendment` | Plant Widerklage, Hilfswiderklage, Aufrechnung, Klageänderung und amendment strategy in englischsprachigen Wirtschaftsprozessen. |
| `default-judgment-and-nonappearance` | Prüft Versäumnis, Anerkenntnis, Säumnisfolgen, Einspruch und taktische Nichtteilnahme in Commercial-Court-Verfahren. |
| `late-submissions-296-zpo` | Steuert verspätetes Vorbringen, Präklusion, Fristverlängerung, gerichtliche Hinweise und Schriftsatznachlass. |
| `local-rules-and-court-guidelines` | Erstellt Live-Check zu Landesrecht, Geschäftsverteilung, Commercial-Court-Guidelines und Gerichts-Webseite vor jeder Einreichung. |
| `redteam-commercial-court-qualitygate` | Red-Team-Gate für alle Commercial-Court-Outputs: Zuständigkeit, Sprache, Fristen, Beweise, Übersetzungen, Geheimnisschutz, Kosten, Rechtsmittel. |
| `glossary-commercial-court-de-en` | Erstellt ein DE/EN-Glossar für Commercial-Court-Mandate: ZPO-Begriffe, Anträge, Beweis, Tenor, Vergleich, Rechtsmittel und falsche Freunde. |
| `judgment-publication-and-anonymisation` | Prüft Urteil, Veröffentlichung, Anonymisierung, Geheimnisschutz, Übersetzungsbedarf und externe Kommunikation nach Entscheidung. |

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `appeal-and-revision-614-zpo` | Prüft Rechtsmittel und Revision/BGH-Pfad nach Commercial-Court-Verfahren: Zulassung, Sprache, Transcript, Tatbestand, Rechtsfehler und Strategie im Commercial Courts Deutschland. |
| `arbitration-clause-bea-erv` | Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-Court-Klauseln im Commercial Courts Deutschland. |
| `bea-erv-english-pleadings` | Prüft beA/ERV-Einreichung englischer Schriftsätze: Dateiformat, Signatur, Anlagen, Fristen, Empfangsbekenntnis und Kanzlei-Workflow im Commercial Courts Deutschland. |
| `bgh-english-bilingual-client` | Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Tenor und Mandantenkommunikation im Commercial Courts Deutschland. |
| `bilingual-client-board-briefing` | Erstellt bilinguale Board- und Mandantenbriefings zu Commercial-Court-Verfahren: risk, timeline, budget, settlement range, next decisions im Commercial Courts Deutschland. |
| `bundle-index-case-management` | Organisiert elektronisches Bundle, Anlagenindex, beA/ERV-Dateinamen, PDF/A, Lesezeichen, Übersetzungen und Exhibit References im Commercial Courts Deutschland. |
| `case-management-conference` | Bereitet Case-Management-Termin vor: issues list, timetable, evidence, confidentiality, settlement, transcript, language and hearing logistics im Commercial Courts Deutschland. |
| `claim-intake-chamber-vs` | Macht aus unordentlichen Deal-Unterlagen ein Claim Intake: Parteien, Vertrag, Breach, Damages, Exhibits, Timeline und Streitwert im Commercial Courts Deutschland. |
| `commercial-chamber-vs-commercial-court` | Vergleicht Commercial Chamber beim Landgericht und Commercial Court beim Oberlandesgericht: Instanz, Zuständigkeit, Streitwert, Verfahrenssprache, Tempo, Rechtsmittel und Mandantenstrategie im Commercial Courts Deutschland. |
| `commercial-court-kaltstart-interview` | Kaltstart-Interview für neue Commercial-Court-Mandate: Parteien, Streitgegenstand, Streitwert, Gerichtsstands-/Sprachklausel, gewünschte Sprache, Unterlagen, Fristen, Output. |
| `confidentiality-trade-contract-interpretation` | Schützt Geschäftsgeheimnisse: Geheimhaltungsantrag, abgestufter Zugang, redacted exhibits, in camera concerns, Trade Secrets Act und Prozessstrategie im Commercial Courts Deutschland. |
| `contract-interpretation-de-en` | Erklärt und prüft englische Vertragsbegriffe unter deutschem Recht: reasonable efforts, best endeavours, indemnity, warranty, termination, material adverse change im Commercial Courts Deutschland. |
| `costs-court-counterclaim-setoff` | Erstellt Kosten- und Risikobudget: Gerichtskosten, Anwaltskosten, Übersetzung, Transcript, Sachverständige, Security, Settlement und Enforcement im Commercial Courts Deutschland. |
| `counterclaim-setoff-claim-amendment` | Plant Widerklage, Hilfswiderklage, Aufrechnung, Klageänderung und amendment strategy in englischsprachigen Wirtschaftsprozessen im Commercial Courts Deutschland. |
| `cross-border-default-judgment` | Prüft internationale Zuständigkeit, Gerichtsstandsvereinbarung, Brüssel Ia, Lugano-Bezug, Drittstaaten und Anti-suit-/lis-pendens-Risiken im Commercial Courts Deutschland. |
| `default-judgment-and-nonappearance` | Prüft Versäumnis, Anerkenntnis, Säumnisfolgen, Einspruch und taktische Nichtteilnahme in Commercial-Court-Verfahren im Commercial Courts Deutschland. |
| `defence-answer-director-officer` | Bereitet Klageerwiderung/Statement of Defence vor: Zuständigkeitsrügen, Sprachrügen, Bestreiten, Einwendungen, Counterclaim, Set-off und Beweise im Commercial Courts Deutschland. |
| `director-officer-liability-dispute` | Prüft D&O-/Organhaftungsstreitigkeiten im Commercial-Court-Kontext: business judgment, damages, insurance, privilege-like concerns and evidence im Commercial Courts Deutschland. |
| `document-production-earn-out` | Prüft Urkundenvorlage und Dokumentenherausgabe nach deutschem Prozessrecht im Commercial-Court-Kontext: § 142 ZPO, Substantiierung, Geheimnisse, proportionality im Commercial Courts Deutschland. |
| `earn-out-accounting-dispute` | Strukturiert Earn-out- und Kaufpreisanpassungsstreitigkeiten: accounting principles, expert determination, disclosure, damages and procedural tactics im Commercial Courts Deutschland. |
| `enforcement-translation-english-legal` | Prüft Vollstreckung aus Commercial-Court-Urteilen/Vergleichen: Titel, Klausel, Zustellung, Übersetzung, EU-/Auslandsbezug und assets im Commercial Courts Deutschland. |
| `englische-verfahrenssprache-late-submissions` | Prüft und gestaltet die englische Verfahrenssprache: Parteivereinbarung, Schriftsätze, Anlagen, mündliche Verhandlung, Protokoll, Urteil, Übersetzungen und BGH-Fortsetzung im Commercial Courts Deutschland. |
| `english-legal-writing-for-german-courts` | Verbessert englische Schriftsätze für deutsche Gerichte: klar, zpo-tauglich, ohne US-Discovery-Duktus, mit sauberem Tatsachenvortrag und Beweisangebot im Commercial Courts Deutschland. |
| `evidence-map-exhibits-translation` | Erklärt Mandanten den Unterschied zwischen deutscher Beweisaufnahme und Common-Law-Erwartungen; erstellt Evidence Map ohne Discovery-Fantasien im Commercial Courts Deutschland. |
| `exhibits-translation-608-zpo` | Plant Anlagen, Übersetzungen und Sprache: welche Dokumente englisch bleiben können, wann Übersetzung nötig ist, wie Exhibit Index und Bundle aussehen im Commercial Courts Deutschland. |
| `expert-evidence-finance-banking` | Plant Sachverständigenbeweis: Privatgutachten, gerichtlicher Sachverständiger, Fragenkatalog, technische Anlagen, Parteigutachten und Anhörung im Commercial Courts Deutschland. |
| `finance-banking-dispute` | Bearbeitet Finance-, Banking- und Capital-Markets-Streitigkeiten mit englischen Dokumenten: facility agreement, covenants, events of default, security, notices im Commercial Courts Deutschland. |
| `forumwahl-court-glossary` | Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist eine Vorstandsvorlage mit Empfehlung im Commercial Courts Deutschland. |
| `glossary-commercial-court-de-en` | Erstellt ein DE/EN-Glossar für Commercial-Court-Mandate: ZPO-Begriffe, Anträge, Beweis, Tenor, Vergleich, Rechtsmittel und falsche Freunde im Commercial Courts Deutschland. |
| `governing-law-hearing-script` | Prüft anwendbares Recht: Rom I/Rom II, Rechtswahl, Eingriffsnormen, UN-Kaufrecht, Beweis fremden Rechts und Übersetzung der Normbegriffe im Commercial Courts Deutschland. |
| `hearing-script-english-advocacy` | Erstellt englische Hearing Scripts für deutsche Anwälte: opening, issue roadmap, witness questions, judicial questions, closing and settlement signals im Commercial Courts Deutschland. |
| `interim-relief-issues-list` | Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sicherheitsleistung und Vollziehung im Commercial Courts Deutschland. |
| `issues-list-and-roadmap` | Formuliert eine Issues List für Commercial-Court-Verfahren: legal issues, factual issues, evidence issues, quantum, jurisdiction and language im Commercial Courts Deutschland. |
| `judgment-publication-jurisdiction-clause` | Prüft Urteil, Veröffentlichung, Anonymisierung, Geheimnisschutz, Übersetzungsbedarf und externe Kommunikation nach Entscheidung im Commercial Courts Deutschland. |
| `jurisdiction-clause-drafting-de-en` | Entwirft deutsch-englische Commercial-Court-Gerichtsstands- und Sprachklauseln für Verträge, AGB-nahe Konstellationen und M&A/Finance-Deals im Commercial Courts Deutschland. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting für Commercial-Courts-Verfahren in Deutschland; erkennt Forum, Sprache, Streitwert, Parteivereinbarung, Case Management, Geheimnisschutz, Beweis, Transcript, Rechtsmittel und englischen Outputbedarf. |
| `klageschrift-english-limitation-tolling` | Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes of action, relief sought, evidence und exhibits im Commercial Courts Deutschland. |
| `late-submissions-296-zpo` | Steuert verspätetes Vorbringen, Präklusion, Fristverlängerung, gerichtliche Hinweise und Schriftsatznachlass im Commercial Courts Deutschland. |
| `limitation-and-tolling-check` | Prüft Verjährung, Hemmung, Standstill, Klageerhebung, Zustellung demnächst und internationale Limitation Issues im Commercial Courts Deutschland. |
| `local-rules-mediation-settlement` | Erstellt Live-Check zu Landesrecht, Geschäftsverteilung, Commercial-Court-Guidelines und Gerichts-Webseite vor jeder Einreichung im Commercial Courts Deutschland. |
| `mediation-settlement-window` | Findet Vergleichsfenster, Mediation, judicial settlement signals und Prozessvergleichsstrategie in Commercial-Court-Verfahren im Commercial Courts Deutschland. |
| `post-ma-pre-litigation` | Bearbeitet Post-M&A Warranty Claims vor Commercial Courts: notice, knowledge qualifiers, baskets, caps, leakage, earn-out, accounts and expert determination im Commercial Courts Deutschland. |
| `pre-litigation-notice-and-standstill` | Bereitet Pre-Action Letter, Standstill Agreement und Verjährungshemmung vor, wenn ein Commercial-Court-Verfahren droht im Commercial Courts Deutschland. |
| `procedural-calendar-protective-measures` | Erstellt einen prozessualen Verfahrenskalender mit Schriftsatzfristen, Anlagen, Übersetzungen, Witness Statements, Sachverständigen und Hearing Date im Commercial Courts Deutschland. |
| `protective-measures-confidential-exhibits` | Plant Schutzmaßnahmen für vertrauliche Anlagen: redactions, confidentiality club, restricted access, sealed bundles und Verhandlungsorganisation im Commercial Courts Deutschland. |
| `public-hearing-appeal-revision` | Steuert Öffentlichkeit, Presse, Public Relations und sensitive Unternehmenskommunikation bei hochkarätigen Commercial-Court-Verfahren im Commercial Courts Deutschland. |
| `redteam-commercial-court-qualitygate` | Red-Team-Gate für alle Commercial-Court-Outputs: Zuständigkeit, Sprache, Fristen, Beweise, Übersetzungen, Geheimnisschutz, Kosten, Rechtsmittel. |
| `ruegelose-einlassung-service-abroad` | Warnt vor rügeloser Einlassung: Zuständigkeit, Sprache, Einlassungsfrist, Verteidigungsanzeige, Prozessstrategie und Mandantenfreigabe im Commercial Courts Deutschland. |
| `service-abroad-hague-eu` | Plant Zustellung ins Ausland: EuZVO, Haager Zustellungsübereinkommen, Übersetzung, service agents, Fristen und Nachweis im Commercial Courts Deutschland. |
| `settlement-court-shareholder-board` | Bereitet gerichtlichen Vergleich, settlement agreement, consent order, Vollstreckbarkeit und mehrsprachige Vergleichsdokumentation vor im Commercial Courts Deutschland. |
| `shareholder-board-dispute` | Bearbeitet Gesellschafter-, Organ- und Joint-Venture-Streitigkeiten mit englischen Vertragsunterlagen vor deutschen Commercial Courts im Commercial Courts Deutschland. |
| `supply-chain-third-party` | Routet Lieferketten-, Vertrieb- und CISG-nahe Streitigkeiten: delivery, defects, force majeure, limitation, governing law and evidence im Commercial Courts Deutschland. |
| `third-party-notice-607-zpo` | Prüft Streitverkündung, Nebenintervention und Drittbeteiligung bei englischsprachigen Commercial-Court-Verfahren im Commercial Courts Deutschland. |
| `verbatim-transcript-video-hearing` | Plant das Wortprotokoll/verbatim transcript: Antrag, Kosten, Verhandlungsstrategie, Korrektur, Zitierfähigkeit und Nutzung im Rechtsmittel im Commercial Courts Deutschland. |
| `video-hearing-128a-284-zpo` | Prüft Videoverhandlung, hybride Beweisaufnahme, ausländische Zeugen, Techniktest und Protokollierung im Commercial Courts Deutschland. |
| `witness-preparation-zustandigkeit-119b` | Bereitet Zeugen in englischsprachigen deutschen Verfahren vor: Wahrheitspflicht, keine Coaching-Grenzüberschreitung, Sprachsicherheit, Dokumente, Ablauf im Commercial Courts Deutschland. |
| `zustandigkeit-119b-gvg-check` | Prüft, ob Commercial Court oder Commercial Chamber eröffnet ist: Wirtschaftsstreitigkeit, Streitwert, Parteivereinbarung, Landesrecht, OLG/LG, internationale Zuständigkeit und Rügefragen im Commercial Courts Deutschland. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
