---
name: interne-untersuchung
description: "Referenz-Skill: gemeinsames Framework für arbeitsrechtliche interne Untersuchungen vom Eingang einer Beschwerde bis zum abschließenden Memo — vertrauliches Untersuchungsprotokoll, Dokumentenverarbeitung mit Relevanzprüfung, Quellendeckungs-Tracking, Abfragen gegen das Protokoll, Memo-Entwurf und Zielgruppen-Zusammenfassungen. Wird von /untersuchung-eroeffnen, /untersuchung-ergaenzen, /untersuchung-abfrage, /untersuchungs-memo und /untersuchungs-zusammenfassung geladen; nicht direkt aufzurufen."
---

# Interne Untersuchung — Referenz-Skill (Arbeitsrecht)

## Zweck

Interne Untersuchungen scheitern auf zwei Wegen: fehlende Quellenabdeckung
(Erkenntnisquellen, die nie erhoben wurden) und fehlende Synthese (Erkenntnisse,
die erhoben wurden, aber nie verknüpft wurden). Diese Skill adressiert beide
Schwachstellen — sie verfolgt, was erhoben wurde und was nicht, verarbeitet
Dokumentenmassen zur Identifikation des Wesentlichen ohne den Anwalt zu
überwältigen, und führt ein strukturiertes Protokoll, das jederzeit zu einem
vertraulichen Memo verdichtet werden kann.

## Vertraulichkeit und Datenschutz

> **Vertraulichkeit.** Alle durch diese Skill erstellten Dateien — Protokolleinträge,
> Memo-Entwürfe, Zielgruppen-Zusammenfassungen, Dokumentennotizen — teilen den
> Vertraulichkeitsstatus der zugrundeliegenden Untersuchung. Eine Weitergabe über
> den autorisierten Kreis hinaus (an nicht beteiligte Dritte, HR ohne ausreichende
> Einschränkung, die Unternehmensseite ohne rechtliche Steuerung) kann den
> Schutzcharakter der Unterlagen gefährden. Alle Dateien dort aufbewahren, wo
> vertrauliche Unterlagen gelagert werden, und jede Weitergabe bewusst entscheiden.

**§ 26 BDSG — Beschäftigtendatenschutz**: Die Verarbeitung personenbezogener
Beschäftigtendaten im Rahmen interner Untersuchungen ist nur zulässig, wenn
sie zur Aufdeckung von Straftaten oder schwerwiegenden Pflichtverletzungen
erforderlich ist und das schutzwürdige Interesse der betroffenen Arbeitnehmer
nicht überwiegt. Verhältnismäßigkeit ist bei jedem Schritt zu prüfen.

**Mitbestimmung § 87 Abs. 1 Nr. 6 BetrVG**: Der Einsatz technischer
Überwachungseinrichtungen (z. B. E-Mail-Auswertung, IT-Forensik) unterliegt
dem Mitbestimmungsrecht des Betriebsrats. Bevor Kommunikationsauswertungen
vorgenommen werden, ist die Zustimmung des Betriebsrats oder eine
Betriebsvereinbarung zur Unternehmensführung erforderlich.

**Detektivkosten**: Kosten für externe Ermittler sind nach der
BAG-Rechtsprechung nur unter engen Voraussetzungen als Schadensersatz
vom Arbeitnehmer ersatzfähig (BAG, Urt. v. 28.10.2010 – 8 AZR 547/09,
NZA 2011, 345).

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Datenverarbeitung für Zwecke des Beschäftigungsverhältnisses;
  Verarbeitung zur Aufdeckung von Straftaten; Verhältnismäßigkeit
- Art. 5, 6 DSGVO: Rechtmäßigkeit der Verarbeitung; berechtigtes Interesse
  als Verarbeitungsgrundlage
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen
  Überwachungseinrichtungen
- § 32 BDSG a.F. / § 26 BDSG n.F.: Kontinuität der Rspr. zur
  Beschäftigtendatenverarbeitung
- § 611a BGB: Arbeitnehmereigenschaft; Mitwirkungspflichten im
  Arbeitsverhältnis
