---
name: mandat-aktualisierung
description: "Laufendes Prozessmandat aktualisieren: neue Schriftsaetze, Beschluesse, Fristen eintragen. Normen: §§ 233 ff. ZPO. Prüfraster: Fristverfolgung, Sachstandsaktualisierung, offene Handlungspunkte. Output: Aktualisiertes Mandats-Protokoll. Abgrenzung: nicht Mandatseroffnung."
---

# Mandats-Aktualisierung

## Zweck

Ein Prozessportfolio bleibt nur dann nützlich, wenn es aktuell ist. Dieser Skill macht das Einpflegen einer Entwicklung effizient — strukturiertes Erfassen in wenigen Minuten, ohne freien Textdrift. Lädt bei jeder Anfrage, einen neuen Vorgang in ein laufendes Prozessmandat einzutragen.

## Eingaben

- **Mandatsbezeichnung (Slug)** (erforderlich): Kurzbezeichnung des Mandats. Falls nicht angegeben, wird eine Liste zuletzt aktualisierter Mandate zur Auswahl angeboten.
- **Ereignistyp**: Auswahl aus Kategorien oder Freitext.
- **Datum**: Standardmäßig heute; kann für rückwirkende Einträge überschrieben werden.
- **Zusammenfassung**: Ein kurzer Absatz — was ist passiert, was bedeutet es, welche unmittelbaren Folgen hat es.
- **Feldupdates** (soweit durch das Ereignis berührt): Status, Verfahrensstadium, Risikoeinstufung, Wesentlichkeit, Streitwert/Exposure, nächste Frist, externe Bevollmächtigte, interne Verantwortliche.

## Rechtlicher Rahmen

### Kernvorschriften

- **§§ 214–229 ZPO** — Fristen, Versäumnis, Wiedereinsetzung; zentral für die Fristenkontrolle im Prozessmandat.
- **§§ 516, 548, 569 ZPO** — Berufungs-, Revisions- und Beschwerdebegründungsfristen (Monats- bzw. Zwei-Monats-Fristen nach Zustellung); jede Fristverlängerung ist einzutragen.
- **§ 116 VwGO** — Zustellung und Fristen im Verwaltungsgerichtsverfahren.
- **§§ 317–329 StPO** — Rechtsmittelfristen im Strafverfahren (Berufungsfrist: eine Woche ab Urteilsverkündung, § 317 StPO).
- **§ 43a Abs. 1, 4 BRAO** — Sachkundige, gewissenhafte Berufsausübung; Pflicht zur lückenlosen Aktenführung als Berufspflicht.
- **§ 11 BORA** — Sorgfaltspflicht bei Fristnotierung und Aktenführung.
- **§§ 257, 261 HGB; § 147 AO** — Aufbewahrungspflichten für Handels- und Steuerunterlagen (6–10 Jahre); relevant für den Beweissicherungsaspekt.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 0: Konfliktsschranke

Vor dem Einpflegen eines Eintrags wird geprüft, ob das Mandat in `_log.yaml` enthalten ist. Fehlt es:

> "Das Mandat [Bezeichnung] ist nicht im Mandatsprotokoll erfasst. Bitte zunächst `/prozessrecht:mandat-aufnahme` ausführen, damit die Interessenkonfliktprüfung erfolgt und die Mandatsakte angelegt wird."

### Schritt 1: Ereignistyp

Angebotene Kategorien:

- **Verfahrensrechtlich** — Schriftsatz eingereicht/erhalten, Beschluss ergangen, Termin stattgefunden, Frist gesetzt
- **Beweiserhebung** — Urkunden vorgelegt/erhalten, Zeugenvernehmung, § 142 ZPO-Anordnung
- **Sachlich** — neue Tatsachen, relevantes Dokument aufgetaucht, Entscheidung zur Sache
- **Strategie** — Positionswechsel, Vergleichsangebot gemacht/erhalten, Änderung der Vergleichskompetenz
- **Risikoneubewertung** — Schwere oder Wahrscheinlichkeit hat sich geändert
- **Beteiligte** — Neue Person einbezogen, Wechsel der externen Bevollmächtigten
- **Administrativ** — Mandatsvertrag geschlossen, Budget angepasst, Beweissicherungsanordnung erneuert

