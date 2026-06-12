---
name: kaltstart-triage
description: "Einstieg, Schnelltriage und Fallrouting im Wandeldarlehen Lebenszyklus-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eig..."
---

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Wandeldarlehen Lebenszyklus** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Wandeldarlehen Lebenszyklus**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket.

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
| `beurkundungserfordernis-pruefung` | Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist. §§ 15 55 GmbHG § 311b BGB Formvorschriften. Prüfraster: Sacheinlage Kapitalerhohung GmbH-Anteil… |
| `bilinguale-vertragserstellung` | Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investoren. BGB Darlehen §§ 488 ff. BGB GmbHG Kapitalerhohung. Prüfraster: Terminologie-Konsistenz… |
| `cap-table-update-pre-post` | Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money… |
| `darlehenshoehe-konditionen` | Darlehenshoehe Zinsen Laufzeit und Konditionen für Wandeldarlehen verhandeln und dokumentieren. §§ 488 491 BGB Darlehensvertrag §§ 246 247 BGB Zinsen. Prüfraster: Darlehenshoehe Zinssatz Disagio Laufzeit Fälligkeit… |
| `dokumenten-upload-extraktion` | Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger… |
| `einsprachige-vertragsfassung-de` | Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität… |
| `formfehler-heilungs-timeline` | Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b BGB Nichtigkeit §§ 15 55 GmbHG Formerfordernisse. Prüfraster: Formmangel Nichtigkeit Heilung… |
| `gesellschafterbeschluss-kapitalerhoehung` | Gesellschafterbeschluss für Kapitalerhohung nach Wandlung vorbereiten. §§ 53 55 56 GmbHG Kapitalerhohung. Prüfraster: Beschlussinhalt Mehrheitserfordernisse notarielle Form neues Stammkapital Einlagepflicht… |
| `gesellschafterbeschluss-vorbereiten` | Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbeschluesse. Prüfraster: Beschlussgegenstand Mehrheiten Ladungspflicht Form Anlagen. Output:… |
| `gesellschafterliste-aktualisieren` | Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Prüfraster: neue Gesellschafter Anteile… |
| `gesellschafterversammlung-einberufen` | Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflichten. Prüfraster: Ladungsfrist Form Tagesordnung Quorum Vollmachten Protokollpflicht. Output:… |
| `handelsregisteranmeldung-kapitalerhoehung` | Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapitalerhohung. Prüfraster: Anmeldungsinhalt Unterlagen Notar Einreichungspflicht… |
| `kyc-aml-geldwaesche` | KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft… |
| `mandat-triage-wandeldarlehen` | Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output:… |
| `mehrere-wandeldarlehen-parallel` | Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren und Konflikte erkennen. §§ 488 ff. BGB § 39 InsO Rangrücktritt. Prüfraster: Pari-passu-Stellung Rangregelungen Wandlungsrechte… |
| `notar-paket-uebermittlung` | Notarpaket für Beurkundungstermin bei Kapitalerhohung durch Wandlung zusammenstellen und uebermitteln. §§ 15 55 GmbHG BeurkG. Prüfraster: Vollständigkeit Beschluss Zeichnungsschein Gesellschafterliste Vollmachten… |
| `parteien-erfassen` | Vertragsparteien eines Wandeldarlehens vollständig identifizieren und dokumentieren. §§ 13 17 GmbHG Gesellschafter §§ 305 ff. BGB AGB bei mehreren Darlehensgebern. Prüfraster: Darlehensgeberin Darlehensnehmerin… |
| `post-eintragung-checkliste` | Nacharbeiten nach Handelsregistereintragung der Kapitalerhohung abschließen. §§ 57 40 GmbHG §§ 39 16 GmbHG Legitimationswirkung. Prüfraster: Eintragsbekanntmachung Gesellschafterliste Anteilsurkunden… |
| `rangruecktritt-formulieren` | Rangrücktrittserklärung für Wandeldarlehen formulieren um insolvenzrechtliche Nachrang­wirkung herzustellen. § 39 InsO qualifizierter Rangrücktritt. Prüfraster: Formulierungsanforderungen BGH-Anforderungen… |
| `sacheinlagebericht-werthaltigkeit` | Sacheinlagebericht für Sachkapitalerhohung durch Wandeldarlehen erstellen und Werthaltigkeit prufen. § 56 GmbHG Sacheinlage §§ 19 8 GmbHG Einlageverpflichtung. Prüfraster: Sacheinlagegegenstand Bewertung Werthaltigkeit… |
| `textform-vs-schriftform-vs-notariell` | Formerfordernis für einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen. §§ 126 126a 126b BGB Schriftform Textform elektronische Form. Prüfraster: Vertragstyp Erklärung Beschluss gesetzliches Formerfordernis… |
| `unterzeichnung-elektronisch-docusign` | Elektronische Unterzeichnung von Wandeldarlehensvertraegen und Begleitdokumenten organisieren. §§ 126a 126b BGB eIDAS-VO qualifizierte elektronische Signatur. Prüfraster: Formerfordernis je Dokument einfache QES oder… |
| `vertraulichkeit-und-sprachklausel` | Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag prüfen oder formulieren. §§ 307 ff. BGB AGB-Recht § 5 BDSG Datengeheimnis. Prüfraster: Geheimhaltungsumfang Ausnahmen Vertragssprache Kollisionsregel… |
| `wandelereignis-eingang` | Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen wenn Investor Wandlung ankündigt. §§ 488 ff. BGB Darlehensvertrag §§ 53 55 GmbHG. Prüfraster: Trigger-Typ Frist Preisbestimmung Erklärung… |
| `wandelereignis-trigger-dispatcher` | Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten wenn Wandelereignis vorliegt. §§ 488 ff. BGB GmbHG SAFE-Terminologie. Prüfraster: Trigger-Typ Qualified Financing Maturity Liquidation Exit… |
| `wandlung-kommunikation-paketverteilung` | Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung organisieren. §§ 130 132 BGB Zugang §§ 15 55 GmbHG. Prüfraster: Empfaengerliste Dokumente Zugang Fristen Bestätigung. Output:… |
| `wandlungsausschluss-pruefung` | Prüfen ob Wandlung gesperrt oder ausgeschlossen ist bei vertraglichen oder gesetzlichen Hindernissen. §§ 134 138 BGB Nichtigkeit § 30 GmbHG Kapitalerhaltung. Prüfraster: Ausschlusstatbestaende Insolvenzreife… |
| `wandlungsmechanik-konzipieren` | Wandlungsmechanik eines SAFE oder Convertible Note konzipieren: Preis Verwasserungsschutz Sonderrechte. SAFE Y-Combinator-Terminologie §§ 53 55 GmbHG §§ 488 ff. BGB. Prüfraster: Wandlungspreis Bewertungsdeckel Rabatt… |
| `wandlungspreis-berechnung` | Wandlungspreis auf Basis vertraglich vereinbarter Parameter berechnen wenn Wandlung ausgelöst wird. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Bewertungsdeckel Rabatt Qualified-Financing-Preis MFN… |
| `wandlungspruefung-trigger-liquidation` | Wandlung bei Liquidationsereignis Auflösung oder Exit prüfen. §§ 60 ff. GmbHG Auflösungsgründe § 179a AktG. Prüfraster: Liquidationstatbestand Liquidationspraeference Verwasserungsschutz Rangordnung… |
| `wandlungspruefung-trigger-maturity` | Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen wenn kein qualifiziertes Finanzierungsereignis eingetreten ist. §§ 488 ff. BGB Fälligkeit. Prüfraster: Laufzeitenddatum Wandlungsrecht Wandlungspflicht… |
| `wandlungspruefung-trigger-qualified-financing` | Wandlung bei qualifizierter Finanzierungsrunde prüfen wenn neue Investitionsrunde als Trigger definiert ist. SAFE §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Qualified-Financing-Definition Mindestbetrag Lead-Investor… |