- § 241 Abs. 2 BGB: Nebenpflichten, insbesondere Auskunftspflicht des
  Arbeitnehmers im Rahmen des Arbeitsverhältnisses
- §§ 626, 314 BGB: Außerordentliche Kündigung bei schwerwiegenden
  Pflichtverletzungen; Verdachtskündigung

**Leitentscheidungen:**

- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 Rn. 14 ff.:
  Verdachtskündigung — Voraussetzungen: dringender Tatverdacht auf Basis
  objektiver Umstände, Verhältnismäßigkeit, vorherige Anhörung des
  Arbeitnehmers als zwingende Wirksamkeitsvoraussetzung
- BAG, Urt. v. 28.10.2010 – 8 AZR 547/09, NZA 2011, 345 Rn. 26 ff.:
  Erstattungsfähigkeit von Detektivkosten — nur soweit konkrete Verdachtslage
  bei Beauftragung bestand und Verhältnismäßigkeit gewahrt ist
- BAG, Urt. v. 13.12.2007 – 2 AZR 537/06, NZA 2008, 1008 Rn. 18 ff.:
  Verwertungsverbot rechtswidrig erlangter Erkenntnisse — heimliche
  Videoüberwachung ohne Mitbestimmung des Betriebsrats; Beweisverwertungsverbot
- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 Rn. 29 ff.:
  Anhörung vor Verdachtskündigung — inhaltliche Mindestanforderungen und
  Fehlerfolgen bei fehlerhafter Anhörung

**Kommentarliteratur:**

- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 165 ff.:
  Verdachtskündigung — Voraussetzungen, Verfahren, Anhörung
- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 120 ff.:
  Datenverarbeitung zur Aufdeckung von Straftaten im Beschäftigungsverhältnis;
  Verhältnismäßigkeitsgrundsatz
- Erfurter Kommentar/Kania, 24. Aufl. 2024, § 87 BetrVG Rn. 62 ff.:
  Mitbestimmung bei technischen Überwachungseinrichtungen; Reichweite
  im Kontext interner Untersuchungen
- Bauer/Krieger/Günther, AGG, 5. Aufl. 2022, Einleitung Rn. 80 ff.:
  Untersuchung von Diskriminierungsvorwürfen; Beweislastverteilung nach § 22 AGG

---

## Modus 1: Neue Untersuchung eröffnen

Ausgelöst durch `/arbeitsrecht:untersuchung-eroeffnen` oder
„Untersuchung eröffnen" / „Untersuchung einleiten wegen".

### Schritt 1 — Sachverhaltserfassung

Frage folgende Punkte in einem einzigen Block ab:

> Zur Eröffnung des Untersuchungsprotokolls werden folgende Angaben benötigt:
>
> **Die Sache**
> - Was ist der Vorwurf oder die Besorgnis in eigenen Worten?
> - Wer ist Beschwerdeführer/in (oder welches Ereignis hat die Untersuchung
>   ausgelöst — Beschwerde, Hinweis, Revision, Vorgesetztenwahrnehmung)?
> - Wer ist die beschuldigte oder in Frage stehende Person?
> - Welcher ungefähre Zeitraum soll untersucht werden?
> - Ist die Untersuchung anwaltsgeleitet? (Wenn ja: erhöhter Schutz
>   der Arbeitsergebnisse. Wenn nein: Schutzstatus vor Beginn klären.)
>
> **Art der Untersuchung** (bestimmt die passende Quellencheckliste)
> - HR: Belästigung / Diskriminierung / Benachteiligung (AGG)
> - Finanzen: Spesenmanipulation / Beschaffungsunregelmäßigkeiten / Untreue
> - Führungskraft: Interessenkonflikt / unzulässige Beziehungen /
>   Governance-Verstöße
> - Hinweisgeber: Vergeltung gegen geschützte Tätigkeit (§§ 34, 36 HinSchG)
> - Sonstiges: kurz beschreiben
>
> **Vertretung und Betriebsrat**
> - Ist die beschuldigte Person, die beschwerdeführende Person oder ein
>   erwarteter Zeuge durch einen Betriebsrat vertreten oder durch Tarifvertrag
>   erfasst? (Wenn ja: Informationsrecht des Betriebsrats nach § 102 BetrVG
>   bei etwaiger Kündigung beachten; kein eigenständiges Teilnahmerecht an
>   Investigativgesprächen, aber § 82 Abs. 2 BetrVG: Arbeitnehmer darf
>   Betriebsratsmitglied zur Besprechung über Beschwerde hinzuziehen)
> - Ist die Gesellschaft ein öffentlich-rechtlicher Arbeitgeber (Behörde,
>   Hochschule, Staatsunternehmen)? (Wenn ja: Besonderheiten des öffentlichen
>   Dienstrechts, ggf. Personalvertretungsgesetz statt BetrVG prüfen)

