# Megaprompt: wandeldarlehen-lebenszyklus

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 50 Skills des Plugins `wandeldarlehen-lebenszyklus`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Wandeldarlehen-Lebenszyklus: ordnet Rolle (Investor, Startup, Geschäftsführung), markie…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Wandeldarlehen Lebenszyklus-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, R…
3. **mandat-triage-mehrere-parallel** — Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. …
4. **begleitet-erstpruefung-und-mandatsziel** — Begleitet: Erstprüfung, Rollenklärung und Mandatsziel.
5. **beurkundungserfordernis-pruefung** — Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist…
6. **bilinguale-vertragserstellung** — Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investore…
7. **cap-table-darlehenshoehe-konditionen** — Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 G…
8. **dokumenten-upload-formfehler-heilungs** — Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardt…
9. **einsprachige-vertragsfassung** — Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehe…
10. **formfehler-heilungs-timeline** — Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b B…
11. **gesellschafterbeschluss-vorbereiten** — Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbes…
12. **gesellschafterliste-aktualisieren** — Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Ge…
13. **gesellschafterversammlung-einberufen** — Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflich…
14. **handelsregisteranmeldung-kapitalerhoehung-kyc** — Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapit…
15. **kyc-aml-geldwaesche** — KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG S…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Wandeldarlehen-Lebenszyklus: ordnet Rolle (Investor, Startup, Geschäftsführung), markiert Frist (Wandlungsoption), wählt Norm (BGB §§ 488 ff. Darlehen, GmbHG/AktG, EStG) und Zuständigkeit (Handelsregister), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Wandeldarlehen Lebenszyklus** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `begleitet-erstpruefung-und-mandatsziel` — Begleitet Erstpruefung und Mandatsziel
- `beurkundungserfordernis-pruefung` — Beurkundungserfordernis Pruefung
- `beurkundungspruefung-quellenkarte-check` — Beurkundungspruefung Quellenkarte Check
- `bilingual-einsprachig` — Bilingual Einsprachig
- `bilinguale-vertragserstellung` — Bilinguale Vertragserstellung
- `cap-table-darlehenshoehe-konditionen` — CAP Table Darlehenshoehe Konditionen
- `chronologie-fristen` — Chronologie Fristen
- `darlehenshoehe-konditionen` — Darlehenshoehe Konditionen
- `dokumenten-upload-formfehler-heilungs` — Dokumenten Upload Formfehler Heilungs
- `einsprachig-verhandlung-vergleich-und-eskalation` — Einsprachig Verhandlung Vergleich und Eskalation
- `einsprachige-vertragsfassung` — Einsprachige Vertragsfassung
- `formfehler-heilungs-timeline` — Formfehler Heilungs Timeline
- `gesellschafterbeschluss-kapitalerhoehung` — Gesellschafterbeschluss Kapitalerhoehung
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Wandeldarlehen Lebenszyklus sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Wandeldarlehen Lebenszyklus-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eig..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Wandeldarlehen Lebenszyklus** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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

Das Plugin begleitet den vollstaendigen Lebenszyklus eines Wandeldarlehens (Convertible Note oder SAFE) für GmbH und UG: von der Ersterfassung der Parteien und der Konditionenverhandlung ueber die Vertragserstellung (bilingual oder einsprachig) und Beurkundungspruefung bis hin zur Wandlungsberechnung, dem Cap-Table-Update und der notar- und handelsregistergerechten Dokumentation der Kapitalerhoehung.

Zielgruppe sind Anwaelte und Steuerberater im Startup- und Venture-Capital-Bereich sowie Inhouse-Juristen, die Wandeldarlehen als Finanzierungsinstrument einsetzen. Das Plugin begleitet sowohl die Darlehensgeber- als auch die Gesellschaftsseite.

## Wann brauchen Sie diese Skill?

- Startup-GmbH und Investor verhandeln ein Wandeldarlehen oder SAFE; Vertrag muss von Grund auf erstellt werden.
- Bestehendes Wandeldarlehen lauft ab oder ein Wandelereignis (qualifizierte Finanzierungsrunde, Exit) tritt ein.
- Mehrere Wandeldarlehen von verschiedenen Investoren muessen parallel koordiniert und auf Kollisionspunkte geprueft werden.
- Kapitalerhoehung durch Wandlung erfordert Notartermin, Gesellschafterbeschluss und Handelsregisteranmeldung.
- Formfehler in Wandeldarlehen- oder Kapitalerhoehungs-Dokumenten muessen identifiziert und geheilt werden.

## Fachbegriffe (kurz erklaert)

- **Wandeldarlehen** — Darlehen nach §§ 488 ff. BGB, das unter bestimmten Bedingungen (Trigger) in Gesellschaftsanteile umgewandelt wird.
- **SAFE** — Simple Agreement for Future Equity; Y-Combinator-Vorlage; kein Darlehen im Rechtssinne, sondern Vereinbarung auf zukuenftige Kapitalbeteiligung.
- **Wandlungspreis** — Preis je neu ausgegebenen Geschaeftsanteil; ergibt sich aus Bewertungs-Cap, Discount oder Finanzierungsrunde.
- **Cap-Table** — Gesellschafterliste inkl. aller voll verwasserten Anteile (fully diluted); zeigt Beteiligungsstruktur vor und nach Wandlung.
- **Qualified Financing** — Qualifiziertes Finanzierungsereignis; haeufigster Wandlungs-Trigger; meist definiert als neue Finanzierungsrunde ab einer Mindestbetrag-Schwelle.
- **Rangruecktritt** — Nachrangabrede nach § 39 InsO; stellt Wandeldarlehen insolvenzrechtlich nachrangig, um Ueberschuldungsausweis zu verhindern.
- **Beurkundungserfordernis** — Kapitalerhoehungen bei GmbH beduerften notarieller Beurkundung nach § 55 GmbHG; Formmangel fuehrt zu Nichtigkeit.
- **SAFE-Y-Combinator** — US-Standardvorlage für Seed-Investitionen; in Deutschland-Transaktionen oft angepasst oder ersetzt.

## Rechtsgrundlagen

- §§ 488 491 BGB — Darlehensrecht
- §§ 53 55 56 57 GmbHG — Satzungsaenderung, Kapitalerhoehung, Sacheinlage, Anmeldung
- § 40 GmbHG — Gesellschafterliste; Anmeldepflicht nach Aenderung
- § 15 GmbHG — Abtretung von Geschaeftsanteilen (Formpflicht)
- § 39 InsO — Nachrang; Rangruecktrittserklaerung
- §§ 125 126 BGB — Form; Schriftform
- GwG §§ 10 11 — KYC/AML-Pflichten bei Investoren
- eIDAS-VO (EU) 910/2014 — Elektronische Signatur

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Neue Vertragserstellung oder laufendes Mandat mit Wandelereignis?
2. Parteien und Konditionen erfassen: Darlehenshoehe, Zinssatz, Laufzeit, Wandlungspreis-Mechanik.
3. Beurkundungserfordernis pruefen: Liegt ein Formerfordernis vor? Notartermin erforderlich?
4. Passenden Skill auswaehlen (siehe Skill-Tour).
5. Nach Wandlung: Cap-Table aktualisieren, Gesellschafterliste einreichen, Handelsregister anmelden.

## Skill-Tour (was gibt es hier?)

- `mandat-triage-wandeldarlehen` — Wandeldarlehensmandat einordnen, Verfahrensroute bestimmen und erste Prioritaeten setzen.
- `parteien-erfassen` — Vertragsparteien vollstaendig identifizieren und dokumentieren; KYC-Vorab-Check.
- `darlehenshoehe-konditionen` — Darlehenshoehe, Zinsen, Laufzeit und Konditionen verhandeln und dokumentieren.
- `einsprachige-vertragsfassung-de` — Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten.
- `bilinguale-vertragserstellung` — Wandeldarlehensvertrag zweisprachig deutsch/englisch für internationale Transaktionen erstellen.
- `textform-vs-schriftform-vs-notariell` — Formerfordernis für einzelne Wandeldarlehens-Dokumente bestimmen und zuordnen.
- `beurkundungserfordernis-pruefung` — Beurkundungserfordernis pruefen; ob Notartermin erforderlich ist klaeren.
- `vertraulichkeit-und-sprachklausel` — Vertraulichkeits- und Sprachklauseln in Wandeldarlehensvertrag pruefen oder formulieren.
- `unterzeichnung-elektronisch-docusign` — Elektronische Unterzeichnung organisieren; eIDAS-Konformitaet pruefen.
- `kyc-aml-geldwaesche` — KYC- und AML-Anforderungen bei Investor-Onboarding pruefen.
- `rangruecktritt-formulieren` — Rangruecktrittserklaerung für insolvenzrechtlichen Nachrang formulieren.
- `wandlungsmechanik-konzipieren` — Wandlungsmechanik konzipieren: Preis, Verwasserungsschutz, Sonderrechte.
- `wandlungspreis-berechnung` — Wandlungspreis auf Basis der vertraglich vereinbarten Parameter berechnen.
- `wandelereignis-trigger-dispatcher` — Wandlungstrigger kategorisieren und an den richtigen Folge-Skill weiterleiten.
- `wandelereignis-eingang` — Eingehende Wandelereignis-Notification pruefen und naechste Schritte bestimmen.
- `wandlungspruefung-trigger-qualified-financing` — Wandlung bei qualifizierter Finanzierungsrunde als Trigger pruefen.
- `wandlungspruefung-trigger-maturity` — Wandlung bei Laufzeitablauf des Wandeldarlehens pruefen.
- `wandlungspruefung-trigger-liquidation` — Wandlung bei Liquidationsereignis oder Exit pruefen.
- `wandlungsausschluss-pruefung` — Pruefen, ob Wandlung gesperrt oder ausgeschlossen ist.
- `mehrere-wandeldarlehen-parallel` — Mehrere parallele Wandeldarlehen von verschiedenen Investoren koordinieren; Konflikte erkennen.
- `cap-table-update-pre-post` — Cap-Table vor und nach Wandlung aktualisieren; Verwasserungseffekte berechnen.
- `gesellschafterbeschluss-vorbereiten` — Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten.
- `gesellschafterbeschluss-kapitalerhoehung` — Gesellschafterbeschluss für Kapitalerhoehung nach Wandlung vorbereiten.
- `gesellschafterversammlung-einberufen` — Gesellschafterversammlung einberufen und Tagesordnung aufstellen.
- `sacheinlagebericht-werthaltigkeit` — Sacheinlagebericht erstellen und Werthaltigkeit pruefen.
- `notar-paket-uebermittlung` — Notarpaket für Beurkundungstermin zusammenstellen und uebermitteln.
- `handelsregisteranmeldung-kapitalerhoehung` — Handelsregisteranmeldung nach Kapitalerhoehung durch Wandlung vorbereiten.
- `gesellschafterliste-aktualisieren` — Gesellschafterliste nach Kapitalerhoehung aktualisieren und einreichen.
- `post-eintragung-checkliste` — Nacharbeiten nach Handelsregistereintragung abschliessen.
- `wandlung-kommunikation-paketverteilung` — Kommunikation und Dokumentenversand an alle Beteiligten nach Wandlungsentscheidung.
- `formfehler-heilungs-timeline` — Formfehler in Wandeldarlehen- oder Kapitalerhoehungs-Dokumenten identifizieren und Heilungsmassnahmen planen.
- `dokumenten-upload-extraktion` — Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren.