## Worum geht es?

Das Plugin begleitet den vollstaendigen Lebenszyklus eines Wandeldarlehens (Convertible Note oder SAFE) für GmbH und UG: von der Ersterfassung der Parteien und der Konditionenverhandlung über die Vertragserstellung (bilingual oder einsprachig) und Beurkundungspruefung bis hin zur Wandlungsberechnung, dem Cap-Table-Update und der notar- und handelsregistergerechten Dokumentation der Kapitalerhoehung.

Zielgruppe sind Anwaelte und Steuerberater im Startup- und Venture-Capital-Bereich sowie Inhouse-Juristen, die Wandeldarlehen als Finanzierungsinstrument einsetzen. Das Plugin begleitet sowohl die Darlehensgeber- als auch die Gesellschaftsseite.

## Wann brauchen Sie diese Skill?

- Startup-GmbH und Investor verhandeln ein Wandeldarlehen oder SAFE; Vertrag muss von Grund auf erstellt werden.
- Bestehendes Wandeldarlehen lauft ab oder ein Wandelereignis (qualifizierte Finanzierungsrunde, Exit) tritt ein.
- Mehrere Wandeldarlehen von verschiedenen Investoren müssen parallel koordiniert und auf Kollisionspunkte geprueft werden.
- Kapitalerhoehung durch Wandlung erfordert Notartermin, Gesellschafterbeschluss und Handelsregisteranmeldung.
- Formfehler in Wandeldarlehen- oder Kapitalerhoehungs-Dokumenten müssen identifiziert und geheilt werden.

