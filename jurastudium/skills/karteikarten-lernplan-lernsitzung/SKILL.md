---
name: karteikarten-lernplan-lernsitzung
description: "Karteikarten Lernplan Lernsitzung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Karteikarten Lernplan Lernsitzung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Karteikarten Lernplan Lernsitzung** im Plugin Jurastudium (Klausur, AG, Examen). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `karteikarten` | Karteikarten für Jurastudium und Examensvorbereitung erstellen: Anwendungsfall Student will Definitionen Tatbestaende Normen und Klausurrelevante Faelle als Lernkarten strukturieren. Lösungsschemata, Tatbestaende, Definitionen Buergerliches Recht Strafrecht öffentliches Recht. Prüfraster Karteikarten-Format Vorderseite Begriff/Norm Rückseite Definition/Schema, Schwierigkeitsgrad einordnen, prüfungsrelevant markieren. Output Karteikarten-Sammlung nach Fachgebiet strukturiert für Spaced-Repetition. Abgrenzung zu Lernplan für Zeitmanagement und zu Tatbestaende-Lernen. |
| `lernplan` | Erstellt oder aktualisiert einen strukturierten Lernplan für das Erste Staatsexamen, das Referendariat oder das Zweite Staatsexamen — phasenbezogen, nach Schwächen gewichtet, adaptiv nach Lernverlauf. Berücksichtigt Repetitoriumskalender (Alpmann, Hemmer, Jura Intensiv, Kaiser-Skripten). Lädt, wenn der Nutzer "Lernplan erstellen", "Examensvorbereitung planen", "Stundenplan Staatsexamen" oder "wie soll ich für [Prüfung] lernen" sagt. |
| `lernsitzung` | Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Lösungsschemata Zivilrecht Strafrecht öffentliches Recht. Prüfraster Thema und Lernziel festlegen, Erklärung Kontrollfragen Uebungsfall Feedback, Wissenslücken identifizieren. Output strukturierte Lernsitzung mit Erklärungen und Zwischentest. Abgrenzung zu Karteikarten für Memorierung und zu Gutachten-Uebung für Klausurtraining. |

## Arbeitsweg

Im Plugin Jurastudium (Klausur, AG, Examen) gilt für **Karteikarten Lernplan Lernsitzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `karteikarten`

**Fokus:** Karteikarten für Jurastudium und Examensvorbereitung erstellen: Anwendungsfall Student will Definitionen Tatbestaende Normen und Klausurrelevante Faelle als Lernkarten strukturieren. Lösungsschemata, Tatbestaende, Definitionen Buergerliches Recht Strafrecht öffentliches Recht. Prüfraster Karteikarten-Format Vorderseite Begriff/Norm Rückseite Definition/Schema, Schwierigkeitsgrad einordnen, prüfungsrelevant markieren. Output Karteikarten-Sammlung nach Fachgebiet strukturiert für Spaced-Repetition. Abgrenzung zu Lernplan für Zeitmanagement und zu Tatbestaende-Lernen.

# Karteikarten-Drill

## Zweck

Definitionen, Tatbestandsmerkmale und Normstrukturen für das Staatsexamen müssen exakt und abrufbar sein — nicht "ungefähr bekannt". Diese Skill erzeugt Karteikarten aus eigenen Materialien (Skripten, Lernblättern, Definitionen-Sammlungen) oder aus eigenen Notizen, übt sie im Leitner-System und zeigt, welche Wissenslücken bestehen.

Nicht diese Skill: Anki selbst ersetzen. Wer Anki bereits nutzt, sollte es behalten. Diese Skill ist für den Direkteinstieg im Chat — ohne Programmwechsel.

Modi: `--erstellen` | `--üben` (Standard) | `--durchsehen` | `--statistik` | `--einheit <n>`

## Eingaben

- **Rechtsgebiet oder Thema** (z. B. "BGB AT Willenserklärung", "§ 242 StGB", "Allgemeines Verwaltungsrecht Ermessen")
- **Quelle** (Skript, Lernblatt, eigene Notizen — optional, aber für genaue Karten erforderlich)
- **Kartenanzahl** (Standard: 10–20 pro Einheit)
- **Prüfungsziel** (Erstes Staatsexamen, Zweites Staatsexamen, Klausur, Hausarbeit)