## Worauf besonders achten

- Beurkundungserfordernis nach § 55 GmbHG ist zwingend für Kapitalerhoehungen; formlose Wandlung fuehrt zur Nichtigkeit des Kapitalerhoehungsbeschlusses.
- Verwasserungsschutzklauseln (Anti-Dilution) muessen praesize formuliert sein; Broad-Based vs. Narrow-Based-Methode kann erhebliche Unterschiede im Wandlungspreis bewirken.
- Rangruecktritt muss vor Wandlung vorliegen, wenn Ueberschuldung droht; ex-post-Rangruecktritt schuetzt nicht rueckwirkend.
- KYC/AML-Pflichten des GwG gelten ab bestimmten Beteiligungsschwellen; fehlende Pruefung des Investors kann Haftung ausloesen.
- Mehrere parallel laufende Wandeldarlehen koennen Kollisionspunkte bei Triggern und Cap-Berechnung haben; Konsistenzpruefung ist unverzichtbar.

## Typische Fehler

- Wandlungspreis-Formel zu unpraezise: Fehlende Definition von Ausgangsgroessen (pre-money valuation, fully diluted cap) fuehrt zu Streit bei Wandlung.
- Notartermin zu spaet eingeplant: Notariatliche Termine bei DNOTA und Notaren brauchen Vorlaufzeit; Last-Minute-Beurkundung ist haeufig nicht moeglich.
- Gesellschafterliste nicht aktualisiert: Nach Wandlung und Eintragung muss Gesellschafterliste innerhalb eines Monats eingereicht werden (§ 40 GmbHG).
- Sacheinlagebericht fehlt: Bei Sachkapitalerhoehung durch Wandlung ist Sacheinlagebericht Pflicht (§ 56 GmbHG); fehlender Bericht blockiert Eintragung.
- SAFE als Darlehen klassifiziert: Falsches Bilanzierungsurteil für SAFE (kein Darlehen, sondern Eigenkapital-Instrument unter US-GAAP; unter HGB haeufig als Verbindlichkeit zu bilanzieren) kann steuerliche Folgen haben.

## Quellen und Aktualitaet

- Stand: 05/2026
- BGB, GmbHG, InsO, GwG, eIDAS-VO in aktuell geltender Fassung
- SAFE-Vorlage des Y-Combinators (Post-Money SAFE, aktuelle Version 2018)

---

## Skill: `mandat-triage-mehrere-parallel`

_Wandeldarlehensmandat einordnen Verfahrensroute bestimmen und erste Prioritaeten setzen. §§ 488 ff. BGB §§ 53 55 GmbHG. Prüfraster: Vertragstyp SAFE Convertible Note Laufzeit Wandlungsereignisse offene Punkte. Output: Mandatssteckbrief Routen-Empfehlung Datenliste. Abgrenzung: Triage und Einstieg..._

# Mandat-Triage Wandeldarlehen – Erstgespräch

## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Mehrere Parallel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Wandeldarlehen Lebenszyklus** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Rechtsform der Gesellschaft: GmbH oder UG (haftungsbeschränkt)
- Firmenname, HRB-Nummer, Amtsgericht, Sitz
- Namen und Rollen der Gesellschafterinnen (Anzahl, Anteile)
- Name und Rechtsform des Darlehensgebers (Privatperson oder juristische Person)
- Beabsichtigter Darlehensbetrag (EUR) und Laufzeit
- Zinssatz (Standard fünf Prozent p.a.)
- Gewünschte Wandelereignisse (Qualified Financing, Exit, Maturity)
- Sprachen-Stack: bilingual DE/EN oder nur DE
- Vorhandener Gesellschafterbeschluss zur grundsätzlichen Kapitalerhöhungsbereitschaft: ja/nein
- Zeitdruck / gewünschtes Unterzeichnungsdatum

## Rechtlicher Rahmen

### Primärnormen
- § 488 BGB (Darlehensvertrag)
- § 1 GmbHG (Rechtsform GmbH), § 5a GmbHG (UG haftungsbeschränkt)
- § 15 Abs. 3, Abs. 4 GmbHG (Anteilsübertragung, Form)
- § 55 ff. GmbHG (Kapitalerhöhung)
- § 126b BGB (Textform)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Rechtsform und Register prüfen
Klären: GmbH oder UG? Bei UG Mindestkapital EUR 1 (§ 5a GmbHG), Thesaurierungspflicht (§ 5a Abs. 3 GmbHG) ansprechen. HRB und Amtsgericht notieren.

### 2. Parteien und Vertretungsmacht erfassen
Gesellschaft: Geschäftsführung alleinvertretungsberechtigt oder Gesamtvertretung? Gesellschafterinnen: Zahl, Anteilsverhältnis, Privatpersonen oder juristische Personen? Darlehensgeber: Privatperson oder GmbH/KG – wer vertritt?

### 3. Wandelereignisse klären
Qualifizierte Finanzierungsrunde: Schwellenwerte Bewertung und Investitionsvolumen bereits bekannt? Exit-Trigger (Share Deal >50%, Asset Deal, IPO, Fusion)? Maturity mit Fall-back-Bewertung: Betrag schon vorstellbar?

### 4. Formfragen vorab
Sprachen-Stack: bilingual oder nur DE? DocuSign-Unterzeichnung akzeptiert? Notarielle Beurkundung gewünscht oder nur Textform?

### 5. Mandatssteckbrief erstellen
Strukturierte Zusammenfassung aller erfassten Punkte; offene Lücken markieren; Skill-Empfehlung ausgeben.

### 6. Nächsten Skill empfehlen
Empfehlung: `parteien-erfassen` für vollständige KYC-Daten, dann `darlehenshoehe-konditionen`.

## Beispiel-Mandatssteckbrief

| Feld | Inhalt |
|---|---|
| Gesellschaft | Sonnenglas Solartechnologie UG (haftungsbeschränkt), HRB 123456, AG Berlin |
| Stammkapital | EUR 1000, 100 Anteile à EUR 1 Nennwert |
| Gesellschafterinnen | Dr. Mira Schöneck 40 Anteile, Lina Habersaat 35 Anteile, Treasury 25 Anteile |
| Darlehensgeber | Northstar Pre-Seed Partners GmbH & Co. KG |
| Betrag | EUR 250000 |
| Laufzeit | 2 Jahre feste Laufzeit |
| Zinssatz | fünf Prozent p.a. (act/360) |
| Cap | EUR 4000000 Pre-Money |
| Discount | zwanzig Prozent |
| Sprache | bilingual DE/EN |
| Unterzeichnung | DocuSign (Textform § 126b BGB) |
| Gesellschafterbeschluss | noch nicht gefasst |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Wandelereignis schon eingetreten | Nachträgliche Vereinbarung problematisch | Wandelereignis kurz bevorstehend | Wandelereignis weit in Zukunft |
| Keine Fall-back-Bewertung vereinbart | Maturity-Wandlung unklar | Bewertung grob geschätzt | Bewertung durch TS belegt |
| Gesellschafterbeschluss fehlt | Mitwirkungspflicht § 5 ungesichert | Beschluss in Planung | Beschluss liegt vor |
| Mehrere parallele Wandeldarlehen | MFN und Stack unklar | Nur ein weiteres WD | Keine weiteren WD |

## Quellen und Updates

Stand: 05/2026.
- GmbHG: https://www.gesetze-im-internet.de/gmbhg/
- §§ 488 ff. BGB (Darlehen): https://www.gesetze-im-internet.de/bgb/__488.html
- § 55 GmbHG (Kapitalerhoehungsbeschluss): https://www.gesetze-im-internet.de/gmbhg/__55.html
- § 56 GmbHG (Sacheinlage): https://www.gesetze-im-internet.de/gmbhg/__56.html
- § 39 InsO (Nachraenge): https://www.gesetze-im-internet.de/inso/__39.html
- §§ 135, 143 InsO (Gesellschafterdarlehen, Anfechtung): https://www.gesetze-im-internet.de/inso/__135.html
- § 15a InsO (Insolvenzantragspflicht): https://www.gesetze-im-internet.de/inso/__15a.html
- § 19 IV GmbHG (Erleichterung Aufrechnung Stammeinlage gegen Gesellschafterforderung — Hinweis: § 19 IV GmbHG i.d.F. MoMiG 2008 weiterhin maßgeblich; DiRUG/DiREG haben Form (Online-Beurkundung) modifiziert, materielle Aufrechnungsregel unveraendert): https://www.gesetze-im-internet.de/gmbhg/__19.html
- DiRUG (BGBl. I 2021, 3338; in Kraft Bargruendung 01.08.2022): https://www.gesetze-im-internet.de/beurkg/__16a.html
- DiREG (in Kraft 01.08.2023; Online-Beurkundung Kapitalerhoehung/Satzungsaenderung bei einstimmigem Beschluss): https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html
- StaRUG (SanInsFoG, BGBl. I 2020, 3256; in Kraft 01.01.2021): https://www.gesetze-im-internet.de/starug/
- § 15b InsO (rechtsformneutrales Zahlungsverbot): https://www.gesetze-im-internet.de/inso/__15b.html
- Bei Aenderung GmbHG/UmwStG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 488 ff. BGB (Darlehen) → §§ 55, 56 GmbHG (Kapitalerhöhung, Sacheinlage) → § 39 InsO (Nachrangige Forderungen, Gesellschafterdarlehen) → §§ 135, 143 InsO (Anfechtung, Rückzahlung) → § 40 GmbHG (Gesellschafterliste) → § 15a InsO (Insolvenzantragspflicht)

---

## Skill: `begleitet-erstpruefung-und-mandatsziel`

_Begleitet: Erstprüfung, Rollenklärung und Mandatsziel._

