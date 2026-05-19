---
name: ki-inventar
description: >
  KI-System-Inventar nach EU-KI-VO (VO 2024/1689) – erfasst je KI-System Rolle (Anbieter,
  Betreiber, Einführer, Händler, Bevollmächtigter, Produkthersteller) und Risikoklasse
  (verboten, hochrisiko, begrenzt, minimal, Allzweck-KI, systemisch). Rolle und Klasse
  werden je System bewertet, nicht je Unternehmen. Verwenden, wenn der Nutzer sagt
  „KI-Inventar", „KI-System hinzufügen", „welche Systeme haben wir", „KI-System klassifizieren",
  „KI-VO-Register" oder „KI-System-Verzeichnis".
argument-hint: "[list | add | edit <id> | classify <id> | show <id>]"
triggers:
  - "KI-Inventar"
  - "KI-System"
  - "EU AI Act Register"
  - "KI-VO Klassifizierung"
  - "Risikoklasse"
language: de
---

# /ki-inventar

## Zweck

Dieses Inventar dient der strukturierten Erfassung aller KI-Systeme einer Organisation nach
Art. 6 ff. KI-VO (VO 2024/1689). Der zentrale Grundsatz: **Rolle und Risikoklasse werden
je KI-System bewertet, nicht je Unternehmen.** Eine Organisation kann Anbieter von System A,
Betreiber von System B und Einführer von System C sein. Jede Kombination löst nach der KI-VO
unterschiedliche Pflichten aus (z. B. Art. 16 ff. für Anbieter, Art. 26 für Betreiber).
Verstöße können nach Art. 99 KI-VO mit Bußgeldern bis zu 35 Mio. EUR oder 7 % des weltweiten
Jahresumsatzes geahndet werden. Das Inventar dient als Basis für alle nachgelagerten Pflichten;
die eigentliche Obligationenanalyse erfolgt im Gespräch, nicht aus einer fest codierten Tabelle.

## Eingaben

- Konfiguration aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
- Bestehendes Inventar unter `ki-systeme.yaml` (gleicher Konfigurationspfad)
- Systembeschreibung des Nutzers oder vorhandene Unterlagen (technische Dokumentation, Verträge)

## Ablauf

1. **Konfiguration lesen.** Prüfen, ob das Praxisprofil vorhanden und befüllt ist. Fehlen
   `[PLATZHALTER]`-Marker, Nutzer an `/ki-governance:kaltstart-interview` verweisen.

2. **Inventar lesen.** Liegt unter `ki-systeme.yaml`. Existiert die Datei nicht, bei erstem
   `add`-Befehl mit leerem `systeme:`-Block anlegen.

3. **Befehl ausführen:**
   - Kein Argument oder `list` → Inventartabelle anzeigen (siehe **Listenformat**)
   - `add` → **Aufnahmefluss** starten
   - `edit <id>` → aktuellen Datensatz zeigen, Änderungsfrage stellen, ein Feld ändern,
     bestätigen, schreiben
   - `classify <id>` → **Klassifizierungsdurchlauf** für bestehenden Datensatz starten,
     `rolle`, `klasse`, `rollenbasis` und `klassenbasis` aktualisieren
   - `show <id>` → vollständigen Datensatz anzeigen

4. **Nach `list` Dashboard anbieten:**
   „Dashboard gewünscht? Filterbar nach Status / Klasse / EU-Nexus / Eigentümer. Auf Wunsch."

5. **Jede Aktion mit Anschlusshinweis abschließen:**
   > Erfasst. Wenn Sie die Pflichten für dieses System durcharbeiten möchten, fragen Sie
   > einfach – ich führe die Analyse im Gespräch durch und markiere, wo die Artikel-Zuordnung
   > Ihre Verifizierung erfordert. Pflichten werden nicht aus einer Tabelle abgeleitet, weil
   > die Zuordnung komplex und die KI-VO noch in der Einführungsphase (bis 2027) ist.

## Listenformat

Kompakte Tabelle:

| ID | Name | Eigentümer | Status | EU-Nexus | Rolle | Klasse | Nächste Prüfung |
|----|------|-----------|--------|----------|-------|--------|-----------------|
| sys-001 | Lebenslauf-Screening | HR / Schmidt | in_produktion | ja | Betreiber | hochrisiko | 2026-08-01 |
| sys-002 | E-Mail-Drafting-Assistent | IT / Meier | in_produktion | nein | Betreiber | begrenzt | 2026-12-01 |

Unter der Tabelle: Zählung nach Klasse und: „N Systeme zur Prüfung innerhalb von 30 Tagen."
Außerdem: Bußgeldrahmen kurz einblenden: Art. 99 Abs. 3 KI-VO – bis 35 Mio. EUR oder 7 %
des weltweiten Jahresumsatzes bei schwerwiegenden Verstößen `[gegen aktuellen KI-VO-Text prüfen]`.