Wenn Betriebsratsteilnahme-Frage aufgeworfen wird: § 82 Abs. 2 BetrVG,
§ 84 BetrVG (Beschwerderecht), § 85 BetrVG (Behandlung von Beschwerden)
recherchieren, bevor Gespräche geführt werden.

### Schritt 2 — Verzeichnis und Dateien anlegen

Erstelle folgende Dateien:

`investigation-[slug]/log.yaml`:

```yaml
# VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]
sache: "[Sachbezeichnung]"
sache_slug: "[slug]"
eroeffnet: "[ISO-Datum]"
anwaltsgeleitet: [true/false]
vorwurf: "[Sachverhaltsdarstellung in eigenen Worten]"
beschwerdefuehrer: "[Name/Funktion oder anonym]"
beschuldigter: "[Name/Funktion]"
tatverdachtszeitraum: "[ungefähre Daten]"
untersuchungsart: "[HR/Finanzen/Fuehrungskraft/Hinweisgeber/Sonstiges]"
status: offen
zuletzt_aktualisiert: "[ISO-Datum]"

fragen:
  - "[Frage 1 — aus dem Vorwurf abgeleitet, z. B. 'Liegt eine unzulässige
     Benachteiligung nach § 3 AGG vor?']"
  - "[Frage 2 falls zutreffend]"

eintraege: []

beweisluecken: []
```

`investigation-[slug]/quellen-checkliste.yaml`:
Wird aus der Untersuchungsart generiert — siehe Checklisten-Vorlagen unten.

`investigation-[slug]/dokumente-geprueft.yaml`:

```yaml
# VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]
sache: "[Sachbezeichnung]"
gesamt_geprueft: 0
gesamt_relevant: 0
zuletzt_aktualisiert: "[ISO-Datum]"
dokumente: []
```

### Schritt 3 — Quellencheckliste

Erstelle die passende Checkliste je nach Untersuchungsart und lege sie dem
Anwalt vor: „Passt diese Checkliste zu Ihrer Sache? Bitte melden Sie, welche
Punkte nicht anwendbar sind (werden als N/A markiert) und ob weitere
Quellen hinzukommen."

**HR-Untersuchung (Belästigung/Diskriminierung/Benachteiligung AGG):**
```yaml
quellen:
  - id: 1
    quelle: "Anhörung Beschwerdeführer/in"
    status: offen
    notizen: ""
  - id: 2
    quelle: "Anhörung Beschuldigte/r"
    status: offen
    notizen: ""
  - id: 3
    quelle: "Zeugenbefragungen — identifizieren aus Schilderungen beider Seiten"
    status: offen
    notizen: ""
  - id: 4
    quelle: "E-Mail-/Kommunikationsauswertung — Beteiligte, relevanter Zeitraum
             (§ 87 Abs. 1 Nr. 6 BetrVG beachten: Mitbestimmung Betriebsrat)"
    status: offen
    notizen: ""
  - id: 5
    quelle: "Personalakte Beschuldigte/r — Leistungsbeurteilungen, frühere
             Beschwerden, Disziplinarmaßnahmen"
    status: offen
    notizen: ""
  - id: 6
    quelle: "Frühere Beschwerden gegen Beschuldigte/n im HR-System"
    status: offen
    notizen: ""
  - id: 7
    quelle: "Vergleichspersonenanalyse — wie wurden ähnliche Fälle behandelt"
    status: offen
    notizen: ""
  - id: 8
    quelle: "Einschlägige Richtlinien — AGG-Richtlinie, Verhaltenskodex,
             Beschwerdeverfahren (Version zum Tatzeitpunkt)"
    status: offen
    notizen: ""
  - id: 9
    quelle: "Organigramm und Berichtslinien zum Tatzeitpunkt"
    status: offen
    notizen: ""
  - id: 10
    quelle: "Kalender / Terminvermerke — Besprechungen oder Ereignisse,
             die in Schilderungen erwähnt wurden"
    status: offen
    notizen: ""
  - id: 11
    quelle: "Dokumentation der Anhörungshinweise (§ 82 Abs. 2 BetrVG /
             Hinweis auf Recht zur Hinzuziehung eines BR-Mitglieds)"
    status: offen
    notizen: ""
```

