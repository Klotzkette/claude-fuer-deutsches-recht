---
name: semester-uebergabe
description: >
  Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene
  Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende
  Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber
  an die nächste übergibt. Liest Fristendatei, Mandantenkommunikationslog und
  Fallhistorie. Lädt, wenn der Supervisor oder abgehende Studierende den
  Semesterabschluss koordinieren, Übergabenotizen erstellen oder einen
  ausscheidenden Studierenden abmelden müssen.
language: de
triggers:
  - "Semesterübergabe"
  - "Fallübergabe"
  - "Kohorte abschließen"
  - "Mandatsübergabe"
  - "Abschluss Semester"
  - "nächste Kohorte"
  - "Exmatrikulation Beratungsstelle"
  - "Mandantenakten übergeben"
  - "Fallakte weiterleiten"
---

# Semesterübergabe

## Zweck

Jedes Semester verliert die Rechtsberatungsstelle ihre gesamte studentische Belegschaft und baut sie neu auf. `/einarbeitung` löst die eine Hälfte des Problems — Einarbeitung der neuen Kohorte. Diese Skill löst die andere Hälfte: Sie verabschiedet die abgehende Kohorte, indem sie Übergabenotizen erstellt, die alle für den Fortgang notwendigen Informationen zu jedem laufenden Mandat enthalten.

Ohne diese Übergabe verlässt das Fallwissen die Beratungsstelle mit den Studierenden. Die neue Kohorte beginnt mit der Fallakte und der Aktennotiz — das reicht nie. Zwei Wochen gehen für die Wiedereinarbeitung verloren; der Mandant erlebt dies als Rückschritt: Anrufe bleiben unbeantwortet, bereits beantwortete Fragen werden erneut gestellt.

**Mandatsgeheimnis:** Übergabenotizen enthalten vertrauliche Mandantendaten (§ 43a Abs. 2 BRAO, § 203 StGB). Sie werden ausschließlich innerhalb der Beratungsstelle zwischen beteiligten Studierenden und dem Supervisor ausgetauscht — niemals per privater E-Mail, Chat-Dienst oder sonstiger ungesicherter Verbindung.

## Eingaben

- **Semester** (Standard: laufendes Semester)
- **Einzelner Fall** (optional: `--fall=[fall-id]`) für Einzelfall-Übergabe (z. B. bei vorzeitigem Ausscheiden)
- **Aktive Fallliste** — wenn die Klinik kein zentrales Fallregister führt, muss diese als Eingabe übergeben werden; die Skill erfindet keine Fälle
- **Zuordnung:** Wer geht, wer kommt — falls bekannt; sonst „TBD — Supervisor weist zu"

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; gilt sinngemäß für Studierende der Beratungsstelle. Die Übergabenotiz enthält nur Informationen, die für die Fallfortführung unbedingt notwendig sind.
- **§ 203 Abs. 1, Abs. 3 StGB** — Verletzung von Privatgeheimnissen: Die Weitergabe von Mandantendaten an nicht-befugte Dritte ist strafbar. Studierende als „berufsmäßig tätige Gehilfen" i. S. d. § 203 Abs. 3 S. 2 StGB.
- **§ 6 Abs. 2 RDG** — Aufsichtspflicht: Fallübergaben sind ein Aufgabenbereich, der der Supervisorenkontrolle bedarf; der begleitende Rechtsanwalt/die begleitende Rechtsanwältin zeichnet die Übergabe ab.
- **§ 50 BRAO** — Aufbewahrungspflicht für Handakten: Der Supervisor hat Unterlagen nach Mandatsende mindestens 5 Jahre aufzubewahren; die Übergabenotizen sind Teil der Handakte im Rechtssinne.
- **DSGVO Art. 5 Abs. 1 lit. f** (Integrität und Vertraulichkeit), **Art. 32 DSGVO** — Technische und organisatorische Maßnahmen für die Datensicherheit; sichere Übertragungswege für Übergabenotizen.

### Leitentscheidungen

