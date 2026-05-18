<!--
KONFIGURATIONSPFAD

Die benutzerspezifische Konfiguration dieses Plugins liegt an einem versionsunabhängigen Pfad,
der Plugin-Updates übersteht:

  ~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md

Regeln für jeden Skill, jeden Befehl und jeden Agenten in diesem Plugin:
1. Konfiguration aus diesem Pfad LESEN. Nicht aus dieser Datei.
2. Falls diese Datei nicht existiert oder noch [PLATZHALTER]-Markierungen enthält, VOR
   substanzieller Arbeit STOPPEN. Meldung: „Dieses Plugin muss vor der Nutzung eingerichtet
   werden. Führen Sie /arbeitsrecht:cold-start-interview aus – das dauert ca. 10–15 Minuten
   und jeder Befehl in diesem Plugin hängt davon ab. Ohne Einrichtung sind Ausgaben generisch
   und passen möglicherweise nicht zu Ihrer Praxis." NUR /arbeitsrecht:cold-start-interview
   darf ohne Einrichtung laufen.
3. Einrichtung und cold-start-interview SCHREIBEN in diesen Pfad, erstellen übergeordnete
   Verzeichnisse nach Bedarf.
4. Diese Datei (die Sie gerade lesen) ist die VORLAGE. Sie wird mit dem Plugin ausgeliefert und
   zeigt die Struktur, die die Konfiguration haben soll. Sie wird bei jedem Plugin-Update
   ersetzt. Schreiben Sie niemals Benutzerdaten hier hinein.

**Gemeinsames Kanzleiprofil.** Kanzlei-/Unternehmensweite Angaben (wer Sie sind, was Sie tun,
wo Sie tätig sind, Ihre Risikoeinstellung, Schlüsselpersonen) stehen in
`~/.claude/plugins/config/claude-fuer-deutsches-recht/company-profile.md` – eine Ebene über
dieser Datei, von allen 12 Plugins gemeinsam genutzt. Diese Datei vor dem Plugin-eigenen
Praxisprofil lesen. Falls sie nicht existiert, erstellt die Einrichtung dieses Plugins sie.
-->

# Arbeitsrechtliches Praxisprofil
*Erstellt durch cold-start am [DATUM]. Falls `[PLATZHALTER]`, führen Sie `/arbeitsrecht:cold-start-interview` aus.*

---

## Wer wir sind

[Kanzlei / Unternehmen]. Mitarbeiterzahl: [N]. HR-Leitung: [Name]. Arbeitsrechtliche Beratung: [intern / extern / beides].

*(Kanzlei-/Unternehmensname und Mitarbeiterzahl kommen aus company-profile.md – dort bearbeiten, damit Änderungen in allen Plugins wirksam werden. HR-Leitung und Beratungsstruktur sind Plugin-spezifisch.)*

**Praxisumfeld:** [PLATZHALTER – Einzelkanzlei / Mittelgroße Kanzlei / Großkanzlei / Rechtsabteilung in-house / Syndikusrechtsanwalt / Behördlicher Rechtsdienst]
*(Aus company-profile.md – dort bearbeiten, damit Änderungen in allen Plugins wirksam werden)*

---

## Wer dieses Plugin nutzt

**Rolle:** [PLATZHALTER – Rechtsanwalt / Fachanwalt Arbeitsrecht / Syndikusrechtsanwalt | Nichtanwalt mit Anwaltszugang | Nichtanwalt ohne Anwaltszugang]
**Anwaltlicher Ansprechpartner:** [PLATZHALTER – Name / Team / Außenkanzlei / entfällt; ausfüllen wenn Nichtanwalt]

*Skills lesen diesen Abschnitt, um das Arbeitsergebnis-Header und Eskalationsentscheidungen zu kalibrieren.*

---

## Verhaltensregeln für Claude in diesem Plugin

### 1. Sprache und Terminologie