**Finanzuntersuchung:**
```yaml
quellen:
  - id: 1
    quelle: "Spesenabrechnungen — betroffene Person, relevanter Zeitraum"
    status: offen
    notizen: ""
  - id: 2
    quelle: "Genehmigungsunterlagen — wer hat Ausgaben oder Transaktionen
             genehmigt"
    status: offen
    notizen: ""
  - id: 3
    quelle: "Lieferanten-/Auftragnehmerakte — Verträge, Rechnungen, Zahlungsbelege"
    status: offen
    notizen: ""
  - id: 4
    quelle: "Finanzsystem-Auswertungen — Kreditoren, Hauptbuch, relevante Konten"
    status: offen
    notizen: ""
  - id: 5
    quelle: "E-Mail-/Kommunikationsauswertung — betroffene Person, Genehmiger,
             Gegenparteien (§ 87 Abs. 1 Nr. 6 BetrVG beachten)"
    status: offen
    notizen: ""
  - id: 6
    quelle: "Anhörung der betroffenen Person"
    status: offen
    notizen: ""
  - id: 7
    quelle: "Anhörung Genehmiger"
    status: offen
    notizen: ""
  - id: 8
    quelle: "Anhörung Lieferanten / Auftragnehmer (soweit zugänglich)"
    status: offen
    notizen: ""
  - id: 9
    quelle: "Audit-Logs — Systemzugriffe für relevante Konten/Systeme"
    status: offen
    notizen: ""
  - id: 10
    quelle: "Frühere Prüfungen oder Reviews für den relevanten Zeitraum"
    status: offen
    notizen: ""
```

**Untersuchung Führungskraft (Interessenkonflikt/Governance):**
```yaml
quellen:
  - id: 1
    quelle: "Anhörung betroffene Führungskraft"
    status: offen
    notizen: ""
  - id: 2
    quelle: "Aufsichtsrats-/Gesellschafterbeschlüsse — relevante Resolutionen,
             Protokolle, Genehmigungen"
    status: offen
    notizen: ""
  - id: 3
    quelle: "Anstellungsvertrag und Änderungen / Nachträge"
    status: offen
    notizen: ""
  - id: 4
    quelle: "Beteiligungsunterlagen — Optionen, Übertragungen, Unverfallbarkeit"
    status: offen
    notizen: ""
  - id: 5
    quelle: "Spesenabrechnungen und Genehmigungsunterlagen"
    status: offen
    notizen: ""
  - id: 6
    quelle: "E-Mail-/Kommunikationsauswertung — betroffene Person, relevante
             Gegenparteien (§ 87 Abs. 1 Nr. 6 BetrVG beachten)"
    status: offen
    notizen: ""
  - id: 7
    quelle: "Interessenkonflikt-Erklärungen (oder Fehlen davon)"
    status: offen
    notizen: ""
  - id: 8
    quelle: "Unterlagen zu Nebentätigkeiten"
    status: offen
    notizen: ""
  - id: 9
    quelle: "Zeugenbefragungen — direkte Mitarbeiter, Kollegen, AR-Mitglieder"
    status: offen
    notizen: ""
  - id: 10
    quelle: "Frühere Beschwerden oder Hinweise auf betroffene Person"
    status: offen
    notizen: ""
```