# Begleitet: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Begleitet Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Wandeldarlehen Lebenszyklus** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Pruefungen und Leistungspunktsystem.
- `§ 16 HRG` — Pruefungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Pruefungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Begleitet: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** UG/GmbH ist Gesellschaftsform, keine Einzelquelle. Prüfe GmbHG §§ 5a, 7, 8, 16, 19, 55 ff.; BGB §§ 488 ff. und 311; ggf. WpPG/VermAnlG/KAGB, GwG, Steuerrecht und notarielle/registerrechtliche Anforderungen live.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Begleitet** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 55 GmbHG
- § 40 GmbHG
- § 53 GmbHG
- § 57 GmbHG
- § 56 GmbHG
- § 15 GmbHG
- § 5 GmbHG
- § 16 GmbHG
- § 51 GmbHG
- § 9 GmbHG
- § 19 GwG
- § 47 GmbHG

### Leitentscheidungen

- BGH VI ZR 232/09
- BGH VI ZR 171/18

---

## Skill: `beurkundungserfordernis-pruefung`

_Beurkundungserfordernis für Wandeldarlehen und Kapitalerhohung prüfen wenn Frage besteht ob Notartermin erforderlich ist. §§ 15 55 GmbHG § 311b BGB Formvorschriften. Prüfraster: Sacheinlage Kapitalerhohung GmbH-Anteil Vorratskapital Abtretungsverbot. Output: Formprüfungs-Memo mit Empfehlung. Abgr..._

# Beurkundungserfordernis-Prüfung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vertragsentwurf §§ 4 und 9
- Wandlungsmechanik: einstufig (Abtretung bestehender Anteile) oder zweistufig (Kapitalerhöhung + neue Anteile)?
- Besteht bereits ein Beschluss zur Kapitalerhöhung?
- Soll die Wandlung durch Abtretung bestehender Anteile oder durch Ausgabe neuer Anteile erfolgen?
- Enthalten Term Sheet oder Nebenvereinbarungen Anteilsübertragungen?

## Rechtlicher Rahmen

### Primärnormen
- § 15 Abs. 3 GmbHG (Beurkundungspflicht Verpflichtung zur Anteilsübertragung)
- § 15 Abs. 4 GmbHG (Beurkundungspflicht Anteilsübertragung selbst)
- § 55 Abs. 1 GmbHG (Kapitalerhöhungsbeschluss – notarielle Beurkundung gemäß § 53 Abs. 2 GmbHG)
- § 53 Abs. 2 GmbHG (Satzungsänderung durch Kapitalerhöhung – notariell)
- § 2 Abs. 3 GmbHG (Online-Beurkundung Gründung; durch DiRUG 2022 eingeführt, BeurkG § 16a)
- § 53 Abs. 4 GmbHG analog / BeurkG § 16a (Online-Beurkundung Kapitalerhöhung seit 1.8.2023 zulässig)
- § 311 Abs. 1 BGB (Schuldrechtliche Verpflichtung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Konstruktion des Wandlungsmechanismus prüfen
Einstufige Konstruktion: Lender tritt in bestehende Anteile ein (Abtretung § 15 Abs. 3 GmbHG → Beurkundungspflicht für den Verpflichtungsvertrag). Zweistufige Konstruktion: Lender erhält neue Anteile durch Kapitalerhöhung → schuldrechtliche Verpflichtung im Wandeldarlehensvertrag nicht beurkundungspflichtig; Beurkundungspflicht tritt erst bei Kapitalerhöhungsbeschluss (§ 53 Abs. 2 GmbHG) und Übernahme (§ 55 Abs. 2 GmbHG) ein.

### 2. Formulierung im Vertrag prüfen
Enthält § 4 eine unbedingte oder bedingte Pflicht zur Abtretung bestehender Anteile? → Beurkundungspflichtig. Enthält § 4 nur die Verpflichtung, bei Eintritt eines Wandlungsereignisses eine Kapitalerhöhung durchzuführen und neue Anteile auszugeben? → Nicht beurkundungspflichtig (herrschende Meinung).

### 3. Term Sheet und Nebenabreden
Alle Dokumente prüfen: Term Sheet, Gesellschaftervertrag, Investorenvereinbarung. Falls dort Anteilsabtretungen vereinbart sind: Formpflicht auf diese Dokumente ausdehnen.

### 4. Heilungsklausel prüfen
§ 9.3 Standard: Falls entgegen Annahme Beurkundungspflicht entsteht, verpflichten sich Parteien zur unverzüglichen notariellen Beurkundung. Kosten trägt die Gesellschaft. Bis zur Beurkundung wirtschaftliche Gleichstellung (§ 9.4).

### 5. Ergebnis dokumentieren
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Trennungsprinzip sicherstellen
Verpflichtungs- und Verfügungsebene sauber getrennt halten. Keine Formulierungen im Wandeldarlehensvertrag, die einen Direkterwerb bestehender Anteile ohne Kapitalerhöhung vorsehen.

### 7. Online-Beurkundung als Option prüfen (DiRUG/DiREG)
- Seit DiRUG (BGBl. I 2021, 3338; in Kraft 01.08.2022) ist Online-Beurkundung der GmbH-Bargruendung moeglich (§ 2 Abs. 3 GmbHG; § 16a BeurkG).
- Durch DiREG (Gesetz zur Ergaenzung der Regelungen zur Umsetzung der Digitalisierungsrichtlinie) ist seit 01.08.2023 die Online-Beurkundung erweitert auf: GmbH-Sachgruendung, GmbH-Satzungsaenderungen einschliesslich Kapitalmassnahmen, Uebernahmeerklaerungen bei Kapitalerhoehung, sowie Online-Beglaubigung für Vereinsregister-Anmeldungen. Wichtig: nicht-einstimmige Mehrheitsbeschluesse sind weiter physisch zu beurkunden (kein Online-Verfahren).
- Mit Lender im Ausland: Online-Beurkundung kann Reise- und Apostille-Aufwand sparen. Voraussetzung: Notar mit Online-Verfahren der Bundesnotarkammer (BNotK); elektronische Identifizierung via eID-Funktion oder Lichtbildausweis-Abgleich.
- Quelle: BMJ-Pressemitteilung https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html ; § 16a BeurkG https://www.gesetze-im-internet.de/beurkg/__16a.html

## Checkliste Beurkundungserfordernis

| Kriterium | Prüfung | Ergebnis |
|---|---|---|
| Wandlung durch neue Anteile (Kapitalerhöhung)? | ja/nein | nein → nicht beurkundungspflichtig |
| Wandlung durch Abtretung bestehender Anteile? | ja/nein | ja → beurkundungspflichtig |
| Term Sheet enthält Anteilsübertragung? | ja/nein | ja → Formprüfung |
| Heilungsklausel im Vertrag vorhanden? | ja/nein | nein → ergänzen |
| Kapitalerhöhungsbeschluss später notariell? | ja/nein | ja → Standard |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Einstufige Abtretung ohne Beurkundung | Vertrag formnichtig § 125 BGB | Unsicherheit über Konstruktion | Zweistufige Kapitalerhöhung |
| Term Sheet mit Anteilsabtretung | Formverstoß | Term Sheet unklar | Term Sheet ohne Abtretung |
| Keine Heilungsklausel | Heilung unmöglich ohne Beurkundung | Klausel unvollständig | Vollständige Heilungsklausel |
| Kapitalerhöhungsbeschluss ohne Notar | Eintragung Handelsregister scheitert | Notar noch nicht beauftragt | Notar bereits beauftragt |

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen und Updates

Stand: 05/2026.
- § 15 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 53 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__53.html
- § 55 GmbHG: https://www.gesetze-im-internet.de/gmbhg/__55.html
- § 2 III GmbHG (Online-Bargruendung seit 01.08.2022): https://www.gesetze-im-internet.de/gmbhg/__2.html
- § 16a BeurkG: https://www.gesetze-im-internet.de/beurkg/__16a.html
- DiRUG (BGBl. I 2021, 3338): https://www.bgbl.de/xaver/bgbl/start.xav?startbk=Bundesanzeiger_BGBl&start=//*[@attr_id=%27bgbl121s3338.pdf%27]
- DiREG-Inkrafttreten 01.08.2023 (Erweiterung Online-Verfahren auf Sachgruendung, Satzungsaenderungen, Kapitalerhoehung): https://www.bmjv.de/SharedDocs/Pressemitteilungen/DE/2022/0729_DIREG_DIRUG.html
- § 19 IV GmbHG (Aufrechnung Stammeinlage gegen Gesellschafterforderung; Hinweis: Erleichterungen durch MoMiG seit 2008, Beleg für Wandlung als Sacheinlage wegen Konfusion ueblich): https://www.gesetze-im-internet.de/gmbhg/__19.html
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 55 GmbHG
- § 40 GmbHG
- § 53 GmbHG
- § 57 GmbHG
- § 56 GmbHG
- § 15 GmbHG
- § 5 GmbHG
- § 16 GmbHG
- § 51 GmbHG
- § 9 GmbHG
- § 19 GwG
- § 47 GmbHG

### Leitentscheidungen

- BGH VI ZR 232/09
- BGH VI ZR 171/18

---

## Skill: `bilinguale-vertragserstellung`

_Wandeldarlehensvertrag zweisprachig deutsch und englisch erstellen für internationale Transaktionen oder ausl. Investoren. BGB Darlehen §§ 488 ff. BGB GmbHG Kapitalerhohung. Prüfraster: Terminologie-Konsistenz Rechtswahl governing-law jurisdiction. Output: bilingualer Vertragsentwurf mit Gegenübe..._

# Bilinguale Vertragserstellung DE/EN

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vollständige Parteidaten aus `parteien-erfassen`
- Konditionen aus `darlehenshoehe-konditionen`
- Wandlungsmechanik aus `wandlungsmechanik-konzipieren`
- Rangrücktrittsklausel aus `rangruecktritt-formulieren`
- Erweiterte Klauseln (Pro-rata, MFN, Liquidationspräferenz, Schiedsklausel) falls vereinbart
- Dateiformat: DOCX (python-docx), Zielordner

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform – ausreichend für Vertragsschluss)
- § 126 BGB (Schriftform – auf Verlangen zusätzlich)
- § 128 BGB (Notarielle Beurkundung – nur falls erforderlich)
- § 15 Abs. 3, Abs. 4 GmbHG (Beurkundungspflicht Anteilsübertragung)
- § 10.1 Standardklausel: Vorrang der deutschen Fassung

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Dokumentstruktur festlegen
Zweispaltige Word-Tabelle ohne Rahmenlinie: linke Spalte DE (breiter, ca. 55 %), rechte Spalte EN (ca. 45 %). Überschriften als Heading 2 in beiden Spalten. Paragrafen 0 bis 10 plus Signaturblock.

