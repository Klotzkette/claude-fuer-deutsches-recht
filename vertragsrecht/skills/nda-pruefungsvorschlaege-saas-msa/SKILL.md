---
name: nda-pruefungsvorschlaege-saas-msa
description: "NDA Pruefungsvorschlaege Saas MSA: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# NDA Pruefungsvorschlaege Saas MSA

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **NDA Pruefungsvorschlaege Saas MSA** im Plugin Vertragsrecht (BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nda-pruefung` | Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur eigenständigen Erstprüfung. Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein NDA erkannt wird. |
| `pruefungsvorschlaege` | Prüft und genehmigt (oder lehnt ab) ausstehende Playbook-Aktualisierungsvorschläge des Playbook-Monitor-Agenten und überträgt genehmigte Änderungen in das Kanzleiprofil. Lädt, wenn der Monitor Vorschläge gemeldet hat, wenn der Nutzer "Playbook-Vorschläge prüfen", "welche Playbook-Updates sind ausstehend" oder "Abweichungsvorschläge durchgehen" sagt. |
| `saas-msa-pruefung` | Prüfung von SaaS-Abonnement- und Rahmenverträgen (MSA) mit Schwerpunkt auf AGB-Kontrolle (§§ 305–310 BGB), automatischer Verlängerung, Preiseskalation, Datenschutz (Art. 28 DSGVO), Haftungsbegrenzung und Vertragsstrafe (§ 339 BGB). Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein SaaS- oder Abonnementvertrag erkannt wird. |

## Arbeitsweg

Im Plugin Vertragsrecht (BGB) gilt für **NDA Pruefungsvorschlaege Saas MSA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nda-pruefung`

**Fokus:** Schnelle Triage von eingehenden NDA-/Geheimhaltungsvereinbarungen in GRÜN / GELB / ROT, damit nur die Vereinbarungen anwaltliche Zeit beanspruchen, die sie wirklich brauchen. Geeignet für Vertrieb und BD zur eigenständigen Erstprüfung. Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein NDA erkannt wird.

# NDA-/Geheimhaltungsvereinbarung-Prüfung

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

## 2. `pruefungsvorschlaege`

**Fokus:** Prüft und genehmigt (oder lehnt ab) ausstehende Playbook-Aktualisierungsvorschläge des Playbook-Monitor-Agenten und überträgt genehmigte Änderungen in das Kanzleiprofil. Lädt, wenn der Monitor Vorschläge gemeldet hat, wenn der Nutzer "Playbook-Vorschläge prüfen", "welche Playbook-Updates sind ausstehend" oder "Abweichungsvorschläge durchgehen" sagt.

# Playbook-Vorschläge prüfen und genehmigen

## Zweck

Diese Skill führt durch ausstehende Vorschläge des Playbook-Monitor-Agenten
und überträgt genehmigte Änderungen in das Kanzleiprofil. Der Monitor beobachtet
Verhandlungsmuster: wenn ein Anwalt eine Abweichung vom Standard-Playbook
wiederholt billigt (Schwellenwert: 5 Mal in den letzten 12 Monaten), generiert
er einen Vorschlag, das Playbook an die gelebte Praxis anzupassen.

Lädt automatisch nach einer Monitor-Meldung oder wenn der Nutzer ausstehende
Vorschläge explizit abfragen möchte.

## Eingaben

Keine Argumente erforderlich — die Skill arbeitet aus der ausstehenden
Vorschlags-Datei. Die Vorschlagsdatei wird vom Playbook-Monitor-Agenten
geschrieben.

## Rechtlicher Rahmen

### Grundprinzip: Klauselkontrolle nach AGB-Recht

Playbook-Vorschläge betreffen typischerweise Klauselpositionen im Bereich
des BGB-Schuldrechts und des AGB-Rechts. Jede Anpassung einer Playbook-Position
muss an den gesetzlichen Grenzen gemessen werden:

- § 305 BGB — Einbeziehungsvoraussetzungen; eine Klausel, die nicht wirksam
 einbezogen wurde, ist keine Verhandlungsposition, die in ein Playbook gehört
- § 305c BGB — Überraschende und mehrdeutige Klauseln; eine Klausel, die
 nach Entstehung und Inhalt so ungewöhnlich ist, dass der Vertragspartner
 nicht mit ihr rechnet, wird nicht Vertragsbestandteil — auch ein Playbook,
 das solche Klauseln als "Standard" führt, erzeugt keine belastbaren Positionen
- § 307 Abs. 1 S. 2 BGB — Transparenzgebot; das Playbook muss die eigene
 Position klar und verständlich formulieren, um sie in Verhandlungen
 durchzusetzen und AGB-rechtliche Kontrolle zu bestehen
- § 307 Abs. 2 BGB — Abweichung von wesentlichen Grundgedanken der gesetzlichen
 Regelung als Indiz für unangemessene Benachteiligung
- §§ 308, 309 BGB — Klauselverbote; Positionen, die gegen diese Verbote
 verstoßen, dürfen nicht als reguläre Playbook-Positionen geführt werden

### Begründungspflicht mit verifizierten Quellen

Jeder Vorschlag zur Änderung einer Playbook-Position muss mit Quellen
begründet sein: zuerst Normtext, dann verifizierte Rechtsprechung mit Datum
und Aktenzeichen, danach nur konkret bereitgestellte oder lizenziert
verifizierte Literatur. Kommentar-, Handbuch- und Aufsatzfundstellen dürfen
nicht aus Modellwissen ergänzt werden.

### Leitentscheidungen für Playbook-Anpassungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Haftungsbeschränkung in AGB; Grenze der zulässigen Absenkung;
 § 309 Nr. 7 BGB)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Transparenzgebot; Änderungsklauseln müssen klar und verständlich sein)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Haftungsfreizeichnung für Vorsatz unwirksam; § 276 Abs. 3 BGB;
 § 309 Nr. 7 lit. b BGB; kein Verhandlungsspielraum für das Playbook)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Klauselkontrolle Gewährleistungsverkürzung; § 309 Nr. 8 BGB;
 Grenzen für Mängelrechtsausschluss in AGB)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (AGB-Einbeziehung im unternehmerischen Verkehr; § 305 Abs. 2 BGB)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 — Vorschlagsdatei laden