**Hinweisgeberuntersuchung (HinSchG / Retaliation):**
```yaml
quellen:
  - id: 1
    quelle: "Anhörung hinweisgebende Person"
    status: offen
    notizen: ""
  - id: 2
    quelle: "Ursprüngliche Meldung oder Hinweis — schriftlich, soweit vorhanden"
    status: offen
    notizen: ""
  - id: 3
    quelle: "Unterlagen zum gemeldeten Sachverhalt (der eigentliche Hinweis)"
    status: offen
    notizen: ""
  - id: 4
    quelle: "Unterlagen zu nachteiligen Maßnahmen gegenüber hinweisgebender
             Person nach der Meldung (§§ 36, 37 HinSchG)"
    status: offen
    notizen: ""
  - id: 5
    quelle: "Anhörung Entscheidungsträger der nachteiligen Maßnahme"
    status: offen
    notizen: ""
  - id: 6
    quelle: "Vergleichspersonenanalyse — Behandlung vergleichbarer Personen
             ohne Meldetätigkeit"
    status: offen
    notizen: ""
  - id: 7
    quelle: "E-Mail-/Kommunikationsauswertung — Entscheidungsträger,
             relevanter Zeitraum"
    status: offen
    notizen: ""
  - id: 8
    quelle: "Zeitliche Nähe: Meldetätigkeit zu nachteiliger Maßnahme
             (§ 36 Abs. 2 HinSchG: Beweislastumkehr)"
    status: offen
    notizen: ""
  - id: 9
    quelle: "Anhörung Beschuldigte/r / Entscheidungsträger"
    status: offen
    notizen: ""
```

---

## Modus 2: Daten hinzufügen

Ausgelöst durch `/arbeitsrecht:untersuchung-ergaenzen`.

### Schritt 1 — Sache identifizieren

Falls mehrere Untersuchungsordner existieren: Frage, zu welcher Sache die
Daten gehören. Bei nur einer Sache: direkt fortfahren.

### Schritt 2 — Datenart identifizieren

Frage (sofern nicht aus dem Kontext klar):
- Befragungsnotizen (von wem?)
- Dokumentenpaket (E-Mails, Akten, Dateien)
- Anwaltsnotizen oder Beobachtungen
- Bestätigung eines Anhörungshinweises

**§ 26 BDSG-Verhältnismäßigkeitsprüfung**: Bei Dokumentenpaketen stets prüfen,
ob die Verarbeitung der enthaltenen Beschäftigtendaten zur Aufklärung des
Vorwurfs erforderlich und verhältnismäßig ist.

### Schritt 3 — Auswahlkriterien für Dokumente

Für jedes Dokumentenpaket gelten folgende Auswahlkriterien. Ein Dokument
wird markiert, wenn es mindestens eines erfüllt. Die Kriterien sind bewusst
etwas weit gefasst — ein False Positive ist besser als ein übersehener
relevanter Fund.

**Auswahlkriterien:**
1. Enthält den Namen einer Untersuchungsbeteiligten (Beschwerdeführer/in,
   Beschuldigte/r, benannte Zeugen)
2. Wurde von einer Beteiligten verfasst oder empfangen und datiert auf den
   relevanten Tatzeitraum
3. Enthält Schlüsselwörter zum Vorwurfstyp (aus der Sachverhaltserfassung
   und aus früheren Protokolleinträgen — Stichwortliste laufend ergänzen)