## Fachbegriffe (kurz erklaert)

- **Wandeldarlehen** — Darlehen nach §§ 488 ff. BGB, das unter bestimmten Bedingungen (Trigger) in Gesellschaftsanteile umgewandelt wird.
- **SAFE** — Simple Agreement for Future Equity; Y-Combinator-Vorlage; kein Darlehen im Rechtssinne, sondern Vereinbarung auf zukuenftige Kapitalbeteiligung.
- **Wandlungspreis** — Preis je neu ausgegebenen Geschäftsanteil; ergibt sich aus Bewertungs-Cap, Discount oder Finanzierungsrunde.
- **Cap-Table** — Gesellschafterliste inkl. aller voll verwasserten Anteile (fully diluted); zeigt Beteiligungsstruktur vor und nach Wandlung.
- **Qualified Financing** — Qualifiziertes Finanzierungsereignis; haeufigster Wandlungs-Trigger; meist definiert als neue Finanzierungsrunde ab einer Mindestbetrag-Schwelle.
- **Rangrücktritt** — Nachrangabrede nach § 39 InsO; stellt Wandeldarlehen insolvenzrechtlich nachrangig, um Ueberschuldungsausweis zu verhindern.
- **Beurkundungserfordernis** — Kapitalerhoehungen bei GmbH beduerften notarieller Beurkundung nach § 55 GmbHG; Formmangel fuehrt zu Nichtigkeit.
- **SAFE-Y-Combinator** — US-Standardvorlage für Seed-Investitionen; in Deutschland-Transaktionen oft angepasst oder ersetzt.

## Rechtsgrundlagen

- §§ 488 491 BGB — Darlehensrecht
- §§ 53 55 56 57 GmbHG — Satzungsaenderung, Kapitalerhoehung, Sacheinlage, Anmeldung
- § 40 GmbHG — Gesellschafterliste; Anmeldepflicht nach Änderung
- § 15 GmbHG — Abtretung von Geschäftsanteilen (Formpflicht)
- § 39 InsO — Nachrang; Rangruecktrittserklaerung
- §§ 125 126 BGB — Form; Schriftform
- GwG §§ 10 11 — KYC/AML-Pflichten bei Investoren
- eIDAS-VO (EU) 910/2014 — Elektronische Signatur

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Neue Vertragserstellung oder laufendes Mandat mit Wandelereignis?
2. Parteien und Konditionen erfassen: Darlehenshoehe, Zinssatz, Laufzeit, Wandlungspreis-Mechanik.
3. Beurkundungserfordernis prüfen: Liegt ein Formerfordernis vor? Notartermin erforderlich?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Nach Wandlung: Cap-Table aktualisieren, Gesellschafterliste einreichen, Handelsregister anmelden.

## Skill-Tour (was gibt es hier?)