### 2. Präambel (§ 0) – beide Sprachen
DE: Gesellschaft (UG-Hintergrund, Stammkapital, Gesellschafterinnen), Unternehmensgegenstand, Finanzierungsbedarf, Wandeldarlehensstruktur, geplante Finanzierungsrunde. EN: Entsprechung mit deutschen Rechtsbegriffen in Klammern.

### 3. §§ 1 bis 3 – Darlehen, Laufzeit, Zinsen
Exakte Zahlen eintragen; keine Platzhalter [●] im ausgefüllten Vertrag. Zinssatz fünf Prozent p.a. act/360. Bankverbindung in Tabelle.

### 4. § 4 Wandlung – alle Trigger und Formel
Qualified Financing mit Schwellenwerten, Maturity, Liquidation Event. Wandlungspreis-Formel bilingual ausformulieren: CS = GK × (C / CV); alternativer Cap-Preis explizit.

### 5. §§ 5 bis 10 – Mitwirkung, Rangrücktritt, Informationsrechte, Vertraulichkeit, Form, Schluss
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Signaturblock
Vier Blöcke: Gesellschaft (Geschäftsführerin), Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber. DocuSign-Hinweis: "Dieser Vertrag kann mittels qualifizierter elektronischer Signatur (z. B. DocuSign) unterzeichnet werden."

## Beispiel-Sprachklausel (§ 10.1)

```
§ 10.1 Sprachklausel. Dieser Vertrag wird in deutscher und englischer Sprache ausgefertigt.
Die deutsche Sprachfassung ist allein verbindlich. Die englische Fassung dient ausschließlich
der besseren Verständlichkeit. Im Fall von Widersprüchen geht die deutsche Fassung vor.
Die in der englischen Fassung in Klammern verwendeten deutschen Begriffe sind verbindliche
Bezugnahmen auf die deutschen Rechtsbegriffe.

Section 10.1 Language clause. This Agreement is executed in German and English.
The German version shall be the only binding version. The English version is for
convenience only. In case of inconsistency, the German version prevails.
German terms in parentheses in the English version are binding references.
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Englische Fassung weicht inhaltlich ab | Auslegungsstreit | Kleinere Abweichungen | Paralleltext konsistent |
| Fehlende Sprachklausel | Unklare Maßgeblichkeit | Mündliche Verständigung | Sprachklausel vorhanden |
| Platzhalter [●] verbleiben | Vertrag nicht unterzeichnungsreif | Einzelne Felder offen | Alle Felder ausgefüllt |
| DocuSign-Hinweis fehlt | Unterzeichner unsicher über Verfahren | Hinweis nur mündlich | Schriftlicher Hinweis |

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften oder GmbHG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung mehrdeutiger Verträge) → Art. 3 Rom-I-VO (Rechtswahl im Vertrag) → § 184 Abs. 2 GVG (Amtssprache Deutsch bei Gericht) → § 55 Abs. 2 GmbHG (notarielle Beurkundung auf Deutsch)

<!-- AUDIT 27.05.2026
Problem : BGH VI ZR 232/09 (NJW 2010, 2812) – WRONG_TOPIC; tatsächlich: Schadensabrechnung und Restwert nach Kfz-Unfall (§ 249 Abs. 2 BGB), kein Bezug zu zweisprachigen Verträgen. Korrekte Fundstelle: NJW 2010, 2724.
Maßnahme: Leitsatz-Zitat entfernt. Kein verifizierter BGH-Ersatz zur Sprachpriorität in zweisprachigen Verträgen gefunden; OLG München 31 Wx 79/16 (GmbHR 2016, 543) verbleibt als valide Quelle.
Quelle: https://dejure.org/2010,477
-->

---

## Skill: `cap-table-darlehenshoehe-konditionen`

_Cap-Table vor und nach Wandlung aktualisieren und Verwasserungseffekte berechnen wenn Wandeldarlehen konvertiert. § 55 GmbHG Kapitalerhohung §§ 17 ff. GmbHG Gesellschafterliste. Prüfraster: Pre-Money Post-Money Wandlungspreis neue Anteile Verwasserung bestehende Gesellschafter. Output: Cap-Table-..._

# Cap-Table Update – Pre-Money und Post-Money

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Aktuelle Gesellschafterliste (§ 40 GmbHG): Name, Anteilszahl, Nennwert, Prozent
- Wandlungsberechnung aus `wandlungspreis-berechnung` (neue Anteile für Lender)
- Kapitalerhöhung neue Investoren: Investitionsbetrag, Preis je Anteil (Rundenpreis Preis A), neue Anteile
- ESOP-Pool (falls vorhanden): Anteilszahl, ausgegeben/reserviert
- Nennwert je Anteil: EUR 1 (Standard)

## Rechtlicher Rahmen

### Primärnormen
- § 40 GmbHG (Gesellschafterliste – Geschäftsführerin reicht nach Kapitalerhöhung neue Liste ein; oder Notar nach § 40 Abs. 2 GmbHG)
- § 55 Abs. 1 GmbHG (Kapitalerhöhung)
- § 5 Abs. 1 GmbHG (Mindestanteilsnennwert EUR 1)
- § 272 HGB (Eigenkapitalausweis)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel Pre-Money-Cap-Table (Sonnenglas UG)

| Gesellschafter | Anteile | Nennwert (EUR) | Prozent |
|---|---|---|---|
| Dr. Mira Schöneck | 40 | 40 | 40.00 % |
| Lina Habersaat | 35 | 35 | 35.00 % |
| Treasury | 25 | 25 | 25.00 % |
| Gesamt | 100 | 100 | 100.00 % |
| Stammkapital | | EUR 100 | |

## Beispiel Post-Money-Cap-Table (nach Wandlung + Seed EUR 1 Mio / Pre-Money EUR 6 Mio)

| Gesellschafter | Anteile | EUR | Prozent |
|---|---|---|---|
| Dr. Mira Schöneck | 40 | 40 | 29.63 % |
| Lina Habersaat | 35 | 35 | 25.93 % |
| Treasury | 25 | 25 | 18.52 % |
| Northstar (Lender, Wandlung) | 7 | 7 | 5.19 % |
| Seed-Investoren (EUR 1 Mio / EUR 40000) | 25 | 25 | 18.52 % |
| ESOP (bestehend, noch frei) | 3 | 3 | 2.22 % |
| Gesamt | 135 | 135 | 100.00 % |
| Stammkapital nach KE | | EUR 135 | |

Verwässerung Schöneck: 40 % → 29.63 % = −10.37 Prozentpunkte

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| ESOP-Pool nicht einbezogen | Verwässerung unterschätzt | ESOP-Größe unbekannt | ESOP vollständig erfasst |
| Falsche Anteilszahl Lender | Cap-Table inkorrekt | Aufrundung strittig | Exakte Berechnung |
| Stammkapital-Erhöhung nicht ins HR eingetragen | Gesellschafterliste veraltet | Eintragung beantragt | Eingetragen |
| Alte Gesellschafterliste verwendet | Altdaten | Teils aktuell | Aktuelle Liste gem. § 40 GmbHG |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, unverzügliche Aktualisierung nach Wandlung) → § 15 GmbHG (Abtretung Anteile) → § 17 GmbHG (Mehrfachabtretung) → § 16 GmbHG (Gesellschafterstellung, Legitimationswirkung Liste) → § 55 GmbHG (Kapitalerhöhungsbeschluss, neue Anteile)

---

## Skill: `dokumenten-upload-formfehler-heilungs`

_Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrechte. Output: strukturiertes Datenmemo mit Extraktionsergebni..._

# Dokumenten-Upload und Datenextraktion

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Hochgeladene Dokumente: Term Sheet, Share Purchase Agreement (SPA), Investor Rights Agreement (IRA), Shareholders Agreement (SHA), Beteiligungsvertrag
- Gesuchte Parameter: Pre-Money, Post-Money, Investitionsvolumen, Anteilsklassen, Nennwert, Vesting, ESOP, Liquidationspräferenzen, Anti-Dilution

## Rechtlicher Rahmen

### Primärnormen
- § 15 GmbHG (Anteilsklassen und Übertragung)
- § 272 HGB (Eigenkapitalausweis nach Klassen)
- § 194 AktG analog (Wandelschuldverschreibungen und Klassen – Orientierung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel-Extrakt Term Sheet

| Parameter | Wert | Quelle |
|---|---|---|
| Pre-Money-Bewertung | EUR 6000000 | Term Sheet Cl. 2.1 |
| Investitionsvolumen | EUR 1000000 | Term Sheet Cl. 2.1 |
| Anteilsklassen | Ordinary + Series A Preferred | Term Sheet Cl. 3 |
| Liquidationspräferenz Series A | 1x non-participating | Term Sheet Cl. 4 |
| ESOP-Pool | zehn Prozent (post-money) | Term Sheet Cl. 5 |
| Anti-Dilution | Broad-based weighted average | Term Sheet Cl. 6 |
| Qualifiziertes Financing nach WDV | Pre-Money ≥ EUR 4 Mio, Vol. ≥ EUR 500000 | WDV § 4.2 lit. a |
| Ist Qualified Financing? | Ja (beide Schwellen erfüllt) | Prüfung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Term Sheet nur als Absichtserklärung | Zahlen unverbindlich | Term Sheet mit Bindungswirkung unklar | Verbindliches Term Sheet |
| ESOP-Pool post-money ohne Klarstellung | Vollverwässerte Basis falsch berechnet | Unklar ob pre/post | Eindeutig pre-money |
| Liquidationspräferenz höher als 1x | Lender-Barausschüttung bevorzugt | Participating Preferred | Non-participating 1x |
| Kein Pre-Money im Dokument | Berechnung nicht möglich | Nur Post-Money | Pre-Money explizit |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG/HGB-Eigenkapitalausweis aktualisieren.

## Vertiefung — Relevante Normen

### Normen-Ergänzung und Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen

§ 12 HGB i.V.m. § 12 HRV (elektronische Einreichung Handelsregister) → Art. 25 eIDAS-VO (qualifizierte elektronische Signatur) → § 378 FamFG (Zurückweisung bei Formmängeln) → § 40 GmbHG (Einreichungspflicht Gesellschafterliste)

---

## Skill: `einsprachige-vertragsfassung`

_Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-Sonderrechte. Output: vollständiger Vertragsentwurf auf Deutsc..._

# Einsprachige Vertragsfassung (nur DE)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Fertiger Inhalt der deutschen Spalte der bilingualen Fassung (aus `bilinguale-vertragserstellung`)
- Zieldatei: DOCX, einspaltig
- Gewünschte Schriftgröße und Zeilenabstand (Standard: Times New Roman 12 pt, 1.5-facher Zeilenabstand)
- Seitenränder: Standard 2.5 cm ringsum

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform), § 126 BGB (Schriftform)
- § 10.1 Sprachklausel (nur DE-Fassung ohne EN-Spalte – dennoch materiell identisch mit bilingualer Fassung)
- Keine gesonderten Anforderungen: Die einsprachige Fassung unterliegt denselben Formregeln wie die bilinguale Fassung.

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beispiel-Dokumentstruktur

```
WANDELDARLEHENSVERTRAG
zwischen
[Parteien]