## Aufnahmefluss (Interview)

Felder einzeln abfragen (oder Einfügen akzeptieren). Pflichtfelder: `name`, `eigentümer`,
`beschreibung`, `status`, `eu_nexus`. Rest kann zurückgestellt werden – explizit darauf
hinweisen: „Sie können die Klassifizierung mit `/ki-governance:ki-inventar classify <id>`
nachholen."

1. **Name.** Kurzbezeichnung des Systems.
2. **Eigentümer.** Person oder Team, das täglich für das System verantwortlich ist.
3. **Beschreibung.** Ein bis zwei Sätze: Was tut es, und mit welchen Daten?
4. **Status.** `geplant | in_entwicklung | in_produktion | ausgemustert`
5. **EU-Nexus.** Wird das System in der EU/EWR betrieben, EU/EWR-Nutzern angeboten oder
   erzeugt es Ausgaben, die Personen in der EU/EWR betreffen? Wenn ja, gilt die KI-VO.
   Transparenzpflichten nach Art. 50 KI-VO beachten (z. B. Offenlegung bei Chatbots,
   Deepfake-Kennzeichnung).
6. **Klassifizierung jetzt?** Anbieten, den Durchlauf sofort zu starten oder zurückzustellen.

ID vergeben: `sys-NNN` (nächste aufsteigende Nummer in der Datei).

## Klassifizierungsdurchlauf

Der Durchlauf ergibt `rolle`, `rollenbasis`, `klasse`, `klassenbasis`. Beide Begründungen
werden markiert `[gegen aktuellen KI-VO-Text prüfen]` – nicht als Absicherung, sondern weil
die Artikel-Zuordnung komplex ist und die KI-VO noch in der Einführungsphase ist. Der Anwalt
trägt die Verantwortung für die Verifizierung.

### Schritt 1: Rolle

> **Wer macht was mit diesem System?**

Optionen mit unterscheidendem Merkmal:

- **Anbieter (Art. 3 Nr. 3 KI-VO)** – Sie entwickeln das KI-System (oder lassen es entwickeln)
  und bringen es unter eigenem Namen oder Warenzeichen auf den EU-Markt oder in Betrieb.
- **Betreiber (Art. 3 Nr. 4 KI-VO)** – Sie nutzen das KI-System in eigener Verantwortung,
  nicht zu rein persönlichen nicht-beruflichen Zwecken. (Häufigster Fall innerhalb von
  Unternehmen.) Betreiberpflichten: Art. 26 KI-VO.
- **Einführer (Art. 3 Nr. 6 KI-VO)** – Sie bringen ein KI-System aus einem Nicht-EU-Anbieter
  in die EU/EWR.
- **Händler (Art. 3 Nr. 7 KI-VO)** – Sie machen ein KI-System auf dem EU-Markt verfügbar,
  ohne Anbieter oder Einführer zu sein.
- **Bevollmächtigter (Art. 3 Nr. 5 KI-VO)** – Sie handeln im Auftrag eines Nicht-EU-Anbieters
  und sind in der EU/EWR ansässig.
- **Produkthersteller (Art. 3 Nr. 15 KI-VO)** – Sie integrieren ein KI-System in ein Produkt
  unter eigenem Namen/Warenzeichen. Werden wie ein Anbieter behandelt.

**Doppelrollen-Flag.** Wenn der Nutzer ein Anbieter-System wesentlich ändert (Fine-Tuning auf
eigenen Daten, Änderung des vorgesehenen Verwendungszwecks, Rebranding), kann er zum
**Anbieter** des geänderten Systems werden – auch wenn er als Betreiber begann. Hinweis
geben, wann immer eine Änderung über die Konfiguration hinausgeht. `[gegen aktuellen
KI-VO-Text prüfen – Art. 25 KI-VO, Anbieterpflichten und wesentliche Änderung]`

Rolle schreiben. `rollenbasis` in einem Satz schreiben.

### Schritt 2: Risikoklasse

> **Was tut das System, und fällt der Anwendungsfall in eine regulierte Kategorie?**

In dieser Reihenfolge prüfen:

**A. Art. 5 KI-VO – Verbotene Praktiken** `[gegen aktuellen KI-VO-Text prüfen – Art. 5]`

Zusammenfassungen, kein endgültiger Text:
- Unterschwellige oder täuschende Techniken, die das Verhalten wesentlich verzerren
- Ausnutzung von Schwachstellen (Alter, Behinderung, sozioökonomische Lage) zur wesentlichen
  Verhaltensbeeinflussung
- Social Scoring durch öffentliche Stellen mit nachteiligen Folgen
- Echtzeit-Fernidentifizierung biometrischer Merkmale in öffentlich zugänglichen Räumen zur
  Strafverfolgung (enge Ausnahmen)