## Rechtlicher Rahmen

Karteikarten aus bereitgestellten Materialien sind vorrangig. Definitionen oder Streitstände ohne zuverlässige Quelle werden mit `[PRÜFEN]` markiert.

**Quellenregel und Rechtsprechung:**

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Leitentscheidungen (Beispiele für Kartenkontexte):**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Quellenregel:**

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Modus bestimmen

- `--erstellen`: Karten aus bereitgestellter Quelle generieren
- `--üben` (Standard): Fällige Karten + neue Karten üben; Frage zeigen → antworten → Antwort zeigen → Selbsteinschätzung → Bucket aktualisieren
- `--durchsehen`: Gesamte Kartei nach Bucket anzeigen
- `--statistik`: Fortschritt je Rechtsgebiet; hängen gebliebene Karten für mündlichen Drill markieren
- `--einheit <n>`: Fokussierte Einheit mit n Karten, priorisiert nach früheren Fehlern

### Schritt 2: Kartenerstellung (`--erstellen`)

**Kartenformat:**

```markdown
### Karte [N]
**F:** [Frage — ein Begriff, ein Tatbestandsmerkmal]
**A:** [Definition oder Regel — ein bis zwei Sätze, exakte Formulierung]
**Norm:** [§ / Art. — z. B. § 119 BGB]
**Quelle:** [Skript-Seite, Literatur, Urteil]
**Bucket:** neu
**Zuletzt geübt:** —
**Nächste Wiederholung:** [heutiges Datum]
**Hinweise:** [Abgrenzungen, Ausnahmen, Klausurfallen]
```

**Kartenregeln:**
1. Ein Begriff, ein Tatbestandsmerkmal = eine Karte. Nie mehrere Definitionen auf einer Karte.
2. Die Forderseite stellt eine Frage, kein Stichwort. Nicht "Vorsatz" — sondern "Was ist Vorsatz im Sinne des § 15 StGB?"
3. Die Rückseite enthält die Definition in Examensqualität — so wie sie in der Klausur gefordert wird.
4. Paragraphenangabe immer mit §-Zeichen: `§ 242 StGB`, `§ 812 Abs. 1 S. 1 Alt. 1 BGB`.
5. Karten aus eigenen Quellen sind zuverlässig. Karten aus meinem Wissen ohne Quelle erhalten `[PRÜFEN: Definition bestätigen]`.

**Beispiel-Karte:**

```
F: Was ist Beleidigung im Sinne des § 185 StGB?
A: Beleidigung ist die Kundgabe der Miss- oder Nichtachtung gegenüber einer bestimmten Person
 durch Erklärung oder tätliches Verhalten.
Norm: § 185 StGB
```

### Schritt 3: Drill-Modus (`--üben`)

**Priorisierung:**
1. Karten mit `nächste_wiederholung <= heute` und Bucket ≠ gekonnt
2. Neue, noch nicht versuchte Karten
3. Kein Fälliges mehr: Fragen, ob gekonnte Karten zur Verfallsprävention wiederholt werden sollen

**Drill-Ablauf je Karte:**
1. Frage zeigen. Auf Antwort warten.
2. Nutzer antwortet (oder: "weiß nicht" / "überspringen")
3. Antwort und Norm zeigen
4. Selbsteinschätzung: `gewusst` / `teilweise` / `nicht gewusst` / `weiß nicht`
5. Bucket und Wiederholungstermin aktualisieren:

| Einschätzung | Bucket | Nächste Wiederholung |
|---|---|---|
| gewusst | aufsteigen (neu → lernend → überprüfend → gekonnt) | +1 Tag neu, +3 lernend, +7 überprüfend, +21 gekonnt |
| teilweise | gleich | +1 Tag |
| nicht gewusst | absteigen | heute +4 Stunden |
| weiß nicht | absteigen | heute +4 Stunden |

## Ausgabeformat

- Karten im Markdown-Format, ein Block je Karte
- Statistik als Tabelle: Rechtsgebiet / Gesamt / Bucket-Verteilung / Heute fällig
- Sitzungsbericht am Ende einer `--einheit`:

```yaml
sitzungs_verlauf:
 - datum: 2026-05-08
 rechtsgebiet: Schuldrecht BT
 typ: karteikarten
 karten_anzahl: 10
 gewusst: 7
 teilweise: 2
 nicht_gewusst: 1
 problemthemen: [§ 823 Abs. 2 BGB Schutzgesetze]
```

