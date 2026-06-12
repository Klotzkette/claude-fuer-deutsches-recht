# Codex-Instruktion: Skill-Tiefe-Boost auf Anthropic-Niveau

**Adressat:** Codex (oder ein anderer ausfuehrender Agent)
**Auftraggeber:** Tom Braegel
**Ziel:** Skills im Repo claude-fuer-deutsches-recht **selektiv** auf das
Tiefe-Niveau von anthropics/claude-for-legal bringen - **ohne generisches
Aufpumpen**. Stattdessen: praezise, rechtsgebietsspezifisch, mit echten Normen,
Rechtsprechung, Workflowschritten und Negativ-Abgrenzungen.

**WICHTIG - LIES ZUERST:**
`CODEX-SELEKTION-welche-skills-tief.md` (selbe Ordner). Dort steht, **welche**
Plugins/Skills auf Anthropic-Tiefe gehoeren (Klasse A - rund 70 Plugins,
Grosskanzlei/Inhouse-Counsel/MCP-anbindbar/mandatsbegleitend), welche nur einen
Teilausbau bekommen (Klasse B) und welche **kurz bleiben müssen** (Klasse C -
Verbraucher-Selbsthilfe, Tool-Skills, Studium). Wende die untenstehenden
Pflicht-Sektionen NUR auf Klasse A in voller Tiefe an.

**Anthropic-Repo zum Selbst-Nachschauen:**
https://github.com/anthropics/claude-for-legal
Schau dir gerne selbst nochmal an, wie Anthropic seine Skills strukturiert -
vor allem `litigation-discovery/skills/`, `transactional-ma/skills/`,
`legal-research/skills/`, `cold-start-interview/`, `customize/`,
`matter-workspace/` und `managed-agent-cookbooks/`. Das ist der Maßstab.
**Anthropic schreibt für US-Grosskanzleien und Inhouse-Counsel mit
MCP-Anbindung an Westlaw, CourtListener, iManage, Slack und Mandanten, die
ein Skill ein ganzes Mandantenleben begleitet** - daher die Laenge. Wir uebernehmen
das Modell nur dort, wo dieser Kontext bei uns passt.

**Branch:** Diese Instruktion liegt auf `anthropic-patterns-experimente`.
Codex arbeitet auf einem eigenen Branch davon, z.B. `codex-skill-boost-batch-N`.
Niemals direkt in `main` mergen, ohne Tom zu fragen.

**Autor-Identitaet:** `Klotzkette / 39582916+Klotzkette@users.noreply.github.com`
Keine Claude/AI/Codex-Erwaehnung in Commit-Messages.

---

## 0. Grundregeln (HARD CONSTRAINTS)

Diese Regeln sind nicht verhandelbar. Verletzung = Validator-Fehler = PR
abgelehnt.

1. **Niemals den Pfad `/home/user/workspace/claude-fuer-deutsches-recht`
   anfassen.** Codex arbeitet auf einem Workclone unter `/tmp/...`.

2. **Frontmatter-Whitelist.** Erlaubt sind in SKILL.md NUR:
   `name`, `description`. Verboten: `triggers`, `when_to_use`, `language`,
   `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`,
   `allowed_tools`, `tools`, `model`, `adapted_from`, `version`,
   `related_skills`. (Wir können `argument-hint` später freischalten, aber
   nicht in diesem Batch.)

3. **`description` <= 1024 Zeichen, ASCII-kompatibel.**
   - Verboten in `description`: `\d\s*,\s*\d` (Komma-Zahl-Falle),
     XML-Pfeil `->` oder `<-`, doppelte Anfuehrungszeichen `"` darin.
   - Body (unter dem Frontmatter) darf alles enthalten - hier sind Umlaute,
     Sonderzeichen und lange Saetze in Ordnung.

4. **`name` <= 64 ASCII kebab-case.** Slug wird **niemals** geaendert.
   Wir benennen keine bestehenden Skills um.

5. **Plugin-Namen werden niemals umbenannt.**

6. **Quellenregel:** Erlaubt sind nur Zitate aus `dejure.org`, `openjur.de`,
   `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`.
   Verboten allein: `BeckRS`, `anwalt24.de`. Aufsaetze brauchen Verfasser,
   Zeitschrift, Jahr, Heft, Seite. Kommentare: Bearbeiter und Randnummer.

7. **Testakten anfassen ist tabu.** Alles unterhalb von
   `testakten/`, `beispielakte-*/`, `fluggastrechte-familie-braeutigam/`,
   `betreuung-hildegard-sauer/` etc. bleibt unveraendert. Diese Ordner haben
   bewusst KEIN YAML-Frontmatter.

8. **Bestehende Inhalte werden nicht geloescht.** Nur ergaenzt, vertieft,
   strukturiert. Wenn ein Skill bereits einen Abschnitt "Prüfraster" hat,
   wird der **ausgebaut**, nicht ersetzt.

9. **Validatoren MUESSEN gruen sein vor jedem Push:**
   ```bash
   python3 scripts/validate-yaml-frontmatter.py
   node scripts/validate-plugin-structure.mjs
   ```

10. **Bevor du pushst:** `git fetch origin main` und sicherstellen, dass du
    nicht Tom's parallele Arbeit ueberschreibst.

---

## 1. Zielprofil: was "Anthropic-Tiefe" konkret bedeutet