§ 0 Präambel
§ 1 Darlehensgewährung und Auszahlung
§ 2 Laufzeit und Rückzahlung
§ 3 Verzinsung
§ 4 Wandlung
§ 5 Mitwirkungspflichten der Gesellschafterinnen
§ 6 Qualifizierter Rangrücktritt
§ 7 Informationsrechte
§ 8 Vertraulichkeit
§ 9 Form, Beurkundung und Ausfertigung
§ 10 Schlussbestimmungen

[Signaturblock: Gesellschaft, Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Inhalt weicht von bilingualer Fassung ab | Zwei verschiedene Vertragsfassungen in Umlauf | Einzelne Formulierungen abweichend | Identischer Inhalt |
| Paragrafenverweise falsch | Lückenhaftes Dokument | Ein Verweis fehlerhaft | Alle Verweise korrekt |
| Signaturblock unvollständig | Unterzeichnung verhindert | Ein Block fehlend | Alle vier Blöcke vollständig |
| Schriftgröße und Layout unleserlich | Professioneller Eindruck fehlt | Geringfügige Formatmängel | Lesefreundliches Layout |

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung) → § 305c Abs. 2 BGB (Unklarheitenregelung AGB) → § 184 GVG (Amtssprache) → §§ 55 Abs. 2, 56 GmbHG (Beurkundung, Sacheinlage)

---

## Skill: `formfehler-heilungs-timeline`

_Formfehler in Wandeldarlehen oder Kapitalerhohungsdokumenten identifizieren und Heilungsmassnahmen planen. §§ 125 311b BGB Nichtigkeit §§ 15 55 GmbHG Formerfordernisse. Prüfraster: Formmangel Nichtigkeit Heilung Nachbeurkundung Fristen. Output: Fehlerliste Heilungsplan Fristenkalender. Abgrenzung..._

# Formfehler und Heilungs-Timeline

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Wandeldarlehensvertrag (Form und Datum)
- Wandlungs-Erklärung (falls erfolgt)
- Bisherige Beurkundungs-Schritte
- Insolvenz-Lage Gesellschaft (drohend? eröffnet?)
- Verhältnis Gesellschaft-Lender (vertrauensvoll? streitig?)

## Schritt 1 — Form-Stufen-Übersicht

### Form-Hierarchie

| Form | Norm | Anwendungsbereich |
|---|---|---|
| Mündlich | – | Selten (Rangrücktritt nicht möglich) |
| Textform | § 126b BGB | Mindest bei Verbraucher Vertragsschluss |
| Schriftform | § 126 BGB | Beweis-Funktion Standard |
| Elektronische Form | § 126a BGB | Qualifizierte elektronische Signatur |
| Notarielle Beurkundung | § 128 BGB iVm § 15 GmbHG | Anteils-Übertragungs-Verpflichtung |

### Schriftform vs. Elektronische Form

- **§ 126a BGB** — qualifizierte elektronische Signatur (QES) ersetzt Schriftform
- **SMS-OTP** / **DocuSign-Standard** — fortgeschrittene Signatur (Art. 26 eIDAS), nicht qualifiziert
- **Bei Schriftform-Erfordernis** ist QES erforderlich
- **eIDAS 2.0** VO 2024/1183 — EU-weite Anerkennung

## Schritt 2 — Wandeldarlehensvertrag Form

### Verpflichtungs-Geschäft (Wandeldarlehensvertrag)

- **Textform § 126b BGB** ausreichend (Lenders Beweis-Sicherheit)
- **Schriftform empfohlen** für Rangrücktritt-Klarheit
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Verfügungs-Geschäft (Anteils-Übertragung bei Wandlung)

- **Notarielle Beurkundung** zwingend § 15 Abs. 3 GmbHG bei Verfügung über existierende Anteile
- **Bei Wandlung durch Kapitalerhöhung** Kapitalerhöhungs-Beschluss notariell zu beurkunden § 53 Abs. 2 GmbHG
- **Übernahme-Erklärung** beim Notar
- **Handelsregister-Anmeldung** notariell beglaubigt § 12 Abs. 1 HGB

### Konkrete Sequenz bei Wandlung

1. Lender erklärt Wandlung schriftlich
2. Geschäftsführer beruft Gesellschafterversammlung ein
3. Kapitalerhöhungs-Beschluss notariell beurkundet
4. Übernahme-Erklärung des Lenders notariell beurkundet (am gleichen Termin möglich)
5. Anmeldung HR notariell beglaubigt
6. Eintragung HR
7. Aktualisierung Gesellschafterliste

## Schritt 3 — Heilungs-Tatbestände

### Form-Mangel beim Wandeldarlehens-Vertrag

#### Bei mündlich vereinbartem Vertrag

- **Beweisbarkeit fragwürdig**
- **Rangrücktritt nicht wirksam** § 39 Abs. 2 InsO erfordert Schriftform für klaren Inhalt
- **Heilung** durch schriftliche Bestätigung
- **Nachträgliche Schriftform** ist möglich, aber Wirkungs-Tag (ex tunc oder ex nunc?) streitig

#### Bei Textform/E-Mail

- **Grundsätzlich wirksam** für Verpflichtungsgeschäft
- **Bei Rangrücktritt fragwürdig** — Streit-Risiko
- **Empfehlung Schriftform-Heilung** durch Nachvertrag

### Form-Mangel bei Wandlungs-Erklärung

- **Empfangsbedürftige Willenserklärung** Lender → Gesellschaft
- **Form nach Vertrag** — typisch Schriftform empfohlen
- **Bei fehlender Schriftform** Heilung durch nachträgliche Bestätigung

### Form-Mangel bei Beschluss

- **Notarielle Beurkundung** Pflicht
- **Bei fehlender Beurkundung** Beschluss nichtig § 125 BGB
- **Heilung nur durch erneuten beurkundeten Beschluss**

## Schritt 4 — Heilungs-Timeline kritisch

### Beispiel-Fall

```
Tag 0: Wandeldarlehens-Vertrag unterzeichnet
 (Textform via DocuSign mit SMS-OTP)
Tag 1-7: Auszahlung Darlehen
Tag 8: Gesellschaft uebermittelt Quartals-Bericht
 Liquiditaets-Schwierigkeiten erkennbar
Tag 9: Geschaeftsfuehrer-Sitzung — Sanierungs-Plan
 Pruefung Zahlungs-Unfaehigkeit § 17 InsO
Tag 14: Insolvenz-Antrag droht
Tag 15: Insolvenz-Antrag eingereicht
```

#### Risiko-Konstellation

- **Wandeldarlehens-Vertrag in Textform** möglicherweise nicht qualifiziert für Rangrücktritt-Wirkung
- **In Insolvenz** Rangrücktritt-Klausel ggf. nicht wirksam — Lender als ungesicherter Gläubiger statt nachrangiger Gläubiger
- **Heilung nicht mehr möglich** nach Insolvenz-Eröffnung
- **Anfechtungs-Risiko** § 130 ff. InsO bei nachträglicher Sicherheits-Bestellung

#### Empfehlung

- **Schriftform-Heilung sofort** bei Vertragsschluss
- **QES-Signatur** wenn elektronisch
- **Notar-Vorab-Konsultation** für Wandlungs-Beschluss bei späteren Trigger

## Schritt 5 — Heilungs-Vorgehensweise

### Schritt 5a — Form-Mangel-Identifikation

- Vertrags-Prüfung
- Unterschriften-Form
- Datum-Stempel
- Vollmachts-Form

### Schritt 5b — Heilungs-Vereinbarung

```
Bestaetigung des Wandeldarlehens-Vertrags vom [Datum]

Die Parteien bestaetigen hiermit den am [Datum] (oder
in [Form]) abgeschlossenen Wandeldarlehens-Vertrag.

Die Bestaetigung erfolgt in Schriftform gem. § 126 BGB
zur Sicherstellung der Beweis- und Rangruecktritt-Funktion.

Die wesentlichen Vertragsinhalte:
[Wiedergabe Inhalt]

Die Heilung wirkt rueckwirkend auf den urspruenglichen
Vertrags-Schluss.

[Ort Datum]
[Lender-Unterschrift] [Gesellschaft-Unterschrift]
```

### Schritt 5c — Notarielle Beurkundung

- Bei Wandlungs-Beschluss
- Beim Notar Termin vereinbart
- Vorabe-Konsultation
- Beurkundungs-Kosten klären

## Schritt 6 — Anfechtungs-Risiken § 130 ff. InsO

### Konstellationen

- **§ 130 InsO** Kongruenz-Anfechtung — wenn Bestellung nach Insolvenz-Antrag-Stellung
- **§ 131 InsO** Inkongruenz-Anfechtung — wenn keine entsprechende Gegenleistung
- **§ 132 InsO** unmittelbar nachteilige Rechtsgeschäfte
- **§ 133 InsO** Vorsatz-Anfechtung — bei Vorsatz auf Gläubiger-Benachteiligung

### Heilungs-Maßnahmen kurz vor Insolvenz

- **Risiko hoch** dass Heilung selbst angefochten wird
- **Anwalts-Beratung** spezifisch Anfechtung
- **Dokumentation** Vorab-Vereinbarung

### Schutz-Strategie

- **Frühe Heilung** vor Krise
- **Bargeschäft-Klausel** wenn Heilung zugleich mit Auszahlung
- **Rangrücktritt** klar als qualifiziert formuliert

## Schritt 7 — Insolvenz-Sonderfall

### Wenn Insolvenz droht

- **Sofortige Form-Heilung** sicherstellen
- **Beratung mit Skill** `mandat-triage-insolvenzrecht`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wandlung erwägen** vor Insolvenz-Eröffnung

### Nach Insolvenz-Eröffnung

- **Wandlung praktisch ausgeschlossen** Gesellschaft-Verfügung Insolvenz-Verwalter
- **Lender als Insolvenz-Gläubiger** mit Rang nach § 39 Abs. 2 InsO (bei wirksamen qualifiziertem Rangrücktritt)
- **Forderungs-Anmeldung** bei Insolvenz-Tabelle § 174 InsO

## Schritt 8 — Notar-Kommunikation