## Beispiel

**Einheit BGB AT — 5 Karten:**

> F: Wann liegt eine Willenserklärung vor?
> A: Eine Willenserklärung ist eine private Willensäußerung, die unmittelbar auf die Herbeiführung einer Rechtsfolge gerichtet ist (Handlungswille, Erklärungsbewusstsein [str.], Geschäftswille).
> Norm: §§ 116 ff. BGB; Ellenberger, in: lizenzpflichtige Literaturquelle, BGB, 84. Aufl. 2025, Vor § 116 Rn. 1.

> F: Was ist der Unterschied zwischen Anfechtung nach § 119 und § 123 BGB?
> A: § 119 BGB: Irrtum über Inhalt oder Erklärungsinhalt (ohne Verschulden des Anfechtungsgegners); § 123 BGB: arglistige Täuschung oder widerrechtliche Drohung (Verschulden des Täuschenden erforderlich). Ausschlussfrist: § 119 "unverzüglich", § 123 Abs. 1 i.V.m. § 124 BGB ein Jahr.
> Norm: §§ 119, 123, 124 BGB.

## Risiken und typische Fehler

- **Ungenaue Definitionen lernen**: Eine Karte mit einer im Wesentlichen richtigen, aber examensuntauglichen Definition ist schlimmer als keine Karte. Definitionen aus Skripten sind oft schärfer als solche aus meinem Wissen — Skripte bevorzugen.
- **Zu viel auf eine Karte**: Tatbestandsmerkmale sind einzeln zu üben, nicht als Block. Wer "Betrug § 263 StGB: alle Merkmale" auf eine Karte schreibt, hat sechs Karten in eine gepresst.
- **Karte als Lernersatz**: Karteikarten sind Abruftraining für bereits Verstandenes. Eine Karte, die regelmäßig falsch beantwortet wird, zeigt ein Verständnisproblem — dann ist mündliches Durcharbeiten mit `pruefungsgespraech-ag` angezeigt.
- **Wiederholungstermine ignorieren**: Das Leitner-System funktioniert nur, wenn die Abstände eingehalten werden. Ausgefallene Tage akkumulieren Rückstand.
- **Keine Normangabe**: Jede Karte muss die einschlägige Norm nennen. Definitionen ohne Norm sind im Examen wertlos.

## Quellenpflicht

Jede Karte, die aus eigenen Unterlagen generiert wurde, trägt die Quellangabe dieser Unterlagen. Karten, die aus meinem Wissen ohne bereitgestellte Quelle generiert werden, erhalten `[PRÜFEN]` — vor dem Einlernen gegen Skript, Lehrbuch oder Kommentar abgleichen. Falsch eingeübte Definitionen schaden mehr als Lücken.

**Kanonische Definitionen-Quellen:**
- Skripten: Alpmann Schmidt, Hemmer/Wüst, Jura Intensiv, Kaiser-Skripten
- Lehrbücher: s. Rechtlicher Rahmen
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 2. `lernplan`

**Fokus:** Erstellt oder aktualisiert einen strukturierten Lernplan für das Erste Staatsexamen, das Referendariat oder das Zweite Staatsexamen — phasenbezogen, nach Schwächen gewichtet, adaptiv nach Lernverlauf. Berücksichtigt Repetitoriumskalender (Alpmann, Hemmer, Jura Intensiv, Kaiser-Skripten). Lädt, wenn der Nutzer "Lernplan erstellen", "Examensvorbereitung planen", "Stundenplan Staatsexamen" oder "wie soll ich für [Prüfung] lernen" sagt.

# Staatsexamen-Lernplan

## Zweck

Ohne Plan verschwindet Zeit. Diese Skill baut einen Lernplan für das Erste oder Zweite Staatsexamen — phasenbezogen, nach Schwachstellen gewichtet, mit Tages- und Wochenstruktur — und passt ihn nach jeder Lernsitzung an. Der Plan lebt; er ist kein exportierter Kalender.

Er gibt auch den nachgelagerten Skills (Karteikarten, Drill, Gutachtenstil) einen gemeinsamen Fahrplan, damit nicht bei jeder Sitzung von vorn gefragt werden muss, was heute dran ist.