Lade den Playbook-Monitor-Agenten und führe Schritt 5 (Prüf- und
Genehmigungsablauf) aus.

Falls keine Vorschlagsdatei existiert oder sie leer ist:

> *Keine ausstehenden Vorschläge. Das Playbook ist aktuell.*

Nicht weiterprocedieren.

### Schritt 2 — Vorschläge einzeln vorstellen

Jeden Vorschlag vollständig anzeigen. Vier Optionen anbieten:

| Option | Bedeutung |
|---|---|
| **Übernehmen** | Änderung sofort in das Kanzleiprofil schreiben |
| **Ablehnen** | Vorschlag verwerfen; kein Schreiben |
| **Bearbeiten** | Vorschlag vor Übernahme anpassen |
| **Zurückstellen** | Vorschlag für spätere Entscheidung aufbewahren |

### Schritt 3 — Diff anzeigen vor Schreiben

Für **Übernehmen** oder **Bearbeiten**: Den exakten Diff
(alter Wert → neuer Wert) im Kanzleiprofil zeigen, bevor geschrieben wird.
Nur nach ausdrücklicher Bestätigung durch den Anwalt übertragen.

**Format des Diffs:**

```
## Playbook — Haftungsbeschränkung (Verwender-Seite)

AKTUELL:
Fallback-Position: 12 Monate Jahresvergütung

NEU (Vorschlag):
Fallback-Position: 18 Monate Jahresvergütung

Begründung (Monitor): 7 von 12 unterzeichneten Verträgen in den letzten
12 Monaten wurden mit 18 Monaten abgeschlossen. Muster liegt oberhalb
des Schwellenwerts (5 Mal).

Quelle: Nur verifizierte Rechtsprechung oder vom Nutzer bereitgestellte/lizenziert live geprüfte Literaturquelle mit exakter Fundstelle.
(Beleg für Zulässigkeit eines 18-Monate-Cap als Fallback live prüfen.)

Übernehmen? (ja / nein / bearbeiten)
```

### Schritt 4 — Ablehnen oder Zurückstellen