### Vorab-Konsultation

- **Inhalts-Klärung** Wandlungs-Beschluss
- **Form-Anforderungen** klären
- **Vollmachts-Prüfung**
- **Termin-Vorbereitung**

### Notar-Auftrag

```
Sehr geehrte/r Notar/in,

wir benoetigen Beurkundungs-Termin für:

- Kapitalerhoehungs-Beschluss § 53 Abs. 2 GmbHG
- Uebernahme-Erklaerung Wandeldarlehens-Lender
- HR-Anmeldung

Wandeldarlehens-Vertrag vom [Datum] (Kopie als Anlage)
Wandlungs-Erklaerung Lender vom [Datum] (Kopie als Anlage)
Gesellschafterliste aktuell (Kopie als Anlage)

Termin-Vorschlag: [Datum-Vorschlaege]
```

### Termin-Logistik

- Notar wählt Datum
- Vorab-Entwürfe versenden
- Mandanten-Vorbereitung (Vollmachten Ausweise)
- Notar-Beurkundungs-Gebühren GNotKG

## Schritt 9 — Häufige Form-Fehler in der Praxis

### Fehler 1: Fehlende Unterschriften aller Parteien

- Heilung durch Nachunterzeichnung
- Wenn nicht möglich: Vertragsbestätigung

### Fehler 2: Datum-Lücken

- Bei undatierter Unterschrift Vermutung Unterzeichnungs-Datum
- Klärung durch Nachbestätigung

### Fehler 3: Vertretungs-Mangel

- Vollmacht-Vorlage erforderlich
- Heilung durch Genehmigung § 177 BGB

### Fehler 4: Elektronische Signatur ohne QES

- Heilung durch Schriftform-Nachvertrag

### Fehler 5: Vergessen Wandlungs-Beschluss

- Bei Wandlung ohne Beschluss — Wandlung nichtig
- Heilung durch nachfolgenden beurkundeten Beschluss

## Schritt 10 — Compliance-Workflow

### Vor Vertragsschluss

- Form-Check (Schrift Notar wenn nötig)
- QES-Signatur wenn elektronisch
- Notar-Vorab-Beratung

### Bei Vertragsschluss

- Alle Unterschriften vollständig
- Datum klar
- Vertretungs-Vollmachten

### Vor Wandlung

- Notar-Termin früh vereinbaren
- Beschluss-Entwurf vorab
- Lender-Übernahme-Erklärung vorab

### Bei Wandlung

- Beurkundung an einem Termin (Beschluss + Übernahme)
- HR-Anmeldung
- Gesellschafterliste-Update

### Nach Wandlung

- HR-Eintragung abwarten
- Aktualisierung Cap-Table
- Steuer-Meldung wenn relevant

## Verzahnung mit anderen Skills

- `beurkundungserfordernis-pruefung` — Detail Beurkundungs-Prüfung
- `textform-vs-schriftform-vs-notariell` — Form-Stufen
- `unterzeichnung-elektronisch-docusign` — eIDAS-Detail
- `wandelereignis-trigger-dispatcher` — Wandlungs-Ereignis-Master
- `gesellschafterbeschluss-kapitalerhoehung` — Beschluss-Inhalt
- `notar-paket-uebermittlung` — Notar-Kommunikation
- `rangruecktritt-formulieren` — Insolvenz-Aspekt

## Ausgabe

- `formfehler-timeline-{az}.md` mit Form-Audit Risiko-Fenster Heilungs-Plan
- Heilungs-Vereinbarung-Entwurf
- Notar-Termin-Vorbereitung
- Bei Insolvenz-Risiko: Eskalations-Memo
- Anfechtungs-Risiko-Memo
- Frist im Fristenbuch (Heilung sofort)

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- BGB §§ 125 126 126a 126b 128 177
- GmbHG §§ 15 53
- HGB § 12
- InsO §§ 39 130 131 132 133 174
- eIDAS-VO 910/2014 und 2024/1183
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- GNotKG

---

## Skill: `gesellschafterbeschluss-vorbereiten`

_Gesellschafterbeschluss für Wandeldarlehensaufnahme oder Satzungsaenderung vorbereiten. §§ 46 53 GmbHG Gesellschafterbeschluesse. Prüfraster: Beschlussgegenstand Mehrheiten Ladungspflicht Form Anlagen. Output: Beschlussentwurf Sitzungsprotokoll. Abgrenzung: nicht für Beschluss zur Kapitalerhohung..._

# Gesellschafterbeschluss vorbereiten (vor Unterzeichnung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Gesellschaft: Firma, HRB, Stammkapital, Gesellschafterinnen mit Anteilen
- Beschlussthema: Grundsatzbeschluss Wandeldarlehen + Bereitschaft Kapitalerhöhung
- Abstimmungsquorum: einstimmig oder Mehrheitsbeschluss nach Satzung?
- Einberufungsform: schriftlich, E-Mail oder Vollversammlung ohne Einberufung?
- Datum der Beschlussfassung

## Rechtlicher Rahmen

