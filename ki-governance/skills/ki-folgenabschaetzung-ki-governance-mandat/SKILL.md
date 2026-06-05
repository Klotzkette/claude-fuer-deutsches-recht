---
name: ki-folgenabschaetzung-ki-governance-mandat
description: "Folgenabschaetzung KI Governance Mandat: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Folgenabschaetzung KI Governance Mandat

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Folgenabschaetzung KI Governance Mandat** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ki-folgenabschaetzung` | KI-Folgenabschätzung (FRIA nach Art. 27 KI-VO + DSFA nach Art. 35 DSGVO) erstellen – strukturierte Aufnahme, Risikoanalyse, Regulierungsklassifizierung nach KI-VO und DSGVO, Richtlinien-Konsistenzprüfung und Empfehlung mit Bedingungen. Verwendet das Hausformat aus der Seed-Folgenabschätzung in der Praxisprofil-CLAUDE.md. Verwenden, wenn der Nutzer sagt "Folgenabschätzung für", "diesen KI-Anwendungsfall bewerten", "FRIA erstellen", "KI-Folgenabschätzung generieren", "wir müssen dieses KI-System dokumentieren", "KI-Risikoprüfung für X" oder nach einem bedingten Triage-Ergebnis. |
| `ki-governance-anpassen` | Geführte Anpassung Ihres KI-Governance-Praxisprofils – eine Einstellung ändern, ohne das vollständige Kaltstart-Interview neu zu starten. Risikoeinstellung, Eskalationskontakte, Use-Case-Register-Einträge, Vendor-KI-Positionen, KI-Richtlinien-Commitments, Folgenabschätzungs-Hausformat oder Mandats-Workspace-Pfade anpassen. Verwenden, wenn der Nutzer sagt "ändere mein [Ding]", "Profil aktualisieren", "Konfiguration bearbeiten", "Playbook anpassen" oder "anpassen". |
| `ki-governance-mandat-arbeitsbereich` | Mandats-Arbeitsbereiche verwalten – neu, liste, wechseln, schließen oder keines (Praxisebene). Datei- Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen. Verwenden, wenn mandatsübergreifend gearbeitet wird, wenn der Nutzer sagt "neues Mandat", "Mandat wechseln", "Mandate auflisten", "Mandat schließen" oder wenn ein inhaltlicher Skill wissen muss, in welchem Mandat er arbeitet. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Folgenabschaetzung KI Governance Mandat**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ki-folgenabschaetzung`

**Fokus:** KI-Folgenabschätzung (FRIA nach Art. 27 KI-VO + DSFA nach Art. 35 DSGVO) erstellen – strukturierte Aufnahme, Risikoanalyse, Regulierungsklassifizierung nach KI-VO und DSGVO, Richtlinien-Konsistenzprüfung und Empfehlung mit Bedingungen. Verwendet das Hausformat aus der Seed-Folgenabschätzung in der Praxisprofil-CLAUDE.md. Verwenden, wenn der Nutzer sagt "Folgenabschätzung für", "diesen KI-Anwendungsfall bewerten", "FRIA erstellen", "KI-Folgenabschätzung generieren", "wir müssen dieses KI-System dokumentieren", "KI-Risikoprüfung für X" oder nach einem bedingten Triage-Ergebnis.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
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
aktivem Mandat fragen: "Für welches Mandat? Oder Praxisebene?" Ausgaben in den Mandatsordner
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
> "Eine vollständige Folgenabschätzung scheint nicht erforderlich. Hier ein Absatz für die
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
 (Wenn "selten" – der Mensch prüft nicht wirklich; er stempelt ab.)
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