## Eingaben

- **Prüfungsziel** (Erstes Staatsexamen / Referendariat / Zweites Staatsexamen)
- **Bundesland** (JAG/JAPrO — Pflichtstoff variiert)
- **Prüfungstermin** (konkret oder ungefähr)
- **Schwache Rechtsgebiete** (Eigenangabe oder aus Lernverlauf)
- **Starke Rechtsgebiete** (weniger Priorität, aber nicht vernachlässigt)
- **Stunden pro Woche** (realistisch, nicht aspirativ)
- **Freie Tage** (Ruhetage — Pläne ohne Erholung brechen in Woche 3 zusammen)
- **Repetitorium** (Alpmann Schmidt, Hemmer/Wüst, Jura Intensiv, Kaiser-Skripten oder keines)

## Rechtlicher Rahmen

Der Pflichtstoffkatalog richtet sich nach dem jeweiligen Juristenausbildungsgesetz und ist Grundlage der Priorisierung.

**Maßgebliche Ausbildungsordnungen:**
- § 5d DRiG — gemeinsamer Pflichtfachkern für alle Bundesländer
- JAG NRW i.d.F. vom 11.03.2003 — NRW-spezifischer Katalog
- JAPO Bayern i.d.F. vom 13.10.2003 — bayerischer Pflichtfachkatalog
- JAPrO Baden-Württemberg — BW-Katalog

**Prüfungsrelevante Leitentscheidungen (Planungsmaßstab):**

Für BGB-Schwerpunktplanung:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Für Strafrecht-Schwerpunktplanung:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kanonische Repetitorien-Literatur:**
- Alpmann Schmidt, Gesamtdarstellungen — kompakt, examensnah
- Hemmer/Wüst, Skriptenreihe — dogmatisch strukturiert nach Prüfungsreihenfolge
- Jura Intensiv, Skriptenreihe — Schwerpunkt Definitionen und Falllösung
- Kaiser-Skripten — starke Farbcodierung, schnell navigierbar
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Wofür planen wir?

> Wofür soll der Plan erstellt werden?
>
> 1. **Erstes Staatsexamen** (Pflichtfachprüfung, ggf. Schwerpunktbereich)
> 2. **Referendariat** (Klausurenkurs, Anwalts-/Stationsvorbereitungen)
> 3. **Zweites Staatsexamen** (Assessorexamen — prozessuale Klausuren, Relationen)

Für (1): Pflichtfachkatalog nach JAG/JAPrO des Bundeslandes laden.
Für (2) und (3): Stationsanforderungen und Klausurenformate klären.

### Schritt 2: Eingaben — einzeln, je eine fragen

Nicht alle Fragen auf einmal. Eine stellen, Antwort abwarten, dann nächste.

- **Prüfungstermin**: Datum bestätigt? Falls nicht: ungefähres Semester / Halbjahr?
- **Rechtsgebiete**: Pflichtfächerkanon nach Landesrecht. Bestätigen: "Gibt es etwas, das ergänzt oder gestrichen werden soll?"
- **Stärkste Rechtsgebiete**: geringste Priorität, aber nicht ignoriert
- **Schwächste Rechtsgebiete**: höchste Priorität, doppelte Stunden
- **Stunden pro Woche**: realistisch, nicht maximal. Nach Angabe:

 > "Sie haben [N] Stunden pro Woche genannt. Was füllt die restliche Zeit — Nebenjob (wie viele Stunden), Familie, Pendelzeit, Repetitorium-Präsenz, Sport, Sonstiges? Der Plan soll zu Ihrem Leben passen, nicht umgekehrt."

 Antwort abwarten. Dann Plausibilitätsprüfung:

 > "Das sind rund [X] Stunden täglich an [Z] Lerntagen, neben [Job + Familie + Pendeln]. Das erscheint [realistisch / eng / kaum tragbar]. Sollen wir die Stundenzahl anpassen, oder starten wir mit dieser Vorgabe und überprüfen nach zwei Wochen?"

 Diesen Schritt nie überspringen — auch wenn bereits eine Stundenzahl im Profil steht.

- **Ruhetage**: Mindestens ein Ruhetag pro Woche. Ohne Ausnahme empfehlen.
- **Lernmethoden**: Mehrauswahl. Skripten lesen / Karteikarten / Klausuren schreiben / Drillsitzungen / Wiederholung mit Lerngruppe. Den Stundenplan nach dem ausrichten, was der Studierende tatsächlich durchhält.

