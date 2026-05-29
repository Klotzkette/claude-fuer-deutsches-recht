# v47.1.0 — Plugin gesellschaftsrecht-legal-english: zwei neue Grundlagen-Skills

Reaktion auf den Hinweis aus der Praxis (LinkedIn-Diskussion vom 29.05.2026), dass M&A-Anwaelte regelmaessig Basics aus BGB AT, Schuldrecht AT und Kapitalaufbringungsrecht uebersehen, weil sie M&A fuer reines Vertragsrecht halten. Gerade in Zeiten breiter KI-Nutzung bleibt das Grundlagenwissen entscheidend, damit Ergebnisse richtig interpretiert werden.

Zwei neue Skills im Plugin `gesellschaftsrecht-legal-english`:

- **`verdeckte-sacheinlage`**: erkennt und prueft verdeckte Sacheinlage und Hin-und-Her-Zahlung nach § 19 Abs. 4 und Abs. 5 GmbHG. Anrechnungsloesung seit MoMiG, Vorbelastungshaftung, Pruefraster mit sieben Schritten, typische M&A-Fallen (Cash-In-Series-A plus Akquisition, Wandeldarlehen, Verrechnungsabreden, Sale-and-lease-back, Beraterhonorar an Investor), klare Heilungswege.
- **`bgb-at-schuldrecht-at-im-ma`**: macht sichtbar, wo BGB AT und Schuldrecht AT in englischsprachigen M&A-, Finanzierungs- und SHA-Vertraegen unter deutschem Recht stillschweigend mitlaufen. Zehnstufiges Pruefraster: Form und Einheitstheorie § 15 Abs. 4 GmbHG, Stellvertretung §§ 164 ff. und § 181 BGB, Bedingungseintritt und -vereitelung § 162 BGB, AGB-Kontrolle §§ 305 ff. und § 307 BGB auch im B2B, Treu und Glauben § 242 BGB fuer reasonable-/best-efforts, Anfechtung §§ 119, 123 BGB und Sperre des § 444 BGB. Konkrete Falleinordnungen mit Heilungswegen.

Beide Skills sind in der Fuehrungsmatrix des `allgemein`-Routing-Skills erfasst, damit Nutzer mit Aussagen wie "Wir machen Vertragsrecht, BGB AT ist egal" oder "Bareinlage und gleichzeitig Erwerb vom Gesellschafter" direkt auf die richtige Stelle geroutet werden.

## Plugin-Version

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `47.1.0` gebumpt (Skill-Anzahl von 30 auf 32). Description und Slug unveraendert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v47.0.0 — Schlussrunde Testakten, Übersichten und quellenfeste Schriftformakte

Große Abschlussrunde über den Akten- und Release-Bestand:

- Alle Testakten-READMEs von sichtbaren Test-/Lehr-/Fiktionsmarkern bereinigt und auf Aktenlogik, Direkt-Downloads und menschliche Umlaute geglättet.
- Schmalfeld-Betreuungsakte um `09_vertragsauszuege_pruefmappe.md` erweitert: Alltagsverträge, Fernwartungs-/Sicherheitssoftware, Hochrisikoanlagen, Spanien-Reservierung, Haustürvertrieb, Beleglücken und priorisierte Maßnahmen.
- Schriftform-Maklerakte Haspelbeck von einem nicht verifizierten BGH-Scheinzitat bereinigt: fake BGH-PDF entfernt, PDFs neu ohne Erzeugungsfußzeilen gebaut, Excel/Markdown-Vorschau auf offene Rechtsprechungsprüfung umgestellt.
- VerkehrsOWi-Akte von konstruierten OLG-Fundstellen bereinigt und in eine quellenfeste Rechtsprechungsrecherche mit Arbeitsmatrix umgebaut.
- Sichtbare Unterrichts-/Muster-Slugs in mehreren Akten entschärft: LUMEN Studios, Strafbefehl, VerkehrsOWi, Solis Vision X, Sozialrecht Tannenberg und Roeschen Tech laufen nun als Arbeits-, Prüf- oder Fallkonferenzakten.
- `SKILLS.md` neu aus dem tatsächlichen Bestand generiert: 2.553 Skill-Links in 105 Plugins, inklusive der bisher fehlenden Agio-/Kapitalrücklage-Skills.
- Plugin-/Testakten-Übersichten aktualisiert; `gesellschaftsrecht` und `grosskanzlei-corporate-ma` verlinken nun auch die Corporate-Legal-English-Frankfurt-Akte.
- README, Testaktenübersicht und Asset-Index auf `v47.0.0` nachgezogen; Sammel-Downloads `alle-plugins-megazip.zip` und `alle-testakten.zip` bleiben sichtbar.

---

# v46.0.0 — Corporate-Legal-English-Akte: Gesamt-PDF und Cap-Table-Abgleich

Nachlauf für `gesellschaftsrecht-legal-english` und die Frankfurt-Startup-Akte:

- `18-cap-table-und-waterfall.xlsx` auf den Aktenstand aus Datei 02 gebracht: Kunigunde/Meinhard/Walburga, 900 VSOP, 5.000 Pool, 6.700 Convertible, 16.679 Northbridge- und 1.390 Krämer-Angel-Anteile.
- `18-cap-table-und-waterfall.pdf` als PDF-Ausdruck des Excel-Arbeitsmodells ergänzt.
- `26-gesamtakte-kometenfalter-series-a.pdf` als 64-seitige zusammengeführte Lesefassung der Aktenbestandteile ergänzt, inklusive Excel-Ausdruck, Bildfragmenten und E-Mail-Anhang.
- WhatsApp-PDF im Chatlook neu erzeugt; die Bildfragmente 20 bis 22 von Rookie-/Lernhinweisen bereinigt.
- README-Dateien, Marketplace und Plugin-Manifest für `gesellschaftsrecht-legal-english` aktualisiert; Plugin-Version jetzt `46.0.0`.

---

# v45.0.0 — Sammel-ZIPs für Plugins und Testakten

Release-Infrastruktur und Übersichten nachgezogen:

- `.github/workflows/release-plugin-zips.yml` baut zusätzlich `alle-plugins-megazip.zip` mit allen installierbaren Plugin-ZIPs plus `marketplace.json`.
- Der Workflow baut zusätzlich `alle-testakten.zip` mit allen Testaktenordnern in Originalstruktur.
- `README.md`, `testakten/README.md` und `ASSET_INDEX.md` zeigen die Sammel-Downloads sichtbar an.
- Erwarteter Release-Umfang: 105 Plugin-ZIPs, 63 Testakten-ZIPs, `marketplace.json` und 2 Sammelarchive, also 171 Assets.

---

# v44.0.1 — Akte: Excel entlehrmaterialisiert, gemischte PDFs nach Kanaltyp getrennt

Folgefix nach v44.0.0. Drei Dinge:

## Excel

- `18-cap-table-waterfall-training.xlsx` → ersetzt durch `18-cap-table-und-waterfall.xlsx`.
- Workbook-Titel: "Cap Table und Waterfall — Series A Project Comet Moth" (statt "Corporate Legal English Training Workbook").
- Sheets neu: Übersicht, Cap Table, Pool-Szenarien, Wandeldarlehen, Waterfall. Sheet "Rookie Quiz" geloescht, Sheet "README" als "Übersicht" mit Mandantin / Aktenzeichen / Sachbearbeitung / Stand neu aufgesetzt.
- Alle "Lernziel", "Didaktischer Hinweis", "fiktive Testakte", "Training Workbook", "didaktisch", "Rookie"-Markierungen entfernt.

## PDF-Trennung nach Kanaltyp

- `01-partnerauftrag-email.md` enthielt zwei E-Mails plus einen Slack-Thread im selben PDF. Aufgeteilt: `01-partnerauftrag-emails.md` (nur die zwei E-Mails) plus `chats/01-slack-comet-moth-cap-table.md` (Slack) jeweils als eigenes DOCX und PDF.
- `11-investor-counsel-markup-roundtrip.md` enthielt drei E-Mails plus eine Randnotiz Westarp. Aufgeteilt: `11-investor-counsel-markup-emails.md` (nur die drei E-Mails) plus `11n-westarp-randnotiz-zum-entwurf.md` (Randnotiz) jeweils als eigenes DOCX und PDF.
- `chats/16-whatsapp-partner-associate-thread.md` jetzt auch als eigenes DOCX und PDF (zusaetzlich zum bereits separat existierenden Datei-16-PDF im Wurzelverzeichnis).

## Restliche Textentlehrungen

- `00-deal-personen-und-zeitleiste.md`: Abschnitt "Was die Akte testet" umbenannt in "Aktenschwerpunkte fuer die kommende Verhandlung", inhaltlich auf das Mandat statt auf den Lernzweck formuliert.
- `06-associate-arbeitsstand.md`: Lead-Absatz von "dem Nachwuchs zeigen, wie eine Partnerin Anfaengertexte umarbeitet — sachlich, hart, lehrreich" auf "Adelheid von Westarp hat am 21.05.2026 vormittags Anmerkungen am Rand vermerkt" geaendert.
- `14-board-und-consent-matters-mapping-de-en.md`: Abschnitt "Lernziel" in "Ausgangspunkt" umbenannt.
- `chats/01-slack-comet-moth-cap-table.md`: Kopfblock "Auszug aus dem internen Slack-Channel" durch realistische Channel-/Teilnehmer-/Zeitstempel-Angaben ersetzt.

## Konsequenzen fuer README und Plugin-README

- Testakten-`README.md`: Aktenbestand-Tabelle aktualisiert (neue Dateinamen `01-partnerauftrag-emails`, `11-investor-counsel-markup-emails`, `11n-westarp-randnotiz-zum-entwurf`, `18-cap-table-und-waterfall.xlsx`). Hinweise auf chats/DOCX/PDF ergaenzt.
- Plugin-`README.md`: Excel-Dateiname aktualisiert; Demo-Material-Sektion um chats/ ergaenzt.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Volltextsuche `lehr|fiktiv|didakt|training|quiz|rookie|lernziel|simul|cheatsheet|musterloesung` ueber alle PDFs/DOCX/XLSX — 0 echte Treffer (nur juristischer Fachbegriff "Zweckuebertragungslehre" verbleibt).

---

# v44.0.0 — Testakte Frankfurt-Startup entlehrmaterialisiert: echte Akte statt Lehrkompendium

Die Frankfurt-Startup-Testakte wird zu einer realistischen Mandatsakte umgebaut. Alle didaktischen Marker ("fiktive Lehrakte", "Aehnlichkeiten zu realen Transaktionen sind nicht beabsichtigt", "Lehrmaterial") sowie alle formalen Lehrhilfen (Cheat-Sheets, Glossare, Fehlerkataloge, Index-Beipackzettel) sind entfernt. Was bleibt, ist das bluehende Leben einer Series-A-Mandatsakte der Kanzlei Hagemann & Westarp fuer die Kometenfalter Systems GmbH.

## Entlehrmaterialisierung

- Fuenf formale Lehrdateien geloescht (jeweils `.md` + `.docx` + `.pdf`): `07-erwarteter-output`, `08-glossar-english-deutsch`, `09-anfaengerfehler-katalog`, `17-anschauungsmaterial-index`, `23-rookie-cheatsheet`.
- In den verbleibenden 15 Markdown-Dateien alle Disclaimer-Zeilen entfernt ("Fiktive Lehrakte", "Aehnlichkeit zu realen Transaktionen", "Lehrmaterial", "Didaktischer Hinweis", "Simuliert wird").
- ASCII-Umlaute systematisch gefixt: `Aehnlichkeiten` → `Ähnlichkeiten`, `Uebersetzung` → `Übersetzung`, `fuer` → `für` (kontextabhaengig), `dass` korrekt, `ß` durchgaengig.
- E-Mail-Adressen entfiktivisiert: `[mailto fiktiv ...]` → echte Kanzlei-Domains (`@hagemann-westarp.de`, `@brackenmuir-quint.de`); "Fiktive Adresse:" → echte Anschrift.
- `README.md` der Testakte komplett neu als Akten-Deckblatt der Kanzlei (Mandantin, Az., Sachbearbeitung, Aktenbestand).

## Re-Rendering

- Alle verbleibenden 16 Markdown-Dateien (15 Sachdateien + `README.md`) sowie das Notar-Memo 19 neu als `.docx` und `.pdf` gerendert (17 DOCX + 17 PDF).
- Footer: `Vertraulich · Akteninterne Bearbeitungsfassung` (statt v43-Footer `Lehrmaterial Didaktisches Gesellschaftsrecht`).
- Nummerierte Listen werden jetzt korrekt als `1.`/`2.`/`3.` gerendert (war v43-Bug — alle Eintraege erschienen als `1.`).
- Notar-Memo 19 (`19-notar-scan-beurkundungssprache`) neu als realistisches Memorandum aus dem Notariat Veitschegger mit Briefkopf, Az. UR-Nr. 1182/2026, ohne didaktische Rahmung.
- EML-Dateien (`emails/11a`, `emails/11b`) korrigiert: echte Domains, korrekte Anschriften.

## Plugin-Version

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json` auf `44.0.0` gebumpt. `description` und Slug unveraendert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Volltextsuche `lehr|fiktiv|didakt|simuliert|aehnlich` in allen 17 PDFs, 17 DOCX, 5 EML, 2 Chat-MDs — 0 Treffer.
- PDF 19 (Notar-Memo) und PDF 11 (Investor-Counsel) visuell mit `pdftoppm` geprueft: Briefkopf korrekt, Nummerierung korrekt, kein Ueberlauf.

---

# v43.0.0 — Frankfurt-Startup-Testakte Big-Law-Rebuild + Plugin-Spotlight "Didaktisches Gesellschaftsrecht — English Business Terms"

Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` komplett neu gerendert und didaktisch erweitert; Plugin `gesellschaftsrecht-legal-english` (Slug unveraendert) tritt jetzt unter dem Titel "Didaktisches Gesellschaftsrecht — English Business Terms" auf.

## Testakte-Rebuild

- Alle 20 Textdateien + 2 didaktische Cheatsheets (19, 23) zusaetzlich als Big-Law-Memo gerendert: 22x `.docx` und 22x `.pdf` im Stil Times New Roman 11pt, Blocksatz, Seitenkopf (Mandantenname links / Dateilabel rechts), Seitenfuss (Vertraulichkeitshinweis links / "Seite X von Y" rechts), H1 zentriert, H2 nummeriert (13pt bold), H3 als (a)/(b) (11pt bold), Tabellen mit grauer Headerzeile und sauberem Umbruch.
- PDF 19 (Notar-Scan Beurkundungssprache § 16 BeurkG) und PDF 23 (Rookie Cheatsheet Corporate Legal English ↔ Deutsches Werkzeug) komplett neu aufgesetzt: kein Textueberlauf am rechten Rand mehr, keine Label-Kollision "Deutsches WerkzeugSatzung" mehr, Spaltenbreiten 22/38/40 % mit sauberem Zeilenumbruch.
- Fiktive E-Mails (2 aus Datei 01, 3 aus Datei 11) zusaetzlich als echte `.eml`-Dateien in `emails/` mit RFC-5322-Headern (Outlook-kompatibel).
- Slack-Thread `#project-comet-moth` (Mittwoch 22:14-22:58) als eigenstaendige Markdown in `chats/01-slack-comet-moth-cap-table.md` extrahiert.
- WhatsApp-Verlauf Partner/Associate (Donnerstag 06:58-08:21) vollstaendig in `chats/16-whatsapp-partner-associate-thread.md` gespiegelt (zusammenhaengender Thread, daher in Gaenze).

## Plugin-Spotlight

