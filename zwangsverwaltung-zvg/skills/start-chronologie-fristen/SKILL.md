---
name: start-chronologie-fristen
description: "Einstieg, Schnelltriage und Fallrouting im Zwangsverwaltung ZVG-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständ..."
---

# Zwangsverwaltung ZVG — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Zwangsverwaltung ZVG**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme.

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
| `zvg-aktenanlage-objektcockpit` | Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten… |
| `zvg-berichtswesen-gericht` | Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage… |
| `zvg-besitzuebernahme` | Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte… |
| `zvg-bestellung-beschlagnahme` | Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden.… |
| `zvg-betriebskosten-hausgeld` | Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben… |
| `zvg-bieterangebot-bewertung` | Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot… |
| `zvg-glaeubiger-schuldner-kommunikation` | Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151… |
| `zvg-insolvenz-schnittstelle` | Schnittstelle Zwangsverwaltung und Insolvenz bei Insolvenz des Schuldners. Anwendungsfall Schuldner wird insolvent waehrend Zwangsverwaltung laeuft und Verwalter muss Koordination mit Insolvenzverwalter klären. Normen… |
| `zvg-instandhaltung-sicherung` | Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB… |
| `zvg-kommandocenter` | Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen starten. Normen §§ 146-161 ZVG Kernvorschriften.… |
| `zvg-konten-kassenfuehrung` | Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG… |
| `zvg-miet-und-pachtverwaltung` | Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen §… |
| `zvg-mieteinzug-rueckstaende` | Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose… |
| `zvg-öffentliche-lasten` | Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu… |
| `zvg-portal-recherche` | Recherche von Zwangsversteigerungsterminen im amtlichen ZVG-Portal für Investoren und Gläubiger. Anwendungsfall Mandant sucht Versteigerungsobjekte oder Gläubiger will Terminuebersicht. Normen §§ 87 ff. ZVG… |
| `zvg-quality-gate` | Quality Gate für Zwangsverwaltung vor Versand oder Rechnungslegung. Anwendungsfall Bericht Rechnungslegung oder Verteilungsplan soll ans Gericht versandt werden und muss vorher geprüft werden. Normen § 161 ZVG… |
| `zvg-raeumung-kuendigung` | Räumung Kündigung und Besitzkonflikte in der Zwangsverwaltung. Anwendungsfall Schuldner weigert sich auszuziehen oder Mieter soll nach Zwangsverwaltungsende kündigt werden. Normen § 150 ZVG Besitzrecht § 543 BGB… |
| `zvg-rechnungslegung` | Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG… |
| `zvg-simulation-training` | Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost… |
| `zvg-verkauf-versteigerung-schnittstelle` | Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG… |
| `zvg-versicherungen-gefahren` | Versicherungsschutz und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Gebaeudeversicherung ist nicht bezahlt oder Schadenfall ist eingetreten. Normen § 154 ZVG Erhaltungspflicht § 823 BGB… |
| `zvg-versteigerungsteilnahme` | Vorbereitung der Teilnahme am Zwangsversteigerungstermin für Gläubiger oder Bieter. Anwendungsfall Mandant will an Versteigerungstermin teilnehmen und benoetigt vollständige Vorbereitung. Normen §§ 87 ff. ZVG Termin §… |
| `zvg-verteilungsplan-155` | Verteilungsplan nach § 155 ZVG für die Auszahlung von Einnahmen in der Zwangsverwaltung. Anwendungsfall Einnahmen sind angefallen und müssen nach gesetzlicher Rangfolge verteilt werden. Normen § 155 ZVG Verteilung §… |

## Worum geht es?

Das Plugin unterstuetzt Zwangsverwalter und Zwangsversteigerungsbeteiligte bei der rechtssicheren Durchfuehrung von Zwangsverwaltungen und Zwangsversteigerungen nach dem Gesetz über die Zwangsversteigerung und die Zwangsverwaltung (ZVG). Es deckt den vollstaendigen Lebenszyklus ab: von der Prüfung des Bestellungsbeschlusses und der Besitzerlangung über die laufende Mietverwaltung, Konten- und Kassenfuehrung sowie Berichterstattung bis zur Jahresrechnung, dem Verteilungsplan und der Schnittstelle zur Zwangsversteigerung.

Zielgruppe sind Rechtsanwaelte und Verwalter, die als Zwangsverwalter bestellt sind, sowie Gläubiger und Investoren, die an Zwangsversteigerungsterminen teilnehmen wollen.

## Wann brauchen Sie diese Skill?

- Sie wurden als Zwangsverwalter bestellt und müssen das Objekt vollstaendig erfassen und das Verfahrenscockpit aufbauen.
- Mieter zahlen nicht und Sie müssen Rueckstaende einziehen, mahnen oder Klagen einleiten.
- Die Rechnungslegungsperiode endet und die Jahres- oder Schlussrechnung muss gerichtsfaehig erstellt werden.
- Der Schuldner wird insolvent und Sie müssen die Koordination mit dem Insolvenzverwalter sicherstellen.
- Ein Mandant will an einem Zwangsversteigerungstermin teilnehmen und benoetigt Vorbereitung und Bieterangebotsanalyse.