### Schritt 2.5: Repetitorium — Ergänzung oder Ersatz?

Wenn ein Repetitorium genutzt wird (Alpmann, Hemmer, Jura Intensiv, Kaiser oder sonstiges strukturiertes Kursangebot):

> "Ihr Repetitorium hat einen eigenen Terminplan. Dieser Plan kann zwei Rollen übernehmen — eine davon wählen:
>
> 1. **Ergänzung**: Das Repetitorium ist der Hauptfahrplan. Dieser Plan füllt Lücken: Zusatzübungen zu schwachen Rechtsgebieten, Karteikarten-Drill, Klausurensimulationen. Kein Parallelcurriculum.
> 2. **Ersatz**: Der Repetitoriums-Terminplan wird nicht befolgt (z. B. wegen Arbeitslast oder Taktung). Dieser Plan übernimmt die Vollstruktur — Rechtsgebiete, Phasen, Tagespläne.
>
> Beide gleichzeitig zu verfolgen führt in Woche 4 zum Zusammenbruch."

Antwort festhalten in YAML: `repetitorium_modus: ergänzung | ersatz`

### Schritt 3: Plan aufbauen

Wochen bis zum Prüfungstermin berechnen. Dann:

**Normalmodus (mehr als 6 Wochen):**

Drei Phasen:

| Phase | Anteil | Inhalt |
|---|---|---|
| **Grundlagenphase** | ~60 % der Zeit | Rechtsgebiete durcharbeiten, Skript + Karteikarten, wenige Klausuren |
| **Intensivphase** | ~30 % | Klausurenvolumen steigern, alle Rechtsgebiete rotieren, Zeitdruck simulieren |
| **Wiederholungsphase** | ~10 % | Schwachstellen aus Sitzungshistorie, Klausurensimulatoren, schwache Gebiete nochmals |

Schwache Rechtsgebiete: ca. doppelte Stunden gegenüber starken Rechtsgebieten.

Wochentags: Welches Rechtsgebiet, welche Methode, wie lange. Puffer einplanen — echte Wochen weichen vom Plan ab.

**Cramphase (weniger als 6 Wochen):**

> "Weniger als sechs Wochen bis zum Termin — das ist Crashkurs-Modus. Der Plan priorisiert hohe Examensrelevanz vor Vollständigkeit. Es entstehen Lücken; das ist der Kompromiss bei dieser Zeitlage."

Examensklassiker in jeder Phase (§§ 280 ff., 823 BGB; §§ 242, 263 StGB; Ermessen VerwR; §§ 80, 113 VwGO). Klausuren jeden Tag. Mindestens eine Klausur-Simulation pro Woche unter Zeitdruck. Letzte zwei Tage vor dem Examen: kein neues Material, nur Wiederholung bekannter Strukturen + Schlaf.

### Schritt 4: Plan schreiben

```yaml
plan_typ: erstes_staatsexamen # oder referendariat / zweites_staatsexamen
bundesland: NRW
pruefungstermin: 2026-07-15
erstellt: 2026-05-08
zuletzt_aktualisiert: 2026-05-08
wochen_bis_pruefung: 10
stunden_pro_woche: 30
tage_pro_woche: 5
modus: normal # oder cram
repetitorium: hemmer
repetitorium_modus: ergänzung
phasen:
 - name: grundlagen
 start: 2026-05-08
 ende: 2026-06-13
 schwerpunkt: Skript lesen, Karteikarten, 2 Klausuren/Woche
 - name: intensiv
 start: 2026-06-14
 ende: 2026-07-10
 schwerpunkt: Klausurenvolumen, alle Gebiete rotieren
 - name: wiederholung
 start: 2026-07-11
 ende: 2026-07-14
 schwerpunkt: Schwachstellen, Simulation
rechtsgebiete:
 bgb_at:
 prioritaet: hoch
 stunden_pro_woche: 6
 methoden: [karteikarten, klausuren, drill]
 schuldrecht_at:
 prioritaet: mittel
 stunden_pro_woche: 4
 methoden: [karteikarten, klausuren]
 stgb_at:
 prioritaet: hoch
 stunden_pro_woche: 5
 methoden: [klausuren, drill]
 verwaltungsrecht:
 prioritaet: mittel
 stunden_pro_woche: 4
 methoden: [skript, klausuren]
tagesplan:
 - datum: 2026-05-08
 wochentag: Freitag
 einheiten:
 - rechtsgebiet: BGB AT
 methode: skript_lesen
 dauer_min: 90
 - rechtsgebiet: BGB AT
 methode: karteikarten
 dauer_min: 45
 - datum: 2026-05-09
 wochentag: Samstag
 einheiten:
 - rechtsgebiet: StGB AT
 methode: klausur
 dauer_min: 120
sitzungs_verlauf: [] # wird von session, karteikarten, drill, gutachten-übung ergänzt
```

