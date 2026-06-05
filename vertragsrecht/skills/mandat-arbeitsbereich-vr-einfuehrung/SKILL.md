---
name: mandat-arbeitsbereich-vr-einfuehrung
description: "Mandat Arbeitsbereich VR Einfuehrung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandat Arbeitsbereich VR Einfuehrung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandat Arbeitsbereich VR Einfuehrung** im Plugin Vertragsrecht (BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vertragsrecht-mandat-arbeitsbereich` | Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven Mandat wechseln, Mandate auflisten, ein Mandat archivieren oder auf kanzleiweiten Kontext umschalten möchte. |
| `vr-einfuehrung-vertragstypen-bgb` | Vertragsrecht einfuehrend: BGB-Vertragstypen Kauf, Werkvertrag, Dienstvertrag, Mietvertrag, Pacht, Darlehen, Geschaeftsbesorgung, Auftrag. Pro Typ Pflichten, Vergueng, Maengelrecht, Kuendigung. Entscheidungstabelle. |
| `abmahnung-uwg` | Unterstützt beim Verfassen und Prüfen von UWG-Abmahnungen nach § 13 UWG sowie der dazugehörigen modifizierten Unterlassungserklärung mit Vertragsstrafe und der Schutzschrift. Lädt, wenn ein Mandat eine wettbewerbsrechtliche Abmahnung, eine strafbewehrte Unterlassungserklärung oder eine Schutzschrift zum Gegenstand hat. |

## Arbeitsweg

Im Plugin Vertragsrecht (BGB) gilt für **Mandat Arbeitsbereich VR Einfuehrung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vertragsrecht-mandat-arbeitsbereich`

**Fokus:** Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven Mandat wechseln, Mandate auflisten, ein Mandat archivieren oder auf kanzleiweiten Kontext umschalten möchte.

# Mandatsarbeitsbereich Vertragsrecht

## Zweck

Anwältinnen und Anwälte arbeiten parallel an mehreren Mandaten. Ein
Mandatsarbeitsbereich hält den Kontext eines Mandanten oder Auftrags strikt
von allen anderen getrennt. Diese Skill verwaltet diese Arbeitsbereiche.

Lädt, wenn ein Anwalt mit Mehrfach-Mandantenstruktur (Kanzlei, Außenmandate)
einen Arbeitsbereich anlegen, wechseln, auflisten oder schließen möchte, oder
wenn eine andere Skill wissen muss, in welchem Mandat sie tätig ist.

**Standardzustand: deaktiviert.** Für Syndikusrechtsanwältinnen und
-anwälte (In-house) mit einem einzigen Mandanten/Arbeitgeber läuft das
Plugin automatisch auf Kanzleiebene. Mandatsarbeitsbereiche werden nur für
Kanzleien und Berufsanwälte mit Mehrfach-Mandantenstruktur aktiviert.

## Eingaben

- Unterbefehl: `neu`, `liste`, `wechseln`, `schließen`, `keine`
- Mandats-Kürzel (Slug): Kurzbezeichnung in Kleinbuchstaben mit Bindestrichen
 (z. B. `mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-msa`)
- Für `neu`: Mandantenangaben (Name, Gegenpartei, Vertragsart, Schlüsselfakten)

## Rechtlicher Rahmen

### Kernvorschriften

Die Mandatsverwaltung ist untrennbar mit dem anwaltlichen Berufsrecht
und der anwaltlichen Verschwiegenheitspflicht verbunden:

- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Rechtsanwalts;
 Mandatsgeheimnis als Kernpflicht
- § 203 StGB — Verletzung von Privatgeheimnissen; strafrechtlicher Schutz
 des Mandatsgeheimnisses
- § 50 BRAO — Handakten; Aufbewahrungspflicht (5 Jahre nach Abschluss
 des Mandats)
- § 2 BORA — Grundpflichten; Interessenkonflikte müssen geprüft werden
 (Mandate gegen frühere Mandanten oder gleichzeitig gegen denselben
 Mandanten in anderem Verfahren)
- DSGVO Art. 5, 25 — Datenschutz durch Technikgestaltung; mandatsbezogene
 personenbezogene Daten dürfen nicht zwischen Mandaten geteilt werden

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Anwaltliche Verschwiegenheitspflicht; Schadensersatz bei
 Geheimnisbruch durch Anwalt; § 43a BRAO)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Anwaltliche Aufbewahrungspflicht von Handakten; § 50 BRAO)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Schutz von Verteidigungsunterlagen; Rechtsanwalt; § 97 StPO analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Unterbefehle

- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` — neuen Mandatsarbeitsbereich
 anlegen, kurze Aufnahme durchführen, `mandat.md` schreiben
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich liste` — alle Mandate mit Status und
 aktivem Kürzel auflisten
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich wechseln <kuerzel>` — aktives Mandat setzen
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich schließen <kuerzel>` — Mandat archivieren
 (verschiebt in `_archiv/`, löscht nie)
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich keine` — von aktivem Mandat trennen,
 auf Kanzleiebene arbeiten