- `gesellschaftsrecht-legal-english/.claude-plugin/plugin.json`: `description` auf "Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English fuer Big-Law-Anfaenger…" umgestellt, `version` auf `43.0.0` gebumpt. Slug `gesellschaftsrecht-legal-english` BLEIBT (kein Rename).
- `gesellschaftsrecht-legal-english/README.md`: Titel auf "Didaktisches Gesellschaftsrecht — English Business Terms". Testakten-Beschreibung um DOCX/PDF/EML/Chats erweitert.
- `.claude-plugin/marketplace.json`: Eintrag fuer `gesellschaftsrecht-legal-english` an die neue description angepasst und auf `43.0.0` synchronisiert.

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- PDF 19/23 + Stichprobe PDF 11 visuell mit `pdftoppm` geprueft: kein Ueberlauf, Header/Footer/Seitenzaehler korrekt.

---

# v42.0.0 — README-Spotlight komplett entfernt

- "Ganz oben: Corporate Legal English"-Spotlight-Block aus README entfernt.
- README startet jetzt direkt mit "Über dieses Repository" nach der Titelzeile und dem Lead-Absatz.
- Keine Plugin-Aenderungen.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v41.0.0 — README-Spotlight: Corporate Legal English statt Meinungspruefer (Tag-Bump nach v40)

Reiner Tag-Bump: Der v40.0.0-Tag wurde bereits zuvor auf den Sanity-Release-Commit `51ade7ae` gesetzt. Da der README-Schnitt (Meinungspruefer-Hero raus, Corporate Legal English oben) danach folgte und Tags nicht ueberschrieben werden, wird der aktuelle `main` als `v41.0.0` markiert.

Inhaltlich identisch zum unten gepflegten v40-Eintrag (Sanity-Release + README-Spotlight). Keine Plugin-Aenderungen.

---

# v40.0.0 — Sanity-Check-Release nach v39 + README-Spotlight Corporate Legal English

Sammelrelease: Der aktuelle `main`-Stand nach `v38.0.0` (Steuerrechts-Sanity-Fix) und `v39.0.0` (CO2KostAufG-Präzisierung) wurde gegen die Repo-Validatoren und den Release-ZIP-Bau geprüft und als nächster stabiler Download-Stand markiert. Zusätzlich wurde das README-Spotlight redaktionell geändert.

## README-Spotlight

- Meinungspruefer-Block ganz oben aus README entfernt.
- Spotlight-Abschnitt umbenannt zu "Ganz oben: Corporate Legal English" und auf `gesellschaftsrecht-legal-english` mit Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` fokussiert (Kaltstart, Dealroom-Lernpfad, Cap Table, Gesellschafterliste, Term Sheet, SHA, Liquidation Preference, Anti-Dilution, Vesting, Drag/Tag, SPA/DD-Begriffe, englische Vertragssprache unter deutschem Recht).
- Keine Plugin-Aenderungen; rein redaktioneller README-Schnitt zusätzlich zum Sanity-Release.

## Qualitätssicherung

- `git diff --check` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-release-zips.py /tmp/codex-release-sanity .claude-plugin/marketplace.json` — OK
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Release-Asset-Sanity: 105 Plugin-ZIPs, 63 Testakten-ZIPs, 1 `marketplace.json`, insgesamt 169 Assets

## Dokumentation

- `README.md` und `ASSET_INDEX.md` auf `v40.0.0` aktualisiert.

---

# v39.0.0 — Codex-Round-5: CO2KostAufG-Praezisierung (§ 3-Pflichtangaben + § 8 Nichtwohngebaeude 2025)

Zwei Codex-Findings zur Testakte `testakten/weg-hausverwaltung-hohenzollernhof/11-co2kostaufg-aufteilungspruefung.md`:

## Findings

- **§ 3 vs. § 5/§ 7 — Primaerdaten von Berechnungsfeldern trennen.** Das Beanstandungsschreiben fuehrte `gebaeudespezifischer Wert in kg CO2/m2/a` und `Einstufung in die Anlage zu § 5` als angeblich vom Gaslieferanten nach § 3 CO2KostAufG zu uebermittelnde Angaben auf. Tatsaechlich kennt der Lieferant weder die relevante Wohnflaeche noch die resultierende § 5-Stufe; § 3 Abs. 1 Nr. 1-5 schuldet nur (1) Brennstoffemissionen in kg CO2, (2) CO2-Preisbestandteil in EUR, (3) heizwertbezogener Emissionsfaktor in kg CO2/kWh, (4) Energiegehalt in kWh, (5) Hinweis auf Erstattungsansprueche §§ 6 Abs. 2, 8 Abs. 2. `gebaeudespezifischer Wert` und `Einstufung` sind § 5/§ 7-Berechnungen des Vermieters. Klarstellung im Datenpflichten-Abschnitt, im Beanstandungsschreiben und im Hinweis fuer die Verwalterin eingebaut.
- **§ 8 CO2KostAufG — Stufenmodell fuer Nichtwohngebaeude 2025 noch nicht operativ.** Der frueher Abschnitt schrieb `ab 01.01.2025 auch Nichtwohngebaeude im Stufenmodell`. § 8 Abs. 4 sieht aber nur vor, dass die haelftige Aufteilung im Jahr 2025 abgeloest werden soll; ein operatives Stufenmodell fuer Nichtwohngebaeude ist im Gesetzestext noch nicht enthalten. Bis zur Einfuehrung der Tabelle gilt nach § 8 Abs. 1 weiterhin **50/50** (Vereinbarungen ueber mehr als 50 % Mieteranteil unwirksam). Korrigiert in der Anwendungsbereichs-Beschreibung und im Berechnungsabschnitt.

Quelle (verifiziert): https://www.gesetze-im-internet.de/co2kostaufg/__3.html, https://www.gesetze-im-internet.de/co2kostaufg/__8.html

## Plugin-Versionsbumps

- `weg-hausverwaltung` 37.0.0 → 38.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v38.0.0 — Sanity-Check Tax + Bug-Fix § 1 Abs. 3 GrEStG statt AO

Sanity-Check des Tax-Commits `4ab560c2` (16 neue GrESt- und Grundsteuer-Skills, zwei neue Testakten). Validatoren alle grün, Rechtsstand-Anker verifiziert (§ 6a GrEStG noch 95 %, BFH II B 13/25, II B 23/25, II B 47/25, BFH II R 25/24 zum Bundesmodell, BVerfG 1 BvL 11/14). Ein Bug gefunden und behoben.

## Bug-Fix

- **`anw-grunderwerbsteuer-share-deal-90-prozent` description**: Die YAML-`description` hatte den falschen Normverweis `§ 1 Abs. 3 AO` (Abgabenordnung) statt `§ 1 Abs. 3 GrEStG`. Im Body war die Norm korrekt zitiert; nur das Suchmetadatum-Feld war vertauscht. Korrigiert.

## Plugin-Versionsbumps

- `steuerrecht-anwalt-und-berater` 36.1.0 → 37.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Forbidden-Frontmatter-Check — leer

---

# v37.0.0 — Codex-Round-4-Fixes: CO2KostAufG-Datenpflichten richtig zuordnen

Drei Codex-Findings zur Testakte `11-co2kostaufg-aufteilungspruefung.md` aus dem v36-PR behoben:

- **Datenpflichten-Basis korrigiert**: `§ 2 Abs. 2 CO2KostAufG` war falsche Anspruchsgrundlage — § 2 regelt nur den Anwendungsbereich. Datenpflichten differenziert nach § 3 (Lieferanteninformation an den Bezieher = WEG/Verwalter), § 5 (Stufentabelle/Anlage), § 6 (Begrenzung Umlagefähigkeit/Erstattungsanspruch Mieter), § 7 Abs. 3 und 4 (Vermieter-Abrechnungspflicht gegenüber Mieter), § 8 (Nichtwohngebäude). Praxis-Klarstellung: die WEG-Jahresabrechnung muss die CO2-Datenfelder selbst **nicht** ausweisen; die Verwalterin muss die § 3-Lieferantendaten an die vermietenden Eigentümer **weiterreichen**, damit diese ihrer § 7-Pflicht nachkommen können.
- **Stufe-5-Anteile entreversed**: Das Beanstandungsschreiben hatte "60 % Vermieter / 40 % Mieter" — die Stufentabelle weist Stufe 5 (27–32 kg CO2/m2/a) korrekt mit **60 % Mieter / 40 % Vermieter** aus. Korrigiert.
- **Endempfehlung konsistent**: Der Schlussabschnitt "Hinweis fuer Verwalterin" empfahl noch die Anwendung des Stufenmodells in der WEG-Heizkostenabrechnung — widersprach der neuen WEG-Analyse. Korrigiert: WEG-interne Verteilung nach HeizkostenV (70/30) bleibt unverändert; Stufenmodell **nicht** in der WEG-Abrechnung; stattdessen separate Anlage "CO2-Lieferantendaten nach § 3 CO2KostAufG" zur Jahresabrechnung. Anfechtungs-Praxisempfehlung entsprechend nachgezogen.

## Plugin-Versionsbumps

- `weg-hausverwaltung` 36.0.0 → 37.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v36.1.0 - Steuerrecht Grundsteuer und Grunderwerbsteuer

- **16 neue Steuerrechts-Skills.** Acht Grundsteuer-Skills decken Kaltstart/Bescheidkette, Verfassungscheck, Ermittlungsbasis, BewG-Bewertung, Einspruch/AdV, Landesmodell-Routing, Hebesatz/Zahlung und gemeinen Wert/Gutachten ab. Acht GrESt-Skills decken Asset Deal, Share Deal, Signing/Closing-Doppelfestsetzung, § 19-Anzeige, SPA-Tax-Clause, § 6a-Konzernklausel und Bescheid/Einspruch/AdV/§ 16 GrEStG ab.
- **Faktenbank erweitert.** `rechtsstand-mai-2026-faktenbank` enthält jetzt die Grundsteuer-Anker BVerfG 10.04.2018, BFH-AdV 27.05.2024, BFH-Bundesmodell 12.11.2025, BFH-Baden-Württemberg-Stand Mai 2026, die gleich lautenden Ländererlasse vom 20.02.2026 zu Share Deals sowie die BFH-Signing/Closing-Beschlüsse II B 13/25, II B 23/25 und II B 47/25.
- **Zwei neue Testakten.** `grundsteuer-rosenwinkel-bescheidkette` führt durch Grundsteuerwert-, Mess- und Gemeindebescheid mit Flächenfehlern, Denkmalschutz, Leerstand und niedrigerem gemeinen Wert. `grunderwerbsteuer-sharedeal-closing-waldkrone` bildet eine Share-Deal-Closing-Akte mit drei Bundesländern, § 19-Anzeige, SPA-Steuerklausel, Escrow und Doppelbescheid-AdV ab.
- **Dokumentation und Metadaten.** Steuerrechts-README, Testakten-README, SKILLS-Übersicht, Asset-Index, Marketplace und Plugin-Manifest aktualisiert; `steuerrecht-anwalt-und-berater` auf `36.1.0` gesetzt.

## Qualitätssicherung

- `git diff --check`
- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- JSON-Manifest-Parse aller Plugin-Manifeste

---

# v36.0.0 — Codex-Round-3-Fixes: HeizkostenV-Bandbreite, § 18 vs. § 28 WEG, CO2KostAufG WEG-Grenzen, Gewährleistungs-Werkart, § 55a GmbHG, negatives Agio

Sechs Codex-Review-Findings aus dem v35-PR systematisch behoben:

- **HeizkostenV-Bandbreite korrekt formuliert** (`weg-hausverwaltung/skills/betriebskosten-nebenkostenabrechnung/SKILL.md`). Die irreführende Formulierung `mindestens 50/30/70 Prozent nach Verbrauch` wurde durch die richtige Regel ersetzt: verbrauchsabhängiger Anteil mindestens 50 Prozent und höchstens 70 Prozent, restlicher Anteil (30 bis 50 Prozent) nach Wohnfläche oder umbautem Raum (§§ 7, 8 HeizkostenV). Der häufige Schlüssel 70/30 ist ausdrücklich als eine zulässige Ausgestaltung innerhalb der Bandbreite gekennzeichnet.
- **§ 55a GmbHG ergänzt** (`corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur/SKILL.md`). Die Authorized-Capital-Zeile in der US-Term-Sheet-Übersetzungstabelle behauptete fälschlich, die GmbH kenne kein genehmigtes Kapital. Korrigiert auf: bei der AG § 202 AktG, bei der GmbH seit MoMiG ausdrücklich § 55a GmbHG (mit Verweis auf den bestehenden Skill `gesellschaftsgruender-genehmigtes-kapital`).
- **Negatives Agio als rechtlich ausgeschlossen klargestellt** (`corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur/SKILL.md`). Die Down-Round-Passage hatte die wirtschaftliche Verwässerung mit einem "negativen Agio" beschrieben. Das ist juristisch falsch: Ausgabe unter pari verstößt gegen § 9 Abs. 1 GmbHG / § 5 Abs. 2 GmbHG (Verbot der Unter-pari-Emission, nichtige Kapitalerhöhung). Korrigiert auf die drei zulässigen Down-Round-Instrumente: Null-Agio, größere Stückzahl zum reduzierten Preis pro Anteil, flankierende Wandeldarlehen oder Anti-Dilution-Anpassungen.
- **CO2KostAufG nicht auf WEG-Innenverhältnis anwenden** (`testakten/weg-hausverwaltung-hohenzollernhof/11-co2kostaufg-aufteilungspruefung.md`). Die Testakte hatte den Eindruck vermittelt, das CO2KostAufG-Stufenmodell sei auf die WEG-Jahresabrechnung anzuwenden. Korrigiert: das CO2KostAufG regelt nur das Vermieter-Mieter-Verhältnis (§§ 1, 2 CO2KostAufG); die WEG-interne Hausgeldumlage bleibt bei § 16 Abs. 2 WEG und HeizkostenV. Praxisrelevanz für die WEG: vermietende Eigentümer brauchen aus der Jahresabrechnung Datengrundlagen (Brennstoffmenge, CO2-Emission, Energieträger, gebäudespezifischer CO2-Wert) gemäß § 2 Abs. 2 CO2KostAufG. Beanstandung und Anfechtungsrisiko entsprechend umformuliert.
- **Gewährleistungsfrist nach Werkart differenziert** (`weg-hausverwaltung/skills/handwerker-beauftragung-vergabe/SKILL.md`). Die pauschale Auswahl `5 / 4 Jahre` ist nur für Bauwerk-Arbeiten korrekt. Ergänzt um die richtige Trias: BGB Bauwerk 5 Jahre (§ 634a Abs. 1 BGB), VOB/B Bauwerk 4 Jahre bei wirksamer Einbeziehung (§ 13 Abs. 4 VOB/B), sonstige Werkleistungen und Wartung 2 Jahre. Im Auftragsbestaetigungs-Muster und in der Vergleichstabelle.
- **Belegeinsicht § 18 Abs. 4 WEG statt § 28 Abs. 4 WEG** (`weg-hausverwaltung/skills/datenschutz-dokumentenfreigabe/SKILL.md`). Die Belegeinsicht in Verwaltungsunterlagen folgt § 18 Abs. 4 WEG; § 28 Abs. 4 WEG regelt nur den Vermögensbericht. Description und Body entsprechend getrennt; beide Rechtsgrundlagen verlinkt.

## Plugin-Versionsbumps

- `corporate-kanzlei` 30.0.0 → 31.0.0
- `weg-hausverwaltung` 35.0.0 → 36.0.0
- `gesellschaftsrecht-legal-english` 35.0.0 → 36.0.0
- `.claude-plugin/marketplace.json` synchronisiert

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v35.0.0 — Agio-Dogmatik in drei Plugins, Codex-Round-2-Fixes, Umlaut-Hygiene Testakte