4. Enthält explizite oder implizite Selbstbelastungen (z. B. „das hätte ich
   nicht tun sollen", „ich weiß, wie das aussieht", „schreib das nicht auf",
   „lösch das")
5. Enthält Aussagen, die einem bereits protokollierten Zeugenbericht
   widersprechen — Widerspruch und den betroffenen Protokolleintrag benennen
6. Enthält sprach- oder inhaltlich sensibles Material: diskriminierende
   Ausdrücke, Drohungen, Bezugnahmen auf geschützte Merkmale (§ 1 AGG),
   Unregelmäßigkeiten, die dem Vorwurfsmuster entsprechen
7. Ist ein Dokumententyp, der in früheren Schilderungen erwähnt, aber noch
   nicht im Dokumentensatz aufgetaucht ist → als Beweislücke protokollieren,
   nicht als Treffer

**Disposition für jedes geprüfte Dokument:**
- `relevant`: erfüllt eines oder mehrere Auswahlkriterien — als Protokolleintrag hinzufügen
- `geprueft-nicht-relevant`: geprüft, kein Auswahlkriterium erfüllt —
  in dokumente-geprueft.yaml mit einem Satz beschreiben

**Nach Bearbeitung eines Dokumentenpakets melden:**

```
Dokumentenprüfung abgeschlossen.
Geprüft: [N] Dokumente
Relevant: [N]
Geprüft / nicht relevant: [N]
Neue Beweislücken: [N]

Relevante Dokumente:
[Liste mit einem Satz Beschreibung und dem Auswahlkriterium, das angesprungen ist]
```

### Schritt 4 — Protokolleinträge schreiben

Für jeden relevanten Fund, Anhang an log.yaml:

```yaml
- eintrag_id: [fortlaufend]
  eintrag_typ: [befragung / dokument / anwaltsnotiz / beweisluecke]
  ereignis_datum: "[Datum des Ereignisses — nicht das Protokolldatum]"
  protokoll_datum: "[ISO-Datetime]"
  quelle: "[Name/Funktion der befragten Person oder Dokumentenbeschreibung]"
  quellen_typ: [beschwerdefuehrer / beschuldigter / zeuge / dokument / anwaltsnotiz]
  fragen: ["[welcher Untersuchungsfrage/-n ist dieser Eintrag zuzuordnen]"]
  bedeutung: [hoch / mittel / hintergrund]
  zusammenfassung: "[was dieser Eintrag zum Erkenntnisstand beiträgt — 2–5 Sätze]"
  zitat: "[wörtliches Zitat wenn bedeutsam — sonst leer]"
  widerspricht_eintrag: [eintrag_id oder null]
  bestaetigt_eintrag: [eintrag_id oder null]
  glaubwuerdigkeitsnotiz: ""
  auswahlkriterium: "[welches Kriterium hat angesprochen — für Dokumente]"
  vertraulich: arbeitsrechtlich-intern
```

Für Beweislücken:

```yaml
- luecke_id: [fortlaufend]
  beschreibung: "[welches Dokument/welche Quelle sollte existieren, fehlt aber]"
  identifiziert_aus: "[welcher Protokolleintrag oder Bericht hat darauf hingewiesen]"
  beschaffungsweg: "[wo es zu bekommen wäre]"
  prioritaet: [hoch / mittel / gering]
  status: offen
```

---

## Modus 3: Protokoll abfragen

Ausgelöst durch `/arbeitsrecht:untersuchung-abfrage`.

Gesamtes Protokoll lesen vor der Antwort. Antworttypen:

**Sachverhaltsabfrage** („Was hat [Person] zu [Thema] gesagt?"):
Aus den Protokolleinträgen antworten, Eintrags-IDs zitieren. Falls das
Protokoll nichts enthält: „Zu [Thema] liegen in diesem Untersuchungsprotokoll
([N] Einträge gesichtet) keine Erkenntnisse vor. Dies sollte ggf. als
Beweislücke erfasst werden."

**Widerspruchsabfrage** („Wo widersprechen sich die Schilderungen?"):
Alle widerspricht_eintrag-Verknüpfungen zeigen. Pro Widerspruch: Was ist
der Konflikt, welche Einträge stehen im Widerspruch, welche dokumentarische
Evidenz besteht?

**Deckungsabfrage** („Was fehlt noch?" / „Wo haben wir Lücken?"):
quellen-checkliste.yaml und beweisluecken im log.yaml auslesen. Melden:
- Noch offene Checklistenpunkte
- Protokollierte Beweislücken
- Schilderungen, die auf bisher nicht erhobene Quellen hinweisen

**Stärkeabfrage** („Was ist die stärkste Evidenz zu jeder Frage?"):
Für jede Untersuchungsfrage: höchstbewertete Protokolleinträge, dokumentarische
Bestätigungen und ungelöste Widersprüche — frageweise strukturiert.

---

## Modus 4: Memo entwerfen oder aktualisieren

Ausgelöst durch `/arbeitsrecht:untersuchungs-memo`.

### Erstmalige Erstellung

Gesamtes Protokoll lesen. Vor dem Entwurf prüfen (Warnung falls nicht erfüllt):
- Mindestens ein Eintrag pro offener Untersuchungsfrage
- Einträge für Beschwerdeführer/in und Beschuldigte/n vorhanden
- Quellencheckliste geprüft (hochprioritäre offene Punkte flaggen)

Memo in folgender Struktur:

```markdown
VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]

---

**VERMERK**

An: [Anwalt eintragen]
Von: [Anwalt eintragen]
Datum: [Datum]
Betr.: Interne Untersuchung — [Sachbezeichnung]
Stand: VORENTWURF

---

## Zusammenfassung

[2–3 Abschnitte: Vorwurf in eigenen Worten, Untersuchungsumfang und
Methodenüberblick, wesentliche Ergebnisse in Stichpunkten (Bestätigt /
Nicht bestätigt / Unklar), empfohlene Maßnahmen. Wird zuletzt geschrieben,
erscheint zuerst.]

---

## Hintergrund und Untersuchungsumfang

**Auslöser:** [Was hat die Untersuchung ausgelöst]

**Untersuchte Vorwürfe:**
[Jede Frage aus dem Protokoll als nummerierter Vorwurf]

**Nicht Untersuchtes:** [Was ausdrücklich ausgeklammert wurde und warum]

**Zeitraum des vorgeworfenen Verhaltens:** [Daten]
**Untersuchungszeitraum:** [Datum Eröffnung] bis [aktuell oder Abschluss]

---

## Methodik

**Durchgeführte Anhörungen:**
| Person | Funktion | Datum | Hinweise |
|---|---|---|---|

**Gesichtete Dokumente:**
[Zusammenfassung nach Dokumentenkategorien, Umfang, Zeitraum.
Vollständiges Dokumentenprotokoll separat geführt.]

**Sonstige Quellen:**
[Richtlinien, Personalakten, sonstige Quellen aus der Checkliste]

**Einschränkungen:** [Angeforderte aber nicht erhaltene Quellen, sonstige Grenzen]

---

## Sachverhaltliche Feststellungen

*[Nach Fragen gegliedert — ein Abschnitt pro Vorwurf. Nicht nach Zeuge,
nicht rein chronologisch.]*

### Frage 1: [Vorwurf]

[Narrative Darstellung der Erkenntnislage. Eintrags-IDs in Klammern zitieren.
Wo Schilderungen im Widerspruch stehen: Widerspruch direkt benennen —
nicht glätten. Dokumentarische Belege mit Zitaten wenn bedeutsam.]

---

## Glaubwürdigkeitsbewertung

*[Eigenständiger Abschnitt. Nur Personen, deren Glaubwürdigkeit entscheidungserheblich
ist — d. h. wo das Ergebnis zu einer Frage davon abhängt, welche Schilderung
geglaubt wird.]*

### [Name/Funktion]

**Innere Konsistenz:** [Konsistent / Inkonsistent — konkrete Angaben]
**Bestätigung:** [Was an dokumentarischer oder sonstiger Evidenz stützt oder
erschüttert die Schilderung]
**Motiv:** [Anlass, die Schilderung zu kreditieren oder zu bezweifeln]
**Impression:** [Beobachtungen des Anwalts bei persönlicher Befragung —
sonst freilassen]
**Bewertung:** [Kreditieren / Nicht kreditieren / Teilweise kreditieren — mit Begründung]

---

## Einschlägige Regelungen

[Zum Tatzeitpunkt geltende Regelungen, die für die Fragen bedeutsam sind.
Version angeben. Keine nach dem Vorfall eingeführten Regelungen zitieren.]

---

## Ergebnisse

| Frage | Ergebnis | Grundlage |
|---|---|---|
| [Frage 1] | Bestätigt / Nicht bestätigt / Unklar | [Ein Satz] |

*Ergebnisse auf Basis des Beweismaßes der überwiegenden Wahrscheinlichkeit.*

---

## Empfehlungen

**Disziplinarische Maßnahmen:** [Falls zutreffend — Grundlage, nicht nur Ergebnis]
**Regelungs- oder Prozessänderungen:** [Falls ein Regelungsdefizit beigetragen hat]
**Schulungen:** [Falls angezeigt]
**Weitere Untersuchung:** [Noch nicht abgeschlossene Stränge]
**Monitoring:** [Erforderliche Nachverfolgung]

---

## Anlage A: Chronologie

[Aus Protokolleinträgen nach ereignis_datum sortiert — nicht nach protokoll_datum.
Format: Datum | Zusammenfassung | Quelle (Eintrags-ID)]

## Anlage B: Gesichtete Dokumente

[Übersichtstabelle aus dokumente-geprueft.yaml]
```

### Falls Memo bereits existiert — Aktualisierung

Memo und Protokoll lesen. Seit dem letzten Entwurf hinzugekommene Einträge
identifizieren.

Änderungen melden, dann fragen: „Soll das gesamte Memo überarbeitet werden
oder nur die betroffenen Abschnitte?"

Änderungen einarbeiten. Geänderte Abschnitte mit `[AKTUALISIERT: Datum]`
markieren bis zur Freigabe durch den Anwalt.

---

## Modus 5: Zielgruppen-Zusammenfassung

Ausgelöst durch `/arbeitsrecht:untersuchungs-zusammenfassung`.

Frage: Für wen ist die Zusammenfassung und welche Entscheidung oder Maßnahme
soll sie unterstützen?

**HR-Zusammenfassung** (für disziplinarische Entscheidung):
- Was ist passiert (Sachverhaltsdarstellung, keine Rechtsanalyse)
- Ergebnis zu jedem Vorwurf (Bestätigt / Nicht bestätigt / Unklar)
- Empfohlene Maßnahme
- Nicht enthalten: Glaubwürdigkeitsmethodik, Rechtsrisikoanalyse,
  anwaltliche Eindrücke
- Kopfzeile: „Vertraulich — Nur für HR — Keine Weitergabe"
- Keine Eintrags-IDs oder Dokumentenverweise

**Geschäftsführung / Aufsichtsrat** (für Governance-Entscheidung):
- Vorwurf und Umfang in einem Abschnitt
- Wesentliche Ergebnisse
- Unternehmensrelevanz / Expositionseinschätzung (nur grob — keine Detailrechtsanalyse)
- Ergriffene und geplante Maßnahmen
- Kopfzeile: „Vertraulich — Interne Untersuchung"

**Externe Bevollmächtigte** (für Prozessvorbereitung oder vertiefende Prüfung):
- Vollständiger Kontext einschließlich Rechtsrisikoanalyse
- Offene Beweisstränge
- Ungelöste Glaubwürdigkeitsfragen
- Dokumente mit erhöhter Prozeßrelevanz

---

## Was diese Skill nicht tut

- Disziplinarische Entscheidungen treffen — sie unterstützt die anwaltlichen
  Feststellungen, nicht die HR-Entscheidung
- Vertraulichkeitsschutz garantieren — Schutz hängt davon ab, wie die
  Untersuchung strukturiert und wie Materialien verteilt wurden
- Dokumente lesen, die technisch nicht verarbeitbar sind — solche Dateien
  für manuelle Prüfung flaggen
- Befragungen durchführen — Befragungsnotizen werden protokolliert,
  nicht selbst geführt
- Anhörungshinweise ersetzen — sie verfolgt, ob sie erteilt wurden,
  erteilt sie nicht selbst

## Quellenpflicht

Bei jeder Ausgabe zu Untersuchungsverfahren zitieren:
- § 26 BDSG (Beschäftigtendatenschutz, Verhältnismäßigkeit)
- § 87 Abs. 1 Nr. 6 BetrVG (Mitbestimmung bei technischer Überwachung)
- BAG, Urt. v. 20.06.2013 – 2 AZR 546/12, NZA 2014, 143 (Verdachtskündigung)
- BAG, Urt. v. 23.08.2018 – 2 AZR 133/18, NZA 2018, 1329 (Anhörung)
- Gola/Heckmann/Schomerus, BDSG, 13. Aufl. 2022, § 26 Rn. 120 ff.
- Erfurter Kommentar/Müller-Glöge, 24. Aufl. 2024, § 626 BGB Rn. 165 ff.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
