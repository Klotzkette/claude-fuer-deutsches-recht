<!--
KONFIGURATIONSPFAD

Benutzerspezifische Konfiguration für dieses Plugin liegt an einem versionsunabhängigen Pfad:

  ~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/CLAUDE.md

Regeln für jeden Skill, jeden Befehl und jeden Agenten in diesem Plugin:
1. Konfiguration von diesem Pfad LESEN. Nicht aus dieser Datei.
2. Existiert diese Datei nicht oder enthält noch [PLATZHALTER]-Marker, VOR substanzieller Arbeit STOPPEN. Ausgabe: „Dieses Plugin benötigt eine Einrichtung, bevor es sinnvolle Ergebnisse liefern kann. Führen Sie /datenschutzrecht:cold-start-interview aus – die Einrichtung dauert ca. 10–15 Minuten; ohne sie sind Ausgaben generisch und entsprechen nicht Ihrer tatsächlichen Praxis." Ausnahme: Das Cold-Start-Interview selbst und --check-integrations laufen auch ohne Setup.
3. Setup und Cold-Start-Interview SCHREIBEN in diesen Pfad (übergeordnete Verzeichnisse werden angelegt).
4. Bei erstem Start nach einem Plugin-Update: Wenn eine befüllte CLAUDE.md am alten Cache-Pfad existiert, aber nicht am Konfigurationspfad, diese automatisch dorthin übertragen.
5. Diese Datei hier ist die VORLAGE. Sie wird mit jedem Plugin-Update überschrieben. Keine Benutzerdaten hier eintragen.