Anthropic-Skills sind im Median ~11.000 Zeichen, unsere ~4.500. Ziel:
**Median-Boost auf 9.000-11.000 Zeichen pro Skill**, aber NICHT durch Bullshit-
Fueller. Jeder neue Zeichen muss inhaltlich zaehlen.

### 1.1 Pflicht-Sektionen pro Skill (in dieser Reihenfolge)

Jeder Skill nach dem Boost hat **mindestens** diese Sektionen. Wenn eine schon
existiert, wird sie ausgebaut, nicht ueberschrieben.

```
# {Titel des Skills}

## Zweck
## Wann wird dieser Skill aufgerufen
## Voraussetzungen und Kontext laden
## Workflow (nummeriert, 5-12 Schritte)
## Pruefraster im Gutachtenstil
## Output-Module
## Quellen und Zitierregel
## Hand-Off zu anderen Skills
## Was dieser Skill nicht macht
## Berufsrechtliche Hinweise
```

Optional, wenn rechtsgebietsbedingt sinnvoll:

```
## Mandantenkommunikation
## Fristen-Logik
## Vergleich mit anderen Rechtsordnungen (nur EU/Common-Law-Bezug)
## Standardisierte Datei-Outputs (matter.md / history.md / chronology.md)
```

### 1.2 Was JEDE Sektion enthalten muss

**`## Zweck`** (200-400 Zeichen)
- Ein Satz "Wofuer ist dieser Skill da."
- Ein Satz "Welches typische Mandatsproblem loest er."
- Ein Satz "Welche Adressatengruppe (Anwalt, Referendar, Selbstvertreter, Verwalter, Studierende)."
- KEINE Werbung. KEIN Marketing-Sprech.

**`## Wann wird dieser Skill aufgerufen`** (300-600 Zeichen)
- Konkrete Trigger-Saetze, die der User typisch sagt:
  > "Ich bekomme eine Klage von ..."
  > "Soll ich Einspruch einlegen gegen ..."
  > "Wie prüfe ich ..."
- Auch Negativ: "Wenn der User stattdessen X fragt, gehoert das zu Skill Y."

**`## Voraussetzungen und Kontext laden`** (400-800 Zeichen)
- Welche Unterlagen sollten vorliegen (Bescheid, Vertrag, Schriftsatz, Akte).
- Welche Stammdaten brauchen wir (Mandantenrolle, Jurisdiktion, Frist).
- Wenn das Repo ein `matters/<slug>/matter.md`-Schema hat (siehe Sektion 4),
  hier referenzieren: "Lies `matter.md` falls vorhanden, sonst frage nach."
- Eine Kurzliste der Variablen, die im Workflow gebraucht werden.

**`## Workflow`** (1500-3500 Zeichen)
- 5-12 nummerierte Schritte.
- Jeder Schritt: knapp, aktiv formuliert, mit konkreter Aktion und konkretem
  Output.
- Beispiel-Stil:
  > 4. Frist berechnen. Prüfe Zustellungsdatum, Wochenende, Feiertag. Wenn
  >    ein Tag fehlt: Hinweis "Zustellung unklar - im Bundeszentralregister
  >    oder beim Mandanten nachfragen." Schreibe Frist im Format YYYY-MM-DD.
- Bei mehreren Faellen: Unterpunkte 4.1, 4.2 (z.B. für Kläger- vs Beklagten-
  Seite, für Verbraucher vs Unternehmer, für Eilfall vs Standardfall).

**`## Pruefraster im Gutachtenstil`** (1500-3000 Zeichen)
- Obersatz / Definition / Subsumtion / Zwischenergebnis pro Tatbestandsmerkmal.
- KEIN Anglo-Stil. Deutsches Gutachten.
- Konkrete Normen mit Absatz, Satz, Nummer.
- Konkrete Rechtsprechung mit Gericht, Datum, Aktenzeichen und prüfbarem
  Link auf dejure.org oder openjur.de.
- Wo BGH/BVerfG/EuGH einschlaegig: zwingend zitieren.

**`## Output-Module`** (300-800 Zeichen)
- Was soll der Skill am Ende produzieren:
  - Gutachten? (mit Aufbau)
  - Schriftsatz-Geruest? (mit Adressat, Rubrum, Antrag)
  - Tabelle/Checkliste?
  - Anschreiben an Mandant?
  - Erinnerungseintrag im `matter.md`?
- Jeweils stichpunktartig.

**`## Quellen und Zitierregel`** (300-500 Zeichen)
- Wiederholung der Repo-Regel: nur freie prüfbare Quellen, keine BeckRS-
  Allein, kein anwalt24.
- Konkrete Datenbanken pro Rechtsgebiet:
  - Insolvenzrecht: bundesgerichtshof.de, openjur.de
  - Verwaltungsrecht: bundesverwaltungsgericht.de, dejure.org
  - EU: curia.europa.eu, eur-lex.europa.eu
  - Verfassungsrecht: bundesverfassungsgericht.de
- Quellen-Tags: `[BGH-Datenbank]`, `[dejure.org]`, `[openjur.de]`,
  `[Web-Recherche - pruefen]`, `[Modellwissen - pruefen]`, `[Mandant]`.

**`## Hand-Off zu anderen Skills`** (200-500 Zeichen)
- Konkrete Plugin-Slash-Befehle als Folgeskills:
  > Nach diesem Skill weiter mit:
  > - `/fachanwalt-strafrecht:strafr-haftpruefung-haftbeschwerde-workflow`
  >   wenn der Mandant in U-Haft sitzt.
  > - `/aktenaufbereiter-strafrecht:akt-zeitstrahl-bauleiter`
  >   wenn ein Zeitstrahl benoetigt wird.