## Fachbegriffe (kurz erklaert)

- **Beschlagnahme** — Rechtliche Wirkung der Anordnung der Zwangsverwaltung: Der Schuldner verliert die Verfuegungsmacht über Fruechte und Nutzungen (§§ 146 148 ZVG).
- **Zwangsverwalter** — Vom Vollstreckungsgericht bestellte Person, die das Objekt im Interesse der Gläubiger verwaltet (§§ 150 ff. ZVG).
- **Treuhandkonto** — Getrenntes Konto für Einnahmen und Ausgaben der Zwangsverwaltung; Zwangsverwalter fuehrt es treuhänderisch.
- **Rechnungslegung** — Pflicht des Zwangsverwalters nach § 161 ZVG, dem Gericht jaehrlich Rechenschaft über Einnahmen und Ausgaben abzulegen.
- **Verteilungsplan** — Verteilung der Einnahmen nach gesetzlicher Rangfolge des § 155 ZVG auf Kosten, Gläubiger und sonstige Berechtigte.
- **Geringstes Gebot** — Mindestgebot in der Zwangsversteigerung nach § 74a ZVG: Maßstab für 7/10-Grenze und Zuschlagsversagung.
- **Absonderungsrecht** — Recht eines Gläubigers, Befriedigung aus einem bestimmten Gegenstand vorrangig zu verlangen (§ 49 InsO im Kontext der Insolvenzschnittstelle).
- **Rangklassen** — Gesetzliche Rangfolge der Befriedigung im ZVG-Verfahren nach § 10 ZVG.

## Rechtsgrundlagen

- §§ 146-161 ZVG — Kernvorschriften der Zwangsverwaltung
- § 155 ZVG — Einnahmen und Ausgaben; Verteilung
- § 161 ZVG — Rechnungslegungspflicht
- § 10 ZVG — Rangklassen im ZVG-Verfahren
- § 74a ZVG — Geringstes Gebot und Wertgrenzen
- § 81 ZVG — Sicherheitsleistung
- § 85a ZVG — Zuschlagsversagung
- §§ 535 543 573 BGB — Mietrecht (Mieteinzug, Kuendigung)
- § 165 InsO — Absonderungsrecht des Grundpfandglaeubigers
- § 823 BGB — Verkehrssicherungspflicht bei Objektmaengeln

## Schritt-für-Schritt: Einstieg ins Plugin

1. Bestellungsbeschluss prüfen und Objektcockpit anlegen (Aktenanlage, Beteiligtenregister, Mieterliste, Treuhandkonto).
2. Besitzerlangung vor Ort protokollieren und Gericht informieren.
3. Laufende Verwaltung: Mieteinzug, Betriebskosten, Instandhaltung, Versicherungen und Konten fuehren.
4. Berichterstattung an Gericht und Gläubiger; Qualitaetsgate vor Versand.
5. Rechnungslegung und Verteilungsplan am Ende der Periode oder bei Aufhebung erstellen.

## Skill-Tour (was gibt es hier?)

