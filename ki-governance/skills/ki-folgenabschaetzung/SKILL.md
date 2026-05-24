---
name: ki-folgenabschaetzung
description: "KI-Folgenabschätzung (FRIA nach Art. 27 KI-VO + DSFA nach Art. 35 DSGVO) erstellen – strukturierte Aufnahme, Risikoanalyse, Regulierungsklassifizierung nach KI-VO und DSGVO, Richtlinien-Konsistenzprüfung und Empfehlung mit Bedingungen. Verwendet das Hausformat aus der Seed-Folgenabschätzung in der Praxisprofil-CLAUDE.md. Verwenden, wenn der Nutzer sagt „Folgenabschätzung für\", „diesen KI-Anwendungsfall bewerten\", „FRIA erstellen\", „KI-Folgenabschätzung generieren\", „wir müssen dieses KI-System dokumentieren\", „KI-Risikoprüfung für X\" oder nach einem bedingten Triage-Ergebnis."
---

# /ki-folgenabschätzung – KI-Folgenabschätzung

## Zweck

Die KI-Folgenabschätzung ist eine dokumentierte Entscheidung, kein Formular. Sie beantwortet:
Was tut dieses KI-System, wie gelangt es zu seinen Ergebnissen, wen betrifft es bei Fehlern,
welche Aufsicht besteht, und ist der Einsatz vertretbar?

Dieses Skill kombiniert zwei rechtlich eigenständige Instrumente:
- **FRIA (Fundamental Rights Impact Assessment)** nach Art. 27 KI-VO – für Betreiber
  hochriskanter KI-Systeme, insbesondere öffentliche Stellen sowie private Stellen, die
  öffentlich finanzierte Dienste erbringen oder Kreditwürdigkeitsbewertungen bzw.
  Lebens-/Krankenversicherungs-Risikobewertungen vornehmen.
- **DSFA (Datenschutz-Folgenabschätzung)** nach Art. 35 DSGVO – bei KI-Systemen, die
  personenbezogene Daten verarbeiten und ein hohes Risiko für die Rechte und Freiheiten
  natürlicher Personen begründen können.

Eine DSFA ist **keine** FRIA, und eine FRIA ist **keine** DSFA. Sie überschneiden sich häufig
und müssen parallel durchgeführt werden. Dieses Skill deckt beide ab und kennzeichnet explizit,
welche Abschnitte welchem Instrument zugehören.

## Eingaben

- Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
  (Hausformat Folgenabschätzung, Use-Case-Register, regulatorischer Fußabdruck)
- Systembeschreibung oder Triage-Ergebnis
- Seed-Folgenabschätzung (sofern im Setup übergeben)

## Rechtlicher Rahmen

### Kernvorschriften

- **Art. 27 KI-VO (VO 2024/1689)** — Folgenabschätzung für Grundrechte (FRIA): Betreiber hochriskanter KI-Systeme, insbesondere öffentliche Stellen sowie private Stellen, die öffentlich finanzierte Dienste erbringen oder Kreditwürdigkeitsbewertungen vornehmen, sind zur Durchführung verpflichtet.
- **Art. 35 DSGVO** — Datenschutz-Folgenabschätzung (DSFA): Pflicht bei hohem Risiko für Rechte und Freiheiten natürlicher Personen, insbesondere bei automatisierten Entscheidungen (Art. 22 DSGVO), Profiling oder Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- **Art. 22 DSGVO** — Automatisierte Einzelentscheidungen mit Rechtswirkung oder erheblicher Beeinträchtigung; nur bei Vorliegen einer Rechtsgrundlage nach Abs. 2 lit. a–c zulässig.
- **Art. 26, Art. 6 i.V.m. Anhang III KI-VO** — Betreiberpflichten bei Hochrisiko-KI; Klassifikation nach Anhang III bestimmt Pflichtumfang.
- **§ 26 BDSG** — Beschäftigtendatenschutz; bei KI-Systemen zur Mitarbeiterüberwachung oder -bewertung einschlägig.
- **§ 44b UrhG, Art. 4 DSM-RL** — Text- und Data-Mining-Schranke; Opt-out-Mechanismus bei Trainingsdaten.
- **§ 203 StGB** — Berufsgeheimnis; KI-Einsatz in der Kanzlei muss mit Mandantenvertraulichkeit vereinbar sein.