- Verwende **immer den vollen Pfad** `/<plugin>:<skill-name>`.

**`## Was dieser Skill nicht macht`** (400-900 Zeichen)
- 4-7 Punkte mit expliziter Negativ-Abgrenzung. Beispiel-Stil aus Anthropic:
  > - Ersetzt nicht das anwaltliche Mandatsverhaeltnis. Der Skill erstellt
  >   eine Vorlage, kein Mandatsangebot.
  > - Berechnet Fristen vorlaeufig. Endgueltig zaehlt das Gericht. Bei Eilfall
  >   immer mit eigener Frist-Berechnung gegenchecken.
  > - Trifft keine taktische Entscheidung. Verteidigungs- oder
  >   Klagestrategie waehlt der Anwalt, nicht der Skill.
- Dieser Abschnitt ist **wichtiger** als der Workflow. Er verhindert
  Halluzinations- und Berufsrechtsschaeden.

**`## Berufsrechtliche Hinweise`** (300-600 Zeichen)
- § 43a BRAO Schweigepflicht bei Drittakten.
- § 49b BRAO Honorarvereinbarung wenn der Skill ein Anschreiben generiert.
- § 3 RDG bei Nicht-Anwaelten (Verbraucherzentrale-Skills, Studi-Skills).
- DSGVO Art. 6 wenn personenbezogene Daten verarbeitet werden.
- Standardsatz: "Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen
  Hinweis an den fallfuehrenden Anwalt."

---

## 2. Rechtsgebietsspezifische Tiefe (KEIN GENERISCHES AUFPUMPEN)

Das ist der entscheidende Punkt. Boost passiert NUR mit echtem Fach-Inhalt.
Pro Rechtsgebiet ein Cheat-Sheet, was hineingehoert.

### 2.1 Strafrecht / OWi

- **Normen-Mindestkern:** §§ 46 StGB Strafzumessung, § 153/153a StPO
  Verfahrenseinstellung, § 257c StPO Verstaendigung, § 407 StPO Strafbefehl,
  §§ 112 ff. StPO U-Haft, § 24 StGB Ruecktritt.
- **Verfahrensphasen:** Ermittlungs- / Zwischen- / Hauptverfahren / Rechtsmittel
- **Akteneinsicht:** § 147 StPO mit Implied Undertaking
- **Pflicht-Rechtsprechung:** BGHSt-Bezuege, BVerfG zu fairem Verfahren,
  EGMR zu Art. 6 EMRK.

### 2.2 Insolvenzrecht

- **Normen:** § 17 (ZU), § 19 (Ueberschuldung), § 15a (Antragspflicht),
  §§ 129 ff. (Anfechtung), §§ 270 ff. (Eigenverwaltung).
- **StaRUG-Kontext:** Frueherkennung § 1 StaRUG, Restrukturierungsplan
  §§ 9 ff., Stabilisierung §§ 49 ff.
- **Pflicht-Rechtsprechung:** BGHZ zu Vorsatzanfechtung, zu Cash-Pool,
  zu Eigenverwaltung-Bescheinigung nach § 270d.
- **Praxis:** IDW S 11 (Fortbestehensprognose), IDW S 6 (Sanierungskonzept).

### 2.3 Mietrecht / WEG

- **Normen:** §§ 535-580a BGB (Wohnraum), §§ 555a-559b (Modernisierung),
  §§ 573 ff. (Kuendigung), § 556 (Betriebskosten); WEG nach Reform 2020.
- **Pflicht-Rechtsprechung:** BGH zu Schoenheitsreparaturen, zu
  Eigenbedarfskuendigung, zu Betriebskostenabrechnung-Formalitaet.
- **Schnittstellen:** Mietminderung & Mangel-Anzeige; Sozialklausel
  § 574 BGB.

### 2.4 Arbeitsrecht

- **Normen:** KSchG, BetrVG, AGG, NachweisG (Reform 2022), TzBfG, TVG,
  ArbZG, ArbSchG.
- **Pflicht-Rechtsprechung:** BAG-Entscheidungen zu KSchG-Anhoerung,
  Betriebsuebergang, AGG-Massregelung, Equal Pay (EuGH).
- **Verfahren:** Guetetermin / Kammertermin / Berufung LAG / Revision BAG.

### 2.5 Familien- / Erbrecht

- **Normen:** BGB Buecher 4 + 5, FamFG, VersAusglG, GNotKG.
- **Pflicht-Rechtsprechung:** BGH zu Pflichtteil, Versorgungsausgleich,
  Zugewinnausgleich; OLG-Rspr zum Umgang.
- **Verfahrensbesonderheit:** Beteiligten-Logik FamFG statt Kläger-/Beklagten-
  Schema.

### 2.6 Verwaltungs- / Verfassungsrecht

- **Normen:** VwVfG, VwGO, BVerfGG, GG.
- **Pflicht-Rechtsprechung:** BVerwG, BVerfG-Leitentscheidungen
  (Verhältnismäßigkeit, Bestimmtheit).
- **EU-Bezug:** EuGH C-Az zu Grundrechtecharta, Vorlagepflicht Art. 267 AEUV.

### 2.7 Datenschutz / IT / KI

- **Normen:** DSGVO, BDSG, AI Act (VO 2024/1689), DSA, DMA, NIS2,
  IT-SiG 2.0, TTDSG.