### Schritt 5: Bestätigung

Vor dem Speichern: Plan in Prosa zusammenfassen und Rückfrage stellen:

> LERNPLAN — KEIN RECHTSRAT
>
> Das habe ich aufgebaut. [X] Wochen bis zum Termin. [Y] Stunden pro Woche an [Z] Tagen. Schwache Rechtsgebiete ([Liste]) erhalten doppelte Stunden. Drei Phasen: Grundlagen bis [Datum], Intensiv bis [Datum], Wiederholung die letzten [N] Tage. Die ersten zwei Wochen sind tagesgenau geplant. Der Rest ist wochenweise — ich fülle den Tagesplan nach jeder abgeschlossenen Sitzung nach.
>
> Stimmt das so? Zu ambitioniert? Zu wenig? Fehlt ein Rechtsgebiet?

Antwort abwarten. Dann speichern.

## Plan aktualisieren

Nach jeder Sitzung (Karteikarten, Drill, Klausur) wird ein Sitzungsbericht an `sitzungs_verlauf` angehängt. Beim nächsten `--aktualisieren`-Aufruf:
- Schwache Rechtsgebiete (niedrige Ergebnisse in 2+ Sitzungen) werden in Priorität und Stunden hochgestuft
- Geplante, aber nicht absolvierte Einheiten: entweder nachgebucht oder als Lücke markiert
- Wenn der Studierende im Rückstand liegt: Pensum anpassen oder Lücke dokumentieren

## Modi

- `--aufbauen` (Standard, wenn kein Plan vorhanden): Vollständiger Neubau mit Eingaben-Dialog
- `--aktualisieren` (Standard, wenn Plan vorhanden): Sitzungshistorie auswerten, Prioritäten neu gewichten, nächste Tage befüllen
- `--status`: Was ist heute und diese Woche geplant? Scoreverlauf? Was liegt zurück?
- `--intensiv`: Crash-Modus erzwingen (auch wenn mehr als 6 Wochen verbleiben)

## Ausgabeformat

- Prosa-Zusammenfassung vor dem Speichern (mit Bestätigungsfrage)
- YAML-Datei mit vollständiger Planstruktur
- Tagesplan für die ersten zwei Wochen tagesgenau; danach wochenweise

## Beispiel

**Eingabe:** "Lernplan für das Erste Staatsexamen NRW, Termin März 2027, Schwächen: Sachenrecht, Strafrecht BT."

**Ergebnis-Prosa:** 10 Monate bis zum Termin. 3 Phasen. Sachenrecht und StGB BT erhalten je 6 Stunden pro Woche (doppelt gegenüber Standardgewichtung). Repetitorium Hemmer als Ergänzung. Erste Wochen: Grundlagenstruktur Sachenrecht (Eigentum, Besitz, beschränkte dingliche Rechte) und StGB BT (§§ 242 ff., §§ 211 ff. StGB). Ab Woche 12: Klausurenphase mit wöchentlich zwei Zeitklausuren.

## Risiken und typische Fehler

- **Zu ambitioniöse Stundenzahl**: Ein Plan mit 50 Stunden pro Woche, den ein vollzeitberufstätiger Studierender aufgestellt hat, bricht in Woche 2. Besser 25 ehrliche Stunden als 50 geplante.
- **Kein Repetitoriums-Abgleich**: Wer parallel Repetitorium und eigenem Plan folgt, verbringt Zeit in zwei Vollcurricula. Eines als primär wählen.
- **Ruhetage weglassen**: Pläne ohne Ruhetage haben eine Halbwertszeit von zwei Wochen.
- **Sitzungsergebnisse nicht einpflegen**: Der Plan ist nur so gut wie das Feedback, das er bekommt. Sitzungsberichte müssen regelmäßig angehängt werden.
- **Wiederholungsphase unterschätzen**: Die letzten Tage sind Konsolidierung, keine Lernphase. Wer kurz vor dem Examen neues Material aufnimmt, verschlechtert seine Leistung.

