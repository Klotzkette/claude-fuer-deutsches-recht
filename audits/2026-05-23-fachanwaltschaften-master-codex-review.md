# Codex-Audit-Anfrage 2026-05-23: Alle 24 Fachanwalts-Plugins

@codex review

## Kontext und Ziel

Das Repo enthaelt 24 Fachanwalts-Plugins mit insgesamt rund 152 Skills, die
deutsche Rechtsanwaeltinnen und Rechtsanwaelte bei der typischen
fachanwaltlichen Mandatsarbeit unterstuetzen sollen. Vom
Mandantengespraech über Anspruchsgrundlagenpruefung bis zum
Schriftsatzentwurf.

**Ziel dieses Audits:** Die Skills sollen **juristisch praeziser** und
**praxisnaeher hilfreicher** werden. Das ist ein **Master-Audit über
alle Fachanwaltschaften** mit der Bitte, **direkt im selben PR** konkrete
Verbesserungen einzucommitten.

## Prüfungsgegenstand

Alle Verzeichnisse `fachanwalt-*` (24 Plugins). Eine vollstaendige
Plugin- und Skill-Inventur findet sich in
`audits/2026-05-23-fachanwaltschaften-inventur.md`.

Plugins (alphabetisch):

1. fachanwalt-agrarrecht
2. fachanwalt-arbeitsrecht
3. fachanwalt-bank-kapitalmarktrecht
4. fachanwalt-bau-architektenrecht
5. fachanwalt-erbrecht
6. fachanwalt-familienrecht
7. fachanwalt-gewerblicher-rechtsschutz
8. fachanwalt-handels-gesellschaftsrecht
9. fachanwalt-insolvenz-sanierungsrecht
10. fachanwalt-internationales-wirtschaftsrecht
11. fachanwalt-it-recht
12. fachanwalt-medizinrecht
13. fachanwalt-miet-wohnungseigentumsrecht
14. fachanwalt-migrationsrecht
15. fachanwalt-sozialrecht
16. fachanwalt-sportrecht
17. fachanwalt-steuerrecht
18. fachanwalt-strafrecht
19. fachanwalt-transport-speditionsrecht
20. fachanwalt-urheber-medienrecht
21. fachanwalt-vergaberecht
22. fachanwalt-verkehrsrecht
23. fachanwalt-versicherungsrecht
24. fachanwalt-verwaltungsrecht

## Prüfdimensionen

Bitte je Skill und je Plugin prüfen und **direkt Verbesserungen
committen**, wo sinnvoll:

### Dimension 1 — Juristische Praezision

- **Paragrafen-Verweise:** Sind die zitierten Normen aktuell, korrekt
  bezeichnet und beziehen sich auf die richtige Fassung? Beispiele:
  - § 313 BGB statt § 242 BGB bei Stoerung der Geschäftsgrundlage
  - § 1626a BGB bei gemeinsamer Sorge unverheirateter Eltern
  - § 17 InsO Zahlungsunfaehigkeit vs § 19 InsO Ueberschuldung
  - Art. 6 / Art. 9 DSGVO statt § DSGVO (kein Paragraf!)
- **BGH/BVerfG-Zitate:** Existieren die zitierten Urteile? Aktenzeichen
  prüfen. Gibt es neuere Leitentscheidungen, die zitiert werden
  sollten?
- **Aktuelle Gesetzeslage:** Wurde z.B. das Hinweisgeberschutzgesetz,
  MoPeG, KStG-Reformen, PflPostG, neue ZPO-Änderungen,
  Mietrechtsanpassungen, Cannabis-Gesetz beruecksichtigt, wo relevant?
- **Fristen:** Sind die genannten Fristen korrekt (z.B. § 626 II BGB
  zwei Wochen, § 4 KSchG drei Wochen, § 45 WEG Beschlussanfechtungsfrist (ein Monat Klage, zwei Monate Begruendung), § 558b BGB)?
- **Zustaendigkeiten:** Amtsgericht vs Landgericht, sachliche und
  oertliche Zustaendigkeit, Streitwertgrenzen.

### Dimension 2 — Praxisrelevante Hilfestellung

- **Mandantengespraech-Checklisten:** Welche Fakten muss die Anwaeltin
  als erstes erfragen? Sind die Checklisten vollstaendig genug, um nach
  dem Erstgespraech tatsaechlich weiterarbeiten zu können?
- **Anspruchsgrundlagen-Prüfschemata:** Sind die Prüfungsreihenfolgen
  korrekt und vollstaendig? Beispiel Arbeitsrecht:
  Kuendigungsschutzklage muss § 4 KSchG-Frist, § 1 KSchG-Anwendbarkeit
  (Schwellenwerte, Wartezeit), Kuendigungsgruende, Sozialauswahl,
  Anhoerung Betriebsrat § 102 BetrVG durchpruefen.
- **Schriftsatz-Bausteine:** Sind die Textbausteine für
  Klageschriften, Beschwerden, Widersprueche so formuliert, dass sie
  direkt verwendbar sind?