[Zwei Sätze: Was tut diese KI und ist der Einsatz vertretbar? Z. B. "Dieses System nutzt
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

**Datenkategorien:** [Konkrete Felder, nicht "Nutzerdaten"]
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
| 1 | [Konkretes Risiko, das an diesem Design haftet – nicht generisch "KI-Halluzination"] | N/M/H | N/M/H | [Konkrete Maßnahme] | Erledigt / Geplant / Lücke | [Name] |

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

**Anfrage:** "Wir wollen einen Chatbot für die Erstberatung von Mandanten einsetzen — was müssen wir prüfen?"

**Ablauf:**
- Risikotrack: Vollständig (erhöhte Governance-Stufe; Drittanbieter-KI-System; Mandantendaten).
- Art. 6 Abs. 2 KI-VO i. V. m. Anhang III: Typischer Mandanten-Erstberatungs-Chatbot ist nicht schon deshalb Hochrisiko, weil er ein allgemeines KI-System nutzt. Entscheidend ist die Zweckbestimmung: Hochrisiko erst bei Einsatz für einen Anhang-III-Zweck, etwa Justiz-/Rechtsdurchsetzungsentscheidung, Beschäftigung, Kreditwürdigkeit oder Zugang zu wesentlichen Diensten.
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
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

## Triage zu Beginn
1. Liegt ein Hochrisiko-KI-System nach Art. 6 KI-VO i.V.m. Anhang III vor (Nr. 1-8)?
2. Ist eine DSFA nach Art. 35 DSGVO erforderlich — automatisierte Entscheidung, Profiling, Art. 9-Daten?
3. Sind personenbezogene Daten betroffen — verlassen sie den Perimeter an Drittanbieter-API?
4. Handelt es sich um eine oeffentliche Stelle oder einen oeffentlich finanzierten Dienst (FRIA Art. 27 KI-VO)?
5. Ist der Einsatz assistierend oder vollautomatisiert — Stempel-Risiko beim nominellen Human-Review?

## Output-Template — Folgenabschaetzungs-Zusammenfassung
**Adressat:** Systemeigentuemer / Governance-Team — Tonfall: strukturiert-berichtend
```
KI-FOLGENABSCHAETZUNG — ZUSAMMENFASSUNG
[DATUM] — System: [SYSTEMNAME] — Status: ENTWURF / GENEHMIGT

Governance-Stufe: [Standard / Erhoeht / Hoch]
Instrument: [FRIA Art. 27 KI-VO / DSFA Art. 35 DSGVO / Beide]

GESAMTRISIKO: [NIEDRIG / MITTEL / HOCH / SEHR HOCH]

KLASSIFIZIERUNG:
- KI-VO: [Risikoklass + Art./Anhang-III-Nr.]
- DSGVO Art. 22: [Einschlaegig / Nicht einschlaegig]
- FRIA Art. 27 KI-VO: [Erforderlich / Nicht erforderlich]
- DSFA Art. 35 DSGVO: [Erforderlich / Nicht erforderlich]

EMPFEHLUNG: [GENEHMIGT / GENEHMIGT MIT BEDINGUNGEN / ABGELEHNT]

Bedingungen:
1. [BEDINGUNG — Eigentuemer: NAME — Frist: DATUM]
2. [BEDINGUNG — Eigentuemer: NAME — Frist: DATUM]

Weiterleitungs-Flags:
- Vendor-Review: [Ja / Nein]
- Separate DSFA: [Ja / Nein]

Freigabe: [NAME], [DATUM]
```

## 2. `ki-governance-anpassen`

**Fokus:** Geführte Anpassung Ihres KI-Governance-Praxisprofils – eine Einstellung ändern, ohne das vollständige Kaltstart-Interview neu zu starten. Risikoeinstellung, Eskalationskontakte, Use-Case-Register-Einträge, Vendor-KI-Positionen, KI-Richtlinien-Commitments, Folgenabschätzungs-Hausformat oder Mandats-Workspace-Pfade anpassen. Verwenden, wenn der Nutzer sagt "ändere mein [Ding]", "Profil aktualisieren", "Konfiguration bearbeiten", "Playbook anpassen" oder "anpassen".

# /anpassen

## Zweck

Der Nutzer hat `/ki-governance:ki-governance-anpassen` eingegeben. Er möchte etwas in seinem Praxisprofil
ändern – eine Risikoeinstellung, einen Eskalationskontakt, eine Playbook-Position, eine
Jurisdiktion, ein Ausgabeformat – ohne das gesamte Kaltstart-Interview neu zu starten und
ohne YAML manuell zu bearbeiten.

## Eingaben

- Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
 und `unternehmens-profil.md` (eine Ebene höher)
- Beschreibung der gewünschten Änderung vom Nutzer

## Ablauf

1. **Konfiguration lesen.** CLAUDE.md und unternehmens-profil.md lesen. Falls CLAUDE.md nicht
 existiert oder noch `[PLATZHALTER]`-Werte enthält:

 > Sie haben noch kein Setup durchgeführt. Führen Sie zuerst `/ki-governance:ki-governance-kaltstart-interview`
 > aus – anpassen dient der Anpassung eines bereits vorhandenen Profils.

2. **Anpassbare Karte anzeigen.** Auflisten, was im Profil steht, gruppiert, mit
 einzeiliger Zusammenfassung des aktuellen Werts:

 - **Unternehmen / Wer Sie sind** – Name, Branche, Jurisdiktionen, Phase, Praxiskontext
 *(geteilt über alle Plugins – Änderungen fließen durch `unternehmens-profil.md`)*
 - **Regulatorischer Fußabdruck** – KI-VO, DSGVO/BDSG, sektorspezifische Regelwerke
 im Anwendungsbereich
 - **Risikoeinstellung** – konservativ / mittig / progressiv, was das für Triage- und
 Folgenabschätzungs-Ausgaben bedeutet
 - **Personen** – Governance-Team, KI-Risikobeauftragter, Eskalationskette, Genehmiger
 - **Use-Case-Register** – genehmigte / bedingte / nie-Einträge und zugehörige Bedingungen
 - **KI-System-Inventar** – je System: Rolle (Anbieter / Betreiber usw.) und Risikoklasse
 nach KI-VO. `/ki-governance:ki-inventar` für den dedizierten Editor verwenden.
 - **Vendor-KI-Governance** – Trainings-auf-Daten, Haftung, Modell-Änderungsmeldung,
 Art. 28 DSGVO AVV, Art. 11 KI-VO Technische Dokumentation und andere Positionen
 - **KI-Richtlinien-Commitments** – öffentliche oder interne Commitments, gegen die das
 Plugin abgleicht
 - **Folgenabschätzungs-Hausformat** – FRIA-/DSFA-Abschnittsreihenfolge, Risiko-Scoring-Format,
 Stakeholder-Framing
 - **Ablauf** – Aufnahme-Pfad, Ausgabeformat, Mandats-Workspace-Pfade, Prüfkadenz für
 den Policy-Monitor
 - **Integrationen** – was verbunden ist (Slack, Dokumentenspeicher, geplante Aufgaben),
 was zurückfällt

3. **Fragen, was geändert werden soll.**

 > Was möchten Sie anpassen? Wählen Sie einen Abschnitt oder beschreiben Sie die Änderung
 > in eigenen Worten.

4. **Änderung vornehmen.** Aktuellen Wert zeigen, neuen Wert abfragen, nachgelagerte
 Auswirkungen erklären, bestätigen, in Konfiguration schreiben.

 Beispiele für nachgelagerte Erklärungen:
 - *Risikoeinstellung mittig → konservativ:* "Ich werde mehr Anwendungsfälle als bedingt
 statt genehmigt markieren, mehr Folge-Prüfungen zur Folgenabschätzung einleiten und
 konservativere Vendor-KI-Redlines empfehlen."
 - *Eskalationskontakt hinzufügen:* "Jeder Skill, der Eskalationen weiterleitet
 (`/anwendungsfall-triage`, `/ki-anbieter-prüfung`, `/regulierungs-lücken-analyse`), wird diesen Kontakt
 nun auf den relevanten Risikostufen einschließen."
 - *Neuer Use-Case-Register-Eintrag:* "`/anwendungsfall-triage` gleicht beim nächsten Lauf
 gegen diesen Eintrag ab. Bestehende Folgenabschätzungen werden nicht neu geschrieben –
 führen Sie sie neu aus, wenn Sie die neue Position darin gespiegelt sehen möchten."

5. **Bei Änderungen am gemeinsamen Profil** (Unternehmensname, Branche, Jurisdiktionen,
 Praxiskontext):
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/unternehmens-profil.md` schreiben
 und vermerken:

 > Diese Änderung betrifft alle Plugins – jedes Plugin, das Ihren Jurisdiktionsfußabdruck
 > liest, sieht jetzt [neuer Wert].

6. **Abschluss.**

 > Erledigt. Ihr nächstes Ergebnis wird die Änderung widerspiegeln. Noch etwas? Sie können
 > `/ki-governance:ki-governance-anpassen` jederzeit ausführen.

## Quellen und Zitierweise

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

Downstream-Auswirkungen von Konfigurationsänderungen können folgende Normen betreffen:
- Art. 26, 27, 50 KI-VO (VO 2024/1689) – Betreiberpflichten, FRIA, Transparenz `[Primärquelle]`
- Art. 35 DSGVO – DSFA-Pflicht `[Primärquelle]`
- Art. 28 DSGVO – Auftragsverarbeitung `[Primärquelle]`

## Ausgabeformat

Interaktiver Dialog: Karte → Auswahl → aktueller Wert / neuer Wert → Bestätigung → Schreiben.

## Risiken / typische Fehler

- **Abschnitt nicht löschen.** Falls der Nutzer etwas "entfernen" möchte, auf
 `[Nicht konfiguriert]` setzen und erklären, was das für das Plugin-Verhalten bedeutet.
 ("Das Entfernen Ihrer Eskalationskette bedeutet, dass `/anwendungsfall-triage` eskalationswürdige
 Punkte markiert, aber nicht an eine bestimmte Person weiterleitet.")
- **Interne Inkonsistenz markieren.** Falls die Änderung das Profil inkonsistent machen würde
 (z. B. Risikoeinstellung progressiv + Eskalation "alles geht an den GC"; oder "KI-VO im
 Anwendungsbereich" + "keine Systeme für EU markiert"), Spannung aufzeigen und fragen,
 welche Seite der Nutzer möchte.
- **Leitplanken-Degradation markieren.** Falls der Nutzer eine Leitplanke deaktivieren
 möchte ("`[prüfen]`-Flag nicht mehr hinzufügen", "Zitats-Warnung weglassen"), erklären,
 wovor die Leitplanke schützt, und die Trade-offs bestätigen. Strukturelle Leitplanken:
 - `[prüfen]`-Markierungs-Mechanismus (zeigt dem Nutzer, wann juristisches Urteil
 erforderlich ist) – tragend, nicht entfernen.
 - Quellenattribuierungs-Tags auf abgerufenem Inhalt – tragend, nicht entfernen.
 - `[prüfen]`-Tags auf zitierten Normen/Vorschriften – tragend, nicht entfernen.
- **Eine Änderung auf einmal.** Nicht das gesamte Interview neu stellen. Bei mehreren
 Änderungen sequenziell vorgehen und jede vor dem Weitermachen bestätigen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 5 KI-VO — verbotene Praktiken (jede Profileinstellung muss dagegen gecheckt werden)
- Art. 26/29 KI-VO — Betreiberpflichten (Anpassungen an Hochrisiko-Einstellungen)
- Art. 22 DSGVO — automatisierte Einzelentscheidungen
- Art. 35 DSGVO — DSFA-Ausloeser
- § 87 Abs. 1 Nr. 6 BetrVG — Mitbestimmungsrecht bei Mitarbeiter-KI

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welcher Abschnitt des Praxisprofils soll geaendert werden — Risikoeinstellung, Register, Eskalation?
2. Hat die Aenderung nachgelagerte Auswirkungen auf andere Skills (Triage, Folgenabschaetzung)?
3. Betrifft die Aenderung die Eskalationsmatrix — wer ist neuer Genehmiger?
4. Wird eine Leitplanke degradiert — welche Schutzfunktion entfaellt?
5. Sind Aenderungen am gemeinsamen Profil (unternehmens-profil.md) betroffen?

## Output-Template — Profil-Aenderungsbestaetigung
**Adressat:** KI-Governance-Verantwortlicher — Tonfall: knapp, bestaedigend
```
PROFIL-AENDERUNGSBESTAETIGUNG
[DATUM] — Geaenderter Abschnitt: [ABSCHNITT]

Alte Einstellung: [ALTER WERT]
Neue Einstellung: [NEUER WERT]

Nachgelagerte Auswirkungen:
- [SKILL X]: [BESCHREIBUNG AUSWIRKUNG]
- [SKILL Y]: [BESCHREIBUNG AUSWIRKUNG]

Leitplanken: [KEINE DEGRADATION / DEGRADIERT: BESCHREIBUNG UND BESTAETIGUNG]

Naechste Pruefung: [DATUM]
Geaendert von: [NAME], [DATUM]
```

## 3. `ki-governance-mandat-arbeitsbereich`

**Fokus:** Mandats-Arbeitsbereiche verwalten – neu, liste, wechseln, schließen oder keines (Praxisebene). Datei- Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen. Verwenden, wenn mandatsübergreifend gearbeitet wird, wenn der Nutzer sagt "neues Mandat", "Mandat wechseln", "Mandate auflisten", "Mandat schließen" oder wenn ein inhaltlicher Skill wissen muss, in welchem Mandat er arbeitet.

# /mandat-arbeitsbereich

## Zweck

Kanzleipraktiker arbeiten mit mehreren Mandanten und Mandaten. Ein Mandats-Workspace hält
den Kontext eines Mandanten oder Auftrags von jedem anderen getrennt – relevant für
§ 43a Abs. 2 BRAO (anwaltliche Verschwiegenheitspflicht) und § 203 StGB (Mandantengeheimnis).
Dieser Skill verwaltet diese Workspaces.

## Eingaben

- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
 (Abschnitt `## Mandate-Workspaces`)
- Subbefehl und optionaler Slug vom Nutzer

## Ablauf

1. CLAUDE.md lesen – bestätigen, dass der Abschnitt `## Mandate-Workspaces` vorhanden ist.
 Falls `Aktiviert` = `✗`:
 > Mandate-Workspaces sind deaktiviert – Sie sind als In-house-Praxis mit einem Mandanten
 > konfiguriert, sodass das Plugin automatisch vom Praxiskontext arbeitet. Wenn Sie
 > tatsächlich für mehrere Mandanten arbeiten, führen Sie `/ki-governance:ki-governance-kaltstart-interview
 > --redo` neu aus und wählen einen Kanzleikontext. Andernfalls benötigen Sie `/mandat-arbeitsbereich`
 > nicht.

2. Auf den ersten Token von `$ARGUMENTS` verzweigen:
 - `new` → Aufnahme-Interview starten, `mandat.md` schreiben, `verlauf.md` und `notizen.md`
 initialisieren.
 - `list` → Alle `mandate/*/mandat.md` auflisten; Tabelle drucken; aktives Mandat markieren.
 - `switch` → `Aktives Mandat:`-Zeile in CLAUDE.md aktualisieren.
 - `close` → `mandate/<slug>/` nach `mandate/_archiv/<slug>/` verschieben; Schließdatum
 in `verlauf.md` protokollieren.
 - `none` → `Aktives Mandat:` auf `keines – nur Praxiskontext` setzen.

3. Dem Nutzer zeigen, was sich geändert hat, und vor dem Schreiben bestätigen.

## Subbefehle

- `/ki-governance:ki-governance-mandat-arbeitsbereich new <slug>` – neuen Mandats-Workspace anlegen, kurzes
 Aufnahme-Interview, `mandat.md` schreiben
- `/ki-governance:ki-governance-mandat-arbeitsbereich list` – Mandate mit Status und Aktiv-Flag auflisten
- `/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>` – aktives Mandat setzen
- `/ki-governance:ki-governance-mandat-arbeitsbereich close <slug>` – Mandat archivieren (nach
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/mandate/_archiv/` verschieben, nie löschen)
- `/ki-governance:ki-governance-mandat-arbeitsbereich none` – von aktivem Mandat trennen, nur auf Praxisebene
 arbeiten

## Speicherlayout

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/
├── CLAUDE.md # praxisweites Praxisprofil
└── mandate/
 ├── <slug>/
 │ ├── mandat.md # Mandant, Gegenseite, Mandatstyp, Kernfakten, Abweichungen
 │ ├── verlauf.md # datiertes Log von Ereignissen, Entscheidungen, Entwürfen
 │ ├── notizen.md # freie Arbeitsnotizen
 │ └── outputs/ # Skill-Ausgaben für dieses Mandat (optionaler Unterordner)
 └── _archiv/
 └── <slug>/ # geschlossene Mandate – lesbar, aber nicht aktiv
```

Slugs sind kleingeschrieben mit Bindestrichen. Beispiele: `mueller-ki-review-2026`,
`xyz-gmbh-aia`, `vendor-openai-avv`.

## Subbefehl-Logik

### `new <slug>`

1. Bestätigen, dass der Slug nicht bereits in `mandate/<slug>/` oder `mandate/_archiv/<slug>/`
 vorhanden ist. Bei Wiederverwendung anderen Slug wählen.
2. Aufnahme-Interview starten:
 - **Mandant** (die von uns vertretene Partei oder die interne Geschäftseinheit bei In-house)
 - **Gegenseite** (die andere Seite – kann mehrere sein)
 - **Mandatstyp** (für ki-governance: KI-Anwendungsfall intern | Vendor-AI-Review | Folgenabschätzung | Regulierungsänderung | Richtlinienprojekt | Sonstiges)
 - **Vertraulichkeitsstufe** (standard | erhöht | Clean-Team – erhöht erfordert besondere
 Vorsicht in mandatsübergreifenden Einstellungen)
 - **Kernfakten** (2–5 Sätze: Worum geht es in diesem Mandat, wer sind die Stakeholder,
 was steht auf dem Spiel)
 - **Mandatsspezifische Abweichungen vom Playbook** (z. B. "Mandant verlangt 24-monatigen
 Haftungshöchstbetrag statt 12", "Gegenseite ist strategischer Partner – beziehungserhaltender
 Ton", "§ 203 StGB: besondere Schutzmechanismen erforderlich")
 - **Verbundene Mandate** (Slugs anderer zusammenhängender Mandate)
3. `mandate/<slug>/mandat.md` mit der nachstehenden Vorlage schreiben.
4. `mandate/<slug>/verlauf.md` mit einem einzigen "Eröffnet"-Eintrag initialisieren.
5. Leere `mandate/<slug>/notizen.md` anlegen.
6. **Nicht** automatisch auf das neue Mandat wechseln. Fragen: "Möchten Sie jetzt zu
 `<slug>` wechseln? (`/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>`)"

### `list`

`mandate/*/mandat.md` auflisten. Tabelle:

| Slug | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archiv/*` unter separater "Archiviert"-Überschrift,
falls vorhanden.

### `switch <slug>`

1. Bestätigen, dass `mandate/<slug>/mandat.md` existiert. Falls nicht, `/mandat-arbeitsbereich
 new <slug>` anbieten.
2. `Aktives Mandat:`-Zeile in CLAUDE.md auf `Aktives Mandat: <slug>` setzen.
3. Nutzern die mandat.md-Zusammenfassung zeigen, damit sie bestätigen können, dass sie
 beim richtigen Mandat sind.

### `close <slug>`

1. Bestätigen, dass `mandate/<slug>/` existiert.
2. "Geschlossen"-Eintrag mit heutigem Datum an `mandate/<slug>/verlauf.md` anhängen.
3. `mandate/<slug>/` → `mandate/_archiv/<slug>/` verschieben.
4. Falls das geschlossene Mandat das aktive war, `Aktives Mandat:` auf
 `keines – nur Praxiskontext` setzen.

### `none`

`Aktives Mandat:` in CLAUDE.md auf `keines – nur Praxiskontext` setzen. Mit Nutzer bestätigen.

## `mandat.md`-Vorlage

```markdown
[ARBEITSPRODUKT-HEADER – gemäß Plugin-Konfiguration; Vertraulichkeitsmarkierung beachten]

# Mandat: [Mandant] – [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]
**§ 203 StGB:** [Schweigepflicht beachtet – Schutzmechanismen: [Beschreibung]]

---

## Parteien

**Mandant:** [Name]
**Gegenseite:** [Name(n)]

## Mandatstyp

[KI-Anwendungsfall intern | Vendor-AI-Review | KI-Folgenabschätzung (FRIA/DSFA) | Regulierungsänderung | Richtlinienprojekt | Sonstiges – mit einzeiliger Begründung]

## Kernfakten

[2–5 Sätze. Worum geht es. Wer sind die Stakeholder. Was steht auf dem Spiel. Was es vom
Standard-Playbook unterscheidet.]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom praxisweiten Playbook, die nur für dieses Mandat gilt.*

- [z. B. "Haftungshöchstbetrag: Mandant verlangt 24 Monate, nicht Hausstandard 12."]
- [z. B. "Ton: beziehungserhaltend – Gegenseite ist strategischer Partner."]
- [z. B. "Rechtswahl: muss deutsches Recht sein."]
- [z. B. "§ 203 StGB: nur On-Premise-Verarbeitung, kein Drittanbieter-KI-System ohne AVV."]

## Verbundene Mandate

- [slug – ein Satz, warum verbunden]

## Vertraulichkeitshinweise

[Falls erhöht oder clean-team, erläutern warum. Wer Mandatsdateien einsehen darf. Ob
mandatsübergreifender Kontext trotz globaler Aktivierung zulässig ist.]
```

## `verlauf.md`-Initialisierung

```markdown
# Verlauf: [Mandant] – [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] – Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext über mandat.md hinaus – z. B. "Eröffnet als Reaktion auf eingehenden
Vendor-KI-Vertrag von [Gegenseite]."]
```

## Mandatsübergreifender Kontext

CLAUDE.md hat ein `Mandatsübergreifender Kontext:`-Flag. Bei `aus` (Standard) liest ein Skill
in Mandat A **niemals** Dateien in `mandate/B/`. Das ist die Vertraulichkeitsgarantie für
die Anforderungen aus § 43a Abs. 2 BRAO und § 203 StGB.

Bei `an` darf ein Skill Dateien mandatsübergreifend nur lesen, wenn der Nutzer explizit
darum bittet (z. B. "Vergleichen Sie unsere Haftungshöchstbetragsposition über die letzten
fünf Vendor-Mandate"). Auch bei `an` ist der Standard, nur das aktive Mandat zu laden.

## Quellen und Zitierweise

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

- § 43a Abs. 2 BRAO – Anwaltliche Verschwiegenheitspflicht `[Primärquelle]`
- § 203 StGB – Mandantengeheimnis bei KI-Einsatz `[Primärquelle]`
- § 53 StPO – Zeugnisverweigerungsrecht `[Primärquelle]`

## Was dieser Skill nicht tut

- **Keine Interessenkonfliktprüfung.** Konflikte liegen beim Praktiker/der Kanzlei;
 das Aufnahme-Formular erfasst, was der Nutzer angibt.
- **Keine Aufbewahrungserzwingung.** Schließen archiviert ein Mandat; es löscht nicht.
 Aufbewahrungsrichtlinie liegt außerhalb des Anwendungsbereichs.
- **Keine Ausgabenweiterleitung.** Der inhaltliche Skill entscheidet, wohin er schreibt;
 dieser Skill teilt ihm mit, welcher Ordner aktiv ist.
- **Keine Entscheidung über mandatsübergreifende Zulässigkeit.** Er liest das Flag und
 befolgt es.

## Risiken / typische Fehler

- **§ 203 StGB bei KI-Einsatz.** Wenn Mandantendaten in ein Drittanbieter-KI-System eingegeben
 werden, AVV nach Art. 28 DSGVO und Vereinbarkeit mit § 203 StGB prüfen. Im mandat.md
 dokumentieren.
- **Slug-Wiederverwendung.** Führt zu Kontext-Vermischung. Immer neu prüfen, ob Slug frei ist.
- **Schließen vs. Löschen.** Archivierte Mandate für Konflikts- und Aufbewahrungszwecke
 niemals löschen.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Anwalts
- § 203 StGB — Mandantengeheimnis
- § 50 BRAO — Handakten-Pflicht (fuenf Jahre)
- Art. 28 DSGVO — Auftragsverarbeitung bei externen Dienstleistern

## Triage zu Beginn
1. Handelt es sich um eine Kanzlei (mehrere Mandanten) oder eine In-house-Situation (ein Mandant)?
2. Ist das gesuchte Mandat bereits angelegt oder muss es neu erstellt werden?
3. Bestehen Interessenkonflikte — wurde der Konflikt-Check (§ 43a BRAO) durchgefuehrt?
4. Soll ein abgeschlossenes Mandat archiviert oder reaktiviert werden?
5. Welcher Skill soll anschliessend im Mandatskontext ausgefuehrt werden?

## Output-Template — Mandats-Workspace-Anlage
**Adressat:** Kanzlei intern — Tonfall: knapp, strukturiert
```
MANDATS-WORKSPACE
Slug: [SLUG]
Angelegt: [DATUM] — Letzte Aktivitaet: [DATUM]
Status: [AKTIV / ARCHIVIERT]

Mandant: [NAME MANDANT]
Gegenseite: [NAME GEGNER]
Mandatstyp: [IT-Recht / KI-Governance / Datenschutz / ...]
Sachgebiet: [KURZBEZEICHNUNG]

Aktenzeichen: [AKTENZEICHEN]
Zustaendige RA/RAin: [NAME]
Konflikt-Check: [DURCHGEFUEHRT AM DATUM — KEIN KONFLIKT / KONFLIKT: BESCHREIBUNG]

Kernfakten: [KURZBEZEICHNUNG 1-3 SAETZE]
Naechste Frist: [DATUM — ART DER FRIST]
Aktiver Skill: [SKILL-NAME]
```