- `mandat-triage-wandeldarlehen` — Wandeldarlehensmandat einordnen, Verfahrensroute bestimmen und erste Prioritaeten setzen.
- `parteien-erfassen` — Vertragsparteien vollstaendig identifizieren und dokumentieren; KYC-Vorab-Check.
- `darlehenshoehe-konditionen` — Darlehenshoehe, Zinsen, Laufzeit und Konditionen verhandeln und dokumentieren.
- `einsprachige-vertragsfassung-de` — Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten.
- `bilinguale-vertragserstellung` — Wandeldarlehensvertrag zweisprachig deutsch/englisch für internationale Transaktionen erstellen.
- `textform-vs-schriftform-vs-notariell` — Formerfordernis für einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen.
- `beurkundungserfordernis-pruefung` — Beurkundungserfordernis prüfen; ob Notartermin erforderlich ist klären.
- `vertraulichkeit-und-sprachklausel` — Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag prüfen oder formulieren.
- `unterzeichnung-elektronisch-docusign` — Elektronische Unterzeichnung organisieren; eIDAS-Konformitaet prüfen.
- `kyc-aml-geldwaesche` — KYC- und AML-Anforderungen bei Investor-Onboarding prüfen.
- `rangruecktritt-formulieren` — Rangruecktrittserklaerung für insolvenzrechtlichen Nachrang formulieren.
- `wandlungsmechanik-konzipieren` — Wandlungsmechanik konzipieren: Preis, Verwasserungsschutz, Sonderrechte.
- `wandlungspreis-berechnung` — Wandlungspreis auf Basis der vertraglich vereinbarten Parameter berechnen.
- `wandelereignis-trigger-dispatcher` — Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten.
- `wandelereignis-eingang` — Eingehende Wandelereignis-Notification prüfen und naechste Schritte bestimmen.
- `wandlungspruefung-trigger-qualified-financing` — Wandlung bei qualifizierter Finanzierungsrunde als Trigger prüfen.
- `wandlungspruefung-trigger-maturity` — Wandlung bei Laufzeitablauf des Wandeldarlehens prüfen.
- `wandlungspruefung-trigger-liquidation` — Wandlung bei Liquidationsereignis oder Exit prüfen.
- `wandlungsausschluss-pruefung` — Prüfen, ob Wandlung gesperrt oder ausgeschlossen ist.
- `mehrere-wandeldarlehen-parallel` — Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren; Konflikte erkennen.
- `cap-table-update-pre-post` — Cap-Table vor und nach Wandlung aktualisieren; Verwasserungseffekte berechnen.
- `gesellschafterbeschluss-vorbereiten` — Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten.
- `gesellschafterbeschluss-kapitalerhoehung` — Gesellschafterbeschluss für Kapitalerhoehung nach Wandlung vorbereiten.
- `gesellschafterversammlung-einberufen` — Gesellschafterversammlung einberufen und Tagesordnung aufstellen.
- `sacheinlagebericht-werthaltigkeit` — Sacheinlagebericht erstellen und Werthaltigkeit prüfen.
- `notar-paket-uebermittlung` — Notarpaket für Beurkundungstermin zusammenstellen und uebermitteln.
- `handelsregisteranmeldung-kapitalerhoehung` — Handelsregisteranmeldung nach Kapitalerhoehung durch Wandlung vorbereiten.
- `gesellschafterliste-aktualisieren` — Gesellschafterliste nach Kapitalerhoehung aktualisieren und einreichen.
- `post-eintragung-checkliste` — Nacharbeiten nach Handelsregistereintragung abschliessen.
- `wandlung-kommunikation-paketverteilung` — Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung.
- `formfehler-heilungs-timeline` — Formfehler in Wandeldarlehen- oder Kapitalerhoehungs-Dokumenten identifizieren und Heilungsmassnahmen planen.
- `dokumenten-upload-extraktion` — Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren.

## Worauf besonders achten

- Beurkundungserfordernis nach § 55 GmbHG ist zwingend für Kapitalerhoehungen; formlose Wandlung fuehrt zur Nichtigkeit des Kapitalerhoehungsbeschlusses.
- Verwasserungsschutzklauseln (Anti-Dilution) müssen praesize formuliert sein; Broad-Based vs. Narrow-Based-Methode kann erhebliche Unterschiede im Wandlungspreis bewirken.
- Rangrücktritt muss vor Wandlung vorliegen, wenn Ueberschuldung droht; ex-post-Rangrücktritt schuetzt nicht rueckwirkend.
- KYC/AML-Pflichten des GwG gelten ab bestimmten Beteiligungsschwellen; fehlende Prüfung des Investors kann Haftung ausloesen.
- Mehrere parallel laufende Wandeldarlehen können Kollisionspunkte bei Triggern und Cap-Berechnung haben; Konsistenzpruefung ist unverzichtbar.

## Typische Fehler

- Wandlungspreis-Formel zu unpraezise: Fehlende Definition von Ausgangsgroessen (pre-money valuation, fully diluted cap) fuehrt zu Streit bei Wandlung.
- Notartermin zu spaet eingeplant: Notariatliche Termine bei DNOTA und Notaren brauchen Vorlaufzeit; Last-Minute-Beurkundung ist haeufig nicht möglich.
- Gesellschafterliste nicht aktualisiert: Nach Wandlung und Eintragung muss Gesellschafterliste innerhalb eines Monats eingereicht werden (§ 40 GmbHG).
- Sacheinlagebericht fehlt: Bei Sachkapitalerhoehung durch Wandlung ist Sacheinlagebericht Pflicht (§ 56 GmbHG); fehlender Bericht blockiert Eintragung.
- SAFE als Darlehen klassifiziert: Falsches Bilanzierungsurteil für SAFE (kein Darlehen, sondern Eigenkapital-Instrument unter US-GAAP; unter HGB haeufig als Verbindlichkeit zu bilanzieren) kann steuerliche Folgen haben.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB, GmbHG, InsO, GwG, eIDAS-VO in aktuell geltender Fassung
- SAFE-Vorlage des Y-Combinators (Post-Money SAFE, aktuelle Version 2018)
