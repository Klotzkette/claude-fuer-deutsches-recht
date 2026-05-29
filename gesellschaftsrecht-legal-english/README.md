# Didaktisiertes Gesellschaftsrecht Legal English

Didaktisches Plugin für die zweisprachige Gesellschaftsrechts- und Transaktionspraxis. Es erklärt nicht nur Begriffe, sondern führt Anfängerinnen, Anfänger und laterale Quereinsteiger durch echte Arbeitsprodukte: Cap Table, Term Sheet, Investment Agreement, Gesellschaftervereinbarung, Satzung, SPA, Due-Diligence-Report, Closing-Checkliste, Mandantenmemo und Partnerbriefing.

Der Leitgedanke: Deutsche Dogmatik bleibt der Anker, aber die Praxis spricht oft zweisprachig. Ein `Cap Table` ist nicht einfach eine Gesellschafterliste. `Liquidation Preference` ist nicht bloß Vorzugsrecht. `Drag-along` ist nicht nur Mitverkaufspflicht. Das Plugin erklärt jeweils:

- was der englische Begriff im Deal-Kontext meint,
- welche deutsche Struktur oder Norm danebensteht,
- wo die Übersetzung verführt oder falsch wird,
- welches Dokument betroffen ist,
- welche Rückfragen ein First-Year Associate stellen muss,
- welcher Output für Partner, Mandant, Notar, Register oder Gegenseite sinnvoll ist.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Gesellschaftsrecht Legal English (`gesellschaftsrecht-legal-english`) | [gesellschaftsrecht-legal-english.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht-legal-english.zip) |

## Testakte

| Testakte | Direkt-Download |
| --- | --- |
| **Frankfurt Startup Round Legal English** | [testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |

Die Testakte enthält eine fiktive Venture-Capital- und M&A-Vorbereitung mit Partnerauftrag, Cap Table, Term Sheet, Gesellschafterliste, SHA-Auszug, DD-Notizen, Mandantenfragen und einem bewusst nervösen Associate-Arbeitsstand. Sie ist inzwischen als kleiner Dealroom angelegt: Markdown-Unterlagen, ein Excel-Trainingsmodell, PDF-Scan, PDF-Cheatsheet, Email-Screenshot, WhatsApp-Screenshot und Whiteboard-Foto.

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
| `allgemein` | Einstieg, Erfahrungslevel, Deal-Kontext, Begriffsfeld und Spezialskills auswählen. |
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

**Schneller Begriffsschock:** `allgemein` -> `rookie-modus` -> `begriffskompass-intake` -> passender Spezialskill -> `partner-briefing-memo`.

**Unübersichtlicher Dealroom:** `allgemein` -> `lernpfad-dealroom-simulator` -> `anschauungsmaterial-multiformat-auswertung` -> passende Spezialskills -> `qualitaetsgate-corporate-legal-english`.

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

- erst `00` bis `03` für Einstieg und Term Sheet,
- dann `08` und `09` für Begriffsschulung und Anfängerfehler,
- dann `16` bis `23` für Multi-Format-Materialien wie WhatsApp, Excel, Scan, Screenshot und Whiteboard,
- zum Schluss `15` für Closing-Logik und Qualitätstor.