Entscheidung protokollieren. Kanzleiprofil unverändert lassen.

Bei **Ablehnen**: In Abweichungslog eintragen, mit Begründung des Anwalts
(falls angegeben) oder mit dem Vermerk "Abgelehnt ohne Begründung".

Bei **Zurückstellen**: Vorschlag für die nächste Runde erhalten.

### Schritt 5 — Abschluss nach allen Vorschlägen

Zusammenfassung zeigen: wie viele Vorschläge übernommen, abgelehnt,
zurückgestellt. Danach Vorschlagsdatei archivieren.

```
Ergebnis:
- 2 Vorschläge übernommen (Haftungsdeckel Fallback, Verjährungsfrist Gewährleistung)
- 1 Vorschlag abgelehnt (Gerichtsstand München → Frankfurt)
- 1 Vorschlag zurückgestellt (Datenlöschfrist AVV)

Kanzleiprofil aktualisiert. Vorschlagsdatei archiviert.
```

## Ausgabeformat

Für jeden Vorschlag: Vollständiger Vorschlagsblock (Klausel, aktueller Wert,
vorgeschlagener neuer Wert, Begründung, Quellenbeleg) + vier Optionen.
Nach Entscheidung: Diff-Anzeige vor Schreiben.
Am Ende: Gesamtübersicht aller Entscheidungen.

## Beispiel

**Szenario:** Der Playbook-Monitor hat festgestellt, dass die Kanzlei in
8 von 10 Fällen eine Verlängerung der Gewährleistungsverjährung auf 2 Jahre
(statt Kanzlei-Standard 1 Jahr) akzeptiert hat.

**Vorschlag:**

```
Klausel: Gewährleistung — Verjährungsfrist (Kunden-Seite)

AKTUELL:
Standardposition: 1 Jahr (§ 438 Abs. 2 BGB; zulässige AGB-Verkürzung
im B2B-Bereich)
Fallback: 1,5 Jahre

NEU (Vorschlag):
Fallback: 2 Jahre (gesetzlicher Regelfall § 438 Abs. 1 Nr. 3 BGB)

Begründung: 8/10 unterzeichneter Verträge aus den letzten 12 Monaten
wurden mit 2 Jahren abgeschlossen.

Quelle:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Grenzen Gewährleistungsverkürzung in AGB)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 (Zulässige Verjährungszeiträume in AGB)
```

Anwalt wählt "Übernehmen" → Diff angezeigt → Kanzleiprofil aktualisiert.

## Risiken und typische Fehler

- **Vorschlag ohne Quellenbeleg akzeptieren.** Jeder Vorschlag zur Änderung
 Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 unterlegt sein. Vorschläge ohne Beleg nicht als "Übernehmen"-fähig markieren.
- **Diff nicht anzeigen.** Ohne Anzeige des exakten Diffs kann der Anwalt
 nicht beurteilen, ob die Änderung korrekt ist. Niemals direkt schreiben
 ohne Bestätigung.
- **Zwingende Verbote als veränderbar darstellen.** Wenn ein Vorschlag eine
 Position betrifft, die gegen §§ 308, 309 BGB oder § 276 Abs. 3 BGB verstößt
 (z. B. Ausschluss der Haftung für Vorsatz oder Körperverletzung), diesen
 Vorschlag mit Fehlermeldung zurückweisen und nicht zur Genehmigung stellen.
- **Zurückgestellte Vorschläge vergessen.** Zurückgestellte Vorschläge bleiben
 in der Datei und werden beim nächsten Aufruf erneut vorgelegt.

## Quellenpflicht

Jeder Vorschlag in der Ausgabe muss enthalten:
- Den betroffenen Paragraphen (z. B. § 309 Nr. 7 BGB, § 438 BGB)
- Mindestens eine BGH-Entscheidung zur Klauselgrenze in korrekter Zitierweise
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 Ist eine Literaturquelle erforderlich, nur als "vom Nutzer bereitgestellte/lizenziert live geprüfte Quelle" mit exakter Fundstelle kennzeichnen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 3. `saas-msa-pruefung`