- **Codex-Round-2-Fixes in `testakten/gesellschaftsrecht-legal-english-frankfurt-startup/`.** Der `§ 14 GmbHG`-Anker für Sonderrechte/Vorzugsanteile wurde in den Dateien `06-associate-arbeitsstand.md` und `07-erwarteter-output-ohne-musterloesung.md` durch den korrekten Anker `Satzungsautonomie + § 35 BGB analog` ersetzt; gestützt auf ständige Rechtsprechung (BGHZ 123, 15; BGH II ZR 89/79 = LM BGB § 35 Nr. 4; OLG Nürnberg 12 U 813/99). § 14 GmbHG (Einlagepflicht/Nennbetrag) wird explizit als Nicht-Anker markiert. In `02-cap-table-und-gesellschafterliste.md` wurde der irreführende Verweis auf eine angebliche Subscription-Liste in Datei 03 Ziff. 2 berichtigt — die 4,8/0,4-Aufteilung steht in Datei 02 selbst (CFO-Slack-Thread vom 28.05.2026); Datei 03 Ziff. 2 verlangt nur eine Lead-Mindestquote von 75 Prozent.
- **Umlaut-Hygiene Testakte.** Sämtliche deutschen Wörter in der Testakte wurden auf korrekte Umlaute (ä/ö/ü/ß) umgestellt. Wortgrenzen-basiertes Ersetzungsskript mit expliziter Wörterliste; englische Termini (gross proceeds, business, issued, less, loss, passu, Voss, Stein, Goetheplatz, ...) bleiben unangetastet. 17 Dateien geändert.
- **Agio-Dogmatik in drei Plugins.** Echtes/korporatives vs. unechtes/schuldrechtliches Agio bei der GmbH; § 3 Abs. 2 GmbHG mit Dauerwirkung auch bei Kapitalerhöhung; Differenzierung nach Fälligkeit (Fall 1 keine Satzungsaufnahme erforderlich, Fall 2 Eintragungshindernis bei Nichtaufnahme); Sachagio im Rahmen des qualifizierten Anteilstauschs § 21 UmwStG; § 272 Abs. 2 Nr. 1 vs. Nr. 4 HGB; § 27 KStG steuerliches Einlagekonto. Rechtsprechung verifiziert: BGH II ZR 216/06; BGH BGHZ 80, 129; BGH BGHZ 71, 40 (Kali+Salz); BFH I R 53/08; BFH IX R 12/22.
  - **Neuer Skill `gesellschaftsrecht/skills/agio-und-kapitalruecklage`** mit voller Dogmatik, Praxismuster-Formulierungen, US-Term-Sheet-Übersetzung und Anfängerfehler-Katalog.
  - **Neuer Skill `corporate-kanzlei/skills/corporate-kanzlei-agio-und-kapitalerhoehungsstruktur`** mit Schnittstellen-Management (Notar, Steuerberater, Investor Counsel, CFO), Strukturierungsentscheidungen und Streitpunkten in der Praxis.
  - **Neue Testakten-Datei `24-agio-und-kapitalruecklage-streitfrage.md`** in der Frankfurt-Testakte mit Mandatsbezug (Kometenfalter Series A), Notiz Adelheid von Westarp an Hildemar K., US-Term-Sheet-Bezug (Original Purchase Price, Par Value, APIC, Liquidation Preference) und Aufgabenkatalog für den Associate.
- **Plugin-Versionsbump.** `gesellschaftsrecht` 29.0.0 → 30.0.0; `corporate-kanzlei` 29.0.0 → 30.0.0; `gesellschaftsrecht-legal-english` 34.0.0 → 35.0.0 in den jeweiligen `<plugin>/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Forbidden-Frontmatter-Check: keine Treffer
- description-Längen ≤ 1024 Zeichen, Skill-Namen ≤ 64 ASCII
- Verifikation aller Rechtsprechungs-Zitate über dejure.org und bundesfinanzhof.de

---

# v34.0.0 - Corporate Legal English didaktisiert, Multi-Format-Testakte

- **`gesellschaftsrecht-legal-english` didaktisch nachgeschärft.** Der `allgemein`-Skill startet jetzt mit einem echten 90-Sekunden-Kaltstart: Sofortdiagnose, Erfahrungslevel, drei Rückfragen, Skill-Routing und Mini-Arbeitsprodukt. Der `rookie-modus` wurde vom bloßen Prüfraster zum Lerncoach mit 30-Minuten-Plan, Begriffskarten, Mini-Übungen und klaren Senior-Review-Gates.
- **Zwei neue Skills.** `lernpfad-dealroom-simulator` führt Anfänger durch mehrteilige Transaktionsakten mit Materialinventar, Dealkarte, Lernpfad, Übungen und Arbeitsprodukt. `anschauungsmaterial-multiformat-auswertung` wertet Excel, PDF, Scan, Screenshot, JPEG, Chat, Email und Dealroom-Fragmente quellenkritisch aus.
- **Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` weiter ausgebaut.** Neu: WhatsApp-Thread als Markdown, Multi-Format-Index, echtes Excel-Trainingsmodell (`18-cap-table-waterfall-training.xlsx`), PDF-Scan zur Beurkundungssprache, Whiteboard-Foto, Investor-Email-Screenshot, WhatsApp-Screenshot und Rookie-Cheatsheet als PDF.
- **Dokumentations- und Versionspflege.** Plugin-README, Testakten-README, Root-README, SKILLS-Übersicht, Marketplace und Plugin-Manifest aktualisiert; `gesellschaftsrecht-legal-english` auf `34.0.0` gesetzt.

## Qualitätssicherung

- `git diff --check`
- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- JSON-Manifest-Parse aller Plugin-Manifeste
- Multi-Format-Sanity: XLSX mit `openpyxl`, PDFs mit `pypdf`, JPEGs mit `PIL` geöffnet

---

# v33.0.0 — Corporate Legal English Testakten-Ausbau, Codex-Klarstellungen

- **Corporate Legal English Testakte massiv ausgebaut.** `testakten/gesellschaftsrecht-legal-english-frankfurt-startup/` von 7 auf 16 Dateien erweitert. Neue Dateien: `00-deal-personen-und-zeitleiste.md` (Cast, Zeitleiste, fiktive Eckdaten), `08-glossar-deutsch-englisch-fallstricke.md` (zwoelf Begriffspaare mit typischen Missverstaendnissen), `09-anfaengerfehler-katalog-mit-partner-rotstift.md` (fuenf Fehlerklassen mit Vorher/Nachher), `10-wandeldarlehen-tante-ermelind.md` (vollstaendiger Convertible Loan mit Discount 20 Prozent, Cap 10 Mio. EUR, 8 Prozent PIK), `11-investor-counsel-markup-roundtrip.md` (Markup-Email Brackenmuir & Quint LLP, interne Sortierung, 02:14-Uhr-Antwort), `12-notar-checkliste-und-handelsregisterlogik.md` (Notariat Schwartz, § 5 BeurkG, Einheitsdoktrin, § 40 GmbHG), `13-side-letter-und-information-rights.md` (Stahlauge Seed Side Letter, Northbridge Series A Side Letter), `14-board-und-consent-matters-mapping-de-en.md` (zehn Reserved Matters mit DE-Umsetzung), `15-closing-checkliste-cp.md` (30 CPs, Gap-Analyse, Post-Closing). Bestandsdateien 01 bis 07 substantiell ausgebaut (Term Sheet jetzt mit vollstaendigem Definitions-Set, SHA-Synopse Seed/Series A, DD-Index mit Datenraumstruktur, Associate-Notiz mit Partner-Rotstift, Pruefraster 100 Punkte).
- **README der Testakte neu strukturiert** mit Lernpfaden A (Begriffsdisziplin, 2 Stunden), B (Mandatsanalyse, 4 Stunden), C (Vertiefung, 4 bis 6 Stunden) und D (Mandantenkommunikation, 1 bis 2 Stunden).
- **Plugin-Versionsbump.** `gesellschaftsrecht-legal-english` von 24.1.0 auf 25.0.0 in `<plugin>/.claude-plugin/plugin.json` und `.claude-plugin/marketplace.json`.
- **Codex-PR-Klarstellung Direktwirkung EU-Lohntransparenzrichtlinie** in `fachanwalt-arbeitsrecht/skills/fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich/SKILL.md`. Praxishinweis: vertikale Direktwirkung gegenueber oeffentlichen Arbeitgebern (Van Duyn 41/74, Becker 8/81, Marshall 152/84) ab 07.06.2026, horizontale Direktwirkung gegenueber privaten Arbeitgebern grundsaetzlich ausgeschlossen (Marshall 152/84, Dansk Industri C-441/14); richtlinienkonforme Auslegung (Marleasing C-106/89) und Francovich-Staatshaftung (C-6/90, C-9/90) bleiben.
- **Codex-PR-Klarstellung BVerfG 1 BvR 183/25** in `mietrecht/skills/mietspiegel-quellen/SKILL.md`. Der Nichtannahmebeschluss vom 08.01.2026 betrifft die 2020er Verlaengerung der Mietpreisbremse (§ 556d BGB in der Fassung vom 19.03.2020) und die Berliner Mietenbegrenzungsverordnung vom 19.05.2020, nicht das Verlaengerungsgesetz vom 17.07.2025 (BGBl. 2025 I Nr. 163, Geltung bis 31.12.2029). Verfassungsgerichtliche Pruefung der 2025er Verlaengerung steht noch aus.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Grep auf verbotene Frontmatter-Felder — 0 Treffer

---

# v29.0.1 — EU-Richtlinien-Nachzug, GVG-Streitwert ab 01.01.2026, Mietpreisbremse-Verlaengerung

- **EU-Lohntransparenzrichtlinie 2023/970 nachgetragen** in `arbeitsrecht/skills/bag-equal-pay-paarvergleich-8azr30024/SKILL.md` und `fachanwalt-arbeitsrecht/skills/fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich/SKILL.md`. Neue Bloecke fassen Art. 5 (vorvertragliche Transparenz, Verbot Gehaltshistorie), Art. 7 (Auskunft binnen zwei Monaten), Art. 9 (Berichtspflichten ab 250 / 150 / 100 Beschaeftigten), Art. 10 (gemeinsame Bewertung ab fuenf Prozent Gefaelle), Art. 16 (Schadensersatz ohne Obergrenze), Art. 18 (Beweislastumkehr bei Pflichtverletzung) und Art. 21 (Verjaehrung mindestens drei Jahre) zusammen. Umsetzungsfrist 07.06.2026; nationale Umsetzung steht zum Stand Mai 2026 noch aus. Quelle: https://eur-lex.europa.eu/eli/dir/2023/970/oj
- **EU-Plattformarbeitsrichtlinie 2024/2831 ausgearbeitet** in `arbeitsrecht/skills/arbeitnehmer-status/SKILL.md`. Einzeiler aus v29 ersetzt durch ausgearbeiteten Block mit Vermutungsregel zugunsten des Beschaeftigungsverhaeltnisses, Beweislastumkehr und Umsetzungsfrist 02.12.2026. Quelle: https://eur-lex.europa.eu/eli/dir/2024/2831/oj
- **Mindestlohn ab 01.01.2026 / 01.01.2027 verifiziert** mit Fundstelle Fuenfte MindestlohnAnpassungsverordnung vom 05.11.2025, BGBl. 2025 I Nr. 268 — in `arbeitsrecht/skills/allgemein/SKILL.md` und `arbeitsrecht/skills/mindestlohn-arbeitszeit-erfassung/SKILL.md`. 13,90 EUR ab 01.01.2026; 14,60 EUR ab 01.01.2027.
- **GVG-Streitwertgrenze korrigiert** in `mietrecht/skills/klageentwurf-amtsgericht/SKILL.md`. Frontmatter und Body benennen jetzt das Gesetz zur Staerkung der Amtsgerichte in Zivilsachen (Bundesrat-Billigung 21.11.2025, Inkrafttreten 01.01.2026) statt der falschen "Justizmodernisierung 2024". Anwaltszwang ebenfalls ab zehntausend Euro; Berufungsbeschwer in § 511 Abs. 2 Nr. 1 ZPO von 600 auf 1.000 Euro angehoben. Uebergangsregelung: vor 01.01.2026 anhaengige Verfahren bleiben bei fünftausend Euro. Quelle: BRAK-Nachrichten 24/2025 vom 26.11.2025.
- **BGH-Rechtsprechung zur Zahlungsverzugskuendigung ergaenzt** in `mietrecht/skills/mahnung-zahlungsverzug-mieter/SKILL.md`: BGH, Urt. v. 01.07.2020 – VIII ZR 323/18 (Schonfristzahlung beseitigt nur die fristlose Kuendigung, hilfsweise ordentliche bleibt wirksam; § 574 Abs. 1 Satz 2 BGB ausgeschlossen) und BGH, Beschl. v. 08.12.2021 – VIII ZR 32/20 (Erheblichkeit nach § 573 Abs. 2 Nr. 1 BGB anhand der Gesamthoehe des Rueckstands). VIII ZR 287/23 vom 09.07.2025 aus v29 unveraendert erhalten.
- **Mietpreisbremse-Verlaengerung dokumentiert** in `mietrecht/skills/mietspiegel-quellen/SKILL.md`. Neuer Block zum Verlaengerungsgesetz vom 17.07.2025 (BGBl. 2025 I Nr. 163, § 556d Abs. 2 Satz 4 BGB bis 31.12.2029) sowie BVerfG-Nichtannahmebeschluss vom 08.01.2026 – 1 BvR 183/25 (Verfassungsbeschwerde gegen die Verlaengerung erfolglos; Bestaetigung der Linie aus 1 BvL 1/18).
- **Versionsbump.** `arbeitsrecht`, `fachanwalt-arbeitsrecht` und `mietrecht` auf `29.0.1` in `<plugin>/.claude-plugin/plugin.json` und in `.claude-plugin/marketplace.json`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v24.2.0 — References-Einzelfix und UNVERIFIABLE-Online-Check

- **Welle 5 — References-Einzelfix.** Die 16 in v24.1.0 noch offenen toten `references/`-Verweise einzeln durchgegangen. 14 waren falsch-positiv (Aufloesungspfade, ASCII-Tree-Beispiele, generierte Skills). 1 echter Bug gefixt: `produktrecht/skills/produktrecht-kaltstart-interview` verwies auf `references/launch-pruefung-framework-de.md`, korrigiert auf den realen Pfad `produktrecht/skills/launch-pruefung/references/seven-category-framework.md`. 2 Laufzeit-Cache-Verweise (`kanzlei-builder-hub`: `registry-cache.json`, `surfaced.json`) durch leere `references/`-Verzeichnisse mit `README.md`-Hinweis dokumentiert.
- **Welle 6 — UNVERIFIABLE-Online-Check.** Die 893 in Welle 2 als UNVERIFIABLE markierten Aktenzeichen wurden online gegen dejure.org, BGH-/BAG-/BFH-/BSG-Datenbanken, Curia, openJur und Landesjustizportale geprueft (20 parallele Batches a ~45 AZ). Ergebnis: 148 rehabilitiert, 621 in Schnellrunde nicht auffindbar, 30 widerspruechlich, 94 uebersprungen. Konservative Strip-Strategie (Welle-1-NOT_FOUND + Original-Audit-Negativ-Marker, ohne positive Hinweise) lieferte 7 sichere Loeschkandidaten – alle bereits durch v24.1.0 entfernt. Welle 6 entfernt netto keine weiteren Zeilen, liefert aber die konsolidierte Klassifikation in `audit/welle2_unverifiable_audit_2026-05-29.json` und die 20 Roh-Batches in `audit/unverifiable_batches/` als Grundlage fuer kuenftige Reparaturwellen.
- **Audit-Bericht erweitert.** `audit/README.md` enthaelt jetzt sechs Wellen mit Methodik und Befunden.
- **Versionsbump.** Alle 103 Plugins (inkl. neuer `meinungspruefer`), Marketplace-Top-Level und alle Marketplace-Plugin-Eintraege einheitlich auf `24.2.0`.
- **Neues Plugin `meinungspruefer`** mit 36 Skills zur Pruefung von Aeusserungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung/Tatsache, Beleidigung, ueble Nachrede, Verleumdung, § 188 StGB, § 193 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR-/EuGH-Rechtsprechung, OLG-/KG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Arbeitsplatz, Schule und kommunale Machtkritik. Rechtsprechungsbank mit frei pruefbaren Quellen und ohne BeckRS-/Kommentar-/Aufsatz-Blindzitate.
- Neue Testakte **`meinungspruefer-grenzfaelle-alltag`** mit X-Post zum kommunalen Bauprojekt, LinkedIn-Pinocchio, Kantinenaeusserung ueber Zahlen, Elternchat, Buergermeister-"Lackaffe", Abmahnung, polizeilicher Anhoerung, Belegmappe und USA-Vergleichsnotiz.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer

---

# v24.1.0 — AZ-Strip, Konversationsstil und LG Aachen 10 O 306/25

- **Welle 3 — Halluzinations-AZ entfernt.** Die im Vollaudit (`audit/audit_problems_2026-05-27.json`) als WRONG_TOPIC oder NOT_FOUND klassifizierten 969 Aktenzeichen wurden aus den betroffenen SKILL.md gestrichen. Ergebnis: 175 Dateien geaendert, 392 Zeilen entfernt; YAML-Frontmatter blieb unangetastet. Dokumentiert in `audit/README.md` und `audit/references_audit_2026-05-29.json`.
- **Welle 4 — References-Konsistenz.** 17 tote Markdown-Verweise auf `references/`-Dateien identifiziert; einer (`rechtsberatungsstelle/.../pruef-warteschlange.yaml` → `review-queue.yaml`) gefixt. Die restlichen 16 sind in `audit/references_audit_2026-05-29.json` dokumentiert.
- **Konversationsstil-Update.** `CLAUDE.md` und alle 102 `<plugin>/skills/allgemein/SKILL.md` erhalten einen verbindlichen Block: erste Antwort konzis, hoechstens eine unverzichtbare Rueckfrage, dann schnell zur Dokumentenproduktion. Ausfuehrlich nur bei echter Subsumtion, Tabellen, Risikoanalysen oder Schriftsatz-/Memo-Text. Allgemein-Skills sind Einstieg, nicht Vorlesung.
- **Frontmatter-Konvention geschaerft.** `CLAUDE.md` listet jetzt die verbotenen Frontmatter-Felder explizit (`triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **LG Aachen 10 O 306/25 (Urteil vom 27.05.2026) als Leitentscheidung aufgenommen** in: `bgb-at-pruefer/.../kauf-im-internet-und-auktionen`, `bgb-at-pruefer/.../gesetzesverbot-sittenwidrigkeit-paragraphen-134-138`, `vertragsrecht/.../vertragspruefung`, `produktrecht/.../feature-risikobewertung`. Inhalt: Button-Beschriftung "Wette abgeben" beim Online-Gluecksspiel genuegt nicht § 312j Abs. 3 BGB; endgueltige Unwirksamkeit nach Abs. 4; Rueckabwicklung nach § 812 BGB unabhaengig von Lizenz. Quellenhinweis: offizieller Volltext zum Aufnahmezeitpunkt noch nicht oeffentlich; Aufnahme erfolgte auf Basis Pressehinweis Gamesright GmbH / rightmart, 28.05.2026.
- **Audit-JSON-Fix bewahrt.** Zwei unescapte Quotes (Z. 425, 7661) aus dem Vollaudit-JSON sind gefixt (bereits in v24.0.0 als Commit `5b0676ef` gepusht).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs` — OK
- `python3 scripts/validate-yaml-frontmatter.py` — 0 Fehler, 0 Warnungen
- `python3 /tmp/welle5_komma_check.py` — 0 Treffer
- Alle 102 Plugins, Marketplace-Top-Level und alle Marketplace-Plugin-Eintraege einheitlich auf `24.1.0`

---

# v24.0.0 — Einheitliche Versionsbasis und vollständige Codex-Integration

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` einheitlich auf Version `24.0.0` gezogen. Damit sind erstmals seit mehreren Releases sämtliche Manifeste, der Marketplace-Top-Level und alle Marketplace-Plugin-Einträge auf identischer Versionsnummer.
- Sämtliche Codex-Pull-Requests (Selbstvertreter Amtsgericht und Sozialgericht, Lobbyregister Bundestag, Wertgrenzen 2026 nach Justizstandort-Stärkungsgesetz, 150 Steuerberater-Skills BWA/Lohn/DBA) sind in `main` integriert und im Release enthalten.
- YAML-Frontmatter-Hygiene aus v23.0.1 vollständig übernommen: 47 SKILL.md-Frontmatter und ein verbliebener Plugin-Root-CLAUDE.md-Bug aus dem ASCII-Quote-Sweep sind bereinigt; alle Skills passieren den offiziellen `claude plugin validate --strict`.
- Validatoren erweitert: `scripts/validate-yaml-frontmatter.py` (echter pyyaml-Parse-Check inklusive Komma-Zahl-Sequenzen) und `scripts/validate-with-claude-cli.sh` (Wrapper für offizielles `claude plugin validate --strict`).

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `python3 scripts/validate-yaml-frontmatter.py`
- `./scripts/validate-with-claude-cli.sh` (offizielle Anthropic CLI v2.1.153)
- `git diff --check`

---

# v23.0.1 — Download-Abdeckung und Quellenhygiene

- Alle 102 Plugin-READMEs geprüft: jedes Plugin nennt sein Plugin-ZIP aus dem `latest`-Release.
- Alle 57 Testakten sind im Testakten-Index mit ZIP-Download eingetragen; jede Testakte ist aus mindestens einem passenden Plugin-README verlinkt.
- Die zentrale README-Übersicht nennt alle 102 Plugins, inklusive `liquiditaetsplanung` und der beiden Selbstvertreter-Plugins.
- Zitierweise v4.0 repo-weit nachgezogen: keine BeckRS-, Kommentar-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei/amtlich oder per lizenziertem Live-Zugriff verifizierter Quelle.
- Unsichere oder nicht frei belegte Rechtsprechungs- und Literaturzeilen in Skills, README-Texten, Generatorvorlagen und Beispiel-Hausregeln durch Live-Verifikationshinweise ersetzt.
- Alle Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.1` gezogen; der `v23.0.0`-Stand bleibt enthalten.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 102/102 Plugin-READMEs mit Plugin-ZIP, 57/57 Testakten-ZIPs im Index und aus Plugin-READMEs erreichbar, 0 unsichere Zitations-Treffer im engeren Audit.
- lokaler Build und Validierung aller Plugin- und Testakten-ZIPs mit `scripts/validate-release-zips.py`

---

# v23.0.0 — Selbstvertreter-Ausbau und ASCII-Anführungszeichen

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `23.0.0` gezogen.
- Beide Selbstvertreter-Testakten (`selbstvertreter-amtsgericht-kuechentisch-kaufpreis` und `selbstvertreter-sozialgericht-heizkosten-eilantrag`) deutlich ausgebaut: je drei neue Dokumente, alle bestehenden Dateien stark erweitert, mittlerer bis höherer Schwierigkeitsgrad. Neu in der Amtsgericht-Akte: AGB-Klauseln zur Prüfung, privat eingeholte Voreinschätzung eines Tischlermeisters, Foto-Inventar mit EXIF-Metadaten, zehn widersprüchliche Internet-Treffer. Neu in der Sozialgericht-Akte: vollständiger Bürgergeld-Bescheid mit Berechnungsblatt, Attest mit Mindesttemperaturangabe wegen kindlichem Asthma, vier Telefonnotizen, KdU-Konzept der Stadt Leipzig.
- Beide Selbstvertreter-Plugins `selbstvertreter-amtsgericht` und `selbstvertreter-sozialgericht` in der Plugin-Übersichtstabelle im Root-README ergänzt (waren bislang versehentlich nicht in der Tabelle).
- Steuerrecht-Plugin: Plugin-README-H1 von "Steuerrecht für Anwaltschaft und Steuerberatung" auf "Steuerrecht - Steuerberater und Anwälte" geändert (Slug `steuerrecht-anwalt-und-berater` bleibt — keine Breaking Changes).
- Repo-weiter Sweep: alle typografischen Anführungszeichen (`"` `"` `'` `'` `"` `"`) durch ASCII `"`/`'` ersetzt in 909 Dateien. Verhindert HTML-Entity-Darstellung (`&#x201E;` etc.) in Plugin-Outputs bei Clients, die Markdown durch HTML-Escaping schicken.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v22.0.0 — Nachbarschaftsstreit, US-Transfer-TIA, KI-VO-Evidence-Pack

- Alle 102 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `22.0.0` gezogen.
- Neues Plugin **`nachbarschaftsstreit-pruefer`** mit 19 Skills zum Nachbarrecht: Überbau (§§ 912-916 BGB), Überhang (§ 910 BGB), Grenzbaum/Grenzanlage (§§ 921-923 BGB), Einfriedung, Immissionen (§ 906 BGB), Notweg (§§ 917-918 BGB), Vertiefung/Baugrube (§ 909 BGB), Hammerschlagsrecht, Landesnachbarrecht-Router, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung und Vergleich. Mit zwölfteiliger Testakte `nachbarschaftsstreit-horrorfall-rosengarten`.
- Drei neue Datenschutz-Skills im Plugin `datenschutzrecht`: `us-transfer-tia-dokumentation`, `standardvertragsklauseln-scc-paket`, `drittlandtransfer-behoerdenpaket-output`. Mit Testakte `datenschutz-us-transfer-cloudsuite-rheinmain` (CloudSuite Assist, DPF-Lücke, SCC Modul 2, hbDI-Antwortentwurf).
- Neuer KI-VO-Skill `output-konformitaetsbescheinigung-evidence-pack` mit Statusleiter Final/Entwurf/Readiness/Drittstelle, EU-Konformitätserklärung nach Art. 47 / Anhang V, Evidence Index und Lückenliste. Mit Testakte `ki-vo-konformitaetsbescheinigung-bewerberpilot`.
- Bereicherungs- und Arbeitsrecht-Cleanup: URL-Konsistenz `claude-fuer-deutsches-recht` und ASCII-Slugs in den Direkt-Download-Tabellen, Skill-Slugs in Plugin-README-Tabellen ohne Umlaute.
- Direkt-Download-Blöcke in den beiden neuen Testakten-READMEs analog zu den 53 anderen.
- Stand jetzt 102 Plugins, 2410 Skills und 55 Testakten.

---

# v21.0.0 — Direkt-Downloads und Bereicherungsrecht-Cleanup

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `21.0.0` gezogen.
- 52 Testakten-Unterordner-READMEs mit sichtbarem Direkt-Download-Button für die jeweilige ZIP-Datei aus dem `latest`-Release.
- 13 Plugin-READMEs mit eigenem **Zum Ausprobieren: Testakte**-Block und Direkt-Download-Link: `arbeitszeugnis-analyse`, `bgb-at-pruefer`, `fachanwalt-arbeitsrecht`, `fachanwalt-sozialrecht`, `fachanwalt-verwaltungsrecht`, `gesellschaftsrecht`, `grosskanzlei-corporate-ma`, `insolvenzrecht`, `jveg-kostenpruefer`, `kanzlei-allgemein`, `liquiditaetsplanung`, `lobbyregister-bundestag`, `steuerrecht-anwalt-und-berater`.
- Bereicherungsrecht-Cleanup: 77 Skills mit Umlaut- und Typo-Reparatur, 50 Skills mit vollständig ausgebauten Aktivierungs-Descriptions im Muster Trigger + Normen + Prüfraster + Output + Abgrenzung.
- Stand bleibt 101 Plugins, 2386 Skills und 52 Testakten.

---

# v20.0.0 — Release 20 Gesamtstand

- Alle 101 Plugin-Manifeste und die zentrale `.claude-plugin/marketplace.json` auf Version `20.0.0` gezogen.
- `README.md` und `testakten/README.md` auf Release `v20.0.0` aktualisiert; Stand bleibt 101 Plugins, 2332 Skills und 52 Testakten.
- Inhaltlicher Stand aus `v19.1.0` bleibt enthalten: BGB-AT-Prüfer mit qES-/beA-/Formfiktion-Workflow, Arbeitszeugnis-Testakte, Legistik-Ausbau und die bisherigen Qualitätsbereinigungen.

---

# v19.1.0 — BGB AT, Arbeitszeugnis-Testakte und Legistik-Ausbau

- Neues Plugin `bgb-at-pruefer` mit 53 Skills zum BGB Allgemeiner Teil: Fallaufnahme, Anspruchsaufbau, Willenserklärung, Zugang, Vertragsschluss, Auslegung, Geschäftsfähigkeit, Form, Nichtigkeit, Anfechtung, Stellvertretung, Bedingungen, Fristen und Verjährung.
- `bgb-at-pruefer` um einen eigenen qES-/beA-/Formfiktion-Skill erweitert: §§ 126, 126a, 130 BGB, § 130e ZPO, § 46h ArbGG, § 173 ZPO und BGH VIII ZR 155/23 / VIII ZR 159/23 werden jetzt als gemeinsamer BGB-AT-/Prozessrechts-Workflow geprüft.
- Neue synthetische Testakte `bgb-at-altfraenkische-werkstatt` mit Online-Auktion, Annahmefrist, Minderjährigenkauf, Vollmacht, Anfechtung, Bedingung, Form-/Sittenwidrigkeitsprüffeldern und beA-/qES-/Formfiktion-Nachtrag.
- Neue Testakte `arbeitszeugnis-analyse-bluehendes-leben` mit zehn vollständigen Arbeitszeugnissen aus zehn Branchen (PTA Apotheke, angestellter Anwalt, MTRA Radiologie, Lagermeister, ZFA, Filialleiterin Sparkasse, Speditionsdisponent, Hotel-Empfangsleiter, Wohnbereichsleitung Pflege, Industriemechanik); tatsächliche Noten verdeckt über gesamte Skala eins bis fünf, ohne Musterlösung.
- `methodenlehre-buergerliches-recht` und `subsumtions-pruefer` verweisen nun auf `bgb-at-pruefer`, wenn die abstrakte Methodik in konkrete BGB-AT-Mechanik überführt werden soll.

- Legistik-Werkstatt auf fünf Startbahnen erweitert: Bundesressort/Bundesregierung, Bundestag/Fraktion/Opposition, Landesressort/Landesregierung, Landtag/Landtagsfraktion und sonstige Normgeber.
- Legistik-Allgemein-Skill fragt jetzt Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Verfahrensstand, Drucksache, Geschäftsordnung und Outputformat ab und routet sauber in Spezial-Skills.
- `formulierungshilfe-bauen` kann jetzt nicht nur ministerielle Koalitions-Zulieferungen, sondern auch Gesetzentwürfe aus der Mitte, Änderungsanträge, Anträge und Entschließungsanträge für Bundestag und Landtage einschließlich Oppositionsarbeit.
- `legistik-auftragsaufnahme`, `normhierarchie-routing` und `referentenentwurf-bauen` trennen fachlichen Verfasser, formalen Initiator und politischen Auftraggeber und führen Landesverfassung, Landes-Geschäftsordnung, Landtags-GO und Verkündungsrecht als Pflichtprüfpunkte mit.
- Perplexitys stummer Upload-Block in allen 100 Allgemein-Skills geglättet: Fristenscan zuerst, Materialklassifikation, Kontextanker, Skill-Routing, nur eine konkrete Rückfrage und ein weniger begrenzender Co-Pilot-Ton.
- Testakten mit `.placeholder`-Dateinamen in Chatbeschreibungen, Bildbeschreibungen, Fehlblätter, Inhaltsvermerke und Validierungsnotizen umbenannt; README-Verweise entsprechend aktualisiert.
- Produktrecht-Skills von offenen Verify-/Pinpoint-Markern, einer nicht tragfähigen Produkthaftungsfundstelle und schematischen Influencer-/Green-Claims-Aussagen bereinigt.
- KI-Governance-Beispiele auf Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO für Bewerbungs-/Beschäftigungssysteme korrigiert und die allgemeine Chatbot/GPAI-Abgrenzung geschärft.
- BVerfG-Leitentscheidung "Soldaten sind Mörder" mit den konkreten Aktenzeichen ersetzt; Quellenhinweis auf geprüfte Primärquellen und Pinpoint-Nachtrag umgestellt.

---

# v19.0.0 — KI-VO-Härtung, BVG-Abschleppakte und Release-Stand

- `ki-vo-ai-act-pruefer` vertieft Art. 3 Nr. 1 KI-VO mit einem dokumentierbaren KI-System-Vermerk zu Automation, Autonomie, Adaptivität, Inferenz, Output und Umgebungseinfluss.
- Art. 6 Abs. 2 i.V.m. Anhang III ist neu aufgebaut: alle acht Bereiche mit Untertatbeständen, Zweckbestimmung, allgemeiner Chatbot/GPAI-Abgrenzung und Mitarbeitenden-Fehlgebrauch.
- Allgemeine Chatbots/GPAI werden ausdrücklich nicht automatisch als Hochrisiko behandelt; maßgeblich sind Anbieter-Zweckbestimmung, Betreiberzweck und tatsächliche Integration in Anhang-III-Prozesse.
- Art. 6 Abs. 3 wurde mit Profiling-Sperre, vier Fallgruppen, Grundrechtsrisiko und Art.-6-Abs.-4-Dokumentation geschärft.
- Normen-/Standards-Skill trennt harmonisierte Normen, gemeinsame Spezifikationen, GPAI Code of Practice und ISO/IEC-Standards ohne falsche Vermutungswirkung.
- Output-Dokumentation enthält jetzt Art.-3-Vermerk, Anhang-III-Matrix, Off-label-Governance, Re-Evaluation-Trigger und Standards-Hinweis.
- Perplexitys BVG-/ÖPNV-Abschleppmaterial ist in `main` integriert: neuer Verwaltungsrechts-Skill `fa-vwgo-widerspruchsbescheid-abschleppen-oepnv` und neue Testakte `bvg-widerspruchsstelle-abschleppen-mobg`.
- Die BVG-Testakte verwendet nun Lichtbildbeschreibungen statt Platzhalterdateien; die VG-Berlin-Fundstelle ist auf Urteil vom 30.05.2022, VG 11 K 298/21, mit Pressemitteilung vom 04.07.2022 korrigiert.
- `README.md`, `SKILLS.md`, `testakten/README.md` und der Allgemein-Skill des Verwaltungsrechts-Plugins spiegeln nun 2279 Skills, 50 Testakten und das neue Routing zum BVG-Widerspruchsbescheid wider.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `19.0.0`.
- `README.md` und `testakten/README.md` auf Stand 101 Plugins, 2331 Skills, 52 Testakten und Release `v19.1.0` aktualisiert.

---

# v18.0.0 — Allgemein-Skills als schöne Plugin-Einstiege

Version 18.0.0 ist ein repo-weiter Workflow-Release: Jedes Plugin hat nun einen eigenen `allgemein`-Einstiegsskill als schnellen Intake-, Workflow- und Routingpunkt.

- 34 fehlende `skills/allgemein/SKILL.md` neu angelegt.
- 66 vorhandene Allgemein-Skills mit einheitlichem Schnellstart-Workflow, Intake in 60 Sekunden, Sofort-Triage, Antwortformat und Routing-Regeln ergänzt.
- Jeder Allgemein-Skill enthält eine automatisch aus dem jeweiligen Plugin gezogene Liste der verfügbaren Spezial-Skills und soll bei Bedarf zwei bis fünf passende Folge-Skills mit Grund und erwartetem Output vorschlagen.
- `SKILLS.md` und README-Zählungen auf 2278 Skills aktualisiert.
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `18.0.0`.

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Zusatzcheck: 100 Plugins, 2278 Skills, 100 Allgemein-Skills mit Schnellstart-Workflow
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.1 — Insolvenzanfechtung-Audit, KI-Screening und Verteidigung

Version 17.5.1 ist ein gezielter Nachlauf nur für Insolvenzanfechtungsrecht. Der Schwerpunkt liegt auf den fehleranfälligen Normgruppen §§ 129, 130/131, 133, 134, 135, 142 und §§ 143-147 InsO, dem Reformstand nach der Anfechtungsreform 2017, den Fristen, dem Bargeschäft, Gesellschafterdarlehen und der Verteidigung des Anfechtungsgegners.

## Korrigiert und gehärtet

- **§§ 130/131 InsO:** kongruente und inkongruente Deckung wurden sauber getrennt; § 130 verlangt Kenntnis, während § 131 die objektive Monats-/Antragsnähe und die subjektiven Alternativen für den zweiten und dritten Monat abbildet.
- **§ 133 InsO:** Vorsatzanfechtung arbeitet nun mit Zehnjahresgrundtatbestand, Vierjahresfenster für Deckungshandlungen, Zahlungsvereinbarungsregel und der Zweijahresvariante für entgeltliche Verträge mit nahestehenden Personen.
- **§ 142 InsO:** Bargeschäft ist nicht mehr als starre 30-Tage-Regel beschrieben; die Skills prüfen unmittelbaren Leistungsaustausch nach Verkehrsauffassung, das Drei-Monats-Fenster für Arbeitsentgelt und die Sondergrenze bei § 133 InsO.
- **§ 135 InsO:** neuer eigener Skill für Gesellschafterdarlehen, Gesellschaftersicherheiten, Rückzahlungen, Besicherungen, Kleinbeteiligungs-/Sanierungsprivileg und Drittfinanzierungsvarianten.
- **§§ 143-147 InsO:** Rechtsfolgen, § 144 InsO, Rechtsnachfolge, Verjährung und Handlungen nach Verfahrenseröffnung wurden neu geordnet; Zinsen werden an § 143 Abs. 1 Satz 3 InsO, Verzug und § 291 BGB angebunden.
- **Verteidigung des Anfechtungsgegners:** neuer eigener Skill mit defensiver Matrix zu Normauswahl, Gläubigerbenachteiligung, Kenntnis, Bargeschäft, Entreicherung, § 144 InsO, Verjährung und Vergleich.

## KI-Anfechtungsworkflow

- Neuer Skill `inso-ki-anfechtungsansprueche-schuldnerakten` für die Auswertung von Schuldnerakten mit Quellenankern, Zahlungschronologie, Anfechtungskandidaten-Matrix, Human-Review-Markierungen und Evidenzlücken.
- Das System darf Anfechtungskandidaten identifizieren und strukturiert vorprüfen, ersetzt aber keine anwaltliche Wertung bei § 133 InsO, Gläubigerbenachteiligungsvorsatz, Kenntnisindizien, Sanierungsversuchen, Bargeschäftsverteidigung und komplexen Dreiecksverhältnissen.
- Insolvenzverwaltung und Fachanwalt-Insolvenz/Sanierung wurden mit demselben Prüfungsmaßstab synchronisiert, damit Verwalterseite, Klagevorbereitung und Verteidigung nicht auseinanderlaufen.

## Release-Stand

- 100 Plugins
- 2244 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.1`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- gezielte Suche nach alten Fehlmustern zu SanInsFoG/Reform 2017, § 130/§ 131, § 133, § 142, § 146 und § 135 InsO
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v17.5.0 — Text-/Quellenaudit, README-Gateway-Anleitung und Lobbyregister-API-Härtung

Version 17.5 finalisiert den nachgezogenen Hauptstand nach v17 und zieht die Repository-Dokumentation, Plugin-Versionen und Release-Artefakte auf einen einheitlichen Zwischenrelease. Schwerpunkt ist ein konservativer Qualitätsschnitt: weniger erfundene Fundstellen, bessere deutsche Beschreibungstexte, klarere README-Anleitung für alternative Claude-kompatible API-Endpunkte und ein belastbareres Lobbyregister-Plugin.

## Korrigiert und gehärtet

- **Rechtsprechungs- und Literaturhinweise:** mehrere falsch oder unsicher zugeordnete BGH-/Kapitalmarkt-/Corporate-Nachweise wurden entfernt oder durch passendere, überprüfbare Leitentscheidungen ersetzt; methodische Skills sollen nicht mehr mit frei erfundenen Aktenzeichen arbeiten.
- **Lobbyregister Bundestag:** die API-Hinweise wurden als lesende Kontroll- und Monitoring-Schicht geschärft. Mock-Artefakte verweisen auf den stabilen `current`-Schema-Pfad und dokumentieren den Stand `R2.21`, statt eine spekulative neue API-Version zu behaupten.
- **README:** die Anleitung zum Einhängen einer eigenen oder zwischengeschalteten Claude-/Anthropic-kompatiblen API wurde providerneutral neu gefasst, mit klarer Trennung zwischen Claude Code im Terminal und Desktop-/Cowork-Oberflächen.
- **Deutsche Beschreibungstexte:** Frontmatter-Descriptions und Marketplace-Texte wurden breit auf Umlaute, ß und lesbare deutsche Formulierungen bereinigt, ohne Pfade, Links oder technische IDs umzubenennen.
- **Testakten:** Lobbyregister-Testakten bleiben bewusst realistisch-fragmentarisch, enthalten aber keine spekulativen API-Abgabeversprechen. Die API wird für Suche, Exportvergleich, Monitoring und Plausibilisierung genutzt.

## Release-Stand

- 100 Plugins
- 2241 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `17.5.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der geänderten Lobbyregister-API-Mockdateien
- lokaler Build und Validierung aller Plugin-ZIPs mit `scripts/validate-release-zips.py`

---

# v16.0.0 — Halluzinationsbereinigung, Audit-Hardening und v15-Finalstand

Version 16 baut direkt auf `v15.0.0` auf und nimmt den dortigen Stand mit Lobbyregister-Plugin, Selbstvertreter-Plugins und Steuerberater-Werkzeugen vollständig mit. Der Schwerpunkt dieses Releases ist eine weitere Qualitätsschicht gegen erfundene oder falsch zugeordnete Rechtsprechungsnachweise.

## Korrigiert und gehärtet

- **KI-Governance / KI-VO:** falsche Altzuordnungen zu `EuGH C-203/22` wurden aus KI-VO-/Governance-Kontexten entfernt und auf den tatsächlich passenden DSGVO-Art.-15-Kontext umgestellt.
- **Insolvenzplan / StaRUG / Insolvenzverwaltung:** unsichere oder nicht verifizierbare BGH-Nachweise wie `VI ZR 184/17`, `IX ZR 238/17`, `IX ZB 32/21` und `IX ZR 18/19` wurden aus produktiven Skills entfernt, soweit keine belastbare Ersatzfundstelle vorlag.
- **Insolvenzrecht / D&O:** falsche `II ZR 234/18`- und `II ZR 199/19`-Zuordnungen wurden durch passende, überprüfte Leitentscheidungen ersetzt.
- **Squeeze-out:** der Handels-/Gesellschaftsrecht-Skill verweist nun auf DAT/Altana und Stollwerck statt auf eine falsche Insolvenz-/Haftungszuordnung.
- **Audit-Dokumentation:** `audit/HALLUZINATIONS_AUDIT_2026-05-27.md` dokumentiert die zusätzliche lokale Reparaturwelle und den Übergang auf `v16.0.0`.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `16.0.0`

## Qualitätssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- Rest-Suche nach den bekannten problematischen Aktenzeichen-/Fundstellenmustern außerhalb der Audit-Historie

---

# v15.0.0 — Lobbyregister, Selbstvertreter, Steuerberater-Werkzeuge und Release-Finalisierung

Version 15 buendelt die nachgelieferten Perplexity-/Klar-Ausbauten mit dem neuen `lobbyregister-bundestag` Plugin und setzt den gesamten Marketplace auf einen einheitlichen Major-Stand.

## Neue und stark ausgebaute Inhalte

- **`lobbyregister-bundestag` neu:** 50 gefuehrte Skills fuer Registrierungspflicht, Ausnahmen, Portal-Eingabeplan, Finanzdaten, Regelungsvorhaben, Stellungnahmen/Gutachten, Verhaltenskodex, Aktualisierung, Bussgeldrisiken, RfS-Kommunikation und Revisionsspur.
- **Open Data/API V2 im Lobbyregister:** eigene Referenz, API-Abfrageplan, JSON-Mapping, Registerexport-Diff und Monitoringplan. Die API wird bewusst als lesende Kontrollschicht gefuehrt; Registrierung und Aktualisierung bleiben Portalhandlungen.
- **Drei Lobbyregister-Testakten:** Dublin-Bank mit Frankfurter Zweigniederlassung und Doppelregistrierungsproblem, Public-Affairs-Agentur Wasserstoff, Bürgerinitiative Waldmoor. Alle drei enthalten API-/Export-Diff-Artefakte.
- **Selbstvertreter-Plugins:** Amtsgericht und Sozialgericht sind auf `main` integriert und in die Marketplace-/Release-Struktur aufgenommen.
- **Steuerberater-Werkzeuge:** `steuerrecht-anwalt-und-berater` enthaelt die neuen StB-Skills fuer BWA, SuSa, Lohn, Jahresabschluss, DBA, Mandantenkommunikation und Software-/Portalroutinen.
- **Audit-Fixes:** Halluzinations- und Aktenzeichen-Reparaturwellen aus den v14.2.x Hotfixes sind mitenthalten.

## Release-Stand

- 100 Plugins
- 2175 `SKILL.md`
- 49 Testakten
- alle `plugin.json` und `.claude-plugin/marketplace.json` auf Version `15.0.0`

## Qualitaetssicherung

- `node scripts/validate-plugin-structure.mjs`
- `git diff --check`
- JSON-Parsing der neuen Lobbyregister-Testakten
- Release-ZIP-Validierung ueber `scripts/validate-release-zips.py` im Build/Workflow

---

# v14.2.0 — Vollumfaenglicher Wissensboost ueber alle 1800+ Skills

Inhaltlicher Tiefenboost ueber alle 97 Plugins und ueber 1800 Skills. Jeder bearbeitete Skill bekommt eine konkrete Triage zum Mandatseinstieg, eine vollstaendige Paragrafenkette mit Wortlaut der zentralen Tatbestandsmerkmale, zwei bis vier aktuelle Leitsatz-Zitate aus BVerfG BGH BAG BFH BSG BVerwG EuGH oder OLG mit Aktenzeichen und Fundstelle, Hinweise auf die zentrale Kommentarliteratur des Rechtsgebiets, einen Schritt-fuer-Schritt-Workflow und ein passendes Output-Template fuer Schriftsatz Bescheid Beschluss oder Mandantenbrief. Strukturelle Bereinigung Plugin sozialrecht-kanzlei vollstaendig nach fachanwalt-sozialrecht uebernommen und alte Light-Touch-Selbstbezeichnung entfernt.

## Was sich pro geboostetem Skill geaendert hat

- **Triage zum Einstieg** — fuenf bis sieben konkrete Vorabfragen mit Begruendung warum sie zu klaeren sind
- **Zentrale Normen mit Wortlaut** — Paragrafenkette mit kursivem Tatbestandsmerkmal nicht nur Paragrafennummer
- **Aktuelle Rechtsprechung** — zwei bis vier Leitsaetze BVerfG BGH BAG BFH BSG BVerwG EuGH OLG mit Aktenzeichen Fundstelle Randnummer Paraphrase
- **Kommentarliteratur** — die ein bis drei einschlaegigen Standardkommentare fuer das Rechtsgebiet
- **Workflow in Schritten** — von Aktenanlage ueber Substantiierung bis Versand
- **Output-Template mit Platzhaltern** — Schriftsatz Bescheid Beschluss Klage Mandantenbrief
- **Rote Schwellen und Eskalationskriterien** — wann Fall an Fachanwalt oder Notar abgegeben gehoert
- **Verzicht auf Boilerplate** — keine generischen Phrasen mehr keine Wiederholungen

## Welleneinteilung

Der Boost erfolgte in 12 Wellen mit jeweils 90 bis 250 Skills.

| Welle | Cluster | Skills |
| --- | --- | --- |
| 1 | Arbeitsrecht inkl. Arbeitszeugnis | 201 |
| 2 | Steuerrecht Familienrecht Erbrecht Sozialrecht | 108 |
| 3 | Strafrecht Verkehrsrecht | 117 |
| 4 | Miet- Bau- und Immobilienrecht | 92 |
| 5 | Medizinrecht Versicherungsrecht Sport- und Transportrecht | 89 |
| 6 | Gewerblicher Rechtsschutz Urheber- und Medienrecht | 90 |
| 7 | IT-Recht Datenschutz KI-Verordnung DSA NIS-2 | 137 |
| 8 | Insolvenz- und Sanierungsrecht | 154 |
| 9 | Corporate M und A Gesellschaftsrecht Gruendung | 208 |
| 10 | Bank- und Kapitalmarktrecht Vergabe International Migration | 114 |
| 11 | Verwaltungs- Verfassungs- Energie- Umwelt- Kartell- Verbraucherrecht | 135 |
| 12 | Prozessrecht Vertragsrecht Forderungsmanagement Compliance Kanzlei-Methodik Jurastudium | 308 |

## Quellenhygiene-Hinweis

Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht aus Modellwissen erzeugt. Literatur darf nur mit vom Nutzer bereitgestellter Quelle oder lizenziertem Live-Zugriff verwendet werden.

## Strukturelle Bereinigung

- **Plugin sozialrecht-kanzlei** wurde vollstaendig in **fachanwalt-sozialrecht** ueberfuehrt. 20 Skills wurden verschoben vier doppelt vorhandene Themen wurden gemergt. Das Fachanwalt-Plugin enthaelt jetzt sowohl die Fachanwalt-Rechtsprechungstiefe als auch die volle Kanzleioperative — Bescheidanalyse Akteneinsicht Anlagen Eilantrag Hilfsmittel Pflegegrad Fristenbuch und PKH.
- **Light-Touch-Selbstbezeichnung entfernt** in 51 Files. Plugins fuer Fachanwaltschaft sind nicht laenger Light-Touch sondern vollumfaenglich.
- **SKILLS.md** mit funktionierenden GitHub-Anker-Links und Zwei-Spalten-Tabelle pro Plugin direkt verlinkt zur SKILL.md.

## Qualitaetssicherung

- Validator `node scripts/validate-plugin-structure.mjs` final OK
- Komma-Sweep in plugin.json und SKILL.md Frontmatter `description:` ueberall ohne Komma zwischen Ziffern
- Cyrillic-Confusables-Sweep ueber alle bearbeiteten Files clean
- Keine verbotenen Frontmatter-Felder (triggers when_to_use language rechtsgebiet license argument-hint user-invocable allowed_tools tools model adapted_from)
- Keine XML-Brackets in description-Feldern
- YAML-Quoting bei descriptions mit Doppelpunkt-Konstrukten korrekt

## Versionsstand nach v14.2.0

- 97 Plugins
- Ueber 1800 boostfaehige Skills bearbeitet (44 Skills waren bereits auf v14.1-Niveau und wurden ohne weitere Aenderung uebernommen)
- alle plugin.json und marketplace.json auf version `14.2.0`

# v14.1.0 — Grosser Inhalts-Boost (145 Top-Skills auf dreifache Tiefe)

Inhaltliche Verdreifachung der 145 fachlich wichtigsten Skills in allen 24 Fachanwalt-Plugins sowie in `steuerrecht-anwalt-und-berater` und den fuenf Corporate-Plugins (`corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender`). Generische Boilerplate-Skills (Erstgespraech, Vergleichsverhandlung, Mandantenkommunikation) sind aus dem Boost ausgenommen — der Fokus liegt auf der fachlichen Substanz.

## Was sich pro geboostetem Skill geaendert hat

Jeder der 145 ausgewaehlten Skills wurde von einer Knappformulierung in eine voll ausgearbeitete Arbeitsanleitung umgeschrieben. Erweitert wurden, wo passend:

- **Kaltstart-Mandantenfragen** — sechs bis zehn konkrete Fragen mit Begruendung
- **Rechtsgrundlagen** — Wortlaut der zentralen Tatbestandsmerkmale, nicht nur Paragrafnummer
- **Pruefschemata in Tabellenform** — acht bis fuenfzehn Schritte
- **Schriftsatzbausteine und Klauselvorlagen** — vollstaendige Formulierungen
- **Beweislast und Darlegungslast** — klar zugeordnet
- **Fristen und Verjaehrung** — konkret kalendermaessig
- **Typische Gegenargumente und Reaktion** — Tabellenform
- **Streitwert und RVG-Hinweise** — beziffert
- **Strategische Empfehlung** — aussergerichtlich, Klage, Vergleich
- **Anschluss-Skills** — Querverweise zu anderen Skills im Plugin
- **Aktuelle Aktenzeichen** — BGH, BAG, BFH, BVerwG, BVerfG, OLG, FG

## Cluster-Aufteilung

| Cluster | Plugins | Geboostete Skills |
| --- | --- | --- |
| Cluster A — 24 Fachanwalt-Plugins | siehe Plugin-Liste unten | 120 |
| Cluster B — Steuerrecht | `steuerrecht-anwalt-und-berater` | 5 |
| Cluster C — Corporate | `corporate-kanzlei`, `grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `gesellschaftsrecht`, `gesellschaftsgruender` | 25 (5 pro Plugin) |

## Fachanwalt-Plugins im Boost (alle 24)

`agrarrecht`, `arbeitsrecht`, `bank-kapitalmarktrecht`, `bau-architektenrecht`, `erbrecht`, `familienrecht`, `gewerblicher-rechtsschutz`, `handels-gesellschaftsrecht`, `insolvenz-sanierungsrecht`, `internationales-wirtschaftsrecht`, `it-recht`, `medizinrecht`, `miet-wohnungseigentumsrecht`, `migrationsrecht`, `sozialrecht`, `sportrecht`, `strafrecht`, `transport-speditionsrecht`, `urheber-medienrecht`, `vergaberecht`, `verkehrsrecht`, `versicherungsrecht`, `verwaltungsrecht`.

## Nebenbei behoben

Zwei alte Validator-Fehler in nicht-geboosteten Skills (Komma-in-Zahlen-Pattern in `description`):

- `fachanwalt-gewerblicher-rechtsschutz/.../SKILL.md`: `§§ 5, 32 HinSchG` zu `§§ 5 und 32 HinSchG`
- `fachanwalt-insolvenz-sanierungsrecht/.../SKILL.md`: `§ 9, 3/4-Mehrheit` zu `§ 9 mit 3/4-Mehrheit`

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.1.0.
- `marketplace.json` (Top-Level und alle Plugin-Eintraege) auf 14.1.0.
- Validator OK.

---

# v14.0.0 — Frischer Major-Release

Frischer Sammelrelease ueber alle 98 Plugins. Der Versionssprung von 12.x auf 14.0 markiert das Ende des 12er-Inkrement-Zyklus und buendelt den aktuellen Stand der Skill-Familie als einheitliches Major-Release.

## Bug-Hunt Immobilienrechtspraxis

Der Immobilien-Plugin-Schwerpunkt dieses Releases ist eine systematische Bug-Pruefung. Geprueft wurden Frontmatter-Felder, Description-Laengen, verbotene Pattern (Komma in Zahlen), verbotene Frontmatter-Keys, Cross-References, kaputte Markdown-Links und Mischformen aus Umlauten und ASCII-Aequivalenten.

- Inkonsistente Schreibweise `Buerogeb\u00e4ude` (ASCII-Mix mit Umlaut) zu `B\u00fcrogeb\u00e4ude` korrigiert (`projekt-arbeitsweise`).
- Cross-Reference auf `memorandums-ersteller` validiert (Plugin existiert im Marketplace, Verweis bleibt).
- Frontmatter aller sieben Skills geprueft: keine verbotenen Felder, keine zu langen Descriptions, keine Komma-Patterns.
- Plugin-Description und Keywords sauber, keine Aenderung erforderlich.

## Globaler Versionsbump

- Alle 98 `plugin.json` auf 14.0.0.
- `marketplace.json` auf 14.0.0 (Top-Level und alle Plugin-Eintraege).
- Validator OK.

---

# v12.6.0 — Aktuelle BAG-Rechtsprechung 2025/2026 (Arbeitsrecht + Fachanwalt)

Drei kuerzlich entschiedene BAG-Urteile, die die Arbeitnehmerseite spuerbar staerken, werden in den Plugins `arbeitsrecht` und `fachanwalt-arbeitsrecht` jeweils als eigenstaendiger Pruefungsskill verankert. Die Skills enthalten Kaltstartfragen, Pruefschema, Schriftsatzbausteine und konkrete Verteidigungslinien.

## Neue Skills im Plugin `arbeitsrecht` (drei)

- `bag-equal-pay-paarvergleich-8azr30024` — BAG 23.10.2025 (8 AZR 300/24): Equal Pay durch Paarvergleich. Eine Arbeitnehmerin muss keine statistische Vergleichsgruppe auswerten. Ein einziger besser bezahlter maennlicher Kollege bei gleichwertiger Arbeit begruendet die Vermutung des Paragraf 22 AGG. Pauschale Hinweise auf Median oder Verhandlungsgeschick reichen nicht mehr.
- `bag-mindesturlaub-kein-verzicht-9azr10424` — BAG 03.06.2025 (9 AZR 104/24): Kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhaeltnis, auch nicht durch gerichtlichen Vergleich. Klausel-Verbote, empfohlene Vergleichsformulierung mit Trennung Mindesturlaub und Mehrurlaub.
- `bag-freistellungsklausel-unwirksam-5azr10825` — BAG 25.03.2026 (5 AZR 108/25): Pauschale formularmaessige Freistellungsklausel nach Kuendigung unwirksam wegen unangemessener Benachteiligung Paragraf 307 BGB. Beschaeftigungsanspruch BAG GS 1/84 bleibt bestehen.

## Neue Skills im Plugin `fachanwalt-arbeitsrecht` (drei)

- `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich` — Anwaltsperspektive auf 8 AZR 300/24: Kaltstart-Rueckfragen, Klagebaustein Equal Pay, typische Arbeitgeber-Verteidigung und Reaktion.
- `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht` — Anwaltsperspektive auf 9 AZR 104/24: empfohlene Vergleichsformulierung, Klausel-Verbote, Nachforderungsmoeglichkeit bei bereits geschlossenem Pauschalvergleich.
- `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` — Anwaltsperspektive auf 5 AZR 108/25: Strategie fuer Beschaeftigungsanspruch oder Verhandlungsmasse, Schriftsatzbaustein, Annahmeverzugsfolgen.

## Plugin-Metadaten

- Plugin-Beschreibung beider Plugins um Hinweis auf aktuelle BAG-Rechtsprechung 2025/2026 ergaenzt.
- README beider Plugins um Abschnitt zu den neuen Skills erweitert.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.6.0.

---

# v12.5.0 — Arbeitszeugnis-Analyse: Vollstaendiger Mandatsablauf

Schliesst den Mandatsworkflow im `arbeitszeugnis-analyse` Plugin: vom Erstkontakt mit dem Mandanten ueber den Ergebnisbericht bis zum Aufforderungsschreiben an den Arbeitgeber. Das Plugin deckt damit nicht nur die Analyse des Zeugnistextes ab, sondern den gesamten Anwaltsworkflow von der Mandatsannahme bis zum Berichtigungsverlangen.

## Neue Skills (drei)

- `erstgespraech-und-mandatsannahme` — Eingangsbestaetigung mit Dank fuer das uebersandte Zeugnis, strukturierte Anforderungsliste fuer fehlende Unterlagen (Arbeitsvertrag, Aenderungsvereinbarungen, Vorzeugnisse, Kuendigungsschreiben, Abmahnungen, Fehlzeitenuebersicht, Lohnabrechnungen), Erstgespraech-Leitfaden in fuenf Bloecken (Sachverhalt, Ziel, Vergleichsbereitschaft, rechtliche Erstinformation, Vereinbarung), Pruefliste vor Mandatsannahme.
- `mandantenbericht-zeugnisanalyse` — Schriftlicher Ergebnisbericht an den Arbeitnehmer in sieben Abschnitten: Gesamtnote, Befund pro Themenbereich, kritische Einzelstellen mit Wortlaut, rechtliche Einordnung, Erfolgsaussichten in drei Stufen, drei Handlungsoptionen (Akzeptanz, Berichtigungsverlangen, Klage) mit Kosten-Nutzen-Abwaegung, klare Empfehlung. Verstaendliche Sprache fuer den juristischen Laien.
- `aufforderungsschreiben-arbeitgeber` — Aussergerichtliches Berichtigungsverlangen mit acht Bausteinen: Mandatsanzeige, Bezugnahme auf das Zeugnis, Rechtsgrundlage Paragraf 109 GewO, Beanstandungen pro Streitstelle (Wortlaut alt, Wortlaut neu, Begruendung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Schlussformel-Pruefung, kalendermaessige Fristsetzung, Klageandrohung, Kostenfolge. Hoeflich-bestimmter Ton ohne Drohgebaerden. Vollstaendiger Mustertext mit Beispielen.

## Plugin-Metadaten

- 31 Skills (vorher 28), 20-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst, hebt den vollstaendigen Mandatsablauf hervor.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.5.0.

---

# v12.4.0 — Arbeitszeugnis-Analyse: Sprachhebel, Codeworte, Klagestrategie

Vertiefung des `arbeitszeugnis-analyse` Plugins um drei spezialisierte Sprach- und Recht-Skills: feingranularer Steigerungsadverbien-Katalog, vollstaendiger Katalog negativer Codeworte fuer sensible Themen sowie eine durchgaengige Klagestrategie zur Zeugnisberichtigung von der ausserprozessualen Rueckforderung bis zum vollstreckbaren Tenor.

## Neue Skills (drei)

- `steigerungsadverbien-katalog` — Vier-Klassen-Matrix der Adverbien mit Notenwirkung: echte Steigerer (stets, jederzeit, immer), Schein-Steigerer mit Risiko (sehr, ausserordentlich nur in Kombination), Abschwaecher (im Allgemeinen, weitgehend, meist) und negative Verstaerker (nie, kaum, kein einziges Mal). Notenkalibrierung jeder Klasse, sodass die satzweise Bewertung das richtige Gewicht erhaelt.
- `negative-codeworte-katalog` — Tabuthemen-Katalog mit den verdeckten Anspielungen auf Alkohol, Krankheit, Diebstahl/Untreue, Konflikt mit Vorgesetzten, mangelnde Loyalitaet, Betriebsratstaetigkeit, sexuelle Verfehlungen, Mitlaeufertum sowie systematischen Auslassungssignalen. Jede Kategorie mit den typischen Formulierungen und dem rechtlich gebotenen Tenor.
- `klage-strategie-zeugnisberichtigung` — Vollstaendige prozessuale Linie: aussergerichtliches Berichtigungsverlangen, Klageantrag mit Tenor (vollstreckbar gemaess Paragraf 888 ZPO), Beweislastverteilung (Note ab Drei: Arbeitnehmer; oberhalb der Drei: Arbeitgeber), Streitwertberechnung, Verjaehrung/Verwirkung und prozesstaktische Empfehlungen.

## Geaenderte Skills

- `verbesserungsvorschlaege-formulieren` — drei neue Drift-Rewrite-Beispiele zu Lernbereitschaft, Innovationsverhalten und Sozialverhalten; ergaenzte Regeln-Tabelle.
- `rechtliche-bewertung-bag-rechtsprechung` — drei neue Absaetze zu verfestigter BAG-Rechtsprechung, Schlussformel-Codeworten und Verjaehrung/Verwirkung; sieben neue Regeln-Tabellenzeilen und drei zusaetzliche Bewertungsbeispiele.

## Plugin-Metadaten

- 28 Skills (vorher 25), erweiterter 16-Schritte-Workflow im README.
- Plugin-Beschreibung neu gefasst und auf die drei neuen Schwerpunkte abgestimmt.
- Globaler Versionsbump aller 98 Plugins und der marketplace.json auf 12.4.0.

---

# v12.3.0 — Arbeitszeugnis-Analyse: Schaufenster-Drift-Detektor

Spezialisierter Ausbau des `arbeitszeugnis-analyse` Plugins um die Erkennung des Schaufenster-Patterns: einzelne Saetze auf Note-1-Niveau, daneben Saetze auf Note-3-Niveau zum selben Themenbereich. Wer nur die Spitzensaetze liest, sieht Note 1; wer die Drift erkennt, sieht die korrekte hochgezogene Zwei bis solide Drei.

## Neue Skills (drei)

- **`bereichs-drift-detektor`** — Erkennt Drift innerhalb derselben acht Themenbereiche (Fachkenntnisse, Lernbereitschaft, strategisches Denken, Arbeitsweise, Engagement, Innovation, Arbeitsergebnis, Sozialverhalten). Spreizung zwei Stufen = Rot, eine Stufe = Orange. Drift in weichen Bereichen (Lernen, Innovation, Sozialverhalten) wird gesondert geflaggt.
- **`satzweise-notenmatrix`** — Bewertet jeden notenrelevanten Satz mit Schulnote von eins bis fuenf. Festes Raster: Steigerungsadverb plus Superlativ = 1, eins davon = 2, Grundaussage = 3, Einschraenkung oder "bemueht" = 4, Distanzformel = 5. Tabellarisches Ausgabeformat mit Themenbereich pro Satz — Datenbasis fuer Drift-Detektor und Gesamtnoten-Aggregation.
- **`muster-arbeitszeugnis-gemischte-noten`** — Vollstaendiges anonymisiertes Schulungszeugnis mit Schaufenster-Pattern. Zeigt 1er- und 3er-Saetze gemischt, vollstaendige Satz-fuer-Satz-Notenmatrix, Bereichs-Drift-Analyse und gewichtete Gesamtnote mit Drift-Penalty.

## Updates

- **`gesamtnoten-aggregation`**: neue Drift-Penalty-Regel (minus halbe Stufe bei Spreizung zwei Stufen, minus halbe Stufe bei konstanter Note 3 in weichen Bereichen). Neues Beispiel: Schaufenster-Zeugnis.
- **`widerspruechliche-bewertungen`**: vierter Widerspruchstyp (Schaufenster-Pattern im selben Themenbereich) mit Verweis auf den neuen Drift-Detektor.
- **`README.md`**: erweiterter Empfehlungs-Workflow um Satzmatrix, Drift-Detektor und Widerspruchsanalyse; Plugin enthaelt jetzt 25 Skills.

## Globaler Versionsbump

Alle 98 Plugins und `marketplace.json` auf v12.3.0.

---

# v12.2.0 — Testakten in Plugin-READMEs sichtbar gemacht

## README-Sweep
13 Plugin-READMEs ergaenzt: Testakte als sichtbarer Direkt-Download (Tabelle) direkt unter der Plugin-Download-Sektion.

- arbeitsrecht (Vogt, Weber)
- aussenwirtschaft-zoll-sanktionen (GlobalMaschinen)
- datenschutzrecht (Solis Vision X)
- dsa-dma-digitalregulierung (Bayerische Baustube)
- geldwaeschepraevention-aml-kyc (Musterholding)
- grosskanzlei-corporate-ma (Datenraum)
- insolvenzrecht (LUMEN Studios — Edelholz war bereits drin)
- insolvenzverwaltung (Moebelwerk Havelberg, Nordlicht Handels)
- kanzlei-allgemein (Kanzlei-Alltag)
- steuerrecht-anwalt-und-berater (Edelholz)
- strafbefehl-verteidiger (LUMEN Studios)
- vertragsrecht (Sieglinger SV-Gutachten)
- zwangsverwaltung-zvg (Friedrichshoefe, Mietshaus Parkstrasse, Eppendorf)

## Fix
- testakten/inkasso-zahlungsklage-modefuchs/README.md: toter Link auf `Akte_ModeFuchs_GmbH.zip` entfernt; nur der `originale/` Ordner mit 28 PDFs bleibt.
- Mapping-Korrektur Testakten zu Plugins: `bauplanungsrecht` -> `normenkontrolle-bauleitplanung`.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.2.0.

# v12.1.0 — Validatorhaertung Plugin-Generator + Versionsbump

## Fix (gegenueber v12.0.0)
- `forderungsmanagement-klagewerkstatt/scripts/plugin_aus_hausregeln.py`: erzeugte hauseigene Mini-Plugins sind jetzt validatorkonform und sofort in Claude Code installierbar.
  - plugin.json description gekuerzt von 514 auf 218 Zeichen (Marketplace-Limit 300).
  - Zahl-Komma-Zahl-Sequenzen `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` (Cowork-Validator-Regel).
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt; Trigger-Phrasen wurden in die description integriert.

## Bump
- Alle 98 Plugins, marketplace.json und CHANGELOG auf v12.1.0.

# v12.0.1 — Hotfix forderungsmanagement-klagewerkstatt Plugin-Generator

## Fix
- `scripts/plugin_aus_hausregeln.py` erzeugt jetzt validatorkonforme Mini-Plugins (`klagewerkstatt-<slug>`):
  - plugin.json description gekuerzt auf 218 Zeichen (vorher 514, Marketplace-Limit 300)
  - Zahl-Komma-Zahl-Sequenz `12, 13, 29, 29c` und `23, 71` ersetzt durch `12/13/29/29c` und `23 und 71` in plugin.json + SKILL.md description
  - Frontmatter-Felder `language`, `license`, `when_to_use` aus erzeugter SKILL.md entfernt (Trigger-Phrasen in description integriert)
- Erzeugte hauseigene Plugins lassen sich jetzt sofort in Claude Code installieren.

## v12.0.0 — 2026-05-26 — Strafrecht-Ausbau: Nebenklage, Zeugenbeistand, Adhaesion, Insolvenzantrag der StA + Codex-Fixes + Bug-Hunt

### Major-Feature: 4 neue Skills im Plugin `fachanwalt-strafrecht`

- `fachanwalt-strafrecht-nebenklage-opfervertretung` — Nebenklagebefugnis § 395 StPO, Anschluss § 396 StPO, Opferanwaltsbeiordnung § 397a StPO, Akteneinsicht § 406e StPO, psychosoziale Prozessbegleitung § 406g StPO, RVG VV Nr. 4124 ff.
- `fachanwalt-strafrecht-zeugenbeistand` — Beistand gemaess § 68b StPO, Pruefung § 55 StPO Selbstbelastung, §§ 52-53 StPO Zeugnisverweigerung, Adressanonymisierung § 68 Abs. 2/3 StPO, Whistleblower-Konstellation.
- `fachanwalt-strafrecht-adhaesionsverfahren` — zivilrechtliche Anspruche im Strafverfahren §§ 403-406c StPO, Antrag § 404 StPO, Vergleich § 405 StPO als Vollstreckungstitel, Grundurteil § 406 StPO, RVG VV Nr. 4143-4147.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` — Insolvenzantrag StA / Finanzamt gegen Angeklagte, Doppelspur Strafverfahren-Insolvenzverfahren, Vermoegensabschoepfung §§ 73 ff. StGB und Beschlagnahme §§ 111b ff. StPO, § 111i StPO, Schweigerecht vs. § 97 InsO.

### Codex-Feedback adressiert (PR fachanwalt-strafrecht)

Drei Skills im Plugin `fachanwalt-strafrecht` enthielten zivilrechtliche Reste aus einem Allgemein-Template (Leistungs-/Feststellungs-/Gestaltungsantrag, Streitwert aus Hauptforderung, Klage-einreichen-Walk-Away). Komplett strafrechts-spezifisch neu geschrieben:

- `schriftsatzkern-substantiierung` — Einspruch gegen Strafbefehl, Revisionsbegruendung, Klageerzwingung, Beweisantraege § 244 StPO, Verfahrenshindernisse, Sach- und Verfahrensruegen.
- `vergleichsverhandlung-strategie` — Verstaendigung § 257c StPO, Einstellung § 153a StPO, Adhaesionsvergleich § 405 StPO, TOA § 46a StGB; statt zivilrechtlicher Skripte.
- `erstgespraech-mandatsannahme` — RVG-Gebuehrentatbestaende VV-RVG Teil 4 und Teil 5 statt Streitwert-Kalkulation, fuenf strafrechtsspezifische Praxis-Konstellationen.

### Bug-Hunt v12.0.0

- Alle Backtick-Cross-Refs auf das fusionierte Plugin `kanzlei-cowork` (52 Dateien in 24 Plugins + CHANGELOG, INSTALLATION, ASSET_INDEX, TESTBERICHT) auf `kanzlei-allgemein` umgestellt.
- Config-Pfade in `kanzlei-allgemein/skills/{sekretariats-tagesbrief, mandantenakte-anlegen, fristenbuch-fuehren, kanzlei-cowork-kaltstart-interview}` von `~/.claude/plugins/config/.../kanzlei-cowork/` auf `kanzlei-allgemein/` korrigiert.
- Slash-Command-Verweise in `tests/smoke-tests.md` und `kanzlei-cowork-kaltstart-interview` von `/kanzlei-cowork:` auf `/kanzlei-allgemein:` umgestellt.
- `tests/smoke-tests.md`: Abschnitt-Header von `## kanzlei-cowork (rechnungserstellung-rvg)` auf `## kanzlei-allgemein (rechnungserstellung-rvg)` umgestellt.
- `kanzlei-allgemein/.claude-plugin/plugin.json`: Keyword `kanzlei-cowork` aus Liste entfernt (Migrations-Hinweis in README/CHANGELOG bleibt).
- Workflow-Validator-Fixes aus v11.0.0-Schluss: `README.md` ohne toten Link `./kanzlei-cowork`; `testakten/README.md` mit allen 46 Akten (vorher 44), inkl. zwei neuer Tabellen-Zeilen und ZIP-Eintraege fuer `dsa-dma-bayrische-baustube-meissner` und `sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger`.

### Repo-Stand v12.0.0

- 98 Plugins, alle plugin.json einheitlich auf 12.0.0
- marketplace.json mit 98 Eintraegen, alle 12.0.0
- 46 Testakten
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII); Validator-Script `validate-plugin-structure.mjs` clean.

