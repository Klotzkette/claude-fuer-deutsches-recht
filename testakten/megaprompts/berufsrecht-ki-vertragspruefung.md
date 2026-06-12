# Megaprompt: berufsrecht-ki-vertragspruefung

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 93 Skills des Plugins `berufsrecht-ki-vertragspruefung`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Berufsrechts-KI bei Vertragsprüfung: ordnet Rolle (Anwalt/Kanzlei, Mandant, KI-Anbieter…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Berufsrecht KI Vertragspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlage…
3. **cloud-act-und-drittstaat-pruefen** — Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNot…
4. **erforderlichkeit-dokumentieren** — Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der ei…
5. **gutachten-erstellen** — Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte…
6. **interview** — Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname V…
7. **rueckfragebrief-an-anbieter** — Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen …
8. **strafprozessuale-regelung-pruefen** — Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirke…
9. **strafrechtliche-belehrung-pruefen** — Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstl…
10. **tom-und-zertifizierungen-pruefen** — Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Berufsrechts-KI bei Vertragsprüfung: ordnet Rolle (Anwalt/Kanzlei, Mandant, KI-Anbieter), markiert Frist (Rechtzeitige Mandatsannahme), wählt Norm (§ 43a BRAO, § 50 BRAO Aktenführung, DSGVO Art. 28 AVV) und Zuständigkeit (RAK), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Berufsrecht Ki Vertragspruefung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `ai-act-rollen-kanzlei-provider-deployer-api` — AI ACT Rollen Kanzlei Provider Deployer API
- `anbietern-belehrung-sonderfall-edge` — Anbietern Belehrung Sonderfall Edge
- `anbietern-schriftsatz-brief-memo-bausteine` — Anbietern Schriftsatz Brief Memo Bausteine
- `art-50-ki-vo-schriftsatz-marketing-chatbot` — ART 50 KI VO Schriftsatz Marketing Chatbot
- `avv-grenzpruefung-brki-anbieter-eu` — AVV Grenzpruefung Brki Anbieter EU
- `avv-grenzpruefung-datenschutz` — AVV Grenzpruefung Datenschutz
- `belehrung-abschlussprodukt-uebergabe` — Belehrung Abschlussprodukt Uebergabe
- `belehrung-abschlussprodukt-und-uebergabe` — Belehrung Abschlussprodukt und Uebergabe
- `berufsrecht-sonderfall-edge-case` — Berufsrecht Sonderfall Edge Case
- `berufsrecht-sonderfall-und-edge-case` — Berufsrecht Sonderfall und Edge Case
- `berufsrechtliche-bnoto-interessen-brao` — Berufsrechtliche Bnoto Interessen BRAO
- `bnoto-interessen` — Bnoto Interessen
- `bnoto-mehrparteien-konflikt-und-interessen` — Bnoto Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Berufsrecht Ki Vertragspruefung sind § 203 StGB, Consumer, § 43e BRAO,. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Berufsrecht KI Vertragspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Berufsrecht Ki Vertragspruefung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Berufsrecht KI Vertragspruefung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Berufsrechtliche und strafrechtliche Vorprüfung von Verträgen mit privaten Legal-AI-Anbietern. Für Rechtsanwälte Steuerberater Wirtschaftsprüfer Patentanwälte Notare. §§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO § 203 StGB. Maßstab sind Gesetz, Gesetzesmaterialien, verifizierbare Kammerpraxis, Rechtsprechung und aktueller Debattenstand. Gutachten Rückfragebrief Klauselvorschläge.

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
| `avv-grenzpruefung-datenschutz` | Kanzlei nutzt KI-Dienstleister und prüft ob AVV nach Art. 28 DSGVO die berufsrechtliche Prüfung ersetzt. Berufsrecht laeuft parallel und ist strenger als Datenschutzrecht. Normen Art. 28 DSGVO §§ 43e BRAO 62a StBerG.… |
| `berufsrecht-ki-vertragspruefung-kaltstart-interview` | Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus… |
| `cloud-act-und-drittstaat-pruefen` | Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR werden als gleichwertig unterstellt. Drittstaaten benoetigen vergleichbares… |
| `erforderlichkeit-dokumentieren` | Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist nach… |
| `gutachten-erstellen` | Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat… |
| `klauselvorschlaege` | Liefere konkrete Mustertexte für Vertragsklauseln mit dem KI-Anbieter. Bausteine Verschwiegenheit Belehrung §§ 203 204 StGB Subunternehmer no training Zero-Retention EU-Hosting Audit-Recht Löschkonzept Professional… |
| `parallelnormen-andere-berufe` | Norm-Adapter-Referenz für alle fuenf Berufsgeheimnistraeger Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar. Mapping der Dienstleisterregelungen Verschwiegenheitspflichten und § 203 StGB-Tatbestaende.… |
| `rueckfragebrief-an-anbieter` | Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und… |
| `strafprozessuale-regelung-pruefen` | Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei… |
| `strafrechtliche-belehrung-pruefen` | Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB.… |
| `subunternehmer-regelung-pruefen` | Prüfe die Subunternehmerklausel im KI-Anbietervertrag. Norm Absatz drei Satz zwei Nummer drei der einschlaegigen Dienstleisterregelung. Pflichtinhalte Zustimmungsvorbehalt der Kanzlei Subunternehmerliste… |
| `tom-und-zertifizierungen-pruefen` | Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für… |
| `verschwiegenheitsklausel-pruefen` | Prüfe die vertragliche Verpflichtung des Dienstleisters auf Verschwiegenheit nach Absatz drei der einschlaegigen Dienstleisterregelung (§§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO). Anforderungen Textform (§ 126b… |

## Worum geht es?

Dieses Plugin unterstuetzt Anwälte, Steuerberater, Wirtschaftsprüfer, Patentanwälte und Notare bei der berufsrechtlichen und strafrechtlichen Pruefung von Verträgen mit privaten Legal-AI-Anbietern. Der Einsatz von KI-Diensten in Kanzleien unterliegt strengen berufsrechtlichen Vorgaben, insbesondere den Verschwiegenheitspflichten und den gesetzlichen Dienstleister-Regelungen der jeweiligen Berufsordnung.

Kernproblem ist das Spannungsfeld zwischen dem Wunsch nach KI-Effizienzgewinnen und der Pflicht, Mandatsdaten vor unberechtigtem Zugriff zu schuetzen. § 203 StGB stellt die unbefugte Offenbarung von Berufsgeheimnissen unter Strafe; die berufsrechtlichen Normen verpflichten Kanzleien, Dienstleister explizit zu belehren und vertraglich auf Verschwiegenheit zu verpflichten.

## Wann brauchen Sie diese Skill?

- Sie prufen erstmals einen Vertrag mit einem KI-Anbieter und benoetigen einen strukturierten Pruefrahmen für Ihren Berufsstand.
- Ein KI-Dienstleister hat seinen Server in den USA und Sie wollen pruefen, ob der US CLOUD Act oder FISA ein Risiko darstellt.
- Sie moechten einen Rueckfragebrief an den Anbieter schreiben, um fehlende Vertragsklauseln zu Verschwiegenheit, Subunternehmern und Datenloeschung nachzufordern.
- Sie sollen ein zusammenfassendes Gutachten für die Kanzleifuehrung erstellen, bevor ein KI-Tool eingefuehrt wird.
- Ihr Kanzleiteam nutzt bereits ein KI-Tool und Sie wollen rueckwirkend pruefen, ob alle berufsrechtlichen Anforderungen erfuellt sind.

## Fachbegriffe (kurz erklaert)

- **§ 203 StGB** — Strafvorschrift zum Schutz von Privatgeheimnissen; erfasst Berufsgeheimnisraeger wie Anwälte, Aerzte und Steuerberater.
- **Dienstleister-Regelung** — Berufsgruppenspezifische Norm (z. B. § 43e BRAO), die Kanzleien verpflichtet, KI-Anbieter auf Verschwiegenheit zu verpflichten und zu belehren.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; laeuft parallel zur berufsrechtlichen Pruefung, ersetzt diese aber nicht.
- **No-Training-Klausel** — Vertragliche Zusage des Anbieters, Mandatsdaten nicht zum Trainieren von KI-Modellen zu verwenden.
- **Zero-Retention** — Zusage, Daten nicht dauerhaft zu speichern; relevant für Loeschkonzept und Audit-Rechte.
- **Cloud Act** — US-amerikanisches Gesetz, das US-Behörden Zugriff auf bei US-Unternehmen gespeicherte Daten ermoeglichen kann, auch wenn Server in der EU stehen.
- **BSI C5** — Cloud Computing Compliance Criteria Catalogue des Bundesamts für Sicherheit in der Informationstechnik; anerkannter Pruefstandard.
- **Norm-Adapter** — Mechanismus im Plugin, der je nach Berufsstand (BRAO, StBerG, WPO, PAO, BNotO) die einschlaegige Dienstleisterregelung auswaehlt.

## Rechtsgrundlagen

- § 43e BRAO — Rechtsanwalt: Inanspruchnahme von Dienstleistern
- § 62a StBerG — Steuerberater: Inanspruchnahme von Dienstleistern
- § 50a WPO — Wirtschaftsprüfer: Inanspruchnahme von Dienstleistern
- § 39c PAO — Patentanwalt: Inanspruchnahme von Dienstleistern
- § 26a BNotO — Notar: Inanspruchnahme von Dienstleistern
- § 203 Abs. 1 Abs. 3 Abs. 4 und Abs. 6 StGB — Verletzung von Privatgeheimnissen
- § 204 StGB — Verwertung fremder Geheimnisse
- Art. 28 DSGVO — Auftragsverarbeitung
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen
- §§ 53a 97 StPO — Zeugnisverweigerungsrecht und Beschlagnahmeverbot

## Schritt-für-Schritt: Einstieg ins Plugin

1. Berufsstand und Anbieter im Kaltstart-Interview erfassen; Norm-Adapter bestimmen.
2. Erforderlichkeit der Offenlegung von Mandatsdaten pruefen und dokumentieren.
3. Verschwiegenheitsklausel im Vertrag lokalisieren und bewerten.
4. Subunternehmer-Regelung, strafrechtliche Belehrung und TOM pruefen.
5. Drittstaat-Risiko (US CLOUD Act, Nicht-EU-Hosting) einschaetzen; ggf. Rueckfragebrief versenden und Gutachten erstellen.

## Skill-Tour (was gibt es hier?)

- `avv-grenzpruefung-datenschutz` — Pruefen ob AVV nach Art. 28 DSGVO die berufsrechtliche Pruefung ersetzt (tut er nicht).
- `berufsrecht-ki-vertragspruefung-kaltstart-interview` — Berufsstand, Anbieter, Vertragsdokument und Normen erfassen; Norm-Adapter aktivieren.
- `cloud-act-und-drittstaat-pruefen` — Auslandsbezug und Drittstaatrisiko (US CLOUD Act, FISA) pruefen; Professional Secrecy Addendum empfehlen.
- `erforderlichkeit-dokumentieren` — Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenueber dem KI-Dienstleister pruefen und dokumentieren.
- `gutachten-erstellen` — Zusammenfassendes Berufsrechts-Gutachten zum KI-Anbietervertrag erstellen.
- `klauselvorschlaege` — Mustertexte für Vertragsklauseln zu Verschwiegenheit, No-Training, Zero-Retention und Subunternehmern liefern.
- `parallelnormen-andere-berufe` — Norm-Adapter-Referenz für alle fuenf Berufsgeheimnistraeger mit Mapping der Dienstleisterregelungen.
- `rueckfragebrief-an-anbieter` — Strukturierten Rueckfragebrief an den KI-Anbieter zu offenen berufsrechtlichen Punkten erstellen.
- `strafprozessuale-regelung-pruefen` — Strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO pruefen.
- `strafrechtliche-belehrung-pruefen` — Belehrung des Dienstleisters ueber § 203 StGB im Vertrag pruefen.
- `subunternehmer-regelung-pruefen` — Subunternehmerklausel auf Zustimmungsvorbehalt, Weiterverpflichtung und Belehrung pruefen.
- `tom-und-zertifizierungen-pruefen` — TOM und Zertifizierungen des Anbieters (ISO 27001, BSI C5, SOC 2) pruefen.
- `verschwiegenheitsklausel-pruefen` — Vertragliche Verpflichtung des Dienstleisters auf Verschwiegenheit lokalisieren und bewerten.

## Worauf besonders achten

- **Berufsrecht und Datenschutzrecht laufen parallel**: Ein vorhandener AVV erfuellt nicht automatisch die berufsrechtlichen Anforderungen nach § 43e BRAO und den Parallelvorschriften.
- **Textformerfordernis**: Die Verschwiegenheitspflicht muss nach § 43e Abs. 3 BRAO in Textform (§ 126b BGB) vereinbart werden; muendliche Zusagen genuegen nicht.
- **Subunternehmer oft uebersehen**: Viele KI-Anbieter nutzen Sprachmodelle grosser US-Konzerne als Subunternehmer; diese muessen ebenfalls verpflichtet werden.
- **Drittstaatrisiko eigenstaendig bewerten**: EU-Sitz des Anbieters genuegt nicht, wenn Muttergesellschaft in den USA dem Cloud Act unterliegt.
- **Strafrechtliche Konsequenzen**: Ein Verstoss gegen § 203 StGB ist eine Straftat, keine Ordnungswidrigkeit.

## Typische Fehler

- Nur den AVV pruefen und berufsrechtliche Parallelvorschriften uebersehen.
- Subunternehmerliste nicht anfordern; Anbieter setzt grosse Sprachmodelle ein, ohne dies offenzulegen.
- Vertrag ohne No-Training-Zusage annehmen; Mandatsdaten koennen in KI-Training einfliessen.
- Erforderlichkeit der Datenweitergabe nicht dokumentieren; interner Compliance-Vermerk fehlt.
- US-Anbieter mit EU-Rechenzentrum als unbedenklich eingestuft, ohne Cloud-Act-Analyse.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
- aktueller berufsrechtlicher Debattenstand zur Einordnung von KI-Tools
- BRAK-Hinweise 12/2024

---

## Skill: `cloud-act-und-drittstaat-pruefen`

_Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional S..._

# Cloud Act und Drittstaat prüfen

## Fachkern: Cloud Act und Drittstaat prüfen

- **KI-/Berufsrechtsproblem (Cloud Act und Drittstaat prüfen):** Prüfe Auslandsbezug des KI-Anbieters nach Absatz vier der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). EU/EWR sind regelmäßig leichter vertretbar; Drittstaaten benötigen eine eigene Berufsgeheimnisprüfung. US-CLOUD Act, FISA, Supportzugriffe, EU-US-DPF, SCC und Professional Secrecy Addendum sauber trennen.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Absatz 4 der jeweiligen Dienstleisterregelung. Wortlaut (am Beispiel § 43e Abs. 4 BRAO; identisch in § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO, § 39c Abs. 4 PAO; bei § 26a BNotO entsprechend):

"Bei der Inanspruchnahme von Dienstleistungen, die im Ausland erbracht werden, darf der Rechtsanwalt dem Dienstleister den Zugang zu fremden Geheimnissen unbeschadet der übrigen Voraussetzungen dieser Vorschrift nur dann eröffnen, wenn der dort bestehende Schutz der Geheimnisse dem Schutz im Inland vergleichbar ist, es sei denn, dass der Schutz der Geheimnisse dies nicht gebietet."

## Berufsrechtliche Auslegungslinie

EU-/EWR-Konstellationen sind wegen gemeinsamer Datenschutz- und Berufsrechtsnähe regelmäßig leichter vertretbar. Außerhalb der EU/des EWR ist die Vergleichbarkeit des Geheimnisschutzes einzelfallabhängig zu prüfen.

Wichtig: Die Vergleichbarkeit bezieht sich auf den Schutz der Geheimnisse, nicht auf das allgemeine Rechtsschutzniveau. Selbst wenn ein Land eine funktionierende Justiz hat, kann der Schutz von Berufsgeheimnissen mangelhaft sein.

## Problemzone USA

Die USA stellen die größte praktische Herausforderung dar, weil die meisten KI-Anbieter dort ansässig sind oder dort verarbeiten lassen.

### CLOUD Act (2018)

Der US-Clarifying Lawful Overseas Use of Data Act verpflichtet US-Anbieter und ihre weltweiten Töchter, US-Behörden auf Anordnung Zugang zu Daten zu gewähren, auch wenn diese außerhalb der USA gespeichert sind. Eine deutsche Hostinglokation schützt also nicht.

### FISA Section 702

FISA Section 702 kann unter bestimmten Voraussetzungen Zugriffe auf elektronische Kommunikation von Nicht-US-Personen über US-Dienste ermöglichen. Für die Kanzlei genügt deshalb nicht die Frage "Wo steht der Server?", sondern es sind Konzern-, Support-, Administrations- und Herausgabezugriffe mitzudenken.

### Konsequenz

Bei US-Anbietern kann ein struktureller Restzugriff durch US-Behörden bestehen, der mit dem deutschen Berufsgeheimnis kollidieren kann. Daraus folgt nicht automatisch ein Totalverbot; erforderlich sind aber eine sorgfältige Abwägung, Datenminimierung, Vertragszusätze und dokumentierte Restrisikoentscheidung.

## Professional Secrecy Addendum

Bei US-Anbietern empfehlenswert: ein eigenes Berufsgeheimnis-Addendum zum Hauptvertrag, das

- die berufsrechtlichen Anforderungen explizit übernimmt
- den Anbieter zur Anfechtung jedes US-Auskunftsverlangens verpflichtet
- den Anbieter zur unverzüglichen Information der Kanzlei verpflichtet, soweit gesetzlich zulässig
- den Anbieter zur Datenminimierung in Richtung USA verpflichtet (keine US-Backups, keine US-Logs)
- Gerichtsstand und anwendbares Recht in Deutschland

Ob ein Anbieter solche Zusätze akzeptiert, muss am konkreten Vertragsstand live geprüft werden. Keine Produktbehauptung aus Modellwissen übernehmen.

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Punkt | Status | Ampel | Bemerkung |
|---|---|---|---|
| Sitz Anbieter (Hauptvertragspartei) | | | |
| Konzernzugehörigkeit (US-Konzern?) | | | |
| Verarbeitungsstandort | | | |
| Backup-Standort | | | |
| Modellanbieter (etwa OpenAI) Standort | | | |
| Hoster Standort | | | |
| CLOUD-Act-Anwendbarkeit | | | |
| FISA-Anwendbarkeit | | | |
| Professional Secrecy Addendum | | | |
| Gerichtsstand Deutschland | | | |
| Anwendbares deutsches Recht | | | |
| Standardvertragsklauseln (SCC) | | | |
| Adequacy decision (EU-US-DPF) | | | |

## EU-US-Data Privacy Framework

Das 2023 in Kraft getretene Data Privacy Framework regelt den datenschutzrechtlichen Datentransfer in die USA. **Es regelt nicht das Berufsgeheimnis.** Es schützt nicht vor CLOUD-Act-Zugriffen. Der DPF ist datenschutzrechtlich relevant, berufsrechtlich nur als Indiz für ein gewisses Schutzniveau, nicht als Genehmigung.

## Empfehlungen

- Bei EU/EWR-Anbietern: Auslandsbezug grundsätzlich unproblematisch
- Bei US-Anbietern: Professional Secrecy Addendum, EU-Hosting-Zusicherung, kein US-Backup
- Bei Anbietern aus sonstigen Drittstaaten (China, Indien): in der Regel rote Ampel — Vergleichbarkeit muss positiv nachgewiesen werden

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 44–49 DSGVO — Drittlandsübermittlung, SCC, Adequacy Decisions, CBPR
- Art. 46 Abs. 2 lit. c DSGVO — Standardvertragsklauseln als geeignete Garantien
- § 43e Abs. 4 BRAO, § 62a Abs. 4 StBerG, § 50a Abs. 4 WPO — Drittstaat-Klausel Berufsrecht
- US CLOUD Act 2018, 18 U.S.C. § 2713 — Zugriff auf Daten unabhängig vom Speicherort
- FISA Section 702, 50 U.S.C. § 1881a — Überwachung elektronischer Kommunikation von Nicht-US-Personen

## Triage-Frage (Entscheidungsbaum)

```
Anbieter Sitz EU/EWR?
 Ja → Auslandsbezug unproblematisch (DAV S. 15)
 Nein → US-Konzern oder US-Tochter?
 Ja → CLOUD Act anwendbar → Professional Secrecy Addendum erforderlich
 EU-Hosting-Zusicherung vorhanden?
 Ja → gelbe Ampel (struktureller Restzugriff bleibt)
 Nein → rote Ampel
 Nein → Sonstiges Drittland (CN, IN, RU)?
 → Vergleichbarkeitsnachweis positiv erforderlich → i.d.R. rote Ampel
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — US-Anbieter in Kanzleiinfrastruktur pruefen | Cloud-Act-Risikobewertung nach Schema unten |
| Variante A — kein US-Bezug erkennbar | Drittstaat-Kapitel trotzdem pruefen (UK TIOPA, CN DSL) |
| Variante B — Mandant will trotz Risiko US-Anbieter nutzen | Risikohinweis dokumentieren; Mandant schriftlich bestaetigen lassen |
| Variante C — staatliche Ermittlung laeuft bereits | Sofortiger Wechsel; Datensicherung und Incident-Response pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Drittstaat-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Drittstaat-Prüfvermerk [DATUM]
Anbieter: [NAME, LAND]
Konzernstruktur: [US-Konzern ja/nein; Mutter: NAME]

A) DSGVO-Drittlandsübermittlung (Art. 44 DSGVO)
Adequacy Decision: [ja/nein; EU-US-DPF ja/nein]
SCC vorhanden: [ja/nein; Datum]
TIA (Transfer Impact Assessment) durchgefuehrt: [ja/nein]

B) Berufsrechtlicher Drittstaat-Check (§ 43e Abs. 4 BRAO)
Vergleichbarkeit Schutzniveau: [ja/eingeschraenkt/nein]
CLOUD-Act-Risiko: [ja/nein/unklar]
Professional Secrecy Addendum: [vorhanden/nicht vorhanden/beantragt]

C) Ampel
DSGVO-Transfer: GRUEN / GELB / ROT
Berufsrecht Drittstaat: GRUEN / GELB / ROT
Empfehlung: [Nutzung freigegeben / Addendum erforderlich / Anbieterwechsel]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Skill: `erforderlichkeit-dokumentieren`

_Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist der Zweck der konkreten Offenlegung, nicht die abstrakte KI-Strategie der Kanzlei. Erstelle einen..._

# Erforderlichkeit dokumentieren

## Fachkern: Erforderlichkeit dokumentieren

- **KI-/Berufsrechtsproblem (Erforderlichkeit dokumentieren):** Prüfe die Erforderlichkeit der Offenlegung von Berufsgeheimnissen gegenüber dem KI-Dienstleister nach Absatz eins der einschlaegigen Dienstleisterregelung (BRAO StBerG WPO PAO BNotO). Bezugspunkt ist der Zweck der konkreten Offenlegung, nicht die abstrakte KI-Strategie der Kanzlei. Erstelle einen internen Compliance-Vermerk mit Beurteilungsspielraum und Grenzen.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Pro Beruf wird auf Absatz 1 der jeweiligen Dienstleisterregelung verwiesen. Diese Vorschriften sind nahezu wortgleich:

- § 43e Abs. 1 BRAO: Der Rechtsanwalt darf Dienstleistern den Zugang zu Tatsachen eröffnen, auf die sich die Verpflichtung zur Verschwiegenheit gemäß § 43a Abs. 2 BRAO bezieht, soweit dies für die Inanspruchnahme der Dienstleistung erforderlich ist.
- § 62a Abs. 1 StBerG — wortgleich für Steuerberater bezogen auf § 57 Abs. 1 StBerG.
- § 50a Abs. 1 WPO — wortgleich für Wirtschaftsprüfer.
- § 39c Abs. 1 PAO — wortgleich für Patentanwalt bezogen auf § 39a Abs. 2 Satz 1 PAO.
- § 26a Abs. 1 BNotO — wortgleich für Notar bezogen auf § 18 BNotO. Beim Notar wird ausdrücklich klargestellt, dass die Eröffnung "ohne Einwilligung der Beteiligten" zulässig ist (Abs. 1 Satz 1).

## Bezugspunkt der Erforderlichkeit

Maßgeblich ist nicht, ob die Kanzlei KI braucht — diese unternehmerische Entscheidung wird vorausgesetzt. Maßgeblich ist, ob die konkrete Offenlegung der Mandatsdaten gegenüber dem konkreten Dienstleister für den konkreten Zweck erforderlich ist. Der Beurteilungsspielraum der Kanzlei ist nicht grenzenlos, aber praktisch relevant.

Praktisch heißt das: Wer ein Tool zur Vertragsanalyse einsetzt, muss nicht begründen, warum er überhaupt KI nutzt. Er muss begründen, warum die Offenlegung der Mandatsdaten gegenüber genau diesem Anbieter zur Erfüllung dieses Zwecks erforderlich ist.

## Erforderlich ≠ unerlässlich

Erforderlichkeit verlangt nicht, dass das Tool der einzig denkbare Weg ist. Es darf eine sinnvolle, fachlich gerechtfertigte Wahl sein. Die Kanzlei darf zwischen verschiedenen Anbietern abwägen — Preis, Funktionsumfang, Sicherheit. Diese Abwägung ist Teil der Berufsausübungsfreiheit, muss bei Mandatsgeheimnissen aber dokumentierbar bleiben.

## Grenzen

Bei zwei Konstellationen verlässt der Vorgang den Bereich des nach Abs. 1 Erforderlichen:

1. **KI-Training mit Mandatsdaten** — Die Übermittlung von Mandatsdaten zu allgemeinen Trainings- oder Modellverbesserungszwecken überschreitet regelmäßig den beauftragten Dienstleistungszweck. Hier muss vertraglich "no training" zugesichert sein.
2. **Datenmengen weit jenseits des Zwecks** — Wird das Tool nur für Recherche eingesetzt, müssen nicht alle Aktenbestandteile hochgeladen werden.

## Prüfpunkte am Vertrag

- Beschreibt der Vertrag den Verarbeitungszweck präzise?
- Ist der Zweck mit dem konkret geplanten Einsatz konsistent?
- Werden Daten erkennbar über den Zweck hinaus verarbeitet (Training, Statistik, Modellverbesserung)?
- Gibt es Zweckbindungsklauseln im Vertrag?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Sonderfall Notar

Bei Dienstleistungen, die unmittelbar einem einzelnen Amtsgeschäft dienen (§ 26a Abs. 4 BNotO), ist die Einwilligung des Beteiligten erforderlich. Die Erforderlichkeit nach Abs. 1 bleibt davon unberührt, tritt aber neben das Einwilligungserfordernis.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 43e Abs. 1 BRAO, § 62a Abs. 1 StBerG, § 50a Abs. 1 WPO, § 39c Abs. 1 PAO, § 26a Abs. 1 BNotO — Erforderlichkeitsschwelle Berufsrecht
- Art. 5 Abs. 1 lit. c DSGVO — Datenminimierung (entsprechender Grundsatz)
- Art. 6 Abs. 1 DSGVO — Zulässigkeit der Verarbeitung

## Schritt-für-Schritt-Workflow

1. **Einsatzzweck konkret benennen:** Was soll das Tool leisten? (Vertragsanalyse, Recherche, Schriftsatzentwurf, Dokumentenprüfung)
2. **Datenkategorien inventarisieren:** Welche Daten werden tatsächlich eingegeben? Mandatsschriftsätze? Urkunden? Bilanzen?
3. **Minimierungsprüfung:** Können Mandantendaten vor Eingabe anonymisiert oder pseudonymisiert werden, ohne Zweck zu verfehlen?
4. **Training-Prüfung:** Vertrag auf "no training"-Klausel prüfen (§ 5 AVV oder dedizierte Klausel). Falls fehlt → rote Ampel Training.
5. **Alternativen abwägen:** Gibt es EU-Anbieter ohne Drittlandrisiko? Ist der Vorteil des gewählten Anbieters sachlich gerechtfertigt?
6. **Vermerk schreiben:** Interne Dokumentation für Kanzleiunterlagen (Beweissicherung im berufsrechtlichen Verfahren).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Erforderlichkeit einer Verarbeitung dokumentieren | Zwei-Stufen-Pruefung nach Art. 5 Abs. 1 lit. c DSGVO; Template unten |
| Variante A — Verarbeitung klar nicht erforderlich | Stoppen empfehlen; Alternative vorschlagen |
| Variante B — Grenzfall mit starkem Interesse | Interessenabwaegung vertiefen; ausfuehrlichere Dokumentation |
| Variante C — besondere Kategorie (Art. 9 DSGVO) | Erhoehter Massstab; gesonderte Rechtsgrundlage noetig |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Compliance-Vermerk Erforderlichkeit

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Interner Compliance-Vermerk Erforderlichkeit
Datum: [DATUM] | Verfasser: [SACHBEARBEITER]
Anbieter: [NAME] | Produkt: [PRODUKT]
Norm-Basis: § [NORM] [GESETZ] Abs. 1

1. Einsatzzweck
[BESCHREIBUNG DES KONKRETEN EINSATZZWECKS]

2. Daten die eingegeben werden
[AUFLISTUNG DER DATENKATEGORIEN]

3. Begruendung Erforderlichkeit
[WARUM IST DIESE OFFENLEGUNG ERFORDERLICH]

4. Alternativen geprueft
[ALTERNATIVE ANBIETER ODER METHODEN; WARUM ABGELEHNT]

5. Training-Klausel
Vertrag Abschnitt [X]: "no training" zugesichert: ja / nein / Luecke
Falls Luecke: Handlungsbedarf [...]

6. Ampel
Erforderlichkeit: GRUEN / GELB / ROT
Begruendung: [...]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Skill: `gutachten-erstellen`

_Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern..._

# Vorprüfungs-Gutachten erstellen

## Fachkern: Vorprüfungs-Gutachten erstellen

- **KI-/Berufsrechtsproblem (Vorprüfungs-Gutachten erstellen):** Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern strukturierte Argumentationshilfe für das Anbietergespräch.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Dienstleisterregelungen der freien Berufe, Auftragsverarbeitung und technische Geheimnisschutzrealität.
- **Entscheidende Weiche:** Mustertext, Anbieterbehauptung, technische Wirklichkeit, Berufsgeheimnis und Datenschutzrolle müssen getrennt bleiben.
- **Arbeitsprodukt:** Vertragsbaustein, Gutachtenstruktur, Redline oder Anbieter-Fragenliste; Ergebnis bleibt Vorprüfung und wird nicht als fertige Berufsrechtsfreigabe ausgegeben.

## Aufbau

### 1. Eingangsdaten

Aus `berufsrecht-ki-vertragspruefung-kaltstart-interview`. Beruf, Anbieter, Produkt, Datenarten, Vertragstyp, Anlagen.

### 2. Norm-Adapter

Aus `parallelnormen-andere-berufe`. Tabelle der einschlägigen Normen. Hinweis auf § 203 StGB als Klammer.

### 3. Maßstab

Maßstab sind zuerst die geltenden Normen und ihre Gesetzesmaterialien. Berufsrechtliche Stellungnahmen, Kammerhinweise und Fachdebatten werden nur als Auslegungshilfe verarbeitet und in ihrer Bindungswirkung kenntlich gemacht.

### 4. Einzelne Prüfpunkte

Pro Skill ein Abschnitt:

- **Erforderlichkeit** (`erforderlichkeit-dokumentieren`)
- **Verschwiegenheitsklausel** (`verschwiegenheitsklausel-pruefen`)
- **Strafrechtliche Belehrung** (`strafrechtliche-belehrung-pruefen`)
- **Subunternehmer-Regelung** (`subunternehmer-regelung-pruefen`)
- **Strafprozessuale Regelung** (`strafprozessuale-regelung-pruefen`)
- **TOM und Zertifizierungen** (`tom-und-zertifizierungen-pruefen`)
- **Cloud Act und Drittstaat** (`cloud-act-und-drittstaat-pruefen`)
- **AVV-Grenzprüfung Datenschutz** (`avv-grenzpruefung-datenschutz`) — als Schnittstelle

Jeder Abschnitt enthält:

- die einschlägige Norm
- die vertretbare Auslegungslinie und Gegenpositionen
- die konkrete Bewertung am vorgelegten Vertrag (Ampel grün/gelb/rot)
- Lücken und offene Punkte

### 5. Gesamtampel

| Bereich | Ampel | Bemerkung |
|---|---|---|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel | | |
| Strafrechtliche Belehrung | | |
| Subunternehmer | | |
| Strafprozessuale Absicherung | | |
| TOM und Zertifizierungen | | |
| Drittstaat | | |
| AVV (Schnittstelle) | | |

### 6. Handlungsempfehlung

Drei Stufen:

- **Annehmbar** (alles grün, gelbe Punkte dokumentieren) — Vertrag nutzbar nach Annahme
- **Nachverhandelbar** (überwiegend grün/gelb, klare rote Punkte) — Rückfragebrief und Klauselvorschläge versenden
- **Nicht annehmbar** (mehrere rote Punkte, strukturelle Probleme) — Anbieterwechsel oder grundlegende Vertragsneuverhandlung

### 7. Anlagen

- Tabellarische Bewertung pro Prüfpunkt
- Lückenliste (priorisiert)
- Verweise auf Rückfragebrief und Klauselvorschläge

## Schlussklausel im Gutachten

Am Ende jedes Gutachtens steht:

> Dieses Vorprüfungs-Gutachten ist keine Rechtsberatung. Es ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der nutzenden Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten. Quellenbasis: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.

## Stil

- Sachlich, kurz
- Tabellen wo möglich
- Keine Marketing-Sprache
- Disclaimer am Anfang und am Ende
- Bezeichne Anbieterversprechen klar als "Aussage Anbieter, noch nicht im Vertrag" oder "im Vertrag (Fundstelle)"

## Output-Format

Markdown, ca. 5 bis 10 Seiten. PDF-Export optional via Plugin `office`.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 43a Abs. 2, 43e BRAO; §§ 57, 62a StBerG; §§ 43, 50a WPO; §§ 39a, 39c PAO; §§ 18, 26a BNotO
- §§ 203, 204 StGB — Straftatbestände
- §§ 53a, 97 StPO — Strafprozessuale Absicherung
- Art. 28, 32 DSGVO — Datenschutzrechtliche Parallelprüfung

## Triage zu Beginn

1. Wurden alle Einzelprüfungen aus den Teilskills (Verschwiegenheit, Belehrung, Subunternehmer, Strafprozess, TOM, Drittstaat) durchgeführt?
2. Liegen alle Vertragsdokumente vor (Hauptvertrag, AGB, AVV, Subunternehmerliste, TOM-Anlage)?
3. Sind offene Punkte aus dem Rückfragebrief beantwortet?
4. Welches Ergebnis soll das Gutachten haben (Freigabe / Nachverhandlung / Ablehnung)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — datenschutzrechtliches Gutachten erstellen | Vollgutachten-Format nach Template unten |
| Variante A — nur kurze Stellungnahme noetig | Kurzgutachten-Format; Normenkette komprimieren |
| Variante B — politisch heikle Einschaetzung für Mandanten | Ergebnis-offen formulieren; Risiken deutlich benennen |
| Variante C — internes Compliance-Memo ohne externe Wirkung | Schlankeres Format; auf Vollzitierung teilweise verzichten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Vorprüfungs-Gutachten (Auszug)

**Adressat:** Kanzlei intern (ggf. auszugsweise für Anbieter) — Tonfall: sachlich-juristisch

```
Vorpruefungs-Gutachten KI-Anbietervertrag
Datum: [DATUM] | Verfasser: [SACHBEARBEITER]
Anbieter: [NAME] | Produkt: [PRODUKT]
Beruf: [BERUF] | Norm-Adapter: § [NORM]

I. Eingangsdaten
[Aus Kaltstart-Interview]

II. Normrahmen
Berufsrecht: § [NORM] [GESETZ]
Strafrecht: §§ 203, 204 StGB
Datenschutz: Art. 28, 32 DSGVO
Strafprozess: §§ 53a, 97 StPO

III. Einzelprüfungen (Ampeltabelle)
| Pruefpunkt | Ampel | Begruendung |
|-------------------------|-------|-------------|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel| | |
| Belehrung §§ 203/204 | | |
| Subunternehmer | | |
| Strafprozess §§ 53a/97 | | |
| TOM / Zertifizierungen | | |
| Drittstaat / CLOUD Act | | |
| AVV Art. 28 DSGVO | | |

IV. Gesamtergebnis
[GRUEN / GELB / ROT]

V. Handlungsempfehlung
[Annehmbar / Nachverhandelbar / Nicht annehmbar]
[Konkrete naechste Schritte]

VI. Disclaimer
Dieses Vorpruefungs-Gutachten ist keine Rechtsberatung. Es ist strukturierte
Argumentationshilfe. Abschließende Beurteilung bleibt der nutzenden Kanzlei
beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.
Quellen: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Skill: `interview`

_Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (BRAO StBerG WPO PAO BNotO) und entscheide ob Kanzleiinfrastr..._

# Kaltstart-Interview

## Fachkern: Kaltstart-Interview

- **KI-/Berufsrechtsproblem (Kaltstart-Interview):** Erfasse Beruf des Auftraggebers (Rechtsanwalt Steuerberater Wirtschaftsprüfer Patentanwalt Notar) Anbieter Produktname Vertragsdokument Datenarten Verarbeitungszweck Hostingland und Subunternehmerstruktur. Bilde daraus den Norm-Adapter (BRAO StBerG WPO PAO BNotO) und entscheide ob Kanzleiinfrastruktur oder Einzelmandats-Tool im Sinne Absatz fuenf vorliegt. Lade dazu die Skill parallelnormen-andere-berufe.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Pflichtfragen

### Beruf des Auftraggebers

Welche Berufsgruppe nutzt das Tool?

- Rechtsanwalt — Norm: § 43e BRAO i.V.m. § 43a Abs. 2 BRAO und § 203 Abs. 1 Nr. 3 StGB
- Steuerberater oder Steuerbevollmächtigter — Norm: § 62a StBerG i.V.m. § 57 Abs. 1 StBerG und § 203 Abs. 1 Nr. 3 StGB
- Wirtschaftsprüfer oder vereidigter Buchprüfer — Norm: § 50a WPO i.V.m. § 43 WPO und § 203 Abs. 1 Nr. 3 StGB (bei Wirtschaftsprüfungsgesellschaft zusätzlich § 59c WPO)
- Patentanwalt — Norm: § 39c PAO i.V.m. § 39a Abs. 2 PAO und § 203 Abs. 1 Nr. 3 StGB
- Notar — Norm: § 26a BNotO i.V.m. § 18 BNotO und § 203 Abs. 1 Nr. 1 StGB

Sind mehrere Berufsgruppen in einer Sozietät gemischt vertreten (Anwalts-Steuerberater-Gesellschaft, multidisziplinäre Praxis), gelten die strengsten Anforderungen kumulativ. Beim Notar besonders auf § 26a Abs. 4 BNotO achten — bei Dienstleistungen für ein einzelnes Amtsgeschäft ist die Einwilligung des Beteiligten erforderlich.

### Anbieter und Produkt

- Firmenname und Sitz des Anbieters (juristische Person, vertretungsberechtigte Personen)
- Produktname und Versionsstand (Bsp.: gängige KI-Sprachmodelle und KI-Frontends; eigene Marken-Frontends)
- Eigene KI-Modelle oder API-Aufruf an Drittanbieter (z.B. Microsoft Azure, AWS Bedrock)
- Welche Subunternehmer sind vorgesehen (Hyperscaler, Modellanbieter, Hosting)?

### Datenarten und Verarbeitungszweck

- Welche Datenkategorien werden eingegeben (Mandatsschriftsätze, Vertragsentwürfe, Personalakten, Bilanzdaten, Notariatsurkunden, Patentanmeldungen)?
- Werden besondere Kategorien personenbezogener Daten verarbeitet (Art. 9 DS-GVO)?
- Geht es um Kanzleiinfrastruktur (übergreifend) oder ein Tool, das einem konkreten Mandat dient (Abs. 5 der Dienstleisterregelung)?
- Wer im Haus hat Zugriff?

### Hostingland und Auslandsbezug

- Wo liegen die Server (EU/EWR, USA, sonstiges Drittland)?
- Wo sitzt der Modellanbieter selbst (etwa OpenAI in den USA)?
- Greift der US-CLOUD Act (US-Konzern oder US-Tochter)?

### Vertragsstand

- Liegt ein eigenständiger Vertrag vor, oder nur AGB plus Datenschutzanhang?
- Wann wurde der Vertrag zuletzt geändert?
- Wer hat unterzeichnet?
- Liegt eine Auftragsverarbeitungsvereinbarung nach Art. 28 DS-GVO bei?

## Heuristik Kanzleiinfrastruktur vs. Einzelmandats-Tool

Nach berufsrechtliche KI-Debatte 32/2025 (Seite 15) ist die Einwilligung des Mandanten oder Beteiligten regelmäßig nicht erforderlich, wenn das Tool als allgemeine Kanzleiinfrastruktur eingesetzt wird. Sie ist erforderlich, wenn das Tool unmittelbar einem einzelnen Mandat oder einem einzelnen Amtsgeschäft dient (Abs. 5 der jeweiligen Dienstleisterregelung).

Indikatoren für **Kanzleiinfrastruktur** (kein Einzelmandatsbezug, keine Einwilligung erforderlich):

- Mandant-unabhängige Recherche, Vorlagenerzeugung, allgemeine Vertragsanalyse, Wissensmanagement
- Verfügbarkeit für alle Mandate
- keine mandatsspezifische Konfiguration

Indikatoren für **Einzelmandats-Tool** (Einwilligung erforderlich):

- Spezielle Konfiguration für einen Mandanten
- Verarbeitung benannter Beteiligter
- Mandat-spezifische Trainingsdaten oder Embeddings
- Notariatsspezifisch: Tool dient einem konkreten Amtsgeschäft

Bei Unsicherheit: konservativ entscheiden und Einwilligung einholen.

## Eingangsdaten
- Beruf: ...
- Norm-Adapter: § ...
- Anbieter: ...
- Produkt: ...
- Subunternehmer: ...
- Datenarten: ...
- Hostingland: ...
- Auslandsbezug: ...
- Vertragstyp: Kanzleiinfrastruktur / Einzelmandats-Tool
- Vertragsdokumente vorgelegt: ja/nein, Stand, Anlagen
```

Diese Daten werden an alle folgenden Skills weitergereicht.

## Lückenmanagement

Wenn der Auftraggeber Antworten nicht hat, ist das selbst schon ein Befund. Fehlende Anbieter-Sitzangaben, fehlende Subunternehmerliste, unklarer Verarbeitungszweck — alles davon landet ohne weiteres im Rückfragebrief.

## Aktuelle Rechtsprechung zum Berufsgeheimnis

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 43a Abs. 2 BRAO, § 43e BRAO — Verschwiegenheitspflicht und Dienstleisterregelung Rechtsanwalt
- § 57 Abs. 1, § 62a StBerG — Steuerberater
- § 43 Abs. 1, § 50a WPO — Wirtschaftsprüfer
- § 39a Abs. 2, § 39c PAO — Patentanwalt
- § 18 BNotO, § 26a BNotO — Notar
- §§ 203, 204 StGB — Straftatbestände Verletzung/Verwertung von Privatgeheimnissen
- §§ 53a, 97 StPO — Zeugnisverweigerungsrecht und Beschlagnahmeverbot für Berufshelfer

## Triage-Frage (Entscheidungsbaum)

```
Beruf bestimmt?
 Nein → Pflichtfrage 1 stellen
 Ja → Norm-Adapter anwenden (BRAO / StBerG / WPO / PAO / BNotO)
 → Kanzleiinfrastruktur oder Einzelmandats-Tool?
 Einzelmandats-Tool → Einwilligungspflicht § 26a Abs. 4 BNotO prüfen
 Kanzleiinfrastruktur → Einwilligung i.d.R. nicht erforderlich (DAV S. 15)
 → Auslandsbezug (US-Anbieter)?
 Ja → Cloud-Act-Prüfung erforderlich → Skill cloud-act-und-drittstaat-pruefen
 Nein → Weiter mit Verschwiegenheitsprüfung
```

## Output-Template — Eingangsdatensatz

**Adressat:** Kanzlei intern — Tonfall: sachlich-strukturiert

```

## Eingangsdaten [DATUM]
- Beruf: [BERUF]
- Norm-Adapter: § [NORM] [GESETZ]
- Anbieter: [NAME, SITZ, LAND]
- Produkt: [NAME, VERSION]
- Subunternehmer: [LISTE ODER "noch nicht bekannt"]
- Datenarten: [BESCHREIBUNG]
- Drittlandbezug: [ja/nein; wenn ja: CLOUD-Act-Risiko: ja/nein]
- Hostingland: [LAND]
- Vertragstyp: Kanzleiinfrastruktur / Einzelmandats-Tool
- Vertragsdokumente vorgelegt: [ja/nein, Datum, Anlagen]
- Nächste Schritte: [Prüfpunkte auflisten]
```

---

## Skill: `rueckfragebrief-an-anbieter`

_Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und Drittstaat) Fragen zu Zertifizierungen und Versprechungen Frist Unterschrift. K..._

# Rückfragebrief an Anbieter

## Fachkern: Rückfragebrief an Anbieter

- **KI-/Berufsrechtsproblem (Rückfragebrief an Anbieter):** Erstelle einen strukturierten Rückfragebrief an den KI-Anbieter zur Klaerung der berufsrechtlichen und strafrechtlichen Pflichten. Aufbau Anschreiben Kontext drei Fragenbloecke (Verschwiegenheit Subunternehmer TOM und Drittstaat) Fragen zu Zertifizierungen und Versprechungen Frist Unterschrift. Klare praezise Fragen die der Anbieter beantworten kann.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Aufbau

### Briefkopf

- Absender: Kanzlei mit Berufsbezeichnung
- Empfänger: Anbieter, vertretungsberechtigte Person
- Datum
- Betreff: "Berufsrechtliche und strafrechtliche Anforderungen — Vertrag [Produktname]"

### Anschreiben

Kurze Einleitung — die Kanzlei prüft den Einsatz des KI-Produkts und benötigt vor Vertragsschluss bzw. zur Fortsetzung des Vertragsverhältnisses Klarstellungen zu den berufsrechtlichen Anforderungen aus §§ [Norm-Adapter] und § 203 StGB.

### Inhaltliche Blöcke

#### Block 1 — Verschwiegenheit und Belehrung

- Wo und wie ist die Verschwiegenheit Ihres Hauses gegenüber der Kanzlei vertraglich geregelt? Bitte konkrete Fundstelle.
- Gilt die Verschwiegenheit gegenüber jedermann und zeitlich unbegrenzt?
- Wie haben Sie Ihre Mitarbeiter zur Verschwiegenheit verpflichtet (Textform nach § 126b BGB)?
- Wie werden Mitarbeiter und Subunternehmer über die strafrechtlichen Folgen einer Pflichtverletzung nach §§ 203, 204 StGB belehrt? Liegt der Normtext als Anlage zu den Mitarbeiterverträgen vor?

#### Block 2 — Subunternehmer

- Bitte legen Sie die aktuelle, abschließende Liste aller Subunternehmer (insbesondere Modellanbieter und Hoster) mit Sitz, Funktion und Verarbeitungsstandort vor.
- Wie werden Subunternehmer vertraglich auf die Verschwiegenheit verpflichtet und über §§ 203, 204 StGB belehrt?
- Welche Vorabinformations- und Zustimmungsrechte hat die Kanzlei bei Hinzunahme oder Wechsel von Subunternehmern?
- Falls Microsoft Azure oder AWS oder Google Cloud zum Einsatz kommt: Welche Region wird genutzt? Wo liegen Backups?

#### Block 3 — Erforderlichkeit, no training, Speicherdauer

- Welche konkreten Datenkategorien werden bei der Nutzung Ihres Dienstes verarbeitet?
- Werden eingegebene Daten zum Training Ihres Modells oder eines Drittmodells verwendet? Bitte vertragliche "no training"-Zusicherung mit Fundstelle.
- Wie lange werden Eingaben gespeichert? Liegt eine Zero-Retention-Klausel vor?
- Wie erfolgt die Löschung am Vertragsende? Erhalten wir ein Löschprotokoll?

#### Block 4 — Strafprozessuale Absicherung

- Wie verhält sich Ihr Haus bei behördlichen Auskunftsverlangen, Durchsuchungs- oder Beschlagnahmeanordnungen?
- Werden Sie die Kanzlei unverzüglich vorab informieren (soweit gesetzlich zulässig)?
- Werden Sie sich gegen unzulässige Beschlagnahmen mit Hinweis auf §§ 53a, 97 StPO zur Wehr setzen?
- Gilt deutsches Recht? Ist der Gerichtsstand Deutschland?

#### Block 5 — TOM und Zertifizierungen

- Welche aktuellen Zertifikate liegen vor (ISO 27001, BSI C5 Typ 2, SOC 2 Typ 2)? Bitte Geltungsbereich, Zertifizierungsstelle und Ausstellungsdatum.
- Wo werden Daten gespeichert (Verarbeitungsstandort und Backupstandort)?
- Welche Verschlüsselung wird im Transport und im Ruhezustand eingesetzt?
- Welche Audit-Logs werden geführt? Wie lange?
- Welche Meldefrist gilt für Sicherheitsvorfälle?

#### Block 6 — Drittstaaten und CLOUD Act

- Sind Sie ein US-Konzern oder eine US-Tochter? Findet US-Recht (CLOUD Act, FISA) auf Ihre Daten Anwendung?
- Liegen Daten oder Backups in Drittstaaten?
- Sind Sie bereit, ein Professional Secrecy Addendum zu unterzeichnen, das US-Auskunftsverlangen anficht und uns informiert?

### Fristsetzung und Hinweise

- Konkrete Frist (typisch zwei bis vier Wochen)
- Hinweis, dass ohne Klarstellung ein Vertragsschluss bzw. eine Fortsetzung berufsrechtlich nicht möglich ist
- Hinweis auf Vertraulichkeit der Anfrage

### Unterschrift

- Name, Funktion (Partner, Compliance-Officer)
- Berufsbezeichnung

## Ton

Sachlich, präzise, keine Anschuldigungen. Der Anbieter soll motiviert sein zu antworten. Die Kanzlei dokumentiert dadurch zugleich die Sorgfalt nach Abs. 2 der Dienstleisterregelung.

## Disclaimer im Brief

Der Brief ist eine berufsrechtliche und strafrechtliche Anfrage, keine zivilrechtliche Geltendmachung. Eine zivilrechtliche oder gar strafrechtliche Geltendmachung ist im Streitfall einem spezialisierten Rechtsanwalt vorbehalten.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 241 Abs. 2, 311 Abs. 2 BGB — Vorvertragliche Aufklärungspflichten
- § 305b BGB — Vorrang der Individualabrede
- § 126b BGB — Textform
- § 43e Abs. 3 BRAO, § 62a Abs. 3 StBerG etc. — Vertragsinhalt der Dienstleisterregelung

## Triage zu Beginn

1. Welche Lücken hat die bisherige Vertragsprüfung ergeben (Ampel: gelb/rot)?
2. Welche Fragen sind klärungsbedürftig (Subunternehmer, Training, Drittstaat)?
3. Ist ein Fristdruck vorhanden (laufende Pilotprojekte, Vertragsbeginn)?
4. Soll die Antwort des Anbieters als vertragliche Zusicherung eingestuft werden?

## Output-Template — Rückfragebrief

**Adressat:** KI-Anbieter — Tonfall: sachlich-präzise, fristsetzend

```
[KANZLEINAME]
[ANSCHRIFT]
[DATUM]

An: [ANBIETER, RECHTSABTEILUNG / DATENSCHUTZTEAM]
Betr.: Rückfrageverfahren berufsrechtliche Compliance — [PRODUKTNAME]
Unser Aktenzeichen: [AZ]

Sehr geehrte Damen und Herren,

wir pruefen den Einsatz von [PRODUKT] in unserer Kanzlei im Hinblick auf die
berufsrechtlichen Anforderungen nach § [NORM] [GESETZ] sowie §§ 203, 204 StGB.
Dazu bitten wir um Beantwortung der folgenden Fragen bis zum [FRIST + 14 TAGE]:

Frageblock 1 — Verschwiegenheit
F1: Sind Ihre Mitarbeiter und alle Subunternehmer in Textform zur Verschwiegenheit
 ueber alle von uns eingegebenen Daten verpflichtet?
F2: Gilt diese Verpflichtung auch nach Vertragsende zeitlich unbegrenzt?

Frageblock 2 — Subunternehmer
F3: Welche Subunternehmer (Modellanbieter, Hoster, Support-Dienstleister) haben
 Zugriff auf von uns eingegebene Daten?
 Bitte vollstaendige Liste: Name, Sitz, Funktion, Verarbeitungsstandort.
F4: Werden wir vor Wechsel oder Hinzunahme von Subunternehmern vorab in Textform
 informiert?

Frageblock 3 — Training und Drittstaat
F5: Werden von uns eingegebene Daten zu Trainingszwecken genutzt?
 (Auch aggregiert oder anonymisiert?)
F6: Wo werden unsere Daten verarbeitet und gespeichert?
 Werden US-Server oder US-Subunternehmer eingesetzt (CLOUD-Act-Risiko)?

Wir bitten um Beantwortung in Textform.

Mit freundlichen Gruessen
[UNTERSCHRIFT]
```

---

## Skill: `strafprozessuale-regelung-pruefen`

_Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunftsverlangen Informationspflicht gegenüber der Kanzlei. Ergaenz..._

# Strafprozessuale Regelung prüfen

## Fachkern: Strafprozessuale Regelung prüfen

- **KI-/Berufsrechtsproblem (Strafprozessuale Regelung prüfen):** Prüfe die strafprozessuale Absicherung des KI-Dienstleisters nach §§ 53a 97 StPO. Zeugnisverweigerungsrecht der mitwirkenden Personen Beschlagnahmeverbot für Mandatsdaten Widerspruchspflicht des Dienstleisters bei behoerdlichen Auskunftsverlangen Informationspflicht gegenüber der Kanzlei. Ergaenzung zum berufsrechtlich-strafrechtlichen Schutz.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Normen

### § 53a StPO — Zeugnisverweigerungsrecht der mitwirkenden Personen

§ 53a StPO erstreckt das Zeugnisverweigerungsrecht der in § 53 Abs. 1 Satz 1 Nr. 1 bis 4 StPO genannten Berufsgeheimnisträger (also Geistliche, Verteidiger, Rechtsanwälte, Patentanwälte, Notare, Steuerberater, Wirtschaftsprüfer, Ärzte etc.) auf ihre Berufshelfer und die ihnen mitwirkenden Personen. Damit auch der KI-Dienstleister, soweit er als "mitwirkende Person" im Sinne des § 203 Abs. 3 Satz 2 StGB eingebunden ist.

### § 97 StPO — Beschlagnahmeverbot

§ 97 Abs. 1 StPO normiert ein Beschlagnahmeverbot für Schriftstücke und elektronische Daten, die sich im Gewahrsam der zur Zeugnisverweigerung Berechtigten befinden, soweit das Vertrauensverhältnis betroffen ist. § 97 Abs. 2 Satz 2 StPO erstreckt dies auch auf Daten, die im Gewahrsam der mitwirkenden Personen liegen.

Praktische Konsequenz: Mandatsdaten beim KI-Dienstleister sind grundsätzlich der Beschlagnahme entzogen, soweit die Verschwiegenheitspflicht gilt.

## Vertragliche Anforderungen

Diese Schutzwirkung muss im Vertrag operationalisiert werden. Empfehlungen:

### Widerspruchspflicht des Dienstleisters

Der Dienstleister soll sich verpflichten, behördlichen Auskunftsverlangen, Beschlagnahmebeschlüssen oder Herausgabeverfügungen mit dem Hinweis auf §§ 53a, 97 StPO entgegenzutreten — und nicht widerstandslos zu kooperieren.

### Informationspflicht gegenüber der Kanzlei

Der Dienstleister muss die Kanzlei unverzüglich informieren, sobald ein Auskunftsverlangen, eine Durchsuchung oder eine Beschlagnahmeanordnung droht oder erfolgt — soweit gesetzlich zulässig (manche US-Beschlagnahmeanordnungen kommen mit Gag Order).

### Pflicht zur prozessualen Inanspruchnahme

Im Idealfall verpflichtet sich der Dienstleister, gegen unzulässige Beschlagnahmen den Rechtsweg zu beschreiten, mindestens aber Widerspruch einzulegen.

### Gerichtsstand und anwendbares Recht

Anwendbares deutsches Recht und ein deutscher Gerichtsstand sind dringend zu empfehlen, da §§ 53a, 97 StPO nur im deutschen Verfahren wirken.

## Prüfschema

| Punkt | Fundstelle | Ampel | Bemerkung |
|---|---|---|---|
| Hinweis auf §§ 53a, 97 StPO im Vertrag | | | |
| Widerspruchspflicht bei behördlichen Verlangen | | | |
| Informationspflicht gegenüber Kanzlei | | | |
| Pflicht zur prozessualen Inanspruchnahme | | | |
| Deutsches Recht und Gerichtsstand | | | |
| Gag-Order-Klausel (Information so weit zulässig) | | | |

## US-Konstellationen — CLOUD Act

Bei US-Anbietern oder US-Töchtern greift der US-CLOUD Act und kann § 97 StPO faktisch unterlaufen. Hier ist ein separates Professional Secrecy Addendum erforderlich (siehe `cloud-act-und-drittstaat-pruefen`).

## Typische Lücken

- Keine Erwähnung von §§ 53a, 97 StPO
- Klausel "wir kooperieren mit Behörden" ohne Vorbehalt
- Keine Pflicht zur Vorab-Information der Kanzlei
- Nur US-Eskalationspfad, kein deutsches Verfahren möglich

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 53, 53a StPO — Zeugnisverweigerungsrecht und dessen Erstreckung auf Berufshelfer
- §§ 94–98 StPO — Beschlagnahme; § 97 StPO Beschlagnahmeverbot für Mandatsunterlagen
- § 203 Abs. 4 StGB — Pflicht des Berufsgeheimnisträgers, den Dienstleister auf §§ 203/204 StGB hinzuweisen
- §§ 43e Abs. 3, 62a Abs. 3 StBerG etc. — Vertragsinhalt

## Triage zu Beginn

1. Ist im Vertrag geregelt, wie der Dienstleister mit behördlichen Auskunftsersuchen umgeht?
2. Enthält der Vertrag eine Widerstandspflicht (Pflicht zur Rechtsbehelfseinlegung)?
3. Ist eine Vorab-Informationspflicht gegenüber der Kanzlei geregelt?
4. Bei US-Anbietern: CLOUD Act Addendum vorhanden?

## Output-Template — Strafprozessuale Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Strafprozessuale Prüfvermerk [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: Zeugnisverweigerungsrecht (§ 53a StPO)
Vertrag regelt Mitwirkung als Berufshelfer: ja / nein / unklar
Fundstelle: [KLAUSEL]

Prüfpunkt 2: Widerstandspflicht bei behördlichen Auskunftsersuchen
Klausel vorhanden: ja / nein
Inhalt: [BESCHREIBUNG]
Fundstelle: [KLAUSEL]

Prüfpunkt 3: Vorab-Informationspflicht der Kanzlei
Geregelt: ja / nein
Fundstelle: [KLAUSEL]

Ergebnis
Ampel strafprozessuale Absicherung: GRUEN / GELB / ROT
Handlungsbedarf: [...]
```

---

## Skill: `strafrechtliche-belehrung-pruefen`

_Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Vertragsanlage. Hinweis auf Sekundaerpflicht des Dienstleisters..._

# Strafrechtliche Belehrung prüfen

## Fachkern: Strafrechtliche Belehrung prüfen

- **KI-/Berufsrechtsproblem (Strafrechtliche Belehrung prüfen):** Prüfe die strafrechtliche Belehrung des Dienstleisters nach Absatz drei Satz zwei Nummer eins der einschlaegigen Dienstleisterregelung. Pflichtinhalte § 203 Absatz eins drei vier und sechs StGB und § 204 StGB. Empfehlung Normtext als Vertragsanlage. Hinweis auf Sekundaerpflicht des Dienstleisters nach § 203 Absatz vier Satz zwei Nummer eins StGB.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm

Absatz 3 Satz 2 Nr. 1 der jeweiligen Dienstleisterregelung verlangt die Verpflichtung des Dienstleisters "unter Belehrung über die strafrechtlichen Folgen einer Pflichtverletzung". Diese Folgen ergeben sich aus § 203 StGB und § 204 StGB.

Pro Beruf identische Anforderung in:

- § 43e Abs. 3 Satz 2 Nr. 1 BRAO
- § 62a Abs. 3 Satz 2 Nr. 1 StBerG
- § 50a Abs. 3 Satz 2 Nr. 1 WPO
- § 39c Abs. 3 Satz 2 Nr. 1 PAO
- § 26a Abs. 3 Satz 2 Nr. 1 BNotO

## § 203 StGB — Architektur

### Abs. 1 — Strafbarkeit der Berufsgeheimnisträger

Wer ein fremdes Geheimnis offenbart, das ihm in seiner Eigenschaft als Angehöriger der dort genannten Berufsgruppen anvertraut oder bekanntgeworden ist. Nr. 1 erfasst unter anderem Notare; Nr. 3 erfasst Rechtsanwälte, Patentanwälte, Notare (alternativ), Steuerberater, Wirtschaftsprüfer und vergleichbare Berufsgruppen.

### Abs. 3 Satz 2 — Befugnisnorm

Die in Abs. 1 Genannten dürfen fremde Geheimnisse gegenüber sonstigen mitwirkenden Personen offenbaren, soweit dies für die Inanspruchnahme der Tätigkeit der sonstigen Personen erforderlich ist. Dies ist die strafrechtliche Befugnisnorm, die das Berufsrecht (§ 43e BRAO etc.) ergänzt.

### Abs. 4 — Strafbarkeit des Dienstleisters

**Abs. 4 Satz 1**: Die strafrechtliche Verantwortlichkeit erstreckt sich auch auf die "sonstigen mitwirkenden Personen", wenn sie das Geheimnis unbefugt offenbaren.

**Abs. 4 Satz 2 Nr. 1**: Sekundärpflicht der Berufsgeheimnisträger — sie haben die mitwirkenden Personen vertraglich zur Geheimhaltung zu verpflichten. Wer dies unterlässt, macht sich nach § 203 Abs. 4 Satz 2 Nr. 1 StGB selbst strafbar. Das ist der zentrale strafrechtliche Druckpunkt für die Sorgfalt bei der Vertragsgestaltung.

### Abs. 6 — gewerbsmäßig

Gewerbsmäßiges Handeln führt zu erhöhter Strafandrohung. Relevant insbesondere für den Dienstleister selbst, der eine Datenverwertung betreibt.

## § 204 StGB

Verwertung fremder Geheimnisse zu eigenen Zwecken. Konkurrenznorm zu § 203 StGB für Fälle, in denen das Geheimnis nicht offenbart, sondern wirtschaftlich verwertet wird (etwa Modelltraining mit Mandatsdaten zu Wettbewerbszwecken).

## Anforderungen an die Belehrung

- Ausdrücklicher Verweis auf § 203 StGB und § 204 StGB im Vertrag
- Hinweis auf Strafandrohung Freiheitsstrafe bis zu einem Jahr oder Geldstrafe (Grundtatbestand)
- Hinweis auf gewerbsmäßige Variante (höhere Strafandrohung)
- Normtext idealerweise als Vertragsanlage
- Empfänger der Belehrung: der Dienstleister selbst und alle sonstigen mitwirkenden Personen (die der Dienstleister einbindet)

## Prüfschema

| Punkt | Fundstelle | Ampel | Bemerkung |
|---|---|---|---|
| Verweis auf § 203 StGB | | | |
| Verweis auf § 204 StGB | | | |
| Belehrung im Vertragstext | | | |
| Normtext als Anlage | | | |
| Belehrung umfasst auch Subunternehmer | | | |

## Typische Lücken

- Pauschaler Hinweis "strafbewehrte Verschwiegenheit" ohne Normnennung — unzureichend
- Belehrung nur auf englisch ohne deutsche Übersetzung — bei deutschem Anbieter problematisch
- Belehrung ausschließlich auf der Subunternehmer-Ebene, nicht beim Dienstleister selbst
- Keine Belehrung in den Mitarbeiterunterlagen des Dienstleisters

## Anlage Normtext (Vorlage)

Im Skill `klauselvorschlaege` befindet sich ein Mustertext der Anlage Normtext §§ 203, 204 StGB, der direkt in den Vertrag übernommen werden kann.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- § 203 Abs. 1, Abs. 3 Satz 2, Abs. 4, Abs. 6 StGB — Verletzung von Privatgeheimnissen
- § 204 StGB — Verwertung fremder Geheimnisse
- §§ 43e Abs. 3 Nr. 1 BRAO, 62a Abs. 3 Nr. 1 StBerG, 50a Abs. 3 Nr. 1 WPO, 39c Abs. 3 Nr. 1 PAO, 26a Abs. 3 Nr. 1 BNotO — Pflicht zur Belehrung in Textform

## Triage zu Beginn

1. Enthält der Dienstleistervertrag eine explizite Belehrung über §§ 203, 204 StGB?
2. Ist die Belehrung in Textform (§ 126b BGB) dokumentiert?
3. Wurde der Normtext der §§ 203/204 StGB als Anlage beigefügt?
4. Verpflichtet der Vertrag den Dienstleister, seine Subunternehmer ebenso zu belehren?
5. Erfasst die Belehrung § 203 Abs. 6 StGB (gewerbsmäßige Variante)?

## Output-Template — Belehrungsprüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
Belehrungsprüfvermerk §§ 203/204 StGB [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: Belehrung im Vertrag
Vorhanden: ja / nein
Fundstelle: [KLAUSEL, ABSCHNITT]
Deckt ab: § 203 Abs. 1 / Abs. 3 Satz 2 / Abs. 4 / Abs. 6 / § 204

Prüfpunkt 2: Normtext als Anlage
Normtext §§ 203/204 StGB als Anlage beigefügt: ja / nein

Prüfpunkt 3: Weiterverpflichtung Subunternehmer
Vertrag verpflichtet Dienstleister zur Belehrung der Subunternehmer: ja / nein
Fundstelle: [KLAUSEL]

Ergebnis
Ampel strafrechtliche Belehrung: GRUEN / GELB / ROT
Luecken: [BESCHREIBUNG]
Handlungsbedarf: [ERGAENZUNGSKLAUSEL / RUECKFRAGE AN ANBIETER]
```

---

## Skill: `tom-und-zertifizierungen-pruefen`

_Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Löschkonzep..._

# TOM und Zertifizierungen prüfen

## Fachkern: TOM und Zertifizierungen prüfen

- **KI-/Berufsrechtsproblem (TOM und Zertifizierungen prüfen):** Prüfe technische und organisatorische Massnahmen des KI-Anbieters und seine Zertifizierungen. Maßstab Art. 32 DS-GVO ISO 27001 BSI C5 (Cloud Computing Compliance Criteria Catalogue) SOC zwei Typ zwei TISAX. Zentral für Berufsrecht no training Zero-Retention EU-Hosting Verschluesselung Löschkonzept Audit-Recht. berufsrechtliche KI-Debatte Seite dreizehn vierzehn.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Auftragsverarbeitung, Dienstleisterregelungen der freien Berufe und prozessuale Akten-/Mandatsgeheimnisse fallbezogen prüfen.
- **Entscheidende Weiche:** Anbieterbehauptung, Vertragswortlaut, technische Realität, Berufsgeheimnis, Datenschutzrolle und Strafbarkeitsrisiko auseinanderziehen.
- **Arbeitsprodukt:** Anbieter-Fragenliste, Risikomatrix, Vertragsredline und Entscheidung, ob Pilot, Stop oder Nachverhandlung.
- **Hinweis:** Ergebnis bleibt Vorprüfung für Kanzlei- oder Spezialberatung; keine Scheinsicherheit gegenüber Berufsrecht oder Strafrecht.

## Norm und Rahmen

Berufsrechtlich verlangt die Sorgfaltspflicht bei der Dienstleisterauswahl (Abs. 2 der jeweiligen Dienstleisterregelung), dass die technische und organisatorische Sicherheit des Anbieters überzeugt. Datenschutzrechtlich präzisiert das Art. 32 DS-GVO. Die berufsrechtliche KI-Debatte 32/2025 (Seite 13) stellt klar: Die Verschlüsselung darf nicht so weit gefordert werden, dass sie die KI-Dienstleistung entwertet. Eine Ende-zu-Ende-Verschlüsselung, die das KI-System-Inferencing unmöglich macht, ist berufsrechtlich nicht zu verlangen.

## "no training" — Zentralfrage

Nach DAV S. 14 ist die Übermittlung von Mandatsdaten zu Trainingszwecken nicht von der Erforderlichkeitsschwelle des Abs. 1 gedeckt. Daher muss der Vertrag eine **"no training"-Klausel** enthalten — eine ausdrückliche Verpflichtung des Anbieters, eingegebene Mandatsdaten nicht zum Training des Modells zu verwenden. Bei API-Aufrufen an Drittmodelle (etwa OpenAI Azure Service) ist zusätzlich der "no training"-Status des Drittmodells nachzuweisen.

## Zero Retention

Die Speicherdauer eingegebener Mandatsdaten beim Anbieter ist möglichst gering zu halten. Optimal: "Zero Retention" — die Daten werden nach der Verarbeitung sofort gelöscht (typisch 0 oder 30 Sekunden nach Abschluss der API-Anfrage). Andernfalls eine konkrete kurze Frist (24 Stunden, sieben Tage). Pauschalfristen wie "bis zu 90 Tage" sind problematisch.

## Zertifizierungen

### ISO 27001

Internationaler Standard für Informationssicherheitsmanagementsysteme. **Mindeststandard**. Prüfen: Geltungsbereich (alle relevanten Standorte und Systeme), Zertifizierungsstelle (akkreditiert), Ausstellungsdatum (höchstens drei Jahre alt), Anhang A Controls relevant.

### BSI C5 (Cloud Computing Compliance Criteria Catalogue)

Vom BSI entwickelter Standard für Cloud-Anbieter. Für Berufsgeheimnisträger besonders aussagekräftig, weil deutsche behördliche Standardkriterien. Es gibt Typ-1- und Typ-2-Testate; Typ 2 ist der Goldstandard.

### SOC 2 Typ 2

US-Standard, oft bei US-Anbietern vorhanden. Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy. Bei US-Anbietern Mindestnachweis, aber nicht spezifisch genug für deutsches Berufsrecht.

### TISAX

Branchenstandard der Automobilindustrie. Für Legal-AI selten einschlägig, aber bei Mandanten aus der Automotive-Branche relevant.

### EU Cloud Code of Conduct

DSGVO-spezifisches Konformitätsverfahren nach Art. 40 DS-GVO. Hilfreich, aber keine eigenständige Sicherheitszertifizierung.

## Konkrete Prüfpunkte

### EU-Hosting

- Speicherort der Daten ausschließlich in EU/EWR?
- Auch Backups in EU/EWR?
- Verarbeitung (Inferencing) in EU/EWR?
- Vertraglich abgesichert oder nur als Selbstauskunft?

### Verschlüsselung

- Transportverschlüsselung TLS aktuell (mindestens TLS einskommadrei)
- Verschlüsselung im Ruhezustand (AES 256)
- Schlüsselverwaltung: Anbieter oder Kanzlei (Bring-your-own-key)?

### Zugriffskontrolle

- Rollenbasierte Zugriffskontrolle beim Anbieter
- Audit-Logs aller Zugriffe auf Mandatsdaten
- Vier-Augen-Prinzip bei Administratorenzugriffen
- Mitarbeiter-Verpflichtungen (Verschwiegenheit, Background Check)

### Löschkonzept

- Auf Anforderung der Kanzlei
- Automatisch nach Vertragsende
- Bestätigung der Löschung durch Anbieter (Löschprotokoll)
- Auch in Backups und Logs

### Audit-Recht

- Recht der Kanzlei zur Auditierung
- Vorhandene Testate als Surrogat (typisch)
- Mindestens jährliche Aktualisierung der Testate

### Meldepflichten

- Information bei Sicherheitsvorfällen (24 bis 48 Stunden)
- Information bei Behördenanfragen
- Information bei Subunternehmerwechsel

## Prüfschema

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Punkt | Status | Ampel | Bemerkung |
|---|---|---|---|
| "no training"-Klausel | | | |
| Zero Retention oder kurze Frist | | | |
| ISO 27001 (akt. Testat) | | | |
| BSI C5 (Typ 2 bevorzugt) | | | |
| SOC 2 Typ 2 | | | |
| EU-Hosting vertraglich | | | |
| Verschlüsselung TLS plus Rest | | | |
| Audit-Logs | | | |
| Löschkonzept | | | |
| Meldepflicht Sicherheitsvorfall | | | |
| Audit-Recht | | | |

## Typische Lücken

- "Wir nehmen Sicherheit ernst" ohne Zertifikat
- ISO-Zertifikat nur für Hauptsitz, nicht für Verarbeitungsstandort
- Trust Center mit Versprechen, die nicht im Vertrag stehen
- Löschung nur "auf Anforderung", keine automatische
- Keine "no training"-Klausel für das verwendete Modell

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- Art. 32 DSGVO — Technische und organisatorische Maßnahmen; Stand der Technik
- Art. 28 Abs. 3 lit. c DSGVO — TOM-Anlage als Pflichtbestandteil der AVV
- Art. 83 Abs. 4 DSGVO — Bußgeld bei Verstoß gegen Art. 32: bis 10 Mio. EUR oder 2 %

## Triage zu Beginn

1. Liegt eine aktuelle TOM-Anlage (mit Datum) zum Vertrag vor?
2. Ist eine ISO-27001-Zertifizierung vorhanden und aktuell (nicht älter als 12 Monate)?
3. Bei Cloud-Anbieter: BSI C5 Typ 2 Testat vorhanden?
4. Sind "no training" und Zero-Retention-Regelungen in den TOMs enthalten?
5. Gibt es ein Audit-Recht der Kanzlei?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — TOM-Abschnitt im Vertrag bewerten | Checkliste Art. 32 DSGVO; Template unten |
| Variante A — Zertifizierung ISO 27001 vorhanden | Zertifikat pruefen ob aktuell; Scope-Abdeckung beachten |
| Variante B — keine TOM-Anlage vorhanden | Ergaenzung fordern; Muster-TOM-Anlage als Verhandlungsgrundlage |
| Variante C — Hochrisiko-Verarbeitung | Erweiterte TOM-Anforderungen; ggf. Pen-Test-Pflicht vereinbaren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — TOM-Prüfvermerk

**Adressat:** Kanzlei intern — Tonfall: sachlich-juristisch

```
TOM-Prüfvermerk [DATUM]
Anbieter: [NAME] | Vertrag: [DOKUMENT, VERSION]

Prüfpunkt 1: TOM-Anlage
Vorhanden: ja / nein | Datum: [DATUM]
Verschlüsselung (Transport/Ruhezustand): [TLS 1.3 / AES-256 / unklar]
Zugangskontrolle / RBAC: [beschrieben / nicht beschrieben]
Löschkonzept: [beschrieben / nicht beschrieben]

Prüfpunkt 2: Zertifizierungen
ISO 27001: [vorhanden / nicht vorhanden] | Gültigkeit: [DATUM]
BSI C5 Typ 2: [vorhanden / nicht vorhanden]
SOC 2 Typ 2: [vorhanden / nicht vorhanden]

Prüfpunkt 3: Berufsrechtliche TOM-Besonderheiten
No-training-Klausel: [vorhanden / Lücke]
Zero-Retention: [vorhanden / Lücke]
EU-Hosting-Zusicherung: [vorhanden / Lücke]
Audit-Recht Kanzlei: [vorhanden / Lücke]

Ergebnis
Ampel TOM/Zertifizierungen: GRUEN / GELB / ROT
Luecken: [BESCHREIBUNG]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