## Quellenpflicht

Zeitschätzungen je Rechtsgebiet sind Orientierungswerte auf Basis typischer Examensgewichtungen — nicht Garantien. Hochprioritäre Themen richten sich nach dem Pflichtfachkatalog des Bundeslandes und der Examenspraxis der letzten Jahre. `[SCHÄTZUNG]` markiert alle Zeitangaben, die auf allgemeinen Erfahrungswerten beruhen.

Hinweis: Dieser Lernplan ersetzt keine Beratung durch Seminarleiter, Repetitoren oder Examenscoaches, die den individuellen Kenntnisstand kennen.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

## 3. `lernsitzung`

**Fokus:** Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Lösungsschemata Zivilrecht Strafrecht öffentliches Recht. Prüfraster Thema und Lernziel festlegen, Erklärung Kontrollfragen Uebungsfall Feedback, Wissenslücken identifizieren. Output strukturierte Lernsitzung mit Erklärungen und Zwischentest. Abgrenzung zu Karteikarten für Memorierung und zu Gutachten-Uebung für Klausurtraining.

# Lerneinheit

## Zweck

Eine strukturierte Lerneinheit mit einer festen Anzahl an Fragen — Karteikarten-Drill, Klausurfrage im Gutachtenstil oder Mündlichkeitssimulation. Die Ergebnisse fließen in den Lernplan ein, sodass die nächste Einheit auf dem aufsetzt, was in dieser Einheit schwierig war.

## Eingaben

- **Rechtsgebiet** (z. B. "Schuldrecht AT", "§§ 242, 243 StGB", "Verwaltungsrecht Ermessen")
- **Anzahl der Fragen** (N)
- **Modus** (`--karteikarten` | `--klausurfrage` | `--mündlich`, Standard: Nachfrage)
- Optional: **Schwerpunkt** (z. B. "Schwerpunkt: Kausalität", "nur Definitionen")

## Rechtlicher Rahmen

Die Fragen folgen dem Examensrelevanzkanon für das Erste und Zweite Staatsexamen nach JAG/JAPrO der Bundesländer. Inhaltlicher Maßstab:

**Leitentscheidungen (Beispiele je Modus):**

Karteikarten-Drill (Definitionen):
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Gutachtenstil-Klausurfragen:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Literatur:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Eingaben prüfen

Wenn Rechtsgebiet oder Anzahl fehlen, einmalig fragen:

> "Welches Rechtsgebiet, und wie viele Fragen? (z. B. 'Schuldrecht AT, 10 Fragen' oder 'StGB BT Eigentumsdelikte 5 — Gutachtenstil')"

### Schritt 2: Modus bestimmen und Inhaltsquelle laden

- `--karteikarten`: `karteikarten`-Skill laden, N Karten im Drill-Modus, priorisiert nach früheren Fehlern + fälligen Karten
- `--klausurfrage`: `gutachten-uebung`-Skill laden, N Kurzklausurfragen im Gutachtenstil generieren, Nutzer schreibt Lösung, Feedback pro Frage
- `--mündlich` (Standard): `pruefungsgespraech-ag`-Skill laden, N Fragen im sokratischen Frage-Antwort-Format, Pushback nach jeder Antwort

Jurisdiktion/Prüfungsordnung aus Nutzerprofil laden, falls vorhanden (z. B. Examensvorbereitung NRW → JAG NRW-Prüfungsstoff priorisieren).

### Schritt 3: N Fragen — eine nach der anderen

Nie mehrere Fragen auf einmal. Erst Antwort abwarten, dann nächste Frage.

Nach jeder Frage: kurze Rückmeldung (richtig / teilweise / falsch + Korrektur). Falsche Antworten mit Normangabe erläutern — nie nur "falsch".

### Schritt 4: Sitzungsabschluss