## v11.0.0 — 2026-05-26 — DSA/DMA-Plugin, BetrVG-Heilung, qES-Befristung, KI-Sachverstaendige, Kanzlei-Cowork-Fusion

### Major-Feature: Plugin "dsa-dma-digitalregulierung"

Neues Plugin Nr. 99: **DSA und DMA und Digitalregulierung EU**. 9 Skills:

- `digitalregulierung-pyramide-check` — Einstiegsskill, ordnet Sachverhalte den passenden Rechtsakten zu (DSA DMA Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO § 19a GWB)
- `dsa-vlop-vlose-einordnung-und-pflichten` — Schwellenwert 45 Mio. EU-Nutzer, Designation, Pflichtenkatalog Art. 34-43
- `dma-gatekeeper-schwellen-und-kernplattformdienste` — drei kumulative Voraussetzungen, quantitative Vermutungen, KPD-Katalog, Pflichten Art. 5-7
- `dsa-art-34-systemische-risikobewertung` — vier Risikoarten, Methodik, Audit Art. 37
- `dsa-art-40-forschungsdatenzugang-algorithmen` — drei Zugangsregime, vetted researchers, Delegierte VO 2024/2987
- `account-sperre-soziales-netzwerk-rechtsbehelfe-art-20-23-dsa` — Stufenmodell Art. 17 / 20 / 21, BGH III ZR 179/20 und III ZR 192/20, Eilrechtsschutz
- `digitalregulierung-schnittstellen-dsgvo-p2b-19a-gwb` — Mehr-Anker-Strategie
- `zustellung-und-vertreter-art-13-dsa-art-37-dma` — Praxis Zustellung gegen Auslands-Plattformen
- `klage-gegen-vlop-einordnung-art-263-aeuv` — Nichtigkeitsklage zum EuG, Frist 2 Monate