### Leitentscheidungen

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 Rn. 49 (Schufa-Score): Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung, wenn KI-Note maßgebliche Grundlage für Drittentscheidung; Maßstab für KI-Scoring in der DSFA.
- EuGH, Urt. v. 16.07.2020 – C-311/18, ECLI:EU:C:2020:559 (Schrems II), NJW 2020, 2613 Rn. 65: Drittstaatentransfer bei Anbieter-APIs; Prüfmaßstab für Art. 28 DSGVO-Auftragsverarbeitung durch KI-Anbieter in Drittstaaten.
- BGH, Urt. v. 13.01.2015 – VI ZR 204/14, NJW 2015, 1236 Rn. 12: Produkthaftung für fehlerhafte Informationsprodukte; übertragbarer Maßstab auf KI-Haftung für fehlerhafte Folgenabschätzungen.

### Kommentare

- Kühling/Buchner, in: Kühling/Buchner (Hrsg.), DSGVO BDSG, 4. Aufl. 2024, Art. 35 Rn. 21 (Voraussetzungen der DSFA-Pflicht).
- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 27 Rn. 3 (FRIA-Anforderungen für Betreiber).

## Ablauf

1. Praxisprofil lesen; Hausformat Folgenabschätzung bestätigen.
2. Risikotrack bestimmen (vereinfacht oder vollständig) anhand Governance-Stufe und
   Systemeigenschaften.
3. Aufnahme führen – gesprächig, kein Formular.
4. Regulierungsklassifizierung für jeden einschlägigen Rechtsakt im Fußabdruck – Risikoklasse,
   Verbots-Exposition, anwendbare Pflichten; Primärquellen zitieren.
5. Abschätzung im Hausformat schreiben.
6. Richtlinien-Diff gegen KI-Governance-Commitments in CLAUDE.md.
7. Ausgabe: Abschätzungsdokument + Bedingungsliste + Übergabe-Flags (Datenschutz DSFA,
   Vendor-Review bei Bedarf).

## Mandate-Kontext

Mandate-Workspaces-Einstellung aus CLAUDE.md prüfen. Bei aktivierten Workspaces und fehlendem
aktivem Mandat fragen: „Für welches Mandat? Oder Praxisebene?" Ausgaben in den Mandatsordner
schreiben.

---

## Schritt 0: Ist eine Folgenabschätzung erforderlich?

Auslöserkriterien aus CLAUDE.md prüfen.

**Unabhängig davon stets prüfen:**
- Trifft die KI eine oder beeinflusst sie wesentlich eine Entscheidung, die eine Person
  betrifft (Beschäftigung, Kredit, Zugang, Preisgestaltung, Content-Moderation)?
- Verarbeitet die KI personenbezogene Daten von Personen?
- Handelt es sich um ein kundenseitiges KI-System und nicht rein intern?
- Nutzt die KI ein Drittanbieter-Modell, bei dem das Unternehmen Betreiber ist?
- Liegt der Anwendungsfall in der Erhöhten oder Hohen Governance-Stufe?
- Ist das System nach Art. 6 KI-VO i.V.m. Anhang III als hochriskant eingestuft?

Wenn nichts zutrifft und der Hausauslöser nicht greift:
> „Eine vollständige Folgenabschätzung scheint nicht erforderlich. Hier ein Absatz für die
> Akte, der erklärt warum – für den Fall, dass jemand fragt."

---

## Schritt 1: Risikotrack

Vor der Aufnahme Track bestimmen. Tier-Definitionen aus CLAUDE.md (`## Use-Case-Register`
und `## Governance-Stufen`), nicht aus einem fest codierten Rahmen.

**Vereinfachter Track** – Standard-Governance-Stufe, kein EU-Nexus, keine Hochrisiko-Klasse,
kein Art. 35 DSGVO-Auslöser.