Am Ende der N Fragen:
- Ergebnis: X/N richtig (Prozentwert)
- Nicht gewusste Themen: Liste mit Unterthema-Tags
- Schwache Unterthemen dieser Sitzung
- Vergleich mit früheren Sitzungen zu diesem Rechtsgebiet (falls Verlauf existiert)
- Empfehlung für die nächste Sitzung

Sitzungsbericht schreiben:

```yaml
sitzungs_verlauf:
 - datum: 2026-05-08
 rechtsgebiet: Schuldrecht AT
 typ: karteikarten # oder klausurfrage / mündlich
 fragen_anzahl: 10
 richtig: 7
 teilweise: 1
 falsch: 2
 schwache_themen: [§ 275 Abs. 1 BGB Unmöglichkeit, § 286 Abs. 2 BGB Verzug ohne Mahnung]
```

Falls Lernplan vorhanden: Sitzungsbericht an `lernplan.yaml` → `sitzungs_verlauf` anhängen.
Falls kein Lernplan: in `sitzungs_verlauf.yaml` schreiben.

### Schritt 5: Anschlussempfehlung

> "Auf Basis dieser Sitzung empfiehlt sich als nächster Schritt: [konkrete Empfehlung — z. B. 'Definitionen § 275 BGB mit karteikarten vertiefen' oder 'gutachtenstil-übung: Klausurfall zu § 286 BGB']."

## Ausgabeformat

- Fragen einzeln, eine nach der anderen
- Rückmeldung je Frage: kurz und normgenau
- Sitzungsabschluss: tabellarische Auswertung + Verlaufsmuster (ab 2+ Sitzungen zu demselben Rechtsgebiet)
- YAML-Sitzungsbericht für den Lernplan

## Beispiel

**Eingabe:** "10 Fragen Strafrecht BT Eigentumsdelikte, Modus mündlich"

**Verlauf (Auszug):**

> Frage 1: A nimmt heimlich das Fahrrad des B mit, um es dauerhaft zu behalten. Welche Straftatbestände kommen in Betracht, und wie lautet der Obersatz für den ersten Anspruch?

Nutzer antwortet. Skill prüft: Ist § 242 Abs. 1 StGB (Diebstahl) benannt? Obersatz vorhanden? Fremdheit der Sache, Wegnahme, Zueignungsabsicht als Prüfungspunkte erwähnt?

Pushback falls unvollständig: "Sie haben § 242 StGB benannt — gut. Was ist Wegnahme? Definition, bitte."

**Sitzungsabschluss:** 7/10 richtig. Schwache Themen: Abgrenzung § 242/246 StGB (Diebstahl/Unterschlagung), Gewahrsamsbruch-Definition. Empfehlung: Karteikarten § 242–248c StGB + eine Klausurfrage zur Abgrenzung.

## Risiken und typische Fehler

- **Rechtsgebiet zu weit gewählt**: "BGB" als Rechtsgebiet für eine 10-Fragen-Einheit ist sinnlos breit. Auf Unterthemen eingrenzen (z. B. "BGB AT Stellvertretung §§ 164 ff.").
- **Modus nicht zur Lernphase passend**: Karteikarten sind für Definitionen-Memorierung. Gutachtenstil-Klausurfragen für Strukturtraining. Mündlich für Verständnis-Tiefe. Den richtigen Modus zur richtigen Lernphase wählen.
- **Sitzungsergebnisse nicht verwerten**: Der Wert der Sitzungshistorie liegt darin, dass schwache Themen bei der nächsten Sitzung priorisiert werden. Sitzungen ohne Auswertung sind verlorenes Feedback.
- **Lernplan-Abweichungen ignorieren**: Wenn die Sitzungshistorie zeigt, dass ein Thema in drei Sitzungen hintereinander schlecht abgeschnitten hat, muss es im Lernplan hochgestuft werden — nicht nur in der nächsten Sitzung wiederholt.

## Quellenpflicht

Normangaben und Definitionen in Fragen und Korrekturen folgen gefestigter Rechtsprechung und kanonischer Literatur. Werden Fragen aus meinem Wissen generiert (nicht aus bereitgestellten Quellen), gilt: inhaltliche Korrektheit ist mit `[PRÜFEN]` markiert, wenn keine sichere Verifikation möglich ist. Vor dem Einlernen gegen Skript oder Kommentar abgleichen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
