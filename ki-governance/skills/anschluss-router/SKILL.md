---
name: anschluss-router
description: "Für digitale Werkzeuge-Governance — Allgemein: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# KI-Governance — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Verordnung (EU) 2024/1689 in der Fassung 2026/1744: Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5 für Anhang III ab 02.12.2027, für Anhang I ab 02.08.2028. Artikel 4 neuer Fassung, Artikel 4a, Verbote und Transparenz gesondert prüfen; Vorfallfrist nach Tatbestand und Ereignis, Datenschutz-Folgenabschätzung vor riskanter Verarbeitung.
- Tragende Rechtsgrundlagen am amtlichen EUR-Lex-Text der KI-Verordnung und der gegebenenfalls einschlägigen DSGVO prüfen. ISO/IEC 42001, NIST AI RMF und OECD-Prinzipien sind keine Verordnungsartikel. Bei harmonisierten Normen konkrete Fassung, Amtsblattfundstelle und abgedeckte Anforderungen nach Artikel 40 feststellen; freiwilliges Managementzertifikat und Konformitätsverfahren nach Artikel 43 trennen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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
- **Primärer Pfad:** Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Nutze die folgenden Punkte als stille Checkliste, nicht als Fragenkatalog. Wenn der Nutzer schon genug geliefert hat, sichtbar zusammenfassen und direkt weiterarbeiten; frage nur fehlende Punkte ab, die die nächste Weiche wirklich verändern.

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
4. **Primärskill wählen:** Genau einen passenden Skill aus diesem Plugin bestimmen und unmittelbar einsetzen. Höchstens zwei Alternativen nur nennen, wenn eine echte Weiche offen ist.
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

### 5. Fachmodule gezielt und sparsam laden

1. Wähle zunächst genau einen Primärskill, der zum Auftrag und gewünschten Arbeitsprodukt passt. Weitere Skills kommen nur bei einer konkreten Schnittstelle hinzu.
2. Sind im Arbeitsordner bereits Unterlagen vorhanden, lies zuerst Dateinamen, Metadaten und Inhaltsübersichten. Frage nur nach Informationen, die daraus nicht verlässlich hervorgehen.
3. Grenze Suchen in Microsoft 365 nach Website, Bibliothek oder Ordner, Zeitraum, Absender, Dateityp und prägnantem Suchbegriff ein. Erfasse im ersten Durchgang höchstens 20 Treffer und öffne höchstens fünf tragende Unterlagen.
4. Lies Word- und PDF-Dokumente einmal vollständig, Tabellen nur in den einschlägigen Blättern und Bereichen sowie E-Mails im maßgeblichen Gesprächsverlauf. Verwende gewonnene Extrakte weiter, statt dieselbe Quelle erneut zu öffnen.
5. Die [vollständige Fachmodulkarte](references/fachmodule.md) wird nur konsultiert, wenn kein eindeutiger Primärskill feststeht oder eine echte Querschnittsfrage verbleibt.

## Worum geht es?

Dieses Plugin unterstuetzt Unternehmen, Kanzleien und Datenschutzbeauftragte bei der Einhaltung der EU-KI-Verordnung (VO 2024/1689, in Kraft seit 01.08.2024) sowie der DSGVO im Kontext von KI-Systemen. Es deckt die gesamte KI-Governance ab: Use-Case-Triage gegen verbotene Praktiken und Hochrisiko-Kategorien, KI-Inventar mit Rollenklassifizierung, Folgenabschaetzung (FRIA nach Art. 27 KI-VO und DSFA nach Art. 35 DSGVO), Vendor-Review für KI-Anbietervertraege, Richtlinien-Monitor und Erstellung interner KI-Richtlinien.

Das Plugin ist praxisorientiert: Es arbeitet mit dem Praxisprofil des Nutzers (Risikoeinstellung, Eskalationskontakte, Use-Case-Register) und kann Mandats-Workspaces für mehrere Klienten verwalten.

## Wann brauchen Sie diese Skill?

- Ihr Unternehmen moechte ein neues KI-System einfuehren und Sie müssen prüfen, ob es unter die KI-VO faellt und welche Risikoklasse gilt.
- Sie benoetigen eine KI-Folgenabschaetzung (FRIA) nach Art. 27 KI-VO oder eine DSGVO-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO.
- Sie prüfen einen KI-Anbietervertrag auf konkrete Lieferkettenpflichten nach Artikel 25, Haftungszusagen und gegebenenfalls Transparenz nach Artikel 13 beziehungsweise 50. Rollen und gesetzliche Pflicht nicht mit frei verhandelter Klausel vermischen.
- Die interne KI-Richtlinie soll gegen neue Regulierungen oder Behördenleitlinien geprueft und aktualisiert werden.
- Sie wollen ein vollstaendiges KI-Inventar aller im Unternehmen eingesetzten Systeme nach Art. 3 KI-VO aufbauen.

