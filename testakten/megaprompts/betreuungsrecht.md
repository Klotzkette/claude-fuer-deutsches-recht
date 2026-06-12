# Megaprompt: betreuungsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 116 Skills (gekuerzt fuer Chat-Fenster) des Plugins `betreuungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Betreuungsrecht: ordnet Rolle (Betroffener, Betreuer, Familie/Angehörige), markiert Fri…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Betreuungsrecht-Plugin für ehrenamtliche Familienbetreuer, Berufsbetreuer, An…
3. **betreuungsrechtliche-erstpruefung-und-mandatsziel** — Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Betreuungsrecht.
4. **genehmigungspflicht-pruefung** — 'Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuun…
5. **jahresbericht-betreuungsgericht** — Jahresbericht und Anfangs-/Schlussbericht für das Betreuungsgericht nach § 1863 BGB erstellen: persönliche Kontakte, Wün…
6. **kaltstart-interview** — Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil mit Angaben zur Rolle (betreute Person / An…
7. **kontodaten-vertragsverdacht-pruefung** — Kontoauszüge und Vertragsunterlagen in Betreuungsfällen auf Missbrauch prüfen: ungewöhnliche Zahlungen, verdächtige Daue…
8. **vermoegensverzeichnis-pruefung** — Vermögensverzeichnis für Betreuung prüfen und erstellen: Betreuer muss bei Aufgabenkreis Vermögenssorge nach § 1835 BGB …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Betreuungsrecht: ordnet Rolle (Betroffener, Betreuer, Familie/Angehörige), markiert Frist (Beschwerde 1 Monat § 63 FamFG), wählt Norm (§§ 1814 ff. BGB, FamFG §§ 271 ff., § 1827 BGB Patientenverfügung) und Zuständigkeit (Betreuungsgericht (AG)), leitet zum passende..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Betreuungsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anschluss-router` — Anschluss Router
- `aufgabenkreise-festlegen` — Aufgabenkreise Festlegen
- `bericht-betreuer-betreuerpflichten` — Bericht Betreuer Betreuerpflichten
- `bericht-mandantenkommunikation` — Bericht Mandantenkommunikation
- `betreuer-als-erbe` — Betreuer ALS Erbe
- `betreuer-registrierung` — Betreuer Registrierung
- `betreuer-registrierung-betreuung` — Betreuer Registrierung Betreuung
- `betreuer-zahlen-schwellen-und-berechnung` — Betreuer Zahlen Schwellen und Berechnung
- `betreuer-zahlen-schwellenwerte-berechnung` — Betreuer Zahlen Schwellenwerte Berechnung
- `betreuerpflichten-alltag` — Betreuerpflichten Alltag
- `betreuerpflichten-formular-portal-und-einreichung` — Betreuerpflichten Formular Portal und Einreichung
- `betreuerpflichten-genehmigung-bericht` — Betreuerpflichten Genehmigung Bericht
- `betreuerpflichten-genehmigung-betreuung` — Betreuerpflichten Genehmigung Betreuung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1814 Abs. 1 BGB` — Betreuungsvoraussetzungen.
- `§ 1815 Abs. 1 BGB` — Aufgabenkreis.
- `§ 1816 BGB` — Betreuerauswahl.
- `§ 1821 Abs. 1 BGB` — Wunschbefolgung.
- `§ 1823 BGB` — Vertretungsmacht.
- `§ 274 FamFG` — Beteiligte.
- `§ 278 FamFG` — Anhörung.
- `§ 280 FamFG` — Gutachten.
- `§ 5 BtOG` — Beratung.
- `§ 8 BtOG` — Betreuungsvermeidung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Betreuungsrecht sind BGB, BtOG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Betreuungsrecht-Plugin für ehrenamtliche Familienbetreuer, Berufsbetreuer, Angehörige, Betroffene und anwaltliche Begleiter. Fragt Rolle, Aufgabenkreise, Fristen, Unterlagen, Risiken, Wunsch der betreuten Person und Ziel-Output ab, schlägt passende Fachm_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Betreuungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Betreuungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Betreuungsrechtliche Skills für ehrenamtliche Familienbetreuer und professionelle Betreuung: erster Monat, Scan-Akte, Kalender/Reminder, Gerichtskommunikation, Wunschermittlung, Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse, Verdachtsverträge und Schutzplan nach BtOG und BGB.

### Ehrenamtlicher Familienbetreuer-Modus

Wenn der Nutzer als Angehöriger, Familienbetreuer oder erstmaliger ehrenamtlicher Betreuer schreibt, führe besonders niedrigschwellig:

1. **Beruhigen und ordnen:** Erst klären, ob überhaupt schon ein Beschluss vorliegt und welche Aufgabenkreise genau gelten.
2. **Nicht überfordern:** keine juristische Gesamtabhandlung, sondern drei Ebenen: `heute`, `diese Woche`, `laufend beobachten`.
3. **Schutz der betreuten Person:** Wunschermittlung nach § 1821 BGB, mildestes Mittel, keine automatische Bevormundung.
4. **Gerichtstaugliche Ordnung:** Scans, Belege, Aktenzeichen, Fristen, Jahresbericht, Vermögensverzeichnis.
5. **Hilfe aktivieren:** Betreuungsgericht, Betreuungsbehörde, Betreuungsverein, Verhinderungsbetreuung und anwaltliche Hilfe an den richtigen Stellen.
6. **Überforderung ernst nehmen:** Bei Immobilien, Erbe, hohem Vermögen, Familienkonflikt, freiheitsentziehenden Maßnahmen, Zwangsbehandlung oder verworrener Vermögenslage früh eskalieren.

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
| Rolle | Wer fragt: betreute Person, Angehöriger/Familienbetreuer, ehrenamtlicher Betreuer, Berufs-/Vereinsbetreuer, Betreuungsbehörde, Anwalt? | Perspektive, Ton und Hilfen bestimmen. |
| Aufgabenkreise | Welche Aufgabenkreise stehen im Beschluss: Vermögenssorge, Gesundheitssorge, Wohnen, Behörden, Post, Aufenthalt? | Nur innerhalb des Aufgabenkreises handeln. |
| Wunsch | Was will die betreute Person selbst, heute oder früher erkennbar? | § 1821 BGB ist der Kern der Betreuung. |
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
| `ehrenamtlicher-betreuer-erster-monat` | Wenn ein Angehöriger oder ehrenamtlicher Betreuer neu bestellt ist und einen handhabbaren 30-Tage-Plan braucht. |
| `familienbetreuer-alltagscockpit` | Wenn Post, Pflege, Bank, Heim, Arzt, Gericht und Behörden in einen Wochenplan gebracht werden sollen. |
| `dokumentenscan-aktenablage-und-belegmappe` | Wenn Scans, Fotos, E-Mails, Kontoauszüge und Bescheide unsortiert vorliegen. |
| `kalender-reminder-und-fristenmanagement` | Wenn Termine, Berichtspflichten, Bescheidfristen, Zahlungen und Routinekontakte in Reminder übersetzt werden sollen. |
| `betreuungsgericht-kommunikation-für-angehoerige` | Wenn ein knapper Brief, eine Rückfrage, Fristverlängerung oder Genehmigungsanfrage ans Gericht benötigt wird. |
| `wunschermittlung-unterstuetzte-entscheidung` | Wenn unklar ist, was die betreute Person will oder wie ihr Wunsch dokumentiert werden soll. |
| `betreuungsverein-behoerde-hilfe-holen` | Wenn der ehrenamtliche Betreuer Unterstützung, Einführung, Fortbildung oder Anbindung braucht. |
| `ueberforderung-verhinderung-und-abgabe` | Wenn der Betreuer merkt, dass Zeit, Krankheit, Konflikt oder Komplexität die Betreuung gefährden. |
| `schutzplan-betreute-person-risikoampel` | Wenn Gesundheits-, Wohn-, Vermögens-, Digitalbetrugs- oder Pflegerisiken schnell priorisiert werden müssen. |
| `familienkonflikt-grenzen-und-rollen` | Wenn Angehörige streiten, Auskunft verlangen, Druck machen oder Eigeninteressen im Raum stehen. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| `betreuer-registrierung` | Erklärt die Abgrenzung beruflicher / ehrenamtlicher (privater) Betreuer nach BtOG seit 01.01.2023 sowie den Weg zur Registrierung als beruflicher Betreuer nach Paragraphen 23 ff. BtOG und der… |
| `betreuungsrecht-kaltstart-interview` | Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md mit Angaben zur Betreuerrolle (Berufsbetreuer /… |
| `genehmigungspflicht-pruefung` | Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung,… |
| `jahresbericht-betreuungsgericht` | Jahresbericht, Anfangsbericht oder Schlussbericht nach § 1863 BGB erstellen und sauber von Vermögensverzeichnis/Rechnungslegung trennen. |
| `kontodaten-vertragsverdacht-pruefung` | Kontoauszüge und Vertragsunterlagen in Betreuungsfällen auf Missbrauch prüfen: Anwendungsfall Betreuer oder Betreuungsgericht hat Verdacht auf ungewöhnliche Zahlungen verdächtige Dauerverträge oder Anlagegeschäfte zum… |
| `vermoegensverzeichnis-pruefung` | Vermögensverzeichnis für Betreuung prüfen und erstellen: Anwendungsfall Betreuer muss nach § 1835 BGB Vermögensverzeichnis aufnehmen oder bestehendes Verzeichnis auf Vollständigkeit und Richtigkeit prüfen. § 1835 BGB… |

## Worum geht es?

Das Betreuungsrecht regelt die rechtliche Fuersorge für Erwachsene, die ihre Angelegenheiten ganz oder teilweise nicht selbst besorgen koennen. Seit der Reform zum 01.01.2023 gilt das Betreuungsorganisationsgesetz (BtOG) neben den materiellen Normen der §§ 1814 ff. BGB. Das Reformgesetz staerkt das Selbstbestimmungsrecht der betreuten Person, praezisiert die Pflichten des Betreuers und regelt erstmals umfassend die Registrierung und Verguetung beruflicher Betreuer.

Dieses Plugin unterstützt ehrenamtliche Familienbetreuer, berufliche Betreuer, Vereins- und Behördenbetreuer sowie deren Rechtsbeistände bei der täglich anfallenden Schutz-, Organisations-, Dokumentations-, Berichts- und Genehmigungsarbeit gegenüber betreuter Person, Betreuungsgericht, Behörden, Banken, Heimen, Ärzten und Pflegekassen.

## Wann brauchen Sie diese Skill?

- Sie sind als Angehöriger oder ehrenamtlicher Betreuer neu bestellt und wollen nichts falsch machen.
- Sie müssen Post scannen, Bescheide verstehen, Fristen notieren und mit Gericht, Bank, Heim oder Pflegekasse kommunizieren.
- Sie sind neu im Betreuungsrecht und möchten einen strukturierten Einstieg in Zuständigkeiten, Aufgabenkreise und Pflichten.
- Sie sind bereits Betreuer und wollen pruefen, welches Rechtsgeschaeft genehmigungspflichtig ist.
- Sie müssen den Jahresbericht nach § 1863 BGB für das Betreuungsgericht erstellen.
- Sie haben Zweifel, ob Kontobewegungen oder Vertraege der betreuten Person auf Missbrauch hindeuten.
- Sie moechten wissen, ob Sie als Berufsbetreuer testamentarisch bedacht werden duerfen.

## Fachbegriffe (kurz erklaert)

- **Betreuer** — vom Betreuungsgericht bestellte Person (§ 1814 BGB), die die betreute Person in bestimmten Aufgabenkreisen rechtlich vertritt.
- **Aufgabenkreis** — der konkret durch das Gericht festgelegte Wirkungsbereich des Betreuers (z.B. Vermögenssorge, Gesundheitssorge, Aufenthaltsbestimmung).
- **Berufsbetreuer** — registrierter Betreuer nach §§ 23 ff. BtOG, der Betreuungen entgeltlich fuehrt und bestimmte Sachkundeanforderungen erfuellt.
- **Genehmigungsvorbehalt** — Rechtsgeschaefte, die der Betreuer nur mit vorheriger Zustimmung des Betreuungsgerichts vornehmen darf (§§ 1848 ff. BGB).
- **Vermögensverzeichnis** — Aufstellung aller Vermoegensgegenstaende und Verbindlichkeiten der betreuten Person bei Amtsuebernahme (§ 1835 BGB).
- **Jahresbericht** — jährliche Berichtspflicht des Betreuers gegenüber dem Betreuungsgericht (§ 1863 Abs. 3 BGB).
- **Betreuungsverein** — anerkannte Stelle, die ehrenamtliche Betreuer einführt, fortbildet, berät und unterstützen kann (§ 15 BtOG).
- **VBVG** — Vergütung beruflicher Betreuer nach dem Vormünder- und Betreuervergütungsgesetz.

## Rechtsgrundlagen

- § 1814 BGB — Voraussetzungen der Betreuung
- §§ 1816 ff. BGB — Auswahl und Eignung des Betreuers
- § 1821 BGB — Pflichten des Betreuers und Wünsche der betreuten Person
- §§ 1835 ff. BGB — Vermögensverzeichnis und Rechnungslegung
- § 1863 BGB — Anfangsbericht, Jahresbericht und Schlussbericht
- §§ 15, 21, 22 BtOG — Unterstützung, Eignung und Anbindung ehrenamtlicher Betreuer
- §§ 1848 ff. BGB — Genehmigungspflichtige Rechtsgeschaefte
- § 30 BtOG — Verbot des Erwerbs von Vermoegensvorteilen
- §§ 23 ff. BtOG — Registrierung als Berufsbetreuer
- VBVG — Verguetung beruflicher Betreuer

## Schritt-für-Schritt: Einstieg ins Plugin

1. Rolle klären: betreute Person, Angehöriger, ehrenamtlicher Betreuer, Berufsbetreuer, Verein/Behörde oder anwaltliche Begleitung?
2. Phase des Mandats bestimmen: Ersteinrichtung (Registrierung, Vermögensverzeichnis), laufende Betreuung (Jahresbericht, Genehmigungen) oder Krisenfall (Missbrauchsverdacht, Erbschaftsfragen)?
3. Passenden Skill auswaehlen (siehe Skill-Tour unten).
4. Eilfristen pruefen: Genehmigungsantraege nach §§ 1848 ff. BGB sind vor der Massnahme einzuholen; Jahresbericht hat gerichtliche Einreichungsfristen.
5. Anschluss-Skill bestimmen: Nach Jahresbericht ggf. Vermoegensverzechnis-Pruefung; nach Missbrauchsverdacht ggf. Genehmigungspflicht-Pruefung.

## Skill-Tour (was gibt es hier?)

- `ehrenamtlicher-betreuer-erster-monat` — erste 30 Tage nach Bestellung: Beschluss, Hilfe-System, Akte, Fristen, Gericht.
- `familienbetreuer-alltagscockpit` — Wochensteuerung für Post, Pflege, Bank, Arzt, Heim, Behörden und Gericht.
- `dokumentenscan-aktenablage-und-belegmappe` — macht aus Scans und Fotos eine gerichtstaugliche Belegmappe.
- `kalender-reminder-und-fristenmanagement` — baut aus Bescheiden, Gerichtspost und Routinepflichten einen Reminderplan.
- `betreuungsgericht-kommunikation-für-angehoerige` — formuliert knappe Rückfragen, Sachstandsmitteilungen und Genehmigungsanfragen.
- `wunschermittlung-unterstuetzte-entscheidung` — dokumentiert Wünsche, Präferenzen und unterstützte Entscheidungen nach § 1821 BGB.
- `betreuungsrecht-kaltstart-interview` — Ersteinrichtung des Plugins: Praxisprofil mit Betreuerrolle, Gericht und Aufgabenkreisen anlegen.
- `betreuer-registrierung` — Erklaert Registrierungsweg, Sachkundeanforderungen und Berufshaftpflicht für Berufsbetreuer nach BtOG.
- `genehmigungspflicht-pruefung` — Prueft, ob ein konkretes Rechtsgeschaeft der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB).
- `jahresbericht-betreuungsgericht` — Erstellt den vollständigen Jahresbericht nach § 1863 BGB für das Betreuungsgericht.
- `vermoegensverzeichnis-pruefung` — Erstellt und prueft das Vermögensverzeichnis nach § 1835 BGB bei Amtsuebernahme oder Kontrollpruefung.
- `kontodaten-vertragsverdacht-pruefung` — Forensische Pruefung von Kontobewegungen und Vertraegen auf Missbrauch zum Nachteil der betreuten Person.
- `betreuer-als-erbe` — Beraet zur Zulaessigkeit testamentarischer Zuwendungen an Berufsbetreuer nach § 30 BtOG.

## Worauf besonders achten

- **Genehmigung vor der Massnahme**: Genehmigungspflichtige Rechtsgeschaefte (§§ 1848 ff. BGB) darf der Betreuer erst nach Erteilung der Genehmigung vornehmen; ein nachtraegliches Genehmigungsverfahren ist nur in engen Ausnahmefaellen moeglich.
- **Subsidiaritaet**: Ein Berufsbetreuer darf nur bestellt werden, wenn geeignete ehrenamtliche oder Angehoerigenbetreuer nicht zur Verfuegung stehen (§ 1816 Abs. 5 BGB).
- **Unterstützung vor Vertretung**: Erst die betreute Person zur eigenen Entscheidung befähigen; Vertretungsmacht nur nutzen, soweit erforderlich (§ 1821 Abs. 1 BGB).
- **Trennung von Betreuervermoegen und eigenem Vermoegen**: Einnahmen und Ausgaben der betreuten Person sind lückenlos zu dokumentieren; Vermischung mit eigenem Vermögen ist ein Haftungsrisiko (§ 1836 BGB).
- **§ 30 BtOG-Verbot**: Berufsbetreuer duerfen sich von der betreuten Person keine Vermoegensvorteile versprechen oder gewähren lassen; Verstoss ist berufsrechtlich relevant.

## Typische Fehler

- Jahresbericht, Vermögensverzeichnis und Rechnungslegung werden zusammengeworfen: § 1863 BGB, § 1835 BGB und Vermögens-/Rechnungslegungspflichten sind sauber zu trennen.
- Genehmigungen werden nach der Massnahme beantragt: Insbesondere bei Grundstuecksveraeusserungen und Heimvertraegen laeuft der Betreuer in eine Unwirksamkeitsfalle.
- Vermögensverzeichnis wird bei Amtsantritt vergessen oder unvollstaendig aufgestellt: Das Gericht kann spaeter keine Veraenderungen mehr nachvollziehen.
- Berufsrechtliche Konsequenzen von § 30 BtOG werden unterschaetzt: Ein Testament zugunsten des Betreuers ist zivilrechtlich nicht automatisch nichtig (OLG Nuernberg 19.07.2023), kann aber berufsrechtliche Folgen nach § 27 BtOG ausloesen.
- Subsidiaritaetsprinzip wird nicht geprueft: Wenn ein geeigneter Angehoeriger vorhanden ist, darf kein Berufsbetreuer bestellt werden.

## Quellen und Aktualitaet

- Stand: 06/2026
- BGB §§ 1814 ff. in der Fassung ab 01.01.2023 (BtOG-Reform)
- BtOG in der Fassung ab 01.01.2023
- VBVG in der aktuellen Fassung
- Aktuelle BGH-Rechtsprechung XII. Zivilsenat (verifiziert):
 - BGH 24.09.2025 - XII ZB 513/24 (Verhinderungsbetreuer; Vorrang Angehörigen-Wunsch; Amtsermittlung § 26 FamFG)
 - BGH 12.02.2025 - XII ZB 433/24 (Bestimmtheitsanforderungen an Beschluss zur medikamentösen Zwangsbehandlung; § 323 Abs. 1 Nr. 1 FamFG)
- Weitere Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle (bundesgerichtshof.de, dejure.org, openjur.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `betreuungsrechtliche-erstpruefung-und-mandatsziel`

_Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel im Betreuungsrecht._

# Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Betreuungsrechtliche Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Betreuungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Arbeitsfokus: **Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1814 Abs. 1 BGB` — Betreuungsvoraussetzungen.
- `§ 1815 Abs. 1 BGB` — Aufgabenkreis.
- `§ 1816 BGB` — Betreuerauswahl.
- `§ 1821 Abs. 1 BGB` — Wunschbefolgung.
- `§ 1823 BGB` — Vertretungsmacht.
- `§ 274 FamFG` — Beteiligte.
- `§ 278 FamFG` — Anhörung.
- `§ 280 FamFG` — Gutachten.
- `§ 5 BtOG` — Beratung.
- `§ 8 BtOG` — Betreuungsvermeidung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BtOG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Betreuungsrechtliche: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** BtOG, BGB, BtO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Betreuungsrechtliche** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `genehmigungspflicht-pruefung`

_'Prüft, ob ein konkretes Rechtsgeschäft, eine Maßnahme oder eine Entscheidung des Betreuers der Genehmigung des Betreuungsgerichts bedarf (§§ 1848 ff. BGB) — etwa Grundstücksverkauf, Erbausschlagung, Heimvertragsabschluss, Wohnungsauflösung, freiheitsentziehende Maßnahmen. Lädt, wenn Schlagwörter..._

# Genehmigungspflicht-Prüfung (§§ 1848 ff. BGB)

## Zweck

Prüfe, ob ein konkret geplantes Rechtsgeschäft oder eine
Maßnahme des Betreuers nach dem **Vier-Augen-Prinzip** der Genehmigung
des Betreuungsgerichts bedarf. Die Reform 2023 hat das System der
Genehmigungspflichten neu strukturiert (§§ 1848–1858 BGB für Vermögens-
sorge; §§ 1828–1834 BGB für personenbezogene Maßnahmen). Ohne
erforderliche Genehmigung sind Geschäfte schwebend unwirksam (§ 1855 BGB).

## Eingaben

- **Aufgabenkreise** des Betreuers (Bestellungsurkunde)
- **Konkret geplante Maßnahme** (z. B. "Verkauf der Eigentumswohnung der
 betreuten Person in Berlin-Charlottenburg")
- **Beteiligte Personen** (Vertragspartner, Heimträger, Arzt)
- **Wirtschaftliche Eckdaten** (Kaufpreis, Heimkosten, Darlehenssumme)
- **Wünsche/Willen der betreuten Person** zum Geschäft (§ 1821 BGB)
- **Vorhandensein einer Vorsorgevollmacht** (verdrängt ggf. Betreuung)

## Rechtlicher Rahmen

### Systematik der Genehmigungspflichten nach Reform 2023

Die §§ 1848–1858 BGB regeln **vermögensbezogene** Genehmigungspflichten:

- § 1848 BGB — Grundsatz: Genehmigung des Gerichts bei wesentlichen
 Vermögensverfügungen
- § 1849 BGB — Genehmigung bei Geschäften über Grundstücke und Rechte an
 Grundstücken
- § 1850 BGB — Genehmigung bei Erbschaftsangelegenheiten (Annahme/
 Ausschlagung der Erbschaft, Erbteilsverkauf)
- § 1851 BGB — Genehmigung bei Aufgabe/Auflösung der Wohnung der
 betreuten Person
- § 1852 BGB — Genehmigung bei Geschäften über erwerbsmäßige Tätigkeit
- § 1853 BGB — Genehmigung bei Kreditaufnahme, Verfügungen über Wertpapiere
- § 1854 BGB — Genehmigung bei Schenkungen (Ausschluss anstandspflichtiger
 Schenkungen)
- § 1855 BGB — Rechtsfolge: schwebende Unwirksamkeit ohne Genehmigung

### Personenbezogene Maßnahmen (§§ 1828–1834 BGB)

- § 1828 BGB — Einwilligung in ärztliche Maßnahmen
- § 1829 BGB — Genehmigung bei lebensgefährlichen oder schwer
 beeinträchtigenden ärztlichen Maßnahmen
- § 1831 BGB — Genehmigung **freiheitsentziehender Unterbringung**
 (geschlossene Heimunterbringung, geschlossene psychiatrische Klinik)
- § 1832 BGB — Genehmigung **freiheitsentziehender Maßnahmen** in offener
 Einrichtung (Bettgitter, Bauchgurt, sedierende Medikamente zur
 Bewegungseinschränkung)

### § 1855 BGB — Schwebende Unwirksamkeit

Rechtsgeschäfte ohne erforderliche Genehmigung sind **schwebend
unwirksam**. Die Genehmigung kann auch nachträglich erteilt werden. Wird
sie versagt, ist das Geschäft endgültig unwirksam. Der Vertragspartner kann
nach § 1856 BGB widerrufen.

### Kanonische Rechtsprechung (Stand 05/2026, Live-Verifikation vor Verwendung)

- BGH, Beschluss vom 12.02.2025 - XII ZB 433/24: Bei Genehmigung oder Anordnung einer medikamentösen Zwangsbehandlung muss der Entscheidungstenor das jeweilige Medikament/den Wirkstoff, die (Höchst-)Dosierung sowie die Verabreichungshäufigkeit hinreichend genau bezeichnen (§ 323 Abs. 1 Nr. 1 FamFG). Quelle: bundesgerichtshof.de / dejure.org.
- BGH, Beschluss vom 24.09.2025 - XII ZB 513/24: Wunsch des/der Betroffenen, durch nahe Angehörige betreut zu werden, hat Vorrang vor Berufsbetreuer; Amtsermittlungspflicht § 26 FamFG.
- Etablierte Linien (zu verifizieren): Bei freiheitsentziehender Unterbringung (§ 1831 BGB n.F.) enge Voraussetzungen — erhebliche Selbstgefährdung, medizinische Indikation, Verhältnismäßigkeit, kein milderes Mittel. SV-Gutachten regelmäßig erforderlich (§ 321 FamFG).
- Bei freiheitsentziehenden Maßnahmen in offener Einrichtung (§ 1832 BGB, vormals § 1906 Abs. 4 BGB a.F.): Bettgitter und Bauchgurt sind genehmigungspflichtig, wenn regelmäßig oder über längeren Zeitraum eingesetzt.
- Grundstücksverkauf (§ 1849 BGB): Verkehrswertnachweis durch qualifiziertes Gutachten/Maklerwertindikation; auffallend niedriger Kaufpreis löst Prüfungspflicht aus.
- Erbausschlagung (§ 1850 BGB): Gericht prüft wirtschaftliches Interesse der betreuten Person (Überschuldung, dingliche Lasten).

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

1. **Aufgabenkreis prüfen**
 Liegt die geplante Maßnahme überhaupt im übertragenen Aufgabenkreis?
 (Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung — § 1815 BGB).
 Fehlt der Aufgabenkreis, ist Erweiterung beim Gericht zu beantragen.

2. **Tatbestand der Genehmigungspflicht prüfen**
 Subsumtion unter konkreten §§ 1848 ff. BGB bzw. §§ 1831, 1832 BGB.

3. **Wunsch der betreuten Person ermitteln (§ 1821 BGB)**
 Auch bei genehmigungspflichtigen Geschäften ist der Wille der betreuten
 Person primärer Maßstab.

4. **Antrag beim Betreuungsgericht stellen**
 Schriftlich oder zur Niederschrift der Geschäftsstelle. Beizufügen:
 - Begründung der Maßnahme
 - Wirtschaftliche Eckdaten (Verkehrswertgutachten, Kostenvoranschlag)
 - Stellungnahme zum Willen der betreuten Person
 - Bei medizinischen Maßnahmen: ärztliches Zeugnis / Gutachten

5. **Anhörung durch das Gericht abwarten**
 Persönliche Anhörung der betreuten Person grundsätzlich Pflicht
 (§ 278 FamFG); bei Unterbringung Sachverständigengutachten
 zwingend (§ 321 FamFG).

6. **Genehmigungsbeschluss umsetzen**
 Geschäft erst nach Rechtskraft des Beschlusses vollziehen. Bei
 Grundstücken: Beschluss als Anlage zum Notarvertrag.

## Beispiel

**Sachverhalt:** Frau Hannelore K. (Heimbewohnerin, siehe Schwester-Skill)
wird zunehmend nachts unruhig, verlässt regelmäßig ihr Zimmer und gefährdet
sich durch Stürze. Die Pflegeheimleitung schlägt vor, nachts Bettgitter
anzubringen sowie ein leichtes Sedativum (Pipamperon 20 mg) zu verabreichen.

**Prüfung:**

> *2. Einschlägige Rechtsnorm:* § 1832 BGB — Genehmigung bei
> freiheitsentziehenden Maßnahmen in offener Einrichtung
>
> *3. Subsumtion:*
> - Maßnahme: Bettgitter + sedierende Medikation
> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
> Rn. 27 ff. — auch in offener Einrichtung)
> - Sedativum: Wenn primär zur Bewegungseinschränkung verabreicht
> (nicht therapeutisch), ebenfalls § 1832 BGB
> - Regelmäßigkeit: jede Nacht — Tatbestand erfüllt
>
> *4. Wille der betreuten Person:* Frau K. wurde am 18.02.2026 befragt
> (Aktenvermerk). Sie äußerte: "Ich will nicht eingesperrt sein, aber
> hinfallen will ich auch nicht." Bei eingeschränkter Einsichtsfähigkeit
> ist mutmaßlicher Wille zu erschließen — Schutz vor Sturzschäden hat
> Priorität.
>
> *5. Ergebnis:* genehmigungspflichtig. Antrag beim Betreuungsgericht
> Berlin-Spandau, AZ XVII 0234/24.
>
> *6. Anlagen:*
> - Ärztliches Zeugnis Dr. Petersen v. 02.03.2026 (Sturzgefahr)
> - Stellungnahme Pflegeheimleitung Sonnenhof
> - Aktenvermerk Anhörung Frau K. v. 18.02.2026
> - Prüfung milderer Mittel (Niedrigflurbett, Sturzmatte) — Stellungnahme

## Risiken und typische Fehler

**1. Genehmigung vor Vollzug einholen**
Geschäft erst nach Rechtskraft des Genehmigungsbeschlusses abschließen.
Vorzeitige Vollziehung führt zur schwebenden Unwirksamkeit (§ 1855 BGB).

**2. "Bettgitter sind keine Freiheitsentziehung"**
Verbreiteter Irrtum: Auch in offenen Einrichtungen sind Bettgitter und
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
24/12 Rn. 27 ff.). Einmalige kurzzeitige Maßnahme bei akuter Eigen-
gefährdung kann ohne Genehmigung erlaubt sein (Notstand).

**3. Heimvertrag**
Der Abschluss eines Heimvertrags durch den Betreuer ist regelmäßig **nicht**
nach § 1851 BGB genehmigungspflichtig, sondern Verwaltungsmaßnahme. Die
**Auflösung der bisherigen Wohnung** ist dagegen genehmigungspflichtig
(§ 1851 BGB), sofern Lebensmittelpunkt aufgegeben wird.

**4. Schenkung an Familie**
Schenkungen sind nach § 1854 BGB grundsätzlich genehmigungspflichtig.
Ausnahme: anstandsbedingte Gelegenheitsgeschenke (Geburtstag, Weihnachten)
in angemessenem Umfang.

**5. Erbausschlagung Frist**
Erbausschlagung ist binnen 6 Wochen nach Kenntnis vom Erbfall zu erklären
(§ 1944 BGB). Bei Genehmigungsbedürftigkeit (§ 1850 BGB) muss der Antrag
**innerhalb der Sechswochenfrist** beim Gericht eingehen; eine Hemmung
greift bei vorzeitiger Antragstellung.

**6. Verkehrswert nicht belegt**
Beim Grundstücksverkauf ist Verkehrswertgutachten oder Maklerwert-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Behauptungen genügen nicht.

**7. Vorsorgevollmacht verdrängt Betreuung**
Vor Antragstellung prüfen, ob eine wirksame Vorsorgevollmacht besteht
(§ 1820 BGB). Der Bevollmächtigte ist vorrangig zu beteiligen; Betreuung
ist subsidiär.

## Quellenpflicht

Bei jeder Ausgabe sind mindestens folgende Belege anzugeben:

- §§ 1848 ff. BGB, §§ 1831, 1832 BGB (einschlägige Rechtsnormen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; nur Nutzerquelle oder lizenzierte Live-Verifikation verwenden.

---
*Dieser Skill ersetzt keine konkrete fachliche Beratung im Einzelfall.
Vor jeder genehmigungspflichtigen Maßnahme ist der Antrag durch den
verantwortlichen Betreuer zu prüfen.*

---

## Skill: `jahresbericht-betreuungsgericht`

_Jahresbericht und Anfangs-/Schlussbericht für das Betreuungsgericht nach § 1863 BGB erstellen: persönliche Kontakte, Wünsche der betreuten Person, Ziele, Maßnahmen, Gründe für Fortbestand oder Änderung der Betreuung, Vermögens-Eckdaten und Anlagen. Für Berufsbetreuer ebenso wie ehrenamtliche Fami..._

# Jahresbericht des Betreuers ans Betreuungsgericht (§ 1863 BGB)

## Zweck

Unterstützt berufliche und ehrenamtliche Betreuerinnen und
Betreuer bei der Erstellung des **Jahresberichts an das Betreuungsgericht**
nach § 1863 Abs. 3 BGB sowie des **Anfangsberichts** nach § 1863 Abs. 1 BGB.
Aus einer Sammlung unsortierter Eingangsdaten — E-Mail-Verkehr mit Heimen,
Ärzten, Kostenträgern, Aktenvermerken über Besuche und Telefonate,
Arztbriefen, Heim- und Pflegeberichten, Kontoauszügen, Behördenpost —
generiert der Skill einen vollständigen, gerichtstauglich strukturierten
Bericht mit den nach § 1863 BGB zwingend vorgeschriebenen Abschnitten.

## Eingaben

- **Stammdaten der betreuten Person:** Name, Geburtsdatum, Anschrift,
 Aufenthaltsort (eigene Wohnung, Heim, Klinik), Aktenzeichen des
 Betreuungsgerichts, Anordnungsdatum und Aufgabenkreise (§ 1815 BGB)
- **Berichtszeitraum:** Berichtsbeginn und -ende (Anfangsbericht: ab
 Bestellung; Jahresbericht: 12 Monate; Schlussbericht: Ende der Betreuung)
- **Persönliche Kontakte:** Datum, Dauer, Ort und Inhalt jedes Besuchs oder
 Telefonats (§ 1821 Abs. 5 BGB — Pflicht zum persönlichen Kontakt)
- **Wohnsituation:** Wechsel der Wohnung, Heimaufnahme, Heimwechsel,
 Klinikaufenthalte
- **Gesundheitliche Situation:** Diagnosen (aktuelle Arztbriefe), Pflegegrad,
 Behandlungen, ärztliche Maßnahmen mit Einwilligungsbedarf (§§ 1828 ff. BGB)
- **Soziale Kontakte:** Familienangehörige, Freundeskreis, Ehrenamtliche
- **Vermögensentwicklung:** Eckdaten (Anfangsbestand, Endbestand,
 wesentliche Veränderungen) — Detailausweis erfolgt in der gesonderten
 Rechnungslegung (§ 1865 BGB)
- **Wünsche und Präferenzen der betreuten Person** (§ 1821 Abs. 2, 3 BGB —
 Vorrang der Wünsche)
- **Bestehender Anfangs- oder Vorjahresbericht** (zur Fortschreibung)

## Rechtlicher Rahmen

### § 1863 BGB — Berichtspflicht des Betreuers

**Abs. 1 — Anfangsbericht:** Der Betreuer hat unverzüglich nach Bestellung,
spätestens binnen drei Monaten, dem Betreuungsgericht über die persönlichen
Verhältnisse der betreuten Person, die zu erledigenden Aufgaben und die
geplante Ausgestaltung der Betreuung zu berichten.

**Abs. 2 — Inhalt des Anfangsberichts:**
1. die persönlichen Verhältnisse der betreuten Person,
2. die Wünsche der betreuten Person und die geplanten Maßnahmen zu ihrer
 Verwirklichung,
3. ggf. Gründe, weshalb Wünschen nicht entsprochen werden kann,
4. die geplante Ausgestaltung der persönlichen Betreuung, insbesondere die
 Häufigkeit persönlicher Kontakte.

**Abs. 3 — Jahresbericht:** Mindestens einmal jährlich hat der Betreuer dem
Betreuungsgericht über die persönlichen Verhältnisse der betreuten Person
sowie über die Ausführung der Betreuung zu berichten. Der Jahresbericht
enthält insbesondere:

1. eine Darstellung der persönlichen Verhältnisse der betreuten Person,
2. den Umfang und Inhalt der persönlichen Kontakte,
3. die Wünsche der betreuten Person und ihre Verwirklichung,
4. Mitteilung, ob Anlass besteht, die Betreuung aufzuheben oder den
 Aufgabenkreis (§ 1815 BGB) zu erweitern oder einzuschränken.

**Abs. 4 — Schlussbericht:** Bei Beendigung der Betreuung hat der Betreuer
einen Schlussbericht zu erstatten.

### § 1821 BGB — Pflichten des Betreuers; Wünsche der betreuten Person

Die Wünsche der betreuten Person sind **Maßstab** der Betreuung (§ 1821
Abs. 2 BGB). Der Betreuer darf nur dann von Wünschen abweichen, wenn die
betreute Person aufgrund ihrer Erkrankung oder Behinderung ihren Willen
nicht frei bilden kann **und** die Verwirklichung des Wunsches die Person
erheblich gefährden würde (§ 1821 Abs. 3 BGB).

§ 1821 Abs. 5 BGB statuiert die **Pflicht zum persönlichen Kontakt** —
der Betreuer hat die erforderlichen Angelegenheiten persönlich mit der
betreuten Person zu besprechen. Häufigkeit und Form sind im
Anfangs- und Jahresbericht darzustellen.

### § 1815 BGB — Aufgabenkreise

Aufgabenkreise sind nicht pauschal ("alle Angelegenheiten"), sondern
einzeln zu bestimmen. Übliche Aufgabenkreise:

- Vermögenssorge
- Gesundheitssorge
- Aufenthaltsbestimmung
- Wohnungsangelegenheiten
- Behörden- und Sozialleistungsangelegenheiten
- Vertretung gegenüber Heim/Pflegeeinrichtung
- Postangelegenheiten (§ 1815 Abs. 2 Nr. 3 BGB — gesonderter Beschluss)

### § 9 BtOG — Berufliche Betreuung

Berufsbetreuer benötigen Registrierung nach § 23 BtOG und Sachkundenachweis
nach § 24 BtOG. Die Berichtspflichten gelten unverändert; für Berufsbetreuer
gilt zusätzlich der Vergütungsanspruch nach § 7 VBVG (pauschalierte
Stundensätze nach Vergütungstabelle).

### Berichtsqualität

Der Bericht ist Grundlage der gerichtlichen Aufsicht (§ 1862 BGB). Er soll so
konkret sein, dass das Gericht erkennen kann, ob die Betreuung ordnungsgemäß
geführt wird, ob die Aufgabenkreise noch passen und ob die Wünsche der
betreuten Person beachtet werden. Pauschale Sätze wie "keine Besonderheiten"
oder "es geht gut" genügen nicht.

Für persönliche Kontakte gilt: Datum, Ort, Dauer, Beteiligte, eigener Eindruck
und besprochene Wünsche festhalten. Telefonate und Videogespräche können
ergänzen; bei Konflikt, Pflegeheim, Gesundheitsrisiko oder Vermögensrisiko
braucht der Bericht erkennbar einen belastbaren eigenen Eindruck.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Eingabesichtung und Kategorisierung**
 Der Skill sichtet alle eingegebenen Dokumente (E-Mails, Aktenvermerke,
 Arztbriefe, Heimberichte, Kontoauszüge, Behördenpost) und ordnet sie
 einem der vier Pflichtabschnitte des § 1863 Abs. 3 BGB zu: persönliche
 Verhältnisse, persönliche Kontakte, Wünsche, Anlass zur Änderung.

2. **Persönliche Verhältnisse darstellen**
 - Wohnsituation (eigene Wohnung / Heim — mit Namen der Einrichtung,
 Aufnahmedatum, Pflegegrad)
 - Gesundheitlicher Zustand (aktuelle Diagnosen, Veränderungen im
 Berichtszeitraum, Klinikaufenthalte)
 - Soziales Umfeld (Angehörige, Freundeskreis, ehrenamtliche Helfer)
 - Wirtschaftliche Verhältnisse in Eckdaten (Anfangs-/Endvermögen,
 Sozialleistungsbezug)
 - Berufliche oder ehrenamtliche Tätigkeit, Beschäftigung

3. **Persönliche Kontakte tabellarisch belegen**
 Pro Kontakt: Datum, Dauer, Ort, kurze Inhaltsangabe, eigener Eindruck,
 Wunschbezug und offene Folgeaufgabe. Bei Heimbewohnern Kontakte nicht nur
 aus Heimberichten ableiten.

4. **Wünsche und ihre Verwirklichung**
 - Wünsche der betreuten Person (geäußert oder erschlossen aus früheren
 Willensbekundungen, Patientenverfügung, Vorsorgevollmacht)
 - Maßnahmen des Betreuers zur Verwirklichung
 - Bei Abweichung: Begründung (§ 1821 Abs. 3 BGB — erhebliche
 Gefährdung)

5. **Anlass zur Änderung der Betreuung prüfen**
 - Sind alle Aufgabenkreise weiter erforderlich? (Verhältnismäßigkeit,
 § 1814 Abs. 3 BGB)
 - Sind weitere Aufgabenkreise erforderlich geworden?
 - Lässt sich die Betreuung aufheben (z. B. wegen Vorsorgevollmacht
 oder Genesung)?

6. **Vermögensentwicklung — Eckdaten**
 Bei Vermögenssorge: kurze Eckdaten (Anfangsbestand, Endbestand, große
 Veränderungen). Die detaillierte **Rechnungslegung** erfolgt gesondert
 nach § 1865 BGB (vereinfachte Rechnungslegung für Familienangehörige
 nach § 1859 BGB ggf. möglich).

7. **Anlagen zusammenstellen**
 Aktuelle Arztbriefe (sofern für Bericht relevant), Heim-/Pflegebericht
 (sofern vorhanden), gegebenenfalls Patientenverfügung, Vorsorgevollmacht,
 Schreiben mit Wunschäußerungen der betreuten Person.

## Ausgabeformat

Strukturierter Berichtstext mit folgenden Abschnitten (entsprechend
§ 1863 Abs. 3 BGB):

```
An das Amtsgericht – Betreuungsgericht – [Ort]
Aktenzeichen: [XVII … / …]

Jahresbericht des Betreuers nach § 1863 Abs. 3 BGB
Berichtszeitraum: [TT.MM.JJJJ – TT.MM.JJJJ]

Betreute Person: [Name, Vorname]
Geboren: [TT.MM.JJJJ]
Anschrift: [Aktueller Aufenthaltsort, Einrichtung]
Bestellung: [TT.MM.JJJJ]
Aufgabenkreise: [Aufzählung gem. § 1815 BGB]

1. Persönliche Verhältnisse der betreuten Person
 1.1 Wohnsituation
 1.2 Gesundheitlicher Zustand
 1.3 Soziales Umfeld
 1.4 Wirtschaftliche Verhältnisse (Eckdaten)

2. Persönliche Kontakte im Berichtszeitraum
 Tabellarische Aufstellung: Datum | Ort | Dauer | Inhalt
 Gesamtfrequenz: [n Besuche, n Telefonate]

3. Wünsche der betreuten Person und ihre Verwirklichung
 3.1 Geäußerte oder erschlossene Wünsche
 3.2 Umgesetzte Maßnahmen
 3.3 Ggf. Abweichungen und deren Begründung (§ 1821 Abs. 3 BGB)

4. Anlass zur Änderung der Betreuung
 [Aufhebung / Erweiterung / Einschränkung / kein Anlass]

5. Vermögensentwicklung (Eckdaten)
 Anfangsbestand: [Datum, Betrag]
 Endbestand: [Datum, Betrag]
 Wesentliche Veränderungen:
 Gesonderte Rechnungslegung nach § 1865 BGB: beigefügt / folgt am …

6. Anlagen
 [Liste]

Ort, Datum [Name, Unterschrift Betreuer/in]
 Betreuer/in
 ggf. Registrierungs-Nr. bei Berufsbetreuung
```

## Beispiel

**Eingabe (Auszug, pseudonymisiert):**

- Betreuung Frau Hannelore K., geb. 14.03.1942, AZ XVII 0234/24
- Aufgabenkreise: Vermögenssorge, Gesundheitssorge, Aufenthaltsbestimmung,
 Vertretung gegenüber Heim, Postangelegenheiten
- Berichtszeitraum: 01.06.2025 – 31.05.2026
- E-Mails: 12 mit Heimleitung Sonnenhof Berlin-Spandau, 4 mit Hausarzt
 Dr. Petersen, 8 mit Rentenversicherung
- Aktenvermerke: 6 Besuche im Heim (jeweils ca. 60 Min), 14 Telefonate
- Arztbriefe: Kardiologie Vivantes Spandau v. 12.09.2025 (Vorhofflimmern,
 Antikoagulation eingeleitet); Allgemeinmedizin Petersen v. 02.03.2026
- Heimrechnung: Pflegegrad 4, Eigenanteil 2.341 EUR/Monat, Sozialhilfe ergänzt
- Kontoauszüge: Anfangsbestand 18342.12 EUR, Endbestand 16108.77 EUR
- Wunschäußerung Frau K. (Vermerk v. 24.11.2025): "Möchte am Heiligabend
 bei Tochter Susanne in Potsdam sein" — umgesetzt durch Abholfahrt am
 24.12.2025

**Ausgabe (Auszug Abschnitt 2):**

> *2. Persönliche Kontakte im Berichtszeitraum*
>
> Im Berichtszeitraum fanden 6 persönliche Besuche und 14 Telefonate statt.
> Die Besuche erfolgten jeweils im Pflegeheim Sonnenhof, Berlin-Spandau.
>
> | Datum | Ort | Dauer | Inhalt |
> |---|---|---|---|
> | 18.06.2025 | Sonnenhof, Spandau | 65 Min | Vorstellungsgespräch, Erfassung Wünsche |
> | 12.09.2025 | Sonnenhof, Spandau | 50 Min | Besprechung Vorhofflimmern-Diagnose, Einwilligung Antikoagulation |
> | 24.11.2025 | Sonnenhof, Spandau | 55 Min | Erörterung Weihnachtsbesuch bei Tochter |
> | 18.02.2026 | Sonnenhof, Spandau | 60 Min | Pflegegrad-Höherstufung 4, Eigenanteilsfinanzierung |
> | … | … | … | … |
>
> Persönliche Kontakte wurden mit Datum, Ort, Dauer und Inhalt dokumentiert.
> Telefonate und Videogespräche können den persönlichen Eindruck ergänzen,
> ersetzen ihn aber in konflikt- oder risikoreichen Situationen nicht.

## Risiken und typische Fehler

**1. Pauschale Formulierungen**
"Frau K. geht es gut, keine Besonderheiten" genügt nicht. Der Bericht muss
substantiiert die persönlichen Verhältnisse darstellen, damit das Gericht
Aufsicht, Erforderlichkeit und Aufgabenkreise prüfen kann.

**2. Persönliche Kontakte zu selten dokumentiert**
Jeder relevante Kontakt ist mit Datum, Ort, Dauer und Inhalt zu dokumentieren.
Bei Heimbewohnern, Krankheit, Konflikten oder Vermögensrisiken muss der Bericht
erkennen lassen, wie sich der Betreuer einen eigenen Eindruck verschafft hat.

**3. Wünsche nicht eigenständig ermittelt**
Der Bericht muss erkennen lassen, wie der Betreuer die Wünsche der
betreuten Person ermittelt hat (Gespräch, Anhörung, Patientenverfügung).
Die bloße Aussage "Die Betreute hat keine Wünsche geäußert" ist
unzureichend, wenn nicht erkennbar ist, ob der Betreuer aktiv gefragt hat
oder welche Kommunikationshilfen versucht wurden.

**4. Vermischung Bericht und Rechnungslegung**
Der Jahresbericht (§ 1863 BGB) und die Rechnungslegung (§ 1865 BGB) sind
**zwei verschiedene Dokumente**. Im Bericht genügen Vermögens-Eckdaten;
die detaillierte Rechnungslegung mit Belegen wird gesondert eingereicht.

**5. Fristen versäumt**
- Anfangsbericht: binnen 3 Monaten nach Bestellung
- Jahresbericht: jährlich, im vom Gericht festgesetzten Turnus
- Schlussbericht: unverzüglich nach Ende der Betreuung
Fristversäumnis kann zur Anhörung, im Wiederholungsfall zur Entlassung
des Betreuers nach § 1868 BGB führen.

**6. Datenschutz bei KI-Nutzung**
Berichte enthalten besondere Kategorien personenbezogener Daten (Art. 9
DSGVO: Gesundheitsdaten) sowie Sozialdaten. Vor Übergabe an externe
KI-Systeme sind Daten zu pseudonymisieren (siehe Skill
`playbook-aus-eigenen-daten` im Plugin `kanzlei-builder-hub`). Berufliche
Schweige-, Datenschutz- und Vertraulichkeitspflichten sind je nach Rolle und
Konstellation gesondert zu prüfen.

**7. Beendigungsanlass nicht geprüft**
§ 1863 Abs. 3 Nr. 4 BGB verlangt ausdrücklich die Mitteilung, ob Anlass
zur Aufhebung, Erweiterung oder Einschränkung besteht. Dieser Abschnitt
darf nie fehlen; er bewirkt die Verhältnismäßigkeitskontrolle nach
§ 1814 Abs. 3 BGB.

**8. Aufgabenkreis "Postangelegenheiten" / "Postkontrolle"**
Wegen Eingriff in Art. 10 GG nur bei gesondertem gerichtlichen Beschluss
(§ 1815 Abs. 2 Nr. 3 BGB). Im Bericht ist Notwendigkeit fortlaufend zu
begründen.

## Quellenpflicht

Bei jeder Ausgabe sind mindestens folgende Belege anzugeben:

- § 1863 BGB (Berichtspflicht) und § 1821 BGB (Wünsche, persönlicher Kontakt)
- Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

---
*Dieser Skill ersetzt keine konkrete fachliche Beratung im Einzelfall.
Vor Einreichung beim Betreuungsgericht ist der Bericht durch den
verantwortlichen Betreuer eigenständig zu prüfen.*

---

## Skill: `kaltstart-interview`

_Kaltstart-Interview für das Betreuungsrecht-Plugin. Befüllt das Praxisprofil mit Angaben zur Rolle (betreute Person / Angehöriger / ehrenamtlicher Familienbetreuer / Berufsbetreuer / Vereinsbetreuer / Behördenbetreuer / anwaltliche Begleitung), Betreuungsgericht, Aufgabenkreisen, Unterstützungsst..._

# /betreuungsrecht:betreuungsrecht-kaltstart-interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Betreuungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Ablauf

1. Zustand der Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md` prüfen.
2. Falls vorhanden und ohne `[PLATZHALTER]`-Marker: bestätigen, dass das Praxisprofil schon befüllt ist, und Modus erfragen (`--redo` für vollständiges Neu-Interview).
3. Falls nicht vorhanden oder mit Platzhaltern: das Kaltstart-Interview unten durchführen.
4. Konfigurationsdatei schreiben (übergeordnete Verzeichnisse bei Bedarf anlegen).
5. Zusammenfassung anzeigen und nächste Schritte vorschlagen.

## `--integrationen-prüfen`

Prüft die Konnektoren-Verfügbarkeit (Dokumentenspeicher, E-Mail-System für Betreuungsbehörde-Kommunikation, Kalender für Anhörungs-/Berichtstermine). Aktualisiert nur den Abschnitt `## Verfügbare Integrationen`, führt kein neues Interview durch.

Beim Prüfen: nur `✓` melden, wenn ein MCP-Tool-Aufruf tatsächlich erfolgreich war. Konfigurierte-aber-ungetestete Konnektoren als `⚪` markieren.

---

## Kaltstart-Interview: Betreuungsrecht

### 1. Wer nutzt dieses Plugin?

- **Rolle:** betreute Person / Angehöriger / ehrenamtlicher Familienbetreuer / ehrenamtlicher Betreuer ohne persönliche Bindung / Berufsbetreuer / Vereinsbetreuer / Behördenbetreuer / Anwalt mit Betreuungsmandaten?
- **Status:** Schon bestellt, nur vorgeschlagen, eigene Anregung läuft, einstweilige Anordnung oder bloße Vorsorgefrage?
- **Anwaltlicher Ansprechpartner** (falls vorhanden): Name, Kanzlei, Erreichbarkeit
- **Berufsverband:** BdB, VfB, VGT, sonstiger oder keiner
- **Unterstützungsstellen:** zuständige Betreuungsbehörde, Betreuungsverein, Betreuungsgericht, ggf. Verhinderungsbetreuung

### 2. Aktuelle Betreuungen

- **Anzahl aktiver Betreuungen:** N; bei Familienbetreuern meist eine konkrete Betreuung, bei Berufsbetreuern Praxisumfang gesondert erfassen.
- **Typische Aufgabenkreise:** Vermögenssorge / Gesundheitssorge / Aufenthaltsbestimmung / Wohnungsangelegenheiten / Postangelegenheiten / Behördenangelegenheiten
- **Zuständige Betreuungsgerichte:** Hauptgericht + weitere
- **Wünsche der betreuten Person:** bekannte Wünsche, frühere Äußerungen, Patientenverfügung, Vorsorgevollmacht, Betreuungsverfügung
- **Dringende Alltagsthemen:** Bank, Miete/Heim, Pflege, Arzt, Bescheide, Schulden, Telefonbetrug, Angehörigenkonflikt

### 3. Berichtswesen

- **Berichtsformat:** Anfangs-/Jahres-/Schlussbericht nach § 1863 BGB; bei Vermögenssorge zusätzlich Vermögensverzeichnis nach § 1835 BGB und Vermögens-/Rechnungslegung nach gerichtlicher Vorgabe.
- **Berichtsturnus:** Standardmäßig jährlich; bei großem Vermögen ggf. abweichend
- **Vorlagen vorhanden:** ja / nein, Ablageort
- **Kalender/Reminder:** gewünschtes System: Papierkalender, Outlook, Apple Kalender, Excel, Aufgabenliste, keine Integration.

### 4. Genehmigungspflichtige Geschäfte

Bekannte Bereiche, in denen regelmäßig Genehmigungen erforderlich sind:
- Grundstücksgeschäfte (§ 1850 BGB)
- Erbschaftsausschlagung (§ 1851 BGB)
- Aufgabe oder Kündigung selbstgenutzten Wohnraums (§ 1833 BGB)
- Freiheitsentziehende Maßnahmen (§ 1831 BGB)
- Sterilisation (§ 1830 BGB)
- Risikoreiche Heilbehandlung (§ 1829 BGB)

### 5. Eskalation

- **Wer hilft bei rechtlich kritischen Fragen?** Betreuungsverein / Betreuungsbehörde / Betreuungsgericht / Anwalt / Notar / Pflegeberatung
- **Wann wird das Betreuungsgericht informiert?** Bei jedem genehmigungspflichtigen Geschäft, bei wesentlichen Statusänderungen, bei vermutetem Missbrauch
- **Überforderungsschwelle:** Welche Themen soll das System rot markieren, damit nicht allein entschieden wird?

### 6. Standort und Sprachen

- **Bundesland / Betreuungsgerichtsbezirk:** [Bayern / NRW / etc.]
- **Sprachkenntnisse der Betreuten:** Deutsch / weitere

---

## Ausgabe

Das Praxisprofil wird in `~/.claude/plugins/config/claude-fuer-deutsches-recht/betreuungsrecht/CLAUDE.md` geschrieben. Anschließend zeigen:

- Was eingerichtet wurde (Zusammenfassung der Antworten)
- Welche Skills jetzt sinnvoll als nächstes laufen können:
 - `/betreuungsrecht:vermögensverzeichnis-prüfung` — bei Eröffnung einer Betreuung
 - `/betreuungsrecht:genehmigungspflicht-prüfung` — vor wesentlichen Geschäften
 - `/betreuungsrecht:jahresbericht-betreuungsgericht` — bei jährlicher Berichtspflicht
 - `/betreuungsrecht:ehrenamtlicher-betreuer-erster-monat` — bei familiärer oder ehrenamtlicher Erstbetreuung
 - `/betreuungsrecht:dokumentenscan-aktenablage-und-belegmappe` — bei unsortierten Scans, Fotos und Bescheiden
 - `/betreuungsrecht:kalender-reminder-und-fristenmanagement` — für Berichtspflichten, Bescheidfristen und Routinekontakte
- Hinweis auf Datenschutz, Vertraulichkeit und sparsame Verarbeitung sensibler Gesundheits- und Vermögensdaten

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtlicher Rahmen

- **§ 1814 ff. BGB** — Betreuungsrecht (seit 01.01.2023 reformiert)
- **§ 1821 BGB** — Pflichten des Betreuers und Wünsche der betreuten Person
- **§§ 1829–1832 BGB** — Genehmigungspflichten
- **VBVG** — Vergütung Berufsbetreuer
- **BtOG** und **BtRegV** — Organisation, Registrierung beruflicher Betreuer und Unterstützung ehrenamtlicher Betreuer
- **FamFG §§ 271–341** — Verfahrensrecht Betreuungssachen

## Hinweise

Dieses Plugin ersetzt keine anwaltliche Beratung. Zitate aus Trainingsdaten sind vor Verwendung gegen Primärquellen (amtliche/freie Quellen oder lizenzierte Datenbanken bei vorhandenem Zugang, Gesetze im Internet) zu prüfen.

---

## Skill: `kontodaten-vertragsverdacht-pruefung`

_Kontoauszüge und Vertragsunterlagen in Betreuungsfällen auf Missbrauch prüfen: ungewöhnliche Zahlungen, verdächtige Dauerverträge, Fernwartung, Telefonbetrug, riskante Anlagen, Angehörigendruck und Auslandsüberweisungen zum Nachteil der betreuten Person. Prüft Aufgabenkreis, Wunschlage (§ 1821 BG..._

# Kontodaten- und Vertragsverdacht-Prüfung

Anwendungsfall in der Betreuung: kontoauszüge, Vertragsunterlagen,
Rechnungen oder Belege darauf geprüft werden sollen, ob Geldabflüsse,
Dauerverträge, Anlagegeschäfte oder sonstige Rechtsgeschäfte für die betreute
Person auffällig, schädlich oder betreuungsgerichtlich relevant sind.

Der Skill ist forensisch, aber nicht voreilig: Er trennt Tatsachen,
Verdachtsmomente, offene Beweise und rechtliche Erstmaßnahmen. Er entscheidet
nicht selbst über Geschäftsfähigkeit, Einwilligungsvorbehalt, Anfechtung,
Genehmigung oder Strafbarkeit, sondern bereitet diese Prüfungen sauber vor.

## Triage — kläre vor Kontodaten-Prüfung
1. Ist Vermögenssorge als Aufgabenkreis im Betreuungsbeschluss enthalten? Ohne diese kein Handlungsrecht.
2. Besteht Einwilligungsvorbehalt (§ 1825 BGB) oder wurde er beim Gericht angeregt?
3. Liegt akuter Missbrauchs-Verdacht vor — dann sofort Gericht informieren, ggf. einstweilige Massnahme (§ 300 FamFG)?
4. Frist für SEPA-Widerruf (8 Wochen für autorisierte Zahlung, 13 Monate für nicht-autorisierte) — bereits abgelaufen?
5. Strafanzeige (§§ 263, 266 StGB) erwägen wenn konkrete Fremdeinwirkung auf Konto erkennbar.

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingangsdaten

Frage zu Beginn knapp nach:

- Betreuungsbeschluss, Datum, Gericht, Aktenzeichen und Aufgabenkreis,
 insbesondere Vermögenssorge, Behördenangelegenheiten, Post,
 Wohnungsangelegenheiten und Gesundheitsfürsorge.
- Zeitraum der Kontoauszüge und betroffene Konten.
- Vorliegende Verträge, Rechnungen, SEPA-Mandate, Vollmachten,
 Fernwartungsunterlagen, Gesprächsnotizen und Bankkorrespondenz.
- Bekannte Wünsche der betreuten Person, Lebensstandard, bisherige Gewohnheiten
 und Vertrauenspersonen.
- Ob bereits Einwilligungsvorbehalt, Sperrvermerk, Bankwarnung,
 Strafanzeige, Widerruf, Kündigung oder Rückbuchung veranlasst wurde.

## Leitplanken

1. **Wunsch und Schutz trennen.** Nach § 1821 BGB sind Wünsche der betreuten
 Person ernst zu nehmen. Auffälligkeit allein ersetzt keine Prüfung, ob die
 Ausgabe gewollt, lebenspraktisch sinnvoll oder nur schlecht dokumentiert ist.
2. **Aufgabenkreis prüfen.** Ohne passende Vermögenssorge oder Vertretungsmacht
 nur vorbereiten, sichern und gerichtliche Klärung vorschlagen.
3. **Keine Bankdaten verändern.** Kontoauszüge werden nur gelesen und
 strukturiert. Originaldateien bleiben unverändert.
4. **Beweise erhalten.** Verträge, Telefonnotizen, Fernwartungsprotokolle,
 E-Mails, SEPA-Mandate, Überweisungsbelege und Versandnachweise separat
 sichern.
5. **Fristen markieren.** Widerruf, Anfechtung, SEPA-Rückgabe, Kündigung,
 Verjährung, Beschwerde und betreuungsgerichtliche Genehmigung immer mit
 Friststatus ausweisen.

## Prüfschritte

### 1. Kontobaseline bilden

Erstelle zuerst eine nüchterne Tabelle:

| Feld | Inhalt |
| --- | --- |
| Zeitraum | Von/bis der Kontoauszüge |
| Anfangsbestand | Betrag und Datum |
| Endbestand | Betrag und Datum |
| Regelmäßige Einnahmen | Rente, Miete, Pflegegeld, Erstattungen |
| Notwendige Ausgaben | Miete, Energie, Krankenversicherung, Heim, Lebensmittel |
| Freier Betrag | Plausibler monatlicher Spielraum |
| Auffällige Saldenbrüche | Rechenfehler, unerklärte Sprünge, nicht passende Jahresabschlüsse |

Wenn Jahresabschluss, Kontosaldo und Einzelbuchungen nicht zusammenpassen,
kennzeichne das als eigenes Beweisthema und fordere Bankklärung an.

### 2. Dauerpositionen und Verträge clustern

Ordne jede wiederkehrende Zahlung einer Kategorie zu:

- **Lebensführung:** Miete, Nebenkosten, Strom, Gas, Telekommunikation,
 Krankenversicherung, Pflege, Hausverwaltung, Rundfunkbeitrag.
- **Plausibel, aber belegpflichtig:** Haushaltshilfe, private Pflegehilfe,
 Fahrdienste, Handwerker, medizinische Selbstzahlerleistungen.
- **Prüfbedürftig:** Lotterie, Dating-/Kontaktportale, Abos,
 Sicherheitsdienste, Fernwartung, Seniorenprodukte, Haustürgeschäfte.
- **Rot:** angebliche Behörden-/Polizeizahlungen, Auslandstransfers,
 Hochrisikoanlagen, Edelmetall/Diamanten, Immobilienreservierungen,
 komplexe Beteiligungen, Zahlungen nach Telefonanweisung.

### 3. Verdachtsscoring

Bewerte jede Position mit niedrig, mittel, hoch oder akut.

Akut ist regelmäßig anzunehmen bei:

- Zahlung an angebliche Polizei, Europol, Staatsanwaltschaft, Bank-Sicherheit
 oder ähnliche Autoritätskulisse.
- Fernwartung oder Sicherheitssoftware mit Zugang zum Rechner der betreuten
 Person, besonders bei weiteren Bank- oder Anlagezahlungen.
- Auslandsüberweisung ohne plausible Dokumentation.
- Vermögensanlage, Immobilienreservierung oder Gesellschaftsbeteiligung bei
 unklarer Geeignetheit, hoher Bindung oder Totalverlustrisiko.
- Ketten von Seniorenprodukten, Lotterie, Kontaktportal oder ähnlichen
 wiederholten Ansprachemustern.

Mittel ist anzunehmen bei:

- Ungewöhnlich hohen Einzelkäufen ohne Bedarfsermittlung.
- Wiederkehrenden Zahlungen ohne Vertrag oder ohne Kündigungsdaten.
- Privaten Hilfezahlungen ohne Quittung, Vertrag oder Leistungsnachweis.

Niedrig ist anzunehmen bei:

- Üblichen Haushaltspositionen mit Vertrag, marktüblichem Betrag und
 nachvollziehbarem Nutzen.

### 4. Rechts- und Genehmigungsfilter

Prüfe als Filter, nicht als Endgutachten:

- **§ 1814 BGB:** Warum ist rechtliche Betreuung erforderlich und welcher
 konkrete Aufgabenkreis trägt die Prüfung?
- **§ 1821 BGB:** Welche Wünsche, Werte und Gewohnheiten der betreuten Person
 sind bekannt? Wo droht erhebliche Selbstschädigung?
- **§ 1825 BGB:** Ist ein Einwilligungsvorbehalt anzuregen, wenn erhebliche
 Vermögensgefährdung durch wiederholte Geschäfte besteht?
- **§ 1835 BGB:** Müssen Positionen im Vermögensverzeichnis, als Forderung,
 als Anlage oder als zweifelhafte Vermögensminderung erfasst werden?
- **§ 1865 BGB:** Welche Belege braucht die Rechnungslegung?
- **§§ 1848 ff. BGB:** Ist bei Grundstücken, Gesellschaftsbeteiligungen,
 Darlehen, riskanten Anlagen oder ähnlichen Geschäften eine
 Genehmigungsprüfung nötig?

### 5. Maßnahmenplan

Erstelle eine priorisierte Liste:

| Priorität | Maßnahme | Zweck | Frist | Adressat | Nachweis |
| --- | --- | --- | --- | --- | --- |
| sofort | Konto- und Onlinebanking-Sicherung | weiteren Abfluss stoppen | heute | Bank | Aktenvermerk |
| sofort | Fernwartung sperren | Zugriff beenden | heute | Anbieter/IT | Protokoll |
| kurzfristig | SEPA-Mandate prüfen | Rückgabe/Kündigung | 1 bis 3 Tage | Bank/Anbieter | Buchungsbeleg |
| kurzfristig | Verträge kündigen/widerrufen/anfechten prüfen | laufende Kosten stoppen | Frist prüfen | Anbieter | Schreiben |
| kurzfristig | Betreuungsgericht informieren | Schutzmaßnahme legitimieren | bei akutem Risiko | Gericht | Bericht |
| danach | Rückforderungs- und Schadensersatzspur | Vermögen mehren | nach Beweissicherung | Anbieter/Bank/Dritte | Anspruchsmemo |

## Beispielakte Schmalfeld

Die Testakte `testakten/betreuung-schmalfeld-kontodaten-vertraege/` enthält
Kontoauszüge 2023 bis 2025, Vertragsunterlagen und eine vorbereitete
Verdachtsliste. Erwartete Kernbefunde:

- Der Rentner Herbert Wilhelm Schmalfeld hat hohe und wiederholte Abflüsse an
 Lotterie, Fernwartung, Sicherheitssoftware, Auslandsvermögensverwaltung,
 Beteiligung, Immobilienreservierung, Edelmetall, Diamant und angebliche
 Sicherheitskautionen.
- Fernwartung und Sicherheitssoftware bilden ein eigenes Schutzthema, weil
 technischer Zugriff und Bank-/Anlageabflüsse zusammenfallen können.
- Die privaten Pflege-/Haushaltshilfezahlungen an Svetlana Petrova sind nicht
 automatisch verdächtig, aber beleg- und plausibilisierungsbedürftig.
- Die Jahresabschlüsse und Salden müssen rechnerisch mit der Bank geklärt
 werden, bevor Beträge in ein Vermögensverzeichnis oder eine
 Rechnungslegung übernommen werden.

Optional kann das Hilfsskript genutzt werden:

```bash
python betreuungsrecht/scripts/betreuung_konto_vertragscheck.py \
 testakten/betreuung-schmalfeld-kontodaten-vertraege/05_schmalfeld_verdaechtige_transaktionen.json
```

---

## Skill: `vermoegensverzeichnis-pruefung`

_Vermögensverzeichnis für Betreuung prüfen und erstellen: Betreuer muss bei Aufgabenkreis Vermögenssorge nach § 1835 BGB ein Vermögensverzeichnis aufnehmen oder ein bestehendes Verzeichnis auf Vollständigkeit und Richtigkeit prüfen. Berücksichtigt Trennungsgebot (§ 1836 BGB), Belege, Konten, Immob..._

# Vermögensverzeichnis und Rechnungslegung (§§ 1835, 1839, 1865 BGB)

## Zweck

Unterstützt den rechtlichen Betreuer mit Aufgabenkreis
Vermögenssorge bei der **Erstellung des Anfangs-Vermögensverzeichnisses**
nach § 1835 Abs. 1 BGB (bei Übernahme der Betreuung), der laufenden
Verwaltung mündelsicher angelegten Vermögens nach § 1839 BGB sowie der
**jährlichen Rechnungslegung** nach § 1865 BGB.

## Eingaben

- Datum der Bestellung (Beginn der Vermögenssorge)
- Bisheriger Betreuer (falls Wechsel) — dessen Schlussrechnung als Eingabe
- Liste aller Konten der betreuten Person (Girokonto, Sparkonten,
 Tagesgeld, Festgeld, Depots) mit IBAN, Stand zum Bestellungstag
- Immobilieneigentum (Grundbuchauszug)
- Bewegliche Sachen von Wert (Schmuck, Kunst, Fahrzeug)
- Forderungen und Verbindlichkeiten (offene Rechnungen, Darlehen,
 Bürgschaften, Erbansprüche)
- Sozialleistungsbescheide (Rente, Grundsicherung, Pflegekasse,
 Hilfe zur Pflege § 61 SGB XII)
- Versicherungspolicen (Lebensversicherung, Sterbegeld, Rechtsschutz)
- Wiederkehrende Einnahmen und Ausgaben (Renten, Mieten, Heimkosten)

## Rechtlicher Rahmen

### § 1835 BGB — Vermögensverzeichnis

**Abs. 1:** Der Betreuer hat unverzüglich nach Übernahme der Betreuung
ein Verzeichnis des seiner Verwaltung unterliegenden Vermögens beim
Betreuungsgericht einzureichen.

**Abs. 2:** Das Verzeichnis muss vollständig sein und mit der Versicherung
der Richtigkeit und Vollständigkeit versehen werden.

**Abs. 3:** Bei nachträglich erworbenem Vermögen (Erbschaft, Schenkung,
Lottogewinn) ist das Verzeichnis zu ergänzen.

### § 1839 BGB — Mündelsichere Anlage

Der Betreuer hat das Geld der betreuten Person, soweit es nicht zur
Bestreitung der laufenden Ausgaben benötigt wird, **verzinslich anzulegen**.
Die Anlage ist auf den Namen der betreuten Person bei einem Kreditinstitut
vorzunehmen, das einer Einlagensicherungseinrichtung angehört (§ 1841 BGB).

**Sperrvermerk (§ 1845 BGB):** Bei größerem Vermögen ordnet das Gericht
regelmäßig die Anlage mit Sperrvermerk an. Verfügungen sind dann nur mit
gerichtlicher Genehmigung möglich. Die Schwelle wird in der Praxis je nach
Gericht zwischen 3.000 und 6.000 EUR Sockelbetrag (Schonvermögen) gezogen.

### § 1865 BGB — Rechnungslegung

**Abs. 1:** Der Betreuer hat jährlich, jeweils zum Ende des
Berichtszeitraums, Rechnung zu legen.

**Abs. 2:** Die Rechnung muss eine geordnete Übersicht der Einnahmen und
Ausgaben enthalten. Belege sind beizufügen, soweit sie nicht ausnahmsweise
entbehrlich sind.

**Abs. 3:** Bei nahen Angehörigen als Betreuer kann das Gericht
vereinfachte Rechnungslegung gestatten (§ 1859 BGB).

### § 1841 BGB — Anlage bei Bank

Der Betreuer hat Gelder verzinslich bei einem Kreditinstitut anzulegen,
das einer Einlagensicherung angehört.

### Kanonische Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Das Vermögensverzeichnis muss alle vermögensrechtlich relevanten
Positionen aufführen. Fahrzeugen, Schmuck und sonstigen beweglichen
Sachen sind mit Schätzwert anzugeben; pauschale Auslassungen sind
unzureichend.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Die Rechnungslegung muss in **kontinuierlicher** Buchführung erfolgen.
Eine einmal jährliche zusammenfassende Aufstellung ohne Belege genügt
nicht; das Gericht muss die Mittelverwendung nachprüfen können.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Verstöße gegen die Pflicht zur mündelsicheren Anlage (§ 1839 BGB) können
Ersatzansprüche der betreuten Person nach § 1826 BGB iVm § 280 Abs. 1
BGB auslösen; Zinsausfallschäden sind ersatzfähig.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Bestandsaufnahme zum Stichtag der Bestellung**
 Bankauskünfte einholen (Vorlage Bestellungsurkunde), Grundbuchauszug
 beantragen, vorhandene Verträge und Versicherungspolicen sichten.

2. **Vermögensverzeichnis strukturieren**
 - A. Geldvermögen (Konten, Depots, Bargeld)
 - B. Immobilien (Anschrift, Grundbuchblatt, Verkehrswert)
 - C. Bewegliche Sachen von Wert
 - D. Forderungen
 - E. Verbindlichkeiten
 - F. Wiederkehrende Einnahmen und Ausgaben

3. **Mündelsichere Anlage prüfen (§ 1839 BGB)**
 Beträge, die nicht binnen 12 Monaten für laufende Ausgaben benötigt
 werden, sind verzinslich anzulegen. Tagesgeld bei
 einlagengesichertem Institut genügt. Bei Sperrvermerk-Anordnung:
 Konto in "Mündelkonto mit Sperrvermerk" umwandeln.

4. **Sperrvermerk einrichten**
 Antrag beim Betreuungsgericht; nach Genehmigung Sperrvermerk-Vereinbarung
 mit Bank schließen. Verfügungen nur noch mit Genehmigung nach
 § 1848 BGB.

5. **Laufende Buchführung**
 Jede Einnahme und Ausgabe zeitnah erfassen. Empfehlung: Excel-Tabelle
 oder spezielle Betreuersoftware. Belege chronologisch sammeln.

6. **Jährliche Rechnungslegung (§ 1865 BGB)**
 Geordnete Aufstellung Einnahmen/Ausgaben mit Belegen, Endsaldo, Abgleich
 mit Kontoauszug. Bei Heimkosten: Hilfe zur Pflege (§ 61 SGB XII)
 beantragen und prüfen.

## Ausgabeformat

```
Vermögensverzeichnis nach § 1835 BGB
Stichtag: [TT.MM.JJJJ — Tag der Bestellung]

Betreute Person: [Name, Geburtsdatum]
Aktenzeichen: [XVII … / …]
Betreuer: [Name, BtOG-Reg.-Nr.]

A. Geldvermögen
 | Konto | IBAN | Saldo | Sperrvermerk |
 |----------------------|-------------------|-----------|--------------|
 | Sparkasse Berlin Giro | DE. . . . | 1.234 EUR | nein |
 | Sparkasse Spar | DE. . . . | 12.000 EUR| ja |

B. Immobilien
 [Anschrift, Grundbuchblatt, geschätzter Verkehrswert]

C. Bewegliche Sachen von Wert
 [Position, Schätzwert]

D. Forderungen
 [Forderung gegen wen, Betrag, Fälligkeit]

E. Verbindlichkeiten
 [Gläubiger, Betrag, monatliche Rate]

F. Wiederkehrende Einnahmen und Ausgaben
 Einnahmen: Altersrente DRV 1.213 EUR/Mon
 Grundsicherung [Antrag/Bescheid]
 Ausgaben: Heimkosten 2.341 EUR/Mon
 Telekom 29 EUR/Mon

Gesamtvermögen zum Stichtag: [Betrag]

Versicherung:
Ich versichere die Richtigkeit und Vollständigkeit dieses Verzeichnisses
(§ 1835 Abs. 2 BGB).

Ort, Datum [Unterschrift Betreuer/in]
```

Bei der jährlichen Rechnungslegung zusätzlich tabellarische
Einnahmen-Ausgaben-Rechnung mit Belegnummern.

## Beispiel

**Sachverhalt:** Herr Werner P., 78 Jahre, lebt nach Schlaganfall im
Pflegeheim. Sohn Klaus zum ehrenamtlichen Betreuer bestellt am 12.05.2026
mit Aufgabenkreis Vermögenssorge und Gesundheitssorge.

**Ausschnitt Vermögensverzeichnis:**

> A. Geldvermögen
>
> | Konto | IBAN | Saldo 12.05.2026 | Sperrvermerk |
> |---|---|---|---|
> | Postbank Giro | DE12 …4521 | 2187.33 EUR | nein |
> | Postbank Tagesgeld | DE12 …7788 | 24500.00 EUR | ja (beantragt) |
> | Volksbank Sparbuch | DE99 …3344 | 8900.00 EUR | ja (beantragt) |
>
> Mündelsicherheit (§ 1839 BGB): Postbank Tagesgeld und Volksbank Sparbuch
> sind verzinslich angelegt und einlagengesichert. Antrag auf Anordnung des
> Sperrvermerks (§ 1845 BGB) für beide Konten wird zeitgleich eingereicht,
> da Vermögen über dem Sockelbetrag von 5.000 EUR liegt.

## Risiken und typische Fehler

**1. Unvollständigkeit**
Schmuck, Bargeld in der Wohnung, Lebensversicherungen mit
Rückkaufswert, Sterbegeldversicherungen werden häufig vergessen. Eine
Wohnungsbegehung mit Bestandsaufnahme ist regelmäßig erforderlich (BGH
XII ZB 174/18 Rn. 14).

**2. Mündelsicherheit verletzt**
Belassen größerer Beträge auf unverzinslichem Girokonto verstößt gegen
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
530/15 Rn. 9 ff.).

**3. Verfügung über gesperrte Konten ohne Genehmigung**
Verfügungen über Konten mit Sperrvermerk ohne gerichtliche Genehmigung
sind nach § 1848 BGB unwirksam und können Schadensersatzansprüche der
betreuten Person auslösen.

**4. Rechnungslegung nur zusammenfassend**
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
632/12 Rn. 21). Belege sind chronologisch und kontinuierlich zu führen.

**5. Schonvermögen Sozialhilfe verkannt**
Bei Heimaufenthalt mit Hilfe zur Pflege: § 90 Abs. 2 Nr. 9 SGB XII —
Schonbetrag 10.000 EUR (Stand 01.01.2023). Vermögen darüber muss erst
verbraucht werden, bevor Sozialhilfe einsetzt. Frühzeitige Antragstellung.

**6. Vermischung Eigenes/Betreutenvermögen**
Strikte Trennung: Niemals Bareinlagen oder Vermögensanlagen auf Konto
des Betreuers. Verstöße können strafrechtliche Folgen haben (Untreue
§ 266 StGB).

## Quellenpflicht

Bei jeder Ausgabe sind mindestens folgende Belege anzugeben:

- §§ 1835, 1839, 1841, 1845, 1865 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

---
*Dieser Skill ersetzt keine konkrete fachliche Beratung im Einzelfall.*

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