- **Pflicht-Rechtsprechung:** EuGH zu Schrems II, Bonifei, Meta-Bagatell,
  Art. 82-DSGVO-Schaden.
- **Verfahren:** Beschwerde § 77 DSGVO, Bussgeldverfahren OWiG +
  Art. 83 DSGVO, KRITIS-Meldepflichten BSI.

### 2.8 Wettbewerb / IP

- **Normen:** UWG, MarkenG, UrhG, PatG, GeschGehG, GeschmMG, GWB.
- **Pflicht-Rechtsprechung:** BGH I ZR-Reihe (UWG), EuGH zu unlauterer
  Vergleichswerbung, Huawei/ZTE-FRAND.
- **Verfahren:** Schutzschrift, einstweilige Verfuegung, Abmahnung-/
  Unterlassungserklaerung-Stufenmodell.

### 2.9 Verbraucher- / Verkehrsrecht

- **Normen:** §§ 312 ff. BGB (FAGG), §§ 433 ff. BGB Kauf, § 7 StVG,
  § 115 VVG, ProdHaftG, GPSR.
- **Pflicht-Rechtsprechung:** BGH-Dieselkomplex VI ZR-Reihe, BGH zu
  Sachmangel/Nacherfuellung; EuGH zu VO 261/2004 (Fluggast).
- **Praxis:** Schadensregulierung-Workflow Quote/Schadensposten.

### 2.10 Sozial- / Migrationsrecht

- **Normen:** SGB I-XII, AufenthG, AsylG, StAG, FreizuegG/EU.
- **Pflicht-Rechtsprechung:** BSG, EuGH C-Az zu Ziebell, Daueraufenthalt EU.
- **Verfahren:** Widerspruch / Klage SG / LSG / BSG; einstweiliger
  Rechtsschutz § 86b SGG.

### 2.11 Studium / Hausarbeiten / Examensvorbereitung

- **Hier kein materielles Recht boosten**, sondern Methodik:
  - Gutachtenstil vs Urteilsstil
  - Fussnotenstil deutsche Jurahausarbeit
  - Pflichtfachstoff vs Schwerpunkt
  - Klausurzeitmanagement
  - Prüfungsordnungen typischer Universitaeten

### 2.12 Wenn das Rechtsgebiet thematisch nicht eindeutig ist

Prüfe den Plugin-Namen. Wenn unklar:
1. Lies die ersten 50 Zeichen der Plugin-`.claude-plugin/plugin.json`-
   `description`.
2. Lies 3 zufaellige Skills aus dem gleichen Plugin.
3. Wenn immer noch unklar: **NICHT boosten**, sondern als Liste in
   `anthropic-lessons/UNCLEAR-SKILLS.md` ablegen und Tom fragen.

---

## 3. Praezise Anweisung an Codex - Iterativer Boost-Workflow

### 3.1 Batching-Strategie

3670 Skills sind zu viel für einen einzigen Boost-Lauf. Codex arbeitet in
**Plugin-Batches**:

- **Eine PR = ein Batch von 5-10 thematisch verwandten Plugins** (~100-200
  Skills).
- Insgesamt ~25-30 PRs nacheinander.
- Jede PR bekommt eigenen Branch `codex-skillboost-<thema>-batch-N`.

Empfohlene Reihenfolge (von einfach nach komplex, damit fruehe Batches als
Muster für spaetere dienen):

1. Methodik/Studi-Plugins (jurastudium, hausarbeitenmacher, methodenlehre,
   zitierweise-deutsches-recht)
2. Verkehrsrecht (verkehrsrecht, verkehrsowi-verteidiger, fluggastrechte)
3. Mietrecht / WEG / Nachbarschaft
4. Arbeitsrecht
5. Familien- / Erbrecht
6. Insolvenzrecht / Sanierung / StaRUG
7. Strafrecht / OWi / Strafbefehl
8. Verwaltungsrecht / Sozialrecht / Migration
9. Datenschutz / IT / KI / Plattformregulierung
10. Wettbewerb / IP / Urheber / Marken
11. Wirtschaftsrecht / Gesellschaftsrecht / Bank
12. Methodik-und-Office-Skills (NDA-Abgleich, Vertragsausfueller etc.)

### 3.2 Pro Skill - Schritt-für-Schritt-Algorithmus für Codex