Freitext möglich, wenn keine Kategorie passt.

### Schritt 2: Datum

Standard: heute. Überschreibung möglich (z. B. für die Nacherfassung eines Ereignisses der letzten Woche).

### Schritt 3: Zusammenfassung

Ein Absatz: Was ist passiert, was bedeutet es, welche unmittelbaren Folgen sind erkennbar.

### Schritt 4: Protokollfelder aktualisieren

Nur die durch das Ereignis betroffenen Felder werden abgefragt:

- `status:` — Hat sich das Stadium verschoben (z. B. Klageerhebung → Beweisaufnahme)?
- `verfahrensstadium:` — Detailangabe zum Unterstand
- `risiko:` — Neubewertung erforderlich?
- `wesentlichkeit:` — Änderung? (neue Tatsachen können Rückstellungs- oder Offenlegungspflicht auslösen)
- `streitwert_exposure:` — Anpassen bei neuen Erkenntnissen
- `nächste_frist:` — Neues kommendes Datum, falls bekannt
- `externe_bevollmaechtigte:` — Wechsel?
- `interne_verantwortliche:` — Neu oder ausgeschieden?
- `beweissicherung:` — Erneuert, erweitert, aufgehoben?

Verfahrensrechtliche Updates berühren in der Regel nur `verfahrensstadium` und `nächste_frist`; ein Vergleichsangebot kann `wesentlichkeit`, `streitwert_exposure` und `status` berühren.

### Schritt 4a: Vergleichsannahmeschranke

Handelt es sich um eine **Vergleichsannahme** (die Partei nimmt ein Vergleichsangebot an, unterzeichnet einen Vergleich oder erteilt grundsätzlich Vollmacht zur Annahme — nicht bloßes Erfassen eines Angebots oder Gegenentwurfs):

> Ein Vergleich hat endgültige Rechtswirkungen — er beseitigt den Klagegegenstand, erfordert typischerweise eine gegenseitige Erlassklausel und kann steuerliche sowie versicherungsrechtliche Folgen haben. Wurde dies mit einem Anwalt besprochen? Falls ja: bitte bestätigen. Falls nein, hier ist ein Briefing für das Gespräch:
>
> [Zusammenfassung: Mandat, Vergleichskonditionen (Betrag, Struktur, Erlassumfang, Vertraulichkeit), gefährdetes Interesse, Stand der Vergleichskompetenz, Risiken, Fragen an den Anwalt.]

Ohne ausdrückliche Bestätigung wird die Annahme nicht eingetragen und die Wesentlichkeit nicht auf Vergleichsbasis umklassifiziert.

### Schritt 4b: Wesentlichkeitsprüfung

Bei bestimmten Ereignistypen ist eine Wesentlichkeitsprüfung obligatorisch — der Nutzer muss explizit antworten:

| Ereignistyp | Hinweistext |
|---|---|
| Sachlich (neue Tatsachen, relevantes Dokument, Entscheidung zur Sache) | "Dieses Ereignis ist sachlicher Natur. Ändert es die Wesentlichkeitseinstufung? Aktuell: [X]. Optionen: rückgestellt / offengelegt / beobachtet / keine. Änderung?" |
| Strategie (Positionswechsel, Vergleichsangebot gemacht oder erhalten) | "Vergleichsaktivität kann eine Wesentlichkeitsumstufung auslösen. Aktuell: [X]. Wenn das Angebot die Exposure verschiebt oder den Streit von 'bestritten' auf 'wahrscheinlich und schätzbar' bewegt, bitte umklassifizieren." |
| Risikoneubewertung | "Risiko hat sich verändert. Die Wesentlichkeit sollte folgen. Aktuell: [X]. Umklassifizieren?" |
| Behördliche Maßnahme | "Behördenhandeln (Durchsuchung, Vorladung, Ordnungsverfügung) löst regelmäßig eine Offenlegungsanalyse aus. Aktuell: [X]. Änderung?" |

"Keine Änderung" muss explizit bestätigt werden. Im Verlaufseintrag wird festgehalten:

```markdown
**Wesentlichkeitsprüfung:** [keine Änderung / geändert von X nach Y]
**Begründung:** [ein Satz]
```

### Schritt 5: Belegdokument (optional)

Falls das Update ein Dokument betrifft (Beschluss, Schriftsatz, Korrespondenz), wird gefragt, ob ein Pfad verlinkt werden soll.

## Ausgabeformat

### Verlaufseintrag in `verlauf.md`

Jüngster Eintrag oben, direkt unter dem `---` nach dem Header:

```markdown
## [JJJJ-MM-TT] — [Ereignistyp]: [Kurztitel]

[Zusammenfassung in einem Absatz.]

**Geänderte Felder:**
- [Feld]: [alt → neu]
- [Feld]: [alt → neu]

**Verweisung Dokument:** [Pfad, falls angegeben]
```

Falls keine Felder geändert wurden, entfällt der Block "Geänderte Felder".

### Protokolldatei `_log.yaml`

- Geänderte Felder werden übernommen.
- `zuletzt_aktualisiert:` wird auf heute gesetzt (oder das Ereignisdatum, falls überschrieben).

### Bestätigung vor dem Speichern

Der Verlaufseintrag und die Yaml-Diff werden dem Nutzer zur Freigabe vorgelegt:

> "Das ist, was ich eintragen und aktualisieren werde. Soll ich das festschreiben?"

## Beispiel

**Sachverhalt:** Im Verfahren Müller ./. Beta GmbH (ZPO-Berufungsverfahren, OLG Frankfurt) ist am 12.05.2025 die Berufungsbegründungsfrist abgelaufen. Die Begründung wurde fristgerecht eingereicht. Keine Risikoänderung.

**Eintrag:**

```markdown
## [2025-05-12] — Verfahrensrechtlich: Berufungsbegründung eingereicht

Berufungsbegründung fristgerecht beim OLG Frankfurt eingereicht (§ 520 Abs. 2 ZPO). Keine inhaltlichen Änderungen zur bisherigen Positionierung. Nächster Termin: Eingang der Berufungserwiderung der Gegenseite erwartet bis 12.07.2025.

**Geänderte Felder:**
- naechste_frist: 2025-07-12
- verfahrensstadium: Berufungsbegründung eingereicht → Berufungserwiderung ausstehend

**Wesentlichkeitsprüfung:** keine Änderung
**Begründung:** Verfahrensrechtlicher Schritt ohne neue Tatsachen oder Risikoverschiebung.
```

## Risiken und typische Fehler

- **Fristversäumnis durch verzögerten Eintrag:** Der Eintrag ersetzt kein Fristenkontrollsystem; die Kanzlei muss separate Fristenkalender nach § 11 BORA führen. Dieser Skill dokumentiert — er sichert keine Fristen.
- **Stillschweigendes Wesentlichkeitsupdating:** Unterbleibt die explizite Wesentlichkeitsprüfung, kann eine Rückstellungspflicht oder eine kapitalmarktrechtliche Offenlegungspflicht übersehen werden.
- **Einträge in nicht-aufgenommene Mandate:** Ohne vorherige Interessenkonfliktprüfung (`/prozessrecht:mandat-aufnahme`) werden keine Einträge angelegt.
- **Vergleichsannahme ohne anwaltliche Prüfung:** Die Schranke ist unüberwindbar für Nicht-Juristen; nur ein explizites Ja entsperrt den Eintrag.
- **Rückwirkende Einträge:** Das Datum kann überschrieben werden; `zuletzt_aktualisiert` in `_log.yaml` zeigt jedoch immer das Bearbeitungsdatum, nicht das Ereignisdatum.
- **Korrekturen:** Vergangene Einträge werden nicht bearbeitet. Korrekturen erfolgen als neuer Eintrag mit Verweis auf den zu korrigierenden Eintrag.

## Quellenpflicht

In der Verlaufsakte und bei Wesentlichkeitsprüfungen sind folgende Quellen heranzuziehen und, soweit angegeben, zu zitieren:

- Gesetzestexte: §§ 214 ff., 516, 520, 548, 569 ZPO; §§ 317 ff. StPO; § 116 VwGO; § 43a BRAO; § 11 BORA
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