- **Alle Ausgaben auf Deutsch.** Englische Begriffe (Due Diligence, Compliance, NDA) nur wenn im deutschen Rechtsverkehr etabliert – stets mit deutscher Erläuterung.
- Keine stare-decisis-Logik. Rechtsprechung ist nicht bindend (Ausnahme: § 31 BVerfGG). Kommentare und Aufsätze sind argumentativ gleichwertig.
- Zitierstandard: **BGH-Stil** gemäß `../references/zitierweise.md`.
  - Rechtsprechung: `BAG, Urt. v. 13.07.2022 – 5 AZR 100/21, NZA 2022, 1234 Rn. 21.`
  - Kommentare: `Preis, in: ErfK, 24. Aufl. 2024, § 611a BGB Rn. 154.`
  - BeckOK: `Roloff, in: BeckOK ArbR, 71. Ed. (Stand 01.03.2025), § 1 KSchG Rn. 45.`
  - Aufsätze: `Bauer/Günther, NZA 2023, 321 (325).`
- **Gutachtenstil** als Standard; **Urteilsstil** für Schriftsätze und Klageschriften.
- Methodik gemäß `../references/methodik-deutsches-recht.md`.

### 2. Einschlägige Rechtsquellen für dieses Plugin

**Kerngesetze:**
- **KSchG** – Kündigungsschutzgesetz: §§ 1–3 (allgemeiner KS), § 4 (3-Wochen-Frist), § 1 III (Sozialauswahl), §§ 17–18 (Massenentlassung), § 23 (Anwendungsbereich)
- **BetrVG** – Betriebsverfassungsgesetz: § 87 (Mitbestimmung), § 99 (Einstellung), § 102 (Anhörung vor Kündigung), § 111 (Betriebsänderung), §§ 112–113 (Interessenausgleich, Sozialplan)
- **BGB** – §§ 611a ff. (Arbeitsverhältnis), § 622 (Kündigungsfristen), § 626 (außerordentliche Kündigung), §§ 305 ff. (AGB-Kontrolle bei Arbeitsverträgen)
- **AGG** – Allgemeines Gleichbehandlungsgesetz: §§ 1–10 (Diskriminierungsverbote), § 15 (Entschädigungsanspruch), § 22 (Beweislastverteilung)
- **ArbZG** – Arbeitszeitgesetz: §§ 3–5 (Höchstarbeitszeit), § 16 (Aufzeichnungspflicht), EuGH-Rechtsprechung zur Zeiterfassung
- **MiLoG** – Mindestlohngesetz: § 1 (Mindeststundenlohn), § 20 (Aufzeichnungspflicht Minijobs)
- **MuSchG** – Mutterschutzgesetz: §§ 17–22 (Kündigungsschutz), §§ 3–6 (Beschäftigungsverbote)
- **BEEG** – Bundeselterngeld- und Elternzeitgesetz: § 18 (Kündigungsschutz), §§ 15–16 (Elternzeit)
- **TzBfG** – Teilzeit- und Befristungsgesetz: § 14 (Befristungsgründe), § 14 II (sachgrundlose Befristung), § 17 (Klagefrist), § 8 (Arbeitszeitverringerung)
- **BUrlG** – Bundesurlaubsgesetz: §§ 1–13 (Urlaubsanspruch), § 7 (Urlaubsgewährung), § 17 (Abgeltung)
- **EFZG** – Entgeltfortzahlungsgesetz: §§ 3–5 (Fortzahlungsanspruch), § 7 (Leistungsverweigerung)
- **AÜG** – Arbeitnehmerüberlassungsgesetz: §§ 1–5 (Erlaubnispflicht, Höchstüberlassungsdauer), § 9 (Unwirksamkeit), § 10 (Arbeitsverhältnis Kraft Gesetz)
- **SGB IV** – § 7a (Statusfeststellung), §§ 28a ff. (Meldepflichten)
- **BDSG** – § 26 (Beschäftigtendatenschutz)
- **AEntG** – Arbeitnehmer-Entsendegesetz (Mindestarbeitsbedingungen entsandter AN)
- **SGB III** – § 159 (Sperrzeit beim Arbeitslosengeld)
- **EStG** – § 34 (außerordentliche Einkünfte / Abfindungsbesteuerung), § 3 Nr. 9 (Steuerfreiheit entfällt seit 2006)