**Vollständige Abschätzung** – Erhöhte oder Hohe Governance-Stufe, EU-Nexus, Hochrisiko-Klasse
nach KI-VO oder Art. 35-Auslöser.

Im Zweifel vollständige Abschätzung. Ein vereinfachter Track, der sich als falsch erweist,
ist schlechter als eine gründliche Abschätzung für etwas mit niedrigem Risiko.

---

## Schritt 2: Aufnahme

Vor dem Schreiben Antworten auf folgende Fragen einholen. Gesprächig – kein Formular.

### Das System

- Was tut die KI? In Alltagssprache, nicht Marketingtext.
- Welches Modell oder welcher Anbieter treibt es an? Fine-tuned oder off-the-shelf?
- Wo sitzt es im Arbeitsablauf – assistierend (Mensch prüft Ausgabe), augmentierend (Mensch kann
  übersteuern, tut es aber meist nicht) oder automatisiert (kein Mensch im Ablauf)?
- Was ist die Ausgabe – generierter Text, ein Score, eine Klassifizierung, eine Empfehlung,
  eine Aktion?

### Betroffene Personen

- Wen betreffen die Ausgaben der KI – Mitarbeiter, Kunden, Dritte?
- Wenn die KI einen Fehler macht (False Positive, False Negative, Halluzination), wen
  trifft der Schaden und was ist der schlimmste realistische Fall?
- Sind schutzbedürftige Gruppen unverhältnismäßig betroffen – Minderjährige, Bewerber,
  Personen in finanzieller Not, Patienten?

### Eingaben und Daten

- Welche Daten verarbeitet die KI?
- Verarbeitet sie personenbezogene Daten? Von wem? (Art. 4 Nr. 1 DSGVO)
- Wurde das Modell auf Unternehmensdaten trainiert oder ist es ein Foundation Model ohne
  unternehmensspezifisches Training?
- Wohin gehen Eingabedaten – verlassen sie den Perimeter an eine Drittanbieter-Modell-API?
  (Auftragsverarbeitung Art. 28 DSGVO prüfen)
- Trainingsdaten-Transparenz: Falls eigene Daten zum Training verwendet wurden, UrhG-Prüfung
  (§ 44b UrhG, Art. 4 DSM-RL Text- und Data-Mining-Schranke) und GeschGehG-Prüfung.

### Entscheidungsfindung und Aufsicht

- Löst die KI-Ausgabe automatisch eine Aktion aus, oder entscheidet ein Mensch?
  (Automatisierte Entscheidungsfindung Art. 22 DSGVO prüfen)
