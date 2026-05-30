# Common-Law-Kompass für deutsche Wirtschaftsjuristen

Großes, freistehendes Plugin für deutsche Anwältinnen und Anwälte im Wirtschaftsrecht, die mit Common Law, English Law, US Law, internationalen Verträgen, bilingualen Fassungen und gemischtem Business-English arbeiten. Es verhindert, dass deutsche Rechtsbegriffe gedankenlos übersetzt werden, und markiert typische False Friends wie Bürgschaft, Garantie, Gewährleistung, Rücktritt, Vertretung, Consideration, representations, warranties, covenants, indemnity, damages, equity oder discovery.

Dieses Plugin ist **vollständig freistehend**. Es benötigt keine anderen Plugins, keine externen Agenten und keine Kanzleisoftware. Wenn keine Datenbank, kein DMS, kein Übersetzungstool, keine Rechercheplattform oder kein Behördenzugang angeschlossen ist, arbeitet es mit manuellen Uploads oder einem ausdrücklich markierten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `common-law-kommandocenter` starten.
3. Rechtsordnung, Zieltext, Parteirolle, Verfahrensstand und gewünschtes Arbeitsprodukt nennen.
4. Vertragsauszug, Memo, Bescheid, Normtext, Redline, Übersetzung oder fiktive Simulationsakte hochladen.
5. Am Ende immer das Qualitätstor verlangen: Rechtsquelle, Jurisdiktion, Denkfehler, False Friends, offene Annahmen, Review-Level und nächster Schritt.

## Enthaltene Skills

- `common-law-kommandocenter` - Common-Law-Kommandocenter
- `common-law-false-friends-scanner` - False-Friends-Scanner
- `common-law-begriffe-uebersetzung` - Begriffs- und Übersetzungswerkstatt
- `common-law-governing-law-jurisdiction` - Governing Law, Jurisdiction und Forum
- `common-law-contract-formation-consideration` - Contract Formation und Consideration
- `common-law-surety-guarantee-indemnity` - Surety, Guarantee und Indemnity
- `common-law-representations-warranties-covenants` - Representations, Warranties und Covenants
- `common-law-remedies-damages-equity` - Remedies, Damages und Equity
- `common-law-interpretation-precedent` - Interpretation und Precedent
- `common-law-us-vs-uk-drafting` - UK vs US Drafting
- `common-law-ucc-sales-goods` - UCC und Sale of Goods
- `common-law-litigation-discovery` - Litigation, Discovery und Evidence
- `common-law-ma-commercial-drafting` - M&A und Commercial Drafting
- `common-law-bilingual-contract-review` - Bilingual Contract Review
- `common-law-client-explainer` - Mandanten-Erklärer
- `common-law-humor-coach` - Low-Key Late-Night Coach
- `common-law-quality-gate` - Common-Law-Qualitätstor
- `common-law-simulation-negotiation` - Simulation und Verhandlungstraining

## Vorlagen

- `assets/templates/bilingual-contract-review.md`
- `assets/templates/common-law-mandatskarte.md`
- `assets/templates/common-law-quality-gate.md`
- `assets/templates/consideration-check.md`
- `assets/templates/discovery-litigation-risk.md`
- `assets/templates/false-friends-matrix.md`
- `assets/templates/governing-law-jurisdiction-check.md`
- `assets/templates/ma-commercial-issue-list.md`
- `assets/templates/remedies-damages-map.md`
- `assets/templates/reps-warranties-covenants.md`
- `assets/templates/simulation-negotiation-playbook.md`
- `assets/templates/surety-guarantee-indemnity-map.md`
- `assets/templates/ucc-sales-check.md`
- `assets/templates/uk-us-drafting-styleguide.md`

## Offizielle Startquellen