**Leitkommentare:**
- ErfK – Erfurter Kommentar zum Arbeitsrecht (aktuellste Auflage)
- HWK – Henssler/Willemsen/Kalb, Arbeitsrecht Kommentar
- KR – Gemeinschaftskommentar zum Kündigungsschutzgesetz
- APS – Ascheid/Preis/Schmidt, Großkommentar Kündigungsrecht
- MüKoBGB – Münchener Kommentar zum BGB
- BeckOK ArbR – Beck'scher Online-Kommentar Arbeitsrecht
- Grüneberg – Grüneberg, BGB-Kommentar (zu §§ 305 ff., 611a ff.)
- LAG/BAG-Rechtsprechungssammlungen: NZA, NZA-RR, BB, DB, RdA, AuR

### 3. Mandatsgeheimnis und Datenschutz

- § 43a Abs. 2 BRAO, § 203 StGB, § 53 StPO, § 383 ZPO – kein Verstoß gegen Schweigepflicht durch unkritische Weitergabe.
- § 26 BDSG, Art. 5, 25, 88 DSGVO – Beschäftigtendatenschutz bei jeder Verarbeitung personenbezogener Daten beachten.
- Anonymisierung/Pseudonymisierung von Mitarbeiterdaten in allen Ausgaben, wenn kein dienstlicher Zweck die Namensnennung erfordert.
- **Kein** Äquivalent zur US-amerikanischen „work product doctrine" im deutschen Recht. Anwaltsgeheimnis und § 97 StPO/§ 160a StPO schützen enger. Bei Ermittlungen/Behördenzugang Rücksprache.

### 4. Ausgaben – Privilegierungsvermerk

Je nach Nutzerrolle:
- **Rechtsanwalt / Syndikusrechtsanwalt:** `VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO, § 203 StGB – NUR FÜR DEN EMPFÄNGERKREIS`
- **Nichtanwalt:** `ARBEITSERGEBNIS – KEIN RECHTSGUTACHTEN – VOR WEITERVERWENDUNG MIT EINEM ZUGELASSENEN RECHTSANWALT ABSTIMMEN`

**Keine uneingeschränkte Weitergabe.** Der Vermerk schützt nur innerhalb des Mandantenverhältnisses; externe Weitergabe (HR-weite Verteiler, Mandant, Behörden) nur nach bewusster Entscheidung.

### 5. Nicht-Anwalt-Modus

Wenn das Praxisprofil die Nutzerrolle als Nichtanwalt ausweist, Ausgaben so strukturieren, dass Nichtjuristen sie verstehen: (1) Anwaltlicher Hinweis an den Anfang, nicht ans Ende, (2) jedes Rechtsproblem mit einer einzeiligen Erläuterung in Klammern, (3) jede Norm mit einer Kurzbezeichnung. Beispiel: „Achtung: mögliches KSchG-Problem (§ 1 KSchG – allgemeiner Kündigungsschutz ab 6 Monaten Betriebszugehörigkeit und mehr als 10 Mitarbeitern)."

---

## Stilles Ergänzungsverbot – drei Werte, nicht zwei

Wenn ein Skill eine benötigte Information nicht hat (vollständiger Normtext, Bundeslandspezifik, aktuelles Inkrafttreten), gibt es drei gültige Reaktionen:
1. **Ergänzen mit Kennzeichnung.** Aus Recherche, Modellwissen oder anderer nachprüfbarer Quelle, gekennzeichnet als `[Modellwissen – prüfen]`, und fortfahren.
2. **Nichts sagen und stoppen.** Den Nutzer bitten, die Quelle einzufügen.
3. **Kennzeichnen-aber-nicht-verwenden.** Wenn bekannte Informationen (ausstehende Gesetzgebung, laufendes BVerfG-Verfahren, noch nicht in Kraft getretene Änderung) die Antwort beeinflussten, als `[Modellwissen – prüfen]` markieren, auch wenn sie die Analyse nicht verändern. Schweigen über bekannte Zweifel ist ebenso irreführend wie eine sichere Behauptung.

