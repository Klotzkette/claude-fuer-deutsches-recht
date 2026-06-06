---
name: nda-pruefungsvorschlaege-saas-msa
description: "Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur eigenständigen Erstprüfung. Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein NDA erkannt wird im Vertragsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# NDA-/Geheimhaltungsvereinbarung-Prüfung

## Arbeitsbereich

Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur eigenständigen Erstprüfung. Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein NDA erkannt wird. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; §§ 305 ff. BGB, NDA, SaaS- — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Eingehende Geheimhaltungsvereinbarungen (NDA, GHV, Verschwiegenheitserklärung) schnell einordnen: GRÜN bedeutet "zur Unterzeichnung weiterleiten"; GELB bedeutet "ein bis zwei konkrete Punkte brauchen Anwaltblick"; ROT bedeutet "vor Verhandlung Rechtsbeistand einschalten". Maßgebliche Rechtsbasis: §§ 17 ff. GeschGehG (Schutz von Geschäftsgeheimnissen), § 241 Abs. 2 BGB (Schutzpflichten), § 307 BGB (AGB-Kontrolle), GmbHG/AktG-Verschwiegenheitspflichten.

## Eingaben

- Geheimhaltungsvereinbarung (Datei-Upload oder Direkteingabe)
- Kontext: Wer ist Offenlegender, wer ist Empfänger? Evaluierungsrichtung?
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`

## Ziel-Bestimmung

Vor der Ausgabe prüfen, wohin das Dokument geht. Wenn ein Ziel genannt wurde (Kanal, Verteiler, Gegenpartei), fragen, ob es innerhalb des Vertraulichkeitskreises liegt. Öffentliche Kanäle, unternehmensweite Verteiler, Gegenseite, Lieferanten und Mandanten (für Arbeitsergebnis) brechen den Schutz. Bei Hinweis auf externen Empfänger: Kennzeichnung und Auswahl anbieten: (a) vertrauliche Version für Recht, (b) bereinigte Version für weiteren Empfänger, (c) beides.

## Ablauf

### Schritt 1: Playbook laden

**Welche Seite?** Vor der Playbook-Anwendung ermitteln, auf welcher Seite das Unternehmen steht.
- Lieferant/Partner evaluiert Ihr Produkt → Verkäuferseite
- Sie evaluieren deren Produkt/Dienstleistung → Käuferseite
- Gegenseitige NDA: Wessen Muster? In welche Richtung läuft die Hauptoffenlegung?
- Falls nicht klar: fragen.

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Playbook` → zutreffende Seite → `NDA-Triage-Positionen` lesen. Diese Positionen sind die Quelle der GRÜN/GELB/ROT-Entscheidung für dieses Team.

Falls keine NDA-Triage-Positionen konfiguriert: Nutzer fragen und Antwort in der CLAUDE.md festhalten.

### Schritt 2: Umfangsprüfung

**Vor NDA-spezifischer Prüfung:** Stellt das Dokument mehr auf, als sein Name andeutet?

Typische Zusatz-Regelungen in NDA-Kleidung: Wettbewerbsverbote, Abwerbungsverbote, Exklusivität, IP-Übertragungen, Vorkaufsrechte, Lizenzerteilungen, Schiedsklauseln mit breitem Anwendungsbereich.

Falls solche Regelungen vorhanden: **Automatisch GELB, unabhängig von NDA-Einzelprüfung.** Kennzeichnen:

> Dieses Dokument ist als NDA bezeichnet, enthält aber [Wettbewerbsverbot / IP-Übertragung / Exklusivität / …]. Es ist mehr als eine Geheimhaltungsvereinbarung. Anwaltliche Prüfung erforderlich.

Ein Dokument, das inhaltlich ein Dienstleistungsvertrag, ein Term Sheet oder ein Covenant-Paket ist, niemals stillschweigend durch NDA-Triage schleusen.

### Schritt 3: Triage

Triage-Buckets:

#### GRÜN – zur Unterzeichnung weiterleiten

Die NDA erfüllt jede Position im Playbook, kein Punkt löst ein ROT aus. Vor GRÜN-Vergabe prüfen:

- Hat das Praxisprofil vom Anwalt geprüfte NDA-Triage-Positionen? Falls nein: GRÜN nicht vergeben (s. u.).
- Jede Playbook-Position einzeln prüfen und im Ergebnis dokumentieren.

**GRÜN setzt anwaltlich geprüfte Playbook-Positionen voraus.** GRÜN ist der einzige Weg zur Unterzeichnung ohne erneute anwaltliche Prüfung. Ohne geprüfte Positionen in der CLAUDE.md:

> Ich kann GRÜN ohne anwaltlich geprüfte NDA-Positionen im Praxisprofil nicht vergeben. Bitte `/vertragsrecht:vertragsrecht-kaltstart-interview` mit dem Syndikusanwalt/Außenanwalt ausführen, oder diese NDA zur anwaltlichen Prüfung vorlegen. GRÜN gegen Standardwerte vergeben bedeutet, dass ein Nicht-Jurist die Positionen gesetzt hat, auf die der nächste Nicht-Jurist vertraut.

**Ausgabe (GRÜN):**

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

## NDA-Triage: [Vertragspartner]

GRÜN – zur Unterzeichnung weiterleiten

### Kurzübersicht

Keine Beanstandungen nach Playbook. Weiterleitung zur Unterzeichnung im Standardprozess.

| Prüfpunkt | Ergebnis | Playbook-Verweis |
|---|---|---|
| [Punkt] | bestanden | [CLAUDE.md-Abschnitt] |

**Nächster Schritt:** [An [CLM] Standard-NDA-Ablauf | An [Genehmiger] zur Unterzeichnung]
```

**Nicht-Juristen-Hinweis:** Falls Nutzerrolle = Nicht-Jurist:

> Dieser Schritt hat rechtliche Folgen (die NDA-Unterzeichnung bindet das Unternehmen). Wurde dies mit einem Rechtsanwalt besprochen? Bei Nein: Kurzüberblick für das Gespräch mit dem Anwalt:
>
> [1-seitige Zusammenfassung: Vertragspartner, Richtung (gegenseitig / einseitig), geprüfte Playbook-Punkte, nicht abgedeckte Punkte, Risiken bei Unterzeichnung im Status quo, drei Fragen an den Anwalt.]

#### GELB – einzelne Punkte brauchen Anwaltblick

Ein oder mehrere Punkte weichen vom Playbook ab, sind aber keine kategorischen K.-o.-Kriterien; oder ein Punkt erscheint, den das Playbook nicht adressiert.

**Ausgabe (GELB):**

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

## NDA-Triage: [Vertragspartner]

GELB – Kennzeichnung für [Genehmiger]

### Kurzübersicht

- [Eine-Zeile-Handlungsempfehlung, z. B. "Wettbewerbsverbot in § 6 streichen oder zeitlich/räumlich eingrenzen"]
- [Weitere Empfehlung]

### Gekennzeichnete Punkte

**1. [Problem]** – § [X]
 Was: [eine Zeile]
 Warum gekennzeichnet: [eine Zeile – welche Playbook-Position betroffen, oder "Playbook schweigt dazu"]
 **Rechtliches Risiko:** [🔴/🟠/🟡/🟢] | **Geschäftliche Reibung:** [🔴/🟠/🟡/🟢]
 Wahrscheinliche Lösung: [akzeptieren / bestimmten Punkt verhandeln / kontextabhängig]

[für jeden Punkt wiederholen]

### Unproblematische Punkte

| Prüfpunkt | Ergebnis | Playbook-Verweis |
|---|---|---|
| [bestandene Punkte] | bestanden | [CLAUDE.md-Abschnitt] |

**Nächster Schritt:** [Genehmiger] zu den gekennzeichneten Punkten befragen, dann zur Unterzeichnung weiterleiten.
```

#### ROT – stopp, zuerst Rechtsrat einholen

Die NDA trifft eine "Nie-akzeptieren"-Position des Playbooks, oder die Vertragsstruktur widerspricht dem Standardansatz des Teams.

**Ausgabe (ROT):**

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

## NDA-Triage: [Vertragspartner]

ROT – nicht weiterleiten; zuerst Rechtsrat einholen

