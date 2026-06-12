# Didaktisches Gesellschaftsrecht — English Business Terms

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`gesellschaftsrecht-legal-english.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/gesellschaftsrecht-legal-english.md) (88 KB)
- Im Repo: [`testakten/megaprompts/gesellschaftsrecht-legal-english.md`](../testakten/megaprompts/gesellschaftsrecht-legal-english.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`gesellschaftsrecht-legal-english`) | [`gesellschaftsrecht-legal-english.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht-legal-english.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Akte Kometenfalter Systems GmbH — Series A Project Comet Moth** (`gesellschaftsrecht-legal-english-frankfurt-startup`) | [Gesamt-PDF lesen](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/gesamt-pdf/gesellschaftsrecht-legal-english-frankfurt-startup_gesamt.pdf) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |
| **Nebelstern Ventures - Berliner VC-Pipeline, Wandeldarlehen und Follow-on-Chaos** (`venture-capital-geber-nebelstern-portfolio-berlin`) | [Gesamt-PDF lesen](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/gesamt-pdf/venture-capital-geber-nebelstern-portfolio-berlin_gesamt.pdf) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Didaktisches Plugin für die zweisprachige Gesellschaftsrechts- und Transaktionspraxis. Es erklärt nicht nur Begriffe, sondern führt Anfängerinnen, Anfänger und laterale Quereinsteiger durch echte Arbeitsprodukte: Cap Table, Term Sheet, Investment Agreement, Gesellschaftervereinbarung, Satzung, SPA, Due-Diligence-Report, Closing-Checkliste, Mandantenmemo und Partnerbriefing.

Der Leitgedanke: Deutsche Dogmatik bleibt der Anker, aber die Praxis spricht oft zweisprachig. Ein `Cap Table` ist nicht einfach eine Gesellschafterliste. `Liquidation Preference` ist nicht bloß Vorzugsrecht. `Drag-along` ist nicht nur Mitverkaufspflicht. Das Plugin erklärt jeweils:

- was der englische Begriff im Deal-Kontext meint,
- welche deutsche Struktur oder Norm danebensteht,
- wo die Übersetzung verführt oder falsch wird,
- welches Dokument betroffen ist,
- welche Rückfragen ein First-Year Associate stellen muss,
- welcher Output für Partner, Mandant, Notar, Register oder Gegenseite sinnvoll ist.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `gesellschaftsrecht-legal-english.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `references/` enthalten.

## Arbeitsweise

Das Plugin arbeitet in drei Schichten:

| Schicht | Zweck |
| --- | --- |
| Begriff | Deutsch/Englisch dekodieren, False Friends markieren, dogmatische Nähe und Differenz erklären |
| Dokument | Begriff im konkreten Dokument verorten: Gesellschafterliste, Satzung, SHA, Term Sheet, SPA, DD-Report |
| Workflow | Aufgabe in ein anwaltliches Arbeitsprodukt übersetzen: Matrix, Memo, Markup-Hinweis, Rückfragenliste, Partnerbriefing |

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `gesellschaftsrecht-legal-english-allgemein` | Einstieg, Erfahrungslevel, Deal-Kontext, Begriffsfeld und Spezialskills auswählen. |
| `rookie-modus` | First-Year-Associate-Modus mit Kleinschritten, Rückfragen und Review-Gates. |
| `lernpfad-dealroom-simulator` | Führt Anfänger durch eine mehrteilige Transaktionsakte mit Materialinventar, Lernpfad, Übungen und Senior-Gates. |
| `anschauungsmaterial-multiformat-auswertung` | Wertet PDF, Scan, Screenshot, JPEG, Excel, Chat, Email und Dealroom-Fragmente als Quellen mit unterschiedlicher Verlässlichkeit aus. |
| `begriffskompass-intake` | Begriff, Dokument, Rechtsordnung, Parteirolle und Outputbedarf erfassen. |
| `cap-table-gesellschafterliste` | Cap Table gegen Gesellschafterliste, § 40 GmbHG und wirtschaftliche Beteiligung abgleichen. |
| `fully-diluted-esop-option-pool` | Fully diluted basis, ESOP/VSOP, Option Pool und Verwässerung erklären und rechnen. |
| `share-classes-vorzugsrechte` | Share classes, preferred/common shares und deutsche Umsetzung in GmbH/AG/Satzung einordnen. |
| `liquidation-preference-waterfall` | Liquidation Preference, participating/non-participating und Exit-Waterfall didaktisch aufbereiten. |
| `anti-dilution-protection` | Full ratchet, broad-based weighted average und deutsche Kapitalerhöhungsmechanik unterscheiden. |
| `vesting-leaver-cliff` | Vesting, Cliff, Good Leaver, Bad Leaver und Einziehung/Abtretung strukturieren. |
| `drag-tag-piggyback` | Drag-along, Tag-along und Piggyback Rights voneinander trennen. |
| `term-sheet-investment-agreement` | Term Sheet, Investment Agreement und rechtliche Bindungswirkung prüfen. |
| `sha-gesellschaftervereinbarung` | Shareholders Agreement, Pooling, Stimmbindung und Satzungsschnittstelle erklären. |
| `articles-association-satzung` | Articles of association, Satzung/Gesellschaftsvertrag und Registerfähigkeit abgleichen. |
| `governance-board-consent-matters` | Board, Advisory Board, Consent Matters und deutsche Organlogik übersetzen. |
| `protective-provisions-vetorechte` | Protective provisions, Reserved Matters, Veto und Sperrminorität praktisch prüfen. |
| `transfer-restrictions-vinkulierung` | Transfer restrictions, ROFR, ROFO, Lock-up und Vinkulierung trennen. |
| `exit-spa-closing-cp` | Exit, SPA, signing, closing, CPs und Closing Deliverables didaktisch erklären. |
| `earn-out-kaufpreismechanik` | Earn-out, Milestones, Leakage und Kaufpreisanpassung in deutscher Vertragslogik aufbereiten. |
| `reps-warranties-indemnities` | Representations, warranties, covenants und indemnities ohne deutsche Scheinsynonyme erklären. |
| `due-diligence-red-flag-report` | DD-Begriffe, Red-Flag-Report, Materiality und Quellenbelege in Anfängerlogik führen. |
| `financing-convertible-loan-safe` | Convertible Loan, SAFE, Wandeldarlehen und deutsche Notar-/Kapitalerhöhungsfragen erklären. |
| `financial-debt-net-debt-working-capital` | Financial Debt, Net Debt, Cash Free Debt Free und Working Capital in Kaufpreisformeln prüfen. |
| `upstream-security-financial-assistance` | Upstream Loan/Security/Guarantee und Kapitalerhaltung/Financial Assistance markieren. |
| `reasonable-efforts-covenants` | Best/reasonable efforts, undertakings und covenants nach deutschem Recht konkretisieren. |
| `deutsches-recht-englische-vertraege` | Englische Vertragssprache bei deutschem Recht, Gerichtssprache und Commercial Courts absichern. |
| `client-explainer-legal-english` | Mandantenfreundliche Erklärung ohne Kanzleijargon erstellen. |
| `partner-briefing-memo` | Kurzes Partnerbriefing mit Issue, Risiko, Vorschlag und Rückfragen schreiben. |
| `qualitaetsgate-corporate-legal-english` | Schlussprüfung: Übersetzung, Rechtsanker, Dokument, Zahlenlogik, Risiken und offene Annahmen. |

## Typische Workflows

**Schneller Begriffsschock:** `gesellschaftsrecht-legal-english-allgemein` -> `rookie-modus` -> `begriffskompass-intake` -> passender Spezialskill -> `partner-briefing-memo`.

**Unübersichtlicher Dealroom:** `gesellschaftsrecht-legal-english-allgemein` -> `lernpfad-dealroom-simulator` -> `anschauungsmaterial-multiformat-auswertung` -> passende Spezialskills -> `qualitaetsgate-corporate-legal-english`.

**Startup-Finanzierungsrunde:** `cap-table-gesellschafterliste` -> `fully-diluted-esop-option-pool` -> `liquidation-preference-waterfall` -> `anti-dilution-protection` -> `term-sheet-investment-agreement` -> `qualitaetsgate-corporate-legal-english`.

**M&A-Dokumente auf Englisch bei deutschem Recht:** `deutsches-recht-englische-vertraege` -> `reps-warranties-indemnities` -> `financial-debt-net-debt-working-capital` -> `exit-spa-closing-cp` -> `partner-briefing-memo`.

## Quellenhygiene

- Dieses Plugin verarbeitet keine Aufsätze, Rezensionen oder sonstige Materialien als zitierfähige Vorlage. Es darf keine externen Texte wörtlich übernehmen, keine Autorennamen oder Fundstellen als Autorität nennen und keine besondere Nähe zu einzelnen Veröffentlichungen behaupten.
- Keine Paywall-Literatur, keine Kommentarzitate und keine Blindzitate.
- Gesetzesanker aus amtlichen oder frei zugänglichen Quellen verwenden.
- Amtliche englische Übersetzungen deutscher Gesetze sind Hilfsmittel, nicht die verbindliche Fassung.
- Bei Rechtsprechung nur Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbare Quelle ausgeben.

## Demo-Material

Die Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` eignet sich für Live-Demos:

- erst `00` bis `03` für Einstieg, Deal-Personen, Cap Table und Term Sheet,
- dann `04` bis `06` für SHA/Satzung/Vesting, DD-Red-Flags und den Associate-Arbeitsstand,
- dann `10` bis `14` für Wandeldarlehen-Vorgeschichte, Investor-Counsel-Markup, Notar-Checkliste, Side Letter und Board-/Consent-Mapping,
- dann `16` und `18` bis `22` für die Multi-Format-Materialien (WhatsApp-Thread im Chatlook, Cap-Table-Excel samt PDF-Ausdruck, Notar-Memo, Whiteboard, Investor-Email- und WhatsApp-Screenshot) sowie `chats/` für Slack-Thread und WhatsApp je als eigenes Dokument,
- zum Schluss `15`, `24` und `25` für Closing-Checkliste, Agio-/Kapitalrücklage-Streitfrage und Mailbox-/Call-Fragmente.
- Für schnelle Vorführungen ohne Fragmentwechsel: `26-gesamtakte-kometenfalter-series-a.pdf`.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfaenger-verhandlung-vergleich-und-eskalation` | Anfaenger: Verhandlung, Vergleich und Eskalation im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `anschauungsmaterial-multiformat-auswertung` | Wertet Corporate-Legal-English-Unterlagen in mehreren Formaten aus: PDF, Scan, Screenshot, JPEG, Excel, Chat, Email, Notarvermerk, Cap Table und Dealroom-Fragmente im Gesellschaftsrecht Legal English. |
| `anti-dilution-articles-association` | Prüft Anti-Dilution-Klauseln, Full Ratchet, Weighted Average, Down Round, Bezugsrechte und deutsche Umsetzungsrisiken im Gesellschaftsrecht Legal English. |
| `articles-association-satzung` | Vergleicht Articles of Association mit Satzung und Gesellschaftsvertrag, prüft Registerfaehigkeit, Pflichtinhalt, Nebenabreden und englische Fassungen im Gesellschaftsrecht Legal English. |
| `begriffskompass-intake-bgb-at` | Erfasst einen Corporate-English-Begriff mit Dokument, Rechtsordnung, Parteirolle, deutscher Naeherung, False-Friend-Risiko und gewuenschtem Arbeitsprodukt im Gesellschaftsrecht Legal English. |
| `bgb-at-schuldrecht-at-im-ma` | Macht sichtbar, wo BGB AT und Schuldrecht AT in englischsprachigen M&A-, Finanzierungs- und SHA-Vertraegen unter deutschem Recht stillschweigend mitlaufen: Form, Stellvertretung, Bedingungen, Verfuegungsverbote, AGB-Kontrolle, Konkretisi... |
| `business-corporate` | Business: Dokumentenmatrix, Lückenliste und Nachforderung im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse u... |
| `cap-table-client-explainer` | Erklaert und prüft Cap Table, Gesellschafterliste, wirtschaftliche Beteiligung, Stammkapital, Geschäftsanteile, Verwässerung und Registerrealitaet im Gesellschaftsrecht Legal English. |
| `chronologie-fristen` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Gesellschaftsrecht Legal English. |
| `client-explainer-legal-english` | Erstellt mandantenfreundliche Erklaerungen von Corporate-Legal-English-Begriffen ohne Jargon, mit Beispielen, Risiken und naechsten Entscheidungen im Gesellschaftsrecht Legal English. |
| `corporate-behoerden-gericht-und-registerweg` | Corporate: Behörden-, Gerichts- oder Registerweg im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `dealroom-quellenkarte` | Dealroom Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `deutsches-englische-drag-tag` | Prüft englische Vertragssprache bei deutschem Recht, Gerichtssprache, Commercial Courts, Übersetzungsregeln, Auslegung und False Friends im Gesellschaftsrecht Legal English. |
| `didaktisches-gesellschafterliste` | Didaktisches: Erstprüfung, Rollenklärung und Mandatsziel im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse un... |
| `dokumente-intake` | Dokumentenintake für Gesellschaftsrecht in legal English: sortiert Articles of Association, Shareholders Agreement, Board Resolutions, prüft Datum, Absender, Frist und Beweiswert (Cap table, Board minutes); markiert Lücken; berücksichtig... |
| `drag-tag-piggyback` | Unterscheidet Drag-along, Tag-along und Piggyback Rights mit Triggern, Mehrheiten, Minderheitenschutz, Vollzug und deutscher Dokumentenlogik im Gesellschaftsrecht Legal English. |
| `due-diligence-earn-out` | Fuehrt durch Due Diligence, Red Flag Report, Legal Fact Book, Materiality, Disclosure Schedule, Q&A und quellenbelegte Findings im Gesellschaftsrecht Legal English. |
| `earn-out-kaufpreismechanik` | Fuehrt durch Earn-out, Milestones, Locked Box, Completion Accounts, Leakage, Kaufpreisanpassung und Streitmechanismen im Gesellschaftsrecht Legal English. |
| `einstieg-routing` | Einstieg, Triage und Routing für Gesellschaftsrecht in legal English: ordnet Rolle (Shareholders, Board of Directors, Investors), markiert Frist (UK confirmation statement annual), wählt Norm (UK Companies Act 2006, Delaware GCL, MBCA (U... |
| `english-anschauungsmaterial-multiformat` | English: Fristen, Form, Zuständigkeit und Rechtsweg im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und dir... |
| `exit-spa-financial-debt` | Erklaert Exit, SPA, signing, closing, Conditions Precedent, Long Stop Date, Closing Deliverables und Vollzugslogik bei Unternehmenstransaktionen im Gesellschaftsrecht Legal English. |
| `financial-debt-net-debt-working-capital` | Prüft Financial Debt, Net Debt, Cash Free Debt Free, Working Capital, Debt-like Items und Kaufpreisformel im M&A-Kontext im Gesellschaftsrecht Legal English. |
| `financing-convertible-fully-diluted` | Erklaert Convertible Loan, Wandeldarlehen, SAFE, Discount, Valuation Cap, MFN und deutsche Notar- und Kapitalerhoehungsfragen im Gesellschaftsrecht Legal English. |
| `fully-diluted-esop-option-pool` | Fuehrt durch fully diluted basis, ESOP, VSOP, Option Pool, Wandlungsrechte, Verwässerung und die Frage, welche Instrumente in die Berechnung gehoeren im Gesellschaftsrecht Legal English. |
| `gesellschafterliste-compliance-dokumentation-und-akte` | Gesellschafterliste: Compliance-Dokumentation und Aktenvermerk im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbre... |
| `gesellschaftsrecht-legal` | Gesellschaftsrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehl... |
| `governance-board-lernpfad-dealroom` | Erklaert Board, Advisory Board, Management Board, Supervisory Board, Consent Matters und deutsche Organlogik für GmbH, AG und Beirat im Gesellschaftsrecht Legal English. |
| `kaltstart-triage` | Einstieg für das Gesellschaftsrecht-Legal-English-Plugin: erkennt Begriffsschock, Deal-Kontext, Erfahrungslevel, Dokumenttyp und routet zu den passenden Corporate-English-Skills. |
| `legal-schriftsatz-brief-und-memo-bausteine` | Legal: Schriftsatz-, Brief- und Memo-Bausteine im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt n... |
| `lernpfad-dealroom-simulator` | Fuehrt Anfaenger durch eine Corporate-Legal-English-Testakte mit Lernpfad, Dealroom-Inventar, Uebungen, Loesungsrichtung, Senior-Gates und konkreten Arbeitsprodukten im Gesellschaftsrecht Legal English. |
| `liquidation-preference-partner-briefing` | Erklaert Liquidation Preference, participating preference, non-participating preference, Exit-Waterfall, Rangfolge und wirtschaftliche Verteilungswirkung im Gesellschaftsrecht Legal English. |
| `output-waehlen` | Output-Wahl für Gesellschaftsrecht in legal English: stimmt Adressat (Shareholders, Board of Directors, Investors), Frist (UK confirmation statement annual) und Form auf den Zweck ab — typische Outputs: Memo English, SPA-Markup, Drag-Alo... |
| `partner-briefing-memo` | Schreibt ein knappes Partnerbriefing zu Corporate-English-Fragen mit Issue, Rechtsanker, wirtschaftlicher Wirkung, Empfehlung und Rueckfragen im Gesellschaftsrecht Legal English. |
| `protective-provisions-qualitaetsgate` | Prüft Protective Provisions, Reserved Matters, Vetorechte, Zustimmungsvorbehalte, Sperrminoritaeten und Blockaderisiken in Corporate-Dokumenten im Gesellschaftsrecht Legal English. |
| `qualitaetsgate-corporate-legal-english` | Schlusspruefung für Corporate Legal English: Begriff, deutsche Naeherung, Dokument, Rechtsanker, Zahlenlogik, Parteiinteresse und offene Annahmen im Gesellschaftsrecht Legal English. |
| `reasonable-efforts-reps-warranties` | Erklaert reasonable efforts, best efforts, commercially reasonable efforts, covenants, undertakings und konkretisiert sie für deutsches Recht im Gesellschaftsrecht Legal English. |
| `reps-warranties-indemnities` | Erklaert Representations, Warranties, Covenants, Indemnities, Disclosure, Knowledge Qualifiers und deutsche Haftungslogik im SPA im Gesellschaftsrecht Legal English. |
| `rookie-modus-sha-gesellschaftervereinbarung` | First-Year-Associate-Modus für Corporate Legal English: fuehrt Schritt für Schritt durch unbekannte Begriffe, Deal-Dokumente, Rueckfragen und Senior-Review-Gates im Gesellschaftsrecht Legal English. |
| `sha-gesellschaftervereinbarung` | Erklaert Shareholders Agreement, Gesellschaftervereinbarung, Stimmbindung, Pooling, Satzungsschnittstelle, Nebenabreden und Vollzug im Gesellschaftsrecht Legal English. |
| `share-classes-anfaenger` | Erklaert share classes, preferred shares, common shares, Vorzugsrechte, Sonderrechte und deutsche Umsetzungsfragen bei GmbH und AG im Gesellschaftsrecht Legal English. |
| `table-term-interessen` | Table: Zahlen, Schwellenwerte und Berechnung im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `term-mehrparteien-konflikt-und-interessen` | Term: Mehrparteienkonflikt und Interessenmatrix im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt... |
| `term-sheet-investment-agreement` | Fuehrt durch Term Sheet, Investment Agreement, Bindungswirkung, Conditions, Exclusivity, Confidentiality, Kosten und deutsche Vollzugsmechanik im Gesellschaftsrecht Legal English. |
| `terms-term-sheet` | Terms: Risikoampel, Gegenargumente und Verteidigungslinien im Corporate Legal English: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/VC-Terms), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse... |
| `transfer-restrictions-upstream-security` | Erklaert Transfer Restrictions, Vinkulierung, ROFR, ROFO, Lock-up, Permitted Transfers und Vollzug bei deutschen Anteilen im Gesellschaftsrecht Legal English. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Gesellschaftsrecht in legal English: trennt fehlende Tatsachen von fehlenden Belegen (Articles of Association, Shareholders Agreement, Board Resolutions), nennt pro Lücke Beweisthema, Beschaffungsweg (UK... |
| `upstream-security-financial-assistance` | Markiert Upstream Loan, Upstream Security, Upstream Guarantee, Financial Assistance, Kapitalerhaltung, Corporate Benefit und Organpflichten im Gesellschaftsrecht Legal English. |
| `verdeckte-sacheinlage-vesting-leaver` | Erkennt und prüft verdeckte Sacheinlage und Hin-und-Her-Zahlung nach § 19 Abs. 4 und Abs. 5 GmbHG, einschließlich Anrechnungsloesung, Vorbelastungshaftung und der typischen M&A-Fallen bei Cash-Capitalization, Wandeldarlehen, Verrechnung... |
| `vesting-leaver-cliff` | Erklaert Vesting, Cliff, Good Leaver, Bad Leaver, Founder Lock-up, Call Options, Einziehung und Rückübertragung im deutschen Gesellschaftsrecht im Gesellschaftsrecht Legal English. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Gesellschaftsrecht Legal English. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