## Fachbegriffe (kurz erklaert)

- **Anbieter:** Artikel 3 Nummer 3 verlangt Entwicklung oder Entwicklung im Auftrag und das dort bezeichnete Inverkehrbringen beziehungsweise Inbetriebnehmen unter eigenem Namen oder Handelsmarke; unentgeltliches Angebot kann erfasst sein. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Betreiber:** Artikel 3 Nummer 4 betrifft die Verwendung unter eigener Verantwortung; ausschließlich persönliche nicht berufliche Verwendung ist ausgenommen. Kein allgemeines Eigenmarkenerfordernis für die Betreiberrolle. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Hochrisiko-KI:** Beide Pfade des Artikels 6 prüfen; im Anhang-III-Pfad Absatz 3 mit Risiko, Fallgruppen und Profiling-Sperre untersuchen. Artikel 6 Absatz 1 mit Anhang I einschließlich Abschnitt A/B und Artikel 2 Absatz 2 von Absatz 2 mit Anhang III trennen. Artikel 6 Absätze 1a bis 1c samt Berichtigung prüfen. Eine sicherheitsrelevante Maschinenfunktion ist nicht allein deshalb ein Anhang-III-Tatbestand. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Grundrechte-Folgenabschätzung:** Artikel 27 erfasst Betreiber, die Einrichtungen des öffentlichen Rechts oder private Einrichtungen sind, die öffentliche Dienstleistungen erbringen, sowie Betreiber der Systeme nach Anhang III Nummer 5 Buchstaben b und c. Systeme nach Anhang III Nummer 2 sind ausgenommen. Öffentliche Finanzierung allein ist kein Tatbestand. DSFA und FRIA haben eigene Voraussetzungen; vorhandene DSFA-Ergebnisse können nach Artikel 27 Absatz 4 einbezogen werden. Artikel 113 Buchstabe c erfasst Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: bei Anhang III ab 02.12.2027, bei Anhang I ab 02.08.2028. Artikel 111 und die Zeitverschränkung mit anderen Abschnitten gesondert prüfen; keine pauschale Verschiebung sämtlicher Pflichten. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **DSFA** — Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO; erforderlich bei hohem Risiko für Betroffene durch Datenverarbeitung.
- **GPAI:** Modellbegriff und Anbieterpflichten nach Artikel 53 prüfen; zusätzliche Systemrisikopflichten nach Artikel 55 setzen die einschlägige Einstufung voraus. Die Nutzung eines fremden Modells macht den Nutzer nicht automatisch zum Modellanbieter. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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
- **Zeitliche Einordnung:** Bestehende Verbote nach Artikel 5 gelten seit 02.02.2025; die neuen Regelungen in Absatz 1 Buchstaben ba und bb sowie Absätzen 1a und 1b gelten ab 02.12.2026. Zulässigkeit nach jedem konkreten Tatbestand und seiner Ausnahme prüfen. Artikel 113 Buchstabe c erfasst Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: bei Anhang III ab 02.12.2027, bei Anhang I ab 02.08.2028. Artikel 111 und die Zeitverschränkung mit anderen Abschnitten gesondert prüfen; keine pauschale Verschiebung sämtlicher Pflichten. GPAI-Altmodelle nach Artikel 111 Absatz 3 gesondert prüfen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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
- **Zeitliche Einordnung:** Bestehende Verbote nach Artikel 5 gelten seit 02.02.2025; die neuen Regelungen in Absatz 1 Buchstaben ba und bb sowie Absätzen 1a und 1b gelten ab 02.12.2026. Zulässigkeit nach jedem konkreten Tatbestand und seiner Ausnahme prüfen. Artikel 113 Buchstabe c erfasst Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: bei Anhang III ab 02.12.2027, bei Anhang I ab 02.08.2028. Artikel 111 und die Zeitverschränkung mit anderen Abschnitten gesondert prüfen; keine pauschale Verschiebung sämtlicher Pflichten. GPAI-Altmodelle nach Artikel 111 Absatz 3 gesondert prüfen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **DSFA und FRIA sind keine Duplikate.** Beide Instrumente haben eigene Anwendungsbereiche und können parallel erforderlich sein; Skill `ki-folgenabschaetzung` kombiniert beide.
- **Interne Richtlinie muss gelebte Praxis abbilden.** Eine Richtlinie, die niemand einhalt, schuetzt nicht vor regulatorischer Verantwortung; Skill `richtlinien-monitor` prüft Konsistenz.
- **GPAI-Modelle gesondert prüfen:** Anbieterpflichten nach Artikel 53 von zusätzlichen Pflichten nach Artikel 55 unterscheiden. Betreiber eines darauf aufbauenden Systems übernehmen diese nicht automatisch; eigenen Rollenwechsel oder Anbieterstatus gesondert begründen. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)

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