```
fuer plugin in batch:
  fuer skill in plugin/skills/:

    # Schritt A: Skill-Analyse
    1. Lies aktuelle SKILL.md komplett.
    2. Extrahiere bestehende Sektionen, Normen-Erwaehnungen, Rechtsprechungs-
       Zitate, Output-Module.
    3. Pruefe: ist es ein "Bauleiter"-, "Leitfaden"-, "Checkliste"-, oder
       "Spezialfall"-Skill? (Aus Slug ableitbar: -bauleiter, -leitfaden,
       -checkliste, -spezial.)

    # Schritt B: Zielgrosse festlegen
    4. Wenn aktueller Skill < 4000 Zeichen: Zielgroesse 8000-11000.
    5. Wenn aktueller Skill 4000-8000: Zielgroesse 9000-12000.
    6. Wenn aktueller Skill > 8000: Zielgroesse "verbessern, nicht aufblasen"
       (max +50%).

    # Schritt C: Inhaltliche Recherche
    7. Bestimme das Rechtsgebiet aus Plugin-Name + bestehendem Inhalt.
    8. Lade das passende Cheat-Sheet aus Sektion 2 dieser Datei.
    9. Identifiziere die 3-5 ZENTRALEN Normen + die 2-4 ZENTRALEN
       Leitentscheidungen.
       - Quellen-Disziplin: nur dejure.org, openjur.de, BGH/BVerfG/EuGH-
         Datenbanken. KEINE Erfindungen, keine halluzinierten Aktenzeichen.
       - Wenn unsicher ueber ein Aktenzeichen: NICHT zitieren. Lieber generisch
         "BGH-Rechtsprechung zur Vorsatzanfechtung" als ein erfundenes Az.

    # Schritt D: Umschreiben
    10. Schreibe alle 10 Pflicht-Sektionen aus Sektion 1.2 dieser Datei.
        Bestehender Content wird integriert, nicht ueberschrieben.
    11. Fuelle das rechtsgebietsspezifische Cheat-Sheet (Sektion 2) in den
        passenden Sektionen ein.
    12. Pruefe Description: bleibt unveraendert, ausser sie hat einen
        Validator-Fehler. Description ist HOLY - der Slug-Suchindex haengt
        dran.

    # Schritt E: Validierung
    13. Pruefe: 10 Pflicht-Sektionen vorhanden?
    14. Pruefe: keine erfundenen Aktenzeichen, keine BeckRS-Allein, kein
        anwalt24, kein Komma-Zahl in description?
    15. Pruefe: alle Cross-Skill-Verweise zeigen auf existierende Plugins/
        Skills im Repo?
    16. Pruefe: Length 8000-12000 Zeichen (Ausnahmen okay, aber begruenden)?

  # Pro Plugin commit
  17. Lokaler git add + commit (lokal, nicht push).

# Pro Batch
18. Validatoren laufen lassen:
    python3 scripts/validate-yaml-frontmatter.py
    node scripts/validate-plugin-structure.mjs
19. Index regenerieren:
    python3 scripts/generate-skills-md.py
    python3 scripts/generate-skills-overview.py
20. git push origin codex-skillboost-<thema>-batch-N
21. PR oeffnen, Tom anpingen, AUF GENEHMIGUNG WARTEN.
```

### 3.3 Was Codex NICHT machen darf

- **Keine Skill-Slug-Änderungen.** Slug bleibt wie er ist.
- **Keine Plugin-Renames.**
- **Keine neuen Skills anlegen** in diesem Boost-Vorgang. Nur bestehende
  vertiefen.
- **Keine Loeschung bestehender Inhalte.**
- **Keine Änderung am Description-Text** ausser zur Behebung eines Validator-
  Fehlers. Description ist Suchindex-relevant.
- **Keine Erfindung von Aktenzeichen oder Fundstellen.** Wenn unsicher:
  generisch zitieren oder weglassen.
- **Keine Mass-Edits ohne Rechtsgebiets-Cheat-Sheet.** Wenn das Cheat-Sheet
  fehlt, Skill in UNCLEAR-SKILLS.md eintragen und ueberspringen.
- **Keine Versionsbumps** in `plugin.json`. Das macht Tom am Ende manuell beim
  Release.
- **Keine Änderung an Testakten-Ordnern.**
- **Keine Mass-Reformatierung** anderer Repo-Dateien (CLAUDE.md, README.md,
  SKILLS.md). Nur SKILL.md-Dateien anfassen.

### 3.4 Was Codex pro PR liefern muss

- Branch-Name: `codex-skillboost-<thema>-batch-<N>`.
- PR-Titel: `[Skill-Boost] <Thema>: <N> Plugins, ~<M> Skills vertieft`
- PR-Body: Liste der Plugins, je Plugin Anzahl der gebooosteten Skills,
  durchschnittliche Laengenaenderung, gefundene Probleme.
- Commit-Granularitaet: pro Plugin ein Commit.
- Commit-Stil:
  ```
  skill-boost: <plugin> - <N> Skills vertieft

  - Pflicht-Sektionen ergaenzt: Zweck, Wann, Voraussetzungen, Workflow,
    Pruefraster, Output, Quellen, Hand-Off, Negativ-Abgrenzung,
    Berufsrecht.
  - Rechtsgebietsspezifik: <Norm-Liste>, <Rspr-Liste>.
  - Durchschnittliche Laengenaenderung: +<X>% (von <A> auf <B> Bytes
    Median).
  ```

---

## 4. Optionale Vertiefung - Matter-Workspace-Konvention

Wenn das jeweilige Plugin Mandantenarbeit unterstuetzt (alle fachanwalt-*,
mietrecht, insolvenzrecht, strafrecht, etc.), sollte der Boost zusaetzlich
folgendes Konzept etablieren:

### 4.1 Standardisierte Mandatsdateien

Pro Mandat ein Ordner unter
`~/.config/claude-fuer-deutsches-recht/<plugin>/mandate/<slug>/` mit:

- `mandat.md` - Narrativ-Intake (Anlass, Parteien, Sachverhalt, Ziel)
- `history.md` - laufendes Logbuch mit datierten Eintraegen
- `chronologie.md` - Zeitstrahl der relevanten Ereignisse (optional)
- `fristen.yaml` - YAML-Liste der laufenden Fristen
- `dokumente/` - Anlagenordner

### 4.2 Skills, die das Schema lesen / schreiben

Pro Plugin sollten zwei Meta-Skills boostbar sein (falls vorhanden):

- `<plugin>-mandat-intake` - legt das Schema neu an
- `<plugin>-mandat-update` - schreibt einen `history.md`-Eintrag