**Fokus:** Prüfung von SaaS-Abonnement- und Rahmenverträgen (MSA) mit Schwerpunkt auf AGB-Kontrolle (§§ 305–310 BGB), automatischer Verlängerung, Preiseskalation, Datenschutz (Art. 28 DSGVO), Haftungsbegrenzung und Vertragsstrafe (§ 339 BGB). Wird von /vertragsrecht:vertragsprüfung geladen, wenn ein SaaS- oder Abonnementvertrag erkannt wird.

# SaaS-/MSA-Prüfung

## Zweck

SaaS-Verträge haben ein anderes Risikoprofil als einmalige Lieferantenverträge. Die Kosten akkumulieren über Verlängerungen, die Daten häufen sich an, und die Wechselkosten wachsen monatlich. Dieser Skill prüft unter Berücksichtigung dieser Besonderheiten. Er führt die Standard-Playbook-Prüfung aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` durch und ergänzt sie um einen SaaS-spezifischen Prüfaufschlag für die Punkte, die bei Abonnementverträgen besonders gefährlich sind.

## Eingaben

- SaaS-/MSA-Vertrag (Datei-Upload oder Direkteingabe)
- Ggf. Auftragsformular (Order Form) separat
- AVV/DPA (falls als separates Dokument)
- Kontext: Auftraggeber oder Auftragnehmer?
- Praxisprofil aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md`

## Akten-Kontext

Falls Akten-Arbeitsbereiche aktiviert, aktive Akte prüfen. Falls keine aktive Akte, fragen.

## Ablauf

### Schritt 1: Playbook laden und Seite bestimmen

**Welche Seite?** Vor der Playbook-Anwendung ermitteln:
- Gegenpartei ist SaaS-Anbieter, der die Plattform verkauft → Käuferseite
- Das Unternehmen ist SaaS-Anbieter, Gegenpartei ist Kunde → Verkäuferseite
- Reseller/White-Label? → Fragen: "Auf welcher Seite steht [Unternehmen] – Anbieter oder Kunde?"

Aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` den zutreffenden Playbook-Abschnitt lesen. Falls nicht konfiguriert: Setup-Befehl nennen.

AGB-Kontrolle nach §§ 305–310 BGB:
- Einbeziehungsvoraussetzungen (§ 305 Abs. 2 BGB) prüfen
- Überraschende Klauseln (§ 305c BGB)
- Transparenzgebot (§ 307 Abs. 1 S. 2 BGB)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei B2B: § 310 Abs. 1 BGB – eingeschränkte Kontrolle, aber § 307 BGB gilt

### Schritt 2: Standard-Playbook-Prüfung

Alle Standard-Checkpunkte aus dem Lieferantenvertrag-Prüfungs-Skill anwenden: Haftung, Freistellung, IP, Datenschutz, Laufzeit/Kündigung, Gerichtsstand. Ergebnisse in die SaaS-spezifische Ausgabe integrieren.

### Schritt 3: SaaS-spezifischer Prüfaufschlag

#### 3.1 Automatische Verlängerung (§ 309 Nr. 9 BGB; § 307 BGB)

Der häufigste Weg, bei dem ein SaaS-Deal schiefläuft: niemand bemerkt das Kündigungsfenster, und das Unternehmen ist für ein weiteres Jahr zum höheren Preis gebunden.

Prüfen und mit CLAUDE.md-Positionen vergleichen:

| Element | Inhalt | Playbook-Position |
|---|---|---|
| Verlängerungslaufzeit | z. B. gleich wie Erstlaufzeit / länger / mehrjährig | [aus CLAUDE.md] |
| Kündigungsfrist | Tage vor Verlängerung | [aus CLAUDE.md] |
| Kündigungsform | E-Mail / Schriftform / Portal / Einschreiben | [aus CLAUDE.md] |
| Preis bei Verlängerung | gleich / CPI-begrenzt / jeweils aktueller Listenpreis | [aus CLAUDE.md] |

**B2C-Hinweis:** § 309 Nr. 9 BGB verbietet stillschweigende Verlängerungen um mehr als 1 Jahr und Kündigungsfristen von mehr als 3 Monaten. Im B2B-Bereich gilt § 307 BGB als Maßstab; übermäßige Kündigungsfristen können unwirksam sein. `[Trainingswissen – prüfen]`

**Fristenerfassung:** Genaues Verlängerungsdatum und Kündigungsfenster unabhängig von Beanstandungen extrahieren. Daten für den Verlängerungstracker-Skill erfassen.

#### 3.2 Preiseskalation

Prüfen und mit CLAUDE.md vergleichen:

| Element | Inhalt |
|---|---|
| Jährliche Erhöhungsklausel | fester %, VPI, unbegrenzt |
| Überverbrauch-Preise | Veröffentlichte Preisliste / Prämienrate / undefiniert |
| Umfang "Vergütung" | nur Abonnement / "Zusatzleistungen" weit definiert |

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

#### 3.3 Datenportabilität und Exit

Wenn (nicht falls) das Unternehmen den Anbieter wechselt: Können die Daten mitgenommen werden?

| Element | Inhalt |
|---|---|
| Exportformat | offen/standardisiert / proprietär-dokumentiert / "wirtschaftlich zumutbar" |
| Export-Verfügbarkeit | Selbstbedienung jederzeit / auf Anfrage / nur bei Kündigung |
| Zugang nach Vertragsende | Tage nach Kündigung |
| Exportkosten | kostenlos / T&M / je GB oder Datensatz |
| Löschbestätigung | auf Anfrage / keine / Anbieter behält Derivate |

**DSGVO-Hinweis (Art. 20 DSGVO):** Datenportabilität ist für personenbezogene Daten ein Betroffenenrecht. Der AVV sollte Löschpflichten und Rückgabe nach Vertragsende regeln (Art. 28 Abs. 3 lit. g DSGVO). Anbieterbehalt "anonymisierter" Derivate: Playbook-Position aus CLAUDE.md prüfen.

#### 3.4 Verfügbarkeit und SLA

Nur relevant, wenn das Unternehmen vom Dienst abhängt. Bei Nice-to-have-Tools überspringen.

| Element | Inhalt |
|---|---|
| Verfügbarkeitszusage | Prozentsatz / "wirtschaftlich zumutbare Bemühung" |
| Messzeitraum | monatlich / quartalsweise / jährlich |
| Abhilfe | Service-Credits (Berechnung, Deckelung, ausschließliche Abhilfe?) |
| Wartungsfenster | definierter Zeitraum / Voranmeldung / unbegrenzt |
| Credit-als-ausschließliche-Abhilfe + Haftungsdeckel | Wechselwirkung prüfen |

**AGB-Hinweis:** Klauseln, die Service-Credits als ausschließliche Abhilfe für Ausfälle festschreiben und gleichzeitig die Haftung auf ein Minimum deckeln, können nach § 307 BGB unangemessen benachteiligend sein. `[Trainingswissen – prüfen]`

#### 3.5 Sub-Auftragsverarbeiter (Art. 28 Abs. 4 DSGVO)

Die Liste der Sub-Auftragsverarbeiter ändert sich über die Laufzeit des Abonnements. Das ist ein Datenschutzproblem mit SaaS-spezifischer Dynamik.

| Element | Inhalt |
|---|---|
| Genehmigungsmodell | allgemeine Genehmigung mit Widerspruchsrecht (Art. 28 II DSGVO) / spezifische Genehmigung |
| Benachrichtigungsfrist | Tage vor Hinzufügung |
| Widerspruchsrecht | ja / nein / Sonderkündigungsrecht |
| Sitz der Sub-Auftragsverarbeiter | EU/EWR / Drittland (Art. 46 DSGVO erforderlich) |

**Art. 28 DSGVO-Pflichtprüfung:** AVV muss abgeschlossen sein, wenn personenbezogene Daten verarbeitet werden. Pflichtinhalte nach Art. 28 Abs. 3 DSGVO: Gegenstand, Dauer, Art und Zweck der Verarbeitung; Art der personenbezogenen Daten; betroffene Personengruppen; Pflichten und Rechte des Verantwortlichen.

#### 3.6 Haftungsbegrenzung in SaaS-Kontext (§§ 305–310, 307 BGB)

Standard-Haftungsprüfung aus Lieferantenvertrag-Skill anwenden. Zusätzlich SaaS-spezifisch prüfen:

- **Datenverlust-Carveout:** Haftung für Datenverlust ausgeschlossen oder begrenzt? (Kann im Widerspruch zu DSGVO-Schadensersatz Art. 82 DSGVO stehen)
- **Haftungsdeckel + Credit-als-einzige-Abhilfe-Kombination:** Wenn Credits die einzige SLA-Abhilfe sind UND die Haftung auf wenige Monatsgebühren begrenzt ist, ist die Haftung de facto minimal.
- **Unbegrenzte Haftung für IP-Verletzungen:** Marktstandard, aber Wechselwirkung mit Gesamtdeckel prüfen.

#### 3.7 Vertragsstrafe (§§ 339, 343 BGB)

Falls Vertragsstrafe (z. B. bei SLA-Verstößen oder Datenschutzverstößen) vereinbart:
- Höhe angemessen? (§ 307 BGB; § 343 BGB Herabsetzungsrecht)
- Verhältnis zur Haftungsklausel: Ist die Vertragsstrafe auf den Haftungsdeckel angerechnet?
- Kumulationsproblem: Mehrere Vertragsstrafen-Tatbestände?

## Ausgabeformat

Memo mit folgendem Aufbau:

```markdown
VERTRAULICH – ANWALTLICHES ARBEITSERGEBNIS (§ 43a II BRAO)