- [UK Supreme Court](https://www.supremecourt.uk/)
- [Arnold v Britton, UKSC contract interpretation](https://www.supremecourt.uk/cases/uksc-2013-0193)
- [Wood v Capita, UKSC contract interpretation](https://www.supremecourt.uk/cases/uksc-2015-0212)
- [Contracts Rights of Third Parties Act 1999](https://www.legislation.gov.uk/ukpga/1999/31/contents)
- [Sale of Goods Act 1979](https://www.legislation.gov.uk/ukpga/1979/54/contents)
- [Unfair Contract Terms Act 1977](https://www.legislation.gov.uk/ukpga/1977/50/contents)
- [U.S. Courts: federal and state courts](https://www.uscourts.gov/about-federal-courts/court-role-and-structure/comparing-federal-state-courts)
- [Federal Rules of Civil Procedure](https://www.uscourts.gov/rules-policies/current-rules-practice-procedure/federal-rules-civil-procedure)
- [Uniform Law Commission: UCC](https://www.uniformlaws.org/acts/ucc)
- [U.S. Supreme Court](https://www.supremecourt.gov/)

## Download

- Plugin-ZIP: [common-law-kompass.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/common-law-kompass.zip)
- Akte: [testakte-common-law-kompass-crossborder-contract.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-common-law-kompass-crossborder-contract.zip)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 19 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Common Law Kompass-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `common-law-begriffe-uebersetzung` | Deutscher Anwalt uebersetzt Vertrags- oder Rechtsbegriffe ins Englische und will funktionale nicht wörtliche Übersetzung. Anwendungsfall Vertragsverhandlung mit UK/US-Gegenpartei Memo an englischsprachigen Mandanten. Prüfraster Zielrecht... |
| `common-law-bilingual-contract-review` | Anwalt prüft deutschen und englischen Vertragstext auf Bedeutungsdrift Rangfolge Definitionskonflikte Haftungsrisiken. Anwendungsfall bilingualer SPA NDA oder Lizenzvertrag. Prüfraster Bedeutungsdrift-Analyse Rangfolgen-Klausel Definitio... |
| `common-law-client-explainer` | Mandant oder Business-Team versteht Common-Law-Konzepte nicht und braucht verstaendliche Erklärung. Anwendungsfall Deutsche kaufen UK-Unternehmen oder schließen US-Vertrag ab. Prüfraster Verstaendlichkeit Vollständigkeit Wesentliche-Punk... |
| `common-law-contract-formation-consideration` | Anwalt oder Mandant will Vertragsschluss-Grundlagen des Common Law verstehen: offer acceptance consideration deed promissory estoppel UCC. Anwendungsfall Transaktionsvertrag oder NDA mit UK/US-Gegenpartei. Prüfraster Consideration-Prüfun... |
| `common-law-false-friends-scanner` | Anwalt oder Übersetzer sucht missverstaendliche deutsch-englische Rechtsbegriffe im Vertragstext oder Memo. Anwendungsfall Vertragsentwurf mit False-Friend-Risiko. Prüfraster Begriff-Scan Risikoeinstufung sichere Alternativen Jurisdiktio... |
| `common-law-governing-law-jurisdiction` | Vertragsparteien muessen Rechtswahlklausel Gerichtsstand und Durchsetzbarkeit für grenzüberschreitenden Vertrag klaeren. UK US oder deutsches Recht. Prüfraster Rechtswahl-Klausel Forum-Venue-Service Arbitrations-Option Vollstreckbarkeit... |
| `common-law-humor-coach` | Common-Law-Erklärungen sollen für Mandanten oder Team leichter lesbar werden ohne Praezision zu verlieren. Anwendungsfall Onboarding-Dokument oder Mandanten-Erklärung. Prüfraster Verstaendlichkeit Ton-Angemessenheit Praezisions-Erhaltung... |
| `common-law-interpretation-precedent` | Deutscher Anwalt liest UK oder US-Gerichtsentscheidung und versteht Praezedenzfall-Logik nicht: ratio decidendi obiter dictum stare decisis Vertragsauslegung. Normen UK Supreme Court Rules US Federal Rules. Prüfraster Ratio-obiter-Unters... |
| `common-law-kommandocenter` | Kanzlei startet Common-Law- UK- US- oder bilinguales Drafting-Mandat und braucht strukturierten Einstieg. Jurisdiktionscheck False-Friends-Scan Arbeitsplan. Prüfraster Jurisdiktion-Identifikation Primaeranliegen-Erfassung Skill-Routing.... |
| `common-law-litigation-discovery` | Anwalt oder Mandant ist in UK/US-Gerichtsverfahren und will pleadings discovery disclosure depositions privilege evidence settlement verstehen. Prüfraster Verfahrensphasen-Überblick Privilege-Prüfung Discovery-Scope Settlement-Optionen.... |
| `common-law-ma-commercial-drafting` | Anwalt draftet oder prüft SPA APA NDA LOI Disclosure Schedules oder Commercial Agreement nach Common Law. Common-Law-Risikomatrix. Prüfraster Reps-Warranties-Covenants-Abgrenzung Boilerplate-Risiken Haftungsklauseln Jurisdiktion. Output... |
| `common-law-quality-gate` | Fertig erstelltes Common-Law-Arbeitsprodukt auf Qualitaet prüfen: Jurisdiktion Quellenstand False Friends UK/US-Trennung Review-Bedarf. Prüfraster Jurisdiktion-Konsistenz Normen-Aktualitaet False-Friends-Scan UK-US-Trennung. Output Quali... |
| `common-law-remedies-damages-equity` | Mandant erleidet Schaden aus UK/US-Vertrag oder Delikt und fragt nach Rechtsfolgen: damages specific performance injunction rescission restitution equitable relief punitive damages. Prüfraster Remedy-Auswahl Schadensmass Equity-Vorausset... |
| `common-law-representations-warranties-covenants` | Anwalt ordnet Klauseln in Common-Law-Transaktionsvertraegen ein: reps warranties covenants conditions undertakings indemnities. Anwendungsfall SPA NDA oder Commercial Agreement. Prüfraster Klausel-Typ-Zuordnung Haftungsfolgen Survical-Pe... |
| `common-law-simulation-negotiation` | Anwalt oder Mandant will UK/US-Vertragsverhandlung oder Mandantengespraech simulieren und False-Friends-Lernkurve absolvieren. Prüfraster Verhandlungs-Simulation Issue-List-Erstellung Mandanten-Erklärung. Output Simulations-Szenario Verh... |
| `common-law-surety-guarantee-indemnity` | Anwalt prüft Sicherheitenklausel und muss zwischen Buergschaft Garantie suretyship guarantee indemnity primary obligation accessory liability unterscheiden. Prüfraster Klausel-Typ-Identifikation Akzessorietaet Durchsetzbarkeit Regress. O... |
| `common-law-ucc-sales-goods` | Anwalt prüft Warenkaufvertrag nach UCC oder Sale of Goods Act: title risk warranties perfect tender remedies. Anwendungsfall US-Kaufvertrag oder UK-Warengeschäft. Prüfraster UCC Art. 2 Sale-of-Goods-Act-Prüfung Title-Risk-Transfer Warran... |
| `common-law-us-vs-uk-drafting` | Anwalt muss zwischen British English English Law US contract style Delaware/New York-Konventionen und Business-English unterscheiden. Anwendungsfall Vertrag für UK- oder US-Gegenpartei. Prüfraster Jurisdiction-Style-Matching Drafting-Kon... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