Alle anderen Skills im Plugin sollten in ihrem `## Voraussetzungen und
Kontext laden` einen Hinweis enthalten:

> Wenn ein `mandat.md` im aktuellen Mandatsordner existiert, lies es zuerst
> und uebernimm Parteien, Aktenzeichen, Frist-Stand. Sonst frage diese
> Stammdaten gezielt ab.

### 4.3 Wann diese Vertiefung NICHT eingebaut wird

- Bei methodischen Skills (jurastudium, hausarbeitenmacher, zitierweise).
- Bei Tool-/Office-Skills (email-umformulierer, vertragsausfueller).
- Bei Studi-Skills generell.

---

## 5. Quality-Checks: Was Tom bei der PR-Review sehen will

Codex sollte bei jeder PR diesen Self-Check ausfuellen:

```
[ ] Alle 10 Pflicht-Sektionen pro Skill vorhanden
[ ] Keine erfundenen Aktenzeichen (Stichproben-Pruefung von 5 Skills)
[ ] Mindestens 3 echte Normen + 2 echte Leitentscheidungen pro Skill
[ ] Hand-Off-Sektion verweist auf existierende Skills (kein Toter Link)
[ ] "Was dieser Skill nicht macht" ist gehaltvoll, nicht generisch
[ ] Berufsrechtliche Hinweise sind rechtsgebietsbezogen
[ ] Description unveraendert oder Validator-Fix begruendet
[ ] Median-Laenge im Batch im Zielkorridor 8000-12000
[ ] validate-yaml-frontmatter.py gruen
[ ] validate-plugin-structure.mjs gruen
[ ] generate-skills-md.py + generate-skills-overview.py durchgelaufen
[ ] git fetch origin main VOR push gemacht
[ ] Keine Aenderung an Testakten-Ordnern
[ ] Keine Aenderung an Skill-Slugs oder Plugin-Namen
```

---

## 6. Beispiel - Vorher / Nachher (illustrativ)

### 6.1 VORHER (aktueller Stil, ~3500 Zeichen)

```markdown
---
name: stbv-einspruch-strafbefehl-leitfaden
description: "Leitfaden Einspruch gegen Strafbefehl: Form, Frist, Beschraenkung auf Rechtsfolge, taktische Erwaegungen. Pruefraster fuer Verteidiger."
---

# StBV: Einspruch Strafbefehl

## Aufgabe
Leitfaden Einspruch gegen Strafbefehl.

## Kaltstart
1. Rolle und Ziel
2. Sachverhalt
3. Fristen
4. Unterlagen
5. Format

## Pruefraster
1. Sachverhalt fixieren
2. Rechtliche Einordnung
3. Pruefung im Gutachtenstil
4. Handlungsempfehlung

## Output-Module
- Pruefvermerk
- Tabellen
- Schriftsatz-Geruest
- Quellenliste

## Quellenregel
- nur freie Quellen
- BeckRS allein nicht zulaessig

## Was dieser Skill nicht macht
- kein Ersatz fuer Mandatsberatung
```

### 6.2 NACHHER (Boost-Ziel, ~10000 Zeichen)