### Kurzübersicht

- [Eine-Zeile-Handlungsempfehlung, z. B. "§ 4 – zur Rechtsabteilung weiterleiten"]

### Kritische Punkte

**1. [Problem]** – § [X]
 > "[genaues Zitat]"
 Warum problematisch: [konkretes Risiko; betroffene Playbook-Position zitieren]
 **Rechtliches Risiko:** [🔴/🟠/🟡/🟢] | **Geschäftliche Reibung:** [🔴/🟠/🟡/🟢]
 Empfohlene Reaktion: [eigenes Muster verwenden | konkrete Formulierung verhandeln | Abstand nehmen]

**Nächster Schritt:** Diese Triage an [GC oder genannte Eskalationsperson aus CLAUDE.md] schicken. Nicht in [CLM oder Genehmigungsworkflow] einpflegen. Vertragspartner nicht signalisieren, dass unterzeichnet wird.
```

## Prüfkatalog

### Gegenseitigkeit / Richtung

Ist die NDA gegenseitig oder einseitig? Position aus CLAUDE.md anwenden.

**Einseitige NDA:** Nicht sofort als ROT markieren. Kurz-Checkliste:
1. Offenbart nur eine Seite Geschäftsgeheimnisse?
2. Beschränkt sich die Offenlegung auf einen konkreten Zweck (z. B. Auftragnehmer erhält Zugang zu Technologie)?
3. M&A, Beschäftigung oder Investition? → Sofort an Rechtsabteilung (außerhalb des Anwendungsbereichs dieses Skills).

Antworten + CLAUDE.md-Position verwenden, um GRÜN/GELB/ROT zu bestimmen.

### Definition "Geschäftsgeheimnisse" (§ 2 Nr. 1 GeschGehG)

Umfang prüfen: markierungspflichtig vs. alles Offenbarte; Anforderungen an Markierung; Bestätigungsfenster für mündliche Offenbarungen. Position aus CLAUDE.md anwenden.

**GeschGehG-Hinweis:** Nach § 2 Nr. 1 GeschGehG sind Geschäftsgeheimnisse nur geschützt, wenn der Inhaber angemessene Geheimhaltungsmaßnahmen getroffen hat. Eine übermäßig weite Definition in der NDA, die auch öffentliche Informationen einschließt, kann die Durchsetzbarkeit gefährden. `[Trainingswissen – prüfen]`

### Ausnahmen vom Vertraulichkeitsschutz

Die fünf typischen Ausnahmen:
1. Allgemein bekannte Information (ohne Verschulden der empfangenden Partei)
2. Bereits bekannte Information der empfangenden Partei
3. Unabhängig entwickelte Information
4. Von Dritten ohne Vertraulichkeitsbindung erhaltene Information
5. Gesetzlich oder gerichtlich offenbarungspflichtige Information (mit Benachrichtigung des Offenlegenden, soweit zulässig)

Playbook-Position aus CLAUDE.md prüfen: Welche Ausnahmen sind zwingend erforderlich?

### Residuals-Klausel

Eine Residuals-Klausel erlaubt die Nutzung von Informationen, die im ungestützten Gedächtnis verbleiben. Zulässigkeit und Formulierungsbreite: Playbook-Position aus CLAUDE.md. Falls Playbook schweigt: fragen.

### Laufzeit und Nachpflichten (§ 2 Nr. 1 lit. b GeschGehG)

Erstlaufzeit, Nachpflichten-Dauer nach Vertragsende, gesonderte Schutzfrist für Handelsgeheimnisse prüfen. Position aus CLAUDE.md anwenden.

### Wettbewerbsverbote, Abwerbungsverbote (§§ 74 ff. HGB analog)

Auf Abwerbungsverbote (Mitarbeiter, Kunden), Wettbewerbsverbote, Exklusivität prüfen. Jurisdiktion beachten: Vertragliche Wettbewerbsverbote für Arbeitnehmer bedürfen Karenzentschädigung (§§ 74 ff. HGB); rein schuldrechtliche Klauseln mit Vertragsstrafe (§ 339 BGB) prüfen. Position aus CLAUDE.md anwenden.

### Gerichtsstand, Rechtswahl

Nach CLAUDE.md `## Playbook` → `Gerichtsstand und Rechtswahl`.