- **Tenor-Vorschlaege:** Bei Skills mit Klageantraegen — sind die
  Antraege korrekt formuliert (Leistungsantrag, Feststellungsantrag,
  Gestaltungsantrag)?
- **Streitwert-Berechnung:** Sind die Streitwert-Hinweise korrekt
  (§§ 3 ff ZPO, § 48 GKG, RVG)?

### Dimension 3 — Workflow-Konsistenz

- **Skill-IDs in Handoffs:** Verweisen Skills auf andere Skills mit
  korrekten IDs? Codex hat in PR #15 bereits nicht-existente
  Skill-Verweise gefunden — gibt es weitere?
- **Mandat-Triage:** Plugins mit `mandat-triage-*`-Skills — fuehren
  diese sinnvoll in die fachspezifischen Skills?
- **Orientierungs-Skills:** Geben die `*-orientierung`-Skills einen
  brauchbaren Einstieg in das Fachgebiet?

### Dimension 4 — Format und Stil

- **DSGVO-Verweise:** Immer `Art.`, **nie** `§`.
- **Komma-Zahlen:** Der Validator verbietet `\d\s*,\s*\d` ausschließlich
  in Skill-`description`-Frontmatter und Plugin-Manifest-`description`. Im
  SKILL.md-Body sind juristische Komma-Zahlen (z.B. `1,5 Promille`,
  `12,5 Prozent`) erlaubt und sollen nicht ohne Not umgeschrieben werden.
- **Skill descriptions:** ≤1024 Zeichen, einzeilig, in Quotes, nur
  `name` + `description` im Frontmatter.
- **Frauenfreundliche Sprache:** Schraegstrich-Form
  `Mandant/-innen`, konsistent durchgehend.
- **Keine Werbe-Floskeln:** "umfassend", "schnell", "einfach" — eher
  praezise juristische Sprache.

### Dimension 5 — Vollstaendigkeit

- **Fehlende Standard-Skills:** Welche typischen Mandate eines
  Fachgebiets fehlen noch? Beispiele:
  - Arbeitsrecht: AGG-Entschaedigung, Aufhebungsvertrag-Verhandlung,
    Arbeitszeugnis
  - Erbrecht: Erbausschlagung-Frist, Vorerbschaft-Nacherbschaft
  - Familienrecht: Versorgungsausgleich-Berechnung, Sorgerechts-Antrag
  - Mietrecht: Mietminderung-Tabelle, Eigenbedarfskuendigung,
    Schoenheitsreparaturen
- **Plugins mit nur 4 Skills (arbeits, gewerbl, handels, insolvenz,
  miet, sozial, steuer):** Hier ist Ausbau besonders sinnvoll.

## Konkrete Bitte

1. **Reviewe systematisch** alle 24 Fachanwalts-Plugins entlang der
   Dimensionen.
2. **Committe direkt** in diesen Branch konkrete Verbesserungen:
   - Korrekturen falscher Paragrafen-Verweise
   - Erweiterungen von Prüfschemata
   - Neue Skills, wo offensichtlich Luecken bestehen
   - Format-Fixes (Komma-Zahlen, DSGVO-Art)
3. **Halte den Author-Standard ein:**
   - `user.name=Klotzkette`
   - `user.email=39582916+Klotzkette@users.noreply.github.com`
   - Keine Erwaehnung von Claude/AI/Codex/GPT/LLM/Sprachmodell in
     Commits oder Plugin-Inhalten.
4. **Validator-Konformitaet:**
   - `\d\s*,\s*\d` in plugin.json-`description` + SKILL.md-`description`
     **verboten** (Validator-Regel). Im SKILL.md-Body sind Komma-Zahlen
     erlaubt. In marketplace.json ebenfalls erlaubt.
   - Skill descriptions ≤ 1024 Zeichen, einzeilig, in Quotes.
   - Plugin descriptions ≤ 300 Zeichen.
   - Skill-Namen Regex `[a-z0-9-]{1,64}`, name == Verzeichnisname.
   - Plugin author MUSS Objekt sein: `{"name": "Klotzkette"}`.
   - Neue Plugins/Skills alphabetisch in marketplace.json /
     plugin.json einsortieren.

## Schweregrade für Findings

- **P1 — juristisch falsch:** Verweis auf nicht existente Norm,
  falsches Fristenmaass, falsche Zustaendigkeit, falsches BGH-AZ,
  falsche Anspruchsgrundlage. **MUSS gefixt werden.**
- **P2 — handwerklicher Mangel:** Unvollstaendiges Prüfschema,
  fehlender Standard-Anspruch, ungenauer Textbaustein. **SOLL gefixt
  werden.**
- **P3 — Stil/Format:** Formulierung, Schreibweise, Komma-Zahlen,
  Gendern. **KANN gefixt werden.**

## Was passiert nach dem Review

- P1-Fixes werden gemerged.
- P2-Fixes werden begutachtet und in der Regel uebernommen.
- P3-Fixes sind willkommen, können aber gesammelt nachgezogen werden.
- Falls Codex auf einzelne Plugins separate Folge-Audits empfiehlt,
  bitte das als Kommentar markieren.

Vielen Dank für die gruendliche Prüfung.