```markdown
---
name: stbv-einspruch-strafbefehl-leitfaden
description: "Leitfaden Einspruch gegen Strafbefehl: Form, Frist, Beschraenkung auf Rechtsfolge, taktische Erwaegungen. Pruefraster fuer Verteidiger."
---

# StBV: Einspruch gegen Strafbefehl - Leitfaden

## Zweck
Dieser Skill begleitet die Pruefung und ggf. Einlegung des Einspruchs gegen
einen Strafbefehl nach § 410 StPO. Typischer Anlass: Mandant erhaelt einen
Strafbefehl per Postzustellungsurkunde, die Einspruchsfrist von zwei Wochen
ab Zustellung laeuft, und Verteidiger muss in kurzer Zeit Form, Inhalt und
Taktik des Einspruchs entscheiden. Adressat: Strafverteidiger im
Erstgespraech, vor allem im OWi-nahen Verkehrsstrafrecht und in
kleineren Wirtschaftsstrafsachen.

## Wann wird dieser Skill aufgerufen

Der User sagt typisch:
- "Mein Mandant hat einen Strafbefehl bekommen, was machen wir?"
- "Strafbefehl wegen § 142 StGB, lohnt der Einspruch?"
- "Welche Frist habe ich noch fuer den Einspruch?"
- "Soll ich auf die Rechtsfolge beschraenken?"

NICHT dieser Skill, sondern andere:
- Wenn es um die Pruefung eines Bussgeldbescheids geht, gehoert das zum
  Plugin `verkehrsowi-verteidiger`, Skill `vowi-bussgeldbescheid-
  pruefung-bauleiter`.
- Wenn der Strafbefehl bereits rechtskraeftig ist und nur die
  Vollstreckung gemildert werden soll, gehoert das in Skill
  `strafr-vermoegensabschoepfung-spezial` bzw. Strafvollstreckung.

## Voraussetzungen und Kontext laden

Vor jeder Aktion lies, falls vorhanden, das Mandatsverzeichnis im aktuellen
Plugin-Workspace (`mandate/<slug>/mandat.md`). Wenn nicht vorhanden, frage
gezielt ab:

- Datum und Form der Zustellung (Postzustellungsurkunde, Ersatzzustellung
  nach § 178 ZPO i.V.m. § 37 StPO?)
- Geschaeftsnummer der Staatsanwaltschaft
- Tatvorwurf und herangezogene Normen
- Festgesetzte Rechtsfolge (Geldstrafe Tagessaetze, Fahrverbot, Sperre,
  Berufsverbot)
- Vorstrafen / BZR-Eintraege
- Aktuelle Lebenssituation des Mandanten (Beruf, Fahrerlaubnis-Abhaengigkeit)

Variablen, die der Workflow braucht:
`zustellung_datum`, `frist_ende`, `tatvorwurf`, `geldstrafe_tagessaetze`,
`fahrverbot_monate`, `sperre_monate`.

## Workflow

1. **Zustellung pruefen.** Pruefe Datum der PZU. Wenn keine PZU vorliegt:
   ist die Zustellung wirksam? § 37 StPO i.V.m. ZPO. Bei Ersatzzustellung
   Hinweis auf moegliche Unwirksamkeit.

2. **Einspruchsfrist berechnen.** Zwei Wochen ab Zustellung, § 410 Abs. 1
   StPO. Sonntag/Feiertag schiebt auf naechsten Werktag, § 43 StPO.
   Schreibe Frist-Ende im Format YYYY-MM-DD. Bei < 3 Tagen Restfrist:
   sofort Einspruchsentwurf bauen, Detailpruefung danach.

3. **Form des Einspruchs.** Schriftlich oder zu Protokoll der Geschaefts-
   stelle, § 410 Abs. 1 S. 1 StPO. Adressat: Amtsgericht, das den
   Strafbefehl erlassen hat. KEIN Telefax, sofern Gericht nicht
   ausdruecklich zulaesst.

4. **Pruefung des Strafbefehls inhaltlich.**
   4.1 Tatvorwurf rechtlich vollstaendig?
   4.2 Strafhoehe verhaeltnismaessig im Hinblick auf §§ 46, 46a StGB?
   4.3 Nebenfolgen (Fahrverbot, Sperre, BZR-Eintrag) verhaeltnismaessig?
   4.4 BGH-Rechtsprechung zu vergleichbaren Faellen?

5. **Beschraenkung des Einspruchs pruefen, § 410 Abs. 2 StPO.**
   Moeglich auf bestimmte Beschwerdepunkte, typisch:
   - nur auf die Rechtsfolgen
   - nur auf das Fahrverbot
   - nur auf einzelne Taten bei Tatmehrheit
   Vorteil: schnellerer Termin, Beschraenkung auf Strafzumessungsfrage.
   Nachteil: Schuldspruch wird rechtskraeftig.

6. **Taktische Erwaegungen.**
   - Wenn Schuldfeststellung problematisch: Vollein­spruch.
   - Wenn Hoehe der Geldstrafe Hauptproblem: Beschraenkung auf
     Rechtsfolgen.
   - Wenn nur Fahrverbot bekaempft werden soll: Teil-Einspruch.

7. **Vollmacht und Akteneinsicht parallel.** Verteidigervollmacht und
   Antrag auf Akteneinsicht nach § 147 StPO mit dem Einspruch
   verbinden.

8. **Schriftsatz aufsetzen** (Output-Geruest siehe Output-Module).

9. **Mandant informieren.** Folgen des Einspruchs erklaeren (Hauptverhandlung,
   Verschlechterungsverbot § 411 Abs. 4 StPO, mogliche Beweisaufnahme,
   Honorar nach RVG VV 4106-4111).

## Pruefraster im Gutachtenstil

**A. Zulaessigkeit des Einspruchs**

Statthaftigkeit: § 410 Abs. 1 StPO sieht den Einspruch gegen Strafbefehle
ausdruecklich vor. Statthaft, wenn ein Strafbefehl nach §§ 407 ff. StPO
ergangen ist und noch nicht rechtskraeftig.

Frist: zwei Wochen ab Zustellung des Strafbefehls. Subsumtion: Pruefe
Datum der PZU und berechne. BGHSt 35, 137 zur Frage der Wirksamkeit der
Zustellung bei zweifelhafter PZU; siehe BGH Beschluss vom ... (nur
einfuegen wenn Aktenzeichen sicher).

Form: § 410 Abs. 1 S. 1 StPO. Schriftlich bei Gericht oder zu Protokoll
der Geschaeftsstelle.

Beschwer: der Mandant ist durch den Strafbefehl beschwert.

**B. Begruendetheit / Erfolgsaussicht**

Pruefe Tatbestand und Rechtsfolge:

1. Ist der Tatvorwurf rechtlich tragfaehig? Liegt ein Tatbestandsmerkmal
   nicht vor?
2. Ist die Beweislage tragfaehig? Bei einseitigen Strafbefehls-Verfahren
   sind die Beweise oft nur die Anzeige + Polizeibericht.
3. Ist die Strafzumessung § 46 StGB-konform? Tagessaetze nach § 40 StGB?
4. Sind Nebenfolgen verhaeltnismaessig? Fahrverbot § 44 StGB nur bei
   Zusammenhang mit Kraftfahrzeugfuehrung.

**C. Beschraenkung des Einspruchs**

§ 410 Abs. 2 StPO erlaubt Beschraenkung. Pruefe, ob Schuldspruch
unangreifbar und nur Rechtsfolge problematisch. Wirkung: Schuldspruch
wird rechtskraeftig, nur Rechtsfolge wird neu verhandelt.

## Output-Module

- Mandantenbrief: Erlaeuterung des Strafbefehls, Optionen, Empfehlung.
- Schriftsatz Einspruch (Geruest):
  - Rubrum, Aktenzeichen, Strafbefehl-Datum
  - "Namens und in Vollmacht ... wird gegen den Strafbefehl ...
    Einspruch eingelegt."
  - ggf. Beschraenkung auf Rechtsfolgen, § 410 Abs. 2 StPO
  - Antrag auf Akteneinsicht, § 147 StPO
  - Vollmacht beigefuegt.
- Fristen-Eintrag fuer `mandate/<slug>/fristen.yaml`.
- Pruefvermerk im `mandat.md` mit Datum und Empfehlung.

## Quellen und Zitierregel

Pflicht-Normen: §§ 407-412 StPO, §§ 44 ff. StGB, § 147 StPO, RVG VV 4106-4111.

Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und pruefbarem Link
(dejure.org, openjur.de, bundesgerichtshof.de). Bei unsicheren Aktenzeichen
generisch zitieren ("BGH-Rechtsprechung zur Strafzumessung bei Verkehrs-
strafsachen") statt erfinden.

Quellen-Tags fuer den Output:
`[BGH-Datenbank]`, `[dejure.org]`, `[openjur.de]`, `[Mandant]`,
`[Modellwissen - pruefen]`.

## Hand-Off zu anderen Skills

Nach diesem Skill weiter mit:
- `/fachanwalt-strafrecht:strafr-revision-pruefung-spezial` wenn nach
  Hauptverhandlung Revision relevant wird.
- `/fachanwalt-verkehrsrecht:verk-fahrerlaubnisrecht-leitfaden` wenn das
  Fahrverbot zentral ist und parallel die Fahrerlaubnisbehoerde aktiv wird.
- `/aktenaufbereiter-strafrecht:akzg-aktenauszug-bauleiter` zur
  Vorbereitung der Akteneinsichts-Auswertung.

## Was dieser Skill nicht macht

- Ersetzt nicht das Mandatsverhaeltnis. Erstellt eine Vorlage, kein
  Mandatsangebot.
- Berechnet Fristen vorlaeufig. Die letztverbindliche Frist liegt im
  Akten- und Zustellungsdokument. Bei Eilfall immer eigene Frist-
  Berechnung gegenchecken.
- Trifft keine taktische Entscheidung ueber Vollein­spruch vs Teil-
  Einspruch. Diese Entscheidung trifft der Verteidiger im Mandanten-
  gespraech.
- Berechnet keine konkrete Strafzumessung; das macht das Gericht in
  der Hauptverhandlung.
- Ersetzt keine Akteneinsicht. Die Akteneinsicht ist Pflicht, bevor
  ueber Beschraenkung des Einspruchs entschieden wird.

## Berufsrechtliche Hinweise

§ 43a Abs. 2 BRAO Schweigepflicht ueber alles Mandanten-Bezogene.
§ 49b BRAO Honorarvereinbarung; im Strafrecht gilt zusaetzlich
§ 14 RVG Verteidigergebuehr. Bei Pflichtverteidigung § 140 StPO
Eintragung pruefen.

Bei erkennbaren Interessenkonflikten (Mandant ist Mitarbeiter eines
Mandanten der Kanzlei in anderer Sache) Hinweis an den fallfuehrenden
Anwalt und ggf. Mandat ablehnen, § 3 BORA.
```

