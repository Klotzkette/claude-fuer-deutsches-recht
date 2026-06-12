---
name: anschluss-router
description: "Einstieg, Schnelltriage und Fallrouting im KI Governance-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig: ord..."
---

# KI-Governance — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **KI Governance**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anwendungsfall-triage` | Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das Unternehmensregister — freigegeben, bedingt oder nicht freigegeben — und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene Praktiken… |
| `ki-anbieter-pruefung` | Prüft KI-Anbieterverträge gegen die unternehmenseigenen Governance- Positionen; kennzeichnet Training auf Daten, Haftung, Modelländerungen und KI-Richtlinien-Konsistenz. Unterscheidet Anbieter/Betreiber-Rolle nach Art.… |
| `ki-folgenabschaetzung` | KI-Folgenabschätzung (FRIA nach Art. 27 KI-VO + DSFA nach Art. 35 DSGVO) erstellen – strukturierte Aufnahme, Risikoanalyse, Regulierungsklassifizierung nach KI-VO und DSGVO, Richtlinien-Konsistenzprüfung und Empfehlung… |
| `ki-governance-anpassen` | Geführte Anpassung Ihres KI-Governance-Praxisprofils – eine Einstellung ändern, ohne das vollständige Kaltstart-Interview neu zu starten. Risikoeinstellung, Eskalationskontakte, Use-Case-Register-Einträge,… |
| `ki-governance-kaltstart-interview` | KI-Governance-Plugin erstmalig einrichten oder Inventar der KI-Systeme im Unternehmen erfassen und AI-Act-Anwendungsbereich prüfen. Führt Erstgespraech durch ermittelt KI-Inventar Rolle im KI-Lieferkette… |
| `ki-governance-mandat-arbeitsbereich` | Mandats-Arbeitsbereiche verwalten – neu, liste, wechseln, schließen oder keines (Praxisebene). Datei- Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen. Verwenden, wenn… |
| `ki-inventar` | KI-System-Inventar nach EU-KI-VO (VO 2024/1689) – erfasst je KI-System Rolle (Anbieter, Betreiber, Einführer, Händler, Bevollmächtigter, Produkthersteller) und Risikoklasse (verboten, hochrisiko, begrenzt, minimal,… |
| `regulierungs-luecken-analyse` | Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer… |
| `richtlinien-monitor` | Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen, Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer geplanten… |
| `richtlinien-vorlage` | Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist,… |

## Worum geht es?

Dieses Plugin unterstuetzt Unternehmen, Kanzleien und Datenschutzbeauftragte bei der Einhaltung der EU-KI-Verordnung (VO 2024/1689, in Kraft seit 01.08.2024) sowie der DSGVO im Kontext von KI-Systemen. Es deckt die gesamte KI-Governance ab: Use-Case-Triage gegen verbotene Praktiken und Hochrisiko-Kategorien, KI-Inventar mit Rollenklassifizierung, Folgenabschaetzung (FRIA nach Art. 27 KI-VO und DSFA nach Art. 35 DSGVO), Vendor-Review für KI-Anbietervertraege, Richtlinien-Monitor und Erstellung interner KI-Richtlinien.

Das Plugin ist praxisorientiert: Es arbeitet mit dem Praxisprofil des Nutzers (Risikoeinstellung, Eskalationskontakte, Use-Case-Register) und kann Mandats-Workspaces für mehrere Klienten verwalten.

## Wann brauchen Sie diese Skill?

- Ihr Unternehmen moechte ein neues KI-System einfuehren und Sie müssen prüfen, ob es unter die KI-VO faellt und welche Risikoklasse gilt.
- Sie benoetigen eine KI-Folgenabschaetzung (FRIA) nach Art. 27 KI-VO oder eine DSGVO-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO.
- Sie prüfen einen KI-Anbietervertrag auf KI-VO-Konformitaet, Haftung und Transparenzpflichten nach Art. 25 KI-VO.
- Die interne KI-Richtlinie soll gegen neue Regulierungen oder Behördenleitlinien geprueft und aktualisiert werden.
- Sie wollen ein vollstaendiges KI-Inventar aller im Unternehmen eingesetzten Systeme nach Art. 3 KI-VO aufbauen.

## Fachbegriffe (kurz erklaert)

- **Anbieter** — Wer ein KI-System entwickelt oder entwickeln lässt und es in Verkehr bringt oder in Betrieb nimmt (Art. 3 Nr. 3 KI-VO).
- **Betreiber** — Wer ein KI-System im eigenen Namen und unter eigener Kontrolle einsetzt (Art. 3 Nr. 4 KI-VO).
- **Hochrisiko-KI** — KI-Systeme nach Anhang III KI-VO (z.B. biometrische Identifikation, Beschäftigung, kritische Infrastruktur); erfordern umfassende Compliance-Pflichten.
- **FRIA** — Fundamental Rights Impact Assessment nach Art. 27 KI-VO: Folgenabschaetzung für Grundrechte bei Hochrisiko-KI durch Betreiber.
- **DSFA** — Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO; erforderlich bei hohem Risiko für Betroffene durch Datenverarbeitung.
- **Allzweck-KI (GPAI)** — General Purpose AI Model; gesonderte Pflichten nach Art. 51 ff. KI-VO für Modelle mit systemischen Risiken.
- **Verbotene Praktiken** — KI-Anwendungen, die nach Art. 5 KI-VO generell verboten sind (z.B. Sozial-Scoring, manipulative Techniken).

## Rechtsgrundlagen

- VO (EU) 2024/1689 (EU-KI-VO) — Gesamtrahmen, Risikoklassen, Verbote, Pflichten
- Art. 5 KI-VO — Verbotene KI-Praktiken
- Anhang III KI-VO — Hochrisiko-KI-Systeme
- Art. 25 KI-VO — Pflichten der Betreiber
- Art. 27 KI-VO — Folgenabschaetzung Grundrechte (FRIA)
- Art. 51-55 KI-VO — Allzweck-KI-Modelle (GPAI) mit systemischen Risiken
- Art. 35 DSGVO — Datenschutz-Folgenabschaetzung (DSFA)
- Art. 13-14 DSGVO — Transparenzpflichten bei automatisierten Entscheidungen

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Unternehmen als Anbieter oder Betreiber, Branche, Groesse, welche KI-Systeme bereits im Einsatz oder geplant.
2. Phase des Mandats bestimmen: Ersteinrichtung (Inventar, Profil), Triage neues KI-System, Folgenabschaetzung, Richtlinien-Erstellung oder Monitoring.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen prüfen: KI-VO-Verbote seit 02.02.2025 anwendbar; Hochrisiko-Pflichten seit 02.08.2026; GPAI-Pflichten seit 02.08.2025.
5. Anschluss-Skill bestimmen: nach Triage folgt Folgenabschaetzung oder Richtlinien-Monitor; nach Vendor-Review ggf. Vertragsnachverhandlung.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `ki-governance-kaltstart-interview` — Ersteinrichtung: KI-Inventar, Rolle in KI-Lieferkette, regulatorischen Anwendungsbereich erfassen.
- `ki-governance-anpassen` — Praxisprofil aktualisieren: Risikoeinstellung, Eskalationskontakte, Module und Workspace-Pfade.
- `ki-governance-mandat-arbeitsbereich` — Mandats-Workspaces verwalten für Mehrfachmandatsbetrieb.

**KI-Inventar und Klassifizierung**

- `ki-inventar` — KI-System-Inventar nach EU-KI-VO: Rolle und Risikoklasse je System erfassen und bewerten.
- `anwendungsfall-triage` — Use-Case gegen Unternehmensregister klassifizieren: freigegeben, bedingt, nicht freigegeben.

**Folgenabschaetzung**

- `ki-folgenabschaetzung` — FRIA nach Art. 27 KI-VO und DSFA nach Art. 35 DSGVO erstellen.

**Vendor und Richtlinien**

- `ki-anbieter-pruefung` — KI-Anbietervertraege auf Governance-Positionen, Training auf Daten, Haftung und Art. 25 KI-VO prüfen.
- `richtlinien-vorlage` — Interne KI-Nutzungsrichtlinie entwerfen auf Basis öffentlicher Muster und Praxisprofil.
- `richtlinien-monitor` — Interne KI-Richtlinie auf Abweichungen von der Praxis und neuen Regulierungen prüfen.
- `regulierungs-luecken-analyse` — Neue KI-Regulierung oder Behördenleitlinie gegen aktuelle Governance-Position abgleichen.

## Worauf besonders achten

- **Anbieter- und Betreiber-Rolle exakt abgrenzen.** Beide Rollen haben unterschiedliche Pflichten nach KI-VO; eine Verwechslung fuehrt zu falschen Compliance-Maßnahmen.
- **Zeitplan der KI-VO beachten.** Verbote (Art. 5) seit 02.02.2025, GPAI seit 02.08.2025, Hochrisiko seit 02.08.2026; nicht alle Pflichten gelten gleichzeitig.
- **DSFA und FRIA sind keine Duplikate.** Beide Instrumente haben eigene Anwendungsbereiche und können parallel erforderlich sein; Skill `ki-folgenabschaetzung` kombiniert beide.
- **Interne Richtlinie muss gelebte Praxis abbilden.** Eine Richtlinie, die niemand einhalt, schuetzt nicht vor regulatorischer Verantwortung; Skill `richtlinien-monitor` prüft Konsistenz.
- **Allzweck-KI-Modelle erfordern Sonderbehandlung.** Bei Einsatz von GPAI-Modellen mit systemischen Risiken gelten Transparenz- und Sorgfaltspflichten nach Art. 53 ff. KI-VO.

## Typische Fehler

- Unternehmen klassifiziert sich als Anbieter obwohl es nur Betreiber ist; fuehrt zu ueberzogenen Compliance-Maßnahmen.
- Use-Case-Triage wird nur einmal durchgefuehrt; bei Weiterentwicklung des KI-Systems ist eine erneute Prüfung erforderlich.
- Folgenabschaetzung wird nach Einfuehrung des Systems erstellt; KI-VO erfordert Vorab-Bewertung.
- KI-Anbietervertrag wird ohne Prüfung der Art. 25 KI-VO-Pflichten akzeptiert; Vertragslücken bei Modellwechsel oder Datenpanne.
- Richtlinie wird erstellt und dann nicht aktualisiert; neue Regulierung und neue Systeme bleiben unberuecksichtigt.

## Quellen und Aktualitaet

- Stand: 05/2026
- VO (EU) 2024/1689 (KI-VO) in geltender Fassung; schrittweise Anwendbarkeit beachten
- VO (EU) 2016/679 (DSGVO) in geltender Fassung

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 35 DSGVO
- § 203 StGB
- Art. 22 DSGVO
- Art. 28 DSGVO
- § 87 BetrVG
- § 26 BDSG
- § 44b UrhG
- Art. 36 DSGVO
- Art. 9 DSGVO
- Art. 79 DSGVO
- Art. 32 DSGVO
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)