### Vertragsstrafe (§ 339 BGB)

Falls Vertragsstrafe vereinbart: Höhe auf Angemessenheit prüfen (§ 307 BGB, § 343 BGB Herabsetzungsrecht). Position aus CLAUDE.md anwenden.

## Redline-Granularität

**Eingriffe so klein wie möglich.** Ein Redline ist ein Verhandlungsinstrument, kein Neuentwurf. Standardmäßig die kleinstmögliche Änderung wählen:
- **Wort** vor Phrase. Phrase vor Satz. Teilsatz vor Klausel. Klausel nur ersetzen, wenn chirurgische Eingriffe schwerer zu lesen wären als ein Neuentwurf.
- Vollständige Klauselersetzung im Übermittlungsschreiben erläutern.

## Ausgaberegeln

**Sauber-NDA-Regel:** Wenn die NDA alle Punkte ohne Beanstandungen besteht, soll die Kurzübersicht nur lauten: "Keine Beanstandungen. Weiterleitung zur Unterzeichnung im Standardprozess." Keinen langen Bericht für eine saubere NDA erstellen.

**Abschluss-Handlung:** `closing_action` aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## NDA-Triage-Einstellungen` lesen und wortgetreu am Ende jeder Ausgabe anhängen. Falls nicht konfiguriert: "NDA im Standardgenehmigungsverfahren weiterleiten."

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen und Rspr.:
- GeschGehG (in Kraft seit 26.04.2019; Umsetzung Richtlinie (EU) 2016/943): https://www.gesetze-im-internet.de/geschgehg/
- § 2 Nr. 1 GeschGehG – Definition Geschaeftsgeheimnis; Angemessenheitsprinzip (Schutzmassnahmen-Erfordernis)
- §§ 16-20 GeschGehG (prozessualer Geheimnisschutz)
- **§ 273a ZPO** (Justizstandort-Staerkungsgesetz; in Kraft 01.04.2025): Erstreckung des prozessualen Geheimnisschutzes ueber den GeschGehG-Streit hinaus auf alle Zivilverfahren; Antrag jeder Partei moeglich; Ordnungsgeld bis 100.000 EUR bei Verstoss; § 6a ArbGG fuer Arbeitsgerichtsverfahren. https://www.gesetze-im-internet.de/zpo/__273a.html — Praxisfolge: NDA-Mechanik kann durch das prozessuale Schutzregime ergaenzt werden.
- § 241 Abs. 2 BGB – Schutzpflichten im Schuldverhaeltnis
- § 307 BGB – AGB-Inhaltskontrolle (bei vorformulierten Klauseln)
- § 339 BGB – Vertragsstrafe; § 343 BGB – richterliche Herabsetzung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kommentare:
- Köhler, in: Köhler/Bornkamm/Feddersen, UWG, 42. Aufl. 2024, § 2 GeschGehG Rn. 5 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Harte-Bavendamm/Henning-Bodewig, UWG, 4. Aufl. 2016, § 17 (alt) UWG Rn. 1 ff. (Vorläufer)

## Risiken / typische Fehler

- **Keine anwaltlich geprüften Playbook-Positionen:** GRÜN ohne geprüfte Positionen ist gefährlich; GELB ist die sichere Standardwahl bei Zweifel.
- **GeschGehG-Anforderungen übersehen:** Eine NDA, die nicht auf die Angemessenheitspflicht des § 2 Nr. 1 GeschGehG hinweist, kann Schutzlücken erzeugen.
- **Wettbewerbsverbote ohne Karenzentschädigung:** Bei Arbeitnehmern unwirksam (§§ 74 ff. HGB); bei Geschäftsführern/Freelancern gesondert prüfen.
- **Jurisdiktionswechsel:** Wenn die NDA ausländisches Recht wählt, überträgt sich die Triage nicht 1:1. ROT-kennzeichnen und Spezialist einschalten.
- **Mandantengeheimnis:** § 43a Abs. 2 BRAO, § 203 StGB bei jeder Weitergabe beachten.