⚠️ Prüfer-Hinweis
[Quellen, gelesene Seiten, gekennzeichnete Punkte, Aktualitätsprüfung]

# SaaS-/MSA-Prüfung: [Anbieter] – [Vertragsbezeichnung]

**Seite:** [Käufer / Verkäufer]
**Jahreswert (ACV):** [Betrag / nicht angegeben – bitte nennen für Eskalationsrouting]
**Laufzeit:** [Dauer, Verlängerung]
**AVV:** [beigefügt / per URL referenziert / fehlt]

---

## Zusammenfassung

[3–5 Sätze: Was ist das Wichtigste, was muss der Anwalt wissen?]

---

## Befunde (nach Schweregrad)

### 🔴 Blockierend
[Befund, §-Verweis, Zitat, Redline-Vorschlag, Eskalations-Empfehlung]

### 🟠 Hoch
[…]

### 🟡 Mittel
[…]

### 🟢 Niedrig / Zur Kenntnis
[…]

---

## SaaS-spezifische Extrakte

| Verlängerungsdatum | Kündigungsfrist | Kündigungsform | Preis bei Verlängerung |
|---|---|---|---|
| [Datum] | [Tage] | [Form] | [Methode] |

---

## Empfohlene Redlines

[Konkrete Klausel-Formulierungsvorschläge, chirurgisch und minimal]

---

## Nächste Schritte
[Entscheidungsbaum gemäß CLAUDE.md]
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Normen und Rspr.:
- §§ 305–310 BGB – AGB-Recht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 309 Nr. 7 BGB – Haftungsausschlussverbote
- § 309 Nr. 9 BGB – Vertragslaufzeit
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Art. 28 DSGVO – AVV; Art. 82 DSGVO – Datenschutz-Schadensersatz
- § 339 BGB – Vertragsstrafe; § 343 BGB – Herabsetzung

Kommentare:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **AVV fehlt, obwohl personenbezogene Daten verarbeitet werden:** Bußgeldrisiko Art. 83 Abs. 4 DSGVO; Haftungsrisiko Art. 82 DSGVO.
- **Automatische Verlängerung mit kurzer Frist und fehlende Kalenderüberwachung:** Für den Verlängerungstracker-Skill extrahieren.
- **Sub-Auftragsverarbeiter-Änderungen ohne Widerspruchsrecht:** Verstoß gegen Art. 28 Abs. 2 DSGVO bei spezifischer Genehmigung.
- **Credit-als-einzige-Abhilfe + Null-Haftung:** Wechselwirkung ergibt de-facto-Haftungsausschluss; im B2C regelmäßig unwirksam nach § 307 BGB.
- **CISG-Abwahl vergessen:** Falls der SaaS-Anbieter im Ausland sitzt, CISG ausschließen.
- **Berufsrechtlicher Hinweis:** § 43a Abs. 2 BRAO, § 203 StGB bei jeder Weitergabe beachten.