### Schritt 1 — Kanzleiprofil prüfen

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`. Prüfe
den Abschnitt `## Mandatsarbeitsbereiche`. Wenn `Aktiviert: ✗`, weise einmal
darauf hin:

> Mandatsarbeitsbereiche sind deaktiviert — Sie sind als In-house-Praxis
> mit einem Mandanten konfiguriert; das Plugin arbeitet automatisch auf
> Kanzleiebene. Wenn Sie tatsächlich mit mehreren Mandanten arbeiten,
> führen Sie `/vertragsrecht:vertragsrecht-kaltstart-interview --redo` aus und wählen
> eine Kanzleisetting-Option. Andernfalls benötigen Sie
> `/mandat-arbeitsbereich` nicht.

### Schritt 2 — Unterbefehl ausführen

Auflösung nach dem ersten Token von `$ARGUMENTE`:

- `neu` → Aufnahme durchführen, `mandate/<kuerzel>/mandat.md` schreiben,
 `verlauf.md` und `notizen.md` anlegen
- `liste` → `mandate/*/mandat.md` aufzählen, Tabelle ausgeben,
 aktives Mandat markieren
- `wechseln` → Zeile `Aktives Mandat:` im Kanzleiprofil aktualisieren
- `schließen` → `mandate/<kuerzel>/` nach `mandate/_archiv/<kuerzel>/`
 verschieben, Abschlussdatum in `verlauf.md` eintragen
- `keine` → `Aktives Mandat:` auf `keine — Kanzleiebene` setzen

### Schritt 3 — Bestätigung vor Schreiben

Dem Nutzer vor jeder Dateiänderung zeigen, was sich ändert, und
Bestätigung einholen.

### Unterbefehl-Logik: `neu <kuerzel>`

1. Prüfen, ob das Kürzel noch nicht in `mandate/<kuerzel>/` oder
 `mandate/_archiv/<kuerzel>/` vorhanden ist. Bei Wiederverwendung:
 anderes Kürzel vorschlagen.