- `zvg-aktenanlage-objektcockpit` — Aktenanlage und Objektcockpit aufbauen: Objektkarte, Beteiligtenregister, Mieterliste und Fristen.
- `zvg-berichtswesen-gericht` — Besitzerlangungsbericht, Sachstandsbericht und Entscheidungsvorlagen für das Vollstreckungsgericht erstellen.
- `zvg-besitzuebernahme` — Besitzerlangung am Objekt protokollieren: Vor-Ort-Termin, Objektbeschreibung, Schlüsselliste und Gericht informieren.
- `zvg-bestellung-beschlagnahme` — Bestellungsbeschluss und Beschlagnahme rechtlich prüfen: Vollstaendigkeitsvermerk und naechste Schritte.
- `zvg-betriebskosten-hausgeld` — Betriebskosten, WEG-Hausgeld und laufende Objektkosten prüfen und abrechnen.
- `zvg-bieterangebot-bewertung` — Zwangsversteigerungsobjekte aus Investorensicht bewerten: Bietlimit, geringstes Gebot und Risikoeinschaetzung.
- `zvg-glaeubiger-schuldner-kommunikation` — Schriftwechsel mit Schuldner, Gläubiger, Mieter, Gericht, Versicherern und Dienstleistern.
- `zvg-insolvenz-schnittstelle` — Koordination mit Insolvenzverwalter bei Insolvenz des Schuldners waehrend laufender Zwangsverwaltung.
- `zvg-instandhaltung-sicherung` — Instandhaltung, Sicherung und Gefahrenabwehr am Objekt; Verkehrssicherungspflichten.
- `zvg-kommandocenter` — Triage und Routing zu allen ZVG-Skills; Statusampel und Tagesaufgaben.
- `zvg-konten-kassenfuehrung` — Treuhandkonto und Buchfuehrung: Einnahmen, Ausgaben, Saldo und Belegverzeichnis.
- `zvg-miet-und-pachtverwaltung` — Miet- und Pachtverwaltung einschliesslich Vertragsuebernahme und Zahlungseinzug.
- `zvg-mieteinzug-rueckstaende` — Mietrueckstaende einziehen: Mahnung, Ratenvereinbarung, Klage und Einzugsnachweis.
- `zvg-öffentliche-lasten` — Grundsteuer, Erschliessungsgebuehren und öffentliche Abgaben in der Rangklassenlogik behandeln.
- `zvg-portal-recherche` — ZVG-Portal-Recherche zu Versteigerungsterminen, Gutachten-Downloads und Terminlisten.
- `zvg-quality-gate` — Qualitaetsgate vor Versand oder Rechnungslegung: Ampelstatus und Freigabeentscheidung.
- `zvg-raeumung-kuendigung` — Raeumung, Kuendigung und Besitzkonflikte mit Schuldner oder Mieter bearbeiten.
- `zvg-rechnungslegung` — Jahresrechnung und Schlussrechnung gerichtsfaehig erstellen.
- `zvg-simulation-training` — Zwangsverwaltungs-Workflows im Simulationsmodus trainieren und demonstrieren.
- `zvg-verkauf-versteigerung-schnittstelle` — Schnittstelle zwischen laufender Zwangsverwaltung und Zwangsversteigerungsverfahren.
- `zvg-versicherungen-gefahren` — Versicherungsschutz prüfen und Schadenfall melden; Deckungsnachweis und Sicherungsmassnahmen.
- `zvg-versteigerungsteilnahme` — Vorbereitung der Teilnahme am Zwangsversteigerungstermin: Ausweis, Sicherheitsleistung, Bietstrategie.
- `zvg-verteilungsplan-155` — Verteilungsplan nach § 155 ZVG: Rangfolge, Betraege, Auszahlungsnachweis und Gerichtsbericht.

## Worauf besonders achten

- **Besitzerlangungsbericht zeitnah**: Das Gericht erwartet sofortige Meldung nach Besitzuebernahme; Verzoegerung kann zu Rueckfragen fuehren.
- **Treuhandkonto strikt getrennt**: Verwaltungseinnahmen dürfen nicht mit Eigengeldern des Verwalters vermischt werden.
- **WEG-Hausgeld als vorrangige Ausgabe**: § 10 ZVG stellt laufendes Hausgeld in eine besondere Rangklasse; Zahlungsverzug kann Schadensersatzpflicht ausloesen.
- **Insolvenzschnittstelle fruehzeitig klären**: Bei Insolvenz des Schuldners ändert sich das Absonderungsrecht; Abstimmung mit Insolvenzverwalter ist unverzueglich erforderlich.
- **Quality Gate vor jedem Gerichtsversand**: Bericht oder Rechnungslegung ohne vorherigen Gate-Lauf riskiert Rueckfragen und Gerichtsmaengel.

## Typische Fehler

- Vorausverfuegungen des Schuldners (Mietvorauszahlungen, Abtretungen) nicht geprueft; unbekannte Belastungen reduzieren auszahlbare Einnahmen.
- Mietrueckstaende zu lange belassen ohne Mahnung und Klageeinleitung; Forderungspraeskription und Insolvenz des Mieters drohen.
- Rechnungslegung ohne vollstaendige Belegpruefung; Gericht fordert Nachbesserungen.
- Bei Aufhebung der Zwangsverwaltung kein Übergabebericht für das Versteigerungsverfahren erstellt.
- Versicherungsschutz erst nach Schadenfall geprueft; rueckwirkende Deckungsluecken sind unvermeidlich.

## Quellen und Aktualitaet

- Stand: 05/2026
- ZVG in der aktuellen Fassung; Normbestand abrufbar unter https://www.gesetze-im-internet.de/zvg/
- Pfaendungsfreigrenzenbekanntmachung 2025 (BGBl. 2025 I Nr. 110) gilt vom 01.07.2025 bis 30.06.2026. Quelle: https://www.recht.bund.de/bgbl/1/2025/110/VO.html
- Justizstandort-Staerkungsgesetz (BGBl. 2025 I Nr. 318 vom 11.12.2025): Wertgrenzenreform ab 01.01.2026 wirkt sich auf Beschwerdesummen aus; Uebergangsvorschrift § 47 EGZPO.
- BGH V. ZS und VII. ZS aktuelle Linien zu Versteigerung und Zuschlag über https://www.bundesgerichtshof.de und https://dejure.org prüfen.