Das ist die Tiefe, die Codex anstreben soll - pro Skill, rechtsgebiets-
spezifisch, mit konkreten Normen, konkreten Verfahrensschritten und
expliziter Negativ-Abgrenzung.

---

## 7. Eskalation / Sonderfaelle

- **Wenn Codex auf einen Skill stoesst, der inhaltlich unklar ist:**
  Eintrag in `anthropic-lessons/UNCLEAR-SKILLS.md` und ueberspringen.
- **Wenn ein Plugin keine sinnvollen Pflicht-Sektionen erlaubt** (z.B.
  reine Tool-Skills): Boost auf ~6000-8000 Zeichen, Sektionen sinnvoll
  reduzieren, in PR-Body begruenden.
- **Wenn die rechtliche Recherche für den Skill scheitert** (Codex hat
  keine Datenbank-Zugriff): GENERISCHE Zitate stehen lassen, NIE erfinden.
  Lieber "BGH-Rechtsprechung zur Vorsatzanfechtung" als ein erfundenes
  Az.

---

## 8. Abschluss-Checks von Tom

Tom prüft pro PR:

- Stichproben-Lesen von 5-10 zufaelligen Skills aus dem Batch.
- Validatoren-Status.
- Lange-Verteilung Diagramm.
- Keine offensichtlichen Halluzinationen bei Aktenzeichen.
- Keine BeckRS-Allein-Zitate.
- Hand-Off-Verweise prüfen (Plugin/Skill existieren).
- Negativ-Abgrenzung pro Stichprobe nicht generisch.

Erst nach Freigabe: Merge.

---

## 9. Versionierung nach Abschluss aller Boost-Batches

Wenn alle 25-30 Batches gemerged sind:

- Version-Bump auf `v53.0.0` (Major, weil Inhaltscharakter sich
  qualitativ ändert).
- Release-Notes: "Skill-Tiefe-Boost auf Anthropic-Niveau, ~3670 Skills
  vertieft, Median-Laenge von ~4500 auf ~10000 Zeichen."
- Index-Regen + Release-Workflow.

---

*Stand dieser Instruktion: nach Analyse von anthropics/claude-for-legal HEAD
am 2026-06-01.*
*Autorisiert durch Tom Braegel.*