- Biometrische Kategorisierung zur Ableitung von Rasse, politischen Meinungen,
  Gewerkschaftszugehörigkeit, religiösen oder weltanschaulichen Überzeugungen, Sexualleben
  oder sexueller Orientierung
- Emotionserkennung am Arbeitsplatz oder in Bildungseinrichtungen (Ausnahmen: Medizin, Sicherheit)
- Anlegen von Gesichtserkennungs-Datenbanken durch Scraping aus Internet oder CCTV
- Prädiktive Polizeiarbeit allein auf Basis von Persönlichkeitsmerkmalen

Trifft zu → Klasse ist `verboten`. Anwendungsfall als Stopp markieren und an den
Prohibited-Practice-Ablauf des Governance-Teams übergeben.

**B. Anhang III – Hochrisiko-Bereiche** `[gegen aktuellen KI-VO-Text prüfen – Anhang III]`

1. Biometrische Identifizierung und Kategorisierung
2. Kritische Infrastruktur (digitale Infrastruktur, Straßenverkehr, Wasser, Gas, Heizung,
   Strom)
3. Allgemeine und berufliche Bildung (Zugang, Bewertung, Proctoring, Überwachung auf
   unerlaubtes Verhalten)
4. Beschäftigung, Arbeitnehmerverwaltung, Selbständigkeit – Einstellung, Auswahl, Beförderung,
   Kündigung, Aufgabenzuweisung, Überwachung, Leistung
5. Wesentliche private und öffentliche Dienste (Sozialleistungen, Kreditwürdigkeit natürlicher
   Personen, Risikobewertung und -bepreisung bei Leben-/Krankenversicherung, Notfallmanagement)
6. Strafverfolgung (Risikobewertung, Polygraphie, Deepfake-Erkennung, Zuverlässigkeit von
   Beweisen, Profiling)
7. Migration, Asyl, Grenzkontrolle (Risikobewertung, Reisedokumentenprüfung, Antragsbearbeitung)
8. Justiz und demokratische Prozesse (Recherche und Auslegung, Beeinflussung von Wahlen)

Trifft zu → Klasse ist `hochrisiko`. Anhang-III-Bereich und Unterabschnitt notieren.
Betreiber-Pflichten gemäß Art. 26 KI-VO prüfen; bei öffentlichen Stellen oder öffentlich
finanzierten Diensten gilt Art. 27 KI-VO (FRIA – Folgenabschätzung für Grundrechte).

**C. Allzweck-KI (Art. 51 KI-VO und folgende)** `[gegen aktuellen KI-VO-Text prüfen]`

- **Allzweck-KI:** Auf großen Datenmengen trainiertes Modell, auf Allgemeinheit ausgelegt,
  in der Lage, kompetent eine breite Palette verschiedener Aufgaben zu erfüllen.
- **Allzweck-KI + systemisches Risiko:** Kumulierter Rechenaufwand > 10^25 FLOPs oder von
  der Kommission als systemisch eingestuft.

**D. Begrenzte Risikoklasse.** Chatbots im Kontakt mit natürlichen Personen, Deepfakes,
Emotionserkennung und biometrische Kategorisierung außerhalb des Anwendungsbereichs von
Art. 5 – Transparenzpflichten nach Art. 50 KI-VO gelten.

**E. Minimale Risikoklasse.** Alles andere.

Klasse schreiben. `klassenbasis` in einem Satz schreiben unter Angabe des Artikels oder
Anhang-Eintrags, markiert `[gegen aktuellen KI-VO-Text prüfen]`.

### Schritt 3: Empfehlungen

Drei nächste Schritte anbieten:
1. „Möchten Sie, dass ich die Pflichten für dieses System durcharbeite? Ich mache das im
   Gespräch – keine Tabelle."
2. „Möchten Sie `/ki-governance:ki-folgenabschaetzung` starten, um eine vollständige
   KI-Folgenabschätzung zu erstellen?"
3. „Möchten Sie ein nächstes Prüfdatum setzen? Ich füge es dem Inventar hinzu."

## Datensatzformat

