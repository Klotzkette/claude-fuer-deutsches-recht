# Didaktisches Gesellschaftsrecht — English Business Terms

<!-- BEGIN plugin-sofort-download-section (autogen) -->
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

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anti-dilution-articles-association` | Anti Dilution Protection, Articles Association Satzung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `begriffskompass-intake-bgb-at` | Begriffskompass Intake, Bgb At Schuldrecht At Im Ma: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `business-corporate` | Business Dokumentenmatrix Und Lueckenliste, Corporate Behörden Gericht Und Registerweg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `cap-table-client-explainer` | Cap Table Gesellschafterliste, Client Explainer Legal English: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `dealroom-quellenkarte` | Dealroom Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `deutsches-englische-drag-tag` | Deutsches Recht Englische Vertraege, Drag Tag Piggyback: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `didaktisches-gesellschafterliste` | Didaktisches Erstpruefung Und Mandatsziel, Gesellschafterliste Compliance Dokumentation Und Akte: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `due-diligence-earn-out` | Due Diligence Red Flag Report, Earn Out Kaufpreismechanik: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `english-anschauungsmaterial-multiformat` | English Fristen Form Und Zustaendigkeit, Anschauungsmaterial Multiformat Auswertung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `exit-spa-financial-debt` | Exit Spa Closing Cp, Financial Debt Net Debt Working Capital: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `financing-convertible-fully-diluted` | Financing Convertible Loan Safe, Fully Diluted Esop Option Pool: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `gesellschaftsrecht-legal` | Gesellschaftsrecht Tatbestand Beweis Und Belege, Legal Schriftsatz Brief Und Memo Bausteine: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `gesellschaftsrecht-legal-english-chronologie-fristen` | Chronologie Und Belegmatrix, Fristen Und Risikoampel: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `gesellschaftsrecht-legal-english-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `gesellschaftsrecht-legal-english-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `gesellschaftsrecht-legal-english-kaltstart-triage` | Einstieg fuer das Gesellschaftsrecht-Legal-English-Plugin: erkennt Begriffsschock, Deal-Kontext, Erfahrungslevel, Dokumenttyp und routet zu den passenden Corporate-English-Skills. |
| `gesellschaftsrecht-legal-english-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `gesellschaftsrecht-legal-english-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `governance-board-lernpfad-dealroom` | Governance Board Consent Matters, Lernpfad Dealroom Simulator: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `liquidation-preference-partner-briefing` | Liquidation Preference Waterfall, Partner Briefing Memo: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `protective-provisions-qualitaetsgate` | Protective Provisions Vetorechte, Qualitaetsgate Corporate Legal English: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `reasonable-efforts-reps-warranties` | Reasonable Efforts Covenants, Reps Warranties Indemnities: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `rookie-modus-sha-gesellschaftervereinbarung` | Rookie Modus, Sha Gesellschaftervereinbarung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `share-classes-anfaenger` | Share Classes Vorzugsrechte, Anfaenger Verhandlung Vergleich Und Eskalation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `table-term-interessen` | Table Zahlen Schwellen Und Berechnung, Term Mehrparteien Konflikt Und Interessen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `terms-term-sheet` | Terms Risikoampel Und Gegenargumente, Term Sheet Investment Agreement: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `transfer-restrictions-upstream-security` | Transfer Restrictions Vinkulierung, Upstream Security Financial Assistance: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `verdeckte-sacheinlage-vesting-leaver` | Verdeckte Sacheinlage, Vesting Leaver Cliff: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
