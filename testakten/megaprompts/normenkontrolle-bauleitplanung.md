# Megaprompt: normenkontrolle-bauleitplanung

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 91 Skills des Plugins `normenkontrolle-bauleitplanung`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Normenkontrolle Bauleitplanung: ordnet Rolle (Antragsteller (Anwohner/Nachbargemeinde),…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen…
3. **pruefung-erstpruefung-und-mandatsziel** — Pruefung: Erstprüfung, Rollenklärung und Mandatsziel.
4. **abwaegungsgebot-1-abs-7-baugb** — Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vi…
5. **anpassungsgebot-flaechennutzungsplan** — Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklun…
6. **antragsbefugnis-eigentuemer-nachbar** — Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2…
7. **aufstellungsbeschluss-bekanntmachung** — Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. …
8. **festsetzungskatalog-9-baugb-baunvo** — Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog…
9. **jahresfrist-47-abs-2-vwgo** — Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahr…
10. **kommunalabgaben-und-beitragssatzungen** — Kommunalabgaben- und Beitragssatzungen: Gebühren, Beiträge, Fremdenverkehr, Abwasser, Elternbeiträge, Kalkulation und Gl…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Normenkontrolle Bauleitplanung: ordnet Rolle (Antragsteller (Anwohner/Nachbargemeinde), Gemeinde, OVG), markiert Frist (§ 47 II VwGO 1 Jahr ab Bekanntmachung), wählt Norm (BauGB §§ 1/2/10, § 47 VwGO Normenkontrolle) und Zuständigkeit (OVG/VGH), leitet zum passende..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Normenkontrolle Bauleitplanung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abwaegung-formular-portal` — Abwaegung Formular Portal
- `abwaegung-formular-portal-und-einreichung` — Abwaegung Formular Portal und Einreichung
- `abwaegungsgebot-1-abs-7-baugb` — Abwaegungsgebot 1 ABS 7 Baugb
- `anfechtung-antragsbefugnis-red-team-korrektur` — Anfechtung Antragsbefugnis RED Team Korrektur
- `anfechtung-tatbestandsmerkmale` — Anfechtung Tatbestandsmerkmale
- `anpassungsgebot-flaechennutzungsplan` — Anpassungsgebot Flaechennutzungsplan
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis Eigentuemer Nachbar
- `antragsbefugnis-fehlerkatalog` — Antragsbefugnis Fehlerkatalog
- `antragsbefugnis-red-team-und-qualitaetskontrolle` — Antragsbefugnis RED Team und Qualitaetskontrolle
- `antragstellervertretung-zahlen-schwellen-und-berechnung` — Antragstellervertretung Zahlen Schwellen und Berechnung
- `artenschutz-naturschutz-aufstellungsbeschluss` — Artenschutz Naturschutz Aufstellungsbeschluss
- `artenschutz-naturschutz-planung` — Artenschutz Naturschutz Planung
- `aufstellungsbeschluss-bekanntmachung` — Aufstellungsbeschluss Bekanntmachung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Normenkontrolle Bauleitplanung sind § 47 VwGO vor BayVGH und OVG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Normenkontrolle Bauleitplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill_

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Normenkontrolle Bauleitplanung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Normenkontrolle Bauleitplanung**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung.

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
| `abwaegungsgebot-1-abs-7-baugb` | Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung… |
| `anpassungsgebot-flaechennutzungsplan` | Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet… |
| `antragsbefugnis-eigentuemer-nachbar` | Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab… |
| `artenschutz-naturschutz-planung` | Buerger oder Naturschutzverband greift Bebauungsplan wegen unzureichender Artenschutzprüfung an. § 44 BNatSchG Zugriffsverbote § 45 Abs. 7 BNatSchG Ausnahme. Prüfraster: spezielle artenschutzrechtliche Prüfung (saP)… |
| `aufstellungsbeschluss-bekanntmachung` | Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs.… |
| `beteiligung-frueh-foermlich` | Mandant greift Bebauungsplan wegen Fehlern in der Buerger- oder Behördenbeteiligung an. §§ 3 4 BauGB Beteiligungsverfahren. Prüfraster: fruehzeitige Beteiligung § 3 Abs. 1 foermliche Auslegung § 3 Abs. 2 mindestens 1… |
| `buergerversammlung-protokoll-audit` | Mandant war bei Buergerversammlung und moechte Niederschrift auf Vollständigkeit prüfen. § 3 Abs. 1 BauGB Buergerversammlung Eroerterungstermin. Prüfraster: Einladung Tagesordnung Sitzungsleitung Wortbeitraege… |
| `einstweilige-anordnung-47-abs-6-vwgo` | Mandant hat Normenkontrollantrag eingereicht und moechte Vollzug des Bebauungsplans bis zur Entscheidung stoppen. § 47 Abs. 6 VwGO einstweilige Anordnung. Prüfraster: Vollzugsfolgenabwaegung als Massstab… |
| `erforderlichkeit-1-abs-3-baugb` | Mandant greift Bebauungsplan als Gefälligkeitsplanung oder Verhinderungsplanung an. § 1 Abs. 3 S. 1 BauGB Erforderlichkeit Planrechtfertigung. Prüfraster: nachvollziehbares staedtebauliches Konzept erforderlich… |
| `festsetzungskatalog-9-baugb-baunvo` | Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche… |
| `immissionsschutz-laerm-bauleitplanung` | Mandant greift Bebauungsplan wegen unzureichendem Schallschutz oder Immissionsschutz an. DIN 18005 TA Laerm § 50 BImSchG. Prüfraster: Orientierungswerte verschiedene Gebietstypen Schallschutzgutachten Methodik… |
| `jahresfrist-47-abs-2-vwgo` | Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB… |
| `mandat-erstgespraech-normenkontrolle` | Grundstueckseigentuemer oder Nachbar kommt wegen Bebauungsplan oder FNP in die Kanzlei. Erstgespraech Normenkontrollmandat. Prüfraster: Mandantenbetroffenheit Antragsbefugnis § 47 Abs. 2 VwGO Antragsfrist… |
| `muendliche-verhandlung-vgh-strategie` | Normenkontrollantrag steht vor muendlicher Verhandlung am VGH oder OVG. Vorbereitung muendliche Verhandlung Normenkontrolle. Prüfraster: Plaedoyer Einleitung Sachverhalt Rechtsausführungen Anträge schriftliche… |
| `normenkontrollantrag-schriftsatz` | Normenkontrollantrag gegen Bebauungsplan oder FNP ist zu erstellen. § 47 VwGO Normenkontrollantrag Schriftsatz. Prüfraster: Rubrum Antrag Begründung Zulässigkeit (Statthaftigkeit Befugnis Frist Rechtsschutzbedürfnis)… |
| `planerhaltung-214-215-baugb` | Gemeinde oder Vorhabentraeger prüft ob erkannte Planfehler zur Unwirksamkeit führen oder durch Planerhaltung geheilt werden. §§ 214 215 BauGB Planerhaltung und Ruegefrist. Prüfraster: § 214 Abs. 1 bis 3 beachtliche… |
| `statthaftigkeit-47-vwgo` | Mandant fragt ob Normenkontrollantrag gegen eine bestimmte Planung zulässig ist. § 47 Abs. 1 VwGO Statthaftigkeit Normenkontrolle. Prüfraster: Antragsgegenstand Bebauungsplan § 10 BauGB vorhabenbezogener B-Plan § 12… |
| `stellplatzsatzung-bay-bauordnung` | Mandant wendet sich gegen Stellplatzsatzung einer Gemeinde oder deren Anwendung bei Bauantrag. Art. 47 BayBO § 9 Abs. 1 Nr. 4 BauGB Art. 81 BayBO Stellplatzsatzung. Prüfraster: Reduzierung Stellplatzschluessel durch… |
| `umweltbericht-umweltpruefung` | Mandant greift Bebauungsplan wegen unzureichender Umweltprüfung oder fehlendem Umweltbericht an. § 2 Abs. 4 BauGB § 2a BauGB Umweltbericht. Prüfraster: Schutzgueter nach Anhang 1 BauGB Mensch Tiere Pflanzen Boden… |
| `veraenderungssperre-zurueckstellung-14-15-baugb` | Bauherr oder Investor hat Bauantrag eingereicht aber Gemeinde hat Veraenderungssperre verhaengt und Antrag wird zurückgestellt. §§ 14 15 BauGB. Prüfraster: Aufstellungsbeschluss Voraussetzung § 14 Abs. 1 BauGB Wirkung… |
| `vorhabenbezogener-bebauungsplan-12-baugb` | Mandant ist Vorhabentraeger eines VEP oder sieht sich durch vorhabenbezogenen B-Plan benachteiligt. § 12 BauGB vorhabenbezogener Bebauungsplan. Prüfraster: Drei-Saeulen-Konstruktion Vorhaben- und Erschließungs-Plan… |

## Worum geht es?

Dieses Plugin begleitet die Pruefung und Anfechtung von Bebauungsplaenen, Flaechennutzungsplaenen und oertlichen Bauvorschriften vor dem Bayerischen Verwaltungsgerichtshof (BayVGH) und den Oberverwaltungsgerichten (OVG) nach § 47 VwGO. Es deckt das Mandat aus der Perspektive des Antragstellers (Eigentuemer, Nachbar, Naturschutzverband) ab.

Das Plugin strukturiert die Zulaessigkeitsvoraussetzungen (Statthaftigkeit, Antragsbefugnis, Jahresfrist), die Fehlertypen nach dem BauGB (Verfahrensfehler, Erforderlichkeit, Abwaegungsmangel, Fehler bei Festsetzungen), die Planerhaltungsregeln der §§ 214 und 215 BauGB sowie den Eilrechtsschutz nach § 47 Abs. 6 VwGO. Es ersetzt keine individuellen Vertretungshandlungen.

## Wann brauchen Sie diese Skill?

- Grundstueckseigentuemer oder Nachbar kommt mit einem neuen Bebauungsplan in die Kanzlei und fragt nach Moeglichkeiten.
- Mandant hat eine Buergerversammlung besucht und moechte das Protokoll auf Vorfestlegungen pruefen lassen.
- Sie muessen schnell beurteilen, ob die Jahresfrist des § 47 Abs. 2 VwGO noch laeuft.
- Mandant moechte die Vollziehung eines gerade bekanntgemachten Bebauungsplans vorlaefig stoppen.
- Naturschutzverband fragt, ob er gegen einen Plan mit unzureichender Artenschutzpruefung vorgehen kann.

## Fachbegriffe (kurz erklaert)

- **Normenkontrolle (§ 47 VwGO)** — Abstraktes Kontrollinstrument; das OVG/VGH prueft die Rechtmaeßigkeit eines Bebauungsplans oder einer oertlichen Bauvorschrift auf Antrag.
- **Antragsbefugnis** — Nur wer in eigenen Rechten verletzt sein koennte, kann Antrag stellen (Moeglichkeitstheorie, § 47 Abs. 2 S. 1 VwGO).
- **Jahresfrist** — Normenkontrollantrag muss innerhalb eines Jahres ab ortsuebl. Bekanntmachung gestellt werden (§ 47 Abs. 2 S. 1 VwGO).
- **Abwaegungsgebot** — Die Gemeinde muss alle betroffenen Belange ermitteln, bewerten und gegeneinander abwaegen (§ 1 Abs. 7 BauGB); vier Fehlerstufen.
- **Planerhaltung** — §§ 214 und 215 BauGB beschraenken, welche Fehler zur Unwirksamkeit fuehren; Verfahrensfehler sind oft heilbar, Ergebnisfehler nicht.
- **Erforderlichkeit** — Bebauungsplan muss einem nachvollziehbaren staedtebaulichen Konzept dienen (§ 1 Abs. 3 BauGB); Gefaelligkeits- und Verhinderungsplanung sind unzulaessig.
- **Veraenderungssperre** — Sicherungsinstrument der Gemeinde nach § 14 BauGB; hemmt Baugenehmigungen waehrend des Aufstellungsverfahrens.
- **VEP** — Vorhabenbezogener Bebauungsplan nach § 12 BauGB mit Vorhaben- und Erschliessungsplan und Durchfuehrungsvertrag.

## Rechtsgrundlagen

- § 47 VwGO — Normenkontrollverfahren, Statthaftigkeit, Antragsbefugnis, Jahresfrist, einstweilige Anordnung.
- §§ 1 bis 13a BauGB — Aufstellungsverfahren, Erforderlichkeit, Abwaegungsgebot, Beteiligung, Veraenderungssperre.
- §§ 214 und 215 BauGB — Planerhaltung: beachtliche Fehler, Ruegefrist, ergaenzendes Verfahren.
- § 9 BauGB — Festsetzungskatalog.
- BauNVO — Art und Mass der baulichen Nutzung, Hoechtsgrenzen.
- § 44 BNatSchG — Artenschutzrechtliche Zugriffsverbote.
- Art. 47 BayBO, Art. 81 BayBO — Stellplaetze und oertliche Bauvorschriften in Bayern.
- § 2 Abs. 4 BauGB, § 2a BauGB — Umweltpruefung und Umweltbericht.

## Schritt-für-Schritt: Einstieg ins Plugin

1. Erstgespraech und Mandatsannahme-Pruefung: Skill `mandat-erstgespraech-normenkontrolle`.
2. Statthaftigkeit und Antragsbefugnis klaeren: `statthaftigkeit-47-vwgo` und `antragsbefugnis-eigentuemer-nachbar`.
3. Jahresfrist berechnen: `jahresfrist-47-abs-2-vwgo`.
4. Fehlersuche nach Prioritaet: Verfahrensfehler, Erforderlichkeit, Abwaegung, Festsetzungen.
5. Eilantrag pruefen bei drohenden Genehmigungen: `einstweilige-anordnung-47-abs-6-vwgo`.
6. Normenkontrollantrag formulieren: `normenkontrollantrag-schriftsatz`.

## Skill-Tour (was gibt es hier?)

**Einstieg und Mandat**

- `mandat-erstgespraech-normenkontrolle` — Erstgespraech, Mandatsannahme-Empfehlung, vorläufige Erfolgsaussichten.
- `statthaftigkeit-47-vwgo` — Statthaftigkeit der Normenkontrolle gegen Bebauungsplan, VEP, oertliche Bauvorschriften.
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis für Eigentuemer, Nachbar, Verband.
- `jahresfrist-47-abs-2-vwgo` — Jahresfrist berechnen, Fristbeginn, fehlerhafte Bekanntmachung.

**Verfahrensfehler**

- `aufstellungsbeschluss-bekanntmachung` — Fehler beim Aufstellungsbeschluss und der Bekanntmachung.
- `beteiligung-frueh-foermlich` — Fehler in der fruehzeitigen und foermlichen Beteiligung.
- `buergerversammlung-protokoll-audit` — Niederschrift der Buergerversammlung auf Vollstaendigkeit pruefen.
- `umweltbericht-umweltpruefung` — Umweltpruefung und Umweltbericht auf Fehler pruefen.
- `artenschutz-naturschutz-planung` — Artenschutzpruefung (saP), CEF-Massnahmen, FFH-Vertraeglichkeit.

**Materielle Fehler**

- `erforderlichkeit-1-abs-3-baugb` — Erforderlichkeit und Planrechtfertigung; Gefaelligkeits- und Verhinderungsplanung.
- `abwaegungsgebot-1-abs-7-baugb` — Vier Abwaegungsfehler-Stufen nach § 1 Abs. 7 BauGB.
- `anpassungsgebot-flaechennutzungsplan` — Entwicklungsgebot aus dem Flaechennutzungsplan.
- `festsetzungskatalog-9-baugb-baunvo` — Unzulaessige Festsetzungen ausserhalb des Katalogs.
- `immissionsschutz-laerm-bauleitplanung` — Schallschutz, TA Laerm, § 50 BImSchG.

**Planerhaltung und Ruegefrist**

- `planerhaltung-214-215-baugb` — Welche Fehler fuehren zur Unwirksamkeit, welche sind heilbar? Ruegefrist ein Jahr.

**Spezialkonstellationen**

- `vorhabenbezogener-bebauungsplan-12-baugb` — VEP-Pruefung für Vorhabentraeger und Drittbetroffene.
- `veraenderungssperre-zurueckstellung-14-15-baugb` — Anfechtung und Entschaedigung bei Veraenderungssperre.
- `stellplatzsatzung-bay-bauordnung` — Stellplatzsatzung nach Art. 47 BayBO und § 9 Abs. 1 Nr. 4 BauGB.

**Schriftsaetze und Verhandlung**

- `normenkontrollantrag-schriftsatz` — Vollstaendiger Normenkontrollantrag mit Zulaessigkeit, Fehleranalyse, Hilfsantrag.
- `einstweilige-anordnung-47-abs-6-vwgo` — Eilantrag nach § 47 Abs. 6 VwGO gegen Vollziehung des Bebauungsplans.
- `muendliche-verhandlung-vgh-strategie` — Vorbereitung der muendlichen Verhandlung am VGH oder OVG.

## Worauf besonders achten

- **Jahresfrist ist absolut** — Ab ortsuebl. Bekanntmachung laeuft die Jahresfrist unabhaengig von Kenntnis; bei fehlerhafter Bekanntmachung beginnt sie nicht.
- **Planerhaltung filtert viele Fehler** — Nicht jeder Verfahrensfehler fuehrt zur Unwirksamkeit; § 214 Abs. 1 BauGB und die Ruegefrist des § 215 BauGB muessen immer mitbeachtet werden.
- **Ergebnisfehler immer beachtlich** — Fehler bei der Festsetzung ausserhalb des Katalogs oder bei der Erforderlichkeit sind nicht heilbar und nicht ruegepflichtig.
- **Teilunwirksamkeit beantragen** — Bei fehlerhaften Einzelfestsetzungen kann Teilunwirksamkeit Erfolg haben, selbst wenn der Gesamtplan sonst Bestand haelt.
- **Eilantrag und Hauptsache koordinieren** — § 47 Abs. 6 VwGO setzt keinen vor dem Antrag in der Hauptsache voraus; Antragsbefugnis muss aber gegeben sein.

## Typische Fehler

- Normenkontrolle gegen Flaechennutzungsplan beantragt, obwohl dieser grundsaetzlich nicht statthafter Gegenstand ist (Ausnahme: Konzentrationsflaechen).
- Ruegefrist des § 215 BauGB versaeumnt; Verfahrensfehler koennen danach nicht mehr geltend gemacht werden.
- Naturschutzverband meldet sich ohne Verbandsklagebefugnis nach § 64 BNatSchG oder § 2 UmwRG.
- Abwaegungsfehler-Argument wird auf Vorgangs- statt auf Ergebnis-Ebene gefuehrt; § 214 Abs. 3 BauGB filtert nur Vorgangsfehler.
- Eilantrag nach § 47 Abs. 6 VwGO wird eingereicht, obwohl Bebauungsplan noch nicht in Kraft ist.

## Quellen und Aktualitaet

- Stand: 05/2026
- BauGB in der geltenden Fassung
- BauNVO in der geltenden Fassung
- VwGO § 47 in der geltenden Fassung
- BNatSchG §§ 44 und 45 in der geltenden Fassung

---

## Skill: `pruefung-erstpruefung-und-mandatsziel`

_Pruefung: Erstprüfung, Rollenklärung und Mandatsziel._

# Pruefung: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Pruefung Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Normenkontrolle Bauleitplanung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: VwGO § 47 Abs. 2 Antrag 1 Jahr nach Bekanntmachung, BauGB § 3 Abs. 2 Auslegung 1 Monat, Einwendungen 1 Monat, § 215 BauGB Rüge formeller/materieller Fehler 1 Jahr.
- Tragende Normen verifizieren: VwGO § 47, BauGB §§ 1, 1a, 2, 3, 4, 4a, 10, 13, 13a, 13b, 30, 34, 35, BImSchG, BNatSchG, UVPG, EU-Plan-UP-RL 2001/42 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Antragsteller (Eigentümer, Gemeinde, Verband), Gemeinde als Antragsgegnerin, OVG/VGH (zuständig), BVerwG (4. Senat), Träger öffentlicher Belange.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Bebauungsplan, Begründung mit Umweltbericht, Abwägungsmaterial, Beteiligungsstellungnahmen, Satzungsbeschluss, Normenkontrollantrag, Eilantrag § 47 Abs. 6 VwGO — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Pruefung: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** VwGO, OVG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Pruefung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `abwaegungsgebot-1-abs-7-baugb`

_Mandant greift Bebauungsplan wegen fehlerhafter Interessenabwaegung an. § 1 Abs. 7 BauGB Abwaegungsgebot. Prüfraster: vier Abwaegungsfehler-Stufen Abwaegungsausfall Abwaegungsdefizit Abwaegungsfehleinschaetzung Abwaegungsdisproportionalitaet. § 214 Abs. 3 BauGB filtert nur Vorgangsfehler nicht Er..._

# Abwägungsgebot § 1 Abs. 7 BauGB

## Schritt 1 — Wortlaut und Bedeutung

### § 1 Abs. 7 BauGB
- Bei der Aufstellung der Bauleitpläne sind die öffentlichen und privaten Belange gerecht gegeneinander und untereinander abzuwägen

### § 2 Abs. 3 BauGB
- Bei der Aufstellung sind die Belange, die für die Abwägung von Bedeutung sind, zu ermitteln und zu bewerten

### Zwei Säulen
- Ermittlungspflicht § 2 Abs. 3 BauGB
- Abwägungspflicht § 1 Abs. 7 BauGB

## Schritt 2 — Vier Stufen Abwägungsfehler (BVerwG)

### Stufe 1 — Abwägungsausfall
- Überhaupt keine Abwägung stattgefunden
- Vorfestlegung der Stadt vor Abwägungsbeschluss
- Reines Abnicken eines vom Investor vorgelegten Konzepts
- BVerwG, Urteil vom 12.12.1969 – 4 C 105.66

### Stufe 2 — Abwägungsdefizit
- Abwägung erfolgte, aber relevante Belange nicht eingestellt
- Übersehen einzelner abwägungserheblicher Belange
- Folge unvollständiger Ermittlung § 2 Abs. 3 BauGB

### Stufe 3 — Abwägungsfehleinschätzung / Fehlgewichtung
- Belange erkannt, aber objektiv falsch gewichtet
- Überschätzung des Plan-Nutzens, Unterschätzung der Belastung
- Zugrundelegung unzutreffender Tatsachen

### Stufe 4 — Abwägungsdisproportionalität
- Das Abwägungsergebnis selbst sprengt den Spielraum
- Schutzgüter werden in einem nicht mehr vertretbaren Maß zurückgestellt
- Häufig: Lärmwerte deutlich über zumutbarer Grenze, ohne Abhilfe

## Schritt 3 — Beachtlichkeit § 214 Abs. 3 BauGB

### Vorgangsfehler (Stufen 1-3)
- Nur beachtlich, wenn offensichtlich und auf das Ergebnis von Einfluss
- Rügefristpflichtig § 215 BauGB

### Ergebnisfehler (Stufe 4)
- Stets beachtlich
- Nicht rügepflichtig
- Strategisch besonders wertvoll

## Schritt 4 — Abwägungsmaterial vollständig ermitteln

### § 2 Abs. 3 BauGB
- Belange ermitteln und bewerten
- Ermittlungspflicht ist Voraussetzung sachgerechter Abwägung

### Pflichten der Gemeinde
- Eigene Ermittlung erforderlich, nicht bloße Übernahme Investor-Gutachten
- Bei Sachverstandsmangel: Sachverständige hinzuziehen
- Schallschutzgutachten, Verkehrsgutachten, Artenschutz-Begutachtung

### Häufige Treffer
- Schallschutzgutachten vom Investor in Auftrag gegeben, ohne Plausibilitätsprüfung
- Lärmprognose ohne worst-case-Annahme
- Verkehrsgutachten ohne Berücksichtigung Stadtteil-Verflechtung
- Artenschutz-Begutachtung nur in falschem Zeitraum

## Schritt 5 — Vorfestlegung als Abwägungsausfall

### Indizien
- Durchführungsvertrag bereits unterzeichnet vor Aufstellungsbeschluss
- Investor hat bereits Vermarktungs-Aktivitäten gestartet
- Stadt hat in Verhandlungen mit Investor verbindliche Zusagen gemacht
- Aussagen Stadtrats-Mitglieder vor Beschluss: "Wir müssen jetzt durchziehen"

### Beweisführung
- Akteneinsicht in Verhandlungsprotokolle Stadt-Investor
- Presse-Recherche
- Eidesstattliche Versicherungen Sitzungsteilnehmer
- E-Mail-Korrespondenz aus IFG / Anti-Korruptions-Hinweis

### Rechtsfolge
- Abwägungsausfall führt zur Unwirksamkeit
- Nicht heilbar durch nachgeholte Abwägungsdokumentation

## Schritt 6 — Formelhafte Abwägungsdokumentation als Defizit

### Indizien
- Stellungnahmen werden mit Standard-Sätzen zurückgewiesen
- Keine Auseinandersetzung mit Substanz der Einwendungen
- Identische Formulierungen für unterschiedliche Belange
- Übernahme von Investor-Argumenten ohne Prüfung

### Beweismittel
- Wortlaut-Vergleich der Abwägungstabelle mit Einwendungen
- Vergleich verschiedener Einwendungen — gleiche Antwort?

## Schritt 7 — Fehlgewichtung typische Felder

### Wertminderung
- Stadt darf Wertminderung Mandanten als untergeordnet einstufen, aber nicht ausblenden
- Wenn Wertminderung nicht erkannt — Defizit
- Wenn Wertminderung erkannt, aber pauschal abgetan — Fehlgewichtung

### Klima
- Hitze-Inseln, Frischluftschneisen — bei Verdichtung relevanter Belang
- Fehlende Erörterung trotz erkennbarer Bedeutung — Defizit
- Erörterung mit "geringer Bedeutung" trotz Hitzeschwüle — Fehlgewichtung

### Stadtbild
- Erhaltenswerte Strukturen, Gründerzeit, Bahnhofsensemble
- Fehlende Erörterung trotz Denkmalbedeutung — Defizit
- Verdrängung durch wirtschaftliches Interesse — Fehlgewichtung möglich

## Schritt 8 — Disproportionalität konkret

### Lärmschwellen-Sprung
- Lärmpegel überschreitet Orientierungswerte DIN 18005 um mehr als 5 dB(A)
- Ohne aktive Schallschutzmaßnahmen
- Verweis auf passive Schallschutzfenster reicht nicht für Außenwohnbereiche

### Verschattung
- Mehr als 50% Sonnenschutz an Hauptaufenthaltsräumen
- Ohne Ausgleich

### Verkehr
- Verdoppelung Verkehr ohne Erschließungsalternative
- Sackgassen-Effekt für Anwohner

## Schritt 9 — Abwägungsschriftsatz-Aufbau

### Empfohlener Aufbau
1. Anspruch auf gerechte Abwägung § 1 Abs. 7 BauGB
2. Ermittlungspflicht § 2 Abs. 3 BauGB — Defizit Stadt
3. Vorgangsfehler-Subsumtion (Ausfall / Defizit / Fehlgewichtung)
4. Offensichtlichkeit und Ergebnis-Relevanz § 214 Abs. 3 BauGB
5. Ergebnisfehler-Subsumtion (Disproportionalität)
6. Rüge nach § 215 BauGB (für Vorgangsfehler) referenzieren
7. Fazit: Antrag auf Unwirksamkeitserklärung

## Quellen

- BauGB §§ 1 Abs. 7, 2 Abs. 3, 214 Abs. 3, 215
- BVerwG, Urteil vom 12.12.1969 – 4 C 105.66 (Vier-Stufen-Lehre)
- BVerwG, Urteil vom 5.7.1974 – 4 C 50.72 (Abwägungsausfall)
- BVerwG, Urteil vom 9.4.2008 – 4 CN 1.07 (Ermittlungspflicht § 2 Abs. 3)
- BVerwG, Urteil vom 22.9.2010 – 4 CN 2.10 (Offensichtlichkeit)

## Ergänzende Rechtsprechung (Stand 05/2026, verifiziert bverwg.de)

- **BVerwG 11.04.2024, 4 BN 50.23** (Abwaegungsmaengel — Klimaschutz § 1 Abs. 5 S. 2 BauGB): Klimaschutz und Klimaanpassung sind als Belang nach § 1 Abs. 5 S. 2 BauGB zwingend in die Abwaegung einzustellen. Quelle: bverwg.de.
- **BVerwG 04.05.2022, 4 CN 2.21** (Bauleitplanung Wind/Solar): Anforderungen an Abwaegung bei Konzentrationszonen-Planung; Substantiierungspflicht. Quelle: bverwg.de.
- **BVerwG 03.04.2020, 4 CN 2.19**: Erhaltungssatzung § 172 BauGB — Anforderungen an Abwaegung und Erforderlichkeit. Quelle: bverwg.de.
- **BVerwG 23.06.2020, 9 A 22.19** (Klimaschutz-Belang Verkehrsplanung; uebertragbar auf Bauleitplanung): Klima als bei Planungen zwingend einzustellender Belang. Quelle: bverwg.de.

Konkrete Entscheidungen vor Verwendung per bverwg.de mit Datum verifizieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 215 BauGB
- § 1 BauGB
- § 214 BauGB
- § 2 BauGB
- § 50 BImSchG
- § 10 BauGB
- § 9 BauGB
- § 14 BauGB
- § 12 BauGB
- § 44 BNatSchG
- § 3 BauGB

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `anpassungsgebot-flaechennutzungsplan`

_Mandant greift Bebauungsplan an weil er nicht aus dem Flaechennutzungsplan entwickelt wurde. § 8 Abs. 2 BauGB Entwicklungsgebot und Anpassungsgebot. Prüfraster: Entwicklungssaussage des FNP bezogen auf Plangebiet Konflikt FNP-Darstellung vs. B-Plan-Festsetzung Ausnahmen § 8 Abs. 3 und 4 BauGB Par..._

# Anpassungsgebot — Flächennutzungsplan

## Schritt 1 — Wortlaut § 8 BauGB

### § 8 Abs. 1 BauGB
- Bebauungspläne enthalten die rechtsverbindlichen Festsetzungen für die städtebauliche Ordnung

### § 8 Abs. 2 S. 1 BauGB (Entwicklungsgebot)
- Bebauungspläne sind aus dem Flächennutzungsplan zu entwickeln

### § 8 Abs. 3 S. 1 BauGB (Parallelverfahren)
- Vor dem Flächennutzungsplan kann ein Bebauungsplan aufgestellt werden, wenn dringende Gründe es erfordern und der Bebauungsplan der beabsichtigten städtebaulichen Entwicklung nicht entgegensteht

### § 8 Abs. 4 BauGB (selbständiger B-Plan)
- Ein Bebauungsplan kann aufgestellt werden, ohne dass ein Flächennutzungsplan vorliegt, wenn er der städtebaulichen Entwicklung nicht widerspricht

## Schritt 2 — Entwicklungsgebot — Begriff "Entwickeln"

### Maßstab
- B-Plan-Festsetzungen müssen aus FNP-Darstellungen "entwickelt" sein
- Entwicklung verlangt sachlichen Bezug, keine 1:1-Identität
- Konkretisierung der FNP-Aussage durch B-Plan

### Beispiel
- FNP: "Wohnbaufläche W"
- B-Plan: WA (allgemeines Wohngebiet) — entspricht Entwicklungsgebot
- B-Plan: GE (Gewerbegebiet) — widerspricht Entwicklungsgebot

### Toleranz
- Geringfügige Abweichungen toleriert
- Größere Abweichungen erfordern FNP-Änderung im Parallelverfahren oder vorab

## Schritt 3 — Parallelverfahren § 8 Abs. 3 BauGB

### Voraussetzungen
- Dringende Gründe für vorgezogenen B-Plan
- B-Plan steht der beabsichtigten städtebaulichen Entwicklung nicht entgegen
- Tatsächlich praktisch häufig parallel betrieben

### Pflichten
- FNP-Änderungsverfahren muss eingeleitet sein
- Beide Pläne werden gemeinsam zur Beschlussfassung gebracht
- Reihenfolge: erst FNP-Wirksamkeit, dann B-Plan-Wirksamkeit (oder zeitgleich)

### Häufige Treffer
- B-Plan wird vor FNP-Änderung wirksam
- Vorgezogener B-Plan ohne dringende Gründe
- Stadt argumentiert mit "Investor-Druck" — kein dringender Grund

## Schritt 4 — Berichtigungsmöglichkeit § 13a Abs. 2 BauGB

### Voraussetzung
- B-Plan der Innenentwicklung nach § 13a BauGB
- Geringfügige Abweichung vom FNP

### Verfahren
- FNP wird im Wege der "Berichtigung" angepasst
- Kein förmliches FNP-Änderungsverfahren erforderlich
- Bekanntmachung Berichtigung im Amtsblatt

### Strategischer Angriffspunkt
- Wenn die Abweichung in Wahrheit nicht "geringfügig" ist
- Wenn der B-Plan in Wahrheit nicht Innenentwicklung nach § 13a darstellt
- Wenn die Berichtigung nicht bekanntgemacht ist

## Schritt 5 — Selbständiger B-Plan § 8 Abs. 4 BauGB

### Anwendungsbereich
- In Gemeinden ohne wirksamen FNP
- Bei isolierten Festsetzungen ohne FNP-Bezug

### Voraussetzung
- B-Plan widerspricht nicht der städtebaulichen Entwicklung
- Strenge Anforderung — restriktiv anwendbar

### Praxis
- Selten relevant in größeren Städten mit umfassendem FNP
- Bei Flecken-Plänen, Sonderzonen denkbar

## Schritt 6 — FNP-Bezug konkret prüfen

### Audit-Schritte
1. FNP-Auszug für das Plangebiet beschaffen
2. FNP-Darstellung identifizieren (Wohnbauflache, gemischte Baufläche, Gewerbefläche, Grünfläche, Verkehrsfläche)
3. B-Plan-Festsetzung mit FNP-Darstellung vergleichen
4. Bei Abweichung: Parallelverfahren oder Berichtigung dokumentiert?

### Häufige Konstellationen
- FNP: "gemischte Baufläche" — B-Plan: WA — Entwicklung zulässig
- FNP: "Wohnbauflache" — B-Plan: MK (Kerngebiet) — problematisch
- FNP: "Grünfläche" — B-Plan: WA — widerspricht Entwicklungsgebot
- FNP: "Bahnanlage" — B-Plan: MU (urbanes Gebiet) — FNP-Änderung zwingend

## Schritt 7 — Konflikt Bahn-Anlage / Bahnflächen

### Sonderfall Bahnhofsbrachen
- Bahnflächen sind häufig im FNP als "Bahnanlage" oder "Fläche für Bahnbetrieb" dargestellt
- Bei Umwandlung in städtisches Quartier — FNP-Änderung erforderlich
- Eisenbahnrecht (Allgemeines Eisenbahngesetz, AEG) für Entwidmung relevant

### Entwidmung § 23 AEG
- Vor B-Plan-Beschluss muss Bahnfläche entwidmet sein
- Sonst Konflikt mit Eisenbahnrecht
- Eisenbahn-Bundesamt zuständig

### Strategischer Hebel
- Wenn Entwidmung nicht vorliegt — B-Plan wirft zwei Probleme auf:
 - FNP-Konflikt
 - Eisenbahnrechts-Konflikt
- Beides als Verstoß gegen Erforderlichkeit oder beachtlicher Fehler

## Schritt 8 — Rechtsfolge bei Verstoß gegen § 8 Abs. 2 BauGB

### Wirksamkeit
- Verstoß gegen Entwicklungsgebot ist beachtlich (§ 214 Abs. 2 BauGB)
- Bei Beachtlichkeit kann Plan unwirksam sein
- § 215 BauGB-Rügefrist gilt

### Heilung
- Durch nachträgliche FNP-Änderung und ergänzendes Verfahren
- Häufiger Heilungsweg der Stadt

## Schritt 9 — Audit-Checkliste

| Punkt | Prüfung |
|---|---|
| FNP-Darstellung Plangebiet identifiziert? | |
| B-Plan-Festsetzung identifiziert? | |
| Übereinstimmung Entwicklungsgebot? | Ja/nein |
| Bei Abweichung: Parallelverfahren? | Ja/nein |
| Bei Abweichung: Berichtigung § 13a Abs. 2 BauGB? | Ja/nein |
| Bei Bahnflächen: Entwidmung § 23 AEG? | Ja/nein |
| FNP-Änderung bekannt gemacht? | Ja/nein |

## Quellen

- BauGB §§ 5 8 13a 214
- AEG § 23
- BVerwG, Urteil vom 28.2.1975 – 4 C 30.72 (Entwicklungsgebot)
- BVerwG, Urteil vom 26.2.1999 – 4 CN 6.98 (Parallelverfahren)
- BVerwG, Urteil vom 27.10.1999 – 11 A 31.98 (Entwidmung Bahnfläche)
- BayVGH, Urteil vom 5.10.2017 – 15 N 16.1652 (Berichtigung)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 47 VwG
- § 215 BauGB
- § 1 BauGB
- § 214 BauGB
- § 2 BauGB
- § 50 BImSchG
- § 10 BauGB
- § 9 BauGB
- § 14 BauGB
- § 12 BauGB
- § 44 BNatSchG
- § 3 BauGB

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `antragsbefugnis-eigentuemer-nachbar`

_Grundstueckseigentuemer oder Nachbar moechte Normenkontrollantrag stellen und fragt ob er antragsbefugt ist. § 47 Abs. 2 S. 1 VwGO Antragsbefugnis Normenkontrolle. Prüfraster: Möglichkeitstheorie als Massstab Eigentuemer im Plangebiet immer antragsbefugt Nachbar bei abwaegungserheblichem Belang B..._

# Antragsbefugnis § 47 Abs. 2 VwGO

## Schritt 1 — Maßstab Möglichkeitstheorie

### Wortlaut § 47 Abs. 2 S. 1 VwGO
- Antragsbefugt ist jede natürliche oder juristische Person, die geltend macht, durch die Rechtsvorschrift oder deren Anwendung in ihren Rechten verletzt zu sein oder in absehbarer Zeit verletzt zu werden

### Möglichkeitstheorie
- Es genügt, dass eine Rechtsverletzung möglich erscheint
- Kein Vollbeweis im Zulässigkeitsstadium
- Schlüssige Darlegung tatsächlicher Anhaltspunkte
- Verstärkter Maßstab seit 1996/2006-Verkürzung — aber keine Beweisanforderung

### Schwelle
- Geltendmachung muss substanziiert erfolgen
- Bloße Behauptung "ich bin betroffen" reicht nicht
- Konkrete Bezugnahme auf bestimmten Belang notwendig

## Schritt 2 — Eigentümer im Plangebiet

### Grundregel
- Eigentümer eines Grundstücks im Plangebiet ist stets antragsbefugt
- Begründung Art. 14 GG: B-Plan-Festsetzungen wirken unmittelbar auf das Eigentum
- BVerwG seit Jahrzehnten unverändert

### Anwendung
- Egal ob Festsetzungen den Mandanten begünstigen oder belasten
- Auch bei nur teilweise im Plangebiet liegenden Grundstücken
- Erbbauberechtigte gleichgestellt
- Wohnungseigentümer für Sondereigentum und Miteigentum am gemeinschaftlichen Eigentum

## Schritt 3 — Eigentümer außerhalb des Plangebiets

### Schwelle abwägungserheblicher Belang
- Außerhalb des Plangebiets nicht automatisch betroffen
- Erforderlich: abwägungserheblicher privater Belang
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16
- BVerwG, Beschluss vom 8.6.2011 – 4 BN 42.10
- Abwägungserheblich = mehr als nur geringfügig betroffen

### Typische abwägungserhebliche Belange
- Lärmzunahme durch Verkehr aus dem Plangebiet
- Verschattung durch Hochbauten
- Gefahr durch Schadstoffemissionen
- Sichtbeziehung bei besonderer landschaftlicher Bedeutung
- Wertminderung wenn auf abwägungserheblichen Belang zurückführbar

### Nicht abwägungserhebliche Belange
- Allgemeine Aussichtseinbußen ohne besondere Schutzwürdigkeit
- Reine wirtschaftliche Konkurrenz
- Bloße Wertminderung ohne Substanz-Beeinträchtigung (BVerwG, Beschluss vom 9.2.1995 – 4 NB 17.94)
- Diffuse "Verschlechterung der Wohnqualität"

## Schritt 4 — Andere Berechtigte

### Mieter und Pächter
- Grundsätzlich nicht antragsbefugt, da kein dingliches Recht
- Ausnahme bei besonderer Schutzgehalt (z.B. Gewerbemieter mit existenziell betroffenem Standort) — restriktiv
- Im Zweifel mit Eigentümer-Mandat verknüpfen

### Erbbauberechtigte
- Wie Eigentümer

### Wohnungseigentümer
- Antragsbefugt für eigene Wohnung
- Bei Gemeinschaftsangelegenheiten Beschluss der WEG erforderlich

## Schritt 5 — Verbandsklage Naturschutz

### Anerkannte Vereinigungen § 3 UmwRG
- Vom Bund oder Land anerkannte Vereinigungen
- BUND, NABU, LBV, Bürgerinitiativen mit Anerkennung

### Klagebefugnis § 2 UmwRG
- Bei Plänen mit UVP-Pflicht oder Sondernormen
- Bei FFH-relevanten Plänen
- Bei B-Plänen mit Umweltbericht — über § 2 Abs. 1 UmwRG i.V.m. § 1 Abs. 1 S. 1 Nr. 4 UmwRG
- Eigenständige Antragsbefugnis ohne dingliches Recht

### Naturschutz § 64 BNatSchG
- Bei Entscheidungen mit Naturschutzbezug
- Häufig kumulativ mit § 2 UmwRG geltend gemacht

## Schritt 6 — Gemeinde gegen übergeordnete Planung

### Anpassungsgebot § 8 Abs. 2 BauGB
- B-Plan muss aus FNP entwickelt werden
- Gemeinde gegen FNP-Änderung des Nachbarn — Antragsbefugnis möglich

### Selbstverwaltungsrecht
- Art. 28 Abs. 2 GG, Art. 11 Abs. 2 BayVerfg
- Gemeinden gegen übergreifende Festsetzungen

## Schritt 7 — Praktische Begründung im Schriftsatz

### Aufbau Antragsbefugnis-Begründung
1. Identifikation Mandant und Eigentumsstellung
2. Verortung Grundstück zur Plangrenze (Lageplan, Maßangaben)
3. Konkreter abwägungserheblicher Belang mit Substanz
4. Verweis auf Aufnahme dieses Belangs in eigener Einwendung im Aufstellungsverfahren (verstärkt aber nicht zwingend)
5. Verweis auf zu erwartende Verletzung in absehbarer Zeit

### Beispielsatz
- "Die Antragstellerin ist Alleineigentümerin des Grundstücks Provinostraße 12, eingetragen im Grundbuch von Augsburg Blatt 4711, das unmittelbar an die nördliche Plangrenze angrenzt. Die im B-Plan festgesetzte Bauhöhe von bis zu 30 m wird zu einer Verschattung der nach Süden orientierten Wohnräume sowie zu einer Verkehrslärmzunahme durch die festgesetzte Tiefgaragenzufahrt führen. Diese Belange sind abwägungserheblich (BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16) und wurden bereits in der Einwendung vom 12.10.2023 substantiiert vorgetragen."

## Schritt 8 — Häufige Fehler bei Antragsbefugnis

- Pauschale Behauptung der Betroffenheit ohne räumlichen Bezug
- Fehlende Substanziierung des Belangs
- Belang, der gerade nicht abwägungserheblich ist (allgemeine Aussicht)
- Fehlende Beifügung Grundbuchauszug bei juristischer Person oder Erbengemeinschaft
- Falsche Antragstellerbezeichnung bei Eheleuten (jeder Eigentümer einzeln)

## Quellen

- VwGO § 47 Abs. 2
- GG Art. 14 Abs. 1, Art. 28 Abs. 2
- BayVerfg Art. 11 Abs. 2
- BauGB § 8 Abs. 2
- BNatSchG § 64
- UmwRG §§ 1 2 3
- BVerwG, Beschluss vom 9.2.1995 – 4 NB 17.94 (Wertminderung)
- BVerwG, Beschluss vom 8.6.2011 – 4 BN 42.10 (Nachbar abwägungserheblich)
- BVerwG, Beschluss vom 31.1.2017 – 4 BN 28.16 (Maßstab Möglichkeitstheorie)

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `aufstellungsbeschluss-bekanntmachung`

_Mandant prüft ob ein Bebauungsplan an einem Verfahrensfehler beim Aufstellungsbeschluss oder der Bekanntmachung leidet. §§ 2 10 BauGB Verfahrenskette. Prüfraster: Aufstellungsbeschluss ortsuebl. Bekanntmachung § 2 Abs. 1 Beschluss als Satzung § 10 Abs. 1 ortsuebliche Bekanntmachung § 10 Abs. 3 Id..._

# Aufstellungsbeschluss und Bekanntmachung

## Schritt 1 — Verfahrenskette im Überblick

### Reguläre Kette
1. Aufstellungsbeschluss § 2 Abs. 1 BauGB
2. Frühzeitige Beteiligung Öffentlichkeit § 3 Abs. 1 BauGB
3. Frühzeitige Beteiligung Behörden § 4 Abs. 1 BauGB
4. Erarbeitung Planentwurf
5. Förmliche Beteiligung Öffentlichkeit § 3 Abs. 2 BauGB (Auslegung)
6. Förmliche Beteiligung Behörden § 4 Abs. 2 BauGB
7. Ggf. erneute Auslegung bei Änderung § 4a Abs. 3 BauGB
8. Abwägungsbeschluss
9. Satzungsbeschluss § 10 Abs. 1 BauGB
10. Bekanntmachung § 10 Abs. 3 BauGB
11. Beizustellen: Begründung mit Umweltbericht zur Einsichtnahme

### Beschleunigte Verfahren
- § 13 BauGB vereinfachtes Verfahren — Schritte verkürzt
- § 13a BauGB Innenentwicklung — keine Umweltprüfung im Einzelfall
- § 13b BauGB Außenentwicklung Wohnbau — Befristung beachten

## Schritt 2 — Aufstellungsbeschluss § 2 Abs. 1 BauGB

### Inhalt
- Beschluss des Gemeinderats, einen B-Plan aufzustellen
- Räumlicher Geltungsbereich abgrenzbar
- Planziel und allgemeines Anliegen

### Form
- Sitzungsöffentlichkeit gewahrt § 52 BayGO
- Beschlussfähigkeit § 47 BayGO
- Befangenheit § 49 BayGO geprüft

### Bekanntmachung Aufstellungsbeschluss
- Ortsübliche Bekanntmachung
- Häufig Amtsblatt
- Fehlt die Bekanntmachung — Verfahrensfehler, aber häufig unbeachtlich nach § 214 BauGB

## Schritt 3 — Identität der Planfassung

### Identitätsprüfung
- Welche Planfassung wurde frühzeitig ausgelegt?
- Welche Planfassung wurde förmlich ausgelegt?
- Welche Planfassung wurde als Satzung beschlossen?
- Welche Planfassung wurde bekanntgemacht?

### Häufige Treffer
- Beschluss-Vorlage zeigt Plan-Stand vom 15.3., Beschluss verweist auf Plan vom 22.4. — Identitätsfehler
- Auslegung erfolgte über Plan-Stand 10.1., Beschluss über 5.5. ohne erneute Auslegung — § 4a Abs. 3 BauGB-Verstoß
- Beschluss umfasst zusätzliche Änderungen die nie ausgelegt waren — beachtlich (§ 214 Abs. 1 S. 1 Nr. 2 BauGB)

## Schritt 4 — Erneute Auslegung § 4a Abs. 3 BauGB

### Pflicht zur erneuten Auslegung
- Wenn Planentwurf nach Auslegung in der Substanz geändert wird
- Substanz = Berührung der Grundzüge der Planung
- Bloße redaktionelle Änderungen genügen nicht für erneute Auslegung

### Begrenzte erneute Auslegung
- Beschränkung auf die geänderten Teile möglich (§ 4a Abs. 3 S. 2 BauGB)
- Hinweis im Bekanntmachungstext erforderlich
- Frist mindestens zwei Wochen

### Häufiger Fehler
- Stadt erkennt nach Auslegung den Hochbauwunsch des Vorhabenträgers, Aufstockung von 6 auf 8 Geschosse, ohne erneute Auslegung in Beschluss aufgenommen — beachtlich

## Schritt 5 — Satzungsbeschluss § 10 Abs. 1 BauGB

### Beschlussgegenstand
- Beschluss umfasst Planurkunde, textliche Festsetzungen, Begründung mit Umweltbericht
- Beschluss in einem Akt — kein Aufspalten zulässig

### Beschlussvorlage
- Vollständig zur Sitzung ausgelegt
- Sieben Tage vor Sitzung an Stadträte verteilt (Bayern: § 47 Abs. 2 BayGO)
- Abwägungsdokumentation als Anlage

### Sitzungsöffentlichkeit
- Beratung und Beschluss in öffentlicher Sitzung § 52 BayGO
- Nichtöffentliche Beratung bei B-Plan-Beschluss in der Regel rechtswidrig

## Schritt 6 — Bekanntmachung § 10 Abs. 3 BauGB

### Inhalt der Bekanntmachung
- Bezeichnung des Plans
- Geltungsbereich
- Inkrafttreten
- Ort der Einsichtnahme in den Plan
- Hinweis auf § 215 BauGB-Rügefrist
- Hinweis auf § 44 BauGB-Entschädigungsanspruch
- Hinweis auf Beachtlichkeit nach § 214 BauGB

### Anstoßfunktion
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87
- Bekanntmachung muss Anstoß-funktion erfüllen
- Bürger muss erkennen können, dass und wo er sich informieren kann
- Bei zu allgemeiner Bezeichnung — Anstoßfunktion verletzt

### Form der Bekanntmachung
- Ortsüblich nach Hauptsatzung der Gemeinde
- Amtsblatt regelmäßig vorgesehen
- Ersatzbekanntmachung bei umfangreichen Plänen möglich (§ 10 Abs. 3 S. 2 BauGB)
- Online-Veröffentlichung als zusätzliche Option, nicht ausreichend allein

## Schritt 7 — Häufige Treffer in der Bekanntmachung

| Fehler | Beachtlichkeit |
|---|---|
| Falsches Aktenzeichen / Plannummer | Anstoßfunktion verletzt — beachtlich |
| Fehlender Hinweis auf § 215 BauGB | Rügefrist läuft nicht — strategisch wichtig |
| Fehlender Hinweis auf § 44 BauGB | Entschädigungsanspruch bleibt — meist nicht beachtlich für Plan-Wirksamkeit |
| Falscher Einsichtsort | Anstoßfunktion verletzt — beachtlich |
| Geltungsbereich nur grob beschrieben | Anstoßfunktion fraglich |
| Bekanntmachung in nicht ortsüblicher Form | Wirksamkeit fraglich |

## Schritt 8 — Audit-Vorgehen

### Beschaffung
- Auszug Sitzungsniederschrift Aufstellungsbeschluss
- Auszug Sitzungsniederschrift Satzungsbeschluss
- Beschlussvorlagen
- Auslegungsnachweise (Auslegungsverfügung, Auslegungsbeginn, Auslegungsende)
- Bekanntmachungsexemplare aller Verfahrensschritte (Aufstellungs-Bek., Auslegungs-Bek., Satzungs-Bek.)

### Tabellarisches Audit
- Zeile pro Verfahrensschritt
- Spalten: Datum, Beschlussfähigkeit, Befangenheit, Bekanntmachung, Anstoßfunktion ja/nein, Fehler ja/nein, Beachtlichkeit
- Auswertung am Schluss

## Quellen

- BauGB §§ 2 3 4 4a 9 10 13 13a 13b 44 214 215
- BayGO Art. 47 49 52
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87 (Anstoßfunktion)
- BVerwG, Urteil vom 18.7.2013 – 4 CN 3.12 (Identität Planfassung)
- BVerwG, Beschluss vom 18.12.1987 – 4 NB 2.87 (Ortsüblichkeit)

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `festsetzungskatalog-9-baugb-baunvo`

_Mandant greift einzelne Festsetzungen im Bebauungsplan als rechtswidrig an. § 9 BauGB abschließender Festsetzungskatalog BauNVO. Prüfraster: Festsetzungen außerhalb des Katalogs unwirksam BauNVO Art und Mass bauliche Nutzung GRZ GFZ Vollgeschosse Hoechstgrenzen § 17 BauNVO Stellplaetze § 9 Abs. 1..._

# Festsetzungs-Katalog § 9 BauGB iVm BauNVO

## Eingaben

- Bebauungsplan-Festsetzungen (textlich beschrieben)
- Planzeichnung (soweit zugänglich)
- Bezugnahme auf BauNVO-Fassung
- Bezug zu sonstigen Spezialgesetzen (BImSchG, BNatSchG, AEG)

## Schritt 1 — § 9 BauGB als abschließender Katalog

### Geltung

- § 9 Abs. 1 BauGB enthält 26 nummerierte Festsetzungs-Tatbestände (Nr. 1 bis 26)
- § 9 Abs. 2 erweitert für besondere Fälle
- § 9 Abs. 3 vorhabenbezogene Bebauungspläne § 12 BauGB
- § 9 Abs. 4 ergänzende Regelungen
- § 9 Abs. 5, 6, 7 Hinweise und Kennzeichnungen (nicht Festsetzungen)
- § 9 Abs. 8 Begründungs-Erfordernis

### Konsequenz Abschließlichkeit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bezugnahme auf Spezialgesetze nur soweit § 9 BauGB dies zulässt
- Konstruktion **"Hinweise"** vs. **Festsetzungen** entscheidend

## Schritt 2 — Kern-Festsetzungen § 9 Abs. 1

### Nr. 1 — Art der baulichen Nutzung

- Konkretisierung über BauNVO §§ 2 bis 9, 11
- Baugebietstypen: WS, WR, WA, WB, MD, MI, MU, MK, GE, GI, SO
- Ausnahmen und Beschränkungen § 1 Abs. 4-9 BauNVO

### Nr. 2 — Maß der baulichen Nutzung

Drei Faktoren nach § 16 ff. BauNVO:
- Grundflächenzahl GRZ (§ 19 BauNVO)
- Geschossflächenzahl GFZ (§ 20 BauNVO)
- Höhe baulicher Anlagen — Wandhöhe, Firsthöhe, Geschoßzahl (§ 18 BauNVO)
- Bei Festsetzung mehrerer Maß-Werte: kumulativ einzuhalten

#### Höchstgrenzen § 17 BauNVO

| Gebietsart | GRZ | GFZ | Bauliche Anlagenhöhe |
|---|---|---|---|
| WS, WR | 0,4 | 1,2 | – |
| WA, WB | 0,4 | 1,2 (WB 1,6) | – |
| MD | 0,6 | 1,2 | – |
| MI, MU | 0,6/0,8 | 1,2/3,0 | – |
| MK | 1,0 | 3,0 | – |
| GE | 0,8 | 2,4 | – |
| GI | 0,8 | 2,4 | – |
| Sondergebiete | nach Festsetzung | nach Festsetzung | – |

#### Überschreitung § 17 Abs. 2 BauNVO

- Nur bei besonderen städtebaulichen Gründen
- Begründung im Plan zwingend
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Nr. 3 — Überbaubare und nicht überbaubare Grundstücksflächen

- Baulinien, Baugrenzen, Bauteppich
- Bauweise (offen, geschlossen, abweichend)

### Nr. 4 — Stellplätze und Garagen

- Eingeschränkt nutzbar — meist Verweis auf Landesbauordnung
- Konkurrenz mit Art. 47 ff. BayBO
- Stellplatzsatzung der Gemeinde nach Art. 81 BayBO

### Nr. 5 — Flächen für Gemeinbedarf

- Schulen, Kindertagesstätten, kirchliche Anlagen, Verwaltung
- Konkretisierung über Nutzungs-Zweck

### Nr. 6 — Verkehrsflächen

- Öffentliche Straßen, Wege, Plätze, Stellplätze für Fahrräder etc.
- Bahnflächen sind grundsätzlich § 38 BauGB-Spezialregelung (siehe unten)

### Nr. 10 — Grünflächen

- Öffentliche und private Grünflächen
- Hier auch festsetzbar: Spielplätze, Bestattungsstätten, Friedhöfe

### Nr. 14 — Flächen für Versorgungs-Anlagen

- Elektrizität, Gas, Wasser, Wärme, Kommunikation

### Nr. 15 — Flächen für Lagerung von Wasser und Abwasser

### Nr. 18 — Flächen für Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft

- Wichtig für Eingriffs-Ausgleich
- Externes Ausgleichs-Bereich nach § 9 Abs. 1a BauGB

### Nr. 21 — Schutzpflichten gem. § 41 BImSchG

- Aktive und passive Schallschutz-Maßnahmen

### Nr. 24 — Festsetzung zur Erhaltung gesunder Wohn- und Arbeitsverhältnisse

- Passiver Schallschutz, gestaltete Außenwohnbereiche
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 3 — Festsetzungen außerhalb § 9 BauGB

### Häufige Fehler

#### Fehler 1: Dynamische Verweisung auf Spezialgesetze

- "Es gelten die Anforderungen der DIN xxxx in der jeweils geltenden Fassung"
- Problematisch: Dynamische Verweisung auf ändernde Spezial-Regelungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 2: Mobilitätskonzept als Festsetzung

- Häufig: B-Plan setzt "Mobilitätskonzept ist Bestandteil der Satzung" fest
- Problematisch: Konkrete Inhalte oft nicht in der Satzung, sondern nur in Anlagen-Papier
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 3: Energetische Anforderungen über GEG-Standard

- Festsetzung "Effizienzhaus 40" — zulässig nur als Festsetzung der Erschließungs-Tiefenstandards
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### Fehler 4: Werbe-Anlagen und Außengastronomie

- Über § 9 BauGB nur eingeschränkt regelbar
- Konkurrenz mit § 81 BayBO örtliche Bauvorschriften — meist diese Norm einschlägig

#### Fehler 5: Photovoltaik-Pflichten

- Über § 9 Abs. 1 BauGB problematisch
- Landesrechtliche Erlaubnis: Art. 44a BayBO (seit 01/2025)

## Schritt 4 — § 9 Abs. 5 6 7 BauGB Hinweise

### § 9 Abs. 5 — Vermerk im Plan

- Bauflächen mit erheblichen Bodennutzungs-Beschränkungen
- Z.B. Altlasten, Bergbauschäden

### § 9 Abs. 6 — Festsetzungen aus anderen Vorschriften

- Soweit andere Rechtsvorschriften Inhalts-Festsetzungen erlauben
- Z.B. Ausgleichs-Flächen nach Naturschutzrecht

### § 9 Abs. 7 — Geltungsbereich

- Räumlicher Geltungsbereich

## Schritt 5 — Bahnflächen § 38 BauGB

### Grundsatz

- Für Bahnflächen gelten Sondervorschriften
- BauGB-Festsetzungen sind eingeschränkt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konsequenz für nicht-entwidmete Bahnflächen

- Stadt kann keine baulichen Festsetzungen treffen
- Vor Entwidmung nach § 23 AEG kein wirksamer B-Plan möglich
- Bei dennoch erfolgter Festsetzung: Teil-Nichtigkeit oder Gesamt-Nichtigkeit

### Prüfungs-Schritt

- Welche Flurstücke sind als Bahnflächen vermerkt?
- Liegt eine Entwidmungs-Entscheidung der Eisenbahn-Verwaltung vor?
- Datum Entwidmung vs. Datum Satzungs-Beschluss

## Schritt 6 — Hochhäuser, Gebäude-Hochhaus-Verordnung

### Bayerische Hochhaus-Richtlinie

- Gebäude über 22 m Hochhaus nach Art. 2 Abs. 4 BayBO
- Brandschutz-Anforderungen
- Festsetzung Hochhaus-Standorte über § 9 Abs. 1 Nr. 1 + Nr. 2 BauGB

### Höhen-Festsetzung

- Wand-/Trauf-/First-Höhe nach § 18 BauNVO
- Bezugshöhe muss klar definiert sein

### Verschattung

- Bei Hochhäusern Verschattungs-Studie erforderlich
- Ermittlungspflicht § 2 Abs. 3 BauGB
- Im Plangebiet-Inneren und in Nachbarschaft

## Schritt 7 — Stellplatz-Festsetzungen

### Rechtsgrundlage

- § 9 Abs. 1 Nr. 4 BauGB (Stellplätze und Garagen)
- Art. 47 BayBO Grundsatz Stellplatzpflicht
- Art. 81 BayBO Stellplatzsatzung als örtliche Bauvorschrift

### Reduzierung durch B-Plan

- Art. 47 Abs. 2 Satz 2 BayBO: B-Plan kann abweichend festsetzen
- Voraussetzungen:
 - städtebauliche Rechtfertigung
 - anderweitige Bedarfsdeckung (z.B. ÖPNV-Nähe, Mobilitätskonzept)
 - Verhältnismäßigkeit

### Praktische Höchstgrenze

- Reduzierung über 50 % verlangt besondere Begründung
- Bei nahezu vollständigem Stellplatz-Verzicht: tragfähiges Mobilitätskonzept zwingend

## Schritt 8 — Schallschutz-Festsetzungen

### Rechtsgrundlage

- § 9 Abs. 1 Nr. 24 BauGB (Erhaltung gesunder Wohn-/Arbeitsverhältnisse)
- § 9 Abs. 1 Nr. 21 BauGB (Schutz-Maßnahmen nach BImSchG)

### Festsetzungs-Typen

- **Aktiver Schallschutz** — Lärmschutzwall, -wand (Festsetzung Lage, Höhe)
- **Passiver Schallschutz** — Schalldämmungs-Anforderungen Außenbauteile
- **Festsetzung Außenwohnbereiche** — bei zulässigen Pegeln

### DIN 18005

- Orientierungswerte:
 - Reines Wohngebiet 50 dB(A) Tag / 35 dB(A) Nacht
 - Allgemeines Wohngebiet 55 / 40 dB(A)
 - Mischgebiet 60 / 45 dB(A)
 - Urbanes Gebiet 63 / 48 dB(A)
- Statische Bezugnahme zulässig

### TA Lärm

- Bei Anlagen-Festsetzungen
- Statische Bezugnahme

## Schritt 9 — Naturschutz-Festsetzungen

### § 9 Abs. 1 Nr. 18 BauGB

- Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Boden, Natur und Landschaft
- Externe Ausgleichs-Maßnahmen § 9 Abs. 1a BauGB

### § 9 Abs. 1 Nr. 20 BauGB

- Flächen für Maßnahmen zum Schutz vor Naturgewalten
- Hochwasserschutz, Bodenerosionsschutz

### Verzahnung BNatSchG

- Eingriffs-Ausgleichs-Bilanz nach § 18 BNatSchG
- Festsetzung Vermeidungs-, Minderungs- und Ausgleichs-Maßnahmen

## Schritt 10 — Prüfraster für Mandanten-Vertretung

### Schritt 10.1 — Festsetzungs-Inventar

- Welche Festsetzungen enthält der Plan?
- Jeweils Rechtsgrundlage benennen lassen

### Schritt 10.2 — Außerhalb-Katalog-Prüfung

- Sind Festsetzungen ohne erkennbare Rechtsgrundlage in § 9 BauGB?
- Bei Verstoß: Teil-Nichtigkeit / Gesamt-Nichtigkeit?

### Schritt 10.3 — Höchstgrenzen-Prüfung § 17 BauNVO

- Werden GRZ/GFZ überschritten?
- Liegen die Voraussetzungen für Überschreitung § 17 Abs. 2 BauNVO vor?
- Begründung im Plan ausreichend?

### Schritt 10.4 — Dynamische Verweisungen

- Bezugnahme auf "jeweils geltende Fassung" einer DIN-Norm?
- Dynamische Verweisung unzulässig → Bestimmtheits-Mangel

### Schritt 10.5 — Mobilitätskonzept-Festsetzung

- Konkret in der Satzung oder nur in Anlage?
- Bestimmtheit ausreichend?

## Schritt 11 — Anwendung auf Bebauungsplan Augsburg Nr. 900

**Beispielsfälle:**

a) **§ 11 Satzung "Mobilitätskonzept"** — Anlage B-1, nur Stichpunktliste. Bestimmtheits-Mangel.

b) **§ 12 Satzung "Energetische Anforderungen"** — Festsetzung "KfW-Effizienzhaus 40". Bezugnahme auf "den jeweils gültigen Standard nach GEG bezogen" — dynamische Verweisung, problematisch.

c) **§ 9 Abs. 4 Satzung "Künstliche Nisthilfen"** — Festsetzung 60 Mauersegler-Nisten + 30 Mehlschwalben-Nisten. § 9 Abs. 1 Nr. 18 BauGB iVm BNatSchG einschlägig. Festsetzung zulässig.

d) **§ 13 Satzung "Materialgebote Fassaden"** — Stoff- und Farbgebote. Über Art. 81 BayBO örtliche Bauvorschrift einschlägig — § 9 BauGB nicht ausreichend.

e) **§ 6 Satzung "Stellplatz 0,3/WE"** — Reduzierung auf 30 % der Stellplatzsatzung-Werte. Art. 47 Abs. 2 Satz 2 BayBO grundsätzlich zulässig, aber **70 % Reduzierung benötigt tragfähiges Mobilitätskonzept**. Im konkreten Fall fragwürdig.

f) **§ 18 Satzung "Bahnflächen"** — Hinweis auf nicht-entwidmete DB-Flächen. § 38 BauGB einschlägig — **keine Festsetzungen zulässig** auf nicht-entwidmeten Bahnflächen.

## Verzahnung mit anderen Skills

- `erforderlichkeit-1-abs-3-baugb`
- `abwaegungsgebot-1-abs-7-baugb`
- `immissionsschutz-laerm-bauleitplanung`
- `stellplatzsatzung-bay-bauordnung`
- `vorhabenbezogener-bebauungsplan-12-baugb`

## Quellen

- BauGB §§ 9, 30, 38
- BauNVO §§ 1-26
- PlanzVO
- BayBO Art. 47, 81
- **BVerwG 04.05.2022, 4 CN 2.21** — Konzentrationszonen-Planung Wind/Solar (bverwg.de)
- **BVerwG 03.04.2020, 4 CN 2.19** — Erhaltungssatzung § 172 BauGB (bverwg.de)
- **BVerwG 17.06.2020, 4 CN 6.18** — Bekanntmachung Bebauungsplan, Anstossfunktion (bverwg.de)
- **BVerwG 11.04.2024, 4 BN 50.23** — Klimaschutz als Abwaegungsbelang (bverwg.de)
- Konkrete weitere Entscheidungen vor Ausgabe per bverwg.de mit Datum verifizieren
- Ernst/Zinkahn/Bielenberg BauGB
- Battis/Krautzberger/Löhr BauGB
- Söfker BauNVO

---

## Skill: `jahresfrist-47-abs-2-vwgo`

_Mandant moechte Normenkontrollantrag stellen und Anwalt prüft ob die Jahresfrist noch laeuft. § 47 Abs. 2 S. 1 VwGO Jahresfrist Normenkontrolle. Prüfraster: Fristbeginn ortsuebliche Bekanntmachung § 10 Abs. 3 BauGB fehlerhafte Bekanntmachung kein Fristbeginn Wiedereinsetzung § 60 VwGO ergaenzende..._

# Jahresfrist § 47 Abs. 2 VwGO

## Schritt 1 — Wortlaut und Grundregel

### § 47 Abs. 2 S. 1 VwGO
- Der Antrag kann innerhalb eines Jahres nach Bekanntmachung der Rechtsvorschrift gestellt werden

### Frist-Verkürzung 2007
- Vor dem 1.1.2007 zwei Jahre
- Durch Gesetz vom 22.12.2006 auf ein Jahr verkürzt
- Übergangsfristen längst abgelaufen

## Schritt 2 — Fristbeginn Bekanntmachung

### Bekanntmachung des B-Plans § 10 Abs. 3 BauGB
- Der Beschluss als Satzung ist ortsüblich bekanntzumachen
- In Bayern regelmäßig Veröffentlichung im Amtsblatt der Gemeinde
- Oder in der Tageszeitung, wenn Hauptsatzung dies vorsieht
- Online-Veröffentlichung zusätzlich, aber nicht allein konstitutiv

### Was wird bekanntgemacht
- Beschluss als Satzung
- Anstoßfunktion: Hinweis wo der Plan einsehbar ist
- Hinweis auf Beachtlichkeit der Verletzung von Vorschriften nach § 215 BauGB
- Hinweis auf Voraussetzungen für Entschädigungsanspruch § 44 BauGB
- Hinweis auf nachträgliche Geltendmachung

### Fehlerhafte Bekanntmachung
- Bei Fehlen der Hinweise auf § 215 BauGB läuft die Rügefrist nicht (§ 215 Abs. 2 BauGB)
- Bei vollständig fehlerhafter Bekanntmachung (z.B. unrichtiger Ort, fehlende Anstoßfunktion) kein Fristbeginn der Jahresfrist
- BVerwG ständige Rechtsprechung — gute Angriffsfläche

## Schritt 3 — Fristberechnung

### Fristbeginn
- Tag der Bekanntmachung zählt nicht mit (§ 187 Abs. 1 BGB analog)
- Bei Veröffentlichung 12.6.2024 läuft die Frist ab 13.6.2024

### Fristende
- Genau ein Jahr nach Beginn (§ 188 Abs. 2 BGB analog)
- Bekanntmachung 12.6.2024 — Fristende 12.6.2025, 24 Uhr
- Wenn Fristende auf Samstag, Sonntag oder Feiertag fällt — nächster Werktag (§ 222 Abs. 2 ZPO i.V.m. § 173 VwGO)

### Praxis Fristenkalender
- Eintrag Hauptfrist
- Vorfrist 1: 2 Wochen vor Ablauf
- Vorfrist 2: 4 Wochen vor Ablauf
- Drei-Augen-Kontrolle Vorlage Anwältin

## Schritt 4 — Antragseingang § 47 VwGO

### Form
- Schriftsatz an das zuständige OVG/VGH (Bayern: BayVGH)
- Eingang Original oder elektronischer Schriftsatz § 55a VwGO über beA
- Eingangsstempel maßgeblich

### Adressat
- BayVGH-Geschäftsstelle München
- bei elektronischer Übermittlung beA an die jeweilige Senatsgeschäftsstelle

## Schritt 5 — Wiedereinsetzung in den vorigen Stand

### § 60 VwGO
- Wiedereinsetzung bei unverschuldeter Versäumung
- Antrag innerhalb von zwei Wochen nach Wegfall des Hindernisses
- Glaubhaftmachung der Wiedereinsetzungstatsachen
- Nachholung der versäumten Handlung innerhalb der Antragsfrist

### Verschulden Mandant / Anwalt
- Anwaltsverschulden wird Mandanten zugerechnet § 173 VwGO i.V.m. § 85 Abs. 2 ZPO
- Bei Fristversäumung durch Anwältin Wiedereinsetzung in der Regel ausgeschlossen — Haftungsfrage

### Höhere Gewalt
- Plötzliche schwere Erkrankung
- Postsendung durch Naturkatastrophe vereitelt
- Betrug oder Täuschung durch Behörde

## Schritt 6 — Heilung durch ergänzendes Verfahren

### § 214 Abs. 4 BauGB
- Mängel können durch ergänzendes Verfahren behoben werden
- Erneuter Beschluss, erneute Bekanntmachung
- Neue Jahresfrist beginnt mit neuer Bekanntmachung
- Aber nur soweit der ergänzte Plan reicht

### Strategische Konsequenz
- Wenn Plan kurz vor Klagefrist nochmals "geheilt" wird — Frist beginnt neu
- Wenn Heilungsversuch unzureichend ist — Angriffspunkt im Hauptsacheverfahren

## Schritt 7 — Parallelfrist § 215 BauGB

### Rügefrist Verfahrensfehler
- Beachtliche Mängel des Verfahrens und der Form werden unbeachtlich, wenn sie nicht innerhalb eines Jahres nach Bekanntmachung schriftlich gegenüber der Gemeinde gerügt werden
- § 215 Abs. 1 Nr. 1 BauGB
- Gilt für formelle Mängel, die nicht ohnehin nach § 214 Abs. 1 BauGB unbeachtlich sind

### Rügefrist Abwägungsfehler
- § 215 Abs. 1 Nr. 3 BauGB
- Mängel im Abwägungsvorgang werden unbeachtlich, wenn nicht binnen Jahresfrist gerügt
- Materielle Abwägungsergebnis-Fehler bleiben unbeachtlich-Frei

### Rüge-Adressat
- Schriftliche Rüge gegenüber der Gemeinde, nicht gegenüber dem Gericht
- Eingang bei der Stadtverwaltung zählt
- Trotzdem zeitgleich mit Normenkontrollantrag vorbereiten

### Hinweis-Erfordernis
- Frist läuft nur, wenn auf sie in Bekanntmachung hingewiesen wurde
- Fehlt Hinweis — keine Rügefrist (§ 215 Abs. 2 BauGB)

## Schritt 8 — Praxisablauf

### Tag 0 — Mandatsannahme
- Bekanntmachungsdatum erfassen
- Hauptfrist und Rügefrist berechnen
- Fristenkalender Eintrag mit Vorfristen

### Phase 1 — Verfahrenskette und Akteneinsicht
- Akteneinsicht bei der Gemeinde § 29 VwVfG (BayVwVfG)
- Vorbereitung Rügeschreiben § 215 BauGB

### Phase 2 — Rüge absenden
- 4 Wochen vor Ablauf Jahresfrist: Rüge per Einschreiben an Gemeinde
- Rüge enthält alle erkannten Verfahrens- und Abwägungsfehler
- Aufbewahrung Postzustellungsurkunde

### Phase 3 — Normenkontrollantrag
- 2 Wochen vor Ablauf Jahresfrist: Schriftsatz bei BayVGH
- Eingang über beA mit Empfangsbekenntnis

## Schritt 9 — Häufige Fristfehler

- Fristbeginn auf Aufstellungsbeschluss statt Bekanntmachung gesetzt — falsch
- Bekanntmachung im Internet statt Amtsblatt als Fristbeginn — abhängig von Hauptsatzung
- Rügefrist § 215 BauGB übersehen — materielle Präklusion
- Vorfristen nicht eingetragen — Risiko bei Krankheit
- Eingang per Fax am Freitagabend ohne Eingangsbestätigung — Beweisproblem

## Quellen

- VwGO § 47 Abs. 2, § 55a, § 60, § 173
- BauGB § 10 Abs. 3, § 214, § 215, § 44
- ZPO § 85 Abs. 2, § 222 Abs. 2
- BGB § 187 Abs. 1, § 188 Abs. 2
- BVerwG, Urteil vom 26.4.2007 – 4 CN 3.06 (Bekanntmachung)
- BVerwG, Beschluss vom 15.4.1988 – 4 N 4.87 (Anstoßfunktion)

## Ergänzende Rechtsprechung (Stand 05/2026)

- **BVerwG 17.06.2020, 4 CN 6.18**: Anforderungen an die Bekanntmachung von Bebauungsplaenen — Anstossfunktion und Fristbeginn § 47 Abs. 2 VwGO. Quelle: bverwg.de.
- **BVerwG 03.04.2020, 4 CN 2.19** (Erhaltungssatzung): Bekanntmachung und Fristbeginn für den Normenkontrollantrag. Quelle: bverwg.de.
- **OVG NRW** und andere OVG/VGH: laufende Rspr. zu Bekanntmachungsmaengeln und Frist; konkrete Aktenzeichen ueber landesrecht-nrw.de bzw. die jeweilige Landesjustiz-Datenbank verifizieren.

Vor Ausgabe per bverwg.de mit Datum und Aktenzeichen verifizieren.

---

## Skill: `kommunalabgaben-und-beitragssatzungen`

_Kommunalabgaben- und Beitragssatzungen: Gebühren, Beiträge, Fremdenverkehr, Abwasser, Elternbeiträge, Kalkulation und Gleichheitssatz.; Normanker: VwGO § 47; KAG der Länder; Art. 3 GG; Äquivalenz- und Kostendeckungsprinzip; macht § 47 VwGO als allgemeines Satzungs- und Rechtsverordnungswerkzeug n..._

# Kommunalabgaben- und Beitragssatzungen: Gebühren, Beiträge, Fremdenverkehr, Abwasser, Elternbeiträge, Kalkulation und Gleichheitssatz.

## Auftrag

Dieser Skill löst § 47 VwGO aus der reinen Bauleitplanung. Er prüft, ob eine im Rang unter dem Landesgesetz stehende Rechtsvorschrift direkt vor dem OVG/VGH überprüft werden kann oder ob nur eine Inzidentkontrolle im Verfahren gegen einen Einzelakt passt.

## Normanker

VwGO § 47; KAG der Länder; Art. 3 GG; Äquivalenz- und Kostendeckungsprinzip. Vor jeder Ausgabe muss das jeweilige Landesrecht geprüft werden, weil § 47 Abs. 1 Nr. 2 VwGO die Normenkontrolle außerhalb der BauGB-Fälle nur eröffnet, soweit Landesrecht dies bestimmt.

## Prüfprogramm

1. Normtyp: Satzung, Rechtsverordnung, Bebauungsplan, Polizeiverordnung, Benutzungssatzung oder bloßer Verwaltungsakt?
2. Statthaftigkeit: § 47 Abs. 1 Nr. 1 oder Nr. 2 VwGO, Landesrechtseröffnung, Rang unter Landesgesetz.
3. Antragsteller: mögliche Rechtsverletzung, Adressat, Eigentümer, Nutzer, Gemeinde, Verband oder Konkurrent.
4. Frist und Rechtsschutzbedürfnis: Jahresfrist, fortbestehende Beschwer, Parallelverfahren.
5. Materielle Kontrolle: Ermächtigung, Zuständigkeit, Verfahren, Bekanntmachung, Bestimmtheit, Gleichheit, Verhältnismäßigkeit.
6. Rechtsfolge: Unwirksamkeit, Bekanntmachung der Entscheidung, Wirkung auf Folgebescheide, neue Satzung.

## Ausgabe

Erzeuge eine Statthaftigkeitsskizze, Satzungs-Red-Team, Eilantragsskizze, Schriftsatzgliederung oder Bürger-/Mandantenbrief.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