```yaml
systeme:
  - id: sys-001
    name: "Lebenslauf-Screening-Tool"
    eigentümer: "HR / Schmidt"
    beschreibung: "Filtert eingehende Lebensläufe nach Stellenkriterien"
    status: in_produktion          # geplant | in_entwicklung | in_produktion | ausgemustert
    eu_nexus: true                 # betrieben, angeboten oder betrifft Personen in der EU/EWR
    rolle: betreiber               # anbieter | betreiber | einführer | händler | bevollmächtigter | produkthersteller
    rollenbasis: "Wir lizenzieren von AnbieterX und betreiben intern [gegen aktuellen KI-VO-Text prüfen]"
    klasse: hochrisiko             # verboten | hochrisiko | begrenzt | minimal | allzweck | allzweck_systemisch
    klassenbasis: "Anhang III Nr. 4 lit. a – Beschäftigung, Einstellungsauswahl [gegen aktuellen KI-VO-Text prüfen]"
    pflichten_bewertet: false
    pflichten_hinweis: "Zu prüfen als Betreiber eines hochriskanten Systems: menschliche Aufsicht (Art. 14 KI-VO), Eingabedatenqualität, Überwachung, Aufzeichnung, Unterrichtung von Arbeitnehmern, FRIA wenn öffentliche Stelle/Dienst (Art. 27 KI-VO) [gegen aktuellen KI-VO-Text prüfen]"
    art50_transparenz: "Offenlegungspflicht prüfen (Art. 50 KI-VO) [prüfen]"
    naechste_pruefung: "2026-08-01"
    pruef_ausloeser: "bei wesentlicher Änderung oder jährlich"
    erstellt: "2026-05-18"
    aktualisiert: "2026-05-18"
```

## Quellen und Zitierweise

Verbindliche Zitierweise gemäß `../references/zitierweise.md`.

**Leitende Normen:**
- Art. 3 Nr. 3, 4, 5, 6, 7 KI-VO (VO 2024/1689) – Definitionen `[Primärquelle – EUR-Lex]`
- Art. 5 KI-VO – Verbotene Praktiken `[Primärquelle – EUR-Lex]`
- Art. 6 KI-VO i.V.m. Anhang III – Hochrisiko-KI-Systeme `[Primärquelle – EUR-Lex]`
- Art. 14, 16, 26 KI-VO – Betreiber- und Anbieterpflichten `[Primärquelle – EUR-Lex]`
- Art. 27 KI-VO – Folgenabschätzung für Grundrechte (FRIA) `[Primärquelle – EUR-Lex]`
- Art. 50 KI-VO – Transparenzpflichten `[Primärquelle – EUR-Lex]`
- Art. 99 KI-VO – Bußgeldrahmen `[Primärquelle – EUR-Lex]`

## Ausgabeformat

- **List:** Kompakte Inventartabelle mit Zählung nach Klasse und 30-Tage-Flag
- **Add/Edit/Classify:** YAML-Datensatz + Durchlauf-Protokoll im Gespräch
- **Show:** Vollständiger Datensatz mit allen Feldern

## Beispiel

```
/ki-governance:ki-inventar classify sys-001
```

> **Klassifizierungsdurchlauf – sys-001: Lebenslauf-Screening-Tool**
>
> **Schritt 1: Rolle**
> Sie lizenzieren das System von VendorX und setzen es intern für HR ein. Sie bestimmen den
> Verwendungszweck und tragen die operative Verantwortung → **Betreiber** nach Art. 3 Nr. 4
> KI-VO `[gegen aktuellen KI-VO-Text prüfen]`.
> Rollenbasis: „Lizenziertes System von VendorX, interner Betrieb durch HR-Team."
>
> **Schritt 2: Risikoklasse**
> Kein Treffer in Art. 5 (kein Verbot erkennbar).
> Anhang III Nr. 4 lit. a: KI-Systeme für Einstellung, Auswahl, Beförderung → **hochrisiko**
> `[gegen aktuellen KI-VO-Text prüfen]`.
> Klassenbasis: „Anhang III Nr. 4 lit. a KI-VO – Einstellungsauswahl."
>
> **Empfehlungen:**
> 1. Pflichten als Betreiber eines hochriskanten Systems durcharbeiten? (Art. 26, 14 KI-VO)
> 2. KI-Folgenabschätzung erstellen? `/ki-governance:ki-folgenabschaetzung`
> 3. Nächstes Prüfdatum: 2027-05-18 (Jahresprüfung)?

## Risiken / typische Fehler

- **Stille Klassifizierung.** Klassifizierungsdurchlauf muss sichtbar sein; kein Auto-Klassifizieren
  aus einer Systembeschreibung.
- **`[prüfen]`-Markierungen entfernen.** Diese sind kein Hedge, sondern der Mechanismus.
  Nicht in Ausgaben entfernen.
- **Wesentliche Änderung ignorieren.** Wenn ein System über die Konfiguration hinaus geändert
  wird, `/ki-inventar classify` erneut ausführen – Änderungen können die Rolle verschieben.
- **Pflichten aus Tabelle ableiten.** Bei Anfragen die Analyse im Gespräch durchführen und
  an `/ki-folgenabschaetzung` für alles weiterleiten, das einen formellen Nachweis benötigt.
- **Art. 99 KI-VO unterschätzen.** Bußgeldrahmen von bis zu 35 Mio. EUR oder 7 % des
  weltweiten Jahresumsatzes nicht als theoretisch behandeln – im Kontext jeder Klassifizierung
  erwähnen. `[Modellwissen – prüfen]`