### Testakte (neu)

- **`testakten/dsa-dma-bayrische-baustube-meissner/`** — fragmentarische Akte mit 17 Dokumenten verschiedener Formate (.md, .csv, .eml). Mandantin Baustube Meissnerlein GmbH, Hoechstadt an der Aisch. Konstellation: Account-Sperre auf US-Plattform "Glitzerwald", parallel VLOP-Designations-Streit, Mitbewerber Lindheim & Soehne KG Schwabach mit Verdacht auf Self-Preferencing, Art.-40-DSA-Forschungsantrag Dr. Vogelbroich (FAU Erlangen), Zustellungsproblem Art. 13 DSA EU-Vertreter Dublin.
- **`testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/`** — fragmentarische Akte mit 15 Dokumenten zum KI-Vorwurf bei Sachverstaendigengutachten (PV-Anlage Werkmangel, Sachverstaendiger Pfaffenberger). Anbindung an LG-Darmstadt-Linie (§ 407a Abs. 1 ZPO; § 8a Abs. 2 S. 1 Nr. 1 und Nr. 2 JVEG).

### BetrVG-Heilung und Ersatzmitglieder

Neue Skills in `arbeitsrecht` und `fachanwalt-arbeitsrecht`:

- `betriebsrat-ladung-und-ersatzmitglieder-pruefen` (arbeitsrecht)
- `betriebsrat-beschluss-heilung-nachtraeglich` (arbeitsrecht)
- `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` (fachanwalt-arbeitsrecht)