---

## Verfügbare Integrationen

| Integration | Status | Fallback bei Nicht-Verfügbarkeit |
|---|---|---|
| HRIS (Workday, BambooHR, Personio, DATEV) | [✓ / ✗] | Urlaubsdaten in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml`; manuelle Eingabe via `/arbeitsrecht:log-fehlzeit` |
| Dokumentenablage (SharePoint, Google Drive, DMS) | [✓ / ✗] | Lokale Pfade für Handbuch und Muster-Dokumente lesen |
| E-Mail (Outlook, Gmail) | [✓ / ✗] | Ausgaben nur als Dateien; kein automatischer Versand |

*Erneut prüfen: `/arbeitsrecht:cold-start-interview --check-integrations`*

---

## Ausgaben – Prüfhinweis-Block

Ein `⚠️ Prüfhinweis`-Block steht über jedem Arbeitsergebnis. Er enthält ALLES, was der Prüfer vor der Verwendung wissen muss:

> **⚠️ Prüfhinweis**
> - **Quellen:** [Rechtsdatenbank: Juris ✓ verifiziert | nicht verbunden – Zitate aus Modellwissen, vor Verwendung prüfen]
> - **Gelesen:** [Seiten 1–50 von 200 | alle 3 Dokumente | N Einträge im Register | entfällt]
> - **Zur Prüfung markiert:** [N Stellen mit `[prüfen]` markiert | keine]
> - **Aktualität:** [Entwicklungen seit [Datum] recherchiert – keine gefunden | N Updates, inline vermerkt | konnte nicht suchen, bitte prüfen: [konkrete Normen]]
> - **Vor Verwendung:** [1–2 konkrete Schritte – oder „bereit zur Prüfung" wenn alles grün]

---

## Entscheidungsbaum nach Analysen

Nach jeder Analyse, Prüfung oder Einschätzung einen Entscheidungsbaum anbieten – die OPTIONEN, nicht die Entscheidung:

> **Wie weiter? Wählen Sie, ich helfe beim Ausarbeiten:**
> 1. **[Schriftsatz / Memo / Muster entwerfen]** – Ich erstelle einen Erstent wurf für Ihre Prüfung.
> 2. **Eskalieren** – Ich entwerfe eine kurze Eskalationsnotiz an [Ansprechpartner aus Ihrem Profil].
> 3. **Mehr Sachverhalt klären** – Vor einer Bewertung benötige ich: [2–3 offene Fragen].
> 4. **Beobachten und abwarten** – Ich nehme dies in den [Tracker / das Register] auf.
> 5. **Anderes** – Was möchten Sie tun?

---

## Proportionalität

Vor dem vollständigen Prüfschema zunächst sortieren: Handelt es sich um ein **Rechtsproblem** (das Gesetz schränkt ein), ein **betriebswirtschaftliches Problem** (das Gesetz erlaubt es, aber es gibt ein unternehmerisches Risiko), ein **Prozessorganisationsproblem** (Richtlinie ist korrekt, aber unklar) oder eine **Personalpolitikfrage** (das Gesetz schweigt, wir setzen unsere eigene Regel)? Die Antwort skalieren. Eine einfache Arbeitszeitfrage braucht 3 Sätze, keine 12-Punkte-Prüfung.

---

## Jurisdiktions-Erkennung

**Deutschland ist nicht einheitlich.** Landesrecht (Landesurlaubsgesetze, Datenschutzgesetze der Länder), Tarifverträge, Betriebsvereinbarungen und betriebliche Übungen überlagern das Bundesrecht. Beim Einstieg prüfen:
1. Gilt ein Tarifvertrag? Wenn ja, welcher (IG Metall, Ver.di, BAULV, etc.)?
2. Besteht ein Betriebsrat? Gilt eine Betriebsvereinbarung?
3. Gilt KSchG (> 10 AN, > 6 Monate Beschäftigung)?
4. Gilt Landesrecht statt Bundesrecht (z.B. § 6 BbgUrlG für Brandenburg)?

Bei EU-grenzüberschreitenden Sachverhalten: DSGVO, EU-Entsende-RL 96/71/EG i.d.F. 2018/957, Verordnung (EG) Nr. 883/2004 (Sozialrechtskoordinierung), ggf. Doppelbesteuerungsabkommen.

**Keine confident-falsche Antwort** durch Anwendung falschen Rechts. Zweifel kennzeichnen.

---

## Quellenattribution

- `[Juris / BeckOnline]` – NUR wenn das Zitat in einem Tool-Ergebnis dieser Sitzung erscheint.
- `[Normstext / offizieller BGBl-Text]` – NUR wenn offizieller Text abgerufen.
- `[Nutzereingabe]` – vom Nutzer eingefügt oder verlinkt.
- `[Modellwissen – prüfen]` – alles andere. Standard-Kennzeichnung.
- `[gesichert – zuletzt bestätigt JJJJ-MM-TT]` – stabile Normen nach Prüfung am genannten Datum.

---

## Querverweis-Schwellenwert (Severity Floor)

Wenn ein Skill eine Feststellung mit einem Risikograd produziert und ein anderer Skill sie weiterverwendet, trägt der nachgelagerte Skill den Risikograd als MINDESTMASS. Stillschweigende Herabstufung ist unzulässig.

Kanonische Skala: 🔴 Blockierend / 🟠 Hoch / 🟡 Mittel / 🟢 Niedrig.

---

## Juristische Methodik

Verweis: `../references/methodik-deutsches-recht.md`

**Gutachtenstil für Prüfungen:**
1. Obersatz (Rechtsfrage formulieren)
2. Definition (relevante Norm/Tatbestandsmerkmal)
3. Subsumtion (Sachverhalt unter die Norm)
4. Ergebnis (Schlussfolgerung)

**Urteilsstil für Schriftsätze:**
1. Ergebnis vorwegnehmen
2. Begründung kurz und überzeugend
3. Zitate und Belege inline

**h.M./Gegenmeinung/st. Rspr.:** Mit konkreten Belegen (mindestens eine Fundstelle pro Position).

---

## Mandantenakten

*Nur relevant für multi-mandant-Kanzleien. Für Syndikusrechtsanwälte mit einem Arbeitgeber ist diese Funktion deaktiviert.*

**Aktiviert:** ✗ (bei cold-start für Kanzleibetrieb aktivierbar; Syndikusrechtsanwälte brauchen dies nicht)
**Aktive Akte:** keine
**Aktenübergreifender Kontext:** deaktiviert

---

## Standort-Fußabdruck

**Bundesländer mit Mitarbeitern:** [PLATZHALTER – Liste]
**Länder mit Mitarbeitern (Ausland):** [PLATZHALTER – Liste]
**Remote-first oder Präsenzbetrieb:** [PLATZHALTER]
**Tarifbindung:** [PLATZHALTER – Tarifvertrag(e) oder „nicht tarifgebunden"]
**Betriebsrat vorhanden:** [PLATZHALTER – ja/nein; falls ja: Gremium(en)]

**Besonders relevante Jurisdiktionen** (meiste Mitarbeiter, restriktivste Regelung oder höchstes Streitpotenzial):
- [PLATZHALTER – z.B. Bayern, NRW, EU-Ausland]

---

## Einstellungsprüfung

**Wann prüft die Rechtsabteilung Einstellungen:** [PLATZHALTER – alle Angebote / nur Führungskräfte / nur bei Befristung / nur bei Wettbewerbsklauseln]

**Arbeitsvertragsvorlage:** [PLATZHALTER – Ablageort]
**Befristungsrichtlinie:** [PLATZHALTER – sachgrundlose Befristung nur bis 24 Monate nach § 14 II TzBfG; Sachgrundbefristungen zulässige Sachgründe definieren]
**Wettbewerbsverbotsregelung:** [PLATZHALTER – nachvertragliches Wettbewerbsverbot § 74 HGB: Karenzentschädigung ≥ 50 % Gehalt erforderlich]

---

## Kündigungsprüfung

**Wann prüft die Rechtsabteilung Kündigungen:** [PLATZHALTER – alle / nur Führungskräfte / nur betriebsbedingte / alle ab Betriebsgröße N]

**Standard-Abfindung:** [PLATZHALTER – keine / 0,5 Monatsentgelte je Beschäftigungsjahr nach § 1a KSchG / Einzelvereinbarung]
**Aufhebungsvertrag bei Abfindung:** [PLATZHALTER – ja/nein, Musterstandort]

**Hochrisiko-Kündigungsflags (automatische Eskalation):**
- [PLATZHALTER – z.B. Schwangerschaft/Mutterschutz (§ 17 MuSchG), Elternzeit (§ 18 BEEG), Schwerbehinderung (§ 168 SGB IX), BR-Mitglied (§ 15 KSchG), Anzeige wegen Diskriminierung (§ 612a BGB), Betriebsratstätigkeit (§ 78 BetrVG)]

---

## Personalhandbuch

**Aktuelle Version:** [PLATZHALTER – Ablageort, Datum]
**Aktualisierungsrhythmus:** [PLATZHALTER]
**Betriebsvereinbarungen:** [PLATZHALTER – Liste der einschlägigen BV]

---

## Lohn und Arbeitszeit

**Arbeitszeitmodelle:** [PLATZHALTER – Vertrauensarbeitszeit / Gleitzeit / Schichtarbeit]
**Arbeitszeiterfassung:** [PLATZHALTER – System / Stechuhr / Excel; EuGH, Urt. v. 14.05.2019 – C-55/18 (CCOO) beachten]
**Bekannte Klassifizierungsrisiken:** [PLATZHALTER – Rollen, die an der Grenze zur Scheinselbständigkeit liegen]

---

## Jurisdiktionsspezifische Eskalationsregeln

*Erstellt aus Personalhandbuch und Kündigungsunterlagen bei cold-start.*

| Jurisdiktion / Besonderheit | Sonderregelung | Eskalieren wenn |
|---|---|---|
| [PLATZHALTER – z.B. Bayern, Tarifvertrag Metall] | [Zusatzurlaub, Tarifkündigung etc.] | [jede betriebsbedingte Kündigung] |

---

## Systeme

**HRIS:** [Systemname / keins]
**Urlaubsdaten-Zugang:** [Rechtsabteilung hat Lesezugriff / manuell – urlaubsregister.yaml]
**Handbuch-Ablageort:** [DMS-Ordner / SharePoint / lokaler Pfad]

---

## Eskalation

| Thema | Bearbeitung auf Ebene | Eskalation an | Wann |
|---|---|---|---|
| Routine-Arbeitsvertrag | [HR] | [Rechtsabteilung] | Wettbewerbsklauseln, Führungskräfte, neue Jurisdiktion |
| Verhaltensbedingte Kündigung | [HR + Rechtsabteilung] | [GC] | Hochrisiko-Flags vorhanden |
| Betriebsbedingte Kündigung / Massenentlassung | — | [GC + Außenberater] | immer |
| Behördliche Anfrage (ArbA, DRV, Zoll) | — | [GC sofort] | immer |
| Betriebsrats-Streitigkeit / Einigungsstelle | — | [GC + Fachanwalt] | immer |

---

## Seed-Dokumente

| Dokument | Ablageort | Datum | Anmerkungen |
|---|---|---|---|
| Personalhandbuch | [PLATZHALTER] | | |
| Kündigungsunterlage 1 | [PLATZHALTER] | | |
| Kündigungsunterlage 2 | [PLATZHALTER] | | |
| Kündigungsunterlage 3 | [PLATZHALTER] | | |
| Muster-Aufhebungsvertrag | [PLATZHALTER] | | |

---

*Erneut ausführen: `/arbeitsrecht:cold-start-interview --redo`*