- Falls menschliche Prüfung: Wie oft ändert der Mensch tatsächlich die Ausgabe der KI?
  (Wenn „selten" – der Mensch prüft nicht wirklich; er stempelt ab.)
- Gibt es ein Widerspruchs- oder Korrekturverfahren für betroffene Personen? (Art. 22 Abs. 3
  DSGVO; Art. 26 Abs. 6 KI-VO)
- Wer ist für die Ausgaben des KI-Systems verantwortlich – gibt es einen benannten Eigentümer?

### Genauigkeit und Fehler

- Was ist die bekannte oder geschätzte Fehlerrate? Welche Tests wurden durchgeführt?
- Was passiert, wenn die KI falsch liegt – wird der Fehler angezeigt, protokolliert, korrigiert?
- Wurden Bias-Tests durchgeführt? Gegenüber welchen demografischen Gruppen?

### Einsatzstufe und Umfang

- **Stufe:** Geplant und noch nicht gebaut / Pilotbetrieb / Live in Produktion / Live und skaliert?
- **Umfang:** Wie viele Personen sind ca. pro Monat/Jahr betroffen?
- **Verlauf:** Wurde es bereits bewertet? Gab es Entscheidungen, die angefochten oder
  aufgehoben wurden?

---

## Schritt 3: Regulierungsklassifizierung

**Schritt 3 Vorprüfung – Fußabdruckaktualität.** Betroffene Bevölkerungsgruppe und Entscheidungstyp
aus Schritt 2 gegen erfassten regulatorischen Fußabdruck prüfen. Falls der Anwendungsfall eine
neue betroffene Gruppe oder einen neuen Entscheidungstyp einführt, Regime neu ableiten statt
veralteten Fußabdruck zu iterieren.

Für jeden einschlägigen Rechtsakt im Fußabdruck:

**KI-VO (VO 2024/1689):**
- Risikoklasse nach Art. 6 KI-VO i.V.m. Anhang III `[prüfen]`
- Verbotene Praktiken Art. 5 KI-VO `[prüfen]`
- Betreiberpflichten Art. 26 KI-VO (technische Dokumentation, Protokollierung, menschliche
  Aufsicht, Unterrichtung von Arbeitnehmern) `[prüfen]`
- FRIA Art. 27 KI-VO – erforderlich? (Öffentliche Stellen oder öffentlich finanzierte private
  Dienste; Kreditwürdigkeit; Lebens-/Krankenversicherungs-Risikobewertung) `[prüfen]`
- Transparenzpflichten Art. 50 KI-VO (Chatbot-Offenlegung, Deepfake-Kennzeichnung) `[prüfen]`

**DSGVO / BDSG:**
- DSFA-Pflicht Art. 35 DSGVO – bei hohem Risiko für Rechte und Freiheiten, insbesondere bei
  automatisierten Entscheidungen (Art. 22), Profiling, Verarbeitung besonderer Kategorien
  (Art. 9) `[prüfen]`
- Auftragsverarbeitung Art. 28 DSGVO bei Drittanbietern `[prüfen]`
- Automatisierte Entscheidungsfindung Art. 22 DSGVO `[prüfen]`
- Beschäftigtendatenschutz § 26 BDSG bei Mitarbeiter-KI `[prüfen]`

**ProdHaftG / Produktsicherheitsrecht:**
- KI-System als Produkt i.S.d. ProdHaftG – Herstellerhaftung für fehlerhafte KI-Ausgaben
  bei körperlichen Schäden prüfen `[Modellwissen – prüfen]`

**§ 203 StGB:**
- Bei Kanzleieinsatz: Mandantengeheimnis und KI-Einsatz vereinbar? Welche Schutzmechanismen
  (On-Premise, Verarbeitung ohne Training) sind vorhanden? `[prüfen]`

**UrhG / GeschGehG:**
- Trainings- oder Input-Daten: § 44b UrhG-Schranke, Art. 4 DSM-RL Opt-out-Mechanismus,
  GeschGehG-Schutz für Modellarchitektur und proprietäre Daten `[prüfen]`

---

## Schritt 4: Abschätzung schreiben

Seed-Struktur aus CLAUDE.md verwenden. Falls keine erfasst, diese Grundstruktur:

```markdown
[ARBEITSPRODUKT-HEADER – gemäß Plugin-Konfiguration]

# KI-Folgenabschätzung: [System-/Funktionsname]

**Erstellt von:** [Name] | **Datum:** [Datum] | **Status:** ENTWURF / GENEHMIGT
**Systemeigentümer:** [Name] | **KI-Governance-Prüfer:** [Name]
**Governance-Stufe:** [Standard / Erhöht / Hoch]
**Track:** [Vereinfacht / Vollständig]
**Instrument:** [FRIA nach Art. 27 KI-VO / DSFA nach Art. 35 DSGVO / Beide]

---

## Zusammenfassung

[Zwei Sätze: Was tut diese KI und ist der Einsatz vertretbar? Z. B. „Dieses System nutzt
ein Drittanbieter-KI-System, um Erstentwürfe für Kundensupport-Antworten vor menschlicher Prüfung
zu erstellen. Die Verarbeitung ist mit der KI-Richtlinie des Unternehmens vereinbar;
drei Bedingungen vor dem Produktiveinsatz erforderlich."]

**Gesamtrisiko:** 🟢 Niedrig / 🟡 Mittel / 🟠 Hoch / 🔴 Sehr hoch

---

## 1. Systembeschreibung

**Funktion:** [Alltagssprache – kein Marketing]
**Modell / Anbieter:** [Wer liefert die KI]
**Einsatzmodus:** [Assistierend / Augmentierend / Automatisiert]
**Ausgabetyp:** [Text / Score / Klassifizierung / Empfehlung / Aktion]
**Status:** [Nicht gestartet / Pilotbetrieb / Produktion]

---

## 2. Betroffene Personen

**Wen es betrifft:** [Mitarbeiter / Kunden / Dritte]
**Umfang:** [Wie viele Personen, wie oft]
**Schaden bei Fehler:** [Realistischster Worst Case – konkret, nicht generisch]
**Schutzbedürftige Gruppen betroffen:** [Ja – [wer] / Nein]

---

## 3. Dateneingaben (DSGVO-relevant)

**Datenkategorien:** [Konkrete Felder, nicht „Nutzerdaten"]
**Personenbezogene Daten:** [Ja – [von wem] / Nein]
**Daten verlassen Perimeter?** [Ja – an [Anbieter] / Nein]
**Auftragsverarbeitung Art. 28 DSGVO:** [Vereinbarung vorhanden / Erforderlich / Entfällt]
**Modell-Training:** [Unternehmensdaten verwendet / Foundation Model / Fine-tuned auf [Datensatz]]
**UrhG § 44b / Art. 4 DSM-RL:** [Opt-out erklärt / Prüfung erforderlich / Entfällt] `[prüfen]`
**GeschGehG:** [Schutz proprietärer Daten sichergestellt / Prüfung erforderlich] `[prüfen]`

---

## 4. Entscheidungsfindung und Aufsicht

**Mensch im Ablauf:** [Immer / Nominell (Stempel-Risiko) / Nein]
**Übersteuerungsmechanismus:** [Wie ein Mensch eingreifen oder korrigieren kann]
**Art. 22 DSGVO anwendbar?** [Ja – vollautomatisierte Entscheidung / Nein] `[prüfen]`
**Widerspruchs-/Korrekturverfahren:** [Ja – [wie] / Nein]
**Benannter Eigentümer:** [Name oder Rolle]

---

## 5. Genauigkeit und Verzerrungen

**Fehlerrate:** [Bekannt / Geschätzt / Nicht getestet]
**Fehlermodus:** [Was passiert, wenn die KI falsch liegt – angezeigt? protokolliert? korrigiert?]
**Bias-Test:** [Durchgeführt – [Ergebnisse] / Nicht durchgeführt / Nicht zutreffend]

---

## 6. Regulierungsklassifizierung

### 6.1 KI-VO (VO 2024/1689)

**Klassifizierung:** [Klasse + Pinpoint-Zitat der maßgeblichen Bestimmung] `[prüfen]`
**Verbotene Praktiken ausgelöst?** [Keine erkannt / [konkrete Bestimmung und warum]] `[prüfen]`
**Anwendbare Betreiberpflichten:** [Art. 26 KI-VO – Liste mit Zitaten] `[prüfen]`
**FRIA Art. 27 KI-VO erforderlich?** [Ja – separate Lieferung / Nein / Prüfung erforderlich] `[prüfen]`
**Art. 50 Transparenzpflichten:** [Offenlegung erforderlich / Entfällt] `[prüfen]`
**Inkrafttreten/Durchsetzungsdatum:** [Datum(en)] `[prüfen]`
**Offene Auslegungsfragen:** [Markierungen]

### 6.2 DSGVO / BDSG

**DSFA Art. 35 DSGVO erforderlich?** [Ja – gesonderte Durchführung / Nein] `[prüfen]`
**Art. 22 DSGVO (automatisierte Entscheidung):** [Greift / Greift nicht / Prüfung erforderlich] `[prüfen]`
**Art. 28 DSGVO (Auftragsverarbeitung):** [AVV abgeschlossen / Erforderlich / Entfällt] `[prüfen]`
**§ 26 BDSG (Beschäftigtendatenschutz):** [Einschlägig / Nicht einschlägig] `[prüfen]`

### 6.3 Sonstige einschlägige Rechtsakte

**ProdHaftG:** [Haftungsanalyse erforderlich / Entfällt] `[prüfen]`
**§ 203 StGB:** [Mandantengeheimnis gewahrt / Schutzmaßnahmen erforderlich] `[prüfen]`
**UrhG § 44b / GeschGehG:** [Trainingsdaten-Compliance sichergestellt / Prüfung erforderlich] `[prüfen]`

---

## 7. Richtlinien-Konsistenz

| Richtlinien-Commitment | Konsistent? | Hinweise |
|---|---|---|
| [Commitment aus CLAUDE.md KI-Richtlinien-Verpflichtungen] | 🟢 / 🟡 / 🟠 / 🔴 | |

[Falls ein Punkt 🟡 oder schlechter: Richtlinienaktualisierung vor dem Einsatz oder Design-
Änderung erforderlich. Einer von beiden muss sich ändern – nicht beides markiert lassen.]

---

## 8. Risiken und Mitigationen

| # | Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Mitigation | Status | Eigentümer |
|---|---|---|---|---|---|---|
| 1 | [Konkretes Risiko, das an diesem Design haftet – nicht generisch „KI-Halluzination"] | N/M/H | N/M/H | [Konkrete Maßnahme] | Erledigt / Geplant / Lücke | [Name] |

**Restrisiko nach Mitigationen:** [Bewertung]

---

## 9. Empfehlung

**[GENEHMIGT / GENEHMIGT MIT BEDINGUNGEN / ÄNDERUNGEN ERFORDERLICH / NICHT GENEHMIGT]**

**Bedingungen (sofern vorhanden):**
- [ ] [Konkrete Maßnahme vor dem Einsatz – Eigentümer, Frist]

**DSFA Art. 35 DSGVO erforderlich?** [Ja – Datenschutzrecht-Plugin ausführen / Nein]
**FRIA Art. 27 KI-VO als separate Lieferung?** [Ja / Nein]
**Vendor-AI-Review erforderlich?** [Ja – `/ki-governance:ki-anbieter-prüfung` / Nein]

**Freigabe:** [Name, Datum]

---

## Zitatprüfung

Regulierungszitate in Abschnitt 6 wurden von einem KI-Modell generiert und nicht gegen
Primärquellen verifiziert. Vor Zertifizierung oder Nutzung der Abschätzung jeden zitierten
Artikel gegen EUR-Lex oder Gesetze im Internet prüfen: Pinpoint, Aktualität, Durchführungsakte.
`[Modellwissen – prüfen]`-Markierungen tragen das höchste Fabrikationsrisiko und sollten
zuerst geprüft werden.
```

## Ausgabeformat

Das Ausgabedokument folgt der Seed-Struktur aus CLAUDE.md (Schritte 4 und 7). Das Dokument enthält:

1. **Arbeitsergebnis-Kopfzeile** (gemäß Plugin-Konfiguration, privilegiert und vertraulich)
2. **Zusammenfassung** — zwei Sätze: Was tut diese KI, ist der Einsatz vertretbar?
3. **Gesamtrisiko-Bewertung** — 🟢 Niedrig / 🟡 Mittel / 🟠 Hoch / 🔴 Sehr hoch
4. **Abschnitte 1–9** (Systembeschreibung, Betroffene, Daten, Aufsicht, Genauigkeit, Klassifizierung, Richtlinien, Risiken, Empfehlung)
5. **Bedingungsliste** mit benannten Eigentümern und Fristen
6. **Weiterleitungs-Flags**: DSFA-Pflicht? Vendor-Review erforderlich?

Bei vereinfachtem Track: Abschnitte 1–3 und Abschnitt 9 sind Pflicht; Abschnitte 4–8 können zusammengefasst werden.

## Beispiel

**Anfrage:** „Wir wollen einen Chatbot für die Erstberatung von Mandanten einsetzen — was müssen wir prüfen?"

**Ablauf:**
- Risikotrack: Vollständig (erhöhte Governance-Stufe; Drittanbieter-KI-System; Mandantendaten).
- Art. 6 KI-VO i.V.m. Anhang III: Kein Hochrisiko erkennbar (keine Einstellungs- oder Kreditentscheidung). `[prüfen-pinpoint]`
- DSFA Art. 35 DSGVO: Prüfung erforderlich — Verarbeitung von Mandantendaten durch Drittanbieter-API (Art. 28 DSGVO); mögliche automatisierte Empfehlungen.
- Art. 50 KI-VO: Chatbot-Offenlegungspflicht gegenüber Mandanten.
- § 203 StGB: Mandantengeheimnis — Auftragsverarbeitungsvertrag mit KI-Anbieter erforderlich, Verarbeitung ohne Training sicherstellen.

**Ergebnis:** GENEHMIGT MIT BEDINGUNGEN — Art. 28 DSGVO AVV abschließen; Chatbot-Offenlegung implementieren; DSFA durchführen; Mandanteneinwilligung einholen.

## Quellenpflicht

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

**Leitende Normen:**
- Art. 27 KI-VO (VO 2024/1689) – FRIA `[Primärquelle – EUR-Lex]`
- Art. 35 DSGVO – DSFA `[Primärquelle – EUR-Lex]`
- Art. 5, 6, 14, 26, 50 KI-VO `[Primärquelle – EUR-Lex]`
- Art. 22, 28 DSGVO – Automatisierte Entscheidungen, Auftragsverarbeitung `[Primärquelle – EUR-Lex]`
- § 26 BDSG – Beschäftigtendatenschutz `[Primärquelle – gesetze-im-internet.de]`
- § 44b UrhG – Text- und Data-Mining-Schranke `[Primärquelle – gesetze-im-internet.de]`
- Art. 4 Richtlinie (EU) 2019/790 (DSM-RL) – Text- und Data-Mining `[Primärquelle – EUR-Lex]`
- § 203 StGB – Mandantengeheimnis `[Primärquelle – gesetze-im-internet.de]`

**Leitentscheidungen:**
- EuGH, Urt. v. 16.07.2020 – C-311/18, ECLI:EU:C:2020:559 (Schrems II), NJW 2020, 2613 Rn. 65 – Drittstaatentransfer bei Anbieter-APIs; Prüfmaßstab für Auftragsverarbeiter-APIs in KI-Systemen `[Modellwissen – prüfen]`
- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 Rn. 49 – Schufa-Score: Automatisiertes Profiling als Art. 22 Abs. 1 DSGVO-Entscheidung bei maßgeblicher Grundlage für Drittentscheidung; Maßstab für KI-Scoring in DSFA `[Modellwissen – prüfen]`
- BGH, Urt. v. 13.01.2015 – VI ZR 204/14, NJW 2015, 1236 Rn. 12 – Produkthaftung für fehlerhafte Informationsprodukte; übertragbarer Maßstab auf KI-Haftung `[Modellwissen – prüfen]`

**Kommentarliteratur:**
- Kühling/Buchner, in: Kühling/Buchner (Hrsg.), DSGVO BDSG, 4. Aufl. 2024, Art. 35 Rn. 21
- Frenzel, in: Paal/Pauly, DSGVO BDSG, 3. Aufl. 2021, Art. 22 Rn. 12
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 27 Rn. 3 (FRIA-Anforderungen)

## Risiken / typische Fehler

- **FRIA und DSFA verwechseln.** Beide Instrumente explizit kennzeichnen und als getrennte
  Lieferungen behandeln, wenn beide erforderlich sind.
- **Art. 22 DSGVO ignorieren.** Bei automatisierten Entscheidungen immer auf vollständige
  Automatisierung prüfen – auch bei nominell menschlicher Prüfung (Stempel-Risiko).
- **Pinpoint-Zitate ohne Prüfung.** Artikel-Nummern der KI-VO haben sich während der
  Konsolidierung verschoben; jeden Pinpoint gegen den Amtsblatttext prüfen.
- **Zu viele generische Risiken.** Ziel: 2–5 echte, am Design haftende Risiken, nicht 12
  aufgeblähte.
- **Zertifizierung ohne Anwalt (bei Nicht-Juristen).** Vor Genehmigungsstempel auf
  Anwaltsprüfung bestehen.