2. Kurzaufnahme durchführen:
 - **Mandant** (vertretene Partei oder interne Geschäftseinheit bei In-house)
 - **Gegenpartei** (andere Seite — kann mehrere sein)
 - **Vertragsart** (Lieferantenvertrag / Dienstleistungsvertrag / NDA /
 SaaS-Abonnement / Nachtrag / Verlängerung / Sonstiges)
 - **Vertraulichkeitsstufe** (Standard / erhöht / Clean-Team)
 - **Schlüsselfakten** (2–5 Sätze: Gegenstand, Beteiligte, Besonderheiten
 gegenüber Standardplaybook)
 - **Mandatsspezifische Abweichungen vom Playbook** (z. B. "Mandant besteht
 auf 24 Monate Haftungsdeckel statt 12; kooperativer Ton, da strategische
 Partnerschaft")
 - **Verwandte Mandate** (Kürzel verbundener Mandate)
3. `mandate/<kuerzel>/mandat.md` nach Vorlage unten schreiben.
4. `mandate/<kuerzel>/verlauf.md` mit einem "Eröffnet"-Eintrag anlegen.
5. Leere `mandate/<kuerzel>/notizen.md` erstellen.
6. **Nicht** automatisch zum neuen Mandat wechseln. Fragen:
 "Möchten Sie jetzt zu `<kuerzel>` wechseln?"

### Unterbefehl-Logik: `liste`

`mandate/*/mandat.md` aufzählen. Erste Zeilen jeder Datei für Status lesen.
Tabelle ausgeben:

| Kürzel | Mandant | Vertragsart | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archivierte Mandate unter
"Archivierte Mandate" separat aufführen.

### Unterbefehl-Logik: `wechseln <kuerzel>`

1. Prüfen, ob `mandate/<kuerzel>/mandat.md` existiert. Falls nicht:
 `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` anbieten.
2. `Aktives Mandat:`-Zeile im Kanzleiprofil auf `<kuerzel>` setzen.
3. `mandat.md`-Zusammenfassung anzeigen, damit der Nutzer das richtige
 Mandat bestätigt.

### Unterbefehl-Logik: `schließen <kuerzel>`

1. Vorhandensein von `mandate/<kuerzel>/` prüfen.
2. Abschlusseintrag mit heutigem Datum in `mandate/<kuerzel>/verlauf.md` hinzufügen.
3. `mandate/<kuerzel>/` nach `mandate/_archiv/<kuerzel>/` verschieben.
4. War das geschlossene Mandat das aktive, `Aktives Mandat:` auf
 `keine — Kanzleiebene` setzen.

### Unterbefehl-Logik: `keine`

`Aktives Mandat:` im Kanzleiprofil auf `keine — Kanzleiebene` setzen.
Mit Nutzer bestätigen.

## Ausgabeformat

### Vorlage `mandat.md`

```markdown
[ARBEITSERGEBNIS-KENNZEICHNUNG — gemäß Kanzleiprofil ## Ausgaben]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Kürzel:** [kürzel]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [Standard / erhöht / Clean-Team]

---

## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Vertragsart

[Lieferantenvertrag / Dienstleistungsvertrag / NDA / SaaS-Abonnement /
Nachtrag / Verlängerung / Sonstiges — mit einem Satz Begründung]

## Schlüsselfakten

[2–5 Sätze: Vertragsgegenstand, beteiligte Personen, Risikolage,
Besonderheiten gegenüber dem Standard-Playbook.]

## Mandatsspezifische Abweichungen vom Playbook

*Jede Abweichung vom kanzleiweiten Playbook, die nur dieses Mandat betrifft.*

- [z. B. "Haftungsobergrenze: Mandant besteht auf 24 Monate, nicht
 Kanzleistandard 12."]
- [z. B. "Ton: beziehungserhaltend — Gegenpartei ist strategischer Partner."]
- [z. B. "Gerichtsstand: muss München sein."]

## Verwandte Mandate

- [Kürzel — ein Satz warum verwandt]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung, wer Einsicht hat,
ob mandatsübergreifender Kontext trotz globaler Einstellung unzulässig ist.]
```

### Vorlage `verlauf.md` (Seed)

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Append-only Ereignisprotokoll. Aktuellster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kürzel: `[kürzel]`. Status: aktiv.
[Anfangskontext — z. B. "Eröffnet auf eingehenden MSA-Entwurf von
[Gegenpartei]."]
```

## Ablagestruktur

```
~/.claude/plugins/config/klotzkette/vertragsrecht/
├── CLAUDE.md # Kanzleiprofil
└── mandate/
 ├── <kuerzel>/
 │ ├── mandat.md # Mandantenangaben, Schlüsselfakten, Abweichungen
 │ ├── verlauf.md # Datiertes Protokoll (Ereignisse, Entscheidungen, Entwürfe)
 │ ├── notizen.md # Freie Arbeitsnotizen
 │ └── ausgaben/ # Skill-Ausgaben für dieses Mandat (optional)
 └── _archiv/
 └── <kuerzel>/ # Geschlossene Mandate — lesbar, nicht aktiv
```

Kürzel sind Kleinbuchstaben mit Bindestrichen. Beispiele:
`mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-nda`.

## Mandatsübergreifender Kontext

Das Kanzleiprofil enthält eine `Mandatsübergreifender-Kontext:`-Option.
Standardmäßig `aus` — eine Skill, die in Mandat A arbeitet, liest **nie**
Dateien aus `mandate/B/`. Das ist die Vertraulichkeitsgarantie.

Bei `ein` darf eine Skill mandatsübergreifend lesen **nur** auf ausdrückliche
Nutzeranfrage. Auch dann gilt: Standardmäßig nur aktives Mandat laden,
es sei denn, der Nutzer fragt explizit nach einer mandatsübergreifenden Ansicht.

## Beispiel

**Szenario:** Kanzlei übernimmt Prüfung eines IT-Dienstleistungsvertrags
für Mandantin GmbH gegen Lieferant X.

```
/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu mueller-it-vertrag-2026
```

Kurzaufnahme ergibt:
- Mandant: Müller GmbH
- Gegenpartei: IT-Lieferant X GmbH
- Vertragsart: Dienstleistungsvertrag
- Besonderheit: Mandant besteht auf unbeschränkter Gewährleistung für
 datenschutzkritische Komponenten

Slug `mueller-it-vertrag-2026` angelegt mit Abweichung:
"Gewährleistung: kein Verjährungsverkürzung für Datenschutz-Komponenten."

## Risiken und typische Fehler

- **Kein Interessenkonflikt-Check.** Diese Skill führt keine automatische
 Konfliktprüfung durch — das ist Aufgabe des Anwalts. Die Aufnahme erfasst,
 was der Nutzer erklärt; sie ersetzt keine Prüfung nach § 43a BRAO, § 3
 BORA.
- **Löschen ist verboten.** Abschließen bedeutet Archivieren. Keine
 Mandatsakte wird gelöscht — Aufbewahrungspflicht nach § 50 BRAO (5 Jahre).
- **Kürzel-Kollision prüfen.** Wird ein Kürzel eines archivierten Mandats
 wiederverwendet, das archivierte Mandat unter `_archiv/<kuerzel>/` belassen.
- **Mandatsübergreifender Kontext bleibt aus.** Wenn nicht explizit
 eingeschaltet, niemals Dateien eines anderen Mandats lesen.

## Quellenpflicht

Bei mandatsspezifischen Hinweisen zur Vertraulichkeit oder Aufbewahrung:
- § 43a Abs. 2 BRAO (Verschwiegenheit), § 50 BRAO (Handakten)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=17.12.1998&Aktenzeichen=IX+ZR+196%2F97
Bundle: bundle_047.json
-->

## 2. `vr-einfuehrung-vertragstypen-bgb`

**Fokus:** Vertragsrecht einfuehrend: BGB-Vertragstypen Kauf, Werkvertrag, Dienstvertrag, Mietvertrag, Pacht, Darlehen, Geschaeftsbesorgung, Auftrag. Pro Typ Pflichten, Vergueng, Maengelrecht, Kuendigung. Entscheidungstabelle.

# Vertragsrecht: BGB-Typen

## Spezialwissen: Vertragsrecht: BGB-Typen
- **Spezialgegenstand:** Vertragsrecht: BGB-Typen / vr einfuehrung vertragstypen bgb. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `abmahnung-uwg`

**Fokus:** Unterstützt beim Verfassen und Prüfen von UWG-Abmahnungen nach § 13 UWG sowie der dazugehörigen modifizierten Unterlassungserklärung mit Vertragsstrafe und der Schutzschrift. Lädt, wenn ein Mandat eine wettbewerbsrechtliche Abmahnung, eine strafbewehrte Unterlassungserklärung oder eine Schutzschrift zum Gegenstand hat.

# UWG-Abmahnung – Erstellung und Prüfung

## Zweck

Dieser Skill unterstützt Rechtsanwält:innen bei der Ausarbeitung einer wettbewerbsrechtlichen
Abmahnung nach § 13 UWG, der Formulierung einer modifizierten Unterlassungserklärung (sog.
"Hamburger Brauch") und der Erstellung einer Schutzschrift gegen eine drohende einstweilige
Verfügung. Anwendungsfelder sind Verstöße gegen §§ 3 ff. UWG (irreführende Werbung,
vergleichende Werbung, aggressive Geschäftspraktiken), Verletzungen von Kennzeichenrechten im
lauterkeitsrechtlichen Kontext sowie Verstöße gegen § 5a UWG (Informationspflichten).

## Eingaben

Das Modell benötigt folgende Informationen:

1. **Wettbewerbsverstoß**: konkrete Handlung (Anzeigentext, Screenshot, URL, Beschreibung)
2. **Verletzter und Verletzer**: vollständige Firmierung, Rechtsform, Sitz
3. **Abmahnender**: Partei (Mitbewerber, Verband § 8 Abs. 3 Nr. 2 UWG oder qualifizierte
 Einrichtung § 8 Abs. 3 Nr. 3 UWG) – Sachlegitimation prüfen!
4. **Fristsetzung**: gewünschte Unterlassungsfrist (üblicherweise 1–2 Wochen)
5. **Vertragsstrafe**: gewünschte Höhe oder Bitte um Vorschlag (Orientierung: wettbewerbsrechtliche Praxis, nur mit verifizierten Quellen,
 typisch EUR 5.001 bis EUR 15.000 je nach Branche und Verletzungsgewicht)
6. **Schutzschrift**: liegt ein konkreter Verfügungsantrag vor oder nur eine vorbeugend
 einzureichende Schutzschrift?

## Rechtlicher Rahmen

### Normen

- **§§ 3, 3a, 5, 5a, 7 UWG** – Verbotstatbestände
- **§ 8 Abs. 1 UWG** – Beseitigungs- und Unterlassungsanspruch
- **§ 8 Abs. 3 UWG** – Anspruchsberechtigte (Mitbewerber, Verbände, qualifizierte Einrichtungen)
- **§ 13 UWG** – formale Anforderungen der Abmahnung (Pflichtinhalt seit UWG-Reform 2021)
- **§ 13a UWG** – Gegenanspruch des Abgemahnten bei unberechtigter Abmahnung
- **§ 14 UWG** – Zuständigkeit (i. d. R. LG am Sitz des Verletzers oder des Verletzten)
- **§ 11 UWG** – Verjährung (6 Monate ab Kenntnis bei Ansprüchen nach §§ 8, 9 Abs. 1, 13 Abs. 3 UWG; Höchstfristen nach § 11 Abs. 3 und 4 UWG)
- **§ 339 BGB** – Vertragsstrafe; **§ 242 BGB** – Herabsetzungsrecht bei unverhältnismäßiger
 Strafe (sog. Korrektivklausel)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Wiederholungsgefahr und die Beseitigungswirkung einer Unterlassungserklärung; eine
 eingeschränkt abgegebene UE beseitigt die Wiederholungsgefahr nur für den konkret bezeichneten
 Verletzungsfall.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Reichweite einer strafbewehrten Unterlassungserklärung; der Gläubiger muss konkret
 beschreiben, welche zukünftigen Handlungen erfasst sein sollen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Abmahnung": Die Abmahnung muss die beanstandete Verletzungshandlung so klar bezeichnen, dass
 der Abgemahnte die Berechtigung prüfen kann; andernfalls ist die Abmahnung unbeachtlich.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Dringlichkeitsvermutung im einstweiligen Verfügungsverfahren; selbst nach UWG-Reform 2021
 gilt die Dringlichkeitsfrist von 1 Monat ab Kenntnis als maßgeblich.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

1. **Sachverhaltsaufnahme** (Tag 0): Wettbewerbsverstoß dokumentieren (Screenshot mit
 Zeitstempel, Notaranschrift oder eidesstattliche Versicherung).
2. **Prüfung der Aktivlegitimation** (§ 8 Abs. 3 UWG): Ist der Mandant Mitbewerber?
 Wettbewerbsverhältnis konkret darlegen.
3. **Prüfung der Dringlichkeit** (§ 12 Abs. 1 UWG): Kenntnis seit wann? 1-Monats-Frist für eV
 wahren. Cave: eigene Werbung mit ähnlichem Inhalt = Verwirkung der Dringlichkeit.
4. **Entwurf der Abmahnung** mit Pflichtangaben § 13 Abs. 2 UWG:
 - Name/Firma des Abmahnenden
 - Bezeichnung der Verletzung (Handlung, Fundort, Datum)
 - Unterlassungsbegehren mit konkreter Beschreibung
 - Angemessene Frist (i. d. R. 7–14 Tage)
 - Aufforderung zur Abgabe einer strafbewehrten Unterlassungserklärung
5. **Entwurf der modifizierten Unterlassungserklärung** (Hamburger Brauch):
 - Benennung der konkreten Verletzungshandlung
 - Vertragsstrafe nach Wahl des Gläubigers oder "angemessene Strafe", Mindestbetrag EUR 5.001
 - Korrektivklausel (Gericht kann Strafe auf EUR 2.500 reduzieren § 342 BGB analog)
 - Reichweite: kerngleiche Verletzungshandlungen einschließen
6. **Prüfung einer Schutzschrift** (§ 945a ZPO): Wenn Gegenabmahnung droht oder Antrag auf
 einstweilige Verfügung zu erwarten ist → Schutzschrift in das Schutzschriftenregister
 (www.zssr.de) einreichen.
7. **Versand**: per Telefax + Einschreiben/Rückschein oder per Boten; Fristlauf dokumentieren.
8. **Reaktion des Gegners**: eingehende UE prüfen (ausreichend? kerngleiche Handlungen
 erfasst?); ggf. Ablehnung mit Begründung.
9. **Gerichtliche Durchsetzung** bei ausbleibender/unzureichender Reaktion: einstweilige
 Verfügung §§ 935, 940 ZPO oder Hauptsacheklage nach §§ 8, 14 UWG.

## Ausgabeformat

Das Modell gibt folgende Dokumente aus:

- **Abmahnschreiben** (Urteilsstil, vollständiger Briefkopf, Datum, Fristsetzung, Anlage UE)
- **Entwurf der Unterlassungserklärung** (separate Anlage, unterschriftsreif)
- **Rechtliches Memo** (Gutachtenstil) mit Prüfung der Erfolgsaussichten
- Optional: **Schutzschrift** (vgl. Skill einstweilige-verfügung)

## Beispiel

**Sachverhalt**: Die Musterprint GmbH bewirbt ihre Druckprodukte online mit "Testersieger Stiftung
Warentest 2023". Das Testergebnis stammt tatsächlich aus 2018 und ist nicht auf das aktuelle
Produkt übertragbar. Der Mandant, die Quickprint AG, ist Mitbewerber im selben Marktsegment.

**Prüfung (Gutachtenstil)**:

*§ 5 Abs. 1 S. 2 Nr. 1 UWG – Irreführung über die Beschaffenheit*: Die Angabe "Testersieger
Stiftung Warentest 2023" ist eine Angabe über wesentliche Merkmale des Produkts (Qualität,
Prüfungsdatum). Sie ist unwahr, da das Testergebnis aus 2018 stammt. Die angesprochenen
Verkehrskreise verstehen die Jahreszahl als Beleg eines aktuellen Tests; eine irreführende
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Einsatz der Werbung.

*Aktivlegitimation (§ 8 Abs. 3 Nr. 1 UWG)*: Die Quickprint AG steht mit der Musterprint GmbH
in einem konkreten Wettbewerbsverhältnis, da beide im selben Segment (Digitaldruckprodukte B2C)
tätig sind. Damit ist die Aktivlegitimation gegeben (Köhler, in: Köhler/Bornkamm/Feddersen,
UWG, 42. Aufl. 2024, § 8 Rn. 3.12).

**Ergebnis**: Die Abmahnung ist begründet. Empfohlen wird eine Frist von 10 Tagen zur Abgabe
der UE sowie eine Vertragsstrafe von EUR 8.001 (Hamburger Brauch).

## Risiken und typische Fehler

- **Fristversäumnis (Dringlichkeit)**: Kenntnis vom Verstoß länger als 1 Monat → Dringlichkeit
 entfallen; eV nicht mehr ohne weiteres zulässig. Fristlauf intern dokumentieren.
- **Unzureichende Bezeichnung der Verletzungshandlung**: Abmahnung ist zu vage → Gegner kann
 Kostengegenanspruch nach § 13a UWG geltend machen.
- **Fehlende Aktivlegitimation**: Kein echtes Wettbewerbsverhältnis → Abmahnung unberechtig
 → Schadensersatz nach § 13a UWG; Missbrauchsgefahr § 8c UWG.
- **Missbrauch (§ 8c UWG)**: Verdacht bei Serienabmahnungen, sachfremden Motiven, überhöhten
 Vertragsstrafen → Abmahnung unwirksam; Mandant haftet für Kosten des Gegners.
- **Unterlassungserklärung zu eng**: Kerngleiche Verletzungen nicht miterfasst → erneute Abmahnung
 erforderlich; Gerichtsverfahren nicht vermieden.
- **Berufsrechtliche Pflichten**: Verschwiegenheit (§ 43a Abs. 2 BRAO, § 203 StGB) wahren;
 Mandantendaten nicht ungesichert per E-Mail übermitteln.
- **Verjährung § 11 UWG**: 6 Monate ab Kenntnis von Verstoß und Verletzer; absolute
 Verjährung 3 Jahre (§§ 195, 199 BGB analog).

## Quellenpflicht

Jede juristische Aussage in Abmahnschreiben, Memos und Schriftsätzen ist nach
`references/zitierweise.md` zu belegen. Rechtsprechungszitate im BGH-Stil (Gericht, Datum,
Az., Fundstelle, Rn., ggf. Kurzbezeichnung). Kommentarzitate mit Bearbeiter, Werk, Auflage,
§ und Rn. Bei umstrittenen Fragen (z. B. Reichweite der Kerngleichheit, Höhe der Vertragsstrafe)
h. M. und Mindermeinung getrennt darstellen. Keine pauschalen "vgl."-Verweise ohne konkrete
Seitenangabe.