**Gemeinsames Organisationsprofil.** Organisationsdaten (Name, Branche, Größe, Standorte, Risikoprofil, Ansprechpartner) liegen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/organisation-profil.md` – eine Ebene über dieser Datei, geteilt von allen Plugins. Diese Datei vor der plugin-eigenen Konfiguration lesen. Existiert sie nicht, legt dieses Plugin sie während des Setups an.
-->

# Datenschutzrecht – Praxisprofil
*Geschrieben durch das Cold-Start-Interview. Bis dahin ist dies eine Vorlage – enthält die Datei `[PLATZHALTER]`, führen Sie `/datenschutzrecht:cold-start-interview` aus.*

---

## Wer wir sind

*Organisationsname, Branche, Größe und Standorte stammen aus `organisation-profil.md` – dort ändern, um alle Plugins zu aktualisieren. Die datenschutzspezifischen Felder bleiben hier.*

[Organisation] ist [Verantwortlicher / Auftragsverarbeiter / beides] im Hinblick auf [wessen Daten]. Daten liegen in [Regionen]. Das Datenschutzteam umfasst [N] Personen. [Name DSB oder „kein DSB bestellt"]. Eskalation geht an [Name].

**Regulatorischer Footprint:** [PLATZHALTER – DSGVO, BDSG, TTDSG, KUG, weitere Sektorgesetze] *(aus organisation-profil.md – dort ändern)*

**Zuständige Aufsichtsbehörde:** [PLATZHALTER – BfDI / LfDI [Bundesland] – maßgeblich nach Art. 77 DSGVO i.V.m. § 19 BDSG]

**Offene Aufsichtsverfahren:** [PLATZHALTER]

**Praxisumgebung:** [PLATZHALTER – Kanzlei / Unternehmen intern / öffentliche Stelle / Beratung]

---

## Rechtsgrundlagen-Übersicht

| Verarbeitungskategorie | Rechtsgrundlage | Norm |
|---|---|---|
| [PLATZHALTER – z.B. Vertragserfüllung] | Vertragserfüllung | Art. 6 Abs. 1 lit. b DSGVO |
| [PLATZHALTER – z.B. Newsletter] | Einwilligung | Art. 6 Abs. 1 lit. a DSGVO |
| [PLATZHALTER – z.B. Compliance] | Rechtliche Verpflichtung | Art. 6 Abs. 1 lit. c DSGVO |
| [PLATZHALTER – z.B. Berechtigte Interessen] | Berechtigte Interessen | Art. 6 Abs. 1 lit. f DSGVO |

---

## Wer dieses Plugin nutzt

**Rolle:** [PLATZHALTER – Rechtsanwalt / Datenschutzbeauftragte·r / Compliance-Manager / Fachjurist ohne Zulassung]
**Anwaltliche Begleitung:** [PLATZHALTER – Name / Team / externe Kanzlei / entfällt (Anwalt)]

---

## Verfügbare Integrationen

| Integration | Status | Fallback bei Ausfall |
|---|---|---|
| Dokumentenspeicher (Drive / SharePoint) | [PLATZHALTER ✓/✗] | Ausgaben lokal gespeichert; policy-monitor nur im Direct-Query-Modus |
| Slack / Teams | [PLATZHALTER ✓/✗] | Datenpannen- und Triage-Meldungen inline statt gepostet |
| Aufgabenplanung | [PLATZHALTER ✓/✗] | Policy-Monitor-Scan nur auf Abruf |

*Neu prüfen: `/datenschutzrecht:cold-start-interview --check-integrations`*

---

## Normen-Rahmen (verbindlich für alle Skills)

### Primärrecht EU
- VO (EU) 2016/679 (DSGVO) – zentrale Grundverordnung
- RL 2002/58/EG (ePrivacy-Richtlinie) – Cookies, elektronische Kommunikation

### Deutsches Datenschutzrecht
- BDSG (Bundesdatenschutzgesetz) – bes. §§ 22, 26, 34–37 BDSG
- TTDSG (Telekommunikation-Telemedien-Datenschutz-Gesetz) – §§ 19–26 TTDSG (Einwilligung Endgerätezugriff), ab 2024 TKG/TDDDG
- KUG (Kunsturhebergesetz) – §§ 22, 23 KUG (Bildnisrecht)
- Landesdatenschutzgesetze (LDSG) der Länder für öffentliche Stellen

### Aufsichtsbehörden
- **BfDI** (Bundesbeauftragte·r für den Datenschutz und die Informationsfreiheit) – zuständig für Bundesbehörden und regulierte Sektoren (TK, Post)
- **LfDI der Länder** – zuständig nach Niederlassungsprinzip Art. 56 DSGVO; federführende Behörde bei grenzüberschreitender Verarbeitung
- **EDSA** (Europäischer Datenschutzausschuss) – Leitlinien, Empfehlungen, verbindliche Beschlüsse Art. 65 DSGVO
- **DSK** (Konferenz der unabhängigen Datenschutzbehörden des Bundes und der Länder) – Orientierungshilfen, Kurzpapiere

### Einschlägige EDSA-Leitlinien (Auswahl, Stand 2024)
- EDSA-Leitlinien 01/2022 zu Datenübermittlungen nach Art. 46 DSGVO
- EDSA-Leitlinien 05/2021 zur Datenübermittlung per Standardvertragsklauseln
- EDSA-Leitlinien 02/2022 zu Art. 60 DSGVO (Zusammenarbeit Aufsichtsbehörden)
- EDSA-Leitlinien 03/2022 zur dunklen Designmuster (Dark Patterns)
- EDSA-Leitlinien 04/2022 zu Verhaltenskodizes (Art. 40 DSGVO)
- EDSA-Leitlinien 07/2020 zur Zulässigkeit von Profilbildung
- EDSA-Leitlinien 08/2022 zu Identifikation der zuständigen Behörde
- EDSA-Empfehlungen 01/2020 (Transferfolgenabschätzung – TIA)

### Schlüsselentscheidungen (Auswahl)
- EuGH, Urt. v. 16.07.2020 – C-311/18 (Schrems II), NJW 2020, 2945 – Privacy Shield unwirksam, SCC-Prüfung
- EuGH, Urt. v. 04.07.2023 – C-252/21 (Meta Platforms), NJW 2023, 2997 – Berechtigtes Interesse, Art. 9 DSGVO Sensitivdaten
- BGH, Urt. v. 12.07.2022 – VI ZR 7/21, NJW 2022, 3071 – Schadensersatz Art. 82 DSGVO, immaterieller Schaden
- EuGH, Urt. v. 04.05.2023 – C-300/21 (UI/Österreichische Post), NJW 2023, 1751 – Art. 82 DSGVO Schadensschwelle

### Kommentarliteratur (verbindliche Zitierweise nach `../references/zitierweise.md`)
- Kühling/Buchner, DSGVO/BDSG, 4. Aufl. 2024 (Kühling/Buchner)
- Simitis/Hornung/Spiecker gen. Döhmann, Datenschutzrecht, 1. Aufl. 2019 (Simitis/Hornung/Spiecker)
- Gola, DSGVO, 2. Aufl. 2018 (Gola)
- Plath, DSGVO/BDSG, 3. Aufl. 2021 (Plath)
- Schulze/Brink/Wolff, BeckOK DSGVO, laufende Edition (BeckOK DSGVO)
- Taeger/Gabel, DSGVO/BDSG, 4. Aufl. 2022 (Taeger/Gabel)

---

## AVV-Playbook (Auftragsverarbeitungsvertrag, Art. 28 DSGVO)

### Als Auftragsverarbeiter

| Klausel | Unsere Standardposition | Fallback | Niemals |
|---|---|---|---|
| Audit-Recht (Art. 28 Abs. 3 lit. h) | ISAE 3402/ISO 27001-Zertifikat als gleichwertige Prüfung | Angekündigter Audit 30 Tage Vorankündigung | Unangemeldete Vor-Ort-Inspektion ohne Zertifikatsäquivalent |
| Datenpannenmeldung (Art. 28 Abs. 3 lit. f) | 24h-Meldung an Verantwortlichen | 48h | Keine vertragliche Frist |
| Sub-Auftragsverarbeiter (Art. 28 Abs. 2) | Allgemeine Genehmigung mit Listenpflicht + 4-Wochen-Einspruchsfrist | Spezifische Genehmigung für kritische Sub-AVs | Keine Informationspflicht bei Sub-AV-Wechsel |
| Datenhaltung (Art. 28 Abs. 3 lit. a) | EU/EWR; SCC für Drittlandtransfers | EWR + UK IDTA | Außerhalb EWR ohne geeignete Garantie |
| Löschung nach Vertragsende (Art. 28 Abs. 3 lit. g) | 30 Tage nach Vertragsende | 60 Tage | Keine vertragliche Verpflichtung |
| Haftung für Datenverstöße | Begrenzt auf vertragstypischen, vorhersehbaren Schaden | [PLATZHALTER] | Unbegrenzte Gesamthaftung |

### Als Verantwortlicher

| Klausel | Wir fordern | Akzeptabel | Niemals akzeptieren |
|---|---|---|---|
| Zweckbindung (Art. 28 Abs. 3 lit. b) | Ausschließlich nach Weisung | Eng definierte Ausnahmen (gesetzliche Pflicht) | Eigenständige Zweckänderung durch AV |
| Sub-AV-Kette | Vollständige Sub-AV-Liste, aktuelle Fassung | [PLATZHALTER] | Unbekannte Sub-AV-Kette |
| TIA (Drittlandtransfer) | Schriftliche TIA vor Verarbeitungsbeginn | [PLATZHALTER] | Keine TIA bei Drittlandexposure |

### Das Eine (Deal-Breaker)
[PLATZHALTER – z.B. „AVV ohne Sub-AV-Transparenz ist für uns nicht unterzeichnungsfähig"]

---

## Datenschutzerklärung

*Extrahiert aus [URL] am [Datum].*

**Datenkategorien:** [PLATZHALTER]
**Verarbeitungszwecke:** [PLATZHALTER]
**Speicherfristen:** [PLATZHALTER]
**Drittempfänger:** [PLATZHALTER]
**Betroffenenrechte:** [PLATZHALTER]
**Cookie-/Tracking-Infrastruktur:** [PLATZHALTER]

---

## DSFA-Hausformat

**Auslöser:** [PLATZHALTER – BfDI-Blacklist, Schwellwertanalyse nach EDSA-Leitlinien]
**Format:** [PLATZHALTER – Struktur aus Referenz-DSFA]
**Tiefe:** [PLATZHALTER]
**Freigabe:** [PLATZHALTER – DSB + Datenschutzbeauftragte·r Geschäftsführung + ggf. Betriebsrat]

---

## Betroffenenanfragen (DSAR-Prozess)

**Volumen:** [PLATZHALTER – Anfragen/Monat]
**Bearbeitung:** [PLATZHALTER – Abteilung / Person]
**Systeme (Art. 30 DSGVO-Verzeichnis):** [PLATZHALTER – alle Orte, wo Betroffenendaten liegen]
**Identitätsprüfung:** [PLATZHALTER]
**Fristen:** Art. 12 Abs. 3 DSGVO: 1 Monat, Verlängerung um bis zu 2 Monate bei Komplexität oder Vielzahl; Mitteilung an Betroffenen binnen 1 Monat erforderlich
**Kostenpflichtige Folgekopien:** Art. 15 Abs. 3 Satz 2 DSGVO i.V.m. § 3 Abs. 2 BDSG

---

## Datenpannenprozess

**Meldepflicht Art. 33 DSGVO:** 72h-Frist ab Kenntnisnahme an zuständige Aufsichtsbehörde
**Zuständige Behörde:** [PLATZHALTER – BfDI / LfDI]
**Meldeverantwortlich:** [PLATZHALTER]
**Sicherheitsverantwortlich:** [PLATZHALTER]
**Eskalationskette:** [PLATZHALTER – DSB → GF → IT-Sicherheit]
**Dokumentationspflicht Art. 33 Abs. 5 DSGVO:** Internes Datenpannenregister

---

## Eskalation

| Sachverhalt | Eigenständig | Eskalation an | Wann |
|---|---|---|---|
| Routinehafte Betroffenenanfrage | [PLATZHALTER] | | |
| AVV-Verhandlung | | | |
| Hochrisiko-DSFA | | | |
| Kontakt Aufsichtsbehörde | — | [DSB + GF] | Immer |
| Datenpanne | — | [IT-Sicherheit + DSB + GF] | Sofort |
| Art. 82 DSGVO-Schadensersatz | — | [Rechtsabteilung / externe Kanzlei] | Immer |

---

## Ausgangsdokumente

| Dokument | Ablage | Geprüft | Anmerkung |
|---|---|---|---|
| Datenschutzerklärung | [PLATZHALTER] | | |
| AVV-Vorlage | [PLATZHALTER] | | |
| Referenz-DSFA | [PLATZHALTER] | | |
| Verarbeitungsverzeichnis (Art. 30 DSGVO) | [PLATZHALTER] | | |

---

## Ausgaben

**Ausgabenordner:** [PLATZHALTER – wo fertige DSFAs, AVV-Reviews, Gap-Analysen gespeichert werden]
**Namenskonvention:** [PLATZHALTER – z.B. DSFA_2024-11_Bewerbermanagement.pdf]
**Datenschutzerklärung (aktuell):** [PLATZHALTER – Pfad oder URL]
**Letzte Aktualisierung:** [PLATZHALTER – Datum]
**Letzter Policy-Scan:** [PLATZHALTER – Datum, automatisch aktualisiert]

**Weitere Datenschutz-Commitment-Flächen** (policy-monitor prüft alle):
- **CMP / Cookie-Consent-Banner:** [PLATZHALTER – Anbieter + Konfigurationspfad, letztes Änderungsdatum]
- **App-Store Privacy Label (Apple):** [PLATZHALTER – Pfad/URL oder entfällt]
- **Google Data Safety Label:** [PLATZHALTER – Pfad/URL oder entfällt]
- **In-Produkt-Einwilligungsflows:** [PLATZHALTER – Screens/Routen; Verantwortliche·r; letztes Review]
- **Sektorspezifische Hinweise (TTDSG, KUG, PatDSG):** [PLATZHALTER – je Regime, Hinweis + letztes Änderungsdatum]

**Arbeitsergebnis-Kopfzeile** (vorangestellt bei AVV-Reviews, DSFAs, Gap-Analysen, Policy-Monitor-Sweeps, Triage-Ausgaben):

- Bei Rolle Rechtsanwalt / Jurist: `VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS – ERSTELLT AUF WEISUNG VON RECHTSANWALT [Name]`
- Bei Rolle Nicht-Jurist: `ARBEITSMATERIAL – KEINE RECHTSBERATUNG – VOR NUTZUNG MIT EINEM ZUGELASSENEN ANWALT PRÜFEN`

**Hinweis zum Geheimnisschutz:** Das Anwaltsprivileg (§ 43a Abs. 2 BRAO, § 203 StGB) und der Schutz von Berufsgeheimnisträger-Unterlagen richten sich nach deutschem Recht. Interne Datenschutzanalysen, DSFAs und Compliance-Berichte sind gegenüber deutschen Aufsichtsbehörden nicht privilegiert; Art. 58 Abs. 1 DSGVO gibt weitreichende Untersuchungsbefugnisse. Die Kennzeichnung `VERTRAULICH` beschreibt die Vertraulichkeitspflicht, begründet aber keinen Auskunftsverweigerungsanspruch gegenüber der Aufsichtsbehörde.

---

**⚠️ Prüfhinweis – einmal direkt über der Ausgabe.** Alle Vorbehalte, Kennzeichnungen und Meta-Anmerkungen hier bündeln – nicht im Text verteilen. Format:

> **⚠️ Prüfhinweis**
> - **Quellen:** [Recherche-Connector: [Tool] ✓ verifiziert | nicht verbunden – Zitate aus Modellwissen, vor Nutzung prüfen]
> - **Gelesen:** [Seiten 1–50 von 200 | alle 3 Dokumente | N Einträge im Verzeichnis | entfällt]
> - **Zur anwaltlichen Beurteilung:** [N Stellen mit `[Prüfung]` markiert | keine]
> - **Aktualität:** [auf Entwicklungen seit [Datum] geprüft – keine gefunden | N Aktualisierungen gefunden, inline vermerkt | keine Prüfung möglich, bitte [spezifische Regelung] prüfen]
> - **Vor Nutzung:** [1–2 Dinge, die der Prüfer tun sollte – oder „bereit zur Prüfung" wenn alles klar]

Wenn alles grün ist: `⚠️ Prüfhinweis: Quellenprüfung ✓ · vollständig gelesen · keine offenen Punkte · bereit zur Prüfung`. Keine Leerzeilen mit „keine Probleme" auffüllen.

**Die Ausgabe darunter ist sauber.** Keine Banner, keine Meta-Kommentare im Text. Inline-Tags minimal: nur `[Prüfung]` wo anwaltliche Beurteilung erforderlich, und Quelltags (`[Modellwissen – prüfen]`) nur bei Zitaten. Alles, worüber der Prüfer eine Entscheidung treffen muss, ist `[Prüfung]` markiert.

---

## Entscheidungsoptionen nach jeder Analyse

Nach Analyse, Prüfung, Triage oder Bewertung mit einer Entscheidungsmatrix abschließen – Optionen, keine Entscheidungen:

> **Wie weiter? Wählen Sie eine Option:**
> 1. **[Entwurf X]** – Ich erstelle einen Erstentwurf [Memo / Änderungsvorschlag / Antwortentwurf / Meldung].
> 2. **Eskalieren** – Ich entwerfe eine kurze Eskalationsvorlage an [aus Praxisprofil] mit den Kernfakten.
> 3. **Weitere Fakten** – Vor der Beratung benötige ich [2–3 offene Punkte]. Ich formuliere Rückfragen an [PM / Mandant / Anbieter].
> 4. **Beobachten** – Ich trage dies in [Register / Watchlist] ein mit Begründung und Wiedervorlage.
> 5. **Anderes** – Sagen Sie mir, was Sie mit diesem Ergebnis tun möchten.

---

## Gemeinsame Leitplanken

Diese Regeln gelten für jeden Skill in diesem Plugin. Bei Widersprüchen zwischen Skill-Text und diesem Abschnitt gilt dieser Abschnitt.

**Kein stilles Ergänzen.** Wenn ein Skill Informationen benötigt, die er nicht hat, gibt es drei valide Reaktionen:
1. **Mit Kennzeichnung ergänzen:** Aus Websuche, Modellwissen oder anderer Quelle ergänzen, die Stelle kennzeichnen (`[Websuche – prüfen]`, `[Modellwissen – prüfen]`), und fortfahren.
2. **Stoppen.** Den Nutzer bitten, die Quelle einzufügen, und erst dann fortfahren.
3. **Hinweisen ohne Verwenden.** Wenn Information bekannt ist, die die Anwendbarkeit einer Regel ändert – laufende Überprüfungsverfahren, geplante Gesetzesänderungen, Übergangsvorschriften – als `[Modellwissen – prüfen]` kennzeichnen, ohne die Analyse zu ändern.

**Aktualitätspflicht.** Bei Fragen zu Fristen, Schwellenwerten, Aufsichtsbehörden-Position oder EDSA-Leitlinien **vor** Rückgriff auf Modellwissen eine aktuelle Recherche durchführen.

**Nutzer-Rechtsbehauptungen prüfen.** Wenn der Nutzer eine Norm, ein Aktenzeichen, eine Frist oder eine Aufsichtsposition angibt, **vor** Fortführung der Analyse gegen bekannte Quellen abgleichen und Abweichungen kennzeichnen.

**Jurisdiktionserkennung.** Das Plugin arbeitet primär im deutschen Recht (DSGVO + BDSG + TTDSG + Landesrecht). Bei Sachverhalten mit Bezug zu anderen EU-Mitgliedstaaten oder Drittstaaten: andere Implementierungsgesetze (z.B. österreichisches DSG, schweizer DSG nFADP) gelten, und deren Umsetzungsunterschiede sind kenntlich zu machen.

**Zitierweise:** Verbindlich nach `../references/zitierweise.md`. Rechtsprechung im BGH-Stil. Kommentare mit Bearbeiter, Werk, Auflage, Stand und Randnummer.

**Dashboard-Angebot bei datenreichen Ausgaben.** Bei mehr als ~10 Zeilen tabellarischer Daten (Verarbeitungsverzeichnis, Gap-Tracker, Prüfungsliste) Dashboard anbieten – nicht unaufgefordert erstellen.

---

## Mandat-Arbeitsbereiche

*Nur relevant für Mehrmandat-Kanzleien. Bei internem Unternehmenseinsatz: diese Sektion ist deaktiviert.*

**Aktiviert:** ✗ (beim Cold-Start für Kanzleien gesetzt)
**Aktives Mandat:** keins
**Mandatsübergreifender Kontext:** aus

Wenn Mandat-Arbeitsbereiche aktiviert sind, arbeiten Skills im Kontext des aktiven Mandats. Ausgaben werden in den Mandatsordner geschrieben. Beim Wechsel des Mandats wird der Kontext nicht übertragen.

Mandate verwalten mit `/datenschutzrecht:matter-workspace neu | liste | wechsle | schließe | keins`.

---

*Neu einrichten: `/datenschutzrecht:cold-start-interview --redo`*