- BGH, Urt. v. 21.06.2012 – IX ZR 32/10, NJW 2012, 2435 Rn. 14 — Handaktenpflicht des Rechtsanwalts; Inhalt und Aufbewahrung; sinngemäß für Klinikakten.
- BGH, Urt. v. 15.04.2010 – IX ZR 189/09, NJW 2010, 2050 Rn. 8 — Verschwiegenheitspflicht bleibt auch nach Mandatsende bestehen; Übergabenachrichten an Dritte außerhalb der Kanzlei sind zu unterlassen.
- BGH, Urt. v. 26.11.2015 – IX ZR 144/14, NJW 2016, 954 Rn. 18 — Kontinuitätspflicht bei Anwaltsübergaben; der übernehmende Anwalt muss vollständig informiert werden; Parallele für Studierende in der Beratungsstelle.
- BVerfG, Beschl. v. 12.04.2005 – 2 BvR 1027/02, NJW 2005, 1917 — Beschlagnahmeschutz anwaltlicher Unterlagen; Grundlage für Vertraulichkeit aller Klinikakten.

### Kommentarliteratur

- Kleine-Cosack, BRAO, 8. Aufl. 2022, § 43a Rn. 15 ff. — Verschwiegenheitspflicht; Umfang, Ausnahmen, Weitergabe an Dritte.
- Deckenbrock/Henssler, RDG, 5. Aufl. 2021, § 6 Rn. 35 ff. — Dokumentations- und Übergabepflichten in der Rechtsberatungsstelle.
- Gola, DSGVO, 3. Aufl. 2022, Art. 5 Rn. 25 ff. — Vertraulichkeit und Integrität; technische und organisatorische Maßnahmen bei der Datenweitergabe.
- Zöller/Greger, ZPO, 35. Aufl. 2024, § 85 Rn. 8 — Anwaltswechsel und Kontinuität der Verfahrensführung; Parallele zur studentischen Fallübergabe.

## Ablauf

### Schritt 1: Fälle und Zuständigkeiten identifizieren