Eingearbeitet: BAG 25.09.2024 — 7 ABR 37/23 (Heilung Betriebsratsbeschluss; Vorinstanz LAG Nuernberg 27.09.2023 — 2 TaBV 8/23), BAG 20.05.2025 — 1 AZR 35/24 (Nachladung Ersatzmitglied).

### Schriftform und qES — Befristung

Neuer Skill in `schriftform-und-textform-bgb`:

- `befristungsabrede-qes-rechtsprechung-stand-2026` — LAG Berlin-Brandenburg 16.03.2022 — 23 Sa 1133/21 (gescannte Unterschrift wahrt § 14 IV TzBfG nicht), ArbG Berlin (einfache elektronische Signatur unwirksam), ArbG Gera 07.03.2024 — 2 Ca 936/23 (qES per DocuSign wahrt Schriftform).

### Maklerskill BGH I ZR 202/25 — voll ueberarbeitet

`maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` komplett neu geschrieben mit 4 verifizierten Leitsaetzen: E-Mail-Austausch erfuellt Textform auch auf getrennten Datentraegern; konkludenter Abschluss moeglich; Erklaerungsende muss erkennbar sein; Bereicherungsanspruch des Maklers gesperrt bei Textformverstoss. Falsche Lehrsaetze der Vorversion ersetzt.