### Primärnormen
- § 46 Nr. 5 GmbHG (Gesellschafterversammlung zur Aufnahme neuer Gesellschafter)
- § 51 GmbHG (Einberufung, Ladungsfrist mindestens eine Woche)
- § 51 Abs. 3 GmbHG (Beschlussfassung ohne Einberufung bei Anwesenheit / Einverständnis aller)
- § 47 GmbHG (Abstimmung, Mehrheitserfordernisse)
- § 53 GmbHG (Satzungsänderung bedarf drei Viertel der abgegebenen Stimmen und notarieller Beurkundung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Art des Beschlusses klären
Option A – Vollversammlung ohne Einberufung (§ 51 Abs. 3 GmbHG): Alle Gesellschafterinnen anwesend und einverstanden. Schnellste Variante. Option B – Einberufung mit einer Woche Frist: Schriftliche Einladung mit Tagesordnung. Option C – Umlaufbeschluss: Schriftliche Zustimmung aller Gesellschafterinnen.

### 2. Tagesordnungspunkt formulieren
"TOP 1: Grundsatzbeschluss zur Bereitschaft der Gesellschafterinnen zur Durchführung einer Kapitalerhöhung gegen Sacheinlage (Forderung aus Wandeldarlehen) im Wandlungsfall gemäß § 4 des Wandeldarlehensvertrags vom [Datum]."

### 3. Beschlusstext entwerfen
"Die Gesellschafterinnen erklären einvernehmlich ihre Bereitschaft, im Falle der wirksamen Ausübung der Wandlungsoption durch den Darlehensgeber gemäß § 4 des Wandeldarlehensvertrags alle erforderlichen gesellschaftsrechtlichen Maßnahmen zur Durchführung der Kapitalerhöhung gegen Sacheinlage, zur Zulassung des Darlehensgebers als neuer Gesellschafter und zum Verzicht auf Bezugsrechte zu ergreifen."

### 4. Protokoll erstellen
Unterschriebenes Protokoll mit Datum, Ort, Anwesende, Abstimmungsergebnis, Fassung des Beschlusstexts. Aufbewahrung in Gesellschaftsakte.

### 5. Abstimmungsergebnis dokumentieren
Einstimmig oder Mehrheitsabstimmung nach Quorum (§ 47 GmbHG). Bei Satzungsänderung: drei Viertel der Stimmen + notarielle Beurkundung (§ 53 GmbHG).

### 6. Verhältnis zum späteren Kapitalerhöhungsbeschluss
Dieser Beschluss ist kein Kapitalerhöhungsbeschluss i.S.d. § 55 GmbHG (der muss notariell beurkundet werden). Er dokumentiert nur die Absichtsbekundung. Der eigentliche Kapitalerhöhungsbeschluss folgt unter `gesellschafterbeschluss-kapitalerhoehung`.

## Beispiel-Protokoll

```
Protokoll der Gesellschafterversammlung der
Sonnenglas Solartechnologie UG (haftungsbeschränkt)
Berlin, [Datum]

Anwesend:
- Dr. Mira Schoeneck (40 Anteile, 40 %)
- Lina Habersaat (35 Anteile, 35 %)
(Treasury-Anteile: 25 Anteile, nicht abstimmend)

TOP 1: Grundsatzbeschluss Wandeldarlehen Northstar
Die Gesellschafterinnen erklären einvernehmlich ihre Bereitschaft ...
[Beschlusstext vollständig]

Abstimmung: einstimmig angenommen.

[Unterschriften Dr. Schoeneck, Habersaat]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Protokoll fehlt | Beweislosigkeit Beschlussfassung | Protokoll nachgereicht | Protokoll sofort vorhanden |
| Ladungsfrist nicht eingehalten, Einwände | Beschluss anfechtbar | Nachträgliche Zustimmung | Ladungsfrist gewahrt oder Verzicht |
| Gesellschafterin verweigert Mitwirkung | Wandlungsblockade | Gesellschafterin unentschlossen | Alle bereit |
| Grundsatzbeschluss als Kapitalerhöhungsbeschluss fehlverstanden | Notarielle Beurkundung irrtümlich unterlassen | Unklare Beschlussfassung | Eindeutige Unterscheidung |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 46 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 51 GmbHG (Einberufung Gesellschafterversammlung, Ladungsfrist eine Woche) → § 47 GmbHG (Beschlussfassung, Mehrheitserfordernisse) → § 53 GmbHG (Satzungsänderung, notarielle Form) → § 43 GmbHG (Geschäftsführerhaftung bei Pflichtverletzung) → § 56 Abs. 2 GmbHG (Sacheinlagebericht, Werthaltigkeit)

---

## Skill: `gesellschafterliste-aktualisieren`

_Gesellschafterliste nach Kapitalerhohung durch Wandlung aktualisieren und beim Handelsregister einreichen. § 40 GmbHG Gesellschafterliste § 16 GmbHG Legitimationswirkung. Prüfraster: neue Gesellschafter Anteile Stammnummern Notar Einreichungsfrist. Output: aktualisierte Gesellschafterliste Einrei..._

# Gesellschafterliste aktualisieren (§ 40 GmbHG)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vorherige Gesellschafterliste (aus dem Handelsregister)
- Ergebnis der Kapitalerhöhung (neue Anteile, Nennwert, Gesellschafternummer)
- Vollständige Daten Lender (Name, Geburtsdatum, Anschrift oder Sitz und Vertreter)
- Notar (hat Kapitalerhöhung beurkundet und überreicht normalerweise aktualisierte Liste)
- Datum der Beurkundung und des vorgesehenen Einreichungsdatums

## Rechtlicher Rahmen

### Primärnormen
- § 40 Abs. 1 GmbHG (Geschäftsführerin reicht neue Gesellschafterliste bei Änderung ein; Pflichtinhalte durch DiRUG/Gesellschafterlistenverordnung erweitert: prozentuale Beteiligung am Stammkapital, ggf. Geburtsname, weitere Identifikatoren)
- § 40 Abs. 2 GmbHG (Mitwirkung eines Notars: Notar reicht Liste ein, wenn er an Änderung mitgewirkt hat)
- Gesellschafterlistenverordnung (GesLV, in Kraft 1.7.2018, modifiziert durch DiRUG) — Pflichtinhalte und Format
- § 16 GmbHG (Gutglaubenswirkung der Gesellschafterliste: nur als Gesellschafter gilt, wer eingetragen ist)
- § 15 GmbHG (Anteilsübertragung – Vollwirkung erst mit Eintragung)
- § 19 GwG (Transparenzregister – wirtschaftlich Berechtigte nach Änderung melden; Vollregister seit August 2021)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Listenentwurf erstellen
Alle Gesellschafterinnen und neuer Lender mit vollständigen Angaben gemäß § 40 Abs. 1 GmbHG i.V.m. GesLV:
- Laufende Nummer (fortlaufend, keine Lücken)
- Gesellschaftername (Vor- und Nachname oder Firma); bei natürlichen Personen ggf. Geburtsname, wenn abweichend
- Geburtsdatum (natürliche Person) oder HRB + Amtsgericht (juristische Person)
- Anschrift (Wohnanschrift oder Geschäftsanschrift Sitz)
- Anzahl der Geschäftsanteile und Nennwert (in EUR)
- Prozentuale Beteiligung am Stammkapital (Pflicht seit DiRUG)
- Datum des Erwerbs (Beurkundungsdatum Kapitalerhöhung)

### 2. Vollständigkeitsprüfung
Alle alten Gesellschafterinnen unverändert übernehmen (Anteile, Nennwert). Neuen Lender-Eintrag hinzufügen. Gesamtstammkapital prüfen: Summe aller Nennwerte = neues Stammkapital.

### 3. Einreichung durch Notar (§ 40 Abs. 2 GmbHG)
Da Notar an Kapitalerhöhung mitgewirkt hat, reicht er die neue Liste ein. Frist: unverzüglich nach Beurkundung.

### 4. Gutglaubenswirkung beachten
Ab Einreichung der neuen Liste gilt der Lender als Gesellschafter (§ 16 Abs. 1 GmbHG). Vor Einreichung: kein Stimmrecht, kein Gewinnbezugsrecht, keine HR-Legitimation.

### 5. Transparenzregister aktualisieren (§ 19 GwG)
Falls Lender nach Kapitalerhöhung wirtschaftlich Berechtigter (mehr als 25 %) wird: Meldung an Transparenzregister unverzüglich nach Eintragung ins Handelsregister.

### 6. Kopie an alle Parteien
Aktuelle Gesellschafterliste (nach HR-Eintragung) an Geschäftsführerin, alle Gesellschafterinnen, Lender, Steuerberater. Ablage in Gesellschaftsakte.

## Muster-Gesellschafterliste (Auszug)

```
Gesellschafterliste der Sonnenglas Solartechnologie UG (haftungsbeschränkt)
Berlin, HRB 123456 B, Amtsgericht Charlottenburg
Stand: [Datum nach Kapitalerhöhung]

Nr. | Name | Geburtsdatum / HRB | Anschrift | Anteile | Nennwert EUR | Erwerb
1 | Dr. Mira Schoeneck | [Datum] | [Anschrift] | 40 | 40 | [Gründungsdatum]
2 | Lina Habersaat | [Datum] | [Anschrift] | 35 | 35 | [Gründungsdatum]
3 | [Treasury GmbH] | HRB ●, AG ● | [Anschrift] | 25 | 25 | [Datum]
4 | Northstar Pre-Seed Partners GmbH & Co. KG | HRA 99999, AG Frankfurt | [Anschrift] | 7 | 7 | [Beurkundungsdatum KE]

Gesamt: 107 Anteile, Stammkapital EUR 107
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Liste nicht eingereicht | Lender hat keine Gutglaubensposition | Liste in Erarbeitung | Notar reicht sofort ein |
| Fehlerhafte Anteilszahl | HR-Liste und tatsächliche Beteiligung weichen ab | Kleiner Tippfehler | Exakt korrekt |
| Transparenzregister nicht aktualisiert | GwG-Bußgeld (§ 56 GwG) | Frist läuft | Aktualisierung bestätigt |
| Lender als Gesellschafter ohne HR-Eintragung | Stimmrechte, Gewinnrechte blockiert | Eintragung beantragt | Eintragung erfolgt |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG § 40/§ 16 aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 40 GmbHG (Gesellschafterliste, Einreichungspflicht, Haftung des GF) → § 16 GmbHG (Legitimationswirkung, gutgläubiger Erwerb) → § 15 GmbHG (Abtretung Geschäftsanteile) → § 12 HGB i.V.m. FamFG (Handelsregisteranmeldung) → § 57 GmbHG (Anmeldung Kapitalerhöhung)

---

## Skill: `gesellschafterversammlung-einberufen`

_Gesellschafterversammlung für Wandeldarlehensmandat einberufen und Tagesordnung aufstellen. §§ 49 51 GmbHG Ladungspflichten. Prüfraster: Ladungsfrist Form Tagesordnung Quorum Vollmachten Protokollpflicht. Output: Einberufungsschreiben Tagesordnung Vollmachtsformular. Abgrenzung: nicht für spezifi..._

# Gesellschafterversammlung einberufen (Kapitalerhöhung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Gesellschaft: Firma, Sitz, Geschäftsführerin
- Gesellschafterinnen: Namen, Adressen, Anteilsverhältnisse
- Tagesordnung: Kapitalerhöhung gegen Sacheinlage, Bezugsrechtsverzicht, Übernahme Lender, ggf. Satzungsänderung
- Gewünschtes Versammlungsdatum
- Einberufungsform: Einschreiben, E-Mail oder Vollversammlung ohne Einberufung?
- Notar bereits beauftragt?

## Rechtlicher Rahmen

### Primärnormen
- § 49 GmbHG (Gesellschafterversammlung – Einberufungspflicht der Geschäftsführung)
- § 50 GmbHG (Einberufungsrecht Gesellschafter mit mehr als zehn Prozent)
- § 51 GmbHG (Form und Frist: schriftlich, mindestens eine Woche)
- § 51 Abs. 3 GmbHG (Beschlussfassung ohne Einberufung bei Einverständnis aller Gesellschafter)
- § 53 Abs. 2 GmbHG (Satzungsänderungsbeschluss: notarielle Beurkundung, drei Viertel-Mehrheit)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Einberufungsform wählen
Option A – Schnellweg (§ 51 Abs. 3 GmbHG): Alle Gesellschafterinnen stimmen der Versammlung ohne Einberufung zu und verzichten auf die Ladungsfrist. Nur möglich bei einstimmigem Einverständnis. Option B – Reguläre Einberufung (§ 51): Schriftliche Einladung mindestens eine Woche vorher, Tagesordnung beifügen.

### 2. Einladungsschreiben verfassen
Absender: Geschäftsführerin. Empfänger: alle Gesellschafterinnen. Inhalt: Datum, Uhrzeit, Ort (oder Videokonferenz falls Satzung erlaubt), Tagesordnung vollständig. Hinweis: Notarielle Beurkundung des Beschlusses (§ 53 Abs. 2 GmbHG).

### 3. Tagesordnung formulieren
TOP 1: Kapitalerhöhung des Stammkapitals um EUR [Nennbetrag neue Anteile] gegen Einbringung der Forderung aus Wandeldarlehen Northstar Pre-Seed Partners GmbH & Co. KG als Sacheinlage. TOP 2: Verzicht der Altgesellschafterinnen auf Bezugsrechte. TOP 3: Zulassung des Darlehensgebers als neuer Gesellschafter. TOP 4: Änderung der Gesellschafterliste.

### 4. Notartermin koordinieren
Kapitalerhöhungsbeschluss bedarf notarieller Beurkundung (§ 53 Abs. 2 GmbHG). Notar beurkundet Beschluss und Übernahmeerklärung des Lenders (§ 55 Abs. 2 GmbHG). Termin mindestens zwei Wochen im Voraus buchen.

### 5. Versand der Einladung und Dokumentation
Versand per Einschreiben (Zugangsnachweis) oder per E-Mail wenn Satzung erlaubt. Zustellungsnachweis archivieren.

### 6. Vollmacht
Falls eine Gesellschafterin nicht persönlich erscheinen kann: schriftliche Vollmacht erforderlich (§ 47 Abs. 3 GmbHG). Bevollmächtigte müssen Beschlussfähigkeit herstellen.

## Muster-Einladung (Auszug)

```
[Gesellschaft, Datum]

Einladung zur außerordentlichen Gesellschafterversammlung
der Sonnenglas Solartechnologie UG (haftungsbeschränkt)

Datum: [Datum], [Uhrzeit] Uhr
Ort: Notariatskanzlei [Notar], [Adresse]

Tagesordnung:
TOP 1: Kapitalerhöhung gegen Sacheinlage
TOP 2: Bezugsrechtsverzicht Altgesellschafterinnen
TOP 3: Zulassung Northstar Pre-Seed Partners GmbH & Co. KG als Gesellschafter
TOP 4: Aktualisierung Gesellschafterliste

Hinweis: Die Beschlussfassung zu TOP 1 bis 3 erfordert notarielle Beurkundung.

[Unterschrift Geschäftsführerin]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Einberufungsmangel, Gesellschafterin erhebt Einwand | Beschluss anfechtbar | Heilung durch nachträgliche Zustimmung | Ordnungsgemäße Einberufung |
| Notar nicht rechtzeitig beauftragt | Versammlung ohne Beurkundung | Notar in Suche | Notar bestätigt Termin |
| Tagesordnung unvollständig | Beschluss über nicht angekündigten Punkt anfechtbar | Nachträgliche Ergänzung | Vollständige Tagesordnung |
| Quorum nicht erreicht | Beschluss nicht gefasst | Vertretung unklar | Alle Gesellschafterinnen anwesend/vertreten |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 49 ff. aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 51 GmbHG (Einberufung Gesellschafterversammlung, Frist 1 Woche) → § 51 Abs. 3 GmbHG (Vollversammlung mit Zustimmung) → § 53 GmbHG (notarielle Beurkundung, vollständige Beschlussangaben) → § 47 Abs. 1 GmbHG (Stimmrecht, Mehrheitserfordernisse)

---

## Skill: `handelsregisteranmeldung-kapitalerhoehung-kyc`

_Handelsregisteranmeldung nach Kapitalerhohung durch Wandlung vorbereiten. § 57 GmbHG Anmeldepflicht §§ 54 55 GmbHG Kapitalerhohung. Prüfraster: Anmeldungsinhalt Unterlagen Notar Einreichungspflicht Eintragungsvoraussetzungen. Output: Anmeldungsentwurf Unterlagencheckliste. Abgrenzung: nicht für G..._

# Handelsregisteranmeldung Kapitalerhöhung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Vollständiges Notar-Paket (aus `notar-paket-uebermittlung`)
- Zuständiges Amtsgericht / Handelsregister (nach Sitz der Gesellschaft)
- Handelsregisternummer (HRB)
- Beauftragter Notar

## Rechtlicher Rahmen

### Primärnormen
- § 57 GmbHG (Anmeldung der Kapitalerhöhung: durch Geschäftsführerin, notarielle Beglaubigung)
- § 57a GmbHG (Inhalt der Anmeldung: neue Gesellschafterliste, Nachweis Sacheinlage)
- § 9c GmbHG (Prüfung durch das Registergericht – materielle Prüfung)
- § 382 FamFG (Registerverfahren – Bearbeitungsfrist)
- § 19 GwG (Transparenzregister-Anmeldepflicht nach HR-Änderung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Einreichung beim Handelsregister
Der Notar reicht die Anmeldung inklusive aller Anlagen elektronisch über das ERV (Elektronischer Rechtsverkehr) beim zuständigen Amtsgericht ein. Kosten: nach GNotKG (Eintragungsgebühr + Notargebühr).

### 2. Standardunterlagen Anmeldung § 57 GmbHG
a) Beschluss über Kapitalerhöhung (notariell beurkundet)
b) Übernahmeerklärung Lender (notariell beurkundet)
c) Sacheinlagebericht
d) Neue Gesellschafterliste (§ 40 GmbHG)
e) Versicherung der Geschäftsführerin nach § 8 Abs. 3 GmbHG (keine Hindernisse)
f) Anmeldungstext (von Notar vorbereitet, notariell beglaubigt)

### 3. Prüfung durch Registergericht (§ 9c GmbHG)
Registergericht prüft: formelle Voraussetzungen (Beschluss, Beurkundung, Unterlagen), materielle Voraussetzungen (Werthaltigkeit Sacheinlage), Vollständigkeit Gesellschafterliste. Häufige Beanstandungen: fehlende Angaben in Gesellschafterliste, unzureichender Sacheinlagebericht, formelle Mängel im Beschluss.

### 4. Bearbeitungsdauer
Standard: zwei bis acht Wochen. Überlastete Gerichte (z. B. AG Charlottenburg/Berlin): bis zu zwölf Wochen. Beschleunigte Eintragung auf Antrag bei wirtschaftlichem Interesse (§ 381 FamFG).

### 5. Nach Eintragung
Eintragungsbenachrichtigung an alle Parteien. Gesellschafterliste jetzt im elektronischen HR abrufbar. Lender hat volle Gesellschafterrechte (§ 16 GmbHG).

### 6. Transparenzregister-Folge-Meldung (§ 19 GwG)
Unmittelbar nach HR-Eintragung: Prüfung ob Lender wirtschaftlich Berechtigter (mehr als 25 % nach Kapitalerhöhung). Falls ja: Meldung an Transparenzregister (www.transparenzregister.de). Frist: unverzüglich.

## Häufige Beanstandungsgründe und Abhilfen

| Beanstandung | Abhilfe |
|---|---|
| Gesellschafterliste unvollständig (fehlendes Geburtsdatum) | Liste korrigieren und neu einreichen |
| Sacheinlagebericht ohne Werthaltigkeitsbegründung | Ergänzte Fassung nachreichen |
| Übernahmeerklärung ohne notarielle Beurkundung | Erneute Beurkundung erforderlich |
| Beschluss ohne Satzungsänderungstext | Beschluss nachbeurkunden |
| Versicherung Geschäftsführerin fehlt | Nachreich der Versicherung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Registergericht beanstandet Sacheinlagebericht | Verzögerung, Nachbesserung | Eine Beanstandung | Keine Beanstandung |
| Bearbeitungsdauer über zwölf Wochen | Gesellschafterrechte Lender verzögert | Acht bis zwölf Wochen | Unter acht Wochen |
| Transparenzregister vergessen | § 56 GwG-Bußgeld bis EUR 150000 | Frist läuft | Unmittelbar gemeldet |
| Notar-Fehler in Unterlagen | Rücknahme und Neueinreichung | Kleiner Formfehler | Alle Unterlagen korrekt |

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG §§ 57/9c oder FamFG aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 57 GmbHG (Anmeldung Kapitalerhöhung zum Handelsregister) → § 57a GmbHG (vereinfachte Kapitalerhöhung) → § 12 HGB i.V.m. §§ 374 ff. FamFG (elektronische Anmeldung) → § 56 Abs. 2 GmbHG (Sacheinlagebericht) → § 8 HGB (Inhalt Handelsregisteranmeldung)

---

## Skill: `kyc-aml-geldwaesche`

_KYC- und AML-Anforderungen bei Wandeldarlehensmandat prüfen wenn Investor oder Darlehensgeberin auftritt. §§ 10 11 GwG Sorgfaltspflichten. Prüfraster: wirtschaftlich Berechtigter Risikoklasse PEP-Status Herkunft Kapital Dokumentation. Output: KYC-Checkliste Risikoeinschaetzung Dokumentationspaket..._

# KYC / AML / Geldwäscheprävention

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Alle Parteien mit vollständigen Identifikationsdaten (aus `parteien-erfassen`)
- Darlehensbetrag und Herkunft der Mittel (Lender)
- HR-Auszüge, Gesellschafterlisten, Organogramme der beteiligten Unternehmen
- Berufsausübungserlaubnis des Beraters (Rechtsanwalt: Pflicht nach § 2 Abs. 1 Nr. 10 GwG)

## Rechtlicher Rahmen

### Primärnormen
- § 2 Abs. 1 Nr. 10 GwG (Rechtsanwälte als Verpflichtete bei Unternehmenstransaktionen)
- § 3 GwG (Wirtschaftlich Berechtigter – natürliche Person mit mehr als 25 % Anteilen/Stimmrechten)
- §§ 10, 11, 12, 13 GwG (Allgemeine, vereinfachte, verstärkte Sorgfaltspflichten)
- § 19 GwG (Transparenzregister – Abgleich und Unstimmigkeitsmeldung)
- § 43 GwG (Verdachtsmeldepflicht bei Geldwäscheverdacht)
- § 47 GwG (Dokumentationspflicht – fünf Jahre nach Vertragsende)
- Art. 2 VO (EU) 765/2006 (EU-Konsolidierte Sanktionsliste)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Verpflichtetenprüfung
Rechtsanwalt als Berater bei Gründung, Kauf oder Verkauf von Gesellschaftsanteilen: Verpflichteter nach § 2 Abs. 1 Nr. 10 GwG. Allgemeine Sorgfaltspflichten nach § 10 GwG verpflichtend.

### 2. Wirtschaftlich Berechtigte ermitteln
Gesellschaft: Wer hält mehr als 25 % der Anteile direkt oder über eine Kette? Beispiel Sonnenglas: Dr. Schöneck (40 %) und Habersaat (35 %) sind wirtschaftlich Berechtigte. Darlehensgeber (GmbH & Co. KG): Wer sind die Kommanditisten, wer hält mehr als 25 %? Transparenzregister prüfen.

### 3. Transparenzregisterabgleich (§ 19 GwG)
Abruf Transparenzregister für alle beteiligten Gesellschaften. Abgleich mit tatsächlichen Eigentumsverhältnissen. Unstimmigkeit? → Meldepflicht § 23a GwG.

### 4. PEP-Screening
Alle natürlichen Personen prüfen: Amtsträger in herausgehobener Position (§ 1 Abs. 12 GwG; z. B. Regierungsmitglieder, höhere Justizbeamte, Führungskräfte staatlicher Unternehmen)? Familienangehörige und enge Vertraute einbeziehen. Treffer: verstärkte Sorgfalt, GF-Freigabe.

### 5. Sanktionslistenscreening
Listen: EU-Konsolidierte Sanktionsliste (eur-lex.europa.eu), OFAC SDN, UN-Sicherheitsratsliste 1267, HM Treasury Financial Sanctions. Alle Parteien mit vollständigen Namen und ggf. Geburtsdaten screenen. Vorsicht: Namensähnlichkeit ohne Treffer ist kein Treffer – prüfen und dokumentieren.

### 6. Mittelherkunftsnachweis
Darlehensbetrag: Woher stammt das Kapital? Kontoauszüge, Jahresabschluss des Lenders, Herkunftsnachweis. Bei Auffälligkeiten: Verdachtsmeldung § 43 GwG an Financial Intelligence Unit (FIU).

## Checkliste KYC-Dokumentation

| Prüfung | Status |
|---|---|
| Identifikationsdokumente aller natürlichen Personen | [ ] |
| HR-Auszüge aller beteiligten Gesellschaften | [ ] |
| Wirtschaftlich Berechtigte ermittelt und dokumentiert | [ ] |
| Transparenzregister abgeglichen | [ ] |
| PEP-Status geprüft, Ergebnis dokumentiert | [ ] |
| Sanktionslisten geprüft (EU/OFAC/UN/HMT) | [ ] |
| Mittelherkunft plausibilisiert | [ ] |
| Aufbewahrungsfrist fünf Jahre eingerichtet | [ ] |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Sanktionslistentreffer | Vertrag darf nicht abgeschlossen werden | Namensähnlichkeit prüfen | Kein Treffer |
| Mittelherkunft ungeklärt | Verdachtsmeldepflicht § 43 GwG | Teilweise belegt | Vollständig belegt |
| PEP ohne verstärkte Sorgfalt | GwG-Verstoß | PEP-Status in Prüfung | Keine PEP |
| Transparenzregister-Unstimmigkeit | Meldepflicht § 23a GwG | Abweichung erklärbar | Konsistent |

## Quellen und Updates

Stand: 05/2026. GwG in der Fassung 05/2026. Bei Änderung GwG oder EU-Sanktionsregime aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 10, 11 GwG (KYC-Pflichten, Identifizierung wirtschaftlich Berechtigter) → § 43 GwG (Meldepflicht) → § 56 GwG (Bußgeld bei Pflichtverletzung) → § 261 StGB (Geldwäsche n.F.) → Art. 3 EU-Geldwäsche-RL 2018/843 (5. AMLD) → § 42 AO (Steuerlicher Gestaltungsmissbrauch)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