- Alle aktiven Fälle erfassen (aus Fallregister + `deadlines.yaml` Fall-IDs + Kommunikationslogs)
- Für jeden Fall: Wer ist der aktuelle/die aktuelle Bearbeiter/-in? Bleibt diese Person oder scheidet sie aus?
- Zuordnung: Ausscheidende/-r → Nachfolger/-in (falls bekannt; sonst „TBD — Supervisor weist zu")

Falls kein zentrales Fallregister existiert: Eingabe einer Fallliste erforderlich. Nicht raten.

### Schritt 2: Fallbezogene Übergabenotiz

Für jeden Fall:

```markdown
# Fallübergabe — [Fallbezeichnung] — [Semester-Ende]

**Fall-ID:** [fall-id]
**Rechtsgebiet:** [Gebiet]
**Ausscheidende/-r Studierende/-r:** [Name]
**Nachfolger/-in:** [Name oder „TBD"]
**Begleitender Supervisor:** [Name]
**Mandant:** [Name oder Mandanten-ID — kein Klarname in unsicheren Systemen]

---

## Aktueller Stand

[Ein Absatz: Verfahrensstand. Was ist getan, was steht aus, wo geht der Fall hin.
Falls der Fall an einem natürlichen Haltepunkt steht (zwischen Einreichungen, wartend
auf Behördenantwort), dies benennen.]

## Offene Fristen

*Aus `deadlines.yaml`. Erste Aufgabe der/des Nachfolger/-in: Fristen bestätigen und übernehmen.*

| Fällig | Typ | Beschreibung | Hinweise |
|---|---|---|---|
| [Datum] | [Typ] | [Einzeiler] | [bei Dringlichkeit: „DRINGEND — fällig innerhalb von [N] Tagen nach Semesterbeginn"] |

## Was getan wurde

- [Wichtige Schritte dieses Semesters: Erstberatung, Einreichungen, Termine, wesentliche Schriftstücke]
- [Erstellte Dokumente — mit Verweis auf Ablageort]

## Was noch offen ist

- [Ausstehende Entscheidungen: z. B. „Mandantin hat noch nicht über das Vergleichsangebot entschieden"]
- [Recherche-Lücken: z. B. „§ 556g BGB Mietpreisbremse — Ausnahmen noch nicht abschließend geprüft"]
- [Offene Kommunikation: z. B. „Antwort der Behörde auf Widerspruch ausstehend"]

## Mandantenbeziehung

- [Wie oft Kontakt? Telefon, E-Mail, persönlich?]
- [Relevanter Beziehungskontext für Nachfolger/-in: Sprache, besondere Lebensumstände, Kommunikationspräferenzen]
- [Nächster geplanter Kontakt oder Termine]

## Erstellte und eingereichte Schriftstücke

*Verweise, kein Inhalt.*

- [Datum] [Schriftstücktyp] — [Ablagepfad] — [Status: eingereicht / Entwurf / in Supervisor-Prüfung]

## Kommunikationshistorie-Zusammenfassung

*Aus dem Kommunikationslog. Dreizeilige Zusammenfassung hier; Nachfolger/-in liest den vollständigen Log.*

[Kurze Zusammenfassung des jüngsten Kommunikationsmusters — z. B. „3 Telefonate seit Erstberatung, alle auf Russisch, Mandantin bevorzugt abends. Letzter Kontakt: 15.04.2026, Adresse für Schriftstück bestätigt."]

## Hinweise des Supervisors an Nachfolger/-in

*Vom Supervisor vor Weiterleitung der Übergabenotiz ergänzt. Kann enthalten: „Dieser Fall hat eine sensible Familiensituation — Akte vor dem ersten Kontakt genau lesen"; „Mandant hat gebeten, alle Post an Postfach, nicht Hausadresse"; „Es gibt noch eine offene Scoping-Frage — erste Woche mit mir besprechen."*

[Hinweise, oder „keine"]

## Erste-Woche-Prioritäten für Nachfolger/-in

1. [Konkret — z. B. „Mandantin innerhalb von 48 Stunden nach Fallübernahme anrufen. Sich vorstellen, Fallübernahme bestätigen."]
2. [Fristenbezogen — z. B. „Widerspruchsfrist endet am [Datum]. Entwurf des abgehenden Studierenden prüfen, überarbeiten, einreichen."]
3. [Wissenslücke — z. B. „Gutachten des abgehenden Studierenden zur Mietpreisbremse lesen, bevor am [Datum] die Verhandlung stattfindet."]

---

**Übergabe erstellt von:** [Ausscheidende/-r Studierende/-r]
**Datum:** [JJJJ-MM-TT]
**Geprüft von:** [Supervisor, sofern Supervisionsmodell dies vorsieht]
```

### Schritt 3: Kohorten-Gesamtübersicht

Nach allen fallbezogenen Notizen, `handoffs/[semester]/_zusammenfassung.md` erstellen:

```markdown
# Kohortenübergabe-Zusammenfassung — [Semester-Ende]

**Ausscheidende Studierende:** [N]
**Eintretende Studierende:** [N]
**Laufende, zu übergebende Fälle:** [N]
**Fälle, die zum Semesterende abgeschlossen werden (keine Übergabe):** [N]

---

## Übergaben

| Fall | Ausscheidend | Nachfolge | Rechtsgebiet | Dringlichkeit |
|---|---|---|---|---|
| [fall-id] | [Name] | [Name oder TBD] | [Gebiet] | [normal / Frist innerhalb 2 Wochen / dringend] |

## Nicht zugewiesen

[Fälle, für die „TBD" als Nachfolger/-in eingetragen ist — Supervisor weist vor Semesterstart zu]

## Fristen innerhalb von 30 Tagen nach Semesterbeginn

[Aus deadlines.yaml — das sind die Fälle, in die die neue Kohorte sofort einarbeiten muss]

## Hinweise für den Supervisor

- [Falls in diesem Semester besondere Leistungsprobleme bei Studierenden aufgefallen sind — für engere Begleitung im Folgesemester notieren]
- [Falls ausscheidende Studierende bereit sind, für den Nachfolger/die Nachfolgerin zur Verfügung zu stehen — z. B. Absolvent/-in, der/die die Übergabe begleiten möchte]
- [Muster über Fälle hinweg — z. B. „Drei von sechs Fällen haben Fristen in den ersten 14 Tagen des neuen Semesters; ggf. Einarbeitungs-Übungen auf diese Rechtsgebiete fokussieren"]
```

### Schritt 4: Supervisoren-Prüfung

Das Schließen oder Übergeben eines Falls ist eine folgenschwere Handlung. Das Gate ist das Supervisionsmodell der Beratungsstelle (§ 6 Abs. 2 RDG). Fallabschluss-Notizen werden immer vom Supervisor abgezeichnet, bevor der Fall im Übergabedokument als geschlossen markiert wird — unabhängig vom gewählten Supervisionsmodell.

- **Formelle Prüfwarteschlange:** Jede Übergabenotiz geht in die Warteschlange, bevor sie an den/die Nachfolger/-in weitergeleitet wird.
- **Konfigurierbare Flags:** Notizen erhalten „VOR WEITERLEITUNG MIT [SUPERVISOR] PRÜFEN"; Supervisor prüft informell.
- **Leichtere Begleitung:** Standard-KI-Label; Supervisor prüft über bestehende Betreuungsstruktur. Fallabschlüsse gehen dennoch vor Markierung als geschlossen an den Supervisor.

### Schritt 5: Übergabe vollziehen

Nach Supervisoren-Prüfung liegen die Übergabenotizen unter `handoffs/[semester]/[fall-id].md`. Der/die Nachfolger/-in liest sie im `/einarbeitung`-Durchlauf zu Semesterbeginn — `/einarbeitung` soll die Notizen für die zugewiesenen Fälle surfacen.

## Ausgabeformat

Per-Fall-Übergabenotiz (Markdown) plus Kohortenübersicht, beide nach dem Schema oben. Alle Notizen werden ausschließlich innerhalb der Beratungsstelle über sichere, bestellungsführende Systeme ausgetauscht.

## Beispiel

**Szenario:** Studierende Müller beendet das Semester und gibt Fall `erdem-mietrecht-2026` an nachfolgende Studierende Schulze weiter. Frist: Widerspruch gegen Mieterhöhung am 08.06.2026.

Übergabenotiz enthält: aktueller Stand (Widerspruchsentwurf fertig, wartet auf Supervisoren-Freigabe), Fristtabelle (08.06.2026 — DRINGEND), Was getan wurde (Erstberatung 15.03.2026, Entwurf 01.04.2026), Hinweis Supervisor: „Mandantin spricht nur Türkisch — Schulze soll Dolmetscher organisieren."

## Risiken und typische Fehler

- **Übergabe ohne Mandatsgeheimniswahrung:** E-Mail-Versand von Übergabenotizen über private Konten oder Chat-Dienste verstößt gegen § 203 StGB und DSGVO Art. 5. Nur bestellungsführende, gesicherte Systeme.
- **Fristenübergabe vergessen:** Die gefährlichste Lücke. Alle aktiven Fristen müssen in der Notiz erscheinen; Nachfolger/-in muss sie in `/fristen` als eigene Fristen neu eintragen.
- **Übergabe ohne Supervisoren-Abzeichnung:** § 6 Abs. 2 RDG verlangt effektive Aufsicht. Auch „formlose" Übergaben sind dem Supervisor zu melden.
- **Zu dünne Übergabenotiz:** „Fall läuft gut" ist keine Übergabe. Die Notiz muss so vollständig sein, dass jemand ohne Vorkenntnisse den Fall übernehmen kann.
- **Mandantenkontakt während der Übergabephase nicht gesichert:** Zwischen Ausscheiden der alten und Übernahme durch neue Studierende muss der Supervisor Ansprechbarkeit für den Mandanten sicherstellen.

## Quellenpflicht

Übergabenotizen sind interne Arbeitsdokumente, keine zitierten Rechtsgutachten. Alle darin enthaltenen offenen Rechtsfragen sind in den entsprechenden Skills (`/memo`, `/recherche-start`) mit Quellenangaben zu hinterlegen. Die Übergabenotiz verweist auf das zugrundeliegende Gutachten, zitiert aber keine Normen eigenständig ohne Verifizierung.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