### KI-Vorwurf bei Sachverstaendigengutachten

Drei neue Skills mit verschiedener Perspektive auf die LG-Darmstadt-Linie:

- `kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` (Anwalts-Generalist)
- `grosskanzlei-corporate-ma/skills/ki-einsatz-bei-gutachten-mandatsseite` (Beratungsseite)
- `jveg-kostenpruefer/skills/pruefung-sachverstaendigengutachten-ki-deklaration` (Kostenpruefer, festsetzungs-orientiert)

### Plugin-Fusion: kanzlei-allgemein in kanzlei-allgemein

Das Plugin `kanzlei-allgemein` wurde vollstaendig in `kanzlei-allgemein` fusioniert. Alle 14 Cowork-Skills sind erhalten und werden ab v11.0.0 unter `kanzlei-allgemein/skills/` ausgeliefert: `aktenbestand-pflege`, `bea-versand-pruefen`, `fristenbuch-fuehren`, `geburtstage-feiertage`, `kanzlei-allgemein-kaltstart-interview`, `mahnwesen-honorar`, `mandantenakte-anlegen`, `mandantenbrief-vorlagen`, `posteingang-ausgang`, `rechnungserstellung-rvg` (inkl. Werkzeug `rvg_gebuehrenrechner.py`), `sekretariats-tagesbrief`, `timesheet-aktenzeitung`, `versand-vor-check`, `weihnachtskarten`. Das Stand-Alone-Plugin `kanzlei-allgemein` ist entfallen.

### Repo-Stand v11.0.0

- 98 Plugins (99 minus Cowork-Fusion plus DSA/DMA)
- marketplace.json mit 98 Eintraegen, alle auf 11.0.0
- 98 plugin.json-Dateien einheitlich auf 11.0.0
- 45 Testakten (vorher 43 plus 2 neu)
- QA: kein `\d,\d` in plugin.json/description und SKILL.md/description; Skill-Namen alle ≤ 64 Zeichen; Plugin-Descriptions alle ≤ 300; Skill-Descriptions alle ≤ 1024; Steuer-Plugin-Konvent eingehalten (Frontmatter ASCII)

### QA-Vorlauf (Commit `69f627c0`)

- Aktenzeichen-Korrekturen in 14 Dateien: II ZR 88/13 → II ZR 88/99; IX ZR 92/04 → IX ZR 228/03; 3 AZR 18/12 → 3 AZR 303/18

# Changelog

Alle wesentlichen Änderungen an diesem Repository werden hier dokumentiert. Format orientiert an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/), Versionierung nach [SemVer](https://semver.org/lang/de/).

## v8.0.0 — 2026-05-25 — Steuer-Plugin Härtung + Codex-Audit-Welle

### Major-Update
- Versionsfelder repo-weit auf 8.0.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

### Steuer-Plugin Erweiterung (PR #70, #71)
- Neuer Skill **`anw-insolvenzreife-pruefung-17-19-inso`** (210 Zeilen): §§ 17, 19 InsO aus Steueranwalts-Sicht mit § 222 AO Stundung, § 361 AO AdV, § 69 AO GF-Haftung Lohnsteuer, § 266a StGB, BGH IX ZB 50/03, IDW S 11, SanInsKG 24-Monats-Prognose.
- **`stb-warnschreiben-krisensignale`** um Abschnitt "Warum gerade der Steuerberater" und "§ 102 StaRUG als Auslöser der StB-Hinweispflicht" erweitert — Steuerberater als externer Bestandteil des Krisenfrüherkennungssystems.
- **Generalueberholung mit sechs neuen Skills**: `anw-stundung-erlass-vollstreckungsaufschub`, `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern`, `anw-organschaft-konzern-grundlagen`, `anw-grunderwerbsteuer-share-deal-90-prozent`, `anw-dac7-dac8-plattformen-krypto`, `anw-minbestg-pillar2-konzernbesteuerung`, `stb-drv-sozialversicherungspruefung`.

### Juristische Korrekturen (Codex-Audit-Welle PR #72–#76)
- **§ 361 AO AdV ist keine Stundung** (PR #72, #74): AdV hemmt nur die Vollziehung, lässt die Fälligkeit unberührt. AdV-Beträge bleiben Passiva I bei der § 17 InsO-Prüfung. Nur die echte Stundung nach § 222 AO verschiebt die Fälligkeit. Korrektur in `anw-insolvenzreife-pruefung-17-19-inso` und 5 weiteren Liquiditätsprüfer-Skills (`insolvenzrecht/zahlungsunfaehigkeit-pruefung-17-inso`, `insolvenzrecht/liquiditaetsvorschau-insolvenzrechtlich`, `liquiditaetsplanung/liquiditaetsvorschau-3wochen`, `liquiditaetsplanung/liquiditaetsvorschau-insolvenzrechtlich`, `steuerrecht-anwalt-und-berater/stb-liquiditaetsvorschau-3wochen`).
- **§ 393 Abs. 2 AO Verwendungsverbot nur für steuerfremde Straftaten** (PR #73): Korrigiert in `anw-steuerstrafverteidigung-verstaendigung`. Für die Steuerstraftat selbst sind Steuerakten verwertbar (BGH 5 StR 191/04; Joecks/Jaeger/Randt, Steuerstrafrecht, 8. Aufl. 2015, § 393 Rn. 81 ff.). § 30 AO schafft kein Verwendungsverbot. § 136a StPO als realer Verteidigungsansatz ergänzt.
- **§ 393 Abs. 1 S. 2 AO nur Zwangsmittelverbot** (PR #75): Präzisiert in `anw-steuerstrafverteidigung-verstaendigung`. Setzt die steuerlichen Mitwirkungspflichten **nicht** generell außer Kraft, sondern verbietet nur den Einsatz von Zwangsmitteln (§ 328 AO) soweit Selbstbelastungsgefahr. §§ 90, 93, 200 AO bestehen fort; Schätzung § 162 AO und Steuererklärungspflicht bleiben.
- **GrESt-Konzernklausel ist § 6a GrEStG** (PR #76): Korrigiert in `anw-grunderwerbsteuer-share-deal-90-prozent` zweifach. § 6a GrEStG begünstigt Umwandlung/Einbringung im Konzern (95 % Beteiligung, 5 Jahre Vor- und Nachbehaltensfrist). § 7 GrEStG regelt dagegen den Übergang von Gesamthand zu Bruchteilseigentum.
- **GIR-Erstabgabe 18 Monate** (PR #76): Korrigiert in `anw-minbestg-pillar2-konzernbesteuerung`. Übergangsregelung nach § 95 Abs. 1 MinStG i.V.m. Art. 44 Abs. 7 EU-RL 2022/2523. Kalenderjahrgleicher Konzern GJ 2024 → Frist 30.6.2026. Folgejahre weiter 15 Monate.

### Tooling und Cleanup (PR #77, #78)
- ASSET_INDEX.md auf Stand v8.0.0 angehoben, Plugin-Counts repo-weit konsistent: 97 Plugins / 43 Fallakten / 1 Manifest = 141 Release-Assets.
- Repo-Sanity-Sweep durchgeführt: Validator, Marketplace, Skill-Struktur (1.643 Skills), Symlinks, README-Referenzen — alle Prüfungen OK.

## v7.1.0 — 2026-05-24 — Steuer-Plugin-Konsolidierung + ELSTER-Klarstellung

### Major-Feature
- Drei Steuer-Plugins (`steuerrecht-kanzlei`, `fachanwalt-steuerrecht`, `steuerberater-werkzeuge`) zu einem konsolidierten Plugin **`steuerrecht-anwalt-und-berater`** zusammengeführt. 18 Skills mit Präfix-Schema `anw-`/`fa-`/`stb-`: 13× Steueranwalt (Kaltstart-Interview, Mandat-Triage, Steuerbescheid-Analyse, Einspruch ans Finanzamt, AdV, Klage Finanzgericht, Akteneinsicht, Außenprüfung, Selbstanzeige § 371 AO, verbindliche Auskunft § 89 II AO, Fristenbuch, Betriebsausgaben/Werbungskosten-Prüfraster, USt-Vorsteuerabzug), 1× FA-Orientierung, 4× Steuerberater (Kaltstart-Interview, BWA/SuSa/Bilanz, 3-Wochen-Liquiditätsvorschau, 3-/6-/12-Monats-Vorschau). Vier inhaltliche Dubletten (Einspruch, Außenprüfung, Selbstanzeige, verbindliche Auskunft) zu jeweils einem Master-Skill gemergt. Repo-Plugin-Anzahl: 99 → 97.

### Juristische Korrekturen
- **ELSTER/ERiC statt beA an Finanzämter** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Versandwege in Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige und verbindlicher Auskunft umgestellt. beA an Finanzbehörden ist unzulässig — ein per beA eingelegter Einspruch wäre formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenüber Finanzgerichten (§ 52d FGO).
- **Triage-Routing-Slugs** im konsolidierten Plugin auf die neuen Skill-Slugs umgestellt; **ASSET_INDEX**-Dubletten bereinigt; **`stb-`-Sister-Skill-Verweise** auf die konsolidierten Pfade aktualisiert.

### Tooling
- Versionsfelder repo-weit auf 7.1.0 angehoben: 97 `plugin.json`-Dateien plus die zentrale `.claude-plugin/marketplace.json` mit 97 Plugin-Einträgen. Summe: 195 Versions-Stellen in 98 Dateien.
- `release-plugin-zips.yml` erzeugt nach dem Tag-Push 97 Plugin-ZIPs + 43 Testakten-ZIPs + `marketplace.json` = 141 Release-Assets.

## v7.0.0 — 2026-05-24 — Reform-Stand 2026

### Major-Update
- Versionsfelder repo-weit auf 7.0.0 vereinheitlicht: 99 `plugin.json`-Dateien (je ein `version`-Feld) plus eine zentrale `.claude-plugin/marketplace.json`, die ihrerseits 99 Plugin-Einträge mit `version`-Feld enthält. Summe: 99 + 1 Manifest-Datei mit 99 internen Versions-Einträgen = 198 angefasste Versions-Stellen in 100 Dateien.

### Inhaltliche Aktualisierungen
- **Wandeldarlehen-Plugin** auf Reform-Stand 05/2026 angehoben (DiRUG 2022/2023, SanInsFoG 1.1.2021, PostModG 1.1.2025, GesLV, Transparenzregister).
- **Steuerrecht** aktualisiert: WtcG-Gebühren, eRechnung-Pflicht ab 1.1.2025 (§ 14 UStG), § 153 AO; Selbstanzeige-Dublette entfernt; § 398a AO Zuschlagsstaffel ergänzt.
- **liquiditaetsplanung**: openpyxl-Dependency komplett entfernt; Kanzleien starten `build_liquiditaetsplan.py` ohne `pip install` (Stdlib-XLSX-Writer mit Live-Formeln, Styles, DXF-Solid-Fills, Conditional Formatting, Freeze Panes).

### Juristische Korrekturen
- **ELSTER/ERiC statt beA gegenueber Finanzbehoerden** (§ 87a Abs. 1 S. 2 AO n.F., JStG 2024, seit 6.12.2024): Im neuen konsolidierten Steuer-Plugin alle Stellen umgestellt, an denen Einspruch, AdV-Antrag, Akteneinsicht, Selbstanzeige oder verbindliche Auskunft per beA an das Finanzamt empfohlen wurden. beA an Finanzbehoerden ist unzulaessig; ein per beA eingelegter Einspruch ist formunwirksam und wahrt die Frist nicht (Nds. FG 12.2.2026 – 2 K 152/25). beA bleibt Pflicht gegenueber Finanzgerichten (§ 52d FGO).
- **§ 44 DSGVO → § 44 BDSG i.V.m. Art. 79 DSGVO**: Vier Arbeitsrechts-Skills zitierten eine nicht existierende DSGVO-Norm. Die DSGVO hat nur Artikel; § 44 BDSG ist die deutsche Norm für die Gerichtszuständigkeit. Vier weitere DSGVO-Verweise (Art. 8, 13, 34, 37 DSGVO) von `§` auf `Art.` umgestellt.
- **kongruent (lat. *congruens*)**: Phase-2-Umlauten-Patch hatte den etablierten Fachbegriff "kongruente / inkongruente Deckung" (§ 130/131 InsO) fälschlich umlautiert. 17 Dateien, 67 Korrekturen.
- **§ 57 II GmbHG statt § 19 GmbHG**: Codex-Befund — falscher Normverweis in `sacheinlagebericht-werthaltigkeit` (Wandeldarlehen-Plugin) korrigiert; § 57 II GmbHG i.V.m. § 8 II GmbHG ist die korrekte Anker-Norm für die GF-Versicherung in der HR-Anmeldung der Kapitalerhöhung.
- **§ 153 AO ist Berichtigungspflicht — KEINE Strafbefreiung**: Codex-P1-Review von PR #60. In `anw-selbstanzeige-371` stand fälschlich, § 153 AO wirke strafbefreiend. Korrekt: § 153 AO ist eine rein steuerliche Berichtigungspflicht ohne strafrechtliche Sperrwirkung; Strafbefreiung folgt allein aus § 371 AO (Vorsatz) bzw. § 378 III AO (Leichtfertigkeit). Drei-Stufen-Bewertung der Ursprungserklärung ergänzt; Praxisempfehlung: bei Zweifeln zusätzlich Selbstanzeige-Weg erfüllen.
- **Stale Skill-Slug-Verweise** behoben: `datenpannenmeldung → datenpanne-meldung`, `auskunftsersuchen-art-15-dsgvo → dsgvo-auskunft`.

### Repo-Polish
- Umlauten-Polish in SKILL.md-Bodies und references/ (531 Dateien, 5017 Korrekturen); YAML-Frontmatter, Eigennamen, Slugs, URLs, Code-Blocks geschützt.
- Skill-Slugs (Verzeichnisnamen) bleiben ASCII; nur Fließtext umlautiert.
- README-Intro klargestellt: Plugin- und Skill-Sammlung; Beck-Verweise entfernt.
- Testakten-Hinweis im Überblick prominent platziert.

### Tooling
- `release-plugin-zips.yml` triggert automatisch auf Tag-Push; pro Release werden 99 Plugin-ZIPs (aus `.claude-plugin/marketplace.json`) plus 43 Testakten-ZIPs (mit `testakte-`-Prefix, separat aus `testakten/*/` verpackt) plus `marketplace.json` als Manifest erzeugt — zusammen 143 Release-Assets.
- Validator (`scripts/validate-plugin-structure.mjs`) bleibt grün.
